#!/usr/bin/env python3
"""Draw proposed crop boxes on a page so the box can be verified in ONE image.

Viewing a crop alone cannot reveal that it clipped the figure; viewing the
box drawn ON the page can. This is the crop-verification tool: propose a box,
overlay it, look -- does the rectangle enclose the WHOLE photo/map with a
little air, and nothing else (no body text, no wrong caption)? Adjust and
repeat. The overlay is downscaled so it is cheap to look at.

Usage:
  draw_boxes.py PAGE X Y W H [X Y W H ...] [--out preview.png] [--scale 0.5]
  draw_boxes.py --batch specs.json [--out preview.png] [--scale 0.5]
     specs.json = [{"page":75,"x":..,"y":..,"w":..,"h":..,"label":"f1"}, ...]
       (a single page's boxes; for multiple pages call once per page)

Writes the overlay to --out (default scratchpad/boxpreview.png) and prints
the path.
"""
import argparse
import json
import os

import cv2

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PNG = os.path.join(ROOT, "data", "png")
DEFAULT_OUT = os.path.join(ROOT, "data", "figs", "_boxpreview.png")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("page", nargs="?", type=int)
    ap.add_argument("coords", nargs="*", type=int)
    ap.add_argument("--batch")
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--scale", type=float, default=0.5)
    a = ap.parse_args()

    boxes = []
    if a.batch:
        specs = json.load(open(a.batch))
        page = specs[0]["page"]
        for i, s in enumerate(specs, 1):
            boxes.append((s["x"], s["y"], s["w"], s["h"], s.get("label", "f%d" % i)))
    else:
        page = a.page
        c = a.coords
        if len(c) % 4 != 0 or not c:
            raise SystemExit("need PAGE X Y W H [X Y W H ...]")
        for i in range(0, len(c), 4):
            boxes.append((c[i], c[i + 1], c[i + 2], c[i + 3], "f%d" % (i // 4 + 1)))

    img = cv2.imread(os.path.join(PNG, "p%04d.png" % page))
    if img is None:
        raise SystemExit("no such page render: p%04d.png" % page)
    for (x, y, w, h, label) in boxes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 6)
        cv2.putText(img, label, (x + 4, max(28, y - 8)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 0, 255), 3)
    if a.scale != 1.0:
        img = cv2.resize(img, None, fx=a.scale, fy=a.scale,
                         interpolation=cv2.INTER_AREA)
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    cv2.imwrite(a.out, img)
    print(a.out, "page", page, "boxes", len(boxes))


if __name__ == "__main__":
    main()
