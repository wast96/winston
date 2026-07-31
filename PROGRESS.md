# PROGRESS — The Autobiography of Huang Mulan

The running per-batch log. Write it as you go, not at the end. One section per
batch: what was translated (unit ids, chapter/section scope), which checks ran
and what they found, notes added (count and numbering), glossary rows added with
status, figures, and anything flagged for the read-through (uncertain readings,
contradictions with scholarship, choices you were unsure of).

## Setup

- Source EPUB: 《黄慕兰自传》(The Autobiography of Huang Mulan), Encyclopedia of
  China Publishing House, 2016 reissue (first ed. 2004), ISBN 9787500097044,
  ASIN B079HPXJQ4. Calibre-produced digital EPUB, reliable Unicode text, no OCR.
  The source carries no footnotes/endnotes of its own.
- Ingest: 53 spine documents, 105 images, 254,900 source characters
  (out/INGEST.md). Colour cover.jpeg present (720x1095).
- Structure: source file boundaries mostly match logical chapters (one spine doc
  per chapter). Logical structure authored in book.json as 44 ch-units: front
  matter (ch00, Note on the Reissue), 38 numbered chapters in five parts
  (ch01-ch38), and five appendices (ch39-ch43). Chapters are flat (no internal
  sections). Handling: five part-divider 临江仙 poems folded into each part's
  first chapter (part_poem_src); source TOC + running header dropped in favour of
  the generated hyperlinked TOC; copyright leaf carried as metadata; the source's
  duplicate 附录四 label (ch42 and ch43) preserved, not renumbered.
- Metadata: wired into build_reading_epub.py for Kindle/Apple Books — Dublin Core
  (title + subtitle, sortable author with file-as + MARC role, language en with
  the Chinese original as dc:source, publisher, year, ISBN, description, BISAC
  subjects, rights) and the colour cover (cover-image + legacy cover hint + cover
  page in the spine).
- Survey: out/SURVEY.md written; skeleton EPUB built (0 of 44 translated),
  qa_epub PASS (56 files, 50 documents, all links resolve).
- Commissioned scope (approved): translate ONLY ch00, ch01-ch21, and ch39-ch43;
  chapters 22-38 stay as pending skeleton pages. Batch target 21,000 source chars
  max → 9 batches (146,824 chars in scope). Plan in book.json "batches".

## B01 = ch00-ch03  (pending — not started)

- (fill in per the batch)
