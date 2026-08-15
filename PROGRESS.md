# PROGRESS — Chen Yangshan: Hero of the Secret War (秘战英雄陈养山)

The running per-batch log. Written as work happens, not at the end.

## Setup / Survey (this session)

- **Book.** 秘战英雄陈养山, by 姚华飞 (Yao Huafei). CCP Party History Press
  (中共党史出版社), Beijing, 2018.4. ISBN 978-7-5098-4587-5. CIP subject:
  陈养山 (1906–1991), biography. 227,000 characters; 15 print sheets; 33.00 RMB.
  Biography volume of the 隐蔽战线春秋书系 (Hidden Front Chronicles) series.
- **Source.** Image-only PDF (`source.pdf`, 99 MB, 243 PDF pages), DuXiu/SuperStar
  digitisation via Anna's Archive. No text layer. PDF p243 is an Anna's Archive
  metadata leaf, NOT book content (reports 231 main book pages). PyMuPDF renders
  fine; no bookmarks (`get_toc()` empty), so structure was recovered from the
  printed TOC (目录, PDF p9–11) and verified opener-by-opener against the scan.
- **Script / orientation.** Modern SIMPLIFIED Chinese, single column, horizontal
  (left-to-right). Clean digital typeface — OCR will be easy (chi_sim, --psm 6).
  This is NOT an old letterpress scan; most of CLAUDE.md's furniture/orientation
  traps are mild here.
- **Offset.** printed = pdf − 11 for the whole body. Verified at printed 2
  (=PDF 13), 27 (=PDF 38), 231 (=PDF 242). Constant — no unpaginated plates in
  the body, so no offset drift.
- **Front matter runs a SECOND sequence.** Cover p1; series-title verso p2 (lists
  the 10-volume 传记卷 set); title page p3; CIP/copyright p4; frontispiece portrait
  of Chen (陈养山 1906–1991) p5; jacket blurb (内容提要) p6; **series foreword
  (丛书前言) by 章百家 (Zhang Baijia)** pp.7–8 on its OWN folio sequence
  (folios 1–2); TOC (目录) pp.9–11. Body (Chapter 1, printed 1) begins at PDF p12.
- **Page furniture.** Running head/foot with folio + running title present; exact
  top/bottom position appears to vary recto vs verso (verso title+folio seen at
  BOTTOM on p13; a running head seen at TOP on p242). MEASURE precisely in Batch 1
  per `ocr_crop.py` and strip textually after OCR. Chapter-opener rectos carry a
  PHOTOGRAPH above the heading (e.g. p38 = Chapter 2) — capture as figures per batch.
- **Structure.** 6 chapters / 29 sections; back matter = Appendix I 陈养山生平 (214),
  II 陈养山遗作 (217), III 陈养山年谱 (223), 参考文献 References (228), 后记
  Afterword (230–231). All folios verified. Full structure in `book.json`.
  TOC discrepancy flagged: the series foreword is not in the printed TOC
  (see `book.json` toc_flags_open).
- **Metadata (Step 0a).** Set in `book.json`; series "Winston Translations",
  index 10. `compose_style.py` run → STYLE.md (zh / nonfiction / popular
  narrative-history voice); STYLE.local.md seeded.
- **Skeleton EPUB.** `build_reading_epub.py` → out/chen-yangshan.epub (0/12
  translated). `qa_epub.py` PASS. **epubcheck 5.1.0: 0 errors / 0 warnings.**
- **Environment.** tesseract chi_sim + chi_tra (sim/trad, incl. vert) installed.
  PaddleOCR NOT installed (expected) → dual-engine substitute is `ocr_dual.py`.
  epubcheck present at /tmp/epubcheck-5.1.0/epubcheck.jar. Java via setup.
- **Branch.** All work consolidated on `claude/chen-yangshan` per commissioner
  and CLAUDE.md rule 2. Stray harness branch `claude/pdf-source-review-ieeufv`
  left untouched (not deleted).

### Cross-book connections to watch (from COLLECTION.md / authority.json)

This book sits in the shelf's core world (中央特科 / the hidden front). Consult
`authority.json` BEFORE romanising: 周恩来 Zhou Enlai, 顾顺章 Gu Shunzhang
(author of shelf book 2), 中央特科 Central Special Branch/Teke, 李克农 Li Kenong,
康生 Kang Sheng, 贺龙 He Long, 恽代英 Yun Daiying, 鲍君甫 Bao Junfu, 军统 (reconcile
the three-way drift noted in COLLECTION.md before use).

## B01 = Chapter 1 "Seeking the Truth, Turning to Revolution" (ch01s01–s05), PDF 12–37, printed 1–26

Status: translated, apparatus complete, EPUB built green; voice gate in progress.

### OCR / page geometry (measured this batch — DO NOT REVERT)
- **Crop.** `ocr_crop.py --lang chi_sim --psm 6 --left 0.045 --right 0.985
  --top 0.08 --running-head "秘战英雄陈养山"`, with a **recto/verso split bottom**:
  RECTO (PDF even) `--bottom 0.945`, VERSO (PDF odd) `--bottom 0.915`.
- **Mirrored furniture.** RECTO (printed odd) carries the running head + folio at
  the TOP (cut by top=0.08); VERSO (printed even) carries folio + book-title foot
  at the BOTTOM. The verso foot band (~0.925–0.953) overlaps recto body text
  (~0.94), so recto is cropped generous and the verso foot is excluded
  geometrically (bottom 0.915; body ends by ~0.910).
- **strip_runfoot patched** (do-not-revert) to remove the verso book-title foot
  textually as a backstop: exact title-tail match, plus any LAST line containing
  a `|` (the ▶ marker + decorative rules OCR as pipe noise; this book's body
  prose never contains `|`).
