#!/usr/bin/env python3
"""Add B05 glossary rows under the correct two-level sections (NOT flat).
Idempotent: skips a key already present. Run once; validate with
check_apparatus.py."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(ROOT, "glossary.json")
g = json.load(open(path, encoding="utf-8"))

A = "&#8217;"  # curly apostrophe, matching the existing notes' typography

people = {
    "苏少卿": {
        "en": "Su Shaoqing", "pinyin": "Su Shaoqing", "status": "decided",
        "note": "The name under which Su Shaoying passes himself off as the "
                "Yan household%ss resident tutor and man of letters (ch07)." % A,
    },
    "苏少英": {
        "en": "Su Shaoying", "pinyin": "Su Shaoying", "status": "decided",
        "note": "Su the Second of the Three Heroes and Four Beauties of Emei "
                "(峨嵋三英四秀); a disciple of Dugu Yihe. His self-made "
                "Saber-and-Sword Double Kill could not save him from Ximen "
                "Chuixue%ss blade (ch07)." % A,
    },
    "马行空": {
        "en": "Ma Xingkong", "pinyin": "Ma Xingkong", "status": "decided",
        "note": "Chief armsman of the Allied Escort Houses of Guanzhong, "
                "styled the Divine Dragon in the Clouds. An old wound from "
                "Huo Tianqing%ss palm halved his skill, so he leans on the "
                "Pavilion of Pearls and Splendour (ch07)." % A,
    },
    "山西雁": {
        "en": "the Shanxi Wild Goose", "pinyin": "Shanxi Yan",
        "status": "decided",
        "note": "The great hero of Guanzhong, famed near forty years for his "
                "twin iron palms; by martial generation the nephew of Huo "
                "Tianqing, though decades his elder. One of the Heaven%ss "
                "Bird sect (ch08)." % A,
    },
    "司空摘星": {
        "en": "Sikong Zhaixing", "pinyin": "Sikong Zhaixing",
        "status": "decided",
        "note": "The king of thieves, who steals only on a wager and never "
                "what is truly valuable; being robbed by him is counted an "
                "honour. He once matched Lu Xiaofeng at somersaults on the "
                "summit of Mount Tai, and takes the likeness of Zhao the "
                "Pockmarked in ch08.",
    },
    "樊鹗": {
        "en": "Fan E", "pinyin": "Fan E", "status": "decided",
        "note": "Master Fan the Elder, one of the Two Talents of the "
                "Northwest (西北双秀); his long tobacco-pipe strikes the "
                "body%ss pressure-points. One of the Seven Heroes of the "
                "Marketplace (ch08)." % A,
    },
    "简二先生": {
        "en": "Master Jian the Second", "pinyin": "Jian Er Xiansheng",
        "status": "decided",
        "note": "The other of the Two Talents of the Northwest, sole heir to "
                "the Finger-Flicking art (弹指神通). One of the Seven Heroes "
                "of the Marketplace (ch08).",
    },
    "赵大麻子": {
        "en": "Zhao the Pockmarked", "pinyin": "Zhao Damazi",
        "status": "decided",
        "note": "The dog-meat cook of the tavern called Yet Another Village, "
                "outside the town; his stew has no equal. Sikong Zhaixing "
                "wears his face in ch08.",
    },
    "商山二老": {
        "en": "the Two Elders of Mount Shang", "pinyin": "Shangshan Er Lao",
        "status": "decided",
        "note": "Two aged and revered masters of the Heaven%ss Bird sect, "
                "reckoned the polestar of the martial world; Huo Tianqing is "
                "their junior martial-brother (ch08)." % A,
    },
    "天禽老人": {
        "en": "the Old Man of Heaven's Birds", "pinyin": "Tianqin Laoren",
        "status": "decided",
        "note": "Founder of the Heaven%ss Bird sect sixty years ago; he took "
                "a wife and got an heir only at seventy-seven, and that heir "
                "is Huo Tianqing (ch08)." % A,
    },
}

organizations = {
    "天禽门": {
        "en": "the Heaven's Bird sect", "pinyin": "Tianqin Men",
        "status": "decided",
        "note": "The school founded by the Old Man of Heaven%ss Birds; Huo "
                "Tianqing is its sole bloodline heir, so its several hundred "
                "disciples would die to a man before they let harm come to "
                "him (ch08)." % A,
    },
    "市井七侠": {
        "en": "the Seven Heroes of the Marketplace", "pinyin": "Shijing Qi Xia",
        "status": "decided",
        "note": "Seven sworn brothers who go disguised as street pedlars "
                "(a bun-seller, a quack, a pockmarked innkeeper and the "
                "rest), also called the Seven Righteous of Shanxi (山西七义); "
                "all of the Heaven%ss Bird sect (ch08)." % A,
    },
}

places = {
    "泰山": {
        "en": "Mount Tai", "pinyin": "Taishan", "status": "decided",
        "note": "The easternmost and most venerated of China%ss five sacred "
                "peaks, in Shandong; watching the sunrise from its summit is "
                "an old pilgrimage (ch07)." % A,
    },
}

added = []
for sec, rows in (("people", people), ("organizations", organizations),
                  ("places", places)):
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
