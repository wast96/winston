# COMPLETION REPORT — *A Thousand Li of Rivers and Mountains* (千里江山图)

**Sun Ganlu, 2022 — the complete annotated English edition.**
Deliverable: `out/thousand-li.epub`. Working branch: `claude/thousand-li`.

The translation is finished. All 37 logical units of the source — the opening
epigraph, 34 titled chapters, the closing unsigned letter, and the two-part
appendix — are translated, annotated, and built into one cumulative, fully
navigable EPUB. This report stands in place of a next-batch handoff.

## What the finished edition contains

- **Front matter:** an embedded cover (the source's own cover art, reproduced
  verbatim in color), a title page, and a full hyperlinked table of contents.
- **The whole text:** the epigraph, all 34 chapters (ch02–ch35), the unsigned
  letter (ch36), and the Appendix (ch37, Material One + Material Two), rendered
  as clean, flowing English in the novel's own voice, apparatus kept out of the
  text and in the notes.
- **217 footnotes**, continuously numbered 1–217 in reading order, each linked
  both ways (reference ↔ body), gathered on a Notes page grouped by chapter.
- **A glossary** of names, places and terms — the term ledger enforcing one
  rendering per referent across the book — and a **translator's note**.
- **A colophon** reproducing and translating the source's copyright leaf, with
  the publisher discrepancy resolved (see open items).
- **Scene typography** restored throughout (centered datelines and scene-break
  dividers) where the digital source marks its cuts only by a blank of sense —
  no word added, dropped, or altered.
- **Metadata** tuned for the Apple Books and Kindle libraries: the document
  shows as *A Thousand Li of Rivers and Mountains* by Sun Ganlu, in English,
  with the cover.

## Final tallies

- Units: **37 / 37** translated. Paragraphs: **2,768**. Footnotes: **217**.
- Batches: B01–B12, all shipped. Notes by the last batches: B10 → 195, B11 →
  204, **B12 → 217** (13 new: ch34 ×4, ch35 ×2, ch36 ×1, ch37 ×6).
- `qa_epub.py`: **PASS** — 50 files, 44 documents; 217 references = 217 bodies
  = 217 backlinks; numbering sequential in reading order; all links resolve.

## Checks run book-wide

- **Faithful, complete quotation.** Every unit's reading text and parity source
  are split from one aligned bilingual QC file that quotes the digital source
  verbatim (`make_bilingual.py` enforces paragraph parity at build time).
- **Automated invariants.** `check_numbers.py` (every numeral/date/year survives
  source→target) and `check_structure.py` (paragraph parity; note anchors
  resolve; heading shape; glossary drift) run on every unit; the whole-book
  re-run is clean (0 unresolved numbers across all 32 machine-checkable units;
  217 anchors resolve; glossary drift 0).
- **Blind double-translation** and **back-translation** passes, in separate
  contexts, on every batch's argumentative/literary passages, sampling the plain
  narration. The final batch's one caught omission (从上海, "from Shanghai") was
  restored.
- **Fact-check against real scholarship** (Wikipedia, Baidu Baike, academic and
  government/museum sources; never Grok/Grokipedia or any AI-written source).
  Where the story meets documented history the notes say whether a person,
  place or event is real and whether the particular claim is corroborated,
  uncorroborated, or the novel's own invention.
- **Auditable term ledger** (`glossary.json`) and **continuous note numbering**,
  both verified end to end.

## Known open items

- **Publisher discrepancy (resolved in the colophon).** The source's copyright
  leaf prints the publisher as 上海文化出版社 (Shanghai Culture Publishing House),
  but the ISBN publisher prefix (978-7-**5321**-8331-9) and the book's Weibo and
  WeChat handles all belong to 上海文艺出版社 (Shanghai Literature and Art
  Publishing House). The latter is given as the true imprint; the leaf's error
  is flagged in the colophon's English note.
- **The garrison's "32nd Army"** (ch03) is the novel's own; there was no such
  unit at Longhua. Flagged in the note and in the translator's note.
- **The bilingual QC files** (`out/*_bilingual.md`) and the built EPUB and the
  extracted source (`data/src/`) are gitignored and regenerable; the reading
  texts, `*_en.json`, `data/zh/*.txt`, and the JSON data files are tracked.

## Residual uncertainties (all flagged in the notes)

The apparatus never launders uncertainty into fluent prose. The notes mark, as
uncorroborated or as the novel's invention, among others:

- **The Appendix as recovered history (ch37).** The martyr register is fiction
  in documentary dress. There was no mass execution at Longhua on 4 April 1933;
  the date is the author's, pointedly the eve of Qingming. The real anchor named
  in the note is the *Longhua Twenty-Four* secretly shot on 7 February 1931,
  among them the *Five Martyrs of the Left League*. The homage is to those real,
  and largely nameless, dead — which is why the one entry left without a name
  ("Anonymous") stands near the head of the roll.
- **Provisional romanizations** (glossary): 宁绍山庄 Ningshao Manor, 马立斯大楼
  the Morriss Building, 普恩济世路 Pu'enjishi Road, 圣母院路 Shengmuyuan Road,
  小浜湾 Xiaobangwan, 田谷邨 the Tiangu Estate — forms not found in
  English-language scholarship.
- **Named-but-unverified specifics**: e.g. the Rentai Bank Company and the Wang
  Jinzhi murder case (invention), the Ningshao Manor cemetery and the Dec-1932
  Puhui Creek / Caohejing joining project (uncorroborated), the "Mr. Song's
  brother" / T. V. Soong reading (an invited inference), and assorted local
  color (theater bills, brand names, dishes) flagged where it could not be
  independently confirmed.

## Provenance / method notes

- The novel's principal characters are the author's invention; their world is
  real. The edition dramatizes a fictional mission against the true background
  of the underground Party in the Shanghai of the White Terror.
- Two `check_numbers.py` lookbehind patches were added this batch (clock time
  十一点; ten-odd 十几分钟), in the same additive style as earlier batches — they
  only ever *remove* source numerals conditionally, so they cannot mask a
  dropped quantity; no prior patch was reverted.
- `render_colophon`, the epigraph/dateline/scene-break support, and the cover +
  metadata additions to `build_reading_epub.py` are all in place and must not be
  reverted.
