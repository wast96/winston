#!/usr/bin/env python3
"""Re-OCR with the text block isolated from the marginal running heads.

This book prints a vertical running title down the outer margin. Under
psm 6 those glyphs land at the end of body lines and corrupt them. Crop
to the text block first; OCR the margin separately if it is ever needed.

Recto (odd printed page) has the vertical head on the right, verso on
the left, so the crop is side-aware.

Usage: ocr_crop.py FIRST LAST [--offset 10]
Writes: data/txt/p####.txt
"""
import argparse
import os
import re
import subprocess

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PNG = os.path.join(ROOT, "data", "png")
TXT = os.path.join(ROOT, "data", "txt")
CROPDIR = os.path.join(ROOT, "data", "crop")

CJK = r"\u4e00-\u9fff\u3000-\u303f\uff00-\uffef"

# fractions of page width/height that hold the body text block
INNER, OUTER, TOP, BOTTOM = 0.085, 0.155, 0.055, 0.945


def despace(line):
    line = re.sub(r"(?<=[" + CJK + r"])\s+", "", line)
    line = re.sub(r"\s+(?=[" + CJK + r"])", "", line)
    return line.strip()


def crop(page, printed):
    im = Image.open(os.path.join(PNG, "p%04d.png" % page))
    w, h = im.size
    if printed % 2 == 1:            # recto: outer margin on the right
        box = (int(w * INNER), int(h * TOP), int(w * (1 - OUTER)), int(h * BOTTOM))
    else:                           # verso: outer margin on the left
        box = (int(w * OUTER), int(h * TOP), int(w * (1 - INNER)), int(h * BOTTOM))
    os.makedirs(CROPDIR, exist_ok=True)
    dest = os.path.join(CROPDIR, "p%04d.png" % page)
    im.crop(box).save(dest)
    return dest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("first", type=int)
    ap.add_argument("last", type=int)
    ap.add_argument("--offset", type=int, default=10)
    a = ap.parse_args()

    os.makedirs(TXT, exist_ok=True)
    for n in range(a.first, a.last + 1):
        img = crop(n, n - a.offset)
        proc = subprocess.run(
            ["tesseract", img, "stdout", "-l", "chi_sim", "--psm", "6"],
            capture_output=True, text=True,
        )
        lines = [despace(l) for l in proc.stdout.splitlines() if despace(l)]
        with open(os.path.join(TXT, "p%04d.txt" % n), "w") as fh:
            fh.write("\n".join(lines))
        print(n, len(lines))


if __name__ == "__main__":
    main()
