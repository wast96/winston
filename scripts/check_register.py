#!/usr/bin/env python3
"""Measure register drift between chapters against a reference chapter.

WHY THIS EXISTS. Over a long translation the voice slides, gradually and
invisibly. On a fifteen-chapter book the dialogue went from 16.2 contractions
per thousand words in the approved reference chapter to 0.37 by chapter six —
two contractions in 136 places where English wants one. Nobody reading a
single chapter would notice. The whole book read as two different translators,
and the later one was stilted, which was the exact failure the first draft had
already been rejected for.

You cannot see this by reading. You can see it instantly by counting.

Run this after EVERY chapter against your reference chapter. It costs nothing
and it is the only way to catch drift while it is still cheap to fix.

The two strongest signals, in order:
  1. contractions inside dialogue   (formality; the big one)
  2. "shall" as a share of shall+will inside dialogue

Punctuation rates (em-dash, semicolon, colon) are weaker signals: they vary
legitimately with how much parenthetical material the source has. Treat a
punctuation gap as a question, not a defect.

Narration-side columns (contraction share of contractable negations,
reveal-bangs per 1k narration words, antique-word count) were added after two
whole-book register passes found the real fight was narration starch, which
the dialogue metrics cannot see. They are informational, never failures: the
narration dial is calibrated per book at the voice gate (genre layer +
STYLE.local), and scripts/register_tics.py carries the full greppable battery.
Chapters under ~1,200 speech words are flagged noisy here and skipped for the
dialogue failure test (the reference doc's ~400-word floor is where the metric
stops meaning anything at all; between the two, look before acting).

Usage:
    check_register.py --ref reference/ch1.md out/ch*.md
"""
import argparse
import re
import statistics as st
import sys

CONTRACTION = r"\b\w+(?:n't|'ll|'re|'ve|'m)\b"
SPEECH = re.compile(r'[“"]([^”"]{4,900})[”"]')


def load(path):
    return ' '.join(l.strip() for l in open(path)
                    if l.strip() and not l.startswith('#'))


def words(t):
    return re.findall(r"[A-Za-z][A-Za-z'\-]*", t)


