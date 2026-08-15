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

## Batch B08 — ch13 (Part Two, Chapter 3: "Disgrace at Hanoi")

第三章 波诡云谲 风雨欲来 "Chapter 3. Treacherous Tides, a Gathering Storm" — the
largest chapter of Part Two (35,117 source chars). Two structural halves, joined
by an in-text "(本章完)" marker (as in ch12): (a) the operational narrative with a
numbered-in-parens series (一)–(四) — the special personage "Mr. Xu," the order to
verify Wang's departure, the want of inside intelligence, and the arrival of the
action team with arms; and (b) an appended biographical essay on Wang Jingwei whose
sub-heading numbering RESTARTS (一)–(五), with an inner enumerated list 一、–六、 inside
its section (三). 262 body paragraphs; 21 notes (174 cumulative); 84 glossary rows.

### Source handling / structure
- drop=2 (running header `英雄无名-陈恭澍` from `<title>` + the `<h2>` chapter title),
  CONFIRMED against the source XHTML.
- The 279 source `<p>` expand to exactly 283 extracted body lines via 4 `<br/>`,
  proven by a paragraph-by-paragraph comparison to `data/src_epub` (zero mismatches).
  The two `<br/>` paragraphs are L157/158 (a prose pair, folded into a merge) and
  L172–175 (a four-line 律诗, kept as four body lines and rendered as verse `{p}`).
- SIX mid-phrase splits where the SOURCE itself broke one sentence across two `<p>`
  (faithfully reproduced by the extractor), all merged in `clean_batch.py`:
  L61/62 (专事国际情报|由王芄生…); L156/157/158 (…僇笑」。这样|可悲的结局…|汪如九原有知… — a
  three-fragment chain); L162/163 (胡涂的事，天|下最不可思议… — 天|下 mid-word); L202/203
  (才逼他走|上极端… — 走|上极端 mid-word); L228/229 (见客的时候，|礼貌十足…).
- All 15 sub-headings are their OWN `<p>` (all `standalone`; no glued tails): the two
  (一)–(四)/(一)–(五) series and the inner 一、–六、 list. The inner list is rendered
  `#### ` (h3) in the reading.md; the parenthesized sections `### ` (h2).
- Sub-heading numbering RESTARTS for the appended Wang essay — a faithful source
  structure (cf. ch09 §五 before §四), kept verbatim (not footnoted; the "(本章完)"
  marker signals the seam).
- NO note markers `[\d+]` present (grepped). NO images. NO set-off HTML formatting
  (ch06–ch13 all had none); verse recovered with the `{p}` marker (first use in the
  project) — 29 pure-verse body lines carry Wang Jingwei's quoted poems.

### Checks (all green)
- `verify_unit.py ch13`: parity 262/262; numbers 0 unresolved (after the B08 noise
  block); anchors 21 ok.
