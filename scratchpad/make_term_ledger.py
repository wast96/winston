#!/usr/bin/env python3
"""Generate out/term_ledger.md -- the auditable whole-book term ledger, straight
from glossary.json. One table per section (people, organizations, places,
terms), every row: hanzi, English rendering, pinyin, status. Notes are stripped
of numeric character references for plain-text reading."""
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
g = json.load(open(os.path.join(ROOT, "glossary.json"), encoding="utf-8"))

SECTIONS = [("people", "People"), ("organizations", "Organisations"),
            ("places", "Places"), ("terms", "Terms & epithets")]


def plain(s):
    s = re.sub(r"<[^>]+>", "", s or "")
    s = html.unescape(s)
    return " ".join(s.split())


def cell(s):
    return plain(s).replace("|", "\\|")


out = ["# Term ledger -- The Golden Roc Dynasty (Lu Xiaofeng, Vol. 1)",
       "",
       "The auditable record of every decided rendering, generated from "
       "`glossary.json`. One rendering per referent, book-wide; statuses are "
       "*attested* (found in English-language scholarship), *decided* (a "
       "settled house rendering), or *provisional* (a romanization not yet "
       "attested). Fed back into the cross-book `authority.json` on "
       "completion.", ""]

grand = 0
for key, label in SECTIONS:
    rows = g.get(key, {})
    if not isinstance(rows, dict) or not rows:
        continue
    out.append("## %s (%d)" % (label, len(rows)))
    out.append("")
    out.append("| Source | Rendering | Pinyin | Status |")
    out.append("| --- | --- | --- | --- |")
    for zh, row in sorted(rows.items(), key=lambda kv: kv[1].get("en", "")):
        out.append("| %s | %s | %s | %s |" % (
            zh, cell(row.get("en", "")), cell(row.get("pinyin", "")),
            row.get("status", "")))
        grand += 1
    out.append("")

out.insert(4, "**%d rows total.**" % grand)
out.insert(5, "")

dest = os.path.join(ROOT, "out", "term_ledger.md")
with open(dest, "w", encoding="utf-8") as fh:
    fh.write("\n".join(out) + "\n")
print("wrote %s: %d rows across %d sections" %
      (dest, grand, sum(1 for k, _ in SECTIONS if g.get(k))))
