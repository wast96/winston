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
B03 (ch09-ch11), B04 (ch12-ch14), B05 (ch15-ch17), B06 (ch18-ch20) and B07 (ch21-ch22)
are done.

First: data/src/ is regenerable and gitignored, so if it is missing run
scripts/ingest_epub.py source.epub to recreate the extracted source text.

Do Batch B08 = ch23 through ch25 end to end: ch23 茄力克 (Garrick), ch24 后台
(Backstage), ch25 角里 (Jiaoli). Read each unit's source from data/src/
(26_part0024.txt, 27_part0025.txt, 28_part0026.txt). Translate to the register in
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
  fixed in the prose, not waived. In B07 the street names 十八甫/下九甫, the idioms
  四四方方/四方/两样, the name 七姑, and 九龙/零散/零碎 went to check_noise.txt as
  non-quantities; clock/floor numbers (中午十二点 -> "twelve o'clock", 二楼 -> "second
  floor") were kept as figures so the count survives. If a compound English word-numeral
  the checker cannot parse is flagged, extend WORD_NUM / spelled_numbers in
  scripts/check_numbers.py, as B04/B06/B07 did (B07 added a "<ones> hundred and <tens>
  thousand" composite for 二十五万 -> "two hundred and fifty thousand", and a negative
  lookbehind on the 一[天次年…] measure stripper so 十一天 -> 11 survives; do NOT revert
  existing patches).

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
  first appearance before footnoting it). Among the ~146 already noted, recently added in B07:
  Haoxian Road / 濠弦街 ("Moat-Bowstring," real; renamed to honor Li Suiqiu) and the fictional
  Tianguan Li address on it; the Wong Tai Sin oracle-lots (real deity/practice, but the novel's
  lot-73 verse is INVENTED -- real lot 73 is auspicious); Cao Song's "one general's fame is built
  on ten thousand rotting bones"; the self-combed women / amahs of Shunde (七姑); the Cantonese
  fo sui (kerosene); the tanglong door (趟栊门, the ch21 title) and the wok-ear gables (镬耳墙);
  the Haizhu Bridge (1933); the oracle's 东施效颦 / 西子 / 郭索 pun that names Xi Shi to Yi
  Junnian's face; the Da Mei Wan Bao (Chinese ed. 16 Jan 1933); the naamyam 客途秋恨 with its
  female xiaosheng and 缪莲仙 / Peach-Blossom-Spring lines; the枪牌 Browning (FN M1900); the
  Reflection Institute (反省院); Liao Zhongkai (shot 20 Aug 1925; the Ye Qinian tie is fiction);
  Dai Jitao / Daiism; the 1924 chronology (Feng Yuxiang jails Cao Kun, Sun goes north). Do NOT
  re-note: Xi Shi (ch03), Shen Bao (ch07), the Canton-Hong Kong Strike (ch15), Bo Gu / the 1933
  Ruijin move (ch13), the courier lines / Kowloon radio (ch15), Haohan (ch04), Chen Jitang /
  "King of the Southern Sky" (ch20), February / Rou Shi (ch19), the Yiddish tumbalalaika (ch09),
  Esperanto (ch12). Note bodies are XHTML with NUMERIC character references (&#8212;, &#160;,
  &#183;), never named entities. Add new glossary rows (one rendering per referent, decided before
  romanizing; real = "attested" with the fact, fictional cast marked so).

Rendering consistency (one rendering per referent -- check glossary.json AND grep earlier reading
files before you romanize or coin an English term). Established renderings that recur into these
chapters: 交通线 = "courier line"; 交通站 = "liaison station"; 交通局 = "Liaison Bureau"; 机要交通员
= "secret courier"; 特工总部 = "the Special Operations Headquarters"; 侦缉队 = "the detective squad";
省港大罢工 = "the Canton-Hong Kong Strike"; 广州起义 = "the Guangzhou Uprising" (the KMT press voice
广州暴动 was rendered "the Guangzhou revolt"); 少山 = "Comrade Shaoshan" (Zhou Enlai); 西施 = "Xi Shi";
叶启年 = "Ye Qinian" (as 叶老师 = "Teacher Ye", as 叶主任 = "Director Ye"); 游天啸 = "You Tianxiao";
龙冬 = "Long Dong"; 凌汶 = "Ling Wen"; 易君年 = "Yi Junnian"; 老肖 = "Old Xiao"; 莫少球 = "Boss Mo".
NOTE for B08+: 茄力克 (ch23) is the Garrick cigarette brand (already glossed); 角里 (ch25) = "Jiaoli".

