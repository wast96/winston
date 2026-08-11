#!/usr/bin/env python3
"""B04 builder: merged-paragraph pipeline for ch05 and ch06.

Copy of the build_b03.py method (see that file's docstring): merged source
(title lines + one verbatim-concatenated line per paragraph, bare-numeric
divider lines excluded), make_bilingual (parity by construction),
split_bilingual, then post-insert '***' at the scene boundaries.
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


def spans(*items):
    """items: ints (single line) or (a, b) tuples; expands to the RANGES list."""
    out = []
    for it in items:
        if isinstance(it, tuple):
            out.append(it)
        else:
            out.append((it, it))
    return out


def singles(a, b):
    return [(n, n) for n in range(a, b + 1)]


# ch05 第四章 盛宴 — dividers at source lines 3, 100, 255.
CH05 = (
    # scene 1: lines 4-99 -> 77 paragraphs
    [(4, 5)] + singles(6, 9) + [(10, 11)] + singles(12, 17) + [(18, 19)]
    + singles(20, 36) + [(37, 39), (40, 42), (43, 43), (44, 45), (46, 46),
                         (47, 48), (49, 51), (52, 54), (55, 56)]
    + singles(57, 58) + [(59, 60)] + singles(61, 66) + [(67, 68)]
    + singles(69, 72) + [(73, 74), (75, 76)] + singles(77, 93)
    + [(94, 95)] + singles(96, 99)
    # scene 2: lines 101-254 -> 148 paragraphs
    + [(101, 102)] + singles(103, 135) + [(136, 137)] + singles(138, 158)
    + [(159, 160)] + singles(161, 197) + [(198, 200), (201, 202)]
    + singles(203, 254)
    # scene 3: lines 256-347 -> 81 paragraphs
    + singles(256, 265) + [(266, 267)] + singles(268, 271) + [(272, 273)]
    + singles(274, 303) + [(304, 305), (306, 307)] + singles(308, 317)
    + [(318, 322), (323, 323), (324, 325), (326, 327), (328, 328),
       (329, 330)] + singles(331, 347)
)

# ch06 第五章 悲歌 — dividers at source lines 3, 52, 260, 281.
CH06 = (
    # scene 1: lines 4-51
    [(4, 4), (5, 6)] + singles(7, 14) + [(15, 16), (17, 17), (18, 20)]
    + singles(21, 38) + [(39, 40)] + singles(41, 51)
    # scene 2: lines 53-259
    + [(53, 54)] + singles(55, 77) + [(78, 79)] + singles(80, 97)
    + [(98, 99)] + singles(100, 103) + [(104, 104), (105, 106)]
    + singles(107, 109) + [(110, 111)] + singles(112, 116) + [(117, 118)]
    + singles(119, 139) + [(140, 141)] + singles(142, 155) + [(156, 157)]
    + singles(158, 159) + [(160, 161)]
    + singles(162, 169) + [(170, 171), (172, 173)] + singles(174, 180)
    + [(181, 182)] + singles(183, 259)
    # scene 3: lines 261-280
    + [(261, 262)] + singles(263, 280)
    # scene 4: lines 282-297
    + singles(282, 289) + [(290, 291)] + singles(292, 297)
)

if __name__ == "__main__":
    which = sys.argv[1:] or ["ch05", "ch06"]
    if "ch05" in which:
        build("ch05", os.path.join(ROOT, "data/src/10_part0000-split-008.txt"),
              "Chapter 4. The Feast", "第四章  盛 宴", CH05, [77, 225])
    if "ch06" in which:
        build("ch06", os.path.join(ROOT, "data/src/11_part0000-split-009.txt"),
              "Chapter 5. A Song of Sorrow", "第五章  悲 歌", CH06, [43, 238, 257])
    print("B04 build complete")
