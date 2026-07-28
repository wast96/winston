# HANDOFF — 特務工作之理論與實際 (Gu Shunzhang)

This file is the baton. A fresh instance with no memory of prior sessions
should read it and start immediately. Rewrite it at the end of every batch, and
always keep the paste-ready message below as its first section.

## Message to paste into the next chat

```
Read gu-shunzhang/CLAUDE.md in full (note the standing rules at the top), then gu-shunzhang/HANDOFF.md, then gu-shunzhang/book.json. Work only on the claude/gu-shunzhang branch; if the session starts you on some other branch, move your work onto claude/gu-shunzhang and drop the stray branch. Then do Batch B07 = Chapter 6 §4-6 (特務技術 continued: 第四節 武器 Weapons, 第五節 破壞術 Sabotage, 第六節 談話術 The Art of Conversation) — PDF pages 139-175, printed folios 107-143, unit ids ch06s04 to ch06s06 — end to end: install the environment (tesseract-ocr chi_tra + chi_tra_vert, pymupdf, pillow, numpy, AND opencv-python-headless — apt WITHOUT poppler-utils, it 404s and aborts the whole apt run; PaddleOCR will not install, so fall back to chi_tra_vert + eye-read and say so), render, OCR with the already-measured crop (scripts/ocr_crop.py, chi_tra_vert --psm 5, OMP_THREAD_LIMIT=1, verify pgrep -c tesseract is 0 after), then read every one of the 37 pages off the 300 dpi scan by eye and translate to the register in CLAUDE.md. NOTE the batch boundary: §3's list ended on folio 107, so §4 武器 opens PARTWAY DOWN folio 107 (PDF 139) at 第四節 — render 139 and start there, do not re-translate the §3 tail. Weapons and Sabotage carry load-bearing numerals (calibres, weights, quantities) and are the likeliest sections in the book to carry plates — crop-verify every unit number and measurement at magnification, and run find_figures.py 139 175 (it merges its manifest, needs opencv); its ink-density detector catches halftone plates but MISSES line diagrams (the ch6 street-tailing figure had to be cropped by hand), so eyeball every page for line art too; caption any vertical caption zone with chi_tra_vert; add specs to figures.json under ch06 and never invent an identification. Confirm book.json's toc_flags_open sub-bullets where they fall in §4 (the two intro items under Weapons: 一、特務人員為什麼要懂得武器 is confirmed present; verify the second) and update book.json if the bookmarks and the body disagree. Author one aligned out/ch06s04-06_bilingual.md, generate the reading text and parity source with scripts/split_bilingual.py, then run scripts/check_numbers.py and scripts/check_structure.py; do blind double-translation and back-translation on the argumentative passages and a full completeness recount of every list against the pages (these sections are list-heavy). IMPORTANT: ch6 is a multi-batch chapter — APPEND §4-6 to the existing out/ch06_reading.md (do not overwrite the §1-3 content); the builder deep-links sections in book.json order by counting the '### ' headings, so ch06_reading.md must end up with §1-6 as six '### Section' headings in order. Add footnotes to notes.json keyed "ch06" (continuous numbering follows automatically, picking up from 109) and extend glossary.json with attestation. Rebuild out/gushunzhang.epub, run scripts/qa_epub.py out/gushunzhang.epub until it passes, then commit to claude/gu-shunzhang and present out/gushunzhang.epub to me directly as an attached file in this chat (not via a git link). Finally rewrite HANDOFF.md to launch Batch B08 (Chapter 6 §7-11). Cite printed folios, never PDF pages; the offset was pdf−32 through folio 107, but plates accumulate through Weapons/Sabotage — READ the folio at each section opener and re-verify. Never invent bridging text (crop the scan and read the continuation). Don't pause for my approval; run the whole batch and report back when the batch is built and QA-green.
```

## What is DONE (do not redo)

- **B01 = Chapter 1 (緒論)** — complete, QA-green. `ch01`, 25 notes.
- **B02 = Chapter 2 (特務組織)** — complete, QA-green. `ch02`, 19 notes (26-44),
  13 glossary rows, 4 figures.
- **B03 = Chapter 3 (特務工作的方法)** — complete, QA-green. `ch03`, 9 notes (45-53).
- **B04 = Chapter 4 (特務觀念)** — complete, QA-green. `ch04`, 9 notes (54-62).
- **B05 = Chapter 5 (秘密)** — complete, QA-green. `ch05`, 23 notes (63-85),
  13 glossary rows, no figures.
- **B06 = Chapter 6 §1-3 (特務技術: 化裝術/釘梢術/反偵探)** — complete, QA-green.
  `out/ch06_reading.md` (92 parity paragraphs), `notes.json` `ch06` **23 notes
  (86-108)**, 9 glossary rows touched, **1 figure** (the street-shadowing
  diagram, `data/figs/ch06_tailing_street.png`, `figures.json: ch06`). Covers
  **PDF 115-138 + folio 107 (PDF 139)** — §3's last list runs onto folio 107
  before §4 begins. See `PROGRESS.md` for the full batch record.
- `out/gushunzhang.epub` now carries **6 of 8 chapters, 108 notes, 12 spine
  files, 1 figure**; `qa_epub.py out/gushunzhang.epub` PASSES; all structural
  checks pass. Chapter 6 shows in the TOC linked, §1-3 deep-linked, §4-11 pending.
