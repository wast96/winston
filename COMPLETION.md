# COMPLETION REPORT — *A Thousand Li of Rivers and Mountains* (千里江山图)

**Sun Ganlu, 2022 — the complete, densification-retrofitted annotated English edition.**
Deliverable: `out/A Thousand Li of Rivers and Mountains.epub`. Working branch: `claude/thousand-li`.

The book is finished, and the four-round annotation retrofit commissioned in
ASSESSMENT.md section 6 is complete. All 37 logical units of the source (the
opening epigraph, 34 titled chapters, the closing unsigned letter, and the
two-part appendix) are translated, annotated, and built into one cumulative,
fully navigable EPUB. This report stands in place of a next-round handoff.

(Obeys CLAUDE.md rule 6: no em dashes in this report's prose.)

## What the finished edition contains

- **Front matter:** an embedded cover (the source's own cover art, reproduced
  verbatim in color), a title page, and a full hyperlinked table of contents
  linking all 37 units.
- **The whole text:** the epigraph, all 34 chapters (ch02 to ch35), the unsigned
  letter (ch36), and the Appendix (ch37, Material One plus Material Two),
  rendered as clean, flowing English in the novel's own voice, with the apparatus
  kept out of the text and in the notes.
- **338 footnotes**, continuously numbered 1 to 338 in reading order, each linked
  both ways (reference to body and back), gathered on a Notes page grouped by
  chapter.
- **A glossary** of names, places and terms (the term ledger enforcing one
  rendering per referent across the book), and a **translator's note**.
- **A colophon** reproducing and translating the source's copyright leaf, with
  the publisher discrepancy resolved (see open items).
- **Scene typography** throughout (centered datelines and scene-break dividers)
  where the digital source marks its cuts only by a turn of sense, with no word
  added, dropped, or altered.
- **Metadata** tuned for the Apple Books and Kindle libraries: the document shows
  as *A Thousand Li of Rivers and Mountains* by Sun Ganlu, in English, with the
  cover.

## The annotation retrofit (the headline of this edition)

The book was first completed at **217 notes** (about 6 per chapter), annotated to
its own older target. ASSESSMENT.md measured that against the current shelf
directive and commissioned a **densification pass in four consolidated rounds,
thinnest-chapter-first**, adding fact-checked first-appearance notes and folding a
set of mechanical (Tier A) consistency conformances, with the reading text
otherwise frozen. The trajectory:

| stage | range | notes added | book total |
|-------|-------|-------------|------------|
| pre-retrofit | whole book | (baseline) | 217 |
| R1 | ch02 to ch10 | +79 | 296 |
| R2 | ch11 to ch19 | +23 | 319 |
| R3 | ch20 to ch28 | +13 | 331 |
| R4 | ch29 to ch37 (+ ch13 reconciliation) | +7 | **338** |

**Final per-chapter distribution** (36 units carry notes; ch01 is the epigraph):
ch02 28, ch03 11, ch04 14, ch05 18, ch06 8, ch07 22, ch08 15, ch09 12, ch10 11,
ch11 12, ch12 15, ch13 11, ch14 7, ch15 7, ch16 10, ch17 5, ch18 9, ch19 5,
ch20 13, ch21 11, ch22 8, ch23 8, ch24 8, ch25 8, ch26 9, ch27 7, ch28 8,
ch29 3, ch30 10, ch31 3, ch32 4, ch33 2, ch34 5, ch35 4, ch36 1, ch37 6.
Mean 9.4, range 1 to 28.

**Honest note on density.** The pass added +122 notes but did not reach the
directive band, and this was the correct outcome under the standing no-pad policy
(no round's launching chat or CORRECTIONS.md ever asked to push harder toward the
band). New notes fell sharply round on round (R1 ~15/chapter, R2 ~2.6, R3 ~1.4,
R4 ~0.8) for one structural reason: this is a single continuous novel whose
recurring referents are footnoted at FIRST appearance, so the later ranges, which
are the mission's execution and resolution, revisit places, people and
organizations already glossed earlier. R4 in particular is the resolution and the
two shortest units (a 553-character interior letter and the documentary appendix);
its real referents were nearly all already noted (Longhua and its pagoda and peach
blossoms; the Party's investigation and special-operations organs; the Nanjing
city wall; the Nineteenth Route Army and the January 28 Incident; the courier
lines and the painting the mission is named for). Every unit was read in full and
grepped against the whole apparatus before any note was written; the caps are
first-appearance discipline, not incuriosity. The three rounds' "HONEST NOTE ON
DENSITY" entries in PROGRESS.md record this in detail.

**Note quality.** Every new note was fact-checked against real scholarship
(Wikipedia EN/ZH, Baidu Baike, and academic, government and museum sources; never
Grok, Grokipedia, or any AI-written source), and each states its real-vs-fiction
and corroborated / uncorroborated / invention verdict in the note body.

## Tier A conformances folded across R1 to R4

All mechanical, grep-located, with `glossary.json`, the affected note bodies, and
`out/<id>_en.json` kept in lockstep, and the reading text otherwise frozen:

- **Date format normalized to "Month D, YYYY"** book-wide. The reading text and
  note bodies are now uniform; `register_tics.py`'s day-month-date battery reads 0
  over the whole book. The large job fell in R4: the ch37 appendix carried all 11
  remaining day-first dates. Republican-reckoning and lunar dates are left as
  period voice and footnoted.
- **authority.json decided renderings** conformed where they appear: 马斯南路
  Route Massenet, 海格路 Avenue Haig (R2); 大美晚报 the Shanghai Evening Post and
  Mercury, 反省院 reflection institute (case), 吴淞口 the mouth of the Wusong River
  (R1/R3, with the last reading-text occurrences at ch34/ch35 cleared in R4);
  老闸捕房 the Louza police station; 白区 the White areas (number; R4, note bodies
  only, since it appears nowhere in the reading text). A whole-book grep confirms
  0 remaining occurrences of any superseded form.
- **Locale spelling** conformed to American: the only genuine common-noun stray,
  "a piece of theatre" (ch27, twice), fixed to "theater"; real concession venue
  names keep their period "Theatre" spelling.
- **Deliverable naming**: `book.json` gained `deliverable`, the build target is
  the full English title, and each round shipped a stamped chat copy
  (`stamp_deliverable.py R<n>`).

## Whole-book reconciliation (final round)

- **Dongjiadu (董家渡)**: unnoted book-wide though it becomes the river-escape hub;
  a first-appearance note added at ch13. **Closed.**
- **The tram**: the ch29 note left as specifically the French Concession tram
  company; no low-value general note added at ch07. **Decided.**
- **The Central Liaison Bureau (中央交通局)**: the courier-lines note left at ch15,
  where the courier apparatus is the actual subject; at ch07 the bureau is only
  named in passing. **Decided.**
- **Zhonghui Trust Bank (中汇银行)**: found already noted at ch10; the logged
  "unnoted" item was stale. **Resolved.**
- **The Peach Blossom Spring allusion**: left at its ch28 title-payoff. Women's
  Normal University confirmed already noted at ch26; the Central Statistics Bureau
  (中统) already covered by the ch03 note, with the 军统 side added at ch35.
- **Drift check**: 97 decided renderings grep-counted across all 37 built units;
  one rendering per referent, no drift.

## Final tallies and QA

- Units: **37 / 37** translated. Paragraphs: **2,768**. Footnotes: **338**.
- `qa_epub.py`: **PASS** (50 files, 44 documents; 338 references = 338 bodies =
  338 backlinks; numbering sequential 1 to 338 in reading order; all links
  resolve; TOC links all 37 units).
- `check_structure.py` paragraph parity: OK on every unit. `check_numbers.py`:
  0 unresolved numerals across all machine-checkable units (re-run on every unit
  whose text changed in the retrofit). `register_tics.py`: day-month-date 0 and
  british-spelling 0 book-wide.
- The pre-retrofit blind double-translation and back-translation passes (with the
  one caught omission 从上海 restored) stand; the retrofit was additive apparatus
  and did not re-open the frozen prose.

## Residual uncertainties (all flagged in the notes)

The apparatus never launders uncertainty into fluent prose. Among the spans
marked, in the notes, as uncorroborated or as the novel's invention:

- **The Appendix as recovered history (ch37).** The martyr register is fiction in
  documentary dress. There was no mass execution at Longhua on April 4, 1933; the
  date is the author's, pointedly the eve of Qingming. The real anchor named in
  the note is the *Longhua Twenty-Four* secretly shot on February 7, 1931, among
  them the *Five Martyrs of the Left League*. The homage is to those real, and
  largely nameless, dead, which is why the one entry left without a name
  ("Anonymous") stands near the head of the roll.
- **The garrison's "32nd Army" (ch03)** is the novel's own; there was no such unit
  at Longhua. Flagged in the note and the translator's note.
- **New R4 flags.** The New Stage (新舞台) is real, but the novel places it on
  Penglai Road in 1933, whereas its documented sites were elsewhere and it had
  closed by the late 1920s, so the placement is flagged as an apparent conflation
  with the later Penglai Grand Theater. The dock "share gangs" (股党) system and
  the eight-share name are real, but the graded six/sixteen/thirty-two/seventy-two
  series the novel lists is its own extrapolation. The label 军统 postdates 1933
  (the descriptive "Military Commission's investigation group" is period-accurate).
- **Provisional romanizations** (glossary): forms not found in English-language
  scholarship, e.g. 宁绍山庄 Ningshao Manor, 马立斯大楼 the Morriss Building,
  普恩济世路 Pu'enjishi Road, 圣母院路 Shengmuyuan Road, 小浜湾 Xiaobangwan,
  田谷邨 the Tiangu Estate.
- **Named-but-unverified specifics**: e.g. the Rentai Bank Company and the Wang
  Jinzhi murder case (invention), the Ningshao Manor cemetery and the December
  1932 Puhui Creek / Caohejing joining project (uncorroborated), the "Mr. Song's
  brother" / T. V. Soong reading (an invited inference), and assorted local color
  (theater bills, brand names, dishes) flagged where it could not be independently
  confirmed.

## Known open items

- **Publisher discrepancy (resolved in the colophon).** The copyright leaf prints
  上海文化出版社 (Shanghai Culture Publishing House), but the ISBN prefix
  (978-7-5321-8331-9) and the book's Weibo and WeChat handles belong to
  上海文艺出版社 (Shanghai Literature and Art Publishing House); the latter is given
  as the true imprint and the leaf's error is flagged in the colophon note.
- **Regenerable, gitignored artifacts**: the bilingual QC files
  (`out/*_bilingual.md`), the built EPUB (`out/*.epub`), and the extracted source
  (`data/src/`). Tracked: the reading texts (`out/*_reading.md`), `out/*_en.json`,
  `data/zh/*.txt`, `edits/*.md`, and the JSON data files (`notes.json`,
  `glossary.json`, `scenes.json`, `book.json`).
- **Provenance to preserve**: `render_colophon`, the epigraph/dateline/scene-break
  support and the cover/metadata additions in `build_reading_epub.py`, the
  additive `check_numbers.py` lookbehind noise patches, and the retrofit scripts
  (`apply_edits.py`, `anchor_check.py`, `conform_r4.py`,
  `patch_note_bodies_r{2,3,4}.py`) must not be reverted.

The edition is complete and shelf-ready.
