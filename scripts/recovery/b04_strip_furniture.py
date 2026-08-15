#!/usr/bin/env python3
# B04 (ch05 PDF 123-139, ch06 PDF 140-153) furniture strip, run on data/txt
# BEFORE assemble. Same disease as B02/B03: page-bottom author-footnotes eat the
# spanning paragraph's continuation, and full-page photos split content across
# the seam. This replays the paragraph-structure repair so a fresh QC regen
# reproduces the counts the English is paired against.
#
# Order of operations:
#   1. Normalize garbled chapter/section headings to the exact structure.json
#      strings (so assemble.py auto-emits them as '### ').
#   2. Truncate author-footnote blocks at a FOOTNOTE-ONLY substring marker.
#   3. Blank the two full-page photos (p125 Dong Biwu calligraphy of the elegy;
#      p134 the 钱壮飞 portrait).
#
# NOTE on the heading guard: ch05/ch06 headings run 8-21 chars, and one ch06s05
# body line ("...从敌人营垒中'拉出来'的典型。") duplicates the s05 heading's
# tokens. A single global maxlen cannot both admit the long headings and reject
# that body line, so the guard is PER-TARGET: len(good)+4. The heading line is
# always within a few chars of its normalized form; the body line is ~29 chars,
# far outside guard 17 for the 13-char s05 title.
import os

TXT = "/home/user/winston/data/txt"

# page -> [(required tokens (OCR-clean substrings of the garbled heading),
#           exact structure.json title)]
HEADING_FIX = {
    123: [(["龙"], "“龙潭三杰”")],             # "龙潭三杰"
    124: [(["我是党中央的"],                     # 我是党中央的
           "李克农说:我是党中央的“警卫员”")],
    132: [(["传奇英雄"],                                 # 传奇英雄
           "传奇英雄钱壮飞")],
    138: [(["才华最高"],                                 # 才华最高
           "“年纪最轻,才华最高”的胡底")],
    140: [(["第一个反间"],                           # 第一个反间(恋)
           "第一个反间谍关系——杨登瀛"),
          (["日本通"],                                       # 日本通
           "“日本通”杨登瀛")],
    144: [(["巡捕房不希望"],                     # 巡捕房不希望
           "兰普逊说:巡捕房不希望与杨登瀛以外的人接触")],
    147: [(["中央驻沪"],                                 # 中央驻沪
           "蒋介石任命的“中央驻沪特派员”")],
    149: [(["全权处理"],                                 # 全权处理
           "徐恩曾把大案交杨登瀛全权处理")],
    152: [(["从敌人营垒"],                           # 从敌人营垒
           "从敌人营垒“拉出来”的典型")],
}

# page -> FOOTNOTE-ONLY substring on the first line of the footnote block.
# Every marker verified absent from that page's body (see the note on p124:
# body carries the name 熊向晖, so the citation TITLE is the marker instead).
FOOTNOTE_START = {
    124: "我的情报与外交",   # 熊向晖:《我的情报与外交生涯》
    128: "深切的怀念",               # 阿英:《深切的怀念》
    133: "第三十七卷",               # 台北《传记文学》第三十七卷第5期
    136: "两次在北京",               # 张振华... 两次在北京与来访者
    137: "叶炳南",                           # 叶炳南:《钱壮飞》
    138: "谈话记录",                     # 张振华... 谈话记录
    139: "玉台新",                         # 《玉台新咏》(OCR garbles 咏->号)
    152: "论反对日本帝国",   # 《论反对日本帝国主义的策略》
}

PHOTO_FULL_PAGE = [125, 134]   # blank entirely (photo + caption only)


def path(page):
    return os.path.join(TXT, "p%04d.txt" % page)


def truncate(page, marker):
    p = path(page)
    lines = open(p).read().split("\n")
    for i, l in enumerate(lines):
        if marker in l:
            new = lines[:i]
            while new and new[-1].strip() == "":
                new.pop()
            open(p, "w").write("\n".join(new) + "\n")
            print("p%04d: footnote truncated %d->%d lines at '%s'"
                  % (page, len(lines), len(new), marker))
            return
    print("p%04d: FOOTNOTE MARKER '%s' NOT FOUND" % (page, marker))


def fix_headings(page, specs):
    p = path(page)
    lines = open(p).read().split("\n")
    changed = 0
    for i, l in enumerate(lines):
        s = l.strip()
        for tokens, good in specs:
            if len(s) > len(good) + 4:          # PER-TARGET guard
                continue
            if all(t in s for t in tokens):
                lines[i] = good
                changed += 1
                print("p%04d: heading '%s' -> '%s'" % (page, s, good))
    if not changed:
        print("p%04d: NO HEADING MATCHED %s" % (page, [t for t, _ in specs]))
    open(p, "w").write("\n".join(lines) + "\n")


# Headings first (before any truncation shifts lines away).
for pg, pairs in HEADING_FIX.items():
    fix_headings(pg, pairs)
for pg, mk in FOOTNOTE_START.items():
    truncate(pg, mk)
for pg in PHOTO_FULL_PAGE:
    open(path(pg), "w").write("\n")
    print("p%04d: blanked (full-page photo)" % pg)
