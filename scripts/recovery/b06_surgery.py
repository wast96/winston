#!/usr/bin/env python3
# B06 (ch09 PDF 198-217, ch10 PDF 218-230) paragraph re-segmentation, run on
# data/zh/ch09.txt and data/zh/ch10.txt AFTER assemble.
#
# The B06 disease is near-total: on the section-opener and block-quote pages the
# OCR dropped ALL paragraph blanks, so the assembler welded whole runs of source
# paragraphs; on a handful of pages a spurious blank/indent over-split one. Rather
# than a fragile weld-then-split, we RE-SEGMENT: within each section (the body
# between two headings) we concatenate every assembled body paragraph back into
# one blob -- exactly the continuous source text, since Chinese lines join with no
# space -- then split it at a verified list of paragraph-START markers.
#
# Every marker is a RAW-OCR substring (apply_fixes runs AFTER) verified to occur
# EXACTLY ONCE in its blob (the script refuses to apply otherwise). Markers were
# read paragraph-by-paragraph off the folios (154-186); see PROGRESS.md.
# NOT idempotent: re-assemble both units before re-running.
import os
import sys

ROOT = "/home/user/winston"
ZH = os.path.join(ROOT, "data", "zh")

# unit -> list of blobs (in reading order); each blob is the ordered list of
# paragraph-START markers for paragraphs 2..N (the split points; paragraph 1 is
# the text before the first marker). One blob per body-run between headings.
CONFIG = {
    "ch09": [
        # blob0 = s01 (魔术大师化广奇 -- 顾顺章), 9 paragraphs
        ["(1895", "1924年投机革命", "在这次武装起义中",
         "随中共中央转至武汉", "虽然身居高位", "还有一个当时还在",
         "美国作家约翰", "主要是领导红队"],
        # blob1 = s02 (令敌胆丧的打狗队), 23 paragraphs
        ["红队的出现早在", "有一个过程", "1925年6月下名", "针对这种情况",
         "从五州时期到上海工人", "反革命政变以后,白色恐怖",
         "大批共产党员和革命群众", "这年9月,中共中央机关",
         "当周恩来从香港回到上海", "红队在上海很出名", "在红队成立初期",
         "到1929年下半年", "红队归第三科领导", "预备会议的会场是由一科",
         "还为参加会议的同志租了", "保卫中共中央机关的安全",
         "红队在镇压叛徒奸细", "正是由于党对红队", "美国作家约翰",
         "为了采取较具实力的行动", "实施行动时用尽各种各样",
         "从1927年年中开始"],
        # blob2 = s03 (李一氓笔下的苏维埃会议), 9 paragraphs
        ["在上海开了一个全国苏维埃", "赵才人敏",
         "这个机关是顾顺章他们", "出席这个会议的人,实到", "这个会议开得很正式",
         "绝大部分不是真名字", "这个临时家庭就解散了",
         "这是笔者看到的有关"],
        # blob3 = s04 (镇压叛徒绝不手软), 12 paragraphs
        ["自从在敌人侦探机关内部", "戴冰石问国民党",
         "密捕后,杨登", "又发现了陈尉年秘密自首",
         "伪登注立刻把这些情况", "由于特科作了细致的调查",
         "黄埔军校第一期毕业生黄第洪", "首先看到这类自首信件",
         "黄第洪又名黄警魂", "接到徐恩曾的通知", "前后几年间,红队还除掉"],
    ],
    "ch10": [
        # blob0 = chapter intro, 2 paragraphs
        ["1928年4月415日,在上海发生了"],
        # blob1 = s01 (英国巡捕冲进罗亦农屋门), 8 paragraphs
        ["幼年时罗亦农在家乡读书", "1919年夏天,他不顾家庭",
         "他到上海进入一所中学", "被派到广州参加全国第二次",
         "离开武汉到达上海", "受中央委托巡视两",
         "许多中外报纸传出"],
        # blob2 = s02 (查找出卖罗亦农的叛徒), 7 paragraphs
        ["中共中央得知这些情况", "何家兴夫妇都曾留学莫斯科",
         "情况查明以后,中央特科立即", "关于营救亦农的计划",
         "我到了何家兴夫妇的住处", "罗亦农于4月18日就被引渡"],
        # blob3 = s03 (残躯何足惜大敌正当前), 12 paragraphs
        # the death poem is set as verse: split its two printed lines so each
        # renders as its own {p} line (残驱=残躯, 大政=大敌 fixed by apply_fixes)
        ["关押在我们牢房的后面一排", "唐瑞林上叛变我们当时",
         "早把生死置之度外", "怀慨登车去", "残驱何足惜", "在束义前",
         "敌人在龙华杀害了", "上海龙华刑场戒备森严",
         "党组织通知了李文宜", "罗亦农英勇牺牲后,党中央机关",
         "1928年三四月间", "是党的重大损失,引起全党"],
        # blob4 = s04 (叛徒在鞭炮声中毙命), 4 paragraphs
        ["我们已经通过内线知道是何家兴", "中央特科在接受了任务",
         "红队严惩叛徒何家兴夫妇的行动"],
    ],
}


