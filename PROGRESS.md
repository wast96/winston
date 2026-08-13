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

## Batch B03 — ch07 (Part One, Section 2)

Unit: ch07 「第二节 一鸣惊人 不同凡响」 = "Section 2. A Startling Debut." The
Zhang Jingyao case told in full: the sudden 7-day sanction order relayed by
Zheng Jiemin (in a brothel-quarter parlor), the reconnaissance of the Legation
Quarter and the Grand Hôtel des Wagons-Lits, the tailor Ying Yuanxun's unwitting
tip, Bai Shiwei's three shots on 7 May 1933, and Chen's long reflective coda
(the intelligence "inside line," the Chiang-record passage, the Lixingshe
promotion, the tailor and the courtesan Feilong). Closes with the lead-in to
the 1934 Ji Hongchang case (ch08). ~21,263 source chars; 362 body paragraphs
across four titled sub-sections.

### Structural recovery (clean_batch.py, ch07 spec added)
Four numbered sub-sections (一–四), each its OWN standalone `<p>` line (src 3,
90, 194, 288) — no glued-to-tail headings this chapter (unlike ch06). ONE
extractor split merged (src 199+200, "…这表示有了 / 新的情况。"). `clean_batch.py
build` prints "362 body paragraphs, 4 sub-headings, source conserved OK." Source
HTML has 367 `<p>` (= 2 furniture + 365 body before the merge) and NO set-off
formatting (no images / center / kt / duokan classes) — plain narrative, so
`apply_format_markers` had nothing to recover.

