# PROGRESS — Chen Yangshan: Hero of the Secret War (秘战英雄陈养山)

The running per-batch log. Written as work happens, not at the end.

## Batch 4. Chapter 3 "From Enemy-Occupied Territory Back to Yan'an" (ch03; PDF 93–115, printed 82–104)

Whole chapter in one file: out/ch03_reading.md + data/zh/ch03.txt, three "###"
section headings from book.json. `ch03` mapped in data/check_config.json (docs +
sources). Because data/zh is gitignored and ch01/ch02 zh are gone on a fresh
checkout, the structural checks were scoped with data/check_config.ch03.json
(ch03 only); build/qa/epubcheck/register run on the whole cumulative EPUB.

### Content
- Section 1 (西安事变隐蔽战线高奏凯歌, PDF 94): the Xi'an Incident on the hidden
  front — Gao Fuyuan won over in captivity, Li Kenong's Luochuan talks with Zhang
  Xueliang and Wang Yizhe, Zhou Enlai's Yan'an meeting with Zhang, Wang Feng and
  Wang Shiying opening the channel to Yang Hucheng, and Chen Yangshan's Xi'an
  intelligence station (1936–40, cover name Chen Mingjun, via Song Qiyun).
- Section 2 (回到延安，整风学习为作战, PDF 103): the wallet-loss ruse escaping
  Xi'an, Chen at the Central Social Affairs Department under Kang Sheng, Zhang
  Suzhen's Party membership and nurseries, the Rectification at the Central Party
  School, Chen as Seventh-Branch secretary vetting cadres (Jiang Qing and Ye Qun
  among them), delegate to the "Seventh Congress," and Guan Fushan's recollection.
- Section 3 (三问康生，战友鲜血同志泪, PDF 110): the killing of four ex-Special
  Branch cadres (Wu Hujing, Xiao Shouhuang, Ouyang Xin, He Changzhi) in the Soviet
  purge, Chen's three questions to Kang Sheng, Kang's Yan'an "Rescue Movement" and
  Mao's counter-directives, and Chen's 1979 and 1988 letters exposing Kang.

### Paragraph structure (125 body paras: S1=40, S2=40, S3=45)
- Quoted documents/recollections set off with `{v}` (18 lines): Guan Fushan's
  3-para recollection; Mao's anti-traitor directive; Chen's two letters (the
  1979 exposé, 5 paras; and the appended 1988 letter to the Central Organization
  Department, title + salutation + body + closing). "附:" -> "Appended:" is a plain
  paragraph separating the two letter blocks. The 致/敬礼 closing merged to one
  line ("With respectful regards,") in both zh and en.

### OCR / silent-loss (crop-verified this batch)
- Same crop as ch01/ch02 (do-not-revert): --lang chi_sim --psm 6 --left 0.045
  --right 0.985 --top 0.08, running-head "秘战英雄陈养山", recto (PDF even)
  --bottom 0.945 / verso (PDF odd) --bottom 0.915, run per-page.
- **DROPPED TAIL restored:** PDF 94 mid-page "尖锐起来。" (the 4-char final line of
  the 张学良–蒋介石 paragraph) was silently dropped by tesseract; restored from the
  scan. Every page bottom verified; no other drops.
- **Crop-verified name corrections** (OCR wrong -> scan-correct): 戚元德 Qi Yuande
  (not 威), 塞先佛 Sai Xianfo (not 寒; base 土, flagged provisional), 劳山 Laoshan
  (not 序山), 瓦窑堡 Wayaobao, 彭德怀 Peng Dehuai, 李克农 Li Kenong, 阎揆要 Yan
  Kuiyao, 建宇 Jianyu (not 建字), 鄜县 Fu County.
- **Source inconsistency (rendered + footnoted):** PDF 94 prints 宗绮云 (Zong) at
  first mention; PDF 99 and the photo caption print 宋绮云 (Song Qiyun, the
  attested martyr). Rendered "Song Qiyun" throughout, variant noted.

### Figures (5; every page eyeballed)
- p0096-f1 Yang Hucheng portrait; p0098-f1 the Maoling group photo (Zhang/Yang/
  Chiang, Oct 1936); p0099-f1 Song Qiyun portrait; p0101-f1 Chen with family
  (1938); p0107-f1 the Seventh Congress hall. Captions translated into
  figures.json (alt uses single quotes only). Chapter-opener photo on PDF 93
  SKIPPED (per ch01/ch02). find_figures matched the plates; none are line art.
