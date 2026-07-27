# HANDOFF — 特務工作之理論與實際 (Gu Shunzhang)

This file is the baton. A fresh instance with no memory of prior sessions
should read it and start immediately. Rewrite it at the end of every batch.

## >>> YOUR JOB THIS SESSION: Batch B01 = Chapter 1 (Introduction) <<<

Translate **Chapter 1, 緒論 (Introduction)** end to end: OCR, translation, the
eight checks, footnotes, EPUB, commit. This is the FIRST batch, so you also do
the one remaining piece of setup engineering (the EPUB builder) along the way.

- **Scope:** ch01, its 3 sections. **PDF pages 27-42** = **printed pages 1-16**.
  - §1 The Nature of Secret-Service Work — PDF 27-32
  - §2 The Importance of Secret-Service Work — PDF 33-37
  - §3 The Scope of Secret-Service Work — PDF 38-42
- Chapter 1 is also the **style-and-quality bar** for the whole book; get its
  register and note density right, because every later batch is measured on it.

## Read these first, in order

1. `CLAUDE.md` — in full. Source facts, the eight checks (the QC contract),
   footnote policy, register, build and handoff rules. Non-negotiable.
2. `book.json` — the structure map. Note `batches` (the 11-batch plan Winston
   set), `citation_convention`, `toc_flags_resolved`, `back_matter`.
3. `PROGRESS.md` — current state and what is already done.

## What is already done (do NOT redo)

- Project scaffold, `source.pdf` committed, glossary seeded.
- **OCR crop is re-measured and working.** `scripts/ocr_crop.py` has this
  book's geometry (vertical, Traditional; crop L0.045 R0.84 T0.11 B0.915;
  `chi_tra_vert --psm 5`; running-head and running-foot filters). Just run it.
- **TOC discrepancies resolved** against the scan; corrected English section
  titles are in `book.json`, and a corrections block is in
  `reference/toc_translated.md`. Trust those titles.

## Citation convention (this edition will be cited in research)

Cite the book's **printed folio**, never the PDF page. The PDF-to-printed
offset drifts (plates are bound in), so **read the folio off each scanned
page**; do not compute it. Main text is printed pp 1-236, then the 勘誤表
(errata) and colophon. See `book.json` -> `citation_convention` / `back_matter`.

## The pipeline for this batch (per CLAUDE.md)

1. Environment: `apt install tesseract-ocr tesseract-ocr-chi-tra
   tesseract-ocr-chi-tra-vert`; `pip install pymupdf pillow numpy`. Try
   `pip install paddlepaddle paddleocr` for check 1's primary engine; if it will
   not install in a few minutes, fall back to `chi_tra_vert` alone and say so.
2. `python scripts/render.py 27 42 --dpi 300`.
3. `python scripts/ocr_crop.py 27 42` (tesseract path). If Paddle installed,
   wire it as primary in `ocr_dual.py` and run the dual-engine char diff.
4. Translate ch1 to the register in CLAUDE.md. Verify BEFORE writing: every
   name, number, low-confidence span, and every char the two OCR engines
   disagree on gets a magnified crop read by eye. Never invent bridging text.
5. Run the **eight checks** (CLAUDE.md). At minimum for this batch: dual-engine
   OCR diff (check 1), invariant/number check (4), the term-ledger update (5),
   inline low-confidence annotation (6), external-scholarship check (7), and a
   3-5% deep audit (8). Do blind double translation (2) and back-translation (3)
   on the argumentative passages. Record what ran and what it found in
   `PROGRESS.md` and this handoff.
6. Footnotes into `notes.json` (keyed `{unit_id: [{anchor, note}]}`, anchors
   verbatim substrings of the English). Every check-6 bracketed span becomes a
   footnote. Glossary rows into `glossary.json` with status + attestation.
7. **Generalise `scripts/build_reading_epub.py`** (still ch1-shaped from the
   sibling project) to: one XHTML per unit, one cumulative EPUB
   `out/theory-practice.epub`, a **full TOC of all 8 chapters / 37 sections**
   from `book.json` with ch1 linked and the rest shown as pending. Continuous
   footnote numbering. Builder must REFUSE to build on any unmatched footnote
   anchor. Then run `scripts/qa_epub.py` and fix until it passes.
8. Also produce `out/ch01_reading.md` (the clean English, Winston's correction
   surface).
9. Commit (message: "B01 ch1: ..."). Then **rewrite this HANDOFF for Batch B02
   = Chapter 2 (PDF 43-71, printed 17-39)**, recording ch1's open questions,
   new glossary entries, and the check results.

## The 11-batch plan (from Winston)

B01 ch1 · B02 ch2 · B03 ch3 · B04 ch4 · B05 ch5 · B06 ch6 §1-3 ·
B07 ch6 §4-6 · B08 ch6 §7-11 · B09 ch7 §1-3 · B10 ch7 §4 · B11 ch8.
Full page ranges in `book.json` -> `batches`.

## Open traps / environment

- Traditional OCR model only (`chi_tra` / `chi_tra_vert`), never `chi_sim`.
- NCL seal over central columns; a few pages have heavy dark-edge artifacts
  (crop-verify by eye). Offset drift: use `book.json` anchors, read folios off
  the page.
- `OMP_THREAD_LIMIT=1` for tesseract; orphaned children spin after a kill
  (see `scripts/ocr_crop.py`).
- Env tools are NOT installed in a fresh container; install them first.
