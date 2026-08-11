# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

<!-- Newest first. Example:
## 2026-01-01 — corrections batch 1
- GLOBAL: renamed "X" to "Y" everywhere (glossary + grep across ch01-ch12); rebuilt, qa green.
- LOCAL: fixed a dropped clause in ch03 section 2.
-->

## 2026-08-11 — deliverable retitled + final QA pass
- LOCAL: renamed the deliverable to the book's name: out/lu-xiaofeng-1.epub →
  "out/The Golden Roc Dynasty.epub" (book.json `deliverable`; internal EPUB
  metadata already carried the correct title and is unchanged). Content
  verified identical to the previous build entry-by-entry.
- Full QA battery re-run on the renamed file: qa_epub, epubcheck 5.1.0,
  check_structure, check_register, check_apparatus, check_reconcile.
  Results recorded in PROGRESS.md (B08 addendum).
