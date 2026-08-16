#!/usr/bin/env python3
"""Add B29's new keyed glossary rows BY HAND into the sectioned glossary.json.
Idempotent; every row carries a pinyin field (qc_entities does rec['pinyin']).
Each hanzi key is verified as a substring of the authoritative data/zh/ch36.txt
so a Write-tool CJK mangling cannot slip a corrupted key into the glossary.

B29 = ch36 (第四章 掌握先机 备多力分, the fourth Part-Four narrative chapter). Most
of the Part-Four furniture is already keyed (特种部队/特种组织; 绥靖总队; 军统; 保密局;
励志训练班; 华北剿匪总司令部; 东北人民解放军; 李玉林/毛万里/马汉三/傅作义/林彪/陶铸/
毛泽东/聂荣臻/罗荣桓/李鸣秋; 绥靖/戡乱/剿匪/匪谍; Beiping/Tianjin/Hebei/冀东).

New keyed rows — distinctive proper nouns / historical figures / place names that
render ONE way and recur through the chapter (the Anguo "heart-extraction" raid and
the Battle of Shijiazhuang):

  安春山   An Chunshan  — commander of the Provisional Third Army, Fu Zuoyi's
                          favorite general; leads the Anguo raid (person; provisional).
  朱占奎   Zhu Zhankui  — Anci county magistrate, ex-Communist sub-district commander
                          captured and turned, who defected back to the Communists in
                          1948 (person; provisional).
  刘玉珠   Liu Yuzhu    — the fixer who "gave" the brigade 2,000 Japanese rifles, later
                          tried alongside Ma Hansan (person; provisional).
  萧润宇   Xiao Runyu   — First-Directly-Subordinate-Section member; author of the
                          quoted "Record of the Work" (person; provisional).
  牛广金   Niu Guangjin — Shijiazhuang work-group member, wounded and captured; author
                          of the quoted "Brief Record" (person; provisional).
  吕正操   Lü Zhengcao  — Communist commander of the Central Hebei Military District,
                          who held the triangle; later a PLA general (person; attested).
  石家庄   Shijiazhuang — the city (its modern name), scene of the Nov-1947 battle
                          (place; decided).
  石门     Shimen       — the older name Chen uses for Shijiazhuang throughout (place;
                          decided; rendered "Shimen," with "(Shijiazhuang)" at first use).
  安次     Anci         — the county garrisoned by the First Directly Subordinate
                          Section (place; decided).
  安国     Anguo        — the county holding the Temple of the Medicine King, object of
                          the raid on Mao (place; decided).
  正定     Zhengding    — the town screening Shimen, and the northern terminus of the
                          Zheng-Tai railway (place; decided).
  掏心战术  the heart-extraction tactic — the code-name of the Anguo raid; recurs
                          (term; decided; the ch36s03 title glosses it at title level).
  平津保三角地带  the Beiping-Tianjin-Baoding triangle — the central-Hebei bandit
                          region; recurs (term/place; decided).

Rendered INLINE, NOT keyed (glossary-key discipline — one-off roster/memoir names,
one-off officers, standard place-names, historical one-mention figures): 罗历戎 Luo
Lirong (Third Army cmdr), 刘英 Liu Ying (32nd Division cmdr), 张铁林 Zhang Tielin
(Shijiazhuang group chief), 陈秀桐/郑静庭/冯志俊/姜丙辰/白永龄/赵万里/王德新/张果维/
马惠璋/郭清钰 (the section roster), 张建三/张侗夫/杨志毅/牛清川/李明光/杨清/朱志璋/张建二
(the work-group roster), 常绍曾/汪鸿翥/吴春祥/陈俊祥 (the Second-Command-Room account
contributors), 曾泽生 Zeng Zesheng, 刘伯承 Liu Bocheng, 胡宗南 Hu Zongnan, 邓宝珊 Deng
Baoshan, 傅东菊 Fu Dongju, 宋劭文/胡仁奎/彭真/孟庆山/程子华/罗玉川 (the border-region
committee), 屈凌汉/罗文浩/李荷/孙连仲/刘瑶章 (the Shimen relief mission), 刘玉珠's host
one Wu, the deputy chief of staff whose surname the source prints as a garbled glyph.
马先生 = Ma Hansan (already keyed as 马汉三; the source names him only as "Mr. Ma" here,
so no new key). Railways (Ping-Han/Zheng-Tai/Bei-Ning/Ping-Gu/Zhe-Gan), the Wutai and
Taihang mountains, 五台山区, 药王庙, Fuping/Yangqu/Yongqing/Gu'an/Jinghai/Qingyuan,
Langfang, Shunyi, and provinces render inline per the settled conventions."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOSS = os.path.join(ROOT, "glossary.json")
ZH = os.path.join(ROOT, "data", "zh", "ch36.txt")

# section -> { hanzi: row }
ADDS = {
    "people": {
        "安春山": {
            "en": "An Chunshan",
            "pinyin": "An Chunshan",
            "status": "provisional",
            "note": "Commander of the Provisional Third Army and a favored general "
                    "of Fu Zuoyi's; led in person the cavalry-spearheaded raid on "
                    "Anguo that narrowly missed Mao Zedong.",
        },
        "朱占奎": {
            "en": "Zhu Zhankui",
            "pinyin": "Zhu Zhankui",
            "status": "provisional",
            "note": "Magistrate of Anci County (concurrently a Hebei district "
                    "commissioner); an ex-Communist military-sub-district commander "
                    "captured and turned, who defected back to the Communists in 1948.",
        },
        "刘玉珠": {
            "en": "Liu Yuzhu",
            "pinyin": "Liu Yuzhu",
            "status": "provisional",
            "note": "A fixer and friend of the deputy brigade commander who made the "
                    "brigade a 'gift' of some 2,000 Japanese rifles, and was later "
                    "detained and tried in the same corruption case as Ma Hansan.",
        },
        "萧润宇": {
            "en": "Xiao Runyu",
            "pinyin": "Xiao Runyu",
            "status": "provisional",
            "note": "A member of the First Directly Subordinate Section; author of "
                    "the 'Record of the Work' quoted at length in section three.",
        },
        "牛广金": {
            "en": "Niu Guangjin",
            "pinyin": "Niu Guangjin",
            "status": "provisional",
            "note": "A member of the Shijiazhuang work-group, wounded by a shell-"
                    "fragment and captured; author of the 'Brief Record of the "
                    "Shijiazhuang Work' quoted in section four.",
        },
        "吕正操": {
            "en": "Lü Zhengcao",
            "pinyin": "Lü Zhengcao",
            "status": "attested",
            "note": "Communist commander of the Central Hebei Military District, "
                    "which held the Beiping-Tianjin-Baoding triangle from 1938; "
                    "later a PLA general.",
        },
    },
    "places": {
        "石家庄": {
            "en": "Shijiazhuang",
            "pinyin": "Shíjiāzhuāng",
            "status": "decided",
            "note": "The Hebei rail-junction city, scene of the Communist siege and "
                    "capture of November 1947; Chen more often calls it by its older "
                    "name, Shimen.",
        },
        "石门": {
            "en": "Shimen",
            "pinyin": "Shímén",
            "status": "decided",
            "note": "The older name of Shijiazhuang, used throughout this chapter.",
        },
        "安次": {
            "en": "Anci",
            "pinyin": "Ancì",
            "status": "decided",
            "note": "The Hebei county garrisoned by the First Directly Subordinate "
                    "Section (its seat, Langfang lies on the Bei-Ning line).",
        },
        "安国": {
            "en": "Anguo",
            "pinyin": "Ānguó",
            "status": "decided",
            "note": "The Hebei county whose Temple of the Medicine King was the "
                    "object of the raid meant to seize Mao Zedong.",
        },
        "正定": {
            "en": "Zhengding",
            "pinyin": "Zhèngdìng",
            "status": "decided",
            "note": "The town reckoned the screen of Shimen, and the northern "
                    "terminus of the Zheng-Tai railway.",
        },
    },
    "terms": {
        "掏心战术": {
            "en": "the heart-extraction tactic",
            "pinyin": "tāoxīn zhànshù",
            "status": "decided",
            "note": "The code-name of the deep raid into the Communist-held triangle "
                    "aimed at seizing the enemy's leadership at a stroke; the chapter "
                    "title glosses it at title level.",
        },
        "平津保三角地带": {
            "en": "the Beiping-Tianjin-Baoding triangle",
            "pinyin": "Píng-Jīn-Bǎo sānjiǎo dìdài",
            "status": "decided",
            "note": "The dozen-odd counties of central Hebei, bounded by Beiping, "
                    "Tianjin, and Baoding, held by the Communists' Central Hebei "
                    "forces from 1938.",
        },
    },
}


def main():
    zh = open(ZH, encoding="utf-8").read()
    g = json.load(open(GLOSS, encoding="utf-8"))
    added = 0
    for sec, rows in ADDS.items():
        assert sec in g, "missing section %r" % sec
        for hanzi, row in rows.items():
            assert hanzi in zh, "key %r not a substring of data/zh/ch36.txt" % hanzi
            assert "pinyin" in row and row["pinyin"], "row %r lacks pinyin" % hanzi
            if hanzi in g[sec]:
                print("already present:", hanzi)
                continue
            g[sec][hanzi] = row
            added += 1
            print("added [%s] %s -> %s" % (sec, hanzi, row["en"]))
    with open(GLOSS, "w", encoding="utf-8") as fh:
        json.dump(g, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    # re-read verification
    g2 = json.load(open(GLOSS, encoding="utf-8"))
    for sec, rows in ADDS.items():
        for hanzi, row in rows.items():
            assert g2[sec][hanzi]["en"] == row["en"], "re-read mismatch %r" % hanzi
    print("re-read verification OK; %d new rows" % added)


if __name__ == "__main__":
    main()
