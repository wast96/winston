#!/usr/bin/env python3
"""Assemble figures.json from the per-unit spec files the extractors wrote.

Each extractor writes data/figs/_specs_<unit>.json (a list of figure objects)
and, for the gallery, data/figs/_specs_plates.json. This merges them into
figures.json, keeping only the keys the builder reads (file, before, alt,
caption for chapters; file, alt, caption for _plates), and VALIDATES:
  - every crop file exists in data/figs/
  - every chapter 'before' anchor is a substring of the first 80 chars of
    exactly ONE body-paragraph line in out/<unit>_reading.md (0 = would fail
    the build; >1 = would place at the wrong, earlier paragraph)
Prints a report; writes figures.json only when --write is given and there are
no hard errors (missing file / zero-match anchor).
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIGS = os.path.join(ROOT, "data", "figs")
OUT = os.path.join(ROOT, "out")

CHAP_KEYS = ("file", "before", "alt", "caption")
PLATE_KEYS = ("file", "alt", "caption")


def body_lines(unit):
    md = os.path.join(OUT, "%s_reading.md" % unit)
    lines = []
    for raw in open(md, encoding="utf-8"):
        line = raw.strip()
        if not line or line.startswith("#") or line == "***":
            continue
        m = re.match(r"^\{([vdgp])\} ", line)
        if m:
            line = line[4:]
        lines.append(line)
    return lines


def main():
    write = "--write" in sys.argv
    errors, warnings = [], []
    figures = {"_note": "Per-unit figure specs consumed by build_reading_epub.py. "
               "file -> data/figs/<file>; before -> verbatim substring within the "
               "first 80 chars of the reading-md paragraph the figure precedes; "
               "alt -> screen-reader text; caption -> translator caption (labels "
               "are the source's). _plates is the front-matter portrait gallery."}

    units = sorted(os.path.basename(p)[len("_specs_"):-len(".json")]
                   for p in glob.glob(os.path.join(FIGS, "_specs_*.json")))
    total = 0
    for unit in units:
        specs = json.load(open(os.path.join(FIGS, "_specs_%s.json" % unit)))
        is_plates = (unit == "plates")
        key = "_plates" if is_plates else unit
        rows = []
        lines = None if is_plates else body_lines(unit)
        for s in specs:
            f = s.get("file", "")
            if not os.path.exists(os.path.join(FIGS, f)):
                errors.append("%s: missing crop file %s" % (unit, f))
            if not is_plates:
                anchor = s.get("before", "")
                hits = [ln for ln in lines if anchor and anchor in ln[:80]]
                distinct = len(set(hits))
                if not anchor or distinct == 0:
                    errors.append("%s: anchor NOT found: %r (file %s)"
                                  % (unit, anchor[:50], f))
                elif distinct > 1:
                    warnings.append("%s: anchor matches %d lines (places at "
                                    "first): %r (file %s)"
                                    % (unit, distinct, anchor[:50], f))
                rows.append({k: s.get(k, "") for k in CHAP_KEYS})
            else:
                rows.append({k: s.get(k, "") for k in PLATE_KEYS})
        figures[key] = rows
        total += len(rows)
        print("%-8s %3d figures" % (unit, len(rows)))

    print("--- total %d figures across %d units ---" % (total, len(units)))
    for w in warnings:
        print("WARN", w)
    for e in errors:
        print("ERR ", e)
    if write and not errors:
        json.dump(figures, open(os.path.join(ROOT, "figures.json"), "w"),
                  ensure_ascii=False, indent=1)
        print("WROTE figures.json")
    elif write:
        print("NOT WRITTEN: fix %d hard error(s) first" % len(errors))


if __name__ == "__main__":
    main()
