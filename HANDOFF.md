# HANDOFF — A Thousand Li of Rivers and Mountains (千里江山图), Sun Ganlu

## THE BOOK IS COMPLETE

All 12 batches are done: the whole novel (37 units — epigraph, 34 chapters, the
unsigned letter, the two-part appendix) is translated, annotated with 217
footnotes, and built into `out/thousand-li.epub` (qa_epub PASS). There is no
next batch. See **COMPLETION.md** for the completion report, and PROGRESS.md for
the per-batch record. Any further work is a corrections pass (see the
"Corrections workflow" section of CLAUDE.md), not a new batch.

<details><summary>Archived B12 kickoff message (the final batch, now done)</summary>

```
Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. We are translating 《千里江山图》 (A Thousand Li of
Rivers and Mountains, Sun Ganlu, 2022) into an annotated English EPUB. The working
branch is claude/thousand-li (ONE branch; move any stray work onto it and delete
the stray). The deliverable is out/thousand-li.epub. B01 (ch01-ch05), B02 (ch06-ch08),
B03 (ch09-ch11), B04 (ch12-ch14), B05 (ch15-ch17), B06 (ch18-ch20), B07 (ch21-ch22),
B08 (ch23-ch25), B09 (ch26-ch27), B10 (ch28-ch30) and B11 (ch31-ch33) are done.

First: data/src/ is regenerable and gitignored, so if it is missing run
scripts/ingest_epub.py source.epub to recreate the extracted source text.

This is the LAST batch. Do Batch B12 = ch34 through ch37 end to end: ch34 鱼生粥 (Fish
Congee), ch35 黄浦江 (The Huangpu River), ch36 一封没有署名的信 / An Unsigned Letter (styled
龙华牺牲烈士的遗物, "a relic of a martyr who died at Longhua"), and ch37 附录 (Appendix). Read
each unit's source from data/src/: ch34 = 37_part0035.txt, ch35 = 38_part0036.txt,
ch36 = 39_part0037.txt, ch37 = 40_part0038.txt AND 41_part0039.txt. NOTE ch37: the
Appendix is ONE chapter with TWO sections (ch37s01 材料一 / "Material One", ch37s02 材料二 /
"Material Two: Members of the CCP Underground Organization Who Died in the Related Operations"),
built from two source files; its reading.md uses "### " (H3) section headings, so tag the
bilingual file "## H2 Appendix", then "### H3 Material One" ... "### H3 Material Two ...". Split
ch37 into two _en.json / bilingual passes if that is cleaner, or one file with the H3 tags in it.
Translate to the register in CLAUDE.md: clean flowing English prose, the novel's own voice, all
apparatus in footnotes, never inline.

Method that works, reuse it:
- For each unit, write out/<id>_en.json (a JSON array of English paragraphs, ONE per
  source paragraph line), then run:
    python3 scripts/make_bilingual.py <id> data/src/<file>.txt "<English title>" <id>_en.json
  It reads the source lines VERBATIM and enforces paragraph parity. Then
    python3 scripts/split_bilingual.py out/<id>_bilingual.md <id> "<中文标题>"
  (make_bilingual.py takes an optional 5th arg = number of leading title/junk lines to skip,
  default 2 = the "未知" line + one title line. ch36's title line is long -- confirm the skip
  count by eyeballing the file; pass 3 if the title wraps to two lines.)
- Run scripts/check_numbers.py out/<id>_bilingual.md --noise check_noise.txt and
  scripts/check_structure.py --pairs data/zh/<id>.txt out/<id>_reading.md, and fix what they flag.
  ALWAYS pass --noise check_noise.txt; if a new non-quantity numeral (a name or idiom with a digit
  in it) is flagged, add it to check_noise.txt with a comment on its own line (no trailing
  comments). Real dropped/altered quantities get fixed in the prose, not waived. Clock/floor/score
  numbers stay figures so the count survives. B11 added to check_noise.txt: 九条巷 (Jiutiao Lane),
  三轮车 (pedicab), 七拐八弯 (idiom), 百般 (idiom). Do NOT revert any existing check_numbers.py patches.

Footnotes are a RICH, fact-checked apparatus (the commissioner asked for a lot):
- Annotate real places, people, institutions and cultural references generously, and say in each
  note whether the thing is REAL history or the novel's invention, and whether the claim is
  corroborated / uncorroborated / contradicted. Fact-check against real scholarship (Wikipedia,
  Baidu Baike, academic/government sources). NEVER cite Grok, Grokipedia, or any AI-written source.
  Use subagents with web access for the research. ch36 (the martyr's letter) and ch37 (the Appendix,
  which frames the whole novel as recovered history and lists named underground members who died)
  are DENSE with names/places/dates presented as documentary -- fact-check every named person,
  place, date and organization there against real scholarship and say in the notes which are real
  and which are the novel's invention. This is the payoff of the book's homage-to-real-martyrs
  framing; treat it carefully.
- Anchors must be verbatim substrings of the English prose; recurring subjects get their note at
  FIRST appearance in the book, so CHECK glossary.json and notes.json before re-noting something
  already covered (grep the reading files for a term's first appearance before footnoting it). 204
  notes are already placed. Among those, added in B11: 宁绍山庄 Ningshao Manor (Ningbo-Shaoxing
  native-place charitable cemetery -- institution real, this named manor unattested); 蒲汇塘/漕河泾
  Puhui Creek & Caohejing (real geography, the Dec-1932 joining project uncorroborated); 梅雨 the
  plum-rains season; 桂花糖芋苗 osmanthus-sugared taro shoots (real Nanjing sweet); 法华镇 Fahua town
  (real border market town); the western-Shanghai dairy belt (real setting); 望平街 Wangping Street
  (real "Newspaper Street"); the North Station / Zhabei bombed in the January 28 1932 fighting (real;
  cross-refs the ch05 Nineteenth Route Army / January 28 note, does NOT re-note it); the GMD
  自首/自新/反省院 repentance machinery + the 危害民国紧急治罪法 ("Reflection Institutes", matching the
  ch22 rendering). Do NOT re-note (already placed): Shen Bao (ch07), the Nineteenth Route Army /
  January 28 (ch05), the Soviet areas / encirclement 围剿 (ch06), Ruijin / Provisional Central (ch22),
  Longhua (ch03), the Zhanyuan (ch03), the Party Affairs Investigation Section (ch03), the Shence
  Gate / 藏兵洞 (ch05/ch28), Hongkou Park (ch09), the Women's Normal University / Duan Qirui (ch26),
  Whampoa (ch23), the China Merchants Steam Navigation Co. (ch02), the painting 千里江山图 / Wang
  Ximeng (ch15). Note bodies are XHTML with NUMERIC character references (&#8212;, &#160;, &#8211;),
  never named entities; use LITERAL curly quotes and LITERAL Chinese characters as the existing notes
  do. Write Chinese into JSON via a file/Python and re-read to verify (B10 caught two mangled glyphs
  that way; B11 re-read clean). Add new glossary rows (one rendering per referent, decided before
  romanizing; real = "attested" with the fact, fictional cast marked so).

Rendering consistency (one rendering per referent -- check glossary.json AND grep earlier reading
files before you romanize or coin an English term). Carry-forward renderings for the ending: 陈千里
= "Chen Qianli"; 陈千元 = "Chen Qianyuan" (brother, arrested with Dong Huiwen; released via the
cemetery hostage move); 卢忠德 = "Lu Zhongde" (= "易君年"/"Yi Junnian" = Ye Qinian's mole "西施"/"Xi
Shi"; the real Yi Junnian was the dead 龙冬/"Long Dong"); 叶启年 = "Ye Qinian" (叶主任 = "Director Ye",
叶老师 = "Teacher Ye"); 游天啸 = "You Tianxiao" (游队长 = "Captain You"); 卫达夫 = "Wei Dafu" (captured
and tortured at the North Station, playing for time); 林石 = "Lin Shi" (died of his wound at Fahua);
李汉 = "Li Han"; 梁士超 = "Liang Shichao"; 凌汶 = "Ling Wen" (presumed killed); 董慧文 = "Dong Huiwen";
田非 = "Tian Fei"; 马秘书 = "Secretary Ma"; 欧阳民 = "Ouyang Min" (the traitor Ye Tao named as she died);
浩瀚同志 = "Comrade Haohan" (the prize being moved; the whole operation exists to get him out);
少山同志 = "Comrade Shaoshan"; 叶桃 = "Ye Tao" (Ye Qinian's dead daughter, Chen's love; her death told
in full in ch31); 方云平 / 老方 = "Fang Yunping" / "Old Fang" (the dead action-group head); 秦传安 /
秦医生 = "Qin Chuan'an" / "Doctor Qin"; 特工总部 = "the Special Operations Headquarters"; 侦缉队 = "the
detective squad"; 瞻园 = "the Zhanyuan"; 神策门 = "the Shence Gate"; 党务调查科 = "the Party Affairs
Investigation Section"; 千里江山图 (the operation / the painting) = "A Thousand Li of Rivers and
Mountains"; 交通线 = "liaison line"; 反省院 = "the Reflection Institute"; 申报 = "Shen Bao"; 书画铺 =
"painting-and-scroll shop"; 烧酒 = "grain spirit" (distinct from 绍酒 = "Shaoxing wine"); 北站 = "the
North Station" (Zhabei); 法华镇 = "Fahua town"; 望平街 = "Wangping Street"; 二/三/四马路 = "Second /
Third / Fourth Avenue".
Where B11 ends: on Lantern Festival day Chen Qianli forces Chen Qianyuan and Dong Huiwen's release by
taking Ye Qinian hostage at Ye Tao's grave, then withdraws his people to the Fahua dairy-shed hideout;
Wei Dafu baits the mole Lu Zhongde and lets himself be seized, and is now being tortured at the Lai'an
Li hotel by the North Station while Ye Qinian, listening from the shadows, has half-guessed that "A
Thousand Li of Rivers and Mountains" is the evacuation of the Communist Central from Shanghai and that
Tian Fei went to meet someone at the station. B12 (Fish Congee / The Huangpu River / An Unsigned Letter
/ Appendix) is the resolution and the documentary coda; read the source and confirm before romanizing
new names.

Scene typography (keep it up): the source carries NO typographic scene dividers. Add entries to
scenes.json for each new chapter (empty arrays are fine): "datelines" lists terse scene-header lines
VERBATIM (rendered centered), "breaks" lists the opening words of paragraphs that begin a new scene at
a hard cut with no dateline (a centered divider is inserted before them). A paragraph that opens on
dialogue uses the leading curly quote in its break anchor (the builder matches startswith). Verify each
string against the reading file, then confirm the built EPUB shows the expected number of breaks (grep
class="brk" / class="dateline" in the unzipped chapter xhtml). B11: ch31 1 dateline + 1 break, ch32 0+2,
ch33 0+1. ch34-ch37 may or may not have breaks; check. ch36 is a single short letter and ch37 is
documentary lists -- likely 0/0 each, but read and confirm.

Run the CLAUDE.md checks including blind double-translation on the argumentative/literary passages and a
back-translation omission pass (use subagents in separate contexts); record what ran in PROGRESS.md.

BECAUSE THIS IS THE LAST BATCH, also do the following instead of writing another handoff:
1. Back matter. back_matter.json is still EMPTY. Author the colophon from the source's copyright leaf
   (rendered via back_matter.json; scripts/build_reading_epub.py already supports it). RESOLVE the
   publisher discrepancy first: the copyright leaf prints 上海文化出版社, but the ISBN prefix
   978-7-5321-8331-9 and the Weibo/WeChat handles all belong to 上海文艺出版社 (Shanghai Literature and
   Art Publishing House). Fact-check which is correct (the ISBN publisher-prefix 5321 = 上海文艺出版社)
   and set the colophon accordingly, with a translator's note flagging the leaf's discrepancy if you
   keep both. The translator_note in book.json is current; leave it unless the ending changes something.
2. A whole-book QA pass: build, run qa_epub.py, and additionally spot-read across the whole spine for
   rendering drift (grep the built units for any term whose glossary rendering changed over the book),
   confirm the TOC links all 37 units, and confirm note numbering is sequential end to end.
3. Write a COMPLETION REPORT (not a handoff): what the finished edition contains, the final note count,
   the checks run book-wide, the known open items (see below), and the residual uncertainties flagged in
   the notes. Put it where a reader will find it (e.g. a COMPLETION.md, and summarize in the chat).

Then rebuild: scripts/build_reading_epub.py out/thousand-li.epub, and run scripts/qa_epub.py
out/thousand-li.epub until green (it refuses on an unmatched note anchor). Commit to claude/thousand-li
and push. Cite chapters, never page numbers. Never invent bridging text; footnote any genuine ambiguity
and leave it visible. Do not pause for approval mid-batch.

When you finish the batch, your final chat reply MUST contain BOTH of these, every time: (1) the built
out/thousand-li.epub attached as a file, and (2) since this is the last batch, the completion report
summary pasted into the chat (in place of a next-batch kickoff). Writing it into a file or pointing me
there is NOT enough. No batch is complete without both.
```

