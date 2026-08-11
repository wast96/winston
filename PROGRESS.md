# PROGRESS — Scales and Claws of Shanghai (上海鱗爪, customs volume)

The running per-batch log. Write it as you go, not at the end. One section per
batch: what was translated (unit ids, PDF and printed ranges), which checks ran
and what they found, notes added (count and numbering), glossary rows added with
status, figures, and anything flagged for the read-through (uncertain readings,
contradictions with scholarship, choices you were unsure of).

## Setup / Survey (2026-08-10)

- Source: image-only PDF, 252 pages, of the 2019 Taipei reprint
  生活在民國的十里洋場：《上海鱗爪》（風俗篇）, Xinrui Wenchuang (Showwe),
  ed. Cai Dengshan, ISBN 978-957-8924-38-3, series 血歷史 140. It is a modern
  RESET (not a facsimile) of the 1933 Shanghai 上海鱗爪, split by the reprint
  into a customs volume; this PDF is that customs volume: author's preface plus
  167 short essays. Clean modern typesetting, Traditional Chinese, vertical
  right-to-left body text, horizontal running heads.
- setup.sh: ran clean; PaddleOCR absent as expected (dual-engine substitute is
  ocr_dual.py per its docstring); epubcheck 5.1.0 present at
  /tmp/epubcheck-5.1.0/epubcheck.jar; checker regression tests green.
- PDF bookmarks: 170, one per essay plus cover/導讀/序, spot-verified accurate
  against the scan (pdf pages, 1-based). Printed TOC (pdf 15-22) folios agree
  with bookmarks throughout the sample checked.
- Offset: printed = pdf - 2, CONSTANT front to back (verified at pdf 13, 23,
  120, 247; no plates, no second front-matter sequence). Body pdf 23-247 =
  printed 21-245. pdf 4, 14, 248, 249, 251 blank or filler; pdf 250 CIP;
  pdf 252 back cover.
- Page furniture (to configure in ocr_crop.py in B01): running head at top
  (recto: essay title, vertical, near-gutter; verso: series title, horizontal)
  plus printed folio as stacked digits in the top outer corner. Body block
  sits below; measure the crop box on B01's pages before OCR. Model
  chi_tra_vert, --psm 5.
- Standing decisions (survey gate, commissioner-approved 2026-08-10): (1) the
  2019 導讀 by Cai Dengshan is EXCLUDED (modern copyrighted text; noted in
  translator_note); (2) the reprint-added period photographs are INCLUDED per
  the commissioner's explicit instruction: run them through the figure
  pipeline per batch (crop from the scan, alt text, caption translating the
  reprint's label and stating provenance: photographs added by the 2019
  editor, not figures of the 1933 book); (3) reprint cover artwork excluded
  (builder generates a typographic cover, consistent with the shelf).
