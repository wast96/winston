# Build data/ch35_apparatus.json for apparatus_merge.py.
# Note bodies authored as plain ASCII + typed hanzi (+ em dashes), then every
# non-ASCII char is converted to a numeric character reference before writing.
# EVERY non-ASCII hanzi glyph used in a note body is asserted to occur in ch35's
# own authoritative data/zh/ch35.txt (a Write-tool corruption would produce a
# glyph absent from the source and trip the assert). Anchors are ASCII substrings
# of ch35_reading.md, with no em dash and no quote/apostrophe. Pinyin is untoned.
#
# ch35 is a narrative chapter (reporting for duty; gathering old comrades; the
# operation to reach Lin Biao and Tao Zhu through Li Mingqiu; the comrades' fates).
# Furniture already noted is NOT re-noted: the 绥靖/戡乱/共匪 civil-war framing, the
# Juntong/Baomiju, 特种部队/特种组织, the Lizhi Class, the Loyal and Patriotic Army,
# the Transport Police Corps, Whampoa, Tilanqiao, the Japanese gendarmerie, the
# Republican-year system; the 1927 Ning-Han split (the purge is cross-referenced,
# not re-explained); the Cultural Revolution and Red Guards, and Tao Zhu's fall
# (already noted). The eight new notes cover items a Western reader first meets here.
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CID = "ch35"
zh = open(os.path.join(ROOT, "data", "zh", CID + ".txt"), encoding="utf-8").read()
reading = open(os.path.join(ROOT, "out", CID + "_reading.md"), encoding="utf-8").read()

NOTES = [
    {
        "anchor": "one great white arched bridge of stone",
        "note": (
            "The Jin'ao-Yudong Bridge (金鳌玉𬟽桥, romanized Jin'ao Yudong; the "
            "source's second character 玉𬟽 is a variant form): a long "
            "white-marble bridge spanning the water between the North Lake (北海) "
            "and the Zhongnanhai (中南海) lake-park, west of the Forbidden City. At "
            "each end stood a stone memorial archway inscribed 金鳌 ('Golden "
            "Sea-Turtle') and 玉𬟽 ('Jade Rainbow'). It was built of 汉白玉 "
            "(hanbaiyu), the fine white marble quarried near Beijing and used "
            "throughout the imperial city; the two archways were dismantled and the "
            "bridge widened in the mid-1950s."
        ),
    },
    {
        "anchor": "this sight should belong to Heaven alone",
        "note": (
            "Chen quotes the couplet 此景只应天上有，人间那得几回看 ('this sight "
            "should belong to Heaven alone; how many times may it be seen in the "
            "mortal world?'). It adapts a famous line by the Tang poet Du Fu, from "
            "his quatrain 'To General Hua,' whose original runs 'this tune should "
            "belong to Heaven alone; how many times may it be heard in the mortal "
            "world?' &#8212; Du Fu's ironic praise of music too fine for a mere "
            "general's house. Chen turns 'tune' and 'heard' into 'sight' and 'seen' "
            "for the rain-washed bridge."
        ),
    },
    {
        "anchor": "the chasing of the deer and the chasing of the stink",
        "note": (
            "Two set phrases. 'Chasing the deer' (逐鹿) is the classical figure for "
            "contending for the throne or for power, the deer standing for the "
            "empire pursued by rival hunters. 'Chasing the stink' (逐臭) alludes to "
            "a classical anecdote of a man whose smell repelled everyone yet whom "
            "one person doggedly followed &#8212; hence the pursuit of base or "
            "sordid gain. Chen means the two posts offered him were rich prizes "
            "alike for the power-hungry and for the graft-hungry."
        ),
    },
    {
        "anchor": "died in a manner dark and unexplained",
        "note": (
            "Lin Biao (林彪, 1907-1971), Communist commander in the Northeast and "
            "later Mao Zedong's (毛泽东) defense minister, was written into the "
            "Party constitution in 1969 as Mao's designated 'successor' (接班人) and "
            "'Vice-Chairman' (副主席). In September 1971, after an alleged plot "
            "against Mao, he died when his plane crashed at Ondorhaan in Mongolia "
            "as he fled toward the Soviet Union; the affair was long shrouded in "
            "secrecy, which is the 'riddle' Chen twice invokes."
        ),
    },
    {
        "anchor": "Party Purge",
        "note": (
            "The 'Party Purge' (清党, qingdang) of April 1927: the violent "
            "expulsion and killing of Communists within the Nationalist Party and "
            "army after Chiang Kai-shek broke with the Communists and the Wuhan "
            "left. At the Whampoa Academy, cadets who had joined the Communist "
            "Party were made to fall out and were arrested; the scene Chen "
            "describes belongs to this purge, the same rupture noted elsewhere as "
            "the 'Ning-Han Split.'"
        ),
    },
    {
        "anchor": "Guangzhou Uprising",
        "note": (
            "The Guangzhou Uprising of 11-13 December 1927, which Chen and Tao Zhu "
            "call by its date, 'the December Twelfth' (双十二): a Communist "
            "insurrection (广州大暴动) that briefly seized parts of the city and "
            "proclaimed a 'Guangzhou Commune,' crushed by Nationalist forces within "
            "three days at heavy cost. Tao Zhu, held after the Whampoa purge, was "
            "among those freed in the rising and swept into the fighting."
        ),
    },
    {
        "anchor": "social department",
        "note": (
            "The 'Social Affairs Department' (社会部, shehuibu; the source writes "
            "社会部门) was the Chinese Communist Party's central intelligence and "
            "security organ, headed through the 1940s by Kang Sheng, not by Luo "
            "Ronghuan. Luo Ronghuan (罗荣桓) was in fact political commissar of the "
            "Northeast field army &#8212; senior in the Party to Lin Biao (林彪), "
            "and later one of the ten marshals of the People's Republic. Chen's "
            "placing of him at the head of the 'social department' is his own "
            "surmise (his text says only that Luo 'must be'), and is not borne out."
        ),
    },
    {
        "anchor": "would drag him out and shoot him",
        "note": (
            "Three campaigns of the early People's Republic. The Three-Anti (三反, "
            "1951) targeted corruption, waste, and bureaucracy among officials; the "
            "Five-Anti (五反, 1952) targeted private businessmen; the Campaign to "
            "Suppress Counter-revolutionaries (镇压反革命, 1950-1953) hunted former "
            "Nationalist officials, officers, and agents, and killed them in great "
            "numbers. Chen's old comrades who stayed on the mainland were caught "
            "and destroyed in these movements."
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
