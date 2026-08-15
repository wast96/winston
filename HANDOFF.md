# HANDOFF — Zhou Enlai: Commander of the Hidden Front

Fresh-session handoff. The paste-ready kickoff is first; everything below it is
the state a new session needs. Batches 1-4 are COMPLETE (ch00-ch06). Next is
B05 = ch07 + ch08.

## Message to paste into the next chat

```
Zhou Enlai B05

Read CLAUDE.md, then HANDOFF.md, then STYLE.md, then book.json. Do Batch 5 =
ch07 (深入龙潭虎穴 / Deep into the Tiger's Den, PDF 154-172, printed 110-128; five
sections ch07s01-05: 调查科与徐恩曾 / 周恩来说"你们把它拿过来" / 抓住徐恩曾的弱点拿到
绝密电码本 / 用他的护照和钱办我们的情报 / 打进国民党最高特务机关的典型) AND ch08
(奉天讲武堂教官——赵唯刚 / Fengtian Military Academy Instructor — Zhao Weigang, PDF
173-197, printed 129-153; six sections ch08s01-06), end to end per the CLAUDE.md
pipeline. Work on branch claude/zhou-enlai; expect a stray per-task branch and
consolidate onto it (CLAUDE.md rule 2 — checkout claude/zhou-enlai, reset --hard
to origin, do the work, delete the stray local+remote).

BEFORE translating, read the final two paragraphs of ch06 in out/ch06_reading.md
(the "pulling out" summation, Peng Pai/Yang Yin) so the voice carries over. ch01
is the FROZEN reference; run check_register.py --ref out/ch01_reading.md on every
unit.

Pipeline notes specific to THIS book (all proven in B01-B04, do not rediscover):
- Body offset is a CONSTANT 44: printed = PDF - 44. Folio-verify each opener by
  eye anyway. ch07 opens PDF 154 = printed 110; ch08 opens PDF 173 = printed 129.
- OCR: ocr_crop.py FIRST LAST --left 0.11 --right 0.90 --top 0.135 --bottom 0.95
  --lang chi_sim --psm 6 --running-head "隐蔽战线统帅周恩来". Verify pgrep -c
  tesseract is 0 after. Second read via ocr_dual.py (it is slow, ~3 configs per
  page; run it in the background, it timed out in the foreground in B04).
- ASSEMBLY IS THE HARD PART. indents.py unreliable; use the blank-line path,
  which FORCE-BREAKS at every page seam, drops in-page blanks, and DROPS/WELDS at
  author-footnote and photo seams. Replay the recovery pattern (scripts/recovery/
  README.md; b04_*.py are the latest models):
  (1) bXX_strip_furniture.py: normalize garbled chapter/section headings to the
  exact structure.json titles with a PER-TARGET length guard (len(good)+4), NOT a
  single global maxlen (headings run 8-21 chars and a body line can share a
  heading's tokens); truncate every author-footnote block at a footnote-ONLY
  marker (verify the exact OCR bytes of the marker first, they garble); blank
  full-page photos; strip top/bottom body-page photos with keep-from/keep-through.
  (2) Add structure.json rows for the chapter + its sections BEFORE assemble.
  (3) rm -rf data/indent; assemble.py <id> FIRST LAST --offset 44.
  (4) bXX_surgery.py: EYEBALL EVERY CONTENT PAGE for paragraph indents, then apply
  splits (one line carrying >1 source paragraph) and welds (page-seam splits +
  dropped in-page blanks). Set-off block quotes are the trap: their extra line
  spacing is captured as a blank BETWEEN EVERY LINE and the assembler over-splits
  them (B04: the 宋治家 quote split into 9). If you re-run surgery, re-assemble
  FIRST (surgery is not idempotent on an already-surgered file). Verify per-section
  EN/ZH paragraph counts, not just the total.
  (5) apply_fixes.py <id> AFTER surgery (surgery markers use the raw OCR bytes).
  (6) Hand-regenerate data/pagemap/<id>.json for the post-surgery structure
  (match each page's first BODY line, after fixes, into the final ZH; skip photo
  pages). qa_epub only checks marker/page-list COUNT parity, but keep indices
  accurate and monotonic so folios land right and don't collide.
- Crop-verify every name/number/alias/date BEFORE writing; record fixes in
  data/ocr_fixes.json via apply_fixes.py. ch07's subjects: the theft of the
  国民党最高特务机关's top-secret codebook via 徐恩曾's weakness (his mistress);
  Zhou Enlai's "拿过来" directive. ch08's subject is 赵唯刚 (Zhao Weigang), the
  Fengtian (奉天/Shenyang) Military Academy instructor who warned a month before
  "九一八" (18 September 1931) that Japan would strike. Watch dropped digits in
  dates and unit numbers, and any 夹带的英文.
- Checks: verify_unit reads unit ids; check_numbers/qc_entities read the
  BILINGUAL path; check_align reads a unit id; check_content --config (ADD ch07,
  ch08 to data/check_config.json). check_structure --pairs SRC TGT for one unit
  (the full --config run opens ch00-ch04 sources that no longer exist locally).
- Glossary: add rows DIRECTLY nested into people/organizations/places/works/terms
  (apparatus_merge adds them FLAT and the builder crashes on a top-level string;
  B04 sidestepped this by editing glossary.json directly and using apparatus_merge
  for notes+figures only).
- Footnotes at reader-model density with fact-check verdicts IN the note; never
  source LLM content (WebSearch Wikipedia/Baidu/academic). Author footnotes are
  reproduced as translator notes tagged "Author's note." at the ① anchor. Note at
  FIRST appearance book-wide (grep notes.json and earlier reading files first);
  keep a "NOT re-noted" list in PROGRESS.
- Cite the book's PRINTED FOLIO in notes, never the PDF page.
- Build the cumulative EPUB, qa_epub green, epubcheck (/tmp/epubcheck-5.1.0).
- Update PROGRESS.md and HANDOFF.md; commit and push to claude/zhou-enlai.

Deliver in THIS chat: the built EPUB attached, AND the next kickoff pasted
verbatim in a fenced code block. Both, every batch.
```

