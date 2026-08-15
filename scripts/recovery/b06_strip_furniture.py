#!/usr/bin/env python3
# B06 (ch09 PDF 198-217, ch10 PDF 218-230) furniture strip, run on data/txt
# BEFORE assemble. Same disease as B02-B05: page-bottom author-footnotes eat the
# spanning paragraph's continuation, and two embedded photos inject OCR garbage.
#
# Order of operations:
#   1. Normalize garbled chapter/section headings to the EXACT book.json titles
#      (pulled by id, never hand-typed -- STYLE.md round-2 rule: proofread every
#      inserted hanzi).  assemble.py then auto-emits them as '### '.
#   2. INSERT the ch09 s04 heading on p214 -- BOTH OCR configs (psm6 + psm4)
#      dropped the bold "镇压叛徒绝不手软" heading in the gap; verified present on
#      the scan (folio 170).
#   3. Truncate 8 author-footnote blocks at a FOOTNOTE-ONLY substring marker.
#   4. Strip the two embedded photos: p210 (李一氓 at his desk, caption + garbage
#      after the last body line) and p225 (李文宜, garbage + caption BEFORE the
#      body).  The figures themselves are recorded in figures.json with alt+caption.
#   5. Drop the p225 leaked folio "181" (the photo shoved the folio into the body
#      crop).
#
# PER-TARGET heading guard len(good)+4 (a body line can share a heading's tokens).
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
    198: [(["行动科和", "红队"], "ch09"),
          (["魔术大师化广奇", "顾顺章"], "ch09s01")],
    203: [(["令敌胆丧", "打狗队"], "ch09s02")],
    210: [(["笔下", "苏维埃会议"], "ch09s03")],
    218: [(["红队利剑"], "ch10"),
          (["英国巡捕冲进罗亦农屋门"], "ch10s01")],
    221: [(["查找出卖罗亦农的叛徒"], "ch10s02")],
    224: [(["残躯何足", "大敌正当前"], "ch10s03")],
    229: [(["鞭炮声中"], "ch10s04")],
}

# page -> (tokens on the line AFTER which to insert, structure id to insert)
INSERT_AFTER = {214: (["以供读者欣赏"], "ch09s04")}

# page -> FOOTNOTE-ONLY substring on the first line of the footnote block.
FOOTNOTE_START = {
    202: "即现在的延安东路",  # gloss ① 爱多亚路 + ② 番摊 (四方摊); two-line block
    199: "文史资料",     # 《中统特工秘录》江苏文史资料编辑部1991年版
    201: "党的文献",     # 杜宁《叛徒顾顺章叛变的经过和教训》《党的文献》1991年第3期
    204: "党史资料丛刊",  # 《关于中央特科》上海《党史资料丛刊》1981年第2期
    214: "人民出版社",   # 李一氓《模糊的荧屏》人民出版社1992年版
    224: "转引",         # 谈话记录 ... 转引自上海《党史资料丛刊》1981 (2 OCR lines)
    226: "1980",         # 《张维桢同志谈话记录》1980年X月25日
    228: "谈话记录",     # 《黄阶然同志谈话记录》1980年4月1日
    230: "李维汉",       # 《李维汉同志谈话记录》1980年5月14日
}

# page -> marker; keep through the line containing marker, drop everything after
# (strips a trailing embedded photo + caption when no body follows it).
TRUNCATE_AFTER = {210: "并且参加了这次会"}   # 李一氓 photo + caption follow

# page -> marker; drop every line BEFORE the first line containing marker
# (strips a leading embedded photo + caption before the body resumes).
DELETE_BEFORE = {225: "委员长"}              # 李文宜 photo + caption precede

# page -> substrings; delete any line containing one (leaked folio junk).
DELETE_CONTAINS = {225: ["181"]}

