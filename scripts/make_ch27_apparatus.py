# Build data/ch27_apparatus.json for apparatus_merge.py.
# Note bodies authored as plain ASCII + typed hanzi + numeric-entity punctuation,
# then every non-ASCII char (the typed hanzi) is converted to a numeric character
# reference before writing. EVERY non-ASCII glyph used in any note body is asserted
# to occur in the authoritative data/zh/ch27.txt (a Write-tool corruption would
# produce a glyph absent from the source and trip the assert). Anchors are ASCII
# substrings of out/ch27_reading.md, with no em dash and no quote/apostrophe.
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZH = open(os.path.join(ROOT, "data", "zh", "ch27.txt"), encoding="utf-8").read()

notes = {
    "ch27": [
        {
            "anchor": "the August Thirteenth Incident",
            "note": (
                "The &#8220;August Thirteenth Incident&#8221; (八一三事变) was the "
                "outbreak, on 13 August 1937, of full-scale fighting between Chinese "
                "and Japanese forces in Shanghai&#8212;the great clash of the war after "
                "the Marco Polo Bridge Incident that July. The three-month Battle of "
                "Shanghai that followed ended in the Chinese city&#8217;s fall, leaving "
                "the foreign concessions as an unoccupied enclave&#8212;the &#8220;"
                "Solitary Island&#8221; of these years."
            ),
        },
        {
            "anchor": "French Municipal Council",
            "note": (
                "Chen is untangling the names of the two concessions&#8217; governing "
                "bodies. The International Settlement was run by the Shanghai Municipal "
                "Council (工部局, Gongbuju); the French Concession by a separate council, "
                "the Conseil d&#8217;administration municipale, in Chinese 公董局 "
                "(Gongdongju), here &#8220;the French Municipal Council.&#8221; The "
                "newspaper&#8217;s 公部局 (Gongbuju written with a wrong first character) "
                "was simply an error. Zhang Xiaolin&#8217;s seat on the French body marks "
                "how far a Green Gang tycoon had risen into the concession&#8217;s "
                "official establishment."
            ),
        },
        {
            "anchor": "the Reformed Government was set up",
            "note": (
                "The Reformed Government (维新政府) was the Japanese-sponsored puppet "
                "regime set up at Nanjing in March 1938 under Liang Hongzhi, with Chen "
                "Qun among its officials, to administer occupied central China. In 1940 "
                "it was folded into Wang Jingwei&#8217;s larger Nanjing &#8220;National "
                "Government.&#8221; Its founding is the moment at which, in the forger&#8217;s "
                "telling, Zhang Xiaolin threw in his lot with the collaborators."
            ),
        },
        {
            "anchor": "there are eighteen points",
            "note": (
                "The lead-in says eighteen, but Chen then numbers his rebuttal (1) "
                "through (19), and closes the section by calling them &#8220;these "
                "nineteen points.&#8221; The &#8220;eighteen&#8221; here is a slip for "
                "nineteen, faithfully preserved."
            ),
        },
        {
            "anchor": "among the Japanese commanders",
            "note": (
                "The forged letter has Zhang meeting Japanese generals named 长奇 "
                "(Changqi) and 松井 (Matsui). Chen&#8217;s point turns on a homophone: "
                "there is no Japanese surname read Changqi (长奇), but 长崎&#8212;identical "
                "in Mandarin sound (Ch&#225;ngq&#237;) and read Nagasaki in Japanese&#8212;is "
                "a real Japanese place- and family-name. The garbled 长奇 betrays a "
                "writer inventing &#8220;enemy generals&#8221; he could not name, one of "
                "Chen&#8217;s grounds for calling the whole letter a forgery."
            ),
        },
        {
            "anchor": "Zhou Fohai the prime mover",
            "note": (
                "Zhou Fohai (周佛海, 1897&#8211;1948), once a founding member of the "
                "Chinese Communist Party and later a senior Nationalist, became the "
                "chief financial architect of Wang Jingwei&#8217;s regime. The "
                "&#8220;Central Reserve Bank&#8221; (中央储备银行), which he set up in "
                "January 1941, issued the puppet regime&#8217;s own currency to drive "
                "the Nationalist fabi out of the occupied zone. The &#8220;Special "
                "District Court&#8221; (特区法院) was the Chinese court that had exercised "
                "jurisdiction over Chinese within the Shanghai concessions; its seizure "
                "stripped away the last organ of Nationalist legal authority there."
            ),
        },
    ]
}


def to_ncr(s):
    return "".join(ch if ord(ch) < 128 else "&#%d;" % ord(ch) for ch in s)


allow = set("—–‘’“”")  # em/en dash, curly quotes (converted, not asserted)
for items in notes.values():
    for e in items:
        for ch in e["note"]:
            if ord(ch) < 128 or ch in allow:
                continue
            assert ch in ZH, "GLYPH NOT IN data/zh (possible mangling): %r U+%04X" % (ch, ord(ch))
        e["note"] = to_ncr(e["note"])
        e["anchor"] = to_ncr(e["anchor"])
        assert e["anchor"].isascii(), e["anchor"]

path = os.path.join(ROOT, "data", "ch27_apparatus.json")
json.dump({"notes": notes}, open(path, "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("wrote", path, "with", len(notes["ch27"]), "notes; all glyphs verified in data/zh")
