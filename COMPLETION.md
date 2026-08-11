# COMPLETION.md — The Golden Roc Dynasty (陆小凤传奇·金鹏王朝, Gu Long)

Whole-book completion report, written on the final batch (B08) in place of a
handoff. This is the document to read to know what the finished edition
contains and how far to trust it.

## Status at a glance

- **13 of 13 units translated** (prologue + twelve chapters); 4,410 merged
  paragraphs.
- **78 translator footnotes**; **0 source-edition footnotes** (the source
  carries none of its own, confirmed by grep over every unit).
- **0 figures** (the novel has no interior images; the source's two decorative
  endpapers carry no story content and were not brought in).
- **86 glossary rows**: 56 people, 6 organisations, 13 places, 11 terms and
  epithets. All are status *decided* except one *attested* (鲁班, Lu Ban, a
  real historical figure). No *provisional* readings remain.
- **qa_epub PASS** (27 files, 20 documents, all links resolve; 78 note
  references / 78 bodies / 78 backlinks).
- **epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings / 0 infos** (EPUB 3.3).
- Deliverable **`out/lu-xiaofeng-1.epub`**, force-committed on branch
  `claude/lu-xiaofeng-1` in the final B08 commit that also carries this report.

## What the finished edition contains

- **Front matter**: cover (the source's own cover image, reused byte-identical),
  title page, a Principal Characters cast page (built from the `principal`
  flags in the glossary), and the native generated table of contents.
- **Body**: the prologue (四 vignettes, each a titled section) and twelve
  numbered chapters. The source's bare-numeric scene markers render as `***`
  scene breaks; the coda (ch13) has none and is one continuous scene.
- **Set-off conventions used**: `***` scene breaks throughout; italic internal
  monologue in the coda. No verse, dateline, hour-gloss, or vignette markers
  were needed in this book beyond scene breaks (the prologue's vignette titles
  are true section headings, carried as such).
- **Back matter**: a Notes section (all 78, numbered continuously), and a
  combined Translator's Note and Glossary page. The Translator's Note is the
  custom text authored in `book.json` (composition date stated so the 2013
  edition date is not mistaken for the work's date).
- **Nothing invented to fill an optional slot**: there is no errata or
  reliability apparatus because the novel is fiction and makes no checkable
  historical claim in its own voice (the historical figures it name-drops,
  e.g. Tian Dan, Li Houzhu, Lu Ban, are handled in footnotes, verdicts stated).

## Per-chapter tally

| Unit | Title | Paragraphs | Notes | Figures |
| --- | --- | --- | --- | --- |
| ch01 | Prologue | 154 | 15 | 0 |
| ch02 | Ch. 1. The Man with Four Eyebrows | 289 | 11 | 0 |
| ch03 | Ch. 2. Princess Danfeng | 323 | 4 | 0 |
| ch04 | Ch. 3. The Great King of the Golden Roc | 333 | 6 | 0 |
| ch05 | Ch. 4. The Feast | 306 | 6 | 0 |
| ch06 | Ch. 5. A Song of Sorrow | 272 | 4 | 0 |
| ch07 | Ch. 6. Pearls and Splendour | 226 | 4 | 0 |
| ch08 | Ch. 7. The Seven Heroes of the Marketplace | 346 | 6 | 0 |
| ch09 | Ch. 8. The Four Beauties of Emei | 283 | 4 | 0 |
| ch10 | Ch. 9. The Flying Swallow Comes and Goes | 237 | 4 | 0 |
| ch11 | Ch. 10. The Maze Tower | 289 | 5 | 0 |
| ch12 | Ch. 11. The Sixth Toe | 1,235 | 6 | 0 |
| ch13 | Ch. 12. Coda | 117 | 3 | 0 |
| **Total** | | **4,410** | **78** | **0** |

Note density tapers as designed: heaviest in the prologue and first chapter
(15, 11), where the furniture of the jianghu, money, and custom is introduced,
then settling to 3 to 6 once the reader has the background. ch12 is the long
climax; its low note count reflects that its material was already covered.

## Batching as executed

Eight batches, one conversation each, on the approved plan (final EPUB
attached and next kickoff pasted in chat at every batch). Completion date
2026-08-11; per-batch dates were not separately logged.

- **B01** — Prologue (ch01). The first-chapter voice gate: revised across
  rounds 2 to 5, then frozen as the register and paragraphing reference.
- **B02** — Chapter 1 (ch02).
- **B03** — Chapters 2 to 3 (ch03, ch04).
- **B04** — Chapters 4 to 5 (ch05, ch06).
- **B05** — Chapters 6 to 7 (ch07, ch08).
- **B06** — Chapters 8 to 10 (ch09, ch10, ch11).
- **B07** — Chapter 11 (ch12), the climax, its own batch.
- **B08** — Chapter 12 (ch13, the coda) plus this whole-book completion pass.

No deviation from the approved batch plan.

## Checks run book-wide, and what they found

The CLAUDE.md QC contract, with final whole-book results:

1. **Verbatim quotation + parity** — by construction via `make_bilingual.py`;
   `check_structure.py` confirms parity per unit (154/289/323/333/306/272/226/
   346/283/237/289/1235/117, all source == translation).
2. **Numeric invariants** — `check_numbers.py --noise data/noise.txt` clean on
   every unit (ch13: 117 pairs, 0 unresolved). Every real quantity is carried
   in the English; only documented idiom/lexical-numeral classes are noised
   (the B08 addition: 三角架 "tripod", a three-legged-frame compound).
3. **Entity survival** — `qc_entities.py` 0 misses on ch13 (and prior).
4. **Alignment and content/displacement** — `check_align.py` (ch13 median 4.29,
   no strays) and `check_content.py` across all 13 units: every glossary-name
   occurrence lands in its paired paragraph (ch13: 81 occurrences).
5. **Register vs the frozen reference** — `check_register.py --ref ch01` on
   ch13: 34.7 contractions/1k = 0.86x of the reference, within tolerance.
6. **Tail verification** — the coda's final paragraphs were read against the
   source before shipping; the closing lament chimes, as the source intends,
   with Lu Xiaofeng's line that closed ch12.
7. **Blind double translation / 8. Round-trip / 9. Deep audit** — see
   "Observed error rate" below.
10. **Scholarship consistency** — historical name-drops (Han Feizi's
    spear-and-shield, the six-toe physiognomy tradition, the Liu-Song
    abdication lament, Tian Dan / Guangwu / Li Houzhu / Huizong, Lu Ban,
    "inviting the ruler into the urn") are footnoted with the verdict stated;
    the fiction's own furniture is glossed, not footnoted.
11. **Whole-book reconciliation** — `check_reconcile.py` plus a by-hand
    grep-count of ~25 decided renderings across all built units. Results:
    - **Spelling locale**: was mixed (British dominant, a handful of American
      forms); cascaded to **uniform British** (colour, honour, realise, sabre)
      across reading files and their JSON sources. Final: 87 British / 0
      American on the curated pairs.
    - **Epithet drift**: one genuine case fixed — 练子枪 was "chain-spear"
      (ch04) and "chain-whip spear" (ch07); unified to **chain-spear**
      book-wide. The remaining `check_reconcile` "drift candidates" are
      distinct source compounds that share an English stem (剑光 sword-light
      vs 剑锋 sword-point vs 剑势 sword-force, etc.), not drift; reviewed, left.
    - **Glossary-forward**: 83 of 86 decided forms appear verbatim; the three
      "unused" are benign surface variants confirmed present (the prose says
      "the celebrated Four Heroes of Jiangdong" with an adjective, "The Green
      Cloud" for the inn's short name, sentence-initial "Sugar-roasted
      chestnuts"), not missing renderings.
    - Name-count spot check: Lu Xiaofeng 1,566, Hua Manlou 616, Huo Xiu 201,
      etc., all in the single decided form; variant probes (Blue Robe, Golden
      roc, Pearls and Splendor, lightness skill) all zero.

## Observed error rate

Random-sample deep audit, `out/deep_audit.md`:

- **Population** 4,410 paragraphs; **sample** 132 (3.0%), **fixed seed**
  20260811, drawn in reading order across all 13 units in proportion to size.
- **Flags**: **0 faithfulness errors** across the four classes (omission,
  addition, mistranslation, invented precision). Two stylistic observations
  (a couple of un-tagged rapid-exchange turns whose source tag is 霍老头道; a
  context-supplied "yours" in ch06) were adjudicated as non-defects: no content
  added or dropped.
- **Honest confidence statement**: zero errors in 132 does **not** prove a zero
  rate. By the rule of three, it bounds the true paragraph-level error rate
  below approximately **3/132 = 2.3% at 95% confidence** — strong evidence of a
  low rate, not a certificate of perfection. The scripted per-chapter checks
  cover the other 97%.

## Findings that need the commissioner's eye

None outstanding. The one plot point a reader may find puzzling is the coda's
last twist: Shangguan Xue'er insists her sister Shangguan Feiyan is alive and
was the herb-gathering old woman, though ch12 shows Feiyan's throat cut. This
is the source's own deliberate hook into Volume 2, not a translation slip; it
is preserved as written and surfaced in the closing footnote, which also
records the source's end-of-volume marker and its pointer to *Legend of Lu
Xiaofeng 2: The Embroidery Bandit* (绣花大盗).

## Residual uncertainties a reader should know about

- **No provisional glossary readings remain** (all 86 rows are decided or, in
  one case, attested). There is nothing marked provisional in the build.
- **Digitization glitches** in the commercial source were rendered to plain
  sense and listed in `PROGRESS.md` per batch; none required a reading-
  uncertainty footnote (they are mechanical typos, not textual cruxes).
- **The source's own end-matter** (the volume-end mark and the sequel teaser)
  is not story text; it is excluded from the chapter body, recorded in
  `book.json` `_source_note`, and surfaced to the reader in the coda's closing
  footnote.

## Reliability map (historical books)

Not applicable. This is a wuxia novel; it makes no historical claim in its own
narrative voice. The real-world figures and phrases it alludes to are handled
individually in footnotes, each with its verdict (corroborated) stated inline.

## Provenance and method

- **Source**: a 2013 Henan Literature and Art Publishing House digital EPUB of
  陆小凤·1·金鹏王朝 (from the 古龙文集 collected-works line). Simplified
  characters. The novel was first serialised 1976 to 1977. No scan, no OCR: the
  source is real digital text, translated from `data/src/` verbatim-paired.
- **Pipeline as run** (per batch): read the source; fix any extractor splits
  and recover set-off formatting; translate to the frozen house style; author
  merged English paragraphs into `scratchpad/<id>_en.txt`; build with a
  re-ranged `scratchpad/build_b0N.py` (make_bilingual gives parity and verbatim
  quotation by construction, then split_bilingual); run verify_unit /
  check_align / check_content / qc_entities; merge notes with
  apparatus_merge.py and glossary rows under the two-level sections directly;
  rebuild the cumulative EPUB; qa_epub, epubcheck, check_structure,
  check_register.
- **Builder features that must not be reverted**: the merged-paragraph build
  method (`build_b0N.py`), the two-level glossary (apparatus_merge for NOTES
  only), the `***`-skip and spelled-number patches in the checkers, the
  documented `data/noise.txt` entries, and the pending-aware / auto-cleaning
  TOC (which now emits a clean, scaffolding-free contents page because the book
  is complete).
- **Rebuild from clean** (exact commands): `./setup.sh`; if `data/src` is
  absent, `python3 scripts/ingest_epub.py source.epub` (do not overwrite
  book.json); `python3 scripts/build_reading_epub.py`; then
  `python3 scripts/qa_epub.py out/lu-xiaofeng-1.epub` and
  `java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/lu-xiaofeng-1.epub`.
- **Regression note**: `./setup.sh` reports 9/10 with one expected failure,
  "hook stands down on template stub"; that case only passes while HANDOFF.md
  holds the template placeholder, and HANDOFF now (correctly) holds the
  completion notice, so the Stop hook enforces and that one test necessarily
  reads FAIL. Not a defect.

## Definition of done — met

- [x] Complete EPUB with cover and clean TOC committed (`out/lu-xiaofeng-1.epub`,
      force-committed with `git add -f`).
- [x] qa_epub PASS and epubcheck 0/0/0/0.
- [x] Per-unit `_reading.md` + `_en.json` present for all 13 units.
- [x] `out/term_ledger.md` rendered from the glossary (86 rows).
- [x] `out/deep_audit.md` written with the honest error-rate statement.
- [x] Both note streams complete (78 translator notes; 0 source notes, by
      design).
- [x] `authority.json` fed back (86 wuxia renderings added, keyed by hanzi
      under the `lu-xiaofeng-1` slug).
- [x] `COMPLETION.md` written (this file).
- [x] `PROGRESS.md` maintained; `HANDOFF.md` rewritten to the COMPLETE notice
      and not touched afterward (the Stop hook keys off it).
