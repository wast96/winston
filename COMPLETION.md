# COMPLETION REPORT — On a Hair Trigger (一触即发) by Zhang Yong

The annotated English translation is complete. This report summarizes the
finished book, the checks run across the whole text, and the known editorial
flags. It replaces a handoff: there is no next batch.

## The book

- Source: a digital EPUB of 一触即发 (Zhang Yong / 张勇), a Calibre-repackaged
  Unicode text, no OCR, one embedded image (the cover). 231,699 translatable
  source characters.
- Structure: flat. Prologue (楔子) plus 35 chapters, one seven-character couplet
  title each, continuous prose, no sections or subsections. 36 units in all.
- Deliverable: `out/On a Hair Trigger.epub`, a single cumulative EPUB with a
  full hyperlinked table of contents, a regenerated title page and cover,
  continuous footnote numbering, a Translator's Note, and a glossary.

## What was produced

- Reading translation: `out/<id>_reading.md` for ch00 to ch35 (7,082 paragraphs
  of English, one per source paragraph).
- Bilingual QC files: `out/<id>_bilingual.md` for every unit (QC only, never
  shipped), source `>` line copied verbatim beneath which sits the English.
- 114 footnotes (`notes.json`), numbered #1 to #114 by the builder in reading
  order, at roughly reference density (about three per chapter-equivalent).
- Glossary (`glossary.json`): 273 entries — 99 people, 73 organizations, 60
  places, 41 terms — of which 145 are `decided`, 90 `attested`, 38 `provisional`.
- Translator's Note (from `book.json`), rendered as back matter with the glossary.

## Batches

Thirteen batches, all done, all checks green (see `PROGRESS.md` for each):
B01 ch00-04, B02 ch05-07, B03 ch08-10, B04 ch11-13, B05 ch14-15, B06 ch16,
B07 ch17-18, B08 ch19-21, B09 ch22-24, B10 ch25-27, B11 ch28-30, B12 ch31-33,
B13 ch34-35 (final).

## Checks run book-wide, and their results

- Faithful verbatim quotation (check 1): every unit's parity source
  (`data/zh/<id>.txt`) diffed line-for-line against the raw source paragraphs.
  ZERO content diffs across all 36 units; no source paragraph dropped or merged.
- Paragraph parity (check 4): `check_structure.py --pairs` OK for all 36 units
  (source paragraph count equals translation paragraph count everywhere).
- Numeral survival (check 4): `check_numbers.py --noise data/noise.txt` reports
  0 unresolved for all 36 units. Every date, year, count, and clock time in the
  source survives into the English; the project non-quantity list `data/noise.txt`
  records each lexicalized/idiomatic numeral excluded, with its reason.
- Note integrity (`qa_epub.py`): 114 references = 114 bodies = 114 backlinks,
  numbering sequential in reading order; every internal link resolves. PASS
  (48 files, 42 documents).
- Term ledger (check 5): one decided rendering per referent, enforced across all
  chapters via `glossary.json`.
- Blind double translation and round-trip back-translation (checks 2/3) applied
  to the argumentative and lyrical passages throughout and sampled on plain
  narration; deep paranoid audits (check 8) run each batch on 3-5% of the text.
  Observed residual error rate ~0% after correction; the failure mode caught in
  practice was numeric (e.g. a "hundred" idiom first rendered "thousand"),
  surfaced mechanically by `check_numbers` before build.

## Known annotations, anachronisms, and editorial flags

Recorded in the notes and glossary and gathered here for the read-through:

- Anachronisms in the source, footnoted where they land: fabi (法币, 1935) used
  loosely for the early-1930s present; the Park Hotel (国际大饭店, opened 1934)
  named a little early; Fung Yu-lan's *A Short History of Chinese Philosophy*
  (《中国哲学简史》 / Macmillan, pub. 1948) used as a password (note at Chapter 28);
  the Xin Zhonghua Bao name (Yan'an, 1937) loose; the Nagoya obi (名古屋带, c.
  1920) tied loosely to the Momoyama age (note at Chapter 30).
- Provisional romanizations (marked `provisional` in the glossary) are
  romanizations not attested in English-language scholarship, including the
  Japanese agents Koyama Eiko (小山缨子), Koyama Chino (小山千野, to whom the source
  assigns no gendered pronoun, so none is supplied), and Momokawa Keiko
  (百川丛惠子, whose middle graph 丛 has no settled kana reading).
- Identity devices rendered as they stand, never silently reconciled: the twins'
  A-Chu / A-Ci naming, the Chapter 33 body-double swap (Muci disguised as A-Chu,
  hypnotized while the real A-Chu waits), and the impostor "Amah A-Yue" (a
  Japanese agent, not the real Amah A-Yue, murdered twenty years before and
  identified as the cut-in-two skeleton).
- Chapter titles: several are genuine Tang/Song quotations or allusions (traced
  and footnoted at first relevance); many are the author's own seven-character
  pastiche in the classical manner (so noted rather than forced onto a source).
- Historical references checked against scholarship and marked corroborated,
  including the Mukden / September 18th Incident, the China League for Civil
  Rights, Gu Shunzhang's and Wu Hao's (Zhou Enlai's) real histories, the Land
  Survey Department of the IJA General Staff, the Thirty-Six Stratagems, and the
  closing 1937 National Government wartime broadcast issued around the fall of
  Shanghai.

## Rebuilding from a clean checkout

`data/src`, `data/zh`, `out/*_en.txt`, and `out/*.epub` are gitignored. From a
fresh clone: run `scripts/ingest_epub.py source.epub` to rebuild `data/src`, then
`scripts/split_bilingual.py` on each committed `out/<id>_bilingual.md` (using the
zh titles in `book.json`) to rebuild `data/zh` and `out/<id>_reading.md`, then
`scripts/build_reading_epub.py "out/On a Hair Trigger.epub"` and
`scripts/qa_epub.py "out/On a Hair Trigger.epub"`.
