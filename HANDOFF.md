# HANDOFF — Zhou Enlai: Commander of the Hidden Front

Fresh-session handoff. The paste-ready kickoff is first; everything below it is
the state a new session needs. Batches 1-5 are COMPLETE (ch00-ch08). Next is
B06 = ch09 + ch10.

## Message to paste into the next chat

```
Zhou Enlai B06

Read CLAUDE.md, then HANDOFF.md, then STYLE.md, then book.json. Do Batch 6 =
ch09 (行动科和"红队" / The Action Section and the "Red Squad", PDF 198-217,
printed 154-173; four sections ch09s01-04: 顾顺章"魔术大师化广奇" / 令敌胆丧的
"打狗队" / 李一氓笔下的"苏维埃会议" / 镇压叛徒绝不手软) AND ch10 (红队利剑出鞘 /
The Red Squad Draws Its Sword, PDF 218-230, printed 174-186; four sections
ch10s01-04: 英国巡捕冲进罗亦农屋门 / 查找出卖罗亦农的叛徒 / "残躯何足惜,大敌正当前"
/ 叛徒在鞭炮声中毙命), end to end per the CLAUDE.md pipeline. Work on branch
claude/zhou-enlai; expect a stray per-task branch and consolidate onto it
(CLAUDE.md rule 2 — checkout claude/zhou-enlai, reset --hard to origin, do the
work, delete the stray local+remote).

BEFORE translating, read the final two paragraphs of ch08 in out/ch08_reading.md
(Zhao Weigang's memoir close — the Japanese-penetration reflection and his
departure to the USSR) so the voice carries over. NOTE ch09/ch10 return to
Mu Xin's own narrative-history voice (the Red Squad, Gu Shunzhang the magician,
the Luo Yinong betrayal), NOT a reproduced first-person memoir like ch08. ch01
is the FROZEN reference; run check_register.py --ref out/ch01_reading.md on every
unit.

Pipeline notes specific to THIS book (all proven in B01-B05, do not rediscover):
- Body offset is a CONSTANT 44: printed = PDF - 44. Folio-verify each opener by
  eye anyway. ch09 opens PDF 198 = printed 154; ch10 opens PDF 218 = printed 174.
- OCR: ocr_crop.py FIRST LAST --left 0.11 --right 0.90 --top 0.135 --bottom 0.95
  --lang chi_sim --psm 6 --running-head "隐蔽战线统帅周恩来". Verify pgrep -c
  tesseract is 0 after. Second read via ocr_dual.py (slow; run in background).
- ASSEMBLY IS THE HARD PART, and the disease MUTATES per batch. The blank-line
  path FORCE-BREAKS at every page seam AND, on some pages, the OCR emits NO
  paragraph blank lines so distinct source paragraphs get WELDED (B05's finding:
  section-opener pages and indent-only runs are the worst). The sentence-end
  check does NOT catch under-splits (both halves end in 。). So: EYEBALL EVERY
  CONTENT PAGE for paragraph indents and reconcile against the assembled counts;
  do not trust the counts alone. Replay the recovery pattern (scripts/recovery/
  README.md; b05_*.py are the latest, most complete models):
  (1) bXX_strip_furniture.py: normalize garbled chapter/section headings to the
  exact structure.json titles with a PER-TARGET length guard (len(good)+4);
  handle multi-line wrapped headings (merge + delete the orphan tail line);
  truncate every author-footnote block at a footnote-ONLY marker (verify the
  exact OCR bytes first, they garble); blank/strip any photos (B05 had none).
  (2) Add structure.json rows for the chapter + its sections BEFORE assemble
  (pull the exact title bytes from book.json).
  (3) rm -rf data/indent; assemble.py <id> FIRST LAST --offset 44 (BOTH units
  before surgery — surgery is NOT idempotent).
  (4) bXX_surgery.py: WELDS FIRST (reunite page-seam breaks), THEN SPLITS (break
  the OCR-welded paragraphs), THEN fixups — a split target can span a weld.
  EYEBALL every content page; verify per-SECTION EN/ZH counts, not just totals.
  Set-off block quotes are the trap in BOTH directions (B04 over-split, B05
  under-split); the Red-Squad chapters have execution scenes and quoted
  documents/memoirs (李一氓's account) — watch them.
  (5) apply_fixes.py <id> AFTER surgery (surgery markers use raw OCR bytes).
  (6) b05_pagemap.py regenerates data/pagemap/<id>.json for the post-surgery
  structure (matches each page's first BODY line, with ocr_fixes applied, into
  the final ZH; monotonic; skips heading-opener lines). Reuse it — pass the new
  unit ids/ranges.
- Crop-verify every name/number/alias/date BEFORE writing; record fixes in
  data/ocr_fixes.json via apply_fixes.py. ch09/ch10 subjects: 顾顺章 the stage
  magician "化广奇" and the Action Section / 红队 ("打狗队"); 李一氓's account of
  the "Soviet Congress"; 罗亦农 (Luo Yinong) betrayed by a traitor and the Red
  Squad's reprisal. Watch dropped digits in dates/unit numbers, 巡捕房/租界
  terms, and any 夹带的英文.
- Checks: verify_unit reads unit ids (parity + check_numbers with data/noise.txt
  + anchors); check_numbers/qc_entities read the BILINGUAL path; check_align
  reads a unit id; check_content --config data/check_config.json (ADD ch09, ch10
  to it). check_structure --pairs SRC TGT for one unit.
- Glossary: add rows DIRECTLY nested into people/organizations/places/works/terms
  (apparatus_merge adds them FLAT and the builder crashes). Decide the prose
  rendering as the glossary `en` (e.g. 中统="Zhongtong"), keep the formal
  expansion in the NOTE — else check_content flags every paragraph. 罗亦农 Luo
  Yinong and 李一氓 Li Yimang are already in glossary (reuse).
- Footnotes at reader-model density with fact-check verdicts IN the note; never
  source LLM content (WebSearch Wikipedia/Baidu/academic). Author footnotes are
  reproduced as translator notes tagged "Author's note." at the ① anchor. Note at
  FIRST appearance book-wide (grep notes.json and earlier reading files first);
  keep a "NOT re-noted" list in PROGRESS. Note anchors must be verbatim ASCII
  substrings of the reading .md (avoid curly-quote/em-dash spans; note BODIES use
  numeric char refs).
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
- **B05 (ch07 Deep into the Tiger's Den + ch08 Zhao Weigang):** complete. ch07 =
  54 body paragraphs, 14 notes, 0 figures; ch08 = 54 body paragraphs (s02-s06 are
  Zhao's reproduced 1983 memoir, first-person), 13 notes, 0 figures. All checks
  green. Full record in PROGRESS.md.
- **EPUB:** out/zhou-enlai.epub = 9 of 28 chapters (ch00-ch08), 143 notes, 136
  pagebreaks; qa_epub PASS, epubcheck 0/0.

## Tooling in place / do not revert

- data/ocr_fixes.json: crop-verified readings for ch00-ch08; replay with
  apply_fixes.py on any fresh regen. B05 added ch07 (41 rows) + ch08 (45 rows).
- scripts/recovery/ (tracked): b02_*, b03_*, b04_*, **b05_*** strip/surgery/
  pagemap scripts + the README. The b05_* set is the current model: WELDS-then-
  SPLITS ordering in surgery, per-target heading guard, multi-line heading merge,
  and b05_pagemap.py (post-surgery pagemap regen). Do not delete.
- ocr_crop.py patches (folio_present, bare-digit strip) and check_content.py
  '_'-prefix skip: keep (from B01).
- data/noise.txt: keep extending, never prune. B05 added 徐新六, 三明, 三洋泾桥,
  派头十足, 40年代, 20万, 千叶, 九一八, 70年代, 七七八八, 四平, 万岁.
- data/check_config.json: docs/sources for ch00-ch08; ADD ch09, ch10 next batch.
- data/pagemap/ch07.json, ch08.json: regenerated post-surgery (b05_pagemap.py).
- Assembly uses the BLANK-LINE path; indents.py unreliable here (margin
  detection returned -1.0 on the B05 pages — do not rely on it).

## Renderings settled (glossary.json is the ledger)

- Principals now include 赵唯刚 Zhao Weigang (cast_order 6) and 蔡伯祥 Cai
  Boxiang (cast_order 7), alongside 周恩来, 陈赓, 顾顺章, 李强.
- ch07 recurring cast (reuse unchanged): 徐恩曾 Xu Enzeng, 陈立夫/陈果夫 Chen
  Lifu/Chen Guofu, 张道藩 Zhang Daofan, 钱壮飞 Qian Zhuangfei, 李克农 Li Kenong,
  胡底 Hu Di, 杨登瀛 Yang Dengying, 邹韬奋 Zou Taofen, 任卓宣/叶青 Ren Zhuoxuan,
  戴笠 Dai Li, 费侠 Fei Xia, 王素卿 Wang Suqing, 刘伯承 Liu Bocheng.
- Terms decided: 中统 = "Zhongtong", 军统 = "Juntong", 党务调查科 = "Investigation
  Section" (formal expansions in the notes, NOT the prose — keeps check_content
  clean). 龙潭三杰 = "Three Heroes of Longtan"; 巡捕房 = "concession police"; 租界
  = "the Concessions".
- ch08 memoir shorthand resolved: 老蔡 = Cai Boxiang (Old Cai), 老廖 = 廖如愿
  Liao Ruyuan (Old Liao). Places: 大阪 Osaka, 千叶 Chiba, 奉天/沈阳 Fengtian/
  Shenyang, 齐齐哈尔 Qiqihar, 伯力 Khabarovsk.
- Everything else in glossary.json; feed decided renderings into authority.json at
  book's end.

## Voice sheets (carry-forward)

- **Mu Xin (author):** confident narrative-history voice, open partisan edge;
  heroes are heroes, 叛徒 traitors, the verdict goes in the note. He steps into
  the first person as interviewer/witness (ch04, ch08 frame); keep that register.
- **Zhou Enlai:** measured, analytic, unshowy; terse directives ("Bring it over
  to us", ch07). **Chen Geng:** quick, cool, wry, the operational hand.
- **Reproduced first-person memoirs** (Zhao Weigang, ch08 s02-s06; 宋治家/宋季仁,
  张振华, 李克农, 徐恩曾 quotes in ch07): keep plain and concrete, colloquial,
  differentiated by detail. Zhao's memoir is casual and run-on — do NOT formalize
  it; his contractions run high vs the frozen reference and that is correct.
  Introduce a reproduced memoir with a note; no {v} vignette markers (prior
  batches render block quotes as plain paragraphs; extended narrative quotes,
  like the Li Kenong biographer's account in ch07 s04, are set off by a colon +
  attribution and rendered as plain paragraphs, no outer quote marks).
- **B06 is back in Mu Xin's narrative voice** (the Red Squad, executions, the Luo
  Yinong betrayal) — full narrative rules, keep the pace, lethal verbs for lethal
  acts (制裁/除掉 = eliminate/kill, 处决 = execute).

## Where the story stands

The penetration of Xu Enzeng's service is fully drawn: the codebook theft and
Zhou Enlai's "bring it over" (ch07), and Zhao Weigang's long watch inside the
Fengtian military establishment, warning a month before the Mukden Incident
(ch08). ch09-ch10 turn to the OTHER arm of the Special Section: the Action
Section and its Red Squad — Gu Shunzhang the stage magician who built it, the
"Dog-Beating Squad," and the reprisals against the traitors who sold out Luo
Yinong.

## Exact next-batch scope

- **B06** = ch09 (PDF 198-217, printed 154-173, ch09s01-04) + ch10 (PDF 218-230,
  printed 174-186, ch10s01-04). Then B07 = ch11 + ch12 per out/SURVEY.md
  (the survey's own batch numbering is one behind, since B05 combined ch07+ch08).

## Open traps / environment state

- Body offset constant 44; folio-verify each opener.
- ASSEMBLY SEAMS mutate every batch: page-seam force-breaks AND OCR-dropped
  in-page blanks (under-splits, esp. on section-opener pages) AND block-quote
  over/under-splits. EYEBALL every content page; verify per-SECTION counts.
- Surgery is WELDS-then-SPLITS-then-fixups, and NOT idempotent (re-assemble both
  units first).
- Heading normalization needs a PER-TARGET length guard; handle multi-line
  wrapped headings.
- apparatus_merge adds glossary rows FLAT; add rows nested directly instead.
  Decide the PROSE form as the glossary `en`, formal expansion in the note.
- Note anchors must be verbatim ASCII substrings of the reading .md.
- ocr_dual.py is slow; run in the background. OMP_THREAD_LIMIT=1 for tesseract;
  kill the process GROUP; pgrep -c tesseract must read 0 after a run.
- epubcheck at /tmp/epubcheck-5.1.0 (re-fetch via setup.sh in a fresh container).
- Pre-existing failing regression test ("hook stands down on template stub");
  template maintenance, does not affect real batches.
