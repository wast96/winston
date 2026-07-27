#!/usr/bin/env python3
"""Pair source paragraphs with their translations for QC.

The bilingual file is a WORKING artifact and is never shipped: it exists so
the numeric-invariant check has a source paragraph and its translation side
by side, and so a human can spot-audit a paragraph without holding two files
open. Deliverables are the reading markdown and the EPUB.

Pairing is positional, which is only sound because check_structure.py has
already proved the paragraph counts match. Run parity FIRST; if it fails,
every pair after the mismatch is garbage and the numeric check will report
nonsense with great confidence.

Usage: make_bilingual.py UNIT_ID
Reads:  data/zh/UNIT.txt, out/UNIT_reading.md
Writes: out/UNIT_bilingual.md
"""
import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def paras(path, head_prefix):
    out = []
    for l in open(path):
        s = l.strip()
        if not s or s.startswith(head_prefix):
            continue
        out.append(s)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("unit")
    a = ap.parse_args()

    src_path = os.path.join(ROOT, "data", "zh", "%s.txt" % a.unit)
    tgt_path = os.path.join(ROOT, "out", "%s_reading.md" % a.unit)
    src = paras(src_path, "###")
    tgt = paras(tgt_path, "#")

    if len(src) != len(tgt):
        print("PARITY MISMATCH source %d translation %d - run check_structure "
              "--pairs first; positional pairing below would be meaningless"
              % (len(src), len(tgt)), file=sys.stderr)
        return 1

    dest = os.path.join(ROOT, "out", "%s_bilingual.md" % a.unit)
    with open(dest, "w") as fh:
        fh.write("<!-- QC artifact, not for distribution: %s -->\n\n" % a.unit)
        for i, (s, t) in enumerate(zip(src, tgt), 1):
            fh.write("**%d.**\n\n> %s\n\n%s\n\n---\n\n" % (i, s, t))
    print("%s: %d pairs -> %s" % (a.unit, len(src), dest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
