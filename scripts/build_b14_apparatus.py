#!/usr/bin/env python3
"""Build the B14 apparatus file (ch64-ch68 notes). Anchors stay literal Unicode
(they must be verbatim, UNIQUE substrings of the reading files); note bodies
have every non-ASCII character encoded to a numeric character reference, per the
apparatus contract. <i> tags are ASCII and pass through untouched."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def enc(s):
    return "".join(c if ord(c) < 128 else "&#%d;" % ord(c) for c in s)


# (unit, anchor, body-in-plain-unicode)
NOTES = [
    # ── ch64 襲撃 / The Attack ──
    ("ch64", "toward Miyako Bay, the object of the attack",
     "The naval raid on Miyako Bay took place at dawn on Meiji 2/3/25 "
     "(6 May 1869). Of the three Ezo-navy ships that set out to seize the "
     "government’s ironclad Kōtetsu by boarding, a storm scattered the "
     "Takao and the Banryū, and the Kaiten went in alone. Running up under "
     "a United States flag, she came alongside bow-first instead of "
     "broadside-to; her deck stood some nine feet above the Kōtetsu’s, "
     "so the boarders had to drop across one or two at a time and were cut "
     "down by the Gatling gun on the ironclad’s deck. The raid failed and "
     "the Kaiten escaped back to Hakodate. The episode is well attested in the "
     "standard histories of the Boshin War; corroborated."),
    ("ch64", "a man had to leap down a full jō",
     "A <i>jō</i> is ten <i>shaku</i>, about 3.03 meters or ten feet — close "
     "to the roughly nine-foot difference in deck height that the Western "
     "accounts of the battle also record."),
    ("ch64", "a piece of three hundred kin",
     "Heavy muzzle-loading guns were rated by the weight of shot they threw, "
     "reckoned in <i>kin</i> (a <i>kin</i> being about 600 grams). A "
     "“three-hundred-<i>kin</i> gun” thus names a very large piece; the "
     "Kōtetsu — the former Confederate ram <i>Stonewall</i> — carried a "
     "300-pounder Armstrong rifle forward, the gun Shiba has in view."),
    ("ch64", "forming the shape of the character ri, リ",
     "The images are drawn from the shapes of two kana. To lie <i>リ</i> "
     "(<i>ri</i>) is for the two ships to lie parallel, side by side, like "
     "that character’s two upright strokes — the position from which every "
     "boarder could pour across at once. To lie <i>イ</i> (<i>i</i>) is to "
     "meet bow-to-side at an angle, as the Kaiten in fact did, so that the men "
     "could cross only one or two at a time."),
    ("ch64", "Cape Heizaki",
     "The cape at the entrance to Miyako Bay, in the Hei district of what is "
     "now Iwate prefecture; 閉伊崎 is read here as Heizaki. Miyako lies on the "
     "Sanriku coast of northeastern Honshū."),
    ("ch64", "There was nothing cowardly in it",
     "Sailing under false colors and striking them for one’s own flag before "
     "opening fire was an accepted <i>ruse de guerre</i> in nineteenth-century "
     "European naval practice, as Shiba says; to fight on while still under the "
     "false flag would have been the breach of custom."),

    # ── ch65 再会 / Reunion ──
    ("ch65", "styling themselves goyōtō",
     "<i>Goyōtō</i>, literally “requisition-robbers,” were bands who plundered "
     "under the pretense of levying funds or goods for official — often "
     "loyalist — purposes in the disorder of the 1860s. Shiba’s gloss in the "
     "text is exact."),
    ("ch65", "returned their domain registers",
     "The <i>hanseki hōkan</i>, the return of the domain land-and-population "
     "registers to the throne. The four leading western lords petitioned to "
     "return them in the third month of Meiji 2 (spring 1869), and the court "
     "ordered all domains to follow in the sixth month (July 1869); Yūjirō "
     "speaks of it here as already accomplished. It was the first step toward "
     "the abolition of the domains in 1871. Corroborated, the dating slightly "
     "compressed."),
    ("ch65", "seemed to be of mixed Ainu blood",
     "The Ainu are the indigenous people of Ezo (Hokkaidō), with a language and "
     "customs of their own, distinct from those of the Japanese of the “home "
     "islands” (<i>naichi</i>) to the south. The boat-chant and the servant "
     "here mark the northern setting."),
    ("ch65", "borrow me a yatate",
     "A <i>yatate</i> is a portable writing-set — a small case holding an "
     "ink-soaked wad and a brush, carried at the belt — the pocket pen of its "
     "day."),
    ("ch65", "Even after Toshizō came to Hokkaidō",
     "Shiba uses the modern name Hokkaidō, an anachronism in these scenes: the "
     "island was still called Ezo, and was formally renamed Hokkaidō only in "
     "the eighth month of Meiji 2 (September 1869), after Toshizō’s death. The "
     "usage is the narrator’s, not the characters’."),

    # ── ch66 官軍上陸 / The Imperial Army Lands ──
    ("ch66", "one photograph of Toshizō now in existence",
     "This is the celebrated seated portrait of Hijikata in Western dress, "
     "taken at Hakodate in 1869 — the only known photograph of him, and the "
     "source of every later likeness. Carried south by Ichimura Tetsunosuke to "
     "the Satō family at Hino, it survives there still. Corroborated."),
    ("ch66", "cut some two sun off its end",
     "A <i>sun</i> is about 3.03 centimeters, one-tenth of a <i>shaku</i>; two "
     "<i>sun</i> is thus a little over an inch."),
    ("ch66", "Yoshitoyo",
     "Yoshitoyo (義豊) was Hijikata’s <i>imina</i>, or formal personal name, "
     "used in a signature such as this in place of the familiar Toshizō. It "
     "recurs in his posthumous Buddhist name at the close of the book."),
    ("ch66", "at a fishing village called Otobe",
     "The new-government expedition landed on Ezo at Otobe, south of Esashi, on "
     "Meiji 2/4/9 (about 20 May 1869), and drove inland toward Hakodate; Esashi "
     "and then Matsumae fell in the days that followed. Corroborated."),
    ("ch66", "a record-long engagement such as there had never before been",
     "The fighting at the Futamataguchi pass, in the fourth month of Meiji 2 "
     "(late May 1869), was one of Hijikata’s few clear successes in the Ezo "
     "campaign; his defense there held for many days, until the collapse of the "
     "other fronts forced him to withdraw. Shiba’s figures — a sixteen-hour "
     "action, thirty-five thousand rounds, a single man lost — are the "
     "traditional ones and cannot be checked precisely, but the tenacity of the "
     "defense is well attested."),

    # ── ch67 五稜郭 / Goryōkaku ──
    ("ch67", "203-Meter Hill",
     "Shōjusan and 203-Meter Hill were the key heights in the Japanese siege of "
     "Russian-held Port Arthur in 1904–05, during the Russo-Japanese War, whose "
     "capture laid the fortress open — the narrator’s forward glance of some "
     "thirty-five years. He goes on to liken Enomoto to the Russian commander "
     "Stoessel and Toshizō to Major-General Kondratenko, Port Arthur’s ablest "
     "and best-loved defender, whose death in the fighting hastened the "
     "surrender."),
    ("ch67", "Shinobirika was the one Ainu word",
     "From the Ainu <i>sino pirka</i>, “truly fine” or “truly beautiful.” Shiba "
     "gives it as the one Ainu word Toshizō learned in the north; the haiku "
     "sets it against the moon over Ezo."),
    ("ch67", "Nakajima Saburōsuke was a man who had once been a yoriki",
     "Nakajima Saburōsuke (1821–1869) had been a <i>yoriki</i>, a "
     "constable-official, of the Uraga magistracy, and was among those who "
     "rowed out to parley when Commodore Perry’s squadron reached Uraga on "
     "Kaei 6/6/3 (8 July 1853) — the event that opened Japan. A pioneer of "
     "Western naval study, he died with his two sons defending the Chiyogatai "
     "battery after the surrender of Goryōkaku. Corroborated."),

    # ── ch68 砲煙 / Gunsmoke ──
    ("ch68", "the fifth hour of the night",
     "By the old system of variable hours, the “fifth hour” of the night "
     "(<i>itsutsu</i>) fell around eight in the evening."),
    ("ch68", "the eleventh of the fifth month of Meiji 2",
     "Hijikata Toshizō was killed on Meiji 2/5/11, which is 20 June 1869 in the "
     "Western calendar — not 11 June, a slip that comes of reading the lunar "
     "day-number as a Gregorian one. He fell leading a sortie near the Ippongi "
     "barrier (Ippongi-kan), on the road between Goryōkaku and the Bentenzaki "
     "battery, struck by a rifle-ball while on horseback; the standard account "
     "puts the wound low in the back. The exact spot and the identity of the "
     "man who fired are debated among historians, and Shiba renders the scene "
     "without settling either. Goryōkaku surrendered a week later, on Meiji "
     "2/5/18 (27 June 1869). Corroborated as to date and manner; the "
     "particulars remain uncertain."),
    ("ch68", "the Gakuheitai of the former Sendai domain",
     "The <i>Gakuheitai</i> was the Western-trained rifle corps of the Sendai "
     "domain, reckoned among the best-drilled units to reach Ezo; its commander "
     "was Hoshi Juntarō, named here among Toshizō’s supporting officers."),
    ("ch68", "there was a small woman who left an offering",
     "Oyuki is Shiba’s invention — he says as much in his afterword — and so is "
     "this closing scene at the temple. No such visitor is recorded; the "
     "sun-shower and the unnamed mourner are the novelist’s farewell, not a "
     "document."),
]


def main():
    out = {"notes": {}}
    for unit, anchor, body in NOTES:
        out["notes"].setdefault(unit, []).append(
            {"anchor": anchor, "note": enc(body)})
    dest = os.path.join(ROOT, "out", "b14_apparatus.json")
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    total = sum(len(v) for v in out["notes"].values())
    print("wrote %s (%d notes across %d units)"
          % (dest, total, len(out["notes"])))


if __name__ == "__main__":
    main()
