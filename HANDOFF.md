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
B03 (ch09-ch11), B04 (ch12-ch14), B05 (ch15-ch17), B06 (ch18-ch20), B07 (ch21-ch22),
B08 (ch23-ch25) and B09 (ch26-ch27) are done.

First: data/src/ is regenerable and gitignored, so if it is missing run
scripts/ingest_epub.py source.epub to recreate the extracted source text.

Do Batch B10 = ch28 through ch30 end to end: ch28 小桃源 (Xiaotaoyuan), ch29 染坊晒场
(The Dyeworks Drying Ground), ch30 扬州师傅 (The Yangzhou Master). Read each unit's source
from data/src/ (31_part0029.txt, 32_part0030.txt, 33_part0031.txt). Translate to the register
in CLAUDE.md: clean flowing English prose, the novel's own voice, all apparatus in footnotes,
never inline.

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
  fixed in the prose, not waived. In B09 these non-quantities went to check_noise.txt:
  二十年代, 零食, 零钱, 五金, 百老汇, 两个字; and check_numbers.py's "十多" stripper was
  extended to an optional ones-digit prefix so "X十多" (五十多/三十多) strips whole instead
  of orphaning a stray 5/3 (this only removes source numerals, never masks a drop). Clock/
  floor/knot numbers stay figures so the count survives (十点五十分 -> "fifty minutes past
  ten"; 二楼 -> "the second floor"). Do NOT revert existing check_numbers.py patches.

Footnotes are a RICH, fact-checked apparatus (the commissioner asked for a lot):
- Annotate real places, people, institutions and cultural references generously, and say
  in each note whether the thing is REAL history or the novel's invention, and whether the
  claim is corroborated / uncorroborated / contradicted. Fact-check against real
  scholarship (Wikipedia, Baidu Baike, academic/government sources). NEVER cite Grok,
  Grokipedia, or any AI-written source. Use subagents with web access for the research.
- Anchors must be verbatim substrings of the English prose; recurring subjects get their
  note at FIRST appearance in the book, so CHECK glossary.json and notes.json before
  re-noting something already covered (grep the reading files for a term's first appearance
  before footnoting it). Among the ~176 already noted, added in B09: the 1925 dissolution of
  the Beijing Women's Normal University (real; Duan Qirui government via minister Zhang Shizhao,
  Lu Xun's involvement); Zhaofeng Garden = Jessfield Park (兆丰花园, real, opened 1914 -- the
  swans are the novel's own touch, flagged uncorroborated); the anarchist-to-Marxist reading
  drift (Pushkin's Captain's Daughter, Kropotkin's 告少年/An Appeal to the Young, 新青年/New
  Youth, Bakunin vs Lenin, the 1920 Chen Wangdao 共产党宣言, Lenin's 1917 远方来信/Letters from
  Afar, the CCP journal 布尔塞维克/Bolshevik 1927-32); Plum Blossom Hill (梅花山, real, over Sun
  Quan's tomb, plums from 1929); the Nationalist right / First United Front + Western Hills
  faction (real backdrop, Ye Qinian's speech invented); the Gonghexiang Wharf (公和祥码头, real
  North-Bund dock, ch27 title); East Broadway (东百老汇路) and its real wharf firms (汇山/Wayside,
  日本邮船/N.Y.K., 耶松/Yehsong, 顺泰/Shuntai); Shanghai borscht (罗宋汤); Cantonese 靓 "leng." Do
  NOT re-note: the Zhanyuan (瞻园, ch03/ch05), the Party Affairs Investigation Section (党务调查科,
  ch03), Nekrasov (ch12), Esperanto (ch12), the China Merchants Steam Navigation Co. (招商局,
  ch02), Duanwu (端午/午时符, ch23), the Wusong bar (吴淞口, ch07), Jardine (怡和, ch21), Xi Shi
  (ch03), Whampoa (ch23), Dianshan Lake / Zhujiajiao (ch25). Note bodies are XHTML with NUMERIC
  character references (&#8212;, &#160;, &#8211;), never named entities; use literal curly quotes
  as the existing notes do. Add new glossary rows (one rendering per referent, decided before
  romanizing; real = "attested" with the fact, fictional cast marked so).

Rendering consistency (one rendering per referent -- check glossary.json AND grep earlier reading
files before you romanize or coin an English term). Established renderings that carry into these
chapters: 陈千里 = "Chen Qianli"; 陈千元 = "Chen Qianyuan" (his brother); 卢忠德 = "Lu Zhongde"
(= the cover-name "易君年"/"Yi Junnian" = Ye Qinian's mole "西施"/"Xi Shi"; real Yi Junnian was the
dead 龙冬/Long Dong -- established ch26-27); 叶启年 = "Ye Qinian" (叶主任 = "Director Ye", 叶老师 =
"Teacher Ye"); 游天啸 = "You Tianxiao" (游队长 = "Captain You"); 林石 = "Lin Shi"; 梁士超 = "Liang
Shichao"; 凌汶 = "Ling Wen" (missing, presumed killed); 老肖 = "Old Xiao"; 莫少球 = "Mo Shaoqiu",
莫太太 = "Mrs. Mo"; 浩瀚同志 = "Comrade Haohan" (deep underground, reachable only through Lu; the
prize Chen must save); 少山同志 = "Comrade Shaoshan"; 叶桃 = "Ye Tao" (Ye Qinian's dead daughter,
Chen's love -- ch26 backstory); 小凤凰 = "Little Phoenix"; 特工总部 = "the Special Operations
Headquarters"; 侦缉队 = "the detective squad"; 淞沪警备司令部 = "the Songhu Garrison Command";
瞻园 = "the Zhanyuan"; 党务调查科 = "the Party Affairs Investigation Section"; 兴昌药号 = "the
Xingchang Apothecary"; 交通站 = "liaison station"; 保管库/保管箱 = "vault / safe-deposit box".
Where B09 ends: Chen has docked at the Gonghexiang Wharf and is playing Lu Zhongde -- he has asked
Lu to hire a small two-or-three-hundred-ton cargo boat and to find a big, secret safe house for
"the next few days" (the operation to extract Haohan), while Lu, watched over by Ye Qinian's men
and a rooftop marksman, feeds Chen a rehearsed lie about Ling Wen's disappearance in Guangzhou.
B10 (小桃源 / 染坊晒场 / 扬州师傅) presumably follows the safe-house/boat operation; read the source
and confirm before romanizing 小桃源 (a Shanghai place-name -- check whether it is the real 小桃园
locale) and 扬州师傅 (a Yangzhou tradesman -- barber/bath trade?).

Scene typography (keep it up): the source carries NO typographic scene dividers. It heads
some scenes with a terse time/place line, and hard-cuts the rest. Add entries to scenes.json
for each new chapter: "datelines" lists those terse scene-header lines VERBATIM (rendered
centered), and "breaks" lists the opening words of paragraphs that begin a new scene at a
hard cut with no dateline (a centered divider is inserted before them). Verify each string
against the reading file, then confirm the built EPUB shows the expected number of breaks
(grep 'class="brk"' in the unzipped chapter xhtml). B09: ch26 had 0 datelines + 2 breaks (into
the Guangzhou flashback of Old Xiao's message; into the long Ye Tao memory); ch27 had 0
datelines + 1 break (the cut from the night cabin to the mid-morning wharf arrival). A paragraph
that opens on dialogue uses the leading curly quote in its break anchor (the builder matches
startswith). ch28-ch30 may or may not have breaks; check.

Run the CLAUDE.md checks including blind double-translation on the argumentative/literary
passages and a back-translation omission pass (use subagents in separate contexts);
record what ran in PROGRESS.md.

Then rebuild: scripts/build_reading_epub.py out/thousand-li.epub, and run
scripts/qa_epub.py out/thousand-li.epub until green (it refuses on an unmatched note
anchor). Commit to claude/thousand-li and push. Rewrite HANDOFF.md so its first section
is the paste-ready kickoff for Batch B11 (ch31-ch33). Cite chapters, never page numbers.
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
- Batch B08 = ch23-ch25 (Garrick, Backstage, Jiaoli): done; 165 notes. The reveal batch.
- Batch B09 = ch26-ch27 (The Guisheng, The Gonghexiang Wharf): done; 176 notes (11 new). ch26 is
  the Ye Tao backstory (aboard the Jardine liner Guisheng, Chen relays the dying Old Xiao's
  advertisement-signal message for the underground Haohan, entrusted to "Yi Junnian," then recalls
  Ye Tao's arc from Ye Qinian's Xinzha-Road anarchist salon to her death inside the Party Affairs
  Investigation Section at the Zhanyuan, hunting the answer to whether Ouyang Min turned traitor).
  ch27: Chen and Liang Shichao work out that the man killed on Haoxian Road was the REAL Yi Junnian
  (Long Dong) and that Lu Zhongde usurped the alias; Chen must NOT expose or kill Lu yet, because Lu
  is the only line to the endangered Haohan. The Guisheng docks at the Gonghexiang Wharf; Chen meets
  Lu under Ye Qinian's guns and plays a counter-theatre (asking for a hired cargo boat and a safe
  house) while Lu tells his rehearsed lie about Ling Wen. See PROGRESS.md.

## Tooling in place

- scripts/make_bilingual.py, split_bilingual.py: the translation pipeline (verbatim source,
  paragraph parity). check_noise.txt: project noise for check_numbers.py (ALWAYS pass
  --noise check_noise.txt); extend when a name/idiom with a digit is flagged. B09 added
  二十年代, 零食, 零钱, 五金, 百老汇, 两个字.
- scenes.json: per-chapter "datelines" and "breaks". Add an entry for every new chapter (empty
  arrays are fine for single-scene chapters). Break anchors for dialogue-opening paragraphs must
  include the leading curly quote.
- scripts/build_reading_epub.py supports datelines, scene breaks, the epigraph and a book.json
  "translator_note". Do not revert.
- scripts/check_numbers.py keeps its patches (B01 clock times / teen ordinals; B03 negative
  lookbehind on the 一[日夜时…] idiom stripper; B04 twentieth/twenty-first/twenty-second;
  B06 "thirteenth"; B07 negative lookbehind on the 一[天次年…] measure stripper and a
  "<ones> hundred and <tens> thousand" composite; B08 "twelfth":12; B09 the optional ones-digit
  prefix on the "X十多" stripper). Do not revert.

## Renderings settled this batch (full ledger in glossary.json)

- People: 段祺瑞 Duan Qirui (real). (叶桃 Ye Tao, 欧阳民 Ouyang Min, 浩瀚 Haohan, 少山 Shaoshan,
  莫少球/莫太太 were already in the ledger.)
- Places (real): 兆丰花园 Zhaofeng Garden (Jessfield Park), 梅花山 Plum Blossom Hill, 秦淮河 the
  Qinhuai River, 栖霞山 Qixia Hill, 石婆婆巷 Shipopo Lane, 道署街 Daoshu Street, 马府街 Mafu Street,
  舟山群岛 the Zhoushan Archipelago, 公和祥码头 the Gonghexiang Wharf, 东百老汇路 East Broadway.
- Orgs (real): 怡和公司 the Jardine company, 汇山码头 the Wayside Wharf, 日本邮船会社 the Japan Mail
  Steamship Company (N.Y.K.), 耶松船厂 the Yehsong Dockyard, 顺泰码头 the Shuntai Wharf,
  北京女子师范大学 the Beijing Women's Normal University.
- 吴淞口 renders "the Wusong bar" (established ch07); 瞻园 "the Zhanyuan" (ch03).

## What is NEXT

- B10 = ch28-ch30 (Xiaotaoyuan, The Dyeworks Drying Ground, The Yangzhou Master). Then
  B11 = ch31-ch33, B12 = ch34-ch37 (book.json "batches").

## Open items for the read-through

- Publisher discrepancy for the colophon: the copyright leaf prints 上海文化出版社, but the ISBN
  prefix and the Weibo/WeChat handles are 上海文艺出版社. Confirm before back_matter.json /
  the colophon is finalized (back_matter.json still empty).
- The painting: named and footnoted at ch15 (Wang Ximeng's 千里江山图). Do NOT re-note it.
- Identity fully resolved for the reader (Lu Zhongde, faked-dead Guangzhou constable = the
  Shanghai "Yi Junnian" = Ye Qinian's "Xi Shi"; the real Yi Junnian was the murdered Long Dong).
  Do NOT re-note Xi Shi (ch03). Keep Cui Wentai's death (ch25), Long Dong's death (ch21), Ye Tao's
  death (ch26 backstory) established.
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
  to verify (in B09 two wrong glyphs -- 祇 for 祺, 栋 for 栖 -- were typed into the apparatus script
  and caught and fixed before running; always re-read).
- Deliverable filename is out/thousand-li.epub. Work stays on branch claude/thousand-li.
  data/src/ and out/*_bilingual.md and out/*.epub are gitignored; out/*_reading.md,
  out/*_en.json, data/zh/*.txt, scenes.json, notes.json, glossary.json are tracked.
