#!/usr/bin/env python3
# B05 (ch07, ch08) paragraph-boundary surgery, run on data/zh/ch07.txt and
# data/zh/ch08.txt AFTER assemble.  Two disease patterns here:
#   - PAGE-SEAM force-breaks: the assembler flushes at every page boundary, so a
#     paragraph that spans a page turn is split.  Welded back (WELD_STARTS).
#   - OCR-DROPPED BLANKS across p168-p170: the 侦缉队长 story, the Liu Bocheng
#     escort intro, and the 7-paragraph SET-OFF block quote (biographer's
#     account) run indent-only with no blank lines, so tesseract welded ~12
#     source paragraphs into one.  Split back (CH07_SPLITS).
# Two tail fixes restore punctuation the OCR mis-read at a real paragraph end
# (p157 科长。read as 科长，; p165 视做"亲信"。clipped to 视做"亲).
# Verified against the page scans (ch07 folios 110-128, ch08 folios 129-153;
# openers p154/p173, block quote p170, memoir p176/p178/p184 eyeballed).
# NOT idempotent: re-assemble before re-running.
import os

ROOT = "/home/user/winston/data/zh"

# ---- ch07 --------------------------------------------------------------
# Under-splits: on p159-p161 the OCR emitted NO blank lines, so the assembler
# welded distinct source paragraphs. Verified paragraph-by-paragraph against the
# folios (110-128). Split back here.
CH07_SPLITS = [
    # s02 p158-160: the "Bring it over" narrative is 4 source paragraphs
    ("徐恩曾开始担任",
     ["这时,钱壮飞已经深得",
      "怎么办?钱壮飞和李克农",
      "徐恩曾到南京一上任"]),
    # s02 p160-162: the Song Jiren memoir region is 4 source paragraphs
    ("许多年后,宋治家",
     ["宋季仁还曾谈到1931年",
      "李克农把搞到的文件叫我送到",
      "党务调查科的办公地址原在南京"]),
    # s03 p162-164: descriptions | Zou Taofen account
    ("关于徐恩曾的外狐和人品",
     ["邹友奋和徐恩曾是南洋"]),
    # The p168-p170 blob (identifier -> split-before markers in text order).
    ("就这样,在中央的领导下",
     ["“龙潭三杰\"除了探取敌人的情报",
      "有时他们还利用国民党机关没人敢惹",
      "1930年初,刘伯承刚从苏联回到上海",
      "李克农按照约定的时间,冒十来到外滩公园",
      "身穿蓝色绸缕长袍的李克农",
      "一辆雪佛莱轿车从远处驶来",
      "汽车启动后,坐在前座的李克农",
      "李立三指指坐在身边的人说",
      "李克农急忙伸过手来紧紧担住",
      "刘伯承不动声色地微微一笑说",
      "在火车的头等车厅里"]),
]

# merge up into the paragraph immediately above (single pass; runs chain)
CH07_WELDS = [
    "度下野去日本",              # p154->155 seam (footnote-truncated)
    "党务调查上面了",            # p158->159 seam
    "里混日子",                  # p161->162 seam
    "人\" ,二则以此作为",        # p162->163 seam
    "此,你何必对我说",           # p163->164 seam
    "了儿女。后来朋友学成",       # p164->165 seam
    "后,这里不但建立起",         # p165->166 seam
    "公开情报机构:在南京丹凤街",  # p166->167 seam
    "了刘伯承离六的情报",         # p170->171 seam (block-quote tail)
    "身一人将刘伯承送往南京的",   # p171 seam (block-quote tail)
    "敌情,与敌人进行针锋相对",    # p171->172 seam
]

