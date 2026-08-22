# COMPLETION.md — Nameless Heroes (英雄无名), whole-book completion report

Written on the final batch (B36) in place of another handoff. This is the
document to read to know what the finished edition contains and how far to
trust it.

## Status at a glance

- **43 of 43 units translated.** All prefaces, introductions, narrative
  chapters, and the Afterword are done; the pending-aware TOC is clean (no
  placeholder), the coverage is complete.
- **375 translator notes**, 0 source notes (the source carries none of its own).
- **0 in-text figures.** The source holds a single image, its cover, reused
  byte-identical; there are no interior figures to place.
- **Glossary: 708 rows** — people 479, organizations 71, places 132, terms 26.
- **qa_epub: PASS** — 57 files, 50 documents, 375 note references / 375 bodies /
  375 backlinks, all links resolve.
- **epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings / 0 infos** (EPUB 3.3).
- **Deliverable:** `out/nameless-heroes.epub`, committed with `git add -f` on
  branch `claude/nameless-heroes` (the completion commit that carries this file).

## What the finished edition contains

- **Front matter:** cover (source image, byte-identical); title page; a cast /
  Principal Characters page generated from the `principal` glossary flags; the
  four collected prefaces and introductions (ch01–ch04).
- **Four Parts:** Part One *Rooting Out Traitors in the North* (ch05–ch09);
  Part Two *Disgrace at Hanoi* (ch10–ch19); Part Three *Renown Won in a Hundred
  Battles* (ch20–ch31); Part Four *Pacification of the Beiping–Tianjin Region*
  (ch32–ch42); and the **Afterword** (ch43).
- **Back matter:** Translator's Note (the project note from book.json, verbatim)
  and Glossary of Names and Terms; the Notes page (popup footnotes with
  `epub:type` noteref/footnote semantics).
- **Set-off conventions used:** scene-break rules (`***`); dateline / hour-gloss
  / verse markers where the source encoded them; long contributed accounts set
  without an outer quote layer (double quotes reserved for the account's own
  inner speech) to avoid unreadable nested guillemets.
