#!/usr/bin/env python3
"""Assemble the EDITORIAL-note batch (roman stream, "ed": true) for ch15, ch16,
and ch17, under CLAUDE.md's generous density model and the STYLE.local rulings
(marker lands ON the glossed term; verdict tag only where a claim is weighed;
one subject one note; a note never restates the body or re-underlines its irony;
no competing translation of a term the body renders; a significance claim scoped;
identify a quoted eyewitness by placement PLUS vantage; pinyin gloss inline once
per named Chinese figure; a book-specific proper name takes the body's own
capitalization; no re-noting a subject an earlier-reading unit already covers).
Anchors are verbatim unique substrings of out/<id>_reading.md; the builder
numbers the stream in lowercase roman by anchor position.

These three chapters close the revolution's defeat, and most of their cast was
placed in an earlier-reading unit, so the new-note count stays modest. NOT
re-noted here (already placed earlier; cross-reference only): Feng Yu-hsiang
(ch04 -- his person; the Chengchow/Hsuchow CONFERENCES are new and noted here),
General Galen/Bluecher (Isaacs's own author asterisk identifies him), the
Kuomintang, the Comintern/E.C.C.I., the CCP, Chiang Kai-shek, Wang Ching-wei,
Chen Tu-hsiu, Borodin, Chow En-lai, Chiu Chiu-pei (ch07 editorial; promoted to
principal this batch but not re-noted), Chang Kuo-tao (ch02/03), Tang Sheng-chih
(ch06), Tang Ping-shan (ch06), Teng Yen-ta / Eugene Chen / Soong Ching-ling
(ch05/11), M. N. Roy (ch02), Lozovsky (author notes), Peng Pai (ch03), Li
Chi-sen (ch05), Chu Pei-teh (ch14), the Northern Expedition, the "Ironsides"/
Fourth Army (ch06), Whampoa, the Green Gang's Mechanics'-Union kin, Yeh Ting
(ch12), Chen Shao-yu = Wang Min (Isaacs's own author asterisk identifies him),
the Paris Commune (ch02 -- the man Galliffet is glossed here), the three Russian
revolutions and the Bolsheviks/Mensheviks (ch00b), the bloc of four classes,
Sun Yat-sen's Three People's Principles (ch03).

Deliberately left to the skip tier (minor one-off actors and sources the body
contexts inline, named in PROGRESS): Yu Yu-jen, Tang Leang-li, Yang Yu-ting,
the Pan-Pacific Trade Union Secretariat; Liu Wei-han / Lo Mai (body glosses the
alias and gives his role), Hua Kang (a source, body-contexted), Chang Fao-cheng,
Tzo Fung-chi, Hwang Che-hsiang, Li Fu-lin, Hsueh Yoh, Huang Ping, Huang Mo-sung,
Deng Cheng-tsah, Chen Shao-yu-the-participant.

Writes scratch/ch1517_editorial_notes.json for apparatus_merge.py.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- ch15 "The Wuhan Debacle" ----
CH15 = [
    ("waited for “der Tag.”",
     "<i>Der Tag</i> is German for &#8220;The Day&#8221; &#8212; the awaited day "
     "of decisive action. The phrase carried an ironic charge between the wars as "
     "the toast the pre-1914 German officer corps was said to raise to the coming "
     "day of war."),
    ("summoned to Chengchow for a conference on June 12",
     "Chengchow (Zhengzhou), the capital of Honan and the crossing of the "
     "north&#8211;south and east&#8211;west trunk railways, and Hsuchow (Xuzhou), "
     "the next great rail junction eastward, were the sites of Feng&#8217;s two "
     "conferences of June 1927: with the Wuhan leaders at Chengchow (June "
     "10&#8211;12) and with Chiang Kai-shek at Hsuchow (June 19&#8211;21). They "
     "are usually taken as the point at which Feng&#8217;s weight settled behind "
     "Nanking."),
    ("like Lochinvar out of his western stronghold",
     "Lochinvar is the dashing young hero of a ballad in Sir Walter Scott&#8217;s "
     "<i>Marmion</i> (1808), who rides &#8220;out of the west&#8221; to carry off "
     "his bride from under her kinsmen&#8217;s noses &#8212; proverbial for a "
     "gallant rescuer arriving in the nick of time."),
    ("Chang Hsueh-liang, the young son of Chang Tso-lin",
     "Chang Hsueh-liang (Zhang Xueliang, 1901&#8211;2001), the &#8220;Young "
     "Marshal,&#8221; who succeeded his assassinated father as master of "
     "Manchuria in 1928. In December 1936 he seized Chiang Kai-shek at Sian (the "
     "Sian Incident) to force a united front against Japan, and then spent most "
     "of the next half-century under Nationalist house arrest."),
    ("Chang Fah-kwei, commander of the “Ironsides,”",
     "Chang Fah-kwei (Zhang Fakui, 1896&#8211;1980), the &#8220;Ironsides&#8221; "
     "commander whose Fourth Army had spearheaded the Northern Expedition. His "
     "falling-out that autumn with Li Chi-sen over the control of Canton opened "
     "the split the Communists tried to exploit in the December rising."),
    ("Chang Kuo-tao, Li Li-san",
     "Li Li-san (Li Lisan, 1899&#8211;1967), a leading labor organizer of the "
     "party. He directed the Chinese Communist Party in 1928&#8211;30, and the "
     "&#8220;Li Lisan line&#8221; of 1930 &#8212; a drive to take the cities by "
     "insurrection &#8212; ended in fresh disaster and his removal."),
    ("On July 15 the Kuomintang Political Council ordered all Communist members",
     "This order of July 15, 1927 is the Wuhan split &#8212; the formal break "
     "between Wang Ching-wei&#8217;s government and the Communists that ended the "
     "alliance of the Kuomintang and the Communist Party (the &#8220;first united "
     "front&#8221;). Begun as a &#8220;peaceful&#8221; separation, unlike "
     "Chiang&#8217;s April 12 bloodletting, it became within days the terror the "
     "rest of the chapter describes."),
]

# ---- ch16 "Autumn Harvest" ----
CH16 = [
    ("the “July Days” of the Bolsheviks in 1917",
     "The July Days were the half-spontaneous armed demonstrations in Petrograd "
     "in July 1917 that the Bolsheviks were blamed for and that brought a wave of "
     "repression down on them &#8212; months before their victory in October. "
     "Stalin&#8217;s analogy cast the 1927 defeat as a like setback soon to be "
     "reversed."),
    ("hastily convened on August 7",
     "The emergency conference of the party&#8217;s leaders at Hankow on August "
     "7, 1927, remembered in Chinese Communist history simply as the August 7 "
     "Conference. It is the point at which Chiu Chiu-pei replaced Chen Tu-hsiu at "
     "the head of the party."),
    ("at once for the GPU",
     "The GPU (later the OGPU) was the Soviet state political police &#8212; the "
     "secret-police organ that succeeded Lenin&#8217;s Cheka and was later folded "
     "into the NKVD."),
    ("by its new representative (Lominadze)",
     "Besso (Vissarion) Lominadze (1897&#8211;1935), the young Georgian Bolshevik "
     "Moscow sent to replace Borodin and Roy. He presided over the August 7 "
     "conference and drove the turn to insurrection; caught up in the "
     "intra-party struggles at home, he took his own life as arrest closed "
     "in."),
    ("occurred at Nanchang, capital of Kiangsi province, on August 1",
     "The Nanchang rising of August 1, 1927 was the first armed action the "
     "Communists mounted on their own against the Kuomintang. Though it failed "
     "and its forces were driven south, the date is kept in China as the founding "
     "day of the Red Army (later the People&#8217;s Liberation Army) and is still "
     "marked as Army Day."),
    ("Two Communist officers, Yeh Ting and Ho Lung",
     "Ho Lung (He Long, 1896&#8211;1969), a Hunanese former bandit chief who had "
     "risen to command a Nationalist army and now brought it over to the "
     "Communists at Nanchang. He became one of the ten marshals of the "
     "People&#8217;s Liberation Army in 1955 and died persecuted in the Cultural "
     "Revolution."),
    ("Chow En-lai, Chang Tai-lei",
     "Chang Tai-lei (Zhang Tailei, 1898&#8211;1927), a founder of the Communist "
     "Youth League. Within months he would head the Canton rising of December and "
     "be killed in it &#8212; the highest-ranking Communist to die in the "
     "insurrections of 1927."),
    ("known as the “Autumn Harvest Uprisings.”",
     "The scattered peasant-and-worker risings of September 1927 in Hunan, Hupeh, "
     "and Kiangsi, ordered by the August 7 line. Mao Tse-tung led the one in "
     "Hunan; when it failed to take Changsha he pulled its survivors back into "
     "the Chingkang mountains &#8212; the beginning of the rural base areas and "
     "the strategy of encircling the cities from the countryside."),
]

# ---- ch17 "The Canton Commune" ----
CH17 = [
    ("formally established itself in the police headquarters",
     "The insurrection of December 11&#8211;13, 1927 is the Canton Commune, or "
     "Guangzhou Uprising &#8212; remembered by the name of the Paris Commune of "
     "1871. The last of the risings ordered from Moscow after the Wuhan collapse, "
     "it held much of the city for barely three days before the Kuomintang "
     "generals retook it."),
    ("the adventurer, Heinz Neumann, who had now arrived in Canton",
     "Heinz Neumann (1902&#8211;1937), a young German Communist and Reichstag "
     "deputy sent by Stalin as Comintern agent to direct the Canton rising. He "
     "was shot in Moscow, a victim of the Great Purge."),
    ("this peasant rising in Hailufeng",
     "Hailufeng is the pair of districts Haifeng and Lufeng, on the East River "
     "coast, where Peng Pai had built the earliest peasant unions. The peasant "
     "&#8220;soviet&#8221; set up there in November 1927 is usually reckoned the "
     "first soviet on Chinese soil; it was crushed early in 1928."),
    ("Not until the Chinese Gallifets set to work",
     "Gaston de Galliffet (1830&#8211;1909) was the French general remembered for "
     "the ferocity with which he put down the Paris Commune of 1871, shooting "
     "captured Communards in droves &#8212; his name a byword for the butchery of "
     "a beaten revolution."),
]


def main():
    reading = {c: open(os.path.join(ROOT, "out", "%s_reading.md" % c),
                       encoding="utf-8").read()
               for c in ("ch15", "ch16", "ch17")}
    batch = {"notes": {}}
    for chid, spec in (("ch15", CH15), ("ch16", CH16), ("ch17", CH17)):
        notes = []
        for anchor, body in spec:
            n = reading[chid].count(anchor)
            if n != 1:
                sys.exit("%s: anchor %r occurs %d times (need 1)"
                         % (chid, anchor, n))
            notes.append({"anchor": anchor, "note": body, "ed": True})
        batch["notes"][chid] = notes
        print("%s: %d editorial notes" % (chid, len(notes)))

    dest = os.path.join(ROOT, "scratch")
    os.makedirs(dest, exist_ok=True)
    path = os.path.join(dest, "ch1517_editorial_notes.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("wrote", path)


if __name__ == "__main__":
    main()
