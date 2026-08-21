#!/usr/bin/env python3
# Build data/ocr_fixes.json entries for ch23/ch24 (crop-verified name/numeral
# garbles).  Idempotent: replaces the ch23/ch24 lists.  Run BEFORE apply_fixes.
#
# Name folds are classified against the scan/context (b13 survey): Chen Geng and
# Liu Ding are almost always mangled, but real 陈X / 刘X names (陈云 Chen Yun,
# 陈立夫/陈果夫, 陈康, 陈连生, 陈寿昌, 陈原道, 陈养山; 刘杞夫 Qian Zhuangfei's
# son-in-law, 刘少白, 刘英, 刘亚雄, 刘伯承) must NOT be folded, so only the
# specific mangled bigrams are listed.
import json
import os

ROOT = "/home/user/winston"
LEDGER = os.path.join(ROOT, "data", "ocr_fixes.json")

# unit -> canonical -> (page, [variants])
NAMES = {
    "ch23": {
        "陈赓": ("f445", ["陈庆", "陈广", "陈刻", "陈废", "陈记", "陈钴", "陈短",
                          "陈笋", "陈乌", "陈鹿", "陈唐", "陈康"]),
        "刘鼎": ("f468", ["刘易", "刘瞻", "刘里", "刘蜀", "刘哆", "刘晶", "刘刚",
                          "刘罗", "刘弓", "刘昂", "刘时"]),
        "蒋介石": ("f479", ["头介石", "薪介石", "范介石"]),
        "顾顺章": ("f441", ["磊顺章", "显顺章", "吴顺章", "电顺章", "顾咕章",
                          "顾顺音", "顾顺更"]),
        "徐恩曾": ("f458", ["徐思曾"]),
        "张国焘": ("f465", ["张国帮", "张国琳", "张国春", "张国霖", "张国栋",
                          "张国玫", "张国态", "张国总"]),
        "陈养山": ("f445", ["陈养出"]),
        "周恩来": ("f441", ["周思来", "周册来"]),
        "李一氓": ("f462", ["李一让", "李一旋"]),
    },
    "ch24": {
        "顾顺章": ("f483", ["磊顺章", "显顺章", "吴顺章", "电顺章", "顾咕章",
                          "顾顺音", "顾顺更", "顾硕章", "显丹章"]),
        "徐恩曾": ("f483", ["徐思曾", "徐恩兽", "徐轧曾", "徐乱曾"]),
        "蒋介石": ("f489", ["薪介石", "范介石", "头介石"]),
        "陈赓": ("f486", ["陈短"]),
    },
}

# numeral / misc garbles verified against the scan (added after check_numbers)
EXTRA = {
    "ch23": [
        {"wrong": "《4中央审查", "right": "《中央审查", "page": "f442",
         "note": "book-title bracket 《 duplicated a phantom 4"},
        {"wrong": "193$年9月", "right": "1935年9月", "page": "f444",
         "note": "1935 OCR'd 193$ (garbled 5)"},
        {"wrong": "193S年3月", "right": "1935年3月", "page": "f462",
         "note": "1935 OCR'd 193S (Latin S for 5)"},
        {"wrong": "乌克三人", "right": "乌克兰人", "page": "f457",
         "note": "乌克兰人 a Ukrainian; 兰 OCR'd 三"},
    ],
    "ch24": [
        {"wrong": "遭逮捕” .0", "right": "遭逮捕”", "page": "f483",
         "note": "note-ref (1) OCR'd as .0"},
        {"wrong": "个新的阶段。9", "right": "个新的阶段。", "page": "f488",
         "note": "note-ref (1) OCR'd as 9"},
        {"wrong": "垂青。\"9", "right": "垂青。\"", "page": "f504",
         "note": "note-ref (1) OCR'd as 9"},
        {"wrong": "杀身之祸了。\"9", "right": "杀身之祸了。\"", "page": "f506",
         "note": "note-ref (1) OCR'd as 9"},
        {"wrong": "军统的1710", "right": "军统的1/10", "page": "f490",
         "note": "fraction 1/10 OCR'd 1710"},
        {"wrong": "中统骨二分子顾建中", "right": "中统骨干分子顾建中", "page": "f503",
         "note": "骨干分子 backbone element; 干 OCR'd 二"},
    ],
}


def build_unit(unit):
    out = []
    for canon, (page, variants) in NAMES[unit].items():
        for v in variants:
            out.append({"wrong": v, "right": canon, "page": page,
                        "note": "OCR name garble"})
    out.extend(EXTRA[unit])
    return out


led = json.load(open(LEDGER))
for unit in ("ch23", "ch24"):
    led[unit] = build_unit(unit)
    print("%s: %d fixes" % (unit, len(led[unit])))
json.dump(led, open(LEDGER, "w"), ensure_ascii=False, indent=1)
print("wrote", LEDGER)