- **Deliberately NOT invented:** `back_matter.json` carries no colophon notice,
  so none is rendered (the book has no errata slot to fill); no source-notes
  stream exists because the source has no notes of its own; no reliability-map
  file was written as a separate artifact (the per-claim verdicts live in the
  notes, as CLAUDE.md's scholarship-consistency contract requires).

## Per-chapter tally

| Unit | Ch | Title (short) | Paras | Notes |
|---|---|---|---|---|
| _Prefaces and Introductions_ | | | | |
| ch01 | 1 | Foreword: The Conception of Nameless Heroes | 8 | 6 |
| ch02 | 2 | Introduction to Rooting Out Traitors in the North | 18 | 20 |
| ch03 | 3 | Introduction to Disgrace at Hanoi | 14 | 9 |
| ch04 | 4 | Introduction to Renown Won in a Hundred Battles | 61 | 24 |
| _Part One. Rooting Out Traitors in the North_ | | | | |
| ch05 | 5 | Prefatory Note | 8 | 8 |
| ch06 | 6 | §1. A Heavy Charge, Pressing Onward | 322 | 24 |
| ch07 | 7 | §2. A Startling Debut | 362 | 11 |
| ch08 | 8 | §3. Tangled Roots, a Substitute Sacrifice | 461 | 13 |
| ch09 | 9 | §4. Impatience Breeds a Grave Blunder | 332 | 9 |
| _Part Two. Disgrace at Hanoi_ | | | | |
| ch10 | 10 | Author's Preface: The Full Story of the Wang Case | 26 | 4 |
| ch11 | 11 | Ch.1. Bloodshed Against the Enemy | 87 | 10 |
| ch12 | 12 | Ch.2. Unfathomable Hearts, Hidden Designs | 131 | 16 |
| ch13 | 13 | Ch.3. Treacherous Tides, a Gathering Storm | 262 | 21 |
| ch14 | 14 | Ch.4. Beset on Three Sides, Ever Forward | 5 | 0 |
| ch15 | 15 | Ch.5. A Blow at Bolang, the Wrong Carriage | 225 | 11 |
| ch16 | 16 | Ch.6. Vile Treachery, Illusions Undone | 116 | 8 |
| ch17 | 17 | Ch.7. Treading Thin Ice, Never Relenting | 147 | 9 |
| ch18 | 18 | Ch.8. Renewed Effort, Wave upon Wave | 138 | 6 |
| ch19 | 19 | A Note from the Author | 4 | 0 |
| _Part Three. Renown Won in a Hundred Battles_ | | | | |
| ch20 | 20 | Author's Preface: Shanghai Behind-the-Lines | 26 | 2 |
| ch21 | 21 | Ch.1. Back in Shanghai, Our Might Restored | 155 | 8 |
| ch22 | 22 | Ch.2. Spring Clouds Unfurl, the First Thrust | 286 | 7 |
| ch23 | 23 | Ch.3. Patriotic Spirit, Moral Bounds | 7 | 1 |
| ch24 | 24 | Ch.4. Beset on Three Sides, Ever Forward | 161 | 6 |
| ch25 | 25 | Ch.5. A Full Reckoning: Remarkable People | 183 | 10 |
| ch26 | 26 | Ch.6. Mount Tai or a Feather, All on One Throw | 321 | 11 |
| ch27 | 27 | Ch.8. The Death of a Tycoon (ch.7 skipped in source) | 133 | 6 |
| ch28 | 28 | Ch.9. Fearsome Renown, Waves of Blood | 217 | 8 |
| ch29 | 29 | Ch.10 (上). Troubles Never Come Singly | 70 | 9 |
| ch30 | 30 | Ch.10 (下). Troubles Never Come Singly | 108 | 5 |
| ch31 | 31 | Written Before the Third Volume Went to Press | 14 | 3 |
| _Part Four. Pacification of the Beiping–Tianjin Region_ | | | | |
| ch32 | 32 | Author's Preface | 35 | 10 |
| ch33 | 33 | Ch.1. Reviving the Ailing, a Second Start | 151 | 6 |
| ch34 | 34 | Ch.2. Self-Starting, of One Heart and Mind | 127 | 3 |
| ch35 | 35 | Ch.3. A Spell of Storm, a Few Fallen Leaves | 194 | 8 |
| ch36 | 36 | Ch.4. Seizing the Initiative, Spread Toils | 187 | 8 |
| ch37 | 37 | Ch.5. War Unending, the People Destitute | 144 | 8 |
| ch38 | 38 | Ch.6. Right and Wrong Made Plain | 135 | 8 |
| ch39 | 39 | Ch.7. Looking Before and After | 179 | 8 |
| ch40 | 40 | Ch.8. Musing on Past and Present | 169 | 9 |
| ch41 | 41 | Ch.9. Reflecting on Past Pain | 200 | 9 |
| ch42 | 42 | Ch.10. Fallen Leaves Return to the Root | 200 | 10 |
| _Afterword_ | | | | |
| ch43 | 43 | Afterword: Closing Remarks | 31 | 3 |
| **Total** | | **43 units** | **6,160** | **375** |

## Batching as executed

Run in 36 working batches (one conversation each), against a book.json batch
array that lumps ch23+ch24, so the working labels run one ahead of the array
from ch24 on. B01 = front matter + ch01–ch05 (the voice gate; the B01 front
matter is the frozen register reference, `reference/B01_frozen.md`). B02–B05 =
ch06–ch09 (Part One). B06–B13 = ch10–ch19 (Part Two). B14–B24 = ch20–ch31
(Part Three). B25 = ch32; B26–B35 = ch33–ch42 (Part Four). B36 = ch43 (the
Afterword) + whole-book completion. No deviation from the approved outline; the
source's own chapter-numbering gaps (Part Three skips ch.7; ch.10 splits into
上/下) are preserved and footnoted, not silently regularized.

## Checks run book-wide, and what they found

1. **Verbatim quotation + parity** — by construction via `make_bilingual`/
   `batch_artifacts`; `verify_unit`/`check_structure` re-check. Parity
   6,160/6,160, all units OK.
2. **Numeric invariants** — `check_numbers` with the project noise rules:
   0 unresolved book-wide. Republican years render literally and match the
   source numeral (or +1911).
3. **Entity survival** — `qc_entities`: 0 misses on the final units; keyed
   terms align to their glossary renderings (e.g. 绥靖 → the noun "pacification",
   never the verb).
