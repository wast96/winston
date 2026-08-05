#!/usr/bin/env python3
"""Record which printed lines are paragraph-initial, from the indent.

The book indents the first line of every paragraph by two full-width spaces
and justifies everything else to the measure. That indent is the author's own
paragraph mark, and it is unambiguous -- unlike the two signals assemble.py
had been using:

  - tesseract's blank line, which it emits only sometimes and never across a
    page break;
  - the short last line, which is right inside a page and WRONG at the foot of
    one, because a page's final line is short whenever the text block ends
    there, whether or not the paragraph does.

That second failure is not hypothetical: it split a nine-man roster in the
front matter across two paragraphs at a page turn, and it moves the paragraph
count, which is what the parity check measures.

tesseract discards the indent (it strips leading whitespace), so it is
measured off the page image instead: a line whose ink starts a full character
width or more to the right of the page's own left margin begins a paragraph.
The margin is taken as the modal line start on that page rather than a
constant, so a page with a wider gutter is judged against itself.

Usage: indents.py FIRST LAST
Writes: data/indent/p####.json  -- [bool] per text line, top to bottom
"""
import argparse
import json
import os
import sys

import cv2
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ocr_crop

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PNG = os.path.join(ROOT, "data", "png")
OUT = os.path.join(ROOT, "data", "indent")

INK = 160
MIN_ROW_INK = 4


def line_starts(page):
    img = cv2.imread(os.path.join(PNG, "p%04d.png" % page), cv2.IMREAD_GRAYSCALE)
    if img is None:
        return None
    h, w = img.shape
    ink = (img < INK).astype(np.uint8)
    rows = ink.sum(axis=1)
    bands, start = [], None
    for i, v in enumerate(rows):
        if v > MIN_ROW_INK and start is None:
            start = i
        elif v <= MIN_ROW_INK and start is not None:
            if i - start > 3:
                bands.append((start, i))
            start = None
    if start is not None:
        bands.append((start, len(rows)))

    out = []
    for y0, y1 in bands:
        cols = ink[y0:y1, :].sum(axis=0)
        nz = np.nonzero(cols > 0)[0]
        if not len(nz):
            continue
        out.append({"y0": int(y0), "y1": int(y1),
                    "x0": int(nz[0]), "x1": int(nz[-1])})
    return out, w, h


# Recto and verso mirror their gutter, so the flush-left position is not one
# number but two. Measuring a single margin across the book put it between the
# two and read every line on one side as indented and none on the other.
MARGIN = {0: None, 1: None}


def measure_margin(first, last, parity, step=6):
    """Modal flush-left position for recto or verso, as a fraction of width."""
    xs, k = [], 0
    for n in range(first, last + 1):
        if n % 2 != parity:
            continue
        k += 1
        if k % step:
            continue
        got = line_starts(n)
        if not got:
            continue
        lines, w, h = got
        if len(lines) < 5:
            continue
        widths = [l["x1"] - l["x0"] for l in lines]
        meas = float(np.median(widths))
        xs += [l["x0"] / float(w) for l in lines
               if (l["x1"] - l["x0"]) > 0.45 * meas]
    if not xs:
        return None
    bins = np.round(np.array(xs) / 0.0024)
    vals, counts = np.unique(bins, return_counts=True)
    return float(vals[np.argmax(counts)]) * 0.0024


def classify(page):
    got = line_starts(page)
    if not got:
        return []
    lines, w, h = got
    if not lines:
        return []
    # Body lines only: drop the folio, which is narrow and set at the outer
    # edge, and headings, which are centred. Both would distort the margin.
    widths = [l["x1"] - l["x0"] for l in lines]
    measure = float(np.median(widths))
    # Drop the folio band by calling ocr_crop's OWN test, not a copy of it.
    # Two independent implementations of "is there a page number here" is one
    # too many: they disagreed on 140 of 515 pages, and every disagreement
    # slid the whole page's paragraph marks one line out of step with the OCR
    # text. That misalignment, not any threshold, is what made the paragraph
    # counts wander.
    if ocr_crop.folio_present(page):
        lines = lines[:-1]
    if not lines:
        return []
    body = [l for l in lines if (l["x1"] - l["x0"]) > 0.45 * measure]
    if not body:
        return [False] * len(lines)
    # The flush-left margin is taken GLOBALLY, from the whole book, not from
    # the page in hand. Estimating it per page was the flaw: a page has only
    # twenty-odd lines, a page whose margin sits a few pixels off centre
    # produces a second cluster, and the estimate then reads ordinary lines as
    # indented -- which split a roster across a page turn and, tuned the other
    # way, merged real paragraphs. The layout is constant across the book, so
    # one measurement over thousands of lines is both more accurate and
    # stable.
    #
    # NOTE (The Gangs of Old Shanghai): this geometric path is NOT used on this
    # book. Its scan carries heavy left-margin speckle and tight line spacing,
    # so the row-band detector does not align one-to-one with the cropped OCR
    # lines and the per-line indent flags land on the wrong lines. Assembly
    # therefore runs from the blank-line/short-line fallback (no data/indent),
    # and paragraph seams are corrected by reading the scan while translating.
    char = 0.024 * w                     # one Han character at this render
    m = MARGIN.get(page % 2)
    margin = m * w if m else float(np.median([l["x0"] for l in body]))
    # The printed indent is two full-width spaces. Requiring most of that,
    # rather than half a character, keeps page skew from reading as an indent:
    # at 0.55 char the first line of a page carrying the continuation of a
    # roster was flagged as a new paragraph, splitting a nine-man list in two.
    return [(l["x1"] - l["x0"]) > 0.45 * measure and l["x0"] > margin + 1.3 * char
            for l in lines]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("first", type=int)
    ap.add_argument("last", type=int)
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    for par in (0, 1):
        MARGIN[par] = measure_margin(a.first, a.last, par)
    print("flush-left margin: even pages %.4f, odd pages %.4f of page width"
          % (MARGIN[0] or -1, MARGIN[1] or -1))
    n_ind = n_line = 0
    for n in range(a.first, a.last + 1):
        flags = classify(n)
        if not flags:
            continue
        with open(os.path.join(OUT, "p%04d.json" % n), "w") as fh:
            json.dump(flags, fh)
        n_ind += sum(flags)
        n_line += len(flags)
    print("%d indented lines in %d text lines across pages %d-%d"
          % (n_ind, n_line, a.first, a.last))


if __name__ == "__main__":
    main()
