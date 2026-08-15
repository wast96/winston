# COMPLETION.md — Burn, O Sword! (燃えよ剣), Shiba Ryōtarō

Whole-book completion report, written on the final batch (B15) in place of a
handoff. This is the document to read to know what the finished edition contains
and how far to trust it.

## Status at a glance

- **Units translated: 71 / 71** — 68 novel chapters (ch01–ch68) + 3 back-matter
  units (afterword, film-director commentary, author bio). The whole book.
- **Translator notes: 481** (continuous numbering, one stream; no source-note
  stream — the source carries no author footnotes).
- **Figures: 0 in-text.** The source's images were a cover, a device layout
  notice, and reading marks; the cover art (`data/figs/embed0009_HD.jpg`) is
  reused byte-identical, and nothing was invented to fill a figure slot.
- **Glossary: 302 rows** — people 172, places 79, organizations 24, terms 27.
- **Body paragraphs: 12,228** across the 71 units.
- **qa_epub: PASS** — 85 files, 78 documents, 481 note references / 481 bodies /
  481 backlinks, all links resolve.
- **epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings / 0 infos** (EPUB 3.3).
- **Deliverable:** `out/burn-o-sword.epub`, committed with `git add -f` on branch
  `claude/burn-o-sword` in the B15 completion commit.

## What the finished edition contains

- **Front matter:** title page (from metadata), a five-paragraph translator's
  note, and a Principal Characters cast page (twelve flagged principals:
  Hijikata, Kondō, Okita, Inoue, Nagakura, Shichiri, Harada, Katsura, Yamanami,
  Serizawa, Saitō Hajime, Oyuki).
- **The novel:** 68 titled chapters, unnumbered as in the source, each a single
  spine document, flat. Scene breaks are set off with `***`; the source's kaiti
  vignettes, datelines, verse, and hour-glosses use the `{v}/{d}/{g}/{p}`
  markers; short quotation + attribution pairs are display-joined (`{j}`) so the
  dialogue reads inline while paragraph parity with the source is preserved by
  construction.
- **Back matter (translated in full):** ch69 あとがき, Shiba's own afterword;
  ch70 解説, the 2020 commentary by film director Harada Masato on his screen
  adaptation; ch71, the publisher's biographical notice of Shiba.
- **Apparatus:** a footnotes section (popup `epub:type="footnote"` asides), a
  glossary, and the cast page. Every note anchor is a verbatim unique substring;
  bodies are XHTML with numeric character references only.
- **Cover:** the source's own cover, reused byte-identical (EPUB3 + legacy
  declarations), as the commissioner asked.
- **Deliberately NOT done:** no source-note stream was opened (the source has no
  author notes); no in-text figures were fabricated; nothing was invented to
  bridge a gap anywhere.

## Per-chapter tally

