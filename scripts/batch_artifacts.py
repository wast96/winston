#!/usr/bin/env python3
"""Derive per-unit out/<id>_en.json from out/<id>_reading.md, and emit a
check_structure/check_content config for the batch's translated units.

out/<id>_en.json is the flat array of English paragraphs (the tracked authored
English), one per source body line: exactly the reading.md lines that are not
blank, not a heading ('#'), not a scene break ('***'), with any {vdgp} set-off
prefix stripped — the same body() rule verify_unit and the checks use.

The config lists every unit that has a reading.md, mapping id -> reading path
and id -> data/zh path, plus notes.json and a variants block for drift.

Usage: batch_artifacts.py ch01 ch02 ...    (default: all ch* with reading.md)
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def body_lines(path):
    out = []
    for l in open(path, encoding="utf-8"):
        s = l.strip()
        if not s or s == "***" or s.startswith("#"):
            continue
        out.append(re.sub(r"^\{[vdgp]\} ", "", s))
    return out


def main(cids):
    if not cids:
        cids = sorted(os.path.basename(p)[:-len("_reading.md")]
                      for p in glob.glob(os.path.join(ROOT, "out", "ch*_reading.md")))
    docs, sources = {}, {}
    for cid in cids:
        rd = os.path.join(ROOT, "out", "%s_reading.md" % cid)
        if not os.path.exists(rd):
            print("skip %s: no reading.md" % cid)
            continue
        en = body_lines(rd)
        dest = os.path.join(ROOT, "out", "%s_en.json" % cid)
        json.dump(en, open(dest, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        docs[cid] = "out/%s_reading.md" % cid
        sources[cid] = "data/zh/%s.txt" % cid
        print("%s: wrote %s (%d paragraphs)" % (cid, dest, len(en)))
    cfg = {"docs": docs, "sources": sources,
           "notes": "notes.json", "heading_depth": 2}
    json.dump(cfg, open(os.path.join(ROOT, "checks.json"), "w"), indent=2)
    print("wrote checks.json (%d units)" % len(docs))


if __name__ == "__main__":
    main(sys.argv[1:])
