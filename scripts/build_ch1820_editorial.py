#!/usr/bin/env python3
"""Assemble the EDITORIAL-note batch (roman stream, "ed": true) for ch18, ch19,
and ch20 -- the final chapters -- under CLAUDE.md's generous density model and
the STYLE.local rulings (marker lands ON the glossed term; verdict tag only
where a claim is weighed; one subject one note, at its first reading appearance;
a note never restates the body or re-underlines its irony; identify a quoted
witness/source by placement, then stop; open with the modern pinyin form and
dates; no repeated death year; a book-specific proper name takes the body's own
capitalization; do NOT re-note a subject an earlier-reading unit already covers).
Anchors are verbatim unique substrings of out/<id>_reading.md; the builder
numbers the stream in lowercase roman by anchor position.

These chapters carry the aftermath (1927-1938): the Kuomintang consolidation and
terror, the Japanese conquest of Manchuria and North China, the rise and fall of
the Kiangsi soviets, the Long March, and the second united front of 1937. Much
of that ground -- and most of the cast of the revolution proper -- was placed in
an earlier-reading unit, so notes concentrate on the NEW subjects of the
aftermath.

NOT re-noted here (already placed editorially in an earlier-reading unit;
grep-verified against notes.json, ed:true, not a mere author-note citation):
Mao Tse-tung (ch00a), Chiang Kai-shek / Chen Tu-hsiu / Borodin / Wang Ching-wei
/ Chow En-lai / Chiu Chiu-pei (principals + earlier chapters), Li Li-san (ch15),
Ho Lung / Yeh Ting (ch16/ch12), Ho Chien (ch13), Feng Yu-hsiang (ch04), Chang
Hsueh-liang (ch15 -- his person; the Sian INCIDENT, the event, is noted at its
full narration in ch20), Sun Fo (ch11), Eugene Chen (ch05/06), Teng Yen-ta
(ch05), Pai Chung-hsi (ch07), Tang Sheng-chih (ch06), Peng Pai (ch03/17), P. Mif
and the Sun Yat-sen University he ran (ch06), the Boxer Protocol / indemnity
(ch01), the "democratic dictatorship" and the bloc of four classes (body-defined
across the book; ch00b), Manchuria / Mukden (ch04), the CCP / Comintern-E.C.C.I.
/ Kuomintang / Red Army designations, Trotsky and the Left Opposition, Stalin,
Bukharin (ch00b/ch02/ch14).

Deliberately left to the skip tier (minor one-off actors, sources the body
contexts inline, or terms the prose itself defines; named in PROGRESS): the
individual Red-district and city figures Chu Pei-teh-type militarists not
recurring here, Yuan and Wang (the Chingkang bandits), Hsiao Keh, Lo Min / the
"Lo Min line" (body-defined), O Fong, Ho Mung-shung, Kung Ho-chung, Chang Yi, Ho
So-hen, Teng Shao-pin, Lo Fu's junior colleagues, the Third Party and the Chinese
Trotskyist org-names (body-contexted), C. T. Wang's successors in office; the
"world economic crisis" (the Great Depression, universally known and body-glossed
via its silver mechanism, which IS noted).

Writes scratch/ch1820_editorial_notes.json for apparatus_merge.py.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def unescape(anchor):
    """Anchors are written with numeric character references for the curly
    quotes / dashes so the Python source stays legible, but the reading file
    (and thus the stored anchor, which the builder matches VERBATIM) uses the
    literal Unicode characters. Convert &#NNNN; -> chr(NNNN) for the anchor."""
    return re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), anchor)

