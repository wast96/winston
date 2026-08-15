# Build data/ch28_apparatus.json for apparatus_merge.py.
# Note bodies authored as plain ASCII + typed hanzi + literal em-dashes, then every
# non-ASCII char (the typed hanzi, the em-dash) is converted to a numeric character
# reference before writing. EVERY non-ASCII hanzi glyph used in any note body is
# asserted to occur in the authoritative data/zh/ch28.txt (a Write-tool corruption
# would produce a glyph absent from the source and trip the assert). Anchors are
# ASCII substrings of out/ch28_reading.md, with no em dash and no quote/apostrophe.
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZH = open(os.path.join(ROOT, "data", "zh", "ch28.txt"), encoding="utf-8").read()

notes = {
    "ch28": [
        {
            "anchor": "by Cao Song",
            "note": (
                "The line 一将功成万骨枯 — \"one general's fame is built on ten "
                "thousand rotting bones\" — closes a quatrain, \"The Year Jihai\" "
                "(己亥岁), by the late-Tang poet Cao Song (曹松). It laments that a "
                "commander's glory is bought with the lives of countless common "
                "soldiers; the taboo Chen describes is a fighting organization's "
                "reluctance to dwell on so disenchanting a thought."
            ),
        },
        {
            "anchor": "The Double Tenth",
            "note": (
                "The Double Tenth (双十节), 10 October, is the national day of the "
                "Republic of China, marking the Wuchang Uprising of 1911 that "
                "touched off the revolution against the Qing dynasty. In occupied "
                "Shanghai it could not be openly celebrated. Fu Xiao'an was killed "
                "the morning after."
            ),
        },
        {
            "anchor": "Great Way City Government",
            "note": (
                "The \"Great Way City Government\" (大道市政府, Dadao Shizhengfu) was "
                "the first Japanese puppet municipality of Shanghai, proclaimed at the "
                "end of 1937 after the city fell; the name invokes the classical ideal "
                "of \"the great way.\" It was soon folded into the Reformed Government's "
                "Shanghai administration. Su Xiwen headed it before Fu Xiao'an."
            ),
        },
        {
            "anchor": "the Mixed Court",
            "note": (
                "The Mixed Court (会审公廨) was the tribunal, established in the 1860s, "
                "that tried Chinese residents of the Shanghai concessions; foreign "
                "\"assessors\" sat beside the Chinese magistrate and came to dominate "
                "it, a standing affront to Chinese sovereignty. The two agreements Chen "
                "reproduces record its abolition and replacement — in 1930 for the "
                "International Settlement and 1931 for the French Concession — by "
                "Chinese-run Special District Courts, the very courts the puppet regime "
                "was now moving to seize."
            ),
        },
        {
            "anchor": "concurrently governor of the",
            "note": (
                "Not to be confused with the Wang regime's Central Reserve Bank "
                "(中央储备银行) at Nanjing: the Federal Reserve Bank of China "
                "(联合准备银行) was the note-issuing bank of the earlier North China "
                "puppet government at Beiping, set up in 1938 with Wang Shiying as "
                "governor. Its Tianjin general manager, Cheng Xigeng (程锡庚), was "
                "assassinated by the Kang Corps in 1939, as Chen recounts just below."
            ),
        },
        {
            "anchor": "Yue opera",
            "note": (
                "Yue opera (越剧), also called Shaoxing opera (绍兴戏) for its home "
                "region in Zhejiang, is a form of Chinese sung drama that by the 1930s "
                "was hugely popular in Shanghai. The piece named, 盘夫索夫 "
                "(\"Interrogating the Husband, Demanding the Husband\"), and its star "
                "Yao Shuijuan (姚水娟) were then at the height of their vogue."
            ),
        },
        {
            "anchor": "drove the carriage for Yang Xiuqiong",
            "note": (
                "Yang Xiuqiong (杨秀琼) was a celebrated swimming champion of 1930s "
                "China, feted as a national beauty. That Chu Minyi (褚民谊) — a senior "
                "figure of the Wang regime — was remembered for driving her carriage "
                "was a byword for his vanity and his courting of celebrity; Chen names "
                "him by the jibe rather than the office."
            ),
        },
        {
            "anchor": "still but a scene from",
            "note": (
                "\"Officialdom Unmasked\" (官场现形记), by Li Baojia (Li Boyuan), is a "
                "celebrated satirical novel of the late Qing, a serial exposure of the "
                "venality and buffoonery of the imperial bureaucracy. To call the "
                "puppets' scramble over the mayoralty a scene from it is to cast them "
                "as stock grotesques of that satire."
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

path = os.path.join(ROOT, "data", "ch28_apparatus.json")
json.dump({"notes": notes}, open(path, "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("wrote", path, "with", len(notes["ch28"]), "notes; all glyphs verified in data/zh")
