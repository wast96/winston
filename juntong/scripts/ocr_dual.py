#!/usr/bin/env python3
"""QC step 1: two independent OCR reads per page, diffed at character level.

PaddleOCR is the better second engine for Chinese but its model weights
download from a host outside the sandbox allowlist, so it is unavailable.
Substitute: tesseract chi_sim under two page-segmentation modes (psm 4
column-aware, psm 6 uniform block) plus an inverted-threshold variant.
These fail differently enough to surface most character-level trouble.

Anything the reads disagree on is written to a flag list for visual
adjudication against the rendered scan.

Usage: ocr_dual.py FIRST LAST
Writes: data/ocr/p####.json  {page, reads: {name: [lines]}, flags: [...]}
"""
import difflib
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PNG = os.path.join(ROOT, "data", "png")
OUT = os.path.join(ROOT, "data", "ocr")

CJK = r"\u4e00-\u9fff\u3000-\u303f\uff00-\uffef"
CONFIGS = [("psm6", ["--psm", "6"]), ("psm4", ["--psm", "4"])]


def despace(line):
    """chi_sim emits a space between every glyph; drop only CJK-internal
    spaces so latin words and numbers keep their spacing."""
    line = re.sub(r"(?<=[" + CJK + r"])\s+", "", line)
    line = re.sub(r"\s+(?=[" + CJK + r"])", "", line)
    return line.strip()


def run(img, extra):
    proc = subprocess.run(
        ["tesseract", img, "stdout", "-l", "chi_sim"] + extra,
        capture_output=True, text=True,
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
    for n in range(first, last + 1):
        img = os.path.join(PNG, "p%04d.png" % n)
        if not os.path.exists(img):
            print("missing render", n, file=sys.stderr)
            continue
        reads = {name: run(img, extra) for name, extra in CONFIGS}
        rec = {
            "page": n,
            "reads": reads,
            "flags": diff_flags(reads["psm6"], reads["psm4"]),
        }
        with open(os.path.join(OUT, "p%04d.json" % n), "w") as fh:
            json.dump(rec, fh, ensure_ascii=False, indent=1)
        print(n, "lines", len(reads["psm6"]), "flags", len(rec["flags"]))


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))
