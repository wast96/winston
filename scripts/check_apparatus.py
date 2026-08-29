#!/usr/bin/env python3
"""Scan the apparatus ledgers for the defects that shipped on real books.

What it looks for, and why:

  1. NAMED HTML ENTITIES in note/glossary bodies (&nbsp; &mdash; &times;).
     Undefined in XHTML; the build breaks, or worse, a lenient parser ships
     them visibly broken. Numeric character references only.
  2. U+FFFD REPLACEMENT CHARACTERS and mojibake tells. One book shipped 18
     garbled CJK glyphs written through a shell heredoc.
  3. DOUBLE-ESCAPED REFERENCES (&amp;#8217;). One builder esc()'d fields that
     already contained character references and 298 glossary entries rendered
     visibly broken. If this fires, either the ledger or the builder is
     double-encoding.
  4. DUPLICATE ANCHORS within a unit (a note silently attaches to the first).
  5. ANCHOR RESOLUTION against out/<unit>_reading.md where present — catch at
     write time what the builder would refuse at build time.
  6. GLOSSARY STATUS values outside attested/provisional/decided, and rows
     whose attested/decided status has an empty note (the attestation IS the
     point of the ledger).

Exit 1 on any hard failure (1, 2, 3, 5); 4 and 6 are warnings.

Usage: check_apparatus.py            (from the project root)
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAMED_ENTITY = re.compile(r"&(?!#\d+;|#x[0-9a-fA-F]+;|amp;|lt;|gt;)[a-zA-Z]+;")
DOUBLE_ESC = re.compile(r"&amp;#\d+;")


def scan_text(where, s, hard, soft):
    if "�" in s:
        hard.append("%s: U+FFFD replacement character: %r" % (where, s[:70]))
    m = NAMED_ENTITY.search(s)
    if m:
        hard.append("%s: named entity %s: %r" % (where, m.group(0), s[:70]))
    m = DOUBLE_ESC.search(s)
    if m:
        hard.append("%s: double-escaped reference %s: %r"
                    % (where, m.group(0), s[:70]))


def main():
    hard, soft = [], []

    npath = os.path.join(ROOT, "notes.json")
    if os.path.exists(npath):
        notes = json.load(open(npath, encoding="utf-8"))
        for cid, items in notes.items():
            if cid.startswith("_"):
                continue
            seen = {}
            rpath = os.path.join(ROOT, "out", "%s_reading.md" % cid)
            reading = open(rpath, encoding="utf-8").read() \
                if os.path.exists(rpath) else None
            for e in items:
                scan_text("notes[%s]" % cid, e.get("note", ""), hard, soft)
                scan_text("anchor[%s]" % cid, e.get("anchor", ""), hard, soft)
                a = e.get("anchor", "")
                seen[a] = seen.get(a, 0) + 1
                if reading is not None and a not in reading:
                    hard.append("notes[%s]: anchor does not resolve: %r"
                                % (cid, a[:70]))
            for a, n in seen.items():
                if n > 1:
                    soft.append("notes[%s]: anchor appears %d times in the "
                                "ledger: %r" % (cid, n, a[:70]))

    gpath = os.path.join(ROOT, "glossary.json")
    if os.path.exists(gpath):
        gloss = json.load(open(gpath, encoding="utf-8"))
        for zh, row in gloss.items():
            if zh.startswith("_"):
                continue
            if isinstance(row, dict):
                scan_text("glossary[%s]" % zh,
                          json.dumps(row, ensure_ascii=False), hard, soft)
                st = row.get("status")
                if st not in ("attested", "provisional", "decided", None):
                    soft.append("glossary[%s]: unknown status %r" % (zh, st))
                elif st in ("attested", "decided") and not row.get("note"):
                    soft.append("glossary[%s]: %s but no attestation note"
                                % (zh, st))

    for msg in hard:
        print("FAIL", msg)
    for msg in soft:
        print("warn", msg)
    print("apparatus scan: %d failure(s), %d warning(s)" % (len(hard), len(soft)))
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
