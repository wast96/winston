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

## B03 = ch015-ch034 (2026-08-12)

Scope: ch015 (肉林秘聞) through ch034 (女相士), PDF 59-83 / printed 57-81.
Twenty essays, the Shanghai demimonde cluster: the courtesan houses and their
grades, brothel slang and catchphrases, foot-fetish and male-prostitution
curiosities, hotel and street trades, the flower-smoke opium dens, a
courtesan beauty-pageant, and the woman physiognomists.

### Pipeline / OCR
- render 59-83 --dpi 300; ocr_crop 59-83 --left 0.03 --right 0.97 --top 0.13
  --bottom 0.95 --lang chi_tra_vert --psm 5 as a ROUGH scaffold only.
  pgrep -c tesseract = 0 after the run (verified twice).
- As in B01/B02, tesseract on this vertical-Traditional reset is ~85% and too
  error-dense to trust; EVERY page was eye-read at magnification and data/zh
  hand-transcribed against the scans. Paragraph structure finalized by hand on
  the blank-line signal, confirmed at the page seams by the short-line signal.
- Column-order (vertical RTL) verified by eye on every page.
- FIGURES: none. Every page 59-83 eyeballed; this text-only demimonde cluster
  carries NO reprint-added photographs (unlike the portrait-heavy B01/B02
  pages). Empty figure list recorded as a deliberate decision.
- Offset confirmed printed = pdf - 2 at every opener (folios 057-081 read off
  the scans).

### Crop / reading verifications (rule 4 corollary + names/numbers)
- ch015: 榻 in 俯伏[榻]上 crop-verified on p59 (col. 8): the reprint PRINTS 楊
  (a poplar), plainly a misprint for 榻 'couch'; rendered to sense ("couch")
  and flagged here (2019 reset, no 1933 collation source). 辜鴻銘 Gu Hongming,
  漕涇 Caojing crop-read.
- Tail-verified against the scans: ch015 close (辜鴻銘/別具風味, p60), ch027
  close (自願作賤...不多罷, p73), ch031 close (提高其「肉」價, p78), ch033
  close (特別標幟, p81), ch034 close (快點去領教罷, p83). Faithful.
- Numbers carried, not noised: all prices/rates rendered in period money
  (叫局兩元, 夜廂六元/八元, 相金兩元, 一元二角, 小洋二毛銅元十枚, etc.).

### Checks (all green)
- verify_unit ch015-ch034: parity OK on all 20
  (3/2/2/2/3/2/2/2/2/2/1/2/4/2/1/3/5/3/5/4 paragraphs); numbers unresolved 0
  after noise; 93 note anchors resolve (0 unresolved).
- check_numbers noise added (data/noise.txt, reasons in-file): 北四川路 (四
  romanized in Sichuan), 十八、九 (elided "eighteen or nineteen"), 長三 /
  么二 / 老六 (courtesan-house names with the numeral romanized). REAL
  quantities all carried in the English.
