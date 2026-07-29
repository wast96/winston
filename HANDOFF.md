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
the stray). The deliverable is out/thousand-li.epub. B01 (ch01-ch05), B02 (ch06-ch08),
B03 (ch09-ch11), B04 (ch12-ch14) and B05 (ch15-ch17) are done.

First: data/src/ is regenerable and gitignored, so if it is missing run
scripts/ingest_epub.py source.epub to recreate the extracted source text.

Do Batch B06 = ch18 through ch20 end to end: ch18 茂昌煤号 (The Maochang Coal
Company), ch19 二月 (February), ch20 兴昌药号 (The Xingchang Apothecary). Read each
unit's source from data/src/ (21_part0019.txt, 22_part0020.txt, 23_part0021.txt).
Translate to the register in CLAUDE.md: clean flowing English prose, the novel's own
voice, all apparatus in footnotes, never inline.

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
  fixed in the prose, not waived (in B05, 两位同志/前后两扇门/四壁 were rendered with the
  explicit count; 退一万步/百褶/千金 were added to check_noise.txt as idioms). If a
  compound English date-ordinal the checker cannot parse is flagged (like "twenty-third"),
  extend WORD_NUM in scripts/check_numbers.py, as B04 did (do not revert existing patches).

Footnotes are a RICH, fact-checked apparatus (the commissioner asked for a lot):
- Annotate real places, people, institutions and cultural references generously, and say
  in each note whether the thing is REAL history or the novel's invention, and whether the
  claim is corroborated / uncorroborated / contradicted. Fact-check against real
  scholarship (Wikipedia, Baidu Baike, academic/government sources). NEVER cite Grok,
  Grokipedia, or any AI-written source. Use subagents with web access for the research.
- Anchors must be verbatim substrings of the English prose; recurring subjects get their
  note at FIRST appearance in the book, so CHECK glossary.json and notes.json before
  re-noting something already covered. Among the ~108 already noted, recently added: the
  painting 千里江山图 (Wang Ximeng, noted at ch15 where the title is first spoken), the
  August 7th Conference, the Central Red Route courier line (Shanghai-Shantou-Ruijin), the
  Canton-Hong Kong Strike, the ABC of Communism, native banks (钱庄), "big yellow croaker"
  gold-bar slang, the Three Principles of the People, Professor Tao (Tao Xisheng), the Nanshi
  police, Tianjin Road, Seward Road. Note bodies are XHTML with NUMERIC character references
  (&#8212;, &#160;, &#183;), never named entities. Add new glossary rows (one rendering per
  referent, decided before romanizing; real = "attested" with the fact, fictional cast
  marked so).

Scene typography (keep it up): the source carries NO typographic scene dividers. It heads
some scenes with a terse time/place line, and hard-cuts the rest. Add entries to scenes.json
for each new chapter: "datelines" lists those terse scene-header lines VERBATIM (rendered
centered), and "breaks" lists the opening words of paragraphs that begin a new scene at a
hard cut with no dateline (a centered divider is inserted before them). Verify each string
against the reading file, then confirm the built EPUB shows the expected number of breaks
(grep 'class="brk"' in the unzipped chapter xhtml). ch15 had 2 breaks, ch16 4, ch17 7 (a
fast heist montage). A paragraph that opens on dialogue uses the leading curly quote in its
break anchor (the builder matches startswith). ch18-ch20 may or may not have breaks; check.

Run the CLAUDE.md checks including blind double-translation on the argumentative/literary
passages and a back-translation omission pass (use subagents in separate contexts);
record what ran in PROGRESS.md.

