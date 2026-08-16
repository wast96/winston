# Build data/ch36_apparatus.json for apparatus_merge.py.
# Note bodies authored as plain ASCII + typed hanzi (+ em dashes), then every
# non-ASCII char is converted to a numeric character reference before writing.
# EVERY non-ASCII hanzi glyph used in a note body is asserted to occur in ch36's
# own authoritative data/zh/ch36.txt. Anchors are ASCII substrings of
# ch36_reading.md, with no em dash and no quote/apostrophe. Pinyin is untoned.
#
# ch36 is a Part-Four narrative chapter (the value and use of intelligence; the
# gun-gift affair that nearly drew Chen into an abuse-of-power case; the "heart-
# extraction" raid on Anguo that just missed Mao; the fighting and sacrifice at
# the Battle of Shijiazhuang). Furniture already noted is NOT re-noted: the 绥靖/
# 戡乱/共匪 civil-war framing, 匪谍/共酋/共干, the Juntong/Baomiju, 特种部队, the
# Lizhi Class and Central Training Corps, the North China Bandit-Suppression HQ
# and Beiping Field Headquarters, Fu Zuoyi, Whampoa, the Marco Polo Bridge (七七),
# the Republican-year system, the Three-Anti/Five-Anti/Suppress-Counterrevolutionaries
# campaigns, and Lin Biao's 1971 death (all covered in earlier batches). The eight
# new notes cover items a Western reader first meets here, one of them a scholarship
# verdict (Mao was not in fact at Anguo).
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CID = "ch36"
zh = open(os.path.join(ROOT, "data", "zh", CID + ".txt"), encoding="utf-8").read()
reading = open(os.path.join(ROOT, "out", CID + "_reading.md"), encoding="utf-8").read()

NOTES = [
    {
        "anchor": "already carries within it the sense of",
        "note": (
            "In the source edition the opening material of this chapter is printed "
            "more than once. The discussion of intelligence and its timeliness, "
            "together with the introduction of the two contributed accounts (by Xiao "
            "Runyu and Niu Guangjin), appears first as the chapter's preamble and is "
            "then restated here, with minor changes of wording, at the head of this "
            "first section; a part of it is repeated once more in the paragraphs that "
            "follow, where the section heading itself is even reproduced in the "
            "middle of a paragraph. The repetition is an artifact of the digital "
            "source and is preserved here as it stands."
        ),
    },
    {
        "anchor": "heart-extraction tactic",
        "note": (
            "The 'heart-extraction tactic' (掏心战术, taoxin zhanshu) is a raiding "
            "doctrine that drives a fast column deep into enemy-held territory to "
            "seize the enemy's headquarters or leadership at a stroke &#8212; to "
            "'cut out the heart' &#8212; rather than fighting through his forces "
            "piecemeal. Here it names the Provisional Third Army's dash on Anguo, "
            "aimed at capturing Mao Zedong himself."
        ),
    },
    {
        "anchor": "the old nest of the Chinese Communists",
        "note": (
            "Yan'an (延安), the town in northern Shaanxi that had been the Chinese "
            "Communists' capital and headquarters since 1937, was taken by "
            "Nationalist forces under Hu Zongnan on 19 March 1947. The capture was "
            "largely symbolic: the Communist leadership had withdrawn beforehand, "
            "and Yan'an was retaken by the Communists in April 1948. Chen returns to "
            "this event, and to Mao Zedong's escape from it, in section four."
        ),
    },
    {
        "anchor": "in jail together in the",
        "note": (
            "The 'Paojuzi' (炮局子, literally 'the artillery-works') was a prison in "
            "the northeast of the old city of Beiping, on a lane of the same name; "
            "under the Japanese occupation it was used to hold political prisoners "
            "and suspected members of the resistance."
        ),
    },
    {
        "anchor": "every one of Japanese make",
        "note": (
            "The 'Type 38' (三八式) and 'Type 30' (三〇式) rifles were the standard "
            "bolt-action infantry rifles of the Japanese army &#8212; the Arisaka "
            "Type 38 (adopted in the 38th year of Meiji, 1905) and its predecessor "
            "the Type 30 (1897). Left in vast numbers at the 1945 surrender, they "
            "armed militia and second-line units on every side of the civil war."
        ),
    },
    {
        "anchor": "carried a high degree of truth",
        "note": (
            "Chen's judgment that the intelligence placing Mao Zedong at Anguo was "
            "highly credible is not borne out. Through 1947 Mao Zedong (毛泽东) "
            "remained in northern Shaanxi (陕北) with the small column that had "
            "evacuated Yan'an, crossing eastward into Shanxi and Hebei only in the "
            "spring of 1948; the Shijiazhuang campaign of late 1947 was directed by "
            "the Jin-Cha-Ji field forces under Nie Rongzhen (聂荣臻), not by Mao in "
            "person. The report that he was directing it from the Temple of the "
            "Medicine King at Anguo was, on the evidence, mistaken."
        ),
    },
    {
        "anchor": "to take the bandit Mao Zedong alive",
        "note": (
            "Here and below Chen uses scornful Nationalist epithets for Mao Zedong: "
            "毛贼泽东 ('the bandit Mao Zedong') and, in the third section's heading "
            "and at its close, 毛酋 ('the Mao chieftain,' rendered 'the bandit chief "
            "Mao'; 酋 is the word for a tribal or bandit chieftain). They belong to "
            "the same idiom as 共匪 'the Communist bandits' and 匪酋 'bandit "
            "chieftains,' preserved throughout this translation."
        ),
    },
    {
        "anchor": "on the outskirts of Shimen",
        "note": (
            "The Battle of Shijiazhuang (石家庄, which Chen calls by its older name "
            "Shimen, 石门): from the spring of 1947 the Communists' Jin-Cha-Ji "
            "forces under Nie Rongzhen (聂荣臻) closed on the Hebei rail-junction "
            "city, and on 12 November 1947, after days of fighting, stormed and took "
            "it. It was the first sizable city the Communists captured and held, and "
            "a marked step in the turning of the North China war in their favor."
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
