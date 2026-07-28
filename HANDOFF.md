# HANDOFF — A Thousand Li of Rivers and Mountains (千里江山图), Sun Ganlu

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. We are translating 《千里江山图》 (A Thousand Li of
Rivers and Mountains, Sun Ganlu, 2022) from source.epub into an annotated English
EPUB. The survey is approved; the working branch is claude/thousand-li and the
deliverable is out/thousand-li.epub.

Do Batch B01 = ch01 through ch05 (the epigraph "1933: Around the Lunar New Year",
then Dice / 骰子, Longhua / 龙华, Miss Tao / 陶小姐, Xuanwu Lake / 玄武湖), end to
end. Read each unit's source from data/src/ (04_part0002.txt, 05_part0003.txt,
06_part0004.txt, 07_part0005.txt, 08_part0006.txt). Translate to the register in
CLAUDE.md: clean flowing English prose, the novel's own voice, all apparatus in
footnotes, never inline.

For each unit author ONE aligned bilingual QC file out/<id>_bilingual.md (source
'>' blockquote line, English paragraph beneath; headings tagged ## / ###), quoting
the source VERBATIM (copy, do not re-type). Generate the reading text and parity
source with scripts/split_bilingual.py. Run scripts/check_numbers.py and
scripts/check_structure.py and fix what they flag. Add footnotes to notes.json
(anchors must be verbatim substrings of the English; ~3 per chapter-equivalent;
recurring subjects noted at first appearance), glossary rows to glossary.json
(decide one rendering per referent BEFORE romanizing), and any figure specs to
figures.json. Run the checks in CLAUDE.md including blind double-translation on the
argumentative/literary passages and a back-translation omission pass; record what
ran in PROGRESS.md.

Settle these provisional titles/renderings in glossary.json this batch as they
come up: Longhua / 龙华 (district + the Longhua garrison/prison and its peach
groves, historically the site of the 1931 execution of the "Longhua martyrs" —
check against scholarship). Then rebuild: scripts/build_reading_epub.py
out/thousand-li.epub, run scripts/qa_epub.py until green (it refuses on an
unmatched note anchor). Commit to claude/thousand-li and push. Rewrite HANDOFF.md
so its first section is the paste-ready kickoff for Batch B02 (ch06–ch08). Cite
chapters/sections, never page numbers. Never invent bridging text; footnote any
genuine ambiguity and leave it visible. Do not pause for approval mid-batch.
Deliver out/thousand-li.epub in chat as an attached file at the end.
```

## What is DONE (do not redo)

- Step 0 (ingest + survey): source EPUB ingested (41 spine docs, 157,360 source
  chars, cover image only). book.json authored as the logical structure — 37
  units (epigraph, 34 titled chapters, closing unsigned letter, two-part
  appendix), 157,170 translatable source chars. Skeleton EPUB builds with a fully
  hyperlinked TOC; qa_epub.py green. Batch plan approved: 12 batches, ~16k chars
  chars each (recorded in book.json "batches"). Committed and pushed to
  claude/thousand-li.
- No chapters translated yet.

## What is NEXT

- Batch B01 = ch01–ch05 (epigraph, Dice, Longhua, Miss Tao, Xuanwu Lake). 15,918
  source chars.
- Then B02 = ch06–ch08, and so on through B12 = ch34–ch37 (see book.json
  "batches" for the full approved plan).

## Open items for the read-through

- Publisher discrepancy: the copyright leaf prints 上海文化出版社, but the ISBN
  prefix (978-7-5321) and the Weibo/WeChat handles are 上海文艺出版社 (Shanghai
  Literature and Art Publishing House). Confirm before the colophon is finalized.
- Provisional English titles to settle in glossary.json as their chapters arrive:
  Garrick / 茄力克 (ch23; an old-Shanghai cigarette brand — verify), Jiaoli / 角里
  (ch25; place name), Xiaotaoyuan / 小桃源 (ch28; "Little Peach Spring", likely a
  venue), The Tanglong Door / 趟栊门 (ch21; Cantonese sliding-door gate), The
  Guisheng / 贵生轮 (ch26; a steamer). One rendering per referent, decided in the
  glossary before it is romanized in prose.
- The novel is grounded in the 1933 Shanghai Communist underground; the appendix
  (Material One, an oral record on Chen Qianli / 陈千里; Material Two, a roll of
  the fallen) frames the fiction as recovered history. Fact-check named people,
  places and dates against real scholarship (rule 5); say corroborated /
  uncorroborated / contradicted.

## State / traps

- book.json is the LOGICAL structure. Source front matter (cover, copyright leaf,
  the source's own 目录/CONTENTS) is NOT a translation unit: the builder generates
  its own title page and Contents, and the copyright leaf will render as the
  colophon via back_matter.json (still to be populated — carries the publisher
  discrepancy above). Nothing is dropped.
- The Appendix (ch37) is ONE chapter with two sections (ch37s01 Material One from
  text/part0038.html, ch37s02 Material Two from text/part0039.html); its
  out/ch37_reading.md uses "### " headings matched to those two section ids in
  order. The two materials come from two different source files.
- The source carries NO footnotes/endnotes of its own; every note in the build is
  the translator's.
- Note anchors are inserted BEFORE markup substitution and must be verbatim
  substrings of the English prose, or the build refuses. Note bodies are XHTML
  with NUMERIC character references (&#8212;, &#160;), never named entities.
- Deliverable filename is out/thousand-li.epub (not the template default
  out/book.epub). Work stays on the single branch claude/thousand-li.
