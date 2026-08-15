#!/usr/bin/env python3
# B07 (ch11 PDF 231-246, ch12 PDF 247-262) paragraph re-segmentation, run on
# data/zh/ch11.txt and data/zh/ch12.txt AFTER assemble.
#
# Same method as b06: within each section (the body between two headings) we
# concatenate every assembled body paragraph back into one blob -- exactly the
# continuous source text -- then split it at a verified list of paragraph-START
# markers.  Every marker is a RAW-OCR substring (apply_fixes runs AFTER surgery)
# read paragraph-by-paragraph off the folios (187-218) and verified to occur
# EXACTLY ONCE in its blob (the script refuses to apply otherwise).
# NOT idempotent: re-assemble both units before re-running.
#
# ch11: s01 14 paras, s02 11 paras, s03 14 paras (39 body + 4 headings)
# ch12: s01 15 paras, s02 21 paras, s03  6 paras (42 body + 4 headings)
import os
import sys

ROOT = "/home/user/winston"
ZH = os.path.join(ROOT, "data", "zh")

CONFIG = {
    "ch11": [
        # blob0 = s01 (针对周恩来的袭击), 14 paragraphs
        ["蓝洗(1896", "帷秋白在", "杨身(1893", "颜虽颐(1900", "邢七贞(1903",
         "张际春(?", "1929年8月24日,彭", "周恩来得知", "周恩来写道",
         "叛徒所佬是黄埔", "次知白春底细", "周恩来原定要来", "可是,任何狭独"],
        # blob1 = s02 (武装营救未能奏效), 11 paragraphs
        ["彭涯先被办禁", "他和杨殷联名秘密", "彭涛,杨委等同志被捕以后",
         "茧,杨五同志至公安局", "中央调动了特科的全部力量", "8月28日晨,敌人将",
         "当日在现场参与指挥", "中央特科的武装行动,通常", "柯记回忆说:营救",
         "营救没有成功,但是这次行动"],
        # blob2 = s03 (彭湃、杨殷等四烈士英勇就义), 14 paragraphs
        # the final report is a reproduced letter: salutation / body / short line
        # / joint signature (挼安, restored in strip) render as four paragraphs.
        ["他们入和警备司令部", "当紫它的威胁逼在眼前", "冠生暨家中老少",
         "我等此次被白害", "余人还坚持不认", "挼安", "浆涯在殉难前",
         "位同志终于在8月30日", "等同志遇难经过", "在临时法院审后",
         "同志初被捕时", "周恩来怀着极度悲痛", "当时在中共中央机关工作的张"],
    ],
    "ch12": [
        # blob0 = s01 (穷追叛徒白鑫), 15 paragraphs
        ["间恩来当即派人帮助", "彭涯等4人的遇难,更激起",
         "这个时候,国民党反动派故意施放烟幕", "曾去过南京一趟",
         "如前文所述,当时柯麟", "柯志认识日伟多年", "被捕的第二天早晨",
         "约找过了十来天", "末然,又过了两个星期", "这次给白诸看病的情形",
         "决定临时在法租界租了", "义过了两个星期,白奢从他住", "日闭呢,他素知红队",
         "他还叫特科再在和合坊租了一间铺面房"],
        # blob1 = s02 (叛徒倒毙在红队枪口下), 21 paragraphs
        ["这天下午,由顾顺章", "这时距离彭浇同志等遇害",
         "国民党报纸虽然对这个案件连篇", "前晚十点钟许", "霞飞路和合坊四和弄",
         "范.白等一行共七人", "事后约一小时,捕房始派探", "昨晨张市长",
         "捕房人员一方", "记者于闻耗后", "这则消息还照", "外文报纸,则大都认为",
         "法租界巡捕房正在", "案件发生在一条叫", "枪击的时间仅几秒钟",
         "枪击发生后几分钟", "调查工作昨天仍在继续", "关于此案的报道在昨天",
         "反动派对白介等人被我方处决", "政人为了对付红队"],
        # blob2 = s03 (镇压叛徒的英雄谭忠余), 6 paragraphs
        ["谭忠余(1909", "1927年初,谭忠余在中共上海",
         "1931年4月顾顺章被捕叛变后", "1931年11月,因和谭忠余工作关系",
         "回到上海不久,党组织派谭忠余"],
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
    CLOSE = "”』」）】》"
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
    for unit in ("ch11", "ch12"):
        print("===", unit, "===")
        allok &= process(unit, apply)
    if not apply:
        print("\nDRY RUN%s. Re-run with --apply to write."
              % ("" if allok else " -- FIX MARKERS FIRST"))
    elif not allok:
        print("\nSOME BLOBS FAILED -- file may be partially written; re-assemble.")
