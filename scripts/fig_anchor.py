#!/usr/bin/env python3
"""Compute the 'before' anchor for a figure, from its printed page.

A figure is placed at the top of the printed page it appears on: the anchor
is the opening of that page's first body paragraph in the reading .md. The
page-to-paragraph map is data/pagemap/<unit>.json (the same one the builder
uses for pagebreak markers), and body paragraphs are counted EXACTLY as the
builder counts them (see render_body): non-empty lines that are not headings
(#..####), not the '***' scene break; a {v}/{d}/{g}/{p} set-off marker is
stripped and the line still counts.

Usage:
  fig_anchor.py UNIT PRINTED_PAGE [--chars 48]      -> prints the anchor
  fig_anchor.py UNIT --list                          -> printed page -> anchor
"""
import argparse
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGEMAP = os.path.join(ROOT, "data", "pagemap")
OUT = os.path.join(ROOT, "out")


def body_paragraphs(unit):
    """Return the list of body-paragraph texts in builder order."""
    md = os.path.join(OUT, "%s_reading.md" % unit)
    paras = []
    for raw in open(md, encoding="utf-8"):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):          # #, ##, ###, #### headings
            continue
        if line == "***":
            continue
        m = re.match(r"^\{([vdgp])\} ", line)
        if m:
            line = line[4:]
        paras.append(line)
    return paras


def page_to_bp(unit):
    pm = json.load(open(os.path.join(PAGEMAP, "%s.json" % unit)))
    return {e["printed"]: e["body_paragraph"] for e in pm}


def anchor_for(unit, printed, chars=48):
    paras = body_paragraphs(unit)
    bp = page_to_bp(unit).get(printed)
    if bp is None:
        return None
    if bp >= len(paras):
        bp = len(paras) - 1
    return paras[bp][:chars]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("unit")
    ap.add_argument("printed", nargs="?", type=int)
    ap.add_argument("--chars", type=int, default=48)
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    if a.list:
        p2b = page_to_bp(a.unit)
        for pr in sorted(p2b):
            print(pr, "->", anchor_for(a.unit, pr, a.chars))
    else:
        print(anchor_for(a.unit, a.printed, a.chars))


if __name__ == "__main__":
    main()
