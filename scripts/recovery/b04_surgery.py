#!/usr/bin/env python3
# B04 (ch05, ch06) paragraph-boundary surgery, run on data/zh/ch05.txt and
# data/zh/ch06.txt AFTER assemble. The blank-line assembler force-breaks at page
# seams, welds paragraphs where the OCR dropped a blank, and OVER-splits set-off
# block quotes whose extra line spacing the OCR captured as blank lines
# (ch05 p130: the 宋治家 quote continuation, one paragraph, split into 9).
# Each operation is verified against the page scans (ch05 folios 79-95,
# ch06 folios 96-109). Splits first, then a single weld pass, per chapter.
import os

ROOT = "/home/user/winston/data/zh"

# ---- ch05 ---------------------------------------------------------------
# SPLITS: (unique substring identifying a welded paragraph, [split-before
# markers in text order]) -> the paragraph is cut before each marker.
CH05_SPLITS = [
    # the 阿英 memoir block (p128): narration-intro | quote-1 | quote-2 |
    # 1928-spring narration head
    ("年一直在芜湖和李克农",
        ["1926年岁划", "我不能忘记", "1928年存,李克农秘密转移到上海"]),
    # the 宋治家 memoir block (p129): 1928-spring narration tail |
    # 宋治家 quote intro | quote-1 | quote-2 head
    ("宣传革命文学",
        ["初到上海的时候没有找到", "……党组织决定我转到上海",
         "不久宫乔岩从小房间搬出去"]),
    # the 李克农 exam testimony (p130-131): narration intro | the quote
    ("以后他殉农曾经谈到",
        ["财时在国民党内主持特务工作"]),
]

# WELD_STARTS: a paragraph beginning with one of these merges into the
# paragraph immediately above it (single pass, so runs of them chain).
CH05_WELDS = [
    "卢敢地同栈人",          # p124 elegy-anecdote tail (intro para 3)
    "织者和领导人",          # p124 李克农 bio head (split by heading seam)
    "宣传革命文学",          # p129 1928-spring narration tail (seam)
    # the 宋治家 quote continuation, over-split by blank-line spacing on p130:
    "问话我概不回答", "一次他真生了气", "必须迅速离开", "和在桥头遇到",
    "滚攻的眼泪", "的天堂,穿人", "推车没那么容易", "底朝天。不久",
    "工。生活有了保障",
    "作,无孔不入",          # p133 陈立夫 letter tail (seam)
    "京长兴街挂牌行医",      # p135 钱壮飞 bio (across the p134 photo)
    "见,钱壮飞设计出",      # p137 张振华/传单 para tail (seam)
    "捕杀共产党人也很",      # p139 胡底 四一二 para tail (seam)
]

# ---- ch06 ---------------------------------------------------------------
CH06_SPLITS = [
    # 连德生 bio (p145): the 陈赓-sends-a-bodyguard tail | 连德生's biography
    ("及时得到杨登泳手上的情报",
        ["连德生是浙江"]),
    # the 内奸 intelligence block (p150-152): 山东省委 traitor |
    # 袁良 commendation | the 冒险家 reflection
    ("掌握的情报日益增多",
        ["1930年上半年,陈广通知杨登瀛", "看到这些情况,也许有人会问"]),
    # the s05 opening (p152): intro | Mao quote | 杨登瀛 example | narration
    ("在隐蔽战线的斗争中",
        ["日本帝国主义者和蒋介石能够用纵横", "杨登注的事例,就是周恩来",
         "的经过情况,证明中央特科"]),
    # the s05 close (p153): 从使用杨登瀛 narration tail | the final 拉出来 para
    ("机关建立的这个反和间谍关系",
        ["“拉出来”,就是采取各种各样"]),
]

CH06_WELDS = [
    "及时得到杨登泳手上的情报",  # p145 陈赓-bodyguard tail (seam, before bio split)
    "又从南京带来了什么新的任务",  # p148 seam tail
    "L作。徐恩曾还对杨登瀛",       # p150 徐恩曾 quote tail (seam)
    "提高,发挥作用也比较大",       # p150 seam tail
    "机关建立的这个反和间谍关系",  # p153 从使用杨登瀛 narration tail (seam)
]


def split_text(text, markers):
    pieces, rest = [], text
    for m in markers:
        i = rest.index(m)
        pieces.append(rest[:i])
        rest = rest[i:]
    pieces.append(rest)
    return [p for p in pieces if p]


def process(chapter, SPLITS, WELDS, fixups=None):
    path = os.path.join(ROOT, "%s.txt" % chapter)
    lines = [l.rstrip("\n") for l in open(path)]
    lines = [l for l in lines if l.strip() != ""]

    for ident, markers in SPLITS:
        for idx, l in enumerate(lines):
            if ident in l:
                pieces = split_text(l, markers)
                lines[idx:idx + 1] = pieces
                print("  %s split @ %-14s -> %d pieces"
                      % (chapter, ident[:10], len(pieces)))
                break
        else:
            print("  %s SPLIT IDENT NOT FOUND: %s" % (chapter, ident))

    out, welded = [], 0
    for l in lines:
        s = l.strip()
        if s.startswith("###"):
            out.append(l)
            continue
        if out and not out[-1].strip().startswith("###") \
                and any(s.startswith(a) for a in WELDS):
            out[-1] = out[-1] + l
            welded += 1
        else:
            out.append(l)

    if fixups:
        out = [fixups(l) for l in out]

    with open(path, "w") as fh:
        fh.write("\n".join(out) + "\n")

    body = [l for l in out if not l.strip().startswith("###")]
    heads = [l for l in out if l.strip().startswith("###")]
    print("  %s welds: %d -> %d body paragraphs, %d headings"
          % (chapter, welded, len(body), len(heads)))


def ch06_fixups(line):
    # OCR clipped the full stop that ends the p149 "运到南京。" paragraph.
    if line.strip().endswith("的两部汽车运到南京，"):
        return line.rstrip()[:-1] + "。"
    return line


process("ch05", CH05_SPLITS, CH05_WELDS)
process("ch06", CH06_SPLITS, CH06_WELDS, ch06_fixups)