| Unit | Title | Paragraphs | Notes | Figures |
|---|---|---|---|---|
| ch01 | The Women's Night Market | 160 | 15 | 0 |
| ch02 | Cutting Down Rokusha | 215 | 14 | 0 |
| ch03 | Shichiri Kennosuke | 178 | 7 | 0 |
| ch04 | The Waiwai Tennō | 198 | 4 | 0 |
| ch05 | Bubaigawara | 172 | 5 | 0 |
| ch06 | The Moon and the Mud | 212 | 3 | 0 |
| ch07 | The Edo Dōjō | 189 | 7 | 0 |
| ch08 | Katsura Kogorō | 202 | 5 | 0 |
| ch09 | The Hachiōji Raid | 178 | 4 | 0 |
| ch10 | The Sutasuta Monk | 168 | 6 | 0 |
| ch11 | The Bringer of Ill Luck | 152 | 11 | 0 |
| ch12 | The Rōshigumi | 187 | 8 | 0 |
| ch13 | Kiyokawa and Serizawa | 170 | 11 | 0 |
| ch14 | Born at Last | 213 | 10 | 0 |
| ch15 | Shijō Great Bridge | 174 | 8 | 0 |
| ch16 | The Takase River | 218 | 8 | 0 |
| ch17 | The Yamanoo in Gion | 203 | 9 | 0 |
| ch18 | The Warrior's Code | 185 | 8 | 0 |
| ch19 | Reunion | 215 | 10 | 0 |
| ch20 | The Crossroads at Nijōhanjiki-chō | 195 | 4 | 0 |
| ch21 | The Code of the Corps | 180 | 7 | 0 |
| ch22 | The Ikedaya | 171 | 9 | 0 |
| ch23 | Ikedaya: A Coda | 133 | 7 | 0 |
| ch24 | Turmoil in the Capital | 136 | 7 | 0 |
| ch25 | The Chōshū Army Storms In | 165 | 5 | 0 |
| ch26 | Itō Kashitarō | 163 | 5 | 0 |
| ch27 | Kashitarō Comes to Kyoto | 174 | 5 | 0 |
| ch28 | New Year, First Year of Keiō | 178 | 6 | 0 |
| ch29 | Toshizō the Hated | 165 | 6 | 0 |
| ch30 | Clouds over Shijō Bridge | 188 | 9 | 0 |
| ch31 | Rain on the Horikawa | 166 | 3 | 0 |
| ch32 | Oyuki | 213 | 5 | 0 |
| ch33 | Red and White | 179 | 3 | 0 |
| ch34 | Yohei's Place | 194 | 9 | 0 |
| ch35 | The Duel at Nijō Nakasu | 196 | 8 | 0 |
| ch36 | The Chrysanthemum Banner | 195 | 7 | 0 |
| ch37 | With Oyuki | 190 | 7 | 0 |
| ch38 | Edo Diary | 184 | 7 | 0 |
| ch39 | The Sword's Fate | 179 | 10 | 0 |
| ch40 | The Great Turn | 145 | 5 | 0 |
| ch41 | Toshizō at Fushimi | 180 | 6 | 0 |
| ch42 | The Battle of Toba-Fushimi (I) | 166 | 8 | 0 |
| ch43 | The Battle of Toba-Fushimi (II) | 174 | 9 | 0 |
| ch44 | The Battle of Toba-Fushimi (III) | 220 | 6 | 0 |
| ch45 | The Battle of Toba-Fushimi (IV) | 181 | 7 | 0 |
| ch46 | Toshizō at Osaka | 176 | 7 | 0 |
| ch47 | The Pine Wood | 188 | 6 | 0 |
| ch48 | Saishō-an | 219 | 3 | 0 |
| ch49 | To Edo | 163 | 11 | 0 |
| ch50 | The Northern March | 185 | 8 | 0 |
| ch51 | Advance into Kōshū | 181 | 9 | 0 |
| ch52 | The Battle of Katsunuma | 178 | 6 | 0 |
| ch53 | Mustering at Nagareyama | 175 | 8 | 0 |
| ch54 | The Parting | 202 | 13 | 0 |
| ch55 | Ōtori Keisuke | 177 | 5 | 0 |
| ch56 | The Siege | 189 | 6 | 0 |
| ch57 | Okita Sōji | 166 | 5 | 0 |
| ch58 | Assistant Commissioner of the Army | 151 | 6 | 0 |
| ch59 | The Fleet Turns North | 152 | 4 | 0 |
| ch60 | Ichimura Tetsunosuke, the Page | 177 | 2 | 0 |
| ch61 | The Seizure of Matsumae Castle | 176 | 4 | 0 |
| ch62 | The Ironclad | 150 | 5 | 0 |
| ch63 | The Sea Fight at Miyako Bay | 161 | 3 | 0 |
| ch64 | The Attack | 169 | 6 | 0 |
| ch65 | Reunion | 182 | 5 | 0 |
| ch66 | The Imperial Army Lands | 150 | 5 | 0 |
| ch67 | Goryōkaku | 145 | 3 | 0 |
| ch68 | Gunsmoke | 163 | 4 | 0 |
| ch69 | あとがき / Afterword | 25 | 6 | 0 |
| ch70 | 解説 / Commentary (Harada Masato) | 28 | 14 | 0 |
| ch71 | 司馬遼太郎 / About the Author | 1 | 4 | 0 |
| **Total** | **71 units** | **12,228** | **481** | **0** |

## Batching as executed

Fifteen batches, on the approved plan; one conversation each.

