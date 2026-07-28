# HANDOFF — 特務工作之理論與實際 (Gu Shunzhang)

This file is the baton. A fresh instance with no memory of prior sessions
should read it and start immediately. Rewrite it at the end of every batch, and
always keep the paste-ready message below as its first section.

## Message to paste into the next chat

```
Read gu-shunzhang/CLAUDE.md in full (note the standing rules at the top), then gu-shunzhang/HANDOFF.md, then gu-shunzhang/book.json. Work only on the claude/gu-shunzhang branch; if the session starts you on some other branch, move your work onto claude/gu-shunzhang and drop the stray branch. Then do Batch B08 = Chapter 6 §7-11 (特務技術 continued: 第七節 密語術 Secret Signals and Codes, 第八節 觀察技能 Observation Skills, 第九節 形相術 Physiognomy, 第十節 催眠術 Hypnotism, 第十一節 攝影術 Photography) — PDF pages 176-219, printed folios 144-177, unit ids ch06s07 to ch06s11 — end to end: install the environment (tesseract-ocr chi_tra + chi_tra_vert, pymupdf, pillow, numpy, AND opencv-python-headless — apt WITHOUT poppler-utils, it 404s and aborts the whole apt run; PaddleOCR will not install, so fall back to chi_tra_vert + eye-read and say so), render, OCR with the already-measured crop (scripts/ocr_crop.py, chi_tra_vert --psm 5, OMP_THREAD_LIMIT=1, verify pgrep -c tesseract is 0 after), then read every one of the ~44 pages off the 300 dpi scan by eye and translate to the register in CLAUDE.md. NOTE the batch boundary: B07 already translated §6 (談話術) through folio 143 AND the one spill-over sentence at the TOP of folio 144 (PDF 176) that completes §6 ("…不要用情感和威力來強迫對方的服從。"); §7 密語術 opens right below that on folio 144. Render 176 and start at 第七節, do NOT re-translate the §6 tail. These sections carry diagrams and plates more than any others so far — 形相術 (physiognomy) and 觀察技能 (observation) may carry face/feature line drawings, 催眠術 (hypnotism) may carry figures, 攝影術 (photography) will likely carry photographic plates and apparatus diagrams — so run find_figures.py 176 219 (it merges its manifest, needs opencv); its ink-density detector catches halftone plates but MISSES line diagrams (the ch6 street-tailing figure and the physiognomy charts must be eyeballed), so scan every page for line art by eye and crop by hand if needed; caption any vertical caption zone with chi_tra_vert; add specs to figures.json under ch06 and never invent an identification. Confirm book.json's toc_flags_open remaining sub-bullets: Observation item 5, and Hypnotism item 7 (催眠與暗示); confirmed already are Observation item 1 = 觀察技能在特務工作上的作用 and Hypnotism item 5 = 被術者的體質 (the four temperaments). Update book.json if the bookmarks and the body disagree. Author one aligned out/ch06s07-11_bilingual.md, generate the reading text and parity source with scripts/split_bilingual.py, then run scripts/check_numbers.py and scripts/check_structure.py; do blind double-translation and back-translation on the argumentative passages and a full completeness recount of every list against the pages (these sections are list-heavy). IMPORTANT: ch6 is a multi-batch chapter — APPEND §7-11 to the existing out/ch06_reading.md (do not overwrite §1-6); the builder deep-links sections in book.json order by counting the '### ' headings, so ch06_reading.md must end up with §1-11 as ELEVEN '### Section' headings in order. Add footnotes to notes.json keyed "ch06" (continuous numbering follows automatically, picking up from 125) and extend glossary.json with attestation. Rebuild out/gushunzhang.epub, run scripts/qa_epub.py out/gushunzhang.epub until it passes, then commit to claude/gu-shunzhang and present out/gushunzhang.epub to me directly as an attached file in this chat (not via a git link). Finally rewrite HANDOFF.md to launch Batch B09 (Chapter 7 §1-3). Cite printed folios, never PDF pages; the offset drifts (~pdf−32 at folio 107, ~pdf−34 by folio 149, ~pdf−42 by folio 173) — READ the folio at each section opener and re-verify. Never invent bridging text (crop the scan and read the continuation). One build-trap to remember: note bodies are XHTML, so use numeric character refs (&#160;, &#215;), never HTML named entities (&nbsp;, &times;) — they break the notes page. Don't pause for my approval; run the whole batch and report back when the batch is built and QA-green.
```

