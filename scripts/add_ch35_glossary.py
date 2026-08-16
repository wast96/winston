#!/usr/bin/env python3
"""Add B28's new keyed glossary rows BY HAND into the sectioned glossary.json.
Idempotent; every row carries a pinyin field (qc_entities does rec['pinyin']).
Each hanzi key is verified as a substring of the authoritative data/zh/ch35.txt
so a Write-tool CJK mangling cannot slip a corrupted key into the glossary.

B28 = ch35 (第三章 一番风雨 几片落叶, the third Part-Four narrative chapter). Most
of the Part-Four furniture is already keyed (特种部队/特种组织; 绥靖总队; 军统; 保密局;
励志训练班; 忠义救国军; 交警总队; 华北剿匪总司令部; 李玉林/罗敬/刘原深/刘培初/张家铨/
郑介民/戴笠/李宗仁/傅作义/江田/张作兴/王文/曾澈/毛万里/何应钦/齐庆斌/罗君强/史泓/聂恩俊;
陈独秀/李大钊/毛泽东/周恩来/聂荣臻; 绥靖/戡乱/剿匪/匪谍; Beiping/Tianjin/Hebei).

New keyed rows — distinctive proper nouns / historical figures that render ONE way
and recur through the chapter's central operation (the attempt to reach Lin Biao and
Tao Zhu through Li Mingqiu):

  李鸣秋   Li Mingqiu   — the ex-Communist schoolmate used as the go-between; the
                          pivot of the whole chapter (person; provisional, obscure).
  李运昌   Li Yunchang  — the East-Hebei guerrilla chief, later a CCP general and
                          Minister of Railways; recurs (person; attested).
  罗荣桓   Luo Ronghuan — political commissar of the NE PLA, whose intervention
                          Zheng Jiemin warns Chen to avoid; later a PLA marshal
                          (person; attested).
  黄郛     Huang Fu     — the diplomat (courtesy Yingbai) who acted for He Yingqin
                          at Beiping in the early 1930s; recurs in the flashback
                          (person; attested).
  东北人民解放军  the Northeast People's Liberation Army — the CCP field army of
                          Lin Biao and Tao Zhu, recurring as the operation's target
                          (org; decided). NB the source once prints the glitch form
                          东北人民解放车 (车 for 军, ch35 L134); the correct glyph is
                          present elsewhere (L94/L158/L181), so the key holds.

Rendered INLINE, NOT keyed (glossary-key discipline — one-off roster/memoir names,
one-off officers, standard place-names, historical one-mention figures, common-noun
renderings that vary): the joining old comrades 白家祺 Bai Jiaqi, 王智斌/齐枕平/郭子中
(the Japanese-interpreter trio), 李耀 Li Yao, 李长清 Li Changqing, 庞兆丰/刘文勋/张筱璞/
魏钧 (the introduced officers); the Shanghai-days colleagues 毛一鹭 Mao Yilu, 黄维
Huang Wei, 洪复予 Hong Fuyu, 周祺卿 Zhou Qiqing; 尹擎宇 Yin Qingyu; 江灏/江振寰 (Jiang
Tian's Communist kin); the Whampoa-days instructors and cadets 郭大荣/赵锦文/俞镛/丁维经/
王文翰/李靖难/卢濬泉/帅崇兴/惠济/王登梯/方鼎英/吴思豫/万力民/何焜/钟期光 (one-off roster);
范行 Fan Xing (from Part One). 华北忠义救国军 renders on the keyed 忠义救国军; 华北人民
解放军 (one mention) and 东北剿匪总司令部 (one mention) render inline. Railways, gates,
hutong, provinces, and place-names per the settled conventions."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOSS = os.path.join(ROOT, "glossary.json")
ZH = os.path.join(ROOT, "data", "zh", "ch35.txt")

# section -> { hanzi: row }
ADDS = {
    "people": {
        "李鸣秋": {
            "en": "Li Mingqiu",
            "pinyin": "Lǐ Míngqiū",
            "status": "provisional",
            "note": "Chen's Whampoa schoolmate, an early Communist imprisoned nine "
                    "years, used in 1948 as the go-between to reach Lin Biao and "
                    "Tao Zhu; the pivot of the chapter.",
        },
        "李运昌": {
            "en": "Li Yunchang",
            "pinyin": "Lǐ Yùnchāng",
            "status": "attested",
            "note": "A Zunhua man and East-Hebei guerrilla chief in the war years, "
                    "later a CCP general and Minister of Railways.",
        },
        "罗荣桓": {
            "en": "Luo Ronghuan",
            "pinyin": "Luó Rónghuán",
            "status": "attested",
            "note": "Political commissar of the Communist Northeast field army, "
                    "senior in the Party to Lin Biao; later a PLA marshal. Zheng "
                    "Jiemin warns Chen to avoid his intervention.",
        },
        "黄郛": {
            "en": "Huang Fu",
            "pinyin": "Huáng Fú",
            "status": "attested",
            "note": "The diplomat (courtesy Yingbai) who acted for He Yingqin at "
                    "Beiping in the early 1930s as chairman of the Executive Yuan's "
                    "Beiping Political Affairs Reorganization Committee.",
        },
    },
    "organizations": {
        "东北人民解放军": {
            "en": "the Northeast People's Liberation Army",
            "pinyin": "Dōngběi Rénmín Jiěfàngjūn",
            "status": "decided",
            "note": "The Chinese Communist field army in the Northeast, commanded "
                    "by Lin Biao with Tao Zhu as political-department director; the "
                    "target of the chapter's intelligence operation.",
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
            assert hanzi in zh, "key %r not a substring of data/zh/ch35.txt" % hanzi
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
