#!/usr/bin/env python3
"""Margin-cropped OCR of the body text block, in three stages.

FIRST ENGINEERING TASK OF ANY NEW BOOK: measure this book's page geometry.
Scanned books print furniture in the margins -- a running head, a running foot
(often the chapter title), and a folio (page number) in an outer corner. Left in
the OCR they corrupt the ends of lines and inject phantom columns and numerals.
This script crops the furniture away before OCR, then strips whatever survives
textually. The crop box is BOOK-SPECIFIC and MUST be measured.

How to measure: render a dozen pages spanning the book (render.py), open several
recto and several verso pages, and read off the fractional bounds (0..1 of page
width/height) of the body text block, just inside the furniture. Pass them with
--left/--right/--top/--bottom. The defaults below are the whole page (no crop) --
WRONG for any real book; they exist only so the script runs before you measure.

  Example (a vertical Traditional book, running head down the right margin,
  folio at the foot):
    ocr_crop.py 27 42 --left 0.045 --right 0.84 --top 0.11 --bottom 0.915 \\
                --lang chi_tra_vert --psm 5 --running-head "書名作者著"

CHOOSE THE RIGHT OCR MODEL. Simplified vs Traditional matters: the simplified
model on a Traditional book is silent, systematic corruption, and vice versa.
chi_tra / chi_tra_vert for Traditional, chi_sim / chi_sim_vert for simplified;
--psm 5 for vertical (right-to-left) text, --psm 6 for horizontal. Where it
installs, PaddleOCR is a stronger primary engine and tesseract the diff partner
(see the eight checks in CLAUDE.md); this path is the tesseract fallback.

WHY OMP_THREAD_LIMIT=1 IS NOT OPTIONAL. Standalone, a page costs ~0.3s to crop
and ~2s to OCR. Run several at once WITHOUT this variable and each pins a core
and never finishes: tesseract asks OpenMP for four threads per process, those
threads busy-wait, and a dozen spinning threads on four cores starve each other.
One OMP thread per process, N processes, is faster and stable. The xargs
invocation below sets it; keep it.

Killing a stalled run leaves the tesseract children ORPHANED and still spinning;
they survive the parent and must be killed by PID (verify with `pgrep -c
tesseract`, which must read 0 when idle) or every later run competes with them.

Usage: ocr_crop.py FIRST LAST [--left --right --top --bottom
                               --lang --psm --running-head --jobs]
Writes: data/txt/p####.txt
"""
import argparse
import os
import re
import subprocess

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PNG = os.path.join(ROOT, "data", "png")
TXT = os.path.join(ROOT, "data", "txt")
CROPDIR = os.path.join(ROOT, "data", "crop")
RAWDIR = os.path.join(ROOT, "data", "raw")

CJK = r"一-鿿　-〿＀-￯"

# Whole-page defaults (no crop). MEASURE your book and override on the command
# line; see the module docstring. These values will NOT give clean OCR as-is.
LEFT, RIGHT, TOP, BOTTOM = 0.0, 1.0, 0.0, 1.0

# Default OCR model/mode. Override per book: chi_tra_vert/chi_sim_vert + psm 5
# for vertical, chi_tra/chi_sim + psm 6 for horizontal.
LANG = "chi_tra_vert"
PSM = "5"

# The running head string, for defensive textual filtering if a shifted page
# slips part of it inside the crop. Set via --running-head to your book's
# running head (title + author as printed in the margin). Empty disables it.
RUNNING_HEAD = ""


def despace(line):
    """chi_sim puts a space between every glyph; drop only CJK-internal
    spaces so latin words and numerals keep theirs."""
    line = re.sub(r"(?<=[" + CJK + r"])\s+", "", line)
    line = re.sub(r"\s+(?=[" + CJK + r"])", "", line)
    return line.strip()


def strip_folio(lines):
    """Drop the printed page number if it survived the crop.

    No crop can do this. Measured over the book, the last body line reaches
    0.9117 of page height on some pages while the folio begins at 0.8890 on
    others, so the two bands overlap globally even though the folio is always
    below the text on any single page. A fixed cut either keeps folios or
    eats real text.

    So it is filtered textually. The folio prints as a dot-delimited numeral
    -- '. 181 .' -- and OCR mangles the digits freely ('。人。', '。1]，。',
    '4。'), so the digits cannot be relied on. What survives every mangle is
    the shape: very short, dot-delimited, and at most one Han character,
    where a real closing line of Chinese prose has several. Left in place a
    folio becomes both a spurious one-line paragraph and a phantom numeral
    for the numeric-invariant check to report.
    """
    while lines and not lines[-1].strip():
        lines.pop()
    if lines:
        last = lines[-1].strip()
        han = len(re.findall(r"[一-鿿]", last))
        dotted = bool(re.match(r"^[.。·、,，\s]", last) or
                      re.search(r"[.。·、,，\s]$", last))
        if len(last) <= 8 and han <= 1 and dotted:
            lines.pop()
    return lines


