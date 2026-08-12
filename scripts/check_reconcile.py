#!/usr/bin/env python3
"""Whole-book reconciliation: the cross-chapter drift no per-unit check sees.

Mechanizes QC check 12 (and the epithet half of the review pass). Real
catches this class of check made on finished books: a repeated epithet
(杏仁色, one character's teeth) rendered THREE ways across 13 batches,
including a British/American spelling split; a decided glossary rendering
("River of Fury") simply ignored in two chapters; rendering/first-appearance
mismatches (投名状, 双陆) where the explanatory note sat on the LATER
occurrence.

What it does:

  1. EPITHET DRIFT (needs data/zh/). Collects source character n-grams
     (2-4 chars) that recur 3+ times book-wide, excluding pure function-word
     grams. For each, looks at the paired English lines and flags phrases
     whose pairings share no common content word — the signature of a
     rendering that drifted. Heuristic by design: it prints candidates for a
     human read, it does not auto-fail. Watch phrases can be pinned in a
     --terms file (one zh phrase per line) for exact tracking.
  2. GLOSSARY FORWARD. Every glossary `en` form should appear somewhere in
     the built text (an unused decided form usually means the prose ignored
     the glossary); every `variants` wrong-form (from the check_structure
     config, wrong forms ONLY) should appear nowhere.
  3. SPELLING LOCALE. Counts -our/-or and -ise/-ize families across all
     reading files and flags a mixed book (two finished books shipped mixed).

Exit 1 only on glossary-forward failures (2); 1 and 3 print for adjudication.

Usage:
    check_reconcile.py                     # all units with a reading file
    check_reconcile.py --terms watched.txt # pin exact phrases
"""
import argparse
import json
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CJK = r"[一-鿿]"
# single-char grams and grams made only of these never carry an epithet
FUNC = set("的了是在有和不与与也就都而及等这那其之于对上下中人一二三"
           "他她它们你我个了着过说道来去到得地很么什没")

STOP_EN = set("""the a an and or of to in on at for with by from as is was
were are be been his her its their he she it they them this that had has
have not no one two out up into over after before all so said says say
""".split())


def body_lines(path):
    out = []
    for l in open(path, encoding="utf-8"):
        s = l.strip()
        if not s or s == "***" or s.startswith("#"):
            continue
        out.append(re.sub(r"^\{[vdgpj]\} ", "", s))
    return out


def content_words(line):
    return {w.lower().strip(".,;:!?\"'()") for w in line.split()
            if w.lower().strip(".,;:!?\"'()") not in STOP_EN and len(w) > 3}


