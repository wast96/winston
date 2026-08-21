# Build data/ch39_apparatus.json for apparatus_merge.py.
# Note bodies authored as plain ASCII + typed hanzi (+ em dashes), then every
# non-ASCII char is converted to a numeric character reference before writing.
# EVERY non-ASCII hanzi glyph used in a note body is asserted to occur in ch39's
# own authoritative data/zh/ch39.txt. Anchors are ASCII substrings of
# ch39_reading.md, with no em dash and no quote/apostrophe. Pinyin is untoned.
#
# ch39 is a Part-Four narrative chapter (battlefield-clearing after the Laishui
# campaign; Fu Zuoyi's vacillating strategy and the destruction of his 35th Army
# at Xinbao'an; the Nanjing conference, the audience with Chiang, and the plan to
# move the unit south). Furniture already noted earlier is NOT re-noted: the
# 绥靖/戡乱/共匪 framing, 匪谍/共酋/共干, the Juntong/Baomiju, the Lizhi Class and the
# Central Training Corps, the North China Bandit-Suppression HQ, the assault team,
# the Republican-year system, Whampoa/the Central Military Academy, Fu Zuoyi and
# the surrender of Beiping, the Lixingshe/Blue Shirts, the province one-character
# abbreviations, the baojia, and the heart-extraction tactic. The eight new notes
# cover items a Western reader first meets here.
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CID = "ch39"
zh = open(os.path.join(ROOT, "data", "zh", CID + ".txt"), encoding="utf-8").read()
reading = open(os.path.join(ROOT, "out", CID + "_reading.md"), encoding="utf-8").read()

NOTES = [
    {
        "anchor": "City of the Wrongfully Dead",
        "note": (
            "In Chinese folk belief the 'City of the Wrongfully Dead' (枉死城, "
            "wangsicheng) is a quarter of the underworld set apart for those who died "
            "before their allotted span or by violence and injustice &#8212; the "
            "drowned, the murdered, the war-slain, suicides &#8212; who must linger "
            "there, barred from passing on to rebirth, until their proper time comes "
            "round. Chen invokes it for the country people cut down as they fled the "
            "fighting."
        ),
    },
    {
        "anchor": "the Laishui campaign",
        "note": (
            "The Laishui campaign (涞水之役) was fought in January 1948 around Laishui "
            "county, southwest of Beiping, between Fu Zuoyi's elite 35th Army and the "
            "North China field forces of the Communist commander Nie Rongzhen. Drawn "
            "into a costly engagement, the 35th Army was beaten; its division commander "
            "Li Mingding (李铭鼎) and its army commander (Chen's 鲁英庆, whose given name "
            "the histories give variously) both took their own lives. Communist accounts "
            "reckon it a victory that checked the Nationalist advance along the Ping-Han "
            "railway; Chen tells it as a story of heroic sacrifice. It foreshadows the "
            "far greater disaster of the same army at Xinbao'an later in the year."
        ),
    },
    {
        "anchor": "the town of Xinbao",
        "note": (
            "The battle of Xinbao'an (新保安), 6-24 December 1948, was an opening act of "
            "the Pingjin Campaign, the Communist conquest of the Beiping-Tianjin region. "
            "Fu Zuoyi's crack 35th Army, sent west to relieve Zhangjiakou and then "
            "ordered back, was cut off and surrounded at the walled town of Xinbao'an, "
            "east of Xuanhua, by Nie Rongzhen's North China forces together with part of "
            "Lin Biao's army come in through the Great Wall; after a week's siege it was "
            "destroyed on 24 December and its commander Guo Jingyun (郭景云) took his own "
            "life. The loss of his best army broke Fu Zuoyi's will and drew him toward "
            "the negotiated surrender of Beiping a month later. Chen's 'not one came "
            "back alive' is a martyr's flourish: the army was annihilated and Guo died, "
            "but many thousands were in fact taken prisoner."
        ),
    },
    {
        "anchor": "the secrets had been leaked beforehand",
        "note": (
            "Chen's suspicion was well founded. Fu Zuoyi's headquarters was deeply "
            "penetrated by Communist intelligence (泄密): his own daughter Fu Dongju, a "
            "Party member working as a journalist, relayed her father's plans to the "
            "Communist side, and other agents sat close about him &#8212; so that his "
            "troop movements were often known to the enemy in advance. This penetration "
            "is generally credited as one cause of the swift Communist victories around "
            "Beiping and of Fu's eventual decision to give up the city. The deputy chief "
            "of staff (副参谋长) whom Chen names cannot be identified here with certainty."
        ),
    },
    {
        "anchor": "Be a nameless hero",
        "note": (
            "The phrase Chiang Kai-shek uses to send Chen off &#8212; 作一个无名英雄, 'be "
            "a hero without a name' &#8212; is the source of this book's title, 英雄无名, "
            "'Nameless Heroes.' It names the ethos of the secret service Chen served: "
            "that its work, by its very nature, could win no public fame, and its dead "
            "could be given no public honor. Chen returns to the phrase across the four "
            "volumes as the keynote of the whole memoir."
        ),
    },
    {
        "anchor": "the Dagong Bao",
        "note": (
            "The Dagong Bao (大公报, commonly romanized Ta Kung Pao, and styled in French "
            "'L'Impartial') was among the most respected Chinese newspapers of the "
            "Republican era, founded at Tianjin in 1902 and known between the wars for "
            "its independence and its liberal, non-partisan stance. Chen's charge that "
            "after 1949 it became a Communist 'mouthpiece' is broadly borne out: its "
            "mainland editions were absorbed into the state press system (the Tianjin "
            "paper was recast under Communist control), while the framing that it was "
            "run by the 'democratic parties' reflects the united-front politics of the "
            "early People's Republic. A Hong Kong edition, pro-Beijing, survives to this day."
        ),
    },
    {
        "anchor": "Kanjurwa Khutukhtu",
        "note": (
            "A khutukhtu (呼图克图, from the Mongolian for a 'holy' or 'blessed one') is "
            "a high reincarnate lama of Mongolian Tibetan Buddhism, a 'living Buddha' "
            "recognized as the rebirth of a line of predecessors. The Kanjurwa Khutukhtu "
            "(甘珠尔瓦呼图克图) was one of the senior such incarnations of Inner Mongolia, "
            "seated in the Chahar country; the holder of the title in this period later "
            "removed to Taiwan. Chen notes that the intelligence group at Duolun was "
            "staffed by Mongols and included the Khutukhtu's younger brother."
        ),
    },
    {
        "anchor": "the coldest of the deep-winter days",
        "note": (
            "'The deep-winter days' renders 数九寒天 (shu jiu han tian), literally 'the "
            "counted nines of the cold.' By an old North China folk reckoning the "
            "coldest stretch of winter is divided into nine nine-day periods, the 'nine "
            "nines,' counted from the winter solstice; the third and fourth nines, in "
            "January, are the bitterest. Chen invokes it for the cold in which the 35th "
            "Army starved and froze in the siege of Xinbao'an."
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
