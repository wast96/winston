#!/usr/bin/env python3
"""Batch helper: pair verbatim source paragraphs with an authored English file
to emit the bilingual QC file, so the source side is copied (never re-typed).

Reads data/src/<srcfile>.txt: strips the UTF-8 BOM, drops blank lines and the
two duplicated chapter-numeral heading lines at the top, leaving one paragraph
per line. Reads the English file (one paragraph per non-blank line, in order).
The two must have equal counts. Writes out/<id>_bilingual.md as
'## H2 Chapter N' then, per pair, a '> <source>' line and one English line.

Usage: _zip_bilingual.py <id> <srcfile> <zh_head> <chapter_en> <english.txt>
  e.g. _zip_bilingual.py ch15 19_chapter17 十五 "Chapter 15" scratch/ch15_en.txt
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def src_paragraphs(srcfile, zh_head):
    path = os.path.join(ROOT, "data", "src", srcfile + ".txt")
    lines = [l.rstrip("\n").lstrip("﻿") for l in open(path, encoding="utf-8")]
    paras = [l.strip() for l in lines if l.strip()]
    # drop the two duplicated chapter-numeral heading lines at the top
    assert paras[0] == zh_head and paras[1] == zh_head, (paras[0], paras[1])
    return paras[2:]


def main(unit_id, srcfile, zh_head, chapter_en, english_file):
    src = src_paragraphs(srcfile, zh_head)
    eng = [l.rstrip("\n") for l in open(english_file, encoding="utf-8")]
    eng = [l.strip() for l in eng if l.strip()]
    if len(src) != len(eng):
        sys.exit("PARAGRAPH COUNT MISMATCH: source=%d english=%d (%s)"
                 % (len(src), len(eng), unit_id))
    out = os.path.join(ROOT, "out", "%s_bilingual.md" % unit_id)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("## H2 %s\n\n" % chapter_en)
        for s, e in zip(src, eng):
            fh.write("> %s\n\n%s\n\n" % (s, e))
    print("wrote %s (%d pairs)" % (out, len(src)))


if __name__ == "__main__":
    main(*sys.argv[1:6])
