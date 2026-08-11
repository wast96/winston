#!/usr/bin/env python3
"""B05 builder: merged-paragraph pipeline for ch07 and ch08.

Same method as build_b04.py (see that file): the English paragraphs are
authored one-per-line in scratchpad/<id>_en.txt (no JSON escaping to fight);
this script JSON-encodes them to out/<id>_en.json, builds a merged source by
concatenating each paragraph group's original source lines VERBATIM (bare
numeric divider lines EXCLUDED), runs make_bilingual (parity by construction)
and split_bilingual, then post-inserts '***' at the scene boundaries.

RANGES and the en.txt lines are kept in lock-step: assert len(RANGES) ==
len(en lines) before anything else, so a drafting slip fails loudly here
rather than as a mysterious parity mismatch downstream.
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
    # a trailing blank line from the editor is not a paragraph
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
    en_json = write_en_json(uid, ranges)
    merged = os.path.join(ROOT, "out", "%s_src_merged.txt" % uid)
    n = merged_source(src_txt, ranges, merged)
    print("%s: %d merged paragraphs" % (uid, n))
    run(os.path.join(SCRIPTS, "make_bilingual.py"), uid, merged, title_en,
        en_json, "2")
    run(os.path.join(SCRIPTS, "split_bilingual.py"),
        os.path.join(ROOT, "out", "%s_bilingual.md" % uid), uid, zh_title)
    reading = os.path.join(ROOT, "out", "%s_reading.md" % uid)
    insert_breaks(reading, breaks)
    print("%s: inserted *** after paragraphs %s" % (uid, breaks))


def spans(*items):
    out = []
    for it in items:
        out.append(it if isinstance(it, tuple) else (it, it))
    return out


def singles(a, b):
    return [(n, n) for n in range(a, b + 1)]


# ch07 第六章 珠光宝气 — dividers at source lines 3, 59, 202.
CH07 = (spans((4, 6), (7, 10), (11, 13))
        + singles(14, 58)           # scene 1 rest
        + singles(60, 201)          # scene 2
        + singles(203, 238))        # scene 3
CH07_BREAKS = [48, 190]

# ch08 第七章 市井七侠 — dividers at source lines 3, 98, 218.
CH08 = (
    # scene 1: lines 4-97
    singles(4, 49) + [(50, 51)] + singles(52, 58) + [(59, 60)]
    + singles(61, 82) + [(83, 84)] + singles(85, 87) + [(88, 89)]
    + [(90, 91)] + singles(92, 97)
    # scene 2: lines 99-217
    + singles(99, 104) + [(105, 107)] + singles(108, 111) + [(112, 113)]
    + [(114, 115)] + singles(116, 116) + [(117, 118)] + singles(119, 132)
    + [(133, 134)] + [(135, 137)] + singles(138, 189) + [(190, 191)]
    + [(192, 194)] + singles(195, 217)
    # scene 3: lines 219-369
    + [(219, 220)] + singles(221, 243) + [(244, 245)] + singles(246, 369)
)
CH08_BREAKS = [89, 197]


if __name__ == "__main__":
    which = sys.argv[1:] or ["ch07", "ch08"]
    if "ch07" in which:
        build("ch07",
              os.path.join(ROOT, "data/src/12_part0000-split-010.txt"),
              "Chapter 6. Pearls and Splendour", "第六章  珠光宝气",
              CH07, CH07_BREAKS)
    if "ch08" in which and CH08 is not None:
        build("ch08",
              os.path.join(ROOT, "data/src/13_part0000-split-011.txt"),
              "Chapter 7. The Seven Heroes of the Marketplace",
              "第七章  市井七侠", CH08, CH08_BREAKS)
    print("B05 build step complete")
