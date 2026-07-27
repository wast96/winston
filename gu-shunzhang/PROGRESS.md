# PROGRESS — 特務工作之理論與實際 (Gu Shunzhang)

Read this first. Written as work happens, not at the end.

## Status: project set up. No text translated yet.

Branch `claude/gu-shunzhang`. Scaffold in place; `source.pdf` committed. The
next session translates the first batch (suggested: front matter 自序, then
Chapter 1) after the OCR crop is re-measured for this book (see Open engineering).

## Source facts established at setup

- 298-page image-only PDF, National Central Library (Taiwan) copy
  (NCL-9900010638). No text layer. 49 embedded bookmarks give the full
  chapter/section map; `book.json` is generated from them.
- **Vertical, right-to-left, Traditional characters.** Running head (book
  title) down the outer margin; chapter title as running foot; folio at the
  bottom outer corner. A round NCL library seal is stamped across the centre
  of the text block on many pages.
- Chapter 1 opens at PDF 27 = printed 1 (verified by eye against folio 一).
  **Page offset drifts** (26 at ch1 to ~54 by ch8) because unpaginated plates
  accumulate. Use the per-section anchors in `book.json`, not a formula.
- 8 chapters, 37 numbered sections. Front matter: title page PDF 3, author's
  preface 自序 PDF 7 (dated Nanjing 20 July 1933), TOC 目錄 PDF 9.

## TOC and title notes

- A translated table of contents (from an earlier chat) is saved at
  `reference/toc_translated.md` and merged into `book.json` as English titles.
- The flagged TOC discrepancies have been **resolved against the scan** (see
  `book.json` -> `toc_flags_resolved` and the corrections block appended to
  `reference/toc_translated.md`):
  - **ch02 s06** = 待遇 "Treatment and Remuneration" (p62/printed 30); the
    translated TOC's "Rewards and Punishments" was wrong.
  - **ch05 s04** = 一般的祕密 "Ordinary Secrets" (p110/printed 78); it exists,
    the translated TOC omitted it.
  - **ch04 s02** = 觀念鬥爭 "The Struggle over Mindset" (interpretive gloss in
    the TOC was "Building the Right Mindset").
  - **ch01 s03 Scope** (body p38-41): 1 reconnaissance, 2 counter-surveillance,
    3 intelligence, 4 communications, 5 sabotage, 6 protection. The TOC
    mislabeled 2-4 and invented a "Sanction/liquidation" not in the book.
  - **ch03 s01 Principles** (body p72-75): 1 proactiveness, 2 secrecy, 3
    agility, 4 precision, 5 universality, 6 practicality. TOC item 2 should be
    "Secrecy" and item 5 "Universality".
  - Still open (`toc_flags_open`): the deepest ch6 sub-bullets (Weapons intro
    item 2, Observation item 5, Hypnotism item 7) to confirm during the ch6
    batch; the plausible TOC values stand provisionally.
- The last few body pages (PDF 293-294) may be a short postscript; confirm when
  translating ch8. Colophon at PDF 295 (中華民國二十二年八月付印, i.e. Aug 1933).

## Open engineering (before the first translation batch)

1. **[DONE] Re-measured the OCR crop.** `scripts/ocr_crop.py` now carries this
   book's geometry (measured off 16 pages, recto+verso): crop left 0.045, right
   0.84, top 0.11, bottom 0.915; OCR `chi_tra_vert --psm 5`; textual filters for
   the right-margin running head and the bottom-margin running foot (chapter
   title). Verified by OCR that the running head no longer bleeds in as a
   spurious column. Trap noted in the script: a few pages (PDF 45, 50, 200, 260
   among samples) have heavy dark-edge scan artifacts no crop removes.
2. **Wire PaddleOCR as the primary engine** in `ocr_dual.py` (check 1), with
   `chi_tra_vert` tesseract as the diff partner. Record whether Paddle installed.
   (Not done yet; tesseract path is working.)
3. **Generalise `build_reading_epub.py`** to emit the full-book TOC (all 8
   chapters / 37 sections from `book.json`) with translated units linked and the
   rest pending, one XHTML per unit, cumulative EPUB `out/theory-practice.epub`.

## The eight checks — state

None run yet (no translation). The contract is in CLAUDE.md; record per batch
here: which checks ran, what they surfaced, the check-8 sampled error rate.

## Glossary

Seeded in `glossary.json`: title, author (Gu Shunzhang, attested), and the
recurring tradecraft terms (mostly `provisional` pending attestation). The
Central Special Branch (中央特科), GPU and Green/Red Gang renderings need
attestation before they are treated as final; cross-check the sibling
Shanghai-underworld glossary for the gang names.

## Flagged for Winston's read-through

- Nothing yet. This section fills as translation proceeds: uncertain readings,
  contradictions with scholarship, choices I was unsure of.
