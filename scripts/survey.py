#!/usr/bin/env python3
"""Structure survey: the FIRST thing to run on a new book, before any batches.

Reads book.json and reports the whole shape of the book -- how many parts,
chapters, sections and subsections; their titles; and how many pages each runs
to -- then proposes a batch breakdown for approval. Pair it with a skeleton
EPUB (`build_reading_epub.py`, which builds a fully hyperlinked table-of-contents
EPUB even with nothing translated yet) so the commissioner can see and navigate
the structure, approve the batches, and only then start Batch 1.

Page counts come from the openers' pdf_page deltas (see compute_spans); set a
book-level "pdf_end"/"printed_end" in book.json so the LAST unit's length is
known too. Cite printed folios.

Usage: survey.py [--target N] [--out out/SURVEY.md]
  --target  approx printed pages per proposed batch (default 25)
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_reading_epub import (compute_spans, part_groups, iter_openers)  # noqa

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def pages(node):
    return node.get("_pages")


def pp_range(node):
    ps, pe = node.get("_pp", (None, None))
    if ps is not None and pe is not None:
        return "%s" % ps if ps == pe else "%s-%s" % (ps, pe)
    a, b = node.get("_pdf", (None, None))
    if a is None:
        return "?"
    return "PDF %s" % a if b is None else "PDF %s-%s" % (a, b)


def propose_batches(structure, target):
    """Group whole chapters into batches near `target` printed pages. A chapter
    much larger than the target is split by its sections. Purely a suggestion."""
    batches, cur, cur_pages = [], [], 0

    def flush():
        nonlocal cur, cur_pages
        if cur:
            batches.append(cur)
            cur, cur_pages = [], 0

    for chap in structure:
        cp = pages(chap) or 0
        if cp > target * 1.6 and chap.get("sections"):
            flush()
            # split this big chapter by sections into sub-batches
            sub, sp = [], 0
            for sec in chap["sections"]:
                sc = pages(sec) or 0
                if sub and sp + sc > target:
                    batches.append([("sec", chap, sub)])
                    sub, sp = [], 0
                sub.append(sec)
                sp += sc
            if sub:
                batches.append([("sec", chap, sub)])
            continue
        if cur and cur_pages + cp > target:
            flush()
        cur.append(chap)
        cur_pages += cp
    flush()
    return batches


def batch_label(batch):
    """batch is a list of chapters, or a single [("sec", chap, [sections])]."""
    if batch and isinstance(batch[0], tuple) and batch[0][0] == "sec":
        _, chap, secs = batch[0]
        first, last = secs[0], secs[-1]
        p = sum(pages(s) or 0 for s in secs)
        rng = first["id"] if first is last else "%s-%s" % (first["id"], last["id"])
        span = "%s-%s" % (pp_range(first).split("-")[0],
                          pp_range(last).split("-")[-1])
        if first is last:
            title = "%s, %s" % (chap["title_en"], first["title_en"])
        else:
            title = "%s, %s to %s" % (chap["title_en"], first["title_en"],
                                      last["title_en"])
        return rng, span, p, title
    first, last = batch[0], batch[-1]
    p = sum(pages(c) or 0 for c in batch)
    rng = first["id"] if first is last else "%s-%s" % (first["id"], last["id"])
    span = "%s-%s" % (pp_range(first).split("-")[0],
                      pp_range(last).split("-")[-1])
    if first is last:
        title = first["title_en"]
    else:
        title = "%s through %s" % (first["title_en"], last["title_en"])
    return rng, span, p, title


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", type=int, default=25,
                    help="approx printed pages per proposed batch (default 25)")
    ap.add_argument("--out", default=os.path.join(ROOT, "out", "SURVEY.md"))
    a = ap.parse_args()

    book = json.load(open(os.path.join(ROOT, "book.json")))
    structure = [c for c in book.get("structure", [])
                 if c.get("id", "").startswith("ch")]
    if not structure:
        sys.exit("book.json has no chapters in 'structure'")
    compute_spans(structure, book)

    n_ch = len(structure)
    n_sec = sum(len(c.get("sections", [])) for c in structure)
    n_sub = sum(len(s.get("subsections", [])) for c in structure
                for s in c.get("sections", []))
    groups = part_groups(structure)
    n_parts = sum(1 for lbl, _ in groups if lbl)
    total_pages = sum(pages(c) or 0 for c in structure)

    L = []
    L.append("# Structure survey - %s" % book.get("title_en", "(untitled)"))
    L.append("")
    L.append("| | count |")
    L.append("|---|---|")
    if n_parts:
        L.append("| Parts | %d |" % n_parts)
    L.append("| Chapters | %d |" % n_ch)
    L.append("| Sections | %d |" % n_sec)
    if n_sub:
        L.append("| Subsections | %d |" % n_sub)
    L.append("| Body pages (known) | %d |" % total_pages)
    L.append("")
    L.append("## Full outline")
    L.append("")
    for part_label, chaps in groups:
        if part_label:
            L.append("### %s" % part_label)
        for chap in chaps:
            L.append("- **%s** &mdash; %s (%s pp.)"
                     % (chap["title_en"], pp_range(chap),
                        pages(chap) if pages(chap) is not None else "?"))
            for sec in chap.get("sections", []):
                L.append("  - %s &mdash; %s (%s pp.)"
                         % (sec["title_en"], pp_range(sec),
                            pages(sec) if pages(sec) is not None else "?"))
                for sub in sec.get("subsections", []):
                    L.append("    - %s" % sub["title_en"])
    L.append("")
    L.append("## Suggested batches (target ~%d printed pages each)" % a.target)
    L.append("")
    L.append("Approve or adjust these, then Batch 1 begins.")
    L.append("")
    L.append("| Batch | Units | Pages | Span | Covers |")
    L.append("|---|---|---|---|---|")
    for i, batch in enumerate(propose_batches(structure, a.target), 1):
        rng, span, p, title = batch_label(batch)
        L.append("| B%02d | %s | %d | %s | %s |" % (i, rng, p, span, title))
    L.append("")
    L.append("_Page counts derive from opener-to-opener deltas; set "
             "book.json `pdf_end`/`printed_end` so the last unit's length is "
             "known. Verify every opener's folio against the scan._")

    text = "\n".join(L) + "\n"
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w").write(text)
    print(text)
    print("wrote %s" % a.out)


if __name__ == "__main__":
    main()
