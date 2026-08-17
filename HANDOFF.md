# HANDOFF — Zhou Enlai: Commander of the Hidden Front

Fresh-session handoff. The paste-ready kickoff is first; everything below it is
the state a new session needs. Batches 1-11 are COMPLETE (ch00-ch20). Next is
B12 = ch21 + ch22.

## Message to paste into the next chat

```
Zhou Enlai B12

Read CLAUDE.md, then HANDOFF.md, then STYLE.md, then book.json. Do Batch 12 =
ch21 (穷凶极恶的捕杀(上) / A Vicious Manhunt, Part 1, PDF 429-457, printed 385-413;
two sections ch21s01-02: 派特务追捕陈赓 / 魔手伸进王根英的娘家) AND ch22 (穷凶极恶的
捕杀(下) / A Vicious Manhunt, Part 2, PDF 458-484, printed 414-440; two sections
ch22s01-02: 秘密绑架丁玲 / 参与暗杀杨杏佛), end to end per the CLAUDE.md pipeline.
Work on branch claude/zhou-enlai; expect a stray per-task branch and consolidate
onto it (CLAUDE.md rule 2 — checkout claude/zhou-enlai, reset --hard to origin,
do the work, delete the stray local+remote).

BEFORE translating, read the final two paragraphs of ch20 in out/ch20_reading.md
(Li Qiang's 1981 account of Bao Junfu, the "veteran of four dynasties") so the
voice carries over. ch21/ch22 continue the aftermath of Gu Shunzhang's April 1931
defection in the same DRAMATIC espionage-thriller register: the Kuomintang's
"vicious manhunt" for the Special Section's people — agents sent after Chen Geng
(陈赓, arrested 1933, then freed through Song Qingling's intervention), the claw
reaching into the family of his wife Wang Genying (王根英), the secret abduction
of the writer Ding Ling (丁玲) with Pan Zinian, and the Blue-Shirt/Juntong
assassination of Yang Xingfo (杨杏佛/杨铨) of the China League for Civil Rights.
Keep the pace; short confident statements. ch01 is the FROZEN reference; run
check_register.py --ref out/ch01_reading.md on every unit.

Pipeline notes specific to THIS book (all proven in B01-B11, do not rediscover):
- Body offset is a CONSTANT 44: printed = PDF - 44. Folio-verify each opener by
  eye anyway. ch21 opens PDF 429 = printed 385; ch22 opens PDF 458 = printed 414.
- OCR: ocr_crop.py FIRST LAST --left 0.11 --right 0.90 --top 0.135 --bottom 0.95
  --lang chi_sim --psm 6 --running-head "隐蔽战线统帅周恩来". Verify pgrep -c
  tesseract is 0 after. ocr_dual.py FIRST LAST is SLOW (~3 reads/page) — run it in
  the BACKGROUND. Back up data/txt for the batch pages before the FIRST strip
  (mkdir data/txt_backup_b12; the b11 rebuild driver expects its own backup dir).
- ASSEMBLY IS THE HARD PART and mutates per batch. USE THE B11 MODEL
  (scripts/recovery/b11_*.py are the newest; b11_rebuild.sh is the deterministic
  strip→assemble→surgery→apply_fixes→pagemap driver — copy it to b12 and edit the
  page range, backup dir, and unit ids/ranges):
  (1) b1X_strip_furniture.py: normalize garbled section/chapter headings to the
  EXACT book.json titles (pull by id; per-target guard len(good)+5; tokens that
  AVOID the garbled char). ch21/ch22 titles have PARENS (上)/(下) — byte-exact.
  If a chapter title prints on TWO OCR lines, special-case a merge (see b11's
  merge_ch19_title). Truncate each author-footnote block. THE KEY LESSON, hammered
  again in B11: the surgery boundary-snap needs a BREAK char (。！？…：) right
  before a paragraph start; grep the assembled zh for OCR-mangled sentence-ends at
  every paragraph SEAM and RESTORE them in the strip (verified on the scan).
  B11's recurring seam mangles: 。 read as 、 / a dash / a comma / dropped; a
  closing ①/"。 read as a DIGIT (9) or a glyph (中/必). Match RESTORE anchors
  across the OCR newline where the seam spans two lines ("施涡等\n4人，").
  (2) Add data/structure.json rows for the chapters + all sections BEFORE assemble
  (pull exact title bytes from book.json; parens/quotes must be byte-exact).
  (3) indents.py FIRST LAST (data/indent is TRACKED). NOTE: indent geometry is
  UNRELIABLE on these scans, so DO NOT trust assemble's auto-segmentation — it
  UNDER-segments (welds paragraphs). Determine paragraph boundaries by READING the
  page images (the real 2-char indents) and encode them as surgery markers.
  BLOCK QUOTES (indented memoir/newspaper extracts) are set off with extra leading;
  the OCR may render them contiguous OR with a blank line between EVERY line —
  read the image, don't trust the blanks. INLINE quotes (dialogue) stay in the
  running paragraph WITH quote marks; DISPLAYED block quotes render as PLAIN
  paragraphs, no outer quotes (Zhang Guotao memoir & the Shen Bao clips in B11).
  (4) b1X_surgery.py --apply: per-SECTION blob split at paragraph-START markers
  (markers[i] starts piece i+1; N paragraphs need N-1 markers; markers are RAW-OCR
  substrings, apply_fixes runs AFTER). DRY-RUN first (verifies each marker occurs
  exactly once, in order). After --apply, AUDIT that every ZH paragraph ends in
  sentence-final punct (colon/semicolon/?/! are legit for intros, list items,
  questions; a stray dash/comma/digit/glyph at an end means a snap misfire → add a
  RESTORE) AND that qc_entities/check_content pass (a split/merge can keep the
  count right while SHIFTING content — happened THREE times in B11; qc_entities
  catching a name in the wrong paragraph is the tell).
  (5) apply_fixes.py <id> AFTER surgery (clean-regen via the rebuild driver before
  every apply_fixes; surgery + apply_fixes are NOT idempotent).
  (6) b1X_pagemap.py regenerates data/pagemap/<unit>.json (edit the build() calls).
- Crop-verify every name/number/alias/date BEFORE writing; record fixes in
  data/ocr_fixes.json via addfixes-style script (Write tool, not heredoc).
  verify_names.py --pdf source.pdf --page N --auto shows dual-OCR DISAGREEMENTS
  (random errors); the SYSTEMATIC mangles both engines agree on you catch by
  knowing the correct historical names (build the fix list from a variant survey:
  grep the assembled zh for 张国. / .代英 patterns). check_numbers catches phantom
  numerals ($=5, ①=9, name char 千/万, weekday/place numerals) and dropped digits;
  fix real garbles in the ZH, carry real values in the English, noise ONLY genuine
  non-quantities (idiom/place/relative-time numerals: add to data/noise.txt,
  longest-first, with a comment line). check_numbers maps English number WORDS
  (sixth→6, second→2) so "the Sixth Central Committee" satisfies 六届.
- Checks: verify_unit reads UNIT IDS (no --noise). qc_entities reads the BILINGUAL
  PATH (out/<id>_bilingual.md); glossary rows need BOTH "en" AND "pinyin"; fix a
  miss by NAMING (or matching the SHELF form — 中统 = "Zhongtong" NOT "CBIS";
  国民党 = "Kuomintang"; 淞沪警备司令部 = "Songhu Garrison Command"). check_align
  reads a unit id. check_content --config data/check_config.json (ADD ch21, ch22 to
  BOTH docs and sources; it wants each glossary EN form present in the paired
  paragraph — and BEWARE false matches: a journal like 《中国青年》 collides with the
  phrase 中国青年 "Chinese youth", so don't add a works row that greps as a common
  phrase). check_structure --pairs SRC TGT. check_register --ref out/ch01_reading.md.
- Glossary: add rows DIRECTLY nested into people/organizations/places/works/terms
  (NOT via apparatus_merge, which drops them at top level where qc_entities can't
  reach); give every row "en" + "pinyin" + "status". REUSE decided renderings: grep
  glossary.json FIRST — most principals are already on the shelf (陈赓 Chen Geng,
  顾顺章, 周恩来, 丁玲 Ding Ling, 杨杏佛/杨铨, 宋庆龄, 王根英 all likely present).
  Consult authority.json for shelf agreement.
- Footnotes at reader-model density with fact-check verdicts IN the note; never
  source LLM content (WebSearch Wikipedia/Executed Today/academic; NEVER
  Grokipedia; block grokipedia.com). Author footnotes reproduced as "Author's
  note." at the ① anchor. Note at FIRST appearance book-wide (grep notes.json and
  earlier reading files first; keep a "NOT re-noted" list in PROGRESS). Chen Geng's
  1933 arrest + Song Qingling's rescue, Ding Ling's abduction, and the Yang Xingfo
  assassination are STRONG corroboration targets. Note anchors must be verbatim
  ASCII substrings of the reading .md (match your exact quote style — B11 used
  straight ASCII ' and ", and used SINGLE quotes for a quote-within-a-quote; avoid
  em-dashes in anchors); note BODIES use numeric char refs only (&#8212; &#8211;
  &#160; &#8220; &#8221; &#8217;). Figure list was EMPTY for ch19/ch20 (narrative
  chapters) — ch21/ch22 may carry portrait plates (Chen Geng, Ding Ling, Yang
  Xingfo): eyeball every page, run find_figures, check char-counts. Merge apparatus
  via apparatus_merge.py (a plain JSON file, Write tool not heredoc);
  check_apparatus.py must be clean. Cite the book's PRINTED FOLIO in notes.
- Build the cumulative EPUB, qa_epub green, epubcheck (/tmp/epubcheck-5.1.0).
- Update PROGRESS.md and HANDOFF.md; commit and push to claude/zhou-enlai.

Deliver in THIS chat: the built EPUB attached, AND the next kickoff pasted
verbatim in a fenced code block. Both, every batch.
```

