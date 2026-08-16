#!/usr/bin/env python3
"""Add B27's new keyed glossary rows BY HAND into the sectioned glossary.json.
Idempotent; every row carries a pinyin field (qc_entities does rec['pinyin']).
Each hanzi key is verified as a substring of the authoritative data/zh/ch34.txt
so a Write-tool CJK mangling cannot slip a corrupted key into the glossary.

B27 = ch34 (第二章 自动自发 同心同德, the doctrinal Part-Four chapter). It is heavy
on definition and organization, so most furniture is already keyed (特种部队 /
特种组织, the two concept-terms; 绥靖总队 the Pacification Corps; 军统 the Juntong;
保密局 the Baomiju; 中统 the Zhongtong; 复兴社 the Renaissance Society; 人民服务总队
the People's Service Corps; 励志训练班; 忠义救国军; 李玉林, 罗敬, 刘培初, 刘原深,
郑介民, 戴笠, 应元勋, 张敬尧, 段祺瑞; 绥靖/戡乱/剿匪/匪谍; Beiping/Tianjin/Hebei).

New keyed rows — distinctive institutions that render ONE way and are likely to
recur, plus the one recurring support figure Chen flags to revisit:

  交警总队           the Transport Police Corps  — the postwar rebadging of the
                     Loyal and Patriotic Army as 'Transport Police' (org).
  华北剿匪总司令部    the North China Bandit-Suppression Headquarters — the body
                     that conferred the First Brigade's code-name '0760' (org).
  聂恩俊             Nie Enjun — the First Brigade quartermaster, a Hefei man and
                     Quartermaster-School graduate; Chen flags him to revisit
                     ('容以后再说'), so keyed provisional (person).

Rendered INLINE, NOT keyed (glossary-key discipline — one-off roster/memoir names,
one-off spies, standard place-names, historical one-mention figures, or common-noun
renderings that legitimately vary), consistent with the ch33 decision to leave these
inline: the section leader / command-room CO 王兆芬 Wang Zhaofen and 张作兴 Zhang
Zuoxing (both inline since ch33); the two Communist spy students 杨荣远 Yang Rongyuan
and 王铭扬 Wang Mingyang (one-off); the roster of brigade commanders 陈振山, 刘仁华,
王德新, 郭重新, 杨正之, 靳易夫, 管容德 and the memoir author 张振东 Zhang Zhendong
(one-off roster); the command-room COs 江田, 常绍曾, 庞兆丰, 张筱朴, 张鲁颖; the general
廖耀湘 Liao Yaoxiang (one mention); the food writer 唐鲁孙 Tang Lusun (inline); the
Tianjin joint-office members 沈泽臣, 张子奇, 王若僖 (one-off); the supply chiefs
surnamed 耿 Geng and 吕 Lü. 华北忠义救国军 renders on the keyed 忠义救国军. Railways,
gates, hutong, and provinces per the settled conventions."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOSS = os.path.join(ROOT, "glossary.json")
ZH = os.path.join(ROOT, "data", "zh", "ch34.txt")

# section -> { hanzi: row }
ADDS = {
    "organizations": {
        "交警总队": {
            "en": "Transport Police Corps",
            "pinyin": "Jiāojǐng Zǒngduì",
            "status": "decided",
            "note": "The Transport Police Corps (交通警察总队), the postwar "
                    "rebadging of the Loyal and Patriotic Army as 'transport "
                    "police'; in Chen's account it was in fact given over to the "
                    "suppression of the Communist rising.",
        },
        "华北剿匪总司令部": {
            "en": "North China Bandit-Suppression Headquarters",
            "pinyin": "Huáběi Jiǎofěi Zǒngsīlìngbù",
            "status": "decided",
            "note": "The North China Bandit-Suppression Headquarters, the "
                    "Nationalist theater command that conferred the First "
                    "Brigade's code-name 'Unit 0760'; built on the keyed "
                    "剿匪 'bandit-suppression'.",
        },
    },
    "people": {
        "聂恩俊": {
            "en": "Nie Enjun",
            "pinyin": "Niè Ēnjùn",
            "status": "provisional",
            "note": "The First Brigade's quartermaster major, a Hefei man and "
                    "graduate of the Quartermaster School, drawn from the Sixth "
                    "Depot Superintendency; Chen flags him to revisit.",
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
            assert hanzi in zh, "key %r not a substring of data/zh/ch34.txt" % hanzi
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
