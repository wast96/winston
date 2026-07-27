#!/usr/bin/env python3
"""Decide whether a page carries a footnote apparatus.

A footnote block betrays itself structurally, before you read a word:
its lines are set smaller, so the peak-to-peak spacing of the horizontal
ink profile drops in the bottom band relative to the body. A separator
rule, where present, shows as a single very wide, very thin ink row.

Reports per page: body line pitch, foot line pitch, their ratio, and
whether a rule-like row was found. A ratio meaningfully below 1.0 is the
signature of smaller type at the foot.

Usage: detect_notes.py PAGE [PAGE ...]
"""
import sys

import numpy as np
from PIL import Image


def profile_pitch(rows):
    """Median distance between successive text-line centres."""
    ink = rows > rows.max() * 0.18 if rows.max() else rows.astype(bool)
    centres, run = [], []
    for i, on in enumerate(ink):
        if on:
            run.append(i)
        elif run:
            centres.append(sum(run) / len(run))
            run = []
    if run:
        centres.append(sum(run) / len(run))
    if len(centres) < 3:
        return None
    return float(np.median(np.diff(centres)))


def find_rule(img, arr):
    """A separator rule: a row spanning much of the text width, one or two
    pixels tall, with nothing like it in the body."""
    h, w = arr.shape
    dark = arr < 150
    widths = dark.sum(axis=1)
    for y in range(int(h * 0.55), h):
        if widths[y] > w * 0.28:
            thickness = 1
            yy = y + 1
            while yy < h and widths[yy] > w * 0.28:
                thickness += 1
                yy += 1
            if thickness <= 4:
                return y, int(widths[y])
    return None


def analyse(page):
    path = "data/png/p%04d.png" % page
    arr = np.array(Image.open(path).convert("L"))
    h, w = arr.shape
    text = arr[int(h * 0.07):int(h * 0.95), int(w * 0.10):int(w * 0.90)]
    rows = (text < 150).sum(axis=1).astype(float)

    n = len(rows)
    body_pitch = profile_pitch(rows[: int(n * 0.70)])
    foot_pitch = profile_pitch(rows[int(n * 0.72):])
    rule = find_rule(Image.open(path), arr)

    ratio = (foot_pitch / body_pitch) if (body_pitch and foot_pitch) else None
    print("page %4d  body pitch %s  foot pitch %s  ratio %s  rule %s"
          % (page,
             "%.1f" % body_pitch if body_pitch else "  n/a",
             "%.1f" % foot_pitch if foot_pitch else "  n/a",
             "%.2f" % ratio if ratio else " n/a",
             ("y=%d w=%d" % rule) if rule else "none"))
    return ratio


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        analyse(int(arg))
