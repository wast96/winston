#!/usr/bin/env python3
"""Verify that source and translation paragraphs line up BY CONTENT.

Paragraph parity compares two counts. Two counts can agree while the texts
have slipped past one another -- a join in one place and a split in another
cancel out, and the counts stay equal while every pair after the first is a
different paragraph beside a different translation. The numeric check then
compares unrelated paragraphs and reports its findings with complete
confidence, which is worse than not running it.

So alignment is checked on its own, from a signal that survives translation:
the ratio of English characters to Han characters. It is remarkably steady for
a given translator and register -- on this book it sits near 4.6 -- and a slip
shows up as a run of pairs where the ratio collapses or explodes, because a
long source paragraph has been set beside a short translation or the reverse.

Reports the first offending run rather than every consequence of it, since one
slip makes everything after it look wrong.

Usage: check_align.py UNIT [--tol 2.2]
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def paras(path, head_prefix):
    return [l.strip() for l in open(path)
            if l.strip() and not l.strip().startswith(head_prefix)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("unit")
    ap.add_argument("--tol", type=float, default=2.2,
                    help="how far a pair's ratio may stray from the unit's "
                         "median, as a multiplicative factor, before it counts "
                         "as a slip")
    a = ap.parse_args()

    src = paras(os.path.join(ROOT, "data", "zh", "%s.txt" % a.unit), "###")
    tgt = paras(os.path.join(ROOT, "out", "%s_reading.md" % a.unit), "#")

    n = min(len(src), len(tgt))
    ratios = []
    for i in range(n):
        zh = len(re.findall(r"[一-鿿]", src[i]))
        en = len(tgt[i])
        ratios.append(en / float(zh) if zh else 0.0)

    good = sorted(r for r in ratios if r > 0)
    med = good[len(good) // 2] if good else 0.0

    bad = [i for i, r in enumerate(ratios)
           if r and (r > med * a.tol or r < med / a.tol)]

    print("%s: %d source, %d translation, median ratio %.2f en/han"
          % (a.unit, len(src), len(tgt), med))
    if len(src) != len(tgt):
        print("  COUNTS DIFFER by %d" % (len(tgt) - len(src)))
    if not bad:
        print("  alignment OK: no pair strays more than %.1fx from the median"
              % a.tol)
        return 0

    print("  %d pair(s) out of line; first is pair %d" % (len(bad), bad[0] + 1))
    for i in bad[:6]:
        print("   pair %-4d ratio %.2f" % (i + 1, ratios[i]))
        print("      zh: %s" % src[i][:52])
        print("      en: %s" % tgt[i][:72])
    return 1


if __name__ == "__main__":
    sys.exit(main())
