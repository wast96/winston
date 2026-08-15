# PROGRESS — China's Secret War (中国秘密战)

The running per-batch log. Written as we go. One section per batch: what was
translated (unit ids, PDF and printed ranges), which checks ran and what they
found, notes added, glossary rows added with status, figures, and anything
flagged for the commissioner's read-through.

## Setup / Survey (Step 0a + 0b)

- **Source:** `source.pdf`, 436 PDF pages, image-only scan, no text layer.
  Internet Archive (archive.org/details/zhongguomimizhan0000unse), scanned from
  a Contra Costa County Library copy. Book: 《中国秘密战：中共情报、保卫工作纪实》
  by 郝在今 (Hao Zaijin), 金城出版社 (Gold Wall Press), Beijing, 最新升级图文版
  (2nd ed., 2015-01). ISBN 978-7-5155-1071-2. 报告文学 (reportage). 330,000
  Chinese chars; 27 print sheets; 710×1000 1/16.
- **Script / orientation:** SIMPLIFIED Chinese, horizontal, left-to-right. Use
  `chi_sim` (psm 6). PaddleOCR not installed (weights host unreachable) — use
  the dual-tesseract substitute `scripts/ocr_dual.py`; note that in each batch.
- **Offset:** CONSTANT `printed = pdf - 36` across the whole body. Verified at
  four chapter openers spanning the book (ch2 46→PDF82, ch5 148→184,
  ch10 307→343, ch12 375→411). No interior plate drift — the 图文版 photos are
  inline on numbered pages, not separate unpaginated plate sequences. Section
  opener pdf pages in book.json are computed (printed+36); spot-verify each
  opener's folio at batch time (an inline full-page plate can nudge a single
  section opener by ±1).
- **Front matter:** cover + title + CIP/copyright (PDF 1–4); a photo-plate
  section INTERLEAVED with the printed 目录 (PDF 5–32, its own folio sequences);
  Preface 前言 探秘 (PDF 33–35, its own sequence, printed 1–3; PDF 36 blank).
- **Back matter:** the book carries its OWN apparatus — a section of source
  notes citing the author's interviews (e.g. "王芳：前国务委员、公安部长，2000年6月8日
  采访"), clustered around printed ~391–394 (PDF 427–430); then Afterword 后记
  (PDF 431–434, printed 395–398). PDF 435–436 are the library endpaper +
  Contra Costa County barcode (scan artifact, not book content). **TODO Batch 1
  / final batch:** run `detect_notes.py` to characterize whether the 注释 are
  per-page footnotes or a collected endnote section, and decide how to
  reproduce them.
- **Page furniture:** verso (even) pages print a VERTICAL running title
  （中国秘密战／——中共情报、保卫工作纪实）in the outer (left) margin; recto (odd)
  pages a vertical running head (章 title, or 目录 on the TOC pages). Folio sits
  in the bottom outer corner. Crop the outer-margin running title before OCR;
  measure the body box in Batch 1 and configure `ocr_crop.py`. First batch's
  first engineering task.
- **Structure:** 12 chapters, 86 numbered sections, + Preface + Afterword.
  Recovered from the printed 目录 (PDF 19–31), which is clean and reliable.
  Full structure and English titles in `book.json`; outline in `out/SURVEY.md`.
- **Environment (setup.sh):** tesseract + chi_sim/chi_tra (and -vert) packs
  installed; PyMuPDF/Pillow/numpy/opencv OK; epubcheck 5.1.0 fetched; checker
  regression tests GREEN. Only note: PaddleOCR absent (expected).
- **Skeleton EPUB:** built (14 units, full hyperlinked pending-aware TOC).
  `qa_epub.py` PASS (27 files, all links resolve). `epubcheck` clean
  (0 fatals / 0 errors / 0 warnings).
- **Branch hygiene:** consolidated onto the canonical book branch
  `claude/chinas-secret-war` (per CLAUDE.md rule 2). The harness's stray
  per-task branch `claude/pdf-source-document-kvueuz` carried no commits beyond
  the template baseline; deleted local, and removed from origin.

Structure and batch plan approved. Batch 1 done (below).

## Batch B01 — Preface (ch00) + Chapter 1 (ch01)

Scope: PDF 33-81; printed Preface 1-3, Chapter 1 printed 1-45. Simplified,
horizontal; chi_sim, psm 6. PaddleOCR absent, so the second read is the
dual-tesseract substitute (scripts/ocr_dual.py, psm 6 vs psm 4).

### Pipeline established (do not revert)
- **Page furniture / crop.** Mirror-margin book: the vertical running title
  sits in the OUTER margin (verso left, recto right). Measured crop, per
  parity: recto (odd PDF) [left 0.07, right 0.86], verso (even PDF)
  [left 0.17, right 0.94], shared top 0.045 / bottom 0.93. Validated by OCR
  (no phantom head column). ocr_crop.py gained per-parity overrides
  (--left-even/--right-even/...) and the geometric folio_present() that
  indents.py needs (it was referenced but missing).
- **assemble.py --blank-assist** (new, opt-in): layers tesseract's blank-line
  paragraph signal on top of the indent, gated by the sentence-end test. The
  indent flags desync from the OCR text on the many inline-photo pages, so the
  blank signal is needed; default behavior unchanged.
- **data/txt_fixes.json + apply_fixes.py --txt** (new): pre-assembly per-page
  OCR fixes for mangles that change paragraph structure. Five here: tesseract
  read the fullwidth exclamation as the digit 1, welding paragraphs; restored.
