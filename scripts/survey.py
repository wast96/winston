#!/usr/bin/env python3
"""Structure survey for an EPUB source: the FIRST thing after ingest, before any
batch. Reads book.json and reports the whole shape of the book -- how many parts,
chapters, sections and subsections; their titles; and how large each is (in
source characters, the natural size metric for Chinese) -- then proposes a batch
breakdown for approval.

Pair it with a skeleton EPUB (`build_reading_epub.py`, which builds a fully
hyperlinked table-of-contents EPUB even with nothing translated yet) so the
commissioner can see and navigate the structure, approve the batches, and only
then start Batch 1.

Sizes come from each unit's 'chars' (filled by ingest_epub.py). If a unit has no
'chars', the survey counts its 'text_file' when present, else shows it as "?".

Usage: survey.py [--target N] [--out out/SURVEY.md]
  --target  approx source characters per proposed batch (default 12000)
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_reading_epub import part_groups  # noqa

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def chars(node):
    if node.get("chars") is not None:
        return node["chars"]
    tf = node.get("text_file")
    if tf and os.path.exists(os.path.join(ROOT, tf)):
        text = open(os.path.join(ROOT, tf)).read()
        return len(re.findall(r"[㐀-鿿豈-﫿]", text))
    return None


def sec_chars(chap):
    """Chapter size falls back to the sum of its sections' sizes."""
    c = chars(chap)
    if c is not None:
        return c
    subs = [chars(s) or 0 for s in chap.get("sections", [])]
    return sum(subs) if subs else None


def fmt(n):
    return "?" if n is None else "{:,}".format(n)


def propose_batches(structure, target):
    batches, cur, cur_c = [], [], 0

    def flush():
        nonlocal cur, cur_c
        if cur:
            batches.append(cur)
            cur, cur_c = [], 0

    for chap in structure:
        cc = sec_chars(chap) or 0
        if cc > target * 1.6 and chap.get("sections"):
            flush()
            sub, sc = [], 0
            for sec in chap["sections"]:
                s = chars(sec) or 0
                if sub and sc + s > target:
                    batches.append([("sec", chap, sub)])
                    sub, sc = [], 0
                sub.append(sec)
                sc += s
            if sub:
                batches.append([("sec", chap, sub)])
            continue
        if cur and cur_c + cc > target:
            flush()
        cur.append(chap)
        cur_c += cc
    flush()
    return batches


def batch_row(i, batch):
    def t(node):
        return node.get("title_en") or node.get("title") or node["id"]
    if batch and isinstance(batch[0], tuple) and batch[0][0] == "sec":
        _, chap, secs = batch[0]
        first, last = secs[0], secs[-1]
        c = sum(chars(s) or 0 for s in secs)
        rng = first["id"] if first is last else "%s-%s" % (first["id"], last["id"])
        if first is last:
            title = "%s, %s" % (t(chap), t(first))
        else:
            title = "%s, %s to %s" % (t(chap), t(first), t(last))
        return "| B%02d | %s | %s | %s |" % (i, rng, fmt(c), title)
    first, last = batch[0], batch[-1]
    c = sum(sec_chars(x) or 0 for x in batch)
    rng = first["id"] if first is last else "%s-%s" % (first["id"], last["id"])
    title = t(first) if first is last else "%s through %s" % (t(first), t(last))
    return "| B%02d | %s | %s | %s |" % (i, rng, fmt(c), title)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", type=int, default=12000,
                    help="approx source characters per proposed batch")
    ap.add_argument("--out", default=os.path.join(ROOT, "out", "SURVEY.md"))
    a = ap.parse_args()

    book = json.load(open(os.path.join(ROOT, "book.json")))
    structure = [c for c in book.get("structure", [])
                 if c.get("id", "").startswith("ch")]
    if not structure:
        sys.exit("book.json has no chapters in 'structure'")

    def t(node):
        return node.get("title_en") or node.get("title") or node["id"]

    n_ch = len(structure)
    n_sec = sum(len(c.get("sections", [])) for c in structure)
    n_sub = sum(len(s.get("subsections", [])) for c in structure
                for s in c.get("sections", []))
    groups = part_groups(structure)
    n_parts = sum(1 for lbl, _ in groups if lbl)
    total = sum(sec_chars(c) or 0 for c in structure)

    L = ["# Structure survey - %s" % (book.get("title_en")
                                      or book.get("title_zh") or "(untitled)"),
         "", "| | count |", "|---|---|"]
    if n_parts:
        L.append("| Parts | %d |" % n_parts)
    L.append("| Chapters | %d |" % n_ch)
    L.append("| Sections | %d |" % n_sec)
    if n_sub:
        L.append("| Subsections | %d |" % n_sub)
    L.append("| Source characters | %s |" % fmt(total))
    L += ["", "## Full outline", ""]
    for part_label, chaps in groups:
        if part_label:
            L.append("### %s" % part_label)
        for chap in chaps:
            L.append("- **%s** &mdash; %s chars" % (t(chap), fmt(sec_chars(chap))))
            for sec in chap.get("sections", []):
                L.append("  - %s &mdash; %s chars" % (t(sec), fmt(chars(sec))))
                for sub in sec.get("subsections", []):
                    L.append("    - %s" % t(sub))
    L += ["", "## Suggested batches (target ~%s source chars each)"
          % "{:,}".format(a.target), "",
          "Approve or adjust these, then Batch 1 begins.", "",
          "| Batch | Units | Chars | Covers |", "|---|---|---|---|"]
    for i, batch in enumerate(propose_batches(structure, a.target), 1):
        L.append(batch_row(i, batch))
    L += ["", "_Sizes are source characters; set each unit's `chars` (ingest "
          "fills this) so batches size correctly._"]

    text = "\n".join(L) + "\n"
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w").write(text)
    print(text)
    print("wrote %s" % a.out)


if __name__ == "__main__":
    main()
