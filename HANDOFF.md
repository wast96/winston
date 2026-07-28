# HANDOFF — A Thousand Li of Rivers and Mountains (千里江山图), Sun Ganlu

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. We are translating 《千里江山图》 (A Thousand Li of
Rivers and Mountains, Sun Ganlu, 2022) into an annotated English EPUB. The working
branch is claude/thousand-li (ONE branch; move any stray work onto it and delete
the stray). The deliverable is out/thousand-li.epub. Batch B01 (ch01-ch05) is done.

First: data/src/ is regenerable and gitignored, so if it is missing run
scripts/ingest_epub.py source.epub to recreate the extracted source text.

Do Batch B02 = ch06 through ch08 end to end: ch06 身份 (Identity), ch07 老方 (Old
Fang), ch08 赛马票 (The Race Ticket). Read each unit's source from data/src/
(09_part0007.txt, 10_part0008.txt, 11_part0009.txt). Translate to the register in
CLAUDE.md: clean flowing English prose, the novel's own voice, all apparatus in
footnotes, never inline.

Method that worked in B01, reuse it:
- For each unit, write out/<id>_en.json (a JSON array of English paragraphs, ONE per
  source paragraph line), then run:
    python3 scripts/make_bilingual.py <id> data/src/<file>.txt "<English title>" <id>_en.json
  It reads the source lines VERBATIM and enforces paragraph parity. Then
    python3 scripts/split_bilingual.py out/<id>_bilingual.md <id> "<中文标题>"
- Run scripts/check_numbers.py out/<id>_bilingual.md --noise check_noise.txt and
  scripts/check_structure.py --pairs data/zh/<id>.txt out/<id>_reading.md, and fix
  what they flag. ALWAYS pass --noise check_noise.txt; if a new non-quantity numeral
  (a name or idiom with a digit in it) is flagged, add it to check_noise.txt with a
  comment on its own line (no trailing comments). Real dropped/altered quantities get
  fixed in the prose, not waived.
- Add footnotes to notes.json (anchors must be verbatim substrings of the English;
  about 3 per chapter; recurring subjects noted at first appearance in the book, so
  check the glossary/notes before re-noting something already covered in B01). Add
  new glossary rows to glossary.json (decide one rendering per referent BEFORE
  romanizing; keep the B01 renderings consistent). Any figure specs to figures.json
  (there are none so far).
- Run the CLAUDE.md checks including blind double-translation on the
  argumentative/literary passages and a back-translation omission pass (use
  subagents in separate contexts, as in B01); record what ran in PROGRESS.md.

Then rebuild: scripts/build_reading_epub.py out/thousand-li.epub, and run
scripts/qa_epub.py out/thousand-li.epub until green (it refuses on an unmatched note
anchor). Commit to claude/thousand-li and push. Rewrite HANDOFF.md so its first
section is the paste-ready kickoff for Batch B03 (ch09-ch11). Cite chapters, never
page numbers. Never invent bridging text; footnote any genuine ambiguity and leave
it visible. Do not pause for approval mid-batch. Deliver out/thousand-li.epub in
chat as an attached file at the end.
```

## What is DONE (do not redo)

- Step 0 (ingest + survey): source ingested, book.json authored (37 units), skeleton
  EPUB with hyperlinked TOC, qa_epub green. 12-batch plan approved (book.json
  "batches").
- Batch B01 = ch01-ch05 (epigraph, Dice, Longhua, Miss Tao, Xuanwu Lake): translated
  end to end. 366 paragraphs; parity and number checks clean; 13 footnotes; glossary
  ledger populated; blind double-translation and back-translation passes done; EPUB
  built and qa_epub PASS. See PROGRESS.md for the full record.

## Tooling in place (built during B01)

- scripts/make_bilingual.py: builds the bilingual QC file from verbatim source lines
  plus a JSON list of English paragraphs. One source line = one English paragraph.
- check_noise.txt: project noise for check_numbers.py; ALWAYS pass
  --noise check_noise.txt. Extend it when a name/idiom containing a digit is flagged.
- scripts/check_numbers.py was patched so clock times (四十分, 五十分) survive the
  number check and teen ordinals (fifteenth, sixteenth) are recognized. Do not revert.

## Renderings settled in the glossary (keep consistent)

- Longhua (龙华) = district + Songhu Garrison Command + prison + Bao'en Pagoda; site of
  the 1931 "Longhua Martyrs". 军法处 = the Judge Advocate's office (its head rendered
  "Director", e.g. Director Mu). 侦缉队 = the detective squad. 巡捕房 = the Municipal
  Police. 工部局 = Shanghai Municipal Council. 特工总部 = the Special Operations
  Headquarters; 党务调查科 = the Party Affairs Investigation Section. 世界大旅社 = the
  World Hotel; 兰心大戏院 = the Lyceum Theatre; 四马路 = Fourth Avenue. Character names
  are standard pinyin (Wei Dafu, Yi Junnian, Ling Wen, You Tianxiao, Mu Chuan, Ye
  Qinian, Dong Huiwen, Chen Qianyuan, Fang Yunping, Haohan, etc.). 租界 = the
  Settlement (the International Settlement). Full ledger in glossary.json.

## What is NEXT

- B02 = ch06-ch08 (Identity, Old Fang, The Race Ticket). 13,949 source chars.
- Then B03 = ch09-ch11, and so on through B12 = ch34-ch37 (book.json "batches").

## Open items for the read-through

- Publisher discrepancy for the colophon: the copyright leaf prints 上海文化出版社, but
  the ISBN prefix (978-7-5321) and the Weibo/WeChat handles are 上海文艺出版社. Confirm
  before back_matter.json / the colophon is finalized (back_matter.json still empty).
- Provisional English titles to settle in the glossary as their chapters arrive:
  Garrick (茄力克, ch23), Jiaoli (角里, ch25), Xiaotaoyuan (小桃源, ch28), The Tanglong
  Door (趟栊门, ch21), The Guisheng (贵生轮, ch26).
- The appendix (ch37) frames the fiction as recovered history (Material One on Chen
  Qianli; Material Two, a roll of the fallen). Fact-check named people/places/dates
  against real scholarship (rule 5) as they arrive.

## State / traps

- book.json is the LOGICAL structure. Source front matter (cover, copyright leaf,
  the source's own 目录) is not a translation unit; the builder makes its own title
  page and Contents; the copyright leaf becomes the colophon via back_matter.json.
- The Appendix (ch37) is ONE chapter with two sections (ch37s01 Material One,
  ch37s02 Material Two) from two source files; its reading.md uses "### " headings.
- The source carries NO footnotes of its own; every note is the translator's.
- Note anchors are inserted BEFORE markup substitution and must be verbatim
  substrings of the English prose. Note bodies are XHTML with NUMERIC character
  references (&#8212;, &#160;, &#183;), never named entities. The chapter H1 title
  cannot carry a note (the builder does not run anchor insertion on it); anchor notes
  in body prose.
- Deliverable filename is out/thousand-li.epub. Work stays on branch
  claude/thousand-li. data/src/ and out/*_bilingual.md and out/*.epub are gitignored;
  out/*_reading.md and data/zh/*.txt are tracked.
