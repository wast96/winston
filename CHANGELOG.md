# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

<!-- Newest first. Example:
## 2026-01-01 — corrections batch 1
- GLOBAL: renamed "X" to "Y" everywhere (glossary + grep across ch01-ch08); rebuilt, qa green.
- LOCAL: fixed dropped clause at ch03 §2 folio 45.
-->

## 2026-08-12 — Batch 9 (FINAL): back matter, reconciliation, close-out
- AFTERWORD: translated Musashino Jiro's 解説 (printed folios 529-534) as attributed
  back matter via back_matter.json; added render_afterword to the builder (placed
  after the last chapter, before the Notes); every name/title/date crop-verified;
  the six novel quotes reuse the published chapter translations verbatim.
- COVER: extracted the publisher colour cover byte-identical from source.pdf
  (cover.jpg) and set book.json cover_image; the generated cover is no longer used.
- GLOBAL reconciliation (check 12): decided and cascaded Mount Kōya, Osaka, Daitō,
  Sassa Narimasa/Sassa, Kyūshū across all units + notes.json + glossary.json; also
  Hattori Hanzō and Taikō kenchi macron drift, the American spelling locale
  (gray/theater/story/mold), and daimyo/shogun (surfaced by the deep audit). Wrong
  forms folded into data/variants.json; check_reconcile --variants clean.
- LEDGERS: rendered out/term_ledger.md (226 rows); fed this book's decided renderings
  into authority.json (slug the-stealthy-ones).
- DEEP AUDIT (check 10): out/deep_audit.md — ~54 paragraphs read against the scan in
  all 8 chapters (fixed seed), zero mistranslation errors; bound ~5.6% at 95%.
- CLOSE-OUT: COMPLETION.md written; final EPUB committed (git add -f); HANDOFF.md
  rewritten to COMPLETE. qa PASS, apparatus clean, epubcheck 0/0/0/0.
- TOOLING ADDED (do not revert): scripts/render_term_ledger.py; render_afterword in
  scripts/build_reading_epub.py; data/variants.json.
