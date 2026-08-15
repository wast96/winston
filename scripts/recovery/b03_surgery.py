#!/usr/bin/env python3
# B03 (ch04) paragraph-boundary surgery, run on data/zh/ch04.txt AFTER assemble.
# The blank-line assembler force-breaks at every page seam and also welds a few
# paragraphs where the OCR dropped a blank line. Each operation below is verified
# against the page scan (folios 51-78). Splits first, then a single weld pass.
#
# Splits (one welded line carrying >1 source paragraph -> its true pieces):
#   - obituary block  (p58): intro | quoted obituary | Li Qiang paragraph
#   - Ke Lin intro    (p60): closing of the lead-in | Ke Lin's dates-and-origin
#   - Ke Lin's Macau  (p67): the Ye Ting paragraph | 17-years | the eulogy
#   - Chen SC's end   (p77): hardship | the breakout quote | the 1934 news
# Welds (a source paragraph the assembler split at a page seam or lost blank):
#   16 continuation lines, each merged back into the paragraph it belongs to.
import os

ZH = "/home/user/winston/data/zh/ch04.txt"

# (unique substring identifying the line, [split-before markers in text order])
SPLITS = [
    ("其中写道:刘易同志经受过",
        ["刘易同志经受过", "曾在中央特科长期和他"]),
    ("爱戴。柯麟(1900",
        ["柯麟(1900"]),
    ("留在澳门。从1935",
        ["从1935年到1951年", "自1951年起"]),
    ("待了六七个小时回年",
        ["回年六七月间", "1934年11月间"]),
]

# Continuation lines: each merges into the paragraph immediately above it.
WELD_STARTS = [
    "是:正是",                 # p52  刘鼎 birth para
    "国以前,跟朱德",           # p55  Germany
    "关系巧妙地向刘",           # p57  Wu Xianqing (photo seam)
    "经考验的我党优秀党员",     # p58  obituary intro tail
    "经历十分了解,对他多次",   # p59  Li Qiang paragraph tail
    "单命群众。以后他被派",     # p60  Ke Lin lead-in tail
    "国创办的一所医学",         # p61  Ke Lin origin tail
    "一处",                     # p65  Deng Xiaoping remark
    "当时叶挺刚从国外回来",     # p67  Ye Ting paragraph tail
    "会,进行社会调查",         # p70  Yun Daiying
    "上海,再转发各地",         # p71  Yang Dengying (spurious blank)
    ":起对这一章文稿",         # p73  author interview (spurious blank)
    "|人作的创建",             # p74  author interview tail
    "发生",                     # p71  Chen Yangshan (April 12; sentence "不久发生")
    "颖,勤奋学习",             # p75  Chen SC telegraph
    "移。在异",                 # p77  Chen SC hardship tail
    "湖南是进的消息",           # p78  Chen SC death tail
]


def split_text(text, markers):
    pieces, rest = [], text
    for m in markers:
        i = rest.index(m)
        pieces.append(rest[:i])
        rest = rest[i:]
    pieces.append(rest)
    return [p for p in pieces if p]


def main():
    lines = [l.rstrip("\n") for l in open(ZH) if l.strip("\n") != "" or True]
    lines = [l for l in lines if l.strip() != ""]

    # 1) splits
    for ident, markers in SPLITS:
        for idx, l in enumerate(lines):
            if ident in l:
                pieces = split_text(l, markers)
                lines[idx:idx + 1] = pieces
                print("split @ %-18s -> %d pieces" % (ident[:12], len(pieces)))
                break
        else:
            print("SPLIT IDENT NOT FOUND: %s" % ident)

    # restore the OCR-clipped full stop at the Chen Shouchang hardship seam
    for idx, l in enumerate(lines):
        if l.strip().startswith("移。在异") and not l.rstrip().endswith("。"):
            lines[idx] = l.rstrip() + "。"
            print("restored clipped '。' on hardship paragraph")
            break

    # 2) single weld pass
    out = []
    welded = 0
    for l in lines:
        s = l.strip()
        if s.startswith("###"):
            out.append(l)
            continue
        if out and not out[-1].strip().startswith("###") \
                and any(s.startswith(a) for a in WELD_STARTS):
            out[-1] = out[-1] + l
            welded += 1
        else:
            out.append(l)

    with open(ZH, "w") as fh:
        fh.write("\n".join(out) + "\n")

    body = [l for l in out if not l.strip().startswith("###")]
    heads = [l for l in out if l.strip().startswith("###")]
    print("welds applied: %d" % welded)
    print("final: %d body paragraphs, %d headings" % (len(body), len(heads)))


if __name__ == "__main__":
    main()
