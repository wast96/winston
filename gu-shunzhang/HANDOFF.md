# HANDOFF — 特務工作之理論與實際 (Gu Shunzhang)

This file is the baton. A fresh instance with no memory of prior sessions
should read it and start immediately. Rewrite it at the end of every batch, and
always keep the paste-ready message below as its first section.

## Message to paste into the next chat

```
Read gu-shunzhang/CLAUDE.md in full (note the standing rules at the top), then gu-shunzhang/HANDOFF.md, then gu-shunzhang/book.json. Work only on the claude/gu-shunzhang branch; if the session starts you elsewhere, move your work onto claude/gu-shunzhang and drop the stray branch. Then do Batch B05 = Chapter 5 (秘密, Secrecy) — PDF pages 90-114, printed folios 58-82, its 4 sections (ch05s01 to ch05s04) — end to end: install the environment (tesseract-ocr chi_tra + chi_tra_vert, pymupdf, pillow, numpy; AND opencv-python-headless this time, because Chapter 5 is about the secret apparatus and secret communications and is likely to carry plates), render, OCR with the already-measured crop (scripts/ocr_crop.py, chi_tra_vert --psm 5), then read every one of the 25 pages off the 300 dpi scan by eye and translate to the register in CLAUDE.md. Run all eight QC checks (author one aligned out/ch05_bilingual.md and generate out/ch05_reading.md + data/zh/ch05.txt with scripts/split_bilingual.py, then check_numbers.py and check_structure.py; blind double-translation and back-translation on the argumentative passages, and since this is a long batch do a full completeness recount of every list against the pages — parity can be green while a whole run of items is dropped from BOTH files). Note that book.json's toc_flags_resolved fixes ch05s04 = 一般的祕密 "Ordinary Secrets" (secrecy in everyday life; first sub-item 日常生活) — it exists in the bookmarks though the translated TOC omitted it; confirm against the section opener at PDF 110. Detect and caption figures with find_figures.py 90 114 (it merges its manifest; needs opencv); captions in this book may be vertical text beside the plate, crop that zone and OCR with chi_tra_vert; add specs to figures.json under ch05 and never invent an identification. Add footnotes to notes.json keyed "ch05" (continuous numbering follows automatically, picking up from 62) and extend glossary.json with attestation. Rebuild out/gushunzhang.epub (the builder is book.json-driven and pending-aware; ch5 links automatically once out/ch05_reading.md exists), run scripts/qa_epub.py until it passes, then commit to claude/gu-shunzhang and present out/gushunzhang.epub to me directly as an attached file in this chat (not via a git link). Finally rewrite HANDOFF.md to launch Batch B06 (Chapter 6 §1-3). Cite printed folios, never PDF pages; verify the offset at the ch5 opener against folio 五八 (it was pdf−32 at ch4, but plates drift it, so READ the folio); never invent bridging text (crop the scan and read the continuation). Don't pause for my approval; run the whole batch and report back when Chapter 5 is built and QA-green.
```

## What is DONE (do not redo)

- **Batch B01 = Chapter 1 (緒論) is complete, built, QA-green.** `out/ch01_reading.md`,
  `notes.json` (`ch01`, 25 notes), glossary, EPUB all in place.
- **Batch B02 = Chapter 2 (特務組織) is complete, built, QA-green.** `out/ch02_reading.md`,
  `notes.json` (`ch02`, 19 notes, numbering 26-44), 13 glossary entries, 4 figures
  in `figures.json`/`data/figs/`.
- **Batch B03 = Chapter 3 (特務工作的方法) is complete, built, QA-green.** `out/ch03_reading.md`,
  `notes.json` (`ch03`, 9 notes, numbering 45-53), 6 glossary rows, no figures.
- **Batch B04 = Chapter 4 (特務觀念) is complete, built, QA-green.** See `PROGRESS.md`
  for the full batch record. `out/ch04_reading.md`, `notes.json` (`ch04`, 9 notes,
  numbering 54-62), 7 glossary rows (觀念 / 特務觀念 / 觀念鬥爭 / 人生觀 / 中心思想 /
  主義 / 桀紂), no figures (all 6 folios are prose). `out/gushunzhang.epub` now carries
  **4 of 8 chapters, 62 notes, 10 spine files**; `qa_epub.py` PASSES; all structural
  checks pass.
- **The EPUB builder is generalised and book.json-driven.** One XHTML per
  translated chapter, full pending-aware TOC (ch1-4 linked and deep-linked;
  ch5-8 shown pending), continuous footnote numbering, refuses to build on any
  unmatched note anchor. You do NOT need to touch the builder for ch5; adding
  `out/ch05_reading.md` is enough for it to appear.
