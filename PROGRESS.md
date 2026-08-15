# PROGRESS — The Sword Roars in the West Wind (剑吼西风：中央特科纪事)

The running per-batch log. Written as we go.

## Setup / Survey (this session)

- Source: image-only PDF scan, 350 pages, no text layer. `source.pdf` (73 MB).
  Front cover is an oil painting (kept as the ebook cover, `data/figs/cover.png`,
  extracted byte-identical from PDF p1). Back cover carries the blurb and
  ISBN 978-7-5155-2038-4. Publisher Gold Wall Press (金城出版社), Beijing;
  1st ed. 2021.6 (this scan is the 2022.3 6th printing). 390,000 characters,
  22 print sheets. CIP subject: CCP intelligence / security work, 1927–1935.
- Script/orientation: **simplified Chinese, horizontal** (verified by cover and
  OCR). OCR model: `chi_sim`, `--psm 6`. (chi_sim + chi_sim_vert packs installed.)
- **Page offset: constant 15 across the ENTIRE book (printed = pdf − 15).**
  Verified at every one of the 15 chapter openers plus References and Afterword
  by OCR-reading the folio band of all 335 body pages. No unpaginated plate
  inserts anywhere; no drift. This is an unusually clean scan. The preface runs
  a SEPARATE roman-numeral sequence (pdf 6–10 = i–v); the TOC is pdf 11–15.
- Front matter map: p1 front cover (painting), p2 back cover, p3 title page,
  p4 CIP/copyright, p5 epigraph (He Zhu 六州歌头, source of the title 剑吼西风),
  p6–10 preface (前言 历史不能被妖魔化), p11–15 table of contents.
- Structure: 15 chapters, two levels (chapter + numbered 一/二/… sections),
  86 sections total. Plus authorial Preface (front), and Works Cited (参考文献,
  printed 323) + Afterword (后记, printed 333) as back matter. Full structure,
  every opener's pdf_page/printed_page, in `book.json`. `pdf_end` 350,
  `printed_end` 335.
- Style contract composed: `STYLE.md` (zh + nonfiction layers), `STYLE.local.md`
  seeded. Voice target: first-rate popular narrative history for a general reader.
- Skeleton EPUB built: `out/sword-roars.epub`, full hyperlinked TOC (112 links,
  deep to every section), original cover embedded. `qa_epub.py` PASS;
  **epubcheck 5.1.0 clean (0 errors / 0 warnings)**.
- Figures: NOT yet detected. There may be inline photographs on numbered pages
  (offset is constant, so no separate plate section). Run `find_figures.py`
  per batch and eyeball for line art; the cover is handled.
- Survey delivered to the commissioner; awaiting approval of shape + batching
  before Batch 1 (Chapter One, the voice-gate frozen reference).

## B01 = Chapter One "不知掩饰，不知生存 / No Concealment, No Survival" (voice gate)

**Scope:** ch01, PDF 16–49, printed 1–34, four sections (ch01s01–s04). Done end
to end; held at the human voice / note-density / formatting gate (Step 0c).

### Pipeline
- Rendered 16–49 @300dpi. **Crop measured for THIS book:**
  `--left 0.06 --right 0.95 --top 0.11 --bottom 0.955 --lang chi_sim --psm 6`
  (folio + running head are one TOP band; no running foot). No tesseract
  orphans (`pgrep -c tesseract` = 0 after each run). `ocr_dual.py` run for the
  name/number disagreement signal.
