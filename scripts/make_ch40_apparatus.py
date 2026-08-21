# Build data/ch40_apparatus.json for apparatus_merge.py.
# Note bodies authored as plain ASCII + typed hanzi (+ em dashes), then every
# non-ASCII char is converted to a numeric character reference before writing.
# EVERY non-ASCII hanzi glyph used in a note body is asserted to occur in ch40's
# own authoritative data/zh/ch40.txt (a correct glyph absent from the source is
# named in English only; the gold-yuan note uses the source's own variant 劵).
# Anchors are ASCII substrings of ch40_reading.md, with no em dash and no
# quote/apostrophe. Pinyin is untoned.
#
# ch40 is a Part-Four narrative chapter (the diverging fates of the three Tianjin
# men; Nie Rongzhen as the overlooked arch-enemy of North China; the "stay-behind
# work" and Ji Zhaoxiang's martyrdom; and the string of defeats from the Northeast
# to the Xinbao'an-Miaofeng disaster). Furniture already noted earlier is NOT
# re-noted: the 绥靖/戡乱/共匪 framing, 匪谍/共酋/共干 and the Mao epithets, the
# Juntong/Baomiju, the No. 76 puppet HQ and the Ume Kikan, the Eighth Route Army,
# the Three-Anti/Five-Anti campaigns, the Marshall-era Executive Headquarters, the
# North China Bandit-Suppression HQ, the Lizhi Class, the province one-character
# abbreviations, Xinbao'an and the Laishui campaign, and the Republican-year
# system. The nine new notes cover items a Western reader first meets here.
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CID = "ch40"
zh = open(os.path.join(ROOT, "data", "zh", CID + ".txt"), encoding="utf-8").read()
reading = open(os.path.join(ROOT, "out", CID + "_reading.md"), encoding="utf-8").read()