- B01 = ch01 (voice gate; ch01 frozen as the register reference). Notes 1–15.
- B02 = ch02–ch07. B03 = ch08–ch13. B04 = ch14–ch18. B05 = ch19–ch23.
- B06 = ch24–ch28. B07 = ch29–ch33. B08 = ch34–ch38. B09 = ch39–ch43.
- B10 = ch44–ch48. B11 = ch49–ch53. B12 = ch54–ch58. B13 = ch59–ch63.
- B14 = ch64–ch68 (the climax and Hijikata's death). Notes to 457.
- **B15 = ch69–ch71 back matter + whole-book reconciliation + this report.**
  Notes 458–481 (24 this batch). No deviation from the approved plan.

## Checks run book-wide, and what they found

1. **Verbatim quotation + parity** — true by construction (`make_bilingual.py`);
   `verify_unit.py` re-checks. All 71 units in parity.
2. **Numeric invariants** — `check_numbers.py --noise data/noise.txt`, every
   unit: 0 unresolved. A reverse invented-precision sweep over all 71 units found
   no fabricated number (its one hit, "Genji 1" for 元治元年, is a false positive).
3. **Entity survival** — `qc_entities.py`: 0 misses book-wide.
4. **Alignment & content/displacement** — `check_align.py` / `check_content.py`
   clean, save the one documented ch52 substring false-flag (近藤勇平 ⊃ 近藤勇),
   which is a checker artifact, not a translation defect.
5. **Register vs frozen ch01** — `check_register.py --ref` within tolerance for
   every unit, back-matter essays included (essay register is exempt from the
   dialogue-contraction expectation).
6. **Tail verification** — each unit's final paragraphs read against the source,
   the back-matter tails included.
7–10. **Once-per-book checks** — blind double translation and back-translation
   sampling done in earlier batches; scholarship verdicts stated in the notes
   (corroborated / uncorroborated / contradicted).
11. **Whole-book reconciliation** (`check_reconcile.py`): epithet-drift heuristic
   returned 33 candidates, all adjudicated as correct on inspection (numeric
   n-gram false positives; context-chosen synonyms such as 小銃弾 "rifle-ball" /
   "rifle-round"; 尊王攘夷 clipped where the source clips). Glossary-forward:
   301/302 decided forms present (the one "unused," 茨木屋 "the Ibarakiya," does
   occur at ch22 — an article-only miss in the exact-string check). Spelling
   locale unified to American (one British "theatre" in a ch34 note corrected;
   final 0 British / 295 American). See `out/term_ledger.md`.

**Reconciliation corrections made this batch (CORRECTIONS.md, GLOBAL):**
- The ch32 and ch68 notes had cited "Shiba's afterword" as the source of the
  statement that Oyuki is invented. On translating the back matter, the afterword
  (ch69) proved to speak only of Hijikata; the explicit statement is in Harada's
  commentary (ch70). Both notes were reworded to cite the commentary; the
  underlying, well-attested fact is unchanged.
- One British "theatre" → "theater" for locale consistency.

## Observed error rate

- Population: 12,228 paragraph pairs. Sample: **489 pairs, 4.0%, fixed seed
  1869**, spread across all 71 units.
- **Errors found: 0.** No fabrication, no omission, no number/date/name error,
  no register break in any sampled paragraph (long single-pass paragraphs read to
  the tail). Adjudicated flags: none.
- **Honest statement:** zero errors in 489 does not prove zero. By the rule of
  three, it bounds the paragraph-level error rate at roughly **3/489 ≈ 0.6%** at
  ~95% confidence — consistent with a rate below ~0.6%, not with zero. Full
  method and figures in `out/deep_audit.md`.

## Findings that need the commissioner's eye

- **None outstanding.** The one substantive historical/interpretive point raised
  in this batch (that the "Oyuki is fiction" authority is Harada's commentary, not
  Shiba's afterword) has been resolved in the notes and logged in CORRECTIONS.md.
- Shiba's deliberate anachronisms are kept as the narrator's, and flagged in the
  notes where a reader might trip: the modern name "Hokkaidō" used before the 1869
  renaming (ch65); the Port Arthur / Russo-Japanese-War forward glance (ch67).

## Residual uncertainties a reader should know about

- **The corrected death date.** Hijikata died Meiji 2/5/11 = **20 June 1869**
  (Gregorian), not 11 June; the lunar-day-as-Gregorian slip is corrected and
  footnoted at ch68. Goryōkaku surrendered Meiji 2/5/18 = 27 June 1869.
- **The Futamataguchi figures** (a sixteen-hour action, 35,000 rounds, one man
  lost) are Shiba's traditional numbers and cannot be checked precisely; the note
  at ch66 says so.
- **Hijikata's death particulars** (exact spot, who fired) are debated among
  historians; Shiba leaves them open and the ch68 note states this.
- **Provisional glossary readings** are marked provisional in the build; no
  damaged-source gaps exist (this is a clean digital source, no OCR).
- **Oyuki is wholly fictional** (Harada's commentary, ch70) — every scene she
  appears in is Shiba's invention, as the notes at ch32, ch37, ch48, ch65, ch68
  now state with the source correctly attributed.

## Reliability map

The novel is historical fiction on a real career; its checkable claims were
fact-checked against scholarship (never LLM-sourced; Grok/Grokipedia ignored),
with verdicts stated in the notes at first appearance. Reliable spine: the
Shinsengumi's founding (1863), the Ikedaya Incident (1864), the Boshin War, the
Ezo campaign, and Hijikata's death at Hakodate (1869) are documented. Reliably
invented: **Oyuki and her whole thread**, and the private interior scenes. This
batch's back matter is the primary evidence for that line — Shiba's afterword on
his method, Harada's commentary naming Oyuki as fiction. Back-matter facts
verified this batch: Shiba = Fukuda Teiichi, b. 1923 Ōsaka, d. 1996; Naoki Prize
1960 for *Fukurō no shiro*; the film postponed from 22 May 2020 to 15 October
2021 (footnoted at ch70).

## Provenance and method

- **Source:** 燃えよ剣（新装版）, Shiba Ryōtarō, Bungeishunjū e-book, 2020-04-20
  (ASIN B086P34MVL). A clean digital EPUB — **no OCR, no scanning**. Ingested with
  `scripts/ingest_epub.py` (Japanese-aware: furigana strip, 8 gaiji substituted
  via `data/gaiji_map.json`, `reference/furigana_readings.tsv` dumped).
- **Pipeline (as run):** ingest → `book.json` structure → per-unit reading files
  (`out/<id>_reading.md`) → `reading_to_en.py` + `make_bilingual.py` (parity by
  construction) → `verify_unit.py` / `check_align.py` / `check_content.py` /
  `qc_entities.py` → apparatus via `apparatus_merge.py` (+ per-batch encoders like
  `build_b15_apparatus.py`) → `build_reading_epub.py` → `qa_epub.py` + epubcheck.
- **Do not revert:** the ingest gaiji map; the `{j}/{v}/{d}/{g}/{p}` markers and
  their build handling; `qc_entities.py` single-kanji skip; the `check_numbers.py`
  hundred/tens/thousand patches; `data/noise.txt` (commented name/idiom rules,
  through B15); the frozen `reference/ch01_ref.md`.
- **Rebuild:** `python3 scripts/build_reading_epub.py && python3
  scripts/qa_epub.py out/burn-o-sword.epub && java -jar
  /tmp/epubcheck-5.1.0/epubcheck.jar out/burn-o-sword.epub`. `data/src/` and
  `data/src_epub/` are gitignored; regenerate with `ingest_epub.py source.epub`
  if empty.

## Definition of done — met

- [x] Complete EPUB with cover and clean TOC (no "pending"), 71/71 units.
- [x] qa_epub PASS; epubcheck 0/0/0/0.
- [x] Per-unit `out/<id>_reading.md` + `out/<id>_en.json` for all 71 units.
- [x] `out/term_ledger.md` rendered (302 rows + by-hand forms + reconciliation).
- [x] `out/deep_audit.md` written (fixed-seed 4% audit, honest error rate).
- [x] Ledgers current: PROGRESS.md, CORRECTIONS.md, this COMPLETION.md.
- [x] One note stream complete (481 notes); no source-note stream needed.
- [x] `authority.json` fed back (301 new terms; one cross-language homograph,
      常州 Changzhou/Hitachi, annotated not "reconciled").
- [x] Final EPUB committed with `git add -f out/burn-o-sword.epub`.
- [x] HANDOFF.md rewritten to COMPLETE.
- [x] All work on branch `claude/burn-o-sword`; stray per-task branch consolidated
      and deleted.
