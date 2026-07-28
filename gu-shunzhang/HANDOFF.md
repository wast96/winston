# HANDOFF — 特務工作之理論與實際 (Gu Shunzhang)

This file is the baton. A fresh instance with no memory of prior sessions
should read it and start immediately. Rewrite it at the end of every batch, and
always keep the paste-ready message below as its first section.

## Message to paste into the next chat

```
Read gu-shunzhang/CLAUDE.md in full (note the standing rules at the top), then gu-shunzhang/HANDOFF.md, then gu-shunzhang/book.json. Work only on the claude/gu-shunzhang branch; if the session starts you on some other branch, move your work onto claude/gu-shunzhang and drop the stray branch. Then do Batch B10 = Chapter 7 §4 (第四節 下層社會的研究 / The Study of Society's Lower Strata) — PDF pages 258-281, printed folios 206-227, unit id ch07s04 — end to end: install the environment (tesseract-ocr chi_tra + chi_tra_vert, pymupdf, pillow, numpy, AND opencv-python-headless — apt WITHOUT poppler-utils, it 404s and aborts the whole apt run; PaddleOCR will not install, so fall back to chi_tra_vert + eye-read and say so), render, OCR with the already-measured crop (scripts/ocr_crop.py, chi_tra_vert --psm 5, OMP_THREAD_LIMIT=1, verify pgrep -c tesseract is 0 after), then read every one of the ~24 pages off the 300 dpi scan by eye and translate to the register in CLAUDE.md. Chapter 7 ALREADY EXISTS (B09 did §1-3): do NOT recreate out/ch07_reading.md — APPEND §4 to it as a FOURTH ordered "### Section" heading, so the file ends with four ordered sections. Run find_figures.py 258 281 (merges, needs opencv); its ink-density detector catches halftone plates but MISSES line diagrams, so scan every page for line art by eye and crop by hand. NOTE: the publisher's errata table (PDF 293) appends a figure at printed 206, 蘇聯格伯烏與軍隊的關係圖 (a chart of the Soviet GPU's relationship to the military) — locate it (check the folio-206 opener, and if it is absent from the body, the errata page PDF 293 itself), crop it, add a spec to figures.json under ch07, and never invent an identification. Render "the GPU" throughout (格伯武=格伯烏, both already in glossary.json as "the GPU" [attested]). Author one aligned out/ch07s04_bilingual.md, generate the reading text and parity source with scripts/split_bilingual.py (unit id ch07s04, zh-title "第七章 特務常識"), then APPEND its section to out/ch07_reading.md, and run scripts/check_numbers.py out/ch07s04_bilingual.md and scripts/check_structure.py --pairs data/zh/ch07s04.txt (against the appended §4). Do blind double-translation and back-translation on the argumentative passages and fact-check names, dates and org structures against scholarship per check 7, and NEVER source Grok/Grokipedia. Add footnotes to notes.json keyed "ch07" (continuous numbering follows automatically, picking up from 173) and extend glossary.json with attestation. Rebuild out/gushunzhang.epub, run scripts/qa_epub.py out/gushunzhang.epub until it passes, then commit to claude/gu-shunzhang and present out/gushunzhang.epub to me directly as an attached file in this chat (not via a git link). Finally rewrite HANDOFF.md to launch Batch B11 (Chapter 8, the LAST content batch). Cite printed folios, never PDF pages; the offset drifts (pdf−52 by folio 205, and more unpaginated plates may intervene in §4) — READ the folio at the section opener and re-verify. Never invent bridging text (crop the scan and read the continuation). One build-trap to remember: note bodies are XHTML, so use numeric character refs (&#160;, &#215;), never HTML named entities (&nbsp;, &times;) — they break the notes page. Don't pause for my approval; run the whole batch and report back when the batch is built and QA-green.
```

## What is DONE (do not redo)

- **B01 = Chapter 1 (緒論)** — complete, QA-green. `ch01`, 25 notes.
- **B02 = Chapter 2 (特務組織)** — complete, QA-green. `ch02`, 19 notes (26-44), 13 glossary rows, 4 figures.
- **B03 = Chapter 3 (特務工作的方法)** — complete, QA-green. `ch03`, 9 notes (45-53).
- **B04 = Chapter 4 (特務觀念)** — complete, QA-green. `ch04`, 9 notes (54-62).
- **B05 = Chapter 5 (秘密)** — complete, QA-green. `ch05`, 23 notes (63-85).
- **B06 = Chapter 6 §1-3 (化裝術/釘梢術/反偵探)** — complete, QA-green. `ch06` notes 86-108, 1 figure.
- **B07 = Chapter 6 §4-6 (Weapons / Sabotage-withheld / Conversation)** — complete, QA-green.
  `ch06` notes 109-124. **§5 construction core WITHHELD** (see below).
