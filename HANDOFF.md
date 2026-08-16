# HANDOFF — Zhou Enlai: Commander of the Hidden Front

Fresh-session handoff. The paste-ready kickoff is first; everything below it is
the state a new session needs. Batches 1-10 are COMPLETE (ch00-ch18). Next is
B11 = ch19 + ch20.

## Message to paste into the next chat

```
Zhou Enlai B11

Read CLAUDE.md, then HANDOFF.md, then STYLE.md, then book.json. Do Batch 11 =
ch19 (扑灭一场特大灾祸——顾顺章叛变前后 / Averting a Catastrophe — The Defection of
Gu Shunzhang, PDF 389-405, printed 345-361; three sections ch19s01-03:
顾顺章护送张国焘去鄂豫皖苏区 / 在汉口被捕叛变 / 一网打尽"中共中央"阴谋彻底破产) AND
ch20 (倾箱倒箧的出卖 / Betrayal to the Last Scrap, PDF 406-428, printed 362-384;
four sections ch20s01-04: 顾顺章出卖了在南京狱中的恽代英 / 顾顺章赴香港捕杀蔡和森 /
出卖、抓捕向忠发 / 还出卖了鲍君甫(杨登瀛)), end to end per the CLAUDE.md pipeline.
Work on branch claude/zhou-enlai; expect a stray per-task branch and consolidate
onto it (CLAUDE.md rule 2 — checkout claude/zhou-enlai, reset --hard to origin,
do the work, delete the stray local+remote).

BEFORE translating, read the final two paragraphs of ch18 in out/ch18_reading.md
(Tu Zuochao's unforgettable 1936 meeting with Zhou Enlai in Xi'an) so the voice
carries over. ch19/ch20 turn from the radio-technical portrait register of
ch17/ch18 back to the book's DRAMATIC espionage-thriller register: Gu Shunzhang
(顾顺章, the Action Section chief, already heavily featured in ch09 and as the
"Master Magician") defects in Hankou in April 1931, and the Party races to avert
the catastrophe (Qian Zhuangfei's warning telegram was covered in ch05); ch20 is
the roll-call of everyone he then betrayed (恽代英 Yun Daiying, 蔡和森 Cai Hesen,
向忠发 Xiang Zhongfa the Party's nominal head, and 鲍君甫/杨登瀛 Yang Dengying the
double agent). Keep the pace; short confident statements; this is where the book
means to grip. ch01 is the FROZEN reference; run check_register.py --ref
out/ch01_reading.md on every unit.

Pipeline notes specific to THIS book (all proven in B01-B10, do not rediscover):
- Body offset is a CONSTANT 44: printed = PDF - 44. Folio-verify each opener by
  eye anyway. ch19 opens PDF 389 = printed 345; ch20 opens PDF 406 = printed 362.
- OCR: ocr_crop.py FIRST LAST --left 0.11 --right 0.90 --top 0.135 --bottom 0.95
  --lang chi_sim --psm 6 --running-head "隐蔽战线统帅周恩来". Verify pgrep -c
  tesseract is 0 after. Back up data/txt for the batch pages before the FIRST strip.
- ASSEMBLY IS THE HARD PART and mutates per batch. USE THE B10 MODEL
  (scripts/recovery/b10_*.py are the newest; they follow b09/b08 and add a
  deterministic rebuild driver, scripts/recovery/b10_rebuild.sh):
  (1) b1X_strip_furniture.py: normalize garbled section/chapter headings to the
  EXACT book.json titles (pull by id; per-target guard len(good)+5; tokens that
  AVOID the garbled char, e.g. ["永不消","红色电波"] when 逝 is mangled). EMPTY every
  figure/facsimile page (photo mid-paragraph; the spanning paragraph rejoins).
  Truncate each author-footnote block (source citations, reproduced as
  "Author's note." at the ① anchor). THE KEY LESSON, hammered again in B10: the
  surgery boundary-snap needs a BREAK char (。！？…：) right before a paragraph
  start; grep the assembled zh for OCR-mangled sentence-ends at every paragraph
  SEAM and RESTORE them in the strip (verified on the scan). In B10 the recurring
  mangles were: 。 read as 、 or a dash - or dropped entirely; a closing ①/"。
  read as a digit (9) or a glyph (必); dropped intro text before a block quote
  (满怀地写道:). Match across the OCR newline where the seam spans two lines
  ("前文已经讲\n过)").
  (2) Add data/structure.json rows for the chapters + all sections BEFORE assemble
  (pull exact title bytes from book.json; fancy-quote/em-dash titles must be
  byte-exact — ch19 title has an em-dash ——, ch20s03 has a 、, ch20s04 has ()).
  (3) indents.py FIRST LAST (data/indent is TRACKED). NOTE: indent geometry is
  UNRELIABLE on these scans (skew flags whole blocks), so DO NOT trust assemble's
  auto-segmentation — determine paragraph boundaries by READING the page images
  (the real 2-char indents) and encode them as surgery markers, the B10 way.
  (4) b1X_surgery.py --apply: per-SECTION blob split at paragraph-START markers
  (markers[i] starts piece i+1; N paragraphs need N-1 markers; markers are RAW-OCR
  substrings, apply_fixes runs AFTER). Note the ch18 chapter-intro paragraph sits
  in its own blob (0 markers) between two headings — expect the same shape if a
  chapter opens with body text before its first section. DRY-RUN first (verifies
  each marker occurs exactly once, in order). Dialogue/quote paragraphs that OPEN
  on a quote: marker a few chars INTO the quote, the snap prepends the opening ".
  BLOCK QUOTES and NEWSPAPER CLIPS: an attribution intro ending in : is its own
  paragraph; a headline is its own paragraph. After --apply, AUDIT that every ZH
  paragraph ends in sentence-final punct (a stray dash/comma/digit at an end means
  a snap misfire → add a RESTORE) and that per-SECTION EN==ZH count AND the
  bilingual aligns (a split/merge can keep the count right while shifting content
  — happened repeatedly in B10; fix EN paragraph breaks to match the ZH, or add a
  RESTORE so the ZH matches the intended source break).
  (5) apply_fixes.py <id> AFTER surgery (clean-regen via b10_rebuild.sh before
  every apply_fixes; the driver replays strip→assemble→surgery→apply_fixes→pagemap
  deterministically from the raw-OCR backup).
  (6) b1X_pagemap.py regenerates data/pagemap/<unit>.json (edit the two build()
  calls to the new unit ids/ranges).
- Crop-verify every name/number/alias/date BEFORE writing; record fixes in
  data/ocr_fixes.json via apply_fixes.py. check_numbers catches phantom numerals
  from glyph garbles ($=5, 万=瓦, 上/工/士=1/10, 《=4, folio numbers leaking into the
  body, footnote ①②③ read as digits) and dropped digits; fix real garbles in the
  ZH, carry real values in the English (figures for 100+ and for anything needing a
  comma; spell out small standalone counts; technical measurements like wattage in
  figures), noise ONLY genuine non-quantities (place/idiom/name numerals: add to
  data/noise.txt, longest-first, with a comment line above each).
- Checks: verify_unit reads UNIT IDS (parity + check_numbers with data/noise.txt +
  anchors) — do NOT pass --noise, it takes only ids. qc_entities reads the BILINGUAL
  PATH (out/<id>_bilingual.md), not the id; glossary rows need BOTH "en" AND
  "pinyin"; fix a miss by NAMING (render 国民党 as Kuomintang, name Shanghai, etc.).
  check_align reads a unit id. check_content --config data/check_config.json (ADD
  ch19, ch20 to BOTH docs and sources; it wants each glossary EN form present in
  the paired paragraph — match the SHELF's decided form, e.g. "T.V. Soong" no space,
  "Communist University of the Toilers of the East"). check_structure --pairs SRC
  TGT. check_register --ref out/ch01_reading.md.
- Glossary: add rows DIRECTLY nested into people/organizations/places/works/terms
  (NOT via apparatus_merge, which drops them at top level where qc_entities can't
  reach); give every row "en" + "pinyin" + "status". Decide the PROSE rendering as
  the glossary `en`, keep the formal expansion in the NOTE. REUSE decided renderings:
  顾顺章 Gu Shunzhang, 周恩来, 陈赓, 杨登瀛/鲍君甫 Yang Dengying, 恽代英 Yun Daiying,
  蔡和森 Cai Hesen, 向忠发 Xiang Zhongfa, 张国焘 Zhang Guotao, 李强, 陈养山 all recur
  (grep glossary.json first). Consult authority.json for shelf agreement.
- Footnotes at reader-model density with fact-check verdicts IN the note; never
  source LLM content (WebSearch Wikipedia/Baidu/academic; NEVER Grokipedia; block
  grokipedia.com). Author footnotes reproduced as "Author's note." at the ① anchor.
  Note at FIRST appearance book-wide (grep notes.json and earlier reading files
  first; keep a "NOT re-noted" list in PROGRESS). Gu Shunzhang's defection is a
  STRONG corroboration target (well-documented 1931 event) — trace to earliest
  source. Note anchors must be verbatim ASCII substrings of the reading .md (match
  your exact quote style — B10 used straight ASCII ' and "); note BODIES use numeric
  char refs only (&#8212; &#8211; &#160; &#8220; &#8221; &#8217;). Figure `alt` must
  NOT contain a double quote; figure `file` is a BARE basename in data/figs/; figure
  `before` anchor must fit in the FIRST ~80 chars of a paragraph (B10 hit this: an
  84-char anchor failed the build — keep anchors short). Merge apparatus via
  apparatus_merge.py (a plain JSON file, Write tool not heredoc); check_apparatus.py
  must be clean.
- Cite the book's PRINTED FOLIO in notes, never the PDF page.
- Build the cumulative EPUB, qa_epub green, epubcheck (/tmp/epubcheck-5.1.0).
- Update PROGRESS.md and HANDOFF.md; commit and push to claude/zhou-enlai.

Deliver in THIS chat: the built EPUB attached, AND the next kickoff pasted
verbatim in a fenced code block. Both, every batch.
```