- **`scripts/split_bilingual.py`** turns one `out/<id>_bilingual.md` into the
  shipped `out/<id>_reading.md` and the parity source `data/zh/<id>.txt`.
  Invocation: `python3 scripts/split_bilingual.py out/ch05_bilingual.md ch05 "第五章 秘密"`.
  Bilingual format: `## H2 <chapter title>` / `## H3 <section title>` heading lines,
  then paragraph pairs of a `> <source>` line immediately followed by one English
  line. (`out/*_bilingual.md` is gitignored — QC only, never shipped.)
- **`scripts/check_numbers.py`** NOISE list already handles 兩個 (measure word),
  the 萬-idioms, and the Arabic list enumerators (`\d+[．.、]`). Keep extending it
  as new false positives appear.
- **OCR crop geometry is correct**; just run `ocr_crop.py`. `OMP_THREAD_LIMIT=1`
  is mandatory; verify `pgrep -c tesseract` is 0 after each run.
- **Page offset is pdf−32 through ch4** (verified PDF 84 = folio 五二; folios 52-57
  each read off the page). book.json says ch5 opener PDF 90 = printed 58 (same
  offset), but READ the folio 五八 at the opener; plates drift it.

## Your job next session: Batch B05 = Chapter 5 (秘密 / Secrecy)

- **Scope:** ch05, its 4 sections. **PDF 90-114 = printed folios 58-82** (25 pages,
  the largest batch so far).
  - §1 祕密的意義 — The Meaning of Secrecy — PDF 90 / folio 58
  - §2 祕密機關 — The Secret Apparatus — PDF 93 / folio 61
  - §3 祕密交通 — Secret Communications — PDF 99 / folio 67
  - §4 一般的祕密 — Ordinary Secrets — PDF 110 / folio 78
- **Section anchors are in `book.json`.** Verify the ch5 opener is folio 五八 by
  eye; the offset from ch4 was pdf−32, but plates drift it, so READ the folio.
- **This chapter probably has plates** (secret apparatus, secret communications).
  Install `opencv-python-headless` and run `find_figures.py 90 114` (it merges its
  manifest). Crop any caption zone and OCR vertical captions with `chi_tra_vert`;
  add specs to `figures.json` under `ch05`. Never invent an identification.
- Recurring subjects already noted in ch1-4 (GPU, C.P., Gu, KMT, Three Principles,
  National Revolution, the Green/Red Gangs, 工部局/捕房, 匪區, 社會化, 官僚化/
  僱傭化, 觀念/觀念鬥爭, the Sunzi tag, 紙上談兵, 緣木求魚, 桀紂) do NOT get
  re-noted unless the new context adds something.

## The 11-batch plan (from Winston)

B01 ch1 [DONE] · B02 ch2 [DONE] · B03 ch3 [DONE] · B04 ch4 [DONE] · B05 ch5 ·
B06 ch6 §1-3 · B07 ch6 §4-6 · B08 ch6 §7-11 · B09 ch7 §1-3 · B10 ch7 §4 ·
B11 ch8. Full page ranges in `book.json` -> `batches`.

## Open traps / environment

- Traditional OCR model only (`chi_tra` / `chi_tra_vert`), never `chi_sim`.
- Env tools are NOT installed in a fresh container; install them first. In this
  environment `apt-get install ... poppler-utils` 404s on poppler and aborts the
  WHOLE transaction — install the tesseract packages WITHOUT poppler-utils
  (`apt-get install -y --no-install-recommends tesseract-ocr tesseract-ocr-chi-tra
  tesseract-ocr-chi-tra-vert`); we render via PyMuPDF and don't need poppler.
  PaddleOCR will not install (weights host off the allowlist); fall back to
  `chi_tra_vert` + eye-read and say so.
- NCL seal over central columns; crop-verify anything under it.
- Offset drift: no constant page formula; read folios off the page.
- `OMP_THREAD_LIMIT=1` for tesseract; orphaned children spin after a kill.
- **Parity is necessary but not sufficient**: it compares two files derived from
  the same bilingual, so a run of items dropped from the bilingual is invisible
  to it. Always recount list items against the scanned pages — doubly important
  for the long ch5 batch.
- Carried-forward open items: 別動隊 rendering provisional (from ch1); the ch7
  GPU spelling (格伯烏) to be reconciled with ch1's 格伯武 when ch7 is done;
  中央特務會議/中央特務總部/各省區特務部 provisional (from the ch2 plate);
  中心思想 rendered "central conviction" is provisional (from ch4).
