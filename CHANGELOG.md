# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

<!-- Newest first. Example:
## 2026-01-01 — corrections batch 1
- GLOBAL: renamed "X" to "Y" everywhere (glossary + grep across ch01-ch08); rebuilt, qa green.
- LOCAL: fixed dropped clause at ch03 §2 folio 45.
-->

## 2026-08-13 — B10 whole-book reconciliation (final batch)
- GLOBAL: one spelling locale, cascaded to American across readings, notes, glossary, book.json (favour/labour/theatre; a capital "Labour" in a note; "greyhound" protected as correct).
- GLOBAL: unified renderings across all built units — 爱多亚路 "Avenue Edward VII"; Yan'an-road glosses to "[Name] East/Middle Road"; 四大家族 "the Four Big Families"; 小阿荣 "Little Ah Rong"; 申报 "Shen Bao" (prose + glossary + authority).
- LOCAL: ch03 name error 吴绍澍 "Wu Xingya" -> "Wu Shaoshu" (folio ~9); ch13 "Rue Foch" -> "Avenue Foch" and "Fu Xiaoan" -> "Fu Xiao'an".
- GLOSSARY: pulled 方治 (false-matches 地方治安); corrected the 常春恒 note (beaten -> shot, per the ch25 source).
- Rebuilt; qa_epub PASS, epubcheck 0/0/0; check_content, check_apparatus, check_reconcile, qc_entities all clean.

