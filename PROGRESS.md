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
