#!/usr/bin/env python3
"""Derive out/<id>_en.json (the flat, one-paragraph-per-source-line English
array that make_bilingual.py pairs with the source) from the authored display
file out/<id>_reading.md, so the two can never drift.

The reading file holds a '## <title>' heading, blank-separated English display
paragraphs, '***' scene-break lines, and '{j} ' display-join prefixes. This
strips the heading, drops the '***' lines, removes the '{j} ' prefix (the join
is display-only), and writes the remaining paragraphs, in order, as a JSON list.
The count must equal the source body-paragraph count; make_bilingual.py enforces
that when it pairs the result against data/src.

Usage: reading_to_en.py ch02
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main(cid):
    path = os.path.join(ROOT, 'out', cid + '_reading.md')
    para = []
    for l in open(path, encoding='utf-8'):
        s = l.strip()
        if not s or s == '***' or s.startswith('#'):
            continue
        para.append(re.sub(r'^\{[vdgpj]\} ', '', s))
    dest = os.path.join(ROOT, 'out', cid + '_en.json')
    with open(dest, 'w', encoding='utf-8') as fh:
        json.dump(para, fh, ensure_ascii=False, indent=0)
        fh.write('\n')
    print('wrote %s (%d paragraphs)' % (dest, len(para)))


if __name__ == '__main__':
    main(sys.argv[1])
