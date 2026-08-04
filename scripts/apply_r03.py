#!/usr/bin/env python3
"""R03 executor: parse edits/ch{12..15}_edits.md, apply prose TOUCH/RECAST edits
to the bilingual files (exact-match, count==1), regenerate reading text, then
append verified NOTE-ADD notes to notes.json. Style pass; source lines untouched.
"""
import json, subprocess, sys, os

CHAPTERS = ["ch12", "ch13", "ch14", "ch15"]
book = json.load(open("book.json", encoding="utf-8"))
zh_title = {u["id"]: u["title"] for u in book["structure"]}


def parse_edits(path):
    edits, notes = [], []
    lines = open(path, encoding="utf-8").read().split("\n")
    i = 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("### ") and ("TOUCH" in ln or "RECAST" in ln):
            old = new = None
            for j in range(i + 1, min(i + 6, len(lines))):
                if lines[j].startswith("OLD: "):
                    old = lines[j][5:]
                elif lines[j].startswith("NEW: "):
                    new = lines[j][5:]
            assert old is not None and new is not None, f"bad TOUCH at {path}:{i+1}"
            edits.append((old, new))
        elif ln.startswith("NOTE-ADD"):
            anchor = note = None
            for j in range(i + 1, min(i + 5, len(lines))):
                if lines[j].startswith("ANCHOR: "):
                    anchor = lines[j][8:]
                elif lines[j].startswith("NOTE: "):
                    note = lines[j][6:]
            assert anchor and note, f"bad NOTE-ADD at {path}:{i+1}"
            notes.append({"anchor": anchor, "note": note})
        i += 1
    return edits, notes


# Phase 1: apply prose edits to bilingual files
parsed = {}
for cid in CHAPTERS:
    edits, notes = parse_edits(f"edits/{cid}_edits.md")
    parsed[cid] = notes
    bpath = f"out/{cid}_bilingual.md"
    content = open(bpath, encoding="utf-8").read()
    for old, new in edits:
        n = content.count(old)
        assert n == 1, f"{cid}: OLD occurs {n}x (need 1): {old!r}"
        content = content.replace(old, new)
    if edits:
        open(bpath, "w", encoding="utf-8").write(content)
    print(f"{cid}: applied {len(edits)} prose edit(s), {len(notes)} note(s) parsed")

# Phase 2: regenerate reading + data/zh from the (possibly edited) bilingual files
for cid in CHAPTERS:
    subprocess.run([sys.executable, "scripts/split_bilingual.py",
                    f"out/{cid}_bilingual.md", cid, zh_title[cid]],
                   check=True, capture_output=True)
print("regenerated reading files")

# Phase 3: verify each new anchor is a verbatim substring of the reading text,
# then append to notes.json (append order does not affect builder numbering,
# which follows reading-order position).
notes_json = json.load(open("notes.json", encoding="utf-8"))
for cid in CHAPTERS:
    rd = open(f"out/{cid}_reading.md", encoding="utf-8").read()
    existing = {n["anchor"] for n in notes_json[cid]}
    for nt in parsed[cid]:
        c = rd.count(nt["anchor"])
        assert c >= 1, f"{cid}: anchor NOT found in reading: {nt['anchor']!r}"
        assert nt["anchor"] not in existing, f"{cid}: duplicate anchor {nt['anchor']!r}"
        notes_json[cid].append(nt)
        existing.add(nt["anchor"])
    print(f"{cid}: notes now {len(notes_json[cid])}")

json.dump(notes_json, open("notes.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
total = sum(len(v) for v in notes_json.values())
print(f"notes.json written; book-wide total notes = {total}")
