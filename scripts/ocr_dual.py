#!/usr/bin/env python3
"""QC step 1: two independent OCR reads per page, diffed at character level.

PaddleOCR is the better second engine but its model weights download from a
host outside the sandbox allowlist, so it is unavailable. Substitute: two
tesseract reads of the SAME model that fail differently, so the spans they
disagree on are the spans worth an eyeball.

JAPANESE ADAPTATION (this book is vertical jpn with furigana). The original
Chinese path OCR'd the WHOLE page with chi_sim under psm 4/6 -- wrong here on
two counts: the wrong script model is silent corruption, and an uncropped page
feeds the running head/folio into the read. So this version crops the measured
body box (same L/R/T/B as ocr_crop / ocr_survey) and runs jpn_vert --psm 5
twice: once on the plain grayscale crop, once on an Otsu-binarised crop. Those
two thresholdings fail differently on the same hard glyphs, which is exactly
the second signal the disagreement filter needs. Set --lang/--psm to restore
the Chinese behaviour on a Chinese book.

Anything the reads disagree on is written to a flag list for visual
adjudication against the rendered scan.

Usage: ocr_dual.py FIRST LAST [--lang jpn_vert --psm 5
                               --left --right --top --bottom]
Writes: data/ocr/p####.json  {page, reads: {name: [lines]}, flags: [...]}
"""
import argparse
import difflib
import json
import os
import re
import subprocess
import sys

import cv2

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PNG = os.path.join(ROOT, "data", "png")
OUT = os.path.join(ROOT, "data", "ocr")
CROP = os.path.join(ROOT, "data", "crop_dual")

# CJK unified + kana + CJK symbols/punctuation + fullwidth (matches ocr_crop).
CJK = r"\u4e00-\u9fff\u3040-\u30ff\u3000-\u303f\uff00-\uffef"

# Measured body-text box for this book (fractions of page w/h).
L, R, T, B = 0.035, 0.965, 0.075, 0.955
LANG, PSM = "jpn_vert", "5"


def despace(line):
    """The vertical models space kana/Han like chi_sim; drop only
    CJK-internal spaces so latin words and numbers keep their spacing."""
    line = re.sub(r"(?<=[" + CJK + r"])\s+", "", line)
    line = re.sub(r"\s+(?=[" + CJK + r"])", "", line)
    return line.strip()


def make_variants(page):
    """Crop the body box, return (gray_png, binarised_png) paths, or None."""
    src = os.path.join(PNG, "p%04d.png" % page)
    if not os.path.exists(src):
        return None
    img = cv2.imread(src)
    if img is None:
        return None
    h, w = img.shape[:2]
    crop = img[int(h * T):int(h * B), int(w * L):int(w * R)]
    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    _, binar = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    gp = os.path.join(CROP, "p%04d_gray.png" % page)
    bp = os.path.join(CROP, "p%04d_bin.png" % page)
    cv2.imwrite(gp, gray)
    cv2.imwrite(bp, binar)
    return gp, bp


def run(img):
    proc = subprocess.run(
        ["tesseract", img, "stdout", "-l", LANG, "--psm", PSM],
        capture_output=True, text=True,
        env={**os.environ, "OMP_THREAD_LIMIT": "1"},
    )
    return [despace(l) for l in proc.stdout.splitlines() if despace(l)]


def diff_flags(a, b):
    """Character-level disagreements between two reads of the same page."""
    flags = []
    sm = difflib.SequenceMatcher(None, "\n".join(a), "\n".join(b))
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        left, right = "\n".join(a)[i1:i2], "\n".join(b)[j1:j2]
        if not left.strip() and not right.strip():
            continue
        ctx = "\n".join(a)[max(0, i1 - 12):i2 + 12].replace("\n", "\u23ce")
        flags.append({"tag": tag, "a": left, "b": right, "ctx": ctx})
    return flags


def main(first, last):
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(CROP, exist_ok=True)
    for n in range(first, last + 1):
        variants = make_variants(n)
        if not variants:
            print("missing render", n, file=sys.stderr)
            continue
        gp, bp = variants
        reads = {"gray": run(gp), "bin": run(bp)}
        rec = {
            "page": n,
            "reads": reads,
            "flags": diff_flags(reads["gray"], reads["bin"]),
        }
        with open(os.path.join(OUT, "p%04d.json" % n), "w") as fh:
            json.dump(rec, fh, ensure_ascii=False, indent=1)
        for p in (gp, bp):
            if os.path.exists(p):
                os.remove(p)
        print(n, "lines", len(reads["gray"]), "flags", len(rec["flags"]))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("first", type=int)
    ap.add_argument("last", type=int)
    ap.add_argument("--lang", default=LANG)
    ap.add_argument("--psm", default=PSM)
    ap.add_argument("--left", type=float, default=L)
    ap.add_argument("--right", type=float, default=R)
    ap.add_argument("--top", type=float, default=T)
    ap.add_argument("--bottom", type=float, default=B)
    a = ap.parse_args()
    LANG, PSM = a.lang, a.psm
    L, R, T, B = a.left, a.right, a.top, a.bottom
    main(a.first, a.last)
