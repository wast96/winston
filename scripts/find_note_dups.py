#!/usr/bin/env python3
"""Find cross-unit duplicate SUBJECTS among new notes (and vs existing notes).

Each entity's Chinese characters are its most reliable identity key. This
extracts every distinct hanzi run (>=2 chars) that appears in a note body and
reports when the SAME hanzi run is used to identify a subject in more than one
unit -- across the incoming batch files and the live notes.json. Those are the
candidates to dedup down to the earliest unit in reading order.

Reading order (earliest first) decides which unit keeps the note.

Usage: find_note_dups.py FILE.json [FILE.json ...]
"""
import json, os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORDER = ['ch00','ch01','ch02','ch02s45','ch03','ch04','ch05','ch06','ch07','ch08','ch09','ch10','ch11']
rank = {u:i for i,u in enumerate(ORDER)}
HAN = re.compile(r'[一-鿿]{2,}')

# hanzi_run -> {unit -> ('NEW'|'EXIST', anchor)}
idx = {}

def add(unit, anchor, body, kind):
    for run in set(HAN.findall(body)):
        idx.setdefault(run, {})
        # keep first-seen per unit
        if unit not in idx[run]:
            idx[run][unit] = (kind, anchor)

# existing notes
live = json.load(open(os.path.join(ROOT,'notes.json'), encoding='utf-8'))
for u, arr in live.items():
    for n in arr:
        add(u, n['anchor'], n['note'], 'EXIST')

# incoming
newkeys = {}  # run -> set(units it's NEW in)
for fn in sys.argv[1:]:
    data = json.load(open(fn, encoding='utf-8'))
    notes = data.get('notes', data)
    for u, arr in notes.items():
        for n in arr:
            add(u, n['anchor'], n['note'], 'NEW')
            for run in set(HAN.findall(n['note'])):
                newkeys.setdefault(run, set()).add(u)

# Report runs that are NEW in >=1 unit AND appear in >=2 units total
print("=== CROSS-UNIT DUPLICATE SUBJECT CANDIDATES (by shared hanzi) ===")
print("(only showing where a NEW note overlaps another unit; earliest unit should keep it)\n")
hits = 0
for run, units in sorted(idx.items(), key=lambda kv: -len(kv[1])):
    if run not in newkeys:
        continue
    if len(units) < 2:
        continue
    # skip very common generic runs
    ordered = sorted(units.items(), key=lambda kv: rank.get(kv[0], 99))
    kinds = [k for k,_ in units.values()]
    print(f"{run} :")
    for u,(kind,anchor) in ordered:
        keep = " <== KEEP (earliest)" if u==ordered[0][0] and 'NEW' in [units[u][0]] else ""
        flag = " [drop if NEW]" if u!=ordered[0][0] else ""
        print(f"    {u:8} {kind:5} «{anchor}»{keep}{flag}")
    hits += 1
print(f"\n{hits} shared-hanzi groups spanning >=2 units")