- check_align: all 20 within 2.2x of the unit median, no stray pair.
- check_content (check_config.json): 0 displaced.
- qc_entities: 0 misses on every unit after fixing ch032 P1 (added "keeper"
  so 包客's rendering is present in the introducing paragraph).
- check_structure: parity OK, 93 anchors resolve, heading shape OK.
- check_apparatus: 0 failures, 0 warnings.
- Build: qa_epub PASS (200 files, 175 documents, 211 refs/bodies/backlinks
  ordered); epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings.
- check_register --ref out/ch001_reading.md: every unit within tolerance
  (all flagged "little dialogue - noisy": each essay is short, under the
  ~1200 speech-word bar, exactly as B02's essays were).

### Apparatus
- Notes: 93 added this batch (book-wide 119-211), numbered by the builder.
  Dense per the commissioner's standing preference: the house-grade system,
  brothel jargon and slang glossed at first appearance, classical allusions
  (金屋藏嬌, 完璧歸趙, 斷袖, 禁臠, 二八, 執牛耳), material/social culture
  (三寸金蓮 bound feet, 姨太太 concubine, period money), and the author as
  interested witness. Every real person/institution/event fact-checked; no
  LLM sources.
- Glossary: 32 rows added (7 people, 7 places, 2 organizations, 16 terms),
  merged SECTIONED. 野雞 given its full glossary decision here ("pheasant",
  decided) per the kickoff; 姨太太 (concubine), 舞女 (dance-girl), 大洋
  (silver dollar) carried per the settled money/term policy. House-grade
  terms 長三/么二/堂子/鹹肉莊/花煙間/淌白/煙妓 all decided.
- FACT-CHECK verdicts recorded IN the notes:
  * 抽籤禁娼 (ch019): CORROBORATED. The International Settlement's 1920
    lottery scheme to abolish licensed prostitution (Hershatter,
    Dangerous Pleasures); it drove the trade unlicensed and into the French
    Concession, as the author says.
  * 辜鴻銘 foot-fetish (ch015): CORROBORATED as the standing anecdote (his
    wife's bound feet his writing "stimulant"; sniffing bound feet).
  * 花選/花榜 courtesan beauty-elections (ch023): CORROBORATED as a real
    newspaper-run Shanghai institution from the 1860s-1917; the 1920
    candy-company version fits the pattern. 永安公司天韻樓 (Wing On roof
    garden, opened 1918): venue CORROBORATED.
  * 美麗牌 / 強盜牌 cigarettes (ch026): CORROBORATED. "Beauty" (My Dear,
    Hwa Ching, 1925) and "Pirate" (BAT's Old Knife) were real brands.
  * 斷袖 cut-sleeve (ch027): the Emperor Ai / Dong Xian allusion, standard.
  * UNCORROBORATED / as-reported (honestly flagged in the notes): the
    企妹 candy company and 電光日報 (ch023); the procurers 薛大塊頭 and
    寄生姆媽 (ch022); the 聞鶯 女相士 murder-case (ch034, a Shanghai
    sensation of the early 1930s, no independent record traced).
  * SOURCE SELF-CENSORSHIP (ch031): the reprint blanks a word as ××
    ("a colony of the ×× people"); plainly "Japanese" from the 東洋
    context. Rendered as printed (××), footnoted.

### Reprint / digitization glitches (LISTed per policy)
- ch015 p59: 楊 printed for 榻 ('couch'); a reprint misprint, rendered to
  plain sense, footnoted-free (sense unambiguous), logged here.

### NOT re-noted this batch (already placed; cross-referenced instead)
- 四馬路 / 福州路 Fourth Avenue: full notes at ch003 and ch012; the ch015
  glossary row cross-refs. 野雞 pheasant: defined at ch012; a glossary row
  added here, and the house-grade note at ch019 expands the system rather
  than re-defining the term. 春宮 spring-palace prints: ch012 (related to
  ch029's 妖精打架, cross-referenced in sense). Money system (dollar / 大洋 /
  小洋 / 毛 / 角 / 分): ch001 and ch014 notes stand; carried, not re-noted.
- Deferred to their own later chapters: 阿羊哥 Brother Sheep (full note at
  ch078); 野雞 standalone (ch043 野雞大學, ch093 野雞).

### Register / voice
- Held to the frozen ch001 reference. The demimonde material rendered in the
  newspaperman's quick, worldly, amused register, the author's asides (the
  foot-sniffing "school of Gu Hongming", the "Milk President" joke, the
  physiognomist's double-meaning "guaranteed to please you") kept in his
  editorializing voice. Contemptuous period language on male prostitution
  (ch027) rendered as printed, terms footnoted neutrally.

## B04 — ch035-ch052 (一杯茶值五大元 through 味蒓園); PDF 84-108 / printed 82-106

The prices-and-trades cluster: teahouse waitresses, the three-hundred-dollar
Cantonese dinner, the sixty-cash character-splitters, the fallen street-singer,
the obscene-book hawkers, the opera master Tan Xinpei, seamstresses and mending
women, the pheasant universities and gilded doctorates, the flower-vase clerks,
the booked hotel rooms, Avenue Joffre gone Russian and the White Russian
drifters, the post-office coolies and parcel companies, and Zhang's Garden.

### Pipeline / method
- Render 84-108 @300dpi. OCR tesseract chi_tra_vert --psm 5 (crop --left 0.03
  --right 0.97 --top 0.13 --bottom 0.95) as scaffold ONLY; every page EYE-READ
  at magnification and data/zh hand-transcribed, exactly as B01-B03. pgrep -c
  tesseract = 0 after OCR (verified). indents.py unused (horizontal-only);
  paragraphs finalized by hand on the blank-line + short-line-at-seam signal.
- Crop-verified spans recorded in data/ocr_fixes.json: ch035 鄉下土老少 (as
  printed, NOT the idiom 土老兒), ch044 斬鹹肉 (斬 not 軋), ch049 釘巴 (金+丁,
  obscure beggar term), ch052 title 味蒓園.
- check_config.json REGENERATED to the 18 units whose data/zh exists (ch035-052).

### Gates (all green)
- verify_unit (parity+numbers+anchors): PASS on all 18. check_numbers --noise:
  0 unresolved. check_align: no pair strays >2.2x from median (ratios 4.4-6.1
  en/han). check_structure: parity OK, 61 notes 0 unresolved, headings OK.
  check_content: all name occurrences in the paired paragraph. qc_entities: 0
  misses. check_register --ref out/ch001_reading.md: within tolerance on all 18.
  check_apparatus: 0 failures / 0 warnings. qa_epub: PASS (272 notes:
  refs=bodies=backlinks, all links resolve). epubcheck 5.1.0: 0 errors /
  0 warnings.
- Numeric-invariant noise added this batch (name/idiom numerals, longest-first):
  黃楚九, 九畝地, 億定盤路, 萬民矚目, 十餘萬, 塵煙四起. Real quantities carried
  in the English, never noised (three-hundred-dollar dinner, five-silver-dollar
  tea, sixty cash, 二元二角 "two dollars and two jiao", etc.).

### Apparatus
- 61 notes (book-wide 212-272), GENEROUS per the commissioner: 3/3/3/7/4/13/
  2/2/2/2/2/1/2/3/2/3/1/6 across ch035-052 (ch040 the theatre chapter carries 13).
- Glossary: 36 rows added (10 people, 14 places, 7 organizations, 5 terms),
  merged SECTIONED. 永安公司 (Wing On) already present, left untouched.
- 2 reprint photos through the figure pipeline: ch037 (p88, 老上海的拆字攤,
  the character-stall) and ch052 (p108, 味蒓園 = Arcadia Hall in Zhang's
  Garden). Both cropped to data/figs/, alt + provenance caption (2019 editor).

### Fact-check verdicts (recorded IN the notes; Wikipedia/Baidu Baike/academic, no LLM sources)
- Tan Xinpei 譚鑫培 (1847-1917), 小叫天, Tan-school laosheng master, court
  purveyor (譚供奉), died Beijing 1917 after a forced performance: CORROBORATED.
  The couplet 「...滿城爭說叫天兒」: REAL; 2nd line exact, 1st line a variant of
  the attested 「家國興亡誰管得」, commonly attributed to Fan Zengxiang 樊增祥.
- Tan + Sai Jinhua 賽金花 cohabitation (ch040): UNCORROBORATED / apocryphal.
  No standard source records it; the documented companion of those years was
  the opera amateur Sun Zuozhou 孫作舟, not Tan. Flagged in the note as gossip
  the author repeats (author-as-interested-witness).
- Huang Chujiu 黃楚九 (1872-1931), patent-medicine magnate, Great World founder:
  CORROBORATED (the 醒舞臺 house-name is consistent with his profile but not
  independently confirmed; noted so).
- Xia brothers 夏月珊/夏月潤, New Stage 新舞臺 (1908, Jiumudi) founders, and the
  "beloved son-in-law" tie (Xia Yuerun's father-in-law = Tan Xinpei):
  CORROBORATED.
- Lin Daiyu 林黛玉 the courtesan (1864-1924, born Lu Jinbao), one of the "Four
  Guardians" 四大金剛: CORROBORATED.
- Joffre / Avenue Joffre (renamed 1915, former Avenue Paul Brunat 寶昌路 1906,
  now Huaihai Rd): CORROBORATED. Zhang's Garden 張園 / Arcadia Hall 安塏第
  (built 1882 Zhang Shuhe, opened 1885, closed ~1918): CORROBORATED. The three
  department stores (Sincere 1917, Wing On 1918, Sun Sun 1926) with roof-gardens:
  CORROBORATED. 性史 (Zhang Jingsheng, 1926) and 肉蒲團 (Li Yu, 17th c.):
  CORROBORATED. General Post Office (1924, North Suzhou Road): CORROBORATED.

### Reprint / TOC discrepancies (LISTed per policy)
- ch052 title: book.json TOC had 味園; the printed title (and running head) is
  味蒓園 (Weichun-yuan). book.json corrected to 味蒓園; title_en "The Weiyuan"
  kept.

### NOT re-noted this batch (already placed; cross-referenced instead)
- Money system (dollar / 大洋 / 小洋 / 毛 / 角 / 分 / 文): ch001 & ch014 notes
  stand; carried, not re-noted (jiao/mao rendered per convention, never "cents").
- Avenue Joffre the STREET: full note at ch018; ch048 adds only 寶昌路 (former
  name) and Joffre the general, and cross-refs the avenue. Bubbling Well Road:
  ch017; mentioned ch038/ch052, not re-noted. salt-meat houses / 鹹肉: ch015 &
  ch018; ch044 斬鹹肉 and ch049 活肉 cross-ref. 野雞 pheasant: ch012; the ch043
  野雞大學 note and ch050 打野雞 note extend the slang rather than redefining it.
  Fourth Avenue: ch003/ch012. Zheng Zhengqiu & Xinwenbao: glossed B02, ch040/
  ch043 cross-ref.
- French Park 法國公園 noted briefly at ch052 (first mention) with a pointer to
  its own later sketch (ch058).

### Register / voice
- Held to the frozen ch001 reference throughout. The author's asides kept in
  his quick, worldly, amused editorializing voice: the "glass-cup" nickname,
  the sneer at pheasant universities and gilded doctorates, the pity for Weng
  Meiqian and the post-office coolies, the nostalgic sigh over Zhang's Garden.

---

## B05 (2026-08-12): ch053-ch070, the amusement-halls-and-rackets cluster

PDF 109-133, printed 107-131. 18 units, all single-run essays (ch060 carries a
two-part editorial coda; ch064 embeds two poem-riddle examples). Translated end
to end per the pipeline.

### Gates (all green)
- verify_unit (parity + numbers + anchors): PASS on all 18.
- check_align: PASS on all 18.
- check_apparatus: 0 failures, 0 warnings.
- check_structure --config: parity OK all 18; 87 notes, 0 unresolved.
- check_content --config: content alignment OK across all units (after two
  wording fixes: ch053 "Mr. Jing Runsan", ch058 "Jessfield Park").
- qc_entities (per bilingual): 0 misses across all 18 (ch064 aligned "riddles"
  to "poem-riddles" in two spots to match the glossary form).
- Cumulative EPUB rebuilt: 71 of 168 chapters, 359 notes, 13 pagebreaks.
- qa_epub: PASS (205 files, all links resolve). epubcheck 5.1.0: 0 fatals /
  0 errors / 0 warnings.
- check_register --ref out/ch001_reading.md: within tolerance on all 18.

### Apparatus added
- 87 footnotes (book-wide 273-359), 47 glossary rows, 3 reprint figures
  (ch053 Huang Chujiu portrait p110; ch056 Garden Bridge / Bund aerial p114;
  ch063 tiger-stove documentary photo p123, a later photograph).

### Fact-checks (verdict stated in each note)
- New World / Great World: Huang Chujiu and Jing Runsan (經潤三) co-founded the
  New World in 1914 (opened Dec 1915) at Nanjing/Xizang Rd by the Racecourse;
  Huang left in 1917 to found the Great World. CORROBORATED (zh Wikipedia).
- The reprint prints the co-founder as 經營三 (a misprint for 經潤三); rendered
  as printed in data/zh, translated to the attested "Jing Runsan", footnoted.
- Telephone: 1882 (Guangxu 8) first Shanghai exchange, Danish Great Northern
  Telegraph at No. 7 the Bund. CORROBORATED. The Zikawei (Xujiahui) Jesuit
  observatory strung telephone lines to the concession firms to relay weather
  from 1 Jan 1882. CORROBORATED. Author's "Pi Xiaopu" unverified; "Neng Mugu"
  a transliteration of a French Jesuit's name. Graham Bell + the muddled
  "American province of Canada" flagged.
- Electric light: "Lide" = R.W. Little (立德祿), founder of the Shanghai
  Electric Company (1882), China's first power plant. CORROBORATED. 自來火 =
  coal gas (first gas street-lamps Nanjing Rd, Dec 1865). CORROBORATED.
- Garden Bridge: first was the Wills Bridge (toll, 1856); bought out and freed
  by the Municipal Council in 1873 (Tongzhi guiyou); present steel truss 1907.
  CORROBORATED.
- Lu Xun of Wu (陸遜, 183-245, a Suzhou man): disambiguated from the writer
  魯迅. The Bubbling Well Road tomb is local legend, UNCORROBORATED (stated).
- French Park: Parc de Koukaza, opened 1909 in Gujiazhai, now Fuxing Park.
  CORROBORATED. Jessfield Park (兆豐公園, 1914, now Zhongshan Park). CORROBORATED.
- 次殖民地 (Sun Yat-sen's "sub-colony") glossed at ch055.

### Traps handled
- ch057 陸遜: full disambiguation note (Wu general, not the writer); the
  English title "The Site of Lu Xun's Tomb" would otherwise mislead.
- ch058 法國公園: full French-Park note placed here at its own chapter (only a
  pointer had stood at ch052).
- ch053 經營三: reprint misprint, handled as above.
- ch059 十八世紀: author's dating error (the gaslight/electric events are late
  19th c.); rendered as printed, footnoted.
- Self-censored blanks rendered as printed and footnoted: ×× clinics (ch054),
  ×× steamship company (ch061), ×× Poetry Societies (ch064).
- ch057 house number 三四〇 (No. 340): crop-verified the first digit is 三, not
  a clipped 一 (a magnified crop that cut the top strokes first read as 一).

### OCR / paragraphing notes
- tesseract chi_tra_vert psm 5 only (~85%); every page eye-read at
  magnification and data/zh hand-transcribed against the scans, as B01-B04.
- indents.py unusable; paragraph structure finalized by hand off the scan
  using the short-line signal at the page seams. ch063 (text band above a
  photo) has no internal short-column breaks, so it is one paragraph.
- data/noise.txt additions this batch (idiom/name/abbreviation numerals):
  巨萬, 零售, 百科, 十六浦, 十幾萬, and the targeted (?<=十一)、二 for the
  "eleven or twelve o'clock" abbreviation.

### NOT re-noted this batch (already placed; cross-referenced instead)
- Money system (dollar / 大洋 / 小洋 / 毛 / 角 / 分 / 文): ch001 & ch014 stand;
  ch056/ch058/ch062/ch063/ch064/ch068/ch069 all cite prices without re-noting.
- Huang Chujiu (glossed + noted B04): ch053 cross-refs. New World (glossed B04).
  Bubbling Well Road (ch017): ch057 mentions, not re-noted. 野雞 pheasant
  (ch012): not recurring here. 靜安寺路 (ch017): ch057 cross-ref.
- The huahui game gets its full note at ch065; ch066 (the result-cry "開什麼")
  cross-refs it. The little pawnshops get their note at ch062; ch069 (the
  "dropped ticket") cross-refs it.

## B06 - thieves, cheats & transport (ch071-ch090) - 2026-08-13

- 20 essays, PDF 134-158, printed folios 132-156. Offset printed = pdf - 2
  confirmed at every opener. ch072 (135-136), ch075 (139-140), ch088 (153-155),
  ch090 (157-158) are multi-page; ch073/074 etc single-page.
- 88 notes (book-wide 360-447), 67 glossary rows, 5 reprint figures.
- Gates all GREEN: verify_unit (parity/numbers/anchors), check_align,
  check_structure --config, check_content --config, qc_entities (per bilingual,
  0 misses), check_apparatus (0/0). qa_epub PASS (210 files, 447 notes resolve).
  epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings. check_register within
  tolerance on all 20 (essays, the "little dialogue - noisy" exempt register).

### Fact-checks (CORROBORATED unless stated)
- ch072: Wu Zhihui (吳稚暉, 1865-1953), a Kuomintang "Four Elders" and philologist.
  Rong Zongjing (榮宗敬, 1873-1938), the "Flour King"; his Shenxin combine's 1934
  liquidity crisis is the "cash-flow trouble," dating the piece to about 1934.
  Chen Gongbo (陳公博, 1892-1946), Minister of Industry 1931-1935, later a Wang
  Jingwei collaborator, executed 1946. Allusions: Lu Zhonglian (Warring States);
  因人成事 (the Mao Sui story, Records of the Grand Historian).
- ch074: 集團結婚, Shanghai's first municipal collective wedding was April 1935
  (New Life Movement, Mayor Wu Tiecheng); dates the piece to 1935 or after.
- ch081: allusions 以貌取人失之子羽 (Confucius on Tantai Ziyu, Records of the
  Grand Historian) and 倚馬千言 (Yuan Hong, A New Account of the Tales of the World).
- ch082: 六馬路 = Beihai Road, the sixth numbered road, laid out 1883 on the arc
  of the old racecourse. City God Temple cross-referenced (glossed/noted earlier).
- ch088: Sheng Xuanhuai (盛宣懷, zi 杏蓀, 1844-1916); his 1917 Shanghai funeral
  procession ran over a mile and drew perhaps a million, filmed as China's first
  newsreel (academic source "Spectacular Death: Sheng Xuanhuai's Funeral
  Procession in 1917"). Zhu Baosan (朱葆三, 1848-1926), Ningbo comprador, thrice
  head of the Chinese Chamber of Commerce; the French Concession's Rue Chu Pao
  San was named for him (confirmed by the reprint street-sign photo). Huang Chujiu
  (glossed B04) died January 1931 deep in debt, so his expected grand funeral was
  dropped, dating the piece to about 1933.
- ch089: 雲飛汽車公司 (Yunfei), a real and prominent early Shanghai taxi firm;
  the Longfei carriage firm to Yunfei taxi transition is reported per the author.
- Sourcing: Wikipedia / Baidu Baike / academic articles. A Grokipedia hit on Zhu
  Baosan was DISREGARDED per rule 5 (never source LLM-written references).

### Internal dating
- This cluster carries 1934 (Rong Zongjing crisis) and 1935 (collective weddings)
  references, mid-1930s, later than the nominal 1933 first edition. Consistent
  with the range HANDOFF already records; footnoted at ch072/ch074/ch088.

### Figures (5, all 2019-editor reprint photos; provenance stated in every caption)
- ch072: 吳稚暉 Wu Zhihui portrait and 榮宗敬 Rong Zongjing portrait (the full-page
  plate at pdf 136).
- ch088: 盛宣懷（杏蓀）portrait (pdf 153); 朱葆三之墓 Zhu Baosan's tomb and
  上海朱葆三路 the Rue Chu-Pao-San street scene (both pdf 155).

### OCR / paragraphing notes
- tesseract chi_tra_vert psm 5 only (~85%); every page eye-read at magnification
  and data/zh hand-transcribed against the scans, as B01-B05. indents.py unusable;
  paragraphing finalized by hand off the scan. Text bands sitting above a reprint
  photo (ch072 top of 135 is full text; ch088 top band of 153) parsed by the
  short-line/blank-line signal as usual; ch088's top band is a single paragraph.
- data/noise.txt additions this batch (each a non-quantity, never masking a drop;
  longest-first): 有零 (三百有零, "-odd"), 萬事 (myriad), 零落 (scattered),
  丘八 (soldier-cant, the 八 not eight), 朱葆三 (name, the 三 not three),
  三、四十 (thirty-or-forty, the 三 abbreviates 三十).
- data/ocr_fixes.json: crop-verified names/numbers recorded for
  ch071/ch073/ch088/ch089 (pickpocket names, gold prices, Sheng/Zhu names,
  carriage counts).

### NOT re-noted this batch (already placed; cross-referenced instead)
- Money system (dollar / 大洋 / 小洋 / 毛 / 角 / 分 / 文): ch001 & ch014 stand;
  ch076 (麻衣債, 五百塊/一角), ch085-ch090 (fares, coppers, dollar notes) cite
  prices without re-noting.
- 白相人 hoodlum (glossed earlier): used at ch072/ch080/ch082, rendered "hoodlum"
  per the decided rendering (locked by the ch132 title "The Hoodlum's Missus");
  its literal "man-about-town" sense is given once in the ch072 note.
- Huang Chujiu (glossed/noted B04): ch088 adds only the death-and-canceled-funeral
  detail. 跑馬廳 the Racecourse (glossed B05): ch082/ch089 cross-ref. 弄堂, 老虎灶,
  小押當, 花會, 遊戲場, 洋人/租界 furniture: cross-referenced, not re-noted.
- 洋盤 sucker (glossed here at ch073): ch078 (阿羊哥) cross-refs the pun.

---

## B07 — ch091-ch110 (假人參 through 尋人), PDF 159-183, printed 157-181

Cheap-eats, quack-doctors and petty-price cluster: fake ginseng, empty-trick
markups, pheasants (cabs/brokers/ticket-touts), the doctor's guarantee, the
night food-stall economy (congee, tofu, wonton, set meals, cold stalls),
ready-made clothiers, room-and-board and privy tolls, iron counter-grilles,
charity sharks, advertising doctors, "superior Chinese," surly clerks
(ghost-faces), the "thirteen o'clock" slang, and missing-person notices.
Offset confirmed printed = pdf - 2, folio re-read at every opener.

### Gates (all green)
- verify_unit (parity + numbers + anchors): all 20 units clean.
- check_align: all 20 within ratio (median en/han 4.87-6.40).
- check_structure --config / check_content --config: PASS across all units.
- qc_entities per bilingual: 0 misses on all 20 (incl. the 33 new glossary rows).
- check_apparatus: 0 failures, 0 warnings.
- check_register --ref out/ch001_reading.md: within tolerance on all 20.
- Build: 111/168 chapters, 489 notes, 13 pagebreaks. qa_epub PASS
  (214 files, 489 ref/body/backlink). epubcheck 5.1.0: 0 fatals/0 errors/0 warnings.

### Apparatus
- 42 notes (book-wide 448-489), 33 glossary rows, 4 reprint figures.
- Fact-checks: Dangui First Stage (founded 1867, Fuzhou Road) and Xu Shaoqing
  its manager to 1914 — CORROBORATED (zh.wikipedia). Lao Dafang confectioner
  (founded 1842); ~40 Shanghai shops shared the name in the 1930s, each set off
  by an added mark — CORROBORATED and matches the author's "a mark added above
  to tell one from another" (ch101). Northeast Volunteer Army (irregular
  anti-Japanese forces after Sept 1931; large 1932 Shanghai relief drives) —
  general facts CORROBORATED, the specific fund-audit scandal the author reports
  UNCORROBORATED in detail; dates the essay to ~1933 (ch105). Feng Zikai
  (1898-1975) cartoonist, studio Yuanyuan Hall, "TK" mark — standard biography.
- Classical allusions footnoted: 吮癰舐痔 (Zhuangzi, abject flattery, ch107);
  螟蛉 (Book of Songs, the adopted child, ch109). Custom footnoted: the missing-
  person notice with 人 printed upside-down (ch110).

### Figures (4, all 2019-editor reprint additions; provenance stated in caption)
- ch096: Feng Zikai brush cartoon "餛飩擔" (The Wonton Carrying-Pole), p165.
- ch098: photo of a 蘇廣成衣鋪 (Su-Guang ready-made clothier) street stall, p168.
- ch099: modern photo of the City God Temple secondhand-book market, p169.
- ch100: photo of a traditional theater's carved balcony boxes, p171.
- ch105 (靠災民發財的善棍) carries NO photo despite being a likely spot — the
  three pages (176-178) are text only; recorded as a deliberate empty figure list.

### OCR / paragraphing notes
- tesseract chi_tra_vert psm 5 only (~85%); every page eye-read at magnification
  and data/zh hand-transcribed against the scans, as B01-B06. indents.py unusable;
  paragraphing finalized by hand off the scan (short-line signal at page seams).
  ch091 (159-160), ch098 (167-168), ch100 (170-171), ch105 (176-178) are the
  multi-page units; ch100's text ends on p170 (p171 is the full-page photo).
- Digitization glitch (render to sense, listed here per CLAUDE.md): ch109 prints
  an unusual 呆戀 for the "dullard" word ("說他呆戀並不呆戀"); the heart-radical
  glyph was crop-verified at 6x but is semantically off (likely a reset error for
  呆戇, Wu "dull-witted"). Rendered for plain sense ("call him a dullard and he is
  no dullard") and footnoted.
- Crop-verified this batch: 拆洋濫污 (ch103 Wu slang, verified 3x); the ch109
  呆戀 glyph (verified 6x); folios read off every opener.
- data/noise.txt additions (each a non-quantity, never masking a drop; longest
  first): 五方雜處 (all quarters, 五 not five), 四出 (on all sides, 四 not four),
  (?<=十五)、六 (十五、六歲 abbreviation, keeps 十五 checked), 五官 (the facial
  features, 五 not five).

### NOT re-noted this batch (already placed; cross-referenced instead)
- Money system (dollar / 大洋 / 小洋 / 毛 / 角 / 分 / 文): ch001 & ch014 stand;
  ch096/ch097/ch102/ch103 cite mao/jiao/cash/copper prices without re-noting the
  policy (ch096 adds only the 100-cash = 10-copper reckoning; ch102 adds 制錢).
- 城隍廟 City God Temple (noted ch001): ch099 cross-refs. 野雞 pheasant (noted
  ch012): ch093/ch095 cross-ref the extended slang. 麥克麥克 muchee-muchee (noted
  ch078): ch105 cross-refs. 寓公 idle rich sojourner (noted ch089): ch107 uses it.
  opium (noted ch033): ch101 cross-refs. pidgin (noted ch018/ch078): ch105 uses
  muchee-muchee; ch107 renders 洋涇浜話 as "pidgin". 捕房 police station (glossed):
  ch103 uses "plain-clothes constable" for 探捕 (its own glossary row) and
  "police station". 小押店 little pawnshop (ch062): ch104 cross-refs.

## B08 — ch111-ch129 (俞調、馬調 through 戤牌頭), PDF 184-208, printed 182-206 (2026-08-13)

Tanci balladry and quack-medicine cant giving way to the con-and-beggar trades.
All 19 units translated end to end; every gate green. Offset held printed = pdf - 2,
folio read off every opener (182 on pdf 184 ... 206 on pdf 208).

### Scope note (kickoff title vs book.json)
- The kickoff titled the batch "through 兜得轉與跑得開," which is ch130 (pdf 209),
  in B09. The authoritative book.json batch B08 = ch111-ch129 (pdf 184-208); the
  last unit is ch129 戤牌頭 "Trading on a Big Name." Followed book.json.

### Units and paragraph structure (hand-finalized off the scan)
- 1 para: ch111, ch113, ch116, ch119, ch121, ch122, ch123, ch124, ch126, ch127.
- 2 para: ch112, ch114, ch117, ch125, ch128, ch129.
- 3 para: ch120. 4 para: ch115, ch118.
- Multi-page units: ch112 (185-186), ch114 (188-190, incl. a photo-only p190),
  ch115 (191-192), ch118 (195-196), ch120 (198-199). ch114's text ends on p189;
  p190 is two full-page reprint images (text finished on the previous page,
  as HANDOFF predicted).

### book.json correction
- ch116 年紅燈 title_en was "The New Year Red Lantern" — a mistranslation. The
  essay is about NEON SIGNS (氖光 neon; 霓紅燈), not New Year lanterns. Corrected
  title_en to "Neon Lights"; nav and section heading rebuilt, old title gone.

### Notes (66; book-wide 490-555)
Generous per the commissioner's instruction. ch114 (the Yan Ruisheng case) carries
13; density tapers to 1-2 in the short late sketches, which is healthy.
- Fact-checks (verdict stated in each note):
  - Yan Ruisheng / Wang Lianying case CONTRADICTS the author's date: he prints 民
    十一(壬戌)=1922, but the murder was June 1920 (民九, 庚申), Yan executed 23 Nov
    1920; the reprinted 申報 ad is dated 2 July 1920. Rendered as printed, footnoted.
    (Wikipedia 閻瑞生案; Jiemian/正午 feature.)
  - He Fenglin (1873-1935, 字茂如), Anhui-clique general, 淞滬護軍使 1920-1924 —
    CORROBORATED (Baidu/Wikipedia 何丰林).
  - Yu Xiushan (俞調) / Ma Rufei (馬調) as the two tanci schools of the Jiaqing-
    Daoguang and Xianfeng-Tongzhi eras, alongside Chen Yugan's 陳調, and 開篇 as
    the prelude — CORROBORATED (弹词 baike; 苏州评弹 essay).
  - Yan Duhe (1889-1968), Xinwenbao 快活林 editor 30+ yrs, serialized Zhang
    Henshui — CORROBORATED (Baidu 严独鹤; Wenhui).
  - The three dog-tracks (Mingyuan/Stadium, Shenyuan in the Settlement; Yiyuan/
    Canidrome on Avenue du Roi Albert, French Concession, built by J. J. Chollot;
    the two Settlement tracks closed ~1931) — author's account CORROBORATED
    (研之有物 / 故事 StoryStudio essays).
  - 姊妹花 (Twin Sisters, 1934, 鄭正秋 dir., 胡蝶), Aurora University, 拆白黨,
    癟三, 花國總理 / 1917 New World flower-election, 新生活運動 (1934) — all
    CORROBORATED. Pu Jinghong (ch115) UNCORROBORATED (not in film histories).

### Figures (3, all 2019-editor reprint additions; ch114; provenance in caption)
- ch114_yan_wang_portraits.png (p188): the two oval news portraits; in-photo
  labels 謀財害命之要犯 閻瑞生 / 前花國總理 王蓮英. Editor caption line excluded.
- ch114_shenbao_ad.png (p190 top): 申報 2 July 1920 ad for 《蓮英被害記》.
- ch114_yanruisheng_playbill.png (p190 bottom): New Stage playbill for 《閻瑞生》.
- No other page in the batch carries a reprint photo (eyeballed each).

### OCR / paragraphing
- tesseract chi_tra_vert psm 5 only (~85%); every page eye-read at magnification
  and data/zh hand-transcribed against the scans, as B01-B07. indents.py unusable;
  paragraphing finalized by hand (short-line signal at page seams; the text band
  above a photo can be one paragraph).
- Crop-verified this batch: 候政 (ch112, the doctor's disclaimer — 政 not 正/診);
  厲害 (ch112 tail, not 屬); 橋塊 (ch122, printed 塊 where 堍 "bridge-approach"
  is expected — rendered to sense, no separate note); 頂梢 (ch123 begging cant,
  glossed uncertain); 吃鬥 / 戤 (ch129, author's own gloss 兇暴 confirms sense).
- data/noise.txt additions (each a non-quantity, never masking a drop; longest
  first): 禮拜三、六 (Wed & Sat race nights, weekday names not counts; English
  carries "Wednesday and Saturday"), 癟三 (biesan, the 三 is part of the word).
  ch126 兩事 carried as a real count ("one of the two affairs, red or white").

### Register / QC (all green)
- verify_unit (parity, numbers, anchors): PASS on all 19.
- check_align, check_structure --config, check_content --config: PASS.
- qc_entities per bilingual: 0 misses (aligned three existing renderings to the
  ledger: 舞女=dance-girl ch115, 堂倌=waiter ch120, 拆字=character-splitting ch121).
- check_apparatus: 0/0. check_register --ref out/ch001_reading.md: all within
  tolerance. qa_epub: PASS (168 docs, 555 notes ref/body/backlink). epubcheck
  5.1.0: 0 fatals / 0 errors / 0 warnings.

### Glossary (49 new rows; 3 already present, left untouched; 302 total)
People: Yu Xiushan, Ma Rufei, Yan Ruisheng, Wang Lianying, He Fenglin, Wu Chunfang,
Zhu Zhijia, Zhu Baosan, Zhao Junyu, Wang Youyou, Yan Duhe, Pu Jinghong. Places:
Fuxiang Li, Xuzhou, Jiumudi, Aurora University, Avenue du Roi Albert, Ward Road,
Yanping Road. Orgs: the New Stage, the Songhu Defence Commissioner, the Canidrome,
the Mingyuan, the Shenyuan. Terms: prelude-song, tanci, the three scares, pulse-
record, morphine, white flour, firing the big gun, red-and-white pills, Premier of
the Flower Kingdom, peeling-white gang, New Life, year-red lamp, neon lamp, sweet
osmanthus, dog racing, jai alai, cement, crab-crawling script, biesan, limpet,
driving the pigs, slaughtering the pigs, taking the payoff, haggling the cut,
patronage ticket, squeeze, trading on a big name, seat-agent.

### NOT re-noted this batch (already placed; cross-referenced instead)
- huahui (noted ch065/ch066): ch118 cross-refs via the 致富全書 note.
- 新世界 the New World / flower-election (noted ch023/ch038/ch053): ch114 cross-refs.
- 白相人 hoodlum (noted ch072): ch127 cross-refs (the author's own gloss 即流氓).
- pidgin / Yangjingbang (noted ch018/ch078): ch123 cross-refs. New Life Movement
  (noted ch074): ch115's note cross-refs and adds only the perm ban. Suzhou Creek
  bridges 天后宮橋/盆湯弄橋 (noted ch056): ch122's note cross-refs, adds 老閘橋/垃圾橋.
  Money policy (ch001/ch014): ch118/ch127/ch128 cite 大洋/大洋鈿/塊 without re-noting.

## B09 — ch130-ch155 (兜得轉與跑得開 through 兩個半滑頭), PDF 209-233, printed 207-231 (2026-08-13)

The swindler / beggar / street-trade heart of the book: 26 short essays on
kidnappers, the hoodlum's wife, cricket-fighting, the three-lights gang, Wu-slang
tags, hat-snatching, a long run of selling-cons and rag trades, two dialect-word
essays, fortune-telling, resurrection cigarettes, tattooing, judgment tea,
skimming, savings swindles, hatching bean sprouts, and two-and-a-half slickers.
All 26 units eye-read at magnification and hand-transcribed to data/zh against the
scans (tesseract chi_tra_vert psm 5 kept only as a scaffold; every page corrected
by eye). Offset held printed = pdf - 2, verified at every opener.

### Page structure resolved
- Two shared pages, boundaries confirmed by eye: PDF 214 carries ch135 頂呱呱與硬繃繃
  (one para) then ch136 拋頂宮 (one para); PDF 218 carries ch140 賣性照片 (one para)
  then ch141 賣冰 (one para).
- ch131 綁匪 finished on PDF 210; ch132 白相人嫂嫂 is a short two-paragraph essay
  wholly on PDF 211 (the lower half of the page is blank, not a lost leaf).
- NUMBERING GAP RESOLVED: the "skipped" PDF 231 (printed 229) is NOT a blank or a
  plate. It is the SECOND page of ch153 儲蓄騙, which runs PDF 230-231 (a six-
  paragraph essay, the longest in the batch). The running head on 231 reads 儲蓄騙
  and the text continues mid-sentence from 230 (滿了五 | 年仍舊還本). book.json's
  ch153 pdf 230 / ch154 pdf 232 is therefore correct; there is no mis-count.
- No reprint photographs on any page 209-233 (all full-text). Zero figures this
  batch, recorded as a deliberate decision.

### Register / QC (all green)
- verify_unit (parity, numbers, anchors): PASS on all 26.
- check_align, check_structure --config, check_content --config: PASS.
- qc_entities per bilingual: 0 misses. Two existing-key substring collisions caught
  and aligned to the ledger: 探捕 (plain-clothes constable) surfaced inside 警探捕
  in ch140 (rendered "plain-clothes constable"); 自來火 (self-coming fire) inside
  自來火街 in ch149 (rendered "Gas Street, the street of the 'self-coming fire'").
- check_apparatus: 0/0. check_register --ref out/ch001_reading.md: all 26 within
  tolerance. qa_epub: PASS (168 docs, 621 notes ref/body/backlink). epubcheck
  5.1.0: 0 fatals / 0 errors / 0 warnings.

### Numbers noise added (data/noise.txt; all false positives, none masks a drop)
五色 (five-colour idiom, ch137/ch142); 張三 / 李四 (generic names, ch137);
(?<=十四)兩 and (?<=三十)兩(?=天|夜) (兩天/兩夜 summarising counter, ch139/ch144);
二(?=、三十) (abbreviated "twenty or thirty", ch133); 三山 (Sanshan place name);
五光十色 (idiom); 十足 (idiom "thoroughly", ch147); 零(?=紙) / 零(?=碎) (零 = odd/
sundry not zero, ch145); 萬國 (International Savings Society name, ch153). NB
ch151's 效力等於零 is a REAL "zero" and was carried in the English, not noised.

### Glossary (17 new rows; 0 already present; 319 total)
Terms: catching crickets (捉蟋蟀), slicker (滑頭), old brothers (老弟兄), old hand
(老門檻), long ingots (長錠), the Three-Lights Gang (三光黨), resurrection cigarettes
(還魂煙), judgment tea (吃講茶), hatching bean sprouts (孵豆芽), a-la (阿拉), spring-
palace pictures (春宮), scavenging (拾荒), dredging for tinfoil ash (撈錫箔灰).
Orgs: the International Savings Society (萬國儲蓄會). Places: the Sanshan Guild Hall
(三山會館), Shengxian (嵊縣), Hankou (漢口). 62 footnotes (book-wide 556-617).

### Fact-checks (rule 5)
- 萬國儲蓄會 International Savings Society (ch153): CORROBORATED. Founded 1912 in the
  French Concession by Rene Fano and Jean Beudin; 15-year prize-bonds at $12/mo
  (half $6, quarter $3) with a monthly lottery draw; ~130,000 subscribers by 1930;
  its apartment block survives as the Wukang / Normandie Mansion. Matches the essay
  (東方仿萬國辦法; 只繳一次現款 month-by-month prize, 滿五年還本). Source: Shanghailander
  / Historic Shanghai / Wikipedia (Wukang Mansion).
- 三山會館 Sanshan Guild Hall (ch142): CORROBORATED as an institution. The Fuzhou /
  Fujian native-place hall in Shanghai (三山 = old name for Fuzhou); the surviving
  hall, built 1909 in Nanshi as a Tianhou/Mazu temple by Fujian fruit-merchants,
  still stands at 1551 Zhongshan South Rd. The author places one at the west end of
  Fuzhou Road; noted honestly. Source: zh.wikipedia / Baidu Baike / Huangpu district.
- 嵊縣 Sheng County, Zhejiang (ch131): the county is real (now Shengzhou); its
  reputation as the seedbed of the Shanghai kidnapping gangs is the one the text and
  popular tradition assign. Specific case records not located; noted at that level.
- 瞿紹伊 (ch130): named as the author's lawyer friend. UNCORROBORATED by search;
  noted honestly as "not further identified with certainty."

### Wu / cant glossed but not ledgered (translator's decisions, noted in situ)
布非切 (ch141, the slurred "buy ice" heard as indecent; pun untranslatable, noted);
阿拉舍希 (ch147, Ningbo particles, not certainly parsed); 口天先生 = 吳/Wu and 草頭老班
(ch155, veiled surnames by character-splitting; the second not recoverable, noted).

### NOT re-noted this batch (already placed; cross-referenced instead)
- 白相人 hoodlum (glossary + noted ch072/ch127): recurs ch130/ch132/ch146(老白相)/
  ch150; rendered "hoodlum" throughout, not re-noted.
- 揩油 skim (noted ch098): ch152 is its own essay and adds the literal "wipe the
  oil" etymology, cross-referencing ch098 rather than re-noting.
- 捉蟋蟀 catching crickets (noted ch133): recurs ch149, cross-ref not re-noted.
- 三百六十行 the 360 trades (noted ch133): recurs ch145, cross-ref not re-noted.
- 拆白黨 peeling-white gang (noted ch114): ch134 likens the three-lights gang to it,
  not re-noted. 拆字 character-splitting (noted ch037/ch121): ch155's 口天 note
  cross-refs it. 早吃日頭夜吃露水 (noted ch150): recurs ch154, not re-noted.
- 綁票 kidnapping (noted B07 ch104): ch131, not re-noted. 捕房 police station,
  四馬路/福州路 Fuzhou Road, money policy (大洋/小洋/毛/角/文/鈿): all cited without
  re-noting.

## B10 — ch156-ch167 + whole-book close-out (2026-08-13) — FINAL BATCH

Units: ch156 點香燭 through ch167 髦兒戲 (PDF 234-247, printed 232-245). 26
paragraphs, 22 notes (book-wide 622-643), 20 glossary rows, 0 figures.

**Page-structure traps resolved off the scan:**
- NUMBERING GAP resolved: ch161 空頭支票 spans PDF 239-241 (four paragraphs);
  PDF 240-241 are its continuation pages, not a plate or blank (exactly as
  ch153 spanned 230-231 in B09). ch162 假鈔票 opens at PDF 242. Verified by
  folio: p239=237, p240=238, p241=239, p242=240 (printed = pdf - 2 holds).
- Every opener's folio read off the scan; body ends at PDF 247 (printed 245,
  ch167, the last essay). PDF 248 blank; 249 = 2019 reprint imprint page;
  250 = National Library CIP; no errata table anywhere.
- No two-essays-share-a-page splits in B10 (each short-titled essay —
  叫火燭/抄把子/假客氣 — occupies its own leaf).

**OCR / transcription:** tesseract chi_tra_vert --psm 5 scaffold only (~85%,
PaddleOCR absent). Every page eye-read at magnification; data/zh hand-
transcribed. `pgrep -c tesseract` = 0 after OCR. Crop-verified at 3-4x and
recorded in data/ocr_fixes.json: bank names 福源/寅泰 (OCR 賓春); the four
counterfeit-coin methods 夾銅/純銅/藥水/銼邊 (OCR 夾多/頃銅/鍾邊); 小錢莊歇夥和
銀匠店歇工; coin/exchange numerals (五百/三百/五十塊, 一塊錢可購二十多角); all
ch167 place and actress names (胡家宅, 群仙茶園, 林黛玉/陳長庚/紅菊花/翁梅倩,
恩曉峰/張文奎/張文豔/白玉梅/張少泉/牛桂芬). No reprint photos on any B10 page —
figure list deliberately empty.

**Checks (all green):** check_structure parity 12/12 OK, 22 anchors resolved;
verify_unit numbers clean after 4 targeted noises (萬狀; 絲毫無二/毫髮無二; 四馬路);
check_align OK; check_content OK (ch167 四馬路 displacement resolved by using the
glossary's decided "Fourth Avenue" for 四馬路, "Fuzhou Road" reserved for 福州路);
qc_entities clean per bilingual; check_apparatus 0/0; check_register all 12
within tolerance of ch001. qa_epub PASS (643/643/643); epubcheck 5.1.0 clean
(0/0/0/0).

**Fact-checks (real scholarship, not LLM sites):**
- 一二八 January 28th Incident (ch157): CORROBORATED — 1932 Shanghai War,
  Japanese attack on Zhabei/Hongkou 28 Jan 1932, 19th Route Army resisted >1
  month (Wikipedia/chiculture; multiple standard histories).
- 恩曉峰 En Xiaofeng (ch167): CORROBORATED — Manchu of Beijing (1887-1949), a
  noted female laosheng of the early all-women Peking-opera stage.
- 男女合演 mixed-sex ban (ch167): CORROBORATED — Beijing govt banned mixed casts
  (reaffirmed 1913), hence the all-female troupes; relaxation ended them.
- 某國 = Japan euphemism (ch157) vs 日本 named (ch162): the author's own veil and
  its dropping; rendered as printed, verdict stated in the notes.
- Minor theatres/banks (群仙,丹桂,妙舞臺,大富貴;福源,寅泰) and minor actresses:
  period-plausible, not individually corroborated; provisional + noted as such.

**Reprint misprints in B10:** none found (B10 clean; earlier list ch052/ch053/
ch109/ch116/ch122 unchanged).

**NOT re-noted this batch (already placed; cross-referenced instead):**
- 空城計 Empty Fort (noted ch040): ch161 cross-refs, brief pointer note only.
- 虹口 Hongkou (noted ch018/ch079): ch157 cross-refs. 北平 Beiping (noted ch100):
  ch162 cross-refs, not re-noted. 嗎啡/opium forms (noted ch113/ch033): ch160
  cross-refs. 林黛玉 (noted ch038): ch167 cross-refs in the 坤角 note, not
  re-noted. 新舞臺 New Stage (noted ch040/ch114): ch167 cites without re-noting.
  錢莊 native bank, 花會 huahui, 探捕 constable, 揩油 skim, money policy: all cited
  without re-noting.

**Whole-book close-out:**
- Back matter: NO errata table; the 2019 imprint page (PDF 249) + CIP (PDF 250)
  are modern production data already in book.json metadata. back_matter.json
  left INERT (the builder's colophon template is for an ORIGINAL copyright leaf
  and would mislabel a reprint imprint). Recorded decision.
- Reconciliation (check_reconcile): epithet drift 0. Spelling locale CASCADED
  to British across ALL reading files + notes/glossary/figures bodies (frozen
  ref ch001 uses "honour"). One real American form fixed ("centerpiece" ->
  "centrepiece"). Residual reconcile MIXED flag is two LOCALE-NEUTRAL words
  ("laborious","vigorous", identical in both locales) caught by the checker's
  prefix heuristic — a documented false positive, not a real mixed locale.
- out/term_ledger.md (339 rows) and out/deep_audit.md (fixed-seed 4.1% sample,
  0 defects in the re-audited subset) rendered.
- authority.json fed this book's renderings under slug "scales-and-claws"
  (317 new terms, 22 appended; 4 benign cross-book article/spacing variants).
- Final EPUB committed with `git add -f out/scales-and-claws-of-shanghai.epub`.

**THE BOOK IS COMPLETE (168/168 units).** Further work is a corrections pass.