### Checks (all green)
- **Source-note grep (`\[\d+\]`):** none present in ch07 (re-checked). No
  `source_notes` stream. No images (survey's cover-only finding confirmed).
- **verify_unit / parity:** source 362 vs translation 362 — equal. Numbers
  0 unresolved with `--noise data/noise.txt`. Anchors 11/11 resolve.
- **check_align:** median ratio **4.62 en/han** (in the B01/B02 band). Two
  pairs flagged at ratio 2.00 — both inherently short declaratives ("It was
  thus:" for 事情是这样的：; "This day was 7 May 1933." for a bare date line),
  content-faithful, not a slip; no run.
- **check_structure:** parity OK; 11 note anchors, 0 unresolved; headings OK.
- **check_content:** 155 name occurrences, 0 displaced (all in paired para).
- **qc_entities:** 0 misses (top census: 北平×49, 张敬尧×49, 六国饭店×44,
  东交民巷×24, 飞龙×19, 天津×17, 含春×14, 杨英×12, 郑介民×10).
- **check_register --ref reference/B01_frozen.md:** "register within tolerance
  of the reference." rhythm CV 0.62 (ref 0.60); em-dash 7.3/1k (ref 8.3);
  dialogue contractions 12.7/1k (ref 0.0 — the frozen front matter has no
  dialogue; ch07's are natural spoken contractions in the Wang/Feilong/steward
  speech, flagged within tolerance). One informational flag: "shall" share 33%
  — VERIFIED DELIBERATE (Chen's formal narrating/reported-speech future: "I
  shall," "we shall meet," Zheng's declaration), matching frozen B01. Not a
  defect.
- **Tail verification (rule 4 corollary):** final four paragraphs (the Ji
  Hongchang lead-in to ch08 and the closing summary) checked against the
  source — faithful, nothing invented or dropped; 五十余日 → "more than fifty
  days", 察、热一带 → "the Chahar-Rehe country", 宣侠父/南汉宸 both named,
  皆曰可杀 → "all said he might be killed" all carried.
- **Once-per-book calibration (checks 7,8):** done in B02; spot re-check on the
  brothel-customs passage (src 18–26) and the killing (src 257–274) — high
  agreement, no drift, no fabrication.
- **Build:** `out/nameless-heroes.epub` 7/43, 102 notes (91 + 11), 0 source
  notes. `qa_epub.py` PASS (57 files, 102 refs = 102 bodies = 102 backlinks).
  **epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings.**

### Digitization glitches (rendered to plain sense; NOT footnoted — mechanical)
- src 21: `折家`→`这家` ("this house"); `一块饯`→`一块钱` ("one dollar");
  `面截了当`→`直截了当` ("straight out").
- src 28: `就走卖唱`→`就是卖唱`; `可走总免不了`→`可是` (走 for 是).
- src 31: `湖同口`→`胡同口` ("mouth of the lane"; 湖 for 胡).
- src 32/35: `王人哥`→`王大哥` (人 for 大).
- src 36: `斟好了苶`→`茶` ("tea"); `拉抬子摆家性`→`拉台子摆家伙` ("set up a
  gaming table").
- src 67: `足自告奋勇`→`是自告奋勇`.
- src 89: paragraph lost its closing `」` and `。` (an unclosed quote); rendered
  as a complete sentence.
- src 93: `什縻`→`什么`.
- src 94: missing `。` after `(军分会代委员长)` before `我和王大哥`; rendered as
  two sentences.
- src 99: `这瑰地方`→`这块地方` (瑰 for 块).
- src 106: `可能走`→`可能是`.
- src 138: `我地想`→`我倒想`.
- src 142: `根木`→`根本` (木 for 本).
- src 143: `参谋长刘某`→`参谋长赵某` (刘 for 赵; the staff officer is 赵庭贵 /
  赵参谋长 everywhere else). Rendered "the chief of staff, Zhao."
- src 146: `打个旽`→`打个盹` ("take a nap").
- src 150: `长袍嵌肩`→`长袍坎肩` ("long gown and sleeveless jacket"; 嵌 for 坎).
- src 174: `对歭`→`对峙` ("standoff").
- src 201: `他所指的走`→`他所指的是` (走 for 是).
- src 211: `揉和在一趄`→`揉和在一起` (趄 for 起).
- src 213: `绐张督办`→`给张督办` (绐 for 给).
- src 233: `八面槽华清园`→`清华园` (the bathhouse is 清华园 at src 230/234/
  238/276/277; 华清园 here is the transposition). Rendered "the Qinghuayuan."
- src 250: `誊出一间`→`腾出一间` ("free up a room"; 誊 for 腾).
- src 253: `甬道德交会点`→`甬道的交会点` (德 for 的).
- src 264: `昴百阔步`→`昂首阔步` ("head high, long strides"; 昴百 for 昂首).
- src 271: `日木兵`→`日本兵` (木 for 本).
- src 277: `北良街`→`北长街` (良 for 长; the address is 北长街).
- src 305: `孙道迹天津`→`孙遁迹天津` ("withdrew into seclusion at Tianjin";
  道 for 遁); `末放下屠刀`→`未放下屠刀` (末 for 未).
- src 310: `十三妺`→`十三妹` (妺 for 妹, a variant glyph).
- src 316/323: `蜜肯相信`→`若肯相信` (src 323, 蜜 for 若); src 323 also missing
  a sentence break after `「获有内应」`.
- src 335: `古章简`→`吉章简` (the gendarmerie 4th-regiment commander / cell
  leader; 古 for 吉; consistent with 吉章简 later in the same line).
- Variant/traditional glyphs (not glitches, rendered plainly): 彷佛(=仿佛),
  鬪(=斗, in 鬪胜), 巿(=市), 囗(=口, 门囗), 謢(=护, 维謢), 蹧蹋(=糟蹋), 呵(excl.).

### Noise rules added (`data/noise.txt`, B03 block)
Itagaki's given name `征四郎` (四 in 坂垣征四郎); idioms `百般`(奉承),
`千秋`(自有千秋), `四平八稳`, `三三两两`; `第二天` (a next-day reference, not a
term-day count — those are carried as "first/second"); elided-tens `五、六十`
(步); place name `东四牌楼`; glitch `昴百阔步` (百 mis-scan of 首); cover name
`常世五` (Zhang's hotel alias); literary name `十三妺` (Shisanmei, source variant
妺); vocative `二爷` (Second Master[s] = "gentlemen"). Real quantities were
carried in the English instead of noised: 一百公尺 "a hundred meters", 十九(都是)
"nineteen in twenty", 午夜十二点 "twelve, midnight", 两个人 "the two of us",
中午十二点 "twelve noon", 六点十五分 "six-fifteen", 十二点三刻 "three quarters
past twelve", 两条甬道 "the two corridors", 二兄 "you two brothers", 三十万银元
"three hundred thousand silver yuan", 五十余日 "more than fifty days".

### Notes ledger (11 this batch; 102 cumulative)
First-appearance discipline observed. **NOT re-noted** (already noted in
B01/B02, per those ledgers): Zhang Jingyao, the Legation Quarter, the Grand
Hôtel des Wagons-Lits, the Beiping Station, the "sanction" euphemism, the 期
classes, Itagaki Seishirō, the Kwantung Army (glossed within the Huanggutun and
Itagaki notes), Sun Chuanfang, Shi Jianqiao (incl. the filial-revenge case),
Ji Hongchang (incl. the Chahar anti-Japanese army and the contested-attribution
note), Feng Yuxiang, Chahar, the Lixingshe / Renaissance Society / Youth &
Military Associations, the Zhongshan tunic, Dai Li, Zheng Jiemin, the yuan, the
Republican-calendar convention. New notes cover: Rehe (Jehol) and the 1933
invasion; Cai E and Xiao Fengxian; the Eight Great Hutongs and the "pure-singing
houses"; "beating the tea-circle" (打茶围); Zhang Zongchang (the Dog-Meat
General); "a second Manchukuo"; "The Secret Records of President Chiang" (the
Sankei Shimbun series); Duan Qirui; Song Zheyuan; "A Tale of Heroic Sons and
Daughters" / Shisanmei; the Boxer Protocol (as the source of the Legation
Quarter's status).

### Glossary rows added (24; principals unchanged at 6)
People (attested): 张宗昌 Zhang Zongchang, 蔡锷 Cai E, 小凤仙 Xiao Fengxian,
宋哲元 Song Zheyuan, 段祺瑞 Duan Qirui, 施从滨 Shi Congbin, 吉章简 Ji Zhangjian,
宣侠父 Xuan Xiafu, 南汉宸 Nan Hanchen. People (provisional): 赵庭贵 Zhao Tinggui,
应元勋 Ying Yuanxun, 飞龙 Feilong, 含春 Hanchun, 蒋孝先 Jiang Xiaoxian, 韩文焕
Han Wenhuan, 丁昌 Ding Chang. Organizations: 关东军 the Kwantung Army, 满洲国
Manchukuo, 北平军分会 the Beiping Military Branch, 中国人民反法西斯大同盟 the
Chinese People's Anti-Fascist Grand Alliance. Places: 东交民巷 the Legation
Quarter, 六国饭店 the Grand Hôtel des Wagons-Lits, 热河 Rehe, 韩家潭 Hanjiatan.
关东军 feeds from the authority shelf ("the Kwantung Army"); feed 张宗昌/蔡锷/
宋哲元/段祺瑞/孙传芳(already)/关东军 back to authority.json on completion.

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — ch07 spec added (drop 2, one merge 199+200, four
  standalone sub-headings, no glued). Same verified source-conservation path.
- Glossary rows added by hand into the sectioned file (people/orgs/places),
  idempotent + re-read-verified (the sectioned glossary must NOT go through
  apparatus_merge's flat-map path); notes merged via apparatus_merge as usual.

## Batch B04 — ch08 (Part One, Section 3)

Unit: ch08 「第三节 盘根错节 李代桃僵」 = "Section 3. Tangled Roots, a
Substitute Sacrifice." The longest unit so far (~36,344 chars per book.json;
41,482 raw source chars). The Ji Hongchang (吉鸿昌) case: the enlargement of
the Beiping/Tianjin Action Groups; the death of Tianjin Station chief Wang
Zixiang (王子襄) while testing a poison; the long reconnaissance through the
Zheng Enpu / Fu Danchi line; and the 9 Nov 1934 shooting inside the Guomin
Hotel (国民大饭店) in the Tianjin French Concession, where the gunman Wang Wen
(王文) killed the wrong man, Liu Shaorang (刘绍勷), by a last-minute switch of
venue and mahjong seats (李代桃僵). Long coda: the newspaper accounts, the
rebuttal of the Communist booklet "General Ji Hongchang," the extradition and
execution of Ji and Ren Yingqi, Ji's full biography, and the lead-in to the
Shi Yousan case (ch09). 461 body paragraphs across six titled sub-sections.

### Structural recovery (clean_batch.py, ch08 spec added)
Six numbered sub-sections (一–六). ONE standalone heading (一 煽扬赤焰的叛国者
皆曰可杀, src line 3) and FIVE glued to the tail of the preceding paragraph
(二…, src 112; 三…, 206; 四…, 250; 五…, 328; 六…, 394) — split off as `###`
sub-headings (same mixed pattern as ch06). SIX extractor-splits merged (src
pairs 95+96, 117+118, 129+130, 150+151, 308+309, 376+377). NOT merged and left
visible per rule 4: src line 402 (第三点：…其原由，在) trails off in a **source
cut** — its continuation is lost and the next line is the next bullet (第四点)
— so it stands as its own paragraph, unmerged, faithfully broken. The
enumerated ；/： bullet lists (Zheng's numbered help-items, the sanction-order
points, the newspaper quotes, the eight-point rebuttal, the biography dates)
are deliberate separate `<p>` and were NOT merged. `clean_batch.py build`
prints "ch08: 461 body paragraphs, 6 sub-headings, source conserved OK." Source
HTML has 468 `<p>` (= 2 furniture + 466 body, before the six merges) plus one
`<h2>`; NO set-off formatting (no images / center / kt / duokan classes) —
plain narrative, so `apply_format_markers` had nothing to recover.

### Checks (all green)
- **Source-note grep (`\[\d+\]`):** none present in ch08 (re-checked). No
  `source_notes` stream. No images (survey's cover-only finding confirmed).
- **verify_unit / parity:** source 461 vs translation 461 — equal. Numbers
  0 unresolved with `--noise data/noise.txt`. Anchors 12/12 resolve.
- **check_align:** median ratio **4.70 en/han** (a touch above ch06 4.55 /
  ch07 4.62 — the heavy quoted-document and news-report matter runs slightly
  looser; still well inside the 2.2× stray bound; no pair strays).
- **check_structure:** parity OK; 12 note anchors, 0 unresolved; headings OK.
- **check_content:** 661 name occurrences, 0 displaced (all in paired para).
  Two real omissions caught and fixed as they surfaced: para 202 restored
  "Tianjin Station" (故站长 → "the late Tianjin Station chief"); para 317
  restored the name "Yang Yushan" (杨玉珊姐弟 → "Yang Yushan and her brother").
- **qc_entities:** 0 misses (top census: 吉鸿昌×169, 北平×98, 天津×98,
  方振武×21, 冯玉祥×20, 军统×16, 制裁×13, 石友三×13).
- **check_register --ref reference/B01_frozen.md:** "register within tolerance
  of the reference." rhythm CV 0.63 (ref 0.60); em-dash 6.0/1k (ref 8.3);
  dialogue contractions 0.0/1k. One informational flag: "shall" share 55% —
  VERIFIED DELIBERATE (Chen's and the agents' formal first-person future: "I
  shall report to you," "I shall now go first," Dai's "I shall telephone,"
  the conditional "we shall have the chance"); matches the frozen B01 voice.
  Not a defect.
- **Tail verification (rule 4 corollary):** final seven paragraphs (461–468,
  the utter-failure summary and the Shi Yousan lead-in) checked against the
  source — faithful, nothing invented or dropped: 反复无常/朝秦暮楚 carried;
  先鸿霞、老褚二人 "the two, Xian Hongxia and old Chu"; 刑究 "interrogation
  under torture"; 史大川 Shi Dachuan; 前后两任司令官 "the two successive
  commanders"; 多田骏/田代皖一郎; 八年抗战/明正典刑/自食恶果 all carried.
- **Once-per-book calibration (checks 7,8):** done in B02; spot re-check on the
  reconnaissance dialogue (src 277–287) and the killing (src 349–352) — high
  agreement, no drift, no fabrication.
- **Build:** `out/nameless-heroes.epub` 8/43, 114 notes (102 + 12), 0 source
  notes. `qa_epub.py` PASS (57 files, 114 refs = 114 bodies = 114 backlinks).
  **epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings.**

### Digitization glitches (rendered to plain sense; NOT footnoted — mechanical)
- Recurring 戴先坐 → 戴先生 "Mr. Dai" (坐 for 生; src 22, 40, 198, 202-region).
- src 50/51: 王于襄 → 王子襄 "Dr. Wang Zixiang" (于 for 子).
- src 91: 方挀武 → 方振武 (挀 for 振).
- src 105/108: 靳云鸮 → 靳云鹗 "Jin Yun'e" (鸮 for 鹗).
- src 68/70/105: 委负会 / 前线委负会 → 委员会 (负 for 员).
- src 117: 略为演示文稿 — garbled (演示文稿 = "presentation slides", an
  auto-correct/digitization artifact); rendered to plain sense "laid out for
  him in short."
- src 273: 𬬭匙 → 钥匙 "key" (variant glyph).
- src 256: 万人活躣 → 活跃/活动 "astir" (躣 a glitch).
- src 275: 王艾 → 王文 "Wang Wen" (艾 for 文).
- src 305/39: 妹妺 → 妹妹 "younger sister" (variant 妺).
- src 426: 偃城 → 郾城 "Yancheng" (偃 for 郾; the Henan town where Feng raised
  troops).
- src 148: the poison "X霜" — the author has REDACTED the first character of
  the poison's name (砒霜 arsenic? the almond note suggests cyanide); rendered
  faithfully as "an 'X-frost'," the redaction left visible, not a note.
- Variant/traditional glyphs (rendered plainly): 巿(=市), 妺(=妹), 鸮/鸮.

### Numeric-invariant handling (data/noise.txt, B04 block; check_numbers 0 unresolved)
Real quantities carried in the English (times spelled to match the checker):
2:55 "two fifty-five", 2:50 "two fifty", 4:45 "four forty-five", 4:57 "four
fifty-seven", 8:40 "eight-forty", 11:30 "eleven-thirty"; 十二万 "one hundred
and twenty thousand"; 一百多公尺 "a hundred meters"; 十来步 "ten-odd steps";
1967–'68; and every 二人/二位/两位 "the two [named]" made explicit ("the two,
Zheng and Fu," etc.). Noised as idiom/name/place/artifact (each with a comment
line): 接二连三, 十三陵, 三道关, 九龙, 五原, 四下, 零碎(=0), 十万火急, 一诺千金,
万不可, 万全, 万难, 亿万, 三明治, 百思, 胡说八道, 七零八落(=708), 十字, 瘪三,
二、三十, 六、七十 (elided tens), and `(?<=五)两个房` (a lookbehind to detach the
count that glued 一四五 into a phantom "1452"; both rooms named in English).

### Notes ledger (12 this batch; 114 cumulative)
First-appearance discipline observed. **NOT re-noted** (already noted in
B01/B02/B03, per those ledgers): Ji Hongchang, the Chahar anti-Japanese army
(民众抗日同盟军), Feng Yuxiang, Fang Zhenwu, Shi Yousan, the Kwantung Army,
Manchukuo, the Legation Quarter, the Grand Hôtel des Wagons-Lits, Tianjin/
Beiping, the "sanction" euphemism, the Juntong / Lixingshe / Renaissance
Society / Special Services Department, Zheng Jiemin, Dai Li, Nan Hanchen, Xuan
Xiafu, He Yingqin, Rehe, the Beiping Military Branch, the Republican-calendar
convention, the yuan, Whampoa, the War of Resistance. New notes cover: the
Tanggu Truce; the Green Gang and "opening the incense hall"; Peking Union
Medical College; the Mackenzie (Ma Dafu) Hospital; the Lishunde / Astor House
Hotel; the "though I did not kill Boren" allusion; the Mauser "box-cannon"
(C96); the Blue Shirt Society (蓝衣社 as the enemy's name for the Lixingshe);
the "Red Building" pun; the Cultural-Revolution Red Guards and the 1967–68
factional fighting (with Jiang Qing "毛婆" and Lin Biao); Ji Hongchang's death
poem (author-as-interested-witness); the Dagongbao / Shenbao newspapers.

### Glossary rows added (54; principals unchanged at 6)
People (38 new): 王子襄 Wang Zixiang, 王玉梅 Wang Yumei, 吕一民 Lü Yimin, 吴萍
Wu Ping, 王文 Wang Wen, 郑恩普 Zheng Enpu, 傅丹墀 Fu Danchi, 杨玉珊 Yang Yushan,
陈国瑞 Chen Guorui, 任应岐 Ren Yingqi, 商震 Shang Zhen, 于学忠 Yu Xuezhong,
张慕陶 Zhang Mutao, 穆欣 Mu Xin, 樊钟秀 Fan Zhongxiu, 靳云鹗 Jin Yun'e, 门致中
Men Zhizhong, 吴佩孚 Wu Peifu, 佟麟阁 Tong Linge, 孙良诚 Sun Liangcheng, 冯占海
Feng Zhanhai, 杨虎城 Yang Hucheng, 李大钊 Li Dazhao, 魏野畴 Wei Yechou, 王芃生
Wang Pengsheng, 邓文仪 Deng Wenyi, 江青 Jiang Qing, 先鸿霞 Xian Hongxia, 史大川
Shi Dachuan, 老褚 old Chu, 多田骏 Tada Hayao, 田代皖一郎 Tashiro Kan'ichirō,
胡洪霞 Hu Hongxia, 王平一 Wang Pingyi, 吴赓恕 Wu Gengshu, 吴幼权 Wu Youquan,
佟荣功 Tong Ronggong, 张璧 Zhang Bi (丁昌 already present, skipped). Organizations
(7): 察哈尔民众抗日同盟军, 蓝衣社 the Blue Shirt Society, 青帮 the Green Gang,
红卫兵 the Red Guards, 行动组/情报组/军事组. Places (9): 国民大饭店 the Guomin
Hotel, 交通旅馆 the Jiaotong Hotel, 惠中饭店 the Huizhong Hotel, 利顺德饭店 the
Lishunde Hotel (Astor House), 小白楼 Xiaobailou, 特别第一区 the First Special
District, 劝业场 the Quanyechang, 紫竹林 Zizhulin, 张家口 Zhangjiakou. Romanizations
for the obscure agents/persons marked `provisional`; feed the historical names
(任应岐, 商震, 于学忠, 吴佩孚, 佟麟阁, 杨虎城, 李大钊, 樊钟秀) to `authority.json`
on completion. Japanese readings (多田骏, 田代皖一郎) provisional — verify when they
recur.

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — ch08 spec added (drop 2, six merges, five glued
  sub-headings, one standalone; 402 deliberately left unmerged as a source cut).
  Same verified source-conservation path.
- `data/noise.txt` — B04 block (idioms/names/places/elided-tens + the
  `(?<=五)两个房` lookbehind). Glossary rows added by hand into the sectioned
  file, idempotent + re-read-verified; notes merged via apparatus_merge as usual.

## Batch B05 — ch09 (Part One, Section 4)

**第四节 急功躁进铸成大错 → "Section 4. Impatience Breeds a Grave Blunder."** The
Shi Yousan case of winter 1934: an over-hasty poisoning-and-shooting plot in the
Tianjin Japanese concession that failed — the inside men Xian Hongxia and the
cook old Chu were seized by the Japanese gendarmerie and lost; Shi Dachuan
escaped but left in anger over Liu Zhaonan's embezzlement and cover-up; Chen fled
to frontier exile at Guisui/Ulanhua, was jailed five months at the Juntong's
Nanjing "Site B," then restored as Tianjin Station chief. Shi Yousan, shielded by
the Japanese garrison commanders Tada Hayao and Tashiro Kan'ichirō, had his
warrant cancelled and a government post given, only to be executed for rebellion
early in the war. 332 body paragraphs; ratio 4.66 en/han.

### Structural recovery (clean_batch.py, ch09 spec added)
- drop 2 (running header + `<h2>`). Six sub-headings, space-style (一 …): 一
  standalone; 二 三 五 四 六 glued to a preceding `<p>` tail.
- **The source prints sections 四 and 五 OUT OF SEQUENCE** — the `<p>` labelled
  五 (「不敢面对现实作了一次边塞流亡」) physically precedes the one labelled 四
  (「处置失当步调与进退失据」), confirmed by byte order in the source XHTML. Preserved
  verbatim in printed order and FOOTNOTED per rule 4 (the numbering note).
- Five extractor-split merges, one a THREE-fragment chain (89→90→91); clean_batch's
  merge logic extended to follow chains (backward-compatible with plain pairs).
  The many ：-ended lines introduce quotes/examples as deliberate separate `<p>`,
  not merged. L54 ("且看石友三…下作行为") is a colon-less lead-in `<p>`, kept whole.
  L164 ends with a stray opening 「 belonging to L165 (misplaced-bracket glitch);
  the two stay separate `<p>`, bracket left where the source has it (chars conserved).
- `<p>` count 338 = body lines 3–340 (1:1). No images, no set-off formatting
  (plain narrative, like ch06–ch08). Grep for note markers `\[\d+\]`: **none present.**

### Checks (all green)
- verify_unit.py ch09: parity 332↔332 OK; numbers **0 unresolved** (checked 332
  pairs); anchors 0.
- check_align.py: 332/332, median ratio **4.66 en/han**, no pair strays >2.2×.
- check_structure.py: parity OK, anchors 0 unresolved, headings OK.
- check_content.py: 162 anchors, 564 name occurrences, all in the paired paragraph.
- qc_entities.py (reconstructed bilingual): **0 misses** (census 王文 x138, 先鸿霞
  x101, 石友三 x80, 刘兆南 x50, 贺参谋 x24, …).
- check_register.py --ref reference/B01_frozen.md: within tolerance. contr 0.3/1k,
  em-dash 7.4/1k (ref 8.3), rhythm CV 0.57 (ref 0.60). "shall" 23% — deliberate
  (Chen's formal narration; the note is informational).
- Tail verified against source (rule 4 corollary): §6 close (zh 335–339), §5 close
  (zh 239), §4 close (zh 280), §3 close (zh 177–179) — all faithful.
- Once-per-book blind double-translation (check 7) and back-translation (check 8)
  were done in B02; spot re-check only, as instructed.
- Build: qa_epub.py PASS (57 files, 50 docs, 123 note refs/bodies/backlinks all
  resolve; 9/43 chapters). **epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings.**

### Digitization glitches (rendered to plain sense; NOT footnoted — mechanical)
- 韩复矩 → 韩复榘 Han Fuju (the general's name); rendered "Han Fuju".
- 阎钖山 → 阎锡山 Yan Xishan (钖 a variant/mis-scan of 锡).
- 坂垣征四郎 → 板垣征四郎 Itagaki Seishirō (坂 for 板, as in earlier batches).
- 李怀章 (src 26, 大司务) vs 林怀章 (src 191, 厨子) — the 北平站 cook's surname given
  two ways; same man, rendered "Li Huaizhang" / "Lin Huaizhang" as each passage prints.
- 北平店 for 北平站 (src 26, 27); 天津店 for 天津站 (src 14) — 店 for 站.
- 发征 for 发怔/发愣 (src 162, "as I stood dazed").
- 去去摸 dittography (src 159, "to feel for the gun"); rendered once.
- 满京 for 南京 (src 249, "Nanjing's reply telegram").
- 铁丝纲 for 铁丝网 (barbed wire); 笫 for 第 throughout; 揷 for 插; 秏 for 耗;
  兪 for 俞 (兪雪侬); 位以 for 畀以/委以 (src 337).
- Variant/traditional glyphs (not glitches, rendered plainly): 櫈(=凳), 麕(=麇),
  刼(=劫), 侬, 冑.

### Numeric-invariant handling (data/noise.txt, B05 block; check_numbers 0 unresolved)
Republican years carried as Gregorian (checker auto-excuses via +1911). Real
quantities carried in the English (rent 40 yuan; the two 2000-dollar sums; 500;
160; 150 li; five months seven days; 70-odd days; prisoner No. 162; the Type 38;
the 29th Army; clock times spelled — "eight forty-five"; 二人/两租界 made explicit
"the two [named]"/"those two"). Noised (idiom/name/place/artifact): 三益成, 望九,
三轮车, 土肥原贤二, 三数, 十足, 零下, 三天两头, 两口, 千叮万嘱, 三刻, 百无聊赖,
王八蛋, 二字, 笫二天, 三更半夜.

### Notes ledger (9 this batch; 123 cumulative)
First-appearance discipline observed. **NOT re-noted** (already noted in
B01–B04, per those ledgers): Shi Yousan, the Japanese concession, the Mauser
"box-cannon", the Green Gang and "opening the incense hall", the Tanggu Truce,
the "sanction" euphemism, the Juntong / Lixingshe / Renaissance Society, the Blue
Shirt Society, the Republican-calendar convention, Dai Li, Zheng Jiemin, Feng
Yuxiang, Song Zheyuan, the Kwantung Army, Manchukuo, Yin Rugeng and the East
Hebei puppet government, Itagaki Seishirō, the yuan, Whampoa / the Military
Academy, Rehe, the War of Resistance. New notes cover: (1) the source's
out-of-sequence section numbering (五 before 四) — editorial/faithfulness note;
(2) He Yingqin / "Minister He" (no prior footnote existed for him despite the B04
list; this is his first note); (3) the 1930 Yan–Feng Revolt / Central Plains War;
(4) Doihara Kenji; (5) the kang (heated brick bed); (6) the "nine-nines" of
winter (数九); (7) Guisui / Suiyuan frontier; (8) the Green Gang generational
rank (通字辈 "Tong" generation); (9) the 1935 North China Autonomy Movement.

### Glossary rows added (72; principals unchanged at 6)
People (29 new): 韩复矩 Han Fuju, 刘郁芬 Liu Yufen, 王树常 Wang Shuchang, 刘翼飞
Liu Yifei, 李培基 Li Peiji, 孙殿英 Sun Dianying, 庞炳勋 Pang Bingxun, 李际春 Li
Jichun, 白坚武 Bai Jianwu, 土肥原贤二 Doihara Kenji, 阎锡山 Yan Xishan, 贺参谋 Staff
Officer He, 刘兆南 Liu Zhaonan, 王云孙 Wang Yunsun, 兪雪侬 Yu Xuenong, 侯子川 Hou
Zichuan, 刘乙光 Liu Yiguang, 连谋 Lian Mou (style Liangshun), 张毅夫 Zhang Yifu,
高荣 Gao Rong, 甘团长 Colonel Gan, 王锐铮 Wang Ruizheng, 张作兴 Zhang Zuoxing, 江田
Jiang Tian, 江宜清 Jiang Yiqing, 江汰清 Jiang Taiqing, 彭雅萝 Peng Yaluo, 陈恭治
Chen Gongzhi (Chen's elder brother), 周仁风 Zhou Renfeng (Chen's cover-name).
(何应钦, 于学忠, 张学良, 张璧, 王平一, 张炎元, 杨英, 毛万里 already present.)
Places (33): 卧佛寺街, 秋田街, 旭街, 海光寺, 顺德, 滦县, 新民, 锦州, 沈阳兵工厂,
按院胡同, 德元成, 弓弦胡同, 米市大街, 光陆电影院, 西直门, 平绥路, 归绥 Guisui,
利源增, 乌兰华 Ulanhua, 辟才胡同, 花园饭店, 羊皮巷, 鸡鹅巷, 老虎桥, 安乐园, 中央饭店,
津浦路, 鸡泽县, 西山疗养院, 阳明山, 大慈寺, 黄寺, 安定门. Organizations (8): 华北
自治运动, 便衣队, 定武军, 南昌行营调查课, 世界日报, 二十九军, 华北政务委员会, 冀北
边区保安司令. Terms (2): 督察 "inspector", 三八式 "the Type 38". Every row carries
a pinyin field (the checker requires it). Obscure operatives/private persons and
minor establishments marked `provisional`; historical figures `attested`. Feed
the historical names (韩复榘, 刘郁芬, 王树常, 李培基, 孙殿英, 庞炳勋, 李际春, 白坚武,
阎锡山) to authority.json on completion; 土肥原贤二/坂垣征四郎 Japanese readings
provisional — verify on recurrence.

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — ch09 spec added; merge logic now follows CHAINS
  (a `<p>` split into 3+ fragments rejoined whole), backward-compatible with the
  earlier pairwise specs (ch01–ch08 output unchanged).
- `data/noise.txt` — B05 block (see above). Glossary rows added by hand into the
  sectioned file, idempotent + re-read-verified; notes merged via apparatus_merge.py.

## Batch B06 — ch10 + ch11 (Part Two opens: "Disgrace at Hanoi")

Two units, 13,734 source chars. ch10 = 「河内汪案始末」自序 "Author's Preface: The
Full Story of the Wang Case at Hanoi" (26 body paragraphs, a short essayistic
preface). ch11 = 第一章 浴血杀敌奋勇抗战 "Chapter 1. Bloodshed Against the Enemy,
Valiant Resistance" (87 body paragraphs, 2 sub-headings). This opens PART TWO,
the 1939 Juntong attempt on Wang Jingwei at Hanoi. New Hanoi cast introduced;
the North China martyrs (Zeng Che, Wang Wen) are eulogized as the chapter
opens, then the summons to Hong Kong and the flight to Hanoi, Dai Li's briefing,
and the full text of Wang's "Yan Telegram" with Chen's rebuttal.

### Structure / extractor handling (clean_batch specs; source conserved OK)
- **ch10** drop=3: running header 英雄无名-陈恭澍 + `<h1>「河内辱命」` (the Part Two
  banner, carried by book.json's `part` field) + `<h3>「河内汪案始末」自序` (the
  chapter title, re-emitted from `title`). No sub-headings; 26 `<p>`, no splits.
- **ch11** drop=2 (header + `<h2>` chapter title). 89 `<p>`. One extractor split:
  (L90,L91) "…汪氏艳 / 电后…" broken mid-word (艳|电), merged. The 「艳电」 document is
  a THREE-`<p>` quoted block (lead-in ends ：, salutation ends ：, then the 1,298-
  char body) — those ：-ended `<p>` are DELIBERATE separate paragraphs, NOT merged.
- **ch11 sub-headings are couplet-style with NO number prefix** (unlike ch06–09's
  一/二/三): L3 一道急急令飞渡万里关山 stands alone; L52 只限于行踪监视与活动侦察 is
  glued to a paragraph's tail (like ch08's glued headings). Confirmed against the
  source XHTML `<p>` boundaries and nav.xhtml (which lists chapter titles only, not
  these in-body sub-headings).
- Note markers `\[\d+\]`: **none present** in either unit (grep clean).
- Set-off formatting / images: **none** — plain narrative (no `<img>/<hr>/<div>/
  class`), confirmed for both files.

### Part Two title — DECISION (open question resolved)
**Keep "Disgrace at Hanoi" as the Part Two heading; no book.json change.** The
source's own part banner (the `<h1>` in ch10 and the nav.xhtml entry) is
「河内辱命」 throughout; 河内汪案始末 is only the published book-title of the
constituent volume, which Chen (ch10 §10–11) settled on at proof stage after
rejecting 河内刺汪 (he would not accept 刺 "stab", "to kill a man off his guard")
and finding 奉使河内记 and 河内辱命 wanting. book.json already models this exactly:
Part Two = "Disgrace at Hanoi" (banner 河内辱命); ch10 = "Author's Preface: The
Full Story of the Wang Case at Hanoi" (河内汪案始末自序). The translator's-note gloss
("Disgrace at Hanoi (published under the title The Full Story of the Wang Case at
Hanoi)") stands. The faithful choice is the source's banner.

### Digitization glitches (rendered to plain sense; NOT footnoted — mechanical)
ch10: 被浦→被捕 (L14, "after my capture"); 戎们→我们 (L21); 议牲→牺牲 (L22, L23,
"sacrifice"); 掌握看→掌握着 (L9, "held fast"); 易如称为→亦可称为 (L10, rendered "might
as well be called"). ch11: 打别嗦→打哆嗦 (L20, "shivered"); 狼狙→狼狈 (L26,
"wretched"); 方炳四→方炳西 (L71, "Fang Bingxi"); 前力→前方 (L81, "front-line"). Inside
the quoted 「艳电」/resolution (rendered to sense, glitch in a primary document):
干沙及→干涉 (L73, "interfere"); 贴偿→赔偿 (L73, "indemnity"); 领土土→领土上 (L79,
dittography, "territory", ×2); 艳驾→艳电 (L80); 承本黛→承本党 (L83, "this Party").
Misplaced-「 glitches (stray open-quote, like ch09 L164): L56 掌握「也应该 and L76
何从「调整起 — rendered to plain sense, the stray bracket dropped. 芦沟桥 for 卢沟桥
inside the 艳电 is a standard variant, not a glitch (Marco Polo Bridge).

### Genuine source corruption + textual anomaly (FOOTNOTED, rule 4)
- **ch11 L69** 我已经和他的爱 — corrupt ("I have already, with his … love"), no
  sense; footnoted, rendered to the evident sense (Dai had settled that Chen alone
  would be the contact's liaison).
- **ch11 L22** cross-reference to "the fifth section" of Book One — as collected
  here Book One runs to four sections (Chapters 6–9); footnoted as the original's
  discrepancy, left as written.

### Checks (all green)
- verify_unit ch10 / ch11: parity 26/26, 87/87; numbers 0 unresolved (after B06
  noise block); anchors clean.
- check_align: ch10 26/26 median 5.18 en/han (preface, essayistic — denser, in
  line with B01 front matter); ch11 87/87 median 4.76 (narrative, top of the
  4.55–4.70 band). No pair strays >2.2× the median.
- check_structure: parity OK both, 2 heading levels OK, 0 unresolved anchors.
- check_content: 0 displacement (7 name occ ch10, 38 ch11, all in paired paras).
- qc_entities: 0 misses (ch10 top 河内 x18; ch11 top 天津 x23, 艳电 x15).
- check_register --ref: within tolerance. ch10 shall 0% (preface); ch11 shall 33%
  — Chen's deliberate narrating "shall" (voice sheet; B05 ran 23%, verified).
  Contractions 0.0/1k both; em-dash 9.1/9.3 vs ref 8.3.
- Tails verified against source (rule 4 corollary): both complete, nothing
  invented or dropped (ch11 tail carries all three dates 22/26/29).
- Build: qa_epub PASS (57 files, 137 refs/137 bodies/137 backlinks, all links
  resolve); epubcheck 5.1.0 → 0 fatals / 0 errors / 0 warnings. EPUB now
  **11/43 chapters**.

### Numeric-invariant handling (data/noise.txt, B06 block)
Real quantities carried in the English (eight years; twenty-seven / thirty years
of age; 300+ days; the two cities Beiping and Tianjin made explicit "two"; the
ten-odd dollars carried as "ten-odd"; Republican years auto-excused via +1911;
the 艳电's dates 3 Nov / 16 Jan / 29 Dec). Noised (idiom/elided-tens): 六亲
(六亲不认), 十二、三 (elided 12–13yr), 接二连三, 三、四十 (elided 30–40 days),
不远千里 ("thousand li" idiom, kept in English but checker maps only "a thousand"),
百万计 ("by the million", round-number idiom).

### Notes ledger (14 this batch: ch10 4, ch11 10; 137 cumulative)
First-appearance discipline observed. **NOT re-noted** (already noted B01–B05):
Wang Jingwei (ch03), Hanoi (ch03), Chen Bijun (ch03), the Ume Kikan / 梅机关
(ch04), Manchukuo (ch03), the Tanggu Truce (B04), the Marco Polo Bridge / War of
Resistance (ch01), the Three Principles of the People (B01), the Republican-
calendar convention, the "sanction" euphemism, the Juntong, Dai Li, Beiping/
Tianjin, Chongqing/Nanjing, the concessions, Kwantung Army. New notes: (ch10) the
1910 assassination of the Qing Prince Regent + Wang's prison quatrain; the "Yan
Telegram" (韵目代日 date-naming, 艳=29th); Konoe Fumimaro; the People's Political
Council. (ch11) the Juntong "ancestral hall"/spirit-tablets; the Anti-Japanese
Traitor-Killing Corps (抗团); the Luan-Yu Guerrilla Command; the "fifth section"
discrepancy; the "Kongming cart" (Indochina cyclo); "Director-General" (总裁) vs
Generalissimo/Commandant + Wang's Vice-Director-General; the Three Principles of
Peace (distinct from Three Principles of the People); the Nov-1938 Chongguangtang
secret Shanghai talks (Gao Zongwu / Mei Siping); the L69 source corruption; the
Jing/Wei proverb (泾渭分明).

### Glossary rows added (59; principals now 8)
People (23): 曾澈 Zeng Che, 方炳西 Fang Bingxi (**principal**, cast 7), 齐庆斌 Qi
Qingbin, 陈资一 Chen Ziyi, 周世光 Zhou Shiguang, 胡永荃 Hu Yongquan, 陈春圃 Chen
Chunpu, 叶吉卿 Ye Jiqing, 晴气庆胤 Haruke Yoshitane, 影佐祯昭 Kagesa Sadaaki, 刘原深
Liu Yuanshen, 近卫文麿 Konoe Fumimaro, 林柏生 Lin Baisheng, 高宗武 Gao Zongwu, 梅思平
Mei Siping, 今井武夫 Imai Takeo, 伊藤芳男 Itō Yoshio, 吴敬恒 Wu Jingheng (Zhihui),
林森 Lin Sen, 张继 Zhang Ji, 陈布雷 Chen Bulei, 剑秋 Jianqiu (identity uncertain),
炳华 Binghua (= 张炎元 Zhang Yanyuan), 汪兆铭 Wang Zhaoming (= 汪精卫). **王鲁翘 Wang
Luqiao elevated to principal (cast 8).** (张作兴, 中岛信一 already present.) Places
(21): 河内 Hanoi, 安南 Annam, 越南 Vietnam, 重庆 Chongqing, 四川 Sichuan, 广西
Guangxi, 跑马地 Happy Valley, 山光饭店, 薄扶林道 Pok Fu Lam Road, 半山 the Mid-Levels,
湾仔 Wan Chai, 干诺道 Connaught Road, 塘沽 Tanggu, 吴淞口 Wusong, 黄浦江 the Huangpu,
宝坻 Baodi, 冀东 East Hebei, 布鲁塞尔 Brussels, 比利时 Belgium, 虹口 Hongkou, 河北大经路
Dajing Road. Organizations (11): 滦榆游击总部 the Luan-Yu Guerrilla Command, 梅机关
the Ume Kikan, 满铁株式会社 the South Manchuria Railway Company, 国民参政会 the
People's Political Council, 天津区 the Tianjin District, 北平第一站 the Beiping First
Station, 国防部情报局 the Intelligence Bureau of the MND, 中国国民党 the Chinese
Nationalist Party, 太古公司 Butterfield & Swire, 怡和洋行 Jardine Matheson, 渣华公司
the Java-China-Japan Line. Terms (3): 艳电 the Yan Telegram, 和平三原则 the Three
Principles of Peace, 孔明车 the Kongming cart. (抗日杀奸团 already present.) Every row
carries a pinyin field; obscure operatives / Japanese readings marked
`provisional`. Feed the historical names (近卫文麿, 影佐祯昭, 高宗武, 梅思平, 林森,
张继, 吴敬恒, 陈布雷) to authority.json on completion.

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — ch10 (drop=3, no headings) and ch11 (drop=2, one
  merge, one standalone + one glued couplet-style sub-heading) specs added;
  backward-compatible with ch01–ch09.
- `data/noise.txt` — B06 block (see above). Glossary rows added by hand into the
  sectioned file, idempotent + re-read-verified; notes merged via apparatus_merge.py.

## Batch B07 — ch12 (Part Two, Chapter 2: "Disgrace at Hanoi")

One unit, 19,990 source chars. ch12 = 第二章 人心叵测别有肺肠 "Chapter 2.
Unfathomable Hearts, Hidden Designs" (131 body paragraphs, 3 sub-headings). The
Hanoi team fills out (Fang Bingxi, Wang Luqiao, then Cen Jiazhuo and Yu Lexing
arrive); the chapter's spine is two long quoted political documents given whole
as "political instruction" from Chongqing — Konoe's third statement (22 Dec) and
the Generalissimo Chiang's 9,000-character address "Exposing the Enemy State's
Plot and Setting Forth the National Policy of Resistance" (26 Dec) — framed by
Chen's insistence that the Juntong had NO advance intelligence of Wang's
collusion, buttressed by Chen Bulei's memoir, the Zhu Zijia (Jin Xiongbai) memoir,
and the anonymous "Yongwu" diary of Wang's flight from Chongqing.

### Structure / extractor handling (clean_batch.py, ch12 spec added; source conserved OK)
- **ch12** drop=2 (running header 英雄无名-陈恭澍 + `<h2>` chapter title). 136 `<p>`
  in the source XHTML (confirmed by tag count), 1:1 with the ingest's body lines.
- **Sub-headings are numbered-in-parens (一)/(二)/(三)** (a THIRD pattern, distinct
  from ch06–09's numbered 一/二/三 and ch11's couplet style): L3 (一) stands alone;
  (二) at L33 and (三) at L69 are glued to the tail of the preceding `<p>` (split off
  as `### ` headings).
- **Four extractor splits** (mid-phrase continuations), merged: (L42,L43) 以分析的|
  方法; (L94,L95) 不敢遽|下判断; (L124,L125) 黯然|握别; **(L131,L132) 笔者相信「用五」|
  先生** — the name 「用五」先生 split across the closing 」, a split the "」 is terminal"
  heuristic hides (caught only on the parity mismatch, then confirmed against the
  source `<p>` boundaries and merged). The many ：-ended lines that lead into the two
  quoted documents are DELIBERATE separate `<p>`, NOT merged.
- **"(本章完)" mid-file:** the chapter proper ends with an in-text "(End of this
  chapter)" marker at L133 (rendered faithfully), after which the source prints a
  5-`<p>` reflective coda (L134–138) — genuine text, kept whole as body paragraphs.
- Note markers `\[\d+\]`: **none present** (grep clean; recorded).
- Set-off formatting / images: **none** — plain narrative (no `<img>/<hr>/<div>/
  em/i/b/span`), confirmed. ch12 carries no figures.

### Digitization glitches (rendered to plain sense; NOT footnoted — mechanical)
- 力炳西 → 方炳西 "Fang Bingxi" (L4, wrong first char). 汪卫卫 → 汪精卫 "Wang Jingwei"
  (L99, 卫卫 for 精卫). 沦爸以亡 → 沦胥以亡 "sink to ruin" (L54). 根木 → 根本 "at bottom"
  (L92). 明自 → 明白 "clear" (L46).
- **Numeric glitches (value carried in the English, form noised — see below):**
  受伤九十六百一十五人 → 9,615 wounded (garbled 九千六百一十五, L21); 于一九二八年内 →
  "within the year 1938" (impossible 1928 for 1938, L80, inside Chen's paraphrase
  of the Five Ministers' plan).
- **Internal date inconsistency in the quoted Chiang address (left visible, NOT
  altered):** L42 prints 近卫十一月二十二日声明 "Konoe's statement of the twenty-second
  of November"; every other reference in the address gives 十二月二十二日 (22 Dec, the
  correct date of Konoe's third statement). Rendered faithfully as printed
  ("November") since it lies inside a quoted document; the reader can see the slip
  against the surrounding "December 22" references.
- **Source punctuation gap:** L17 (Liu Yuanshen's quoted testimony) omits the
  closing 」 after 戴先生说「临澧的训练是很成功的。」; the quote is closed there and
  Chen's own commentary (其实失败与成功…) resumes outside it, per sense.

### Checks (all green)
- verify_unit ch12: parity 131/131; numbers 0 unresolved (after B07 noise block);
  anchors 16 ok.
- check_align: 131/131, median 4.84 en/han (above the 4.55–4.76 narrative band, in
  line with the two long formal/oratorical quoted documents that dominate the
  chapter). No pair strays >2.2× the median.
- check_structure: parity OK, 16 notes / 0 unresolved anchors, 2 heading levels OK.
- check_content: 0 displacement (171 name occurrences, all in the paired paragraph).
- qc_entities: 0 misses (top: 重庆 x30, 汪精卫 x28, 河内 x20, 东亚新秩序 x20).
- check_register --ref: within tolerance. shall 33% — Chen's deliberate narrating
  "shall" PLUS the period-diplomatic Konoe statement and Chiang's oratory (both use
  "shall" as the register demands); verified deliberate (ch11 B06 also ran 33%).
  Contractions 0.0/1k; em-dash 5.0/1k vs ref 8.3; rhythm CV 0.71.
- Tail verified against source (rule 4 corollary): the 5-paragraph coda (L134–138)
  rendered complete, nothing invented or dropped (idioms 空穴来风, 只闻楼梯响, 节外生枝,
  一子先着, and 多事婆 = Chen Bijun all carried; Dai's closing order verbatim in sense).
- Build: qa_epub PASS (57 files, 153 refs/153 bodies/153 backlinks, all links
  resolve); epubcheck 5.1.0 → 0 fatals / 0 errors / 0 warnings. EPUB now
  **12/43 chapters**.
- setup.sh regression: the ONE known false alarm ("hook stands down on template
  stub") still fails as documented; all other checker regression tests pass.

### Numeric-invariant handling (data/noise.txt, B07 block; check_numbers 0 unresolved)
Real quantities carried in the English: the eighteen-man team; the Fifth and Tenth
Divisions and 30,000 annihilated at Tai'erzhuang; the Japanese-admitted 2,367 dead
(rendered as digits so the checker composes the value) and 9,615 wounded; the
"two, myself and Duanmu Kai"; the "two dynasties of Song and Ming"; 70 million,
450 million people, 12+ million sq km, 5,000 years (all in the English);
Republican years kept literal ("the twenty-seventh year", matching the source
numeral and Part-Two/B06 convention); clock times spelled out. **Noised**
(idiom / name / archaic-numeral / glitch artifacts — value, where real, stays in
the English): 十两 (spurious 12 from 第十两个师团), 九十六百一十五 (garbled 9,615),
万众一心, 五光十色, 矛盾百出, 千辛万苦, 百姓 (老百姓), 阴谋百出, 四万万五千万 (万万=亿,
parser can't compose 450M), 一千二百余万 (余万 form, parser splits it), 一九二八
(glitch for 1938), 阿六 (servant name), 用五 (pen name).

### Notes ledger (16 this batch; 153 cumulative)
First-appearance discipline observed. **NOT re-noted** (already noted B01–B06):
Konoe Fumimaro (ch10), the Three Principles of Peace (ch11), Gao Zongwu / Mei
Siping (ch11), "Director-General" 总裁 (ch11), the Yan Telegram (ch10), Chen Bijun
(ch03), the People's Political Council (ch10), the Jing/Wei proverb (ch11), the
"eighteen men" of the Hanoi team (ch03), the Republican-calendar convention, the
Juntong / Dai Li / Zheng Jiemin, Hanoi / Chongqing / Kunming, Manchukuo, the
Three Principles of the People, the Xi'an Incident (ch06). New notes: (1) the
Eighteen Arhats / Vajra-guardians Buddhist allusion; (2) the battle of
Tai'erzhuang + the disputed casualty figures (fact-check verdict: contested);
(3) Long Yun of Yunnan; (4) the "New Order in East Asia"; (5) 支那/"Shina" as the
derogatory Japanese exonym (rendering-policy note); (6) the Five Ministers'
Conference; (7) the Kōain (Asia Development Board) + the "Tai-Shi Board"; (8) the
Twenty-One Demands + Yuan Shikai; (9) the Nine-Power Treaty + Open Door; (10) the
Treaty of Shimonoseki + the Korea precedent; (11) the Zhanggufeng / Lake Khasan
Incident + Shigemitsu; (12) the Tanaka Memorial + Meiji legacy-policy (**verdict:
generally regarded as a forgery**); (13) the Jinan Incident of 1928 + Tanaka
Giichi; (14) "the Party Leader" 总理 = Sun Yat-sen (vs 总裁 = Chiang); (15) Jin
Xiongbai / Zhu Zijia and his Wang-regime memoir; (16) Hirota Kōki's 1935 Three
Principles.

### Glossary rows added (40 by hand; principals unchanged at 8)
People (22): 岑家焯 Cen Jiazhuo, 余乐醒 Yu Lexing, 龙云 Long Yun, 有田 Arita (八郎),
平沼骐一郎 Hiranuma Kiichirō, 田中义一 Tanaka Giichi, 金雄白 Jin Xiongbai, 朱子家 Zhu
Zijia, 用五 Yongwu (identity unknown), 张季鸾 Zhang Jiluan, 甘乃光 Gan Naiguang, 陈树人
Chen Shuren, 彦慈 Yanci, 孙哲生 Sun Zhesheng (= 孙科 Sun Ke/Fo), 蒋廷黻 Jiang Tingfu,
彭学沛 Peng Xuepei, 陈公博 Chen Gongbo, 周佛海 Zhou Fohai, 广田 Hirota (弘毅), 重光葵
Shigemitsu Mamoru, 袁世凯 Yuan Shikai. Places (8): 台儿庄 Tai'erzhuang, 张鼓峰
Zhanggufeng, 珊瑚坝 Shanhuba, 上清寺 Shangqingsi, 美专校街 Meizhuanxiao Street, 北碚
Beibei, 桂林 Guilin, 滇越路 the Yunnan–Vietnam railway. Organizations (4): 五相会议
the Five Ministers' Conference, 兴亚院 the Kōain, 临澧训练班 the Linli Training Class,
掌故 Zhanggu (HK magazine). Terms (7): 东亚新秩序 New Order in East Asia, 东亚协同体
East Asian Cooperative Body, 田中奏折 Tanaka Memorial, 二十一条款 Twenty-One Demands,
九国公约 Nine-Power Treaty, 马关条约 Treaty of Shimonoseki, 国家总动员法 National
General Mobilization Law. Every row carries a pinyin field; obscure operatives /
minor diary names / uncertain identities marked `provisional`. **Deliberately NOT
given a glossary row:** 总理 (ambiguous — Sun Yat-sen "the Party Leader" vs 内阁总理
"cabinet premier"; the footnote covers Sun). Feed the historical names (有田八郎,
平沼骐一郎, 田中义一, 广田弘毅, 重光葵, 袁世凯, 孙科, 蒋廷黻, and the collaborationist
金雄白, 陈公博, 周佛海) to authority.json on completion.

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — ch12 spec added (drop=2; four merges incl. the
  「用五」先生 name-split; one standalone + two glued numbered-in-parens sub-headings).
  Backward-compatible with ch01–ch11.
- `data/noise.txt` — B07 block (see above). Glossary rows added by hand into the
  sectioned file, idempotent + re-read-verified; the 16 notes merged via
  apparatus_merge.py (numeric character references; anchors verbatim in body text).
