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
B03 (ch09-ch11), B04 (ch12-ch14), B05 (ch15-ch17), B06 (ch18-ch20), B07 (ch21-ch22)
and B08 (ch23-ch25) are done.

First: data/src/ is regenerable and gitignored, so if it is missing run
scripts/ingest_epub.py source.epub to recreate the extracted source text.

Do Batch B09 = ch26 through ch27 end to end: ch26 贵生轮 (The Guisheng), ch27 公和祥码头
(The Gonghexiang Wharf). Read each unit's source from data/src/ (29_part0027.txt,
30_part0028.txt). Translate to the register in CLAUDE.md: clean flowing English prose,
the novel's own voice, all apparatus in footnotes, never inline.

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
  fixed in the prose, not waived. In B08 these idioms/names went to check_noise.txt as
  non-quantities: 五颜六色, 六神无主, 五花大绑, 三七二十一 (不管三七二十一), 零件; and a
  missing word-ordinal "twelfth":12 was added to WORD_NUM in scripts/check_numbers.py
  (for 正月十二 -> "the twelfth of the first month"). Clock/floor numbers stay figures so
  the count survives (中午十二点 -> "around twelve o'clock"; 晚上八点 -> "eight that
  evening"). Do NOT revert existing check_numbers.py patches.

Footnotes are a RICH, fact-checked apparatus (the commissioner asked for a lot):
- Annotate real places, people, institutions and cultural references generously, and say
  in each note whether the thing is REAL history or the novel's invention, and whether the
  claim is corroborated / uncorroborated / contradicted. Fact-check against real
  scholarship (Wikipedia, Baidu Baike, academic/government sources). NEVER cite Grok,
  Grokipedia, or any AI-written source. Use subagents with web access for the research.
- Anchors must be verbatim substrings of the English prose; recurring subjects get their
  note at FIRST appearance in the book, so CHECK glossary.json and notes.json before
  re-noting something already covered (grep the reading files for a term's first appearance
  before footnoting it). Among the ~165 already noted, added in B08: Guangzhou's Central Park
  (real; site of the 平南王府/Shang Kexi, then the governor's office; Sun proposed the park,
  opened 1921, named Central 1926); Kang Youwei's Italian sphinx statues (real man; donation
  attested only in popular sources; the sphinx recurs on the Garrick tin); Three Castles (三炮台,
  Wills, 1878) and Garrick (茄力克, Lambert & Butler, sphinx tin -- the chapter's identity clue:
  Yi Junnian smoked Garrick back in ch08); fantan (番摊); the Duanwu customs 午时符 / 洗龙舟水;
  the all-female Cantonese 女班 / huadan / xiaosheng / 包头 (群芳艳 echoes the real 群芳艳影);
  the Cantonese opera 十美绕宣王 / 背解红罗 / 苏金定; the silver-shield (银盾) patron custom;
  Whampoa Military Academy (黄埔军校, 1924); the Zhongshan Warship Incident (中山舰事件, 20 Mar
  1926 -- the constable's bomb/letter is the novel's invented spark); Little Phoenix's "胭脂用尽"
  (texture); Dianshan Lake (淀山湖); Jiaoli/Zhujiajiao (角里 = 朱家角, ch25 title; read Jiǎolǐ, NOT
  the Suzhou 甪里/Lùlǐ); Shangta (商榻, "merchants' lodging"); Songze (崧泽; the source's 菘泽 is a
  folk miswriting); the western-Shanghai roads Brenan/Warren/Rubicon/Hongqiao + Hongqiao airfield;
  the Zhu-Hu county road (珠沪县道); straw-tied pork (稻草扎肉). Do NOT re-note: Xi Shi (ch03),
  Haoxian Road / Moat-Bowstring (ch21), Shamian (ch20), the Sincere rooftop garden (ch20), Dashatou
  (ch20), the Reflection Institute (ch22), Longhua (ch03), North Sichuan Road (ch07). Note bodies
  are XHTML with NUMERIC character references (&#8212;, &#160;, &#183;), never named entities. Add new
  glossary rows (one rendering per referent, decided before romanizing; real = "attested" with the
  fact, fictional cast marked so).

Rendering consistency (one rendering per referent -- check glossary.json AND grep earlier reading
files before you romanize or coin an English term). Established renderings that recur into these
chapters: 贵生轮 = "the Guisheng"; 公和祥码头 = "the Gonghexiang Wharf" (both already appear at the
end of ch25, spoken by Ye Qinian setting the ambush); 特工总部 = "the Special Operations Headquarters";
侦缉队 = "the detective squad"; 淞沪警备司令部 = "the Songhu Garrison Command"; 站长 = "station chief";
陈千里 = "Chen Qianli"; 易君年 = "Yi Junnian"; 叶启年 = "Ye Qinian" (叶主任 = "Director Ye", 叶老师 =
"Teacher Ye"); 游天啸 = "You Tianxiao" (游队长 = "Captain You"); 崔文泰 = "Cui Wentai" (killed at
Dianshan Lake in ch25 -- keep his death established); 卢忠德 = "Lu Zhongde" (= Yi Junnian = "Xi Shi",
revealed ch23-24); 小凤凰 = "Little Phoenix"; 保管库/保管箱 = "vault / safe-deposit box"; 天津路 =
"Tianjin Road"; 北站 = "North Station" (real Shanghai North Station -- glossed; its chapter is ch33,
note it there if warranted). The ch25 close sets up B09 directly: Chen returns to Shanghai on the
Guisheng, docks around noon at the Gonghexiang Wharf, Yi Junnian meets him, and Ye Qinian has You
Tianxiao's men and a rooftop marksman waiting -- shoot only if Chen shoots, let Yi Junnian go, take
Chen alive if possible.

Scene typography (keep it up): the source carries NO typographic scene dividers. It heads
some scenes with a terse time/place line, and hard-cuts the rest. Add entries to scenes.json
for each new chapter: "datelines" lists those terse scene-header lines VERBATIM (rendered
centered), and "breaks" lists the opening words of paragraphs that begin a new scene at a
hard cut with no dateline (a centered divider is inserted before them). Verify each string
against the reading file, then confirm the built EPUB shows the expected number of breaks
(grep 'class="brk"' in the unzipped chapter xhtml). B08: ch23 had 1 dateline (正月初十，立春)
+ 2 breaks (the flashback to the waterside shed; the return to the park gate); ch24 had 0
(one continuous evening at the Lehua theatre); ch25 had 1 break (the cut to the Zhengyuan
Hotel that evening). A paragraph that opens on dialogue uses the leading curly quote in its
break anchor (the builder matches startswith). ch26-ch27 may or may not have breaks; check.

Run the CLAUDE.md checks including blind double-translation on the argumentative/literary
passages and a back-translation omission pass (use subagents in separate contexts);
record what ran in PROGRESS.md.

Then rebuild: scripts/build_reading_epub.py out/thousand-li.epub, and run
scripts/qa_epub.py out/thousand-li.epub until green (it refuses on an unmatched note
anchor). Commit to claude/thousand-li and push. Rewrite HANDOFF.md so its first section
is the paste-ready kickoff for Batch B10 (ch28-ch30). Cite chapters, never page numbers.
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
- Batch B05 = ch15-ch17 (Code Words, The Bank, The Suitcase): done; 108 notes.
- Batch B06 = ch18-ch20 (The Maochang Coal Company, February, The Xingchang Apothecary): done; 130 notes.
- Batch B07 = ch21-ch22 (The Tanglong Door, The Tiannan Teahouse): done; 146 notes.
- Batch B08 = ch23-ch25 (Garrick, Backstage, Jiaoli): done; 165 notes (19 new). ch23-24 are the
  reveal: Chen Qianli, in Guangzhou hunting for the vanished Ling Wen and Old Xiao, traces the
  Garrick cigarette to the "dead" constable Lu Zhongde, and from the actress Little Phoenix learns
  Lu's whole story -- a KMT provocateur who faked his death (Zhongshan-Warship era), was slipped
  into the Shanghai underground as "Yi Junnian," lured Long Dong to his death, and is Ye Qinian's
  "Xi Shi." ch25 kills off Cui Wentai: he flees the gold-switch fiasco to Dianshan Lake, is caught
  by You Tianxiao at Jiaoli (the suitcase holds only coal-yard scale-weights -- Chen switched the
  gold in the bank vault), and is drowned; Ye Qinian then sets the wharf ambush for Chen's return.
  See PROGRESS.md.

## Tooling in place

- scripts/make_bilingual.py, split_bilingual.py: the translation pipeline (verbatim source,
  paragraph parity). check_noise.txt: project noise for check_numbers.py (ALWAYS pass
  --noise check_noise.txt); extend when a name/idiom with a digit is flagged. B08 added
  五颜六色, 六神无主, 五花大绑, 三七二十一, 零件.
- scenes.json: per-chapter "datelines" and "breaks". Add an entry for every new chapter (empty
  arrays are fine for single-scene chapters). Break anchors for dialogue-opening paragraphs must
  include the leading curly quote.
- scripts/build_reading_epub.py supports datelines, scene breaks, the epigraph and a book.json
  "translator_note". Do not revert.
- scripts/check_numbers.py keeps its patches (B01 clock times / teen ordinals; B03 negative
  lookbehind on the 一[日夜时…] idiom stripper; B04 twentieth/twenty-first/twenty-second;
  B06 "thirteenth"; B07 negative lookbehind on the 一[天次年…] measure stripper and a
  "<ones> hundred and <tens> thousand" composite; B08 "twelfth":12). Do not revert.

## Renderings settled this batch (full ledger in glossary.json)

- People: 小凤凰 Little Phoenix (fictional huadan). 卢忠德 Lu Zhongde note updated: = Yi Junnian =
  "Xi Shi" (the ch23-24 reveal).
- Places (real): 中央公园 Central Park (Guangzhou), 东濠涌 Donghao Creek, 淀山湖 Dianshan Lake,
  朱家角 Zhujiajiao, 商榻 Shangta, 崧泽 Songze, 青浦 Qingpu, 白利南路 Brenan Road, 华伦路 Warren Road,
  罗别根路 Rubicon Road, 虹桥路 Hongqiao Road, 虹桥机场 Hongqiao airfield, 北站 North Station.
  Decided/fictional: 乐华 the Lehua, 新亚旅社 the Xinya Hotel, 正元旅社 the Zhengyuan Hotel,
  珠沪县道 the Zhu-Hu county road.
- Orgs: 群芳艳 the Qunfangyan troupe (fictionalized; echoes real 群芳艳影); 黄埔军校 Whampoa
  Military Academy (real).
- Terms: 三炮台 Three Castles, 番摊 fantan, 花旦 huadan, 稻草扎肉 straw-tied pork, 中山舰事件 the
  Zhongshan Warship Incident, 午时符 the noon-hour charm.

## What is NEXT

- B09 = ch26-ch27 (The Guisheng, The Gonghexiang Wharf). Then B10 = ch28-ch30, B11 = ch31-ch33,
  B12 = ch34-ch37 (book.json "batches").

## Open items for the read-through

- Publisher discrepancy for the colophon: the copyright leaf prints 上海文化出版社, but the ISBN
  prefix and the Weibo/WeChat handles are 上海文艺出版社. Confirm before back_matter.json /
  the colophon is finalized (back_matter.json still empty).
- The painting: named and footnoted at ch15 (Wang Ximeng's 千里江山图). Do NOT re-note it when the
  name recurs.
- Xi Shi / Yi Junnian / Lu Zhongde: the identity is now fully resolved for the reader (Lu Zhongde,
  faked-dead Guangzhou constable = the Shanghai "Yi Junnian" = Ye Qinian's "Xi Shi"). Do NOT re-note
  Xi Shi (glossed ch03). Keep Cui Wentai's death (ch25) and Long Dong's death (ch21) established.
- The "Mr. Song's brother" / T. V. Soong reading (ch17) is footnoted as an invited inference; keep
  that framing if the Song family recurs.
- The appendix (ch37) frames the fiction as recovered history. Fact-check its named
  people/places/dates against real scholarship (rule 5) as they arrive.

## State / traps

- book.json is the LOGICAL structure. ch01 is an epigraph (kind:"epigraph"), NOT a chapter.
- The Appendix (ch37) is ONE chapter with two sections (ch37s01, ch37s02) from two source files;
  its reading.md uses "### " headings.
- The source carries NO footnotes of its own and NO typographic scene dividers; every note is the
  translator's, and scene datelines/breaks are supplied via scenes.json.
- Note anchors are inserted BEFORE markup substitution and must be verbatim substrings of the
  English prose. Note bodies are XHTML with NUMERIC character references, never named entities.
  A chapter H1 title cannot carry a note. Write Chinese into JSON via a file/Python and re-read
  to verify (in B08 four wrong glyphs -- 潠/毌/甲 -- were typed into the apparatus script and caught
  and fixed before the merge; always re-read).
- Deliverable filename is out/thousand-li.epub. Work stays on branch claude/thousand-li.
  data/src/ and out/*_bilingual.md and out/*.epub are gitignored; out/*_reading.md,
  out/*_en.json, data/zh/*.txt, scenes.json, notes.json, glossary.json are tracked.
