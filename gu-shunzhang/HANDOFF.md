# HANDOFF — 特務工作之理論與實際 (Gu Shunzhang)

This file is the baton. A fresh instance with no memory of prior sessions
should read it and start immediately. Rewrite it at the end of every batch, and
always keep the paste-ready message below as its first section.

## Message to paste into the next chat

```
Read gu-shunzhang/CLAUDE.md in full (note the standing rules at the top), then gu-shunzhang/HANDOFF.md, then gu-shunzhang/book.json. Work only on the claude/gu-shunzhang branch; if the session starts you elsewhere, move your work onto claude/gu-shunzhang and drop the stray branch. Then do Batch B06 = Chapter 6 §1-3 (特務技術 / Secret-Service Tradecraft, sections 化裝術 Disguise, 釘梢術 Shadowing, 反偵探 Counter-Surveillance) — PDF pages 115-138, printed folios 83-106, its 3 sections (ch06s01 to ch06s03) — end to end: install the environment (tesseract-ocr chi_tra + chi_tra_vert, pymupdf, pillow, numpy, AND opencv-python-headless, because the tradecraft chapter is the likeliest in the book to carry plates), render, OCR with the already-measured crop (scripts/ocr_crop.py, chi_tra_vert --psm 5), then read every one of the 24 pages off the 300 dpi scan by eye and translate to the register in CLAUDE.md. Run all eight QC checks (author one aligned out/ch06_bilingual.md and generate out/ch06_reading.md + data/zh/ch06.txt with scripts/split_bilingual.py, then check_numbers.py and check_structure.py; blind double-translation and back-translation on the argumentative passages, and a full completeness recount of every list against the pages — this chapter is list-heavy). Detect and caption figures with find_figures.py 115 138 (it merges its manifest; needs opencv); captions in this book may be vertical text beside the plate, crop that zone and OCR with chi_tra_vert; add specs to figures.json under ch06 and never invent an identification. While translating §2 釘梢術 and §3 反偵探, confirm book.json's toc_flags_open sub-bullets against the scan where they fall in these sections. Add footnotes to notes.json keyed "ch06" (continuous numbering follows automatically, picking up from 86) and extend glossary.json with attestation (化裝術/釘梢術/反偵探 are already provisional rows — upgrade or keep as you verify). Rebuild out/gushunzhang.epub (the builder is book.json-driven and pending-aware; ch6 links automatically once out/ch06_reading.md exists), run scripts/qa_epub.py until it passes, then commit to claude/gu-shunzhang and present out/gushunzhang.epub to me directly as an attached file in this chat (not via a git link). Finally rewrite HANDOFF.md to launch Batch B07 (Chapter 6 §4-6). Cite printed folios, never PDF pages; verify the offset at the ch6 opener against folio 八三 (it was pdf−32 through ch5, but plates drift it, so READ the folio); never invent bridging text (crop the scan and read the continuation). Don't pause for my approval; run the whole batch and report back when the batch is built and QA-green.
```

## What is DONE (do not redo)

- **Batch B01 = Chapter 1 (緒論) is complete, built, QA-green.** `out/ch01_reading.md`,
  `notes.json` (`ch01`, 25 notes), glossary, EPUB all in place.
- **Batch B02 = Chapter 2 (特務組織) is complete, built, QA-green.** `out/ch02_reading.md`,
  `notes.json` (`ch02`, 19 notes, numbering 26-44), 13 glossary entries, 4 figures
  in `figures.json`/`data/figs/`.
- **Batch B03 = Chapter 3 (特務工作的方法) is complete, built, QA-green.** `out/ch03_reading.md`,
  `notes.json` (`ch03`, 9 notes, numbering 45-53), 6 glossary rows, no figures.
- **Batch B04 = Chapter 4 (特務觀念) is complete, built, QA-green.** `out/ch04_reading.md`,
  `notes.json` (`ch04`, 9 notes, numbering 54-62), 7 glossary rows, no figures.
- **Batch B05 = Chapter 5 (秘密) is complete, built, QA-green.** See `PROGRESS.md`
  for the full batch record. `out/ch05_reading.md` (138 paragraphs), `notes.json`
  (`ch05`, 23 notes, numbering **63-85**), 13 glossary rows (先施公司/永安公司 +
  祕密/祕密機關/祕密交通/交通人員/抄靶子/包探/巡捕/漏格法/明碼/娘姨/同鄉會),
  **no figures** (all 25 folios are prose/lists; `figures.json: {"ch05": []}`).
  `out/gushunzhang.epub` now carries **5 of 8 chapters, 85 notes, 11 spine files**;
  `qa_epub.py` PASSES; all structural checks pass.
- **The EPUB builder is generalised and book.json-driven.** One XHTML per
  translated chapter, full pending-aware TOC (ch1-5 linked and deep-linked;
  ch6-8 shown pending), continuous footnote numbering, refuses to build on any
  unmatched note anchor. You do NOT need to touch the builder for ch6; adding
  `out/ch06_reading.md` is enough for it to appear.
