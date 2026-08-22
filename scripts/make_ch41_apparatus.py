# Build data/ch41_apparatus.json for apparatus_merge.py.
# Note bodies authored as plain ASCII + typed hanzi (+ em dashes), then every
# non-ASCII char is converted to a numeric character reference before writing.
# EVERY non-ASCII hanzi glyph used in a note body is asserted to occur in ch41's
# own authoritative data/zh/ch41.txt (a correct glyph absent from the source is
# named in English only). Anchors are ASCII substrings of ch41_reading.md, with
# no em dash and no quote/apostrophe. Pinyin is untoned.
#
# ch41 is a Part-Four narrative chapter (the brigade's move south to its
# dissolution at Penghu; the fall of Tianjin and Beiping; the besieged-city
# street scenes of Chen's Beiping; and the flight out with Zheng Jiemin). The
# already-covered furniture is NOT re-noted: the 绥靖/戡乱/共匪 framing and the
# Communist-spy vocabulary, the Juntong/Baomiju, Fu Zuoyi and Beiping's surrender,
# the North China Bandit-Suppression HQ, the Republican-year system, the silver
# dollar and the Yuan big-head and the gold-yuan collapse (ch06/ch40), the Boxer
# Uprising and the 1901 settlement and the Eight-Power intervention (ch07/ch16),
# Duan Qirui (ch07), the Miaofeng temple fair and the 数九 winter (ch40/ch39),
# and the Xinbao'an-Zhangjiakou disaster (ch39). The nine new notes cover items a
# Western reader first meets here.
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CID = "ch41"
zh = open(os.path.join(ROOT, "data", "zh", CID + ".txt"), encoding="utf-8").read()
reading = open(os.path.join(ROOT, "out", CID + "_reading.md"), encoding="utf-8").read()

