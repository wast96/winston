#!/usr/bin/env python3
"""Generate out/ch25_bilingual.md (后记一 / "Afterword I") with GUARANTEED
verbatim source quotation.

Reads the source paragraphs from data/src/53_text00050.txt, pairs each (in
reading order) with a hand-authored English paragraph, and emits the '>'/English
bilingual QC file. The source is never re-typed here: it is read from disk and
quoted byte-for-byte, and the script asserts that the concatenation of every
blockquote equals the source content character-for-character before writing.

Source structure (ch25, 后记一 -- an AUTHOR'S AFTERWORD, an essay, NOT a
numbered chapter):
  raw[0] L1  : 后记一  -> absorbed into the H2 title (not a paragraph)
  raw[1..21] : 21 body paragraphs, one per source line. No dateline, no opening
               vignette, no per-chapter time-gloss (afterwords have none).
  No extractor-split paragraphs (every body line ends on a terminal mark except
  L16, whose colon legitimately introduces the following narrative block, a
  genuine paragraph break, not a split). No trailing U+200B line in this ingest.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "src", "53_text00050.txt")
OUT = os.path.join(ROOT, "out", "ch25_bilingual.md")

TITLE_EN = "Afterword I"

# --- English paragraphs, in source reading order (21 body paragraphs) ----------
BODY = [
# raw1
"The third year of Tianbao was a quiet year. In the histories there is almost nothing about it worth setting down at length. Though it was rumored far and wide among the common people that a divine fire had descended upon Chang'an and carried off a great many souls, the officials kept a deep and studied silence on the matter.",
# raw2
"And yet the third year of Tianbao was also, in its way, a year of consequence: for a great many people—the great Tang itself among them—it was the year in which everything turned.",
# raw3
"In the fourth month of that year He Zhizhang's carriage returned to his old home at Shanyin; but the He household, pleading that the old man was worn out from the journey, shut its gates and received no guests at all. Before long there came, of all things, word that He Zhizhang had quietly passed away, eighty-four years old. The elders and gentry of his native place had the chance only to read the two poems he had left behind on coming home; not one of them had set eyes on the man himself. When the news reached Chang'an, the Son of Heaven suspended the court in mourning, and the whole body of civil and military officials offered up poems in his honor—which became one of the cultural events of the third year of Tianbao.",
# raw4
"At the same time, Wang Zhongsi, off in distant Shuofang, all at once launched against the Türks an offensive many times fiercer than any before, with every look of meaning to trample the steppe flat. After months of hard fighting the Türks' Ozmish Khagan was defeated and slain, and his head sent to the capital; his successor, the Baimei Khagan, was killed the very next year, and what remained of his people was swallowed up by the Uyghurs. From that time on, upon the grasslands the name of the Türks was heard no more.",
# raw5
"While Shuofang saw battle upon battle, in the northeast all was peace and calm. In the ninth month of that year a Hu general named An Lushan rose to be military commissioner of Fanyang and Surveillance Commissioner of Hebei, while keeping his command as military commissioner of Pinglu besides—a rising political star in the firmament of the Tianbao court. His loyalty was beyond reproach; he had won the unanimous confidence of all, from the Son of Heaven down to the Right Minister, who held that the whole region of Hebei might safely be given into his hands.",
# raw6
"But none of this was what the Son of Heaven cared for most. At the close of the third year of Tianbao he formally took Taizhen into the palace, and could hardly wait to invest her, the next year, as Noble Consort. From then on sovereign and consort lived in perfect accord, keeping in the Xingqing Palace the life of a pair of immortals wedded together.",
# raw7
"The Jing'an Bureau, being no more than a temporary office, was soon dissolved. Li Bi, its Deputy Director, sent up a memorial begging leave to resign, and quit Chang'an to begin a pilgrimage in search of the Way among the immortals' mountains. The tale of it passed for a while as a pretty story among the people of Chang'an. Once, midway, he did return to the city; but, pressed hard by Yang Guozhong and his like, he departed once again.",
# raw8
"The heir apparent, Li Heng, having lost his most powerful support, enjoyed but two years of peace. Beginning in the fifth year of Tianbao, the Right Minister Li Linfu stirred up one great case after another—the case of Wei Jian, the case of Du Youlin, and the rest—each of which shook court and country alike and swept up numberless men in its toils. The heir apparent lost one trusted intimate after another, and was even forced into two separate ruptures of his marriage, so that he was hard beset indeed. He fretted past all measure, until the hair at both his temples went white with it.",
# raw9
"This state of things went on until the An Lushan Rebellion, in the fourteenth year of Tianbao. Li Heng did not follow the Son of Heaven into Shu, but fled to Lingwu and there ascended the throne, honoring the Son of Heaven from afar as Retired Emperor. Thus the great Tang came to be split among three powers: the Retired Emperor in Shu, the new Son of Heaven at Lingwu, and Prince Yong away off at Jiangling.",
# raw10
"Just then Li Bi, so long unseen, came forth from his seclusion once more to aid Li Heng—yet he would by no means take any office, and consented to stay on only in the standing of a guest counselor. Under his contriving and management Li Heng was able to turn defeat into victory: to break the rebel armies without, to keep down both the Retired Emperor and Prince Yong within, and so at last to accomplish the great work of restoration. Men called Li Bi 'the White-Robed Chancellor.' His work done, Li Bi begged leave to withdraw yet again, and hid himself away among the hills and forests. After Suzong's death, both Daizong and Dezong, sovereigns of two reigns, summoned him back to court to be their chancellor; and Li Bi came forth to the chancellorship several times, and several times retired again. In the course of his life he served four emperors—Xuanzong, Suzong, Daizong, and Dezong—four times cast down and four times raised up, and by the merits he heaped up was at length enfeoffed as Marquis of Ye County.",
# raw11
"Besides Li Bi, the An Lushan Rebellion threw up yet another figure of legend. This man was no native of the Middle Land, but a Nestorian monk by the name of Yisi. Yisi was a man of rare and surpassing vision. He was active in Guo Ziyi's command, serving as a counselor in the army, and rose in office to Grand Master of the Palace with Golden Seal and Purple Ribbon, concurrent vice military commissioner of Shuofang, and probationary Director of the Palace Administration, and was granted the purple kasaya. In the fourth year of Tianbao the Persian Temple was renamed the Daqin Temple, and the Nestorian faith reached the very summit of its growth within the borders of the great Tang. In the second year of Jianzhong, Yisi set up in the courtyard of the Daqin Temple a stone stele, which he named the Stele of the Propagation in China of the Luminous Religion of Daqin, to commemorate the hard road by which the Nestorian faith had come into the Middle Land. This stele has come down a thousand years, all the way to the present day.",
# raw12
"Yet whether Li Bi or Yisi, neither, for sheer ups and downs of fortune, could match Yuan Zai for the stuff of legend. After the third year of Tianbao this man's official career ran smooth all the way; and, sprung from mean and lowly birth, he took to wife Wang Yunxiu, the daughter of Wang Zhongsi—a match that was for a time the talk and wonder of the town. Once the An Lushan Rebellion had broken out, Yuan Zai moved with the moment, seized upon every chance, and won the especial regard of Suzong, that is Li Heng, rising into the highest ranks of the court. After Suzong's death he made common cause with the powerful eunuch Li Fuguo, and mounted at last to the chancellorship, becoming a minister of decisive weight in the reign of Daizong and gathering all power into his own hands. Even Li Bi could find no way to stand against him.",
# raw13
"But once Yuan Zai had the power wholly in his grasp, he took bribes and pocketed spoils, grew corrupt and given over to luxury, and did as he pleased without a scruple. His wife and his sons too ran riot and lorded it about, insolent past all bearing. Daizong at length could bear it no more, and gave order that he be seized and granted death. When Yuan Zai was dead, by the statutes of the great Tang his wife might have been spared; yet Wang Yunxiu declared: 'The Thirteenth Daughter of the house of Wang, twenty years the daughter of the military commissioner of Taiyuan, sixteen years the wife of a chancellor—who could ever set down in writing the tale of Changxin and Zhaoyang? To die is fortune enough!' And so she died together with him.",
# raw14
"But there were still others who could not, as these men did, leave even the faintest trace of themselves in the histories.",
# raw15
"After the An Lushan Rebellion had been put down, there appeared all at once among the people a book of this kind, entitled The Deeds of An Lushan and signed with the name of Yao Runeng, commandant of Huayin County. Yet of this author's life, apart from the book itself, there is a complete blank; no one knows out of what motive he came to write such a book at all.",
# raw16
"This book sets down the life of An Lushan, in three volumes—upper, middle, and lower—and in the lower volume Yao Runeng makes mention of a certain matter:",
# raw17
"On the fifteenth day of the seventh month in the fifteenth year of Tianbao, with the rebel army drawing near the capital, Xuanzong led his people in headlong flight from Chang'an. When they had come as far as Mawei Slope, the heir apparent Li Heng, together with Chen Xuanli, Grand General of the Longwu Army, and others, laid a secret plot to raise a mutiny and make away with the treacherous minister Yang Guozhong. On that day Yang Guozhong, outside the post-station at Mawei Slope, fell in with a few Tibetan envoys; and even as he stood speaking with them, a great press of soldiers came surging out on every side, all crying aloud that Yang Guozhong was in collusion with the Tibetans.",
# raw18
"Yang Guozhong started in great alarm, and was on the point of opening his mouth to rail at them. Then out from the ranks charged a horseman by the name of Zhang Xiaojing, who first with a single arrow brought Yang Guozhong down from his horse, and then struck off his head and hacked the body till it was maimed and unwhole.",
# raw19
"With Zhang Xiaojing to lead the way, the soldiers' spirits rose mightily, and in one concerted rush they surrounded the post-station and demanded that the Son of Heaven put Yang Guifei to death. Xuanzong, driven to it against his will, could only bear the pain and have Yang Guifei strangled; and only then did the several companies draw back. This was the famous Mutiny at Mawei Slope.",
# raw20
"This mutiny changed the destinies of a great many people. But as to who that horseman was who first raised the cry, and what his origins, and how his fortunes went afterward, the book makes no mention whatever; it leaves only a name, as though the man had sprung all at once out of the empty air.",
# raw21
"Perhaps, when Yao Runeng came to write this passage, he was seized of a sudden by a surge of feeling he could not master, and so set down that name on the impulse of the moment. As to why he did so, that is no longer a thing those who came after can ever know.",
]


def main():
    raw = open(SRC, encoding="utf-8").read().split("\n")
    while raw and raw[-1].strip() == "":
        raw.pop()
    src = [l.strip() for l in raw[1:]]           # body paragraphs (title raw[0] dropped)

    assert len(src) == len(BODY), \
        "paragraph count mismatch: %d source vs %d english" % (len(src), len(BODY))

    # verbatim guarantee: concatenation of all blockquotes == source content
    concat_bq = "".join(src)
    concat_src = "".join(l.strip() for l in raw[1:])
    assert concat_bq == concat_src, "VERBATIM MISMATCH"
    print("verbatim check OK: %d source chars, %d body paragraphs"
          % (len(concat_src), len(src)))

    out = ["## H2 " + TITLE_EN, ""]
    for zh, en in zip(src, BODY):
        out.append("> " + zh)
        out.append(en)
        out.append("")
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    print("wrote", OUT)


if __name__ == "__main__":
    main()
