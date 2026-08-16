# Build data/ch33_apparatus.json for apparatus_merge.py.
# Note bodies authored as plain ASCII + typed hanzi (+ em dashes), then every
# non-ASCII char is converted to a numeric character reference before writing.
# EVERY non-ASCII hanzi glyph used in a note body is asserted to occur in ch33's
# own authoritative data/zh/ch33.txt (a Write-tool corruption would produce a
# glyph absent from the source and trip the assert). Anchors are ASCII substrings
# of ch33_reading.md, with no em dash and no quote/apostrophe. Pinyin is untoned.
#
# ch33 opens the on-the-ground 1946-49 narrative. Furniture already noted is NOT
# re-noted: the 绥靖/戡乱/共匪 civil-war framing, the Marshall Mission / Committee
# of Three / Executive Headquarters, the Lizhi Plan, the Jiangxi bandit-suppression
# / 别働总队, the Youth Army, Fu Zuoyi and the surrender of Beiping (all ch32); the
# Baomiju as the Juntong's 1946 successor (ch04); Whampoa, the Marco Polo Bridge,
# fabi, and the Republican-year system (earlier batches). The six new notes cover
# items a Western reader first meets here.
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CID = "ch33"
zh = open(os.path.join(ROOT, "data", "zh", CID + ".txt"), encoding="utf-8").read()
reading = open(os.path.join(ROOT, "out", CID + "_reading.md"), encoding="utf-8").read()

NOTES = [
    {
        "anchor": "old lair, at a single stroke",
        "note": (
            "Yan'an (延安), a county town in northern Shaanxi, was the seat of the "
            "Chinese Communist Party and the heart of its base area from 1937 until "
            "the spring of 1947, when Nationalist troops under Hu Zongnan took it. "
            "The Communists gave the town up without a real defense and retook it "
            "the following year; Chen cites its fall as proof that the Communist "
            "revolt could have been put down had the Americans not stayed his "
            "government's hand."
        ),
    },
    {
        "anchor": "special-operations unit of a new pattern",
        "note": (
            "'Special-operations unit' (特种部队, tezhong budui) and 'special "
            "organization' (特种组织, tezhong zuzhi) are Chen's terms for the "
            "special-warfare formations of the secret service. The chapter that "
            "defines them (Part Four, chapter two) glosses 特种部队 as 'Special "
            "Forces'; it is rendered here 'special-operations unit,' after this "
            "chapter's own section title. The 'special organization' whose decay "
            "the Leader mourned was the older service, the Juntong foremost among "
            "them; the Pacification Corps was the new one raised in its place."
        ),
    },
    {
        "anchor": "faded door-gods",
        "note": (
            "Door-gods (门神, menshen): paired guardian figures, printed on paper "
            "or painted, pasted one to each leaf of a gate to keep evil and "
            "ill-luck from the household. The pair are traditionally the Tang "
            "generals Qin Qiong and Yuchi Gong, who once stood watch over the "
            "emperor's door, or the demon-queller Zhong Kui."
        ),
    },
    {
        "anchor": "Heavenly Dog",
        "note": (
            "In Chinese folk belief the Heavenly Dog (天狗, tiangou) was the beast "
            "that devoured the sun or the moon to bring on an eclipse, which the "
            "people drove off by beating drums and gongs. Chen's jibe is that Liu "
            "Peichu had better have played the Heavenly Dog and swallowed the "
            "Communists at a gulp than raise such windy slogans."
        ),
    },
    {
        "anchor": "suffocated to death in the Great Tunnel",
        "note": (
            "The Great Tunnel disaster (大隧道) at Chongqing, 5 June 1941, when a "
            "great crowd sheltering from a long Japanese night raid in a rock "
            "air-raid tunnel suffocated in the crush and the foul air. Estimates of "
            "the dead ranged from about a thousand to several thousand. Luo Jing's "
            "memoir, quoted here, dates it to the fifth month, close to the event."
        ),
    },
    {
        "anchor": "April First assembly",
        "note": (
            "April the first (四一) was kept by the service as its founding "
            "anniversary, marking the establishment in 1932 of the Special "
            "Services Department under Dai Li, the nucleus of what became the "
            "Juntong. The 'April First assembly' was its yearly commemoration at "
            "the Chongqing headquarters, and the 'April First Library' one of the "
            "institutions named for the day."
        ),
    },
]


def to_ncr(s):
    return "".join(ch if ord(ch) < 128 else "&#%d;" % ord(ch) for ch in s)


def main():
    for e in NOTES:
        assert e["anchor"] in reading, "anchor not in reading: %r" % e["anchor"]
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
