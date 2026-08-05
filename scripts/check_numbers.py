#!/usr/bin/env python3
"""Assert every quantity in the source survives into the translation.

Reads a bilingual QC file: each '>' blockquote is a source line, the paragraph
beneath it is the translation. Compares arabic numerals, Chinese numerals, and
years. Does not read meaning — it catches dropped or altered quantities, which
is the error class that is both most costly and most mechanical.

This is the single highest value-per-token check in the whole pipeline. It is
a script, it runs in a second, and it caught real dropped numbers repeatedly
across nine complete books. Run it after every chapter, not at the end.

THE INVARIANTS (learned the hard way, nine separate times):
  1. Noise rules only ever REMOVE source numerals, so a noise rule can never
     mask a dropped quantity. If a flag is a real quantity, fix the English to
     carry the value; never noise it away.
  2. Ordering is load-bearing: longest literal first. A short pattern that is
     a prefix (or infix) of a longer number eats half the phrase and leaves a
     stray numeral behind (一日 inside 二十一日 orphans a 20; 几分 inside
     十几分钟 orphans a 10). Do NOT sort programmatically: character classes
     make short patterns look long and the sort reintroduces the bug.
  3. Every noise pattern that begins with a numeral is auto-guarded with a
     negative lookbehind (see _guard) so it cannot fire inside a larger
     compound number. This killed the whole "orphaned digit" bug class.
  4. Project noise (--noise file) is applied BEFORE the built-in list, so a
     project rule can pre-empt a built-in that would damage its numbers
     (e.g. prisoner ID 五一三 must strip before the 五一 May Day rule).

Usage: check_numbers.py out/ch03_bilingual.md [--noise noise.txt]
"""
import re
import sys

CN_DIGIT = {"零": 0, "〇": 0, "一": 1, "二": 2, "两": 2, "兩": 2, "三": 3, "四": 4,
            "五": 5, "六": 6, "七": 7, "八": 8, "九": 9}
WORD_NUM = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12, "thirteen": 13, "several": None, "ten thousand": 10000,
    "both": 2, "twice": 2, "neither": 2, "either": 2, "dozen": 12, "pair": 2,
    "zero": 0, "nil": 0,          # 一比零, a nil-nil score
    "lead": 1,
}
# Ordinals are TARGET-side only, so an unused entry can only ADD to the
# translation's number set — it can never create a false negative. Ship the
# whole block rather than discovering one at a time (lunar dates, regnal and
# Republican years, day-of-month in letters, and card ranks all want them;
# the old built-ins stopped at "tenth" and every project paid for it).
ORDINALS = {
    "first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5,
    "sixth": 6, "seventh": 7, "eighth": 8, "ninth": 9, "tenth": 10,
    "eleventh": 11, "twelfth": 12, "thirteenth": 13, "fourteenth": 14,
    "fifteenth": 15, "sixteenth": 16, "seventeenth": 17, "eighteenth": 18,
    "nineteenth": 19, "twentieth": 20, "thirtieth": 30, "fortieth": 40,
    "fiftieth": 50, "sixtieth": 60, "seventieth": 70, "eightieth": 80,
    "ninetieth": 90, "hundredth": 100, "thousandth": 1000,
}
WORD_NUM.update(ORDINALS)
TEENS = {"fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
         "eighteen": 18, "nineteen": 19}
TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
        "seventy": 70, "eighty": 80, "ninety": 90}
ONES = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
        "seven": 7, "eight": 8, "nine": 9}
# compound ordinals: twenty-first .. ninety-ninth (target-side, safe)
_ORD_ONES = {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5,
             "sixth": 6, "seventh": 7, "eighth": 8, "ninth": 9}
for _t, _tv in TENS.items():
    for _o, _ov in _ORD_ONES.items():
        WORD_NUM["%s-%s" % (_t, _o)] = _tv + _ov
MONTHS = {1: "january", 2: "february", 3: "march", 4: "april", 5: "may",
          6: "june", 7: "july", 8: "august", 9: "september",
          10: "october", 11: "november", 12: "december"}

# Numerals that are grammar, idiom or names rather than quantities. Stripping
# these is what makes the check usable; without it every measure word is a
# false hit and you stop reading the output, which is the real failure mode.
#
# ORDERING IS LOAD-BEARING. Longest literal first. See module docstring.
# This is a GENERIC starter list: measure words, four-character idioms,
# fractions, list enumerators. Project-specific entries (names with digits,
# local idioms) go in the --noise file, which is applied FIRST.
#
# Both simplified and Traditional forms are included where they differ.
NOISE = [
    # --- list enumerators & fractions (structure, not quantities) ---
    r"\d+[．.、]",                                  # "1." "2、" sub-item heads
    r"[一二三四五六七八九十百千零]+分之[一二三四五六七八九十百千零]+",  # 二分之一, fractions
    # --- measure words: a bare 一 + classifier is "a/an", not the count 1 ---
    r"一[艘條条頂顶隻只個个位群把張张片口指邊边旁時时下陣阵壺壶碟種种番場场股家棵套幅]",
    r"一[輛辆眼躬支絲丝聲声定天次間间驚惊槍枪動动言樣样路批封面團团句道年身手筆笔遍]",
    r"[一不][旦時时般點点些]",
    # 十几/十多 must run BEFORE the [幾几數数] classes, or 几分 fires inside
    # 十几分钟 and orphans the 十 (longest-first, again). The optional ones-
    # digit prefix on the 多 rule strips 二十多 whole instead of orphaning 二.
    r"十[幾几分]", r"[零一二兩两三四五六七八九]?[十几幾]多",
    r"[幾几數数][盞盏輛辆個个位條条艘句步進进層层次口杯天年分]",
    r"[幾几數数][十百千][萬万]",                    # 几十万: strip whole, else the
    r"[幾几數数][十百千]",                          #   2-char rule orphans a bare 万
    r"[幾几數数][萬万]", r"再三",
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
    r"十全十美", r"十拿九穩", r"十拿九稳", r"十分",  # 十分 = "very", not 10
    r"四面八方", r"四通八達", r"四通八达", r"一心一意", r"一五一十",
    # bare 一 as adverb/idiom fragment: 一[direction/time/manner], not the count
    r"一[舉举動动身面言語语氣气日夜時时刻步分寸點点]", r"兩[頭头端邊边面全難难]",
    r"三[番兩两]", r"四[面方處处海座周]", r"九[鼎]", r"八[面方]",
    r"一一(?![零〇一二两兩三四五六七八九十百千万萬億])",  # 一一 "one by one" -- but NOT the head of a compound like 一一七 (117)
]

