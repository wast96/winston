#!/usr/bin/env python3
"""Assemble per-page OCR into a per-chapter source file, one paragraph a line.

Paragraph reconstruction uses two signals, because neither alone is enough:

  1. BLANK LINE. tesseract emits an empty line where a paragraph ends. This
     is the strongest signal and the reason ocr_crop.py preserves blanks.
  2. SHORT LINE. The source is justified, so every line is the full measure
     EXCEPT the last line of a paragraph. A line materially shorter than the
     chapter's median therefore ends a paragraph.

Signal 2 covers what signal 1 misses at page boundaries, where the blank
falls off the end of the page. Signal 1 covers what signal 2 misses when a
paragraph happens to end flush with the measure. Neither is discarded.

Headings are passed in from data/structure.json and emitted as '### ' lines
so the translation can carry the same structure and the parity check can
skip them.

Usage: assemble.py CHAPTER_ID FIRST_PDF LAST_PDF [--structure data/structure.json]
Writes: data/zh/CHAPTER_ID.txt
"""
import argparse
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TXT = os.path.join(ROOT, "data", "txt")
ZH = os.path.join(ROOT, "data", "zh")
PAGEMAP = os.path.join(ROOT, "data", "pagemap")
INDENT = os.path.join(ROOT, "data", "indent")

SHORT_RATIO = 0.82   # of the median full line; below this the line ends a para

# A paragraph break in Chinese prose always follows sentence-final punctuation.
# Whatever signal proposes a break -- indent, blank line, short line -- it is
# wrong if the text so far does not end on one of these, because no paragraph
# ends in the middle of a sentence. This single test removed every false split
# the indent measurement produced: all of them opened mid-sentence, at a page
# top, where a continuation line's offset had been misread as an indent.
SENT_END = "。！？…"
# Closing quotes and brackets may follow the stop, so they are stripped before
# the test rather than counted as ends themselves. Counting ')' as a sentence
# end let a stray OCR bracket authorise a break in mid-sentence.
SENT_CLOSERS = "”’』」》）)\"' 　"


def load_pages(first, last):
    """Stream of (page, line, starts_paragraph).

    starts_paragraph comes from the printed INDENT, measured off the page
    image by indents.py, and it is the authoritative signal: it is the mark
    the typesetter actually made. The two older signals are kept only as
    fallbacks where no indent data exists, because each fails in a way this
    one does not -- tesseract's blank line is absent across page breaks, and
    the short-last-line rule reports a false paragraph end at the foot of
    every page whose text block happens to end there.
    """
    stream = []
    for n in range(first, last + 1):
        p = os.path.join(TXT, "p%04d.txt" % n)
        if not os.path.exists(p):
            continue
        ip = os.path.join(INDENT, "p%04d.json" % n)
        flags = json.load(open(ip)) if os.path.exists(ip) else None
        raw = open(p).read().split("\n")
        k = 0
        for l in raw:
            if l.strip():
                f = flags[k] if (flags and k < len(flags)) else None
                k += 1
            else:
                f = None
            stream.append((n, l, f))
        # NO forced break at the page end. A paragraph runs across the page
        # boundary far more often than it stops there, and forcing a break
        # here split 21 paragraphs in the first chapter alone, leaving
        # orphan tails like a three-character line standing as its own
        # paragraph. Whether the paragraph continues is already decided by
        # the short-line test on the page's own last line.
    return stream


