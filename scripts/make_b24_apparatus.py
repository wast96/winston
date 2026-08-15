# Build data/ch30_apparatus.json and data/ch31_apparatus.json for apparatus_merge.py.
# Note bodies authored as plain ASCII + typed hanzi, then every non-ASCII char (the
# typed hanzi, any em-dash) is converted to a numeric character reference before
# writing. EVERY non-ASCII hanzi glyph used in a note body is asserted to occur in
# that unit's own authoritative data/zh/<id>.txt (a Write-tool corruption would
# produce a glyph absent from the source and trip the assert). Anchors are ASCII
# substrings of the unit's reading.md, with no em dash and no quote/apostrophe.
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(cid):
    zh = open(os.path.join(ROOT, "data", "zh", cid + ".txt"), encoding="utf-8").read()
    reading = open(os.path.join(ROOT, "out", cid + "_reading.md"), encoding="utf-8").read()
    return zh, reading


NOTES = {
    "ch30": [
        {
            "anchor": "pig-cage van",
            "note": (
                "The pig-cage van (猪笼车) was the barred prison wagon of the "
                "Shanghai police, so nicknamed for the caged compartment in which "
                "prisoners were carried; the equivalent of a Western police "
                "wagon or Black Maria."
            ),
        },
        {
            "anchor": "chief of the criminal section of the French police",
            "note": (
                "This French officer, whom Liu Yuanshen names Malone (马隆), was a "
                "paid inside contact of the Shanghai District within the French "
                "Concession police. Section 5 below, in Chen Gongshu's own "
                "narration, names the same man Malone (马龙): Liu and Chen spell the "
                "foreign name with different characters, but it is one officer. He "
                "could not save either of them, the enemy's demand for rendition "
                "being beyond his power to resist, but he did each a small kindness "
                "at the French station."
            ),
        },
        {
            "anchor": "the season of the Double Ninth",
            "note": (
                "The Double Ninth Festival (重阳), the ninth day of the ninth lunar "
                "month, falls in mid-autumn; in 1941 it came on 28 October, the day "
                "before the night here described. It marks the turn toward the cold "
                "of the year, which is the point of the reference."
            ),
        },
        {
            "anchor": "the longest day of my life",
            "note": (
                "From this section on, the narrating voice is no longer Liu "
                "Yuanshen's but the author's own: sections 3 (above), and the "
                "earlier sections 1 and 2 in Part 1 of this chapter, are from Liu "
                "Yuanshen's memoir, while section 4 here returns to Chen Gongshu "
                "narrating his own arrest. The source marks no change, and the two "
                "first-person accounts run on unbroken; Chen acknowledges the "
                "confusion and supplies this correction himself in the closing note "
                "of Part Three (see the following chapter, item 8)."
            ),
        },
        {
            "anchor": "Biluochun",
            "note": (
                "Biluochun (碧螺春, roughly 'green snail spring') is one of China's "
                "most celebrated green teas, grown around Lake Tai near Suzhou and "
                "prized for its tender early-spring leaf. The card, addressed to a "
                "boss of No. 76 and signed by Zhu Min, betrays his standing with "
                "the enemy."
            ),
        },
    ],
    "ch31": [
        {
            "anchor": "page sixty-five",
            "note": (
                "The parenthetical page citations throughout this note are the "
                "author's own, and refer to the pagination of the original serial "
                "or book edition, not to this translation, which has no fixed "
                "pages. They are kept as written; the corrections themselves are "
                "given in full."
            ),
        },
        {
            "anchor": "Xiaoshang River",
            "note": (
                "The two pieces named are operas: The Tale of Hongfu (红拂传), on a "
                "Tang-dynasty romance, and Xiaoshang River (小商河), on the death in "
                "battle of the Southern Song general Yang Zaixing (杨再兴), who "
                "served under the patriot commander Yue Fei (岳飞). The actor is "
                "recalling the running order of a Shanghai opera bill on which the "
                "singer Xin Yanqiu made her debut."
            ),
        },
        {
            "anchor": "reform through labour",
            "note": (
                "Reform through labour (劳动改造, laogai) was the penal-labour system "
                "of the People's Republic, under which convicts and political "
                "prisoners were held in camps and put to hard labour. The report is "
                "that Lin Huaibu, who had assassinated the magnate Zhang Xiaolin, "
                "was serving in such a camp in northern Jiangsu."
            ),
        },
    ],
}


def to_ncr(s):
    return "".join(ch if ord(ch) < 128 else "&#%d;" % ord(ch) for ch in s)


def main():
    for cid, items in NOTES.items():
        zh, reading = load(cid)
        for e in items:
            assert e["anchor"] in reading, "anchor not in reading: %r" % e["anchor"]
            for ch in e["anchor"]:
                assert ord(ch) < 128, "anchor has non-ASCII: %r" % e["anchor"]
                assert ch not in "—\"'‘’“”", \
                    "anchor has a forbidden char: %r" % e["anchor"]
            for ch in e["note"]:
                if ord(ch) >= 128 and ch != "—":
                    assert ch in zh, \
                        "note glyph not in data/zh/%s.txt: %r" % (cid, ch)
            e["note"] = to_ncr(e["note"])
        dest = os.path.join(ROOT, "data", cid + "_apparatus.json")
        json.dump({"notes": {cid: items}}, open(dest, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2)
        print("wrote %s (%d notes)" % (dest, len(items)))


if __name__ == "__main__":
    main()
