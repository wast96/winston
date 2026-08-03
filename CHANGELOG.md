# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

<!-- Newest first. Example:
## 2026-01-01 — corrections batch 1
- GLOBAL: renamed "X" to "Y" everywhere (glossary + grep across ch01-ch12); rebuilt, qa green.
- LOCAL: fixed a dropped clause in ch03 section 2.
-->

## 2026-08-03 — EPUB opens cleanly in Apple Books (metadata fix)
- GLOBAL: the book's dc:identifier was declared urn:uuid: but was not a valid UUID
  (tail segment "ziye-maodun-midnight" is not hexadecimal), which epubcheck flagged
  and which made Apple Books fail to open/import the file. Replaced book.json "uid"
  with a valid, deterministic UUIDv5 (urn:uuid:0b0de36a-c123-573a-a5eb-772845816949),
  stable across every rebuild so Apple treats rebuilds as the same book. Rebuilt
  out/Midnight.epub; epubcheck 5.1.0 now reports 0 errors / 0 warnings; qa green.
