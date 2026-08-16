#!/usr/bin/env python3
# B09 (ch15 PDF 296-320, ch16 PDF 321-332) paragraph re-segmentation, run on
# data/zh/ch15.txt and data/zh/ch16.txt AFTER assemble.  Follows b08.
#
# Each section body is concatenated into one blob and split at a verified list
# of paragraph-START markers.  markers[i] starts piece i+1; piece 0 is the blob
# head, so a blob of N paragraphs needs N-1 markers.  Markers are RAW-OCR
# substrings (apply_fixes runs AFTER), each occurring EXACTLY ONCE in its blob.
# Dialogue paragraphs that open on a quotation use a marker just inside the
# quote and rely on the boundary-snap to prepend the opening quote (verified on
# the scan; ！ OCR'd as 上/性/伍, ？ ascii).  The two reproduced letters (Mao,
# Zhou) split salutation | body | closing; the two salutations OCR differently
# (Mao 少铂间志, Zhou 少白同志) so their markers are distinct.
# NOT idempotent: re-assemble both units before re-running.
#
# ch15: s01 33, s02 23, s03 19  (75 body + 4 headings)
# ch16: s01 5, s02 30, s03 7    (42 body + 4 headings)
import os
import sys

ROOT = "/home/user/winston"
ZH = os.path.join(ROOT, "data", "zh")

CONFIG = {
    "ch15": [
        # ---- s01 (贡生—省议员—开明绅士刘少白), 33 paragraphs, 32 markers ----
        ["刘少白的出身和早年", "刘少白,名家庚",
         "1911年,武昌首义,正在山西大学", "1927年,蒋介石发动",
         "虽出身地主家庭", "他因积极参与辛亥革命", "刘少白早年进山西武备学堂",
         "从他这时的答卷来看", "大革命失败后,蒋介石大肆屠杀",
         "1928年,刘少百的朋友", "1929年初,刘亚雄从苏联回到上海",
         "1931年1月,刘亚雄调到", "刘少白得知这个消息", "直到10多年后",
         "且说那天刘少", "一直牵挂着狱中受苦", "已久的国防前线", "1936年夏天,王",
         "抗日战争爆发后,刘少白按照党的指示", "解放战争初期,老解放区",
         "少铂间志:九", "九月十五大示读悉", "敬颂大安", "毛泽东十月三十日",
         "1947年,刘亚雄在东北工作期间", "少白同志:数", "数数返延",
         "项得亚雄一信", "专此即臻", "周恩来七二拜", "1948年3月工日", "毛泽东周恩来的直率陈情"],
        # ---- s02 (牧师和律师), 23 paragraphs, 22 markers ----
        ["美国著名记者埃德加", "到达西安以前", "我在旅馆住了",
         "在其后的一个星期里", "这位牧师真名董健吾", "浦化人也是一位牧师",
         "董健吾于1926年底抵达", "浦化人走后,董健吾继续留在西北军",
         "1928年秋,南京国民党中央党部", "董健吾回上海后",
         "有联系的情报科副科长", "1931年顾顺章叛变投敌",
         "在律师中,中央特科主要的关系有", "浙江海盐县人", "虽是一般律师",
         "1932年2月16日至21日间", "早已离开上海到达中央苏区",
         "潘汉年知道,其时已调", "黄定慧正是办理此事的合适人选",
         "黄定慧领命后,就去约会", "黄定慧将此情况报经潘汉年",
         "在此以后,潘汉年又要黄定慧"],
        # ---- s03 (向新闻界发展), 19 paragraphs, 18 markers ----
        ["中国共产党在领导人民进行革命斗争", "30年代初期,国内竞办新闻通讯社",
         "在情报科统一规划下,打进敌人心脏", "情报科成立初期,别名",
         "这个时候,有个广东人办的南华通讯社", "从1928年至1935年6月特科结束",
         "正在考虑如何在四川打开局面", "陈养山原与上海一些新闻单位有联系",
         "当年参与其事的陈昌的妻子刘其珍", "的精力没有白费",
         "大量秘密和公开的、非法", "此外,我们还利用敌人矛盾",
         "我们除通讯社的工作外", "这次采用公开的通讯社形式",
         "1936年7月,陈养山和陈克寒", "周恩来于12月19日从西安打电报",
         "随后即在西安成立红中通讯社", "陈养山在西安红中通讯社工作的时间不长"],
    ],
    "ch16": [
        # ---- s01 (淞沪警备司令部), 5 paragraphs, 4 markers ----
        ["当时国民党淞沪警备司令部位于龙华镇", "钱大钧,字幕尹",
         "其间两度出任淞沪警备司令", "国民党淞沪警备司令部罪行累累"],
        # ---- s02 (第四号政治密查员), 30 paragraphs, 29 markers ----
        ["宋再生原名宋启荣", "经过陈刻认真细致的安排", "宋再生财着笑,证异地问",
         "能式辉的名字", "这倒是个肥缺", "陈大同笑喀喀", "宋再生把手一摆",
         "行上", "陈大同有关蒋方震", "和陈大同分手后",
         "很快领到警备司令部的第四号", "就在这年颈月底的一天", "罗迈?",
         "没等宋再生再开口", "宋再生财毛", "姓黄的那个家伙拍着", "那好性",
         "宋再生打发走那个姓黄的家伙", "转眼到了正月初五",
         "宋再生把这个姓黄的带到大东旅社", "陈刻遂带此人坐上汽车",
         "顾顺章见陈刻领着", "不错伍", "顾顺章请他两个进屋",
         "这时端上来的酒叫", "在南京路游竹", "宋再生于1930年8月因筹款失手",
         "即宋启华", "在50年代初期审王运动中"],
        # ---- s03 (英法租界巡捕房), 7 paragraphs, 6 markers ----
        ["站稳了脚跟", "同捕房探是陆连奈", "共产党员陈彭年",
         "这个时期,中央特科继续在已夺取", "对于当时所联系的人物",
         "这样,上海党的隐蔽工作"],
    ],
}


def load(unit):
    return [l.rstrip("\n") for l in open(os.path.join(ZH, "%s.txt" % unit))]


def blobs_of(lines):
    tokens, cur = [], []
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
        print("  %s blob%d: markers OUT OF ORDER" % (unit, bi))
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
    out, bi, ok = [], 0, True
    for kind, val in tokens:
        if kind == "H":
            out.append(val)
        else:
            blob = "".join(val)
            if bi >= len(blob_markers):
                print("  %s: MORE blobs than marker-lists (bi=%d)" % (unit, bi))
                ok = False; bi += 1; continue
            pieces = split_blob(blob, blob_markers[bi], unit, bi)
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
    for unit in ("ch15", "ch16"):
        print("===", unit, "===")
        allok &= process(unit, apply)
    if not apply:
        print("\nDRY RUN%s. Re-run with --apply to write."
              % ("" if allok else " -- FIX MARKERS FIRST"))
    elif not allok:
        print("\nSOME BLOBS FAILED -- re-assemble.")
