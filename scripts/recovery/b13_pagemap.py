#!/usr/bin/env python3
# Regenerate data/pagemap/<unit>.json for the post-surgery ZH structure (B13).
# Copy of b11_pagemap.py with the build() calls retargeted to ch23/ch24.
import json, os, re

ROOT = "/home/user/winston"
TXT = os.path.join(ROOT, "data", "txt")
ZH = os.path.join(ROOT, "data", "zh")
PAGEMAP = os.path.join(ROOT, "data", "pagemap")
LEDGER = json.load(open(os.path.join(ROOT, "data", "ocr_fixes.json")))


def fix(s, unit):
    for f in LEDGER.get(unit, []):
        s = s.replace(f["wrong"], f["right"])
    return s


def first_body_snippet(page, unit, heads):
    p = os.path.join(TXT, "p%04d.txt" % page)
    for l in open(p):
        s = fix(l.strip(), unit)
        if not s:
            continue
        sc = re.sub(r"\s", "", s)
        if sc in heads:
            continue
        return sc[:12]
    return None


def build(unit, first, last, offset=44):
    paras = [l.rstrip("\n") for l in open(os.path.join(ZH, "%s.txt" % unit))]
    joined = []
    b = 0
    for p in paras:
        if p.startswith("###"):
            continue
        joined.append((b, re.sub(r"\s", "", p)))
        b += 1
    heads = {re.sub(r"\s", "", p[4:]) for p in paras if p.startswith("###")}

    mapping = []
    cur = 0
    for page in range(first, last + 1):
        snip = first_body_snippet(page, unit, heads)
        if snip is None:
            continue
        found = None
        for bi, txt in joined:
            if bi < cur:
                continue
            if snip and snip in txt:
                found = bi
                break
        if found is None:
            for bi, txt in joined:
                if bi < cur:
                    continue
                if snip[:6] and snip[:6] in txt:
                    found = bi
                    break
        if found is None:
            print("  p%d: snippet %r NOT FOUND (cur=%d)" % (page, snip, cur))
            found = cur
        mapping.append({"printed": page - offset, "pdf": page,
                        "body_paragraph": found})
        cur = found
    with open(os.path.join(PAGEMAP, "%s.json" % unit), "w") as fh:
        json.dump(mapping, fh, ensure_ascii=False, indent=1)
    print("%s: %d pages, printed %d-%d, body idx %d-%d"
          % (unit, len(mapping), mapping[0]["printed"], mapping[-1]["printed"],
             mapping[0]["body_paragraph"], mapping[-1]["body_paragraph"]))
    prev = -1
    for m in mapping:
        if m["body_paragraph"] < prev:
            print("  NON-MONOTONIC at printed %d: %d < %d"
                  % (m["printed"], m["body_paragraph"], prev))
        prev = m["body_paragraph"]


build("ch23", 485, 526)
build("ch24", 527, 552)
