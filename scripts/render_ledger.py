#!/usr/bin/env python3
"""Render glossary.json as out/term_ledger.md, the auditable term ledger:
every decided rendering, so someone who reads no Chinese can check the book's
name and term choices. Groups by status, sorts by English form.

Usage: render_ledger.py
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
META = {"_about", "book", "people", "organizations", "places", "terms"}


def deref(s):
    # numeric character references -> plain text for the markdown ledger
    s = re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), s)
    return re.sub(r"<[^>]+>", "", s)


def main():
    g = json.load(open(os.path.join(ROOT, "glossary.json"), encoding="utf-8"))
    rows = [(k, v) for k, v in g.items() if k not in META and isinstance(v, dict)]
    by_status = {"attested": [], "provisional": [], "decided": [], "other": []}
    for zh, v in rows:
        st = v.get("status", "other")
        by_status.get(st, by_status["other"]).append((zh, v))

    out = []
    out.append("# Term Ledger — *China's Secret War*\n")
    out.append("The single source of truth for every rendering in the "
               "translation. One rendering per referent for the whole book. "
               "Status: **attested** (a form used in scholarship), "
               "**provisional** (a romanization not found outside the source; "
               "the build marks these visibly), **decided** (a project style "
               "call).\n")
    out.append("Total entries: %d.\n" % len(rows))
    labels = [("attested", "Attested"), ("decided", "Decided"),
              ("provisional", "Provisional"), ("other", "Unclassified")]
    for key, title in labels:
        items = by_status[key]
        if not items:
            continue
        items.sort(key=lambda kv: (kv[1].get("en") or "").lower())
        out.append("\n## %s (%d)\n" % (title, len(items)))
        out.append("| English | Pinyin | 中文 | Note |")
        out.append("| --- | --- | --- | --- |")
        for zh, v in items:
            en = (v.get("en") or "").replace("|", "\\|")
            py = (v.get("pinyin") or "").replace("|", "\\|")
            note = deref(v.get("note") or "").replace("|", "\\|").replace("\n", " ")
            if len(note) > 240:
                note = note[:237] + "..."
            principal = " \u2605" if v.get("principal") else ""
            out.append("| %s%s | %s | %s | %s |" % (en, principal, py, zh, note))
    text = "\n".join(out) + "\n"
    dest = os.path.join(ROOT, "out", "term_ledger.md")
    with open(dest, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote out/term_ledger.md: %d entries (%d attested, %d decided, "
          "%d provisional)" % (len(rows), len(by_status["attested"]),
          len(by_status["decided"]), len(by_status["provisional"])))


if __name__ == "__main__":
    main()
