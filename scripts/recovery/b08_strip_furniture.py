#!/usr/bin/env python3
# B08 (ch13 PDF 263-275, ch14 PDF 276-295) furniture strip, run on data/txt
# BEFORE assemble. Same disease as B02-B07: page-bottom author-footnotes eat the
# spanning paragraph's continuation, one embedded photo injects a caption line,
# and several section headings are garbled by BOTH OCR configs.
#
# Order of operations:
#   1. Normalize garbled chapter/section headings to the EXACT book.json titles
#      (pulled by id, never hand-typed).  assemble.py then auto-emits '### '.
#   2. RESTORE stray footnote-marker chars (OCR read the superscript circled
#      numbers as 包/中/? ) and two spurious leading quotation marks that OCR
#      produced from the paragraph indent.  All verified on the scan.
#   3. DROP the single embedded-photo caption line (p278, the Yipin Xiang hotel).
#      The figure itself is recorded in figures.json with alt+caption.
#   4. Truncate author-footnote blocks at a FOOTNOTE-ONLY substring marker.
#      (The footnote texts are reproduced as translator notes in notes.json.)
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
    263: [(["营救任缠时"], "ch13"),
          (["两次营救任强时"], "ch13s01")],
    266: [(["第二次被捕"], "ch13s02")],
    270: [(["名救关向应"], "ch13s03")],
    276: [(["开操新局面"], "ch14"),
          (["纠正了单纯恐怖行动"], "ch14s01")],
    279: [(["旷世奇才杨度"], "ch14s02")],
    287: [(["两个国会议员"], "ch14s03")],
}

# OCR-dropped/mangled footnote markers and two spurious leading quotes -- all
# verified on the scan. These sit at TRUE paragraph boundaries; without them the
# surgery boundary-snap misattributes a paragraph's tail to the next one.
RESTORE = {
    265: [("“这时,在上海的陈玉英", "这时,在上海的陈玉英"),    # spurious lead quote (f221)
          ("“与任中时同时囚押", "与任中时同时囚押")],           # spurious lead quote (f221)
    266: [("稳定下来。包", "稳定下来。")],                       # stray ① (OCR 包) after 戴映东 quote (f222)
    274: [("交保释放。?", "交保释放。")],                        # stray ① (OCR ?) after 张纪恩 quote (f230)
    282: [("秘密党员。中", "秘密党员。")],                       # stray ① (OCR 中) after 尹骐 quote (f238)
    286: [("写上。\"中", "写上。\"")],                            # stray ① (OCR 中, ASCII " quote) after 周恩来 quote (f242)
    275: [("吴露.", "吴露。")],                                  # sentence-end 。 OCR'd as ASCII '.' at 李沫英 quote end, wraps a line (f231)
    284: [("无恶不作的反动人", "无恶不作的反动人物。")],         # OCR dropped the 2-char trailing line "物。" ending the Du Yuesheng bio (f240)
    285: [("挡风雯", "挡风墙罢了。")],                           # OCR misread 墙 and dropped the short trailing line "罢了。" ending P9 (f241)
}

# page -> substring; delete any single line containing it (an embedded-photo
# caption sitting mid-page while the body flows around the image).
DROP_LINE = {
    278: "位于西藏中路",   # 一品香旅社 caption (folio 234)
}

# page -> FOOTNOTE-ONLY substring on the first line of the footnote block.
FOOTNOTE_START = {
    266: "章学新主编",    # ①章学新主编《任弼时传》人民出版社、中央文献出版社1994
    269: "浙江青年",      # ①周朴农口述《难忘的三十九天》《浙江青年》1982年第12期
    274: "党史资料丛刊",  # ①张纪恩《周恩来同志在上海革命活动片断及其他》上海《党史资料丛刊》
    275: "党史资料丛刊",  # ①李沫英《1931年我在狱中知道的一些情况及其他》上海《党史资料丛刊》
    282: "潘汉年",        # ①尹骐《潘汉年的情报生涯》人民出版社1976年版
    283: "极右翼的",      # ①政学系是1916年…极右翼的政治派系  +  ②改组派/西山会议派
    286: "1978年",        # ①王冶秋《难忘的记忆》1978年7月30日《人民日报》
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


def drop_line(page, marker):
    p = path(page)
    lines = open(p).read().split("\n")
    keep = [l for l in lines if marker not in l]
    if len(keep) == len(lines):
        print("p%04d: DROP-LINE MARKER '%s' NOT FOUND" % (page, marker))
    else:
        print("p%04d: dropped %d line(s) at '%s'"
              % (page, len(lines) - len(keep), marker))
    open(p, "w").write("\n".join(keep))


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
for pg, pairs in RESTORE.items():
    restore(pg, pairs)
for pg, mk in DROP_LINE.items():
    drop_line(pg, mk)
for pg, mk in FOOTNOTE_START.items():
    truncate(pg, mk)
