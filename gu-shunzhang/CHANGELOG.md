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

## 2026-07-28 — Batch B07: Chapter 6 §4-6 (Weapons / Sabotage / Conversation)

- Translated ch06 **§4 (武器, Weapons)** and **§6 (談話術, The Art of
  Conversation)** and appended them to `out/ch06_reading.md`; the chapter now
  carries §1-6 as six ordered `### Section` headings, all deep-linked in the EPUB.
- **§5 (破壞術, Sabotage) withheld in full as dangerous how-to content**
  (explosive-device construction). Its PDF pages (151-168, folios 119-136) were
  never rendered, read or translated; an editorial placeholder holds its section
  slot so numbering stays intact. The explosive/munition tail of §4 (folio 118 and
  the gas-gun cartridge internals on folio 117) was likewise omitted, with an
  editorial footnote marking the omission.
- `notes.json` `ch06` +14 footnotes (109-122); book total **122**.
- `glossary.json` +9 rows (Shanghai Garrison Command, Kwong Sang Hong; handgun,
  Mauser pistol, gas-gun, art of conversation, revolver, malacca baton [prov.],
  political prisoner).
- `book.json`: `toc_flags_open` — §4 Weapons’ two intro items resolved against
  the body.
- `scripts/check_numbers.py`: narrowed NOISE `十[几分步]`→`十[几分]` (it was
  eating the 十 out of 三十步 / 二十步); added idioms 千鈞一髮, 三緘其口, 模棱兩可.
- Checks: check_numbers CLEAN (137 pairs); parity OK (137/137); qa_epub PASS
  (22 files, 12 docs, 122 refs/bodies/backlinks). Dual-engine OCR substituted by
  whole-batch eye-read (Paddle unavailable). No figures in range.
- Fixed a build-breaker: HTML named entities (`&nbsp;`, `&times;`) in note bodies
  are undefined in XHTML; use numeric refs (`&#160;`, `&#215;`).

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
