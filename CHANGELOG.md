# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

## 2026-08-22 — R4 register pass: tic sweep, back batch (ch18–ch22)
Tier-B tic sweep of the back batch (ch18–ch22), including the spine test on
ch19's five and ch21's two flagged long sentences. Reading text edited via
edits/<id>_edits.md + apply_edits.py; content frozen (no para merged/split, no
fact/number/name/date/hedge changed, no quoted material touched).
- **19 English-surface edits** across ch18(4)/ch19(6)/ch20(4)/ch21(5)/ch22(0):
  trailing 此外/并且/又/还/还有 "besides" → "also"/"as well"; 除…外 "besides X"
  → "apart from X"; 先后 "one after another" → "in succession" (people) and
  接连 reordered for rhythm; 只好 "could only" → "had no choice but to"; 便
  "thereupon" → "then"; 后来 "At length" → "Later"; inverted antique "let slip
  no chance" → "missed no chance"; de-nominalized "the teaching of the …";
  **one calibrated-ruling-1 de-inversion** (ch19 L79 fronted-infinitive subject);
  **one spine split** (ch21 L201 run-on cut at the hall).
- **ch22 came back clean** (0 edits): a testimony-saturated chapter (the prison
  hypnotism memoir, the Shen Bao report, Shen Zui's assassination account, the
  Organization Department statement) — every tic is KEEP-listed. ch20 likewise
  KEPT every in-quote litotes/could-only/besides (Chen Yangshan / Bao Junfu /
  Chen Geng's reply letter).
- Long-sentence spine test: only ch21 L201 split; all others pass (single-spine
  biographies, colon-plus-list measure enumerations, rhetorical how-lists that
  keep the author's heat, semicolon-balanced deliberations, quoted documents).
- KEEP-list guard caught and left three in-quote hits: "could only work hard to
  repay" (ch18, Zhang Shenchuan memoir), "Presently Chiang Kai-shek came" (ch19,
  Cai Mengjian testimony), "could only make contact by telephone" (ch20, Chen
  Yangshan testimony).
- ch21's 18 等-tags ("and the rest"/"and the others") LEFT as genuine
  varying-membership truncations; the mild arrestee-group alternation is flagged
  for R5's whole-book check_reconcile.py (the plan's place for it).
- Pre-flight: regenerated data/zh for ch18–ch22 from data/txt_backup_b1* via the
  b1N_rebuild.sh drivers; all five verify_unit green before any edit.
- Files touched: out/ch18,ch19,ch20,ch21_reading.md;
  edits/ch18,ch19,ch20,ch21,ch22_edits.md; PROGRESS.md; rebuilt
  out/zhou-enlai.epub. notes.json unchanged (339; no anchor moved).
- verify_unit green on all five; check_register within tolerance vs
  ch01_reading.pre-R.md (em-dash 1.00×); typography guard clean (0 curly quotes,
  0 new ellipses); qa_epub PASS; **epubcheck 5.1.0: 0 errors, 0 warnings.**

## 2026-08-22 — R3 register pass: tic sweep, middle batch (ch09–ch14, ch16, ch17)
Tier-B tic sweep of ch09–ch14 and ch17, plus the FULL aligned zh-en read of
ch16. Reading text edited via edits/<id>_edits.md + apply_edits.py; content
frozen (no para merged/split, no facts/numbers/names/hedges changed).
- **18 English-surface edits** across ch09(5)/ch11(4)/ch13(1)/ch14(5)/ch16(2)/
  ch17(1): litotes 不少/不小 ("no few/no little" -> "a good many / quite a few /
  a good deal of"); 除...外 "besides" -> "apart from"; trailing 并/还 "besides"
  -> "as well"; 纷纷 -> "each" (distributive) and 相继 -> "in succession"; the
  ch11 martyr-group 等-list drift collapsed to "and the others"; two narration
  ellipses cut per STYLE ruling 8 (ch14); 只得 -> "had no choice but to" (ch16).
- **ch16 got the full aligned read** (42 paras, 2 edits): it is largely
  operational, not elevated-antique like ch15, so it correctly yields few
  register edits — no padding to a number.
- **ch10 & ch12 came back clean** (0 edits): quoted memoirs/letters/dialogue and
  meaningful "and the others"/"and the rest" distinctions, respected per KEEP.
- Long-sentence spine test on the >90-word narration sentences: no split (single-
  spine colon-lists, em-dash action beats, or splitter artifacts across in-quote
  periods).
- KEEP-list guard caught two mechanical over-corrections and left them: "let
  slip not a moment" (ch11, Zhou Enlai's quoted essay) and "whereupon" (ch12,
  quoted newspaper).
