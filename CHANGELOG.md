# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

<!-- Newest first. Example:
## 2026-01-01 — corrections batch 1
- GLOBAL: renamed "X" to "Y" everywhere (glossary + grep across ch01-ch08); rebuilt, qa green.
- LOCAL: fixed dropped clause at ch03 §2 folio 45.
-->

## 2026-08-15 — B20: ch20 解説 / Afterword (Muramatsu Takeshi) — BOOK COMPLETE
- ch20 translated (folios 653-660, 26 paras, 19 notes). The 解説, a third-party critical
  afterword; rendered as modern literary criticism, not Shiba's narrative. All checks green.
- FACT-CHECK CORRECTION: the critic 村松剛 reads Muramatsu **Takeshi**, not "Tsuyoshi" as the
  survey had it. Corrected in book.json (ch20 title_en) and reflected in the built EPUB.
- data/noise.txt +6: Shōwa era-year dates (三十四年/三十一年/三十年/四十年, rendered as Gregorian
  years, guarded) and name numerals 道三 (Dōsan) / 歳三 (Toshizō).
- data/checks.json: ch20 registered in docs+sources so check_content covers it.
- Build now reports 20 of 20 chapters; title page states the book is COMPLETE (no pending
  markers). notes.json 130→149. qa_epub PASS (34 files, 27 docs); epubcheck 5.1.0 0/0/0/0.
- check_reconcile re-run: 0 British / 133 American; no new drift from ch20.
- BOOK COMPLETE (20 of 20 sections). COMPLETION.md updated; next step is a corrections pass.

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