4. **Alignment / content displacement** — `check_align` (every unit within
   2.2× of its median ratio) and `check_content`. The only displacements are the
   **documented false positives**, all homograph or keyed-substring artifacts,
   not real misplacements: ch08 Shunde ×3, ch09 "Jize County" ×1, ch13 ×9,
   ch26 武汉卿/劳勃生路 ×2, ch38 海防/Haiphong ×1, ch41 河内/Hanoi ×1 (河内 = the
   substring of 护城河内墙, "the moat's inner wall"). ch43 itself: 0 displaced.
5. **Register vs the frozen reference** — `check_register --ref`: within
   tolerance for every unit, including the reflective Afterword (Chen's
   narrating "shall" is deliberate and left intact).
6. **Tail verification** — each unit's final paragraphs read against the source;
   ch43's closing paragraphs (the book's last words) verified explicitly.
7–10. **Bounded once-per-book checks** — blind double translation and
   round-trip back-translation used for calibration on representative/resistant
   passages; scholarship verdicts carried *in* the notes (corroborated /
   uncorroborated / contradicted), contested claims left faithful and footnoted.
11. **Whole-book reconciliation** (`check_reconcile` + hand):
   - **Spelling locale unified to American.** The book was mixed (736 American
     vs 38 British across curated pairs); the decided policy is a single
     American locale, cascaded across prose, note bodies, and glossary bodies
     (theatre→theater, honour→honor, colour→color, centre→center, metre→meter,
     defence→defense, grey→gray, organise→organize, practise→practice,
     marvellous→marvelous, favour→favor, labour→labor, neighbour→neighbor —
     26 tokens). Proper-noun safety was verified first (no Labour Party, no
     surname Grey, no proper Centre/Honour). Re-check: **0 British / 774
     American.**
   - **张垣 / 张家口 reconciled.** Both are the same city (Kalgan). The source
     uses both names; the translation now renders 张垣 → **Zhangyuan** and
     张家口 → **Zhangjiakou** uniformly (the lone ch08 张垣, previously collapsed
     to "Zhangjiakou", was aligned to "Zhangyuan"), with a first-appearance note
     at ch08 introducing the city and both of its names. 张垣 → Zhangyuan is now
     keyed; check_content shows no new displacement.
   - **Grep-count of ~20 decided renderings** confirmed consistent single
     renderings and first-appearance notes: the Juntong (72, first ch04, noted),
     the Baomiju (2, introduced in the ch04 note), Dai Li (33, noted ch02),
     sanction/制裁 (defined in the ch04 note — see the residuals section),
     Pacification Corps (75, ch32), Wang Jingwei (195, noted ch03), the Three
     Principles of the People (25, noted ch05), Whampoa (18, noted ch05),
     Biographical Literature (9, noted ch18), Zhangyuan/Zhangjiakou (ch08),
     and the Part-Four command vocabulary.
   - **`authority.json` fed back:** this book's decided/attested renderings were
     merged under the slug `nameless-heroes` (399 new cross-book terms, 43
     agreements with prior books, 1 flagged disagreement — see residuals).

## Observed error rate

See `out/deep_audit.md`. Population 6,160 paragraphs; fixed-seed sample of 45
pairs (seed 43), read against the source for omission / fabrication / invented
precision / mistranslation / displacement. Result: **44 of 45 fully faithful;
zero substantive errors.** The one flag was a title nuance (ch07 何部长（军分会
代委员长）rendered "acting **deputy** chairman" for 代委员长 = *acting chairman*),
corrected in this batch. Zero substantive errors in 45 bounds the true rate
below roughly **6–7%** at 95% confidence — not zero. This sits on top of the
whole-population scripted coverage above.

## Findings that need the commissioner's eye

- **宋子文 → "Song Ziwen" (pinyin), where the shelf's other books use "T. V.
  Soong."** One occurrence (ch11); the glossary note already bridges to "T. V.
  Soong." Left as pinyin (the book's house rule is pinyin-except-conventional);
  `authority.json` flags it `reconcile` honestly. A commissioner who wants the
  conventional form shelf-wide can request the one-word change.