- `check_align.py ch13`: 262/262, median ratio 4.79 en/han, no pair strays >2.2x
  (essay + quoted-document-heavy, like ch12's 4.84; narrative sits ~4.55–4.76).
- `check_structure.py`: parity OK; anchors 0 unresolved; heading levels OK.
- `check_content.py`: 229 name occurrences, all in the paired paragraph (0 displaced).
- `qc_entities.py` (reconstructed bilingual): 0 misses (top: 河内 x73, 徐先生 x63,
  汪精卫 x44, 魏春风 x21).
- `check_register.py --ref reference/B01_frozen.md`: within tolerance; "shall" 29%
  (Chen's deliberate formality + quoted documents; B06/B07 ran ~33%, verified).
- `qa_epub.py`: PASS (57 files, 50 documents, all links resolve; 174 refs/bodies/
  backlinks). `epubcheck 5.1.0`: 0 fatals / 0 errors / 0 warnings.
- Tail verified against the source (the Japan-surrender / Wang's-death closing
  paragraph and the final 朝中措 ci): faithful and complete.

### Numeric flags — carried vs noised
- CARRIED in the English (real quantities): 二人/两派 → made explicit "the two…" /
  "two factions"; 二十几岁 → "twenty-odd years"; 考生上万 → "over ten thousand";
  十倍 → "ten times"; and the date 三月二十一日 → "twenty-first" (rendered as the
  source prints it, though the Zhongshan Warship Incident is conventionally the
  20th — noted in the footnote).
- NOISED (idioms / names / archaic forms / artifacts; value NOT a quantity), new
  B08 block in `data/noise.txt`: 五短身材, 十八、九 (elided-tens), 百听不厌, 万能,
  一九○五/○三/○六 (fullwidth-zero U+25CB years; English carries 1905/1903/1906),
  十六两/八两 (两 "tael" misread as 2; English carries the tael counts), 百计, 九原,
  十刹海 (place), 两面三刀, 万众响应, 飘零, 吉冈文六 (name), 四万万 (= 4×10^8,
  parses to 50000; English carries "four hundred million"), 零丁, 千古, 零落,
  再三再四 (pre-empts the built-in 再三 orphan bug), 势不两立.

### Digitization glitches (rendered to plain sense; NOT footnoted — mechanical)
- 一九○五 / 一九○三 / 一九○六 — fullwidth ○ (U+25CB) for the zero in years;
  rendered 1905 / 1903 / 1906.
- 云龙 for 龙云 (Long Yun, given-name/surname inverted) — rendered "Long Yun."
- 教亡图存 for 救亡图存 ("saving the nation from ruin") — plain sense.
- 亡我者我也，我不自，谁能亡之 — a character dropped after 我不自 (…自亡/自侮);
  rendered "had I not brought it on myself."
- 则市民前七年 for 则是民前七年 (市 for 是) — "was the pen name…the seventh year
  before the Republic."
- 近卫内各 for 近卫内阁 (各 for 阁, "cabinet") — "Konoe cabinet."
- 玲木 for 铃木 (Suzuki) — "Suzuki."
- 切实贝覆 for 切实具覆/回覆 — "report it soundly."
- 务报员 for 谍报员/收发报员 — "a communications-and-cipher man."
- 两枝左输 for 两枝左轮 (revolver) — "two revolvers."
- 也有人到郑介民 for …归之于郑介民 — "ascribe it to Mr. Zheng Jiemin."
- 总变为他是 for 总以为他是 — "forever taking it that."
- 军校校长奖…攻击时烛发其奸 — 奖 for 蒋 and a garbled clause; rendered "the
  then-Commandant of the Military Academy saw through their treachery."
- 曾、沉死后 for 曾、沈死后 (沉 for 沈, Shen) — "after the deaths of Zeng and Shen."
- 虞美人 ci: the closing 」 is dropped in the source (秋来雕尽…满人间。) — rendered
  as verse; bracket not supplied.

### Notes ledger (21 this batch; 174 cumulative)
First-appearance discipline observed. **NOT re-noted** (already noted B01–B07):
Konoe / the New Order in East Asia, the Three Principles of Peace, Gao Zongwu /
Mei Siping, the Yan Telegram, Chen Bijun, Zeng Zhongming (ch04), the People's
Political Council, Yuan Shikai (ch12), the Nine-Power Treaty, the Twenty-One
Demands, the Tanaka Memorial, Tai'erzhuang, Long Yun, the Xi'an Incident, the
Whampoa/Central Military Academy, "the Party Leader" 总理 = Sun Yat-sen, the
Republican-calendar convention, the Juntong / Dai Li / Zheng Jiemin, Hanoi /
Chongqing / Kunming / Haiphong. New notes: (1) Xifeng — the Juntong's own
detention camp; (2) No. 27 Gao Lang Street / Rue Colombert, the assassination
locale; (3) Chennault & the Flying Tigers / 14th Air Force; (4) the Prince Regent
Zaifeng + the 1910 bomb plot; (5) the famous prison couplet 引刀成一快 and its
later irony; (6) the Tongmenghui + the Min Bao; (7) Zhang Taiyan; (8) Liang Qichao
+ the Royalists; (9) Yuan Shikai's Hongxian monarchy; (10) Borodin; (11) the
Zhongshan Warship Incident (**+ the source's 21st vs the conventional 20th**);
(12) the Ninghan Split; (13) the Marco Polo Bridge Incident; (14) Trautmann's
mediation; (15) Liu Yu & Zhang Bangchang, the puppet-emperor archetype; (16)
Gambetta; (17) Li Yu (the Latter Ruler Li) + "music of a doomed state"; (18) the
Shanhaijing + the Jingwei-bird myth; (19) the First Sino-Japanese War + the
Ryukyus; (20) the bomb-Chongqing allegation (**verdict: uncorroborated**, Chen
himself hedges it); (21) the Gao Zongwu–Tao Xisheng defection of Jan 1940.

### Glossary rows added (84 by hand; principals unchanged at 8)
People (57): 何芝园 He Zhiyuan, 徐先生 "Mr. Xu" (pseudonym), 曾先生 "Mr. Zeng"
(distinct from Zeng Che/Zeng Zhongming), 魏春风 Wei Chunfeng, 阮小姐 Miss Nguyen,
曹师昂 Cao Shi'ang, 谭天堑 Tan Tianqian, 张逢义 Zhang Fengyi, 郑邦国 Zheng Bangguo,
陈步云 Chen Buyun, 黄强 Huang Qiang (Mujing), 稽小姐 Miss Ji, 罗君强 Luo Junqiang,
陈皋 Chen Gao, 谷正鼎 Gu Zhengding, 王宠惠 Wang Chonghui, 宋子文 Song Ziwen, 魏道明
Wei Daoming, 王芄生 Wang Fansheng, 大屋久寿雄 Ōya Kusuo, 汪兆镛 Wang Zhaoyong, 汪兆辛
Wang Zhaoxin, 朱执信 Zhu Zhixin, 梁启超 Liang Qichao, 黄兴 Huang Xing, 章太炎 Zhang
Taiyan, 宋教仁 Song Jiaoren, 陶成章 Tao Chengzhang, 吴樾 Wu Yue, 黄复生 Huang Fusheng,
罗世勋 Luo Shixun, 载沣 Zaifeng, 善耆 Shanqi, 廷杰 Tingjie, 袁克定 Yuan Keding, 杨度
Yang Du, 鲍罗廷 Borodin, 马林 Maring, 越飞 Joffe, 陈炯明 Chen Jiongming, 陈独秀 Chen
Duxiu, 周恩来 Zhou Enlai, 叶挺 Ye Ting, 贺龙 He Long, 张发奎 Zhang Fakui, 沈崧 Shen
Song, 顾孟余 Gu Mengyu, 郑学稼 Zheng Xuejia, 吉冈文六 Yoshioka Bunroku, 唐有壬 Tang
Youren, 陈畊基 Chen Gengji, 刘子蕃 Liu Zifan, 袁尹白 Yuan Yinbai, 孙中山 Sun Yat-sen,
董其昌 Dong Qichang, 元遗山 Yuan Haowen. Places (17): 无锡, 绍兴, 番禺, 三水, 横滨
Yokohama, 里昂 Lyon, 南昌, 武汉, 汉口, 西贡 Saigon, 海防 Haiphong, 槟榔屿 Penang,
新加坡 Singapore, 息烽 Xifeng, 高朗街 Gao Lang Street, 北极阁 Beiji Pavilion, 名古屋
Nagoya. Organizations (6): 同盟会 the Tongmenghui, 民报 the Min Bao, 光复会 the
Restoration Society, 保皇党 the Royalists, 国际问题研究所 the Institute of
International Affairs, 双照楼诗词稿 Verses from the Double-Reflection Tower.
Terms (5): 中山舰事件 the Zhongshan Warship Incident, 宁汉分裂 the Ninghan Split,
五四运动 the May Fourth Movement, 甲午战争 the First Sino-Japanese War, 琉球 the
Ryukyus. Every row carries a pinyin field; obscure operatives / uncertain
readings marked `provisional`. **Deliberately NOT glossaried:** 徐 as a bare
surname beyond the "Mr. Xu" pseudonym row.

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — ch13 spec added (drop=2; six merges incl. three
  mid-word/mid-phrase source splits and one `<br/>` prose pair folded into a
  three-fragment chain; fifteen standalone sub-headings). Backward-compatible.
- `data/noise.txt` — B08 block (see above).
- Glossary: 84 rows added by hand into the sectioned file, idempotent +
  re-read-verified. The 21 notes merged via `apparatus_merge.py` (numeric
  character references; anchors verbatim in body text, not headings).
- First use of the `{p}` verse marker in this project (builder renders
  `<p class="verse">`; `check_structure`/`batch_artifacts` strip the prefix).

## Batch B09 — ch14 (Part Two, Chapter 4: "Disgrace at Hanoi")

第四章 三面受敌 一往无前 "Chapter 4. Beset on Three Sides, Ever Forward" — a very
short bridge chapter (520 source chars), a preview of the action to come: it
frames the operation as three phases and foreshadows its failure ("可是却失败了！").
5 body paragraphs; 0 new notes (174 cumulative, unchanged); 0 new glossary rows.

### Source handling / structure
- drop=2 (running header `英雄无名-陈恭澍` from `<title>` + the `<h2>` chapter title),
  CONFIRMED against `data/src_epub/OEBPS/Text/index_split_000_0013.xhtml`.
- Exactly 6 `<p>`: ONE couplet-style sub-heading with NO number prefix (L3
  `壁垒坚强迎接多方面的挑战`, like ch11's style — its own `<p>`, emitted `standalone`)
  and FIVE body paragraphs (L4–L8). NO `<br/>`, NO images, NO set-off HTML.
- All five body lines end on a terminal char (。/！), so there are NO extractor
  mid-phrase splits — verified p-by-p against the source XHTML (merges [], glued {}).
- NO note markers `[\d+]` present (grepped: "none present"). Confirmed no images.
- `clean_batch.py` ch14 spec added; source conserved OK (5 body paragraphs, 1
  sub-heading).

### Checks (all green)
- `verify_unit.py ch14`: parity 5/5; numbers 0 unresolved (with the B09 noise
  block); anchors 0 ok (no notes).
- `check_align.py ch14`: 5/5, median ratio 5.33 en/han, no pair strays >2.2x. The
  high ratio is expected for a 520-char chapter (small-sample swing; narrative sits
  ~4.55–4.76, prefaces/essays higher) — read the note, did NOT de-formalize.
- `check_structure.py --config checks.json`: parity OK; anchors 174 unresolved 0;
  heading levels OK.
- `check_content.py --config checks.json`: ch14 clean (1 name occurrence, all in
  the paired paragraph, 0 displaced). The remaining flags in the run are
  PRE-EXISTING ch13 name-map artifacts (Miss Nguyen/Oya Kusuo/Yuan Haowen —
  diacritic/variant forms the substring name_map cannot match), unchanged by B09;
  the script exits 0.
- `qc_entities.py` (reconstructed bilingual, headings stripped): 0 misses
  (census: 汪精卫 x1, 制裁 x1).
- `check_register.py --ref reference/B01_frozen.md`: within tolerance (contractions
  0.0/1k, em-dash 4.0/1k vs ref 8.3, rhythm noisy — little dialogue). "shall" 0%
  (this chapter simply has no "shall"; Chen's narrating "shall" remains deliberate
  where it occurs elsewhere).
- `qa_epub.py`: PASS (57 files, 50 documents, all links resolve; 174 refs/bodies/
  backlinks). `epubcheck 5.1.0`: 0 fatals / 0 errors / 0 warnings / 0 infos.
- Tail verified against the source (L8 那么，败在那里？…也作了不偏不倚的文代。):
  faithful and complete.

### Numeric flags — carried vs noised
- CARRIED in the English (real quantities): 三个阶段 → "three phases"; 两个半月 →
  "two and a half months"; 十天 → "ten days"; 一天 → "a single day"; 两度 → "twice
  over"; 第一/第二/最后阶段 → "first/second/last phase".
- NOISED (elided-tens approximations; the "N or N+1" range IS carried in the
  English), new B09 block in `data/noise.txt`: 十七、八 (→ "seventeen or eighteen"),
  四、五 (→ "four or five"), 三、四 (→ "three or four", appears twice), 二、三 (→
  "two or three"). Without these the checker reads the trailing 八/五/四/三 as bare
  counts and orphans them.

### Digitization glitches (rendered to plain sense; NOT footnoted — mechanical)
- 江案 for 汪案 ("the Wang case", 江 for 汪) — appears twice (L5, L6); rendered
  "the Wang case" both times.
- 纯粹去百姓 for 纯粹老百姓 (去 for 老, "plain ordinary folk") — "merely so many
  plain civilians."
- 出卖而国家利益 for 出卖我国家利益 (而 for 我) — "selling out our nation's interests."
- 不偏不倚的文代 for …交代 (文 for 交, "an account/reckoning") — "an even-handed
  reckoning has been given."
- 违涉重洋 for 远涉重洋 (违 for 远, the set phrase "travel far across the oceans") —
  rendered "crossed far over the seas."

### Notes ledger (0 this batch; 174 cumulative)
No new notes — a very short bridge chapter, and its two allusive idioms both had
earlier first appearances that were rendered inline without a footnote, so
first-appearance discipline forbids newly noting them here:
- 为虎作伥 "play the tiger's cat's-paw" — first appeared ch02 ("a tiger's
  accomplice"), again ch13 ("playing the tiger's cat's-paw"); rendered here
  "playing the tiger's cat's-paw" to match the most recent form.
- 人人得而诛之 "any man might rightfully put him to death" — first appeared ch02/ch07.
**NOT re-noted** (already covered B01–B08): the sanction euphemism 制裁, Mr. Dai /
the Juntong, Wang Jingwei, the Republican-calendar convention, 留学生 "returned
students", the special-police training.

### Glossary rows added (0; principals unchanged at 8)
ch14 introduces no new referent. All names/terms it uses (汪精卫 Wang Jingwei, 戴先生
Mr. Dai, 制裁 "sanction") are already settled rows. Reused, not re-added.

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — ch14 spec added (drop=2; merges []; glued {}; one
  standalone couplet sub-heading). Backward-compatible.
- `data/noise.txt` — B09 block (four elided-tens forms; see above).
- No new notes (apparatus_merge not invoked), no new glossary rows.

## Batch B10 — ch15 (Part Two, Chapter 5: "Disgrace at Hanoi")

第五章 博浪一击 误中副车 "Chapter 5. A Blow at Bolang, the Wrong Carriage Struck" —
the CLIMAX and second-largest chapter of Part Two (~21,830 source chars). The
assassination attempt itself and its failure: Yu Lexing's poison-bread "soft
action" that fails testing and the gas device; the "sanction order" arriving in
the small hours of 19 March of the twenty-eighth year (1939); the botched car
chase across the Red River bridge; the night raid on No. 27 Gao Lang Street where
Wang Luqiao shoots the man under the bed — Zeng Zhongming, NOT Wang Jingwei (the
title's 误中副车); three men captured; and a documentary section (五) quoting and
correcting three real books. 225 body paragraphs; 11 new notes (185 cumulative);
~13 new glossary rows; principals unchanged at 8.

### Source handling / structure
- drop=2 (running header `英雄无名-陈恭澍` from `<title>` + the `<h2>` chapter title),
  CONFIRMED against `data/src_epub/OEBPS/Text/index_split_000_0014.xhtml` (parsed
  block-by-block: 1 `<h2>` + 235 `<p>`, zero mismatches vs the extracted text).
- FIVE numbered-in-parens sub-headings (一)–(五), each its own `<p>`, all
  `standalone` (no glued tails): L3/L51/L97/L131/L185. NO `<br/>`, NO images, NO
  set-off HTML (confirmed).
- FIVE extractor mid-phrase splits (source `<p>` breaking one sentence), merged as
  body-line pairs and re-confirmed against the XHTML: L13/14 (弹是子弹，药就|是),
  L153/154 (墙里面，|有一方小院落, a comma split), L167/168 (这不是汪|精卫, split
  mid-name), L175/176 (最愉快的一段|时刻), L208/209 (「午夜□□」那两|节故事).
- The MANY ；/：-ended lines are DELIBERATE separate `<p>` and were NOT merged: the
  announced attack plan (L59 lead-in + L60–65 bullets), the three decisions (L88/90),
  the job-division (L143/144), the reader-questions (L125), and the three
  quoted-book lead-ins in section (五) (L189, L210) with their multi-`<p>` quoted
  blocks kept whole. `clean_batch.py` ch15 spec added; source conserved OK (225 body
  paragraphs, 5 sub-headings).
- NO note markers `[\d+]` present (grepped: "none present", as through B09).

### Checks (all green)
- `verify_unit.py ch15`: parity 225/225; numbers 0 unresolved (with the B10 noise
  block); anchors 11 ok.
- `check_align.py ch15`: 225/225, median ratio 4.60 en/han, no pair strays >2.2x.
- `check_structure.py --config checks.json`: parity OK; anchors (all notes) 0
  unresolved; heading levels OK.
- `check_content.py --config checks.json`: **ch15 clean** (226 name occurrences,
  all in the paired paragraph, 0 displaced). The Yu Lexing full-name spots (源 余乐醒
  vs 乐醒兄) are rendered "Brother Yu Lexing" at the three full-name occurrences to
  carry the glossary form. The run's remaining flags (ch07 Zhanggu ×1, ch08 Shunde
  ×3, ch13 Miss Nguyen ×7 / Oya Kusuo / Yuan Haowen) are the KNOWN PRE-EXISTING
  name-map artifacts, unchanged from HEAD; the ch13 change below removed the 郑邦国
  entry but added no new displacement (ch13 source has 郑邦国, no glossary key now).
- `qc_entities.py` (reconstructed bilingual, headings stripped): 0 misses (census
  top: 徐先生 ×29, 河内 ×25, 唐英杰 ×24, 魏春风 ×18, 制裁 ×17, 张逢义 ×16, 陈邦国 ×16).
- `check_register.py --ref reference/B01_frozen.md`: within tolerance (contractions
  4.9/1k from the heavy dialogue; shall 9% — Chen's narrating "shall", deliberate;
  em-dash 9.0/1k; rhythm CV 0.63). Did NOT de-formalize the two long quoted-book
  blocks.
- `qa_epub.py`: PASS (57 files, 50 documents, all links resolve; 185 refs/bodies/
  backlinks). `epubcheck 5.1.0`: 0 fatals / 0 errors / 0 warnings / 0 infos.
- Tail verified against the source (L231 制裁汪精卫的工作，并不到此为止… and the L229–230
  举一个例 / 吴稚晖 passage before it): faithful and complete.

### CRITICAL name-trap RESOLVED — 陈邦国 / 郑邦国
ch13 (B08) recorded this action-team member as 郑邦国 "Zheng Bangguo" (4×); ch15
writes 陈邦国 "Chen Bangguo" 16× consistently, AND the semi-official Biography of Dai
Yunong quoted in ch15 §(五) also writes 陈. Resolved to the better-attested form
**Chen Bangguo (陈邦国)**: (a) renamed the glossary key 郑邦国 → 陈邦国 (en "Chen
Bangguo", pinyin Chén Bāngguó, status provisional) with a note recording the
source's own 陈/郑 discrepancy; (b) updated the BUILT ch13 unit (`out/ch13_reading.md`
Zheng Bangguo → Chen Bangguo, 4×; `ch13_en.json` regenerated; ch13 re-verified —
numbers 0, anchors 21 ok, parity 262/262); (c) footnoted the discrepancy at the
first ch15 occurrence (rule 4). Wikipedia's "陈邦国" is a different modern PRC
official, not this figure; the 十八罗汉 secondary rosters vary (often 郑), so the
romanization stays provisional.

### Numeric flags — carried vs noised (check_numbers 0 unresolved)
- CARRIED as digits / explicit words (real quantities): dates 二十八年三月十九/二十/廿/
  二十一/二十二日; times 二时许, 十一时四十分, 四点钟, 四点五十分, 零时过九分 (rendered
  "nine minutes past the zero hour"); Republican years 三十年, 六十八年 (1979), 七十年
  (1981), 四十八年 (1959), 三十七/三十八年; distances 九十公里 (90 km), 三公里, 三百公尺,
  两百公尺; money 四千五百 (4,500), 五百, 九张 (nine notes); page/volume 二○三页 (203),
  九十四页 (94), 四十一–四十四页, 第十一册, 六册, 第五册; counts 七个人, 三组/三辆, 三枪,
  五人, 三人; 第五十四次 (Fifty-fourth). Where the source used a bare 二人/三同志 etc., a
  matching "the two of them / three in all / both" was added to the English so the
  count survives (pairs 29, 38, 58–60, 89, 102, 129, 169, 212).
- NOISED (data/noise.txt B10 block; the VALUE is still carried in the English):
  八、九百, 四、五百, 四、五十, 四、五样, 五、六响, 五、六个, 七、八分钟 (elided-tens /
  "N or N+1" spans); 三两天, 两三分钟, 一两分钟, 十来分钟; the fullwidth-zero page ref
  二○三 (○ = U+25CB → "203"); 五百一张 (the greedy matcher read 五百一 as 501); 万不能
  (万 as intensifier, not 10000); 三桃山 (place-name 三, not the count 3). ORDERING FIX:
  the B09 short forms 四、五 / 三、四 / 二、三 were moved BELOW the B10 compounds that
  contain them (四、五百 etc.), or the short rule fires first and orphans the leftover
  百/十 (100/10).

### Digitization glitches (rendered to plain sense; NOT footnoted — mechanical)
Single-character substitution classes, pervasive in this chapter:
- 先→光: 戴光生 → 戴先生 "Mr. Dai" (L12); 曾光生 → 曾先生 "Mr. Zeng" (L36).
- 卫→术: 汪精术 → 汪精卫 "Wang Jingwei" (L53).
- 鸣→呜: 曾仲呜 → 曾仲鸣 "Zeng Zhongming" (recurring, L176/206/207/208/209/213/215/218/221).
- 汪→江: 江之卑劣 → 汪之卑劣 "so base as Wang" (L230, same class as ch14's 江案).
- 文↔交 (section 五's quoted books): 摘录交内→文内 (L184), 本交→本文 (L190), 官交书→官文书
  (L193), 汪交惺→汪文惺 "Wang Wenxing" (L206), 交杰→文杰 "He Wenjie" (L209).
- 声→聋: 小聋叫他 → 小声 "in a low voice" (L159); 枪聋 → 枪声 "gunfire" (L188, L215).
- Others: 「内工作」→「河内工作」 (dropped 河, L54); 引溥→引导 "guide" (L61); 一片一斤→一片一片
  "slice by slice" (L41); 解择→解释 "explained" (L18); 注妻→汪妻 + 陈壁君→陈璧君 "Wang's
  wife Chen Bijun" (L128); 警犭→警犬 "guard dogs" (L188); 我达以为→我还以为 "I still
  supposed" (L176); 闲枪声→闻枪声 "hearing the shots" (L207); 历史资科→资料 (L8); 将总统
  秘录→蒋总统秘录 (L181); 其其职责→其职责 (dittography, L141); 什糜→什么 (L92); 舂风→春风
  "Wei Chunfeng" (L37/L134); 共中→其中 (L120/187/203/212); 时问→时间 "time" (L90/223);
  某次→其次 "secondly" (L145); 房问→房间 "room" (L218); 隧着→随着 "as" (L231); 违个→这个
  "this" (L225); 走一件→是一件 (L227); 遍是→便是 (L216); 拒动→扭动 "worked the handle"
  (L162); 相昆连→相毗连 "adjoined" + 仲呜夫好→夫妇 + 行凶老→行凶者 + 层之卧室→the bedroom
  (L206–208); 驳亮枪→驳壳枪 "Mauser" (L207); 锻羽→铩羽 "clipped wings" (L122);
  演示文稿→演示 "a demonstration" (anachronism, L44). None footnoted (mechanical typos).
- 汪逆 / 汪某 are NOT glitches: 汪逆(精卫) = "the traitor Wang (Jingwei)", 汪某 = "the man
  Wang" — rendered faithfully. The □□ in 「午夜□□」 (L208) is a source lacuna, kept as "□□".

### Notes ledger (11 this batch; 185 cumulative)
New notes (first-appearance-disciplined): the Red River / Pont Doumer (Long Bien)
bridge; the 陈/郑 Bangguo surname discrepancy; the Da Le / Dan Dao / San Tao Shan
resort-name discrepancy; the three real quoted books with scholarship verdicts
(蒋总统秘录, 戴雨农先生传, 汪政权的开场与收场 — all real, semi-official / journalistic,
corroborating in the main); 行状 (Wang's 曾仲鸣先生行状 eulogy); Wang's apologia 举一个例
+ the doctored National Defense Council record; Wu Jingheng (Zhihui); the Hiranuma
cabinet; the maxim 罪不及妻孥.
**NOT re-noted** (already covered earlier): the TITLE allusion 博浪一击/误中副车 —
Zhang Liang's Bolang ambush and "striking the wrong carriage" was noted in **ch04**
(that note even points forward, "It also titles a later chapter"); the sanction
euphemism 制裁 / 制裁令 (B01/B06); Mr. Dai / the Juntong; Wang Jingwei; Zeng Zhongming
(the person); 朱执信 Zhu Zhixin (glossary-identified, peripheral here); No. 27 Gao
Lang Street / the Continental Hotel (B08); the Republican-calendar convention;
不入虎穴焉得虎子 and 打草惊蛇 (transparent from context — not padded).

### Glossary rows added (~13 by hand; principals unchanged at 8)
- people: 陈邦国 Chen Bangguo (renamed from 郑邦国); household/witnesses from the quoted
  essay — 方君璧 Fang Junbi (attested), 朱媺 Zhu Mei, 何文杰 He Wenjie, 汪文惺 Wang
  Wenxing (attested), 陈国琦 Chen Guoqi, 戴芸生 Dai Yunsheng, 何就 He Jiu, 陈国星 Chen
  Guoxing, 汪圯 Wang Yi. (唐英杰 Tang Yingjie, 余鉴声 Yu Jiansheng, 平沼骐一郎 Hiranuma
  Kiichirō, 金雄白 Jin Xiongbai / 朱子家 Zhu Zijia, 吴敬恒 Wu Jingheng, 朱执信 Zhu Zhixin
  already existed from B08 — reused, not re-added.)
- places: 红河大桥 the Red River bridge (attested); 打叻 Da Le (with the Dan Dao / San
  Tao Shan variant note).
- organizations: 东方汇理银行 the Banque de l'Indochine (attested).
- The three quoted BOOK titles are handled by footnotes, NOT glossary rows: a glossary
  entry keyed on the full hanzi title cross-flagged earlier chapters (ch10/ch13
  render the same titles slightly differently), so they were left out of the ledger.
  Every glossary row carries a `pinyin` field (qc_entities requirement).

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — ch15 spec added (drop=2; five body-line-pair merges;
  glued {}; five standalone (一)–(五) sub-headings). Backward-compatible.
- `data/noise.txt` — B09+B10 elided-tens block reordered longest-first (compounds
  before the bare 四、五 / 三、四 / 二、三), plus B10 entries (see above).
- `glossary.json` — 郑邦国 renamed to 陈邦国; ~12 rows added; sectioned, hand-merged.
- `out/ch13_reading.md` + `out/ch13_en.json` — Zheng Bangguo → Chen Bangguo (name
  reconciliation; ch13 re-verified green).

---

## Batch B11 — ch16 (Part Two, Chapter 6)

第六章 奸伪卑劣 寿张为幻 "Chapter 6. Vile Treachery, Illusions Undone" — the
reckoning-and-indictment chapter closing Part Two. Chen owns the Hanoi failure,
escapes to Chongqing, then mounts a documentary indictment of Wang Jingwei:
he quotes IN FULL two of Wang's own texts — the eulogy 「曾仲鸣先生行状」 (dated
6 Apr 1939) and the apologia 「举一个例」 (9 Apr 1939, enclosing the doctored record
of the 国防最高会议第五十四次常务委员会议 with its attendee roster) — rebuts them, and
copies out Chiang's 17 Apr press conference and Wu Jingheng's 9,000-word essay
「对汪精卫「举一个例」的进一解」. 116 body paragraphs; **8 new notes (193 cumulative)**;
**34 glossary rows** added. All checks green; qa_epub PASS; epubcheck 0/0/0/0.
EPUB now **16/43 chapters**.

### Structure
- drop=2 (running header 英雄无名-陈恭澍 + <h2>). Confirmed p-by-p against
  data/src_epub/OEBPS/Text/index_split_000_0015.xhtml: **1 <h2> + 121 <p>**, no
  <br/>, no <img>, no set-off formatting — zero mismatches.
- FOUR numbered-in-parens sub-headings (一)-(四): (一),(三),(四) STANDALONE (their own
  <p>); (二) GLUED onto the tail of a preceding <p> (cf. ch08) and split off. Rendered
  "(1)"–"(4)".
- TWO mid-phrase splits MERGED (the source itself broke one sentence across two <p>,
  both inside quoted Wang documents): L65/66 (行状: …茫茫后死之感，何时|已乎！) and
  L96/97 (举一个例: …何况现时|除第三国际外…). 121 − 2 merges − 3 standalone headings =
  116 body; +1 glued heading = 4 sub-headings.
- The meeting-record ATTENDEE ROSTER inside 举一个例 breaks across three <p> (L84 出席,
  L85 列席, L86 主席/秘书长/秘书主任): DELIBERATE document formatting, NOT extractor
  splits — kept as separate paragraphs, NOT merged (cf. ch12/ch13/ch15 quoted docs).
- In-text "(第六章完)" coda at L117 (rendered "(End of Chapter Six.)"), after which four
  <p> close Part Two and bridge to Part Three (Chen recalled, "punishment of the spirit,"
  reassigned to Shanghai; Wang Luqiao already arrested there).
- Source note markers `\[\d+\]`: **none present** (grepped; none through B11).

### Checks (all green)
- verify_unit ch16: parity 116/116; numbers 0 unresolved; anchors 8 ok.
- check_align: 116/116, median ratio **4.78 en/han** (document-heavy, in band with
  ch12 4.84 / ch13 4.79; the two long Wang documents + Wu essay lift it, as expected).
- check_structure: ALL PASS (parity + 193 anchors, 0 unresolved).
- check_content: ch16 **182 name occurrences, 0 DISPLACED**. The overall nonzero exit
  is ONLY the KNOWN pre-existing artifacts (ch07 Zhanggu ×1, ch08 Shunde ×3, ch13
  Miss Nguyen/Oya Kusuo/Yuan Haowen ×9 — diacritic/variant substring-match artifacts,
  unchanged; the 34 new glossary rows introduced NO new displacements).
- qc_entities: 0 misses (census top: 曾仲鸣 ×33, 汪精卫 ×19, 河内 ×16, 重庆 ×16, 艳电 ×13).
- check_register --ref B01_frozen: within tolerance (contr 0.0/1k, shall 0%, em-dash
  8.7/1k, sent med 25, rhythm 0.67).
- qa_epub PASS (57 files, all links resolve); epubcheck 0 fatals/0 errors/0 warnings.
- TAIL verified against source: the (第六章完) coda (L115), the three giant polemic
  paragraphs' tails (L112 …如南京议和之不再提及是也; L113 …无法得他们表面化; L114 …追悔也
  莫及了！再会！), and the closing 上海滩 paragraph (L121) — all faithful.

### Notes ledger (8 this batch; 193 cumulative)
New notes (first-appearance-disciplined): the chapter TITLE source (奸伪卑劣 from Chiang's
11 Apr 1939 diary; 寿张为幻 flagged as a corrupt/uncertain glyph, rendered by sense
"Illusions Undone"); 岳忠武十二金牌 (Yue Fei recalled by twelve gold tablets, killed on
Qin Hui's contrivance); Wang's death-poem couplet 引刀成一快，不负少年头 (1910 prison poem);
the Munich/Sudetenland/哈柴 Hácha analogy (Sep 1938 Munich, Mar 1939 Hácha); 梁孟 Liang
Hong & Meng Guang (the proverbial devoted couple, ironic); the 卫/-wei pun (近卫 Konoe +
汪精卫 Wang, the "Duet of the Two Weis"); 甲午/庚子 (the 1895 Shimonoseki and 1900 Boxer
"humiliating peaces"); the 1935 察哈尔 Chahar affair (Wang's removal of Song Zheyuan).
**NOT re-noted** (covered earlier): 行状 and 举一个例 (both NOTED in ch15 at first mention —
here quoted in full); the doctoring of the meeting record (ch15); Wu Jingheng (Zhihui)
(ch15); Trautmann + his 1937 mediation (ch13); the Konoe "New Order in East Asia" (ch12);
艳电 the Yan Telegram (B06); 制裁 "sanction" (B01/B06); the 1910 Prince Regent plot /
Zaifeng (ch10/ch13); Yin Rugeng (ch02); Korea's annexation via Shimonoseki (ch12);
the Three Principles of the People, the Xi'an Incident, the Marco Polo Bridge Incident,
the Nine-Power Treaty (glossary/earlier). 秦桧, 李完用, 吴三桂, 溥仪 handled by the new
glossary rows (which decode the "white iron / tungsten steel" jab), not separate notes.

### Glossary rows added (34 by hand; every row carries a `pinyin` field)
- Meeting-record roster & officials: 于右任 Yu Youren, 居正 Ju Zheng, 孔祥熙 Kong Xiangxi
  (H. H. Kung), 翁文灏 Weng Wenhao, 邵力子 Shao Lizi, 陈立夫 Chen Lifu, 陈果夫 Chen Guofu,
  董显光 Dong Xianguang, 张群 Zhang Qun, 徐堪 Xu Kan, 徐谟 Xu Mo, 顾祝同 Gu Zhutong (Mo-san),
  白崇禧 Bai Chongxi (Jiansheng), 唐生智 Tang Shengzhi (Meng-xiao), 徐永昌 Xu Yongchang
  (Ci-chen; source 次展/次辰 = misprint for 次宸), 陶德曼 Trautmann, 川樾 Kawagoe.
- Traitor/puppet archetypes in Wu's essay: 秦桧 Qin Hui, 李完用 Yi Wan-yong, 吴三桂 Wu
  Sangui, 溥仪 Puyi, 哈柴 Hácha, 张伯伦 Chamberlain, 苏锡文 Su Xiwen, 梁鸿志 Liang Hongzhi.
- Nationalist elders: 李石曾 Li Shizeng, 张溥泉 Zhang Puquan (= Zhang Ji).
- 行状 revolutionaries: 方君瑛 Fang Junying, 黎仲实 Li Zhongshi, 俞云纪 Yu Yunji.
- Hanoi narrative: 丹娜 Dana (the métisse cover-driver, provisional), and the three
  captured (cover names, provisional): 袁伯勋 Yuan Boxun, 孙亚东 Sun Yadong, 杨卫河 Yang
  Weihe.
- Renderings REUSED (already in glossary): 曾仲鸣, 方君璧, 汪精卫/汪兆铭, 陈璧君, 王鲁翘,
  唐英杰, 陈邦国 (Chen Bangguo — the B10 resolution held), 陈步云, 余鉴声, 张逢义, 余乐醒,
  岑家焯, 曹师昂, 谭天堑, 徐先生, 魏春风, 阮小姐, 方炳西, 戴笠, 龙云, 吴敬恒, 金雄白/朱子家,
  何文杰, 汪文惺, 陈国琦, 王克敏, 殷汝耕, 顾孟余, 陈独秀, 载沣, 近卫文麿, 林柏生, 高宗武,
  宋哲元, 陈布雷, 王宠惠, 黄复生. Western contemporaries (Hitler, Mussolini, Lenin, Stalin,
  Trotsky) rendered directly, NOT glossary'd. The two quoted Wang documents + the three
  books are handled by FOOTNOTES (ch15), NOT glossary title-rows (which cross-flag).

### Digitization glitches (rendered to plain sense; LISTED, none footnoted — mechanical)
Same single-character-substitution classes as ch15. Representative:
- 愔弱→懦弱 (L5); 我地→我倒 (L6); 张皇失揩→失措 (L14); 不移深入→不够 (L15); 室故→事故 +
  傅仲鸣→曾仲鸣 + 曾仲呜→曾仲鸣 (L28); 全译木→全译本 (L29); 这梗→这种 (L30); 透木眼→透视眼
  + 着到→看到 (L31); 大大力力→大大方方 (L45); 拙笨的迪→连 + 安高人→安南人 (L46).
- In the quoted 「汪政权…」 passage: 著作→轰炸 + 文侯→文杰 + 大砖→大碍 + 轨可能→就可能 +
  地体→她体 + 江文惺→汪文惺 + 绉着→皱着 + 丈杰→文杰 + 力君璧→方君璧 (L56); 找个人→我个人 (L61).
- In the 行状: 造七月→迨七月 + 若被任/举→君被任/举 (recurring) (L68/69); 九首→九省 +
  倍簁→倍蓰 + 视转→视线 + 之误→之谋 (L71); 家专→家事 (L74, L81) + 目砚→目视 (L74).
- In 举一个例 / meeting record: 三月二十七月→二十七日 (L78); 国防最高会机→会议 (L84); 徐次展/
  次辰→次宸 + 叫德→此德 + 范圈→范围 (L87/88); 却此→即此 (L93).
- In Wu's essay (L110–114): 吴敬桓→吴敬恒 + 庄谐杂件→杂陈 (L110); 形于笔褚→笔楮 (L100);
  狠狠→狼狈 + 会先生→曾先生 + 汪民→汪氏 + 一张于→一登于 + 陈整君→陈璧君 + 研主张→商主张 +
  通国研→所 + 详细捕驳→批驳 + 全几→全国 + 宜傅→宣传 + 他订己→他自己 + 常此→当此 + 江氏→汪氏
  (recurring) (L112); 背寒追媛→趋暖 + 面心里→而 + 看白粉→着 + 妄前→台前 + 日木→日本 +
  明划→明确 + 辨护→辩护 + 鸡道→岂道 + 逻缉→逻辑 (L113); 长冶→长治 + 看想→设想 + 会经→曾经 +
  保持看/照看→着 + 贯澈→贯彻 (L107/108/114). NUMBER-garbles carried in the English and
  noised: 四万百五千百→四万万五千万 (450 million), 六十万百→六十万万 (~600 million).
- Not glitches: 汪逆 = "the traitor Wang", 汪某 = "the man Wang", 汪氏 = "Wang" — rendered
  faithfully. 王 xx (L14) is a source REDACTION of an assassinated man's name, kept as
  "Wang So-and-so".

### data/noise.txt — B11 block appended (10 entries, each commented)
七上八下, 危机四伏, 九江, 千百 (何止千百), 百余万 ("over a million", carried in words),
万不得已, 初一二三 (dated 1/2/3), 二 O 五 (page 205, Latin-O + spaces), and the two
number-garbles 四万百五千百 / 六十万百. All strip SOURCE approximations/glitches only;
real values carried in the English.

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — ch16 spec added (drop=2; merges [(65,66),(96,97)];
  glued {48: (二)…}; standalone [3,76,111] = (一),(三),(四)). Backward-compatible.
- `data/noise.txt` — B11 block (see above).
- `glossary.json` — 34 people rows added by hand (sectioned; every row has `pinyin`).

## Batch B12 — ch17 (Part Two, Chapter 7)

第七章 临深履薄 锲而不舍 "Chapter 7. Treading Thin Ice, Never Relenting" — the
seventh chapter of Part Two, following the reckoning-and-indictment chapter
(ch16). Recalled to Chongqing, given a "punishment of the spirit," idled as
Acting Chief of the Third Section, then reassigned to Shanghai over a farewell
banquet, Chen presses on against Wang. Three sub-sections: (一) the grinding
pain of failure and the return to Chongqing; (二) the comrades still at Hanoi
and their follow-up actions — anchored by a quoted autograph letter from Wang
Jingwei to 龙云 Long Yun (dated 30 March 1939, nine days AFTER the sanction, so
NOT its cause) and a long quotation from Kagesa Sadaaki's memoir and 蒋总统秘录
on Wang's flight, the 三点协议事项 and the June 1939 Tokyo talks; (三) the renewed
thousand-li pursuit — Chen's Shanghai reassignment, his last parting from Dai
Li, and Wang Luqiao's arrest (14 July 1939) in the French Concession. 147 body
paragraphs; **9 new notes (202 cumulative)**; **49 glossary rows** added. All
checks green; qa_epub PASS; epubcheck 0/0/0/0. EPUB now **17/43 chapters**.

### Structure
- drop=2 (running header 英雄无名-陈恭澍 + <h2>). Confirmed p-by-p against
  data/src_epub/OEBPS/Text/index_split_000_0016.xhtml: **1 <h2> + 151 <p>**, no
  <br/>, no <img>, no set-off formatting — zero mismatches.
- THREE numbered-in-parens sub-headings (一)-(三), each STANDALONE (its own <p>,
  blocks 1/43/106): (一)失败之苦是非常折磨人的, (二)留在河内的同志们还有后续行动,
  (三)千里追踪奋勇杀敌的再出发. Rendered "(1)"-"(3)".
- ONE mid-phrase split MERGED (the source itself broke one sentence across two
  <p>, inside the quoted Kagesa memoir): L74/75 (…我(汪氏)决不过问，| 断然引咎下野，
  以明心迹。」 — a comma split). 151 − 1 merge − 3 standalone headings = 147 body.
- The tail L151/L152 read as run-on but each is a COMPLETE <p> ending on a
  terminal char (。), so NOT merged.
- DELIBERATE separate <p> kept whole (NOT merged): the six-point 南华日报 list
  (L10 lead-in; L11-14, points 二/三/四 glued in one source <p> at L12); the
  quoted Wang→Long Yun letter (L50 lead-in; L51 salutation ends ：; L52-53 body);
  the 三点协议事项 (L60 lead-in; L61-63); the quoted Kagesa memoir (L66/L73
  lead-ins) and 蒋总统秘录 excerpts (L78/L80/L85/L89 lead-ins); the 板垣 four-point
  talks (L80 lead-in; L81-84); the "使我难以忘怀的是─" dash lead-in (L112 → L113-117).
- NO in-text "(第七章完)" coda; the final <p> (L153) FORWARD-references the book's
  后记 accounting for the 十九个 Hanoi participants — a forward reference, not a cut.
- Source note markers `\[\d+\]`: **none present** (grepped; none through B12).

### Checks (all green)
- verify_unit ch17: parity 147/147; numbers 0 unresolved; anchors 9 ok.
- check_align: 147/147, median ratio **4.78 en/han** (document-heavy, identical to
  ch16 4.78; the quoted letter + Kagesa/秘录 excerpts lift it, as expected/flagged).
- check_structure: ALL PASS (parity + 202 anchors, 0 unresolved).
- check_content: ch17 **225 name occurrences, 0 DISPLACED** ("all in the paired
  paragraph"). The overall nonzero exit is ONLY the KNOWN pre-existing artifacts
  (ch07 Zhanggu ×1, ch08 Shunde ×3, ch13 Miss Nguyen/Oya Kusuo/Yuan Haowen ×9 —
  diacritic/variant substring-match artifacts, unchanged). NOTE: two would-be new
  glossary keys were caught cross-flagging and corrected before final: 小巷子
  ("Little Lane") is a COMMON NOUN appearing literally in ch06/07/13/15 — the row
  was REMOVED (Xiaoxiangzi is rendered inline in ch17, no row); and 杜美路 was fixed
  from "Rue Doumer" to the glossary's "Route Doumer" in the ch17 text.
- qc_entities: 0 misses (census top: 河内 ×52, 重庆 ×33, 汪精卫 ×19, 军统 ×13,
  汪兆铭 ×11, 制裁 ×10, 毛人凤 ×9).
- check_register --ref B01_frozen: within tolerance (contr 0.0/1k, shall 43%
  [deliberate — Chen's formal narration + the quoted Wang letter/Kagesa memoir;
  read the note, not de-formalized], em-dash 6.4/1k, sent med 25, rhythm 0.62).
- qa_epub PASS (57 files, all links resolve); epubcheck 0 fatals/0 errors/0 warnings.
- TAIL verified against source: the three-sides-beset paragraph (L151), the
  Nanjing/direct-deployment paragraph (L152), and the closing 后记/十九个 forward
  reference (L153) — all faithful. The two longest quoted passages re-verified
  clause-by-clause against the source (rule 4): the Wang→Long Yun letter (L52/53)
  and Wang's peace-government "thinking" paragraph (L74) — complete, no omission,
  no fabrication.

### Notes ledger (9 this batch; 202 cumulative)
New notes (first-appearance-disciplined): 志舟 Zhizhou (Long Yun's courtesy name,
so the reader sees the letter is to Long Yun); No. 76 极司菲尔路 Jessfield Road (the
Wang regime's notorious secret-service HQ under Ding Mocun/Li Shiqun); 长板坡
Changbanpo (the Peking-opera aria of Zhao Yun, drunk bravado); 杜公馆 the Du
residence (Du Yuesheng, Green Gang boss, opposite Chen's lodging); 青天白日满地红旗
the ROC national flag (and the added "Peace/Anti-Communism/Reconstruction"
streamer); 百梅 Baimei (obscure in source — the Nov 1938 Shanghai secret talks;
uncertainty flagged, verdict stated); 戴雨农先生全集 the Complete Works of Mr. Dai
Yunong (1979 Nationalist commemorative source — read with that in mind, like the
Biography noted in B10); 沪滨三次历险实录 the True Record of Three Perils on the
Shanghai Shore (Zheng Xiuyuan's memoir Chen quotes); the Qiantang bore (八月中
钱塘江口的涨潮, the tidal-bore simile for the bombers).
**NOT re-noted** (covered earlier, per the ledger): 制裁 "sanction" (B01/B06); 汪逆/
汪某/汪氏 the traitor Wang forms (B06); 艳电 the Yan Telegram (B06); Konoe & his
"New Order in East Asia" / the Konoe statement (ch12); 曾仲鸣 Zeng Zhongming
(ch15/ch16); 梅机关 the Ume Kikan and 影佐祯昭 Kagesa (glossary; text self-glosses);
the Three Principles of the People, the Blue Shirt Society, the Whampoa/academy
系统, the Republican-calendar convention (B01–B06); 制裁 the "soft action"药/面包
episode (ch15); 蒋总统秘录 (ch15). New cast handled by GLOSSARY rows (below), not
separate notes.

### Glossary rows added (49 by hand; every row carries a `pinyin` field)
- People (30): 王兆槐 Wang Zhaohuai, 王持平 Wang Chiping, 周伟龙 Zhou Weilong, 徐钟奇
  Xu Zhongqi, 赵世瑞 Zhao Shirui, 陶一珊 Tao Yishan, 赵理君 Zhao Lijun, 胡尚武 Hu
  Shangwu, 白绳祖 Bai Shengzu, 潘其武 Pan Qiwu, 王飞 Wang Fei (styled Chongtian), 帅崇兴
  Shuai Chongxing, 朱啸谷 Zhu Xiaogu, 刘俊卿 Liu Junqing, 刘绍奎 Liu Shaokui, 王亢子
  Wang Kangzi (蝉红), 王因子 Wang Yinzi (蝉绿); Japanese: 犬养健 Inukai Ken, 犬养毅
  Inukai Tsuyoshi, 周隆庠 Zhou Longxiang, 有田八郎 Arita Hachirō, 西尾寿造 Nishio
  Toshizō, 佐藤贤了 Satō Kenryō, 矢野征记 Yano Seiki, 清水董三 Shimizu Tōzō, 谷垣专一
  Tanigaki Sen'ichi, 仓冈克行 Kuraoka Katsuyuki, 板垣征四郎 Itagaki Seishirō (alias of
  the existing 坂垣 row; source writes 板垣/坂垣/扳垣); Chinese: 陈调元 Chen Diaoyuan,
  邓龙光 Deng Longguang.
- Organizations (7): 南华日报 the South China Daily News, 西南运输公司 the Southwest
  Transport Company, 特务团 the Special Service Regiment, 中央训练团 the Central
  Training Corps, 政友会 the Seiyūkai, 临时政府 the Provisional Government, 维新政府
  the Reformed Government.
- Terms/ships (2): 北光丸 the Hokkō Maru, 霞飞将军 the Général Joffre.
- Places (10): 望龙门 Wanglongmen, 浮屠关 Futuguan, 愚园路 Yuyuan Road, 杜美路 Route
  Doumer, 极司菲尔路 Jessfield Road, 卡尔登公寓 the Carlton Apartments, 吴淞口 the
  Wusong bar, 黄埔江 the Huangpu River, 麦阳路 Maiyang Road, 基隆 Keelung.
- REUSED (already in glossary): 陈恭澍, 戴笠 (老板/戴先生/戴雨农), 汪精卫/汪兆铭 (汪逆/
  汪某/汪氏), 陈璧君, 龙云, 毛人凤, 毛万里, 王云孙, 何芝园, 郑修元, 刘原深, 胡永荃, 杨英,
  曹师昂, 谭天堑, 王天木, 余乐醒, 王鲁翘, 方炳西, 徐先生, 魏春风, 阮小姐, 影佐祯昭, 近卫文麿,
  平沼骐一郎, 王克敏, 梁鸿志, 张发奎, 曾仲鸣, 周佛海/梅思平/高宗武/董道宁, 陈邦国, 余鉴声,
  张逢义; 军统, 蓝衣社, 梅机关, 五相会议; 珊瑚坝, 虹口, 海防, 干诺道. Books cited (蒋总统秘录,
  戴雨农先生全集, 沪滨三次历险实录) handled by FOOTNOTES, NOT glossary title-rows.

### Digitization glitches (rendered to plain sense; LISTED, none footnoted — mechanical)
Same single-character-substitution classes as ch15/ch16. Representative:
- 渡厚→浓厚 (L9); 有开河内→关于河内 (L9); 颠箥→颠簸 (L23); 雅雀无声→鸦雀无声 (L30);
  毛人见→毛人凤 (L26); 蒋委负长→委员长 (L52); 江说→汪说 + 对江→对汪 (L104); 应孩→应该
  (L73); 近卫望明→近卫声明 (L74) + 民家→民众/民间 (recurring, L74/L76); 影佐帧昭→影佐祯昭
  (recurring); 扳垣征四郎→板垣征四郎 (L86); 徙容就义→从容就义 (L152); 世居河内→(likely)
  蛰居河内 (L53, rendered neutrally "long dwelt at Hanoi"; the letter says 蛰居 twice
  and 久居 once); 廷企→(likely) 延企 (L53, rendered "long-standing eagerness by sense").
- Not glitches: 汪逆 = "the traitor Wang", 汪某 = "the man Wang", 汪氏 = "Wang". XX / xxxx
  (L30) are the source's own REDACTIONS in the air-raid scene, kept as ellipses in sense.

### data/noise.txt — B12 block appended (8 entries, each commented)
十万大山 (Shiwan Mountains, place name), 百梅 (Baimei cover-name), 一九四○ (fullwidth-zero
year 1940, ○=U+25CB), 二○九 (page 209, same U+25CB class as 二○三/二 O 五), 几两重 (tael
idiom), 八郎 (Arita Hachirō's name; cf. the noised 征四郎), 颠三倒四 (topsy-turvy idiom),
千金 ("daughter" honorific). All strip SOURCE approximations/name-embedded/idiom numerals
only; real values (dates, the three-point agreement, page 213, forty-three years, the
nineteen participants) carried in the English as digits/words.

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — ch17 spec added (drop=2; merges [(74,75)]; glued {};
  standalone [3,45,108] = (一),(二),(三)). Backward-compatible.
- `data/noise.txt` — B12 block (see above).
- `glossary.json` — 49 rows added by hand (sectioned; every row has `pinyin`); the
  stray 小巷子 common-noun row was removed after it cross-flagged ch06/07/13/15.

## Batch B13 — ch18 + ch19 (Part Two, Chapter 8 + Author's Note) — COMPLETES PART TWO

第八章 再接再励前仆后继 "Chapter 8. Renewed Effort, Wave upon Wave" (ch18) is the
EIGHTH and LAST chapter of Part Two ("Disgrace at Hanoi"), plus 「英雄无名」作者小启
"A Note from the Author" (ch19), the short authorial notice CLOSING Part Two,
signed 陈恭澍谨启七十二年五月 (May 1983). ch18 takes over the Shanghai District
(12 Aug 1939), tracks Wang Jingwei's Shanghai/Nanjing movements and the 30 Mar
1940 "还都" (return-of-the-capital) farce, then mourns the "wave upon wave" of
patriots who took up the sanction after the Hanoi failure (Wu Gengshu + Dai
Jingyuan, Chen Sancai, Huang Yiguang, Shao Mingxian) and gives an accounting of
all NINETEEN Hanoi participants (dead / whereabouts-unknown / still living). ch19
announces the Part-Three Shanghai volume and invites former 上海区 comrades to
send corrections. **ch18 = 138 body paragraphs; ch19 = 4 body paragraphs. 6 new
notes (208 cumulative); 21 glossary rows added.** All checks green; qa_epub PASS;
epubcheck 0/0/0/0. **EPUB now 19/43 chapters. PART TWO COMPLETE.**

### Structure
- **ch18** drop=2 (running header 英雄无名-陈恭澍 + <h2>). Confirmed p-by-p against
  data/src_epub/OEBPS/Text/index_split_000_0017.xhtml: **1 <h2> + 143 <p>**, no
  <br/>, no <img>, no set-off formatting — zero mismatches.
  - THREE numbered-in-parens sub-headings (一)-(三): (一)总是跟在后头就已失去机先 is
    STANDALONE (its own <p>, L3); (二)痛定思痛字字为汪案牺牲者悼念 (glued to L31 tail)
    and (三)生死荣辱之中也有幸与不幸 (glued to L86 tail) are GLUED and split off (cf.
    ch08/ch16). Rendered "(1)"-"(3)".
  - FOUR mid-phrase splits MERGED (last char a comma or mid-word, next <p> ends
    terminal, no chains): L20/21, L39/40 (mid-word 告|知), L57/58, L134/135
    (mid-word 走|出来). 143 − 1 standalone heading − 4 merges = 138 body.
  - DELIBERATE separate <p> kept whole (NOT merged): the ：-ended enumerated
    lead-ins (L6 还有：, L12 …伪政权：, L113 …下落不明的：, L132 …三个人了：); the martyr
    roster labels (L35 其一：… glued to its own body with a dash; L51 其二：陈三才先烈,
    L62 其三：黄逸光先烈 each its own <p>); the quoted telegram (L70), Kagesa/Liu memoir
    excerpts (L66/67), and (注：…) gloss (L71).
  - NO in-text "(第八章完)" coda (confirmed by grep; cf. ch14/ch15/ch17). The final
    <p> (L145) closes Part Two, forward-referencing Part Three (百战声威) and Part Four.
- **ch19** drop=2 (running header + <h1> notice title; source uses <h1>, not <h2>).
  Confirmed p-by-p: **0 <h2> / 1 <h1> + 4 <p>**, no <br/>, no <img>. NO sub-headings.
  4 body <p>: the 拙着…第三部 announcement, the 三种态度/两点谅解 body, the 来信请寄 line,
  and the 陈恭澍谨启七十二年五月 signature (ends non-terminal 月 but a DELIBERATE separate
  <p>, kept as its own paragraph, NOT merged).
- Source note markers `\[\d+\]`: **none present** in either unit (grepped; none through B13).

### Checks (all green)
- verify_unit ch18: parity 138/138; numbers 0 unresolved; anchors 6 ok.
- verify_unit ch19: parity 4/4; numbers 0 unresolved; anchors 0 ok.
- check_align: ch18 138/138, median ratio **4.98 en/han**; ch19 4/4, **6.45 en/han**.
  Both run high as expected: ch18 is roster/document-heavy (a quoted telegram, the
  Liu Shoufa memoir excerpt, 19 one-paragraph biographical notices); ch19 is a
  4-paragraph formal notice. No pair strays > 2.2x from the median.
- check_structure: ALL PASS (parity + 208 anchors, 0 unresolved).
- check_content: ch18 **219 name occurrences, 0 DISPLACED**; ch19 **3, 0 DISPLACED**
  ("all in the paired paragraph"). Overall nonzero exit is ONLY the KNOWN pre-existing
  artifacts (ch07 Zhanggu ×1, ch08 Shunde ×3, ch13 Miss Nguyen/Oya Kusuo/Yuan Haowen
  ×9 — diacritic/variant substring artifacts, unchanged). 铅山 was NOT glossary-keyed
  (it also occurs in ch04, would cross-flag; rendered "Yanshan" inline).
- qc_entities: 0 misses both units (ch18 census top: 河内 ×36, 汪精卫 ×35, 制裁 ×18,
  吴赓恕 ×14, 曾先生 ×10; ch19: 调查统计局 ×1, 陈恭澍 ×1). All 21 new rows carry pinyin.
- check_register --ref B01_frozen: within tolerance (ch18 contr 0.0/1k, shall 0%,
  em-dash 7.8/1k, sent med 23, rhythm 0.66; ch19 shall 0%, em-dash 7.4/1k, med 30).
- qa_epub PASS (57 files, all links resolve); epubcheck 0 fatals/0 errors/0 warnings.
- TAIL verified against source: ch18's Part-Two close (L145: the "one of three
  survivors" reflection forward-referencing Part Three "百战声威"/Part Four,
  publication set for 七十三年, the 猜单双 fortune "shall not die within two or three
  years"); ch19's 陈恭澍谨启七十二年五月 signature — both faithful, complete, no
  fabrication. The quoted Dai telegram (L70) and Liu Shoufa memoir (L66/67)
  re-verified clause-by-clause (rule 4).

### Notes ledger (6 this batch; 208 cumulative)
New notes (first-appearance-disciplined): 邓演达 Deng Yanda (Third Party leader
executed 1931; the ill-omened house); 还都 the "return of the capital" (Wang's
30 Mar 1940 ceremony proclaiming the National Government's "return" to Nanjing);
荆轲聂政 Jing Ke and Nie Zheng (the archetypal Warring-States assassin-retainers,
from Sima Qian's 刺客列传); 雨花台 Yuhuatai (the Nanjing execution ground where Dai
Jingyuan and Wu Gengshu were shot); 常山 the "烈并常山" inscription (the Yan Gaoqing/
Changshan loyalty allusion, via Wen Tianxiang's Song of Righteousness); 传记文学
Biographical Literature (Zhuanji Wenxue, the Taipei monthly, founded 1962 by Liu
Shaotang, in which the memoir was serialized; note says MORE than the glossary row).
**NOT re-noted** (covered earlier, per the ledger): 制裁 "sanction" (B01/B06); 汪逆/
汪某/汪氏 the traitor Wang forms (B06); 「一二八」 the January 28 Incident (ch05);
梅机关 the Ume Kikan + 影佐祯昭 Kagesa (glossary; text self-glosses); No. 76 极司菲尔路
Jessfield Road (ch17/B12; ch18 spells it 极司非而路, a variant — rendered "Jessfield
Road"); 行状 "record of conduct" (ch15/ch16); 蒋总统秘录/戴雨农先生全集 books (ch15/ch17);
陈邦国/郑邦国 the name trap (footnoted at first ch15 occurrence; Chen re-explains it
in-text at ch18 L118, NOT re-noted). New cast handled by GLOSSARY rows, not notes.

### Glossary rows added (21 by hand; every row carries a `pinyin` field)
- People (18): 陈三才 Chen Sancai, 黄逸光 Huang Yiguang, 戴静园 Dai Jingyuan (原名
  戴星炳 Dai Xingbing), 邵明贤 Shao Mingxian (the four/five new Wang-case martyrs);
  陈群 Chen Qun, 邓演达 Deng Yanda, 钱新民 Qian Xinmin (Nanjing District chief),
  王钟岳 Wang Zhongyue (化名 王乐 Wang Le), 陈石生 Chen Shisheng, 陈耀祖 Chen Yaozu,
  唐骏圻 Tang Junqi (the Kaohsiung correspondent), 王伯群 Wang Boqun, 吴四宾 Wu Sibao
  (source glitch 宾→宝), 周至柔 Zhou Zhirou, 王叔铭 Wang Shuming (ROC air-force
  generals), 刘守法 Liu Shoufa, 刘方雄 Liu Fangxiong, 刘原深 Liu Yuanshen, 韩继文 Han
  Jiwen (尚英), 张亚民 Zhang Yamin.
- Organizations (2): 新一组 New Group One, 传记文学 Biographical Literature (journal).
- Places (1): 雨花台 Yuhuatai.
- REUSED (already in glossary, all with pinyin): 郑修元, 傅筱庵, 张啸林, 吴佩孚,
  王克敏, 王文, 山本荣治, 陈调元, 西尾寿造, 坂垣/板垣征四郎, 影佐祯昭, 梅机关, 晴气庆胤,
  中岛信一, 李士群, 梁鸿志, 今井武夫, 吴赓恕, 邓文仪, 梅思平, 谭天堑, 岑家焯, 余乐醒,
  余鉴声, 徐先生, 魏春风, 阮小姐, 唐英杰, 张逢义, 陈邦国, 陈步云, 曹师昂, 曾先生, 愚园路,
  临时政府, 维新政府, 华北政务委员会, 曾仲鸣, 上海区/南京区 (rendered inline). 铅山 NOT
  keyed (occurs in ch04 too; "Yanshan" inline). Books cited handled by note, not glossary.

### Digitization glitches (rendered to plain sense; LISTED, none footnoted — mechanical)
Same single-character-substitution classes as ch15/ch16/ch17. ch18:
- 不合沬→不合法 "unlawful" (L10, 沬→法); 困为→因为 "because" (L20, L139, 困→因);
  吴四宾→吴四宝 Wu Sibao (L17, 宾→宝); 说讪→(idle chatter) (L17, rendered by sense);
  情报资科→情报资料 (L26, 科→料); 行综→行踪 "movements" (L27, 综→踪); 悟山来→悟出来
  "come to realize" (L99, 山→出); 首光→首先 "first" (L129, 光→先); 上刚文→上文 (L131,
  刚 extraneous); 师局兄→师昂兄 Cao Shi'ang (L132, 局→昂); 这么仿→这么做 (L80, 仿→做);
  爱国志土→志士 "patriots" (L81, 土→士); 杳询→查询 (L125, 杳→查).
- 烈并常山: the 挽额 inscription; 烈 read as "valor/heroism"; rendered "A Valor to Rank
  with Changshan" and the Changshan/Yan Gaoqing allusion FOOTNOTED (reading uncertainty
  + allusion, not a mechanical typo).
- ch19: 疎失 = 疏失 (variant, not a typo). No significant glitches.

### data/noise.txt — B13 block appended (5 entries, each commented)
三才 (Chen Sancai's given name, glyph 三; cf. noised 毛万里/征四郎), 成千 (thousands
idiom), 千难 (千难万难 idiom — noised as 千难 because an earlier 万难 rule pre-strips
the 万难 half, else the 千 orphans as 1000), 再而三 (一而再再而三 idiom), 两手 (有两手
"some real skill" idiom). All strip SOURCE name-embedded/idiom numerals only; real
values (dates, 165 cm, 19 participants, ten thousand li idiom carried as "ten thousand
li", counts) carried in the English as digits/words.

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — ch18 spec (drop=2; merges [(20,21),(39,40),(57,58),
  (134,135)]; glued {31:(二)…, 86:(三)…}; standalone [3]) and ch19 spec (drop=2; no
  merges/glued/standalone) added. Backward-compatible.
- `data/noise.txt` — B13 block (see above).
- `glossary.json` — 21 rows added by hand (sectioned; every row has `pinyin`).

## Batch B14 — ch20 (Part Three OPENS: "Renown Won in a Hundred Battles") — self-preface

「上海抗日敌后行动」自序 "Author's Preface: Shanghai Behind-the-Lines Operations
Against Japan" (ch20) is the SELF-PREFACE that **opens Part Three**, whose part
title is 「百战声威」 "Renown Won in a Hundred Battles". Chen recounts the Part-Three
title's evolution (百战声威 → 抗战期间上海敌后行动 → 上海敌后行动 → the final 上海抗日
敌后行动), sets the scope at 二十八年八月至三十年十月 (Aug 1939 – Oct 1941, the span
the ch19 notice announced), then gives a compressed portrait of the Shanghai
District: its unprecedented ~1,000-strong size, its full internal/external
order of battle (duplex HQ; 22 courier-liaison stations; 3 standing wireless
stations + 1 reserve; Chief/District Accountants; technical room + "warehouse";
New Group One; five intelligence groups; eight action brigades; the "soft"-work
units), the tally of two years' work (200+ own casualties; 100+ traitors
sanctioned; 50+ sabotage instances; ~40 Japanese officers killed), the enemy's
Nov-1941 full-page press exposé, and — in a preview of ch21 — his Aug-1939
arrival, appointment as District Chief, and the crisis left by Chen Dirong's
betrayal. **26 body paragraphs. 2 new notes (210 cumulative); 2 glossary rows
added.** All checks green; qa_epub PASS; epubcheck 0/0/0/0. **EPUB now 20/43
chapters. PART THREE OPENS.** (Next: B15 = ch21, the first Shanghai chapter.)

### Structure
- **ch20** drop=3 (cf. ch10, the Part-Two preface): running header 英雄无名-陈恭澍 +
  <h1>「百战声威」 (the Part-Three banner, rendered from book.json's `part` field) +
  <h3>「上海抗日敌后行动」自序 (the preface's own title, re-emitted from book.json
  `title_en`). Confirmed p-by-p against data/src_epub/OEBPS/Text/index_split_000_0019.xhtml:
  **1 <h1> + 1 <h3> + 26 <p>**, no <h2>, no <br/>, no <img>, no set-off formatting —
  zero mismatches.
  - The title 「上海抗日敌后行动」自序 is **heading markup (`<h3>`), NOT a `<p>`** — the
    kickoff's structure note had guessed it a `<p>` and proposed drop=2 + standalone;
    inspecting the raw XHTML showed the `<h3>`, so it drops with the header/banner
    (drop=3), exactly parallel to how ch10 dropped its `<h2>` preface title. The
    reading.md `##` comes from book.json title_en; keeping the title as a body line
    would have duplicated it.
  - The 26 body `<p>` (L4–L29) map **1:1** to the 26 source `<p>` — **NO extractor
    mid-phrase splits, no merges, no glued, no standalone**. The lone non-terminal
    line (L12, "…大致有如下者–", ending on a dash lead-in) is its own source `<p>`
    introducing the region-structure list; DELIBERATE separate `<p>`, NOT a split,
    NOT merged (cf. the ；/：-ended lead-ins in ch16/ch17/ch18).
  - NO (一)-style paren sub-headings (grepped; none). NO in-text "(…完)" coda (grepped).
- Source note markers `\[\d+\]`: **none present** (grepped; none through B14).

### Checks (all green)
- verify_unit ch20: parity 26/26; numbers 0 unresolved; anchors 2 ok.
- check_align: ch20 26/26, median ratio **5.31 en/han** — dense as expected for a
  preface (the B01 prefaces + ch10 are the models; HANDOFF notes prefaces run ~5.2).
  No pair strays > 2.2x from the median.
- check_structure: ALL PASS (parity 26/26 + 210 anchors, 0 unresolved).
- check_content: ch20 **8 name occurrences, 0 DISPLACED** ("all in the paired
  paragraph"). Overall nonzero exit is ONLY the KNOWN pre-existing artifacts (ch07
  Zhanggu ×1, ch08 Shunde ×3, ch13 Miss Nguyen/Oya Kusuo/Yuan Haowen ×9 — unchanged).
- qc_entities: 0 misses (census top: 军统 ×4, 河内 ×2, 重庆 ×2, 陈第容 ×2, 调查统计局,
  北平, 天津, 督察, 新一组, 黄志远, 蓝衣社, 制裁). Both new rows carry pinyin. (One
  transient miss caught + fixed: 督察 rendered "supervisor" → corrected to the
  glossary-decided "inspector".)
- check_register --ref B01_frozen: within tolerance (contr 0.0/1k, shall 0%,
  em-dash 9.2/1k, sent med 35, rhythm 0.61 vs ref 0.60). A preface with no dialogue
  and no narrating "shall" — as expected; not de-formalized.
- qa_epub PASS (57 files, 210 references/bodies/backlinks, all links resolve);
  epubcheck 0 fatals / 0 errors / 0 warnings / 0 infos.
- TAIL verified against source: P26/L29 (「上海区」建立已久…重振雄威，还敌冠以颜色！) —
  faithful, complete. The two longest paragraphs (P16/L19 the task-list close;
  P17/L20 the statistics + press-exposé) re-verified clause-by-clause (rule 4);
  the number check confirms every real quantity survived.

### Notes ledger (2 this batch; 210 cumulative)
New notes (first-appearance-disciplined): 阎王殿上的勾魂簿 the King of Hell (Yama) and
the "soul-summoning register" (勾魂簿) — the undestroyable accountant's vouchers as a
death-register (culture/belief; unnoted before — the prior "underworld" notes are
Sandianhui/Yan Xishan/Du Yuesheng, not Yama); 新申报 / 中华日报 the two occupation-era
Shanghai papers that printed the enemy's full-page exposé (institution; the
Zhonghua Ribao founded 1932 as Wang Jingwei's clique organ). **NOT re-noted**
(covered earlier, per the ledger): 卷头长白 "Prefatory Candour" (rendered, front
matter); 北国锄奸 / 河内汪案始末 / 百战声威 the part titles (settled); 军事委员会调查
统计局 / 军统 the Juntong (B01/glossary); 上海区 "the Shanghai District" (inline);
蓝衣社 the Blue Shirt Society (NOTED ch08 — reused, not re-noted); the Republican-
calendar convention (front matter — years rendered literally). New personnel handled
by GLOSSARY rows, not notes.

### Glossary rows added (2 by hand; every row carries a `pinyin` field)
- People (2): 陈第容 Chen Dirong (assistant secretary whose leak triggered the search
  of 14 offices), 黄志远 Huang Zhiyuan (the old comrade who preserved the newspaper
  sheets). Both `provisional` (romanization mine).
- REUSED (already in glossary, with pinyin): 郑修元 Zheng Xiuyuan (District secretary),
  蓝衣社 the Blue Shirt Society, 督察 "inspector", 新一组 New Group One, 制裁 "sanction".
- **赵君** (the acting District Chief): rendered "a Mr. Zhao" in-text and **NOT
  glossary-keyed** — 君 is likely honorific (surname only; full given name not given
  here), and he recurs in ch21; keying a bare surname risks a cross-chapter conflict
  (cf. the B12/B13 glossary-key discipline). Firm up in B15 when ch21 names him.

### Digitization glitches (rendered to plain sense; LISTED, none footnoted — mechanical)
Same single-character-substitution / homophone classes as ch15–ch18. ch20:
- 随528；科技进步 → 随着科技进步 "with the advance of science and technology" (L19/P16;
  528 + a stray ； are garbage where 着 belongs — the only ASCII glitch in the unit;
  528 NOISED, plain sense carried).
- 真刀买枪 → 真刀真枪 "real blades and real guns" (L20/P17, 买→真).
- 反问 → 反间 "counter-espionage" (L17/P14, 问→间; L19/P16 prints 反间 correctly).
- 曾经捉到过 → 曾经提到过 "was once mentioned" (L7/P4, 捉→提).
- 助理处记 → 助理书记 "the assistant secretary" (L13/P10, 处→书; parallels 区本部书记 /
  the later 助理书记 陈第容).
- 敌为宪兵 → 敌伪宪兵 "the enemy-and-puppet gendarmes" (L28/P25, 为→伪; the pervasive
  敌伪 compound — Japanese Kempeitai + puppet gendarmerie).
- 全部五十余单位 另有 (L27/P24): a dropped full stop (a space where the sentence breaks);
  rendered as a sentence boundary.
- 还敌冠以颜色 (L29/P26): a slightly garbled idiom for 给以颜色/以颜色看 "give [them] a
  taste / show [them] our colors"; rendered "give the enemy back some color to reckon with".
None is genuine reading uncertainty, so none is footnoted (per policy).

### data/noise.txt — B14 block appended (3 entries, each commented)
百数十 (百数十个外勤单位 "over a hundred [field units]", an estimate; checker reads the
百 as 100), 十余 (十余人 "a dozen-odd", ten-plus estimate; guarded so it never fires
inside 二十余 etc.), 528 (the 随着 glitch above). All strip SOURCE approximate/glitch
numerals only; every real value (200+, 100+, 50+, ~40, 22, 4, 3, 1, 14, "about a
thousand", the 28th-year/30th-year dates, Nov 28) is carried in the English as
digits/words and matched by the checker.

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — ch20 spec (drop=3; no merges/glued/standalone) added.
  Backward-compatible; source-conservation check passes (26 body paragraphs).
- `data/noise.txt` — B14 block (see above).
- `glossary.json` — 2 rows added by hand (sectioned; every row has `pinyin`).

## Batch B15 — ch21 (Part Three, Chapter 1: "Renown Won in a Hundred Battles")

**Unit:** ch21 = 第一章 十里洋场重振雄威 "Chapter 1. Back in Shanghai, Our Might Restored."
The FIRST Shanghai chapter and the longest so far in Part Three (~21,426 source chars).
Chen arrives in fallen Shanghai (early Aug 1939), is appointed District Chief by Dai Li's
telegram (takes over 12 Aug 1939), and rebuilds the shattered Shanghai District: the
14-office search that followed Chen Dirong's betrayal, Zheng Xiuyuan holding the District
together single-handed (three excerpts from his memoir "沪滨三次历险实录"), the duplex
command center, and a full order-of-battle roll of the inner staff, five intelligence
groups, eight action brigades, New Group One, and the Kang Corps. Ends on the magazine
serialization coda "(第一章完下期续载)" with seven further paragraphs after it.

### Structure (confirmed p-by-p against the source XHTML)
- `index_split_000_0020.xhtml` parses to **1 `<h2>` + 162 `<p>`**, NO `<h1>`, NO `<br/>`,
  NO `<img>`. drop=2 (running header 英雄无名-陈恭澍 + `<h2>` chapter title). The 162 txt
  body lines map 1:1 to the 162 `<p>` — zero mismatches.
- **THREE mid-phrase merges** where a source `<p>` boundary severs one sentence (first ends
  non-terminal): L56/57 (…是办理制裁 | 汪精卫的项目。 — an enumerated 一、 item split at
  制裁|汪精卫), L93/94 (…这或者 | 就是戴先生…的理由了吧。), L107/108 (…也要提供不少 |
  条件再加上一番经营才成。). No chains.
- **FOUR couplet-style sub-headings** (NO number prefix, cf. ch11/ch14), each its own plain
  `<p>` (standalone): L3 死无对证永成悬疑的一桩大反间, L37 危机四伏中稳扎稳打渡过难关,
  L82 我们的敌后工作指挥中心别具一格, L112 无形火线上无所不在的战斗行动者剪影.
- The ：/-ended lead-ins, the 一、-八、 and 1-4 enumerated items, the roster lines, and the
  『』-closed dialogue lines are DELIBERATE separate `<p>` (NOT merged). L86 (…如何应用了)
  ends on 了 with the source's 。 dropped — a DELIBERATE paragraph break (new topic
  follows), NOT a split; rendered as its own paragraph.
- **Serialization coda:** "(第一章完下期续载)" is glued to the tail of L157/P147 (the Sun
  Dacheng one-armed-hero paragraph), with SEVEN further `<p>` (P148-P154) after it — a
  magazine-installment seam faithfully reproduced (cf. the "(第N章完)" coda in
  ch12/ch13/ch16, here with 下期续载 + trailing content). Rendered "(End of Chapter One; to
  be continued in the next issue.)" and preserved as body text.
- **No source note markers:** grep `\[\d+\]` → none present (consistent through B14).
- **No images** in the unit (confirmed).
- clean_batch.py: `ch21: 155 body paragraphs, 4 sub-headings, source conserved OK`.

### Checks (all green for ch21; pre-existing artifacts unchanged except one FIXED)
- `verify_unit.py ch21`: parity **155/155**, numbers **0 unresolved**, anchors 0 ok (then 8).
- `check_align.py ch21`: 155/155, **median ratio 4.89 en/han**, no pair strays > 2.2x. Above
  the 4.55–4.78 narrative band, as expected: the chapter is document-heavy (three long
  Zheng-Xiuyuan memoir excerpts, an embedded Liu-Shaokui memoir quote, and several
  enumerated explanatory lists lift the ratio; read the note, do not reset).
- `check_structure.py`: ALL STRUCTURAL CHECKS PASS; anchors 218 notes, 0 unresolved.
- `check_content.py`: **ch21 157 name occurrences, all in the paired paragraph (0 displaced).**
  Known pre-existing artifacts remain ch08 Shunde ×3, ch13 Miss Nguyen/Oya Kusuo/Yuan
  Haowen ×9. **ch07 Zhanggu ×1 is now GONE** — see the glossary-key fix below.
- `qc_entities.py` (reconstructed bilingual, 155 pairs): **entity misses: 0.** 督察 ×13
  aligns to the glossary-decided "inspector" (the B14 near-miss avoided).
- `check_register.py --ref`: **within tolerance.** shall 33% (Chen's deliberate essayistic
  narration, cf. B06 33% / B12 43%; verified narration not dialogue — do NOT de-formalize),
  contractions 0.0, em-dash 7.1/1k (ref 8.3), rhythm CV 0.61 (ref 0.60).
- Tail verified against the source (rule 4 corollary), P144–P154 incl. the coda seam.
- Build: `21 of 43 chapters, 218 notes`. `qa_epub.py` PASS (218 refs/bodies/backlinks).
  **epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings / 0 infos.**

### Glossary-key fix — 掌故 / "Zhanggu" (a DISCIPLINE violation, now removed)
The organizations key **掌故 → "Zhanggu"** (a Hong Kong history magazine, cited once in
ch12 P108 as "the 'Zhanggu' magazine published at Hong Kong") violated glossary-key
discipline: 掌故 is ALSO the common noun "old lore / anecdote," which is how ch07 P24
("old hometown lore") and ch21 P59 ("looked on as old lore") use it. A key must render
ONE way everywhere and be a distinctive proper noun; periodicals are handled by
FOOTNOTE/inline, not keyed. **Removed the key.** Effects: the ch12 magazine reference is
self-glossed inline (unchanged); **ch07's known Zhanggu artifact is now resolved** (206
occ., all in paired); ch21 P59 is clean. Net: one fewer known content-check artifact.

### Glossary rows added BY HAND (19; sectioned file; every row has `pinyin`)
People (mostly `provisional`, romanization mine): 万里浪 Wan Lilang (4th-Brigade traitor →
No.76 First Section chief), 刘时雍 Liu Shiyong (4th-Brigade leader), 蒋安华 Jiang Anhua
(3rd Brigade, the mainstay), 吉震苍 Ji Zhencang (2nd Brigade, cover Zhao Sheng, the
Du-Yuesheng-tied brigade), 毕高奎 Bi Gaokui (New Group One; also 毕镐奎), 孙大成 Sun
Dacheng (Kang-Corps leader, a cover name; lost an arm at the Bund Park), 刘健 Liu Jian
(2nd Intel Group), 萧杰英 Xiao Jieying (inner-courier-station head), 萧张权 Xiao Zhangquan
(8th Brigade, martyred at Suzhou), 张璜 Zhang Huang (accountant), 杨震裔 Yang Zhenyi
(chief wireless inspector), 陈明楚 Chen Mingchu (cover name of Chen Dirong), 王世英 Wang
Shiying (compiler-reviewer), 潘绍岳 Pan Shaoyue (6th Brigade). `attested`: 戴藏宜 Dai
Cangyi (Dai Li's son), 翁光辉 Weng Guanghui (1st Shanghai District chief), 吴乃宪 Wu
Naixian (2nd chief, styled Jinfu), 杜月笙 Du Yuesheng (Green Gang boss; already NOTED at
ch17 — do NOT re-note). Organizations: 忠义救国军 "the Loyal and Patriotic Army."
REUSED (already keyed, consistent): 郑修元 Zheng Xiuyuan, 陈第容 Chen Dirong, 黄志远 Huang
Zhiyuan, 赵理君 Zhao Lijun, 毛万里 Mao Wanli, 王天木 Wang Tianmu, 王鲁翘 Wang Luqiao, 刘原深
Liu Yuanshen, 王亢子/王因子 the Wang daughters, 胡永荃 Hu Yongquan, 朱啸谷 Zhu Xiaogu,
白绳祖 Bai Shengzu, 刘俊卿/刘绍奎 the two Lius, 周伟龙 Zhou Weilong.

**赵君 RESOLVED:** the acting District Chief called "a Mr. Zhao" in the ch20 preview is
named in full here — **赵理君 Zhao Lijun** (already glossary-keyed, `attested`). Rendered
"Zhao Lijun" throughout ch21; his cover name **凌秋云 "Ling Qiuyun"** appears in the memoir.

### Notes added (8; first-appearance-disciplined; cumulative 218)
1. **忠义救国军** "Loyal and Patriotic Army" (Dai Li's guerrilla/irregular force; Shanghai
   office as District cover). 2. **秦晋之说** the Qin-Jin marriage allusion (结为秦晋).
3. **越界筑路** extra-settlement roads (the disputed-jurisdiction gray zone at the concession
   edges). 4. **亭子间** the Shanghai lane-house back-room. 5. **白相人** Shanghai-dialect
   idler/petty tough. 6. **法币** the fabi national currency + the 38-yuan courier wage.
7. **唐生智** Tang Shengzhi (Hunanese general, anti-Chiang risings; later Nanjing 1937).
8. **邓演达事件 / 两广事件** the Deng Yanda execution (1931) + the Two Guangs revolt (1936).
**NOT re-noted (already covered):** the French Concession / International Settlement (ch04),
Du Yuesheng / the Green Gang (ch04/ch17), the Blue Shirt Society (ch08), the Juntong (org),
制裁 "sanction" (term), the Xi'an Incident (ch06), the Kōain (ch12), No.76 / 特工总部 /
Li Shiqun / Ding Mocun (ch04/ch17), the 抗日杀奸团 / Kang Corps (ch02/ch11), the Republican
calendar convention, 十里洋场 (chapter-title epithet).

### Digitization glitches (rendered to plain sense; LISTED, none footnoted — mechanical)
Same single-character-substitution / homophone / dropped-punctuation classes as ch15–ch20:
- 极感僧恨 → 极感憎恨 "the bitterest loathing" (P4, 僧→憎).
- 这不是说我根木头 → …我是块木头 "not that I am a blockhead" (P28, garbled 是块; a dropped/
  substituted character, plain sense carried).
- 高级干中 → 高级干部中 "among the senior cadres" (P24, dropped 部).
- 享高寿八十余 第三任 (P34): a dropped full stop (space where the sentence breaks between
  "…over eighty." and "The third chief…"); rendered as a sentence boundary.
- 更谈不到如何应用了[／]建立新的… (P79→P80): a dropped full stop after 了; rendered as a
  paragraph boundary (the two source `<p>` are distinct thoughts, NOT a mid-phrase split).
- 重新建立工作指挥中心是为了隐扎隐打 → …稳扎稳打 "fighting steadily from firm ground"
  (P81, 隐→稳; the same 稳扎稳打 the sub-heading L37 uses correctly).
- 接二连二 → 接二连三 "one after another" (P15, the idiom's second 三 mis-scanned as 二;
  NOISED as 接二连二, plain sense carried).
None is genuine reading uncertainty, so none is footnoted (per policy).

### data/noise.txt — B15 block appended (each entry commented)
Elided-tens/approximate & idiom/name numerals stripped (SOURCE numerals only; every real
value carried in the English and matched by the checker): **三、五十** (thirty-to-fifty,
in the elided block, longest-first), **七一四** (the "714" July-14th event-name, cf. 九一八/
一二八), **接二连二** (the mis-scanned idiom), **四出** (侦骑四出 "out on all sides"),
**凋零** (制作者早已凋零, 零=0 idiom), **百利而无一损** ("all gain and no loss," 百/一 rhetorical),
**万般** (万般出于无奈 idiom), and the coy name-numeral 万-glyph refs of Wan Lilang: **万里浪**,
**万某**, **万即**, and bare **万里 / 万兄** (Mao Wanli named without 毛/兄 — placed AFTER the
longer 毛万里 / 万里兄 / 万里浪 rules so those strip first). Real quantities CARRIED (checker
matched): 两点四十分 "forty minutes past two", 两点五十分 "fifty minutes past two", 二人 "two
men", 平津两地 "both Beiping and Tianjin", the 28th/29th/30th/26th/21st-year dates, No.277 /
No.71 / No.24, 3,000 yuan, 38 yuan, fourteen offices, twenty-two courier units, eight
brigades, "about a thousand," etc.

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — ch21 spec added (drop=2; 3 merges; 4 standalone sub-headings;
  no glued). Backward-compatible; source-conservation check passes (155 body paragraphs).
- `data/noise.txt` — B15 block (see above); 三、五十 slotted into the elided-tens block.
- `glossary.json` — 19 rows added by hand; the 掌故→"Zhanggu" common-noun key REMOVED.
- `notes.json` — 8 notes appended via apparatus_merge.py (numeric character references).

## Batch B16 — ch22 (Part Three, Chapter 2: "Renown Won in a Hundred Battles")

**Unit:** ch22 = 第二章 春云乍展风雷初动 "Chapter 2. Spring Clouds Unfurl, the First
Thunder Stirs." The SECOND Shanghai chapter and the LONGEST unit yet (~35,471 source
chars, half again as long as ch21). The Shanghai District's first sanction operations of
1940 get under way: (1) the deterrent sanction of the French police chief inspector Cheng
Haitao (18 Oct 1939), after Dai Li's stinging "timid as a mouse" telegram; (2) fresh
internal trouble (the DDS Café near-kidnapping from Zheng Xiuyuan's memoir; the legendary
turncoat Wan Lilang walking into No.76; the mysterious official "Secretary Geng" Geng
Jiaji); (3) personnel and funds (Wang Yixin removed; Chen's childhood friends Qi Qingbin
and Zhang Zuoxing installed as secretary and radio inspector; Dai's refusal of Hu
Yongquan's bank offer); (4) the reunion with the "international spy" Fan Xing / Fan Jiman
and the New Group One order of battle and work lines; (5) a long essay on the Juntong's
manner, iron discipline, power of life and death, and moral conscience, closing with the
Christmas 1939 Weldon Dance Hall sanction of Chen Dirong and He Xingjian, the Wang Tianmu
riddle, and the new plan to strike armed Japanese. Ends on the serialization coda
"(第三章完，下期续载)".

### Structure (confirmed p-by-p against the source XHTML)
- `index_split_000_0021.xhtml` parses to **1 `<h2>` + 292 `<p>`**, NO `<h1>`, NO `<br/>`,
  NO `<img>`. drop=2 (running header 英雄无名-陈恭澍 + `<h2>` chapter title).
- **THREE mid-phrase merges** where a source `<p>` boundary severs one sentence (first ends
  non-terminal; no chains): L31/32 (…有关人士 | 有以指教。), L221/222 (…笔者敢于如此肯 |
  定，是体验… ; 肯定 split), L279/280 (…立即避 | 入了女用洗手间，得脱此难。; 避入 split).
- **THREE standalone couplet sub-headings** (NO number prefix, cf. ch11/ch14/ch21): L3
  一警百清除障碍以展示威力, L40 一波未平一波又起内部又出祸害, L64 人事经费时常困扰着陷区单位.
- **TWO glued sub-headings** fused onto a paragraph tail: L108 (…反而不去动脑筋了。 +
  异地重逢又展开一场曲境探幽), L202 (…分出来另做记述。 + 从铁的纪律生杀权限说到道德观念,
  which L203-L204 then enumerate as 作风风气/铁的纪律/生杀权限/道德观念).
- L215 (…谈谈我们的纪律) and L250 (…要多杀几个发动侵略战争的日本人) each end with a dropped
  full stop; both are short prose paragraphs (new topic follows), NOT headings and NOT
  splits. The ：/─-ended lead-ins, the 一、-三、 / 1- enumerated items (rendered as ordinary
  paragraphs, per parity), the roster lines (L183-185), and the 「」/『』 dialogue lines are
  DELIBERATE separate `<p>` (NOT merged).
- **No source note markers:** grep `\[\d+\]` returns none (consistent through B15).
- **No images** in the unit (confirmed).
- clean_batch.py: `ch22: 286 body paragraphs, 5 sub-headings, source conserved OK`.

### Checks (all green for ch22; pre-existing artifacts unchanged)
- `verify_unit.py ch22`: parity **286/286**, numbers **0 unresolved** (auto noise), anchors ok.
- `check_align.py ch22`: 286/286, **median ratio 4.70 en/han**, no pair strays > 2.2x
  (document-heavy chapter; within the expected band).
- `check_structure.py`: ALL STRUCTURAL CHECKS PASS; anchors **225 notes, 0 unresolved**;
  headings level positions OK.
- `check_content.py`: **ch22 201 name occurrences, all in the paired paragraph (0 displaced).**
  Four initial displacements were all glossary-key alignment (rendering the keyed form):
  杜美路 "Route Doumer" (was "Doumer Road"), 羊皮巷 "Yangpi Lane" (was "Sheepskin Lane"),
  连谋 "Lian Mou" (was "Lianmou"), 鸡泽县 "Jize County" (glossary en capitalized to match).
  Known pre-existing artifacts unchanged: ch08 Shunde ×3, ch13 Miss Nguyen/Oya Kusuo/Yuan
  Haowen ×9.
- `qc_entities.py` (reconstructed bilingual, 286 pairs): **entity misses: 0.** 督察 aligns to
  glossary "inspector"; census tops 制裁 ×40, 万里浪 ×25, 王天木/马河图 ×22.
- `check_register.py --ref`: **within tolerance.** shall 36% (Chen's deliberate essayistic
  narration, cf. ch21 33% / B12 43%; verified narration not dialogue, do NOT de-formalize),
  contractions 0.3, em-dash 7.8/1k (ref 8.3), rhythm CV 0.64 (ref 0.60).
- Tail verified against the source (rule 4 corollary; critical on a 35k single-pass unit):
  the plan points L282-284, the Jiang-Anhua/Bi-Gaokui exchange L285, and the coda L286.
- Build: `22 of 43 chapters, 225 notes`. `qa_epub.py` PASS (225 refs/bodies/backlinks).
  **epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings / 0 infos.**

### Glossary rows added BY HAND (29; sectioned file; every row has `pinyin`)
People. `provisional` (romanization mine): 程海涛 Cheng Haitao, 耿嘉基 Geng Jiaji (courtesy
Jizhi, "Secretary Geng"), 王一新 Wang Yixin, 马河图 Ma Hetu, 岳清江 Yue Qingjiang, 丁寳龄
Ding Baoling, 何行健 He Xingjian (+ alias 何天风 He Tianfeng), 汪秋芳 Wang Qiufang (+ cover
汪芳 Wang Fang), 田淑君 Tian Shujun, 傅胜蓝 Fu Shenglan, 丁文蕙 Ding Wenhui, 俞叶封 Yu
Yefeng, 傅炳宸 Fu Bingchen, 邵飘萍 Shao Piaowei (action man; namesake of the journalist),
张圣才 Zhang Shengcai, 陈默 Chen Mo, 赵刚义 Zhao Gangyi, 钱人龙 Qian Renlong, 伊凡诺夫 Ivanov,
范纪曼 Fan Jiman (alias of Fan Xing). `attested`: 虞洽卿 Yu Qiaqing, 贺耀组 He Yaozu
(figurehead Bureau director), 褚民谊 Chu Minyi, 万墨林 Wan Molin, 傅式说 Fu Shishuo (source
misprints 傅 as 传), 顾兰君 Gu Lanjun (film star), 杨虎 Yang Hu.
REUSED (already keyed, consistent): 范行 Fan Xing, 王天木 Wang Tianmu, 齐庆斌 Qi Qingbin,
张作兴 Zhang Zuoxing, 胡永荃 Hu Yongquan, 陈第容/陈明楚 Chen Dirong/Chen Mingchu, 郑介民
Zheng Jiemin, 陈三才 Chen Sancai, 彭雅萝 Peng Yaluo, 毕高奎/黄志远/朱啸谷/刘原深/蒋安华/吉震苍/
刘时雍/万里浪 (the B15 order-of-battle), 张啸林/周佛海/丁默邨/李士群/杜月笙/戴笠/汪精卫.
GLOSSARY-KEY DISCIPLINE upheld: no common-noun or book-title keys; periodicals (新申报) and
books (沪上往事) go to notes/inline, not the glossary.

### Notes added (7; first-appearance-disciplined; cumulative 225)
1. **条子 / gold bars** (Shanghai reckoned large sums in gold ingots; ten bars for a phone
   number; the same currency as the "key money" for a flat). 2. **GPU** (the Soviet secret
   police; byword for ruthless clandestine training; cf. the ch06 Cheka note). 3. **邵飘萍**
   the journalist (1886-1926, shot by Zhang Zuolin; the action man of the same name is a
   different person, as the source flags). 4. **匈奴未灭，何以家为** (Huo Qubing's vow;
   justifies the Juntong marriage ban). 5. **为山九仞，功亏一篑** (Book of Documents allusion
   in Dai's telegram). 6. **万墨林 / 沪上往事** (Du Yuesheng's manager and his memoir, quoted
   on Yu Yefeng). 7. **the Badlands (歹土)** the western-Shanghai extra-settlement no-man's
   land of casinos and puppet gunmen.
**NOT re-noted (already covered):** the French Concession / International Settlement (ch04),
Du Yuesheng / the Green Gang (ch04/ch17), the Blue Shirt Society + Renaissance Society /
Lixingshe (ch05/ch08), the Juntong (org), 制裁 "sanction" (term), No.76 / 特工总部 /
Li Shiqun / Ding Mocun (ch04/ch17), the 抗日杀奸团 / Kang Corps (ch02/ch11), 忠义救国军
(ch21), 越界筑路 (ch21), 法币 (ch21), 亭子间 / 白相人 (ch21), the East Hebei Autonomous
Government (ch09), the Cheka (ch06), Whampoa (ch05), the Republican calendar convention.

### Digitization glitches (rendered to plain sense; LISTED, none footnoted — mechanical)
- **STRAY 杀 title glitch:** the `<h2>` reads 第二章 春云乍展风雷初动**杀**; the 杀 is fused
  onto the couplet title (properly 春云乍展／风雷初动). Dropped in clean_batch.py; book.json
  title_en is already clean and is used for the visible heading.
- **Coda 第三章完:** the serialization coda reads "(第三章完，下期续载)" where ch21's correct
  coda read 第一章完 for the book's Ch1; this is book Ch2, so the 三 is a 三-for-二 glitch.
  Rendered to plain sense "(End of Chapter Two, to be continued in the next issue.)"; the
  第三章完 numeral is NOISED so the check does not demand a match.
- 传式说 → 傅式说 "Fu Shishuo" (传→傅; the correct 傅 appears at 傅某 nearby).
- 天王木 → 王天木 "Wang Tianmu" (character transposition, L257).
- 化石陈明楚 → 化名陈明楚 "cover name Chen Mingchu" (石→名, L266).
- 工共租界 → 公共租界 "International Settlement" (工→公, L273).
- 众失之的 → 众矢之的 "the target of all the arrows" (失→矢, L285).
- 愚原路 → 愚园路 "Yuyuan Road" (原→园, L268).
- 万先失 → 万先生 "Mr. Wan" (失→生, L225; NOISED as 万先失).
- 予以制的命令 → 予以制裁的命令 "an order to sanction" (dropped 裁, L225).
- 上级随即下拿下令 → 随即下令 "at once sent down an order" (dittography 拿下, L221).
- 此来番沪 → 返沪 "on this trip to Shanghai" (番→返, L196); 外文部长 → 外交部长 "minister of
  foreign affairs" (文→交, L196).
- 贪赎重罪 → 贪渎 "the grave charge of corruption" (赎→渎, L48).
- **Source name inconsistency (NOT a glitch of ours; preserved faithfully):** the innocent
  bystander is 刘恒 at L266, 刘桓 then 刘恒 at L272. Rendered "Liu Heng" / "Liu Huan (on
  inquiry)" / "Mr. Liu Heng" exactly as the source varies.
None is genuine reading uncertainty, so none is footnoted (per policy).

### data/noise.txt — B16 block appended (each entry commented)
Idiom/name/glitch numerals stripped (SOURCE numerals only; every real value carried in the
English and matched): **万想不到** (10000 idiom), **万千** (myriad), the bare-surname Wan
forms **万有何 / 万队 / 万答 / 万逆 / 万与** (Wan Lilang named by 万 alone), **万墨林** and
**万先失** (Wan Molin), **外八字** (splay-footed, 八), **合十** (palms-together, 十),
**不三不四** (disreputable, 3/4), **两个钱** (a bit of money, 两), **八旬** (in one's eighties;
the checker cannot read 旬), and the coda glitch **第三章完** (三-for-二). Real quantities
CARRIED (checker matched): 五点四十分 "five-forty", 十二点 "twelve"/"midnight", 两百/一百
"two hundred"/"one hundred", 二人/二兄/三人/三位 rendered "the two"/"both"/"the three",
京沪/平津两地 "both …", 三时三十分 "half past three, three-thirty", 两个礼拜 "two weeks",
三千元 3,000 yuan, 五十万圆 five hundred thousand yuan, the 28th/29th/30th/32nd-year dates,
八年前 eight years, and the Oct-18 / Dec-8 / Dec-25 / Jan-14 / Feb-26 operation dates.

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — ch22 spec added (drop=2; 3 merges; 3 standalone + 2 glued
  sub-headings; the clean couplet title, 杀 dropped). Source-conservation check passes.
- `data/noise.txt` — B16 block (see above).
- `glossary.json` — 29 rows added by hand (all with `pinyin`); 鸡泽县 en capitalized to
  "Jize County" (place, ch22-only, safe).
- `notes.json` — 7 notes appended via apparatus_merge.py (numeric character references).

## Batch B17 — ch23 (Part Three, Chapter 3: "Renown Won in a Hundred Battles")

**Unit:** ch23 = 第三章 爱国情操 道德规范 "Chapter 3. Patriotic Spirit, Moral Bounds." A
SHORT framing/bridge chapter (~534 source chars — the shortest since ch19), 7 body
paragraphs. It names the Shanghai District's "three-sided enemy" — the Concession police
and detectives, the Shanghai Japanese Gendarmerie, and No.76 — foregrounds the terror of
the Japanese gendarmerie ("谈虎色变") and the double danger of No.76 (Chinese collaborators
who know the District, and a cover for Communist conspiracy), and previews the two chapters
to come, closing on the Yu Yefeng (俞叶封) sanction that ch22 promised to recount. No new
narrative action; a register/theme bridge into ch24.

### Structure (confirmed p-by-p against the source XHTML)
- `index_split_000_0022.xhtml` parses to **1 `<h2>` + 8 `<p>`**, NO `<h1>`, NO `<br/>`,
  NO `<img>`. drop=2 (running header 英雄无名-陈恭澍 + `<h2>` chapter title).
- The txt has 10 lines: L1 header, L2 `<h2>` title, L3 couplet sub-heading, L4-L10 = 7 body
  paragraphs — all ending on terminal punctuation, so **1:1 with no merges, no glued**.
- **ONE standalone couplet sub-heading** (NO number prefix, cf. ch11/ch14/ch21/ch22): L3
  初生之犊组成了一枝生力军 → "Newborn Calves Form a Fresh Fighting Force."
- **No source note markers:** grep `\[\d+\]` returns none (consistent through B16).
- **No images** in the unit (confirmed).
- clean_batch.py: `ch23: 7 body paragraphs, 1 sub-headings, source conserved OK`.

### Checks (all green for ch23; pre-existing artifacts unchanged)
- `verify_unit.py ch23`: parity **7/7**, numbers **0 unresolved** (auto noise), anchors 1 ok.
- `check_align.py ch23`: 7/7, **median ratio 5.82 en/han**, no pair strays > 2.2x. Runs
  above the narrative band (4.55-4.78) as expected for a very short, dense framing essay on
  so few paragraphs (per the kickoff note — read the note, do not reset).
- `check_structure.py`: ALL STRUCTURAL CHECKS PASS; anchors **226 notes, 0 unresolved**;
  headings level positions OK.
- `check_content.py`: **ch23 1 name occurrence, all in the paired paragraph (0 displaced).**
  Known pre-existing artifacts unchanged (from the substring matcher on already-shipped
  chapters, NOT regressions): ch08 Shunde ×3; ch13 Miss Nguyen/Oya Kusuo/Yuan Haowen ×9;
  ch09 "Jize County" ×1 (paragraph 220 — the 鸡泽县 key added in B16 surfaces an older ch09
  rendering; a whole-book reconciliation item, out of scope for a single new unit).
- `qc_entities.py` (reconstructed bilingual, 7 pairs, headings stripped): **entity misses:
  0.** Census: 军统 ×1 (the Juntong), 俞叶封 ×1 (Yu Yefeng), 制裁 ×1 (sanction).
- `check_register.py --ref`: **within tolerance.** contractions 0.0, em-dash 4.2/1k (ref
  8.3), rhythm CV 0.77 (ref 0.60, flagged "little dialogue — noisy", expected for 7 paras).
- Tail verified against the source (rule 4 corollary): L10 (the Yu Yefeng sanction preview —
  险恶/锐不可当/一往无前/突破万难/迭次完成/镇慑作用/制裁…俞叶封一案) rendered in full.
- Build: `23 of 43 chapters, 226 notes`. `qa_epub.py` PASS (226 refs/bodies/backlinks).
  **epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings / 0 infos.**

### Settled renderings REUSED (all keyed or in-text, Part-Three consistent)
"the Shanghai District"; "the Juntong"; 制裁 "sanction"; 敌伪 "the enemy and the puppets";
忠义救国军 "the Loyal and Patriotic Army" (not in this unit); "Special Operations
Headquarters" / "No. 76"; 日本宪兵队 "the Japanese gendarmerie"; 上海日本宪兵队 "the
Shanghai Japanese Gendarmerie"; 新亚和平促进会 "New Asia Peace Promotion Association";
俞叶封 Yu Yefeng; 抗战八年 "the eight years of the War of Resistance" (八 carried, matched).
No new glossary rows (all furniture already keyed or handled in-text; GLOSSARY-KEY
DISCIPLINE upheld — 上海区/七十六号/敌伪/汪伪/日本宪兵队 are consistent in-text renderings,
not distinctive proper-noun keys).

### Notes added (1; first-appearance-disciplined; cumulative 226)
1. **为虎作伥 (playing jackal to the tiger)** — the chang (伥) folk belief: the ghost of a
   person killed by a tiger, bound to lure fresh victims into its path; hence "to abet a
   powerful evildoer." Chen turns it on No.76. Texture note (kind 3); genuinely opaque
   behind the functional gloss, first appearance.
**NOT re-noted (already covered):** No.76 / 特工总部 / Ding Mocun / Li Shiqun (ch04/ch17);
the Japanese gendarmerie; 制裁 "sanction"; the French Concession / International Settlement
(ch04); the Juntong; 忠义救国军 (ch21); the New Asia Peace Promotion Association (ch22); the
Republican calendar convention. 谈虎色变 rendered transparently ("turn pale with terror at
the mere mention") — no note needed.

### Digitization glitches (rendered to plain sense; LISTED, none footnoted — mechanical)
- **百性 → 百姓** "the common people" (我中国百性; homophone glitch, L6). NOISED both forms
  (百姓 and 百性) so the checker does not read the 百 as the count 100.
- **交赋 → 交付** "laid upon / assigned" (上级所交赋的任务, L10; 赋→付 homophone).
None is genuine reading uncertainty, so none is footnoted (per policy).

### data/noise.txt — B17 block appended (each entry commented)
Idiom-noun **百姓** "the common people" (+ the source glitch form **百性**): the 百 is
lexical, not the count 100. All real quantities carried and matched: **抗战八年** "the eight
years of the War of Resistance" (八 CARRIED).

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — ch23 spec added (drop=2; no merges; no glued; 1 standalone
  couplet sub-heading L3). Source-conservation check passes.
- `data/noise.txt` — B17 block (百姓 / 百性).
- `notes.json` — 1 note appended via apparatus_merge.py (numeric character references).
- `scripts/make_ch23_apparatus.py` — the one ch23 note (hanzi built from code points to
  defeat the CJK-mangling hazard; verified 为虎作伥 / 伥 before converting to NCRs).

## Batch B18 — ch24 (Part Three, Chapter 4: "Renown Won in a Hundred Battles")

**Unit:** ch24 = 第四章 三面受敌 一往无前 "Chapter 4. Beset on Three Sides, Ever Forward." A
FULL chapter (~17,105 source chars; 161 body paragraphs), the fuller chapter that DELIVERS
on ch23's preview. It (a) sets out the "new plan" for the Shanghai District (single, secret
accounts and wireless; the great transfer of exposed personnel) carried to Chongqing by Qi
Qingbin for the April-First Congress; (b) anatomizes the "three-sided enemy" section by
section — the International Settlement police (its Special Branch / political section under
劳勃生), the French Concession police, the Shanghai Japanese Gendarmerie (its structure, its
poison unit, and a catalogue of tortures, staged over three periods), and No.76 (its layout,
personnel, the "black gaol," its four tortures, its three great crimes); and (c) tells the
Yu Yefeng (俞叶封) sanction at the 更新舞台 (Gengxin Stage, Jan 1940) in full, through
PARALLEL accounts — Wan Molin's memoir 「沪上往事」 juxtaposed line-by-line with the Shanghai
「申报」 (Shenbao) and a third eyewitness column — a meditation on the unreliability of news
and history. Closes with Dai Li's system-wide Juntong self-review (the 510,000-yuan monthly
budget; the 11,000-man complement) and the arms-donation episode.

### Structure (confirmed p-by-p against the source XHTML)
- `index_split_000_0023.xhtml` parses to **1 `<h2>` + 166 `<p>`**, NO `<h1>`, NO `<br/>`,
  NO `<img>`, NO `[\d+]` note markers. Proven 1:1 against the txt body (166 body lines, ZERO
  mismatches). The txt's 167 `wc -l` vs 168 `awk NR` is a no-trailing-newline artifact.
- drop=2 (running header 英雄无名-陈恭澍 + `<h2>` chapter title).
- **THREE merges** where a source `<p>` boundary severs one sentence: L26/L27 (克莱登's
  parenthetical, …有关抗日 | 活动)); L106/L107 (逮 | 捕「抗日份子」— 逮捕 split); L11/L12 (a
  **STRAY orphan enumerator "(一)"** between the (三)-continuation and (四) of the 「新案」 list
  — a digitization glitch, merged forward into (四) so no orphan "(1)" paragraph appears; the
  stray 一 is conserved in data/zh and rendered to plain sense).
- **SIX sub-headings** (5 section headings + 1 opening couplet): L3 standalone couplet
  壁垒坚强迎接多方面的挑战 → "Fortress Firm, Meeting Challenge from Every Side" (REUSES ch14,
  which shares this chapter title AND couplet; NO 「」 as ch24's source has none); L33
  **head-glued** (一)公共租界巡捕房 → "(1) The International Settlement Police"; L38 standalone
  (二)法租界巡捕房 → "(2) The French Concession Police"; L46 **tail-glued** 「日本宪兵队」惨无人道;
  L95 **tail-glued** 罪恶昭彰的「七十六号」 (its tail ends in a full-width 」 — easy to miss in a
  non-terminal scan); L122 **tail-glued** 以雷霆万钧之势打击魔鬼.
- The top-of-chapter (一)-(四) 「新案」 list items (L7-L12) are ORDINARY list paragraphs
  (rendered per parity, NOT headings), distinct from the (一)/(二) SECTION headings.
- Roster / juxtaposition / lead-in lines kept as DELIBERATE separate `<p>` (NOT merged): the
  gendarmerie district-command dash-roster (L57); the sanction-case roster (L125/L126); the
  申报 news-article `<p>` (L141-L148, each opening 「); the 沪上往事 / 申报 juxtaposition lines
  (L154-L159). L34 名称如下： is a soft list lead-in (kept separate).
- clean_batch.py: `ch24: 161 body paragraphs, 6 sub-headings, source conserved OK`.

### Checks (all green for ch24; pre-existing artifacts unchanged)
- `verify_unit.py ch24`: parity **161/161**, numbers **0 unresolved** (auto noise), **6
  anchors ok**.
- `check_align.py ch24`: 161/161, **median ratio 5.33 en/han**, no pair strays > 2.2x. Above
  the document-heavy band (4.7-4.9) because of the MANY very short quoted/table/juxtaposition
  lines (the one-word torture verbs 「打」「摔」…, the 沪上往事/申报 alternation, the police
  establishment tables) that expand proportionally in English — register (below) is the real
  gate and passes.
- `check_structure.py`: ALL STRUCTURAL CHECKS PASS; anchors **232 notes, 0 unresolved**.
- `check_content.py`: **ch24 118 name occurrences, all in the paired paragraph (0 displaced).**
  Seven initial displacements were all keyed-name/place renderings I aligned to the glossary:
  北平 Beiping (not Peiping), 天津 Tianjin (not Tientsin), 汉口 Hankou (not Hankow), 四川
  Sichuan (not Szechuen — "North Sichuan Road"), 虹口 Hongkou (not Hongkew — incl. the SMP
  station roster), and 新一组 "New Group One." Known pre-existing artifacts UNCHANGED (NOT
  regressions): ch08 Shunde ×3; ch13 Miss Nguyen/Oya Kusuo/Yuan Haowen ×9; ch09 "Jize County"
  ×1 (para 220, a whole-book reconciliation item).
- `qc_entities.py` (reconstructed bilingual, 161 pairs, headings stripped): **entity misses:
  0.** Census: 俞叶封 ×25, 特工总部 ×17, 更新舞台 ×12, 李士群 ×11, 陈默 ×10, 新艳秋 ×9.
- `check_register.py --ref`: **within tolerance.** contractions 0.0, shall 25% (deliberate,
  in the B06-B16 band 29-43%), em-dash 4.4/1k (ref 8.3), rhythm CV 0.60 (= ref 0.60).
- Tail verified against the source (rule 4 corollary, critical on a 17k single-pass unit):
  the last four paragraphs (Dai's 8-point Juntong self-review; his two self-criticism quotes;
  the 510,000-yuan budget + 11,000-man complement; the arms donation; the closing on the
  "friend" of unclear background) rendered in full, no fabrication, no drift. Pair 161's
  elliptical 前者 rendered to preserve the source's two-referent ambiguity (not conflated).
- Build: `24 of 43 chapters, 232 notes`. `qa_epub.py` PASS (232 refs/bodies/backlinks).
  **epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings / 0 infos.**

### Settled renderings REUSED (Part-Three consistent)
"the Shanghai District"; "the Juntong"; 制裁 "sanction"; 督察 "inspector"; 敌伪 "the enemy
and the puppets"; 汪伪 "Wang puppets"; 忠义救国军 "the Loyal and Patriotic Army"; 特工总部 /
七十六号 "Special Operations Headquarters" / "No. 76"; 丁默邨 Ding Mocun / 李士群 Li Shiqun
(NOTED ch04/ch17 — NOT re-noted); 新亚和平促进会 "New Asia Peace Promotion Association"; 俞叶封
Yu Yefeng; 陈默 Chen Mo; 万墨林 Wan Molin / 沪上往事 (Wan's memoir, NOTED ch22); 万里浪 Wan
Lilang; 更新舞台 "Gengxin Stage" (reused from ch22, now KEYED); 公共租界 "International
Settlement" / 法租界 "French Concession"; 工部局 "Municipal Council"; 日本宪兵队 "the Japanese
gendarmerie" / 上海日本宪兵队 "the Shanghai Japanese Gendarmerie"; the Republican-year
convention (literal; checker matches the source numeral).

### New glossary rows (9; BY HAND into the sectioned glossary; every row a pinyin field)
people (8): 劳勃生 Lao Bosheng (provisional — SMP political-section chief, a transliteration
of an uncertain Western name); 袁殊 Yuan Shu (aka Xueyi/Xiaoyi); 新艳秋 Xin Yanqiu (dan
actress); 吴世宝 Wu Shibao (No.76 guard commander, alias Yunfu); 胡均鹤 Hu Junhe (No.76 2nd
Section); 傅也文 Fu Yewen (provisional — No.76 secretary-general); 刘俊卿 Liu Junqing
(provisional — SMP officer); 蒋福田 Jiang Futian (provisional — French Concession police).
places (1): 更新舞台 Gengxin Stage. NOT keyed (rendered inline / by note, not distinctive
one-way proper-noun keys): 申报/新申报/中华日报/民族晚报 (periodicals — notes/inline); 克莱登/
葛乐华/普莱德 (one-off transliterated SMP officers, pinyin inline); the Japanese gendarmerie
officers (romaji inline, cf. ch22); 云九/王振鹄/随波/叶吉卿/王宪和/张国震 (one-off, inline).

### Notes added (6; first-appearance-disciplined; cumulative 232)
1. **the SMP Special Branch / 政治科 + 劳勃生 (Lao Bosheng)** — the political section is the
   Special Branch, the political-intelligence arm of the British-run Settlement police (the
   chapter's chief target); the name is an uncertain transliteration of a Western surname
   (Robertson/Robinson?), identity not fixable; 克莱登 is the same kind.
2. **更新舞台 / 新艳秋 / Peking opera** — Xin Yanqiu, a dan (female-role) actress of the Cheng
   Yanqiu school; the three operas named in the rival accounts (Yutangchun / Xiaoshang River-
   Yang Zaixing / Tiaohuache-Gao Chong) are Peking-opera staples; Chen sets them side by side
   to show how one night yields three different "eyewitness" plays.
3. **申报 (Shenbao)** — China's paper of record, founded Shanghai 1872; distinguished from the
   occupation-era 新申报 (noted ch20). Chen's quoted issue is a straight next-morning report.
4. **多摩部队 / 玉部队 (Tama Force / Gyoku Unit)** — by Chen's informant's account, part of the
   Japanese army's secret poison / chemical-and-biological research (same field as Unit 731).
5. **三不主义 (Wu Peifu's "Three Nots")** — Wu Peifu (1874-1939), warlord; his personal code
   (variously reported: no refuge in the concessions, no foreign loans, no hoarded wealth);
   refused all Japanese overtures, died at Beiping 1939.
6. **袁殊 (Yuan Shu)** — the "five-faced spy" (1911-1987): drew pay from Juntong, Zhongtong,
   the Japanese, and the Wang regime while a CCP agent throughout; Chen's suspicion was right.
**NOT re-noted (already covered):** No.76 / 特工总部 / Ding Mocun / Li Shiqun (ch04/ch17); the
International Settlement / French Concession (ch04); the Japanese gendarmerie (ch11/ch23);
制裁 "sanction"; the Blue Shirt Society / Lixingshe (ch05/ch08); the Green-Gang "three
tycoons" incl. 张啸林's 1940 assassination (ch04); 沪上往事 / Wan Molin (ch22); 中华日报 (ch20);
忠义救国军 (ch21); the Republican calendar. Vivid tortures (老虎櫈 tiger bench, 灌凉水, 皮鞭子)
described transparently in-text — no note needed.

### Digitization glitches (rendered to plain sense; LISTED, none footnoted — mechanical)
- **Stray orphan "(一)"** (L11) between the (三)-continuation and (四) of the 「新案」 list —
  merged forward into (四), absorbed (see Structure).
- **制裁俞叶原 → 俞叶封** (L138; 原-for-封): rendered "the sanction of Yu Yefeng."
- **仁济医仁 → 仁济医院** (L142; 仁-for-院): rendered "the Renji Hospital."
- **南就日本宪兵司令部 → 南京** (L50; 就-for-京): rendered "Nanking."
- **计锋相对 → 针锋相对** (L53; 计-for-针): rendered "stood point-blank opposed."
- **信千拈来 → 信手拈来** (L162; 千-for-手, a column name): rendered "Idle Gleanings."
- **毕高奎同同志** (L16; dittography 同同): rendered once.
- **汇司虹口** (L34 station roster): a garbled/duplicated SMP-station token (虹口 duplicated,
  汇司 unclear); rendered to sense within the roster.
- **Source internal date inconsistency:** L91 (commander table) gives Miura Saburo's term as
  "自二十年至二十九年" (二十 for 二十七), where L95 gives "自二十七年至二十九年" — both rendered
  faithfully (the 三面受敌 gendarmerie founded 民国二十七年元月, so 二十 is the slip). NOT a
  translation error; kept visible, both numerals matched.
None is genuine reading uncertainty, so none is footnoted (per policy).

### data/noise.txt — B18 block appended (each entry commented)
Idioms/approximates: 四季, 九死一生, 十万八千, 三两万, 三教九流, 漏洞百出. Japanese
name-numerals: 三浦三郎 / 三浦 (Miura), 四方谅二 (Shikata), 五岛 (Goto). Bare-surname 万: 万先生
"Mr. Wan," 万的连襟 "Wan's brother-in-law." Buddhist/column names: 大千世界, 信千拈来. The ○
(U+25CB circle-zero) ADDRESS artifact 五○○ (Lane 500) — the numeric checker cannot read ○ as
zero and mis-parses it as a bare 5; the English carries the real value (Lane 500), so only
the mis-read glyph-string is noised (cf. 四○七 rooms, which self-resolve via the neighboring
ordinal dates fourth/seventh). Name-numerals: 邵范九, 云九. ALL REAL quantities CARRIED and
matched — the two police-establishment tables (513/599/256/3645 Settlement force; 1794/212
French; 4666 constables, 509 sergeants…) rendered as digits or as word-forms so the checker's
、/○-split values match; the twenty-ninth-year budget 五十一万余 → "510,000-odd," the complement
一万一千余 → "11,000-odd," the 一百二十余 transfer, the 一百五十 sq-metre gaol, all carried.

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — ch24 spec added (drop=2; 3 merges incl. the orphan-(一) absorb;
  3 tail-glued + 1 standalone section headings + 1 standalone couplet); **NEW `glued_head`
  spec field** (a heading fused onto a paragraph HEAD, e.g. L33 (一)公共租界巡捕房) with a
  startswith-assert, mirroring the existing tail-glued `glued`. Source-conservation passes;
  the .get("glued_head", {}) default leaves all earlier units untouched.
- `scripts/add_ch24_glossary.py` — adds the 9 new rows BY HAND into the SECTIONED glossary
  (idempotent; each hanzi key asserted present in data/zh/ch24.txt to catch mangling).
- `scripts/make_ch24_apparatus.py` — the 6 ch24 notes (every non-ASCII glyph asserted present
  in data/zh/ch24.txt before converting to NCRs; defeats the CJK-mangling hazard).
- `data/noise.txt` — B18 block (see above).
- `notes.json` — 6 notes appended via apparatus_merge.py (numeric character references).

## Batch B19 — ch25 (Part Three, Chapter 5: "Renown Won in a Hundred Battles")

**Unit:** ch25 = 第五章 全面检讨奇人奇事 "Chapter 5. A Full Reckoning: Remarkable People,
Remarkable Deeds." A FULL chapter (~15,600 source chars; 183 body paragraphs), continuing
ch24's system-wide reckoning. Three movements: (a) **"A Review of the Juntong's Work in the
Early Years of the War"** — reproduces Dai Li's own work-directives, under the run-in labels
情报部份 (intelligence), 破坏部份 (sabotage), 行动部份 (action), and 检讨总结 (the summary of
shortcomings, 15 numbered self-criticism points ending on Dai's own); (b) **"Accepting Without
Leave a Consignment of Donated Arms"** — the 144 Mauser pistols the exile "friend" sends via
Hu Yongquan, stored on Qi Qingbin's advice against Dai's telegram foreseeing a mass action
(the Sihang Warehouse / interned soldiers), the German "Mr. Shi" met through the eye-doctor
Nie Chonghou; (c) **"A Remarkable Man of Political Background Who Yet Served No Double-Agent
Ends"** — the stalled sanction of Zhang Xiaolin, the Tianjin notable Pan Zixin ("Master Pan
the Seventh"), and the long Fan Xing (范纪曼) intelligence-source puzzle set against the CCP's
Shanghai underground (Pan Hannian, the Jiangsu Provincial Committee). Closes on the sacrifice
essay and Sima Qian's "heavier than Mount Tai, lighter than a feather."

### Structure (confirmed p-by-p against the source XHTML)
- `index_split_000_0024.xhtml` parses to **1 `<h2>` + 191 `<p>` + 2 `<br/>`**, NO `<h1>`, NO
  `<img>`, NO `[\d+]` note markers. Proven 1:1: after drop=2 the txt's 193 body lines map to
  the 191 `<p>` once the two intra-`<p>` `<br/>` pairs are rejoined (verified with a byte-exact
  p-by-p diff, zero mismatches).
- drop=2 (running header 英雄无名-陈恭澍 + `<h2>` chapter title).
- **NINE merges.** TWO are the intra-`<p>` `<br/>` line breaks — a NEW trigger vs ch24, a
  `<br/>` INSIDE one `<p>` rendered as a newline by the extractor: L46/L47 (…爆破器材等。`<br/>`
  以及…), L105/L106 (…比我有见地。`<br/>`而况且…). SEVEN are source `<p>` boundaries that sever
  one sentence (the class merged since ch06), TWO of which CHAIN into a `<br/>` pair:
  L5/L6 (comma), L45/L46/L47 (秦|同志 + `<br/>`), L52/L53 (应即予|加强), L61/L62 (标|准, inside a
  quoted line), L84/L85 (离开本|局), L104/L105/L106 (到时|候 + `<br/>`), L118/L119 (结果|如何).
  **NOTE:** the B18 kickoff's coarse "191 = 191 `<p>`, only the 2 `<br/>`" reconciliation
  missed these 7 severed-`<p>` boundaries; per CLAUDE.md's merge rule they merge, and parity
  is data/zh↔reading.md (183/183), NOT the raw `<p>` count — a documented, correct departure.
- **THREE sub-headings.** L3 standalone opening couplet 八年抗战初期「军统局」工作检讨 → "A Review
  of the Juntong Bureau's Work in the Early Years of the Eight-Year War of Resistance" (cf.
  ch11/ch14/ch21/ch22/ch23/ch24). L88 **tail-glued** 未经许可接受了 ─一批赠与的武器经手 (ends
  non-terminal after a space+─) → "Accepting Without Leave a Consignment of Donated Arms; the
  Handling of It." L126 **tail-glued** 有政治背景无反间作用的奇人奇事 (ends on terminal 事, reads
  as the section heading for the 张啸林/范行 narrative that follows) → "A Remarkable Man of
  Political Background Who Yet Served No Double-Agent Ends."
- The four work-review dividers 情报部份─ (L8, head-glued to its quote), 破坏部份─ (L29,
  standalone), 行动部份─ (L60, standalone), 检讨总结─本局工作当前之缺点：(L70, head-glued) are
  kept INLINE as run-in labels (source formats them inconsistently glued/standalone), NOT
  ### headings — this preserves parity naturally and matches the source's own presentation.
- The enumerated directive/summary items (1.-6. intelligence needs; 1.-11. sabotage编组;
  1.-15. summary), the sub-list headers 对战区：/ 对后方：, the 范行-analysis list items, and
  the `：`-lead-ins are DELIBERATE separate `<p>` (rendered per parity, NOT merged).
- clean_batch.py: `ch25: 183 body paragraphs, 3 sub-headings, source conserved OK`.

### Checks (all green for ch25; pre-existing artifacts unchanged)
- `verify_unit.py ch25`: parity **183/183**, numbers **0 unresolved** (auto noise), **10
  anchors ok**.
- `check_align.py ch25`: 183/183, **median ratio 4.97 en/han**; one outlier (11. 密本照发 →
  "The cipher-books to be issued as before," a 4-char directive item). In the document-heavy
  band (ch24 = 5.33) because of the many short quoted-directive/list lines; register is the
  real gate and passes.
- `check_structure.py`: ALL STRUCTURAL CHECKS PASS; anchors **242 notes, 0 unresolved**.
- `check_content.py`: **ch25 97 name occurrences, all in the paired paragraph (0 displaced).**
  Known pre-existing artifacts UNCHANGED (NOT regressions): ch08 Shunde ×3; ch13 Miss Nguyen/
  Oya Kusuo/Yuan Haowen ×9; ch09 "Jize County" ×1.
- `qc_entities.py` (reconstructed bilingual, 183 pairs, headings stripped): **entity misses:
  0.** Census: 范行 ×38, 军统 ×12, 行动组 ×9, 天津 ×9, 胡永荃 ×8, 潘子欣 ×7, 北平 ×6, 制裁 ×5,
  督察 ×5, 张啸林 ×5. 制裁 rendered "sanction," 督察 "inspector/inspectorate," 军统局 "the
  Juntong Bureau" throughout (the qc gate).
- `check_register.py --ref`: **within tolerance.** contractions 0.0, shall 67% (deliberate —
  Chen's formal narration PLUS the many imperative Dai Li directives "shall be set up / shall
  have / shall be issued"; the tool itself flags it informationally as "may be deliberate"),
  em-dash 7.4/1k (ref 8.3), rhythm CV 0.69 (ref 0.60).
- Tail verified against the source (rule 4 corollary, critical on a 15k single-pass unit): the
  last eight paragraphs (the sacrifice essay; the labor-movement nameless dead; the Xiao
  family 5/3/2; New Group One; the buried-alive comrade; 特工总部 killing 8, only 3 sourced;
  the Sima Qian close) rendered in full, no fabrication, no drift. Every count carried.
- Build: `25 of 43 chapters, 242 notes`. `qa_epub.py` PASS (242 refs/bodies/backlinks).
  **epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings / 0 infos.**

### Settled renderings REUSED (Part-Three consistent)
"the Shanghai District"; "the Juntong"/"the Juntong Bureau"; 制裁 "sanction"; 督察 "inspector"
(function → "inspectorate," keeping the checker's substring); 敌伪 "the enemy and the puppets";
汪伪 "Wang puppets"; 忠义救国军 "the Loyal and Patriotic Army" (NOTED ch21); 特工总部/七十六号
"Special Operations Headquarters"/"No. 76" (李士群 Li Shiqun NOTED ch04/ch17 — NOT re-noted);
公共租界 "International Settlement"/法租界 "French Concession" (NOTED ch04); 俞叶封/兪叶封 Yu
Yefeng; 张啸林 Zhang Xiaolin (NOTED ch04, one of the three Green-Gang tycoons); 齐庆斌 Qi
Qingbin, 张作兴 Zhang Zuoxing (Brother = 兄); 戴雨农 Dai Yunong/Mr. Dai; 郑介民 Zheng Jiemin
(NOTED ch04); 杜月笙 Du Yuesheng (NOTED ch17); Whampoa (NOTED ch05); 驳壳枪 Mauser (NOTED ch08);
北平 Beiping / 天津 Tianjin / 四川 Sichuan (keyed pinyin, NOT postal); attested Shanghai roads
inline (Seymour Road 西摩路, Route Doumer 杜美路, Route de Grouchy 格罗希路, Carlton Apartments
卡尔登公寓, Bubbling Well Road 静安寺路); the Republican-year convention (literal; checker
matches the source numeral, or auto-escapes via +1911).

### New glossary rows (5 net new; BY HAND into the sectioned glossary; every row a pinyin field)
Of the 9 people rows asserted, 4 pre-existed (秦启荣 Qin Qirong, 毛人凤 Mao Renfeng, 潘汉年 Pan
Hannian, 高荣 Gao Rong — added in earlier chapters, en matched). NEW (5): 聂崇侯 Nie Chonghou
(provisional — the Jiangxi/German-trained eye doctor); 潘子欣 Pan Zixin (provisional — "Master
Pan the Seventh," the Tianjin notable); 胡永荃 Hu Yongquan (provisional — the fixer who carries
the arms gift); 彭雅萝 Peng Yaluo (provisional — Fan Xing's companion); **兪叶封 Yu Yefeng** (the
variant glyph 兪-for-俞 the source uses, keyed so qc gates it in this unit too). NOT keyed
(rendered inline in pinyin, glossary-key discipline): the telegram names 钱新民/廖公劭, the
former secretary 刘方雄, the sabotage-directive operatives 方步舟/谢冰/岳烛远/谢镇南/邹适, the
CCP Jiangsu Committee roster 刘晓/刘长胜/张爱萍/刘宁一/王尧山/沙文汉/张执一/刘少文, 叶吉卿; and
the German "Mr. Shi" (只 a surname-sound). Shanghai roads kept inline (attested, not keyed).

### Notes added (10; first-appearance-disciplined; cumulative 242)
1. **秦启荣 (Qin Qirong)** — Shandong Nationalist guerrilla commander, sixth Whampoa class, a
   Juntong man; killed 1943; the demolition brigade / Qingdao action group were his Shandong work.
2. **"twenty thousand yuan a day" (每日 vs 每月)** — the directive prints "a day," but Chen's own
   reckoning below and item 7's "two months' funds" both treat it as monthly; rendered as the
   source prints it, the discrepancy the source's own (rule 4: made visible, not smoothed).
3. **毛人凤 (Mao Renfeng)** — Dai Li's closest lieutenant and effective administrator; succeeded
   him at the head of the Juntong after Dai's 1946 death.
4. **釜底抽薪 (drawing the firewood from under the cauldron)** — the classical idiom for striking
   at a trouble's root; Dai applies it to the sanction of Wang Jingwei, and Chen takes it up.
5. **四行仓库 (the Sihang Warehouse / the interned "lone battalion")** — the 88th Division's last
   stand ("Eight Hundred Heroes"), Oct 1937; the disarmed survivors interned in the Settlement
   are the "detained officers and men" of Dai's telegram.
6. **洋泾浜/pidgin English (Yangjingbang)** — the source's 洋经滨 homophone; the creek dividing
   the Settlement from the French Concession that named Shanghai's trade-jargon and "pidgin."
7. **潘汉年 (Pan Hannian)** — the CCP's foremost Shanghai intelligence officer, working the seams
   among the Nationalist/Japanese/Wang services; met Wang Jingwei, dealt with Li Shiqun; purged
   1955, later rehabilitated; the "Jiangsu Provincial Committee" was the Party's Shanghai lead.
8. **老泰山 ("Old Mount Tai" = father-in-law)** — the vivid colloquial kinship term, playing by
   chance against the classical Mount Tai figure that closes the chapter.
9. **蟹壳黄 (xieke huang, "crab-shell yellow")** — the small flaky sesame-brushed Shanghai
   pastry eaten hot from the oven, savory (scallion) or sweet.
10. **司马迁 "heavier than Mount Tai, lighter than a feather"** — Sima Qian's "Letter in Answer
   to Ren An"; the proverb for weighing a death by its worth, which also titles the next chapter.
**NOT re-noted (already covered):** the Marco Polo Bridge Incident (ch13); No.76 / 特工总部 /
Li Shiqun (ch04/ch17); the International Settlement / French Concession (ch04); 郑介民 Zheng
Jiemin (ch04); 何应钦 He Yingqin (ch09); Du Yuesheng (ch17); Whampoa (ch05); the Mauser 驳壳枪
(ch08); 忠义救国军 (ch21); 张啸林 as a Green-Gang tycoon (ch04); the Republican calendar.

### Digitization glitches (rendered to plain sense; LISTED, none footnoted — mechanical)
- **载先生 → 戴先生** (L27/data-zh L29; 載-for-戴): rendered "Mr. Dai."
- **敌军行重 → 敌军行动** (L8 directive; 重-for-动): rendered "movements of the enemy forces."
- **铁路坏工作 → 铁路破坏工作** (L31; 破 dropped): rendered "sabotage on the railway."
- **而练亦由吾人负责 → 而训练** (L48; 训 dropped): rendered "and the training likewise."
- **准予继绩行动 → 继续** (L48; 绩-for-续): rendered "to carry our action on."
- **在杭战初期 → 抗战** (L53; 杭-for-抗): rendered "in the early days of the war."
- **忠义教国军 → 忠义救国军** (L59; 教-for-救): rendered "the Loyal and Patriotic Army."
- **因为敌后活务 → 敌后工作/活动** (L57; 活务 unclear): rendered "work behind the enemy's lines."
- **对行动工作的个扼要 → 一个扼要** (L57; 一 dropped): rendered "a terse review."
- **粤妙 → 奥妙** (L94; 粤-for-奥): rendered "the deep subtlety."
- **不管共产党采取什么态 → 什么态度** (L26; 度 dropped): rendered "whatever posture."
- **始终是把它列工作 → 列为工作** (L26; 为 dropped): rendered "held it always to be."
- **居该党领导地至者 → 领导地位** (L19; 至-for-位): rendered "leading positions."
- **我朱来 → 我素来(?)** (L126; 朱-for-素, uncertain): rendered "I had of old come to it."
- **× redactions (source's own blanks, rendered as em-dash blanks):** 自×月份起 ("from the ——
  month"), 贺×同志 ("Comrade He ——"), ×棋 / Pan's mis-heard game ("——-chess," Chen guessing
  "copper-chess"), 陈××先生 in Liu Shaokui's memoir ("Mr. Chen ——"). NOT footnoted — the
  narrator explains his own uncertainty (×棋) or these are self-evident redactions.
None is genuine reading uncertainty, so none is footnoted (per policy). The 每日/每月 directive
discrepancy IS footnoted (note 2) because it is a substantive stumble a reader would hit.

### data/noise.txt — B19 block appended (each entry commented)
Elided years: 二十八、九 (the 九 elides its 二十; English carries "twenty-eighth and twenty-ninth
years"). Name-numerals: 道三 (Zhou Daosan), 四行仓库 (Sihang Warehouse), 广九 (Canton–Kowloon
railway). Idioms: 日理万机, 两缺 (器材教两缺 "both wanting"), 一宅两用. Weekday: 星期六. Lexical:
零钱 (loose change). ALL REAL quantities CARRIED and matched as DIGITS so the checker's split
values align: the demolition-brigade table (500 men, 20,000/day, 20 Mausers/10,000 rounds, 20
revolvers/4,000 rounds, 12 Mausers/10 revolvers/200 rounds, 2,400 & 3,000 yuan); the 144 → 140
Mausers, 13,000-odd rounds; the 150,000 Northeast funds; the twenty-ninth-year budget carried
identically to ch24 (11,000 men, 510,000-odd yuan); the 100,000-yuan gun valuation.

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — ch25 spec added (drop=2; 9 merges incl. the 2 intra-`<p>` `<br/>`
  pairs and 2 chains that fold a severed-`<p>` boundary into a `<br/>` pair; 2 tail-glued + 1
  standalone sub-headings). The `<br/>`-inside-a-`<p>` case is handled by the existing `merges`
  machinery (the extractor renders `<br/>` as a newline, so it is just another line pair).
- `scripts/add_ch25_glossary.py` — adds the new rows BY HAND into the SECTIONED glossary
  (idempotent; each hanzi key asserted present in data/zh/ch25.txt; 4 pre-existed, 5 net new).
- `scripts/make_ch25_apparatus.py` — the 10 ch25 notes (every non-ASCII glyph asserted present
  in data/zh/ch25.txt before converting to NCRs; the correct 洋泾浜 glyphs are ABSENT from the
  source so the note uses the source's 洋经滨 form + pinyin, and 孤军/司马迁 are described in
  English/pinyin since those glyphs are not in ch25's source).
- `data/noise.txt` — B19 block (see above).
- `notes.json` — 10 notes appended via apparatus_merge.py (numeric character references).

---

## Batch B20 (ch26) — 第六章 泰山鸿毛 同此一掷 "Chapter 6. Mount Tai or a Feather, All on One Throw"

A FULL martyr-roster chapter (~19,000 source chars). Source XHTML parses to 1 `<h2>` + 280 `<p>`
+ 54 `<br/>`, NO `<h1>`, NO `<img>`, NO `[\d+]` note markers; proven byte-exact p-by-p against the
txt body. drop=2. **321 body paragraphs; 6 sub-headings.** EPUB now 26/43 chapters, 253 notes.
All checks green; qa_epub PASS; epubcheck 0/0/0/0.

### Structure (the 54 `<br/>` and the merges)
ALL 54 `<br/>` fall in just FOUR `<p>`, and — contrary to the coarse "every `<br/>` is a merge"
assumption — they are mostly TABLE/roster line breaks, kept as separate rows (CLAUDE.md: roster
lines are deliberate separate lines):
- **p#177 (34 `<br/>` = 35 rows):** the enemy-compiled 「蓝衣社在沪所犯案件统计表」 tally of our
  sanctions of Japanese personnel (name/date/place/casualty/action-group) — rows KEPT.
- **p#214 + p#217 (9 + 9 `<br/>` = two 10-row blocks):** the Japanese gendarmerie's own
  「大陆宪兵实录」 record of anti-Japanese incidents (July–Oct, in Japanese) — rows KEPT.
- **p#211 (2 `<br/>` = 3 segments):** three complete reflective PROSE sentences in one `<p>` —
  the ONLY `<br/>`-prose MERGE (chain L248-249-250 → one paragraph; cf. ch25's intra-`<p>` `<br/>`).
- **SEVEN severed-`<p>` merges** (a source `<p>` boundary severing one sentence): L25/26 (处理|之,
  inside a quoted letter), L31/32 (说在|安全撤退), L90/91 (为了一个|「权」字), L161/162 (一日，在|
  江湾, inside the quoted tally), L263/264 (Ivanov row's 暗杀 verb split across the `<p>`),
  L304/305 (干|起来了), L323/324 ((块)|放在).
- **SIX sub-headings:** 4 standalone (L3 opening couplet 没有名籍生死不明的先烈们; L96 the Xu Wenqi
  essay title 中日战争中死难无名英雄之一; L218 the enumerated section heading 二、日本宪兵留下来的
  一段记录; L277 「抗日杀奸团」为抗战奉献牺牲) + **2 TAIL-GLUED** (L38 …又一例证。+ 萧氏一家满门忠贞;
  L76 …再深一层去研究了。+ 我们的同志作了敌伪的「活人祭」 — this one ends in a full-width 」, which a
  non-terminal scan misses; caught via the three-tell's 」 case). The 二、 record heading has no
  explicit 一、 sibling (the enemy-compiled 统计表 above is the implicit "one") — a faithful
  numbering anomaly.

### Checks
- verify_unit ch26: **parity 321/321, numbers 0 unresolved, anchors 11 ok.**
- check_align ch26: 321 source / 321 translation, **median ratio 4.98 en/han** (document-heavy,
  in line with ch24 5.33 / ch25 4.97; alignment OK, no pair strays >2.2x).
- check_structure: parity 321/321 OK; ALL STRUCTURAL CHECKS PASS.
- check_content: ch26 **261 name occurrences, 2 DISPLACED** — both KNOWN keyed-substring
  FALSE POSITIVES, NOT regressions: 武汉 "Wuhan" (city key) matches inside the personal name
  武汉卿 "Wu Hanqing"; 劳勃生 "Lao Bosheng" (the SMP officer, keyed) matches inside the road name
  劳勃生路, correctly rendered "Robison Road". (Pre-existing artifacts unchanged: ch08 Shunde ×3,
  ch13 ×9, ch09 "Jize County" ×1.)
- qc_entities on the reconstructed bilingual: 2 misses = the SAME two false positives; all 25 new
  keyed people + 2 orgs render consistently (census: 蒋安华 ×42, 抗团 ×29, 徐寿新 ×14, 余延智 ×18…).
- check_register --ref: within tolerance; **83% "shall"** (deliberate — the many quoted Dai Li
  telegrams + the formal Xu Wenqi essay; cf. ch25 67%). Do NOT de-formalize.
- Tail verified against source (the 张啸林/林怀部 questions, source L324-328) — faithful, no fabrication.

### The heavily-corrupted source block (rendered to reconstructed sense; FOOTNOTED)
p#120-123 and p#125 (the paragraphs introducing the sanction-of-Japanese section and the Kang
Corps) are SEVERELY garbled in the source ebook — nearly every character miscut (e.g. 「敌讨划」,
二作 for 工作, 敉戎们 for 被我们, 圆志高亢 for 斗志高亢, 戴两农 for 戴雨农, 百寓人 for 百万人). Rendered
to their evident sense, which the CLEAN parallel passages below fully corroborate (the three-point
proposal at p#127+, the tally dates, and the detailed Akagi account). Note 4 flags the block AND
the one substantive slip left visible: the garbled text credits Akagi's sanction to the "Second
Action Brigade" (第二行动大队), while the tally and the gendarmerie account both credit Jiang Anhua's
Third Action Brigade (第三行动大队) with Li Liang as director.

### Digitization glitches (rendered to plain sense; NOT footnoted unless real reading uncertainty)
记亿→记忆 (记忆, several), 「权」宇→字, 虹口公围→公园, 行动工佯→工作, 戴先坐→戴先生, 囚为→因为,
接髑→接触, 余寿棪→徐寿棪 (余/徐), 陈恭树→陈恭澍 (the enemy's own 澍→树 mis-spelling, which Chen
himself remarks on), 其长安→长女, 徐文棋→徐文祺 (in a quote), 二遇→那一带, 绣东→浦东, 甚股→甚殷,
十一一月→十二月, 汪苏省委→江苏省委, 这般人物代表？→代表了 (stray ？), 但？也为所欲为 (stray ？),
挨了？才动手 / ？？ (stray ？). ○ (U+25CB) and × redactions: 社会事业xxxx委员会, x新纱厂, 陈xx/刘xx,
交寿○, 一○四号 (No. 104, ○-zero), the tally's 海 xx / 华 xx / 西岩 x, 美制○？三八 (an American .38),
陆 xx 之夫人 (Mr. Lu ——). All carried to real values in the English; ○/× glyph-strings noised.

### data/noise.txt — B20 block appended (each entry commented)
Name-numerals: 三郎 (Saburō in 小林峰三郎/杉本喜三郎), 五十岚 (Igarashi), 三兴 (Sanxing Mill),
三通书局 (Santong Book Co.). Idioms: 万岁, 九泉, 抖五抖六, 百出 (花样百出), 百业, 数百万, 二位.
Weekday: 星期五. Month-glyphs rendered as English month-names (never as a digit in narrative or in
the Japanese roster): 六月-十月. ○-artifact address: 一○四. Glitches: 戴两农 (两 for 雨), 二作
(二 for 工), 零星 (0), 十一一月 (11 for Dec), 百寓 (百 for 百万). All REAL quantities CARRIED as
digits (the 35-row tally 29/9/29…30/10/22 with casualty counts; 3332 badge; 51524 gun number;
No. 104/No. 24/No. 321; 370 yuan/month; 500,000 yuan road-money; 3,000+ arrested; the 500-man
guerrilla band with 250 long/short guns; 60-odd, 20-odd, 30-odd; 83 captured, 19 losses).

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — ch26 spec added (drop=2; 9 merges = 1 intra-`<p>` `<br/>` prose chain
  (248-250) + 7 severed-`<p>` boundaries; the three TABLE `<p>` (p#177/214/217) NOT merged, kept as
  roster rows; 4 standalone + 2 tail-glued sub-headings incl. the `」`-ending L76).
- `scripts/add_ch26_glossary.py` — 27 new rows BY HAND into the sectioned glossary (25 people +
  2 orgs; each hanzi key asserted present in data/zh/ch26.txt).
- `scripts/make_ch26_apparatus.py` — the 11 ch26 notes (every non-ASCII glyph asserted present in
  data/zh/ch26.txt before NCR conversion).
- `data/noise.txt` — B20 block (see above).
- `notes.json` — 11 notes appended via apparatus_merge.py.

## Batch B21 (ch27) — 第八章 大亨之死 扑朔迷离 "Chapter 8. The Death of a Tycoon, Shrouded in Mystery"

A FULL chapter (~12,500 source chars): the Zhang Xiaolin tycoon-death case, continuing ch26's
tail on the 张啸林/林怀部 sanction (14 Aug 1940). Source XHTML parses to 1 `<h2>` + 136 `<p>`,
NO `<h1>`, NO `<br/>`, NO `<img>`, NO `[\d+]` note markers; proven byte-exact p-by-p against the
txt body (136 body lines after drop=2, ZERO mismatches). drop=2. **133 body paragraphs; 3
sub-headings.** EPUB now 27/43 chapters, 259 notes. All checks green; qa_epub PASS; epubcheck 0/0/0/0.

**Faithful numbering gap:** Part Three SKIPS 第七章 — ch26 was 第六章, ch27 is 第八章 (confirmed
against book.json title_en). Not an error; preserved.

### Structure (headings + merges)
ch27 uses ENUMERATED 一、二、三 SECTION headings (NOT the couplet style of ch21-ch26):
- **L3 一、这件案子不一定是我们干的** — standalone (its own `<p>`) → `### 1.`
- **L64 …时有著作发表。+ 二、事实该怎么样便怎么样** — TAIL-GLUED after a terminal 。 → `### 2.`
- **L94 …我们有办法把你弄出来。」+ 三、一篇游戏文章写的满纸荒唐** — TAIL-GLUED after a full-width
  `」` (the three-tell's `」` case; cf. ch24/ch26) → `### 3.`
- **TWO severed-`<p>` merges** (a source `<p>` boundary severing one sentence): L13/14 (…始于清|
  道光二十九年…, inside the quoted 「上海租界问题」 excerpt), L41/42 (…也在新闻中|出现过…).
- The 六、七月 (June–July) and 五、六十人 (fifty-sixty) forms are number RANGES using 、, NOT headings.
- The (1)-(19) rebuttal points at L107-L128 are enumerated LIST items rendered as ordinary
  paragraphs per parity, NOT section headings; the `：`-ended quote/list lead-ins and the closed
  `。)` parentheticals are DELIBERATE separate `<p>` and are NOT merged (incl. L99, which ends on a
  trailing "(3)" marker after a terminal 。 with a new 「-quote at L100 following).

### Checks
- verify_unit ch27: **parity 133/133, numbers 0 unresolved, anchors 6 ok.**
- check_align ch27: 133 source / 133 translation, **median ratio 4.82 en/han** (alignment OK, no
  pair strays >2.2x; a touch below the document-heaviest chapters — ch27 is argument + two
  reproduced news items + one forged letter, less pure directive-text than ch24-ch26).
- check_structure: parity 133/133 OK; **ALL STRUCTURAL CHECKS PASS**; anchors 259 notes, 0 unresolved.
- check_content: ch27 **105 name occurrences, all in the paired paragraph (0 DISPLACED).** The one
  transient displacement caught in drafting (para 111: source 制裁(张啸林) had Zhang Xiaolin in a
  parenthetical the English first dropped) was FIXED by carrying "(of Zhang Xiaolin)". Pre-existing
  artifacts unchanged: ch08 Shunde ×3, ch13 ×9, ch09 "Jize County" ×1, ch26 武汉卿/劳勃生路 ×2.
- qc_entities on the reconstructed bilingual: **0 misses** (census: 林怀部 ×52, 张啸林 ×46, 制裁 ×18,
  赵圣 ×13, 杜月笙 ×9, 虹口 ×3, 军统 ×3, 吉震苍 ×3, 傅筱庵 ×3, 黄金荣 ×2).
- check_register --ref: **within tolerance**; shall 0% (this chapter carries no quoted directives —
  it is Chen's own argument plus two news reports and the forged letter, so the narrating "shall"
  simply does not arise here; NOT a de-formalization), em-dash 11.4/1k, contr 0.8/1k, sent med 28.
- Tail verified against source (L136-137, the puppet regime's Central Reserve Bank / Special
  District Court offensive and the bloody reprisal) — faithful, no fabrication.

### Notes (6 new; 253 → 259 cumulative)
Most of the chapter's furniture is already covered and was NOT re-noted (see ledger below). New:
1. **the August Thirteenth Incident** — the 13 Aug 1937 outbreak of the Battle of Shanghai.
2. **French Municipal Council** — untangles the two councils: 工部局 = Shanghai Municipal Council
   (Settlement); 公董局 = the French Concession's Conseil (here "French Municipal Council"); the
   paper's 公部局 was an error. Zhang sat on the French body.
3. **the Reformed Government** (维新政府, Liang Hongzhi's 1938 Nanjing puppet regime; Chen Qun among
   its officials; folded into Wang Jingwei's regime in 1940).
4. **there are eighteen points** — the lead-in says 18 but Chen numbers (1)-(19) and closes with
   "these nineteen points"; the 18 is a slip for 19, faithfully preserved.
5. **among the Japanese commanders** — the 长奇/长崎 homophone: no Japanese surname reads Changqi
   (长奇), but 长崎 (same Mandarin sound, read Nagasaki) is real; a ground for Chen calling the
   letter a forgery. (A "texture lost in translation" note.)
6. **Zhou Fohai the prime mover** — Zhou Fohai + the 中央储备银行 Central Reserve Bank currency war
   (Jan 1941) + the 特区法院 Special District Court seizure.

### Glossary (2 net new rows, BY HAND via add_ch27_glossary.py; each key asserted in data/zh)
- 赵圣 **Zhao Sheng** (working name of the Second Action Brigade commander; real name 吉震苍 Ji
  Zhencang already keyed — two names, one man, each renders its own way; "第二队赵圣才说…" is
  Zhao Sheng + adverb 才, not a longer name).
- 黄金荣 **Huang Jinrong** (the third Green-Gang tycoon, beside Du Yuesheng and Zhang Xiaolin).
- Rendered INLINE, NOT keyed: 东郭牙 Dongguo Ya (pen name), 裴可权 Pei Kequan (contributor), 马龙
  Maron (French inspector), 柳乃夫 Liu Naifu, 阿四 Ah Si (driver, in the 沪上往事 excerpt), 朱升
  Zhu Sheng (Fu Xiao'an's cook-assassin, whose act is NOTED ch04), the second victim named three
  ways 吴金桂/吴建臣/吴鸿 (the source itself flags the discrepancy). Periodicals (新申报 Xin Shen Bao,
  大公报 Ta Kung Pao, 大成 Dacheng) and books (上海租界问题, 沪上往事) inline/footnote, not keys.

### NOT re-noted (already covered; first-appearance discipline)
Zhang Xiaolin (ch04), Fu Xiao'an + the cook-assassination (ch04 note already names it), the Green
Gang + its generation-name ranks 通/悟/大 (ch04 / ch09), Du Yuesheng (ch17), the concessions
(ch04), fabi (ch21), No.76 / 特工总部 / 李士群 (ch04 / ch17), 忠义救国军 the Loyal and Patriotic Army
(ch21), the 孤岛 Solitary Island (ch26), the Marco Polo Bridge Incident (ch13), the Xin Shen Bao
(ch20), Wan Molin (inline, B15/B16 shelf).

### Digitization glitches (rendered to plain sense; NOT footnoted unless real reading uncertainty)
- **L69 迷样 → 谜样** ("a figure of mystery"; 迷 for 谜).
- **L76 dittography** 「提出办法提出报告」 (提出 doubled) — rendered once ("report that an inside line
  had been laid").
- **L89 被补 → 被捕** ("arrested"; 补 for 捕).
- **L113 「u 时政府已得情报」** — the `u ` is a mis-rendered opening 「; rendered as an opening quote.
- **L60 演示文稿** — a software-conversion artifact (the modern Office term for "slideshow") standing
  where the source meant a clipping/transcript of the 大公报; rendered "the transcript of the Ta
  Kung Pao".
- **L103 出狱来才之慈母** — garbled (stray 才; 出狱[以]来…[年老]之慈母); rendered to sense "my aged mother".
- **L131 保留？变质的存在** — stray ？ for a dropped char; rendered "persist, in some altered form".
- **L136 李士？ / ？收 / ？存** → 李士群 (？ for 群) / 接收 (？ for 接) / 现存 (？ for 现).
- **L137 搏？ → 搏斗** ("a struggle"; ？ for 斗).
All carried to plain sense; none footnoted (mechanical, no reading uncertainty).

### In-text discrepancies preserved (faithful, discussed by the author himself; not glitches)
- 林怀部 vs 林怀步 (Zhao Sheng's report's homophone slip) and 林怀郭 vs 林怀部 (the forged letter's 郭
  for 部) — the author dwells on both; carried and discussed in the English.
- Zhang's age given as 68 (Xin Shen Bao) / 64 (Ta Kung Pao) / 64-or-65 (by the Dacheng birthday) —
  all carried.
- The second victim named 吴金桂 / 吴建臣 / 吴鸿 with three different offices — all carried; the
  author's own point (rebuttal 16).

### data/noise.txt — B21 block appended (each entry commented)
Date-names 八一三 (813, 13 Aug 1937) and 八一四 (814, the day of the killing); elided 十数 (ten-odd,
"a dozen or more"); driver's name 阿四 (Ah Si). Two REAL values fixed in the English rather than
noised (rule 4): 一时四十分 → "at forty minutes past one" (carries 40); 前两年 → "Two years or so
ago" (carries 2). All other real quantities CARRIED as digits/words (the 20-yuan wage vs the
District's 40; the 10,000-yuan reward; the 15-year sentence and 5-plus years served; the eight
action brigades; the twenty-second generation; the (1)-(19) rebuttal numbering; the 1842/1848/
1849/1864 concession-founding dates; the fifty-or-sixty-man Brigade strength).

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — ch27 spec added (drop=2; 2 severed-`<p>` merges 13/14 + 41/42; 3
  enumerated 一、二、三 headings: 1 standalone L3 + 2 tail-glued L64/L94, the latter ending in `」`).
- `scripts/add_ch27_glossary.py` — 2 new rows BY HAND (赵圣, 黄金荣; each key asserted in data/zh/ch27.txt).
- `scripts/make_ch27_apparatus.py` — the 6 ch27 notes (every non-ASCII glyph asserted present in
  data/zh/ch27.txt before NCR conversion).
- `data/noise.txt` — B21 block (see above).
- `notes.json` — 6 notes appended via apparatus_merge.py.

## Batch B22 (ch28) — 第九章 声威大震血浪腥风 "Chapter 9. Fearsome Renown, Waves of Blood"

The height-of-renown-and-blood chapter, continuing ch27's tail (特区法院 / 中央储备银行 / 血腥报复).
Three sections: (1) 一个特务工作者的心态与感受, Chen's reflections on killing, war, and the burden of
action work (the self-preface tallies; Dai's "非大流血不足以寒敌胆" telegram; the Cao Song poem; his
own errors of conscience — Liu Shaorang, the Zhang Xiaolin son encounter, the Yu Yefeng talk with
Sheng Liyue); (2) 铲除巨奸寒敌胆树立声威, the Fu Xiao'an / Zhu Sheng axe-killing in full (the "打通",
the 50,000-yuan reward, the reproduced Chongqing Ta Kung Pao report, the Japanese spokesman
Mabuchi's 新申报 statement, the Zhou Fohai diary on the mayoral succession, Dai's 70,000 award);
(3) 谁来清偿这笔寃孽债, the puppet institutional offensive — the two reproduced court-retrocession
agreements (公共租界 1930, 法租界 1931), the Zhou Fohai diary on the court "takeover", the killing of
the Frenchman Duluo (公董局政务督办), the Central Reserve Bank sabotage cases, and the No. 76 bloody
reprisal (the Bank of China machine-gunning), closing on Chen's own capture.

### Structure (confirmed p-by-p against the source XHTML)
- Source `Text/index_split_000_0027.xhtml` parses to **1 `<h2>` + 224 `<p>`**, NO `<h1>`, NO `<br/>`,
  NO `<img>`, NO `[\d+]` note markers. **drop=2** (running header 英雄无名-陈恭澍 + `<h2>` title).
- Byte-exact p-by-p diff: the 224 body lines map 1:1 to the 224 `<p>`, **zero mismatches**.
- **THREE enumerated 一、二、三 SECTION headings, all STANDALONE** (their own `<p>`, whole line =
  heading; unlike ch27's two tail-glued): L3 一、一个特务工作者的心态与感受; L49 二、铲除巨奸寒敌胆树立声威;
  L129 三、谁来清偿这笔寃孽债. Emitted as `### `.
- **FOUR severed-`<p>` merges** (first ends non-terminal, class merged since ch06): L80/L81
  (照我们的|经验), L135/L136 (订有协议的——|「上海公共租界特区法院协议」…, a trailing em-dash introducing
  the named agreement; source glitch "——-" ASCII hyphen after em-dash), L157/L158 (法院|事),
  L214/L215 (什么|事？). data/zh: 217 body lines (224 − 4 merges − 3 headings-as-`###` counted apart).
- **INNER enumerated 一、二、三 DOCUMENT-CLAUSE lists (NOT headings, kept as ordinary body lines per
  parity):** the two reproduced court agreements — 公共租界 (L137-139: clauses 一/二/三 under L136's
  lead-in) and 法租界 (L143-145: clauses 一/二/三、四 under L142's lead-in). Rendered as ordinary
  paragraphs (like ch27's (1)-(19) list). L222 ends non-terminal 事 but is a dropped-stop glitch of a
  complete sentence (那是他们的事[。]), NOT a merge; L223 opens 不过、a distinct closing paragraph.

### Checks (all green for ch28; pre-existing artifacts unchanged)
- clean_batch.py: **217 body paragraphs + 3 sub-headings, source conserved OK.**
- verify_unit.py ch28: **parity 217=217; numbers 217 pairs, 0 unresolved; anchors 0 ok.**
- check_align.py ch28: **217/217, median ratio 5.09 en/han, no pair strays >2.2x** (document-heavy;
  cf. ch24 5.33 / ch25 4.97 / ch26 4.98 / ch27 4.82).
- check_structure.py: **ALL STRUCTURAL CHECKS PASS** (parity 217=217; 267 anchors 0 unresolved).
- check_content.py: **ch28 172 name occurrences, 0 displaced** ("all in the paired paragraph").
  Only the documented PRE-EXISTING artifacts remain (ch08 ×3, ch09 ×1, ch13 ×9, ch26 ×2). One
  ch28 displacement was FIXED by aligning to the keyed term 东亚新秩序 "New Order in East Asia"
  (had been rendered lowercase "a new order in East Asia" in the Mabuchi statement, twice).
- qc_entities.py (reconstructed bilingual, 217 pairs): **0 misses** (周佛海 x47, 朱升 x36, 傅筱庵 x26,
  制裁 x23, 李士群 x12).
- check_register.py --ref: **within tolerance**; "shall" 22% is the DELIBERATE document register (the
  two reproduced court agreements' "shall" clauses + Dai's directive "there shall be a heavy reward").
- check_apparatus.py: 0 failures / 0 warnings. qa_epub: PASS (28/43 chapters, 267 notes all resolve).
  epubcheck 5.1.0: **0 fatals / 0 errors / 0 warnings / 0 infos.**

### Settled renderings REUSED (Part-Three consistent)
傅筱庵 Fu Xiao'an, 张啸林 Zhang Xiaolin, 林怀部 Lin Huaibu, 杜月笙 Du Yuesheng (杜先生 "Mr. Du"),
周佛海 Zhou Fohai, 李士群 Li Shiqun (士群 "Shiqun" in the diary), 陈公博 Chen Gongbo (公博 "Gongbo"),
汪精卫 Wang Jingwei, 赵圣 Zhao Sheng, 陈默 Chen Mo, 齐庆斌 Qi Qingbin, 刘原深 Liu Yuanshen,
黄志远 Huang Zhiyuan, 孙大成 Sun Dacheng, 胡永荃 Hu Yongquan, 俞叶封/兪叶封 Yu Yefeng, 汪时璟 Wang
Shiying, 虞洽卿 Yu Qiaqing, 褚民谊 Chu Minyi, 苏锡文 Su Xiwen, 梅思平 Mei Siping; 会审公廨 the Mixed
Court; 特区法院 "Special District Court"; 中央储备银行 "Central Reserve Bank"; 第二行动大队 "Second
Action Brigade". Place-names in glossary PINYIN: 北平 Beiping, 天津 Tianjin, 虹口 Hongkou, 重庆
Chongqing (重庆大公报 "Chongqing Ta Kung Pao"), 汉口 Hankou, 河内 Hanoi. Attested roads inline:
爱多亚路 Avenue Edward VII, 南京路 Nanking Road, 马霍路 Mohawk Road, 外滩 the Bund; PINYIN for the
uncertain: 祥德路 Xiangde Road, 白赛仲路 Baisaizhong Road, 恺自迩路 Kaiziěr Road, 西爱咸斯路 Xi'aixiansi
Road. Republican years literal (二十二年 "twenty-second year", etc.; the checker +1911-escapes).

### New glossary rows (3 net new; BY HAND via add_ch28_glossary.py; every row a pinyin field)
- 朱升 **Zhu Sheng** (person) — the servant who axed Fu Xiao'an (11 Oct 1940); central to Section 2,
  ~36 occurrences. Rendered inline in ch27 (act NOTED ch04); KEYED here to enforce "Zhu Sheng"
  everywhere. Variants 朱生/朱升源 and the alias 陈中南 stay inline.
- 联合准备银行 **the Federal Reserve Bank** (org) — the North China puppet bank (Wang Shiying governor;
  Cheng Xigeng manager, sanctioned 1939); distinct from the Central Reserve Bank. NOTED.
- 会审公廨 **the Mixed Court** (org) — the concessions' pre-1930 joint tribunal the two agreements
  abolished, replaced by the Special District Courts. NOTED.
- Rendered INLINE, NOT keyed: 裴可权 Pei Kequan, 盛礼约 Sheng Liyue (/盛郁 Sheng Yu), 王晓籁 Wang
  Xiaolai, 张法尧 Zhang Fayao, 余祥琴 Yu Xiangqin, 杜洛 Duluo (the Frenchman), 柳汝祥 Liu Ruxiang,
  钱书城 Qian Shucheng; one-off Japanese officers (臼井宽三 Usui Kanzō, 马渊 Mabuchi, 前田 Maeda,
  谷荻 Yahagi, 樱井 Sakurai, 曾弥 Sone, 青木 Aoki, 西园寺 Saionji, 犬养 Inukai, 木村市大郎 Kimura
  Ichitarō, 结城 Yūki, 日高 Hidaka, 上田 Ueda); sanctioned staff (季明远 Ji Mingyuan, 张永纲 Zhang
  Yonggang, 厉鼎模 Li Dingmo) and operatives (叶东山 Ye Dongshan, 赵家鑫 Zhao Jiaxin, 何凤祥 He
  Fengxiang, 丁小宝 Ding Xiaobao, 董威 Dong Wei, 田杰林 Tian Jielin, 林镇城 Lin Zhencheng); 程锡庚
  Cheng Xigeng; 曹松 Cao Song (Tang poet); 杨秀琼 Yang Xiuqiong, 姚水娟 Yao Shuijuan; Fu's kin
  (宋有圭 Song Yougui, 品圭 Pingui) and companions (周文瑞/魏晋三/盛老三); 程/彭 Cheng/Peng, 杨惺华
  Yang Xinghua; the agreements' transliterated foreign signatories and 徐谟 Xu Mo / 吴昆吾 Wu Kunwu.
  Books/periodicals (上海租界问题, 新申报 Xin Shen Bao, 重庆大公报, 官场现形记) footnote/inline.

### Notes added (8; first-appearance-disciplined; cumulative 259 → 267)
- **by Cao Song** — the Tang poet Cao Song, his quatrain 己亥岁, and the line 一将功成万骨枯.
- **The Double Tenth** — 双十节, the ROC national day (Wuchang Uprising, 1911).
- **Great Way City Government** — 大道市政府, the first Japanese puppet Shanghai municipality (1937).
- **the Mixed Court** — 会审公廨, the pre-1930 concession tribunal the two agreements abolished.
- **concurrently governor of the** — 联合准备银行 the (North China) Federal Reserve Bank vs the Wang
  regime's 中央储备银行 Central Reserve Bank; Cheng Xigeng's 1939 assassination.
- **Yue opera** — 越剧 / 绍兴戏, the play 盘夫索夫, and its star 姚水娟 Yao Shuijuan.
- **drove the carriage for Yang Xiuqiong** — 杨秀琼 the swimming star; 褚民谊's carriage-driver jibe.
- **still but a scene from** — 官场现形记 "Officialdom Unmasked" (Li Baojia), the late-Qing satire.

### NOT re-noted (already covered; first-appearance discipline)
特区法院 / 中央储备银行 / 周佛海 (ch27), 维新政府 the Reformed Government (ch27), 工部局/公董局 the two
municipal councils (ch27), the 八一三 August Thirteenth Incident (ch27), Fu Xiao'an + the cook-
assassination (ch04), Zhang Xiaolin (ch04), Du Yuesheng (ch17), Yu Qiaqing (ch26), 制裁 sanction,
the concessions (ch04), No.76 / 特工总部 / 李士群 (ch04/ch17), fabi (ch21), the Kang Corps 抗团 (ch26),
忠义救国军 (ch21), the Marco Polo Bridge (ch13), the Xin Shen Bao (ch20), the Blue Shirt Society (ch08).

### Digitization glitches (rendered to plain sense; NOT footnoted unless real reading uncertainty)
- **L6 顷耳一听 → 倾耳** ("listened closely"; 顷 for 倾); **L6 一搂搬机 → 扳机** ("pulled the trigger"; 搬 for 扳).
- **L15 写到这褢 → 里/裡** ("writing to this point"; 褢 for 裡).
- **L39 兪家的专 → 事** ("the affairs of the Yu family"; 专 for 事).
- **L75 汉冶平股东联合会 → 汉冶萍** (the Hanyeping Company; 平 for 萍); rendered "the Hanyeping … Joint Association".
- **L116 陈公傅 → 陈公博** (Chen Gongbo; 傅 for 博) — a name glitch, rendered correctly.
- **L136 洋泾滨章程 → 洋泾浜** (the Yangjingbang Regulations; source prints 滨 for 浜, cf. ch25); rendered "the Yangjingbang Regulations".
- **L191 又项目由津去平 → 专程** ("made a special trip from Tianjin to Beiping"; 项目 for 专程).
- **L199 第七行功大队 → 第七行动大队** (the Seventh Action Brigade; 功 for 动).
- **L205 暗椿 → 暗桩** ("planted agents / hidden watchers"; 椿 for 桩, variant).
- **L208 武盘 → 武器** ("weapons"; 盘 for 器).
- **Dash glitches:** L60 第二天—– , L133 订有协议的——- , L207 血腥报复—- (extra ASCII hyphen after an em-dash) — rendered as clean em-dashes.
- **Source redactions (rendered as em-dash blanks / bracketed):** L75 前清XXX(字迹不清) → "held ——— (the characters are illegible)"; L77 妻X氏 → "the wife, née ——"; L187 十二月XX日 → "On the ——th of the twelfth month"; L162 予以XX → "whether we might —— the Frenchman Duluo" (Chen self-censoring 制裁). L93 招商局总理(？) — the source's own (?) uncertainty marker, kept as "(?)".
All carried to plain sense; none footnoted (mechanical, no reading uncertainty).

### In-text discrepancy preserved (faithful, not a glitch)
- The tally figures of Section 1 (一百余 traitors / 四十余 Japanese / 五十余 sabotage jobs / 两百余 own
  losses) are Chen's own preface figures, re-cited "by an incomplete count"; rendered "over a hundred /
  over forty / over fifty / over two hundred". The 余-approximate forms are noised as the checker flags.

### data/noise.txt — B22 block appended (each entry commented)
Idioms/name-elements: 正反两面 (both sides, for good and ill — the 两 not a count), 一二两部 (本书第一二两部
"parts one and two" — the run 一二两 mis-read as 122), 上万 (成千上万 "thousands upon thousands" — the
built-in 成千 clears the head, this the 上万 tail), 四明银行 (the Ningpo Commercial/Siming Bank — 四 a name
element), 宽三 (臼井宽三 Usui Kanzō — 三 a name element). REAL counts fixed in the English rather than
noised (rule 4): 三国同盟 → "three-Power alliance" (carries 3); 两方面 → "these two … the one side … the
other" (carries 2); 二人 → "the two, Qian Shucheng and Liu Ruxiang" (carries 2). All other real
quantities CARRIED as digits/words (the 50,000/70,000/20,000-yuan rewards; the 22-yuan wage; the 69/42
ages; the 13-year service; the 12 White Russian guards; the 10/14-article agreements; the 24-hour
delivery rule; the 3-year extendable term; the 1930/1931 agreement dates; the sixty-odd cases / one
every five days).

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — ch28 spec added (drop=2; 4 severed-`<p>` merges 80/81, 135/136, 157/158,
  214/215; 3 standalone enumerated 一、二、三 headings L3/L49/L129; the inner document-clause 一、二、三
  lists stay ordinary body lines).
- `scripts/add_ch28_glossary.py` — 3 new rows BY HAND (朱升; 联合准备银行; 会审公廨; each key asserted in
  data/zh/ch28.txt).
- `scripts/make_ch28_apparatus.py` — the 8 ch28 notes (every non-ASCII glyph asserted present in
  data/zh/ch28.txt before NCR conversion).
- `data/noise.txt` — B22 block (see above).
- `notes.json` — 8 notes appended via apparatus_merge.py (cumulative 267).

## Batch B23 (ch29) — 第十章 祸不单行 柱折梁摧(上) "Chapter 10. Troubles Never Come Singly; Pillars Snap, Beams Fall (Part 1)"

The disaster/collapse chapter, the (上) half of a two-part chapter (ch30 = the 下 half). Continues
ch28's tail (the early-1941 特工总部 + 上海日本宪兵队 crackdown and Chen's own capture). A two-voice
chapter: Chen's essayistic narration frames Liu Yuanshen's (刘原深) first-person memoir 沪滨三次历险实录.
Two enumerated 一、二 sections: (1) 是我误了他的锦绣前程 — Chen loses a son to pneumonia, then the bureau
summons Liu Yuanshen to the Chengdu Advanced Education Class; Chen persuades him to stay, and hands
him the acting command of the First Action Brigade as a two-month "temporary task" (the Changsha-fire
dispatch, the seventeen classmates and the nine martyred in Pudong, Dai Li's blanket-scolding and his
station farewell); (2) 人性理性交织下的特务活动 — Liu takes over the brigade, meets the three
sub-brigade leaders (Liu Quande / Xiang Qiangwei-Luo Chengjin / the turned Zhou Xiyuan), and is drawn
step by step into the Zhou Xiyuan / Zhu Min trap over the sanction of Xu Liqiu, breaking off on the
28 June meeting. Chen's closing narration recaps the two-year run and his own capture.

### Structure (confirmed p-by-p against the source XHTML)
- Source `Text/index_split_000_0028.xhtml` parses to **1 `<h2>` + 72 `<p>`**, NO `<h1>`, NO `<br/>`,
  NO `<img>`, NO `[\d+]` note markers. **drop=2** (running header 英雄无名-陈恭澍 + `<h2>` title).
- Byte-exact p-by-p diff: the 72 body lines map 1:1 to the 72 `<p>`, **zero mismatches**.
- **TWO enumerated 一、二 SECTION headings:** L3 一、是我误了他的锦绣前程 (STANDALONE, its own `<p>`);
  二、人性理性交织下的特务活动 TAIL-GLUED onto L33 after a terminal 。(…他怎么说我就怎么答应了。二、…),
  split off via `glued`.
- **ONE severed-`<p>` merge** (first ends non-terminal, class merged since ch06): L65/L66
  (…所有的问题必可负责代为 | 解决。).
- NOT merged (deliberate separate lines): the ：-ended memoir/document lead-ins (L32 …原文如下：,
  L40 …也不能无疑：), and L19 (以下这一段…细说他这一段不平凡的历程) — a complete lead-in sentence whose
  final 。 the source drops (a glitch, rendered with a period), NOT a split.
- clean_batch.py ch29: **70 body paragraphs, 2 sub-headings, source conserved OK.**

### Checks (all green)
- **verify_unit.py ch29:** parity 70=70; numbers 0 unresolved (after the B23 noise block); anchors 0.
- **check_align.py ch29:** 70/70, median ratio **4.97 en/han** (dialogue/document-heavy; in range).
- **check_structure.py:** parity 70=70 OK; anchors 276 notes, 0 unresolved; headings OK.
- **check_content.py:** ch29 **27 name occurrences, all in the paired paragraph** (0 displaced). The
  only DISPLACED remain the documented pre-existing artifacts (ch08 ×3, ch09 ×1, ch13 ×9, ch26 ×2).
- **qc_entities.py** (reconstructed bilingual): census 周西垣 ×27, 朱敏 ×26, 制裁 ×14, 刘全德/万里浪/
  许力求 ×9 …; **0 misses.**
- **check_register.py --ref:** within tolerance; "shall" 56% (deliberate — the chapter carries many
  quoted directives/telegrams/dialogue; cf. B19 67%, B20 83%). Contractions 0.0, em-dash 6.8/1k.
- **check_apparatus.py:** 0 failures, 0 warnings.
- **qa_epub.py:** PASS (43 documents, 4300 paragraphs, 276 references/bodies/backlinks).
- **epubcheck 5.1.0:** 0 fatals / 0 errors / 0 warnings / 0 infos.
- **EPUB now 29/43 chapters, 276 notes.**

### Glossary (7 net-new keyed rows, BY HAND via scripts/add_ch29_glossary.py; each key asserted in data/zh)
周西垣 Zhou Xiyuan (the turned third-sub-brigade leader), 冯贤 Feng Xian (Zhou's cover name — renders
its OWN way, NOT "Zhou Xiyuan", per the source's deliberate use), 朱敏 Zhu Min (Zhou's secretary /
informant), 刘全德 Liu Quande (first-sub-brigade leader, ex-Ruijin "Little Red Devil"), 相强伟 Xiang
Qiangwei (second-sub-brigade leader), 骆成金 Luo Chengjin (Xiang's deputy; tortured on the tiger bench),
许力求 Xu Liqiu (South China Evening News director, the bait target). All `provisional`. Rendered INLINE
(NOT keyed): 祝慎之 Zhu Shenzhi (pediatrician); the classmate roster (唐与元/张学礼/张毓檀/吴菊生/杨继志/
张维贤; 狄玺庭/李玉顺/刘士愚/丁履敬); bureau personnel 李肖白/周康; Wuhan-internship staff 刘培初/张树勋/
陈仙洲 (董威 inline from B22); maidservants 赵妈/彩爱. 南华晚报 is a footnote, not a key.

### Notes added (9; first-appearance-disciplined; cumulative 267 → 276)
- **the great Changsha fire** — 长沙大火 (12 Nov 1938), the scorched-earth Wenxi Fire.
- **the Linli class** — the Juntong's 1938 Linli (临沣 in source, for 临澧) special training class;
  Chiang principal (校长), Dai Li class director (班主任).
- **the Advanced Education Class** — 高等教育班 of the 中央军校 at Chengdu; the plot's hinge.
- **Xiaozhilong** — 消治龙, an early sulfonamide (sulfa) antibacterial.
- **Little Red Devil** — 红小鬼, CCP boy soldiers; 瑞金 the Jiangxi Soviet base.
- **tiger bench** — 老虎凳, the standard No. 76 torture.
- **South China Evening News** — 南华晚报, Wang Jingwei's Hong Kong organ (Lin Bosheng, 1939).
- **dead before the campaign was won** — 出师未捷身先死, Du Fu on Zhuge Liang.
- **State Express 555** — 茄力克 Garrick / 三五 State Express 555, premium tinned cigarettes.

### NOT re-noted (already covered; first-appearance discipline)
No.76 / 特工总部 (ch04/ch17), 制裁 sanction, 忠义救国军 the Loyal and Patriotic Army (ch21), Dai Li's
1946 air-crash death (ch02/ch25), Whampoa (early), the concessions (ch04), Zhang Xiaolin / Fu Xiao'an
(ch04/ch28), Wang Jingwei / the Wang puppets (throughout), 军统局 the Juntong Bureau (ch04).

### Digitization glitches (rendered to plain sense; NOT footnoted — mechanical, no reading uncertainty)
- **L19 dropped final 。** on the memoir lead-in (…不平凡的历程) — rendered with a period.
- **L32 移交xx同志** — a redacted name (lowercase xx) → rendered "Comrade XX".
- **L32 潇酒 → 潇洒** ("dashing"; 酒 for 洒).
- **L41 局惟有听命行事 → 周** (Zhou had no course but to obey; 局 for 周) — rendered "Zhou".
- **L49 霞飞坊 X 号** — a redacted lane number (× redaction) → rendered "No. —" (em-dash blank).
- **L54 妳 → 你** (Zhu Min is male; the source's feminine 妳) — rendered "you".
- **L54 怎怎么 → 怎么** (dittography); **L54 索兴 → 索性** ("straight to the point"); **L54 dropped
  closing 」** at the paragraph end — quote closed in the English.
- **L62 三○一室 → Room 301** (○ = U+25CB for 0; the numeric checker mis-reads it — noised the
  glyph-string, real value 301 carried).
- **L70 当？ → 当即** ("readily"; stray ？); **L70 幺么小丑** ("petty clown"; 幺么/幺麽 variant).
- **L72 了？实身份 → 真实身份** ("true identity"; stray ？).

### data/noise.txt — B23 block appended (each entry commented)
Idioms/counters/name-elements: 两相配合 (acting in concert — 两 not 2), 两难 (dilemma), 五旬 (about
fifty — decade form; fifty carried in the English), 八仙桥 (Baxianqiao — 八 a name element), 五福楼
(the Wufu Lou restaurant — 五 a name element), 送给了万 / 万某 / 被万 (bare surname 万 = Wan Lilang, not
10000), 万一 (idiom "if by any chance"), 三○一 (Room 301 address artifact, ○ mis-read). Counters carried
by naming (like B22's 二位): 周、朱两人, 陈、齐两位, 朱、周二人. All REAL quantities CARRIED as digits/words
(the 4-dollar stake / 2,000-odd winnings; the seventeen classmates; the nine martyred; the six/ten/
eight-man sub-brigades; the 3 revolvers / 2 Mausers / 1 Browning; the 2 revolvers + 60 rounds; the
sixty-odd cases / one every five days; the ten-month tally; the two-month task; the 13th/15th/22nd/
24th/25th/28th/29th dates; ages 24/32/29/23; the 17 March 1946 air crash; ROC years 27/28/30/35).

### Tooling added / changed (do NOT revert)
- `scripts/clean_batch.py` — ch29 spec added (drop=2; 1 severed-`<p>` merge 65/66; standalone heading
  L3; tail-glued heading on L33 after a terminal 。).
- `scripts/add_ch29_glossary.py` — 7 new rows BY HAND (each key asserted in data/zh/ch29.txt).
- `scripts/make_ch29_apparatus.py` — the 9 ch29 notes (every non-ASCII glyph asserted present in
  data/zh/ch29.txt before NCR conversion; correct forms 临澧/文夕/蜀相 NOT typed since absent from the
  glitchy/abridged source — described in English/pinyin instead).
- `data/noise.txt` — B23 block (see above).
- `notes.json` — 9 notes appended via apparatus_merge.py (cumulative 276).