## Status: what is DONE

- **Survey + B01 (ch00 Preface + ch01):** complete, voice gate approved; ch01 is
  the frozen register reference.
- **B02 (ch02 + ch03)** through **B09 (ch15 + ch16):** complete.
- **B10 (ch17 Communications Chief "Zeng Peihong" — Li Qiang + ch18 The Red
  Airwaves That Never Die):** complete. ch17 = 74 body paras, 5 sections, 11
  notes, 5 figures: Li Qiang's whole career (Changshu scholar-family boy to the
  Party's radio pioneer), building the first transceiver with Cai Shuhou and Tu
  Zuochao, the Hong Kong station, the two training classes and the December 1930
  Sichengli raid, then the sweep into the Soviet-area radio net and the Long
  March. ch18 = 59 body paras, chapter-opener + 4 sections, 15 notes, 2 figures:
  portraits of the radio men (Cai Shuhou and the Comintern/Sorge milieu; Zhang
  Shenchuan the first operator; Mao Qihua the Soviet-trained expert; Tu Zuochao
  the "Carpenter," closing on his 1936 reunion with Zhou Enlai in Xi'an). All
  checks green; details in PROGRESS.md B10.
- **EPUB:** out/zhou-enlai.epub = 19 of 28 chapters (ch00-ch18), 259 notes, 319
  pagebreaks; qa_epub PASS, epubcheck 0/0/0.

## Tooling in place / do not revert

- data/ocr_fixes.json: crop-verified readings for ch00-ch18; replay with
  apply_fixes.py on any fresh regen. B10 added ch17 + ch18.
- scripts/recovery/ (tracked): b02_* through **b10_*** strip/surgery/pagemap
  scripts + README, plus **b10_rebuild.sh** (the deterministic
  strip→assemble→surgery→apply_fixes→pagemap driver). The b10_* set is the CURRENT
  model. Do not delete.
- ocr_crop.py patches, check_content.py '_'-prefix skip: keep (from B01).
- data/noise.txt: keep extending, never prune. B10 added the ch17/ch18 idiom and
  place numerals (see PROGRESS B10 for the list).
- data/check_config.json: docs+sources for ch00-ch18; ADD ch19, ch20 next batch.
- data/pagemap/ch17.json, ch18.json: regenerated post-surgery (b10_pagemap.py).
- data/figs/: 7 new B10 crops (p0334/p0341/p0356/p0358/p0362-f1 for ch17,
  p0382/p0385-f1 for ch18); p0356 was cropped by hand (find_figures misses a
  handwriting facsimile). All tracked.
- Assembly: indents.py IS run but its geometry is UNRELIABLE on these scans;
  paragraph boundaries come from READING the page images. The fix is
  RE-SEGMENTATION (b10_surgery.py) with markers built by eye.
- KNOWN HAZARD: apply_fixes.py and surgery are NOT idempotent. Always clean-regen
  (b10_rebuild.sh) before apply_fixes; keep the raw data/txt backup for the batch.
- KNOWN HAZARD: qc_entities.py KeyErrors if a glossary row lacks "pinyin" — every
  row you add needs "en" + "pinyin". It reads the BILINGUAL path, not a unit id.
- KNOWN HAZARD: the surgery snap needs a BREAK char at each seam; OCR-mangled
  ！/。/《/dash/dropped-。/footnote-digit at a seam must be RESTORE'd in the strip.
- KNOWN HAZARD: a figure `before` anchor longer than ~80 chars fails the build.

## Renderings settled (glossary.json is the ledger)

- Held terms carried from earlier batches (grep glossary.json): 中央特科 Central
  Special Section, 红队 Red Squad, 淞沪警备司令部 Songhu Garrison Command, 巡捕房
  concession police, 租界 the Concessions, 白色恐怖 White Terror, 军统 Juntong,
  同盟会 Tongmenghui, 晋绥 Shanxi-Suiyuan, 西行漫记 Red Star Over China.
- B10 people (glossary, 73 new rows): 曾培鸿 Zeng Peihong (alias of Li Qiang),
  蔡叔厚 Cai Shuhou, 毛齐华 Mao Qihua, 涂作潮 Tu Zuochao, 王诤 Wang Zheng, 伍云甫 Wu
  Yunfu, 吴克坚 Wu Kejian, 张辉瓒 Zhang Huizan, 李明瑞 Li Mingrui, 俞作柏/俞作豫 Yu
  Zuobai/Yu Zuoyu, 黄尚英 Huang Shangying, 李翔梧 Li Xiangwu, 汤恩伯 Tang Enbo, 张学良
  Zhang Xueliang, 夏衍 Xia Yan, 左尔格 Richard Sorge, 赛克特 Seeckt, plus the training
  class, the Comintern-group, and Nanchang-negotiation casts. See PROGRESS B10.
- SHELF forms to hold: 东方大学 "Communist University of the Toilers of the East"
  (used in 7 prior chapters, NOT "Eastern University"); 宋子文 "T.V. Soong" (no
  space, existing row). Match these in prose or check_content flags them.
- Feed decided renderings into authority.json at book's end (out/term_ledger.md).

## Voice sheets (carry-forward)

- **Mu Xin (author):** confident narrative-history voice, open partisan edge;
  heroes are heroes, 叛徒 traitors, the verdict goes in the note. His potted
  biography and exposition is the highest-risk zone for stiltedness — break it
  into short confident statements, no dash-glosses. B10 em-dash rate came in at
  4.1/2.4 per 1k (vs the ch01 reference's 6.0); stay at or under.
- **Zhou Enlai:** measured, analytic, unshowy; warm and terse in the Xi'an reunion
  with Tu Zuochao (ch18). **Chen Geng:** quick, cool, the operational hand.
  **Li Qiang** (the B10 lead): the technical man, precise and unfussy in his own
  recollections. **Gu Shunzhang** (the B11 villain): the vain "Master Magician"
  turned traitor — render his self-serving turn cold, let the facts damn him.
- **Reproduced material** (facsimile LETTERS, calligraphy inscriptions, memoir
  quotes, the Snow/西行漫记 passage, newspaper clips): rendered as PLAIN paragraphs,
  no outer quotes on block quotes; an attribution intro ending in a colon is its
  OWN paragraph; a newspaper headline is its own paragraph. Author source-citations
  reproduced as "Author's note." at the ① anchor.
- **Dialogue and first-person memoir** (heavy in ch17/ch18, and in the ch19/ch20
  interrogation and betrayal scenes): natural and contracted, differentiated by
  speaker; keep the long veteran-memoir quotes as single paragraphs matching the
  source's own paragraphing.

## Where the story stands

The Party's clandestine arms are all drawn (intelligence ch04-08; Action/Red
Squad ch09-12; the rescue and political turn ch13-14; the political-penetration
arc ch15-16; the radio and communications arc ch17-18). B11 (ch19-20) turns to
the book's central catastrophe: Gu Shunzhang's April 1931 defection in Hankou and
the wave of betrayals that followed. Chen Geng, Li Qiang, and the Longtan Three
have already appeared; ch05 told how Qian Zhuangfei's telegram gave the Party the
hours it needed to break the net. ch19-20 tell the defection itself and its cost.

## Exact next-batch scope

- **B11** = ch19 (PDF 389-405, printed 345-361, ch19s01-03) + ch20 (PDF 406-428,
  printed 362-384, ch20s01-04). Then B12 = ch21 (opens PDF 429) + ch22.
  (out/SURVEY.md's batch numbering runs one behind, since B05 combined ch07+ch08.)

## Open traps / environment state

- Body offset constant 44; folio-verify each opener.
- ASSEMBLY: indent geometry unreliable; read paragraph boundaries off the images.
  OCR-mangled sentence-ends at paragraph seams defeat the surgery snap; RESTORE
  them in the strip. EMPTY full-page image/facsimile pages. After --apply, audit
  that every ZH paragraph ends in sentence-final punct AND align the bilingual per
  section (a split/merge can keep the count right while shifting content).
- Surgery + apply_fixes are NOT idempotent (use b10_rebuild.sh); DRY-RUN surgery
  before --apply.
- data/indent is TRACKED — git checkout it if you rm -rf'd it before re-running.
- qc_entities needs "pinyin" on every glossary row and reads the bilingual PATH;
  check_content wants the SHELF's glossary EN form in the paired paragraph (fix a
  flag by NAMING or matching the shelf form).
- Figure `alt` must not contain a double quote; `file` is a bare basename in
  data/figs/; `before` anchor must fit the first ~80 chars. Note anchors verbatim
  ASCII substrings (match your exact quote style); note bodies numeric char refs.
- verify_unit takes UNIT IDS (no --noise); qc_entities/check_align take paths/ids
  as noted above.
- OMP_THREAD_LIMIT=1 for tesseract; kill the process GROUP; pgrep -c tesseract
  must read 0 after a run.
- epubcheck at /tmp/epubcheck-5.1.0 (re-fetch via setup.sh in a fresh container).
- Pre-existing failing regression test ("hook stands down on template stub");
  template maintenance, does not affect real batches.

