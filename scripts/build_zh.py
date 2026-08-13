#!/usr/bin/env python3
"""Build data/zh/<id>.txt from data/src/<srcbase>.txt, mechanically:
title line '### <title>' then one body line per non-empty source paragraph,
skipping the first two header lines. File-to-file copy; no authoring."""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def main(cid, srcbase, title):
    src = os.path.join(ROOT, 'data/src', srcbase + '.txt')
    lines = open(src, encoding='utf-8').read().split('\n')
    body = [l for l in lines[2:] if l.strip()]
    dest = os.path.join(ROOT, 'data/zh', cid + '.txt')
    with open(dest, 'w', encoding='utf-8') as fh:
        fh.write('### ' + title + '\n')
        for l in body:
            fh.write(l + '\n')
    print('wrote %s (%d body lines)' % (dest, len(body)))
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
