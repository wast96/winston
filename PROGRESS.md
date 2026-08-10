# PROGRESS — The Stealthy Ones (忍びの者〈五右衛門釜煎り〉)

## Batch 0 — survey (Step 0a + 0b)

Status: survey delivered; awaiting commissioner approval of the batch plan
(and of the two open decisions below) before Batch 1.

### What the book is
- Japanese historical novel (時代小説) by Tomoyoshi Murayama (村山知義,
  1901–1977); the concluding "Goemon boiled in the cauldron" arc of his
  ninja saga 忍びの者. Scanned 1987 Kobunsha bunko edition.
- Vertical text, right-to-left, dense furigana (rubi). Folio at the top
  OUTER corner; no running head/foot down the margins.
- 537 PDF pages. Body = 8 chapters, printed 5–528 (PDF 7–530). Afterword
  解説 by Musashino Jiro, printed 529–534 (PDF 531–536). Colour cover PDF p1;
  publisher back-cover blurb PDF p537.
- PDF→printed offset is a CONSTANT +2 (printed = pdf − 2), verified at all
  eight chapter openers and the afterword. Text-only book, no plates.
- No internal numbered sections within chapters; continuous prose with
  scene breaks (render as `***`).

### Environment / setup
- setup.sh pack list switched from Chinese to Japanese: `tesseract-ocr-jpn`
  and `tesseract-ocr-jpn-vert` (both installed OK; tesseract 5.x).
- PyMuPDF / Pillow / numpy / opencv installed. epubcheck 5.1.0 fetched to
  /tmp/epubcheck-5.1.0 (works). PaddleOCR NOT installed (expected) — use the
  dual-engine tesseract substitute (scripts/ocr_dual.py).
- `apt-get update` prints a 403 for an unrelated third-party PHP PPA
  (ondrej/php); harmless, the needed packages installed individually.
- Checker regression tests: green.

### OCR geometry (validated on a chapter-1 sample)
- Crop (fractions of page): left 0.06, right 0.96, top 0.09, bottom 0.935.
  This drops the top-corner folio cleanly and keeps all body text.
- OCR: `--lang jpn_vert --psm 5`. Sampled pages OCR'd cleanly with no stray
  folio numerals and correct paragraph starts. Second read: ocr_dual.py.
- Known trap for this book: furigana (rubi) sit beside the kanji and can be
  merged into the main column by OCR — crop-verify names/numbers by eye.

### Deliverables this session
- book.json filled: metadata (Step 0a) + full 8-chapter structure (Step 0b),
  pdf_end/printed_end = 530/528.
- out/SURVEY.md written; skeleton EPUB out/the-stealthy-ones.epub built.
- qa_epub: PASS. epubcheck: 0 fatals / 0 errors / 0 warnings.

### Decisions — RESOLVED by the commissioner (survey approval)
1. Batch granularity: **whole chapters, as surveyed** (8 batches; Chapter 5
   stays a single 102 pp. batch). No pre-splitting.
2. The afterword 解説 (Musashino Jiro): **translate it**, as clearly-attributed
   back matter in the final batch (after ch08).
3. Cover: **generated typographic cover** (default). cover_image left empty.

### Chapter English titles are PROVISIONAL
Confirmed at the voice gate / refined as the book is read. Current drafts:
New Waves; A Warm Current; Surface and Underside; War upon War; The Two of
Them; Earth and Water; Death, Death, Death; Death Throes.
