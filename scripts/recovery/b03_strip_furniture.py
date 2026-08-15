#!/usr/bin/env python3
# B03 (ch04, PDF 95-122) furniture strip, run on data/txt BEFORE assemble.
# Same disease as B02: page-bottom author-footnotes eat the spanning paragraph's
# continuation, and embedded photos weld/split content. This replays the exact
# paragraph-structure repair so a fresh QC regen reproduces the counts the
# English is paired against.
#
# Order of operations, per page:
#   1. Truncate author-footnote blocks at a FOOTNOTE-ONLY substring marker.
#   2. Blank the full-page photo (p113 = the 陈养山 portrait).
#   3. Strip the p101 TOP photo (吴先清): keep from the first body line.
#   4. Truncate the p104 BOTTOM photo (柯麟): keep THROUGH the last body line.
#   5. Normalize the four garbled section headings + the chapter title to the
#      exact structure.json strings, so assemble.py auto-emits them as '### '.
import os

TXT = "/home/user/winston/data/txt"

# page -> substring on the FIRST line of the footnote block; truncate there.
# Every marker is a footnote-only string (verified absent from that page's body).
FOOTNOTE_START = {
    98:  "灵夏部",          # 灵夏部:《刘鼎》…第四十三卷
    100: "赵子动",          # 赵子彧:《吴先清》…第二十四卷
    102: "1986年9月3日",    # 《人民日报》citation for the 刘鼎 obituary
    103: "1987年6月7日",    # 李强:《忆刘鼎同志》,《光明日报》
    108: "汉彩竟",          # 汪彩章·李葆定:《贺诚传》(first of two notes)
    110: "李谷定",          # 李葆定·冯彩章:《柯麟传略》
    112: "罗才长",          # 罗才长:《创业艰难百战多》
    114: "曾出席中国共产党第一次",  # 陈潭秋 biographical note
    120: "社会学学会",       # 上海社会学学会《社会报》
    121: "欧阳瑟",          # 金冲及·欧阳瑟:《陈寿昌》…第四十九卷
}

PHOTO_FULL_PAGE = [113]                      # blank entirely (portrait + caption)

# TOP photo: drop every line BEFORE the first line containing this body marker.
PHOTO_TOP_KEEP_FROM = {101: "关系巧妙地向"}   # 吴先清 portrait sits above the body

# BOTTOM photo: keep every line THROUGH the first line containing this marker,
# drop the rest (the photo + caption).
PHOTO_BOTTOM_KEEP_THROUGH = {104: "是当时美国在中"}  # 柯麟 portrait below the body

# Garbled heading line -> exact structure.json title. Matched by REQUIRED
# tokens plus a length guard (<=15 chars): section headings are short standalone
# lines, body lines run the full ~28-char measure, so a stray token in the body
# (e.g. "福将" recurring in p112 body) can never trip the replacement.
HEADING_FIX = {
    95:  [(["情报战线的英"], "情报战线的英豪"),
          (["兵器专家刘"],   "兵器专家刘鼎")],
    103: [(["济世名医柯"],   "济世名医柯麟")],
    112: [(["隐蔽战线的", "福将"], "隐蔽战线的“福将”陈养山")],
    118: [(["血染沙场"],     "血染沙场的陈寿昌")],
}
HEADING_MAXLEN = 15


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


def keep_from(page, marker):
    p = path(page)
    lines = open(p).read().split("\n")
    for i, l in enumerate(lines):
        if marker in l:
            new = lines[i:]
            open(p, "w").write("\n".join(new) + "\n")
            print("p%04d: top photo stripped, kept from line %d ('%s')"
                  % (page, i, marker))
            return
    print("p%04d: TOP-PHOTO MARKER '%s' NOT FOUND" % (page, marker))


def keep_through(page, marker):
    p = path(page)
    lines = open(p).read().split("\n")
    for i, l in enumerate(lines):
        if marker in l:
            new = lines[:i + 1]
            open(p, "w").write("\n".join(new) + "\n")
            print("p%04d: bottom photo stripped, kept through line %d ('%s')"
                  % (page, i, marker))
            return
    print("p%04d: BOTTOM-PHOTO MARKER '%s' NOT FOUND" % (page, marker))


def fix_headings(page, specs):
    p = path(page)
    lines = open(p).read().split("\n")
    changed = 0
    for i, l in enumerate(lines):
        s = l.strip()
        if len(s) > HEADING_MAXLEN:
            continue
        for tokens, good in specs:
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
for pg, mk in PHOTO_TOP_KEEP_FROM.items():
    keep_from(pg, mk)
for pg, mk in PHOTO_BOTTOM_KEEP_THROUGH.items():
    keep_through(pg, mk)
