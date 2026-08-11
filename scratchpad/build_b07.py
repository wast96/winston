#!/usr/bin/env python3
"""B07 builder: merged-paragraph pipeline for ch12 (the climax).

Copy of build_b06.py, re-ranged for one unit. Reads English one-paragraph-per-
line from scratchpad/ch12_en.txt, JSON-encodes to out/ch12_en.json, builds a
merged source (the bare-numeric divider lines 3/161/203/363 EXCLUDED), runs
make_bilingual (parity by construction) and split_bilingual, then post-inserts
'***' at the scene boundaries (cumulative paragraph counts).

ch12 is dialogue-heavy; each source body line is its own beat, so the mapping
is 1:1 (singles) throughout, matching the freshly-approved ch11 precedent.

  python3 scratchpad/build_b07.py ch12
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


# ch12 第十一章 第六根足趾 — dividers at source lines 3, 161, 203, 363 (bare
# numeric markers 01/02/03/04). Four scenes; the final scene (lines 364-1241)
# is the long one (878 lines). 1:1 mapping throughout (no extractor splits).
CH12 = (
    singles(4, 160)                                 # scene 1 (157 paras)
    + singles(162, 202)                             # scene 2 (41 paras)
    + singles(204, 362)                             # scene 3 (159 paras)
    + singles(364, 1241)                            # scene 4 (878 paras)
)
# *** after cumulative paragraph counts at each scene end: 157, 157+41=198,
# 198+159=357. No break after scene 4 (chapter end).
CH12_BREAKS = [157, 198, 357]


UNITS = {
    "ch12": ("data/src/17_part0000-split-015.txt",
             "Chapter 11. The Sixth Toe", "第十一章  第六根足趾",
             CH12, CH12_BREAKS),
}


if __name__ == "__main__":
    which = sys.argv[1:] or list(UNITS)
    for uid in which:
        src, title, zh, ranges, breaks = UNITS[uid]
        build(uid, os.path.join(ROOT, src), title, zh, ranges, breaks)
    print("B07 build step complete")
