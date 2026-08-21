#!/usr/bin/env python3
"""Add B32's new keyed glossary rows BY HAND into the sectioned glossary.json.
Idempotent; every row carries a pinyin field (qc_entities does rec['pinyin']).
Each hanzi key is verified as a substring of the authoritative data/zh/ch39.txt
so a Write-tool CJK mangling cannot slip a corrupted key into the glossary.

B32 = ch39 (第七章 瞻前顾后 未雨绸缪, the seventh Part-Four narrative chapter:
battlefield-clearing after Laishui, Fu Zuoyi's vacillating strategy and the
destruction of the 35th Army at Xinbao'an, and the plan to move the unit south).
Much of the furniture is already keyed (傅作义 Fu Zuoyi, 聂荣臻 Nie Rongzhen, 林彪
Lin Biao, 郑介民 Zheng Jiemin, 李玉林 Li Yulin, 刘培初 Liu Peichu, 史泓 Shi Hong,
安春山 An Chunshan, 顾祝同 Gu Zhutong, 陈诚 Chen Cheng, 李宗仁 Li Zongren, 邓文仪
Deng Wenyi, 贺龙 He Long; 石家庄, 张家口 Zhangjiakou, 塘沽 Tanggu; 华北剿匪总司令部,
绥靖总队, 中央训练团, 励志训练班, 力行社; 特种部队, 特种组织, 平津保三角地带, 绥靖).

New keyed rows are the three account-authors central to the chapter's sections,
one more account-author, the recurring 35th-Army / 11th-Army-Group generals of
the Zhangyuan-Xinbao'an disaster, the two Zhuoxian-district commissioners of
section one, and the five recurring places of the pacification and Xinbao'an
narratives.

New keyed rows:
  王兆芬  Wang Zhaofen  — commanding officer of the First Command Room at Zhuoxian;
                         author of the long section-1 account of opening up the work.
  张鲁颖  Zhang Luying  — commanding officer of the Fifth Command Room at Zhangyuan;
                         author of the section-2 account of the Chahar-Suiyuan work.
  陈振山  Chen Zhenshan — commander of the Second (Northeast) Brigade; Chen's fellow
                         traveler to Nanjing, later lost in the Northeast fighting.
  孟广第  Meng Guangdi  — leader of the Baoding Group under the First Command Room;
                         author of the short Zhuoxian "Cleanse-the-Source" account.
  鲁英庆  Lu Yingqing   — commander of the 35th Army who took his own life at
                         Zhangfeidian in the Laishui campaign (source glitches the
                         name 鲁英尘 / 鲁英屡; one man).
  郭景云  Guo Jingyun   — commander of the 35th Army who took his own life at the fall
                         of Xinbao'an; the army's second commander to die by his hand.
  孙兰峰  Sun Lanfeng   — commander of the 11th Army Group garrisoning Zhangyuan;
                         broke out with heavy loss to reach Guisui.
  李铭鼎  Li Mingding   — division commander under Lu Yingqing who took his own life
                         first at Laishui.
  李中庸  Li Zhongyong  — administrative inspector-commissioner (probably the Second
                         district) who drew the First Command Room into training work.
  王凤岗  Wang Fenggang — the hard-driving commissioner of the "iron triangle"
                         district; died later in a Taiwan prison.

New keyed places:
  涿县    Zhuoxian      — the seat of the First Command Room; hub of section one.
  新保安  Xinbao'an     — the walled town on the Ping-Sui line where the 35th Army was
                         besieged and destroyed, 6-24 December 1948.
  涞水    Laishui       — the county and campaign (涞水之役) where the 35th Army bled
                         and its commanders died, and the coffins were requisitioned.
  保定    Baoding       — the Hebei provincial city; a district-group seat and a hub of
                         the Ping-Han-line pacification work.

Rendered INLINE, NOT keyed (glossary-key discipline — one-off officials, account
sub-figures, one-mention places, and figures already treated inline elsewhere):
王有声 Wang Yousheng (Zhuoxian magistrate), 张荫梧 Zhang Yinwu, 赵伯衡 Zhao Boheng,
孙祖义 Sun Zuyi, 崔老选 Cui Laoxuan / 崔万兴 Cui Wanxing, 赵百川 Zhao Baichuan (=赵明山,
"the Star Shell"), 陈凤桐 Chen Fengtong, 王志毅 Wang Zhiyi, 白德昭 Bai Dezhao and the
Mongol members 贡楚格策登 Gongchuge Ceden / 乌瑞山 Wu Ruishan / 仁亲道尔吉 Renqin Daorji
(and the 甘珠尔瓦呼图克图 Kanjurwa Khutukhtu), 孙文良 Sun Wenliang, 钟宁寿 Zhong Ningshou,
楚溪春 Chu Xichun, 何思源 He Siyuan / 刘瑶章 Liu Yaozhang, 范汉杰 Fan Hanjie, 王云孙 Wang
Yunsun, 杨予 Yang Yu, 魏宁 Wei Ning; the Communist commanders 刘伯承 Liu Bocheng, 陈毅
Chen Yi, 徐向前 Xu Xiangqian (kept inline). 张垣 Zhangyuan (the literary name of
Zhangjiakou; rendered "Zhangyuan" in ch39 with the in-text gloss "(Zhangjiakou in
Chahar)", but NOT keyed — ch08 already renders the same 张垣 as "Zhangjiakou," a
whole-book reconciliation item). Places inline: 宛平 Wanping, 小稻村
Xiaodaocun, 望都 Wangdu, 易县 Yixian, 多伦 Duolun, 宣化 Xuanhua, 怀安 Huai'an, 沙城
Shacheng, 万全 Wanquan, 柴沟堡 Chaigoubu, 下花园 Xiahuayuan, 通县 Tongxian, 丰台 Fengtai,
张飞店 Zhangfeidian, 南苑 Nanyuan, 归绥 Guisui, 包头 Baotou, 集宁 Jining, 大同 Datong,
太原 Taiyuan, 承德 Chengde, 葫芦岛 Huludao, 长春 Changchun, 济南 Jinan, 开封 Kaifeng,
唐山 Tangshan, 丰润 Fengrun, 昌黎 Changli, 秦皇岛 Qinhuangdao, 房山 Fangshan, 定兴
Dingxing, 满城 Mancheng, 大沽口 Dagu, 青岛 Qingdao, 香林寺 Xianglin Temple; the provinces
and rail lines render inline per the settled conventions."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOSS = os.path.join(ROOT, "glossary.json")
ZH = os.path.join(ROOT, "data", "zh", "ch39.txt")

ADDS = {
    "people": {
        "王兆芬": {
            "en": "Wang Zhaofen",
            "pinyin": "Wang Zhaofen",
            "status": "provisional",
            "note": "Commanding officer of the First Command Room, seated at Zhuoxian; "
                    "author of the long account quoted in section one of the opening-up "
                    "of the work and the aftermath of the Laishui campaign. (The source "
                    "glitches the surname 主兆芬 once; one man.)",
        },
        "张鲁颖": {
            "en": "Zhang Luying",
            "pinyin": "Zhang Luying",
            "status": "provisional",
            "note": "Commanding officer of the Fifth Command Room at Zhangyuan and later "
                    "brigade-adjutant for liaison to the North China Bandit-Suppression "
                    "Headquarters; author of the section-2 account of the Chahar-Suiyuan work.",
        },
        "陈振山": {
            "en": "Chen Zhenshan",
            "pinyin": "Chen Zhenshan",
            "status": "provisional",
            "note": "Commander of the Second Brigade in the Northeast; Chen's companion "
                    "on the journey to the Nanjing conference, with whom he made the "
                    "compact for a Northeast fallback. Lost in the Northeast fighting, "
                    "his fate never confirmed.",
        },
        "孟广第": {
            "en": "Meng Guangdi",
            "pinyin": "Meng Guangdi",
            "status": "provisional",
            "note": "Leader of the Baoding Group under the First Command Room; author of "
                    "the short account of the Zhuoxian 'Cleanliness and Hygiene' / "
                    "'Cleanse-the-Source, Root-Out-Traitors' movement.",
        },
        "鲁英庆": {
            "en": "Lu Yingqing",
            "pinyin": "Lu Yingqing",
            "status": "provisional",
            "note": "Commander of the 35th Army who, following his division commander Li "
                    "Mingding, took his own life at the Zhangfeidian station in the "
                    "Laishui campaign. The source misprints the given name as 鲁英尘 and "
                    "鲁英屡 elsewhere; one man.",
        },
        "郭景云": {
            "en": "Guo Jingyun",
            "pinyin": "Guo Jingyun",
            "status": "provisional",
            "note": "Successor commander of the 35th Army, who took his own life at the "
                    "fall of Xinbao'an on 24 December 1948 — the army's second commander "
                    "to die by his own hand for his country.",
        },
        "孙兰峰": {
            "en": "Sun Lanfeng",
            "pinyin": "Sun Lanfeng",
            "status": "provisional",
            "note": "Commander of the 11th Army Group garrisoning Zhangyuan; after the "
                    "destruction of the 35th Army he broke out in two columns, of whose "
                    "fifty thousand and more only a few thousand reached Guisui.",
        },
        "李铭鼎": {
            "en": "Li Mingding",
            "pinyin": "Li Mingding",
            "status": "provisional",
            "note": "Division commander under Lu Yingqing in the 35th Army; hampered by "
                    "the guarding of prisoners, his division met defeat at Laishui, and "
                    "he took his own life first.",
        },
        "李中庸": {
            "en": "Li Zhongyong",
            "pinyin": "Li Zhongyong",
            "status": "provisional",
            "note": "Administrative inspector-commissioner (probably of the Second "
                    "district), a former Chongqing colleague of Wang Zhaofen's, who drew "
                    "the First Command Room into training the district's administrative cadres.",
        },
        "王凤岗": {
            "en": "Wang Fenggang",
            "pinyin": "Wang Fenggang",
            "status": "provisional",
            "note": "The hard-driving anti-Communist commissioner whose district was "
                    "praised as the 'iron triangle of Beiping-Tianjin-Baoding'; he sought "
                    "out Wang Zhaofen for the pacification work and died later in a Taiwan prison.",
        },
    },
    "places": {
        "涿县": {
            "en": "Zhuoxian",
            "pinyin": "Zhuoxian",
            "status": "decided",
            "note": "The county southwest of Beiping on the Ping-Han line where the First "
                    "Command Room had its seat; the hub of section one and the place to "
                    "which Fu Zuoyi's requisitioned coffins were sent.",
        },
        "新保安": {
            "en": "Xinbao’an",
            "pinyin": "Xinbao'an",
            "status": "decided",
            "note": "The walled town on the Ping-Sui line, southeast of Xuanhua, where "
                    "Guo Jingyun's 35th Army was surrounded and destroyed between 6 and "
                    "24 December 1948.",
        },
        "涞水": {
            "en": "Laishui",
            "pinyin": "Laishui",
            "status": "decided",
            "note": "The Hebei county and the campaign (the 涞水之役) in which the 35th "
                    "Army bled, its commander and division commander took their lives, "
                    "and the mass encoffining of the dead was carried out.",
        },
        "保定": {
            "en": "Baoding",
            "pinyin": "Baoding",
            "status": "decided",
            "note": "The Hebei provincial city on the Ping-Han line; seat of the First "
                    "Command Room's Baoding Group and a hub of the line's pacification work.",
        },
    },
}


def main():
    zh = open(ZH, encoding="utf-8").read()
    for sect, rows in ADDS.items():
        for hanzi in rows:
            assert hanzi in zh, "key not in data/zh/ch39.txt: %s" % hanzi
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
