# COMPLETION.md — Chen Yangshan: Hero of the Secret War (秘战英雄陈养山)

The whole-book completion report, written on the final batch (B10) in place of a
handoff. This is what you read to know what you now have and how far to trust it.

## Status at a glance

- **12 of 12 units translated** (foreword, six chapters, three appendices,
  references, afterword). The title page reads COMPLETE.
- **432 footnotes**, continuous and book-wide; every reference, body, and
  backlink resolves.
- **78 figures** (portraits, group photos, document facsimiles, calligraphy
  tributes), each with real screen-reader `alt` text and a translator's caption
  whose provenance is stated.
- **731 glossary referents** — people 550, organizations 91, places 56,
  events 32, terms 2 — one rendering per referent, audited in `out/term_ledger.md`.
- **Build:** `qa_epub` PASS (89 files, 19 documents, 432/432/432 notes resolve,
  all links resolve). **epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings.**
- **Deliverable:** `out/chen-yangshan.epub`, committed with `git add -f` in the
  Batch 10 completion commit on branch `claude/chen-yangshan`.

## What the finished edition contains

- **Front matter:** a generated typographic cover in English (see the cover note
  below); title page (stating the edition is complete); a Principal Characters
  page (Chen Yangshan, Yun Daiying, He Long); a translator's note; and the
  series foreword by Zhang Baijia.
