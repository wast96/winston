#!/usr/bin/env python3
# Add ch04's crop-verified OCR corrections to data/ocr_fixes.json (idempotent).
# Every "right" reading was verified against the page scan (folios 51-78).
# Run once, then `apply_fixes.py ch04`.
import json, os

LEDGER = "/home/user/winston/data/ocr_fixes.json"

FIXES = [
    # --- Liu Ding (刘鼎), his original name and aliases ---
    ("刘瞻", "刘鼎", 51, "Liu Ding"),
    ("刘里", "刘鼎", 51, "Liu Ding"),
    ("刘虹", "刘鼎", 51, "Liu Ding"),
    ("刘蜡", "刘鼎", 52, "Liu Ding"),
    ("刘曙", "刘鼎", 52, "Liu Ding"),
    ("刘晤", "刘鼎", 55, "Liu Ding"),
    ("刘允", "刘鼎", 55, "Liu Ding"),
    ("刘淆", "刘鼎", 56, "Liu Ding"),
    ("刘晶", "刘鼎", 54, "Liu Ding (guangming interview)"),
    ("刘轩", "刘鼎", 58, "Liu Ding"),
    ("刘蜀", "刘鼎", 58, "Liu Ding"),
    ("刘易", "刘鼎", 51, "Liu Ding (the dominant garble)"),
    ("阐思俊", "阚思俊", 51, "Liu Ding original name Kan Sijun"),
    ("羡泽民", "阚泽民", 51, "Liu Ding alias Kan Zemin"),
    # --- Chen Geng (陈赓) ---
    ("陈刻", "陈赓", 51, "Chen Geng"),
    ("陈庆", "陈赓", 56, "Chen Geng"),
    ("陈记", "陈赓", 65, "Chen Geng"),
    ("陈广", "陈赓", 65, "Chen Geng"),
    ("陈庚", "陈赓", 72, "Chen Geng"),
    ("陈废", "陈赓", 56, "Chen Geng (approval)"),
    # --- Ke Lin (柯麟) ---
    ("柯罕", "柯麟", 59, "Ke Lin"),
    ("柯据", "柯麟", 60, "Ke Lin"),
    ("柯所", "柯麟", 60, "Ke Lin"),
    ("柯饼", "柯麟", 62, "Ke Lin"),
    ("柯赫", "柯麟", 65, "Ke Lin"),
    ("柯蔚", "柯麟", 65, "Ke Lin"),
    ("柯记", "柯麟", 66, "Ke Lin"),
    ("柯岂", "柯麟", 64, "Ke Lin"),
    ("柯鹿", "柯麟", 62, "Ke Lin"),
    ("柯刨", "柯麟", 67, "Ke Lin"),
    # --- He Cheng (贺诚) / He Long (贺龙) ---
    ("锅诚", "贺诚", 62, "He Cheng"),
    ("锅减", "贺诚", 65, "He Cheng"),
    ("锅龙", "贺龙", 72, "He Long"),
    ("货龙", "贺龙", 72, "He Long"),
    # --- Peng Pai (彭湃) ---
    ("彭涯", "彭湃", 61, "Peng Pai"),
    ("彭洲", "彭湃", 60, "Peng Pai"),
    ("彭洗", "彭湃", 61, "Peng Pai"),
    ("茧涯", "彭湃", 64, "Peng Pai"),
    ("芝涯", "彭湃", 64, "Peng Pai"),
    ("艾涯", "彭湃", 64, "Peng Pai"),
    # --- Chen Yangshan (陈养山) ---
    ("陈养出", "陈养山", 68, "Chen Yangshan"),
    ("陈蛮山", "陈养山", 72, "Chen Yangshan"),
    # --- Chen Shouchang (陈寿昌) ---
    ("陈夺虽", "陈寿昌", 76, "Chen Shouchang"),
    ("陈寿虽", "陈寿昌", 75, "Chen Shouchang"),
    ("陈寿吕", "陈寿昌", 77, "Chen Shouchang"),
    ("陈寿员", "陈寿昌", 78, "Chen Shouchang"),
    # --- Yun Daiying (恽代英) — many garbles ---
    ("匈代英", "恽代英", 70, "Yun Daiying"),
    ("怪代英", "恽代英", 70, "Yun Daiying"),
    ("那代英", "恽代英", 70, "Yun Daiying (article title)"),
    ("履代英", "恽代英", 70, "Yun Daiying"),
    ("业代英", "恽代英", 70, "Yun Daiying"),
    ("必=代英", "恽代英", 68, "Yun Daiying"),
    ("人必代英", "恽代英", 63, "Yun Daiying"),
    # --- other names ---
    ("任强时", "任弼时", 70, "Ren Bishi"),
    ("魏记祖", "魏宸祖", 54, "Wei Chenzu, minister to Germany"),
    ("魏雇祖", "魏宸祖", 54, "Wei Chenzu"),
    ("杜月笔", "杜月笙", 56, "Du Yuesheng"),
    ("陈宝双", "陈宝骅", 56, "Chen Baohua"),
    ("余世令", "余世颂", 70, "Yu Shisong"),
    ("优野学", "佐野学", 75, "Sano Manabu"),
    ("估野学", "佐野学", 76, "Sano Manabu"),
    ("优野尝", "佐野学", 76, "Sano Manabu"),
    ("白蠢", "白鑫", 64, "Bai Xin, traitor"),
    ("白讲", "白鑫", 64, "Bai Xin"),
    ("白春", "白鑫", 64, "Bai Xin"),
    ("白夺", "白鑫", 74, "Bai Xin"),
    ("杨登注", "杨登瀛", 71, "Yang Dengying"),
    ("杨登党", "杨登瀛", 71, "Yang Dengying"),
    ("杨登沪", "杨登瀛", 71, "Yang Dengying"),
    ("饱君甫", "鲍君甫", 71, "Bao Junfu = Yang Dengying"),
    ("刘伯承", "刘伯承", 55, "Liu Bocheng (confirm, was garbled 刘们请)"),
    ("刘们请", "刘伯承", 55, "Liu Bocheng, commander"),
    # --- place / org garbles that carry meaning ---
    ("外维埃", "苏维埃", 55, "Soviet"),
    ("上上钻县", "上虞县", 68, "Shangyu county, Zhejiang"),
    ("阔西", "闽西", 65, "western Fujian"),
    ("向国西发展", "向闽西发展", 66, "Red Army into western Fujian"),
    ("同季医院", "同德医院", 65, "Tongde Hospital, Xiamen"),
    ("四成里", "四成里", 76, "Sicheng Li (radio class site)"),
    # --- number-bearing garble (dropped/■): keep digits honest ---
    ("回年六七月间", "同年六七月间", 77, "'same year, 6th-7th month' (lost 。同)"),
]


def main():
    led = json.load(open(LEDGER)) if os.path.exists(LEDGER) else {}
    rows = [{"wrong": w, "right": r, "page": p, "note": n}
            for (w, r, p, n) in FIXES if w != r]
    led["ch04"] = rows
    json.dump(led, open(LEDGER, "w"), ensure_ascii=False, indent=1)
    print("ch04: wrote %d fix rows" % len(rows))


if __name__ == "__main__":
    main()
