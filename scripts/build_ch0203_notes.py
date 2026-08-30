#!/usr/bin/env python3
"""Assemble the AUTHOR-note batch for ch02 and ch03: Isaacs's own numbered
endnotes (bodies verbatim from the back matter, de-hyphenated and italic-run
merged by the ch01 cleaner) PLUS his asterisk page-foot footnotes, each anchored
to the exact phrase it follows in out/<id>_reading.md via data/anchors/<id>.json
(built by anchor_offsets.py). Author notes carry NO "ed" flag, so the builder
numbers them in the arabic stream by anchor position.

Writes scratch/ch0203_author_notes.json for apparatus_merge.py.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from dump_endnotes import endnotes          # noqa: E402
from build_ch01_notes import clean_body     # noqa: E402  (reuse the ch01 cleaner)

# Isaacs's endnote back matter: (chapter number, first_pdf, last_pdf) covering
# the heading for this chapter through the next chapter heading.
ENDNOTE_RANGE = {
    "ch02": (2, 364, 365),
    "ch03": (3, 365, 368),
}

# The asterisk page-foot footnotes, verbatim, IN READING (position) ORDER, one
# per asterisk mark. Italics as <i>; soft line-break hyphens de-hyphenated; the
# em-dash source lines folded in. Transcribed from the scan (8pt foot band).
ASTERISK_BODIES = {
    "ch02": [
        # after "...rich, middle, and poor." (the peasant categories)
        "Professor Chen defined these categories as follows: “When a peasant "
        "family is barely capable of self-support from the land, and in its "
        "agricultural labour not directly exploited by, nor exploiting, others, "
        "we may say that such a family belongs to the class of middle peasants. "
        "The status of the middle peasants helps us to determine that of the "
        "other two classes of peasantry. When a peasant family hires one or more "
        "agricultural labourers by the day or by the season during busy times, "
        "to an extent exceeding in its total consumption of labour power that "
        "required by the average middle peasant family for self-support, or when "
        "the land which it cultivates surpasses in area the average of the land "
        "used by the middle peasant, we shall then classify this family as that "
        "of a rich peasant. Where we see families cultivating twice as much land "
        "as the middle peasants in their village, we safely classify them as "
        "those of rich peasants without further considering the labour "
        "relations. The poor peasants are comparatively easy to recognize. All "
        "peasant families whose number of cultivated mow (one mow is one-sixth "
        "of an English acre) falls below that of the middle peasants and whose "
        "members, besides living on the fruits of their own cultivation have to "
        "rely upon a wage income or some income of an auxiliary nature, belong "
        "to the poor peasants in general. Those poor peasants who do not "
        "cultivate any land, either their own or leased, but hire themselves "
        "out, or who cultivate a mere patch of land but have to support "
        "themselves chiefly by selling their labour power in agriculture, are "
        "called hired agricultural labourers, but still belong to the "
        "peasantry.” —Agrarian Problems in Southernmost China, "
        "Shanghai, 1936, p. 8.",
        # after "...total of $1,500,000,000,"
        "Calculated in U.S. dollars at par.",
        # after "...the camp of the Liquidators"
        "The Liquidators were those Mensheviks who after the defeat of the 1905 "
        "revolution wanted to adapt the labor movement to czarist legality.",
    ],
    "ch03": [
        # after "...found their way into the bourgeois camp."
        "Among the founders was Tai Chi-tao, who left the Communist Party within "
        "a few months of its formation under the pressure of a stinging rebuke "
        "from Sun Yat-sen. He later became the chief bourgeois ideologist of the "
        "Kuomintang. Others who soon broke away included Chen Kung-po, Shao "
        "Li-tze, and Chow Fu-hai, all later luminaries in the Kuomintang regime "
        "that massacred thousands of Communists and workers and peasants.",
        # after "...Maring based his proposal on three factors."
        "This information is based on notes of a conversation with Maring at "
        "Amsterdam in 1935.",
        # after "...would welcome it."
        "According to Chen Tu-hsiu, the entry was voted when Maring invoked the "
        "discipline of the Comintern. Maring denies this, pointing out that "
        "there was ample opportunity for appeal against him to the higher organs "
        "of the Communist International, but that no such appeals were made. "
        "“Moreover, I possessed no specific instructions from the "
        "Comintern,” he added, “I had no document in my hand.” "
        "Further light on this point undoubtedly exists in the unpublished and "
        "unavailable archives of the Comintern. According to P. Mif, of the Far "
        "Eastern Bureau of the Comintern, the first formal instructions “to "
        "co-ordinate the activities of the Kuomintang and the young Communist "
        "Party of China,” were contained in a special communication of the "
        "Executive Committee of the Comintern dated January 12, 1923. By that "
        "time the Communists had already entered the Kuomintang, although the "
        "formal decision to do so was not taken until the Third Conference of "
        "the Chinese Communist Party in June 1923. Cf. P. Mif, <i>Heroic "
        "China</i>, New York, 1937, pp. 21–22.",
        # after "...that was Lenin's richest legacy."
        "The late Arthur Ransome gave an astute summary of the Comintern’s "
        "contribution to the Chinese revolution when he wrote in February 1927 "
        "that Russia taught the Kuomintang “how to turn Dr. Sun’s pious "
        "programme of a raised standard of living for the workers into a stout "
        "weapon of offence and defence. Borodin may be said to have taught Dr. "
        "Sun to rely on classes rather than on individuals after having taught "
        "him to rely on a party instead of on himself. Borodin could show how "
        "the Revolution of 1905 was brought about by the workmen…for the "
        "benefit of the Russian bourgeoisie. He could show how agrarian "
        "revolution in France…crushed the feudal lords for the benefit of "
        "the French bourgeoisie…. These are dangerous weapons, but no other "
        "could have brought about the result achieved. In bringing these weapons "
        "into active operation the obvious agents to use were the Chinese "
        "Communists, and on them will fall the heaviest blows if and when the "
        "Chinese revolution finds it necessary to blunt them.” —<i>The "
        "Chinese Puzzle</i>, London, 1927.",
        # after "...Three People's Principles and nothing more."
        "In 1924 Sun attempted to reconcile his doctrines with the ideas of "
        "Communism, identifying the latter with his own principle of the "
        "“people’s livelihood.” The resultant muddle confused "
        "many of his own disciples and does not make for easy reading. He "
        "remained true, however, to the fundamental bourgeois principle of the "
        "inviolability of private property. For an ably documented study of the "
        "evolution of Sun’s ideas, see Shu-chin Tsui, “The Influence "
        "of the Canton-Moscow Entente upon Sun Yat-sen’s Political "
        "Philosophy,” <i>The Chinese Social and Political Science "
        "Review</i>, Peiping, April, July, October 1934.",
        # after "...killed and 117 wounded."
        "The foreigners claimed in justification that they were fired upon "
        "first. They had a difficult time trying to prove it. The section of the "
        "demonstration passing the bridge when shooting began was composed "
        "entirely of students and workers who were marching unarmed. And the "
        "fact remains that only two foreigners were killed in the affair whereas "
        "fifty-two Chinese were killed by the murderous machinegun fire which "
        "swept across the bridge.",
    ],
}


def endnote_bodies(chid):
    """Return {endnote_number: cleaned XHTML body}. A back-matter note whose
    text wraps into a second block comes back as a numberless NOTE line; append
    it to the current note's RAW text and clean once at the end."""
    chnum, first_pdf, last_pdf = ENDNOTE_RANGE[chid]
    raw, order, started = {}, [], False
    head_prefix = "%d." % chnum
    for kind, txt in endnotes(chnum, first_pdf, last_pdf):
        if kind == "HEAD" and txt.strip().startswith(head_prefix):
            started = True
            continue
        if kind == "HEAD" and started:
            break                       # reached the NEXT chapter heading
        if kind == "NOTE" and started:
            m = re.match(r"\s*(\d+)\.", txt)
            if m:
                num = int(m.group(1))
                raw[num] = txt
                order.append(num)
            elif order:                 # a wrapped continuation of the last note
                raw[order[-1]] += " " + txt
    return {num: clean_body(raw[num]) for num in raw}


