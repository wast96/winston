# PROGRESS — The Owl's Castle (梟の城, Shiba Ryōtarō)

Running per-batch log. Written as work happens, not at the end.

## Setup (survey session)

- **Source:** Internet Archive scan `fukuronoshiro0000ryot` (2024), Shinchō
  Bunko edition, ISBN 978-4-10-115201-1, ¥890. 674 PDF pages. Image-only; the
  Archive's embedded text layer OCR'd the vertical Japanese as **Latin script**
  and is pure garbage (unusable — confirmed on several pages). We OCR fresh.
- **Script/orientation:** vertical, right-to-left Japanese with **furigana**
  ruby throughout. OCR model **`jpn_vert`, `--psm 5`**. (setup.sh installs only
  the Chinese packs; `tesseract-ocr-jpn` + `tesseract-ocr-jpn-vert` installed
  manually this session — a setup.sh gap to fix for Japanese books.)
- **Page furniture:** running head 梟の城 and the folio are BOTH at the TOP of
  the page (folio alternates top-outer corner; folios are ARABIC numerals).
  Bottom margin is clean (no running foot). Measured body-text crop:
  **left 0.035, right 0.965, top 0.075, bottom 0.955** (fractions of page).
  This crop gives clean OCR with no furniture contamination.
- **PaddleOCR:** not installed (expected); dual-engine substitute is
  `ocr_dual.py` for batches.
- **Offset (READ folios; do not compute):** printed folio == PDF render page
  for folios **7–302** and again **425–660**, but drifts **+2 render pages**
  across folios ~**338–397** (an unnumbered leaf enters around folio 302–338;
  an apparent 1-leaf scan gap around folio 397–425 brings it back). Each
  opener's folio was read directly off the scan. The batch covering folios
  ~302–425 (B09–B13) must build its `data/pagemap/` by reading folios, and
  should check for a possibly missing leaf in the 397–425 span.

## Structure recovery

- The scan is **missing the first table-of-contents leaf** (the sections before
  伊賀ノ山). The full 19-section list was recovered from (a) the surviving second
  TOC leaf (PDF p3: 伊賀ノ山…伏見城 with exact folios) and (b) OCR of the body,
  cross-checked against the Japanese Wikipedia / Shinchōsha listing. Every
  opener's folio was verified on the page image.
- 19 titled novel sections (modelled as ch01–ch19, flat — the book has no
  numbered chapters or sub-sections), + the **解説 afterword** by Muramatsu
  Tsuyoshi (村松剛), folios 653–660, modelled as ch20.
- Novel body: folios **7–652**. First published Kōdansha, Sept 1959 (per the
  colophon line on folio 660). Naoki Prize (42nd, 1960).

## Tooling added this session (do not revert)

- `scripts/find_headings_vert.py` — vertical-text heading detector (the
  template's `find_headings.py` profiles ROWS for horizontal Chinese; this
  transposes to COLUMNS and filters furigana by glyph width). Catches
  fresh-page openers reliably; mid-page breaks needed OCR confirmation.
- `scripts/ocr_survey.py` — survey OCR runner: crop + `jpn_vert`, keeps
  paragraph blanks, and deliberately does NOT apply the Chinese
  `strip_folio`/`strip_runfoot` (see below).

## Flags for Batch 1 / the read-through

- **Batch-1 pipeline patches needed (Japanese):** `ocr_crop.py`'s `despace()`
  only strips spaces adjacent to Han (`一-鿿`), so kana keep OCR spaces; and its
  `strip_folio()` would DELETE a real short dialogue line ending in 。 (this
  book is dialogue-heavy). Use `jpn_vert --psm 5` with the crop above and adapt
  those two functions for kana before Batch 1. Furniture is top-only, so folio/
  runfoot strips are unnecessary if the crop is correct.
- **English section titles are PROVISIONAL** (drafted for the skeleton); settle
  them at the voice gate. Evocative ones to footnote: 水狗 (Water Dog), 修羅
  (Carnage), 五三ノ桐 (Paulownia Crest), 甲賀ノ摩利 (Mari of Kōga), 白い法印
  (the White Hōin).
- **解説 (ch20):** a third-party critical essay. Whether to translate it is the
  commissioner's call (raised in SURVEY.md); it is in the structure so it shows
  in the skeleton, and can be dropped if declined.
- **Title in English:** using "The Owl's Castle"; the film adaptations use
  "Owls' Castle". Confirm at the voice gate.
- **Cover:** the scan's cover is the copyrighted Shinchō woodcut; leaving
  `cover_image` empty so the builder generates a typographic cover.

## Checks run (survey)

- Skeleton EPUB built; `qa_epub.py` PASS (33 files, 26 documents, all links
  resolve); **epubcheck 5.1.0 clean** (0 fatals / 0 errors / 0 warnings).
- Checker regression tests green (setup.sh).
