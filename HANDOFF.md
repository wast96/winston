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
B08 (ch23-ch25), B09 (ch26-ch27) and B10 (ch28-ch30) are done.

First: data/src/ is regenerable and gitignored, so if it is missing run
scripts/ingest_epub.py source.epub to recreate the extracted source text.

Do Batch B11 = ch31 through ch33 end to end: ch31 墓地 (The Cemetery), ch32 牛奶棚
(The Dairy Shed), ch33 北站 (North Station). Read each unit's source from data/src/
(34_part0032.txt, 35_part0033.txt, 36_part0034.txt). Translate to the register in
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
  fixed in the prose, not waived. Clock/floor/score numbers stay figures so the count
  survives (一比零 -> "one to nil"; 二楼 -> "the second floor"). In B10 these
  non-quantities went to check_noise.txt: 八仙桥, 四分五裂, 成千上百, 王八蛋, 千爱; and
  check_numbers.py gained "nil"/"zero"=0 in WORD_NUM so the football score is accounted.
  Do NOT revert any existing check_numbers.py patches.

Footnotes are a RICH, fact-checked apparatus (the commissioner asked for a lot):
- Annotate real places, people, institutions and cultural references generously, and say
  in each note whether the thing is REAL history or the novel's invention, and whether the
  claim is corroborated / uncorroborated / contradicted. Fact-check against real
  scholarship (Wikipedia, Baidu Baike, academic/government sources). NEVER cite Grok,
  Grokipedia, or any AI-written source. Use subagents with web access for the research.
