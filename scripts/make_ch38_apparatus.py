# Build data/ch38_apparatus.json for apparatus_merge.py.
# Note bodies authored as plain ASCII + typed hanzi (+ em dashes), then every
# non-ASCII char is converted to a numeric character reference before writing.
# EVERY non-ASCII hanzi glyph used in a note body is asserted to occur in ch38's
# own authoritative data/zh/ch38.txt. Anchors are ASCII substrings of
# ch38_reading.md, with no em dash and no quote/apostrophe. Pinyin is untoned.
#
# ch38 is a Part-Four narrative chapter (the case of Zhu Zhankui, the defector who
# came over to the Nationalists, was made a district commissioner and security
# commander, worked in concert with Chen's assault team through 1948, and in the
# end lured them into a trap and went back to the Communists). Furniture already
# noted is NOT re-noted: the 绥靖/戡乱/共匪 civil-war framing, 匪谍/共酋/共干, the
# Juntong/Baomiju, the Lizhi Class and the Central Training Corps, the Youth Army,
# the North China Bandit-Suppression HQ, the assault team, the Republican-year
# system, the Marco Polo Bridge / Double-Seventh Incident, the Three Principles of
# the People, the Red Guards and the Cultural Revolution, the tunnel warfare and
# the Type 38 rifle, He Long's Jiangxi bandit-suppression days (all covered in
# earlier batches). The eight new notes cover items a Western reader first meets here.
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CID = "ch38"
zh = open(os.path.join(ROOT, "data", "zh", CID + ".txt"), encoding="utf-8").read()
reading = open(os.path.join(ROOT, "out", CID + "_reading.md"), encoding="utf-8").read()

NOTES = [
    {
        "anchor": "Anti-Japanese University",
        "note": (
            "The 'Anti-Japanese University' was the Chinese People's Anti-Japanese "
            "Military and Political University (抗日军政大学, 'Kangda' 抗大 for short), "
            "the Communist Party's foremost academy for military and political cadres "
            "at Yan'an. Founded in 1936 as the Red Army University (红军大学) and "
            "renamed the following year, it put many tens of thousands of cadres "
            "through short, intensive courses across the war years. Chen writes of it "
            "with scorn; historians count it a central instrument of the Party's "
            "wartime growth."
        ),
    },
    {
        "anchor": "bandit chieftain He Long",
        "note": (
            "He Long (贺龙, 1896-1969) was a founder of the Chinese Red Army and leader "
            "of the Nanchang Uprising of 1927; through the war against Japan he "
            "commanded the 120th Division of the Eighth Route Army, and after 1949 was "
            "made one of the ten marshals of the People's Liberation Army. As Chen goes "
            "on to note, even so decorated a figure was persecuted in the Cultural "
            "Revolution and died under it in 1969; he was posthumously rehabilitated "
            "in 1974."
        ),
    },
    {
        "anchor": "help Xiao Ke",
        "note": (
            "Xiao Ke (萧克, 1907-2008) was a senior Red Army commander who served as "
            "deputy commander of the 120th Division under He Long; he was ranked a full "
            "general of the People's Liberation Army in 1955."
        ),
    },
    {
        "anchor": "as a chuigushou",
        "note": (
            "A chuigushou (吹鼓手, literally a 'blower-and-drummer') was an itinerant "
            "folk bandsman hired to play at village weddings, funerals, and festivals, "
            "chiefly upon the suona, the loud double-reed shawm Chen here calls the laba "
            "(喇叭, 'horn'). The trade ranked low in social esteem, which is the point "
            "of Chen's dwelling upon it: it marks how humble Zhu Zhankui's beginnings "
            "were, and gives the bitter close of the chapter its sting."
        ),
    },
    {
        "anchor": "patter-rhyme of the storyteller",
        "note": (
            "Chen likens the instructor's jingle to the 数白嘴 and 流口辙 (shu bai zui, "
            "liu kou zhe) of the folk performing arts: the rapid, rhymed, tongue-"
            "tripping patter of the kuaiban clapper-talker and the xiangsheng comic "
            "dialogue, glib and easy to remember but of no weight. The point is that "
            "the crude mnemonic, for all that, held good in the trial."
        ),
    },
    {
        "anchor": "Eighteenth Group Army",
        "note": (
            "On the forming of the second united front in 1937, the Communist forces in "
            "North China were taken into the National Revolutionary Army as the Eighth "
            "Route Army (八路军), formally styled the Eighteenth Group Army "
            "(第十八集团军); under nominal Nationalist command they were made up of the "
            "115th, 120th, and 129th Divisions. With the New Fourth Army south of the "
            "Yangtze, these were the two principal Communist field armies of the war. "
            "Chen's point is that the numbering was a Nationalist grant, which the "
            "Communists soon cast off for designations of their own."
        ),
    },
    {
        "anchor": "Hanyang-made",
        "note": (
            "The 'Hanyang-made 7.9' is the Hanyang rifle (汉阳造), the Chinese-built "
            "copy of the German Gewehr 88 in 7.9mm, turned out at the Hanyang Arsenal "
            "from 1895 and the most widely produced domestic rifle in Chinese hands "
            "into the 1940s. The 'Type 38' beside it is the Japanese Arisaka service "
            "rifle."
        ),
    },
    {
        "anchor": "employ a man and doubt him not",
        "note": (
            "A maxim of statecraft, in the source 用而不疑、疑而不用 ('employ a man and "
            "doubt him not; doubt a man and employ him not'), counseling that a ruler "
            "either trust a servant wholly or not take him into service at all. The "
            "magnanimity Chen pairs with it, 泱泱大度 &#8212; the phrase that titles this "
            "section &#8212; is the broad, unhurried bearing proper to a great state: "
            "the willingness to win men over rather than hold them at arm's length."
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
