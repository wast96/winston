# HANDOFF — 特務工作之理論與實際 (Gu Shunzhang)

This file is the baton. A fresh instance with no memory of prior sessions
should read it and start immediately. Rewrite it at the end of every batch, and
always keep the paste-ready message below as its first section.

## Message to paste into the next chat

```
Read gu-shunzhang/CLAUDE.md in full (note the standing rules at the top), then gu-shunzhang/HANDOFF.md, then gu-shunzhang/book.json. Work only on the claude/gu-shunzhang branch; if the session starts you elsewhere, move your work onto claude/gu-shunzhang and drop the stray branch. Then do Batch B03 = Chapter 3 (特務工作的方法, Methods of Secret-Service Work) — PDF pages 72-83, printed folios 40-51, its 3 sections (ch03s01 to ch03s03) — end to end: install the environment (tesseract-ocr chi_tra + chi_tra_vert, pymupdf, pillow, numpy; opencv for figures if the chapter has plates), render, OCR with the already-measured crop (scripts/ocr_crop.py, chi_tra_vert --psm 5), then read every page off the 300 dpi scan by eye and translate to the register in CLAUDE.md. Run all eight QC checks (author one aligned out/ch03_bilingual.md and generate out/ch03_reading.md + data/zh/ch03.txt with scripts/split_bilingual.py, then check_numbers.py and check_structure.py; blind double-translation and back-translation on the argumentative passages). Add footnotes to notes.json keyed "ch03" (continuous numbering follows automatically) and extend glossary.json with attestation. Detect and caption figures if any (find_figures.py needs opencv; captions may be vertical, OCR with chi_tra_vert). Rebuild out/gushunzhang.epub (the builder is already book.json-driven and pending-aware; ch3 will link automatically), run scripts/qa_epub.py until it passes, then commit to claude/gu-shunzhang and present out/gushunzhang.epub to me directly as an attached file in this chat (not via a git link). Finally rewrite HANDOFF.md to launch Batch B04 (Chapter 4). Cite printed folios, never PDF pages; verify the offset at the ch3 opener against folio 四十; never invent bridging text (crop the scan and read the continuation). Don't pause for my approval; run the whole batch and report back when Chapter 3 is built and QA-green.
```

## What is DONE (do not redo)

- **Batch B01 = Chapter 1 (緒論) is complete, built, QA-green.** `out/ch01_reading.md`,
  `notes.json` (`ch01`, 25 notes), glossary, EPUB all in place.
- **Batch B02 = Chapter 2 (特務組織) is complete, built, QA-green.** See
  `PROGRESS.md` for the full batch record. `out/ch02_reading.md`, `notes.json`
  (`ch02`, 19 notes, numbering 26-44), 13 new glossary entries, 4 figures in
  `figures.json`/`data/figs/`, and `out/gushunzhang.epub` (2 of 8 chapters,
  44 notes) are all in place; `qa_epub.py` PASSES.
- **The EPUB builder is generalised and book.json-driven.** It emits one XHTML
  per translated chapter, a full pending-aware TOC (ch1-2 linked and their
  sections deep-linked; ch3-8 shown pending), continuous footnote numbering,
  and refuses to build on any unmatched note anchor. You do NOT need to touch
  the builder for ch3; adding `out/ch03_reading.md` is enough for it to appear.
- **`scripts/split_bilingual.py`** turns one `out/<id>_bilingual.md` into the
  shipped `out/<id>_reading.md` and the parity source `data/zh/<id>.txt`.
  Invocation: `python3 scripts/split_bilingual.py out/ch03_bilingual.md ch03 "第三章 特務工作的方法"`.
- **`scripts/check_numbers.py`** NOISE list has been extended for this book,
  most recently with 萬-intensifier idioms (萬不得已, 萬不可, 萬一, 萬分, 萬萬,
  千萬). Keep extending it as new measure-word / idiom false positives appear.
- **OCR crop geometry is correct**; just run `ocr_crop.py`.

## Your job this session: Batch B03 = Chapter 3 (Methods of Secret-Service Work)

