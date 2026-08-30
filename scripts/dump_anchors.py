#!/usr/bin/env python3
"""List every in-text reference mark of a chapter IN READING ORDER, with the
prose that immediately precedes it, so the author-note anchors can be resolved
against out/<id>_reading.md without guessing.

Isaacs marks his citations two ways: a 5.5pt superscript digit (his numbered
endnote) and a full-size inline asterisk (a page-foot footnote). This walks the
body AND set-off block-quote spans in the same reading order the extractor uses
(so the marks come out in the order the builder will number them), and for each
mark prints its kind -- endnote NUMBER or '*' -- and the ~60 characters of
running prose before it. Superscript digits and asterisks are NOT counted into
that preceding prose (they are markers, not text).

Usage: dump_anchors.py <chid>
"""
import json
import os
import sys
import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from extract_isaacs import classify  # noqa: E402  (shared block classifier)

PDF = os.path.join(ROOT, "source.pdf")


def main(chid):
    book = json.load(open(os.path.join(ROOT, "book.json")))
    nodes = book["structure"]
    node = next(c for c in nodes if c["id"] == chid)
    idx = nodes.index(node)
    pdf_start = node["pdf_page"]
    pdf_end = (nodes[idx + 1]["pdf_page"] - 1) if idx + 1 < len(nodes) \
        else book["pdf_end"]

    doc = pymupdf.open(PDF)
    prose = []            # running prose characters (marks excluded)
    marks = []            # (kind, preceding_tail)
    for pnum in range(pdf_start, pdf_end + 1):
        page = doc[pnum - 1]
        blocks = [b for b in page.get_text("dict")["blocks"] if "lines" in b]
        blocks.sort(key=lambda b: b["bbox"][1])
        for b in blocks:
            if classify(b) not in ("body", "quote"):
                continue
            for l in b["lines"]:
                for s in l["spans"]:
                    if s["flags"] & 1:                 # superscript endnote mark
                        if s["text"].strip():
                            tail = "".join(prose)[-60:].replace("\n", " ")
                            marks.append((s["text"].strip(), tail))
                        continue
                    t = s["text"]
                    while "*" in t:                    # inline asterisk footnote
                        pre, t = t.split("*", 1)
                        prose.append(pre)
                        tail = "".join(prose)[-60:].replace("\n", " ")
                        marks.append(("*", tail))
                    prose.append(t)
    doc.close()

    print("=== %s: %d in-text reference marks (reading order) ===" %
          (chid, len(marks)))
    for i, (kind, tail) in enumerate(marks, 1):
        print("%3d  [%s]  ...%s" % (i, kind, tail))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1])
