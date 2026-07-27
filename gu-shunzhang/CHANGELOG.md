# CHANGELOG

Dated entries summarising what each corrections batch cascaded where, and any
project-structural changes.

## 2026-07-27 — Project set up

- Created the `gu-shunzhang` project (branch `claude/gu-shunzhang`) for Gu
  Shunzhang's 特務工作之理論與實際 (1933), styled on the Wang Yaqiao / Juntong /
  Shanghai-underworld projects but with a batch workflow and an eight-check QC
  contract.
- Committed `source.pdf` (National Central Library scan, 298 pp) to the branch.
- Generated `book.json` (8 chapters, 37 sections) from the PDF's embedded
  bookmarks; enriched it with English titles from the translated TOC
  (`reference/toc_translated.md`) and flagged two structural discrepancies.
- Seeded `glossary.json`; wrote CLAUDE.md, README, PROGRESS, HANDOFF,
  CORRECTIONS. No book text translated yet.

## 2026-07-27 — Batch B01: Chapter 1 (緒論, Introduction) translated and built

- Translated Chapter 1 (printed folios 1-16 / PDF 27-42; 3 sections, 60
  paragraphs) end to end: `out/ch01_reading.md` (deliverable),
  `out/ch01_bilingual.md` (QC-only source-above-English draft).
- OCR: tesseract `chi_tra_vert` via the measured crop, cross-read against a
  direct eye-read of all 16 rendered pages (PaddleOCR unavailable; weights host
  off the allowlist). All names/numbers/uncertain spans crop-verified.
- Ran all eight QC checks; recorded in PROGRESS.md. `check_numbers.py`: 0
  unaccounted numbers over 60 pairs. `check_structure.py`: parity 60/60,
  anchors 25/25, heading shape consistent, glossary drift 0.
- Added 25 footnotes to `notes.json` (`ch01`). Extended `glossary.json` with
  pinyin + attestation for the recurring referents (KMT, Three Principles,
  National Revolution, Central Special Branch, GPU, and others).
- Engineering: rewrote `scripts/build_reading_epub.py` to be book.json-driven
  with a full 8-chapter/37-section pending-aware TOC and continuous footnote
  numbering; added `scripts/split_bilingual.py`; extended `check_numbers.py`
  for Traditional 萬/億, fractions, "million", and numeral-idioms.
- Built `out/gushunzhang.epub` (ch1 linked, ch2-8 pending); `qa_epub.py`
  PASS. HANDOFF.md rewritten to launch Batch B02 (Chapter 2).
