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
    ],
    "ch22": [],
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