## Status: what is DONE

- **Survey + B01 (ch00 Preface + ch01):** complete, voice gate approved; ch01 is
  the frozen register reference.
- **B02 (ch02+ch03)** through **B10 (ch17+ch18):** complete.
- **B11 (ch19 Averting a Catastrophe — Gu Shunzhang's Defection + ch20 Betrayal
  to the Last Scrap):** complete. ch19 = 42 body paras, 3 sections, 9 notes, 0
  figures: the January 1931 Fourth Plenum and Wang Ming's rise, Gu Shunzhang's
  escort of Zhang Guotao to the E-Yu-Wan Soviet on the Special Section's timber
  boat (Zhang Guotao's own memoir quoted at length), Gu's arrest in Hankou (24
  Apr 1931) and instant defection, Cai Mengjian's account of the surrender and
  the audience with Chiang, and Qian Zhuangfei's warning telegram that let Zhou
  Enlai evacuate the whole apparatus in a day. ch20 = 64 body paras, 4 sections,
  12 notes, 0 figures: the roll-call of Gu's victims — Yun Daiying (executed
  Nanjing 29 Apr 1931), Cai Hesen (betrayed at the HK seamen's meeting, executed
  Guangzhou, aged 36), Xiang Zhongfa (the only CCP general secretary to defect —
  arrested 22 June, shot 24 June 1931), and the double agent Bao Junfu (Yang
  Dengying), whom the Party protected to the end. All checks green; details in
  PROGRESS.md B11.
