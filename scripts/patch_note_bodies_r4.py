#!/usr/bin/env python3
"""R4 note-body / anchor / glossary patches (apply_edits.py adds and moves
notes but never edits an existing body). All guarded (exact-count), never a
heredoc; notes.json and glossary.json rewritten via json.dump(ensure_ascii=
False, indent=2).

Jobs:
 1. Tier A day-first dates -> "Month D, YYYY" inside existing note bodies:
    ch30 (Ma Zhenhua), ch33 (Zhabei), ch35 (Vallon), ch37[frame], ch37[Anonymous].
 2. Tier A authority number: 白区 "the White area" -> "the White areas" in the
    ch11 body (the ch06 body already reads plural; the reading text has no
    occurrence book-wide).
 3. Anchor move for the ch37 frame note, whose anchor a date normalization in
    the reading text breaks ("4 April 1933 at Longhua Prison" ->
    "April 4, 1933, at Longhua Prison"); run conform_r4.py FIRST so the new
    anchor is a verbatim substring of the normalized reading.
 4. glossary.json 白区 -> "the White areas" (authority decided form).
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES = os.path.join(ROOT, "notes.json")
GLOSS = os.path.join(ROOT, "glossary.json")

# (unit, anchor-substring locating the note, OLD, NEW)
PATCHES = [
    ("ch30", "Ma Zhenhua",
     "on 17 March 1928", "on March 17, 1928"),
    ("ch33", "the Japanese army bombed Zhabei",
     "28&#8211;29 January", "January 28&#8211;29"),
    ("ch35", "the Vallon Monument",
     "on 6 May 1911", "on May 6, 1911"),
    ("ch37", "Longhua Prison",
     "at Longhua on 4 April 1933;", "at Longhua on April 4, 1933;"),
    ("ch37", "Longhua Prison",
     "which fell on 5 April in 1933)", "which fell on April 5 in 1933)"),
    ("ch37", "Longhua Prison",
     "on 7 February 1931", "on February 7, 1931"),
    ("ch37", "Anonymous",
     "market on 10 January 1933", "market on January 10, 1933"),
    ("ch11", "Red China",
     "in the White area was dangerous", "in the White areas were dangerous"),
]

# (unit, OLD anchor, NEW anchor) -- NEW must occur in the post-conform reading
ANCHOR_MOVES = [
    ("ch37", "4 April 1933 at Longhua Prison", "April 4, 1933, at Longhua Prison"),
]


def main():
    notes = json.load(open(NOTES, encoding="utf-8"))
    for unit, sub, old, new in PATCHES:
        hits = [n for n in notes.get(unit, []) if sub in n["anchor"]]
        if len(hits) != 1:
            sys.exit("%s: anchor-substring %r matched %d notes"
                     % (unit, sub, len(hits)))
        body = hits[0]["note"]
        if body.count(old) != 1:
            sys.exit("%s [%s]: OLD occurs %dx (need 1): %r"
                     % (unit, sub, body.count(old), old))
        hits[0]["note"] = body.replace(old, new)
        print("patched body %s [%s]: %r -> %r" % (unit, sub, old, new))

    for unit, oldA, newA in ANCHOR_MOVES:
        reading = open(os.path.join(ROOT, "out", "%s_reading.md" % unit),
                       encoding="utf-8").read()
        if newA not in reading:
            sys.exit("%s: new anchor not in reading (run conform_r4.py first): %r"
                     % (unit, newA))
        hits = [n for n in notes.get(unit, []) if n["anchor"] == oldA]
        if len(hits) != 1:
            sys.exit("%s: anchor %r matched %d notes" % (unit, oldA, len(hits)))
        hits[0]["anchor"] = newA
        print("moved anchor %s: %r -> %r" % (unit, oldA, newA))

    with open(NOTES, "w", encoding="utf-8") as fh:
        json.dump(notes, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    # glossary 白区 -> the White areas
    g = json.load(open(GLOSS, encoding="utf-8"))
    e = g["terms"]["白区"]
    if e["en"] != "the White areas":
        e["en"] = "the White areas"
        e["status"] = "decided"
        e["note"] = ("Real. Nationalist-controlled territory, opposed to the "
                     "'Red'/Soviet areas; the underground's world. Authority "
                     "decided form: plural collective 'the White areas' (R4).")
        with open(GLOSS, "w", encoding="utf-8") as fh:
            json.dump(g, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        print("glossary 白区 -> the White areas")
    else:
        print("glossary 白区 already plural")
    print("patch_note_bodies_r4: done")


if __name__ == "__main__":
    main()
