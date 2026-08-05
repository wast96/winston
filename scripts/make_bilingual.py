#!/usr/bin/env python3
"""Assemble out/<id>_bilingual.md from the VERBATIM source lines and a JSON list
of English paragraphs, so the source can never be mistyped.

The source text file (data/src/*.txt) holds, one per line: a junk author line
('未知'), the chapter title, then one source paragraph per line. This reads the
body lines straight from that file, zips them with the English paragraphs given
in a JSON file, and writes the bilingual QC file:

    ## H2 <title_en>
    > <source paragraph>
    <english paragraph>
    ...

Usage: make_bilingual.py <unit_id> <src_txt> <title_en> <english.json> [title_lines]
  title_lines: how many leading lines are title/junk to skip (default 2:
  the '未知' line and the one title line). Pass 3 when the title spans two lines.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main(unit_id, src_txt, title_en, en_json, skip=2):
    src_lines = [l.rstrip("\n") for l in open(src_txt, encoding="utf-8")]
    body = [l for l in src_lines[skip:] if l.strip()]
    english = json.load(open(en_json, encoding="utf-8"))
    if len(body) != len(english):
        sys.exit("MISMATCH %s: %d source paragraphs vs %d english"
                 % (unit_id, len(body), len(english)))
    out = ["## H2 " + title_en]
    for zh, en in zip(body, english):
        out.append("> " + zh)
        out.append(en)
    dest = os.path.join(ROOT, "out", "%s_bilingual.md" % unit_id)
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    print("wrote %s (%d paragraph pairs)" % (dest, len(body)))


if __name__ == "__main__":
    skip = int(sys.argv[5]) if len(sys.argv) > 5 else 2
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], skip)