# ---- ch18 "Fruits of Defeat" ----
CH18 = [
    ("At the end of 1930 the Chinese Red Aid estimated",
     "The Chinese Red Aid was the Chinese section of International Red Aid "
     "(known by its Russian initials MOPR), the Comintern-sponsored body that "
     "collected relief for political prisoners and their families. The "
     "casualty tallies cited here therefore come from the victims&#8217; own "
     "side."),
    ("aggravated by the American silver purchasing policy in 1934",
     "The United States Silver Purchase Act of June 1934 drove up the world "
     "price of silver. Because China was almost alone in still being on a silver "
     "standard, the metal was pulled out of the country, contracting its money "
     "and credit and deepening the slump &#8212; which forced China off silver "
     "and onto a managed paper currency in 1935 (corroborated)."),
    ("terminating the status quo created by the Washington Treaty of 1922",
     "The Nine-Power Treaty, signed at the Washington Conference of "
     "1921&#8211;22, bound the powers to respect China&#8217;s territorial "
     "integrity and the &#8220;Open Door&#8221; of equal commercial access. "
     "Japan&#8217;s seizure of Manchuria in 1931 was its first open breach."),
    ("the plans of Britain and France for the creation of a cordon sanitaire",
     "A <i>cordon sanitaire</i> (French, &#8220;quarantine line&#8221;) is a "
     "ring of buffer states used to seal off a feared neighbor; the phrase "
     "entered interwar politics for the belt of countries meant to contain "
     "Soviet Russia."),
    ("transformed it into &#8220;Manchukuo,&#8221;",
     "Manchukuo (&#8220;Manchu country&#8221;) was the puppet state Japan "
     "proclaimed in the three northeastern provinces in 1932, with the deposed "
     "last Qing emperor as its figurehead (see the final chapter). Almost no "
     "government recognized it; it vanished with Japan&#8217;s "
     "defeat in 1945."),
    ("occupied Jehol",
     "Jehol (Rehe) was the province north of the Great Wall between Manchuria "
     "and Inner Mongolia. Japanese forces overran it early in 1933 and annexed "
     "it to Manchukuo, carrying the conquest up to the Wall itself."),
    ("the soldiers of the 19th Route Army made their historic stand at Shanghai",
     "The 19th Route Army (also written Nineteenth Route Army) was a Cantonese "
     "force under Tsai Ting-kai (Cai Tingkai) whose defense of Shanghai against "
     "the Japanese in January&#8211;March 1932, in defiance of Chiang&#8217;s "
     "policy of non-resistance, made it a patriotic symbol. Chiang broke it up "
     "after it launched the Fukien revolt of 1933 (see the final chapter)."),
    ("headed by Lord Lytton",
     "The Lytton Commission was the League of Nations inquiry, under the second "
     "Earl of Lytton, whose 1932 report found Japan the aggressor in Manchuria "
     "but proposed autonomy under nominal Chinese sovereignty rather than simple "
     "restoration. Japan answered by walking out of the League in 1933."),
    ("Chiang Kai-shek&#8217;s representatives signed the Tangku Truce",
     "The Tangku Truce of May 31, 1933 ended the fighting after Jehol by setting "
     "up a demilitarized zone across northeastern Hopei, in effect conceding the "
     "loss of Manchuria and Jehol to Japan."),
    ("the Chin-Doihara accord recognized Japan&#8217;s claim",
     "The Chin-Doihara and Ho-Umetsu agreements of mid-1935, extorted under "
     "Japanese pressure, cleared Nationalist troops, officials, and party "
     "organs out of Chahar and Hopei, loosening Nanking&#8217;s hold on North "
     "China ahead of the full invasion of 1937."),
    ("when Japanese forces marched to the gates of Peiping",
     "Peiping (&#8220;northern peace&#8221;) was the new name given to Peking "
     "in 1928, when the Nationalists moved the capital south to Nanking and the "
     "old city lost its status as &#8220;northern capital&#8221;; it is the "
     "Peking (Beijing) of the earlier chapters under its 1928&#8211;49 name."),
    ("Bukharin told the Sixth Congress of the Comintern in July 1928",
     "The Sixth World Congress of the Communist International (Moscow, "
     "July&#8211;September 1928) proclaimed the ultra-left &#8220;Third "
     "Period&#8221; line and wrote the &#8220;democratic dictatorship&#8221; and "
     "the turn to soviets into the Comintern&#8217;s program for China &#8212; "
     "the course this chapter examines."),
    ("the sudden discovery of the &#8220;third period,&#8221;",
     "The &#8220;Third Period&#8221; was the Comintern&#8217;s 1928 doctrine "
     "that capitalism had entered a final phase of terminal crisis and imminent "
     "revolution. It licensed ultra-left &#8220;class against class&#8221; "
     "tactics and treated socialist and reformist parties as the main enemy "
     "&#8212; a line that split the German left before Hitler and, in China, "
     "underwrote the reckless insurrections that followed."),
    ("wrote Trotsky to the Sixth Congress from his exile in Alma Ata",
     "Alma-Ata (now Almaty, in Kazakhstan) was where Stalin banished Trotsky in "
     "January 1928, a year before expelling him from the Soviet Union "
     "altogether. The letters to the Sixth Congress quoted here were written "
     "from that internal exile."),
    ("faction of the Kuomintang (&#8220;Reorganizationists&#8221;)",
     "The Reorganization Clique (Gaizupai) were the followers of Wang Ching-wei, "
     "active around 1928&#8211;31, who called for a return to the party&#8217;s "
     "more populist &#8220;reorganized&#8221; form of 1924 and opposed "
     "Chiang&#8217;s military rule &#8212; the civilian, anti-Chiang opposition "
     "the Communists left unchallenged."),
    ("headed by Chen Shao-yu (Wang Min)",
     "Wang Ming (Wang Min; born Chen Shao-yu, 1904&#8211;1974) led the "
     "Moscow-trained group known as the &#8220;Returned Students&#8221; or "
     "&#8220;Twenty-Eight Bolsheviks,&#8221; installed atop the party in 1931 "
     "under Pavel Mif&#8217;s patronage. The Comintern&#8217;s man in China and "
     "later Mao Tse-tung&#8217;s chief rival for the leadership, he was pushed "
     "aside by Mao in the war years and died in exile in Moscow."),
    ("established what it called the &#8220;Chinese Soviet Republic.&#8221;",
     "The Chinese Soviet Republic was proclaimed at Juichin (Ruijin) in Kiangsi "
     "(Jiangxi) on November 7, 1931, with Mao Tse-tung as chairman &#8212; the "
     "federation of rural base areas whose &#8220;rise and fall&#8221; the next "
     "chapter traces. Broken by Chiang&#8217;s fifth campaign, it was "
     "abandoned in the retreat of 1934."),
]

