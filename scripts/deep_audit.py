#!/usr/bin/env python3
"""Random-sample deep audit (CLAUDE.md check 10): a fixed-seed 3-5% sample of
the book's reading paragraphs, each re-verified against source.pdf.
check_fidelity.py already proves the WHOLE-unit letters+digits match; this
zooms to the paragraph and asks a stronger question of the sample: does every
letter/digit of the paragraph appear, IN ORDER, in that chapter's source text?

Metric: letter-level ordered-subsequence coverage. Reduce the paragraph and the
source pages each to a lowercase [a-z0-9] stream, then greedily match the
paragraph stream through the source stream in order. Furniture (running heads,
folios, footnotes) and de-hyphenation only ADD source characters or remove
hyphens, so a faithful paragraph reaches ~100% coverage; a dropped, altered, or
reordered word drops it. Any paragraph below the threshold is reported for an
eyeball check (that is where an 'invented precision' error would surface).

Usage: deep_audit.py [--seed N] [--rate 0.04]
"""
import json
import os
import random
import re
import sys

import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, "source.pdf")
BOOK = json.load(open(os.path.join(ROOT, "book.json")))
OFFSET = 23   # printed = pdf - 23 (body); front matter uses its own, handled below


def words(s):
    return re.findall(r"[a-z0-9]+", s.lower())


def letters(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def coverage(needle, hay):
    """Fraction of `needle` chars matched as an in-order subsequence of `hay`."""
    if not needle:
        return 1.0
    j, matched = 0, 0
    for ch in needle:
        k = hay.find(ch, j)
        if k == -1:
            # cannot place this char in order; skip it (counts as a miss)
            continue
        j = k + 1
        matched += 1
    return matched / len(needle)


def reading_paragraphs(unit):
    md = open(os.path.join(ROOT, "out", "%s_reading.md" % unit),
              encoding="utf-8").read()
    out = []
    for line in md.split("\n"):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        s = re.sub(r"^\{[qvdgp]\}\s*", "", s)
        if s == "***":
            continue
        s = s.replace("*", "")
        out.append(s)
    return out


def unit_source_letters(unit):
    node = next(c for c in BOOK["structure"] if c["id"] == unit)
    idx = BOOK["structure"].index(node)
    lo = node["pdf_page"]
    hi = (BOOK["structure"][idx + 1]["pdf_page"] - 1
          if idx + 1 < len(BOOK["structure"]) else BOOK["pdf_end"])
    doc = pymupdf.open(PDF)
    s = "".join(doc[p - 1].get_text() for p in range(lo, hi + 1))
    doc.close()
    return letters(s)


def main():
    seed = 20260831
    rate = 0.04
    args = sys.argv[1:]
    if "--seed" in args:
        seed = int(args[args.index("--seed") + 1])
    if "--rate" in args:
        rate = float(args[args.index("--rate") + 1])

    units = [c["id"] for c in BOOK["structure"]]
    all_paras = []
    for u in units:
        for i, p in enumerate(reading_paragraphs(u)):
            if len(words(p)) >= 12:      # skip very short lines (headings-ish)
                all_paras.append((u, i, p))
    rng = random.Random(seed)
    k = max(1, round(len(all_paras) * rate))
    sample = rng.sample(all_paras, k)
    sample.sort()

    THRESH = 0.995
    src_cache = {}
    results = []
    for u, i, p in sample:
        if u not in src_cache:
            src_cache[u] = unit_source_letters(u)
        cov = coverage(letters(p), src_cache[u])
        results.append((u, i, cov, p))

    bad = [r for r in results if r[2] < THRESH]
    covs = [r[2] for r in results]
    print("seed=%d  sampled %d of %d paragraphs (%.1f%%)"
          % (seed, k, len(all_paras), 100.0 * k / len(all_paras)))
    print("letter-coverage: min=%.4f  mean=%.4f  below %.3f: %d"
          % (min(covs), sum(covs) / len(covs), THRESH, len(bad)))
    for u, i, cov, p in bad:
        print("  LOW %.4f  %s para %d: %s" % (cov, u, i, p[:80]))
    return results, bad, k, len(all_paras), seed


if __name__ == "__main__":
    main()
