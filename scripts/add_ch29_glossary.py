#!/usr/bin/env python3
"""Add ch29's new glossary rows BY HAND into the sectioned glossary.json.
Idempotent; every row carries a pinyin field (qc_entities does rec['pinyin']).
Each hanzi key is verified as a substring of the authoritative data/zh/ch29.txt
so a Write-tool CJK mangling cannot slip a corrupted key into the glossary.

ch29 (祸不单行 柱折梁摧(上)) is the disaster chapter: Chen's narration frames
Liu Yuanshen's first-person memoir of taking over the First Action Brigade and
walking into the Zhou Xiyuan / Zhu Min trap. Most recurring cast is already
keyed (Zhang Xiaolin / Fu Xiao'an / Nie Chonghou / Hu Yongquan / Liu Junqing /
Zhang Zuoxing / Liu Yuanshen / Qi Qingbin / Chen Gongshu / Dai Li / Zhou Weilong /
Zhao Lijun / Wang Tianmu / Zheng Xiuyuan / Wan Lilang / Wang Jingwei). Seven new
keyed rows, all central to the trap-narrative and recurring (into ch30):

  周西垣   Zhou Xiyuan  — the turned third-sub-brigade leader; the trap that takes
        Liu Yuanshen. Renders "Zhou Xiyuan" everywhere.
  冯贤     Feng Xian    — Zhou Xiyuan's cover name; the source uses it deliberately
        (此人名叫冯贤(周西垣的化名)), so it renders "Feng Xian", NOT "Zhou Xiyuan".
  朱敏     Zhu Min      — Zhou's unit secretary and informant, the memoir's foil.
  刘全德   Liu Quande   — first-sub-brigade leader (ex-Ruijin "Little Red Devil").
  相强伟   Xiang Qiangwei — second-sub-brigade leader.
  骆成金   Luo Chengjin — Xiang's deputy (Hangzhou Police Academy; tortured at No.76).
  许力求   Xu Liqiu     — director of Wang Jingwei's Hong Kong South China Evening
        News; the sanction target Zhou dangles as bait.

Rendered INLINE, NOT keyed (glossary-key discipline — one-off roster names, a
one-off doctor, the bureau personnel): 祝慎之 Zhu Shenzhi (the pediatrician);
the classmate roster 唐与元 Tang Yuyuan / 张学礼 Zhang Xueli / 张毓檀 Zhang Yutan /
吴菊生 Wu Jusheng / 杨继志 Yang Jizhi / 张维贤 Zhang Weixian and the martyred party
狄玺庭 Di Xiting / 李玉顺 Li Yushun / 刘士愚 Liu Shiyu / 丁履敬 Ding Lüjing; the
bureau personnel officers 李肖白 Li Xiaobai / 周康 Zhou Kang; the Wuhan-internship
staff 刘培初 Liu Peichu / 张树勋 Zhang Shuxun / 陈仙洲 Chen Xianzhou (董威 Dong Wei
already inline from B22); the maidservants 赵妈 Amah Zhao / 彩爱 Cai'ai. The
periodical 南华晚报 (South China Evening News) is a footnote, not a key. Places
render per the settled convention (Avenue Joffre, Route Vallon, Route Delastre,
Rue du Consulat, Seymour Road, Bubbling Well Road, Nanking Road, Xi'aixiansi
Road, Baxianqiao, Fourth Avenue, Xiafei Lane; Chengdu, Changsha, Ruijin,
Wuhan, Hankou, Nanjing, Hong Kong, Jinhua, Wenzhou, Jiaxing, Sheng County,
Hangzhou)."""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOSS = os.path.join(ROOT, "glossary.json")
ZH = os.path.join(ROOT, "data", "zh", "ch29.txt")
zh_text = open(ZH, encoding="utf-8").read()

PEOPLE = {
    "周西垣": {"en": "Zhou Xiyuan", "pinyin": "Zhōu Xīyuán", "status": "provisional",
             "note": "The third-sub-brigade leader of the First Action Brigade, "
                     "turned by Wan Lilang; the trap through which Liu Yuanshen was "
                     "taken. Cover name 冯贤 (Feng Xian), keyed separately."},
    "冯贤": {"en": "Feng Xian", "pinyin": "Féng Xián", "status": "provisional",
           "note": "Cover name of Zhou Xiyuan; the source uses it as such "
                   "(此人名叫冯贤(周西垣的化名)), so it renders 'Feng Xian', not "
                   "'Zhou Xiyuan'."},
    "朱敏": {"en": "Zhu Min", "pinyin": "Zhū Mǐn", "status": "provisional",
           "note": "Zhou Xiyuan's unit secretary and the informant who denounced "
                   "him; the foil of Liu Yuanshen's memoir."},
    "刘全德": {"en": "Liu Quande", "pinyin": "Liú Quándé", "status": "provisional",
             "note": "First-sub-brigade leader, a Jiangxi man and former Ruijin "
                     "'Little Red Devil'; killed in Shanghai after the government "
                     "moved to Taiwan."},
    "相强伟": {"en": "Xiang Qiangwei", "pinyin": "Xiàng Qiángwěi", "status": "provisional",
             "note": "Second-sub-brigade leader, a man of Sheng County in Zhejiang."},
    "骆成金": {"en": "Luo Chengjin", "pinyin": "Luò Chéngjīn", "status": "provisional",
             "note": "Xiang Qiangwei's deputy, out of the Hangzhou Police Academy; "
                     "tortured on the tiger bench at No. 76 without confessing."},
    "许力求": {"en": "Xu Liqiu", "pinyin": "Xǔ Lìqiú", "status": "provisional",
             "note": "Director of the South China Evening News, Wang Jingwei's "
                     "Hong Kong propaganda organ; the sanction target Zhou Xiyuan "
                     "dangles as bait."},
}


def main():
    gl = json.load(open(GLOSS, encoding="utf-8"))
    added = 0
    for k, v in PEOPLE.items():
        if k not in zh_text:
            sys.exit("KEY NOT IN data/zh (possible mangling): %r" % k)
        if k in gl["people"]:
            if gl["people"][k].get("en") != v["en"]:
                sys.exit("CONFLICT: %s already keyed to %r" % (k, gl["people"][k]))
            continue
        gl["people"][k] = v
        added += 1
    json.dump(gl, open(GLOSS, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("added %d ch29 glossary rows" % added)


if __name__ == "__main__":
    main()
