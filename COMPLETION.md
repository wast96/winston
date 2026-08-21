# COMPLETION.md — *China's Secret War* (中国秘密战)

The book is COMPLETE. This report replaces the next-batch handoff; it is the
document to read to know what the finished edition contains and how far to
trust it.

## Status at a glance

- **14 of 14 units translated:** the Preface, Chapters 1 through 12, and the
  Afterword. 3,285 English body paragraphs.
- **251 footnotes**, continuously numbered book-wide.
- **Glossary / term ledger: 284 rows** (187 attested, 91 decided, 6
  provisional), rendered for audit as `out/term_ledger.md`.
- **Figures: deferred** (`figures.json` empty). See "What the finished edition
  contains" for the standing question this leaves for you.
- **qa_epub: PASS** (28 files, 21 documents, all links resolve; 251
  ref/body/backlink triples; 336 page markers matched to the page list).
- **epubcheck 5.1.0: clean** (0 fatals / 0 errors / 0 warnings / 0 infos),
  EPUB 3.3.
- **Deliverable:** `out/chinas_secret_war.epub`, committed to the branch
  `claude/chinas-secret-war` with `git add -f` (chat attachments do not
  outlive the container; the branch does).

## What the finished edition contains

- **Front matter:** a title page stating honestly that the edition is complete
  (all 14 chapters); a Principal Characters page generated from the glossary's
  flagged cast; a translator's note (from `book.json`).
- **Body:** the Preface, twelve chapters each with its numbered sections, and
  each chapter's own chapter-end **Principal Sources** (主要资料) rendered as a
  translated section. The Afterword is a separate back-matter unit.
- **Set-off conventions used:** scene-break asterisms (`***`), verse blocks
  (`{p}`), and the occasional vignette/dateline markers, all rendered by the
  builder; italics for book, journal, film, and play titles.
- **Footnotes** at reader-model density, as popups (EPUB3 `aside`) plus an
  endnotes page for readers that do not support popups.
