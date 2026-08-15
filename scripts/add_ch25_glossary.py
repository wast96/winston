#!/usr/bin/env python3
"""Add ch25's new glossary rows BY HAND into the sectioned glossary.json.
Idempotent; every row carries a pinyin field (qc_entities does rec['pinyin']).
Each hanzi key is verified as a substring of the authoritative data/zh/ch25.txt
so a Write-tool CJK mangling cannot slip a corrupted key into the glossary.

ch25 is a "remarkable people, remarkable deeds" chapter: it brings in a new
Shanghai/Juntong cast (the sabotage-directive commander Qin Qirong, Dai Li's
deputy Mao Renfeng, the CCP intelligence chief Pan Hannian, the eye-doctor
Nie Chonghou, the Tianjin notable Pan Zixin, the fixer Hu Yongquan, Fan Xing's
companion Peng Yaluo, Chen's schoolmate Gao Rong) plus the variant glyph 兪叶封
(the source writes 兪 for 俞) so qc gates Yu Yefeng in this unit too.

One-off names rendered inline in pinyin, NOT keyed (glossary-key discipline):
the telegram-distribution names 钱新民/廖公劭, the former secretary 刘方雄, the
sabotage-directive operatives 方步舟/谢冰/岳烛远/谢镇南/邹适, the CCP Jiangsu
Committee roster 刘晓/刘长胜/张爱萍/刘宁一/王尧山/沙文汉/张执一/刘少文, and
李士群's associate 叶吉卿. Shanghai roads (西摩路 Seymour Road, 杜美路 Route Doumer,
格罗希路 Route de Grouchy, 卡尔登公寓 Carlton Apartments, 静安商场 Jing'an Market,
etc.) keep their attested names inline and are NOT keyed."""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOSS = os.path.join(ROOT, "glossary.json")
ZH = os.path.join(ROOT, "data", "zh", "ch25.txt")

zh_text = open(ZH, encoding="utf-8").read()

PEOPLE = {
    "秦启荣": {"en": "Qin Qirong", "pinyin": "Qín Qǐróng", "status": "attested",
               "note": "A Shandong man of the sixth Whampoa class, named in Dai Li's "
                       "directive to command the Tianjin-Pukou demolition brigade and "
                       "organize the Qingdao action group."},
    "毛人凤": {"en": "Mao Renfeng", "pinyin": "Máo Rénfèng", "status": "attested",
               "note": "Dai Li's acting secretary-general and closest deputy, who "
                       "succeeded him at the head of the Juntong after Dai's death in 1946."},
    "潘汉年": {"en": "Pan Hannian", "pinyin": "Pān Hànnián", "status": "attested",
               "note": "The Chinese Communist Party's foremost intelligence operative in "
                       "occupied Shanghai, who worked the seam between the underground and "
                       "the Wang puppets' No. 76."},
    "聂崇侯": {"en": "Nie Chonghou", "pinyin": "Niè Chónghóu", "status": "provisional",
               "note": "A Jiangxi-born, German-trained doctor of ophthalmology in Shanghai "
                       "whom Chen recruited to interpret with the German arms-keeper. "
                       "Romanization mine."},
    "潘子欣": {"en": "Pan Zixin", "pinyin": "Pān Zǐxīn", "status": "provisional",
               "note": "\"Master Pan the Seventh,\" a Jiangsu-born Tianjin notable "
                       "(keeper of the National Grand Hotel) living hidden in Shanghai; "
                       "called \"the Du Yuesheng of Tianjin.\" Romanization mine."},
    "胡永荃": {"en": "Hu Yongquan", "pinyin": "Hú Yǒngquán", "status": "provisional",
               "note": "A volunteer worker of the Shanghai District, the well-connected "
                       "\"man who knew every road,\" who carried the German arms gift from "
                       "Hong Kong. Romanization mine."},
    "高荣": {"en": "Gao Rong", "pinyin": "Gāo Róng", "status": "provisional",
             "note": "Chen's twice-over schoolfellow (see Part One), chief of the Suiyuan "
                     "Station, charged with the Beiping-Suiyuan railway demolition unit. "
                     "Romanization mine."},
    "彭雅萝": {"en": "Peng Yaluo", "pinyin": "Péng Yǎluó", "status": "provisional",
               "note": "Fan Xing's companion, who kept the secondhand bookshop in the "
                       "Jing'an Market with him. Romanization mine."},
    # variant glyph: the source writes 兪 (U+516A) for 俞; same man as 俞叶封.
    "兪叶封": {"en": "Yu Yefeng", "pinyin": "Yú Yèfēng", "status": "attested",
               "note": "Variant-glyph spelling (兪 for 俞) of Yu Yefeng, the collaborator "
                       "sanctioned at the Gengxin Stage in January 1940 (ch24)."},
}


def main():
    gl = json.load(open(GLOSS, encoding="utf-8"))
    added = 0
    for k, v in PEOPLE.items():
        if k not in zh_text:
            sys.exit("KEY NOT IN data/zh (possible mangling): %r" % k)
        if k in gl["people"]:
            if gl["people"][k].get("en") != v["en"]:
                sys.exit("CONFLICT: %s already keyed to %r" % (k, gl["people"][k]))
            continue
        gl["people"][k] = v
        added += 1
    json.dump(gl, open(GLOSS, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("added %d new rows; people=%d" % (added, len(gl["people"])))


if __name__ == "__main__":
    main()