- book.json: metadata filled (series Winston Translations #10); complete
  structure, 168 chapters (ch000 = author's 1933 preface, signed 癸酉七夕
  天虛我生 = Chen Diexian; ch001-ch167 = the essays); 10 proposed batches.
- Skeleton EPUB built (out/scales-and-claws-of-shanghai.epub): qa_epub PASS
  (181 files, 174 documents, all links resolve); epubcheck 5.1.0: 0 errors,
  0 warnings.
- Branch consolidation per rule 2: canonical branch claude/scales-and-claws;
  stray harness branch claude/pdf-source-review-igkdaq carried no unique
  commits, deleted local and remote.
- B01 note: the batch's pdf_range [12,33] contains a gap — preface pdf 12-13,
  then blank pdf 14 and the printed TOC pdf 15-22, body resumes pdf 23. OCR
  only 12-13 and 23-33.

## B01 = ch000-ch001 (2026-08-11, voice gate PASSED)

Voice, note density and formatting approved by the commissioner; ch001 frozen
as the register reference. Commissioner asked for MORE notes going forward
(generous/dense annotation is the standing preference).


Scope: ch000 (序, Author's Preface, PDF 12-13 / printed 10-11) and ch001
(上海人的過年忙, The New Year Rush, PDF 23-33 / printed 21-31). PDF 14-22
(blank verso + printed TOC) skipped.

### Pipeline / OCR
- Page furniture measured: running head + stacked folio digits in the TOP
  band (mirrors L/R by page parity), body block below. Crop configured in
  ocr_crop.py: --left 0.03 --right 0.97 --top 0.13, --lang chi_tra_vert
  --psm 5. Bottom bound is PAGE-TYPE dependent (see below).
- Two page geometries: FULL-TEXT pages (13, 26-33) cropped --bottom 0.95;
  PHOTO pages (12, 23, 24, 25 — reprint photos occupy the lower ~45%)
  cropped --bottom ~0.51-0.56 so the photo band stays out of body OCR (it
  would otherwise wreck indent/paragraph detection). Ran in separate passes.
- Column order (vertical RTL) verified correct by eye against the assembled
  output on multiple pages. `pgrep -c tesseract` = 0 after every OCR run.
- OCR ENGINE CAVEAT (say-which-you-did): PaddleOCR unavailable; used
  tesseract chi_tra_vert --psm 5 only. tesseract is MEDIOCRE on this
  vertical-Traditional reset (~85% char accuracy, dense plausible-mangles:
  廟→講, 郁→克, 魑魅魍魎→往魅鬼手, etc.). ocr_dual.py was NOT run: it is
  hardwired to chi_sim + horizontal psm 6/4 (wrong script AND orientation
  for this book) and would emit noise, not a useful disagreement signal.
  Instead, being the reference batch, EVERY page was read by eye at
  magnification (that reading IS the crop-verification), and data/zh was
  produced as a full eye-transcription corrected against the scans.
- CROP-VERIFIED at magnification (data/ocr_fixes.json): the load-bearing
  opener number 一剎那已**二十四**年 (24, NOT 34 — a first-read error caught
  by the crop); 定鼎金陵; the preface signature 癸酉七夕天虛我生識於西湖息養社
  (dates the preface to 1933); 商輟於市、工輟於業 (輟); temple names
  城隍廟/南京路虹廟 (systematic 廟→講 mangle). Residual minor uncertainties
  (do-not-block): 不遑計及 (遑), 鑼鼓鐃鈸 (鐃) — sense unaffected.
- REPRODUCIBILITY NOTE: data/zh is .gitignored (copyright). Because the OCR
  is too error-dense for targeted-fix replay, data/ocr_fixes.json holds the
  crop-verified KEY readings as the audit trail, NOT a full reconstruction.
  A fresh checkout's auto-regenerated data/zh for B01 is NOT authoritative;
  the verified Chinese lives in the eye-transcription, and the tracked
  deliverables (out/*_reading.md, ledgers, pagemap, structure) are complete.

### Checks (all green)
- verify_unit ch000/ch001: parity 2/2 and 19/19, numbers unresolved 0/0
  (after fixes), anchors 7/18 resolve.
- check_numbers: 3 flags triaged — 萬事如意 (萬, idiom) and 百貨 (百, compound)
  added to data/noise.txt with reasons; 四毛 was rendered "forty cents"
  (40≠4), FIXED by rendering 毛 as the period unit *mao* (preserves the
  numeral, better scholarship) not by noising a real quantity.
- check_align: ch000 median 7.53, ch001 median 5.58 en/han, no pair strays.
- check_content (--config check_config.json): 0 displaced.
- qc_entities: ch000 0 misses, ch001 0 misses (entity census printed).
- check_structure: parity OK, 25 anchors resolve, heading shape OK.
- check_apparatus: 0 failures, 0 warnings.
- Build: qa_epub PASS (187 files, all links resolve, 25 refs/bodies/backlinks
  ordered); epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings.
- Tail verification (rule 4 corollary): ch001 closing paragraph (大魚大肉)
  re-read against PDF 33; ch000 signature against PDF 13. Faithful.
- check_register NOT run: B01 is the reference; it freezes on gate approval.

### Apparatus
- Notes: 25 total (ch000 = 7, ch001 = 18), numbered continuously book-wide by
  the builder (1-7, 8-25). Note-dense opener as briefed: calendar politics,
  New Year customs, money/shop practice, two classical allusions (Zhuangzi
  天地 / 卑之毋甚高論), Shanghai temples and institutions. Fact-checked against
  Wikipedia, Baidu Baike, ctext/Wikisource, Zdic and press (no LLM sources).
  Verdicts recorded IN the notes where relevant.
- Two honest UNCORROBORATED flags in the notes: (a) 《格言叢輯》's authorship
  and vogue rest only on the preface's own word — no independent record found;
  (b) ch001's internal dating ("twenty-four years"; "seven or eight years")
  points to ~1935-36, a little AHEAD of the collection's 1933 imprint —
  flagged as the author's loose reckoning; cannot collate against the 1933
  original (this is a 2019 reset).
- Glossary: 22 rows added (people 2, places 6, organizations 4, terms 10).
  Yu Muxia flagged principal:true (cast one-liner). Shelf-consistent
  renderings adopted from authority.json: 南京路 Nanjing Road, 南市 Nanshi,
  捕房 police station. New decided/provisional/attested renderings recorded.
- Figures: 5 reprint images cropped to data/figs/ (tracked) and specced in
  figures.json — ch000 shikumen archway (Ping'an Li); ch001 spring-couplets
  photo, a period LINE-DRAWING of year-end cleaning (揮簷塵, captioned as
  such), new-clothes photo, firecrackers photo. Each caption translates the
  reprint's label AND states provenance (2019 editor's addition, not a 1933
  figure). Placed thematically (couplets→open, cleaning→Cleaning,
  new-clothes→New Clothes, firecrackers→Firecrackers).

### Register / voice (frozen at gate approval)
- Preface: formal classical-period English (elevated but readable, not
  fake-Scripture). Chapter: 1930s newspaperman's miscellany — quick, worldly,
  amused, the author stepping in to editorialize. Subsection topic-labels set
  as ITALIC run-in leads (the builder supports *italic*→<i> only, not bold;
  #### subheads would break the heading-shape gate against ch000).

### Template fixes (do NOT revert; see HANDOFF do-not-revert list)
- scripts/check_content.py name_map: skip '_'-prefixed section/entry keys and
  non-dict values (crashed on the glossary's documented "_about" string).
- indents.py is HORIZONTAL-only (row-band line-start logic) and errors on
  this vertical book (missing ocr_crop.folio_present); NOT used. assemble.py
  ran on the blank-line signal; paragraph structure finalized by hand against
  the eye-reading. data/indent/ intentionally empty for this book.
- check_config.json (new, tracked): {docs,sources,notes,variants} for
  check_structure/check_content, filtered to BUILT units; regenerate as
  batches complete.
- data/noise.txt: added 萬事如意, 百貨 (with reasons).

### Known benign failure (recorded, not a regression)
- tests/run_tests.py: 9/10 green; the one FAIL is "hook stands down on
  template stub". That test restores the committed HANDOFF.md and expects the
  Stop hook to stand down — which only happens when HANDOFF is the untouched
  template placeholder (first line "(First line: ...)"). Our HANDOFF now
  carries a REAL kickoff, so the hook correctly enters its enforcing path.
  Template-only fixture assumption; the hook itself is working as designed.
