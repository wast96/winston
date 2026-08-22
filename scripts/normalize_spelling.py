#!/usr/bin/env python3
"""Whole-book spelling-locale reconciliation (B36, the completion batch).

check_reconcile.py flagged a MIXED spelling locale: 736 American vs 38 British
tokens across 11 curated pairs, plus a few British-only strays (metre, practise).
The book is overwhelmingly American; the decided whole-book policy is a SINGLE
American locale. This cascades the British forms to American across the reading
prose, the note bodies, and the glossary bodies.

Proper-noun safety was verified first: there is no "Labour Party", no surname
"Grey", no proper "Centre"/"Honour"; every British token is a generic word or a
Shanghai theatre building-name. The theatre building-names are already SPLIT in
the source translation ("Cathay/Grand/Lyceum Theatre" vs "Kwang Hua/Jixiang/Towa
Theater"), so unifying on "Theater" removes real drift rather than overriding a
consistent proper-noun convention.

Each pattern is chosen so it touches ONLY the intended word family:
  colour/honour/favour/labour/neighbour  -- the "our"->"or" families (substring
      safe: these letter-runs occur in no unrelated English word)
  centre/theatre/defence/marvellous      -- substring safe (note "central" holds
      "centr" not "centre"; "theatrical" holds "theatr" not "theatre")
  grey     -- word-bounded, to spare American "greyhound" (none present anyway)
  organis  -- only before e/a, to spare "organism"
  metre    -- substring safe (also fixes kilometre/centimetre; "metric" is metr-)
  practis  -- substring safe (practise/practised/practising)
Case of each occurrence's first letter is preserved.
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (compiled pattern, american-stem). The pattern matches the British stem; the
# replacement swaps in the American stem and lets any inflectional suffix ride.
RULES = [
    (re.compile(r"colour", re.I), "color"),
    (re.compile(r"honour", re.I), "honor"),
    (re.compile(r"favour", re.I), "favor"),
    (re.compile(r"labour", re.I), "labor"),
    (re.compile(r"neighbour", re.I), "neighbor"),
    (re.compile(r"centre", re.I), "center"),
    (re.compile(r"theatre", re.I), "theater"),
    (re.compile(r"defence", re.I), "defense"),
    (re.compile(r"marvellous", re.I), "marvelous"),
    (re.compile(r"\bgrey", re.I), "gray"),
    (re.compile(r"organis(?=[ea])", re.I), "organiz"),
    (re.compile(r"metre", re.I), "meter"),
    (re.compile(r"practis", re.I), "practic"),
]


def case_like(model, repl):
    """Give repl the capitalization pattern of model's leading run."""
    if model[:1].isupper():
        return repl[:1].upper() + repl[1:]
    return repl


def convert(text):
    counts = {}
    for pat, amer in RULES:
        def sub(m):
            counts[amer] = counts.get(amer, 0) + 1
            return case_like(m.group(0), amer)
        text = pat.sub(sub, text)
    return text, counts


def process_file(path):
    src = open(path, encoding="utf-8").read()
    out, counts = convert(src)
    changed = out != src
    return src, out, counts, changed


def targets():
    import glob
    files = sorted(glob.glob(os.path.join(ROOT, "out", "ch*_reading.md")))
    files += [os.path.join(ROOT, "notes.json"),
              os.path.join(ROOT, "glossary.json")]
    return files


def main(apply):
    total = {}
    touched = []
    for path in targets():
        src, out, counts, changed = process_file(path)
        if changed:
            touched.append((os.path.relpath(path, ROOT), counts))
            for k, v in counts.items():
                total[k] = total.get(k, 0) + v
            if apply:
                open(path, "w", encoding="utf-8").write(out)
    for rel, counts in touched:
        print("  %-26s %s" % (rel, ", ".join("%s+%d" % (k, v)
                                             for k, v in sorted(counts.items()))))
    print("%s: %d files, replacements: %s"
          % ("APPLIED" if apply else "DRY-RUN", len(touched),
             ", ".join("%s=%d" % (k, v) for k, v in sorted(total.items()))))


if __name__ == "__main__":
    import sys
    main(apply="--apply" in sys.argv)