def _line_bands(page):
    """Text-line bands of a FULL-page render, top to bottom, each
    {y0,y1,x0,x1} in pixels. Kept byte-for-byte identical to
    indents.line_starts' band detection so that folio_present and the indent
    measurement can never disagree about what "the last line" is (two copies
    of that test once disagreed on 140 of 515 pages, sliding whole pages out
    of step). Returns (bands, w, h) or None if the render is missing."""
    import cv2
    import numpy as np
    img = cv2.imread(os.path.join(PNG, "p%04d.png" % page), cv2.IMREAD_GRAYSCALE)
    if img is None:
        return None
    h, w = img.shape
    ink = (img < 160).astype(np.uint8)
    rows = ink.sum(axis=1)
    bands, start = [], None
    for i, v in enumerate(rows):
        if v > 4 and start is None:
            start = i
        elif v <= 4 and start is not None:
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


def folio_present(page):
    """Does this FULL-page render carry a folio as its last text band?

    The folio prints as a short, isolated numeral at the very foot ('. 2 .'),
    set well below the last line of prose. indents.py calls this to drop that
    band before it measures paragraph indents, so its per-line flags line up
    with the folio-free CROPPED OCR text.

    The digits are OCR-unreliable, so the test is purely geometric, and the
    third clause is the one that matters: a folio is separated from the prose
    above it by a clear vertical GAP, whereas a genuinely short LAST LINE of a
    paragraph sits one ordinary line-height below its predecessor. Testing only
    "short and low" would delete real short closing lines (the failure that
    once silently ate the last line of 41% of a chapter's pages); requiring the
    gap does not. Scanner speckle in the foot margin is wider than a folio and
    fails the narrowness clause, so it does not trip the test either."""
    got = _line_bands(page)
    if not got:
        return False
    lines, w, h = got
    if len(lines) < 2:
        return False
    import numpy as np
    measure = float(np.median([l["x1"] - l["x0"] for l in lines]))
    line_h = float(np.median([l["y1"] - l["y0"] for l in lines])) or 1.0
    last, prev = lines[-1], lines[-2]
    narrow = (last["x1"] - last["x0"]) < 0.35 * measure
    low = last["y0"] > 0.85 * h
    gap = (last["y0"] - prev["y1"]) > 0.7 * line_h
    return bool(narrow and low and gap)


def strip_runfoot(lines):
    """Drop the running foot (the chapter title) if it survived the crop.

    Body descenders reach ~0.92 of page height, the foot sits just below, so the
    crop keeps a sliver of it on some pages. The foot is the chapter title,
    '第X章 ...', printed once per page in the bottom margin. It cannot be blanket
    filtered because the same string is a REAL heading on a chapter's opening
    page -- but there it is near the top, never the last line. So: strip it only
    when it is the last non-empty line of the page.
    """
    while lines and not lines[-1].strip():
        lines.pop()
    if lines:
        last = lines[-1].strip()
        if len(last) <= 16 and re.match(r"^第[一二三四五六七八九十百]+章", last):
            lines.pop()
    return lines


def strip_head(lines):
    """Drop any line that is really a slice of the running-head column.

    Defensive only; the right crop excludes the head on clean pages. A line of
    four or more Han characters that appear as a contiguous run inside
    RUNNING_HEAD, and nothing else, is the head, not prose.
    """
    out = []
    for l in lines:
        s = re.sub(r"\s", "", l)
        han = re.sub(r"[^一-鿿]", "", s)
        if len(han) >= 4 and han in RUNNING_HEAD and len(s) - len(han) <= 1:
            continue
        out.append(l)
    return out


def make_crop(page):
    src = os.path.join(PNG, "p%04d.png" % page)
    if not os.path.exists(src):
        return None
    dest = os.path.join(CROPDIR, "p%04d.png" % page)
    if os.path.exists(dest):
        return dest
    im = Image.open(src)
    w, h = im.size
    box = (int(w * LEFT), int(h * TOP), int(w * RIGHT), int(h * BOTTOM))
    im.crop(box).convert("L").save(dest)
    return dest