</details>

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
- Batch B10 = ch28-ch30 (Xiaotaoyuan, The Dyeworks Drying Ground, The Yangzhou Master): done; 195 notes.
- Batch B12 = ch34-ch37 (Fish Congee, The Huangpu River, An Unsigned Letter, Appendix): done; 217 notes
  (13 new). THE FINAL BATCH: back matter (colophon, publisher resolved), cover + Books/Kindle metadata,
  whole-book QA, and COMPLETION.md written. The book is finished.
- Batch B11 = ch31-ch33 (The Cemetery, The Dairy Shed, North Station): done; 204 notes (9 new). ch31 is
  the emotional climax: Chen Qianli confronts Ye Qinian at Ye Tao's grave on Lantern Festival day and
  tells the full truth of her death (she joined the Party at the Women's Normal University, worked inside
  the Zhanyuan, was shot from behind by Ye's own agents who were hunting Chen, and died in the Shence Gate
  vault after naming Ouyang Min the traitor); Chen takes Ye and Secretary Ma hostage to free Chen Qianyuan
  and Dong Huiwen. ch32: Wei Dafu baits the mole Lu Zhongde and plants a Shen Bao ad, then lets himself be
  taken. ch33: Wei is tortured at a Lai'an Li hotel by the North Station while Ye Qinian works out that
  "A Thousand Li of Rivers and Mountains" is the Communist Central's evacuation. See PROGRESS.md.

