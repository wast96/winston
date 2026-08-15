#!/usr/bin/env python3
# Regenerate data/pagemap/<unit>.json for the post-surgery ZH structure.
# The assemble.py auto-map is stale after surgery (splits/welds changed body
# indices). For each PDF page we take a distinctive snippet of its first BODY
# line (from data/txt, with the same ocr_fixes applied), find which final-ZH
# body paragraph contains it (monotonic scan), and record
# {printed, pdf, body_paragraph}.  qa_epub checks only marker/page-list count
# parity, but accurate indices keep folio citations landing on the right page.
import json, os, re, sys

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
        if sc in heads:          # page opens on a (normalized) heading; skip it
            continue
        # a snippet long enough to be unique, short enough to survive a
        # mid-line weld boundary
        return sc[:12]
    return None


def build(unit, first, last, offset=44):
    body = []
    idx_of = {}
    paras = [l.rstrip("\n") for l in open(os.path.join(ZH, "%s.txt" % unit))]
    b = 0
    joined = []
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
        if snip in heads or any(h.startswith(snip) for h in heads):
            # page opens on a heading; use the first body line AFTER it
            pass
        found = None
        for bi, txt in joined:
            if bi < cur:
                continue
            if snip and snip in txt:
                found = bi
                break
        if found is None:
            # fall back: relax the snippet
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
    # monotonic check
    prev = -1
    for m in mapping:
        if m["body_paragraph"] < prev:
            print("  NON-MONOTONIC at printed %d: %d < %d"
                  % (m["printed"], m["body_paragraph"], prev))
        prev = m["body_paragraph"]


build("ch07", 154, 172)
build("ch08", 173, 197)
