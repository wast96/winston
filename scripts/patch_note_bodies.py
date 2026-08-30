#!/usr/bin/env python3
"""R2 note-body patches: Tier A date normalization (day-first -> Month D, YYYY)
in ch11-ch19 note bodies, plus the Massenet/Haige gloss updates that the R2
name conformances require. apply_edits.py adds/moves notes but never edits an
existing body; this does that, safely: each (unit, anchor-substring, old->new)
must match exactly one note and OLD must occur exactly once in it. notes.json is
rewritten via json.dump(ensure_ascii=False, indent=2), the apply_edits format.
"""
import json
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES = os.path.join(ROOT, "notes.json")

# (unit, anchor-substring to locate the note, OLD, NEW)
PATCHES = [
    # --- Tier A: name conformances that touch existing bodies ---
    ("ch11", "Route Massenet", "<i>Massenet Road</i> (马斯南路)", "<i>Route Massenet</i> (马斯南路)"),
    ("ch11", "Zhaozhujiao Road",
     "<i>Haige Road</i> (海格路, Avenue Haig; today Huashan Road)",
     "<i>Avenue Haig</i> (海格路; today Huashan Road)"),
    # --- Tier A: day-first dates -> Month D, YYYY in ch11-ch19 note bodies ---
    ("ch11", "Red China", "at Ruijin on 11 December 1931", "at Ruijin on December 11, 1931"),
    ("ch13", "the greatest living dramatist",
     "reached Shanghai on 17 February 1933", "reached Shanghai on February 17, 1933"),
    ("ch13", "the greatest living dramatist",
     "(11&#8211;12 February)", "(February 11&#8211;12)"),
    ("ch13", "Bogu", "on a decision of 13 January 1933", "on a decision of January 13, 1933"),
    ("ch14", "workers' pickets",
     "the third uprising of 21 March 1927", "the third uprising of March 21, 1927"),
    ("ch14", "the Twenty-Sixth Army",
     "on 12&#8211;13 April it tricked", "on April 12&#8211;13 it tricked"),
    ("ch15", "stormed into the Soviet consulate",
     "on 13 December 1927", "on December 13, 1927"),
    ("ch15", "the August 7th Conference",
     "secretly at Hankou on 7 August 1927", "secretly at Hankou on August 7, 1927"),
    ("ch15", "the Canton",
     "the Shakee (Shaji) shooting of 23 June 1925", "the Shakee (Shaji) shooting of June 23, 1925"),
    ("ch19", "February, she remembered",
     "at Longhua on 7 February 1931", "at Longhua on February 7, 1931"),
]


def main():
    notes = json.load(open(NOTES, encoding="utf-8"))
    changed = 0
    for unit, anchor_sub, old, new in PATCHES:
        if old == new:
            continue
        hits = [nt for nt in notes.get(unit, []) if anchor_sub in nt["anchor"]]
        if len(hits) != 1:
            sys.exit("%s: anchor-substring %r matched %d notes" % (unit, anchor_sub, len(hits)))
        body = hits[0]["note"]
        c = body.count(old)
        if c != 1:
            sys.exit("%s [%s]: OLD occurs %dx (need 1): %r" % (unit, anchor_sub, c, old))
        hits[0]["note"] = body.replace(old, new)
        changed += 1
        print("patched %s [%s]: %r -> %r" % (unit, hits[0]["anchor"][:30], old[:40], new[:40]))
    with open(NOTES, "w", encoding="utf-8") as fh:
        json.dump(notes, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("done; %d bodies patched" % changed)


if __name__ == "__main__":
    main()
