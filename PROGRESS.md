# PROGRESS — The Golden Roc Dynasty (陆小凤传奇·金鹏王朝, Gu Long)

The running per-batch log. Write it as you go, not at the end. One section per
batch: what was translated (unit ids, chapter/section scope), which checks ran
and what they found, notes added (count and numbering), glossary rows added with
status, figures, and anything flagged for the read-through (uncertain readings,
contradictions with scholarship, choices you were unsure of).

## Setup / Survey (Step 0)

- `./setup.sh`: green (pillow installed, epubcheck present at
  /tmp/epubcheck-5.1.0/epubcheck.jar, checker regression tests green). Nothing
  FAILED.
- Source EPUB: `陆小凤传奇·1·金鹏王朝`, 古龙 (Gu Long), Henan Literature & Art
  Publishing House, 2013 (古龙文集 collected-works line), ISBN 978-7-80765-772-9.
  Simplified characters. The novel was first serialised 1976-77.
- Ingest (out/INGEST.md): 18 spine documents, 3 images, 124,096 source chars.
- **Source's own notes: NONE.** Grep for `\[\d+\]` over every extracted unit
  returns zero matches. No `source_notes.json` stream needed for this book; re-grep
  each batch's source and record "none present" per CLAUDE.md.
- Structure: the source split its single text into 18 mechanical
  `part0000_split_NNN.html` chunks. These DO line up one-to-one with the logical
  units: each content chunk opens with a `<p class="x2" id="toc-anchor">`
  heading. Mapped to 13 logical units — the prologue (楔子) + 12 numbered
  chapters. No merge/split of content chunks was needed; only front matter was
  excluded (see book.json `_source_note`): 2 half-title stubs, the CIP colophon,
  the source TOC, and the titlepage (its cover.jpeg reused as the EPUB cover).
- **The prologue alone has named internal sections** — four vignettes (熊姥姥的糖炒栗子
  / 老实和尚 / 西门吹雪 / 花满楼), modelled as book.json sections and shown in the TOC.
  Chapters 1-12 divide themselves with bare numeric markers (01, 02, ...); these
  are scene breaks, to be recovered as `***` with apply_format_markers.py, not
  TOC sections.
- **Chapter 11 (第六根足趾, "The Sixth Toe") is the long climax at ~31,104 chars**
  — roughly 3x a normal chapter. Sized as its own batch.
- Images: `cover.jpeg` = the cover (reused byte-identical). `00001.jpeg`/`00002.jpeg`
  = decorative publisher endpapers (alt 知识小说环衬), no story content — NOT carried
  into figures.json. The book has no story images of its own.
- Digitization glitches: none audited yet (a per-batch task). Note the source
  uses a full-width space inside its chapter headings (第一章　...), collapsed in
  extraction — cosmetic only.
- Skeleton build: `qa_epub.py` PASS (26 files, 19 documents, all links resolve);
  `epubcheck` 3.3: 0 fatals / 0 errors / 0 warnings / 0 infos. Cover embedded.

## B01 = Prologue (ch01) — voice gate

### Environment / setup

- `./setup.sh`: pillow present, epubcheck present at
  /tmp/epubcheck-5.1.0/epubcheck.jar. **Checker regression tests: 9/10 green;
  1 EXPECTED failure.** The failing case is `hook stands down on template
  stub`. That test restores the current HANDOFF.md and asserts the Stop hook
  stays quiet — but HANDOFF.md now carries a REAL, filled-in kickoff
  ("Lu Xiaofeng 1 B01"), not the template placeholder (which starts with
  "(First line:"). So the hook correctly ENFORCES on a live book, and that one
  test necessarily reports FAIL for any project with a real kickoff. Not a
  defect; the enforcing-path hook tests and all builder/number tests pass, and
  the hook working is exactly what guards our final voice-gate reply.
- `data/src` and `data/src_epub` were absent (gitignored); regenerated with
  `scripts/ingest_epub.py source.epub` (18 spine docs, 3 images, 124,096 src
  chars). book.json left untouched (ingest writes only book.draft.json).
- **Source's own notes: none present.** Re-grep of
  `data/src/06_part0000-split-004.txt` for `\[\d+\]` returns zero matches.

