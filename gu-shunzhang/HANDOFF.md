# HANDOFF — 特務工作之理論與實際 (Gu Shunzhang)

This file is the baton. A fresh instance with no memory of prior sessions
should read it and start immediately. Rewrite it at the end of every batch, and
always keep the paste-ready message below as its first section.

## Message to paste into the next chat

```
Read gu-shunzhang/CLAUDE.md in full (note the standing rules at the top), then gu-shunzhang/HANDOFF.md, then gu-shunzhang/book.json. Work only on the claude/gu-shunzhang branch; if the session starts you on some other branch, move your work onto claude/gu-shunzhang and drop the stray branch. Then do Batch B09 = Chapter 7 §1-3 (特務常識 / General Knowledge for Secret-Service Work: 第一節 社會化問題 Blending Into Society, 第二節 C.P.特務工作 CP [Communist Party] Secret-Service Work, 第三節 蘇聯特務工作 Soviet Secret-Service Work) — PDF pages 220-257, printed folios 178-205, unit ids ch07s01 to ch07s03 — end to end: install the environment (tesseract-ocr chi_tra + chi_tra_vert, pymupdf, pillow, numpy, AND opencv-python-headless — apt WITHOUT poppler-utils, it 404s and aborts the whole apt run; PaddleOCR will not install, so fall back to chi_tra_vert + eye-read and say so), render, OCR with the already-measured crop (scripts/ocr_crop.py, chi_tra_vert --psm 5, OMP_THREAD_LIMIT=1, verify pgrep -c tesseract is 0 after), then read every one of the ~38 pages off the 300 dpi scan by eye and translate to the register in CLAUDE.md. This is Chapter 7, a NEW chapter (ch06 is finished): create out/ch07_reading.md fresh with a "## Chapter 7. General Knowledge for Secret-Service Work" H2 and §1-3 as three ordered "### Section" headings. Run find_figures.py 220 257 (merges, needs opencv); its ink-density detector catches halftone plates but MISSES line diagrams, so scan every page for line art by eye and crop by hand if needed; add specs to figures.json under ch07 and never invent an identification. NOTE the ch7 §3 (Soviet) material: reconcile the GPU spelling — ch1 used 格伯武 and an earlier ch7 note flagged 格伯烏; both are already in glossary.json as "the GPU" [attested], so render "the GPU" throughout and pick ONE hanzi headword if the body forces a choice. The publisher's errata table (PDF 293) appends a figure at printed 206 (蘇聯格伯烏與軍隊的關係圖, GPU-military relationship chart) — that folio is §4 (B10), NOT this batch, so do not chase it here. Author one aligned out/ch07s01-03_bilingual.md, generate the reading text and parity source with scripts/split_bilingual.py (unit id ch07s01-03, zh-title "第七章 特務常識"), then run scripts/check_numbers.py and scripts/check_structure.py; do blind double-translation and back-translation on the argumentative passages (the CP/Soviet sections are polemical and history-heavy — fact-check names, dates and org structures against scholarship per check 7, and NEVER source Grok/Grokipedia). Add footnotes to notes.json keyed "ch07" (continuous numbering follows automatically, picking up from 147) and extend glossary.json with attestation. Rebuild out/gushunzhang.epub, run scripts/qa_epub.py out/gushunzhang.epub until it passes, then commit to claude/gu-shunzhang and present out/gushunzhang.epub to me directly as an attached file in this chat (not via a git link). Finally rewrite HANDOFF.md to launch Batch B10 (Chapter 7 §4). Cite printed folios, never PDF pages; the offset drifts (~pdf−42 by folio 177) — READ the folio at each section opener and re-verify. Never invent bridging text (crop the scan and read the continuation). One build-trap to remember: note bodies are XHTML, so use numeric character refs (&#160;, &#215;), never HTML named entities (&nbsp;, &times;) — they break the notes page. Don't pause for my approval; run the whole batch and report back when the batch is built and QA-green.
```

## What is DONE (do not redo)

- **B01 = Chapter 1 (緒論)** — complete, QA-green. `ch01`, 25 notes.
- **B02 = Chapter 2 (特務組織)** — complete, QA-green. `ch02`, 19 notes (26-44),
  13 glossary rows, 4 figures.
