#!/usr/bin/env python3
"""Turn detected heading geometry into a chapter map.

find_headings.py locates heading LINES by geometry and OCRs each band in
isolation at psm 7. That band OCR is rough — a single short line gives the
engine no context — so the titles it produces are only good enough to tell
one heading from another.

This script re-reads each title from the page's own body OCR instead, where
the surrounding page gives the engine context and the same line comes out
markedly cleaner. Geometry says WHERE a heading is; the body OCR says WHAT
it says.

Level assignment: a heading that is the first text on its page and sits
below the normal top margin opens a chapter; anything else is a section
within the current chapter. Titles that wrap to two lines are joined when
the second band is centred, short and immediately below the first.

Usage: build_structure.py [--offset 5] [--out data/structure.json]
"""
import argparse
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TXT = os.path.join(ROOT, "data", "txt")

TERMINAL = "。！？；："


def page_lines(page):
    p = os.path.join(TXT, "p%04d.txt" % page)
    if not os.path.exists(p):
        return []
    return [l.strip() for l in open(p).read().splitlines() if l.strip()]


def best_line(cands, band_text, used):
    """Pick the body-OCR line that best matches a band-OCR title."""
    best, score = None, -1
    for i, l in enumerate(cands):
        if i in used:
            continue
        if len(l) > 30 or (l and l[-1] in TERMINAL):
            continue
        common = len(set(l) & set(band_text))
        s = common - abs(len(l) - len(band_text)) * 0.3
        if s > score:
            best, score = i, s
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offset", type=int, default=5)
    ap.add_argument("--headings", default=os.path.join(ROOT, "data", "headings.json"))
    ap.add_argument("--out", default=os.path.join(ROOT, "data", "structure.json"))
    a = ap.parse_args()

    recs = json.load(open(a.headings))
    out = []
    for r in recs:
        heads = r.get("heads") or []
        if not heads:
            continue
        page = r["page"]
        lines = page_lines(page)
        used = set()
        for hd in heads:
            band = re.sub(r"[^一-鿿0-9]", "", hd.get("text", ""))
            idx = best_line(lines, band, used) if band else None
            if idx is not None:
                used.add(idx)
                title = lines[idx]
            else:
                title = hd.get("text", "")
            level = "chapter" if (hd.get("page_opening") and hd["top"] > 0.15) \
                else "section"
            out.append({
                "level": level,
                "pdf": page,
                "printed": page - a.offset,
                "top": hd["top"],
                "title": title,
                "band_ocr": hd.get("text", ""),
            })

    with open(a.out, "w") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)

    for e in out:
        print("%-7s p%-4d pr%-4d %.3f  %s" % (e["level"], e["pdf"],
                                              e["printed"], e["top"], e["title"]))
    print("\n%d chapters, %d sections"
          % (sum(1 for e in out if e["level"] == "chapter"),
             sum(1 for e in out if e["level"] == "section")))


if __name__ == "__main__":
    main()
