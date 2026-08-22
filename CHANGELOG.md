# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

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
