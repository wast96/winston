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
B03 (ch09-ch11), B04 (ch12-ch14), B05 (ch15-ch17) and B06 (ch18-ch20) are done.

First: data/src/ is regenerable and gitignored, so if it is missing run
scripts/ingest_epub.py source.epub to recreate the extracted source text.

Do Batch B07 = ch21 through ch22 end to end: ch21 趟栊门 (The Tanglong Door),
ch22 添男茶楼 (The Tiannan Teahouse). Read each unit's source from data/src/
(24_part0022.txt, 25_part0023.txt). Translate to the register in CLAUDE.md: clean
flowing English prose, the novel's own voice, all apparatus in footnotes, never inline.

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
  fixed in the prose, not waived (in B06, 两天/十七甫/五味子/五指毛桃/八婆/两公婆/十足十 were
  added to check_noise.txt as names/idioms; the clock times 十二点 were rendered "twelve",
  两天 as "two days", so the count survives). If a compound English word-numeral the checker
  cannot parse is flagged, extend WORD_NUM in scripts/check_numbers.py, as B04/B06 did (B06
  added "thirteenth"; do not revert existing patches).

Footnotes are a RICH, fact-checked apparatus (the commissioner asked for a lot):
- Annotate real places, people, institutions and cultural references generously, and say
  in each note whether the thing is REAL history or the novel's invention, and whether the
  claim is corroborated / uncorroborated / contradicted. Fact-check against real
  scholarship (Wikipedia, Baidu Baike, academic/government sources). NEVER cite Grok,
  Grokipedia, or any AI-written source. Use subagents with web access for the research.
- Anchors must be verbatim substrings of the English prose; recurring subjects get their
  note at FIRST appearance in the book, so CHECK glossary.json and notes.json before
  re-noting something already covered (a term already in glossary.json usually appeared in
  an earlier chapter and is already noted or covered there -- grep the reading files for its
  first appearance before footnoting it). Among the ~130 already noted, recently added in B06:
  Rou Shi's novella February (Chunchao Book Company, 1929; Lu Xun preface; Rou Shi a Longhua
  martyr, shot 7 Feb 1931) and its Tao Yuanqing line-drawing cover (NOT the woodcut the novel
  describes); the Relief Society (济难会 / China Red Aid); the 山/崔 blood-clue; the 脑后见腮/反骨
  physiognomy allusion; the Ninghan/Ningyue mergers and 训政 political tutelage; the playing-card
  code names (Laokai = the King); Dashatou Station; Deng Zhongxia and the strike Labour College;
  Chen Jitang's Guangdong; the Sincere Company rooftop; Shamian; Lingnan architecture (竹筒屋/骑楼/
  满洲窗); the People's Palace; the 吊钟花 / Shuangmendi flower market; the Hao cipher (豪密, Zhou
  Enlai); the captured high-power radio; Zhu Huiri; the Guangzhou Republican Daily; Lu Zhongde /
  Ouyang Min (fictional). Note bodies are XHTML with NUMERIC character references (&#8212;, &#160;,
  &#183;), never named entities. Add new glossary rows (one rendering per referent, decided before
  romanizing; real = "attested" with the fact, fictional cast marked so).

Rendering consistency (one rendering per referent -- check glossary.json AND grep earlier reading
files before you romanize or coin an English term). Established renderings that recur into the
Guangzhou chapters: 交通线 = "courier line"; 交通站 = "liaison station"; 交通局 = "Liaison Bureau";
机要交通员 = "secret courier"; 特工总部 = "the Special Operations Headquarters"; 苏区 = "the Soviet
area(s)"; 侦缉队 = "the detective squad"; 省港大罢工 = "the Canton-Hong Kong Strike"; 广州起义 =
"the Guangzhou Uprising"; 少山 = "Comrade Shaoshan" (Zhou Enlai); 龙冬 = "Long Dong". Boss Mo /
Mrs. Mo / Old Xiao and the Xingchang Apothecary are glossed from B06.

Scene typography (keep it up): the source carries NO typographic scene dividers. It heads
some scenes with a terse time/place line, and hard-cuts the rest. Add entries to scenes.json
for each new chapter: "datelines" lists those terse scene-header lines VERBATIM (rendered
centered), and "breaks" lists the opening words of paragraphs that begin a new scene at a
hard cut with no dateline (a centered divider is inserted before them). Verify each string
against the reading file, then confirm the built EPUB shows the expected number of breaks
(grep 'class="brk"' in the unzipped chapter xhtml). B06 had ch18 3 breaks, ch19 2, ch20 0
(a single continuous Guangzhou scene). A paragraph that opens on dialogue uses the leading
curly quote in its break anchor (the builder matches startswith). ch21-ch22 may or may not
have breaks; check.

Run the CLAUDE.md checks including blind double-translation on the argumentative/literary
passages and a back-translation omission pass (use subagents in separate contexts);
record what ran in PROGRESS.md.

Then rebuild: scripts/build_reading_epub.py out/thousand-li.epub, and run
scripts/qa_epub.py out/thousand-li.epub until green (it refuses on an unmatched note
anchor). Commit to claude/thousand-li and push. Rewrite HANDOFF.md so its first section
is the paste-ready kickoff for Batch B08 (ch23-ch25). Cite chapters, never page numbers.
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
- Batch B05 = ch15-ch17 (Code Words, The Bank, The Suitcase): done; 108 notes. The title painting is
  spoken for the first time (ch15) and Cui Wentai bolts with the gold (ch17).
