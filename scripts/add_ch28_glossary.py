#!/usr/bin/env python3
"""Add ch28's new glossary rows BY HAND into the sectioned glossary.json.
Idempotent; every row carries a pinyin field (qc_entities does rec['pinyin']).
Each hanzi key is verified as a substring of the authoritative data/zh/ch28.txt
so a Write-tool CJK mangling cannot slip a corrupted key into the glossary.

ch28 (声威大震血浪腥风) is the height-of-renown chapter: the Fu Xiao'an /
Zhu Sheng axe-killing in full, the two reproduced court-retrocession agreements,
the killing of the Frenchman Duluo, the puppet Central Reserve Bank sabotage,
and the No. 76 bloody reprisal. Almost all its recurring cast is already keyed
(Fu Xiao'an / Zhang Xiaolin / Lin Huaibu / Du Yuesheng / Zhou Fohai / Li Shiqun /
Chen Gongbo / Wang Jingwei / Zhao Sheng / Chen Mo / Qi Qingbin / Liu Yuanshen /
Huang Zhiyuan / Sun Dacheng / Hu Yongquan / Yu Yefeng / Wang Shiying / Yu Qiaqing /
Chu Minyi / Su Xiwen / Mei Siping). Three new keyed rows only:

  朱升   Zhu Sheng    — the servant who axed Fu Xiao'an (11 Oct 1940); central
        to Section 2. Rendered inline in ch27 (act NOTED ch04); keyed here because
        he recurs ~15x and renders "Zhu Sheng" everywhere. His alias 陈中南
        (Chen Zhongnan) and the source's spelling-variants 朱生/朱升源 stay inline.
  联合准备银行 the Federal Reserve Bank — the North China puppet bank (Wang Shiying
        governor; Cheng Xigeng general manager, sanctioned 1939); distinct from the
        Wang regime's 中央储备银行 Central Reserve Bank. NOTED.
  会审公廨 the Mixed Court — the Shanghai concessions' pre-1930 joint tribunal that
        the two reproduced agreements abolished, replaced by the Special District
        Courts. NOTED.

Rendered INLINE, NOT keyed (glossary-key discipline): the contributor 裴可权
(Pei Kequan); Fu's old friend / Yu Yefeng's son-in-law 盛礼约 (Sheng Liyue) and
his given name 盛郁 (Sheng Yu); the Chamber chairman 王晓籁 (Wang Xiaolai); Zhang
Xiaolin's lawyer son 张法尧 (Zhang Fayao) and the lawyer 余祥琴 (Yu Xiangqin); the
Frenchman 杜洛 (Duluo, Political Affairs Superintendent of the French Municipal
Council); Zhou Fohai's aide 柳汝祥 (Liu Ruxiang) and the money-men 钱书城 (Qian
Shucheng); the one-off Japanese officers (臼井宽三 Usui Kanzō, 马渊 Mabuchi, 前田
Maeda, 谷荻 Yahagi, 樱井 Sakurai, 曾弥 Sone, 青木 Aoki, 西园寺 Saionji, 犬养 Inukai,
木村市大郎 Kimura Ichitarō, 结城 Yūki, 日高 Hidaka, 上田 Ueda); the sanctioned bank
staff (季明远 Ji Mingyuan, 张永纲 Zhang Yonggang, 厉鼎模 Li Dingmo) and the operatives
who struck them (叶东山 Ye Dongshan, 赵家鑫 Zhao Jiaxin, 何凤祥 He Fengxiang, 丁小宝
Ding Xiaobao, 董威 Dong Wei, 田杰林 Tian Jielin, 林镇城 Lin Zhencheng); 程锡庚 Cheng
Xigeng (Federal Reserve Bank manager, sanctioned 1939); the Tang poet 曹松 (Cao
Song); the swimming star 杨秀琼 (Yang Xiuqiong) and the Yue-opera actress 姚水娟
(Yao Shuijuan); Fu's kin (宋有圭 Song Yougui, 品圭 Pingui) and dinner companions
(周文瑞 Zhou Wenrui, 魏晋三 Wei Jinsan, 盛老三 Sheng the Third); the go-betweens
程/彭 (Cheng/Peng) and Zhou's brother-in-law 杨惺华 (Yang Xinghua); the agreements'
transliterated foreign signatories (第安斯/雅克博/许立德/葛隆福/赫龙门/甘格霖/赖歌德/
甘格兰) and the Chinese ones (徐谟 Xu Mo, 吴昆吾 Wu Kunwu). The 大道市政府 "Great Way
City Government" is NOTED. Books/periodicals (上海租界问题, 新申报 Xin Shen Bao,
重庆大公报 Chongqing Ta Kung Pao, 官场现形记 Officialdom Unmasked) are footnotes/
inline, not keys."""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOSS = os.path.join(ROOT, "glossary.json")
ZH = os.path.join(ROOT, "data", "zh", "ch28.txt")
zh_text = open(ZH, encoding="utf-8").read()

PEOPLE = {
    "朱升": {"en": "Zhu Sheng", "pinyin": "Zhū Shēng", "status": "attested",
             "note": "The servant who killed the puppet Shanghai mayor Fu Xiao'an "
                     "with an axe on 11 Oct 1940; central to ch28 Section 2. His "
                     "assassination act was noted at ch04. Source spelling-variants "
                     "(朱生, 朱升源) and the alias 陈中南 render inline."},
}

ORGS = {
    "联合准备银行": {"en": "the Federal Reserve Bank", "pinyin": "Liánhé Zhǔnbèi Yínháng",
                 "status": "attested",
                 "note": "The North China puppet regime's central bank of issue "
                         "(Federal Reserve Bank of China, 1938); Wang Shiying its "
                         "governor. Distinct from the Wang regime's Central Reserve "
                         "Bank (中央储备银行)."},
    "会审公廨": {"en": "the Mixed Court", "pinyin": "Huìshěn Gōngxiè",
              "status": "attested",
              "note": "The Shanghai concessions' pre-1930 joint tribunal, abolished "
                      "by the two reproduced retrocession agreements and replaced by "
                      "the Chinese Special District Courts."},
}


def main():
    gl = json.load(open(GLOSS, encoding="utf-8"))
    added = 0
    for sec, rows in (("people", PEOPLE), ("organizations", ORGS)):
        for k, v in rows.items():
            if k not in zh_text:
                sys.exit("KEY NOT IN data/zh (possible mangling): %r" % k)
            if k in gl[sec]:
                if gl[sec][k].get("en") != v["en"]:
                    sys.exit("CONFLICT: %s already keyed to %r" % (k, gl[sec][k]))
                continue
            gl[sec][k] = v
            added += 1
    json.dump(gl, open(GLOSS, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("added %d ch28 glossary rows" % added)


if __name__ == "__main__":
    main()
