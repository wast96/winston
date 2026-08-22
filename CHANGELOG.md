# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

<!-- Newest first. Example:
## 2026-01-01 — corrections batch 1
- GLOBAL: renamed "X" to "Y" everywhere (glossary + grep across ch01-ch08); rebuilt, qa green.
- LOCAL: fixed dropped clause at ch03 §2 folio 45.
-->

## 2026-08-22 — Footnote densification pass (commissioner request)
- GLOBAL: greatly increased footnote density across the whole book at the
  commissioner's request, explaining the "little references" a Western lay
  reader would miss (people, places, events, institutions, offices, terms,
  idioms) that earlier passes left unglossed. Notes total 432 -> 657 (+225),
  all fact-checked against Wikipedia / Baidu Baike / academic sources (never
  AI-generated references, per rule 5), verbatim-anchored, XHTML numeric
  entities only. Per-unit: ch00 4->10, ch01 73->100, ch02 130->157, ch03
  62->90, ch04 75->142, ch05 47->76, ch06 24->47, ch07 6->10, ch08 6->10,
  ch09 2->7, ch10 1->3, ch11 2->5.
- FIX (silent-loss guard): the previously note-less sections 4-5 of chapter 2
  had a stale duplicate reading file (out/ch02s45_reading.md) that the builder
  never reads (chapter 2's full text lives in out/ch02_reading.md). Six new
  notes first keyed to the phantom "ch02s45" unit were re-keyed to "ch02" so
  they actually render; the phantom key was removed from notes.json. All six
  anchors verified unique in ch02_reading.md within the sections 4-5 region.
- FIX: one Chen Geng note used the traditional glyph for geng; corrected to the
  simplified form to match the book's script.
- DEDUP: 26 cross-unit duplicate-subject notes removed, keeping each subject at
  its first appearance in reading order (recurring subjects noted once).
- TOOLING (do not revert): scripts/validate_new_notes.py (pre-merge anchor +
  entity check) and scripts/find_note_dups.py (cross-unit duplicate detector
  keyed on shared hanzi).
- Rebuilt; check_apparatus 0/0, qa_epub PASS (657 refs/bodies/backlinks),
  epubcheck 0 fatals / 0 errors / 0 warnings. EPUB ~12.2 MiB.

## 2026-08-21 — Batch 10: Afterword + whole-book close (book COMPLETE)
- NEW: ch11 Afterword translated (PDF 241-242); 11 paras, 2 notes, 13 glossary rows.
- GLOBAL FIX: 霞飞路 rendered "Route Joffre" corrected to the shelf-agreed,
  historically correct "Avenue Joffre" (glossary + ch02 prose x2 + the ch02 note
  anchor and body); reconciled against authority.json across the shelf.
- FIGURE RECOVERY: restored 15 Chapter 2 figures (sections 1-3) silently wiped at
  B03 by apparatus_merge's wholesale per-unit figure replace; recovered crops and
  original alt/captions from the B02 commit. Book figures 63 -> 78; ch02 5 -> 20.
- authority.json fed this book's decided renderings (chen-yangshan on 45 entries;
  巡捕房 variant registered; 中原/Nakahara homograph kept separate).
- Notes: +1 at ch06 (Xiao Shouhuang/Xiao Taihuang source variant), +1 at ch08
  (1988 letter cross-reference to Chapter 3). Book-wide notes now 432.
- Rendered out/term_ledger.md (731 referents, 52 provisional) and out/deep_audit.md
  (44-paragraph random sample, seed 424242, zero substantive errors hand-read).
- Wrote COMPLETION.md; rewrote HANDOFF.md to COMPLETE. Rebuilt: 12 of 12,
  qa_epub PASS, epubcheck 0/0/0. Final EPUB committed with git add -f.
