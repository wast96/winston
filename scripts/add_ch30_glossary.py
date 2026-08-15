#!/usr/bin/env python3
"""Add B24's new keyed glossary rows BY HAND into the sectioned glossary.json.
Idempotent; every row carries a pinyin field (qc_entities does rec['pinyin']).
Each hanzi key is verified as a substring of the authoritative data/zh/<id>.txt
so a Write-tool CJK mangling cannot slip a corrupted key into the glossary.

B24 = ch30 (第十章 下, the trap sprung + Liu's/Chen's capture) + ch31 (the
Part-Three closing errata note). Most recurring cast is already keyed (Zhou
Xiyuan / Zhu Min / Xu Liqiu / Wan Lilang / Liu Junqing / Nie Chonghou / Hu
Yongquan / Qi Qingbin / Zhang Zuoxing / Dai Li / Chen Gongshu; Qian Xinmin /
Jiang Anhua were keyed earlier; and in ch31 Geng Jiaji / Xu Shouxin / Yu Yanzhi
/ Zhou Xiliang / Yu Yefeng / Zhang Xiaolin / Lin Huaibu / Chen Gongbo / Xin
Yanqiu). Three new keyed rows, each recurring within ch30's capture narrative:

  褚亚鹏   Chu Yapeng    — ex-Beiping-station courier who ran the Bubbling Well
        Road electrical-shop liaison station; arrested and paraded to identify
        Chen at No. 76, but did not point him out. (~4 occurrences.)
  林焕芝   Lin Huanzhi   — the Cantonese-speaking action-section chief at No. 76,
        formerly of the Shanghai District Fourth Team; his brother 林镇城 Lin
        Zhencheng (kept inline, one-off) was of the Third Team. (~6 occurrences.)
  姜绍谟   Jiang Shaomo  — courtesy Cilie; Chief of the Shanghai Reserve District
        (the Second District), who had lain hidden and never been exposed, and
        who took over the Shanghai work after Chen's capture and carried it to
        the victory of the war of resistance.

Rendered INLINE, NOT keyed (glossary-key discipline — one-off names in a single
capture scene, or a French police contact / a foreign colleague): 仇淑英 Qiu
Shuying (internal-courier-station chief); 陈贤荣 Chen Xianrong and his cover
程远 Cheng Yuan (the District accountant) and his kinsman 孙国昌 Sun Guochang;
the three radio-station chiefs 秦尔同 Qin Ertong / 张湘南 Zhang Xiangnan / 顾汉卿
Gu Hanqing; 桂涤非 Gui Difei (personnel assistant secretary); 马隆/马龙 Malone
(the French police criminal-section chief and secret Shanghai District contact —
Liu spells it 马隆, Chen 马龙, one man); 克莱德 Clyde (a Settlement-police
colleague); 胡永安 Hu Yong'an (Hu Yongquan's brother); 阿平 A-ping (Qi's maid).
In ch31, all names are recurring-keyed or one-off inline (刘仲康 Liu Zhongkang,
李洪春 Li Hongchun, 梁慧超 Liang Huichao, 杨再兴 Yang Zaixing, 岳飞 Yue Fei,
随波 Suibo, 徐展 Xu Zhan). The variant 余廷智 (for keyed 余延智 Yu Yanzhi) renders
'Yu Yanzhi' inline. Places render per the settled convention (Avenue Joffre,
Joffre Terrace, Seymour Road, Sinza Road, Rue Bourgeat, Bubbling Well Road,
Jessfield Road; Hongkou, Zhabei, Chongqing, Chengdu, Nanjing, Qingdao, Subei/
northern Jiangsu)."""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOSS = os.path.join(ROOT, "glossary.json")
zh_ch30 = open(os.path.join(ROOT, "data", "zh", "ch30.txt"), encoding="utf-8").read()
zh_ch31 = open(os.path.join(ROOT, "data", "zh", "ch31.txt"), encoding="utf-8").read()
zh_all = zh_ch30 + zh_ch31

PEOPLE = {
    "褚亚鹏": {"en": "Chu Yapeng", "pinyin": "Chǔ Yàpéng", "status": "provisional",
             "note": "Formerly a courier of the Beiping station, transferred to "
                     "Shanghai; he ran an electrical shop on Bubbling Well Road as "
                     "a Shanghai District liaison station. Arrested a month before "
                     "Chen and brought to No. 76 to identify him, he did not point "
                     "Chen out."},
    "林焕芝": {"en": "Lin Huanzhi", "pinyin": "Lín Huànzhī", "status": "provisional",
             "note": "The Cantonese-speaking chief of the action section at No. 76, "
                     "formerly of the Shanghai District Fourth Team; his elder "
                     "brother Lin Zhencheng was of the Third Team."},
    "姜绍谟": {"en": "Jiang Shaomo", "pinyin": "Jiāng Shàomó", "status": "provisional",
             "note": "Courtesy name Cilie; Chief of the Shanghai Reserve District "
                     "(the Second District), who had lain concealed in Shanghai "
                     "without his identity being exposed, and who took over the "
                     "Shanghai work after Chen's capture and carried it on to the "
                     "victory of the war of resistance."},
}


def main():
    gl = json.load(open(GLOSS, encoding="utf-8"))
    added = 0
    for k, v in PEOPLE.items():
        if k not in zh_all:
            sys.exit("KEY NOT IN data/zh (possible mangling): %r" % k)
        if k in gl["people"]:
            if gl["people"][k].get("en") != v["en"]:
                sys.exit("CONFLICT: %s already keyed to %r" % (k, gl["people"][k]))
            continue
        gl["people"][k] = v
        added += 1
    json.dump(gl, open(GLOSS, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("added %d B24 glossary rows" % added)


if __name__ == "__main__":
    main()