def load(unit):
    return [l.rstrip("\n") for l in open(os.path.join(ZH, "%s.txt" % unit))]


def blobs_of(lines):
    """Return list of (heading_lines_before, body_paragraphs) runs. Actually we
    just need the ordered body-runs (each a list of body paragraph strings), plus
    the interleaved headings, to rebuild the file."""
    tokens = []  # ('H', text) or ('B', [paras])
    cur = []
    for l in lines:
        if not l.strip():
            continue
        if l.startswith("###"):
            if cur:
                tokens.append(("B", cur)); cur = []
            tokens.append(("H", l))
        else:
            cur.append(l)
    if cur:
        tokens.append(("B", cur))
    return tokens


def split_blob(text, markers, unit, bi):
    ok = True
    for m in markers:
        n = text.count(m)
        if n != 1:
            print("  %s blob%d: MARKER %r found %d times (need 1)"
                  % (unit, bi, m, n))
            ok = False
    if not ok:
        return None
    # verify order (each marker after the previous)
    pos = [text.index(m) for m in markers]
    if pos != sorted(pos):
        print("  %s blob%d: markers OUT OF ORDER %s" % (unit, bi, pos))
        return None
    pieces, rest = [], text
    for m in markers:
        i = rest.index(m)
        pieces.append(rest[:i]); rest = rest[i:]
    pieces.append(rest)
    # Snap each boundary back to the sentence end: a marker chosen a few
    # characters into its paragraph would otherwise leave that paragraph's
    # leading name/date stuck on the previous piece. Move the tail after the
    # last sentence-final punctuation of piece[i-1] onto the front of piece[i].
    BREAK = "。！？…：:!?"
    CLOSE = "”』」）】》"
    for i in range(1, len(pieces)):
        prev = pieces[i - 1]
        k = max((prev.rfind(c) for c in BREAK), default=-1)
        if k < 0:
            continue
        j = k + 1
        while j < len(prev) and prev[j] in CLOSE:
            j += 1
        # a trailing parenthetical/citation after the sentence end (e.g. a
        # "(《…》)" source attribution) belongs to the previous paragraph, not
        # the next -- do not move it forward.
        if j < len(prev) and prev[j] not in "(（《":
            pieces[i] = prev[j:] + pieces[i]
            pieces[i - 1] = prev[:j]
    return pieces


def process(unit, apply):
    lines = load(unit)
    tokens = blobs_of(lines)
    blob_markers = CONFIG[unit]
    out = []
    bi = 0
    ok = True
    for kind, val in tokens:
        if kind == "H":
            out.append(val)
        else:
            blob = "".join(val)   # concatenate assembled paras -> source text
            markers = blob_markers[bi]
            pieces = split_blob(blob, markers, unit, bi)
            if pieces is None:
                ok = False
            else:
                print("  %s blob%d: %d assembled -> %d paragraphs"
                      % (unit, bi, len(val), len(pieces)))
                out.extend(pieces)
            bi += 1
    if bi != len(blob_markers):
        print("  %s: expected %d blobs, saw %d" % (unit, len(blob_markers), bi))
        ok = False
    if ok and apply:
        with open(os.path.join(ZH, "%s.txt" % unit), "w") as fh:
            fh.write("\n".join(out) + "\n")
        body = [l for l in out if not l.startswith("###")]
        print("  %s WRITTEN: %d body paragraphs, %d headings"
              % (unit, len(body), len([l for l in out if l.startswith('###')])))
    return ok


if __name__ == "__main__":
    apply = "--apply" in sys.argv
    allok = True
    for unit in ("ch09", "ch10"):
        print("===", unit, "===")
        allok &= process(unit, apply)
    if not apply:
        print("\nDRY RUN%s. Re-run with --apply to write."
              % ("" if allok else " -- FIX MARKERS FIRST"))
    elif not allok:
        print("\nSOME BLOBS FAILED -- file may be partially written; re-assemble.")
