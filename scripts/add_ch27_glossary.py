#!/usr/bin/env python3
"""Add ch27's new glossary rows BY HAND into the sectioned glossary.json.
Idempotent; every row carries a pinyin field (qc_entities does rec['pinyin']).
Each hanzi key is verified as a substring of the authoritative data/zh/ch27.txt
so a Write-tool CJK mangling cannot slip a corrupted key into the glossary.

ch27 (大亨之死) is the Zhang Xiaolin tycoon-death case. Almost all its cast is
already keyed (Zhang Xiaolin/Lin Huaibu/Du Yuesheng/Fu Xiao'an/Ji Zhencang/
Pan Zixin/Qi Qingbin/Liu Yuanshen/Zheng Xiuyuan/Wan Molin/Liang Hongzhi/
Chen Qun/Zhou Fohai/Li Shiqun/He Xingjian). Two new keyed rows only:

  赵圣  Zhao Sheng   — the working name of the Second Action Brigade commander
        (real name 吉震苍 Ji Zhencang, already keyed); the two names denote one
        man but the source uses both and each renders its own way (the source's
        "第二队赵圣才说…" is Zhao Sheng + the adverb 才, not a longer name).
  黄金荣 Huang Jinrong — the third of the Green Gang's "Three Tycoons," beside
        Du Yuesheng and Zhang Xiaolin; recurs whenever the trio is named.

Rendered INLINE, NOT keyed (glossary-key discipline): the pen-name 东郭牙
(Dongguo Ya) and the contributor 裴可权 (Pei Kequan); the one-off Western
officer 马龙 (Maron); the letter's one-off names 柳乃夫 (Liu Naifu) and the
driver 阿四 (Ah Si); the twice-/thrice-named second victim 吴金桂/吴建臣/吴鸿
(Wu Jingui/Wu Jianchen/Wu Hong — the source itself flags the discrepancy);
the cook 朱升 (Zhu Sheng, whose Fu Xiao'an axe-killing is NOTED ch04). Periodicals
(新申报 Xin Shen Bao, 大公报 Ta Kung Pao, 大成 Dacheng) and books (上海租界问题,
沪上往事) are footnotes/inline, not keys."""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOSS = os.path.join(ROOT, "glossary.json")
ZH = os.path.join(ROOT, "data", "zh", "ch27.txt")
zh_text = open(ZH, encoding="utf-8").read()

PEOPLE = {
    "赵圣": {"en": "Zhao Sheng", "pinyin": "Zhào Shèng", "status": "attested",
             "note": "The working name of the Second Action Brigade's commander "
                     "(real name Ji Zhencang, keyed); the man who reported the "
                     "Zhang Xiaolin sanction. Rendered Zhao Sheng consistently."},
    "黄金荣": {"en": "Huang Jinrong", "pinyin": "Huáng Jīnróng", "status": "attested",
               "note": "The third of the Green Gang's 'Three Tycoons' of Shanghai, "
                       "beside Du Yuesheng and Zhang Xiaolin (see ch04)."},
}


def main():
    gl = json.load(open(GLOSS, encoding="utf-8"))
    added = 0
    for sec, rows in (("people", PEOPLE),):
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
    print("added %d new rows; people=%d" % (added, len(gl["people"])))


if __name__ == "__main__":
    main()
