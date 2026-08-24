# PROGRESS — Zhou Enlai: Commander of the Hidden Front (隐蔽战线统帅周恩来)

The running per-batch log. Write it as you go, not at the end. One section per
batch: what was translated (unit ids, PDF and printed ranges), which checks ran
and what they found, notes added (count and numbering), glossary rows added with
status, figures, and anything flagged for the read-through (uncertain readings,
contradictions with scholarship, choices you were unsure of).

## Setup (survey session, Step 0a/0b)

- **Source:** `source.pdf`, image-only scan, 582 PDF pages, no text layer, no
  bookmarks. 隐蔽战线统帅周恩来 by 穆欣 (Mu Xin), 中国青年出版社 (China Youth
  Press), Beijing, 1st ed. Jan 2002, ISBN 7-5006-4686-0. 377,000 hanzi;
  850×1168 1/32; 17.125 print sheets + 18 plate leaves. Xidian University
  library copy: red oval seal, barcode 11018166, minor handwriting on cover and
  verso (cosmetic; not on body text). CIP subject: 周恩来 生平事迹 1927–1931.
- **Script / orientation:** simplified Chinese, horizontal. OCR model `chi_sim`,
  `--psm 6`. `chi_sim` confirmed installed. Second read: `ocr_dual.py`
  (PaddleOCR not installed; tesseract psm-6/psm-4 + inverted-threshold
  substitute).
- **Page furniture:** running head is the book title centred at the top of body
  pages (verso and recto both show 隐蔽战线统帅周恩来 / the chapter title); folio
  in the bottom outer corner. Crop box NOT yet measured — first engineering task
  of Batch 1 (configure `ocr_crop.py`, validate by OCR that no running-head
  column bleeds into the text box).
- **Structure:** recovered from the printed 目录 (PDF 38–43), verified folio by
  folio against the scan. No numbered chapters: 25 titled chapters + 前言 +
  结束语 + 后记 (28 units, 92 sections). Full structure in `book.json`.
- **Offset:** body is a **constant** `printed = pdf − 43`. Verified at ch01
  (printed 1 = PDF 44), ch25 (printed 509 = PDF 552), 后记 (printed 535 = PDF
  578) and its end (printed 537 = PDF 580). Front matter runs its own
  sequences: 前言 printed 1 = PDF 35 (offset 34); plate folios 1–~32 = PDF
  3–34. `pdf_end` 580, `printed_end` 537.
- **Plates:** PDF 3–34, ~32 numbered plate folios (agent portraits, Zhou/Mao
  handwriting, a captioned 密信). Captions carry names that recur in the text —
  fold these into `figures.json` with real `alt` text as the relevant chapters
  are translated; cross-reference the footnotes.
- **Metadata (Step 0a):** written into `book.json` — title_en "Zhou Enlai:
  Commander of the Hidden Front", author "Mu Xin", publisher China Youth Press,
  series "Winston Translations" #10, subjects set, translator's note drafted.
  Names checked against `authority.json`: Zhou Enlai, Chen Geng, Gu Shunzhang,
  Chiang Kai-shek all agree with the shelf.
- **Skeleton build:** `build_reading_epub.py` → `out/zhou-enlai.epub` (0/28
  translated, full hyperlinked pending-aware TOC + real cover). `qa_epub.py`
  PASS (41 files, all links resolve). epubcheck 5.1.0: 0 errors / 0 warnings.
- **Survey:** `out/SURVEY.md` (characterization + full outline + 18 proposed
  batches at ~30 printed pp). Awaiting commissioner approval (Step 0b gate).

## Open items to resolve in Batch 1

- Measure and configure the OCR crop box; validate by OCR.
- Verify ch01's opener folio and the first section's folio against the scan
  before translating (offset re-check per chapter, though the body offset is
  expected constant).
- Establish the frozen voice reference at the Step 0c gate (first-chapter voice
  approval).

## Batches (proposed; see out/SURVEY.md — awaiting approval)

18 batches, ch00–ch27. B01 = 前言 + ch01. Final batch B18 = ch25 + 结束语 +
后记, kept light for back matter, cover finalisation, and whole-book
reconciliation.

## Batch 1 (B01): ch00 (前言) + ch01 (中央特科的诞生) — DONE, at the voice gate

Translated: **ch00** (Preface, PDF 36-38, printed 1-3, 6 paragraphs) and **ch01**
(The Birth of the Central Special Section, PDF 45-59, printed 1-15, 38 body
paragraphs in three sections). This is the first-chapter voice gate (Step 0c):
ch01 SETS the frozen reference voice. Presented in chat; awaiting approval.

### Offset correction (important)
- The survey's body offset was wrong by one. Read off the scan: TOC ends at
  **PDF 44** (folio 6); the body opens at **PDF 45** (folio 1). So the body
  offset is a **constant 44** (printed = pdf minus 44), not 43. Verified at
  ch01 opener (printed 1 = PDF 45), ch01s02 (printed 4 = PDF 48), ch01s03
  (printed 10 = PDF 54), and the ch01/ch02 boundary (ch02 opens PDF 60 =
  printed 16, folio read).
- The preface is NOT PDF 35 (that is plate folio 32); it is **PDF 36-38**
  (its own sequence, printed 1-3, offset 35).
- book.json corrected: every body pdf_page +1 (120 values), ch00 pdf 36,
  pdf_end 581. printed_page values were already right. Later openers past ch02
  are still the survey's inference and must be folio-verified per batch.

### Engineering (do not revert)
- **OCR crop measured and configured:** --left 0.11 --right 0.90 --top 0.135
  --bottom 0.95, --lang chi_sim --psm 6, --running-head "隐蔽战线统帅周恩来".
  Validated by OCR: no running-head column bleed.
- **ocr_crop.py patched:** added `folio_present()` (was MISSING; indents.py
  imported it and crashed) and extended `strip_folio` to drop bare-digit
  folios (this book folios in clean numerals, e.g. "14", "人4").
- **check_content.py patched:** `name_map` now skips '_'-prefixed meta keys
  (the glossary's '_about' string crashed it; the builder already skips them).
- **Paragraph assembly uses the BLANK-LINE path, not indents.** indents.py's
  per-line flags misalign here because it scans page furniture (running head +
  rule) and embedded photos that the cropped OCR excludes; so data/indent/ was
  deleted and assemble.py ran on tesseract's blank lines (reliable WITHIN a
  page on this scan). The blank-line path misses breaks only at page seams and
  at pages tesseract emitted no blanks for (p47,48,49,55,59); those were split
  by hand against the page images and are documented in data/ocr_fixes.json's
  companion note below. A fresh QC regen must redo this (data/zh is untracked).

