#!/usr/bin/env python3
"""Add B33's new keyed glossary rows BY HAND into the sectioned glossary.json.
Idempotent; every row carries a pinyin field (qc_entities does rec['pinyin']).
Each hanzi key is verified as a substring of the authoritative data/zh/ch40.txt
so a Write-tool CJK mangling cannot slip a corrupted key into the glossary.

B33 = ch40 (第八章 抚今追昔 烟波千里, the eighth Part-Four narrative chapter:
the fates of the three Tianjin men, Nie Rongzhen as the overlooked arch-enemy of
North China, the "stay-behind work" and Ji Zhaoxiang's martyrdom, and the string
of defeats from Jinzhou to the Xinbao'an-Miaofeng disaster). Most of the
furniture is already keyed (傅作义 Fu Zuoyi, 聂荣臻 Nie Rongzhen, 林彪 Lin Biao,
罗荣桓 Luo Ronghuan, 郑介民 Zheng Jiemin, 李玉林 Li Yulin, 刘原深 Liu Yuanshen,
毕高奎 Bi Gaokui, 计兆祥 Ji Zhaoxiang, 侯腾 Hou Teng, 史泓 Shi Hong, 安春山
An Chunshan, 郭景云 Guo Jingyun, 聂恩俊 Nie Enjun, 中岛信一 Nakajima Shin'ichi;
新保安 Xinbao'an, 保定 Baoding, 塘沽 Tanggu, 锦州 Jinzhou, 张家口 Zhangjiakou).

New keyed rows are the three Tianjin Intelligence Group men whose diverging fates
are the whole of section one, and the chart-draftsman comrade whose obituary
opens the seam of section two (already rendered "Hong Fuyu" inline in ch35, now
central here). 王智斌 and 郭子中 were rendered inline the same way in ch33/ch35;
they graduate to keys as section one turns on them. 齐枕萍 is keyed on the ch40
form (ch33/ch35 print the homophone 齐枕平, a different string; both render
"Qi Zhenping").

New keyed rows:
  王智斌  Wang Zhibin   — leader of the Tianjin Intelligence Group; the one of the
                         three who "took the crooked road," went over to the
                         Communists, and vanished in the Three-Anti purge (also
                         named 王紫斌 Wang Zibin).
  齐枕萍  Qi Zhenping   — group member; recommended by Chen to Zheng Jiemin's
                         "Central Second Section," served thirty years, died 1986.
  郭子中  Guo Zizhong   — group member; fled to Japan, was deported to the mainland.
  洪复予  Hong Fuyu     — the chart-and-table draftsman of the First Pacification
                         Brigade (and earlier of the Shanghai Station); died alone
                         and unmarried in Taiwan (also in ch35).

Rendered INLINE, NOT keyed (glossary-key discipline — one-off Communist officials,
one-mention historical commanders, name-lists, and one-chapter places): 许建国 Xu
Jianguo and 杨帆 Yang Fan (successive CCP Shanghai public-security directors), 中岛
Nakajima (already keyed in full), 廖耀湘 Liao Yaoxiang, 袁朴 Yuan Pu, 吴克华 Wu Kehua,
詹大南 Zhan Danan, 范汉杰 Fan Hanjie, 卢濬泉 Lu Junquan, 胡轨 Hu Gui, 孙龙光 Sun
Longguang, 李复生 Li Fusheng (all inline); the Communist commanders 朱德 Zhu De,
彭德怀 Peng Dehuai, 叶剑英 Ye Jianying, 徐向前 Xu Xiangqian, 杨成武 Yang Chengwu, 郭天民
Guo Tianmin, 黄永胜 Huang Yongsheng, 熊伯涛 Xiong Botao, 邓华 Deng Hua (name-list,
inline); 侯飞霞 Hou Feixia (the courtesy name of the keyed Hou Teng — same man,
inline); 张上校 Colonel Zhang (bare surname). Places inline: 胥各庄 Xugezhuang, 顺义
Shunyi, 密云 Miyun, 黄县 Huang county, 哈尔滨 Harbin, 沈阳 Shenyang, 太原 Taiyuan, 集宁
Jining, 康庄 Kangzhuang, 南口 Nankou, 昌平 Changping, 怀来 Huailai, 镇边城 Zhenbiancheng,
门头沟 Mentougou, 土木堡 Tumu Fort, 宋家营 Songjiaying, 妙峰山 the Miaofeng Mountains,
横岭 Hengling, 八达岭 Badaling, 青龙桥 Qinglong Bridge, 长春 Changchun, 葫芦岛 Huludao,
锦西 Jinxi, 宁波 Ningbo, 府学胡同 Fuxue Lane; the provinces and rail lines render inline
per the settled conventions. 张垣 stays the whole-book reconciliation item."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOSS = os.path.join(ROOT, "glossary.json")
ZH = os.path.join(ROOT, "data", "zh", "ch40.txt")

ADDS = {
    "people": {
        "王智斌": {
            "en": "Wang Zhibin",
            "pinyin": "Wang Zhibin",
            "status": "provisional",
            "note": "Leader of the 'Tianjin Intelligence Group'; a Northeast-born, "
                    "Japanese-educated former puppet interpreter who, of the three men "
                    "who set out together, 'took the crooked road,' was taken by the "
                    "Communists off the Shandong coast, went over to them, and vanished "
                    "after Yang Fan's purge. Also named 王紫斌 Wang Zibin.",
        },
        "齐枕萍": {
            "en": "Qi Zhenping",
            "pinyin": "Qi Zhenping",
            "status": "provisional",
            "note": "Member of the 'Tianjin Intelligence Group'; recommended by Chen to "
                    "the 'Central Second Section' under Zheng Jiemin, where he worked "
                    "thirty years, dying of illness in 1986. (Written 齐枕平 in the "
                    "earlier chapters; one man.)",
        },
        "郭子中": {
            "en": "Guo Zizhong",
            "pinyin": "Guo Zizhong",
            "status": "provisional",
            "note": "Member of the 'Tianjin Intelligence Group'; a Harbin-raised man of "
                    "a simpler, honester sort who fled to Japan and, unable to remain "
                    "when his papers ran out, was deported to the mainland.",
        },
        "洪复予": {
            "en": "Hong Fuyu",
            "pinyin": "Hong Fuyu",
            "status": "provisional",
            "note": "The draftsman of the First Pacification Brigade (earlier of the "
                    "Shanghai Station), who made the home-made enemy-order charts that "
                    "hung in the brigade-headquarters office; after his discharge he "
                    "worked decades in an advertising firm and died alone, unmarried, in "
                    "Taiwan.",
        },
    },
}


def main():
    zh = open(ZH, encoding="utf-8").read()
    for sect, rows in ADDS.items():
        for hanzi in rows:
            assert hanzi in zh, "key not in data/zh/ch40.txt: %s" % hanzi
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
