#!/usr/bin/env python3
"""Recover section openings in a VERTICAL, right-to-left Japanese scan.

The template's find_headings.py profiles ROWS and looks for a short centred
horizontal line -- correct for a horizontal Chinese book, useless here. In a
vertical book a section title is a short COLUMN, set off with blank space above
and below it, and flanked by a wider-than-normal gap from the surrounding body
columns. So this transposes the idea: profile COLUMNS, and flag any text column
whose ink floats in a short band with clear sky above AND below it.

Body columns run the full height of the text block. An end-of-paragraph column
is short but TOP-aligned (blank only below). A section title is the only thing
that floats: short, with blank above and below. That single signal separates
openings from running pages without reading a glyph; the band is then OCR'd
alone with jpn_vert to label what the geometry found.

Reads data/png_survey/p####.png (200 dpi). Usage:
  find_headings_vert.py FIRST LAST [--out data/headings.json] [--dir ...]
"""
import argparse
import json
import os
import subprocess

import cv2
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INK = 165            # grey level below which a pixel counts as ink
TOP_FURNITURE = 0.065  # running head + folio live in the top band; ignore it
SIDE_MARGIN = 0.03
MIN_COL_INK = 6      # ink pixels in a column before it counts as text
FLOAT_ABOVE = 0.11   # blank fraction of body height required above a title
FLOAT_BELOW = 0.11   # ... and below
MAX_TITLE_H = 0.55   # a title column is at most this fraction of body height


def col_bands(colsum, thresh):
    bands, start = [], None
    for i, v in enumerate(colsum):
        if v > thresh and start is None:
            start = i
        elif v <= thresh and start is not None:
            if i - start > 2:
                bands.append((start, i))
            start = None
    if start is not None:
        bands.append((start, len(colsum)))
    return bands


def analyse(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return None
    h, w = img.shape
    top = int(h * TOP_FURNITURE)
    body = img[top:int(h * 0.965), int(w * SIDE_MARGIN):int(w * (1 - SIDE_MARGIN))]
    bh, bw = body.shape
    ink = (body < INK).astype(np.uint8)
    colsum = ink.sum(axis=0)
    # column bands = vertical text lines
    bands = col_bands(colsum, MIN_COL_INK)
    if not bands:
        return {"blank": True, "heads": []}
    widths = [x1 - x0 for x0, x1 in bands]
    med_w = float(np.median(widths))
    gaps = [bands[i + 1][0] - bands[i][1] for i in range(len(bands) - 1)]
    med_gap = float(np.median(gaps)) if gaps else 0.0
    ox = int(w * SIDE_MARGIN)
    heads = []
    for i, (x0, x1) in enumerate(bands):
        # a section title is a FULL-WIDTH column (furigana ruby is ~half width)
        if (x1 - x0) < 0.62 * med_w:
            continue
        sub = ink[:, x0:x1]
        rows = sub.sum(axis=1)
        nz = np.nonzero(rows > 1)[0]
        if len(nz) == 0:
            continue
        y0, y1 = nz[0], nz[-1]
        height = (y1 - y0) / float(bh)
        above = y0 / float(bh)
        below = (bh - y1) / float(bh)
        left_gap = (x0 - bands[i - 1][1]) if i else bw
        right_gap = (bands[i + 1][0] - x1) if i + 1 < len(bands) else bw
        set_off = bool(med_gap and min(left_gap, right_gap) >= 1.8 * med_gap)
        # a title EITHER sits alone with wide sky both sides (section starts a
        # fresh column block) OR floats vertically between two sections on a
        # running page (blank above AND below within its own column).
        floats = above >= 0.18 and below >= 0.18
        if 0.05 <= height <= 0.45 and (set_off or floats):
            heads.append({
                "x": [int(x0 + ox), int(x1 + ox)],
                "y": [int(y0 + top), int(y1 + top)],
                "h_frac": round(height, 3),
                "above": round(above, 3),
                "below": round(below, 3),
                "lgap": round(left_gap / med_gap, 1) if med_gap else 0,
                "rgap": round(right_gap / med_gap, 1) if med_gap else 0,
            })
    return {"heads": heads, "n_cols": len(bands)}


def ocr_band(path, head, pad=14):
    img = cv2.imread(path)
    x0, x1 = head["x"]
    y0, y1 = head["y"]
    crop = img[max(0, y0 - pad): y1 + pad, max(0, x0 - pad): x1 + pad]
    crop = cv2.resize(crop, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    tmp = "/tmp/vhead.png"
    cv2.imwrite(tmp, crop)
    r = subprocess.run(["tesseract", tmp, "stdout", "-l", "jpn_vert", "--psm", "5"],
                       capture_output=True, text=True,
                       env={**os.environ, "OMP_THREAD_LIMIT": "1"})
    return r.stdout.strip().replace(" ", "").replace("\n", "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("first", type=int)
    ap.add_argument("last", type=int)
    ap.add_argument("--dir", default=os.path.join(ROOT, "data", "png_survey"))
    ap.add_argument("--out", default=os.path.join(ROOT, "data", "headings.json"))
    ap.add_argument("--no-ocr", action="store_true")
    a = ap.parse_args()

    recs = []
    for n in range(a.first, a.last + 1):
        path = os.path.join(a.dir, "p%04d.png" % n)
        r = analyse(path)
        if r is None:
            continue
        r["page"] = n
        for hd in r.get("heads", []):
            hd["text"] = "" if a.no_ocr else ocr_band(path, hd)
            print("p%-4d h%.2f above%.2f below%.2f  %s"
                  % (n, hd["h_frac"], hd["above"], hd["below"], hd["text"]))
        if r.get("heads"):
            recs.append(r)

    if a.out:
        old = {}
        if os.path.exists(a.out):
            try:
                old = {x["page"]: x for x in json.load(open(a.out))}
            except Exception:
                old = {}
        for r in recs:
            old[r["page"]] = r
        with open(a.out, "w") as fh:
            json.dump([old[k] for k in sorted(old)], fh, ensure_ascii=False, indent=1)
    print("\n%d pages with a floating short column" % len(recs))


if __name__ == "__main__":
    main()
