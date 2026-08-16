#!/usr/bin/env python3
# B09 (ch15 PDF 296-320, ch16 PDF 321-332) furniture strip, run on data/txt
# BEFORE assemble. Follows the b08 model.
#
#   1. Normalize garbled section headings to the EXACT book.json titles
#      (pulled by id).  Only ch15s01 is garbled (— OCR'd as 一); the rest are
#      clean but re-asserted for safety.  assemble.py then auto-emits '### '.
#   2. RESTORE stray footnote-marker chars and OCR-dropped sentence-ends that
#      would weld two paragraphs.  All verified on the scan.
#   3. Truncate author-footnote blocks at a FOOTNOTE-ONLY substring marker.
#      (Reproduced as translator notes in notes.json.)
#
# NOTE: the two full-page image pages p305 (Mao letter facsimile) and p322
# (Longhua Garrison photo) are emptied separately; they sit mid-paragraph and
# the spanning paragraph is rejoined across the gap by assemble.
#
# PER-TARGET heading guard len(good)+4.
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
    296: [(["开拓新局面"], "ch15"),
          (["贡生", "省议员", "开明绅士刘少白"], "ch15s01")],
    304: [(["牧师和律师"], "ch15s02")],
    313: [(["向新闻界发展"], "ch15s03")],
    321: [(["开拓新局面"], "ch16"),
          (["淞沪警备司令部"], "ch16s01")],
    324: [(["第四号政治密查员"], "ch16s02")],
    330: [(["英法租界巡捕房"], "ch16s03")],
}

# OCR-dropped/mangled markers, spurious quotes, and welding fixes -- verified on
# the scan.  Restores only; content OCR garbles go through data/ocr_fixes.json.
RESTORE = {
    307: [("道。出", "道。")],                    # ① (OCR 出) at 冯玉祥 quote end (P7)
    308: [("保释出狱。\"G", "保释出狱。\"")],   # stray footnote-anchor ① (OCR G)
    318: [("编辑.中", "编辑。"),                   # 。① (OCR .中) at 陈养山 memoir end (CY3)
          ("情报机关昵习", "情报机关呢!")],       # ！ (OCR 习) at 陈养山 inline-quote end
    319: [("5个\n月0", "5个月。"),               # ① (OCR 0) at 李一氓 block-quote end
          ("红中\n社、\n\n周恩来", "红中社。周恩来")],  # 。 (OCR 、) at 筹办西安红中社 end
    328: [("魔术道具。.", "魔术道具。")],         # ① (OCR ascii .) at 千里香 paragraph end (P26)
    # ！ OCR'd as a non-break glyph that welds two dialogue turns.
    325: [("时运来了上", "时运来了!")],           # ！ (OCR 上) after Chen Datong's greeting
}

# page -> FOOTNOTE-ONLY substring on the first line of the footnote block.
FOOTNOTE_START = {
    306: "南粤",              # ①《西行漫记》,香港南粤出版社,1977年版,第22~23页。
    307: "黑龙江人民出版社",  # ①冯玉祥《我的生活》,黑龙江人民出版社1981年版,第564页。
    308: "抗战爆发后",        # ②《我的生活》第564页 + 浦化人 later-career note
    317: "纪念陈养山文集",    # ①《忆…重庆的战斗经历》《纪念陈养山文集》第49页。
    318: "纪念陈养山文集",    # ①《纪念陈养山文集》第127~128页。
    319: "模糊的荧屏",        # ①《模糊的荧屏》,第245~246页。(李一氓 memoir)
    324: "陆米强",            # ①余卫平、陆米强《龙华国民党淞沪警备司令部》…1983年第3辑。
    328: "后来查明",          # ①后来查明:…"罗迈"不是李维汉…(author content note)
    331: "文史资料",          # ①《我与上海法租界》,上海《文史资料选辑》1979年第6辑。
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
            print("p%04d: restored '%s' -> '%s'" % (page, repr(wrong), repr(right)))
        else:
            print("p%04d: RESTORE ANCHOR %r NOT FOUND" % (page, wrong))
    open(p, "w").write(s)


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
for pg, mk in FOOTNOTE_START.items():
    truncate(pg, mk)
