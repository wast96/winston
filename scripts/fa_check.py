#!/usr/bin/env python3
"""First-appearance helper for the footnote pass.
Usage: fa_check.py "search term" ["term2" ...]
For each term: lists (in chapter order) which out/ch*_reading.md files contain it,
and lists any notes.json anchors (any chapter) that contain the term (case-insensitive).
"""
import sys, json, glob, os, re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files=sorted(glob.glob(os.path.join(ROOT,'out','ch*_reading.md')))
files=[f for f in files if '.pre-R' not in f]
notes=json.load(open(os.path.join(ROOT,'notes.json')))
def chap(f): return os.path.basename(f).split('_')[0]
for term in sys.argv[1:]:
    t=term.lower()
    print('==== %r ====' % term)
    hits=[]
    for f in files:
        txt=open(f).read().lower()
        if t in txt:
            hits.append(chap(f))
    print('  reading files:', ' '.join(hits) if hits else '(none)')
    # notes
    noted=[]
    for ch,lst in notes.items():
        for n in lst:
            if t in n['anchor'].lower() or t in n['note'].lower():
                noted.append('%s:%s' % (ch, n['anchor'][:40]))
    if noted:
        for x in noted:
            print('  NOTED', x)
    else:
        print('  NOTED (none)')
