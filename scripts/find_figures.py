#!/usr/bin/env python3
"""Locate figure/photo regions on a scanned page.

Text and halftone photographs differ in a way that survives binarisation:
text is thin strokes arranged in regular horizontal bands with wide gaps,
a photograph is a dense block with high local ink coverage and no gaps.
Dilate horizontally to fuse each into blobs, then keep blobs whose ink
density and aspect are photo-like rather than line-like.

Usage: find_figures.py FIRST LAST [--offset 10]
Writes data/figs/p####-f#.png and prints a manifest line per figure.
"""
import argparse
import json
import os

import cv2
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PNG = os.path.join(ROOT, "data", "png")
FIGS = os.path.join(ROOT, "data", "figs")

MIN_AREA_FRAC = 0.012      # ignore anything smaller than ~1.2% of the page
MIN_DENSITY = 0.30         # photos hold far more ink per unit area than text
MIN_HEIGHT_FRAC = 0.045    # taller than a couple of text lines


def detect(page):
    path = os.path.join(PNG, "p%04d.png" % page)
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return []
    h, w = img.shape
    ink = (img < 160).astype(np.uint8)

    # fuse glyphs into blocks; wide kernel joins a text line, tall kernel
    # only closes up when the region is solid, which is the photo case
    kern = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
    closed = cv2.morphologyEx(ink, cv2.MORPH_CLOSE, kern)

    n, labels, stats, _ = cv2.connectedComponentsWithStats(closed, 8)
    out = []
    for i in range(1, n):
        x, y, bw, bh, area = stats[i]
        if bw * bh < MIN_AREA_FRAC * w * h:
            continue
        if bh < MIN_HEIGHT_FRAC * h:
            continue
        density = ink[y:y + bh, x:x + bw].mean()
        if density < MIN_DENSITY:
            continue
        out.append({"x": int(x), "y": int(y), "w": int(bw), "h": int(bh),
                    "density": round(float(density), 3),
                    "page_frac": round(float(bw * bh) / (w * h), 3)})
    return out


def is_furniture(box, all_boxes, tol=40):
    """A region that appears at nearly the same coordinates on several
    pages is a running decoration, not a figure. This book prints one in
    the outer margin of every recto."""
    hits = 0
    for other in all_boxes:
        if other["page"] == box["page"]:
            continue
        if (abs(other["x"] - box["x"]) < tol and abs(other["y"] - box["y"]) < tol
                and abs(other["w"] - box["w"]) < tol and abs(other["h"] - box["h"]) < tol):
            hits += 1
    return hits >= 2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("first", type=int)
    ap.add_argument("last", type=int)
    ap.add_argument("--offset", type=int, default=10)
    a = ap.parse_args()

    os.makedirs(FIGS, exist_ok=True)

    raw = []
    for n in range(a.first, a.last + 1):
        for box in detect(n):
            raw.append(dict(box, page=n, printed=n - a.offset))

    manifest = []
    for box in raw:
        if is_furniture(box, raw):
            print("skip furniture p%d at (%d,%d)" % (box["page"], box["x"], box["y"]))
            continue
        k = sum(1 for m in manifest if m["page"] == box["page"]) + 1
        img = cv2.imread(os.path.join(PNG, "p%04d.png" % box["page"]))
        crop = img[box["y"]:box["y"] + box["h"], box["x"]:box["x"] + box["w"]]
        name = "p%04d-f%d.png" % (box["page"], k)
        cv2.imwrite(os.path.join(FIGS, name), crop)
        rec = dict(box, file=name)
        manifest.append(rec)
        print(json.dumps(rec, ensure_ascii=False))

    with open(os.path.join(FIGS, "manifest.json"), "w") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
