# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

<!-- Newest first. Example:
## 2026-01-01 — corrections batch 1
- GLOBAL: renamed "X" to "Y" everywhere (glossary + grep across ch01-ch08); rebuilt, qa green.
- LOCAL: fixed dropped clause at ch03 §2 folio 45.
-->

## 2026-08-31 — Batch 9 (final): ch18–20 + whole-book close-out
- Added ch18 "Fruits of Defeat", ch19 "The Rise and Fall of 'Soviet China'", ch20 "The New 'National United Front'": 195 author + 46 editorial notes (incl. a first-appearance ch02 "mow" note); 16 glossary rows; +1 book-wide fix (`</i>`+word lost-space in 8 earlier author notes).
- CLOSE-OUT: linked back-matter Index (parse_index.py → data/index.json → render_index; 501 entries, all folio refs hyperlinked); authority.json fed this book's 144 renderings; out/term_ledger.md and out/deep_audit.md rendered; COMPLETION.md written; final EPUB committed with `git add -f`.
- The book is COMPLETE. qa_epub PASS, epubcheck clean, check_fidelity/check_apparatus green.
