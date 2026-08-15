# HANDOFF — Nameless Heroes (英雄无名), Chen Gongshu

This file is the baton. A fresh session with no memory reads it and starts
immediately. **It is the ARCHIVE of the message below, not its delivery:
every batch ends with this file's paste-block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count.** Rewrite
it at the end of every batch; always keep the paste-ready block below as its
first section. When the book completes, replace it with the completion notice
and do not touch it afterward.

## Message to paste into the next chat

```
Nameless Heroes B21

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once (its ONE failing regression test, "hook stands down on template stub", is a KNOWN false alarm; all others pass), then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05), B02 (ch06), B03 (ch07), B04 (ch08), B05 (ch09), B06 (ch10 preface + ch11), B07 (ch12), B08 (ch13), B09 (ch14), B10 (ch15), B11 (ch16), B12 (ch17), B13 (ch18 + ch19), B14 (ch20), B15 (ch21), B16 (ch22), B17 (ch23), B18 (ch24), B19 (ch25) and B20 (ch26) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them. PART TWO ("Disgrace at Hanoi") is COMPLETE; PART THREE ("Renown Won in a Hundred Battles" / 百战声威) is under way (ch20 self-preface + ch21/ch22/ch23/ch24/ch25/ch26). The EPUB now holds 26/43 chapters, 253 notes. NOTE on batch numbering: book.json's batches array lumps ch23+ch24 as "B17", so the working batch labels run ONE AHEAD of the book.json array from ch24 on (ch24 = B18, ch25 = B19, ch26 = B20, ch27 = B21).

Do Batch B21 = ch27 (ONE unit, a FULL chapter): ch27 = 第八章 大亨之死 扑朔迷离 "Chapter 8. The Death of a Tycoon, Shrouded in Mystery." IMPORTANT: Part Three SKIPS 第七章 - this is a FAITHFUL numbering gap (ch26 was 第六章, ch27 is 第八章; confirm ch27's title_en in book.json). ch27 continues DIRECTLY from ch26's tail: ch26 ("Mount Tai or a Feather") closed by raising the 张啸林 (Zhang Xiaolin) sanction (14 Oct 1940, shot by his hired bodyguard 林怀部 Lin Huaibu) and the doubts around it; ch27 is the full treatment of that "shrouded in mystery" case. Read the tail of ch26 English (out/ch26_reading.md, the last ~10 paragraphs on 大亨/张啸林/林怀部) and ch26 for register + story continuity. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch27 from data/src (28_index-split-000-0026.txt). CONFIRM structure p-by-p against data/src_epub/OEBPS/Text/index_split_000_0026.xhtml [parses to 1 <h2> + 136 <p>, NO <h1>, NO <br/>, NO <img>, NO [\d+] note markers]. drop=2 (running header 英雄无名-陈恭澍 + <h2> chapter title). The txt is ~137 wc-l lines; after drop=2 the 136 body lines map 1:1 to the 136 <p> (NO <br/>, so NO intra-<p> line breaks this time - unlike ch26's 54). Still do the byte-exact p-by-p diff FIRST (the B19/B20 method: extract <p> inner text, walk each <p> consuming 1 body line, assert every <p> matches its body line) to CONFIRM 136=136 and to LOCATE any SEVERED-<p> boundaries (a source <p> whose last char is non-terminal, continuing into the next <p> - ch25 had 7, ch26 had 7; per CLAUDE.md they MERGE, and parity is data/zh↔reading.md, NOT the raw <p> count). HEADS UP: ch27 uses ENUMERATED 一、二、三… SECTION HEADINGS - p#0/L3 一、这件案子不一定是我们干的 is the FIRST (standalone, cf. the 一、二、 style; distinct from ch26's couplet-style). GREP p-by-p for the full 一、-N、 series and for any glued/(N)-parens headings (watch the "three-tell": standalone; tail-glued ending non-terminal OR in a full-width 」; head-glued 一、X or a run-in label like 情报部份─; ch25/ch26 had tail-glued couplet headings, ch26 had one ending in 」). DISTINGUISH enumerated LIST items (rendered as ordinary paragraphs per parity) from 一、二、 SECTION headings (rendered ### ) - judge by function (a heading introduces a section; a list item is one of a set under a lead-in).
2. Extend scripts/clean_batch.py with ch27's spec (drop=2; the confirmed severed-<p> merges if any; the confirmed 一、-N、 standalone/glued headings). It supports merges (chains follow the merge_from map), standalone, tail-glued `glued`, and head-glued `glued_head`. Run it (source-conservation check must pass). Write out/ch27_reading.md (## from book.json title_en; one English paragraph per source body line; section headings as ### ; enumerated-list items as ordinary paragraphs per parity; run-in labels kept INLINE as prose). Then run scripts/batch_artifacts.py ch27, and ALWAYS finish with a NO-ARG run (the trap: an ID-run writes checks.json with ONLY that unit; the no-arg run restores all 27 units so check_structure/check_content see them).
3. Translate to the FROZEN register (Chen's voice sheet in HANDOFF; document-heavy chapters run higher - ch24 5.33, ch25 4.97, ch26 4.98 median with high "shall" on quoted directives/documents; read the note, do NOT reset or de-formalize the deliberate "shall"). Consult glossary.json and authority.json BEFORE romanizing anything; REUSE the settled Part-Three renderings (see the "Renderings settled" and the B15-B20 shelf sections of HANDOFF - all keyed with pinyin where keyed): 张啸林 Zhang Xiaolin (NOTED ch04, the Green-Gang tycoon), 林怀部 Lin Huaibu (keyed B20, the bodyguard), 傅筱庵 Fu Xiao'an (keyed/NOTED ch04, puppet Shanghai mayor), 杜月笙 Du Yuesheng (NOTED ch17), 黄金荣 Huang Jinrong (the three Green-Gang tycoons); the Shanghai District; the Juntong/the Juntong Bureau; 制裁 "sanction"; 敌伪 "the enemy and the puppets"; 特工总部/七十六号 "Special Operations Headquarters"/"No. 76"; 公共租界 "International Settlement"/法租界 "French Concession"; 第二行动大队 "Second Action Brigade"; 军统局 "the Juntong Bureau". IMPORTANT place-name convention (the check_content/qc_entities gate): keyed CITY/PROVINCE names render in PINYIN per the glossary - 北平 Beiping, 天津 Tianjin, 汉口 Hankou, 四川 Sichuan, 虹口 Hongkou, 重庆 Chongqing (NOT postal Peiping/Tientsin/Hankow/Szechuen/Hongkew/Chungking; 重庆大公报 renders "Chongqing Ta Kung Pao"); 愚园路 Yuyuan Road, 冀东 East Hebei are KEYED (align to them); non-keyed attested Shanghai ROADS keep their historical names (Robison Road, Avenue Edward VII, Yates Rd, etc.). Render Republican years literally (二十九年 = "the twenty-ninth year"; the checker matches the source numeral or auto-escapes via +1911). WATCH ch27's digitization glitches (list in PROGRESS.md, render to plain sense, footnote only real reading uncertainty): the same classes seen ch15-ch26 (single-char substitutions, dropped stops, 載-for-戴, mismatched guillemets, stray ？, and any ○/× redactions in room/lane/phone numbers - the numeric checker mis-reads ○; carry the real value in English and noise only the mis-read glyph-string; × redactions render as em-dash blanks). Dates/counts: carry real values as DIGITS; NOISE only idiom/approximate/name-numeral/elided forms (data/noise.txt already carries the B01-B20 rules; add ch27's).
4. Checks: verify_unit.py ch27 (parity + numbers with noise auto-found + anchors); check_align.py ch27; regenerate checks.json with scripts/batch_artifacts.py (no args) and run check_structure.py --config checks.json + check_content.py --config checks.json (NOTE: check_content prints KNOWN PRE-EXISTING artifacts and exits nonzero because of them - ch08 Shunde ×3, ch13 ×9, ch09 "Jize County" ×1, and now ch26's TWO documented keyed-substring FALSE POSITIVES: 武汉 "Wuhan" inside 武汉卿 "Wu Hanqing", and 劳勃生 "Lao Bosheng" inside the road 劳勃生路 "Robison Road"; CONFIRM ch27 itself shows "all in the paired paragraph" / 0 displaced, and align any keyed name/place to its glossary-decided rendering. A NEW unit's displacements are almost always a keyed name/place rendered a DIFFERENT way than the glossary - align the English to the keyed form; the exception is a keyed name that is a SUBSTRING of a larger different referent (person or road), which is a documented false positive, not a fix). Do NOT add COMMON-NOUN or book/periodical keys. qc_entities.py on a reconstructed bilingual (data/zh body lines + out/ch27_en.json, `> zh` / en pairs, strip the ### heading lines; every glossary row needs a pinyin field). Verify the TAIL against the source. check_register.py --ref reference/B01_frozen.md out/ch27_reading.md ("shall" is deliberate - read the note, do not de-formalize).
5. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (full list in PROGRESS.md; the big already-covered furniture: No.76/特工总部/丁默邨(keyed B20)/李士群 ch04/ch17, the concessions ch04, the gendarmerie ch11/ch23/ch24, 制裁, the Blue Shirts ch05/ch08, the Green-Gang three tycoons + 张啸林 ch04, Du Yuesheng ch17, 忠义救国军 ch21, the Sihang Warehouse/Mao Renfeng/Pan Hannian/Sima Qian-Mount Tai ch25, and the B20 furniture: 虞洽卿 Yu Qiaqing, 邵力子 Shao Lizi, 张爱萍/张执一, 求仁得仁, the 挽联, Ruby Queen, Ward Road Gaol, the 孤岛 Solitary Island, the Axis-recognition lantern parade, and the whole Shanghai cast). ch27 (大亨之死) is the Zhang Xiaolin tycoon-death chapter - expect new furniture (the Green-Gang/tycoon world, 林怀部's fate, any period figures/institutions) that earns notes; be generous but do NOT pad, do NOT re-note. Merge notes via apparatus_merge.py (numeric character references only in note bodies; anchors verbatim ASCII substrings of the reading.md body text, NO em dash and NO quote/apostrophe character - substring traps; multi-occurrence anchors attach at the first). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field; apparatus_merge's glossary path assumes a FLAT map and would corrupt the sectioned file - use it ONLY for notes; scripts/add_ch26_glossary.py is the by-hand pattern, asserting each hanzi key against data/zh). Confirm ch27 carries no images (its XHTML has NO <img> - confirm). For any CJK in a note body use the make_ch26_apparatus.py pattern (author bodies with typed hanzi, ASSERT every non-ASCII glyph is present in data/zh/ch27.txt, then convert to NCRs) to defeat the CJK-mangling hazard - and remember a CORRECT glyph may be ABSENT if the source prints a glitch/variant form, so describe such terms with the source's own form + pinyin.
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; update HANDOFF.md; commit and push to claude/nameless-heroes. (next is B22 = ch28; confirm its title_en in book.json.)

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B22 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
```

