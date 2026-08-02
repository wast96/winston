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
    # B05: ch12 has 9 photo captions (lines 7,11,13,15,21,31,32[roster],33,42,44)
    # AND a trailing 【注释】 block (lines 45-49) that belongs to earlier chapters'
    # endnotes (ch05[1], ch08[2], ch11[3]/[4]) -- NOT ch12 body text -- so drop it.
    "ch12": ("18_index-split-016.txt",
             {1, 2, 7, 11, 13, 15, 21, 31, 32, 33, 42, 44, 45, 46, 47, 48, 49}),
    # ch13 opens Part Three; 5 photo captions (lines 4,8,11,12[roster],19,22).
    "ch13": ("20_index-split-018.txt", {1, 2, 4, 8, 11, 12, 19, 22}),
    # ch14 has NO images, so only header(1) + title(2) drop.
    "ch14": ("21_index-split-019.txt", {1, 2}),
    # B06: ch15 has 5 photo captions -- line 7 (Fanmaji-costume charity photo, img
    # 00037) with its inscribed poem on line 8; line 13 (lawyers' team, 00038) with
    # its roster line 14; line 26 (charity-sale painting, 00039); line 27 (early-
    # resistance group, 00040); line 31 (reversed relief-shelter caption, 00041).
    "ch15": ("22_index-split-020.txt", {1, 2, 7, 8, 13, 14, 26, 27, 31}),
    # ch16 has 3 photo captions -- line 9 (Documents masthead, 00042); line 10 (the
    # couplet, 00043); line 31 (Shanghai Women cover, 00044) with its 说明 roster
    # line 32. The 风雨书屋 publication list (lines 7,8,11-15) is BODY text, kept.
    "ch16": ("23_index-split-021.txt", {1, 2, 9, 10, 31, 32}),
    # B07: ch17 has 5 photo captions -- line 8 (Chen Xunshe couple, 00045); line 14
    # (Du Yuesheng portrait, 00046); line 19 (1991 visit to Wu Jufang, 00047); line
    # 21 (Niuwei garden party, 00048) with its roster line 22; line 25 (1940 with
    # Wang Huazhen, 00049).
    "ch17": ("24_index-split-022.txt", {1, 2, 8, 14, 19, 21, 22, 25}),
    # ch18 has NO images, so only header(1) + title(2) drop.
    "ch18": ("25_index-split-023.txt", {1, 2}),
    # ch19 has 1 photo caption -- line 4 (Zhigao with First International Shelter
    # colleagues, 00050) with its roster line 5.
    "ch19": ("26_index-split-024.txt", {1, 2, 4, 5}),
}
# Part-opening chapters prepend the part's 临江仙 poem: file, 1-indexed lines to
# KEEP (poem title + 2 stanzas). ch05 = Part Two; ch13 = Part Three.
POEM = {
    "ch05": ("10_index-split-008.txt", [3, 4, 5]),
    "ch13": ("19_index-split-017.txt", [3, 4, 5]),
}


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
