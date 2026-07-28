# HANDOFF — 特務工作之理論與實際 (Gu Shunzhang)

This file is the baton. A fresh instance with no memory of prior sessions should read it and
start immediately. Rewrite it at the end of every batch, and always keep the paste-ready message
below as its first section.

## Message to paste into the next chat

```
Read gu-shunzhang/CLAUDE.md in full (note the standing rules at the top), then gu-shunzhang/HANDOFF.md, then gu-shunzhang/book.json. Work only on the claude/gu-shunzhang branch; if the session starts you on some other branch, move your work onto claude/gu-shunzhang and drop the stray branch. Then do Batch B11 = Chapter 8, 第八章 特務人員的修養的問題 (The Self-Cultivation of Secret-Service Personnel) — §1 工作的精神 (The Spirit of the Work) and §2 身心的鍛練 (Cultivation of Body and Mind), PDF 282-292, printed folios 228-236, unit ids ch08s01 and ch08s02 — THE LAST CONTENT BATCH — end to end: install the environment (tesseract-ocr chi_tra + chi_tra_vert, pymupdf, pillow, numpy, AND opencv-python-headless — apt WITHOUT poppler-utils, it 404s and aborts the whole apt run; PaddleOCR will not install, so fall back to chi_tra_vert + eye-read and say so), render, OCR with the already-measured crop (scripts/ocr_crop.py, chi_tra_vert --psm 5, OMP_THREAD_LIMIT=1, verify pgrep -c tesseract is 0 after), then read every one of the ~11 pages off the 300 dpi scan by eye and translate to the register in CLAUDE.md. Chapter 8 is a NEW chapter: create out/ch08_reading.md with an H2 (## Chapter 8. The Self-Cultivation of Secret-Service Personnel) and §1-§2 as two ordered "### Section" headings. Author one aligned out/ch08_bilingual.md (both sections), generate the reading text and parity source with scripts/split_bilingual.py (unit id ch08, zh-title "第八章 特務人員的修養的問題"), then run scripts/check_numbers.py out/ch08_bilingual.md and scripts/check_structure.py --pairs data/zh/ch08.txt out/ch08_reading.md. Run find_figures.py 282 292 (merges, needs opencv), but its ink-density detector MISSES line diagrams, so scan every page for line art by eye and crop by hand. Do blind double-translation and back-translation on the argumentative passages and fact-check names/dates against scholarship per check 7, and NEVER source Grok/Grokipedia. Add footnotes to notes.json keyed "ch08" (continuous numbering follows automatically, picking up from 202) and extend glossary.json with attestation. BECAUSE THIS IS THE LAST CONTENT BATCH, also do the final back-matter and a whole-book pass: (a) build the EPUB back matter — the 勘誤表 errata table (PDF 293) and the 版權頁 colophon (PDF 295: 中華民國二十二年八月 / August 1933, 不准翻印 "no reprinting") — as translator's back-matter pages, APPLYING any still-unapplied errata corrections to the affected folios and recording them; and (b) rebuild out/gushunzhang.epub with all 8 chapters + back matter + the full pending-aware TOC (now fully linked), run scripts/qa_epub.py until green, and re-run scripts/check_structure.py --config over every unit. Cite printed folios, never PDF pages; the offset is ~pdf−54 at folio 228 and more unpaginated plates may intervene — READ the folio at each section opener and re-verify (body text ends printed p236, confirmed by the errata's last entry). Never invent bridging text (crop the scan and read the continuation). Build-trap: note bodies are XHTML, so use numeric character refs (&#160;, &#215;), never HTML named entities (&nbsp;, &times;). Then commit to claude/gu-shunzhang, present out/gushunzhang.epub to me directly as an attached file in this chat (not via a git link), and — INSTEAD OF another handoff — write a COMPLETION REPORT: the whole book done, per-chapter note/figure/glossary tallies, every still-open provisional reading and every history flag gathered for my read-through, and a sampled error-rate estimate. Don't pause for my approval; run the whole batch and report back when the book is built and QA-green.
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
  complete, QA-green. `ch06` notes 125-146, 6 figures total.
- **B09 = Chapter 7 §1-3 (社會化問題 / C.P.特務工作 / 蘇聯特務工作)** — complete, QA-green.
  `out/ch07_reading.md` created; §1-3 as three ordered `### Section` headings. `ch07` notes 147-172,
  6 figures (`ch07-f1..f6`). Folios 178-205 (PDF 220-257).
