#!/usr/bin/env python3
# B05 (ch07 PDF 154-172, ch08 PDF 173-197) furniture strip, run on data/txt
# BEFORE assemble. Same disease as B02-B04: page-bottom author-footnotes eat the
# spanning paragraph's continuation. This book's ch07/ch08 have NO full-page
# photos (find_figures 154-197 found nothing; eyeballed openers p154/p173 and
# memoir p178 confirm text-only pages).
#
# Order of operations:
#   1. Normalize garbled chapter/section headings to the exact structure.json
#      strings (so assemble.py auto-emits them as '### ').  Quote glyphs and a
#      few OCR letter-swaps differ; the s04 heading (p166) wraps two OCR lines.
#   2. Truncate author-footnote blocks at a FOOTNOTE-ONLY substring marker.
#
# PER-TARGET heading guard len(good)+4 (headings run 6-30 chars; a body line can
# share a heading's tokens).  All markers verified against the page's own body.
import os

TXT = "/home/user/winston/data/txt"

# page -> [(required tokens (OCR-clean substrings of the garbled heading),
#           exact structure.json title)]
HEADING_FIX = {
    154: [(["深入龙潭虎穴"], "深入龙潭虎穴"),
          (["调查科与徐恩曾"], "调查科与徐恩曾")],
    158: [(["周恩来说", "拿过来"], "周恩来说:“你们把它拿过来”")],
    162: [(["抓住徐恩曾的弱点"], "抓住徐恩曾的弱点,拿到绝密电码本")],
    # s04 heading wraps two OCR lines: "...除掉我" + "们最恨的警控"; merge+fix here,
    # and delete the orphan tail line below.
    166: [(["拿他的护照和钱", "除掉我"],
           "拿他的护照和钱,办我们的情报;用他的手和枪,除掉我们最恨的警探")],
    171: [(["向国民党最高特务机关", "打进去"],
           "向国民党最高特务机关“打进去”的典型")],
    173: [(["教官", "赵唯刚"], "奉天讲武堂教官——赵唯刚"),
          (["政变后两个月参加共产党"], "“四一二”政变后两个月参加共产党")],
    178: [(["高等军学研究班"], "在奉天讲武堂和高等军学研究班")],
    187: [(["被捕的刘伯刚"], "营救被捕的刘伯刚")],
    191: [(["兵运工作再遭挫折"], "兵运工作再遭挫折")],
    192: [(["一次抢救文件的斗争"], "一次抢救文件的斗争")],
    195: [(["前一个月侦知日军要动手"], "“九一八”前一个月侦知日军要动手")],
}

# Orphan heading-wrap tails to delete outright (the p166 s04 second line).
DELETE_CONTAINS = {166: ["们最恨的警控"]}

# page -> FOOTNOTE-ONLY substring on the first line of the footnote block.
FOOTNOTE_START = {
    154: "Communist",          # (1) C.P.=Communist Party abbreviation gloss
    156: "中国文史出版社",       # 张文《中统头子徐恩曾》
    161: "在地下交通线上",       # 《战斗在地下交通线上》党史资料丛刊
    163: "中统头子徐恩曾",       # 张文…；赵敏麟《徐恩曾的历史和活动片断》
    164: "香港三联书店",         # 《邹韬奋文集》第三卷
    165: "1963年6月2日",        # 张振华谈话记录
    171: "林聪",                # 林聪《李克农传略》中共党史资料第57期
    172: "invisible",          # 徐恩曾《The Invisible Conflict》1957
    187: "是赵唯刚的同学",       # (author's note on Liu Bogang)
    192: "满洲军委书记韩元波",   # (author's note listing the arrested)
}


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
    if page in DELETE_CONTAINS:
        keep = []
        for l in lines:
            if any(tok in l for tok in DELETE_CONTAINS[page]):
                print("p%04d: deleted orphan heading tail '%s'" % (page, l.strip()))
                continue
            keep.append(l)
        lines = keep
    if not changed:
        print("p%04d: NO HEADING MATCHED %s" % (page, [t for t, _ in specs]))
    open(p, "w").write("\n".join(lines) + "\n")


# Headings first (before any truncation shifts lines away).
for pg, pairs in HEADING_FIX.items():
    fix_headings(pg, pairs)
for pg, mk in FOOTNOTE_START.items():
    truncate(pg, mk)
