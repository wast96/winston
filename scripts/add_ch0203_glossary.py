#!/usr/bin/env python3
"""Add ch02/ch03 glossary rows straight into their SECTIONS (people /
organizations / places / terms), preserving the sectioned structure that the
builder's render_glossary and Principal Characters page require. NOT via
apparatus_merge, which flattens rows to the top level (HANDOFF trap). Rows are
added only if the hanzi key is absent; existing rows are left untouched.
Pinyin forms agree with authority.json. Re-reads and reports after writing.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOSS = os.path.join(ROOT, "glossary.json")

ADD = {
    "people": {
        "陈独秀": {"en": "Chen Tu-hsiu", "pinyin": "Chen Duxiu",
                   "status": "attested", "principal": True, "cast_order": 3,
                   "cast": "1879&#8211;1942. Co-founder and first leader of the "
                   "Chinese Communist Party; made to carry the blame for the "
                   "1927 defeat, expelled in 1929, and thereafter a Trotskyist.",
                   "note": "1879&#8211;1942. Leader of the New Culture and May "
                   "Fourth movements; co-founder and first general secretary of "
                   "the CCP; scapegoated for the 1927 disaster, expelled in "
                   "1929, and later a follower of Trotsky."},
        "鲍罗廷": {"en": "Borodin", "pinyin": "Bao Luoting",
                   "status": "attested", "principal": True, "cast_order": 4,
                   "cast": "1884&#8211;1951. Chief Soviet (Comintern) adviser to "
                   "the Kuomintang, 1923&#8211;27; architect of its "
                   "reorganization and of the united front whose collapse this "
                   "book recounts.",
                   "note": "Mikhail Borodin (1884&#8211;1951), the chief Comintern "
                   "adviser to the Kuomintang from 1923; recalled to Moscow after "
                   "1927 and died in a Soviet labor camp. Isaacs keeps his "
                   "working name, Borodin."},
        "陈翰笙": {"en": "Chen Han-seng", "pinyin": "Chen Hansheng",
                   "status": "attested",
                   "note": "1897&#8211;2004. Marxist economist whose village "
                   "surveys of the 1920s&#8211;30s Isaacs draws on for his "
                   "picture of the agrarian crisis."},
        "李大钊": {"en": "Li Ta-chao", "pinyin": "Li Dazhao",
                   "status": "attested",
                   "note": "1889&#8211;1927. Co-founder of the CCP; Peking "
                   "University librarian; hanged by the warlord Chang Tso-lin in "
                   "1927."},
        "张国焘": {"en": "Chang Kuo-tao", "pinyin": "Zhang Guotao",
                   "status": "attested",
                   "note": "1897&#8211;1979. A founding Communist, later a rival "
                   "of Mao; defected to the Kuomintang in 1938."},
        "陈炯明": {"en": "Chen Chiung-ming", "pinyin": "Chen Jiongming",
                   "status": "attested",
                   "note": "1878&#8211;1933. Cantonese general who gave Sun "
                   "Yat-sen a base and then drove him from Canton in 1922; "
                   "expelled from Kwangtung in 1925."},
        "廖仲恺": {"en": "Liao Chung-kai", "pinyin": "Liao Zhongkai",
                   "status": "attested",
                   "note": "1877&#8211;1925. The most left-wing of Sun&#8217;s "
                   "aides and a champion of the Soviet alliance; assassinated by "
                   "Kuomintang rightists in 1925."},
        "吴佩孚": {"en": "Wu Pei-fu", "pinyin": "Wu Peifu",
                   "status": "attested",
                   "note": "1874&#8211;1939. Dominant militarist of North China "
                   "in the early 1920s; ordered the February 1923 massacre of "
                   "the Peking&#8211;Hankow railway strikers."},
        "彭湃": {"en": "Peng Pai", "pinyin": "Peng Pai",
                  "status": "attested",
                  "note": "1896&#8211;1929. Organizer of China&#8217;s first "
                  "mass peasant associations, at Haifeng; shot by the Kuomintang "
                  "in 1929."},
        "汪精卫": {"en": "Wang Ching-wei", "pinyin": "Wang Jingwei",
                   "status": "attested",
                   "note": "1883&#8211;1944. Leader of the Kuomintang left and "
                   "Chiang&#8217;s rival; headed the Wuhan government in 1927 and "
                   "later the Japanese puppet regime at Nanking (1940&#8211;44)."},
        "陈廉伯": {"en": "Chen Lim-pak", "pinyin": "Chen Lianbo",
                   "status": "attested",
                   "note": "Compradore of the Hongkong and Shanghai Banking "
                   "Corporation who financed the Canton Merchants&#8217; "
                   "Volunteers against the Kuomintang in 1924."},
        "杨希闵": {"en": "Yang Hsi-min", "pinyin": "Yang Ximin",
                   "status": "attested",
                   "note": "Yunnanese general whose mercenary army held Canton "
                   "until routed by the Kuomintang in 1925."},
        "刘震寰": {"en": "Liu Chen-han", "pinyin": "Liu Zhenhuan",
                   "status": "attested",
                   "note": "Kwangsi general allied with Yang Hsi-min in Canton; "
                   "expelled with him in 1925."},
    },
    "organizations": {
        "新青年": {"en": "New Youth", "pinyin": "Xin Qingnian",
                   "status": "attested",
                   "note": "The magazine Chen Tu-hsiu founded in 1915, central "
                   "organ of the New Culture Movement."},
        "黄埔军校": {"en": "Whampoa Military Academy", "pinyin": "Huangpu Junxiao",
                     "status": "attested",
                     "note": "The Nationalist officers&#8217; school founded near "
                     "Canton in 1924 with Soviet aid; Chiang Kai-shek&#8217;s "
                     "power base."},
        "商团": {"en": "Merchants&#8217; Volunteers", "pinyin": "Shangtuan",
                 "status": "attested",
                 "note": "The British-backed Canton merchant militia crushed by "
                 "the Kuomintang in 1924."},
        "安福系": {"en": "Anfu clique", "pinyin": "Anfu xi",
                   "status": "attested",
                   "note": "The pro-Japanese faction that controlled the Peking "
                   "government in 1918&#8211;20."},
        "第二国际": {"en": "Second International", "pinyin": "Di&#8217;er Guoji",
                     "status": "attested",
                     "note": "The pre-1914 federation of socialist parties, whose "
                     "collapse into wartime nationalism prompted the founding of "
                     "the Comintern."},
    },
    "places": {
        "山东": {"en": "Shantung", "pinyin": "Shandong",
                 "status": "attested",
                 "note": "The eastern coastal province whose former German "
                 "concessions were handed to Japan at Versailles, touching off "
                 "the May Fourth movement."},
        "海丰": {"en": "Haifeng", "pinyin": "Haifeng",
                 "status": "attested",
                 "note": "District in eastern Kwangtung; cradle of Peng Pai&#8217;s "
                 "peasant movement."},
        "沙面": {"en": "Shameen", "pinyin": "Shamian",
                 "status": "attested",
                 "note": "The small British-and-French concession island at "
                 "Canton; focus of the 1925 boycott."},
        "沙基": {"en": "Shakee", "pinyin": "Shaji",
                 "status": "attested",
                 "note": "The Canton bund where British and French troops shot "
                 "down marchers on June 23, 1925."},
        "浙江": {"en": "Chekiang", "pinyin": "Zhejiang",
                 "status": "attested",
                 "note": "Wealthy coastal province south of Shanghai."},
        "河南": {"en": "Honan", "pinyin": "Henan",
                 "status": "attested",
                 "note": "North-central province, site of the February 1923 "
                 "railway massacre at Chengchow (Zhengzhou)."},
        "安徽": {"en": "Anhwei", "pinyin": "Anhui",
                 "status": "attested",
                 "note": "Lower-Yangtze province; Chen Tu-hsiu&#8217;s home."},
    },
    "terms": {
        "厘金": {"en": "likin", "pinyin": "lijin",
                 "status": "attested",
                 "note": "The internal transit tax (1853&#8211;1931) levied on "
                 "goods in movement at local barriers."},
        "县": {"en": "hsien", "pinyin": "xian",
                "status": "attested",
                "note": "A county, the basic unit of local administration."},
        "三民主义": {"en": "Three People&#8217;s Principles",
                     "pinyin": "San Min Zhuyi", "status": "attested",
                     "note": "Sun Yat-sen&#8217;s doctrine of nationalism, "
                     "democracy, and the people&#8217;s livelihood; the "
                     "Kuomintang&#8217;s official ideology (San Min Chu I)."},
    },
}


def main():
    g = json.load(open(GLOSS, encoding="utf-8"))
    added = 0
    for section, rows in ADD.items():
        sec = g.setdefault(section, {})
        for k, v in rows.items():
            if k in sec:
                print("skip existing %s/%s" % (section, k))
                continue
            sec[k] = v
            added += 1
    with open(GLOSS, "w", encoding="utf-8") as fh:
        json.dump(g, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    # re-read and verify
    g2 = json.load(open(GLOSS, encoding="utf-8"))
    for section, rows in ADD.items():
        for k in rows:
            assert g2[section][k]["en"] == rows[k]["en"], (section, k)
    print("added %d rows; re-read verified" % added)
    for s in ("people", "organizations", "places", "terms"):
        print("  %s: %d rows" % (s, len(g2[s])))


if __name__ == "__main__":
    main()
