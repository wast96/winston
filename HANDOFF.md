# HANDOFF — Zhou Enlai: Commander of the Hidden Front

Fresh-session handoff. The paste-ready kickoff is first; everything below it is
the state a new session needs. Batches 1-12 are COMPLETE (ch00-ch22). Next is
B13 = ch23 + ch24.

## Message to paste into the next chat

```
Zhou Enlai B13

Read CLAUDE.md, then HANDOFF.md, then STYLE.md, then book.json. Do Batch 13 =
ch23 (隐蔽、撤退、转移 / Concealment, Withdrawal, Relocation, PDF 485-526, printed
441-482; SIX sections ch23s01-06: 中央特委会调整和特科改组 / 陈赓、陈养山转移天津 /
李强到莫斯科深造 / “龙潭三杰”去中央苏区立新功 / 刘鼎撤离一波三折 / 周恩来安抵红都瑞金)
AND ch24 (叛徒顾顺章的可耻下场 / The Traitor Gu Shunzhang's Shameful End, PDF
527-552, printed 483-508; FOUR sections ch24s01-04: 人人喊打的过街老鼠 / 变本加厉的
出卖 / 写了一本献媚取宠的书 / 终被徐恩曾处决), end to end per the CLAUDE.md pipeline.
Work on branch claude/zhou-enlai; expect a stray per-task branch and consolidate
onto it (CLAUDE.md rule 2 — checkout claude/zhou-enlai, reset --hard to origin,
do the work, delete the stray local+remote).

BEFORE translating, read the final two paragraphs of ch22 in out/ch22_reading.md
(Shen Zui's account of Guo Decheng's poisoning and the "Guo Decheng Road") so the
voice carries over. ch23 turns from the manhunt to the Party's orderly RETREAT:
the reshuffle of the Special Committee and reorganization of the Special Section,
Chen Geng and Chen Yangshan's move to Tianjin, Li Qiang's study in Moscow, the
"Three Heroes of Longtan" (Qian Zhuangfei / Li Kenong / Hu Di) winning new merit
in the Central Soviet, Liu Ding's troubled withdrawal, and Zhou Enlai's safe
arrival at the red capital, Ruijin (late 1931). ch24 closes the Gu Shunzhang
arc: the hunted traitor, his worsening betrayals, the fawning book he wrote, and
his execution by Xu Enzeng. Register: the same confident narrative-history voice;
ch01 is the FROZEN reference; run check_register.py --ref out/ch01_reading.md on
every unit.

Pipeline notes specific to THIS book (all proven in B01-B12, do not rediscover):
- Body offset is a CONSTANT 44: printed = PDF - 44. Folio-verify each opener by
  eye anyway. ch23 opens PDF 485 = printed 441; ch24 opens PDF 527 = printed 483.
- OCR: ocr_crop.py FIRST LAST --left 0.11 --right 0.90 --top 0.135 --bottom 0.95
  --lang chi_sim --psm 6 --running-head "隐蔽战线统帅周恩来". Verify pgrep -c
  tesseract is 0 after. ocr_dual.py FIRST LAST is SLOW — run it in the BACKGROUND.
  Back up data/txt for the batch pages before the FIRST strip (mkdir
  data/txt_backup_b13).
- ASSEMBLY IS THE HARD PART and mutates per batch. USE THE B12 MODEL
  (scripts/recovery/b12_*.py are the newest; b12_rebuild.sh is the deterministic
  strip→assemble→surgery→addfixes→apply_fixes→pagemap driver — copy it to b13 and
  edit the page range, backup dir, and unit ids/ranges). Key pieces:
  (1) b12_strip_furniture.py: normalize garbled section/chapter headings to the
  EXACT book.json titles (byte-exact, incl. parens/quotes). Section headings often
  sit MID-PAGE (not at the page top) — locate them by grepping the raw OCR, not by
  assuming line 1. TRUNCATE author-footnote blocks (foot-of-page citations); some
  are the substantive 注N bio blocks that you reproduce as "Author's note." REMOVE
  figure-caption blocks that OCR'd INTO the body (REMOVE_UNTIL for a caption at the
  page top, TRUNCATE_AFTER for one at the foot) — B12 had four such plates.
  (2) Add data/structure.json rows for the chapters + all sections BEFORE assemble
  (pull exact title bytes from book.json).
  (3) indents.py FIRST LAST (data/indent is TRACKED). Indent geometry is
  UNRELIABLE; determine paragraph boundaries by READING the page images.
  (4) b12_surgery.py is the ROBUST re-segmenter: it matches CLEAN paragraph-opening
  markers against a NORMALIZED view of the blob (systematic OCR name-mangles
  de-mangled — all SAME-LENGTH — then punctuation stripped, with an index map back
  to raw), and splits the RAW blob at the mapped positions with NO snap. So you
  write markers in clean text and mangled seams DON'T need restoring for
  segmentation. Each marker must be the EXACT paragraph OPENING (not a mid-para
  substring, or the pre-marker text leaks into the previous paragraph — cost us
  two mis-splits in B12 on "1933年3月," date-prefixes) and unique after
  normalization. Extend DEMANGLE with any same-length opening-word mangle a marker
  needs; run the DRY-RUN until every section reports its paragraph count.
  DIALOGUE turns are each their own paragraph (ch21s01 alone was 80). VERSE is ONE
  {p} paragraph with verse-lines joined by " / " (NOT multiple lines — that breaks
  parity). DISPLAYED block quotes (memoir, newspaper, statements) render as PLAIN
  paragraphs, no outer quotes; inline dialogue keeps quote marks.
  (5) b12_addfixes.py builds data/ocr_fixes.json rows (name/number garbles),
  applied AFTER surgery. (6) b12_pagemap.py regenerates data/pagemap.
- Chen Geng 陈赓 is mangled ~15 ways (陈刻/陈庆/陈广/陈记/陈钴/陈废/陈唐 …); a similar
  fan-out hits 蒋介石 (将/葛/藉/攻/萝/薪/莉 介石), 蔡元培, 杨铨 (杨狂 …), 王根英, 丁玲
  (于玲), 鲁迅 (重迅). Build the fix list from a variant survey (Python Counter over
  陈X / X介石 patterns), being careful NOT to fold real names (陈藻英/陈连生/陈月先/
  陈独秀, 沈醉's alias 陈沦). qc_entities needs the CANONICAL hanzi in the ZH, so
  these fixes are REQUIRED, not optional. check_numbers phantoms in B12: ① note-ref
  OCR'd as a trailing digit (9/0/7/1), 《 title-bracket OCR'd as 4, and single-char
  garbles that inject a numeral (六然→凛然[6], 这个三→这个厂[3], 工部六→工部局[6],
  7十→7寸[10], 红十闻→红十字[10], 丁零→丁玲[0], 万决定→乃决定[10000]); arabic+万
  composites (6万/30多万) orphan a bare 万 → noise `[0-9]+万` (data/noise.txt).
- Checks (all must pass): verify_unit UNIT_ID (parity+numbers+anchors, no --noise);
  make_bilingual UNIT_ID then qc_entities out/<id>_bilingual.md (accepts the en's
  FIRST or LAST word, so "concession"/"police"/"Kuomintang" satisfy the multiword
  forms); ADD ch23/ch24 to data/check_config.json (docs+sources) then check_content
  --config data/check_config.json (wants the EXACT glossary en form in the paired
  paragraph — use the SHELF form, e.g. Ta Kung Pao / Shen Bao / Dog-Beating Squad,
  and BEWARE works/terms that grep as phrases: B12 had to delete 同盟会 [in 同盟会员]
  and 时报 [in 当时报纸]); check_align UNIT_ID; check_structure --pairs SRC TGT;
  check_register --ref out/ch01_reading.md.
- Glossary: add rows DIRECTLY nested into people/organizations/places/works (NOT via
  apparatus_merge, which drops them at top level where qc_entities can't reach); give
  every row "en" + "pinyin" + "status". GREP glossary.json FIRST — most principals
  are already on the shelf after B12 (陈赓, 顾顺章, 周恩来, 李强, 陈养山, 钱壮飞, 李克农,
  胡底, 刘鼎, 徐恩曾, 戴笠 all likely present). Consult authority.json for shelf
  agreement (it decided 宋庆龄 = "Song Qingling"; follow the ledger, not "Soong").
- Footnotes at reader-model density with fact-check verdicts IN the note; never
  source LLM content (WebSearch Wikipedia/academic; NEVER Grokipedia; block
  grokipedia.com). Author footnotes reproduced as "Author's note." at the ① anchor
  for QUOTED passages (not bare narrative citations). Note at FIRST appearance
  book-wide (grep notes.json and earlier reading files first; keep a "NOT re-noted"
  list in PROGRESS). ch23 STRONG corroboration targets: the Longtan Three (Qian
  Zhuangfei/Li Kenong/Hu Di), Zhou Enlai's route to Ruijin, Liu Ding. ch24: Gu
  Shunzhang's execution (徐恩曾, ~1935). Note anchors are verbatim ASCII substrings
  of the reading .md (B12 used straight ASCII ' and "); bodies use numeric char
  refs only (&#8212; &#8211; &#160; &#8220; &#8221; &#8217;). Eyeball every page for
  figures (portrait plates likely for Qian Zhuangfei / Li Kenong / Liu Ding / Gu
  Shunzhang), run find_figures, check char-counts; strip any caption that OCR'd into
  the body. Merge apparatus via apparatus_merge.py (plain JSON, Write tool);
  check_apparatus.py must be clean. Cite the book's PRINTED FOLIO in notes.
- Build the cumulative EPUB, qa_epub green, epubcheck (/tmp/epubcheck-5.1.0).
- Update PROGRESS.md and HANDOFF.md; commit and push to claude/zhou-enlai.

Deliver in THIS chat: the built EPUB attached, AND the next kickoff pasted
verbatim in a fenced code block. Both, every batch.
```

