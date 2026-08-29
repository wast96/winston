#!/usr/bin/env python3
"""Pre-flight anchor check for an edit list, before apply_edits.py runs.

Every note anchor and figure `before` anchor is a verbatim substring of the
reading text; a prose edit whose OLD contains one will break it unless the
NEW preserves it or the same pass moves the anchor in notes.json /
figures.json. The builder's refusal on an unmatched anchor is the backstop,
not the check: run this BEFORE applying, fix the collisions in the edit list,
and never discover them at build time.

Usage: anchor_check.py <unit> [edits-suffix]
Reads edits/<unit>_<suffix>.md (default suffix "edits") in the apply_edits
grammar and reports every OLD line that contains a live anchor.

Provenance: built on the-sword-roars' revision pass, refined on
chinas-secret-war's; promoted to the shared scripts in template v2.3.
"""
import json
import sys
from pathlib import Path


def rows(path, unit, key):
    p = Path(path)
    if not p.is_file():
        return []
    return [r[key] for r in json.loads(p.read_text(encoding="utf-8"))
            .get(unit, []) if key in r]


def main():
    if len(sys.argv) < 2:
        sys.stderr.write(__doc__)
        return 2
    unit = sys.argv[1]
    suffix = sys.argv[2] if len(sys.argv) > 2 else "edits"
    edits = Path("edits/%s_%s.md" % (unit, suffix))
    if not edits.is_file():
        sys.stderr.write("anchor_check: no edit list at %s\n" % edits)
        return 2
    notes = rows("notes.json", unit, "anchor")
    figs = rows("figures.json", unit, "before")
    olds = [ln[5:].rstrip("\n") for ln in edits.open(encoding="utf-8")
            if ln.startswith("OLD: ")]
    print("anchor_check: %s vs %d note anchor(s), %d figure anchor(s), "
          "%d OLD line(s)" % (edits, len(notes), len(figs), len(olds)))
    found = False
    for o in olds:
        for a in notes:
            if a in o:
                print("NOTE anchor in OLD:", repr(a[:50]), "|", o[:45])
                found = True
        for a in figs:
            if a in o:
                print("FIGURE anchor in OLD:", repr(a[:50]), "|", o[:45])
                found = True
    print("--- collisions found; ensure NEW preserves them or add a "
          "NOTE-ANCHOR move in the same pass ---" if found
          else "--- no anchor collisions ---")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
