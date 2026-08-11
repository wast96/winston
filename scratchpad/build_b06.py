#!/usr/bin/env python3
"""B06 builder: merged-paragraph pipeline for ch09, ch10, ch11.

Copy of build_b05.py, re-ranged. Reads English one-paragraph-per-line from
scratchpad/<id>_en.txt, JSON-encodes to out/<id>_en.json, builds a merged
source (bare-numeric divider lines EXCLUDED), runs make_bilingual (parity by
construction) and split_bilingual, then post-inserts '***' at the scene
boundaries (cumulative paragraph counts).

  python3 scratchpad/build_b06.py ch09     # one unit
  python3 scratchpad/build_b06.py          # all three
"""
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "scripts")
SCRATCH = os.path.join(ROOT, "scratchpad")


def merged_source(src_txt, ranges, dest):
    lines = [l.rstrip("\n") for l in open(src_txt, encoding="utf-8")]
    out = [lines[0], lines[1]]                    # the two title/stub lines
    for a, b in ranges:
        out.append("".join(lines[a - 1:b]))       # 1-indexed, verbatim join
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    return len(out) - 2


def write_en_json(uid, ranges):
    txt = os.path.join(SCRATCH, "%s_en.txt" % uid)
    paras = [l.rstrip("\n") for l in open(txt, encoding="utf-8")]
    while paras and paras[-1] == "":
        paras.pop()
    if len(paras) != len(ranges):
        sys.exit("%s: %d en.txt paragraphs but %d ranges" %
                 (uid, len(paras), len(ranges)))
    dest = os.path.join(ROOT, "out", "%s_en.json" % uid)
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(paras, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    return dest


def run(*args):
    r = subprocess.run([sys.executable] + list(args), capture_output=True,
                       text=True)
    sys.stdout.write(r.stdout)
    if r.returncode:
        sys.stdout.write(r.stderr)
        sys.exit("FAILED: %s" % " ".join(args))


def insert_breaks(reading_path, after_paras):
    blocks = open(reading_path, encoding="utf-8").read().split("\n\n")
    for k in sorted(after_paras, reverse=True):
        blocks.insert(k + 1, "***")
    with open(reading_path, "w", encoding="utf-8") as fh:
        fh.write("\n\n".join(blocks) + ("\n" if not blocks[-1].endswith("\n")
                                        else ""))


def build(uid, src_txt, title_en, zh_title, ranges, breaks):
    write_en_json(uid, ranges)
    merged = os.path.join(ROOT, "out", "%s_src_merged.txt" % uid)
    n = merged_source(src_txt, ranges, merged)
    print("%s: %d merged paragraphs" % (uid, n))
    run(os.path.join(SCRIPTS, "make_bilingual.py"), uid, merged, title_en,
        os.path.join(ROOT, "out", "%s_en.json" % uid), "2")
    run(os.path.join(SCRIPTS, "split_bilingual.py"),
        os.path.join(ROOT, "out", "%s_bilingual.md" % uid), uid, zh_title)
    reading = os.path.join(ROOT, "out", "%s_reading.md" % uid)
    insert_breaks(reading, breaks)
    print("%s: inserted *** after paragraphs %s" % (uid, breaks))


def spans(*items):
    return [it if isinstance(it, tuple) else (it, it) for it in items]


def singles(a, b):
    return [(n, n) for n in range(a, b + 1)]


# ch09 第八章 峨嵋四秀 — dividers at source lines 3, 26, 117, 176, 239.
CH09 = (
    spans((4, 5), (6, 7)) + singles(8, 25)                       # scene 1
    + spans((27, 28), (29, 31), (32, 32), (33, 34), (35, 36),
            (37, 38), (39, 39), (40, 41), (42, 43), (44, 44),
            (45, 45), (46, 46), (47, 48), (49, 49), (50, 51),
            (52, 52), (53, 54), (55, 55), (56, 57), (58, 59),
            (60, 60)) + singles(61, 116)                         # scene 2
    + spans((118, 119), (120, 120)) + singles(121, 129)
    + spans((130, 132), (133, 133), (134, 135)) + singles(136, 139)
    + spans((140, 141), (142, 143)) + singles(144, 145)
    + spans((146, 146), (147, 147)) + singles(148, 158)
    + spans((159, 160), (161, 162)) + singles(163, 167)
    + spans((168, 168), (169, 169), (170, 170), (171, 171),
            (172, 172), (173, 173), (174, 175))                  # scene 3
    + spans((177, 177), (178, 178), (179, 180)) + singles(181, 238)  # scene 4
    + spans((240, 242)) + singles(243, 317)                      # scene 5
)
CH09_BREAKS = [20, 97, 146, 207]


# ch10 第九章 飞燕去来 — dividers at source lines 3, 106.
CH10 = (
    spans((4, 5)) + singles(6, 105)                              # scene 1
    + spans((107, 108), (109, 109), (110, 111)) + singles(112, 244)  # scene 2
)
CH10_BREAKS = [101]

# ch11 第十章 迷楼 — dividers at source lines 3, 112, 179, 234. Source lines
# 43-44 are the two lines of the threat-verse (line 43 ends on a comma, an
# extractor split); merged into one paragraph.
CH11 = (
    singles(4, 42) + spans((43, 44)) + singles(45, 111)          # scene 1
    + singles(113, 178)                                          # scene 2
    + singles(180, 233)                                          # scene 3
    + singles(235, 296)                                          # scene 4
)
CH11_BREAKS = [107, 173, 227]


UNITS = {
    "ch09": ("data/src/14_part0000-split-012.txt",
             "Chapter 8. The Four Beauties of Emei", "第八章  峨嵋四秀",
             CH09, CH09_BREAKS),
    "ch10": ("data/src/15_part0000-split-013.txt",
             "Chapter 9. The Flying Swallow Comes and Goes", "第九章  飞燕去来",
             CH10, CH10_BREAKS),
    "ch11": ("data/src/16_part0000-split-014.txt",
             "Chapter 10. The Maze Tower", "第十章  迷 楼",
             CH11, CH11_BREAKS),
}


if __name__ == "__main__":
    which = sys.argv[1:] or list(UNITS)
    for uid in which:
        src, title, zh, ranges, breaks = UNITS[uid]
        build(uid, os.path.join(ROOT, src), title, zh, ranges, breaks)
    print("B06 build step complete")
