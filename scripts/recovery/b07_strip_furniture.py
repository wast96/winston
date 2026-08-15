#!/usr/bin/env python3
# B07 (ch11 PDF 231-246, ch12 PDF 247-262) furniture strip, run on data/txt
# BEFORE assemble. Same disease as B02-B06: page-bottom author-footnotes eat the
# spanning paragraph's continuation, embedded photos/facsimiles inject OCR
# garbage, and one section heading was dropped by BOTH OCR configs.
#
# Order of operations:
#   1. Normalize garbled chapter/section headings to the EXACT book.json titles
#      (pulled by id, never hand-typed).  assemble.py then auto-emits '### '.
#   2. INSERT the ch11 s02 heading "武装营救未能奏效" on p239 -- both OCR configs
#      dropped it; verified present on the scan (folio 195).
#   3. RESTORE OCR-dropped sentence-ends / a colon that introduces a block quote,
#      so the assembler's splits land cleanly.
#   4. Strip embedded figures (a full-page photo p232, the Hehe Fang map p251, and
#      the two newspaper facsimiles p254/p257).  The figures themselves are
#      recorded in figures.json with alt+caption.
#   5. Truncate author-footnote blocks at a FOOTNOTE-ONLY substring marker.
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
    231: [(["路侧的枪声"], "ch11"),
          (["针对周恩来"], "ch11s01")],
    243: [(["四烈士英勇就义"], "ch11s03")],
    247: [(["路侧的枪声"], "ch12"),
          (["穷追叛徒"], "ch12s01")],
    251: [(["叛徒倒毙在红队枪口下"], "ch12s02")],
    259: [(["镇压叛徒的英雄"], "ch12s03")],
}

# page -> (tokens on the line AFTER which to insert, structure id to insert)
INSERT_AFTER = {239: (["以免组织继续遭到破坏"], "ch11s02")}

# OCR-dropped sentence-ends, stray footnote-marker chars, and one dropped run --
# all verified on the scan. These sit at TRUE paragraph boundaries; without them
# the surgery boundary-snap misattributes a paragraph's tail to the next one.
RESTORE = {
    234: [("的发展。史", "的发展。")],              # stray ① after Qu Qiubai quote (f188)
    236: [("省于委秘书，", "省于委秘书。"),          # dropped 。 before Xing Shizhen bio
          ("国民党反动派进行斗争", "国民党反动派进行斗争。")],  # dropped 。 before Zhang bio
    237: [("的事件。吓", "的事件。")],              # stray ① after Zhou article quote (f193)
    238: [('逮捕带走。"岂', "逮捕带走。”")],        # stray ② after Ke Lin quote (f194)
    # BOTH OCR configs dropped the closing 。” of the martyrs' Zhou-article quote #4
    244: [("孝揭其为党努力", "孝揭其为党努力。”"),
    # and the joint-signature line of the final report ("挼 安" -- Yang Yin's alias
    # 孟挼 + Peng Pai's alias 孟安, folio 200); restore both.
          ("余人还坚持不认，", "余人还坚持不认。挼安")],
    246: [("回前斗争号", "回前斗争!”")],           # dropped closing !” of Zhou quote #8 (f202)
    248: [('接济他们。"史', "接济他们。”")],        # stray ① after Ke Lin quote (f204)
    249: [("去出\n诊，", "去出\n诊。")],            # dropped 。 before 果然 paragraph (f205)
    250: [("病。'因此", "病。”因此")],              # stray ① -> closing ” before 因此 (f206)
    # OCR dropped the run 一的大暗杀案"。 (the 一 wrapped and was lost); verified f209
    253: [("说是“东方惟", "说是“东方惟一的大暗杀案”。"),
          ("该报记者写道，", "该报记者写道：")],  # colon introduces 时报 quote (folio 209)
}

# page -> replacement content. The retyped 字林西报 translation's first paragraph
# on p257 sits directly under the English facsimile and both OCR configs mangled
# it beyond repair; transcribed clean off the scan (folio 213). It welds with the
# clean p258 continuation ("杀了四人...").
OVERWRITE = {
    257: "法租界巡捕房正在调查一起前所未有的行刺案件。星期一晚10时左右在通往霞飞路的"
         "一条胡同里(离“孔雀东方戏院”不远),一群身份不明的人当场枪\n",
}

# page -> marker; drop every line BEFORE the first line containing marker
# (strips a leading embedded photo/facsimile + caption before the body resumes).
DELETE_BEFORE = {
    251: "制定周密的行动计划",   # Hehe Fang map + caption precede the body resume
    254: "前晚十点钟许",         # 时报 facsimile + caption precede the reprinted article
}

# page -> True: blank the whole page (a full-page photo, body flows around it).
BLANK = {232: True}   # 彭湃 arrest-site photo (folio 188)

# page -> FOOTNOTE-ONLY substring on the first line of the footnote block.
FOOTNOTE_START = {
    234: "人民出版社",   # ①柯麟《回忆彭湃》人民出版社1992年版 + ②中共中央《以群众…》
    237: "本文刊载",     # 本文刊载于1930年8月13日《红旗日报》
    238: "人民出版社",   # 柯麟《回忆彭湃》人民出版社1992年版,第214~215页
    242: "阶前白刃",     # 《阶前白刃明如霜——…》《中华英烈》1986年第5期
    243: "214页",        # 柯麟《回忆彭湃》,第214页
    248: "216",          # 《回忆彭湃》,第216~217页
    250: "215",          # 《回忆彭湃》,第215~216页
    253: "1929年",       # 1929年11月13日《时报》 (body uses 11月13日, not 1929年)
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
            if len(s) > len(good) + 4:
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


def restore(page, pairs):
    p = path(page)
    s = open(p).read()
    for wrong, right in pairs:
        if wrong in s:
            s = s.replace(wrong, right)
            print("p%04d: restored '%s' -> '%s'" % (page, wrong, right))
        else:
            print("p%04d: RESTORE ANCHOR '%s' NOT FOUND" % (page, wrong))
    open(p, "w").write(s)


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


def blank(page):
    open(path(page), "w").write("\n")
    print("p%04d: BLANKED (full-page figure)" % page)


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


for pg, pairs in HEADING_FIX.items():
    fix_headings(pg, pairs)
for pg, (tok, sid) in INSERT_AFTER.items():
    insert_after(pg, tok, sid)
for pg, pairs in RESTORE.items():
    restore(pg, pairs)
for pg, mk in DELETE_BEFORE.items():
    delete_before(pg, mk)
for pg in BLANK:
    blank(pg)
for pg, mk in FOOTNOTE_START.items():
    truncate(pg, mk)
for pg, text in OVERWRITE.items():
    open(path(pg), "w").write(text)
    print("p%04d: OVERWRITTEN with clean scan transcription" % pg)
