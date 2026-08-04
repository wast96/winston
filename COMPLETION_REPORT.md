# COMPLETION REPORT — Midnight (子夜), Mao Dun

Annotated English translation, digital-EPUB source. This report closes the book:
Batch B18 finished the final three units, and the whole spine is now translated,
annotated, built, and validated.

## What the book is

An annotated English edition of Mao Dun's 1933 novel 子夜 (*Midnight*), the
panoramic realist portrait of Shanghai in 1930: the industrialist Wu Sunfu, the
bond-market speculators, the silk filatures and their strikes, and a Chinese
bourgeoisie caught between foreign capital and revolution. Translated in full
from the digital source EPUB (no OCR); the source text is authoritative and was
rendered faithfully and in full, with an apparatus of translator's footnotes, a
glossary, the author's own preserved endnotes, and a translator's note.

## Units

- **20 units**, all translated: Chapters One through Nineteen (ch01–ch19) plus
  the Afterword (后记, ch20).
- **Source size: 243,113 characters** across the 20 units.
- Delivered EPUB: `out/Midnight.epub`. Per-unit reading text: `out/<id>_reading.md`
  (the correction surface). Cumulative build driven entirely by `book.json`.

## Batching (as executed)

One approved plan, 21,000-source-char maximum per batch. B01–B17 were one chapter
each (ch01–ch17); **B18 = ch18 + ch19 + Afterword** (17,836 chars), the final batch.

## Notes

- **Translator footnotes: 109**, builder-numbered 1–109 continuous in reading order,
  every reference with a body and a backlink (qa-verified). Density ~3–6 per
  chapter-equivalent; recurring subjects noted at first appearance.
- **Author (source) notes: 9** — the original's own endnotes [1]..[9], placed at
  their in-text markers and kept visibly distinct from the translator's notes:
  ch01 [1][2], ch02 [3], ch05 [4], ch06 [5][6][7], ch11 [8][9]. `source_notes.json`
  is complete and frozen.
- B18 added translator notes 101–109 (the Xuande censer & Tibetan incense; the
  walled-in monk; Jia Yi's *Rhapsody on the Owl*; the *Lingfei jing* hand; the
  Domestic Bond Maintenance Association; the "hollow dumpling" idiom; the Red Army
  at Ji'an/Changsha, summer 1930; the Qingdao/Beidaihe/Kuling resorts; the "new
  *Scholars of the Grove*").

## Glossary

- **384 entries** total: 118 people, 50 organizations, 115 places, 101 terms — one
  rendering per referent, each with a status (`attested` / `provisional` / `decided`)
  and its attestation. This is the term ledger that enforced cross-chapter
  consistency for the industrialist, comprador, bond-market and strike cast across
  the whole book.

## Check results (whole book)

- **Faithful, complete quotation.** Every bilingual QC file quotes the source
  verbatim; for the final batch this was verified mechanically — 0 mismatches across
  all 286 B18 paragraphs. Paragraph parity is the structural backstop throughout.
- **`check_numbers.py`** (with `data/noise_zh.txt`): every unit reports **0
  unresolved**. The noise file documents, chapter by chapter, each non-quantity
  numeral (idioms, names/places with digits, fractions, uncomputable compound
  myriads, positional-year and clock residues) — with the reason recorded on each line.
- **`check_structure.py --pairs`**: paragraph parity **OK** on every unit
  (one English paragraph per source paragraph; note anchors resolve; heading shape
  uniform).
- **`qa_epub.py out/Midnight.epub`**: **PASS** — 32 files, 26 documents, 4,190
  paragraphs, 109 note references / 109 bodies / 109 backlinks, all links resolve,
  numbering sequential in reading order.
- **epubcheck 5.1.0** (EPUB 3.3 rules): **0 fatals / 0 errors / 0 warnings.**
- The full, hyperlinked table of contents links all 20 translated units; the
  translator's note and the author's afterword both render; the book validates for
  Apple Books.

## Observed error rate (random-sample deep audit)

A ~5% sample of the final batch (14 paragraphs spread across ch18, ch19 and the
afterword) was given the full paranoid treatment — verbatim-quote confirmation,
omission check, and close fidelity read against the source. **0 substantive errors
observed** (no omissions, no invented material, no mistranslation); only ordinary
stylistic latitude in phrasing. Consistent with the per-batch audits recorded in
`PROGRESS.md` across ch01–ch17.

## Back matter

The source's own imprint/copyright page (版权信息) and table of contents (目录) are
source apparatus, not translatable units, and are excluded by design (`book.json`).
`back_matter.json` ships inert (a colophon placeholder only), so no colophon is
rendered — nothing was invented to fill it. The **Translator's Note** (from
`book.json`'s `translator_note`) renders as a front/back-matter page, and the
author's **Afterword** (后记) is translated as the final chapter (ch20).

## Definition of done — met

Front matter + all 20 chapters, full hyperlinked TOC, footnotes throughout at
reference density, glossary and translator's note current, author's afterword and
endnotes preserved, `qa_epub` PASS and epubcheck clean across the whole spine.
`out/<id>_reading.md`, `notes.json`, `glossary.json`, `figures.json`, `book.json`,
`source_notes.json`, `PROGRESS.md` all current. The book has no figures (the sole
source image is the cover) and no colophon; both are accounted for above.

**Deliverable: `out/Midnight.epub`** — presented in chat.
