#!/usr/bin/env python3
"""Add B31's new keyed glossary rows BY HAND into the sectioned glossary.json.
Idempotent; every row carries a pinyin field (qc_entities does rec['pinyin']).
Each hanzi key is verified as a substring of the authoritative data/zh/ch38.txt
so a Write-tool CJK mangling cannot slip a corrupted key into the glossary.

B31 = ch38 (第六章 曲直分明 反复无常, the sixth Part-Four narrative chapter, the
Zhu Zhankui defection-and-betrayal case). Most of the furniture is already keyed
(朱占奎 Zhu Zhankui, 常绍曾 Chang Shaozeng, 李玉林, 刘原深, 刘培初, 郑介民, 张炎元,
吕正操 Lü Zhengcao, 贺龙 He Long, 林彪, 陶铸, 聂荣臻, 江田; 绥靖总队, 中央训练团,
华北剿匪总司令部, 平津保三角地带; 绥靖/戡乱/剿匪/匪谍/共酋/共干; 石家庄, 安国, 大兴,
安次, 立水桥, 冀东, Beiping/Tianjin). New keyed rows are the three assault-team
commanders whose accounts fill the chapter, the tragic Second-Command-Room staff
officer, the Communist general Xiao Ke, and the towns of the Jin-Pu-line theatre
that recur across sections two through four.

New keyed rows:
  汪鸿翥   Wang Hongzhu  — first commander of the directly subordinate assault team;
                          author of the section-2 account of its forming and battles.
  吴春祥   Wu Chunxiang  — third commander of the assault team; author of the
                          section-4 account of the march and withdrawal at Wangqingtuo.
  谷守林   Gu Shoulin    — staff officer of the Second Command Room; the man who, sent
                          to Hong Kong on mainland work in 1951, lost his reason and
                          vanished — Chen's most painful memory of the chapter.
  萧克     Xiao Ke       — He Long's deputy in the 120th Division; the Communist
                          general to whose forces Zhu Zhankui was sent after 1945.
  王庆沱   Wangqingtuo   — the town west of Yangliuqing garrisoned by Zhu Zhankui's
                          security corps; it fell to the bandits the night the team left.
  杨柳青   Yangliuqing   — the town near Tianjin to which the Second Command Room fell
                          back on the northern reach of the Jin-Pu line.
  独流     Duliu         — the Jin-Pu-line station where the assault team detrained and
                          awaited orders; a Second-Command-Room group was stationed there.
  静海     Jinghai       — the Hebei county on the Jin-Pu line where the Second Command
                          Room was seated (at Tangguantun / the county town).
  顺义     Shunyi        — the county north of Beiping where the assault team broke up a
                          puppet commissar and an arms-repair shop in the autumn of 1948.
  唐官屯   Tangguantun   — the Jin-Pu-line town in Jinghai where the assault-team charge
                          was handed over and a Second-Command-Room group was stationed.

Rendered INLINE, NOT keyed (glossary-key discipline — one-off account-authors,
subordinate officers, the district-company commanders, and one-mention villages):
王志毅 Wang Zhiyi (the 'Story of Zhu Zhankui' author), 董英 Dong Ying (the sham
commissioner), 任卓宣 Ren Zhuoxuan, 徐佛观 Xu Foguan, 张鲁颖 Zhang Luying, 李长清 Li
Changqing, 徐立德 Xu Lide, 杨士毅 Yang Shiyi, 窦玉麟 Dou Yulin, 张保权 Zhang Baoquan,
贾叔铭 Jia Shuming, 赵濶亭 Zhao Kuoting, 李葆章/李保章 Li Baozhang (source spells it two
ways), 张侗夫 Zhang Tongfu, 陈俊祥 Chen Junxiang, 任德勤 Ren Deqin, 赵子侠 Zhao Zixia,
王维宁 Wang Weining, 吴玉林 Wu Yulin, 刘纯熙 Liu Chunxi, 张麟阁 Zhang Linge, 马钟麟 Ma
Zhonglin, 孙守义 Sun Shouyi, 刘楚枫 Liu Chufeng, 张培植 Zhang Peizhi, 汪鸿骏 Wang Hongjun
(distinct from 汪鸿翥); the Communist commander 刘伯承 Liu Bocheng; the training-camp
figures 中野 Nakano. Villages/places inline: 五重山 Wuchongshan, 白房村 Baifang, 牛栏山
Niulanshan, 赵家寨子 Zhaojiazhaizi, 王家庄子 Wangjiazhuangzi, 青王庄 Qingwangzhuang, 唐二里/
汤二里 Tang'erli, 昌平 Changping, 永清 Yongqing, 固安 Gu'an, 沧县 Cang county, 德县/德州
De county / Dezhou, 清河镇 Qinghe, 南苑 Nanyuan, 喜峰口 Xifengkou, 都山 Dushan, 明孝陵
Ming Xiaoling; the provinces and rail lines render inline per the settled conventions."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOSS = os.path.join(ROOT, "glossary.json")
ZH = os.path.join(ROOT, "data", "zh", "ch38.txt")

ADDS = {
    "people": {
        "汪鸿翥": {
            "en": "Wang Hongzhu",
            "pinyin": "Wang Hongzhu",
            "status": "provisional",
            "note": "First commander of the First Brigade's directly subordinate "
                    "assault team; author of the account quoted in section two of the "
                    "team's forming and its battles about Beiping and Tianjin.",
        },
        "吴春祥": {
            "en": "Wu Chunxiang",
            "pinyin": "Wu Chunxiang",
            "status": "provisional",
            "note": "Third commander of the directly subordinate assault team; author "
                    "of the section-four account of the march and withdrawal between "
                    "Yangliuqing, Wangqingtuo, and Tang'erli on the night Zhu Zhankui defected.",
        },
        "谷守林": {
            "en": "Gu Shoulin",
            "pinyin": "Gu Shoulin",
            "status": "provisional",
            "note": "Staff officer of the Second Command Room, who called with Chang "
                    "Shaozeng upon Zhu Zhankui; sent by Chen to Hong Kong on mainland "
                    "work in 1951, he lost his reason and vanished without trace.",
        },
        "萧克": {
            "en": "Xiao Ke",
            "pinyin": "Xiao Ke",
            "status": "attested",
            "note": "He Long's deputy as commander of the 120th Division of the Eighth "
                    "Route Army; the senior Communist commander in the Hebei-Rehe border "
                    "region to whose forces Zhu Zhankui was sent after 1945.",
        },
    },
    "places": {
        "王庆沱": {
            "en": "Wangqingtuo",
            "pinyin": "Wangqingtuo",
            "status": "decided",
            "note": "The town some fifteen li west of Yangliuqing garrisoned by Zhu "
                    "Zhankui's security corps; it fell to the bandit army on the night "
                    "the assault team and the Second Command Room withdrew from it.",
        },
        "杨柳青": {
            "en": "Yangliuqing",
            "pinyin": "Yangliuqing",
            "status": "decided",
            "note": "The town on the northern reach of the Jin-Pu railway near Tianjin "
                    "to which the Second Command Room fell back as the working district "
                    "shifted ever northward.",
        },
        "独流": {
            "en": "Duliu",
            "pinyin": "Duliu",
            "status": "decided",
            "note": "The Jin-Pu-line station where the assault team detrained and "
                    "awaited orders; the Second Command Room's Second Group was seated there.",
        },
        "静海": {
            "en": "Jinghai",
            "pinyin": "Jinghai",
            "status": "decided",
            "note": "The Hebei county on the northern reach of the Jin-Pu railway where "
                    "the Second Command Room was seated.",
        },
        "顺义": {
            "en": "Shunyi",
            "pinyin": "Shunyi",
            "status": "decided",
            "note": "The county north of Beiping where the assault team, in the autumn "
                    "of 1948, seized a puppet county commissar and broke up an "
                    "arms-repair shop at Niulanshan.",
        },
        "唐官屯": {
            "en": "Tangguantun",
            "pinyin": "Tangguantun",
            "status": "decided",
            "note": "The town in Jinghai county on the Jin-Pu line where the assault-team "
                    "command was handed from Wang Hongzhu to Chang Shaozeng, and where "
                    "the Second Command Room's Third Group was stationed.",
        },
    },
}


def main():
    zh = open(ZH, encoding="utf-8").read()
    for sect, rows in ADDS.items():
        for hanzi in rows:
            assert hanzi in zh, "key not in data/zh/ch38.txt: %s" % hanzi
    g = json.load(open(GLOSS, encoding="utf-8"))
    added = 0
    for sect, rows in ADDS.items():
        g.setdefault(sect, {})
        for hanzi, row in rows.items():
            if hanzi in g[sect]:
                continue
            g[sect][hanzi] = row
            added += 1
    json.dump(g, open(GLOSS, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("added %d new rows" % added)
    g2 = json.load(open(GLOSS, encoding="utf-8"))
    for sect, rows in ADDS.items():
        for hanzi, row in rows.items():
            assert g2[sect][hanzi]["en"] == row["en"], hanzi
            assert "pinyin" in g2[sect][hanzi], hanzi
    print("re-read verify OK")


if __name__ == "__main__":
    main()