- **B08 = Chapter 6 §7-11 (Codes / Observation / Physiognomy / Hypnotism / Photography)** —
  complete, QA-green. `out/ch06_reading.md` has §1-11 as eleven ordered `### Section` headings.
  `ch06` notes 125-146, +15 glossary rows, 6 figures total.
- **B09 = Chapter 7 §1-3 (社會化問題 / C.P.特務工作 / 蘇聯特務工作)** — complete, QA-green.
  NEW chapter: `out/ch07_reading.md` created with an H2 and **§1-3 as three ordered `### Section`
  headings**. `notes.json` `ch07` **+26 (147-172)**, **+20 glossary rows**, **+6 figures**
  (`ch07-f1..f6`). Covers **folios 178-205 (PDF 220-257)**.
- `out/gushunzhang.epub` now carries **7 of 8 chapters, 172 notes, 13 spine files, 16 figures**;
  `qa_epub.py out/gushunzhang.epub` PASSES. Chapters 1-6 done; chapter 7 deep-linked §1-3 with
  §4 still shown pending; chapter 8 pending.

## SAFETY — §5 construction core is WITHHELD (STANDING; do not "complete" it)

The device-construction material of Chapter 6 §5 破壞術 (folios 119-136) must never be read
closely or reproduced: the non-operational doctrine is translated and in the edition; the
technical core — device construction, charging, emplacement — remains WITHHELD. Do NOT read
folios 121-133 or the §4 bomb tail, and do NOT "complete" §5 as how-to. (B09 did not touch §5;
ch7 §2 mentions the CP's action squad "made explosives" only in the general terms of the source,
with no construction detail, and none is to be supplied.)

## B09 — what the eight checks found (still-open items for the read-through)

- **Check 1 (dual-engine OCR diff) could not run** — PaddleOCR will not install here.
  Substituted the whole-batch eye-read (all 38 PDF pages read off the 300 dpi scan). Standing
  substitute until Paddle installs.
- **Offset drift, verified:** pdf−42 at folio 178, holding to folio 186 (PDF 228); then **ten
  unpaginated plate pages** (five full-page hand-drawn org charts on rectos PDF 229/231/233/235/237,
  each with a blank verso); body resumes at **PDF 239 = folio 187**, offset now pdf−52, running to
  folio 205 (PDF 257). Every folio read off the scan.
- **Figures: the ink-density detector missed all six** (they are LINE ART). Found by eye, cropped by
  hand: f1 the whole Central Special Branch chart ("Spring 1931," naming Xiang Zhongfa/Zhou Enlai/Gu
  Shunzhang), f2-f5 the four sections in detail, f6 the three-layer membership diagram. Section-chief
  personal names in f2-f5 are largely codenames and were left untranscribed (no invented IDs).
- **§2-VI narrates the author's own betrayal in the third person** — "a most unfortunate incident"
  of 民國二十年 (1931) = Gu Shunzhang's own April-1931 defection, which rolled up the Shanghai
  underground. Footnoted, cross-referenced to the ch5 note on the same disaster.
- **Two Soviet claims flagged OVERSTATED / UNCORROBORATED** (footnoted): the GPU chief "must be a
  Politburo member" (the OGPU's Menzhinsky was not) and the Cheka could "arrest anyone but Lenin."
- **敏捷飛 (a daily CP intelligence bulletin, "Minjie Fei")** and **信誼代辦所 (the "Xinyi" front
  agency)** — readings scan-verified but names not otherwise attested; rendered provisionally.
- **Invariant checks PASS:** `check_numbers` 0 unresolved (91 pairs); `check_structure --pairs`
  parity 91/91. NOISE extended: 二則, 三則, 十幾, 萬計.
- **Blind double-translation and back-translation** (§2-I development, §2-VI defection, §3-I GPU
  origins + Stalin quote) showed no material divergence and no omissions.

