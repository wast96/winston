# HANDOFF — Zhou Enlai: Commander of the Hidden Front

Fresh-session handoff. The paste-ready kickoff is first; everything below it is
the state a new session needs. Batches 1-8 are COMPLETE (ch00-ch14). Next is
B09 = ch15 + ch16.

## Message to paste into the next chat

```
Zhou Enlai B09

Read CLAUDE.md, then HANDOFF.md, then STYLE.md, then book.json. Do Batch 9 =
ch15 (开拓新局面(中) / Opening a New Chapter (Part 2), PDF 296-320, printed
252-276; three sections ch15s01-03: 贡生—省议员—开明绅士刘少白 / 牧师和律师 /
向新闻界发展) AND ch16 (开拓新局面(下) / Opening a New Chapter (Part 3), PDF
321-332, printed 277-288; three sections ch16s01-03: 淞沪警备司令部 /
"第四号政治密查员" / 英法租界巡捕房), end to end per the CLAUDE.md pipeline.
Work on branch claude/zhou-enlai; expect a stray per-task branch and consolidate
onto it (CLAUDE.md rule 2 — checkout claude/zhou-enlai, reset --hard to origin,
do the work, delete the stray local+remote).

BEFORE translating, read the final two paragraphs of ch14 in out/ch14_reading.md
(Hu Egong's Feng Yuxiang liaison and his 1934 arrest / defection to Kong Xiangxi)
so the voice carries over. ch15/ch16 stay in Mu Xin's narrative-history voice and
continue ch14's political-penetration mode: ch15 is three more recruited outside
figures (刘少白 the enlightened gentry-scholar — already met in ch14 and in the
glossary as Liu Shaobai; a pastor and a lawyer; the move into the press), ch16
turns to penetrating the enemy's own organs (the Songhu Garrison Command, a
"political investigator," the British/French concession police). Apply STYLE.md's
"exposition and political framing" rules hardest — short confident statements, no
dash-glosses. ch01 is the FROZEN reference; run check_register.py --ref
out/ch01_reading.md on every unit.

Pipeline notes specific to THIS book (all proven in B01-B08, do not rediscover):
- Body offset is a CONSTANT 44: printed = PDF - 44. Folio-verify each opener by
  eye anyway. ch15 opens PDF 296 = printed 252; ch16 opens PDF 321 = printed 277.
- OCR: ocr_crop.py FIRST LAST --left 0.11 --right 0.90 --top 0.135 --bottom 0.95
  --lang chi_sim --psm 6 --running-head "隐蔽战线统帅周恩来". Verify pgrep -c
  tesseract is 0 after. Second read via ocr_dual.py (slow; run in background —
  in B08 the dual read was not needed; names were crop-verified directly).
- ASSEMBLY IS THE HARD PART and mutates per batch. USE THE B08 MODEL
  (scripts/recovery/b08_*.py are the newest, most complete; they follow b07):
  (1) b0X_strip_furniture.py: normalize garbled headings to the EXACT book.json
  titles (per-target guard len(good)+4, pull titles by id); RESTORE stray
  footnote-marker chars (① OCR'd as 包/中/? etc.) and spurious leading 201C
  quotes (OCR reads the paragraph indent as a “); DROP_LINE any embedded-photo
  caption sitting mid-page; truncate every author-footnote block at a
  footnote-ONLY marker; and — THE B08 LESSON — RESTORE every OCR-dropped
  sentence-end that would weld two paragraphs. The disease this batch was OCR
  dropping a SHORT TRAILING LINE (物。 / 罢了。) or rendering a 。 as an ASCII '.'
  ('.'  is 0x2e; the enumeration comma 、 is ALSO OCR'd as '.', so only the
  ONE that is a real sentence end matters — find it because the surgery
  boundary-snap then splits at the wrong 。). Verify exact bytes on the scan;
  the RESTORE quote char is ASCII " (0x22) in this OCR, curly “ ” are 201C/201D.
  (2) Add data/structure.json rows for the chapter + its sections BEFORE assemble
  (pull exact title bytes from book.json).
  (3) rm -rf data/indent; indents.py FIRST LAST; assemble.py <id> FIRST LAST
  --offset 44 (BOTH units before surgery — surgery is NOT idempotent).
  (4) b0X_surgery.py --apply. markers[i] starts piece i+1; a blob of N paragraphs
  needs N-1 markers (piece 0 is the blob head). markers are RAW-OCR substrings
  (apply_fixes runs AFTER). DRY-RUN first (verifies every marker occurs exactly
  once, in order). Build the marker list by EYEBALLING every content page. Then
  verify each ZH paragraph ENDS in sentence-final punct (attribution-intro colons
  are the only OK exceptions) and that each piece STARTS with its marker (the
  boundary-snap may correctly prepend the true paragraph start, e.g. "陈刻",
  before a mid-paragraph marker — that is fine). Poem/verse and reproduced
  block quotes (辞海-style dictionary entries, memoir quotes) are each ONE
  paragraph; a 七律 renders as a SINGLE {p} line with " / " between the couplets
  (ch10/ch14 model). Verify EN paragraph count == ZH count.
  (5) apply_fixes.py <id> AFTER surgery. apply_fixes is NOT idempotent — always
  clean-regen (restore data/txt from a backup, strip->assemble->surgery) before
  apply_fixes, never incrementally. (Keep a backup of the raw data/txt for the
  batch pages before the FIRST strip; you WILL regen several times.)
  (6) b0X_pagemap.py regenerates data/pagemap/<unit>.json (edit the two build()
  calls to the new unit ids/ranges).
- Crop-verify every name/number/alias/date BEFORE writing; record fixes in
  data/ocr_fixes.json via apply_fixes.py. B08 had HEAVY name garble (任弼时 alone
  had 22 OCR variants). check_numbers catches phantom numerals from glyph garbles
  ($=5, S=5, 《=4, 乃->万, 阅->六, 雨->十) and dropped digits; fix real garbles in
  the ZH, carry real values in the English (12点 -> "twelve"; use figures for 100+
  per STYLE), noise ONLY genuine non-quantities (names/places with a digit-glyph:
  王老九, 字新三, 百货大楼, 刘锡五).
- Checks: verify_unit reads unit ids (parity + check_numbers with data/noise.txt
  + anchors); qc_entities reads the BILINGUAL path (out/<id>_bilingual.md) — its
  glossary rows need BOTH "en" AND "pinyin" keys or it KeyErrors; check_align
  reads a unit id; check_content --config data/check_config.json (ADD ch15, ch16
  to docs AND sources; it wants each glossary EN form present in the paired
  paragraph, so spell out "Chinese Communist Party" etc. where the source has the
  full 中国共产党). check_structure --pairs SRC TGT for one unit.
- Glossary: add rows DIRECTLY nested into people/organizations/places/works/terms
  (NOT via apparatus_merge, which drops them at top level where qc_entities can't
  reach; give every row "en" + "pinyin" + "status"). Decide the PROSE rendering as
  the glossary `en`, keep the formal expansion in the NOTE. REUSE the already-
  decided renderings; 刘少白 Liu Shaobai and 淞沪警备司令部 Songhu Garrison Command
  and 龙华 Longhua all recur in ch15/ch16 (already in glossary from B08/earlier).
- Footnotes at reader-model density with fact-check verdicts IN the note; never
  source LLM content (WebSearch Wikipedia/Baidu/academic; NEVER Grokipedia; block
  grokipedia.com). Author footnotes reproduced as translator notes tagged
  "Author's note." at the ① anchor. Note at FIRST appearance book-wide (grep
  notes.json and earlier reading files first). Note anchors must be verbatim ASCII
  substrings of the reading .md (straight quotes, no en/em-dash spans; note BODIES
  use numeric char refs only, e.g. &#8212; &#8211; &#160;). Figure `alt` must NOT
  contain a double quote; figure `file` is a BARE basename in data/figs/.
- Cite the book's PRINTED FOLIO in notes, never the PDF page.
- Build the cumulative EPUB, qa_epub green, epubcheck (/tmp/epubcheck-5.1.0).
- Update PROGRESS.md and HANDOFF.md; commit and push to claude/zhou-enlai.

Deliver in THIS chat: the built EPUB attached, AND the next kickoff pasted
verbatim in a fenced code block. Both, every batch.
```