- Anchors must be verbatim substrings of the English prose; recurring subjects get their
  note at FIRST appearance in the book, so CHECK glossary.json and notes.json before
  re-noting something already covered (grep the reading files for a term's first appearance
  before footnoting it). 195 notes are already placed. Among those, added in B10: Chiang's
  攘外必先安内 slogan; the extra-settlement road disputes (越界筑路 / the Lai'an Li case);
  Huangniqiang (real peach locality) vs. the fictional garden Xiaotaoyuan; the Zhuangyuanlou /
  Ningbo tangyuan (with a 1938-dating caveat); the 藏兵洞 soldiers' shelter-vault at the Shence
  Gate; the Third Party / Deng Yanda; the Laozi "straw dogs" quotation (Dao De Jing ch.5); the
  National Products Market; the French tramway "no second class" detail (flagged uncorroborated);
  the Uchiyama Bookstore; Chiai-li and its cherry-blossom folk etymology (flagged); Ma Zhenhua
  (the 1928 suicide and its stage drama); the Settlement football scene / Scotto Cup / Jinan
  University; the Zhengjia wooden bridge; the Lantern Festival; Hart Road / Robert Hart;
  standard-gold speculation (标金); the Yangzhou "Three Heads" of Huaiyang cuisine. Do NOT
  re-note (already placed): Zhaojiabang (ch11), the Shence Gate as a place (ch05 Xuanwu Lake),
  Hongkou Park (ch09), the Women's Normal University / Duan Qirui (ch26), The Guide/向导 (ch04),
  Bukharin's ABC of Communism (ch16), Dai Jitao (ch22), Chen Guofu/Chen Lifu (ch13), the 1927
  April Twelfth purge (ch09), Nekrasov (ch12), Miss Tao (ch04), the Zhanyuan (ch03), the Party
  Affairs Investigation Section (ch03), the Wusong bar (ch07), Whampoa (ch23), the China Merchants
  Steam Navigation Co. (ch02). Note bodies are XHTML with NUMERIC character references (&#8212;,
  &#160;, &#8211;), never named entities; use LITERAL curly quotes and LITERAL Chinese characters
  as the existing notes do. Write Chinese into JSON via a file/Python and re-read to verify (in
  B10 two mangled glyphs -- 攢 for 攘, 鱢 for 鲢 -- were typed and caught on re-read; always
  re-read). Add new glossary rows (one rendering per referent, decided before romanizing; real =
  "attested" with the fact, fictional cast marked so).

Rendering consistency (one rendering per referent -- check glossary.json AND grep earlier reading
files before you romanize or coin an English term). Established renderings that carry forward:
陈千里 = "Chen Qianli"; 陈千元 = "Chen Qianyuan" (his brother); 卢忠德 = "Lu Zhongde" (= the
cover-name "易君年"/"Yi Junnian" = Ye Qinian's mole "西施"/"Xi Shi"; the real Yi Junnian was the dead
龙冬/Long Dong); 叶启年 = "Ye Qinian" (叶主任 = "Director Ye", 叶老师 = "Teacher Ye"); 游天啸 = "You
Tianxiao" (游队长 = "Captain You"); 林石 = "Lin Shi"; 李汉 = "Li Han"; 梁士超 = "Liang Shichao";
凌汶 = "Ling Wen" (凌太太 = "Mrs. Ling"; missing, presumed killed); 崔文泰 = "Cui Wentai"; 老肖 =
"Old Xiao"; 老方 = "Old Fang"; 董慧文 = "Dong Huiwen" (Chen Qianyuan's love, a teacher); 董师傅 =
"Master Dong" (her father, the Yangzhou chef); 莫少球 = "Mo Shaoqiu", 莫太太 = "Mrs. Mo"; 浩瀚同志 =
"Comrade Haohan" (deep underground, reachable only through Lu; the prize Chen must save); 少山同志 =
"Comrade Shaoshan"; 叶桃 = "Ye Tao" (Ye Qinian's dead daughter, Chen's love -- ch26/ch28 backstory);
孟老 = "Old Meng" (the retired assassin at Xiaotaoyuan); 小凤凰 = "Little Phoenix"; 特工总部 = "the
Special Operations Headquarters"; 侦缉队 = "the detective squad"; 淞沪警备司令部 = "the Songhu
Garrison Command"; 瞻园 = "the Zhanyuan"; 神策门 = "the Shence Gate"; 党务调查科 = "the Party Affairs
Investigation Section"; 兴昌药号 = "the Xingchang Apothecary"; 交通站 = "liaison station";
保管库/保管箱 = "vault / safe-deposit box"; 小桃源 = "Xiaotaoyuan" (glossed "Little Peach Spring").
Where B10 ends: on the eve of the Lantern Festival Ye Qinian has sprung his net -- You Tianxiao's
squad has arrested Chen Qianyuan and Dong Huiwen at Master Dong's dinner; Chen Qianli, having cut
his way out of the dyeworks and the Zhaojiabang coal-yard ambush, has reached the pinned Lin Shi
and Li Han (a shot fired at close range between two bodies as the chapter cuts off). B11 (墓地 /
牛奶棚 / 北站) presumably follows the operation to extract Haohan and the closing moves; read the
source and confirm before romanizing new place-names (墓地 a cemetery; 牛奶棚 a dairy shed; 北站 =
the North Railway Station, already in play as the Zhabei station).

Scene typography (keep it up): the source carries NO typographic scene dividers. It heads some
scenes with a terse time/place line, and hard-cuts the rest. Add entries to scenes.json for each
new chapter: "datelines" lists those terse scene-header lines VERBATIM (rendered centered), and
"breaks" lists the opening words of paragraphs that begin a new scene at a hard cut with no
dateline (a centered divider is inserted before them). A paragraph that opens on dialogue uses the
leading curly quote in its break anchor (the builder matches startswith). Verify each string
against the reading file, then confirm the built EPUB shows the expected number of breaks (grep
class="brk" in the unzipped chapter xhtml). B10: ch28 0 datelines + 2 breaks, ch29 0+0, ch30 0+3.
ch31-ch33 may or may not have breaks; check.

Run the CLAUDE.md checks including blind double-translation on the argumentative/literary passages
and a back-translation omission pass (use subagents in separate contexts); record what ran in
PROGRESS.md.

Then rebuild: scripts/build_reading_epub.py out/thousand-li.epub, and run
scripts/qa_epub.py out/thousand-li.epub until green (it refuses on an unmatched note anchor).
Commit to claude/thousand-li and push. Rewrite HANDOFF.md so its first section is the paste-ready
kickoff for Batch B12 (ch34-ch37, the last batch: ch34 Fish Congee, ch35 The Huangpu River, ch36
An Unsigned Letter, ch37 Appendix). Cite chapters, never page numbers. Never invent bridging text;
footnote any genuine ambiguity and leave it visible. Do not pause for approval mid-batch.

When you finish the batch, your final chat reply MUST contain BOTH of these, every time, so I can
start the next batch from a fresh chat: (1) the built out/thousand-li.epub attached as a file, and
(2) the next batch's paste-ready kickoff message pasted VERBATIM inside a fenced code block, right
here in the chat. Writing it into HANDOFF.md or pointing me there is NOT enough. No batch is
complete without both.
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
- Batch B09 = ch26-ch27 (The Guisheng, The Gonghexiang Wharf): done; 176 notes.
- Batch B10 = ch28-ch30 (Xiaotaoyuan, The Dyeworks Drying Ground, The Yangzhou Master): done; 195
  notes (19 new). ch28 is the villain's backstory: Ye Qinian at his hidden peach garden Xiaotaoyuan
  confesses the whole Ye Tao affair to the retired assassin Old Meng (the Beiping years, the
  Guangzhou cipher leak, the killer he set on Chen, her death in a shelter-vault at the Shence Gate),
  closing on his Laozi "straw dogs" creed. ch29 is Chen Qianli's escape from the Menghua Street trap
  over the dyeworks drying ground and his fight through the Zhaojiabang coal-yard ambush to Lin Shi
  and Li Han. ch30 is the lovers' day of Chen Qianyuan and Dong Huiwen (Hongkou Park, the Scotto Cup,
  the Ma Zhenhua-play flashback) ending in the Yangzhou master's Three Heads dinner and their arrest
  by You Tianxiao's squad. See PROGRESS.md.

## Tooling in place

- scripts/make_bilingual.py, split_bilingual.py: the translation pipeline (verbatim source,
  paragraph parity). check_noise.txt: project noise for check_numbers.py (ALWAYS pass
  --noise check_noise.txt); extend when a name/idiom with a digit is flagged. B10 added
  八仙桥, 四分五裂, 成千上百, 王八蛋, 千爱.
- scenes.json: per-chapter "datelines" and "breaks". Add an entry for every new chapter (empty
  arrays are fine for single-scene chapters). Break anchors for dialogue-opening paragraphs must
  include the leading curly quote.
- scripts/build_reading_epub.py supports datelines, scene breaks, the epigraph and a book.json
  "translator_note". Do not revert.
- scripts/check_numbers.py keeps its patches (B01 clock times / teen ordinals; B03 negative
  lookbehind on the 一[日夜时…] idiom stripper; B04 twentieth/twenty-first/twenty-second;
  B06 "thirteenth"; B07 negative lookbehind on the 一[天次年…] measure stripper and a
  "<ones> hundred and <tens> thousand" composite; B08 "twelfth":12; B09 the optional ones-digit
  prefix on the "X十多" stripper; B10 "nil"/"zero":0 for a football score). Do not revert.

## Renderings settled this batch (full ledger in glossary.json)

- People: 孟老 Old Meng (fictional), 董师傅 Master Dong (fictional), 邓演达 Deng Yanda (real),
  穆处长 Section Chief Mu (fictional).
- Places (real): 黄泥墙 Huangniqiang, 千爱里 Chiai-li, 赫德路 Hart Road, 郑家木桥 the Zhengjia
  wooden bridge, 界路 Boundary Road. Fictional: 小桃源 Xiaotaoyuan ("Little Peach Spring").
- Orgs (real): 内山书店 the Uchiyama Bookstore, 法商电车公司 the French tramway company,
  暨南大学 Jinan University.
- Terms (real): 标金 standard gold, 第三党 the Third Party, 越界筑路 extra-settlement road building,
  攘外必先安内 Chiang's slogan; 藏兵洞 soldiers' shelter-vault.

## What is NEXT

- B11 = ch31-ch33 (The Cemetery, The Dairy Shed, North Station). Then B12 = ch34-ch37, the LAST
  batch (Fish Congee, The Huangpu River, An Unsigned Letter, Appendix). On the last batch, do any
  back matter and a whole-book QA pass and write a completion report instead of another handoff.

## Open items for the read-through

- Publisher discrepancy for the colophon: the copyright leaf prints 上海文化出版社, but the ISBN
  prefix and the Weibo/WeChat handles are 上海文艺出版社. Confirm before back_matter.json /
  the colophon is finalized (back_matter.json still empty).
- The painting: named and footnoted at ch15 (Wang Ximeng's 千里江山图). Do NOT re-note it.
- Identity fully resolved for the reader (Lu Zhongde = the Shanghai "Yi Junnian" = Ye Qinian's
  "Xi Shi"; the real Yi Junnian was the murdered Long Dong). Ye Tao's death now told in full from
  Ye Qinian's side (ch28). Keep Cui Wentai's death (ch25), Long Dong's death (ch21), Ye Tao's
  death (ch26/ch28) established.
- The "Mr. Song's brother" / T. V. Soong reading (ch17) is footnoted as an invited inference; keep
  that framing if the Song family recurs.
- ch36 (An Unsigned Letter) is styled "遗物" (a martyr's relic); ch37 (Appendix) frames the fiction
  as recovered history. Fact-check its named people/places/dates against real scholarship (rule 5)
  as they arrive.

## State / traps

- book.json is the LOGICAL structure. ch01 is an epigraph (kind:"epigraph"), NOT a chapter.
- The Appendix (ch37) is ONE chapter with two sections (ch37s01, ch37s02) from two source files;
  its reading.md uses "### " headings.
- The source carries NO footnotes of its own and NO typographic scene dividers; every note is the
  translator's, and scene datelines/breaks are supplied via scenes.json.
- Note anchors are inserted BEFORE markup substitution and must be verbatim substrings of the
  English prose. Note bodies are XHTML with NUMERIC character references for dashes/nbsp, LITERAL
  curly quotes and LITERAL Chinese. A chapter H1 title cannot carry a note. Write Chinese into JSON
  via a file/Python and re-read to verify (B10 caught 攢->攘 and 鱢->鲢 that way).
- Deliverable filename is out/thousand-li.epub. Work stays on branch claude/thousand-li.
  data/src/ and out/*_bilingual.md and out/*.epub are gitignored; out/*_reading.md,
  out/*_en.json, data/zh/*.txt, scenes.json, notes.json, glossary.json are tracked.