### Digitization glitches (rendered to plain sense; not footnoted)

- **ch01 line 48**: `削尖大匝鞋` — `匝` (zā) is anomalous here; the phrase is a
  bandit's footwear ("削尖" = sharp/pointed-toed). Rendered to plain sense as
  "sharp-toed, oversized shoes." Mechanical glitch, not a reading uncertainty,
  so no footnote per CLAUDE.md.
- No other glitches found in ch01 (no mismatched guillemets, no dittography,
  no fullwidth-Latin-in-years).

### Scope

- ch01 (楔子, Prologue), 6,069 src chars, 4 vignette sections rendered as `###`
  headings and TOC entries: ch01s01 Granny Xiong's Sugar-Roasted Chestnuts /
  ch01s02 The Honest Monk / ch01s03 Ximen Chuixue / ch01s04 Hua Manlou.
- Source line 1 is the repeated running-title stub (陆小凤：金鹏王朝 13-03-07
  副本); line 2 the chapter title 楔 子. Both skipped by make_bilingual
  (skip=2). 217 body lines -> 213 prose paragraphs + 4 section titles.
- No extractor-split paragraphs in ch01 (every content line ends on terminal
  punctuation). No U+200B lines, no doubled headings, no spliced captions.
- **Set-off formatting:** the prologue source HTML encodes NONE of the
  apply_format_markers kinds (no `kt` vignette spans, no Image00005 scene-rule,
  no dateline, no hour-gloss) -- the whole chapter is plain `<div
  class="calibre1">` prose. So apply_format_markers.py was not run for ch01
  ("where the source HTML encodes it"); the four vignette titles are recovered
  as `### ` headings via the bilingual->H3->split path. The prologue has no
  bare-numeric dividers (those begin in ch2).

### Checks (all green)

- `make_bilingual.py ch01 ... 2`: 217 paragraph pairs (parity true by
  construction).
- `verify_unit.py ch01`: numbers checked 213 pairs, **0 unresolved**
  (`--noise data/noise.txt`); anchors **14 ok**.
- `check_align.py ch01`: 213/213, median ratio 3.92 en/han, alignment OK.
- `check_content.py`: 126 name occurrences, all in the paired paragraph;
  content alignment OK.
- `check_structure.py`: parity 213|213 OK; anchors 14 notes, 0 unresolved;
  headings OK; ALL STRUCTURAL CHECKS PASS.
- `qc_entities.py`: entity misses **0** (census: 花满楼 x40, 上官飞燕 x25,
  西门吹雪 x13, 洪涛 x13, 赵刚 x9, 张放 x8, 熊姥姥 x6, 崔一洞 x5, 水蛇帮 x4,
  糖炒栗子 x3, 陆小凤 x3, 活菩萨 x2). Achieved by carrying the name (not a
  pronoun) into each source paragraph that names the character -- faithful,
  since the source repeats the name there.