- **`scripts/split_bilingual.py`** turns one `out/<id>_bilingual.md` into the
  shipped `out/<id>_reading.md` and the parity source `data/zh/<id>.txt`.
  Invocation: `python3 scripts/split_bilingual.py out/ch06_bilingual.md ch06 "第六章 特務技術"`.
  Bilingual format: `## H2/H3/H4 <heading>` heading lines, then paragraph pairs
  of a `> <source>` line immediately followed by one English line. Use `## H4`
  for the 一、二、三 sub-parts (they render as `#### I./II./III.` and do NOT count
  as parity paragraphs — same convention ch2 and ch5 use). (`out/*_bilingual.md`
  is gitignored — QC only, never shipped.)
- **`scripts/check_numbers.py`** NOISE list now also handles the ch5 false
  positives (二房東, 五倍子, 五香, 四週) on top of the earlier ones. Keep
  extending it as new measure-word / fixed-term hits appear.
- **OCR crop geometry is correct**; just run `ocr_crop.py`. `OMP_THREAD_LIMIT=1`
  is mandatory; verify `pgrep -c tesseract` is 0 after each run.
- **Page offset is pdf−32 through ch5** (folios 58-82 each read off the page,
  opener 五八 verified). book.json says ch6 opener PDF 115 = printed 83 (same
  offset), but READ the folio 八三 at the opener; the tradecraft chapter is the
  likeliest to bind in unpaginated plates that drift the offset.

## Your job next session: Batch B06 = Chapter 6 §1-3 (特務技術 / Tradecraft)

- **Scope:** ch06 §1-3. **PDF 115-138 = printed folios 83-106** (24 pages).
  - §1 化裝術 — Disguise — PDF 115 / folio 83
  - §2 釘梢術 — Shadowing / Tailing — PDF 117 / folio 85
  - §3 反偵探 — Counter-Surveillance — PDF 127 / folio 95
- **Section anchors are in `book.json`.** Verify the ch6 opener is folio 八三 by
  eye; offset from ch5 was pdf−32, but plates drift it, so READ the folio.
- **This chapter is the likeliest in the book to carry plates** (disguise,
  tailing geometry). Install `opencv-python-headless` and run
  `find_figures.py 115 138` (it merges its manifest). Crop any caption zone and
  OCR vertical captions with `chi_tra_vert`; add specs to `figures.json` under
  `ch06`. Never invent an identification. (Chapter 5 turned out to have none, so
  don't force it — but check, and caption honestly if plates are there.)
- **book.json `toc_flags_open`:** the ch6 deep sub-bullets not yet verified fall
  mostly in later sections (§4 Weapons, §8 Observation, §10 Hypnotism → batches
  B07/B08), but confirm any sub-item structure inside §1-3 against the scan as
  you translate, and update book.json if the bookmarks and the body disagree.
- Recurring subjects already noted in ch1-5 do NOT get re-noted unless the new
  context adds something. In particular **釘梢/釘梢術 was already noted and
  glossed in ch05** ("the art of shadowing"), as were 抄靶子, 巡捕, 包探,
  化裝術/反偵探 (glossary provisional), GPU, C.P., the Green/Red Gangs, 社會化,
  巡捕房, etc.

## The 11-batch plan (from Winston)

B01 ch1 [DONE] · B02 ch2 [DONE] · B03 ch3 [DONE] · B04 ch4 [DONE] ·
B05 ch5 [DONE] · B06 ch6 §1-3 · B07 ch6 §4-6 · B08 ch6 §7-11 ·
B09 ch7 §1-3 · B10 ch7 §4 · B11 ch8. Full page ranges in `book.json` -> `batches`.

## Open traps / environment

- Traditional OCR model only (`chi_tra` / `chi_tra_vert`), never `chi_sim`.
- Env tools are NOT installed in a fresh container; install them first. In this
  environment `apt-get install ... poppler-utils` 404s on poppler and aborts the
  WHOLE transaction — install the tesseract packages WITHOUT poppler-utils
  (`apt-get install -y --no-install-recommends tesseract-ocr tesseract-ocr-chi-tra
  tesseract-ocr-chi-tra-vert`); we render via PyMuPDF and don't need poppler.
  `pip install pymupdf pillow numpy opencv-python-headless` all install cleanly.
  PaddleOCR will NOT install (weights host off the allowlist); fall back to
  `chi_tra_vert` + eye-read and say so.
- NCL seal over central columns; crop-verify anything under it.
- Offset drift: no constant page formula; read folios off the page.
- `OMP_THREAD_LIMIT=1` for tesseract; orphaned children spin after a kill.
- **Parity is necessary but not sufficient**: it compares two files derived from
  the same bilingual, so a run of items dropped from the bilingual is invisible
  to it. Always recount list items against the scanned pages — doubly important
  for the list-heavy tradecraft chapter.
- **Load-bearing numerals get crop-verified at magnification.** In ch5 the whole
  telegraph-cipher page (folio 76) was zoomed and the arithmetic checked for
  self-consistency; do the same for any tables, unit numbers, or measurements in
  ch6 (weapons calibres etc. come in B07).
- Carried-forward open items: 別動隊 rendering provisional (from ch1); the ch7
  GPU spelling (格伯烏) to be reconciled with ch1's 格伯武 when ch7 is done;
  中央特務會議/中央特務總部/各省區特務部 provisional (from the ch2 plate);
  中心思想 rendered "central conviction" provisional (from ch4); 抄靶子
  "stop-and-frisk" provisional (from ch5). Two ch5 source misprints recorded and
  footnoted (店務員→電務員 folio 78; 綠化鈷→氯化鈷 folio 73) — watch for more.
