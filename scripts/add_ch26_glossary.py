#!/usr/bin/env python3
"""Add ch26's new glossary rows BY HAND into the sectioned glossary.json.
Idempotent; every row carries a pinyin field (qc_entities does rec['pinyin']).
Each hanzi key is verified as a substring of the authoritative data/zh/ch26.txt
so a Write-tool CJK mangling cannot slip a corrupted key into the glossary.

ch26 (泰山鸿毛) is a martyr-roster chapter: it names the nameless dead of the
Shanghai District and the Kang Corps, reproduces a martyr's prison memoir, a
Japanese gendarmerie account of the Akagi assassination, and a captured CCP
memoir. New keyed cast, all rendered one way in the reading text.

One-off names rendered inline in pinyin, NOT keyed (glossary-key discipline):
the eight martyrs of the Ding Mocun verdict (许克/李楚琛/陈兆庆/徐阿梅/彭福戎),
the Kang Corps founders/martyrs (李宝奇/沈栋/郭肇和/李如鹏/李实仁/陈肇基/冯运修/
纪树仁/纪念华/朱云/陈维霖/罗长光/黄昆/张仲华), the Kang Corps action men (祝宗梁/
袁汉俊/吕乃灏/刘世华/孙克敏/钱致伦/叶以昌/何敏信/阚津婉), the Akagi hit-team
(李德昌/叶东山/周振芳/俞森林/杨景文/方慧生), the Japanese officers rendered inline
(中村常雄/小林峰三郎/杉本喜三郎/加藤田), the Tianjin/Beiping targets (陶尚铭/王竹林/
程锡庚/俞大纯), 向海潜 (styled name of Xiang Songpo, inline "Xiang Haiqian"), and
the labor-movement sub-group roster (贺智诚/贝布/章灿/徐梅平 etc.). Attested
Shanghai roads/parks keep their historical names inline (Robison Road, Yu Yuen…
no: 愚园路 is keyed "Yuyuan Road" from a prior batch; the officer 劳勃生 "Lao
Bosheng" is keyed but the road 劳勃生路 renders "Robison Road" — a keyed-substring
false positive, documented in PROGRESS)."""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOSS = os.path.join(ROOT, "glossary.json")
ZH = os.path.join(ROOT, "data", "zh", "ch26.txt")
zh_text = open(ZH, encoding="utf-8").read()

