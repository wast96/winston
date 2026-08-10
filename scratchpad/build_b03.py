#!/usr/bin/env python3
"""B03 builder: merged-paragraph pipeline for ch03 and ch04.

For each unit: build a MERGED source file (the two title lines verbatim, then
one line per merged paragraph, each the VERBATIM concatenation of its source
body lines, divider lines '01/02/...' excluded); run make_bilingual (parity by
construction) and split_bilingual; then post-insert '***' scene breaks into the
reading.md at the paragraph boundaries that correspond to the source's
bare-numeric dividers.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "scripts")


def merged_source(src_txt, ranges, dest):
    lines = [l.rstrip("\n") for l in open(src_txt, encoding="utf-8")]
    out = [lines[0], lines[1]]                    # the two title/stub lines
    for a, b in ranges:
        out.append("".join(lines[a - 1:b]))       # 1-indexed, verbatim join
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    return len(out) - 2


def run(*args):
    r = subprocess.run([sys.executable] + list(args), capture_output=True,
                       text=True)
    sys.stdout.write(r.stdout)
    if r.returncode:
        sys.stdout.write(r.stderr)
        sys.exit("FAILED: %s" % " ".join(args))


def insert_breaks(reading_path, after_paras):
    blocks = open(reading_path, encoding="utf-8").read().split("\n\n")
    # blocks[0] is the H2 title; paragraph N is blocks[N].
    for k in sorted(after_paras, reverse=True):
        blocks.insert(k + 1, "***")
    with open(reading_path, "w", encoding="utf-8") as fh:
        fh.write("\n\n".join(blocks) + ("\n" if not blocks[-1].endswith("\n")
                                        else ""))


def build(uid, src_txt, title_en, zh_title, ranges, breaks):
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


CH03 = ([(4, 5), (6, 7)]
        + [(n, n) for n in range(8, 147)]
        + [(n, n) for n in range(148, 200)]
        + [(n, n) for n in range(201, 331)])

CH04 = ([(4, 5), (6, 8), (9, 9), (10, 10), (11, 11)]
        + [(n, n) for n in range(12, 174)]
        + [(n, n) for n in range(175, 255)]
        + [(256, 257), (258, 258), (259, 260)]
        + [(n, n) for n in range(261, 308)]
        + [(n, n) for n in range(309, 345)])

if __name__ == "__main__":
    build("ch03", os.path.join(ROOT, "data/src/08_part0000-split-006.txt"),
          "Chapter 2. Princess Danfeng", "第二章  丹凤公主", CH03, [141, 193])
    build("ch04", os.path.join(ROOT, "data/src/09_part0000-split-007.txt"),
          "Chapter 3. The Great King of the Golden Roc", "第三章  大金鹏王",
          CH04, [167, 247, 297])
    print("B03 build complete")
