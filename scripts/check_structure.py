#!/usr/bin/env python3
"""Structural integrity checks that cost nothing and catch silent losses.

Every check here exists because something was silently lost on a real project
and nobody noticed for weeks.

  1. PARAGRAPH PARITY. Source paragraph count must equal translation paragraph
     count. A dropped or merged paragraph is invisible in prose and obvious
     here. Cheapest structural check there is.

  2. NOTE ANCHORS RESOLVE. Every footnote anchor must appear verbatim in the
     prose exactly where you think it does. On a real book twelve notes were
     written and silently dropped because their anchors had drifted out of
     sync — usually just capitalisation, "a gentleman's word" against a
     sentence starting "A gentleman's word". The build stayed green because
     references and bodies still agreed WITH EACH OTHER: twelve of each,
     both absent. Agreement between two derived artifacts is not integrity.

  3. HEADING CONVENTION. Every chapter file must open with the same heading
     levels. One chapter used a single '#' where the others used two, the
     builder treated it as the book title and skipped it, and that chapter
     shipped with no title at all.

     Only the OPENING headings are compared (default: first two). Deeper
     structure legitimately varies — a prologue has no numbered sections while
     chapters do — and comparing the whole shape flags that as a defect.

  4. GLOSSARY DRIFT. One rendering per referent across the whole book.

Usage:
    check_structure.py --config book.json
    check_structure.py --pairs data/zh/ch03.txt out/ch03.md

Config keys:
    docs      {chapter_id: path}      required
    sources   {chapter_id: path}      enables the parity check
    notes     path to notes.json      enables the anchor check
    datelines {chapter_id: anchor}    anchors the BUILDER injects rather than
                                      ones present in the prose. Whitelisted,
                                      but reported, so the list cannot quietly
                                      grow into a way of hiding real orphans.
    variants  {canonical: [wrong…]}   enables the drift check. Put ONLY wrong
                                      forms in each value list, NEVER the
                                      canonical form, or every correct
                                      occurrence is flagged as drift.
    parity_exceptions {chapter_id: {"delta": int, "why": str}}
                                      a DECLARED departure from one-to-one
                                      rendering; printed on every run.
    heading_depth  int                how many opening headings must agree
                                      (CLI --heading-depth wins if given).
"""
import argparse
import json
import os
import re
import sys


def body_lines(path, skip_heads=True):
    """Non-blank lines that count as paragraphs. Scene-break markers ('***'
    alone on a line) are layout, not text, and are skipped; the set-off
    prefixes {v}/{d}/{g}/{p} (vignette, dateline, hour-gloss, verse) are
    stripped so the line text compares clean."""
    out = []
    for l in open(path):
        s = l.strip()
        if not s or s == '***':
            continue
        if skip_heads and s.startswith('#'):
            continue
        out.append(re.sub(r'^\{[vdgpj]\} ', '', s))
    return out


def check_parity(src_path, tgt_path, src_head_prefix='###', exception=None):
    """exception: {"delta": int, "why": str} for a DELIBERATE departure from
    one-to-one rendering.

    There is exactly one legitimate reason for the counts to differ, and it
    must be declared in the config, printed on every run, and carry a written
    reason -- otherwise the exception list becomes a way of silencing the very
    check that catches dropped paragraphs. A mismatch of any size other than
    the declared delta still fails.
    """
    all_src = body_lines(src_path, skip_heads=False)
    src = [l for l in all_src if not l.startswith(src_head_prefix)]
    # Drop the chapter title ONLY if it was not already removed as a heading.
    # assemble.py marks titles with '### ', so the filter above takes them
    # out; dropping a further line on top of that deleted a real paragraph
    # and biased every parity result by one -- in the direction that hides a
    # genuinely dropped paragraph, which is the defect this check exists for.
    if len(src) == len(all_src) and src:
        src = src[1:]
    tgt = body_lines(tgt_path)
    delta = (exception or {}).get('delta', 0)
    ok = len(src) + delta == len(tgt)
    note = ''
    if delta:
        note = '  [declared %+d: %s]' % (delta, (exception or {}).get('why', ''))
    print("  parity %-22s source %3d | translation %3d  %s%s"
          % (os.path.basename(tgt_path), len(src), len(tgt),
             "OK" if ok else "MISMATCH", note))
    return ok


