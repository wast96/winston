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
