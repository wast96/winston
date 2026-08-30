#!/usr/bin/env python3
"""Add the ch04/ch05 glossary rows STRAIGHT INTO their sections (people /
organizations / places). The book's glossary.json is SECTIONED; apparatus_merge
flattens it, so glossary rows are added here instead (HANDOFF trap note). en =
the Wade-Giles / conventional-English form Isaacs prints in the body; pinyin =
the modern form (agreeing with authority.json where the shelf has settled one);
status attested. Idempotent: a hanzi key already present is left untouched.
Re-reads glossary.json afterward to verify.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GPATH = os.path.join(ROOT, "glossary.json")

PEOPLE = {
    "胡汉民": {"en": "Hu Han-min", "pinyin": "Hu Hanmin", "status": "attested",
        "note": "1879&#8211;1936. Senior Kuomintang leader and rival of Chiang "
        "for Sun&#8217;s mantle; sent to Moscow in 1925 after the murder of "
        "Liao Chung-kai, later leader of the party right."},
    "戴季陶": {"en": "Tai Chi-tao", "pinyin": "Dai Jitao", "status": "attested",
        "note": "1891&#8211;1949. Chief ideologist of the Kuomintang right; his "
        "anti-Communist &#8220;Sun Yat-senism&#8221; gave the reaction its "
        "doctrine."},
    "张静江": {"en": "Chang Ching-chiang", "pinyin": "Zhang Jingjiang",
        "status": "attested",
        "note": "1877&#8211;1950. Financier, bankroller of Sun&#8217;s "
        "revolution and Chiang&#8217;s patron and mentor; briefly chairman of "
        "the Kuomintang Central Executive Committee."},
    "陈其美": {"en": "Chen Chi-mei", "pinyin": "Chen Qimei", "status": "attested",
        "note": "1878&#8211;1916. Revolutionary ally of Sun, military governor "
        "of Shanghai after 1911, and Chiang&#8217;s early patron; assassinated "
        "in 1916."},
    "虞洽卿": {"en": "Yu Ya-ching", "pinyin": "Yu Qiaqing", "status": "attested",
        "note": "1867&#8211;1945. Leading Shanghai comprador-banker and shipping "
        "magnate; a financial backer of Chiang Kai-shek."},
    "冯玉祥": {"en": "Feng Yu-hsiang", "pinyin": "Feng Yuxiang",
        "status": "attested",
        "note": "1882&#8211;1948. The &#8220;Christian General,&#8221; warlord "
        "of the Kuominchun in the northwest; joined the Kuomintang and the "
        "Northern Expedition in 1926."},
    "郭松龄": {"en": "Kuo Sung-lin", "pinyin": "Guo Songling",
        "status": "attested",
        "note": "1883&#8211;1925. General under Chang Tso-lin who mutinied "
        "against him in November 1925 and was captured and shot."},
    "邓演达": {"en": "Teng Yen-ta", "pinyin": "Deng Yanda", "status": "attested",
        "note": "1895&#8211;1931. Left-wing Kuomintang leader and Whampoa "
        "political director; broke with Chiang and was executed in 1931."},
    "李济深": {"en": "Li Chi-sen", "pinyin": "Li Jishen", "status": "attested",
        "note": "1885&#8211;1959. Kwangsi-linked general who ruled Kwangtung "
        "after the government moved north; later a vice-chairman of the "
        "People&#8217;s Republic."},
    "陈友仁": {"en": "Eugene Chen", "pinyin": "Chen Youren", "status": "attested",
        "note": "1878&#8211;1944. Trinidad-born lawyer and Nationalist foreign "
        "minister; chief spokesman of the Wuhan government in 1927."},
    "伍朝枢": {"en": "C. C. Wu", "pinyin": "Wu Chaoshu", "status": "attested",
        "note": "1887&#8211;1934. Nationalist foreign minister at Canton and "
        "later ambassador to the United States; son of the diplomat Wu "
        "Ting-fang."},
    "许崇智": {"en": "Hsu Chung-shih", "pinyin": "Xu Chongzhi",
        "status": "attested",
        "note": "1886&#8211;1965. Commander of the Cantonese Army; implicated "
        "in the 1925 murder of Liao Chung-kai and driven from Canton, clearing "
        "a military rival from Chiang&#8217;s path."},
    "高语罕": {"en": "Kao Yu-han", "pinyin": "Gao Yuhan", "status": "attested",
        "note": "1888&#8211;1948. Communist and member of the Kuomintang "
        "Supervisory Committee; the &#8220;Tuan Chi-jui&#8221; remark quoted "
        "here was his."},
    "李之龙": {"en": "Li Chih-lung", "pinyin": "Li Zhilong", "status": "attested",
        "note": "1897&#8211;1928. Communist head of the Canton Naval Bureau and "
        "nominal object of the March 20 coup; executed by the Nationalists in "
        "1928."},
    "段祺瑞": {"en": "Tuan Chi-jui", "pinyin": "Duan Qirui", "status": "attested",
        "note": "1865&#8211;1936. Peiyang militarist and head of the Peking "
        "government whose troops carried out the March 18, 1926, massacre."},
}

ORGANIZATIONS = {
    "西山会议派": {"en": "Western Hills Conference group",
        "pinyin": "Xishan huiyi pai", "status": "attested",
        "note": "The right-wing Kuomintang faction that met in the Western "
        "Hills outside Peking in November 1925 to demand expulsion of the "
        "Communists and dismissal of Borodin."},
    "孙文主义学会": {"en": "Sun Yat-senist Society",
        "pinyin": "Sun Wen zhuyi xuehui", "status": "attested",
        "note": "A right-wing anti-Communist body of 1925, strong among the "
        "Whampoa cadets, that claimed to defend Sun&#8217;s doctrine against "
        "Communist influence."},
    "青帮": {"en": "Green Circle", "pinyin": "Qing Bang", "status": "attested",
        "note": "Isaacs&#8217;s name for the Green Gang, Shanghai&#8217;s "
        "dominant secret society, controlling opium, gambling, and labor "
        "rackets; the instrument of the April 1927 purge."},
}

PLACES = {
    "青岛": {"en": "Tsingtao", "pinyin": "Qingdao", "status": "attested",
        "note": "Port and former German leasehold in Shantung, seized by Japan "
        "in 1914; a center of the 1925 strike wave."},
}


def main():
    g = json.load(open(GPATH, encoding="utf-8"))
    added = 0
    for section, rows in (("people", PEOPLE), ("organizations", ORGANIZATIONS),
                          ("places", PLACES)):
        sec = g.setdefault(section, {})
        for zh, row in rows.items():
            if zh in sec:
                continue
            sec[zh] = row
            added += 1
    with open(GPATH, "w", encoding="utf-8") as fh:
        json.dump(g, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    back = json.load(open(GPATH, encoding="utf-8"))
    for section, rows in (("people", PEOPLE), ("organizations", ORGANIZATIONS),
                          ("places", PLACES)):
        for zh in rows:
            if zh not in back[section]:
                raise SystemExit("re-read verification failed: %s" % zh)
    print("glossary: %d rows added; people=%d organizations=%d places=%d"
          % (added, len(back["people"]), len(back["organizations"]),
             len(back["places"])))


if __name__ == "__main__":
    main()
