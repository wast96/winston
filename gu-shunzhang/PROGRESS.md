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
- Two structural flags carried in `book.json` -> `toc_flags`, to resolve at
  translation time against the scan:
  - **ch02 s06**: bookmark hanzi is 待遇 (treatment / remuneration / pay); the
    translated TOC rendered it "Rewards and Punishments" (=賞罰). Provisional
    title set to the literal "Remuneration / Treatment" pending a clean read.
  - **ch05 s04**: 一般的祕密 ("General Secrets") is in the bookmarks but was
    omitted from the translated TOC. Title provisional.
  - Several sub-items were OCR-carried in that TOC and are flagged there for a
    clean read (ch1 s3 items 2-4; ch3 s1 principles 2 and 5; ch4 s2 title;
    a few ch6 sub-items).

## Open engineering (before the first translation batch)

1. **Re-measure the OCR crop.** `scripts/ocr_crop.py` is inherited from the
   Juntong book (horizontal, no running head). This book is vertical with an
   outer-margin running head, a running foot and a folio. Measure ink bounds on
   ~12 pages of THIS book and rewrite the crop to exclude all three furniture
   zones; add vertical handling (tesseract `--psm 5`, `chi_tra_vert`).
2. **Wire PaddleOCR as the primary engine** in `ocr_dual.py` (check 1), with
   `chi_tra_vert` tesseract as the diff partner. Record whether Paddle installed.
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
