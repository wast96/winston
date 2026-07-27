#!/usr/bin/env python3
"""Margin-cropped OCR of the body text block, in three stages.

Geometry for THIS book (顧順章 特務工作之理論與實際), measured off sixteen
sample pages spanning the whole book, recto and verso. This is a VERTICAL,
right-to-left, Traditional-character book, and its page furniture is not the
Juntong book's:

    - The body text block spans, as fractions of the full page:
        left ~0.05   right ~0.82   top ~0.14   bottom ~0.92
    - The RUNNING HEAD (特務工作之理論與實際) is a single vertical column in
      the OUTER margin, consistently on the RIGHT in this scan, at x ~0.85-0.92,
      with the FOLIO below it in the bottom-right. Both are excluded by the
      right crop at 0.84.
    - A RUNNING FOOT (the chapter title, e.g. 第三章 特務工作的方法) sits in the
      bottom margin just below the text block. Body descenders reach ~0.92, so
      the crop cannot cut low enough to drop the foot without clipping the last
      character of some columns; it is removed textually instead (strip_runfoot),
      the same tactic the Juntong/Wang Yaqiao pipeline used for the folio.
    - The top margin is blank (no header row); nothing to strip there.

    CROP: left 0.045   right 0.84   top 0.11   bottom 0.915

Chosen to keep every body glyph while excluding the running-head column and
its folio. Verified by OCR: at these bounds the running head does not appear
as a spurious extra column, which it does at right >= 0.86.

A HANDFUL OF PAGES (seen at PDF 45, 50, 200, 260 among the samples) carry heavy
dark-edge scan artifacts that no crop removes; OCR on those is noisier and they
are worth a crop-verify by eye.

OCR MODEL: chi_tra_vert with --psm 5 (single block of vertically aligned
text). Traditional, not simplified: chi_sim on this book is silent, systematic
corruption. PaddleOCR is the intended PRIMARY engine here (see ocr_dual.py and
check 1 in CLAUDE.md); this tesseract path is the diff partner and the fallback.

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

LEFT, RIGHT, TOP, BOTTOM = 0.045, 0.84, 0.11, 0.915

# OCR language/mode for this vertical Traditional book. Overridable via --lang.
LANG = "chi_tra_vert"
PSM = "5"

# The running head, for defensive textual filtering if a horizontally shifted
# page slips part of it inside the right crop. The crop already excludes it on
# clean pages.
RUNNING_HEAD = "特務工作之理論與實際顧順章著"


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
                    help="tesseract language; default chi_tra_vert (vertical "
                         "Traditional). NEVER chi_sim on this book.")
    ap.add_argument("--psm", default=PSM,
                    help="page-segmentation mode; default 5 (vertical block)")
    a = ap.parse_args()

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
