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

## B02 = ch002-ch014 (2026-08-11)

Scope: ch002 (宋案的回顧) through ch014 (跳舞), PDF 34-58 / printed 32-56.
Thirteen essays, the "press and politics" cluster: the Song Jiaoren case, Dai
Jitao, Zhang Taiyan, Kang Youwei, the revolutionary papers, Zhou Hao, Xue
Dake, the magazines, the evening papers, Culture Street, the new drama, and
the dance halls.

### Pipeline / OCR
- render 34-58 --dpi 300; ocr_crop 34-58 --left 0.03 --right 0.97 --top 0.13
  --bottom 0.95 --lang chi_tra_vert --psm 5 as a ROUGH scaffold only.
  pgrep -c tesseract = 0 after the run.
- As in B01, tesseract on this vertical-Traditional reset is ~85% and too
  error-dense to trust; every page was EYE-READ at magnification and data/zh
  hand-transcribed against the scans. Paragraph structure finalized by hand,
  cross-checked against the OCR blank-line signal (short-line judgment at the
  page seams where the blank falls off the page; confirmed every break).
- Crop-verified load-bearing readings recorded in data/ocr_fixes.json: the
  Song-case telegram phrase 毀宋酬勳; Song's age 三十有二; Hong's 電氣絞刑;
  the crossed sobriquets on printed p40 (岑西林/黎黃陂, see below); the
  Minquan Bao staff names (牛霹生, 蔣箸超, 吳雙熱); 薛大可; 砉然; the dance
  price 三角三分. Verified against magnified column crops (scratch_crops/).

### Figures (13, all reprint-added, provenance stated in every caption)
- ch002: four portraits from PDF 34-35 (宋教仁 Song Jiaoren, 應桂馨 Ying
  Guixin, 洪述祖 Hong Shuzu, 趙秉鈞 Zhao Bingjun), placed at paragraph
  openings across the chapter.
- ch003 戴季陶; ch005 章太炎; ch006 康有為 (portraits).
- ch010: three magazine covers (《禮拜六》Libai Liu, 韜奮的《生活》Shenghuo,
  邵洵美的《十日談》Shiritan/Decameron), one per paragraph P2-P4.
- ch012 老上海福州路書店 (street photo); ch013 the 春柳社 Camille cartoon
  and 鄭正秋 portrait.
- Photos cropped to data/figs/ (tracked); each caption translates the
  reprint's own label AND states the 2019-editor provenance. NOTE:
  find_figures.py NOT used (it misses line art / false-positives dense text);
  every page eyeballed by hand.

### Checks (all green)
- verify_unit (parity + numbers) ch002-ch014: parity OK on all
  (6/1/2/2/4/2/3/2/4/4/3/6/3 paragraphs); numbers unresolved 0 after noise.
- check_numbers noise added (data/noise.txt, with per-entry reasons):
  十六開/四開/八開 (paper formats), 禮拜六 (the "Saturday" magazine title),
  九一八/一二八 (event dates carried as month-day), 瞎七搭八 (idiom), the
  weekday run 星期一、二、三、四、五, 萬丈深淵 (idiom). REAL quantities were
  carried in the English instead of noised: 十萬元 -> "one hundred thousand
  dollars"; 一百多種 -> "one hundred titles and more"; 兩字 -> "two-character
  pen name"; 兩報 -> "both the Shenbao and the Xinwenbao".
- check_align: all 13 units within 2.2x of the unit median, no stray pair.
- check_content (check_config.json, ch002-ch014): 0 displaced.
- qc_entities: 0 misses on every unit (entity census printed per unit).
- check_structure: parity OK, 93 note anchors resolve (118 book-wide), 0
  unresolved, heading shape OK.
- check_apparatus: 0 failures, 0 warnings.
- Build: qa_epub PASS (200 files, 175 documents, 118 refs/bodies/backlinks
  ordered, 13 pagebreaks); epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings.
- check_register --ref out/ch001_reading.md: all 13 units within tolerance.
- Tail verification (rule 4 corollary): ch002 (膽識俱優 / p37), ch006
  (好惡不同了 / p42), ch013 (不堪回首之感 / p56), ch014 (不可救藥 / p58)
  re-read against the scans. Faithful.

### Apparatus
- Notes: 93 added this batch (book-wide 26-118), numbered by the builder.
  Dense per the commissioner's standing "go crazy" instruction: who each
  person/paper/office/party/event was, texture lost in translation (idioms,
  allusions, the "spring-palace" and "pheasant" slang), and the author as
  interested witness. Every historical claim fact-checked against Wikipedia
  (EN/ZH), Baidu Baike and academic/reference sources (NO LLM-written sites);
  verdicts stated IN the notes.