- **Source typo in a caption:** the Maoling caption prints 汉开帝墓; Maoling is the
  tomb of Emperor Wu of Han (汉武帝), rendered correctly in the translated caption.

### Fact-checks carried in the notes (interested-witness discipline)
- **Seventh Congress date:** source says 1943 (prep meeting and congress); the
  Seventh Congress in fact met 23 Apr–11 Jun 1945. Rendered as printed; footnoted
  that Mao's own "24-year course" (1921+24) and the 1.2M-member figure both point
  to 1945.
- **Kang Sheng's culpability:** the deaths of the four cadres in the 1937–38
  Soviet purge are well attested; how far Kang personally engineered particular
  cases rests on post-1980 testimony — said so in the note. Kang expelled
  posthumously 1980, ashes removed from Babaoshan.
- Loaded partisan voice (section 3) rendered faithfully; verdicts in the notes.

### Apparatus
- **62 footnotes** (book-wide 265), high density per the standing directive:
  glossed every non-obvious person/place/institution/event at first appearance,
  cross-referenced (not re-noted) figures already covered in ch01/ch02 (Chiang
  Kai-shek, the Central Special Branch, Whampoa, Zhou Enlai, Mao Zedong, He Long,
  Li Kenong, Kang Sheng, Pan Hannian, Li Lisan, the Long March, April 12 coup).
- **+100 glossary rows** (326 referents total): all decided pinyin except 塞先佛
  provisional. Reused decided forms (He Long, Zhou Enlai, Chiang Kai-shek, Kang
  Sheng, Li Kenong, Liu Ding, Mao Zedong, Wang Shiying, Chen Kehan, Luo Qingchang,
  Pan Hannian, Zhang Suzhen, Li Yimang). authority.json confirmed Zhang Xueliang,
  Hu Zongnan, He Long. NOT re-noted (already placed): the recurring figures above.

### Checks (all green)
- parity 125=125; verify_unit numbers 0 unresolved; check_content 340 name
  occurrences, 0 displaced; check_align OK (median 4.55 en/han, no stray);
  qc_entities 0 misses (census: 陈养山×69, 康生×63, 西安×51 …); check_apparatus
  0/0; check_register --ref ch01 within tolerance (em-dash 0.0/1k; dialogue-light,
  judged on narratorial signals).
- data/noise.txt extended: 一〇七 (107th Div numeral misparse), 七尺 (seven-foot
  idiom), 七贤庄 (Qixianzhuang), 一打二拉 (Wang-Ming idiom), 立三路线 (line label),
  120万 / 100万 / 1亿 (arabic+万/亿 magnitude splits, carried in English prose).
  The 四人 count (母子四人) was carried in English ("four in all"), not noised.
- Build: qa_epub PASS (265 refs/bodies/backlinks); **epubcheck 5.1.0 = 0/0/0.**

## Batch 3. Chapter 2, sections 4–5 (ch02s04–s05; PDF 69–92, printed 58–81)

The Red Squad's assassinations (Luo Yinong's informers He Jiaxing, the enemy
agent Dai Bingshi, the spy Chen Weinian, the traitors Bai Xin and Huang Dihong)
and the Chongqing news-agency episode of the "Three Chens."

- **Unit model.** Appended sections 4–5 (two `### ` titles + five `#### ` numbered
  case headings) to the SAME `out/ch02_reading.md`; the whole chapter is one
  builder unit. ch02 reading file now 321 lines; 142 new body/{v} parity lines.
- **data/zh regeneration.** `data/zh/ch02.txt` (sections 1–3) is gitignored and
  did NOT survive the fresh checkout, so whole-`ch02` parity via the default
  config can't be run without regenerating sections 1–3. Per HANDOFF, scoped the
  structural checks to the rebuilt unit: `data/zh/ch02s45.txt` (sections 4–5
  source) + `out/ch02s45_reading.md` (a slice of the appended English) + a scoped
  `data/check_config.b3.json` mapping unit `ch02s45`. The slice is verbatim the
  appended part of `out/ch02_reading.md`. Register/build/qa/epubcheck run on the
  WHOLE chapter file (no zh needed); apparatus anchors validated against the whole
  file.