def measure(path):
    t = load(path)
    speech = ' '.join(SPEECH.findall(t))
    narration = SPEECH.sub(' ', t)
    nw = len(words(narration)) or 1
    sw = len(words(speech)) or 1
    aw = len(words(t)) or 1
    shall = len(re.findall(r'\bshall\b', speech, re.I))
    will = len(re.findall(r'\bwill\b', speech, re.I))
    # Narration-side formality: the shelf's later drift fights (two full
    # register passes) were narration-side, not dialogue-side, so measure
    # narration too. Contraction share of contractable negations, the
    # reveal-bang rate, and the antique-word count are all INFORMATIONAL:
    # report, never fail — the calibrated dial lives in the style contract
    # (genre layer + STYLE.local), and quoted documents legitimately skew a
    # documentary chapter. scripts/register_tics.py carries the full battery.
    n_contr = len(re.findall(CONTRACTION, narration))
    n_neg = len(re.findall(
        r"\b(?:did|do|does|could|would|should|had|has|have|is|was|were|are|"
        r"will|can) not\b|\bcannot\b", narration, re.I))
    antique = len(re.findall(
        r"\b(?:thereupon|whereupon|at length|presently|ere long|"
        r"of a morning|of an evening|was wont to|had no wish to|"
        r"made bold to|and no mistake|still less could|forthwith)\b",
        narration, re.I))
    sents = [s for s in re.split(r'(?<=[.!?])["”]?\s+', t) if len(s.split()) > 1]
    return {
        'speech_words': sw,
        'contr_per_1k': 1000.0 * len(re.findall(CONTRACTION, speech)) / sw,
        'shall_share': 100.0 * shall / max(1, shall + will),
        'narr_contr_share': 100.0 * n_contr / max(1, n_contr + n_neg),
        'narr_bang_per_1k': 1000.0 * narration.count('!') / nw,
        'antique_words': antique,
        'emdash_per_1k': 1000.0 * t.count('—') / aw,
        'semicolon_per_1k': 1000.0 * t.count(';') / aw,
        'sent_median': st.median([len(s.split()) for s in sents]) if sents else 0,
        # Rhythm: coefficient of variation of sentence length. Translationese
        # that "drones" comes out with every sentence the same size and shape
        # (defect class G in the revision taxonomy), which no other metric
        # sees. Healthy narrative prose usually sits around 0.55-0.75; a
        # collapse toward uniformity reads as monotone even when every word
        # is right. INFORMATIONAL only: report, never fail — a legitimately
        # staccato action chapter can run low.
        'sent_cv': (st.pstdev(L := [len(s.split()) for s in sents]) /
                    (st.mean(L) or 1)) if len(sents) > 10 else 0,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ref', required=True,
                    help='the approved reference chapter: the voice to match')
    ap.add_argument('--contr-tol', type=float, default=0.45,
                    help='fail if dialogue contraction rate falls below this '
                         'fraction of the reference (default 0.45)')
    ap.add_argument('files', nargs='+')
    a = ap.parse_args()

    ref = measure(a.ref)
    print("reference: %s" % a.ref)
    print("   dialogue contractions %.1f/1k   shall-share %.0f%%   "
          "em-dash %.1f/1k   rhythm CV %.2f"
          % (ref['contr_per_1k'], ref['shall_share'],
             ref['emdash_per_1k'], ref['sent_cv']))
    print("   narration: contraction share %.0f%%   bangs %.1f/1k   "
          "antique words %d   (informational)\n"
          % (ref['narr_contr_share'], ref['narr_bang_per_1k'],
             ref['antique_words']))

    hdr = ('file', 'contr/1k', 'vs ref', 'shall%', 'em-dash/1k', 'sent med',
           'rhythm', 'nar-c%', 'bang/1k', 'antq')
    print('%-26s %9s %8s %7s %11s %9s %7s %7s %8s %5s' % hdr)
    print('-' * 108)

    failures, warnings = [], []
    for f in a.files:
        m = measure(f)
        ratio = m['contr_per_1k'] / ref['contr_per_1k'] if ref['contr_per_1k'] else 1
        flag = ''
        if m['speech_words'] < 1200:
            flag = ' (little dialogue — noisy)'
        elif ratio < a.contr_tol:
            flag = '  <-- STILTED'
            failures.append((f, m, ratio))
        elif m['shall_share'] > max(10.0, ref['shall_share'] + 10):
            # A warning, not a failure. Some chapters are legitimately formal
            # because a speaker's stiffness is deliberate. Look, then judge.
            flag = '  <-- check "shall" (may be deliberate)'
            warnings.append(f)
        if (m['sent_cv'] and ref['sent_cv'] and not flag
                and m['sent_cv'] < 0.7 * ref['sent_cv']):
            flag = '  <-- rhythm flattening (read it aloud; informational)'
        print('%-26s %9.1f %7.2fx %6.0f%% %11.1f %9.0f %7.2f %6.0f%% %8.1f %5d%s'
              % (f.split('/')[-1], m['contr_per_1k'], ratio, m['shall_share'],
                 m['emdash_per_1k'], m['sent_median'], m['sent_cv'],
                 m['narr_contr_share'], m['narr_bang_per_1k'],
                 m['antique_words'], flag))

    print("\nnarration columns are informational (the dial is calibrated per "
          "book at the voice gate);\nrun scripts/register_tics.py for the "
          "full greppable battery with line numbers.")
    if warnings:
        print("\nNOTE: elevated \"shall\" in %s — verify it is a deliberately"
              " formal speaker before changing anything." % ', '.join(
                  w.split('/')[-1] for w in warnings))
    if failures:
        print("\nREGISTER DRIFT in %d file(s). The dialogue has gone formal "
              "relative to the reference." % len(failures))
        print("Fix by contracting inside speech — but NOT blanket: leave")
        print("  - speakers whose stiffness is deliberate (foreign officials,")
        print("    ceremonial registers the source itself marks as formal)")
        print("  - quoted documents: telegrams, newspaper copy, declarations")
        print("  - classical tags, proverbs and set-piece oaths")
        print("  - a character naming himself in the third person")
        return 1
    print("\nregister within tolerance of the reference")
    return 0


if __name__ == '__main__':
    sys.exit(main())
