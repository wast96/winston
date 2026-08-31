# Deep audit — The Tragedy of the Chinese Revolution (annotated edition)

Random-sample deep audit (CLAUDE.md check 10), run on completion of the book.
Because this is an annotated **English** edition, not a translation, the audit
splits into two questions: is the reading text a faithful reset of Isaacs's
1938 source, and are the added notes accurate?

## 1. Reading-text fidelity (the machine layer)

The whole-book gate `scripts/check_fidelity.py` compares the letters-and-digits
of every reading unit against the born-digital source text; it passes for all
22 units (ch18 32,548 / ch19 53,394 / ch20 58,463 characters matched this
batch, and every earlier unit before it). That is a 100% whole-unit character
match across the book.

The deep audit zooms from the whole unit to the paragraph and asks a stronger
question of a random sample: does **every** letter and digit of the paragraph
appear, in order, in that chapter's source text? A dropped, altered, or
reordered word would drop the ordered-subsequence coverage below 1.0; furniture
(running heads, folios, footnotes) and de-hyphenation only add source
characters or remove hyphens, so a faithful paragraph reaches 1.0.

    scripts/deep_audit.py --seed 20260831 --rate 0.04
    seed=20260831  sampled 49 of 1229 paragraphs (4.0%)
    letter-coverage: min=1.0000  mean=1.0000  below 0.995: 0

- **Sample:** 49 paragraphs (4.0%), fixed seed 20260831, spread across 18 of
  the 22 units.
- **Result:** every sampled paragraph scored 1.0000 letter-coverage — zero
  errors.
- **Honest bound:** zero errors in 49 independent samples is consistent with a
  true paragraph-level error rate below about 6% at 95% one-sided confidence.
  That sampling bound is the weaker statement here; the binding one is that
  `check_fidelity` verifies the *entire* text, not a sample, at exact
  letters-and-digits — so the residual mechanical-extraction risk is not the
  sampling bound but the small set of things a character tally cannot see
  (paragraph boundaries, hyphens, stray glyphs), each of which is hand-checked
  every batch and logged in PROGRESS.

## 2. Notes accuracy (the human layer)

The notes are where an error would hide, so the dates, identifications, and
verdict tags added this project were checked against standard scholarship
(Wikipedia, Baidu Baike, academic works; never an AI-written reference). A
paranoid re-check of the final batch's editorial notes confirmed, among others:
the Long March (October 1934 – October 1935), the Marco Polo Bridge clash (July
7, 1937), the Sian Incident (the mutiny of December 12, 1936; Chiang released on
Christmas Day), the Fukien rebellion (November 1933 – January 1934), the US
Silver Purchase Act (June 1934), the Tangku Truce (May 31, 1933), the Seventh
Comintern Congress (July–August 1935), and the life-dates of Chu Teh
(1886–1976), Peng Teh-huai (1898–1974), Wang Ming (1904–1974), von Seeckt
(1866–1936), H. H. Kung (1881–1967), Wellington Koo (1888–1985), and Pu Yi
(1906–1967). No discrepancy was found. The book-wide reconciliation
(`check_reconcile.py`) was read by hand; its findings are recorded in
COMPLETION.md.

## Residual uncertainties a reader should know

- The reading text reproduces Isaacs's own errors and 1938 usage verbatim
  (misprints, internal inconsistencies, British spelling); these are marked in
  the notes or listed in PROGRESS, never silently corrected.
- The editorial notes state a fact-check verdict only where a claim is actually
  weighed; a plain identification carries none. Where scholarship and Isaacs's
  partisan account diverge, the note says so and the text stays as printed.
