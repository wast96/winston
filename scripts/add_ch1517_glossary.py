#!/usr/bin/env python3
"""Add the ch15/16/17 glossary rows STRAIGHT INTO the people section (the
glossary.json is SECTIONED; apparatus_merge flattens it -- HANDOFF trap), and
PROMOTE Chiu Chiu-pei (Qu Qiubai) to principal, cast_order 7. en = the
Wade-Giles / conventional-English form Isaacs prints; pinyin = the modern form,
agreeing with authority.json where the shelf has settled one (张学良 Zhang
Xueliang, 李立三 Li Lisan, 贺龙 He Long are "agreed"; 张发奎 Zhang Fakui is
single-book but the same form; 张太雷 Zhang Tailei is NEW to the shelf -- record
it in authority.json on the final batch). Only Chinese figures go in the
glossary; the batch's foreign figures (Heinz Neumann, Lominadze, Galliffet)
stay in the notes, as Browder / Malraux / Pilsudski did.

PRINCIPAL PROMOTION: Chiu Chiu-pei (Qu Qiubai) succeeds Chen Tu-hsiu at the head
of the party at the August 7, 1927 conference (ch16). His existing 瞿秋白 row
already records the succession; this sets principal true, cast_order 7, and adds
the cast one-liner for the Principal Characters page. Principals now: Sun 1,
Chiang 2, Chen Tu-hsiu 3, Borodin 4, Wang Ching-wei 5, Chow En-lai 6, Chiu
Chiu-pei 7. Idempotent; re-reads glossary.json to verify.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GPATH = os.path.join(ROOT, "glossary.json")

PEOPLE = {
    "张学良": {"en": "Chang Hsueh-liang", "pinyin": "Zhang Xueliang",
        "status": "attested",
        "note": "1901&#8211;2001. The &#8220;Young Marshal,&#8221; who succeeded "
        "his father Chang Tso-lin in Manchuria in 1928 and in December 1936 "
        "seized Chiang Kai-shek at Sian to force a united front against Japan, "
        "then spent most of the next half-century under house arrest."},
    "张发奎": {"en": "Chang Fah-kwei", "pinyin": "Zhang Fakui",
        "status": "attested",
        "note": "1896&#8211;1980. Commander of the Fourth &#8220;Ironsides&#8221; "
        "Army; his 1927 rivalry with Li Chi-sen over the control of Canton opened "
        "the split the Communists tried to use in the December rising."},
    "李立三": {"en": "Li Li-san", "pinyin": "Li Lisan", "status": "attested",
        "note": "1899&#8211;1967. Labor organizer and leader of the Chinese "
        "Communist Party in 1928&#8211;30; the &#8220;Li Lisan line&#8221; of "
        "1930 urban insurrections ended in defeat and his removal."},
    "贺龙": {"en": "Ho Lung", "pinyin": "He Long", "status": "attested",
        "note": "1896&#8211;1969. Former bandit chief turned Nationalist "
        "commander who brought his army over to the Communists at the Nanchang "
        "uprising; one of the ten marshals of the People&#8217;s Liberation Army "
        "(1955), he died persecuted in the Cultural Revolution."},
    "张太雷": {"en": "Chang Tai-lei", "pinyin": "Zhang Tailei",
        "status": "attested",
        "note": "1898&#8211;1927. A founder of the Communist Youth League who led "
        "the Canton Commune of December 1927 and was killed in it &#8212; the "
        "highest-ranking Communist to die in the risings of 1927."},
}

# Chiu Chiu-pei promotion (existing 瞿秋白 row): add these fields.
CHIU_ZH = "瞿秋白"
CHIU_CAST = ("1899&#8211;1935. Writer and translator who succeeded Chen Tu-hsiu "
             "at the head of the Chinese Communist Party at the August 7, 1927 "
             "conference and led its turn to armed insurrection; captured and "
             "executed by the Nationalists in 1935.")


def main():
    g = json.load(open(GPATH, encoding="utf-8"))
    sec = g.setdefault("people", {})
    added = 0
    for zh, row in PEOPLE.items():
        if zh in sec:
            continue
        sec[zh] = row
        added += 1

    # Promote Chiu Chiu-pei to principal, cast_order 7.
    chiu = sec.get(CHIU_ZH)
    if chiu is None:
        raise SystemExit("Chiu Chiu-pei row %s missing" % CHIU_ZH)
    promoted = not chiu.get("principal")
    chiu["principal"] = True
    chiu["cast_order"] = 7
    chiu["cast"] = CHIU_CAST

    with open(GPATH, "w", encoding="utf-8") as fh:
        json.dump(g, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    back = json.load(open(GPATH, encoding="utf-8"))
    for zh in PEOPLE:
        if zh not in back["people"]:
            raise SystemExit("re-read verification failed: %s" % zh)
    b_chiu = back["people"][CHIU_ZH]
    if not (b_chiu.get("principal") and b_chiu.get("cast_order") == 7):
        raise SystemExit("Chiu promotion not persisted")
    principals = sorted((v["cast_order"], v["en"])
                        for v in back["people"].values() if v.get("principal"))
    print("glossary: %d rows added; Chiu promoted=%s; people=%d"
          % (added, promoted, len(back["people"])))
    print("principals:", principals)


if __name__ == "__main__":
    main()