## Status: what is DONE

- **Survey + B01 (ch00 Preface + ch01):** complete, voice gate approved; ch01 is
  the frozen register reference.
- **B02 (ch02 Section One + ch03 Chen Geng):** complete. All checks green.
- **B03 (ch04 Heroes of the Intelligence Front):** complete. All checks green.
- **B04 (ch05 Three Heroes of Longtan + ch06 Yang Dengying):** complete. ch05 =
  41 body paragraphs, 16 notes, 2 figures; ch06 = 40 body paragraphs, 7 notes,
  0 figures. All checks green. Full record in PROGRESS.md.
- **EPUB:** out/zhou-enlai.epub = 7 of 28 chapters (ch00-ch06), 116 notes, 96
  pagebreaks; qa_epub PASS, epubcheck 0/0.

## Tooling in place / do not revert

- data/ocr_fixes.json: crop-verified readings for ch00-ch06; replay with
  apply_fixes.py on any fresh regen. B04 added ch05 (28 rows) + ch06 (22 rows).
- scripts/recovery/ (tracked): b02_*, b03_*, b04_* strip/surgery scripts + the
  README documenting the per-batch assembly-seam recovery order. The b04_* pair
  is the current model (per-target heading guard; block-quote over-split welds).
  Do not delete.
- ocr_crop.py patches (folio_present, bare-digit strip) and check_content.py
  '_'-prefix skip: keep (from B01).
- data/noise.txt: keep extending, never prune. B04 added 正经八百, 瘪三, 30年代,
  胡百昌, 5万, 金钱万能, 万里.
- data/check_config.json: docs/sources for ch00-ch06; ADD ch07, ch08 next batch.
- data/pagemap/ch05.json, ch06.json: hand-regenerated for the post-surgery
  structure.
- Assembly uses the BLANK-LINE path; indents.py unreliable here.

## Renderings settled (glossary.json is the ledger; +37 rows in B04)

- Principals unchanged: 周恩来 Zhou Enlai, 陈赓 Chen Geng (alias 王庸 Wang Yong),
  顾顺章 Gu Shunzhang, 李强 Li Qiang.
