# COMPLETION.md — *Scales and Claws of Shanghai* (上海鱗爪, customs volume)

Whole-book completion report, written on the final batch (B10) instead of
another handoff. This is the document to read to know what the finished
edition is and how far to trust it.

## Status at a glance

- **168 of 168 units translated** — the preface (序) and all 167 essays.
- **643 footnotes**, continuously numbered book-wide, ref/body/backlink all
  balanced.
- **35 figures** (reprint photographs and one line diagram) with alt text and
  provenance captions; concentrated in the front matter and the illustrated
  early essays. **B10 added no figures** — pages 234–247 carry no reprint
  photographs (verified page by page; recorded as a deliberate empty list).
- **339 glossary rows** — people 68, places 66, organizations 45, terms 160;
  sectioned, with status attested / provisional / decided.
- **qa_epub: PASS** — 217 files, 175 documents, 643 references / 643 bodies /
  643 backlinks, all links resolve.
- **epubcheck 5.1.0: clean** — 0 fatals / 0 errors / 0 warnings / 0 infos
  (EPUB 3.3 rules).
- **Deliverable:** `out/scales-and-claws-of-shanghai.epub`, committed to the
  branch `claude/scales-and-claws` (`git add -f`, since `out/` is otherwise
  ignored).

## What the finished edition contains

- **Front matter:** cover (typographic + reprint plates), title page stating
  honestly that the edition is **complete** (all 168 chapters), a Principal
  Characters page, and a translator's note.
- **Body:** all 167 essays plus the preface, as clean reading prose. All
  apparatus lives in the notes — no inline bilingual text, no page numbers in
  the prose, no `[?]` flags.
- **Set-off conventions used:** scene asterisms, italic vignette/dateline
  blocks, verse blocks, and the italic sub-topic headings within the long
  New-Year essay (ch001).
- **Notes:** reader-model density (a Westerner with no Chinese background),
  tapering naturally toward the late essays as the book's furniture gets
  covered; popup-enabled (`epub:type="footnote"`) with a fallback endnotes
  page.
- **Glossary** and **term ledger** (`out/term_ledger.md`) current.
- **Back matter: deliberately none.** The book has **no errata table**. Its
  final leaves are the 2019 reprint's modern imprint page (PDF 249:
  publisher 新銳文創/秀威資訊, chief editor 蔡登山, BOD first edition Feb 2019,
  ISBN 978-957-8924-38-3, series 血歷史 140) and the National Library CIP
  record (PDF 250) — bibliographic production data, not a historical colophon.
  That provenance is already carried in `book.json` metadata (publisher, year,
  `source_ref`) and the OPF. The builder's colophon template is written for
  "the book's **original** copyright leaf"; rendering the reprint's imprint
  through it would mislabel it, so `back_matter.json` is left inert — the
  faithful choice, and consistent with B01–B09.

## Per-chapter tally (final batch, B10)

| Unit | Title | Folio | Paras | Notes | Figures |
|---|---|---|---|---|---|
| ch156 | Lighting Incense and Candles | 232 | 1 | 1 | 0 |
| ch157 | Ronin of a Certain Country | 233 | 2 | 4 | 0 |
| ch158 | Crying the Fire Watch | 234 | 1 | 1 | 0 |
| ch159 | Flowers on the Tree | 235 | 2 | 1 | 0 |
| ch160 | The Frisk | 236 | 2 | 1 | 0 |
| ch161 | Rubber Checks | 237–239 | 4 | 3 | 0 |
| ch162 | Counterfeit Banknotes | 240 | 4 | 2 | 0 |
| ch163 | Counterfeit Silver Dollars | 241 | 1 | 1 | 0 |
| ch164 | Counterfeit Small Coin | 242 | 2 | 2 | 0 |
| ch165 | Fake Calligraphy and Paintings | 243 | 3 | 2 | 0 |
| ch166 | False Politeness | 244 | 2 | 1 | 0 |
| ch167 | The All-Girl Troupes | 245 | 2 | 3 | 0 |

B10 totals: 12 units, 26 paragraphs, 22 notes, 20 glossary rows, 0 figures.

## Batching as executed

- Survey (2026-08-10): structure, metadata, batch plan, skeleton — approved.
- B01 (08-11) ch000–ch001; voice gate passed, ch001 frozen as reference.
- B02 (08-11) ch002–ch014 · B03 (08-12) ch015–ch034 · B04 (08-12) ch035–ch052
  · B05 (08-12) ch053–ch070 · B06 (08-13) ch071–ch090 · B07 (08-13)
  ch091–ch110 · B08 (08-13) ch111–ch129 · B09 (08-13) ch130–ch155.
- **B10 (08-13) ch156–ch167 + whole-book close-out.** No deviation from the
  approved 10-batch plan; the final batch was run light on translation and
  heavy on close-out as planned.

## Checks run book-wide, and what they found

1. **Numeric invariants** (`check_numbers`, noise-guarded): clean on all B10
   units; four source-numeral idioms/names noised with targeted rules
   (萬狀, 絲毫無二 / 毫髮無二, 四馬路) — no real quantity masked.
2. **Parity / structure** (`check_structure`): PASS, all 12 units; 22 anchors
   resolved, 0 unresolved.
3. **Entity survival** (`qc_entities`): clean per bilingual file.
4. **Alignment + content-displacement** (`check_align`, `check_content`):
   clean; one displacement flag (ch167 四馬路) resolved by honouring the
   glossary distinction 四馬路 = "Fourth Avenue" vs 福州路 = "Fuzhou Road".
5. **Register** (`check_register --ref out/ch001_reading.md`): all 12 within
   tolerance of the frozen reference.