## Status: what is DONE

- **Survey + B01 (ch00 Preface + ch01):** complete, voice gate approved; ch01 is
  the frozen register reference.
- **B02 (ch02+ch03)** through **B11 (ch19+ch20):** complete.
- **B12 (ch21 A Vicious Manhunt Part 1 + ch22 A Vicious Manhunt Part 2):**
  complete. ch21 = 104 body paras, 2 sections, 11 notes, 2 figures: Gu Shunzhang's
  Zhongtong action squad hunts the Special Section's people; Chen Geng arrested at
  the Beijing/Lido Theatre 24 Mar 1933, tortured in the concession cells, tried and
  extradited (Song Qingling and the China League for Civil Rights intervene),
  refuses Chiang Kai-shek face to face at Nanchang, and escapes late May 1933; his
  wife Wang Genying seized Dec 1933, three years in the Model Prison / Xiaozhuang
  reformatory (the Noulens hunger strike), freed by Zhou Enlai Aug 1937, killed in
  battle 8 Mar 1939. ch22 = 47 body paras, 2 sections, 10 notes, 2 figures: the
  secret abduction of Ding Ling and Pan Zinian (14 May 1933, Ying Xiuren killed),
  her three years in Nanjing under Xu Enzeng the "Smiling Tiger" and Gu Shunzhang,
  escape to Bao'an 1936, rehabilitation 1984; and the Blue Shirt/Juntong
  assassination of Yang Xingfo (18 Jun 1933), founder-secretary of the China League
  for the Protection of Civil Rights. All checks green; details in PROGRESS.md B12.
