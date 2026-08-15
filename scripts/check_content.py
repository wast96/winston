#!/usr/bin/env python3
"""Verify that paired paragraphs hold the SAME CONTENT, not merely the same
volume of it.

WHY THIS EXISTS ALONGSIDE check_align.py. That script compares the ratio of
English characters to Han characters and reports a run of pairs where the
ratio collapses or explodes. It is the right check for text that has gone
MISSING. It is structurally blind to text that has been MISPLACED, because a
displacement preserves every ratio: each paragraph still receives about the
right amount of English, just not the right sentences.

That blindness has cost this project twice. ch03 carried a skipped paragraph
and a one-place offset that check_align passed as "alignment OK". ch02 had its
boundaries slipped by one across roughly forty paragraphs -- the assassination
narrative and the Lu Haifang episode -- and check_align passed that too. Both
times the thing that found it was content: a numeral in a paragraph whose
translation did not contain it, and a proper name sitting one paragraph later
in the English than in the Chinese.

So this check asks the only question that catches it. For every source
paragraph, take the proper names the glossary maps into English, and require
that the paragraph paired with it actually contains them. The glossary is
already maintained as a hanzi-to-English key, one rendering per referent, so
it is exactly the cross-lingual fixed point needed and costs nothing to reuse.

Generic renderings are excluded deliberately. 特务 -> "secret agent /
operative" never appears in the prose in that literal form and would report a
phantom miss on every paragraph that mentions an operative, which is most of
them. Only entries whose English looks like a name -- capitalised, no slash,
long enough not to collide by accident -- are used.

The check is one-directional on purpose: a name may legitimately appear in the
English where the Chinese used a pronoun, so an EXTRA occurrence is not a
fault. A name the source has and the translation lacks is.

Usage: check_content.py [--config book.json]
"""
import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# The author's own name is not usable as an anchor. This is a first-person
# memoir in which Shen Zui repeatedly names himself in the third person -- he
# appears in his own roster of instructors -- and the only correct English for
# that is "me". Every such place would otherwise be reported as displaced.
AUTHOR = {"沈醉"}


def name_map(path):
    """hanzi -> English, restricted to distinctive proper names."""
    out = {}
    if not os.path.exists(path):
        return out
    for _cat, entries in json.load(open(path)).items():
        # keys starting with '_' are documentation, not sections (matches the
        # builder's convention); their values may be plain strings.
        if _cat.startswith("_") or not isinstance(entries, dict):
            continue
        for zh, e in entries.items():
            en = e.get("en", "")
            if zh in AUTHOR:
                continue
            if len(zh) < 2 or "/" in en or len(en) < 4:
                continue
            if not en[0].isupper():
                continue
            out[zh] = en
    return out


def paragraphs(src_path, tgt_path):
    src = [l.rstrip("\n") for l in open(src_path) if l.strip()]
    src = [l for l in src if not l.startswith("###")]
    tgt = [l.strip() for l in open(tgt_path)
           if l.strip() and not l.strip().startswith("#")]
    return src, tgt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default=os.path.join(ROOT, "book.json"))
    ap.add_argument("--glossary", default=os.path.join(ROOT, "glossary.json"))
    a = ap.parse_args()

    cfg = json.load(open(a.config))
    names = name_map(a.glossary)
    print("content alignment: %d glossary names usable as anchors" % len(names))

    failed = False
    if not cfg.get("docs"):
        print("check_content: config has no 'docs' map; NOTHING was checked. "
              "Pass --config with a check_structure-style config "
              "({docs:{id:path}, sources:{id:path}}); a check that quietly "
              "measures nothing is worse than no check.")
        sys.exit(1)
    for unit, doc in cfg.get("docs", {}).items():
        src_path = os.path.join(ROOT, cfg["sources"][unit])
        tgt_path = os.path.join(ROOT, doc)
        if not (os.path.exists(src_path) and os.path.exists(tgt_path)):
            continue
        src, tgt = paragraphs(src_path, tgt_path)
        if len(src) != len(tgt):
            print("  %-14s SKIPPED: %d source paragraphs, %d translation "
                  "(run check_structure first)" % (unit, len(src), len(tgt)))
            failed = True
            continue
        occurrences = 0
        misses = []
        for i, (z, e) in enumerate(zip(src, tgt)):
            want = {en for zh, en in names.items() if zh in z}
            occurrences += len(want)
            gone = sorted(n for n in want if n not in e)
            if gone:
                misses.append((i + 1, gone))
        if misses:
            failed = True
            print("  %-14s %d name occurrences, %d DISPLACED"
                  % (unit, occurrences, sum(len(g) for _, g in misses)))
            for p, gone in misses[:12]:
                print("       paragraph %-4d source has %s, translation does "
                      "not" % (p, ", ".join(gone)))
            if len(misses) > 12:
                print("       ... and %d more" % (len(misses) - 12))
        else:
            print("  %-14s %d name occurrences, all in the paired paragraph"
                  % (unit, occurrences))

    print("\nCONTENT ALIGNMENT FAILURES" if failed
          else "\ncontent alignment OK across all units")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
