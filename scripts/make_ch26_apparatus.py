# Build data/ch26_apparatus.json for apparatus_merge.py.
# Note bodies authored as plain ASCII + typed hanzi + curly punctuation, then
# every non-ASCII char is converted to a numeric character reference before
# writing. EVERY non-ASCII glyph used in any note body is asserted to occur in
# the authoritative data/zh/ch26.txt (a Write-tool corruption would produce a
# glyph absent from the source and trip the assert). Anchors are ASCII
# substrings of out/ch26_reading.md, with no em dash and no quote/apostrophe.
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZH = open(os.path.join(ROOT, "data", "zh", "ch26.txt"), encoding="utf-8").read()

notes = {
    "ch26": [
        {
            "anchor": "Mr. Yu Qiaqing",
            "note": (
                "Yu Qiaqing (虞洽卿, 1867&#8211;1945) was one of the great civic "
                "figures of Republican Shanghai: a Ningbo-born comprador who rose "
                "to lead the Shanghai General Chamber of Commerce, gave his name to "
                "a central thoroughfare (Yu Ya Ching Road), and stood close to the "
                "Green Gang bosses. It was his prestige, not any labor experience, "
                "that Dai Li wanted to lend the workers&#8217; committee&#8212;which "
                "is why Chen doubts the whole scheme."
            ),
        },
        {
            "anchor": "Shao Lizi",
            "note": (
                "Shao Lizi (邵力子, 1882&#8211;1967), a veteran Nationalist "
                "statesman, newspaper editor, and educator, later served as "
                "ambassador to the Soviet Union and as a government negotiator with "
                "the Communists; after 1949 he remained on the mainland."
            ),
        },
        {
            "anchor": "Zhang Aiping",
            "note": (
                "Chen&#8217;s parenthetical is borne out: Zhang Aiping (张爱萍, "
                "1910&#8211;2003) did become a senior general of the People&#8217;s "
                "Liberation Army and served as the People&#8217;s Republic&#8217;s "
                "minister of national defense from 1982 to 1988. Zhang Zhiyi (张执一, "
                "1911&#8211;1983), author of the memoir Chen quotes, was a Communist "
                "united-front operative who rose to be a deputy head of the "
                "Party&#8217;s Central United Front Work Department&#8212;so his own "
                "account of infiltrating the Loyal and Patriotic Army is, as Chen "
                "reads it, a confession as much as a boast."
            ),
        },
        {
            "anchor": "the highest man of the Japanese side",
            "note": (
                "The source paragraphs that open this section are badly garbled in "
                "the original ebook&#8212;nearly every character miscut&#8212;and are "
                "here rendered to their evident sense, which the clean parallel "
                "passages below (the tally table and the detailed gendarmerie "
                "account) fully corroborate. One slip in the garbled text is left "
                "visible: it credits the sanction of Akagi to the "
                "&#8220;Second Action Brigade&#8221; (第二行动大队), whereas both the "
                "captured tally and the gendarmerie&#8217;s own record assign it to "
                "Jiang Anhua&#8217;s Third Action Brigade (第三行动大队), and name "
                "Li Liang as the director on the spot."
            ),
        },
        {
            "anchor": "I set out here in outline",
            "note": (
                "The dates in the tally that follows are given in the source&#8217;s "
                "Republican-calendar form, year/month/day: &#8220;29/9/29&#8221; is "
                "the 29th day of the 9th month of the 29th year of the Republic, i.e. "
                "29 September 1940, and &#8220;30/10/22&#8221; is 22 October 1941. "
                "Two entries carry an &#8220;xx&#8221; where a place-name character "
                "was redacted in the source; these are shown as a blank."
            ),
        },
        {
            "anchor": "seeking benevolence and finding it",
            "note": (
                "An allusion to the Analects (VII.15): asked whether the ancient "
                "worthies Bo Yi and Shu Qi, who starved rather than serve a house "
                "they held unrighteous, had any regret, Confucius answered, "
                "&#8220;They sought benevolence and got it (求仁得仁)&#8212;what was "
                "there to regret?&#8221; The phrase marks a death freely chosen for "
                "what one holds right, so that it is beyond pity."
            ),
        },
        {
            "anchor": "I made an elegiac couplet to mourn him",
            "note": (
                "A wanlian (挽联) is a paired funeral scroll: two balanced lines of "
                "equal length, hung at a mourning, that answer each other phrase for "
                "phrase. Xu Wenqi&#8217;s couplet sets the dead man&#8217;s loyalty "
                "to the state in its first (upper) line against his filial and "
                "brotherly duty to an aged mother and young sisters in its second, "
                "each line closing on the writer&#8217;s own grief at surviving him. "
                "Rendered here as a single run of prose, since the two halves must "
                "stand as one line for the paragraph count."
            ),
        },
        {
            "anchor": "Ruby Queen",
            "note": (
                "Ruby Queen (红锡包) was a cheap and hugely popular cigarette of "
                "British-American Tobacco in Republican China. The &#8220;Great "
                "Britain brand&#8221; (大英牌) that Shanghai people called it, and the "
                "northern nickname &#8220;Fenbao&#8221; (粉包), name the same packet, "
                "whose thin printed wrapper the martyr uses to shield a photograph."
            ),
        },
        {
            "anchor": "Ward Road Gaol",
            "note": (
                "Ward Road Gaol (提篮桥监狱), the great prison in the Hongkou "
                "district run by the Shanghai Municipal Council, was then reckoned "
                "the largest prison in the Far East."
            ),
        },
        {
            "anchor": "Gunfire on the Solitary Island",
            "note": (
                "&#8220;The Solitary Island&#8221; (孤岛) was the name for the "
                "foreign concessions of Shanghai in the span between the fall of the "
                "surrounding Chinese districts in November 1937 and Japan&#8217;s "
                "seizure of the settlements after Pearl Harbor in December 1941: an "
                "unoccupied enclave ringed by occupied territory, and the ground on "
                "which the whole underground war of this chapter was fought."
            ),
        },
        {
            "anchor": "lantern-parade celebration rallies",
            "note": (
                "On 1 July 1941 Germany, Italy, and several Axis and Axis-aligned "
                "states extended diplomatic recognition to Wang Jingwei&#8217;s "
                "Nanjing regime. The &#8220;lantern-parade celebration rallies&#8221; "
                "(提灯游行庆祝大会) were the puppet government&#8217;s public "
                "festivities marking it&#8212;which is why the Kang Corps set out to "
                "bomb the one at Jessfield Park."
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

path = os.path.join(ROOT, "data", "ch26_apparatus.json")
json.dump({"notes": notes}, open(path, "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("wrote", path, "with", len(notes["ch26"]), "notes; all glyphs verified in data/zh")
