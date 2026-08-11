#!/usr/bin/env python3
"""Whole-book random-sample deep audit sampler (final batch).

Pairs each unit's source paragraphs (data/zh/<id>.txt, minus the ### heading)
with its English reading paragraphs (out/<id>_reading.md, minus the ## heading
and any '***' scene-break lines) 1:1 -- parity is guaranteed by
check_structure. Draws a FIXED-SEED random sample of ~SAMPLE_PCT% of all
paragraphs across the whole book and writes them, in reading order, to
out/deep_audit.md for a line-by-line faithfulness read.

Deterministic: same seed + same text -> same sample every run.
"""
import glob
import json
import os
import random
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEED = 20260811
SAMPLE_PCT = 3.0

book = json.load(open(os.path.join(ROOT, "book.json"), encoding="utf-8"))
order = [c["id"] for c in book["structure"]]

pairs = []  # (unit, idx_within_unit, zh, en)
for uid in order:
    zpath = os.path.join(ROOT, "data", "zh", "%s.txt" % uid)
    rpath = os.path.join(ROOT, "out", "%s_reading.md" % uid)
    zlines = [l.rstrip("\n") for l in open(zpath, encoding="utf-8")]
    zlines = [l for l in zlines if l and not l.startswith("###")]
    blocks = open(rpath, encoding="utf-8").read().split("\n\n")
    en = []
    for b in blocks:
        b = b.strip()
        if not b or b == "***" or b.startswith("#"):
            continue
        en.append(" ".join(b.split()))
    if len(zlines) != len(en):
        raise SystemExit("PARITY MISMATCH %s: zh %d en %d"
                         % (uid, len(zlines), len(en)))
    for i, (z, e) in enumerate(zip(zlines, en), 1):
        pairs.append((uid, i, z, e))

total = len(pairs)
k = round(total * SAMPLE_PCT / 100.0)
rng = random.Random(SEED)
idx = sorted(rng.sample(range(total), k))

out = ["# Whole-book deep audit sample",
       "",
       "Fixed seed %d; %.1f%% of %d paragraphs = %d sampled pairs, in reading "
       "order. Each pair read zh-against-en for faithfulness (omission, "
       "addition, mistranslation, invented precision)." % (SEED, SAMPLE_PCT,
                                                            total, k),
       ""]
for n, j in enumerate(idx, 1):
    uid, i, z, e = pairs[j]
    out.append("## %d. %s para %d" % (n, uid, i))
    out.append("zh: %s" % z)
    out.append("en: %s" % e)
    out.append("")

dest = os.path.join(ROOT, "out", "deep_audit.md")
with open(dest, "w", encoding="utf-8") as fh:
    fh.write("\n".join(out) + "\n")
print("wrote %s: %d pairs sampled from %d (seed %d)" % (dest, k, total, SEED))
