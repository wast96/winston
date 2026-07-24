#!/usr/bin/env python3
"""Render PDF pages to PNG via PyMuPDF.

pdftoppm cannot decode this book's JBIG2 streams ("Unknown segment type"),
so poppler is not usable here. MuPDF handles them.

Usage: render.py FIRST LAST [--dpi 300] [--out data/png]
"""
import argparse
import os

import fitz

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("first", type=int)
    ap.add_argument("last", type=int)
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--out", default=os.path.join(ROOT, "data", "png"))
    ap.add_argument("--pdf", default=os.path.join(ROOT, "src.pdf"))
    a = ap.parse_args()

    os.makedirs(a.out, exist_ok=True)
    doc = fitz.open(a.pdf)
    for n in range(a.first, a.last + 1):
        dest = os.path.join(a.out, "p%04d.png" % n)
        if os.path.exists(dest):
            continue
        doc[n - 1].get_pixmap(dpi=a.dpi).save(dest)
        print("rendered", n)


if __name__ == "__main__":
    main()