Then rebuild: scripts/build_reading_epub.py out/thousand-li.epub, and run
scripts/qa_epub.py out/thousand-li.epub until green (it refuses on an unmatched note
anchor). Commit to claude/thousand-li and push. Rewrite HANDOFF.md so its first section
is the paste-ready kickoff for Batch B07 (ch21-ch22). Cite chapters, never page numbers.
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
- Batch B03 = ch09-ch11 (The Photograph, The Clinic, The Tenant): done, all checks clean.
- Batch B04 = ch12-ch14 (A Letter from Afar, The Revolving Door, New Year's Eve): done; 90 notes.
- Batch B05 = ch15-ch17 (Code Words, The Bank, The Suitcase): 217 paragraphs; parity and number
  checks clean; blind double-translation and back-translation confirm the text; 18 new footnotes
  taking the book to 108 notes; glossary expanded. The title painting is spoken for the first time
  (ch15, as the passphrase) and footnoted there; Cui Wentai bolts with the gold (ch17). See PROGRESS.md.
- Book-wide so far: footnotes at 108, fact-checked and real-vs-fictional / corroborated-labelled;
  ch01 is a centered EPIGRAPH (kind:"epigraph"); scene typography via scenes.json + builder;
  glossary the term ledger (real "attested", fictional marked).

## Tooling in place

- scripts/make_bilingual.py, split_bilingual.py: the translation pipeline (verbatim source,
  paragraph parity). check_noise.txt: project noise for check_numbers.py (ALWAYS pass
  --noise check_noise.txt); extend when a name/idiom with a digit is flagged. B05 added
  退一万步, 百褶, 千金.
- scenes.json: per-chapter "datelines" (verbatim scene-header lines, rendered centered) and
  "breaks" (paragraph-opening anchors for hard cuts, get a centered divider). Add an entry for
  every new chapter (empty arrays are fine for single-scene chapters). Break anchors for
  dialogue-opening paragraphs must include the leading curly quote.
- scripts/build_reading_epub.py supports datelines, scene breaks, the epigraph and a book.json
  "translator_note". Do not revert.
- scripts/check_numbers.py keeps its patches (B01 clock times / teen ordinals; B03 negative
  lookbehind on the 一[日夜时…] idiom stripper; B04 added twentieth/twenty-first/twenty-second
  to WORD_NUM). Do not revert.

## Renderings settled this batch (full ledger in glossary.json)

- People: Little Shi (小施, bank safe-deposit clerk, fictional); Mr. Ji (纪先生, Chen Qianli's
  wealthy-collector bank alias, fictional); Wang Jinzhi (王金枝, the murdered steward of Cui Wentai's
  anecdote, apparently fictional). Real: Professor Tao = Tao Xisheng (陶希圣); T. V. Soong (宋子文),
  finance minister 1928-33, evoked unnamed by the "Mr. Song's brother" / Ministry-of-Finance hint.
- Places: Tianjin Road (天津路), Seward Road (熙华德路 -> Changzhi Rd), Jiangxi Road (江西路), Shantou
  (汕头), Wuhan (武汉), Hangzhou (杭州) -- all real; Fucheng Li (阜成里) and the Yiyuan Café (逸园咖啡馆)
  likely fictional.
- Orgs: the Yuji native bank (裕记钱庄, fictional command post); the Nanshi Police Bureau (南市警察署);
  Taikoo (太古, Butterfield & Swire / China Navigation Co.).
- Terms: big yellow croaker (大黄鱼, gold-bar slang); native bank (钱庄); secondhand-clothes shop
  (估衣铺); jianren rank (简任); the August 7th Conference (八七会议); the Canton-Hong Kong Strike
  (省港大罢工); the Three Principles of the People (三民主义); the ABC of Communism (共产主义ABC); the
  Central Red Route (中央红色交通线); marten-paw fur (貂爪仁, the novel's embellishment).

## What is NEXT

- B06 = ch18-ch20 (The Maochang Coal Company, February, The Xingchang Apothecary). Then B07 =
  ch21-ch22, and so on through B12 = ch34-ch37 (book.json "batches").

## Open items for the read-through

- Publisher discrepancy for the colophon: the copyright leaf prints 上海文化出版社, but the ISBN
  prefix and the Weibo/WeChat handles are 上海文艺出版社. Confirm before back_matter.json /
  the colophon is finalized (back_matter.json still empty).
- The painting: now named and footnoted at ch15 (Wang Ximeng's 千里江山图, spoken as the passphrase).
  Do NOT re-note the painting when the name recurs.
- The "Mr. Song's brother" / T. V. Soong reading (ch17) is footnoted as an invited inference, not
  stated by the text; keep that framing if the Song family recurs.
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
