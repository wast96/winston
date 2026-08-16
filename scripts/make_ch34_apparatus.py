# Build data/ch34_apparatus.json for apparatus_merge.py.
# Note bodies authored as plain ASCII + typed hanzi (+ em dashes), then every
# non-ASCII char is converted to a numeric character reference before writing.
# EVERY non-ASCII hanzi glyph used in a note body is asserted to occur in ch34's
# own authoritative data/zh/ch34.txt (a Write-tool corruption would produce a
# glyph absent from the source and trip the assert). Anchors are ASCII substrings
# of ch34_reading.md, with no em dash and no quote/apostrophe. Pinyin is untoned.
#
# ch34 is the doctrinal chapter (defines the special-operations unit, three
# features, collective leadership), so it introduces FEW new items. Furniture
# already noted is NOT re-noted: the 特种部队/特种组织 concept-pair (ch33), the
# 绥靖/戡乱/共匪 civil-war framing, the Marshall Mission, the Lizhi Plan, the
# Jiangxi bandit-suppression/别働总队, the Youth Army (all ch32); the Baomiju
# (ch04); the Zhongshan tunic (ch06), the Renaissance Society/Blue Shirts (ch08),
# Duan Qirui (ch07), the Legation Quarter and the Hotel of Six Nations (ch06);
# Whampoa, fabi, the Republican-year system (earlier). The three new notes cover
# items a Western reader first meets here.
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CID = "ch34"
zh = open(os.path.join(ROOT, "data", "zh", CID + ".txt"), encoding="utf-8").read()
reading = open(os.path.join(ROOT, "out", CID + "_reading.md"), encoding="utf-8").read()

NOTES = [
    {
        "anchor": "Transport Police Corps",
        "note": (
            "The Transport Police Corps (交通警察总队, jiaotong jingcha zongdui): "
            "after the victory over Japan the Nationalist government, pressed by "
            "the Marshall mission to cut back its army, preserved the guerrilla "
            "force known as the Loyal and Patriotic Army (忠义救国军) by "
            "reorganizing it in 1946 as a paramilitary 'transport police,' "
            "nominally a railway-guard constabulary. Chen's point is that its real "
            "work was the suppression of the Communist rising, not the guarding of "
            "traffic."
        ),
    },
    {
        "anchor": "India-Burma Expeditionary Force",
        "note": (
            "The India-Burma Expeditionary Force (印缅远征军): the Chinese "
            "Expeditionary Force that fought the Japanese in Burma and along the "
            "India-Burma frontier from 1942 to 1945, alongside British and "
            "American troops, to keep open the land supply route into China. Liao "
            "Yaoxiang (廖耀湘, 1906-1968) was one of its senior commanders; Yang "
            "Rongyuan, the Communist agent unmasked here, had served under him as "
            "a junior officer before demobilization."
        ),
    },
    {
        "anchor": "Han Family Cooking",
        "note": (
            "'Tan Family Cooking' (谭家菜, Tanjiacai) is the most celebrated of "
            "Beijing's 'official-household' cuisines (官府菜)&#8212;a refined "
            "private table that grew out of the kitchen of Tan Zongjun, a "
            "Cantonese Hanlin scholar of the late Qing, and was carried on "
            "commercially by his son; run from a private home by reservation, it "
            "survived into the People's Republic and is served to this day at the "
            "Beijing Hotel. 'Han Family Cooking' (韩家菜) was a lesser house of the "
            "same kind. Chen, writing decades later, is unsure which of the two he "
            "was taken to."
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
