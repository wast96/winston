# Build data/ch42_apparatus.json for apparatus_merge.py.
# Note bodies authored as plain ASCII + typed hanzi (+ em dashes), then every
# non-ASCII char is converted to a numeric character reference before writing.
# EVERY non-ASCII hanzi glyph used in a note body is asserted to occur in ch42's
# own authoritative data/zh/ch42.txt. Anchors are ASCII substrings of
# ch42_reading.md, with no em dash and no quote/apostrophe. Pinyin is untoned.
#
# ch42 is the tenth and LAST full Part-Four narrative chapter (the disbanding of
# the Pacification Corps, the withdrawal of the stay-behind men from besieged
# Beiping, the southward journey guarding Chiang's home region at Xikou/Fenghua
# and the brigade's dissolution at Penghu, and Chen's own post-1949 course
# through Hong Kong, Japan and back). Already-covered furniture is NOT re-noted:
# the 绥靖/戡乱/共匪 framing and the stay-behind work, the Juntong/Baomiju, Fu
# Zuoyi and Beiping's surrender, the Temple-of-Heaven airfield and the North
# China Bandit-Suppression HQ, the Republican-year system, the silver dollar and
# the Yuan big-head and the gold-yuan collapse, Whampoa, the Lizhi Class, the
# Xu-Bang Campaign. The ten new notes cover items a Western reader first meets
# here.
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CID = "ch42"
zh = open(os.path.join(ROOT, "data", "zh", CID + ".txt"), encoding="utf-8").read()
reading = open(os.path.join(ROOT, "out", CID + "_reading.md"), encoding="utf-8").read()

NOTES = [
    {
        "anchor": "dragged off and shot",
        "note": (
            "The Campaign to Suppress Counter-Revolutionaries (镇压反革命, zhenya "
            "fangeming, commonly 镇反) was a mass political purge across the new "
            "People's Republic in 1950-51, aimed at former Nationalist officials, "
            "officers, police, secret-service men, landlords, and 'bandit' remnants. "
            "Public accusation-trials and mass shootings were the rule; scholarly "
            "estimates of those killed run from the official figure of some 700,000 "
            "up to two million and more. Jiang Tian, a Nationalist agent left behind "
            "in Beiping, was exactly the kind of man it was aimed at."
        ),
    },
    {
        "anchor": "Tilanqiao",
        "note": (
            "Tilanqiao (提篮桥), in the Hongkou district of Shanghai, was the site of "
            "the Ward Road Gaol, opened by the foreign-run Municipal Council in 1903 "
            "and long the largest prison in the Far East; the place-name became a "
            "byword for the jail itself. That Chen and this 'street figure' had once "
            "been 'fellow inmates in trouble' there points back to Chen's own "
            "imprisonment, recounted in the earlier parts of the memoir."
        ),
    },
    {
        "anchor": "Ten thousand taxes for the Republic",
        "note": (
            "A bitter homophone pun. The stock cheer 万岁 (wansui, 'ten thousand "
            "years,' i.e. 'long live') is here twisted to its near-homophone 万税 "
            "(wanshui, 'ten thousand taxes'), so that 'Long live the Republic' "
            "becomes 'Ten thousand taxes for the Republic.' The wall-slogan mocks a "
            "government whose runaway paper money and levies had beggared the city."
        ),
    },
    {
        "anchor": "loyal outcasts and rejected sons",
        "note": (
            "孤臣孽子 (guchen niezi), literally 'the orphaned minister and the son of "
            "a concubine' -- the sidelined and the aggrieved -- alludes to the "
            "Mencius (7A.18), which holds that just such men, living in constant "
            "apprehension, are thereby sharpened in virtue and understanding. Hu Gui "
            "invokes it to cast his cast-adrift corps as men whose very hardship "
            "fits them to serve."
        ),
    },
    {
        "anchor": "that little building where His Excellency Chiang was born",
        "note": (
            "Xikou (溪口), in Fenghua, Zhejiang, was Chiang Kai-shek's native town, "
            "and the brigade's charge in early 1949 -- after Chiang had retired to "
            "it -- was to guard its approaches. The sights the men glimpse are its "
            "landmarks: the Wuling gate (武岭大门) at the village mouth; the Miaogao "
            "Terrace (妙高台), a hilltop retreat above Xuedou Monastery where Chiang "
            "often lodged; the Qianzhang Rock waterfall (千丈岩); and the Chiang "
            "family's ancestral house, holding the room in which Chiang was born in "
            "1887."
        ),
    },
    {
        "anchor": "huadiao and chenshao wines",
        "note": (
            "Shaoxing in Zhejiang is the home of China's most famous yellow "
            "rice-wines (黄酒). Huadiao (花雕, 'carved flower,' after the ornamented "
            "jars in which it was sealed and aged -- by custom laid down at a "
            "child's birth) and chenshao (陈绍, 'aged Shaoxing') are prized mellow "
            "grades, amber in color and warmed before drinking. For the young "
            "soldiers passing through, they were a local delicacy worth slipping out "
            "of barracks for."
        ),
    },
    {
        "anchor": "spirit-medium boy",
        "note": (
            "A jitong (乩童 -- the term is Southern Fujianese and Taiwanese) is a "
            "spirit-medium who, in a trance held to be possession by a god, delivers "
            "oracles and performs feats of self-mortification at temple rites. That "
            "a mainland officer could 'play' one well enough to awe the islanders is "
            "Chen's measure of how thoroughly his men had taken to Penghu."
        ),
    },
    {
        "anchor": "the great earthquake struck Tangshan",
        "note": (
            "The Tangshan (唐山) earthquake of 28 July 1976, of magnitude about 7.6, "
            "levelled the industrial city of Tangshan in Hebei and killed on the "
            "order of a quarter of a million people -- among the deadliest "
            "earthquakes of the twentieth century. Zhang Zuoxing, sentenced to "
            "'reform through labor' at a farm near Tangshan, would have lain in its "
            "path, which is why Chen reckons his chances 'more ill than good.'"
        ),
    },
    {
        "anchor": "no few old soldiers",
        "note": (
            "After 1949 the Nationalist government quietly recruited former Japanese "
            "officers of the occupation years as anti-Communist military advisers; "
            "the best-known group, the 'White Group' (白团, Baituan), served the "
            "Republic of China army on Taiwan into the 1960s. Of the men Chen names, "
            "Nemoto Hiroshi (根本博), once the last commander of the Japanese North "
            "China garrison, had slipped secretly to Taiwan in 1949 and is credited "
            "with helping plan the defense that threw back the Communist landing on "
            "Kinmen (Guningtou) that October; Wachi Takaji (和知鹰二) had headed "
            "Japanese special-service work in South China. Chen's own use of such "
            "men, in Japan, was a separate strand of the same turn to yesterday's "
            "enemy against today's."
        ),
    },
    {
        "anchor": "with a certain great power",
        "note": (
            "Chen leaves the 'great power' (某一大国) unnamed throughout. From the "
            "date (late 1949), the Hong Kong base, the shape of the arrangement -- "
            "money for intelligence, its fruits withheld from Chen's own government "
            "-- and the CAT (Civil Air Transport) airline he later flew, which the "
            "American CIA quietly bought in 1950, it is generally understood to be "
            "the United States. Early American intelligence ran just such deniable, "
            "arms-length contracts with stray Nationalist networks in these years."
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
