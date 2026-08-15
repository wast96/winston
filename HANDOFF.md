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
Nameless Heroes B20

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once (its ONE failing regression test, "hook stands down on template stub", is a KNOWN false alarm; all others pass), then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05), B02 (ch06), B03 (ch07), B04 (ch08), B05 (ch09), B06 (ch10 preface + ch11), B07 (ch12), B08 (ch13), B09 (ch14), B10 (ch15), B11 (ch16), B12 (ch17), B13 (ch18 + ch19), B14 (ch20), B15 (ch21), B16 (ch22), B17 (ch23), B18 (ch24) and B19 (ch25) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them. PART TWO ("Disgrace at Hanoi") is COMPLETE; PART THREE ("Renown Won in a Hundred Battles" / 百战声威) is under way (ch20 self-preface + ch21/ch22/ch23/ch24/ch25). The EPUB now holds 25/43 chapters, 242 notes.

Do Batch B20 = ch26 (ONE unit, ~19,000 source chars, a FULL chapter): ch26 = 第六章 泰山鸿毛 同此一掷 "Chapter 6. Mount Tai or a Feather, All on One Throw." NOTE on batch numbering: book.json's batches array lumps ch23+ch24 as "B17", so the working batch labels run ONE AHEAD of the book.json array from ch24 on (ch24 = B18, ch25 = B19, ch26 = B20). Read the tail of ch25 English (out/ch25_reading.md) and ch24/ch25 for register + story continuity; ch25 ("a full reckoning") closed on the nameless dead and Sima Qian's "death heavier than Mount Tai, lighter than a feather" (NOTED ch25 as note 10 - do NOT re-note; ch26's very title 泰山鸿毛 reuses the allusion). ch26 opens on 没有名籍生死不明的先烈们 "The Nameless Martyrs, Their Life or Death Unknown" and the 上海职工运动委员会 (Shanghai Workers'-Movement Committee) episode. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch26 from data/src (27_index-split-000-0025.txt). CONFIRM structure p-by-p against data/src_epub/OEBPS/Text/index_split_000_0025.xhtml [parses to 1 <h2> + 280 <p> + 54 <br/>, NO <h1>, NO <img>, NO [\d+] note markers]. drop=2 (running header 英雄无名-陈恭澍 + <h2> chapter title). RECONCILE the body count: the txt is ~336 awk-NR lines but the XHTML has 280 <p>; the difference is the FIFTY-FOUR <br/> tags. HEADS UP: ch26 has an UNUSUALLY high <br/> count (54, vs ch25's 2 and ch13's 4) - many <p> hold intra-paragraph line breaks the extractor renders as newlines. Each <br/> is a MERGE pair (or a CHAIN, if a <p> carries several <br/>), NOT a paragraph boundary. Do the byte-exact p-by-p diff FIRST (the B19 method: extract <p> inner text with <br/>→marker, walk each <p> consuming 1 body line per segment, assert every non-br <p> matches its body line) to locate all 54 and any CHAINS (a <p> with 2+ <br/> = a 3+-line chain), THEN also grep p-by-p for SEVERED-<p> boundaries (a source <p> whose last char is non-terminal, continuing into the next <p> - B19 had 7 of these the coarse br-only reconciliation missed; per CLAUDE.md they ALSO merge, and parity is data/zh↔reading.md, NOT the raw <p> count). Sub-heading: p#0/L3 没有名籍生死不明的先烈们 is the opening sub-heading (couplet-style, cf. ch11/ch14/ch21/ch22/ch23/ch24/ch25) - standalone. GREP p-by-p for further standalone/glued/(一)-(二)-parens section headings (watch the "three-tell": standalone; tail-glued ending non-terminal OR in a full-width 」; head-glued (一)X or a label like 情报部份─ / 破坏部份─ run-in; ch25 had a head-glued 情报部份─ kept INLINE and two tail-glued story titles).
2. Extend scripts/clean_batch.py with ch26's spec (drop=2; ALL the <br/> merges incl. chains; the confirmed severed-<p> merges; the confirmed standalone/glued headings). It already supports merges (chains follow the merge_from map), standalone, tail-glued `glued`, and head-glued `glued_head`. The intra-<p> <br/> case is handled by the plain `merges` machinery (the extractor renders <br/> as a newline, so it is just another line pair; a <p> with N <br/> is a chain of N+1 lines). Run it (source-conservation check must pass). Write out/ch26_reading.md (## from book.json title_en; one English paragraph per source body line; sub-headings as ### ; any enumerated-list items as ordinary paragraphs per parity; run-in section labels like 情报部份─ kept INLINE as prose, cf. ch25). Then run scripts/batch_artifacts.py ch26, and ALWAYS finish with a NO-ARG run (the trap: an ID-run writes checks.json with ONLY that unit; the no-arg run restores all 26 units so check_structure/check_content see them).
3. Translate to the FROZEN register (Chen's voice sheet in HANDOFF; document-heavy chapters run higher - ch24 measured 5.33, ch25 4.97 median with 67% "shall" on its many quoted Dai Li directives; read the note, do NOT reset or de-formalize the deliberate "shall"). Consult glossary.json and authority.json BEFORE romanizing anything; REUSE the settled Part-Three renderings (see the "Renderings settled" and the B15/B16/B18/B19 shelf sections of HANDOFF - all keyed with pinyin where keyed): the Shanghai District; the Juntong/the Juntong Bureau; 制裁 "sanction"; 督察 "inspector"/"inspectorate" (align common-noun terms to the glossary - the qc_entities gate); 敌伪 "the enemy and the puppets"; 特工总部/七十六号 "Special Operations Headquarters"/"No. 76"; 公共租界 "International Settlement"/法租界 "French Concession"; 忠义救国军 "the Loyal and Patriotic Army"; 刘绍奎 Liu Shaokui/刘俊卿 Liu Junqing/蒋福田 Jiang Futian (keyed ch24); 齐庆斌 Qi Qingbin, 张作兴 Zhang Zuoxing (兄=Brother); 戴雨农 Dai Yunong/Mr. Dai; 毛人凤 Mao Renfeng (NOTED ch25). IMPORTANT place-name convention (the check_content/qc_entities gate): keyed CITY/PROVINCE names render in PINYIN per the glossary - 北平 Beiping, 天津 Tianjin, 汉口 Hankou, 四川 Sichuan, 虹口 Hongkou (NOT the postal Peiping/Tientsin/Hankow/Szechuen/Hongkew); non-keyed attested Shanghai ROADS keep their historical names (Seymour Road, Route Doumer, Bubbling Well Road, Newchwang Road, etc.). Render Republican years literally (二十九年 = "the twenty-ninth year"; the checker matches the source numeral or auto-escapes via +1911). WATCH ch26's digitization glitches (list in PROGRESS.md, render to plain sense, footnote only real reading uncertainty): the same classes seen ch15-ch25 (single-char substitutions, dropped stops, 載-for-戴, mismatched guillemets), and watch the ○ (U+25CB circle-zero) and × (redaction) in any room/lane/phone numbers (the numeric checker mis-reads ○ - carry the real value in the English and noise only the mis-read glyph-string; × redactions render as em-dash blanks, cf. ch25). Dates/counts: carry real values as DIGITS; NOISE only idiom/approximate/name-numeral/elided forms (data/noise.txt already carries the B01-B19 rules; add ch26's).
4. Checks: verify_unit.py ch26 (parity + numbers with noise auto-found + anchors); check_align.py ch26; regenerate checks.json with scripts/batch_artifacts.py (no args) and run check_structure.py --config checks.json + check_content.py --config checks.json (NOTE: check_content prints KNOWN PRE-EXISTING artifacts and exits nonzero because of them - ch08 Shunde ×3, ch13 Miss Nguyen/Oya Kusuo/Yuan Haowen ×9, ch09 "Jize County" ×1; CONFIRM ch26 itself shows "all in the paired paragraph" / 0 displaced, and align any keyed name/place to its glossary-decided rendering). Do NOT add COMMON-NOUN or book/periodical keys. qc_entities.py on a reconstructed bilingual (data/zh body lines + out/ch26_en.json, `> zh` / en pairs, strip the ### heading lines; every glossary row needs a pinyin field). Verify the TAIL against the source (critical on a 19k+ single-pass unit - the corruption class hides in the last paragraphs). check_register.py --ref reference/B01_frozen.md out/ch26_reading.md ("shall" in Chen's narration + quoted directives is deliberate - read the note, do not de-formalize).
5. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (full list in PROGRESS.md; the big already-covered furniture: No.76/特工总部/丁默邨/李士群 ch04/ch17, the concessions ch04, the gendarmerie ch11/ch23, 制裁, the Blue Shirts ch05/ch08, the Green-Gang three tycoons ch04, Du Yuesheng ch17, 忠义救国军 ch21, the Sihang Warehouse/釜底抽薪/Mao Renfeng/Pan Hannian/xieke huang/pidgin/Sima Qian-Mount Tai ch25, the Republican calendar, and the whole Shanghai cast). ch26 (泰山鸿毛, "the nameless martyrs") is a martyr-roster chapter - expect genuinely new furniture (people, worker-movement cases, the 上海职工运动委员会 and its patrons 虞洽卿 Yu Qiaqing / 赵子刚) that earns notes; be generous but do NOT pad, do NOT re-note. Merge notes via apparatus_merge.py (numeric character references only in note bodies; anchors verbatim ASCII substrings of the reading.md body text, NO em dash and NO quote/apostrophe character - substring traps; multi-occurrence anchors attach at the first). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field; apparatus_merge's glossary path assumes a FLAT map and would corrupt the sectioned file - use it ONLY for notes; scripts/add_ch25_glossary.py is the by-hand pattern, asserting each hanzi key against data/zh). Confirm ch26 carries no images (its XHTML has NO <img> - confirm). For any CJK in a note body use the make_ch25_apparatus.py pattern (author bodies with typed hanzi, ASSERT every non-ASCII glyph is present in data/zh/ch26.txt, then convert to NCRs) to defeat the CJK-mangling hazard - and remember a CORRECT glyph may be ABSENT if the source prints a glitch/variant form (ch25's 洋泾浜 was absent, only the source's 洋经滨 present), so describe such terms with the source's own form + pinyin.
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; update HANDOFF.md; commit and push to claude/nameless-heroes. (next is B21 = ch27, titled 第八章 - Part Three SKIPS 第七章, a faithful numbering gap; confirm its title_en in book.json.)

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B21 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
```

## What is DONE (do not redo)

- **Step 0 (survey).** Ingest + book.json (43 chapters, 5 TOC parts) +
  skeleton EPUB. See the survey section of PROGRESS.md.
- **Batch B01 (ch01-ch05), the front matter.** 67 notes. **VOICE GATE PASSED:**
  the B01 front matter is the FROZEN register reference (`reference/B01_frozen.md`)
  for `check_register.py --ref` from B02 on.
- **Batch B02 (ch06), Part One Section 1.** 322 paragraphs; the once-per-book blind
  double-translation and back-translation samples were done here.
- **Batch B03 (ch07), Part One Section 2.** 362 paragraphs; the Zhang Jingyao case.
- **Batch B04 (ch08), Part One Section 3.** 461 paragraphs; the Ji Hongchang case.
- **Batch B05 (ch09), Part One Section 4.** 332 paragraphs; the Shi Yousan case.
  **Part One COMPLETE.**
- **Batch B06 (ch10 + ch11), Part Two opens.** Part Two title RESOLVED: "Disgrace at Hanoi."
- **Batch B07 (ch12), Part Two Chapter 2.** "Unfathomable Hearts, Hidden Designs."
- **Batch B08 (ch13), Part Two Chapter 3.** "Treacherous Tides, a Gathering Storm."
- **Batch B09 (ch14), Part Two Chapter 4.** A very short bridge chapter; 0 new notes.
- **Batch B10 (ch15), Part Two Chapter 5.** The CLIMAX (the botched Hanoi sanction).
  Name trap RESOLVED: 郑邦国 -> 陈邦国 "Chen Bangguo."
- **Batch B11 (ch16), Part Two Chapter 6.** The reckoning/indictment chapter.
- **Batch B12 (ch17), Part Two Chapter 7.** Recall to Chongqing, then Shanghai reassignment.
- **Batch B13 (ch18 + ch19). PART TWO COMPLETE.** ch18 takes over the Shanghai District;
  ch19 = the closing Author's Note.
- **Batch B14 (ch20), PART THREE OPENS.** ch20 = the Part-Three self-preface; 2 notes.
- **Batch B15 (ch21), Part Three Chapter 1.** Chen arrives (Aug 1939), rebuilds the order of
  battle. 8 notes; 19 glossary rows.
- **Batch B16 (ch22), Part Three Chapter 2.** The LONGEST unit (286 body paragraphs). The
  first 1940 sanctions; the Fan Xing reunion; the moral-conscience essay. 7 notes; 29 rows.
- **Batch B17 (ch23), Part Three Chapter 3.** A SHORT framing bridge (7 body paragraphs).
  Names the "three-sided enemy," previews the Yu Yefeng sanction. 1 note; 0 new rows.
- **Batch B18 (ch24), Part Three Chapter 4.** 第四章 三面受敌 一往无前 "Beset on Three Sides,
  Ever Forward" - the FULL chapter (161 body paragraphs) delivering on ch23. The "new plan";
  the anatomy of the three-sided enemy (SMP Special Branch under 劳勃生; French Concession
  police; the Japanese gendarmerie + poison unit + torture catalogue; No.76); the Yu Yefeng
  sanction at the 更新舞台 (Gengxin Stage, Jan 1940) told through PARALLEL press/memoir accounts.
  drop=2; 3 merges; 6 sub-headings (1 standalone couplet REUSING ch14, 1 head-glued (一), 1
  standalone (二), 3 tail-glued couplets). 6 notes (232 cumulative); 9 glossary rows.
- **Batch B19 (ch25), Part Three Chapter 5.** 第五章 全面检讨奇人奇事 "A Full Reckoning:
  Remarkable People, Remarkable Deeds" - a FULL chapter (183 body paragraphs) continuing the
  reckoning. Three movements: (a) Dai Li's work-directives reproduced under the run-in labels
  情报/破坏/行动 + a 15-point 检讨总结 self-criticism; (b) the 144-Mauser arms-gift episode (Hu
  Yongquan, Qi Qingbin's counsel, the Sihang-Warehouse telegram, the German "Mr. Shi" via the
  eye-doctor Nie Chonghou); (c) the stalled Zhang Xiaolin sanction, Pan Zixin, and the Fan Xing
  intelligence-source puzzle vs the CCP Shanghai underground (Pan Hannian). **drop=2; NINE
  merges** - 2 intra-<p> <br/> pairs (a NEW trigger; the extractor renders <br/> as a newline)
  + 7 severed-<p> boundaries (2 of them CHAINING into a <br/> pair), which the B18 kickoff's
  coarse "191=191<p>" reconciliation missed but CLAUDE.md's merge rule requires (parity is
  data/zh↔reading.md = 183/183, NOT the raw <p> count). **3 sub-headings** (L3 standalone
  couplet + L88/L126 tail-glued story titles); the four 情报部份─/破坏部份─/行动部份─/检讨总结─
  work-review dividers kept INLINE as run-in labels (source formats them inconsistently). NO
  images, NO note markers. **183 body paragraphs; 10 notes (242 cumulative); 5 net new glossary
  rows** (4 pre-existed). All checks green; qa_epub PASS; epubcheck 0/0/0/0. **EPUB now 25/43
  chapters.** Detail in PROGRESS.md ("Batch B19").

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` - derives data/zh/<id>.txt verbatim from data/src,
  applying per-unit drops/merges/heading-splits with a source-conservation check.
  Specs for ch01-ch25. Merge logic FOLLOWS CHAINS. **drop is variable:** most chapters
  drop=2; ch01/ch10/ch20 drop=3. `standalone` = a sub-heading kept as its own <p> with
  no heading markup, emitted as a `### ` line; `glued` = a sub-heading fused onto a
  paragraph's TAIL (endswith), split off; `glued_head` (B18) = a heading fused onto a
  paragraph's HEAD (startswith), split off; `merges` = source <p> pairs that sever one
  sentence OR an intra-<p> `<br/>` line break (B19; the extractor renders `<br/>` as a
  newline, so a <p> with N `<br/>` is just a chain of N+1 body lines). The
  `.get("glued_head", {})` default leaves earlier units untouched.
- `scripts/batch_artifacts.py` - derives out/<id>_en.json FROM out/<id>_reading.md
  and writes checks.json. Author the reading.md; run this. **TRAP: running it with an
  ID writes checks.json with ONLY that unit; ALWAYS finish with a no-arg run** so
  check_structure/check_content see every unit. `body_lines` strips `#`-headings,
  `***`, and the `{vdgp}` set-off prefix.
- `scripts/verify_unit.py <id>` - parity + numbers (auto-finds data/noise.txt; do NOT
  pass --noise, it is treated as a cid) + anchors. Run per unit.
- `scripts/build_reading_epub.py` - builds out/nameless-heroes.epub from book.json +
  the reading.md/en.json + notes.json + glossary.json + figures.json. It uses
  book.json `title_en` for the visible chapter heading (H1); `### ` sub-headings render
  as <h2>; note bodies collect in OEBPS/notes.xhtml as <aside epub:type="footnote"> with
  epub:type="noteref" markers in the chapter (popup semantics).
- `scripts/check_content.py` (patched) - name_map skips "_"-prefixed glossary
  categories/entries. It flags KNOWN PRE-EXISTING artifacts and exits NONZERO because
  of them: **ch08 Shunde (3), ch13 Miss Nguyen/Oya Kusuo/Yuan Haowen (9), and ch09 "Jize
  County" (1, para 220 - the 鸡泽县 key added in B16 surfaces an older ch09 rendering; a
  whole-book reconciliation item)** - NOT regressions. The pass criterion for a NEW batch is
  "the batch's own unit shows all name occurrences in the paired paragraph / 0 displaced."
  A NEW unit's displacements are almost always a keyed name/place rendered a DIFFERENT way
  than the glossary: align the English (or, for a clear case-only place mismatch, the
  glossary) to the keyed form. B18's were all PINYIN-vs-POSTAL city names; B19 had none.
  Do NOT add book-TITLE or COMMON-NOUN keys.
- **Verse marker `{p}`** (first used ch13): prefix a pure-verse line with `{p} `; the
  builder renders `<p class="verse">`; the checks strip it.
- Glossary is authored/merged BY HAND into the SECTIONED file
  (book/people/organizations/places/terms), idempotent + re-read-verified. **Every row
  MUST carry a `pinyin` field** - `qc_entities.py` does `rec["pinyin"]` and KeyErrors
  otherwise. `scripts/add_ch25_glossary.py` is the by-hand pattern: it asserts each hanzi
  key is a substring of data/zh/<id>.txt to catch a Write-tool mangling. A `/`-joined key
  (e.g. 俞叶封/兪叶封) holds alternate hanzi for one referent; qc splits on `/`. apparatus_merge's
  glossary path assumes a FLAT map and would corrupt the sectioned file; NOTES still go
  through apparatus_merge.py.
- **qc_entities catches term-rendering drift too:** a glossary common-noun term rendered
  a different way flags as a "miss." Align the English to the glossary (督察 "inspector";
  use "inspectorate" for the abstract function - it still carries the "inspector" substring).
- **GLOSSARY-KEY DISCIPLINE:** a key must be a DISTINCTIVE proper noun that renders ONE way
  everywhere and must NOT occur elsewhere with a different rendering. Periodicals and books
  are FOOTNOTES/inline, not glossary keys. One-off transliterated Western/Japanese officer
  names, one-off telegram-roster names, and attested Shanghai ROADS are rendered inline, not
  keyed. A bare surname whose full name is unknown is rendered inline.
- **Note-anchor gotchas:** anchors must be ASCII, WITHOUT any quote/apostrophe character
  AND without an em dash (U+2014) - all substring traps. The reading.md uses curly
  quotes/apostrophes and em dashes freely, so pick an anchor phrase with none of them (B19
  used "Comrade Qin Qirong", "twenty thousand yuan a day", "the firewood from under the
  cauldron", "the Sihang Warehouse", "pidgin", "his father-in-law", "xieke huang", "heavier
  than Mount Tai"). Multi-occurrence anchors attach at the FIRST occurrence.
- **make_ch25_apparatus.py pattern (scripts/):** author note bodies as plain ASCII + typed
  hanzi in a Python file, ASSERT every non-ASCII glyph occurs in data/zh/<id>.txt (a
  Write-tool corruption produces a glyph absent from the source and trips the assert), then
  convert every non-ASCII char to a numeric char ref and run apparatus_merge.py. **NEW B19
  caveat:** a CORRECT glyph may be ABSENT if the source prints a glitch/variant (洋泾浜's 泾/浜
  were absent, only the source's 洋经滨 present; 孤军/司马迁 not in ch25's source) - describe
  such terms with the source's own form + pinyin/English, not the correct hanzi.
- data/noise.txt carries the B01-B19 project noise rules (each with a comment line).
  Republican years render literally; the checker matches the source numeral (or auto-escapes
  Republican-year N via N+1911). **The elided-tens block is ordered LONGEST-FIRST.**
  Name-numeral glyphs are noised. Idiom numerals are noised. **The ○ (U+25CB) address
  artifact:** the checker cannot read ○ as zero - noise the mis-read glyph-string, carry the
  real value in the English. **× (source redaction)** renders as an em-dash blank (自×月份起,
  贺×同志, ×棋, 陈××先生 in B19). Every REAL value is CARRIED and matched as DIGITS (the B19
  demolition-brigade table, the 144→140 Mausers/13,000 rounds, 150,000 funds, and the ch24-
  identical twenty-ninth-year budget 11,000 men / 510,000-odd yuan).
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches it; re-run
  per session). setup.sh's ONE failing regression test ("hook stands down on template
  stub") is a KNOWN false alarm; all other regression tests pass.

## Renderings settled / carry-forward

- 军统 / 军统局 -> "the Juntong" / "the Juntong Bureau" (DECIDED). 戴笠 Dai Li (courtesy Yunong;
  老板 "the Boss"; 戴先生 "Mr. Dai"; 戴雨农 "Dai Yunong"); 汪精卫 Wang Jingwei (汪逆 "the traitor
  Wang"). 制裁 "sanction"; 制裁令 "sanction order." 敌伪 "the enemy and the puppets"; 汪伪 "Wang
  puppets"; 沦陷区/沦陷地区 "the fallen zone(s)"; 战区 "war zone"; 后方 "the rear"; 区长 "District
  Chief"; 督察 "inspector" / "inspectorate"; 总督察 "Chief Inspector"; 第二处 "the Second
  Section." Chiang's titles: 校长 "the Commandant", 委员长 "the Generalissimo", 委座 "the
  Generalissimo", 总裁 "the Director-General"; 总长 "the Chief of the General Staff" (=何应钦
  He Yingqin, NOTED ch09). 领袖 "the Leader" (Chiang). 总理 = "the Party Leader" = Sun Yat-sen.
  日本宪兵队 "the Japanese gendarmerie"; 七十六号 "No. 76"; 特工总部 "Special Operations
  Headquarters"; 工部局 "Municipal Council"; 公共租界 "International Settlement"; 法租界 "French
  Concession"; 巡捕房 the Concession police / "police station."
- **PLACE-NAME CONVENTION (the qc gate enforces the glossary's PINYIN for keyed cities):**
  北平 Beiping, 天津 Tianjin, 汉口 Hankou, 四川 Sichuan, 虹口 Hongkou (NOT Peiping/Tientsin/
  Hankow/Szechuen/Hongkew). Non-keyed attested Shanghai ROADS keep their historical forms:
  Seymour Road (西摩路), Route Doumer (杜美路), Route de Grouchy (格罗希路), Carlton Apartments
  (卡尔登公寓), Bubbling Well Road (静安寺路), Newchwang Road (牛庄路), Jessfield Road (极司非而路),
  Avenue Edward VII (爱多亚路), Gordon Road (戈登路), Weihaiwei Road (威海卫路), North Sichuan
  Road (北四川路 - 四川 pinyin); SMP stations (Louza, Sinza, Wayside, Yangtszepoo…) keep their
  attested names. Concession-street rule (B16): keep attested names, use pinyin for the
  uncertain rather than invent a French name.
- **Book / part titles (in-text; DECIDED; reuse verbatim):** 英雄无名 = "Nameless Heroes";
  Part One 北国锄奸 = "Rooting Out Traitors in the North"; Part Two = "Disgrace at Hanoi";
  Part Three 百战声威 = "Renown Won in a Hundred Battles." 蓝衣社 = "the Blue Shirt Society"
  (NOTED ch08). 忠义救国军 = "the Loyal and Patriotic Army" (NOTED ch21). 抗日杀奸团/抗团 =
  "Anti-Japanese Traitor-Killing Corps"/"Kang Corps" (NOTED ch02/ch11). 新亚和平促进会 = "New
  Asia Peace Promotion Association" (ch22). Books handled by FOOTNOTE/inline (not glossary):
  蒋总统秘录, 戴雨农先生传, 汪政权的开场与收场, 沪滨三次历险实录, 沪上往事 (Wan Molin's memoir,
  NOTED ch22); periodicals: 申报 (Shenbao, NOTED ch24), 新申报 / 中华日报 (occupation papers,
  NOTED ch20), 民族晚报.
- **B15/B16 shelf (ch21/ch22 casts; reuse; all keyed with pinyin):** 郑修元 Zheng Xiuyuan,
  陈第容/陈明楚 Chen Dirong/Chen Mingchu, 黄志远 Huang Zhiyuan, 赵理君 Zhao Lijun, 刘原深 Liu
  Yuanshen, 吉震苍 Ji Zhencang, 毕高奎 Bi Gaokui, 孙大成 Sun Dacheng, 万里浪 Wan Lilang, 张璜
  Zhang Huang, 戴藏宜 Dai Cangyi, 杜月笙 Du Yuesheng (NOTED ch17), 朱啸谷 Zhu Xiaogu, 程海涛
  Cheng Haitao, 耿嘉基 Geng Jiaji, 何行健/何天风 He Xingjian/He Tianfeng, 俞叶封 Yu Yefeng, 万墨林
  Wan Molin, 邵飘萍 Shao Piaowei (NOTED), 陈默 Chen Mo, 赵刚义 Zhao Gangyi, 范纪曼 Fan Jiman
  (alias of 范行 Fan Xing), 张啸林/杜/黄金荣 the three Green-Gang tycoons (张啸林 NOTED ch04).
- **B18 shelf (ch24; reuse; all keyed with pinyin unless noted inline):** 劳勃生 Lao Bosheng
  (NOTED); 更新舞台 Gengxin Stage; 新艳秋 Xin Yanqiu (NOTED); 袁殊 Yuan Shu (NOTED); 吴世宝 Wu
  Shibao, 胡均鹤 Hu Junhe, 傅也文 Fu Yewen (No.76); 刘俊卿 Liu Junqing, 蒋福田 Jiang Futian
  (concession police); 刘绍奎 Liu Shaokui, 周伟龙 Zhou Weilong, 吴佩孚 Wu Peifu (三不主义 NOTED);
  gendarmerie officers rendered INLINE (romaji).
- **B19 shelf (ch25; reuse; all keyed with pinyin unless noted):** 秦启荣 Qin Qirong (NOTED -
  Shandong guerrilla commander); 毛人凤 Mao Renfeng (NOTED - Dai's deputy, later Juntong chief);
  潘汉年 Pan Hannian (NOTED - CCP Shanghai intelligence chief); 高荣 Gao Rong (Suiyuan Station,
  Chen's schoolmate); 聂崇侯 Nie Chonghou (eye doctor); 潘子欣 Pan Zixin ("Master Pan the
  Seventh," Tianjin notable); 胡永荃 Hu Yongquan (the fixer); 彭雅萝 Peng Yaluo (Fan Xing's
  companion); 兪叶封 = 俞叶封 Yu Yefeng (variant glyph, keyed). NEW ch25 notes: Qin Qirong; the
  每日/每月 directive discrepancy; Mao Renfeng; 釜底抽薪; the Sihang Warehouse / lone battalion;
  pidgin/Yangjingbang; Pan Hannian + the CCP Jiangsu Committee; 老泰山 (father-in-law); 蟹壳黄
  xieke huang; Sima Qian's "heavier than Mount Tai." Rendered INLINE (not keyed): the telegram
  names 钱新民/廖公劭, 刘方雄, the sabotage operatives 方步舟/谢冰/岳烛远/谢镇南/邹适, the CCP
  roster 刘晓/刘长胜/张爱萍/刘宁一/王尧山/沙文汉/张执一/刘少文, 叶吉卿, the German "Mr. Shi."

## ⚠ Name trap RESOLVED (do not reopen): 陈邦国 / 郑邦国

The Hanoi action-team member the source spells 郑邦国 in ch13 and 陈邦国 in ch15/ch16/ch17
is ONE man. RESOLVED to **Chen Bangguo (陈邦国)**: glossary key renamed; the built ch13 unit
updated; the discrepancy footnoted at the first ch15 occurrence. Use Chen Bangguo consistently.

## Voice sheet - CHEN GONGSHU (author / narrator)

- REGISTER: educated, formal, essayistic first person; grave and a touch archaic but not
  stilted. Long semicolon-joined clauses; four-character idiom and classical allusion used
  freely and footnoted when they carry weight. Refers to himself as 笔者 "the writer" and
  我 "I." His narrating "shall" is DELIBERATE - do not de-formalize it; check_register flags
  it informationally (B06 33%, B08 29%, B12 43%, B14 0%, B15 33%, B16 36%, B18 25%, B19 67%
  - elevated because the chapter reproduces many imperative Dai Li directives).
- STANCE: self-justifying yet self-effacing; insists on truthfulness, admits his blunders;
  tender toward dead comrades, bitter and scornful toward the enemy. When quoting hostile/
  puppet or comrades' documents, keep the quoted register DISTINCT from Chen's own dry scorn
  (ch21/ch22/ch24/ch25 do this for the memoirs, Dai's telegrams and directives, and news reports).
- Ratio ~4.55-4.78 en/han in narrative; prefaces denser (~5.2-5.3); document-heavy chapters
  run higher (ch21 4.89, ch22 4.70, ch24 5.33, ch25 4.97 median). Read the note, do not reset.

## Voice sheets - principal & recurring cast

- **DAI LI (戴雨农 / Mr. Dai / 老板 "the Boss").** After ch17 he and Chen meet no more, only
  letters and telegrams; his word is "as a mountain." Warm off duty, abrupt on business. In
  ch24 he makes his one lifetime self-criticism; in ch25 his work-directives are reproduced at
  length and he refuses to let subordinates raise their own funds - so Chen takes the arms-gift
  on his own shoulders.
- **QI QINGBIN (齐庆斌, alt. Ruozhai) & ZHANG ZUOXING (张作兴, alt. Kexin).** Chen's childhood
  friends (Part One ch06); the Shanghai District secretary and radio inspector. In ch25 Qingbin
  counsels Chen to keep the arms-gift against a future mass action, and Zuoxing takes delivery.
- **ZHENG XIUYUAN (郑修元).** District secretary who held the Shanghai District together; his
  memoir quoted in ch21/ch22. Transferred out (Dec 1939).
- **LIU YUANSHEN (刘原深).** The very man who revises "Nameless Heroes" for Chen; his living
  memory-check throughout Part Three. Consult on every Shanghai-cast recall.
- **BI GAOKUI / HUANG ZHIYUAN (毕高奎 / 黄志远).** Leader and deputy of New Group One; Bi held
  the First Intelligence Group concurrently.
- **CHEN MO (陈默).** Detachment/cell leader of the Second Action Brigade; led the Yu Yefeng
  sanction (Jan 1940, ch24).
- **FAN XING / FAN JIMAN (范行 / 范纪曼).** The "communications man" of tangled background whose
  intelligence-source Chen cannot fathom; the long ch25 puzzle (probably CP-tied, but his
  material outclasses the CCP's Shanghai product, so not a CCP double-agent). "A man of feeling."
- **Dead comrades carried in memory:** ZENG CHE 曾澈, WANG WEN 王文 (ch11); ZENG ZHONGMING
  曾仲鸣 (ch15/ch16); 陈三才 Chen Sancai (ch21/ch22); 丁文蕙 Ding Wenhui (ch22, the Qingdao martyr).

## Where the book stands

- Part One (北国锄奸) COMPLETE (B01-B05).
- Part Two ("Disgrace at Hanoi") COMPLETE (B06-B13).
- **Part Three ("Renown Won in a Hundred Battles" / 百战声威) is under way (B14-B19).** ch20 =
  self-preface; ch21 = arrival + order of battle; ch22 = the first 1940 sanctions + Fan Xing;
  ch23 = the "three-sided enemy" framing bridge; ch24 = the anatomy of the three-sided enemy +
  the Yu Yefeng sanction + Dai's self-review; ch25 = the full work-review + the arms-gift + the
  Fan Xing intelligence puzzle.
- **NEXT: B20 = ch26** - 第六章 泰山鸿毛 同此一掷 "Chapter 6. Mount Tai or a Feather, All on One
  Throw," a FULL chapter (~19,000 chars, 1 <h2> + 280 <p> + 54 <br/>). drop=2; the 54 <br/> are
  intra-<p> line breaks = 54 MERGE pairs/chains (do the byte-exact p-by-p diff FIRST), PLUS grep
  for severed-<p> boundaries (cf. ch25's 7). Opening sub-heading L3 没有名籍生死不明的先烈们
  (standalone). The 上海职工运动委员会 / worker-movement martyrs. No images, no note markers.

## What is NEXT

- Batch B20 = ch26 (full chapter). Kickoff is the paste-block at the top. Runs to completion
  (no gate); ends by pasting the B21 kickoff. B21 = ch27 (titled 第八章 - Part Three SKIPS
  第七章, a faithful numbering gap; confirm ch27's title_en in book.json). NOTE: book.json's
  batches array lumps ch23+ch24 as "B17"; the working plan runs ONE AHEAD from ch24 on (ch24 =
  B18, ch25 = B19, ch26 = B20).
- The frozen register reference is `reference/B01_frozen.md`. Narrative sits at 4.55-4.78
  en/han; prefaces/document-heavy chapters run higher (ch24 = 5.33, ch25 = 4.97) - alignment/
  register are the gates, not the raw ratio.
- Sub-heading pattern DIFFERS by chapter. Styles seen: Part One numbered 一/二/三;
  ch11/ch14/ch20-title/ch21/ch22/ch23/ch24/ch25 COUPLET-STYLE with NO number prefix;
  ch12/ch13/ch15/ch16/ch17/ch18/ch24-sections numbered-in-parens (一)/(二)…; GLUED sub-heads
  seen ch08/ch16/ch18/ch22 (tail), ch24 (BOTH tail and HEAD), ch25 (two tail-glued story
  titles); ch25 also has run-in section LABELS (情报部份─ etc.) kept INLINE as prose, distinct
  from headings. Grep each new chapter p-by-p, and DISTINGUISH enumerated LIST items (per
  parity) from (一)/(二) SECTION headings and from run-in labels.
- WATCH for source anomalies: cuts, misplaced-「 glitches, corrupt/dropped-character phrases,
  dropped full stops, the in-text "(第N章完，下期续载)" coda/magazine-seam pattern, a STRAY glyph
  fused onto a chapter title (ch22's 杀), a STRAY orphan enumerator (ch24's "(一)"), the ○
  (U+25CB) circle-zero and × redactions in addresses/names (ch24/ch25), and pervasive single-
  character substitutions. Intra-<p> `<br/>` line breaks are MERGE pairs/chains, not paragraph
  boundaries (ch25 had 2; ch26 has FIFTY-FOUR - do the byte-exact p-by-p diff FIRST). Severed-<p>
  boundaries (a source <p> ending non-terminal) ALSO merge (ch25 had 7). Re-grep each batch's
  source for `\[\d+\]` note markers (none through B19).

## Open items for the read-through / completion

- Feed decided renderings back to authority.json on completion: 军统 "the Juntong"; the full
  B02-B19 historical-name set (Part One; the Japanese/negotiator names; the Wang-essay set;
  the Part-Two Hanoi/Chongqing casts; the martyrs; the Shanghai-District staff, order of
  battle, the B16 operative/collaborator cast, the B18 SMP/gendarmerie/No.76 cast, and the B19
  Juntong-directive/arms-gift/Fan-Xing cast).
- Japanese name readings to verify when the men recur (多田骏, 田代皖一郎, 土肥原贤二, 板垣征四郎,
  近卫文麿, 影佐祯昭, 今井武夫, 晴气庆胤; 大屋久寿雄; 横山秋马; 岩井英一; the B18 gendarmerie
  officers - rendered inline, romaji to firm up).
- Provisional romanizations to firm up when sources allow (glossary `provisional` rows, incl.
  the Shanghai-District cast, the B16 operatives, the B18 rows 劳勃生/傅也文/刘俊卿/蒋福田, and
  the B19 rows 聂崇侯/潘子欣/胡永荃/彭雅萝/高荣).
- Whole-book reconciliation items: ch09 "Jize County" (para 220, the 鸡泽县 key); the pinyin-
  vs-postal city names (standardized to pinyin for keyed cities from B18). Stray source glyph
  still to resolve: 毛酋 in a ch36 section title.

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01-B19 builds (0/0/0/0). Source is a clean
  digital EPUB, predominantly simplified with residual variant glyphs and pervasive
  digitization glitches (list them, render to plain sense, do not footnote mechanical typos).
  B01-B19 glitch lists are in PROGRESS.md.
- Running-header line 英雄无名-陈恭澍 opens all 43 content files: drop it. drop count is
  variable - most drop=2; ch01/ch10/ch20 drop=3.
- Enumerated ；/：/、 bullet lists, quoted-document/directive/roster lines, salutations, verse
  lines, juxtaposition lines, run-in section labels (情报部份─ etc.), and 『』-closed dialogue
  are DELIBERATE separate `<p>` - do NOT merge them; only genuine mid-phrase splits (last char
  not terminal, OR a source `<p>` boundary that severs one sentence, OR an intra-<p> `<br/>`)
  merge, and those can CHAIN. A line ending on a dash lead-in that is its OWN source `<p>` is
  DELIBERATE, NOT a split. ALWAYS confirm the extracted body count p-by-p against data/src_epub.
- Faithful numbering gaps/anomalies (NOT errors): Part Three skips 第七章 (ch27 = 第八章),
  splits ch10 into (上)/(下); 三面受敌 一往无前 titles two chapters (ch14 and ch24); ch09 printed
  §五 before §四; ch13 restarts its (一)-(五) numbering; ch16 reproduces two whole Wang
  documents; ch21/ch22/ch24 carry magazine "下期续载" seams; ch24 has a source-internal date
  slip; ch25 has a 每日/每月 directive discrepancy (footnoted). Preserve and, where a reader
  would stumble, footnote.
- Expect a stray per-task branch at the top of every batch; consolidate onto
  claude/nameless-heroes per rule 2.