## What is DONE (do not redo)

- **B01 = Chapter 1 (緒論)** — complete, QA-green. `ch01`, 25 notes.
- **B02 = Chapter 2 (特務組織)** — complete, QA-green. `ch02`, 19 notes (26-44),
  13 glossary rows, 4 figures.
- **B03 = Chapter 3 (特務工作的方法)** — complete, QA-green. `ch03`, 9 notes (45-53).
- **B04 = Chapter 4 (特務觀念)** — complete, QA-green. `ch04`, 9 notes (54-62).
- **B05 = Chapter 5 (秘密)** — complete, QA-green. `ch05`, 23 notes (63-85),
  13 glossary rows, no figures.
- **B06 = Chapter 6 §1-3 (化裝術/釘梢術/反偵探)** — complete, QA-green.
  `ch06` notes 86-108 (23), 9 glossary rows, 1 figure (street-shadowing diagram).
- **B07 = Chapter 6 §4-6 (Weapons / Sabotage / Conversation)** — complete,
  QA-green. `out/ch06_reading.md` now has §1-6 as six ordered `### Section`
  headings. `notes.json` `ch06` **+16 (109-124)**, 9 glossary rows, **no figures**
  (none in range). Covers **folios 107-118 (§4) and 137-143 (§6)**.
  **§5 (破壞術, Sabotage): non-operational DOCTRINE included, construction core
  WITHHELD** — see the safety note below.
- `out/gushunzhang.epub` now carries **6 of 8 chapters, 124 notes, 12 spine
  files, 1 figure**; `qa_epub.py out/gushunzhang.epub` PASSES. Chapter 6 shows in
  the TOC with §1-6 deep-linked and §7-11 pending.

## SAFETY — §5 construction core is WITHHELD (STANDING; do not "complete" it)

The device-construction material must never be read closely or reproduced. Current
state after B07 + its addendum:
- **§5 破壞術 (folios 119-136 / PDF 151-168): the NON-OPERATIONAL DOCTRINE is now
  translated and in the edition** — §I rationale, §II political forms + the four
  modes (written/verbal/chemical/mechanical), §III the wrecking-cell organization.
  It was rendered from OCR of **only** folios 119-120 and 134-136; the recipe zone
  (folios 121-133) was **never read**. The passages are flagged in-text as more
  provisional than the rest, and are outside the number/parity checks.
- **The technical core — device construction, charging, emplacement — remains
  WITHHELD**, marked in `ch06_reading.md` by an editorial bracket inside §II. Do
  NOT read folios 121-133 or the §4 bomb tail; do NOT "complete" §5 as how-to.
- The `### Section 5` heading MUST stay (builder numbering: ch06s05 → ch06s06).
- The explosive/munition tail of §4 (folio 118 and the gas-gun cartridge internals
  on folio 117) is likewise omitted, marked by a footnote in §4.
- Optional future work, doctrine-only: §5's included passages could be given the
  full eye-read + number-check the other sections got, to lift them out of
  "provisional" — the SAME non-operational scope, construction still withheld.
- If Winston asks for more of §5, give only strictly non-operational content
  (doctrine, targets, organization), never construction, and confirm scope first.

## Your job next session: Batch B08 = Chapter 6 §7-11

