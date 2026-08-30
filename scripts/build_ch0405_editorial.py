#!/usr/bin/env python3
"""Assemble the EDITORIAL-note batch (roman stream, "ed": true) for ch04 and
ch05, under CLAUDE.md's generous density model and the STYLE.local rulings
(marker lands ON the glossed term; verdict tag only where a claim is weighed;
one subject one note; no re-noting a subject an earlier-reading unit already
covers; no printed-folio parentheticals; a note is never vaguer than its text;
each note tested against the whole paragraph it sits in; pinyin gloss inline
once per named Chinese figure). Anchors are verbatim unique substrings of
out/<id>_reading.md; the builder numbers the stream in lowercase roman by
anchor position.

NOT re-noted here (already placed in an earlier-reading unit; cross-reference
only): the Kuomintang, the Comintern/E.C.C.I. body, the CCP, Sun Yat-sen,
Chiang Kai-shek, Borodin, Wang Ching-wei, Chen Tu-hsiu, Trotsky, Lenin, Stalin,
Bukharin, the compradores, the 1911 revolution, Yuan Shih-kai, the Whampoa
Academy, the May Thirtieth movement, the Canton-Hong Kong strike, Shameen,
Shakee, Chang Tso-lin, Wu Pei-fu, Tai Chi-tao, Liao Chung-kai, Chen
Chiung-ming, the Washington Conference, extraterritoriality, the Northern
Expedition, the 1905 Russian revolution, likin, hsien, Tuan Chi-jui (identified
in ch03's Anfu-clique note and in Isaacs's own ch05 footnote), Louis Fischer.

Writes scratch/ch0405_editorial_notes.json for apparatus_merge.py.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- ch04 "Canton: To Whom the Power?" ----
CH04 = [
    ("the Western Hills Conference group",
     "At this meeting, held at the Biyun Temple by Sun Yat-sen&#8217;s coffin, "
     "right-wing Kuomintang leaders resolved to expel the Communists from the "
     "party and to dismiss Borodin. The group became the organized right-wing "
     "opposition to the Canton leadership."),
    ("took the name “Sun Yat-senist Society.”",
     "The Sun Yat-senist Society (Sun Wen zhuyi xuehui), founded in 1925, was a "
     "right-wing anti-Communist body organized chiefly among the Whampoa "
     "cadets and younger party members. It claimed to guard Sun&#8217;s "
     "doctrine against Communist &#8220;adulteration&#8221; and served Chiang "
     "and the right as a lever against Communist influence in the army."),
    ("of Feng Yu-hsiang",
     "Feng Yu-hsiang (Feng Yuxiang, 1882&#8211;1948), the &#8220;Christian "
     "General,&#8221; commanded the Kuominchun (Guominjun), which held the "
     "northwest and the Peking region. Shifting alliances repeatedly, he leaned "
     "toward the Nationalists and formally joined the Kuomintang and the "
     "Northern Expedition in 1926."),
    ("the Fengtien military, who had assumed control",
     "Fengtien (Fengtian) is the old name for the Mukden region of Manchuria; "
     "the &#8220;Fengtien military&#8221; were the forces of the Manchurian "
     "warlord Chang Tso-lin, whose clique held Shanghai in 1925."),
    ("the revolt of Kuo Sung-lin",
     "Kuo Sung-lin (Guo Songling, 1883&#8211;1925), one of Chang Tso-lin&#8217;s "
     "ablest generals, mutinied against him in November 1925 and drove almost "
     "to Mukden before Japanese forces intervened to save Chang. Kuo was "
     "captured and shot in December 1925."),
    ("on the afternoon of March 18, 1926",
     "In the March 18, 1926, massacre, troops of the Peking government of Tuan "
     "Chi-jui fired on a crowd protesting a foreign ultimatum over the Taku "
     "forts guarding Tientsin, killing forty-seven and wounding some two "
     "hundred. The writer Lu Xun called it &#8220;the darkest day since the "
     "founding of the Republic.&#8221;"),
    ("the members of the foreign Municipal Council",
     "The Shanghai Municipal Council governed the International Settlement, the "
     "foreign-run district of Shanghai. Its councillors and voting ratepayers "
     "were overwhelmingly British, American, and Japanese; no Chinese sat on it "
     "until the three seats conceded, as related here, in 1926."),
    ("The speaker, Stirling Fessenden",
     "Stirling Fessenden (1875&#8211;1943), an American lawyer, chaired the "
     "Shanghai Municipal Council. In April 1927 he would open the way for "
     "Chiang&#8217;s purge by letting the Green Gang&#8217;s armed bands move "
     "through the International Settlement to fall on the Shanghai workers."),
    ("rose Yu Ya-ching, banker and compradore",
     "Yu Ya-ching (Yu Qiaqing, 1867&#8211;1945), a leading Shanghai comprador, "
     "banker, and shipping magnate, was among the most powerful Chinese "
     "businessmen in the International Settlement and a financial backer of "
     "Chiang Kai-shek."),
    ("the staff of General Chen Chi-mei",
     "Chen Chi-mei (Chen Qimei, 1878&#8211;1916), a close ally of Sun Yat-sen, "
     "was military governor of Shanghai after the 1911 revolution and Chiang "
     "Kai-shek&#8217;s early patron and sworn brother. He drew Chiang into both "
     "the revolutionary movement and the city&#8217;s underworld, and was "
     "assassinated in 1916 by agents of Yuan Shih-kai."),
    ("and Chang Ching-chiang, who was adding",
     "Chang Ching-chiang (Zhang Jingjiang, 1877&#8211;1950), a wealthy financier "
     "and early bankroller of Sun Yat-sen&#8217;s revolution, became Chiang "
     "Kai-shek&#8217;s patron and political mentor and briefly chaired the "
     "Kuomintang&#8217;s Central Executive Committee. Nearly blind, he was "
     "reckoned one of the party&#8217;s &#8220;four elders.&#8221;"),
    ("and gang in Shanghai, the Green Circle",
     "The Green Gang (Qing Bang; Isaacs&#8217;s &#8220;Green Circle&#8221;) was "
     "Shanghai&#8217;s dominant secret society, controlling the opium traffic, "
     "gambling, prostitution, and much of the labor market. Chiang&#8217;s ties "
     "to it and to its bosses&#8212;Huang Chin-jung, the &#8220;Hwang "
     "Ching-yung&#8221; named here, and Tu Yueh-sheng&#8212;made it the "
     "instrument of the April 1927 slaughter of the Shanghai Communists."),
    ("chief among them Hu Han-min",
     "Hu Han-min (Hu Hanmin, 1879&#8211;1936), a senior Kuomintang leader and a "
     "rival of Chiang&#8217;s for Sun&#8217;s mantle. Implicated in the August "
     "1925 assassination of the left-wing leader Liao Chung-kai, he was eased "
     "out of Canton and sent to Moscow, as this chapter recounts; he returned "
     "to lead the party right and later headed the Nationalist Legislative Yuan "
     "before breaking with Chiang in 1931."),
    ("the Krestintern, the Peasants’ International",
     "The Krestintern (Krestyansky Internatsional), the Communist "
     "International&#8217;s peasant organization, founded in Moscow in 1923 to "
     "draw the world&#8217;s peasantry behind Soviet policy; in practice "
     "largely a propaganda body."),
    ("The Sixth Plenum of the Executive Committee",
     "The Executive Committee of the Communist International (E.C.C.I.) was the "
     "Comintern&#8217;s governing body between world congresses. Its Sixth "
     "Enlarged Plenum, meeting in Moscow in February&#8211;March 1926, adopted "
     "the resolution on China quoted here, which hailed the Canton government "
     "and bound the Chinese Communists more tightly to the Kuomintang."),
    ("the Chinese Kerenskys who sat",
     "Alexander Kerensky (1881&#8211;1970) headed Russia&#8217;s Provisional "
     "Government between the February and October revolutions of 1917&#8212;the "
     "moderate swept aside by the Bolsheviks. Calling the Kuomintang chiefs "
     "&#8220;Chinese Kerenskys&#8221; casts them as a doomed liberal interlude "
     "before a proletarian seizure of power that, in China, never came."),
]

# ---- ch05 "Canton: The Coup of March 20, 1926" ----
CH05 = [
    ("the gunboat *Chung-* *shan*",
     "The Chung-shan (Zhongshan) Incident of March 20, 1926. On the pretext "
     "that this gunboat had been moved to threaten him in a Communist plot, "
     "Chiang proclaimed martial law, arrested the Communist commissars in his "
     "army and the guards of the Soviet advisers, and made himself master of "
     "Canton. Historians still dispute whether any plot existed; most, like "
     "Isaacs, read the affair as Chiang&#8217;s calculated stroke against "
     "Communist and Soviet influence. The vessel bore Sun Yat-sen&#8217;s "
     "honorific name, Sun Chung-shan (Sun Zhongshan)."),
    ("Teng Yen-ta, a Communist sympathizer",
     "Teng Yen-ta (Deng Yanda, 1895&#8211;1931), a left-wing Kuomintang leader "
     "and Whampoa political director. He later headed the Nationalist "
     "army&#8217;s political department, broke with Chiang over the 1927 "
     "betrayal, founded a &#8220;Third Party,&#8221; and was executed on "
     "Chiang&#8217;s orders in 1931."),
    ("said Eugene Chen",
     "Eugene Chen (Chen Youren, 1878&#8211;1944), a Trinidad-born, "
     "Western-trained lawyer, served as the Nationalists&#8217; foreign "
     "minister and the chief spokesman of the Wuhan left government in 1927. He "
     "conducted the movement&#8217;s combative diplomacy with the powers."),
    ("conferred with C. C. Wu",
     "C. C. Wu (Wu Chao-shu, 1887&#8211;1934), son of the diplomat Wu Ting-fang, "
     "was foreign minister at Canton and afterward the Nationalists&#8217; "
     "ambassador to the United States."),
    ("the Kwangsi militarist, Li Chi-sen",
     "Li Chi-sen (Li Jishen, 1885&#8211;1959), a general tied to the Kwangsi "
     "clique, governed Kwangtung after the national government moved north and "
     "crushed the Canton labor movement. He joined the 1927 anti-Communist "
     "purge, yet decades later chaired a pro-Communist party and became a "
     "vice-chairman of the People&#8217;s Republic of China."),
    ("Earl Browder, Tom Mann, and Jacques Doriot",
     "The Comintern&#8217;s 1927 delegation to China: Earl Browder "
     "(1891&#8211;1973), soon general secretary of the American Communist "
     "Party; Tom Mann (1856&#8211;1941), the veteran British labor agitator; "
     "and Jacques Doriot (1898&#8211;1945), then a French Communist deputy, who "
     "in the 1930s turned to fascism and led the collaborationist Parti "
     "Populaire Fran&#231;ais under the German occupation."),
]


def main():
    reading = {c: open(os.path.join(ROOT, "out", "%s_reading.md" % c),
                       encoding="utf-8").read() for c in ("ch04", "ch05")}
    batch = {"notes": {}}
    for chid, spec in (("ch04", CH04), ("ch05", CH05)):
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
    path = os.path.join(dest, "ch0405_editorial_notes.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("wrote", path)


if __name__ == "__main__":
    main()
