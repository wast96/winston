# Build data/ch24_apparatus.json for apparatus_merge.py.
# Note bodies authored as plain ASCII + typed hanzi, then every non-ASCII char
# is converted to a numeric character reference before writing. To defeat the
# CJK-mangling hazard (see HANDOFF), EVERY non-ASCII glyph used in any note body
# is asserted to occur in the authoritative data/zh/ch24.txt: a Write-tool
# corruption would produce a glyph absent from the source and trip the assert.
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZH = open(os.path.join(ROOT, "data", "zh", "ch24.txt"), encoding="utf-8").read()

notes = {
    "ch24": [
        {
            "anchor": "Lao Bosheng, chief of the political section",
            "note": (
                "The political section (政治科) of the Shanghai Municipal Police "
                "was its Special Branch, the political-intelligence arm of the "
                "British-run police of the International Settlement and the chief "
                "adversary anatomized in this chapter. &#8220;Lao Bosheng&#8221; "
                "(劳勃生) is the Chinese transliteration of a Western&#8212;probably "
                "British&#8212;surname (something on the order of Robertson or "
                "Robinson); Chen gives only the Chinese form, and the officer&#8217;s "
                "original name and identity cannot be fixed with certainty. The "
                "eighth-section chief he names next, &#8220;Kelaideng,&#8221; is a "
                "transliteration of the same uncertain kind."
            ),
        },
        {
            "anchor": "give his applause to Xin Yanqiu",
            "note": (
                "Xin Yanqiu (新艳秋) was a celebrated actress of the dan, or female, "
                "roles in Peking opera, famed as a leading exponent of the Cheng "
                "Yanqiu style. The pieces named in the rival accounts that follow "
                "&#8212;&#8220;Yutangchun,&#8221; &#8220;A Snowy Night at Xiaoshang "
                "River&#8221; (the death of the Song general Yang Zaixing), and "
                "&#8220;Tiaohuache&#8221; (Gao Chong storming the war-carts)&#8212;are "
                "all staples of the Peking-opera repertoire. Chen sets the three side "
                "by side to show how witnesses to a single night could each &#8220;see"
                "&#8221; a different play."
            ),
        },
        {
            "anchor": "from page seven of the Shanghai Shenbao",
            "note": (
                "The Shenbao (申报), founded at Shanghai in 1872, was for decades "
                "China&#8217;s foremost daily and its paper of record. It is to be "
                "distinguished from the occupation-era Xin Shen Bao (新申报) noted "
                "earlier&#8212;a separate wartime sheet under Japanese and "
                "collaborationist control; the Shenbao report Chen reproduces here is "
                "a straight piece of news from the morning after the killing."
            ),
        },
        {
            "anchor": "belonging to the Tama Force",
            "note": (
                "By the account of Chen&#8217;s informant, a former gendarmerie "
                "officer, the &#8220;Tama Force&#8221; (多摩部队) and its &#8220;Gyoku "
                "Unit&#8221; (玉部队) belonged to the Japanese army&#8217;s secret "
                "research into poisons and chemical and biological agents&#8212;the "
                "same field of activity as the notorious Unit 731 in Manchuria, which "
                "used prisoners as human subjects."
            ),
        },
        {
            "anchor": "doctrine of the three nots",
            "note": (
                "Wu Peifu (吴佩孚, 1874&#8211;1939) was one of the most powerful "
                "warlords of the early Republic. He was celebrated for a personal "
                "code he styled the &#8220;three nots&#8221; (三不主义); the exact "
                "three are reported variously, but they center on his refusal to "
                "take refuge in the foreign concessions, to borrow foreign money, "
                "and to hoard private wealth. Living to his principles, he spurned "
                "every Japanese overture to head a puppet government after 1937, and "
                "died at Beiping in 1939."
            ),
        },
        {
            "anchor": "a man surnamed Yuan and named Shu",
            "note": (
                "Yuan Shu (袁殊, 1911&#8211;1987), the journalist here dismissed by "
                "Chen as a source of little worth, was in fact one of the most "
                "remarkable double agents of the age&#8212;the so-called &#8220;"
                "five-faced spy,&#8221; who at various times drew pay from the "
                "Nationalist Juntong and Zhongtong, from the Japanese, and from the "
                "Wang puppet regime, while serving throughout as an agent of the "
                "Chinese Communist Party. Chen&#8217;s suspicion, set down here, "
                "proved exactly right."
            ),
        },
    ]
}


def to_ncr(s):
    return "".join(ch if ord(ch) < 128 else "&#%d;" % ord(ch) for ch in s)


# Per-glyph verification against the authoritative source before converting.
allow = set("—–‘’“”")  # em/en dash, curly quotes
for items in notes.values():
    for e in items:
        for ch in e["note"]:
            if ord(ch) < 128 or ch in allow:
                continue
            assert ch in ZH, "GLYPH NOT IN data/zh (possible mangling): %r U+%04X" % (ch, ord(ch))
        e["note"] = to_ncr(e["note"])
        e["anchor"] = to_ncr(e["anchor"])
        assert e["anchor"].isascii(), e["anchor"]

path = os.path.join(ROOT, "data", "ch24_apparatus.json")
json.dump({"notes": notes}, open(path, "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("wrote", path, "with", len(notes["ch24"]), "notes; all glyphs verified in data/zh")