- **Scope:** ch03, its 3 sections. **PDF 72-83 = printed folios 40-51.**
  - §1 工作的原則 — Principles of the Work — PDF 72 / folio 40
  - §2 工作上絕對反對的事項 — Things Absolutely Forbidden in the Work — PDF 76 / folio 44
  - §3 工作的實施 — Carrying Out the Work — PDF 80 / folio 48
  - (Section anchors are in `book.json`. Verify the ch3 opener is folio 四十 by
   eye; the offset from ch2 was pdf-31, but plates drift it, so READ the folio.)

## The pipeline for this batch (per CLAUDE.md)

1. Install env (tesseract chi_tra + chi_tra_vert, pymupdf, pillow, numpy;
   opencv only if the chapter has plates). PaddleOCR will not install (weights
   host off the allowlist); fall back to `chi_tra_vert` + eye-read and say so.
2. `python3 scripts/render.py 72 83 --dpi 300`, then
   `OMP_THREAD_LIMIT=1 python3 scripts/ocr_crop.py 72 83`. Kill stray tesseract
   children and confirm `pgrep -c tesseract` is 0 after.
3. Read EVERY page off the 300 dpi PNG by eye (the OCR is a diff partner only).
   Crop-verify every name, number, and low-confidence span. Watch for the
   enumerated principle lists — **book.json's `toc_flags_resolved` already
   corrects the ch3 §1 principles** to, in order: 1 積極性 proactiveness,
   2 祕密性 secrecy, 3 敏捷性 agility, 4 精密性 precision, 5 普遍性 universality,
   6 實際性 practicality (the translated TOC mislabeled items 2 and 5). Confirm
   against the body and translate them faithfully.
4. Author `out/ch03_bilingual.md` (source line `>` above English), then
   `split_bilingual.py`. Run `check_numbers.py out/ch03_bilingual.md` and
   `check_structure.py --pairs data/zh/ch03.txt out/ch03_reading.md` until clean.
   Blind double-translation + back-translation on the argumentative passages;
   sample the enumerated filler. **After the automated checks pass, do a
   completeness pass**: parity can be green while a whole run of list items is
   missing from BOTH files (that happened in B02 with §7 f-m). Recount each
   section's items against the pages before you trust parity.
5. Footnotes into `notes.json` under `ch03`; recurring subjects already noted in
   ch1-2 (GPU, C.P., Gu, KMT, Three Principles, National Revolution, the Green/
   Red Gangs, 工部局/捕房, the three-layer taxonomy) do NOT get re-noted unless
   the new context adds something. Glossary rows with status + attestation.
6. Figures: ch3 is short prose and may have NO plates; check with
   `find_figures.py 72 83` (merges its manifest) after `pip install
   opencv-python-headless`. If there are captioned insets, crop and OCR with
   `chi_tra_vert`; add specs to `figures.json` under `ch03`. Never invent an
   identification.
7. Rebuild `out/gushunzhang.epub`, run `qa_epub.py` until PASS. Commit
   (message like "B03 ch3: ..."). Present the EPUB to Winston as an attached
   file in chat. Then rewrite this HANDOFF for **Batch B04 = Chapter 4 (特務觀念,
   The Secret-Service Mindset, PDF 84-89, printed 52-57)** with a fresh kickoff
   block at the top.

## The 11-batch plan (from Winston)

B01 ch1 [DONE] · B02 ch2 [DONE] · B03 ch3 · B04 ch4 · B05 ch5 · B06 ch6 §1-3 ·
B07 ch6 §4-6 · B08 ch6 §7-11 · B09 ch7 §1-3 · B10 ch7 §4 · B11 ch8.
Full page ranges in `book.json` -> `batches`.

## Open traps / environment

- Traditional OCR model only (`chi_tra` / `chi_tra_vert`), never `chi_sim`.
- NCL seal over central columns; on the ch2 pages it sat mostly off the text,
  but do not assume. Read folios off the page; the offset drifts across plates.
- `OMP_THREAD_LIMIT=1` for tesseract; orphaned children spin after a kill.
- Env tools are NOT installed in a fresh container; install them first.
- **Parity is necessary but not sufficient**: it compares two files derived
  from the same bilingual, so a run of items dropped from the bilingual is
  invisible to it. Always recount list items against the scanned pages.
- Carried-forward open items: 別動隊 rendering provisional (from ch1); the ch7
  GPU spelling (格伯烏) to be reconciled with ch1's 格伯武 when ch7 is done;
  中央特務會議/中央特務總部/各省區特務部 are provisional (from the ch2 plate).