## What is DONE (do not redo)

- **Step 0 (survey).** Ingest + book.json (43 chapters, 5 TOC parts) + skeleton EPUB.
- **Batch B01 (ch01-ch05), the front matter.** 67 notes. **VOICE GATE PASSED:** the B01
  front matter is the FROZEN register reference (`reference/B01_frozen.md`) from B02 on.
- **B02-B05 (ch06-ch09). Part One COMPLETE.**
- **B06-B13 (ch10-ch19). Part Two ("Disgrace at Hanoi") COMPLETE.**
- **Batch B14 (ch20), PART THREE OPENS.** ch20 = the Part-Three self-preface.
- **Batch B15 (ch21).** Arrival + order of battle. **Batch B16 (ch22).** First 1940 sanctions
  + Fan Xing. **Batch B17 (ch23).** The "three-sided enemy" framing bridge. **Batch B18 (ch24).**
  The anatomy of the three-sided enemy + the Yu Yefeng sanction + Dai's self-review. **Batch B19
  (ch25).** The full work-review + the arms-gift + the Fan Xing intelligence puzzle.
- **Batch B20 (ch26), Part Three Chapter 6.** 第六章 泰山鸿毛 同此一掷 "Mount Tai or a Feather, All
  on One Throw" - a FULL martyr-roster chapter (321 body paragraphs). The Shanghai
  Workers'-Movement Committee episode; the nameless dead (Zhang Xingqiu/Zhu Tieying, Shao Fanjiu,
  Tao Lianfang buried alive); the Xiao family; the He Xingjian / CCP-infiltration passage (Zhang
  Zhiyi's captured memoir); the Xu Shouxin (Zhu Chengwo) "living sacrifice" and Xu Wenqi's
  reproduced prison essay; the 35-row enemy tally of sanctioned Japanese + the Japanese
  gendarmerie's own Akagi-assassination record; the Kang Corps. **drop=2; ALL 54 `<br/>` are in
  4 `<p>` and are TABLE/roster rows kept separate EXCEPT one 3-line prose block merged; 7
  severed-`<p>` merges; 6 sub-headings (4 standalone + 2 tail-glued, one ending in `」`).** 321
  body paragraphs; 11 notes (253 cumulative); 27 net new glossary rows (25 people + 2 orgs). Two
  documented keyed-substring FALSE POSITIVES in check_content/qc (武汉卿/劳勃生路). Heavily-corrupted
  source block (p#120-125) rendered to reconstructed sense + footnoted. All checks green; qa_epub
  PASS; epubcheck 0/0/0/0. **EPUB now 26/43 chapters.** Detail in PROGRESS.md ("Batch B20").

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` - derives data/zh/<id>.txt verbatim from data/src, applying per-unit
  drops/merges/heading-splits with a source-conservation check. Specs for ch01-ch26. Merge logic
  FOLLOWS CHAINS. **drop is variable:** most chapters drop=2; ch01/ch10/ch20 drop=3. `standalone`
  = a sub-heading kept as its own <p> with no heading markup, emitted as `### `; `glued` = a
  sub-heading fused onto a paragraph's TAIL (endswith), split off; `glued_head` = a heading fused
  onto a paragraph's HEAD (startswith), split off; `merges` = source <p> pairs that sever one
  sentence OR an intra-<p> `<br/>` line break (the extractor renders `<br/>` as a newline).
  **B20 lesson: not every `<br/>` is a merge** - a `<p>` that is a TABLE/roster (each `<br/>` a
  data row) is KEPT as rows, only a `<br/>`-split PROSE sentence merges. **B20 lesson: a tail-glued
  heading can end in a full-width `」`** (the three-tell's `」` case), which a non-terminal scan
  misses - grep for it.
- `scripts/batch_artifacts.py` - derives out/<id>_en.json FROM out/<id>_reading.md and writes
  checks.json. Author the reading.md; run this. **TRAP: running it with an ID writes checks.json
  with ONLY that unit; ALWAYS finish with a no-arg run.**
- `scripts/verify_unit.py <id>` - parity + numbers (auto-finds data/noise.txt; do NOT pass
  --noise) + anchors. Run per unit.
- `scripts/build_reading_epub.py` - builds out/nameless-heroes.epub. Uses book.json `title_en`
  for the visible chapter H1; `### ` sub-headings render as <h2>; notes collect in
  OEBPS/notes.xhtml with popup semantics.
- `scripts/check_content.py` (patched) - name_map skips "_"-prefixed glossary categories. It
  flags KNOWN PRE-EXISTING artifacts and exits NONZERO: **ch08 Shunde (3), ch13 (9), ch09 "Jize
  County" (1)** - NOT regressions. **B20 added TWO documented keyed-substring FALSE POSITIVES:
  武汉 "Wuhan" matching inside the person 武汉卿 "Wu Hanqing"; 劳勃生 "Lao Bosheng" (the SMP officer)
  matching inside the road 劳勃生路, correctly "Robison Road".** The pass criterion for a NEW batch
  is "the batch's own unit shows all name occurrences in the paired paragraph / 0 displaced" -
  EXCEPT a keyed name that is a substring of a larger different referent (person or road), which
  is a documented false positive, not a fix. A NEW unit's TRUE displacements are almost always a
  keyed name/place rendered a DIFFERENT way than the glossary: align the English to the keyed form.
  Do NOT add book-TITLE or COMMON-NOUN keys.
- **Verse marker `{p}`** (ch13, reused ch26 for the 挽联): prefix a pure-verse line with `{p} `;
  the builder renders `<p class="verse">`; the checks strip it.
- Glossary is authored/merged BY HAND into the SECTIONED file (book/people/organizations/places/
  terms), idempotent + re-read-verified. **Every row MUST carry a `pinyin` field** - qc_entities
  does `rec["pinyin"]` and KeyErrors otherwise. `scripts/add_ch26_glossary.py` is the by-hand
  pattern: asserts each hanzi key is a substring of data/zh/<id>.txt. A `/`-joined key holds
  alternate hanzi for one referent; qc splits on `/`. apparatus_merge's glossary path assumes a
  FLAT map and would corrupt the sectioned file; NOTES still go through apparatus_merge.py.
- **qc_entities catches term-rendering drift too:** a glossary common-noun term rendered a
  different way flags as a "miss." Align the English to the glossary.
- **GLOSSARY-KEY DISCIPLINE:** a key must be a DISTINCTIVE proper noun that renders ONE way
  everywhere. Periodicals and books are FOOTNOTES/inline, not keys. One-off transliterated
  Western/Japanese officer names, one-off telegram/roster names, and attested Shanghai ROADS are
  inline, not keyed. A bare surname whose full name is unknown is rendered inline.
- **Note-anchor gotchas:** anchors must be ASCII, WITHOUT any quote/apostrophe character AND
  without an em dash (U+2014) - all substring traps. The reading.md uses curly quotes and em
  dashes freely, so pick an anchor phrase with none of them (B20 used "Mr. Yu Qiaqing", "Shao
  Lizi", "Zhang Aiping", "the highest man of the Japanese side", "I set out here in outline",
  "seeking benevolence and finding it", "I made an elegiac couplet to mourn him", "Ruby Queen",
  "Ward Road Gaol", "Gunfire on the Solitary Island", "lantern-parade celebration rallies").
  Multi-occurrence anchors attach at the FIRST occurrence.
- **make_ch26_apparatus.py pattern (scripts/):** author note bodies as plain ASCII + typed hanzi
  + curly punctuation, ASSERT every non-ASCII glyph occurs in data/zh/<id>.txt, then convert every
  non-ASCII char to a numeric char ref and run apparatus_merge.py. **A CORRECT glyph may be ABSENT
  if the source prints a glitch/variant** (cf. ch25's 洋泾浜) - describe such terms with the
  source's own form + pinyin/English, not the correct hanzi.
- data/noise.txt carries the B01-B20 project noise rules (each with a comment line). Republican
  years render literally; the checker matches the source numeral (or auto-escapes Republican-year
  N via N+1911). The elided-tens block is ordered LONGEST-FIRST. Name-numeral glyphs are noised.
  Idiom numerals are noised. **The ○ (U+25CB) address artifact:** the checker cannot read ○ as
  zero - noise the mis-read glyph-string, carry the real value in the English. **× (source
  redaction)** renders as an em-dash blank. Every REAL value is CARRIED and matched as DIGITS.
  **B20 lesson: month-glyphs 六月-十月 rendered as English month-names (not digits) are noised**
  (the slash-format tally dates carry their real digits separately).
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches it; re-run per session).
  setup.sh's ONE failing regression test ("hook stands down on template stub") is a KNOWN false
  alarm; all other regression tests pass.

## Renderings settled / carry-forward

- 军统 / 军统局 -> "the Juntong" / "the Juntong Bureau" (DECIDED). 戴笠 Dai Li (courtesy Yunong;
  老板 "the Boss"; 戴先生 "Mr. Dai"; 戴雨农 "Dai Yunong"); 汪精卫 Wang Jingwei (汪逆 "the traitor
  Wang"). 制裁 "sanction"; 制裁令 "sanction order." 敌伪 "the enemy and the puppets"; 汪伪 "Wang
  puppets"; 沦陷区/沦陷地区 "the fallen zone(s)"; 战区 "war zone"; 后方 "the rear"; 区长 "District
  Chief"; 督察 "inspector" / "inspectorate"; 总督察 "Chief Inspector" (电讯总督察 "chief
  communications inspector"); 第二处 "the Second Section." Chiang's titles: 校长 "the Commandant",
  委员长/委座 "the Generalissimo", 总裁 "the Director-General"; 领袖 "the Leader"; 总理 "the Party
  Leader" (Sun Yat-sen). 日本宪兵队 "the Japanese gendarmerie"; 七十六号 "No. 76"; 特工总部 "Special
  Operations Headquarters"; 工部局 "Municipal Council"; 公共租界 "International Settlement"; 法租界
  "French Concession"; 巡捕房 the Concession police / "police station"; 三民主义 "the Three
  Principles of the People."
- **PLACE-NAME CONVENTION (the qc gate enforces the glossary's PINYIN for keyed cities):**
  北平 Beiping, 天津 Tianjin, 汉口 Hankou, 四川 Sichuan, 虹口 Hongkou, 重庆 Chongqing (NOT Peiping/
  Tientsin/Hankow/Szechuen/Hongkew/Chungking). 重庆大公报 = "Chongqing Ta Kung Pao". KEYED roads:
  愚园路 "Yuyuan Road", 冀东 "East Hebei". Non-keyed attested Shanghai ROADS keep their historical
  forms: Avenue Edward VII (爱多亚路), Robison Road (劳勃生路 - NOT "Lao Bosheng Road"; the officer
  劳勃生 is keyed "Lao Bosheng", a documented substring false positive), Yates Rd (同孚路), Sinza Rd
  (新闸路), Wayside Rd (西华德路), Dixwell Rd (狄思威路), Seward Rd (施高塔路), Range Rd (老靶子路),
  North Sichuan Rd (北四川路), Foochow Rd (福州路), Park Rd (派克路), Route Massenet (马斯南路),
  Route Père Robert (金神父路), Avenue Joffre (霞飞路), Avenue du Roi Albert (亚尔培路), Kiaochow Rd
  (胶州路), Kungping Rd (公平路), the Bund/Whangpoo, Zikawei (徐家汇), Jessfield Park (兆丰花园/公园),
  Hongkou Park (虹口公园). Concession-street rule: keep attested names, use pinyin for the uncertain.
- **Book / part titles (in-text; DECIDED; reuse verbatim):** 英雄无名 = "Nameless Heroes"; Part One
  北国锄奸 = "Rooting Out Traitors in the North"; Part Two = "Disgrace at Hanoi"; Part Three 百战声威
  = "Renown Won in a Hundred Battles." 蓝衣社 = "the Blue Shirt Society" (NOTED ch08; also the
  enemy's name for the Juntong). 忠义救国军 = "the Loyal and Patriotic Army" (NOTED ch21). 抗日杀奸团
  = "the Anti-Japanese Traitor-Killing Corps" / 抗团 = "the Kang Corps" (NOTED ch02/ch11; 抗团 keyed
  B20). Books by FOOTNOTE/inline (not glossary): 蒋总统秘录, 戴雨农先生传/全集, 沪滨三次历险实录,
  沪上往事 (Wan Molin), 在敌人心脏里 (Zhang Zhiyi, ch26), 大陆宪兵实录 (the Japanese gendarmerie
  memoir, ch26); periodicals: 申报 Shenbao (NOTED ch24), 大公报 Ta Kung Pao, 中华日报/新申报
  (occupation papers, ch20), 中美日报, 传记文学.
- **B15/B16 shelf (ch21/ch22):** 郑修元 Zheng Xiuyuan, 陈第容/陈明楚 Chen Dirong/Chen Mingchu, 黄志远
  Huang Zhiyuan, 赵理君 Zhao Lijun, 刘原深 Liu Yuanshen, 毕高奎 Bi Gaokui, 孙大成 Sun Dacheng, 万里浪
  Wan Lilang, 戴藏宜 Dai Cangyi, 杜月笙 Du Yuesheng (NOTED ch17), 俞叶封 Yu Yefeng, 万墨林 Wan Molin,
  范纪曼 Fan Jiman (= 范行 Fan Xing), 张啸林/杜/黄金荣 the three Green-Gang tycoons (张啸林 NOTED ch04),
  曾澈 Zeng Che, 王文 Wang Wen, 王天木 Wang Tianmu.
- **B18 shelf (ch24):** 劳勃生 Lao Bosheng (NOTED); 更新舞台 Gengxin Stage; 新艳秋 Xin Yanqiu (NOTED);
  袁殊 Yuan Shu (NOTED); 刘俊卿 Liu Junqing, 蒋福田 Jiang Futian (concession police); 刘绍奎 Liu
  Shaokui, 周伟龙 Zhou Weilong (道三 Daosan).
- **B19 shelf (ch25):** 秦启荣 Qin Qirong (NOTED); 毛人凤 Mao Renfeng (NOTED); 潘汉年 Pan Hannian
  (NOTED); 聂崇侯 Nie Chonghou; 潘子欣 Pan Zixin; 胡永荃 Hu Yongquan; 彭雅萝 Peng Yaluo; 高荣 Gao Rong.
- **B20 shelf (ch26; reuse; all keyed with pinyin):** 丁默邨 Ding Mocun (keyed B20), 汪时璟 Wang
  Shiying, 施何成 Shi Hecheng, 邵范九 Shao Fanjiu, 陶联芳 Tao Lianfang, 徐寿新 Xu Shouxin (= 朱承我
  Zhu Chengwo), 徐寿棪 Xu Shouyan, 徐文祺 Xu Wenqi, 余延智 Yu Yanzhi, 周锡良 Zhou Xiliang (= 周希良),
  张执一 Zhang Zhiyi, 赤木亲之 Akagi Chikayuki, 林秀澄 Hayashi Hidezumi, 李正梁/李亮 Li Zhengliang/Li
  Liang, 林怀部 Lin Huaibu, 俞作柏 Yu Zuobai, 林之江 Lin Zhijiang, 萧焕文 Xiao Huanwen, 萧杰英 Xiao
  Jieying, 萧张权 Xiao Zhangquan, 陈植琚 Chen Zhiju, 李鑫 Li Xin, 缪维 Miao Wei, 黄克忠 Huang Kezhong,
  向松坡 Xiang Songpo; 上海职工运动委员会 the Shanghai Workers'-Movement Committee, 抗团 the Kang Corps.
  NEW ch26 notes: Yu Qiaqing; Shao Lizi; Zhang Aiping/Zhang Zhiyi; the corrupted source block +
  Second/Third Brigade slip; the Republican-year tally dates; 求仁得仁; the 挽联; Ruby Queen; Ward
  Road Gaol; the 孤岛 Solitary Island; the Axis-recognition lantern parade. Rendered INLINE (not
  keyed): the eight verdict martyrs (许克/李楚琛/陈兆庆/徐阿梅/彭福戎), the Kang Corps founders/roster,
  the Akagi hit-team (李德昌/叶东山/周振芳/俞森林/杨景文), the Japanese officers (中村常雄 etc., romaji),
  向海潜 (Xiang Haiqian, styled name of Xiang Songpo).

## Voice sheet - CHEN GONGSHU (author / narrator)

- REGISTER: educated, formal, essayistic first person; grave and a touch archaic but not stilted.
  Long semicolon-joined clauses; four-character idiom and classical allusion used freely and
  footnoted when they carry weight. Refers to himself as 笔者 "the writer" and 我 "I." His narrating
  "shall" is DELIBERATE - do not de-formalize it; check_register flags it informationally (B06 33%,
  B08 29%, B12 43%, B15 33%, B16 36%, B18 25%, B19 67%, B20 83% - elevated when the chapter
  reproduces many quoted directives/documents; ch26 carries three Dai Li telegrams + a formal
  memorial essay).
- STANCE: self-justifying yet self-effacing; insists on truthfulness, admits his blunders; tender
  toward dead comrades, bitter and scornful toward the enemy and the Communists. When quoting
  hostile/puppet/comrades' documents (memoirs, telegrams, news reports, the captured CCP memoir),
  keep the quoted register DISTINCT from Chen's own dry scorn.
- Ratio ~4.55-4.78 en/han in narrative; prefaces denser (~5.2-5.3); document-heavy chapters run
  higher (ch21 4.89, ch22 4.70, ch24 5.33, ch25 4.97, ch26 4.98 median). Read the note, do not reset.

## Voice sheets - principal & recurring cast

- **DAI LI (戴雨农 / Mr. Dai / 老板 "the Boss").** After ch17 only letters and telegrams; his word
  is "as a mountain." In ch26 three of his telegrams (to Zhou Weilong, Yu Zuobai, He Xingjian) are
  reproduced, and he refuses to confine the Kang Corps to an "intelligence viewpoint."
- **QI QINGBIN (齐庆斌) & ZHANG ZUOXING (张作兴).** Chen's childhood friends; the Shanghai District
  secretary and radio inspector.
- **ZHENG XIUYUAN (郑修元).** District secretary who held the Shanghai District together; his memoir
  "沪滨三次历险实录" is quoted throughout Part Three.
- **LIU YUANSHEN (刘原深).** The very man who revises "Nameless Heroes" for Chen; his living
  memory-check throughout Part Three (in ch26 he supplies the Tao Lianfang and Yu Yanzhi cases and
  takes charge of the Kang Corps liaison).
- **SUN DACHENG (孙大成).** The Kang Corps action leader; came to Shanghai July 1940 as the corps'
  representative, blew off an arm test-firing a demolition agent (Oct 1941), survived No. 76.
- **Dead comrades carried in memory:** ZENG CHE 曾澈, WANG WEN 王文 (ch11, and the Kang Corps
  founder, ch26); the ch26 martyrs (Xu Shouxin/Zhu Chengwo, Yu Yanzhi, Zhou Xiliang, Tao Lianfang,
  Xiao Zhangquan, Chen Zhiju, Li Xin, Miao Wei/Huang Kezhong).

## ⚠ Name trap RESOLVED (do not reopen): 陈邦国 / 郑邦国

The Hanoi action-team member the source spells 郑邦国 in ch13 and 陈邦国 in ch15/ch16/ch17 is ONE
man. RESOLVED to **Chen Bangguo (陈邦国)**. Use Chen Bangguo consistently.

## Where the book stands

- Part One (北国锄奸) COMPLETE (B01-B05). Part Two ("Disgrace at Hanoi") COMPLETE (B06-B13).
- **Part Three ("Renown Won in a Hundred Battles" / 百战声威) under way (B14-B20).** ch20 =
  self-preface; ch21 = arrival + order of battle; ch22 = first 1940 sanctions + Fan Xing; ch23 =
  the "three-sided enemy" bridge; ch24 = the anatomy of the three-sided enemy + Yu Yefeng sanction
  + Dai's self-review; ch25 = the full work-review + arms-gift + Fan Xing puzzle; ch26 = the
  nameless martyrs (labor committee, the Xiao family, the He Xingjian/CCP passage, the Xu Shouxin
  living sacrifice, the enemy tally + Japanese gendarmerie record, the Kang Corps).
- **NEXT: B21 = ch27** - 第八章 大亨之死 扑朔迷离 "The Death of a Tycoon, Shrouded in Mystery"
  (Part Three SKIPS 第七章 - a faithful numbering gap). Continues ch26's tail on the 张啸林/林怀部
  sanction. 1 <h2> + 136 <p>, NO <br/>, NO <img>, NO note markers. drop=2. Opens with the
  enumerated section heading 一、这件案子不一定是我们干的 (ch27 uses 一、二、 style headings, NOT couplets).

## What is NEXT

- Batch B21 = ch27. Kickoff is the paste-block at the top. Runs to completion (no gate); ends by
  pasting the B22 kickoff. B22 = ch28 (confirm title_en in book.json). Working batch labels run ONE
  AHEAD of book.json's batches array from ch24 on (ch24 = B18 … ch27 = B21).
- The frozen register reference is `reference/B01_frozen.md`. Narrative sits at 4.55-4.78 en/han;
  document-heavy chapters run higher (ch24 5.33, ch25 4.97, ch26 4.98) - alignment/register are
  the gates, not the raw ratio.
- Sub-heading pattern DIFFERS by chapter. Styles seen: Part One numbered 一/二/三; ch11/ch14/
  ch20-title/ch21-ch26 COUPLET-STYLE with NO number prefix; ch12/ch13/ch15/ch16/ch17/ch18-sections
  numbered-in-parens (一)/(二)…; ch27 uses 一、二、 enumerated headings. GLUED sub-heads seen ch08/
  ch16/ch18/ch22 (tail), ch24 (BOTH tail and HEAD), ch25 (two tail-glued), ch26 (two tail-glued,
  one ending in `」`). Grep each new chapter p-by-p, and DISTINGUISH enumerated LIST items (per
  parity) from (一)/(二) or 一、 SECTION headings and from run-in labels.
- WATCH for source anomalies: cuts, misplaced-「 glitches, corrupt/dropped-character phrases,
  dropped full stops, the "(第N章完，下期续载)" coda/magazine-seam pattern, a STRAY glyph fused onto a
  title (ch22's 杀), a STRAY orphan enumerator (ch24's "(一)"), stray ？ (ch26), the ○ (U+25CB) and
  × redactions in addresses/names, a HEAVILY-corrupted block (ch26's p#120-125), and pervasive
  single-character substitutions. Intra-<p> `<br/>` line breaks: PROSE splits MERGE, TABLE/roster
  rows are KEPT (ch26). Severed-<p> boundaries (a source <p> ending non-terminal) MERGE (ch25/ch26
  each had 7). Re-grep each batch's source for `\[\d+\]` note markers (none through B20).

## Open items for the read-through / completion

- Feed decided renderings back to authority.json on completion: 军统 "the Juntong"; the full
  B02-B20 historical-name set.
- Japanese name readings to firm up when the men recur (多田骏, 田代皖一郎, 土肥原贤二, 板垣征四郎,
  近卫文麿, 影佐祯昭, 今井武夫, 晴气庆胤; 大屋久寿雄; 横山秋马; 岩井英一; the B18 gendarmerie officers;
  the B20 gendarmerie officers 中村常雄/小林峰三郎/杉本喜三郎/加藤田/林秀澄 Hayashi Hidezumi/大冢清
  Ōtsuka Kiyoshi and the Akagi 赤木亲之 Chikayuki - romaji to firm up).
- Provisional romanizations to firm up (glossary `provisional` rows, incl. the Shanghai-District
  cast, the B16 operatives, the B18 rows, the B19 rows).
- Whole-book reconciliation items: ch09 "Jize County" (the 鸡泽县 key); the pinyin-vs-postal city
  names (standardized to pinyin from B18); the two B20 keyed-substring false positives (武汉卿 /
  劳勃生路) - both correct as rendered, flagged only by substring match. Stray source glyph still to
  resolve: 毛酋 in a ch36 section title.

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01-B20 builds (0/0/0/0). Source is a clean digital
  EPUB, predominantly simplified with residual variant glyphs and pervasive digitization glitches
  (list them, render to plain sense, do not footnote mechanical typos). B01-B20 glitch lists in
  PROGRESS.md; ch26 carries an unusually heavy corrupted block (p#120-125, footnoted).
- Running-header line 英雄无名-陈恭澍 opens all 43 content files: drop it. drop count is variable -
  most drop=2; ch01/ch10/ch20 drop=3.
- Enumerated ；/：/、 bullet lists, quoted-document/directive/roster lines (INCLUDING intra-<p>
  `<br/>` TABLE rows, ch26), salutations, verse lines, juxtaposition lines, run-in section labels,
  and 『』-closed dialogue are DELIBERATE separate `<p>`/lines - do NOT merge them; only genuine
  mid-phrase splits (last char not terminal, OR a source `<p>` boundary that severs one sentence,
  OR an intra-<p> `<br/>` inside PROSE) merge, and those can CHAIN.
- Faithful numbering gaps/anomalies (NOT errors): Part Three skips 第七章 (ch27 = 第八章); ch10 splits
  into (上)/(下); 三面受敌 一往无前 titles two chapters (ch14 and ch24); ch09 printed §五 before §四;
  ch13 restarts its (一)-(五) numbering; ch16 reproduces two whole Wang documents; ch21/ch22/ch24
  carry magazine "下期续载" seams; ch24 has a source-internal date slip; ch25 has a 每日/每月
  directive discrepancy (footnoted); ch26 marks a section 二、 with the "一、" only implicit, and its
  source credits Akagi to the "Second Brigade" against the tally's Third (footnoted). Preserve and,
  where a reader would stumble, footnote.
- Expect a stray per-task branch at the top of every batch; consolidate onto claude/nameless-heroes
  per rule 2.
