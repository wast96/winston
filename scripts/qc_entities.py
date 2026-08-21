#!/usr/bin/env python3
"""QC: no named entity silently dropped or re-rendered.

Reads the same bilingual audit format as check_invariants (source blockquote
above English paragraph). For every glossary entry whose hanzi appears in a
source paragraph, require that the decided English rendering (or its pinyin)
appears in the paired English paragraph. Reports misses; exit 1 if any.

Whole-file totals are also printed so a chapter's entity census can be eyed
against the source in one line.

Usage: qc_entities.py out/chNN_bilingual.md [glossary.json]
"""
import json
import re
import sys


def pairs(path):
    src, buf = None, []
    for line in open(path):
        if line.startswith(">"):
            if src is not None and buf:
                yield src, " ".join(buf)
                buf = []
            src = line.lstrip("> ").strip()
        elif line.strip() and not line.startswith(("#", "---", "**", "`")):
            if src is not None:
                buf.append(line.strip())
    if src is not None and buf:
        yield src, " ".join(buf)


# 严重 is the ch10 courier Yan Zhong but also the ubiquitous adjective
# "severe" (极其严重 "extremely grave," 白色恐怖最严重 "the height of the White
# Terror"); as an entity-map key it flags every adjectival use. Same homograph
# fix already applied to check_content.py (B13). Keep the two lists in sync.
HOMOGRAPHS = {"严重"}


def main(path, gloss_path="glossary.json"):
    gloss = json.load(open(gloss_path))
    flat = {}
    for section in gloss.values():
        if not isinstance(section, dict):
            continue
        for zh, rec in section.items():
            # keys like 盒子枪/驳壳枪 hold alternate hanzi for one referent
            for form in zh.split("/"):
                if form in HOMOGRAPHS:
                    continue
                flat[form] = rec

    bad = 0
    totals = {}
    for i, (src, tgt) in enumerate(pairs(path), 1):
        low = tgt.lower()
        for form, rec in flat.items():
            hits = src.count(form)
            if not hits:
                continue
            totals[form] = totals.get(form, 0) + hits
            en_ok = rec["en"].lower() in low
            py_ok = rec["pinyin"].lower() in low
            # surname-only mentions are normal Chinese usage; accept the
            # rendering's final word (family or given name) as presence
            last_ok = rec["en"].split()[-1].lower() in low or \
                rec["en"].split()[0].lower() in low
            if not (en_ok or py_ok or last_ok):
                bad += 1
                print("pair %d: %s (%s) not found in English" %
                      (i, form, rec["en"]))
                print("   zh:", src[:60])
                print("   en:", tgt[:70])
    seen = ", ".join("%s x%d" % (k, v) for k, v in
                     sorted(totals.items(), key=lambda kv: -kv[1])[:12])
    print("entity census (top): %s" % (seen or "none"))
    print("entity misses: %d" % bad)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
