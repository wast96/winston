#!/usr/bin/env python3
"""Register tic battery: grep the shelf's known translationese tells.

Mechanizes the kill lists promoted into the styles/ layers (v2.3): antique
function words, the could-only class, pivots, nominalizations, deng-tags,
archaic quote tags, narration ellipses and reveal-bangs, interrogative "in
the end," sentence-initial numerals, date-format and spelling-locale drift,
litotes calques, and >90-word narration sentences for the spine test.

A HIT IS A CANDIDATE, NOT AUTOMATICALLY A DEFECT. Every battery carries its
carve-outs (quoted documents, slogans, formal-by-design speakers, note
anchors, genuinely idiomatic uses); each hit must pass or fail the read-aloud
test. The script is informational by design: it always exits 0 and always
prints what it measured.

Usage:
    register_tics.py ch01 [ch02 ...]     per-unit listing with line numbers
    register_tics.py --profile [units]   counts-only calibration table
                                         (default: every out/*_reading.md)

Arguments may be unit ids (resolved to out/<id>_reading.md) or paths to .md
files. A book can extend or silence batteries without forking the script via
data/register_tics.local.json:
    {"add": [{"name": "...", "pattern": "...", "note": "...",
              "ignorecase": false}],
     "disable": ["battery-name", ...]}

Provenance: generalized from the per-book batteries built on the-sword-roars
(B09) and chinas-secret-war, and the counts measured on zhou-enlai.
"""
import argparse
import json
import re
import sys
from pathlib import Path

MONTHS = ("January|February|March|April|May|June|July|August|September|"
          "October|November|December")

# (name, pattern, ignorecase, note). Order is the report order.
BATTERIES = [
    ("antique-fn-words",
     r"\b(thereupon|whereupon|at length|presently|ere long|of a morning|"
     r"of an evening|was wont to|had no wish to|made bold to|come what may|"
     r"and no mistake|still less could|forthwith|let slip)\b", True,
     "_base kill list; plain modern equivalent or cut"),
    ("trailing-besides",
     r"[a-z,] besides[.,;]", False,
     "the trailing '...and a reward besides' form; 'as well' / 'too' / cut"),
    ("could-only",
     r"\b(could only|could not but|could not help|cannot help|not help but)\b",
     False,
     "plain the archaic ones ('had to', or the verb); idiomatic hits stay"),
    ("pivots",
     r"\b(that is to say|which was to say|in other words|namely)\b", False,
     "the source's restatement pivot; usually a comma appositive or a colon"),
    ("nominalization",
     r"\b[Tt]he [a-z]+(?:ing|ment) of the\b", False,
     "convert ~2/3 to finite verbs; the idiomatic set stays"),
    ("deng-tag",
     r"\b(and the rest|and the others|and so on)\b", False,
     "vary ('among others'), restructure, or cut; not zero; skip note anchors"),
    ("one-after-another",
     r"\bone after (?:another|the other)\b", False,
     "vary: 'in turn', 'one by one', 'in succession', or cut"),
    ("quote-tag-archaism",
     r"\b(in his lifetime|in his later years|in her later years|"
     r"disclosed many years later|recalled in (?:his|her) later years|"
     r"would recall)\b", False,
     "modernize and vary quote tags ('later recalled', or plain 'said')"),
    ("narration-ellipsis",
     r"(?:\.\.\.|…)(?![\"”'’])", False,
     "close with a period in narration; a quotation that truncates is exempt"),
    ("in-the-end-question",
     r"\bin the end\b[^.!?\n]*\?", False,
     "interrogative-intensifier calque; the narrative 'ultimately' use is fine"),
    ("sentence-initial-numeral",
     r"^[0-9]", False,
     "recast, spell out, or reorder"),
    ("day-month-date",
     r"\b\d{1,2} (?:%s)\b" % MONTHS, False,
     "flag against the book's decided date format (shelf default Month D, YYYY)"),
    ("british-spelling",
     r"\b(colour|rumour|licence|honour|labour|neighbour|theatre|centre|"
     r"defence|realise|organise|recognise)\w*\b", True,
     "flag against the decided locale (shelf default American); proper names "
     "of real venues are exempt"),
    ("litotes",
     r"\b(no few|no small|not a little)\b", False,
     "state it positively; quoted matter exempt"),
]

QUOTE_CHARS = "\"“”"


def resolve(arg, out_dir):
    p = Path(arg)
    if p.suffix == ".md" and p.is_file():
        return p
    return Path(out_dir) / ("%s_reading.md" % arg)


