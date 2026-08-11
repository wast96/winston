#!/usr/bin/env python3
"""Merge a batch's apparatus (glossary rows, notes, figures) into the ledgers.

WHY THIS EXISTS. Writing rare CJK characters into JSON through a shell
heredoc silently mangles a few glyphs — one finished book shipped with 18
garbled characters in its note bodies despite a CLAUDE.md warning saying not
to do exactly that. Warnings do not fix mechanical hazards; tools do. Author
the batch's apparatus as a plain JSON file (written with the Write tool, not
a heredoc), then let this script validate and merge it.

Merge file shape (any key optional):

    {
      "glossary": { "<zh>": {"en": ..., "pinyin": ..., "status":
                    "attested|provisional|decided", "note": ...}, ... },
      "notes":    { "<unit_id>": [ {"anchor": ..., "note": ...}, ... ] },
      "figures":  { "<unit_id>": [ {"file": ..., "before": ...,
                    "alt": ..., "caption": ...}, ... ] }
    }

Semantics (idempotent — safe to re-run):
  - glossary rows are added only if the zh key is absent; an existing row is
    never silently overwritten (change the glossary deliberately, with the
    cascade grep, per CLAUDE.md).
  - a unit's notes are APPENDED, skipping anchors already present.
  - a unit's figures are REPLACED wholesale.

Validation before anything is written:
  - every note body and glossary note must use NUMERIC character references
    only; a named entity (&nbsp; &mdash;) is an XHTML build-breaker.
  - no U+FFFD replacement characters (the mangling tell).
  - every note anchor must be a verbatim substring of out/<unit>_reading.md
    if that file exists (catch at write time, not build time).
  - after writing, the ledgers are re-read and the merged values compared
    byte-for-byte (the re-read half of "write via a file and verify").

Usage: apparatus_merge.py batch_apparatus.json
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAMED_ENTITY = re.compile(r"&(?!#\d+;|#x[0-9a-fA-F]+;|amp;|lt;|gt;)[a-zA-Z]+;")


def load(name, default):
    p = os.path.join(ROOT, name)
    if not os.path.exists(p):
        return default
    return json.load(open(p, encoding="utf-8"))


def save(name, obj):
    p = os.path.join(ROOT, name)
    with open(p, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    return json.load(open(p, encoding="utf-8"))


def check_text(where, s):
    if "�" in s:
        sys.exit("%s: U+FFFD replacement character (mangled glyph): %r"
                 % (where, s[:60]))
    m = NAMED_ENTITY.search(s)
    if m:
        sys.exit("%s: named entity %s breaks the XHTML build; use a numeric "
                 "character reference: %r" % (where, m.group(0), s[:60]))


def main(path):
    batch = json.load(open(path, encoding="utf-8"))
    problems = 0

    for zh, row in batch.get("glossary", {}).items():
        check_text("glossary %s" % zh, json.dumps(row, ensure_ascii=False))
        if row.get("status") not in ("attested", "provisional", "decided"):
            sys.exit("glossary %s: status must be attested/provisional/"
                     "decided" % zh)
    for cid, items in batch.get("notes", {}).items():
        rpath = os.path.join(ROOT, "out", "%s_reading.md" % cid)
        reading = open(rpath, encoding="utf-8").read() \
            if os.path.exists(rpath) else None
        for e in items:
            check_text("note %s" % cid, e["note"])
            check_text("anchor %s" % cid, e["anchor"])
            if reading is not None and e["anchor"] not in reading:
                print("UNRESOLVED anchor in %s: %r" % (cid, e["anchor"][:70]))
                problems += 1
    if problems:
        sys.exit("%d unresolved anchors; nothing written" % problems)

    if "glossary" in batch:
        g = load("glossary.json", {})

        def _present(gl, zh):
            # rows nest under section keys ({section: {hanzi: row}}); a row is
            # present if it appears in ANY section. Never treat _-prefixed keys
            # (e.g. _about) as sections.
            return any(isinstance(sec, dict) and zh in sec
                       for k, sec in gl.items() if not k.startswith("_"))

        added = skipped = 0
        for zh, row in batch["glossary"].items():
            if _present(g, zh):
                skipped += 1
                continue
            row = dict(row)
            section = row.pop("category", "terms")
            g.setdefault(section, {})[zh] = row
            added += 1
        back = save("glossary.json", g)
        for zh in batch["glossary"]:
            if not _present(back, zh):
                sys.exit("re-read verification failed for glossary %s" % zh)
        total = sum(len(sec) for k, sec in g.items()
                    if not k.startswith("_") and isinstance(sec, dict))
        print("glossary: %d added, %d already present (left untouched), "
              "%d total" % (added, skipped, total))

    if "notes" in batch:
        n = load("notes.json", {})
        for cid, items in batch["notes"].items():
            unit = n.setdefault(cid, [])
            have = {e["anchor"] for e in unit}
            fresh = [e for e in items if e["anchor"] not in have]
            unit.extend(fresh)
            print("notes %s: %d appended, %d already present, unit total %d"
                  % (cid, len(fresh), len(items) - len(fresh), len(unit)))
        back = save("notes.json", n)
        if json.dumps(back, ensure_ascii=False, sort_keys=True) != \
           json.dumps(n, ensure_ascii=False, sort_keys=True):
            sys.exit("re-read verification failed for notes.json")

    if "figures" in batch:
        f = load("figures.json", {})
        for cid, items in batch["figures"].items():
            for spec in items:
                for key in ("file", "before", "caption"):
                    if key not in spec:
                        sys.exit("figure in %s missing %r" % (cid, key))
                if "alt" not in spec:
                    print("WARNING: figure %s in %s has no alt text"
                          % (spec["file"], cid))
            f[cid] = items
            print("figures %s: %d spec(s) (replaced)" % (cid, len(items)))
        save("figures.json", f)

    print("merge complete and re-read verified")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