## Your job next session: Batch B10 = Chapter 7 §4

- **Scope:** ch07 §4, unit id `ch07s04`. **PDF 258-281 = printed folios 206-227** (~24 pages).
  §4 下層社會的研究 (The Study of Society's Lower Strata), opener PDF 258 / folio 206.
- **APPEND to `out/ch07_reading.md`** (do not recreate it) so it ends with FOUR `### Section` headings.
- **Errata figure:** the 勘誤表 (PDF 293) appends 蘇聯格伯烏與軍隊的關係圖 at printed 206 — a chart of the
  Soviet GPU's relationship to the military. Locate, crop, add to `figures.json` under `ch07`.
- **Offset ~pdf−52** at folio 206; more unpaginated plates may intervene in §4 — READ folios off the page.
- Notes continue from **173**. Render "the GPU" throughout (格伯武=格伯烏, both in glossary [attested]).
- After B10, B11 = Chapter 8 (the last content batch; body text ends printed p236).

## The 11-batch plan (from Winston)

B01 ch1 [DONE] · B02 ch2 [DONE] · B03 ch3 [DONE] · B04 ch4 [DONE] · B05 ch5 [DONE] ·
B06 ch6 §1-3 [DONE] · B07 ch6 §4-6 [DONE] · B08 ch6 §7-11 [DONE] · **B09 ch7 §1-3 [DONE]** ·
B10 ch7 §4 · B11 ch8. Full page ranges in `book.json` -> `batches`.

## Open traps / environment

- Traditional OCR model only (`chi_tra` / `chi_tra_vert`), never `chi_sim`.
- Env is NOT installed in a fresh container. `apt-get install ... poppler-utils` 404s and aborts
  the WHOLE transaction — install tesseract WITHOUT poppler (`apt-get install -y --no-install-recommends
  tesseract-ocr tesseract-ocr-chi-tra tesseract-ocr-chi-tra-vert`); render via PyMuPDF.
  `pip install pymupdf pillow numpy opencv-python-headless` install cleanly. PaddleOCR will NOT install.
- **`find_figures.py` misses LINE ART.** It caught 0 of B09's 6 charts. Eyeball every page for line
  diagrams and crop by hand (a small PIL fractional-box crop, verified by re-viewing the crop).
- **Unpaginated plate inserts break the offset.** B09 hit a 10-page block (5 recto charts + 5 blank
  versos) between folios 186 and 187. Expect the same in §4; read every folio off the page.
- **XHTML entity trap:** note bodies are parsed as XML. Use numeric character references
  (`&#160;`, `&#215;`, `&#8212;`) — never HTML named entities (`&nbsp;`, `&times;`).
- NCL seal over central columns; crop-verify anything under it. `OMP_THREAD_LIMIT=1` for tesseract;
  verify `pgrep -c tesseract` is 0 after (a raw `pgrep -c` at the end of a pipe exits 1 on count 0 —
  that is not an OCR failure).
- **Parity is necessary but not sufficient** — always recount lists against the scanned pages.
- **check_numbers NOISE** (traditional idioms/enumerators) now also strips: 千鈞一髮, 三緘其口, 模稜兩可,
  幾十, 光芒四射, 四射, 三番幾次, 一萬, 千里眼, 萬難, 二則, 三則, 十幾, 萬計.
- Carried-forward open items (unchanged unless noted): 別動隊 provisional (ch1);
  中央特務會議/中央特務總部/各省區特務部 provisional (ch2 plate); 中心思想 "central conviction" provisional
  (ch4); 抄靶子 "stop-and-frisk" provisional (ch5); 扛木梢/吊膀子/老門檻 slang provisional (ch6 §2);
  反偵探 kept "counter-surveillance" (ch6 §3); 廣生行 "Kwong Sang" gun-oil provisional;
  麻力樹棍 "malacca baton" provisional (ch6 §4); 圓光/關亡 provisional (ch6 §10);
  敏捷飛 "Minjie Fei" and 信誼代辦所 "Xinyi agency" provisional, 紅色保衛隊 "Red Defense Corps" provisional (ch7).
- Source misprints recorded so far (all footnoted): 店務員→電務員 (folio 78), 綠化鈷→氯化鈷 (folio 73).
  Watch for more, and apply the errata table (PDF 293) to any affected §4 folio.