# ---- ch19 "The Rise and Fall of 'Soviet China'" ----
CH19 = [
    ("The first and most important of these armies was formed at Chingkangshan",
     "Chingkangshan (the Jinggang Mountains), on the Hunan&#8211;Kiangsi border, "
     "was the refuge where Mao Tse-tung and then Chu Teh gathered the first "
     "durable Red base in 1927&#8211;28. It is celebrated in Chinese Communist "
     "history as the &#8220;cradle of the Red Army.&#8221;"),
    ("Here came the German-educated Communist officer, Chu Teh",
     "Chu Teh (Zhu De, 1886&#8211;1976), a former Yunnan-army officer, became "
     "the Red Army&#8217;s commander-in-chief and Mao Tse-tung&#8217;s lifelong "
     "military partner from Chingkangshan onward &#8212; hence the paired name "
     "&#8220;Chu-Mao.&#8221; He led the Eighth Route Army against Japan and, "
     "after 1949, was a marshal and head of state of the People&#8217;s "
     "Republic."),
    ("A small force under Peng Teh-huai",
     "Peng Teh-huai (Peng Dehuai, 1898&#8211;1974) was one of the ablest Red "
     "commanders and later a marshal and China&#8217;s defense minister. "
     "Disgraced in 1959 for challenging Mao Tse-tung over the famine of the "
     "Great Leap Forward, he died after brutal treatment in the Cultural "
     "Revolution."),
    ("the Communist Fang Chih-min headed a partisan band",
     "Fang Chih-min (Fang Zhimin, 1899&#8211;1935) built the soviet base in "
     "northeastern Kiangsi. Captured when his column was cut off during the "
     "breakout of 1934&#8211;35, he was executed by the Kuomintang and is "
     "remembered as a Communist martyr for the prison essays he left behind."),
    ("had all been students in Moscow during the years of the revolution",
     "These young men were the &#8220;Returned Students,&#8221; or "
     "&#8220;Twenty-Eight Bolsheviks&#8221; &#8212; Chinese Communists trained "
     "at the Sun Yat-sen University in Moscow (whose rector, Pavel Mif, is noted "
     "earlier). Backed by Mif and the Comintern, and led by Chen Shao-yu (Wang "
     "Min), they ousted Li Li-san and ran the party from 1931; it is their "
     "Moscow-dictated line that these chapters attack."),
    ("Manuilsky expressed his astonishment",
     "Dmitry Manuilsky (1883&#8211;1959), a Ukrainian Bolshevik, was a secretary "
     "of the Communist International and one of Stalin&#8217;s chief managers of "
     "it through the 1930s."),
    ("the Chinese equivalent not of the Russian Bolshevik Party but of the Social Revolutionary Party",
     "The Socialist Revolutionaries were the mass peasant-based party that "
     "rivaled the Bolsheviks in the Russian Revolution of 1917. Isaacs&#8217;s "
     "comparison casts the Chinese party&#8217;s reliance on a purely peasant "
     "base as a slide away from Bolshevism toward the agrarian populism the "
     "Bolsheviks had defeated."),
    ("Lo Fu, a leading spokesman",
     "Lo Fu (Zhang Wentian, 1900&#8211;1976), one of the Moscow-trained "
     "leaders, became the party&#8217;s general secretary in 1935 and later a "
     "senior diplomat; he was purged alongside Peng Teh-huai in 1959."),
    ("schooled by the German General von Seeckt",
     "General Hans von Seeckt (1866&#8211;1936), who had rebuilt the German army "
     "after 1919, advised Chiang Kai-shek in 1933&#8211;35 and helped design the "
     "advancing ring of blockhouses and economic blockade that finally strangled "
     "the Kiangsi soviet (corroborated)."),
    ("That &#8220;long trek&#8221; will be recorded",
     "This flight &#8212; the Long March of October 1934 to October 1935 "
     "&#8212; carried the main Red forces some six thousand miles from Kiangsi "
     "to a new base at Yenan in the far northwest (see the final chapter). Mao "
     "Tse-tung fastened his grip on the party during it, and it became the "
     "founding epic of Chinese Communism."),
]

