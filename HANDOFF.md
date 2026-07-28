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
the stray). The deliverable is out/thousand-li.epub. B01 (ch01-ch05) and B02
(ch06-ch08) are done.

First: data/src/ is regenerable and gitignored, so if it is missing run
scripts/ingest_epub.py source.epub to recreate the extracted source text.

Do Batch B03 = ch09 through ch11 end to end: ch09 照片 (The Photograph), ch10 诊所
(The Clinic), ch11 租客 (The Tenant). Read each unit's source from data/src/
(12_part0010.txt, 13_part0011.txt, 14_part0012.txt). Translate to the register in
CLAUDE.md: clean flowing English prose, the novel's own voice, all apparatus in
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

Footnotes are now a RICH, fact-checked apparatus (the commissioner asked for a lot more):
- Annotate real places, people, institutions and cultural references generously, and say
  in each note whether the thing is REAL history or the novel's invention, and whether the
  claim is corroborated / uncorroborated / contradicted. Fact-check against real
  scholarship (Wikipedia, Baidu Baike, academic/government sources). NEVER cite Grok,
  Grokipedia, or any AI-written source. Use subagents with web access for the research,
  as in B02.
- Anchors must be verbatim substrings of the English prose; recurring subjects get their
  note at FIRST appearance in the book, so CHECK glossary.json and notes.json before
  re-noting something already covered. Note bodies are XHTML with NUMERIC character
  references (&#8212;, &#160;, &#183;), never named entities. Add new glossary rows
  (one rendering per referent, decided before romanizing; real = "attested" with the fact,
  fictional cast marked so).

Scene typography (keep it up, watch for it going forward): the source carries NO
typographic scene dividers. It heads some scenes with a terse time/place line, and
hard-cuts the rest. Add entries to scenes.json for each new chapter: "datelines" lists
those terse scene-header lines VERBATIM (rendered centered), and "breaks" lists the
opening words of paragraphs that begin a new scene at a hard cut with no dateline (a
centered divider is inserted before them). Verify each string against the reading file.

Run the CLAUDE.md checks including blind double-translation on the argumentative/literary
passages and a back-translation omission pass (use subagents in separate contexts, as in
B02); record what ran in PROGRESS.md.

Then rebuild: scripts/build_reading_epub.py out/thousand-li.epub, and run
scripts/qa_epub.py out/thousand-li.epub until green (it refuses on an unmatched note
anchor). Commit to claude/thousand-li and push. Rewrite HANDOFF.md so its first section
is the paste-ready kickoff for Batch B04 (ch12-ch14). Cite chapters, never page numbers.
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
- Batch B01 = ch01-ch05 (epigraph, Dice, Longhua, Miss Tao, Xuanwu Lake): translated end to
  end; parity/number checks clean; blind double-translation and back-translation done.
- Batch B02 = ch06-ch08 (Identity, Old Fang, The Race Ticket): 255 paragraphs; all checks
  clean (blind double-translation and back-translation confirm the text). See PROGRESS.md.
- Book-wide enhancements applied this batch (they touch B01 too; recorded in CHANGELOG.md):
  1. Footnotes grown from 13 to 46 across ch02-ch08, fact-checked, real-vs-fictional and
     corroborated/uncorroborated/contradicted labelled. A reader-facing translator's note
     was added (real/fictional framing and the scene-typography convention).
  2. ch01 reframed from a content-less chapter into a centered EPIGRAPH (kind:"epigraph").
  3. Scene typography added via scenes.json + builder: centered datelines and scene breaks.
  4. glossary.json expanded; real entities "attested", fictional cast marked.

## Tooling in place

- scripts/make_bilingual.py, split_bilingual.py: the translation pipeline (verbatim source,
  paragraph parity). check_noise.txt: project noise for check_numbers.py (ALWAYS pass
  --noise check_noise.txt); extend when a name/idiom with a digit is flagged.
- scenes.json (NEW): per-chapter "datelines" (verbatim scene-header lines, rendered centered)
  and "breaks" (paragraph-opening anchors for hard cuts, get a centered divider). Add an
  entry for every new chapter.
- scripts/build_reading_epub.py was patched to support datelines, scene breaks, the epigraph,
  and a book.json "translator_note". Do not revert. check_numbers.py keeps its B01 patches
  (clock times, teen ordinals). Do not revert.

## Renderings settled (keep consistent; full ledger in glossary.json)

- Cast (fictional): Chen Qianli, Chen Qianyuan, Ling Wen, Yi Junnian ("Old Yi"), Fang Yunping
  ("Old Fang") + son "Young Fang", Wei Dafu ("Old Wei"), Lin Shi, Liang Shichao, Dong Huiwen,
  Cui Wentai, Tian Fei, Qin Chuan'an, You Tianxiao, Mu Chuan, Ye Qinian, Miss Tao. Aliases:
  Haohan (浩瀚), "Old Kai" (老开, distinct from Haohan). Real figures (attested): Chiang
  Kai-shek / the Generalissimo, Cai Tingkai / Commander Cai, Weng Zhaoyuan / Brigade
  Commander Weng (distinct from the fictional Adjutant Weng), Du Yuesheng, Li Guojie, Li
  Hongzhang, Lu Xun, Feng Xuefeng, Chen Geng, Sun Yat-sen, Marlene Dietrich, Qiu Ying.
- Institutions: 军法处 = the Judge Advocate's office (head = "Director"); 侦缉队 = the detective
  squad; 巡捕房 = the Municipal Police; 工部局 = Shanghai Municipal Council; 特工总部 = the
  Special Operations Headquarters; 党务调查科 = the Party Affairs Investigation Section;
  中央交通局 = the Central Liaison Bureau; 左联 = the Left League; 房屋经租处 = the
  house-letting agency. Places: Longhua, the World Hotel, the Lyceum Theatre, the Grand
  Theatre, the Carlton Theatre, the racecourse (today People's Square), the Four Banks'
  Savings Society building (= Park Hotel), the German Hospital, Xinjing, Beiping, Khabarovsk,
  North Sichuan Road. 租界 = the Settlement (the International Settlement).

## What is NEXT

- B03 = ch09-ch11 (The Photograph, The Clinic, The Tenant). Then B04 = ch12-ch14, and so on
  through B12 = ch34-ch37 (book.json "batches").

## Open items for the read-through

- Publisher discrepancy for the colophon: the copyright leaf prints 上海文化出版社, but the
  ISBN prefix and the Weibo/WeChat handles are 上海文艺出版社. Confirm before back_matter.json /
  the colophon is finalized (back_matter.json still empty).
- Provisional English titles to settle in the glossary as their chapters arrive: Garrick
  (茄力克, ch23; already glossed as the cigarette brand), Jiaoli (角里, ch25), Xiaotaoyuan
  (小桃源, ch28), The Tanglong Door (趟栊门, ch21), The Guisheng (贵生轮, ch26).
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
  English prose. Note bodies are XHTML with NUMERIC character references, never named
  entities. A chapter H1 title cannot carry a note.
- Deliverable filename is out/thousand-li.epub. Work stays on branch claude/thousand-li.
  data/src/ and out/*_bilingual.md and out/*.epub are gitignored; out/*_reading.md,
  out/*_en.json, data/zh/*.txt, scenes.json, notes.json, glossary.json are tracked.
