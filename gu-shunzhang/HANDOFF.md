# HANDOFF — 特務工作之理論與實際 (Gu Shunzhang)

This file is the baton. A fresh instance with no memory of prior sessions
should read it and start immediately. Rewrite it at the end of every batch, and
always keep the paste-ready message below as its first section.

## Message to paste into the next chat

```
Read gu-shunzhang/CLAUDE.md in full (note the standing rules at the top), then gu-shunzhang/HANDOFF.md, then gu-shunzhang/book.json. Work only on the claude/gu-shunzhang branch; if the session starts you elsewhere, move your work onto claude/gu-shunzhang and drop the stray branch. Then do Batch B04 = Chapter 4 (特務觀念, The Secret-Service Mindset) — PDF pages 84-89, printed folios 52-57, its 3 sections (ch04s01 to ch04s03) — end to end: install the environment (tesseract-ocr chi_tra + chi_tra_vert, pymupdf, pillow, numpy; opencv only if the chapter has plates), render, OCR with the already-measured crop (scripts/ocr_crop.py, chi_tra_vert --psm 5), then read every page off the 300 dpi scan by eye and translate to the register in CLAUDE.md. Run all eight QC checks (author one aligned out/ch04_bilingual.md and generate out/ch04_reading.md + data/zh/ch04.txt with scripts/split_bilingual.py, then check_numbers.py and check_structure.py; blind double-translation and back-translation on the argumentative passages). Note that book.json's toc_flags_resolved fixes the ch04 §2 title to 觀念鬥爭 = "The Struggle over Mindset" (the translated TOC's "Building the Right Mindset" is an interpretation) — confirm against the section opener and translate faithfully. Add footnotes to notes.json keyed "ch04" (continuous numbering follows automatically) and extend glossary.json with attestation. Detect and caption figures if any (find_figures.py needs opencv; captions may be vertical, OCR with chi_tra_vert). Rebuild out/gushunzhang.epub (the builder is already book.json-driven and pending-aware; ch4 will link automatically), run scripts/qa_epub.py until it passes, then commit to claude/gu-shunzhang and present out/gushunzhang.epub to me directly as an attached file in this chat (not via a git link). Finally rewrite HANDOFF.md to launch Batch B05 (Chapter 5). Cite printed folios, never PDF pages; verify the offset at the ch4 opener against folio 五二; never invent bridging text (crop the scan and read the continuation). Don't pause for my approval; run the whole batch and report back when Chapter 4 is built and QA-green.
```

## What is DONE (do not redo)

- **Batch B01 = Chapter 1 (緒論) is complete, built, QA-green.** `out/ch01_reading.md`,
  `notes.json` (`ch01`, 25 notes), glossary, EPUB all in place.
- **Batch B02 = Chapter 2 (特務組織) is complete, built, QA-green.** `out/ch02_reading.md`,
  `notes.json` (`ch02`, 19 notes, numbering 26-44), 13 glossary entries, 4 figures
  in `figures.json`/`data/figs/`.
- **Batch B03 = Chapter 3 (特務工作的方法) is complete, built, QA-green.** See
  `PROGRESS.md` for the full batch record. `out/ch03_reading.md`, `notes.json`
  (`ch03`, 9 notes, numbering 45-53), 6 new glossary rows, no figures (the
  chapter has no plates). `out/gushunzhang.epub` now carries **3 of 8 chapters,
  53 notes, 9 spine documents**; `qa_epub.py` PASSES; all structural checks pass.
- **The EPUB builder is generalised and book.json-driven.** One XHTML per
  translated chapter, full pending-aware TOC (ch1-3 linked and deep-linked;
  ch4-8 shown pending), continuous footnote numbering, refuses to build on any
  unmatched note anchor. You do NOT need to touch the builder for ch4; adding
  `out/ch04_reading.md` is enough for it to appear.
- **`scripts/split_bilingual.py`** turns one `out/<id>_bilingual.md` into the
  shipped `out/<id>_reading.md` and the parity source `data/zh/<id>.txt`.
  Invocation: `python3 scripts/split_bilingual.py out/ch04_bilingual.md ch04 "第四章 特務觀念"`.
- **`scripts/check_numbers.py`** NOISE list extended (B03): 千萬/萬萬 reordered
  before the bare 萬X idioms (fixes a 千→1000 orphan), and `r"\d+[．.、]"` added
  to strip the Arabic sub-item enumerators the book prints (1. 2. 3.). Keep
  extending it as new false positives appear.
- **OCR crop geometry is correct**; just run `ocr_crop.py`.
- **Page offset is currently pdf−32** (verified PDF 72 = folio 四〇, PDF 84 =
  printed 52 per book.json → same offset, but READ the folio; plates drift it).