- **OCR.** Rendered/cropped 69–92 with the ch01/ch02 crop, per-parity bottom
  (recto/even `--bottom 0.945`, verso/odd `--bottom 0.915`, `--running-head
  秘战英雄陈养山`); `ocr_dual.py` for the disagreement filter. `pgrep -c
  tesseract` = 0 after every run. data/zh hand-assembled from corrected OCR +
  every page image read by eye; portrait bio-boxes and photo captions kept OUT of
  data/zh (they are figure captions, in figures.json) so parity stays 1:1.
- **Dropped-tail trap CONFIRMED.** p80 (end of the Chen Weinian episode): OCR
  dropped the paragraph-final short line 冰棒"……; restored from the scan. Every
  page bottom checked against the image.
- **Crop-verified names/readings** (OCR form on the left was WRONG): 刘鼎 Liu Ding
  (OCR 刘易, the "Hart Road hospital" operation), 陈慰年 Chen Weinian (OCR 陈奈年
  throughout — confirmed 慰 on p80), 白鑫 Bai Xin (OCR 白侈/白佬/白奢/白夺/白钨),
  彭湃 Peng Pai (OCR 彭涯/彭涛), 谭余保 Tan Yubao, 红色恐怖队 (OCR 红色信怖队),
  恽代英 Yun Daiying (OCR 履代英), 镣铐 (OCR 镀铸), 袭击 (OCR 黎击), 五卅 (OCR 五州),
  温嗣翔/李鸿混 (given provisional — characters doubtful in the scan).
- **Figures (5; find_figures + eyeballed EVERY page).** find_figures found exactly
  the 5 real plates (p73 Luo Yinong portrait, p81 Peng Pai portrait, p82 the
  puppet Shanghai police HQ building, p89 Chen Yangshan & Chen Kehan, p90 Chen
  Kehan in the 1950s); no line art or document plates elsewhere (OCR ran clean and
  ungarbled on every other page). Portrait bio-boxes translated into the figure
  captions; alt text carries NO straight double quotes.
- **The book's own footnote.** p88 carries the author's numbered footnote ① on
  陈昌 (Chen Chang); reproduced as our translated footnote, attributed to the book.
- **Source errors rendered as printed + footnoted** (do NOT "fix"): the Peng
  Pai / Yang Yin arrest is printed "1928年8月24日" but fell on **24 Aug 1929**
  (execution at Longhua 30 Aug 1929; the book's own later "1929年9月14日" news item
  confirms 1929) — footnoted, corroborated against standard Party-history accounts
  and the Bai Xin-informer record; the "几千万" (tens of millions) slaughtered in
  the 1927–28 white terror is authorial hyperbole (actual toll in the hundreds of
  thousands; CCP membership then under 60,000) — rendered faithfully, footnoted.
- **Bai Xin killing corroborated**: shot by the Red Squad the night of 11 Nov 1929
  at Hehefang off Route Joffre (now Huaihai Middle Rd) — matches the account;
  footnoted.
- **Notes / glossary / figures.** +24 footnotes on ch02 (unit total 130; book-wide
  203). Most section-4/5 subjects (Luo Yinong, Peng Pai and the four martyrs, Bai
  Xin, Dai Bingshi, Chen Weinian, Huang Dihong, Yang Jianhong, Xu Enzeng, Tan
  Shaoliang, Whampoa, Wang Genying, Shen Bao, the Red Squad, the Special Branch,
  the Communist University of the Toilers of the East, the Songhu Garrison Command)
  were ALREADY noted at first appearance in earlier batches — cross-referenced,
  NOT re-noted. +83 glossary rows (226 referents total). NOT re-noted (already
  placed): the traitors as a group, the Special Branch, the Red Squad, Whampoa,
  Sun Yat-sen, the four-martyr group. Minor unfootnoted tier: bit-part bodyguards
  and patrolmen (Han Yunxiu, Lin Hanchen, Wang Baoyuan, Fan Zhengluo, Wang
  Rongchuan), the Red Squad member roll, one-off local officials (Yuan Jiapei,
  Huang Yingqian, Li Honghun, Li Jiemin) — glossary rows only.
