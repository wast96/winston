#!/usr/bin/env python3
# B10 (ch17 PDF 333-363, ch18 PDF 364-388) paragraph re-segmentation, run on
# data/zh/ch17.txt and data/zh/ch18.txt AFTER assemble.  Follows b09.
#
# Each section body is concatenated into one blob and split at a verified list
# of paragraph-START markers (markers[i] starts piece i+1; a blob of N
# paragraphs needs N-1 markers).  Markers are RAW-OCR substrings (apply_fixes
# runs AFTER), each occurring EXACTLY ONCE in its blob.  Paragraph boundaries
# were read off the page images (the indent geometry is unreliable in this
# batch -- scanner skew flags whole blocks).  Dialogue/quote paragraphs that
# open on a quotation use a marker just inside the quote; the boundary-snap
# prepends the opening quote.
#
# NOT idempotent: re-assemble both units before re-running.
#
# ch17: s01 14, s02 8, s03 15, s04 24, s05 13   (74 body + 6 headings)
# ch18: intro 1, s01 16, s02 13, s03 12, s04 17 (59 body + 5 headings)
import os
import sys

ROOT = "/home/user/winston"
ZH = os.path.join(ROOT, "data", "zh")

CONFIG = {
    "ch17": [
        # ---- s01 (党的电讯事业创始人李强), 14 paragraphs, 13 markers ----
        ["1928年,中国共产党第六次", "因此,中共中央人迫切",
         "第四科科长李强", "李强(1905", "他在这时得到一位",
         "大学时代,李强思想上", "在1924年5月介绍李强",
         "李强很快发现叶楚耸", "1926年初,李强任上海浦东",
         "1926年10月到1927年2月", "臣装起义前夕",
         "四一二反革命政变后", "前文已述,李强在武汉"],
        # ---- s02 (为党造出第一部收发报机), 8 paragraphs, 7 markers ----
        ["当周奶来提出要李强进行", "听了周恩来的话,李强当即表示",
         "领受了研制无线电收发报机的任务后", "给李强帮助最大的",
         "就这样,在无线电设备和技术资料", "从此,李强就和张沈川一起建立起",
         "这台收发报机,由于报务员的通讯技术"],
        # ---- s03 (到香港建立电台), 15 paragraphs, 14 markers ----
        ["次是李强一个人去的", "这年年底,李强第二次去香港",
         "我们到香港后,把密码交给了王梦兰", "上海党中央与香港南方局之间",
         "我党第一部电台的报务员张沈川,曾经", "1929年12月,李强和黄尚英到香港",
         "他还说道:那时电台的设备不完善", "当时张沈川一直带这部电台住在沪西",
         "李强第二次到香港,除完成了", "一件事是从香港带两部电台回上海",
         "俞作相买好后存放在一家英国洋行", "第二件事是1929年底,邓小平",
         "在香港电台工作的黄尚英由于工作辛苦", "1930年12月1日,香港的电台遭到破坏"],
        # ---- s04 (培训党的第一代报务员), 24 paragraphs, 23 markers ----
        ["第一期无线电训练班采取分散居住", "参加第一批学习的伍云十事后回忆",
         "但到后来,种种迹象显示", "这次搬家以后,学习环境比较安定",
         "该是在收发报机器上进行练习", "生活上的困难并不比学习条件",
         "第一期培训通讯技术人员取得了一些经验", "根据第一期的经验,李强与张沈川建议",
         "第2期无线电训练班的负责人为顾", "尽管制定了这些规定防范敌人的破坏",
         "1930年12月17日下午,天冷", "出事这天,李强和毛齐华",
         "这次涂作潮也差一点被捕", "这天下午,伍云肃不知道训练班出了事",
         "他们被捕后的第二天,12月18日", "丐籁达路破获反动机关",
         "昨午十二时许,市公安局局长", "事先张沈川看到训练班隐蔽不周密",
         "还由毛齐华到方延", "出事后,过了几天,中央特科在福建路",
         "经过这次沉痛教训,大家提高了警惕", "1931年6月,又派这年3月刚从苏联回国",
         "在四成里被捕的那些同志,在狱中表现"],
        # ---- s05 (划时代的通信革命), 13 paragraphs, 12 markers ----
        ["党在苏区无线电工作的创建", "为了沟通上海和江西中央苏区",
         "就在红一方面军只有", "当时担任红一方面军新成立的无线电政委",
         "中央苏区第三次反", "随着电台的发展,红军无线电技术人员",
         "1931年11月,在江西瑞金成立了以毛", "无线电台在红军长征中,也对作战发挥",
         "在长征中做电台侦听工作的钟夫翔说", "自从1929年中央特科在上海创建第一部电台后",
         "到了20节纪80年代,李强回顾", "我党无线电通信工作诞生以来已经半个多世纪"],
    ],
    "ch18": [
        # ---- chapter intro (before s01 heading), 1 paragraph, 0 markers ----
        [],
        # ---- s01 (留日电机专家蔡叔厚), 16 paragraphs, 15 markers ----
        ["从日本回到上海后", "大革命失败后,他的中学同学沈端先",
         "蔡叔厚利用绍敦电机公司老板的身份", "顾顺章被捕产变后",
         "他虽然当\"老板", "调到中央特科后,将绍敦电机公司搬到福昨路",
         "蔡叔厚调到共产国际中国组后,领导上给他布置的任务",
         "1933年,中国组的工作重点", "1934年4月,罗伦斯由于叛徒出卖被捕",
         "此后,尽管处境危险,蒙权厚仍然坚持为党工作",
         "蔡叔厚这位在工作中一向以革命事业为重", "在刘少文.沙文汉的领导下",
         "一直认为,同刘少文谈过自己的情况",
         "全国解放后,蔡叔厚又多次同党提出恢复党籍", "党的十一属三中全会以后"],
        # ---- s02 (党的第一个报务员张沈川), 13 paragraphs, 12 markers ----
        ["其时张沈川正任上海法租界中共地方", "这时,上海报纸上登载",
         "张沈川人学后,发现电台台长", "这个学校请了交通大学两名教授",
         "张沈川在1929年5月结业后", "在这个电台实习期间,张沈川",
         "这事也郑来了麻烦", "张沈用离开第六军用电台",
         "1929年8月24日,发生子由于叛徒白舍", "1929年冬,李强领导研制的收发报机成功",
         "当时上海的白色和仙怖严重", "1930年12月17日,第四科设在上海法租输"],
        # ---- s03 (留苏专家毛齐华), 12 paragraphs, 11 markers ----
        ["在莫斯科的中国留学生中培训无线电", "1929年年底,毛齐华等",
         "他们到上海后,住进组织上指定的三马路", "毛齐华安顿好了住处",
         "随者各苏区鞍勃发展", "上海的环境日益险恶,斗争更加艰难",
         "尽管环境险恶,物质条件困难", "毛齐华除了制造收发报机",
         "在险象环生的严峻处境中", "面对如此严峻局面,毛齐华和战友们",
         "另据毛齐华回忆:1936年春"],
        # ---- s04 (木匠涂作潮), 17 paragraphs, 16 markers ----
        ["以后由于", "五庆运动开头,他听到日本人杀害",
         "五讨运动后期,1925年10月", "1929年!月,涂作潮进入列于格",
         "1930年3月,涂作潮和宋湾回到上海", "浊时中央特科的电台是输出功率",
         "1930年秋,涂作潮参加了第四科在上海巨籁达路", "1930年12月底,中央苏区取得了第一次反",
         "2月4日,经缆饮冰安排", "不料,此刻事情发生剧变",
         "张辉瑛曾在其拆师大会上说", "2月7日上午一到南昌",
         "1931年3月,中央决定涂作潮和曾三", "以后涂作潮又于1935年4月回到上海",
         "有一件事情我要永远记在心里", "不久,刘罗回来了,要我收拾好东西"],
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
    for unit in ("ch17", "ch18"):
        print("===", unit, "===")
        allok &= process(unit, apply)
    if not apply:
        print("\nDRY RUN%s. Re-run with --apply to write."
              % ("" if allok else " -- FIX MARKERS FIRST"))
    elif not allok:
        print("\nSOME BLOBS FAILED -- re-assemble.")