- **The EPUB builder now handles a PARTIALLY-translated chapter.** It counts the
  `### ` section headings in each chapter's reading doc and deep-links only those
  sections, showing the rest pending — so ch6 §4-11 appear pending even though
  `ch06.xhtml` exists. B07/B08 just APPEND their sections to `out/ch06_reading.md`
  and rebuild; nothing else in the builder needs touching.
- **`scripts/check_numbers.py` NOISE** now also strips 萬一, 一本萬利, 百貨,
  十字, 第二天 (the first two go at the TOP, before the 一[measure] group).
- **`scripts/split_bilingual.py`** invocation for a multi-batch chapter:
  `python3 scripts/split_bilingual.py out/ch06s04-06_bilingual.md ch06s04-06 "第六章 特務技術"`
  — then MERGE its reading output into `out/ch06_reading.md` after the §3 tail,
  and its `data/zh` output likewise. (For B06 the whole chapter file was written
  at once; for B07 you are appending, so split to a scratch id and concatenate,
  or hand-append the aligned pairs — either way keep §1-6 as six ordered
  `### Section` headings.)

## Your job next session: Batch B07 = Chapter 6 §4-6

- **Scope:** ch06 §4-6, unit ids ch06s04-ch06s06. **PDF 139-175 = printed folios
  107-143** (37 pages).
  - §4 特務應用的武器 — Weapons — PDF 139 / folio 107 (opens PARTWAY DOWN 107,
    after §3's qualifications list finishes at the top of 107)
  - §5 破壞術 — Sabotage / Destruction — PDF 151 / folio 119
  - §6 談話術 — The Art of Conversation — PDF 169 / folio 137
- **Anchors in `book.json`.** Offset was pdf−32 through folio 107; READ the folio
  at each section opener — Weapons/Sabotage are the likeliest to bind in plates
  that drift the offset.
- **Load-bearing numerals:** calibres, weights, charge quantities. Crop-verify
  every unit number and measurement at magnification (ch5 precedent: the whole
  telegraph-cipher page was zoomed and the arithmetic checked).
- **Figures likely.** `find_figures.py 139 175` catches halftone plates but
  MISSED the ch6 line diagram — eyeball every page for line art (weapon
  drawings, sabotage schematics) and crop by hand if needed. Add to
  `figures.json: ch06`; never invent an identification.
- **book.json `toc_flags_open`:** confirm the two intro items under Weapons
  (第四節). Confirmed present so far: item 1 = 特務人員為什麼要懂得武器; verify
  the second intro item against the body and update book.json.

## The 11-batch plan (from Winston)

B01 ch1 [DONE] · B02 ch2 [DONE] · B03 ch3 [DONE] · B04 ch4 [DONE] ·
B05 ch5 [DONE] · **B06 ch6 §1-3 [DONE]** · B07 ch6 §4-6 · B08 ch6 §7-11 ·
B09 ch7 §1-3 · B10 ch7 §4 · B11 ch8. Full page ranges in `book.json` -> `batches`.

## Open traps / environment

- Traditional OCR model only (`chi_tra` / `chi_tra_vert`), never `chi_sim`.
- Env is NOT installed in a fresh container. `apt-get install ... poppler-utils`
  404s and aborts the WHOLE transaction — install tesseract WITHOUT poppler
  (`apt-get install -y --no-install-recommends tesseract-ocr tesseract-ocr-chi-tra
  tesseract-ocr-chi-tra-vert`); render via PyMuPDF. `pip install pymupdf pillow
  numpy opencv-python-headless` install cleanly. PaddleOCR will NOT install;
  fall back to `chi_tra_vert` + eye-read and say so (dual-engine OCR diff, check
  1, cannot run — substitute the whole-batch eye-read, as B05/B06 did).
- NCL seal over central columns; crop-verify anything under it.
- Offset drift: no constant formula; read folios off the page.
- `OMP_THREAD_LIMIT=1` for tesseract; orphaned children spin after a kill
  (verify `pgrep -c tesseract` is 0).
- `find_figures.py` merges its manifest AND only catches halftone plates —
  eyeball for LINE ART, which it misses (the ch6 street-tailing diagram was
  hand-cropped).
- **Parity is necessary but not sufficient** (it compares two files from the
  same bilingual): always recount lists against the scanned pages.
- **ch6 is multi-batch:** APPEND to `out/ch06_reading.md`; never overwrite the
  §1-3 content. Six ordered `### Section` headings must end up in the file so
  the builder's per-section deep-linking stays correct.
- Carried-forward open items (unchanged unless noted):
  別動隊 provisional (ch1); the ch7 GPU spelling 格伯烏 to reconcile with ch1's
  格伯武; 中央特務會議/中央特務總部/各省區特務部 provisional (ch2 plate);
  中心思想 "central conviction" provisional (ch4); 抄靶子 "stop-and-frisk"
  provisional (ch5). NEW from B06: **反偵探 kept as "counter-surveillance"** (not
  "counter-detection") for whole-book consistency; **the 扛木梢 slang** ("carry
  off a wooden dummy") is a provisional reading of a Shanghai expression; the
  **§1 head misnumbering** (source prints 一,二,四,四) renumbered I-IV and footnoted.
- Source misprints recorded so far (all footnoted): 店務員→電務員 (folio 78),
  綠化鈷→氯化鈷 (folio 73). Watch for more.