# OCR dropped a run of characters (verified against the scan). Restore it so the
# assembler sees the whole sentence and the paragraph splits land cleanly.
# (wrong, right) applied to the page's text.
RESTORE = {
    200: [("他又曾表现晨",
           "他又曾表现畏怯动摇。")],               # 畏怯动摇。->晨 (folio 156)
    204: [("察队就武装起来了.中",
           "察队就武装起来了。")],                 # 。① mis-OCR'd .中 (folio 160)
    208: [("白讲等,在上海引起极大",
           "白讲等,在上海引起极大震动。")],       # dropped 震动。 (folio 164)
    213: [("全都被捕牺牲了，",
           "全都被捕牺牲了。")],                   # sentence-final 。->， (folio 169)
    222: [("很快查明:出卖罗亦",
           "很快查明:出卖罗亦农的就是何家兴和贺稚华。"),
          ("抽奢里的党的文件也未被抄走，",
           "抽奢里的党的文件也未被抄走。")],       # dropped run + 。->， (folio 178)
    226: [("我们看过.中",
           "我们看过。")],                         # 。① mis-OCR'd .中 (folio 182)
    227: [("从容步人刑场,英勇",
           "从容步人刑场,英勇就义。")],           # dropped 就义。 (folio 183)
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
            if len(s) > len(good) + 4:          # PER-TARGET guard
                continue
            if all(t in s for t in tokens):
                lines[i] = good
                changed += 1
                print("p%04d: heading '%s' -> '%s'" % (page, s, good))
    if not changed:
        print("p%04d: NO HEADING MATCHED %s" % (page, [t for t, _ in specs]))
    open(p, "w").write("\n".join(lines))


def insert_after(page, tokens, sid):
    p = path(page)
    lines = open(p).read().split("\n")
    good = TITLE[sid]
    for i, l in enumerate(lines):
        if all(t in l for t in tokens):
            lines.insert(i + 1, "")
            lines.insert(i + 2, good)
            open(p, "w").write("\n".join(lines))
            print("p%04d: inserted heading '%s' after '%s'"
                  % (page, good, l.strip()))
            return
    print("p%04d: INSERT ANCHOR %s NOT FOUND" % (page, tokens))


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


def truncate_after(page, marker):
    p = path(page)
    lines = open(p).read().split("\n")
    for i, l in enumerate(lines):
        if marker in l:
            new = lines[:i + 1]
            open(p, "w").write("\n".join(new) + "\n")
            print("p%04d: truncated-after %d->%d lines at '%s'"
                  % (page, len(lines), len(new), marker))
            return
    print("p%04d: TRUNCATE-AFTER MARKER '%s' NOT FOUND" % (page, marker))


def delete_before(page, marker):
    p = path(page)
    lines = open(p).read().split("\n")
    for i, l in enumerate(lines):
        if marker in l:
            new = lines[i:]
            open(p, "w").write("\n".join(new))
            print("p%04d: delete-before dropped %d leading lines at '%s'"
                  % (page, i, marker))
            return
    print("p%04d: DELETE-BEFORE MARKER '%s' NOT FOUND" % (page, marker))


def delete_contains(page, subs):
    p = path(page)
    lines = open(p).read().split("\n")
    keep = []
    for l in lines:
        if any(x in l for x in subs):
            print("p%04d: deleted junk line '%s'" % (page, l.strip()))
            continue
        keep.append(l)
    open(p, "w").write("\n".join(keep))


# Headings first (before truncation shifts lines away).
for pg, pairs in HEADING_FIX.items():
    fix_headings(pg, pairs)
for pg, (tok, sid) in INSERT_AFTER.items():
    insert_after(pg, tok, sid)
# Photo strips before footnote truncation (independent pages here, but keep the
# leading/trailing deletions grouped).
for pg, mk in TRUNCATE_AFTER.items():
    truncate_after(pg, mk)
for pg, mk in DELETE_BEFORE.items():
    delete_before(pg, mk)
for pg, subs in DELETE_CONTAINS.items():
    delete_contains(pg, subs)
for pg, pairs in RESTORE.items():
    p = path(pg)
    s = open(p).read()
    for wrong, right in pairs:
        if wrong in s:
            s = s.replace(wrong, right)
            print("p%04d: restored dropped run at '%s'" % (pg, wrong[:10]))
        else:
            print("p%04d: RESTORE ANCHOR '%s' NOT FOUND" % (pg, wrong[:10]))
    open(p, "w").write(s)
for pg, mk in FOOTNOTE_START.items():
    truncate(pg, mk)
