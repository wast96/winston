#!/usr/bin/env python3
"""Add B30's new keyed glossary rows BY HAND into the sectioned glossary.json.
Idempotent; every row carries a pinyin field (qc_entities does rec['pinyin']).
Each hanzi key is verified as a substring of the authoritative data/zh/ch37.txt
so a Write-tool CJK mangling cannot slip a corrupted key into the glossary.

B30 = ch37 (第五章 兵连祸结 民不聊生, the fifth Part-Four narrative chapter). Most of
the Part-Four furniture is already keyed (特种部队/特种组织; 绥靖总队; 军统; 保密局;
华北剿匪总司令部; 抗日杀奸团; 复兴社; 青帮; 忠义救国军; 绥靖/戡乱/剿匪/匪谍; 石家庄/石门;
李玉林/傅作义/聂荣臻/王文/王克敏/刘少奇/萧润宇/牛广金/郑恩普; 安定门/西直门; Beiping/
Tianjin). 常绍曾 was inline (one mention) in ch36; here it is the North-Suburb Group
leader and the author of three quoted accounts, so it graduates to a key.

New keyed rows — distinctive proper nouns / historical figures / place names that
render ONE way and recur through the chapter (the fall of Shimen, and the Battle of
Lishuiqiao):

  常绍曾   Chang Shaozeng — leader of the North-Suburb Mixed Group (later the West-
                            Suburb Group); a Japanese-Military-Academy graduate and
                            once Chen's own pupil; author of three quoted accounts.
  田英杰   Tian Yingjie   — squad leader of the North-Suburb intelligence squad, the
                            "Captain Tian" of the Battle of Lishuiqiao; author of the
                            quoted first-person battle narrative.
  卢德明   Lu Deming      — directly-subordinate member attached to the Field HQ unit
                            at Shimen; author of the quoted account of Shimen's fall.
  刘子元   Liu Ziyuan     — commander of the Daxing county self-defense brigade at
                            Lishuiqiao; a former follower of the Loyal and Patriotic Army.
  冯玉柱   Feng Yuzhu     — Chang Shaozeng's successor as North-Suburb Group leader;
                            went into the city to summon the relief on the battle night.
  王抚洲   Wang Fuzhou    — a.k.a. Wang Zhenwu; Young China Party man who ran the Third
                            Route Army in Shandong; later a vice-minister in Taiwan.
  白家祺   Bai Jiaqi      — Lieutenant Colonel, brigade-attached; author of the Hong
                            Kong "Guohun" piece whose song opens the Lishuiqiao section.
  杜心吾   Du Xinwu       — the famed martial artist of Cili, Hunan (his name properly
                            written 杜心五); "dragon head" in the Hongmen and a senior
                            of the Green Gang, under whom Chen and Cheng Yanqiu studied.
  程艳秋   Cheng Yanqiu   — the great Peking-opera dan (also written 程砚秋), one of the
                            Four Great Dan; here Chen's fellow "disciple" under Du Xinwu.
  立水桥   Lishuiqiao     — the Daxing-county village, some thirty li north of Beiping's
                            Andingmen, scene of the October 1948 night battle.
  大兴     Daxing         — the Hebei county north of Beiping into which the North-
                            Suburb Group's work extended; Lishuiqiao lay within it.
  赵家坟   Zhaojiafen     — the base village of the North-Suburb Group, at the
                            northeastern corner of Beiping.

Rendered INLINE, NOT keyed (glossary-key discipline — one-off roster/officer/memoir
names, standard historical one-mention figures, standard place-names): the Shimen
defenders 罗历戎 Luo Lirong, 李文定 Li Wending, 刘英 Liu Ying, 刘清池 Liu Qingchi,
赵劲军 Zhao Jinjun, 侯子固 Hou Zigu; the Communist figures 杨得志 Yang Dezhi, 杨成武
Yang Chengwu, 刘伯承 Liu Bocheng, 杨秀峰 Yang Xiufeng, 薄一波 Bo Yibo, 黄敬/俞启威 Huang
Jing / Yu Qiwei; Chang Shaozeng's training-class roster 钱致伦/王忠/尹东耕/阎尚新; the
Ninth-Route staff 齐庆斌 Qi Qingbin, 张克新 (张作兴) Zhang Kexin, 陈肇基 Chen Zhaoji,
骆永康 Luo Yongkang; the Lishuiqiao-night names 米仁甫 Mi Renfu, 马良知 Ma Liangzhi,
李志达 Li Zhida, 路焕仲 Lu Huanzhong, and the grooms 庄飞/杨天铎/张岳生; 王镇吾 (Wang
Fuzhou's alt name); 白世维 Bai Shiwei. Villages/places render inline: 望都 Wangdu,
北湖渠 Beihuqu, 仰山 Yangshan, 昌平 Changping, 怀柔 Huairou, 北苑 Beiyuan, 路家坟
Lujiafen, 勇士营 Yongshiying, 羊房 Yangfang, 白家坟 Baijiafen, 谢格庄 Xiegezhuang,
林南仓 Linnancang, 宝坻 Baodi, 玉田 Yutian, 平原 Pingyuan, 禹城 Yucheng, 德州 Dezhou,
海淀 Haidian, 门头沟 Mentougou, 西山 Western Hills, 万寿山 Wanshou Hill, 八达岭 Badaling,
十三陵 the Ming Tombs, 府学胡同/东观音寺胡同/沈篦子胡同/煤渣胡同 (the Beiping lanes),
东直门 Dongzhimen; and the provinces render inline per the settled conventions."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOSS = os.path.join(ROOT, "glossary.json")
ZH = os.path.join(ROOT, "data", "zh", "ch37.txt")

ADDS = {
    "people": {
        "常绍曾": {
            "en": "Chang Shaozeng",
            "pinyin": "Chang Shaozeng",
            "status": "provisional",
            "note": "Leader of the North-Suburb Mixed Group and afterward the West-"
                    "Suburb Group; a graduate of the Japanese Military Academy and "
                    "once Chen's own pupil; author of three accounts quoted in section two.",
        },
        "田英杰": {
            "en": "Tian Yingjie",
            "pinyin": "Tian Yingjie",
            "status": "provisional",
            "note": "Squad leader of the North-Suburb intelligence squad, the "
                    "'Captain Tian' of the Battle of Lishuiqiao; author of the quoted "
                    "first-person account of that night's fight and break-out.",
        },
        "卢德明": {
            "en": "Lu Deming",
            "pinyin": "Lu Deming",
            "status": "provisional",
            "note": "A directly-subordinate member attached to the Beiping Field "
                    "Headquarters' unit at Shimen; author of the quoted account of "
                    "the Communist assault on and capture of Shimen.",
        },
        "刘子元": {
            "en": "Liu Ziyuan",
            "pinyin": "Liu Ziyuan",
            "status": "provisional",
            "note": "Commander of the Daxing county self-defense brigade at "
                    "Lishuiqiao; a former follower of the North China Loyal and "
                    "Patriotic Army.",
        },
        "冯玉柱": {
            "en": "Feng Yuzhu",
            "pinyin": "Feng Yuzhu",
            "status": "provisional",
            "note": "Chang Shaozeng's successor as leader of the North-Suburb Group; "
                    "on the battle night he went into Beiping to lay the urgent report "
                    "and summon the cavalry relief.",
        },
        "王抚洲": {
            "en": "Wang Fuzhou",
            "pinyin": "Wang Fuzhou",
            "status": "provisional",
            "note": "Also called Wang Zhenwu; a Young China Party man who ran the "
                    "Third Route Army of the Loyal and Patriotic Army in Shandong, a "
                    "National Assembly delegate, later a vice-minister of economic "
                    "affairs in Taiwan.",
        },
        "白家祺": {
            "en": "Bai Jiaqi",
            "pinyin": "Bai Jiaqi",
            "status": "provisional",
            "note": "A lieutenant colonel, brigade-attached; author of the piece 'The "
                    "Battle of Moxingling' in the Hong Kong magazine Guohun, whose "
                    "verse opens the Lishuiqiao section.",
        },
        "杜心吾": {
            "en": "Du Xinwu",
            "pinyin": "Du Xinwu",
            "status": "provisional",
            "note": "The renowned martial artist of Cili in Hunan (his name properly "
                    "written 杜心五); 'dragon head' of the Hongmen's Qixia Mountain "
                    "lodge and a senior of the Green Gang, under whom Chen and Cheng "
                    "Yanqiu were briefly enrolled as disciples.",
        },
        "程艳秋": {
            "en": "Cheng Yanqiu",
            "pinyin": "Cheng Yanqiu",
            "status": "provisional",
            "note": "The great Peking-opera dan (his stage name also written 程砚秋), "
                    "one of the 'Four Great Dan'; here Chen's fellow 'disciple' under "
                    "Du Xinwu, who in 1947-48 pressed Chen to intercede for detainees.",
        },
    },
    "places": {
        "立水桥": {
            "en": "Lishuiqiao",
            "pinyin": "Lìshuǐqiáo",
            "status": "decided",
            "note": "The Daxing-county village, some thirty li north of Beiping's "
                    "Andingmen, named for its cement bridge; scene of the October "
                    "1948 night battle between the local corps and the Communist militia.",
        },
        "大兴": {
            "en": "Daxing",
            "pinyin": "Dàxìng",
            "status": "decided",
            "note": "The Hebei county north of Beiping into which the North-Suburb "
                    "Group extended its pacification work; Lishuiqiao lay within it.",
        },
        "赵家坟": {
            "en": "Zhaojiafen",
            "pinyin": "Zhàojiāfén",
            "status": "decided",
            "note": "The base village of the North-Suburb Mixed Group, at the "
                    "northeastern corner of Beiping.",
        },
    },
}


def main():
    zh = open(ZH, encoding="utf-8").read()
    for sect, rows in ADDS.items():
        for hanzi in rows:
            assert hanzi in zh, "key not in data/zh/ch37.txt: %s" % hanzi
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
    # re-read verify
    g2 = json.load(open(GLOSS, encoding="utf-8"))
    for sect, rows in ADDS.items():
        for hanzi, row in rows.items():
            assert g2[sect][hanzi]["en"] == row["en"], hanzi
            assert "pinyin" in g2[sect][hanzi], hanzi
    print("re-read verify OK")


if __name__ == "__main__":
    main()