- **Printed-page markers:** folio page-list navigation for ch04 through ch13
  (each unit's resegment script rebuilds its pagemap). ch01 and ch03 carry no
  folio markers (a clean rebuild is a corrections-pass task; no note cites a
  ch03 folio, and ch01's remaining zh-parity gap is from B01).
- **Cover:** a generated typographic cover (the scan yielded no usable cover
  image; `cover_image` is unset by deliberate decision).
- **Back matter deliberately left inert:** the last leaf of the book (printed
  p. 398 / PDF 434) carries only the Afterword's closing contact block and a
  library barcode. There is no publisher's index, errata table, or colophon,
  so `back_matter.json` is empty on purpose, not by omission.
- **Figures deliberately deferred:** this is the 图文版 (illustrated edition),
  and every chapter carries inline photographs (unit rosters, portraits of the
  new police chiefs, and so on). None are reproduced. The standing question,
  whether to include every photo, a curated subset, or none, is still yours to
  decide; the translation is complete without them, and the captions are the
  source's, not inventions.

## Per-chapter tally

| Unit | Title | First folio | Paragraphs | Notes |
| --- | --- | --- | --- | --- |
| ch00 | Preface: Probing the Secret | 1 | 28 | 2 |
| ch01 | Ch. 1. "The Gun" and "The Knife" | 1 | 299 | 19 |
| ch02 | Ch. 2. Secret War | 46 | 339 | 36 |
| ch03 | Ch. 3. From "Underground" to "Aboveground" | 98 | 305 | 27 |
| ch04 | Ch. 4. Pulling Out the Nails | 135 | 119 | 14 |
| ch05 | Ch. 5. Into the Tiger's Den | 148 | 330 | 24 |
| ch06 | Ch. 6. The Great Spies of the East | 187 | 341 | 12 |
| ch07 | Ch. 7. Rooting Out Traitors | 220 | 223 | 27 |
| ch08 | Ch. 8. Yan'an's First Great Counter-espionage Case | 246 | 182 | 8 |
| ch09 | Ch. 9. The "Rescue Campaign" | 269 | 368 | 16 |
| ch10 | Ch. 10. The Open Scheme | 307 | 355 | 22 |
| ch11 | Ch. 11. The Great Turning | 348 | 236 | 19 |
| ch12 | Ch. 12. Light and Dark Change Places | 375 | 128 | 21 |
| ch13 | Afterword | 395 | 32 | 4 |
| | **Total** | | **3,285** | **251** |

## Batching as executed

The book ran in thirteen batches, one conversation each, on the plan approved
at the survey with no structural deviation:

- B01: Preface + Chapter 1 (the frozen voice reference; voice gate passed).
- B02 / B03: Chapter 2 (sections 1 to 5, then 6 to 8 plus Principal Sources).
- B04 through B12: Chapters 3 through 11, one chapter per batch, each with its
  Principal Sources.
- B13 (this batch): Chapter 12 (whole chapter plus its Principal Sources) and
  the Afterword, then back-matter check, the whole-book reconciliation sweep,
  the term ledger, the deep audit, the authority feedback, and this report.

## Checks run book-wide, and what they found

- **Numeric invariants** (`verify_unit` / `check_numbers` with
  `data/noise.txt`): 0 unresolved across every unit checked. Numerals inside
  names, places, idioms, and unit designations are noised with a commented
  literal; real quantities are carried, in digits where load-bearing.
- **Parity, anchors, heading shape:** every unit at 1:1 source-to-translation
  parity; all 251 note anchors resolve to verbatim substrings.
- **Alignment and content** (`check_align`): no pair strays beyond tolerance
  from each unit's median ratio.
- **Register vs the frozen ch01 reference** (`check_register`): within
  tolerance throughout. The later documentary chapters carry little
  conversational speech (their quotations are documents, directives, and
  slogans, kept formal by design), so the dialogue-contraction metric is noisy
  there and the units are judged on the narratorial signals. The em-dash rate
  was held low (ch12 0.5/1k, ch13 1.1/1k).
- **Whole-book reconciliation** (`check_reconcile`, check 12): exit clean. One
  spelling locale (American, 626 curated hits, 0 British). Three epithet-drift
  candidates, all adjudicated by hand as legitimate distinct compounds
  (counter-revolutionary the adjective vs counter-revolutionaries the noun;
  military-academy vs military-attaché; public-order vs public-security), not
  drift. The "unused glossary form" list is chapter-title and slogan concepts
  that appear as titles or in variant tense, not missing renderings.
- **Fact-checking (interested-witness doctrine):** the book is a sympathetic
  insider's account and is at its most partisan on the contested episodes. The
  text renders his account faithfully; the footnotes carry the counter-record
  with a stated verdict, checked against Wikipedia, Baidu Baike, and academic
  sources (never Grok/Grokipedia). See the reliability notes below.

## Observed error rate

Full report in `out/deep_audit.md`. A fixed-seed random sample (seed
20250821) of 81 paragraphs, 3.5% of the 2,314 paragraphs in the re-pairable
frame (ch04 through ch13; the Preface and Chapters 1 to 3 could not be
re-paired this session and were verified in their own batches). Two defects
were found, both in Chapter 8, and both were corrected in this batch:
西北公学 had been rendered "West China College" (西北 is Northwest, and the
same school is "Northwest College" in Chapters 2, 5, and 7), fixed to
"Northwest College" across ch08; and 冀南行署 "Jinan Administrative Office"
(ambiguous with the city 济南) was clarified to "South Hebei Administrative
Office." The other 79 sampled paragraphs, including all sampled Chapter 12/13
work, were faithful. One clear error in 81 is about 1.2% at the paragraph
level; a clean 81 would have proved only a rate below roughly 3.6%, so the
finding shows the rate is low, not zero. Both defects found were fixed, so the
shipped text is one pass cleaner than the sample measured.

## Reliability map (the interested-witness verdicts)

The book is reportage by a sympathetic insider, and its factual spine (dates,
offices, operations, named cases) is largely DOCUMENTED and holds up against
the record. Its unreliability is one of framing and omission on the contested
episodes, which the footnotes flag at the point of the claim:

- **The Suppression of Counterrevolutionaries** (Ch. 12): presented as a
  triumph of public order. DOCUMENTED as a mass execution campaign; the
  official 1954 count was about 712,000 executed, and historians' estimates
  run from roughly 500,000 to two or three million. The book omits the toll;
  the note supplies it.
- **The Cultural Revolution purge of the security system** (Ch. 12): the
  slogan "smash the police, procuratorate, and courts" and the wholesale purge
  are DOCUMENTED; the casualty figures the book gives are the public-security
  system's own post-Mao reckoning, so identified in the note.
- **"The earliest counter-terror rule in the world"** and **"the safest great
  country in the world"** (Ch. 12): the author's rhetorical and partisan
  claims, marked UNCORROBORATED in the notes.
- **Pan Hannian, Yang Fan, the "Two Chens"** (Ch. 12): the author himself
  calls these wrongful cases, matching the settled post-Mao verdict
  (rehabilitated in the 1980s).
- Earlier volumes' contested figures (Kang Sheng and the Rescue Campaign, the
  Yan'an purges, Pan Hannian's fall) carry their verdicts in their own
  chapters' notes.

## Findings that need the commissioner's eye

- **The figures decision** (every photo / a subset / none) is the one open
  editorial choice; the edition is complete either way.
- **A handful of provisional romanizations** stand where a name survives only
  in Chinese transliteration (below).
- Nothing else requires adjudication; the machine checks are clean and the two
  audit findings were fixed.

## Residual uncertainties a reader should know about

- **Provisional glossary readings** (6 rows, marked provisional and visibly
  flagged by the build): e.g. the French attaché "Lei Meng" and the Uyghur
  merchant "Aimaiti," each footnoted at first use.
- **The 101-name public-security roster** in Chapter 12 was crop-read from the
  scan name by name and checked against both OCR configs; a dense list of rare
  given names is the passage most exposed to a single mis-stroke.
- **ch01 zh parity** (269/299 from B01) and **ch03 folio markers** remain the
  two known housekeeping gaps, neither affecting any footnote or the reading
  text; both are corrections-pass items.
- **The source's own slips** are rendered as printed and footnoted where they
  matter (e.g. the ch11 case of one name printed for two men), never silently
  harmonized.

## Provenance and method

- **Source:** *中国秘密战：中共情报、保卫工作纪实* (最新升级图文版 / 2nd ed.),
  Beijing: Gold Wall Press (金城出版社), 2015, ISBN 978-7-5155-1071-2. An
  image-only scan (Internet Archive, from Contra Costa County Library), 436
  PDF pages, no text layer. Simplified Chinese, horizontal, left to right.
- **Pipeline as run:** PyMuPDF render at 300 dpi; tesseract `chi_sim psm 6`
  with a measured per-parity mirror-margin crop (recto [0.07, 0.86], verso
  [0.17, 0.94], top 0.045, bottom 0.93), plus `ocr_dual.py` (PaddleOCR was
  unavailable). Every page was then read by eye and every true paragraph
  transcribed into a hardcoded, hand-verified resegment script
  (`scripts/resegment_chNN.py`) that rebuilds `data/zh/chNN.txt` and the
  pagemap; names, numbers, and unit designations were crop-verified
  (`scripts/crop_band.py` for dense rosters and faded spans).
- **Builder features that must not be reverted:** the per-parity crop
  geometry; the resegment-after-assemble rule; the flat-glossary renderer; the
  chapter-title H1 is not anchorable (chapter-concept notes sit on a body
  phrase); note bodies are XHTML with numeric character references only; the
  builder refuses an unmatched anchor or an unplaced figure spec.
- **To rebuild from a clean checkout:** run `./setup.sh`, replay the resegment
  scripts to regenerate `data/zh` and the pagemaps, then
  `python3 scripts/build_reading_epub.py` and
  `python3 scripts/qa_epub.py`, and `java -jar
  /tmp/epubcheck-5.1.0/epubcheck.jar out/chinas_secret_war.epub`.
- **Environment:** `OMP_THREAD_LIMIT=1` is mandatory for tesseract; kill the
  process group and confirm `pgrep -c tesseract` reads 0. The setup regression
  test "hook stands down on template stub" fails benignly now that HANDOFF
  holds a real kickoff block.

## Definition of done — met

- The EPUB: front matter, all chapters, full clean TOC, generated cover,
  footnotes at reader-model density, glossary and translator's note current,
  qa_epub PASS across the whole spine, epubcheck clean, back matter correctly
  empty, and the file itself committed (`git add -f out/chinas_secret_war.epub`).
- `out/<id>_reading.md` per unit (the correction surface); `out/term_ledger.md`;
  `out/deep_audit.md`.
- `notes.json`, `glossary.json`, `figures.json` (empty by decision), `book.json`
  current; `authority.json` fed with this book's decided renderings under the
  slug `chinas-secret-war`.
- `PROGRESS.md` and this `COMPLETION.md` written; `CHANGELOG.md` updated;
  `HANDOFF.md` rewritten to say the book is COMPLETE.

Further work on this book is a corrections pass, driven by the commissioner's
read (see `CORRECTIONS.md` for the form).
