# HANDOFF — Zhou Enlai: Commander of the Hidden Front

Fresh-session handoff. The paste-ready kickoff is first; everything below it is
the state a new session needs. Batch 1 is COMPLETE and sits at the first-chapter
voice gate (Step 0c), awaiting commissioner approval. Do NOT start Batch 2 until
the voice is approved.

## Message to paste into the next chat

```
Zhou Enlai B02

Read CLAUDE.md, then HANDOFF.md, then STYLE.md, then book.json. Do Batch 2 =
ch02 (一科——特科的"总管家", PDF 60-76, printed 16-32) + ch03 (情报科长"王庸"——陈赓,
PDF 77-94, printed 33-50), end to end per the CLAUDE.md pipeline. Work on branch
claude/zhou-enlai; expect a stray per-task branch and consolidate onto it
(CLAUDE.md rule 2).

BEFORE translating, read the final two paragraphs of ch01 in
out/ch01_reading.md: HANDOFF describes the voice, but those pages ARE the voice.
ch01 is the FROZEN reference; run check_register.py --ref out/ch01_reading.md on
every unit.

Pipeline notes specific to THIS book (all proven in B01, do not rediscover):
- Body offset is a CONSTANT 44: printed = PDF - 44. Read the folio at each
  opener anyway. ch02 opens PDF 60 = printed 16 (verified); ch03 opener PDF 77 =
  printed 33 is the survey's inference, folio-verify it.
- OCR: ocr_crop.py FIRST LAST --left 0.11 --right 0.90 --top 0.135 --bottom 0.95
  --lang chi_sim --psm 6 --running-head "隐蔽战线统帅周恩来". Verify pgrep -c
  tesseract is 0 after. Second read via ocr_dual.py.
- Paragraph assembly: do NOT trust indents.py on this book (it scans page
  furniture and embedded photos and misaligns). Delete data/indent/ for the
  range and let assemble.py use tesseract's blank lines. Then FIX page-seam
  merges by reading the page images: tesseract emits no paragraph blanks on some
  pages, so a paragraph that ends at a page bottom silently merges with the next
  page's opener. Verify every seam and every blank-less page against the scan.
- The book has its OWN footnotes (author source citations) and embedded photos.
  Strip footnote lines and photo/caption lines from the body OCR before
  assembly; run find_figures.py FIRST LAST for the photos; reproduce the
  author's footnotes as notes tagged "Author's note."; fold photos into
  figures.json with real alt text and a translator caption.
- Crop-verify every name, number, alias, unit designation BEFORE writing; record
  fixes in data/ocr_fixes.json via apply_fixes.py. Watch 陈赓 (ch03's subject,
  alias 王庸 / "Wang Yong"), 顾顺章 (alias 化广奇), 钱大钧 (ch03s04).
- Checks: verify_unit per unit; check_align; check_content --config
  data/check_config.json (regenerate that config to include the new units);
  check_numbers with --noise data/noise.txt; qc_entities on the bilinguals;
  apparatus via apparatus_merge.py (check_apparatus clean); check_register --ref.
- Footnotes at reader-model density; put fact-check verdicts IN the note; never
  source LLM content. Note at FIRST appearance book-wide (grep notes.json and
  the earlier reading files first); keep a "NOT re-noted" list in PROGRESS.
- Cite the book's PRINTED FOLIO in notes, never the PDF page.
- Build the cumulative EPUB, qa_epub green, epubcheck (/tmp/epubcheck-5.1.0).
- Update PROGRESS.md and HANDOFF.md; commit and push to claude/zhou-enlai.

Deliver in THIS chat: the built EPUB attached, AND the next kickoff pasted
verbatim in a fenced code block. Both, every batch.
```

## Status: what is DONE

- **Survey (Step 0a/0b): approved.** Metadata + 28-unit structure in book.json.
- **STYLE.md written; read every batch.**
- **B01 = ch00 (Preface) + ch01: translated, all checks green, EPUB built.**
  At the voice gate (Step 0c), awaiting approval. Full record in PROGRESS.md.
- **Offset corrected book-wide:** body offset is a constant 44 (was 43 in the
  survey); every body pdf_page in book.json bumped +1, ch00 to PDF 36, pdf_end
  to 581. printed_page values were already correct.

## Tooling in place / do not revert

- book.json drives the build. Deliverable is out/zhou-enlai.epub.
- data/figs/cover.png is the book's own cover (byte-copied by the builder).
- **ocr_crop.py:** added `folio_present()` (indents.py needs it; was missing)
  and taught `strip_folio` to drop bare-digit folios. Crop box measured (above).
