# HANDOFF — Zhou Enlai: Commander of the Hidden Front

Fresh-session handoff. The paste-ready kickoff is first; everything below it is
the state a new session needs. Batches 1-7 are COMPLETE (ch00-ch12). Next is
B08 = ch13 + ch14.

## Message to paste into the next chat

```
Zhou Enlai B08

Read CLAUDE.md, then HANDOFF.md, then STYLE.md, then book.json. Do Batch 8 =
ch13 (营救任弼时、关向应 / Rescuing Ren Bishi and Guan Xiangying, PDF 263-275,
printed 219-231; three sections ch13s01-03: 两次营救任弼时 / 任弼时第二次被捕 /
营救关向应) AND ch14 (开拓新局面(上) / Opening a New Chapter (Part 1), PDF 276-295,
printed 232-251; three sections ch14s01-03: 纠正了单纯恐怖行动,引向政治斗争轨道 /
旷世奇才杨度 / 两个国会议员:梅宝玑、胡鄂公), end to end per the CLAUDE.md pipeline.
Work on branch claude/zhou-enlai; expect a stray per-task branch and consolidate
onto it (CLAUDE.md rule 2 — checkout claude/zhou-enlai, reset --hard to origin,
do the work, delete the stray local+remote).

BEFORE translating, read the final two paragraphs of ch12 in out/ch12_reading.md
(the Tan Zhongyu bio and his death crossing the border) so the voice carries
over. ch13/ch14 stay in Mu Xin's narrative voice, but ch14 turns from action to
the political/intelligence-penetration mode (Yang Du the polymath, the two MPs)
— apply STYLE.md's "exposition and political framing" rules hardest there.
ch01 is the FROZEN reference; run check_register.py --ref out/ch01_reading.md on
every unit.

Pipeline notes specific to THIS book (all proven in B01-B07, do not rediscover):
- Body offset is a CONSTANT 44: printed = PDF - 44. Folio-verify each opener by
  eye anyway. ch13 opens PDF 263 = printed 219; ch14 opens PDF 276 = printed 232.
- OCR: ocr_crop.py FIRST LAST --left 0.11 --right 0.90 --top 0.135 --bottom 0.95
  --lang chi_sim --psm 6 --running-head "隐蔽战线统帅周恩来". Verify pgrep -c
  tesseract is 0 after. Second read via ocr_dual.py (slow; run in background).
- ASSEMBLY IS THE HARD PART and mutates per batch. The disease (B06-B07) is
  near-total welding on section-opener / block-quote / newspaper / photo pages
  PLUS OCR-dropped sentence-ends that merge two paragraphs silently. USE THE B07
  MODEL (scripts/recovery/b07_*.py are the newest, most complete):
  (1) b0X_strip_furniture.py: normalize garbled headings to the EXACT book.json
  titles (per-target guard, pull titles by id); INSERT any heading BOTH OCR
  configs dropped; DELETE_BEFORE / BLANK / TRUNCATE_AFTER to strip embedded
  photos and newspaper facsimiles (b07 added an OVERWRITE table for a page whose
  clean body was mangled by facsimile bleed — transcribe it off the scan);
  truncate every author-footnote block at a footnote-ONLY marker; and a RESTORE
  table for OCR-dropped sentence-ends / stray footnote-marker chars / dropped
  runs (verify exact bytes on the scan; b07 restored 13). The RESTORE quote char
  is ASCII " (0x22) in this OCR, not curly — check bytes before writing anchors.
  (2) Add data/structure.json rows for the chapter + its sections BEFORE assemble
  (pull exact title bytes from book.json).
  (3) rm -rf data/indent; indents.py FIRST LAST; assemble.py <id> FIRST LAST
  --offset 44 (BOTH units before surgery — surgery is NOT idempotent).
  (4) b0X_surgery.py --apply (re-segment; DRY-RUN first, it verifies every
  marker occurs exactly once). Build the true per-section paragraph-START marker
  list by EYEBALLING every content page. Then verify each ZH paragraph ENDS in
  sentence-final punctuation and STARTS with its expected phrase; a MID-SENTENCE
  end or a stray leading char (footnote-marker ① OCR'd as 史/吓/岂/') means an
  OCR-dropped 。 to add to RESTORE. Block quotes / reproduced newspaper articles
  span pages: each is ONE paragraph unless the source indents a new one; verify
  EN paragraph count == ZH count.
  (5) apply_fixes.py <id> AFTER surgery. apply_fixes is NOT idempotent — a
  "wrong" that is a substring of its "right" corrupts on a SECOND apply; always
  clean-regen (strip->assemble->surgery) before apply_fixes, never incrementally.
  (6) b0X_pagemap.py regenerates data/pagemap/<unit>.json (edit the two build()
  calls to the new unit ids/ranges).
- Crop-verify every name/number/alias/date BEFORE writing; record fixes in
  data/ocr_fixes.json via apply_fixes.py. check_numbers catches DROPPED DIGITS
  (B07: 1月11日->11月11日 twice, 11月5日->9日, 9多发->90多发) and OCR phantom
  numerals (footnote 《->4, 了->7, 士->七/十, 千->干, leaked folio ji95, 乃->万).
  Fix real garbles in the ZH; noise only genuine non-quantities (place/rail
  compounds with a digit-glyph, idioms, ages written 廿/念).
- Checks: verify_unit reads unit ids (parity + check_numbers with data/noise.txt
  + anchors); check_numbers/qc_entities read the BILINGUAL path; check_align
  reads a unit id; check_content --config data/check_config.json (ADD ch13, ch14
  to docs AND sources). check_structure --pairs SRC TGT for one unit.
- Glossary: add rows DIRECTLY nested into people/organizations/places/works/terms
  (apparatus_merge adds them via the batch file, validated). Decide the PROSE
  rendering as the glossary `en`, keep the formal expansion in the NOTE. REUSE
  the already-decided 周恩来, 顾顺章, 陈赓, 康生, 陈云, 红队 Red Squad, 打狗队
  Dog-Beating Squad, 中央特科 Central Special Section; 任弼时 and 关向应 recur here
  (关向应 already in glossary as Guan Xiangying; add 任弼时 = Ren Bishi).
- Footnotes at reader-model density with fact-check verdicts IN the note; never
  source LLM content (WebSearch Wikipedia/Baidu/academic; NEVER Grokipedia).
  Author footnotes reproduced as translator notes tagged "Author's note." at the
  ① anchor. Note at FIRST appearance book-wide (grep notes.json and earlier
  reading files first). Note anchors must be verbatim ASCII substrings of the
  reading .md (straight quotes, no en/em-dash spans; note BODIES use numeric
  char refs only). Figure `alt` must NOT contain a double quote (breaks the XML
  attribute — use single quotes); figure `file` is a BARE basename in data/figs/.
- Cite the book's PRINTED FOLIO in notes, never the PDF page.
- Build the cumulative EPUB, qa_epub green, epubcheck (/tmp/epubcheck-5.1.0).
- Update PROGRESS.md and HANDOFF.md; commit and push to claude/zhou-enlai.

Deliver in THIS chat: the built EPUB attached, AND the next kickoff pasted
verbatim in a fenced code block. Both, every batch.
```

