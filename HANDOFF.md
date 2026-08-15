# HANDOFF — Zhou Enlai: Commander of the Hidden Front

Fresh-session handoff. The paste-ready kickoff is first; everything below it is
the state a new session needs. Batches 1-3 are COMPLETE (ch00-ch04). Next is
B04 = ch05 + ch06.

## Message to paste into the next chat

```
Zhou Enlai B04

Read CLAUDE.md, then HANDOFF.md, then STYLE.md, then book.json. Do Batch 4 =
ch05 (“龙潭三杰” / The “Three Heroes of Longtan”, PDF 123-139, printed 79-95;
three sections ch05s01 李克农 / ch05s02 钱壮飞 / ch05s03 胡底) AND ch06 (第一个反
间谍关系——杨登瀛 / The First Counter-Espionage Asset — Yang Dengying, PDF 140-153,
printed 96-109; five sections ch06s01-05), end to end per the CLAUDE.md pipeline.
Work on branch claude/zhou-enlai; expect a stray per-task branch and consolidate
onto it (CLAUDE.md rule 2 — the recipe: checkout claude/zhou-enlai, reset --hard
to origin, do the work, delete the stray local+remote).

BEFORE translating, read the final two paragraphs of ch04 in out/ch04_reading.md
(Chen Shouchang’s death) so the voice carries over. ch01 is the FROZEN reference;
run check_register.py --ref out/ch01_reading.md on every unit.

Pipeline notes specific to THIS book (all proven in B01-B03, do not rediscover):
- Body offset is a CONSTANT 44: printed = PDF - 44. Folio-verify each opener by
  eye anyway. ch05 opens PDF 123 = printed 79; ch06 opens PDF 140 = printed 96.
- OCR: ocr_crop.py FIRST LAST --left 0.11 --right 0.90 --top 0.135 --bottom 0.95
  --lang chi_sim --psm 6 --running-head "隐蔽战线统帅周恩来". Verify pgrep -c
  tesseract is 0 after. Second read via ocr_dual.py. (Recto running head is the
  chapter title, stripped by the top crop; verso is the book title.)
- ASSEMBLY IS THE HARD PART. indents.py is unreliable; use the blank-line path,
  but it FORCE-BREAKS at every page seam and occasionally drops an in-page blank,
  and it DROPS/WELDS content at author-footnote and photo seams. Follow
  scripts/recovery/README.md and REPLAY the recovery pattern:
  (1) Write a bXX_strip_furniture.py: normalize garbled section headings to the
  exact structure.json titles (so assemble auto-emits ###); truncate every
  author-footnote block at a footnote-ONLY substring marker; blank full-page
  photos; strip top/bottom body-page photos with keep-from / keep-through markers.
  (2) Add structure.json rows for the chapter + its sections BEFORE assemble.
  (3) assemble.py <id> FIRST LAST --offset 44.
  (4) Write a bXX_surgery.py: EYEBALL EVERY CONTENT PAGE for paragraph indents,
  then apply splits (one line carrying >1 source paragraph) and backward-welds
  (page-seam splits + dropped in-page blanks). The decisive signal is the printed
  INDENT read off the scan, not punctuation. Verify per-section paragraph counts
  match EN vs ZH before trusting parity (a compensating +1/-1 hides in the total).
  (5) apply_fixes.py <id> AFTER surgery (surgery markers use the raw OCR bytes).
  (6) Hand-regenerate data/pagemap/<id>.json for the post-surgery structure.
- Crop-verify every name/number/alias/date BEFORE writing; record fixes in
  data/ocr_fixes.json via apply_fixes.py. ch05’s subjects are the “Three Heroes
  of Longtan” 李克农 (Li Kenong), 钱壮飞 (Qian Zhuangfei), 胡底 (Hu Di), planted in
  Xu Enzeng’s CC-Clique secret service; the Gu Shunzhang defection (April 1931)
  hinges on their warning. ch06’s subject is 杨登瀛 / 鲍君甫 (Yang Dengying / Bao
  Junfu), the “Japan hand,” the first counter-espionage asset (already recruited
  in ch04 by Chen Yangshan — cross-reference, do not re-note the basics). Watch
  夹带的英文 (兰普逊/Lampson in ch06s02) and dropped digits in dates.
- Checks: verify_unit per unit; check_align; check_content --config
  data/check_config.json (ADD ch05, ch06 to it); qc_entities on the bilinguals;
  apparatus via apparatus_merge.py (check_apparatus clean); check_register --ref.
  After apparatus_merge, RE-NEST new glossary rows into the people/organizations/
  places/works/terms sub-dicts (the merge adds them flat and the builder crashes
  on a top-level string).
- Footnotes at reader-model density with fact-check verdicts IN the note; never
  source LLM content. Note at FIRST appearance book-wide (grep notes.json and the
  earlier reading files first); keep a “NOT re-noted” list in PROGRESS.
- Cite the book’s PRINTED FOLIO in notes, never the PDF page.
- Build the cumulative EPUB, qa_epub green, epubcheck (/tmp/epubcheck-5.1.0).
- Update PROGRESS.md and HANDOFF.md; commit and push to claude/zhou-enlai.

Deliver in THIS chat: the built EPUB attached, AND the next kickoff pasted
verbatim in a fenced code block. Both, every batch.
```

