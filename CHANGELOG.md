# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

<!-- Newest first. Example:
## 2026-01-01 — corrections batch 1
- GLOBAL: renamed "X" to "Y" everywhere (glossary + grep across ch01-ch12); rebuilt, qa green.
- LOCAL: fixed a dropped clause in ch03 section 2.
-->
## 2026-07-28 — Batch B02 plus book-wide enhancements (touch B01)

- GLOBAL: added scene typography. New scenes.json and builder support render the source's
  terse time/place scene-headers as centered datelines and insert centered scene breaks at
  hard cuts. Applied across ch02-ch08 (the source itself carries no dividers; this is
  typography only, no text changed). Files: scenes.json, scripts/build_reading_epub.py.
- GLOBAL: reframed ch01 "1933 / Around the Lunar New Year" as a centered epigraph rather
  than a content-less chapter (kind:"epigraph" in book.json; builder renders it centered and
  drops it from the chapter tally). Files: book.json, out/ch01_reading.md,
  scripts/build_reading_epub.py.
- GLOBAL: expanded the footnote apparatus from 13 to 46 notes (ch02-ch08), all fact-checked
  against Wikipedia / Baidu Baike / academic sources, marking real vs fictional and
  corroborated / uncorroborated / contradicted. Added a reader-facing translator's note
  (real/fictional framing and the typography convention). Files: notes.json, book.json.
- GLOBAL: glossary expanded with B02 referents; real figures and places moved to "attested"
  with the fact behind them, fictional cast marked as such. File: glossary.json.
- NEW: translated ch06 (Identity), ch07 (Old Fang), ch08 (The Race Ticket) end to end;
  parity, number, blind double-translation and back-translation checks clean. Files:
  out/ch0{6,7,8}_reading.md, data/zh/ch0{6,7,8}.txt, out/ch0{6,7,8}_en.json.
- Extended check_noise.txt (四下, 第二天, 年三十, 四川, 二(?=岁)).
- Rebuilt out/thousand-li.epub (8 of 37 units, 46 notes); qa_epub PASS.

## 2026-07-28 — glossary accuracy (B01 read-through question)
- LOCAL: glossary rows for 浙江大戏院 and 世界大旅社 enriched after fact-check.
  浙江大戏院 confirmed as the real Hudec cinema on Zhejiang Middle Road by the
  Fourth Avenue market (the author's named location, not 大上海大戏院). For 世界大旅社
  the sources consulted differ on whether the specific hotel is documented, so its
  note is left neutral (the rooftop-amusement-garden type was real to the district);
  renderings unchanged. Superseded in part by the B02 pass above.