- **B03 = Chapter 3 (特務工作的方法)** — complete, QA-green. `ch03`, 9 notes (45-53).
- **B04 = Chapter 4 (特務觀念)** — complete, QA-green. `ch04`, 9 notes (54-62).
- **B05 = Chapter 5 (秘密)** — complete, QA-green. `ch05`, 23 notes (63-85).
- **B06 = Chapter 6 §1-3 (化裝術/釘梢術/反偵探)** — complete, QA-green.
  `ch06` notes 86-108, 1 figure (street-shadowing diagram).
- **B07 = Chapter 6 §4-6 (Weapons / Sabotage-withheld / Conversation)** — complete,
  QA-green. `ch06` notes 109-124. **§5 construction core WITHHELD** (see below).
- **B08 = Chapter 6 §7-11 (Codes / Observation / Physiognomy / Hypnotism / Photography)**
  — complete, QA-green. `out/ch06_reading.md` now has **§1-11 as eleven ordered
  `### Section` headings**. `notes.json` `ch06` **+22 (125-146)**, +15 glossary rows,
  **+5 figures** (cipher wheel + four physiognomy plates; total ch06 = 6).
  Covers **folios 144-177 (PDF 176-219)**.
- `out/gushunzhang.epub` now carries **6 of 8 chapters, 146 notes, 12 spine files,
  10 figures**; `qa_epub.py out/gushunzhang.epub` PASSES. Chapter 6 is fully done and
  deep-linked §1-11; chapters 7-8 still show in the TOC as pending.

## SAFETY — §5 construction core is WITHHELD (STANDING; do not "complete" it)

The device-construction material must never be read closely or reproduced. §5 破壞術
(folios 119-136): the **non-operational doctrine** is translated and in the edition;
the **technical core — device construction, charging, emplacement — remains WITHHELD**,
marked by an editorial bracket inside §II. Do NOT read folios 121-133 or the §4 bomb
tail, and do NOT "complete" §5 as how-to. If Winston asks for more of §5, give only
strictly non-operational content and confirm scope first. (B08 did not touch §5.)

## B08 — what the eight checks found (still-open items for the read-through)

- **Check 1 (dual-engine OCR diff) could not run** — PaddleOCR will not install in this
  environment. Substituted the whole-batch eye-read (all 44 PDF pages read off the 300 dpi
  scan), as B05-B07 did. This remains the standing substitute until Paddle installs.
- **Physiognomy (§9) and hypnotism (§10) are period pseudoscience** — humoral
  "constitutions," face-verdicts, clairvoyance and telepathy. Translated faithfully as the
  author's belief and framed as such in a leading footnote; not endorsed.
- **"Austrian psychiatrist who first created hypnotism"** (§10-I) is almost certainly a
  garbled reference to Mesmer (Austrian, animal magnetism), not a psychiatrist, and the
  word "hypnotism" was Braid's. Footnoted as **uncorroborated**.
- **§10-VII** carries a brief period anecdote of an attempted hypnotic rape (told to show
  a subject wakes when commanded against his will). Rendered plainly, not sensationalized.
- **book.json TOC reconciliation (recorded in `toc_flags_resolved_b08`):**
  Observation item 5 = **能力的觀察** (Ability), CONFIRMED. Hypnotism item 5 =
  **催眠術與體質的關係** (the four temperaments), CONFIRMED. Hypnotism item 7: the
  bookmark's guess **催眠與暗示 is WRONG** — the body's seventh subsection is
  **催眠術與道德問題** (Hypnotism and the Question of Morality); no 催眠與暗示 exists.
- **check_numbers NOISE extended** for this batch: 幾十, 光芒四射/四射, 三番幾次, 一萬
  (the mahjong "1 of Characters" tile — verified no real 一萬 quantity in §7-11), 千里眼,
  萬難. All are fixed terms/idioms carrying non-quantity numerals.
- **Blind double-translation** (§8-I, §10-I) and **back-translation** (same + §10-VII)
  showed no material divergence and no omissions.

## Your job next session: Batch B09 = Chapter 7 §1-3

