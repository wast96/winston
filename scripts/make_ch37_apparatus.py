# Build data/ch37_apparatus.json for apparatus_merge.py.
# Note bodies authored as plain ASCII + typed hanzi (+ em dashes), then every
# non-ASCII char is converted to a numeric character reference before writing.
# EVERY non-ASCII hanzi glyph used in a note body is asserted to occur in ch37's
# own authoritative data/zh/ch37.txt. Anchors are ASCII substrings of
# ch37_reading.md, with no em dash and no quote/apostrophe. Pinyin is untoned.
#
# ch37 is a Part-Four narrative chapter (the fall of Shimen and the terror that
# followed; the pacification unit welcomed in the North Suburb, shunned in the
# West; and the night battle of Lishuiqiao between the local corps and the
# Communist militia). Furniture already noted is NOT re-noted: the 绥靖/戡乱/共匪
# civil-war framing, 匪谍/共酋/共干, the Juntong/Baomiju, the Lizhi Class, the
# Anti-Japanese Traitor-Killing Corps and the Renaissance Society (Blue Shirts),
# the North China Loyal and Patriotic Army and the Luan-Yu Guerrilla HQ, the
# North China Bandit-Suppression HQ and Beiping Field Headquarters, the Youth
# Army, the assassination of Wang Kemin, the Republican-year system, the Double
# Tenth, the Green Gang's generation ranks, Jing Ke, and Zhao Yun's feat at
# Changban (all covered in earlier batches). The eight new notes cover items a
# Western reader first meets here.
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CID = "ch37"
zh = open(os.path.join(ROOT, "data", "zh", CID + ".txt"), encoding="utf-8").read()
reading = open(os.path.join(ROOT, "out", CID + "_reading.md"), encoding="utf-8").read()