Scene typography (keep it up): the source carries NO typographic scene dividers. It heads
some scenes with a terse time/place line, and hard-cuts the rest. Add entries to scenes.json
for each new chapter: "datelines" lists those terse scene-header lines VERBATIM (rendered
centered), and "breaks" lists the opening words of paragraphs that begin a new scene at a
hard cut with no dateline (a centered divider is inserted before them). Verify each string
against the reading file, then confirm the built EPUB shows the expected number of breaks
(grep 'class="brk"' in the unzipped chapter xhtml). B07 had ch21 2 breaks (arrival at Haoxian
Road; the post-murder coda) and ch22 0 (one continuous run, teahouse to boat, like ch20). A
paragraph that opens on dialogue uses the leading curly quote in its break anchor (the builder
matches startswith). ch23-ch25 may or may not have breaks; check.

Run the CLAUDE.md checks including blind double-translation on the argumentative/literary
passages and a back-translation omission pass (use subagents in separate contexts);
record what ran in PROGRESS.md.

Then rebuild: scripts/build_reading_epub.py out/thousand-li.epub, and run
scripts/qa_epub.py out/thousand-li.epub until green (it refuses on an unmatched note
anchor). Commit to claude/thousand-li and push. Rewrite HANDOFF.md so its first section
is the paste-ready kickoff for Batch B09 (ch26-ch27). Cite chapters, never page numbers.
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
- Batch B06 = ch18-ch20 (The Maochang Coal Company, February, The Xingchang Apothecary): done; 130 notes.
- Batch B07 = ch21-ch22 (The Tanglong Door, The Tiannan Teahouse): 217 paragraphs (ch21 161, ch22 56);
  parity and number checks clean; blind double-translation and back-translation/faithfulness audits
  confirm the text; 16 new footnotes taking the book to 146. ch21 is the hinge of the novel: Ling Wen's
  search in Guangzhou for Long Dong leads to the crime-scene house on Haoxian Road, and Yi Junnian --
  cold, sleepless, watched by a Long Dong who is not there -- reveals himself through the photograph
  (he swore his Party oath there, with Long Dong as sponsor, then killed him and took the picture),
  murders Ling Wen off-page (the blood on his hands), and strangles the diviner who names "Xi Shi" to
  his face. ch22 confirms it: Old Xiao (the Ruijin courier carrying an oral order about Comrade Haohan)
  is ambushed at the teahouse in a piece staged by Yi Junnian, who is "Xi Shi," Ye Qinian's ace, planted
  under a dead man's name -- his whole Guangzhou-to-Shanghai back-story laid out. See PROGRESS.md.
- Book-wide so far: footnotes at 146, fact-checked and real-vs-fictional / corroborated-labelled;
  ch01 is a centered EPIGRAPH (kind:"epigraph"); scene typography via scenes.json + builder;
  glossary the term ledger (real "attested", fictional marked).

## Tooling in place

- scripts/make_bilingual.py, split_bilingual.py: the translation pipeline (verbatim source,
  paragraph parity). check_noise.txt: project noise for check_numbers.py (ALWAYS pass
  --noise check_noise.txt); extend when a name/idiom with a digit is flagged. B07 added
  十八甫, 下九甫, 四四方方, 四方, 七姑, 两样, 九龙, 零散, 零碎.
- scenes.json: per-chapter "datelines" (verbatim scene-header lines, rendered centered) and
  "breaks" (paragraph-opening anchors for hard cuts, get a centered divider). Add an entry for
  every new chapter (empty arrays are fine for single-scene chapters, as ch20/ch22). Break anchors
  for dialogue-opening paragraphs must include the leading curly quote.
