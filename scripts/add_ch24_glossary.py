#!/usr/bin/env python3
"""Add ch24's new glossary rows BY HAND into the sectioned glossary.json.
Idempotent; every row carries a pinyin field (qc_entities does rec['pinyin']).
Each hanzi key is verified as a substring of the authoritative data/zh/ch24.txt
so a Write-tool CJK mangling cannot slip a corrupted key into the glossary."""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOSS = os.path.join(ROOT, "glossary.json")
ZH = os.path.join(ROOT, "data", "zh", "ch24.txt")

zh_text = open(ZH, encoding="utf-8").read()

PEOPLE = {
    "劳勃生": {"en": "Lao Bosheng", "pinyin": "Láo Bóshēng", "status": "provisional",
              "note": "The source gives only the Chinese transliteration 劳勃生 of a "
                      "Western (probably British) surname—likely something like "
                      "Robertson or Robinson—of the Shanghai Municipal Police political "
                      "section; the original form is not certain, so the romanization is "
                      "of the Chinese as given."},
    "袁殊": {"en": "Yuan Shu", "pinyin": "Yuán Shū", "status": "attested",
             "note": "Also called Xueyi (学易) and Xiaoyi (筱易); a journalist-agent of "
                     "tangled loyalties, later revealed as a Communist."},
    "新艳秋": {"en": "Xin Yanqiu", "pinyin": "Xīn Yànqiū", "status": "attested",
               "note": "A celebrated Peking-opera actress of the female (dan) roles, "
                       "performing at the Gengxin Stage on the night of Yu Yefeng's sanction."},
    "吴世宝": {"en": "Wu Shibao", "pinyin": "Wú Shìbǎo", "status": "attested",
               "note": "Alias Yunfu (云甫); an underworld figure and first commander of "
                       "No. 76's guard corps, later poisoned."},
    "胡均鹤": {"en": "Hu Junhe", "pinyin": "Hú Jūnhè", "status": "attested",
               "note": "Chief of the Second Section of No. 76, later found to be a "
                       "Communist as well."},
    "傅也文": {"en": "Fu Yewen", "pinyin": "Fù Yěwén", "status": "provisional",
               "note": "Secretary-general of No. 76, installed at the recommendation of "
                       "Li Shiqun's wife; later found to be a Communist. Romanization mine."},
    "刘俊卿": {"en": "Liu Junqing", "pinyin": "Liú Jùnqīng", "status": "provisional",
               "note": "A Shanghai Municipal Police officer brought into the Shanghai "
                       "District's work by Liu Shaokui. Romanization mine."},
    "蒋福田": {"en": "Jiang Futian", "pinyin": "Jiǎng Fútián", "status": "provisional",
               "note": "A working connection of the Shanghai District within the French "
                       "Concession police. Romanization mine."},
}
PLACES = {
    "更新舞台": {"en": "Gengxin Stage", "pinyin": "Gēngxīn Wǔtái", "status": "attested",
                 "note": "A Peking-opera theater on Newchwang Road in the International "
                         "Settlement; the site of the Yu Yefeng sanction of January 1940."},
}


def main():
    gl = json.load(open(GLOSS, encoding="utf-8"))
    added = 0
    for sec, rows in (("people", PEOPLE), ("places", PLACES)):
        for k, v in rows.items():
            if k not in zh_text:
                sys.exit("KEY NOT IN data/zh (possible mangling): %r" % k)
            if k in gl[sec]:
                if gl[sec][k].get("en") != v["en"]:
                    sys.exit("CONFLICT: %s already keyed to %r" % (k, gl[sec][k]))
                continue
            gl[sec][k] = v
            added += 1
    json.dump(gl, open(GLOSS, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("added %d new rows; people=%d places=%d" %
          (added, len(gl["people"]), len(gl["places"])))


if __name__ == "__main__":
    main()
