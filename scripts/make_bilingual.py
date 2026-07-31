#!/usr/bin/env python3
"""Assemble a bilingual QC file from a VERBATIM source .txt and an English
paragraph file, so the source blockquote lines are copied, never re-typed.

Source: a data/src file (2 metadata lines, then one source paragraph per line).
English: one English paragraph per line, in the same order and count.
Emits out/<id>_bilingual.md: '## H2 <title>' then '> <src>' / '<en>' pairs.

Usage: make_bilingual.py <src_txt> <en_txt> <id> "## H2 <english chapter title>"
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main(src_txt, en_txt, unit_id, header):
    src = [l.rstrip("\n") for l in open(src_txt)][2:]
    src = [l for l in src if l.strip()]
    en = [l.rstrip("\n") for l in open(en_txt)]
    en = [l for l in en if l.strip()]
    if len(src) != len(en):
        sys.exit("MISMATCH: %d source paragraphs vs %d English paragraphs"
                 % (len(src), len(en)))
    out = [header, ""]
    for s, e in zip(src, en):
        out.append("> " + s)
        out.append(e)
        out.append("")
    path = os.path.join(ROOT, "out", "%s_bilingual.md" % unit_id)
    with open(path, "w") as fh:
        fh.write("\n".join(out).rstrip() + "\n")
    print("wrote %s: %d pairs" % (path, len(src)))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