- Glossary: 25 rows added (11 people, 3 places, 7 organizations/papers, 4
  terms), merged into the SECTIONED glossary. Reused unchanged from B01:
  南京路 (ch009,013), 捕房 (ch003, via 總巡捕房). authority.json feed-back is
  deferred to book completion (Definition of Done) per the cross-book shelf
  convention; decided renderings live in glossary.json meanwhile.
- FACT-CHECK FLAGS recorded in the notes (honest apparatus):
  * ch002 Song "declined" the Agriculture-Forestry post: CONTRADICTED. He
    took it (Apr 1912) and resigned (Jul 1912); the book conflates this with
    his later refusal of Yuan's bribes. Rendered as printed, footnoted.
  * ch002 age 三十有二 = 32 by Chinese count, 30 Western. Footnoted.
  * ch002 電氣絞刑: UNCORROBORATED embellishment. Hong Shuzu was hanged
    (5 Apr 1919), the drop famously botched. Rendered as printed, footnoted.
  * ch002 telegram phrases 毀宋酬勳 / 梁山: CORROBORATED as real case
    evidence. Zhao/Ying/Wu deaths CORROBORATED (Zhao poisoning is the
    traditional allegation, one revisionist stroke view noted).
  * ch005 光緒三十二年 (1906) for the Subao case: WRONG. The case broke in
    1903 (Guangxu 29); 1906 is when Zhang was released. Footnoted. Also the
    Subao's actual editor was Zhang Shizhao, not Zhang Taiyan (footnoted).
  * ch006 crossed sobriquets 黎元洪之稱岑西林 / 岑春煊之稱黎黃陂: SOURCE
    ERROR (Li Yuanhong was 黎黃陂, Cen Chunxuan 岑西林). Rendered as printed,
    footnoted.
  * ch006 《國是報》: UNCORROBORATED. Kang's documented 1913 Shanghai organ
    was 《不忍》(Buren); the Guoshi Bao attribution is unverified, possibly a
    confusion. Footnoted honestly.
  * ch006 傀儡國 (Manchukuo, 1932) dates the sketch to 1932+; ch010's "Year
    of the Magazine" and internal reckonings point to composition ~1934-35,
    a few years past the 1933 imprint (same internal-dating gap flagged in
    B01; unresolved, cannot collate against a 1933 original in this reset).
  * ch009 Xue Dake as one of "洪憲六君子": the canonical Six were the
    Chouan Society (Yang Du et al.); Xue was the press propagandist, not
    usually counted among them. Clarified in the note.

### Tooling fixes (do NOT revert; added to HANDOFF do-not-revert list)
- scripts/apparatus_merge.py PATCHED: glossary merge is now SECTION-AWARE.
  It routes each batch glossary row into people/places/organizations/terms
  (a row's optional "section" field, default "terms"), treats a zh already
  present in ANY section as already-present, and preserves the flat behavior
  for an un-sectioned ledger. The old flat merge shelved rows at the top
  level and CRASHED the builder's render_glossary. (B02 rows were moved into
  sections by hand after the fact; B03+ can pass a sectioned batch glossary.)
- Note bodies are inserted RAW (not escaped): a bare "&" breaks the notes
  XHTML (it slipped past apparatus_merge's named-entity guard and produced a
  fatal epubcheck parse error, dropping every later note body). Fixed
  "S. Moutrie & Co." -> "S. Moutrie &#38; Co." Use &#38; for a literal
  ampersand in any note/glossary body.
- Figure "before" anchors MUST fall in the first ~80 chars of the target
  paragraph (the builder inserts the figure before that paragraph); five
  B02 specs were repointed to paragraph openings.
- check_config.json REGENERATED to ch002-ch014 only: ch000/ch001 data/zh is
  gitignored and not regenerable in a fresh container (B01 reproducibility
  note), so check_structure/check_content cover the batch's units; the
  builder still refuses any unmatched anchor book-wide as the backstop.

### Register / voice
- Held to the frozen ch001 reference. The grave political-history essays
  (ch002-ch009) keep the newspaperman's quick, worldly, editorializing voice
  without slipping into academic distance; the author's own asides (the dog
  cartoon, "trading on his years", the "blot on Culture Street", the dance-
  hall moral) rendered in his amused register.

### NOT re-noted this batch (already placed; cross-referenced instead)
- 袁世凱 Yuan Shikai: full note at ch002 (Glossary); later chapters use the
  short "Yuan". 民立報/民權報/天鐸報: IDed at ch002 (four-paper note +
  Glossary), not re-noted at ch003/ch007/ch008. Zhou Hao: note at ch002,
  his own chapter (ch008) adds only new detail (the Su-style calligraphy).
  南京路, 捕房/巡捕房: B01 notes stand; not re-noted.
- Deferred to their own later chapters (NOT noted here): 野雞 as a standalone
  (ch043 野雞大學, ch093 野雞) gets its full glossary decision there; here only
  a first-appearance footnote at ch012. 舞女 rendered "dance-girl"
  consistently; glossary decision deferred.