def main():
    reading = {c: open(os.path.join(ROOT, "out", "%s_reading.md" % c),
                       encoding="utf-8").read() for c in ("ch02", "ch03")}
    batch = {"notes": {}}
    for chid in ("ch02", "ch03"):
        bodies = endnote_bodies(chid)
        anchors = json.load(open(os.path.join(ROOT, "data", "anchors",
                                              "%s.json" % chid)))
        ast_iter = iter(ASTERISK_BODIES[chid])
        notes = []
        for a in anchors:
            if a["kind"] == "num":
                num = int(a["value"])
                if num not in bodies:
                    sys.exit("%s: missing endnote body %d" % (chid, num))
                body = bodies[num]
            else:
                body = next(ast_iter)
            anchor = a["anchor"]
            if reading[chid].count(anchor) != 1:
                sys.exit("%s: anchor not unique: %r" % (chid, anchor))
            notes.append({"anchor": anchor, "note": body})
        leftover = list(ast_iter)
        if leftover:
            sys.exit("%s: %d asterisk bodies unused" % (chid, len(leftover)))
        batch["notes"][chid] = notes
        print("%s: %d author notes (%d endnote + %d asterisk)"
              % (chid, len(notes),
                 sum(1 for a in anchors if a["kind"] == "num"),
                 sum(1 for a in anchors if a["kind"] == "ast")))

    dest = os.path.join(ROOT, "scratch")
    os.makedirs(dest, exist_ok=True)
    path = os.path.join(dest, "ch0203_author_notes.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("wrote", path)


if __name__ == "__main__":
    main()
