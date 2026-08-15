# COMPLETION.md — Owl's Castle (梟の城, Shiba Ryōtarō)

The novel proper is COMPLETE. Nineteen of the book's twenty sections are
translated, annotated, and built into the deliverable EPUB. The twentieth
section, ch20 解説, is a third-party critical afterword by Muramatsu Tsuyoshi;
whether to translate it is the commissioner's separate call (see the flag at
the end of this file). This document is written instead of another handoff.

## Status at a glance

- 19 of 20 sections translated (the untranslated one is the afterword, ch20).
- Notes: 130, at reader-model density, tapering naturally to the late chapters.
- Figures: 0. The book is text-only throughout; every chapter's empty figure
  list is a deliberate, recorded decision, confirmed by find_figures plus an
  eyeball of every page.
- Glossary: 113 people, 113 places, 30 terms.
- qa_epub: PASS (34 files, 27 documents, all links resolve).
- epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings / 0 infos.
- Deliverable: out/owls-castle.epub, committed with git add -f on branch
  claude/owls-castle.

## What the finished edition contains

Front matter (title page stating honestly that 19 of 20 sections are
translated; translator's note; a Principal Characters page for the marked
cast), all nineteen novel chapters with a full hyperlinked TOC, footnotes as
popups plus an endnotes page, a glossary, and printed-folio page markers with a
page-list nav (422 markers). A generated typographic cover (the scan yields no
usable cover image). Set-off conventions used across the book: scene-break
asterisms, italic vignette and dateline blocks, verse blocks, and a source
hour-gloss form. Back matter is deliberately inert: book.json back_matter is [],
because the book carries no errata, colophon, or index that belongs in the
apparatus. The 解説 afterword is NOT back matter; it is ch20, a full section.

## Per-chapter tally

| Unit | Title | Folios | Paragraphs | Notes | Figures |
|---|---|---|---|---|---|
| ch01 | Otogi Pass | 7–63 | 523 | 17 | 0 |
| ch02 | The Rain-Soaked Buddha | 64–89 | 276 | 6 | 0 |
| ch03 | The White Hōin | 90–123 | 385 | 16 | 0 |
| ch04 | Kisaru and Gohei | 124–148 | 286 | 5 | 0 |
| ch05 | Rakshasa Valley | 149–166 | 152 | 6 | 0 |
| ch06 | The Ninja Cipher | 167–206 | 312 | 5 | 0 |
| ch07 | Juraku | 207–236 | 280 | 5 | 0 |
| ch08 | The Thief of the Capital | 237–302 | 580 | 6 | 0 |
| ch09 | Mari of Kōga | 302–338 | 324 | 11 | 0 |
| ch10 | A Strange Accident | 338–373 | 312 | 4 | 0 |
| ch11 | The Hills of Iga | 373–397 | 230 | 6 | 0 |
| ch12 | The Celestial Maiden of Yoshino | 397–425 | 212 | 10 | 0 |
| ch13 | The Water Dog | 425–456 | 245 | 6 | 0 |
| ch14 | Carnage | 456–508 | 446 | 6 | 0 |
| ch15 | The Paulownia Crest | 508–566 | 440 | 5 | 0 |
| ch16 | Mount Kannabi | 566–583 | 132 | 4 | 0 |
| ch17 | The Shadowing | 584–591 | 44 | 6 | 0 |
| ch18 | The Ishida Mansion | 591–608 | 122 | 3 | 0 |
| ch19 | Fushimi Castle | 608–652 | 310 | 3 | 0 |
| — | (ch20 解説 / Afterword, folios 653–660: NOT translated) | | | | |

Total translated body paragraphs: 5,611. One permanent scan gap (printed
folios 404–405) is handled honestly in ch12 with no invented bridging text.

## Batching as executed

One section per batch, B01 through B19, each a fresh conversation started from
the previous batch's pasted kickoff, following the survey-approved plan. B12
absorbed the 404–405 scan gap. The final batch, B19, carried the climax chapter
plus the whole-book completion protocol below.

## Checks run book-wide, and what they found

- Numeric invariants (check_numbers, per chapter): 0 unresolved book-wide.
  Name-and-idiom numerals live in data/noise.txt with a comment each.
- Parity, anchors, heading shape (check_structure / verify_unit): clean; each
  unit's source line count equals its translation paragraph count.
- Entity survival (qc_entities) and displacement (check_content, the
  authoritative one): 0 misses, every glossary name present in the paragraph
  it belongs to.