NOTES = [
    {
        "anchor": "the copper coins minted in the days of the Northern government",
        "note": (
            "The coinage of besieged Beiping was a tangle of layers. Above the "
            "worthless paper stood the silver dollar (银元); below it, for small "
            "change, circulated copper coins left from the Beiyang (Northern) "
            "government of the 1910s and 1920s. The common 'copper' (铜子儿) was a "
            "two-cash piece, locally called 'a big one' (大枚), so that the four "
            "hundred coppers a dollar fetched were in value only two hundred; a "
            "ten-cash 'small copper' also existed but went unused at Beiping. "
            "Earlier the local bank had issued paper 'hair notes' (毛票) worth a "
            "tenth of a dollar, and the old 'Official Money Bureau' (官钱局) its "
            "copper-cash notes. Bitten again and again by paper money, the townsfolk "
            "trusted only hard coin."
        ),
    },
    {
        "anchor": "hot-pot at the Donglaishun",
        "note": (
            "The Donglaishun (东来顺), founded about 1903 in the Dong'an Market off "
            "Wangfujing, is Beijing's most famous Muslim (Hui) restaurant, renowned "
            "above all for instant-boiled mutton (the source's 涮锅子, literally "
            "'rinse the pot'): paper-thin slices of lamb swirled by the diner in a "
            "charcoal-fired copper pot of simmering broth and eaten with a "
            "sesame-sauce dip. The 'sliced-meat' (片肉) master Chen watches was the "
            "knife-hand whose skill the house was known for. That such a place "
            "should blaze with light and sit full, with the enemy at the walls, is "
            "the very anomaly Chen dwells on."
        ),
    },
    {
        "anchor": "Altar of Land and Grain",
        "note": (
            "Chen is mistaken here: the Temple of Heaven (天坛) and the Altar of "
            "Land and Grain (社稷坛) are two different places. The Temple of Heaven, "
            "in the southern city, is where the Ming and Qing emperors sacrificed to "
            "Heaven and prayed for good harvests; its great round hall is the Hall of "
            "Prayer for Good Harvests (祈年殿), and it is that hall, indeed, whose "
            "silhouette serves as the emblem of the city. The Altar of Land and "
            "Grain is a separate, square altar just west of the Forbidden City, now "
            "within Zhongshan Park. The Yongle-reign dates Chen gives (1406 to 1420) "
            "are of the right order for the Temple-of-Heaven complex."
        ),
    },
    {
        "anchor": "also called Hademen",
        "note": (
            "Chongwenmen (崇文门), the southeastern gate of Beijing's inner city, was "
            "popularly called Hademen (哈德门), and a well-known cigarette brand took "
            "the name. Chen's folk etymology &#8212; that 'Hade' was a foreign "
            "general killed in the Eight-Power intervention of 1900, the gate named "
            "to force his remembrance as a 'national humiliation' &#8212; is, as he "
            "himself notes on being corrected, mistaken: the name is far older, "
            "traced to a Yuan-dynasty (13th-14th century) princely mansion near the "
            "gate. His parenthetical citation is to the Taipei journal Biographical "
            "Literature (传记文学)."
        ),
    },
    {
        "anchor": "mixed-grain flour",
        "note": (
            "'Mixed-grain flour' (杂合面, zahemian) was the cheapest of staples: a "
            "milled mixture of coarse grains and bean flours &#8212; millet, "
            "sorghum, corn, ground beans &#8212; eaten by the poor when wheat flour "
            "was out of reach. To pawn one's winter quilt to buy it, in the depth of "
            "the siege, was the last shift of the destitute."
        ),
    },
    {
        "anchor": "Eight Great Lanes",
        "note": (
            "The 'Eight Great Lanes' (八大胡同) were the licensed pleasure quarter of "
            "old Beijing, a cluster of small lanes just southwest of Qianmen, hard by "
            "the Dashilan theaters and the Tianqiao amusement grounds. Flourishing "
            "under the late Qing and the Republic, they held the graded courtesan "
            "houses Chen describes &#8212; from the 'pure-chant little troupe' "
            "(清吟小班), which professed to sell song and not the body, down to the "
            "plainer houses. The quarter was closed after 1949. Only the name was "
            "proverbial; brothels stood elsewhere in the city too."
        ),
    },
    {
        "anchor": "the five-colored flag giving way to the white sun",
        "note": (
            "Chen names the successive regimes by their flags. The five-colored flag "
            "(五色旗) &#8212; horizontal bars of red, yellow, blue, white, and black, "
            "for the five peoples of the young Republic &#8212; was the national flag "
            "from 1912 until the Northern Expedition; the Nationalists then replaced "
            "it with the 'white sun in a blue sky over a field of red' "
            "(青天白日满地红), which is still the flag of the Republic of China. The "
            "point of the passage is how many times, within four decades, Beiping had "
            "changed rulers: Beiyang warlords, Duan Qirui, Zhang Zuolin, the "
            "Nationalists, eight years of Japanese occupation, and now once more."
        ),
    },
    {
        "anchor": "John Leighton Stuart",
        "note": (
            "John Leighton Stuart (司徒雷登, 1876-1962) was an American "
            "missionary-educator born in Hangzhou, founder and long-time president of "
            "Yenching University in Beijing, and United States Ambassador to China "
            "from 1946 to 1949 &#8212; the years of the Marshall mediation and the "
            "civil war. His even-handed dealings with both sides drew Nationalist "
            "suspicion; after the Communist victory Mao Zedong marked his departure "
            "with the well-known essay 'Farewell, Leighton Stuart.' The aide Chen "
            "names, 傅泾波 (Fu Jingbo), was Stuart's Chinese secretary and closest "
            "confidant for decades."
        ),
    },
    {
        "anchor": "drawing of the firewood from under the cauldron",
        "note": (
            "'Drawing the firewood from under the cauldron' (釜底抽薪) is a proverb "
            "and one of the classic Thirty-Six Stratagems: rather than fight the "
            "boiling water directly, take away the fire beneath &#8212; that is, "
            "remove the root of a trouble. Chen's surmise is that Fu Zuoyi, if he had "
            "already judged Deng Baoshan (邓宝珊) a danger, sent him off to Nanjing "
            "precisely to draw him away from the source of harm."
        ),
    },
]


def to_ncr(s):
    return "".join(ch if ord(ch) < 128 else "&#%d;" % ord(ch) for ch in s)


def main():
    seen = set()
    for e in NOTES:
        assert e["anchor"] in reading, "anchor not in reading: %r" % e["anchor"]
        assert e["anchor"] not in seen, "duplicate anchor: %r" % e["anchor"]
        seen.add(e["anchor"])
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
