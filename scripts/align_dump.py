#!/usr/bin/env python3
"""QC-only: dump aligned zh|en pairs for a unit using the SAME body() logic as
verify_unit.py (strip '#' lines, '***', set-off {vdgp} prefixes), so the pairing
matches the fidelity gate exactly. For the reviewer's aligned read during the
register pass; never ships. Usage: align_dump.py ch09 [start end]"""
import os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def body(path):
    out = []
    for l in open(path, encoding="utf-8"):
        s = l.strip()
        if not s or s == '***' or s.startswith('#'):
            continue
        out.append(re.sub(r'^\{[vdgp]\} ', '', s))
    return out

cid = sys.argv[1]
a = int(sys.argv[2]) if len(sys.argv) > 2 else 0
b = int(sys.argv[3]) if len(sys.argv) > 3 else 10**9
zh = body(os.path.join(ROOT, 'data', 'zh', cid + '.txt'))
en = body(os.path.join(ROOT, 'out', cid + '_reading.md'))
assert len(zh) == len(en), "parity %d vs %d" % (len(zh), len(en))
for i in range(a, min(b, len(zh))):
    print("### p%03d" % (i + 1))
    print("ZH:", zh[i])
    print("EN:", en[i])
    print()