- **B10 = Chapter 7 §4 (下層社會的研究 / The Study of Society's Lower Strata)** — complete, QA-green.
  `out/ch07_reading.md` now ends with §4 as the **fourth** ordered `### Section` heading (file = §1-§4).
  `ch07` notes **+29 (173-201)**, glossary **+19**, **2 figures** (`ch07-f7` the errata GPU-army chart,
  `ch07-f8` the kidnapping-gang org chart). Folios 206-227 (PDF 258-281). **Also restored §3's item f**,
  which B09 dropped (see B10 findings below).
- `out/gushunzhang.epub` now carries **7 of 8 chapters, 201 notes, 13 spine files, 18 figures**;
  `qa_epub.py out/gushunzhang.epub` PASSES (36 files, all links resolve). Chapters 1-7 fully done
  (ch7 §1-4 all linked); chapter 8 still pending in the TOC.

## SAFETY — §5 construction core is WITHHELD (STANDING; do not "complete" it)

The device-construction material of Chapter 6 §5 破壞術 (folios 119-136) must never be read closely
or reproduced: the non-operational doctrine is translated and in the edition; the technical core —
device construction, charging, emplacement — remains WITHHELD. Do NOT read folios 121-133, and do
NOT "complete" §5 as how-to. Chapter 8 is self-cultivation/morale and does not touch this.

## B10 — what the eight checks found (still-open items for the read-through)

- **Check 1 (dual-engine OCR diff) could not run** — PaddleOCR will not install here. Substituted
  the whole-batch eye-read (all 24 PDF pages read off the 300 dpi scan). Standing substitute.
- **Offset, verified:** pdf−52 at folio 206 (PDF 258); a **2-page plate insert** (PDF 259 = the
  errata GPU-army chart, PDF 260 = blank verso); body resumes PDF 261 = folio 207, offset **pdf−54**,
  holding to folio 227 (PDF 281). §4 ends at folio 227; ch8 opens folio 228. Every folio read off the scan.
- **B09 DROPPED §3's item f** (folio 206 top: the tail of "9. Activity abroad" — cover identities
  used abroad: pastors, engineers, journalists, foreign-national fronts, temporary "travel-party"
  outfits). It sits on B10's first page, past B09's PDF-257 cut. **RESTORED** in `out/ch07_reading.md`
  (appended to §3). Not re-fed to `data/zh/ch07s03.txt`; §3 parity not re-run. Winston may want to eyeball.
