#!/usr/bin/env python3
"""Margin-cropped OCR of the body text block, in three stages.

Geometry for THIS book, measured off fourteen sample pages rather than
assumed (the previous book in this pipeline needed a side-aware crop for a
vertical running title down the outer margin; this one has no running head
at all, so the crop is symmetric):

    ink bounds   left >= 0.083   right <= 0.946   top >= 0.073   bottom <= 0.900

The crop sits outside those bounds on every side so no glyph is clipped,
while still excluding the footer band holding the printed page number --
which is ink, and which OCR otherwise appends to the last line of the page
as a stray numeral. That matters more than it sounds: a stray numeral at a
page break is exactly what the numeric invariant check then reports as an
altered quantity.

WHY OMP_THREAD_LIMIT=1 IS NOT OPTIONAL. Standalone, a page costs 0.3s to
crop and ~2s to OCR. Run three pages at once WITHOUT this variable and each
one pins a core at 130% and does not finish in ten minutes -- three
processes produced nothing at all in seven hundred seconds, twice, once
through a thread pool and once through xargs. The cause is not the harness:
tesseract asks OpenMP for four threads per process, OpenMP threads
busy-wait, and twelve spinning threads on four cores starve each other
rather than merely sharing. One OMP thread per process, N processes, is
both faster and stable -- `-c 4.2s user` for the default against 1.7s
pinned, on the same page.

Killing a stalled run leaves the tesseract children ORPHANED and still
spinning; they survive the parent and must be killed by PID (verify with
pgrep) or every later run competes with them for the same four cores.

Usage: ocr_crop.py FIRST LAST [--jobs 3]
Writes: data/txt/p####.txt
"""
import argparse
import json
import os
import re
import subprocess

import cv2
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PNG = os.path.join(ROOT, "data", "png")
TXT = os.path.join(ROOT, "data", "txt")
CROPDIR = os.path.join(ROOT, "data", "crop")
RAWDIR = os.path.join(ROOT, "data", "raw")
INDENT = os.path.join(ROOT, "data", "indent")

CJK = r"一-鿿　-〿＀-￯"

LEFT, RIGHT, TOP, BOTTOM = 0.055, 0.965, 0.050, 0.905


def despace(line):
    """chi_sim puts a space between every glyph; drop only CJK-internal
    spaces so latin words and numerals keep theirs."""
    line = re.sub(r"(?<=[" + CJK + r"])\s+", "", line)
    line = re.sub(r"\s+(?=[" + CJK + r"])", "", line)
    return line.strip()


def folio_present(page):
    """Decide from the PAGE GEOMETRY whether a printed folio is present.

    The earlier version of this guessed from the text, dropping a short last
    line that carried at most one Han character. That rule deleted a real
    two-character line -- a paragraph whose final line was 写。 -- and with it
    the paragraph break that followed, silently merging two paragraphs of the
    book. Silent loss of text is the worst defect this pipeline can produce
    after invented text, so the guess is replaced by a measurement.

    A folio is unmistakable in the row profile and nothing else on the page
    looks like it: it sits alone below a gap far larger than the leading, and
    it is a few glyphs wide against a full measure. Either signal alone would
    misfire; together they do not.
    """
    img = cv2.imread(os.path.join(PNG, "p%04d.png" % page), cv2.IMREAD_GRAYSCALE)
    if img is None:
        return False
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
    if len(bands) < 3:
        return False
    gaps = [bands[i + 1][0] - bands[i][1] for i in range(len(bands) - 1)]
    med_gap = float(np.median(gaps))
    last_gap = gaps[-1]
    y0, y1 = bands[-1]
    cols = ink[y0:y1, :].sum(axis=0)
    nz = np.nonzero(cols > 0)[0]
    last_w = (nz[-1] - nz[0]) if len(nz) else 0
    widths = []
    for a, b in bands[:-1]:
        c = ink[a:b, :].sum(axis=0)
        n = np.nonzero(c > 0)[0]
        if len(n):
            widths.append(n[-1] - n[0])
    measure = float(np.median(widths)) if widths else w
    return bool(med_gap and last_gap > 1.35 * med_gap and last_w < 0.25 * measure)


# A folio the engine ran into a text line, e.g. "...告诉。" + "。34。." + "张师…".
# Matched anywhere in the line, not only at its end, because the merge does not
# always land last.
FOLIO_EMBED = re.compile(r"[。.·]\s*\d{1,3}\s*[。.·]\s*[.·]?")


