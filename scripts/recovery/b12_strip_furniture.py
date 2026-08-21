#!/usr/bin/env python3
# B12 (ch21 PDF 429-457, ch22 PDF 458-484) furniture strip, run on data/txt
# BEFORE assemble.  Follows the b11 model.
#
#   1. Normalize garbled section/chapter headings to the EXACT book.json titles.
#      ch21 chapter title 穷凶极恶(蜀 OCR)/(上); s01 陈赓 (陈广 OCR).  ch22 title
#      and s01 clean.  s02 headings sit MID-PAGE (p450 l24, p471 l18).
#   2. Truncate author-footnote (source-citation / bio) blocks from the body.
#      Most sit at the page foot -> truncate marker-to-end.  The two bio notes
#      注1 潘梓年 (p470 foot) and 注2 应修人 (p471 TOP, before the s02 heading)
#      are reproduced as "Author's note." in ch22s01; 注2 needs a top-block cut.
#   3. RESTORE OCR-mangled sentence-ends at paragraph seams (added after the
#      surgery dry-run surfaces them).
#
# NOT idempotent on the raw txt: restore from data/txt_backup_b12 before re-run.
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

# page -> [(required OCR-clean tokens avoiding the garbled glyph, structure id)]
HEADING_FIX = {
    429: [(["极恶的捕杀(上)"], "ch21"),
          (["派特务追捕陈"], "ch21s01")],
    450: [(["魔手伸进王根英的娘家"], "ch21s02")],
    458: [(["极恶的捕杀(下)"], "ch22"),
          (["秘密绑架丁玲"], "ch22s01")],
    471: [(["参与暗杀杨杏佛"], "ch22s02")],
}

# page -> distinctive substring on the FIRST line of a foot-of-page footnote
# block; block runs from there to page end.
FOOTNOTE_START = {
    429: "叛徒顾顺章叛变的经过和经验",   # 杜宁 (author's note: sources杨之华 quote)
    430: "江苏文史资料编辑部",           # 顾顺章被杀真相 / 中统特工秘录
    436: "上海公理的例子",               # 《中国论坛》(author's note: sources法庭 quote)
    438: "红色中国杂记",                 # 斯诺 (author's note: sources 火车 quote)
    442: "在白色恐怖的卫城中",           # 《中国论坛》(author's note: sources quote)
    443: "在白色慌怖的卫城中",           # 《中国论坛》(author's note: sources quote)
    445: "本节所引宋庆龄的话",           # 宋庆龄选集 (author's note)
    456: "见杨力",                       # 杨力 1980 谈话记录 (Author's note, mid-page)
    459: "1986年3月16日",               # 新华社 丁玲生平
    460: "最近的丁玲女士",               # 少青
    461: "鲁迅约见朝鲜友人",             # 李政文 (author's note: sources 鲁迅诗)
    463: "湖南文艺出版社1991年版",       # 丁玲《魍魉世界》(author's note)
    468: "第八卷",                       # 丁玲文集 + 组织部通知
    470: "注1:潘梓年",                   # 潘梓年 bio (Author's note)
    475: "追忆和鲁迅先生",               # 宋庆龄 (author's note: sources quote)
    476: "杨杏佛事略",                   # 杨小佛
    477: "中统走卒",                     # 林成萌 + 顾案 + 丁玲 (3 cites)
    479: "文史资料选辑",                 # 沈醉 (author's note: sources quote)
    480: "1933年6月19日",               # 《申报》
    481: "南海出版公司2001年版",         # Epstein + 2 cites
    482: "宋庆龄选集",                   # 宋庆龄声明 (author's note: sources quote)
    484: "杨杏佛.史量才被暗杀的经过",     # 沈醉 (repeat cite)
}

# p471: the 注2 应修人 bio block is at the TOP of the page, before the s02
# heading -> remove lines from the marker up to (not including) the heading.
TOP_BLOCK = {
    471: ("注2:应修人", "参与暗杀杨杏佛"),
}

