#!/usr/bin/env python3
"""Assemble the AUTHOR-note batch for ch18, ch19 and ch20 (the final chapters):
Isaacs's own numbered endnotes (bodies verbatim from the back matter) PLUS his
asterisk page-foot footnotes. Built on the build_ch1517_notes.py pattern
(do-not-revert tooling); see that file for the full method notes.

Numbered endnotes are POSITIONAL: the Nth numbered back-matter note (reading
order) is the body for in-text mark N. The in-text numbered marks come out a
clean 1..N run for all three units (ch18 1-53, ch19 1-88, ch20 1-45), with no
duplicate mark and no gap (verified).

Asterisk footnotes:
  * ch18: ONE footnote (printed p. 287, the fates of Wang Ching-wei and the
    Wuhan Left after the 1927 reconciliation). Grouping [1].
  * ch19: THREE footnotes, one foot block each (printed p. 297 the ECCI letter,
    p. 298 Chen Tu-hsiu's expulsion and fate, p. 303 Chiu Chiu-pei's fate).
    Grouping [1, 1, 1].
  * ch20: FIVE in-text asterisk marks but SEVEN foot blocks. The LAST footnote
    (anchored at "political ends.*", printed p. 332) is a MULTI-PARAGRAPH
    footnote: a single '*' whose body runs three paragraphs (the Shanghai
    Evening Post, the North China Daily News, and the Daily Worker/Sian-coup
    flip-flop), crop-verified against the page image (one '*' in the body, three
    foot paragraphs sharing it). The first four marks take one block each
    (printed p. 317, 321, 325, 328). Grouping [1, 1, 1, 1, 3].

No stray-glyph '*' this batch (ast-mark count matches the marked foot blocks
exactly), so no AST_SKIP. Each assembled asterisk stream is reduce-checked
(letters+digits) against the raw foot text so no drift can slip in.

Writes scratch/ch1820_author_notes.json for apparatus_merge.py.
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
from build_ch1517_notes import (                 # noqa: E402
    reduce, fix_italic_space, restore_hyphens,
)

PDF = os.path.join(ROOT, "source.pdf")

# Endnote back matter: (chapter number, first_pdf, last_pdf). first_pdf is the
# page carrying this chapter's endnote HEAD; last_pdf reaches the next chapter's
# HEAD (which closes the range). Headings verified: "18. Fruits of Defeat" PDF
# 390, "19. ...Soviet China" PDF 392, "20. ...United Front" PDF 395; the index
# begins PDF 397 (printed 374), so ch20 runs 395-397 (index entries start with a
# letter, not a digit, so they are not miscounted as notes).
ENDNOTE_RANGE = {
    "ch18": (18, 390, 392),
    "ch19": (19, 392, 395),
    "ch20": (20, 395, 397),
}

PDF_RANGE = {"ch18": (303, 316), "ch19": (317, 338), "ch20": (339, 362)}

AST_GROUP = {
    "ch18": [1],
    "ch19": [1, 1, 1],
    "ch20": [1, 1, 1, 1, 3],
}

AST_SKIP = {}


def foot_blocks(chid):
    """The chapter's asterisk page-foot footnote bodies, in reading (page)
    order, as cleaned XHTML. The leading '*'/'**'/'***' marker is stripped; a
    foot paragraph with no marker (a continuation, or a further paragraph of a
    multi-paragraph footnote) comes through as its own block."""
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
            txt = re.sub(r"^\s*\*+\s*", "", txt)
            out.append(restore_hyphens(clean_body(txt)))
    doc.close()
    return out


def foot_reduced(chid):
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
    units = ("ch18", "ch19", "ch20")
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
        skip = set(AST_SKIP.get(chid, []))
        if skip:
            dropped = [a for a in ast_marks if a["anchor"] in skip]
            ast_marks = [a for a in ast_marks if a["anchor"] not in skip]
            if len(dropped) != len(skip):
                sys.exit("%s: AST_SKIP anchors not all found: %s" % (chid, skip))

        mark_vals = {int(a["value"]) for a in num_marks}
        if max(mark_vals) != len(bodies) or mark_vals != set(range(1, len(bodies) + 1)):
            sys.exit("%s: %d bodies but mark values %s (expected 1..%d)"
                     % (chid, len(bodies), sorted(mark_vals), len(bodies)))
        dup = len(num_marks) - len(bodies)
        if dup:
            print("%s: NOTE source has %d duplicate numbered mark(s) "
                  "(kept, cite the same body)" % (chid, dup))

        notes = []
        for a in num_marks:
            pos = int(a["value"])
            if not 1 <= pos <= len(bodies):
                sys.exit("%s: mark %d out of range" % (chid, pos))
            anchor = a["anchor"]
            if R.count(anchor) != 1:
                sys.exit("%s: num anchor not unique: %r" % (chid, anchor))
            notes.append({"anchor": anchor, "note": fix_italic_space(bodies[pos - 1])})

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
            notes.append({"anchor": anchor, "note": fix_italic_space(body)})
            ast_reduced.append(body)

        if reduce("".join(ast_reduced)) != foot_reduced(chid):
            sys.exit("%s: asterisk body drift vs raw foot text" % chid)

        batch["notes"][chid] = notes
        print("%s: %d author notes (%d endnote + %d asterisk)"
              % (chid, len(notes), len(num_marks), len(ast_marks)))

    dest = os.path.join(ROOT, "scratch")
    os.makedirs(dest, exist_ok=True)
    path = os.path.join(dest, "ch1820_author_notes.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("wrote", path)


if __name__ == "__main__":
    main()
