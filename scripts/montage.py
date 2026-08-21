#!/usr/bin/env python3
"""Contact sheet of figure crops for a fast QA sweep.

Reviewing every crop against its page is the expensive step; a montage lets
many crops be eyeballed in one image for the obvious failure -- a clipped
head, a sliver of the next photo, a caption swallowed into the frame. Each
tile is labelled with its filename so a bad one can be named and re-cropped.

Usage: montage.py file1.png file2.png ... [--out sheet.png] [--cols 4] [--tile 360]
       montage.py --glob 'p004*-*.png' [--out sheet.png]
Files are resolved under data/figs/.
"""
import argparse
import glob as globmod
import os

import cv2
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIGS = os.path.join(ROOT, "data", "figs")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--glob")
    ap.add_argument("--out", default=os.path.join(FIGS, "_montage.png"))
    ap.add_argument("--cols", type=int, default=4)
    ap.add_argument("--tile", type=int, default=380)
    a = ap.parse_args()

    names = list(a.files)
    if a.glob:
        names += [os.path.basename(p) for p in
                  sorted(globmod.glob(os.path.join(FIGS, a.glob)))]
    names = [n for n in names if not n.startswith("_")]
    if not names:
        raise SystemExit("no crops given")

    tile = a.tile
    pad = 8
    lab = 22
    cell = tile + 2 * pad + lab
    cols = a.cols
    rows = (len(names) + cols - 1) // cols
    sheet = np.full((rows * cell, cols * cell, 3), 245, np.uint8)

    for i, name in enumerate(names):
        img = cv2.imread(os.path.join(FIGS, name))
        r, c = divmod(i, cols)
        y0 = r * cell
        x0 = c * cell
        if img is not None:
            h, w = img.shape[:2]
            s = min(tile / w, tile / h)
            rw, rh = int(w * s), int(h * s)
            resized = cv2.resize(img, (rw, rh), interpolation=cv2.INTER_AREA)
            oy = y0 + lab + pad + (tile - rh) // 2
            ox = x0 + pad + (tile - rw) // 2
            sheet[oy:oy + rh, ox:ox + rw] = resized
            cv2.rectangle(sheet, (ox, oy), (ox + rw, oy + rh), (200, 200, 200), 1)
        cv2.putText(sheet, name, (x0 + pad, y0 + 16),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.42, (0, 0, 160), 1)
    cv2.imwrite(a.out, sheet)
    print(a.out, "tiles", len(names), "%dx%d" % (cols, rows))


if __name__ == "__main__":
    main()