- **EPUB:** out/zhou-enlai.epub = 21 of 28 chapters (ch00-ch20), 280 notes, 356
  pagebreaks; qa_epub PASS, epubcheck 0/0/0.

## Tooling in place / do not revert

- data/ocr_fixes.json: crop-verified readings for ch00-ch20; replay with
  apply_fixes.py on any fresh regen. B11 added ch19 (50) + ch20 (71).
- scripts/recovery/ (tracked): b02_* through **b11_*** strip/surgery/pagemap
  scripts + README, plus b10_rebuild.sh and **b11_rebuild.sh** (the deterministic
  drivers). The b11_* set is the CURRENT model. Do not delete.
- ocr_crop.py patches, check_content.py '_'-prefix skip: keep (from B01).
- data/noise.txt: keep extending, never prune. B11 added the idiom/place/weekday/
  relative-time numerals (千秋, 半百, 三刻, 胡说八道, 六安, 七里坪, 星期六, 第二天,
  十万火急).
- data/check_config.json: docs+sources for ch00-ch20; ADD ch21, ch22 next batch.
- data/pagemap/ch19.json, ch20.json: regenerated post-surgery (b11_pagemap.py).
- data/txt_backup_b11/: raw OCR for pages 389-428 (the rebuild driver's source).
- Assembly: indents.py IS run but its geometry is UNRELIABLE; paragraph boundaries
  come from READING the page images. The fix is RE-SEGMENTATION (b11_surgery.py)
  with markers built by eye.
- KNOWN HAZARD: apply_fixes.py and surgery are NOT idempotent. Always clean-regen
  (rebuild driver) before apply_fixes; keep the raw data/txt backup for the batch.
- KNOWN HAZARD: qc_entities.py KeyErrors if a glossary row lacks "pinyin" — every
  row you add needs "en" + "pinyin". It reads the BILINGUAL path, not a unit id.
- KNOWN HAZARD: the surgery snap needs a BREAK char at each seam; OCR-mangled
  ！/。/comma/dash/dropped-。/footnote-digit at a seam must be RESTORE'd in the
  strip. A split/merge can keep the parity count right while SHIFTING content —
  qc_entities/check_numbers (not parity) catch it.
- KNOWN HAZARD: a figure `before` anchor longer than ~80 chars fails the build;
  a note anchor with an em-dash won't match the ASCII reading text.

## Renderings settled (glossary.json is the ledger)

- Held terms carried from earlier batches: 中央特科 Central Special Section, 红队
  Red Squad, 淞沪警备司令部 Songhu Garrison Command, 巡捕房 concession police, 租界
  the Concessions, 白色恐怖 White Terror, 军统 Juntong, **中统 Zhongtong** (NOT
  "CBIS"), 国民党 Kuomintang, 东方大学 "Communist University of the Toilers of the
  East", 宋子文 "T.V. Soong".
- B11 people (58 new glossary rows): the E-Yu-Wan cast (沈泽民/张琴秋/夏曦/曾洪易/
  陈昌浩), the enemy officials (蔡孟坚/何成濬/杨庆山/张冲/顾建中/熊式辉/孟真/张国栋),
  the Cai Hesen circle (向警予/葛健豪/秋瑾/蔡畅/蔡庆熙/李一纯/罗学瓒/蔡元培/杨昌济/
  曾国藩/邓发/陈济棠/施滉), the Xiang Zhongfa affair (杨秀贞[existing]/陈琮英/黄玠然/
  布哈林/叶荣生/曹炳生/鲍文蔚/吴醒亚/吴汉祺), and the rescue cast (朱月倩/霍步青/钱潮/
  欧阳大汉/谢云巢/叶耀明/王震南/罗瑞卿/周佛海). See PROGRESS B11 for the full list.
- Feed decided renderings into authority.json at book's end (out/term_ledger.md).

## Voice sheets (carry-forward)

- **Mu Xin (author):** confident narrative-history voice, open partisan edge;
  heroes are heroes, 叛徒 traitors, the verdict goes in the note. His potted
  biographies (Yun Daiying, Cai Hesen in B11) are the highest-risk zone for
  stiltedness — break them into short confident statements, no dash-glosses. B11
  em-dash rate came in at 3.9/3.3 per 1k (vs the ch01 reference's 6.0); stay at or
  under.
- **Zhou Enlai:** measured, analytic, unshowy; decisive in a crisis (the one-day
  evacuation in ch19). **Chen Geng** (the B12 lead, hunted): quick, cool, the
  operational hand. **Gu Shunzhang** (the B11 villain, still betraying in the
  background of B12): the vain traitor — render his self-serving turn cold, let
  the facts damn him. **Yun Daiying / Cai Hesen / Xiang Zhongfa** (the B11
  martyrs): render their last words at full force (STYLE's heat doctrine — a
  martyr's defiance is hot in the source, hot in English).
- **Reproduced material** (memoir block quotes, newspaper clips, letters, a
  classical poem): DISPLAYED blocks render as PLAIN paragraphs, no outer quotes;
  INLINE dialogue keeps its quote marks; an attribution intro ending in a colon is
  its OWN paragraph; a newspaper headline is its own paragraph; verse takes the
  {p} marker. Author source-citations reproduced as "Author's note." at the ①
  anchor (only for QUOTED passages, not bare narrative citations — the B10/B11
  practice).

## Where the story stands

The Party's clandestine arms are all drawn (intelligence ch04-08; Action/Red
Squad ch09-12; the rescue and political turn ch13-14; political penetration
ch15-16; radio and communications ch17-18). B11 (ch19-20) told the central
catastrophe: Gu Shunzhang's April 1931 defection and the wave of betrayals
(Yun Daiying, Cai Hesen, Xiang Zhongfa, the attempt on Bao Junfu). B12 (ch21-22)
turns to the manhunt that followed: the pursuit and 1933 arrest of Chen Geng and
his rescue through Song Qingling, the raid on Wang Genying's family, the
abduction of Ding Ling, and the assassination of Yang Xingfo.

## Exact next-batch scope

- **B12** = ch21 (PDF 429-457, printed 385-413, ch21s01-02) + ch22 (PDF 458-484,
  printed 414-440, ch22s01-02). Then B13 = ch23 (opens PDF 485, six sections) +
  ch24. (out/SURVEY.md's batch numbering runs one behind, since B05 combined
  ch07+ch08.)

## Open traps / environment state

- Body offset constant 44; folio-verify each opener.
- ASSEMBLY: indent geometry unreliable; read paragraph boundaries off the images.
  assemble UNDER-segments; full surgery re-segmentation. OCR-mangled sentence-ends
  at paragraph seams defeat the snap; RESTORE them in the strip (across the OCR
  newline where needed). After --apply, audit paragraph endings AND run
  qc_entities/check_content to catch content shifts that parity misses.
- Surgery + apply_fixes are NOT idempotent (use the rebuild driver); DRY-RUN
  surgery before --apply.
- data/indent is TRACKED — git checkout it if you rm -rf'd it before re-running.
- qc_entities needs "pinyin" on every glossary row and reads the bilingual PATH;
  check_content wants the SHELF's glossary EN form in the paired paragraph (fix a
  flag by NAMING or matching the shelf form; beware works-row false matches).
- verify_unit takes UNIT IDS (no --noise); qc_entities/check_align take paths/ids.
- OMP_THREAD_LIMIT=1 for tesseract; kill the process GROUP; pgrep -c tesseract
  must read 0 after a run. ocr_dual is slow — background it.
- epubcheck at /tmp/epubcheck-5.1.0 (re-fetch via setup.sh in a fresh container).
- Pre-existing failing regression test ("hook stands down on template stub");
  template maintenance, does not affect real batches.
