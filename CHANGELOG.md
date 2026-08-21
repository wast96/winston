# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

<!-- Newest first. Example:
## 2026-01-01 — corrections batch 1
- GLOBAL: renamed "X" to "Y" everywhere (glossary + grep across ch01-ch08); rebuilt, qa green.
- LOCAL: fixed dropped clause at ch03 §2 folio 45.
-->

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
