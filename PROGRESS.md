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
