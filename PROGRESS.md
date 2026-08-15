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
