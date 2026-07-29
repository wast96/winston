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
the stray). The deliverable is out/thousand-li.epub. B01 (ch01-ch05), B02 (ch06-ch08)
and B03 (ch09-ch11) are done.

First: data/src/ is regenerable and gitignored, so if it is missing run
scripts/ingest_epub.py source.epub to recreate the extracted source text.

Do Batch B04 = ch12 through ch14 end to end: ch12 远方来信 (A Letter from Afar), ch13
旋转门 (The Revolving Door), ch14 除夕 (New Year's Eve). Read each unit's source from
data/src/ (15_part0013.txt, 16_part0014.txt, 17_part0015.txt). Translate to the register
in CLAUDE.md: clean flowing English prose, the novel's own voice, all apparatus in
footnotes, never inline.

Method that works, reuse it:
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

Footnotes are a RICH, fact-checked apparatus (the commissioner asked for a lot):
- Annotate real places, people, institutions and cultural references generously, and say
  in each note whether the thing is REAL history or the novel's invention, and whether the
  claim is corroborated / uncorroborated / contradicted. Fact-check against real
  scholarship (Wikipedia, Baidu Baike, academic/government sources). NEVER cite Grok,
  Grokipedia, or any AI-written source. Use subagents with web access for the research.
- Anchors must be verbatim substrings of the English prose; recurring subjects get their
  note at FIRST appearance in the book, so CHECK glossary.json and notes.json before
  re-noting something already covered (e.g. the German Hospital, the Longhua martyrs,
  Winter, the Judge Advocate's office, the Morriss name are all ALREADY noted). Note
  bodies are XHTML with NUMERIC character references (&#8212;, &#160;, &#183;), never
  named entities. Add new glossary rows (one rendering per referent, decided before
  romanizing; real = "attested" with the fact, fictional cast marked so).

Scene typography (keep it up): the source carries NO typographic scene dividers. It heads
some scenes with a terse time/place line, and hard-cuts the rest. Add entries to scenes.json
for each new chapter: "datelines" lists those terse scene-header lines VERBATIM (rendered
centered), and "breaks" lists the opening words of paragraphs that begin a new scene at a
hard cut with no dateline (a centered divider is inserted before them). Verify each string
against the reading file. (B03's ch09-ch11 were each a single continuous scene, so their
entries are empty; ch12-ch14 may or may not be — check.)

Run the CLAUDE.md checks including blind double-translation on the argumentative/literary
passages and a back-translation omission pass (use subagents in separate contexts);
record what ran in PROGRESS.md.

Then rebuild: scripts/build_reading_epub.py out/thousand-li.epub, and run
scripts/qa_epub.py out/thousand-li.epub until green (it refuses on an unmatched note
anchor). Commit to claude/thousand-li and push. Rewrite HANDOFF.md so its first section
is the paste-ready kickoff for Batch B05 (ch15-ch17). Cite chapters, never page numbers.
Never invent bridging text; footnote any genuine ambiguity and leave it visible. Do not
pause for approval mid-batch.

When you finish the batch, your final chat reply MUST contain BOTH of these, every time,
so I can start the next batch from a fresh chat: (1) the built out/thousand-li.epub
attached as a file, and (2) the next batch's paste-ready kickoff message pasted VERBATIM
inside a fenced code block, right here in the chat. Writing it into HANDOFF.md or pointing
me there is NOT enough. No batch is complete without both.
```

## What is DONE (do not redo)

- Step 0 (ingest + survey): source ingested, book.json authored (37 units), skeleton EPUB
  with hyperlinked TOC, qa green. 12-batch plan approved (book.json "batches").
- Batch B01 = ch01-ch05 (epigraph, Dice, Longhua, Miss Tao, Xuanwu Lake): done, all checks clean.
- Batch B02 = ch06-ch08 (Identity, Old Fang, The Race Ticket): done, all checks clean.
- Batch B03 = ch09-ch11 (The Photograph, The Clinic, The Tenant): 255 paragraphs; parity and
  number checks clean; blind double-translation and back-translation confirm the text; 22 new
  footnotes (+1 retro on ch07) taking the book to 69 notes; glossary expanded. See PROGRESS.md.
- Book-wide so far: footnotes at 69, fact-checked and real-vs-fictional / corroborated-labelled;
  ch01 is a centered EPIGRAPH (kind:"epigraph"); scene typography via scenes.json + builder;
  glossary the term ledger (real "attested", fictional marked).

## Tooling in place

- scripts/make_bilingual.py, split_bilingual.py: the translation pipeline (verbatim source,
  paragraph parity). check_noise.txt: project noise for check_numbers.py (ALWAYS pass
  --noise check_noise.txt); extend when a name/idiom with a digit is flagged. B03 added
  吴四宝 and 三成坊.
- scenes.json: per-chapter "datelines" (verbatim scene-header lines, rendered centered) and
  "breaks" (paragraph-opening anchors for hard cuts, get a centered divider). Add an entry for
  every new chapter (empty arrays are fine for single-scene chapters).
- scripts/build_reading_epub.py supports datelines, scene breaks, the epigraph and a book.json
  "translator_note". Do not revert.
- scripts/check_numbers.py keeps its patches (B01 clock times / teen ordinals; B03 negative
  lookbehind on the 一[日夜时…] idiom stripper so real dates like 十一日 parse, plus the ordinal
  "eleventh" in WORD_NUM). Do not revert.

## Renderings settled this batch (full ledger in glossary.json)

- People: Wu Sibao (吴四宝, "Little Bao" — real Green-Gang/No.76 figure, planted here as a minor
  tenant); Assistant Manager Wu (吴作民); Jin Delin (金德林, fictional). Li Han (李汉) already glossed.
- Institutions: 中汇信托银行 = the Zhonghui Trust Bank (Du Yuesheng's, real); 仁泰银公司 = the
  Rentai Bank Company (likely fictional); 东陆经租处 = the Donglu house-letting agency;
  冠生园 = Guanshengyuan (real). 内奸 = "mole"; 特务 = "agents"; 看守所 = "the lockup";
  上级派来的同志 = "the comrade sent down from above"; 任务 = "assignment".
- Places: 马立斯新村 = the Morriss Estate; 虹口公园 = Hongkou Park; 静安寺 = Jing'an Temple;
  同福里/三成坊 = Tongfu Li / Sancheng Fang (fictional lanes); 田谷邨 = the Tiangu Estate.
  Real French-Concession roads with today's names: 马斯南路 = Massenet Road (Sinan Rd);
  愚园路 = Yuyuan Rd; 地丰路 = Difeng Rd (Urumqi North Rd); 海格路 = Haige Rd (Huashan Rd);
  善钟路 = Shanzhong Rd (Changshu Rd); 赵主教路 = Zhaozhujiao Rd (today WUYUAN Rd, after Bishop
  Maresca — NOT Shaanxi South Rd); 肇嘉浜 = Zhaojiabang (creek).

## What is NEXT

- B04 = ch12-ch14 (A Letter from Afar, The Revolving Door, New Year's Eve). Then B05 = ch15-ch17,
  and so on through B12 = ch34-ch37 (book.json "batches").

## Open items for the read-through

- Publisher discrepancy for the colophon: the copyright leaf prints 上海文化出版社, but the ISBN
  prefix and the Weibo/WeChat handles are 上海文艺出版社. Confirm before back_matter.json /
  the colophon is finalized (back_matter.json still empty).
- Provisional English titles to settle in the glossary as their chapters arrive: Garrick (茄力克,
  ch23; already glossed as the cigarette brand), Jiaoli (角里, ch25), Xiaotaoyuan (小桃源, ch28),
  The Tanglong Door (趟栊门, ch21), The Guisheng (贵生轮, ch26).
- The appendix (ch37) frames the fiction as recovered history. Fact-check its named
  people/places/dates against real scholarship (rule 5) as they arrive.

## State / traps

- book.json is the LOGICAL structure. ch01 is an epigraph (kind:"epigraph"), NOT a chapter,
  and is excluded from the chapter tally. Front matter in the spine (cover, copyright leaf,
  the source's own 目录) is not a translation unit.
- The Appendix (ch37) is ONE chapter with two sections (ch37s01, ch37s02) from two source
  files; its reading.md uses "### " headings.
- The source carries NO footnotes of its own and NO typographic scene dividers; every note is
  the translator's, and scene datelines/breaks are supplied via scenes.json.
- Note anchors are inserted BEFORE markup substitution and must be verbatim substrings of the
  English prose. Note bodies are XHTML with NUMERIC character references, never named entities.
  A chapter H1 title cannot carry a note.
- Deliverable filename is out/thousand-li.epub. Work stays on branch claude/thousand-li.
  data/src/ and out/*_bilingual.md and out/*.epub are gitignored; out/*_reading.md,
  out/*_en.json, data/zh/*.txt, scenes.json, notes.json, glossary.json are tracked.
