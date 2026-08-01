#!/usr/bin/env python3
"""B02 bilingual generator: interleave VERBATIM source paragraphs (read straight
from data/src/*.txt, never re-typed) with the English from out/<id>_en.txt.

Per unit: skip the running-header line (黄慕兰自传), the chapter-title line, and the
caption-only lines (they go to figures.json / footnotes, not the reading text).
ch05 additionally prepends the Part Two 临江仙 poem, read verbatim from the part
divider file, matched to the italic English epigraph lines in ch05_en.txt.

Writes out/<id>_bilingual.md: a '## H2 <English title>' line, then paragraph pairs
of a '> <source>' line and the English line beneath.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def src_lines(name):
    path = os.path.join(ROOT, "data", "src", name)
    return [l.rstrip("\n") for l in open(path) if l.strip()]


# unit -> (source file, set of 1-indexed lines to DROP: header, title, captions)
DROP = {
    "ch04": ("09_index-split-007.txt", {1, 2, 8, 12, 13, 14, 18}),
    "ch05": ("11_index-split-009.txt", {1, 2, 7}),
    "ch06": ("12_index-split-010.txt", {1, 2, 5}),
    # B03: drop header(1) + title(2), then image captions.
    "ch07": ("13_index-split-011.txt", {1, 2, 26, 27}),   # two end-of-chapter photo captions
    "ch08": ("14_index-split-012.txt", {1, 2}),           # no images/captions
    "ch09": ("15_index-split-013.txt", {1, 2, 15, 16}),   # Chen family photo caption + roster
    # B04: both chapters have NO images, so only header(1) + title(2) drop.
    "ch10": ("16_index-split-014.txt", {1, 2}),
    "ch11": ("17_index-split-015.txt", {1, 2}),
}
# ch05 prepends the Part Two poem: file, 1-indexed lines to KEEP (title + 2 stanzas)
POEM = {"ch05": ("10_index-split-008.txt", [3, 4, 5])}


def build(unit):
    src_file, drop = DROP[unit]
    lines = src_lines(src_file)
    src_paras = []
    if unit in POEM:
        pfile, keep = POEM[unit]
        plines = src_lines(pfile)
        src_paras += [plines[i - 1] for i in keep]
    src_paras += [l for i, l in enumerate(lines, 1) if i not in drop]

    en = [l.rstrip("\n") for l in open(os.path.join(ROOT, "out", "%s_en.txt" % unit))
          if l.strip()]
    title, en_paras = en[0], en[1:]

    if len(src_paras) != len(en_paras):
        sys.exit("PARITY MISMATCH %s: source %d paras vs english %d paras"
                 % (unit, len(src_paras), len(en_paras)))

    out = ["## H2 %s" % title, ""]
    for zh, e in zip(src_paras, en_paras):
        out.append("> %s" % zh)
        out.append(e)
        out.append("")
    dest = os.path.join(ROOT, "out", "%s_bilingual.md" % unit)
    with open(dest, "w") as fh:
        fh.write("\n".join(out) + "\n")
    print("wrote %s (%d paragraph pairs)" % (dest, len(src_paras)))


if __name__ == "__main__":
    for u in sys.argv[1:] or ["ch04", "ch05", "ch06"]:
        build(u)
