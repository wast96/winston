#!/usr/bin/env python3
"""Add B08 (ch13) glossary rows under the two-level sections (NOT the flat
apparatus path). Idempotent: skips a key already present. Validate with
check_apparatus.py."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(ROOT, "glossary.json")
g = json.load(open(path, encoding="utf-8"))

terms = {
    "狐狸精": {
        "en": "fox-spirit", "pinyin": "huli jing", "status": "decided",
        "note": "In Chinese folklore a fox that has cultivated the power to "
                "take human shape, most often a beautiful woman, and bewitches "
                "men; in common speech, an insult for a seductress or "
                "husband-stealer, with the ghostly sense worn away. Distinct "
                "from the plain &#8216;little fox&#8217; (&#23567;&#29392;&#29432;), "
                "which marks only slyness. See the note at first appearance "
                "(ch13, the Coda).",
    },
}

added = []
for sec, rows in (("terms", terms),):
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
    print(" ", a)
print("total rows now:", sum(len(v) for v in g.values() if isinstance(v, dict)))
