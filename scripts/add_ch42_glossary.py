#!/usr/bin/env python3
"""Add B35's new keyed glossary rows BY HAND into the sectioned glossary.json.
Idempotent; every row carries a pinyin field (qc_entities does rec['pinyin']).
Each hanzi key is verified as a substring of the authoritative data/zh/ch42.txt
so a Write-tool CJK mangling cannot slip a corrupted key into the glossary.

B35 = ch42 (第十章 落叶归根 善其始终, the tenth and LAST full Part-Four narrative
chapter: the disbanding of the Pacification Corps, the withdrawal of the
stay-behind men from besieged Beiping, the brigade's southward journey guarding
Chiang's home region at Xikou/Fenghua and its dissolution at Penghu, and Chen's
own post-1949 course through Hong Kong, Japan and back). Most of the furniture is
already keyed (郑介民 Zheng Jiemin, 李玉林 Li Yulin, 刘原深 Liu Yuanshen, 张鲁颖 Zhang
Luying, 汪鸿翥 Wang Hongzhu, 刘培初 Liu Peichu, 毛人凤 Mao Renfeng, 王兆芬 Wang Zhaofen,
常绍曾 Chang Shaozeng, 田英杰 Tian Yingjie, 萧润宇 Xiao Runyu, 吴春祥 Wu Chunxiang, 林彪
Lin Biao, 中岛信一 Nakajima Shin'ichi, 郑恩普 Zheng Enpu, 张炎元 Zhang Yanyuan, 连谋
Lian Mou; 塘沽 Tanggu, 张家口 Zhangjiakou, 乌兰华 Ulanhua).

New keyed rows: the account-author 冯志俊 graduates from inline (a one-mention
comrade in ch41) to a key, since the whole "Record of the Xiaolingfeng Garrison"
that anchors section 3 is his first-person account; and the five places central to
the southward journey and the guarding of Chiang's native place, each rendered one
way across every chapter it appears in (verified against the other chapters' data/zh
and their reading.md: Xikou, Fenghua, Xiaolingfeng, Penghu, Magong).

Rendered INLINE, NOT keyed (glossary-key discipline — one-mention men, name-lists,
one-passage figures, standard place names, and cross-referenced Part-One kin): 江田
Jiang Tian, 张作兴 Zhang Zuoxing (already keyed), 陶铸 Tao Zhu, 李运昌 Li Yunchang, 李鸣秋
Li Mingqiu, 聂恩俊 Nie Enjun, 白世维 Bai Shiwei, 孙时林 Sun Shilin, 何思源 He Siyuan, 刘不同
Liu Butong, 李浩昆 Li Haokun, 吴尙游 Wu Shangyou, 胡轨 Hu Gui, 梅长龄 Mei Changling, 马寿泉
Ma Shouquan, 黄文炳 Huang Wenbing, 李良荣 Li Liangrong, 乌瑞山 Wu Ruishan, 汤恩伯 Tang Enbo,
李振清 Li Zhenqing, 孙文良 Sun Wenliang, 唐纵 Tang Zong, 韩尙英 Han Shangying, 曹霄青 Cao
Xiaoqing, 渡边渡 Watanabe Wataru, 和知鹰二 Wachi Takaji, 根本博 Nemoto Hiroshi, and the
Xiaolingfeng small-group roster (刘迈青 etc.). Places inline: 上海 Shanghai, 南京 Nanjing,
杭州 Hangzhou, 宁波 Ningbo, 绍兴 Shaoxing, 厦门 Xiamen, 漳州 Zhangzhou, 泉州 Quanzhou, 长泰
Changtai, 岩溪 Yanxi, 林墩 Lindun, 青岛 Qingdao, 基隆 Keelung, 台北 Taipei, 台中 Taichung,
香港 Hong Kong, 台湾 Taiwan, 日本 Japan, 东京 Tokyo, 菲律宾 the Philippines, 泰国 Thailand,
北投 Beitou, 跑马地 Happy Valley, 惠安 Hui'an, 高雄 Kaohsiung, 白沙 Baisha, 蒋家 Jiangjia."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOSS = os.path.join(ROOT, "glossary.json")
ZH = os.path.join(ROOT, "data", "zh", "ch42.txt")

ADDS = {
    "people": {
        "冯志俊": {
            "en": "Feng Zhijun",
            "pinyin": "Feng Zhijun",
            "status": "provisional",
            "note": "A comrade of the First Brigade, in those days a little past "
                    "twenty and about the rank of lieutenant, later a retired major "
                    "general; the author of the first-person 'Record of the "
                    "Xiaolingfeng Garrison' that anchors this chapter's third "
                    "section. Rendered inline in ch41; keyed here.",
        },
    },
    "places": {
        "溪口": {
            "en": "Xikou",
            "pinyin": "Xikou",
            "status": "decided",
            "note": "Chiang Kai-shek's native town in Fenghua, Zhejiang; the "
                    "brigade's charge in the winter and spring of 1949 was to guard "
                    "its outer ring.",
        },
        "奉化": {
            "en": "Fenghua",
            "pinyin": "Fenghua",
            "status": "decided",
            "note": "The Zhejiang county that holds Xikou, Chiang's home place.",
        },
        "小灵峰": {
            "en": "Xiaolingfeng",
            "pinyin": "Xiaolingfeng",
            "status": "decided",
            "note": "A vital pass in the Siming Mountains on the outer ring of "
                    "Xikou, guarded by the brigade; the subject of Feng Zhijun's "
                    "garrison record.",
        },
        "澎湖": {
            "en": "Penghu",
            "pinyin": "Penghu",
            "status": "decided",
            "note": "The Pescadores; the island group to which the brigade withdrew "
                    "from Xiamen in September 1949 and where it was finally "
                    "disbanded.",
        },
        "马公": {
            "en": "Magong",
            "pinyin": "Magong",
            "status": "decided",
            "note": "The main harbor town of Penghu (the Pescadores), where the "
                    "brigade went ashore in September 1949.",
        },
    },
}


def main():
    zh = open(ZH, encoding="utf-8").read()
    for sect, rows in ADDS.items():
        for hanzi in rows:
            assert hanzi in zh, "key not in data/zh/ch42.txt: %s" % hanzi
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
