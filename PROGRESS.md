# PROGRESS — The Whistling Wind (风萧萧) by Xu Xu (徐訏)

The running per-batch log. Write it as you go, not at the end. One section per
batch: what was translated (unit ids, chapter/section scope), which checks ran
and what they found, notes added (count and numbering), glossary rows added with
status, figures, and anything flagged for the read-through (uncertain readings,
contradictions with scholarship, choices you were unsure of).

## Setup / Step 0 (ingest + survey) — DONE, awaiting batch approval

- Source EPUB: `source.epub` = 风萧萧, simplified-character digital text
  (publisher metadata credits epub掌上书苑 / cnepub, dated 2020-09-17). No OCR.
  Color cover art present (568x800 JPEG).
- Ingest (`scripts/ingest_epub.py`): 63 spine documents, 2 images, 235,864
  source characters. Text to `data/src/`, cover to `data/figs/cover.jpg`,
  report `out/INGEST.md`, draft `book.draft.json`.
- Structure: the source's file boundaries do NOT match the logical book, so
  `book.json` was authored by hand from the draft:
  - ch00 = About the Author (作者简介, source `chapter2.html`) — front matter.
  - ch01..ch58 = the novel's 58 numerically-headed chapters (源 一..五十八 =
    source `chapter3.html`..`chapter60.html`). Verified: my ch01..ch58 map
    one-to-one onto the source headings 一..五十八.
  - ch59 = Impressions of Xu Xu (徐訏印象, source `chapter62.html`) — appendix.
  - THREE source documents are deliberately NOT modelled as body chapters and
    are recorded in `book.json` `_source_note` so they are not silently
    dropped: `coverpage.html` (cover image + an uploader-supplied scholarly
    abstract, reused as cover art + basis for the English catalogue
    description); `chapter61.html` (a 45-char edition/imprint note — to become
    the translated Colophon back-matter on the final batch); `chapter1.html`
    (the source's own 目录/TOC, superseded by the build's hyperlinked TOC).
- Metadata: pulled from the source OPF and fact-checked against Wikipedia /
  Baidu Baike scholarship (author dates, original serialization, character
  roles). `book.json` now carries store metadata (title/author file-as sort
  keys, MARC `aut` role, language, 1943 date, subjects, English description,
  cover). `scripts/build_reading_epub.py` was extended to emit rich Dublin Core
  OPF metadata + a color cover (EPUB3 `cover-image` property, legacy
  `<meta name="cover">`, guide + landmark), formatted for Kindle and Apple Books.
- Survey (`scripts/survey.py --target 21000`): counts + full outline +
  proposed 13-batch plan (every batch <= 21,000 source chars, the commissioner's
  cap) in `out/SURVEY.md`.
- Skeleton EPUB built to `out/The Whistling Wind.epub`; `scripts/qa_epub.py`
  PASS (72 files, 66 documents, all links resolve). Fully navigable
  hyperlinked TOC, 0 of 60 chapters translated.

Checks run this step: JSON validity of book.json; numeral-mapping assertion
(ch01..ch58 == source 一..五十八); qa_epub PASS; OPF well-formedness + cover
wiring verified. No translation performed (Step 0 only).

## B01 = <scope — set after approval>

- (fill in per the batch)