def check_anchors(notes_path, docs, datelines=None, show_multi=False):
    """Only ZERO matches is a failure.

    An earlier version of this also failed anchors matching more than once, on
    the theory that the note might attach to the wrong occurrence. That was
    wrong, and it is worth recording why: recurring-character notes are
    deliberately anchored to a bare name and deliberately attach at its FIRST
    appearance. On a real book that rule made the check emit twenty-odd
    "ambiguous" lines per run — "Du Yuesheng (134 occurrences)" — all correct
    behaviour. A check whose output is mostly noise is a check nobody reads,
    and the one real failure hides in the scroll. Multiplicity is reported
    only on request, and never fails.
    """
    notes = json.load(open(notes_path))
    datelines = datelines or {}
    bad, waived, multi, total = [], [], [], 0
    for cid, path in docs.items():
        prose = open(path).read()
        for e in notes.get(cid, []):
            total += 1
            n = prose.count(e['anchor'])
            if n == 0:
                (waived if e['anchor'] == datelines.get(cid) else bad).append(
                    (cid, e['anchor']))
            elif n > 1:
                multi.append((cid, e['anchor'], n))
    print("  anchors: %d notes, %d unresolved, %d waived (%d attach at first "
          "of several occurrences, expected)"
          % (total, len(bad), len(waived), len(multi)))
    for cid, a in bad:
        print("     UNRESOLVED %-9s %s" % (cid, a[:76]))
    for cid, a in waived:
        print("     waived (builder-injected dateline) %-9s %s" % (cid, a[:50]))
    if show_multi:
        for cid, a, n in multi:
            print("     multi %-9s %-58s %d" % (cid, a[:58], n))
    return not bad


def check_headings(docs, depth=2):
    # Compared POSITION BY POSITION, not as whole tuples. Comparing the
    # tuple (title level, first section level) can never pass on a book
    # where some chapters have sections and some do not: a sectionless
    # chapter's shape is (2,) and a sectioned one's is (2, 3), which is
    # exactly the legitimate variation the docstring promises not to flag.
    # That comparison went INCONSISTENT the moment ch04 (no sections)
    # joined ch01-03 (sections) and would have stayed red for the whole
    # rest of the book. What the check exists to catch is a heading at the
    # WRONG LEVEL -- a '#' title where the others use '##' -- so each
    # position is required to agree only across the documents that have a
    # heading at that position at all.
    by_pos = {}
    shapes = {}
    for cid, path in docs.items():
        heads = [l.strip() for l in open(path) if l.strip().startswith('#')][:depth]
        shape = tuple(len(h) - len(h.lstrip('#')) for h in heads)
        shapes.setdefault(shape, []).append(cid)
        for i, lvl in enumerate(shape):
            by_pos.setdefault(i, {}).setdefault(lvl, []).append(cid)
    ok = all(len(lvls) == 1 for lvls in by_pos.values())
    print("  headings: %d level position(s) %s"
          % (len(by_pos), "OK" if ok else "INCONSISTENT"))
    if not ok:
        for i, lvls in sorted(by_pos.items()):
            if len(lvls) > 1:
                for lvl, cids in sorted(lvls.items()):
                    print("     position %d level %d: %s"
                          % (i, lvl, ', '.join(cids)))
    return ok


def check_drift(docs, variants):
    """variants: {canonical: [wrong forms]}"""
    bad = 0
    for cid, path in docs.items():
        t = open(path).read()
        for canon, wrongs in variants.items():
            for w in wrongs:
                if re.search(r'\b%s\b' % re.escape(w), t):
                    print("     DRIFT in %-9s %r should be %r" % (cid, w, canon))
                    bad += 1
    print("  glossary drift: %d" % bad)
    return bad == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', help='JSON: {docs:{id:path}, notes:…, '
                                     'sources:{id:path}, variants:{…}}')
    ap.add_argument('--pairs', nargs=2, metavar=('SRC', 'TGT'))
    ap.add_argument('--show-multi', action='store_true',
                    help='list anchors matching more than once (informational)')
    ap.add_argument('--heading-depth', type=int, default=None,
                    help='how many opening headings must match across files '
                         '(default 2; deeper structure varies legitimately)')
    a = ap.parse_args()

    if a.pairs:
        return 0 if check_parity(*a.pairs) else 1

    cfg = json.load(open(a.config))
    docs = cfg['docs']
    ok = True
    print("structural checks")
    if cfg.get('sources'):
        for cid, sp in cfg['sources'].items():
            if cid in docs:
                ok &= check_parity(sp, docs[cid],
                                   exception=cfg.get('parity_exceptions',
                                                     {}).get(cid))
    if cfg.get('notes'):
        ok &= check_anchors(cfg['notes'], docs, cfg.get('datelines'),
                            a.show_multi)
    # The config may set its own heading_depth (book.json documents why);
    # it was silently ignored until ch06, which is how the shape check ran
    # red from ch04 on without stopping the line. CLI flag wins if given.
    depth = (a.heading_depth if a.heading_depth is not None
             else cfg.get('heading_depth', 2))
    ok &= check_headings(docs, depth)
    if cfg.get('variants'):
        ok &= check_drift(docs, cfg['variants'])
    print("\n%s" % ("ALL STRUCTURAL CHECKS PASS" if ok else "STRUCTURAL FAILURES"))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
