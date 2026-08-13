# COMPLETION.md — The Gangs of Old Shanghai (旧上海的帮会)

The book is **COMPLETE**. All 28 units are translated, annotated, and built into a
single cumulative EPUB that passes every gate. Further work is a corrections pass, not
translation.

## Status at a glance

- **28 / 28 units translated** (front matter, 24 memoir/study chapters, two appendices).
- **409 footnotes**; **0 figures** (this is an all-text anthology — no plates or line art
  in the source; recorded as a deliberate empty figure set).
- **Glossary: 920 rows** — people 621, organizations 152, places 90, terms 57.
- **qa_epub: PASS** — 42 files, 35 documents, 28 reading documents, 1,213 paragraphs, 409
  refs / 409 bodies / 409 backlinks all resolve, 22 pagebreak markers matched.
- **epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings / 0 infos** (EPUB 3.3).
- **Deliverable:** `out/gangs-of-old-shanghai.epub`, committed with `git add -f` on branch
  `claude/gangs-of-old-shanghai` (the B10 finalize commit).

## What the finished edition contains

- **Front matter:** typographic cover (no scanned cover in the source), title page
  stating the build is complete, a Principal Characters page (the cast flagged
  `principal` in the glossary), and the translator's note from `book.json`.
- **Body:** the 24 chapters in reading order under their part groupings (Workers'
  Movement; Green Gang and Hongmen Origins; Figures of the Older Generation; Huang
  Jinrong; Du Yuesheng; Zhang Xiaolin and the Three Big Bosses; Gu Zhuxuan), each with
  its contributor byline as a dateline.
- **Appendices:** Appendix I, the Heng Society charter (13 articles in 6 chapters,
  legal-document register); Appendix II, the 1934 member roll, given as a *described*
  appendix — its composition analyzed and a fourteen-entry, image-verified sample
  reproduced, rather than a full romanized transcription of 324 personal names that OCR
  cannot support to this project's standard (see the appendix's own note).
- **Set-off conventions used:** `{d}` datelines for bylines; `***` scene breaks; block
  quotations for classical citations. No `{v}`/`{g}`/`{p}` were needed in this book.
- **Back matter:** deliberately left **inert**. The book carries no errata table, and its
  colophon data (edition, series, registration number, price) is already captured in the
  EPUB metadata via `book.json`'s `source_ref`; `back_matter.json` was therefore not
  enabled. This is a decision, not an omission.
- **Printed-page markers:** `epub:type="pagebreak"` spans and a page-list nav are emitted
  from `data/pagemap/`, so the folio citations in the notes are followable.

## Per-chapter tally

| Unit | Title | Folio | Paras | Notes |
|---|---|---|---|---|
| ch01 | Editorial Note | 1 | 5 | 2 |
| ch02 | Preface | 1 | 8 | 6 |
| ch03 | A Few Notes on the Shanghai Workers' Movement and the Gangs | 1 | 42 | 19 |
| ch04 | Fragmentary Materials on Using Gang Connections in Revolutionary Work | 21 | 18 | 16 |
| ch05 | A Brief Study of the Early Organization of the Green Gang | 29 | 79 | 65 |
| ch06 | The Origins and Evolution of the Green Gang | 51 | 103 | 12 |
| ch07 | A Preliminary Inquiry into the History of the Hongmen | 68 | 54 | 15 |
| ch08 | Shanghai Gang Figures I Have Known | 87 | 76 | 25 |
| ch09 | Zhang Renkui and the Ren Society | 108 | 26 | 15 |
| ch10 | My Teacher Yuan Hanyun | 115 | 29 | 14 |
| ch11 | A Brief Life of My Late Father Xu Langxi | 126 | 16 | 10 |
| ch12 | A Brief Account of Huang Jinrong | 131 | 26 | 15 |
| ch13 | What I Saw as Huang Jinrong's Steward | 138 | 69 | 12 |
| ch14 | The Huang Jinrong I Knew | 167 | 87 | 12 |
| ch15 | On Du Yuesheng | 195 | 211 | 51 |
| ch16 | Reminiscences of the Du Household | 248 | 58 | 17 |
| ch17 | The Du Yuesheng I Knew | 268 | 62 | 11 |
| ch18 | How Du Yuesheng Broke into the Dada Steamship Company | 284 | 23 | 8 |
| ch19 | How Du Yuesheng Became Chairman of the Shanghai Flour Exchange | 293 | 10 | 6 |
| ch20 | Du Yuesheng and the Heng Society | 300 | 54 | 17 |
| ch21 | Du Yuesheng's Ties to Dai Li and the Juntong | 321 | 46 | 20 |
| ch22 | The Life of Zhang Xiaolin | 342 | 18 | 8 |
| ch23 | The Zhang Xiaolin I Knew | 347 | 10 | 6 |
| ch24 | The Collusion and Rivalry of Shanghai's Three Big Bosses | 350 | 20 | 6 |
| ch25 | How Gu Zhuxuan Rose in Zhabei and Opened the Tianchan Stage | 357 | 10 | 7 |
| ch26 | Revolutionary Work Under Gu Zhuxuan's Cover | 360 | 23 | 11 |
| ch27 | Appendix I. Charter of the Heng Society | 367 | 13 | 2 |
| ch28 | Appendix II. Roll of Heng Society Members (1934) | 369 | 17* | 1 |

