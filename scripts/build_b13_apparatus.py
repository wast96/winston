#!/usr/bin/env python3
"""Build the B13 apparatus file (ch59-ch63 notes). Anchors stay literal Unicode
(they must be verbatim substrings of the reading files); note bodies have every
non-ASCII character encoded to a numeric character reference, per the apparatus
contract. <i> tags are ASCII and pass through untouched."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def enc(s):
    return "".join(c if ord(c) < 128 else "&#%d;" % ord(c) for c in s)


# (unit, anchor, body-in-plain-unicode)
NOTES = [
    ("ch59", "twenty-six Krupp rifled guns of twelve-centimeter bore",
     "Shiba’s figure is not quite right. The Kaiyō-maru, built for the "
     "shogunate at Dordrecht and completed in 1866, carried at her commissioning "
     "eighteen Krupp 16-centimeter rifled muzzle-loaders together with eight "
     "30-pounders — twenty-six in the main battery, of thirty-four guns in "
     "all. The bore was 16 centimeters, not 12, and not every one of the "
     "twenty-six was a Krupp piece; but she was indeed among the most powerful "
     "warships afloat in her day."),
    ("ch59", "the Danish-Austrian War",
     "This is the Second Schleswig War of 1864. Shiba’s own label, the "
     "“Denmark–Austria war,” drops Prussia, and it was Prussia "
     "— not Austria — that was the dominant partner in the alliance "
     "that crushed Denmark; the next paragraph names both powers correctly. "
     "Enomoto is traditionally said to have gone to the front as an observer "
     "while a student in the Netherlands, though the detail is biographical "
     "rather than firmly documented."),
    ("ch59", "up for sale at a thousand ryō",
     "By the late Tokugawa the standing of a shogunal retainer had become, in "
     "effect, a commodity: an impoverished <i>gokenin</i> or <i>hatamoto</i> "
     "family could sell its house rank and stipend to an outsider with money and "
     "learning, who thereby bought his way into the samurai class and the "
     "shogunate’s service. Enomoto’s father, a commoner’s son and "
     "a gifted mathematician, entered the ruling order in just this way."),
    ("ch59", "Inō Tadataka",
     "Inō Tadataka (1745–1818), the shogunate’s great surveyor, "
     "who spent the last seventeen years of his life walking the coasts of Japan "
     "and produced the first accurate map of the whole country. That "
     "Enomoto’s father studied under such men marks the family as serious "
     "practitioners of Western-influenced science."),

    ("ch60", "one of the few survivors of the Shinsengumi",
     "Ichimura Tetsunosuke (1854–1877) is a historical figure, and the "
     "tradition that will pay off the thread begun here is well attested by the "
     "Satō family of Hino: in the spring of 1869, shortly before "
     "Hijikata’s death at Hakodate, he is held to have sent the boy south "
     "out of the doomed fortress carrying his own photograph, a lock of his hair, "
     "and a last message to the Satō house of his home country. Ichimura "
     "reached them, and it is largely through him and the Satō records that "
     "Hijikata’s last years are known. He was killed, as told here, fighting "
     "Saigō’s army in 1877."),
    ("ch60", "a samurai dies for the man who knows his worth",
     "An old maxim from the Chinese classics — <i>shi wa onore o shiru mono "
     "no tame ni shisu</i> — first spoken by the assassin Yu Rang in the "
     "Warring States, as recorded in the <i>Zhanguo ce</i> and in Sima "
     "Qian’s <i>Shiji</i>: a man of honor gives his life for the one who "
     "truly recognizes him. The narrator raises it only to set it aside — "
     "Ichimura’s devotion, he says, was something stranger and less reasoned "
     "than that."),

    ("ch61", "the one domain that held no rice-assessed fief",
     "Almost every <i>daimyō</i> was ranked by the assessed rice yield "
     "(<i>kokudaka</i>) of his land. Matsumae, at the far northern reach of "
     "Honshū, held territory too cold for rice, and was reckoned instead a "
     "castle-holding house with no stated koku figure; its wealth came from its "
     "monopoly of trade with the Ainu and the produce of Ezo — fish, kelp, "
     "and furs. In this it stood alone among the roughly two hundred and sixty "
     "domains."),
    ("ch61", "now a national treasure",
     "Shiba’s aside had fallen out of date even as he wrote it. The Matsumae "
     "keep he calls a national treasure — the last castle keep raised in "
     "Japan in the old feudal style, finished in 1854 — burned down in 1949; "
     "a concrete reconstruction was put up on the site in 1961. Today it is the "
     "castle grounds and a surviving gate that carry protected status."),
    ("ch61", "four-kin mountain guns",
     "Artillery of the period was rated by the weight of its shot in <i>kin</i> "
     "(about 600 grams), on the French model then in vogue: a “four-kin” "
     "gun threw a shell of roughly four kin, a light field or mountain piece, and "
     "the “twelve-kin” cannon that answered it a far heavier one. The "
     "kin measure of caliber recurs through these battle chapters."),
    ("ch61", "as Saitō Hajime renamed himself",
     "Here the novel parts from the record. The historical Saitō Hajime did "
     "not cross to Ezo: he stayed to fight at Aizu, was interned after its "
     "surrender, and never went north at all. Shiba brings him to Hokkaidō "
     "in order to write this scene, in which Hijikata saves his life by sending "
     "him away. Saitō did live on to the end of Meiji — under the names "
     "Yamaguchi and later Fujita Gorō, serving as a Tokyo policeman and "
     "ending his days as a school clerk — one of the corps’s last "
     "survivors, as the novel says."),

    ("ch62", "This ship was later named the Azuma",
     "The ironclad was the former CSS <i>Stonewall</i>, a steam ram built at "
     "Bordeaux in 1864 for the Confederacy under the cover name <i>Sphinx</i>. "
     "She reached Japan after the American Civil War; the United States, "
     "declaring neutrality in the Japanese conflict, held her at Yokohama and "
     "would not release her until the fighting was decided, then delivered her to "
     "the new Meiji government early in 1869. Renamed Azuma in 1871, she was the "
     "first ironclad of the Imperial Japanese Navy, and her coming, as this "
     "chapter says, tipped the naval balance against Hakodate."),
    ("ch62", "had already been fixed by election",
     "The Ezo regime chose its officers by ballot in December 1868 — a thing "
     "without precedent in Japan, where office had always come by birth or "
     "appointment. Some eight hundred and fifty-six votes were cast; Enomoto "
     "Takeaki was elected president and Matsudaira Tarō vice-president, with "
     "Ōtori Keisuke and Arai Ikunosuke over army and navy and Hijikata as "
     "assistant army commissioner. Foreign observers, and later writers, often "
     "called the short-lived government a republic."),
    ("ch62", "Ōmura Masujirō",
     "Ōmura Masujirō (1824–1869), a physician’s son of "
     "Chōshū turned military scientist, was the architect of the new "
     "government’s army and is reckoned a father of the modern Japanese "
     "military. His caution here — wait for spring — was overruled. He "
     "was cut down by disaffected samurai later in 1869, only months after the "
     "events of these chapters."),
    ("ch62", "the Tōgō Heihachirō of later days",
     "Tōgō Heihachirō (1848–1934), then an obscure Satsuma "
     "gunnery officer, would become the most famous admiral in Japanese history: "
     "commander of the Combined Fleet that destroyed the Russian navy at Tsushima "
     "in 1905. Shiba, in the midst of a novel of Hijikata, cannot resist the long "
     "digression that follows on the young Tōgō aboard the Kasuga "
     "— the two men were, for these few weeks, on opposite sides of the same "
     "sea."),
    ("ch62", "the old wakō over again",
     "The <i>wakō</i> were the sea-raiders — mostly Japanese, later of "
     "mixed Japanese and Chinese make — who plundered the coasts of Korea "
     "and China from the fourteenth to the sixteenth centuries, boarding ships "
     "and sacking ports. To the Western-schooled naval officers, Hijikata’s "
     "plan to take a modern ironclad by leaping aboard sword in hand seemed a "
     "throwback to that piratical past."),

    ("ch63", "a gun with six muzzles",
     "This is the Gatling gun, the hand-cranked, multi-barreled forerunner of the "
     "machine gun, patented in America in 1862; Shiba’s furigana glosses his "
     "“field quick-firing gun” with the name outright. Its rate of fire "
     "made it murderous against men crossing an open deck, and in the raid told "
     "in the next chapter it would cut the boarders down. Some survivors’ "
     "testimony held that the weapon was in truth massed rifle fire rather than a "
     "Gatling, but the Gatling account is the standard one."),
    ("ch63", "famous for its ninja",
     "Kōga (also read Kōka), a district of Ōmi province, was with "
     "neighboring Iga one of the two great homes of the ninja tradition — "
     "the covert agents and irregular fighters of the warring-states age. That "
     "the sober naval officer Kōga Gengo should spring from such stock is a "
     "quiet irony the narrator enjoys."),
    ("ch63", "the later Kuroda Kiyotaka",
     "Kuroda Kiyotaka (1840–1900), a Satsuma officer who rose to direct the "
     "colonization of Hokkaidō and, in 1888, to become the second prime "
     "minister of Japan. His heavy drinking, which the narrator makes the hinge "
     "of this comic-tragic scene, dogged his whole career. It was Kuroda who, "
     "after Hakodate fell, argued successfully that Enomoto’s life be "
     "spared."),
]


def main():
    out = {"notes": {}}
    for unit, anchor, body in NOTES:
        out["notes"].setdefault(unit, []).append(
            {"anchor": anchor, "note": enc(body)})
    dest = os.path.join(ROOT, "out", "b13_apparatus.json")
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    total = sum(len(v) for v in out["notes"].values())
    print("wrote %s (%d notes across %d units)"
          % (dest, total, len(out["notes"])))


if __name__ == "__main__":
    main()