- **Tooling fixes this batch — DO NOT REVERT:**
  - `scripts/indents.py`: it called a non-existent `ocr_crop.folio_present` and
    assumed a *bottom* folio; this book's furniture is at the TOP. Rewrote
    `line_starts` to drop furniture bands by y-position (constants
    `FURNITURE_TOP=0.11`, `FURNITURE_BOTTOM=0.955` = the OCR crop).
  - `scripts/check_numbers.py`: added an **arabic+万 combiner** ("31万"=310,000,
    "2.6万"=26,000) that runs BEFORE the noise loop (the built-in `\d+[．.、]`
    list-marker rule was eating the "2." of "2.6万" → phantom 6万=60,000).
    Regression fixtures still green.
  - `scripts/check_content.py`: `name_map` now skips `_`-prefixed doc keys /
    non-dict sections (it choked on the glossary's `_about` string).
- **data/zh/ch01.txt is a HAND TRANSCRIPTION of the scans, not OCR output.**
  Character-level OCR was too noisy and `assemble.py`'s positional
  indent↔OCR-line zip breaks on this book's many figure pages and the
  decorative chapter opener (tesseract's line count diverges from the geometric
  band count there). The source side was read off the scans directly, one
  paragraph per line, parity-guaranteed, every name/number cross-checked
  against the dual OCR and (for hard cases) magnified crops.
  **Reproducibility caveat, raised at the gate:** `data/zh/` is gitignored
  (copyright), so the default regenerate-from-OCR path will NOT reproduce this
  file; the tracked deliverable (`out/ch01_reading.md`, apparatus, EPUB) is
  complete regardless. Decision on whether to track `data/zh` for this book is
  the commissioner's.

### Checks (all green)
- Parity 165 = 165 (`check_structure --pairs`, `verify_unit`).
- Numbers: `check_numbers --noise data/noise.txt` 0 unresolved / 165 pairs.
  `data/noise.txt` extended: event-date names read as one numeral (七一五, 五二〇,
  二七, 八七, 六一, 五四), numeral-bearing names (李立三, 张阿四, 肖阿四, 马万祺),
  decade labels (20世纪/20年代), idioms (百般, 四通八达, 万岁, 九腔十八调, 成百,
  风情万种, 海纳百川, 两手, 万恶, …). Every entry commented.
- `check_align` median 4.98 en/han, no pair > 2.2×. `check_content` 203 name
  occurrences 0 displaced. `qc_entities` 0 misses. `check_apparatus` clean.
  Builder anchor gate green (it caught 2 anchors orphaned by voice-gate edits;
  fixed).
- Tail verification: closing paragraphs of every section re-read against the
  scan. Crop-verified: Red Squad roster (谭忠余/张阿莲/张文虎/张文龙 p20), the
  南昌决裂 reading (as printed; footnoted), casualty figures 31万/2.6万 (p31),
  addresses 22号/679号.

### Apparatus
- **115 footnotes** (`notes.json`): first the 52-note base (figures, events,
  institutions, idioms, quotations a non-specialist needs, first-appearance
  anchored, fact-check verdicts where checkable: the 310,000 purge-deaths as the
  Party's own Sixth-Congress reckoning; Wakeman = 魏斐德; the Latin maxim = the
  chapter-title source); then **+63 notes for the commissioner's density
  request** (`data/ch01_notes2.json`, merged), closing every place / reference /
  minor-figure gap a reader with no China background would hit. The trigger was
  explicit: the six Shanghai pleasure-houses ("Tower-Beyond-the-Tower … the
  Great World") of which the reader knew two, now all glossed in one note. The
  new batch sweeps: the venues and the amusement-arcade world; classical
  conjuring (baixi, the Seven Sages); the department stores and Shen Bao; the
  Green Gang; the three Shanghai workers' uprisings; the concession/settlement
  geography that the whole book turns on; the warlords and revolutionaries named
  in passing (Lu Diping, Zhang Jingyao, Cheng Qian, Tang Shengzhi, Zhang Zuolin,
  Yuan Shikai, Li Yuanhong, Feng Yuxiang, Bai Chongxi …); the Party congresses
  (Third, Fifth, Sixth) and bodies (Youth League, Comintern, CPPCC/NPC, Southern
  Bureau); the 1927 Politburo roster; institutions (Tongmenghui, Tōa Dōbun
  Shoin, Naigai, Cihai, People's Daily); the White-Terror enforcers and the
  White/Soviet-areas vocabulary; allusions (Lord Chunshen, Zhuge Liang, Patrick
  Henry); and the shikumen/tingzijian/xiaokai material culture. All 63 anchors
  verified unique and non-nesting against the 52 already placed; numeric refs
  only; `check_apparatus` clean, builder anchor gate green, `qa_epub` PASS,
  epubcheck 0/0.
- **12 figures** (`figures.json`) with real alt text; `find_figures` MISSED the
  Shen Bao ad-clippings (dense newsprint) and the org chart (line art) — cropped
  by hand (`data/figs/ch01-*.png`). The faded photo behind the p16 chapter title
  is treated as design furniture, NOT a captioned figure.
- Glossary: principal cast + recurring names/orgs/terms; `authority.json` to be
  updated on completion.

### Voice gate (Step 0c) — blind-critique loop
- Round 1 (context-blind reader): ~40 findings; applied 33, kept the deliberate
  正面/背面 parallelism and the Mao/Lu Xun/couplet quotations (load-bearing, the
  blind reader couldn't see them). Six RULE/WHY/FIX/CHECK classes folded into
  `STYLE.local.md`.
- Round 2: opened "polished, high-accomplishment… mostly real English"; ~44
  further fixes (garbled-logic, remaining calques, doubled synonyms, purple);
  apparatus "read clean." Two more rules added to `STYLE.local.md`.
- Round 3: convergence check (running / done — see HANDOFF).
- On approval this chapter is the FROZEN register reference
  (`check_register.py --ref out/ch01_reading.md`).

### Setup-report note
- `tests/run_tests.py`: one FAIL, "hook stands down on template stub" — benign
  (the survey already put a real kickoff in HANDOFF.md, so the Stop hook
  correctly ENFORCES rather than standing down). Not a regression.

### NOT re-noted (already placed) — for later batches, cross-reference don't re-note
- Gu Shunzhang, Chen Geng, Zhou Enlai, the Central Special Branch, the Red
  Squad, Chiang Kai-shek, Yang Du, Pan Hannian, Li Dazhao, Du Yuesheng, the
  Whampoa Academy, the May Thirtieth Massacre, the Great Revolution / party
  purge, the "ten years of turmoil", Wakeman, Zhang Guotao, Xu Enzeng, Dong
  Jianwu, Qu Qiubai, Li Qiang, Mei Baoji, Mei Gongbin, the Nineteenth Route
  Army, Song Qingling — all first-noted in ch01.

## B02 = Chapter Two "清者自清，浊者自浊 / The Clean Stay Clean, the Foul Stay Foul"

**Scope:** ch02, PDF 50-59, printed 35-44, two sections (ch02s01 一、英雄阳刚 /
"A Hero's Mettle"; ch02s02 二、流氓无产者 / "The Lumpen Proletariat"). Done end
to end. 56 body paragraphs.

### Pipeline
- Rendered 50-59 @300dpi. Crop as B01:
  `--left 0.06 --right 0.95 --top 0.11 --bottom 0.955 --lang chi_sim --psm 6`.
  `ocr_crop` + `ocr_dual` run; `pgrep -c tesseract` = 0 after each.
- **Folios verified off the scan at every page:** pdf 50 = chapter opener
  (decorative, faded photo behind the title, NO printed folio = printed 35);
  pdf 52-58 read 037-043; **offset holds at a constant 15, no drift** (matches
  book.json / B01).
- **data/zh/ch02.txt is a HAND TRANSCRIPTION** off the scans (same reason as
  B01: OCR too noisy, assemble misaligns on the figure-heavy pages 52-53 and
  the opener). Parity-guaranteed, one paragraph per line, every name/number
  cross-checked against dual OCR and magnified crops. (data/zh gitignored;
  reproducibility caveat as B01.)

### Crop-verified readings (names/numbers)
- **约翰·拜伦、罗伯特·帕克 = John Byron and Robert Pack** (NOT "Baolun/Park"):
  authors of *The Claws of the Dragon: Kang Sheng* (1992; Chinese tr. 1998).
  The crop caught 拜 (Byron) mis-first-read as 豹. Western scholars, own names.
- **史曜宾 (Shi Yaobin) and 史砚芬 (Shi Yanfen) are TWO DIFFERENT people**,
  both in the source: Shi Yaobin = the Yixing county-committee secretary
  (p51); Shi Yanfen = uprising vice-commander and the martyr executed at
  Yuhuatai 1928 (p52-53). Rendered as printed; footnoted the distinction.
- Verified: 宗孟平/宗益寿/宗颖/吴丹枫/宗文斌, 匡亚明/洁玉/匡世, 荆溪, 史曜宾,
  李旸谷, 宗盘林, 宗道章, 万益, 段炎华, 蒋三大, 严朴, 后塍, 英举, 赵和, 宗益茂,
  官林, 李凯, 罗青长, 薛岳, 蔡孟坚, 杨之华/杏花/文君/杜宁. Numbers:
  6支部/39党员, 502工会/82万会员/3000党员, 五十多万, 12时, 十三村镇 all crop-clean.
- **杜宁 (Du Ning) is Yang Zhihua's pen name** (the p58 citation uses it);
  footnoted so the reader does not take it for a separate authority.

### Checks (all green)
- Parity 56 = 56 (`check_structure --pairs`, `verify_unit`).
- Numbers: `check_numbers --noise data/noise.txt` 0 unresolved / 56 pairs.
  `data/noise.txt` extended (commented): idiom-numerals 十足 / 万能 / 两肋;
  the approximate quantity 五十多万 (= "over 500,000", rendered in full, listed
  so the generic 十多 rule does not fragment it and orphan 万=10000); and the
  name-numerals 万益 (surname 万) and 蒋三大 (三). 中午12时 rendered "twelve noon"
  so the 12 is carried.
- `check_align` median 5.10 en/han, no pair > 2.2x. `check_content` 45 name
  occurrences, all in the paired paragraph. `qc_entities` 0 misses (incl. the
  14 new glossary rows). `check_apparatus` clean.
- **Register vs frozen ch01** (`check_register --ref out/ch01_reading.md`):
  within tolerance. Dialogue-contraction metric QUIET (this chapter is quoted
  meeting-records + citations, little scene dialogue) — judged on the
  narratorial signals (em-dash 8.7/1k vs ref 8.2; rhythm CV 0.59 vs 0.67;
  sent median 23), all in range.
- Tail verification: closing paragraphs (p58, the 顾顺章 blood-and-iron coda)
  re-read against the scan; faithful, nothing invented.
- Build: cumulative EPUB rebuilt (2/18 chapters, 143 notes). `qa_epub` PASS
  (49 files, all links resolve). **epubcheck 5.1.0 clean (0/0).**

### Apparatus
- **28 footnotes** (`data/ch02_apparatus.json` -> notes.json). Coverage:
  the chapter-title proverb; the Aug 7 Conference and Autumn Harvest Uprising;
  Jiangnan geography; the 节孝祠 shrine; Shi Yanfen (martyr + the Shi Yaobin
  distinction); the Relief Society (济难会 / Red Aid); Chen Yun; the KMT 自首
  surrender policy; the Mencius three-cannots and the "受屈…知君子" maxim; Mao's
  1945 "On Coalition Government" line and his 1925 class-analysis essay; the
  five Shanghai leaders (Chen Duxiu, Peng Shuzhi, Luo Yinong, Zhao Shiyan,
  Wang Shouhua) with fates; the Shanghai Provisional Municipal Government; the
  Northern Expedition; "C.P."; the Shanghai General Labor Union; the lumpen-
  proletariat concept; the secret societies (Triads/Gelaohui/Big Sword/
  Zailihui/Green Gang); Nanyang Brothers Tobacco; Byron & Pack; Cai Mengjian;
  Yang Zhihua/Du Ning; Xue Yue; the Green Gang initiation hall. Fact-checks
  corroborated against Party and Western sources (Shi Yanfen, the Byron/Pack
  book, Cai Mengjian's 1931 capture of Gu, the Provisional Municipal Govt).
- **5 figures** (`figures.json`, hand-cropped from the scans, real alt text):
  portraits of Zong Mengping, Kuang Yaming, Yan Pu (p52) and Chen Yun (p53),
  and the group photo of Gu Shunzhang at the Provisional Municipal Government
  (p55). `find_figures` not relied on. The full-page faded painting on **pdf 59**
  (no folio, no caption) is treated as design furniture, NOT a captioned
  figure (as with the ch01 chapter-title photo).
- **14 new glossary rows** (people: Zong Mengping, Kuang Yaming, Shi Yanfen,
  Chen Yun, Chen Duxiu, Peng Shuzhi, Luo Yinong, Zhao Shiyan, Wang Shouhua,
  Cai Mengjian, Xue Yue, Yang Zhihua; orgs: Nanyang Brothers Tobacco, Shanghai
  General Labor Union). All `attested`. (apparatus_merge places rows at top
  level; MOVED into people/organizations sections by hand, else the builder's
  render_glossary chokes on a flat row — noted for next batch.)

### NOT re-noted (already placed in ch01) — cross-referenced, not re-noted
- Gu Shunzhang, Zhou Enlai, the Central Special Branch, the Red Squad, the
  "dog-beating"/"beating the dogs" usage, the Third/Action Section, Chiang
  Kai-shek, the May Thirtieth, the three Shanghai workers' uprisings, the
  soviet/White-areas vocabulary, Qu Qiubai, Du Yuesheng, the Green Gang
  (青帮; the initiation-hall custom is newly noted), Wakeman, Zhang Guotao,
  Xu Enzeng, the April 12 coup / party purge, the Comintern.

### Tooling notes (do not revert)
- `data/noise.txt`: see the ch02 block appended at the end (idiom/name/quantity
  numerals). Every entry commented; longest-literal-first respected.
- `apparatus_merge.py` writes glossary rows at the JSON top level; they must be
  moved into the correct section (people/organizations/...) or the builder
  fails at render_glossary. Figure `file` fields must be BASENAMES only
  (builder prepends data/figs and images/); a "data/figs/..." prefix breaks
  qa_epub with a missing-image path.
- `check_structure.py --config` cannot run a whole-book parity pass on a fresh
  checkout because data/zh/ch01.txt is gitignored/absent; per-unit
  `--pairs data/zh/ch02.txt out/ch02_reading.md` was run instead (OK).

## B03 = Chapter Three "谁是犹大 / Who Is Judas" (ch03)

- **Scope:** PDF 60-81, printed 45-66. Seven sections ch03s01-s07. Offset held
  at a constant 15 (folios 045-066 read off the scan at every opener; no drift).
  The chapter turns from the moral contrast of ch02 to the hunt for a traitor:
  the betrayal, arrest, and execution of Luo Yinong (罗亦农) in April 1928, and
  the Special Branch reprisal on the informers He Zhihua (贺稚华) and her husband
  He Jiaxing (何家兴).
- **Source recovery.** OCR (chi_sim, psm 6, crop 0.06/0.95/0.11/0.955) was noisy
  on the proper names as expected (夏禹奎 came out four different ways), so
  `data/zh/ch03.txt` was hand-transcribed from the page images and cross-checked
  against the dual-OCR read, exactly as for ch01-ch02. Parity is exact: **146
  source paragraphs = 146 translation paragraphs** (7 `###` section headings).
- **Translation:** `out/ch03_reading.md`, one paragraph per source line. Voice
  carried over from the end of ch02 (read first). Real scene dialogue this
  chapter (Luo/Li courtship, the He couple, quoted Deng Xiaoping); differentiated
  per the voice sheets in HANDOFF. The set-off Peng Shuzhi memoir block is a
  `{v}` vignette (one source paragraph, parity-locked).
- **Checks, all green:**
  - parity 146=146 (`check_structure --pairs`).
  - numbers: `check_numbers --noise` 0 unresolved. Caught one real error mid-draft
    (三千或五万 rendered "three or five thousand"; fixed to "three thousand or
    fifty thousand") and the dropped inline citation years, now all restored in
    the ch02 "(Author, YEAR)" style. Also carried 八人 "eight", 二楼 "second-floor",
    两家 "two households", 上海 "Shanghai" where first drafted loose.
  - align OK (median 4.46 en/han, no pair strays > 2.2x).
  - content displacement OK (370 name occurrences, all in the paired paragraph).
  - entities: `qc_entities` 0 misses (Li Zheshi named once in two grief
    paragraphs where pronouns had carried her; He Jiaxing named in the 何家兴夫妇
    paragraph).
  - register vs the FROZEN ch01 reference: within tolerance. The dialogue
    contraction rate is 6.0/1k against ch01's 0.3/1k (20x), but this is the
    expected signal, not drift: ch01 is nearly dialogue-free and ch03 carries
    real scene dialogue (the register-drift caveat for reportage). Narratorial
    signals (em-dash 0.0/1k, rhythm CV 0.68 vs 0.67, sentence median 20) sit on
    the reference. Metric noted as expected, not a flag.
  - `check_apparatus` 0/0; qa_epub PASS (176 refs/bodies/backlinks); epubcheck
    5.1.0 clean (0 fatals / 0 errors / 0 warnings).
- **Footnotes: 33 new** (unit total 33). Coverage swept across the four domains:
  people first-introduced (Luo Yinong, Zheng Chaolin, Zhu De, Zhu Min, Deng
  Xiaoping, Kang Sheng, Zhang Zuolin, Qian Dajun, Yang Dengying/Bao Junfu, Hu
  Jintao, Chen Yannian, Xia Minghan); institutions and places (KUTV, Longhua,
  the Great World, Hardoon Garden, the Mixed Court, the Green and Red Gangs, the
  White Terror, Bolshevik, Bubbling Well Road); material culture and allusion
  (Rue Bourgeat / concession streets, comprador, chaibaidang, Xiang embroidery,
  the Bai Juyi and Li Yu allusions, Lu Xun's Wandering); and the source-critical
  notes (the redacted "奉蒋××令" reproduced as printed; the 夏明翰/夏明瀚 misprint;
  the 贺稚华/贺治华 name variant against Zhu De's letter; the Monte Cristo maxim;
  the unresolved manner of He Zhihua's death, left as the author leaves it).
- **FACT-CHECK / interested-witness.** He Zhihua = the historical 贺治华, Zhu De's
  wife and mother of Zhu Min: corroborated, and footnoted at the Zhu De note.
  Luo Yinong's execution at Longhua (21 April 1928): corroborated. The identity
  of the traitor is contested in the sources the author himself quotes (Zheng
  Chaolin's letter version vs the informer-woman version vs the "who profits"
  reading); the translation renders all faithfully and the notes flag the
  disagreement rather than resolving it. Kang Sheng leading the killing squad:
  uncorroborated, one version only, footnoted as such.
- **Figures: 4** (basenames in `figures.json`, real alt text, translator's
  captions with source-label provenance stated):
  - `ch03-luo-yinong.png`, `ch03-li-zheshi.png` (paired portraits, pdf 63).
  - `ch03-he-zhihua-europe.png` (group photo, He Zhihua front row right-2, pdf 72).
  - `ch03-shanghai-map.png` (old street map locating 178 Rue Bourgeat, pdf 77).
  - The faded chapter-opener montage on pdf 60 (no folio, no caption) is treated
    as design furniture, NOT a captioned figure (as with ch01/ch02 openers).
    `find_figures` not relied on; every page eyeballed.
- **59 new glossary rows** (people, organizations, places, terms), added
  DIRECTLY into the correct sections by a one-shot script (re-read verified),
  not via apparatus_merge's flat top-level write. All `attested`/`decided`.
  李维汉 already present (reused). Key: 李哲时 = Li Zheshi (= 李文宜 Li Wenyi),
  贺稚华 = He Zhihua, 何家兴 = He Jiaxing, 朱德 = Zhu De, 郑超麟 = Zheng Chaolin,
  杨登瀛/鲍君甫 = Yang Dengying/Bao Junfu (the ch04 double agent).

### NOT re-noted (already placed in ch01/ch02) — cross-referenced, not re-noted
- The August 7 (八七) Conference (noted ch02), the Nanchang Uprising (ch01), the
  Green Gang (ch01; the Red Gang is folded into the new Green-and-Red note),
  the tingzijian (ch01), Chiang Kai-shek / Wang Jingwei (ch01), Zhang Tailei
  (ch01; his widow Wang Yizhi is glossed only), the Special Branch / Red Squad /
  "beating the dogs" (ch01), Gu Shunzhang / Chen Geng / Zhou Enlai / Qu Qiubai /
  Chen Duxiu (ch01-ch02).

### Tooling notes (do not revert)
- `data/noise.txt`: ch03 block appended (四川 Sichuan; 三教街 Sanjiao Street;
  化整为零; 一百二十四; 推三阻四; 万籁; 万般; 第二天). Every entry commented;
  longest-literal-first respected. These are place-names and idioms carrying a
  numeral that is not a quantity; no real dropped number was ever noised.
- `data/content_config.json` extended to include ch03 so the displacement check
  covers it (ch01+ch02+ch03).
- Glossary discipline: apparatus_merge STILL writes glossary rows at the JSON
  top level; this batch bypassed that by adding rows straight into the sections
  with a re-read-verified one-shot (deleted after use). Either path is fine;
  just never leave a flat top-level row, which breaks render_glossary.

## B04 = Chapter Four "喋血霞飞路 / Bloodshed on Avenue Joffre" (ch04)

- **Scope:** PDF 82-107, printed 67-92. Seven sections ch04s01-s07. Offset held
  at a constant 15 (folios 068-091 read off the scan at every opener; no drift).
  The double-agent chapter that ch03's ending set up: the arrests at Jingyuanli
  "as if foreknown" (Peng Pai, Yang Yin, Yan Changyi, Xing Shizhen + Zhang
  Jichun, 24 Aug 1929; four shot at Longhua 30 Aug), Yang Dengying/Bao Junfu the
  double agent run by Chen Geng, the failed Fenglin Bridge rescue, Bai Xin's
  betrayal exposed, and the Red Squad's killing of Bai Xin on Avenue Joffre
  (11 Nov 1929). Closes on Zhou Enlai sheltering Yang Dengying in Qincheng
  Prison during the Cultural Revolution.
- **Source recovery.** `data/zh/ch04.txt` hand-transcribed off the page images
  (OCR too noisy on the proper names, as before), cross-checked against the
  dual-OCR read and magnified crops. Parity is exact: **131 source paragraphs =
  131 translation paragraphs** (chapter title + 7 `###` section headings).
- **Translation:** `out/ch04_reading.md`, one paragraph per source line. Voice
  carried from the end of ch03 (read first). Section 7 carries a run of set-off
  block quotations and the **李强日记 (Li Qiang's Diary) 1968-69 entries**, all
  marked `{v}` vignettes (date + entry combined one-per-line; the source's
  abridging "……" kept as its own `{v} ...` line). The White-Russian-café
  set-piece (s03) is rendered at elevation as the author's own descriptive prose.
- **Checks, all green:**
  - parity 131=131 (`check_structure --pairs`, `verify_unit`).
  - numbers: `check_numbers --noise` 0 unresolved. Caught one real slip
    (五位负责人 first drafted "the other four leaders"; fixed to "the five
    leaders, Peng Pai among them"). noise.txt extended with ch04 proper-name
    numerals (百禄里, 五洲, 三民, 三轮车 = Popov's "Tricycle", 八仙桥).
  - align median 4.85 en/han, no pair > 2.2x. content displacement 174 name
    occurrences, all in the paired paragraph (content_config extended to ch04).
  - entities: `qc_entities` 0 misses (top: 杨登瀛 x60, 周恩来 x58, 陈赓 x27,
    董健吾 x14, 鲍君甫 x12).
  - register vs FROZEN ch01: the dialogue-contraction metric is QUIET/flagged
    "STILTED" (0.0/1k), the expected reportage signal for a chapter that is
    almost entirely quoted documents (Zhou Enlai's 1930 proclamation, the
    Comintern report, a memoir/biography stack, and the diary) with only a
    handful of scene-dialogue lines (the Bai Xin/Ke Lin exchange). Judged on the
    narratorial signals: rhythm CV 0.68 vs ref 0.67, sentence median 23, em-dash
    0.9/1k (low, consistent with ch03's 0.0) — all in range. Not real drift.
  - `check_apparatus` 0/0; qa_epub PASS (200 refs/bodies/backlinks); **epubcheck
    5.1.0 clean (0 fatals / 0 errors / 0 warnings).**
  - tail verification: the s07 closing paragraphs re-read against p0106 (printed
    091); faithful, nothing invented.
- **Footnotes: 24 new** (unit total 24). Coverage across the four domains:
  people first-introduced (Peng Pai, Yang Yin, Yan Changyi+Xing Shizhen, Zhang
  Jichun, Bai Xin, An E, Ke Lin, Huang Jinrong, Luo Qingchang; Dong Jianwu
  supplemented from ch01 with the Red-Pastor/Mao's-sons material); institutions
  and places (the Zhongtong lineage via the two Chens, Sun Yat-sen Univ. Moscow
  vs KUTV, St. Peter's vs Grace Church, Avenue Joffre, Qincheng, the Republican
  Daily, the Guangzhou Uprising); texture and reference (Lu Xun's censorship
  opening and "opening a skylight", the North China Daily News, the White
  Russian émigrés, the Internationale, Dusko Popov = "Tricycle"); and one
  source-critical note (the 12-vs-1015 Jingyuanli house-number discrepancy, as
  printed). Fact-checks corroborated against Wikipedia/Baidu/academic/official
  sources (the Peng-Yang-Yan-Xing arrest and execution and Bai Xin's betrayal;
  Popov = Tricycle, MI5/MI6, Bond inspiration — cited to Wikipedia/UK National
  Archives, NOT the Grokipedia hit; An E; Dong Jianwu; Ke Lin).
- **Figures: 10** (basenames in `figures.json`, real alt text, translator's
  captions with source-label provenance stated): four martyr portraits
  (`ch04-peng-pai.png`, `ch04-yang-yin.png`, `ch04-yan-changyi.png`,
  `ch04-xing-shizhen.png`, pdf 85-86), `ch04-yang-dengying.png` (pdf 87),
  `ch04-an-e.png` (pdf 89), `ch04-garrison.png` (the Songhu Garrison Command,
  pdf 92), `ch04-shanghai-map.png` (old street map locating Fenglin Bridge,
  pdf 93 — a full-page figure), `ch04-red-flag-daily.png` (Zhou Enlai's memorial
  front page, pdf 95), `ch04-yang-family.png` (1956 family photo, pdf 102). The
  faded full-page painting on pdf 107 (no folio, no caption) is design
  furniture, NOT a captioned figure (as with the ch01-ch03 openers/closers).
- **62 new glossary rows** (people, organizations, places, terms), added
  directly into the correct sections by a re-read-verified script (not via
  apparatus_merge's flat top-level write). Key: 彭湃=Peng Pai, 杨殷=Yang Yin,
  白鑫=Bai Xin, 安娥=An E, 柯麟=Ke Lin, 董健吾=Dong Jianwu (already present),
  中统=the Zhongtong, 霞飞路=Avenue Joffre, 秦城监狱=Qincheng Prison.

### Source oddities logged (per the typo policy)
- **p0089 (printed 074) prints "白行车" for "自行车" (bicycle).** An evident
  imprint typo (白 for 自); rendered to plain sense "a bicycle." Listed here,
  not footnoted (below the annotation threshold).
- The 静安区委党史研究室 (2016) quote gives "经远里1015号" where every other
  source gives "12号"; both reproduced as printed and the discrepancy footnoted.

### Tooling notes (do not revert)
- **Builder alt-attribute escaping (FIXED this batch):** `build_reading_epub.py`
  emitted `alt="%s"` through `esc()` (which is `html.escape(quote=False)`), so a
  double quote inside alt text (`'Wuhing Road'` was first written with real "")
  produced malformed XHTML and qa_epub/epubcheck reported the WHOLE chapter's
  ids as undefined. Changed that one call to `html.escape(..., quote=True)`.
  Keep it. Lesson: an alt string with a literal `"` is now safe, but prefer
  single quotes in alt text anyway.
- `data/noise.txt`: ch04 block appended (百禄里, 五洲, 三民, 三轮车, 八仙桥),
  every entry commented, longest-literal-first respected. All are proper-name
  numerals rendered romanized; none masks a real dropped quantity.
- `data/content_config.json` extended to include ch04.

### NOT re-noted (already placed in ch01-ch03) — cross-referenced, not re-noted
- The Central Special Branch / Red Squad / "beating the dogs" (ch01); Zhou Enlai,
  Chen Geng, Gu Shunzhang, Xu Enzeng, Kang Sheng (ch01/ch03); the Whampoa Academy
  (ch01); the Green Gang (ch01); Longhua (ch03); the Comintern / KUTV (ch01/ch03);
  the April 12 coup / Great Revolution / White Terror (ch01/ch03); Chiang
  Kai-shek / the Kuomintang (ch01); Nanchang Uprising (ch01); "Judas" (ch03
  title); Yang Dengying/Bao Junfu & Chen Yangshan (ch03); Li Qiang, Dong Jianwu
  (ch01, supplemented here); the tingzijian / shikumen (ch01).
