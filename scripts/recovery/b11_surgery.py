#!/usr/bin/env python3
# B11 (ch19 PDF 389-405, ch20 PDF 406-428) paragraph re-segmentation, run on
# data/zh/ch19.txt and data/zh/ch20.txt AFTER assemble.  Follows b10.
#
# Each SECTION body is concatenated into one blob and split at a verified list
# of paragraph-START markers (markers[i] starts piece i+1; a blob of N
# paragraphs needs N-1 markers).  Markers are RAW-OCR substrings (apply_fixes
# runs AFTER), each occurring EXACTLY ONCE in its blob.  Boundaries were read
# off the page images (indent geometry is unreliable on these scans).
#
# NOT idempotent: re-assemble both units before re-running.
#
# ch19: s01 22, s02 7, s03 13         (42 body + 4 headings)
# ch20: s01 19, s02 16, s03 20, s04 9 (64 body + 5 headings)
import os
import sys

ROOT = "/home/user/winston"
ZH = os.path.join(ROOT, "data", "zh")

CONFIG = {
    "ch19": [
        # ---- s01 (顾顺章护送张国焘去鄂豫皖苏区), 22 paragraphs ----
        ["这次四中全会后", "六届四中全会后", "其时张国寿刚从苏联",
         "有的“著作家", "张国帮去武汉", "其实,这次张国春",
         "张国春一行到达武汉", "1931年3月中名", "顾顺章为我服务",
         "晨光普照的时间", "在日租界一条较僻静", "接着他又告诉我们",
         "在这个仅有两间卧房", "七日偿晚", "八日上午八时",
         "苏区派来的交通员于4月8日", "国民党武汉行营侦缉处长杨庆山",
         "在武汉亲目逮捕", "当顾顺章要被押送到军法处",
         "4月25日清晨,国民党武汉行营主任何成",
         "何成滩和在汉口的国民党特务黄凯"],
        # ---- s02 (在汉口被捕叛变), 7 paragraphs ----
        ["4月27日(星期一)顾顺章才被敌人用轮船", "稍事休息,些备坚就带顾顺章",
         "的文章,记述了叛徒顾顺章", "徐恩曾把顾顺章抢先转移秘密关押",
         "据当时在徐恩曾手下当差的调查科助理", "外修订正"],
        # ---- s03 (一网打尽“中共中央”阴谋彻底破产), 13 paragraphs ----
        ["这天夜里,钱壮飞一直坐在南京中山东路", "何成滩的电报,发给国民党中央党部",
         "第一封电报,说黎明", "第2封电报,说将用兵舰",
         "第3封电报,说改用飞机", "钱壮飞看完这些密电,大吃一惊",
         "刘杞夫于26日凌晨到达上海", "这天是星期天,不是李克农和陈广预订",
         "这时胡底还在天津", "面对着这种险恶的形势,周恩来在陈云",
         "周恩来做事一贯精密细致", "在关系着我党命运的这个千钧一发"],
    ],
    "ch20": [
        # ---- s01 (顾顺章出卖了在南京狱中的恽代英), 19 paragraphs ----
        ["是我国早期的马克思主义者", "又名莲轩", "在五四运动爆发时",
         "五四运动后,马克思列宁主义", "1922年春,履代贡在四川泸州",
         "1927年前后,在中国历史转变关头", "1928年党的第六次全国代表大会后",
         "本是蒋介石恨之人骨", "隐姓埋名,自毁面容",
         "1931年春节后,必代英从狱中支部", "浪迹江湖数旧游",
         "在1930年被捕不久", "周恩来指示,必须使用一切手段",
         "狱中党支部高跨远瞩", "正当党组织紧张地为",
         "1931年4月29日,敌人就将", "罪恶的枪声响起",
         "其时那个正在徐恩曾手下任职"],
        # ---- s02 (顾顺章赴香港捕杀蔡和森), 16 paragraphs ----
        ["双姓栓林", "是和母亲妹妹一起到法国", "不久国内学界兴起赴法勤工俭学",
         "到法国后,接受了科学共产主义", "在法国组织中国社会主义青年团",
         "第二次至第六次全国代表大会上", "在大革命失败的紧要关头",
         "1928年初,柳和森", "长期在上海和莫斯科两地工作",
         "从苏联回国,提出要去中央苏区", "到香港不久,就得知顾顺章被捕",
         "这年6月10日,香港海员", "被捕后,党组织立即采取了营救",
         "敌人的残酷折磨丝毫无损", "牺牲后,党和人民始终深切"],
        # ---- s03 (出卖、抓捕向忠发), 20 paragraphs ----
        ["1880年出生", "这个姘头是顾顺章", "这次闻知顾顺章叛变,周恩来紧急",
         "被捕的消息,最早是中央特科情报科", "正为向忠发一夜未归",
         "被捕后,首先供出的是", "刊载了一则由远东社",
         "为共党首领,于昨日", "这天被引渡到国民党淞沪警备",
         "再说淞沪警备司令", "又在《本埠新闻》栏里刊登了一则短讯",
         "中央得知向忠发已在龙华", "周恩来办事一向精密细致",
         "做法文翻译的鲍文蔚", "看过这份口供,开始曾经怀疑",
         "却没有将他叛变的口供公布", "一案本来抱的希望很大",
         "毛泽东在杭州接见外宾", "1972年6月,周恩来在一次讲话"],
        # ---- s04 (还出卖了鲍君甫(杨登瀛)), 9 paragraphs ----
        ["当顾顺章叛变的消息刚刚传到上海", "全国展开镇压反革命运动后",
         "率领部队解放云南后", "对中央特科有过重要贡献,本",
         "审理鲍君甫的过程中", "获释后,因无经济来源",
         "期间,鲍君甫不免受到群众冲击", "有一次谈到鲍君甫的时候说"],
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
    CLOSE = "”’』」）】》\""
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
    for unit in ("ch19", "ch20"):
        print("===", unit, "===")
        allok &= process(unit, apply)
    if not apply:
        print("\nDRY RUN%s. Re-run with --apply to write."
              % ("" if allok else " -- FIX MARKERS FIRST"))
    elif not allok:
        print("\nSOME BLOBS FAILED -- re-assemble.")
