#!/usr/bin/env python3
"""Execute the R04 register-pass edit lists (ch16-ch19).

Parses edits/<id>_edits.md for TOUCH/RECAST prose edits and NOTE-ADD blocks,
applies the prose edits to out/<id>_bilingual.md with exact-match count==1,
regenerates the reading text, verifies every new note anchor is a verbatim
substring of the post-edit reading text, then appends the notes to notes.json.
No NOTE-ANCHOR items in this batch (no edit touches an existing note anchor).
"""
import json, re, subprocess, sys

IDS = ["ch16", "ch17", "ch18", "ch19"]
ZH_TITLE = {u["id"]: u["title"] for u in json.load(open("book.json"))["structure"]}


def parse_edits(cid):
    """Return (prose_edits, notes) parsed from edits/<cid>_edits.md."""
    lines = open(f"edits/{cid}_edits.md", encoding="utf-8").read().split("\n")
    prose, notes = [], []
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
                elif lines[j].startswith("WHY:"):
                    break
            assert old is not None and new is not None, f"{cid}: bad edit block at line {i+1}"
            prose.append((old, new))
        elif ln.startswith("NOTE-ADD "):
            anchor = note = None
            for j in range(i + 1, min(i + 5, len(lines))):
                if lines[j].startswith("ANCHOR: "):
                    anchor = lines[j][8:]
                elif lines[j].startswith("NOTE: "):
                    note = lines[j][6:]
                elif lines[j].startswith("WHY:"):
                    break
            assert anchor and note, f"{cid}: bad NOTE-ADD at line {i+1}"
            notes.append((anchor, note))
        i += 1
    return prose, notes


def main():
    all_notes = {}
    # 1. Apply prose edits to the bilingual files.
    for cid in IDS:
        prose, notes = parse_edits(cid)
        all_notes[cid] = notes
        path = f"out/{cid}_bilingual.md"
        text = open(path, encoding="utf-8").read()
        for old, new in prose:
            n = text.count(old)
            if n != 1:
                sys.exit(f"ABORT {cid}: OLD occurs {n} times (need 1):\n  {old!r}")
            text = text.replace(old, new)
        open(path, "w", encoding="utf-8").write(text)
        print(f"{cid}: applied {len(prose)} prose edits, {len(notes)} notes queued")

    # 2. Regenerate reading text for edited chapters.
    for cid in IDS:
        subprocess.run(
            ["python3", "scripts/split_bilingual.py", f"out/{cid}_bilingual.md", cid, ZH_TITLE[cid]],
            check=True, capture_output=True,
        )

    # 3. Verify every new anchor is a verbatim substring of the post-edit reading text.
    for cid in IDS:
        reading = open(f"out/{cid}_reading.md", encoding="utf-8").read()
        for anchor, _ in all_notes[cid]:
            c = reading.count(anchor)
            if c != 1:
                sys.exit(f"ABORT {cid}: anchor occurs {c}x in reading text (need 1):\n  {anchor!r}")
    print("all new anchors verified as unique verbatim substrings")

    # 4. Append notes to notes.json, in file order (paragraph order).
    notes_json = json.load(open("notes.json", encoding="utf-8"))
    added = 0
    for cid in IDS:
        lst = notes_json.setdefault(cid, [])
        existing = {n["anchor"] for n in lst}
        for anchor, note in all_notes[cid]:
            if anchor in existing:
                sys.exit(f"ABORT {cid}: anchor already present: {anchor!r}")
            lst.append({"anchor": anchor, "note": note})
            added += 1
    json.dump(notes_json, open("notes.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    total = sum(len(v) for v in notes_json.values())
    print(f"appended {added} notes; book-wide total now {total}")


if __name__ == "__main__":
    main()
