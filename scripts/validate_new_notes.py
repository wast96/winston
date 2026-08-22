#!/usr/bin/env python3
"""Validate a batch of NEW notes before merging them into notes.json.

Checks, per note, that would otherwise break the build or ship a defect:
  - anchor is a verbatim substring of out/<unit>_reading.md
  - anchor is unique enough (report if it occurs more than once: it will
    attach to the FIRST occurrence, which is usually what we want, but flag it)
  - note body uses numeric character references only (no named entities)
  - no U+FFFD replacement characters
  - anchor not already present in the live notes.json for that unit
  - no duplicate anchors within the incoming batch for a unit

Usage: validate_new_notes.py FILE.json [FILE.json ...]
Exit 1 if any HARD problem (missing anchor, named entity, FFFD, dup-in-batch).
Unique-occurrence and already-present are reported as INFO/SKIP, not failures.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAMED = re.compile(r"&(?!#\d+;|#x[0-9a-fA-F]+;|amp;|lt;|gt;)[a-zA-Z]+;")

live = {}
p = os.path.join(ROOT, "notes.json")
if os.path.exists(p):
    live = json.load(open(p, encoding="utf-8"))

reading_cache = {}
def reading(unit):
    if unit not in reading_cache:
        rp = os.path.join(ROOT, "out", f"{unit}_reading.md")
        reading_cache[unit] = open(rp, encoding="utf-8").read() if os.path.exists(rp) else None
    return reading_cache[unit]

hard = 0
info = 0
total_ok = 0
for fn in sys.argv[1:]:
    try:
        data = json.load(open(fn, encoding="utf-8"))
    except Exception as e:
        print(f"[FILE ERROR] {fn}: {e}")
        hard += 1
        continue
    notes = data.get("notes", data)  # accept bare {unit:[...]} too
    for unit, arr in notes.items():
        text = reading(unit)
        if text is None:
            print(f"[HARD] {fn} unit {unit}: no reading file out/{unit}_reading.md")
            hard += 1
            continue
        existing_anchors = {n["anchor"] for n in live.get(unit, [])}
        seen = set()
        for i, n in enumerate(arr):
            a = n.get("anchor", "")
            body = n.get("note", "")
            tag = f"{fn}:{unit}[{i}] {a!r}"
            if not a:
                print(f"[HARD] {tag}: empty anchor"); hard += 1; continue
            if a not in text:
                print(f"[HARD] {tag}: anchor NOT a verbatim substring"); hard += 1; continue
            occ = text.count(a)
            if "�" in body or "�" in a:
                print(f"[HARD] {tag}: U+FFFD replacement char"); hard += 1; continue
            m = NAMED.search(body)
            if m:
                print(f"[HARD] {tag}: named entity {m.group(0)!r}"); hard += 1; continue
            if a in seen:
                print(f"[HARD] {tag}: duplicate anchor within batch"); hard += 1; continue
            seen.add(a)
            if a in existing_anchors:
                print(f"[SKIP] {tag}: anchor already in notes.json (merge will skip)"); info += 1; continue
            if occ > 1:
                print(f"[INFO] {tag}: anchor occurs {occ}x (attaches to first)"); info += 1
            total_ok += 1
    print(f"--- {fn}: file parsed ---")

print(f"\nSUMMARY: {total_ok} mergeable notes OK, {info} info/skip, {hard} HARD problems")
sys.exit(1 if hard else 0)