- **EPUB:** out/zhou-enlai.epub = 23 of 28 chapters (ch00-ch22), 301 notes, 407
  pagebreaks; qa_epub PASS, epubcheck 0/0/0.

## Tooling in place / do not revert

- data/ocr_fixes.json: crop-verified readings for ch00-ch22; replay with
  apply_fixes.py on any fresh regen. B12 added ch21 (52) + ch22 (42) rows.
- scripts/recovery/ (tracked): b02_* through **b12_*** strip/surgery/pagemap/addfixes
  scripts + README, plus the b1X_rebuild.sh drivers. The **b12_* set is the CURRENT
  model** (robust normalized-match surgery, no snap; a separate b12_markers.py holds
  the marker lists; b12_addfixes.py builds the ocr_fixes rows; b12_glossary.py adds
  nested glossary rows). Do not delete.
- data/noise.txt: keep extending, never prune. B12 added 百花洲, 十六铺, 五短身材,
  红十字, 一九三几, 十字路, and the arabic+万 composite patterns `[0-9]+万` /
  `[0-9]+多万` / `[0-9]+万多`.
- data/check_config.json: docs+sources for ch00-ch22; ADD ch23, ch24 next batch.
- data/pagemap/ch21.json, ch22.json: regenerated post-surgery (b12_pagemap.py).
- data/txt_backup_b12/: raw OCR for pages 429-484 (the rebuild driver's source).
- Assembly: indents.py IS run but geometry is UNRELIABLE; boundaries come from
  READING the page images and are encoded as surgery markers.
- KNOWN HAZARD: apply_fixes.py + surgery are NOT idempotent. Always clean-regen
  (b12_rebuild.sh) before apply_fixes; keep the raw data/txt backup for the batch.
- KNOWN HAZARD: qc_entities.py KeyErrors if a glossary row lacks "pinyin" — every
  row needs "en" + "pinyin". It reads the BILINGUAL path, and accepts the en's
  first OR last word.
- KNOWN HAZARD: check_content wants the EXACT glossary en form; a short glossary key
  can FALSE-MATCH a common phrase (同盟会 in 同盟会员, 时报 in 当时报纸) — delete such
  keys if no chapter uses the entity for real, or the run never goes clean.
- KNOWN HAZARD: VERSE must be one {p} line with " / " between verse-lines, or parity
  breaks. A figure `before` anchor must be in the first ~80 chars of a paragraph.

## Renderings settled (glossary.json is the ledger)

- Held terms: 巡捕房 concession police, 中央特科 Central Special Section, 红队 Red
  Squad, 打狗队 Dog-Beating Squad, 淞沪警备司令部 Songhu Garrison Command, 白色恐怖
  White Terror, 中统 Zhongtong, 军统 Juntong, 复兴社 Renaissance Society (= 蓝衣社
  Blue Shirts), 国民党 Kuomintang, 中国民权保障同盟 China League for the Protection
  of Civil Rights, 反省院 reformatory (fanshengyuan).
- SHELF DECISION: 宋庆龄 = "Song Qingling" (authority.json, huang-mulan), NOT "Soong
  Ching-ling". 大公报 = Ta Kung Pao, 大美晚报 = Da Mei Wan Bao, 申报 = Shen Bao,
  字林西报 = North China Daily News.
- B12 people (85 new glossary rows): 陈赓 Chen Geng, 丁玲 Ding Ling, 杨铨/杨杏佛
  Yang Quan/Yang Xingfo, 王根英 Wang Genying, 邓文仪 Deng Wenyi, 谭国辅 Tan Guofu,
  沈醉 Shen Zui, 戴笠 Dai Li, 潘梓年, 应修人, 胡也频, 帅孟奇, 夏之栩, 钱瑛, 何宝珍,
  熊天荆, 冯雪峰, and the League/press/rescue cast. See PROGRESS B12 and glossary.json.
  REMOVED false-matching keys 同盟会 and 时报.
- Feed decided renderings into authority.json at book's end (out/term_ledger.md).

## Voice sheets (carry-forward)

- **Mu Xin (author):** confident narrative-history voice, open partisan edge;
  heroes are heroes, 叛徒 traitors, the verdict goes in the note. Break potted
  biographies into short confident statements, no dash-glosses. B12 em-dash rate
  came in at 3.4/3.9 per 1k (vs the ch01 reference's 6.0); stay at or under.
- **Chen Geng** (B12 lead; carries into ch23): quick, cool, the operational hand;
  scathing and witty under interrogation (the "So-so" to Chiang). **Zhou Enlai**
  (ch23 lead): measured, analytic, decisive in a crisis. **Gu Shunzhang** (the B11
  villain, the ch24 subject): the vain traitor — render his self-serving turn cold,
  let the facts damn him. **Ding Ling / Wang Genying / Yang Xingfo** (B12 martyrs
  and captives): render their defiance and their captivity at full force; Ding
  Ling's long first-person memoir is displayed and plain.
- **Reproduced material:** DISPLAYED blocks (memoir, newspaper clips, telegrams,
  statements) render as PLAIN paragraphs, no outer quotes; INLINE dialogue keeps its
  quote marks; an attribution intro ending in a colon is its OWN paragraph; VERSE
  takes the {p} marker as ONE paragraph with " / " line breaks. Author
  source-citations reproduced as "Author's note." at the ① anchor (QUOTED passages
  only).

## Where the story stands

The Party's clandestine arms are all drawn (intelligence ch04-08; Action/Red Squad
ch09-12; rescue and political turn ch13-14; political penetration ch15-16; radio
ch17-18). B11 (ch19-20) told the central catastrophe: Gu Shunzhang's April 1931
defection and the wave of betrayals. B12 (ch21-22) told the manhunt that followed:
Chen Geng's arrest and rescue, the raid on Wang Genying, the abduction of Ding
Ling, the assassination of Yang Xingfo. B13 (ch23-24) turns to the orderly RETREAT
of the apparatus (the Special Section reorganized, the key cadres withdrawn to
Tianjin / Moscow / the Central Soviet, Zhou Enlai's own move to Ruijin) and to the
END of the traitor Gu Shunzhang (his execution by Xu Enzeng).

## Exact next-batch scope

- **B13** = ch23 (PDF 485-526, printed 441-482, ch23s01-06) + ch24 (PDF 527-552,
  printed 483-508, ch24s01-04). Then B14 = ch25 (《伍豪启事》, PDF 553-569, 3
  sections) + ch26 (结束语) + ch27 (后记); the final batch also carries back matter,
  cover, whole-book reconciliation (check 12), COMPLETION.md, and commits the EPUB.
  (out/SURVEY.md's batch numbering runs one behind, since B05 combined ch07+ch08.)

## Open traps / environment state

- Body offset constant 44; folio-verify each opener.
- ASSEMBLY: use b12_rebuild.sh as the model; robust normalized-match surgery needs
  EXACT-opening unique markers; extend DEMANGLE for opening-word mangles; DRY-RUN
  until paragraph counts are right. Audit paragraph endings AND run
  qc_entities/check_content to catch content shifts parity misses.
- Surgery + apply_fixes are NOT idempotent (use the rebuild driver).
- data/indent is TRACKED — git checkout it if you rm -rf'd it before re-running.
- qc_entities needs "pinyin" on every glossary row and reads the bilingual PATH;
  check_content wants the EXACT shelf en form and false-matches short keys.
- verify_unit takes UNIT IDS (no --noise); check_numbers/check_content take the
  bilingual/config.
- OMP_THREAD_LIMIT=1 for tesseract; kill the process GROUP; pgrep -c tesseract must
  read 0 after a run. ocr_dual is slow — background it.
- epubcheck at /tmp/epubcheck-5.1.0 (re-fetch via setup.sh in a fresh container).
- Pre-existing failing regression test ("hook stands down on template stub");
  template maintenance, does not affect real batches.