- The "Three Heroes of Longtan" (龙潭三杰), settled and biographied in ch05:
  李克农 Li Kenong, 钱壮飞 Qian Zhuangfei, 胡底 Hu Di. 杨登瀛/鲍君甫 Yang Dengying /
  Bao Junfu (alias 刘君珊 Liu Junshan), the ch06 subject, settled.
- New recurring cast that RETURNS later (reuse unchanged): 徐恩曾 Xu Enzeng,
  陈立夫 Chen Lifu, 陈果夫 Chen Guofu, 张道藩 Zhang Daofan, 蔡孟坚 Cai Mengjian,
  连德生 Lian Desheng, 兰普逊 Lampson, 谭绍良 Tan Shaoliang, 安娥 An E, 刘鼎 Liu
  Ding (recurs in ch07 as intelligence deputy).
- Terms held: 龙潭三杰 = "Three Heroes of Longtan"; 田中奏折 = "Tanaka Memorial";
  上海——冒险家的乐园 = "Shanghai: The Paradise of Adventurers"; 中统 = "CC Clique /
  Central Bureau of Investigation and Statistics"; 东方大学 = "Communist University
  of the Toilers of the East"; 巡捕房 rendered as "police station(s)" / "the
  police" of the Concessions (per ch01-ch03).
- Everything else in glossary.json; feed decided renderings into authority.json at
  book's end.

## Voice sheets (carry-forward)

- **Mu Xin (author):** confident narrative-history voice, open partisan edge;
  heroes are heroes, 叛徒 traitors, the verdict goes in the note. He steps into the
  first person as an interviewer/witness (ch04); keep that register where it
  appears.
- **Zhou Enlai:** measured, analytic, unshowy; terse directives ("Bring it over
  to us" is the ch07s02 title). Recurs heavily in ch07.
- **Chen Geng:** quick, cool, wry; the operational hand behind Yang Dengying.
- **Memoir/testimony quotations** (阿英, 宋治家, 张振华, 李克农's exam account, 徐恩曾's
  memoir) are first-person; keep each plain and concrete, differentiated by
  detail, in quotation marks (no {v} vignette markers were used — prior batches
  render block quotes as plain quoted paragraphs). Verse (the Dong Biwu elegy)
  uses the {p} marker, one {p} line per source line (a couplet per line here).

## Where the story stands

The Central Special Section's intelligence arm is fully drawn: Chen Geng's branch
(ch03), its heroes (ch04), the Three Heroes of Longtan planted inside Xu Enzeng's
service (ch05), and Yang Dengying, the first counter-espionage asset "pulled out"
of the enemy camp (ch06). ch07 goes deeper into that penetration (the codebook
theft, Zhou Enlai's "bring it over to us"); ch08 turns to Zhao Weigang inside the
Fengtian military establishment and the warning before the Mukden Incident.

## Exact next-batch scope

- **B05** = ch07 (PDF 154-172, printed 110-128, ch07s01-05) + ch08 (PDF 173-197,
  printed 129-153, ch08s01-06). Then B06 = ch09 + ch10 per out/SURVEY.md.

## Open traps / environment state

- Body offset constant 44; folio-verify each opener.
- ASSEMBLY SEAMS are the biggest time-sink every batch: page-seam force-breaks,
  dropped in-page blanks, and block quotes over-split by blank-per-line spacing.
  EYEBALL every content page; verify per-section EN/ZH counts.
- Heading normalization needs a PER-TARGET length guard, not a global maxlen.
- Re-running surgery is NOT idempotent; re-assemble first.
- apparatus_merge adds glossary rows FLAT; add rows nested directly instead.
- After a surgery split, check the split marker does not strand an entity name on
  the wrong side of a paragraph boundary (qc_entities will flag it).
- ocr_dual.py is slow; run it in the background.
- OMP_THREAD_LIMIT=1 for tesseract; kill the process GROUP; pgrep -c tesseract
  must read 0 after a run. PaddleOCR absent; use ocr_dual.py.
- epubcheck at /tmp/epubcheck-5.1.0 (re-fetch via setup.sh in a fresh container).
- Pre-existing failing regression test ("hook stands down on template stub");
  template maintenance, does not affect real batches.