- **制裁/sanction first appears in ch02 but is formally defined in the ch04
  note.** The ch02 uses ("target of sanction", "work of sanction") are
  transparent from context (the killing sense is plain); the etymological note
  (制裁 = the service's euphemism) lands two short chapters later. Left as
  shipped rather than reopen two voice-gated front-matter chapters; flagged here
  for awareness.

## Residual uncertainties a reader should know about

- **Provisional romanizations still to firm up** (flagged `provisional` in the
  glossary and marked in the build): 241 people, 19 places, 5 organizations.
  These are best-effort pinyin for names not found attested in English-language
  scholarship; among them the Kanjurwa Khutukhtu's brother, several Japanese and
  Mongol readings, and people-names introduced only once. Listed by category at
  the end of `out/term_ledger.md`.
- **Documented false positives** (not errors): the homograph and keyed-substring
  displacements listed under check 4 above; the ch32 "Fifth Part" self-numbering
  (the Beiping–Tianjin volume calls itself the Fifth Part though Shanghai was the
  Third — preserved and footnoted); the garbled deputy-chief-of-staff surname
  glyph (ch36); name-form variants (杜心吾/杜心五, 程艳秋/程砚秋, the 鲁英庆 glitches
  in ch39) — all read to plain sense and, where a real reading uncertainty, noted.
- **Digitization glitches** are pervasive in the source (single-character
  substitutions, dropped stops, mismatched guillemets, redaction glyphs); each
  is read to plain sense and listed per batch in PROGRESS.md; only genuine
  reading uncertainty is footnoted, never a mechanical typo.

## Provenance and method

- **Source:** a clean digital EPUB (no OCR, no scanning) of the collected
  *Nameless Heroes* (英雄无名) by Chen Gongshu (陈恭澍), a Nationalist/Juntong
  secret-service memoir; 45 spine documents, 43 modeled as chapters (cover →
  cover image; source nav → superseded by the generated TOC). Every content file
  opens with the running-header line 英雄无名-陈恭澍, dropped at translation time
  (drop count variable: most drop=2; ch01/ch10/ch20/ch32 drop=3).
- **Pipeline as run:** `ingest_epub` → `clean_batch` (per-unit drop/merge/
  heading specs with a source-conservation check) → translate to the frozen
  register → `batch_artifacts` (derives `out/<id>_en.json` from the authored
  `out/<id>_reading.md`; always finish with a no-arg run) → `verify_unit`,
  `check_align`, `check_structure`, `check_content`, `qc_entities`,
  `check_register` → apparatus via `apparatus_merge` (numeric character
  references in note bodies; anchors verbatim ASCII) and glossary rows added by
  hand into the sectioned `glossary.json` → `build_reading_epub` → `qa_epub` +
  epubcheck.
- **Builder features that must not be reverted:** the pending-aware TOC and
  coverage; the source cover reused byte-identical (EPUB3 + legacy declarations);
  the popup-note semantics; refuse-on-unmatched-anchor for the note stream; the
  render-layer typography (straight quotes → curly; sources stay plain); the
  by-hand sectioned glossary (apparatus_merge's glossary path assumes a flat map
  and would corrupt it — notes still go through apparatus_merge).
- **Rebuild from a clean checkout:**
  `./setup.sh` (its one failing regression test, "hook stands down on template
  stub", is a known false alarm) → `python3 scripts/ingest_epub.py source.epub`
  → `python3 scripts/clean_batch.py` → `python3 scripts/batch_artifacts.py` →
  `python3 scripts/build_reading_epub.py` → `python3 scripts/qa_epub.py` →
  `java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/nameless-heroes.epub`.

## Definition of done — met

- [x] Complete EPUB with cover and clean TOC (43/43), committed with `git add -f
      out/nameless-heroes.epub`.
- [x] `qa_epub` PASS; epubcheck 0/0/0/0.
- [x] Per-unit `out/<id>_reading.md` + `out/<id>_en.json` for all 43 units.
- [x] `out/term_ledger.md` written; `out/deep_audit.md` written (fixed-seed
      sample, honest error-rate statement).
- [x] Both note streams complete (375 translator notes; 0 source notes, none in
      the source).
- [x] `authority.json` fed back under slug `nameless-heroes`.
- [x] Whole-book reconciliation run and applied (spelling locale; Zhangyuan/
      Zhangjiakou).
- [x] `PROGRESS.md` maintained; `HANDOFF.md` rewritten to COMPLETE.
