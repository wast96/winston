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

---

## Batch B24 — ch30 (第十章 祸不单行 柱折梁摧(下)) + ch31 (写在「英雄无名」第三部专书出版前)

**COMPLETES PART THREE.** ch30 = the (下) half of Chapter Ten (ch29 = 上): the trap sprung and the
two captures. ch31 = the Part-Three closing ERRATA note. EPUB now **31/43 chapters, 284 notes**.

### Structure (byte-exact p-by-p, both units)
- **ch30:** source XHTML `index_split_000_0029.xhtml` = 1 `<h2>` + 110 `<p>`, NO `<h1>`/`<br/>`/
  `<img>`/`[\d+]`. drop=2 (running header + `<h2>`). 110 `<p>` matched the txt body 1:1, zero
  mismatches. THREE enumerated SECTION headings: **三、仁者之心终为幺么所乘** (standalone, p#0);
  **四、霎时间发生了巨大变故** (tail-glued on p#19 after a terminal 」); **五、保持住应有的人格与尊严**
  (tail-glued on p#73 after a terminal ！). ONE severed-`<p>` merge (source L91/L92: …尽量的 | 多了解).
  NOT merged (deliberate separate `<p>`): the ：-ended dialogue lead-in p#70 (…他追问：) and the
  memoir lead-in p#4 (…其文如下：); the inline 第一、/第二、 enumerations inside single `<p>` (p#10,
  p#106) and the 三、四尺 number-range (p#67) kept as body lines per parity. **108 body paragraphs +
  3 sub-headings.** Two-voice chapter: sections 三 = Liu Yuanshen's memoir, sections 四/五 = Chen's
  own narration of his arrest (per ch31 erratum #8; the "我" who "led the Shanghai District" / is the
  区长 is Chen). Voice-switch footnoted at section 4.
- **ch31:** source `index_split_000_0030.xhtml` = 1 `<h1>` + 14 `<p>`, NO `<h2>`/`<br/>`/`<img>`/
  `[\d+]`. drop=2 (running header + `<h1>` front-matter title; first body line 抗战期间…). 14 `<p>`
  matched 1:1. The enumerated 一、–八、 items (p#5–p#13) are an ERRATA/addendum LIST (each cites an
  earlier chapter by 页/page number), kept as ordinary DOCUMENT-CLAUSE body lines per parity — NOT
  section headings, none standalone/glued. NO merges. **14 body paragraphs.** ch30/ch31 carry NO
  images (confirmed).

### Checks (all green)
- clean_batch source-conservation OK (both). verify_unit ch30/ch31: parity OK, **numbers 0 unresolved**,
  anchors OK. check_align ch30 108/108 median **4.64**; ch31 14/14 median **5.48** (document-heavy note).
- check_structure: parity 108/108, 14/14 OK; anchors 284 notes, 0 unresolved; headings OK.
- check_content: ch30 **all in the paired paragraph** (1 fixed: the sign "HONGKOU" → keyed "Hongkou");
  ch31 **all in the paired paragraph**. (The pre-existing artifacts ch08×3 / ch13×9 / ch09×1 / ch26×2
  persist, not regressions.)
- qc_entities: ch30 **0 misses** (top: 万里浪 x10, 林焕芝 x7, 褚亚鹏 x6, 朱敏 x5, 重庆 x5, 周西垣 x4);
  ch31 **0 misses**.
- check_register --ref: ch30 within tolerance (shall 9%, 108 paras); ch31 within tolerance (shall 0%,
  short note). check_apparatus 0/0. qa_epub **PASS** (284 refs/bodies/backlinks). **epubcheck 0/0/0/0.**
- Tails verified against source: ch30 closes on Jiang Shaomo (Cilie) taking over the Shanghai Reserve
  District and fighting on to victory; ch31 closes on erratum #8 (the two-voice clarification). Nothing
  dropped.

### Notes added (8; cumulative 284)
- **ch30 (5):** the pig-cage van (猪笼车, the barred police wagon); Malone (马隆/马龙 — the French
  criminal-section chief and secret Shanghai District contact, spelled two ways by Liu vs Chen, one
  officer); the Double Ninth (重阳, 28 Oct 1941); the section-4 voice switch (Liu's memoir → Chen's own
  narration, per ch31 #8); Biluochun tea (碧螺春, the card betraying Zhu Min).
- **ch31 (3):** the page-citation apparatus (the parenthetical 页 numbers are the author's, to the
  original edition, not this one); the opera bill (红拂传 / 小商河 / Yang Zaixing 杨再兴 / Yue Fei 岳飞);
  reform through labour (劳动改造, laogai — where Lin Huaibu was traced).
- **NOT re-noted (first-appearance ledger):** No. 76 / 特工总部 (ch04/ch17), 制裁 (sanction), the tiger
  bench 老虎凳 (ch29), the Blue Shirt Society 蓝衣社 (ch08), the "three-stripe head" 三道头 police
  sergeant (explained in the quoted passage in ch24), 忠义救国军 the Loyal and Patriotic Army (ch21),
  抗团 the Kang Corps (ch20), the Jessfield Road / No. 76 address, the war of resistance / fallen zone.

### Glossary — 3 net new keyed rows (scripts/add_ch30_glossary.py; each key asserted in data/zh)
褚亚鹏 Chu Yapeng (ex-Beiping courier, the Bubbling Well Road electrical-shop station; paraded to ID
Chen but did not); 林焕芝 Lin Huanzhi (Cantonese action-section chief at No. 76, ex-Fourth Team; brother
林镇城 Lin Zhencheng inline); 姜绍谟 Jiang Shaomo (courtesy Cilie; Shanghai Reserve/Second District chief
who carried on after Chen's capture). Rendered INLINE (one-off): 仇淑英 Qiu Shuying, 陈贤荣/程远 Chen
Xianrong/Cheng Yuan, 孙国昌 Sun Guochang, 秦尔同/张湘南/顾汉卿 (radio chiefs), 桂涤非 Gui Difei, 马隆/马龙
Malone, 克莱德 Clyde, 胡永安 Hu Yong'an, 阿平 A-ping; in ch31 刘仲康 Liu Zhongkang, 李洪春 Li Hongchun,
梁慧超 Liang Huichao, 杨再兴 Yang Zaixing, 岳飞 Yue Fei, 随波 Suibo, 徐展 Xu Zhan. 钱新民 Qian Xinmin,
蒋安华 Jiang Anhua were already keyed.

### Digitization glitches (rendered to plain sense; none footnoted as reading uncertainty — mechanical)
- **ch30:** 小与会 → 小雨会 (与/雨); 一˙ / ˙足而观 / 来˙汤面 (stray ˙ glyphs); 这里是租借 → 租界 (借/界);
  什庆时候 → 什么 (庆/么); 微笑首 → 微笑颔首 (dropped char); 拼拼揍揍 → 拼拼凑凑 (揍/凑); 看「稀奇哈」
  (stray 哈); 三楼旧光依，灯 → 三楼的灯光依旧 (scrambled — rendered "the lamplight as before"); 左石 →
  左右 (石/右); 突然间蒋安华说 → 突然问 (间/问); 马夫前蹄 → 马失前蹄 (夫/失); 不屑几分钟 → 不消几分钟
  (屑/消); 使搬 → 速搬? (uncertain final instruction, rendered "shift your quarters"). Redactions:
  内交站报告 "我是xx" and X嫂 rendered as em-dash blanks.
- **ch31:** 耿某会被 → 曾被 (会/曾); 余廷智 → 余延智 (廷/延; keyed form Yu Yanzhi, noted); 将有以补充 →
  将有所补充; 上海第 X 农场 (× redaction → "No. ——").

### data/noise.txt — B24 addition
- **退一万步** (idiom "even taking ten thousand steps back / at the very worst"; the 一万 is rhetorical,
  not a count). All REAL quantities CARRIED as digits/words: the dates (28 Jun 1941; 29/30 Oct 1941 =
  ROC 30; 27 Dec 1939 = ROC 28); clock times (9:00 / 9:40 / 2:30 / 8:27 / past 11 / gone 1 / 5:10 /
  past 9); counts (50 yards, 2-inch photo, 2 revolvers, 15 min, 5 feet, 500 vs 85 yuan, 2 zhang,
  ~500 out / ~1000 in, a dozen+ premises, age 25, ten-or-so parties, 2 paces, 2 men, a thousand strong,
  9 steps, 7–8 steps, two-short-one-long); the ch31 errata page numbers (65/84/124/87/129/85/89 — the
  author's, to the original edition).

### Tooling added (do NOT revert)
- `scripts/clean_batch.py` — ch30 spec (drop=2; merge 91/92; standalone L3; glued L22 四, L76 五) and
  ch31 spec (drop=2; errata list as body lines, no headings/merges).
- `scripts/add_ch30_glossary.py` — 3 new rows BY HAND (each key asserted in data/zh/ch30.txt|ch31.txt).
- `scripts/make_b24_apparatus.py` — the 8 B24 notes (every non-ASCII glyph asserted present in that
  unit's data/zh before NCR conversion). `notes.json` — 8 notes appended via apparatus_merge.py
  (cumulative 284).

## Batch B25 — ch32 (自序) — "Author's Preface"

**OPENS PART FOUR** ("Pacification of the Beiping-Tianjin Region" / 平津地区绥靖戡乱). ch32 = the
Part-Four self-preface (parallel to ch10/ch20). The 1946-49 civil-war material begins: after the
Japanese surrender Chen commands the First Brigade of the Ministry of National Defense Pacification
Corps in the Nationalist-Communist fighting around Beiping and Tianjin. EPUB now **32/43 chapters,
294 notes**. The Nationalist idiom is preserved, not softened (共匪 "the Communist bandits", 绥靖戡乱
"pacification and the suppression of rebellion"), framed by a footnote.

### Structure (byte-exact p-by-p)
- source XHTML `index_split_000_0031.xhtml` = 1 `<h1>` (平津地区绥靖戡乱, the Part-Four super-title,
  handled by book.json `part`) + 1 `<h3>` (自序) + 35 `<p>`, NO `<h2>`/`<br/>`/`<img>`/`[\d+]`.
  **drop=3** (running header + `<h1>` + `<h3>`; the ch10/ch20 part-preface pattern). First body line
  after drop=3 = 缅怀一辈小兄弟们… (confirmed). The 35 `<p>` (L4-L38) matched the txt body 1:1, zero
  mismatches; **every `<p>` ends terminal → NO severed-`<p>` merges**. NO section headings inside: the
  two enumerated-LOOKING line starts (L22 五个指挥室分布在…, L37 三十八年一月杪…) are BODY sentences
  opening on a numeral, kept as body lines per parity. **35 body paragraphs, 0 sub-headings.** No images.
  clean_batch.py ch32 spec added (drop=3; no merges/glued/standalone); source-conservation OK.

### Checks (all green)
- verify_unit ch32: parity OK, **numbers 0 unresolved**, anchors **10 ok**. check_align 35/35 median
  **5.57 en/han** (a preface runs denser, cf. ch20/ch31; alignment OK, no pair strays >2.2x).
- check_structure: parity 35/35 OK; anchors **294 notes, 0 unresolved**; headings OK. ALL PASS.
- check_content: ch32 **28 name occurrences, all in the paired paragraph** (0 displaced). Whole-book
  rescan with the 10 new keys shows only the documented pre-existing artifacts (ch08×3 / ch09×1 /
  ch13×9 / ch26×2 = 武汉卿/劳勃生路 keyed-substring false positives) — no new displacement.
- qc_entities (reconstructed bilingual): **0 misses**; census top 北平×16, 绥靖×13, 绥靖总队×9,
  郑介民×5, 励志计划×3, 刘培初×3.
- check_register vs reference/B01_frozen.md: **within tolerance** (contr 0.0/1k = 1.00x ref; shall 0%;
  em-dash 8.7/1k vs 8.3; little dialogue). The narrating "shall" is deliberate; a preface runs denser.
- Tail (P33-P35, source L36-L38) verified against the source: the Temple-of-Agriculture airstrip flight,
  the second Beiping party's flight to Qingdao at end-Jan 1949, the two refused resignations + autumn-1949
  mainland work — all faithful.
- qa_epub **PASS** (57 files, 50 documents, 294 refs/bodies/backlinks). epubcheck 5.1.0 **0/0/0/0**.

### Footnotes — 10 new (per the reader model; Part Four opens the civil-war furniture)
1. the Nationalist civil-war idiom (共匪/绥靖/戡乱, 1946-49; War of Liberation in the other historiography;
   preserved, not softened) — anchor "the war to suppress the rebellion" (P2).
2. the "Fifth Part" discrepancy (Chen's own count reaches the fifth part though Shanghai was "the Third
   Part" and this edition presents four books; noted per rule 4) — "the Fifth Part" (P3).
3. the Marshall Mission / Committee of Three / Military Mediation Executive Headquarters (1946) — "Marshall".
4. the Lizhi Plan (励志 "to steel the will"; the Lizhi Training Class at the Central Training Corps) — "Lizhi Plan".
5. the Jiangxi bandit-suppression (剿匪 Encirclement Campaigns; the 别働总队 special-detachment precedent) —
   "the Jiangxi bandit-suppression".
6. the Youth Army (青年军, "a hundred thousand youths, a hundred thousand soldiers") — "Youth Army".
7. the five Republican rail lines (北宁/津浦/平汉/平古/平绥, named descriptively) — "Beiping-Liaoning line".
8. Fu Zuoyi (the negotiated surrender of Beiping, Jan 1949, backdrop of the preface) — "Fu Zuoyi".
9. Fenghua (Chiang's native place; he had just retired as President, Jan 1949; Li Zongren acting) — "Fenghua".
10. the Temple of Agriculture (先农坛, imperial plowing altar → makeshift airstrip in the siege) — "Temple of Agriculture".

### Glossary — 10 net new keyed rows (scripts/add_ch32_glossary.py; each key asserted in data/zh/ch32.txt)
People: 叶剑英 Ye Jianying (Communist rep on the Executive HQ), 刘培初 Liu Peichu (Pacification Corps
Commander; memoir author; = the Wuhan practice-corps leader of ch29), 李宗仁 Li Zongren (Beiping Field
HQ director; 1949 acting president), 傅作义 Fu Zuoyi (North China Bandit Suppression C-in-C; surrendered
Beiping), 计兆祥 Ji Zhaoxiang (stay-behind wireless operator, martyr). Organizations: 绥靖总队 the
Pacification Corps, 军事调处执行部 the Military Mediation Executive Headquarters, 军事三人小组 the Committee
of Three, 励志训练班 the Lizhi Training Class. Terms: 励志计划 the Lizhi Plan. Rendered INLINE (one-off
Western/officials, standard provinces, common-noun term): 马歇尔 Marshall, 罗柏森 Colonel Robertson, 侯腾
Hou Teng, 徐启明 Xu Qiming, 张家铨 Zhang Jiaquan, 史泓 Shi Hong, 雷处长 Director Lei; 河北 Hebei, 绥远
Suiyuan, 山东 Shandong, 河南 Henan, 山西 Shanxi; 戡乱 "suppression of rebellion" (already so rendered ch04).
NOT keyed 河北 (would false-flag the keyed 河北大经路 → "Dajing Road") / 绥远 (standard, appears ch08/09/22/25).

### Settled Part-Four renderings (reuse)
总队 "Corps" / 总队长 "Corps Commander"; 大队 "brigade" / 大队长 "brigade commander" (reuse B24); 分队 /
中队 "company"; 指挥室 "command room"; 指挥员 "commanding officer" vs 指挥官 "commander"; 突击队 "assault
team"; 直属组 "directly subordinate section" / 直属员 "directly subordinate agent"; 部队长 "unit commander";
部队代号 "unit code-name"; 编制 "establishment"; 配属关系 "relation of attachment"; 留置工作 "stay-behind
work"; 绥靖 "pacification" / 戡乱 "suppression of rebellion" / 剿匪 "bandit-suppression" / 匪谍 "Communist
spies" / 共酋 "Communist chieftains" / 共干 "Communist cadres"; 收复区 "recovered areas" / 交战区 "combat
zones"; 军需官 "quartermaster"; 行辕 "Field Headquarters" / 行辕主任 "director"; 剿匪总部/绥靖公署 "Bandit
Suppression Headquarters"/"Pacification Office". Republican years literal (三十五年 = 1946 … 三十八年 = 1949).

### Digitization glitches (rendered to plain sense; none footnoted — mechanical)
- **ch32:** dropped 。 mid-`<p>` at L10 (先生。不过), L11 (军官。先前), L13 (多了。/省份。的确), L17
  (欢迎了。/一部份。？→ stray ？), L19 (清道夫。), L26 (主要内容。/欢迎了。), L29 (溃不成军者。);
  L13 部队长！ → 部队长」 (stray ！ for 」); L21 情报组﹄归绥市 (mismatched ﹃﹄ + dropped 、 separator);
  L23 员额…主要内容 (dropped 。); L19 卤获了许多文件》 (stray 》); L23 络起来 → 摞起来 (络/摞, "stacked");
  L24 透行辕 → 透过/托 (rendered "through the prior arrangement of"); L7 听长 → 厅长 (听/厅, "chief of
  the Second Department"). All rendered to plain sense; none is a reading uncertainty.

### data/noise.txt — B25 additions
- **百废待兴** and **百事待擧** (idioms; the 百 = "myriad/all," not the count 100 — English renders the
  idiom, not a quantity). All REAL quantities CARRIED as digits/words: 200+ cities; ROC years 35/36/37/38/
  39/40 = 1946-51; the five brigades / First-Fifth Brigade; 20,000+ (2nd Brigade); ~1,000+ students;
  7 brigades + 3-4 companies; 20+ provinces; 50 vs 100+ per brigade; 4 visits by the Leader; 1-month
  terms; 200+ assault-team men; 40-odd stay-behind men (twice); past-60 veterans; the 平津 railway cut.

## Batch B26 (ch33) — 第一章 振衰起敝 二次出发 "Chapter 1. Reviving the Ailing, a Second Start"

The FIRST Part-Four NARRATIVE chapter (following the ch32 self-preface): Chen returns to Beiping in
1947 and stands up the First Brigade of the Ministry of National Defense Pacification Corps. Structure
CONFIRMED by byte-exact p-by-p diff vs the source XHTML: 1 <h2> + 4 <h3> (the section heads 一/二/三/四)
+ 153 <p>, zero mismatches; NO <h1>/<br/>/<img>/[\d+]. drop=2. clean_batch spec: standalone=[10,35,73,112]
(the four <h3>), merges=[(17,18),(19,20)]. TWO mid-phrase severs: L17/18 inside the quoted 浮生掠影集
(Liu Peichu memoir), ...你与副厅长张炎元、|侯腾两位同志商量好了; and L19/20 masked by a stray ！ standing
in for a closing 」 (实际上﹁中央训练团！|对于﹁励志班﹂...). Result 151 body paragraphs, 4 sub-headings,
source conserved OK. The inner enumerations kept as BODY per parity (三、四岁 / 二十二、三年 / 陈资一、
周世光 / 第二、三、四部书 / the committee-duties 一、二、三、四 list in one <p>).

### Checks
- verify_unit ch33: parity 151/151 OK; numbers 151 pairs unresolved 0; anchors 0 (before apparatus).
- check_align ch33: 151/151, median ratio **5.32 en/han** (HIGH; the chapter is roughly half quoted
  document: Luo Jing's ~17-paragraph autobiography, Liu Peichu's memoir quotes, Li Yulin's 事略, the
  Leader's speeches). Alignment OK, no pair strays >2.2x from median. Register is the gate, not the raw
  ratio.
- check_register --ref: within tolerance (contr 0.0, em-dash 7.6/1k vs ref 8.3, rhythm CV 0.68 vs 0.60);
  "shall" 80% flagged informationally = the deliberate narrating shall (Chen's voice sheet).
- check_structure: parity OK; anchors 300 notes, 0 unresolved; headings OK.
- check_content: ch33 165 name occurrences, ALL in the paired paragraph, 0 displaced (after aligning
  西直门/安定门 to the keyed Xizhimen/Andingmen and 冀东冀北 -> "East Hebei and North Hebei"; the
  pre-existing artifacts ch08/09/13/26 unchanged).
- qc_entities: 0 misses (after 绥靖 in L118 rendered noun "pacification" not verb "pacify").
- Tail verified against source (L154-156). qa_epub PASS (57 files, 300 refs/bodies/backlinks).
  epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings / 0 infos. **EPUB now 33/43 chapters, 300 notes.**

### Notes (6 net-new; 300 cumulative). NOT re-noted furniture
6 new notes, first-appearance disciplined: Yan'an (延安, the CCP base taken 1947); the special-operations
unit / special organization concept (特种部队/特种组织, reconciling the ch34 "Special Forces" gloss);
door-gods (门神); the Heavenly Dog (天狗, the eclipse-beast, Chen's jibe at Liu Peichu); the Great Tunnel
disaster (大隧道, Chongqing 5 June 1941); April First (四一, the service's founding anniversary). NOT
re-noted (already covered): the 绥靖/戡乱/共匪 framing, Marshall Mission/Committee of Three/Executive HQ,
the Lizhi Plan, the Jiangxi bandit-suppression/别働总队, the Youth Army, Fu Zuoyi/Beiping's surrender (all
ch32); the Baomiju as the Juntong's 1946 successor (ch04); Whampoa, the Marco Polo Bridge, fabi, the
Republican-year system (earlier batches).

### New keyed glossary rows (12; via scripts/add_ch33_glossary.py)
People: 李玉林 Li Yulin (deputy brigade cmdr, a pillar), 罗敬 Luo Jing (political director / cover
calligrapher, a pillar), 侯腾 Hou Teng (deputy chief, Second Bureau), 吴安之 Wu Anzhi, 马汉三 Ma Hansan,
张家铨 Zhang Jiaquan (upgraded from ch32 inline), 史泓 Shi Hong (upgraded from ch32 inline), 陈诚 Chen
Cheng (Chief of the General Staff). Orgs: 保密局 the Baomiju, 人民服务总队 the People's Service Corps.
Terms: 特种部队 "special-operations unit", 特种组织 "special organization" (both decided; the ch34s01
title glosses 特种部队 "Special Forces" but the body follows this chapter's "Special-Operations Unit").
Reused the whole B01-B25 keyed cast (刘原深/毕高奎/齐庆斌/曾澈/陈资一/周世光/王天木/毛人凤/郑介民/张炎元/
刘培初/傅作义 etc.) and Part-Four vocab. Rendered INLINE (one-off roster/memoir names, standard places,
Western officers): the 4 other brigade commanders 陈振山/刘仁华/郭重新/靳易夫, 王兆芬, 王文, 张作兴,
李运昌, 吕正操, 楼兆元, 王云孙, and Luo Jing's whole memoir roster; 华北忠义救国军 "the North China Loyal
and Patriotic Army" (built on the keyed 忠义救国军); Marshall / Colonel Robertson.

### Digitization glitches (rendered to plain sense; none footnoted — mechanical)
- **ch33:** L14 马歌尔 for 马歇尔 (Marshall; L13 spells it correctly); ⋮ (U+22EE) as ellipsis at L5;
  stray ！ standing for 」 at L17 (中央训练团！), L46 (掏粪的！), L89 (死刑屮 stray 屮 for 」), L117
  (华北忠救军！); stray 『 opening bracket + " for 」 at L19 (励志“即将); stray ？ at L55 (李汉元？), L61
  (恶意？), L62 (情治单位？), L69 (天津之行？); stray | at L44 (小三合|, dropped 院，); 〇 (U+3007) glitch
  at L86 (不至于吧〇); corrupt run at L20 (名过 for 名流, 一甸 for 一句, 回公/批着 garbled), 恺切 for 剀切
  at L19, 丽友 for 良友 at L61, 示能 for 不能 at L92; × redaction 冯xx at L136 (rendered "Dr. Feng ——").
  Many dropped 。 mid-<p> (L3, L5, L14, L15, L16, L38, L46, L50, L57, L61, L81, L118, L119, L149).
  All rendered to plain sense; none is a reading uncertainty.

### data/noise.txt — B26 additions
- Name-numerals **马汉三** (Ma Hansan, 三), **英千里** (Ying Qianli, 千), **陈资一** (Chen Ziyi, 一);
  idiom **百废待擧** (a 擧-variant of 百废待兴, the 百 = "myriad," not 100). REAL quantities carried as
  digits/words: 3,500 words (Lizhi Plan); ~120 men/brigade, ~600 total (alt 400+); 5 brigades / First-Fifth
  Brigade; 7 brigades + 3 companies; 1,500 yuan fabi (twice); ROC years 3/6/22-23/26/27/28/29/30/32/34/35/
  36/41/46/51/57 and 民前七年 = 1905, all matched by ordinal or +1911; No. 5 / Fifth Brother; the twenty-odd
  signatories; 100-day detention; 8 days at sea; 20+ medical students.

## Batch B27 (ch34) — 第二章 自动自发 同心同德 "Chapter 2. Self-Starting, of One Heart and Mind"

The SECOND Part-Four narrative chapter and the doctrinal one: Chen defines the special-operations unit,
lays out the First Brigade's establishment, its three features (求创新/有冲劲/致祥和 "to seek the new / to
have drive / to reach concord"), and closes with three gatherings (a Beiping command briefing, the 1938
Tianjin "joint operations," and a Taiwan-era high-level briefing) that frame collective leadership.
Structure CONFIRMED by byte-exact p-by-p diff vs the source XHTML: 1 <h2> + 3 <h3> (section heads 一/二/三)
+ 127 <p>, ZERO mismatches; NO <h1>/<br/>/<img>/[\d+]. drop=2. clean_batch spec: standalone=[15,53,90]
(the three <h3>, raw 1-based), merges=[] (no severed <p>: every kept line matched its element exactly, both
non-terminal and glitch-masked ！？》 endings scanned). Result 127 body paragraphs, 3 sub-headings, source
conserved OK. The doctrinal INNER enumerations kept as BODY per parity (NOT headings): the 第一/第二/第三
features list under section 2 (body L86-88); the 一/二/三 duty lists in single <p> (L36-38, L125-128); the
number-ranges 十三、四年 / 两、三百人 / 五、六天.

### Checks
- verify_unit ch34: parity 127/127 OK; numbers 127 pairs unresolved 0 (after 5 noise additions, below);
  anchors 0 (before apparatus).
- check_align ch34: 127/127, median ratio **5.19 en/han** (HIGH, as expected for a doctrinal/definitional
  chapter, cf. ch33's 5.32); alignment OK, no pair strays >2.2x from median. Register is the gate, not ratio.
- check_register --ref: within tolerance (contr 0.0 = ref; em-dash 9.3/1k vs ref 8.3; rhythm CV 0.64 vs 0.60);
  "shall" 33% flagged informationally = the deliberate narrating shall (Chen's voice sheet).
- check_structure: parity OK; anchors 303 notes, 0 unresolved; headings OK.
- check_content: ch34 46 name occurrences, ALL in the paired paragraph, 0 displaced (the pre-existing
  artifacts ch08 Shunde ×3 / ch09 Jize ×1 / ch13 ×9 / ch26 ×2 unchanged).
- qc_entities: 0 misses (特种部队 x17, 特种组织 x10, 绥靖 x20, 绥靖总队 x14, 人民服务总队 x4, 刘培初 x4 all
  survive; 绥靖 rendered noun "pacification"/"Pacification" throughout, never the verb).
- Tail verified against source (L128-131, the 四/据理力争/民主原则/三个故事 close). qa_epub PASS (57 files,
  303 refs/bodies/backlinks). epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings / 0 infos.
  **EPUB now 34/43 chapters, 303 notes.**

### Notes (3 net-new; 303 cumulative). NOT re-noted furniture
3 new notes, first-appearance disciplined (doctrinal chapter → few new items): the Transport Police Corps
(交通警察总队, the postwar rebadging of the Loyal and Patriotic Army under Marshall's army-cut pressure);
the India-Burma Expeditionary Force (印缅远征军, the Chinese Expeditionary Force in Burma 1942-45, Yang
Rongyuan's old service under Liao Yaoxiang); Tan/Han Family Cooking (谭家菜/韩家菜, the famous Beijing
"official-household" private-kitchen cuisine, still served at the Beijing Hotel). NOT re-noted (already
covered): 特种部队/特种组织 (ch33), the 绥靖/戡乱/共匪 framing, the Marshall Mission, the Lizhi Plan, the
Jiangxi bandit-suppression/别働总队, the Youth Army (all ch32); the Baomiju (ch04); the Zhongshan tunic
(ch06), the Renaissance Society/Blue Shirts (ch08), Duan Qirui (ch07), the Legation Quarter and the Hotel
of Six Nations (ch06); Whampoa, fabi, the Republican-year system (earlier).

### New keyed glossary rows (3; via scripts/add_ch34_glossary.py)
Orgs: 交警总队 "Transport Police Corps", 华北剿匪总司令部 "North China Bandit-Suppression Headquarters"
(the 0760-code issuer; built on the keyed 剿匪 "bandit-suppression"). People: 聂恩俊 Nie Enjun (First
Brigade quartermaster; provisional; Chen flags him to revisit). Reused the whole B01-B26 keyed cast and
Part-Four vocab. Rendered INLINE, NOT keyed (consistent with the ch33 decision): 王兆芬 Wang Zhaofen and
张作兴 Zhang Zuoxing (inline since ch33); the two spy students 杨荣远 Yang Rongyuan / 王铭扬 Wang Mingyang;
the brigade-commander roster 陈振山/刘仁华/王德新/郭重新/杨正之/靳易夫/管容德 and memoir author 张振东; the
command-room COs 江田/常绍曾/庞兆丰/张筱朴/张鲁颖; 廖耀湘 Liao Yaoxiang (one mention); the food writer
唐鲁孙 Tang Lusun; the Tianjin joint-office members 沈泽臣/张子奇/王若僖; supply chiefs 耿/吕. 华北忠义救国军
renders on the keyed 忠义救国军.

### Keyed renderings reused in the ch34 body (qc-enforced)
特种部队 "special-operations unit" (title-level "Special Forces" is title-only), 特种组织 "special
organization", 绥靖总队 "the Pacification Corps", 军统/军统局 "the Juntong"/"the Juntong Bureau", 保密局
"the Baomiju", 中统 "the Zhongtong", 复兴社 "the Renaissance Society", 国防部第二厅 "the Second Bureau of
the Ministry of National Defense", 人民服务总队 "the People's Service Corps", 忠义救国军 "the Loyal and
Patriotic Army", 励志训练班 "the Lizhi Training Class", 直属组 "directly subordinate section", 指挥室
"command room", 指挥员 "commanding officer" vs 指挥官 "commander", 部队长 "unit commander", 大队长 "brigade
commander", 中队 "company", 编制 "establishment", 配属 "attach". People: 李玉林 Li Yulin, 罗敬 Luo Jing,
刘培初 Liu Peichu, 刘原深 Liu Yuanshen, 郑介民 Zheng Jiemin, 戴笠/戴先生 "Mr. Dai", 应元勋 Ying Yuanxun,
张敬尧 Zhang Jingyao, 段祺瑞 Duan Qirui.

### Digitization glitches (rendered to plain sense; none footnoted — mechanical)
- **ch34:** stray ！ standing for 」 at L23 (绥靖总队！), L56 (大队长！ / 虚荣！), L58 (华北忠救军！);
  stray ？ for 、 at L31 (大言不惭？); stray 〇 (U+3007) for a stop/？ at L81 (需要呢〇), L99 (只供一桌〇);
  U+3007 in the numeral strings 〇七六〇 (Unit 0760, L10) and 二〇五师 (205th Division, L32); stray glyphs
  ︸ for ﹁ (L19 特别任务, L30 绥靖), ︴ (L78, after 一百五十人以下), | (L81/L86 dash-stroke), |- (L105),
  ≤ for a stop (L123); mismatched ﹃/﹁ guillemets (L4/L17/L23/L79). Char substitutions: 缓靖→绥靖 (L50),
  情治箪位→情治单位 (箪/单, L24), 岩重→严重 (L36), 也示无可议→也不无可议 (示/不, L36), 淮境→佳境 (L99),
  些么→什么 (L108), 刀"定→到底 (L30), ﹁。供﹂ (L32, a stray 。 inside 「供」), 卤获→掳获 "captured" (L55).
  Variant/valid forms kept to sense: 变体武装/变制武装 "an armed force of irregular form" (L4/L18), 队附/
  队副 "brigade deputy". Many dropped 。 mid-<p> (L4, L6, L23, L44, L50, L55, L81, L86, L130). × redaction
  项xx → "Xiang ——" (L50). All rendered to plain sense; none is a reading uncertainty.

### data/noise.txt — B27 additions (5)
- **三数百** "some three hundred men / several hundred" (assault-team strength, L79) — placed BEFORE the
  older 三数 rule so it pre-empts it (else 三数 fires first and orphans a bare 百=100); English "some three
  hundred men". **四象桥** "Sixiang Bridge" (Nanjing HQ address, L44) — the 四 is a place-name glyph.
  **十三、四** "the thirteenth and fourteenth years" (民国十三、四年 = 1924-25, L63) — the 四 elides 十四 (14),
  carried as the ordinal "fourteenth". **四壁** "on every side / the four bare walls" (idiom, L64) — not a
  count of 4. **两租界** "the British and French Concessions" (L113) — the 两 is a counter carried by naming
  both. **东四** "Dongsi (North Avenue)" (Beiping district, L63) — the 四 is a place-name glyph. All REAL
  quantities carried as digits/words: 6,000 officers; 3,500 to Taiwan / 2,500+ lost (written as DIGITS, the
  compound-composition trap); ~600 est. / 400 employed / a thousand-and-several-hundred; 7 brigades + 3
  companies + 1 assault brigade; five command rooms; ~100-150 per room; ROC years 22-23/27/28/36/37/38/75,
  all matched by ordinal or +1911; eleven characters; eighteen months; two years; eightieth birthday.

## Batch B28 (ch35) — 第三章 一番风雨 几片落叶 "Chapter 3. A Spell of Storm, a Few Fallen Leaves"

The THIRD Part-Four narrative chapter. Chen reports for duty and fixes the First Brigade's chain of
command (attached to the Beiping Field Headquarters, then the North China Bandit-Suppression Headquarters,
both directors indifferent); gathers old comrades to build up the brigade's strength; and mounts the
operation this chapter is really about — using the ex-Communist schoolmate Li Mingqiu as a go-between to
reach the Communist commanders Lin Biao and Tao Zhu (Chen's own Whampoa classmate) in the Northeast, for
strategic intelligence, which won the brigade two large Ministry-of-National-Defense prizes. It closes on
the bleak fates of the players: Li Mingqiu dead months later; Jiang Tian and Zhang Zuoxing destroyed in
the early-PRC campaigns; Tao Zhu broken in the Cultural Revolution; Lin Biao dead in the 1971 plane crash.
Structure CONFIRMED by byte-exact p-by-p diff vs the source XHTML: 1 <h2> + 4 <h3> (section heads
一、/二、/三、/四、) + 196 <p>, ZERO mismatches; NO <h1>/<br/>/<img>/[\d+], 0 images. drop=2. clean_batch
spec: standalone=[8,49,77,141] (the four <h3>, raw 1-based), merges=[(25,26),(136,137)] — TWO glitch-masked
severs: L25/26 (...我当﹁天津站！|长时..., the ！ standing for 」 and the word 站长 "station chief" split across
the boundary), and L136/137 (...嘴里说：﹃在打流！|﹂我点穿他说..., the dialogue's closing bracket ﹂ orphaned
onto the next <p>). The other ！？》-ending lines (L12/30/33/47/53/90/172/173) are genuine terminal rhetorical
questions, NOT severs. Result 194 body paragraphs, 4 sub-headings, source conserved OK. INNER enumerations
kept as BODY per parity (NOT headings): the 一/二/三/四/五 go-between-qualification list (L148-152), the
其一/其二/其三 intelligence tiers (L86-89), Zheng's 一/二/三/四 instructions (L182-185), the name-lists and
number-ranges.

### Checks
- verify_unit ch35: parity 194/194 OK; numbers 194 pairs unresolved 0 (after 8 noise additions, below);
  anchors 0 (before apparatus).
- check_align ch35: 194/194, median ratio **5.15 en/han** (higher than the ~4.55-4.78 narrative guide, but
  this chapter carries the marble-bridge digression, essayistic reflection, and formal dialogue; cf. ch34's
  doctrinal 5.19, ch33's 5.32). Alignment OK, no pair strays >2.2x from median — alignment/register are the
  gates, not the raw ratio.
- check_register --ref: within tolerance (contr 0.0 = ref; em-dash 6.8/1k vs ref 8.3; rhythm CV 0.57 vs 0.60);
  "shall" 11% flagged informationally = the deliberate narrating shall (Chen's voice sheet).
- check_structure: parity OK; anchors 311 notes, 0 unresolved; headings OK.
- check_content: ch35 162 name occurrences, ALL in the paired paragraph, 0 displaced. ALSO fixed a
  PRE-EXISTING ch32 displacement (see Corrections). The four pre-existing artifacts (ch08 Shunde ×3 /
  ch09 Jize ×1 / ch13 ×9 / ch26 ×2) unchanged.
- qc_entities: 0 misses (北平 x47, 李鸣秋 x44, 林彪 x26, 江田 x24, 张作兴 x21, 绥靖 x19, 天津 x18, 陶铸 x18,
  李运昌 x12, 军统 x6, 郑介民 x6, 东北人民解放军 x5 all survive; 绥靖 rendered noun "pacification" throughout).
- Tail verified against source (L195-199, the five endings: Li Mingqiu / Jiang Tian / Zhang Zuoxing / Tao Zhu
  / Lin Biao, closing on Chen's own "record of the brush, awaiting the summons"). qa_epub PASS (57 files,
  311 refs/bodies/backlinks). epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings / 0 infos.
  **EPUB now 35/43 chapters, 311 notes.**

### Notes (8 net-new; 311 cumulative). NOT re-noted furniture
8 new notes, first-appearance disciplined: the Jin'ao-Yudong Bridge (金鳌玉𬟽桥, the white-marble bridge over
the Beihai/Zhongnanhai water, with its two archways, dismantled/widened mid-1950s; 汉白玉 white marble folded
in); the Du Fu couplet (此景只应天上有..., Chen's adaptation of 赠花卿 "To General Hua," 曲/闻 → 景/看); the
逐鹿/逐臭 idiom pair (chasing the deer = power, chasing the stink = base gain); Lin Biao's death (林彪
1907-1971, the 1969 successor/vice-chairman, the 1971 Ondorhaan crash — the "riddle" Chen twice invokes);
the 1927 Party Purge (清党, cross-referenced to the already-noted Ning-Han Split, the Whampoa fall-out scene);
the Guangzhou Uprising (广州大暴动, 11-13 Dec 1927, the "December Twelfth" / Guangzhou Commune, from which Tao
Zhu was freed); the Social Affairs Department (社会部, the CCP intelligence organ headed by Kang Sheng NOT Luo
Ronghuan — Chen's placement of 罗荣桓 there is his own surmise "应是", scholarship-flagged as not borne out);
the Three-Anti/Five-Anti/Suppress-Counterrevolutionaries campaigns (三反/五反/镇压反革命, 1950-53). NOT re-noted
(already covered): the 绥靖/戡乱/共匪 framing, Juntong/Baomiju, 特种部队/特种组织, the Lizhi Class, the Loyal and
Patriotic Army, the Transport Police Corps, Whampoa, Tilanqiao, the Japanese gendarmerie, the Republican-year
system; the Cultural Revolution/Red Guards and Tao Zhu's fall (already noted at an earlier chapter).

### New keyed glossary rows (5; via scripts/add_ch35_glossary.py)
People: 李鸣秋 Li Mingqiu (the ex-Communist go-between, chapter pivot; provisional), 李运昌 Li Yunchang
(East-Hebei guerrilla chief, later CCP general/Minister of Railways; attested), 罗荣桓 Luo Ronghuan (NE-army
commissar, later marshal; attested), 黄郛 Huang Fu (the diplomat Yingbai, He Yingqin's early-1930s Beiping
stand-in; attested). Orgs: 东北人民解放军 "the Northeast People's Liberation Army" (Lin/Tao's field army, the
operation's target; decided — NB the source once prints the glitch 东北人民解放车 车/军, correct glyph present
elsewhere). Reused the whole B01-B27 keyed cast and Part-Four vocab. Rendered INLINE, NOT keyed (glossary-key
discipline, consistent with the ch33/ch34 decisions): 白家祺 Bai Jiaqi, the interpreter trio 王智斌/齐枕平/
郭子中, 李耀 Li Yao, 李长清 Li Changqing, the introduced officers 庞兆丰/刘文勋/张筱璞/魏钧, the Shanghai-days
colleagues 毛一鹭/黄维/洪复予/周祺卿, 尹擎宇 Yin Qingyu, Jiang Tian's Communist kin 江灏/江振寰, the Whampoa-days
roster 郭大荣/赵锦文/俞镛/丁维经/王文翰/李靖难/卢濬泉/帅崇兴/惠济/王登梯/方鼎英/吴思豫/万力民/何焜/钟期光, 范行
Fan Xing. 华北忠义救国军 renders on the keyed 忠义救国军; 华北人民解放军 and 东北剿匪总司令部 (one mention each)
render inline.

### Corrections (cross-unit)
- **ch32 para 25 (§ ch32):** aligned "North China Bandit Suppression Headquarters/Command" → the keyed
  hyphenated form "North China Bandit-Suppression Headquarters" (华北剿匪总司令部, keyed at B27/ch34). This
  was a PRE-EXISTING check_content displacement introduced when the hyphenated key was added at B27 (confirmed
  present on the committed HEAD before B28). Regenerated ch32 en.json; check_content ch32 now 0 displaced.

### Keyed renderings reused in the ch35 body (qc-enforced)
军统/军统局 "the Juntong"/"the Juntong Bureau", 保密局 "the Baomiju", 特务处 "the Special Services Department"
(the Juntong's forerunner), 绥靖总队 "the Pacification Corps", 华北剿匪总司令部 "North China Bandit-Suppression
Headquarters", 忠义救国军 "the Loyal and Patriotic Army", 励志训练班/励志班 "the Lizhi Training Class"/"Lizhi
Class", 红卫兵 "the Red Guards", 特种部队 "special-operations unit", 绥靖 "pacification" (noun throughout).
Vocab: 北平行辕 "the Beiping Field Headquarters", 大队 "brigade"/大队长 "brigade commander", 中队 "company",
指挥室 "command room", 指挥员 "commanding officer", 直属组 "directly subordinate section", 配属关系 "relation
of attachment", 编制 "establishment", 戡乱 "suppression of rebellion", 剿匪 "bandit-suppression", 冀东 "East
Hebei". People: 李宗仁 Li Zongren, 傅作义 Fu Zuoyi, 刘培初 Liu Peichu, 张家铨 Zhang Jiaquan, 郑介民 Zheng
Jiemin, 江田 Jiang Tian, 张作兴 Zhang Zuoxing, 林彪 Lin Biao, 陶铸 Tao Zhu, 聂荣臻 Nie Rongzhen, 毛泽东 Mao
Zedong, 周恩来 Zhou Enlai, 陈独秀 Chen Duxiu, 李大钊 Li Dazhao, 戴笠 Dai Li (戴雨农 "Mr. Dai Yunong"),
何应钦 He Yingqin (何敬公), 王文 Wang Wen, 曾澈 Zeng Che, 毛万里 Mao Wanli, 齐庆斌 Qi Qingbin, 罗君强 Luo
Junqiang, 史泓 Shi Hong.

### Digitization glitches (rendered to plain sense; none footnoted — mechanical)
- **ch35:** stray ！ standing for 」 at L25 (天津站！, the merged sever), L95 (副主席！), L113 (华北忠救军！),
  L114 (天津站！长), L136 (在打流！, the merged sever); stray glyph 〇/× not present here, but a stray glyph ︼
  for 」 at L169 (一无﹁种因︼) with doubled ，，; ≤ stray glyph at L35 (请随我来≤﹂); | intra-<p> stroke at
  L26 (此桥|原来) and L53 (朋友们|在拙着); 〇-like glitch: 这怎么讲呢〇 (L145, 〇 for ？). Char substitutions:
  东北人民解放车→东北人民解放军 (车/军, L134), 季鸣萩→李鸣秋 (季/李, 萩/秋, L173), 回答莪说→回答我说 (莪/我,
  L38), 宝坁县→宝坻县 (坁/坻, L113), x redactions 第x路/第x纵队/军校x期 (L113/L94/L128) rendered "——th".
  Rare/variant glyph 玉𬟽 (𬟽 for 蝀 in the bridge name 金鳌玉𬟽桥, L26/28) — kept as the source form, note
  gives the standard romanization Jin'ao Yudong. Many dropped 。 mid-<p> (L2/3/8/9/11/13/16/25...). All
  rendered to plain sense; none is a reading uncertainty.

### data/noise.txt — B28 additions (8)
- **两旁** "on both sides" (道路两旁, L33) — the 两 is the set idiom for "both/either side," English "the one
  side... the other". **两者** "the two [groups]" (新参加的与受过训的两者之间, L73) — counter carried by naming
  both. **二人** "the two of them" (毛一鹭、黄维二人 / 江田、李鸣秋二人 / 林、陶二人) — counter-by-naming, both
  named. **两地** "in Beiping and Tianjin" (北平、天津两地, L155) — counter-by-naming. **万力民** (Wan Limin, a
  1927-purged Whampoa cadet, L130) — the 万 is the surname (Wan), not 10000. **四平街** "Siping" (a Northeast
  town, L189) — the 四 is a place-name glyph. **一百三、四十** "some hundred and thirty or forty men" (L132) —
  the source hedges 130/140, carried as the approximate, not the composed 103. **一百零几** "a hundred and
  some men" (Tao Zhu's hedged survivor count, L134) — the 几 makes it approximate ("a hundred-odd"). All REAL
  quantities carried as digits/words: 120 men (DIGITS, the compound-composition trap); nine years' prison;
  twenty-odd young recruits; six or seven / three interpreters; two or three hundred (guerrilla band); ROC
  years 15/18-19/21/22-23/25/27/28/30/32/35/36/37/38/40, all matched by ordinal or +1911; the 1179 Jin-dynasty
  lake date carried literally.

## Batch B29 (ch36) — 第四章 掌握先机 备多力分 "Chapter 4. Seizing the Initiative, Spread Too Thin"

The FOURTH Part-Four narrative chapter, in four sections: (1) the value and timeliness of
intelligence and its use, opening onto the failed attempt to reach Lin Biao/Tao Zhu (a
supplement to ch35), the three intelligence items Li Mingqiu brought back, and the riddle of the
pistol-carrying visitor; (2) the gun-gift affair — Liu Yuzhu's "gift" of ~2,000 Japanese rifles
that nearly drew Chen into the abuse-of-power case that destroyed "Mr. Ma" (Ma Hansan) and Liu;
(3) the "heart-extraction tactic" — the Provisional Third Army's cavalry dash on Anguo to seize
Mao, mistimed so the Bandit Chief escaped (Xiao Runyu's long contributed "Record of the Work"),
with Chen's critique of the botched pursuit; (4) the Battle of Shijiazhuang (Nov 1947) — the fall
of Shimen and the fighting, capture, and sacrifice of the work-group (Niu Guangjin's contributed
"Brief Record"), with Chen's reflections on dispersed defense, prisoner-handling, and abandoning
recovered areas.

### Structure / ⚠ SOURCE DUPLICATION artifact
Byte-exact p-by-p diff vs the source XHTML: 1 <h2> + 4 <h3> (section heads 一、/二、/三、/四、) + 188
<p>, ZERO mismatches; NO <h1>/<br/>/<img>/[\d+], 0 images. The "1-line count scare" flagged in the
kickoff was a trailing-newline miscount: the file has NO trailing newline, so it is 194 lines
(wc -l counts 193), and 194 − drop(2) = 192 body lines = 4 <h3> + 188 <p>. clean_batch spec:
drop=2; standalone=[18,71,108,154] (the four <h3>, raw 1-based); merges=[(49,50)] — ONE glitch-
masked sever (...其后更由﹁地方！|转向﹁中央﹂..., the ！ standing for closing 」, the phrase
由﹁地方﹂转向﹁中央﹂ "from the 'local' turning toward the 'central'" split across the boundary).
The other ！？》-ending lines are genuine terminal rhetorical questions/exclamations, NOT severs
(notably L52 ...形容为一场﹁智慧鬪争！, a grammatically complete predicate; L53 高明者就可以占上风 is a
separate short sentence). Result 187 body paragraphs, 4 sub-headings, source conserved OK.
- **THE MAJOR ANOMALY:** the chapter's opening is DUPLICATED in the source. The intelligence-
  timeliness preamble appears THREE times — the chapter preamble (data/zh z2-16), a restatement at
  the head of section 1 (z18-32), and a partial re-restatement (z33-37) — with the Anguo raid +
  the two contributed-account intros appearing twice (z2-16 and z18-32). z33 (a single source <p>)
  even fuses the 牛广金 sentence + the section-1 HEADING TEXT (一、从情报的价値观念说到情报运用) + the
  first section-1 body para. Real narrative begins at z38. This is a digital-source production
  artifact. Per CLAUDE.md rule 4, ALL of it is translated faithfully (parity preserved, nothing
  dropped, nothing invented), each pass rendered per its own actual wording (they differ slightly),
  and a footnote at the head of section 1 (anchor "already carries within it the sense of")
  explains the repetition honestly and leaves it visible.
- INNER enumerations kept as BODY per parity (NOT headings): the three intelligence items 一/二/三
  (z52/53/59) with the guiding-points sub-list 二/三/四/五/六 (z54-58); the temple-search rhetorical
  checklist (z144-151); the border-region committee roster; the section membership roster.

### Checks
- verify_unit ch36: parity 187/187 OK; numbers 187 pairs unresolved 0 (after 11 noise additions,
  below); anchors 8 ok (after apparatus).
- check_align ch36: 187/187, median ratio **5.42 en/han** (above the ch33-35 5.15-5.32 band, but
  this chapter carries two long contributed memoir-accounts, the tripled preamble, and heavy
  essayistic reflection). Alignment OK, no pair strays >2.2x from median — alignment/register are
  the gates, not the raw ratio.
- check_register --ref: within tolerance (contr 0.0 = ref; em-dash 7.3/1k vs ref 8.3; rhythm CV
  0.59 vs 0.60; sent med 28); "shall" 0% this chapter (the deliberate narrating shall is sparse
  here; flagged informationally per the voice sheet when present).
- check_structure: parity OK; anchors 319 notes, 0 unresolved; headings OK.
- check_content: ch36 76 name occurrences, ALL in the paired paragraph, 0 displaced. The four
  pre-existing artifacts (ch08 Shunde ×3 / ch09 Jize ×1 / ch13 ×9 / ch26 ×2) unchanged.
- qc_entities: 0 misses (石门 x30, 北平 x25, 石家庄 x24, 安次 x19, 毛泽东 x16, 安国 x14, 林彪 x14,
  刘玉珠 x13, 萧润宇 x8, 李鸣秋 x7, 东北人民解放军 x7, 朱占奎 x7 all survive; 掏心战术 rendered
  "the heart-extraction tactic" and 平津保三角地带 "the Beiping-Tianjin-Baoding triangle" throughout).
- Tail verified against source (z188-192: the small unit's limits, the clumsy leadership, the no-
  prisoner-handling course, the twice-abandoned recovered areas, closing on "political warfare"
  still worth deep study). qa_epub PASS (57 files, 319 refs/bodies/backlinks). epubcheck 5.1.0:
  0 fatals / 0 errors / 0 warnings / 0 infos. **EPUB now 36/43 chapters, 319 notes.**

### Notes (8 net-new; 319 cumulative). NOT re-noted furniture
8 new notes, first-appearance disciplined: the source-duplication artifact (see above); the
heart-extraction tactic (掏心战术, deep raid to seize the enemy's leadership at a stroke); the
Nationalist recovery of Yan'an (延安, Hu Zongnan, 19 Mar 1947 — symbolic, retaken Apr 1948); the
Paojuzi prison (炮局子, a Japanese-era Beiping jail); the Type 38 / Type 30 rifles (三八式/三〇式, the
Japanese Arisaka bolt-actions, surrendered in vast numbers in 1945); a SCHOLARSHIP VERDICT that
the intelligence placing Mao at Anguo was mistaken (毛泽东 stayed in 陕北 through 1947; the
Shijiazhuang campaign was Nie Rongzhen's 聂荣臻, not Mao's — text stands, footnote flags it); the
Mao epithets (毛贼泽东/毛酋, of the same idiom as 共匪/匪酋); the Battle of Shijiazhuang (石家庄/石门,
Nie Rongzhen's forces, fell 12 Nov 1947, the first sizable city the CCP took and held). NOT
re-noted (already covered): the 绥靖/戡乱/共匪 framing, 匪谍/共酋/共干, Juntong/Baomiju, 特种部队, the
Lizhi Class/Central Training Corps, the North China Bandit-Suppression HQ and Beiping Field
Headquarters, Fu Zuoyi, Whampoa, the Marco Polo Bridge (七七), the Republican-year system, the
Three-Anti/Five-Anti/Suppress-Counterrevolutionaries campaigns, and Lin Biao's 1971 death.

### New keyed glossary rows (13; via scripts/add_ch36_glossary.py)
People: 安春山 An Chunshan (Provisional Third Army cmdr, Fu's favorite; provisional), 朱占奎 Zhu
Zhankui (Anci magistrate, ex-Communist who re-defected in 1948; provisional), 刘玉珠 Liu Yuzhu
(the gun-gift fixer; provisional), 萧润宇 Xiao Runyu (section 3 account author; provisional),
牛广金 Niu Guangjin (section 4 account author; provisional), 吕正操 Lü Zhengcao (Central Hebei
Military District cmdr, later PLA general; attested). Places: 石家庄 Shijiazhuang, 石门 Shimen (the
older name Chen uses), 安次 Anci, 安国 Anguo, 正定 Zhengding (all decided). Terms: 掏心战术 "the
heart-extraction tactic", 平津保三角地带 "the Beiping-Tianjin-Baoding triangle" (decided). Reused the
whole B01-B28 keyed cast and Part-Four vocab. Rendered INLINE, NOT keyed (glossary-key discipline):
罗历戎 Luo Lirong, 刘英 Liu Ying, 张铁林 Zhang Tielin, the section roster 陈秀桐/郑静庭/冯志俊/姜丙辰/
白永龄/赵万里/王德新/张果维/马惠璋/郭清钰, the work-group roster 张建三/张侗夫/杨志毅/牛清川/李明光/杨清/
朱志璋, the Second-Command-Room contributors 常绍曾/汪鸿翥/吴春祥/陈俊祥, 曾泽生 Zeng Zesheng, 刘伯承
Liu Bocheng, 胡宗南 Hu Zongnan, 邓宝珊 Deng Baoshan, 傅东菊 Fu Dongju, the border-region committee
宋劭文/胡仁奎/彭真/孟庆山/程子华/罗玉川, the Shimen relief mission 屈凌汉/罗文浩/李荷/孙连仲/刘瑶章.
马先生 = Ma Hansan (already keyed as 马汉三; source names him only "Mr. Ma" here). The deputy chief
of staff whose surname the source prints as a garbled glyph (鿄述哉) rendered "—— Shuzai".

### data/noise.txt — B29 additions (11)
- **三角地带** (三角 "triangle" in 平津保三角地带/平津三角地带) — descriptor, carried "triangle".
- **五台** (五台山[区] "the Wutai Mountains") — place-name numeral. **十余万** (approximate "more than
  a hundred thousand," Lin's force) — MUST precede the bare 十余 rule (relocated before it, else
  十余 consumes it and orphans the 万). **三〇式** ("Type 30" rifle; the 〇 is the mis-read zero
  glyph). **千奇百怪** (idiom, "every freak and marvel," 千/百). **老千** ("card-sharp," slang, 千).
  **七、八十** (approximate "seventy or eighty li"). **四望** (idiom 举目四望 "gazing about," 四).
  **万急** (idiom 情况万急 "utmost extremity," 万). **张建三** (name numeral, section member). **张建二**
  (name-glitch for 张建三; 二). All REAL quantities carried as DIGITS (the compound-composition
  trap): 2,000 rifles, 200 li, 800,000 / 3,200,000 / 1,150,000 / 2,700,000 troops, 100,000 /
  16,000 / 20,000 / 10,000 casualties, 190,000 / 300,000 population, 70,000 / 30,000, four to one;
  ROC years 24/27/34/35/36/37/38/39/75 matched by ordinal or +1911; case No. 1906 literal.

### Digitization glitches (rendered to plain sense; none footnoted — mechanical)
- **ch36:** single-char substitutions 暴珍天物→暴殄天物 (珍/殄, z5), 松是→始终是 (z19), 厉害→利害
  (z21), 事熊→事态 (z87), 右门→石门 (右/石, z164), 认有→认为 (有/为, z189), 惋借→惋惜 (借/惜, z188),
  匐匍→匍匐 (transposed, z179), 位是→位于 (z159), 不股→小股 (z122), 工肃清→一肃清 (工/一 in the 工/二/
  三/四 list, z118); stray ！ standing for 」 (z48 伪﹁广东省长！。 and 由﹁地方！ [the merged sever];
  z50 智慧鬪争！); stray glyph ︸ for ﹁ (z23 其︸时间性, z112 ︸暂编第三军 / ︸〇七六〇, z150 ︸走远了);
  stray 》 for punctuation mid-clause (z4 民间团体》, z105 余愠》, z172 功能》, z192 必要》); stray 〔/〕/《
  (z87 他这句话〕, z150 罢休《); stray | intra-<p> stroke (z134 活捉毛贼泽东| and 训令|); 〇 in
  addresses/codes/numbers (z81 三〇式, z112 〇七六〇 the 0760 code, z134 一九〇六号) — the numeric
  checker mis-reads 〇, so the real values are carried in English and only the mis-read glyph-string
  is noised; × redactions rendered as em-dash blanks (z168 十月十x日 "the ——th of October", z175
  杨x芳 "Yang ——fang", z112 李xx "Li ——"); variant/rare glyphs 价値/価値 (值), 鬪 (斗), 尙 (尚), 刼
  (劫), 躭 (耽), and a garbled surname glyph 鿄 in 鿄述哉, rendered "—— Shuzai". Many dropped 。
  mid-<p>. All rendered to plain sense; none is a reading uncertainty.

---

## Batch B30 (ch37 = 第五章 兵连祸结 民不聊生, the FIFTH Part-Four narrative chapter)

"Chapter 5. War Unending, the People Destitute." Three sections: ch37s01 "The Fall of Shimen:
100,000 Communist Troops Attack, a Few Thousand Nationalists Hold On"; ch37s02 "Different Ground:
Welcomed Here, Shunned There"; ch37s03 "A Bitter Fight: Local Corps against the Communist Militia."
The fall of Shimen and the terror that followed (from Lu Deming's contributed account); the North-
Suburb Group welcomed while the West-Suburb Group was shunned by the North China Bandit-Suppression
HQ on its own side; and Tian Yingjie's first-person narrative of the October 1948 night battle of
Lishuiqiao between the Daxing local corps and the Communist militia.

### Structure
- drop=2 (running header 英雄无名-陈恭澍 + <h2> chapter title). Byte-exact p-by-p diff against the
  source XHTML: 1 <h2> + 3 <h3> (section heads 一/二/三) + 144 <p>, ZERO mismatches; NO <h1>/<br/>/
  <img>/[\d+], 0 images. File has NO trailing newline (149 lines; wc -l counts 148); after drop=2 the
  txt has 147 body lines = 3 <h3> heads (raw 1-based L11/L43/L90) + 144 <p>. standalone=[11,43,90].
- NO severed-<p> merges. The two glitch-masked ！-ending candidates are BOTH complete separate
  sentences, not mid-predicate severs (L79 ...不满。！ with a doubled 。！ then L80 a new sentence
  headed by a stray ︸; L91 ...摩星岭之役！ closes a title, L92 opens with an orphaned 。 then a NEW
  sentence). NO ch36-class source-duplication (the near-duplicate scan found nothing >0.6).
- 144 body paragraphs. median ratio 5.50 en/han (document/quote-heavy: two long contributed
  first-person accounts plus an embedded doggerel song). Alignment OK (no pair strays >2.2x).

### Checks (all green)
- verify_unit ch37: parity OK; numbers 0 unresolved (after the noise additions below); anchors OK.
- check_align: median 5.50, OK. check_structure: ALL PASS (327 notes, 0 unresolved). check_content:
  ch37 138 name occurrences, 0 DISPLACED (the ch08/09/13/26 lines are the documented pre-existing
  artifacts). qc_entities: 0 misses (census top: 立水桥 x27, 北平 x23, 石门 x14, 常绍曾 x10). Tail
  verified against source (the grim well/corpse close of section 3 is faithful and complete).
  check_register --ref: within tolerance ("shall" deliberate). check_apparatus: 0 failures.
  qa_epub: PASS (37/43 chapters, 327 notes). epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings.

### Notes (8 new; 327 cumulative) — all first-appearance, none re-noted
1. Province one-character abbreviations (晋/察/冀/鲁/豫 = Shanxi/Chahar/Hebei/Shandong/Henan) and the
   Communist wartime "border regions" (anchor "Jin-Ji-Lu-Yu Border Region").
2. 三光部队 "Three-Alls Force" (rendered "Strip-It-Clean Force"): the Japanese scorched-earth slogan
   turned on the corrupt Nationalist takeover officials (anchor "Strip-It-Clean Force").
3. 风萧萧兮: Jing Ke's Yi River parting song (Jing Ke himself covered at ch18) (anchor "The wind blows
   bleak").
4. Du Xinwu (杜心五) and the sworn brotherhoods 洪门 (Hongmen) / 青帮 (Green Gang), 龙头 "dragon head",
   the 大字辈 seniority generation (anchor "Du Xinwu of Cili in Hunan").
5. The "Four Great Dan" (四大名旦) of Peking opera and Cheng Yanqiu's post-1949 leftward turn (anchor
   "Four Great Dan").
6. The "chicken-feather letter" (鸡毛信) urgency-grading of village post, matchstick = most urgent
   (anchor "chicken-feather added").
7. The baojia (保甲) household mutual-responsibility system, the base tier the pacification unit and
   the Communists alike worked through (anchor "baojia office").
8. Moxingling (摩星岭, Mount Davis, Hong Kong) and the 1950 refugee-leftist clash behind Bai Jiaqi's
   piece (anchor "The Battle of Moxingling").
- Zhao Zilong/赵子龙 deliberately NOT noted (Zhao Yun's Changban feat already covered at ch17).
  复兴社/Renaissance Society (Blue Shirts), Wang Kemin, the Double Tenth, the Youth Army, the Green
  Gang's generation ranks, Jing Ke, and the Loyal-and-Patriotic-Army/Luan-Yu HQ furniture all
  already covered and NOT re-noted.

### Glossary (12 net-new keyed rows; add_ch37_glossary.py)
- People (provisional): 常绍曾 Chang Shaozeng (North-Suburb Group leader, three quoted accounts;
  graduated from inline in ch36), 田英杰 Tian Yingjie (the Lishuiqiao "Captain Tian", battle account
  author), 卢德明 Lu Deming (Shimen account author), 刘子元 Liu Ziyuan (Daxing self-defense brigade
  cmdr), 冯玉柱 Feng Yuzhu (successor North-Suburb Group leader), 王抚洲 Wang Fuzhou (Third-Route-Army
  manager, later Taiwan vice-minister), 白家祺 Bai Jiaqi (Lt Col, the Guohun-song author), 杜心吾
  Du Xinwu (the Cili martial-arts master; source spells 心吾 for 心五), 程艳秋 Cheng Yanqiu (the opera
  dan; also 程砚秋).
- Places (decided): 立水桥 Lishuiqiao, 大兴 Daxing, 赵家坟 Zhaojiafen.
- Reused the whole B01-B29 keyed cast and Part-Four vocab. 郑恩普 Zheng Enpu already keyed. INLINE,
  NOT keyed (glossary-key discipline): the Shimen defenders 罗历戎/李文定/刘英/刘清池/赵劲军/侯子固; the
  Communist figures 杨得志/杨成武/刘伯承/杨秀峰/薄一波/黄敬(俞启威); the training roster 钱致伦/王忠/尹东耕/
  阎尚新; the Ninth-Route staff 齐庆斌/张克新/陈肇基/骆永康; the Lishuiqiao-night names 米仁甫/马良知/
  李志达/路焕仲, the grooms 庄飞/杨天铎/张岳生, 王镇吾 (Wang Fuzhou's alt name), 白世维; the villages 望都/
  北湖渠/仰山/昌平/怀柔/北苑/路家坟/勇士营/羊房/白家坟/谢格庄/林南仓/宝坻/玉田/平原/禹城/德州/海淀/门头沟/
  西山/万寿山/八达岭/十三陵 and the Beiping lanes 府学胡同/东观音寺胡同/沈篦子胡同/煤渣胡同/东直门.

### data/noise.txt — B30 additions (7)
- **二十多** (approximate "twenty-odd provinces"; the built-in 多 rule can orphan the leading 二).
- **二流子** (slang "idler/ne'er-do-well", 二). **一两百** (approximate range "a hundred or two apiece").
- **八达岭** (place-name numeral Badaling, 八). **万寿山** (place-name numeral Wanshou Hill, 万).
- **二〇八** (the 208th Division designation; the 〇 mis-read glyph orphans 二/八 — carried "208th
  Division"). **两淡** (idiom 名利两淡 "indifferent alike to fame and gain"; 两 = "both", not the count 2).
- All REAL quantities carried as DIGITS/words: 10,000 / 100,000 / 600,000 / 25,000,000 troops and
  population, the Lishuiqiao counts (three militia brigades ~1,100-odd; 11 dead + 27 wounded local
  corps, 1 dead + 1 missing + 3 wounded assault team; ~30-odd enemy corpses); ROC years 22/26/27/28/
  36/37/38/40 matched by ordinal or +1911; the 0760 unit code and 208th Division carried literally.

### Digitization glitches (rendered to plain sense; none footnoted — mechanical)
- **ch37:** stray ！ standing for a closing 」 (z4 抗日杀奸团！, z90 摩星岭之役！, z79 doubled 。！);
  stray closing/opening presentation glyphs ︸ for 「 (z80 ︸西郊混合组, z130 ︸我一口气) and ⋮ for 」
  (z78 撤销⋮, z127); orphaned 。 heading z92 (the 摩星岭之役 sentence's stop displaced onto the next
  <p>); enumeration-marker glitches in Lu Deming's numbered document — 工/口 for 一/二 (z14/z15),
  凵/| for （一）(z18), 闫 for 三 (z33), 出 for 七 (z38); stray 》 mid-clause (z38 出有甚于此的》); stray
  glyphs 〕(z104), ≥ (z124), | (z128 法宝|), }/| (z81 往事了|}); 。令 for 口令 (z129 dropped 口);
  单-char substitutions 价値/価値 (值), 混身 (浑身, z38), 境丙 for 境内 (z98), 匪一军 (stray 一, z113);
  variant/rare glyphs 鄕 (乡), 覇 (霸), 鬪 (斗), 尙 (尚), 槪 (概), 擧 (举), 楡 (榆), 郞 (郎), 鎗 (枪),
  毘 (毗), 艶 (艳, in 程艶秋), 坁 (坻, in 宝坁), 天家 for 大家 (z77); the 〇 mis-read glyph in the 0760
  unit code (z73/z143) and the 二〇八 Division (z75/z76); x redactions (z54 第x团, 王xx). Many dropped
  。 mid-<p>. All rendered to plain sense; none is a reading uncertainty.

## Batch B31 (ch38 = 第六章 曲直分明 反复无常, the SIXTH Part-Four narrative chapter)

"Chapter 6. Right and Wrong Made Plain, yet Ever Fickle." Four sections: ch38s01 "Had Japan Not
Invaded, None of This Would Have Happened"; ch38s02 "Would That Every Unit Were So Steadfast";
ch38s03 "Or Did the Tide Turn and Their Resolve Fail?"; ch38s04 "For All the Waverings, Magnanimous
Still." The case of Zhu Zhankui (朱占奎), the defector: an anti-Japanese village guerrilla captured by
the Japanese, who escaped, fell in by mistake with Lü Zhengcao's Communists, rose to a subdistrict
command, was purged, went over to He Long/Xiao Ke, was captured by the Nationalists, made a district
commissioner and major-general security commander, worked in concert with Chen's assault team through
1948 in the Beiping-Tianjin-Baoding triangle — and at the end of that year lured the Second Command
Room and the directly subordinate assault team into a "widening of the guerrilla front" that was a
trap, and defected back to the Communists. Built on three long contributed accounts by the assault
team's three successive commanders (Wang Hongzhu, Chang Shaozeng, Wu Chunxiang) plus Wang Zhiyi's
"Story of Zhu Zhankui," framed and annotated by Chen. Closes with the tragedy of the staff officer
Gu Shoulin, who lost his reason in Hong Kong in 1951 and vanished.

### Structure
- drop=2 (running header 英雄无名-陈恭澍 + <h2> chapter title). Byte-exact p-by-p diff against the
  source XHTML: 1 <h2> + 4 <h3> (section heads 一/二/三/四) + 135 <p>, ZERO mismatches; NO <h1>/<br/>/
  <img>/[\d+], 0 images. File has NO trailing newline (141 lines; wc -l counts 140); after drop=2 the
  txt has 139 body lines = 4 <h3> heads (raw 1-based L15/L46/L69/L113) + 135 <p>. standalone=[15,46,
  69,113]. The "1-line count scare" (ch36 pattern) was a trailing-newline miscount, confirmed harmless.
- NO severed-<p> merges. L68 ends 。﹂ (sentence closed inside a closing-quote glyph, terminal). The
  two ！/？-ending candidates are complete terminal sentences, NOT mid-predicate severs (L48 ...你死
  我活！ a rhetorical exclamation; L106 ...打游击的？ a rhetorical question with a stray 分明是圈套）
  paren-glitch). NO ch36-class source-duplication (near-duplicate scan found nothing >0.6; no heading
  text fused mid-<p>).
- 135 body paragraphs. median ratio 5.55 en/han (document/quote-heavy: four contributed accounts).
  Alignment OK (no pair strays >2.2x).

### Checks (all green)
- verify_unit ch38: parity 135/135 OK; numbers 0 unresolved (after the noise additions below);
  anchors OK. check_align: median 5.55, OK. check_structure: ALL PASS (335 notes, 0 unresolved).
- check_content: ch38 178 name occurrences, 1 "DISPLACED" = the DOCUMENTED HOMOGRAPH FALSE POSITIVE
  海防 (paragraph 60): keyed as the place "Haiphong" (Part Two), but here 协力于海防 means "aid in the
  coast defense" (common noun), correctly rendered "coast defense" — softening it to "Haiphong" would
  be WRONG. (Same class as ch26's 武汉卿/劳勃生路 keyed-substring false positives.) The ch08/09/13/26
  lines are the other documented pre-existing artifacts.
- qc_entities: 1 miss = the SAME 海防/Haiphong false positive; otherwise clean (census top: 朱占奎 x73,
  北平 x15, 常绍曾 x15, 贺龙 x13, 汪鸿翥 x13, 王庆沱 x13, 谷守林 x10, 绥靖 x8 — the keyed noun rendered
  "pacification" throughout, NO verb-form drift).
- Tail verified against source (zh138-140: the siege of Beiping / Zhu at Nanyuan; Chen never again
  finding the name in Communist records; the bitter close "took up his old trade again — the blowing
  of the horn" is faithful and complete). check_register --ref: within tolerance (contr 0.0/1k,
  em-dash 7.1/1k, rhythm 0.69; "shall" deliberate). check_apparatus: 0 failures. qa_epub: PASS (38/43
  chapters, 335 notes). epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings / 0 infos.

### Notes (8 new; 335 cumulative) — all first-appearance, none re-noted
1. The "Anti-Japanese University" = the CCP cadre academy Kangda (抗日军政大学/抗大, founded 1936 as
   红军大学); scholarship verdict against Chen's scorn (anchor "Anti-Japanese University").
2. He Long (贺龙, 1896-1969): Red Army founder, Nanchang Uprising, 120th-Division commander, PLA
   marshal; persecuted to death in the Cultural Revolution (corroborating Chen's remark), rehabilitated
   1974 (anchor "bandit chieftain He Long").
3. Xiao Ke (萧克, 1907-2008): He Long's deputy in the 120th Division, full general 1955 (anchor "help
   Xiao Ke").
4. The chuigushou (吹鼓手): the low-status folk shawm-and-drum bandsman of weddings/funerals, the suona
   Chen calls the 喇叭 laba — Zhu's humble trade and the chapter's bitter close (anchor "as a
   chuigushou").
5. 数白嘴 / 流口辙: the rapid rhymed patter of the folk performing arts (kuaiban/xiangsheng), Chen's
   simile for the explosives-recipe jingle (anchor "patter-rhyme of the storyteller").
6. The Eighteenth Group Army / Eighth Route Army (第十八集团军/八路军): the 1937 united-front
   redesignation, the 115th/120th/129th Divisions, the New Fourth Army (anchor "Eighteenth Group Army").
7. The Hanyang rifle (汉阳造, Gewehr-88 copy in 7.9mm, from 1895) vs the Japanese Arisaka Type 38
   (anchor "Hanyang-made").
8. The statecraft maxim 用而不疑、疑而不用 ("employ a man and doubt him not...") and 泱泱大度 (the
   section-4 title, the "grand bearing of a great state") (anchor "employ a man and doubt him not").
- NOT re-noted: the Marco Polo Bridge / Double-Seventh Incident, Yan'an, the Youth Army, the 208th
  Division, the Lizhi Class / Central Training Corps, the Three Principles of the People, the Red
  Guards / Cultural Revolution, tunnel warfare, the Type 38 rifle, He Long's Jiangxi bandit-suppression
  days, the North China Bandit-Suppression HQ, the whole 绥靖/戡乱/共匪 framing — all covered earlier.
  Ren Zhuoxuan (任卓宣) and Xu Foguan (徐佛观), named once as instructors, left inline.

### Glossary (10 net-new keyed rows; add_ch38_glossary.py)
- People: 汪鸿翥 Wang Hongzhu (first assault-team cmdr, section-2 account author), 吴春祥 Wu Chunxiang
  (third assault-team cmdr, section-4 account author), 谷守林 Gu Shoulin (Second-Command-Room staff
  officer, the Hong Kong tragedy) — all provisional; 萧克 Xiao Ke (attested).
- Places (decided): 王庆沱 Wangqingtuo, 杨柳青 Yangliuqing, 独流 Duliu, 静海 Jinghai, 顺义 Shunyi,
  唐官屯 Tangguantun (the Jin-Pu-line theatre towns that recur across sections 2-4).
- Reused the whole B01-B30 keyed cast and Part-Four vocab (朱占奎/常绍曾/李玉林/刘原深/刘培初/郑介民/
  张炎元/吕正操/贺龙/林彪/陶铸/聂荣臻/江田; 绥靖总队/中央训练团/华北剿匪总司令部/平津保三角地带; 绥靖
  "pacification"/戡乱/剿匪/匪谍/共酋/共干; 石家庄/安国/大兴/安次/立水桥/冀东). Settled common-noun
  renderings reused (not keyed): 突击队 "assault team", 直属突击队 "directly subordinate assault team",
  第二指挥室 "Second Command Room", 区队 "district company", 分队 "sub-brigade", 小组 "small group",
  骑兵班 "cavalry squad", 自衞队 "self-defense corps", 打情报 "beating out intelligence" (Chen's jargon).
- INLINE, NOT keyed (glossary-key discipline — one-off account-authors, subordinate/district-company
  officers, one-mention figures/villages): 王志毅 Wang Zhiyi, 董英 Dong Ying, 任卓宣 Ren Zhuoxuan,
  徐佛观 Xu Foguan, 张鲁颖 Zhang Luying, 李长清 Li Changqing, 徐立德 Xu Lide, 杨士毅 Yang Shiyi, 窦玉麟
  Dou Yulin, 张保权 Zhang Baoquan, 贾叔铭 Jia Shuming, 赵濶亭 Zhao Kuoting, 李葆章/李保章 Li Baozhang
  (source spells it both ways), 张侗夫 Zhang Tongfu, 陈俊祥 Chen Junxiang, 任德勤 Ren Deqin, 赵子侠
  Zhao Zixia, 王维宁 Wang Weining, 吴玉林 Wu Yulin, 刘纯熙 Liu Chunxi, 张麟阁 Zhang Linge, 马钟麟 Ma
  Zhonglin, 孙守义 Sun Shouyi, 刘楚枫 Liu Chufeng, 张培植 Zhang Peizhi, 汪鸿骏 Wang Hongjun (distinct
  from 汪鸿翥), 刘伯承 Liu Bocheng, 中野 Nakano; the villages 五重山 Wuchongshan, 白房村 Baifang, 牛栏山
  Niulanshan, 赵家寨子 Zhaojiazhaizi, 王家庄子 Wangjiazhuangzi, 青王庄 Qingwangzhuang, 唐二里/汤二里
  Tang'erli, 昌平/永清/固安/沧县/德县/德州/清河镇/南苑/喜峰口/都山/明孝陵.

### data/noise.txt — B31 additions (8)
- **五、六万** (approximate range "some fifty or sixty thousand"; the built-in 万 rule matches 六万 and
  orphans the leading 五). **六旬** (age idiom "past his sixtieth year", 旬 = a span of ten).
- **三五一** (idiom 三五一簇 "in knots of three and five"; the checker mis-reads 三五一 as the
  positional value 351). **化整为零** (idiom "break the whole into parts"; the 零 = 0). **二门** (the
  architectural "inner gate"; 二 = second gate, not the count 2).
- **唐二里 / 汤二里** (place-name numeral Tang'erli; 二 part of the name; source prints it both ways).
- **一一五** (the 115th Division designation; the checker reads the digit-string 一一五 as the composed
  value 5 rather than 115 — cf. 二〇八; carried "115th Division"; 一二九→129 and 一二〇 parse cleanly).
- All REAL quantities carried as DIGITS/words: force ~3,500 men; the atlas scale "one part in
  3,500,000" and ">200 km" (written as DIGITS since spelled compounds do not compose); 208th Division;
  the assault-team establishment (4 district companies → after / 3, 5 men per group); the Baifang
  haul (48 sacks grain, 6/10 horses); the Wangqingtuo timings (5:40 pm, 9:20 pm, 5:10 am, forty-past-
  five etc. rendered with "past" forms carrying both digits); 12 LMGs + 28 automatic rifles; >120 /
  ~200 / >400 men; ROC years 24/26/30/34/36/37/38/40 matched by ordinal or +1911.

### Digitization glitches (rendered to plain sense; none footnoted — mechanical)
- **ch38:** stray ） standing for a closing paren/」 (z105 分明是圈套）both sides); stray ！ after a
  terminal 。 (z74 撤退。！); stray closing/opening presentation glyphs ︸ heading z34, 〕(z96 会报〕),
  ⋮ for 」 (z97 政治部队⋮), 》 mid-clause (z119 有感情》), 〞/" (z133 陷落"); the 〇 mis-read glyph in
  the 0760 unit code (z117) and 一二〇师; enumeration-marker glitches in the four-point judgment 〇/2/
  囝/困 for （一）（二）（三）（四）(z123-125, rendered (1)-(4)); the | / 叵 dash-glitches (z21 记述如下|,
  z63 队长一职由常绍曾同学接任叵); single-char substitutions 兵不血刄 (刃, z106), 冷不妨 (冷不防, z78),
  比一行动 (此, z79), 军纪岩明 (严明, z72), 刘佰承 (刘伯承, z40), 整䓩 (整枝, z89), 过过来 (dittography,
  z13); variant/rare glyphs 鄕 (乡), 鬪 (斗), 尙 (尚), 刼 (劫), 窰 (窑), 尶尬 (尴尬), 衞 (卫), 濶 (阔),
  彩 for 采 (兴高彩烈); x/% redactions (第x专区, xx县, x月, 九月x日, %月). All rendered to plain sense;
  none is a reading uncertainty. Name-form variants noted: 朱占奎/朱占魁 (same man, inline), 李葆章/李保章
  (same man), 唐二里/汤二里 (same place); 徐佛观 = the philosopher Xu Fuguan (source 佛 for 复), inline.

## Batch B32 (ch39 = 第七章 瞻前顾后 未雨绸缪, the SEVENTH Part-Four narrative chapter)

"Chapter 7. Looking Before and After, Providing Against the Storm." Three sections: ch39s01 "What I
Saw and Did While Clearing the Battlefield"; ch39s02 "A Strategy Revised Again and Again, Still
Without Direction"; ch39s03 "A Loyal Heart Providing for the Whole Unit's Future." Section 1 is Wang
Zhaofen's long account of opening up the First Command Room's work at Zhuoxian (the Zhenmin Herald,
Commissioner Wang Fenggang and the "iron triangle," the mass encoffining of the dead after the
Laishui campaign, and the Zhuoxian "Cleanse-the-Source" movement, with Meng Guangdi's sub-account).
Section 2 is Zhang Luying's account of the Fifth Command Room at Zhangyuan, then Chen's own reckoning
of Fu Zuoyi's vacillating strategy and the destruction of the 35th Army at Xinbao'an and the 11th
Army Group at Zhangyuan, and the failure of Nationalist intelligence. Section 3: the dated Dagong-Bao
chronicle of the summer-1948 collapse, the Nanjing conference and the audience with Chiang ("Be a
nameless hero"), Zheng Jiemin's charge to prepare the "stay-behind work," the compact with Chen
Zhenshan of the Northeast Brigade, and the plan to move the First Brigade south.

### Structure
- drop=2 (running header 英雄无名-陈恭澍 + <h2> chapter title). Byte-exact p-by-p diff against the
  source XHTML: 1 <h2> + 3 <h3> (section heads 一/二/三) + 179 <p>, ZERO mismatches; NO <h1>/<br/>/
  <img>/[\d+], 0 images. File has NO trailing newline (184 lines; wc -l counts 183); after drop=2 the
  txt has 182 body lines = 3 <h3> heads (raw 1-based L15/L61/L133) + 179 <p>. standalone=[15,61,133].
  The "1-line count scare" (ch36/ch38 pattern) was a trailing-newline miscount, confirmed harmless.
- NO severed-<p> merges. Every body line ends on a terminal glyph. All ！/？-ending candidates are
  complete terminal sentences (L11 壮烈成仁！, L36 使人钦敬！, L46 该当如何？, L108 回不到北平了！, L116
  令人肃然起敬！, L129 那还了得！), NOT mid-predicate severs. The L50-L53 run (再就是...如何处理？ / 凵
  就地掩埋？ / 二...？ / 三...？) is an enumerated OPTIONS list (凵=一 glitch, then 二/三), each a complete
  question kept as its own BODY line per parity, rendered (1)(2)(3). NO ch36-class source-duplication
  (near-duplicate scan found nothing >0.6; no heading text fused mid-<p>).
- 179 body paragraphs. median ratio 5.58 en/han (document/quote-heavy: two long contributed accounts
  plus a dated news chronicle). Alignment OK (no pair strays >2.2x).

### Checks (all green)
- verify_unit ch39: parity 179/179 OK; numbers 0 unresolved (after the 7 noise additions below);
  anchors OK. check_align: median 5.58, OK. check_structure: ALL PASS (343 notes, 0 unresolved).
- check_content: ch39 213 name occurrences, 0 displaced ("all in the paired paragraph"). The
  ch08/09/13/26/38 lines are the documented pre-existing artifacts (Shunde/Jize/武汉卿/劳勃生路/海防).
  NOTE: keying 张垣→Zhangyuan was DROPPED — ch08 already renders the same 张垣 as "Zhangjiakou," so
  张垣 is rendered "Zhangyuan" INLINE in ch39 (with the in-text gloss "(Zhangjiakou in Chahar)") and
  logged as a whole-book reconciliation item, not keyed.
- qc_entities: 0 misses (census top: 傅作义 x34, 北平 x34, 绥靖 x22, 涿县 x22, 涞水 x9, 保定 x9, 王兆芬
  x8, 孙兰峰 x8, 张鲁颖 x7). Fixed 1 verb-form 绥靖 ("pacified the locality" -> "carried out the
  pacification of the locality") so the keyed noun appears in the paragraph.
- check_register --ref: within tolerance (contr 0.0/1k, shall 0%, em-dash 6.6/1k, rhythm 0.64).
- Tail verified against source (L183/L184 rendered in full, nothing dropped or invented).
- qa_epub PASS (43 docs, 5564 paras, 343 refs/bodies/backlinks, all links resolve). epubcheck 5.1.0:
  0 fatals / 0 errors / 0 warnings / 0 infos. EPUB now 39/43 chapters, 343 notes.

### Notes (8 new; 335 -> 343 cumulative)
1. City of the Wrongfully Dead (枉死城, the folk-belief underworld quarter for the untimely/violent dead).
2. The Laishui campaign (涞水之役, Jan 1948; the 35th Army beaten, Li Mingding and the army commander
   both suicides; scholarship verdict; foreshadows Xinbao'an).
3. The battle of Xinbao'an (新保安, 6-24 Dec 1948, opening act of the Pingjin Campaign; the 35th Army
   annihilated, Guo Jingyun a suicide; broke Fu Zuoyi's will; "not one survived" is a martyr's
   flourish, many thousands were captured).
4. The intelligence leak (泄密; Fu Zuoyi's HQ penetrated, his daughter Fu Dongju among the sources; a
   scholarship verdict on Chen's suspicion; the deputy chief of staff unidentifiable here).
5. "Be a nameless hero" (Chiang's 作一个无名英雄 = the source of the book's title 英雄无名).
6. The Dagong Bao (大公报 / Ta Kung Pao; the liberal Republican paper; the post-1949 "mouthpiece"
   claim broadly borne out; the surviving Hong Kong edition).
7. The Kanjurwa Khutukhtu (甘珠尔瓦呼图克图; a Mongol reincarnate lama / "living Buddha"; the 呼图克图
   title; his younger brother in the Duolun intelligence group).
8. The "nines" of winter (数九寒天; the nine nine-day periods counted from the winter solstice).

### Glossary — B32 net-new keyed rows (15: 10 people, 5 places)
- People: 王兆芬 Wang Zhaofen (First Command Room, section-1 account author), 张鲁颖 Zhang Luying (Fifth
  Command Room, section-2 account author; graduated from inline in ch38), 陈振山 Chen Zhenshan (Second/
  Northeast Brigade commander), 孟广第 Meng Guangdi (Baoding Group, sub-account author), 鲁英庆 Lu
  Yingqing (35th Army cmdr, Laishui suicide; source glitches 鲁英尘/鲁英屡), 郭景云 Guo Jingyun (35th
  Army cmdr, Xinbao'an suicide), 孙兰峰 Sun Lanfeng (11th Army Group cmdr), 李铭鼎 Li Mingding (division
  cmdr, Laishui suicide), 李中庸 Li Zhongyong (Second-district commissioner), 王凤岗 Wang Fenggang
  ("iron triangle" commissioner). All provisional.
- Places (all decided): 涿县 Zhuoxian, 新保安 Xinbao'an (en carries a curly apostrophe "Xinbao’an" to
  match the reading.md typography — the glossary en was set to the curly form so check_content/qc
  match), 涞水 Laishui, 保定 Baoding.
- Kept INLINE (glossary-key discipline): 王有声/张荫梧/赵伯衡/孙祖义/崔老选/崔万兴/赵百川(=赵明山)/陈凤桐/
  王志毅/白德昭/贡楚格策登/乌瑞山/仁亲道尔吉/孙文良/钟宁寿/楚溪春/何思源/刘瑶章/范汉杰/王云孙/杨予/魏宁;
  the Communist commanders 刘伯承/陈毅/徐向前; 张垣 Zhangyuan (see reconciliation note above). Places
  inline: 宛平/小稻村/望都/易县/多伦/宣化/怀安/沙城/万全/柴沟堡/下花园/通县/丰台/张飞店/南苑/归绥/包头/
  集宁/大同/太原/承德/葫芦岛/长春/济南/开封/唐山/丰润/昌黎/秦皇岛/房山/定兴/满城/大沽口/青岛/香林寺.

### data/noise.txt — B32 additions (7)
- **六神无主** (idiom "out of one's wits"; 六 = the six spirits, not the count 6).
- **赵百川** (person name Zhao Baichuan; 百 = 100 part of the name).
- **崔万兴** (person name Cui Wanxing; 万 = 10000 part of the name).
- **一来二去** (idiom "back and forth"; 二 = part of the set phrase).
- **顚三倒四** (idiom "topsy-turvy"; 三/四 part of the phrase; source prints 顚 for 颠).
- **三心两意** (idiom "of a divided mind"; 三/两 part of the phrase; Fu Zuoyi's vacillation).
- **数九寒天** (idiom "the depth of winter"; 九 = the nine nine-day periods, not the count 9).
- All REAL quantities carried as DIGITS/words: 35th/11th/16th Armies, the columns and brigades and
  regiments of the Deng Wenyi bulletin, ~300,000 (总兵力约三十万), ~70,000 / ~20,000 / ~50,000 (the
  Zhangyuan-Xinbao'an forces), 769 corpses on the first day and >3,000-odd handed over, ~400 vehicles,
  ~20 degrees below zero, 57 spies arrested, ROC years 21/28/34/36/37/38/40 matched by ordinal or
  +1911. The ×-redaction 第x纵队 (L112) rendered as an em-dash blank "the ——th Column."

### Digitization glitches (rendered to plain sense; none footnoted — mechanical)
- Single-char name substitutions: 主兆芬 for 王兆芬 (王兆芬 = Wang Zhaofen, L16); 鲁英尘 (L44/L86) and
  鲁英屡 (L116) for 鲁英庆 (Lu Yingqing, one man); 缓靖 for 绥靖 (L20).
- Dropped-stop / redaction glyphs: 〇 for a missing punctuation (为什么〇, L4); fullwidth ＠ for a stop
  (声名亦渐为人所称道＠, L30); 张家。 with the 。 for a dropped 口 (= Zhangjiakou, L79).
- Stray presentation glyphs standing for a dash/colon or a closing 」: | (下面就是...原文|, L19; 再说几句
  伤心话|, L45; 傅作义的三心两意|, L104/L129), 》(为题》, L66; 副主任》, L81), 〕(涿县时〕, L55; 从张垣一役
  中〕, L104), 〞/" for a closing 」 (在那个时候, L45; 西去包绥", L130), ﹄ mismatched guillemet (一小撮﹄,
  L141), ︴ head-glyph (︴玉林兄, L181).
- Enumeration-marker glitches: 工 for 一 (工我方官兵, L47), 凵 for 一 (凵就地掩埋 L51; 凵因工作态度 L73),
  all rendered as arabic (1). The × redaction 第x纵队 (L112) rendered "the ——th Column."
- Other single-char substitutions: 灭线 for 火线 (firing line, L7); 保一定 for 保定 (Baoding, L19); 联紧
  for 联系 (L66); 福射状 for 辐射状 (L87); 杆了毡 (dialect, "matted into felt," L114). Name-form/place:
  张垣 = the literary name of 张家口 Zhangjiakou (source glosses it 张垣（察哈尔张家口）, L62).

## Batch B33 (ch40 = 第八章 抚今追昔 烟波千里, the EIGHTH Part-Four narrative chapter)

"Chapter 8. Musing on Past and Present, Mist over a Thousand Miles." Four sections: ch40s01 "Three Men
in Step, Each His Own Way, onto Three Roads"; ch40s02 "The Overlooked Arch-Enemy of the North China
Front"; ch40s03 "May You, Steadfast and Striving, Live On There Forever"; ch40s04 "Every Defeat Lost
with Unyielding Regret." Section 1 traces the diverging fates of the three men of the Tianjin
Intelligence Group (Wang Zhibin, who defected to the Communists and vanished in Yang Fan's purge; Guo
Zizhong, deported from Japan; Qi Zhenping, thirty years in the Central Second Section). Section 2 is
Chen's reckoning of Nie Rongzhen as the "number-one adversary" of the North China front, from the
Wutai base and the Hundred Regiments Offensive to the fall of Beiping, framed by the intelligence-
employment thesis (knowing the enemy is nothing without the strength to act) and closed by the seam
obituary of the draftsman Hong Fuyu. Section 3 is the "stay-behind work": recruiting, matériel, and
funds (the gold-yuan collapse, the "Yuan big-head" silver dollar and flour), the martyrdom of Ji
Zhaoxiang, and Chen's bitter account of the foreign-sponsored air-drops into the mainland. Section 4
is the string of defeats: Chiang's autumn-1948 inspections, the Liaoshen collapse, the Xu-Bang
(Huaihai) Campaign, and the Xinbao'an-Miaofeng disaster of the Provisional Third Army, closing on the
Miaofeng temple-fair reverie and the aborted transfer to the North China Bandit-Suppression HQ.

### Structure
- drop=2 (running header 英雄无名-陈恭澍 + <h2> chapter title). Byte-exact p-by-p diff against the
  source XHTML: 1 <h2> + 4 <h3> (section heads 一/二/三/四) + 170 <p>, ZERO mismatches; NO <h1>/<br/>/
  <img>/[\d+], 0 images. File has NO trailing newline (176 lines; wc -l counts 175); after drop=2 the
  txt has 174 body lines = 4 <h3> heads (raw 1-based L17/L31/L71/L127) + 170 <p>.
  standalone=[17,31,71,127]. The "1-line count scare" (ch36/ch38/ch39 pattern) was a trailing-newline
  miscount, confirmed harmless.
- ONE glitch-masked severed-<p> merge=[(96,97)]: raw L96 ends 我问他：﹁要枪做什么？ (opens ﹁, leaves it
  unclosed; the ？ masks the continuation) and raw L97 begins ﹂计同学用他那双湿润的眼睛望望我 - the
  dialogue ﹁要枪做什么？﹂ was split so its closing ﹂ orphaned onto the next <p>. Merge restores
  opens==closes. Every other body line ends on a terminal glyph; the L88-L94 and L168-L169 runs of
  rhetorical questions / the 山里红 aside are each complete sentences kept as BODY lines per parity.
  NO ch36-class source-duplication (near-duplicate scan found nothing >0.6).
- 169 body paragraphs. median ratio 5.37 en/han. Alignment OK (no pair strays >2.2x).

### Checks (all green)
- verify_unit ch40: parity 169/169 OK; numbers 0 unresolved (after the 8 noise additions below);
  anchors OK. check_align: median 5.37, OK. check_structure: ALL PASS (352 notes, 0 unresolved).
- check_content: ch40 125 name occurrences, 0 displaced ("all in the paired paragraph"). Fixed 2
  near-miss rendering mismatches to the keyed forms: 中岛信一 curly apostrophe -> straight "Nakajima
  Shin'ichi" (glossary en uses a straight '); 冀东 "East-Hebei" (hyphen) -> "East Hebei" (space) to
  match the keyed en. The ch08/09/13/26/38 lines are the documented pre-existing artifacts
  (Shunde/Jize/武汉卿/劳勃生路/海防-Haiphong).
- qc_entities: 0 misses (census top: 北平 x22, 聂荣臻 x21, 王智斌 x17, 林彪 x10, 天津 x9, 郭子中 x8, 绥靖
  x7, 新保安 x7). 绥靖 rendered the keyed noun "pacification" throughout (no verb-form drift).
- check_register --ref: within tolerance (contr 0.0/1k, shall 0%, em-dash 8.0/1k, rhythm 0.61).
- Tail verified against source (L174 the Dagong-Bao Youth-Salvation-Corps notice rendered in full,
  nothing dropped or invented).
- qa_epub PASS (43 docs, 5732 paras, 352 refs/bodies/backlinks, all links resolve). epubcheck 5.1.0:
  0 fatals / 0 errors / 0 warnings / 0 infos. EPUB now 40/43 chapters, 352 notes.

### Notes (9 new; 343 -> 352 cumulative)
1. The Hundred Regiments Offensive (百团大战, Aug-Dec 1940; Zhu De and Peng Dehuai; the "Three-All"
   reprisals; Mao's attested disapproval, revived against Peng in 1959; Chen's banditry/jealousy
   reading is the Nationalist framing).
2. Lu Zhishen (鲁智深, the "Flowery Monk" of the Water Margin; Mao's "of old Lu Zhishen, today Nie
   Rongzhen" quip likening Wutai to the outlaw fastness).
3. The Xu-Bang / Huaihai Campaign (徐蚌会战, Nov 1948-Jan 1949; ~half a million Nationalists
   destroyed around Xuzhou; decided the war; Chen's casualty figures of the right order).
4. The Liaoshen Campaign / fall of the Northeast (Jinzhou 15 Oct, Changchun 20 Oct, Shenyang, Liao
   Yaoxiang's army wiped out; freed Lin Biao's army for the Pingjin fighting; Fan Hanjie / Lu Junquan
   taken at Jinzhou).
5. The gold yuan and the silver dollar (金圆劵, the Aug-1948 currency and its collapse; the "Yuan
   big-head" 袁大头 silver dollar bearing Yuan Shikai's head; why agents were paid in flour and silver).
6. The Miaofeng temple fair (妙峰山庙会; the lunar-spring pilgrimage to Bixia Yuanjun's shrine, the
   kowtowing devout, the pilgrim associations; suppressed after 1949, revived recently).
7. The shanlihong / candied haws (山里红 / 糖葫芦; hawthorn 山楂 on a stick; the giant willow-withe
   pilgrim's version vs the refined city tanghulu).
8. Straw dogs (刍狗; the Daodejing "heaven and earth treat the ten thousand things as straw dogs";
   sacrificial effigies used then discarded).
9. The button-knob (顶子, the Qing hat-finial marking rank; "blood that dyes the button-knob crimson"
   = a career bought with subordinates' lives).

### Glossary - B33 net-new keyed rows (4 people; all provisional)
- 王智斌 Wang Zhibin (Tianjin Group leader who defected; also 王紫斌 Wang Zibin), 齐枕萍 Qi Zhenping
  (Central Second Section; written 齐枕平 in ch33/ch35, one man), 郭子中 Guo Zizhong (deported from
  Japan), 洪复予 Hong Fuyu (the brigade draftsman; also in ch35). 王智斌/郭子中 graduated from inline in
  ch33/ch35 (rendered identically there); 洪复予 from inline in ch35 - all render one way across chapters.
- Kept INLINE (glossary-key discipline - one-off Communist officials, one-mention commanders,
  name-lists, courtesy names, one-chapter places): 许建国 Xu Jianguo, 杨帆 Yang Fan (CCP Shanghai PSB
  directors), 廖耀湘 Liao Yaoxiang, 袁朴 Yuan Pu, 吴克华 Wu Kehua, 詹大南 Zhan Danan, 范汉杰 Fan Hanjie,
  卢濬泉 Lu Junquan, 胡轨 Hu Gui, 孙龙光 Sun Longguang, 李复生 Li Fusheng; the Communist commanders 朱德
  Zhu De, 彭德怀 Peng Dehuai, 叶剑英 Ye Jianying, 徐向前 Xu Xiangqian, and Nie's sub-district commanders
  杨成武/郭天民/黄永胜/熊伯涛/邓华; 侯飞霞 Hou Feixia (courtesy name of the keyed 侯腾 Hou Teng, one man);
  张上校 Colonel Zhang. Places inline: 胥各庄/顺义/密云/黄县/哈尔滨/沈阳/太原/集宁/康庄/南口/昌平/怀来/
  镇边城/门头沟/土木堡/宋家营/妙峰山/横岭/八达岭/青龙桥/长春/葫芦岛/锦西/宁波/府学胡同.

### data/noise.txt - B33 additions (8)
- **毫无二致** (idiom "in no way different"; 二 part of the set phrase, not the count 2).
- **百团大战** (campaign name "Hundred Regiments Offensive"; 百 = 100 part of the proper name - the text
  gives the real figures 四十多个团 / 二十多个团).
- **五花八门** (idiom "of every stripe and kind"; 五/八 part of the phrase).
- **七荤八素** (idiom "thrown into a muddle"; 七/八 part of the phrase).
- **九十月** (elided consecutive months 九月、十月; the checker misreads 九十 as the value 90).
- **十一、二日** (elided date 十一、十二; the checker reads the trailing 二 as the count 2).
- **三心二意** (idiom "of a divided mind"; variant of 三心两意 with 二; 三/二 part of the phrase).
- **接二连三** (idiom "one after another"; 二/三 part of the phrase).
- All REAL quantities carried as DIGITS/words: 180,000 garrison / 150,000 conscript laborers /
  460,000 & 304,000 Huaihai casualties / 760,000 total & 230,000 (three-in-ten) dead / 150,000 vs
  40,000 (~7:2) at Xinbao'an / the 35th/16th Armies, columns, brigades, regiments, battalions;
  25,000-li Long March written as digits; ROC years 23-40 matched by ordinal or +1911.

### Digitization glitches (rendered to plain sense; none footnoted - mechanical)
- Stray glyphs standing for a closing 」 / a colon / a stop: ︸ before 清除国民党特务 (L28) and before
  卷头长白 (L105, = a 「); | before 运用情报的力量 (L64); 〕 after 四种之多 (L66); 》 after 补给 (L85) and
  after 三、四月间 (L164); ？ for a stop after 训练下级军政干部 (L38).
- Single-char / variant substitutions rendered to sense: 闚关东 for 闯关东 (L25, "crossed into
  Guandong"); 迂迥 for 迂迴 (L65, "roundabout"); 挢得 for 搅得 (L66, "thrown into a muddle"); 非夷所思 for
  匪夷所思 (L101, "past all thought"); 受赚 for 受骗 (L120, "deceived"); 穴尺 for 六尺 (L166, "five or six
  chi"); 方、面 stray 、 in 平绥路方面 (L144); 金圆劵 (劵 variant of 券, kept as the source form in the note).
- Name variant (NOT a glitch): 王紫斌 = 王智斌 Wang Zhibin ("also named," L25); 齐枕萍 (L17+) = 齐枕平 of
  ch33/ch35, one man (Qi Zhenping). 侯飞霞 = the courtesy name of 侯腾 Hou Teng (L169, one man).
- Redaction: xx公司 (L110, a redacted company name) kept as "XX Company."

## Batch B34 - ch41 (第九章 痛定思痛 来者可追), the NINTH Part-Four narrative chapter

"Chapter 9. Reflecting on Past Pain, the Future Still to Redeem" - the brigade's move south
(Beiping -> Tanggu by ship -> Shanghai -> Shaoxing -> Ningbo -> Xiamen -> Penghu, its
dissolution, Wang Hongzhu's account of the sea passage and the funeral-parlor billet in Shanghai);
the fall of Beiping and Tianjin (Fu Zuoyi's fatal irresolution, the severing of the Beiping-Tianjin
railway, the defense-zone order of battle, the month-long defense of Tianjin and Chen Changjie's
capture, the sea withdrawal from Tanggu, the peace-movement and Fu's surrender through Deng Baoshan);
the besieged-city street scenes of Chen's Beiping (a numbered topic-list: market and daily life,
the currency, the airfields inside the city incl. the Temple of Heaven, the pawnshops, the guns and
the unafraid townsfolk, the markets and temple fairs, the Eight Great Lanes, and a walk across the
whole city); and the final flight out with Zheng Jiemin (the booklet of stay-behind personnel,
the classmate's parting pistol, and Deng Baoshan's no-show at the plane).

- **Structure (CONFIRMED byte-exact p-by-p vs index_split_000_0040.xhtml):** 1 <h2> + 4 <h3>
  (section heads 一/二/三/四 at RAW 1-based L8/L40/L100/L171) + 200 <p>; NO <h1>, <br/>, <img>,
  or [\d+] note markers; 0 images. drop=2. Raw txt = 206 lines (no trailing newline; wc -l 205);
  206 - 2 = 204 body = 4 h3 + 200 p. clean_batch.py spec: drop=2, merges=[], glued/glued_head={},
  standalone=[8,40,100,171]. Source conserved OK. data/zh/ch41.txt = 205 lines (1 title + 4 heads
  + 200 body).
- **NO severed-<p> boundaries** (every body line ends terminal; all ！/？/》-enders verified complete
  sentences whose next line begins anew - L22 噢！, L25 好快呵！, L85 妄想！, L104 四与一吧？, L142
  太平日子吧！, L170 也写不完呵！, L181 生命与前途！). NO glitch-masked severs.
- **Inner enumerations kept as BODY lines per parity** (judged by function): section 3 carries a
  numbered run-in topic-list 一/二/三/四/五/六/七/八 (L104 一、一般市况 fused after the intro colon;
  L113 二、金圆券; L122 三、城内抢修飞机场 fused mid-line after item 二's tail; L134 四、当铺; L138 五、
  炮声; L145 六、市集庙会; L150 七、事理之外; L159 八、走遍全城 fused mid-line), rendered with arabic
  run-in numbers (1)-(8). Item 八 carries sub-items glitched 工/口/曰 for 一/二/三 (L160/L163/L165)
  plus a real 四 (L168), rendered (1)-(4). Section 2 carries unnumbered thematic run-in labels (L62
  以军事为主的天津攻防战, L87 失去存在价値塘沽弃守, L91 围困下的心战政战与统战) and a glitched
  defense-zone roster (L56-L59: 凵/口 for 一/二, （。1/（）2 for the two sub-zones). Section 4 carries
  其一/其二 sub-points (L178/L179).
- **⚠ ch36-class SOURCE-DUPLICATION artifact (ONE, minor):** at L5 (pair 4, the "文件中" document
  excerpt) a running-header/TOC fragment 内容提要第九章痛定思痛来者可追 is fused MID-WORD, splitting
  大军作战 into 大军作[...]战. Rendered to plain sense (restored "In large-army warfare"; the injection
  dropped as a mechanical artifact, NOT footnoted). Near-duplicate scan otherwise found nothing >0.6;
  no whole-paragraph duplication.

### Checks (all green)
- **verify_unit ch41:** parity 200/200 pairs; numbers 0 unresolved (with data/noise.txt auto-found);
  anchors 9 ok.
- **check_align ch41:** 200 source / 200 translation, median ratio 5.37 en/han (in the ch33-ch40
  band); no pair strays >2.2x from median.
- **check_structure (41 units):** ALL STRUCTURAL CHECKS PASS; parity 200/200; anchors 361 notes,
  0 unresolved; headings OK.
- **check_content (41 units):** ch41 = 196 name occurrences, 1 DISPLACED = the NEW documented
  keyed-substring FALSE POSITIVE 河内/Hanoi (河内 = the place Haiphong... no: 河内 Hanoi keyed; here it
  is the substring of 护城河|内墙 "the moat's inner wall" at pair 60). Translation correctly renders
  "moat's inner wall," no Hanoi; translation stands. All other units unchanged (pre-existing ch08 x3,
  ch09 x1, ch13 x9, ch26 x2, ch38 海防/Haiphong x1).
- **qc_entities (reconstructed bilingual):** 1 miss = the same 河内/Hanoi false positive. Census: 北平
  x78, 天津 x40, 傅作义 x26, 塘沽 x17, 林彪 x12, 邓宝珊 x7, 张家口 x4, 陈长捷 x4, 绍兴 x3, 汪鸿翥 x3,
  安春山 x3, 孙兰峰 x3. 绥靖 rendered the noun "pacification" (not the verb); 侯镜如 Hou Jingru clean.
- **check_register --ref reference/B01_frozen.md:** within tolerance (contr 0.0, shall 40% [the
  deliberate narrating "shall," informational], em-dash 6.9/1k vs ref 8.3, rhythm CV 0.60 = ref).
- **Tail verified** against source (pairs 194-200, the Deng-Baoshan-no-show ending): faithful, no
  fabrication.
- **qa_epub:** PASS (43 documents, 5931 paragraphs; 361 note refs / 361 bodies / 361 backlinks; 57
  files, all links resolve). **epubcheck 5.1.0:** 0 fatals / 0 errors / 0 warnings / 0 infos.
- **EPUB now 41/43 chapters, 361 notes.**

### Notes (9 new; 361 cumulative) - first-appearance, NOT re-noted
1. **the Beiping copper-cash system** (铜子儿/大枚/毛票/官钱局) - the tangled subsidiary coinage under
   the silver dollar (the dollar and gold-yuan already noted ch06/ch40).
2. **the Donglaishun** (东来顺) and instant-boiled mutton (涮锅子) - Beijing's famous Hui mutton house.
3. **the Temple of Heaven / Altar of Land and Grain error** - Chen conflates 天坛 and 社稷坛 (two
   different sites); factual correction, source error stays visible.
4. **Hademen** (哈德门/崇文门) - the folk etymology (a foreign general of 1900) vs the actual Yuan-era
   origin; Chen's own self-correction, citing 传记文学.
5. **mixed-grain flour** (杂合面) - poverty staple of coarse grains.
6. **the Eight Great Lanes** (八大胡同) - old Beijing's licensed pleasure quarter near Qianmen; the
   three grades incl. 清吟小班.
7. **the five-colored flag / white-sun flag** (五色旗 / 青天白日满地红) - the two national flags and
   the regime succession (Duan Qirui already noted ch07).
8. **John Leighton Stuart** (司徒雷登) - the US Ambassador; Yenching University; 傅泾波 his secretary.
9. **drawing the firewood from under the cauldron** (釜底抽薪) - the proverb / Thirty-Six Stratagems.

### Glossary - B34 (3 net-new keyed rows, all people, provisional)
- **邓宝珊 Deng Baoshan** - deputy commander-in-chief of the North China Bandit-Suppression HQ, Fu
  Zuoyi's secret negotiating rep, and (proved afterward) the broker of Fu's surrender; the no-show at
  Zheng Jiemin's plane. GRADUATED from inline (rendered "Deng Baoshan" once in ch36).
- **陈长捷 Chen Changjie** - Tianjin garrison commander; refused the break-out to Tanggu, fought a
  month, taken alive.
- **侯镜如 Hou Jingru** - commander of the 17th Army Group; carried out the Tanggu sea withdrawal.
- Kept INLINE (glossary-key discipline): the defense-zone roster commanders 周北峰/李文/骆振韶/袁朴/
  黄翔/李士林/林伟俦/刘云瀚/王治熙/段沄/朱致一; the Qi-Qingbin sub-story kin 张树德/张廷谔/江韵清/江灏/
  江振寰 (rendered as in ch06/ch35: Jiang Yunqing/Jiang Hao/Jiang Zhenhuan); the peace-movement
  name-list 张荫梧/许惠东/何思源/吕复/康同璧/刘鸿瑞/郭树棠; comrades 邹仪/魏宁/林立/毛一鹭/冯志俊;
  one-mention 傅泾波 Fu Jingbo, 司徒雷登 John Leighton Stuart, 李秋生 Li Qiusheng. Places inline:
  上海/绍兴/宁波/厦门/海澄/漳州/澎湖/青岛/太原/大同/杨村/豆张庄/喜峰口/山海关/冷口/唐山/芦台/军粮城/
  张贵庄 and the Beiping gates/landmarks (崇文门/宣武门/天坛/东来顺 etc.). 张垣 -> "Zhangyuan" inline
  (whole-book reconciliation item; ch08 renders it Zhangjiakou). 西直门 Xizhimen keyed (from B33).

### data/noise.txt - B34 additions (8)
- **五、六十万** (elided-tens myriad range "500,000-600,000"; placed BEFORE the shorter 五、六十 rule,
  which would strip 五、六十 and orphan the 万 as 10000 - longest-first).
- **社会百态 -> 百态** (idiom "the myriad forms of society"; 百 = 100 part of the set phrase).
- **大三轮** (counter-by-naming "motor-tricycle"; the 三 names the three-wheeled vehicle. NOT bare
  三轮, which occurs in ch22's 二三轮).
- **四明山** (place-name numeral "the Siming Mountains"; the 四 part of the name).
- **百顺胡同** (place-name numeral "Baishun Lane"; the 百 part of the name).
- **一四〇六 / 一四二〇** (Ming Yongle regnal-year dates 1406 / 1420 printed with 〇 (U+3007); the
  checker cannot read the digit-string - real values carried in English).
- **三〇三** (Biographical Literature issue no. 303 printed with 〇; real value in English).
- All REAL quantities carried as DIGITS/words: 180,000 (Beiping zone) / 150,000 (Tanggu zone) /
  36,000 (Tanggu withdrawal) / 5,000,000 residents / a million (besiegers) / 1,700 & 1,600 m (Temple
  of Heaven perimeter) / 380 & 1,000-odd blockhouses / 9:35 (departure) etc.; ROC years 36-40 by
  ordinal or +1911.

### Digitization glitches (rendered to plain sense; none footnoted - mechanical)
- **ch36-class TOC injection** (see above): 内容提要第九章痛定思痛来者可追 fused mid-word in 大军作战 (L5).
- Stray glyphs for a dash / colon / closing 」: ︸ at head of L28 (万万想不到); | for a dash in
  失去存在价値塘沽弃守| (L87), c|47 (L124, = C-47), 四、当铺开门营业| (L134); |‖ in 一、一般市况...|‖
  (L104); ‖ in 有答案‖ (L156); the roster/list markers 凵/口 for 一/二 (L57/L58) and （。1/（）2 for the
  two sub-zones (L58/L59), 工/口/曰 for 一/二/三 in the item-八 sub-list (L160/L163/L165).
- ！ standing for a closing 」: 接受﹃改编！ (L98), 东单夜市！。 (L146), 与共匪有勾结！ (L200).
- Single-char substitutions rendered to sense: 匪车 for 匪军 (L92, "bandit army"); 一雨天 for 一两天
  (L53, "a day or two"); 李秋生先生天作 for 大作 (L164, "esteemed article"); 摸不着头，脑 stray 、 in
  头脑 (L198).
- Dittography: 毛一一鹭 for 毛一鹭 Mao Yilu (L184).
- ○/〇 (U+25CB / U+3007) redaction/code/date artifacts (real value in English, mis-read glyph noised):
  〇七六〇部队 (unit code 0760, L53); 一〇一军/二〇五师/二〇八师 (unit numbers, L27/L56); 一四〇六/一四二〇
  (Ming years, L127); 三〇三期 (issue no., L164).
- × redaction: 陈xx (a redacted personal name in Zhu Zhankui's loudspeaker call, L53) rendered "Chen
  so-and-so."
- Doubled/stray punctuation: 目前；，(L147). Mismatched guillemets ﹁﹂﹃﹄ pervasive (rendered to sense).
- Name variants (NOT glitches): 邓某 = 邓宝珊 Deng Baoshan; 玉林兄 = 李玉林 Li Yulin; 原深兄 = 刘原深 Liu
  Yuanshen; 鲁颖兄 = 张鲁颖 Zhang Luying; 介民先生 = 郑介民 Zheng Jiemin; 老齐 = 齐庆斌 Qi Qingbin.

## Batch B35 - ch42 (第十章 落叶归根 善其始终), the TENTH and LAST full Part-Four narrative chapter

"Chapter 10. Fallen Leaves Return to the Root, Seen Through to the End" - the disbanding of the
Pacification Corps and the diaspora of its men. Section 1: Chen's own leave-taking (the last visit
to Jiang Tian and Zhang Zuoxing, who stay and are killed/sentenced in the 镇反 campaign; the near
carbon-monoxide death at the Nanjing Central Hotel; the reorganization into the Youth
National-Salvation Corps that pushes him out; the drifting, stock-gambling weeks in Shanghai; the
passage to Taiwan). Section 2: the withdrawal of the stay-behind men from besieged Beiping - Zhang
Luying's contributed account (the fight for aircraft through Li Haokun, the Temple-of-Heaven flight
to Qingdao) and Liu Yuanshen's supplementary account (Chen's parting with Zheng Jiemin's overfull
plane, the anarchy of the "political entry into the city," Fu Zuoyi's unused "Tianxiong" plane).
Section 3: the southward journey guarding Chiang's home region - the contributed accounts of Wang
Hongzhu (护衞先总统蒋公故鄕 / 闽南剿匪), Feng Zhijun (小灵峰衞戍记, the Xiaolingfeng garrison, the louse
in the ear, Chiang glimpsed on a mountain-chair), Xiao Runyu (我部南调情形, the Hengchun's broken
propeller), and Wu Chunxiang (the Lindun night action, the disbanding at Penghu). Section 4: Chen's
post-1949 course - Liu Peichu's gift of gold, the unnamed "great power" cooperation out of Hong Kong,
the Japan mission using former Japanese officers, the chief-of-Second-Section post, the
two-hundred-man reunion, Li Yulin as Penghu magistrate; and the ring-composition close.

- **Structure (CONFIRMED byte-exact p-by-p vs index_split_000_0041.xhtml, 0 mismatches):** 1 <h2> +
  4 <h3> (section heads 一/二/三/四 at RAW 1-based L13/L64/L105/L161) + 201 <p>; NO <h1>, <br/>, <img>,
  or [\d+] note markers; 0 images. drop=2. Raw txt = 207 lines (no trailing newline; wc -l 206);
  207 - 2 = 205 body = 4 h3 + 201 p. clean_batch.py spec: drop=2, merges=[(9,10)], glued/glued_head={},
  standalone=[13,64,105,161]. Source conserved OK. data/zh/ch42.txt = 205 lines (1 title + 4 heads +
  200 body).
- **ONE glitch-masked severed-<p> boundary at (9,10):** L9 ends ...牺牲、尽职！ and L10 begins 之外，书中
  也有... - the bound postposition 之外 ("besides X") cannot begin a sentence, so the source broke one
  clause (...尽职之外，书中也有...) across two <p> with a spurious ！ masking the split. Merged. All other
  ！/？/》-enders verified complete sentences whose next line begins anew (incl. L97 颂扬伟大！/以下是原深
  兄的补述 and L144 顺逆可知矣！/﹁离船登岸, both contributed-account intros, NOT severs).
- **DELIBERATE authorial RING COMPOSITION (NOT a duplication artifact):** the final section opens
  (L3-L9) with a prose appraisal of the Pacification Corps and closes (L201-L207) by restating it as
  an enumerated 一/二/三 list, bracketed by the identical sentence L8 == L206 (笔者忝为其中之一员...) and
  the near-echo L9 =~ L207 (全般事迹...笃实、忠勇、牺牲、尽职). Both kept and translated faithfully
  (rule 4); L8/L206 rendered identically in English. NO source-injection run (grep 内容提要/第十章/落叶
  归根 mid-<p> = none).
- **Inner enumerations kept as BODY lines per parity** (judged by function): section 1's three-point
  self-reflection (L54/L55/L56 一/二/三) and section 4's closing appraisal (L200/L201/L202 一/二/三)
  rendered "First/Second/Third." The stay-behind decision-points (L73/L74/L75) and recollection-points
  (L83/L84/L85) carry the glitch enumeration markers 川/口/囝/〕2/30 for 一/二/三 and are rendered
  (1)(2)(3).

### Checks (all green)
- **verify_unit ch42:** parity 200/200 pairs; numbers 0 unresolved (with data/noise.txt auto-found);
  anchors 10 ok.
- **check_align ch42:** 200 source / 200 translation, median ratio 5.27 en/han (in the ch33-ch41
  band); no pair strays >2.2x from median.
- **check_structure (42 units):** ALL STRUCTURAL CHECKS PASS; parity 200/200; anchors 371 notes,
  0 unresolved; headings OK.
- **check_content (42 units):** ch42 = 167 name occurrences, ALL IN THE PAIRED PARAGRAPH (0 displaced),
  after aligning three keyed near-misses to the glossary: 张作兴 -> named "Jiang Tian and Zhang
  Zuoxing" (was elided as "the two of them"), 乌兰华 "Wulanhua" -> "Ulanhua" (the keyed form), 中岛信一
  curly -> straight apostrophe "Nakajima Shin'ichi." Other units unchanged (pre-existing ch08 x3,
  ch09 x1, ch13 x9, ch26 x2, ch38 海防/Haiphong x1, ch41 河内/Hanoi x1; the 6 new place keys added
  occurrences to ch38/ch41 but NO new displacements).
- **qc_entities (reconstructed bilingual):** 0 misses (fixed 1 verb-form: 绥靖 in the title 闽南剿匪、
  绥靖地方 rendered the noun "Pacification of the Land," not the verb "Pacifying"). Census: 北平 x34,
  绥靖 x16, 澎湖 x15, 江田 x12, 郑介民 x10, 张作兴 x9, 绍兴 x8, 马公 x7, 绥靖总队 x7, 溪口 x6, 汪鸿翥 x6.
- **check_register --ref reference/B01_frozen.md:** within tolerance (contr 0.0 = ref, shall 0%,
  em-dash 8.0/1k vs ref 8.3, rhythm CV 0.56).
- **Tail verified** against source (pairs L200-L205, the ring-composition close): faithful, no
  fabrication; L204 identical to the opening L8 rendering, L205 mirrors L9 with the source's small
  variation (同学同志们 "students and comrades" vs 全体同学们 "all the students").
- **qa_epub:** PASS (43 documents, 6130 paragraphs; 371 note refs / 371 bodies / 371 backlinks; 57
  files, all links resolve). **epubcheck 5.1.0:** 0 fatals / 0 errors / 0 warnings / 0 infos.
- **EPUB now 42/43 chapters, 371 notes.**

### Notes (10 new; 371 cumulative) - first-appearance, NOT re-noted
1. **the Suppression of Counter-Revolutionaries** (镇压反革命 / 镇反) - the 1950-51 mass purge of
   ex-Nationalists; where Jiang Tian was shot and Zhang Zuoxing sentenced.
2. **Tilanqiao** (提篮桥) - Shanghai's Ward Road Gaol; Chen's "fellow inmate in trouble" points back
   to his own imprisonment.
3. **the 万岁/万税 pun** - the wall-slogan 民国万税 "ten thousand taxes for the Republic," twisting the
   cheer 万岁 "long live."
4. **孤臣孽子** - the Mencius (7A.18) allusion in Hu Gui's "Letter to All Comrades."
5. **Xikou and its landmarks** (溪口 / 武岭大门 / 妙高台 / 千丈岩 / Chiang's birthplace) - Chiang's
   native town, the brigade's charge in 1949.
6. **Shaoxing yellow wines** (花雕 / 陈绍 / 黄酒) - the aged rice-wines the young soldiers slipped out
   to drink.
7. **the spirit-medium boy** (乩童 / jitong) - the Southern Fujianese/Taiwanese trance-medium.
8. **the Tangshan earthquake** (唐山大地震, 28 July 1976) - why Chen reckons Zhang Zuoxing's chances
   "more ill than good."
9. **the recruited Japanese officers** (白团 Baituan; 根本博 Nemoto Hiroshi at Kinmen/Guningtou; 和知鹰二
   Wachi Takaji) - the ROC's post-1949 turn to former occupation officers.
10. **the unnamed "great power"** (某一大国) - the US/CIA reading of Chen's Hong Kong cooperation, via
    the date, the arrangement, and CAT (Civil Air Transport, CIA-bought 1950).

### Glossary - B35 (6 net-new keyed rows: 1 person + 5 places)
- **冯志俊 Feng Zhijun** (person, provisional) - GRADUATED from inline (a one-mention comrade in ch41);
  the first-person author of the 小灵峰衞戍记 that anchors section 3.
- **溪口 Xikou / 奉化 Fenghua / 小灵峰 Xiaolingfeng / 澎湖 Penghu / 马公 Magong** (places, decided) - the
  five places central to the southward journey and the guarding of Chiang's native place; each renders
  one way across every chapter it appears in (verified vs the other chapters' data/zh and reading.md;
  no cross-chapter conflict, no new check_content displacements).
- Kept INLINE (glossary-key discipline - one-mention men, name-lists, one-passage figures, standard
  places): 江田 Jiang Tian, 陶铸 Tao Zhu, 李运昌 Li Yunchang, 李鸣秋 Li Mingqiu, 聂恩俊 Nie Enjun, 白世维
  Bai Shiwei, 孙时林 Sun Shilin, 何思源 He Siyuan, 刘不同 Liu Butong, 李浩昆 Li Haokun, 吴尙游 Wu Shangyou,
  胡轨 Hu Gui, 梅长龄 Mei Changling, 马寿泉 Ma Shouquan, 黄文炳 Huang Wenbing, 李良荣 Li Liangrong, 乌瑞山
  Wu Ruishan, 汤恩伯 Tang Enbo, 李振清 Li Zhenqing, 孙文良 Sun Wenliang, 唐纵 Tang Zong, 韩尙英 Han Shangying,
  曹霄青 Cao Xiaoqing, 渡边渡 Watanabe Wataru, 和知鹰二 Wachi Takaji, 根本博 Nemoto Hiroshi, and the
  Xiaolingfeng roster (刘迈青 etc.). Places inline: 上海/南京/杭州/宁波/绍兴/厦门/漳州/泉州/长泰/岩溪/林墩/
  青岛/基隆/台北/台中/香港/东京/北投/跑马地/惠安/高雄/白沙/蒋家 Jiangjia. 乌兰华 -> "Ulanhua" (keyed form
  from 北国锄奸 ch04). 张垣 stays the whole-book reconciliation item.

### data/noise.txt - B35 additions (8)
- **坐六望七** (idiom "in one's sixties"; 六/七 not counts) and **火冒三丈** (idiom "in a blazing rage";
  三 not a count).
- **几两金子** (measure "several taels of gold"; 两 = tael after non-numeric 几, misread as 2) and
  **两黄金** (residual after the existing 三、五十 rule strips 三、五十, orphaning 两 in 三、五十两黄金).
- **千方** (residual after the existing 百计 rule strips 百计, orphaning 千 in the idiom 千方百计).
- **千丈岩** (place-name numeral "the Qianzhang Rock waterfall" at Xikou; 千 part of the name).
- **30搭机** (glitch enumeration marker "30" for the run-in ordinal 三/(3)).
- **十x日** (date with the ones-place day-digit redacted, 三十七年十二月十x日; the checker reads a phantom
  10 - rendered em-dash blank).
- All REAL quantities carried as DIGITS/words: nearly 200,000 (Beiping garrison), some fifty
  (stay-behind party), six / several taels of gold, ten Yuan big-heads, more than two hundred
  (reunion), fifteen li, sixteen ridges, nine machine guns, sixty-odd islands; ROC years 21-76 by
  ordinal or +1911.

### Digitization glitches (rendered to plain sense; none footnoted - mechanical)
- Spurious ！ masking the L9/L10 sever (尽职！之外, see Structure). Dropped 。 (run-ons): 毫无人性|三十七年
  十二月 (L10), 临刑前的一刹那|张作兴 and 无产阶级出身...|结果 (L27), 那一大家子人呢〇 (L162, 〇 for 。).
- Stray glyph for a colon | : 平实的结论应该是|构想 (L3), 清楚的知道| (L44), 所记的槪略| / 其文照录如下|
  (L113), 原文如下| (L116/L139).
- Stray glyph for opening/closing 「」: ︸ for 「 in 只说了一句︸不如先去台湾 (L47); ！ for 」 in 设计委员！
  (L163), 大陆工作处！ (L175); ？ for 。 in 政工大队？ (L158); ﹃ for 」 in 绥靖总队﹃至此结束 (L158);
  《 for 。 in 齐聚在台湾《三十八年 (L47); ⋮ stray in the slogan list (L99).
- ︼ for 一 in ︼架银色飞机 (L100). M】 for M1 in 大八粒 M】半自动步枪 (L134).
- Illegible/redacted: 打倒猼猚獽 (three corrupt glyphs for the slogan's target, L99, rendered "Down with
  so-and-so"); 〇七六〇 = unit code 0760 (L27, 〇 mis-read); 十x日 (redacted day, L139); %月 (redacted
  month, L154); 蒋xx (redacted name, L177); x君 (redacted kinsman, L98).
- Single-char substitutions rendered to sense: 重马费 for 车马费 (L163, "carriage allowance"); 稍了一个
  口信 for 捎了 (L164); 书伏夜出 for 昼伏夜出 (L127, "lying up by day").
- Mismatched presentation-form guillemets ﹁﹂﹃﹄ for 「」『』 pervasive (rendered to sense).
- Name/title variants (NOT glitches): 良顺兄/连良顺 = 连谋 Lian Mou; 张炳华 = 张炎元 Zhang Yanyuan; 郑三爷
  = 郑恩普 Zheng Enpu; 兆芬 = 王兆芬 Wang Zhaofen; 鲁颖兄 = 张鲁颖 Zhang Luying; 原深兄 = 刘原深 Liu Yuanshen.

## Batch B36 - ch43 (英雄无名 篇后续话, the Afterword) + WHOLE-BOOK COMPLETION - THE LAST BATCH

**BOOK COMPLETE: 43/43 chapters, 375 notes, qa_epub PASS, epubcheck 0/0/0/0.**

### ch43 structure
- src 44_index-split-000-0042.txt. drop=2 (running header 英雄无名-陈恭澍 + <h2> title). NO sections
  (no <h3>) -> book.json ch43 has NO `sections` array; reading.md = `## title_en` + body paragraphs.
- **The 31-vs-32 count question RESOLVED:** byte-exact p-by-p diff vs the XHTML showed 1 <h2> + 32 <p>,
  but the LAST <p> is EMPTY (the extractor drops it) -> 31 NON-EMPTY <p> == 31 body lines, a clean 1:1
  match. NO severs (every body line ends terminal), NO glued, NO standalone, NO merges, NO source-injection
  (内容提要/篇后续话 scan clean; near-duplicate scan clean). 0 images (grep <img> = 0). No [\d+] markers.
- clean_batch source-conservation OK. 31 body paragraphs.

### ch43 translation & checks
- Chen's grave reflective register (the narrating "shall" DELIBERATE, preserved). median ratio 5.43
  en/han (reflective coda, higher than narrative band, like the ch32 preface; alignment is the gate).
- verify_unit: 31 pairs, 0 unresolved numbers, 3 anchors ok. check_align: 31/31, no pair strays >2.2x.
- check_content: ch43 7 name occurrences, 0 DISPLACED. qc_entities: 0 misses (传记文学 x3, 罗敬 x2,
  制裁 x2, 绥靖 x1 [in the Part-Four book title], 河内 x1 [in the Part-Two book title], 刘绍唐 x1,
  刘原深 x1 - all align to glossary). check_register: within tolerance. TAIL (the book's last words)
  verified explicitly vs source - faithful, complete.
- **NO new noise rules needed** (all numbers resolved: the five-book enumeration 1/2/3/4/5, the
  ordinals second/third/fourth/fifth, 十年/七年/八年/五本, ROC years - all traced).

### ch43 notes (3 net-new; 375 cumulative) & glossary (1 net-new row)
- 3 notes: (1) the five-books editorial enumeration reconciled to the four Parts of this collection
  (book 4 抗战后期反间活动 "Counter-Agent Work..." is Chen's separate volume, not carried as a Part);
  (2) 刘绍唐 Liu Shaotang, publisher of Biographical Literature, met/thanked for the first time;
  (3) 大中至正 "the great, the central, and the utterly upright", the classical closing ideal (the
  arch at the Chiang Kai-shek Memorial Hall), on which the book's last argument turns.
- 1 glossary row: 刘绍唐 Liu Shaotang (people, decided). NOT re-noted: 制裁/sanction, 军统/保密局,
  戴雨农 Dai Li, the ROC-year system, the five-part memoir structure, 特务/tewu, 传记文学.
- Digitization glitches (rendered to sense, none footnoted - mechanical): L1 glitched book-enumeration
  markers 丨/2/3/囡/同 for 一/二/三/四/五; L3 mismatched ﹃...﹂ and a stray ？ for a closing 」
  (自传﹂？); L6 安享余—年 (stray — in 余年); L22/L25 ﹁特务！ (stray ！ for a closing 」); dropped 。
  stops (园地|这; 之处|过去; 关联|所以; 前题 for 前提); pervasive ﹁﹂﹃﹄ for 「」『』.

### WHOLE-BOOK COMPLETION (CLAUDE.md "Definition of done")
- **Clean TOC 43/43** (no pending placeholder), coverage complete. qa_epub PASS (57 files, 50 docs,
  375/375/375 note refs/bodies/backlinks). epubcheck 5.1.0: 0 fatals/errors/warnings/infos.
- **check_reconcile + reconciliation applied:**
  - **Spelling locale unified to AMERICAN** (was 736 American vs 38 British across curated pairs).
    scripts/normalize_spelling.py cascaded 26 tokens across prose + note bodies + glossary bodies
    (theater/honor/color/center/meter/defense/gray/organize/practice/marvelous/favor/labor/neighbor),
    proper-noun-safe (no Labour Party / surname Grey / proper Centre-Honour). Re-check: 0 British /
    774 American.
  - **张垣/张家口 reconciled:** both are Kalgan; source uses both names. Now 张垣 -> Zhangyuan and
    张家口 -> Zhangjiakou uniformly (the lone ch08 张垣, previously collapsed to "Zhangjiakou", aligned
    to "Zhangyuan"), with a first-appearance city note at ch08 (Zhangjiakou/Kalgan + the literary name
    Zhangyuan). 张垣 -> Zhangyuan now keyed; check_content shows NO new displacement (ch08 still 3
    Shunde FPs, ch41 still 1 河内 FP).
  - **~20 decided renderings grep-counted**, single renderings + first-appearance notes confirmed
    (the Juntong 72/ch04, Baomiju via ch04 note, Dai Li 33/ch02, Pacification Corps 75/ch32, Wang
    Jingwei 195/ch03, Three Principles 25/ch05, Whampoa 18/ch05, Biographical Literature 9/ch18).
- **Deep audit** (out/deep_audit.md): fixed-seed (43) sample of 45 pairs (0.7%) read vs source;
  44/45 fully faithful, ZERO substantive errors; 1 title nuance fixed (ch07 何部长（军分会代委员长）:
  "acting deputy chairman" -> "acting chairman of the Military Branch Council", 代委员长 = acting
  chairman). Bounds the rate below ~6-7% at 95% (not zero); sits atop whole-population scripted checks.
- **authority.json fed back** (scripts/feed_authority.py) under slug `nameless-heroes`: 399 new
  cross-book terms, 43 agreements with prior books, 1 flagged disagreement (宋子文 "Song Ziwen" pinyin
  vs the shelf's "T. V. Soong" - honest `reconcile`; NH glossary note already bridges to T. V. Soong).
- **out/term_ledger.md** written (decided/attested renderings by category with whole-book counts;
  provisional list appended). **COMPLETION.md** written. **HANDOFF.md rewritten to COMPLETE.**
- **Findings left for the commissioner (documented, not silently changed):** 宋子文 pinyin-vs-Soong;
  制裁/sanction used from ch02 but formally defined in the ch04 note (ch02 uses transparent from
  context). Provisional romanizations (241 people / 19 places / 5 orgs) remain to firm up.

## R1 (ch06) — register revision pass, EXEMPLAR batch

Scope: ch06 only, English-to-English register edits per REVISION_PLAN.md §3
(T1–T6) and §5. Content frozen; **406 edits + 1 note-anchor move** applied via
`edits/ch06_edits.md` + `apply_edits.py` (every OLD verified unique,
sequential application simulated before every real run; the reading file was
re-derived from the pristine text on each amendment so the edits file remains
the single source of truth). The 406 comprise the main sweep (~254), a
chain-split/straggler round (~12), and the blind-critique fold-in (~140).

### Tic battery, before → after

| class | before | after |
|---|---|---|
| T1 besides (adverbial, approx) | 15 | 12 |
| T1 thereupon/whereupon | 1 | 1 |
| T1 wont/no-wish/made-bold/still-less | 2 | 0 |
| T1 day-month dates | 5 | 1 |
| T2 could not but / could only | 6 | 1 |
| T2 cannot/could-not help | 1 | 1 |
| T2 pivots (namely / that is to say) | 4 | 0 |
| T2 gerund-of nominalizations | 6 | 5 |
| T2 litotes (no small/no few) | 6 | 0 |
| T3 quoted terms (straight pairs) | 304 | 184 |
| T5 contractions | 0 | 3 (line count) |
| T6 impersonal one + modal | 20 | 7 |
| T4 semicolons | 247 | 250 |
| T4 sentences >60 / >90 words | 41 / 7 | 32 / 5 (mean 26.3 → 25.2 wps) |

### Surviving hits, defended (the battery is a flag, not a verdict)

- **besides 13:** every survivor is prepositional ("besides reporting it",
  "besides manpower") or postpositive ("a jangling call-bell besides") —
  the counter is approximate; the killed class was the sentence adverb.
- **thereupon 1** and **day-month date 1** ("26 February 1932"): both inside
  quoted documents (the Chronicle passage p058, Dai Li's own account p063) —
  exempt by §3.1.
- **could only 1** (p146 "I could only write a little at a time, by stealth
  and in scraps") and **could not help 1** (p280 "one could not help lending
  an ear"): both natural English in context; p280 sits inside Chen's
  unwritten-rule maxim, an essayist coda the KEEP list protects.
- **gerund-of 5:** "at the urging of the", "the wording of the slogans",
  "the parting of the ways" (idiom), "at the founding of the work", one in a
  quoted document — all natural or exempt.
- **impersonal one 7 (grep lines):** three are false positives ("no one
  dared/could"); the real survivors are p051 (思过半矣, Chen's deliberate
  classical allusion), p073 (the recruiter's quasi-official speech, T5
  CAUTION), p117 and p280 (essayist codas, KEEP list). Thinned 20 → ~4 real,
  roughly the plan's two-thirds.
- **semicolons 250 (247 before):** nine chain-staples were split (p021,
  p045 ×2, p056, p113, p138, p148, p164, p215, p316); the offsetting
  additions are list semicolons in the p217 gezi run and balanced pairs.
  Chains of ≥2 semicolons in narration now: p018 (name roster, list-exempt),
  p086 (deliberate parallel triple), p217 (list), quoted documents. The
  book-wide halving target is a narration-chain target, not a raw count.

### T3 policy applied (the biggest visible change)

Recurring decided terms whose first use and gloss note live in ch01–ch05
(Juntong, Lixingshe, Special Services Department, Beiping Station, Bureau of
Investigation and Statistics, Second/Sixth Department, Intelligence Section,
the Association family, Tianjin Station, secret-service work, Legation
Quarter, plus in-chapter repeats of gezi, Siwei Society, Art Academy) went
plain throughout ch06: 304 → 185 straight pairs; the residue is quoted
documents, dialogue, naming constructions ("X for short", "was named X",
name-as-name), anatomized words, marked irony, and ch06 note-anchor sites.
NOTE-ANCHOR: the 「四维学会」 note's anchor `the "Siwei Society"` had in fact
been matching the p296 mention (the p295 naming site has the period inside
the quotes); it now anchors on `named it the "Siwei Society."` at the naming
itself. All 24 ch06 anchors verified post-apply.

### Checks

- `verify_unit.py ch06`: parity 322/322, numbers 0 unresolved, 24 anchors ok.
- **noise.txt additions (both non-quantities, documented in the file):**
  五官 (facial-features idiom — its 5 had been spuriously "accounted" by a
  month-May match on the old wording "it may be"); 四个大字 (meta-linguistic
  character count, same class as the existing 两个字 rule).
- `check_align.py ch06`: OK, median 4.53 en/han, no pair strays >2.2x.
- `check_content.py --config checks.json`: ch06 clean (216 name occurrences,
  all in the paired paragraph). The displaced hits elsewhere (ch08 ×3, ch09,
  ch13 ×9, ch26 ×2, ch38, ch41) are exactly the known-benign list in
  REVISION_PLAN.md §2 — no new displacement.
- **Tail check:** p318–p322 re-read against zh clause by clause — dates, the
  sanction order, the full periodic sentence with all epithets, Itagaki,
  the "mutiny"/"coup" pair, Bai Shiwei: nothing dropped, nothing added.
- **Spot-audit:** fixed seed 20260822, 21 of 203 edited paragraphs (10%+)
  read zh-against-en in full (p001, 012, 031, 055, 062, 068, 099, 113, 147,
  154, 161, 204, 210, 218, 236, 246, 255, 260, 282, 288, 315): ZERO
  meaning-drift defects. Zero in 21 proves the edit-induced error rate is
  below ~14% (rule of three), not zero.

### Fidelity corrections found during the aligned read (source-driven, logged)

- p091 各言其是 — old EN said the sections "each going its own way"; the
  phrase means THE ACCOUNTS DIFFER. Corrected.
- p154 三度莅临 — old EN "the Leader came three times [on graduation day]";
  corrected to "for the third time the Leader came" (opening p111 + mid-course
  visits p094 make graduation his third address; the old reading was
  impossible on its face).
- p170 戴笠处长 — old EN promoted Dai Li to "Bureau Head"; he was head of the
  Second DEPARTMENT (处长). Corrected.
- p197 东洋味 — "an Eastern flavor" → "a Japanese flavor" (东洋 = Japan; the
  sentence is a pointed observation about Wang Tianmu's rooms).
- p191 捉襟见肘 — the old line carried an invented image ("patching the elbow
  only tore the shoulder"); restored the real one (straighten the lapel and
  the elbow shows).
- p277 一显身手 — "showing his hand" (= revealing secrets, the opposite) →
  "show what he could do"; p263 谈情说爱 — "making love" (dated sense trap) →
  "courting"; p253 斜面 — "on the slant" → "diagonally opposite"; p088
  人力车 — "man-pulled cart" → "rickshaw"; p121 "XiangguSi studio" →
  "Xianggu Temple studio"; p211 迁走 — the landlord wasn't moving out, the
  telephone wasn't being moved away.

### Flagged for R13 reconciliation (NOT changed in R1; glossary-forward class)

- 保密局: glossary decides "the Baomiju," but ch04 and ch06 read "Bureau of
  Confidential Investigation" while ch33–ch35 use "Baomiju." One rendering
  must win book-wide; a ch06-only change would just relocate the
  inconsistency.
- "storey/storeys" survives in ch06 ×3, ch17 ×2, ch18, ch24 ×2, ch30, ch41 ×3
  despite the B36 American-spelling pass (not in its curated pairs). Fix
  book-wide in R13.
- 政治运用 rendered "political operation" in ch06 (was the calque "political
  use," ch06-only term) — confirm no other chapter carries "political use."

### Setup note

- setup.sh regression: the ONE known false alarm ("hook stands down on
  template stub") still fails as documented (PROGRESS lines 153, 892); all
  other checker regression tests green.

### Blind critique (plan §5 step 6) and adjudication

The revised chapter went, alone and unsourced, to a context-blind reader
with the plan's verbatim prompt. It returned **493 numbered findings**
(archived verbatim at `edits/ch06_blind_critique.md`). Adjudication:

- **ACCEPTED: 147 findings → ~140 edit blocks** (each block's WHY cites its
  critique number). The accepted classes, in priority order:
  1. **Wrong-meaning idiom calques** — the highest-value catches: "for his
     sake" for 为了他的事 (over his case), "in good part" for largely,
     "showing his hand" already fixed, "palm of his hand" for the
     back-of-the-hand idiom, 刮地皮 rendered as farming, "cracked the case"
     for a crime that never happened, 这一关 as "barrier," 不着边际 as
     "wide-of-the-mark" (evasive, not inaccurate), 这也难说 as "hard to say."
  2. **Outright grammar breaks** — "showed very unnatural," "we ended every
     one of us," "was a small plank-built side room each" (first sweep),
     "pressed me to a meal out" (my own), "the Mr. Zheng Jiemin present"
     (first sweep), "he was assistant of," dangling participles ("Hearing
     that...", "Checking the dates...", "Repenting his former errors...",
     "on inquiring..."), broken antecedents (buyer/stallkeeper, "it was hard
     to mend"), tense slips (present erupting into memoir at p151, p165,
     p217, p269, p314-first-sweep).
  3. **Collocation errors** — "steeped in a temper," "high grounding,"
     "listened sharply," "carried a pride," "burrs were thick."
  4. **Redundant doublings** — in fact/indeed, usually/normally, ever
     after/year after year, whole/unanimous, thus/as a matter of course,
     around the clock/twenty-four hours a day.
  5. A handful of dialogue naturalizations consistent with the §3.4 voice
     sheets (Chen with friends contracts; Dai Li's farewell and report
     remarks lose their starch, keep their brevity).
- **REJECTED: 346 findings, by class, with the reason as the record:**
  - **Chen's persona and the KEEP list** (the largest class): 笔者 "the
    writer," the humility formulas (dare not warrant / respectfully await
    guidance / will not presume to guess), "in person / by his own hand,"
    the topic frames (as for / to speak again of), the reflective codas and
    rhetorical questions, "the higher-ups" (上级, consistent term), the
    intensifiers the source itself carries. The blind reader calls this
    "the single loudest source of translationese"; the plan calls it Chen
    (§3.1: modulate, never raze). This is the calibration question for the
    commissioner at the gate.
  - **The author's own irony and marked terms:** scare quotes on 「谋杀」
    (murdered), 「托付」 (entrusting), the 「一鸣惊人」/「不同凡响」 double
    chengyu, "foreign goods" for 洋货 applied to texts, the 酒肉朋友
    argument, "periphery of the core" (外围 is the org-speak term of art).
  - **Quoted documents and quasi-official speech** (the Chronicle, Dai Li's
    account, the magazine passage, the recruiter's slogan-catalogue, Zheng
    Jiemin's numbered principles): exempt by §3.1, wholesale.
  - **Source-carried doubling and structure:** paired proverbs the source
    itself pairs (顾头顾脚 + 捉襟见肘; 越扯越长 + 离题越远), the tripled
    "good" of the Beiping paean, the (?) after the Investigation Section,
    the Browning-vs-unknown-make contradiction, the 梯子 (ladder) oddity in
    the gezi sketch — faithful oddities stay visible.
  - **Fidelity-risk fixes**: suggestions that would alter claims (e.g.
    "split the government" for 分裂活动, "assets" for 「运用人员」,
    dropping "three or five days"/"three men"/"two words" would break
    numeric invariants or decided renderings).
  - **Two reader errors:** 连谋 parsed as "a certain Lian" (谋 is the given
    name); "nothing to boast of" counted as three words (it is four, matching
    the 四个字 meta-count).
- Full ledger: every accepted item is traceable by critique number in the
  edits file; every rejected item falls under one of the classes above.

### Post-fold-in verification

- `verify_unit.py ch06` green after every apply cycle (one number regression
  caught and fixed en route: dropping "the two of us" orphaned 我们两个人's
  两 at p033 — restored; and the 五官/四个大字 noise entries above).
- Supplementary spot-audit of six fold-in-only paragraphs (p003, p020, p041,
  p072, p143, p283) against zh: all faithful. Combined audits: 27 paragraphs,
  zero meaning-drift defects.
- Tail (p318–p322) re-verified after the fold-in touched p321–p322.
- check_align ch06 OK (median 4.53); check_content ch06 clean (216/216).

## R2 (ch07, ch08) — register revision pass

Scope: ch07 + ch08, English-to-English register edits per REVISION_PLAN.md §3
(T1-T6) and §5. Content frozen. **ch07: 86 edits; ch08: 65 edits** via
`edits/ch07_edits.md` / `edits/ch08_edits.md` + `apply_edits.py` (every OLD
verified unique; sequential apply simulated before each real run; the reading
file re-derived from the pristine text on each amendment so the edits file
stays the single source of truth). No note anchors touched (ch07 11 anchors,
ch08 13 anchors, all still resolve); no notes added.

### Tic battery, before -> after

| class | ch07 before | ch07 after | ch08 before | ch08 after |
|---|---|---|---|---|
| T1 besides (adverbial, approx) | 11 | 8 | 17 | 16 |
| T1 thereupon/whereupon | 0 | 0 | 7 | 7 |
| T1 forthwith/presently/at length | 0 | 0 | 5 | 1 |
| T1 of-a-morning/evening/sudden | 1 | 1 | 3 | 1 |
| T1 wont/no-wish/made-bold/still-less | 0 | 0 | 4 | 3 |
| T1 nothing for it | 0 | 0 | 2 | 0 |
| T1 day-month dates | 5 | 2 | 16 | 6 |
| T2 could not but / could only | 3 | 2 | 0 | 0 |
| T2 and-the-rest/others | 6 | 5 | 12 | 12 |
| T2 pivots (namely / that is to say) | 2 | 0 | 0 | 0 |
| T2 gerund-of nominalizations | 3 | 2 | 3 | 3 |
| T2 litotes (no small / no few) | 3 | 1 | 4 | 2 |
| T3 quoted terms (straight pairs) | 0* | 0* | 361 | 322 |
| T5 contractions (n't only) | 6 | 11 | 0 | 2 |
| T6 impersonal one (+modal) | 11 | 3 | 27 | 23 |
| T4 semicolons | 245 | 245 | 407 | 405 |
| T4 sentences >60 / >90 | 43/12 | 38/11 | 94/26 | 92/25 |

*ch07 uses CURLY quotes (") for quotation and straight ' for apostrophes, so
the battery's straight-pair metric reads 0 for it; the real count was ~73
curly term-pairs, of which 40 narration proper-name pairs were thinned (see
below). ch08 uses straight quotes throughout. The T5 battery counts only
`n't` forms; most ch08 dialogue contractions added were 's/'ll ('ll: p166,
p330x2, p331, p340; and Wu Ping/Wang Wen 's-forms), which this metric ignores.

### T3 policy applied (the biggest eye-level change)

Decided recurring PROPER NAMES / orgs whose first book-use + gloss lives in
earlier chapters went PLAIN in narration:
- **ch07 (40 strips):** Grand Hôtel des Wagons-Lits, Legation Quarter, Beiping
  Station, Tianjin Station, Water Gate, the Japanese/American barracks,
  Lixingshe, Juntong.
- **ch08 (41 strips):** Beiping Station, Tianjin Station, Juntong.
Quotes KEPT at: naming/anatomizing sites (ch07 "legation district" p095, Water
Gate + the "water" word p098, the barracks/guard-detachment anatomy p100,
Lixingshe naming p326; ch08 Action/Intelligence/Military Group forming,
special commissioner / Renaissance Society / inspectorate system /
Investigation Section / Xiaobailou intros, "Ground C", the p220 & p387
anatomizing org-lists), the author's marked deixis (ch07 p321 "that"/"this",
p354 "Heaven's"), titles-as-titles, code names, and EVERYTHING inside quoted
documents and dialogue. Generated programmatically (byte-exact OLD, uniqueness
pre-checked); paragraphs that hold quoted documents/dialogue were skipped
wholesale.

### T5 dialogue naturalization

- **ch07:** Wang Tianmu (worldly/urbane social & practical asides), Qi Nanpu
  (blunt), Chen-in-scene & Bai Shiwei (terse with comrades), Feilong
  (spirited Beiping girl) contracted / de-stiffened. KEPT formal (T5 CAUTION):
  Zheng Jiemin's sanction briefing (p036-045, quasi-official), the stewards'
  deferential register, Manager Ying (already natural), Wang's sententious
  "all-rounder" teaching (p011).
- **ch08:** the rough/operational speakers naturalized — Wu Ping (p296),
  Chen Guorui (p340), Wang Wen (p166, p346), Yang Yushan (p330x2, p331). KEPT
  formal by characterization: Chen's frontal persuasion of the conservative
  elders Zheng/Fu, his operational briefings (a "troop-order"), Dai Li's
  weighted speech, Wang Yumei's dignified reproach, the hotel boy's
  deferential speech, and all quoted testimony/documents/Communist rhetoric.

### Surviving hits, defended (the battery is a flag, not a verdict)

- **ch07 day-month 2, of-a-sudden 1:** the 2 dates ("18 April", "21 April"/
  "the nineteenth") sit inside the Secret Records quoted document (p307-313,
  exempt); "all of a sudden" (p068) is living English idiom, not the
  costume-drama "of a sudden."
- **ch07 could-only 2:** p046 ("could only do our utmost", a landing coda) and
  p107 ("we could only turn right", the actual route) both read naturally.
- **ch07 and-the-rest 5 / gerund-of 2 / litotes 1:** the "and the others" cases
  are 他们 (real group reference), the 等 case in the Secret Records is exempt;
  gerund survivors are p333 (natural) and p362 (a deliberate parallel closing);
  litotes survivor is a natural collocation.
- **ch08 thereupon/whereupon 7, of-a-sudden 1, day-month 6, litotes 1(of 2),
  and-the-rest (most):** all inside quoted documents — Feng's telegram, the
  evidence lists, the two newspaper items, the Communist booklet, Ji's
  deposition/notice — which §3.1 exempts wholesale.
- **ch08 forthwith 1, still-less 3:** the surviving forthwith is in the p412
  military-branch notice (document); "still less" survivors are correlative
  comparisons (p370 "still less could there be error", p382 "Still less do we
  understand"), legitimate English.
- **ch08 impersonal one 23:** the bulk are Chen's essayist reflective codas
  ("what one may see from this affair", "one may see how venomous…") that the
  KEEP list protects (§3.2 T6 CAUTION); only genuinely-generic perception /
  team "one" was thinned (p111, p174, p293, p294).

### Rejected finding classes (RULE R1-4 — adjudicated by class, not item)

No blind critique this batch (R6/R11 carry the two spot checks). Standing
REJECT-by-class calls that shaped the pass: Chen's persona furniture (笔者
"the writer", humility formulas, topic frames, reflective codas, the narrating
"shall"); his interested-witness political heat ("the utterly evil Communist
Party", "the Mao hag Jiang Qing", "his dog's foul wind", "traitors",
"sanction") — never laundered, never sharpened; the author's marked irony /
scare-quoted terms he anatomizes; source-carried doubling and faithful
oddities; and everything inside quoted documents and quasi-official speech.

### Fidelity note found during the aligned read (source-driven, logged)

- ch08 p204: the English had fused two source sentences with a dash, leaving a
  dangling "After the 'Investigation Section' was merged into the 'Juntong'…—
  Wang was short and wiry" (RULE R1-2 class). Split into two sentences per the
  zh (「调查课」拨并「军统局」后，改由戴先生领导。他短小精干…). Not a content change.

### Checks

- `verify_unit.py ch07`: parity 362/362, numbers 0 unresolved, 11 anchors ok.
- `verify_unit.py ch08`: parity 461/461, numbers 0 unresolved, 13 anchors ok.
- **noise.txt addition (documented in the file):** `三、四两` — an enumerated
  pair recapped by 两 "the two of them" (三、四两层楼 ch08 = "the third and
  fourth floors"; 第三、四两集 ch17). The 两 is a summarizing counter, not an
  independent quantity; placed before the bare `三、四` per the longest-literal
  ordering rule. This resolved a PRE-EXISTING ch08 number flag at pair 269
  (present in the shipped text, not introduced by R2) and greens ch17's same
  idiom too.
- `check_align.py`: ch07 OK (median 4.60; two low-ratio flags are short
  declaratives — "It was thus:", the date line); ch08 OK (median 4.69, no
  strays >2.2x).
- `check_content.py --config checks.json`: ch07 clean (206/206 name
  occurrences in the paired paragraph); ch08 3 DISPLACED = the documented
  homograph/substring false positive "ch08 Shunde" (the Lishunde Hotel,
  利顺德, contains the substring "shunde"; §2 known-benign) — no NEW
  displacement.
- `check_register.py --ref reference/R1_frozen.md`:
  - **ch07:** within tolerance (dialogue contractions 19.7/1k = 7.38x ref).
    "shall"-share 33% is a benign warning — the only two shalls are Zheng
    Jiemin's quasi-official sanction briefing (p044-045), deliberate/KEEP.
  - **ch08:** flags `STILTED` (1.0/1k = 0.38x ref, threshold 0.45x). This is a
    documented FALSE POSITIVE per `references/register-drift.md` §§1-2: ch08's
    "speech" word-count is dominated by quoted documents (Feng's telegram, the
    evidence lists, two newspaper reports, Ji's deposition, the military-branch
    notice, Ji's letters/poem, the Communist booklet's long excerpts) and by
    deliberately-formal speakers (Chen's persuasion of the conservative elders,
    Wu Ping's testimony, Ji's Communist rhetoric, Dai Li, Wang Yumei's
    dignified reproach, the deferential hotel boy) — all of which the reference
    forbids contracting. Every genuinely-casual line (the operatives Wang Wen,
    Chen Guorui, Wu Ping, Yang Yushan) was naturalized; the flag is measuring
    the chapter's documentary density, not register drift. The fidelity gate
    (verify_unit) is green.
- **Tail check:** ch07 p318-322 and ch08 p453-461 re-read against zh — no
  register edit falls in either tail (last ch07 edit p357, last ch08 edit
  p452); the frozen tails are unchanged and faithful.
- **Spot-audit (fixed seed 20260822, 10%+ of edited paragraphs, min 10):**
  - ch07: 26 paragraphs read zh-against-en (the seeded sample plus every
    RECAST/dialogue block) — ONE content slip caught and fixed (p162 dropped
    "in detail"/仔细; restored). Otherwise zero meaning-drift.
  - ch08: 21 paragraphs read (seeded sample plus the grammar recast, dates,
    and all naturalized dialogue) — one nuance tightened (p346 顾虑到 rendered
    "worried … might" rather than "watching in case"). Otherwise zero
    meaning-drift.
- Build: `qa_epub.py` **PASS** (57 files, 50 documents, 375 refs/375 bodies/
  375 backlinks, all links resolve); epubcheck 5.1.0 **0 fatals / 0 errors /
  0 warnings / 0 infos** (EPUB 3.3).

### R13 reconciliation flags (NOT changed in R2)

- ch07 keeps one-off proper hotel names quoted at their single ch07 appearance
  ("Hôtel de Pékin", "Central Hotel", "Chang'anchun Hotel" p143) — low
  frequency; confirm book-wide treatment in R13.
- ch08 "special commissioner", "inspectorate system", "Intelligence Group",
  "Action Group", "Military Group", "Renaissance Society", "Investigation
  Section" left quoted (naming/anatomizing/list contexts here) — confirm
  whether any recur plainly enough elsewhere to warrant book-wide thinning.

### Setup note

- setup.sh regression: the ONE known false alarm ("hook stands down on
  template stub") still fails as documented — it is the kickoff_guard Stop hook
  correctly ENFORCING because HANDOFF.md carries a real (non-template) kickoff,
  which is exactly what we want; the test assumes a template-stub HANDOFF. All
  other checker regression tests green.

## R3 (ch01-ch05, ch09, ch10) — register revision pass

Scope: ch01-ch05 (front matter, light-touch), ch09 + ch10 (main chapters).
English-to-English register edits per REVISION_PLAN.md §3 (T1-T6) and §5.
Content frozen. Edits via `edits/<id>_edits.md` + `apply_edits.py` (every OLD
verified unique; ch09 re-derived from pristine on amendment so the edits file
stays the single source of truth). Totals: **ch01 0, ch02 1, ch03 1, ch04 3,
ch05 4, ch09 65, ch10 11 = 85 edits.** No note anchors moved; no notes added.

### Tic battery, before -> after (key classes)

| class | ch04 b/a | ch05 b/a | ch09 b/a | ch10 b/a |
|---|---|---|---|---|
| T1 of-a-sudden | 0/0 | 0/0 | 13/1* | 0/0 |
| T1 forthwith/presently | 0/0 | 0/0 | 2/0 | 0/0 |
| T1 nothing-for-it | 0/0 | 0/0 | 1/0 | 1/1** |
| T1 day-month dates | 0/0 | 0/0 | 0/0*** | 0/0*** |
| T2 could-not-but/only | 1/1 | 0/0 | 3/1 | 0/0 |
| T3 quoted pairs | 95/94 | 10/6 | 298/271 | 20/20 |
| T4 semicolons | 51/49 | 2/2 | 395/395 | 20/20 |
| T4 >60 / >90 | 14/14 | 1/0 | 79/75 · 14/13 | 10/10 · 4/4 |

ch01: 0 edits (at target); its 1 "still less" is a correlative (更不敢), KEEP.
ch02: 15 quoted pairs all KEEP (first-use naming, marked irony on self-styled
titles, anatomized "success"/"failure", "Blind Wang", quoted maxims); 1 edit
(collocation "put off that" -> "Never mind that"). ch03: 1 T1 date. 
\* ch09 of-a-sudden 13->1: the surviving 1 is "all of a sudden" (living idiom,
KEEP). Also converted 9 spelled-ordinal narration dates -> American (not counted
by the digit-based day-month battery). \*\* ch10 "nothing for it" survivor is
inside Chiang's quoted address (p021), exempt §3.1. \*\*\* ch09/ch10 date
conversions were spelled-ordinal / 民國-year forms the digit battery never
counted; real accessibility wins (see below).

### T3 policy applied

- **ch04** (essayist meditation on "the meaning of secret-service work"): the
  95 pairs are almost all KEEP — Chen anatomizes the terms AS words through
  p019-p061 (T3 CAUTION). Only 1 strip (decided-org repeat "Juntong" p056).
- **ch05** (founding of the Juntong): first-use org names KEEP quotes at their
  book-first site (p001-p004, p006-p007 anchors); the 4 repeat-uses in running
  prose (p005 x2, p006 x2: Special Services Department, Second Department) went
  plain (consistent with R1's ch06 treatment).
- **ch09**: 27 strips of decided station names "Beiping Station"/"Tianjin
  Station" (glossed at book-first-use in ch02/ch05) -> plain in narration, same
  as R2 for ch07/ch08. **The note-anchor site (`the "Beiping Station" had had`
  at the "first taste of defeat" anchor) is preserved quoted.** KEPT quoted:
  Intelligence/Military Group, inspectorate system/inspector, the compound
  "Tianjin Station Intelligence Group", enumerated work-heads, the Shi-bio
  self-styled titles, and everything inside dialogue/telegrams. Generated
  programmatically (byte-exact OLD, uniqueness pre-checked, anchor auto-skipped).
- **ch02, ch10**: all quoted terms verified legitimate KEEPs (0 strips).

### ch09 T1/T2/T5 detail

9 spelled-ordinal narration dates -> American; 11 "of a sudden" -> suddenly/all
at once; 2 forthwith -> at once; 1 nothing-for-it recast; 2 "could not but"
recast; 9 T5 rough-speaker naturalizations (Shi Yousan, Staff Officer He, Chen
Guozhi, Shi Dachuan, Wang Wen). **check_register: ch09 was STILTED-flagged
before the T5 pass (0.3 contr/1k); after, 1.7/1k, within tolerance.** The
residual "shall"-share (23%) is the deliberate narrating shall (KEEP). The 21
"besides" hits are all natural (postpositive "X besides" / sentence-initial
"Besides,") — defended, not the costume-drama sentence-adverb.

### ch10 dates -> Gregorian (accessibility + book consistency)

ch10 alone rendered 民國 years literally ("the twenty-eighth year of the
Republic"), inaccessible to the target reader and inconsistent with the
Gregorian standard used throughout ch01-ch09. All 11 converted (民國 N =
1911+N; date-VALUE preserved), spelled-ordinal days -> American. The 4
battery-flagged >90-word sentences are all exempt (colon-list p003, landing
periodic build p008, quote-period merge artifacts, quoted speech p020-021).

### Noise entries added (data/noise.txt) — do-not-revert

- `四、五千` (ch09 p121, 四、五千块 "four or five thousand dollars"): resolved a
  PRE-EXISTING verify_unit number flag (present in the shipped text, surfaced by
  R3's per-chapter verify); the bare `四、五` rule orphaned 千 as a phantom 1000.
  Longer literal, placed before `四、五`. RULE R1-3.
- `二十一、二` / `二十七、八` (elided Republic-year pairs, ch10; also present as an
  age in ch26 and a year in ch33): the Gregorian rendering removed the incidental
  2/8 the old ordinal wording carried, orphaning the checker's mis-parse of the
  elided 、二 / 、八; same class as the existing `十三、四`. Noise only removes
  source numerals, so it cannot cause a false failure elsewhere.

### Checks (all green)

- verify_unit: ch01 8/8, ch02 18/18, ch03 14/14, ch04 61/61, ch05 8/8, ch09
  332/332, ch10 26/26; numbers 0 unresolved each; all anchors resolve (ch09's 9
  incl. the preserved Beiping-Station anchor).
- check_align: no strays. check_content: only the documented known-benign FPs
  (ch08 Shunde, ch09 Jize p220 [untouched], ch13, ch26, ch38, ch41) — no NEW
  displacement.
- check_register --ref reference/R1_frozen.md: all 7 within tolerance.
- Tail checks: ch04 p060-061, ch05 p008, ch09 p330-332, ch10 p025-026 re-read
  against zh — faithful; last edits fall before each tail.
- Spot-audit (edited paragraphs read zh-against-en): every edit is
  register/punctuation-only (quote strips, date reformats, of-a-sudden ->
  all-at-once, contractions, could-not-but recasts) with the propositional
  content preserved by construction; the non-mechanical recasts (ch09 p203
  不由得 "in spite of myself", p269 冷不防 "all at once", p270 找死 "your own
  death you're after", p259/p154/p257 rough-speaker recasts) re-verified against
  zh — zero meaning drift.
- Build: qa_epub PASS (57 files, 50 documents, 375 refs/375 bodies/375
  backlinks); epubcheck 5.1.0 0 fatals / 0 errors / 0 warnings / 0 infos.

### Rejected finding classes (RULE R1-4, by class)

Standing REJECT-by-class calls that shaped R3: Chen's persona furniture (笔者
"the writer", humility formulas, topic frames, the reflective essayist codas of
ch04/ch10, the narrating "shall"); his interested-witness heat ("the utterly
evil Communist Party", "the bandit chief Mao", "traitors", "sanction"); the
author's marked irony / anatomized terms (esp. ch04's whole "meaning of
secret-service work" essay and ch10's title discussion); source-carried
doubling and faithful oddities; correlative "still less" (更不敢/更不会);
postpositive "besides"; and everything inside quoted documents, telegrams,
verse, and quasi-official/deferential speech (Chen to Dai Li, Dai Li's grave
audience speech, Wang Wen's substantive operational briefings).

### R9 / whole-book reconciliation flags (NOT changed in R3)

- **民國-year rendering:** ch10 rendered Republic years literally (now converted
  to Gregorian); confirm no other unrevised chapter still does so.
- **第二处:** rendered "Second Bureau" in ch09 p031/p056 vs "Second Department"
  in ch05 p004/p005 (free rendering, not a glossary term) — pick one book-wide.
- **保密局** "Bureau of Confidential Investigation" (ch04 p038) vs glossary
  "Baomiju" — standing R1 flag.
- **the cook who does/did the cooking** (ch09 p097 dialogue, p186 narration):
  mild tautology for 烧饭的厨子/厨司务, left as source-carried doubling; consider
  thinning the narration instance in a later cleanup.

### Setup note

- setup.sh regression: the ONE known false alarm ("hook stands down on template
  stub") still fails as documented — it is the kickoff_guard Stop hook correctly
  ENFORCING because HANDOFF.md carries a real (non-template) kickoff; the test
  assumes a template-stub HANDOFF. All other checker regression tests green.

## R4 (ch11, ch12, ch13) — register revision pass

Scope: the opening of the Hanoi sub-book. ch11 "Bloodshed Against the Enemy"
(87 paras), ch12 "Unfathomable Hearts, Hidden Designs" (131 paras), ch13
"Treacherous Tides, a Gathering Storm" (262 paras). 217 edits total (ch11 51,
ch12 31, ch13 135), English-to-English per REVISION_PLAN.md §3/§5, content
frozen. The dominant work was DATE accessibility (§10): these chapters carry
the Hanoi-mission chronology and a long biographical essay on Wang Jingwei
(1879-1945), so Republic-YEAR narration dates ("the twenty-eighth year of the
Republic") and Republic-era month calques ("the eleventh month") were converted
to Gregorian/American (year N = 1911+N; "sixth month" = June). Qing-era/ganzhi/
lunar dates and every date INSIDE quoted material stay.

### Tic battery, before -> after (key classes)

| class | ch11 | ch12 | ch13 |
|---|---|---|---|
| T1 besides (adverbial) | 6 -> 4 | 6 -> 4 | 4 -> 4 |
| T1 thereupon/whereupon | 0 -> 0 | 1 -> 0 | 3 -> 0 |
| T1 forthwith/presently/at length | 4 -> 3 | 1 -> 0 | 0 -> 0 |
| T1 of-a-morning/sudden | 0 -> 0 | 2 -> 1 | 1 -> 0 |
| T1 wont/no-wish/still-less | 3 -> 0 | 1 -> 1 | 4 -> 3 |
| T1 nothing for it | 3 -> 0 | 0 -> 0 | 1 -> 0 |
| T2 could not but / could only | 1 -> 0 | 1 -> 0 | 7 -> 6 |
| T2 pivots (that is to say/namely) | 0 -> 0 | 2 -> 1 | 3 -> 0 |
| T2 litotes (no small/few) | 0 -> 0 | 3 -> 2 | 5 -> 4 |
| T3 quoted-term pairs | 98 -> 86 | 242 -> 235 | 284 -> 284 |
| T6 impersonal one | 11 -> 7 | 11 -> 10 | 34 -> 19 |
| T4 semicolons | 117 -> 116 | 244 -> 244 | 437 -> 436 |
| T4 sentences >60 / >90 | 26/7 -> 25/6 | 70/20 -> 69/20 | 78/25 -> 77/24 |

Surviving hits, defended against the read-aloud test (§3.2):
- **ch11 forthwith x3, of-a-morning:** all inside the Wang Jingwei "Yan
  Telegram" (p070) and its re-quote (p077) — quoted document, exempt.
- **ch12 besides/of-a-morning/that-is-to-say/litotes:** all inside Chiang's
  ~9,000-char address (p036-056) or the Zhu Zijia excerpt (p104), or plain
  prepositional "besides" (p086/p090, T1 CAUTION).
- **ch13 still-less x3, could-not-but/could-only x6, litotes x4:** "still less"
  (p087/p139) and "could only" (只有/只好 = had no recourse) are defensible
  modern English; the litotes are mostly the false positive 小馆 ("no little
  northern eatery" = a small restaurant, not a litotes) and the standard idiom
  "no small feat"; "could not but lament/be torn" is Chen's grave register.
- The T3 pair counts stay high because these chapters legitimately quote a great
  deal (telegrams, statements, official documents, classical poems and ci).

### T1 dates -> Gregorian/American (the bulk; §10, number-check-safe)

- **ch11:** 16 narration dates (民國二十八年元月 -> January 1939; 九月二十七日 ->
  September 27, 1939; etc.). Dates inside the Yan Telegram/expulsion resolution
  stay.
- **ch12:** ~15 narration dates. Konoe's 2nd/3rd statements, Chiang's address,
  and the Chen Bulei / Wang Yunsun / Zhu Zijia / Yongwu quoted excerpts are all
  exempt (§3.1) — their internal dates stay.
- **ch13:** ~75 date conversions, including Republic-era month calques
  ("the eleventh month" -> November) across the Wang Jingwei biography. Qing/
  ganzhi/lunar dates (宣统/庚戌/民前/丙午 forms, p152/p155/p169/p172/p262 birth-
  year) and dates inside the many quoted poems, ci, and diary excerpts stay.

### T3 quote-thinning (recurring decided org names -> plain in narration)

- **ch11:** stripped later occurrences of Tianjin Station, Luan-Yu Command,
  Tianjin District, Beiping (First) Station, Anti-Japanese Traitor-Killing
  Corps, action group / political department. Quotes KEPT at the note-anchor
  first-appearance sites (Luan-Yu Guerrilla Command p004, Anti-Japanese
  Traitor-Killing Corps p008), on the anatomized document title "Yan Telegram",
  the verbatim telegram markings, and marked-irony terms.
- **ch12:** stripped later occurrences of the Five Ministers' Conference (anchor
  at p074 kept), Beiping Station and Aviation Inspection Office (p093).
- **ch13:** no org-name strips needed — its recurring terms are either already
  plain, or first-appearance/anatomizing sites (Special-Service Regiment, Yu
  Special District, etc., all introduced and glossed in p086). Hotel names
  ("Continental"/"Railway") and the project designation "Hanoi work" kept
  quoted (R9 flag below).

### T5 dialogue naturalization

- **ch11:** Dai's fronted-object instruction un-inverted but kept uncontracted
  (mission speech, §3.4); Luqiao contracts freely (爽朗); Chen-in-scene a light
  contraction with a near-peer.
- **ch13:** Mr. Xu (bold, worldly host) contracts in living speech; Mrs. Xu
  (warm hostess), Wei Chunfeng (young, frank), and Bingxi's offhand asides
  naturalized. Chen's earnest formal reply to Mr. Xu (p044) kept formal
  (characterization, T5 CAUTION); Dai's and Cao's mission instructions kept
  their weight.

### T6 impersonal "one"

Thinned where it renders a generic 人/谁 that is really I/we/you (his own
sensation, their own predicament, or a reader address), and where 由此可见/可见/
只能说是 read as a hedge ("this shows"/"plainly"/passive). Kept in the essayist
codas and general maxims (ch13's "one must have a certain measure," "one who
can neither advance nor retreat," the reflective generalizations). ch13's 34 ->
19 is the largest single-chapter thinning of the pass so far.

### One grammar fix (ch13 p189)

个中利害，大家都看得清清楚楚: the shipped English "The gain and loss of it all
could see clearly" dropped the subject 大家, leaving "gain and loss" impossibly
"seeing". Restored to "The gain and loss of it all, everyone could see clearly"
— content preserved, ungrammatical clause repaired (English-to-English).

### Checks (all green)

- verify_unit per chapter: parity ch11 87/87, ch12 131/131, ch13 262/262;
  numbers 0 unresolved (ch11 87 pairs, ch12 131, ch13 262); all note anchors
  resolve (ch11 10, ch12 16, ch13 21).
- check_register --ref reference/R1_frozen.md: **ch11 within tolerance**
  (2.3 contr/1k, 0.88x; "shall" 33% is the deliberate narrating shall — KEEP);
  **ch13 within tolerance** (2.3/1k, 0.86x); **ch12 flags STILTED (0.0 contr/1k)
  — the ch08-class documentary false positive**: of ~2,969 "speech" words the
  measure counts, ~1,936 are long quoted documents and the rest quoted terms;
  ch12 has essentially no casual dialogue to contract, so it was NOT chased (per
  the R3 ruling; contracting quoted documents is forbidden).
- check_align: ch11/ch12 OK; ch13 one flag (pair 163, ratio 10.5) is a `{p}`
  verse line — a terse classical couplet expanded in English, a poem never
  edited (benign verse-ratio FP).
- check_content (--config checks.json): ch11/ch12 clean; ch13's 9 "displaced"
  are the documented benign diacritic/variant name FPs (Nguyễn vs "Nguyen" x7,
  Ōya vs "Oya", Yuan Yishan vs glossary "Yuan Haowen") — pre-existing, not
  touched by R4.
- Build + qa_epub: **PASS** (57 files, 50 documents, 375 refs/375 bodies/375
  backlinks, all links resolve). epubcheck 5.1.0: **0 fatals / 0 errors / 0
  warnings / 0 infos**.

### Noise entries added (data/noise.txt) — do-not-revert

- **二十二、三** (ch12 p093): elided Republic-year pair 民国二十二、三年 (1933-34);
  the 、三 elides 二十三 and the checker misreads a bare 3. Same class as the R3
  二十一、二 / 二十七、八 entries.
- **二○七** (ch13 p185): the fullwidth circle (U+25CB) in address 二○七号 (No. 207)
  breaks the positional-year parse, so the checker reads bare 2/7 instead of 207.
  The English carries "No. 207"; surfaced in R4 only because the incidental
  "twenty-seventh" wording that had covered the stray 7 was converted to a
  Gregorian date.

### Rejected finding classes (RULE R1-4, by class)

Standing REJECT-by-class calls held through R4: Chen's persona furniture (笔者
self-reference, humility formulas, topic frames), the deliberate narrating
"shall" (KEEP-list, verified), his interested-witness heat ("traitor,"
"sanction," the martyr reverence, the Wang-Jingwei indictment), quoted
documents in full (telegrams, statements, Chiang's address, the diary/memoir
excerpts, all the classical poems and ci), org terms of art, and source-carried
doubling. No fabrication risk: content frozen, every NEW verified to preserve
the OLD's propositional content (spot-audits recorded per chapter, tails checked
— ch11 p083, ch12 p129/p131, ch13 p262 Aug-10-1945 surrender / Nov-10-1944
Wang's death).

### R9 / whole-book reconciliation flags (NOT changed in R4)

- **Project-name quoting:** "Hanoi work"/"Hanoi operation" (河内工作) and the
  hotel names ("Continental"/"Railway") are kept quoted as named
  operations/places; decide book-wide in R9 whether to strip after first use.
- **"Wang case" (汪案):** kept quoted (case designation); low frequency here.
- **四十年代 (ch13 p130):** rendered "the forties"; in a Taiwan/ROC context 四十
  年代 is Minguo 40s = the 1950s. Possible value error (frozen; flag for R9).
- **民前 birth year (ch13 p262):** "twenty-eighth year before the Republic"
  (= 1884) conflicts with p134's "1883" (光绪九年) — a source inconsistency left
  visible; R9 to note.
- **p152 vs p155 二月 (ch13):** the same Xuantong-2 date is "the twenty-first of
  February" at p152 but "the twenty-first of the second month" (lunar) at p155;
  pre-existing translator inconsistency, left as-is.

### Setup note

- setup.sh regression: the ONE known false alarm ("hook stands down on template
  stub") still fails as documented — the kickoff_guard Stop hook correctly
  ENFORCING because HANDOFF.md carries a real (non-template) kickoff. All other
  checker regression tests green.

## R5 (ch14, ch15, ch16, ch17, ch18) — register revision pass

Fifth batch of the register pass (REVISION_PLAN.md §3/§5). The opening of the
Shanghai sub-book: the Wang-case prologue (ch14), the botched Bolang assault and
the mistaken killing of Zeng Zhongming (ch15), the essayistic/documentary
post-mortem (ch16), the flight back to Chongqing and the new Shanghai mission
(ch17), and taking over the Shanghai District plus the fates of the nineteen
Hanoi comrades (ch18). **170 edits total** (ch14 5, ch15 39, ch16 25, ch17 36,
ch18 61) via `edits/<id>_edits.md` + `apply_edits.py`.

This batch is dominated by **DATE accessibility**: ch15/ch17/ch18 are
mission-chronology chapters (like R4's ch11-13), so the bulk is Republic-year and
spelled day-month NARRATION dates -> Gregorian/American across 1925-1984
(number-check-safe: Republic year N -> N+1911 per check_numbers.py L327; month
names carry the month numeral). Quoted-document dates, day-only ordinals, one
lunar reference (ch17 p027 Qiantang tidal bore, "eighth month"), and a recorded
death-time (ch18 p079 "sixteen o'clock", carries 十六时) are LEFT. The remainder
is T6 impersonal "one" thinned where concrete, T5 dialogue naturalization
(the canonical §3.2 Bingxi example at ch16 p034; Mr. Xu, Chunfeng, Luqiao, Tang),
a handful of T1/T2 antique/calque, and three RULE R1-1 opaque/broken-idiom fixes.

### Tic battery, before -> after (key classes)

| class | ch14 | ch15 | ch16 | ch17 | ch18 |
|---|---|---|---|---|---|
| T1 besides (adv) | 0->0 | 8->7 | 7->7 | 9->9 | 10->10 |
| T1 of-a-sudden/morning | 0->0 | 9->3 | 2->2 | 3->1 | 0->0 |
| T1 nothing-for-it | 0->0 | 2->0 | 1->0 | 2->1 | 0->0 |
| T2 could-not-but/only | 0->0 | 8->8 | 5->5 | 5->5 | 0->0 |
| T2 pivots (that-is-to-say) | 0->0 | 5->3 | 2->1 | 1->1 | 1->1 |
| T2 litotes (no small/few) | 0->0 | 6->5 | 0->0 | 1->1 | 1->1 |
| T5 contractions | 0->0 | 6->7 | 0->4 | 0->0 | 0->0 |
| T6 impersonal "one" | 0->0 | 21->17 | 13->10 | 8->8 | 8->8 |
| T4 >60 / >90 words | 1/1 | 59/14->58/14 | 61/15->59/14 | 47/12->45/12 | 37/3->34/2 |
| T3 quoted pairs | 2 | 151 | 92 | 170 | 131 |

The residual T1/T2/T6 counts are dominated by QUOTED DOCUMENTS and the formal
announcements, which legitimately hit the battery (§3.1) and are not chased:
ch15 is ~1/3 quoted material (the Chiang/Dai/Zhu excerpts, the p054-p061 order),
ch16 ~60% (Wang's "Account"/"To Cite One Instance", the committee minutes,
Chiang's Q&A, Wu Zhihui's essay), ch17 ~50% (the "six leads", Wang's Long-Yun
letter, Kagesa's memoir, Chiang's Secret Records, Zheng's True Record), ch18
several long excerpts (Liu Shoufa's memoir, Dai's telegram, Tang's letters).
The remaining narration "besides" are prepositional/"in addition" uses (T1
CAUTION); the surviving "could only/not but" and "one" are essayist generalizing
in Chen's reflective codas (T6 CAUTION).

### T3 quote policy applied

Near-zero strips this batch (contrast R4's org-name strips). The quoted pairs
here are legitimately KEPT: live dialogue, book/paper/episode titles (several are
note-anchor sites), author-coined terms anatomized on the page ("soft/hard
action", "loud/silent weapon", "combat readiness", the definitional
"Juntong Bureau"/"Juntong" at ch17 p183), quoted-document fragments, and marked
irony ("advocacy of peace"/"suing for surrender"). "Hanoi work" (河内工作)
project-name quoting stays for the R9 book-wide decision (per the R4 handoff).

### Blind-critique spot check (R5, §5.6/§8) — adjudicated by class (RULE R1-4)

Ran the verbatim blind-reader prompt on the revised **ch16 §1** (the narration +
reported-dialogue span, p001-p045, no source/plan) — 150 findings returned. The
reader was calibrated to a MODERN-NEUTRAL target; this book's target is
deliberately GRAVE-FORMAL (§3.1, which departs from the shelf's modern-neutral
default). Adjudication:

- **ACCEPTED (2), applied to ch16 in a follow-up commit** — findings that cross
  even the grave-living line: (a) ch16 p012 "set the record of having,
  single-handed, cut down with his own hand..." — garbled, doubled
  单枪匹马/手刃; tightened. (b) ch16 p023 "'first come, first master'" (先入为主)
  — not an English idiom, opaque (RULE R1-1) -> "'first impressions rule'"
  (the concept is already glossed as the "law of primacy" at p014).
- **REJECT-by-class (~148)**, with the KEEP-list reason as the record:
  1. **Deliberate grave/formal register** (~55): "that we might", "by rights",
     "brooks no", "vaunt", "come what may", uncontracted narration, grave
     periodic sentences that LAND. This IS the target voice (§3.1 read-aloud
     tiebreaker: a grave, precise, old-fashioned but LIVING narrator). REJECT.
  2. **笔者 / "the writer"** persona formula (RULE R1-4): deliberate, KEEP.
  3. **Rendered chengyu kept for their image** (§3.3): 养虎遗患, 按图索骥,
     虎头蛇尾, 空穴来风, 出这口气, "scale and half a claw" — the reader wants
     them all de-imaged; KEEP the ones that land in context (the two that read
     genuinely broken/opaque were the ACCEPTs above).
  4. **"in truth"/topic-comment/clause-stacking** flagged as translationese:
     these are Chen's cadence; the >90-word two-spine cases are triaged under
     T4, not razed. REJECT as a class, watch under RULE R1-5.
  The blind reader stopped short of the quoted documents (they weren't in the
  excerpt); on the register itself, the two real defects it caught are exactly
  the RULE R1-1 class the pass exists to fix, and they fed back in.

### Recurring-tic watch (RULE R1-5)

The blind critique confirmed two live repetition tics to thin as met: "in truth"
/ "to speak truly" (Chen's filler doublet), and "talk over" (x3 in ch16 §1).
Handled where they clustered; flagged for the remaining batches.

### Spot-audit (>=10% of edited paragraphs per chapter, against the source)

Meaning preserved in every sampled edit; the register pass makes only in-paragraph
English changes (no text moved between paragraphs — check_align confirms).
- **Dates (the bulk):** verified the Republic->Gregorian arithmetic (N+1911) on a
  fixed sample spanning the range — ch15 p047 (28->1939), p124 (30->1941), p190
  (37/38->1948/49); ch17 p002 (20->1931), p108 (15->1926), p112 (28->1939);
  ch18 p001 (28->1939), p079 (24->1935, 32->1943, 33->1944), p098 (50->1961),
  p138 (73->1984). All correct; day/month numerals preserved.
- **Recasts / idiom fixes (re-read zh against en):** ch14 p002 为虎作伥 ->
  "playing cat's-paw to the tiger"; ch15 p079 Mr. Xu's legal opinion (naturalized,
  content intact), p114 (nothing-for-it + one->we); ch16 p034 Bingxi
  尽管放心走好了...由我负责料理 -> "Don't worry, go. I'll take care of things
  here."; ch17 p017 有就是有，没有就没有 -> "What was, was; what was not, was
  not."; p002 背黑锅 -> "made the scapegoat". All propositionally faithful.
- **Tails** re-read against zh: ch15 p225, ch16 p116, ch17 p147, ch18 p138 — all
  match; no drift or invention.

### Checks (all green)

- `verify_unit.py`: parity ch14 5 / ch15 225 / ch16 116 / ch17 147 / ch18 138;
  numbers 0 unresolved (each after resolving one RULE R1-3 latent match:
  ch17 p054 "fortnight"->"two weeks" for 两周; ch18 p115 廿九 kept spelled);
  anchors ch14 0 / ch15 11 / ch16 8 / ch17 9 / ch18 6 all resolve.
- `check_align.py`: all five OK (no pair strays >2.2x from the chapter median).
- `check_register.py --ref reference/R1_frozen.md`: ch14/ch15/ch16 within
  tolerance. **ch17 flags STILTED (0.0 contr/1k, 43% shall)** and **ch18 the
  script self-labels "little dialogue — noisy"** — both the ch08/ch12-class
  DOCUMENTARY false positive (quoted-document mass + Dai Li's deliberately-formal
  mission-instruction dialogue, which §3.4 keeps formal); NOT chased, matching
  the R4 ch12 decision.
- `check_content.py`: config-unavailable this batch (the plain book.json lacks the
  docs/sources map it needs; it self-reports "NOTHING was checked"). The register
  pass moves no text between paragraphs, so displacement is guarded by
  check_align (passed) + verify_unit's number/anchor invariants; noted honestly.
- Build + `qa_epub.py`: **PASS** (57 files, 50 documents, 375 refs/bodies/backlinks,
  all links resolve). **epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings / 0 infos.**

### Noise entries added (data/noise.txt) — do-not-revert

- `五十一、二` — the elided Republic-year pair 民国五十一、二年 (1962-63, ch18
  p123); the lone 、二 (2) has no English match once the pair renders "1962 or
  1963" (the old "fifty-second" was coincidentally supplying it; RULE R1-3).
  Same class as R4's `二十二、三`.

### RULE R1-3 latent matches surfaced (documented, not contorted)

Two date edits removed a coincidental ordinal sub-number match: ch17 p054's
"twenty-second" was supplying the 2 that covered 两周 ("two weeks", rendered
"fortnight") -> fixed by carrying the real quantity ("two weeks"); ch18 p115's
"twenty-ninth" was supplying the 9 that the variant 廿九 needs -> kept spelled
("twenty-ninth of April", month Anglicized only).

### Rejected finding classes (RULE R1-4, by class) — standing calls held through R5

Chen's persona furniture (笔者/"the writer", humility formulas, topic frames,
the narrating "shall"); quoted documents (register, length, archaisms, quotes,
等-tags, dates inside them); Chen's interested-witness heat ("the man Wang",
"traitor", the reverent martyr set-pieces, 日本鬼子 "Japanese devils"); decided
glossary renderings; set-off markers; note anchors; chengyu that land; the
source's own faithful oddities. Dai Li's mission-instruction dialogue stays
formal (§3.4: never contracts in anything quasi-official).

### R9 / whole-book reconciliation flags (NOT changed in R5)

- **为虎作伥 / 虎伥 rendering drift:** ch14 p002 "playing cat's-paw to the tiger"
  vs ch17 p145 "play the tiger's lackey" — decide one book-wide in R9.
- **虎头蛇尾 rendering drift:** ch15 p136 "a tiger's head, a snake's tail" vs
  ch18 p052 "a tiger's head trailing off to a snake's tail" — reconcile in R9.
- **民前四年 (ch18 p103):** "the fourth year before the Republic" (= 1908) LEFT
  unconverted — the +1911 rule does not apply to 民前 (before-Republic) forms,
  and the R4 handoff shows 民前 birth-years are error-prone (a 1883/1884 source
  inconsistency in ch13). Convert/gloss in R9 or the F0 footnote pass.
- **沐猴而冠 (ch18 p010) "play the monkey in a hat":** kept as mockery; verify it
  reads for a Western reader in R9 (candidate for an F0 note).
- Carried R1-R4 flags still stand ("Hanoi work"/hotel quoting; 第二处 "Second
  Bureau"(ch09) vs "Second Department"(ch05); 四十年代 "the forties" possible
  Minguo-40s=1950s; etc.).

### Setup note

- setup.sh regression: the ONE known false alarm ("hook stands down on template
  stub") still FAILS as documented at R2-R4 — the kickoff_guard Stop hook is
  correctly ENFORCING because HANDOFF.md carries a real (non-template) kickoff,
  which is precisely what that test inverts. Benign; not a tooling regression, not
  fixed (altering the guard to pass on a live branch would hide real regressions).
  All other checker regression tests green.

## R6 (ch19, ch20, ch21, ch22, ch23, ch24) — register revision pass

Sixth batch of the register pass (REVISION_PLAN.md §3/§5). The front and opening
of the Third Part (Shanghai): the author's short notice (ch19) and preface (ch20),
then Chapter 1 — Chen's arrival in occupied Shanghai and the inventory of the
Shanghai District's units (ch21); Chapter 2 — the Cheng Haitao sanction, Wan
Lilang's defection, the Fan Xing intelligence line, and the Christmas-Eve sanction
of Chen Mingchu (ch22); Chapter 3 — the short reverent intro on the three foes
(ch23); and Chapter 4 — the two Concessions' police, the Japanese gendarmerie and
its tortures, No. 76, and the Yu Yefeng case (ch24). **181 edits total** (ch19 3,
ch20 21, ch21 52, ch22 66, ch23 1, ch24 38) via `edits/<id>_edits.md` +
`apply_edits.py`.

Like R5, dominated by **DATE accessibility**: ch20-ch24 are mission-chronology
chapters, so the bulk is Republic-year and spelled day-month NARRATION dates ->
Gregorian/American across 1925-1983 (number-check-safe: Republic year N -> N+1911
per check_numbers.py; month names carry the month numeral). ALL quoted-document
dates are LEFT (§3.1): the self-cited First-Part preface (ch19 p001, ch20 p004/
p005), Dai Li's telegrams (ch22 p002/p011/p095/p101/p171/p219/p233), Zheng
Xiuyuan's "Three Perils"/"DDS Cafe" accounts (ch21, ch22), the Fourth Team report,
Bi Gaokui's audience, Wan Molin's book and the Shenbao news (ch24), the police-
roster excerpt (ch24 p028-p036), Dai's quoted self-review (ch24 p158). The
remainder: T6 impersonal "one" thinned where it renders a concrete 你/我/我们
(generic essayist maxims and hypotheticals kept, §3.2 T6 CAUTION); adverbial
"besides"/"aught"/"still less"/"withal"/"making bold" (T1, prepositional "besides"
kept); a few T2 "could not but"/litotes/inversions; light T5 naturalization of
Mao Wanli's analytical monologue (ch21 p017-p020); recurring "severally" and
"one may say/see" varied (RULE R1-5); and several RULE R1-1/R1-2 fixes.

### Tic battery, before -> after (key classes)

| class | ch19 | ch20 | ch21 | ch22 | ch23 | ch24 |
|---|---|---|---|---|---|---|
| T1 besides (adv) | 0->0 | 5->4 | 10->8 | 21->18 | 0->0 | 8->8 |
| T1 day-month dates | 0->0 | 0->0 | 0->0 | 0->0 | 0->0 | 0->0 |
| T2 could-not-but/only | 0->0 | 0->0 | 5->3 | 14->13 | 0->0 | 4->4 |
| T2 litotes (no small/few) | 0->0 | 1->0 | 8->7 | 3->3 | 0->0 | 4->4 |
| T6 impersonal "one" | 0->0 | 1->0 | 19->11 | 30->22 | 1->0 | 11->9 |
| T4 >60 / >90 words | 4/1 | 13/5 | 45/12->45/11 | 100/24->101/23 | 2/1->2/0 | 71/20->69/20 |
| T3 quoted pairs | 9 | 46 | 250 | 389 | 12 | 368 |

The residual T1/T2/T6 counts are dominated by QUOTED DOCUMENTS (ch21/ch22/ch24
carry very large quoted-material mass — Zheng's and Liu Shaokui's memoirs, Dai's
telegrams, Wan Molin's book, the Shenbao news, the police rosters, Chen's self-
citations), which legitimately hit the battery (§3.1) and are not chased; plus
prepositional "besides" (T1 CAUTION), faithful SOURCE litotes (不下/不少/不简单),
and Chen's essayist generalizing "one" in his reflective codas (T6 CAUTION). All
"day-month dates" hits went to 0 (narration dates converted; quoted-doc dates the
battery would flag are inside `>`-free quoted paragraphs it does not scan as such,
and are LEFT by policy). The >60/>90 counts barely move: the long sentences here
are quoted documents (stay long, §3.1) and Chen's periodic set-pieces that LAND
(T4 CAUTION); not chased.

### T3 quote policy applied

Near-zero strips this batch. The quoted pairs are legitimately KEPT: quoted
documents and self-citations, live dialogue, author-anatomized terms ("large"/
"many"/"soft work"/"stratagem"/"three-stripe head"/"Badlands"), marked irony,
titles-as-titles, code/cover names, and note-anchor sites. Recurring decided
proper names/orgs already plain in narration from earlier batches.

### RULE R1-1 / R1-2 fixes (wrong-image idiom + dangling participle)

- ch20 p018: 都是政策的执行者 was "all but the executors of that policy" — English
  "all but" = "almost/everything except", a wrong-meaning calque -> "every one of
  us, executors of that policy".
- ch21 p035: 大显身手 was "shown his hand" (= reveal one's cards) -> "shown his
  prowess" (the R1 critique's 一显身手 class, RULE R1-1).
- ch21 p014: dangling participle "caught something of his temper, my mind grew
  brighter" -> "having caught..., I found my mind grew..." (RULE R1-2).

### Recurring-tic watch (RULE R1-5)

"severally" (ch20 preface, 3x -> thinned to 1); "one may say/see/put it"
(ch21/ch22/ch24, varied to "we may see"/"you might say"/"to put it thus" or the
hedge dropped). Watched, not eradicated.

### Spot-audit (>=10% of edited paragraphs per chapter, against the source)

Audited the substantive edits of each chapter against the zh (all date
conversions, the R1-1/R1-2 fixes, the clarity recasts, the impersonal->concrete
conversions, and each chapter's tail). All preserve propositional content exactly.
Sample verified: ch20 p017 end-Oct 1941 / Nov 28 / p020 early-Aug 1939; ch21 p003
early-Aug 1939, p035 dates + 大显身手->"prowess", p076 Aug 12 1939, p020 Wanli
grammar recast; ch22 p081 Dec 1925, p105 1935, p153 Dec 25 1939, p199 Dai Li
death Mar 17 1946, p068 garbled-clause recast, p203 impersonal->I; ch24 p044/p045
Jan 1938, p143 the Jan-14-vs-Jan-15-1940 discrepancy preserved, p121 Room 407
preserved, p160 "boldly". Per-chapter number checks all reconcile (parity by
construction; ch19 4/ch20 26/ch21 155/ch22 286/ch23 7/ch24 161 pairs, 0 unresolved).

### Rejected finding classes (RULE R1-4, by class) — standing calls held through R6

No blind critique this batch (R5 carried one spot check; the second is scheduled
for R8, §8). Standing reject-by-class calls, cited once here: Chen's persona
furniture (作者/笔者 "the writer", humility formulas, topic frames, the narrating
"shall"); quoted documents and self-citations (register, length, archaisms,
dates, 等-tags inside them); Chen's interested-witness heat (the anti-Communist
verdicts on Yuan Shu / the "Fifth Group"; the gendarme "two-legged beast" and
torture catalog; the No. 76 "robbers' den" and its three crimes; the martyr
reverence; his frank view of women comrades ch22 p229/p238; "using Chinese to
control Chinese"); decided glossary renderings (sanction, District, Juntong,
Blue Shirt Society, cover names); set-off markers; note anchors; chengyu that
land; the source's own faithful oddities. Mao Wanli's speech naturalized (close
friend, blunt); Dai Li's telegrams and quasi-official utterances stay formal.

### Checks (all green)

- Parity by construction; `verify_unit.py` per chapter: numbers 0 unresolved
  (ch19 4 / ch20 26 / ch21 155 / ch22 286 / ch23 7 / ch24 161 pairs), anchors all
  resolve (ch19 0 / ch20 2 / ch21 8 / ch22 7 / ch23 1 / ch24 6).
- `check_align.py` per unit OK (no pair strays > 2.2x from the unit median).
- `check_content.py --config checks.json`: all six R6 units "all in the paired
  paragraph" (no displacement); the only failures are the six documented benign
  homograph/substring false positives (ch08 Shunde, ch09 Jize, ch13, ch26, ch38,
  ch41), unchanged.
- `check_register.py --ref reference/R1_frozen.md`: ch19/ch20/ch23 within
  tolerance; **ch21/ch22/ch24 flag STILTED — the ch08/ch12/ch17-class documentary
  false positive** (contractions ~0 because the only free speech is Wanli's
  deliberately-analytical monologue plus quoted documents/rosters; shall% 33-36%
  is the deliberate narrating "shall", KEEP-listed and verified across batches),
  NOT chased.
- Build + `qa_epub.py`: **PASS** (57 files, 50 documents, 375 refs/375 bodies/375
  backlinks, all links resolve). **epubcheck 5.1.0: 0 fatals / 0 errors / 0
  warnings / 0 infos** (EPUB 3.3).
- Checker regression tests (setup.sh): green except the one documented benign
  false alarm ("hook stands down on template stub", see Setup note below); the
  new noise entry did not disturb check_numbers (pass-fixture OK, fail-fixture
  5/5).

### Noise entries added (data/noise.txt) — do-not-revert

- `四○七` (ch24 p121/p123): Room number 四○七号 = "Room 407". The full-width zero
  ○ breaks the CJK numeral run, so the checker reads bare 4 and 7 instead of 407;
  the real quantity 407 IS fixed in the English ("Room 407"). The old wording's
  spelled ordinals "twenty-fourth"/"twenty-seventh" had coincidentally supplied
  those 4/7; converting the narration date to "June 24, 1938" orphaned them
  (RULE R1-3). Strip the mis-parsed source token. Earlier R1-R5 entries all stand.

### RULE R1-3 latent matches surfaced (documented, not contorted)

- ch24 p121/p123: the 四○七号 (Room 407) / spelled-ordinal collision above — the
  canonical R1-3 case, fixed by a documented noise entry, not by contorting the
  date wording. Watch this class on every date edit that drops an ordinal word.

### R9 / whole-book reconciliation flags (NOT changed in R6)

- **为虎作伥 rendering drift widened:** now FOUR variants book-wide — ch14
  "cat's-paw to the tiger", ch17 "the tiger's lackey", **ch22 p016 "the tiger's
  accomplice", ch23 p006 "playing jackal to the tiger"** (ch23's is a NOTE ANCHOR,
  so R9 must move the anchor if it reconciles). Decide one rendering in R9.
- **沐猴而冠 drift:** ch18 p010 "play the monkey in a hat" vs **ch24 p098 "a monkey
  crowned and gowned"** — reconcile in R9 (candidate for an F0 note).
- **ch24 p085 gendarme-commander roster, 二十/二十七 SOURCE typo:** the table gives
  Miura Saburo's first term as 自二十年 (="from the twentieth year" = 1931), which
  contradicts the 1938 founding (二十七年元月) stated at p044/p045. LEFT in
  era-year form (a table where converting would print the wrong 1931); the
  inconsistency itself is a source error to note in R9/F0, faithful as rendered.
- **Source name inconsistency (ch22 p266):** the killed bystander is 姓刘名桓
  ("Liu Huan") then 刘恒先生 ("Mr. Liu Heng"); p260 also "Liu Heng" — a 桓/恒
  source glitch, faithful as rendered.
- **ch24 p017 dittography** (据毕高奎兄提示...重复) already collapsed cleanly in the
  shipped English; **ch22 p243** stray source fragment left faithful.
- 爪牙 rendered "cat's-paw"/"talons and fangs"/"the cat's-paw to the enemy"
  (ch22/ch23/ch24) — a term distinct from 为虎作伥 but sharing the "cat's-paw"
  image; note for R9 so the two idioms stay visibly separate.
- All carried R1-R5 flags still stand.

### Setup note

- setup.sh regression: the ONE known false alarm ("hook stands down on template
  stub") still FAILS as documented at R2-R5 — the kickoff_guard Stop hook is
  correctly ENFORCING because HANDOFF.md carries a real (non-template) kickoff,
  which is precisely what that test inverts. Benign; not a tooling regression, not
  fixed. All other checker regression tests green (including check_numbers after
  the new noise entry).

---

## R7 (ch25, ch26, ch27, ch28, ch29) — register revision pass

Seventh batch of the register pass (REVISION_PLAN.md §3/§5). The middle of the
Third Part (Shanghai): Chapter 5 — the early-war Juntong-Bureau work-review
through Dai Li's quoted work-directions, and the 144-Mauser gift + the Fan Xing
intelligence line (ch25); Chapter 6 — the nameless martyrs, the Xiao family, the
He-Xingjian/Communist-confession analysis, the Xu Shouxin martyrdom, the campaign
to shoot uniformed Japanese soldiers, and the Anti-Japanese Traitor-Killing Corps
(ch26); Chapter 8 — whether the Zhang Xiaolin sanction was really ours, and the
refutation of a forged confession (ch27); Chapter 9 — the agent's state of mind
on killing, the Fu Xiao'an axe-sanction, the Yu Yefeng talk, the seizure of the
concession courts and the Central Reserve Bank (ch28); Chapter 10 Part 1 — the
Liu Yuanshen story and Chen's capture (ch29). **193 edits total** (ch25 30, ch26
56, ch27 17, ch28 65, ch29 25) via `edits/<id>_edits.md` + `apply_edits.py`.

Dominated, as R5/R6, by **DATE accessibility**: these are mission-chronology and
martyr-record chapters, so the bulk is Republic-year and spelled day-month
NARRATION dates -> Gregorian/American (number-check-safe: Republic year N ->
N+1911 per check_numbers.py; month names carry the month numeral). ch28 carries
the heaviest load, including **two diary-paraphrase chronologies** (p145-p152
court, p166-p185 bank) that Chen renders explicitly "以笔者的口气 / in my own voice"
(so NARRATION, converted from the opaque "Xth of the Yth month" form); its
genuinely-quoted Zhou-Fohai diary entries (p103-p104, p153-p154) keep their dates.
**ALL quoted-document dates are LEFT** (§3.1): Dai Li's telegrams and work-orders
(ch25 documents, ch26 p002-p003/p054-p059, ch28 p011); the embedded co-authored
memoirs (Xu Wenqi's "One of the Nameless Heroes" ch26 p090-p103; Zhang Zhiyi's
Communist confession ch26 p062; the forged "Lin Huaibu" letter ch27 p094-p101);
the Japanese "Mainland Gendarmerie" record and its Japanese-language appendix
(ch26 p213-p262); the casualty TABLE (ch26 p170-p206); all news reports (Ta Kung
Pao, Xin Shen Bao, Chung Mei, etc.); the court-agreement article texts (ch28
p131-p140); the Cao Song poem (ch28 p013). The remainder: T1 kill-list words
("of a sudden"/"aught"/"had no wish"/"still less"/"nothing for it but"/"Let it be
marked"/sentence-initial "Besides"); T2 "could not but"/"cannot but" recast to the
plain modal or "could not help"; T6 impersonal "one may say/see/imagine" thinned
where it renders a hedging 可以说/可见/照想 (essayist generalizing "one" kept, §3.2
T6 CAUTION); RULE R1-1 "struck of a heap"->"gave a start"; RULE R1-5 "severally"
thinned and a doubled "besides" de-doubled.

ch29's embedded first-person account by Liu Yuanshen (p018-p062, written for the
book at Chen's request) treated as EDITABLE contributed prose per the R6
Mao-Wanli-monologue precedent — dates converted, clearest calques fixed; its
genuinely-quoted bureau telegrams (p014/p029/p057) and the Chen/Zhu-Min dialogue
LEFT. ch29 p063-p070 repeat ch28's ending verbatim (source doubling across the
chapter seam, a faithful oddity KEPT visible; its dates rendered to MATCH the ch28
R7 edits).

### Tic battery, before -> after (key classes)

| class | ch25 | ch26 | ch27 | ch28 | ch29 |
|---|---|---|---|---|---|
| T1 of-a-sudden | 3->0 | 4->4 | 0->0 | 0->0 | 3->2 |
| T1 no-wish/made-bold/still-less | 1->0 | 3->3 | 3->3 | 3->3 | 0->0 |
| T1 nothing-for-it | 1->0 | 0->0 | 0->0 | 0->0 | 2->2 |
| T1 besides (adv) | 12->12 | 14->13 | 7->6 | 13->12 | 8->8 |
| T1 day-month dates | 0->0 | 0->0 | 0->0 | 0->0 | 0->0 |
| T2 could-not-but/only | 3->1 | 2->2 | 1->1 | 8->5 | 9->6 |
| T6 impersonal "one" | 13->9 | 16->13 | 7->6 | 7->6 | 5->5 |
| T4 >60 / >90 words | 45/13->44/13 | 116/33->112/31 | 39/14->38/14 | 55/18 | 39/7 |
| T3 quoted pairs | 180 | 464 | 0 | 211 | 103 |

The residual T1/T2/T6 counts are dominated by QUOTED DOCUMENTS, which
legitimately hit the battery (§3.1) and are not chased: ch26's of-a-sudden (4) and
no-wish/still-less (3) are inside the Xu Wenqi memoir and the quoted news reports;
its "could not but" (2) likewise. The "day-month dates" battery hits go to 0
everywhere (narration dates converted; quoted-document day-month dates the battery
would flag sit in `>`-free quoted paragraphs it does not scan). "besides" barely
moves because almost all hits are prepositional/tail "besides" (T1 CAUTION), not
the sentence-adverb; the sentence-initial ones were fixed (ch27 p051, ch28 p045).
**Residual note:** ch29's 2 "nothing for it but" (p053, p056) and 2 of the
"could not but" (p053 "rail at myself", p056 "suspect") sit in Liu Yuanshen's
embedded grave account and were LEFT (tic-battery-is-a-flag; the embedded account
handled lightly on register-words, and hand-editing outside the apply_edits
pipeline was declined to keep that do-not-revert contract clean). The T4 >60/>90
counts barely move: the long sentences are quoted documents (stay long, §3.1) and
Chen's periodic set-pieces that LAND (T4 CAUTION); not chased.

### T3 quote policy applied

Near-zero strips this batch, per the R5/R6 precedent (the immediate calibration
target). These Part-3 chapters carry the omnipresent decided org names ("Shanghai
District", "Juntong Bureau", "Beiping Station", "action brigade", etc.) with the
source's 「」 quotes; the ADJACENT revised chapters ch19-ch24 KEEP those quotes in
plain narration (verified: revised ch24 keeps 9 quoted "Shanghai District" in
narration, ch22 keeps 28), so stripping them in ch25-ch29 would make R7 internally
inconsistent with its own neighbours. KEPT for Part-3 consistency and FLAGGED for
the R9 whole-book decision (see reconciliation flags). The quoted pairs otherwise
KEPT are: quoted documents/memoirs/news/telegrams, live dialogue, author-
anatomized terms, marked irony, titles-as-titles, code/cover names, and
note-anchor sites.

### RULE R1-1 / R1-5 fixes

- ch25 p088: 为之一怔 was "I was struck of a heap" — a costume-drama idiom
  (read-aloud test) -> "I gave a start" (RULE R1-1, register).
- ch25 p002/p111: recurring "severally" (RULE R1-5) thinned to "each"/"apart"
  (p057 "severally to four men" kept for variation).
- ch26 p316: a doubled "besides" in one clause (尚且沽名钓誉) de-doubled ->
  "besides gain, angled after name and fame too" (RULE R1-5).

### Recurring-tic watch (RULE R1-5)

"one may say/see/imagine" (ch25 p081/p098/p128/p150/p153, ch26 p007/p027/p069,
ch27 p002, ch28 p043 — varied to "you might say/see", the hedge dropped, or the
plain statement); "severally" (ch25). Watched, not eradicated.

### Spot-audit (>=10% of edited paragraphs per chapter, against the source)

Audited the substantive edits of each chapter against the zh (all date
conversions, the R1-1 fix, the recasts, the impersonal thinning, and each
chapter's tail). All preserve propositional content exactly; every +1911 mapping
verified and confirmed consistent by the 0-unresolved number gate. Sample: ch25
p001 (1937/1940), p050 (1935/1940/1950), p058/p088/p166 recasts; ch26 p084
(1952-53), p136 (Sept 1940-Oct 1941), p231 (1939-40), p292 (Christmas Eve 1940),
p301 (Dec 1983); ch27 p039 (1936/1940, lunar 五月初六 kept lunar), p113 (June
1973/Jan 1976); ch28 p129 (Feb 27/Apr 1, 1930), p145/p166 chronology anchors
(Oct 21/24, 1940), p181 (Jan 6, 1941); ch29 p021 (Changsha fire Nov 12, 1938),
p036 (Dai Li death Mar 17, 1946). Per-chapter number checks all reconcile
(parity by construction; ch25 183 / ch26 321 / ch27 133 / ch28 217 / ch29 70
pairs, 0 unresolved).

### Rejected finding classes (RULE R1-4, by class) — standing calls held through R7

No blind critique this batch (R5 carried one spot check; the second is scheduled
for R8, §8). Standing reject-by-class calls, cited once here: Chen's persona
furniture (笔者 "the writer", humility formulas, the narrating "shall"); quoted
documents, memoirs, telegrams, news, tables, and self-citations (register, length,
archaisms, dates, era-year forms inside them); Chen's interested-witness heat (the
traitor/martyr register, the anti-Communist verdicts, the reverence set-pieces —
the "ground to powder" close ch25 p183, the "living sacrifice" ch26); decided
glossary renderings; set-off markers; note anchors; chengyu that land; the
source's own faithful oddities (the ch26 p116-p122 garble; the ch29 chapter-seam
doubling). Chen's formal dialogue to superiors/subordinates stays formal (§3.2 T5
CAUTION); the already-colloquial Zhu-Min dialogue (ch29 p051) LEFT as rendered.

### Checks (all green)

- Parity by construction; `verify_unit.py` per chapter: numbers 0 unresolved
  (ch25 183 / ch26 321 / ch27 133 / ch28 217 / ch29 70 pairs), anchors all resolve
  (ch25 10 / ch26 11 / ch27 6 / ch28 8 / ch29 9).
- `check_align.py` per unit OK (no pair strays > 2.2x from the unit median).
- `check_content.py`: no displacement flag on any R7 unit; the only failures are
  the documented benign homograph/substring false positives (ch08 Shunde, ch09
  Jize, ch13, ch26, ch38, ch41 — ch26's did not even fire this pass), unchanged.
- `check_register.py --ref reference/R1_frozen.md`: **all five flag STILTED — the
  ch08/ch12/ch17/ch21-class documentary false positive** (contractions ~0 because
  the free speech is quoted documents/memoirs plus grave narration; shall% is
  document-borne — ch26 83% is entirely Dai-Li-telegram + Xu-Wenqi-memoir + Zhang-
  Zhiyi-confession + gendarmerie-record "shall", ch25 60% likewise; ch27 shall% 0%,
  flagged only for near-zero dialogue in an analytical chapter). Confirmed
  document-borne by inspection; NOT chased, consistent with R6 ch21/ch22/ch24.
- Build + `qa_epub.py`: **PASS** (57 files, 50 documents, 6160 paragraphs, 375
  refs / 375 bodies / 375 backlinks, all links resolve). **epubcheck 5.1.0: 0
  fatals / 0 errors / 0 warnings / 0 infos** (EPUB 3.3).
- Checker regression tests (setup.sh): green except the one documented benign
  false alarm ("hook stands down on template stub", Setup note below); the three
  new noise entries did not disturb check_numbers (pass-fixture OK, fail 5/5).

### Noise entries added (data/noise.txt) — do-not-revert

- `四十一、二` (ch26 p084): elided Republic-year pair 民国四十一、二年 = 1952-53; the
  、二 elides 四十二 (42), so the checker reads 四十一 (41) and a bare 二 (2). English
  "1952 or 1953"; the lone 2 has no match. Same class as R5's `五十一、二`.
- `李圣五` (ch28 p146): the personal name 李圣五 (Li Shengwu) ends in 五 (5); the old
  narration date "the twenty-fifth of the tenth month" had been supplying that 5
  via "fifth", so converting to "October 25" orphaned it (RULE R1-3). The 五 is
  part of the name, not a quantity.
- `三十几` (ch29 p036): approximate age 三十几岁 "in his thirties" (thirtysomething);
  the checker reads 三十 (30), which the old "the thirty-fifth year" supplied via
  "thirty"; converting Dai Li's death to "March 17, 1946" orphaned it (RULE R1-3,
  R5 latent-match class). Not a hard quantity.
- Earlier R1-R6 entries all stand (incl. R6's `四○七`).

### RULE R1-3 latent matches surfaced (documented, not contorted)

- ch28 p146 (`李圣五`) and ch29 p036 (`三十几`) above — both are the canonical R1-3
  case (a spelled ordinal in the old date had been silently covering a
  name-numeral / approximate-age numeral), fixed by a documented noise entry, not
  by contorting the date wording. Watch this class on every date edit that drops a
  spelled ordinal near a name-with-digit or an approximate quantity.

### R9 / whole-book reconciliation flags (NOT changed in R7)

- **T3 Part-3 org-name quotes:** ch19-ch29 uniformly KEEP the source's 「」 quotes
  on the recurring decided org names ("Shanghai District"/"Juntong Bureau"/etc.)
  in plain narration (the T3 rule's letter would strip them, but ch06-ch12 already
  stripped their own occurrences and the later Part-3 batches kept theirs for
  volume/consistency). R9 must make the book-wide call and, if it strips, grep
  every built unit and rebuild; note-anchor sites keep their quotes regardless.
- **SOURCE GARBLE, ch26 p116-p122:** the ZH is OCR-corrupted (池区范国, 二十丸年,
  甫眼虔, etc.) though the shipped English is clean; R7 avoided date edits in that
  band (except p116, whose 二十九年初 is readable and orphan-safe). A digitization
  glitch to record; nothing to correct in the English.
- **沐猴而冠 drift widens:** ch28 p023 "a monkey dressed up as a man" — cf. ch18
  p010 "play the monkey in a hat", ch24 p098 "a monkey crowned and gowned". Now
  THREE variants; reconcile in R9 (candidate for an F0 note).
- **为虎作伥/tiger-cat's-paw:** ch28 p072 (in the quoted Ta Kung Pao report) renders
  为虎作伥 as "played the tiger's cat's-paw" — a QUOTED-doc instance, LEFT; note it
  alongside the four narration variants (ch14/ch17/ch22/ch23) for the R9 decision,
  but it stays as quoted-source wording.
- **Chapter-seam doubling (ch28 -> ch29):** ch29 p063-p070 repeat ch28 p210-p217
  near-verbatim (the source overlaps the chapter boundary). Rendered identically
  in R7 (same date edits); a faithful source structural repeat, not to be silently
  merged. R9 note only.
- **Xu-name / 圣五 etc.:** the ch28 p146 Li Shengwu name-numeral now noised (above).
- All carried R1-R6 flags still stand (为虎作伥 four narration variants; 沐猴而冠;
  ch24 p085 gendarme-roster 二十/二十七 source typo; ch22 p266 桓/恒; 爪牙 vs
  为虎作伥 image overlap; the R1-R5 flags).

### Setup note

- setup.sh regression: the ONE known false alarm ("hook stands down on template
  stub") still FAILS as documented at R2-R6 — the kickoff_guard Stop hook is
  correctly ENFORCING because HANDOFF.md carries a real (non-template) kickoff,
  which is precisely what that test inverts. Benign; not a tooling regression, not
  fixed. All other checker regression tests green (including check_numbers after
  the three new noise entries).

## R8 (ch30, ch31, ch32, ch33, ch34, ch35) — register revision pass

Eighth batch of the register pass (REVISION_PLAN.md §3/§5). The Third-Part close
plus the whole FIFTH Part opening: Chapter 10 Part 2 — Liu Yuanshen's own arrest
account and Chen's capture (ch30); the Third-Volume front matter — "Written
Before the Third Volume Went to Press" (ch31) and the "Author's Preface" (ch32);
and the Fifth Part's first three chapters — the Lizhi Class / Pacification Corps
and Chen's return to Beiping (ch33), the corps organization and the three
"briefings" (ch34), and the Li-Mingqiu / Lin-Biao / Tao-Zhu strategic-intelligence
case (ch35). **141 edits total** (ch30 31, ch31 4, ch32 20, ch33 46, ch34 18,
ch35 27) via `edits/<id>_edits.md` + `apply_edits.py`; ch30's last 5 are the
blind-critique ACCEPTs (below).

Dominated, as R3-R7, by **DATE accessibility**: the Fifth-Part chapters are
mission-chronology and career-recap chapters saturated with Republic-year
NARRATION dates -> Gregorian (number-check-safe: Republic year N -> N+1911, which
`check_numbers.py` resolves natively via `(m+1911) in target`; month names carry
the month numeral). ~86 date phrases converted across the six. **ALL
quoted-document dates LEFT** (§3.1): Chiang's opening-ceremony addresses (ch33
p004/p017), the Liu Peichu memoir *Fleeting Glimpses of a Floating Life* (ch33
p014/p021/p027, ch34 p032, ch35 p017/p087), the Luo Jing autobiographical excerpt
(ch33 p118-p134 — a bracketed 兹摘录如下 EXCERPT of another man's first-person
life-account, treated as a QUOTED DOCUMENT and LEFT WHOLE, its many dates
untouched — distinct from the Liu Yuanshen ch30/ch29 account, an un-quoted
contributed narrative section that IS edited), the Li Yulin 事略 (ch33 p111),
the self-quoted Book-1 telegram (ch33 p108), the US-spokesman statement (ch33
p001), Wang Zhaofen's account (ch34 p029-p030), Tao Zhu's and Li Mingqiu's
reported speech (ch35 p130/p161-p185). ch30's opening section 3 IS Liu Yuanshen's
own arrest account "set down in his own hand" — EDITABLE contributed prose per
the R6/R7 (Mao Wanli / Liu Yuanshen) precedent — its dates converted; sections
4-5 are Chen's own capture narrative. The remainder: T1 kill-list
(of-a-sudden->suddenly/all-at-once ×6 in ch30; bethought/bethinking; no-help-for-
it / nothing-for-it; in-this-wise; adverbial "besides"); T2 could-not-but /
could-only recasts and a couple of 失信背约 / 兼-doubling de-doublings (RULE R1-5);
T6 impersonal "one" thinned to I/you/which-shows WHERE it renders a generic
self, the **essayist "one" KEPT** (ch34/ch35 are heavily reflective; §3.2 T6
CAUTION); RULE R1-1 wrong-image fix 硬着头皮 "harden my scalp" -> "steel myself"
(ch30). A very few T5: 2 contractions for the casual young speaker Zhou (ch30).

### Tic battery, before -> after (classes that moved; DATE work is not visible here)

| class | ch30 | ch31 | ch32 | ch33 | ch34 | ch35 |
|---|---|---|---|---|---|---|
| T1 of-a-sudden | 6->0 | 0 | 0 | 3->2 | 1->0 | 0 |
| T1 nothing-for-it | 0 | 0 | 0 | 1->0 | 0 | 2->0 |
| T1 besides (adv) | 8->8 | 1->0 | 5->4 | 11->10 | 8->8 | 8->8 |
| T1 day-month dates | 0->0 | 0 | 0 | 0 | 0 | 0 |
| T2 could-not-but/only | 6->3 | 0 | 1->0 | 2->2 | 3->3 | 11->10 |
| T2 litotes | 5->5 | 1->0 | 1->1 | 2->1 | 3->3 | 5->5 |
| T6 impersonal "one" | 4->1 | 0 | 2->0 | 12->9 | 8->8 | 15->15 |
| T4 >60 / >90 words | 30/6 | 2/0 | 12/1 | 48/16->47/15 | 47/12->45/12 | 43/13->43/12 |
| T3 quoted pairs | 0 | 0 | 73 | 0 | 0 | 0 |

The **"day-month dates" battery row stays 0 because the Republic-year narration
dates this batch converts are of the "the thirtieth year of the Republic" /
"the seventh month" FORM, which that grep (built for "10 November" numeric
day-month) never counted; the ~86 conversions are the batch's real bulk and are
invisible to the battery** (the number gate, 0 unresolved across all six, is
their proof). Residual T1/T2/T6 counts are dominated by (a) essayist "one" in the
reflective chapters (ch34/ch35 — KEPT, §3.2 T6 CAUTION), (b) "besides" that is
prepositional/tail, not the sentence-adverb (T1 CAUTION), and (c) faithful
"could only" (只好/只有) and grave litotes inside Chen's/Liu's deliberate register.
T4 barely moves: the long sentences are quoted documents (stay long) and Chen's
periodic set-pieces that LAND (T4 CAUTION); the two ACCEPTED splits (ch30 #233,
and the ch33/ch34 seams) are the only topology touches.

### T3 quote policy applied

Near-zero strips, per the R5/R6/R7 precedent. ch32's 73 quoted pairs are the
Fifth-Part org/plan/term-of-art names ("Committee of Three", "Lizhi Plan",
"Pacification Corps", the rail lines, "pacification"/"intelligence"/"action"/
"assault", etc.) and the quoted Liu Peichu memoir; ch33/ch34/ch35 carry the same
decided org names with the source's 「」 in plain narration. The book-wide strip
decision remains DEFERRED to R9 (see reconciliation flags); KEPT this batch for
consistency with the adjacent Part-3/Fifth-Part chapters. Quotes otherwise KEPT
at naming/anatomizing sites, marked irony, titles, code/cover names, quoted
documents, dialogue, and note-anchor sites.

### Spot-audit (>=10% of edited paragraphs per chapter, against the source)

Audited each chapter's substantive edits against the zh (all date conversions,
the R1-1 fix, the recasts, the impersonal thinning, and each chapter's tail). All
preserve propositional content exactly; every +1911 mapping verified and
confirmed by the 0-unresolved number gate. Sample: ch30 p001 (June 28, 1941),
p021/p085 (Oct 29-30, 1941), p014 硬着头皮->"steel myself"; ch31 p010 (Dec 27,
1939 martyrdom date); ch32 p005 (1946), p018/p024 (Sept 1947), p031 (1950-51),
p034 (end Jan 1949); ch33 p002/p011 (1946), p013 (mid-Mar 1946), p017 (July 20,
1947), p030 (1914), p083 (1933/1939/1947), p107 (1938-39; 民前七年 LEFT), p145
(Aug 1945); ch34 p006 (spring-summer 1949), p054 (1986 = year of writing), p060
(1924-25; 1938), p089 (Apr 1933), p115 (Jan-Aug 1939); ch35 p028 (late autumn
1947), p051 (spring 1926), p091 (1947-48), p102 (1936), p125 (Apr 1927), p128
(summer 1930), p155 (end 1947-autumn 1948), p191 (1949; 1951). Per-chapter
number checks all reconcile (parity by construction; ch30 108 / ch31 14 / ch32 35
/ ch33 151 / ch34 127 / ch35 194 pairs, 0 unresolved). Tails re-read against zh:
all faithful and intact.

### SECOND blind critique (§8/§9.2) — revised ch30, adjudicated ACCEPT/REJECT-by-class

The verbatim §5.6 blind-reader prompt was run on the REVISED ch30 (alone, no
source, no plan, no repo context) by a context-blind reader. It returned **354
findings** — an aggressive modern-neutral read that, as predicted by RULE R1-4,
flags Chen's persona and deliberate gravity wholesale.

**ACCEPTED (5) — genuine errors, none of them persona; folded into ch30:**
- #5 (p002): participle-to-finite tense shift "first riding two stops... then got
  off" -> "first rode... then got off".
- #54 (p008, dialogue): RULE R1-1 wrong-image "call this Mr. Zhang a Yangzhou
  fried rice" (叫 = order food; "call sb a X" = insult) -> "order".
- #104 (p014): dangling participle "My heart was uneasy, not knowing what I
  waited for" -> "Uneasy, I had no idea what I was waiting for" (RULE R1-2).
- #233 (p063): syntactic ambiguity "neither of them tall, thick-set and stoutly
  built" -> "Neither of them was tall; both were thickset and solidly built".
- #300 (p087): opaque archaism "two possible bournes" -> "two possible
  destinations".

**REJECTED-by-class (the other ~349), with reason (RULE R1-4):**
- *Deliberate grave/formal register = the §3.1 TARGET, not a defect* (~150+):
  "wretched past telling", "past all bearing", "beyond all looking-for", "at the
  very pass of life and death", "in the broad, brazen light of day", "a thing not
  to be borne thinking of", "how should I not be grateful?", the narrating "shall",
  the periodic build-ups. The read-aloud test keeps these: a grave old officer CAN
  say them; they are Chen's/Liu's persona (content), which this pass modulates, not
  razes. The blind reader is calibrated to modern-neutral, which §3.1 explicitly
  rejects for Chen's voice.
- *Rendered chengyu / idiom-images to KEEP for their picture (§3.3) and annotate
  in F0, NOT smooth away* (~40): 刀山火海 "mountains of knives and seas of fire",
  粉身碎骨 "dashed to powder and bits", 釜底抽薪 "take the firewood from under the
  cauldron", 死不瞑目 "eyes that could close", 狗急跳墙 "a cornered dog will leap the
  wall", 生死关头, 察言观色, 衣冠禽兽 "a beast in man's clothes", 疑心生暗鬼 "suspicion
  breeds its phantoms".
- *Cultural terms / character-decompositions left in scare-quotes pending the F0
  FOOTNOTE pass — not the register pass's job* (~25): "pig-cage van" (猪笼车),
  "three-stripe head" (三道头), the 立早章 Zhang name-decomposition, "turtle's egg"
  (王八蛋), "Second Master" (二爷), "rice-bowl" as livelihood (饭碗), 久仰 "I have
  long admired the name", the 老同事/新同事 pun. These are FLAGGED for F0 (§12), not
  changed here.
- *Faithful renderings whose "fix" would distort the source* (~30): #235 "they
  liked to shove and jostle" (source 喜欢 = were fond of); #188 "a black glass bead
  glinting in the crack" (the source keeps Liu's not-sure-what-it-is ambiguity);
  #242 "open-handed" (a defensible reading of the author's ironic 「大方」); the
  emotion-lists and the deliberate 坐南朝北-type source repetitions.
- *Recurring-tic observations logged as a RULE R1-5 WATCH for R9's book-wide
  sweep, not chased in a spot-checked chapter* (see below): #89 the "no little /
  no few / not a few / no small" litotes family; "of set purpose" for 故意; "as I
  recall" hedges; "one sheet of" for 一片; the rhetorical-question deduction habit.

**Verdict:** the blind critique confirms the pass is on target for its own brief
— the reader stops at register only where the register is Chen's DELIBERATE
persona (RULE R1-4 exactly as R1 found: the great bulk of flags name the
protected furniture), and the genuinely actionable errors it surfaced (5) were
real and are fixed. This is the register pass's success signal, not a defect
signal (§10: "a blind reader should stop flagging register within two spot
checks" — the residue is persona/idiom/footnote-pass, which by design it will
keep naming until F0 annotates the idioms and the register is read WITH its
persona in mind).

### New §3.5 rule (append to REVISION_PLAN.md at R9 if it recurs)

- **RULE R8-1 (proposed): the "no little / no few / not a few / no small" litotes
  family is a recurring tic to sweep book-wide in R9.** WHY: the R8 blind read
  named it "the single most pervasive translationese tic" in ch30 (a dozen-plus
  instances). It is already on the T2 kill-list ("litotes counting"), but the
  QUALITY-litotes form ("a man of no little depth") reads as grave register and
  was left case-by-case; the QUANTITY form ("no small number", "no few comrades")
  should be thinned. FIX: R9's whole-book pass greps `no (little|few|small)\b` and
  `not a few` and thins the quantity instances to "a good many / quite a few /
  considerable", keeping a grave quality-litotes only where it genuinely lands.
  CHECK: the grep count drops materially book-wide.

### Noise entries added (data/noise.txt) — do-not-revert

- `郑、毛两位` (ch33 p083): counter-by-naming "Messrs. Zheng and Mao, the two of
  them"; both named in the English, so 两 (2) is a counter, not a tracked value
  (cf. 陈、齐两位 / 周、朱两人). RULE R1-3 latent match: the old date wording
  "twenty-second year" matched `\bsecond\b`->2 and had been covering this 两;
  converting to "1933" orphaned it.
- `三十六、七` (ch35 p091): elided Republic-year pair 三十六、七年 = 1947-48; 、七
  elides 三十七, so the checker reads 三十六 (36) and a bare 七 (7). Rendered "1947
  or 1948" (+1911); the old "thirty-seventh" carried the 7 via `\bseventh\b`.
  Strip the whole elided pair (English carries the years). Same class as 二十七、八.
- `卅二` (ch35 p059): 卅二年 = the 32nd Republic year (1943); 卅 (a variant of 三十)
  is NOT in the checker's CJK-numeral charset, so 卅二 reads as a bare 二 (2) that
  the old "thirty-second year" covered via `\bsecond\b`. Rendered "1943" orphaned
  it (RULE R1-3). Strip the mis-parsed pair.
- All R1-R7 entries stand.

### RULE R1-3 latent matches surfaced (documented, not contorted)

- ch33 p083 (`郑、毛两位`), ch35 p091 (`三十六、七`), ch35 p059 (`卅二`) above — all
  three are the R1-3 class: a spelled ordinal or elided form in the old date had
  been silently covering a counter / elided-tens / variant-glyph numeral, fixed by
  a documented noise entry, not by contorting the date. The `卅二` case adds a new
  sub-species: a VARIANT NUMERAL GLYPH (卅 for 三十) outside the checker's charset;
  watch for 卅/廿 forms on every date edit.

### R9 / whole-book reconciliation flags (NOT changed in R8)

- **T3 org-name quotes now span ch19-ch35** all KEEP the source's 「」 on the
  recurring decided org names in plain narration; R9 makes the book-wide strip
  call (ch32's 73 pairs are the densest single-chapter instance — org/plan names).
- **Rail-line rendering drift:** 津浦(铁路) appears as "Jin-Pu Railway" (ch33
  p035/p109, ch35) AND "Tianjin-Pukou line" (ch32 p019); 平汉 as "Ping-Han" and
  "Beiping-Hankou line"; 北宁 as "Bei-Ning" and "Beiping-Liaoning line" (a note
  anchor at ch34 p019). R9 reconcile the line names book-wide (anchor sites keep
  their form).
- **第二处 rendering:** "Second Section" (ch33 p075/p099, ch34, ch35) vs the earlier
  §R3 flag "Second Bureau"(ch09)/"Second Department"(ch05); and 第二厅 "Second
  Bureau"(ch33 p013). R9 decide 处/厅 (Section/Bureau/Department) book-wide.
- **民前 forms LEFT unconverted** (ch33 p107 民前七年 "the seventh year before the
  Republic" = 1905; +1911 does not apply to 民前, per the §R5 ch18 precedent).
- **Contributed-account boundary ruling (R8):** an embedded first-person account
  is EDITABLE narration when it is an un-quoted narrative SECTION written for the
  book (Liu Yuanshen ch29/ch30, Mao Wanli ch21) but a QUOTED DOCUMENT, left whole,
  when it is a bracketed 摘录 EXCERPT of the person's own writing (Luo Jing ch33
  p118-p134). R9 note the distinction.
- **RULE R8-1 litotes sweep** (above) — the whole-book quantity-litotes thin.
- All carried R1-R7 flags still stand (为虎作伥 four+ variants; 沐猴而冠 three
  variants; the ch23 为虎作伥 NOTE ANCHOR to move; the ch26 p116-p122 SOURCE GARBLE;
  the ch28->ch29 seam doubling; 爪牙 vs 为虎作伥 image overlap).

### check_register (documentary/narration false positive, NOT chased)

All six flag STILTED — the documented ch08/ch12/ch17/ch21/ch26-class false
positive for narration-and-quoted-document-dominated chapters (contractions ~0
because Chen's/Liu's narration is uncontracted by persona; ch33 shall% 80% is
document-borne — Chiang's/Liu Peichu's quoted addresses; ch34/ch35 are
essay+narration with almost no dialogue). NOT chased (the dialogue that exists —
captors, officials, Chen concealing identity — is formal BY DESIGN; ch30 added 2
Zhou contractions where a casual young speaker genuinely warranted them).

### Fidelity gates (all green)

Parity by construction (make_bilingual refuses a count mismatch); numbers 0
unresolved across all six (108/14/35/151/127/194 pairs); note anchors all resolve
(ch30 5 / ch31 3 / ch32 10 / ch33 6 / ch34 3 / ch35 8); check_align OK on all six;
check_content (--config checks.json) shows all six "all in the paired paragraph"
(no displacement; the DISPLACED units ch08/ch09/ch13/ch26 are the documented
benign homograph/substring false positives, none in R8 scope). Build: qa_epub
PASS (57 files, 50 documents, 375 refs/375 bodies/375 backlinks, all links
resolve); epubcheck 5.1.0 **0 fatals / 0 errors / 0 warnings / 0 infos** (EPUB
3.3). Committed and pushed at every chapter boundary (six commits) plus this
close.

### Setup note

- setup.sh regression: the ONE known false alarm ("hook stands down on template
  stub") still FAILS as documented at R2-R7 — the kickoff_guard Stop hook is
  correctly ENFORCING because HANDOFF.md carries a real (non-template) kickoff,
  which is exactly what that test inverts. Benign; all other checker regression
  tests green (including check_numbers after the three new R8 noise entries).

---

# R9 — ch36 through ch43 plus the whole-book close (register revision, FINAL register batch)

Scope: ch36, ch37, ch38, ch39, ch40, ch41, ch42, ch43 (Chapters 4 through 10 of
the Fifth Part plus the Afterword), then the whole-book close per REVISION_PLAN
§8. English-to-English only, content frozen. About 229 edits total (ch36 47,
ch37 11, ch38 10, ch39 32, ch40 66, ch41 31, ch42 30, ch43 2), of which the
three-plus-two listed under "close" below were caught by the close rather than
the per-chapter passes.

## Dominant edit = DATE accessibility (Chen's narration only; +1911)

R9's eight chapters are heavy with Chen's own narration (ch39, ch40, ch41 are
military chronologies), so the batch converted roughly 230 Republic-year AND
spelled day-month narration dates to Gregorian and American order. Quoted
documents and reproduced comrade accounts were LEFT WHOLE with their internal
dates and period register, per §3.1. The reproduced-account boundaries handled
this batch:

- **Left whole (quoted / reproduced accounts, dates and archaisms preserved):**
  Xiao Runyu's and Niu Guangjin's essays (ch36); Lu Deming's, Chang Shaozeng's,
  Tian Yingjie's combat memoir, and Bai Jiaqi's verse song (ch37); Wang Zhiyi's,
  Wang Hongzhu's, Chang Shaozeng's, Wu Chunxiang's accounts (ch38); Wang
  Zhaofen's, Meng Guangdi's, Zhang Luying's accounts, the Deng Wenyi report,
  and the Dagong Bao chronology excerpt p129-p142 (ch39); the Nie Jining
  telegram, the Guangming Ribao passage, the National-Defense week-report, the
  Dagong Bao notice, and Chen's own Soliloquy self-citation (ch40); the
  "lessons" staff document, Wang Hongzhu's withdrawal account, the Zhu Zhankui
  intel report, the Lin/Luo surrender letter, and the dynastic reign-year dates
  p123 which already carry their Gregorian year in parentheses (ch41); Zhang
  Luying's, Wang Hongzhu's, Feng Zhijun's, Xiao Runyu's, Wu Chunxiang's accounts
  (ch42).
- **Editable contributed account (R8 precedent / HANDOFF names Liu Yuanshen):**
  Liu Yuanshen's UN-QUOTED supplement (ch42 p093-p099) is editable narration;
  its dates converted. Wang Zhaofen's numbered-section account (ch39, rendered
  without per-paragraph quotes) was treated as a reproduced document and LEFT,
  for consistency with the other comrade accounts.
- **笔者附注 rule:** Chen's writer's-notes OUTSIDE a quoted block convert
  (ch36 p108, ch39 p143 tail, ch40 p128); those embedded INSIDE a quoted block
  stay with it (ch36 p113/p130, ch37 p018/p037, ch42 p073), for visual
  uniformity within the reproduced text.

## New noise.txt entry (RULE R1-3)

- `三十八、九` (ch40 p101, elided 1949-50; the 、九 elides 三十九, so the checker
  reads 三十八 and a bare 九). Do-not-revert. Same class as R8 三十六、七 and R7
  二十七、八 / 四十一、二. The other elided forms this batch needed (九十月,
  十一、二日, 十x redacted-day) were already noised.

## Two genuine catches by the mechanical gates

1. **check_numbers, ch40 p045/p048:** 三十五年 (Republic 35) was first rendered
   1936; the checker flagged the orphaned 35, and 35+1911 = 1946 (the Marshall
   cease-fire of January 1946, the PLA renaming of 1946). Both corrected to 1946
   and re-verified. A confusion of 三十五 (35) with 二十五 (25); the number check
   exists for exactly this.
2. **Whole-book Republic-year sweep (the close):** three narration dates were
   missed in the per-chapter passes and caught by the close: ch36 p062 (三十七年
   年底 -> end of 1948), ch39 p041 (三十七年 -> 1948, the Laishui-campaign
   sentence), ch40 p063 (三十五年 -> 1946, the unit-designation confusion). All
   fixed, recorded in the edits files under an "R9 whole-book close" marker, and
   re-verified.

## Register (T1/T2), tic before -> after (R9 chapters)

Selected classes; full battery saved during the pass. "besides" survivors are
prepositional or quoted; "could only" survivors are natural English or quoted;
"one" survivors are the essayist codas (T6 CAUTION). Quoted documents legitimately
hit every class.

| unit | could-not-but/only | litotes no small/few | impersonal one | sent >60/>90 |
|---|---|---|---|---|
| ch36 | 8->6 | 6->1 | 22->21 | 63/8 |
| ch37 | 4->4 | 2->2 | 5->5 | 53/14 |
| ch38 | 1->1 | 1->0 | 5->5 | 73/19 |
| ch39 | 5->4 | 7->4 | 13->12 | 57/14 |
| ch40 | 5->5 | 4->0 | 13->13 | 53/16 |
| ch41 | 3->3 | 2->2 | 7->7 | 48/7 |
| ch42 | 8->8 | 7->4 | 16->16 | 41/8 |
| ch43 | 1->1 | 0->0 | 1->1 | 7/0 |

T4 sentence topology was left essentially untouched (§3.2 T4 CAUTION: most long
sentences are quoted documents or Chen's deliberate periodic build-ups that
land; triage the >90-word two-spine narration cases only, of which R9 met none
worth splitting). Litotes was the main register lever this batch (RULE R8-1
quantity-form sweep), plus T1 trailing/adverbial "besides," "of a sudden,"
"nothing for it but," and a handful of T2 "could not but" recasts.

## Spot-audit (10% of edited paragraphs, and the R9 deep audit)

Per-chapter spot audits were satisfied as the batch ran (parity by construction;
numbers 0 unresolved per chapter, which is the mechanical proof that every date
edit carried its source numerals). The whole-book close then ran the deep-audit
protocol on 10 fresh EDITED pairs spanning every edit class (ch36 p086 litotes,
ch37 p038 could-not-but, ch38 p038 litotes, ch39 p098 could-not-but, ch40 p045
the 1946 date-fix, ch40 p012 of-a-sudden, ch41 p041 date+of-a-sudden, ch42 p024
nothing-for-it, ch42 p093 Liu-Yuanshen date, ch43 p008 besides): 10 of 10
faithful, zero substantive errors. Every register edit preserves the source's
propositional content exactly.

## Rejected / left-by-class (RULE R1-4)

- The narrating "shall" (KEEP #1): net delta 0 across the whole R9 diff. Same
  for "sanction," "traitor," "Juntong," "Beiping" (each net delta 0). The
  mechanical date pass did not over-correct any KEEP-list item.
- Quoted-document dates and archaisms: left whole (see the accounts listed
  above). The remaining "the Nth year" forms in the R9 chapters (ch36 8, ch38
  17, ch42 8, and the rest near zero) are, on classification, all quoted-account
  dates, quoted-title dates, dynastic reign-years with parenthetical Gregorian,
  or "the eight years" duration forms.
- Essayist "one" (T6 CAUTION): the intelligence-value codas (ch36) and the
  Afterword's grave reflective register (ch43) were left; the Afterword took
  only two trailing-"besides" edits.

## Whole-book close (REVISION_PLAN §8)

- **check_reconcile.py:** no hard failures. Drift candidates are homograph/
  substring anchor coincidences (热边区 vs 冀辽热; 奋鬪精神 near different year
  numbers) and are not real rendering drift. Epithet drift 433 candidates flagged
  for a human read (informational). Glossary forward 675/708 decided forms
  present; the ~33 unused forms are pre-existing curation artifacts (glossary/
  note-only long forms such as "the Tianjin-Pukou Railway," whose prose uses the
  decided short form "Jin-Pu"). Spelling locale 0 British / 775 American.
- **Rail-line drift (HANDOFF §R8 flag) resolved:** prose uses the hyphenated
  short forms uniformly (Jin-Pu 18, Ping-Han 26, Bei-Ning 13, Ping-Sui 14); the
  long descriptive forms are glossary-only. No prose drift.
- **KEEP-list diff-grep (§3.3):** done, net delta 0 for shall/sanction/traitor/
  Juntong/Beiping; set-off markers untouched.
- **Grep-count of ~20 decided renderings:** consistent book-wide (Juntong 90,
  Beiping Station 109, Bandit-Suppression Headquarters 91, Lizhi Class 64,
  Fu Zuoyi 81, Lin Biao 76, Zhu Zhankui 86, etc.). "People's Liberation Army"
  reads 0 only because the grep used a straight apostrophe against the text's
  curly one; the term is present throughout.
- **Deep audit re-run (§10):** 10/10 faithful (above).
- **Build:** qa_epub PASS (57 files, 50 documents, 375 refs/375 bodies/375
  backlinks, all links resolve); epubcheck 5.1.0 **0 fatals / 0 errors / 0
  warnings / 0 infos** (EPUB 3.3). One note anchor moved (ch42 "no few old
  soldiers" -> "a good many old soldiers") with its paired NOTE-ANCHOR; the note
  body still resolves. notes.json book-wide total 375 (unchanged; R9 added no
  notes).

## Fidelity gates (all green)

Per-chapter, as the batch ran: parity by construction; numbers 0 unresolved
(ch36 187 / ch37 144 / ch38 135 / ch39 179 / ch40 169 / ch41 200 / ch42 200 /
ch43 31 pairs); note anchors all resolve (8/8/8/8/9/9/10/3); check_align OK on
all eight; check_register STILTED on the essay/chronicle chapters is the known
documentary/near-zero-dialogue false positive (contractions ~0 because these
chapters are narration and quoted accounts with almost no dialogue), consistent
with R7/R8, not chased; ch37/ch39/ch41/ch42/ch43 read "within tolerance."

## Setup note

- setup.sh regression: the ONE known false alarm ("hook stands down on template
  stub") still FAILS as documented since R2 (the kickoff_guard Stop hook is
  correctly ENFORCING because HANDOFF.md carries a real, non-template kickoff,
  which is exactly what that test inverts). Benign; all other checker regression
  tests green (including check_numbers after the new 三十八、九 noise entry).

## NEXT

The R1-R9 register pass is COMPLETE. Per REVISION_PLAN §8/§12 and the standing
commissioner directive, R9 does NOT declare the book complete: it serves the
F0 FOOTNOTE-DENSITY pass kickoff. HANDOFF.md's next-chat message is now the F0
kickoff (§12.5), and the R9 reply serves that kickoff in place of a completion
notice.

---

# F0 — FOOTNOTE-DENSITY PASS (single wave, whole book) — IN PROGRESS

Authority: REVISION_PLAN.md §12. Content FROZEN; notes only. Baseline at
start of F0: 375 translator notes (per-chapter start counts recorded below).
Method per chapter (§12.3): read shipped English against the Chinese source
in aligned chunks; list every term/person/place/event/institution/allusion a
non-specialist Western reader would miss; check glossary.json + existing
notes.json FIRST (no duplicates; first-appearance discipline — grep earlier
occurrences); draft with real sources and stated verdicts; author via
apparatus_merge.py; check_apparatus clean; rebuild + qa_epub (+ epubcheck);
commit AND PUSH at every chapter boundary.

**RESUME POINT:** see the "F0 chapter ledger" line below for the last COMPLETE
chapter. An interrupted session resumes from the next chapter with the SAME F0
kickoff (REVISION_PLAN §12.5). Do not spawn a new batch id.

## F0 chapter ledger (last COMPLETE chapter = ch08)

- **ch01 (Foreword) — DONE.** Notes 6 -> 10 (+4). New notes span all four
  kinds/domains:
  - `the storyteller's embroidery` — 演义 <i>yanyi</i>, the historical-romance
    genre (literary culture; e.g. *Romance of the Three Kingdoms*). Chen
    disclaims writing a yanyi. Source: standard literary reference
    (Wikipedia, "Romance of the Three Kingdoms" / the yanyi genre).
    Verdict: corroborated.
  - `a martyr's death` — 成仁 <i>chengren</i>, allusion to *Analects* 15.9
    (卫灵公, 杀身成仁); the set phrase 成功成仁. Source: Chinese Text Project
    (ctext.org, Wei Ling Gong 9) + Legge translation. Verdict: corroborated
    (canonical).
  - `a scale and half a claw` — 一鳞半爪 idiom; a dragon glimpsed in cloud,
    hence any fragmentary view. Source: Baidu Baike 一鳞半爪 (earliest attr.
    Tang, 高仲武《中兴间气集》; poetics locus 赵执信《谈龙录》, variant 一鳞一爪).
    Verdict: corroborated.
  - `the thread that stitches the pages together` — 钉书的线 / 线装
    (thread-bound books), material culture. Source: standard reference on
    Chinese traditional bookbinding (线装书). Verdict: corroborated.
  - NOT re-noted in ch01 (already covered by the 6 pre-F0 notes): War of
    Resistance; 特务工作 tewu gongzuo; 活口 huokou; 忠烈祠 Martyrs' Shrine /
    奉祀忠烈; the title 英雄无名; the five-part plan. Considered and DECLINED
    (would be padding): 可歌可泣, 故神其说, 二三十年代 (decade explicit in the
    English), 名节, 自我标榜.
  - ch01 is the book's least concrete chapter (an abstract, reflective
    foreword); downstream narrative chapters carry far more concrete
    references (people, places, units, weapons, currency, geography) and will
    be much denser. +4 here is the honest density for a foreword.

- **ch02 (Introduction: Rooting Out Traitors in the North) — DONE.** Notes 20 -> 27 (+7).
  New: `courtesy name Yunong` (the <i>zi</i>/courtesy-name convention, social structure);
  `the French Concession of Tianjin` (Tianjin's foreign concessions / extraterritoriality,
  institutions); `the Northwest Army` (Feng Yuxiang's 西北军 warlord army, recurring
  affiliation); `the plum tree withered in the peach tree's place` (李代桃僵 idiom, 11th
  of the Thirty-Six Stratagems, Han yuefu 《鸡鸣》 — Baidu Baike; texture); `Dairen`
  (Japanese-held Dalian / Kwantung Leased Territory); `a Japanese rōnin` (浪人 / 大陸浪人
  continental adventurers); `give up his life for righteousness` (Mencius 6A.10 舍生取义,
  ctext.org — allusion, companion to the foreword's 成仁 note).
  NOT re-noted (forward-noted or already covered): Yan-Feng revolt of 1930 / Central Plains
  War (noted at ch09); Marco Polo Bridge Incident (ch01 War-of-Resistance note names it;
  full note at ch13); Du Fu "campaign not yet won / dead before the campaign was won" line
  (noted at ch29); courtesy-name further instances (ch15, ch17); Dai Li, Legation Quarter
  (extraterritoriality already there), Ji Hongchang, Feng Yuxiang, Sun Chuanfang, Shi
  Jianqiao, bushidō, Shi Yousan, Yin Rugeng, Wang Kemin, Chahar, Beiping Station, etc.
  (all among the 20 pre-F0 notes). Declined as padding: Mount Tai (retreat, not the
  泰山鸿毛 allusion), Fang Zhenwu, "Blind Wang" (in the Wang Kemin note).

Running total: ch01 **379**, ch02 **386** (qa_epub PASS each; epubcheck 5.1.0
0/0/0/0 at ch01, ch02). Per-chapter policy: qa_epub every chapter; epubcheck at
~5-chapter checkpoints and the finale (note-only additions, so check_apparatus +
qa_epub carry the per-chapter risk).

- **ch03 (Introduction: Disgrace at Hanoi) — DONE.** Notes 9 -> 11 (+2).
  New: `Rear a tiger and you leave yourself a calamity` (养虎遗患, Sima Qian,
  *Records of the Grand Historian* / Xiang Yu annals — Zhang Liang & Chen Ping
  to Liu Bang; allusion, source Baidu Baike / Zdic; verdict corroborated);
  `My Final Frame of Mind` (汪精卫《最后之心情》 deathbed essay — authenticity
  DISPUTED: surfaced 1964, provenance/handwriting doubts, Chen Bijun denied a
  will existed; verdict uncorroborated/contested, text left faithful per rule 5;
  sources: 民国网, 网易/163 feature on the 遗嘱 controversy).
  NOT re-noted / already covered by the 9 pre-F0 notes: Wang Jingwei, Hanoi /
  Tonkin / French Indochina, the yandian peace telegram, shuanghuang "two-man
  act", Chongqing, Chen Bijun, the Nanjing puppet government, the eighteen-man
  action team. Declined as padding: "Let Me Give One Example" (Wang's essay —
  prose characterizes it), 穿房越脊/飞檐走壁 (martial-skill phrase, transparent).
  Total after ch03: **388**.

- **ch04 (Introduction: Renown Won in a Hundred Battles + the essay on secret
  service work) — DONE.** Notes 24 -> 26 (+2). Already the densest intro; added
  only genuine gaps. New: `cooking the hound once the hare is caught` (兔死狗烹,
  Sima Qian, *Records of the Grand Historian* / 越王勾践世家, Fan Li's letter;
  allusion, source Baidu Baike; corroborated); `air-dropping our working comrades
  one by one into the mainland` (the early-1950s US/CIA covert airdrops of
  Nationalist agents from Taiwan under Western Enterprises Inc.; Downey–Fecteau
  1952 Manchuria shoot-down; kind-4 author-as-witness + reference; sources:
  CIA.gov "Extraordinary Fidelity," globalsecurity.org/formosa, FRUS 1952-54
  v14 — NOT the Grokipedia hit, excluded per rule 5; corroborated).
  NOT re-noted (already covered): Three Tycoons / Green Gang (in Zhang Xiaolin
  note); Nie Rongzhen (in Lin Biao note); Mao Renfeng + Bureau of Confidential
  Investigation/保密局 (in Zheng Jiemin note); Juntong, Kempeitai, Tokkō, Ume
  Kikan, Ōtsuka, Li Shiqun, Special Operations HQ, Fu Xiao'an, Zhang Xiaolin,
  Zeng Zhongming, striking-the-wrong-carriage, Mencius 富贵不能淫 ("riches and
  honor cannot corrupt"), Zhongnan shortcut, unequal treaties, International
  Settlement, Gang of Four, Liu Shaoqi, Lin Biao, Mao Zedong, Kaohsiung 1979.
  Declined as padding: 借刀杀人 (transparent, inside a rhetorical list), Tao Zhu
  (list member), Xin Shen Bao / Zhonghua Ribao (newspaper titles), Gestapo/CIA
  (Western readers know them). Total after ch04: **390**.

- **ch05 (Prefatory Note, Part One) — DONE.** Notes 8 -> 9 (+1). Already
  thoroughly noted; added the one real gap: `the Military Affairs Commission of
  the National Government` (军事委员会, Chiang Kai-shek's supreme military organ,
  the wartime command center of the Nationalist state; recurs in ~15 chapters,
  previously only named in passing inside other notes; wound up 1946 → Ministry
  of National Defense, consistent with the book's own later references). Standard
  institutional fact; verdict corroborated.
  NOT re-noted (covered by the 8 pre-F0 notes): September 18th / Mukden Incident,
  January 28th / Shanghai Incident, Whampoa, Three Principles of the People,
  Lixingshe (Blue Shirts already in its note), Special Services Department,
  Bureau of Investigation and Statistics, Revolutionary Soldiers' Comrades
  Association; courtesy-name convention (noted ch02). Declined as padding:
  "green striplings," "thorns and brambles" (transparent). Total after ch05:
  **391**. [epubcheck 0/0/0/0 checkpoint]

- **ch06 (Part One §1, A Heavy Charge — the Zhang Jingyao assassination; R1
  frozen exemplar) — DONE.** Notes 24 -> 36 (+12). Long (655-line),
  reference-dense narrative. New (all first-appearance, standard historical
  facts unless noted; verdicts corroborated): `the fight against the bandits`
  (匪/共匪 = the Communists — key recurring euphemism, unlocks all later
  "bandit-suppression"); `after the move to Taiwan` (1949 Nationalist retreat,
  the book's now/then frame; "the late President" = Chiang, d. 1975); `at
  Nanjing and Mount Lu` (庐山 Lushan, Chiang's summer HQ); `Fuyou Street near
  Zhongnanhai` (中南海); `also a fellow provincial from Sichuan` (同乡 native-place
  ties, recurring social bond); `ranked with Li Dazhao and Chen Duxiu` (CCP
  co-founders, 1921); `In the party purge of 1927` (清党 / White Terror, Apr
  1927 KMT-CCP split); `announced his retirement by open telegram` (通电 circular
  telegram, Republican practice); `startle all with its first cry` (一鸣惊人,
  Han Feizi 喻老 / Shiji 滑稽列传 — verified ctext/Sohu/BJ Daily); `was struggled
  to death by the Chinese Communists` (斗争/批斗 struggle session, CR); `Miss Zhu
  the Ninth` (排行 birth-rank naming); `into the Northeast...to organize a
  Volunteer Army` (义勇军; Gen. Li Du 李杜 1880-1956, Jilin Self-Defense Army —
  verified zh.wikipedia/People's Daily/Baidu; corroborated).
  NOT re-noted (covered earlier or by ch06's own 24): War of Resistance (ch01);
  Whampoa/Three Principles/Sept18/Jan28/Lixingshe/Special Services Dept/Bureau-
  Juntong (ch04-05); Feng Yuxiang/Northwest Army/Legation Quarter/courtesy-name/
  Beiping/Dai Li/Zhang Jingyao/Zheng Jiemin/Chahar (ch02); thread-bound books
  (ch01); He Yingqin/Fenghua (noted later at ch09/ch32 — first-appearance
  imperfection left as-is, not duplicated); the prescribed Neo-Confucian works
  (Wang Yangming/Lu Xiangshan/Zeng Guofan/Qi Jiguang — in ch06 "prescribed
  books" note); Green/Hong Gang (in ch06 Sandianhui note); Zhang Zuolin (in ch06
  Huanggutun note); Xi'an Incident/Zhang Xueliang (ch06). Declined as padding:
  Zhang Zhizhong, "New Kuomintang," Fuxingshe/Renaissance Society (Lixingshe
  layer, covered), Youth Corps, Sun Yat-sen Mausoleum, Luoyang move, Beihai/
  Zhongshan Park, jiao unit, Dong'an/Dangui bookstalls, Nanjing standalone.
  Total after ch06: **403**.

- **ch07 (Part One §2, A Startling Debut — courtesan-quarter cover + the
  killing) — DONE.** Notes 11 -> 21 (+10). Texture-rich; existing notes already
  covered the pleasure-quarter (Eight Great Hutongs / pure-singing houses /
  Pingkangli / beating-the-tea-circle) and the Cai E–Xiao Fengxian and Shi
  Jianqiao stories, so I added only NON-duplicative items. New: `Kwantung Army`
  (関東軍, IJA Manchuria garrison — previously only named inside other notes);
  `Northern Expedition of the National Revolutionary Army` (1926–28, Nationalist
  reunification); `rivers-and-lakes` (江湖 jianghu); `Heaven's Net Is Wide`
  (天网恢恢, Dao De Jing ch.73); `bamboo already formed in his breast` (胸有成竹,
  Su Shi on Wen Tong); `a mute eating goldthread` (哑巴吃黄连, goldthread=bitter);
  `never laid down the butcher's knife` (放下屠刀立地成佛, Buddhist); `memorial
  archway` (牌楼 pailou, recurring); `a round-arm bow` (作揖/拱手 salute,
  recurring); `redeemed her from the register` (从良 courtesan buy-out). All
  standard cultural/historical facts; verdicts corroborated.
  NOT re-noted (covered): Xiao Fengxian (in Cai E note), Pingkangli/清吟小班/
  pure-singing (in Eight Great Hutongs note), Shisanmei/He Yufeng & Shi Congbin
  (in the novel + Shi Jianqiao notes), Beiping, Legation Quarter, Grand Hôtel des
  Wagons-Lits (ch06), Sun Chuanfang/Shi Jianqiao/Ji Hongchang/Northwest Army/
  Chahar/courtesy-name (ch02), Itagaki/Zhang Zuolin/Zhongnanhai (ch06), He
  Yingqin (ch09), Juntong (ch04), Rehe/second Manchukuo/Duan Qirui/Song Zheyuan/
  Boxer Protocol/Zhang Zongchang (ch07 pre-F0). Declined as padding: Water Gate,
  Qianmen, spirit-wall, snuff bottles, bathhouse, Tan-family cuisine, Hôtel de
  Pékin, German Hospital, "single spear and lone horse," "beating the grass to
  startle the snake" (English conveys it), flower-name/procuress-mother/mounting-
  the-tray (district economy already glossed). Total after ch07: **413**.

- **ch08 (Part One §3, Tangled Roots — the Ji Hongchang / Liu Shaorang case) —
  DONE.** Notes 13 -> 22 (+9). New (all first-appearance; standard cultural/
  historical commonplaces, verdicts corroborated): `the eighth year before the
  Republic` (民国/民前 year-reckoning, unlocks quoted dates — Republic Year 1 =
  1912); `sixty-odd li` (里 ≈ ½ km, recurring measure); `a great gated mansion of
  four courtyards` (四合院 siheyuan); `White Russians` (post-1917 émigrés in North
  China); `the cart ahead is a warning to the cart behind` (前车之鉴); `the woe of
  the pond-fish` (城门失火殃及池鱼); `every bush and tree a soldier` (草木皆兵, Fei
  River 383); `Tianjin Wei` (天津卫, Ming garrison origin of the city's name); `a
  man should make himself strong` (自强不息, Book of Changes 乾卦象传).
  NOT re-noted / covered: Mauser "box cannon" (in the "German-made" note),
  generation-ranks + opening-the-incense-hall (in the Green Gang note), Beiping,
  Zhang Jingyao, Grand Hôtel (ch06), Lixingshe/Whampoa (ch05), Feng Yuxiang/
  Northwest Army/Chahar/Rehe/courtesy-name (ch02), circular telegram/bandits/
  Taiwan (ch06), Northern Expedition/Kwantung Army (ch07), He Yingqin (ch09),
  Chongqing (ch03), Kempeitai (ch04), Li Dazhao (ch06), Lin Biao/Gang-of-Four/
  Jiang Qing (ch04/ch08 pre-F0), Wu Peifu (noted ch24), vajra/金刚 (ch12 Arhats),
  spirit-tablet (near-dup of ch11 ancestral-hall note). Declined as padding:
  regular-script calligraphy, Ming Tombs, cornbread/wowotou, Guominjun (=Northwest
  Army), Zhili clique (Beiyang covered), greenwood (=jianghu, ch07), "cash"/wen,
  Nanchang HQ, Tada Hayao/Tashiro (one-off garrison commanders), "For whom does
  one toil" (uncertain Luo Yin attribution — not guessed). Total after ch08:
  **422**.

<!-- F0_LEDGER_APPEND -->


