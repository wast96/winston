#!/usr/bin/env python3
"""Derive the clean reading edition and the parity source from one bilingual
QC file, so the two can never drift apart.

The bilingual file (out/<id>_bilingual.md, QC ONLY, never shipped) holds, in
order: heading lines tagged '## H2/H3/H4 <text>', then paragraph pairs of a
'> <source>' line followed by one English line. This script emits:

  out/<id>_reading.md   English only: '## '/'### '/'#### ' headings + prose.
  data/zh/<id>.txt      '### <chapter zh title>' then one source line per
                        paragraph, for check_structure.py parity.

Usage: split_bilingual.py out/ch01_bilingual.md ch01 "第一章 緒論"
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEVEL = {"H2": "## ", "H3": "### ", "H4": "#### "}


def main(bilingual, unit_id, zh_title):
    reading, zh = [], ["### " + zh_title]
    src = None
    for raw in open(bilingual):
        line = raw.rstrip("\n")
        s = line.strip()
        if not s:
            continue
        if s.startswith("## H"):
            tag, _, text = s[3:].partition(" ")
            reading.append(LEVEL[tag] + text)
            continue
        if s.startswith("#"):            # a plain comment line
            continue
        if s.startswith(">"):
            src = s.lstrip("> ").strip()
            continue
        # an English paragraph line: pairs with the pending source line
        reading.append(s)
        if src is not None:
            zh.append(src)
            src = None

    out_reading = os.path.join(ROOT, "out", "%s_reading.md" % unit_id)
    with open(out_reading, "w") as fh:
        fh.write("\n\n".join(reading) + "\n")
    zh_dir = os.path.join(ROOT, "data", "zh")
    os.makedirs(zh_dir, exist_ok=True)
    with open(os.path.join(zh_dir, "%s.txt" % unit_id), "w") as fh:
        fh.write("\n".join(zh) + "\n")
    n_para = len(zh) - 1
    print("wrote %s (%d headings+paras) and data/zh/%s.txt (%d paras)"
          % (out_reading, len(reading), unit_id, n_para))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
