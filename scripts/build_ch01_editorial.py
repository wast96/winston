#!/usr/bin/env python3
"""Assemble the EDITORIAL note batch for ch01 (the reader-facing layer, per
CLAUDE.md's generous density model). Each note carries "ed": true so the
builder numbers it in the roman stream (i, ii, iii). Anchors are given as
plain-text hints and resolved to the exact reading.md slice; the resolver
refuses a hint that is missing, not unique, or already claimed by an author
note (apparatus_merge dedups by anchor, so a collision would silently drop
the editorial note).

Writes scratch/ch01_editorial_notes.json.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
READING = os.path.join(ROOT, "out", "ch01_reading.md")

# (anchor hint, note body XHTML). Order is irrelevant: the builder numbers the
# roman stream by position in the text.
NOTES = [
    ("toward a solution on the battlefields of the class struggle",
     "Isaacs writes as a Marxist, and specifically from the Trotskyist "
     "opposition to Stalin; the framing of Chinese history as a sequence of "
     "class struggles driving toward revolution is his lens throughout, and "
     "later notes flag where it shapes a factual claim."),
    ("the “Asiatic mode of production,”",
     "Karl Marx’s term for societies in which a centralized state, controlling "
     "irrigation and public works, extracts surplus from largely "
     "self-sufficient villages, supposedly leaving them static for centuries. "
     "It was debated among Marxists in the 1920s&#8211;30s, later suppressed "
     "in the USSR, and is rejected by most historians today (a real term of "
     "Marx’s; its application to China is contested)."),
    ("the attempted reforms of Wang Mang",
     "Wang Mang (c. 45 BCE&#8211;23 CE) seized the throne from the Han dynasty "
     "(206 BCE&#8211;220 CE, China’s formative empire) and ruled as the Xin "
     "dynasty (9&#8211;23 CE), decreeing a sweeping nationalization of land "
     "before he was overthrown. His usurpation fell between the Western and "
     "Eastern Han, not strictly &#8220;after the fall of the Han&#8221; as "
     "Isaacs has it (broadly corroborated; the dating is loose)."),
    ("those advocated by Wang An-shih",
     "Wang Anshi (1021&#8211;1086), chief councillor of the Song, whose New "
     "Policies of 1069 included state farm loans and price stabilization. They "
     "came more than a century into the Song (Isaacs’s &#8220;Sung,&#8221; "
     "960&#8211;1279), not at its rise after the T&#8217;ang (618&#8211;907) "
     "(a real reformer; the timing is compressed)."),
    ("The Manchus came to power",
     "The Manchus, a people from beyond the Great Wall in the northeast, "
     "conquered China in 1644 and ruled as the Ch&#8217;ing (Qing) dynasty "
     "until 1912 &#8212; the last imperial dynasty. As non-Han rulers they "
     "imposed the queue and were the target of the anti-dynastic, "
     "ethnic-nationalist feeling Isaacs describes."),
    ("European contacts with Cathay",
     "&#8220;Cathay&#8221; is an old European name for China, from the Khitan "
     "people; by the twentieth century it was archaic and literary."),
    ("divided the Celestial Empire",
     "&#8220;The Celestial Empire&#8221; was a nineteenth-century Western "
     "epithet for imperial China, echoing the emperor’s title as the Son of "
     "Heaven; Isaacs uses it with irony."),
    ("the Opium Wars of 1842 and 1858",
     "The two wars Britain (joined by France in the second) fought to force "
     "open the China trade and protect the opium traffic: the First Opium War "
     "(1839&#8211;42), ended by the Treaty of Nanking, and the Second, or "
     "&#8220;Arrow,&#8221; War (1856&#8211;60), whose Treaties of Tientsin "
     "were signed in 1858. Isaacs dates them by those treaties, not by the "
     "fighting (corroborated)."),
    ("Chinese woven cloth (nankeens)",
     "A durable yellowish cotton cloth woven in China and named for Nanking, "
     "once a staple export until British machine-made cottons destroyed the "
     "trade."),
    ("set up the system of extraterritoriality",
     "The treaty privilege by which foreigners in China answered to their own "
     "countries’ laws and courts, not Chinese law, and were exempt from "
     "Chinese taxation &#8212; a central grievance of the nationalist movement, "
     "not abolished until 1943."),
    ("the different foreign “spheres of influence,”",
     "Regions where one power claimed priority for its railways, loans, and "
     "mines &#8212; Britain in the Yangtze valley, Japan in the northeast, "
     "France in the far south, Russia in Manchuria &#8212; stopping short of "
     "outright colonies."),
    ("arrived at Canton laden with silver",
     "Canton (modern Guangzhou), the great southern port and, before 1842, the "
     "only city where Westerners could trade; later the base of the "
     "overseas-Chinese and revolutionary movements. (On the older spellings "
     "Isaacs uses throughout &#8212; Canton, Peking, Nanking &#8212; see the "
     "note on this edition; the modern pinyin forms are in the glossary.)"),
    ("the port merchants and mandarins",
     "&#8220;Mandarin,&#8221; from Portuguese, was the Western name for a "
     "Chinese scholar-official of the imperial bureaucracy, ranked by "
     "examination degree and by the colored button on his cap (the "
     "&#8220;mandarin’s button&#8221; Isaacs mentions below)."),
    ("Members of the co-hongs",
     "The Cohong (<i>gonghang</i>) was the guild of licensed Chinese merchant "
     "houses at Canton that, before 1842, monopolized all trade with "
     "Westerners; its members grew immensely rich and buffered the government "
     "from the foreigners."),
    ("worth as much as 200,000 taels",
     "The tael (abbreviated Tls. in the trade tables later in the chapter) was "
     "a Chinese unit of silver by weight &#8212; the customs, or Haikwan, tael "
     "was about 37.8 grams &#8212; not a coin, used for large sums and "
     "government accounts; 200,000 taels denotes a very great fortune."),
    ("the class of compradores",
     "A comprador (from Portuguese, &#8220;buyer&#8221;) was the Chinese "
     "manager who ran a foreign firm’s dealings with the local market. Isaacs "
     "makes this class &#8212; brokers for foreign capital, often also "
     "landlords &#8212; central to his account of how imperialism fastened "
     "onto Chinese society (a real social category; the emphasis is his)."),
    ("crystallized during the Taiping Rebellion",
     "The Taiping Rebellion (1850&#8211;1864), a quasi-Christian mass uprising "
     "that grew from the &#8220;God-worshippers&#8221; of the far south, took "
     "Nanking in 1853 as its &#8220;Heavenly Capital,&#8221; and held much of "
     "the Yangtze valley until 1864. With some 20&#8211;30 million dead it was "
     "among the deadliest wars in history; Isaacs’s &#8220;eleven years&#8221; "
     "counts from the Nanking capital to the fall (corroborated)."),
    ("swept northward from Kwangsi",
     "Kwangsi (modern Guangxi), the far-southern province where Hung’s "
     "God-worshippers first rose."),
    ("Hung Tsui-chuen",
     "Hong Xiuquan (1814&#8211;1864), the Taiping leader, who after a series "
     "of visions proclaimed himself the younger brother of Jesus and, at "
     "Nanking, &#8220;Heavenly King&#8221; (<i>Tianwang</i>); he died as the "
     "city fell in 1864. Isaacs’s spelling &#8220;Hung Tsui-chuen&#8221; is "
     "idiosyncratic even for the 1930s (standard Wade-Giles: Hung "
     "Hsiu-ch&#8217;&#252;an)."),
    ("the old Ming costumes restored",
     "The Ming (1368&#8211;1644) was the last Han-Chinese dynasty before the "
     "Manchu conquest; restoring Ming dress and letting the hair grow "
     "(rejecting the queue) proclaimed a Han restoration against the Manchus."),
    ("the queue, badge of subjection",
     "The queue &#8212; shaved forehead and long braid &#8212; was imposed on "
     "Chinese men by the Manchus after 1644 on pain of death; cutting it off "
     "was itself an act of rebellion, which is why the Taipings and the 1911 "
     "revolutionaries did so."),
    ("The Christian General Gordon",
     "Charles George &#8220;Chinese&#8221; Gordon (1833&#8211;1885), the "
     "British officer who led the Western-officered &#8220;Ever-Victorious "
     "Army&#8221; against the Taipings and was later killed at Khartoum. "
     "Isaacs’s sardonic phrasing underscores that Christian powers crushed the "
     "Taipings’ own Christianity."),
    ("Tseng Kuo-fan",
     "Zeng Guofan (1811&#8211;1872), the Hunan official whose provincial army "
     "broke the Taiping Rebellion; a pillar of the landed gentry and of the "
     "&#8220;self-strengthening&#8221; movement (the post-1860 drive to adopt "
     "Western arms and industry while preserving the old order) that followed."),
    ("and Li Hung-chang",
     "Li Hongzhang (1823&#8211;1901), the most powerful Chinese official of "
     "the late Qing: Taiping-war commander, founder of arsenals, steamship and "
     "mining companies, and negotiator of the treaties ending the wars with "
     "Japan and the Boxers. Isaacs casts him as the &#8220;compradore-in-chief"
     "&#8221; who launched China’s first modern industries."),
    ("the anti-Manchu Triads",
     "The Triads (<i>Tiandihui</i>, &#8220;Heaven and Earth Society&#8221;) "
     "were sworn brotherhoods, part secret society and part criminal "
     "fraternity, with a standing &#8220;oppose the Qing, restore the "
     "Ming&#8221; tradition. Their Small Sword Society held the walled Chinese "
     "city of Shanghai from 1853; the foreign guns Isaacs mentions intervened "
     "in 1854."),
    ("the Summer Palace",
     "The Yuanmingyuan, the emperors’ vast garden-palace outside Peking, "
     "looted and burned by British and French troops in October 1860 to force "
     "China’s submission &#8212; a byword for imperialist vandalism."),
    ("occupied Cambodia and Annam",
     "Annam is an old Western name for central Vietnam; with Cambodia and "
     "Tonkin it became part of French Indochina in the 1880s."),
    ("with the Meiji Restoration",
     "The Meiji Restoration of 1868 overthrew Japan’s shogunate and launched "
     "rapid, state-led industrialization and military modernization; within a "
     "generation Japan defeated China (1895) and Russia (1905). Isaacs "
     "contrasts Japan’s success with China’s blocked development."),
    ("established in North Manchuria",
     "Manchuria is the northeastern region of China (the Manchu homeland), rich "
     "in land and minerals and coveted by both Russia and Japan; Japan would "
     "seize it in 1931."),
    ("In 1894 the new island power",
     "The First Sino-Japanese War (1894&#8211;95), fought chiefly over Korea, "
     "ended in a crushing Chinese defeat that exposed the failure of Qing "
     "&#8220;self-strengthening&#8221; and set off the scramble for "
     "concessions."),
    ("The Treaty of Shimonoseki",
     "The treaty of April 17, 1895 ending the Sino-Japanese War: China "
     "recognized Korea’s independence, ceded Taiwan and the Liaotung Peninsula "
     "(soon returned under Russian, French, and German pressure), paid a "
     "200-million-tael indemnity, and &#8212; as Isaacs stresses &#8212; opened "
     "China to foreign-owned factories, a right extended to all the powers by "
     "most-favored-nation clauses (corroborated)."),
    ("Adam Smith, John Stuart Mill, Herbert Spencer, and Thomas Huxley",
     "These British liberal and evolutionary thinkers reached Chinese reformers "
     "mainly through the celebrated translations of Yen Fu (Yan Fu) around 1900; "
     "the social-Darwinist ideas of Spencer and Huxley &#8212; struggle, "
     "adaptation, survival &#8212; especially marked the reform generation."),
    ("gained the ear of the young emperor Kwang Hsu",
     "The Kuang-hs&#252;, or Guangxu, Emperor (reigned 1875&#8211;1908) backed "
     "the 1898 reforms and was placed under palace arrest by the Empress "
     "Dowager for the rest of his life; he died in 1908, a day before her "
     "(forensic tests in 2008 confirmed arsenic poisoning)."),
    ("the famous “Hundred Days” of reform",
     "The Hundred Days’ Reform (June&#8211;September 1898): a burst of "
     "modernizing edicts under Guangxu, ended by the Empress Dowager’s coup. "
     "Isaacs uses it to show the impotence of reform imposed from above."),
    ("resistance to the reforms crystallized around the Empress Dowager",
     "Cixi (1835&#8211;1908), the Empress Dowager who dominated the Qing court "
     "for nearly half a century. She crushed the 1898 reforms, later backed the "
     "Boxers, and only then conceded halting constitutional change &#8212; "
     "Isaacs’s &#8220;last vigorous representative&#8221; of the dynasty."),
    ("Kang Yu-wei and Liang Chi-chao",
     "Kang Youwei (1858&#8211;1927), the scholar who recast Confucius as a "
     "reformer and led the 1898 &#8220;Hundred Days,&#8221; and his brilliant "
     "disciple Liang Qichao (1873&#8211;1929), China’s most influential "
     "journalist-reformer. Both fled abroad after the coup and thereafter "
     "argued for constitutional monarchy, not revolution &#8212; which is why "
     "Isaacs later shows students turning away from Kang."),
    ("the I Ho Chuan (Fists for the Protection of Public Peace)",
     "The Yihequan, &#8220;Boxers United in Righteousness,&#8221; a north-China "
     "martial-arts movement whose anti-foreign, anti-Christian rising the court "
     "turned outward in 1900; Isaacs’s gloss &#8220;Fists for the Protection of "
     "Public Peace&#8221; is a loose rendering of the name."),
    ("under the Boxer Protocol of 1901",
     "The settlement of September 7, 1901 imposed by the powers after the Boxer "
     "Rising: an indemnity of 450 million taels (about US $333 million, payable "
     "with interest over 39 years), foreign legation guards, and razed forts. "
     "Isaacs’s &#8220;U.S. $350,000,000&#8221; rounds the figure up slightly "
     "(substantially corroborated)."),
    ("a war fought across Chinese territory by Russia and Japan",
     "The Russo-Japanese War (1904&#8211;05), fought largely in Manchuria "
     "&#8212; Chinese soil &#8212; over rival claims to Manchuria and Korea; "
     "Japan’s victory was sealed by the Treaty of Portsmouth without China’s "
     "consent."),
    ("Russia’s 1905 revolution",
     "The 1905 revolution against the Russian tsar, touched off partly by "
     "defeat by Japan; its example encouraged constitutional agitation in "
     "China and pushed the Qing court toward concessions."),
    ("resembling the zemstvos under the czar in Russia",
     "The zemstvos were elected local assemblies in tsarist Russia with real "
     "but tightly limited powers; Isaacs likens the Qing’s 1910 provincial "
     "assemblies to them for his mostly Western readers."),
    ("another exile, Sun Yat-sen",
     "Sun Yat-sen (1866&#8211;1925), the Canton-born, Hawaii- and Hong "
     "Kong-educated revolutionary regarded as the founder of the Chinese "
     "Republic. His Revolutionary Alliance (Tungmenghui) led the anti-Manchu "
     "movement; he was briefly first provisional president in 1912 and later "
     "rebuilt the Kuomintang, whose fate is the subject of this book."),
    ("the Miao tribes in the southwest and the Muslims in the northwest",
     "The Miao (Hmong) are a non-Han hill people of south and southwest China; "
     "the &#8220;Muslims&#8221; are the Hui and other Muslim communities of the "
     "northwest. Both mounted major revolts in the mid-nineteenth century amid "
     "the general upheaval."),
    ("especially in Hunan, Hupeh, and Szechwan",
     "Three central and western provinces &#8212; modern Hunan, Hubei, and "
     "Sichuan &#8212; where the campaign to keep the railways in Chinese hands "
     "was strongest, and where the 1911 revolt would break out."),
    ("The revolution of 1911",
     "The Xinhai Revolution of 1911, which toppled the Qing and founded the "
     "Republic on January 1, 1912. Isaacs’s theme is that it was a &#8220;tiny "
     "push&#8221; that changed the label but not the social order, leaving "
     "power to provincial militarists (a real revolution; the dismissive "
     "reading is his own)."),
    ("power passed into the hands of provincial or regional satraps",
     "The warlords: after Yuan Shih-kai’s death in 1916 China fragmented among "
     "regional militarists with their own armies and taxes, often backed by "
     "rival foreign powers &#8212; the &#8220;warlord era&#8221; (c. "
     "1916&#8211;1928) that is the backdrop to the revolution Isaacs will "
     "describe."),
    ("compelled to give way to Yuan Shih-kai",
     "Yuan Shikai (1859&#8211;1916), the Qing army’s strongest general, who "
     "secured the emperor’s abdication and then supplanted Sun as president in "
     "1912, ruling as a dictator and briefly proclaiming himself emperor "
     "(1915&#8211;16). His maneuvering is Isaacs’s prime example of the 1911 "
     "revolution’s betrayal."),
    ("his party, the Kuomintang",
     "The Kuomintang (Guomindang, Nationalist Party), formed in 1912 out of "
     "Sun Yat-sen’s Revolutionary Alliance. It is the central actor in this "
     "book: allied with the Communists and Moscow from 1923, it turned on them "
     "in 1927 &#8212; the &#8220;tragedy&#8221; of Isaacs’s title."),
    ("a direct result of the Great War",
     "The First World War (1914&#8211;18). With the industrial powers absorbed "
     "in Europe, foreign competition in Chinese markets eased and native "
     "industry surged, as Isaacs details in the figures that follow."),
    ("A telegraph line was laid between Shanghai and Tientsin",
     "Tientsin (modern Tianjin), the great treaty port and gateway to Peking on "
     "the northern coast."),
    ("the revolt of the garrison at Wuchang",
     "The Wuchang Uprising of October 10, 1911 &#8212; a mutiny of the "
     "New Army garrison at Wuchang, on the Yangtze &#8212; touched off the "
     "Xinhai Revolution; the date is still marked as the Republic’s &#8220;Double "
     "Tenth.&#8221;"),
    ("silk from the Kiangsu districts",
     "Kiangsu (modern Jiangsu), the wealthy lower-Yangtze province around "
     "Shanghai and Nanking, long a center of silk production."),
    ("the Canton-Hankow Railway",
     "Hankow (part of modern Wuhan, with Hanyang and Wuchang), the great "
     "commercial city where the Han river meets the Yangtze; the projected "
     "Canton&#8211;Hankow trunk line would tie south China to the Yangtze. "
     "Hankow later becomes the seat of the left-Kuomintang government at the "
     "center of this book."),
]


def norm(s):
    return (s.replace("’", "'").replace("‘", "'")
             .replace("“", '"').replace("”", '"'))


def main():
    raw = open(READING, encoding="utf-8").read()
    nraw = norm(raw)
    # anchors already claimed by author notes (collision would drop the note)
    existing = set()
    npath = os.path.join(ROOT, "notes.json")
    if os.path.exists(npath):
        for e in json.load(open(npath, encoding="utf-8")).get("ch01", []):
            existing.add(e["anchor"])

    out = []
    seen = set()
    problems = 0
    for hint, body in NOTES:
        h = norm(hint)
        i = nraw.find(h)
        if i < 0:
            print("NOT FOUND: %r" % hint); problems += 1; continue
        if nraw.find(h, i + 1) != -1:
            print("NOT UNIQUE: %r" % hint); problems += 1; continue
        anchor = raw[i:i + len(h)]
        if anchor in existing or anchor in seen:
            print("COLLISION with an existing/other anchor: %r" % anchor)
            problems += 1
            continue
        seen.add(anchor)
        out.append({"anchor": anchor, "note": body, "ed": True})
    if problems:
        sys.exit("%d anchor problem(s); nothing written" % problems)

    dest = os.path.join(ROOT, "scratch")
    os.makedirs(dest, exist_ok=True)
    path = os.path.join(dest, "ch01_editorial_notes.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump({"notes": {"ch01": out}}, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("wrote %s (%d editorial notes)" % (path, len(out)))


if __name__ == "__main__":
    main()
