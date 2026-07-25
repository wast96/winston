#!/usr/bin/env python3
"""Assert every quantity in the source survives into the translation.

Reads a bilingual QC file: each '>' blockquote is a source line, the paragraph
beneath it is the translation. Compares arabic numerals, Chinese numerals, and
years. Does not read meaning — it catches dropped or altered quantities, which
is the error class that is both most costly and most mechanical.

This is the single highest value-per-token check in the whole pipeline. It is
a script, it runs in a second, and it caught real dropped numbers repeatedly
across a fifteen-chapter book. Run it after every chapter, not at the end.

Usage: check_numbers.py out/ch03_bilingual.md
"""
import re
import sys

CN_DIGIT = {"零": 0, "一": 1, "二": 2, "两": 2, "三": 3, "四": 4,
            "五": 5, "六": 6, "七": 7, "八": 8, "九": 9}
WORD_NUM = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12, "thirteen": 13, "several": None, "ten thousand": 10000,
    "second": 2, "third": 3, "first": 1, "lead": 1, "fourth": 4, "fifth": 5,
    "sixth": 6, "seventh": 7, "eighth": 8, "ninth": 9, "tenth": 10,
    "both": 2, "twice": 2, "neither": 2, "either": 2, "dozen": 12, "pair": 2,
}
TEENS = {"fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
         "eighteen": 18, "nineteen": 19}
TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
        "seventy": 70, "eighty": 80, "ninety": 90}
ONES = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
        "seven": 7, "eight": 8, "nine": 9}
MONTHS = {1: "january", 2: "february", 3: "march", 4: "april", 5: "may",
          6: "june", 7: "july", 8: "august", 9: "september",
          10: "october", 11: "november", 12: "december"}

# Numerals that are grammar, idiom or names rather than quantities. Stripping
# these is what makes the check usable; without it every measure word is a
# false hit and you stop reading the output, which is the real failure mode.
#
# ORDERING IS LOAD-BEARING. Longest literal first. A short pattern that is a
# prefix of a long one will eat half the phrase and leave a stray numeral
# behind. Do NOT sort this list programmatically by length: character classes
# make short patterns look long and the sort reintroduces the bug. This was
# discovered the hard way, twice.
NOISE = [
    r"八九不离十", r"四十多", r"三十多", r"二十几", r"二十多",
    r"十几", r"几十", r"十多",
    r"一[艘条顶只个位群把张片口指边旁时下阵壶碟种番场股家棵套幅丢看脚]",
    r"一[辆眼躬支丝声定天次间惊枪动言样阵路批封面团句道年身手笔]",
    r"[一不][旦时般点些]",
    r"千载难逢", r"千军万马", r"七嘴八舌", r"五短身材", r"千真万确",
    r"一举一动", r"一口", r"十分", r"七八", r"三十六计", r"一片",
    r"万[马千]", r"灵机一动", r"大吃一惊", r"头一次", r"有一天",
    r"一夜之间", r"千万", r"万籁", r"千恩万谢", r"十里洋场",
    r"八字胡", r"八仙桌", r"八拜之交", r"两人", r"三言两语",
    r"四起", r"五体投地", r"两[位界个]", r"四座", r"说一不二",
    r"零钱", r"[一二三]是", r"[几数][盏辆个位十百千万条艘句步进层次口杯天年分]",
    r"十[几分步]", r"五指", r"五花大绑", r"三巡", r"再三",
    r"一[举动身面言语气日夜时刻步分寸点]", r"两[头端边面全难]",
    r"三[番两教]", r"四[面方处海座]", r"九[鼎爷哥光江]", r"八[面方拜仙字]",
    r"七[八嘴]", r"说三道四", r"入木三分", r"一小时", r"化整为零",
    r"一一", r"三道防线", r"分两路", r"两乘", r"两日",
    r"四周", r"两旁", r"零部件", r"两[三边]", r"四[下面]", r"一[遍番]",
    r"朝三暮四", r"一清二楚", r"信心十足", r"十恶不赦", r"几秒",
    r"礼让三分", r"一哆嗦", r"三大[亨闻]", r"一拥而", r"一沓",
    r"一箭双雕", r"一迭声",
]


