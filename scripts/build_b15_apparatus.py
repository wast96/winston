#!/usr/bin/env python3
"""Build the B15 apparatus file (ch69-ch71 back-matter notes). Anchors stay
literal Unicode (verbatim, UNIQUE substrings of the reading files, no embedded
straight quotes/apostrophes); note bodies have every non-ASCII character encoded
to a numeric character reference. <i> tags are ASCII and pass through."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def enc(s):
    return "".join(c if ord(c) < 128 else "&#%d;" % ord(c) for c in s)


# (unit, anchor, body-in-plain-unicode)
NOTES = [
    # ── ch69 あとがき / Afterword (Shiba) ──
    ("ch69", "just on a hundred years now",
     "Shiba reckons from Hijikata’s death in 1869 (Meiji 2); “just on a "
     "hundred years” places the writing of this afterword about 1969. The "
     "novel itself had been serialized earlier, in 1962–64; this short piece "
     "was added to a later edition and is carried forward in the 2020 new "
     "edition translated here."),
    ("ch69", "At about four shaku up",
     "A <i>shaku</i> is about 30.3 centimeters, so four <i>shaku</i> is "
     "roughly 1.2 meters — about the height at which a boy would brace his "
     "hands against the post. The amber sheen is the polish of Toshizō’s grip "
     "over years of wrestling practice against it."),
    ("ch69", "a great central pillar",
     "The <i>daikokubashira</i>, the thick central post of a traditional "
     "farmhouse: its chief structural support and, by extension, the "
     "“mainstay” of the household. It takes its name from Daikoku, the god of "
     "wealth and the kitchen."),
    ("ch69", "In the garden grows arrow-bamboo",
     "<i>Yadake</i> (<i>Pseudosasa japonica</i>), the straight, slender bamboo "
     "whose culms were cut for arrow shafts. It was planted at samurai "
     "residences as a token of martial readiness, which is why a farmer’s son "
     "who planted it was announcing an ambition above his birth."),
    ("ch69", "the brow-plate of a helmet",
     "The <i>hachigane</i>, an iron brow-band worn tied around the head, or "
     "under a hood, as light armor. The sword-cut on it is a relic of "
     "Hijikata’s fighting. The piece survives, with the Kanesada sword, at the "
     "Ishida birth-house, today the Hijikata Toshizō Museum; the sword the "
     "afterword names is the same Izumi-no-kami Kanesada blade carried south "
     "from Hakodate in the errand of the closing chapters. Corroborated."),
    ("ch69", "the family trade of gathering it",
     "The Hijikata family of Ishida made and sold a folk medicine, the “Ishida "
     "powder” (<i>Ishida sanyaku</i>), a remedy for bruises and wounds "
     "compounded from a wayside herb gathered on the gravel beds of the "
     "Asakawa; Toshizō hawked it about the villages in his youth. That the boy "
     "who mixed and distributed it should later organize the Shinsengumi is "
     "Shiba’s point in these closing paragraphs. Well attested; corroborated."),

    # ── ch70 解説 / Commentary (Harada Masato) ──
    ("ch70", "the invented figure of Kurama Tengu",
     "Kurama Tengu, the masked swordsman-hero of Osaragi Jirō’s enormously "
     "popular novels and their many film versions — a wholly fictional "
     "champion of the imperial cause in the last shogunal years. Harada’s "
     "point is that as a boy he preferred the real, historical Katsura to this "
     "invented hero."),
    ("ch70", "the beautiful Gion geisha Ikumatsu",
     "Ikumatsu, the Gion <i>geiko</i> who sheltered the hunted Katsura Kogorō "
     "and afterward became his wife, known after the Restoration as Kido "
     "Matsuko. Theirs is among the best-loved romances of the period; "
     "corroborated."),
    ("ch70", "which I read later",
     "<i>Shinsengumi Keppūroku</i> (“Chronicle of the Shinsengumi”), Shiba’s "
     "other major Shinsengumi book: a set of linked short stories published "
     "just after <i>Moeyo ken</i>, taking the corps as a whole rather than "
     "Hijikata alone for its subject."),
    ("ch70", "were program-pictures",
     "A “program picture” was the studios’ term for a formula B-feature turned "
     "out on a fixed schedule to fill out a double bill — the opposite of a "
     "prestige production. Harada’s complaint is that the 1960s screen "
     "versions of Shiba were of this routine kind."),
    ("ch70", "Shimozawa Kan",
     "Shimozawa Kan (1892–1968), the writer whose documentary-style "
     "Shinsengumi chronicles — the <i>Shinsengumi Shimatsuki</i> and its "
     "companion volumes, gathered from survivors and their descendants — are "
     "the factual bedrock beneath most later Shinsengumi fiction, Shiba’s "
     "included."),
    ("ch70", "party of ten made for the Ikedaya",
     "Here Harada draws on present-day scholarship. The raid was made by a "
     "small party: Kondō with about ten men entered the Ikedaya, while "
     "Hijikata’s larger body was searching other inns nearby and came up only "
     "after the fighting had begun. The novel’s neater version — two parties "
     "sent against two separately reported targets — is the dramatized "
     "“popular account.” The affair had been touched off by the arrest of the "
     "loyalist arms-dealer Furutaka Shuntarō, tortured into revealing the plot "
     "(see the Ikedaya chapters). Broadly corroborated."),
    ("ch70", "She is a created character",
     "This passage, by the director of the 2020 film, is the plain statement "
     "on which the footnotes to this translation have relied: Oyuki is "
     "fiction. There was no historical Oyuki; the whole thread — the "
     "painting-master’s widow, the Shimabara nights, the Hakodate reunion, the "
     "temple offering at the close — is Shiba’s invention. Harada adds that "
     "Shiba seems to have drawn on the story of his own courtship of his wife "
     "(Fukuda Midori). Shiba’s own afterword, the preceding chapter, speaks "
     "only of Hijikata and does not mention her, so it is Harada’s commentary "
     "here that is the surviving testimony to the point. Corroborated."),
    ("ch70", "cruelty pictures",
     "<i>Zankokue</i>, “atrocity pictures” — a lurid vein of late-Edo and "
     "Meiji woodblock art depicting torture, murder, and battlefield death, of "
     "which the “bloody prints” (<i>muzan-e</i>) of Tsukioka Yoshitoshi are "
     "the best known. This turn is Harada’s addition for the film; in the "
     "novel Oyuki paints in the Shijō-Maruyama manner."),
    ("ch70", "the Shijō-Maruyama school",
     "The Shijō-Maruyama school of painting, founded in eighteenth-century "
     "Kyoto by Maruyama Ōkyo and carried on by Matsumura Goshun, prized "
     "naturalistic observation drawn from life. In the novel it is the art "
     "Oyuki had come from Edo to Kyoto to study."),
    ("ch70", "a figure named Honda Kakuan",
     "Honda Kakuan, a physician of Hino said to have taught the young Hijikata "
     "his letters; the name recurs in the diary Hijikata kept. Harada links "
     "him to Watanabe Kazan (1793–1841), the samurai-painter and "
     "Western-studies scholar broken in the 1839 “Prison of the "
     "Barbarian-Studies Group” (<i>Bansha no goku</i>) for urging that the "
     "country open itself. Kazan died before Hijikata was six, so any "
     "connection is one of ideas, not acquaintance; the claim is Harada’s."),
    ("ch70", "The white peony",
     "One of Hijikata’s own haiku, from the manuscript verse-collection he "
     "left under his <i>haigō</i> (haiku name) Hōgyoku: <i>hakubotan / tsukiyo "
     "tsukiyo ni / somete hoshi</i> (“white peony — I would have it dyed by "
     "the moonlit nights, night on moonlit night”). The sense of the last line "
     "is debated. That the swordsman of the Shinsengumi also wrote verse is "
     "one of the book’s recurring notes."),
    ("ch70", "the French army officer Brunet",
     "Four foreign eyewitnesses of the period, whose images Harada took as "
     "reference: Wilhelm Heine, the German-American artist who came with "
     "Perry; Charles Wirgman, the British illustrator and founder of the "
     "<i>Japan Punch</i>; Jules Brunet, the French artillery officer who "
     "resigned his commission to fight alongside Enomoto in the Ezo republic — "
     "that is, in the very campaign this novel closes with; and Felice Beato, "
     "the pioneering photographer of Yokohama. Corroborated."),
    ("ch70", "War Minister Anami Korechika",
     "Anami Korechika (1887–1945), the Army Minister who resisted surrender to "
     "the end and took his own life on 15 August 1945; he is the central "
     "figure of Harada’s <i>Japan’s Longest Day</i>. He completes Harada’s "
     "trio of “beautiful losers” at the turning points — Ishida Mitsunari of "
     "Sekigahara, Hijikata of the Boshin War, Anami of 1945. Corroborated."),
    ("ch70", "opens on 22 May 2020",
     "The date given here is from the 2020 edition, and was the film’s "
     "original release schedule. The COVID-19 pandemic forced a postponement "
     "of more than a year; Harada’s <i>Moeyo ken</i>, with Okada Jun’ichi as "
     "Hijikata, finally opened in Japan on 15 October 2021. Corroborated."),

    # ── ch71 司馬遼太郎 / About the Author ──
    ("ch71", "Shiba Ryōtarō was born in the city of",
     "“Shiba Ryōtarō” is a pen name; the author was born Fukuda Teiichi "
     "(1923–1996). He took the name in homage to the Chinese historian Sima "
     "Qian (in Japanese, Shiba Sen), author of the <i>Records of the Grand "
     "Historian</i>, reading it as “a man (Tarō) who falls far (<i>ryō</i>) "
     "short of Shiba [Sen]” — a scholar’s modest bow to the master of "
     "historical narrative. Corroborated."),
    ("ch71", "In Shōwa 35 (1960)",
     "Japanese years are counted by imperial era: Taishō (1912–26), Shōwa "
     "(1926–89), and Heisei (1989–2019). Thus Shōwa 35 is 1960, and the "
     "author’s Taishō 12 is 1923. The bracketed Western years throughout this "
     "notice are supplied by the translator; the source dates the birth and "
     "death in both systems and the prizes by era-year alone."),
    ("ch71", "the 42nd Naoki Prize",
     "The Naoki Prize, Japan’s foremost award for popular fiction, given "
     "twice a year since 1935 to a rising or mid-career writer; it made "
     "Shiba’s name. He took the 42nd, for <i>Fukurō no shiro</i> (“The Castle "
     "of the Owl”), in 1960. Corroborated."),
    ("ch71", "Order of Culture",
     "The Order of Culture (<i>Bunka-kunshō</i>), Japan’s highest honor for "
     "achievement in the arts and sciences, conferred by the Emperor each 3 "
     "November; the “Person of Cultural Merit” (<i>bunka kōrōsha</i>) named "
     "just before is the standing distinction that ordinarily precedes it. "
     "Corroborated."),
]


def main():
    out = {"notes": {}}
    for unit, anchor, body in NOTES:
        out["notes"].setdefault(unit, []).append(
            {"anchor": anchor, "note": enc(body)})
    dest = os.path.join(ROOT, "out", "b15_apparatus.json")
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    total = sum(len(v) for v in out["notes"].values())
    print("wrote %s (%d notes across %d units)"
          % (dest, total, len(out["notes"])))


if __name__ == "__main__":
    main()
