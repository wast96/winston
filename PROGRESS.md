# PROGRESS — Nameless Heroes (英雄无名), Chen Gongshu

The running per-batch log. One section per batch: units, checks and findings,
notes added, glossary rows, figures, and anything flagged for the read-through.

## Setup / Survey (Step 0)

- **Source EPUB:** the collected 「英雄无名」 (*Nameless Heroes*) tetralogy by
  陈恭澍 (Chen Gongshu), a Nationalist (Juntong) secret-service memoir.
  Digital text, no OCR. Predominantly simplified script with residual
  variant/traditional glyphs (鬪, 価, 値, 鄕) from an imperfect conversion —
  treat as digitization glitches, list them, do not footnote mechanical
  typos.
- **Ingest:** 45 spine documents, 1 image, 624,120 source characters
  (`out/INGEST.md`). The one image is the cover (`data/figs/英雄无名-陈恭澍.png`),
  reused byte-identical.
- **Structure:** 43 of the 45 spine docs modeled as chapters; the source's
  file boundaries mostly match logical chapters, so few merges. EXCLUDED and
  recorded in `book.json` `_source_note`: `Text/cover.xhtml` (→ cover image)
  and `Text/nav.xhtml` (the source's own TOC, superseded by the built one).
  The four constituent books are modeled as four TOC parts, with the front
  prefaces/introductions grouped and the afterword trailing.
- **Source's own apparatus:** NONE. Grepped `data/src/` for `\[\d+\]` — none
  present. No `source_notes.json` stream needed. Re-grep each batch's source
  anyway and record "none present."
- **Running-header quirk:** every content file's first line is the header
  `英雄无名-陈恭澍`. It is page furniture, not text; drop it at translation
  time (do not pair it in the bilingual). 43 files carry it.
- **Faithful numbering gaps (NOT errors):** Part Three skips chapter 7 and
  splits chapter 10 into (上)/(下); Parts Two and Three both carry a chapter
  titled 三面受敌 一往无前. Preserve as-is.
- **Skeleton build:** `build_reading_epub.py` → `out/nameless-heroes.epub`
  (0/43 translated). `qa_epub.py` PASS (56 files, all links resolve).
  epubcheck 5.1.0: **0 fatals / 0 errors / 0 warnings**.
- **Survey:** `out/SURVEY.md` at target ~18,000 chars → 35 batches proposed.
  Total 623,161 chars across 43 chapters, 37 sections, 5 TOC parts.

### Flags for the voice gate / read-through
- **军统 (Juntong) is a live cross-book `reconcile` in `authority.json`**
  (three renderings on the shelf: "Military Statistics Bureau" / "the
  Juntong" / "Juntong"). This book uses it constantly and should settle a
  single rendering at the Batch 1 voice gate, then feed it back.
- Agreed shelf renderings already available: 戴笠 → Dai Li; 汪精卫 → Wang
  Jingwei; 北平 → Beiping; 天津 → Tianjin.
- Part title 河内辱命 rendered provisionally as "Disgrace at Hanoi"; the
  author discusses his own title choices (rejecting 河内刺汪) in the ch10
  preface — worth a translator note there.
- Stray glyphs to resolve in context at translation time: the trailing 杀 on
  the ch22 source title (第二章 春云乍展风雷初动杀); 寿张为幻 in the ch16
  title; 毛酋 ("the Mao chieftain") in a ch36 section title.

## Batch B01 — ch01–ch05 (front matter)

Units: ch01 Foreword ("The Conception of Nameless Heroes"); ch02–ch04 the
author's Introductions to the first three books; ch05 Part One's Prefatory
Note. Expository first-person authorial prose. ~10,589 source chars.

### Checks (all green)
- **Source-note grep (`\[\d+\]`):** none present in any of the five units
  (re-checked per batch, as required). No `source_notes` stream.
- **Parity / verify_unit:** ch01 8, ch02 18, ch03 14, ch04 61, ch05 8 —
  source vs translation paragraph counts equal for every unit. Numbers,
  anchors all pass with `--noise data/noise.txt`.
- **check_align:** all OK; median en/han ratios ch01 5.28, ch02 5.30,
  ch03 4.84, ch04 4.80, ch05 5.12; no pair strays > 2.2x.
- **check_content:** 38 glossary names usable as anchors; 0 displaced across
  all units (ch02 26, ch03 8, ch04 31, ch05 4 name occurrences all in the
  paired paragraph).
- **check_structure:** parity OK; 67 note anchors, 0 unresolved; heading
  shape OK.
- **Tail verification (rule 4 corollary):** final paragraph of every unit
  checked against the source — faithful, nothing invented or dropped.
- **Build:** `out/nameless-heroes.epub` 5/43 chapters, 67 notes, 0 source
  notes. `qa_epub.py` PASS (57 files, 67 refs = 67 bodies = 67 backlinks).
  **epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings.**
- **check_register:** N/A this batch — B01 is the *reference* to be frozen at
  the voice gate; `--ref` checks begin at B02.
- **Blind double-translation (check 7, once/book):** deferred to an early
  *narrative* chapter (B02+); front matter is expository and the human voice
  gate is the calibration for B01.

### 军统 DECIDED → "the Juntong"
Rendered 军统 / 军统局 as **"the Juntong"** throughout (matches the memoir's
own shorthand; reader-friendly). Full name given in the ch04 first-appearance
note: the Bureau of Investigation and Statistics of the Military Affairs
Commission (军事委员会调查统计局), with the 1938-name-for-1932 anachronism
flagged. Recorded in `glossary.json` (organizations, status "decided"). Feeds
back to `authority.json` on completion (resolving the three-way reconcile).

### Structural recovery (ch04)
The ch04 introduction carries five titled sub-sections that the digitization
flattened into plain `<p>` text — three glued to the tail of the preceding
paragraph (另外两部书; 我对「特务工作」的看法; 为什么要「制裁」) and two left as
bare standalone paragraphs (中国模式的「特工」; 为无名英雄留历史纪录). Recovered
as `###` sub-headings via `scripts/clean_batch.py` (which separates the glued
text and verifies the source characters are conserved exactly). This is a
structural recovery, not invented text — every character is the source's. Flag
for the voice gate: confirm this is wanted.

### Digitization glitches (rendered to plain sense; NOT footnoted — mechanical)
- ch02 §5 (source): `殷汝湖` → `殷汝耕` (湖 for 耕; the man is Yin Rugeng).
- ch02 §17 (source `山木荣治`) and elsewhere: `山木` → `山本` (Yamamoto).
- ch03 §5: `说起来真；是千头万绪` — stray full-width `；` after 真.
- ch03 §6: `最有埋据的解答` → `根据` (埋 for 根); rendered "best-grounded."
- ch04 §2: `过度阶段` → `过渡阶段` ("transitional stage").
- ch04 §9: `永辽不会屈服` → `永远` ("never, ever submit").
- ch04 §14: `大冢清先空所嘱` → `先生`.
- ch04 §43: `揍巧挡住了去路` → `凑巧` ("by chance").
- ch04 §51: stray `1364` injected mid-sentence (`结果 1364；没有任何收获`) —
  dropped as junk (noised in `data/noise.txt`).
- ch04 (several): `戴雨农光生` → `先生` (光 for 先).
- ch05 §5: `秘密组织三「军统局」` — stray `三` standing in for punctuation
  (rendered as ";"; the orphaned 三 noised).
- ch05 §6: `第二度` → `第二处` ("Second Department").
- ch05 §7 (source): line 9 `…披荆斩棘建立起来的` lost its terminal `。`
  (rendered with a period).
- Variant/traditional glyphs (not glitches, rendered plainly): `鬪` (=斗,
  "struggle") in ch04 §13/§16.

### Noise rules added (`data/noise.txt`)
九一八, 一二八 (event date-names read as 918/128); decade labels
`[…]、?[…]?十年代`; `[…]十多[万萬]` (三十多万 orphaned 万); 石友三, 毛万里,
姓万 (names with numeral glyphs); idioms 万恶 / 一波三折 / 千头万绪 / 一了百了
/ 千变万化 / 十恶不赦; 组织三 and 1364 (glitches). Republican years are carried
as Gregorian (check_numbers maps year+1911 automatically).

### Notes ledger (67 total: ch01 6, ch02 20, ch03 9, ch04 24, ch05 8)
First-appearance discipline observed. **NOT re-noted** (noted at first
appearance, deliberately not repeated): Dai Li (first ch02 → recurs ch04,
ch05); Wang Jingwei (ch03 → ch04); Beiping (ch02 → ch03/04/05); the Juntong
(ch04 → ch05); War of Resistance (ch01 → ch02–05); secret service work / 特务
(ch01 → throughout); Legation Quarter / Concessions (ch02 → ch04); Chongqing,
Nanjing (ch03 → ch04); the "sanction" euphemism (ch04 §6 → the "Why Sanction?"
section); the Republican-calendar convention (ch02 §3, once).

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — derives `data/zh/<id>.txt` verbatim from
  `data/src/`, applying the per-unit drops/merges/heading-splits and verifying
  the source characters are conserved. Replaces the make_bilingual→
  split_bilingual path for a batch whose logical paragraphs differ from the
  source's `<p>` boundaries (merges + flattened headings).
- `scripts/batch_artifacts.py` — derives `out/<id>_en.json` from
  `out/<id>_reading.md` and writes `checks.json` (docs/sources config for
  check_structure / check_content).
- `scripts/check_content.py` — `name_map` now skips `_`-prefixed glossary
  categories/entries (it crashed on the sectioned glossary's `_about` string).
- Glossary is authored **sectioned** (people/organizations/places/terms) and
  merged by hand + validated with `apparatus_merge.check_text`, because
  `apparatus_merge`'s glossary path expects a FLAT `{zh: row}` map and would
  corrupt the sectioned file. Notes still go through `apparatus_merge.py`.

### Setup note
`tests/run_tests.py` reports ONE failure: "hook stands down on template stub."
This is NOT a real defect: the test assumes `HANDOFF.md` still holds the
template's *placeholder* kickoff, but it now holds a real book kickoff, so
`kickoff_guard.py` correctly refuses to stand down. The hook works as designed;
the test is coupled to template state. All other regression tests green.

## Batch B02 — ch06 (Part One, Section 1)

Unit: ch06 「第一节 任重道远 勇往直前」 = "Section 1. A Heavy Charge, Pressing
Onward." The FIRST NARRATIVE unit: Chen's 1931 audience with Chiang, the
Special Research Class, his meeting with Dai Li, the Honggongci training class,
the founding of the Beiping Station, the Fan Xing intelligence mystery, Dai
Li's 1933 Beiping inspection, and the assassination of Zhang Jingyao.
~25,236 source chars; 322 body paragraphs across five titled sub-sections.

### Structural recovery (clean_batch.py, ch06 spec added)
Five numbered sub-sections (一–五). One standalone heading (一 学友小聚初识戴
雨农, src line 3) and FOUR glued to the tail of the preceding paragraph (二…,
src line 72; 三…, 145; 四…, 194; 五…, 280) — split off as `###` sub-headings.
FIVE extractor-splits merged (src pairs 101+102, 173+174, 202+203, 221+222,
230+231). `clean_batch.py build` prints "322 body paragraphs, 5 sub-headings,
source conserved OK." No set-off formatting in the source HTML (no images, no
`center`/`kt`/duokan classes) — plain narrative, so `apply_format_markers`
had nothing to recover.

### Checks (all green)
- **Source-note grep (`\[\d+\]`):** none present in ch06 (re-checked). No
  `source_notes` stream. No images (survey's cover-only finding confirmed).
- **verify_unit / parity:** source 322 vs translation 322 — equal. Numbers
  0 unresolved with `--noise data/noise.txt`. Anchors 24/24 resolve.
- **check_align:** OK; median ratio **4.55 en/han** (narrative runs a touch
  terser than the essayistic front matter's 4.8–5.3, still well inside the
  2.2× stray bound; no pair strays).
- **check_structure:** parity OK; 24 note anchors, 0 unresolved; headings OK.
- **check_content:** 152 name occurrences, 0 displaced (all in paired para).
- **qc_entities:** 0 misses (top census: 北平×56, 力行社×26, 范行×21,
  军统×20, 特务处×15, 郑介民×15, 戴笠×14, 天津×13).
- **check_register --ref reference/B01_frozen.md:** "register within tolerance
  of the reference." rhythm CV 0.62 (ref 0.60); em-dash 7.5/1k (ref 8.3).
  One informational flag: "shall" share 22% — VERIFIED DELIBERATE, this is
  Chen's formal essayistic authorial future ("I shall set out below"), matching
  the frozen B01, plus reported documents/formal speech. Not a defect.
- **Tail verification (rule 4 corollary):** final three paragraphs (the Zhang
  Jingyao killing, its effect, and Bai Shiwei's first merit) checked against
  the source — faithful, nothing invented or dropped, all quantities carried.
- **Build:** `out/nameless-heroes.epub` 6/43, 91 notes (67 + 24), 0 source
  notes. `qa_epub.py` PASS (57 files, 91 refs = 91 bodies = 91 backlinks).
  **epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings.**

### Once-per-book calibration checks (done this batch)
- **Blind double-translation (check 7):** representative narrative passages
  re-rendered fresh and compared (the first sight of Dai Li, src 30; the Wang
  Tianmu sizing-up, src 204–205). High semantic agreement; divergence only
  stylistic. Dialogue (src 35–38) shows the expected register-dependent
  variation, not a defect. Calibration good — no systematic drift, no
  fabrication.
- **Round-trip back-translation (check 8, omission detector, sample):** the
  Dai residence paragraph (src 49) back-translated and matched against the
  source — no omissions (反潮 "rising damp," 穷对付 "make shift in poverty"
  both survive).

### Digitization glitches (rendered to plain sense; NOT footnoted — mechanical)
- src 243–244: `邱介民`/`邱先生` → `郑介民`/`郑先生` (Zheng Jiemin, the special
  commissioner; src 246+ correctly write 郑). Rendered "Zheng Jiemin."
- src 191: `陈恭树` → `陈恭澍` (the author himself). Rendered "Chen Gongshu."
- src 238: `豫鄂院三省` → `豫鄂皖` (Henan-Hubei-Anhui; src 302 has it right).
- src 56 (§1): `三月十七届空难` → `十七日` (17 March 1946); same line `所似`→`所以`,
  and a stray `了` in `不过了我记得`.
- src 11: `事质上`→`事实上`; `长杉短褂`→`长衫短褂` ("long gown and short jacket").
- src 16: `摆摆整挤` → `整齐` ("tidied things up").
- src 103: `增壁` → `墙壁` ("walls").
- src 124: `返带我们` → `曾带` ("once took us").
- src 142: `郡有` → `都有` ("every instructor had").
- src 143: `许多只课说程` → `许多课程` (scrambled; "many of the courses").
- src 159: `拙它分为`→`姑且…把它分`; `精神封延续`→`仍延续` ("carried on to this day").
- src 173: `一无小疪` → `一无小疵` ("one small blemish").
- src 184: `活在台活` → `活在台湾` ("still living in Taiwan").
- src 225: `苏州湖同` → `苏州胡同` ("Suzhou Hutong").
- src 326: `坂垣` → standard `板垣` (Itagaki; noted in the footnote and glossary).
- src 327: trailing stray `中` after `政变` ("a mutiny or a coup").
- src 18: `十四人那以` → `都以` ("each for a different reason").
- Variant/traditional glyphs (not glitches, rendered plainly): 鬪(=斗), 櫈(=凳),
  剌(=刺), 鄕(=乡).

### Noise rules added (`data/noise.txt`, B02 block)
`三两百` (idiom "two or three hundred"; the built-in 三两 strip would orphan a
100); place/org/personal names with numeral glyphs: `三道高井`, `三点会`, `四川`,
`四维学会`, `六国饭店`, `万里兄`, `万事通`; anniversary date-name `三一七`
(March 17th); idioms `五颜六色`, `四邻`, `三脚猫`, `四不像`, `千里之外`, `二手货`,
`两个字` (meta-linguistic character-count); weekday indices `星期一、三、五`.
Real quantities were carried in the English instead of noised (two-color pencil,
24 hours, two comrades, two yuan eight jiao, second step, one hundred HK$,
two men).

### Notes ledger (24 this batch; 91 cumulative)
First-appearance discipline observed. **NOT re-noted** (already noted in B01,
per that ledger): Dai Li, the Juntong, Beiping/Tianjin, the Whampoa Academy,
the Three Principles of the People, the Lixingshe / Special Services Department
/ Bureau of Investigation and Statistics / Revolutionary Soldiers' Comrades
Association, Zheng Jiemin, Zhang Jingyao, the Legation Quarter, the September
18th / January 28th Incidents, the War of Resistance, secret-service work, the
"sanction" euphemism, the Republican-calendar convention. New notes cover: the
Commandant (Chiang's academy titles), the Zhongshan tunic, the Central Military
Academy, the prescribed Confucian/statecraft classics, the Gong-Character Mess
Hall, "Zhongzheng," the numbered classes (期), the yuan, Hu Hanmin / "New
Kuomintang," the Suzhou-Hangzhou proverb, the Honggongci, the Cheka, the four
secret societies, Dai Li's motto couplet, the Zhongtong, the Beiping "gezi,"
the Youth Party, the Grand Hôtel des Wagons-Lits, the Huanggutun bombing, the
Four Young Masters, the Siwei Society (四维), the Xi'an Incident, Itagaki
Seishirō, the Baoding academy.

### Glossary rows added (17; principals now 6)
People: 王天木 Wang Tianmu (**principal**, cast 5), 范行 Fan Xing (**principal**,
cast 6), 白世维 Bai Shiwei, 杨英 Yang Ying, 戚南谱 Qi Nanpu, 吴泰勋 Wu Taixun,
李士珍 Li Shizhen, 黄雍 Huang Yong, 张炎元 Zhang Yanyuan, 张作霖 Zhang Zuolin,
胡汉民 Hu Hanmin, 张学良 Zhang Xueliang, 何应钦 He Yingqin, 坂垣征四郎 Itagaki
Seishirō. 郑介民 Zheng Jiemin **elevated to principal** (cast 4). Organizations:
复兴社 the Renaissance Society, 中统 the Zhongtong. Romanizations for the obscure
figures (Fan Xing, Yang Ying, Qi Nanpu) marked `provisional`. Feed 胡汉民,
张学良 back to `authority.json` on completion.

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — ch06 spec added (drop 2, five merges, four glued
  sub-headings, one standalone). Same verified source-conservation path as B01.
- `reference/B01_frozen.md` (new) — the concatenated ch01–ch05 readings, the
  single frozen reference file for `check_register.py --ref` from B02 on.