- Reproducible pipeline for ch01 zh: indents 37 81 (NOT 33-36; the preface has
  its own margins and assembles from the blank-line signal), apply_fixes --txt,
  assemble ch00 33 35 --offset 32, assemble ch01 37 81 --offset 36
  --blank-assist, apply_fixes ch00 ch01.

### Translated and checked
- **ch00 (Preface):** 28 body paragraphs. verify_unit CLEAN (parity 28/28,
  numbers 0 unresolved, 2 anchors ok); check_align OK.
- **ch01 (Chapter 1):** 9 sections + a translated "Principal Sources" section.
  299 English body paragraphs. The frozen VOICE REFERENCE is
  out/ch01_reading.md (check_register run: contractions 2.0/1k, em-dash 3.4/1k,
  rhythm CV 0.49).
- **Apparatus:** glossary.json +17 rows (12 flagged principal: Zhou Enlai, Mao
  Zedong, Chen Geng, Gu Shunzhang, Kang Sheng, Li Kenong, Qian Zhuangfei, Hu
  Di, Chiang Kai-shek, Dai Li, Zhu De, Zhang Xueliang; plus the key organs and
  the word tewu). notes.json: 2 for ch00, 19 for ch01 (reader-model density for
  a long 1927-1937 chapter). check_apparatus clean.
- **Build:** cumulative EPUB builds; qa_epub PASS (28 files, 21 notes, all
  links resolve); epubcheck 5.1.0 clean (0 fatals / 0 errors / 0 warnings).
- Builder patch: render_glossary now renders BOTH sectioned and flat glossary
  rows (apparatus_merge writes flat), so the build does not need a manual
  re-sectioning pass each batch.

### KNOWN ISSUE, top follow-up: ch01 zh parity
verify_unit ch01 FAILS parity: zh 269 vs en 299. The zh side is the OCR
reconstruction, and it under-segments on the figure-heavy pages, where the
inline photos defeat BOTH the indent flags and tesseract's blank lines. The
English is one paragraph per TRUE source paragraph (every page was read from
the scan while translating), so this gap is a defect of the zh QC scaffolding,
not a dropped or added translation paragraph. Because check_content and
qc_entities pair zh to en positionally, they are pending this reconciliation
and were not run clean. Reconcile by hand-splitting the merged zh paragraphs
on the figure pages to 299, recording the splits in ocr_fixes.json (\n
insertions) so a fresh checkout reproduces; then rerun verify_unit /
check_content / qc_entities. (data/zh is gitignored copyright text; the tracked
out/ch01_reading.md is the correction surface and is complete and correct.)

### Figures: DEFERRED (deliberate)
figures.json is empty this batch. The 图文版 carries many inline photos (one or
more per body page, captions often vertical in the outer margin) plus a
Shaan-Gan-Ning border-region MAP on printed 39 (PDF 75). Extracting and
cropping them was deferred to keep the voice gate focused on text, voice, and
note density. Recorded here as a deliberate decision, not an oversight; figure
extraction is a follow-up (and the standing approach for all 12 图文 chapters
needs a commissioner decision: reproduce every inline photo, or a curated
subset).

### FINDING: source notes are PER-CHAPTER
The survey expected the book's own source-note apparatus only at the book's end
(printed ~391-394). In fact EACH chapter ends with its own "主要资料"
(Principal Sources) section: ch01's runs printed 42-45 (PDF 78-81), ~42
interview and reference entries. Rendered this batch as a translated "Principal
Sources" section at the chapter's end. This changes the plan for later batches
and for B13's whole-book source-note handling; flag for the commissioner.

### Source errors rendered as printed and footnoted (verdicts stated)
- Jinggangshan base "across Jiangxi, Fujian, and Zhejiang" (printed 14/PDF 50):
  geographically wrong (Zhejiang not part; figures describe the Central Soviet
  Area). CONTRADICTED.
- Li Dazhao's execution dated 1928 (printed 36/PDF 72): actually April 1927.
  CONTRADICTED.
- Security badge letters "GBW" then called the Russian GPU (printed 16/PDF 52):
  the letters do not match GPU. Flagged.
- Contested history footnoted with verdicts: the "AB Corps" as a real
  conspiracy is CONTRADICTED (the CCP's own 2002 verdict, quoted by the author,
  is cited); the author's framing of Mao's role in the Futian purge is noted as
  partisan.
- Rendered-as-printed uncertain name: 曾固林 "Zeng Gulin" (printed 19/PDF 55),
  the 20th Red Army commander arrested at Futian; obscure, possibly a misprint.

### OCR-fix ledgers
- data/txt_fixes.json: 5 pre-assembly fixes (p37/38/64/76/80, ！->1).
- data/ocr_fixes.json: ch00 has 31 crop-verified char + 2 paragraph-split
  fixes; heading restored. ch01 char fixes are NOT yet fully laddered (to be
  done with the parity reconciliation above).

### Environment / checks
- OMP_THREAD_LIMIT=1 throughout; tesseract left 0 orphans (pgrep -c 0).
- setup.sh checker regression tests: one benign FAIL, "hook stands down on
  template stub." That sub-test asserts the Stop hook stands down when
  HANDOFF.md still holds the TEMPLATE placeholder; HANDOFF.md now holds a real
  batch kickoff, so the hook correctly demands it. Not a defect in the checkers
  or the hook; it will "fail" for the life of the project until completion.

### Batch ends at the voice gate (Step 0c)
B01 stops here for the commissioner to judge voice, note density, and
formatting on ch00 + ch01. Do NOT begin B02 until approved.