## Tooling in place

- scripts/make_bilingual.py, split_bilingual.py: the translation pipeline (verbatim source,
  paragraph parity). check_noise.txt: project noise for check_numbers.py (ALWAYS pass
  --noise check_noise.txt); extend when a name/idiom with a digit is flagged. B11 added
  九条巷, 三轮车, 七拐八弯, 百般.
- scenes.json: per-chapter "datelines" and "breaks". Add an entry for every new chapter (empty
  arrays are fine for single-scene chapters). Break anchors for dialogue-opening paragraphs must
  include the leading curly quote.
- scripts/build_reading_epub.py supports datelines, scene breaks, the epigraph, a book.json
  "translator_note", and back_matter.json (colophon). Do not revert.
- scripts/check_numbers.py keeps its patches (B01 clock times / teen ordinals; B03 negative
  lookbehind on the 一[日夜时…] idiom stripper; B04 twentieth/twenty-first/twenty-second;
  B06 "thirteenth"; B07 negative lookbehind on the 一[天次年…] measure stripper and a
  "<ones> hundred and <tens> thousand" composite; B08 "twelfth":12; B09 the optional ones-digit
  prefix on the "X十多" stripper; B10 "nil"/"zero":0 for a football score). Do not revert.

## Renderings settled this batch (full ledger in glossary.json)

