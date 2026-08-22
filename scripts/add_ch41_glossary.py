#!/usr/bin/env python3
"""Add B34's new keyed glossary rows BY HAND into the sectioned glossary.json.
Idempotent; every row carries a pinyin field (qc_entities does rec['pinyin']).
Each hanzi key is verified as a substring of the authoritative data/zh/ch41.txt
so a Write-tool CJK mangling cannot slip a corrupted key into the glossary.

B34 = ch41 (第九章 痛定思痛 来者可追, the ninth Part-Four narrative chapter: the
brigade's move south to its dissolution at Penghu, the fall of Tianjin and
Beiping, the besieged-city street scenes of Chen's hometown, and the final
flight out with Zheng Jiemin). Most of the furniture is already keyed (傅作义 Fu
Zuoyi, 林彪 Lin Biao, 聂荣臻 Nie Rongzhen, 罗荣桓 Luo Ronghuan, 郑介民 Zheng Jiemin,
李玉林 Li Yulin, 刘原深 Liu Yuanshen, 张鲁颖 Zhang Luying, 常绍曾 Chang Shaozeng,
王兆芬 Wang Zhaofen, 汪鸿翥 Wang Hongzhu, 孙兰峰 Sun Lanfeng, 郭景云 Guo Jingyun,
安春山 An Chunshan, 齐庆斌 Qi Qingbin, 朱占奎 Zhu Zhankui, 徐永昌 Xu Yongchang, 叶剑英
Ye Jianying; 塘沽 Tanggu, 张家口 Zhangjiakou, 新保安 Xinbao'an, 杨柳青 Yangliuqing,
冀东 East Hebei, 西直门 Xizhimen).

New keyed rows are the three Nationalist commanders central to the fall-of-
Beiping-Tianjin narrative and, above all, to the chapter's ending. 邓宝珊
graduates from inline (rendered "Deng Baoshan" once in ch36) to a key as the last
seven paragraphs turn on him — the "deputy commander-in-chief" who brokered Fu's
surrender and who never boards the plane. 陈长捷 and 侯镜如 first appear here and
recur across the Tianjin and Tanggu passages of section two.

New keyed rows:
  邓宝珊  Deng Baoshan  — old general of the Northwest Army; a deputy commander-in-
                         chief of the North China Bandit-Suppression Headquarters,
                         Fu Zuoyi's secret negotiating representative, and (proved
                         afterward) the go-between for Fu's surrender to the
                         Communists; fails to board Zheng Jiemin's plane out.
  陈长捷  Chen Changjie — Tianjin garrison commander; trusting the city's ring of
                         blockhouses, he refused the counsel to break out to Tanggu,
                         fought a month, and was taken alive when the bandits broke
                         into the Garrison Command.
  侯镜如  Hou Jingru    — commander of the Seventeenth Army Group, holding the
                         "Jin-Gu Defense Zone"; carried out the sea withdrawal of the
                         Tanggu main force, thirty-six thousand-odd men, to Qingdao.

Rendered INLINE, NOT keyed (glossary-key discipline — one-mention roster
commanders, one-passage figures, name-lists, cross-referenced Part-One kin, and
one-chapter places): 周北峰 Zhou Beifeng, 李文 Li Wen, 骆振韶 Luo Zhenshao, 袁朴 Yuan
Pu, 黄翔 Huang Xiang, 李士林 Li Shilin, 林伟俦 Lin Weichou, 刘云瀚 Liu Yunhan, 王治熙
Wang Zhixi, 段沄 Duan Yun, 朱致一 Zhu Zhiyi (the defense-zone roster); 张树德 Zhang
Shude, 张廷谔 Zhang Ting'e, 江韵清 Jiang Yunqing, 江灏 Jiang Hao, 江振寰 Jiang Zhenhuan
(the Qi-Qingbin sub-story and its Part-One kin, rendered as in ch06/ch35); 张荫梧
Zhang Yinwu, 许惠东 Xu Huidong, 何思源 He Siyuan, 吕复 Lü Fu, 康同璧 Kang Tongbi, 刘鸿瑞
Liu Hongrui, 郭树棠 Guo Shutang (the peace-movement name-list); 邹仪 Zou Yi, 魏宁 Wei
Ning, 林立 Lin Li, 毛一鹭 Mao Yilu, 冯志俊 Feng Zhijun (comrades); 傅泾波 Fu Jingbo, 司徒
雷登 John Leighton Stuart, 李秋生 Li Qiusheng (one-mention). Places inline: 上海
Shanghai, 绍兴 Shaoxing, 宁波 Ningbo, 厦门 Xiamen, 海澄 Haicheng, 漳州 Zhangzhou, 澎湖
Penghu, 青岛 Qingdao, 太原 Taiyuan, 大同 Datong; 杨村 Yangcun, 豆张庄 Douzhangzhuang,
喜峰口 Xifengkou, 山海关 Shanhaiguan, 冷口 Lengkou, 唐山 Tangshan, 芦台 Lutai, 军粮城
Junliangcheng, 张贵庄 Zhangguizhuang; the Beiping gates and landmarks (崇文门
Chongwenmen, 宣武门 Xuanwumen, 天坛 the Temple of Heaven, 东来顺 Donglaishun, etc.).
张垣 stays the whole-book reconciliation item (rendered "Zhangyuan" here)."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOSS = os.path.join(ROOT, "glossary.json")
ZH = os.path.join(ROOT, "data", "zh", "ch41.txt")

ADDS = {
    "people": {
        "邓宝珊": {
            "en": "Deng Baoshan",
            "pinyin": "Deng Baoshan",
            "status": "provisional",
            "note": "An old general of the Northwest Army and a deputy commander-in-"
                    "chief of the North China Bandit-Suppression Headquarters, with no "
                    "troops under his own hand; Fu Zuoyi's secret negotiating "
                    "representative to Lin Biao, and (as was afterward proved) the "
                    "go-between who brokered Fu's surrender to the Communists. He "
                    "failed to board Zheng Jiemin's plane out of Beiping. Rendered "
                    "inline in ch36; keyed here.",
        },
        "陈长捷": {
            "en": "Chen Changjie",
            "pinyin": "Chen Changjie",
            "status": "provisional",
            "note": "Commander of the Tianjin garrison. Trusting the city's ring of "
                    "blockhouses and holding that he could last three or four months, "
                    "he refused the Ministry of National Defense's counsel to break "
                    "out to Tanggu and pass on to Qingdao; he fought a month, and was "
                    "taken alive when the bandits broke into the Garrison Command on "
                    "the fifteenth of the first month.",
        },
        "侯镜如": {
            "en": "Hou Jingru",
            "pinyin": "Hou Jingru",
            "status": "provisional",
            "note": "Commander of the Seventeenth Army Group, holding the 'Jin-Gu "
                    "Defense Zone' (both the Tianjin and the Tanggu sub-zones). On "
                    "orders to withdraw after Tianjin fell, he carried out the sea "
                    "withdrawal of the Tanggu main force, thirty-six thousand-odd men, "
                    "to Qingdao.",
        },
    },
}


def main():
    zh = open(ZH, encoding="utf-8").read()
    for sect, rows in ADDS.items():
        for hanzi in rows:
            assert hanzi in zh, "key not in data/zh/ch41.txt: %s" % hanzi
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
