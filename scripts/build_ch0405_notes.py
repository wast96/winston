#!/usr/bin/env python3
"""Assemble the AUTHOR-note batch for ch04 and ch05: Isaacs's own numbered
endnotes (bodies verbatim from the back matter, de-hyphenated and italic-run
merged by the ch01 cleaner) PLUS his asterisk page-foot footnotes, each anchored
to the exact phrase it follows in out/<id>_reading.md via data/anchors/<id>.json
(built by anchor_offsets.py). Author notes carry NO "ed" flag, so the builder
numbers them in the arabic stream by anchor position.

Numbering is POSITIONAL: the Nth numbered back-matter note (in reading order)
is the body for in-text mark N. This is robust to a printing error in Isaacs's
own back matter -- ch05's endnotes are misnumbered "...17, 18, 18, 20..." in the
1938 source (two notes labelled 18, no 19), while the in-text reference marks
run correctly 1-59. Keying by the printed label would collide on 18 and drop
19; positional numbering follows the correct in-text sequence. (Logged in
PROGRESS as a source misprint, kept visible, not repaired -- the reader never
sees the back-matter numbers; the edition renumbers by position.)

Writes scratch/ch0405_author_notes.json for apparatus_merge.py.
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
    "ch04": (4, 368, 369),
    "ch05": (5, 369, 370),
}

# The asterisk page-foot footnotes, verbatim, IN READING (position) ORDER, one
# per asterisk mark. Italics as <i>; soft line-break hyphens de-hyphenated; the
# split italic runs of a wrapped title folded into one; literal Unicode
# punctuation (curly quotes, ellipsis, em dash). Transcribed from the scan
# (8pt foot band).
ASTERISK_BODIES = {
    "ch04": [
        # after "...the Generalissimo of the Canton Army" (Hu Han-min's title)
        "In Moscow, Hu made full use of the honorary title of "
        "“Generalissimo,” which he inherited from Sun Yat-sen.",
    ],
    "ch05": [
        # after "...many dubious would-be Kuomintang heroes were involved."
        "Li Chih-lung, the Communist head of the Naval Bureau who all "
        "unwittingly became the chief nominal object of the night’s "
        "operations, has recorded a good part of the story in a pamphlet, "
        "<i>The Resignation of Chairman Wang Ching-wei</i>, not published "
        "until a year later at Wuhan.",
        # after "...grovel, before the new master of the Nationalist movement."
        "Another particularly crude example of historical distortion with "
        "regard to the March 20 coup will be found in the writings of the "
        "ex-czarist general, V. A. Yakhontoff, who found his way without "
        "difficulty into Stalin’s camp a few years ago. According to "
        "Yakhontoff, “in less than two months (after the coup) the "
        "‘Rights’ and the ‘Centrists’ were forced to "
        "compromise and agree to many concessions to the ‘Lefts’ in "
        "order to gain the support of the masses…. In May, therefore, the "
        "factions were reconciled and Chiang Kai-shek became leader of the "
        "Kuomintang and commander-in-chief of the Revolutionary armies” "
        "(V. A. Yakhontoff, <i>Russia and the Soviet Union in the Far "
        "East,</i> New York, 1932, p. 151.) Chiang “conceded” and "
        "“compromised” by making himself master of Canton!",
        # after "...there is a Tuan Chi-jui,"
        "Tuan Chi-jui was head of the notoriously corrupt government at "
        "Peking.",
        # after "...did not dispute in the least...the internal organization
        # of the Kuomintang."
        "The author of this report, Tsao Sze-yuan, was destined to suffer the "
        "consequences of not having disputed “in the least” the "
        "bourgeois offensive. A year later he died a martyr’s death at "
        "the hands of Chiang Kai-shek’s executioner.",
    ],
}


def endnote_bodies(chid):
    """Return an ORDERED list of cleaned XHTML bodies -- one per numbered note,
    in reading order. A note whose text wraps into a second block comes back as
    a numberless NOTE line; append it to the current note's RAW text and clean
    once at the end. The printed label on each note is deliberately ignored (see
    module docstring: ch05's labels are misprinted)."""
    chnum, first_pdf, last_pdf = ENDNOTE_RANGE[chid]
    raw, started = [], False
    head_prefix = "%d." % chnum
    for kind, txt in endnotes(chnum, first_pdf, last_pdf):
        if kind == "HEAD" and txt.strip().startswith(head_prefix):
            started = True
            continue
        if kind == "HEAD" and started:
            break                       # reached the NEXT chapter heading
        if kind == "NOTE" and started:
            if re.match(r"\s*\d+\.", txt):
                raw.append(txt)         # a new numbered note
            elif raw:
                raw[-1] += " " + txt    # a wrapped continuation of the last note
    return [clean_body(t) for t in raw]


def main():
    reading = {c: open(os.path.join(ROOT, "out", "%s_reading.md" % c),
                       encoding="utf-8").read() for c in ("ch04", "ch05")}
    batch = {"notes": {}}
    for chid in ("ch04", "ch05"):
        bodies = endnote_bodies(chid)
        anchors = json.load(open(os.path.join(ROOT, "data", "anchors",
                                              "%s.json" % chid)))
        num_marks = [a for a in anchors if a["kind"] == "num"]
        if len(bodies) != len(num_marks):
            sys.exit("%s: %d endnote bodies but %d numbered marks"
                     % (chid, len(bodies), len(num_marks)))
        ast_iter = iter(ASTERISK_BODIES[chid])
        notes = []
        for a in anchors:
            if a["kind"] == "num":
                pos = int(a["value"])           # in-text mark number, 1-based
                if not 1 <= pos <= len(bodies):
                    sys.exit("%s: mark %d out of range" % (chid, pos))
                body = bodies[pos - 1]
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
              % (chid, len(notes), len(num_marks),
                 sum(1 for a in anchors if a["kind"] == "ast")))

    dest = os.path.join(ROOT, "scratch")
    os.makedirs(dest, exist_ok=True)
    path = os.path.join(dest, "ch0405_author_notes.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("wrote", path)


if __name__ == "__main__":
    main()
