#!/usr/bin/env python3
# Build data/ocr_fixes.json entries for ch25/ch26/ch27 (crop-verified name and
# numeral/garble corrections, all checked against the page scans).  Idempotent:
# replaces the ch25/ch26/ch27 lists.  Run BEFORE apply_fixes, AFTER surgery.
#
# Per-unit NAME maps: a garble that is a real name elsewhere must not be folded
# blindly (e.g. 陈云/陈养山/陈忠经/陈诚/陈华 are NOT 陈赓; only the specific
# garbled bigrams 陈广/陈庆/陈刻 map to 陈赓, per unit).
import json
import os

ROOT = "/home/user/winston"
LEDGER = os.path.join(ROOT, "data", "ocr_fixes.json")


def F(wrong, right, page, note):
    return {"wrong": wrong, "right": right, "page": page, "note": note}


FIXES = {
    "ch25": [
        # --- names ---
        F("毛洋东", "毛泽东", "f520", "Mao Zedong; 泽 OCR'd 洋"),
        F("江理及其一伙", "江青及其一伙", "f520", "Jiang Qing; 青 OCR'd 理"),
        F("陈志举", "陈志皋", "f516", "Chen Zhigao; 皋 OCR'd 举"),
        F("陈志尝", "陈志皋", "f516", "Chen Zhigao; 皋 OCR'd 尝"),
        F("陈志涯", "陈志皋", "f516", "Chen Zhigao; 皋 OCR'd 涯"),
        F("陈志果", "陈志皋", "f518", "Chen Zhigao; 皋 OCR'd 果"),
        F("黄幕兰", "黄慕兰", "f516", "Huang Mulan; 慕 OCR'd 幕"),
        F("李一训", "李一氓", "f518", "Li Yimang; 氓 OCR'd 训"),
        F("周思来", "周恩来", "f512", "Zhou Enlai; 恩 OCR'd 思"),
        # --- dates / numerals ---
        F("9月工日", "9月1日", "f510", "1 OCR'd 工"),
        F("2月1S日", "2月15日", "f511", "15 OCR'd 1S"),
        F("2月316日", "2月16日", "f515", "16 OCR'd 316 (phantom 3)"),
        F("$月19日", "5月19日", "f519", "5 OCR'd $"),
        F("1968年1!月", "1968年1月", "f522", "stray ! after 1"),
        F("简报》第S5期", "简报》第55期", "f520", "55 OCR'd S5"),
        # --- notice / readability garbles ---
        F("政治音景", "政治背景", "f509", "背景; 背 OCR'd 音"),
        F("内容的充廖", "内容的荒谬", "f510", "荒谬; OCR'd 充廖"),
        F("这则父造", "这则伪造", "f510", "伪 OCR'd 父"),
        F("敞人等深信", "敝人等深信", "f511", "forged notice's humble self-ref 敝人"),
        F("敢人本良心", "敝人本良心", "f511", "敝人; OCR'd 敢人"),
        F("倪偶", "傀儡", "f511", "傀儡; OCR'd 倪偶"),
        F("从事草命", "从事革命", "f511", "革 OCR'd 草"),
        F("之初趁", "之初衷", "f511", "初衷; 衷 OCR'd 趁"),
        F("尼为捧骗国人", "皆为欺骗国人", "f511", "皆为欺骗; OCR'd 尼为捧骗"),
        F("伍豪等二百四十三人祝", "伍豪等二百四十三人启", "f511", "启 OCR'd 祝"),
        F("毒闫", "毒辣", "f514", "毒辣; 辣 OCR'd 闫"),
        F("日色义怖", "白色恐怖", "f514", "白色恐怖; OCR'd 日色义怖"),
        F("不信嘟", "不信邪", "f514", "邪 OCR'd 嘟"),
        F("党组织泊人", "党组织派人", "f514", "派 OCR'd 泊"),
        F("效据周少山", "兹据周少山", "f517", "兹 OCR'd 效 (Ba He notice)"),
        F("也个能全信", "也不能全信", "f522", "不 OCR'd 个"),
        # 《 book-title bracket OCR'd as a digit
        F("登4伍豪", "登《伍豪", "f512", "《 OCR'd 4"),
        F("刊物6斗争", "刊物《斗争", "f515", "《 OCR'd 6"),
        F("用4时报", "用《时报", "f515", "《 OCR'd 4"),
        F("上海4时事", "上海《时事", "f516", "《 OCR'd 4"),
        F("季源溥警告4申报", "季源溥警告《申报", "f513", "《 OCR'd 4"),
        F("说六申报", "说《申报", "f514", "《 OCR'd 六"),
        F("炮制4伍豪", "炮制《伍豪", "f512", "《 OCR'd 4"),
        F("在《4申报", "在《申报", "f513", "phantom 4 after 《"),
        F("伍豪启事”7”申报", "伍豪启事”申报", "f513", "note-ref/？ OCR'd 7"),
        F("该声明的。”9", "该声明的。”", "f513", "note-ref ② OCR'd 9"),
        # real numbers OCR-garbled: restore them
        F("只举出-再四十三人", "只举出二百四十三人", "f519", "243; 二百 OCR'd -再"),
        F("197S年9月20日", "1975年9月20日", "f525", "1975; 5 OCR'd S"),
        # 诬蔑 / 污蔑 family
        F("诬茂", "诬蔑", "f509", "诬蔑; 蔑 OCR'd 茂"),
        F("污芒", "污蔑", "f515", "污蔑; 蔑 OCR'd 芒"),
        F("造谣污项", "造谣污蔑", "f516", "污蔑; 蔑 OCR'd 项"),
        F("攻击诬套", "攻击诬蔑", "f521", "诬蔑; 蔑 OCR'd 套"),
        F("造语诬芯", "造谣诬蔑", "f521", "造谣诬蔑; OCR'd 造语诬芯"),
    ],
    "ch26": [
        # --- names ---
        F("净宝航", "阎宝航", "f528", "Yan Baohang; 阎 OCR'd 净"),
        F("疝宝航", "阎宝航", "f529", "Yan Baohang; 阎 OCR'd 疝"),
        F("净明诗", "阎明诗", "f529", "Yan Mingshi; 阎 OCR'd 净"),
        F("能向晖", "熊向晖", "f530", "Xiong Xianghui; 熊 OCR'd 能"),
        F("季米特洛大", "季米特洛夫", "f529", "Dimitrov; 夫 OCR'd 大"),
        F("正是陈刻", "正是陈赓", "f528", "Chen Geng; 赓 OCR'd 刻"),
        F("薪介石", "蒋介石", "f530", "Chiang Kai-shek; 蒋 OCR'd 薪"),
        F("向薪军官", "向蒋军官", "f532", "Chiang's officers; 蒋 OCR'd 薪"),
        # --- numerals ---
        F("6月?21日", "6月21日", "f529", "stray ? in date"),
        F("6月21昌", "6月21日", "f529", "日 OCR'd 昌"),
        F("两万三后余人", "两万三千余人", "f533", "千 OCR'd 后"),
        F("$0周年", "50周年", "f529", "50; 5 OCR'd $"),
        F("陆军1S3个整师", "陆军153个整师", "f531", "153; 5 OCR'd S"),
        F("偏亿去处", "偏僻去处", "f531", "偏僻; 僻 OCR'd 亿"),
        F("11月4中共", "11月《中共", "f534", "《 OCR'd 4"),
        # --- garbles ---
        F("抗日成争", "抗日战争", "f529", "战 OCR'd 成"),
        F("工作虐心源血", "工作呕心沥血", "f528", "呕心沥血; OCR'd 虐心源血"),
        F("布置打人国民党", "布置打入国民党", "f528", "打入; 入 OCR'd 人"),
        F("打和人国民党", "打入国民党", "f530", "打入; OCR'd 打和人"),
        F("当年打人国民党", "当年打入国民党", "f530", "打入; 入 OCR'd 人"),
    ],
    "ch27": [
        # --- names ---
        F("陈广", "陈赓", "f535", "Chen Geng; 赓 OCR'd 广 (ch27-wide)"),
        F("陈庆", "陈赓", "f537", "Chen Geng; 赓 OCR'd 庆 (ch27-wide)"),
        F("周因来", "周恩来", "f535", "Zhou Enlai; 恩 OCR'd 因"),
        F("周思来", "周恩来", "f535", "Zhou Enlai; 恩 OCR'd 思"),
        F("刘章、柯遍", "刘鼎、柯麟", "f537", "Liu Ding, Ke Lin; OCR'd 刘章、柯遍"),
        # --- garbles ---
        F("极端隐藏", "极端隐蔽", "f536", "隐蔽; 蔽 OCR'd 藏"),
        F("白色恶怖笼覃", "白色恐怖笼罩", "f536", "白色恐怖笼罩; OCR'd 恶怖笼覃"),
        F("珠死的斗争", "殊死的斗争", "f536", "殊死; 殊 OCR'd 珠"),
        F("不总赐教", "不吝赐教", "f536", "不吝赐教; 吝 OCR'd 总"),
        F("的斗争,万是你死", "的斗争,乃是你死", "f536", "乃是; 乃 OCR'd 万"),
    ],
}


led = json.load(open(LEDGER))
for unit in ("ch25", "ch26", "ch27"):
    led[unit] = FIXES[unit]
    print("%s: %d fixes" % (unit, len(led[unit])))
json.dump(led, open(LEDGER, "w"), ensure_ascii=False, indent=1)
print("wrote", LEDGER)
