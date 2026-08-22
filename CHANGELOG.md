# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

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
