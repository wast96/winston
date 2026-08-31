#!/usr/bin/env python3
"""Assemble the EDITORIAL-note batch (roman stream, "ed": true) for ch06, ch07,
and ch08, under CLAUDE.md's generous density model and the STYLE.local rulings
(marker lands ON the glossed term; verdict tag only where a claim is weighed;
one subject one note; no re-noting a subject an earlier-reading unit already
covers; no printed-folio parentheticals; a note is never vaguer than its text;
each note tested against the whole paragraph it sits in; no competing
translation of a term the body already renders; pinyin gloss inline once per
named Chinese figure). Anchors are verbatim unique substrings of
out/<id>_reading.md; the builder numbers the stream in lowercase roman by
anchor position.

NOT re-noted here (already placed in an earlier-reading unit; cross-reference
only): the Kuomintang, the Comintern/E.C.C.I. body, the CCP, Sun Yat-sen,
Chiang Kai-shek, Borodin, Voitinsky, Wang Ching-wei (noted ch03; promoted to a
principal this batch), Chen Tu-hsiu, Trotsky, Lenin, Stalin, Bukharin, the
compradores, the Northern Expedition, the Whampoa Academy, May Thirtieth, the
Canton-Hong Kong strike, Chang Tso-lin, Wu Pei-fu, the Fengtien clique, the
Sixth Plenum of the E.C.C.I., the Green Gang and its bosses Hwang Ching-yung
and Tu Yueh-sen (noted ch04), Yu Ya-ching, Huang Fu, C. T. Wang, Yang Yu-ting,
Chang Ching-chiang, the International Settlement and the Shanghai Municipal
Council, extraterritoriality, hsien, Louis Napoleon the man (ch02; his Society
of December 10 is glossed here as a distinct allusion), the Three People's
Principles, the Boxers.

Deliberately left to the glossary / unnoted (minor one-off actors, named as a
skip tier in PROGRESS): Sir Miles Lampson, Li Pao-chang, Hsueh Yoh, Chang Chi,
Chang Siao-ling, Yang Hu, Niu Yung-chien's fellow negotiators (Yang Hsin-fu,
Wang Shiao-lai), Pi Shu-cheng, Chow Feng-chi, Quo Tai-chi, Wang I-ting, J. B.
Powell, Rodney Gilbert, Hua Kang, Ho Sen.

Writes scratch/ch0608_editorial_notes.json for apparatus_merge.py.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- ch06 "From Canton to the Yangtze" ----
CH06 = [
    ("Tang Sheng-chih, a Hunan militarist",
     "Tang Sheng-chih (Tang Shengzhi, 1889&#8211;1970), a Hunan general who "
     "threw in with the Northern Expedition and rose to govern the province and "
     "to command much of the Wuhan government&#8217;s military strength. He "
     "later turned against Chiang Kai-shek, was defeated, and after 1949 held "
     "office under the People&#8217;s Republic."),
    ("Sun Chuang-fang, military overlord of the five eastern provinces",
     "Sun Chuang-fang (Sun Chuanfang, 1885&#8211;1935) held Kiangsu, Chekiang, "
     "Anhwei, Fukien, and Kiangsi as the self-styled head of a five-province "
     "league. Broken by the Northern Expedition, he retired to the Japanese "
     "concession at Tientsin, where in 1935 he was shot dead by a woman "
     "avenging her father, whom Sun had had beheaded a decade before."),
    ("the famous “Ironsides” army",
     "The Fourth Army of the National Revolutionary Army, celebrated as the "
     "&#8220;Iron Army&#8221; (tiejun) for its feats in the Northern "
     "Expedition, above all the storming of Wuchang in October 1926. Isaacs "
     "renders the nickname &#8220;Ironsides,&#8221; after Oliver "
     "Cromwell&#8217;s hard-driving English Civil War cavalry."),
    ("comrade Chow En-lai",
     "Chow En-lai (Zhou Enlai, 1898&#8211;1976), then the Communists&#8217; "
     "chief organizer of work in the army and soon the director of their "
     "underground and military apparatus in Shanghai, where he led the March "
     "1927 workers&#8217; rising recounted in the next chapter. He became "
     "premier of the People&#8217;s Republic of China from 1949 until his "
     "death."),
    ("directives of the Seventh Plenum of the Executive Committee of the Communist International",
     "The Seventh Enlarged Plenum of the E.C.C.I., the Communist "
     "International&#8217;s governing Executive Committee, met in Moscow from "
     "November 22 to December 16, 1926, with China as its principal business. "
     "Its theses on the Chinese question, quoted throughout this chapter, were "
     "the Comintern&#8217;s fullest statement of the policy that governed the "
     "Chinese Communists on the eve of the 1927 rupture."),
    ("Tang Ping-shan, delegate of the Chinese Communist Party",
     "Tang Ping-shan (Tan Pingshan, 1886&#8211;1956), a founder of the Chinese "
     "Communist Party and its senior figure inside the Kuomintang. He sat on "
     "the Kuomintang&#8217;s Central Executive Committee and in 1927 became "
     "minister of agriculture in the Wuhan government; expelled from the "
     "Communist Party after the defeat, he helped found a &#8220;Third "
     "Party&#8221; and was reconciled with the Communists only late in life."),
    ("When P. Mif, later chief of the Stalinist experts",
     "Pavel Mif (1901&#8211;1939), the Soviet Union&#8217;s rising China "
     "specialist and rector of the Sun Yat-sen University for Chinese students "
     "in Moscow. As Stalin&#8217;s instrument in the Chinese party he later "
     "advanced the group of returned students known as the &#8220;Twenty-eight "
     "Bolsheviks.&#8221; He was shot in Stalin&#8217;s purges in 1939."),
    ("shelled the Yangtze town of Wanhsien",
     "The Wanhsien Incident of September 5, 1926: British gunboats bombarded "
     "Wanhsien (Wanxian), an upper-Yangtze port, after a general allied to Wu "
     "Pei-fu seized two British steamers and their crews. Scores of Chinese "
     "soldiers and civilians were killed, and the shelling sharpened "
     "anti-British feeling as the Northern Expedition advanced."),
    ("the Chen-O’Malley notes of February 19 and March 2",
     "The Chen&#8211;O&#8217;Malley agreements were negotiated by the "
     "Nationalist foreign minister Eugene Chen with the British diplomat Owen "
     "O&#8217;Malley&#8212;among the first occasions on which a foreign power "
     "gave a treaty concession in China back. They took effect in March 1927."),
    ("visited Kiukiang and inspected",
     "Arthur Ransome (1884&#8211;1967), the <i>Manchester Guardian</i>&#8217;s "
     "correspondent in revolutionary Russia and then in China."),
]

# ---- ch07 "The Shanghai Insurrection" ----
CH07 = [
    ("the initiative to a Kuomintang committee headed by Niu Yung-chien",
     "Niu Yung-chien (Niu Yongjian), a veteran Kuomintang politician who served "
     "as Chiang Kai-shek&#8217;s chief agent in Shanghai, holding a mandate "
     "from the party headquarters at Canton."),
    ("Chang Tsung-chang, warlord of Shantung",
     "Chang Tsung-chang (Zhang Zongchang, 1881&#8211;1932), the &#8220;Dogmeat "
     "General,&#8221; notorious even among warlords for his private fortune, "
     "his harem, and the White Russian mercenaries in his army. Driven from "
     "Shantung by the Northern Expedition, he was shot dead at Tsinan station "
     "in 1932 by the nephew of a man he had killed."),
    ("the right-wing Kuomintang politicians, led by Wu Chih-hui",
     "Wu Chih-hui (Wu Zhihui, 1865&#8211;1953), an anarchist turned Kuomintang "
     "elder, essayist, and celebrated calligrapher, one of the party&#8217;s "
     "revered &#8220;four elders.&#8221; Fiercely anti-Communist, he would "
     "move the resolution at the April 1927 Central Supervisory Committee "
     "meeting that gave Chiang&#8217;s purge of the Communists its party "
     "sanction."),
    ("Chiu Chiu-pei, one of its leading members",
     "Chiu Chiu-pei (Qu Qiubai, 1899&#8211;1935), a writer and translator among "
     "the Communist Party&#8217;s foremost leaders. At the August 1927 "
     "emergency conference he replaced Chen Tu-hsiu at the party&#8217;s head; "
     "captured by the Nationalists, he was executed in 1935."),
    ("the failure of the German insurrection in 1923",
     "The &#8220;German October&#8221; of 1923: the Communist International, "
     "counting on a revolution in Germany, ordered and then called off a "
     "rising. The cancellation reached Hamburg too late, and the local "
     "Communists&#8217; isolated revolt was crushed within a day&#8212;a "
     "debacle the Comintern long invoked as a warning."),
    ("Pai Chung-hsi, a Kwangsi general",
     "Pai Chung-hsi (Bai Chongxi, 1893&#8211;1966), a Muslim general of the "
     "Kwangsi clique and a chief of staff of the Northern Expedition, "
     "nicknamed the &#8220;Little Chuko&#8221; for his generalship. He "
     "occupied Shanghai for Chiang and commanded the troops behind the April "
     "1927 purge there; he died on Taiwan, a former Nationalist defense "
     "minister."),
    ("reinforced by White Russian mercenaries",
     "White Russians were anti-Bolshevik &#233;migr&#233;s who fled Russia "
     "after the Bolshevik victory in the civil war of 1917&#8211;1922. Tens of "
     "thousands settled in China, and many destitute former soldiers hired "
     "themselves to the warlords; Chang Tsung-chang&#8217;s armored-train and "
     "machine-gun crews, met throughout these pages, were their most feared "
     "employment."),
    ("the Commercial Press, the Fifth police station",
     "The Commercial Press (Shangwu Yinshuguan), founded in Shanghai in 1897, "
     "was China&#8217;s largest publishing house and a landmark of the Chapei "
     "district; its big workforce made it a stronghold of the labor movement."),
]

# ---- ch08 "The Prodigal's Return" ----
CH08 = [
    ("A native of Ningpo",
     "Ningpo (Ningbo), a port south of Shanghai in Chekiang province, was the "
     "home region of the &#8220;Chekiang&#8211;Ningpo&#8221; financiers who "
     "dominated Shanghai&#8217;s banking. A Chekiang man himself, Chiang "
     "Kai-shek could claim these bankers as fellow provincials&#8212;a bond of "
     "native place that counted for much in Chinese business and politics."),
    ("the Russian Black Hundred groups",
     "The Black Hundreds were reactionary, ultra-monarchist gangs in the last "
     "years of Tsarist Russia, notorious for street violence and for anti-Jewish "
     "pogroms carried out with official connivance."),
    ("Louis Napoleon’s Society of December the Tenth",
     "The Society of December 10 was the club of hired toughs and lumpen "
     "adventurers with which Louis Napoleon (Napoleon III) intimidated his "
     "opponents on his road to power in France, named for the date of his 1848 "
     "election. Marx dissected it in <i>The Eighteenth Brumaire of Louis "
     "Bonaparte</i>, the source of the comparison Isaacs reaches for here."),
    ("Ho Ying-chin sat with an army",
     "Ho Ying-chin (He Yingqin, 1890&#8211;1987), one of Chiang Kai-shek&#8217;s "
     "most senior and loyal generals and a fellow student of his in Japan, long "
     "the mainstay of the Nationalist high command. He served as minister of "
     "war and, briefly in 1949, premier, and died on Taiwan."),
    ("Wu Chih-hui, Tsai Yuan-pei",
     "Tsai Yuan-pei (Cai Yuanpei, 1868&#8211;1940), the eminent educator who as "
     "chancellor of Peking University (1917&#8211;1926) sheltered the ferment "
     "of the May Fourth era and who later founded the Academia Sinica. Another "
     "of the Kuomintang&#8217;s anti-Communist &#8220;four elders,&#8221; he "
     "lent his great prestige to the 1927 purge."),
    ("looting and attacks on foreigners on the day the city changed hands",
     "The Nanking Incident of March 24, 1927. Later scholarship broadly bears "
     "out Isaacs&#8217;s view that no plot lay behind the affair and that the "
     "attackers were mostly undisciplined and deserting troops, not agents of "
     "the Communists or of Chiang. (corroborated)"),
    ("notably the *North China Daily News,*",
     "The <i>North China Daily News</i>, published in Shanghai, was the most "
     "influential British newspaper in China and the recognized organ of "
     "foreign&#8212;above all British&#8212;settler opinion."),
]


def main():
    reading = {c: open(os.path.join(ROOT, "out", "%s_reading.md" % c),
                       encoding="utf-8").read()
               for c in ("ch06", "ch07", "ch08")}
    batch = {"notes": {}}
    for chid, spec in (("ch06", CH06), ("ch07", CH07), ("ch08", CH08)):
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
    path = os.path.join(dest, "ch0608_editorial_notes.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("wrote", path)


if __name__ == "__main__":
    main()