def strip_folio(lines, page):
    """Drop the printed page number, but only when the page actually has one.

    Two shapes. Usually the folio is its own row band and OCR gives it its own
    line, which folio_present detects and the line is dropped. Occasionally the
    engine runs it onto the end of the last line of text instead, where it
    survives as a dot-wrapped numeral -- nine such across the book. Those are
    trimmed off the tail rather than deleting the line, because the line is
    real text. Left in place they are phantom quantities for the numeric check
    and, worse, silent additions to the author's prose.
    """
    while lines and not lines[-1].strip():
        lines.pop()
    if lines and folio_present(page):
        lines.pop()
    while lines and not lines[-1].strip():
        lines.pop()
    return trim_embedded_folios(lines)


def trim_embedded_folios(lines):
    """Remove a folio the engine merged into a line of text.

    Separate from the line-drop above because this one is IDEMPOTENT and the
    line-drop is not: re-running the line-drop on an already-cleaned page pops
    a second, real line. That is what --clean-only now restricts itself to.
    """
    out = []
    for l in lines:
        if l.strip():
            trimmed = FOLIO_EMBED.sub("。", l)
            if trimmed.strip():
                l = re.sub(r"。{2,}", "。", trimmed)
        out.append(l)
    return out


def indents_from_tsv(page, n_lines):
    """Left edge of each OCR line, and which lines are indented.

    Returns a list of booleans parallel to the page's non-blank text lines.
    The reference margin is the MODE of the line starts on this page, taken
    from the OCR's own lines, so a page with a wider gutter is judged against
    itself and no global or recto/verso calibration is needed.
    """
    tsv = os.path.join(RAWDIR, "p%04d.tsv" % page)
    if not os.path.exists(tsv):
        return [False] * n_lines
    lines = {}
    with open(tsv) as fh:
        next(fh, None)
        for row in fh:
            f = row.rstrip("\n").split("\t")
            if len(f) < 12 or f[11].strip() == "":
                continue
            key = (f[2], f[3], f[4])          # block, paragraph, line
            left, width = int(f[6]), int(f[8])
            cur = lines.get(key)
            if cur is None or left < cur[0]:
                lines[key] = (left, width)
    if not lines:
        return [False] * n_lines
    order = sorted(lines, key=lambda k: tuple(int(x) for x in k))
    starts = [lines[k][0] for k in order]
    step = 10
    binned = [round(s / float(step)) for s in starts]
    margin = max(set(binned), key=binned.count) * step
    char = 0.024 * 2258          # one Han character at the cropped render
    flags = [s > margin + 1.3 * char for s in starts]
    if len(flags) < n_lines:
        flags += [False] * (n_lines - len(flags))
    return flags[:n_lines]


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
    a = ap.parse_args()

    for d in (TXT, CROPDIR, RAWDIR):
        os.makedirs(d, exist_ok=True)

    if a.clean_only:
        n_done = 0
        for n in range(a.first, a.last + 1):
            p = os.path.join(TXT, "p%04d.txt" % n)
            if not os.path.exists(p):
                continue
            # NOT strip_folio: that drops a whole line and is not idempotent,
            # so re-running it on cleaned pages eats real text. Only the
            # idempotent embedded-folio trim is safe to re-apply.
            lines = trim_embedded_folios(open(p).read().split("\n"))
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
    # Ask for tsv alongside txt. The tsv carries a bounding box for every
    # word, and therefore the left edge of every OCR LINE -- which is the only
    # way to know the printed indent that cannot fall out of step with the
    # text. Deriving the indent from the page image separately and matching it
    # to the text by line index disagreed on 140 of 515 pages, because
    # tesseract's line grouping is not the printed line banding: it merges and
    # splits lines of its own accord. Same pass, same lines, no alignment.
    cmd = ("cat %s | OMP_THREAD_LIMIT=1 xargs -P %d -I{} "
           "tesseract %s/{}.png %s/{} -l chi_sim --psm 6 txt tsv 2>/dev/null"
           % (listfile, a.jobs, CROPDIR, RAWDIR))
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
        out = strip_folio(out, n)
        with open(os.path.join(TXT, "p%04d.txt" % n), "w") as fh:
            fh.write("\n".join(out))
        body = [l for l in out if l.strip()]
        flags = indents_from_tsv(n, len(body))
        os.makedirs(INDENT, exist_ok=True)
        with open(os.path.join(INDENT, "p%04d.json" % n), "w") as fh:
            json.dump(flags, fh)
        for ext in (".tsv",):
            q = os.path.join(RAWDIR, "p%04d%s" % (n, ext))
            if os.path.exists(q):
                os.remove(q)
        os.remove(raw)
        crop = os.path.join(CROPDIR, "p%04d.png" % n)
        if os.path.exists(crop):
            os.remove(crop)
        done += 1
    print("stage 3: %d pages written" % done)


if __name__ == "__main__":
    main()
