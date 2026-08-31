#!/usr/bin/env python3
"""Assemble the AUTHOR-note batch for ch12, ch13 and ch14: Isaacs's own numbered
endnotes (bodies verbatim from the back matter, de-hyphenated and italic-run
merged by the ch01 cleaner) PLUS his asterisk page-foot footnotes.

Numbered endnotes are POSITIONAL, exactly as build_ch0911_notes.py: the Nth
numbered back-matter note (reading order) is the body for in-text mark N; the
num anchors come from data/anchors/<id>.json (anchor_offsets.py). The in-text
numbered marks come out a clean 1..N run for all three units (ch12 1-60,
ch13 1-65, ch14 1-45).

The asterisk footnotes are anchored using the anchor_offsets resolutions (every
asterisk in-text mark survives in the born-digital text layer this batch, so no
hand-picked anchor is needed, unlike B06), paired positionally with the
page-order foot blocks. What IS specified per unit is the BLOCK GROUPING: two of
ch14's four asterisk footnotes are long, multi-paragraph notes that print across
several foot blocks (and, for the first, across a page turn):

  * ch12: three single-block asterisk footnotes (pp. 180, 181, 182).
  * ch13: six single-block asterisk footnotes, three of them on printed p. 198
    (*, ** and *** -- Isaacs's second and third page-foot symbols; anchor_offsets
    collapses each run to one mark, so the reading-order marks and page-order
    foot blocks line up one to one).
  * ch14: FOUR footnotes but THIRTEEN foot blocks. The first (the composition of
    the Russian Opposition, printed p. 212) runs 6 blocks and wraps the p.212->
    213 page turn; the fourth (the comparison of Chiu Chiu-pei's confession with
    Trotsky's May 7 Theses, printed p. 222) runs 5 blocks, its body carrying
    Isaacs's own "Again:" quotations. The two middle notes are single blocks.
    Grouping: [6, 1, 1, 5]. Every foot block is consumed, in order.

The foot bodies are read programmatically from the foot-classified blocks
(italics as <i>, de-hyphenated), so nothing is hand-retyped; only the block
grouping is specified. Each assembled asterisk stream is reduce-checked
(letters+digits) against the raw foot text so no drift can slip in.

Writes scratch/ch1214_author_notes.json for apparatus_merge.py.
"""
import json
import os
import re
import sys

import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from dump_endnotes import endnotes, spans_text   # noqa: E402
from build_ch01_notes import clean_body          # noqa: E402
from extract_isaacs import classify              # noqa: E402

PDF = os.path.join(ROOT, "source.pdf")

# Isaacs's endnote back matter: (chapter number, first_pdf, last_pdf), the
# heading for this chapter through the next chapter heading (which closes it).
ENDNOTE_RANGE = {
    "ch12": (12, 380, 382),
    "ch13": (13, 382, 384),
    "ch14": (14, 384, 385),
}

PDF_RANGE = {"ch12": (197, 215), "ch13": (216, 234), "ch14": (235, 249)}

# Per-unit asterisk foot-footnote block GROUPING, in page order. The anchors
# come from anchor_offsets (data/anchors/<id>.json, kind "ast"), zipped with
# these block counts. Sum(GROUP[chid]) must equal the number of foot blocks.
AST_GROUP = {
    "ch12": [1, 1, 1],
    "ch13": [1, 1, 1, 1, 1, 1],
    "ch14": [6, 1, 1, 5],
}


def reduce(s):
    return re.sub(r"[^a-z0-9]", "", re.sub(r"<[^>]+>", "", s).lower())


def restore_hyphens(s):
    """Clean two source/cleaner artifacts the shared pipeline leaves behind
    (see build_ch0911_notes.py): a hard hyphen fused at a line break in a WG
    name ("Kaishek" is never a form Isaacs writes -- always "Kai-shek"), and a
    C0 control character in the born-digital text layer (an XML build-breaker;
    rendered to a space and collapsed)."""
    s = s.replace("Kaishek", "Kai-shek")
    # ch14's Trotsky-Theses foot footnote prints "Chiu Chiupei's" closed in the
    # born-digital text layer where the name is "Chiu-pei" (the hyphenated form
    # appears two lines above in the SAME footnote). Isaacs never writes the
    # name closed, so restore the dropped hyphen (logged in PROGRESS).
    s = s.replace("Chiupei", "Chiu-pei")
    s = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", " ", s)
    return re.sub(r"\s{2,}", " ", s).strip()


def foot_blocks(chid):
    """The chapter's asterisk page-foot footnote bodies, in reading (page)
    order, as cleaned XHTML (italics <i>, soft line-break hyphens fused). The
    leading '*'/'**'/'***' foot marker is stripped; a foot paragraph with no
    marker (a continuation) comes through as its own block."""
    first_pdf, last_pdf = PDF_RANGE[chid]
    doc = pymupdf.open(PDF)
    out = []
    for pnum in range(first_pdf, last_pdf + 1):
        blocks = [b for b in doc[pnum - 1].get_text("dict")["blocks"]
                  if "lines" in b]
        blocks.sort(key=lambda b: b["bbox"][1])
        for b in blocks:
            if classify(b) != "foot":
                continue
            txt = " ".join(spans_text(l) for l in b["lines"])
            txt = re.sub(r"^\s*\*+\s*", "", txt)     # strip leading marker
            out.append(restore_hyphens(clean_body(txt)))
    doc.close()
    return out


