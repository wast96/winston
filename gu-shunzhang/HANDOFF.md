# HANDOFF — 特務工作之理論與實際 (Gu Shunzhang)

This file is the baton. A fresh instance with no memory of prior sessions
should be able to read it and start the next batch immediately. Rewrite it at
the end of every batch.

## Current state (project setup, no translation yet)

- Branch: `claude/gu-shunzhang`. Scaffold complete; `source.pdf` committed.
- Read `CLAUDE.md` in full first (source facts, the eight checks, register,
  build and footnote policy), then `PROGRESS.md`, then `book.json`.

## What has been translated

- Nothing. This is the setup commit.

## The eight checks

- Not yet run (no text). Contract in CLAUDE.md.

## Glossary

- Seeded in `glossary.json`. Entries marked `provisional` need attestation
  before they are final. Do not romanise any new name without adding a row.

## Next batch to do

Suggested first batch: **front matter 自序 (author's preface, PDF 7-8), then
Chapter 1 — Introduction (ch01, PDF 27-42, printed 1-16), its three sections.**
Confirm the exact scope with Winston if he has not named one.

Before translating any text, do the three setup engineering tasks in
`PROGRESS.md` -> "Open engineering":
1. Re-measure `scripts/ocr_crop.py` for this book's vertical layout + furniture.
2. Wire PaddleOCR as primary in `ocr_dual.py`; note if it installs.
3. Generalise `build_reading_epub.py` for the full-book pending-aware TOC.

Then run the per-batch pipeline in CLAUDE.md, run all eight checks, write the
footnotes, rebuild the EPUB, run `qa_epub.py`, update `PROGRESS.md` and this
file, and commit.

## Open traps / environment

- Traditional OCR model only (`chi_tra` / `chi_tra_vert`), never `chi_sim`.
- NCL seal over central columns; offset drift (use `book.json` anchors).
- OpenMP/tesseract `OMP_THREAD_LIMIT=1` and orphaned children (see
  `scripts/ocr_crop.py`).
- Environment tools (tesseract, PaddleOCR) are NOT yet installed in this
  container; install per CLAUDE.md "Environment" at the start of the batch.