- `check_apparatus.py`: 0 failures, 0 warnings.
- **Tail verification:** last paragraphs (src 216-217, the "four eyebrows"
  riddle and Shangguan Feiyan's resolve to seek Lu Xiaofeng out) checked
  verbatim against the source before shipping.
- Build: `build_reading_epub.py` -> 1 of 13 chapters, 14 notes, 0 source
  notes. `qa_epub.py`: PASS (27 files, 20 documents, all links resolve; 14
  refs / 14 bodies / 14 backlinks). `epubcheck` 5.1.0: **0 fatals / 0 errors /
  0 warnings / 0 infos**.
- `check_register.py --ref out/ch01_reading.md out/ch01_reading.md`: dialogue
  contractions **25.4/1k**, shall-share 0%, em-dash 0.0/1k, rhythm CV 0.70.
  **ch01 is the FROZEN REGISTER REFERENCE for the whole book** (pending the
  voice-gate approval).

### Footnotes (14; first-appearance discipline)

Aimed at a Western reader with no Chinese background. In document order:
1. escort trade (biaoshi/biaoju) 2. money & weight (cash / catty / tael)
3. sugar-roasted chestnuts 4. mandarin ducks vs the owl on bridal shoes
5. length units (cun / zhang / li) 6. qinggong + the martial-monk / Shaolin
convention 7. living Bodhisattva (the irony) 8. Ximen Chuixue's name-pun +
his sacred-killing ritual 9. jianghu 10. the Nine Provinces + the
character-counting that makes "five words, one life" work 11. Hua Manlou's
name-pun 12. Taisui ("Terror") + Cui Yidong's "One Hole" name-pun 13. guqin
14. "four eyebrows" (the hero's riddle; titles ch1).

**NOT re-noted / deliberately not footnoted:**
- jianghu (noted at L93; NOT re-noted at its 2nd use, L153).
- the Nine Provinces (noted at L93; NOT re-noted at L94).
- four eyebrows (noted at L213; NOT re-noted at L216/L217).
- Water Snake Gang, courtesans (名妓), and the "Little Phoenix" gloss on
  Xiaofeng are glossed inline / self-evident in context -- no note.
- 面壁思过 (rendered "sit facing the wall to reflect on my fault"), 义气
  (folded into the jianghu note as "codes of honour") -- no separate note.
- 江南 (Jiangnan) glossed in the glossary only; a footnote is deferred to a
  chapter where the region carries plot weight (first appearance L155).

### Apparatus added

- **glossary.json**: 21 rows. people (13): Lu Xiaofeng, Ximen Chuixue, Hua
  Manlou (all `principal:true` with cast blurbs), Zhang Fang, Granny Xiong,
  Hong Tao, Zhao Gang, Cui Yidong, Shangguan Feiyan, Xiaohong, Xiaocui,
  Xiaoyu, Xiaoyun. organizations (1): Water Snake Gang. places (2): Jiangnan,
  the Nine Provinces. terms (5): jianghu, sugar-roasted chestnuts,
  lightness-skill (qinggong), guqin, living Bodhisattva. All `status:
  decided` (pinyin without tone marks per the shelf convention this book
  sets). notes.json: 14 entries under ch01.
- No figures (the book has none).

### Decided shelf renderings (this batch sets them)

- Names in Hanyu Pinyin, no tone marks: Lu Xiaofeng, Ximen Chuixue, Hua
  Manlou, Zhang Fang, Hong Tao, Zhao Gang, Cui Yidong, Shangguan Feiyan.
- 熊姥姥 -> **Granny Xiong** (en) / Xiong Laolao (pinyin). Flagged in the
  survey as a first-batch call; "Granny" for 姥姥 reads naturally and the
  section title already used it.
- 江湖 -> **jianghu** (kept romanized, footnoted, glossary term).
- 轻功 -> **lightness-skill** (qinggong).
- 一刀镇九州 -> **"One Blade Quells the Nine Provinces"**; 九州 -> the Nine
  Provinces. 闪电刀 -> the Lightning Blade. 玉连环 -> Jade Linked-Rings.
  花刀太岁 -> the Flower-Blade Terror (太岁 = Taisui). (The one-off epithets
  are in the footnotes, not the glossary.)
- 字 counted as "words" in the tally exchanges (matches English word counts in
  the Ximen scene: 4 / 2 / 2), with note 10 clarifying Chinese counts by
  character so "five words" for the 5-character 一刀镇九州 and 我是个瞎子 (=
  "I am a blind man", 5 words) reads true.

### Tooling touched (see HANDOFF do-not-revert)

- `data/noise.txt`: added `第二天` (idiom "the next day/morning", not the
  ordinal; the plank's 第一块/第二块 stay "first/second piece"). This was the
  ONLY number-check false positive.
- `glossary.json` reshaped to the two-level `section -> {zh: row}` form the
  builder (`render_glossary`) and `qc_entities` require. `apparatus_merge.py`
  adds glossary rows FLAT at the top level, which those two consumers cannot
  render/scan; its notes path is correct and was used as-is. See HANDOFF.
- `scripts/check_content.py`: `name_map` now skips `_`-prefixed / non-dict
  top-level keys (it crashed on the glossary's string-valued `_about`). Matches
  the guard already in `qc_entities` and `render_glossary`. Regression harness
  still 9/10 (only the expected template-stub hook case).

### Voice-gate revision (round 2) — commissioner feedback applied

The commissioner read the opening at the voice gate and flagged the voice.
Core note: rendering Gu Long's one-sentence-per-line source 1:1 made English
that "breaks every sentence onto its own line" until the breaks lose meaning;
the prose was also stilted (uncontracted, repetitive "they had just... they
had just"), and forced character names where a fluent writer uses a pronoun.

Changes made across the WHOLE prologue:
- **Merged-paragraph parity.** Adjacent NARRATION lines are now grouped into
  paragraphs by beat; dialogue turns and deliberate punch-lines ("Blood.";
  "Five words, one life.") stay on their own. 213 source lines -> **153 merged
  paragraphs**. Parity is still 1:1 and verbatim-by-construction, but the unit
  is now a merged paragraph: a small script concatenates each group's source
  lines VERBATIM (no re-typing) into a merged source, which make_bilingual
  pairs against the merged English. data/zh/ch01.txt and out/ch01_reading.md
  hold the merged pairs; all checks run on them.
- **Voice pass.** Contractions in narration as well as dialogue; varied
  constructions; trimmed doublings; foreboding carried by rhythm and irony,
  never by invented detail (rule 4 held — nothing added). Natural pronouns
  within a paragraph, the name re-anchored only at a new beat or as an object.
- Concrete fixes from the note: crisp standalone opening line; "not a pair"
  (not "no pair"); "one of them" (not "someone"); horse-froth simile
  rewritten; "wonderfully light and at ease" doubling cut; the chestnut name
  said once, not twice.

Re-checks after the revision (all green):
- verify_unit: 153 pairs, numbers 0 unresolved, anchors 14 ok.
- check_align 153/153, median ratio 3.78, no strays (the one short atmospheric
  closer was trimmed to clear the ratio gate).
- check_content 114 name occurrences all placed; qc_entities 0 misses (the 4
  pronoun paragraphs the detectors flagged were re-anchored with the name at a
  natural beat/object position — a fluent re-use, not the consecutive
  repetition that was objected to). check_apparatus 0/0; check_structure ALL
  PASS.
- qa_epub PASS (165 paragraphs); epubcheck 0/0/0/0.
- **check_register: contractions 35.8/1k (up from 25.4), shall 0%, em-dash
  0.2/1k, rhythm CV 0.76.** This revised ch01 is the frozen reference (pending
  the re-read at the gate).

Note count unchanged at 14 (anchors "three cun thick" -> "three cun of solid
wood" and "What Ximen Chuixue blows is not snow" -> "...blows from his sword is
not snow" to match the revised prose).

### Voice-gate revision (round 3) — full literary re-render

The commissioner gave concrete model paragraphs at the gate ("try to beat
these") establishing the target register: a fluent, literary, image-forward
translation that reads like a published novel, not a gloss. The WHOLE prologue
was re-rendered to it. Distilled in HANDOFF "Voice / house style".
- 154 paragraphs (the `*Blood*` punch split onto its own line; builder renders
  `*...*` as italic, verified `<i>Blood</i>`).
- Freer, dynamic-equivalence rendering: recast/reorder for natural English;
  minor pleonasm trimmed where the commissioner's models trimmed it (the horse
  simile at the poisoning; the moon-dismissal in line 3). Nothing plot-bearing,
  no name, no number dropped; the strangle-intent kept ("hands reaching for
  her neck"). Small characterising touches in dialogue where they fit the voice
  (Granny Xiong's "dear").
- Escort note anchor "escorted in from far away" -> "escorted the long road
  in". All 14 anchors resolve.
- Re-checks all green: verify_unit 154 pairs / numbers 0 / anchors 14;
  check_align no strays (median 3.87); check_content all placed; qc_entities 0;
  check_apparatus 0/0; check_structure PASS; qa_epub PASS; epubcheck 0/0/0/0.
- **check_register: contractions 38.9/1k, rhythm CV 0.78** (frozen reference).

**OPEN QUESTION for the commissioner (money/units).** One model line rendered
十文钱一斤 as "ten bucks apiece". Kept as "ten cash a catty" for now, because
full domestication would clash with the monk's "four taels of silver" a few
paragraphs on, with li/zhang/cun elsewhere, and with the two units footnotes.
Flagged in chat: keep period units (current) vs. domesticate money book-wide.
Answer decides the treatment for all 12 chapters and the units notes.
