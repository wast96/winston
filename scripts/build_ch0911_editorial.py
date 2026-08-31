#!/usr/bin/env python3
"""Assemble the EDITORIAL-note batch (roman stream, "ed": true) for ch09, ch10,
and ch11, under CLAUDE.md's generous density model and the STYLE.local rulings
(marker lands ON the glossed term; verdict tag only where a claim is weighed;
one subject one note; a note never restates the body or re-underlines its irony;
no competing translation of a term the body renders; a significance claim scoped;
a quoted eyewitness identified by placement and stopped; pinyin gloss inline once
per named Chinese figure; no re-noting a subject an earlier-reading unit already
covers). Anchors are verbatim unique substrings of out/<id>_reading.md; the
builder numbers the stream in lowercase roman by anchor position.

These three chapters carry a large cast, but nearly all of it was introduced at
its first appearance in an EARLIER-reading unit, so the new-note count is small
(the density tapers as recurring furniture is already placed, exactly as the
model predicts). NOT re-noted here (already placed earlier; cross-reference
only): the Kuomintang, the Comintern/E.C.C.I. and its Seventh Plenum, the CCP,
Sun Yat-sen, Chiang Kai-shek, Borodin, Chen Tu-hsiu, Trotsky, Lenin, Stalin,
Bukharin, Wang Ching-wei, the "bloc of four classes" (ch00b), the Comintern
delegation Earl Browder / Tom Mann / Jacques Doriot (ch05), M. N. Roy (ch02,
the Second Congress colonial theses), Li Ta-chao (ch03), Li Chi-sen (ch05), the
Western Hills group (ch04), Wu Chih-hui and Chang Ching-chiang (ch07/earlier),
Yu Ya-ching, the Green Gang and its bosses Hwang Ching-yung / Tu Yueh-sen (ch04),
the Northern Expedition, May Thirtieth, Chang Tso-lin, Feng Yu-hsiang (ch04),
Tang Sheng-chih (ch06), Eugene Chen (ch05/06), Teng Yen-ta and Liao Chung-kai
(ch05/earlier), the Paris Commune (ch02), the Society of December 10 and the
<i>Eighteenth Brumaire</i> (ch08), Louis Fischer (ch03), George Sokolsky
(ch05/08), Anna Louise Strong's book <i>China's Millions</i> (author-note
citation, ch11 -- SHE is identified here). Isaacs's April 5 "squeezed lemon"
speech being unpublished is already covered by his OWN author note (ch09), so no
editorial note repeats it.

Deliberately left to the glossary / unnoted (minor one-off actors, named as a
skip tier in PROGRESS): Sydor Stoler, Chen Tsang-shen, General Chang Chun,
Soumei Cheng, Francis Zia, K. P. Chen, Wang Hsiao-lai, Wang Han-liang, Lin Chun,
Hsin Ting-yu, Ku Chen-chung, Chen Chuen, Chang Siao-ling, Wang Shao-hua, Victor
Stern, Chitarov, Louis Fischer's second appearance.

Writes scratch/ch0911_editorial_notes.json for apparatus_merge.py.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- ch09 "The Conspiracy of Silence" ----
CH09 = [
    ("Martinov, the Menshevik",
     "Alexander Martynov (1865&#8211;1935), for two decades a leading Menshevik "
     "theorist, who came over to the Bolsheviks in 1923 and served as a "
     "Comintern publicist. His articles supplied much of the &#8220;theoretical&#8221; "
     "justification for the very China policy Isaacs is dissecting."),
    ("the “Chinese Pilsudski”",
     "J&#243;zef Pi&#322;sudski (1867&#8211;1935), the Polish socialist "
     "revolutionary who, after leading Poland to independence, seized power in a "
     "military coup in May 1926 and ruled as an authoritarian nationalist. "
     "Trotsky&#8217;s point is the arc from left-wing national revolutionary to "
     "right-wing dictator &#8212; the road he expected Chiang to travel faster."),
    ("Malraux’s Kyo",
     "Andr&#233; Malraux (1901&#8211;1976), the French novelist and later De "
     "Gaulle&#8217;s minister of culture. His <i>Man&#8217;s Fate</i> "
     "(<i>La Condition humaine</i>, 1933), which won the Prix Goncourt, is set "
     "in the Shanghai of these very weeks; Kyo Gisors, invoked here, is its "
     "Communist protagonist. Isaacs draws on the novel&#8217;s scenes as a kind "
     "of eyewitness to the insurrection."),
]

# ---- ch10 "The Coup of April 12, 1927" ----
CH10 = [
    ("The Workers’ Trade Alliance, freshly organized",
     "A scab union got up under Green Gang and Kuomintang direction to replace "
     "the Communist-led General Labor Union the gangsters had just helped "
     "destroy. It took over the shattered labor movement and enrolled the "
     "workers in the name of the San Min Principles. (corroborated)"),
    ("the new Nanking government",
     "Chiang Kai-shek&#8217;s rival Nationalist government, proclaimed at Nanking "
     "on April 18, 1927, six days after the coup, against the existing "
     "left-Kuomintang government at Wuhan. The rivalry of these &#8220;two "
     "governments,&#8221; Nanking and Wuhan, shapes the chapters that follow."),
    ("Yung Chung-chin",
     "Yung Chung-chin (Rong Zongjing, 1873&#8211;1938), the cotton-and-flour "
     "magnate of Wusih and the foremost Chinese industrialist of the day. His "
     "arrest for balking at Chiang&#8217;s forced loan, recounted here, is well "
     "attested. (corroborated)"),
    ("Ernst Thaelmann",
     "Ernst Th&#228;lmann (1886&#8211;1944), chairman of the German Communist "
     "Party from 1925 and a staunch Comintern loyalist. The Moscow-directed "
     "refusal to unite with the Social Democrats against the Nazis is what "
     "Isaacs means by handing the party over &#8220;to the Nazi "
     "executioners&#8221;; Th&#228;lmann himself was arrested in 1933 and shot "
     "at Buchenwald in 1944."),
    ("Walter Duranty",
     "Walter Duranty (1884&#8211;1957), the <i>New York Times</i>&#8217;s Moscow "
     "correspondent, who won a Pulitzer Prize in 1932 and is now remembered "
     "chiefly for dispatches that minimized Stalin&#8217;s repressions and "
     "denied the Soviet famine. Isaacs cites his forecast because it proved "
     "right."),
    ("Fuge, tace, quiesce!",
     "Latin, &#8220;Flee, be silent, keep still&#8221; &#8212; the counsel the "
     "desert hermit St. Arsenius gave himself. The whole passage is Marx "
     "quoting his own <i>Eighteenth Brumaire of Louis Bonaparte</i>, where the "
     "bourgeoisie is told the same thing, and then told it again by Bonaparte."),
]

# ---- ch11 "Wuhan: 'The Revolutionary Center'" ----
CH11 = [
    ("Sun Fo",
     "Sun Fo (Sun Ke, 1891&#8211;1973), Sun Yat-sen&#8217;s only son, "
     "American-educated and a former mayor of Canton, later president of the "
     "Legislative Yuan. The nickname his colleagues gave him, &#8220;Sun "
     "Wu-kung,&#8221; is that of the Monkey King of the classic novel "
     "<i>Journey to the West</i>, who somersaults thousands of miles in a "
     "single bound &#8212; a play on their shared surname, Sun, that mocked his "
     "sudden changes of front."),
    ("George Hsu-chien",
     "George Hsu-chien (Xu Qian, 1871&#8211;1940), a Christian and Western-trained "
     "jurist, twice minister of justice, and one of the Wuhan government&#8217;s "
     "Left Kuomintang leaders. Hunted after the Wuhan collapse, he withdrew from "
     "politics to Hong Kong in the autumn of 1927."),
    ("Ku Meng-yu",
     "Ku Meng-yu (Gu Mengyu, 1889&#8211;1972), a German-trained economist and "
     "dean at Peking University who headed the Kuomintang&#8217;s propaganda "
     "department at Wuhan. He backed Wang Ching-wei&#8217;s July 1927 break with "
     "the Communists and later led an anti-Communist &#8220;Third Force&#8221; in "
     "exile."),
    ("Soong Ching-ling",
     "Soong Ching-ling (Song Qingling, 1893&#8211;1981), Sun Yat-sen&#8217;s young "
     "widow and a mainstay of the Kuomintang left, who broke with Chiang&#8217;s "
     "Nanking regime and, long afterward, served as a vice-chair of the "
     "People&#8217;s Republic of China."),
    ("Anna Louise Strong",
     "Anna Louise Strong (1885&#8211;1970), an American journalist and one of the "
     "few Western eyewitnesses inside the Wuhan camp &#8212; a lifelong "
     "sympathizer first with the Soviet Union and then with the Chinese "
     "Communists. Her Wuhan reporting is what Isaacs quotes for Borodin&#8217;s "
     "parable."),
    ("the Eighth Plenum of the Executive Committee of the Communist International",
     "The Eighth Enlarged Plenum of the E.C.C.I. met in Moscow, May 18&#8211;30, "
     "1927. It was the Opposition&#8217;s last platform inside the International: "
     "Trotsky and the Yugoslav Communist Vujovi&#263; spoke there against the "
     "China policy and were formally condemned."),
]


def main():
    reading = {c: open(os.path.join(ROOT, "out", "%s_reading.md" % c),
                       encoding="utf-8").read()
               for c in ("ch09", "ch10", "ch11")}
    batch = {"notes": {}}
    for chid, spec in (("ch09", CH09), ("ch10", CH10), ("ch11", CH11)):
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
    path = os.path.join(dest, "ch0911_editorial_notes.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("wrote", path)


if __name__ == "__main__":
    main()