- **Figures: the ink-density detector caught 0** (both LINE ART). Cropped by hand: **f7** the errata
  plate 蘇聯 G.P.U 與軍隊的關係 (GPU penetrating the Red Army; anchored in §3, captioned as the
  errata's printed-206 insert), **f8** the kidnapping-gang org chart (領袖→墊本/{接洽·內守·外勤·線索}/書記).
- **數十八 is a source misprint** (folio 223, "每幫數十八或數百人"): scan-verified, does not parse;
  almost certainly 數十 ("some tens"). Rendered "some tens," footnoted (note 201), stripped in check_numbers.
- **Green Gang origin dating flagged:** the book's 明嘉靖十七年 (1538) for Patriarch Luo is NOT
  historical (Luo Qing d.1527; the boatmen's brotherhood dates to Yongzheng 1726). Footnoted as
  gang legend vs. scholarship. The 翁錢潘 patriarchs and 羅祖 origin are the gang's traditional account.
- **Three tycoons + 三鑫公司** (opium monopoly, 1918, ~⅓ of govt revenue) corroborated and footnoted.
  **嵊縣 kidnapping** flagged as an uncorroborated period commonplace.
- **Provisional readings:** 李則高 (fortune-teller boss), 癩頭筋鮑方 (flower-club king), 剝豬玀
  "pig-skinners," 洋盤 "foreign platter," the 彫林/三光碼子 police cant (譯音). Green Gang generation-poem
  variant (仁倫/與禮 vs standard 能仁/興理) footnoted.
- **Invariant checks PASS:** `check_numbers` 0 unresolved (56 pairs); `check_structure --pairs`
  parity 56/56. NOISE extended (see below). Double- and back-translation on the argumentative
  passages showed no material divergence and no omissions.

## Your job next session: Batch B11 = Chapter 8 (the LAST content batch)

- **Scope:** ch08, unit ids `ch08s01` (§1 工作的精神) and `ch08s02` (§2 身心的鍛練).
  **PDF 282-292 = printed folios 228-236** (~11 pages). §1 opener PDF 282 / folio 228.
- NEW chapter: **create** `out/ch08_reading.md` (H2 + two `### Section` headings). Notes continue
  from **202**. Offset ~pdf−54 at folio 228; read folios off the page.
- **Because it is the last content batch:** also build the **back matter** — errata table (PDF 293)
  and colophon (PDF 295) — as translator's pages, apply any still-unapplied errata to the affected
  folios, do a **whole-book QA pass**, and write a **COMPLETION REPORT instead of a handoff**.
- Body text ends printed p236 (confirmed by the errata's last entry).

## The 11-batch plan (from Winston)

B01 ch1 [DONE] · B02 ch2 [DONE] · B03 ch3 [DONE] · B04 ch4 [DONE] · B05 ch5 [DONE] ·
B06 ch6 §1-3 [DONE] · B07 ch6 §4-6 [DONE] · B08 ch6 §7-11 [DONE] · B09 ch7 §1-3 [DONE] ·
**B10 ch7 §4 [DONE]** · B11 ch8 [LAST]. Full page ranges in `book.json` -> `batches`.

## Open traps / environment

- Traditional OCR model only (`chi_tra` / `chi_tra_vert`), never `chi_sim`.
- Env is NOT installed in a fresh container. `apt-get install ... poppler-utils` 404s and aborts the
  WHOLE transaction — install tesseract WITHOUT poppler (`apt-get install -y --no-install-recommends
  tesseract-ocr tesseract-ocr-chi-tra tesseract-ocr-chi-tra-vert`); render via PyMuPDF.
  `pip install pymupdf pillow numpy opencv-python-headless` install cleanly. PaddleOCR will NOT install.
- **`find_figures.py` misses LINE ART.** It caught 0 of B09's 6 charts and 0 of B10's 2. Eyeball
  every page for line diagrams and crop by hand (small PIL fractional-box crop, re-viewed to verify).
- **Builder figure anchors match within the FIRST 80 chars of a paragraph** (`fig["before"] in line[:80]`).
  Put the anchor phrase at (or near) the start of its paragraph, or the figure silently won't place.
- **Unpaginated plate inserts break the offset.** B09 hit a 10-page block; B10 hit a 2-page plate
  (PDF 259-260). Expect more; read every folio off the page.
- **XHTML entity trap:** note bodies are parsed as XML. Use numeric character references
  (`&#160;`, `&#215;`, `&#8212;`) — never HTML named entities (`&nbsp;`, `&times;`).
- **Heredoc/CJK corruption:** when writing rare hanzi into JSON via a shell heredoc, some characters
  (嘯, 鑫, 鹹, 涇, 嵊, 悶, 玀, 揹) can silently mangle. Verify the written JSON by re-reading the hanzi,
  or write via a file rather than an inline heredoc.
- NCL seal over central columns; crop-verify anything under it. `OMP_THREAD_LIMIT=1` for tesseract;
  verify `pgrep -c tesseract` is 0 after.
- **Parity is necessary but not sufficient** — always recount lists against the scanned pages.
- **check_numbers NOISE** now also strips (B10): 數十八 (misprint), 四川, 四卡子橋, 黃楚九, 長三, 么二,
  零頭, 萬古千秋, 萬象, 數[十百千]; and "seventeenth"=17 added for regnal years (嘉靖十七年 = 1538).
  Carried from B09: 二則, 三則, 十幾, 萬計. Order in the NOISE list is load-bearing (longest first).
- Carried-forward provisional readings (unchanged): 別動隊 (ch1); 中央特務會議/總部/各省區特務部 (ch2 plate);
  中心思想 "central conviction" (ch4); 抄靶子 (ch5); 扛木梢/吊膀子/老門檻 (ch6 §2); 反偵探
  "counter-surveillance" (ch6 §3); 廣生行 "Kwong Sang"; 麻力樹棍 "malacca baton" (ch6 §4); 圓光/關亡 (ch6 §10);
  敏捷飛 "Minjie Fei" / 信誼代辦所 "Xinyi agency" / 紅色保衛隊 "Red Defense Corps" (ch7 §1-3);
  李則高 / 癩頭筋鮑方 / 剝豬玀 / 洋盤 / 彫林·三光碼子 (ch7 §4).
- Source misprints recorded so far (all footnoted): 店務員→電務員 (folio 78), 綠化鈷→氯化鈷 (folio 73),
  數十八→數十 (folio 223). The errata table (PDF 293) is still to be applied fully in B11 to any
  affected ch8 folio and rendered as back matter.
