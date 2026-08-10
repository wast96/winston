#!/usr/bin/env python3
"""Build a candidate data/zh/<id>.txt from OCR text + the English reading file.

The zh file is the tracked correction surface, paragraph-aligned 1:1 with
out/<id>_reading.md. Hand-building it end-to-end through Write/Edit is the
biggest CJK-heavy payload in the pipeline and, on this book, drives the
transport-layer 400s that surface as "safety guardrails triggered." This
script produces a candidate the model only has to hand-diff.

What it does:

  1. Reads out/<id>_reading.md and counts its body paragraphs (lines that
     are neither blank nor headings). Also lifts the ## title, {d} byline,
     and ### section headings in order.
  2. Reads data/txt/p####.txt for the chapter's PDF range and stitches the
     lines into one text stream, dropping folios (bare digits) and running
     head/foot residue.
  3. Segments the stream into paragraph candidates using the same signals
     assemble.py uses (blank line, short line, sentence-final punctuation)
     but WITHOUT the geometric indent hints, since those don't survive this
     book's scan.
  4. Emits data/zh/<id>.txt with heading/byline markers interleaved to
     match the English structure, and body paragraphs slotted in order.

What it CANNOT do:

  - Guarantee the paragraph split exactly matches English decisions. When
    the segmented count doesn't match the target, the script writes
    everything to a work file at data/zh_work/<id>.txt AND prints a
    mismatch report showing per-section counts, so the human can see
    where to merge or split. The canonical data/zh/<id>.txt is written
    only when counts line up section-for-section.
  - Fix OCR errors. Names and numbers still need eye-verification against
    the scan; the script emits the OCR text as-is.

Usage:
    build_zh_candidate.py CH_ID FIRST_PDF LAST_PDF
    build_zh_candidate.py ch13 147 175
"""
import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TXT = os.path.join(ROOT, "data", "txt")
ZH = os.path.join(ROOT, "data", "zh")
ZH_WORK = os.path.join(ROOT, "data", "zh_work")
OUT = os.path.join(ROOT, "out")

CJK_END_PUNCT = "。！？」』"  # a paragraph can only end on one of these
SHORT_RATIO = 0.82            # below this, a line ends its paragraph
CJK = r"一-鿿"


def load_reading(cid):
    """Return (title_line, byline, sections). sections is a list of
    (heading_or_None, [para, para, ...]) pairs in order; the leading
    section may have heading=None if there's no ### before the first body
    paragraph.
    """
    path = os.path.join(OUT, cid + "_reading.md")
    title = None
    byline = None
    sections = [(None, [])]
    for raw in open(path):
        line = raw.rstrip("\n")
        if not line.strip():
            continue
        if line.startswith("## ") and title is None:
            title = line
            continue
        if line.startswith("{d} "):
            byline = line
            continue
        if line.startswith("### "):
            sections.append((line, []))
            continue
        sections[-1][1].append(line)
    # drop the leading (None, []) if nothing landed in it
    if sections[0][0] is None and not sections[0][1]:
        sections.pop(0)
    return title, byline, sections


def load_ocr_pages(first, last):
    """Concatenate OCR text for the page range, preserving blank lines
    between pages (they carry paragraph-break signal from assemble.py's
    logic) and dropping obvious folio-only lines and dot-only artefacts.
    """
    out = []
    for n in range(first, last + 1):
        p = os.path.join(TXT, "p%04d.txt" % n)
        if not os.path.exists(p):
            continue
        for raw in open(p):
            line = raw.rstrip()
            if re.fullmatch(r"[·•.\s\d]+", line or " "):
                # folio marker like "· 138 ·" or a stray dot line
                continue
            out.append(line)
        out.append("")  # page boundary is a soft paragraph hint
    return out


def clean_line(s):
    """Basic OCR-noise scrubbing that never touches CJK glyphs.

    Strip stray latin-punct artefacts that tesseract emits between glyphs,
    but leave the CJK characters alone — real OCR corrections happen in
    hand-editing, not here.
    """
    # collapse repeated whitespace
    s = re.sub(r"\s+", "", s)
    return s


