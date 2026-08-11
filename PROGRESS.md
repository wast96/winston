# PROGRESS — The Rebel (叛逆者) / Bi Yu

The running per-batch log. Write it as you go, not at the end. One section per
batch: what was translated (unit ids, chapter/section scope), which checks ran
and what they found, notes added (count and numbering), glossary rows added with
status, figures, and anything flagged for the read-through (uncertain readings,
contradictions with scholarship, choices you were unsure of).

## Setup

- Source EPUB: 叛逆者 (Bi Yu / 畀愚), People's Literature Publishing House
  (人民文学出版社), first published June 2020. A collection of FOUR novellas:
  叛逆者 (The Rebel), 邮差 (The Postman), 氰化钾 (Potassium Cyanide), 胭脂 (Rouge).
  Republican-era / wartime Shanghai espionage fiction. Clean digital text
  (no OCR). One image only: the cover. No source footnotes (grepped `\[\d+\]`
  across all units: none present).
- Ingest: 54 spine documents, 1 image, 118,277 source characters (out/INGEST.md).
- Structure: the source numbers the stories as 51 continuous chapters
  (第1章..第51章), the numbered installments of the four novellas. Modeled here
  as 51 translation units (ch01..ch51) grouped into four `part`s. Three spine
  docs are NOT chapters and are excluded (recorded in book.json `_source_note`):
  cover_page.xhtml (cover), part0000.xhtml (版权信息 imprint), part0001.xhtml
  (目录 source TOC). The 后记 (part0031) is chapter 30 in the source and reads as
  the coda/afterword of 邮差; modeled as ch30 under the The Postman part,
  title_en "Afterword".
- Skeleton: built, qa_epub PASS (51 docs), epubcheck 5.1.0 clean (0/0/0/0).
  Cover embedded byte-identical.

## B01 = <scope>

- (fill in per the batch)
