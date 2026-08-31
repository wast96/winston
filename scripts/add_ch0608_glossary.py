#!/usr/bin/env python3
"""Add the ch06/07/08 glossary rows STRAIGHT INTO their sections (people /
organizations); the glossary.json is SECTIONED and apparatus_merge flattens it
(HANDOFF trap). en = the Wade-Giles / conventional-English form Isaacs prints
in the body; pinyin = the modern form (agreeing with authority.json where the
shelf has settled one); status attested. Also PROMOTES Wang Ching-wei to
principal (cast_order 5): the narrative of ch06-08 turns increasingly on him
(his April 1, 1927 return and the Chiang-Wang manoeuvres). Idempotent: a hanzi
key already present is left as is except for the Wang promotion, which is
applied in place. Re-reads glossary.json afterward to verify.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GPATH = os.path.join(ROOT, "glossary.json")

PEOPLE = {
    "唐生智": {"en": "Tang Sheng-chih", "pinyin": "Tang Shengzhi",
        "status": "attested",
        "note": "1889&#8211;1970. Hunan general who joined the Northern "
        "Expedition, governed the province, and became a military mainstay of "
        "the Wuhan government; later held office under the People&#8217;s "
        "Republic."},
    "孙传芳": {"en": "Sun Chuang-fang", "pinyin": "Sun Chuanfang",
        "status": "attested",
        "note": "1885&#8211;1935. Warlord of a five-province league in the "
        "lower Yangtze; broken by the Northern Expedition and assassinated at "
        "Tientsin in 1935."},
    "周恩来": {"en": "Chow En-lai", "pinyin": "Zhou Enlai", "status": "attested",
        "note": "1898&#8211;1976. Communist organizer of the Shanghai workers&#8217; "
        "risings of 1927; later the first premier of the People&#8217;s Republic "
        "of China (1949&#8211;76)."},
    "瞿秋白": {"en": "Chiu Chiu-pei", "pinyin": "Qu Qiubai", "status": "attested",
        "note": "1899&#8211;1935. Writer and Communist leader who succeeded Chen "
        "Tu-hsiu at the head of the party in August 1927; executed by the "
        "Nationalists in 1935."},
    "谭平山": {"en": "Tang Ping-shan", "pinyin": "Tan Pingshan",
        "status": "attested",
        "note": "1886&#8211;1956. Founder of the Chinese Communist Party and "
        "its senior figure inside the Kuomintang; minister of agriculture at "
        "Wuhan in 1927, later a founder of the &#8220;Third Party.&#8221;"},
    "张宗昌": {"en": "Chang Tsung-chang", "pinyin": "Zhang Zongchang",
        "status": "attested",
        "note": "1881&#8211;1932. The &#8220;Dogmeat General,&#8221; rapacious "
        "warlord of Shantung with a White Russian mercenary corps; "
        "assassinated at Tsinan in 1932."},
    "白崇禧": {"en": "Pai Chung-hsi", "pinyin": "Bai Chongxi",
        "status": "attested",
        "note": "1893&#8211;1966. Muslim general of the Kwangsi clique and chief "
        "of staff of the Northern Expedition; took Shanghai for Chiang and "
        "later a Nationalist defense minister on Taiwan."},
    "何应钦": {"en": "Ho Ying-chin", "pinyin": "He Yingqin", "status": "attested",
        "note": "1890&#8211;1987. Senior and loyal general of Chiang Kai-shek, "
        "a fellow student in Japan; later Nationalist minister of war and "
        "briefly premier."},
    "钮永建": {"en": "Niu Yung-chien", "pinyin": "Niu Yongjian",
        "status": "attested",
        "note": "Veteran Kuomintang operative and Chiang Kai-shek&#8217;s chief "
        "agent in Shanghai, holding a mandate from party headquarters at "
        "Canton."},
    "吴稚晖": {"en": "Wu Chih-hui", "pinyin": "Wu Zhihui", "status": "attested",
        "note": "1865&#8211;1953. Anarchist turned Kuomintang elder, essayist "
        "and calligrapher, one of the party&#8217;s anti-Communist &#8220;four "
        "elders&#8221;; moved the April 1927 resolution sanctioning the purge."},
    "蔡元培": {"en": "Tsai Yuan-pei", "pinyin": "Cai Yuanpei", "status": "attested",
        "note": "1868&#8211;1940. Eminent educator, chancellor of Peking "
        "University in the May Fourth era and founder of the Academia Sinica; "
        "one of the Kuomintang&#8217;s &#8220;four elders.&#8221;"},
    "杜月笙": {"en": "Tu Yueh-sen", "pinyin": "Du Yuesheng", "status": "attested",
        "note": "1888&#8211;1951. Foremost boss of the Shanghai Green Gang; a "
        "chief organizer of the April 1927 slaughter of the Communists."},
    "黄金荣": {"en": "Hwang Ching-yung", "pinyin": "Huang Jinrong",
        "status": "attested",
        "note": "1868&#8211;1953. Green Gang chief and detective in the French "
        "Concession police; &#8220;Pock-marked Hwang,&#8221; reputed to have "
        "sponsored Chiang&#8217;s early gang initiation."},
    "张啸林": {"en": "Chang Siao-ling", "pinyin": "Zhang Xiaolin",
        "status": "attested",
        "note": "1877&#8211;1940. One of the three Green Gang bosses of "
        "Shanghai; later a collaborator with the Japanese, by whom he was "
        "assassinated."},
    "李宝章": {"en": "Li Pao-chang", "pinyin": "Li Baozhang", "status": "attested",
        "note": "Commander of the Shanghai garrison for the warlord Sun "
        "Chuang-fang; ran the white terror against the workers in early 1927 "
        "before defecting to Chiang Kai-shek."},
    "米夫": {"en": "P. Mif", "pinyin": "Pavel Mif", "status": "attested",
        "note": "1901&#8211;1939 (pseudonym of M. A. Fortus). Soviet China "
        "specialist and rector of the Sun Yat-sen University in Moscow; "
        "Stalin&#8217;s instrument in the Chinese party. Shot in the purges."},
}

ORGANIZATIONS = {
    "商务印书馆": {"en": "Commercial Press", "pinyin": "Shangwu Yinshuguan",
        "status": "attested",
        "note": "Founded in Shanghai in 1897, China&#8217;s largest publishing "
        "house and a landmark of the Chapei district; its workforce made it a "
        "labor stronghold and, in the 1927 rising, a fortified strongpoint."},
    "字林西报": {"en": "North China Daily News", "pinyin": "Zilin Xibao",
        "status": "attested",
        "note": "The leading British newspaper in China, published in Shanghai; "
        "the recognized organ of foreign settler opinion at its most "
        "die-hard."},
}


def main():
    g = json.load(open(GPATH, encoding="utf-8"))
    added = 0
    for section, rows in (("people", PEOPLE), ("organizations", ORGANIZATIONS)):
        sec = g.setdefault(section, {})
        for zh, row in rows.items():
            if zh in sec:
                continue
            sec[zh] = row
            added += 1

    # Promote Wang Ching-wei to a principal (cast_order 5); apply in place.
    wang = g["people"].get("汪精卫")
    if wang is not None:
        wang["principal"] = True
        wang["cast_order"] = 5
        wang["cast"] = ("1883&#8211;1944. Leader of the Kuomintang left and "
            "Chiang&#8217;s chief rival for Sun&#8217;s mantle; headed the "
            "Wuhan (&#8220;Left&#8221;) government in 1927, whose break with "
            "the Communists this book recounts, and in 1940 became head of the "
            "Japanese-sponsored government at Nanking.")

    with open(GPATH, "w", encoding="utf-8") as fh:
        json.dump(g, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    back = json.load(open(GPATH, encoding="utf-8"))
    for section, rows in (("people", PEOPLE), ("organizations", ORGANIZATIONS)):
        for zh in rows:
            if zh not in back[section]:
                raise SystemExit("re-read verification failed: %s" % zh)
    if not back["people"]["汪精卫"].get("principal"):
        raise SystemExit("Wang promotion did not stick")
    print("glossary: %d rows added; people=%d organizations=%d; Wang principal=%s (order %s)"
          % (added, len(back["people"]), len(back["organizations"]),
             back["people"]["汪精卫"]["principal"],
             back["people"]["汪精卫"]["cast_order"]))


if __name__ == "__main__":
    main()