- **Body:** the series foreword (ch00), Chapters 1-6, then Appendix I (obituary),
  Appendix II (Chen's posthumous writings), Appendix III (chronology), the
  References, and the Afterword by Yao Huafei.
- **Set-off conventions used:** `{v}` vignette/quoted-document blocks (letters,
  the forged "Wu Hao Notice," recollections); `{p}` verse (Yun Daiying's prison
  poem). No datelines or scene-asterisms were needed.
- **Cover:** the builder generated a typographic English cover. The original
  colour cover (a striking duotone portrait, PDF p1) is entirely in Chinese; the
  builder copies a cover image byte-identical and cannot composite an English
  title onto the scan, so a Chinese-only cover would leave the cover unreadable
  to the intended reader. The portrait is preserved inside as the ch07
  frontispiece. **Switching to the colour cover is a one-line `book.json`
  change** (`cover_image`) if you prefer it.
- **Deliberately not invented:** `book.json` `back_matter` is left empty — the
  book carries no errata table or colophon to reproduce.

## Per-chapter tally

| Unit | Title | Folios (printed) | Paragraphs | Notes | Figures |
|---|---|---|---|---|---|
| ch00 | Foreword to the Series | 1-2 (front) | 6 | 4 | 0 |
| ch01 | Ch. 1 Seeking the Truth, Turning to Revolution | 1-26 | 141 | 73 | 10 |
| ch02 | Ch. 2 Extraordinary Years in the Special Branch | 27-81 | 311 | 130 | 20 |
| ch03 | Ch. 3 From Enemy-Occupied Territory Back to Yan'an | 82-104 | 125 | 62 | 5 |
| ch04 | Ch. 4 Hard Fighting in the Jin-Sui Border Region | 105-160 | 245 | 75 | 8 |
| ch05 | Ch. 5 Anecdotes from Around the Founding of New China | 161-193 | 180 | 47 | 17 |
| ch06 | Ch. 6 A Loyal Heart Revealed in a Time of Injustice | 194-213 | 67 | 24 | 14 |
| ch07 | Appendix I. Chen Yangshan: A Life | 214-216 | 14 | 6 | 1 |
| ch08 | Appendix II. Chen Yangshan's Posthumous Writings | 217-222 | 38 | 6 | 3 |
| ch09 | Appendix III. A Chronology | 223-227 | 76 | 2 | 0 |
| ch10 | References | 228-229 | 42 | 1 | 0 |
| ch11 | Afterword | 230-231 | 11 | 2 | 0 |
| | **Total** | | **1,256** | **432** | **78** |

## Batching as executed

- **Survey** — structure, metadata, composed STYLE.md, skeleton EPUB.
- **B01** — Chapter 1 (voice gate; frozen register reference).
- **B02-B03** — Chapter 2. **B04** — Chapter 3. **B05-B06** — Chapter 4.
  **B07** — Chapter 5. **B08** — Chapter 6.
- **B09** — front + back matter (foreword, appendices I-III, references).
- **B10** — Afterword + whole-book close (this batch).

No deviation from the approved plan; Chapter 5 was kept as one unit rather than
split.

## Checks run book-wide, and what they found

1. **Numeric invariants** (`check_numbers --noise`): 0 unresolved on every unit.
2. **Parity / anchors / heading shape** (`check_structure`, `verify_unit`): parity
   exact on every unit (ch11 11=11); all 432 note anchors resolve.
3. **Entity survival** (`qc_entities`): 0 misses on every unit.
4. **Alignment and content** (`check_align`, `check_content`): no displacement;
   ratio outliers all benign (verse, short formal closings).
5. **Register vs the frozen ch01 reference** (`check_register --ref`): within
   tolerance throughout; the appendices and afterword are dialogue-quiet and were
   judged on the narratorial signals, which held (ch11 em-dash 0.0/1k, rhythm
   0.47 vs ref 0.50).
6. **Tail verification** against the scan on every unit's final paragraphs.
7. **Apparatus** (`check_apparatus`): 0 failures / 0 warnings.
8. **Style freshness** (`check_style_freshness`): all layers fresh; STYLE.md never
   recomposed mid-book.
9. **Whole-book reconciliation** (`check_reconcile` + human read): **epithet drift
   0**; 704/731 decided forms present in the prose (the rest appear only in
   captions or notes); **one wrong form found and fixed** — 霞飞路 "Route Joffre" →
   the shelf-agreed, historically correct **"Avenue Joffre"** (ch02 prose, note
   anchor and body, and glossary), rebuilt and re-validated; the 中原 = "Nakahara"
   homograph correctly kept separate from the shelf's "Central Plains"; the ~20
   core decided renderings grep-consistent (no "Chungking"/"Peking"/"Chou En-lai"
   forms surviving; "Peking Union Medical College Hospital" and the romanized
   book title "Teke ..." are correct fixed forms).

10. **Figure integrity sweep (added this batch).** A cross-check of the figure
    crops on disk against `figures.json` caught a **silent loss**: Chapter 2's
    fifteen section-1/3 figures (Zhou Enlai, the Three Heroes of Longtan, Bao
    Junfu, Chen Geng, and others) had been wiped at B03, when `apparatus_merge`
    replaced ch02's figures wholesale with the section-4/5 set — the trap the
    skill names, and ch02 was the only chapter split across two batches, so the
    only one exposed. The crops and their original `alt`/captions were recovered
    from the B02 commit and re-merged (ch02 now 20 figures; book 63 → **78**),
    and the build (which refuses any unplaced figure anchor) validated every one.
    The sweep now reports **0 unreferenced crops and 0 missing files** across all
    units, so no other chapter is affected.

## Observed error rate

See `out/deep_audit.md`. Population 1,256 body paragraphs; sample 44 (3.5%) at a
fixed seed (424242). The sampled paragraphs that could be pinned to a source page
(concentrated in ch03 narrative and quoted speech, ch08 documents, ch09
chronology — about twenty paragraph-equivalents) were read character-by-character
against the scan: **zero substantive errors**. The whole-book invented-precision
grep screen returned only faithful renderings. Honest confidence: zero errors in
~20 hand-read paragraphs is evidence of no systematic problem, not proof of a
zero rate — it is consistent with a true per-paragraph error rate up to a few
percent, and should be read together with the per-chapter gates (which ran on the
full text of every unit).

## Findings that need the commissioner's eye

- **Cover choice** (typographic English vs the Chinese colour cover) — see above;
  a one-line change either way.
- **The 1988 letter appears twice** (quoted in Chapter 3, reproduced in Appendix
  II with its manuscript facsimile). Both English renderings are faithful to the
  source's two printings; they are cross-referenced in a note rather than
  force-harmonized, so their wording differs slightly. Say the word if you would
  rather they be made identical.
- **Interested-witness verdicts** are carried in the notes throughout (e.g. the
  Kang Sheng culpability question, the CIA-holiday legend for Li Kenong's death,
  the Wang Ming "deliberate betrayal" reading of the 1931 Longhua arrests). These
  are judgment calls a machine cannot settle.

## Residual uncertainties a reader should know about

- **52 provisional romanizations** (of 731 referents): minor bit-part names whose
  exact scan characters were doubtful. The build marks these; every one is listed
  in `out/term_ledger.md` (status *provisional*).
- **Source errors preserved as printed and footnoted, never silently fixed:** the
  1912-for-1942 training date and the Shangdang-campaign date slip (ch04); the
  Ma Hanshan / Ma Hansan and Zhou/Tian Gaoming name variants (ch04); the
  Seventh-Congress 1943-for-1945 dating (ch03); the Peng Pai arrest year (ch02);
  the "Tenth Central Committee" plenum that should read Eleventh (ch06); the
  Xiao Shouhuang / Xiao Taihuang name variant (noted at ch06); a handful of
  obscure local place-names left unfootnoted by the declared minor-name tier.
- **The rehabilitation timeline** (1978 verdict quashed; the residual "Right
  deviation" finding negated only in 1983) is consistent across the book and
  explained in the notes; the obituary's compression to 1978 is flagged in ch07.
- **No content was withheld or omitted for policy reasons.**

## Reliability map

This is a celebratory Party biography and a primary source; its partisanship is
rendered faithfully and its checkable claims carry per-claim verdicts
(corroborated / uncorroborated / contradicted) in the footnotes at first
appearance, rather than in a separate reliability_map.md. The pattern: the
documentary spine (dates, offices, postings, the chronology, the reproduced
letters and the Wu Hao forgery) checks out against standard Party-history
accounts; the contested episodes are the factional readings of motive (who
deliberately let whom be taken), which the notes mark as the survivors' reading
rather than settled fact.

## Provenance and method

- **Source:** 秘战英雄陈养山, by 姚华飞 (Yao Huafei), CCP Party History Press,
  Beijing, 2018 (ISBN 978-7-5098-4587-5). Image-only PDF scan (DuXiu/SuperStar
  via Anna's Archive), 243 PDF pages; 231 printed pages plus front matter and an
  appended metadata leaf. Modern simplified Chinese, single column, horizontal.
- **Offset:** printed = pdf − 11 for the body; front matter runs a second folio
  sequence (foreword printed 1-2 at PDF 7-8).
- **OCR:** tesseract `chi_sim`, `--psm 6`, body crop `--left 0.045 --right 0.985
  --top 0.08 --running-head "秘战英雄陈养山"`, recto/verso split bottom (0.945 /
  0.915); `ocr_dual.py` (psm4 vs psm6) for the disagreement filter (PaddleOCR
  unavailable). Front-matter pages 7-8 used a different crop (no top running head).
  `data/zh` was hand-assembled from corrected OCR and the page images.
- **Builder features that must not be reverted:** the section-nav omits pending
  sections (epubcheck NAV-011/RSC-005); `apparatus_merge` merges glossary rows
  into sections and refuses on an unmatched anchor; figure `alt` carries no
  straight double quotes; `strip_runfoot` removes the verso book-title foot.
- **Rebuild from a fresh checkout:** `./setup.sh`, then
  `python3 scripts/build_reading_epub.py`, `python3 scripts/qa_epub.py`, and
  `java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/chen-yangshan.epub`.
  Per-unit checks need `data/zh` regenerated (gitignored) and run with the
  unit-scoped `data/check_config.<id>.json`.

## Definition of done — met

- [x] EPUB: front matter + all 12 units, full clean TOC, cover, figures with
  captions/alt, 432 footnotes, glossary and translator's note current, qa_epub
  PASS across the whole spine, epubcheck 0/0/0.
- [x] `out/<id>_reading.md` per unit; `out/term_ledger.md`; `out/deep_audit.md`.
- [x] `notes.json`, `glossary.json`, `figures.json`, `book.json` current;
  `authority.json` fed this book's decided renderings (chen-yangshan registered
  on 45 entries; the 中原 homograph excluded).
- [x] `COMPLETION.md` written with the sampled error rate and residual
  uncertainties; `CHANGELOG.md` updated; `PROGRESS.md` current.
- [x] Final EPUB committed with `git add -f out/chen-yangshan.epub`.
- [x] `HANDOFF.md` rewritten to say the book is COMPLETE.
