#!/usr/bin/env python3
"""Find glossary subjects that appear in the reading text but are never
touched by any existing footnote — the first-appearance gaps for a
density pass.

For each glossary row that carries a substantive `note`, locate the FIRST
unit (in book.json reading order) and paragraph whose English prose contains
the row's `en` form (word-boundary match). Then decide whether that subject
is already served by an existing footnote anywhere in the book: a subject is
considered COVERED if its `en` form (or a distinctive token of it) occurs
inside any existing note anchor or note body.

Output: for each chapter, the un-covered subjects whose first appearance is
in that chapter, with the paragraph text so a note anchor can be chosen.

Usage: note_gaps.py [chapter_id]
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(name):
    return json.load(open(os.path.join(ROOT, name), encoding="utf-8"))


def reading_order(book):
    return [c["id"] for c in book["structure"]]


def unit_paras(unit):
    p = os.path.join(ROOT, "out", f"{unit}_reading.md")
    if not os.path.exists(p):
        return []
    out = []
    for line in open(p, encoding="utf-8"):
        s = line.rstrip("\n")
        if not s.strip():
            continue
        out.append(s)
    return out


def main():
    book = load("book.json")
    notes = load("notes.json")
    glо = load("glossary.json")  # noqa
    order = reading_order(book)

    # Build the "covered" text: all anchors + note bodies, lowercased.
    covered_blobs = []
    for unit, arr in notes.items():
        for n in arr:
            covered_blobs.append(n.get("anchor", "").lower())
            covered_blobs.append(n.get("note", "").lower())
    covered_text = "\n".join(covered_blobs)

    # existing anchors per unit (to know what's already anchored where)
    anchors_by_unit = {u: [n["anchor"] for n in arr] for u, arr in notes.items()}

    # Gather subjects with notes.
    subjects = []
    for cat in ("people", "places", "organizations", "terms"):
        for zh, row in glо.get(cat, {}).items():
            if not isinstance(row, dict):
                continue
            note = row.get("note")
            en = row.get("en")
            if not note or not en:
                continue
            subjects.append((cat, zh, en, row))

    # Preload unit paragraphs in order.
    paras = {u: unit_paras(u) for u in order}

    def find_first(en):
        # word-boundary, case-sensitive-ish (allow leading cap)
        pat = re.compile(r"(?<![A-Za-z])" + re.escape(en) + r"(?![A-Za-z])")
        for u in order:
            for i, para in enumerate(paras[u]):
                if pat.search(para):
                    return u, i, para
        return None, None, None

    def is_covered(en):
        return en.lower() in covered_text

    filt = sys.argv[1] if len(sys.argv) > 1 else None
    results = {u: [] for u in order}
    for cat, zh, en, row in subjects:
        u, i, para = find_first(en)
        if u is None:
            continue  # never appears in prose
        if is_covered(en):
            continue  # already discussed in some note
        results[u].append((cat, en, zh, row.get("note", ""), para))

    for u in order:
        rows = results[u]
        if filt and u != filt:
            continue
        if not rows:
            continue
        print(f"\n===== {u} : {len(rows)} uncovered subjects =====")
        # sort people first then places/orgs/terms
        rank = {"people": 0, "places": 1, "organizations": 2, "terms": 3}
        rows.sort(key=lambda r: rank.get(r[0], 9))
        for cat, en, zh, note, para in rows:
            snippet = para[:110]
            print(f"[{cat}] {en}  ({zh})")
            print(f"    glossnote: {note[:160]}")
            print(f"    firstpara: {snippet}")
    # summary
    total = sum(len(results[u]) for u in order)
    print(f"\nTOTAL uncovered subjects appearing in prose: {total}")


if __name__ == "__main__":
    main()