# Figure-caption blocks that OCR'd INTO the body.  The captions are reproduced
# in figures.json; strip them so they do not pollute parity.
#   REMOVE_UNTIL: drop every line before the first line containing the anchor
#   (caption sits at the page TOP; body begins at the anchor).
REMOVE_UNTIL = {
    433: "镇南关起义",        # Lidu Theatre plate (fig ch21-1)
    441: "带。到处有枪",       # League leaders group photo (fig ch21-2)
    475: "元培和我都被选为",   # Soong at League meeting (fig ch22-1)
}
#   TRUNCATE_AFTER: keep through the line containing the anchor, drop the rest
#   (caption sits at the page FOOT after the body).
TRUNCATE_AFTER = {
    478: "一直为军",           # Yang Xingfo's body plate (fig ch22-2)
}

# OCR-mangled sentence-ends / dropped text at paragraph seams -- verified on the
# scan.  Restores only; content garbles go through data/ocr_fixes.json.
RESTORE = {
}


def path(page):
    return os.path.join(TXT, "p%04d.txt" % page)


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
    hits = [i for i, l in enumerate(lines) if marker in l]
    if not hits:
        print("p%04d: FOOTNOTE MARKER '%s' NOT FOUND" % (page, marker))
        return
    if len(hits) > 1:
        print("p%04d: FOOTNOTE MARKER '%s' AMBIGUOUS (%d hits)"
              % (page, marker, len(hits)))
        return
    i = hits[0]
    new = lines[:i]
    while new and new[-1].strip() == "":
        new.pop()
    open(p, "w").write("\n".join(new) + "\n")
    print("p%04d: footnote truncated %d->%d lines at '%s'"
          % (page, len(lines), len(new), marker))


def remove_top_block(page, start, end_before):
    p = path(page)
    lines = open(p).read().split("\n")
    si = next((i for i, l in enumerate(lines) if start in l), None)
    ei = next((i for i, l in enumerate(lines) if end_before in l), None)
    if si is None or ei is None or si >= ei:
        print("p%04d: TOP_BLOCK anchors bad (si=%s ei=%s)" % (page, si, ei))
        return
    new = lines[:si] + lines[ei:]
    open(p, "w").write("\n".join(new))
    print("p%04d: top-block removed lines %d..%d (%r..%r)"
          % (page, si, ei - 1, start, end_before))


def remove_until(page, anchor):
    p = path(page)
    lines = open(p).read().split("\n")
    idx = next((i for i, l in enumerate(lines) if anchor in l), None)
    if idx is None:
        print("p%04d: REMOVE_UNTIL anchor %r NOT FOUND" % (page, anchor))
        return
    open(p, "w").write("\n".join(lines[idx:]))
    print("p%04d: removed %d head lines before %r" % (page, idx, anchor))


def truncate_after(page, anchor):
    p = path(page)
    lines = open(p).read().split("\n")
    idx = next((i for i, l in enumerate(lines) if anchor in l), None)
    if idx is None:
        print("p%04d: TRUNCATE_AFTER anchor %r NOT FOUND" % (page, anchor))
        return
    open(p, "w").write("\n".join(lines[:idx + 1]) + "\n")
    print("p%04d: kept through %r, dropped %d tail lines"
          % (page, anchor, len(lines) - idx - 1))


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
    for pg, (st, eb) in TOP_BLOCK.items():
        remove_top_block(pg, st, eb)
    for pg, anc in REMOVE_UNTIL.items():
        remove_until(pg, anc)
    for pg, anc in TRUNCATE_AFTER.items():
        truncate_after(pg, anc)
    for pg, mk in FOOTNOTE_START.items():
        truncate(pg, mk)
    for pg, specs in HEADING_FIX.items():
        fix_headings(pg, specs)
    for pg, pairs in RESTORE.items():
        restore(pg, pairs)