def load_local(path):
    """Apply data/register_tics.local.json (add/disable) if present."""
    batteries = list(BATTERIES)
    p = Path(path)
    if not p.is_file():
        return batteries, None
    spec = json.loads(p.read_text(encoding="utf-8"))
    disabled = set(spec.get("disable", []))
    batteries = [b for b in batteries if b[0] not in disabled]
    for extra in spec.get("add", []):
        batteries.append((extra["name"], extra["pattern"],
                          bool(extra.get("ignorecase")), extra.get("note", "")))
    return batteries, p


def narration_lines(lines):
    """(lineno, line) pairs for lines that carry no quoted speech at all.
    Line-level heuristic, good enough for a candidate sweep."""
    return [(n, l) for n, l in lines if not any(c in l for c in QUOTE_CHARS)]


def long_sentences(text, floor=90):
    body = " ".join(l.strip() for l in text.splitlines()
                    if l.strip() and not l.startswith("#"))
    sents = [s for s in re.split(r'(?<=[.!?])["”]?\s+', body)
             if len(s.split()) > 1]
    return [s for s in sents if len(s.split()) > floor]


def run_unit(path, batteries, profile):
    text = path.read_text(encoding="utf-8")
    lines = list(enumerate(text.splitlines(), 1))
    counts = {}
    if not profile:
        print("########## %s ##########" % path)
    for name, pattern, icase, note in batteries:
        rx = re.compile(pattern, re.IGNORECASE if icase else 0)
        hits = [(n, l) for n, l in lines for _ in rx.finditer(l)]
        counts[name] = len(hits)
        if not profile:
            print("=== [%s] (%s) ===" % (name, note))
            for n, l in hits[:60]:
                print("%d: %s" % (n, l.strip()[:110]))
            if len(hits) > 60:
                print("  ... and %d more" % (len(hits) - 60))
    # python-computed batteries
    bangs = [(n, l) for n, l in narration_lines(lines) if "!" in l]
    counts["narration-bang"] = len(bangs)
    longs = long_sentences(text)
    counts["long-sentence>90w"] = len(longs)
    if not profile:
        print("=== [narration-bang] (reveal-bangs outside speech; ration "
              "hard, the fact lands with a period) ===")
        for n, l in bangs[:40]:
            print("%d: %s" % (n, l.strip()[:110]))
        print("=== [long-sentence>90w] (spine test: count finite spines, "
              "find the main verb; colon-lists and documents exempt) ===")
        for s in longs[:20]:
            print("%d words: %s..." % (len(s.split()), s[:110]))
    return counts


def main():
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("units", nargs="*",
                    help="unit ids (out/<id>_reading.md) or .md paths; "
                         "with --profile, defaults to out/*_reading.md")
    ap.add_argument("--profile", action="store_true",
                    help="counts-only calibration table across units")
    ap.add_argument("--out", default="out", help="dir holding *_reading.md")
    ap.add_argument("--local", default="data/register_tics.local.json")
    args = ap.parse_args()

    batteries, local = load_local(args.local)
    if local:
        print("register_tics: local battery config %s applied" % local)

    if args.units:
        paths = [resolve(u, args.out) for u in args.units]
    elif args.profile:
        paths = sorted(Path(args.out).glob("*_reading.md"))
    else:
        ap.error("give unit ids, or --profile for the whole-book table")
    paths = [p for p in paths if p.is_file() or
             print("register_tics: SKIP missing %s" % p)]
    if not paths:
        print("register_tics: nothing to measure")
        return 0

    all_counts = {p: run_unit(p, batteries, args.profile) for p in paths}

    if args.profile:
        names = [b[0] for b in batteries] + ["narration-bang",
                                             "long-sentence>90w"]
        width = max(len(n) for n in names) + 2
        print("\nregister_tics profile (%d units): counts are CANDIDATES, "
              "each hit still faces its carve-outs" % len(paths))
        header = " " * width + " ".join("%8s" % p.name.split("_")[0]
                                        for p in paths) + "     total"
        print(header)
        for name in names:
            row = [all_counts[p].get(name, 0) for p in paths]
            print("%-*s%s %9d" % (width, name,
                                  " ".join("%8d" % c for c in row), sum(row)))
    else:
        print("\nregister_tics: measured %d batteries over %d unit(s); every "
              "hit above is a candidate for the read-aloud test, not a "
              "verdict." % (len(batteries) + 2, len(paths)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