- **Scope:** ch07 §1-3, unit ids ch07s01-ch07s03. **PDF 220-257 = printed folios 178-205**
  (~38 pages). This is a NEW chapter — create `out/ch07_reading.md` fresh.
  - §1 社會化問題 — Blending Into Society — PDF 220 / folio 178
  - §2 C.P.特務工作 — CP [Communist Party] Secret-Service Work — PDF 227 / folio 185
  - §3 蘇聯特務工作 — Soviet Secret-Service Work — PDF 246 / folio 194
- **Offset ~pdf−42** at the start of ch7; READ the folio at each opener and re-verify.
- **Polemical, history-heavy sections.** The CP and Soviet chapters name real people,
  organizations, dates and structures — fact-check against scholarship (check 7). NEVER
  source Grok/Grokipedia (standing rule).
- **GPU spelling:** ch1 used 格伯武, an earlier ch7 note flagged 格伯烏; BOTH are already in
  `glossary.json` (organizations) as "the GPU" [attested]. Render "the GPU" throughout.
- **Errata figure** (蘇聯格伯烏與軍隊的關係圖, printed 206) belongs to §4 = B10, not B09.
- Notes continue from **147**.

## The 11-batch plan (from Winston)

B01 ch1 [DONE] · B02 ch2 [DONE] · B03 ch3 [DONE] · B04 ch4 [DONE] ·
B05 ch5 [DONE] · B06 ch6 §1-3 [DONE] · B07 ch6 §4-6 [DONE] · **B08 ch6 §7-11 [DONE]** ·
B09 ch7 §1-3 · B10 ch7 §4 · B11 ch8. Full page ranges in `book.json` -> `batches`.

## Open traps / environment

- Traditional OCR model only (`chi_tra` / `chi_tra_vert`), never `chi_sim`.
- Env is NOT installed in a fresh container. `apt-get install ... poppler-utils`
  404s and aborts the WHOLE transaction — install tesseract WITHOUT poppler
  (`apt-get install -y --no-install-recommends tesseract-ocr tesseract-ocr-chi-tra
  tesseract-ocr-chi-tra-vert`); render via PyMuPDF. `pip install pymupdf pillow numpy
  opencv-python-headless` install cleanly. PaddleOCR will NOT install; fall back to
  `chi_tra_vert` + eye-read and say so (check 1 substituted by the whole-batch eye-read).
- **XHTML entity trap:** note bodies are parsed as XML. Use numeric character references
  (`&#160;`, `&#215;`, `&#8212;`) — never HTML named entities (`&nbsp;`, `&times;`).
- NCL seal over central columns; crop-verify anything under it.
- Offset drift: no constant formula; read folios off the page.
- `OMP_THREAD_LIMIT=1` for tesseract; verify `pgrep -c tesseract` is 0 after.
- `find_figures.py` merges its manifest AND only catches halftone plates — eyeball for
  LINE ART, which it misses (B08's five plates were all found by eye, not the detector).
- **Parity is necessary but not sufficient** (it compares two files from the same
  bilingual): always recount lists against the scanned pages.
- **Appending vs new chapter:** ch6 was multi-batch (append). Ch7 is likewise multi-batch
  (B09 = §1-3, B10 = §4) — B09 CREATES `out/ch07_reading.md`; B10 APPENDS §4 to it, so
  ch07_reading.md must end with FOUR ordered `### Section` headings after B10.
- **check_numbers NOISE** (traditional idioms) now also strips: 千鈞一髮, 三緘其口,
  模稜兩可, 幾十, 光芒四射, 四射, 三番幾次, 一萬, 千里眼, 萬難.
- Carried-forward open items (unchanged unless noted):
  別動隊 provisional (ch1); 中央特務會議/中央特務總部/各省區特務部 provisional (ch2 plate);
  中心思想 "central conviction" provisional (ch4); 抄靶子 "stop-and-frisk" provisional (ch5);
  扛木梢/吊膀子/老門檻 slang provisional (ch6 §2); 反偵探 kept "counter-surveillance" (ch6 §3);
  廣生行 "Kwong Sang" gun-oil provisional; 麻力樹棍 "malacca baton" provisional (ch6 §4);
  圓光/關亡 provisional (ch6 §10). GPU: render "the GPU" (格伯武 = 格伯烏), reconcile in ch7.
- Source misprints recorded so far (all footnoted): 店務員→電務員 (folio 78),
  綠化鈷→氯化鈷 (folio 73). Watch for more.
