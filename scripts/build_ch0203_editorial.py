#!/usr/bin/env python3
"""Assemble the EDITORIAL-note batch (roman stream, "ed": true) for ch02 and
ch03: the reader-facing layer under CLAUDE.md's generous density model and the
STYLE.local rulings (marker lands ON the glossed term; verdict tag only where a
claim is weighed; one subject one note; no re-noting a subject an earlier-
reading unit already covers; no printed-folio parentheticals; no body-restating
filler). Anchors are verbatim unique substrings of out/<id>_reading.md; the
builder numbers the stream in lowercase roman by anchor position.

Writes scratch/ch0203_editorial_notes.json for apparatus_merge.py.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- ch02 "Problems of the Chinese Revolution" (theory; most of the Marxist
# and Russian cast is already noted in the front matter and ch01) ----
CH02 = [
    ("Professor Chen Han-seng has estimated",
     "Chen Han-seng (1897&#8211;2004), a Marxist economist and sociologist "
     "whose field surveys of Chinese villages in the 1920s and 1930s, cited "
     "repeatedly in this chapter, documented the concentration of land and the "
     "spread of tenancy. He worked at the Academia Sinica and later for the "
     "international Communist movement, and lived to 107."),
    ("*sous l’ancien régime*",
     "French, &#8220;under the old regime&#8221; &#8212; the France of "
     "absolute monarchy before the Revolution of 1789."),
    ("and *likin*",
     "<i>Likin</i> (lijin), an internal transit tax levied on goods in "
     "movement at innumerable local barriers. Introduced in 1853 to fund the "
     "suppression of the Taiping Rebellion and not abolished until 1931, it "
     "fragmented China&#8217;s internal market and became a byword for fiscal "
     "extortion."),
    ("Cromwell’s armies",
     "Oliver Cromwell (1599&#8211;1658) led the parliamentary armies that "
     "defeated and executed Charles I and headed the resulting Commonwealth "
     "(1649&#8211;1660) &#8212; the English Revolution that Trotsky&#8217;s "
     "introduction invokes as the classic bourgeois revolution."),
    ("the National Assembly of 1789",
     "Isaacs contrasts two phases of the French Revolution: the National "
     "Assembly of 1789, the moderate body of propertied reformers of its first "
     "phase, and the Jacobin republic of 1793, dominated by Robespierre&#8217;s "
     "radicals, which abolished feudal dues and defended the Revolution by "
     "terror. His point is that the later, more plebeian phase, not the first, "
     "broke feudalism."),
    ("the sans-culotte",
     "The <i>sans-culottes</i> (French, literally &#8220;without "
     "knee-breeches&#8221;) were the radical wage-earners and small tradesmen "
     "of Paris whose street militancy drove the French Revolution leftward in "
     "1792&#8211;94."),
    ("Cavaignac",
     "Louis-Eug&#232;ne Cavaignac (1802&#8211;1857), the French general who "
     "bloodily crushed the Paris workers&#8217; rising of June 1848 &#8212; for "
     "Isaacs the type of the bourgeoisie&#8217;s turn against its own "
     "revolution."),
    ("the Bismarcks and the Louis Napoleons",
     "Otto von Bismarck (1815&#8211;1898), who unified Germany from above, and "
     "Louis Napoleon (Napoleon III, 1808&#8211;1873), who seized power in "
     "France by coup in 1851: Isaacs&#8217;s shorthand for the authoritarian "
     "strongmen to whom a bourgeoisie frightened of revolution surrendered "
     "power after 1848."),
    ("the Paris Commune of 1871",
     "The revolutionary municipal government that ruled Paris for some ten "
     "weeks in the spring of 1871 before being crushed with thousands of "
     "deaths. Marx analyzed it as the first working-class seizure of power, and "
     "Lenin took it as the model of the &#8220;dictatorship of the "
     "proletariat.&#8221;"),
    ("the Second World Congress of the Communist International in 1920",
     "The Comintern&#8217;s Second Congress (Moscow, July&#8211;August 1920) "
     "adopted Lenin&#8217;s &#8220;Theses on the National and Colonial "
     "Question,&#8221; quoted here, together with the supplementary theses of "
     "the Indian Communist M. N. Roy. It set the line &#8212; support for "
     "anti-colonial movements, but strict organizational independence within "
     "them &#8212; whose abandonment in China this book indicts."),
    ("The Social Democrats of the Second International",
     "The Second International (1889&#8211;1916) was the pre-war federation of "
     "socialist and labor parties. Isaacs&#8217;s charge is that its major "
     "parties, when war broke out in 1914, backed their own governments rather "
     "than international workers&#8217; solidarity &#8212; the collapse that "
     "prompted the founding of the Comintern, the Third International."),
    ("needs of “war Communism.”",
     "&#8220;War Communism&#8221; (1918&#8211;1921) was the Bolshevik "
     "regime&#8217;s emergency economy during the civil war: grain forcibly "
     "requisitioned from the peasants, industry nationalized, private trade "
     "suppressed. Its exhaustion of the country forced the retreat to the New "
     "Economic Policy."),
    ("the New Economic Policy to win a breathing space",
     "The New Economic Policy (NEP), adopted in 1921, replaced forced "
     "requisitioning with a tax in kind and allowed limited private trade and "
     "small enterprise to revive an economy wrecked by war. It lasted until "
     "Stalin&#8217;s forced collectivization at the end of the 1920s."),
    ("the theory of “Socialism in one country”",
     "The doctrine, advanced by Stalin from 1924 and elaborated by Bukharin, "
     "that a socialist society could be built in the Soviet Union alone without "
     "waiting for revolution abroad. It broke with the Bolsheviks&#8217; "
     "original premise &#8212; and with Trotsky&#8217;s &#8220;permanent "
     "revolution&#8221; &#8212; that the Russian revolution could survive only "
     "as part of an international one; Isaacs makes it the root of the "
     "Comintern&#8217;s subordination of foreign revolutions to Soviet state "
     "interests."),
    ("the rich peasants (kulaks)",
     "<i>Kulaks</i>, the better-off peasants who hired labor or rented out "
     "land. Courted under the NEP, they were &#8220;liquidated as a "
     "class&#8221; in Stalin&#8217;s forced collectivization of 1929&#8211;33, "
     "with millions dispossessed, deported, or starved."),
    ("the Nepmen",
     "The <i>Nepmen</i> were the private traders and small entrepreneurs who "
     "flourished under the New Economic Policy; like the kulaks they were "
     "squeezed out when the NEP was ended."),
    ("the bourgeois Provisional Government in March 1917",
     "The Provisional Government held power in Russia between the fall of the "
     "tsar in February/March 1917 and the Bolshevik seizure of power in "
     "October. Whether socialists should support it &#8212; the dispute "
     "recounted here &#8212; was the pivot of Lenin&#8217;s April Theses."),
    ("The Mensheviks Martinov and Rafes",
     "Alexander Martynov (1865&#8211;1935) and Moissaye Rafes "
     "(1883&#8211;1942), former Mensheviks who joined the Bolsheviks in the "
     "early 1920s and became Comintern commentators on China. Isaacs casts them "
     "as importing into Comintern policy the old Menshevik premise that the "
     "bourgeoisie must lead the bourgeois revolution."),
    ("the rotting autocracy of the Romanoffs",
     "The Romanov dynasty ruled Russia from 1613 until the tsar&#8217;s "
     "abdication in 1917; &#8220;the Romanoffs&#8221; stands here for the "
     "imperial autocracy itself."),
]

# ---- ch03 "The New Awakening" (the 1919&#8211;25 narrative; the front-loaded
# cast chapter) ----
CH03 = [
    ("the figure of Chen Tu-hsiu",
     "Chen Tu-hsiu (Chen Duxiu, 1879&#8211;1942), a leader of the New Culture "
     "and May Fourth movements and, from 1921, co-founder and first general "
     "secretary of the Chinese Communist Party. The Comintern made him the "
     "scapegoat for the 1927 disaster he had been made to preside over; he was "
     "expelled in 1929, joined Trotsky&#8217;s opposition, and died in "
     "obscurity. Isaacs, himself a Trotskyist, treats him sympathetically."),
    ("his famous magazine, *New Youth*",
     "<i>New Youth</i> (Xin Qingnian), founded by Chen in 1915, was the leading "
     "organ of the New Culture Movement, championing vernacular writing, "
     "science, and democracy against Confucian tradition and drawing a whole "
     "generation &#8212; the young Mao among its readers &#8212; toward radical "
     "ideas."),
    ("the infamous Twenty-One Demands of 1915",
     "A set of secret demands Japan pressed on China in January 1915 that would "
     "have reduced it to a near-protectorate, extending Japanese control over "
     "Shantung, Manchuria, and China&#8217;s finances and police. China "
     "conceded a reduced version under ultimatum, and the demands became a "
     "lasting nationalist grievance."),
    ("The shining phrases of Woodrow Wilson",
     "Woodrow Wilson (1856&#8211;1924), U.S. president 1913&#8211;21, whose "
     "wartime rhetoric of national self-determination raised hopes across the "
     "colonial world. At the Paris Peace Conference he acquiesced in handing "
     "Germany&#8217;s Shantung holdings to Japan rather than returning them to "
     "China."),
    ("On May 4, 1919",
     "The May Fourth movement began with student demonstrations in Peking on "
     "May 4, 1919, against the Versailles decision to grant Japan the former "
     "German rights in Shantung. It broadened into a nationwide anti-imperialist "
     "and cultural awakening &#8212; strikes, boycotts, and a turn among "
     "intellectuals toward Marxism &#8212; that this chapter takes as the "
     "opening of the &#8220;second Chinese revolution.&#8221;"),
    ("syndicalism",
     "Syndicalism, a current of revolutionary trade-unionism holding that "
     "workers should overthrow capitalism and run society through their own "
     "unions, chiefly by the general strike, rather than through political "
     "parties."),
    ("General Chen Chiung-ming permitted him",
     "Chen Chiung-ming (Chen Jiongming, 1878&#8211;1933), the Cantonese general "
     "who gave Sun "
     "Yat-sen a base in Canton and then, in June 1922, turned on him and drove "
     "him out. A federalist opposed to Sun&#8217;s centralizing nationalism, he "
     "was finally expelled from Kwangtung in 1925."),
    ("Others, like Li Ta-chao",
     "Li Ta-chao (Li Dazhao, 1889&#8211;1927), head librarian at Peking "
     "University and, with Chen Tu-hsiu, co-founder of the Chinese Communist "
     "Party. Seized in a raid on the Soviet embassy in Peking, he was hanged by "
     "the warlord Chang Tso-lin in April 1927."),
    ("and Chang Kuo-tao",
     "Chang Kuo-tao (Zhang Guotao, 1897&#8211;1979), a founding Communist and "
     "delegate to the 1921 congress, later a military rival of Mao. He broke "
     "with the party and defected to the Kuomintang in 1938."),
    ("laid before Sun Yat-sen by Dalin",
     "Sergei Dalin (1902&#8211;1985), a young Soviet envoy sent in 1922 by the "
     "Young Communist International, the Comintern&#8217;s youth organization. "
     "His mission put the first proposal for a Communist&#8211;Kuomintang "
     "alliance directly to Sun, who refused a two-party bloc."),
    ("Maring, the first delegate of the Comintern in China",
     "&#8220;Maring&#8221; was the alias of Hendricus Sneevliet "
     "(1883&#8211;1942), a Dutch Communist who had organized the left in the "
     "Dutch East Indies. As the Comintern&#8217;s first agent in China he "
     "devised the &#8220;bloc within&#8221; &#8212; Communists joining the "
     "Kuomintang as individuals &#8212; the policy this book indicts. He was "
     "later shot by the Nazis in occupied Holland."),
    ("participated in the Saraket Islam",
     "Sarekat Islam (&#8220;Islamic Union&#8221;), a mass Indonesian "
     "organization founded in 1912 against Dutch colonial rule. Maring had "
     "helped build Communist influence in its left wing &#8212; the model he "
     "now proposed to apply in China."),
    ("the military strength of the warlord Wu Pei-fu",
     "Wu Pei-fu (Wu Peifu, 1874&#8211;1939), the dominant militarist of North "
     "China in the early 1920s, backed by British interests. His troops carried "
     "out the February 7, 1923, massacre of the Peking&#8211;Hankow railway "
     "strikers described below."),
    ("the notorious pro-Japanese Anfu clique",
     "The Anfu clique was the pro-Japanese faction around the militarist Tuan "
     "Chi-jui that controlled the Peking government in 1918&#8211;20, named for "
     "the Anfu Club through which it was organized."),
    ("sent by the Chita government and the Irkutsk Bureau of the Comintern",
     "The Chita government (the Far Eastern Republic, a buffer state the "
     "Soviets maintained in Siberia, 1920&#8211;22) and the Comintern&#8217;s "
     "Irkutsk Bureau were Moscow&#8217;s early channels to East Asia. The "
     "&#8220;Irkutsk line&#8221; first backed the warlord Wu Pei-fu, before the "
     "Comintern turned to Sun Yat-sen."),
    ("sent Adolph Joffe",
     "Adolf Joffe (1883&#8211;1927), a senior Soviet diplomat. The joint "
     "statement he issued with Sun in Shanghai on January 26, 1923 &#8212; the "
     "Sun&#8211;Joffe Manifesto &#8212; sealed the Soviet&#8211;Kuomintang "
     "entente, Moscow conceding that China was not ready for Communism while "
     "pledging support for national unification."),
    ("When Michael Borodin",
     "Mikhail Borodin (1884&#8211;1951), the chief Soviet adviser to the "
     "Kuomintang from 1923. He reorganized the party on Bolshevik lines and "
     "steered its alliance with the Communists; when the alliance collapsed in "
     "1927 he was recalled to Moscow, and he died in one of Stalin&#8217;s "
     "labor camps in 1951."),
    ("the Whampoa Military Academy",
     "Founded near Canton in May 1924 with Soviet funds and advisers to build a "
     "loyal Nationalist officer corps. Its first commandant was Chiang "
     "Kai-shek, and it became the power base from which he came to dominate the "
     "army and the party."),
    ("thoroughly reorganized at its first national congress in January 1924",
     "This was the Kuomintang&#8217;s First National Congress. Its admission of "
     "Communists as individual members inaugurated the &#8220;united "
     "front&#8221; &#8212; the alliance of the Nationalists, the Communists, and "
     "Moscow whose course this book traces."),
    ("to borrow Wang Ching-wei’s summary",
     "Wang Ching-wei (Wang Jingwei, 1883&#8211;1944), a leader of the "
     "Kuomintang left and Chiang&#8217;s rival for Sun&#8217;s mantle. He "
     "headed the Wuhan government in 1927 and, from 1940, the "
     "Japanese-sponsored puppet regime at Nanking until his death."),
    ("the Washington Conference of 1921–22",
     "The Washington Conference (November 1921&#8211;February 1922) produced "
     "naval-limitation and Pacific treaties among the powers, with a "
     "Nine-Power Treaty affirming China&#8217;s territorial integrity in "
     "principle. Chinese nationalists saw it as merely regularizing joint "
     "foreign domination &#8212; Wang Ching-wei&#8217;s &#8220;co-operative "
     "slow encroachment.&#8221;"),
    ("supported by Liao Chung-kai",
     "Liao Chung-kai (Liao Zhongkai, 1877&#8211;1925), the most left-wing of "
     "Sun&#8217;s close aides and a champion of the Soviet alliance and the "
     "worker&#8211;peasant movement. He was assassinated by Kuomintang "
     "rightists in August 1925."),
    ("the massacre of February 7, 1923, at Chengchow, Honan",
     "The &#8220;February 7&#8221; massacre: when railwaymen on the "
     "Peking&#8211;Hankow line moved to found a general union, the warlord Wu "
     "Pei-fu had the strike crushed by force, with dozens killed. It became a "
     "landmark in the labor movement&#8217;s calendar of martyrs. "
     "(Isaacs&#8217;s figure of sixty dead runs higher than most later "
     "estimates, which put it in the thirties.)"),
    ("cradled in Haifeng, in the East River districts of Kwantung, by Peng Pai",
     "Peng Pai (1896&#8211;1929), who built China&#8217;s first mass peasant "
     "associations at Haifeng from 1922 and in 1927 led a short-lived Haifeng "
     "&#8220;soviet&#8221; &#8212; a peasant-run local government on the Russian "
     "model."),
    ("Britain’s Labour prime minister, Ramsay Macdonald",
     "Ramsay MacDonald (1866&#8211;1937) headed Britain&#8217;s first Labour "
     "government (January&#8211;November 1924). His silence, for Isaacs, shows "
     "that a Labour ministry pursued the same imperial policy in China as its "
     "Conservative predecessors."),
    ("G. Voitinsky, Comintern delegate in China",
     "Grigori Voitinsky (1893&#8211;1953), the Comintern envoy who had helped "
     "the Chinese Communists organize in 1920&#8211;21 and now, Isaacs argues, "
     "worked to subordinate the labor movement to Kuomintang leadership."),
    ("It was the afternoon of May 30.",
     "The May Thirtieth incident: on May 30, 1925, British-officered police in "
     "Shanghai&#8217;s International Settlement fired on a crowd protesting the "
     "killing of a Chinese mill worker, killing twelve. The outrage set "
     "off a nationwide wave of strikes and boycotts &#8212; the May Thirtieth "
     "movement &#8212; that carried the revolution into its mass phase."),
    ("When they passed the Shakee Road Bridge",
     "The Shakee (Shaji) massacre of June 23, 1925: British and French troops "
     "on Shameen, the foreign concession island at Canton, fired across the "
     "canal on an anti-imperialist march, killing fifty-two. It triggered the "
     "long Canton&#8211;Hong Kong strike and boycott described next."),
    ("A boycott of British goods and a general strike were immediately declared.",
     "The Canton&#8211;Hong Kong strike and boycott ran about sixteen months, "
     "from June 1925 to October 1926 &#8212; among the longest strikes anywhere "
     "to that time. It paralyzed British Hong Kong and became the mass base on "
     "which the Kuomintang consolidated its power in the south."),
    ("the Yunnanese generals, Yang Hsi-min and Liu Chen-han",
     "Yang Hsi-min (Yang Ximin) and Liu Chen-han (Liu Zhenhuan) commanded "
     "Yunnanese mercenary armies "
     "quartered in Canton who cooperated with the Kuomintang for their own "
     "advantage. When they turned against it they were routed by Whampoa cadets "
     "and armed workers in June 1925."),
    ("But Whitehall saw more wisely",
     "&#8220;Whitehall,&#8221; the London street lined with government "
     "ministries, stands for the British government itself."),
]


def main():
    reading = {c: open(os.path.join(ROOT, "out", "%s_reading.md" % c),
                       encoding="utf-8").read() for c in ("ch02", "ch03")}
    batch = {"notes": {}}
    for chid, notes in (("ch02", CH02), ("ch03", CH03)):
        seen = set()
        out = []
        for anchor, body in notes:
            if reading[chid].count(anchor) == 0:
                sys.exit("%s: anchor NOT FOUND: %r" % (chid, anchor))
            if reading[chid].count(anchor) > 1:
                sys.exit("%s: anchor NOT UNIQUE: %r" % (chid, anchor))
            if anchor in seen:
                sys.exit("%s: duplicate anchor: %r" % (chid, anchor))
            seen.add(anchor)
            out.append({"anchor": anchor, "note": body, "ed": True})
        batch["notes"][chid] = out
        print("%s: %d editorial notes" % (chid, len(out)))

    dest = os.path.join(ROOT, "scratch")
    os.makedirs(dest, exist_ok=True)
    path = os.path.join(dest, "ch0203_editorial_notes.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("wrote", path)


if __name__ == "__main__":
    main()
