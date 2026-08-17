#!/usr/bin/env python3
# B11 (ch19 PDF 389-405, ch20 PDF 406-428) furniture strip, run on data/txt
# BEFORE assemble.  Follows the b10 model.
#
#   1. Normalize garbled section/chapter headings to the EXACT book.json titles.
#      ch19's chapter title prints on TWO OCR lines (em-dash break) -> merge.
#   2. No figure/facsimile pages in this batch (ch19/ch20 are pure narrative;
#      find_figures empty, char-counts show no plate pages).
#   3. Truncate author-footnote blocks (source citations / content notes);
#      quoted-passage sources and the two substantive notes (王竹樵 identity,
#      抄靶子) are reproduced as "Author's note." at the (1) anchor in notes.json.
#   4. RESTORE OCR-mangled sentence-ends at paragraph seams (the b09/b10 lesson).
#
# NOT idempotent on the raw txt: restore from data/txt_backup_b11 before re-run.
import json
import os

ROOT = "/home/user/winston"
TXT = os.path.join(ROOT, "data", "txt")

book = json.load(open(os.path.join(ROOT, "book.json")))
TITLE = {}


def _walk(nodes):
    for u in nodes:
        if "id" in u and "title" in u:
            TITLE[u["id"]] = u["title"]
        for s in u.get("sections", []):
            TITLE[s["id"]] = s["title"]


_walk(book["structure"])

# page -> [(required OCR-clean tokens, structure id whose title is the target)]
HEADING_FIX = {
    389: [(["顾顺章护送张国", "去鄂"], "ch19s01")],
    402: [(["一网打尽", "中共中央阴谋彻底破产"], "ch19s03")],
    406: [(["倾箱倒", "的出卖"], "ch20"),
          (["顾顺章出卖了在南京狱中的"], "ch20s01")],
    413: [(["顾顺章赴香港捕杀"], "ch20s02")],
}

# page -> distinctive substring on the FIRST line of the footnote block; the
# block runs from there to the page foot.  All are author source-citations or
# author content notes; quoted-passage sources become "Author's note." notes.
FOOTNOTE_START = {
    389: "中共党史大事年表",       # (1) 大事年表 (2) 中国共产党的七十年
    390: "中国共产党历史",         # 中国共产党历史 上册
    391: "关于中央特科",           # 陈养山《关于中央特科》
    392: "一次谈话记录",           # 李强 1981-10 谈话记录
    395: "关于告密顾顺章",         # substantive: 王竹樵 vs 尤崇新 identity
    396: "中统头子徐恩曾",         # 《中统头子徐恩曾》第9页
    397: "两个可能改写中国近代历史",  # 蔡孟坚 传记文学
    401: "中统头子徐恩曾",         # (1) 徐恩曾 12页 (2) 万亚刚 特务大师顾顺章
    409: "拦住行人",               # substantive: 抄靶子 explanation
    410: "中国青年出版社1995",     # 《恽代英传》第536页
    411: "第336 ~ 537",           # 《恽代英传》第536~537页
    413: "中统从顾案血腥发家",     # 张国栋
    414: "纪念蒙和森",             # 李立三《纪念蔡和森同志》
    415: "林彬给毛泽东",           # (1)(2) 蔡和森文集 (3) 毛泽东书信选集
    418: "罗绍达",                 # 罗绍达《蔡和森》人物传
    420: "关于向忠发被捕",         # 高生整理《关于向忠发被捕叛变问题》
}

# OCR-mangled sentence-ends / dropped intro text at paragraph seams -- verified
# on the scan.  Restores only; content garbles go through data/ocr_fixes.json.
RESTORE = {
    # ch20s02: the period after "施滉等4人。" OCR'd as a comma, welding the tail
    # of S2P13 onto S2P14 across the surgery snap (printed p.373).  Also 施滉.
    417: [("施涡等\n4人，", "施滉等4人。")],
    # ch20s01: the 。① closing the 恽代英传 block quote OCR'd as a dash, so the
    # surgery snap pulled the "周恩来立即安排" sentence into the next paragraph.
    411: [("搭民船回来-", "搭民船回来。")],
}


def path(page):
    return os.path.join(TXT, "p%04d.txt" % page)


def merge_ch19_title(page=389):
    """ch19 title prints on two OCR lines with an em-dash break; merge to the
    exact book.json title and drop the stray folio-leak line above it."""
    p = path(page)
    lines = open(p).read().split("\n")
    out = []
    i = 0
    good = TITLE["ch19"]
    while i < len(lines):
        s = lines[i].strip()
        # stray leading folio digit(s) before the title
        if not out and s.isdigit():
            i += 1
            continue
        if "扑灭一场特大灾祸" in s:
            out.append(good)
            # skip the continuation line "——顾顺章叛变前后"
            if i + 1 < len(lines) and "顾顺章叛变前后" in lines[i + 1]:
                i += 2
            else:
                i += 1
            continue
        out.append(lines[i])
        i += 1
    open(p, "w").write("\n".join(out))
    print("p%04d: merged ch19 title -> %r" % (page, good))


def fix_headings(page, specs):
    p = path(page)
    lines = open(p).read().split("\n")
    changed = 0
    for i, l in enumerate(lines):
        s = l.strip()
        for tokens, sid in specs:
            good = TITLE[sid]
            if len(s) > len(good) + 5:
                continue
            if all(t in s for t in tokens):
                lines[i] = good
                changed += 1
                print("p%04d: heading '%s' -> '%s'" % (page, s, good))
    if not changed:
        print("p%04d: NO HEADING MATCHED %s" % (page, [t for t, _ in specs]))
    open(p, "w").write("\n".join(lines))


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


def restore(page, pairs):
    p = path(page)
    s = open(p).read()
    for wrong, right in pairs:
        if wrong in s:
            s = s.replace(wrong, right)
            print("p%04d: restored %r -> %r" % (page, wrong, right))
        else:
            print("p%04d: RESTORE ANCHOR %r NOT FOUND" % (page, wrong))
    open(p, "w").write(s)


if __name__ == "__main__":
    merge_ch19_title(389)
    for pg, mk in FOOTNOTE_START.items():
        truncate(pg, mk)
    for pg, specs in HEADING_FIX.items():
        fix_headings(pg, specs)
    for pg, pairs in RESTORE.items():
        restore(pg, pairs)