## Status: what is DONE

- **Survey + B01 (ch00 Preface + ch01):** complete, voice gate approved; ch01 is
  the frozen register reference.
- **B02 (ch02 + ch03 Chen Geng):** complete.
- **B03 (ch04 Heroes of the Intelligence Front):** complete.
- **B04 (ch05 Three Heroes of Longtan + ch06 Yang Dengying):** complete.
- **B05 (ch07 Deep into the Tiger's Den + ch08 Zhao Weigang):** complete.
- **B06 (ch09 The Action Section and the "Red Squad" + ch10 The Red Squad Draws
  Its Sword):** complete.
- **B07 (ch11 Gunshots off Avenue Joffre Part 1 + ch12 Part 2):** complete.
- **B08 (ch13 Rescuing Ren Bishi and Guan Xiangying + ch14 Opening a New Chapter
  Part 1):** complete. ch13 = 34 body paras, 8 notes, 0 figures (the two arrests
  and rescues of Ren Bishi, told with the torture scene at full heat; the
  document-rescue that freed Guan Xiangying). ch14 = 44 body paras, 11 notes,
  1 figure (一品香旅社 hotel photo). The chapter turns from action to the
  political-penetration mode: correcting Gu Shunzhang's pure-terror tactics, and
  the recruitment of Yang Du (monarchist-turned-Communist, with his 七律 poem and
  the 1979 Cihai entry) and the two MPs Mei Baoji and Hu Egong (with the long Yang
  Xianzhen arrest set-piece in Beiping). All checks green. Details in PROGRESS.md.
- **EPUB:** out/zhou-enlai.epub = 15 of 28 chapters (ch00-ch14), 206 notes, 231
  pagebreaks; qa_epub PASS, epubcheck 0/0/0.

## Tooling in place / do not revert

- data/ocr_fixes.json: crop-verified readings for ch00-ch14; replay with
  apply_fixes.py on any fresh regen. B08 added ch13 (57 rows) + ch14 (67 rows).
- scripts/recovery/ (tracked): b02_* through **b08_*** strip/surgery/pagemap
  scripts + README. The b08_* set is the CURRENT model (follows b07; adds the
  DROP_LINE helper for a single mid-page caption line and three dropped-sentence-
  end RESTOREs). Do not delete.
- ocr_crop.py patches, check_content.py '_'-prefix skip: keep (from B01).
- data/noise.txt: keep extending, never prune. B08 added 王老九, 字新三, 百货大楼,
  刘锡五.
- data/check_config.json: docs+sources for ch00-ch14; ADD ch15, ch16 next batch.
- data/pagemap/ch13.json, ch14.json: regenerated post-surgery (b08_pagemap.py).
- Assembly: indents.py IS used; the fix is RE-SEGMENTATION (b08_surgery.py).
- KNOWN HAZARD: apply_fixes.py is not idempotent (substring wrong->right). Always
  clean-regen before apply_fixes; keep a backup of raw data/txt for the batch.
- KNOWN HAZARD: qc_entities.py KeyErrors if a glossary row lacks a "pinyin" key —
  every row you add (people AND orgs/places/works) needs "en" + "pinyin".

## Renderings settled (glossary.json is the ledger)

- Terms held: 中央特科 Central Special Section, 红队 Red Squad, 打狗队 Dog-Beating
  Squad, 淞沪警备司令部 Songhu Garrison Command, 巡捕房 concession police, 租界 the
  Concessions, 白色恐怖 the White Terror.
- B08 people: 任弼时 Ren Bishi, 关向应 Guan Xiangying, 陈琮英 Chen Congying (Ren's
  wife; 琮 crop-verified), 杨度 Yang Du, 杜月笙 Du Yuesheng, 胡鄂公 Hu Egong, 杨献珍
  Yang Xianzhen, 刘少白 Liu Shaobai, 梅宝玑 Mei Baoji, 章士钊 Zhang Shizhao, 黄金荣
  Huang Jinrong, 张啸林 Zhang Xiaolin, 胡汉民 Hu Hanmin, 王闿运 Wang Kaiyun, 周朴农
  Zhou Punong, 柳湜 Liu Shi, 余昌生 Yu Changsheng, 郭亮 Guo Liang, 梅龚彬 Mei
  Gongbin, 梅中林 Mei Zhonglin. Orgs: 政学系 Political Study Clique, 改组派 Kuomintang
  Reorganizationists, 筹安会 Peace Planning Society, 反帝大同盟 Anti-Imperialist
  League, 顺直省委 Shun-Zhi provincial committee, 中华共进会 China Mutual Advancement
  Society, 中国互济会 China Mutual Aid Society, 中国民权保障同盟 China League for the
  Protection of Civil Rights, 中国自由大同盟 China Freedom League. Places: 提篮桥监狱
  Tilanqiao Prison, 龙华 Longhua. Works: 辞海 Cihai, 红旗 Red Flag, 大公报 Ta Kung
  Pao, 泰东日报 Taidong Daily.
- Killing verbs (STYLE ledger): 镇压/制裁 of a traitor by the Section/Red Squad =
  eliminate/kill; 处决 = execute; 除掉 = kill; 镇压 of a movement = crush.
- 中国 government/party names: spell out "Chinese Communist Party" for 中国共产党
  in a paragraph that has it (check_content enforces the glossary EN in-paragraph).
- Feed decided renderings into authority.json at book's end (out/term_ledger.md).

## Voice sheets (carry-forward)

- **Mu Xin (author):** confident narrative-history voice, open partisan edge;
  heroes are heroes, 叛徒 traitors, the verdict goes in the note. In ch14 he steps
  into exposition (potted histories of Du Yuesheng, the KMT factions, the two MPs)
  — this is the highest-risk zone for stiltedness; break it into short confident
  statements, no dash-glosses.
- **Zhou Enlai:** measured, analytic, unshowy; terse directives ("no reckless
  killing of traitors, and only those who did great harm; ... no kidnapping for
  ransom"). **Chen Geng:** quick, cool, the operational hand (runs the Guan
  Xiangying document-rescue and the Tianjin political work). **Ren Bishi:** in the
  prison scenes, steady and reasoning ("learn to argue with the enemy, to reason
  the struggle out").
- **Reproduced material** (memoir quotes: Zhou Punong, Zhang Ji'en, Li Moying,
  Yang Xianzhen's long Beiping recollection; the 辞海 dictionary entry; the Yin Qi
  book quote): rendered as PLAIN paragraphs. An attribution intro ending in a colon
  is its OWN paragraph; the block quote a SEPARATE paragraph, no outer quotes.
  INLINE quotes (intro + quote in one source paragraph, common in ch14) keep their
  quote marks inline. A quote/entry spanning pages is ONE paragraph unless the
  source indents a new one. Verse (Yang Du's 七律) = a SINGLE {p} line, couplets
  joined by " / ".
- **B09 (ch15/ch16 continue the political turn):** ch15 = three recruited outside
  figures (Liu Shaobai the enlightened gentry-scholar; a pastor and a lawyer; the
  press). ch16 = penetrating the enemy's organs (the Songhu Garrison Command, a
  political-investigator asset, the concession police). Same exposition-heavy,
  portrait-heavy register as ch14 — highest-risk for stiltedness.

## Where the story stands

The Special Section's arms are drawn (intelligence penetration ch04-ch08; the
Action Section / Red Squad ch09-ch12). B08 opened a NEW phase: ch13 showed the
Section as rescuer (Ren Bishi twice, Guan Xiangying's trunk of documents), and
ch14 recorded the deliberate TURN from pure terror to political struggle under
Zhou Enlai and Chen Geng — correcting Gu Shunzhang's excesses (he is now on the
road to his 1931 defection, foreshadowed) and recruiting eminent outsiders (Yang
Du; the parliamentarians Mei Baoji and Hu Egong; Yang Xianzhen). ch15-ch16
continue that political-penetration arc.

## Exact next-batch scope

- **B09** = ch15 (PDF 296-320, printed 252-276, ch15s01-03) + ch16 (PDF 321-332,
  printed 277-288, ch16s01-03). Then B10 = ch17 (电讯科长"曾培鸿"——李强, opens PDF
  333) + ch18. (out/SURVEY.md's batch numbering runs one behind, since B05
  combined ch07+ch08.)

## Open traps / environment state

- Body offset constant 44; folio-verify each opener.
- ASSEMBLY welds heavily AND drops sentence-ends (esp. a SHORT trailing line, or
  a 。 rendered as ASCII '.'); RE-SEGMENT by verified marker list; add every
  dropped 。 to RESTORE; EYEBALL every content page; verify per-SECTION EN==ZH.
- Surgery is NOT idempotent (re-assemble both units first); DRY-RUN before --apply.
- apply_fixes is NOT idempotent (clean-regen before every apply_fixes; keep a
  backup of raw data/txt for the batch pages).
- qc_entities needs "pinyin" on every glossary row; check_content wants the
  glossary EN form present in the paired paragraph.
- Figure `alt` must not contain a double quote; `file` is a bare basename in
  data/figs/. Note anchors verbatim ASCII substrings; note bodies numeric char
  refs only.
- ocr_dual.py is slow; run in the background. OMP_THREAD_LIMIT=1 for tesseract;
  kill the process GROUP; pgrep -c tesseract must read 0 after a run.
- epubcheck at /tmp/epubcheck-5.1.0 (re-fetch via setup.sh in a fresh container).
- Pre-existing failing regression test ("hook stands down on template stub");
  template maintenance, does not affect real batches.
