#!/usr/bin/env python3
"""B08 builder: merged-paragraph pipeline for ch13 (the coda / 尾声).

Copy of build_b07.py, re-ranged for one unit. Reads English one-paragraph-per-
line from scratchpad/ch13_en.txt, JSON-encodes to out/ch13_en.json, builds a
merged source, runs make_bilingual (parity by construction) and split_bilingual.

ch13 is short (one scene, NO bare-numeric dividers → NO '***' breaks) and has
NO extractor splits (every body line 3-119 ends on terminal punctuation,
re-verified). The two trailing publisher lines are EXCLUDED from the body:
  line 120  《陆小凤传奇：金鹏王朝》完                (the volume-END marker)
  line 121  相关情节请看《陆小凤传奇2：绣花大盗》     (a next-volume teaser)
Both are recorded in book.json _source_note and surfaced in a closing
translator's footnote; they are not story text and carry no story content.
Mapping is 1:1 (singles) throughout.

  python3 scratchpad/build_b08.py ch13
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


# ch13 第十二章 尾声 (Coda). One scene, no dividers. Body = source lines 3-119
# (117 paragraphs, 1:1). Lines 120-121 (END marker + sequel teaser) excluded.
CH13 = singles(3, 119)
CH13_BREAKS = []


UNITS = {
    "ch13": ("data/src/18_part0000-split-016.txt",
             "Chapter 12. Coda", "第十二章  尾 声",
             CH13, CH13_BREAKS),
}


if __name__ == "__main__":
    which = sys.argv[1:] or list(UNITS)
    for uid in which:
        src, title, zh, ranges, breaks = UNITS[uid]
        build(uid, os.path.join(ROOT, src), title, zh, ranges, breaks)
    print("B08 build step complete")
