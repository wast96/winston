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

Awaiting the commissioner's approval of the structure and batch plan (first
gate). On approval, Batch 1 (Preface + Chapter 1) begins in a fresh chat.
