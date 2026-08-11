#!/usr/bin/env python3
"""Add B06 glossary rows under the two-level sections (NOT the flat apparatus
path). Idempotent: skips a key already present. Validate with
check_apparatus.py."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(ROOT, "glossary.json")
g = json.load(open(path, encoding="utf-8"))

A = "&#8217;"  # curly apostrophe, matching the existing notes' typography

people = {
    "马秀真": {
        "en": "Ma Xiuzhen", "pinyin": "Ma Xiuzhen", "status": "decided",
        "note": "The eldest of the Four Beauties of Emei; tall, with a pair "
                "of long phoenix eyes and a killing air even as she smiles. "
                "She leads the four in the bath-house interrogation of Lu "
                "Xiaofeng (ch09).",
    },
    "叶秀珠": {
        "en": "Ye Xiuzhu", "pinyin": "Ye Xiuzhu", "status": "decided",
        "note": "The third of the Four Beauties of Emei, and the honest, "
                "plain-spoken one of the four (ch09).",
    },
    "孙秀青": {
        "en": "Sun Xiuqing", "pinyin": "Sun Xiuqing", "status": "decided",
        "note": "The second of the Four Beauties of Emei; big-eyed, "
                "thin-lipped and sharp-tongued, and taken despite herself "
                "with Ximen Chuixue (ch09).",
    },
    "石秀雪": {
        "en": "Shi Xiuxue", "pinyin": "Shi Xiuxue", "status": "decided",
        "note": "The youngest of the Four Beauties of Emei; gentlest-seeming "
                "and hottest-tempered, she fights with a pair of short swords "
                "and dares, alone of the four, to love where she will. Hua "
                "Manlou catches her blades between two fingers, and she loses "
                "her heart to him (ch09).",
    },
}

organizations = {
    "峨嵋四秀": {
        "en": "the Four Beauties of Emei", "pinyin": "Emei Si Xiu",
        "status": "decided",
        "note": "The four young women disciples of the Emei sword-school "
                "(secretly headed by Dugu Yihe): Ma Xiuzhen, Sun Xiuqing, Ye "
                "Xiuzhu and Shi Xiuxue. Their given names all share the "
                "generation-character <i>xiu</i> (秀, &#8216;graceful, "
                "comely&#8217;), marking them as martial-sisters of one "
                "generation, whence &#8216;the Four Beauties&#8217; (四秀). "
                "They are the counterpart of the Three Heroes (三英) among the "
                "Seven Swords of Emei (ch09)."
    },
}

added = []
for sec, rows in (("people", people), ("organizations", organizations)):
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
