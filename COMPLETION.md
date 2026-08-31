# COMPLETION.md — The Tragedy of the Chinese Revolution (annotated edition)

Written on the final batch (B09) instead of another handoff. This is the
document to read to know what the finished edition contains and how far to
trust it.

## Status at a glance

- **22 of 22 units prepared** (front matter + ch01–20). The book is COMPLETE.
- **1,308 footnotes**: 1,009 author notes (Isaacs's own numbered endnotes and
  asterisk footnotes, folded into one arabic stream and placed at the point
  they mark) + 299 editorial notes (the new reader-facing roman stream).
- **Glossary: 144 rows** — 88 people, 20 organizations, 21 places, 15 terms —
  plus a 7-name Principal Characters page (Sun Yat-sen, Chiang Kai-shek, Chen
  Tu-hsiu, Borodin, Wang Ching-wei, Chow En-lai, Chiu Chiu-pei).
- **Linked back-matter Index**: 501 main entries + 447 sub-entries, every folio
  reference a live hyperlink, every "see"/"see also" linked to its target.
- **Figures: none** (a text-only born-digital source; no plates).
- **qa_epub: PASS** — 37 files, 30 documents, 1,308 refs = bodies = backlinks,
  348 page-list = 348 markers, all links resolve, 0.6 MB (well under the 30 MB
  cap). **epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings** (EPUB 3.3).
- **Deliverable:** `out/The Tragedy of the Chinese Revolution.epub`, committed
  to the branch with `git add -f` in the completion commit.

## What the finished edition contains

- **Front matter:** cover (generated typographic), title page (marked
  COMPLETE), Principal Characters page, full hyperlinked contents.
- **Body:** Isaacs's 1938 text, reproduced verbatim (faithful reset, mechanical
  fixes only), ch01–20 plus the Foreword and Trotsky's Introduction.
- **Set-off conventions used:** block quotations (`{q}`, Isaacs quotes
  documents, speeches, and resolutions at length) and scene breaks; no figures,
  verse, or datelines occur.
- **Two note layers by numeral system** (commissioner decision): author notes
  arabic, editorial notes roman, both restarting per chapter, rendered as
  popup footnotes.
- **Back matter:** the editor's note, the glossary, and the linked Index.
  `back_matter.json` is left INERT on purpose — the 1938 first edition carries
  no errata table or colophon to reproduce, so none was invented.

## Per-chapter tally

| Unit | Title | Author | Editorial | Total |
|---|---|---|---|---|
| ch00a | Foreword, by Arnold R. Isaacs | 1 | 16 | 17 |
| ch00b | Introduction, by Leon Trotsky | 0 | 30 | 30 |
| ch01 | Seeds of Revolt | 32 | 53 | 85 |
| ch02 | Problems of the Chinese Revolution | 29 | 20 | 49 |
| ch03 | The New Awakening | 59 | 31 | 90 |
| ch04 | Canton: To Whom the Power? | 32 | 16 | 48 |
| ch05 | Canton: The Coup of March 20, 1926 | 63 | 7 | 70 |
| ch06 | From Canton to the Yangtze | 44 | 10 | 54 |
| ch07 | The Shanghai Insurrection | 21 | 8 | 29 |
| ch08 | The Prodigal's Return | 47 | 7 | 54 |
| ch09 | The Conspiracy of Silence | 58 | 3 | 61 |
| ch10 | The Coup of April 12, 1927 | 42 | 6 | 48 |
| ch11 | Wuhan: "The Revolutionary Center" | 29 | 6 | 35 |
| ch12 | The "Revolutionary Center" at Work | 63 | 11 | 74 |
| ch13 | The Struggle for the Land | 71 | 6 | 77 |
| ch14 | Moscow and Wuhan | 49 | 5 | 54 |
| ch15 | The Wuhan Debacle | 63 | 7 | 70 |
| ch16 | Autumn Harvest | 49 | 8 | 57 |
| ch17 | The Canton Commune | 62 | 4 | 66 |
| ch18 | Fruits of Defeat | 54 | 17 | 71 |
| ch19 | The Rise and Fall of "Soviet China" | 91 | 10 | 101 |
| ch20 | The New "National United Front" | 50 | 18 | 68 |
| | **Total** | **1,009** | **299** | **1,308** |