- **Style: em-dash discipline.** First English draft over-used the dashed-in
  appositive gloss (failure mode #1: 36 em dashes). Rewrote 25 of them as parens /
  commas / colons / periods per the contract; only the interrupted-speech dash
  ("Ice po—") remains. em-dash rate now 0.1/1k, matching the frozen ch01 reference.
- **Checks (all green).**
  - Parity: ch02s45 142 source = 142 translation.
  - Numbers: `verify_unit.py ch02s45` 142 pairs, 0 unresolved (noise extended:
    10万, 百步穿杨, 百炼成钢, 三民照相馆, 万县, 一九三〇, 零乱; the "four martyrs"
    fixed in English, not noised).
  - Content (displacement): 359 name occurrences, all in the paired paragraph.
  - Alignment: median ratio 4.32 en/han, no pair strays > 2.2x.
  - Entities: `qc_entities` 0 misses.
  - Register vs ch01: within tolerance (contr 14.3/1k, em-dash 0.1/1k, rhythm 0.54).
  - Apparatus: `check_apparatus` 0 failures / 0 warnings (all 130 anchors resolve).
  - Build: qa_epub PASS (203 refs = 203 bodies = 203 backlinks); **epubcheck 5.1.0
    = 0 fatals / 0 errors / 0 warnings**.
- **Tail verified** against the scan (p92): the 1987 recollection closing the
  chapter (50多年前; Chen Kehan; Chen Chang tormented to death 1960, rehabilitated
  1981) reads faithfully.

## Batch 2. Chapter 2, sections 1–3 (ch02s01–s03; PDF 39–68, printed 28–57)

The heart of the book: the birth of the Central Special Branch, the Chen
Yangshan / Bao Junfu double-agent bond, and the Chen Geng / Chen Yangshan
Tianjin operation.

- **Unit model.** The builder reads ONE reading file per chapter
  (`out/ch02_reading.md`); ch02 is split across batches, so this file now holds
  sections 1–3 (three `### ` section titles from book.json) with the chapter's
  three intro paragraphs before section 1. B03 will append sections 4–5 to the
  SAME `out/ch02_reading.md` and `data/zh/ch02.txt`. check_config maps the unit
  id `ch02` to both. 169 source paragraphs, 169 translation paragraphs.
- **OCR.** Rendered/cropped 38–68 with the ch01 crop (recto `--bottom 0.945`,
  verso `--bottom 0.915`, `--running-head 秘战英雄陈养山`); `ocr_dual.py` for the
  disagreement filter. `pgrep -c tesseract` = 0 after every run. data/zh
  hand-assembled from corrected OCR + scans, portrait bio-boxes and photo
  captions kept OUT of data/zh (they are figure captions, translated into
  figures.json) so parity stays 1:1.
- **Crop-verified names/readings** (dual-OCR disagreement + eye on the scan;
  the OCR forms on the left were WRONG): 刘鼎 Liu Ding (OCR 刘易/刘里),
  徐恩曾 Xu Enzeng (徐恩兽/徐四曾), 钱大钧 Qian Dajun (钱大钩), 熊瑾玎 Xiong Jinding
  (能瑾末), 张克侠 Zhang Kexia (张殉侠) and 何基沣 He Jifeng (何基汗); the
  Northwest-Army pair, distinct from the traitor 张克云 Zhang Keyun (张开运),
  鞠华 Ju Hua (misprinted 葛华 once in the narrative; the letter and court address
  read 鞠), 胡鄂公 Hu Egong, 杨登瀛 Yang Dengying, 陈彭年 Chen Pengnian (our agent,
  died on the Long March) vs the traitor 陈慰年 Chen Weinian, 俞同良 Yu Tongliang,
  殷鉴 Yin Jian (曾 is the adverb "had", not part of the name), 周仲英 Zhou Zhongying,
  茅乃功/茅功 (one man, two printed forms). Also restored a silently-dropped tail
  ("于是陈赓让鲍君甫去英捕房活动。", p56) and read 一片荒凉 (not "salt", p64).
- **Source errors rendered as printed + footnoted** (never silently fixed):
  李一氓(又名李坤泰); 李坤泰 is actually the birth name of 李一超/赵一曼, not of
  Li Yimang; 武和景 for 武胡景 (Wu Hujing); Yang Jianhong's death given as suicide
  (自杀, p52) then as execution (被处死, p54); Bao Junfu's own 1951 deposition
  dates his Party tie to 1926 and claims Party membership, going beyond the
  narrative (which treats him throughout as a non-Party agent from 1928); the
  concession car "驶出国民党中央巡捕房" (the concession police were not in fact
  Nationalist-run). Each carries a note.
- **Figures: 15.** Zhou Enlai portrait (p40, missed by find_figures), Pan Hannian
  + Kang Sheng portraits (p41), the "Three Heroes of Longtan" triple photo (p44),
  Chen Shouchang (p45), Bao Junfu (p46), Chen Lifu (p47), the over-street-building
  photo (p51), Xu Enzeng (p52), Huang Molan (p57), the Gu Shunzhang defection
  record; a vertical traditional-character document table, MISSED by find_figures
  (p58), Chen Geng (p61), Wang Genying (p62), Liu Shaobai (p63), Yang Xianzhen
  (p65). Portrait bio-boxes translated as the figure caption. The chapter-opener
  frontispiece (p38, two soldiers) was SKIPPED, matching the ch01 decision to
  omit opener photos.
- **Notes: 106** (book-wide continuous total now 179). Matches the ch01 density
  directive: every non-obvious person/place/institution/event/period-term glossed
  at first appearance, each note saying more than the name, with fact-check
  verdicts where a claim is checkable (Kang Sheng's later persecutions, Pan
  Hannian's 1955 fall, the source errors above). Already-noted ch01 recurring
  subjects NOT re-noted: Zhou Enlai, Chen Geng, Bao Junfu, Gu Shunzhang, Ren
  Bishi, Li Weihan, Qu Qiubai, Li Lisan, Chiang Kai-shek, Wang Jingwei, the May
  Thirtieth / May Fourth movements, the August 7 Conference, the Nanchang
  Uprising, Whampoa, Zhang Zuolin, the Northern Expedition.
- **Glossary: +102 rows** (143 referents total), all with `section` fields.
  Decided renderings fed to authority.json at completion.
- **Checks, all green.** parity 169=169; check_numbers 0 unresolved (noise
  extended: 四川, 20世纪, `[0-9]0年代`, 十足, 涕零, 一二八, 九一八, 两家话, 第二天);
  qc_entities 0 misses; check_content 0 displaced (fixed 3 real/redundant drops:
  Shanghai ×2, Zhang Daofan; and renamed the colliding glossary key
  中国青年 → 《中国青年》 so it no longer matches inside 中国青年团); check_align OK
  (median 4.54 en/han, no strays); check_apparatus 0/0; check_register within
  tolerance of the frozen ch01 reference (em-dash 0.1/1k vs ref 0.6; dialogue
  contraction metric noisy per the reportage caveat); check_style_freshness all
  layers FRESH. verify_unit ch02 green. qa_epub PASS; **epubcheck 5.1.0 =
  0 fatals / 0 errors / 0 warnings.**
- **Builder patch (do-not-revert).** `build_reading_epub.sec_nav`: the EPUB nav
  now OMITS pending (untranslated) sections/subsections instead of linking them
  to the bare chapter file. A partially-translated chapter otherwise put a link
  to the top of the document AFTER a link to a later anchor in the same file
  (epubcheck NAV-011, toc not in reading order), and a `<span>` leaf is invalid
  in a toc nav (RSC-005). The contents.xhtml PAGE still shows the whole shape,
  pending entries and all. Exposed by ch02 being the first chapter translated a
  batch at a time.
- **Figure-alt hazard fixed in data, worth knowing:** a figure `alt` string is
  written into an `alt="..."` attribute with `esc(quote=False)`, so a straight
  double-quote inside alt text breaks the attribute and makes the XHTML
  unparseable (epubcheck RSC-016 fatal, then a cascade of phantom "missing
  anchor" reports). Keep figure `alt` free of `"` (use single quotes); caption
  text may keep double quotes (it is element content, typographized).

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
- **HUMAN GATE outcome:** commissioner approved the voice, and asked for much
  higher footnote density ("explain the names and places and all that... just in
  case there's a gap," but no padding). Applied: ch01 notes 24 -> **73** (glossed
  every non-obvious person/place/institution/event/term at first appearance,
  each saying more than the name). Recorded as a standing note-density RULE in
  STYLE.local.md for all future batches. Rebuilt: qa PASS, epubcheck 0/0, all
  73 anchors resolve. Awaiting confirmation, then freeze as register reference.
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
