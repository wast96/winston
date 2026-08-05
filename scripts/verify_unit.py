#!/usr/bin/env python3
"""Post-edit verification for one unit: parity, numbers, anchors.

Reconstructs a bilingual QC pairing from the 1:1 line alignment between
data/zh/<id>.txt and out/<id>_reading.md (scene-break markers skipped, set-off
prefixes stripped), writes it to a temp file, and runs the number invariant
over every pair; then verifies paragraph parity and that every notes.json
anchor for the unit still resolves verbatim.

Usage: verify_unit.py ch01 [ch02 ...]      (exit 1 on any failure)
"""
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def body(path):
    out = []
    for l in open(path):
        s = l.strip()
        if not s or s == '***' or s.startswith('#'):
            continue
        out.append(re.sub(r'^\{[vdgp]\} ', '', s))
    return out


def main(cids):
    notes = json.load(open(os.path.join(ROOT, 'notes.json')))
    ok = True
    for cid in cids:
        zh = body(os.path.join(ROOT, 'data', 'zh', cid + '.txt'))
        en = body(os.path.join(ROOT, 'out', cid + '_reading.md'))
        if len(zh) != len(en):
            print('%s PARITY FAIL: zh %d vs en %d' % (cid, len(zh), len(en)))
            ok = False
            continue
        tmp = tempfile.NamedTemporaryFile('w', suffix='.md', delete=False)
        for z, e in zip(zh, en):
            tmp.write('> %s\n\n%s\n\n' % (z, e))
        tmp.close()
        r = subprocess.run([sys.executable,
                            os.path.join(ROOT, 'scripts', 'check_numbers.py'),
                            tmp.name, '--noise', os.path.join(ROOT, 'noise.txt')],
                           capture_output=True, text=True)
        tail = r.stdout.strip().splitlines()
        if r.returncode:
            print('%s NUMBERS FAIL:' % cid)
            print(r.stdout)
            ok = False
        else:
            print('%s numbers: %s' % (cid, tail[-1] if tail else '?'))
        os.unlink(tmp.name)
        text = open(os.path.join(ROOT, 'out', cid + '_reading.md')).read()
        bad = [e['anchor'] for e in notes.get(cid, []) if e['anchor'] not in text]
        if bad:
            ok = False
            print('%s ANCHOR FAIL:' % cid)
            for a in bad:
                print('   ', a[:80])
        else:
            print('%s anchors: %d ok' % (cid, len(notes.get(cid, []))))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
