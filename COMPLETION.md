# COMPLETION.md — Owl's Castle (梟の城, Shiba Ryōtarō)

The book is COMPLETE. All twenty sections — the nineteen novel chapters and the
critical afterword — are translated, annotated, and built into the deliverable
EPUB. Further work is a corrections pass, not new translation. This document
replaces a handoff.

## Status at a glance

- 20 of 20 sections translated. The title page now states the book is complete.
- Notes: 149, at reader-model density. ch20, a reference-dense critical essay,
  carries 19 (see the note on density below); the novel chapters taper as their
  furniture gets covered.
- Figures: 0. The book is text-only throughout; every chapter's empty figure
  list is a deliberate, recorded decision, confirmed by find_figures plus an
  eyeball of every page.
- Glossary: 113 people, 113 places, 30 terms. ch20 added no rows (every name it
  reuses from the novel was already decided; its external writers and works are
  footnoted, not glossaried, since each appears once).
- qa_epub: PASS (34 files, 27 documents, all links resolve).
- epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings / 0 infos.
- Deliverable: out/owls-castle.epub, committed with git add -f on branch
  claude/owls-castle.

## What the finished edition contains

Front matter (title page stating honestly that the book is complete;
translator's note; a Principal Characters page for the marked cast), all
nineteen novel chapters and the afterword, with a full hyperlinked TOC,
footnotes as popups plus an endnotes page, a glossary, and printed-folio page
markers with a page-list nav (422 markers). A generated typographic cover (the
scan yields no usable cover image). Set-off conventions used across the book:
scene-break asterisms, italic vignette and dateline blocks, verse blocks, and a
source hour-gloss form. Back matter is deliberately inert: book.json back_matter
is [], because the book carries no errata, colophon, or index that belongs in
the apparatus. The 解説 afterword is NOT back matter; it is ch20, a full
section.

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
| ch20 | Afterword (Muramatsu Takeshi) | 653–660 | 26 | 19 | 0 |

Total translated body paragraphs: 5,637. One permanent scan gap (printed
folios 404–405) is handled honestly in ch12 with no invented bridging text.

## The afterword (ch20), and one fact-check correction

ch20 is the 解説 (kaisetsu), a signed critical essay commissioned for the
Shinchō Bunko edition, written March 1965. It is a third party's appreciative
literary criticism, not Shiba's period narrative, and is rendered in that
register: measured, essayistic, first-person modern English criticism.

- **Author's name corrected.** The survey and earlier documents called the
  critic "Muramatsu Tsuyoshi." The scholar 村松剛 (1929–1994) reads **Muramatsu
  Takeshi** (むらまつ たけし); this is confirmed by Japanese reference sources.
  book.json's ch20 title_en, the glossary-free footnote, and the built EPUB now
  all read Takeshi; SURVEY.md was corrected likewise.
- **Note density is deliberately high.** The essay is a map of the postwar
  Japanese literary field: it names roughly twenty writers, works, prizes, and
  historical figures a Western reader cannot be expected to know (Tachikawa
  Bunko and Sarutobi Sasuke; Murayama Tomoyoshi, Yamada Fūtarō, Ishihara
  Shintarō, Yoshikawa Eiji, Kōda Rohan, Sakaguchi Ango; Ōmura Masujirō, Kawai
  Tsuginosuke, Saitō Dōsan, Hijikata Toshizō; the Naoki Prize, the Shinsengumi,
  the Sankei Shimbun, and several of Shiba's own novels). Each earns one
  substantive footnote at first mention. This is a reader model, not a quota:
  without the notes the essay reads as a wall of unknown names.
- **NOT re-noted (already placed in the novel):** Tsuzura Jūzō, Kazama Gohei,
  Shimotsuge Jirōzaemon, Kohagi, Kisaru, Toyotomi Hideyoshi, the Tokugawa house,
  Kōga/Iga — all glossaried or footnoted earlier. Miyamoto Musashi the swordsman
  is footnoted at ch06; ch20's note is on Yoshikawa's *novel* and cross-refers.
- **Source discrepancy left visible (footnoted):** Muramatsu dates Shiba's
  prize-winning *The Persian Sorcerer* to 1955; the story in fact appeared in
  1956. Rendered as printed, with the correction in the note.
- **Register.** check_register reports ch20 within tolerance of the ch01
  reference, with 0 contractions — flagged "little dialogue — noisy." That is
  the correct nonfiction register for a critical essay, formal by design, not a
  defect.

## Batching as executed

One section per batch, B01 through B20, each a fresh conversation started from
the previous batch's pasted kickoff, following the survey-approved plan. B12
absorbed the 404–405 scan gap. B19 carried the novel's climax plus the
whole-book completion protocol; B20 added the afterword and closed the book.

## Checks run book-wide, and what they found

- Numeric invariants (check_numbers, per chapter): 0 unresolved book-wide.
  Name-and-idiom numerals live in data/noise.txt with a comment each; B20 added
  the Shōwa era-year dates (rendered as Gregorian years) and the name numerals
  in 道三/歳三.
- Parity, anchors, heading shape (check_structure / verify_unit): clean; each
  unit's source line count equals its translation paragraph count.
- Entity survival (qc_entities) and displacement (check_content, the
  authoritative one): 0 misses, every glossary name present in the paragraph it
  belongs to.
- Register vs the frozen ch01 reference (check_register): every unit within
  tolerance (see the ch20 note above; ch19 ran 0.61x, in the formal band with
  ch15 and ch18).
- Whole-book reconciliation (check_reconcile), re-run at completion: 0 British /
  133 American spelling locale. Remaining reconcile candidates are date
  compounds matching different actual days, the abbreviated vs. full court title
  for Ishida Mitsunari, and the one unused glossary form below — all adjudicated
  for a human read, none introduced by ch20.

## Observed error rate

Random-sample deep audit on ch19, 14 of 310 paragraphs (4.5%), fixed seed 19:
zero fidelity errors (full report in out/deep_audit.md). ch20 was additionally
given full paranoid treatment as the closing unit: every proper name
crop-verified against the page images at high DPI, the tail (final paragraphs
and the colophon on folio 660) read against the scan, and the era-date and
name numerals reconciled. No fabrication; the OCR was used only as a
cross-check against a hand transcription made from the images.

## Findings that need the commissioner's eye

- The court title 治部少輔 for Ishida Mitsunari appears both as "Jibu-no-shō" (7)
  and "Jibu-no-shōyū" (5) across the earlier chapters. Both name the same
  office; harmonizing to one form is a one-line corrections-pass grep if wanted.
- One unused glossary form, "Imai Sōkun" (今井宗薫, Sōkyū's son), is decided but
  never surfaces in the prose; harmless, and a candidate for pruning.

## Residual uncertainties a reader should know about

- The permanent scan gap at printed folios 404–405 (ch12): a leaf missing from
  the scanned copy, left as an honest gap with a footnote, no invented text.
- Provisional romanizations and damaged-scan readings are each footnoted at the
  point they occur; there is no silent guess anywhere in the apparatus.
- ch19: the quoted diary form 「又一人者八釜にて煎らる」 is rendered "boiled in a
  cauldron"; the printed 八 most likely stands for は in the original 又一人ハ釜ニテ,
  noted in data/noise.txt. Imai Sōkyū's fictional survival past his real 1593
  death is footnoted honestly rather than corrected.
- ch20: the 1955-vs-1956 date for *The Persian Sorcerer* prize (above), and the
  essay's grouping of Kawai Tsuginosuke under *The Man of Demonic Cunning* (Shiba
  later gave Kawai his own novel, *Tōge*) — both left as printed and footnoted.

## Provenance and method

- Source: image-only PDF scan from the Internet Archive (fukuronoshiro0000ryot),
  the Shinchō Bunko edition; vertical, right-to-left, furigana throughout, all
  page furniture at the top of the page. No usable text layer.
- OCR: PyMuPDF render at 300 dpi; tesseract jpn_vert psm 5 with the measured
  crop (L0.035 R0.965 T0.075 B0.955, --no-furniture-strip), plus ocr_dual.py as
  the second read. Every unit, ch20 included, was hand-transcribed from the page
  images into data/zh/chNN.txt (the parity surface); assemble.py was NOT used to
  weld this vertical text.
- Builder features that must not be reverted: the sectioned glossary (add rows
  directly, not via apparatus_merge); the note-anchor and figure-spec refusal
  gates; the pending-aware TOC (now fully resolved); the pagebreak/page-list
  emission from data/pagemap/. Offset held at 0 (printed == PDF) unbroken from
  folio 406 to the end, confirmed by folio reads through the afterword (653–660).
- Rebuild from a clean checkout: run ./setup.sh, then
  `apt-get install -y tesseract-ocr-jpn tesseract-ocr-jpn-vert`; then
  `python3 scripts/build_reading_epub.py`, `python3 scripts/qa_epub.py`, and
  `java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/owls-castle.epub`.

## Definition of done — met

- EPUB: front matter + all 19 chapters + the afterword, full clean TOC (no
  pending markers), generated cover, no figures (recorded decision), footnotes
  at reader density, glossary and translator's note current, qa_epub PASS across
  the whole spine, epubcheck clean. The file itself is committed
  (git add -f out/owls-castle.epub).
- out/chNN_reading.md per unit (the correction surface), out/term_ledger.md,
  out/deep_audit.md all present.
- notes.json, glossary.json, figures.json (empty), book.json current;
  authority.json fed with this book's decided renderings under slug owls-castle.
- COMPLETION.md written (this file); PROGRESS.md and HANDOFF.md updated;
  CHANGELOG.md has the completion entry.
- Nothing is left undone. The book is COMPLETE; the next step is a corrections
  pass if the commissioner's read turns any up.
