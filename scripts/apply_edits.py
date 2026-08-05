#!/usr/bin/env python3
"""Apply a committed edit list to a unit's prose, mechanically and safely.

This is the EXECUTE half of a revision/register pass (see REVISION_PLAN
.template.md). The ANALYZE half reads a chapter against its source and writes
`edits/<id>_edits.md`; this script applies it. Splitting the roles keeps the
pass reviewable, resumable across sessions, and mechanically safe: every
change is in git before it touches the prose.

Edit-file grammar (one block per edit):

    ### p<NNN> [T1..T6] TOUCH|RECAST
    OLD: <exact current text; must occur EXACTLY ONCE in the file>
    NEW: <replacement, final typography>
    WHY: <source phrase + what was wrong>

    NOTE-ANCHOR
    OLD: <anchor as it appears in notes.json>
    NEW: <anchor after the prose edit>

    NOTE-ADD
    ANCHOR: <verbatim substring of the post-edit prose>
    NOTE: <XHTML body, numeric character references only>
    WHY: <what a non-specialist reader would miss>

Safety properties (each one a lesson):
  - OLD must occur exactly once; anything else aborts before writing. A
    replace on a 2x match silently edits the wrong occurrence.
  - NOTE-ANCHOR pairs run in the same pass as the prose edit that breaks
    them; the builder's refusal on an unmatched anchor is the backstop,
    not the check.
  - New anchors are verified as verbatim substrings of the POST-edit prose.
  - notes.json is written via json.dump(ensure_ascii=False), never by hand
    or heredoc (the CJK-mangling trap).
  - If an edit cannot be applied cleanly, the script aborts and names it;
    it never improvises a third wording.

Usage:
    apply_edits.py ch01 ch02 ...          # applies edits/chNN_edits.md to
                                          # out/chNN_reading.md
    apply_edits.py --bilingual ch01 ...   # applies to out/chNN_bilingual.md,
                                          # then regenerates the reading file
                                          # with split_bilingual.py
"""
import argparse
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def parse_edits(path):
    edits, anchor_moves, notes = [], [], []
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
            if old is None or new is None:
                sys.exit("bad TOUCH/RECAST block at %s:%d" % (path, i + 1))
            edits.append((old, new, ln.strip()))
        elif ln.strip() == "NOTE-ANCHOR":
            old = new = None
            for j in range(i + 1, min(i + 4, len(lines))):
                if lines[j].startswith("OLD: "):
                    old = lines[j][5:]
                elif lines[j].startswith("NEW: "):
                    new = lines[j][5:]
            if old is None or new is None:
                sys.exit("bad NOTE-ANCHOR block at %s:%d" % (path, i + 1))
            anchor_moves.append((old, new))
        elif ln.startswith("NOTE-ADD"):
            anchor = note = None
            for j in range(i + 1, min(i + 5, len(lines))):
                if lines[j].startswith("ANCHOR: "):
                    anchor = lines[j][8:]
                elif lines[j].startswith("NOTE: "):
                    note = lines[j][6:]
            if not anchor or not note:
                sys.exit("bad NOTE-ADD block at %s:%d" % (path, i + 1))
            notes.append({"anchor": anchor, "note": note})
        i += 1
    return edits, anchor_moves, notes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("units", nargs="+")
    ap.add_argument("--bilingual", action="store_true",
                    help="edit the bilingual file and regenerate the reading "
                         "file (for projects that track bilinguals)")
    a = ap.parse_args()

    book = json.load(open(os.path.join(ROOT, "book.json"), encoding="utf-8"))
    zh_title = {u["id"]: u.get("title", "") for u in book.get("structure", [])}
    notes_path = os.path.join(ROOT, "notes.json")
    notes_json = json.load(open(notes_path, encoding="utf-8"))

    for cid in a.units:
        epath = os.path.join(ROOT, "edits", "%s_edits.md" % cid)
        edits, anchor_moves, new_notes = parse_edits(epath)
        target = os.path.join(ROOT, "out", "%s_%s.md"
                              % (cid, "bilingual" if a.bilingual else "reading"))
        content = open(target, encoding="utf-8").read()
        for old, new, label in edits:
            n = content.count(old)
            if n != 1:
                sys.exit("%s: OLD occurs %dx (need exactly 1) at %s\n  %r"
                         % (cid, n, label, old))
            if a.bilingual and old in "".join(
                    l for l in content.splitlines() if l.startswith(">")):
                sys.exit("%s: edit would touch a source '>' line: %r"
                         % (cid, old))
            content = content.replace(old, new)
        if edits:
            open(target, "w", encoding="utf-8").write(content)
        if a.bilingual and edits:
            subprocess.run([sys.executable,
                            os.path.join(ROOT, "scripts", "split_bilingual.py"),
                            target, cid, zh_title.get(cid, "")], check=True)

        unit_notes = notes_json.setdefault(cid, [])
        for old, new in anchor_moves:
            hits = [n for n in unit_notes if n["anchor"] == old]
            if len(hits) != 1:
                sys.exit("%s: NOTE-ANCHOR OLD matches %d notes: %r"
                         % (cid, len(hits), old))
            hits[0]["anchor"] = new

        reading = open(os.path.join(ROOT, "out", "%s_reading.md" % cid),
                       encoding="utf-8").read()
        existing = {n["anchor"] for n in unit_notes}
        for nt in new_notes:
            if nt["anchor"] not in reading:
                sys.exit("%s: new anchor NOT a verbatim substring of the "
                         "post-edit reading text: %r" % (cid, nt["anchor"]))
            if re.search(r"&(?!#\d+;)[a-zA-Z]+;", nt["note"]):
                sys.exit("%s: note body uses a NAMED entity (breaks the XHTML "
                         "build); use numeric character references: %r"
                         % (cid, nt["note"][:60]))
            if nt["anchor"] in existing:
                sys.exit("%s: duplicate anchor %r" % (cid, nt["anchor"]))
            unit_notes.append(nt)
            existing.add(nt["anchor"])
        for old, new in anchor_moves:
            if new not in reading:
                sys.exit("%s: moved anchor NOT in post-edit reading: %r"
                         % (cid, new))
        print("%s: %d edit(s), %d anchor move(s), %d note(s) added; notes now %d"
              % (cid, len(edits), len(anchor_moves), len(new_notes),
                 len(unit_notes)))

    with open(notes_path, "w", encoding="utf-8") as fh:
        json.dump(notes_json, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("notes.json written; book-wide total = %d"
          % sum(len(v) for k, v in notes_json.items()
                if not k.startswith("_")))


if __name__ == "__main__":
    main()
