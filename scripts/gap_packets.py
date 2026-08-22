#!/usr/bin/env python3
"""Emit one JSON packet per chapter for the footnote-density pass.

Each packet lists the uncovered glossary subjects whose FIRST book-wide
appearance is in that chapter (from note_gaps logic), with a suggested
verbatim anchor confirmed present in the reading file, the vetted glossary
note as the factual seed, and the first paragraph for context. Also lists
the chapter's existing note anchors (so a drafter never duplicates).

Writes packets to <outdir>/<unit>_gappacket.json.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(name):
    return json.load(open(os.path.join(ROOT, name), encoding="utf-8"))


def unit_paras(unit):
    p = os.path.join(ROOT, "out", f"{unit}_reading.md")
    if not os.path.exists(p):
        return []
    return [l.rstrip("\n") for l in open(p, encoding="utf-8") if l.strip()]


def unit_text(unit):
    p = os.path.join(ROOT, "out", f"{unit}_reading.md")
    return open(p, encoding="utf-8").read() if os.path.exists(p) else ""


def main():
    outdir = sys.argv[1]
    os.makedirs(outdir, exist_ok=True)
    book = load("book.json")
    notes = load("notes.json")
    glo = load("glossary.json")
    order = [c["id"] for c in book["structure"]]

    covered_blobs = []
    for unit, arr in notes.items():
        for n in arr:
            covered_blobs.append(n.get("anchor", "").lower())
            covered_blobs.append(n.get("note", "").lower())
    covered_text = "\n".join(covered_blobs)

    subjects = []
    for cat in ("people", "places", "organizations", "terms"):
        for zh, row in glo.get(cat, {}).items():
            if isinstance(row, dict) and row.get("note") and row.get("en"):
                subjects.append((cat, zh, row["en"], row))

    paras = {u: unit_paras(u) for u in order}
    texts = {u: unit_text(u) for u in order}

    def find_first(en):
        pat = re.compile(r"(?<![A-Za-z])" + re.escape(en) + r"(?![A-Za-z])")
        for u in order:
            for para in paras[u]:
                if pat.search(para):
                    return u, para
        return None, None

    def anchor_for(en, unit):
        """Prefer the bare distinctive form if present verbatim in the file."""
        txt = texts[unit]
        candidates = [en]
        for pre in ("the ", "a ", "an ", "The "):
            if en.startswith(pre):
                candidates.append(en[len(pre):])
        for c in candidates:
            if c and c in txt:
                return c
        return en  # let apparatus_merge flag it if truly absent

    per = {u: [] for u in order}
    for cat, zh, en, row in subjects:
        u, para = find_first(en)
        if u is None or en.lower() in covered_text:
            continue
        per[u].append({
            "cat": cat,
            "en": en,
            "zh": zh,
            "suggested_anchor": anchor_for(en, u),
            "gloss_note": row.get("note", ""),
            "status": row.get("status", ""),
            "first_para": para,
        })

    for u in order:
        if not per[u]:
            continue
        packet = {
            "unit": u,
            "title_en": next(c["title_en"] for c in book["structure"]
                             if c["id"] == u),
            "existing_anchors": [n["anchor"] for n in notes.get(u, [])],
            "gaps": per[u],
        }
        with open(os.path.join(outdir, f"{u}_gappacket.json"), "w",
                  encoding="utf-8") as f:
            json.dump(packet, f, ensure_ascii=False, indent=2)
        print(f"{u}: {len(per[u])} gaps -> {u}_gappacket.json")


if __name__ == "__main__":
    main()