- **SILENT OCR-LOSS class found and worked around.** tesseract psm6/psm4/psm11 on
  the full page-crop DROP an isolated paragraph-final SHORT line (both at page
  bottom above the foot AND mid-page). Confirmed losses recovered from the scan:
  p13 "逐渐衰败，生活贫寒。" and p15 "为恐慌。". A psm11 cross-pass over the whole
  batch confirmed these were the ONLY two dropped tails. Lesson for later batches:
  a paragraph whose OCR ends without sentence-final punctuation before a blank is
  a dropped-tail suspect; verify against the scan. `data/zh/ch01.txt` was
  hand-assembled from the corrected OCR + scans for this reason (a third of the
  pages carry photos with text wrap, which the indent/assemble geometry cannot
  handle here — `ocr_crop.folio_present` is also absent, so indents.py is unused
  this book).
- ocr_dual.py second read run (psm4 vs psm6); crop-verified readings recorded in
  `data/ocr_fixes_notes.md` (military-commission names, Chen Geng, the Zhou poem,
  the Longhua martyr, classical Cao E names).

### Figures (10; eyeballed every page — find_figures MISSED p16, false-negative on
line-thin calligraphy p18)
- p12/p19 portrait (same photo; placed ONCE, at the p19 clerk-portrait context,
  caption "…Hankou, 1924"); p16 《中国青年》; p17 Yun Daiying; p18 Zhou Enlai's
  1953 calligraphy of Yun's prison poem (hand-cropped; also rendered as {p} verse
  in the body); p24 Ren Bishi; p29 Shanghai Bund (source prose caption); p31 Wang
  Yifei; p32 Chen in Ningbo; p33 April-12 massacre (source prose caption); p34
  He Long. All with real `alt`. Source photo captions translated into figures.json;
  they are NOT body paragraphs (excluded from data/zh, so parity stays 1:1).

### Translation & apparatus
- `out/ch01_reading.md`: 141 body paragraphs + 5 section headings, one paragraph
  per source line. Block quotes as `{v}`; the prison poem as `{p}` verse.
- notes.json: 23 footnotes (reader = Westerner, no China background): geography,
  jinshi, 曹娥/水经注, 实业救国, May Fourth, 二七/li, 中国青年, Youth League,
  Ren Bishi, Lenin issue, 楚囚 allusion + poem-variant, May Thirtieth /
  International Settlement / SMC / McEuen, Northern Expedition, April 12 / white
  terror, Nanchang Uprising, silver dollars, Green Gang, Central Special Branch,
  Gu Shunzhang. Continuous, all anchors verbatim.
- glossary.json: 41 rows in sections people/organizations/places/events; 3
  principals (Chen, Yun, He Long) → Principal Characters front page. Reused
  authority.json agreed forms (He Long, Zhou Enlai, Chiang Kai-shek, Kuomintang,
  Central Special Branch, Wuhan/Hankou/Shanghai, Northern Expedition, etc.).

### Checks (all green)
- check_numbers --noise: **0 unresolved** (141 pairs). Real drops fixed to carry
  the value (三人, 6时, 3时45分, and large counts written as digits 200,000/50,000/
  250,000/100,000). Noise added for idioms/names/date-labels (三罢, 万岁, 百官,
  百姓, 李立三, 九江, 矢田七太郎, 四出, 一分为二, 二话, 百年, 四一二, and the
  X多万 magnitude approximations with English rendering noted).
- parity 141=141; anchors 23 ok; qc_entities 0 misses (census: 陈养山×131 …);
  check_content OK (281 name occurrences all in the paired paragraph);
  check_apparatus 0/0.
- **check_align: 1 expected flag** — pair 33, poem line 2 (故人生死各千秋。, 7
  hanzi) expands ~10x in English. High ratio = expansion, not missing text; a
  legitimate verse exception, not a defect.
- Build: qa_epub PASS; **epubcheck 5.1.0 = 0 errors / 0 warnings.**

### Tooling patches (do-not-revert)
- `ocr_crop.strip_runfoot`: verso book-title / pipe-foot removal (above).
- `apparatus_merge.py`: glossary now merges into SECTIONS (`"section"` field on a
  row, default terms) instead of flat top-level keys — the flat form crashed the
  builder's render_glossary and made qc_entities vacuous.
- `check_content.name_map`: skip `_`-prefixed metadata keys (e.g. `_about`),
  which are strings, not sections.

### Register reference
On voice-gate approval, ch01 becomes the FROZEN register reference
(`check_register.py --ref out/ch01_reading.md` for every later batch).

### Voice gate (Step 0c)
- **Blind-critique loop complete: 3 rounds, converging 30 -> 24 -> 14 findings**
  (round 3: "largely clean, reads as fluent English"). Each round: a fully
  context-blind FRESH reader (no source, no STYLE, no project) via
  voice_gate_critique.py; all fixes applied and re-verified against the source;
  all gates re-run green after each round. STYLE.local.md evolved with 8
  RULE/WHY/FIX/CHECK entries (heroic-formula rationing, 成语-as-calque,
  water/storm imagery, editorial-adjective/coinage, fronted-inversion, classical-
  tag framing, impression-formula + metaphor budget, no clefts/antique
  light-verbs) + a 7-item word-level ledger. Archived under review/voice_gate/.
  NEXT: human voice/notes/formatting gate, then freeze ch01 as register reference.
- Regression note: setup.sh "CHECKER REGRESSION TESTS FAILED" is a benign
  artifact — the kickoff_guard template-stand-down fixture expects a placeholder
  HANDOFF.md, but ours is a real book handoff, so the hook correctly refuses to
  stand down. All translation checkers (check_numbers, builder, compose_style)
  pass.