## Status: what is DONE

- **Survey + B01 (ch00 Preface + ch01):** complete, voice gate approved; ch01 is
  the frozen register reference.
- **B02 (ch02 + ch03 Chen Geng):** complete. All checks green.
- **B03 (ch04 Heroes of the Intelligence Front):** complete.
- **B04 (ch05 Three Heroes of Longtan + ch06 Yang Dengying):** complete.
- **B05 (ch07 Deep into the Tiger's Den + ch08 Zhao Weigang):** complete.
- **B06 (ch09 The Action Section and the "Red Squad" + ch10 The Red Squad Draws
  Its Sword):** complete.
- **B07 (ch11 Gunshots off Avenue Joffre Part 1 + ch12 Part 2):** complete.
  ch11 = 39 body paras, 11 notes, 1 figure (Peng Pai arrest-site photo); ch12 =
  42 body paras, 8 notes, 3 figures (Hehe Fang entrance, 时报 + 字林西报
  facsimiles). The Bai Xin affair: martyrdom of Peng Pai/Yang Yin/Yan
  Changyi/Xing Shizhen, the failed rescue, the Red Squad's killing of Bai Xin,
  the press coverage, and Tan Zhongyu. All checks green. Record in PROGRESS.md.
- **EPUB:** out/zhou-enlai.epub = 13 of 28 chapters (ch00-ch12), 187 notes, 198
  pagebreaks; qa_epub PASS, epubcheck 0/0/0.

## Tooling in place / do not revert

- data/ocr_fixes.json: crop-verified readings for ch00-ch12; replay with
  apply_fixes.py on any fresh regen. B07 added ch11 (~90 rows) + ch12 (~40 rows).
- scripts/recovery/ (tracked): b02_* through **b07_*** strip/surgery/pagemap
  scripts + README. The b07_* set is the CURRENT model: adds an OVERWRITE table
  (clean scan transcription for a facsimile-mangled page) on top of the b06
  RE-SEGMENT-by-marker-list-with-boundary-SNAP method. Do not delete.
- ocr_crop.py patches, check_content.py '_'-prefix skip: keep (from B01).
- data/noise.txt: keep extending, never prune. B07 added 百禄里, 两广, 广三铁路,
  广九, 丘八, 万望, 万难, 千万群众, 惊惶万状, 十恶不赦, 第二天, 这两天.
- data/check_config.json: docs+sources for ch00-ch12; ADD ch13, ch14 next batch.
- data/pagemap/ch11.json, ch12.json: regenerated post-surgery (b07_pagemap.py).
- Assembly: indents.py IS used (rm -rf data/indent; indents.py; assemble); the
  fix is RE-SEGMENTATION (b07_surgery.py), not tuning the assembler.
- KNOWN HAZARD: apply_fixes.py is not idempotent (substring wrong->right).
  Always clean-regen before apply_fixes; never apply incrementally on fixed text.

## Renderings settled (glossary.json is the ledger)

- Terms: 中央特科 = "Central Special Section", 红队 = "Red Squad", 行动科 =
  "Action Section", 打狗队 = "Dog-Beating Squad", 淞沪警备司令部 = "Songhu Garrison
  Command", 巡捕房 = "concession police", 租界 = "the Concessions", 工部局 =
  Shanghai Municipal Council (in the NOTE; prose uses "Municipal Police").
- B07 people: 杨殷 Yang Yin, 白鑫 Bai Xin, 颜昌颐 Yan Changyi, 邢士贞 Xing Shizhen,
  张际春 Zhang Jichun, 范争波 Fan Zhengbo, 熊式辉 Xiong Shihui, 谭忠余 Tan Zhongyu,
  周惠年 Zhou Huinian, 康生 Kang Sheng, 陈云 Chen Yun. B07 places: 和合坊 Hehe
  Fang, 蒲石路 Rue Bourgeat, 白宫饭店 White Palace Hotel. B07 works: 字林西报 North
  China Daily News, 时报 Shi Bao, 申报 Shen Bao, 大陆报 The China Press.
- Killing verbs (STYLE ledger): 镇压/制裁 of a traitor by the Section/Red Squad =
  eliminate/kill, 处决 = execute, 除掉 = kill; 镇压 of a movement = crush.
- Feed decided renderings into authority.json at book's end (out/term_ledger.md).

## Voice sheets (carry-forward)

- **Mu Xin (author):** confident narrative-history voice, open partisan edge;
  heroes are heroes, 叛徒 traitors, the verdict goes in the note. He steps into
  the first person as interviewer/witness where the frame calls for it (the whole
  Tan Zhongyu surname-inquiry in ch12 is Mu Xin recounting his research letters).
- **Zhou Enlai:** measured, analytic, unshowy; terse directives. He is also the
  RHETORICAL voice in his Red Flag Daily martyr-essay (ch11): keep the heat full
  in the peroration ("ever onward in effort, ever onward in struggle"). **Chen
  Geng:** quick, cool, the operational hand (directs the Bai Xin killing).
- **Reproduced block quotes** (memoir quotes: Ke Lin, Li Qiang; reproduced
  NEWSPAPER articles: 时报, 字林西报; Zhou Enlai's essay): rendered as PLAIN
  paragraphs. Attribution intro ending in a colon is its OWN paragraph; the block
  quote a SEPARATE paragraph (no outer quotes). INLINE quotes (intro + quote in
  one source paragraph) keep quote marks inline. A quote/article spanning pages
  is ONE paragraph unless the source indents a new one. Reproduced newspaper
  prose keeps a period-newspaper register (the 时报 quote is formal literary
  Chinese; the 字林西报 was English — render as natural English news prose).
- **Reproduced letters** (the martyrs' joint final report in ch11): salutation /
  body / short lines / signature as separate paragraphs, set as a letter.
- **B08 (ch13 rescues; ch14 political turn):** ch13 stays full narrative (the Ren
  Bishi / Guan Xiangying rescues). ch14 shifts to exposition + character
  portraits (Yang Du the Qing-to-CCP polymath; two secret MPs) — highest-risk
  zone for stiltedness; break the information into short confident statements.

## Where the story stands

The Special Section's arms are drawn (intelligence penetration ch04-ch08; the
Action Section / Red Squad ch09-ch12). ch11-ch12 closed the Bai Xin affair: the
martyrdom of Peng Pai and Yang Yin, the failed rescue, and the Red Squad's
relentless hunt and killing of the traitor Bai Xin off Avenue Joffre, led by Tan
Zhongyu. ch13 turns to two dramatic RESCUES (Ren Bishi, twice; Guan Xiangying —
who appears in ch12 warning Ke Lin). ch14 opens the "new situation": correcting
pure-terror tactics toward political struggle, and the recruitment of remarkable
outside figures (Yang Du; the parliamentarians Mei Baoji and Hu Egong).

## Exact next-batch scope

- **B08** = ch13 (PDF 263-275, printed 219-231, ch13s01-03) + ch14 (PDF 276-295,
  printed 232-251, ch14s01-03). Then B09 = ch15 (开拓新局面(下), opens PDF 296) +
  ch16. (out/SURVEY.md's batch numbering runs one behind, since B05 combined
  ch07+ch08.)

## Open traps / environment state

- Body offset constant 44; folio-verify each opener.
- ASSEMBLY welds heavily AND drops sentence-ends; RE-SEGMENT by verified marker
  list with the boundary-SNAP; add every dropped 。/① to RESTORE; EYEBALL every
  content page; verify per-SECTION EN==ZH counts. Block quotes / newspaper
  reproductions spanning pages are ONE paragraph unless the source indents.
- Surgery is NOT idempotent (re-assemble both units first); DRY-RUN before --apply.
- apply_fixes is NOT idempotent (substring wrong->right corrupts on re-apply);
  clean-regen before every apply_fixes.
- Figure `alt` must not contain a double quote (XML attribute break); `file` is a
  bare basename in data/figs/. Note anchors verbatim ASCII substrings; note
  bodies numeric char refs only.
- ocr_dual.py is slow; run in the background. OMP_THREAD_LIMIT=1 for tesseract;
  kill the process GROUP; pgrep -c tesseract must read 0 after a run.
- epubcheck at /tmp/epubcheck-5.1.0 (re-fetch via setup.sh in a fresh container).
- Pre-existing failing regression test ("hook stands down on template stub");
  template maintenance, does not affect real batches.