def foot_reduced(chid):
    """The same foot text as one reduced stream, for a drift check."""
    first_pdf, last_pdf = PDF_RANGE[chid]
    doc = pymupdf.open(PDF)
    chunks = []
    for pnum in range(first_pdf, last_pdf + 1):
        blocks = [b for b in doc[pnum - 1].get_text("dict")["blocks"]
                  if "lines" in b]
        blocks.sort(key=lambda b: b["bbox"][1])
        for b in blocks:
            if classify(b) != "foot":
                continue
            chunks.append("".join(s["text"] for l in b["lines"]
                                  for s in l["spans"]))
    doc.close()
    return reduce("".join(chunks))


def endnote_bodies(chid):
    """Ordered cleaned XHTML bodies, one per numbered back-matter note, in
    reading order (printed labels ignored -- positional numbering)."""
    chnum, first_pdf, last_pdf = ENDNOTE_RANGE[chid]
    raw, started = [], False
    head_prefix = "%d." % chnum
    for kind, txt in endnotes(chnum, first_pdf, last_pdf):
        if kind == "HEAD" and txt.strip().startswith(head_prefix):
            started = True
            continue
        if kind == "HEAD" and started:
            break
        if kind == "NOTE" and started:
            if re.match(r"\s*\d+\.?\s", txt):
                raw.append(txt)
            elif raw:
                raw[-1] += " " + txt
    return [restore_hyphens(clean_body(re.sub(r"^\s*\d+\.?\s*", "", t)))
            for t in raw]


def main():
    units = ("ch12", "ch13", "ch14")
    reading = {c: open(os.path.join(ROOT, "out", "%s_reading.md" % c),
                       encoding="utf-8").read() for c in units}
    batch = {"notes": {}}
    for chid in units:
        R = reading[chid]
        bodies = endnote_bodies(chid)
        anchors = json.load(open(os.path.join(ROOT, "data", "anchors",
                                              "%s.json" % chid)))
        num_marks = [a for a in anchors if a["kind"] == "num"]
        ast_marks = [a for a in anchors if a["kind"] == "ast"]
        # POSITIONAL numbering maps in-text mark value N to the Nth back-matter
        # body. Normally #marks == #bodies. ch13 is a SOURCE numbering error:
        # its Min Kuo Jih Pao passage carries the superscript "64" TWICE (once
        # mid-quote at "were closed down.", once at the quote's end after "Ho
        # Chien."), so there are 65 in-text marks but only 64 back-matter notes
        # (verified: the ch13 endnotes run a clean 1..64 and end at "64. Min Kuo
        # Jih Pao, June 18-19, 1927," with no note 65 before the ch14 heading).
        # Both "64" marks legitimately cite note 64; the builder renders them
        # positionally as the edition's markers 64 and 65, each showing that
        # citation. So the invariant is not equal counts but: every mark value
        # is a real body index, and every body is cited by at least one mark.
        mark_vals = {int(a["value"]) for a in num_marks}
        if max(mark_vals) != len(bodies) or mark_vals != set(range(1, len(bodies) + 1)):
            sys.exit("%s: %d bodies but mark values %s (expected 1..%d)"
                     % (chid, len(bodies), sorted(mark_vals), len(bodies)))
        dup = len(num_marks) - len(bodies)
        if dup:
            print("%s: NOTE source has %d duplicate numbered mark(s) "
                  "(kept, cite the same body)" % (chid, dup))

        notes = []
        # numbered endnotes: positional
        for a in num_marks:
            pos = int(a["value"])
            if not 1 <= pos <= len(bodies):
                sys.exit("%s: mark %d out of range" % (chid, pos))
            anchor = a["anchor"]
            if R.count(anchor) != 1:
                sys.exit("%s: num anchor not unique: %r" % (chid, anchor))
            notes.append({"anchor": anchor, "note": bodies[pos - 1]})

        # asterisk footnotes: anchor_offsets anchors zipped with block groups
        group = AST_GROUP[chid]
        if len(group) != len(ast_marks):
            sys.exit("%s: %d ast marks but %d groups"
                     % (chid, len(ast_marks), len(group)))
        fblocks = foot_blocks(chid)
        if sum(group) != len(fblocks):
            sys.exit("%s: groups sum to %d but %d foot blocks"
                     % (chid, sum(group), len(fblocks)))
        fi = 0
        ast_reduced = []
        for a, nblocks in zip(ast_marks, group):
            body = " ".join(fblocks[fi:fi + nblocks])
            fi += nblocks
            anchor = a["anchor"]
            if R.count(anchor) != 1:
                sys.exit("%s: ast anchor not unique: %r" % (chid, anchor))
            notes.append({"anchor": anchor, "note": body})
            ast_reduced.append(body)

        # drift check: assembled asterisk bodies == raw foot text (letters+digits)
        if reduce("".join(ast_reduced)) != foot_reduced(chid):
            sys.exit("%s: asterisk body drift vs raw foot text" % chid)

        batch["notes"][chid] = notes
        print("%s: %d author notes (%d endnote + %d asterisk)"
              % (chid, len(notes), len(num_marks), len(ast_marks)))

    dest = os.path.join(ROOT, "scratch")
    os.makedirs(dest, exist_ok=True)
    path = os.path.join(dest, "ch1214_author_notes.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("wrote", path)


if __name__ == "__main__":
    main()
