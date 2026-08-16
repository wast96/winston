#!/usr/bin/env python3
"""Add B26's new keyed glossary rows BY HAND into the sectioned glossary.json.
Idempotent; every row carries a pinyin field (qc_entities does rec['pinyin']).
Each hanzi key is verified as a substring of the authoritative data/zh/ch33.txt
so a Write-tool CJK mangling cannot slip a corrupted key into the glossary.

B26 = ch33 (第一章 振衰起敝 二次出发, the FIRST Part-Four narrative chapter). Most
furniture is already keyed (Zheng Jiemin, Zhang Yanyuan, Liu Peichu, Ye Jianying,
Marshall inline, Dai Li, Mao Renfeng, Bai Chongxi, Zhang Qun, Zhou Enlai, Wang
Tianmu, Wang Kemin, Qi Qingbin, Bai Shiwei, Zeng Che, Chen Ziyi, Zhou Shiguang,
Mao Wanli, He Zhiyuan, Pan Qiwu, Zheng Enpu, Bi Gaokui, Liu Yuanshen; 绥靖总队,
励志训练班, 励志计划, 军事三人小组, 军事调处执行部, 忠义救国军, 临澧训练班, 中央训练团;
绥靖/戡乱/剿匪/匪谍; Beiping/Tianjin/East Hebei/Luan county; the gates Andingmen,
Xizhimen). New keyed rows, each a distinctive proper noun or institution that
renders ONE way and recurs (the three First-Brigade pillars, the command chain,
the Baomiju, the People's Service Corps, and the two Part-Four concept-terms):

  李玉林  Li Yulin      — deputy commander of the First Brigade (a First-Brigade pillar).
  罗敬    Luo Jing      — the brigade's political director; calligrapher of the covers.
  侯腾    Hou Teng      — deputy chief of the Second Bureau (Zheng's command chain).
  吴安之  Wu Anzhi      — Beiping colleague, now Ping-Han Railway police chief.
  马汉三  Ma Hansan     — Beiping Office director, then civil-affairs bureau chief.
  张家铨  Zhang Jiaquan — the old Cangzhou-Section leader, now at the Field HQ.
  史泓    Shi Hong      — the old Beiping-Station courier, now at the Bandit Sup. HQ.
  陈诚    Chen Cheng    — Chief of the General Staff (Chen's self-correction, sec. 1).
  保密局  the Baomiju   — the postwar successor to the Juntong; Mao Renfeng's bureau.
  人民服务总队 the People's Service Corps — Liu Peichu's earlier corps, handed over.
  特种部队 special-operations unit (term)  — the new-pattern force of section 1.
  特种组织 special organization (term)     — the older service the Leader mourned.

Rendered INLINE, NOT keyed (glossary-key discipline — one-off roster/memoir names,
standard place-names, Western/one-off officers, or common-noun renderings that
legitimately vary): the four other brigade commanders 陈振山/刘仁华/郭重新/靳易夫,
王兆芬, 王文, 张作兴, 李运昌, 吕正操, 楼兆元, 王云孙, 张逢义, 佟荣功, 陈仙洲, 李汉元,
程一鸣, 王智斌/齐枕平/郭子中, and the whole roster of Luo Jing's memoir (邢广谟,
何其祥, 乔家才, 沈兼士, 英千里, 张怀, 魏南昌, 龚仙舫, 刘钦礼, 刘启瑞, 张毅夫, 傅有权,
沈克非, 王之桐, 刘罗义, 关颂韬); Marshall / Colonel Robertson (Western); 华北忠义救国军
'the North China Loyal and Patriotic Army' (built on the keyed 忠义救国军); the
railways, gates, and provinces per the settled conventions."""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOSS = os.path.join(ROOT, "glossary.json")
zh = open(os.path.join(ROOT, "data", "zh", "ch33.txt"), encoding="utf-8").read()

