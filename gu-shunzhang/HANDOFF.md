# HANDOFF — 特務工作之理論與實際 (Gu Shunzhang)

This file is the baton. A fresh instance with no memory of prior sessions
should read it and start immediately. Rewrite it at the end of every batch, and
always keep the paste-ready message below as its first section.

## Message to paste into the next chat

```
Read gu-shunzhang/CLAUDE.md in full, then gu-shunzhang/HANDOFF.md, then gu-shunzhang/book.json. Then do Batch B02 = Chapter 2 (特務組織, Secret-Service Organization) — PDF pages 43-71, printed pages 17-39, its 7 sections (ch02s01 to ch02s07) — end to end: install the environment (tesseract-ocr chi_tra + chi_tra_vert, pymupdf, pillow, numpy; opencv for figures if the chapter has plates), render, OCR with the already-measured crop (scripts/ocr_crop.py, chi_tra_vert --psm 5), then read every page off the 300 dpi scan by eye and translate to the register in CLAUDE.md. Run all eight QC checks (author one aligned out/ch02_bilingual.md and generate out/ch02_reading.md + data/zh/ch02.txt with scripts/split_bilingual.py, then check_numbers.py and check_structure.py; blind double-translation and back-translation on the argumentative passages). Add footnotes to notes.json keyed "ch02" (continuous numbering follows automatically) and extend glossary.json with attestation. Detect and caption figures if any (find_figures.py needs opencv; captions may be vertical, OCR with chi_tra_vert). Rebuild out/gushunzhang.epub (the builder is already book.json-driven and pending-aware; ch2 will link automatically), run scripts/qa_epub.py until it passes, then commit. Finally rewrite HANDOFF.md to launch Batch B03 (Chapter 3). Cite printed folios, never PDF pages; verify the drifted offset at the ch2 opener against folio 十七; never invent bridging text (crop the scan and read the continuation). Don't pause for my approval; run the whole batch and report back when Chapter 2 is built and QA-green.
```

## What is DONE (do not redo)

- **Batch B01 = Chapter 1 (緒論) is complete, built, and QA-green.** See
  `PROGRESS.md` for the full batch record. `out/ch01_reading.md`, `notes.json`
  (`ch01`, 25 notes), `glossary.json`, and `out/gushunzhang.epub` are all
  in place; `qa_epub.py` PASSES across the spine.
- **The EPUB builder is generalised and book.json-driven.** It emits one XHTML
  per translated chapter, a full 8-chapter/37-section pending-aware TOC (ch1
  linked and its sections deep-linked; ch2-8 shown pending), continuous
  footnote numbering, and refuses to build on any unmatched note anchor. You do
  NOT need to touch the builder for ch2; adding `out/ch02_reading.md` is enough
  for it to appear, linked, in the TOC.
- **`scripts/split_bilingual.py`** turns one `out/<id>_bilingual.md` into the
  shipped `out/<id>_reading.md` and the parity source `data/zh/<id>.txt`. Use
  it; it keeps the two from drifting. Invocation:
  `python3 scripts/split_bilingual.py out/ch02_bilingual.md ch02 "第二章 特務組織"`.
- **`scripts/check_numbers.py`** was extended for this book (Traditional 萬/億,
  X分之Y fractions, English million/billion, numeral-idiom NOISE). Keep
  extending the NOISE list as new measure-word false positives appear.
- **OCR crop geometry is correct**; just run `ocr_crop.py`.

## Your job this session: Batch B02 = Chapter 2 (Secret-Service Organization)

- **Scope:** ch02, its 7 sections. **PDF 43-71 = printed 17-39.**
  - §1 Principles of Organization — PDF 43 / printed 17
  - §2 The Detective Network — PDF 46 / printed 20
  - §3 The Communications Network — PDF 51 (printed anchor in book.json reads 21; verify)
  - §4 Selection of Personnel — PDF 52 / printed 22
  - §5 Discipline — PDF 59 / printed 27
  - §6 Treatment and Remuneration — PDF 62 / printed 30 (TOC "Rewards and Punishments" was WRONG; = 待遇)
  - §7 Training — PDF 67 / printed 35
  (Section page anchors are in `book.json`; the offset drifts, so read the folio
  off each page rather than computing it. Confirm the ch2 opener is printed 十七.)

## The pipeline for this batch (per CLAUDE.md)

1. Install env (see the kickoff message). PaddleOCR will almost certainly not
   install (weights host is off the allowlist); fall back to `chi_tra_vert` and
   the eye-read, and say so, exactly as B01 did.
2. `python3 scripts/render.py 43 71 --dpi 300`, then
   `OMP_THREAD_LIMIT=1 python3 scripts/ocr_crop.py 43 71`.
3. Read EVERY page off the 300 dpi PNG by eye (the seal corrupts central
   columns; the eye-read is the authority). Crop-verify every name, number, and
   low-confidence span. Chapter 2 is organizational and will have concrete
   numbers (personnel grades, pay, cell sizes); those are load-bearing, so
   crop-verify each.
4. Author `out/ch02_bilingual.md` (source line `>` above English), then
   `split_bilingual.py`. Run `check_numbers.py out/ch02_bilingual.md` and
   `check_structure.py` (parity/anchors/headings/drift) until clean. Do the
   blind double-translation and back-translation on the argumentative passages;
   sample the list/enumeration filler.
5. Footnotes into `notes.json` under `ch02`; recurring subjects already noted
   in ch1 (GPU, C.P., Gu, the KMT, Three Principles, National Revolution) do NOT
   get re-noted unless the new context adds something. Glossary rows with
   status + attestation.
6. Figures: if the chapter has plates, `pip install opencv-python-headless`,
   run `find_figures.py 43 71` (it merges its manifest), crop caption zones and
   OCR with `chi_tra_vert`; add specs to `figures.json` under `ch02`. If no
   caption is legible, caption neutrally; never invent an identification.
7. Rebuild `out/gushunzhang.epub`, run `qa_epub.py` until PASS. Commit
   (message like "B02 ch2: ..."). Then rewrite this HANDOFF for **Batch B03 =
   Chapter 3 (特務工作的方法, PDF 72-83, printed 40-51)** with a fresh kickoff
   block at the top.

## The 11-batch plan (from Winston)

B01 ch1 [DONE] · B02 ch2 · B03 ch3 · B04 ch4 · B05 ch5 · B06 ch6 §1-3 ·
B07 ch6 §4-6 · B08 ch6 §7-11 · B09 ch7 §1-3 · B10 ch7 §4 · B11 ch8.
Full page ranges in `book.json` -> `batches`.

## Open traps / environment

- Traditional OCR model only (`chi_tra` / `chi_tra_vert`), never `chi_sim`.
- NCL seal over central columns; a few pages carry heavy dark-edge artifacts.
  Read folios off the page; offset drifts (use `book.json` anchors).
- `OMP_THREAD_LIMIT=1` for tesseract; orphaned children spin after a kill.
- Env tools are NOT installed in a fresh container; install them first.
- ch01 open items carried forward: 別動隊 rendering is provisional; the ch7 GPU
  spelling (格伯烏) should be reconciled with ch1's 格伯武 when ch7 is done.