6. **Tail verification:** every unit's final paragraphs eye-read against the
   scan; ch167 (the book's last leaf) crop-verified in full.
7. **Crop-verification:** bank names (福源, 寅泰), the four counterfeit-coin
   methods, the coin/exchange numerals, and every ch167 actress/place name
   read at 3–4× magnification; recorded in `data/ocr_fixes.json`.
8. **Whole-book reconciliation** (`check_reconcile`): **epithet drift 0** —
   no cross-chapter rendering drift. Glossary forward 326/339 decided forms
   present in prose; the 13 "unused" forms live legitimately in notes,
   headings, or are covered by a pronoun/variant. **Spelling locale unified
   to British** (see below).
9. **Deep audit** (`out/deep_audit.md`): fixed-seed 4.1 % sample, 0 defects in
   the re-audited subset (see below).

### Spelling locale (reconciliation, check 12)

The book had drifted mixed British/American across batches. The frozen
reference ch001 and the preface use British forms ("honour"), so **British was
cascaded across the whole book** — all reading files, note and glossary
bodies, and figure anchors — via curated pairs (colour, honour, favour,
labour, neighbour, theatre, centre, defence, harbour, savour, flavour,
travelling, …). One genuine American spelling was caught in a note body
("centerpiece" → "centrepiece"). The reconciliation checker still prints a
residual MIXED flag from two locale-neutral words — **"laborious"** and
**"vigorous"**, which are spelled identically in British and American English
— caught by its `\blabor…`/`\bvigor…` prefix heuristic. These are checker
false positives, not real American spellings; no real American form remains in
the corpus.

## Observed error rate

A fixed-seed (`seed 42`) random sample of **16 paragraphs (4.1 %)** across the
whole book. Six paragraphs whose exact leaf could be pinned were re-audited
character-by-character against the original scans this pass — ch010, ch077,
ch117, ch148 (earlier batches) and ch161, ch162 (B10, already crop-verified) —
spanning first, middle, and final batches: **zero fidelity defects of any
class** (fabrication, dropped/altered numeral, invented precision,
displacement, name error). Zero in six is a small subset and does not, alone,
bound the rate tightly (binomially compatible with rates into the mid-teens of
a percent at 95 %); the real assurance is that every one of the 392 paragraphs
passed the full per-batch gate suite, and B10 was eye-transcribed and
crop-verified rather than trusted to OCR. Full report: `out/deep_audit.md`.

## Findings that need the commissioner's eye

- **None blocking.** The one judgement call this batch — reproduce the modern
  reprint imprint as a colophon, or not — was resolved as "not" (see *back
  matter* above); reversing it would be a small, clean change if preferred.
- The reconciliation checker's residual spelling flag is a documented false
  positive (see above); if a perfectly green reconcile is wanted, the checker
  could be patched to exempt locale-neutral `laborious`/`vigorous`, but that
  edits a gate to silence a non-defect and was deliberately **not** done.

## Fact-check verdicts (B10)

- **The January 28th Incident** (一二八, ch157): **CORROBORATED** — the 1932
  Shanghai War; Japanese attack on Zhabei/Hongkou 28 Jan 1932, 19th Route Army
  resisted over a month (standard histories).
- **En Xiaofeng** (恩曉峰, ch167): **CORROBORATED** — Manchu of Beijing
  (1887–1949), a celebrated female *laosheng* of Peking opera's early
  all-women stage.
- **The mixed-sex performance ban** (男女合演, ch167): **CORROBORATED** — the
  Beijing government forbade men and women acting together (reaffirmed 1913),
  which is why all-female troupes existed; the ban's later relaxation ended
  them.
- **某國 = Japan** (ch157) vs **日本 named** (ch162): the author's own veil and
  its dropping — rendered as printed, footnoted, verdict stated in the notes.
- Minor Shanghai theatres/banks (群仙, 丹桂, 妙舞臺, 大富貴; 福源, 寅泰) and the
  minor actresses are period-plausible but not individually corroborated;
  marked **provisional** in the glossary and noted at that level.

## Residual uncertainties a reader should know about

- **Provisional romanizations** (glossary `provisional`, build-marked): most
  of the ch167 all-girl-troupe actresses, the two B10 native banks, and a tail
  of minor figures from earlier batches.
- **The 2019 reprint is a reset, not a collation** of the 1933 original. Where
  it misprints (ch052, ch053, ch109, ch116, ch122 from earlier batches; **B10
  found none new**), the text is rendered to plain sense and footnoted.
- **Self-censorship / euphemism for Japan** (某國 in ch157, 日本 in ch162):
  rendered as printed, the contrast footnoted.
- **The author is an interested witness**: his anti-Japanese barbs (ch157,
  ch162) and moralizing are translated faithfully, not smoothed or endorsed.

## Provenance and method

- **Source:** *上海鱗爪* (風俗篇), Yu Muxia 郁慕俠 (orig. 1933), 2019 Taipei
  BOD reprint, 新銳文創 / 秀威資訊, ed. 蔡登山; ISBN 978-957-8924-38-3;
  vertical-RTL Traditional Chinese, image-only scan.
- **Pipeline:** PyMuPDF render → tesseract `chi_tra_vert --psm 5` scaffold
  (~85 %, too error-dense to trust) → **full eye-transcription and
  crop-verification of every page** into `data/zh` → reading translation →
  `make_bilingual` positional QC → the scripted gate suite → cumulative EPUB
  build → qa_epub + epubcheck.
- **Authority ledger:** this book's decided renderings fed back into
  `authority.json` under slug `scales-and-claws` (317 new terms, 22 appended;
  4 benign cross-book article/spacing variants recorded).

*This book is COMPLETE. Further work is a corrections pass, not a batch.*