## Status: what is DONE

- **Survey + B01 (ch00 Preface + ch01):** complete, voice gate approved; ch01 is
  the frozen register reference.
- **B02 (ch02 Section One + ch03 Chen Geng):** complete. All checks green.
- **B03 (ch04 Heroes of the Intelligence Front):** complete. 62 body paragraphs,
  24 notes, 3 figures, all checks green. Full record in PROGRESS.md.
- **EPUB:** out/zhou-enlai.epub = 5 of 28 chapters, 93 notes, 68 pagebreaks;
  qa_epub PASS, epubcheck 0/0.

## Tooling in place / do not revert

- data/ocr_fixes.json: ~180 crop-verified readings (ch00-ch04); replay with
  apply_fixes.py on any fresh regen. ch04 = 86 rows.
- **scripts/recovery/** (tracked): b02_* and b03_* strip/surgery scripts, plus
  README.md documenting the per-batch assembly-seam recovery order. The book’s
  OCR seams drop/weld content; this is the replayable procedure. Do not delete.
- ocr_crop.py patches (folio_present, bare-digit strip) and check_content.py
  '_'-prefix skip: keep (from B01).
- data/noise.txt: keep extending, never prune. B03 added 第二天/第二年, 二十多万,
  10万大洋/30万, 曾三, 万载, 老百姓.
- data/check_config.json: docs/sources for ch00-ch04; ADD ch05, ch06 next batch.
- data/pagemap/ch04.json: hand-regenerated for the 62-para post-surgery structure.
- Assembly uses the BLANK-LINE path; indents.py unreliable here.

## Renderings settled (glossary.json is the ledger; +85 rows in B03, 177 total)

- Principals (unchanged): 周恩来 Zhou Enlai, 陈赓 Chen Geng (alias 王庸 Wang Yong),
  顾顺章 Gu Shunzhang, 李强 Li Qiang (alias 曾培鸿).
- ch04 subjects (recur later): 刘鼎 Liu Ding (orig. 阚思俊 Kan Sijun), 柯麟 Ke Lin,
  陈养山 Chen Yangshan (orig. 程仰山 Cheng Yangshan, alias 老王 “Old Wang”), 陈寿昌
  Chen Shouchang. Also settled: 贺诚 He Cheng, 周越华 Zhou Yuehua, 吴先清 Wu Xianqing,
  潘汉年 Pan Hannian, 杨登瀛/鲍君甫 Yang Dengying / Bao Junfu (the ch06 subject),
  杨献珍 Yang Xianzhen, 佐野学 Sano Manabu, 罗明 Luo Ming, 叶挺 Ye Ting, 张云逸 Zhang
  Yunyi, 李少石 Li Shaoshi.
- ch05 cast, ALREADY in glossary from ch03/ch04: 李克农 Li Kenong, 钱壮飞 Qian
  Zhuangfei, 胡底 Hu Di. ch06 subject 杨登瀛 in glossary. Reuse unchanged.
- Decided terms to hold: 北京大学 = “Beijing University” (shelf ledger, NOT
  “Peking”); 黄埔军校 = “Whampoa”; 中统 = “CC Clique / Central Bureau of
  Investigation and Statistics”; 东方大学 = “Communist University of the Toilers of
  the East”; 达生医院 Dasheng Hospital; 镜湖医院 Kiang Wu Hospital; 汇丰银行
  Hongkong and Shanghai Bank; 新四军 New Fourth Army.
- Everything else in glossary.json; feed decided renderings into authority.json at
  book’s end.

## Voice sheets (carry-forward)

- **Mu Xin (author):** confident narrative-history voice, open partisan edge.
  Heroes are heroes, 叛徒 traitors; the verdict goes in the note, the voice stays.
  He steps into the FIRST PERSON at the end of ch04 (“Back in the 1960s... I had
  interviewed Comrade Chen Yangshan”) — keep that authorial-witness register, and
  footnote his identity (done for ch04).
- **Chen Geng (in dialogue):** quick, cool, wry under pressure. Recurs.
- **Zhou Enlai:** measured, analytic, unshowy; terse directives (“Bring it over
  to us”). In ch04 he briefs He Cheng (“become the Party’s eyes and ears, its
  nerves and its bloodstream”) — grave, plain, with a dry closing warmth.
- **Li Qiang (own testimony):** plain, colloquial first-person reminiscence.
- Memoir quotations (周越华 on the Dasheng Hospital; 陈养山 on recruiting Bao Junfu)
  are quoted first-person: keep each plain and concrete, differentiated by detail.
- ch05: 李克农’s reported line “I am the Party Central’s bodyguard” sets his voice
  (wry, self-deprecating). 钱壮飞 is the legendary hero; 胡底 “the youngest and most
  gifted.” Build their sheets as they speak.

## Where the story stands

The intelligence branch under Chen Geng (“Wang Yong”) is established (ch03), and
ch04 has told four of its heroes: Liu Ding the weapons expert, Ke Lin the
physician-agent (Dasheng Hospital, then two decades undercover in Macau), Chen
Yangshan the “lucky general” (who first recruited Yang Dengying and sheltered He
Long), and Chen Shouchang the radio/intelligence worker who fell in battle in
1934. ch05 turns to the most famous agents of all, the “Three Heroes of Longtan”
planted inside Xu Enzeng’s secret service, whose warning would avert catastrophe
when Gu Shunzhang defected; ch06 tells the fuller story of Yang Dengying, the
first counter-espionage asset, met in ch04.

## Exact next-batch scope

- **B04** = ch05 (情报 PDF 123-139, printed 79-95, ch05s01-03) + ch06 (PDF
  140-153, printed 96-109, ch06s01-05). Then B05 = ch07 + ch08 per out/SURVEY.md.

## Open traps / environment state

- Body offset constant 44; folio-verify each opener.
- ASSEMBLY SEAMS force-break at every page and drop/weld at footnote+photo seams
  and dropped in-page blanks; EYEBALL every content page for indents and verify
  per-section EN/ZH paragraph counts (see scripts/recovery/README.md). This is the
  single biggest time-sink and every batch hits it.
- apparatus_merge.py adds glossary rows FLAT; re-nest into categories or the build
  crashes.
- OMP_THREAD_LIMIT=1 for tesseract; kill the process GROUP; pgrep -c tesseract
  must read 0 after a run. PaddleOCR absent; use ocr_dual.py.
- epubcheck at /tmp/epubcheck-5.1.0 (re-fetch via setup.sh in a fresh container).
- Pre-existing failing regression test ("hook stands down on template stub");
  template maintenance, does not affect real batches.
