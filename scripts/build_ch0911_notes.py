#!/usr/bin/env python3
"""Assemble the AUTHOR-note batch for ch09, ch10 and ch11: Isaacs's own numbered
endnotes (bodies verbatim from the back matter, de-hyphenated and italic-run
merged by the ch01 cleaner) PLUS his asterisk page-foot footnotes.

Numbered endnotes are POSITIONAL, exactly as build_ch0608_notes.py: the Nth
numbered back-matter note (reading order) is the body for in-text mark N; the
num anchors come from data/anchors/<id>.json (anchor_offsets.py). The in-text
numbered marks come out a clean 1..N run for all three units.

The asterisk footnotes are handled DIFFERENTLY from build_ch0608's positional
approach, because two of this batch's asterisk references have NO extractable
in-text mark and so are invisible to anchor_offsets:

  * ch09 has THREE asterisk footnotes (one on p167, two on p170) but only TWO
    in-text asterisks survive in the born-digital text layer -- the reference
    mark for the p167 footnote (the Nanking-bombardment note) is absent from
    both the text layer AND the printed page image (crop-verified by eye). Its
    referent is unambiguous: the only p167 sentence about the foreign powers
    "participating directly in the suppression of the mass movement," which the
    footnote documents (American patrol, British soldiers, Japanese marines).
  * ch11's single asterisk footnote is printed as TWO foot paragraphs -- the
    Chen Tu-hsiu / Wu Chih-hui interview, then "This conversation took place on
    March 6, 1927..." The second paragraph carries NO '**' marker (crop-verified
    foot band); it is a continuation of the one '*' note, not a second footnote.

So the asterisk stream is anchored EXPLICITLY here: each foot footnote is paired
with a hand-picked, verified-unique anchor phrase in the reading, and ch11's two
foot paragraphs are joined into one note body. The foot bodies themselves are
read programmatically from the foot-classified blocks (italics as <i>,
de-hyphenated), so nothing is hand-retyped; only the anchors and the block
grouping are specified. Each assembled body is reduce-checked (letters+digits)
against the raw foot text so no drift can slip in.

Writes scratch/ch0911_author_notes.json for apparatus_merge.py.
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
    "ch09": (9, 375, 377),
    "ch10": (10, 377, 379),
    "ch11": (11, 379, 380),
}

# The asterisk page-foot footnotes, anchored EXPLICITLY (see module docstring).
# Each entry: (anchor phrase in out/<id>_reading.md, number of consecutive
# foot blocks that make up this note's body -- 1 except ch11, whose one note is
# printed as two foot paragraphs). Foot blocks are consumed in reading order.
ASTERISK = {
    "ch09": [
        ("suppression of the mass movement.", 1),   # p167 Nanking bombardment
        ("without protest.", 1),                     # p170 Hsueh Yoh
        ("founder of the Communist Party.", 1),      # p170 Li Ta-chao
    ],
    "ch10": [
        ("escaped into hiding.", 1),                 # Ku Chen-chung / Chow En-lai
        ("Chen Chuen,", 1),                          # Chen Chuen / Yang Hu
        ("cause of the revolution.”", 1),       # methods of the counterrevolution
    ],
    "ch11": [
        ("quite understand.", 2),                    # Chen Tu-hsiu / Wu Chih-hui (two paras)
    ],
}

PDF_RANGE = {"ch09": (155, 172), "ch10": (173, 182), "ch11": (183, 196)}

# A num anchor that anchor_offsets could only make unique by crossing a
# paragraph boundary (and swallowing a '{q} ' block marker) cannot be inserted
# by the builder, which places anchors per paragraph. ch09's endnote 29 sits
# after "Chen." -- the second line of the manifesto's two-line signature, whose
# paragraph is just "Chen." (not unique in the chapter). Anchor it instead to
# the unique first signature line "Signed: Wang"; the marker then renders on the
# signature block, where Isaacs set it.
ANCHOR_OVERRIDE = {
    ("ch09", "Signed: Wang\n\n{q} Chen."): "Signed: Wang",
}


def reduce(s):
    return re.sub(r"[^a-z0-9]", "", re.sub(r"<[^>]+>", "", s).lower())


def restore_hyphens(s):
    """Clean two source/cleaner artifacts the shared pipeline leaves behind:

    1. A hard hyphen fused at a line break. clean_body collapses every
       'word- word' into 'wordword', right for a soft line-break hyphen but
       wrong for a compound whose closed form is a non-word. "Kaishek" is never
       a form Isaacs writes -- it is always "Kai-shek" -- so the fused form is
       unambiguously a broken hard hyphen. (Invisible to the reduced drift
       check, which strips hyphens; caught by eye and pinned here.)
    2. A C0 control character in the born-digital text layer: ch10's endnote 9
       carries a literal NUL (0x00) where a space belongs (“Police Report
       for April,”<NUL>Municipal Gazette). A control char is an XML
       build-breaker; render it to plain sense (a space) and collapse. (Logged
       in PROGRESS as a digitization glitch.)"""
    s = s.replace("Kaishek", "Kai-shek")
    s = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", " ", s)
    return re.sub(r"\s{2,}", " ", s).strip()


def foot_blocks(chid):
    """Return the chapter's asterisk page-foot footnote bodies, in reading
    order, as cleaned XHTML (italics <i>, soft line-break hyphens fused). The
    leading '*'/'**' foot marker is stripped; a foot paragraph with no marker
    (ch11's continuation) comes through as its own block."""
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
            txt = re.sub(r"^\s*\*+\s*", "", txt)     # strip leading */** marker
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
    units = ("ch09", "ch10", "ch11")
    reading = {c: open(os.path.join(ROOT, "out", "%s_reading.md" % c),
                       encoding="utf-8").read() for c in units}
    batch = {"notes": {}}
    for chid in units:
        R = reading[chid]
        bodies = endnote_bodies(chid)
        anchors = json.load(open(os.path.join(ROOT, "data", "anchors",
                                              "%s.json" % chid)))
        num_marks = [a for a in anchors if a["kind"] == "num"]
        if len(bodies) != len(num_marks):
            sys.exit("%s: %d endnote bodies but %d numbered marks"
                     % (chid, len(bodies), len(num_marks)))

        notes = []
        # numbered endnotes: positional
        for a in num_marks:
            pos = int(a["value"])
            if not 1 <= pos <= len(bodies):
                sys.exit("%s: mark %d out of range" % (chid, pos))
            anchor = ANCHOR_OVERRIDE.get((chid, a["anchor"]), a["anchor"])
            if R.count(anchor) != 1:
                sys.exit("%s: num anchor not unique: %r" % (chid, anchor))
            notes.append({"anchor": anchor, "note": bodies[pos - 1]})

        # asterisk footnotes: explicit anchors; foot blocks consumed in order
        fblocks = foot_blocks(chid)
        fi = 0
        ast_reduced = []
        for anchor, nblocks in ASTERISK[chid]:
            body = " ".join(fblocks[fi:fi + nblocks])
            fi += nblocks
            if R.count(anchor) != 1:
                sys.exit("%s: ast anchor not unique: %r" % (chid, anchor))
            notes.append({"anchor": anchor, "note": body})
            ast_reduced.append(body)
        if fi != len(fblocks):
            sys.exit("%s: %d foot blocks, %d consumed" % (chid, len(fblocks), fi))

        # drift check: assembled asterisk bodies == raw foot text (letters+digits)
        if reduce("".join(ast_reduced)) != foot_reduced(chid):
            sys.exit("%s: asterisk body drift vs raw foot text" % chid)

        batch["notes"][chid] = notes
        print("%s: %d author notes (%d endnote + %d asterisk)"
              % (chid, len(notes), len(num_marks), len(ASTERISK[chid])))

    dest = os.path.join(ROOT, "scratch")
    os.makedirs(dest, exist_ok=True)
    path = os.path.join(dest, "ch0911_author_notes.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("wrote", path)


if __name__ == "__main__":
    main()
