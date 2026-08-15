# HANDOFF — Zhou Enlai: Commander of the Hidden Front

Fresh-session handoff. The paste-ready kickoff is first; everything below it is
the state a new session needs. Batches 1-6 are COMPLETE (ch00-ch10). Next is
B07 = ch11 + ch12.

## Message to paste into the next chat

```
Zhou Enlai B07

Read CLAUDE.md, then HANDOFF.md, then STYLE.md, then book.json. Do Batch 7 =
ch11 (霞飞路侧的枪声(上) / Gunshots off Avenue Joffre (Part 1), PDF 231-246,
printed 187-202; three sections ch11s01-03: 针对周恩来的袭击 / 武装营救未能奏效 /
彭湃、杨殷等四烈士英勇就义) AND ch12 (霞飞路侧的枪声(下) / Gunshots off Avenue
Joffre (Part 2), PDF 247-262, printed 203-218; three sections ch12s01-03:
穷追叛徒白鑫 / 叛徒倒毙在红队枪口下 / 镇压叛徒的英雄谭忠余), end to end per the
CLAUDE.md pipeline. Work on branch claude/zhou-enlai; expect a stray per-task
branch and consolidate onto it (CLAUDE.md rule 2 — checkout claude/zhou-enlai,
reset --hard to origin, do the work, delete the stray local+remote).

BEFORE translating, read the final two paragraphs of ch10 in out/ch10_reading.md
(the Li Weihan account of the reprisal and the closing on the Red Squad guarding
the Central) so the voice carries over. ch11/ch12 stay in Mu Xin's narrative
voice: the attempt on Zhou Enlai's life, the failed armed rescue and the
martyrdom of Peng Pai / Yang Yin, and the hunt and killing of the traitor Bai
Xin off Avenue Joffre. ch01 is the FROZEN reference; run check_register.py
--ref out/ch01_reading.md on every unit.

Pipeline notes specific to THIS book (all proven in B01-B06, do not rediscover):
- Body offset is a CONSTANT 44: printed = PDF - 44. Folio-verify each opener by
  eye anyway. ch11 opens PDF 231 = printed 187; ch12 opens PDF 247 = printed 203.
- OCR: ocr_crop.py FIRST LAST --left 0.11 --right 0.90 --top 0.135 --bottom 0.95
  --lang chi_sim --psm 6 --running-head "隐蔽战线统帅周恩来". Verify pgrep -c
  tesseract is 0 after. Second read via ocr_dual.py (slow; run in background).
- ASSEMBLY IS THE HARD PART and mutates per batch. B06's disease was near-total
  welding (the OCR drops ALL paragraph blanks on section-opener and block-quote
  pages, so a whole section welds into a few paragraphs) PLUS OCR-dropped
  sentence-ends that merge two paragraphs silently. The B06 method (use it):
  EYEBALL EVERY CONTENT PAGE, build the true paragraph-start list per section,
  and RE-SEGMENT rather than weld-then-split — b06_surgery.py concatenates each
  section's assembled body into one blob and splits at a verified marker list
  (each marker found exactly once), with a boundary-SNAP that moves the tail
  after the last sentence-final punctuation onto the next piece (so a marker a
  few chars into its paragraph still lands the split cleanly) and refuses to
  move a trailing "(《…》)" citation forward. Recovery order (scripts/recovery/
  README.md; b06_*.py are the newest, most complete models):
  (1) b0X_strip_furniture.py: normalize garbled headings to the exact book.json
  titles (per-target guard, pull titles by id); INSERT any heading the OCR
  dropped entirely (B06's p214); truncate every author-footnote block at a
  footnote-ONLY marker (incl. gloss footnotes like 番摊/延安东路); strip embedded
  photos (delete-before / truncate-after / delete-contains) and leaked folios;
  and a RESTORE table for OCR-dropped or mangled sentence-ends (verify the exact
  bytes on the scan — B06 restored 8: 畏怯动摇。, 。①->.中 x2, 震动。, 牺牲了。->，,
  a dropped run, 抄走。->，, 就义。).
  (2) Add data/structure.json rows for the chapter + its sections BEFORE assemble
  (pull exact title bytes from book.json).
  (3) rm -rf data/indent; indents.py FIRST LAST; assemble.py <id> FIRST LAST
  --offset 44 (BOTH units before surgery — surgery is NOT idempotent).
  (4) b0X_surgery.py --apply (re-segment; DRY-RUN first, it verifies every
  marker occurs exactly once and reports counts). Then verify each ZH paragraph
  ENDS in sentence-final punctuation and STARTS with its expected phrase (a
  MID-SENTENCE end or a wrong start means an OCR-dropped 。 to add to RESTORE).
  Block quotes span pages and MUST stay ONE paragraph — do NOT mirror a page
  seam as a paragraph break (B06's English over-split 9 block-quote paragraphs
  before merging; verify EN paragraph count == ZH count).
  (5) apply_fixes.py <id> AFTER surgery (surgery markers use raw OCR bytes).
  (6) b06_pagemap.py regenerates data/pagemap/<id>.json for the post-surgery
  structure (monotonic; matches each page's first BODY line with ocr_fixes
  applied). Reuse it — edit the two build() calls to the new unit ids/ranges.
- Crop-verify every name/number/alias/date BEFORE writing; record fixes in
  data/ocr_fixes.json via apply_fixes.py. check_numbers catches DROPPED DIGITS
  (B06: 11月->1月 twice, 4月415日) and OCR phantom numerals (footnote markers
  ①->5, 《->4, ②->2, em-dash ——->一一, 尤其->万其, 士->十). Fix real garbles in
  the ZH; noise only genuine non-quantities (idioms, brand names, Arabic+万 mix).
- Checks: verify_unit reads unit ids (parity + check_numbers with data/noise.txt
  + anchors); check_numbers/qc_entities read the BILINGUAL path; check_align
  reads a unit id; check_content --config data/check_config.json (ADD ch11, ch12
  to it). check_structure --pairs SRC TGT for one unit.
- Glossary: add rows DIRECTLY nested into people/organizations/places/works/terms
  (apparatus_merge adds them FLAT and the builder crashes). Decide the PROSE
  rendering as the glossary `en`, keep the formal expansion in the NOTE. REUSE
  the already-decided 彭湃 Peng Pai, 杨殷 Yang Yin, 白鑫 Bai Xin, 谭忠余 Tan
  Zhongyu, 周恩来, 顾顺章, 陈赓, 红队 Red Squad, 打狗队 Dog-Beating Squad.
- Footnotes at reader-model density with fact-check verdicts IN the note; never
  source LLM content (WebSearch Wikipedia/Baidu/academic). Author footnotes are
  reproduced as translator notes tagged "Author's note." at the ① anchor. Note at
  FIRST appearance book-wide (grep notes.json and earlier reading files first;
  Peng Pai/Yang Yin/Bai Xin already noted in ch02/ch04 — cross-ref, do not
  re-note). Keep a "NOT re-noted" list in PROGRESS. Note anchors must be verbatim
  ASCII substrings of the reading .md (straight quotes, no em-dash spans; note
  BODIES use numeric char refs only).
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
- **B03 (ch04 Heroes of the Intelligence Front):** complete. All checks green.
- **B04 (ch05 Three Heroes of Longtan + ch06 Yang Dengying):** complete.
- **B05 (ch07 Deep into the Tiger's Den + ch08 Zhao Weigang):** complete.
- **B06 (ch09 The Action Section and the "Red Squad" + ch10 The Red Squad Draws
  Its Sword):** complete. ch09 = 53 body paragraphs, 16 notes, 1 figure (Li
  Yimang); ch10 = 34 body paragraphs (incl. Luo Yinong's {p}-verse death poem),
  9 notes, 1 figure (Li Wenyi). Two fact-check corrections footnoted (珠江
  misprint for 珠河; 阮啸仙 "defected" contradicted — he was a martyr). All checks
  green. Full record in PROGRESS.md.
- **EPUB:** out/zhou-enlai.epub = 11 of 28 chapters (ch00-ch10), 168 notes, 168
  pagebreaks; qa_epub PASS, epubcheck 0/0/0.

## Tooling in place / do not revert

- data/ocr_fixes.json: crop-verified readings for ch00-ch10; replay with
  apply_fixes.py on any fresh regen. B06 added ch09 (~30 rows) + ch10 (~20 rows).
- scripts/recovery/ (tracked): b02_* through **b06_*** strip/surgery/pagemap
  scripts + the README. The b06_* set is the CURRENT model: RE-SEGMENT by verified
  marker list with boundary-SNAP + trailing-citation guard (b06_surgery.py), a
  RESTORE table for OCR-dropped sentence-ends and an INSERT for a dropped heading
  (b06_strip_furniture.py), and b06_pagemap.py. Do not delete.
- ocr_crop.py patches (folio_present, bare-digit strip) and check_content.py
  '_'-prefix skip: keep (from B01).
- data/noise.txt: keep extending, never prune. B06 added 五粮液, 百炼成钢, 一二百,
  两手, 4万.
- data/check_config.json: docs/sources for ch00-ch10; ADD ch11, ch12 next batch.
- data/pagemap/ch09.json, ch10.json: regenerated post-surgery (b06_pagemap.py).
- Assembly: indents.py IS used in B06 (rm -rf data/indent; indents.py; assemble).
  The blank-line + indent path welds heavily on this book; RE-SEGMENTATION is the
  fix, not tuning the assembler.

## Renderings settled (glossary.json is the ledger)

- Terms: 中央特科 = "Central Special Section", 红队 = "Red Squad", 行动科 =
  "Action Section", 打狗队 = "Dog-Beating Squad", 淞沪警备司令部 = "Songhu Garrison
  Command", 中统 = "Zhongtong", 军统 = "Juntong", 党务调查科 = "Investigation
  Section", 巡捕房 = "concession police", 租界 = "the Concessions", 工部局 =
  Shanghai Municipal Council (in the NOTE; prose uses "Municipal Police" for
  工部局捕房). Works: 康生传 = "The Claws of the Dragon", 双山回忆录 = "Reminiscences
  of Shuangshan", 模糊的荧屏 = "The Blurred Screen".
- Killing verbs (STYLE ledger): 镇压/制裁 of a traitor by the Section/Red Squad =
  eliminate (or kill), 处决 = execute, 除掉 = kill; 镇压 of a movement = crush.
- Everything else in glossary.json; feed decided renderings into authority.json at
  book's end (out/term_ledger.md on completion).

## Voice sheets (carry-forward)

- **Mu Xin (author):** confident narrative-history voice, open partisan edge;
  heroes are heroes, 叛徒 traitors, the verdict goes in the note. He steps into
  the first person as interviewer/witness where the frame calls for it; keep that.
- **Zhou Enlai:** measured, analytic, unshowy; terse directives. **Chen Geng:**
  quick, cool, wry, the operational hand (leads the Red Squad reprisals in B06).
- **Reproduced block quotes** (Chen Yangshan, Li Yimang, Li Wenyi, Zhang Weizhen,
  Huang Jieran, Li Weihan in B06; the Claws of the Dragon passage): rendered as
  PLAIN paragraphs set off by a colon + attribution, no {v} markers, no outer
  quote marks. A quote that spans pages stays ONE paragraph — the block quote is
  the recurring parity trap (B06 over-split 9 before merging). Keep the quoted
  memoirs plain, concrete, colloquial, differentiated by detail; the Claws of the
  Dragon passage is Mu Xin's back-translation of an English book, re-rendered.
- **Verse** ({p}): Luo Yinong's death poem in ch10 is set as two {p} lines, each
  couplet on its own line. ch11/ch12 may carry martyrs' last words — set verse as
  {p}, one source line per line.
- **B07 stays in Mu Xin's narrative voice** (the assassination plot, the failed
  rescue, the Bai Xin hunt) — full narrative rules, keep the pace, lethal verbs.

## Where the story stands

The Special Section's two arms are now both drawn: the intelligence penetration
of the Kuomintang services (ch04-ch08) and the Action Section / Red Squad
(ch09-ch10) — Gu Shunzhang the stage magician who built it, the "Dog-Beating
Squad," and the reprisals against the couple He Jiaxing / He Zhihua who sold out
Luo Yinong. ch11-ch12 ("Gunshots off Avenue Joffre," Parts 1-2) turn to the
Bai Xin affair: the plot to kill Zhou Enlai, the failed armed rescue and the
martyrdom of Peng Pai and Yang Yin (both already noted in ch02), and the Red
Squad's relentless hunt and killing of the traitor Bai Xin, led by Tan Zhongyu.

## Exact next-batch scope

- **B07** = ch11 (PDF 231-246, printed 187-202, ch11s01-03) + ch12 (PDF 247-262,
  printed 203-218, ch12s01-03). Then B08 = ch13 + ch14 (ch13 opens PDF 263).
  (out/SURVEY.md's batch numbering runs one behind, since B05 combined ch07+ch08.)

## Open traps / environment state

- Body offset constant 44; folio-verify each opener.
- ASSEMBLY welds heavily (OCR drops paragraph blanks on opener/block-quote pages)
  AND drops sentence-end punctuation (merging paragraphs). RE-SEGMENT by verified
  marker list with the boundary-SNAP; add every dropped 。/① to the RESTORE table;
  EYEBALL every content page and verify per-SECTION EN==ZH counts. Block quotes
  spanning pages are ONE paragraph.
- Surgery (b06_surgery.py) is NOT idempotent (re-assemble both units first);
  DRY-RUN validates markers before --apply.
- check_numbers catches dropped digits and OCR phantom numerals; fix real garbles
  in the ZH, noise only genuine non-quantities.
- apparatus_merge adds glossary rows FLAT (crashes the builder); add rows nested
  directly. Note anchors must be verbatim ASCII substrings; note bodies numeric
  char refs only. Figure `before` anchor must be in the FIRST ~80 chars of its
  target paragraph.
- ocr_dual.py is slow; run in the background. OMP_THREAD_LIMIT=1 for tesseract;
  kill the process GROUP; pgrep -c tesseract must read 0 after a run.
- epubcheck at /tmp/epubcheck-5.1.0 (re-fetch via setup.sh in a fresh container).
- Pre-existing failing regression test ("hook stands down on template stub");
  template maintenance, does not affect real batches.
