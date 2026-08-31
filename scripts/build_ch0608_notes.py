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

Writes scratch/ch0608_author_notes.json for apparatus_merge.py.
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
    "ch06": (6, 370, 372),
    "ch07": (7, 372, 373),
    "ch08": (8, 373, 375),
}

# The asterisk page-foot footnotes, verbatim, IN READING (position) ORDER, one
# per asterisk mark. Italics as <i>; soft line-break hyphens de-hyphenated; the
# split italic runs of a wrapped title folded into one; literal Unicode
# punctuation (curly quotes, ellipsis, em dash). Transcribed from the scan
# (8pt foot band).
ASTERISK_BODIES = {
    "ch06": [
        # * after "...raised the question of work in the army, comrade V."
        "Voitinsky",
        # ** after "...First he told comrade M."
        "Mandalyan",
        # * after "...a “sympathizing party,” into the Communist International."
        "The participation of Shao Li-tze, of Chiang’s personal entourage, as "
        "fraternal delegate of the Kuomintang in the Seventh Plenum of the "
        "E.C.C.I. in November 1926, confirms the membership status of the "
        "Kuomintang in the International.",
    ],
    "ch07": [
        # * after "...the servant of the foreign and Chinese bourgeoisie."
        "Men like Ferral, the banker in André Malraux’s <i>Mans’ Fate</i>.",
    ],
    "ch08": [
        # * after "...held incommunicado." (the arrested-journalists page)
        "In Peking two American journalists, Wilbur Burton and Mildred "
        "Mitchell, who worked for the <i>Nationalist News Agency</i>, were "
        "arrested by the northern military and held incommunicado. Virtually "
        "left to their fate by the U.S. Legation, they were freed as a result "
        "of the publicity given their case by Randall Gould of the United "
        "Press and the efforts of Charles J. Fox, a Tientsin lawyer. Gould was "
        "later banned from Legation press conferences by MacMurray, the U.S. "
        "minister. William and Rayna Prohme, who edited the <i>People’s "
        "Tribune</i>, were generally regarded as race renegades. Borodin, of "
        "course, had horns.",
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
            # A new numbered note. The trailing period is OPTIONAL: ch06's
            # back-matter note 14 is misprinted "14" (no period) in the 1938
            # source while every other label carries one; the relaxed regex
            # still yields a perfectly sequential 1..N run for ch06/07/08, so no
            # wrapped continuation is misread as a label. (Kept visible, not
            # repaired -- the reader sees the edition's positional numbering.)
            if re.match(r"\s*\d+\.?\s", txt):
                raw.append(txt)         # a new numbered note
            elif raw:
                raw[-1] += " " + txt    # a wrapped continuation of the last note
    # Strip the leading label here with an OPTIONAL period so ch06's
    # period-less "14" label is removed too (clean_body only strips "N.").
    return [clean_body(re.sub(r"^\s*\d+\.?\s*", "", t)) for t in raw]


def main():
    reading = {c: open(os.path.join(ROOT, "out", "%s_reading.md" % c),
                       encoding="utf-8").read() for c in ("ch06", "ch07", "ch08")}
    batch = {"notes": {}}
    for chid in ("ch06", "ch07", "ch08"):
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
    path = os.path.join(dest, "ch0608_author_notes.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("wrote", path)


if __name__ == "__main__":
    main()
