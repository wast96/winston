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
