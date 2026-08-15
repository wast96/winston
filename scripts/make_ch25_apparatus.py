# Build data/ch25_apparatus.json for apparatus_merge.py.
# Note bodies authored as plain ASCII + typed hanzi, then every non-ASCII char
# is converted to a numeric character reference before writing. To defeat the
# CJK-mangling hazard (see HANDOFF), EVERY non-ASCII glyph used in any note body
# is asserted to occur in the authoritative data/zh/ch25.txt: a Write-tool
# corruption would produce a glyph absent from the source and trip the assert.
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZH = open(os.path.join(ROOT, "data", "zh", "ch25.txt"), encoding="utf-8").read()

notes = {
    "ch25": [
        {
            "anchor": "Comrade Qin Qirong",
            "note": (
                "Qin Qirong (秦启荣) was a Nationalist guerrilla commander in "
                "Shandong, a graduate of the sixth class of the Whampoa Military "
                "Academy (黄埔) and a Juntong man. Through the war years he raised "
                "and led anti-Japanese and anti-Communist irregulars in the "
                "province, and was killed in 1943. The demolition brigade and the "
                "Qingdao action group of Dai Li&#8217;s directive were part of this "
                "Shandong work."
            ),
        },
        {
            "anchor": "twenty thousand yuan a day",
            "note": (
                "The directive as reproduced reads &#8220;a day&#8221; (每日); but "
                "the writer&#8217;s own reckoning just below, which works out each "
                "man&#8217;s pay from a monthly sum of twenty thousand, and item "
                "7&#8217;s grant of two months&#8217; funds, both treat the sum as "
                "monthly (每月). The figure is rendered as the source prints it; the "
                "discrepancy is the source&#8217;s own."
            ),
        },
        {
            "anchor": "Mr. Mao Renfeng",
            "note": (
                "Mao Renfeng (毛人凤, 1897&#8211;1956) was Dai Li&#8217;s fellow "
                "townsman and closest lieutenant, long the effective administrator "
                "of the Juntong under him. After Dai&#8217;s death in an air crash "
                "in 1946 he rose to head the organization and the secret services "
                "that grew out of it, following the Nationalist government to Taiwan."
            ),
        },
        {
            "anchor": "the firewood from under the cauldron",
            "note": (
                "&#8220;To draw the firewood from under the cauldron&#8221; "
                "(釜底抽薪) is a classical idiom for striking at the root of a "
                "trouble rather than its symptoms&#8212;taking the fuel away instead "
                "of trying to stop the water boiling. Dai Li applies it to the "
                "sanction of Wang Jingwei himself, and Chen takes up the figure in "
                "the next breath."
            ),
        },
        {
            "anchor": "the Sihang Warehouse",
            "note": (
                "The Sihang Warehouse (四行仓库), the &#8220;Four Banks&#8217; "
                "Warehouse&#8221; on the north bank of Suzhou Creek, was the site of "
                "the celebrated last stand of a battalion of the 88th Division&#8212;"
                "the &#8220;Eight Hundred Heroes&#8221;&#8212;covering the Chinese "
                "retreat from Shanghai in late October 1937. After withdrawing into "
                "the International Settlement the survivors were disarmed and held "
                "for years in an interned &#8220;lone battalion&#8221; camp; it is "
                "these detained men, and others held in the French Concession, that "
                "Dai Li&#8217;s telegram proposes to reach."
            ),
        },
        {
            "anchor": "pidgin",
            "note": (
                "&#8220;Pidgin English&#8221; renders yangjingbang English&#8212;the "
                "source prints the homophone 洋经滨 for the usual name. The "
                "Yangjingbang was a creek that once ran between the International "
                "Settlement and the French Concession at Shanghai; the makeshift "
                "trade-tongue spoken along it lent its name to broken commercial "
                "English, the word &#8220;pidgin&#8221; itself being thought a "
                "Chinese-inflected rendering of &#8220;business.&#8221;"
            ),
        },
        {
            "anchor": "Pan Hannian",
            "note": (
                "Pan Hannian (潘汉年, 1906&#8211;1977) was the Chinese Communist "
                "Party&#8217;s foremost intelligence officer in occupied Shanghai, "
                "working through the very seams among the Nationalist, Japanese, and "
                "Wang-puppet services that Chen describes; he is known to have met "
                "Wang Jingwei and to have dealt with Li Shiqun of No. 76. Purged "
                "after 1949 on charges arising from those wartime contacts, he was "
                "posthumously rehabilitated. The &#8220;Jiangsu Provincial "
                "Committee&#8221; Chen lists was the Party&#8217;s underground "
                "leadership for the Shanghai region."
            ),
        },
        {
            "anchor": "his father-in-law",
            "note": (
                "The word Chen uses is laotaishan (老泰山), literally &#8220;Old "
                "Mount Tai,&#8221; a familiar and respectful colloquial term for "
                "one&#8217;s wife&#8217;s father. It plays, by chance, against the "
                "classical figure of Mount Tai that closes the chapter."
            ),
        },
        {
            "anchor": "xieke huang",
            "note": (
                "Xieke huang (蟹壳黄), literally &#8220;crab-shell yellow,&#8221; is "
                "a small round Shanghai pastry of flaky, layered dough, brushed with "
                "sesame and baked crisp and golden&#8212;so named for its color and "
                "its hard, ridged &#8220;shell.&#8221; It is eaten hot from the oven, "
                "as here, and may be either savory (scallion, as Chen smells it) or "
                "sweet."
            ),
        },
        {
            "anchor": "heavier than Mount Tai",
            "note": (
                "The words are Sima Qian&#8217;s, from his &#8220;Letter in Answer "
                "to Ren An&#8221; (first century B.C.): a man has but one death, and "
                "it may be weightier than Mount Tai (泰山) or lighter than a swan&#8217;s "
                "feather (鸿毛)&#8212;it lies in the use to which he turns it. The "
                "saying became proverbial for weighing a death by its worth; Chen "
                "invokes it only to set his nameless comrades apart, whose deaths "
                "answered to no such reckoning. It furnishes, too, the title of the "
                "chapter that follows."
            ),
        },
    ]
}


def to_ncr(s):
    return "".join(ch if ord(ch) < 128 else "&#%d;" % ord(ch) for ch in s)


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

path = os.path.join(ROOT, "data", "ch25_apparatus.json")
json.dump({"notes": notes}, open(path, "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("wrote", path, "with", len(notes["ch25"]), "notes; all glyphs verified in data/zh")
