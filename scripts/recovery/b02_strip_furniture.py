#!/usr/bin/env python3
# Strip author-footnote blocks (they sit at page bottoms and, left in, break the
# paragraph accumulator and drop the continuation) and blank full-page photo
# pages, from the raw per-page OCR, so re-assembly joins paragraphs correctly.
import os
TXT = "/home/user/winston/data/txt"

# page -> substring marking the FIRST line of the footnote block; truncate there.
FOOTNOTE_START = {
    62: "中央特科一科的工作情况",
    66: "江苏省委",
    71: "党中央机关在上海的活动片断",
    72: "中共党史大事年表",
    73: "会审公堂",          # explanatory note about the Mixed Court
    75: "来信摘登",
    91: "秘密的岗位",
    92: "春节是公历",         # explanatory note about Chen Geng's death date
}
PHOTO_PAGES = [63, 68, 83]

def truncate(page, marker):
    p = os.path.join(TXT, "p%04d.txt" % page)
    lines = open(p).read().split("\n")
    for i, l in enumerate(lines):
        if marker in l:
            new = lines[:i]
            while new and new[-1].strip() == "":
                new.pop()
            open(p, "w").write("\n".join(new) + "\n")
            print("p%04d: truncated %d->%d lines at '%s'" % (page, len(lines), len(new), marker))
            return
    print("p%04d: MARKER '%s' NOT FOUND" % (page, marker))

for pg, mk in FOOTNOTE_START.items():
    truncate(pg, mk)
for pg in PHOTO_PAGES:
    open(os.path.join(TXT, "p%04d.txt" % pg), "w").write("\n")
    print("p%04d: blanked (photo page)" % pg)
