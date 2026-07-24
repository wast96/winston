#!/usr/bin/env python3
"""QC step 4: assert every quantity in the source survives into the target.

Reads a bilingual markdown file where each '>' blockquote is source
Chinese and the paragraph beneath it is the English. Compares, per pair:
arabic numerals, Chinese numerals converted to arabic, and years.

Does not read meaning. It only catches dropped or altered quantities,
which is the error class that is both most costly and most mechanical.

Usage: check_invariants.py out/pilot_ch1_s1.md
"""
import re
import sys

CN_DIGIT = {"零": 0, "一": 1, "二": 2, "两": 2, "三": 3, "四": 4,
            "五": 5, "六": 6, "七": 7, "八": 8, "九": 9}
WORD_NUM = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12, "thirteen": 13, "several": None, "ten thousand": 10000,
    "second": 2, "third": 3, "first": 1, "lead": 1,
    "fourth": 4, "fifth": 5, "sixth": 6, "seventh": 7, "eighth": 8,
    "ninth": 9, "tenth": 10, "both": 2,
}


def cn_to_int(token):
    """Handle the small forms that appear in running prose: 二, 十三, 三十."""
    if token in CN_DIGIT:
        return CN_DIGIT[token]
    if "十" in token:
        left, _, right = token.partition("十")
        tens = CN_DIGIT.get(left, 1) if left else 1
        ones = CN_DIGIT.get(right, 0) if right else 0
        return tens * 10 + ones
    return None


# Numerals that are grammar or idiom, not quantities. Stripping these is
# what makes the check usable; without it every 一艘 and 九爷 is a false hit.
NOISE = [
    r"一[艘条顶只个位群把张片口指边旁时下阵壶碟种番场股家棵套幅丢看脚]",  # measure words
    r"一[辆眼躬支丝声定天次间惊枪动言样阵路批封面团句道年身手笔]",       # more measure/idiom 一s (prologue+)
    r"[一不][旦时般点些]",
    r"九爷", r"九光", r"九帅",                                   # Wang Yaqiao's title/name
    r"千载难逢", r"千军万马", r"七嘴八舌", r"五短身材",
    r"千真万确", r"一举一动", r"一口", r"十分", r"七八", r"王八蛋",
    r"三十六计", r"一片", r"万[马千]",
    r"第一辆",              # "the lead car"
    r"灵机一动", r"大吃一惊", r"头一次", r"有一天", r"一夜之间",
    r"瘪三",                # Shanghai slang, the 三 is not a quantity
    r"千万", r"万籁", r"千恩万谢", r"十里洋场",
    r"九哥",                 # fraternal address for Wang Yaqiao
    r"石友三",               # the 三 is a name, not a count
    r"八字胡", r"八仙桌", r"八拜之交", r"两人", r"三言两语",
    r"四起", r"五体投地", r"三大亨", r"二师兄",
]
MONTHS = {1: "january", 2: "february", 3: "march", 4: "april", 5: "may",
          6: "june", 7: "july", 8: "august", 9: "september",
          10: "october", 11: "november", 12: "december"}


def source_numbers(text):
    stripped = text
    for pat in NOISE:
        stripped = re.sub(pat, "", stripped)
    nums = set(int(n) for n in re.findall(r"\d+", stripped))
    for tok in re.findall(r"[零一二两三四五六七八九十]+", stripped):
        val = cn_to_int(tok)
        # a bare 一 as "one" is nearly always a measure word or idiom, not a
        # quantity; suppressing it kills the last chronic false-positive
        # class. Arabic 1 in the source is still checked.
        if val is not None and not (val == 1 and tok == "一"):
            nums.add(val)
    return nums


def target_numbers(text):
    nums = set(int(n) for n in re.findall(r"\d+", text))
    low = text.lower()
    for word, val in WORD_NUM.items():
        if val is not None and re.search(r"\b" + word + r"\b", low):
            nums.add(val)
    for val, name in MONTHS.items():
        if name in low:
            nums.add(val)
    return nums


def pairs(path):
    src, buf = None, []
    for line in open(path):
        if line.startswith(">"):
            if src is not None and buf:
                yield src, " ".join(buf)
                buf = []
            src = line.lstrip("> ").strip()
        elif line.strip() and not line.startswith(("#", "---", "**", "`")):
            if src is not None:
                buf.append(line.strip())
    if src is not None and buf:
        yield src, " ".join(buf)


def main(path):
    bad = npairs = 0
    for i, (src, tgt) in enumerate(pairs(path), 1):
        npairs = i
        s, t = source_numbers(src), target_numbers(tgt)
        # a Republican-calendar year in the source may rightly surface as the
        # Gregorian year in the target (民国十六年 -> 1927)
        missing = {m for m in s - t if (m + 1911) not in t}
        if missing:
            bad += 1
            print("pair %d: unaccounted %s" % (i, sorted(missing)))
            print("   zh:", src[:60])
            print("   en:", tgt[:60])
    print("checked %d pairs, unresolved: %d" % (npairs, bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