def main():
    global LEFT, RIGHT, TOP, BOTTOM, RUNNING_HEAD
    ap = argparse.ArgumentParser()
    ap.add_argument("first", type=int)
    ap.add_argument("last", type=int)
    ap.add_argument("--clean-only", action="store_true",
                    help="re-apply stage 3 filtering to pages already OCR'd, "
                         "without re-running tesseract")
    ap.add_argument("--jobs", type=int, default=3,
                    help="stay below core count; tesseract already threads "
                         "internally and oversubscription is what drove load "
                         "to 12 on 4 cores on the last attempt")
    ap.add_argument("--lang", default=LANG,
                    help="tesseract language; e.g. chi_tra_vert / chi_sim_vert "
                         "(vertical) or chi_tra / chi_sim (horizontal). Match "
                         "the book's SCRIPT (Traditional vs simplified) exactly.")
    ap.add_argument("--psm", default=PSM,
                    help="page-segmentation mode; 5 for vertical, 6 horizontal")
    ap.add_argument("--left", type=float, default=LEFT,
                    help="crop: left edge of text block, fraction 0..1 of width")
    ap.add_argument("--right", type=float, default=RIGHT,
                    help="crop: right edge, fraction 0..1 (excludes outer margin)")
    ap.add_argument("--top", type=float, default=TOP,
                    help="crop: top edge, fraction 0..1 of height")
    ap.add_argument("--bottom", type=float, default=BOTTOM,
                    help="crop: bottom edge, fraction 0..1 (excludes foot/folio)")
    ap.add_argument("--running-head", default=RUNNING_HEAD,
                    help="the book's running head (title+author as printed in "
                         "the margin); used to filter stray head columns. Empty "
                         "disables that filter.")
    a = ap.parse_args()

    LEFT, RIGHT, TOP, BOTTOM = a.left, a.right, a.top, a.bottom
    RUNNING_HEAD = a.running_head

    for d in (TXT, CROPDIR, RAWDIR):
        os.makedirs(d, exist_ok=True)

    if a.clean_only:
        n_done = 0
        for n in range(a.first, a.last + 1):
            p = os.path.join(TXT, "p%04d.txt" % n)
            if not os.path.exists(p):
                continue
            lines = strip_runfoot(strip_folio(strip_head(
                open(p).read().split("\n"))))
            with open(p, "w") as fh:
                fh.write("\n".join(lines))
            n_done += 1
        print("re-cleaned %d pages" % n_done)
        return

    def pending(n):
        p = os.path.join(TXT, "p%04d.txt" % n)
        return not os.path.exists(p) or os.path.getsize(p) == 0

    todo = [n for n in range(a.first, a.last + 1) if pending(n)]
    if not todo:
        print("nothing to do")
        return

    # stage 1: crops
    crops = [c for c in (make_crop(n) for n in todo) if c]
    print("stage 1: %d crops" % len(crops), flush=True)

    # stage 2: OCR, one process per page, no pipes back to this parent
    listfile = os.path.join(RAWDIR, "todo.txt")
    with open(listfile, "w") as fh:
        for c in crops:
            fh.write("%s\n" % os.path.splitext(os.path.basename(c))[0])
    cmd = ("cat %s | OMP_THREAD_LIMIT=1 xargs -P %d -I{} "
           "tesseract %s/{}.png %s/{} -l %s --psm %s 2>/dev/null"
           % (listfile, a.jobs, CROPDIR, RAWDIR, a.lang, a.psm))
    subprocess.run(cmd, shell=True, check=False)
    print("stage 2: OCR done", flush=True)

    # stage 3: normalise whitespace and file per page
    #
    # KEEP THE BLANK LINES. tesseract drops the source's two-space paragraph
    # indent, but it marks a paragraph end by emitting an empty line, and
    # that is the only paragraph signal the OCR carries. An earlier version
    # filtered empties out as noise, which silently destroyed the paragraph
    # structure the parity check exists to verify. Runs of blanks collapse
    # to one; leading and trailing blanks go.
    done = 0
    for n in todo:
        raw = os.path.join(RAWDIR, "p%04d.txt" % n)
        if not os.path.exists(raw):
            continue
        lines, out = [despace(l) for l in open(raw).read().splitlines()], []
        for l in lines:
            if not l and (not out or not out[-1]):
                continue
            out.append(l)
        out = strip_runfoot(strip_folio(strip_head(out)))
        with open(os.path.join(TXT, "p%04d.txt" % n), "w") as fh:
            fh.write("\n".join(out))
        os.remove(raw)
        crop = os.path.join(CROPDIR, "p%04d.png" % n)
        if os.path.exists(crop):
            os.remove(crop)
        done += 1
    print("stage 3: %d pages written" % done)


if __name__ == "__main__":
    main()
