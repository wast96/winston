# Build data/ch43_apparatus.json for apparatus_merge.py.
# Note bodies authored as plain ASCII + typed hanzi (+ em dashes), then every
# non-ASCII char is converted to a numeric character reference before writing.
# EVERY non-ASCII hanzi glyph used in a note body is asserted to occur in ch43's
# own authoritative data/zh/ch43.txt. Anchors are ASCII substrings of
# ch43_reading.md, with no em dash and no quote/apostrophe. Pinyin is untoned.
#
# ch43 is the Afterword (篇后续话), the reflective coda that closes the whole
# five-book memoir. It is LIGHT on new material; already-covered furniture is
# NOT re-noted: the 制裁/sanction work (heavily footnoted from Part One on), the
# Nationalist 戡乱/共匪 framing, the Juntong/Baomiju, Dai Li the legendary
# spymaster, the Republican-year system, the War of Resistance, the journal
# Biographical Literature itself, the 特务/tewu debate. Only THREE new notes: a
# structural note reconciling the editor's five-book count with the four Parts
# of this collection; the publisher Liu Shaotang, met here for the first time;
# and the classical closing ideal 大中至正, on which the book's last argument
# turns.
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CID = "ch43"
zh = open(os.path.join(ROOT, "data", "zh", CID + ".txt"), encoding="utf-8").read()
reading = open(os.path.join(ROOT, "out", CID + "_reading.md"), encoding="utf-8").read()

NOTES = [
    {
        "anchor": "these five books",
        "note": (
            "The editor's note counts five books; the present collection, Nameless "
            "Heroes, gathers four of them as its four Parts: Part One, Rooting Out "
            "Traitors in the North (the editor's book 1); Part Two, Disgrace at "
            "Hanoi (his book 2, first published under the title The Full Story of "
            "the Wang Case at Hanoi); Part Three, Renown Won in a Hundred Battles, "
            "on the Shanghai operations (his book 3, whose plainer working title he "
            "gives here as Behind-the-Lines Operations at Shanghai); and Part Four, "
            "Pacification of the Beiping-Tianjin Region (his book 5). The remaining "
            "title in the list, Counter-Agent Work in the Latter Period of the War "
            "of Resistance (抗战后期反间活动, his book 4), is a separate volume of "
            "Chen's, cited elsewhere in these pages but not carried here as a Part."
        ),
    },
    {
        "anchor": "Mr. Liu Shaotang",
        "note": (
            "Liu Shaotang (刘绍唐, 1921-2000) founded, and for some four decades "
            "edited, the Taipei monthly Biographical Literature (传记文学), the "
            "foremost venue for Republican-era memoir and first-hand historical "
            "recollection; it was there that all of Chen's books were serialized "
            "before appearing between covers. So large was the archive of witness "
            "he gathered that he was commonly spoken of as a one-man bureau of "
            "unofficial history."
        ),
    },
    {
        "anchor": "the great, the central, and the utterly upright",
        "note": (
            "A rendering of 大中至正 (da zhong zhi zheng), a classical formula for "
            "supreme rectitude -- literally 'the great, the central, and the "
            "utterly correct' -- with roots in Song Neo-Confucian commentary on the "
            "Book of Changes. In Nationalist civic language the four characters "
            "stood for uprightness itself, and were famously inscribed on the "
            "memorial arch at the approach to the Chiang Kai-shek Memorial Hall in "
            "Taipei. Chen makes this ideal, together with 'the open and aboveboard' "
            "(光明磊落), the standard against which the old work of killing by "
            "sanction is at last weighed and set aside."
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
