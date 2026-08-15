#!/usr/bin/env python3
# B08 (ch13 PDF 263-275, ch14 PDF 276-295) paragraph re-segmentation, run on
# data/zh/ch13.txt and data/zh/ch14.txt AFTER assemble.
#
# Same method as b06/b07: within each section (the body between two headings) we
# concatenate every assembled body paragraph back into one blob -- exactly the
# continuous source text -- then split it at a verified list of paragraph-START
# markers.  markers[i] starts piece i+1; piece 0 is the blob head, so a blob of
# N paragraphs needs N-1 markers.  Every marker is a RAW-OCR substring
# (apply_fixes runs AFTER surgery) read paragraph-by-paragraph off folios 219-251
# and verified to occur EXACTLY ONCE in its blob (the script refuses otherwise).
# NOT idempotent: re-assemble both units before re-running.
#
# ch13: preamble 2, s01 8, s02 11, s03 13  (34 body + 4 headings)
# ch14: s01 7, s02 17, s03 20              (44 body + 4 headings)
import os
import sys

ROOT = "/home/user/winston"
ZH = os.path.join(ROOT, "data", "zh")

CONFIG = {
    "ch13": [
        # blob0 = preamble (chapter opener, before s01), 2 paragraphs
        ["前文已经讲过,对于不幸被捕"],
        # blob1 = s01 (两次营救任弼时), 8 paragraphs
        ["原名任培国", "1928年3月,中共临时中央政治局决定",
         "是1928年10月在安徽南陵县被捕", "南陵县法院会同国民党县党部",
         "在上海的陈玉英接到任理卿", "与任中时同时囚押",
         "当国民党安徽省法院派人到长沙"],
        # blob2 = s02 (任弼时第二次被捕), 11 paragraphs
        ["罗迈一见陈", "从中央特科得到这一消息后,就打发",
         "去开会的地点早被敌人发现", "用严刑拷打,甚至施用电刑",
         "当时在上海总工会任青工部长", "敌人不相信我们的口供,对我们两次用刑",
         "一被捕,中共中央就令中央特科抓紧营救", "周朴农在前引的文章中回忆道",
         "11月22日,上海公共租界会审公堂", "12月25日,当租界里洋人过"],
        # blob3 = s03 (营救关向应), 13 paragraphs
        ["原名关致祥,化名李世珍", "到上海大学学习", "运动爆发。五州运动兴起",
         "1930年2月,由疝忠发", "六届四中全会是根据共产国际指示",
         "顾顺章被捕产变后,供出了中共中央在上海", "被捕以后,如何营救",
         "将这些情况向周恩来汇报后", "后来,陈刻就叫杨登",
         "当时有位共产党员张纪恩", "另一位在全国总工会",
         "在1931年年底出狱后,即被中共中央作为中央代表"],
    ],
    "ch14": [
        # blob0 = s01 (纠正了单纯恐怖行动…), 7 paragraphs
        ["由于顾顺章原是青帮", "中央特科的权力很大,但周恩来自始至终",
         "随着胜利形势的发展,顾顺章的错误思想",
         "这种做法,显然和党的长远利益格格不人",
         "周恩来在领导中央特科工作中,始终贯彻",
         "顾顺章个人品德方面的恶劣倾向"],
        # blob1 = s02 (旷世奇才杨度), 17 paragraphs (incl. the 七律 poem and the
        # 辞海 block quote, each ONE paragraph)
        ["又名杨暂子", "茶销药白伴孤身", "由于杨度政治上的几度转变",
         "1927年李大钊被奉系军闽", "杨度到上海和中央特科取得联系",
         "杨度参加共产党后,离开家室", "杜月笔是什么人",
         "沾满革命者和人民鲜血", "这样一来,从", "杨度向中央特科提供的情报多而重要",
         "为了使于开展工作", "杨度入党虽然是秘密的", "杨度因操劳过度",
         "遵照周恩来的指示,1979年出版", "杨度(1874", "王治秋在他写的"],
        # blob2 = s03 (两个国会议员:梅宝玑、胡鄂公), 20 paragraphs
        ["在上海,当中央特科把斗争重点转向政治领域", "(1884",
         "1922年8月,第一届国会复会", "在旧官场做事较久",
         "本来,杨献珍和胡鄂公并不认识", "4月中旬,衣骂公和杨献珍乘船",
         "明鄂公听说营救有望", "7月10日前后,杨献珍清早买来",
         "7月中旬一天,陈刻来到", "听到北平的风声", "胡鄂公这时从上海回到天津",
         "7月22日,杨献珍便乘火车来到北平", "杨献珍离开天津以前,胡鄂公将5份",
         "第二天,杨献珍带上5份秘密的", "来到门前,杨献珍迈步走进了黑河大门",
         "杨献珍被捕的信息传到天津", "陈广这次到天津来,深得胡鄂公的配合",
         "胡鄂公从天津回到上海后,继续专做上层政治情报",
         "明鄂公在情报工作中对党作出了一定贡献"],
    ],
}


def load(unit):
    return [l.rstrip("\n") for l in open(os.path.join(ZH, "%s.txt" % unit))]


def blobs_of(lines):
    tokens = []
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
    pos = [text.index(m) for m in markers]
    if pos != sorted(pos):
        print("  %s blob%d: markers OUT OF ORDER %s" % (unit, bi, pos))
        return None
    pieces, rest = [], text
    for m in markers:
        i = rest.index(m)
        pieces.append(rest[:i]); rest = rest[i:]
    pieces.append(rest)
    BREAK = "。！？…：:!?"
    CLOSE = "”』」）】》\""
    for i in range(1, len(pieces)):
        prev = pieces[i - 1]
        k = max((prev.rfind(c) for c in BREAK), default=-1)
        if k < 0:
            continue
        j = k + 1
        while j < len(prev) and prev[j] in CLOSE:
            j += 1
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
            blob = "".join(val)
            if bi >= len(blob_markers):
                print("  %s: MORE blobs than marker-lists (bi=%d)" % (unit, bi))
                ok = False
                bi += 1
                continue
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
    for unit in ("ch13", "ch14"):
        print("===", unit, "===")
        allok &= process(unit, apply)
    if not apply:
        print("\nDRY RUN%s. Re-run with --apply to write."
              % ("" if allok else " -- FIX MARKERS FIRST"))
    elif not allok:
        print("\nSOME BLOBS FAILED -- file may be partially written; re-assemble.")