- Register vs the frozen ch01 reference (check_register): every unit within
  tolerance. ch19 ran 0.61x, in the same formal band as ch15 (0.60x) and ch18
  (0.68x), because roughly a quarter of the chapter is documentary and
  essayistic (the historical Goemon digression and two quoted diary records)
  and the central confrontation is grave by design; the casual dialogue (the
  horse-drivers, Gohei's exchanges) is contracted.
- Whole-book reconciliation (check_reconcile): the one real finding was a mixed
  spelling locale. ch01, the commissioner-approved reference, is American; the
  38 drifted British forms (80 occurrences once inflections and other markers
  are counted) were cascaded to American across all reading files, notes.json,
  and glossary.json. The ledger now reads 0 British / 130 American. Remaining
  reconcile candidates were adjudicated as false positives (date-compounds like
  文禄三 and 三条河 matching different actual days) or as pre-existing minor items
  left for a corrections pass (see below).

## Observed error rate

Random-sample deep audit on ch19 (the newest chapter), 14 of 310 paragraphs
(4.5%), fixed seed 19: zero fidelity errors. Honest bound: zero in 14 proves a
rate below roughly 20% at 95% confidence, not zero; the true rate is far lower
given the per-paragraph crop-verification and the compound-coverage grep. Full
report in out/deep_audit.md.

## Findings that need the commissioner's eye

- ch20 解説 (Afterword by Muramatsu Tsuyoshi), folios 653–660: translate it, or
  ship the novel as-is? This is a third-party critical essay, not Shiba's text.
  If wanted, it becomes B20.
- The court title 治部少輔 for Ishida Mitsunari appears both as "Jibu-no-shō" (7)
  and "Jibu-no-shōyū" (5) across the earlier chapters. Both name the same
  office; harmonizing to one form is a one-line corrections-pass grep if the
  commissioner prefers it.
- One unused glossary form, "Imai Sōkun" (今井宗薫, Sōkyū's son), is decided but
  never surfaces in the prose; harmless, and a candidate for pruning.

## Residual uncertainties a reader should know about

- The permanent scan gap at printed folios 404–405 (ch12): a leaf missing from
  the scanned copy, left as an honest gap with a footnote, no invented text.
- Provisional romanizations and damaged-scan readings are each footnoted at the
  point they occur; there is no silent guess anywhere in the apparatus.
- ch19 specifically: the quoted diary form 「又一人者八釜にて煎らる」 is rendered
  "boiled in a cauldron"; the printed 八 most likely stands for は in the
  original 又一人ハ釜ニテ, and is noted as such in data/noise.txt. Imai Sōkyū's
  survival and later Tokugawa dealings are the author's fictional liberty (the
  real Sōkyū died in 1593); this is footnoted honestly rather than corrected.

## Provenance and method

- Source: image-only PDF scan from the Internet Archive (fukuronoshiro0000ryot),
  the Shinchō Bunko edition; vertical, right-to-left, furigana throughout, all
  page furniture at the top of the page. No usable text layer.
- OCR: PyMuPDF render at 300 dpi; tesseract jpn_vert psm 5 with the measured
  crop (L0.035 R0.965 T0.075 B0.955, --no-furniture-strip), plus ocr_dual.py as
  the second read. Every unit was hand-transcribed from the page images into
  data/zh/chNN.txt (the parity surface); assemble.py was NOT used to weld this
  vertical text.
- Builder features that must not be reverted: the sectioned glossary (add rows
  directly, not via apparatus_merge); the note-anchor and figure-spec refusal
  gates; the pending-aware TOC; the pagebreak/page-list emission from
  data/pagemap/. Offset held at 0 (printed == PDF) unbroken from folio 406 to
  the end; confirmed for ch19 by reading the running-head folio of every page
  across PDF 608–652.
- Rebuild from a clean checkout: run ./setup.sh, then
  `apt-get install -y tesseract-ocr-jpn tesseract-ocr-jpn-vert`; then
  `python3 scripts/build_reading_epub.py`, `python3 scripts/qa_epub.py`, and
  `java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/owls-castle.epub`.

## Definition of done — met

- EPUB: front matter + all 19 chapters, full clean TOC, generated cover, no
  figures (recorded decision), footnotes at reader density, glossary and
  translator's note current, qa_epub PASS across the whole spine, epubcheck
  clean. The file itself is committed (git add -f out/owls-castle.epub).
- out/chNN_reading.md per unit (the correction surface), out/term_ledger.md,
  out/deep_audit.md all present.
- notes.json, glossary.json, figures.json (empty), book.json current;
  authority.json fed with this book's 256 decided renderings under slug
  owls-castle.
- COMPLETION.md written (this file); PROGRESS.md and HANDOFF.md updated;
  CHANGELOG.md has the completion entry.
- One item is by design NOT done: ch20 解説, the afterword, pending the
  commissioner's translate-or-not decision.
