#!/usr/bin/env python3
"""Resolve each in-text reference mark of a chapter to a UNIQUE verbatim anchor
substring of out/<id>_reading.md, ending exactly where the marker belongs.

Method (robust to spacing / de-hyphenation / italic markup differences between
the raw PDF and the reset reading file): reduce both the mark's preceding PDF
prose and the reading file to a lowercase [a-z0-9] stream, with an index map
back to the reading file. Find the reduced tail in the reduced reading stream;
its end maps to a reading-file offset -- the point the marker follows. Then grow
a window backward from that offset until it is a unique substring of the reading
file and starts on a word boundary, avoiding the '*' italic markers.

Writes data/anchors/<id>.json: an ordered list of {kind, value, anchor}, kind
"num" (Isaacs endnote, value = his printed number) or "ast" (asterisk foot
footnote). Consumed by build_ch0203_notes.py.

Usage: anchor_offsets.py <chid> [<chid> ...]
"""
import json
import os
import re
import sys
import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from extract_isaacs import classify  # noqa: E402

PDF = os.path.join(ROOT, "source.pdf")


def reduce_map(text):
    """Return (reduced_stream, index_map) where index_map[k] is the offset in
    `text` of the character that produced reduced_stream[k].

    The single letter of a block-marker prefix ('{q} ', '{v} ', '{d} ', '{g} ',
    '{p} ') is skipped, so it does not inject a stray 'q'/'v'/'d'/'g'/'p' into
    the reduced reading stream. Without this a mark whose preceding-prose probe
    window crosses a set-off paragraph boundary (ch09's signature note 29, after
    the one-line quote '{q} Chen.') would not be found: '...wang' + 'q' + 'chen'
    breaks the 'signedwangchen' probe. The PDF prose stream has no '{X}'
    sequences, so this guard is a no-op there."""
    red, imap = [], []
    for i, ch in enumerate(text):
        c = ch.lower()
        if c in "qvdgp" and i > 0 and text[i - 1] == "{" \
                and i + 1 < len(text) and text[i + 1] == "}":
            continue                     # the letter of a '{q} ' block marker
        if ("a" <= c <= "z") or ("0" <= c <= "9"):
            red.append(c)
            imap.append(i)
    return "".join(red), imap


def reading_text(chid):
    path = os.path.join(ROOT, "out", "%s_reading.md" % chid)
    return open(path, encoding="utf-8").read()


def marks_with_tails(chid):
    """Every reference mark in reading order with the raw PDF prose before it."""
    book = json.load(open(os.path.join(ROOT, "book.json")))
    nodes = book["structure"]
    node = next(c for c in nodes if c["id"] == chid)
    idx = nodes.index(node)
    pdf_start = node["pdf_page"]
    pdf_end = (nodes[idx + 1]["pdf_page"] - 1) if idx + 1 < len(nodes) \
        else book["pdf_end"]
    doc = pymupdf.open(PDF)
    prose, marks = [], []
    for pnum in range(pdf_start, pdf_end + 1):
        blocks = [b for b in doc[pnum - 1].get_text("dict")["blocks"]
                  if "lines" in b]
        blocks.sort(key=lambda b: b["bbox"][1])
        for b in blocks:
            if classify(b) not in ("body", "quote"):
                continue
            for l in b["lines"]:
                for s in l["spans"]:
                    if s["flags"] & 1:
                        if s["text"].strip():
                            marks.append(("num", s["text"].strip(),
                                          "".join(prose)))
                        continue
                    t = s["text"]
                    while "*" in t:
                        pre, t = t.split("*", 1)
                        prose.append(pre)
                        marks.append(("ast", None, "".join(prose)))
                    prose.append(t)
    doc.close()
    # Collapse a run of consecutive asterisks (Isaacs's ** is the SECOND
    # page-foot footnote symbol on a page, *** the third): the run is ONE
    # reference mark, not several. Consecutive 'ast' marks carry identical
    # preceding prose (the second asterisk adds no text between them), so a
    # same-prose 'ast' immediately after an 'ast' is a continuation glyph and
    # is dropped. Two DISTINCT footnote references always have intervening
    # prose, so their tails differ and neither is merged.
    merged = []
    for m in marks:
        if (m[0] == "ast" and merged and merged[-1][0] == "ast"
                and merged[-1][2] == m[2]):
            continue
        merged.append(m)
    return merged


def resolve(chid):
    R = reading_text(chid)
    Rr, imap = reduce_map(R)
    marks = marks_with_tails(chid)
    out = []
    used_ends = set()
    for kind, value, tail in marks:
        tr, _ = reduce_map(tail)
        probe = tr[-40:]                # last 40 reduced chars before the mark
        # the mark falls after the LAST occurrence of this prose run
        pos = Rr.rfind(probe)
        if pos < 0:
            sys.exit("%s: tail not found in reading: ...%r" % (chid, tail[-50:]))
        red_end = pos + len(probe)       # reduced index just past the anchor
        if red_end in used_ends:
            sys.exit("%s: duplicate mark end at reduced %d" % (chid, red_end))
        used_ends.add(red_end)
        end_char = imap[red_end - 1] + 1  # reading-file offset after the anchor
        # absorb the closing punctuation the mark actually follows (Isaacs sets
        # his reference marks after the period/quote), so the marker lands there
        # A closing italic '*' marker is transparent here: step over it so the
        # anchor ends after the whole italicized term (and any punctuation that
        # follows it), placing the note marker where Isaacs set his reference
        # mark -- after '*hsien*.' not inside it.
        while end_char < len(R) and R[end_char] in ".,;:!?”’\")*":
            end_char += 1
        # grow the window backward until unique and word-boundary clean.
        # Prefer an anchor free of '*' italic markers, but fall back to a
        # unique anchor that DOES contain complete italic runs -- the builder
        # inserts anchors BEFORE markup substitution, so a '*term*' anchor is
        # safe (STYLE.local Batch 2 ruling). Needed when the mark falls right
        # after an italicized term (e.g. six or seven *hsien*).
        red_lo = red_end - 12
        fallback = None
        while red_lo > 0:
            start_char = imap[red_lo]
            # snap to a word start (previous char is a space/quote/paren)
            while start_char > 0 and R[start_char - 1] not in " \t\n“”‘’\"'([":
                start_char -= 1
            anchor = R[start_char:end_char]
            if R.count(anchor) == 1:
                if "*" not in anchor:
                    break
                if fallback is None:
                    fallback = anchor
            red_lo -= 4
        else:
            if fallback is not None:
                anchor = fallback
            else:
                sys.exit("%s: could not make unique anchor before %d"
                         % (chid, red_end))
        out.append({"kind": kind, "value": value, "anchor": anchor})
    return out


def main(chids):
    dest = os.path.join(ROOT, "data", "anchors")
    os.makedirs(dest, exist_ok=True)
    for chid in chids:
        res = resolve(chid)
        nnum = sum(1 for r in res if r["kind"] == "num")
        nast = sum(1 for r in res if r["kind"] == "ast")
        path = os.path.join(dest, "%s.json" % chid)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(res, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        print("%s: %d marks (%d endnote, %d asterisk) -> %s"
              % (chid, len(res), nnum, nast, path))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
