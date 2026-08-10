# PROGRESS — Scales and Claws of Shanghai (上海鱗爪, customs volume)

The running per-batch log. Write it as you go, not at the end. One section per
batch: what was translated (unit ids, PDF and printed ranges), which checks ran
and what they found, notes added (count and numbering), glossary rows added with
status, figures, and anything flagged for the read-through (uncertain readings,
contradictions with scholarship, choices you were unsure of).

## Setup / Survey (2026-08-10)

- Source: image-only PDF, 252 pages, of the 2019 Taipei reprint
  生活在民國的十里洋場：《上海鱗爪》（風俗篇）, Xinrui Wenchuang (Showwe),
  ed. Cai Dengshan, ISBN 978-957-8924-38-3, series 血歷史 140. It is a modern
  RESET (not a facsimile) of the 1933 Shanghai 上海鱗爪, split by the reprint
  into a customs volume; this PDF is that customs volume: author's preface plus
  167 short essays. Clean modern typesetting, Traditional Chinese, vertical
  right-to-left body text, horizontal running heads.
- setup.sh: ran clean; PaddleOCR absent as expected (dual-engine substitute is
  ocr_dual.py per its docstring); epubcheck 5.1.0 present at
  /tmp/epubcheck-5.1.0/epubcheck.jar; checker regression tests green.
- PDF bookmarks: 170, one per essay plus cover/導讀/序, spot-verified accurate
  against the scan (pdf pages, 1-based). Printed TOC (pdf 15-22) folios agree
  with bookmarks throughout the sample checked.
- Offset: printed = pdf - 2, CONSTANT front to back (verified at pdf 13, 23,
  120, 247; no plates, no second front-matter sequence). Body pdf 23-247 =
  printed 21-245. pdf 4, 14, 248, 249, 251 blank or filler; pdf 250 CIP;
  pdf 252 back cover.
- Page furniture (to configure in ocr_crop.py in B01): running head at top
  (recto: essay title, vertical, near-gutter; verso: series title, horizontal)
  plus printed folio as stacked digits in the top outer corner. Body block
  sits below; measure the crop box on B01's pages before OCR. Model
  chi_tra_vert, --psm 5.
- Standing decisions (survey gate, commissioner-approved 2026-08-10): (1) the
  2019 導讀 by Cai Dengshan is EXCLUDED (modern copyrighted text; noted in
  translator_note); (2) the reprint-added period photographs are INCLUDED per
  the commissioner's explicit instruction: run them through the figure
  pipeline per batch (crop from the scan, alt text, caption translating the
  reprint's label and stating provenance: photographs added by the 2019
  editor, not figures of the 1933 book); (3) reprint cover artwork excluded
  (builder generates a typographic cover, consistent with the shelf).
- book.json: metadata filled (series Winston Translations #10); complete
  structure, 168 chapters (ch000 = author's 1933 preface, signed 癸酉七夕
  天虛我生 = Chen Diexian; ch001-ch167 = the essays); 10 proposed batches.
- Skeleton EPUB built (out/scales-and-claws-of-shanghai.epub): qa_epub PASS
  (181 files, 174 documents, all links resolve); epubcheck 5.1.0: 0 errors,
  0 warnings.
- Branch consolidation per rule 2: canonical branch claude/scales-and-claws;
  stray harness branch claude/pdf-source-review-igkdaq carried no unique
  commits, deleted local and remote.
- B01 note: the batch's pdf_range [12,33] contains a gap — preface pdf 12-13,
  then blank pdf 14 and the printed TOC pdf 15-22, body resumes pdf 23. OCR
  only 12-13 and 23-33.

## B01 = ch000-ch001 (pending approval)

- (fill in per the batch)
