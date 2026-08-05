#!/usr/bin/env python3
"""Recover a book's structure when the scan has no table of contents.

This edition's scan jumps straight from the CIP page to body text: no TOC
page exists to OCR, and the PDF carries no bookmarks. So the chapter map has
to be derived from the pages themselves.

Two geometric signals separate a section opening from a running page, and
both survive a poor scan far better than OCR does:

  1. TOP DROP. A section opening leaves the upper third of the page blank.
     A running page starts its text at the same height every time.
  2. CENTRED SHORT LINE. The heading is one short line with wide, roughly
     equal margins on both sides, whereas body lines are justified to the
     full measure.

Ink-row profiling finds both without reading a single character. OCR is then
run on the heading band ALONE — a few hundred glyphs for the whole book
instead of half a million — and only to label what the geometry already found.

Usage: find_headings.py FIRST LAST [--offset 5] [--out data/headings.json]
"""
import argparse
import json
import os
import subprocess

import cv2
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PNG = os.path.join(ROOT, "data", "png")

INK = 160          # grey level below which a pixel counts as ink
MIN_ROW_INK = 4    # pixels of ink needed before a row counts as text
TOP_DROP = 0.16    # first ink below this fraction of page height = opening
CENTRE_TOL = 0.06  # left/right margin may differ by this fraction and still
                   # read as centred


def row_profile(img):
    ink = (img < INK).astype(np.uint8)
    return ink.sum(axis=1), ink


def line_bands(rows, min_ink=MIN_ROW_INK):
    """Contiguous runs of inked rows -> (start, end) per text line."""
    bands, start = [], None
    for i, v in enumerate(rows):
        if v > min_ink and start is None:
            start = i
        elif v <= min_ink and start is not None:
            if i - start > 3:
                bands.append((start, i))
            start = None
    if start is not None:
        bands.append((start, len(rows)))
    return bands


def analyse(page):
    """Return every heading-shaped line on the page, not just the first.

    Restricting this to the first line missed every section that opens
    part-way down a page, which left 70-page gaps in the recovered map. A
    heading is judged on three things at any position: centred with wide
    margins, short of the full measure, and set off by extra leading above
    or below.
    """
    path = os.path.join(PNG, "p%04d.png" % page)
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return None
    h, w = img.shape
    # ignore the footer band: the printed page number is ink but not text
    body = img[: int(h * 0.90), :]
    rows, ink = row_profile(body)
    bands = line_bands(rows)
    if not bands:
        return {"page": page, "blank": True}

    heights = [b[1] - b[0] for b in bands]
    med_h = float(np.median(heights))
    # normal leading, measured on this page rather than assumed
    gaps = [bands[i + 1][0] - bands[i][1] for i in range(len(bands) - 1)]
    med_gap = float(np.median(gaps)) if gaps else 0.0

    widths = []
    for y0, y1 in bands:
        cols = ink[y0:y1, :].sum(axis=0)
        nz = np.nonzero(cols > 0)[0]
        widths.append((nz[0], nz[-1]) if len(nz) else (0, w))
    measure = float(np.median([r - l for l, r in widths])) or w

    heads = []
    for i, (y0, y1) in enumerate(bands):
        l, r = widths[i]
        left, right = l / float(w), 1.0 - r / float(w)
        if not (abs(left - right) < CENTRE_TOL and left > 0.18):
            continue
        if (r - l) > 0.72 * measure:        # a full-measure line is body text
            continue
        above = (y0 - bands[i - 1][1]) if i else y0
        below = (bands[i + 1][0] - y1) if i + 1 < len(bands) else int(h * 0.9) - y1
        if med_gap and max(above, below) < 1.6 * med_gap and i:
            continue                        # no extra leading: not set off
        heads.append({
            "band": [int(y0), int(y1)],
            "line_index": i,
            "top": round(y0 / float(h), 4),
            "left": round(left, 4),
            "right": round(right, 4),
            "width_frac": round((r - l) / measure, 3),
            "tall": bool((y1 - y0) > 1.15 * med_h),
            "page_opening": bool(i == 0 and y0 / float(h) > TOP_DROP),
        })

    return {
        "page": page,
        "n_lines": len(bands),
        "heads": heads,
        "opening": bool(heads),
        "band": heads[0]["band"] if heads else [int(bands[0][0]), int(bands[0][1])],
    }


def ocr_band(page, band, pad=18):
    """OCR just the heading line. psm 7 = treat the image as one text line."""
    path = os.path.join(PNG, "p%04d.png" % page)
    img = cv2.imread(path)
    y0, y1 = band
    crop = img[max(0, y0 - pad): y1 + pad, :]
    crop = cv2.resize(crop, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    tmp = "/tmp/heading_%04d.png" % page
    cv2.imwrite(tmp, crop)
    r = subprocess.run(["tesseract", tmp, "stdout", "-l", "chi_sim", "--psm", "7"],
                       capture_output=True, text=True)
    os.remove(tmp)
    return r.stdout.strip().replace(" ", "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("first", type=int)
    ap.add_argument("last", type=int)
    ap.add_argument("--offset", type=int, default=5)
    ap.add_argument("--out", default=os.path.join(ROOT, "data", "headings.json"))
    a = ap.parse_args()

    recs = []
    for n in range(a.first, a.last + 1):
        r = analyse(n)
        if r is None:
            continue
        r["printed"] = n - a.offset
        for hd in r.get("heads", []):
            hd["text"] = ocr_band(n, hd["band"])
            print("p%-4d printed %-4d top %.3f w%.2f %s %s"
                  % (n, r["printed"], hd["top"], hd["width_frac"],
                     "OPEN" if hd["page_opening"] else "mid ", hd["text"]))
        recs.append(r)

    # merge, never overwrite: re-running one range must not lose the others
    if os.path.exists(a.out):
        old = {x["page"]: x for x in json.load(open(a.out))}
    else:
        old = {}
    for r in recs:
        old[r["page"]] = r
    with open(a.out, "w") as fh:
        json.dump([old[k] for k in sorted(old)], fh, ensure_ascii=False, indent=1)
    print("\n%d openings in %d pages" % (sum(1 for r in recs if r.get("opening")),
                                         len(recs)))


if __name__ == "__main__":
    main()
