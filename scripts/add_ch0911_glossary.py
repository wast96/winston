#!/usr/bin/env python3
"""Add the ch09/10/11 glossary rows STRAIGHT INTO the people section (the
glossary.json is SECTIONED; apparatus_merge flattens it -- HANDOFF trap). en =
the Wade-Giles / conventional-English form Isaacs prints; pinyin = the modern
form, agreeing with authority.json where the shelf has settled one (孙科 Sun Ke,
顾孟余 Gu Mengyu, 宋庆龄 decided "Soong Ching-ling", 荣宗敬 Rong Zongjing; 徐谦 is
new to the shelf). Only Chinese figures go in the glossary; the batch's foreign
figures (Pilsudski, Malraux, Thaelmann, Duranty, Martynov, Anna Louise Strong)
stay in the notes, as Browder / Doriot / Mann did.

Also PROMOTES Chow En-lai to a principal (cast_order 6): he led the Shanghai
workers' insurrection (ch07) and escaped the April 12 coup (ch10), and is the
book's most recognizable recurring name after the first five principals -- the
standard courtesy to a Western reader who loses track of the cast. Idempotent;
re-reads glossary.json to verify.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GPATH = os.path.join(ROOT, "glossary.json")

PEOPLE = {
    "孙科": {"en": "Sun Fo", "pinyin": "Sun Ke", "status": "attested",
        "note": "1891&#8211;1973. Sun Yat-sen&#8217;s only son, American-educated "
        "and a former mayor of Canton; a leader of the Wuhan government in 1927 "
        "and later president of the Legislative Yuan."},
    "徐谦": {"en": "George Hsu-chien", "pinyin": "Xu Qian", "status": "attested",
        "note": "1871&#8211;1940. Christian and Western-trained jurist, twice "
        "minister of justice, and a left-Kuomintang leader at Wuhan; fled to "
        "Hong Kong after the Wuhan collapse."},
    "顾孟余": {"en": "Ku Meng-yu", "pinyin": "Gu Mengyu", "status": "attested",
        "note": "1889&#8211;1972. German-trained economist and Peking University "
        "dean who headed the Kuomintang&#8217;s propaganda department at Wuhan; "
        "backed Wang Ching-wei&#8217;s July 1927 break with the Communists."},
    "宋庆龄": {"en": "Soong Ching-ling", "pinyin": "Song Qingling",
        "status": "attested",
        "note": "1893&#8211;1981. Sun Yat-sen&#8217;s widow and a mainstay of the "
        "Kuomintang left; broke with Chiang&#8217;s Nanking regime and, long "
        "afterward, served as a vice-chair of the People&#8217;s Republic of "
        "China."},
    "荣宗敬": {"en": "Yung Chung-chin", "pinyin": "Rong Zongjing",
        "status": "attested",
        "note": "1873&#8211;1938. The cotton-and-flour magnate of Wusih and the "
        "foremost Chinese industrialist of the day; arrested by Chiang in 1927 "
        "for balking at a forced loan."},
}


def main():
    g = json.load(open(GPATH, encoding="utf-8"))
    added = 0
    sec = g.setdefault("people", {})
    for zh, row in PEOPLE.items():
        if zh in sec:
            continue
        sec[zh] = row
        added += 1

    # Promote Chow En-lai to a principal (cast_order 6); apply in place.
    chow = g["people"].get("周恩来")
    if chow is not None:
        chow["principal"] = True
        chow["cast_order"] = 6
        chow["cast"] = ("1898&#8211;1976. Communist organizer who led the "
            "Shanghai workers&#8217; insurrection of March 1927 and narrowly "
            "escaped Chiang&#8217;s April coup; later the first premier of the "
            "People&#8217;s Republic of China (1949&#8211;76).")

    with open(GPATH, "w", encoding="utf-8") as fh:
        json.dump(g, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    back = json.load(open(GPATH, encoding="utf-8"))
    for zh in PEOPLE:
        if zh not in back["people"]:
            raise SystemExit("re-read verification failed: %s" % zh)
    if not back["people"]["周恩来"].get("principal"):
        raise SystemExit("Chow promotion did not stick")
    print("glossary: %d rows added; people=%d; Chow principal=%s (order %s)"
          % (added, len(back["people"]),
             back["people"]["周恩来"]["principal"],
             back["people"]["周恩来"]["cast_order"]))


if __name__ == "__main__":
    main()
