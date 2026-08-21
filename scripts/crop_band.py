#!/usr/bin/env python3
"""Magnified horizontal-band crop of a rendered page, for eye-verifying dense
rosters / faded spans. PLAYWRIGHT-free (plain Pillow).

Usage: crop_band.py PAGE Y0 Y1 [X0 X1] [--scale 2.0] [--out PATH]
  PAGE      pdf page number (reads data/png/pNNNN.png)
  Y0 Y1     vertical band as FRACTIONS of page height (0..1)
  X0 X1     optional horizontal band as fractions of width (default 0..1)
"""
import argparse
import os
from PIL import Image

ROOT = '/home/user/winston'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('page', type=int)
    ap.add_argument('y0', type=float)
    ap.add_argument('y1', type=float)
    ap.add_argument('x0', type=float, nargs='?', default=0.0)
    ap.add_argument('x1', type=float, nargs='?', default=1.0)
    ap.add_argument('--scale', type=float, default=2.0)
    ap.add_argument('--out', default=None)
    a = ap.parse_args()
    src = os.path.join(ROOT, 'data', 'png', 'p%04d.png' % a.page)
    im = Image.open(src)
    W, H = im.size
    box = (int(a.x0 * W), int(a.y0 * H), int(a.x1 * W), int(a.y1 * H))
    crop = im.crop(box)
    if a.scale != 1.0:
        crop = crop.resize((int(crop.width * a.scale), int(crop.height * a.scale)),
                           Image.LANCZOS)
    out = a.out or os.path.join(ROOT, 'scratch_crop.png')
    os.makedirs(os.path.dirname(out), exist_ok=True) if os.path.dirname(out) else None
    crop.save(out)
    print('wrote', out, crop.size)


if __name__ == '__main__':
    main()