PEOPLE = {
    "李玉林": {"en": "Li Yulin", "pinyin": "Lǐ Yùlín", "status": "provisional",
             "note": "Deputy commander of Chen's First Brigade, a fellow "
                     "East-Hebei man and, in the War of Resistance, chief of "
                     "staff of the Sixth Route Army of the North China Loyal and "
                     "Patriotic Army; imprisoned and tortured by the Japanese, "
                     "he survived and was called 'Fifth Brother' by his fellow "
                     "prisoners. One of the three 'pillars' of the brigade."},
    "罗敬": {"en": "Luo Jing", "pinyin": "Luó Jìng", "status": "provisional",
            "note": "The First Brigade's political director, and the calligrapher "
                    "who inscribed the covers and title-leaves of all five Nameless "
                    "Heroes volumes; a Fu Jen University graduate gravely wounded "
                    "by a bomb-splinter at Chongqing in 1941. A 'pillar' of the "
                    "brigade."},
    "侯腾": {"en": "Hou Teng", "pinyin": "Hóu Téng", "status": "provisional",
            "note": "Courtesy name Feixia; one of the two deputy chiefs of the "
                    "Second Bureau of the Ministry of National Defense, in Zheng "
                    "Jiemin's command chain over the Pacification Corps."},
    "吴安之": {"en": "Wu Anzhi", "pinyin": "Wú Ānzhī", "status": "provisional",
             "note": "An old Beiping-Tianjin colleague of Chen's, now chief of "
                     "the police department of the Ping-Han Railway Administration "
                     "Bureau; he met Chen at Xiyuan airfield on his return."},
    "马汉三": {"en": "Ma Hansan", "pinyin": "Mǎ Hànsān", "status": "provisional",
             "note": "Appointed by Dai Li director of the Juntong's Beiping Office "
                     "after the victory, then Chief of the Bureau of Civil Affairs "
                     "of the Beiping Municipal Government; his residence was the "
                     "very Meizha Hutong house of the 1938 Wang Kemin operation."},
    "张家铨": {"en": "Zhang Jiaquan", "pinyin": "Zhāng Jiāquán", "status": "provisional",
             "note": "Leader of the 'Cangzhou Section' in the early 1930s, now a "
                     "major-general and chief of the Second Section of the Beiping "
                     "Field Headquarters."},
    "史泓": {"en": "Shi Hong", "pinyin": "Shǐ Hóng", "status": "provisional",
            "note": "An old directly subordinate courier of the Beiping Station, "
                    "now a major-general and chief of the Second Section of the "
                    "North China Bandit Suppression Headquarters."},
    "陈诚": {"en": "Chen Cheng", "pinyin": "Chén Chéng", "status": "attested",
            "note": "1898-1965; one of Chiang Kai-shek's most trusted generals "
                    "and, at this time, Chief of the General Staff (Chen corrects "
                    "here his fourth volume's misattribution of the post to Bai "
                    "Chongxi, who was Minister of National Defense)."},
}

ORGANIZATIONS = {
    "保密局": {"en": "the Baomiju", "pinyin": "Bǎomìjú", "status": "decided",
             "note": "In full the Bureau of Secrets (保密局) of the Ministry of "
                     "National Defense, the postwar successor to the Juntong "
                     "(Bureau of Investigation and Statistics) after its 1946 "
                     "reorganization; headed by Mao Renfeng. Chen served it as "
                     "leader of the Beiping directly subordinate section while "
                     "commanding the Pacification Corps' First Brigade under the "
                     "separate Second Bureau."},
    "人民服务总队": {"en": "the People's Service Corps", "pinyin": "Rénmín Fúwù Zǒngduì",
                "status": "provisional",
                "note": "A Ministry of National Defense corps commanded by Liu "
                        "Peichu in eastern Henan before he was moved to head the "
                        "Pacification Corps; several of its cadres passed into the "
                        "Lizhi Class."},
}

TERMS = {
    "特种部队": {"en": "special-operations unit", "pinyin": "tèzhǒng bùduì",
              "status": "decided",
              "note": "The new-pattern special force of the Pacification Corps; "
                      "the same compound is glossed 'Special Forces' in the "
                      "chapter that defines it (Part Four, chapter two)."},
    "特种组织": {"en": "special organization", "pinyin": "tèzhǒng zǔzhī",
              "status": "decided",
              "note": "The Leader's term for the older special services he had "
                      "'raised with his own hands over twenty years,' the Juntong "
                      "foremost among them, whose decay he lamented at the opening "
                      "of the Lizhi Class."},
}

SECTIONS = {"people": PEOPLE, "organizations": ORGANIZATIONS, "terms": TERMS}


def main():
    gl = json.load(open(GLOSS, encoding="utf-8"))
    added = 0
    for sec, rows in SECTIONS.items():
        for k, v in rows.items():
            if k not in zh:
                sys.exit("KEY NOT IN data/zh/ch33.txt (possible mangling): %r" % k)
            if k in gl[sec]:
                if gl[sec][k].get("en") != v["en"]:
                    sys.exit("CONFLICT: %s already keyed to %r" % (k, gl[sec][k]))
                continue
            gl[sec][k] = v
            added += 1
    json.dump(gl, open(GLOSS, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("added %d B26 glossary rows" % added)


if __name__ == "__main__":
    main()