## Your job this session: Batch B04 = Chapter 4 (The Secret-Service Mindset)

- **Scope:** ch04, its 3 sections. **PDF 84-89 = printed folios 52-57.**
  - §1 觀念問題之重要 — Why the Question of Mindset Matters — PDF 84 / folio 52
  - §2 觀念鬥爭 — The Struggle over Mindset — PDF 85 / folio 53
  - §3 特務人員的人生觀 — The Life-Outlook of Secret-Service Personnel — PDF 87 / folio 55
  - (Section anchors are in `book.json`. Verify the ch4 opener is folio 五二 by
   eye; the offset from ch3 was pdf−32, but plates drift it, so READ the folio.)

## The pipeline for this batch (per CLAUDE.md)

1. Install env (tesseract chi_tra + chi_tra_vert, pymupdf, pillow, numpy;
   opencv only if the chapter has plates). PaddleOCR will not install (weights
   host off the allowlist); fall back to `chi_tra_vert` + eye-read and say so.
2. `python3 scripts/render.py 84 89 --dpi 300`, then
   `OMP_THREAD_LIMIT=1 python3 scripts/ocr_crop.py 84 89`. Kill stray tesseract
   children and confirm `pgrep -c tesseract` is 0 after.
3. Read EVERY page off the 300 dpi PNG by eye (the OCR is a diff partner only).
   Crop-verify every name, number, and low-confidence span, and anything under
   the NCL seal. **book.json's `toc_flags_resolved` fixes the §2 title** to
   觀念鬥爭 = "The Struggle over Mindset"; confirm against the opener.
4. Author `out/ch04_bilingual.md` (source line `>` above English), then
   `split_bilingual.py`. Run `check_numbers.py out/ch04_bilingual.md` and
   `check_structure.py --pairs data/zh/ch04.txt out/ch04_reading.md` until clean.
   Blind double-translation + back-translation on the argumentative passages
   (Chapter 4 is likely to be mostly argumentative — it is about outlook and
   ideological struggle — so double the bulk of it, not just a sample).
   **After the automated checks pass, do a completeness pass**: parity can be
   green while a whole run of items is missing from BOTH files. Recount each
   section's items against the pages before you trust parity.
5. Footnotes into `notes.json` under `ch04`; recurring subjects already noted in
   ch1-3 (GPU, C.P., Gu, KMT, Three Principles, National Revolution, the Green/
   Red Gangs, 工部局/捕房, the three-layer taxonomy, 匪區, 社會化, the six §1
   principles, 紙上談兵 and the Sunzi tag) do NOT get re-noted unless the new
   context adds something. Glossary rows with status + attestation.
6. Figures: ch4 is short prose and likely has NO plates; check with
   `find_figures.py 84 89` (merges its manifest) after `pip install
   opencv-python-headless`. If there are captioned insets, crop and OCR with
   `chi_tra_vert`; add specs to `figures.json` under `ch04`. Never invent an
   identification.
7. Rebuild `out/gushunzhang.epub`, run `qa_epub.py` until PASS. Commit
   (message like "B04 ch4: ..."). Present the EPUB to Winston as an attached
   file in chat. Then rewrite this HANDOFF for **Batch B05 = Chapter 5 (秘密,
   Secrecy, PDF 90-114, printed 58-82)** with a fresh kickoff block at the top.

## The 11-batch plan (from Winston)

B01 ch1 [DONE] · B02 ch2 [DONE] · B03 ch3 [DONE] · B04 ch4 · B05 ch5 ·
B06 ch6 §1-3 · B07 ch6 §4-6 · B08 ch6 §7-11 · B09 ch7 §1-3 · B10 ch7 §4 ·
B11 ch8. Full page ranges in `book.json` -> `batches`.

## Open traps / environment

- Traditional OCR model only (`chi_tra` / `chi_tra_vert`), never `chi_sim`.
- NCL seal over central columns; on the ch3 pages it sat over the lower-middle
  of the text block and obscured one character (暗中進行, folio 50, footnoted).
  Read folios off the page; the offset drifts across plates (pdf−32 at ch3).
- `OMP_THREAD_LIMIT=1` for tesseract; orphaned children spin after a kill.
- Env tools are NOT installed in a fresh container; install them first.
- **Parity is necessary but not sufficient**: it compares two files derived
  from the same bilingual, so a run of items dropped from the bilingual is
  invisible to it. Always recount list items against the scanned pages.
- Carried-forward open items: 別動隊 rendering provisional (from ch1); the ch7
  GPU spelling (格伯烏) to be reconciled with ch1's 格伯武 when ch7 is done;
  中央特務會議/中央特務總部/各省區特務部 are provisional (from the ch2 plate).