def epithet_drift(units, watched):
    gram_lines = defaultdict(list)   # gram -> [(unit, en_line)]
    charfreq = defaultdict(int)
    for cid, (zh_path, en_path) in units.items():
        for line in body_lines(zh_path):
            for ch in line:
                charfreq[ch] += 1
    # Adaptive rarity gate: an epithet worth tracking (杏仁色) carries at
    # least one character OUTSIDE the book's ~150 most frequent; grams built
    # entirely from everyday characters (的笑声, 现在还) are connective
    # prose whose free rendering legitimately varies, and flagging them
    # buried the one real signal under hundreds of false candidates.
    common = {c for c, _ in sorted(charfreq.items(),
                                   key=lambda kv: -kv[1])[:150]}
    for cid, (zh_path, en_path) in units.items():
        zh, en = body_lines(zh_path), body_lines(en_path)
        if len(zh) != len(en):
            print("  drift: %s parity %d|%d, skipped (fix parity first)"
                  % (cid, len(zh), len(en)))
            continue
        for z, e in zip(zh, en):
            grams = set()
            # 3-4 char grams only: 2-char grams are dominated by ordinary
            # verb phrases (抬头, 点了) whose free rendering legitimately
            # varies; the drift class that shipped (杏仁色) is a descriptive
            # compound. At most one function char per gram.
            for n in (3, 4):
                for i in range(len(z) - n + 1):
                    g = z[i:i + n]
                    if re.fullmatch(CJK + "{%d}" % n, g) and \
                            sum(c in FUNC for c in g) <= 1 and \
                            any(c not in common for c in g):
                        grams.add(g)
            for g in grams:
                gram_lines[g].append((cid, e))
    # glossary zh terms are covered by qc_entities/glossary-forward; skip
    gz = set()
    gpath = os.path.join(ROOT, "glossary.json")
    if os.path.exists(gpath):
        def collect(d):
            for k, v in d.items():
                if k.startswith("_"):
                    continue
                if isinstance(v, dict) and "en" in v:
                    gz.add(k)
                elif isinstance(v, dict):
                    collect(v)
        collect(json.load(open(gpath, encoding="utf-8")))
    # THE DETECTOR, learned from the real incident: drifted renderings
    # usually KEEP their head word and vary around it (almond-tinted /
    # almond-coloured / almond-white all share "almond"). So: find the
    # content word shared by most pairings (the rendering anchor), then flag
    # when the full token built on it takes more than one form. Pairings
    # with NO shared word are free prose, not drift, and flagging them
    # buried the signal under thousands of false candidates.
    flagged = 0
    reported = set()
    for g, occ in sorted(gram_lines.items(), key=lambda kv: -len(kv[1])):
        if any(g in term for term in gz):
            continue
        occ = list({(c, e) for c, e in occ})
        if g not in watched and (len(occ) < 3 or len(occ) > 15):
            continue                 # too rare to drift, or too common to read
        toklists = [[w.lower().strip(".,;:!?\"\u201c\u201d\u2018\u2019()")
                     for w in e.split()] for _, e in occ]
        stem_count = defaultdict(int)
        for toks in toklists:
            for stem in {t.split("-")[0] for t in toks
                         if len(t.split("-")[0]) > 3
                         and t.split("-")[0] not in STOP_EN}:
                stem_count[stem] += 1
        for stem, n in stem_count.items():
            if n < max(2, int(0.7 * len(toklists))):
                continue             # not a stable rendering anchor
            forms = defaultdict(int)
            for toks in toklists:
                for t in toks:
                    t = t.split("\u2014")[0]          # cut em-dash run-ons
                    if not (t == stem or t.startswith(stem + "-")):
                        continue
                    # normalize inflection so plurals/possessives/adverbs do
                    # not read as drift: the class that shipped is a
                    # COMPOUND varying after the hyphen (almond-tinted vs
                    # almond-coloured vs almond-white)
                    t = re.sub(r"('s|s'|s)$", "", t)
                    forms[t] += 1
            hyphenated = {f for f in forms if "-" in f}
            if len(hyphenated) > 1 and len(forms) > 1 and \
                    max(forms.values()) < sum(forms.values()):
                key = (stem, frozenset(forms))
                if key in reported:
                    continue
                reported.add(key)
                flagged += 1
                print("  DRIFT CANDIDATE %r x%d — anchor %r varies: %s"
                      % (g, len(occ), stem,
                         ", ".join("%s x%d" % kv for kv in
                                   sorted(forms.items(), key=lambda kv: -kv[1]))))
    print("  epithet drift: %d candidate(s) for a human read" % flagged)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--terms", help="file of watched zh phrases, one per line")
    ap.add_argument("--variants", help="check_structure-style config with a "
                                       "variants map (wrong forms only)")
    a = ap.parse_args()
    watched = set()
    if a.terms:
        watched = {l.strip() for l in open(a.terms, encoding="utf-8")
                   if l.strip() and not l.startswith("#")}

    units = {}
    for f in sorted(os.listdir(os.path.join(ROOT, "out"))):
        m = re.match(r"(.+)_reading\.md$", f)
        if not m:
            continue
        zh = os.path.join(ROOT, "data", "zh", m.group(1) + ".txt")
        if os.path.exists(zh):
            units[m.group(1)] = (zh, os.path.join(ROOT, "out", f))
    readings = [os.path.join(ROOT, "out", f)
                for f in sorted(os.listdir(os.path.join(ROOT, "out")))
                if f.endswith("_reading.md")]
    if not readings:
        print("no reading files; nothing to reconcile")
        return 0
    alltext = "\n".join(open(p, encoding="utf-8").read() for p in readings)
    # note bodies count as usage: many glossary rows exist FOR the notes
    npath = os.path.join(ROOT, "notes.json")
    if os.path.exists(npath):
        alltext += "\n" + json.dumps(json.load(open(npath, encoding="utf-8")),
                                      ensure_ascii=False)

    print("reconciliation over %d unit(s), %d with zh pairing"
          % (len(readings), len(units)))
    if units:
        epithet_drift(units, watched)
    else:
        print("  epithet drift: SKIPPED (no data/zh; regenerate it first — "
              "a skipped check is not a passed check)")

    bad = 0
    gpath = os.path.join(ROOT, "glossary.json")
    if os.path.exists(gpath):
        gloss = json.load(open(gpath, encoding="utf-8"))
        rows = []

        def walk(d):
            for k, v in d.items():
                if k.startswith("_"):
                    continue
                if isinstance(v, dict) and "en" in v:
                    rows.append((k, v))
                elif isinstance(v, dict):
                    walk(v)
        walk(gloss)
        unused = [(zh, r["en"]) for zh, r in rows
                  if r.get("en") and len(r["en"]) > 3
                  and r["en"] not in alltext]
        for zh, en in unused:
            print("  UNUSED glossary form %r (%s) — prose never uses the "
                  "decided rendering" % (en, zh))
        print("  glossary forward: %d/%d decided forms present in the text"
              % (len(rows) - len(unused), len(rows)))
    if a.variants:
        cfg = json.load(open(a.variants, encoding="utf-8"))
        for canon, wrongs in cfg.get("variants", {}).items():
            for w in wrongs:
                n = len(re.findall(r"\b%s\b" % re.escape(w), alltext))
                if n:
                    bad += 1
                    print("  WRONG FORM %r x%d (should be %r)" % (w, n, canon))

    # Curated pairs only: a bare -our/-ise suffix count reads "four",
    # "hour", "rise" and "promise" as locale markers and cries wolf.
    PAIRS = [("colour", "color"), ("honour", "honor"), ("favour", "favor"),
             ("labour", "labor"), ("neighbour", "neighbor"),
             ("armour", "armor"), ("harbour", "harbor"),
             ("odour", "odor"), ("vigour", "vigor"), ("grey", "gray"),
             ("realise", "realize"), ("recognise", "recognize"),
             ("apologise", "apologize"), ("organise", "organize"),
             ("theatre", "theater"), ("centre", "center"),
             ("travelled", "traveled"), ("marvellous", "marvelous"),
             ("defence", "defense"), ("offence", "offense")]
    low = alltext.lower()
    gb = us = 0
    mixed_pairs = []
    for b, a2 in PAIRS:
        nb = len(re.findall(r"\b%s\w*" % b, low))
        na = len(re.findall(r"\b%s\w*" % a2, low))
        gb += nb
        us += na
        if nb and na:
            mixed_pairs.append("%s x%d vs %s x%d" % (b, nb, a2, na))
    print("  spelling locale: %d British, %d American (curated pairs)"
          % (gb, us))
    for mp in mixed_pairs:
        print("    MIXED PAIR: %s" % mp)
    if mixed_pairs or (gb and us and min(gb, us) > 2):
        print("  MIXED SPELLING LOCALE — pick one and cascade "
              "(two finished books shipped mixed)")

    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