- scripts/build_reading_epub.py supports datelines, scene breaks, the epigraph and a book.json
  "translator_note". Do not revert.
- scripts/check_numbers.py keeps its patches (B01 clock times / teen ordinals; B03 negative
  lookbehind on the 一[日夜时…] idiom stripper; B04 added twentieth/twenty-first/twenty-second;
  B06 added "thirteenth"; B07 added a negative lookbehind on the 一[天次年…] measure stripper
  so teen+measure like 十一天 keeps its 11, and a "<ones> hundred and <tens> thousand" composite
  in spelled_numbers for 二十五万 -> "two hundred and fifty thousand"). Do not revert.

## Renderings settled this batch (full ledger in glossary.json)

- People: 七姑 Qigu (fictional amah). Real: 廖仲恺 Liao Zhongkai, 戴季陶 Dai Jitao, 冯玉祥 Feng Yuxiang,
  曹锟 Cao Kun, 缪莲仙 Miao Lianxian, 黎遂球 Li Suiqiu.
- Places: 豪贤路 Haoxian Road, 光复路 Guangfu Road, 十八甫 Shibafu Street (all real); 天官里 Tianguan Li
  (fictional lane on the real Haoxian Road).
- Orgs: 大美晚报 the Da Mei Wan Bao, 反省院 the Reflection Institute, 国华报 the Guohua Bao, 广州报界公会
  the Guangzhou Press Association (all real; the Guohua Bao's two-run detail uncorroborated).
- Terms: 趟栊门 tanglong door, 自梳女 self-combed woman, 疍家 Tanka, 客途秋恨 Ke Tu Qiu Hen, 黄大仙
  Wong Tai Sin, 火水 fo sui.
- Consistency: 广州暴动 (KMT press voice) rendered "the Guangzhou revolt", distinct from the Party's
  "the Guangzhou Uprising" (广州起义, glossed); 叶主任 = "Director Ye" / 叶老师 = "Teacher Ye" (both 叶启年);
  爱人 rendered "lover" (Long Dong is Ling Wen's secret lover; her dead husband was a merchant).

## What is NEXT

- B08 = ch23-ch25 (Garrick, Backstage, Jiaoli). Then B09 = ch26-ch27, and so on through
  B12 = ch34-ch37 (book.json "batches").

## Open items for the read-through

- Publisher discrepancy for the colophon: the copyright leaf prints 上海文化出版社, but the ISBN
  prefix and the Weibo/WeChat handles are 上海文艺出版社. Confirm before back_matter.json /
  the colophon is finalized (back_matter.json still empty).
- The painting: named and footnoted at ch15 (Wang Ximeng's 千里江山图, spoken as the passphrase).
  Do NOT re-note the painting when the name recurs. The ch22 contact-signal (an advert to buy
  "old paintings and calligraphy") quietly echoes the title; left unglossed as plot, not reference.
- Xi Shi: the reveal is complete (ch22 -- Yi Junnian is the original "Xi Shi," Ye Qinian's ace;
  Cui Wentai was given the same code name in ch14 as a decoy). Do NOT re-note Xi Shi (glossed ch03).
- Long Dong (龙冬): the mystery is now resolved for the reader -- Yi Junnian killed him in Guangzhou
  and took his place. Ling Wen never learned it. Keep his death as established when it recurs.
- The "Mr. Song's brother" / T. V. Soong reading (ch17) is footnoted as an invited inference; keep
  that framing if the Song family recurs.
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
  A chapter H1 title cannot carry a note. Write Chinese into JSON via a file/Python and re-read
  to verify (a heredoc mangled four glyphs in B07; caught and fixed).
- Deliverable filename is out/thousand-li.epub. Work stays on branch claude/thousand-li.
  data/src/ and out/*_bilingual.md and out/*.epub are gitignored; out/*_reading.md,
  out/*_en.json, data/zh/*.txt, scenes.json, notes.json, glossary.json are tracked.
