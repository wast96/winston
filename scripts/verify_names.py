#!/usr/bin/env python3
"""Crop-verify proper names and numerals against the page scan.

WHY TARGETED, NOT WHOLE-PAGE. Reading every rendered page image by eye is the
single most expensive thing you can do on a scanned-book project — on a real
book it was well over a hundred high-resolution image reads and it dominated
the budget. It also was not necessary. The documented failure mode of OCR on
CJK scans is NOT gibberish, which you would notice anyway; it is names and
numbers that come out as contextually plausible valid words. Those are the
dangerous errors, and they are a tiny fraction of the page.

So: OCR the page, extract the spans that can hurt you, and magnify ONLY those.
One image read of a name strip costs a fraction of a full page, and catches
the same defects.

Real catches from this method on one book:
  沈钧侨 → 沈钧儒 (a famous jurist, mangled into a nobody)
  姚神父路 → 金神父路 (a street that does not exist → Route Pere Robert)
  山本大作 → the author's own error for 河本大作, caught because the name
             was crop-verified and then checked against the record

Usage:
    verify_names.py --pdf source.pdf --page 143 --terms 沈钧儒 1932年11月2日
    verify_names.py --pdf source.pdf --page 143 --auto      # extract candidates
"""
import argparse
import os
import re
import subprocess
import sys

SCRATCH = os.environ.get('SCRATCH', '/tmp')

# Characters that are grammar, never the first character of a name. Without
# this the place-name pattern greedily swallows the particles in front of the
# name — "在他赵铁" for 赵铁桥 — and the output is unreadable junk.
STOP = set('的了是在有和与也都就还很把被将从对给让使为以及而或即但却'
           '这那哪其此该他她它我你您们个是不没无很最更太真已经又再')

# Common surnames. Anchoring on these is what makes personal-name extraction
# work: OCR mangles names into contextually plausible words, and a mangled
# name almost always keeps its (high-frequency, well-printed) surname.
SURNAME = ('王李张刘陈杨黄赵周吴徐孙马朱胡林郭何高罗郑梁谢宋唐许韩冯邓曹'
           '彭曾萧田董袁潘于蒋蔡余杜叶程苏魏吕丁任沈姚卢姜崔钟谭陆汪范金'
           '石廖贾夏韦付方白邹孟熊秦邱江尹薛闫段雷侯龙史陶黎贺顾毛郝龚邵'
           '万钱严覃武戴莫孔向汤')

NUMERIC = re.compile(
    r'[0-9]{2,4}年[0-9]{1,2}月[0-9]{1,2}日'       # full dates
    r'|[0-9]{1,4}[年月日号元万千百]'                # numeric + unit
    r'|第[0-9一二三四五六七八九十]+[军师旅团营连]'      # unit numbers: load-bearing
)
# A surname followed by one or two given-name characters.
PERSON = re.compile(r'[%s][一-鿿]{1,2}' % SURNAME)
# 2-3 characters immediately before a place suffix, suffix included.
PLACE = re.compile(r'[一-鿿]{2,3}(?:路|街|巷|里|弄|桥|寺|山|楼|馆)')


def candidates(text):
    """Extract spans worth an eyeball, dropping obvious grammatical junk."""
    out = set(NUMERIC.findall(text))
    for pat in (PERSON, PLACE):
        for m in pat.findall(text):
            # Any function word inside means the window straddled a boundary
            # rather than landing on a name.
            if not (set(m) & STOP):
                out.add(m)
    return sorted(out)


def render_page(pdf, page, dpi=300):
    """PyMuPDF only. Poppler cannot decode many JBIG2 scans."""
    import fitz
    doc = fitz.open(pdf)
    out = os.path.join(SCRATCH, 'p%04d.png' % page)
    doc[page - 1].get_pixmap(dpi=dpi).save(out)
    return out


def ocr(img, psm='6', lang='chi_sim'):
    r = subprocess.run(['tesseract', img, 'stdout', '-l', lang, '--psm', psm],
                       capture_output=True, text=True)
    return r.stdout


def crop_around(img, term, text, pad=140):
    """Magnify the band of the page containing `term`.

    Locates by line index in the OCR, which is approximate but good enough to
    put the term inside a readable strip.
    """
    from PIL import Image
    lines = text.split('\n')
    idx = next((i for i, l in enumerate(lines) if term in l), None)
    if idx is None:
        return None
    im = Image.open(img)
    W, H = im.size
    frac = idx / max(1, len(lines))
    y = int(H * frac)
    box = (0, max(0, y - pad), W, min(H, y + pad))
    crop = im.crop(box).resize(((box[2] - box[0]) * 2, (box[3] - box[1]) * 2),
                               Image.LANCZOS)
    out = os.path.join(SCRATCH, 'verify_%s.png' % re.sub(r'\W', '', term)[:20])
    crop.save(out)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pdf', required=True)
    ap.add_argument('--page', type=int, required=True)
    ap.add_argument('--terms', nargs='*', default=[])
    ap.add_argument('--auto', action='store_true',
                    help='extract candidate names/numbers from the OCR')
    ap.add_argument('--all', action='store_true',
                    help='with --auto, show every candidate rather than only '
                         'the ones the two OCR configs disagree on')
    ap.add_argument('--dpi', type=int, default=300)
    a = ap.parse_args()

    img = render_page(a.pdf, a.page, a.dpi)
    text = ocr(img)

    terms = list(a.terms)
    if a.auto:
        terms += [c for c in candidates(text) if c not in terms]
    if not terms:
        print("no terms to verify; pass --terms or --auto")
        return 0

    # ONE second pass over the whole page, not one per term. A different psm
    # is a free second opinion: where two configs disagree, the scan is hard
    # and the reading is at risk. Running this inside the loop re-OCRs the
    # same page N times and is the difference between one second and a minute.
    alt = ocr(img, psm='4')

    # Terms named explicitly are always shown — you asked about them. Terms
    # found by --auto are filtered to the disagreements unless --all, because
    # that is the whole point: a span both configs read identically is not
    # where the risk is, and cropping it costs an image read for nothing.
    risky = [t for t in terms if t not in alt]
    shown = terms if (a.all or not a.auto) else (
        [t for t in a.terms] + [t for t in risky if t not in a.terms])

    print("page %d — %d candidate(s), %d disagreement(s), showing %d\n"
          % (a.page, len(terms), len(risky), len(shown)))
    for t in shown:
        crop = crop_around(img, t, text)
        print("  %-22s dual-OCR agrees: %-5s  crop: %s"
              % (t, t in alt, crop or 'NOT LOCATED'))

    if not shown:
        print("  (both OCR configs agree on every candidate)")
    print("\nRead ONLY the crops where dual-OCR disagreed. Do not read the")
    print("whole page. Expect junk among auto candidates: Chinese surnames")
    print("are also common words (马上, 顾左右, 郑重), so the extractor")
    print("cannot tell a name from an idiom. The disagreement filter can.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
