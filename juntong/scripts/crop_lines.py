#!/usr/bin/env python3
"""Magnify the exact printed lines containing given terms, stitched into one
image.

Why this exists alongside verify_names.py. That script filters candidates by
dual-OCR disagreement, which is the right default: where two configurations
read a span identically there is usually nothing to look at. But the filter
fails on THIS book's dominant error, because the mangle is systematic rather
than random -- 戴笠 is read as 戴符 / 戴竺 / 戴笃 / 戴答 / 戴科 by psm 6 and
psm 4 ALIKE. Two engines making the same mistake agree perfectly, and a
disagreement filter reports nothing to check. Systematic mangles have to be
named and looked at.

Two differences from verify_names.py's crop:
  - the line is located by ROW-BAND GEOMETRY rather than by guessing from the
    line's index as a fraction of page height, so the strip is actually
    centred on the term's line;
  - several terms, across several pages, stitch into ONE image, because the
    cost that matters is the number of image reads, not their size.

Usage:
    crop_lines.py --page 8 --terms 戴笠 蒋介石
    crop_lines.py --spec 8:戴笠 8:蒋介石 10:一九六二年 --out /tmp/check.png
"""
import argparse
import os

import cv2
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PNG = os.path.join(ROOT, "data", "png")
TXT = os.path.join(ROOT, "data", "txt")

INK = 160
MIN_ROW_INK = 4


def bands(page):
    img = cv2.imread(os.path.join(PNG, "p%04d.png" % page), cv2.IMREAD_GRAYSCALE)
    if img is None:
        return None, []
    h, w = img.shape
    ink = (img[: int(h * 0.90), :] < INK).astype(np.uint8)
    rows = ink.sum(axis=1)
    out, start = [], None
    for i, v in enumerate(rows):
        if v > MIN_ROW_INK and start is None:
            start = i
        elif v <= MIN_ROW_INK and start is not None:
            if i - start > 3:
                out.append((start, i))
            start = None
    if start is not None:
        out.append((start, len(rows)))
    return img, out


def find_line(page, term):
    """Index of the OCR line holding `term`, matched to a printed row band.

    The per-page OCR keeps blank lines as paragraph marks; the printed page
    has no such rows, so they must come out before the OCR line index can be
    used as a row-band index.
    """
    p = os.path.join(TXT, "p%04d.txt" % page)
    if not os.path.exists(p):
        return None
    lines = [l for l in open(p).read().split("\n") if l.strip()]
    for i, l in enumerate(lines):
        if term in l:
            return i
    return None


def strip(page, term, pad=26, scale=2.0):
    img, bs = bands(page)
    if img is None or not bs:
        return None
    idx = find_line(page, term)
    if idx is None or idx >= len(bs):
        return None
    y0, y1 = bs[idx]
    h, w = img.shape
    box = (0, max(0, y0 - pad), w, min(h, y1 + pad))
    im = Image.open(os.path.join(PNG, "p%04d.png" % page)).crop(box)
    return im.resize((int(im.width * scale), int(im.height * scale)),
                     Image.LANCZOS)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--page", type=int)
    ap.add_argument("--terms", nargs="*", default=[])
    ap.add_argument("--spec", nargs="*", default=[],
                    help="PAGE:TERM pairs, so one image can span pages")
    ap.add_argument("--out", default="/tmp/crop_lines.png")
    ap.add_argument("--scale", type=float, default=2.0)
    a = ap.parse_args()

    jobs = [(a.page, t) for t in a.terms]
    for s in a.spec:
        pg, _, term = s.partition(":")
        jobs.append((int(pg), term))

    tiles, labels = [], []
    for pg, term in jobs:
        im = strip(pg, term, scale=a.scale)
        if im is None:
            print("  NOT LOCATED  p%-4d %s" % (pg, term))
            continue
        tiles.append(im)
        labels.append("p%d %s" % (pg, term))

    if not tiles:
        raise SystemExit("nothing located")
    W = max(t.width for t in tiles)
    H = sum(t.height + 6 for t in tiles)
    canvas = Image.new("RGB", (W, H), "white")
    y = 0
    for t in tiles:
        canvas.paste(t, (0, y))
        y += t.height + 6
    canvas.save(a.out)
    print("%d strips -> %s  (%dx%d)" % (len(tiles), a.out, W, H))
    for l in labels:
        print("   ", l)


if __name__ == "__main__":
    main()