- **Scope:** ch06 §7-11, unit ids ch06s07-ch06s11. **PDF 176-219 = printed folios
  144-177** (~44 pages).
  - §7 密語術 — Secret Signals and Codes — PDF 176 / folio 144 (opens partway down
    144, after §6's one spill-over sentence at the top — already translated in B07)
  - §8 觀察技能 — Observation Skills — PDF 183 / folio 149
  - §9 形相術 — Physiognomy — PDF 193 / folio 159
  - §10 催眠術 — Hypnotism — PDF 207 / folio 165
  - §11 攝影術 — Photography — PDF 215 / folio 173
- **Offset drifts** (~pdf−32 at folio 107, ~pdf−34 by 149, ~pdf−42 by 173): READ
  the folio at each opener.
- **Figures very likely** in this batch (physiognomy face charts, hypnotism,
  photographic plates and apparatus). `find_figures.py` catches halftone plates
  but MISSES line diagrams — eyeball every page. Add to `figures.json: ch06`;
  never invent an identification.
- **book.json `toc_flags_open`:** confirm Observation item 5 and Hypnotism item 7
  (催眠與暗示) against the body; update book.json.
- After B08, `out/ch06_reading.md` must end with §1-11 as **eleven** ordered
  `### Section` headings.

## The 11-batch plan (from Winston)

B01 ch1 [DONE] · B02 ch2 [DONE] · B03 ch3 [DONE] · B04 ch4 [DONE] ·
B05 ch5 [DONE] · B06 ch6 §1-3 [DONE] · **B07 ch6 §4-6 [DONE]** · B08 ch6 §7-11 ·
B09 ch7 §1-3 · B10 ch7 §4 · B11 ch8. Full page ranges in `book.json` -> `batches`.

## Open traps / environment

- Traditional OCR model only (`chi_tra` / `chi_tra_vert`), never `chi_sim`.
- Env is NOT installed in a fresh container. `apt-get install ... poppler-utils`
  404s and aborts the WHOLE transaction — install tesseract WITHOUT poppler
  (`apt-get install -y --no-install-recommends tesseract-ocr tesseract-ocr-chi-tra
  tesseract-ocr-chi-tra-vert`); render via PyMuPDF. `pip install pymupdf pillow
  numpy opencv-python-headless` install cleanly. PaddleOCR will NOT install;
  fall back to `chi_tra_vert` + eye-read and say so (dual-engine OCR diff, check 1,
  cannot run — substitute the whole-batch eye-read, as B05/B06/B07 did).
- **XHTML entity trap (new, cost a failed build in B07):** note bodies are parsed
  as XML. Use numeric character references (`&#160;`, `&#215;`, `&#8212;`) — never
  HTML named entities (`&nbsp;`, `&times;`), which are undefined and make the whole
  notes.xhtml unparseable, cascading to "missing anchor" on every note.
- NCL seal over central columns; crop-verify anything under it.
- Offset drift: no constant formula; read folios off the page.
- `OMP_THREAD_LIMIT=1` for tesseract; orphaned children spin after a kill
  (verify `pgrep -c tesseract` is 0).
- `find_figures.py` merges its manifest AND only catches halftone plates —
  eyeball for LINE ART, which it misses.
- **Parity is necessary but not sufficient** (it compares two files from the same
  bilingual): always recount lists against the scanned pages.
- **ch6 is multi-batch:** APPEND to `out/ch06_reading.md`; never overwrite earlier
  sections. Eleven ordered `### Section` headings must end up in the file so the
  builder's per-section deep-linking stays correct.
- **check_numbers.py NOISE** now also strips 千鈞一髮, 三緘其口, 模稜兩可, and its
  `十[几分步]` rule was narrowed to `十[几分]` (so 三十步 / 二十步 stay checkable).
- Carried-forward open items (unchanged unless noted):
  別動隊 provisional (ch1); the ch7 GPU spelling 格伯烏 to reconcile with ch1's
  格伯武; 中央特務會議/中央特務總部/各省區特務部 provisional (ch2 plate);
  中心思想 "central conviction" provisional (ch4); 抄靶子 "stop-and-frisk"
  provisional (ch5); 扛木梢 slang provisional (ch6 §2); 反偵探 kept as
  "counter-surveillance" (ch6 §3). NEW from B07: **廣生行 "Kwong Sang" gun-oil**
  is almost certainly the famous cosmetics house — the gun-oil trade is
  uncorroborated, rendering provisional; **麻力樹棍 "malacca baton"** provisional
  (麻力 read as a transliteration of "malacca").
- Source misprints recorded so far (all footnoted): 店務員→電務員 (folio 78),
  綠化鈷→氯化鈷 (folio 73). Watch for more.
