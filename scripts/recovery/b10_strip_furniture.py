#!/usr/bin/env python3
# B10 (ch17 PDF 333-363, ch18 PDF 364-388) furniture strip, run on data/txt
# BEFORE assemble.  Follows the b09 model.
#
#   1. Normalize garbled section/chapter headings to the EXACT book.json titles.
#   2. Empty the SEVEN figure/facsimile pages so the spanning paragraph rejoins:
#      p334 Li Qiang portrait (photo at foot, caption after a complete para),
#      p341 first-station photo (top), p356 Li Qiang letter facsimile (top),
#      p358 Mao calligraphy (top), p362 1945 Yan'an group photo (mid, + its
#      footnote), p382 Tu Zuochao portrait (top), p385 Li Xiangwu portrait (mid).
#   3. Truncate author-footnote blocks (source citations / content notes),
#      reproduced as "Author's note." translator notes in notes.json.
#   4. RESTORE OCR-mangled sentence-ends at paragraph seams (the b09 lesson).
#
# NOT idempotent on the raw txt: restore from data/txt_backup_b10 before re-run.
import json
import os
import sys

ROOT = "/home/user/winston"
TXT = os.path.join(ROOT, "data", "txt")
BACKUP = os.path.join(ROOT, "data", "txt_backup_b10")

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
    333: [(["电讯科长"], "ch17"),
          (["党的电讯事业创始人李强"], "ch17s01")],
    337: [(["为党造出第一部收发报机"], "ch17s02")],
    342: [(["到香港建立电台"], "ch17s03")],
    346: [(["培训党的第一代报务员"], "ch17s04")],
    355: [(["划时代的通信"], "ch17s05")],
    364: [(["永不消", "红色电波"], "ch18"),
          (["留日电机专家"], "ch18s01")],
    370: [(["党的第一个报务员张沈川"], "ch18s02")],
    375: [(["留苏专家毛齐华"], "ch18s03")],
    381: [(["木匠", "涂作潮"], "ch18s04")],
}

# figure pages -- ("before", marker): drop everything BEFORE the first line whose
# stripped text contains marker (photo+caption sits at page top);
# ("after", marker): keep up to and including the first line containing marker,
# drop the rest (photo/caption/footnote sits at page foot).
FIGURE = {
    334: ("after", "卓越领导人"),      # Li Qiang portrait, caption 李强在工作中
    341: ("before", "才能做完"),        # first-station photo + caption
    356: ("before", "法利用电台"),      # Li Qiang letter facsimile + caption
    358: ("before", "问对方在何处"),    # Mao calligraphy + caption
    362: ("after", "的报纸"),           # 1945 Yan'an group photo (+ its footnote)
    382: ("before", "森的继兄"),        # Tu Zuochao portrait + caption
    385: ("after", "已被处决"),         # Li Xiangwu portrait + caption
}

# page -> distinctive substring on the FIRST line of the footnote block; the
# block runs from there to the page foot.  (p362's footnote already goes with
# its figure above.)
FOOTNOTE_START = {
    336: "我的革命历程",       # 李强《我的革命历程》《中共党史资料》第49辑
    339: "忆过极厚同志",       # 李强《忆蔡叔厚同志》1984-02-11 人民日报
    340: "难忘的回忆",         # 张沈川《难忘的回忆》《难忘的战斗岁月》第21页
    342: "中共党史出版社",     # 《一次划时代的通信革命》《红军的耳目与神经》第1页
    343: "红军的耳目与神经》?第3页",  # 同前 第3页
    344: "第12页",             # 《"地下"无线电波》第12页 + 《难忘的回忆》第23页
    348: "地下电波",           # 伍云甫《"地下"电波》第28、31页
    351: "第24~26页",          # 张沈川《难忘的记忆》第24-26页 + 毛齐华 第18-19页
    352: "第35",               # 涂作潮《"木匠"的回忆》第35页
    359: "从半部电台开始",     # 王诤《从半部电台开始》第52页 + 同前 第8页
    361: "长征路上",           # 黎平《长征路上》第146页 + 《收译密电》第119-120页
    363: "耳目与神经?第5页",   # 《红军的耳目与神经》第5页
    366: "忆殖叔厚同志",       # 李强《忆蔡叔厚同志》人民日报
    368: "中共党史人物传",     # 刘瑜《蔡叔厚》《中共党史人物传》第27卷
    370: "1984年2月1日",       # 李强《忆蔡叔厚同志》人民日报（本节引文出处）
    374: "此处及本节",         # 张沈川引文均见《难忘的记忆》
    377: "我党早期的",         # 毛齐华《我党早期的"地下"电台》第17页
    381: "上海工运",           # 《毛泽东关于白区工作的一次谈话》《上海工运史资料》
    387: "赎救张辉",           # 晓农、冯都《赎救张辉瓒》《纵横》2001年第9期
    388: "木区\"的回忆",       # 涂作潮《"木匠"的回忆》第42页
}

# OCR-mangled sentence-ends / footnote-marker chars at paragraph seams -- verified
# on the scan.  Restores only; content garbles go through data/ocr_fixes.json.
RESTORE = {
    # ch17s05: OCR dropped "满怀地写道:" before Li Qiang's closing block quote,
    # leaving the intro paragraph without its sentence-ending colon.
    363: [("文章中,豪情", "文章中,豪情满怀地写道:")],
    # ch18s03: "。'另" (quote-close + new paragraph) OCR'd as the single glyph 必,
    # welding Mao Qihua's retreat quote to the following narration.
    380: [("必据毛齐华回忆", "。另据毛齐华回忆")],
    # ch17s04: OCR dropped the line "表交待。" ending the sixth training-班 measure,
    # so the six-measures list had no sentence-end and the surgery snap pulled it
    # into the next paragraph.  Restored from the scan (printed p.305).
    349: [("假履历\n尽管制定了这些规定", "假履历表交待。\n尽管制定了这些规定")],
    # ch17s02: OCR dropped the period ending "...划时代意义的革命。" (printed p.298).
    342: [("划时代意义的革命", "划时代意义的革命。")],
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


def figure(page, mode, marker):
    p = path(page)
    lines = open(p).read().split("\n")
    hit = None
    for i, l in enumerate(lines):
        if marker in l:
            hit = i
            break
    if hit is None:
        print("p%04d: FIGURE MARKER %r NOT FOUND" % (page, marker))
        return
    if mode == "before":
        new = lines[hit:]
        print("p%04d: dropped %d leading fig lines (resume %r)"
              % (page, hit, marker))
    else:  # after
        new = lines[:hit + 1]
        print("p%04d: kept %d lines through %r, dropped %d"
              % (page, hit + 1, marker, len(lines) - hit - 1))
    open(p, "w").write("\n".join(new))


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
    # figures and footnotes first (they truncate), then headings, then restores
    for pg, (mode, mk) in FIGURE.items():
        figure(pg, mode, mk)
    for pg, mk in FOOTNOTE_START.items():
        truncate(pg, mk)
    for pg, specs in HEADING_FIX.items():
        fix_headings(pg, specs)
    for pg, pairs in RESTORE.items():
        restore(pg, pairs)
