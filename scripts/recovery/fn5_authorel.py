#!/usr/bin/env python3
"""Author data/fn5_notes.json for the FN5 footnote-density batch.

Hanzi are pulled PROGRAMMATICALLY from glossary.json by English rendering and
encoded to numeric character references (never hand-typed into the JSON), per
FOOTNOTE_PASS.md section 6 and the STYLE.md round-2 rule.
People notes carry no hanzi. Dashes are numeric refs.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
g = json.load(open(os.path.join(ROOT, "glossary.json"), encoding="utf-8"))

def ncr(s):
    return "".join("&#%d;" % ord(c) for c in s)

def gloss_hz(en_wanted):
    """Return numeric-char-ref encoding of the glossary hanzi key whose en matches."""
    for sec, rows in g.items():
        if not isinstance(rows, dict) or sec in ("_about", "book"):
            continue
        for hz, rec in rows.items():
            en = rec.get("en", "") if isinstance(rec, dict) else ""
            if en == en_wanted:
                return ncr(hz)
    raise SystemExit("glossary hanzi not found for %r" % en_wanted)

EM = "&#8212;"   # em dash
EN = "&#8211;"   # en dash (date ranges)
LSQ = "&#8216;"; RSQ = "&#8217;"; LDQ = "&#8220;"; RDQ = "&#8221;"

shenbao = gloss_hz("Shen Bao")
huji = gloss_hz("China Mutual Aid Society")
takungpao = gloss_hz("Ta Kung Pao")

notes = {
  "ch02": [
    {"anchor": "a shikumen house",
     "note": ("A <i>shikumen</i> (" + LDQ + "stone-framed gate" + RDQ + ") is the "
              "characteristic Shanghai row house of the late nineteenth and early "
              "twentieth centuries: a two- or three-story brick terrace entered "
              "through a stone-arched doorway off a lane. Packed close and easily "
              "lost among their neighbors, such lanes gave the underground both "
              "cover and quick exits, and recur throughout this book. Corroborated.")},
  ],
  "ch03": [
    {"anchor": "study at Sun Yat-sen University in Moscow",
     "note": ("Sun Yat-sen University in Moscow (KUTK) was founded in 1925 to train "
              "Chinese Communist and Kuomintang cadres, and put many of the Party" + RSQ +
              "s leaders of the 1930s through its classes before it closed in 1930. "
              "It is distinct from the Communist University of the Toilers of the East, "
              "the older and broader Comintern school also named in this book. Corroborated.")},
  ],
  "ch04": [
    {"anchor": "the Party since the Third Plenary Session of the Eleventh Central Committee",
     "note": ("The Third Plenary Session of the Eleventh Central Committee, held in "
              "Beijing in December 1978, is the meeting at which Deng Xiaoping" + RSQ +
              "s line prevailed and China turned to " + LDQ + "reform and opening." + RDQ +
              " It became the benchmark from which the Party dated its repudiation of "
              "the Cultural Revolution, and thus of the rehabilitations this book records. "
              "Corroborated.")},
  ],
  "ch05": [
    {"anchor": "he threw in with Sun Chuanfang",
     "note": ("Sun Chuanfang (1885" + EN + "1935), a warlord of the Zhili clique, "
              "controlled the five provinces of the lower Yangzi&#8212;his self-styled "
              + LDQ + "League of Five Provinces" + RDQ + "&#8212;until the Northern "
              "Expedition broke his power in 1926" + EN + "1927. In 1935 he was shot "
              "dead in a Tianjin Buddhist temple by Shi Jianqiao, avenging a father Sun "
              "had had executed a decade earlier, in a killing that became a celebrated "
              "public cause. Corroborated.")},
  ],
  "ch10": [
    {"anchor": "the Shanghai Shen Bao and News Daily of April 22",
     "note": ("The <i>Shen Bao</i> (" + shenbao + "), founded in 1872, was the largest "
              "and most influential Chinese-language daily in Shanghai; its independence "
              "gave its pages unusual weight&#8212;as the " + LDQ + "Wu Hao Notice" + RDQ +
              " affair, late in this book, would turn on. Corroborated.")},
  ],
  "ch14": [
    {"anchor": "December 1929 to join the China Mutual Aid Society",
     "note": ("The China Mutual Aid Society (" + huji + ") is the body earlier called "
              "the China Relief Society (see the note at chapter&#160;2): the "
              "Communist-organized legal-aid and relief society founded in 1925 was "
              "reorganized under this name in 1929. Corroborated.")},
    {"anchor": "a piece of news in Ta Kung Pao",
     "note": ("<i>Ta Kung Pao</i> (" + takungpao + ", " + LDQ + "L" + RSQ + "Impartial"
              + RDQ + "), founded at Tianjin in 1902, was among the most respected "
              "independent Chinese newspapers of the Republican era; it still publishes "
              "from Hong Kong and is one of the oldest Chinese-language papers in the "
              "world. Corroborated.")},
  ],
  "ch15": [
    {"anchor": "left Shanghai for the E-Yu-Wan Soviet area",
     "note": ("The E-Yu-Wan Soviet&#8212;named for the one-syllable classical names of "
              "its three provinces, Hubei (E), Henan (Yu), and Anhui (Wan)&#8212;straddled "
              "the Dabie Mountains and was the second-largest Communist base of the early "
              "1930s and the home of the Fourth Front Army. Under Zhang Guotao its main "
              "force was driven out in 1932. Corroborated.")},
  ],
  "ch16": [
    {"anchor": "he entered the Baoding Army Officers' Academy to study artillery",
     "note": ("The Baoding Army Officers" + RSQ + " Academy, in Hebei, was China" + RSQ +
              "s first modern regular-army officer school; in its years of operation "
              "(1912" + EN + "1923) it trained some eleven thousand officers, many of whom "
              "became the senior commanders of the warlord and Nationalist armies. With "
              "the Yunnan and Whampoa academies it is counted one of the three great "
              "cradles of Republican-era officers. Corroborated.")},
  ],
  "ch17": [
    {"anchor": "a cousin of Li Mingrui",
     "note": ("Li Mingrui (1896" + EN + "1931), a Guangxi general who threw in with the "
              "Communists, was commander-in-chief of the Red Seventh and Eighth Armies "
              "raised in the Bose and Longzhou uprisings that Deng Xiaoping led in 1929"
              + EN + "1930. Captured by Nationalist forces, he was executed in 1931. "
              "Corroborated.")},
  ],
  "ch23": [
    {"anchor": "the State Political Security Bureau in Ruijin",
     "note": ("The State Political Security Bureau (Guojia Zhengzhi Baoweiju) was the "
              "Chinese Soviet Republic" + RSQ + "s political-police and counter-espionage "
              "organ, set up at Ruijin in 1931 and modeled on the Soviet Cheka and GPU; "
              "its first head, Deng Fa, was nicknamed China" + RSQ + "s Dzerzhinsky. It is "
              "where the withdrawn Central Special Section men found new work in the Red "
              "base. Corroborated.")},
    {"anchor": "received Snow, Ma Haide, Ding Ling, and others",
     "note": ("Ma Haide (George Hatem, 1910" + EN + "1988), a Lebanese-American physician "
              "who reached Shanghai in 1933, was drawn to the Communist cause through Agnes "
              "Smedley&#8212;the same circle that sheltered Liu Ding&#8212;and in 1936 made "
              "his way to the Red base, where he took this Chinese name and became the first "
              "foreigner admitted to the Chinese Communist Party. He spent the rest of his "
              "life in China, notably in the control of leprosy and venereal disease. "
              "Corroborated.")},
    {"anchor": "the day of the Dragon Boat Festival",
     "note": ("The Dragon Boat Festival (Duanwu), on the fifth day of the fifth lunar "
              "month and later associated with the poet Qu Yuan, is a traditional Chinese "
              "holiday; here it simply fixes the date of the travelers" + RSQ + " arrival, "
              "in the early summer of 1931. Corroborated.")},
  ],
  "ch25": [
    {"anchor": "its general manager Shi Liangcai",
     "note": ("Shi Liangcai (1880" + EN + "1934) owned and published the <i>Shen Bao</i> "
              "(see the note at chapter&#160;10), making it the most powerful independent "
              "voice in the Chinese press. His refusal to bend to the Kuomintang and his "
              "paper" + RSQ + "s calls to resist Japan cost him his life: on 13 November "
              "1934 Dai Li" + RSQ + "s agents ambushed and killed him on the Shanghai" + EN +
              "Hangzhou road. Corroborated.")},
    {"anchor": "his adviser Tao Xingzhi",
     "note": ("Tao Xingzhi (1891" + EN + "1946), one of modern China" + RSQ + "s foremost "
              "educators, studied under John Dewey at Columbia and built a mass-education "
              "movement on the maxim " + LDQ + "life is education." + RDQ + " A prominent "
              "progressive, he advised Shi Liangcai on the reform of the <i>Shen Bao</i>. "
              "Corroborated.")},
  ],
  "ch26": [
    {"anchor": "Shen Anna, sent by Zhou Enlai to penetrate the Kuomintang Central Party Headquarters",
     "note": ("Shen Anna (born Shen Wan, 1915" + EN + "2010) was placed by the Party inside "
              "the Kuomintang" + RSQ + "s central apparatus as a shorthand stenographer, an "
              "assignment Zhou Enlai helped arrange; from the late 1930s to 1949 she "
              "transcribed the Nationalists" + RSQ + " highest councils and passed the "
              "minutes to the Communists, one of the most productive of the Party" + RSQ +
              "s moles. Corroborated.")},
  ],
}

out = {"notes": notes}
p = os.path.join(ROOT, "data", "fn5_notes.json")
with open(p, "w", encoding="utf-8") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=2)
    fh.write("\n")
n = sum(len(v) for v in notes.values())
print("wrote %s: %d notes across %d units" % (p, n, len(notes)))