- **check_content.py:** `name_map` skips '_'-prefixed meta keys.
- **data/ocr_fixes.json:** 19 crop-verified readings for ch00/ch01; replay with
  apply_fixes.py on any fresh regen or the mangles return.
- **data/noise.txt:** event-label and numeral-name rules added (四一二 etc.).
- **data/check_config.json:** the check_structure / check_content config;
  regenerate it to add each batch's new units.
- **data/pagemap/ch00.json, ch01.json:** hand-built (correct after the paragraph
  re-splits); the builder emits page markers from them.
- Assembly on this book uses the BLANK-LINE path (see the kickoff); indents.py
  is unreliable here.

## Renderings settled so far (glossary.json is the ledger; check authority.json)

- Principals flagged: 周恩来 Zhou Enlai, 陈赓 Chen Geng (alias 王庸 Wang Yong),
  顾顺章 Gu Shunzhang (alias 化广奇 Hua Guangqi), 李强 Li Qiang (alias 曾培鸿
  Zeng Peihong). Aliases to keep straight also: 伍豪 = Zhou Enlai.
- 中央特科 = the Central Special Section. 特务科 = Special Services Section.
  红队 = Red Squad ("Dog-Beating Squad"). 巡捕房 = concession police; 巡捕 =
  constable. 租界 = the Concessions. 白色恐怖 = White Terror. 共产国际 =
  Comintern (chosen over "Communist International"; hold it). 广州 = Guangzhou.
- Chiang Kai-shek, Wang Jingwei, Chen Duxiu, Borodin, Maring: conventional forms.
- Everything else decided in glossary.json as it comes up; feed decisions back
  into authority.json at book's end.

## Voice sheets (carry-forward; the ch01 reference voice)

- **Mu Xin (author):** confident narrative-history voice with an open partisan
  edge. Heroes are heroes, 叛徒 are traitors, 匪 are bandits. Keep the heat where
  he runs hot (the Shanghai "adventurers' playground" passage, the martyr
  counts); verdicts go in the note, never the prose. Exposition wants short,
  confident sentences, not decoded reference entries.
- **Zhou Enlai:** so far only in reported summary and one terse quoted judgment
  ("Because the whole political line was wrong, we had the intelligence and were
  numb to it all the same..."). Measured, analytic, unshowy. Fill this in as he
  speaks directly in later chapters.
- **Li Qiang (in his own 1981 testimony, ch01):** plain, colloquial, first-
  person reminiscence, fond of concrete detail and asides ("Fat Dong, Dong
  Xingwu perhaps, or Dong Shengwu"). Contractions and loose connectors are
  right here; keep it spoken, not tidied into report prose. He is a PRINCIPAL
  (ch17 is his), so this voice recurs.
- Chen Geng, Gu Shunzhang, Li Kenong: not yet heard directly; establish at first
  dialogue.

## Where the story stands

Preface and ch01 done: the political rationale for Party intelligence work (the
White Terror after 1927, 知己知彼 from the Sunzi), the Wuhan Special Services
Section as the seed, and the founding of the Central Special Section in Shanghai
under Zhou Enlai, autumn 1927, with its four sections (One = general
office/steward; Two = intelligence; Three = the Red Squad; Four = radio) and the
Nov 1928 Special Committee (Xiang Zhongfa, Zhou, Gu Shunzhang). ch02 opens the
detailed treatment of Section One.

## Exact next-batch scope

- **B02** = ch02 (一科, PDF 60-76, printed 16-32; sections ch02s01-03) + ch03
  (陈赓, PDF 77-94, printed 33-50; sections ch03s01-04). Then B03 per
  out/SURVEY.md.

## Open traps / environment state

- Body offset constant 44; folio-verify each opener anyway. Front-matter plates
  run to PDF 35; preface PDF 36-38; TOC PDF 39-44 (not translated); body PDF 45+.
- indents.py unreliable on this book; use the blank-line path and verify seams.
- Embedded photos and the book's own footnotes recur; handle per the kickoff.
- OMP_THREAD_LIMIT=1 for tesseract; kill the process GROUP; pgrep -c tesseract
  must read 0 after a run. PaddleOCR absent; use ocr_dual.py.
- epubcheck at /tmp/epubcheck-5.1.0 (may need re-fetch via setup.sh in a fresh
  container).
- Pre-existing failing regression test ("hook stands down on template stub");
  does not affect real batches. See PROGRESS.md.
