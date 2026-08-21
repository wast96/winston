#!/usr/bin/env python3
"""Downscaled page montage, to sweep the whole book for figures by eye.

find_figures.py flags dense photo blocks but misses faint maps and line
diagrams (too little ink) and can only hint at where a photo's edges are.
To be SURE every figure is caught -- the standing instruction -- sweep every
page in labelled thumbnail sheets and record which pages carry an image.
Thumbnails are big enough to see a faint map, small enough that a chapter is
a handful of sheets.

Usage: scan_pages.py FIRST LAST [--cols 3 --rows 3 --tile 760 --out DIR]
Writes sheet_####_####.png per sheet into --out (default scratchpad).
"""
import argparse
import os

import cv2
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PNG = os.path.join(ROOT, "data", "png")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("first", type=int)
    ap.add_argument("last", type=int)
    ap.add_argument("--cols", type=int, default=3)
    ap.add_argument("--rows", type=int, default=3)
    ap.add_argument("--tile", type=int, default=760)
    ap.add_argument("--out", default=os.path.join(
        ROOT, "data", "figs", "_scan"))
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)

    per = a.cols * a.rows
    tile = a.tile
    lab = 30
    cellw = tile + 12
    cellh = tile + lab + 12
    pages = list(range(a.first, a.last + 1))
    for start in range(0, len(pages), per):
        chunk = pages[start:start + per]
        sheet = np.full((a.rows * cellh, a.cols * cellw, 3), 250, np.uint8)
        for i, p in enumerate(chunk):
            img = cv2.imread(os.path.join(PNG, "p%04d.png" % p))
            r, c = divmod(i, a.cols)
            y0 = r * cellh
            x0 = c * cellw
            cv2.putText(sheet, "p%04d" % p, (x0 + 6, y0 + 22),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 180), 2)
            if img is not None:
                h, w = img.shape[:2]
                s = min(tile / w, tile / h)
                rw, rh = int(w * s), int(h * s)
                resized = cv2.resize(img, (rw, rh), interpolation=cv2.INTER_AREA)
                oy = y0 + lab
                ox = x0 + 6
                sheet[oy:oy + rh, ox:ox + rw] = resized
                cv2.rectangle(sheet, (ox, oy), (ox + rw, oy + rh),
                              (210, 210, 210), 1)
        out = os.path.join(a.out, "sheet_%04d_%04d.png" % (chunk[0], chunk[-1]))
        cv2.imwrite(out, sheet)
        print(out)


if __name__ == "__main__":
    main()
