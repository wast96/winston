#!/usr/bin/env python3
"""Crop a figure region out of a rendered page by EXPLICIT pixel coordinates.

find_figures.py auto-detects photo blocks but (a) misses maps and line art
(too little ink), (b) cuts off photos whose edges fade to light, and (c)
false-positives on dense text. When the crop must be right -- and for the
figures in a shipped book it must -- the box is chosen BY EYE off the page
image and passed here. Coordinates are in the ORIGINAL rendered-page pixels
(the same numbers you read off the page image; the Read tool prints the
original size and a multiply-to-map factor).

Single:  crop_fig.py PAGE X Y W H OUT [--pad 12]
Batch:   crop_fig.py --batch specs.json
         specs.json = [{"page":75,"x":.., "y":.., "w":.., "h":.., "out":"p0075-f1.png", "pad":12}, ...]

Writes data/figs/OUT and prints the final (clamped) box so the caller can
confirm nothing was silently shifted. --pad adds a safety margin on every
side (clamped to the page) so a slightly-tight box does not clip the image.
"""
import argparse
import json
import os

import cv2

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PNG = os.path.join(ROOT, "data", "png")
FIGS = os.path.join(ROOT, "data", "figs")


def crop_one(page, x, y, w, h, out, pad=0):
    src = os.path.join(PNG, "p%04d.png" % page)
    img = cv2.imread(src)
    if img is None:
        raise SystemExit("no such page render: %s" % src)
    H, W = img.shape[:2]
    x0 = max(0, x - pad)
    y0 = max(0, y - pad)
    x1 = min(W, x + w + pad)
    y1 = min(H, y + h + pad)
    if x1 <= x0 or y1 <= y0:
        raise SystemExit("empty box for %s: (%d,%d,%d,%d) on %dx%d" %
                         (out, x, y, w, h, W, H))
    os.makedirs(FIGS, exist_ok=True)
    dest = os.path.join(FIGS, out)
    cv2.imwrite(dest, img[y0:y1, x0:x1])
    print("wrote %s  box=(%d,%d,%d,%d)  from p%04d (%dx%d)" %
          (out, x0, y0, x1 - x0, y1 - y0, page, W, H))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("page", nargs="?", type=int)
    ap.add_argument("x", nargs="?", type=int)
    ap.add_argument("y", nargs="?", type=int)
    ap.add_argument("w", nargs="?", type=int)
    ap.add_argument("h", nargs="?", type=int)
    ap.add_argument("out", nargs="?")
    ap.add_argument("--pad", type=int, default=0)
    ap.add_argument("--batch")
    a = ap.parse_args()
    if a.batch:
        specs = json.load(open(a.batch))
        for s in specs:
            crop_one(s["page"], s["x"], s["y"], s["w"], s["h"], s["out"],
                     s.get("pad", a.pad))
    else:
        if None in (a.page, a.x, a.y, a.w, a.h, a.out):
            raise SystemExit("need PAGE X Y W H OUT (or --batch specs.json)")
        crop_one(a.page, a.x, a.y, a.w, a.h, a.out, a.pad)


if __name__ == "__main__":
    main()
