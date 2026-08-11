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