# ---- ch20 "The New 'National United Front'" ----
CH20 = [
    ("thrashed Foreign Minister C. T. Wang",
     "C. T. Wang (Wang Cheng-ting; Wang Zhengting, 1882&#8211;1961) was a "
     "veteran diplomat and foreign minister whom nationalist students beat in "
     "1931 over the government&#8217;s refusal to resist Japan; he later served "
     "as ambassador to Washington."),
    ("His successor, V. K. Wellington Koo",
     "V. K. Wellington Koo (Ku Wei-chun; Gu Weijun, 1888&#8211;1985) was "
     "China&#8217;s most eminent modern diplomat &#8212; its spokesman against "
     "the Shantung transfer at the 1919 Paris Peace Conference, ambassador to "
     "Paris, London, and Washington, and afterward a judge of the International "
     "Court of Justice."),
    ("to this day continue to shake the uneasy throne of Henry Pu Yi",
     "Pu Yi (1906&#8211;1967) was the last emperor of the Qing, put on the "
     "throne as an infant in 1908 and deposed in 1912. The Japanese installed "
     "him as nominal ruler of Manchukuo in 1932 and &#8220;emperor&#8221; in "
     "1934; captured by Soviet troops in 1945, he ended his days as an ordinary "
     "citizen of the People&#8217;s Republic."),
    ("the *hunghudtze* or &#8220;bandits,&#8221;",
     "The <i>hunghutze</i> (&#8220;red beards&#8221;) were the traditional "
     "armed bandit bands of Manchuria. After the Japanese conquest of 1931 many "
     "of them turned to anti-Japanese guerrilla resistance, as Isaacs notes."),
    ("the formation of a new &#8220;People&#8217;s Productionist Party&#8221;",
     "This is the Fukien Rebellion of November 1933&#8211;January 1934: "
     "dissident Kuomintang politicians and the 19th Route Army set up a rival "
     "&#8220;People&#8217;s Revolutionary Government&#8221; at Foochow, broke "
     "with Nanking, and sought terms with the Reds. Chiang crushed it within two "
     "months and dispersed the 19th Route Army (corroborated)."),
    ("launched the movement for creation of a Fourth International",
     "The Fourth International was the world organization of Trotsky&#8217;s "
     "followers, launched in the mid-1930s and formally founded in 1938 in "
     "opposition to the Stalinized Comintern (the Third International). Isaacs "
     "wrote as one of its supporters."),
    ("consummating at its Seventh World Congress in Moscow (July 1935)",
     "The Seventh &#8212; and last &#8212; World Congress of the Communist "
     "International (July&#8211;August 1935) proclaimed the &#8220;Popular "
     "Front&#8221; line: alliances with socialist and liberal parties and "
     "&#8220;peace-loving&#8221; governments against fascism. In China this "
     "meant the drive for a fresh united front with the Kuomintang."),
    ("the National Salvation Association, a petty bourgeois nationalist body",
     "The National Salvation Association was the broad patriotic movement "
     "pressing for a united front against Japan. In November 1936 Nanking "
     "arrested seven of its leaders &#8212; the &#8220;Seven Gentlemen&#8221; "
     "whose jailing the book mentions just below &#8212; making them a cause "
     "for the resistance movement (corroborated)."),
    ("H. H. Kung, the finance minister who went to Europe",
     "H. H. Kung (Kung Hsiang-hsi; Kong Xiangxi, 1881&#8211;1967), a banker "
     "reputed to descend from Confucius and married to a sister of Madame Chiang "
     "Kai-shek, ran Nationalist finances as finance minister and premier for "
     "much of the 1930s and 1940s."),
    ("represented in China by Sir Frederick Leith-Ross",
     "Sir Frederick Leith-Ross (1887&#8211;1968), chief economic adviser to the "
     "British Treasury, led the 1935&#8211;36 mission that helped Nanking take "
     "China off silver and put its new managed currency (the <i>fabi</i>) on a "
     "sterling footing &#8212; the reform described here (corroborated)."),
    ("made a tentative stab across the Suiyuan border",
     "In November 1936 Chinese provincial forces threw back a Japanese-backed "
     "Manchukuo-and-Mongol thrust into Suiyuan, in Inner Mongolia. The "
     "&#8220;Suiyuan victory,&#8221; the first Chinese success against the "
     "creeping advance, gave a sharp lift to the movement for resistance "
     "(corroborated)."),
    ("the officers and men of the Sian garrison rose in revolt on the night of December 11",
     "This mutiny, in the early hours of December 12, 1936, is the Sian "
     "Incident: Chang Hsueh-liang (noted earlier) and his Manchurian troops "
     "seized Chiang Kai-shek to force him to end the civil war and fight Japan. "
     "With Chow En-lai mediating (below), Chiang was freed on Christmas Day, and "
     "the affair opened the way to the second Kuomintang&#8211;Communist united "
     "front."),
    ("in the southwest with Chen Chi-tang, Li Tsung-jen",
     "Chen Chi-tang (Chen Jitang, 1890&#8211;1954), the militarist master of "
     "Kwangtung, and Li Tsung-jen (Li Zongren, 1890&#8211;1969), the leading man "
     "of the Kwangsi clique (with Pai Chung-hsi), were semi-independent "
     "southwestern warlords whom Chiang finally brought to heel in 1936."),
    ("A Communist youth congress held at Yenan, Shensi",
     "Yenan (Yan&#8217;an), a town in northern Shensi, became the "
     "Communists&#8217; headquarters from 1936&#8211;37 until 1947; the "
     "&#8220;Yenan period&#8221; saw Mao Tse-tung consolidate his leadership and "
     "his doctrine. Isaacs also calls the seat by its county name, "
     "&#8220;Fushih.&#8221;"),
    ("as the &#8220;Eighth Route Army&#8221; was announced at Nanking",
     "The Eighth Route Army was the name under which the Red Army was folded "
     "into the Nationalist forces in September 1937 for the war with Japan. "
     "Under Chu Teh&#8217;s command it became the main Communist force in the "
     "north and, with the New Fourth Army, a nucleus of what grew into the "
     "People&#8217;s Liberation Army."),
    ("A new &#8220;national united front&#8221; now took shape",
     "This is the Second United Front (1937&#8211;1941), the wartime alliance of "
     "the Kuomintang and the Communists against Japan. An armed truce rather "
     "than a merger, it frayed steadily and broke down in practice with the New "
     "Fourth Army Incident of January 1941, though neither side formally "
     "renounced it during the war."),
    ("the &#8220;Lukouchiao incident&#8221;&#8212;the clash south of Peiping",
     "The clash at the Lukouchiao (Lugouqiao), the &#8220;Marco Polo Bridge&#8221; "
     "southwest of Peiping, on July 7, 1937 opened the full-scale "
     "Sino-Japanese War of 1937&#8211;45, which four years later merged into the "
     "Second World War in the Pacific."),
    ("made a fresh stand around Hsuchow",
     "Near Hsuchow (Xuzhou) in the spring of 1938 Chinese armies won, at "
     "Taierhchuang (Tai&#8217;erzhuang), the first major Chinese victory of the "
     "war, mauling some of Japan&#8217;s best divisions before the city itself "
     "fell in May (corroborated)."),
]


def main():
    reading = {c: open(os.path.join(ROOT, "out", "%s_reading.md" % c),
                       encoding="utf-8").read()
               for c in ("ch18", "ch19", "ch20")}
    batch = {"notes": {}}
    for chid, spec in (("ch18", CH18), ("ch19", CH19), ("ch20", CH20)):
        notes = []
        for anchor, body in spec:
            anchor = unescape(anchor)
            n = reading[chid].count(anchor)
            if n != 1:
                sys.exit("%s: anchor %r occurs %d times (need 1)"
                         % (chid, anchor, n))
            notes.append({"anchor": anchor, "note": body, "ed": True})
        batch["notes"][chid] = notes
        print("%s: %d editorial notes" % (chid, len(notes)))

    dest = os.path.join(ROOT, "scratch")
    os.makedirs(dest, exist_ok=True)
    path = os.path.join(dest, "ch1820_editorial_notes.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("wrote", path)


if __name__ == "__main__":
    main()
