#!/usr/bin/env python3
"""Render glossary.json as a human-readable term ledger (out/term_ledger.md).

So a reader who knows no Chinese can audit every decided rendering: hanzi,
English form, pinyin, status, and any note, grouped by category and sorted by
the English form. Regenerable; run at whole-book completion.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CAT_TITLES = {
    "people": "People",
    "organizations": "Organizations",
    "places": "Places",
    "terms": "Terms",
    "book": "Works",
}


def main():
    g = json.load(open(os.path.join(ROOT, "glossary.json"), encoding="utf-8"))
    out = ["# Term Ledger",
           "",
           "Every decided rendering in this book, so a reader who knows no "
           "Chinese can audit each one. Generated from `glossary.json` by "
           "`scripts/make_ledger.py`; do not hand-edit.",
           ""]
    total = 0
    for cat, rows in g.items():
        if not isinstance(rows, dict) or cat.startswith("_"):
            continue
        items = [(h, r) for h, r in rows.items() if isinstance(r, dict)]
        if not items:
            continue
        out.append("## %s (%d)" % (CAT_TITLES.get(cat, cat.title()), len(items)))
        out.append("")
        out.append("| Chinese | English | Pinyin | Status | Note |")
        out.append("| --- | --- | --- | --- | --- |")
        for h, r in sorted(items, key=lambda x: (x[1].get("en") or "").lower()):
            note = (r.get("note") or "").replace("|", "\\|").replace("\n", " ")
            out.append("| %s | %s | %s | %s | %s |" % (
                h, r.get("en", ""), r.get("pinyin", ""),
                r.get("status", ""), note))
            total += 1
        out.append("")
    out.insert(3, "**%d entries total.**" % total)
    out.insert(4, "")
    dst = os.path.join(ROOT, "out", "term_ledger.md")
    open(dst, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("wrote %s (%d entries)" % (dst, total))


if __name__ == "__main__":
    main()
