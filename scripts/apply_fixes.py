#!/usr/bin/env python3
"""Re-apply crop-verified OCR corrections to an assembled source file.

Crop verification is the most expensive step in this pipeline and its results
were, until this script existed, the most perishable: the corrections lived
only in the translator's head and in the finished English. `data/txt/` and
`data/zh/` are deliberately untracked (they are the book's own text, not
project work), so a fresh checkout re-runs OCR and silently reintroduces every
mangle that was already paid for once -- 张国焘 goes back to being 张国琳.

So every reading confirmed against the scan is recorded in
`data/ocr_fixes.json` with the page it was verified on and why, and replayed
here. The ledger doubles as an audit trail: anyone can see which readings are
the scan's and which are mine.

Corrections also matter to the CHECKS, not just the prose. An OCR mangle that
turns 十八年 into 十和年 leaves a bare 十 that the numeric check reports as a
dropped "10" against a translation that correctly says "eighteen" -- a false
positive that would otherwise be silenced with a noise rule, hiding the real
defect underneath.

Usage: apply_fixes.py UNIT_ID [...]     (or --all)
"""
import argparse
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZH = os.path.join(ROOT, "data", "zh")
TXT = os.path.join(ROOT, "data", "txt")
LEDGER = os.path.join(ROOT, "data", "ocr_fixes.json")
TXT_LEDGER = os.path.join(ROOT, "data", "txt_fixes.json")


def apply_txt(fixes, verbose=True):
    """Apply per-PAGE OCR corrections to data/txt/p####.txt BEFORE assembly.

    Some OCR mangles are not just wrong characters, they change the PARAGRAPH
    STRUCTURE: tesseract reads a fullwidth exclamation ！ as the digit 1, so
    assemble.py's sentence-end gate never fires and two source paragraphs weld
    into one. A fix recorded in the zh ledger cannot undo that -- by the time
    it runs, the merge has already happened. These corrections therefore live
    in data/txt_fixes.json and are replayed here on the per-page text, so a
    fresh checkout re-segments correctly instead of reproducing the merge.

    Ledger form: [{"page": 37, "wrong": "...", "right": "...", "why": "..."}].
    """
    applied, missing = 0, []
    for f in fixes:
        p = os.path.join(TXT, "p%04d.txt" % f["page"])
        if not os.path.exists(p):
            missing.append(f)
            continue
        text = open(p).read()
        n = text.count(f["wrong"])
        if n:
            open(p, "w").write(text.replace(f["wrong"], f["right"]))
            applied += n
        else:
            missing.append(f)
    if verbose:
        print("  txt (pre-assembly): %d fix(es) applied, %d not found"
              % (applied, len(missing)))
        for f in missing:
            print("      not found on p%s: %r" % (f.get("page", "?"), f["wrong"]))
    return applied, len(missing)


def apply_unit(unit, fixes, verbose=True):
    path = os.path.join(ZH, "%s.txt" % unit)
    if not os.path.exists(path):
        print("  %s: no assembled source, skipped" % unit)
        return 0, 0
    text = open(path).read()
    applied, missing = 0, []
    for f in fixes:
        n = text.count(f["wrong"])
        if n:
            text = text.replace(f["wrong"], f["right"])
            applied += n
        else:
            missing.append(f)
    with open(path, "w") as fh:
        fh.write(text)
    if verbose:
        print("  %-16s %2d fix(es) applied, %d already clean or not found"
              % (unit, applied, len(missing)))
        for f in missing:
            print("      not found: %r (verified on PDF p%s)"
                  % (f["wrong"], f.get("page", "?")))
    return applied, len(missing)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("units", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--txt", action="store_true",
                    help="apply data/txt_fixes.json to the per-page OCR text "
                         "BEFORE assembly (paragraph-structure OCR fixes); run "
                         "this, then re-run assemble.py, then apply the zh "
                         "ledger with the normal invocation")
    a = ap.parse_args()

    if a.txt:
        if not os.path.exists(TXT_LEDGER):
            print("no txt ledger at %s" % TXT_LEDGER)
            return 1
        print("pre-assembly OCR corrections (per page)")
        apply_txt(json.load(open(TXT_LEDGER)))
        return 0

    if not os.path.exists(LEDGER):
        print("no ledger at %s" % LEDGER)
        return 1
    ledger = json.load(open(LEDGER))
    units = list(ledger) if a.all else a.units
    if not units:
        print("pass unit ids or --all")
        return 1

    print("crop-verified OCR corrections")
    total = 0
    for u in units:
        got, _ = apply_unit(u, ledger.get(u, []))
        total += got
    print("%d replacement(s) across %d unit(s)" % (total, len(units)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
