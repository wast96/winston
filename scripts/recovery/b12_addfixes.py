#!/usr/bin/env python3
# Build data/ocr_fixes.json entries for ch21/ch22 (crop-verified name/numeral
# garbles).  Idempotent: replaces the ch21/ch22 lists.  Run BEFORE apply_fixes.
import json
import os

ROOT = "/home/user/winston"
LEDGER = os.path.join(ROOT, "data", "ocr_fixes.json")

# unit -> canonical -> (page, [variants])
NAMES = {
    "ch21": {
        "陈赓": ("f385", ["陈记", "陈刻", "陈废", "陈钴", "陈庆", "陈广", "陈煞",
                          "陈短", "陈委", "陈铸", "陈庚", "陈唐", "陈笋", "陈灿"]),
        "陈藻英": ("f388", ["陈菠英"]),
        "蒋介石": ("f400", ["萝介石", "葛介石", "藉介石", "将介石", "莉介石",
                          "葡介石", "攻介石"]),
        "杨铨": ("f390", ["杨狂"]),
        "王根英": ("f406", ["王根灿", "王根关", "王根类", "王根喘", "王根负"]),
        "顾顺章": ("f385", ["丘顺章", "顾顺更"]),
        "谭国辅": ("f389", ["谭国畏"]),
        "夏之栩": ("f399", ["夏之棚"]),
        "邓文仪": ("f402", ["闻文仪"]),
        "廖承志": ("f385", ["鹿承志", "雇承志", "庆承志", "记承志"]),
        "罗登贤": ("f391", ["罗登质", "罗登贰", "罗登贸"]),
    },
    "ch22": {
        "陈赓": ("f430", ["陈刻"]),
        "蒋介石": ("f419", ["萝介石", "藉介石"]),
        "蔡元培": ("f429", ["些元培", "蒙元培", "葡元培", "莹元培", "歼元培",
                          "紫元培", "桂元培", "从元培", "栓元培"]),
        "杨杏佛": ("f427", ["杨查佛", "杨可佛"]),
        "杨铨": ("f427", ["杨狂", "杨镍", "杨锭", "杨欠", "杨猴", "杨镁"]),
        "顾顺章": ("f414", ["顺顺章"]),
        "鲁迅": ("f416", ["重迅", "求迅"]),
        "沈钧儒": ("f430", ["沈钩颂", "沈钩儒"]),
        "沈醉": ("f433", ["沈醇"]),
        "丁玲": ("f414", ["于玲", "」玲"]),
        "冯雪峰": ("f424", ["汉雪峰"]),
        "恽代英": ("f428", ["钧代英", "翁代英", "履代英"]),
        "史沫特莱": ("f423", ["史沫特菜"]),
    },
}

# numeral / misc garbles verified against the scan (added after check_numbers)
EXTRA = {
    "ch21": [
        {"wrong": "赵夺英", "right": "赵冠英", "page": "f398",
         "note": "69th Div commander name; crop-verified"},
        {"wrong": "3位肥翌", "right": "5位肥胖", "page": "f391",
         "note": "China Forum quote: FIVE judges (OCR read 5 as 3); crop-verified f391"},
        {"wrong": "一副六然", "right": "一副凛然", "page": "f405",
         "note": "凛然 (OCR 六 for 凛 injected phantom 6)"},
        {"wrong": "这个三的", "right": "这个厂的", "page": "f408",
         "note": "恒丰纱厂 the mill (OCR 三 for 厂 injected phantom 3)"},
        {"wrong": "幻想1", "right": "幻想!", "page": "f405",
         "note": "exclamation OCR'd as 1"},
        {"wrong": "了?7", "right": "了?", "page": "f401",
         "note": "quote-close/note-ref OCR'd as 7"},
        {"wrong": "即被捕。\"9", "right": "即被捕。\"", "page": "f385",
         "note": "note-ref (1) OCR'd as 9"},
        {"wrong": "光头.9", "right": "光头。", "page": "f386",
         "note": "note-ref (1) OCR'd as 9; period garble"},
        {"wrong": "工部六的律师", "right": "工部局的律师", "page": "f392",
         "note": "工部局 the Municipal Council (OCR 六 for 局 injected phantom 6)"},
        {"wrong": "判决,二已在", "right": "判决,早已在", "page": "f392",
         "note": "早已 (OCR 二 for 早 injected phantom 2)"},
        {"wrong": "四来请读", "right": "回来请读", "page": "f392",
         "note": "回来 came back (OCR 四 for 回 injected phantom 4)"},
        {"wrong": "有7十见方", "right": "有7寸见方", "page": "f396",
         "note": "7-inch opening (OCR 十 for 寸 injected phantom 10)"},
        {"wrong": "复了一遍17", "right": "复了一遍", "page": "f399",
         "note": "note-ref (1) OCR'd as 17"},
        {"wrong": "4中国论坛", "right": "中国论坛", "page": "f391",
         "note": "book-title bracket 《 OCR'd as 4"},
    ],
    "ch22": [
        {"wrong": "站1和另外", "right": "和另外", "page": "f414",
         "note": "author-note ref [2] OCR'd as :站1"},
        {"wrong": "潘梓年主]", "right": "潘梓年", "page": "f414",
         "note": "author-note ref [1] OCR'd as 主]"},
        {"wrong": "4《大美晚报", "right": "《大美晚报", "page": "f414",
         "note": "book-title bracket 《 OCR'd as 4"},
        {"wrong": "的一个事件\"9", "right": "的一个事件\"", "page": "f416",
         "note": "note-ref (1) OCR'd as 9"},
        {"wrong": "找保杰放呢7", "right": "找保释放呢?", "page": "f423",
         "note": "保释 bail (OCR 杰 for 释); note-ref OCR'd as 7"},
        {"wrong": "讲吓…和0", "right": "讲吓……", "page": "f422",
         "note": "quotation ellipsis + note-ref OCR'd as 和0"},
        {"wrong": "心疼。0", "right": "心疼。", "page": "f424",
         "note": "note-ref (1) OCR'd as 0"},
        {"wrong": "4中国共产党现状", "right": "中国共产党现状", "page": "f429",
         "note": "book-title bracket 《 OCR'd as 4"},
        {"wrong": "尚多,万决定", "right": "尚多,乃决定", "page": "f438",
         "note": "乃 then (OCR 万 for 乃 injected phantom 10000)"},
        {"wrong": "又去了。\"9", "right": "又去了。\"", "page": "f426",
         "note": "note-ref (1) OCR'd as 9"},
        {"wrong": "红十闻会医院", "right": "红十字会医院", "page": "f435",
         "note": "红十字会 Red Cross (OCR 闻 for 字)"},
        {"wrong": "丁零说", "right": "丁玲说", "page": "f418",
         "note": "丁玲 (OCR 零 for 玲 injected phantom 0)"},
    ],
}


def build_unit(unit):
    out = []
    # 陈藻英 must precede any bare-陈 fix; dict order preserves that here.
    for canon, (page, variants) in NAMES[unit].items():
        for v in variants:
            out.append({"wrong": v, "right": canon, "page": page,
                        "note": "OCR name garble"})
    out.extend(EXTRA[unit])
    return out


led = json.load(open(LEDGER))
for unit in ("ch21", "ch22"):
    led[unit] = build_unit(unit)
    print("%s: %d fixes" % (unit, len(led[unit])))
json.dump(led, open(LEDGER, "w"), ensure_ascii=False, indent=1)
print("wrote", LEDGER)
