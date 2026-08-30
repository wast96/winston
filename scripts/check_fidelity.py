#!/usr/bin/env python3
"""Whole-unit fidelity check for the faithful reset (CLAUDE.md rule 4).

Reduce BOTH sides to a letters+digits-only lowercase stream and confirm they
are IDENTICAL, so nothing in Isaacs's prose was dropped, added, or reordered
by extraction and the hand fixes on out/<id>_reading.md:

  - reading side: out/<id>_reading.md, minus the '## ' heading, the '***'
    scene breaks, the '{q} ' block-quote prefixes, and the '*' italic markers;
  - PDF side: the unit's body-prose spans only (drop-cap initial included;
    running heads, folios, the chapter title, the 8pt page-foot footnotes,
    the superscript reference marks, and the ZapfDingbats scene ornaments all
    excluded, exactly as extraction treats them).

Because both streams keep only [a-z0-9], differences of whitespace, hyphen,
quote style, and italic markup cannot cause a false mismatch: a mismatch means
real prose text differs. On a mismatch it prints the first divergence with
context so it can be located.

Usage: check_fidelity.py <chid> [<chid> ...]
"""
import json
import os
import re
import sys
import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, "source.pdf")

BODY_LO, BODY_HI = 9.3, 10.5   # body prose point size
DROP_MIN = 40.0                # drop-cap initial
TITLE_LO, TITLE_HI = 18.0, 30.0  # chapter/section title point size
QUOTE_LO, QUOTE_HI = 8.6, 9.2   # set-off block quotation (smaller type)
QUOTE_X0_LO, QUOTE_X0_HI = 63, 110  # its left indent (matches extract_isaacs)


def reduce(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def dominant_size(block):
    szs = [round(s["size"], 1) for l in block["lines"] for s in l["spans"]
           if s["text"].strip()]
    return max(set(szs), key=szs.count) if szs else 0.0


def is_quote_block(block):
    """A set-off block quotation: smaller type AND indented from the body
    margin, the same geometry gate extract_isaacs uses. Keeps a 9.0pt quote
    while still excluding the 9.0pt running heads and folios at that size."""
    sz = dominant_size(block)
    x0 = block["bbox"][0]
    return QUOTE_LO <= sz <= QUOTE_HI and QUOTE_X0_LO <= x0 <= QUOTE_X0_HI


def reading_stream(chid):
    path = os.path.join(ROOT, "out", "%s_reading.md" % chid)
    out = []
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("#"):
            continue
        if line.strip() == "***":
            continue
        for pre in ("{q} ", "{v} ", "{d} ", "{g} ", "{p} "):
            if line.startswith(pre):
                line = line[len(pre):]
        line = line.replace("*", "")
        out.append(line)
    return reduce("".join(out))


def pdf_stream(chid):
    book = json.load(open(os.path.join(ROOT, "book.json")))
    nodes = book["structure"]
    node = next(c for c in nodes if c["id"] == chid)
    idx = nodes.index(node)
    pdf_start = node["pdf_page"]
    pdf_end = (nodes[idx + 1]["pdf_page"] - 1) if idx + 1 < len(nodes) \
        else book["pdf_end"]
    doc = pymupdf.open(PDF)
    out = []
    for pnum in range(pdf_start, pdf_end + 1):
        page = doc[pnum - 1]
        blocks = [b for b in page.get_text("dict")["blocks"] if "lines" in b]
        blocks.sort(key=lambda b: b["bbox"][1])
        for b in blocks:
            quote = is_quote_block(b)
            for l in b["lines"]:
                for s in l["spans"]:
                    if s["flags"] & 1:            # superscript reference mark
                        continue
                    if "Dingbat" in s["font"] or "Zapf" in s["font"]:
                        continue                  # scene ornament
                    sz = s["size"]
                    # a big display glyph is the drop-cap INITIAL (a letter) --
                    # kept; the giant chapter NUMERAL beside it (100pt, digits
                    # only) is furniture the extractor drops, so exclude it.
                    drop = sz >= DROP_MIN and any(c.isalpha() for c in s["text"])
                    # keep body prose, the drop-cap initial, and set-off block
                    # quotations (smaller type; a whole block decides, not a
                    # per-span size, so a quote's own spans all survive)
                    keep = quote or (BODY_LO <= sz <= BODY_HI) or drop
                    if TITLE_LO <= sz <= TITLE_HI:
                        keep = False              # chapter/section title
                    if not keep:
                        continue
                    out.append(s["text"])
    doc.close()
    return reduce("".join(out))


def main(chids):
    ok = True
    for chid in chids:
        r = reading_stream(chid)
        p = pdf_stream(chid)
        if r == p:
            print("%s: FIDELITY OK (%d chars match)" % (chid, len(r)))
            continue
        ok = False
        print("%s: MISMATCH  reading=%d chars  pdf=%d chars" % (chid, len(r), len(p)))
        n = min(len(r), len(p))
        i = 0
        while i < n and r[i] == p[i]:
            i += 1
        lo = max(0, i - 30)
        print("  first divergence at char %d:" % i)
        print("    reading: ...%s[%s]%s..." % (r[lo:i], r[i:i+1], r[i+1:i+30]))
        print("    pdf    : ...%s[%s]%s..." % (p[lo:i], p[i:i+1], p[i+1:i+30]))
    return 0 if ok else 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1:]))
