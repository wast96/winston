#!/usr/bin/env python3
"""Survey-only OCR: crop furniture, run jpn_vert, keep paragraph blanks.

Deliberately does NOT apply ocr_crop.py's Chinese strip_folio/strip_runfoot
(strip_folio would delete a real short Japanese dialogue line ending in the
full stop; this book's furniture is all at the TOP and cropped away here).
Output feeds structural detection only; the batch pipeline re-OCRs properly.

Usage: ocr_survey.py FIRST LAST [--jobs 3]
Reads data/png_survey/p####.png, writes data/txt_survey/p####.txt
"""
import argparse
import os
import subprocess

import cv2

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PNG = os.path.join(ROOT, "data", "png_survey")
TXT = os.path.join(ROOT, "data", "txt_survey")
CROP = os.path.join(ROOT, "data", "crop_survey")

L, R, T, B = 0.035, 0.965, 0.075, 0.955


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("first", type=int)
    ap.add_argument("last", type=int)
    ap.add_argument("--jobs", type=int, default=3)
    a = ap.parse_args()
    os.makedirs(TXT, exist_ok=True)
    os.makedirs(CROP, exist_ok=True)
    todo = []
    for n in range(a.first, a.last + 1):
        src = os.path.join(PNG, "p%04d.png" % n)
        out = os.path.join(TXT, "p%04d.txt" % n)
        if not os.path.exists(src) or os.path.exists(out):
            continue
        img = cv2.imread(src)
        h, w = img.shape[:2]
        crop = img[int(h * T):int(h * B), int(w * L):int(w * R)]
        cv2.imwrite(os.path.join(CROP, "p%04d.png" % n), crop)
        todo.append(n)
    if not todo:
        print("nothing to do")
        return
    listfile = os.path.join(CROP, "todo.txt")
    with open(listfile, "w") as fh:
        for n in todo:
            fh.write("p%04d\n" % n)
    cmd = ("cat %s | OMP_THREAD_LIMIT=1 xargs -P %d -I{} "
           "tesseract %s/{}.png %s/{} -l jpn_vert --psm 5 2>/dev/null"
           % (listfile, a.jobs, CROP, TXT))
    subprocess.run(cmd, shell=True, check=False)
    # tidy crops
    for n in todo:
        c = os.path.join(CROP, "p%04d.png" % n)
        if os.path.exists(c):
            os.remove(c)
    print("OCR'd %d pages" % len(todo))


if __name__ == "__main__":
    main()