*ch28 is a described appendix, not paragraph-parallel prose.

## Batching as executed

B01 (ch01–04), B02 (ch05–06), B03 (ch07–08), B04 (ch09–12), B05 (ch13–14), B06a/b (ch15,
split), B07a (ch16), B07b (ch17–18), B08a (ch19), B08b (ch20), B08c (ch21), B09 (ch22–24),
**B10 (ch25–28 + whole-book reconciliation, back matter, cover, term ledger, deep audit,
completion, committed EPUB)**. Batching followed the approved survey; the only deviation
was ch15's mid-chapter split (B06a/b), taken because the chapter is by itself a fifth of
the book.

## Checks run book-wide, and their final result

1. **Numeric invariants** (`check_numbers`, every chapter): clean; `data/noise.txt` carries
   the curated idiom/name exceptions (B10 added `四郊` = "the outskirts").
2. **Parity / anchors / heading shape** (`verify_unit`): clean on every unit; no undeclared
   parity exceptions.
3. **Entity survival** (`qc_entities`): 0 misses on every parallel unit. `方治` was pulled
   from the glossary in B10 because it false-matches inside `地方治安` ("local order").
4. **Alignment and content** (`check_align`, `check_content`): `check_align` within
   tolerance; **`check_content` clean book-wide (exit 0)** after B10 resolved three standing
   displacements — a real name error in ch03 (`吴绍澍` had been rendered "Wu Xingya"; corrected
   to "Wu Shaoshu"), and two rendering variants in ch13 ("Rue Foch" → "Avenue Foch", "Fu
   Xiaoan" → "Fu Xiao'an").
5. **Register vs the frozen ch03 reference** (`check_register`): every B10 unit within
   tolerance.
6. **Tail verification:** the final paragraphs of ch25 and ch26 were read against the scan.
7. **Crop verification:** every proper name, number, and dual-OCR-flagged span in ch25–ch28
   was read from a magnified page crop; the readings are logged in `data/ocr_fixes.json`
   under keys `ch25`–`ch28`.
8. **Blind double translation / round-trip / random-sample audit:** the deep audit below.
9. **Scholarship consistency:** every biographical note in ch25–ch28 states its verdict
   (corroborated / uncorroborated); the Gu Zhuxuan age discrepancy and the two-contributor
   disagreements are footnoted, not reconciled.
10. **Whole-book reconciliation** (`check_reconcile`, exit 0): resolved this session —
    spelling locale cascaded to American (favour→favor, labour→labor, theatre→theater, and
    a stray "Labour" in a note); `爱多亚路` unified to "Avenue Edward VII"; the Yan'an-road
    glosses unified to the "[Name] East/Middle Road" order; `四大家族` unified to "the Four
    Big Families"; `小阿荣` unified to "Little Ah Rong"; `申报` unified to "Shen Bao" across
    prose, glossary, and the shelf ledger. The 154 epithet-drift candidates were read by
    hand and are legitimate hyphen-compound variation (e.g. detective / detective-head).
    "Lin Fanmin" (ch20, `林范民`, a chief auditor) was confirmed a *different person* from
    "Lin Yaomin" (ch21, `林尧民`) — a false alarm, no change.

## Observed error rate

Whole-book random-sample deep audit (`out/deep_audit.md`): population 1,196 parallel
paragraphs, sample **42 (3.5%)**, `random.seed(54)`. **Zero substantive fidelity errors**
(no fabrication, no dropped name or number, no consequential mistranslation) across the
sample, including its hardest name-dense list and long-narrative cases. One minor clarity
observation (ch15's `上海市参议会` → "Shanghai Municipal Council", which context
disambiguates from the Settlement's SMC). Honest bound: zero in 42 places the true rate
below about **7% at 95% confidence** (rule of three), not at zero.

## Findings that need the commissioner's eye

- **ch15 `参议会` → "Shanghai Municipal Council."** Defensible, but shares its English with
  the International Settlement's 工部局. If the commissioner prefers, "Shanghai Municipal
  Assembly" would remove all risk of confusion. Left as printed for now.
- **Two-contributor disagreements are preserved, not fixed:** Gu Zhuxuan's given name
  (Songmao vs Rumao), his gang master (Cao Youshan vs Liu Dengjie), and his rank in the
  Zhabei corps (deputy vs commander) differ between ch25 and ch26; Zhang Xiaolin's
  birthplace differs between ch22 and ch23. Each is footnoted.
- **The 1934 member roll** is described, not fully transcribed — a deliberate fidelity call
  (see below and the appendix note). If a full romanized roster is wanted, it would need a
  dedicated name-by-name crop-verification pass.

## Residual uncertainties a reader should know about

- Provisional romanizations (glossary `status: provisional`) are the translator's readings,
  not found in outside scholarship; they are marked in the build and listed in
  `out/term_ledger.md`.
- The OCR layer is the accuracy floor for rare names. Running-prose names were
  crop-verified; the 324-name member roll was not, and is given as a described appendix
  with a verified sample rather than invented pinyin.
- Damaged-scan or ambiguous readings across the book are flagged in their notes; none were
  silently bridged.

## Provenance and method

- **Source:** *旧上海的帮会* (*上海文史资料选辑* 第五十四辑), Shanghai People's Publishing
  House, August 1986. Image-only PDF, 391 pages, no text layer. Printed-to-PDF offset a
  constant 9 through the body; front matter runs its own short sequences.
- **OCR:** tesseract `chi_sim`, crop `--left 0.06 --right 0.91 --top 0.09 --bottom 0.89
  --psm 6`, folio at the foot; second read via `ocr_dual.py` (PaddleOCR unavailable). zh
  files hand-corrected against the OCR to match the English 1:1 (geometric indent detection
  bypassed for this book).
- **Do-not-revert tooling:** the `check_numbers.py` million/billion patch (B08c); the
  `data/noise.txt` ordering (the `万千` rule must precede the bare-`万` rule) and its
  accumulated blocks through `四郊`; the CLAUDE.md operating-guardrails section.
- **Rebuild from a clean checkout:**
  `./setup.sh` → regenerate OCR for any needed pages → `python3 scripts/build_reading_epub.py`
  → `python3 scripts/qa_epub.py out/gangs-of-old-shanghai.epub` →
  `java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/gangs-of-old-shanghai.epub`.
  `work/content_cfg.json` is gitignored; regenerate it over every unit with both a reading
  and a zh file before running `check_content`.

## Definition of done — met

- [x] EPUB: front matter + all 28 units, full clean hyperlinked TOC, typographic cover,
      no figures (honest empty set), 409 footnotes at reader-model density, glossary and
      translator's note current, qa_epub PASS across the whole spine, epubcheck clean.
- [x] `out/<id>_reading.md` for every unit (the correction surface).
- [x] `out/term_ledger.md` rendered (920 rows); `out/deep_audit.md` written (3.5% sample).
- [x] `notes.json`, `glossary.json`, `figures.json`, `book.json` current.
- [x] `authority.json` fed this book's decided renderings (slug `gangs-of-old-shanghai`).
- [x] `COMPLETION.md` written from the template; `PROGRESS.md` and `HANDOFF.md` updated,
      HANDOFF rewritten to COMPLETE.
- [x] Final EPUB committed with `git add -f out/gangs-of-old-shanghai.epub`.
