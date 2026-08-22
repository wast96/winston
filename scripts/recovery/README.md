# Batch-specific source recovery (data/zh is untracked and regenerable)

This book's blank-line assembly path drops/mangles content wherever a page
carries an author footnote or an embedded photo. `data/ocr_fixes.json` replays
the CHARACTER-level fixes, but the PARAGRAPH-STRUCTURE repairs are scripted here
so a fresh QC regen reproduces the exact paragraph counts the English is paired
against.

## B02 (ch02 PDF 60-76, ch03 PDF 77-94) regen order
1. `render.py 60 94 --dpi 300`
2. `ocr_crop.py 60 94 --left 0.11 --right 0.90 --top 0.135 --bottom 0.95 \
   --lang chi_sim --psm 6 --running-head "隐蔽战线统帅周恩来"` ; `ocr_dual.py 60 94`
3. For p83 keep only the body below the photo caption (from "的腿是在盗窃");
   blank p63 and p68 (photo+caption only). `b02_strip_furniture.py` blanks
   p63/p68 and truncates the author-footnote blocks (p62,66,71,72,73,75,91,92).
   NOTE the p73 marker is "军法会审处" (footnote-only), NOT "会审公堂" (also in body).
4. `rm -rf data/indent` ; `assemble.py ch02 60 76 --offset 44` ;
   `assemble.py ch03 77 94 --offset 44`
5. `b02_surgery.py` (heading fixes, seam merges/splits, two scan-verified
   clipped-line restorations: "生涯。" p65, "客车。" p92).
6. `apply_fixes.py ch02 ch03`
Result: ch02 = 40 body paras + 4 headings; ch03 = 37 + 5.

## B03 (ch04 PDF 95-122) regen order
1. `render.py 95 122 --dpi 300`
2. `ocr_crop.py 95 122 --left 0.11 --right 0.90 --top 0.135 --bottom 0.95 \
   --lang chi_sim --psm 6 --running-head "隐蔽战线统帅周恩来"` ; `ocr_dual.py 95 122`
3. `b03_strip_furniture.py`: normalizes the 5 garbled headings to the exact
   structure.json titles (so assemble auto-emits ###); truncates 10 author-
   footnote blocks; blanks the full-page 陈养山 photo (p113); strips the TOP
   photo (吴先清, p101, keep-from marker) and the BOTTOM photo (柯麟, p104,
   keep-through marker).
4. Add ch04 rows to data/structure.json (ch04 + ch04s01-04, pdf 95/95/103/112/118).
   `rm -rf data/indent` ; `assemble.py ch04 95 122 --offset 44`
5. `b03_surgery.py`: 4 splits (obituary block-quote p58; Ke Lin intro p60; Ke
   Lin Macau p67; Chen Shouchang end p77) + 16 backward-welds (page seams and
   two spurious in-page OCR blanks p71/p73). Result: 62 body paras + 5 headings.
6. `apply_fixes.py ch04` (167+ crop-verified char fixes; includes the dropped
   digit 12月1日->12月17日 and the note-marker/bracket garbles).
7. `data/pagemap/ch04.json` is hand-regenerated for the 62-para structure (the
   assemble auto-output was stale after surgery); 27 rows, printed 51-78,
   p113/printed-69 (the full-page photo) skipped.

## B05 (ch07 PDF 154-172, ch08 PDF 173-197) regen order
1. `render.py 154 197 --dpi 300`
2. `ocr_crop.py 154 197 --left 0.11 --right 0.90 --top 0.135 --bottom 0.95 \
   --lang chi_sim --psm 6 --running-head "隐蔽战线统帅周恩来"` ; `ocr_dual.py 154 197`
3. `b05_strip_furniture.py`: normalizes headings (per-target guard; the ch07 s04
   heading wraps two OCR lines — merge + delete the orphan tail); truncates the
   author-footnote blocks (ch07 p154/156/161/163/164/165/171/172, ch08 p187/192);
   NO photos in this range (find_figures found none; every page eyeballed).
4. Add ch07 + ch08 rows to data/structure.json (pull exact title bytes from
   book.json). `rm -rf data/indent` ; `assemble.py ch07 154 172 --offset 44` ;
   `assemble.py ch08 173 197 --offset 44` (BOTH before surgery).
5. `b05_surgery.py`: WELDS FIRST (page-seam breaks), THEN SPLITS (OCR-welded
   paragraphs — the OCR drops in-page blanks on some pages, esp. section openers),
   THEN fixups. NOT idempotent: re-assemble both units before re-running.
   ch07: s02 [14]->4, [16]->4, [18]->2, s04 block-quote blob ->12, + 4 tail fixes
   incl. the scan-restored p171 clipped line. ch08: s03 [29]->3, s05 [40]->4.
   Result: ch07 = 54 body + 6 headings; ch08 = 54 body + 7 headings.
6. `apply_fixes.py ch07 ch08` (86 crop-verified char fixes; names, dropped date
   digits, memoir shorthand 老蔡/老廖, place names 大阪/千叶).
7. `b05_pagemap.py` regenerates data/pagemap/ch07.json + ch08.json for the
   post-surgery structure (matches each page's first BODY line into the final ZH;
   monotonic; skips heading-opener lines).

## B01 (ch00 Preface PDF 36-38, ch01 PDF 45-59) + B02 robustness — added by R1 (2026-08-22)

B01 originally had no strip/surgery script and no raw-OCR backup. On a fresh
QC regen with tesseract 5.3.4 (the build used an older tesseract), the
character stream reproduces but the BLANK-LINE paragraph structure drifts.

- **ch00 (Preface).** Assemble range is PDF **36-38** only (39-44 are the
  table of contents; 45 is ch01). `scripts/recovery/b01_surgery.py` strips the
  running-head furniture and the trailing source citation and fixes two
  OCR-misplaced breaks; result 6 body paragraphs, verify_unit GREEN.
  Regen: `assemble.py ch00 36 38 --offset 44` ; `b01_surgery.py` ;
  `apply_fixes.py ch00`.
- **ch01.** zh 32 vs en 38 under tesseract 5.3.4 (six OCR-welded boundaries).
  §2 welds are mapped in b01_surgery comments; §3 is ambiguous and is NOT
  force-split (a wrong split passes parity while mis-pairing lines). PINNED as
  a known parity limitation in REVISION_PLAN.md section 2; edits verified by
  the zh-independent guard set.
- **ch03.** zh 38 vs en 37 (a p83 photo-page body displacement). Same pin.
- **B02 robustness patch.** `b02_surgery.py` now SKIPS a missing anchor with a
  warning (was a fatal SystemExit on the first miss, which aborted all of
  ch02's merges). Under tesseract 5.3.4 two anchors drift (`延请`,
  `革命委员会委员`); with skip-and-warn, ch02 lands 40/40 GREEN, ch03 lands
  38 (one short, the p83 case above). DO NOT REVERT the skip-and-warn.