### Source traps found
- The book has its OWN footnotes (author's source citations): one on printed
  p.2 (薛耕莘), one in the preface (《周恩来传》). Captured them, stripped from the
  body OCR, and reproduced both as footnotes tagged "Author's note."
- Two embedded photographs in ch01: printed p.4 (workers' pickets before HQ)
  and p.5 (pickets marching to a rally). find_figures.py caught both; cropped
  to data/figs/p0048-f1.png and p0049-f1.png, folded into figures.json with
  alt text and translator captions (source's own labels).
- OCR-era glitches fixed and logged in data/ocr_fixes.json (19 readings):
  numbers (28小时 read as 2小时; 500 as $S00; 60人 as 66人; 当时 as 2时; 5月 as
  S月; 老白脸 as 老百脸 injecting a phantom 100; 千方百计 as 干方百计) and names
  (张国焘 mangled 3 ways, 聂荣臻, 尹宽, 深水埗, 陈赓, 恽代英, 顾顺章, 向忠发, 蒋介石).

### Checks run — all green
- verify_unit ch00/ch01: parity 6/6 and 38/38, numbers 0 unresolved, anchors
  12 + 25 ok.
- check_align OK (median ratio 4.30 / 4.37 en per han, no pair strays 2.2x).
- check_content OK (66 glossary names, all name occurrences in the paired
  paragraph; fixed two spots where "the Party" replaced 中国共产党 and
  standardised "Comintern").
- qc_entities: 0 misses each.
- check_apparatus: 0 failures / 0 warnings.
- check_numbers noise added: 四一二/四一五/七一五 (event labels), 三军, 两党,
  李立三, 九江, 九龙.
- Build: 2/28 chapters, 37 notes, 17 pagebreaks. qa_epub PASS. epubcheck 5.1.0:
  0 errors / 0 warnings. check_register sets the ch01 baseline (em-dash 6.0/1k,
  rhythm CV 0.58, sentence median 23); future batches run
  `check_register.py --ref out/ch01_reading.md`.

### Notes: coverage and fact-check verdicts
- 12 notes in the preface, 25 in ch01. Fact-checked against Wikipedia
  ("Central Special Branch", "Xiang Zhongfa", "Gu Shunzhang"), Baidu Baike
  ("Cheng Ziqing"), and the received Sunzi text. Corroborated: the Nov 14 1928
  Special Committee (Xiang Zhongfa / Zhou / Gu), the First Congress details, the
  Nanchang Uprising, extraterritoriality, the section structure. Flagged as the
  author's own figure / uncorroborated in that precise form: the 2,100 killed
  in the Guangzhou "April 15" massacre; the identification of the 1921 intruder
  as Cheng Ziqing follows Chinese sources and is rare in Western scholarship.
- Tier deliberately left unfootnoted: minor persons fully covered by the
  glossary and Principal Characters page; routine place names.
- NOT re-noted (placed once, at first appearance): White Terror, the April 12
  coup, the Central Special Section, Gu Shunzhang, Xiang Zhongfa, the Comintern,
  the Sunzi (用间篇) — all noted in the preface; ch01 mentions carry no repeat.

### Calibrated ruling seeded (STYLE.md)
- 同志 ("comrade"): kept "Comrade" inside direct address / testimony (the Li
  Qiang quote) and dropped in plain narration; footnote convention deferred to
  commissioner taste at the gate.
- 巡捕房 decided as "concession police", 巡捕 as "constable" (glossary + note).

### Known pre-existing issue (not introduced here)
- tests/run_tests.py has ONE failing case from before this batch: "hook stands
  down on template stub" (kickoff_guard placeholder detection). It does not
  affect real batches (the "compliant wrap-up" case passes). Left for the
  commissioner; fixing it is template maintenance, out of scope for a
  translation batch.

## B01 voice-gate revision (commissioner feedback, round 1)

Commissioner read the notes and five sample sentences at the gate and flagged
recurring prose faults. Recorded them as four CLASSES in STYLE.md's Calibrated
rulings (lead with the thrust / no fronted-infinitive subjects; collapse doubled
并列 pairs and never repeat a word for the source's parallelism; break stacked
run-ons at their beats; Sun Tzu + Art of War naming, recast the chapter-citation
intro). Fixed the five flagged sentences and swept the rest of the preface and
ch01 for the same classes (the White Terror opener, the "everywhere...everywhere"
sentence, the Chen Duxiu and The Guide run-ons, two more fronted-infinitive
subjects, the "to effect" doubled adverb, the closing "once heard"). Added 孙子 =
Sun Tzu and 孙子兵法 = Art of War to glossary; updated the two Sun Tzu note anchors
and bodies. All checks still green; qa_epub PASS; epubcheck 0/0. Content is
otherwise unchanged (a style pass, not a retranslation). Re-presented at the gate.

## B01 voice-gate revision (commissioner feedback, round 2 — full read)

A second, much deeper review of the whole preface + ch01. Applied every item:
- Systemic/global: 破坏 "wrecking"->"sabotage"; 半个月 "half a month"->"two weeks";
  killing verbs put on a controlled set (制裁/镇压叛徒 = eliminate, 处决 = execute,
  broad 镇压 = crush; never "put down/dealt with" for lethal acts); "great"
  de-cluttered (major/considerable/far-reaching); numeral style fixed (spell <100
  and rhetorical rounds, digits for 100+/statistics); 及时 settled on "in time";
  trailing 。…… no longer ". …" in narrative (cut) or quotes (single trailing …);
  photo-caption disclaimer stated once in the translator's note, stripped from
  both captions.
- Per-item diction fixes (heart's blood->heart and soul; take->gather
  intelligence; pulled out->recruited from within; drove into->planted inside;
  throwing out->discarding; law of winning->of victory; stood on the defensive->
  lagged; spread->posted; wrong door->wrong place; etc.).
- Accuracy catches: 英租界 rendered "International Settlement police" (no British-
  only concession by 1922) with a footnote; the 虎狼成群 name-pun (Yang HU/tiger,
  Chen QUN/pack) now footnoted instead of read as a numeric slip; 单线联系 glossed
  as single-line contact tradecraft; a note on the 向导 4->6 issue gap; "Chen
  Duxiu's wife, Gao Junman" (antecedent fix).
- Two of my own inserted note-glosses had wrong characters: 谊->谋 (谋攻篇) and
  闽->闸 (闸北/Zhabei). Fixed. RULE recorded: proofread every inserted hanzi
  char-by-char against the glossary or scan.
- Thinned Wikipedia/Baidu pointers: cited Wakeman, Policing Shanghai for the
  Special Section; dropped the explicit Baidu pointer on Cheng Ziqing.
- STYLE.md updated with the round-2 META-DIAGNOSIS (translating at the token/
  clause level instead of writing English), seven more rulings, a decided-
  renderings word-level ledger, and the numeral rule.
- Section heading "...You Take a Beating" KEPT: the source 没有情报保卫工作就要挨打
  is itself colloquial/punchy; the register variation is the author's.
All checks green; 40 notes; qa_epub PASS; epubcheck 0/0. Style pass only,
content unchanged.

## Batch 2 (B02): ch02 (一科——特科的"总管家") + ch03 (情报科长"王庸"——陈赓) — DONE

Translated: **ch02** (Section One, PDF 60-76, printed 16-32; 40 body paragraphs =
untitled chapter intro + three sections ch02s01-03) and **ch03** (Chen Geng, PDF
77-94, printed 33-50; 37 body paragraphs in four sections ch03s01-04). Openers
folio-verified: ch02 PDF 60 = printed 16, ch03 PDF 77 = printed 33. Body offset
constant 44 confirmed throughout.

### Branch consolidation (rule 2)
Session opened on stray branch claude/zhou-enlai-b02-l2nkse, which was identical
to origin/claude/zhou-enlai (586cef0); local claude/zhou-enlai was stale at
acdea51. Reset local to origin, deleted the stray, pruned its tracking ref. All
work on claude/zhou-enlai.

### Source recovery (the heavy lift; do not re-discover)
The blank-line assembly path, left alone, DROPS or WELDS content on this book:
- **Author-footnote lines sit at page bottoms and eat the seam.** Streamed into
  the paragraph accumulator, a page-bottom footnote whose text ends in 。 flushed
  the spanning paragraph WITHOUT its continuation. Three whole paragraphs were
  lost this way and recovered: p67 (Zhou Enlai's 1946/1966/1973 tribute to the
  Xiong Jinding couple), p72 (the close of the 六届三中全会 account), p74 (method-1
  trial + the 任氏/何维道 rescue). FIX: strip footnote blocks from data/txt BEFORE
  assembly so paragraphs join across the seam.
- **Truncation-marker trap:** "会审公堂" appears in BOTH the p73 body and its
  footnote; truncating at the first hit cut live text (lost the whole method-1
  trial). Use a footnote-ONLY marker (军法会审处).
- **Photo pages are not all full-page.** p63/p68 are photo+caption only (blank
  them; body joins across); p83 is a 20%-photo with real body text below (strip
  ONLY the photo+caption, keep from "的腿是在盗窃").
- **Blank-less pages weld paragraphs** (p62, p65, p91): de-welded by hand against
  the scan. p65 = the 生黎医院/福兴商号 narrative is ONE paragraph through
  "革命生涯。", then "凡是当年" starts a new one.
- **Two OCR-clipped short lines restored from the scan:** "生涯。" (p65, dropped
  between 革命 and 凡是) and "客车。"" (p92, a 3-char line above the footnote).
All seams and blank-less pages eyeballed against the page images. The structural
surgery is SCRIPTED (source never re-typed) and committed under
scripts/recovery/ (b02_strip_furniture.py, b02_surgery.py, README with the regen
order) so a fresh data/zh regen replays. Final structure: ch02 40 body + 4
headings, ch03 37 body + 5 headings.

### Crop-verification (names/numbers, all eyeballed on the scan)
陈赓 (garbled ~15 ways) and its aliases 王庸/庶康; 熊瑾玎 (garbled 7 ways) + 朱端绥;
陆连奎 (not 陆连硅); 彭湃 (OCR read 彭涛, scan confirms 彭湃); 廖仲恺; 谭曙卿; 张克侠;
钱大钧; 刘鼎 (OCR 刘易); 欧阳新; 陈寿昌 (OCR 陈夺电); 董健吾; 阎锡山; 何基沣; 叶剑英;
任弼时 (aliases 彭德生/胡少甫) + 陈琮英 (not 陈玉英); 赵一曼/李一超/李坤泰; 李白/李侠/
裘慧英; 戴荣鑫 (tail-verify caught OCR 戴荣奢, scan shows 鑫). Dates fixed against
scan: 任弼时 arrest 1929年11月17日 (OCR dropped a 1); 卢冬生 joins CCP 1927年12月7日
(OCR 2月7日); 张克侠/李强 recollection dated 1983年5月24日. All recorded in
data/ocr_fixes.json (67 fixes this batch across ch02/ch03).

### Checks — all green
- verify_unit: parity 40/40 and 37/37, numbers 0 unresolved, anchors 16 + 13.
- check_align OK (median 4.49 / 4.58 en per han). check_content OK (all name
  occurrences in the paired paragraph; set glossary 黄埔军校 = "Whampoa" so the
  abbreviated recurring form anchors).
- qc_entities: 0 misses each.
- check_apparatus: 0 failures. qa_epub PASS (69 notes, 41 pagebreaks).
  epubcheck 5.1.0: 0 errors / 0 warnings.
- check_register --ref out/ch01_reading.md: within tolerance (ch02 em-dash 4.2,
  ch03 5.0 vs ref 6.0; sentence median 23 = ref; rhythm CV 0.59-0.63 vs 0.58).
  ch03's higher dialogue-contraction rate is the Chen Geng chase/dialogue scenes,
  flagged by the tool as noisy-but-in-tolerance.

### Notes: coverage and fact-check verdicts (16 ch02 + 13 ch03)
Fact-checked against Wikipedia (Chen Geng, Yun Daiying, Zhao Yiman, Li Bai, Peng
Pai): CORROBORATED and dated in the note. Chen Geng b. 27 Feb 1903, d. 16 Mar
1961; saved Chiang Kai-shek Oct 1925 (the episode the train story turns on).
Yun Daiying executed 29 Apr 1931 Nanjing, betrayed by Gu Shunzhang. Peng Pai
shot at Longhua 30 Aug 1929. Zhao Yiman = Li Kuntai/Li Yichao, executed by the
Japanese 2 Aug 1936. Li Bai (film Li Xia) executed 7 May 1949. Author's own
source citations reproduced as "Author's note." (Hong Yangsheng, Li Weihan, Liu
Shuqin, the CCP chronology, the Mixed Court gloss, Li Qiang's letter, Zhang
Kexia, the Chen Geng death-date note). Texture notes: 江东父老 (the Xiang Yu
allusion), 小开 (Shanghai slang), 红头阿三 (Sikh constables' nickname).
- NOT re-noted (already placed in ch00/ch01): White Terror, April 12 coup,
  Central Special Section, Gu Shunzhang, Red Squad, extraterritoriality, the
  concession constables, May Thirtieth movement, Cultural Revolution, Nanchang
  Uprising, Chen Geng (ch01 has a brief note; ch03 adds the fuller career note).
- Tier left deliberately unfootnoted: the minor cover-family and staff names
  (covered by the glossary); routine streets and their modern names.

### Source discrepancy preserved (not silently fixed)
The Political Bureau office is "云南路447号" in the ch02 body (p65, clean scan) but
"云南路477号" on the p68 photo caption; both are reproduced as printed, and the
figures.json caption flags it. Likely a caption typo in the source.

### Glossary
+83 rows this batch (people/places/orgs); status set per row (attested for the
well-documented, provisional/decided for the obscure cover names). Principals
REUSED unchanged from B01: 周恩来, 陈赓, 顾顺章, 李强 (+ aliases 王庸, 化广奇). Decided
this batch and to hold: 黄埔军校 = "Whampoa"; 中国救济总会 = China Relief Society;
国际济难会 = International Red Aid; 太古公司 = Butterfield and Swire; 会审公堂 rendered
"Mixed Court" with the author's own gloss footnoted.

## B03 — ch04 情报战线的英豪 / Heroes of the Intelligence Front (PDF 95-122, printed 51-78)

Four biographical sections in one unit: ch04s01 兵器专家刘鼎 (Liu Ding, weapons
expert), ch04s02 济世名医柯麟 (Ke Lin, physician), ch04s03 隐蔽战线的"福将"陈养山
(Chen Yangshan), ch04s04 血染沙场的陈寿昌 (Chen Shouchang). Offset 44 folio-verified
at every opener (folios 51-78 all confirmed by eye).

### Pipeline / assembly
- OCR: ocr_crop --left 0.11 --right 0.90 --top 0.135 --bottom 0.95 --psm 6
  --running-head "隐蔽战线统帅周恩来"; ocr_dual second read. pgrep -c tesseract = 0
  after each run. NOTE: recto running head is the CHAPTER title 情报战线的英豪
  (stripped by the top crop), verso is the book title (stripped by --running-head).
- Furniture (scripts/recovery/b03_strip_furniture.py): 5 garbled headings
  normalized to structure.json titles; 10 author-footnote blocks truncated;
  full-page 陈养山 portrait (p113) blanked; TOP photo 吴先清 (p101) and BOTTOM
  photo 柯麟 (p104) stripped. Figures: 3 (吴先清 p101, 柯麟 p104, 陈养山 p113);
  find_figures caught all three (photos, density 0.5-0.63); no 刘鼎/陈寿昌 portrait.
- Assembly is the hard part (as warned). The blank-line path force-breaks at
  every page seam and dropped two in-page blanks (p71 运到|上海, p73 李强、刘鼎|一起).
  scripts/recovery/b03_surgery.py: 4 splits + 16 backward-welds, all verified
  against the page scans (every one of the 27 content pages was eyeballed for
  indents). Final: **62 body paragraphs + 5 headings.** Two boundary calls made
  from re-reading the scan: the p110->p111 Ye Ting paragraph is ONE paragraph
  (first line not indented; source idx37); the Chen Yangshan "不久发生四一二"
  seam (p114->p115) is ONE sentence (welded).
- data/pagemap/ch04.json hand-regenerated for the 62-para structure (assemble's
  auto-output was stale post-surgery), 27 rows, printed 51-78, photo page 69 skipped.

### Checks (all green)
- verify_unit ch04: parity 62=62; numbers 0 unresolved (after noise + fixes);
  anchors n/a-then-24 placed.
- check_align: median 4.78 en/han, no pair strays >2.2x.
- check_content --config data/check_config.json (ch04 added): 225 name
  occurrences, 0 displaced (after two conventional-rendering fixes: 北京大学 =
  "Beijing University" per the shelf ledger, not "Peking"; 中国共产党党员 rendered
  with the full org name).
- qc_entities on the bilingual: 0 misses.
- check_register --ref out/ch01_reading.md: within tolerance (em-dash 0.3/1k vs
  6.0 ref, rhythm CV 0.48 vs 0.58).
- check_apparatus: 0 failures / 0 warnings. qa_epub: PASS (93 refs/bodies/backlinks,
  68 pagebreaks). epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings.

### OCR fixes (data/ocr_fixes.json, ch04 = 86 rows; replay with apply_fixes.py ch04)
167 replacements applied. Principal-name garbles were legion: 刘鼎 (刘易/刘瞻/刘里/
刘蜡/刘晤/刘允/刘淆/刘晶/刘轩/刘蜀), 陈赓 (陈刻/陈庆/陈记/陈广/陈庚/陈废), 柯麟 (柯罕/柯据/
柯所/柯饼/柯赫/柯蔚/柯记/柯岂/柯鹿/柯刨), 贺诚/贺龙 (锅诚/锅减/锅龙/货龙), 彭湃 (彭涯/彭洲/
彭洗/茧涯/芝涯/艾涯), 恽代英 (匈/怪/那/履/业/必=/人必代英), 陈养山 (陈养出/陈蛮山), 陈寿昌
(陈夺虽/陈寿虽/陈寿吕/陈寿员). Did NOT blanket-replace 陈 (陈独秀/陈炯明/陈宝骅/陈潭秋/
陈原道/陈志英/陈月波/陈希堪 all distinct and correct). Key crop-verified readings:
魏宸祖, 杜月笙, 陈宝骅, 任弼时, 佐野学, 白鑫, 杨登瀛/鲍君甫, 刘伯承, 阚思俊(刘鼎 orig name).

### Source discrepancies preserved (rendered as printed, footnoted)
- **Chen Shouchang death date:** book says "1935年初" (early 1935); he was in
  fact mortally wounded at Laohudong 21 Nov 1934 and died the next day (aged 28).
  The 1935 is when the Soviet named a memorial "Shouchang County" after him.
  Rendered as printed, corrected in the note.
- **He Cheng dates:** book prints "贺诚(1901~1981)"; he actually died 8 Nov 1992,
  not 1981. Rendered as printed, corrected in the note.
- **He Long bounty:** the 100,000-silver-dollar figure is the book's; not
  independently corroborated (noted).
- **1948年夏** (Ke Lin/Ye Jianying to Shanghai after the Dec 1927 Guangzhou
  Uprising): an obvious misprint for 1928; rendered as printed (no note added, as
  the 9-months-in-Hong-Kong context makes the year self-evidently 1928 — flagged
  here for the read-through if a note is wanted).
- **胡汉民改组派** (idx13): the Reorganizationists were Wang Jingwei's faction;
  the source ties them to Hu Hanmin. Rendered as printed (Mu Xin's framing).
- **12月1日 vs 12月17日** (radio class raid): OCR dropped the 7; scan shows
  12月17日. Fixed in source; English carries "17 December 1930".
- **老虎洞鸦尖坳**: the death-site place name; rendered "Laohudong-Yajian'ao".

### Notes: 24 added (numbered continuously by the builder; 93 total book-wide)
Reader-model density with fact-check verdicts IN the note; all verified against
Wikipedia/Baidu Baike/PRC party-history organs (NO LLM-sourced content). The four
subjects (Liu Ding, Ke Lin, Chen Yangshan, Chen Shouchang) each get a career
note; plus Wu Xianqing (Soviet purge death, rehabilitated 1984), Pan Hannian
(arrested 1955, d.1977, rehab 1982), He Long, Ye Ting/New Fourth Army, Yang
Dengying/Bao Junfu (cross-ref ch06), Yang Xianzhen, He Cheng, Bai Xin, Luo Ming
(the "Luo Ming line" 1933), Deng Xiaoping (Shanghai underground), Blyukher/Galen,
Thälmann, Sano Manabu (the June 1933 tenkō recantation — a partisan irony the
book leaves unremarked), Zunyi Conference, Fifth Encirclement, CC Clique/中统,
KUTV, Stalin's *Concerning Questions of Leninism*, Chen Tanqiu (author's-note
reproduction), the author's own voice (Mu Xin identified), Three Heroes of
Longtan (cross-ref ch05).

- **NOT re-noted (already placed in ch00-ch03):** White Terror, April 12 / April
  15 coups, Central Special Section, Gu Shunzhang, Red Squad, Nanchang Uprising,
  Whampoa, Peng Pai (ch02), Yun Daiying (ch02), Ren Bishi (ch02), Li Lisan /
  Li-San Line (ch02), Liao Zhongkai assassination (ch03), May Thirtieth, February
  7 strike, Cultural Revolution, Three Heroes of Whampoa. Cross-referenced where
  useful.
- **Tier left deliberately unfootnoted:** minor cover names and one-appearance
  local figures (covered by the glossary), routine place names and their modern
  equivalents, the 1948->1928 misprint.

### Glossary: +85 rows (now 177 total). Reorganized into categories by hand.
People (46), organizations (13), places (19), works (7). GOTCHA for next batch:
apparatus_merge.py adds glossary rows FLAT at the top level; they must be moved
into the people/organizations/places/works/terms sub-dicts afterward or the
builder's render_glossary crashes on a string value. Decided this batch and to
hold: 北京大学 = "Beijing University" (shelf ledger, not "Peking"); 东方大学 =
"Communist University of the Toilers of the East"; 达生医院 = "Dasheng Hospital";
镜湖医院 = "Kiang Wu Hospital"; 汇丰银行 = "Hongkong and Shanghai Bank"; 中统 =
"CC Clique / Central Bureau of Investigation and Statistics"; alias 老王 =
"Old Wang" (Chen Yangshan). REUSED unchanged: 陈赓, 周恩来, 顾顺章, 李强, 彭湃,
恽代英, 贺龙, 叶挺, 叶剑英, 刘少奇, 邓小平, 朱德, 任弼时, 李立三, 廖仲恺, 刘伯承 and the
four ch03-introduced intelligence workers 刘鼎/柯麟/陈养山/陈寿昌.

### noise.txt additions (this batch)
第二天, 第二年 (day/year idioms), 二十多万 (EN "two hundred thousand"), 10万大洋 /
30万 (EN "100,000" / "300,000"; Arabic+万 the check can't pair), 曾三 (name Zeng
San), 万载 (place), 老百姓 (idiom). Extend, do not prune.

---

## B04 - ch05 ("Three Heroes of Longtan") + ch06 (Yang Dengying)

Both chapters complete. ch05 = 41 body paragraphs + 3 section headings; ch06 =
40 body paragraphs + 5 section headings. All checks green: parity 41/41 and
40/40; check_numbers 0 unresolved both; qc_entities 0 misses; check_align OK;
check_content OK across both; check_apparatus 0 failures; check_register within
tolerance of the ch01 reference (em-dash 1.9 and 1.8 per 1k, well under the ref
6.0). EPUB rebuilt: 7 of 28 chapters, 116 notes, 96 pagebreaks; qa_epub PASS;
epubcheck 0 errors / 0 warnings.

### Assembly (the usual seam surgery; scripts in scripts/recovery/)
- b04_strip_furniture.py: normalized 10 garbled headings (chapter titles +
  8 section titles) to the exact structure.json strings via a PER-TARGET length
  guard (len(good)+4), because ch05/ch06 headings run 8-21 chars and one ch06s05
  body line duplicates the s05 heading tokens; truncated 8 author-footnote blocks;
  blanked the two full-page photos (p125 Dong Biwu calligraphy, p134 Qian
  Zhuangfei portrait).
- b04_surgery.py: ch05 3 splits (the 阿英 memoir block, the 宋治家 memoir block,
  the 李克农 exam testimony) + 16 welds, including the 宋治家 quote continuation on
  p130 that the OCR captured with a blank line between EVERY line (over-split into
  9). ch06 4 splits (连德生 bio, the 内奸/山东省委 block, the s05 Mao-quote opening,
  the s05 close) + 5 welds. NOTE the ch06 s05 split marker had to be "杨登注的事例"
  (not "的事例") so 杨登瀛 lands in the next paragraph, not the Mao quote (else
  qc_entities would demand Yang Dengying inside the Mao quote).
- Assembly uses the BLANK-LINE path; indents.py still unreliable here.
- data/pagemap/ch05.json (14 entries) and ch06.json (14 entries) hand-regenerated
  for the post-surgery structure via /tmp/regen_pagemap.py logic (match each
  page's first body line into the final fixed ZH). p125/p134 skipped (photos).

### OCR fixes (data/ocr_fixes.json; replay with apply_fixes.py)
- ch05: 28 rows. Load-bearing number: 悬赏5万元 (crop-verified p83; OCR read
  "上贫3万元"). Also stray-digit garbles that injected phantom quantities (《4中央
  ->《中央, 隐蔽8->隐蔽, i927->1927, 田十->田埂, 用十文->用古文, 社会人十->社会人士,
  孔祥四->孔祥熙, two garbled footnote markers), Hu Di alias 光天->裳天, and the
  Shanghainese word 瘪三 (three OCR variants) which the number check reads as "3".
- ch06: 22 rows, mostly the pervasive entity garbles: 杨登瀛 (7 variants, 76
  occurrences), 陈赓 (8 variants), 刘鼎 (刘易/刘里), 徐恩曾, 兰普逊 (兰善撑),
  杨剑虹 (杨剑蚜), plus the ①->0 footnote-marker garble in the Mao quote.

### Crop-verified this batch (verify_names.py + eyeball)
李克农 reward 5万 (p83); 李克农 aliases 曼梓/稼轩/泽田/侠公/震中/钟和 (p82);
胡底 aliases 北风/胡马/裳天/伊于胡底, orig. name 胡百昌 (p94). The crop tool
mislocated top-of-page lines (grabbed the running-head band); re-read those from
the full page image instead.

### Footnotes: 16 in ch05, 7 in ch06 (fact-checked, verdicts IN the note)
ch05 new subjects: Li Kenong (General 1955, deputy foreign minister, d. 1962 -
corroborated), Dong Biwu (CCP founder, acting head of state 1972-75), Qian
Zhuangfei (d. ~1 Apr 1935 near Jinsha, Guizhou; fixed by a 2002 inquiry -
corroborated), Hu Di (strangled Sept 1935 on Zhang Guotao's orders; the source's
"1936" is a year late - CONTRADICTED on the date), Cai Mengjian (arrested Gu
Shunzhang Apr 1931), Xu Enzeng (中统 chief, Chen Lifu's cousin), the Sun Society,
the 煞星 folk term, the Monkey-King / Journey to the West allusion, and the
classical poem behind 南飞. Author's notes reproduced ("Author's note." tag):
Xiong Xianghui memoir, 阿英 People's Daily piece, 台北 Biographical Literature,
张振华 date-discrepancy note, 叶炳南 biography, 张振华 talk record.
ch06 new subjects: Chen Lifu / Chen Guofu ("two Chens" / CC Clique), Lampson
(source gives the English name; Special Branch of the Shanghai Municipal Police;
the individual could not be identified - UNCORROBORATED as to the man), the
Tanaka Memorial (authenticity DISPUTED), Shanghai: The Paradise of Adventurers
(G.E. Miller, 1937), An E, and a cross-ref note on Yang Dengying (recruited
ch04). Author's note: the Mao "On Tactics Against Japanese Imperialism" citation.

- **NOT re-noted (already placed):** Gu Shunzhang (ch00), White Terror / April 12
  (ch00), May Thirtieth (ch01), CC Clique / 中统 / Central Bureau (ch04),
  Concessions (ch01), Songhu Garrison (ch03), Communist University of the Toilers
  of the East (ch04), Peng Pai (ch02), Whampoa (ch03), Qian Dajun (ch03), Three
  Heroes of Longtan concept (ch04, cross-ref). Cross-referenced in the new notes.
- **Deliberately unfootnoted:** the Tang/Han figures in the elegy commentary
  (Fang Xuanling, Li Zuoche, Wei Zheng, Du Ruhui, Han Xin) are explained in Mu
  Xin's own commentary paragraph; one-appearance walk-ons covered by the glossary.

### Figures: 2 (ch05). p125 Dong Biwu's calligraphy of the elegy (placed before
the elegy-commentary paragraph); p134 the Qian Zhuangfei portrait (before his
bio). Cropped by hand from the page PNGs into data/figs/. ch06 has no figures
(deliberate: no plates or portraits on printed 96-109).

### Glossary: +37 rows, added DIRECTLY nested into categories (people/works/
terms/organizations) to sidestep the flat-then-renest crash. New recurring cast
that returns later: 徐恩曾, 陈立夫, 陈果夫, 张道藩, 蔡孟坚, 连德生, 兰普逊, 谭绍良,
安娥. REUSED unchanged: 李克农, 钱壮飞, 胡底, 杨登瀛/鲍君甫, 陈赓, 刘鼎, 陈养山,
顾顺章, 周恩来, 杨剑虹, 钱大钧, 柯庆施, 瞿秋白. Rendering held: 龙潭三杰 = "Three
Heroes of Longtan"; 田中奏折 = "Tanaka Memorial"; 上海——冒险家的乐园 = "Shanghai:
The Paradise of Adventurers"; 论反对日本帝国主义的策略 = Mao's "On Tactics Against
Japanese Imperialism."

### noise.txt additions (this batch)
正经八百 (idiom), 瘪三 (Shanghainese "bum", contains 三), 30年代 (EN "1930s"),
胡百昌 (name contains 百), 5万 (Arabic+万 bounty, EN "50,000"), 金钱万能 /
万里 (idioms). Extend, do not prune.

### Environment note
The pre-existing regression test "hook stands down on template stub" still FAILS
(template maintenance only; does not affect real batches). epubcheck re-fetched
to /tmp/epubcheck-5.1.0.

## Batch 5 (B05): ch07 (深入龙潭虎穴 / Deep into the Tiger's Den) + ch08 (奉天讲武堂教官——赵唯刚 / Fengtian Military Academy Instructor — Zhao Weigang) — DONE

- **ch07** = PDF 154-172, printed 110-128, 5 sections. **54 body paragraphs**,
  6 headings, 14 notes, 0 figures.
- **ch08** = PDF 173-197, printed 129-153, 6 sections. **54 body paragraphs**,
  7 headings, 13 notes, 0 figures. Sections s02-s06 are Zhao Weigang's own 1983
  memoir, reproduced verbatim (first-person); rendered plain and concrete per
  the memoir voice sheet, introduced by a note at "Here I set down, in full,
  this memoir." No {v} markers.
- Branch consolidated onto `claude/zhou-enlai` (stray per-task branch
  `claude/...b05...jybavp` was identical to origin, deleted local; the remote
  ref never existed on origin, pruned).

### Assembly — the heavy lift (do NOT re-discover)
The OCR emits paragraph blank lines INCONSISTENTLY: most pages carry them, but
several do not, so the blank-line assembler UNDER-split there (welded distinct
source paragraphs). This is the opposite of B04's block-quote OVER-split, and the
sentence-end heuristic does NOT catch it (both halves end in 。). Found only by
eyeballing every content page. Recovery scripts (tracked): `b05_strip_furniture.py`,
`b05_surgery.py`, `b05_pagemap.py`.
- **b05_surgery.py ORDER matters:** WELDS run FIRST (reunite page-seam breaks),
  then SPLITS (break the OCR-welded paragraphs), then fixups. A split target can
  span a weld (ch07 s02 P1-P4), so splits-before-welds fails. NOT idempotent:
  re-assemble ch07 AND ch08 before re-running.
- ch07 under-splits fixed: s02 [14]->4 paras, [16]->4 (Song Jiren memoir region:
  intro+quote1 | intro2 | set-off block quote | HQ paragraph), [18]->2
  (descriptions | Zou Taofen); s04 block-quote blob [43]->12 (the Li Kenong
  biographer's Liu Bocheng-escort account, indent-only, no OCR blanks p169-170).
- ch08 under-splits fixed: s03 [29]->3, s05 [40]->4 — BOTH on section-opener
  pages (p187, p192), where the OCR emitted a blank after the heading but none
  between the body paragraphs. Every other memoir page assembled clean.
- Scan-verified clipped-line restorations: ch07 p171 the last line of the Li
  Kenong quote ("...就在中央饭店楼上一住……"), dropped by OCR before the s05 heading.

### Crop-verification (names/numbers/dates, eyeballed on the scan)
- ch07 systematic name mangles fixed via ocr_fixes: 徐恩曾 (8 曾-garbles + 4
  兽-garbles), 陈赓 (庆/刻/广/席/钴), 蒋介石 (薪/萝/葛/欧 + 葛家王朝), 杨登瀛,
  顾顺章, plus 邹韬奋 (韬 read as 三/友/播/辐/耕), 章乃器 (乃->万), Zou-quote
  book-title bracket (《->4). Real translation catch from check_numbers: 二届
  **四**中全会 = Fourth Plenum (I had written "Second"). 20万 noised (Arabic+万).
- ch08: 蔡麻子 (葵/殖/茸/歼/化/花), 蔡伯祥 (袭->蔡), 吴宝祥 (关->吴), 杨宇霆
  (宇霆->字才/字), 臧士毅 (成/藏/医士圾), 翁之麟 (彬/忌), 大阪 (孤/了啤),
  千叶 (干->千), 老廖=廖如愿 (记/雇/庆/康), 老蔡 memoir shorthand (葵/葡/莫/蒙/
  节/华/花/蓝/伍/秦 all -> 蔡). Dropped-digit ages: 92岁 (9岁), 94岁 (4岁);
  1951年 (195S1年); 古色古香 (古->十).

### Checks — all green (both units)
verify_unit (parity 54/54 each, numbers 0 unresolved, anchors 14+13 ok);
check_align OK; qc_entities 0 misses; check_content "all in the paired paragraph";
check_register within tolerance vs ch01 (ch08 contractions elevated — colloquial
memoir, expected; em-dash 6.5/6.1 per 1k). check_apparatus 0/0. qa_epub PASS
(28 docs, 450 paras, 143 notes ref/body/backlink, 136 pagebreaks). epubcheck
5.1.0: 0 fatals / 0 errors / 0 warnings.

### Notes: coverage and fact-check verdicts (14 ch07 + 13 ch08)
- ch07: Gu's manual《特务工作之理论与实际》; C.P.=Communist Party (author's ①);
  蒋家天下陈家党 idiom; the Zhongtong's org history (x-ref ch04/ch06); Xu Enzeng
  b.1898 in the book vs **1896** in the record (CONTRADICTED, footnoted; d.1985);
  Zhang Wen citation (author's ①); Zou Taofen + Life Bookstore + Seven Gentlemen
  (章乃器/李公朴 named); Ren Zhuoxuan/Ye Qing (renegade theorist); Dai Li/Juntong;
  Song Jiren citation (author's ①); Liu Bocheng (later marshal); Central Plains
  War 1930; Zhang Xueliang the Young Marshal; Xu's memoir《The Invisible
  Conflict》1957 (author's ①). All corroborated except the Xu birth year.
- ch08: Gu's chart codenames (满洲麻子=Cai); Zhao Weigang aliases + Liu Shaoqi
  rescue (corroborated); May Thirtieth 1925; the 1924 Soviet treaty renunciation
  (Karakhan); Guo Songling revolt 1925; Chinese Eastern Railway war 1929; the
  九一八/Mukden Incident; **Cai Boxiang wrongly killed as a traitor and cleared**
  (as related on Chen Geng's authority; specific circumstances UNCORROBORATED
  independently); Northeast Flag Replacement 1928; Puyi's Manchukuo enthronement
  amnesty; Liu Bogang bio (author's ①); the five killed at Boketu (author's ①);
  the memoir-reproduction note. X-refs (NOT re-noted): New Youth/The Guide
  (ch01), August 7 Conference (ch02), Li Lisan line (ch02), Zhang Xueliang (ch07).

### NOT re-noted (already placed earlier in the book)
龙潭三杰/Three Heroes of Longtan (ch05), Li Kenong/Qian Zhuangfei/Hu Di bios
(ch05), Gu Shunzhang (ch00), Chen Lifu/Chen Guofu/CC Clique (ch04, ch06), Xu
Enzeng basic bio (ch05), April 12 / White Terror (early), New Youth & The Guide
(ch01), August 7 Conference & Li Lisan line (ch02).

### Glossary: rows added DIRECTLY nested (people/orgs/places/works)
New principals flagged: 赵唯刚 Zhao Weigang (cast_order 6), 蔡伯祥 Cai Boxiang
(cast_order 7). 中统 decided = "Zhongtong", 军统 = "Juntong", 党务调查科 =
"Investigation Section" (formal expansions live in the notes, not the prose, so
check_content stays clean). REUSED unchanged: 徐恩曾, 陈立夫, 陈果夫, 张道藩,
钱壮飞, 李克农, 胡底, 杨登瀛, 陈赓, 周恩来, 顾顺章, 蒋介石, 李立三, 刘伯承,
张学良, 冯玉祥, 阎锡山.

### noise.txt additions (this batch)
徐新六, 三明, 三洋泾桥, 派头十足, 40年代, 20万 (ch07); 千叶, 九一八, 70年代,
七七八八, 四平, 万岁 (ch08). Extend, do not prune.

### Figures: 0 for both chapters (deliberate)
find_figures 154-197 found nothing; every content page eyeballed and every
chapter opener/memoir page confirmed text-only. No plates or portraits in the
ch07/ch08 folio ranges.

### Reading uncertainties for the read-through
- ch08 minor memoir figures resolved from the scan but obscure: 老廖 = 廖如愿
  (Manchuria prov. cmte secretary-general); the Shanghai contact's surname reads
  廖 at p180 but 庆 at p179 (OCR); rendered "Old Liao" throughout.
- The book's ch08 focuses on the rescue of 刘伯刚 (Liu Bogang, Zhao's classmate);
  scholarship on Zhao Weigang foregrounds instead his 1929 role shielding Liu
  Shaoqi — a different episode, noted at the aliases anchor.
- Source internal discrepancy kept: Xu Enzeng b.1898 (book) vs 1896 (record).

## Batch 6 (B06): ch09 (行动科和"红队" / The Action Section and the "Red Squad", PDF 198-217, printed 154-173) + ch10 (红队利剑出鞘 / The Red Squad Draws Its Sword, PDF 218-230, printed 174-186) — DONE

Both back in Mu Xin's narrative-history voice (the Red Squad's operations, Gu
Shunzhang the stage magician who built it, the Luo Yinong betrayal and reprisal),
with several long set-off block quotes (Chen Yangshan on the pickets; the John
Byron / Robert Pack Claws of the Dragon passage; Li Yimang's Blurred Screen
account of the 1930 "Soviet Congress"; Li Wenyi, Zhang Weizhen, Huang Jieran, and
Li Weihan on Luo Yinong's arrest, death, and the reprisal). Result: ch09 = 53
body paragraphs (5 headings), ch10 = 34 body paragraphs (5 headings, including
Luo Yinong's two-line death poem set as {p} verse).

### Assembly — the B06 disease was near-total welding plus OCR-dropped sentence-ends
On the section-opener and block-quote pages the OCR dropped ALL paragraph blanks,
so the assembler welded whole runs of source paragraphs (one blob per section ran
6 assembled -> 23 true paragraphs in ch09 s02). Rather than the fragile
weld-then-split, B06 RE-SEGMENTS: concatenate each section's assembled body into
one blob (the continuous source text, since Chinese lines join with no space) and
re-split at a verified list of paragraph-START markers, each confirmed to occur
exactly once in its blob. scripts/recovery/b06_surgery.py carries the marker
lists and a boundary-SNAP (moves the tail after the last sentence-final
punctuation of a piece onto the next), so a marker chosen a few chars into its
paragraph still lands the split at the true boundary; it also refuses to move a
trailing "(《…》)" citation forward. The snap exposed EIGHT OCR-dropped or
mangled sentence-ends that had merged two paragraphs; all are restored in
b06_strip_furniture.py's RESTORE table (verified on the scan): p200 畏怯动摇。(→晨),
p204 。①(→.中), p208 震动。(dropped), p213 牺牲了。(→，), p222 农的就是何家兴和贺稚华。
(dropped run) + 抄走。(→，), p226 。①(→.中), p227 就义。(dropped). Also a dropped
digit trap caught by check_numbers: 1926年11月 and 11月4日 both OCR'd 1月 (11->1),
and 4月15日 OCR'd 4月415日 — the English already had the right dates from the scan.

### Furniture strip (b06_strip_furniture.py, all tracked)
Normalized the 2 chapter + 8 section headings to the exact book.json titles
(per-target guard); INSERTED the ch09 s04 heading 镇压叛徒绝不手软 that BOTH OCR
configs dropped on p214; truncated 9 author-footnote blocks (p199,201,202,204,214,
224,226,228,230 — p202 carries two gloss footnotes ① 爱多亚路 ② 番摊); stripped the
two embedded photos (p210 李一氓 at his desk, caption after the last body line;
p225 李文宜, garbage+caption before the body) and the p225 leaked folio.

### Figures (2 — first figures since B04)
find_figures flagged p210 and p225; both are portraits. ch09: p0210-f1.png (Li
Yimang at his desk, 1984), placed before the Blurred Screen block quote. ch10:
p0225-f1.png (Li Wenyi holding Yang Zhihua's daughter Qu Duyi), placed before the
Zhang Weizhen quote. alt+caption in figures.json; captions are the source's.

### Checks — all green (both units)
verify_unit (parity 53/53 and 34/34, numbers 0 unresolved with data/noise.txt,
anchors ok); check_align OK (median 4.44 / 4.63 en/han); qc_entities 0 misses;
check_content all-in-paired-paragraph; check_register within tolerance vs ch01
(em-dash 3.0 / 2.5 per 1k, BELOW ch01's 6.0; little dialogue so contraction rate
noisy). check_apparatus 0/0. qa_epub PASS (28 docs, 527 paras, 168 notes
ref/body/backlink, 168 pagebreaks). epubcheck 5.1.0: 0 fatals / 0 errors / 0
warnings.

### Notes (16 ch09 + 9 ch10 = 25) — coverage and fact-check verdicts
Reader notes: 拿摩温 "number one" (pidgin from English); 大世界 Great World; the
Claws of the Dragon book (John Byron/Robert Pack 1992, biography of Kang Sheng —
CORROBORATED, real book, "John Byron" a diplomat's pen name); 王凡西 Wang Fanxi +
双山回忆录; the 1930 Soviet Congress (Li Lisan line, x-ref); 李一氓 Li Yimang;
淞沪警备司令部 Songhu Garrison Command; 布尔塞维克 Bolshevik journal; 工部局 /
"British Concession" period looseness (International Settlement); 布拉吉 = Russian
platye (texture); 钱大钧 Qian Dajun; 洛克 Locke (conjectural romanization). Two
fact-check corrections: **赵一曼 killed at 珠江 is a misprint for 珠河 County**
(renamed Shangzhi 1946, which the memoir itself uses two sentences later —
CORROBORATED correction); **阮啸仙 "later defected" is CONTRADICTED** — Ruan
Xiaoxian (1898-1935) did not defect, he stayed behind after the Long March and
was killed in Jiangxi in 1935, a martyr. 柔石/胡也频/冯铿 = three of the Left
League Five Martyrs (Oriental Hotel arrest Jan 1931, Longhua 7 Feb 1931 —
CORROBORATED). Ten author footnotes reproduced tagged "Author's note." at the ①
anchor (the source-citation footnotes: 中统特工秘录, 杜宁/党的文献, 关于中央特科,
李一氓/模糊的荧屏, and the Luo Yinong talk-transcripts — Li Wenyi, Zhang Weizhen,
Huang Jieran, Li Weihan, all from Jin Zaiji's 1981 article — plus the p202 glosses
爱多亚路=Yan'an East Rd and 番摊=fantan).

### NOT re-noted (already placed earlier in the book)
Gu Shunzhang bio+defection (ch00), Green Gang / "April 12" (ch00), Red Squad /
Central Special Section (ch00, ch01), Dog-Beating Squad / 巡捕房 (ch01), May
Thirtieth (early), August 7 Conference / Li Lisan line (ch02), Luo Yinong bio +
betrayal (ch02), Zhao Yiman / Li Kuntai (ch02), Mixed Court 会审公堂 (ch02),
Peng Pai + Yang Yin (ch02), Deng Xiaoping (ch04), Bai Xin (ch04), Whampoa /
Yun Daiying / extraterritoriality (early), Gu's manual 特务工作之理论与实际 (ch07).

### Glossary: 33 rows added DIRECTLY nested (people/orgs/places/works)
New: 行动科 = "Action Section", 打狗队 = "Dog-Beating Squad", 淞沪警备司令部 =
"Songhu Garrison Command"; 大世界 = "Great World"; works 康生传 = "The Claws of the
Dragon", 双山回忆录 = "Reminiscences of Shuangshan", 模糊的荧屏 = "The Blurred
Screen", 布尔塞维克 = "Bolshevik"; and the batch's people (张杏华, 颜昌颐, 钟汝梅,
谭忠余, 林金生, 王凡西, 林育南, 柯柏年, 滕代远, 何长工, 柔石, 胡也频, 冯铿, 徐锡根,
阮啸仙, 戴冰石, 杨剑虹, 陈尉年, 王松生, 黄第洪, 唐瑞林, 张维桢, 黄玠然, 郑超麟,
许白昊, 吴稚晖). REUSED unchanged: 顾顺章, 罗亦农, 李一氓, 杨登瀛, 李维汉, 邓小平,
彭湃, 李文宜, 赵一曼, 何家兴, 贺稚华, 钱大钧, 周恩来, 陈赓, 蒋介石, 陈立夫, 徐恩曾,
李立三, 刘鼎, 任弼时, 刘少奇, 陈独秀. Dropped a 工部局 row (prose uses "Municipal
Police" for 工部局捕房; the note carries "Shanghai Municipal Council").

### noise.txt additions (this batch)
五粮液, 百炼成钢, 一二百 (ch09 idioms/brand, English carries the sense); 两手,
4万 (ch10 — 两手="both hands"; 4万 is an Arabic+万 mix the parser can't combine,
English carries "40,000"). Extend, do not prune.

### Reading uncertainties for the read-through
- 洛克 (the British agent who arrested Luo Yinong) is given only in Chinese
  transcription; "Locke" is a conjecture, footnoted.
- Source date discrepancies kept as printed and footnoted: the bounty-poster in
  Li Wenyi's letter is dated 4月22日 though the execution was 4月21日; Huang
  Jieran's talk-transcript is dated "1930年4月1日" in the scan, evidently a
  misprint for 1980.
- 珠江 (Zhao Yiman's death place) rendered as printed with a note that it is a
  misprint for 珠河/Shangzhi.

## Batch 7 (B07): ch11 (霞飞路侧的枪声(上) / Gunshots off Avenue Joffre, Part 1, PDF 231-246, printed 187-202) + ch12 (霞飞路侧的枪声(下) / Part 2, PDF 247-262, printed 203-218) — DONE

The Bai Xin affair: the traitor's tip-off, the arrest (24 Aug 1929) and
martyrdom of Peng Pai, Yang Yin, Yan Changyi, Xing Shizhen (executed 30 Aug;
Zhang Jichun survived), the failed armed rescue; then the Red Squad's hunt and
killing of Bai Xin off Avenue Joffre (11 Nov 1929), the press coverage, and a
life of Tan Zhongyu who led the strike. ch11 = 39 body paras + 4 headings,
11 notes, 1 figure. ch12 = 42 body paras + 4 headings, 8 notes, 3 figures.

### Checks — all green
- parity: ch11 39/39, ch12 42/42 (check_structure --pairs).
- numbers: verify_unit / check_numbers --noise, 0 unresolved both units.
- entities: qc_entities 0 misses both (彭湃 x42, 白鑫 x24/x31, 杨殷 x25, 谭忠余 x20).
- alignment: check_align OK; check_content (ch11/ch12 added to check_config) OK.
- register: check_register --ref out/ch01_reading.md within tolerance (both
  low-dialogue, flagged noisy — expected for documentary/biographical chapters).
- apparatus: check_apparatus 0/0; anchors 11 ok (ch11) + 8 ok (ch12).
- build: qa_epub PASS (13/28 chapters, 187 notes, 198 pagebreaks); epubcheck
  5.1.0 clean (0 fatals / 0 errors / 0 warnings).
- tail verification (rule 4): read the final paragraphs of each unit against the
  scan; corrected 湖北、襄阳、枣阳 (OCR 训阳/束阳) and 鄂豫苏区 (OCR 鄂天) in ch12's close.

### Assembly — same B06 disease; b07_* scripts (tracked)
Near-total welding on opener/block-quote/newspaper pages plus OCR-dropped
sentence-ends. b07_strip_furniture.py: normalized 8 headings; INSERTED the ch11
s02 heading 武装营救未能奏效 (both OCR configs dropped it, folio 195); blanked the
full-page 彭湃 arrest-site photo (p232); DELETE_BEFORE the Hehe-Fang photo (p251)
and the 时报 facsimile (p254); OVERWROTE p257's mangled 字林西报-translation opener
with a clean scan transcription (the English facsimile bled into the OCR);
truncated 8 author-footnote blocks; RESTORE table of 13 dropped sentence-ends /
stray footnote-marker chars / a dropped run (说是"东方惟一的大暗杀案"。 folio 209)
and the joint-signature line 挼安 of the martyrs' final report (folio 200).
b07_surgery.py RE-SEGMENTS by verified marker list (ch11 s01/s02/s03 = 14/11/14,
ch12 s01/s02/s03 = 15/21/6) with the boundary-SNAP. b07_pagemap.py regenerates
the pagemaps. NOT idempotent: re-assemble both units before re-running surgery.
NOTE apply_fixes.py is NOT idempotent either — a "wrong" that is a substring of
its "right" (1月11日带领红队 -> 11月11日带领红队) corrupts on a SECOND apply; always
clean-regen (strip -> assemble -> surgery) before apply_fixes, never incrementally.

### data/ocr_fixes.json — ch11 ~90 rows, ch12 ~40 rows
Heavy per-name garble maps (彭湃 had ~14 distinct garbles, 白鑫 ~20, 杨殷 ~12,
颜昌颐 ~10). Crop-verified numbers: 11月11日 (departure AND s03 opener, dropped
digit twice), 11月9日 (吴开先 report; 5->9), 90多发子弹 (9->90), 8月30日 ($->8),
共5人/标传5人 ($->5), 三民照相馆 (三->二), 廿八/廿二 kept as printed. Phantom
numerals fixed: 《->4 (six work-title brackets), 了->7, 士->七/十, 干->千, leaked
folio ji95->头子, 乃命 (乃->万). Family names verified on folio 203/216: 彭洪,
许玉庆, 彭小沛, 周凤, 彭仕禄 (source prints 仕; person is Peng Shilu, footnoted).

### NOT re-noted (already placed earlier; cross-referenced instead)
Peng Pai + Yang Yin (ch02), Bai Xin + Ke Lin (ch04), Nanchang Uprising (ch00),
August 7 Conference (ch02), May Thirtieth (ch01), Whampoa (ch03), Longhua (ch01),
White Terror (ch00), April 12 (ch00), Red Squad / Dog-Beating Squad (ch01),
Hailufeng (ch02), Sun Yat-sen (ch03), the Concessions / Municipal Police / Mixed
Court / Songhu Garrison (ch01-02), Kang Sheng (ch09 — cross-ref'd for the 1931
reorganization).

### Glossary: 28 rows added (nested), key reuse held
New people: 杨殷 Yang Yin, 白鑫 Bai Xin, 邢士贞 Xing Shizhen, 张际春 Zhang Jichun,
范争波 Fan Zhengbo, 范争洛 Fan Zhengluo, 熊式辉 Xiong Shihui, 方乃斌 Fang Naibin,
吴开先 Wu Kaixian, 周惠年 Zhou Huinian, 许玉庆 Xu Yuqing, 康生, 陈云, 张纪恩,
韩云秀, 蔡飞, 罗斯 Ross. Places: 和合坊 Hehe Fang, 蒲石路 Rue Bourgeat (named in
the reproduced NCDN article), 白宫饭店 White Palace Hotel, 新世界饭店, 达生医院.
Works: 字林西报 North China Daily News, 时报 Shi Bao, 申报 Shen Bao, 大陆报 The
China Press, 民国日报 Minguo Ribao, 中华英烈. REUSED unchanged: 彭湃, 颜昌颐,
谭忠余, 陈赓, 顾顺章, 杨登瀛, 柯麟, 周恩来, 关向应, 瞿秋白, 张道藩, 陈立夫,
蒋介石, 李强, 李立三, 贺诚, 红队, 中央特科, 打狗队, 淞沪警备司令部, 龙华.

### noise.txt additions (this batch)
百禄里, 两广, 广三铁路, 广九 (place/rail compounds with a digit-glyph); 丘八
("gray tunics", soldier slang), 万望, 万难, 千万群众, 惊惶万状, 十恶不赦, 第二天,
这两天 (idioms/rounds the English carries by sense). Extend, do not prune.

### Reading uncertainties / source facts for the read-through
- 吴开先's report reproaching the Concession is dated 11月9日 as printed, two days
  BEFORE the killing it discusses (11月11日) — a likely misprint, kept and footnoted.
- The claim of a 28 Aug 1929 attempt on Chiang Kai-shek's life (in Zhou Enlai's
  own contemporary essay) is not independently corroborable; footnoted as stated.
- The reproduced North China Daily News article overstates Bai Xin's rank
  (garrison detective-bureau chief); footnoted, its account otherwise corroborates.
- The two reproduced newspaper articles (时报, 字林西报) are internally
  self-contradictory in places; the source flags this with bracketed 按 notes,
  kept verbatim in the translation.

## Batch 8 (B08): ch13 (营救任弼时、关向应 / Rescuing Ren Bishi and Guan Xiangying, PDF 263-275, printed 219-231) + ch14 (开拓新局面(上) / Opening a New Chapter (Part 1), PDF 276-295, printed 232-251) — DONE

### Pipeline / recovery
- Body offset constant 44 held; folios 219-251 verified by eye on every opener.
- OCR: ocr_crop.py 263 295 --left 0.11 --right 0.90 --top 0.135 --bottom 0.95
  --lang chi_sim --psm 6 --running-head "隐蔽战线统帅周恩来"; ocr_dual.py in bg.
  Second-read dual OCR was not needed for the fixes (names crop-verified directly).
- Recovery scripts (tracked): scripts/recovery/b08_strip_furniture.py + b08_surgery.py
  + b08_pagemap.py, following the B07 model. Structure rows for ch13/ch13s01-03,
  ch14/ch14s01-03 added to data/structure.json (titles pulled from book.json).
- b08_strip_furniture: normalized 8 garbled headings to exact titles; RESTORE'd
  stray footnote markers (① OCR'd as 包/中/? and two spurious leading 201C quotes),
  ONE embedded-photo caption line dropped (p278 一品香旅社), truncated 7 author-
  footnote blocks. Also RESTORE'd three OCR-dropped sentence-ends that would have
  welded paragraphs: 吴露. (ASCII '.' for 。 at 李沫英 quote end, f231), the dropped
  2-char line 物。 ending the Du Yuesheng bio (f240), and 挡风墙罢了。 (OCR 挡风雯,
  墙罢了。 dropped, crop-verified f241). These three are the B08 form of the
  "OCR drops a short trailing line and merges two paragraphs" disease.
- b08_surgery: re-segmented ch13 into 2(preamble)+8+11+13 = 34 body + 4 headings,
  ch14 into 7+17+20 = 44 body + 4 headings. The ch14 s02 poem (七律) and the 辞海
  block quote are each ONE paragraph. DRY-RUN verified every marker occurs once;
  post-apply verified each ZH para ends in sentence-final punct (the 4 exceptions
  are attribution-intro colons) and starts with its expected phrase.

### Checks (all GREEN)
- verify_unit ch13/ch14: parity 34/44 OK, numbers 0 unresolved, anchors placed.
- check_structure --pairs: parity OK both.
- check_numbers (--noise): after fixing phantom numerals (大十→大雨, 六读→阅读,
  4红旗→《红旗, 万以→乃以) and carrying real values (12点 -> "twelve"; 150 as
  figures) and noising 4 name/place number-glyphs (王老九, 字新三, 百货大楼,
  刘锡五) — 0 unresolved.
- qc_entities: ch13 0 misses, ch14 0 misses (new glossary terms enforced).
- check_align: OK both (median 4.56 / 4.51 en/han). check_content: all in-paragraph
  (fixed 5 ch13 paras to carry "Chinese Communist Party" / "All-China Federation of
  Trade Unions" verbatim). check_register vs ch01: within tolerance both
  (em-dash 0.4 / 3.3 per 1k vs ref 6.0; no sentence over the 2-dash budget).
- qa_epub PASS (28 docs, 206 notes, 231 pagebreaks); epubcheck 0/0/0.

### OCR fixes (data/ocr_fixes.json): ch13 = 57 rows, ch14 = 67 rows
Heavy name garble this batch. 任弼时 alone had 22 OCR variants (任缠时/任强时/任祝时
/任咒时/任绚时/任顷时/任弱时/任大时/…); 关向应 5; 陈琮英 (Ren's wife, 琮 crop-verified
f222) 5; 陈赓 many (陈刻/陈广/陈庆/陈庚/陈鹿 ch13; 陈记/陈委/陈煞/陈广/陈大/陈康/陈钴
ch14 — 陈委/陈煞 crop-verified as 陈赓 on f235, NOT 陈云; 陈养 left alone = 陈养山);
胡鄂公 12 variants; 刘少白 6; 杜月笙 5; 杨登瀛 4; 梅宝玑 3. Plus 瞿秋白, 向忠发,
龚德元/龚饮冰 (奢->龚), 刘鼎 (刘易), 张国焘 (张国春), 王闿运 (王阁运), 孙毓筠,
李燮和, 张勋, 汪大燮, 阎锡山, 纪晓岚, 蔡和森, 何基沣, 殷鉴, 吴景濂, 孔祥熙, and
digit-glyphs ($=5, S=5, 《=4, 乃->万).

### Notes: ch13 = 8, ch14 = 11 (19 new; book total now 206)
Content notes with fact-check verdicts (all corroborated via Wikipedia/standard
biographies, NEVER LLM sources): Ren Bishi bio (1904-1950, youngest of the Five
Secretaries), Guan Xiangying bio (Manchu Gūwalgiya, He Long's commissar, d.1946),
International Red Aid / MOPR, Yang Du (monarchist "Six Gentlemen" -> secret CCP
1929, revealed 1975 via Cihai), Du Yuesheng (Green Gang, Wang Shouhua murder /
April 12), Zhang Xun's 1917 restoration, Cihai, Qi Baishi, Yang Xianzhen (later
"two combine into one" philosopher, denounced 1964). SOURCE-ERROR footnotes (kept
as printed, flagged): "February 30, 1929" (impossible date); Yang Du "1920" in
Japan (body contradicts the same chapter's Cihai entry, 1902 — correct); "Nanjing
Uprising" rendered as printed (see below). AUTHOR'S NOTES reproduced (tagged
"Author's note."): the two long explanatory footnotes on 政学系 (Political Study
Clique) and the 改组派/西山会议派 (Western Hills Conference faction, 14 names), and
6 source-citation footnotes (任弼时传; 周朴农 难忘的三十九天; 张纪恩; 李沫英; 尹骐
潘汉年的情报生涯; 王冶秋 难忘的记忆).

### Reading uncertainties / source facts for the read-through
- ch13: "1929年2月30日" (Feb 30) is an impossible date, printed as-is, footnoted.
- ch14: the body's "1920年去日本留学" for Yang Du is a source error — the Cihai
  entry it quotes gives 1902, and Yang Du in fact went to Japan in 1902; kept as
  printed, footnoted.
- ch14: "南京起义" (Nanjing Uprising), where Mei Zhonglin was killed, is almost
  certainly a misprint for the Nanchang Uprising (Aug 1927); rendered "Nanjing
  Uprising" as printed. (Not footnoted separately — low-stakes; flagged here.)
- ch14: the author's ② footnote nominally attached to 改组派 (Reorganizationists)
  actually describes the 西山会议派 (Western Hills faction); reproduced faithfully
  as the author wrote it.

### NOT re-noted (already placed earlier; cross-referenced, not repeated)
April 12 coup / White Terror (ch00), August 7 Conference / Mixed Court / Wang Ming
/ Pavel Mif / Fourth Plenum of the Sixth CC (ch02), Communist University of the
Toilers of the East (ch04), The Guide (ch01), New Youth, May Thirtieth (ch08/ch11),
Comintern (ch01), Green Gang (ch00), concession police (ch01/02/09), Ke Lin (ch04),
Gu Shunzhang (ch00+), the traitor Bai Xin (ch11/ch12).

### Glossary: 31 rows added (nested into people/organizations/places/works)
New people: 刘少白 Liu Shaobai, 梅宝玑 Mei Baoji, 章士钊 Zhang Shizhao, 黄金荣 Huang
Jinrong, 张啸林 Zhang Xiaolin, 胡汉民 Hu Hanmin, 王闿运 Wang Kaiyun, 周朴农 Zhou
Punong, 柳湜 Liu Shi, 余昌生 Yu Changsheng, 李沫英 Li Moying, 郭亮 Guo Liang,
梅龚彬 Mei Gongbin, 梅中林 Mei Zhonglin. Orgs: 中国互济会 China Mutual Aid Society,
政学系 Political Study Clique, 改组派 Kuomintang Reorganizationists, 筹安会 Peace
Planning Society, 反帝大同盟 Anti-Imperialist League, 顺直省委 Shun-Zhi provincial
committee, 中华共进会 China Mutual Advancement Society, 中国民权保障同盟 China League
for the Protection of Civil Rights, 中国自由大同盟 China Freedom League. Places:
提篮桥监狱 Tilanqiao Prison, 龙华 Longhua. Works: 辞海 Cihai, 红旗 Red Flag, 大公报
Ta Kung Pao, 泰东日报 Taidong Daily, 君宪救国论 "Saving the Nation Through
Constitutional Monarchy". REUSED unchanged: 任弼时, 关向应, 陈赓, 陈养山, 陈琮英,
周恩来, 顾顺章, 杨登瀛, 刘鼎, 柯麟, 李维汉, 康生, 陈云, 杨度, 胡鄂公, 杨献珍,
杜月笙, 张国焘, 王根英, 潘震亚, 何维道, 张纪恩, 冯玉祥, 孔祥熙, 蔡和森, 李大钊,
袁世凯, 汪精卫, 恽代英, 杨虎, 米夫, 王明, 国际济难会, 上海大学, 淞沪警备司令部.

### noise.txt additions (this batch)
王老九 (nickname, 九), 字新三 (courtesy name, 三), 百货大楼 (department store, 百),
刘锡五 (name, 五). Extend, do not prune.

### Figures
ch14: 1 figure (data/figs/ch14_yipinxiang.png, the 一品香旅社 hotel photo, p278
folio 234), placed before the "In leading the work of the Central Special Section"
paragraph. ch13: no figures (every page eyeballed; find_figures found none).

---

## B09 — ch15 (Opening a New Chapter, Part 2) + ch16 (Part 3)

ch15 = 75 body paragraphs, 3 sections (贡生—省议员—开明绅士刘少白 / 牧师和律师 /
向新闻界发展), 19 notes, 1 figure (Mao's reply-letter facsimile, p305 folio 261).
ch16 = 42 body paragraphs, 3 sections (淞沪警备司令部 / "第四号政治密查员" /
英法租界巡捕房), 8 notes, 1 figure (Longhua garrison photo, p322 folio 278).
Both full-page image pages (p305, p322) sit mid-paragraph; emptied before assemble,
the spanning paragraph rejoined across the gap.

### Checks run and what they found
- verify_unit / check_numbers (--noise data/noise.txt): 0 unresolved both units.
  Real garbles fixed in ZH (carried real values in EN): 东北千->东北军, 博十->博古,
  张家11->张家口 (口 OCR'd as 11), 七-五->七一五, 赏格$万->5万, 19495->1949,
  刊登4寻人->《寻人 (《 OCR'd as 4), 好吧!1->好吧! (stray 1). Phantom-numeral noise
  added: 三一八, 五原, 三教九流, 十足, 千里香, 三友实业社, 百里, 50年代.
- check_align: OK both (median 4.86 / 4.93 en/han, no pair >2.2x).
- check_structure --pairs: parity OK (75/75, 42/42).
- check_register --ref out/ch01_reading.md: within tolerance both (em-dash 0.4 and
  0.8/1k vs ref 6.0 — dash-glosses avoided per STYLE).
- qc_entities: ch16 clean; ch15 ONE reported miss = 曾三 (Zeng San), a FALSE
  POSITIVE: the substring 曾三 sits inside 他曾三去延安 ("he went three times to
  Yan'an", 曾 = aspect adverb + 三去). Not the person. Documented, not a defect.
- check_content --config data/check_config.json (ch15/ch16 added to docs+sources):
  ch16 all-in-paragraph; ch15 only the same 曾三 false positive.
- apparatus / check_apparatus: 0 failures. qa_epub PASS (61 files, 233 notes).
  epubcheck (5.1.0): 0 fatals / 0 errors / 0 warnings.
- Tail verification (rule 4 corollary): final paragraphs of both units read against
  the scan (p320, p332) — faithful.

### OCR-fixes ledger (data/ocr_fixes.json) — ch15/ch16
Heavy name garble again. ch15: 陈赓 (陈刻/陈钴/陈庆/陈废/陈六/陈广), 刘少白
(刘少上/刘少百/刘少日/刘少和白), 陈志皋 (陈志举/尝/皖/果/浴/捍), 阎锡山 (移/净/冰锡山),
傅作义 (传/健作义), 王若飞 (王耕/春/者飞), 绥远 (组远), 董健吾/浦化人 kept,
汉玉祥->冯玉祥, 李一谍/李一让->李一氓, 任缠时/任弦时->任弼时, plus the numeric
garbles above. ch16: 宋再生 (宋绸生/上绸生/捍生), 熊式辉 (能式辉/元辉), 熊天翼
(能天辟/必), 蒋方震 (萝方震), 范广珍 (范三珍), 陆连奎 (陆连奈), 韩复榘 (韩复策/扔/圩复),
薛耕莘 (薛耕革), 朱岑楼 (朱专楼). Replay with apply_fixes.py after any clean regen.

### 刘鼎 (Liu Ding), NOT "刘易"
HANDOFF (B08) listed a settled "刘易 Liu Yi"; that was imprecise. The 情报科副科长
who liaised with 董健吾 and appears in ch16's closing roster is 刘鼎 (Liu Ding) —
crop-verified on p309 and p332. The glossary already had 刘鼎 = Liu Ding; kept.
OCR "刘易" corrected to 刘鼎 in ch15/ch16 ZH.

### Shelf drift flagged for the whole-book reconciliation (NOT fixed here)
The glossary's decided EN forms were used this batch, but earlier chapters drift:
晋绥 = "Shanxi-Suiyuan" (glossary) vs 2 stray "Jin-Sui" in earlier units; 军统 =
"Juntong" (glossary) vs 3 "Military Statistics Bureau"; 同盟会 = "Tongmenghui" vs
1 "Revolutionary Alliance". Reconcile at book's end.

### Renderings settled (glossary.json is the ledger)
People added: 董健吾 Dong Jianwu (董贤武 Dong Xianwu; 王牧师 Pastor Wang; 周二胖子
"Fat Zhou the Second"), 浦化人 Pu Huaren, 宋再生 Song Zaisheng (宋启荣 Song Qirong /
宋启华 Song Qihua "Young Song"; "老宋" Old Song), 熊式辉 Xiong Shihui (天翼 Tianyi),
钱大钧 Qian Dajun, 蒋方震 Jiang Fangzhen (蒋百里 Jiang Baili), 陈志皋 Chen Zhigao,
黄定慧 Huang Dinghui (黄慕兰 Huang Mulan), 傅作义 Fu Zuoyi, 王若飞 Wang Ruofei,
潘汉年 Pan Hannian, 范广珍 Fan Guangzhen, 刘亚雄 Liu Yaxiong, 蔡麻子 Pockmarked Cai,
巴和 Baihe (French lawyer), 陈养山 (reused), and the ch16 martyr roster (罗亦农
Luo Yinong, 彭湃 Peng Pai, 陈延年/陈乔年 Chen Yannian/Qiaonian, etc.). Orgs: 南华通讯社
Nanhua News Agency, 新四川通讯社 New Sichuan News Agency, 复兴社 Renaissance Society,
世界与中国杂志社 World and China Magazine society. Works: 西行漫记 Red Star Over China,
京报 Jing Bao, 文化周报 Cultural Weekly, 徐州日报 Xuzhou Ribao, 晋绥日报
Shanxi-Suiyuan Daily. Places: 龙华寺 Longhua Temple, 龙华兵工厂 Longhua Arsenal.
REUSED unchanged: 刘少白, 杨献珍, 胡鄂公, 陈赓, 顾顺章, 杨登瀛, 刘鼎, 李强, 李维汉,
任弼时, 关向应, 白崇禧, 康生, 阎锡山, 冯玉祥, 淞沪警备司令部, 龙华, 红队, 军统.

### NOT re-noted (already placed in earlier chapters)
Green Gang, Feng Yuxiang, Zhang Xueliang, Ren Bishi, Guan Xiangying, Gu Shunzhang,
Du Yuesheng, Wu Hao (the alias; the Notice affair IS newly noted here), Peng Pai
(cross-ref in the martyr note), Kang Sheng (his 1947 land-reform role newly noted),
Yan Xishan, Li Lisan, Li Weihan, Longhua (the garrison/martyrs newly noted),
Bai Chongxi, International Settlement (the 英租界 anachronism newly noted).

### noise.txt additions (this batch)
三一八 (March 18 massacre), 五原 (Wuyuan), 三教九流 (idiom, 九), 十足 (idiom),
千里香 (wine name), 三友实业社 (company), 百里 (Jiang Baili), 50年代 (decade). Extend,
do not prune.

### Figures
ch15: data/figs/ch15_mao_letter.png (Mao's handwritten reply to Liu Shaobai, p305,
folio 261), placed before "In 1947, while Liu Yaxiong was working in the Northeast".
ch16: data/figs/ch16_longhua.png (the Longhua garrison-command gateway, p322, folio
278), placed before "At that time the Kuomintang's Songhu Garrison Command stood
north". Both captions mark labels as the source's, caption as the translator's.

## B10 — ch17 (电讯科长"曾培鸿"——李强 / Communications Chief "Zeng Peihong" — Li Qiang) + ch18 (永不消逝的红色电波 / The Red Airwaves That Never Die)

Scope: ch17 PDF 333-363 (printed 289-319), 5 sections, 74 body paragraphs;
ch18 PDF 364-388 (printed 320-344), a chapter-opener plus 4 sections, 59 body
paragraphs. Body offset constant 44, folio-verified at both openers by eye.

Pipeline: render 333-388 at 300 dpi; ocr_crop --left 0.11 --right 0.90 --top
0.135 --bottom 0.95 --lang chi_sim --psm 6 (pgrep tesseract 0 after). Assembly
via the b10_* recovery scripts (follow b09): b10_strip_furniture.py normalizes
the 11 headings, empties the SEVEN figure/facsimile pages, truncates the author
footnote blocks, and RESTORES six OCR-mangled sentence-ends that would defeat the
surgery snap (归案迅办、->。 ; 高超的机务技术- ->。 ; 前文已经讲过) missing 。 ;
表示感谢① OCR'd as 9 ; 满怀地写道: dropped ; 必据毛齐华 for 。另据). structure.json
rows added; indents.py; assemble.py --offset 44; b10_surgery.py --apply
(ch17 74, ch18 59, all markers unique/in order); apply_fixes.py; b10_pagemap.py.
NOTE: indent geometry is unreliable in this batch (scanner skew flags whole
blocks), so paragraph boundaries were read off the page images directly.

Checks all green: parity (74/74, 59/59), verify_unit numbers 0 unresolved,
check_align OK, qc_entities 0 misses (one 国民党 and one 上海 fixed by naming),
check_content all in the paired paragraph (fixed T.V. Soong spacing and the KUTV
form to the shelf's "Communist University of the Toilers of the East"),
check_apparatus clean, qa_epub PASS (19/28 chapters, 259 notes, 319 pagebreaks),
epubcheck 0/0/0, check_register within tolerance (em-dash 4.1/2.4 vs ref 6.0).

### OCR-era garbles fixed (data/ocr_fixes.json ch17/ch18), all crop-verified
Number garbles: $=5 (功率$0瓦, 训练$名, 5$0名, 7元5$角); 万=瓦 (输出功率100万);
上/工=1 (1930年上月, 2月工日); 士=十 (第二士八师); dropped/added digit (193年底
->1930, 19%31->1931, 1月?28日). Name garbles: 冯文彬 (OCR 当文彬), 王诤 (王净/王将),
公秉藩 (公时/公肝藩), 冯文彬. Char garbles: 纱三->纱厂, 工三->工厂, 车合成十->革命战士,
党外人十->党外人士, 四惧->畏惧, 埋头苦二->埋头苦干, 闸二同志->曾三同志, 六上二团->
六十二团, 福申路->福煦路. Folio 311 leaked into a body paragraph (removed); QRC?7->QRC?.

### noise.txt additions (place/idiom/name numerals, longest-first)
20世纪80年代, 十字路口, 十二时许, 千里眼, 四成里, 四盛里, 万国, 万汐烛, 万能, 百般,
百色, 两位先生, 零件, 感慨万端 (ch17); 成千上万, 第三国际, 二房东, 三房客, 百货公司,
零工, 7元5角 (ch18).

### Figures (7; find_figures found 6, the p356 letter facsimile cropped by hand)
ch17: p0334-f1 (Li Qiang portrait, "李强在工作中"), p0341-f1 (first-station site,
福德坊32号), p0356-f1 (Li Qiang's 1980 letter to Mu Xin, facsimile), p0358-f1
(Mao's calligraphy inscription for the radio workers), p0362-f1 (1945 Yan'an
group photo: Wu Yunfu, Wu Shaozu, Tu Zuochao / Zeng San, Wang Zigang, Wang Zheng).
ch18: p0382-f1 (Tu Zuochao portrait), p0385-f1 (Li Xiangwu portrait).

### Notes (26): 11 ch17 + 15 ch18, at first appearance book-wide
Author-note citations reproduced at the ① anchor (Li Qiang's memoir, the
《红军的耳目与神经》 collection, Snow's Red Star). NOT re-noted (already placed in
earlier chapters): May Thirtieth, April 12, White Terror, Long March, Red Star
Over China, Whampoa, Cheka, the encirclement campaigns, Gu Shunzhang, Central
Special Section, Songhu Garrison Command, Sun Yat-sen (person), Pan Hannian
(ch15). New notes cover: Li Qiang/曾培鸿 homophone + career, Bose/Longzhou
uprisings, the Southern Bureau, Marconi, Shen Bao, Zhang Huizan, Mao's
千里眼顺风耳 phrase, the QRC Q-code, Cai Shuhou, Xia Yan, the Comintern China
group, Seeckt, Sorge, the "mysterious foreigner case", Tang Enbo, the Pan-Yang
case, Kunlun Film Co., KUTV, Sun Yat-sen University (Moscow), Frunze school,
the Hao cipher, the December 12 (Xi'an) Incident.

### B10 fact-check verdicts (Wikipedia / Baidu Baike / BIT archives, no LLM)
CORROBORATED: Li Qiang (orig. name 曾培洪, built first CCP transmitter 1929, CAS
academician 1955, Minister of Foreign Trade); Richard Sorge (Shanghai 1930-32,
Red Army Fourth Dept, Tokyo ring, hanged 1944); Zhang Huizan (18th Div, captured
at Longgang 30 Dec 1930, executed 28 Jan 1931, head to Ji'an); the Hao cipher
(豪密, devised by Zhou Enlai from his alias Wu Hao, one-time-pad, unbroken to
1949); Hans von Seeckt (Chiang's chief adviser 1933-35, blockhouse strategy);
the Bose/Longzhou uprisings under Deng Xiaoping (alias Deng Bin); the Xi'an
Incident (12 Dec 1936). UNCERTAIN: "Lawrence"/the mysterious-foreigner case
(agent's true identity not settled) — noted as such.

### Fact-check verdicts (in the notes; sources: Wikipedia / Baidu Baike, no LLM)
CORROBORATED: Snow/Red Star & Pastor Wang = Dong Jianwu; Dong Jianwu (Datong
Kindergarten, sheltered Mao's sons); the Wu Hao Notice forgery + French-lawyer
counter-notice; the Longhua martyrs & several-thousand scale (caveat: 1927 dead
Zhao Shiyan/Chen Yannian sourced only as "Shanghai" outside PRC); Fu Zuoyi; Wang
Ruofei (Heichashan crash 1946); Jiang Baili; No. 76; the Yang Fan case; Han Fuju;
Kang Sheng & the Jin-Sui land-reform excesses (caveat: Mao rebuked the leftist line
generally, did not blame Kang at the time); Yan Xishan.

### Setup note
setup.sh regression test "hook stands down on template stub" FAILS (pre-existing
template-maintenance stub, does not affect real batches) — all other checks green.

---

## B11 — ch19 (Averting a Catastrophe: Gu Shunzhang's Defection) + ch20 (Betrayal to the Last Scrap)

Complete. ch19 = 42 body paras, chapter title + 3 sections (s01 22, s02 7, s03 13),
9 notes, 0 figures. ch20 = 64 body paras, chapter title + 4 sections (s01 19,
s02 16, s03 20, s04 9), 12 notes, 0 figures. Both chapters are pure narrative:
find_figures empty, char-counts show no plate pages, section-opener images
eyeballed (p406/p413/p418) — figure list EMPTY as a deliberate decision.

### Pipeline / checks (all green)
- OCR: ocr_crop 389-428, chi_sim psm6, crop 0.11/0.90/0.135/0.95, running-head
  stripped; pgrep tesseract 0 after. ocr_dual for the disagreement filter.
- Assembly (b11_strip_furniture / b11_surgery / b11_pagemap / b11_rebuild.sh,
  following the b10 model). ch19 title prints on TWO OCR lines (em-dash break) —
  merge_ch19_title() special-cases it. All 7 section headings normalised (p398,
  p418, p425 were already exact). Paragraph boundaries read off the images; full
  surgery re-segmentation (assemble under-segments as always).
- verify_unit: parity 42/64, numbers 0 unresolved, anchors 9/12 ok.
- qc_entities 0 misses; check_align OK; check_content all-in-paired-paragraph;
  check_structure parity OK; check_register within tolerance (em-dash 3.9/3.3 per
  1k vs the ch01 ref 6.0). check_apparatus 0 failures. qa_epub PASS; epubcheck
  0 fatals/0 errors/0 warnings. EPUB now 21 of 28 chapters (ch00-ch20), 280 notes.

### Surgery boundary traps fixed (the "split/merge keeps the count right while
shifting content" hazard — caught by qc_entities/check_numbers, not parity)
- p417 施滉等4人。: the period OCR'd as a comma, welding S2P13's tail into S2P14
  (also 施涡→施滉). RESTORE'd in the strip.
- p411 搭民船回来。①: the block-quote's closing 。① OCR'd as a dash, so the snap
  pulled the "周恩来立即安排" sentence into the next paragraph. RESTORE'd.
- Leading ① of a block quote read as "9" and welded to the next paragraph start
  (91931→1931, 9蔡→蔡); trailing ① read as 中 (在于此。”中). Fixed via ocr_fixes.

### OCR-fix ledger (data/ocr_fixes.json: ch19 50, ch20 71) — highlights
Systematic name garbles corrected: 张国焘 (7 variants), 恽代英 (21 variants!),
蔡和森 (18), 向忠发 (3), 陈琮英 (was OCR'd 陈玉英/陈院英 throughout — Ren Bishi's
wife, ONE person), 顾顺章, 周恩来, 瞿秋白, 陈赓, 蔡孟坚, 何成濬, 熊式辉, 陈绍禹,
邹韬奋, 谢云巢, 王竹樵, 鄂豫皖 (8 variants). Number/marker garbles: $=5 (第5天,
刑字5237号, 生活费50元), 丸=九 (Shen Bao clip time), 刘夭千 phantom 千 (=刘杞夫),
poem 患/事, 第二大=第二天. NOTE 张国栋 is a DIFFERENT person (Zhang Guodong, the
CI memoirist) — NOT merged with 张国焘.

### noise.txt additions (genuine non-quantities; longest-first)
千秋 (a thousand autumns, poem idiom); 半百 (near/past fifty, idiomatic age);
三刻 (九点三刻 = a quarter to ten, clock time); 胡说八道 (talk nonsense idiom);
六安 / 七里坪 (place names with a numeral char); 星期六 (Saturday); 第二天 (next
day, relative-time idiom); 十万火急 (desperately urgent idiom).

### Crop-verified obscure names (read on the scan)
钱椒椒 Qian Jiaojiao (Qian Zhuangfei's daughter, Liu Qifu's wife); 孟真 Meng Zhen
(the CI Fourth-Section chief who wrote the 《特务大师顾顺章》 piece); 刘杞夫 Liu
Qifu (Qian's son-in-law/courier; source also writes 刘藉千/刘夭千); 陈琮英 Chen
Congying; 施滉 Shi Huang; 黄玠然 Huang Jieran; 曾洪易→赣东北 (northeast Jiangxi).

### Glossary (added 58 rows nested into people/organizations/works, en+pinyin+
status). Most principals already on the shelf (顾顺章/周恩来/张国焘/恽代英/蔡和森/
向忠发/杨登瀛/鲍君甫/米夫/王明/熊式辉/蔡孟坚/王竹樵/刘杞夫/黄玠然 etc.). New:
沈泽民/张琴秋/夏曦/曾洪易/杨庆山/何成濬/张冲/顾建中/张长根/尤崇新/孟真/张国栋/钱潮/
欧阳大汉/朱月倩/霍步青/秦邦宪/黄负生/吴玉章/张治中/杨昌济/罗学瓒/蔡元培/葛健豪/秋瑾/
蔡畅/蔡庆熙/李一纯/向警予/曾国藩/邓发/陈济棠/施滉/黄静汶/谢云巢/叶耀明/王震南/王作林/
布哈林/叶荣生/曹炳生/鲍文蔚/吴醒亚/吴汉祺/罗瑞卿/周佛海/李熙元/王思诚/钱椒椒/侯如史/
杨邨人, plus orgs (少年中国学会/利群书社/互助社/新民学会) and works (东方杂志/向导/
申报). SHELF form held: 中统 = "Zhongtong" (NOT my first-draft "CBIS" — reverted
to match the 6 prior uses; already footnoted in ch07).

### NOT re-noted (already placed in earlier chapters; cross-referenced)
Gu Shunzhang (ch09), Zhang Guotao (ch01/05), Wang Ming + Mif (ch02), Yun Daiying
(ch02), Cai Hesen (ch11), Xiang Zhongfa (preface), Yang Dengying/Bao Junfu (ch06),
Qian Zhuangfei + Longtan Three (ch04/05), Zou Taofen (ch07), Whampoa (ch03),
Songhu Garrison (ch02+), Xu Enzeng (ch05/07), Cai Mengjian (ch05), Xiong Shihui
(ch11/16), Zhongtong (ch05-09). Minor discrepancies left unnoted (tier named in
STYLE): the source dates Cai Hesen's death only to "shortly after" the 10 June
arrest — the note supplies the independent 4 August 1931.

### B11 fact-check verdicts (in the notes; Wikipedia / Executed Today / academic
research notes; NO LLM/Grokipedia)
CORROBORATED: Gu Shunzhang's defection (arrested Hankou 24 Apr 1931, defected,
Qian Zhuangfei's warning telegram to Zhou Enlai 25 Apr, the emergency evacuation);
Yun Daiying executed Nanjing 29 Apr 1931 after Gu's confession; Xiang Zhongfa
(only CCP general secretary to defect — arrested 22 June, confessed, shot 24 June
1931 before Chiang's stay arrived); the Longhua martyrs (7 Feb 1931, ~24 dead,
incl. the Five Martyrs of the Left League: Rou Shi/Hu Yepin/Yin Fu/Feng Keng/Li
Weisen[Li Qiushi]); Cai Hesen betrayed at the HK seamen's meeting 10 June 1931,
extradited to Chen Jitang, executed Guangzhou (independent record: 4 Aug 1931),
aged 36. CAVEAT stated in the note: the manner of Cai Hesen's execution (limbs
nailed to the wall, chest bayoneted) is the Communist account and is NOT
independently corroborated. Author's notes reproduced for the 王竹樵/尤崇新
informer dispute, the 抄靶子 term, and the block-quote sources (Cai Mengjian's
Taipei memoir; Zhang Guotao's My Recollections; A Life of Yun Daiying).

## B12 (ch21 A Vicious Manhunt Part 1 + ch22 A Vicious Manhunt Part 2)

Both chapters complete. ch21 = 104 body paragraphs across 2 sections (s01 派特务
追捕陈赓 = 80 paras, s02 魔手伸进王根英的娘家 = 24), 11 notes, 2 figures. ch22 = 47
body paragraphs (s01 秘密绑架丁玲 = 26, s02 参与暗杀杨杏佛 = 21), 10 notes, 2
figures. The manhunt after Gu Shunzhang's defection: the pursuit and 24 March 1933
arrest of Chen Geng at the Beijing/Lido Theatre, his refusal of Chiang Kai-shek's
personal inducements at Nanchang and escape through Song Qingling's intervention
(late May 1933); the raid on his wife Wang Genying's family, her three years in
the Model Prison and Xiaozhuang reformatory (the Noulens hunger strike), Zhou
Enlai's freeing her in August 1937, and her death in battle 8 March 1939; the
secret abduction of Ding Ling with Pan Zinian (14 May 1933, Ying Xiuren killed),
her three years in Nanjing and escape to Bao'an, rehabilitated 1984; and the Blue
Shirt/Juntong assassination of Yang Xingfo (18 June 1933) of the China League for
the Protection of Civil Rights.

### B12 checks (all green)
verify_unit ch21/ch22: parity 104/47, numbers 0 unresolved, anchors 0 ok.
check_align: OK (median 4.24 / 4.38 en/han, no pair strays >2.2x). qc_entities:
CLEAN both (after settling Song Qingling and concession-police forms). check_content:
all name occurrences in the paired paragraph (369 ch21, 260 ch22). check_register
vs ch01: within tolerance (em-dash 3.4 / 3.9 per 1k vs the reference's 6.0).
check_apparatus: 0 failures. qa_epub: PASS (301 notes, 407 pagebreaks). epubcheck
5.1.0: 0 fatals / 0 errors / 0 warnings.

### B12 renderings settled (glossary; 85 new rows this batch)
SHELF DECISION FOLLOWED: 宋庆龄 = "Song Qingling" (authority.json / huang-mulan),
NOT "Soong Ching-ling" (translation reworded to match). Held: 巡捕房 = concession
police, 中统 Zhongtong, 军统 Juntong, 复兴社 Renaissance Society (= Blue Shirts /
蓝衣社), 中国民权保障同盟 = China League for the Protection of Civil Rights, 大公报 =
Ta Kung Pao, 大美晚报 = Da Mei Wan Bao, 申报 = Shen Bao, 打狗队 = Dog-Beating Squad.
New principals: 陈赓 Chen Geng (lead), 丁玲 Ding Ling, 杨铨/杨杏佛 Yang Quan/Yang
Xingfo, 王根英 Wang Genying, 邓文仪 Deng Wenyi, 谭国辅 Tan Guofu, 沈醉 Shen Zui,
戴笠 Dai Li, plus the full League/press/rescue cast (see glossary people/orgs/
places/works). REMOVED two false-matching glossary keys: 同盟会 (matched inside
同盟会员) and 时报 "Shi Bao" (matched inside 当时报纸); neither is used as a real
entity anywhere in ch00-22.

### B12 NOT re-noted (already placed earlier, cross-referenced)
Zhongtong / Juntong (ch05-09), concession police / 巡捕房 (ch01+), Comrade /同志
(ch01), Whampoa (earlier), International Settlement / Concessions (ch01+),
Nineteenth Route Army (earlier), Second Eastern Expedition (context supplied in the
Chen-Geng-saved-Chiang note), Gu Shunzhang / the defection (ch19), Deng Xiaoping,
White Terror, Central Special Section. Minor low-stakes discrepancies left unnoted
(tier named in STYLE).

### B12 fact-check verdicts (in the notes; WebSearch Wikipedia / academic; NO
LLM/Grokipedia)
CORROBORATED: Chen Geng arrested at the Beijing/Lido Theatre 24 March 1933, taken
to Nanchang, refused Chiang, escaped ~a month later with Song Qingling's help;
Ding Ling abducted from the International Settlement 14 May 1933, held in Nanjing,
escaped 1936 via Feng Xuefeng to Bao'an, rehabilitated by the 1984 Central
Committee resolution; Yang Xingfo (secretary-general of the China League for Civil
Rights) shot dead 18 June 1933 by the Blue Shirts on Chiang's order; the Blue
Shirts / Renaissance Society (founded April 1932, Whampoa core, Chiang head); Hu
Yepin among the Five Martyrs of the Left League (Longhua, 7 Feb 1931); Wang Genying
killed at Nangong 8 March 1939. CONTRADICTED IN PART: the Noulens couple. The book
calls them "Poles"; "Hilaire Noulens" was in fact Jakob Rudnik, a Soviet
(Ukrainian-born) Comintern liaison agent (wife Tatiana Moissenko), and contrary to
the book they were NOT freed after the prison hunger strike but only in 1937
(death sentence commuted to life). The note states this. Author's notes reproduced
for the block-quote sources (Yang Zhihua/Du Ning; Edgar Snow; China Forum; Xinhua's
Ding Ling obituary; Ding Ling's own Wangliang shijie memoir; Shen Bao; Epstein's
Soong Ching Ling) and the two author bio-notes for Pan Zinian and Ying Xiuren.

## B13 (ch23 Concealment/Withdrawal/Relocation + ch24 The Traitor Gu Shunzhang's Shameful End)

DONE end to end. ch23 = 101 body paragraphs, 6 sections, 14 notes, 3 figures;
ch24 = 63 body paragraphs, 4 sections, 8 notes, 1 figure. All checks green.

### Scope
- ch23 (PDF 485-526, printed 441-482): the orderly retreat of the apparatus after
  Gu Shunzhang's defection. Special Committee reshuffled, Special Section
  reorganized under Chen Yun (s01); Chen Geng and Chen Yangshan work Tianjin then
  are withdrawn (s02); Li Qiang barred by Wang Ming from KUTV, becomes a Soviet
  radio expert, returns 1937 (s03); the "Three Heroes of Longtan" to the Central
  Soviet, Qian Zhuangfei lost on the Long March 1935, Hu Di murdered by Zhang
  Guotao 1936, Li Kenong (s04); Liu Ding's arrest, release, capture at Yiyang,
  escape, Smedley/Alley, Xi'an (s05); Zhou Enlai's route Shanghai->Shantou->Dapu->
  Ruijin, late 1931 (s06).
- ch24 (PDF 527-552, printed 483-508): Gu Shunzhang the hunted traitor and the
  1931 wanted-order signed by Mao (s01); his worsening betrayal, the surrender
  policy, the spy-training classes, the Zhongtong/Juntong tug-of-war (s02); the
  fawning book he ghost-wrote, The Theory and Practice of Secret-Service Work, in
  which he betrayed the Special Section's structure (s03); his execution by Xu
  Enzeng, ~1935 at Suzhou, told through four conflicting agent memoirs (s04).

### Checks (all pass)
- parity 101/101 and 63/63 (check_structure).
- verify_unit ch23/ch24: anchors ok (14 / 8), numbers clean.
- check_numbers --noise: 0 unresolved both. Extended data/noise.txt (nine idioms/
  measure forms: 九牛二虎, 五角形, 曾传六, 一再, 千瓦, 濮备九, 化整为零, 一同,
  最后一期, 1个多月, 十多万, 十亚不赦, 1/10, [0-9]+年代, parenthesized CJK ordinals).
- qc_entities: 0 misses both. check_content --config: OK all units.
- check_align OK (ratio 4.33 / 4.37). check_register --ref ch01: within tolerance
  (em-dash 4.8 / 6.1 per 1k vs ref 6.0).
- qa_epub PASS (28 docs, 323 notes, 470 pagebreaks); epubcheck 0/0/0.

### Real errors the checks surfaced and fixed
- 陈康 was NOT a separate person: both occurrences are Chen Geng (OCR 赓->康). Folded
  to 陈赓 (removed the stray glossary row).
- 陈庆斋 (Chen Qingzhai) was wrongly folded by a too-broad 陈庆->陈赓 in ch24; removed.
- 张国栋 is Zhang Guotao (张国焘) in ch23s04 but a REAL different person Zhang Guodong
  (张文) in ch24: the 张国焘 fold list is ch23-only (per-unit NAMES), so ch24 keeps 张国栋.
- 第二次国内革命战争 mistranslated "Third" -> "Second" (number check).
- 万吨水压机 -> "10,000-ton" (figures per STYLE).
- Pan Hannian / Tianjin dropped in two paragraphs (qc_entities), restored.

### OCR-era digitization glitches LISTED (rendered to plain sense; only genuine
reading uncertainty footnoted)
- Note-ref circled-1 markers OCR'd as trailing digits (.0 / 9) at quote ends; the
  book-title bracket 《 as 4; 1/10 as 1710; 乌克兰人 as 乌克三人; 193$ / 193S as 1935;
  骨干 as 骨二. All corrected via data/ocr_fixes.json (crop/context verified).
- Pervasive name mangles de-mangled: 陈赓 (~15 forms), 刘鼎 (~11), 张国焘 (8),
  蒋介石, 顾顺章, 徐恩曾, 陈养山, 周恩来, 李一氓. Canonical hanzi restored so
  qc_entities passes.

### Source errors footnoted (kept as printed)
- Alma-Ata called "capital of Uzbekistan" (it was the Kazakh SSR's). Footnoted.

### Fact-check verdicts (in the notes; WebSearch Wikipedia/academic; NO LLM/Grokipedia)
CORROBORATED: Chen Yun took over the Special Section 1931 (later PRC economic
architect); Fang Zhimin founded the northeast-Jiangxi / Min-Zhe-Gan soviet,
captured Jan 1935, wrote Beloved China in Nanchang prison, executed 6 Aug 1935;
Agnes Smedley (US journalist, Comintern circles, d. 1950); Rewi Alley (New
Zealander, Shanghai fire-brigade inspector, sheltered Communists, Gung Ho founder);
Qian Zhuangfei's Long March death spring 1935 attested in outline (Meiliangkeng
manner a 1985 reconstruction); Hu Di killed Sept 1936 on Zhang Guotao's orders;
C.C. clique = Chen Guofu/Chen Lifu faction controlling the Zhongtong. UNCORROBORATED:
the Zhongtong charge that Gu Shunzhang had resumed Communist contact (author argues
it is internally inconsistent). Author's notes reproduced for the block-quote and
memoir sources (Du Ning/Yang Zhihua; Chen Yangshan; Wu Chengfang; the Chen Yun
Chronicle; Li Yimang's Blurred Screen x2; the Xifeng investigation report; the
Liu Ding People's Daily obituary; Huang Ping's Recollections; Dick Wilson; Zhang
Wen; the Zhongtong Lackey; Lin Jinsheng; the "Master of Secret-Service Work"; Chen
Weiru).

### NOT re-noted (already placed earlier in the book; cross-referenced)
White Terror, Central Special Section, Red Squad, Three Heroes of Longtan, Wu Hao,
Li Lisan line, Fourth Plenum, Xiang Zhongfa, Kang Sheng, Pan Hannian, Wang Ming,
Ruijin, Central Soviet, Chinese Eastern Railway Incident, September 18 / Mukden /
Marco Polo Bridge Incident, Zunyi Conference, Long March, Zhang Guotao, Feng
Yuxiang, Xi'an Incident, Chiang Kai-shek, Whampoa, GPU, Cheka, Dog-Beating Squad,
Kuomintang, Zhongtong, Juntong, concession police, Songhu Garrison Command.

### Assembly (b13_* recovery scripts, the current model)
Furniture strip switched to a robust LINE-BASED foot-citation peeler (this batch had
~31 foot citations, several glued to the last body line with no blank). Three photo
plates (Smedley p517 top, Rewi Alley p520 top, Zhou's Ruijin office p523 foot) and
one hand-drawn diagram (Gu's Second-Branch network, p543 mid-page, which
find_figures MISSED as line art) stripped from the body and reproduced as figures.
Surgery markers written in clean text against the same-length de-mangle map.

## B14 (FINAL) — ch25 Wu Hao Notice + ch26 Conclusion + ch27 Afterword; book COMPLETE

ch25 (《伍豪启事》的出笼与破灭, printed 509-525, 3 sections, 52 body paras, 8 notes,
2 figures): the KMT's Feb 1932 forged "Wu Hao and Others Withdraw from the CP"
notice (Zhang Chong + Huang Kai of the Investigation Section); Chen Yangshan's 1951
interrogation of Huang Kai; the Provisional Central Committee's rebuttal (the Party's
own Wu Hao Notice in Struggle #4; Mao's Central Government Proclamation; Barrister Ba
He's notice for "Zhou Shaoshan" via Pan Hannian/Huang Mulan/Chen Zhigao); and the
1967-1980 reckoning after Jiang Qing and the Gang of Four weaponized the forgery,
through Zhou's, Mao's, Kang Sheng's, Xie Fuzhi's, and Chen Yun's statements, Zhou's
pre-surgery signing (Sept 1975), his death (Jan 1976), and the Tiananmen Incident.
ch26 (结束语, printed 526-534, 19 paras, 7 notes): Mu Xin's summation of Zhou's
hidden-front leadership, extended through the anti-Japanese and Liberation wars
(Yan Baohang's Barbarossa warning; Xiong Xianghui and the "Three Later Heroes";
Shen Anna; Zhang Kexia's Huaihai defection; Zhou's own retrospective on intelligence
work). ch27 (后记, printed 535-537, 7 paras, 1 note): the author's afterword on
sources and method.

### Figures
ch25-1 Barrister Ba He's Shen Bao clipping (p561, find_figures caught it);
ch25-2 Zhou's handwritten report manuscript (p568, MISSED by find_figures as
handwriting, cropped by hand). find_figures found only p561.

### Checks (all green)
verify_unit ch25/ch26/ch27 (parity 52/19/7, numbers 0 unresolved, anchors 8/7/1 ok);
qc_entities 0 misses (removed 斗争 as a works entry — false-matched "struggle" — and
罗斯 — substring of 俄罗斯; both hazards CLAUDE.md warns of); check_content --config
OK (0 displacement); check_align OK; check_structure parity OK; check_register within
tolerance of ch01; check_apparatus 0/0. Build: qa_epub PASS (28/28, 339 notes, 496
pagebreaks), epubcheck 0/0/0.

### OCR notes (dual-engine tesseract; PaddleOCR host unreachable)
Folio garble intermittently caught by the crop (S$10/和4l11/S$12/S$34), stripped
textually. Per-unit name folds: 陈广/陈庆→陈赓 (ch27), 毛洋东→毛泽东, 江理→江青,
陈志皋's four garbles, 能向晖→熊向晖, 净宝航→阎宝航, 刘章→刘鼎, 柯遍→柯麟. Real
numbers OCR corrupted and restored: 二百四十三→243 (Zhou's 1967 批示), 1S3→153,
197S→1975, $0周年→50周年. 《-as-digit phantoms (4/6/六) and note-ref-as-digit
phantoms fixed. Idioms to data/noise.txt: 数万万, 亿万, 千百倍, 日理万机, 万劫,
一百两, 伍豪二字. No fabrication; the one cut-off (逸豪 p510) read off the scan.

### Fact-check verdicts (real scholarship; never LLM-sourced)
Wu Hao Notice CORROBORATED (Zhang Chong the forger; Mao's 1932 proclamation; the
CR reckoning, "a sword over Zhou's head"). Yan Baohang's Barbarossa warning:
contribution CORROBORATED, its decisive 24-hour effect UNCORROBORATED (Western
scholarship notes Stalin disregarded many such warnings). Zhang Chong later became
the KMT's liaison to Zhou (ironic, noted). Source inconsistency footnoted: Mu Xin
attributes a memoir to Li Yimang but cites 《模糊的荧屏》(Huang Mulan's memoir).

### NOT re-noted (already placed earlier; cross-referenced)
Wu Hao (as Zhou's alias), Central Special Section, Zhongtong, Juntong, White Terror,
Kuomintang, Cultural Revolution, Kang Sheng, September Eighteenth / Mukden, Shanghai
Incident / Nineteenth Route Army, Shen Bao, Chinese Eastern Railway, Li Lisan line,
Wang Ming, Three Heroes of Longtan, Ningdu, Chiang Kai-shek, Central Soviet, Ruijin.

### Whole-book completion tail
Reconciliation sweep (check 12): glossary-forward 843/847; spelling standardized to
American (grey→gray, travelled→traveled x2, one note theatre→theater); 9 remaining
"Theatre" are proper venue names (kept). Deep audit (check 10): 41-para 3% fixed-seed
sample + 100% scan verification of B14 = 0 substantive errors (out/deep_audit.md).
out/term_ledger.md (847 rows) written; authority.json fed (252 renderings, slug
zhou-enlai); COMPLETION.md written; HANDOFF.md rewritten to COMPLETE. Back matter
left inert (no errata/colophon; PDF p582 blank). Cover from data/figs/cover.png.

## R1 (register revision) — pre-flight regression run (2026-08-22)

Regenerated `data/zh/` for all 28 units from source (b02-b09 re-OCR at the
recorded crop, b10-b14 from `data/txt_backup_b*`), replayed `apply_fixes.py`
(1318 + 42 + 218 + 345 + 210 replacements). Container tesseract is 5.3.4; the
original build used an older tesseract, so the character stream reproduces
(fixes replay) but blank-line paragraph structure drifts on the two oldest
batches.

- **verify_unit GREEN on 26/28**: ch00, ch02, ch04-ch27 (parity + numbers +
  anchors). ch00 recovered by a new `scripts/recovery/b01_surgery.py` (range
  fix 36-38 + 2 boundary repairs -> 6 paras). ch02 recovered by making
  `b02_surgery.py` skip-and-warn on a missing anchor instead of aborting
  fatally (-> 40/40).
- **ch01, ch03 parity not reproducible here** (documented + pinned in
  REVISION_PLAN.md section 2): ch01 zh 32 vs en 38 (6 OCR welds; §3 ambiguous,
  not force-split); ch03 zh 38 vs en 37 (p83 photo-page displacement). The
  shipped book built green at B14; this is a scaffold-reproducibility limit.
  R1 edits on these two units are Tier A mechanical swaps verified by the
  zh-independent guard set (apply_edits + notes.json anchor grep + builder
  anchor refusal + direct number/typography grep + check_register).
- **Benign zh number artifacts pinned** (parity OK, en correct): ch04 pair 37
  [7], ch15 pair 36 [2,10,30,1948], ch16 pair 2 [0,5,6,7,8].
- Snapshotted `out/ch01_reading.pre-R.md` (34450 bytes, identical to a8dda4c)
  as the frozen register reference for check_register through R2-R5.
- `pgrep -c tesseract` == 0 after every OCR run.

## R1 (register revision) — Tier A globals + ch15 exemplar (2026-08-22)

Batch R1 complete. Edits only via edits/<id>_edits.md + apply_edits.py (dates
scripted by scripts/recovery/gen_date_edits.py); Politburo done as a global
cascade per CLAUDE.md. Content frozen; no paragraph merged/split; no facts or
hedges changed.

### Tier A globals
- **Dates:** all 95 day-month dates -> month-day (ch00-ch05, ch09-ch12); 0
  day-month dates remain book-wide. 5 NOTE-ANCHOR pairs (ch00, ch02 x3, ch12)
  and 3 figures.json `before` anchors (ch01, ch02, ch11) re-synced to the
  post-edit prose. House style matched: "Month DD, YYYY," mid-sentence.
- **Politburo:** 政治局/中央政治局 -> "the Politburo" book-wide (51 reading-file
  hits + 3 note bodies), the redundant "Central" dropped to match ch19-ch20's
  existing form; "Politburos" plural and "Politburo Standing Committee" handled.
  Recorded in glossary.json (organizations: 中央政治局, 政治局) and authority.json
  (中央政治局 -> the Politburo [zhou-enlai]).
- **Ledger residuals:** "in good time" -> "in time/promptly" at 14 narration
  sites (ch03 x2, ch04, ch07 x2, ch09 x3, ch11, ch12, ch16, ch17, ch18, ch23);
  ch07 "driving into the heart of the enemy" -> "planted inside the heart of
  the enemy" (打入). The only surviving "in good time" are ch15's three, all in
  quoted testimony (see below).

### ch15 exemplar (the R2-R5 calibration target)
Full aligned zh-en read of all 75 paragraphs; 12 narration edits (litotes
calques "no little/no small" x5, trailing "besides" x1, "given to startling
acts", redundant "in his lifetime", 只好/"could only", a calqued "one after
another", "besides"->"apart from", de-inverted "broke free at last of"). 63
paragraphs left untouched — restraint is the point.

**Surviving tics, all defended aloud:**
- "Before long" x5 (不久/其后): defensible modern English, not antique ("ere
  long"); one is inside Feng Yuxiang's quote.
- connective "besides X" x6 + "Besides, ..." sentence-initial: modern usage;
  two are inside quotes (Liu Ding, Liu Qizhen/Chen Yangshan).
- litotes "no little work" (Wang Ruofei quote) + "no small quarter" (来头不小
  idiom, quote-marked): KEEP-list (quoted / idiom).
- "one after another" (¶4): inside the Yang Xianzhen memorial inscription.
- "in good time" x3 (及时): all inside quoted testimony (Pan Hannian's report,
  Chen Yangshan's essay) — KEEP-list (quoted documents untouched).
KEPT untouched throughout: the memorial inscription (¶3-5), the Mao and Zhou
letters, the Edgar Snow / Feng Yuxiang / Liu Ding / Pan Hannian / Liu Qizhen /
Chen Yangshan / Li Yimang quotes. No narration sentence > 90 words (no spine
split).

### QC
- verify_unit green on all edited good-parity units; the only NUMBERS "fails"
  are the three PINNED zh regen artifacts (ch04 pair 37, ch15 pair 36, ch16
  pair 2) — en correct. ch01/ch03 (pinned parity limits) anchors 0 broken.
- check_apparatus clean; typography clean (no curly quotes; pre-existing
  quotation-abridgment ellipses unchanged).
- Build: 28/28 chapters, 339 notes, 496 pagebreaks. qa_epub PASS. epubcheck
  5.1.0: 0 errors, 0 warnings.
- **10% spot-audit (15 edited paragraphs across all classes) vs source: zero
  meaning drift.** Digits preserved on every date; 打进/钻进心脏 -> "planted
  inside"; 及时 -> "in time"; 颇有威望 -> "considerable standing"; 只好 -> "had
  no choice but to"; 政治局 -> "the Politburo". All faithful.

## R2 (register revision) — tic sweep, front batch: ch00–ch08 (2026-08-22)

Batch R2 complete. Front batch of the Tier-B tic sweep (REVISION_PLAN §7).
Edits only via edits/<id>_edits.md + apply_edits.py. Content frozen; no
paragraph merged/split; no facts, numbers, names, or hedges changed.

### Pre-flight (fresh container)
- Regenerated `data/zh/` for ch00–ch08 per scripts/recovery/README.md: render
  36–197 @300dpi, ocr_crop (recorded crop, chi_sim psm6), then b01–b05
  strip/assemble/surgery/apply_fixes. `pgrep -c tesseract` == 0 after OCR.
  (ocr_dual skipped — not needed for the QC scaffold; content frozen.)
- Reverted data/pagemap/ch00–ch08 (assemble's auto-output is stale after
  surgery; the committed hand-built pagemaps are authoritative).
- verify_unit matches the §2 pins exactly: ch00/ch02/ch05/ch06/ch07/ch08 fully
  green; ch01 parity zh32/en38, ch03 parity zh38/en37 (pinned); ch04 pair 37
  `[7]` (pinned). No unpinned warning.

### Edits — 11 English-surface swaps across 5 units (ch00/ch03/ch05/ch08 clean)
- **ch01 (2):** 相继 "Massacres followed elsewhere one after another" -> "in
  place after place"; 相继 "the arrest, one after another, of" -> "the arrest,
  in turn, of". All 28 note anchors survive (grep-verified; neither edit
  touches an anchor).
- **ch02 (1):** 陆续 "returned to Shanghai one after another" -> "in succession".
- **ch04 (1):** trailing "did much work besides to assist" -> "did much other
  work to assist".
- **ch06 (6):** appositive ", besides," -> "also"; 不少 "no little intelligence"
  -> "a good deal of"; 不少 "no little convenience" -> "considerable"; 先后 "one
  after another resigned" -> "resigned in turn"; 不得不 "could not but hand" ->
  "had to hand"; 不小 "no small bribe" -> "a sizable bribe".
- **ch07 (1):** trailing "cowed besides by" -> "cowed as well by". (R1 already
  did this unit's Tier A ledger residuals: 及时 x2, 打入.)

### Clean chapters (0 edits — the pass working)
- **ch00** (preface): only hit is idiomatic "the building of the Central
  Special Section began" — natural English, left.
- **ch03**: all hits defensible — "no small thing" (Liu Bocheng quote),
  sentence-initial "Besides," (narration, modern), "and others" 等-closers,
  "the founding of Whampoa" (idiom), "Many years later," (reads naturally).
- **ch05**: every hit is inside quoted reminiscence (Li Kenong, Song Zhijia,
  Zhang Zhenhua, Ah Ying) or idiomatic ("the building of the country").
- **ch08**: the entire body (¶19–121) is Zhao Weigang's quoted memoir; ALL its
  tic hits (could only ×6, before long ×4, besides ×7, no small ×3, no few,
  could not but) are KEEP-list and untouched.

### Surviving tics, all defended aloud
- ch01:81 "no small hindrance" — inside the quoted 1930 Central Committee
  secret-work circular (KEEP: Party document).
- ch02:5 "no small feat" — fixed English idiom, not a 不少 calque.
- ch04:17 "could only wait tables" — plan-named FINE idiom, and inside Liu
  Ding's quoted reminiscence; ch04:131 "could only go back and hide" — inside
  the quoted Chen Shouchang mountain account.
- ch07:63 "no little superstition" — inside a quote-marked characterization;
  ch07:97 "one after another" — inside the Li Kenong biographer block quote.
- Connective/sentence-initial "Besides…" left across ch02/ch03/ch06/ch07 as
  modern "in addition" (plan CAUTION); "Before long" left as modern English.

### Long-sentence spine test
Regenerated the >90-word narration list for ch00–ch08 (ch01 113w schemes-list,
ch03 96w achievements-anaphora, ch03 97w parallel "not knowing…, they…", ch06
94w cumulative description; the others are quoted). Every one is a single-spine
colon/semicolon list or cumulative construction — none splits (a list is never
broken to shorten). No spine split, as in the ch15 exemplar.

### QC
- verify_unit: all edited units match the §2 pins (ch01 pinned parity, ch04
  pinned `[7]`; ch02/ch06/ch07 green). ch01 28/28 anchors present post-edit.
- Typography guard: R2 introduced **zero** smart quotes/ellipses. The 3
  pre-existing Unicode ellipses (ch01:43,47 Li Qiang; ch02:59 Liu Shuqin) are
  trailing-in-quotation marks that STYLE.md ruling 8 explicitly sanctions;
  in KEEP-zone quotes, left untouched.
- check_register vs out/ch01_reading.pre-R.md: all 5 edited units within
  tolerance (em-dash rate unchanged; ch07's "shall" flag is pre-existing formal
  quoted speech — Zou Taofen / Xu Enzeng dialogue — not an R2 edit).
- notes.json unchanged (byte-identical; 339 book-wide; no anchor moved).
- Diff reviewed for KEEP-list over-corrections: none (ch07 "no little
  superstition" quote correctly left; only the adjacent narration changed).
- **10% spot-audit — all 11 edited sites vs source: zero meaning drift.** Every
  litotes maps 不少/不小 (vague quantity preserved vague); 相继/陆续/先后 keep
  their succession sense; 不得不 -> "had to"; no number, name, date, unit, or
  hedge changed; no quoted material touched.
- Build: 28/28 chapters, 339 notes, 496 pagebreaks. qa_epub PASS (78 files, all
  links resolve). **epubcheck NOT available in this container** (setup could
  not fetch it; network-restricted). qa_epub is the gate and passes.

## R3 (register revision) — tic sweep, middle: ch09–ch14, ch16, ch17 (2026-08-22)

Batch R3 complete. Tier-B tic sweep of ch09–ch14 and ch17, plus the FULL
aligned zh-en read of ch16 (the "other biography chapter"). Edits only via
edits/<id>_edits.md + apply_edits.py. Content frozen; no paragraph merged/split;
no facts, numbers, names, or hedges changed.

### Pre-flight (fresh container)
- `./setup.sh` (tesseract 5.3.4 + chi_sim/chi_tra; epubcheck 5.1.0 fetched OK
  this time). The one pre-existing checker-regression failure ("hook stands
  down on template stub") is template maintenance, unrelated to the book.
- Regenerated `data/zh/` for R3's units: render 198–332 @300dpi, ocr_crop
  (recorded crop 0.11/0.90/0.135/0.95, chi_sim psm6, running-head strip), then
  b06 (ch09/ch10), b07 (ch11/ch12), b08 (ch13/ch14), b09 (ch15/ch16)
  strip/assemble/surgery/apply_fixes; ch17 (+ch18) from `b10_rebuild.sh`
  (txt_backup_b10). `pgrep -c tesseract` == 0 after every OCR run. Reverted
  data/pagemap/ (assemble's auto-output is stale after surgery; the committed
  hand-built pagemaps are authoritative).
- verify_unit matches the §2 pins exactly: ch09/ch10/ch11/ch12/ch13/ch14/ch17
  fully green; ch16 shows ONLY its pinned pair-2 `[0,5,6,7,8]` (OCR-garbled
  龙华兵工厂/1865 on the zh side; the English renders 1865/1913/1927 correctly).
  No unpinned warning.

### The sweep — 18 English-surface edits across 6 units; ch10 & ch12 clean
- **ch09 (5):** litotes 不少/不少/不少 ("no few/no little" -> "a good many /
  quite a few / a good deal of"); 除...外 "besides" -> "apart from"; 纷纷 "one
  after another" -> "each" (distributive, not sequence, per §3.2 caution).
- **ch11 (4):** collapsed the martyr-group 等-list drift (彭湃、杨殷等 rendered
  "and the rest" L21/L35/L45 vs "and the others" elsewhere) to the reverent
  majority form "and the others"; trailing 并 "besides" -> "as well".
- **ch13 (1):** 除...外 "besides" -> "apart from".
- **ch14 (5):** two trailing "besides" -> "as well"; 相继被捕 "one after
  another" -> "in succession"; two genuine NARRATION ellipses cut per STYLE
  ruling 8 (L35 Du Yuesheng bio 。……; L83 name-list).
- **ch16 (2), FULL aligned read of all 42 paras:** 只得 "could only" -> "had no
  choice but to"; litotes 不少 "no little work" -> "a good deal of work". ch16
  is largely OPERATIONAL (the Song Zaisheng infiltration, the magic-wine trap,
  the intelligence network) with two FACTUAL officer mini-bios — not elevated-
  antique like ch15 — so it correctly yields fewer register edits, not more.
  No padding to a number.
- **ch17 (1):** 除...外 "besides" -> "apart from". The chapter is heavily
  first-person Li Qiang memoir (KEEP), so it comes back near-clean.
- **ch10 & ch12 clean (0 edits):** every flagged site is quoted memoir/letter/
  dialogue (KEEP), a good form ("and the others"/"and the rest" with a
  meaningful martyr/traitor distinction in ch12), a modern form ("before long,"
  "the evening of the"), or genuine sequence.

### Surviving tics, all defended aloud (NOT re-noted / left)
- "Before long"/"before long" (不久) everywhere: modern English, not "ere long."
- "could only" ch09:47 (只能, genuine restrictive), ch17:67 (只能, physical),
  ch17:95 & ch17:97 (inside Li Qiang's quoted memoir).
- "could not help" ch16:43 & ch17:97 (不禁, idiomatic English).
- de-nominalizations left as idiomatic ("the fighting of the Pudong pickets,"
  "the development of the revolution," "from the founding of the Central Special
  Section," "the founding of the ... radio station") or inside quotes ("the
  arming of the peasants," ch09 document list; "the crossing of the Jinsha
  River," ch17 quote); "at the planning of the French consul-general" (ch14:35)
  held for restraint (diction-adjacent).
- "one after another" ch09:43 (连续, genuine sequence of eliminations), ch12:49
  (Fan brothers hit in sequence), ch12:81 (covert entry one by one), ch16:13
  (inside a quote, 先后).
- "and the rest"/"and the others" left where a good form or a meaningful
  distinction: ch11:77 (Zhou Enlai's quoted essay), ch12 (martyrs vs traitors),
  ch13:67 (其余 = remainder of documents), ch14:61 (orgs), ch17:103.
- "no small risk" (ch17:75) & "no small part" (ch17:143, quoted): idiomatic
  English collocations, defensible aloud (unlike "no few"/"no little" calques).
- trailing/quoted "besides" left: ch09:77 (memoir quote), ch11:23 (Zhou essay),
  ch12:25 (Ke Lin quote), ch14 dialogue; "Besides X, ..." sentence-initial +
  gerund (ch16:36, ch12:37) modern; "besides"+gerund (ch17:71/129) natural.
- "let slip" ch11:59 (inside Zhou Enlai's quoted essay — KEEP despite the plan
  citing it; the KEEP list wins), ch14:69 & elsewhere (modern "reveal" idiom).
- "whereupon" ch12:55 (inside a quoted newspaper article — KEEP).
- Long-sentence spine test: no split. ch11:25 (semicolon-split), ch12:11
  (single-spine + embedded newspaper quote), ch12:41 & ch12:57 (splitter
  artifacts across in-quote periods — real sentences all <90w), ch16 quoted
  letters, ch17:103 (single-spine colon list of six measures), ch17:121
  (dramatic action beat carried by an em-dash), ch17:153 (near-all quoted
  Chiang telegrams).

### QC
- verify_unit: ch09–ch14, ch17 green; ch16 shows only its pinned pair-2 zh
  artifact. Anchors: all present, 0 broken; notes.json byte-unchanged (339
  book-wide; no anchor moved — no prose edit touched an anchor).
- Typography guard: R3 introduced **zero** smart quotes/ellipses (per-file
  Unicode-punct count identical HEAD vs post-edit). The pre-existing "…"
  ellipses (ch09:15/21/69, ch11:39, ch16:9/11, ch17:43/153) are quotation-
  abridgment marks inside quoted material, sanctioned by STYLE ruling 8; left.
- check_register vs out/ch01_reading.pre-R.md: all 6 edited units within
  tolerance; em-dash rates well under the ~6/1k reference (no pile-ups).
- check_apparatus clean (0 failures, 0 warnings).
- **10% spot-audit — all 18 edited sites re-verified vs source: zero meaning
  drift.** Litotes map 不少/不小 (vague quantity kept vague); 相继/连续/纷纷/先后
  handled per their actual sense (sequence vs distributive); 只得 -> "had no
  choice but to"; 除...外 -> "apart from"; the 等-list collapse preserves the
  referent; the two ellipsis cuts are punctuation-only. No number, name, date,
  unit, or hedge changed; no quoted/dialogue material touched.
- Diff searched for KEEP-list over-corrections: none survived. Two mechanical
  over-corrections were CAUGHT and left in triage — "let slip not a moment"
  (ch11:59, Zhou Enlai's quoted essay) and "whereupon" (ch12:55, quoted
  newspaper) — exactly the cases the KEEP-list guard exists for.
- Build: 28/28 chapters, 339 notes, 496 pagebreaks. qa_epub PASS (78 files,
  all links resolve). **epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings.**

### Observed for R5 (book-wide diction ledger, deliberately NOT fixed piecemeal)
These are STYLE.md decided-rendering residuals that drifted; fixing them only in
R3's units would create the partial-application drift the plan forbids. They
belong to R5's whole-book reconciliation (a global grep-and-cascade), not the
tic sweep:
- 破坏 (enemy act) -> "wrecking" (ledger decided: **sabotage**): e.g.
  ch09:47, ch16:2. Book-wide count to be swept at R5.
- 镇压/除掉 of traitors -> soft "put down"/"did away with" (killing-verb ledger:
  **eliminate/kill**): e.g. ch09:47 "put it down", ch16:32 "did away with this
  menace". Sweep at R5's 叛徒/killing-verb reconciliation.

## R4 — register pass: tic sweep, back batch (ch18–ch22) — 2026-08-22

Tier-B register tic sweep of the back batch (ch18–ch22), per REVISION_PLAN.md
sections 3–5. Reading text edited only via edits/<id>_edits.md + apply_edits.py;
content frozen (no paragraph merged/split, no fact/number/name/date/hedge
changed, no quoted material touched).

### Pre-flight (fresh container)
- Regenerated `data/zh/` for ch18–ch22 from `data/txt_backup_b1*` via the
  `scripts/recovery/b1N_rebuild.sh` drivers (b10 → ch17+ch18, b11 → ch19+ch20,
  b12 → ch21+ch22). Deterministic (no re-OCR needed); `apply_fixes.py` replayed.
  The one `apply_fixes` "not found" (`沈钩儒`, ch22) is the benign tesseract-5.3.4
  drift the HANDOFF flagged; verify_unit is the gate.
- **All five units verify_unit GREEN before any edit** (parity + numbers +
  anchors, 0 unresolved): ch18 59 pairs, ch19 42, ch20 64, ch21 104, ch22 47.
  Better than the R1 pins predicted — no benign number-pair artifacts for this
  range (none pinned; if one appears on a later regen, pin it, do not "fix" the
  English). `data/pagemap/` regenerated byte-identical to the committed maps.

### Edits — 19 English-surface edits across 17 paragraphs
- **ch18 (4):** trailing 此外 "besides" → "also"; 先后 "one after another" →
  "in succession" (people); 除了 "besides political courses" → "apart from";
  de-nominalized "the teaching of the radio training class" → "teaching the…".
- **ch19 (6):** 接连 "one after another six cables" reordered for rhythm; three
  trailing 并且/又/还有 "besides" → "as well"; 只好 "could only consent" → "had no
  choice but to consent"; **calibrated ruling 1 de-inversion** of the L79
  fronted-infinitive subject ("to have the enemy destroy… was hard to resolve
  upon" → "it was indeed hard to resolve on letting the enemy destroy…").
- **ch20 (4):** 便 "thereupon" → "then"; three trailing 又/还 "besides" → "as
  well". (A testimony-dense chapter; every litotes/could-only/besides hit in the
  Chen Yangshan / Bao Junfu / Chen Geng-letter quotes was KEPT.)
- **ch21 (5):** 后来 "At length they announced" → "Later" (source is 后来, not
  "finally"); 除…外 "besides Tan Guofu" → "apart from"; 只好 "could only quibble
  at last" → "at last had no choice but to quibble"; inverted antique "let slip
  no chance" → "missed no chance" (R3's "let slip no [X]" precedent); **one L201
  spine split** (the ask→gather→report→explain→say→tell run-on, cut at the hall).
- **ch22 (0):** a clean chapter — testimony-saturated; every flagged site is
  inside a quoted memoir (the prison hypnotism account), the Shen Bao report, the
  Shen Zui assassination account, or the Organization Department statement, and
  is KEPT. Line 73 "and so on" is a FALSE POSITIVE on "and so, on the one hand".

### Spine test (ch19's five, ch21's two, plus every >90-word narration sentence)
No splits except ch21 L201. All others pass: single-spine biographies (ch19 L11,
ch21 L109), colon-plus-list measure enumerations (ch19 L87), rhetorical how-lists
that keep the author's heat (ch21 L65), semicolon-balanced deliberations (ch19
L79, ch22 L69), and quoted documents/testimony (ch20 L53, ch22 L53/L81/L97/L99,
the Deng Xiaoping eulogy). A list is never broken to shorten a sentence.

### Defended tic survivors (every surviving battery hit)
- ch18:63 "could only work hard to repay" — Zhang Shenchuan's first-person
  quoted memoir. ch19:55 "Presently Chiang Kai-shek came" — inside Cai Mengjian's
  quoted testimony (**the KEEP-list guard's textbook catch**: archaism inside
  quotation marks stays; the plan's 3.2 lists this site but 3.3/STYLE override,
  as with R3's "whereupon"). ch20:123 "could only make contact by telephone" —
  Chen Yangshan's quoted testimony. All 不久 "Before long" (ch18×6, ch20:51,
  ch21:161/201) = modern, kept. Genuine sequence 相继/接连 kept where rhythm holds
  (ch20:67, ch22:69). besides+gerund kept as modern (ch22:69 "besides demanding").
- **等-tag density flagged for R5:** ch21 carries 18 "and the rest"/"and the
  others" hits (a rescue narrative full of name-lists) with VARYING membership,
  so each is a genuine truncation and LEFT (ch15-exemplar rule). The mild "Chen
  Geng and the rest" vs "…and the others" alternation for the arrestee group is
  recorded here for R5's whole-book `check_reconcile.py` human read — the plan's
  designated place for repeated-rendering consistency, not the per-chapter sweep.

### QC
- verify_unit: ch18–ch22 all GREEN (parity + numbers + anchors, 0 unresolved),
  before and after edits. notes.json byte-unchanged (**339** book-wide; 0 anchor
  moves — no prose edit touched an anchor; apply_edits reported 0 note changes).
- Typography guard: R4 introduced **zero** smart quotes/ellipses (per-file
  U+2026 count identical pre/post; ch18 4→4, etc.). Zero curly quotes anywhere.
  The 40 pre-existing "…" are quotation-abridgment marks inside quoted material
  (STYLE ruling 8), unchanged; the book builds epubcheck-clean with them.
- check_register vs out/ch01_reading.pre-R.md: all five within tolerance;
  em-dash rate 1.00× the reference (no change), 0% exclamations added.
- **Spot-audit — all 17 edited paragraphs re-verified vs source: zero meaning
  drift.** Each edit is a surface swap at a flagged site with the source phrase
  recorded in its WHY line; no number, name, date, unit, or hedge changed; no
  quoted/dialogue/document material touched. (100% of edited paragraphs, well
  above the 10%/min-10 bar.)
- Diff searched for KEEP-list over-corrections: none survived. The three
  in-quote hits above were caught in triage and left.
- Build: 28/28 chapters, 339 notes, 496 pagebreaks. qa_epub PASS (78 files, 35
  documents, all links resolve). **epubcheck 5.1.0: 0 fatals / 0 errors / 0
  warnings.**

### Carried to R5 (unchanged from R3's list; still deliberately NOT fixed here)
- 破坏 (enemy act) → "wrecking" (ledger: **sabotage**) — e.g. ch21:5 "wrecking",
  "The wrecking of the Central Military Commission"; ch20:67 "wrecked"; book-wide.
- 镇压/除掉 of traitors → soft "put down"/"did away with" (killing-verb ledger:
  **eliminate/kill**) — sweep at R5's 叛徒/killing-verb reconciliation.
- ch21's 等-tag alternation (above), for R5's check_reconcile.py.

---

## R5 — tail tic sweep (ch23-ch27) + whole-book reconciliation + close (2026-08-22)

Final register batch. Pre-flight: stray branch `claude/modest-archimedes-7h5vbz`
folded into `claude/zhou-enlai` (its head equalled origin, no work stranded);
data/zh regenerated for ch17-ch27 (b10-b14 rebuild drivers, deterministic, no
re-OCR); ch09/ch10/ch16 pages re-OCR'd raw for killing-verb source consultation.
verify_unit GREEN on all regenerated units before any edit (ch23-27: 0 unresolved
number pairs — no benign artifacts to pin; ch18-22 green too).

### Tail tic sweep (ch23-ch27) — 6 narration edits
ch23-ch25 are extremely quote-dense (memoirs, the Du Ning essay, Mao's
Proclamation, the Xifeng county report, testimony); nearly every tic hit sits
inside quoted matter and is KEPT. ch26 (Conclusion) and ch27 (Afterword) came
back **clean** (0 edits) — expected per the plan's near-zero-tic list.
- ch23 (3): "left Shanghai one after another" / "…Qian Zhuangfei did, one after
  another" (相继/先后相继, people) -> "in succession"; "owed no little to his
  wife" (出力不小 litotes) -> "a great deal".
- ch24 (1): "transferred one after another to other places" (相继调往各地) ->
  "in succession".
- ch25 (2): two 除…外 "besides/Besides" (Mao clearing up the forged notice) ->
  "apart from".
- Defended survivors (source-checked): ch23 "at length"(memoir, = in detail),
  "could not but"(Li Yimang memoir), "and the rest"(Du Ning essay), "as ill
  luck would have it"(不幸得很, matches R4's ch21 decision); ch24 "Of late"/
  "besides"(Mao's Proclamation, a KEEP document), the "one after another" at
  连续/接连 sites (genuine sequence); ch25 "one after another" at 先后连续 (the
  notices really ran in 4 papers Feb 16-21) and 纷纷落网 (a real multi-year
  1950-51 campaign, dated); ch27 "at length"(talk at length = in detail),
  陆续不断 "one after another".

### 叛徒 variety check (plan 3.2) — VERDICT: renegade is drift, collapsed
Sampled all three variants against source. **traitor** is the primary rendering
book-wide. **renegade** (29 occ.) is confined to ch21/ch22 (batch B12) + 2 in
ch24, every one rendering 叛徒 (verified: 叛徒王云程 -> "renegade Wang Yuncheng",
无耻的叛徒 -> "shameless renegade"), and ch21/ch22 use BOTH "traitor" and
"renegade" for 叛徒 in the same chapters — the signature of per-batch drift, not
distinct-source variation. STYLE.md sanctions "traitor" OR "turncoat" for 叛徒
but NOT "renegade". VERDICT: collapse renegade -> traitor (28 sites via
`scripts/recovery/r5_collapse_renegade.py`, a grep-driven global rendering fix
per the CLAUDE.md corrections workflow; anchor-safe — no anchor/note/glossary
body contains "renegade"); 1 kept where the same sentence already used "traitor"
(ch21 "the renegade Chen Weiru … the traitors' ranks", per plan 3.2). **turncoat
(11 occ., ch04-09 + ch24) KEPT** as the STYLE-sanctioned deliberate early-batch
variant of 叛徒 — not drift.

### Killing-verb ledger cascade (STYLE round-2) — 3 edits, source-verified
The soft rendering of a lethal act ("put down"/"did away with" for 镇压/除掉 of
traitors by the Red Squad) is the exact STYLE killing-verb defect. Raw-OCR
source confirms: ch09 "打狗队"连续镇压了几个公开的叛徒 / 及时的镇压叛徒 ->
"eliminated"; ch16 为党和人民除掉了 -> "eliminated". KEPT (source-checked): ch09
"put down turncoats who informed" (镇压 of scab-informers by the early workers'
pickets, suppression) and "put it down" (镇压 of an activity, not a person);
ch07 "put down the people's resistance" (镇压 of a movement = suppress); ch10
"resolved to do away with them" (first-person memoir quote); ch15 "did away
with feudal customs" (abolish, not killing); ch24 "do away with Chen Lifu…"
(villain's quoted dialogue). ch24 "put down by its master" (dog idiom, quote).

### Whole-book antique-straggler sweep — 2 edits the per-chapter gates missed
register_tics.sh re-run over all 28 units; every surviving hit defended. Two
genuine stragglers surfaced (fix the gate, not just the defect): ch12
"whereupon" (便/遂 connective, narration) -> "and then"; ch22 "at length"
(终于, inside the 1984 Central Org Dept notice — its own register is plain
modern officialese, so the antique "at length" is off-register) -> "at last".
Defended survivors book-wide: "before long"(不久), "let slip"(reveal sense),
"Presently"/"Of late"/"for all that"(quotes), "at length"(= in detail).

### check_reconcile.py — human-read adjudication
- **Epithet drift: 69 candidates, all hyphenation noise** (counter-X, anti-X,
  twenty-X, three-story vs three — distinct compounds, not rendering drift).
- **Glossary forward: 845/849** decided forms present. 4 unused are pre-existing
  (0 in HEAD too) and legitimate: "Chen Zhifei" (prose uses the given name
  "Zhifei"), "Zhao Minlin"/"Jiang Baili"/"Guangming Daily" (referents mentioned
  by variant or not by that exact form). Not R5 regressions.
- **Spelling locale: the theatre/theater "mix" is the recorded B14 decision** —
  all 9 "Theatre" are venue proper names (Carlton, Beijing, Lido, Yangtze,
  Peacock Oriental); all 7 "theater" are the common noun. The check flags an
  intentional, documented split, not drift.

### 破坏 (enemy act) rendering — ADJUDICATED, no blanket cascade
The R4 carry-forward flagged a book-wide 破坏 -> "wreck*" cascade to "sabotage".
On review of all ~50 "wreck*" sites, the surviving renderings are contextually
appropriate: 破坏组织 (an organization smashed by mass arrest) = wreck/smash/
destroy, NOT "sabotage" (which implies covert subversion — the wrong sense);
破坏计划 = "wreck a plan" (idiomatic English). The abstract-noun calque the
ledger actually flagged ("forestall the enemy's *wrecking*") does not survive
in the current text. A blanket "sabotage" swap would misrender the mass-arrest
sense, so it is deliberately NOT done. If the commissioner wants uniform
"sabotage" regardless, that is a one-line global corrections item (site
inventory: ch04:103, ch09:59/95/99, ch10:43/45, ch11:27/31, ch12:31/47,
ch16:5, ch17:137, ch19:13/69, ch20:65/67/91/113/129, ch21:5/7/23, ch22:29,
ch23:7/15/91/99/101, ch24:5/7/9/11/19/35/41/43/67/69/89/99, ch25:31, ch27:3 —
many inside quoted documents/memoirs, which are KEEP).

### QC
- verify_unit GREEN on every unit with data/zh that was edited (ch21/22/24 +
  ch23/25): parity + numbers (0 unresolved) + anchors. ch09/ch12/ch16 (no
  regenerated data/zh) verified by the zh-independent guard set (apply_edits
  OLD-unique, anchors intact, no number/typography change, check_register) —
  the R1 ch01/ch03 precedent.
- Typography: **zero** new non-ASCII introduced by any R5 edit (per-file char
  counts identical HEAD->now for all 8 touched files). Pre-existing U+2026
  (quotation abridgment), U+2013, and accented foreign names (Lü, café) left.
- check_register vs out/ch01_reading.pre-R.md: all touched units within
  tolerance.
- **Whole-pass (R1-R5) diff audit: 192 word-level edits, 188/188 balanced
  insertions/deletions across 25 files — zero paragraph-boundary changes.**
  Every change classified: dates, Politburo, renegade->traitor, litotes,
  besides, 只好, 相继 people, killing verbs, antique stragglers, de-inversions.
  KEEP-list grep clean: 0 em-dash swaps, 0 contractions-by-quota, 0 "Comrade"
  removals, 0 quoted-document register changes; the one "let slip"->"missed" is
  the antique "allow to escape" sense (not the KEEP reveal sense).
- **Spot audit: 20+ edited paragraphs across R1-R5 re-verified vs source
  (well above 10%/min-15) — zero meaning drift.**
- Build: 28/28, 339 notes, 496 pagebreaks. qa_epub PASS. epubcheck 5.1.0: 0
  errors / 0 warnings.

### R5 total: 12 register edits (6 tic + 3 killing-verb + 2 straggler + the ch25
"besides"×2 counted in the 6) + 28-site renegade collapse. The register pass
(R1-R5) is COMPLETE. Further work is a corrections pass (CLAUDE.md), and the
commissioner's requested footnote-density pass (FOOTNOTE_PASS.md), which is next.

## FN1 — footnote-density pass, ch00-ch05 (FOOTNOTE_PASS.md batch 1)

First batch of the footnote-density pass the commissioner asked for (increase
note density; explain every person, place, event, term a non-specialist Western
reader would miss, at first appearance book-wide, with real checked content).
Content FROZEN: this pass ADDS notes only. No prose, number, name, or paragraph
change (verified: `git diff` touches only notes.json + docs + the two merge
files; no out/ch*_reading.md edited).

### Branch
Session opened on stray branch `claude/eloquent-fermat-yad3vr` (== origin/
claude/zhou-enlai, all R1-R5 work). Folded per CLAUDE.md rule 2: checked out
`claude/zhou-enlai`, reset to origin, deleted the stray (local + pruned remote).
All FN1 work on `claude/zhou-enlai`.

### data/zh decision
`data/zh` was absent on this checkout (untracked/regenerable). NOT regenerated
for this pass: it is a parity-QC scaffold for PROSE work, and FN1 changes no
prose and runs no parity check. Anchors are verified against `out/<id>_
reading.md` (present) by apparatus_merge; hanzi are proofread against
`glossary.json` (present) and decoded from their numeric refs; fact-checking is
against external scholarship, not the OCR. No source reading a note depends on
required a fresh scan crop this batch. (If a later FN batch needs qc_entities
first-appearance mapping, regenerate per scripts/recovery/README.md then.)

### Notes added (before -> after)
- ch00 12 -> 19 (+7): Zhou Enlai, Chiang Kai-shek, Great Revolution, Comintern,
  Li Qiang, Deng Yingchao, Central Soviet.
- ch01 28 -> 41 (+13): three Shanghai workers' uprisings, Northern Expedition,
  Fifth National Congress, Borodin, Zhu De, He Long, Liu Bocheng, Zhao Shiyan,
  Chen Yannian, Zhang Tailei, Li Weihan, Nov-1927 enlarged Provisional Politburo,
  the "July 15" split (fills the dangling cross-ref from the ch00 Wang Jingwei note).
- ch02 16 -> 22 (+6): Qu Qiubai, Su Zhaozheng, Liu Shaoqi, Xiang Ying,
  He Mengxiong (+ the Longhua martyrs / Feb 7 1931), China Relief Society (+ MOPR).
- ch03 13 -> 19 (+6): Eastern Expeditions (+ Chen Jiongming), He Yingqin,
  Tang Shengzhi, Ye Jianying, Zhou Yiqun, Sun Yat-sen.
- ch04 24 -> 34 (+10): May Fourth Movement, Tongmenghui, Yuan Shikai, Li Dazhao,
  Cai Hesen, Xi'an Incident, Deng Yanda, Sun Bingwen, Reorganizationists (accuracy
  note on the book's "under Hu Hanmin"), Yang Yin.
- ch05 16 -> 20 (+4): Zhang Xun's 1917 restoration, Chen Diaoyuan (+ ticket-bandit
  nuance + the author's uncorroborated 20-million-yuan figure), Kong Xiangxi, Li Fuchun.
- **FN1 total: +46 notes. Book 339 -> 385. ch00-ch05: 109 -> 155.**

### Fact-checking
Every added identification checked against real scholarship (English/Chinese
Wikipedia, Baidu Baike, Britannica, Maitron, official CCP-history sites). Verdict
stated in each note. NO Grok/Grokipedia or any AI-written reference used (they
surfaced in some result lists and were rejected). Research gathered by four
sourced-dossier sweeps; findings verified before authoring. Notes that grade a
book claim rather than just identify: Chen Diaoyuan (identity corroborated,
20-million-yuan plunder = author's, uncorroborated; ticket-bandit nickname traces
to the 1923 Lincheng case, not his own banditry); Reorganizationists ("under Hu
Hanmin" is loose — the faction looked to Wang Jingwei; corrected in the note);
Xiang Ying (birth year 1895 vs 1898 flagged).

### Hanzi discipline
People notes carry NO hanzi (house style; eliminates insertion risk). Term/org/
event notes carry hanzi as NUMERIC character references, each decoded and
cross-checked: 大革命, 共产国际, 中央苏区, 北伐 (ch00-01); 中国济难会, 孙中山,
五四运动, 同盟会, 改组派 (ch02-05). 共产国际/中央苏区/孙中山/改组派/中国济难会
match glossary.json exactly; 大革命/北伐/五四运动/同盟会 are the standard forms,
decoded and eyeballed. No U+FFFD anywhere; build carries them intact.

### NOT re-noted (already placed — cross-referenced, no second note)
- Chiang Kai-shek: only ch00 (new) is the ID; recurs everywhere un-renoted.
- Ren Bishi: ID kept at ch02 (arrest) + ch13 (full bio); ch00 preface mention
  left un-noted (close, glancing).
- Luo Yinong, Yun Daiying: IDs kept at ch02 (first substantive treatment);
  ch01 list-mentions left un-noted.
- Deng Xiaoping: ID kept at ch04; first appears ch02 (minutes-keeper) but
  famous + close, left un-noted at ch02.
- Chen Yangshan: ID kept at ch04; ch01 mention left un-noted.
- Du Yuesheng, Yang Du: full treatments at ch14; ch04 first-appearances are
  glancing and self-glossed ("that great Shanghai gangster"), left un-noted here.
- Guangzhou Uprising: full note at ch11; ch04 mention self-dated ("of December
  11"), left un-noted here (the Ye Jianying note at ch03 already names it).
- Chen Guofu/Chen Lifu: ID at ch06 (one chapter on); ch05 "party bosses" partial
  gloss, left un-noted here.
- Nie Rongzhen, Chen Geng, Peng Pai, Wang Jingwei, Zhang Guotao, Gu Shunzhang,
  Xiang Zhongfa, Pan Hannian, Ye Ting, Blyukher, Thalmann, Sano Manabu, Pavel
  Mif, Xu Enzeng, Cai Mengjian, Li Kenong, Qian Zhuangfei, Hu Di, Li Bai, Zhao
  Yiman: already noted (ch00-ch05), reused unchanged.
- In-text self-glossed, deliberately un-footnoted (author supplies the gloss):
  the elegy figures Fang Xuanling / Li Zuoche / Wei Zheng / Du Ruhui / Han Xin
  (ch05 prose); "Three Great Policies" (listed in ch05 prose); Three Principles
  of the People (covered by the Sun Yat-sen note); minor cover-family members,
  shops, and schools named once (Xiong Jinding, Zhu Duansui, Li Yimang, Wing On,
  Sincere, Nanyang/Zhejiang schools, West Lake Exposition), Butterfield & Swire,
  Li Jishen (peripheral name-drop).

### Reconciliation items for later FN batches / FN5 (cross-chapter, out of FN1 scope)
Notes at a first appearance in ch00-ch05 that also have a note in ch06+; the
later one should be trimmed to a cross-reference when its batch runs:
- Liu Bocheng: new ID at ch01 (first appearance, Nanchang) + existing bio at ch07
  (episode-specific). FN2: trim ch07 to a cross-ref to ch01.
(All other FN1 additions have no ch06+ duplicate.)

### QC
- check_apparatus.py: 0 failures, 0 warnings (both merges).
- Build: 28/28 chapters, **385 notes**, 496 pagebreaks. qa_epub PASS (385
  refs/bodies/backlinks resolve, sequential). epubcheck 5.1.0: 0 fatals / 0
  errors / 0 warnings.
- Every anchor verified a unique verbatim substring of its reading file before
  merge. No prose/number/paragraph change (notes-only pass).

## FN2 — footnote-density pass, ch06-ch11 (FOOTNOTE_PASS.md batch 2)

Second batch of the commissioner's footnote-density pass (Yang Dengying and the
first counter-espionage tie; the tiger's den; Fengtian; the Action Section and
the Red Squad; the Avenue Joffre gunfights). Content FROZEN: notes ADDED and
reconciled only. No prose, number, name, or paragraph change (verified: git diff
touches only notes.json + data/fn2_notes.json + docs; no out/ch*_reading.md
edited).

### Branch
Session opened on stray branch `claude/zhou-enlai-fn2-footnotes-sowd3r` (per the
harness). Per CLAUDE.md rule 2 the canonical working branch is `claude/zhou-enlai`;
this session's commits are pushed to the harness-designated branch for delivery
and can be folded onto `claude/zhou-enlai` per the usual recipe. All FN2 work is
notes-only and additive.

### data/zh decision
Not regenerated (parity scaffold, not needed for a notes-only pass; same
rationale as FN1). Anchors verified against out/<id>_reading.md by
apparatus_merge; hanzi taken from glossary.json and emitted as numeric refs;
fact-checking against external scholarship.

### Notes added (before -> after)
- ch06 7 -> 11 (+4): Zhang Daofan, Sun Ke, Zeng Guofan (+ the Family Letters as
  a "molding" gift), the Mao 1935 quote source ("On Tactics Against Japanese
  Imperialism," Wayaobao, 27 Dec 1935).
- ch07 14 -> 20 (+6): Li Zongren (+ Guangxi clique; Bai Chongxi cross-ref),
  Liang Qichao, the Sun Yat-sen tunic (Zhongshan suit), Nanyang College
  (-> Shanghai Jiao Tong), Central Military Academy (Whampoa successor, cross-ref
  ch03), the "true face of Mount Lu" allusion (Su Shi).
- ch08 13 -> 16 (+3): Fengtian (place/clique + Zhang Zuolin; hanzi 奉天), Yang
  Yuting (+ the Yang-Chang killing), the Four Cardinal Principles (Deng, 1979).
- ch09 16 -> 21 (+5): the Green Gang (cross-ref Du Yuesheng ch14), Yang Zhihua
  (Du Ning), the Sixth National Congress (Moscow 1928), the League of Left-Wing
  Writers (hanzi; cross-ref the Longhua martyrs ch02), the Northeast Anti-
  Japanese United Army.
- ch10 9 -> 12 (+3): Wu Zhihui, Water Margin & Romance of the Three Kingdoms
  (Four Great Classical Novels), and the Canton-Hong Kong Strike moved here to
  its first appearance (see reconciliation below).
- ch11 11 -> 14 (+3): Chen Yi (Lyon expulsion; later marshal/foreign minister),
  the Hailufeng soviet (Peng Pai; China's first soviet), and a caution that the
  1927 "Red Guards" (chiweidui) are NOT the 1966 Cultural Revolution Red Guards
  (hongweibing).
- **FN2 total: +24 notes. Book 385 -> 409. ch06-ch11: 70 -> 94.**

### Reconciliations (pre-existing duplicate/misplaced notes trimmed)
- **Liu Bocheng (mandated):** trimmed the ch07 episode note to a cross-reference
  to the first-appearance note at chapter 1, keeping only the escort-through-
  Nanjing detail.
- **Qian Dajun:** first appears (and is fully noted) at chapter 3; the redundant
  ch10 note trimmed to a cross-reference to chapter 3.
- **Canton-Hong Kong Strike:** first appears at ch10 (Luo Yinong's bio); the note
  had sat one chapter late at ch11. Added at ch10 (first appearance) and the ch11
  note trimmed to a cross-reference to chapter 10.

### Cut after fa_check — already covered, not re-noted (cross-referenced instead)
Central Plains War, Feng Yuxiang, Yan Xishan (all in the ch07 "tangled war"
note); Zhongtong, Juntong, Dai Li, Ren Zhuoxuan/Ye Qing (ch07); the Chen brothers
/ CC Clique (ch04, ch06); Zou Taofen note already covers Zhang Naiqi, Li Gongpu,
the Life Bookstore, and "Since the War of Resistance Began"; September 18
(Mukden) Incident (ch08); August 7 Conference (ch02); Congress of Soviet Areas
(ch02/ch09); Nanchang Uprising (ch00); Whampoa (ch03); Communist University of
the Toilers of the East (ch04); Encirclement Campaigns (ch04); Songhu Garrison
Command (ch03); Beiyang/Northern Warlords (ch01); New Youth, Cultural Revolution,
Bai Chongxi, Lin Yunan (ch01/ch02); the Monkey King / Princess Iron Fan allusion
(ch05); Zhang Zuolin (folded into the ch08 Fengtian note rather than a separate
note); Chen Duxiu, Yuan Shikai, Peng Pai, Yang Yin, Zhang Tailei, Ye Ting, Sun
Yat-sen, Li Weihan, Deng Xiaoping, Ye Jianying, Su Zhaozheng, Liu Shaoqi (all
noted earlier). Deliberately left unfootnoted (prose-covered or too minor):
Yang Jianhong and Lian Desheng (the prose introduces each fully and neither is
independently attestable), Liu Ding (noted ch04), Cai Boxiang (fate noted ch08),
Yan Changyi / Xing Shizhen / Zhang Jichun (the ch11 prose gives each a full
obituary), and the string of one-appearance cover names, shops, streets, and
minor warlords.

### Fact-checking
Every added identification checked against real scholarship (English/Chinese
Wikipedia, Baidu Baike, Britannica, New World Encyclopedia, ANU/academic
histories, and primary texts on Marxists.org for the Mao report and Su Shi poem).
Verdict stated in each note. NO Grok/Grokipedia or any AI-written reference used
(such results surfaced in searches and were rejected). Graded/flagged claims:
Yang Zhihua birth year 1900 vs 1901 (flagged in the note); Fengtian rendered
carefully (city officially Shenyang from 1914 but "Fengtian"/"Mukden" persisted
and revived under Manchukuo; province -> Liaoning 1929); Green Gang police
penetration stated at the level the scholarship supports.

### Hanzi discipline
People notes carry NO hanzi. Only two term notes carry hanzi, both taken
verbatim from glossary.json and emitted as numeric character references generated
programmatically from the glossary string (never hand-typed): 奉天 (Fengtian,
places) and 中国左翼作家联盟 (League of Left-Wing Writers, organizations); each
decoded and byte-matched against the glossary. All other term/allusion notes use
pinyin/English to eliminate insertion risk (chiweidui/hongweibing, Qing Bang,
Zhongshan suit). No U+FFFD; no named entities.

### QC
- check_apparatus.py: 0 failures, 0 warnings.
- Build: 28/28 chapters, **409 notes**, 496 pagebreaks. qa_epub PASS (409
  refs/bodies/backlinks resolve, sequential). epubcheck 5.1.0: 0 fatals / 0
  errors / 0 warnings.
- Every new anchor verified a unique verbatim substring of its reading file
  before merge. No prose/number/paragraph change (notes-only pass).

## FN3 — footnote-density pass, ch12-ch17 (FOOTNOTE_PASS.md batch 3)

Third batch of the commissioner's footnote-density pass (the Bai Xin manhunt
aftermath and Avenue Joffre gunfight; the two Ren Bishi rescues and the Guan
Xiangying rescue; the Yang Du / Du Yuesheng "new chapter" trio; Liu Shaobai, the
pastors and lawyers, the Wu Hao counter-notice; the Songhu Garrison Command and
Song Zaisheng; Li Qiang and the radio branch). Content FROZEN: notes ADDED and
reconciled only. No prose, number, name, date, or paragraph change (verified:
git diff touches only notes.json + data/fn3_notes.json + docs + the rebuilt
EPUB; no out/ch*_reading.md edited).

### Branch
Session opened on stray branch `claude/zhou-enlai-fn3-footnotes-jrymzg` (== origin/
claude/zhou-enlai at FN2's HEAD, 0/0 divergence). Per CLAUDE.md rule 2 the canonical
working branch is `claude/zhou-enlai`; checked it out, reset to origin, did all FN3
work there. Stray branch carried no unique commits, so nothing to fold; deleted at
close.

### data/zh decision
Not regenerated (parity scaffold, not needed for a notes-only pass; same rationale
as FN1/FN2). Anchors verified against out/<id>_reading.md by apparatus_merge; hanzi
taken from glossary.json (gloss_hanzi.py) and emitted as numeric character
references generated programmatically from the glossary string; fact-checking
against external scholarship.

### Notes added (before -> after)
- ch12 8 -> 9 (+1): Chen Yun (reconciled from ch23; see below).
- ch13 8 -> 9 (+1): Tilanqiao Prison (提篮桥, place).
- ch14 11 -> 20 (+9): Kang Youwei, Song Meiling (+ morphine-plant charge graded),
  Ji Yun/Xiaolan, Zhang Shizhao, Huang Jinrong, Lu Xun, Cai Yuanpei, the Four Great
  Families (concept; IDs Song Ziwen = T.V. Soong), and the Civil Rights League
  chronology flag (the League postdates Yang Du's 1931 death).
- ch15 19 -> 24 (+5): Tan Sitong (+ Tang Caichang), Renaissance Society/Blue Shirts
  (reconciled from ch21), Eugene Chen, Bo Gu, the Red China News Agency -> Xinhua.
- ch16 8 -> 8 (+0): chapter already densely annotated at FN-batch level (Longhua
  martyrs, Jiang Fangzhen+Baoding, Han Fuju, No. 76, Yang Fan clique); the Songhu
  Garrison Command is noted at its first appearance (ch03), Qian Dajun at ch03,
  Xiong Shihui/Song Zaisheng given full prose obituaries. No un-covered reader-need
  first appearance found here — a genuine 0, not a skipped sweep.
- ch17 11 -> 13 (+2): the Ningdu Uprising / Twenty-sixth Route Army (event, 宁都),
  Long Yun.
- **FN3 total: +18 notes. Book 409 -> 427. ch12-ch17: 65 -> 83.**

### Reconciliations (mandated by the FN3 kickoff; pre-existing later notes trimmed)
- **Chen Yun:** first appears ch12 ("Chen Yun led the Section"); the full ID note
  sat at ch23. Added the ID at ch12 (first appearance) and trimmed the ch23 note to
  a cross-reference to chapter 12.
- **Renaissance Society / Blue Shirts:** first appears ch15; the definition sat at
  ch21. Added the full note at ch15 (first appearance) and trimmed the ch21 note to
  a cross-reference to chapter 15.

### NOT re-noted (already placed earlier — cross-referenced, no second note)
- Chiang Kai-shek, Gu Shunzhang, Chen Geng, Yang Dengying, Zhang Daofan, Chen Lifu,
  Kang Sheng (ch09/ch12), Peng Pai, Ke Lin (ch04), Whampoa, Green Gang, Red Squad /
  Dog-Beating Squad, Avenue Joffre, French Concession/International Settlement,
  Songhu Garrison Command (ch03), Mixed Court (ch02), Qian Dajun (ch03) — ch12/ch16.
- Ren Bishi (bio kept at ch13, first substantive treatment; ch02 arrest + ch12
  glancing mention left as-is), Guan Xiangying (bio at ch13; ch12 glancing mention
  left un-noted, per the Ren Bishi pattern), Wang Ming (ch02), Pavel Mif (ch00-05),
  International Red Aid/MOPR (ch13), May Fourth (ch04), Fifth/Sixth Congresses,
  August 7 Conference, Communist University of the Toilers of the East (ch04).
- Yang Du + Du Yuesheng (full notes at ch14, correctly placed — first substantive
  appearance), Political Study Clique + Reorganizationists + Qi Baishi + Cihai +
  Yang Xianzhen + Zhang Xun's restoration (all noted ch14 already), Peace Planning
  Society / "Six Gentlemen" / Hongxian (folded into the Yang Du note), China Mutual
  Advancement Society (共进会, covered in the Du Yuesheng note), Song Qingling (ch03).
- Fu Zuoyi, Wang Ruofei, Marco Polo Bridge Incident, March Eighteenth massacre,
  Kang Sheng land reform, Edgar Snow / Red Star Over China, Dong Jianwu, Pu Huaren,
  T.V. Soong (ch15 note kept; IDed again in the ch14 Four Great Families note),
  Juntong, Xi'an Incident (ch04), Zhang Xueliang (ch07/ch08) — all noted already.
- Li Qiang (ch00), May Thirtieth (ch01), Bose/Longzhou Uprising (ch17 existing),
  Southern Bureau, Marconi, Zhang Huizan, He Yingqin (ch03), Zunyi/Long March (ch04),
  Central Soviet / Chinese Soviet Republic (ch00/ch02) — all noted already.
- Deliberately left unfootnoted (prose gives a full placement, or too minor/self-
  glossed): Tan Zhongyu, Zhou Huinian, Hu Egong, Mei Baoji, Liu Shaobai, Song
  Zaisheng/Song Qihua, Xiong Shihui, Chen Zhigao, Pan Zhenya, Huang Dinghui (all
  given full prose bios in-text); Wang Jiaxiang (glancing, inside a quoted memoir);
  Shen Junru, Yan Fu, Liu Shipei, Yu Dafu, Eugene Chen's colleagues, and the string
  of one-appearance agents, detectives, cover names, streets, and venues.

### Items flagged for FN5 whole-book reconciliation (first appearance precedes FN3 scope)
- **shikumen** (Shanghai row-house type): recurs heavily from ch02 on; genuinely
  un-noted book-wide. First appearance ch02 is out of FN3 scope; note it at ch02 in
  FN5 (a real reader-need term).
- **Shen Bao**: noted at ch17, but first appears ch10; the note is a chapter late.
- **Sun Chuanfang** (warlord, first ch05), **Baoding Army Officers' Academy** (first
  ch03, contextualized inside the ch16 Jiang Fangzhen note), **Sun Yat-sen University
  Moscow** (noted ch18, first appears ch03) — all noted-or-glossed but not at their
  true first appearance; FN5 nicety.
- **互济会 rendering drift**: the same relief society is rendered "China Relief
  Society" (ch02, where it is noted) and "China Mutual Aid Society" (ch14/ch15). A
  glossary/prose-consistency item for FN5, not a footnote fix (prose is frozen).

### Fact-checking
Every added identification checked against real scholarship (English Wikipedia,
China Daily, and academic biographies) before authoring; verdict stated in each
note. NO Grok/Grokipedia or any AI-written reference used (both appeared in result
lists for Bo Gu, Long Yun, and Eugene Chen and were rejected). Graded/flagged
claims: the Song Meiling morphine-plant charge (the author's hostile assertion,
uncorroborated); the Civil Rights League chronology (the League postdates Yang Du's
death, so his "participation" cannot be literal — the discrepancy is the source's);
the Four Great Families label (a partisan concept; the families' prominence real,
the sweeping capital-control figures a partisan estimate). Long Yun birth year 1884
per Wikipedia (a secondary source gives 1888; 1884 used).

### Hanzi discipline
People notes carry NO hanzi. Four term/place/event notes carry hanzi as numeric
character references generated programmatically from glossary.json strings (never
hand-typed): 提篮桥 (Tilanqiao, places), 复兴社 + 蓝衣社 (Renaissance Society / Blue
Shirts, organizations), 宁都 (Ningdu, places). Each byte-matched to the glossary and
verified intact in the built XHTML. Four Great Families, Red China News Agency /
Xinhua use pinyin (glossary lacked the terms). No U+FFFD in any text file; the only
U+FFFD byte-matches in the EPUB are inside PNG image binaries.

### QC
- check_apparatus.py: 0 failures, 0 warnings.
- Build: 28/28 chapters, **427 notes**, 496 pagebreaks. qa_epub PASS (427
  refs/bodies/backlinks resolve, sequential). epubcheck 5.1.0: 0 fatals / 0
  errors / 0 warnings.
- Every new anchor verified a unique verbatim substring of its reading file before
  merge (all 18 count==1). No prose/number/paragraph change (notes-only pass).

## FN4 — footnote-density pass, ch18-ch22 (FOOTNOTE_PASS.md batch 4)

Fourth batch of the commissioner's footnote-density pass (the radio men and cipher
work; the Gu Shunzhang defection and its averting; the Yun Daiying, Cai Hesen, and
Xiang Zhongfa betrayals; the Chen Geng and Wang Genying manhunts; the Ding Ling
abduction and the Yang Xingfo assassination). Content FROZEN: notes ADDED and
reconciled only. No prose, number, name, date, or paragraph change (verified: git
diff touches only notes.json + data/fn4_notes.json + docs + the rebuilt EPUB; no
out/ch*_reading.md edited).

### Branch
Session opened on stray branch `claude/zhou-enlai-fn4-footnotes-2kwtag` (== origin/
claude/zhou-enlai at FN3's HEAD, 0/0 divergence). Per CLAUDE.md rule 2 the canonical
working branch is `claude/zhou-enlai`; checked it out, reset to origin, did all FN4
work there. Stray branch carried no unique commits, so nothing to fold; deleted at
close.

### data/zh decision
Not regenerated (parity scaffold, not needed for a notes-only pass; same rationale
as FN1/FN2/FN3). Anchors verified unique verbatim substrings of out/<id>_reading.md
by apparatus_merge (all 14 count==1); hanzi taken from glossary.json (gloss_hanzi.py)
and emitted as numeric character references generated programmatically from the
glossary string; fact-checking against external scholarship.

### Notes added (before -> after)
- ch18 15 -> 19 (+4): the Naigai Cotton Mill (place/institution), Gu Zhenghong
  (person; May Thirtieth trigger, x-ref ch01), Deng Zhongxia (person; x-ref the
  Canton-Hong Kong strike ch10), Wayaobao (place; the Dec 1935 conference and CC
  seat).
- ch19 9 -> 10 (+1): the Comintern's Far Eastern Bureau (org; x-ref the Noulens
  note ch21).
- ch20 12 -> 14 (+2): Qiu Jin (person), the Young China Association (org).
- ch21 11 -> 14 (+3): the 19th Route Army (unit; x-ref the Jan 28 Incident ch20),
  the Eighth Route Army (unit; x-ref the New Fourth Army ch04), the Executive Yuan
  (office).
- ch22 10 -> 14 (+4): Agnes Smedley (person; reconciled from ch23 — see below),
  Academia Sinica (org), Zhang Wentian (person), Yang Shangkun (person).
- **FN4 total: +14 notes. Book 427 -> 441. ch18-ch22: 57 -> 71.**

### Reconciliation (mandated by the FN4 kickoff; pre-existing later note trimmed)
- **Agnes Smedley:** first appears ch22 ("its American members Agnes Smedley and
  Harold Isaacs"); the full ID note sat at ch23. Added the ID at ch22 (first
  appearance) and trimmed the ch23 note to a cross-reference to chapter 22.

### NOT re-noted (already placed earlier — cross-referenced, no second note)
- **People:** Li Lisan (ch01), Li Qiang (ch00), Zhou Enlai/Chiang Kai-shek/Mao
  Zedong (early), Gu Shunzhang, Chen Geng, Zhang Guotao (ch01/ch05), Wang Ming
  (ch02), Pavel Mif, Qian Zhuangfei, Li Kenong, Hu Di, Xu Enzeng, Cai Mengjian,
  Zhang Daofan (ch06), Chen Lifu (ch06), Kang Sheng, Pan Hannian, Nie Rongzhen,
  Chen Yun (ch12), Yun Daiying (ch02, full bio kept at ch20 where he is the
  subject), Cai Hesen (ch04, full bio kept at ch20 as subject), Xiang Jingyu
  (ch20), Xiang Zhongfa (ch20 as subject), Bukharin (ch20), Ren Bishi (ch13),
  Guan Xiangying (ch13), Deng Yingchao (ch00), Zou Taofen (ch07), Cai Yuanpei
  (ch14), Song Qingling (ch03), Lu Xun (ch14), Ding Ling/Pan Zinian/Ying
  Xiuren/Hu Yepin (ch22 existing), Dai Li/Juntong/Zhongtong (ch07), Edgar Snow
  (ch15), Liu Ding (ch04), Liu Bocheng (ch01), Zhang Xueliang (ch07), Zhang
  Huizan ("Butcher Zhang," ch18 existing), Yang Zhihua (ch09), Tang Enbo (ch18
  existing), Seeckt/Sorge (ch18 existing), Xia Yan (ch18 existing), Yang Quan
  (full bio at ch22, his first substantive treatment; the glancing ch14/ch21
  mentions left as-is, per the Ren Bishi pattern).
- **Places/orgs/events/terms:** May Thirtieth (ch01), May Fourth (ch04),
  April 12 coup, Northern Expedition (ch01), Whampoa (ch03), Green Gang, French
  Concession/International Settlement, Avenue Joffre, Red Squad/Dog-Beating Squad,
  Songhu Garrison Command (ch03), Sixth Congress / Fifth Congress, August 7
  Conference (ch02), Comintern (ch00), Central Soviet (ch00/ch02), Fourth Plenum
  of the Sixth CC (ch19 existing), Cheka (ch00) and GPU (ch19), work-study-in-
  France movement (ch04), Reorganizationists (ch04), the "Third Party" (folded
  into the Deng Yanda note ch04), Long March / Zunyi (ch04), 1911 Revolution /
  Tongmenghui (ch04), Fourth Front Army (Zhang Guotao's, ch01/ch19), Hilaire
  Noulens / Pan-Pacific Trade Union Secretariat (ch21 existing), China Forum /
  Harold Isaacs (ch21 existing), SACO (ch22 existing), New Fourth Army (ch04),
  Red China News Agency -> Xinhua (ch15), League of Left-Wing Writers / Longhua
  Martyrs (ch02/ch09/ch20), January 28 Incident (ch20 existing), Renaissance
  Society/Blue Shirts (ch15), Canton-Hong Kong strike (ch10), Barbusse (named in
  the ch21 Noulens note).
- **Deliberately left unfootnoted** (prose gives a full placement, or too minor/
  self-glossed): Shen Zemin and Chen Changhao (the ch19 prose gives their Party
  posts; both peripheral to the defection narrative), He Chengjun, Yang Qingshan,
  Zhang Chong, Gu Jianzhong, Zhang Wen/Guodong, Meng Zhen, Lou Zhendan, Yang
  Yuqing (KMT/memoirist figures the prose places), Tan Renfeng / Song Jiaoren /
  Huang Xing (1911 figures the ch21 prose glosses in full), Lampson, Gu Zhenglun,
  Deng Wenyi, Wu Zhongxin, Yu Xuezhong (prose-covered KMT men), the women political
  prisoners given prose bios (Shuai Mengqi, Xia Zhixu, Qian Ying, Tan Guofu, Wang
  Genying herself), He Xiangning, Liu Yazi, Ye Shengtao, Israel Epstein, Feng
  Xuefeng, the Barbusse/Rolland/Vaillant-Couturier list of foreign supporters, and
  the string of one-appearance agents, cover names, streets, hotels, and venues.

### Items flagged for FN5 whole-book reconciliation (first appearance precedes FN4 scope)
- **E-Yu-Wan / Hubei-Henan-Anhui Soviet:** the full base-area note sits at ch19,
  but the base is first named ("E-Yu-Wan") at ch15 (also ch17). A placement nicety
  for FN5 (move to ch15 or cross-ref); the note itself is good and correct.
- **Li Mingrui** (warlord-general who joined the Deng Xiaoping Bose Uprising): first
  appears ch17, un-noted book-wide. Note at ch17 in FN5 if judged a reader-need.
- **Third Plenum of the Eleventh Central Committee** (the 1978 reform turning point):
  recurs from ch04 (also ch18, ch22), un-noted as an event. Note at ch04 in FN5.
- **Hu Yepin** is touched by notes at ch09 (Oriental Hotel meeting), ch20 (Longhua
  Martyrs collective), and ch22 (his individual ID as Ding Ling's companion). First
  appearance ch09. The three are complementary, not duplicative, but FN5 should
  confirm the collective-vs-individual split reads cleanly.
- (Carried from FN3, still open: shikumen first at ch02; Shen Bao noted ch17, first
  ch10; Sun Chuanfang first ch05; Baoding Academy first ch03; Sun Yat-sen University
  Moscow noted ch18, first ch03; the 互济会 "China Relief Society" vs "China Mutual
  Aid Society" rendering drift.)

### Fact-checking
Every added identification checked against real scholarship (English Wikipedia,
Cambridge/academic histories, official CCP-history sites, the PRC foreign-ministry
biography for Zhang Wentian) before authoring; verdict stated in each note. NO
Grok/Grokipedia or any AI-written reference used (Grokipedia surfaced in result
lists for Gu Zhenghong/May Thirtieth, Zhang Wentian, the 19th Route Army, and the
Far Eastern Bureau, and was rejected each time). Dates cross-checked: Gu Zhenghong
killed 15 May 1925 (No. 7 Naigai mill); Deng Zhongxia shot Nanjing 21 Sept 1933;
Wayaobao Conference 17 Dec 1935; 19th Route Army — Jan 28 1932 Shanghai defense,
Fujian People's Government proclaimed 22 Nov 1933, crushed Jan 1934; Zhang Wentian
head of the CC from Zunyi (Jan 1935) to 1943, purged at Lushan 1959; Yang Shangkun
PRC president 1988-1993.

### Hanzi discipline
People notes (Gu Zhenghong, Deng Zhongxia, Qiu Jin, Agnes Smedley, Zhang Wentian,
Yang Shangkun) carry NO hanzi. Two term/place notes carry hanzi as numeric character
references generated programmatically from glossary.json strings (never hand-typed):
瓦窑堡 (Wayaobao, places) and 少年中国学会 (Young China Association, organizations);
each byte-matched to the glossary (both "attested") and verified intact and singular
in the built XHTML. The Naigai mill, the Far Eastern Bureau, the 19th/Eighth Route
Armies, the Executive Yuan, and Academia Sinica use pinyin/English (the glossary
lacks those terms; per FOOTNOTE_PASS 6, pinyin is preferred to a hand-typed glyph).
No U+FFFD in any text file or in the EPUB xhtml.

### QC
- check_apparatus.py: 0 failures, 0 warnings.
- Build: 28/28 chapters, **441 notes**, 496 pagebreaks. qa_epub PASS (441
  refs/bodies/backlinks resolve, sequential). epubcheck 5.1.0: 0 fatals / 0
  errors / 0 warnings.
- Every new anchor verified a unique verbatim substring of its reading file before
  merge (all 14 count==1). No prose/number/paragraph change (notes-only pass).

## FN5 — footnote-density pass, ch23-ch27 + whole-book close-out (FOOTNOTE_PASS.md batch 5, LAST)

Final batch of the commissioner's footnote-density pass (the manhunt survivors
and the radio-line reconstruction; Gu Shunzhang's shameful end; the Wu Hao Notice
affair; the Conclusion and Afterword), plus the whole-book apparatus
reconciliation and close-out. Content FROZEN: notes ADDED and reconciled only. No
prose, number, name, date, or paragraph change (verified: git diff touches only
notes.json + data/fn5_notes.json + scripts/recovery/fn5_*.py + docs + the rebuilt
EPUB; no out/ch*_reading.md edited).

### Branch
Session opened on stray branch `claude/zhou-enlai-fn5-footnotes-56c6dt` (== origin/
claude/zhou-enlai at FN4's HEAD; the local claude/zhou-enlai was one commit behind
and was reset to origin). Per CLAUDE.md rule 2 the canonical working branch is
`claude/zhou-enlai`; checked it out, reset to origin, did all FN5 work there. Stray
branch carried no unique commits beyond origin/claude/zhou-enlai, so nothing to
fold; deleted at close (local + remote).

### data/zh decision
Not regenerated (parity scaffold, not needed for a notes-only pass; same rationale
as FN1-FN4). Anchors verified unique verbatim substrings of out/<id>_reading.md by
apparatus_merge (all 16 count==1); hanzi taken from glossary.json (gloss_hanzi.py)
and emitted as numeric character references generated programmatically from the
glossary string; fact-checking against external scholarship.

### Notes added (before -> after) — the tail (ch23-ch27)
- ch23 14 -> 17 (+3): the State Political Security Bureau (org; the Soviet's
  GPU-modeled political police, Deng Fa its first head), Ma Haide/George Hatem
  (person; the first foreigner in the CCP, met through the Smedley/Liu Ding circle
  this chapter describes), the Dragon Boat Festival (custom/term).
- ch24 8 -> 8 (+0): a genuine 0, not a skipped sweep. Dick Wilson (source) is noted
  already; Yang Hu is noted at ch01 (the tiger-wolf pun); the Cheka/GPU, the C.C.
  clique, and the string of Zhongtong/Juntong agents are either noted earlier or
  given full prose placement inside the chapter's own quotations.
- ch25 8 -> 10 (+2): Shi Liangcai (person; the Shen Bao publisher assassinated by
  Dai Li's men in 1934), Tao Xingzhi (person; the Dewey-trained educator). The whole
  Cultural-Revolution frame is already noted: Lin Biao / Jiang Qing / the Gang of
  Four / the Cultural Revolution and the Tiananmen Incident all carry full notes at
  ch25 (see below), and the Awakening Society / Nankai and Kang Sheng are noted here
  too.
- ch26 7 -> 8 (+1): Shen Anna (person; the Party's long-serving stenographer-mole in
  the Kuomintang Central HQ). Yan Baohang + the Barbarossa-warning claim (graded),
  Xiong Xianghui / Hu Zongnan / the "Three Later Heroes," and Zhang Kexia / the
  Huaihai Campaign are already noted; Dimitrov is self-glossed in the prose.
- ch27 1 -> 1 (+0): the Afterword needs nothing new (Mu Xin's own closing note).
- **Tail subtotal: +6 notes.** The tail was already densely annotated during the
  B13/B14 translation batches, so FN5's tail additions are modest by design.

### Notes added (before -> after) — whole-book reconciliation (first appearance precedes ch23)
Clearing the FN3/FN4 "Items flagged for FN5" backlog, each noted at its true
book-wide first appearance:
- ch02 22 -> 23 (+1): shikumen (Shanghai row-house type; recurs from ch02 on).
- ch03 19 -> 20 (+1): Sun Yat-sen University in Moscow (first appears ch03, Zhang
  Kexia; the full note had sat at ch18 -> trimmed to a cross-ref).
- ch04 34 -> 35 (+1): the Third Plenary Session of the Eleventh Central Committee
  (Dec 1978; the reform turning point the book dates rehabilitations from).
- ch05 20 -> 21 (+1): Sun Chuanfang (warlord of the lower Yangzi; assassinated 1935).
- ch10 12 -> 13 (+1): the Shen Bao (first appears ch10; the ID had sat at ch17 ->
  ch17 trimmed to the author's-device note + cross-ref).
- ch14 20 -> 22 (+2): the China Mutual Aid Society (bridged to the China Relief
  Society note at ch02 — the same body, renamed in 1929; see the rendering note
  below), and Ta Kung Pao (the Tianjin daily, first appears ch14).
- ch15 24 -> 25 (+1): the E-Yu-Wan Soviet (first named "E-Yu-Wan" at ch15; the full
  base-area note had sat at ch19 -> trimmed to a cross-ref keeping the ch19-specific
  Zhang Guotao detail).
- ch16 8 -> 9 (+1): the Baoding Army Officers' Academy (first appears ch16, Qian
  Dajun — NOT ch03, whose "Baoding" is Baoding Road, a Shanghai street; the FN4 flag
  was corrected on this point).
- ch17 13 -> 14 (+1): Li Mingrui (Guangxi general, Bose/Longzhou uprisings; killed
  1931).
- **Reconciliation subtotal: +10 notes.**
- **FN5 total: +16 notes. Book 441 -> 457. ch23-ch27: 38 -> 44.**

### Reconciliations (pre-existing later notes trimmed to cross-references)
- **Shen Bao:** ID added at ch10 (first appearance); ch17 note trimmed to the
  author's-device observation + cross-ref to chapter 10.
- **Sun Yat-sen University Moscow:** ID added at ch03 (first appearance); the ch18
  "Study and work at 'Sun Yat-sen University'" note trimmed to a cross-ref.
- **E-Yu-Wan / Hubei-Henan-Anhui Soviet:** ID added at ch15 (first appearance); the
  ch19 note trimmed to a cross-ref, keeping the ch19-specific "driven out in 1932
  under Zhang Guotao" detail.

### 互济会 rendering "drift" — resolved as a historical rename, not an error
The FN3 flag treated "China Relief Society" vs "China Mutual Aid Society" as a
rendering drift. It is not: the glossary maps two DIFFERENT Chinese names
consistently — 中国济难会 -> "China Relief Society" (the 1925 original, attested) and
中国互济会 -> "China Mutual Aid Society" (the 1929 rename, decided). The prose is
therefore correct and consistent, and content stays frozen. To spare the reader the
two-name confusion, a bridging note at the first "China Mutual Aid Society" (ch14)
ties it to the China Relief Society note at ch02. No glossary or prose change.

### NOT re-noted (already placed earlier — cross-referenced or left, no second note)
- **Cultural-Revolution personalities:** Lin Biao, Jiang Qing, the Gang of Four
  first appear as glancing biographical asides at ch04 (Liu Ding's persecution; the
  author's own imprisonment); the full identification note is kept at ch25, where the
  Wu Hao affair makes them the subject (the Ren Bishi placement pattern). The
  Cultural Revolution itself is noted early (ch01/ch02).
- **Already noted, reused unchanged:** Chen Yun (ch12), Kang Sheng, Pan Hannian,
  Chen Geng, Li Kenong/Qian Zhuangfei/Hu Di (Three Heroes of Longtan), Xu Enzeng,
  Zhang Daofan, Chen Lifu/Chen Guofu (C.C. clique), Dai Li/Juntong/Zhongtong,
  Cheka (ch00)/GPU (ch19), the Kwantung Army (in the ch08 Mukden note), the Chinese
  Eastern Railway Incident (ch08), Yang Hu (ch01 pun note), Dick Wilson (ch24), the
  Long March/Zunyi (ch04), Central Soviet/Chinese Soviet Republic (ch00/ch02),
  Whampoa (ch03), Rewi Alley (ch23), Agnes Smedley (ch22), Fang Zhimin (ch23),
  Xiong Xianghui/Hu Zongnan (ch05/ch26), Zhang Kexia/Huaihai Campaign (ch26), the
  Nineteenth Route Army (ch21), Deng Xiaoping, Feng Yuxiang, Yan Xishan, Zhang
  Xueliang, Song Qingling, Ding Ling, the New Fourth Army / Eighth Route Army.
- **Hu Yepin cluster confirmed complementary (FN4 open item):** ch09 (the Oriental
  Hotel arrest meeting), ch20 (the Longhua Martyrs collective), ch22 (his individual
  bio as Ding Ling's companion). Three anchors, three local needs; reads cleanly, no
  merge.
- **Deliberately left unfootnoted** (prose gives a full placement, or too minor/self-
  glossed, or inside a quoted memoir): The Voice of China (glancing, inside Alley's
  quoted memoir, self-contextualized as a publication); Kuang Hui'an, Shen Shouya,
  Zhang Qiuyang, Xu Qiang, Shao Fumin, Zhang Keyun, Old Ju, Wu Chengfang, Huang Ping,
  Lu Weiliang, "Little Cantonese," Rewi Alley's household (Gumperson, Mike), Herbert
  Wunsch, Erich Landauer, Bocic, Li Du, Zhou Zhirou, Li Jinde, Kang Ze (all prose-
  placed or one-appearance); the crowd of self-glossed Zhongtong/Juntong agents in
  ch24 (Huang Kai, Meng Zhen, Lin Jinsheng, Gu Jianzhong, Zhang Guodong, Chen Weiru,
  Lin Chengyin, etc., each given a full prose obituary inside the chapter's own
  quotations); Zhang Mutao; Wu Faxian, Xu Shiyou, Xie Fuzhi, Wang Dongxing, Zhang
  Chunqiao/Yao Wenyuan (Cultural-Revolution figures the prose or the ch25 Gang-of-
  Four note places); the Min-Zhe-Gan (Fujian-Zhejiang-Jiangxi) Soviet (covered by the
  E-Yu-Wan and Fang Zhimin notes).

### Fact-checking
Every added identification checked against real scholarship (English/Chinese
Wikipedia, Baidu Baike, Cambridge China Quarterly, University of Hawai'i Press,
SHINE/China Daily, and academic biographies) before authoring; verdict stated in
each note. NO Grok/Grokipedia or any AI-written reference used (Grokipedia surfaced
in result lists for Ma Haide, the Longzhou Uprising, and the assassinations query,
and was rejected each time). Dates cross-checked: Shen Anna (Shen Wan) 1915-2010,
placed via Zhou Enlai; Shi Liangcai 1880-1934, killed 13 Nov 1934 by Dai Li's
agents; Sun Chuanfang 1885-1935, shot 13 Nov 1935 by Shi Jianqiao; Li Mingrui
1896-1931; Ma Haide (George Hatem) 1910-1988; Baoding Academy 1912-1923 (~11,000
officers); Deng Fa first head of the State Political Security Bureau (Ruijin, 1931);
Tao Xingzhi 1891-1946 (Dewey/Columbia); Third Plenary Session of the 11th CC, Dec
1978.

### Hanzi discipline
People/place/event notes carry NO hanzi (Ma Haide, Shi Liangcai, Tao Xingzhi, Shen
Anna, Sun Chuanfang, Li Mingrui, the State Political Security Bureau, the Third
Plenary Session, Baoding Academy, E-Yu-Wan, shikumen, the Dragon Boat Festival, Sun
Yat-sen University Moscow — all use pinyin/English, as the glossary lacks the term or
house style forbids hanzi in people notes). Three org/work notes carry hanzi as
numeric character references generated programmatically from glossary.json strings
(never hand-typed): 申报 (Shen Bao, ch10), 中国互济会 (China Mutual Aid Society, ch14),
大公报 (Ta Kung Pao, ch14). Each byte-matched to the glossary and verified intact and
singular in the built XHTML. No U+FFFD in any text file or in the EPUB xhtml.

### term_ledger.md
FN5 added NO glossary rows (the glossary already held every hanzi the new notes
needed), so glossary.json is byte-identical and out/term_ledger.md (847 decided
renderings) is already current — no refresh needed.

### QC
- check_apparatus.py: 0 failures, 0 warnings.
- Build: 28/28 chapters, **457 notes**, 496 pagebreaks. qa_epub PASS (457
  refs/bodies/backlinks resolve, sequential). epubcheck 5.1.0: 0 fatals / 0 errors /
  0 warnings (EPUB 3.3).
- Every new anchor verified a unique verbatim substring of its reading file before
  merge (all 16 count==1). No prose/number/paragraph change (notes-only pass).
- **The footnote-density pass (FN1-FN5) is COMPLETE.** Further work is a corrections
  pass.
