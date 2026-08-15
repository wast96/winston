# HANDOFF — Zhou Enlai: Commander of the Hidden Front

Fresh-session handoff. The paste-ready kickoff is first; everything below it is
the state a new session needs. Batches 1 and 2 are COMPLETE (ch00-ch03). Next is
B03 = ch04.

## Message to paste into the next chat

```
Zhou Enlai B03

Read CLAUDE.md, then HANDOFF.md, then STYLE.md, then book.json. Do Batch 3 =
ch04 (情报战线的英豪 / Heroes of the Intelligence Front, PDF 95-122, printed
51-78; four sections ch04s01 刘鼎 / ch04s02 柯麟 / ch04s03 陈养山 / ch04s04 陈寿昌),
end to end per the CLAUDE.md pipeline. Work on branch claude/zhou-enlai; expect a
stray per-task branch and consolidate onto it (CLAUDE.md rule 2).

BEFORE translating, read the final two paragraphs of ch03 in out/ch03_reading.md.
ch01 is the FROZEN reference; run check_register.py --ref out/ch01_reading.md on
every unit.

Pipeline notes specific to THIS book (all proven in B01-B02, do not rediscover):
- Body offset is a CONSTANT 44: printed = PDF - 44. Read the folio at each opener
  anyway. ch04 opens PDF 95 = printed 51 (survey inference; folio-verify).
- OCR: ocr_crop.py FIRST LAST --left 0.11 --right 0.90 --top 0.135 --bottom 0.95
  --lang chi_sim --psm 6 --running-head "隐蔽战线统帅周恩来". Verify pgrep -c
  tesseract is 0 after. Second read via ocr_dual.py.
- ASSEMBLY IS THE HARD PART ON THIS BOOK. indents.py is unreliable; use the
  blank-line path, but it DROPS/WELDS content at every author-footnote and photo
  seam. Follow scripts/recovery/README.md exactly: (1) STRIP author-footnote
  blocks and blank photo pages from data/txt BEFORE assemble (a page-bottom
  footnote silently eats the spanning paragraph's continuation; three paragraphs
  were lost this way in B02). Use a footnote-ONLY truncation marker (a body word
  can collide, e.g. 会审公堂 in B02). (2) Photo pages may be photo+caption only OR
  a small photo with body text below; strip only the photo+caption in the latter.
  (3) After assemble, de-weld blank-less pages and fix page-seam splits by hand
  against the scan; restore any OCR-clipped short lines (B02 lost "生涯。" and
  "客车。"). Add structure.json rows for ch04 + its sections; garbled section
  headings will not auto-detect, so set them as ### by hand.
- Crop-verify every name/number/alias/date BEFORE writing; record fixes in
  data/ocr_fixes.json via apply_fixes.py. ch04's subjects are the intelligence
  workers already met in ch03's roster: 刘鼎 (Liu Ding, weapons expert), 柯麟 (Ke
  Lin, physician), 陈养山 (Chen Yangshan), 陈寿昌 (Chen Shouchang). 陈X garbles are
  legion (陈赓 alone had ~15); do NOT blanket-replace 陈 (陈养山/陈独秀/陈炯明/陈寿昌
  are distinct). Watch dropped digits in dates ("X月" losing a leading 1).
- Checks: verify_unit per unit; check_align; check_content --config
  data/check_config.json (add ch04 to it); check_numbers via verify_unit with
  --noise data/noise.txt; qc_entities on the bilinguals; apparatus via
  apparatus_merge.py (check_apparatus clean); check_register --ref.
- Footnotes at reader-model density with fact-check verdicts IN the note; never
  source LLM content. Note at FIRST appearance book-wide (grep notes.json and the
  earlier reading files first); keep a "NOT re-noted" list in PROGRESS.
- Cite the book's PRINTED FOLIO in notes, never the PDF page.
- Build the cumulative EPUB, qa_epub green, epubcheck (/tmp/epubcheck-5.1.0).
- Update PROGRESS.md and HANDOFF.md; commit and push to claude/zhou-enlai.

Deliver in THIS chat: the built EPUB attached, AND the next kickoff pasted
verbatim in a fenced code block. Both, every batch.
```

## Status: what is DONE

- **Survey + B01 (ch00 Preface + ch01):** complete, voice gate approved; ch01 is
  the frozen register reference.
- **B02 (ch02 Section One + ch03 Chen Geng):** complete. 40 + 37 body paragraphs,
  all checks green, 29 notes, 3 figures, EPUB rebuilt. Full record in PROGRESS.md.
- **EPUB:** out/zhou-enlai.epub = 4 of 28 chapters, 69 notes, 41 pagebreaks;
  qa_epub PASS, epubcheck 0/0.

## Tooling in place / do not revert

- data/ocr_fixes.json: now ~90 crop-verified readings (ch00-ch03); replay with
  apply_fixes.py on any fresh regen.