PEOPLE = {
    "丁默邨": {"en": "Ding Mocun", "pinyin": "Dīng Mòcūn", "status": "attested",
               "note": "Co-founder and director of the puppet Special Operations "
                       "Headquarters (No. 76) with Li Shiqun; tried and executed as a "
                       "traitor after the war."},
    "汪时璟": {"en": "Wang Shiying", "pinyin": "Wāng Shíjǐng", "status": "attested",
               "note": "North China's foremost economic collaborator; the Kang Corps' "
                       "unfinished target (see Part One, ch06). Rendered Wang Shiying "
                       "consistently across the book."},
    "施何成": {"en": "Shi Hecheng", "pinyin": "Shī Héchéng", "status": "attested",
               "note": "A New Group One operative (aliases Bao Yueren, later Peng Jun); "
                       "his letters supply several of the chapter's martyr cases."},
    "邵范九": {"en": "Shao Fanjiu", "pinyin": "Shào Fànjiǔ", "status": "attested",
               "note": "A cousin's nephew of the KMT elder Shao Lizi; sanctioned in "
                       "November 1939 for going over to the puppets."},
    "陶联芳": {"en": "Tao Lianfang", "pinyin": "Táo Liánfāng", "status": "attested",
               "note": "A New Group One member, buried alive by the puppet Huzhou "
                       "Station after being caught re-linking with the Bureau."},
    "徐寿新": {"en": "Xu Shouxin", "pinyin": "Xú Shòuxīn", "status": "attested",
               "note": "Alias Zhu Chengwo; chief communications inspector of the "
                       "Shanghai District, shot at No. 76 on 25 Dec 1939. The reproduced "
                       "Xu Wenqi essay memorializes him."},
    "朱承我": {"en": "Zhu Chengwo", "pinyin": "Zhū Chéngwǒ", "status": "attested",
               "note": "Alias of the martyr Xu Shouxin, taken to keep the memory of his "
                       "late wife Zhu Cheng'e."},
    "徐寿棪": {"en": "Xu Shouyan", "pinyin": "Xú Shòuyǎn", "status": "attested",
               "note": "Xu Shouxin's younger brother, a Juntong veteran; his letters "
                       "recovered his brother's martyrdom for this book."},
    "徐文祺": {"en": "Xu Wenqi", "pinyin": "Xú Wénqí", "status": "attested",
               "note": "A Shanghai District assistant secretary imprisoned with Xu "
                       "Shouxin at No. 76; author of the reproduced memorial essay."},
    "余延智": {"en": "Yu Yanzhi", "pinyin": "Yú Yánzhì", "status": "attested",
               "note": "Fifth Action Brigade commander (surname perhaps Chu), killed "
                       "with Xu Shouxin at No. 76 in December 1939."},
    "周锡良": {"en": "Zhou Xiliang", "pinyin": "Zhōu Xīliáng", "status": "attested",
               "note": "A counter-espionage operative inside No. 76, killed there in "
                       "December 1939; the puppet verdict writes his name with a "
                       "different middle character (周希良), alike in sound."},
    "张执一": {"en": "Zhang Zhiyi", "pinyin": "Zhāng Zhíyī", "status": "attested",
               "note": "A CCP united-front operative under the Jiangsu Provincial "
                       "Committee, later deputy head of the Party's Central United Front "
                       "Work Department; author of the quoted memoir 'In the Heart of "
                       "the Enemy.'"},
    "赤木亲之": {"en": "Akagi Chikayuki", "pinyin": "Akagi Chikayuki", "status": "attested",
               "note": "Japanese deputy commissioner of the Shanghai Municipal Police, "
                       "assassinated on Yuyuan Road, June 1941."},
    "林秀澄": {"en": "Hayashi Hidezumi", "pinyin": "Hayashi Hidezumi", "status": "attested",
               "note": "Lieutenant-colonel, chief of the Special Higher Section of the "
                       "Shanghai Japanese Gendarmerie; the 'Section chief Lin' Chen knew "
                       "only by surname."},
    "李正梁": {"en": "Li Zhengliang", "pinyin": "Lǐ Zhèngliáng", "status": "attested",
               "note": "Alias Li Liang; leader of the Third Action Brigade's Fourth "
                       "Group, who directed the Akagi assassination."},
    "李亮": {"en": "Li Liang", "pinyin": "Lǐ Liàng", "status": "attested",
             "note": "The everyday name of Li Zhengliang, director of the Akagi case."},
    "林怀部": {"en": "Lin Huaibu", "pinyin": "Lín Huáibù", "status": "attested",
               "note": "The hired bodyguard who shot the tycoon Zhang Xiaolin dead in "
                       "October 1940; the mysteries around him open ch27."},
    "俞作柏": {"en": "Yu Zuobai", "pinyin": "Yú Zuòbǎi", "status": "attested",
               "note": "Deputy commander-in-chief of the Loyal and Patriotic Army, "
                       "addressed in one of Dai Li's quoted telegrams."},
    "林之江": {"en": "Lin Zhijiang", "pinyin": "Lín Zhījiāng", "status": "attested",
               "note": "A No. 76 executioner (with Wan Lilang) of Xu Shouxin; later "
                       "turned back to the government and died in poverty at Hong Kong."},
    "萧焕文": {"en": "Xiao Huanwen", "pinyin": "Xiāo Huànwén", "status": "attested",
               "note": "The Hunan-born patriarch of the Xiao family, whose whole "
                       "household served the Juntong; kept the Loyal Army's liaison."},
    "萧杰英": {"en": "Xiao Jieying", "pinyin": "Xiāo Jiéyīng", "status": "attested",
               "note": "The Xiao patriarch's third daughter, who ran one of the Shanghai "
                       "District's liaison stations out of the family home."},
    "萧张权": {"en": "Xiao Zhangquan", "pinyin": "Xiāo Zhāngquán", "status": "attested",
               "note": "The Xiao family's youngest son, Eighth Action Brigade commander, "
                       "tortured to death by the Suzhou gendarmerie, aged about 24."},
    "陈植琚": {"en": "Chen Zhiju", "pinyin": "Chén Zhíjū", "status": "attested",
               "note": "Xiao Shuying's husband; leader of the Dachang field group, blown "
                       "to death by an enemy plane early in the war."},
    "李鑫": {"en": "Li Xin", "pinyin": "Lǐ Xīn", "status": "attested",
             "note": "A Shanghai Kang Corps action man who perished with his own bomb at "
                     "the Jessfield Park Axis-recognition rally, August 1941."},
    "缪维": {"en": "Miao Wei", "pinyin": "Miào Wéi", "status": "attested",
             "note": "A Kang Corps operative killed with Huang Kezhong when their charge "
                     "went off at Hongkou Park."},
    "黄克忠": {"en": "Huang Kezhong", "pinyin": "Huáng Kèzhōng", "status": "attested",
               "note": "A Kang Corps action man (also recorded as Huang Ruitang); took "
                       "part in the Tōwa Theater bombing and died at Hongkou Park."},
    "向松坡": {"en": "Xiang Songpo", "pinyin": "Xiàng Sōngpō", "status": "attested",
               "note": "A prominent Hong Gang chief in Shanghai (styled Haiqian) whose "
                       "connection the CCP operative Zhang Zhiyi used."},
}

ORGS = {
    "上海职工运动委员会": {"en": "the Shanghai Workers'-Movement Committee",
                          "pinyin": "Shànghǎi Zhígōng Yùndòng Wěiyuánhuì",
                          "status": "attested",
                          "note": "The labor-movement organ Dai Li ordered set up in "
                                  "1940, with the notables Yu Qiaqing and Zhao Zigang as "
                                  "figurehead members; it never really took shape."},
    "抗团": {"en": "the Kang Corps", "pinyin": "Kàngtuán", "status": "decided",
             "note": "The standard abbreviation of the Anti-Japanese Traitor-Killing "
                     "Corps (抗日杀奸团, NOTED ch02/ch11)."},
}


def main():
    gl = json.load(open(GLOSS, encoding="utf-8"))
    added = 0
    for sec, rows in (("people", PEOPLE), ("organizations", ORGS)):
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
    print("added %d new rows; people=%d orgs=%d"
          % (added, len(gl["people"]), len(gl["organizations"])))


if __name__ == "__main__":
    main()