- Places (real): 蒲汇塘 the Puhui Creek, 漕河泾 the Caohejing, 小闸镇 Xiaozha, 法华镇 Fahua town,
  望平街 Wangping Street, 老西门 Laoximen, 浙江路 Zhejiang Road, 大舞台 the Great Stage. Provisional:
  宁绍山庄 Ningshao Manor (real institution, named manor unattested).
- Terms: 烧酒 grain spirit (distinct from 绍酒 Shaoxing wine).
- Reused from the ledger unchanged: 反省院 the Reflection Institute, 北站 the North Station, 申报 Shen
  Bao, 书画铺 painting-and-scroll shop, 欧阳民 Ouyang Min, 田非 Tian Fei, 马秘书 Secretary Ma, 董家渡
  Dongjiadu, 马府街 Mafu Street, 方云平/老方 Fang Yunping/Old Fang.

## What is NEXT

- B12 = ch34-ch37, the LAST batch (Fish Congee, The Huangpu River, An Unsigned Letter, Appendix). On the
  last batch, do the back matter (colophon from back_matter.json, resolving the publisher discrepancy), a
  whole-book QA pass, and a COMPLETION REPORT instead of another handoff.

## Open items for the read-through

- Publisher discrepancy for the colophon: the copyright leaf prints 上海文化出版社, but the ISBN prefix
  (978-7-5321-...) and the Weibo/WeChat handles are 上海文艺出版社 (Shanghai Literature and Art Publishing
  House). The ISBN publisher-prefix 5321 = 上海文艺出版社. Resolve in B12 when back_matter.json is authored
  (still empty).
