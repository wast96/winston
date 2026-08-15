#!/usr/bin/env python3
"""Add B25's new keyed glossary rows BY HAND into the sectioned glossary.json.
Idempotent; every row carries a pinyin field (qc_entities does rec['pinyin']).
Each hanzi key is verified as a substring of the authoritative data/zh/ch32.txt
so a Write-tool CJK mangling cannot slip a corrupted key into the glossary.

B25 = ch32 (自序, the Part-Four self-preface; OPENS Part Four, the 1946-49
civil-war material). Most furniture is already keyed (Zheng Jiemin, Zhang Qun,
Zhou Enlai, Lin Biao, Nie Rongzhen, Zhang Yanyuan; 绥靖 'pacification'; 制裁
'sanction'; Beiping / Tianjin / Chahar / Rehe / Guisui). New keyed rows, each a
distinctive proper noun or institution that renders ONE way and (for the recur-
ring ones) appears again in Part Four:

  叶剑英  Ye Jianying   — Communist representative on the Executive Headquarters.
  刘培初  Liu Peichu    — Corps Commander of the Pacification Corps; author of the
        quoted memoir; earlier the Wuhan practice-corps leader (ch29).
  李宗仁  Li Zongren    — director of the Beiping Field Headquarters.
  傅作义  Fu Zuoyi      — commander of the North China Bandit Suppression HQ.
  计兆祥  Ji Zhaoxiang  — wireless operator of the stay-behind work, a martyr.
  绥靖总队 the Pacification Corps        — the Ministry of National Defense corps.
  军事调处执行部 the Military Mediation Executive Headquarters (Beiping, 1946).
  军事三人小组 the Committee of Three    — Marshall, Zhang Qun, Zhou Enlai.
  励志训练班 the Lizhi Training Class    — training class for the pacification units.
  励志计划 the Lizhi Plan (term)         — the plan raising and training them.

Rendered INLINE, NOT keyed (glossary-key discipline — one-off transliterated
Western names, one-off officials, standard place-names, or common-noun terms
whose rendering legitimately varies): 马歇尔 Marshall and 罗柏森 Colonel Robertson
(Western); 侯腾 Hou Teng, 徐启明 Xu Qiming, 张家铨 Zhang Jiaquan, 史泓 Shi Hong,
雷处长 Director Lei (one-off officials); 河北 Hebei, 绥远 Suiyuan, 山东 Shandong,
河南 Henan, 山西 Shanxi (standard provinces); 戡乱 'suppression of rebellion'
(common-noun term, already rendered so in ch04). Rail lines rendered descript-
ively and footnoted (Beiping-Liaoning / Tianjin-Pukou / Beiping-Hankou /
Beiping-Gubeikou / Beiping-Suiyuan). Places per the settled convention
(Beiping, Tianjin, Nanjing, Shanghai, Ningbo, Qingdao, Hong Kong, Magong)."""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOSS = os.path.join(ROOT, "glossary.json")
zh = open(os.path.join(ROOT, "data", "zh", "ch32.txt"), encoding="utf-8").read()

PEOPLE = {
    "叶剑英": {"en": "Ye Jianying", "pinyin": "Yè Jiànyīng", "status": "attested",
             "note": "The Communist representative on the Military Mediation "
                     "Executive Headquarters at Beiping and chief of staff of the "
                     "Communist army; later a marshal of the People's Republic."},
    "刘培初": {"en": "Liu Peichu", "pinyin": "Liú Péichū", "status": "provisional",
             "note": "Corps Commander of the Ministry of National Defense "
                     "Pacification Corps and head of its Student Corps; author of "
                     "the posthumous memoir Fleeting Glimpses of a Floating Life, "
                     "quoted here. Earlier he had led the Wuhan practice corps in "
                     "which Chen trained (see Part Three, chapter ten)."},
    "李宗仁": {"en": "Li Zongren", "pinyin": "Lǐ Zōngrén", "status": "attested",
             "note": "1891-1969; a leading Guangxi general, director of the "
                     "Chairman's Beiping Field Headquarters, and later, in 1949, "
                     "acting President of the Republic of China."},
    "傅作义": {"en": "Fu Zuoyi", "pinyin": "Fù Zuòyì", "status": "attested",
             "note": "1895-1974; commander-in-chief of the North China Bandit "
                     "Suppression Headquarters and the Nationalist defender of "
                     "Beiping, which he surrendered by negotiated agreement to the "
                     "Communists in January 1949, sparing the city a siege."},
    "计兆祥": {"en": "Ji Zhaoxiang", "pinyin": "Jì Zhàoxiáng", "status": "provisional",
             "note": "A wireless operator of the First Brigade's stay-behind work "
                     "left in Beiping; he shot himself to resist arrest, one of the "
                     "few of the stay-behind party whose fate Chen could trace."},
}

ORGANIZATIONS = {
    "绥靖总队": {"en": "the Pacification Corps", "pinyin": "Suíjìng Zǒngduì",
              "status": "attested",
              "note": "In full the Ministry of National Defense Pacification "
                      "Corps, the postwar special force raised for the 1946-49 "
                      "campaign against the Communists; Chen commanded its First "
                      "Brigade in the Beiping-Tianjin region."},
    "军事调处执行部": {"en": "the Military Mediation Executive Headquarters",
                 "pinyin": "Jūnshì Tiáochǔ Zhíxíngbù", "status": "attested",
                 "note": "The tripartite body (American, Nationalist, and "
                         "Communist) set up at Beiping in 1946 to enforce the "
                         "cease-fire brokered by the Marshall Mission."},
    "军事三人小组": {"en": "the Committee of Three", "pinyin": "Jūnshì Sānrén Xiǎozǔ",
                "status": "attested",
                "note": "The three-man committee of Marshall, Zhang Qun for the "
                        "government, and Zhou Enlai for the Communists, that "
                        "directed the 1946 truce negotiations."},
    "励志训练班": {"en": "the Lizhi Training Class", "pinyin": "Lìzhì Xùnliàn Bān",
               "status": "attested",
               "note": "The training class at the Central Training Corps in "
                       "Nanjing through which the cadres of the Pacification Corps "
                       "were passed; see the note on the Lizhi Plan."},
}

TERMS = {
    "励志计划": {"en": "the Lizhi Plan", "pinyin": "Lìzhì Jìhuà", "status": "decided",
              "note": "The plan under which the Ministry of National Defense "
                      "raised, trained, and tasked the Pacification Corps; 励志 "
                      "means to steel the will or better oneself."},
}

SECTIONS = {"people": PEOPLE, "organizations": ORGANIZATIONS, "terms": TERMS}


def main():
    gl = json.load(open(GLOSS, encoding="utf-8"))
    added = 0
    for sec, rows in SECTIONS.items():
        for k, v in rows.items():
            if k not in zh:
                sys.exit("KEY NOT IN data/zh/ch32.txt (possible mangling): %r" % k)
            if k in gl[sec]:
                if gl[sec][k].get("en") != v["en"]:
                    sys.exit("CONFLICT: %s already keyed to %r" % (k, gl[sec][k]))
                continue
            gl[sec][k] = v
            added += 1
    json.dump(gl, open(GLOSS, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("added %d B25 glossary rows" % added)


if __name__ == "__main__":
    main()
