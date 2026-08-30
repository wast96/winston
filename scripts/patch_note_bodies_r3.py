#!/usr/bin/env python3
"""R3 note-body patches (apply_edits.py adds/moves notes but never edits an
existing body). Two jobs:

 1. Tier A inside existing bodies in ch20-ch28:
    - day-first dates -> "Month D, YYYY" (or "Month D" bare);
    - the Da Mei Wan Bao regloss (lead with the English masthead, decided form)
      and its date;
    - the Reflection Institute -> reflection institute case fix (generic only;
      the proper "Capital Reflection Institute" stays capitalized).
    Each (unit, anchor-substring, OLD, NEW): OLD must occur exactly once in the
    one note the anchor-substring picks out.

 2. First-appearance relocation: the osmanthus-sugared taro shoots note was at
    ch31 (a recurrence); its FIRST appearance is ch26, where R3 adds the note.
    Remove the now-duplicate ch31 note.

notes.json is rewritten via json.dump(ensure_ascii=False, indent=2).
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES = os.path.join(ROOT, "notes.json")

# (unit, anchor-substring locating the note, OLD, NEW)
PATCHES = [
    # --- Tier A: day-first dates -> Month D, YYYY (or Month D) ---
    ("ch20", "That is Shamian",
     "marchers of 23 June 1925", "marchers of June 23, 1925"),
    ("ch22", "Liao Zhongkai",
     "on 20 August 1925", "on August 20, 1925"),
    ("ch22", "Feng Yuxiang had not yet",
     "on 23 October the warlord", "on October 23 the warlord"),
    ("ch22", "Feng Yuxiang had not yet",
     "on 13 November Sun set out", "on November 13 Sun set out"),
    ("ch24", "the Zhongshan gunboat",
     "of 20 March 1926", "of March 20, 1926"),
    ("ch28", "To resist the foreign",
     "an address of 30 November 1931", "an address of November 30, 1931"),
    # --- Tier A: Da Mei Wan Bao regloss (note anchor already moved to the
    #     English masthead by apply_edits) + its date ---
    ("ch22", "Shanghai Evening Post and Mercury",
     "The <i>Da Mei Wan Bao</i> (大美晚报, the <i>Shanghai Evening Post and Mercury</i>)",
     "The <i>Shanghai Evening Post and Mercury</i> (大美晚报, <i>Da Mei Wan Bao</i>)"),
    ("ch22", "Shanghai Evening Post and Mercury",
     "began on 16 January 1933", "began on January 16, 1933"),
    # --- Tier A: Reflection Institute -> reflection institute (generic only) ---
    ("ch22", "reflection institute in Nanjing",
     "The <i>Reflection Institute</i> (反省院) was a real",
     "The <i>reflection institute</i> (反省院) was a real"),
]

# First-appearance relocation: remove the duplicate ch31 note now placed at ch26.
REMOVALS = [("ch31", "osmanthus-sugared taro shoots")]


def main():
    notes = json.load(open(NOTES, encoding="utf-8"))
    changed = 0
    for unit, anchor_sub, old, new in PATCHES:
        if old == new:
            continue
        hits = [nt for nt in notes.get(unit, []) if anchor_sub in nt["anchor"]]
        if len(hits) != 1:
            sys.exit("%s: anchor-substring %r matched %d notes"
                     % (unit, anchor_sub, len(hits)))
        body = hits[0]["note"]
        c = body.count(old)
        if c != 1:
            sys.exit("%s [%s]: OLD occurs %dx (need 1): %r"
                     % (unit, anchor_sub, c, old))
        hits[0]["note"] = body.replace(old, new)
        changed += 1
        print("patched %s [%s]: %r -> %r"
              % (unit, hits[0]["anchor"][:30], old[:42], new[:42]))

    for unit, anchor_exact in REMOVALS:
        before = len(notes.get(unit, []))
        notes[unit] = [nt for nt in notes.get(unit, [])
                       if nt["anchor"] != anchor_exact]
        removed = before - len(notes[unit])
        if removed != 1:
            sys.exit("%s: expected to remove exactly 1 note %r, removed %d"
                     % (unit, anchor_exact, removed))
        print("removed %s note anchored %r (relocated to first appearance)"
              % (unit, anchor_exact))

    with open(NOTES, "w", encoding="utf-8") as fh:
        json.dump(notes, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("done; %d bodies patched, %d note(s) removed" % (changed, len(REMOVALS)))


if __name__ == "__main__":
    main()