NOTES = [
    {
        "anchor": "Hundred Regiments Offensive",
        "note": (
            "The Hundred Regiments Offensive (百团大战, baituan dazhan) was the largest "
            "set-piece action the Communist Eighth Route Army fought against the Japanese, "
            "waged across North China from August to December 1940 against the occupation's "
            "railways, roads, and blockhouses; its name comes from the roughly one hundred "
            "regiments committed. Zhu De and Peng Dehuai directed it. It is generally "
            "credited as the Communists' one great open offensive of the war &#8212; but it "
            "drew savage Japanese reprisals (the 'Three-All' mopping-up: burn all, kill "
            "all, loot all), and Mao Zedong is indeed thought to have disapproved, holding "
            "that it exposed Communist strength too soon, a charge revived against Peng in "
            "his 1959 purge. Chen's telling &#8212; that it was mere banditry and Mao's "
            "objection mere jealousy &#8212; is the Nationalist reading, but the "
            "disapproval itself is well attested."
        ),
    },
    {
        "anchor": "Lu Zhishen",
        "note": (
            "Lu Zhishen (鲁智深), the 'Flowery Monk,' is one of the hundred and eight heroes "
            "of the classic Ming novel the Water Margin: an army officer turned "
            "outlaw-monk, huge, hot-tempered, and prodigiously strong, who takes to the "
            "bandit stronghold of Mount Liang. Mao's reported quip &#8212; 'of old there "
            "was Lu Zhishen, and today there is Nie Rongzhen' &#8212; likened Nie's "
            "mountain base at Wutai to the outlaws' mountain fastness; Mao meant it for "
            "praise, and Chen throws it back as a confession of banditry."
        ),
    },
    {
        "anchor": "Xu-Bang Campaign",
        "note": (
            "What Chen calls the Xu-Bang Campaign (徐蚌会战, named for Xuzhou and Bengbu, "
            "the Nationalist term) is the battle the Communists call the Huaihai Campaign, "
            "the largest engagement of the civil war, fought from November 1948 to January "
            "1949 across the plains of northern Jiangsu and Anhui about Xuzhou. Some half a "
            "million Nationalist troops under the Xuzhou 'Bandit-Suppression' command were "
            "encircled and destroyed by the Communist East China and Central Plains field "
            "armies; the defeat laid the lower Yangzi and the capital, Nanjing, open, and "
            "in effect decided the war. The casualty figures Chen cites are of the right "
            "order of magnitude."
        ),
    },
    {
        "anchor": "Jinzhou fell into the hands of the Communist army",
        "note": (
            "The collapse Chen sketches here &#8212; the fall of Jinzhou on 15 October "
            "1948, of Changchun on the 20th, and of Shenyang soon after, with Liao "
            "Yaoxiang's relief army wiped out on the retreat &#8212; was the Liaoshen "
            "Campaign (September to November 1948), the first of the three great Communist "
            "offensives that decided the civil war. Lin Biao's Northeast Field Army took "
            "Jinzhou to seal the passes to the south, forced the surrender of the starved "
            "Changchun garrison, and destroyed the field armies sent to recover the city; "
            "with the Northeast wholly lost, Lin's army was freed to march south through "
            "the Great Wall into the Beiping-Tianjin fighting that follows. Fan Hanjie and "
            "Lu Junquan were the senior Nationalist commanders taken at Jinzhou."
        ),
    },
    {
        "anchor": "gold yuan note had no standing",
        "note": (
            "The gold yuan note (the source prints 金圆劵) was the currency the Nationalist "
            "government issued in August 1948 to replace the ruined fabi; within months "
            "runaway inflation destroyed it too, and by the winter of 1948-49 it was all "
            "but worthless. In that collapse people fell back on things of intrinsic value "
            "&#8212; sacks of flour, and above all silver. The 'Yuan big-head' (袁大头) was "
            "the standard Republican silver dollar (银元), struck from 1914 with the "
            "profile of President Yuan Shikai (袁世凯), whose bald head gave the coin its "
            "nickname. Chen's stay-behind agents were provisioned in flour and these silver "
            "dollars precisely because paper money would buy nothing after the fall."
        ),
    },
    {
        "anchor": "held a temple fair every year",
        "note": (
            "The Miaofeng Mountains (妙峰山), northwest of Beijing, were the site of the "
            "most celebrated temple-fair pilgrimage (庙会) of the old capital: each spring, "
            "in the lunar third and fourth months, great crowds climbed to the shrine of "
            "the goddess Bixia Yuanjun to burn incense, and the most devout would kowtow "
            "the whole way up the mountain. Voluntary pilgrim associations gave out food, "
            "tea, and entertainment free along the road. Suppressed after 1949, the fair "
            "has been revived in recent decades. Chen's memory of it frames his lament that "
            "folk custom outlasts the wars fought over the land."
        ),
    },
    {
        "anchor": "hawthorns strung on a willow withe",
        "note": (
            "The 'shanlihong' (山里红) or 'big candied-haws stick' is the outsized country "
            "cousin of the tanghulu (糖葫芦), the candied-fruit skewer sold through the "
            "northern Chinese winter: hawthorn berries (山楂) threaded on a stick and glazed "
            "with sugar. The refined city version is small, dipped in rock sugar, and mixes "
            "in crab-apple and water-chestnut; the pilgrim's souvenir Chen describes was a "
            "rough giant &#8212; hawthorns alone on a whole willow withe several feet long, "
            "glazed with cheap malt sugar &#8212; a fairground trophy more than a sweet."
        ),
    },
    {
        "anchor": "as of straw dogs",
        "note": (
            "'Straw dogs' (刍狗, chugou) alludes to the Daoist classic the Daodejing: "
            "'Heaven and earth are not benevolent; they treat the ten thousand things as "
            "straw dogs.' Straw dogs were figures plaited for a sacrifice, used with "
            "reverence for the moment of the rite and then thrown away and trampled. Chen's "
            "charge is that the foreign power spent his comrades' lives as carelessly as "
            "those discarded effigies."
        ),
    },
    {
        "anchor": "red blood that dyes the button-knob crimson",
        "note": (
            "'The button-knob' renders dingzi (顶子), the round finial atop a Qing "
            "official's hat, whose material and color proclaimed its wearer's rank &#8212; "
            "the higher the office, the costlier the knob. The saying Chen turns bitter "
            "here, that a red-topped rank is 'blood that dyes the button-knob crimson,' "
            "means a career or a promotion bought with the lives of the men under one: the "
            "commander wins his rank, and it is his soldiers' blood that colors it."
        ),
    },
]


def to_ncr(s):
    return "".join(ch if ord(ch) < 128 else "&#%d;" % ord(ch) for ch in s)


def main():
    seen = set()
    for e in NOTES:
        assert e["anchor"] in reading, "anchor not in reading: %r" % e["anchor"]
        assert e["anchor"] not in seen, "duplicate anchor: %r" % e["anchor"]
        seen.add(e["anchor"])
        for ch in e["anchor"]:
            assert ord(ch) < 128, "anchor has non-ASCII: %r" % e["anchor"]
            assert ch not in "—\"'‘’“”", \
                "anchor has a forbidden char: %r" % e["anchor"]
        for ch in e["note"]:
            if ord(ch) >= 128 and ch != "—":
                assert ch in zh, \
                    "note glyph not in data/zh/%s.txt: %r" % (CID, ch)
        e["note"] = to_ncr(e["note"])
    dest = os.path.join(ROOT, "data", CID + "_apparatus.json")
    json.dump({"notes": {CID: NOTES}}, open(dest, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print("wrote %s (%d notes)" % (dest, len(NOTES)))


if __name__ == "__main__":
    main()
