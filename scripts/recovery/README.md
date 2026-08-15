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
