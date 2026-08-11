#!/usr/bin/env python3
"""Add B07 (ch12) glossary rows under the two-level sections (NOT the flat
apparatus path). Idempotent: skips a key already present. Validate with
check_apparatus.py."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(ROOT, "glossary.json")
g = json.load(open(path, encoding="utf-8"))

people = {
    "青枫": {
        "en": "the Taoist Qingfeng", "pinyin": "Qingfeng", "status": "decided",
        "note": "The Taoist abbot of the Green Wind Temple and Huo Tianqing&#8217;s "
                "friend over the chessboard; bought by Huo Xiu to bear false "
                "witness that Huo Tianqing had died by his own hand, and burned "
                "with his temple soon after (ch12).",
    },
    "鲁班": {
        "en": "Lu Ban", "pinyin": "Lu Ban", "status": "attested",
        "note": "The legendary master carpenter and engineer of the state of Lu "
                "in the fifth century BCE, patron deity of builders and "
                "craftsmen; Zhu Ting&#8217;s art of contrivances descends from "
                "him. See the note at his first mention (ch12).",
    },
    "鲁大师": {
        "en": "Master Lu", "pinyin": "Lu Dashi", "status": "decided",
        "note": "Zhu Ting&#8217;s master in the maker&#8217;s art and a descendant "
                "of Lu Ban; now dead, leaving Zhu Ting the first hand under "
                "heaven at the making of hidden contrivances (ch12).",
    },
}

places = {
    "青风观": {
        "en": "the Green Wind Temple", "pinyin": "Qingfeng Guan",
        "status": "decided",
        "note": "The Taoist temple on the front of Huo Xiu&#8217;s mountain, "
                "where Huo Tianqing&#8217;s body is found; its abbot is the "
                "Taoist Qingfeng (青枫), whose name chimes with the temple&#8217;s "
                "(both sound <i>Qingfeng</i>). Huo Xiu burns it to the ground "
                "to destroy the one witness to his lie (ch12).",
    },
}

added = []
for sec, rows in (("people", people), ("places", places)):
    for zh, row in rows.items():
        if zh in g[sec]:
            continue
        g[sec][zh] = row
        added.append("%s/%s -> %s" % (sec, zh, row["en"]))

with open(path, "w", encoding="utf-8") as fh:
    json.dump(g, fh, ensure_ascii=False, indent=2)
    fh.write("\n")

print("added %d rows:" % len(added))
for a in added:
    print("  " + a)
