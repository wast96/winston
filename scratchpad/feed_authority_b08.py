#!/usr/bin/env python3
"""Feed this book's decided renderings back into authority.json (cross-book
name authority). Keyed by hanzi; each rendering maps to the list of book slugs
that used it. Idempotent: re-running only appends this book's slug where missing.

Book slug: lu-xiaofeng-1 (from book.json deliverable).
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = "lu-xiaofeng-1"

g = json.load(open(os.path.join(ROOT, "glossary.json"), encoding="utf-8"))
apath = os.path.join(ROOT, "authority.json")
a = json.load(open(apath, encoding="utf-8"))
terms = a.setdefault("terms", {})

SECTIONS = ("people", "organizations", "places", "terms")
added = updated = 0
for sec in SECTIONS:
    rows = g.get(sec, {})
    if not isinstance(rows, dict):
        continue
    for zh, row in rows.items():
        if not isinstance(row, dict) or "en" not in row:
            continue
        en = row["en"]
        status = row.get("status", "decided")
        note = row.get("note", "")
        entry = terms.get(zh)
        if entry is None:
            terms[zh] = {
                "renderings": {en: [SLUG]},
                "category": sec,
                "status": status,
                "note": note,
            }
            added += 1
        else:
            rends = entry.setdefault("renderings", {})
            slugs = rends.setdefault(en, [])
            if SLUG not in slugs:
                slugs.append(SLUG)
                updated += 1

with open(apath, "w", encoding="utf-8") as fh:
    json.dump(a, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

print("authority.json: %d new terms added, %d existing terms got this slug" %
      (added, updated))
print("total authority terms now:", len(terms))
