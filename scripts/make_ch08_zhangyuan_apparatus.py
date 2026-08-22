# Whole-book reconciliation note (B36, completion batch): introduce the city
# Zhangjiakou / Kalgan at its first appearance (ch08) and record that Chen also
# calls it by its literary name Zhangyuan (张垣), the form he favors in the
# Part-Four chapters on the 1946-49 fighting. The lone ch08 张垣 has been aligned
# to "Zhangyuan" so 张垣 -> Zhangyuan / 张家口 -> Zhangjiakou now holds book-wide.
# Anchor is the first "Zhangjiakou" in ch08 ("sent off to Zhangjiakou"); note
# glyphs 张家口/张垣 are asserted present in data/zh/ch08.txt, then NCR-encoded.
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CID = "ch08"
zh = open(os.path.join(ROOT, "data", "zh", CID + ".txt"), encoding="utf-8").read()
reading = open(os.path.join(ROOT, "out", CID + "_reading.md"), encoding="utf-8").read()

NOTES = [
    {
        "anchor": "sent off to Zhangjiakou",
        "note": (
            "Zhangjiakou (张家口), a city in Chahar province -- now in northwestern "
            "Hebei -- commanding the pass through the Great Wall onto the Mongolian "
            "plateau; long known to Mongols and Westerners as Kalgan (from the "
            "Mongolian for 'gate' or 'barrier'), it was the great entrepot of the "
            "caravan tea-road to Russia and, in these years, a strategic prize on "
            "the northern front. Chen also calls it by its literary name Zhangyuan "
            "(张垣), the form he uses more often in the later chapters on the 1946-49 "
            "fighting; the two names are one place."
        ),
    },
]


def to_ncr(s):
    return "".join(ch if ord(ch) < 128 else "&#%d;" % ord(ch) for ch in s)


def main():
    for e in NOTES:
        assert e["anchor"] in reading, "anchor not in reading: %r" % e["anchor"]
        for ch in e["anchor"]:
            assert ord(ch) < 128 and ch not in "—\"'‘’“”", \
                "bad anchor char: %r" % e["anchor"]
        for ch in e["note"]:
            if ord(ch) >= 128 and ch != "—":
                assert ch in zh, "note glyph not in data/zh/%s.txt: %r" % (CID, ch)
        e["note"] = to_ncr(e["note"])
    dest = os.path.join(ROOT, "data", CID + "_zhangyuan_apparatus.json")
    json.dump({"notes": {CID: NOTES}}, open(dest, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print("wrote %s (%d notes)" % (dest, len(NOTES)))


if __name__ == "__main__":
    main()
