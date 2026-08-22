#!/usr/bin/env python3
"""Generate edits/<id>_edits.md date-normalization blocks (day-month -> month-day).

Auto-handles single dates; the three compound/range sites are excluded here and
added by hand. House style (from the book's own 609 month-day dates):
  "DD Month YYYY"  -> "Month DD, YYYY" (+ trailing comma if mid-sentence)
  "DD Month"       -> "Month DD"       (no comma)
Every OLD is made unique by extending left context word by word.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MONTHS = ("January February March April May June July August September "
          "October November December").split()
DATE = re.compile(r'\b(\d{1,2}) (' + '|'.join(MONTHS) + r')( \d{4})?\b')

# (unit, exact matched text) sites that belong to a compound handled by hand.
SKIP = {
    ("ch01", "10 November"),      # "9 and 10 November"
    ("ch02", "28 September 1930"), # "24 to 28 September 1930"
    ("ch11", "30 August"),        # "30 August and 1 August"
    ("ch11", "1 August"),         # "30 August and 1 August"
}


def flip(day, month, year, after_char):
    core = "%s %s" % (month, day)
    if year:
        core += ", " + year.strip()
        # add the post-year comma mid-sentence (house style), unless punctuation
        # or end-of-line already follows.
        if after_char not in (",", ".", ";", ")", "”", '"', "", "\n"):
            core += ","
    return core


def make_unique(text, old, start):
    """Extend old leftward until it occurs exactly once in text."""
    if text.count(old) == 1:
        return old
    # walk back adding characters from the source until unique
    i = start
    while i > 0 and text.count(text[i:start] + old) != 1:
        i -= 1
    cand = text[i:start] + old
    return cand if text.count(cand) == 1 else None


def gen(unit):
    path = os.path.join(ROOT, "out", unit + "_reading.md")
    text = open(path, encoding="utf-8").read()
    blocks = []
    for m in DATE.finditer(text):
        day, month, year = m.group(1), m.group(2), m.group(3)
        matched = m.group(0)
        if (unit, matched) in SKIP:
            continue
        after = text[m.end():m.end() + 1]
        new_core = flip(day, month, year, after)
        old = make_unique(text, matched, m.start())
        if old is None:
            print("  !! could not uniquify %r in %s" % (matched, unit), file=sys.stderr)
            continue
        new = old[:-len(matched)] + new_core if len(old) > len(matched) else new_core
        blocks.append((old, new, matched))
    return blocks


def main(units):
    for unit in units:
        blocks = gen(unit)
        lines = ["# %s date normalization (Tier A, R1) -- day-month -> month-day\n" % unit]
        for old, new, matched in blocks:
            lines.append("### %s [T-date] TOUCH" % unit)
            lines.append("OLD: %s" % old)
            lines.append("NEW: %s" % new)
            lines.append("WHY: date order; house style is month-day (%s)\n" % matched)
        out = os.path.join(ROOT, "edits", unit + "_edits.md")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
        print("%s: %d date edits -> %s" % (unit, len(blocks), out))


if __name__ == "__main__":
    main(sys.argv[1:])