The editorial count is highest in the early chapters, where the whole cast and
apparatus of the revolution are introduced, and tapers as recurring figures
receive their note at first appearance — exactly the generous-first, taper-later
shape the reader model predicts.

## Batching as executed

- Survey: book.json filled, builder adapted for an annotated edition, skeleton
  EPUB, source.pdf committed.
- B01 ch01; B02 front matter (ch00a, ch00b); B03 ch02–03; B04 ch04–05; B05
  ch06–08; B06 ch09–11; B07 ch12–14; B08 ch15–17; **B09 ch18–20 + whole-book
  close-out** (linked index, reconciliation sweep, term ledger, deep audit,
  authority feed-back, final EPUB committed). No deviation from the approved
  batch plan.

## Checks run book-wide, and what they found

- **Reading-text fidelity** (`check_fidelity.py`): all 22 units match the source
  letters-and-digits exactly.
- **Apparatus** (`check_apparatus.py`): 0 failures — every note anchor a verbatim
  substring, numeric character references only, no mangled glyphs.
- **Build gates** (`qa_epub.py` + epubcheck): green, as above.
- **Two-stream note numbering:** verified in the built XHTML (arabic author /
  roman editorial, restarting per chapter).
- **Whole-book reconciliation** (`check_reconcile.py`, read by hand):
  - 141 of 144 decided glossary forms are used verbatim in the text. The three
    "unused" flags are not gaps: "Merchants' Volunteers" appears five times (the
    check compares a `&#8217;` entity against the body's literal apostrophe);
    "Three People's Principles" and "T'ang" are ledger rows Isaacs's text renders
    in variant forms — legitimate, harmless entries.
  - **Spelling locale is deliberately mixed** and must stay so: Isaacs's body is
    British 1938 spelling (labour, defence, centre), the editorial apparatus is
    American (labor, defense, center), and the Communist documents Isaacs quotes
    carry their translators' American spelling. The sweep's "MIXED LOCALE" flag
    is the expected signature of this two-register design, not a defect. The one
    "labour" inside an editorial note is the proper noun "Labour government."
  - Cross-unit bridges confirmed: "Hsu Chien" (ch12) is bridged to "George
    Hsu-chien" (ch11 note, Xu Qian); Wuhan is glossed as the Wuchang–Hankow–
    Hanyang tri-city (ch07/ch12 notes); the last emperor is bridged "Hsuan Tung"
    (ch01) → "Henry Pu Yi" (ch20 note + glossary).
  - Epithet-drift and other translation-only checks are N/A to a faithful-reset
    English edition (no zh source to pair).

## Observed error rate

Random-sample deep audit (`deep_audit.py`, `out/deep_audit.md`): fixed seed
20260831, **49 of 1,229 reading paragraphs (4.0%)**, spread across 18 units,
scored by letter-level ordered-subsequence coverage against the source.
**Every sampled paragraph scored 1.0000 — zero errors.** Zero errors in 49
samples is consistent with a true paragraph-level error rate below about 6% at
95% one-sided confidence; the binding statement, though, is that `check_fidelity`
verifies the *entire* text (not a sample) at exact letters-and-digits, so the
residual mechanical risk is only in what a character tally cannot see (paragraph
boundaries, hyphens, stray glyphs), each hand-checked every batch. The editorial
notes' dates and identifications were re-checked against standard scholarship;
no discrepancy found.

## Findings that need the commissioner's eye

- **The book is a partisan work** (Trotskyist, with a Trotsky introduction). The
  editorial notes mark where its factual claims are corroborated and where the
  standpoint shapes them, without arguing the politics; a reader should still
  read the narrative as an interested account.
- Nothing else a machine check could not settle remains open. The register of
  the editorial notes was calibrated at the Batch 1 voice gate and held to the
  frozen reference through the blind-critique loop of every batch, including
  B09's two-round loop on ch18.

## Residual uncertainties a reader should know about

- Isaacs's own errors and 1938 usage are reproduced verbatim and flagged, never
  silently corrected: misprints, internal inconsistencies, and British spelling
  stay; period place-names (Canton, Peking/Peiping, Kiangsi, Jehol) are kept and
  bridged to modern forms in the notes and glossary.
- Source quirks kept visible this batch (logged, not "fixed"): ch20's opening
  curly quote where a closing belongs, just before reference mark 37 (cf. ch11,
  ch17); ch18's asterisk footnote closing on a stray single quote
  ("...government.'"). Earlier quirks are listed in PROGRESS.md.
- Six printed folios (159, 211, 226, 245, 293, 332) begin mid-paragraph, so they
  carry no pagebreak anchor of their own; the linked index resolves a reference
  to any of them to the nearest earlier anchor in the same chapter. Endnote
  references in the index (e.g. "340n4") point into Isaacs's back-matter notes,
  which this edition renders inline, so they are shown as plain text.

## Reliability map

Not written as a separate table: Isaacs's book is a documented, heavily-sourced
polemic rather than a work making novel factual claims to be individually
adjudicated. Where a specific claim is checkable, the editorial note attached to
it carries the verdict inline (corroborated / uncorroborated / contradicted).

## Provenance and method

- **Source:** Harold R. Isaacs, *The Tragedy of the Chinese Revolution*,
  Haymarket Books, Chicago, 2009 — a reprint of the Secker & Warburg (London,
  1938) first edition. ISBN 9781608461097.
- **Not a translation.** The PDF has a clean born-digital text layer; there was
  no OCR. Extraction is a faithful reset (`extract_isaacs.py`): de-hyphenation,
  drop-cap fold, furniture strip, superscript-mark removal, asterisk-footnote
  capture, block-quote capture, pagemap emission — each verified by
  `check_fidelity.py`.
- **Builder features that must not be reverted** are listed in HANDOFF.md's
  do-not-revert section; this batch added the linked-index renderer
  (`render_index` in `build_reading_epub.py`, driven by `data/index.json` from
  `parse_index.py`) and its CSS.
- **Rebuild from a clean checkout** (English wordlists required — `setup.sh`
  installs Chinese OCR packs the extractor never uses, so also
  `sudo apt-get install -y wamerican wbritish`):
  `python3 scripts/build_reading_epub.py` →
  `python3 scripts/qa_epub.py` →
  `java -jar /tmp/epubcheck-5.1.0/epubcheck.jar "out/The Tragedy of the Chinese Revolution.epub"`.

## Style ledger harvest (feeds the between-books promotion pass)

STYLE.local.md carries no `#promote` rules — every rule is tagged `#book`. This
edition is a special case on the shelf (an annotated English edition, not a
translation: British body + American apparatus, Wade-Giles-in-text with pinyin
in the notes), so its voice-gate rulings are edition-specific and were kept on
the book, not promoted to the shared translation layers. The one general
observation worth a sibling's attention, recorded here rather than promoted: the
weighed-claim-only verdict tag will look like an "orphan" in any chapter with a
single checkable claim — that is expected, not a reason to scatter the tag.

## Definition of done — met

- [x] EPUB: front matter + all 22 units, full clean TOC, generated cover,
      footnotes at reader-model density, glossary + editor's note + linked
      Index, `qa_epub` PASS across the whole spine, epubcheck clean, no back
      matter (the book has none), and the file itself committed (`git add -f`).
- [x] `out/<id>_reading.md` per unit; `out/term_ledger.md`; `out/deep_audit.md`.
- [x] `notes.json`, `glossary.json`, `figures.json` (empty by design),
      `book.json`, `data/index.json` current; `authority.json` fed this book's
      144 renderings (64 new-to-shelf entries, 80 slugs appended).
- [x] `COMPLETION.md` written from the template with the sampled error rate.
- [x] `PROGRESS.md` and `HANDOFF.md` current; HANDOFF rewritten to COMPLETE;
      `CHANGELOG.md` updated. Further work on this book is a corrections pass.
