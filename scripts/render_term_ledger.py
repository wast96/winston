#!/usr/bin/env python3
"""Render glossary.json as out/term_ledger.md: a human-auditable table of every
decided rendering, so someone who reads no Chinese can check the whole ledger
(CLAUDE.md 'Definition of done'). One table per section; the note column carries
the identification (numeric character references decoded to plain text)."""
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def plain(s):
    return re.sub(r"\s+", " ", html.unescape(s or "").replace("|", "\\|")).strip()


def main():
    g = json.load(open(os.path.join(ROOT, "glossary.json"), encoding="utf-8"))
    out = ["# Term ledger — The Tragedy of the Chinese Revolution",
           "",
           "Every decided rendering in `glossary.json`, for a reader who reads "
           "no Chinese. **English (text)** is the Wade-Giles or conventional "
           "form Isaacs prints and which stays in the body; **Pinyin** is the "
           "modern form given in the glossary and first-appearance notes.", ""]
    principals = []
    for section in ("people", "organizations", "places", "terms"):
        rows = g.get(section, {})
        if not rows:
            continue
        out.append("## %s (%d)" % (section.title(), len(rows)))
        out.append("")
        out.append("| English (text) | Pinyin | Hanzi | Status | Note |")
        out.append("|---|---|---|---|---|")
        for zh, rec in sorted(rows.items(),
                              key=lambda kv: kv[1].get("pinyin") or kv[1]["en"]):
            out.append("| %s | %s | %s | %s | %s |" % (
                plain(rec.get("en", "")), plain(rec.get("pinyin", "")),
                zh, rec.get("status", ""), plain(rec.get("note", ""))))
            if rec.get("principal"):
                principals.append((rec.get("cast_order", 99), plain(rec["en"])))
        out.append("")
    if principals:
        out.append("## Principal characters (front-matter page)")
        out.append("")
        for order, en in sorted(principals):
            out.append("%d. %s" % (order, en))
        out.append("")
    dest = os.path.join(ROOT, "out", "term_ledger.md")
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    n = sum(len(g.get(s, {})) for s in ("people", "organizations", "places", "terms"))
    print("wrote %s (%d rows)" % (dest, n))


if __name__ == "__main__":
    main()