def cn_to_int(token):
    """Read a Chinese numeral, including 百/千/万 compounds.

    The original handled only digits and 十, so 一千四百 fell apart and left
    a bare 四 that no English rendering of "fourteen hundred" could account
    for: the check reported a dropped number on a paragraph that had dropped
    nothing. Positional year forms (一九三八) are deliberately NOT summed --
    they are digit strings rather than quantities, and a token with no
    place-value character returns None so the caller ignores it.
    """
    if token in CN_DIGIT:
        return CN_DIGIT[token]
    if not re.search(r"[十百千万]", token):
        return None
    total, section, digit = 0, 0, 0
    for ch in token:
        if ch in CN_DIGIT:
            digit = CN_DIGIT[ch]
        elif ch == "十":
            section += (digit or 1) * 10
            digit = 0
        elif ch == "百":
            section += (digit or 1) * 100
            digit = 0
        elif ch == "千":
            section += (digit or 1) * 1000
            digit = 0
        elif ch == "万":
            total += ((section + digit) or 1) * 10000
            section = digit = 0
    return (total + section + digit) or None


def source_numbers(text, extra_noise=()):
    stripped = text
    for pat in list(NOISE) + list(extra_noise):
        stripped = re.sub(pat, "", stripped)
    nums = set(int(n) for n in re.findall(r"\d+", stripped))
    for tok in re.findall(r"[零一二两三四五六七八九十百千万]+", stripped):
        val = cn_to_int(tok)
        # A bare 一 is nearly always a measure word, not a quantity.
        if val is not None and not (val == 1 and tok == "一"):
            nums.add(val)
    return nums


def spelled_numbers(low):
    """English spells numbers out where the source prints digits."""
    found = set()
    for tens, tval in TENS.items():
        for ones, oval in ONES.items():
            if re.search(r"\b%s[- ]%s\b" % (tens, ones), low):
                found.add(tval + oval)
        if re.search(r"\b" + tens + r"\b", low):
            found.add(tval)
        # "fifty thousand" is 5万 in the source, printed as a bare 5.
        if re.search(r"\b" + tens + r"[- ]?\w* ?thousand\b", low):
            found.add(tval // 10)
            found.add(tval * 1000)
    for teen, tval in TEENS.items():
        if re.search(r"\b" + teen + r"\b", low):
            found.add(tval)
        # "fourteen hundred" renders 一千四百; both readings must count
        if re.search(r"\b" + teen + r"[- ]?hundred\b", low):
            found.add(tval * 100)
            found.add(tval % 10 * 100)
    # English says "a hundred" where the source says 一百; without these the
    # indefinite article reads as an absent numeral and the check reports a
    # dropped quantity on a paragraph that kept it.
    if re.search(r"\ba hundred\b", low):
        found.add(100)
    if re.search(r"\ba thousand\b", low):
        found.add(1000)
    for ones, oval in ONES.items():
        if re.search(r"\b%s hundred thousand\b" % ones, low):
            found.add(oval * 100000)
            found.add(oval * 10)
        if re.search(r"\b%s hundred\b" % ones, low):
            found.add(oval * 100)
        if re.search(r"\b%s thousand\b" % ones, low):
            found.add(oval * 1000)
    return found


def target_numbers(text):
    nums = set(int(n) for n in re.findall(r"\d+", text))
    low = text.lower()
    nums |= spelled_numbers(low)
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


def load_extra_noise(path):
    """Project-specific noise: names containing numerals, local idioms.

    The built-in list is generic. EVERY project accumulates its own — personal
    names with digits in them, place names, set phrases. Keep them in a plain
    text file, one regex per line, and pass --noise. Extending this list as
    false positives appear is what keeps the check readable; a check nobody
    reads is a check that catches nothing.
    """
    if not path:
        return []
    return [l.strip() for l in open(path)
            if l.strip() and not l.startswith('#')]


def main(path, extra_noise=()):
    bad = npairs = 0
    for i, (src, tgt) in enumerate(pairs(path), 1):
        npairs = i
        s, t = source_numbers(src, extra_noise), target_numbers(tgt)
        # A Republican-calendar year may rightly surface as the Gregorian one.
        missing = {m for m in s - t if (m + 1911) not in t}
        if missing:
            bad += 1
            print("pair %d: unaccounted %s" % (i, sorted(missing)))
            print("   zh:", src[:60])
            print("   en:", tgt[:60])
    print("checked %d pairs, unresolved: %d" % (npairs, bad))
    return 1 if bad else 0


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("bilingual")
    ap.add_argument("--noise", help="file of project-specific noise regexes")
    a = ap.parse_args()
    sys.exit(main(a.bilingual, load_extra_noise(a.noise)))
