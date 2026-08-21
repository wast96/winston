#!/usr/bin/env python3
"""Feed this book's decided renderings from glossary.json into the cross-book
authority ledger (authority.json), tagged with this book's slug. Idempotent.

For each glossary term with an English form, ensure authority.terms[zh] holds
that rendering with the slug in its book list. Existing shelf entries and other
books' slugs are preserved untouched; a rendering this book uses is added (or
the slug appended to an existing identical rendering).

Usage: feed_authority.py
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = "chinas-secret-war"
META = {"_about", "book", "people", "organizations", "places", "terms"}


def category_for(zh, row):
    py = row.get("pinyin") or ""
    en = row.get("en") or ""
    # crude: a two/three-char zh with a capitalized two-token pinyin name -> person
    if py and py[:1].isupper() and 1 <= len(py.split()) <= 2 and \
       2 <= len(zh) <= 4 and not en.lower().startswith("the "):
        return "people"
    if en.lower().startswith("the "):
        return "organizations"
    return "terms"


def main():
    g = json.load(open(os.path.join(ROOT, "glossary.json"), encoding="utf-8"))
    a = json.load(open(os.path.join(ROOT, "authority.json"), encoding="utf-8"))
    terms = a.setdefault("terms", {})
    added = tagged = 0
    for zh, row in g.items():
        if zh in META or not isinstance(row, dict):
            continue
        en = row.get("en")
        if not en:
            continue
        entry = terms.get(zh)
        if entry is None:
            entry = {"renderings": {}, "category": category_for(zh, row),
                     "status": "book-decided"}
            if row.get("note"):
                entry["note"] = row["note"]
            terms[zh] = entry
            added += 1
        rends = entry.setdefault("renderings", {})
        books = rends.setdefault(en, [])
        if SLUG not in books:
            books.append(SLUG)
            tagged += 1
    with open(os.path.join(ROOT, "authority.json"), "w", encoding="utf-8") as f:
        json.dump(a, f, ensure_ascii=False, indent=1)
        f.write("\n")
    # re-read verify
    back = json.load(open(os.path.join(ROOT, "authority.json"), encoding="utf-8"))
    assert len(back["terms"]) >= len(terms) - 1
    print("authority.json: %d new term(s), %d rendering(s) tagged '%s'; "
          "%d terms total" % (added, tagged, SLUG, len(back["terms"])))


if __name__ == "__main__":
    main()
