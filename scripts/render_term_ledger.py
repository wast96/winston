#!/usr/bin/env python3
"""Render glossary.json as out/term_ledger.md — the auditable term ledger.

One row per decided rendering, grouped by section, so a reader with no
Japanese can audit every choice: source form, English rendering, status,
and the gloss. Principals are flagged. Note bodies may carry numeric
character references (from the apparatus); they are shown verbatim, which
is legible enough for an audit table.

Usage: python3 scripts/render_term_ledger.py
"""
import json, os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECTIONS = [("people", "People"), ("organizations", "Organizations"),
            ("places", "Places"), ("terms", "Terms")]


def unent(s):
    """Numeric character references -> characters, for a plain-text table."""
    return html.unescape(s or "")


def cell(s):
    return unent(s).replace("|", "\\|").replace("\n", " ").strip()


def main():
    g = json.load(open(os.path.join(ROOT, "glossary.json"), encoding="utf-8"))
    meta = json.load(open(os.path.join(ROOT, "book.json"), encoding="utf-8"))
    out = []
    out.append("# Term ledger — %s" % meta.get("title_en", ""))
    out.append("")
    out.append("Every rendering decided for this book, grouped by kind, so the "
               "choices can be audited without reading Japanese. **Status:** "
               "*attested* = a form used in English scholarship; *provisional* "
               "= a romanization of mine, not found outside; *decided* = a "
               "project style call. Principals (the front-matter cast) are "
               "marked \u2605.")
    out.append("")
    total = 0
    for key, label in SECTIONS:
        sec = g.get(key, {})
        if not sec:
            continue
        # sort: principals first (by cast_order), then by English rendering
        def sort_key(item):
            v = item[1]
            return (0, v.get("cast_order", 0)) if v.get("principal") \
                else (1, unent(v.get("en", "")).lower())
        rows = sorted(sec.items(), key=sort_key)
        out.append("## %s (%d)" % (label, len(rows)))
        out.append("")
        out.append("| Source | Rendering | Status | Note |")
        out.append("| --- | --- | --- | --- |")
        for cjk, v in rows:
            star = " \u2605" if v.get("principal") else ""
            out.append("| %s | %s%s | %s | %s |"
                       % (cell(cjk), cell(v.get("en", "")), star,
                          cell(v.get("status", "")), cell(v.get("note", ""))))
            total += 1
        out.append("")
    out.append("---")
    out.append("")
    out.append("%d entries total. Rendered from `glossary.json` "
               "(`scripts/render_term_ledger.py`)." % total)
    dest = os.path.join(ROOT, "out", "term_ledger.md")
    open(dest, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("wrote %s (%d entries)" % (dest, total))


if __name__ == "__main__":
    main()
