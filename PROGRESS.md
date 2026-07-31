# PROGRESS — On a Hair Trigger (一触即发) by Zhang Yong

The running per-batch log. Write it as you go, not at the end. One section per
batch: what was translated (unit ids, chapter scope), which checks ran and what
they found, notes added (count and numbering), glossary rows added with status,
figures, and anything flagged for the read-through (uncertain readings,
contradictions with scholarship, choices you were unsure of).

## Setup

- Source EPUB: 一触即发 by Zhang Yong (张勇). Digital EPUB (Calibre-repackaged
  EasyPub text, internal timestamp 2015), reliable Unicode, no OCR. One embedded
  image (the cover). The source carries no notes of its own.
- Ingest (out/INGEST.md): 38 spine documents, 1 image, 232,092 source characters
  in total; of these the translatable content is 231,699 chars across the
  prologue and 35 chapters (the 目录 and cover pages are the remainder).
- Structure: the source's file boundaries DO match logical chapters (one spine
  file per chapter), so no merge/split was needed; the source's cover page and
  目录 were dropped from book.json because the builder regenerates a title page
  and a full hyperlinked contents. Flat book: Prologue (ch00) + ch01 to ch35,
  no sections or subsections.
- Batch plan: approved at a 21,000-char maximum, 13 batches (book.json
  "batches").
- Skeleton EPUB built to out/On a Hair Trigger.epub; scripts/qa_epub.py PASS
  (48 files, 42 documents, all links resolve). Kindle/Apple Books metadata and
  cover embedded.

## B01 = Prologue + Chapters 1 to 4 (ch00 to ch04)

- Not started.