- **scripts/recovery/** (NEW, tracked): b02_strip_furniture.py, b02_surgery.py,
  README.md documenting the assembly-seam recovery order. The book's OCR seams
  drop content; this is the replayable procedure. Do not delete.
- ocr_crop.py patches (folio_present, bare-digit strip) and check_content.py
  '_'-prefix skip: keep (from B01).
- data/noise.txt: B02 added place/idiom/name numerals — 四川, 六合, 三民, 红十字,
  万不得已, 阿四, 五卅, 三七二十一, 千难万险, 千辛万苦, 干辛万苦, 立三. Extend, do not prune.
- data/check_config.json: docs/sources for ch00-ch03; ADD ch04 next batch.
- data/pagemap/ch02.json, ch03.json: REGENERATED to match the post-surgery
  paragraph structure (the assemble auto-output was stale after the seam repairs;
  a fresh regen must recompute them against the final structure, not trust
  assemble's first pass). Monotonic and spot-checked.
- Assembly uses the BLANK-LINE path; indents.py unreliable here.

## Renderings settled (glossary.json is the ledger; +83 rows in B02)

- Principals (unchanged): 周恩来 Zhou Enlai, 陈赓 Chen Geng (alias 王庸 Wang Yong,
  别号 庶康 Shukang), 顾顺章 Gu Shunzhang (alias 化广奇), 李强 Li Qiang (alias 曾培鸿).
- Section One (ch02): 洪扬生 Hong Yangsheng (later 洪松涛), 熊瑾玎 Xiong Jinding +
  朱端绥 Zhu Duansui, 李维汉 Li Weihan (alias 罗迈 Luo Mai).
- Intelligence branch (ch03, recurs in ch04): 李克农 Li Kenong, 钱壮飞 Qian
  Zhuangfei, 胡底 Hu Di, 陈寿昌 Chen Shouchang, 陈养山 Chen Yangshan, 刘鼎 Liu Ding,
  柯麟 Ke Lin, 欧阳新 Ouyang Xin (alias 刘大汉 "Big Hunk").
- Chen Geng's circle: 王根英 Wang Genying (wife), 陈知非 Chen Zhifei (son), 卢冬生 Lu
  Dongsheng, 周逸群 Zhou Yiqun, 牛惠霖 Niu Huilin, 张克侠 Zhang Kexia, 钱大钧 Qian
  Dajun, 陆连奎 Lu Liankui.
- Decided terms: 黄埔军校 = "Whampoa"; 会审公堂 = "Mixed Court" (author's gloss
  footnoted); 中国救济总会 = China Relief Society; 国际济难会 = International Red Aid.
- Everything else in glossary.json; feed decided renderings into authority.json at
  book's end.

## Voice sheets (carry-forward)

- **Mu Xin (author):** confident narrative-history voice, open partisan edge.
  Heroes are heroes, 叛徒 traitors. Keep the heat where he runs hot (the Chen Geng
  chase set-pieces, Chiang's melodrama played for irony); verdicts go in the note.
- **Chen Geng (in dialogue, ch03):** quick, cool, wry under pressure; coaxes and
  jokes his way out of danger (the train scene with Qian Dajun, the roadside
  banter with Lu Dongsheng). Colloquial and confident, never grandiloquent. He
  recurs across the book; keep this voice.
- **Li Qiang (own testimony):** plain, colloquial first-person reminiscence, fond
  of concrete asides. (Established B01; recurs in ch02's staff list and ch17.)
- **Zhou Enlai:** measured, analytic, unshowy; terse directives ("Bring it over
  to us"). Fill in as he speaks directly in later chapters.
- Hong Yangsheng, Liu Shuqin, Li Weihan, Zhang Kexia speak in quoted recollection:
  each plain and first-person, differentiated by their concrete detail.

## Where the story stands

Section One (the "steward" branch: secret offices, meeting venues, rescues,
martyrs' burials) and Section Two (intelligence, under Chen Geng as "Wang Yong")
are both established. Chen Geng's legend is told through B01's Nanchang wound and
B02's Hong Kong ordeal, the Niu Huilin hospital, the "ever-present Mr. Wang," and
the Qian Dajun train escape. ch04 turns to four more intelligence-front heroes.

## Exact next-batch scope

- **B03** = ch04 (情报战线的英豪, PDF 95-122, printed 51-78; ch04s01-04). Then B04
  = ch05 + ch06 per out/SURVEY.md.

## Open traps / environment state

- Body offset constant 44; folio-verify each opener.
- ASSEMBLY SEAMS drop/weld content (see scripts/recovery/README.md); this is the
  single biggest time-sink and every batch hits it.
- Embedded photos and the book's own author-footnotes recur; handle per recovery.
- OMP_THREAD_LIMIT=1 for tesseract; kill the process GROUP; pgrep -c tesseract
  must read 0 after a run. PaddleOCR absent; use ocr_dual.py.
- epubcheck at /tmp/epubcheck-5.1.0 (may need re-fetch via setup.sh in a fresh
  container).
- Pre-existing failing regression test ("hook stands down on template stub");
  template maintenance, does not affect real batches.
