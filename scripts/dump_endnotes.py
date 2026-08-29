#!/usr/bin/env python3
"""One-off helper: dump Isaacs's own endnote texts for a chapter (verbatim,
italics as <i>), and the in-text context preceding each reference mark, so the
notes.json author-note bodies and anchors can be transcribed accurately."""
import re
import sys
import pymupdf

PDF = "source.pdf"


def spans_text(line, keep_sup=True):
    out, ital = [], False
    for s in line["spans"]:
        t = s["text"]
        if (s["flags"] & 1) and not keep_sup:
            continue
        is_ital = bool(s["flags"] & 2)
        if is_ital and not ital:
            out.append("<i>"); ital = True
        elif not is_ital and ital:
            out.append("</i>"); ital = False
        out.append(t)
    if ital:
        out.append("</i>")
    return "".join(out)


def endnotes(chnum, first_pdf, last_pdf):
    """Read the endnote pages, capture the block-run for the chapter heading
    'chnum. <title>' up to the next chapter heading, split on leading numbers."""
    doc = pymupdf.open(PDF)
    lines = []
    for idx in range(first_pdf - 1, last_pdf):
        page = doc[idx]
        blocks = [b for b in page.get_text("dict")["blocks"] if "lines" in b]
        blocks.sort(key=lambda b: b["bbox"][1])
        for b in blocks:
            szs = [round(s["size"], 1) for l in b["lines"]
                   for s in l["spans"] if s["text"].strip()]
            if not szs:
                continue
            dom = max(set(szs), key=szs.count)
            if dom >= 12.5:                 # chapter heading in the notes
                txt = "".join(s["text"] for l in b["lines"]
                              for s in l["spans"]).strip()
                lines.append(("HEAD", txt))
            elif 7.4 <= dom <= 8.6:         # note text
                txt = " ".join(spans_text(l) for l in b["lines"])
                lines.append(("NOTE", txt))
    doc.close()
    return lines


def main():
    chnum = int(sys.argv[1])
    first_pdf, last_pdf = int(sys.argv[2]), int(sys.argv[3])
    for kind, txt in endnotes(chnum, first_pdf, last_pdf):
        print("[%s] %s" % (kind, txt))


if __name__ == "__main__":
    main()