- Batch B06 = ch18-ch20 (The Maochang Coal Company, February, The Xingchang Apothecary): 190 paragraphs
  (ch18 54, ch19 48, ch20 88); parity and number checks clean; blind double-translation and
  back-translation/faithfulness audit confirm the text; 22 new footnotes taking the book to 130.
  ch18 hides the group in the Zhaojiabang coal yard and reveals HOW Chen Qianli read the traitor
  (Old Fang's blood-written half-山 pointing at 崔/Cui); ch19 is Ling Wen's turn -- her past with Long
  Dong and the novel February -- and she takes command of the Guangzhou leg; ch20 moves to Guangzhou,
  where a courier from the Ruijin Soviet (Old Xiao) has a secret oral order for Lin Shi and, Lin Shi
  absent, must decide whether to trust it to Ling Wen. See PROGRESS.md.
- Book-wide so far: footnotes at 130, fact-checked and real-vs-fictional / corroborated-labelled;
  ch01 is a centered EPIGRAPH (kind:"epigraph"); scene typography via scenes.json + builder;
  glossary the term ledger (real "attested", fictional marked).

## Tooling in place

- scripts/make_bilingual.py, split_bilingual.py: the translation pipeline (verbatim source,
  paragraph parity). check_noise.txt: project noise for check_numbers.py (ALWAYS pass
  --noise check_noise.txt); extend when a name/idiom with a digit is flagged. B06 added
  十足十, 十七甫, 五味子, 五指毛桃, 八婆, 两公婆.
- scenes.json: per-chapter "datelines" (verbatim scene-header lines, rendered centered) and
  "breaks" (paragraph-opening anchors for hard cuts, get a centered divider). Add an entry for
  every new chapter (empty arrays are fine for single-scene chapters, as ch20). Break anchors for
  dialogue-opening paragraphs must include the leading curly quote.
- scripts/build_reading_epub.py supports datelines, scene breaks, the epigraph and a book.json
  "translator_note". Do not revert.
- scripts/check_numbers.py keeps its patches (B01 clock times / teen ordinals; B03 negative
  lookbehind on the 一[日夜时…] idiom stripper; B04 added twentieth/twenty-first/twenty-second;
  B06 added "thirteenth" to WORD_NUM). Do not revert.

## Renderings settled this batch (full ledger in glossary.json)

- People: Mo Shaoqiu / Boss Mo (莫少球) and Mrs. Mo (莫太太), the Guangzhou liaison-station couple,
  and Old Xiao (老肖), the Ruijin courier -- all fictional. Lu Zhongde (卢忠德) and Secretary Ouyang
  Min (欧阳民), from Mrs. Mo's story, apparently fictional. Real: Deng Zhongxia (邓中夏), Chen Jitang
  (陈济棠), Zhu Huiri (朱晖日), Rou Shi (柔石), Tao Yuanqing (陶元庆).
- Places: Shamian (沙面), Dashatou (大沙头), Gujiazhai Park (顾家宅公园 -> Fuxing Park), the People's
  Palace (平民宫), Jianglan Street (浆栏街), Shuangmendi (双门底), Gaodi Street (高第街) -- all real;
  the Maochang Coal Company (茂昌煤号), the Xingchang Apothecary (兴昌药号), the Tiannan Teahouse
  (添男茶楼) and the Nanhua Building (南华楼) fictional / local-color settings.
- Orgs: the Relief Society (济难会, real), the strike Labour College (劳动学院, real), the French
  Concession Municipal Council (公董局, real), the Sincere Company (先施公司, real), the Guangzhou
  Republican Daily (广州民国日报, real).
- Terms: February (二月, Rou Shi's novella); the Hao cipher (豪密); the hanging-bell flower (吊钟花);
  bamboo-tube house (竹筒屋); Manchu windows (满洲窗); arcade (骑楼); stove-cat (煨灶猫).
- Consistency: 交通站 settled as "liaison station", 交通局 as "Liaison Bureau", 机要交通员 as
  "secret courier" (matching the established 特工总部 = "Special Operations Headquarters" from ch03).

## What is NEXT

- B07 = ch21-ch22 (The Tanglong Door, The Tiannan Teahouse). Then B08 = ch23-ch25, and so on
  through B12 = ch34-ch37 (book.json "batches").

## Open items for the read-through

- Publisher discrepancy for the colophon: the copyright leaf prints 上海文化出版社, but the ISBN
  prefix and the Weibo/WeChat handles are 上海文艺出版社. Confirm before back_matter.json /
  the colophon is finalized (back_matter.json still empty).
- The painting: named and footnoted at ch15 (Wang Ximeng's 千里江山图, spoken as the passphrase).
  Do NOT re-note the painting when the name recurs.
- The "Mr. Song's brother" / T. V. Soong reading (ch17) is footnoted as an invited inference, not
  stated by the text; keep that framing if the Song family recurs.
- Long Dong (龙冬): the novel's mystery is whether he is dead. ch20's Mrs. Mo insists he survived
  the Guangzhou wreck; keep his rescue-story figures (Lu Zhongde, Ouyang Min) marked fictional.
- Provisional English titles to settle in the glossary as their chapters arrive: Garrick (茄力克,
  ch23; already glossed as the cigarette brand), Jiaoli (角里, ch25), Xiaotaoyuan (小桃源, ch28),
  The Guisheng (贵生轮, ch26). The Tanglong Door (趟栊门, ch21) and Tiannan Teahouse (添男茶楼, ch22)
  are next: 趟栊 is the Cantonese sliding-slat door; 添男茶楼 is glossed "the Tiannan Teahouse" from B06.
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
