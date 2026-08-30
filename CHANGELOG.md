# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

<!-- Newest first. Example:
## 2026-01-01 — corrections batch 1
- GLOBAL: renamed "X" to "Y" everywhere (glossary + grep across ch01-ch12); rebuilt, qa green.
- LOCAL: fixed a dropped clause in ch03 section 2.
-->
## 2026-08-30 — front matter: reader-orientation pages + pronunciation (commissioner request)

- NEW (front matter): three spoiler-free orientation pages added after the Cast, in the
  spine and the navigation (Cast, then Divided City, Two Sides, Reckoning the Days, then the
  text):
  - **The Divided City** — Shanghai's split jurisdictions (International Settlement, French
    Concession, Nanshi, Zhabei) and why the borders drive the plot.
  - **The Two Sides** — the Communist underground structure vs the Nationalist secret
    services, and the vocabulary the reader meets (White areas, reflection institute, etc.).
  - **Reckoning the Days** — the lunar calendar the novel keeps time by (the first month,
    New Year's Eve, the Lantern Festival), mapped to early 1933, plus the solar terms and the
    Republican year count.
- NEW: the **Cast page** now also carries a *Names and forms of address* note (Old X / Little
  X / Master / rank / code names) and a *Saying the names* pinyin pronunciation guide (the
  surprising sounds with worked examples, plus a place-name list). Each cast entry gained a
  rough respelling, and the geography page carries respellings inline on first mention.
- SPOILER-FREE by design: orientation and pronunciation only; no plot, no character reveals.
  A build-time guard-grep of all four new pages confirmed no reveal terms leaked.
- Mechanics: the orientation pages are data-driven from a new `orientation.json`; the cast
  extras from the expanded `cast.json`. `scripts/build_reading_epub.py` gained
  `render_orientation_page()`, extended `render_cast()`, a `.pron` style, and the spine/nav
  wiring. Files: orientation.json, cast.json, scripts/build_reading_epub.py.
- Rebuilt out/A Thousand Li of Rivers and Mountains.epub (37 of 37 units, 338 notes);
  qa_epub.py PASS (54 files, 48 documents, 338 references = bodies = backlinks; all links
  resolve). No translation text, note, glossary, or rendering of the body changed.

## 2026-08-30 — front matter: spoiler-free Cast of Characters (commissioner request)

- NEW (front matter): added a **Cast of Characters** page at the start of the book, placed
  in the spine right after the Contents (cover, title page, contents, cast, then the text)
  and linked in the e-reader navigation. It groups the principal figures by faction (the
  Communist underground; the Nationalist secret service; other Shanghai figures) with a
  one-line blurb each, so the reader can tell who is who at a glance.
- SPOILER-FREE by design: every figure is described only by the surface role in which the
  reader first meets them. No hidden identities, allegiances-behind-a-cover, deaths,
  reveal-romances, or plot turns are stated; back-story-only figures (e.g. Ye Tao) are
  omitted entirely, and the cover identities of double-dealing figures are presented at face
  value, exactly as the narrative first frames them. A build-time guard-grep confirmed no
  reveal terms leaked onto the page. The near-identical names Chen Qianli / Chen Qianyuan
  are flagged for the reader.
- Mechanics: the cast is data-driven from a new `cast.json` (the editable source of truth);
  `scripts/build_reading_epub.py` gained `render_cast()`, a `.cast` style block, and the
  spine/nav wiring. Files: cast.json, scripts/build_reading_epub.py.
- Rebuilt out/A Thousand Li of Rivers and Mountains.epub (37 of 37 units, 338 notes);
  qa_epub.py PASS (51 files, 45 documents, 338 references = bodies = backlinks; all links
  resolve). No translation text, note, glossary, or rendering changed.

## 2026-07-31 — corrections pass: no items filed; build re-verified green

- CORRECTIONS.md contained no items (template only), so no text, note, glossary or
  rendering changed. The edition stands as completed at B12.
- Branch hygiene (CLAUDE.md rule 2): the stray branch claude/thousand-li-corrections-4e2fdv
  duplicated the working branch's history; the stale local claude/thousand-li was
  fast-forwarded to the full B01-B12 history (origin already had it) and the stray branch
  deleted, local and remote. No commits were lost; the two branches were identical.
- Re-verification from a clean checkout: data/src/ regenerated (scripts/ingest_epub.py,
  41 spine documents, 157,360 source chars); out/thousand-li.epub rebuilt (37 of 37 units,
  217 notes); qa_epub.py PASS (50 files, 44 documents, 217 references = bodies = backlinks,
  all links resolve); check_numbers.py --noise check_noise.txt clean on all 36 machine-
  checkable units (2,710 pairs, 0 unresolved; ch01 epigraph has no body pairs);
  check_structure.py parity OK on all 36, whole-book anchor check 217 notes / 0 unresolved;
  heading shapes the documented legitimate three (epigraph, chapters, Appendix H2+H3).
- Files touched: CHANGELOG.md only.

## 2026-07-29 — Batch B03 (ch09-ch11) plus one retro note and a tooling fix

- Translated ch09-ch11 (255 paragraphs); footnotes grown from 46 to 69 (22 new + 1 retro on
  ch07's surety-bond mention). Glossary expanded with the B03 referents. Files: out/ch09-11_*,
  notes.json, glossary.json, scenes.json (empty entries for three single-scene chapters).
- TOOLING: patched scripts/check_numbers.py so the built-in idiom stripper 一[日夜时…] no longer
  eats the 一 out of a real date compound like 十一日 (which had mis-parsed March 11 as "10");
  added a negative lookbehind (mirroring the existing 十分 guard) and registered the ordinal
  "eleventh" in WORD_NUM. Verified conservative: standalone 一日/一时 idioms still stripped,
  十一日/二十一日 now parse correctly. No text affected; a number-check false positive removed.

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
