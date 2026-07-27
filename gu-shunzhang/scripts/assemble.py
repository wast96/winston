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

SHORT_RATIO = 0.82   # of the median full line; below this the line ends a para


def load_pages(first, last):
    stream = []
    for n in range(first, last + 1):
        p = os.path.join(TXT, "p%04d.txt" % n)
        if not os.path.exists(p):
            continue
        for l in open(p).read().split("\n"):
            stream.append((n, l))
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
    a = ap.parse_args()

    os.makedirs(ZH, exist_ok=True)
    structure = json.load(open(a.structure)) if os.path.exists(a.structure) else []
    heads = heading_set(structure, a.first, a.last)
    head_titles = {e["title"] for es in heads.values() for e in es}

    stream = load_pages(a.first, a.last)
    lens = [len(l) for _, l in stream if l.strip()]
    if not lens:
        raise SystemExit("no text in range")
    lens.sort()
    measure = lens[int(len(lens) * 0.75)]      # upper quartile = the full measure
    cutoff = a.short_ratio * measure

    paras, cur = [], []
    for page, line in stream:
        s = line.strip()
        if not s:
            if cur:
                paras.append("".join(cur))
                cur = []
            continue
        if s in head_titles:
            if cur:
                paras.append("".join(cur))
                cur = []
            paras.append("### " + s)
            continue
        cur.append(s)
        if len(s) < cutoff:
            paras.append("".join(cur))
            cur = []
    if cur:
        paras.append("".join(cur))

    paras = [p for p in paras if p.strip()]
    dest = os.path.join(ZH, "%s.txt" % a.chapter)
    with open(dest, "w") as fh:
        fh.write("\n".join(paras) + "\n")

    body = [p for p in paras if not p.startswith("###")]
    chars = sum(len(re.findall(r"[一-鿿]", p)) for p in body)
    print("%s: PDF %d-%d, measure %d, cutoff %.1f" % (a.chapter, a.first, a.last,
                                                      measure, cutoff))
    print("  %d paragraphs (%d headings), %d CJK chars, mean para %d chars"
          % (len(body), len(paras) - len(body), chars,
             chars // max(1, len(body))))


if __name__ == "__main__":
    main()
