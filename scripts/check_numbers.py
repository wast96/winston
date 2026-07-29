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

CN_DIGIT = {"零": 0, "一": 1, "二": 2, "两": 2, "兩": 2, "三": 3, "四": 4,
            "五": 5, "六": 6, "七": 7, "八": 8, "九": 9}
WORD_NUM = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12, "thirteen": 13, "several": None, "ten thousand": 10000,
    "second": 2, "third": 3, "first": 1, "lead": 1, "fourth": 4, "fifth": 5,
    "sixth": 6, "seventh": 7, "eighth": 8, "ninth": 9, "tenth": 10,
    "both": 2, "twice": 2, "neither": 2, "either": 2, "dozen": 12, "pair": 2,
    # Extend WORD_NUM with any spelled-out numbers your translation uses that the
    # source prints as digits/hanzi. Example: teen ordinals for regnal years
    # ("the seventeenth year of the reign", 十七年); the built-ins stop at "tenth".
    "seventeenth": 17,
    # Teen ordinals used for lunar-calendar days in this book (腊月十五/十六 ->
    # "the fifteenth/sixteenth of the last lunar month"); spelled_numbers only
    # knows the cardinal teens, so the ordinal form must be declared here.
    "fifteenth": 15, "sixteenth": 16, "fourteenth": 14, "eighteenth": 18,
    "nineteenth": 19,
    # Ordinal day-of-month in a formal letter (保管箱延用至三月十一日 ->
    # "the eleventh of March"); the built-ins stop at "tenth".
    "eleventh": 11,
    # Compound lunar-date ordinals and a Republican-year tens word used in
    # B04 (腊月二十一/二十二 -> "the twenty-first/second"; 民国二十年 -> "the
    # twentieth year of the Republic"). spelled_numbers only composes cardinals
    # like "twenty-two", so these ordinal forms must be declared here.
    "twentieth": 20, "twenty-first": 21, "twenty-second": 22,
    # Ordinal for a playing-card rank in B06 (老开 = 第十三张牌 -> "the King, the
    # thirteenth card in the deck"). "thirteen" is a built-in but the ordinal is not.
    "thirteenth": 13,
    # Lunar-date ordinal used in B08 (正月十二 -> "the twelfth of the first month");
    # WORD_NUM has the cardinal "twelve" but the ordinal form was missing.
    "twelfth": 12,
    # Zero, used in B10 for a football score (一比零 -> "one to nil"); the source
    # prints 零 and English scores it as "nil"/"zero", neither of which was mapped.
    "nil": 0, "zero": 0,
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
# This is a GENERIC starter list. It strips the numerals that recur in almost
# any Chinese prose: measure words, four-character idioms, fractions, and list
# enumerators. It does NOT contain project-specific entries. As you translate,
# EVERY time the check flags a numeral that is not a real quantity (a proper
# name with a digit in it, a local idiom, a set phrase), add it here (or, better,
# to a per-project --noise file, see load_extra_noise). A check whose output is
# mostly false positives is a check nobody reads; keeping this list current is
# what keeps the real dropped-number visible. Record what you add, and why.
#
# Both simplified and Traditional forms are included where they differ, so the
# list works on either script. Extend with whichever your book uses.
NOISE = [
    # --- list enumerators & fractions (structure, not quantities) ---
    r"\d+[．.、]",                                  # "1." "2、" sub-item heads
    r"[一二三四五六七八九十百千零]+分之[一二三四五六七八九十百千零]+",  # 二分之一, fractions
    # --- measure words: a bare 一 + classifier is "a/an", not the count 1 ---
    r"一[艘條条頂顶隻只個个位群把張张片口指邊边旁時时下陣阵壺壶碟種种番場场股家棵套幅]",
    # Lookbehind added in B07: without it, the 一[天次年…] measure-word stripper
    # eats the 一 out of a teen/compound like 十一天 (11 days) or 三十一年
    # (31 years), orphaning 十/三十 read as 10/30. Mirrors the B03 lookbehind on
    # the 一[日夜时…] class. A bare 一天/一次/一年 (no preceding digit) still strips.
    r"(?<![零一二三四五六七八九十])一[輛辆眼躬支絲丝聲声定天次間间驚惊槍枪動动言樣样路批封面團团句道年身手筆笔遍]",
    # Lookbehind added in B12: without it the 一[点…] idiom stripper ("一点" =
    # "a little") eats the 一点 out of a clock time like 十一点 (11 o'clock),
    # orphaning a bare 十 read as 10. Mirrors the B03/B07 lookbehind patches. A
    # bare 一点/一些 (no preceding 十/digit) still strips.
    r"(?<![零一二三四五六七八九十])[一不][旦時时般點点些]",
    # Lookbehind added in B12: without (?<!十) this 几X measure stripper eats
    # the 几分 out of 十几分钟 (ten-odd minutes) before the 十[幾几分] rule can
    # strip 十几, orphaning a bare 十 read as 10 (same class of bug as 十几条).
    # A bare 几分/几十 (no preceding 十) still strips.
    r"(?<!十)[幾几數数][盞盏輛辆個个位十百千萬万條条艘句步進进層层次口杯天年分]",
    r"[幾几數数][十百千]",                          # 幾十/數百 "some tens/hundreds"
    # 十几 "ten-odd" / 十分 "very" — but NOT the 十 inside a clock time such as
    # 四十分 (40 min) or 五十分 (50 min), where the preceding digit means this 十
    # is the tens place of a real quantity. The lookbehind keeps those intact so
    # times survive to the number check instead of orphaning a stray ones-digit.
    # B09: an optional ones-digit prefix so "X十多" (五十多 "fifty-odd", 三十多
    # "thirty-odd") strips whole instead of orphaning the leading 五/三 read as
    # 5/3. Such "-odd" figures are inherently approximate and were never precisely
    # checkable anyway; this only REMOVES source numerals, so it can never mask a
    # dropped quantity. A bare 十多/几多 still strips. Supersedes the 二(?=岁) case.
    r"(?<![零一二三四五六七八九十百千])十[幾几分]", r"[零一二兩两三四五六七八九]?[十几幾]多", r"再三",
    # --- 萬/万 and 千 as intensifier, not the quantity 10000/1000 ---
    # ORDERING: 千萬/萬萬 must precede bare 萬X, or r"萬不可" eats the 萬 out of
    # 千萬不可 and orphans a 千 read as 1000. Longest literal first, always.
    r"千萬", r"万万", r"萬萬", r"萬不得已", r"萬不可", r"萬一", r"萬分",
    r"千万", r"万一", r"万分", r"以萬計", r"以万计", r"萬計", r"万计",
    # --- common four-character idioms carrying non-quantity numerals ---
    r"一舉一動", r"一举一动", r"一清二楚", r"說一不二", r"说一不二",
    r"三番五次", r"三番兩次", r"三番两次", r"三令五申", r"再三再四",
    r"五花八門", r"五花八门", r"七嘴八舌", r"亂七八糟", r"乱七八糟",
    r"千方百計", r"千方百计", r"千篇一律", r"千真萬確", r"千真万确",
    r"千軍萬馬", r"千军万马", r"千載難逢", r"千载难逢", r"千鈞一髮", r"千钧一发",
    r"萬無一失", r"万无一失", r"包羅萬象", r"包罗万象", r"瞬息萬變", r"瞬息万变",
    r"九牛一毛", r"入木三分", r"朝三暮四", r"三言兩語", r"三言两语",
    r"十全十美", r"十拿九穩", r"十拿九稳",
    r"(?<![零一二三四五六七八九])十分",  # 十分 = "very", not 10 (but keep 四十分/五十分)
    r"四面八方", r"四通八達", r"四通八达", r"一心一意", r"一五一十",
    # bare 一 as adverb/idiom fragment: 一[direction/time/manner], not the count.
    # Lookbehind keeps it from eating the 一 of a compound like 十一日 ("the
    # eleventh"), which would else mis-parse the date 十一日 as 十日 (=10).
    r"(?<![零一二三四五六七八九十])一[舉举動动身面言語语氣气日夜時时刻步分寸點点]", r"兩[頭头端邊边面全難难]",
    r"三[番兩两]", r"四[面方處处海座周]", r"九[鼎]", r"八[面方]",
    r"一一",                                        # 一一 "one by one"
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
    if not re.search(r"[十百千万萬億]", token):
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
        elif ch in ("万", "萬"):
            total += ((section + digit) or 1) * 10000
            section = digit = 0
        elif ch == "億":
            total += ((section + digit) or 1) * 100000000
            section = digit = 0
    return (total + section + digit) or None


def source_numbers(text, extra_noise=()):
    stripped = text
    for pat in list(NOISE) + list(extra_noise):
        stripped = re.sub(pat, "", stripped)
    nums = set(int(n) for n in re.findall(r"\d+", stripped))
    for tok in re.findall(r"[零一二两兩三四五六七八九十百千万萬億]+", stripped):
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
    # "<ones> hundred and <tens> thousand" composes a Chinese 万-compound written
    # as N万 (B07: 二十五万 = 25万 = 250000 -> "two hundred and fifty thousand").
    # spelled_numbers otherwise only reaches "fifty thousand" (50000) and
    # "two hundred" (200), never their sum.
    for ones, oval in ONES.items():
        for tens, tval in TENS.items():
            if re.search(r"\b%s hundred(?: and)? %s thousand\b" % (ones, tens), low):
                found.add((oval * 100 + tval) * 1000)
    return found


def target_numbers(text):
    nums = set(int(n) for n in re.findall(r"\d+", text))
    low = text.lower()
    nums |= spelled_numbers(low)
    # "million"/"billion" multipliers: the source writes 萬/億 compounds that
    # English spells as "five million", "a hundred million", and so on.
    MULT = {"million": 10 ** 6, "billion": 10 ** 9}
    for word, scale in MULT.items():
        for m in re.findall(r"(\d+)\s*" + word, low):
            nums.add(int(m) * scale)
        for name, val in ONES.items():
            if re.search(r"\b%s %s\b" % (name, word), low):
                nums.add(val * scale)
        if re.search(r"\b(a|one) %s\b" % word, low):
            nums.add(scale)
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