NOTES = [
    {
        "anchor": "Jin-Ji-Lu-Yu Border Region",
        "note": (
            "Chinese place-compounds of this kind are built from one-character "
            "abbreviations of the provinces they span: 晋 (Jin) for Shanxi, 察 (Cha) "
            "for Chahar, 冀 (Ji) for Hebei, 鲁 (Lu) for Shandong, and 豫 (Yu) for "
            "Henan. Thus 'Jin-Cha-Ji' is the Shanxi-Chahar-Hebei border zone and "
            "'Jin-Ji-Lu-Yu' the Shanxi-Hebei-Shandong-Henan border zone. The "
            "Communists' wartime 'border regions' (边区) were base areas straddling "
            "such provincial edges, where the reach of the central government was "
            "weakest; the profusion of shifting designations that Chen remarks on is "
            "a symptom of that improvised, overlapping administration."
        ),
    },
    {
        "anchor": "Strip-It-Clean Force",
        "note": (
            "The epithet in the source is 三光部队, the 'Three-Alls Force.' The phrase "
            "三光 ('three alls') was the byword for the Japanese army's scorched-earth "
            "policy in North China &#8212; 'burn all, kill all, loot all.' Here it is "
            "turned mockingly upon the Nationalist takeover officials, who after the "
            "1945 victory were widely reviled for stripping the recovered areas bare "
            "for their own gain; to brand them a 'Three-Alls Force' was to say their "
            "plunder was no better than the enemy's."
        ),
    },
    {
        "anchor": "The wind blows bleak",
        "note": (
            "The line 风萧萧兮 ('the wind blows bleak...') opens the parting song that "
            "Jing Ke &#8212; the Warring-States assassin met with in an earlier "
            "chapter &#8212; is said to have sung at the Yi River as he set out to "
            "kill the King of Qin, knowing he would not return: 'The wind blows "
            "bleak, the Yi River cold; the brave man, once gone, comes back no more.' "
            "To part 'in the mood of that line' is to part as men going to their death."
        ),
    },
    {
        "anchor": "Du Xinwu of Cili in Hunan",
        "note": (
            "Du Xinwu (whose name is properly written 杜心五, 1869-1953) was a famed "
            "martial artist, master of the 自然门 ('Natural Gate') boxing school and "
            "a figure of the sworn brotherhoods. The 洪门 (Hongmen) and the 青帮 "
            "(Green Gang) were the two great secret fraternities of Republican China; "
            "a 龙头 ('dragon head') was the head of a Hongmen lodge, while the Green "
            "Gang ranked its members by seniority generations, the 大字辈 or "
            "'Da-character generation' being a senior one. That a single man should "
            "hold high standing in both, as Du did, was uncommon."
        ),
    },
    {
        "anchor": "Four Great Dan",
        "note": (
            "The 'Four Great Dan' (四大名旦) were the four most celebrated performers "
            "of female roles (旦, dan) in Peking opera between the wars: Mei Lanfang, "
            "Cheng Yanqiu, Shang Xiaoyun, and Xun Huisheng. Cheng Yanqiu, famed for "
            "his grave and muffled singing style, remained on the mainland after 1949 "
            "and was admitted to the Communist Party not long before his death in "
            "1958 &#8212; the 'leaning to the left,' and then 'toppling over,' at "
            "which Chen, writing from Taiwan, glances here."
        ),
    },
    {
        "anchor": "chicken-feather added",
        "note": (
            "The 'chicken-feather letter' (鸡毛信, jimao xin) was a folk convention of "
            "the North China countryside for marking a dispatch's urgency: a chicken "
            "feather stuck to the envelope meant 'urgent, carry with all speed,' the "
            "feather standing for the wings of haste. Here the villagers' relay grades "
            "its messages in three degrees, the most urgent of all marked not with a "
            "feather but with a matchstick (火柴梗) tied on."
        ),
    },
    {
        "anchor": "baojia office",
        "note": (
            "The baojia (保甲) was the old system of household mutual-responsibility "
            "and registration, revived by the Nationalist government in the 1930s as "
            "the base tier of local control: households were grouped into jia and jia "
            "into bao, each with a headman answerable for the conduct, movements, and "
            "guests of those beneath him. The 'baojia office' here is that headman's "
            "office, through which the village watch, courier, and household-check "
            "duties were dispatched &#8212; the very apparatus the pacification unit "
            "worked through, and which the Communists worked through in their turn."
        ),
    },
    {
        "anchor": "The Battle of Moxingling",
        "note": (
            "Moxingling (摩星岭, Mount Davis) is a hill on the western tip of Hong "
            "Kong Island where, in 1949-50, the British authorities housed thousands "
            "of destitute Nationalist soldiers and refugees who had fled the "
            "mainland. On 1 May 1950 a clash there between the refugees and local "
            "leftists left casualties on both sides, after which the camp was cleared "
            "and its people removed to Rennie's Mill in the eastern New Territories. "
            "It is this 'open strife and hidden struggle' that Bai Jiaqi's magazine "
            "piece took for its subject."
        ),
    },
]


def to_ncr(s):
    return "".join(ch if ord(ch) < 128 else "&#%d;" % ord(ch) for ch in s)


def main():
    for e in NOTES:
        assert e["anchor"] in reading, "anchor not in reading: %r" % e["anchor"]
        assert reading.count(e["anchor"]) >= 1
        for ch in e["anchor"]:
            assert ord(ch) < 128, "anchor has non-ASCII: %r" % e["anchor"]
            assert ch not in "—\"'‘’“”", \
                "anchor has a forbidden char: %r" % e["anchor"]
        for ch in e["note"]:
            if ord(ch) >= 128 and ch != "—":
                assert ch in zh, \
                    "note glyph not in data/zh/%s.txt: %r" % (CID, ch)
        e["note"] = to_ncr(e["note"])
    dest = os.path.join(ROOT, "data", CID + "_apparatus.json")
    json.dump({"notes": {CID: NOTES}}, open(dest, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print("wrote %s (%d notes)" % (dest, len(NOTES)))


if __name__ == "__main__":
    main()