- Files touched: out/ch09,ch11,ch13,ch14,ch16,ch17_reading.md;
  edits/ch09,ch11,ch13,ch14,ch16,ch17_edits.md; rebuilt out/zhou-enlai.epub.
  notes.json unchanged (339; no anchor moved).
- verify_unit green (ch16 shows only its pinned pair-2 zh artifact);
  check_register within tolerance vs ch01_reading.pre-R.md; typography guard
  clean (zero new smart punct); spot-audit of all 18 sites vs source = zero
  meaning drift.
- Build 28/28, 339 notes; qa_epub PASS; **epubcheck 5.1.0: 0 errors, 0 warnings.**
- Noted for R5 (book-wide diction ledger, not fixed piecemeal): 破坏 ->
  "wrecking" (ledger: sabotage) and 镇压/除掉 -> soft "put down"/"did away with"
  (killing-verb ledger: eliminate/kill); these need a whole-book cascade.

## 2026-08-22 — R2 register pass: tic sweep, front batch (ch00–ch08)
Tier-B tic sweep of the front chapters. Reading text edited via
edits/<id>_edits.md + apply_edits.py; content frozen (no para merged/split,
no facts/numbers/names/hedges changed).
- **11 English-surface edits** across ch01(2)/ch02(1)/ch04(1)/ch06(6)/ch07(1):
  相继/陆续/先后 "one after another" calques, 不少/不小 litotes ("no little/no
  small" -> "a good deal of/considerable/sizable"), trailing/appositive
  "besides" (-> "also/as well/other"), 不得不 "could not but" -> "had to".
- **ch00/ch03/ch05/ch08 came back clean** (0 edits): quoted memoirs and
  idioms, respected per the KEEP list. ch08's whole body is Zhao Weigang's
  memoir; all its tic hits are KEEP-list.
- Long-sentence spine test on the >90-word narration sentences: no split (all
  single-spine list/cumulative constructions).
- Files touched: out/ch01_reading.md, out/ch02_reading.md, out/ch04_reading.md,
  out/ch06_reading.md, out/ch07_reading.md; edits/ch0{1,2,4,6,7}_edits.md;
  rebuilt out/zhou-enlai.epub. notes.json unchanged (339; no anchor moved).
- verify_unit matches §2 pins; check_register within tolerance vs
  ch01_reading.pre-R.md; typography guard clean (zero new smart punct);
  spot-audit of all 11 sites vs source = zero meaning drift.
- Build 28/28, 339 notes; qa_epub PASS. epubcheck not available in this
  container (fetch network-restricted); qa_epub is the gate.

## 2026-08-22 — R1 register pass: Tier A globals + ch15 exemplar
Reading text edited via edits/<id>_edits.md + apply_edits.py; Politburo via a
global cascade (CLAUDE.md). Content frozen (no para merged/split, no facts or
hedges changed).
- **Dates:** 95 day-month dates -> month-day (ch00-ch05, ch09-ch12). Cascaded
  to 5 note anchors (ch00, ch02 x3, ch12) and 3 figures.json `before` anchors
  (ch01, ch02, ch11).
- **Politburo:** 政治局/中央政治局 -> "the Politburo" book-wide (51 reading + 3
  note bodies); recorded in glossary.json and authority.json.
- **Ledger residuals:** "in good time" -> "in time/promptly" (14 narration
  sites); ch07 "driving into the heart of the enemy" -> "planted inside..."
  (打入). Three quoted "in good time" in ch15 kept (quoted testimony).
- **ch15 exemplar:** 12 narration edits (litotes calques, trailing "besides",
  "given to startling acts", "in his lifetime", 只好, a calqued "one after
  another"); quoted material untouched; the R2-R5 calibration target.
- Build 28/28, 339 notes, 496 pagebreaks; qa_epub PASS; epubcheck 5.1.0 clean;
  10% spot-audit (15 paras) vs source: zero meaning drift.

## 2026-08-22 — R1 pre-flight: data/zh regeneration + recovery tooling (no reading text changed)
- Regenerated `data/zh/` for all 28 units; verify_unit GREEN on 26/28.
- TOOLING (do not revert): added `scripts/recovery/b01_surgery.py` (ch00
  Preface: assemble range 36-38, strip furniture + 2 boundary repairs -> 6
  paras, GREEN); patched `scripts/recovery/b02_surgery.py` to skip-and-warn on
  a missing OCR anchor instead of a fatal SystemExit (ch02 -> 40/40 GREEN
  under tesseract 5.3.4).
- Documented in `scripts/recovery/README.md` the B01 recipe and the two
  parity limits (ch01, ch03) this container's tesseract 5.3.4 cannot
  reproduce; pinned the known-benign warnings in `REVISION_PLAN.md` section 2.
- Snapshotted `out/ch01_reading.pre-R.md` as the frozen register reference.

## 2026-08-22 — revision pass planned (no text changed)
- Added `REVISION_PLAN.md` from the template: five batches (R1 foundation +
  globals + ch15 exemplar; R2-R4 tic sweeps front/middle/back; R5 tail +
  reconciliation + close), filled with live examples, KEEP list, and verbatim
  kickoffs for every batch.
- `HANDOFF.md` again carries a paste-ready kickoff (R1) as its first section;
  the completion notice stands below it.
- Still no reading text, apparatus, or EPUB content modified.

## 2026-08-22 — register-pass assessment (no text changed)
- Added `review/REGISTER_PASS_ASSESSMENT.md`: a measured survey of the built
  book against the register rebaseline and style machinery on
  `claude/the-sword-roars` (commit 8431573), with a ranked defect inventory,
  prose quality score, and a recommendation for a bounded tic-sweep pass.
- TOOLING: imported `scripts/register_tics.sh` (the sword branch's grep
  battery for the rebaseline kill list; runs against this repo unmodified).
- No reading text, apparatus, or EPUB content was modified.

<!-- Newest first. Example:
## 2026-01-01 — corrections batch 1
- GLOBAL: renamed "X" to "Y" everywhere (glossary + grep across ch01-ch08); rebuilt, qa green.
- LOCAL: fixed dropped clause at ch03 §2 folio 45.
-->

## 2026-08-22 — B14 (final batch) + book completion
- Translated ch25 (Wu Hao Notice), ch26 (Conclusion), ch27 (Afterword); book now 28/28 complete.
- GLOBAL: spelling locale standardized to American across all units (out/ch10 grey->gray; out/ch13, out/ch14 travelled->traveled; notes.json theatre->theater). Proper-noun "Theatre" venue names kept.
- GLOSSARY: added B14 rows (people/places/works); removed 斗争 (works; false-matched "struggle") and 罗斯 (substring of 俄罗斯).
- Ledgers: authority.json fed with decided renderings (slug zhou-enlai); out/term_ledger.md and out/deep_audit.md written; COMPLETION.md written; HANDOFF.md -> COMPLETE.
- Rebuilt: qa_epub PASS, epubcheck 0/0/0. EPUB committed with git add -f.