# ---- ch08 --------------------------------------------------------------
# Under-splits on the two section-opener pages (p187 s03, p192 s05), where the
# OCR emitted a blank after the heading but none between the body paragraphs.
# Every other memoir page carried its blanks and assembled clean (verified
# against folios 129-153).
CH08_SPLITS = [
    # s03 p187: work-problem intro | Yang Bingsen | the arrest
    ("老昔找到我研究刘伯刚",
     ["杨炳森又名杨凤璋",
      "除此之外,刘伯刚还常到东陵"]),
    # s05 p192: what打铺保 is | social ties | 1930 arrests | the Korean couple
    ("我的另一项工作任务就是为同志们打铺保",
     ["我有很多社会关系",
      "1930年满洲省委遭破获",
      "那时朝鲜同志自己没有独立的党"]),
]

CH08_WELDS = [
    "留学和参加党的经过,赵唯刚回",   # p173->174 seam (into "关于赴日")
    "报》上。这是我下决心走革命",    # p174->175 seam
    "月10日,我在日本由李人一",      # (in-memoir seam)
    "入中国共产党,在中共日本",      # (in-memoir seam)
    "人来了,叫你到日本站悦来客栈",   # p178->179 seam
    "间了他一些问题以后,就备了个",   # p187->188 seam (footnote-truncated)
    "被杀害。因老胡在沈阳的房子",    # p191->192 seam
    "人印了任,但仍有电话、房子",    # p192->193 seam (footnote-truncated)
    "这种警察也是便衣",             # p195->196 seam
]


def split_text(text, markers):
    pieces, rest = [], text
    for m in markers:
        i = rest.index(m)
        pieces.append(rest[:i])
        rest = rest[i:]
    pieces.append(rest)
    return [p for p in pieces if p]


def ch07_fixups(line):
    s = line.rstrip()
    # p157: real paragraph end mis-read as a comma
    if s.endswith("专任中央组织部党务调查科科长，"):
        return s[:-1] + "。"
    # p165: 视做"亲信"。 clipped to 视做"亲
    if "倚为他的左右手,视做" in s and s.endswith("亲"):
        return s + "信”。"
    # p171: block-quote tail 南京的。① mis-read as 南京的.中
    if s.endswith("身一人将刘伯承送往南京的.中"):
        return s[:-2] + "。"
    # p171: OCR dropped the last line of the 李克农 quote before the s05 heading;
    # restored from the scan (folio 127): "...就在中央饭店楼上一住……"
    if s.endswith("到了南京,就在中"):
        return s + "央饭店楼上一住……”"
    # p161: block-quote paragraph P8 ends 避免了一次损失。① — the 。 was eaten at
    # the split boundary with the next paragraph
    if s.endswith("避免了一次损失"):
        return s + "。"
    # p163: descriptions paragraph ends 干得出来。"② — strip the note-ref glyph
    if s.endswith("什么事他都干得出来。\"@"):
        return s[:-1]
    return line


def process(chapter, SPLITS, WELDS, fixups=None):
    path = os.path.join(ROOT, "%s.txt" % chapter)
    lines = [l.rstrip("\n") for l in open(path)]
    lines = [l for l in lines if l.strip() != ""]

    # WELDS FIRST: reunite page-seam force-breaks, so a paragraph the OCR split
    # across a page turn is whole again before we break the under-splits.
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
    lines = out

    # SPLITS SECOND: break the paragraphs the OCR welded because it emitted no
    # blank line (a split region may span a weld we just healed).
    for ident, markers in SPLITS:
        for idx, l in enumerate(lines):
            if ident in l:
                pieces = split_text(l, markers)
                lines[idx:idx + 1] = pieces
                print("  %s split @ %-12s -> %d pieces"
                      % (chapter, ident[:10], len(pieces)))
                break
        else:
            print("  %s SPLIT IDENT NOT FOUND: %s" % (chapter, ident))

    if fixups:
        lines = [fixups(l) for l in lines]

    with open(path, "w") as fh:
        fh.write("\n".join(lines) + "\n")

    body = [l for l in lines if not l.strip().startswith("###")]
    heads = [l for l in lines if l.strip().startswith("###")]
    print("  %s welds: %d -> %d body paragraphs, %d headings"
          % (chapter, welded, len(body), len(heads)))


process("ch07", CH07_SPLITS, CH07_WELDS, ch07_fixups)
process("ch08", CH08_SPLITS, CH08_WELDS)