def heading_set(structure, first, last):
    """Exact heading strings expected in this range, by page."""
    heads = {}
    for e in structure:
        if first <= e["pdf"] <= last:
            heads.setdefault(e["pdf"], []).append(e)
    return heads


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter")
    ap.add_argument("first", type=int)
    ap.add_argument("last", type=int)
    ap.add_argument("--structure",
                    default=os.path.join(ROOT, "data", "structure.json"))
    ap.add_argument("--short-ratio", type=float, default=SHORT_RATIO)
    ap.add_argument("--offset", type=int, default=19,
                    help="PDF page minus printed page. 19 for the main text, "
                         "5 for the front matter, which carries its own "
                         "numbering sequence")
    a = ap.parse_args()

    os.makedirs(ZH, exist_ok=True)
    structure = json.load(open(a.structure)) if os.path.exists(a.structure) else []
    heads = heading_set(structure, a.first, a.last)
    head_titles = {e["title"] for es in heads.values() for e in es}

    stream = load_pages(a.first, a.last)
    have_indents = any(f is not None for _, _, f in stream)
    lens = [len(l) for _, l, _ in stream if l.strip()]
    if not lens:
        raise SystemExit("no text in range")
    lens.sort()
    measure = lens[int(len(lens) * 0.75)]      # upper quartile = the full measure
    cutoff = a.short_ratio * measure

    # Track which printed page each paragraph STARTS on, so the EPUB can
    # carry page-break markers for citation. A printed page nearly always
    # begins mid-paragraph; the marker is therefore placed at the paragraph
    # boundary at or after the page turn, which is the best a translation can
    # honestly do -- English word order does not preserve where a Chinese page
    # broke. Recorded as "the page begins at or before this paragraph".
    paras, cur, cur_page = [], [], None
    starts = []          # (printed_page, index into paras)
    seen_pages = set()

    def can_break():
        """True if the accumulated text ends a sentence.

        Trailing characters that are neither Han nor a sentence stop are
        stripped first. Closing quotes legitimately follow the stop, and OCR
        noise does too: a stray '|' left after a full stop was enough to make
        this return False and suppress a real paragraph break, which then slid
        the whole chapter out of alignment with its translation.
        """
        if not cur:
            return False
        s = cur[-1].rstrip()
        while s and s[-1] not in SENT_END and not re.match(r"[一-鿿]", s[-1]):
            s = s[:-1]
        return bool(s) and s[-1] in SENT_END

    def flush():
        if cur:
            paras.append("".join(cur))
            cur.clear()

    # Which stream positions are the first non-blank line of their page: the
    # one place the indent flag cannot be trusted, because a page-top line's
    # offset is measured against a margin estimated from that page alone and
    # scanner skew reads as an indent. There the older signal is sound
    # instead -- if the PREVIOUS page ended on a short line, the paragraph
    # ended with it. Inside a page the indent is authoritative and the
    # short-line rule is wrong, because a page's last line is short whenever
    # the text block ends there.
    first_of_page, seen = set(), set()
    for idx, (page, line, _) in enumerate(stream):
        if line.strip() and page not in seen:
            seen.add(page)
            first_of_page.add(idx)

    for idx, (page, line, indented) in enumerate(stream):
        s = line.strip()
        if not s:
            if not have_indents:
                flush()
            continue
        if s in head_titles:
            flush()
            if page not in seen_pages:
                seen_pages.add(page)
                starts.append((page, len(paras)))
            paras.append("### " + s)
            continue
        # THE INDENT ALONE, gated by the sentence-end test.
        #
        # The detector was checked against the pages themselves rather than
        # against paragraph counts: on two sample pages it flagged six indents
        # of six and three of three, with no false positives. It is exact, and
        # propping it up with the short-line rule -- which was added when the
        # counts disagreed -- only put back the page-foot over-splitting the
        # indent exists to avoid. Every extra break the short-line rule
        # contributed was a false one.
        #
        # The page-top suppression is gone for the same reason: it was there
        # because the indent was not trusted, and it silently lost every
        # paragraph that genuinely opens at the head of a page.
        if can_break() and indented:
            flush()
        if not cur:
            cur_page = page
            if page not in seen_pages:
                seen_pages.add(page)
                starts.append((page, len(paras)))
        cur.append(s)
    flush()

    paras = [p for p in paras if p.strip()]
    dest = os.path.join(ZH, "%s.txt" % a.chapter)
    with open(dest, "w") as fh:
        fh.write("\n".join(paras) + "\n")

    # re-express page starts as indices into the BODY paragraph list, which is
    # what the builder walks and what parity counts
    body_index, mapping = {}, []
    b = 0
    for i, para in enumerate(paras):
        body_index[i] = b
        if not para.startswith("###"):
            b += 1
    for page, idx in starts:
        mapping.append({"printed": page - a.offset,
                        "pdf": page,
                        "body_paragraph": body_index.get(idx, 0)})
    os.makedirs(PAGEMAP, exist_ok=True)
    with open(os.path.join(PAGEMAP, "%s.json" % a.chapter), "w") as fh:
        json.dump(mapping, fh, ensure_ascii=False, indent=1)

    body = [p for p in paras if not p.startswith("###")]
    chars = sum(len(re.findall(r"[一-鿿]", p)) for p in body)
    print("%s: PDF %d-%d, measure %d, cutoff %.1f" % (a.chapter, a.first, a.last,
                                                      measure, cutoff))
    print("  %d paragraphs (%d headings), %d CJK chars, mean para %d chars"
          % (len(body), len(paras) - len(body), chars,
             chars // max(1, len(body))))
    print("  page map: %d printed pages, %s-%s"
          % (len(mapping), mapping[0]["printed"] if mapping else "-",
             mapping[-1]["printed"] if mapping else "-"))


if __name__ == "__main__":
    main()
