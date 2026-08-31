#!/usr/bin/env python3
"""Add the ch18/19/20 glossary rows STRAIGHT INTO their sections (glossary.json
is SECTIONED; apparatus_merge flattens it -- HANDOFF trap). en = the Wade-Giles
/ conventional-English form Isaacs prints; pinyin = the modern form, agreeing
with authority.json where the shelf has settled one (朱德 Zhu De is already on
the shelf, single-book, same form). Only Chinese figures/terms go in the
glossary; the batch's foreign figures (von Seeckt, Leith-Ross, Manuilsky, Lord
Lytton) stay in the notes. Pu Yi (溥仪, en "Hsuan Tung") and Ho Ying-chin
(何应钦) already have rows and are not re-added.

No principal promotion this batch: Isaacs's 1938 book, ending in 1937-38, never
makes Chu Teh or Mao Tse-tung its central figure, and Mao is glossed as the
book's later shadow at ch00a. Principals stay Sun 1, Chiang 2, Chen Tu-hsiu 3,
Borodin 4, Wang Ching-wei 5, Chow En-lai 6, Chiu Chiu-pei 7.

Idempotent; re-reads glossary.json to verify.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GPATH = os.path.join(ROOT, "glossary.json")

PEOPLE = {
    "朱德": {"en": "Chu Teh", "pinyin": "Zhu De", "status": "attested",
        "note": "1886&#8211;1976. Former Yunnan-army officer who became "
        "commander-in-chief of the Red Army and Mao Tse-tung&#8217;s lifelong "
        "military partner from Chingkangshan (&#8220;Chu-Mao&#8221;); led the "
        "Eighth Route Army against Japan and, after 1949, was a marshal and head "
        "of state of the People&#8217;s Republic."},
    "彭德怀": {"en": "Peng Teh-huai", "pinyin": "Peng Dehuai",
        "status": "attested",
        "note": "1898&#8211;1974. One of the ablest Red commanders, later a "
        "marshal and China&#8217;s defense minister; disgraced in 1959 for "
        "challenging Mao over the Great Leap famine, he died persecuted in the "
        "Cultural Revolution."},
    "王明": {"en": "Wang Min", "pinyin": "Wang Ming", "status": "attested",
        "note": "1904&#8211;1974. Born Chen Shao-yu (陈绍禹). Led the "
        "Moscow-trained &#8220;Returned Students&#8221; (&#8220;Twenty-Eight "
        "Bolsheviks&#8221;) installed atop the party in 1931 under Pavel "
        "Mif&#8217;s patronage; the Comintern&#8217;s man and later Mao "
        "Tse-tung&#8217;s chief rival, he was pushed aside in the war years and "
        "died in exile in Moscow."},
    "方志敏": {"en": "Fang Chih-min", "pinyin": "Fang Zhimin",
        "status": "attested",
        "note": "1899&#8211;1935. Built the soviet base in northeastern Kiangsi; "
        "captured during the 1934&#8211;35 breakout and executed by the "
        "Nationalists, remembered for the essays he wrote in prison."},
    "张闻天": {"en": "Lo Fu", "pinyin": "Zhang Wentian", "status": "attested",
        "note": "1900&#8211;1976. Pen name Lo Fu. One of the Moscow-trained "
        "leaders; became the party&#8217;s general secretary in 1935 and later a "
        "senior diplomat, purged with Peng Teh-huai in 1959."},
    "孔祥熙": {"en": "H. H. Kung", "pinyin": "Kong Xiangxi", "status": "attested",
        "note": "1881&#8211;1967. Banker reputed to descend from Confucius and "
        "married to a sister of Madame Chiang Kai-shek; Nationalist finance "
        "minister and premier for much of the 1930s and 1940s."},
    "王正廷": {"en": "C. T. Wang", "pinyin": "Wang Zhengting", "status": "attested",
        "note": "1882&#8211;1961. Veteran diplomat and foreign minister, beaten "
        "by nationalist students in 1931 over non-resistance to Japan; later "
        "ambassador to Washington."},
    "顾维钧": {"en": "Wellington Koo", "pinyin": "Gu Weijun", "status": "attested",
        "note": "1888&#8211;1985. China&#8217;s most eminent modern diplomat: its "
        "spokesman at the 1919 Paris Peace Conference, ambassador to Paris, "
        "London, and Washington, and afterward a judge of the International Court "
        "of Justice."},
    "陈济棠": {"en": "Chen Chi-tang", "pinyin": "Chen Jitang", "status": "attested",
        "note": "1890&#8211;1954. Militarist master of Kwangtung, a "
        "semi-independent southern warlord whom Chiang Kai-shek finally brought "
        "to heel in 1936."},
    "李宗仁": {"en": "Li Tsung-jen", "pinyin": "Li Zongren", "status": "attested",
        "note": "1890&#8211;1969. Leading man of the Kwangsi clique (with Pai "
        "Chung-hsi); a semi-independent southwestern commander later acting "
        "president of the Republic in 1949."},
}

ORGANIZATIONS = {
    "中华苏维埃共和国": {"en": "Chinese Soviet Republic",
        "pinyin": "Zhonghua Suweiai Gongheguo", "status": "attested",
        "note": "The federation of rural soviet base areas proclaimed at Juichin "
        "(Ruijin) in Kiangsi on November 7, 1931, with Mao Tse-tung as chairman; "
        "broken by Chiang&#8217;s fifth campaign and abandoned in the retreat of "
        "1934."},
    "八路军": {"en": "Eighth Route Army", "pinyin": "Balujun",
        "status": "attested",
        "note": "The name under which the Red Army was folded into the "
        "Nationalist forces in September 1937 for the war with Japan; under Chu "
        "Teh&#8217;s command the main Communist force in the north."},
    "十九路军": {"en": "Nineteenth Route Army", "pinyin": "Shijiu Lujun",
        "status": "attested",
        "note": "Cantonese army (Isaacs also writes &#8220;19th Route Army&#8221;) "
        "whose defense of Shanghai against Japan in early 1932 defied "
        "Chiang&#8217;s non-resistance; it joined the Fukien revolt of 1933 and "
        "was then broken up."},
    "救国会": {"en": "National Salvation Association", "pinyin": "Jiuguohui",
        "status": "attested",
        "note": "The broad patriotic movement of the mid-1930s pressing for a "
        "united front against Japan; Nanking jailed seven of its leaders (the "
        "&#8220;Seven Gentlemen&#8221;) in November 1936."},
}

PLACES = {
    "满洲国": {"en": "Manchukuo", "pinyin": "Manzhouguo", "status": "attested",
        "note": "The puppet state Japan proclaimed in the three northeastern "
        "provinces in 1932, with the deposed last Qing emperor (Pu Yi) as "
        "figurehead; recognized by almost no one and dissolved in 1945."},
}

TERMS = {
    "红胡子": {"en": "hunghutze", "pinyin": "honghuzi", "status": "attested",
        "note": "&#8220;Red beards&#8221; &#8212; the traditional armed bandit "
        "bands of Manchuria (Isaacs spells it &#8220;hunghudtze&#8221;); many "
        "turned to anti-Japanese guerrilla resistance after 1931."},
}


def main():
    g = json.load(open(GPATH, encoding="utf-8"))
    added = 0
    for secname, rows in (("people", PEOPLE), ("organizations", ORGANIZATIONS),
                          ("places", PLACES), ("terms", TERMS)):
        sec = g.setdefault(secname, {})
        for zh, row in rows.items():
            if zh in sec:
                continue
            sec[zh] = row
            added += 1

    with open(GPATH, "w", encoding="utf-8") as fh:
        json.dump(g, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    back = json.load(open(GPATH, encoding="utf-8"))
    for secname, rows in (("people", PEOPLE), ("organizations", ORGANIZATIONS),
                          ("places", PLACES), ("terms", TERMS)):
        for zh in rows:
            if zh not in back[secname]:
                raise SystemExit("re-read verification failed: %s/%s"
                                 % (secname, zh))
    print("glossary: %d rows added (people=%d org=%d places=%d terms=%d)"
          % (added, len(back["people"]), len(back["organizations"]),
             len(back["places"]), len(back["terms"])))


if __name__ == "__main__":
    main()
