# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

<!-- Newest first. Example:
## 2026-01-01 — corrections batch 1
- GLOBAL: renamed "X" to "Y" everywhere (glossary + grep across ch01-ch08); rebuilt, qa green.
- LOCAL: fixed dropped clause at ch03 §2 folio 45.
-->

## 2026-08-15 — B19: ch19 伏見城 / Fushimi Castle + whole-book completion
- ch19 translated (folios 608-652, 310 paras, 3 notes). The final novel chapter. All checks green.
- GLOBAL: spelling locale cascaded British→American across ch05/06/08/09/13/16/19 reading files,
  notes.json, glossary.json (80 occurrences: storey→story, colour→color, travelling→traveling,
  favour→favor, humour→humor, honour→honor, rumour→rumor, grey→gray, centre→center, etc.). ch01
  (approved reference) was already American. Rebuilt; qa_epub PASS, epubcheck 0/0/0/0. Ledger now
  0 British / 130 American.
- data/pagemap/ch19.json added (45 entries, printed==PDF). data/noise.txt +9 name/idiom numerals.
- authority.json: 256 decided renderings fed in under slug owls-castle.
- New files: COMPLETION.md, out/deep_audit.md, out/term_ledger.md.
- Novel COMPLETE (19 of 20 sections). ch20 解説 (afterword) pending the commissioner's decision.
