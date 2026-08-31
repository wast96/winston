#!/usr/bin/env python3
"""Assemble the EDITORIAL-note batch (roman stream, "ed": true) for ch12, ch13,
and ch14, under CLAUDE.md's generous density model and the STYLE.local rulings
(marker lands ON the glossed term; verdict tag only where a claim is weighed;
one subject one note; a note never restates the body or re-underlines its irony;
no competing translation of a term the body renders; a significance claim scoped;
a quoted eyewitness identified by placement PLUS vantage, minus both duplications;
pinyin gloss inline once per named Chinese figure; a book-specific proper name
takes the body's own capitalization; no re-noting a subject an earlier-reading
unit already covers). Anchors are verbatim unique substrings of out/<id>_reading.md;
the builder numbers the stream in lowercase roman by anchor position.

These three chapters are heavily built of quoted documents (Stalin, Trotsky, the
ECCI resolutions) and their large cast was almost all introduced in an
EARLIER-reading unit, so the new-note count stays modest. NOT re-noted here
(already placed earlier; cross-reference only): the Kuomintang, the Comintern/
E.C.C.I. and its plenums, the CCP, Sun Yat-sen, Chiang Kai-shek, Borodin, Chen
Tu-hsiu, Wang Ching-wei, Trotsky, Lenin, Stalin, Bukharin (ch00b), M. N. Roy
(ch02, the Second Congress colonial theses -- his Fifth Congress role and the
June telegram he showed Wang are body narrative), Feng Yu-hsiang (ch04 -- his
Chengchow/Hsuchow conferences arrive in ch15), Tang Sheng-chih (ch06), Eugene
Chen (ch05/06), the Northern Expedition, May Thirtieth, Chang Tso-lin, the Green
Gang, the bloc of four classes, the Three People's Principles (ch03), Confucius
(ch01), Mif and Chiu Chiu-pei and Tang Ping-shan (ch06), Browder/Doriot/Mann
(ch05), Lozovsky (Profintern, ch-earlier author notes), the Paris Commune. The
author-note citations to Chapman, Treint, Hicks and Citrine are bibliographic;
the PERSONS Chapman and Treint are identified here without repeating those
citations' titles.

Deliberately left to the glossary / unnoted (minor one-off actors and terms,
named as a skip tier in PROGRESS): Chen Cheng (a one-line body mention), Yang
Sen, Yu Hsueh-chung, Hsia To-yen, Chang Lien-sen, Jen Hsu, Tu Cheng-tsu, the Red
Spears and the Min Tuan / lien pao / tuchun / tangpu terms the body glosses
inline, Andreyev Hall.

Writes scratch/ch1214_editorial_notes.json for apparatus_merge.py.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- ch12 "The 'Revolutionary Center' at Work" ----
CH12 = [
    ("Coué school of revolutionary politics",
     "&#201;mile Cou&#233; (1857&#8211;1926), the French pharmacist who popularized "
     "healing by &#8220;optimistic autosuggestion,&#8221; taught through a formula "
     "repeated daily: <i>Every day, in every way, I am getting better and "
     "better</i>."),
    ("Baron Tanaka",
     "Baron Tanaka Giichi (1864&#8211;1929), the army general who became prime "
     "minister of Japan on April 20, 1927. He is identified with a harder, more "
     "interventionist line toward China than the cabinet he replaced."),
    ("Sir Austen Chamberlain, the foreign secretary",
     "Sir Austen Chamberlain (1863&#8211;1937), who was British foreign secretary "
     "throughout the 1924&#8211;29 Conservative government and directed its policy "
     "toward China."),
    ("the Arcos raid",
     "The London police raid of May 12, 1927 on Arcos Ltd., the Soviet trade "
     "delegation&#8217;s premises, mounted to recover an allegedly stolen "
     "military document. It turned up little, but served the Baldwin government "
     "as the pretext for the rupture with Moscow."),
    ("the Kuomintang leader, Tan Yen-kai",
     "Tan Yen-kai (Tan Yankai, 1880&#8211;1930), a Hunanese elder of the "
     "Kuomintang and chairman of the Nationalist government &#8212; first at "
     "Wuhan, then, after the party split healed, at Nanking, where he headed the "
     "Executive Yuan until his death."),
    ("Yen Hsi-shan",
     "Yen Hsi-shan (Yan Xishan, 1883&#8211;1960), the warlord who ruled Shansi "
     "province as its &#8220;model governor&#8221; from 1911 and joined the "
     "Northern Expedition in 1927. He held Shansi almost without a break until "
     "1949, then followed the Nationalists to Taiwan."),
    ("Hsiang Chung-fah, Communist secretary of the General Labor Union",
     "Hsiang Chung-fah (Xiang Zhongfa, 1880&#8211;1931), a Hupeh boatmen&#8217;s "
     "and labor organizer who in 1928 became the nominal general secretary of the "
     "Chinese Communist Party &#8212; the highest party office in name, though "
     "real authority lay elsewhere."),
    ("Yeh Ting, a Communist officer",
     "Yeh Ting (Ye Ting, 1896&#8211;1946), a Communist commander of the Northern "
     "Expedition who would go on to lead the Nanchang uprising and the Canton "
     "Commune later in 1927."),
    ("the opening of the Fifth Congress of the Chinese Communist Party in Hankow on April 27",
     "The Fifth Congress of the Chinese Communist Party met at Hankow (one of "
     "the three cities that make up Wuhan) from April 27 to May 9, 1927, in the "
     "weeks after Chiang&#8217;s Shanghai coup; it re-elected Chen Tu-hsiu "
     "general secretary."),
    ("de l’audace, de l’audace, encore de l’audace.",
     "The words echo Georges Danton (1759&#8211;1794), whose call to the French "
     "Assembly on September 2, 1792, as the Prussians advanced on Paris, is "
     "remembered as <i>de l&#8217;audace, encore de l&#8217;audace, toujours de "
     "l&#8217;audace</i> &#8212; &#8220;boldness, more boldness, always "
     "boldness.&#8221; Danton himself went to the guillotine in 1794."),
    ("a son or brother in a Sam Browne belt",
     "A Sam Browne belt &#8212; the leather waist belt with a diagonal strap "
     "over the shoulder &#8212; was the mark of a commissioned officer; &#8220;a "
     "son or brother in a Sam Browne belt&#8221; means a relative holding an "
     "army commission."),
]

# ---- ch13 "The Struggle for the Land" ----
CH13 = [
    ("the *tuhao*—the local bullies",
     "The peasant movement&#8217;s signature village slogan was <i>da dao tuhao "
     "lieshen</i>, &#8220;down with the local tyrants and evil gentry.&#8221; The "
     "<i>tuhao</i> are the rural strongmen; the <i>haosen</i> (properly "
     "<i>haoshen</i>) Isaacs names through the chapter are the powerful gentry "
     "&#8212; the same class the slogan targets."),
    ("writes Chapman",
     "H. Owen Chapman, a British doctor living in Hankow through the Wuhan "
     "months; his 1928 book, written from inside the Nationalist capital, is a "
     "hostile eyewitness record of the period that Isaacs quotes throughout these "
     "chapters."),
    ("General Hsu Keh-chang, commander of the local garrison",
     "General Hsu Keh-chang (Xu Kexiang, 1890&#8211;1964), who led this Changsha "
     "coup of May 21, 1927. It is remembered as the Horse Day Incident (<i>Ma Ri "
     "Shibian</i>): in the telegraphic code then used to abbreviate dates, the "
     "21st of a month was written with the character <i>ma</i>, "
     "&#8220;horse.&#8221;"),
    ("Ho Chien, who was due to hold the province in fief",
     "Ho Chien (He Jian, 1887&#8211;1956), a Hunanese general who became the "
     "province&#8217;s military governor after this terror and stayed a byword "
     "for anti-Communist ferocity; in 1930 his provincial regime executed Mao "
     "Tse-tung&#8217;s wife, Yang Kai-hui. He later followed the Nationalists to "
     "Taiwan."),
    ("Hsu Chao-jen, the Canton trade union leader",
     "Hsu Chao-jen (Su Zhaozheng, 1885&#8211;1929), a seamen&#8217;s-union leader "
     "of the 1922 Hong Kong strike and the Canton&#8211;Hong Kong strike of "
     "1925&#8211;26, and chairman of the All-China Federation of Trade Unions. As "
     "Wuhan&#8217;s minister of labor he was among the first Communists to hold "
     "government office; he died in 1929."),
    ("the Five Classics and the Four Books",
     "The core of the old Confucian curriculum every examination candidate "
     "mastered: the Four Books (the <i>Analects</i>, the <i>Mencius</i>, and two "
     "chapters drawn from the <i>Book of Rites</i>) and the Five Classics (the "
     "classics of Odes, Documents, Changes, and Rites, and the <i>Spring and "
     "Autumn Annals</i>)."),
]

# ---- ch14 "Moscow and Wuhan" ----
CH14 = [
    ("the Anglo-Russian Trade Union Unity Committee",
     "A joint body of Soviet and British T.U.C. leaders set up in 1925, which "
     "Stalin prized as a lever against the British government. Its British "
     "members &#8212; A. A. Purcell, George Hicks, and Walter Citrine &#8212; "
     "held back during the 1926 General Strike and after; the committee collapsed "
     "in 1927, as the Opposition had long said it would."),
    ("Enrich yourselves!",
     "Bukharin&#8217;s 1925 exhortation to the peasants to grow prosperous under "
     "the New Economic Policy. The Opposition denounced it as a surrender to "
     "capitalism in the villages, and it was later turned against Bukharin "
     "himself."),
    ("Albert Treint, than a member of the presidium of the Executive Committee",
     "Albert Treint (1889&#8211;1971), a former general secretary of the French "
     "Communist Party who had led its &#8220;Bolshevization&#8221; and the purge "
     "of its Trotskyists. By 1927 he was himself moving toward the Opposition, "
     "and was expelled in January 1928 &#8212; which is what makes his inside "
     "account of the plenum Stalin tried to conceal worth weighing."),
    ("Ercoli of Italy",
     "&#8220;Ercoli&#8221; was the Comintern pseudonym of Palmiro Togliatti "
     "(1893&#8211;1964), who would lead the Italian Communist Party from 1927 "
     "until his death and become the commanding figure of postwar Italian "
     "communism."),
    ("General Chu Pei-teh, who held Kiangsi province",
     "Chu Pei-teh (Zhu Peide, 1888&#8211;1937), the Yunnanese general commanding "
     "the Third Army and governing Kiangsi. His purge of the Communists there was "
     "comparatively bloodless &#8212; he had them escorted out of the province "
     "rather than shot."),
]


def main():
    reading = {c: open(os.path.join(ROOT, "out", "%s_reading.md" % c),
                       encoding="utf-8").read()
               for c in ("ch12", "ch13", "ch14")}
    batch = {"notes": {}}
    for chid, spec in (("ch12", CH12), ("ch13", CH13), ("ch14", CH14)):
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
    path = os.path.join(dest, "ch1214_editorial_notes.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("wrote", path)


if __name__ == "__main__":
    main()
