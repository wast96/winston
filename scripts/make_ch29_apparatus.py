# Build data/ch29_apparatus.json for apparatus_merge.py.
# Note bodies authored as plain ASCII + typed hanzi, then every non-ASCII char (the
# typed hanzi, any em-dash) is converted to a numeric character reference before
# writing. EVERY non-ASCII hanzi glyph used in any note body is asserted to occur in
# the authoritative data/zh/ch29.txt (a Write-tool corruption would produce a glyph
# absent from the source and trip the assert). Anchors are ASCII substrings of
# out/ch29_reading.md, with no em dash and no quote/apostrophe.
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZH = open(os.path.join(ROOT, "data", "zh", "ch29.txt"), encoding="utf-8").read()
READING = open(os.path.join(ROOT, "out", "ch29_reading.md"), encoding="utf-8").read()

notes = {
    "ch29": [
        {
            "anchor": "the great Changsha fire",
            "note": (
                "The great Changsha fire (长沙大火) of 12 November 1938, later "
                "remembered as the Wenxi Fire. On a false report that Japanese "
                "troops were about to enter the city, Nationalist forces set it "
                "ablaze under a scorched-earth order; the fire burned for days, "
                "destroyed much of Changsha, and killed thousands of its people. "
                "Chiang Kai-shek had the officials who had botched the execution of "
                "the order tried and shot. Here it fixes the date of Liu Yuanshen's "
                "dispatch to Shanghai."
            ),
        },
        {
            "anchor": "the Linli class",
            "note": (
                "The Linli class was the Juntong's special training class held from "
                "1938 at Linli in Hunan (the source prints the place as 临沣). Chiang "
                "Kai-shek was its nominal principal (校长) and Dai Li its class "
                "director (班主任) — the relationship Liu invokes just below. It "
                "trained many of the operatives the service sent into occupied China."
            ),
        },
        {
            "anchor": "the Advanced Education Class",
            "note": (
                "The Advanced Education Class (高等教育班) of the Central Military "
                "Academy (中央军校), then at Chengdu, was an advanced course for "
                "serving officers; to be sent to it was a mark of favor and a step "
                "toward promotion. Giving it up, as Liu Yuanshen does here, is the "
                "hinge of the whole chapter."
            ),
        },
        {
            "anchor": "Xiaozhilong",
            "note": (
                "Xiaozhilong (消治龙) was a Chinese trade name for one of the early "
                "sulfonamide (sulfa) antibacterials that reached China in the late "
                "1930s. Before penicillin these were the first drugs effective "
                "against bacterial infections such as pneumonia, though, as here, "
                "often too late to save an advanced case."
            ),
        },
        {
            "anchor": "Little Red Devil",
            "note": (
                "Little Red Devils (红小鬼) were the boy soldiers and orderlies of "
                "the Chinese Communist forces. Ruijin (瑞金) in Jiangxi was the "
                "capital of the Communists' Central Soviet base from 1931 until the "
                "Long March began in 1934. Liu means that Liu Quande had grown up "
                "within the Communist movement before he came over to the "
                "Nationalist side."
            ),
        },
        {
            "anchor": "tiger bench",
            "note": (
                "The tiger bench (老虎凳) was a standard torture: the victim was "
                "seated with his legs bound flat along a bench and bricks forced one "
                "by one under his heels, bending the knees backward until the joints "
                "and tendons tore. It was notorious at the puppet Special Operations "
                "Headquarters at No. 76."
            ),
        },
        {
            "anchor": "South China Evening News",
            "note": (
                "The South China Evening News (南华晚报) was Wang Jingwei's "
                "Chinese-language organ at Hong Kong, launched in 1939 under Lin "
                "Bosheng to argue the case for a negotiated peace with Japan. Xu "
                "Liqiu, the sanction target Zhou Xiyuan dangles here, was its "
                "director."
            ),
        },
        {
            "anchor": "dead before the campaign was won",
            "note": (
                "The phrase 出师未捷身先死 (roughly, dead before the campaign was "
                "won) is from Du Fu's poem on Zhuge Liang, the great strategist of "
                "the Three Kingdoms who died on campaign before his aim was "
                "achieved. Liu applies it to the young classmates killed on crossing "
                "into occupied territory, before they could strike a single blow."
            ),
        },
        {
            "anchor": "State Express 555",
            "note": (
                "Garrick (茄力克) and State Express 555 (三五) were premium British "
                "cigarettes sold in tins; both were among the costlier imported "
                "brands in the Shanghai of the day, a small token of standing."
            ),
        },
    ],
}


def to_ncr(s):
    out = []
    for ch in s:
        if ord(ch) < 128:
            out.append(ch)
        else:
            out.append("&#%d;" % ord(ch))
    return "".join(out)


def main():
    for cid, items in notes.items():
        for e in items:
            # assert the anchor is a verbatim ASCII substring of the reading
            assert e["anchor"] in READING, "anchor not in reading: %r" % e["anchor"]
            for ch in e["anchor"]:
                assert ord(ch) < 128, "anchor has non-ASCII: %r" % e["anchor"]
                assert ch not in "—\"'‘’“”", \
                    "anchor has a forbidden char: %r" % e["anchor"]
            # assert every non-ASCII glyph in the body occurs in the source
            for ch in e["note"]:
                if ord(ch) >= 128 and ch != "—":
                    assert ch in ZH, "note glyph not in data/zh/ch29.txt: %r" % ch
            e["note"] = to_ncr(e["note"])
    dest = os.path.join(ROOT, "data", "ch29_apparatus.json")
    json.dump({"notes": notes}, open(dest, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print("wrote %s (%d notes)" % (dest, len(notes["ch29"])))


if __name__ == "__main__":
    main()
