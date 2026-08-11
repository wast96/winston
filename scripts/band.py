#!/usr/bin/env python3
"""Crop a horizontal band of a rendered page by OCR-text line number.

Usage: band.py PAGE LINE1 [LINE2] [--out NAME]

LINE numbers are 1-based indices into the NON-BLANK lines of
data/txt/pNNNN.txt (the same text the OCR crop produced). The band is
computed from the ocr_crop box (top 0.09, bottom 0.89) assuming lines are
evenly spaced, with a margin of one line either side. Saves a png crop to
the scratchpad and prints its path.
"""
import sys, os
from PIL import Image

TOP, BOT = 0.09, 0.89
SCRATCH = os.environ.get("BAND_OUT", "/tmp/claude-0/-home-user-winston/74d20146-18bd-5011-ad00-9a4efabfbf0b/scratchpad")

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    page = int(args[0])
    l1 = int(args[1])
    l2 = int(args[2]) if len(args) > 2 else l1
    txt = open(f"data/txt/p{page:04d}.txt").read().splitlines()
    nonblank = [ln for ln in txt if ln.strip()]
    n = len(nonblank)
    img = Image.open(f"data/png/p{page:04d}.png")
    w, h = img.size
    band_h = (BOT - TOP) / n
    y1 = max(0, TOP + (l1 - 1.6) * band_h)
    y2 = min(1.0, TOP + (l2 + 0.9) * band_h)
    crop = img.crop((int(0.04 * w), int(y1 * h), int(0.95 * w), int(y2 * h)))
    os.makedirs(SCRATCH, exist_ok=True)
    out = os.path.join(SCRATCH, f"band_p{page}_{l1}_{l2}.png")
    crop.save(out)
    print(out)
    for i in range(max(0, l1 - 2), min(n, l2 + 1)):
        print(f"  ocr line {i+1}: {nonblank[i][:40]}")

if __name__ == "__main__":
    main()