# Any noise pattern that could fire INSIDE a larger compound number gets a
# negative lookbehind: 一日 must not match the tail of 二十一日 (orphaning a
# 20), 十分 must not match the tail of 四十分, 一点 must not match the tail of
# 十一点. Applied automatically to every pattern that begins with a Chinese
# numeral or with a character class containing one. This one guard killed the
# recurring "orphaned digit" false-positive class across nine books.
_CN_NUM_CLASS = "零〇一二两兩三四五六七八九十百千万萬億"
_GUARD = "(?<![" + _CN_NUM_CLASS + "])"


def _guard(pat):
    if pat.startswith("(?"):
        return pat                      # already carries its own assertion
    first = pat[0]
    if first in _CN_NUM_CLASS:
        return _GUARD + pat
    if first == "[":
        end = pat.find("]")
        if end > 0 and any(c in _CN_NUM_CLASS for c in pat[1:end]):
            return _GUARD + pat
    return pat


def _decomma(text):
    """2,500,000 is one number, not three. Strip digit-group commas before
    matching; this also makes the 'comma-free digits in the English' style
    rule unnecessary."""
    return re.sub(r"(?<=\d),(?=\d)", "", text)


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
        # Positional digit strings: 一九三八 is the year 1938 and a dropped
        # year is exactly the drop this check exists to catch (the original
        # ignored these entirely). Three digits or more only: two-digit runs
        # like 五六 are almost always "five or six", not 56.
        if len(token) >= 3 and all(ch in CN_DIGIT for ch in token):
            return int("".join(str(CN_DIGIT[ch]) for ch in token))
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
    stripped = _decomma(text)
    # Project noise FIRST: a project rule must be able to pre-empt a built-in
    # that would eat the middle of one of its numbers (the 五一三/五一 case,
    # the 两三百/两三 case). Then the generic list.
    for pat in list(extra_noise) + list(NOISE):
        stripped = re.sub(_guard(pat), "", stripped)
    nums = set(int(n) for n in re.findall(r"\d+", stripped))
    for tok in re.findall(r"[零〇一二两兩三四五六七八九十百千万萬億]+", stripped):
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
            # "two hundred and fifty thousand" = 二十五万 = 250,000; the
            # separate hundred/thousand rules reach only 200 and 50,000 and
            # the check reported a drop on a faithful paragraph.
            if re.search(r"\b%s hundred(?: and)? %s thousand\b" % (ones, tens), low):
                found.add(oval * 100000 + tval * 1000)
            for o2, o2v in ONES.items():
                if re.search(r"\b%s hundred(?: and)? %s[- ]%s thousand\b"
                             % (ones, tens, o2), low):
                    found.add(oval * 100000 + (tval + o2v) * 1000)
            # "five hundred and sixty" = 五百六十 = 560, one number.
            if re.search(r"\b%s hundred(?: and)? %s\b" % (ones, tens), low):
                found.add(oval * 100 + tval)
            for o2, o2v in ONES.items():
                if re.search(r"\b%s hundred(?: and)? %s[- ]%s\b"
                             % (ones, tens, o2), low):
                    found.add(oval * 100 + tval + o2v)
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
    text = _decomma(text)
    nums = set(int(n) for n in re.findall(r"\d+", text))
    low = text.lower()
    nums |= spelled_numbers(low)
    # "million"/"billion" multipliers: the source writes 萬/億 compounds that
    # English spells as "five million", "a hundred million", and so on.
    MULT = {"million": 10 ** 6, "billion": 10 ** 9}
    for word, scale in MULT.items():
        for m in re.findall(r"(\d+)\s*" + word, low):
            nums.add(int(m) * scale)
        for name, val in dict(ONES, **dict(TEENS, **TENS)).items():
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

    One regex per line; '#' comment lines only — NO trailing comments (the
    whole non-# line is kept as the pattern). Longest literal first; a rule
    that can be the tail of a larger number needs a lookbehind (though
    _guard now adds one automatically to numeral-initial patterns). These
    run BEFORE the built-in list, so a project rule can protect its own
    numbers from a greedy built-in. Record every entry's meaning and the
    phrase the English uses, on its own comment line above it.
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