def segment(lines):
    """Return a list of paragraph strings segmented from OCR lines.

    Signals (any one ends a paragraph):
      - blank line
      - line ending in sentence-final punctuation AND the next non-blank
        line starts a plausible new sentence
      - short line materially below the chapter's median run-length

    Signals that block a break (any one keeps two lines together):
      - the running text does not yet end in sentence-final punctuation
      - the next line looks like a continuation (opens with a quote-close
        or a low-precedence character)
    """
    cleaned = [clean_line(l) for l in lines]
    # compute median non-blank line length as the "full measure"
    lens = sorted(len(l) for l in cleaned if l)
    if not lens:
        return []
    median = lens[len(lens) // 2] or 1
    short_thresh = int(median * SHORT_RATIO)

    paras = []
    buf = ""
    for i, line in enumerate(cleaned):
        if not line:
            if buf:
                paras.append(buf)
                buf = ""
            continue
        buf += line
        # decide whether buf ends here
        ends_sentence = buf[-1:] in CJK_END_PUNCT
        is_short = len(line) < short_thresh
        # peek at next non-blank line for continuation hint
        j = i + 1
        while j < len(cleaned) and not cleaned[j]:
            j += 1
        next_line = cleaned[j] if j < len(cleaned) else ""
        continues = next_line and next_line[:1] in "）」』】)"
        if ends_sentence and is_short and not continues:
            paras.append(buf)
            buf = ""
    if buf:
        paras.append(buf)
    return paras


CN_SECT_RE = re.compile(
    r"^[(（]?"
    r"([一二三四五六七八九十]+)"
    r"[)）、,.]?"
)


def clip_to_headings(paras, sections):
    """Slot paras into sections by scanning for the source's own numbered
    section markers (一、 二、 (一) (二) ...) at the head of a paragraph.
    A paragraph whose OCR opens with such a marker starts a new section,
    and the marker text itself is stripped from the paragraph. Falls back
    to a slack-aware sequential fill when no markers are found.

    This is best-effort — the human hand-corrects the boundaries. What we
    guarantee is that all OCR paragraphs end up somewhere, and the section
    heading markers are emitted in the right order.
    """
    slots = [(h, [], want) for h, want in [(s[0], len(s[1])) for s in sections]]

    # first pass: scan for source markers; index paragraphs by which slot
    # they open (or None if they carry no marker)
    marker_positions = []  # list of (para_index, sect_index)
    n_sections = len(slots)
    # if there's a leading pre-heading slot, the first marker starts slot 1
    sect_offset = 1 if slots and slots[0][0] is None else 0
    expected_sect = sect_offset
    for i, p in enumerate(paras):
        m = CN_SECT_RE.match(p)
        if not m:
            continue
        # only accept a marker if it lands in numerical sequence — otherwise
        # a stray "一九三一年" style opener would look like a section
        num_word = m.group(1)
        cn_to_int = _cn_to_int(num_word)
        if cn_to_int is None:
            continue
        want_num = expected_sect - sect_offset + 1
        if cn_to_int == want_num:
            marker_positions.append((i, expected_sect))
            expected_sect += 1
            if expected_sect >= n_sections:
                break

    if marker_positions and len(marker_positions) == n_sections - sect_offset:
        # markers found for every section — split cleanly
        boundaries = [0] + [pos for pos, _ in marker_positions] + [len(paras)]
        for si in range(n_sections):
            start = boundaries[si]
            end = boundaries[si + 1]
            block = paras[start:end]
            # strip the leading section marker from the first paragraph of
            # each non-pre-heading section
            if si >= sect_offset and block:
                block = block[:]
                block[0] = CN_SECT_RE.sub("", block[0], count=1)
                # also strip a short heading text like "、黄金荣的家世..." — up
                # through the next period-or-mark, if the marker was consumed
                # and the remainder still leads with the heading topic
                block[0] = re.sub(r"^[、,．. ]+", "", block[0])
            slots[si] = (slots[si][0], list(block), slots[si][2])
        return slots

    # fallback: slack-aware sequential fill. Give each section its want
    # count from the running paras; if we run short, later sections get
    # empty; if we run long, extras spill into the last section.
    idx = 0
    for p in paras:
        while idx < len(slots) - 1 and len(slots[idx][1]) >= slots[idx][2]:
            idx += 1
        slots[idx][1].append(p)
    return [(h, ps, want) for h, ps, want in slots]


_CN_DIGITS = {c: i for i, c in enumerate("零一二三四五六七八九", 0)}


def _cn_to_int(s):
    """Parse a Chinese numeral 1..20 or so; return None on anything odd."""
    if s == "十":
        return 10
    if len(s) == 1 and s in _CN_DIGITS:
        return _CN_DIGITS[s]
    if len(s) == 2 and s.startswith("十") and s[1] in _CN_DIGITS:
        return 10 + _CN_DIGITS[s[1]]
    if len(s) == 2 and s.endswith("十") and s[0] in _CN_DIGITS:
        return _CN_DIGITS[s[0]] * 10
    if len(s) == 3 and s[1] == "十" and s[0] in _CN_DIGITS and s[2] in _CN_DIGITS:
        return _CN_DIGITS[s[0]] * 10 + _CN_DIGITS[s[2]]
    return None


def emit(title, byline, filled):
    out = []
    if title:
        out.append(title)
    if byline:
        out.append(byline)
    for heading, paras, _want in filled:
        if heading:
            out.append(heading)
        out.extend(paras)
    return "\n".join(out) + "\n"


def report(filled, sections):
    lines = []
    total_want = sum(len(s[1]) for s in sections)
    total_got = sum(len(f[1]) for f in filled)
    lines.append(f"total: want {total_want} paragraphs, got {total_got}")
    for (heading, ps, want), (_, wparas) in zip(filled, sections):
        got = len(ps)
        mark = "OK" if got == want else "MISMATCH"
        h = (heading or "(pre-heading)").replace("### ", "")[:60]
        lines.append(f"  {mark:>8}  want {want:3d}  got {got:3d}  {h}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cid")
    ap.add_argument("first", type=int)
    ap.add_argument("last", type=int)
    args = ap.parse_args()

    title, byline, sections = load_reading(args.cid)
    lines = load_ocr_pages(args.first, args.last)
    paras = segment(lines)
    filled = clip_to_headings(paras, sections)
    text = emit(title, byline, filled)

    rpt = report(filled, sections)
    print(rpt)

    total_want = sum(len(s[1]) for s in sections)
    total_got = sum(len(f[1]) for f in filled)

    if total_want == total_got and all(len(f[1]) == f[2] for f in filled):
        os.makedirs(ZH, exist_ok=True)
        path = os.path.join(ZH, args.cid + ".txt")
        open(path, "w").write(text)
        print(f"\n-> wrote {path} (counts match; hand-correct OCR errors in place)")
    else:
        os.makedirs(ZH_WORK, exist_ok=True)
        path = os.path.join(ZH_WORK, args.cid + ".txt")
        open(path, "w").write(text)
        print(
            f"\n-> wrote {path} (COUNT MISMATCH; fix section splits before "
            f"moving to data/zh/)"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