- The painting: named and footnoted at ch15 (Wang Ximeng's 千里江山图). Do NOT re-note it.
- Identity fully resolved (Lu Zhongde = the Shanghai "Yi Junnian" = Ye Qinian's "Xi Shi"; the real Yi
  Junnian was the murdered Long Dong). Ye Tao's death now told in full from both sides (ch28 Ye Qinian's,
  ch31 Chen Qianli's). Deaths established: Cui Wentai (ch25), Long Dong (ch21), Ye Tao (ch26/ch28/ch31),
  Old Fang / Fang Yunping (referred to throughout; the action-group head), Lin Shi (ch32, of his wound).
- The "Mr. Song's brother" / T. V. Soong reading (ch17) is footnoted as an invited inference; keep that
  framing if the Song family recurs.
- ch36 (An Unsigned Letter) is styled "遗物" (a martyr's relic); ch37 (Appendix) frames the fiction as
  recovered history and lists named underground members who died. Fact-check its named people/places/
  dates against real scholarship (rule 5) as they arrive -- this is the book's homage payoff.

## State / traps

- book.json is the LOGICAL structure. ch01 is an epigraph (kind:"epigraph"), NOT a chapter.
- The Appendix (ch37) is ONE chapter with two sections (ch37s01, ch37s02) from two source files
  (40_part0038.txt and 41_part0039.txt); its reading.md uses "### " headings.
- The source carries NO footnotes of its own and NO typographic scene dividers; every note is the
  translator's, and scene datelines/breaks are supplied via scenes.json.
- Note anchors are inserted BEFORE markup substitution and must be verbatim substrings of the
  English prose. Note bodies are XHTML with NUMERIC character references for dashes/nbsp, LITERAL
  curly quotes and LITERAL Chinese. A chapter H1 title cannot carry a note. Write Chinese into JSON
  via a file/Python and re-read to verify.
- Deliverable filename is out/thousand-li.epub. Work stays on branch claude/thousand-li.
  data/src/ and out/*_bilingual.md and out/*.epub are gitignored; out/*_reading.md,
  out/*_en.json, data/zh/*.txt, scenes.json, notes.json, glossary.json are tracked.
