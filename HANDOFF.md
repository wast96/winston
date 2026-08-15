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
Nameless Heroes B19

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once (its ONE failing regression test, "hook stands down on template stub", is a KNOWN false alarm; all others pass), then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05), B02 (ch06), B03 (ch07), B04 (ch08), B05 (ch09), B06 (ch10 preface + ch11), B07 (ch12), B08 (ch13), B09 (ch14), B10 (ch15), B11 (ch16), B12 (ch17), B13 (ch18 + ch19), B14 (ch20), B15 (ch21), B16 (ch22), B17 (ch23) and B18 (ch24) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them. PART TWO ("Disgrace at Hanoi") is COMPLETE; PART THREE ("Renown Won in a Hundred Battles" / 百战声威) is under way (ch20 self-preface + ch21/ch22/ch23/ch24). The EPUB now holds 24/43 chapters, 232 notes.

Do Batch B19 = ch25 (ONE unit, ~15,600 source chars, a FULL chapter): ch25 = 第五章 全面检讨奇人奇事 "Chapter 5. A Full Reckoning: Remarkable People, Remarkable Deeds." NOTE on batch numbering: book.json's batches array lumps ch23+ch24 as "B17", so the working batch labels run ONE AHEAD of the book.json array from ch24 on (ch24 = B18, ch25 = B19). Read the tail of ch24 English (out/ch24_reading.md) and ch22/ch23/ch24 for register + story continuity; ch24 closed on Dai Li's system-wide Juntong self-review and the arms-donation episode (the "friend" of unclear background), which ch25 ("a full reckoning") continues. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch25 from data/src (26_index-split-000-0024.txt). CONFIRM structure p-by-p against data/src_epub/OEBPS/Text/index_split_000_0024.xhtml [parses to 1 <h2> + 191 <p> + 2 <br/>, NO <h1>, NO <img>, NO [\d+] note markers]. drop=2 (running header 英雄无名-陈恭澍 + <h2> chapter title). RECONCILE the body count: the txt is ~195 awk-NR lines but the XHTML has 191 <p>; the difference is the TWO <br/> tags, which sit INSIDE a <p> (an intra-paragraph line break the extractor renders as a newline) - so they are TWO MERGE pairs to rejoin, NOT paragraph boundaries. The two are at XHTML L99 (…爆破器材等。<br/>以及和主管人事的部门治商人事问题。) and L215 (…庆斌兄的确比我有见地。<br/>而况且这原是公家之物…) - both first parts end on a terminal 。 but are the SAME <p>, so MERGE regardless (this is a NEW merge trigger vs ch24's severed-sentence merges - a <br/> inside one <p>). After the 2 merges the body should be 191 lines = 191 <p>, 1:1. Sub-heading: p#0/L3 八年抗战初期「军统局」工作检讨 is the opening sub-heading (couplet-style, cf. ch11/ch14/ch21/ch22/ch23/ch24-couplet) - standalone. GREP p-by-p for further standalone/glued/(一)-(二)-parens section headings (ch24 had a head-glued (一) + tail-glued couplet section headings; watch for the same "three-tell" - standalone, tail-glued ending non-terminal OR in a full-width 」, and head-glued (一)X).
2. Extend scripts/clean_batch.py with ch25's spec (drop=2; the 2 <br/> merges; the confirmed standalone/glued headings). It already supports merges (chains), standalone, tail-glued `glued`, and (NEW in B18) head-glued `glued_head`. Run it (source-conservation check must pass). Write out/ch25_reading.md (## from book.json title_en; one English paragraph per source body line; sub-headings as ### ; any enumerated-list items as ordinary paragraphs per parity). Then run scripts/batch_artifacts.py ch25, and ALWAYS finish with a NO-ARG run (the trap: an ID-run writes checks.json with ONLY that unit; the no-arg run restores all 25 units so check_structure/check_content see them).
3. Translate to the FROZEN register (Chen's voice sheet in HANDOFF; document-heavy chapters run higher - ch24 measured 5.33 on its many short quoted/table/juxtaposition lines; read the note, do not reset). Consult glossary.json and authority.json BEFORE romanizing anything; REUSE the settled Part-Three renderings (see the "Renderings settled" and "B18 shelf" sections of HANDOFF - all keyed with pinyin where keyed): the Shanghai District; the Juntong; 制裁 "sanction"; 督察 "inspector" (align common-noun terms to the glossary - the qc_entities gate); 敌伪 "the enemy and the puppets"; 特工总部/七十六号 "Special Operations Headquarters"/"No. 76" (丁默邨 Ding Mocun/李士群 Li Shiqun, NOTED - do NOT re-note); 公共租界 "International Settlement"/法租界 "French Concession" (NOTED ch04); 工部局 "Municipal Council"; 日本宪兵队 "the Japanese gendarmerie"; 齐庆斌 Qi Qingbin (兄=Brother); 戴雨农 Dai Yunong/Mr. Dai. IMPORTANT place-name convention (the check_content/qc_entities gate): keyed CITY/PROVINCE names render in PINYIN per the glossary - 北平 Beiping, 天津 Tianjin, 汉口 Hankou, 四川 Sichuan, 虹口 Hongkou (NOT the postal Peiping/Tientsin/Hankow/Szechuen/Hongkew); non-keyed attested Shanghai ROADS keep their historical names (Newchwang Road, Jessfield Road, Avenue Edward VII, etc.). Render Republican years literally (二十六年 = "the twenty-sixth year"; the checker matches the source numeral). WATCH ch25's digitization glitches (list in PROGRESS.md, render to plain sense, footnote only real reading uncertainty): the same classes seen ch15-ch24, and watch the ○ (U+25CB circle-zero) in any room/lane/phone numbers (the numeric checker mis-reads ○ - carry the real value in the English and noise only the mis-read glyph-string, as B18 did for 五○○; four-digit ○ addresses may need word-forms so the checker's split values match). Dates/counts: carry real values; NOISE only idiom/approximate/name-numeral forms (data/noise.txt already carries the B01-B18 rules; add ch25's).
4. Checks: verify_unit.py ch25 (parity + numbers with noise auto-found + anchors); check_align.py ch25; regenerate checks.json with scripts/batch_artifacts.py (no args) and run check_structure.py --config checks.json + check_content.py --config checks.json (NOTE: check_content prints KNOWN PRE-EXISTING artifacts and exits nonzero because of them - ch08 Shunde ×3, ch13 Miss Nguyen/Oya Kusuo/Yuan Haowen ×9, ch09 "Jize County" ×1; CONFIRM ch25 itself shows "all in the paired paragraph" / 0 displaced, and align any keyed name/place to its glossary-decided rendering - the usual B18 fix was pinyin-vs-postal city names). Do NOT add COMMON-NOUN or book/periodical keys. qc_entities.py on a reconstructed bilingual (data/zh body lines + out/ch25_en.json, `> zh` / en pairs, strip the ### heading lines; every glossary row needs a pinyin field). Verify the TAIL against the source (critical on a 15k+ single-pass unit - the corruption class hides in the last paragraphs). check_register.py --ref reference/B01_frozen.md out/ch25_reading.md ("shall" in Chen's narration is deliberate - read the note, do not de-formalize; ch24 ran 25%).
5. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (full list in PROGRESS.md; the big already-covered furniture: No.76/特工总部/丁默邨/李士群 ch04/ch17, the concessions ch04, the gendarmerie ch11/ch23, 制裁, the Blue Shirts ch05/ch08, the Green-Gang three tycoons ch04, 沪上往事/万墨林 ch22, 申报/新申报/中华日报 ch20/ch24, the Republican calendar, and the whole Shanghai cast). ch25 is a "full reckoning" chapter (奇人奇事 "remarkable people and deeds") - expect genuinely new furniture (people, cases) that earns notes; be generous but do NOT pad, do NOT re-note. Merge notes via apparatus_merge.py (numeric character references only in note bodies; anchors verbatim ASCII substrings of the reading.md body text, NO em dash and NO quote/apostrophe character - substring traps; multi-occurrence anchors attach at the first). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field; apparatus_merge's glossary path assumes a FLAT map and would corrupt the sectioned file - use it ONLY for notes; scripts/add_ch24_glossary.py is the by-hand pattern, asserting each hanzi key against data/zh). Confirm ch25 carries no images (its XHTML has NO <img> - confirm). For any CJK in a note body use the make_ch24_apparatus.py pattern (author bodies with typed hanzi, ASSERT every non-ASCII glyph is present in data/zh/ch25.txt, then convert to NCRs) to defeat the CJK-mangling hazard.
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; update HANDOFF.md; commit and push to claude/nameless-heroes. (next is B20 = ch26, 第六章 泰山鸿毛 同此一掷 "Chapter 6. Mount Tai or a Feather, All on One Throw"; note ch27 is titled 第八章 - Part Three skips 第七章, a faithful numbering gap.)

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B20 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
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
- **Batch B18 (ch24), Part Three Chapter 4.** ch24 = 第四章 三面受敌 一往无前 "Chapter 4. Beset
  on Three Sides, Ever Forward" - the FULL chapter (161 body paragraphs) that DELIVERS on
  ch23. The "new plan" (single/secret accounts + wireless; the great personnel transfer);
  the anatomy of the three-sided enemy section by section (the Settlement police / SMP
  Special Branch under 劳勃生; the French Concession police; the Shanghai Japanese Gendarmerie
  and its poison unit + torture catalogue; No.76 - layout, "black gaol," four tortures, three
  crimes); and the Yu Yefeng sanction at the 更新舞台 (Gengxin Stage, Jan 1940) told through
  PARALLEL press/memoir accounts (「沪上往事」 vs the 「申报」 vs a third eyewitness). Closes on
  Dai's Juntong self-review + the arms donation. drop=2; **3 merges** (L26/27 克莱登
  parenthetical, L106/107 逮捕, L11/12 a STRAY orphan "(一)" absorbed); **6 sub-headings**
  (L3 standalone couplet REUSING ch14; L33 **head-glued** (一)公共租界巡捕房; L38 standalone
  (二)法租界巡捕房; L46/L95/L122 **tail-glued** section couplets - L95 罪恶昭彰的「七十六号」 ends
  in a 」, easy to miss). NO images, NO note markers. **161 body paragraphs; 6 notes (232
  cumulative); 9 glossary rows (8 people + 更新舞台).** All checks green; qa_epub PASS;
  epubcheck 0/0/0/0. **EPUB now 24/43 chapters.** Detail in PROGRESS.md ("Batch B18").

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` - derives data/zh/<id>.txt verbatim from data/src,
  applying per-unit drops/merges/heading-splits with a source-conservation check.
  Specs for ch01-ch24. Merge logic FOLLOWS CHAINS. **drop is variable:** most chapters
  drop=2; ch01/ch10/ch20 drop=3. `standalone` = a sub-heading kept as its own <p> with
  no heading markup, emitted as a `### ` line; `glued` = a sub-heading fused onto a
  paragraph's TAIL (endswith), split off; **`glued_head` (NEW in B18) = a heading fused
  onto a paragraph's HEAD (startswith), split off** (e.g. ch24 L33 (一)公共租界巡捕房); the
  `.get("glued_head", {})` default leaves all earlier units untouched; `merges` = source
  <p> pairs that sever one sentence OR (ch25) an intra-<p> `<br/>` line break.
- `scripts/batch_artifacts.py` - derives out/<id>_en.json FROM out/<id>_reading.md
  and writes checks.json. Author the reading.md; run this. **TRAP: running it with an
  ID writes checks.json with ONLY that unit; ALWAYS finish with a no-arg run** so
  check_structure/check_content see every unit. `body_lines` strips `#`-headings,
  `***`, and the `{vdgp}` set-off prefix.
- `scripts/verify_unit.py <id>` - parity + numbers (auto-finds data/noise.txt; do NOT
  pass --noise, it is treated as a cid) + anchors. Run per unit.
- `scripts/build_reading_epub.py` - builds out/nameless-heroes.epub from book.json +
  the reading.md/en.json + notes.json + glossary.json + figures.json. It uses
  book.json `title_en` for the visible chapter heading, so a residual glitch in the
  hanzi `title` field never surfaces.
- `scripts/check_content.py` (patched) - name_map skips "_"-prefixed glossary
  categories/entries. It flags KNOWN PRE-EXISTING artifacts and exits NONZERO because
  of them: **ch08 Shunde (3), ch13 Miss Nguyen/Oya Kusuo/Yuan Haowen (9), and ch09 "Jize
  County" (1, para 220 - the 鸡泽县 key added in B16 surfaces an older ch09 rendering; a
  whole-book reconciliation item)** - NOT regressions. The pass criterion for a NEW batch is
  "the batch's own unit shows all name occurrences in the paired paragraph / 0 displaced."
  A NEW unit's displacements are almost always a keyed name/place rendered a DIFFERENT way
  than the glossary: align the English (or, for a clear case-only place mismatch, the
  glossary) to the keyed form. **B18's were all PINYIN-vs-POSTAL city names** (Beiping not
  Peiping, Tianjin not Tientsin, Hankou not Hankow, Sichuan not Szechuen, Hongkou not
  Hongkew) plus 新一组 "New Group One" - the keyed glossary form (pinyin) wins for cities;
  non-keyed attested Shanghai ROADS keep their historical names. Do NOT add book-TITLE or
  COMMON-NOUN keys.
- **Verse marker `{p}`** (first used ch13): prefix a pure-verse line with `{p} `; the
  builder renders `<p class="verse">`; the checks strip it.
- Glossary is authored/merged BY HAND into the SECTIONED file
  (book/people/organizations/places/terms), idempotent + re-read-verified. **Every row
  MUST carry a `pinyin` field** - `qc_entities.py` does `rec["pinyin"]` and KeyErrors
  otherwise. `scripts/add_ch24_glossary.py` is the by-hand pattern: it asserts each hanzi
  key is a substring of data/zh/<id>.txt to catch a Write-tool mangling. apparatus_merge's
  glossary path assumes a FLAT map and would corrupt the sectioned file; NOTES still go
  through apparatus_merge.py.
- **qc_entities catches term-rendering drift too:** a glossary common-noun term rendered
  a different way flags as a "miss." Align the English to the glossary (督察 "inspector").
- **GLOSSARY-KEY DISCIPLINE:** a key must be a DISTINCTIVE proper noun that renders ONE way
  everywhere and must NOT occur elsewhere with a different rendering. Periodicals (新申报,
  申报, 中华日报) and books (沪上往事) are FOOTNOTES/inline, not glossary keys. One-off
  transliterated Western/Japanese officer names are rendered inline (pinyin/romaji), not
  keyed. A bare surname whose full name is unknown is rendered inline.
- **Note-anchor gotchas:** anchors must be ASCII, WITHOUT any quote/apostrophe character
  AND without an em dash (U+2014) - all substring traps. The reading.md uses curly
  quotes/apostrophes and em dashes freely, so pick an anchor phrase with none of them (ch24
  used "Lao Bosheng, chief of the political section", "belonging to the Tama Force",
  "doctrine of the three nots", "a man surnamed Yuan and named Shu"). Multi-occurrence
  anchors attach at the FIRST occurrence.
- **make_ch24_apparatus.py pattern (scripts/):** author note bodies as plain ASCII + typed
  hanzi in a Python file, ASSERT every non-ASCII glyph occurs in data/zh/<id>.txt (a
  Write-tool corruption produces a glyph absent from the source and trips the assert), then
  convert every non-ASCII char to a numeric char ref and run apparatus_merge.py. **The
  CJK-heredoc/Write mangling hazard is REAL** (B16's 功亏一篑 came through corrupted); keep
  hanzi in note bodies to the minimum needed and eyeball it.
- data/noise.txt carries the B01-B18 project noise rules (each with a comment line).
  Republican years render literally; the checker matches the source numeral. **The
  elided-tens block is ordered LONGEST-FIRST.** Name-numeral glyphs are noised (the Wan
  forms 万里浪/万墨林/万先生/万的连襟…, the Japanese names 三浦三郎/三浦/四方谅二/五岛, 邵范九,
  云九). Idiom numerals (四季/九死一生/十万八千/三两万/三教九流/漏洞百出/大千世界/信千拈来 and the
  B01-B17 set) are noised. **The ○ (U+25CB circle-zero) address artifact:** the checker
  cannot read ○ as zero and mis-parses 五○○ as a bare 5 - noise the mis-read glyph-string
  (五○○), carry the real value in the English; 四○七 rooms self-resolve via neighboring
  ordinal dates. Every REAL value is CARRIED and matched (police-establishment tables as
  digits/word-forms so the 、/○-split values match; 五十一万余 -> "510,000-odd"; 一万一千余 ->
  "11,000-odd"; etc.).
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches it; re-run
  per session). setup.sh's ONE failing regression test ("hook stands down on template
  stub") is a KNOWN false alarm; all other regression tests pass.

## Renderings settled / carry-forward

- 军统 / 军统局 -> "the Juntong" (DECIDED). 戴笠 Dai Li (courtesy Yunong; 老板 "the Boss";
  戴先生 "Mr. Dai"; 戴雨农 "Dai Yunong"); 汪精卫 Wang Jingwei (汪逆 "the traitor Wang").
  制裁 "sanction"; 制裁令 "sanction order." 敌伪 "the enemy and the puppets"; 汪伪 "Wang
  puppets"; 沦陷区 "the fallen zone"; 区长 "District Chief"; 督察 "inspector"; 总督察 "Chief
  Inspector." Chiang's titles: 校长 "the Commandant", 委员长 "the Generalissimo", 总裁 "the
  Director-General" (Wang = 副总裁 "Vice-Director-General"). 总理 = "the Party Leader" = Sun
  Yat-sen. 日本宪兵队 "the Japanese gendarmerie"; 七十六号 "No. 76"; 特工总部 "Special
  Operations Headquarters"; 工部局 "Municipal Council"; 公共租界 "International Settlement";
  法租界 "French Concession"; 巡捕房 the Concession police / "police station."
- **PLACE-NAME CONVENTION (the qc gate enforces the glossary's PINYIN for keyed cities):**
  北平 Beiping, 天津 Tianjin, 汉口 Hankou, 四川 Sichuan, 虹口 Hongkou (NOT Peiping/Tientsin/
  Hankow/Szechuen/Hongkew). Non-keyed attested Shanghai ROADS keep their historical forms:
  Newchwang Road (牛庄路), Jessfield Road (极司非而路), Avenue Edward VII (爱多亚路), Avenue du
  Roi Albert (亚尔培路), Gordon Road (戈登路), Bubbling Well Road (静安寺路), Weihaiwei Road
  (威海卫路), North Sichuan Road (北四川路 - 四川 pinyin), Foochow Road, Honan Road, Kiangse
  Road; SMP stations (Louza, Sinza, Wayside, Yangtszepoo, Dixwell/Kashing/Chengtu/Poutoo/
  Yulin Roads) keep their attested names. Concession-street rule (from B16): keep attested
  names, use pinyin for the uncertain rather than invent a French name.
- **Book / part titles (in-text; DECIDED; reuse verbatim):** 英雄无名 = "Nameless Heroes";
  Part One 北国锄奸 = "Rooting Out Traitors in the North"; Part Two = "Disgrace at Hanoi";
  Part Three 百战声威 = "Renown Won in a Hundred Battles." 蓝衣社 = "the Blue Shirt Society"
  (NOTED ch08). 忠义救国军 = "the Loyal and Patriotic Army" (NOTED ch21). 抗日杀奸团/抗团 =
  "Anti-Japanese Traitor-Killing Corps"/"Kang Corps" (NOTED ch02/ch11). 新亚和平促进会 = "New
  Asia Peace Promotion Association" (ch22). Books handled by FOOTNOTE/inline (not glossary):
  蒋总统秘录, 戴雨农先生传, 汪政权的开场与收场, 沪滨三次历险实录, 沪上往事 (Wan Molin's memoir,
  NOTED ch22), the "Zhanggu" magazine; periodicals: 申报 (Shenbao, China's paper of record,
  NOTED ch24), 新申报 / 中华日报 (occupation papers, NOTED ch20), 民族晚报.
- **B15/B16 shelf (ch21/ch22 casts; reuse; all keyed with pinyin):** 郑修元 Zheng Xiuyuan,
  陈第容/陈明楚 Chen Dirong/Chen Mingchu, 黄志远 Huang Zhiyuan, 赵理君 Zhao Lijun, 刘原深 Liu
  Yuanshen, 吉震苍 Ji Zhencang (cover 赵圣 Zhao Sheng), 毕高奎 Bi Gaokui, 孙大成 Sun Dacheng,
  万里浪 Wan Lilang, 张璜 Zhang Huang, 戴藏宜 Dai Cangyi, 杜月笙 Du Yuesheng (NOTED ch17), 朱啸谷
  Zhu Xiaogu, 程海涛 Cheng Haitao, 耿嘉基 Geng Jiaji, 何行健/何天风 He Xingjian/He Tianfeng,
  俞叶封 Yu Yefeng, 万墨林 Wan Molin, 邵飘萍 Shao Piaowei (NOTED journalist-namesake), 陈默 Chen
  Mo, 赵刚义 Zhao Gangyi, 范纪曼 Fan Jiman (alias of Fan Xing), 张啸林/杜/黄金荣 the three Green-
  Gang tycoons (张啸林 NOTED ch04).
- **B18 shelf (ch24; reuse; all keyed with pinyin unless noted inline):** 劳勃生 Lao Bosheng
  (SMP political-section/Special-Branch chief, transliteration uncertain - NOTED); 更新舞台
  Gengxin Stage (place, sanction site); 新艳秋 Xin Yanqiu (dan actress - NOTED); 袁殊 Yuan Shu
  (the "five-faced spy" - NOTED); 吴世宝 Wu Shibao (alias Yunfu), 胡均鹤 Hu Junhe, 傅也文 Fu
  Yewen (No.76 figures); 刘俊卿 Liu Junqing, 蒋福田 Jiang Futian (concession police); 刘绍奎 Liu
  Shaokui, 周伟龙 Zhou Weilong, 陈调元 Chen Diaoyuan, 吴佩孚 Wu Peifu (三不主义 NOTED). Rendered
  INLINE (not keyed): the Japanese gendarmerie officers 大木繁 Oki Shigeru, 三浦三郎 Miura
  Saburo, 纳见敏郎 Nami Toshiro, 木下荣市 Kinoshita Eiichi, 四方谅二 Shikata Ryoji, 山崎直吉
  Yamazaki Naokichi, 大井英夫 Oi Hideo, 长光捷治 Nagamitsu Shoji, 大冢清 Otsuka Kiyoshi, 赤木亲之
  Akagi Chikayuki, 五岛茂 Goto Shigeru; the one-off SMP officers 克莱登 Kelaideng, 葛乐华
  Gelehua, 普莱德 Pulaide, and 云九 Yunjiu, 王振鹄 Wang Zhenhu, 随波 Suibo. NEW ch24 notes:
  the SMP Special Branch / 劳勃生; 更新舞台 / 新艳秋 / Peking opera; 申报 Shenbao; 多摩部队/玉部队
  (poison unit); 三不主义 Wu Peifu; 袁殊 Yuan Shu.

## ⚠ Name trap RESOLVED (do not reopen): 陈邦国 / 郑邦国

The Hanoi action-team member the source spells 郑邦国 in ch13 and 陈邦国 in ch15/ch16/ch17
is ONE man. RESOLVED to **Chen Bangguo (陈邦国)**: glossary key renamed; the built ch13 unit
updated; the discrepancy footnoted at the first ch15 occurrence. Use Chen Bangguo consistently.

## Voice sheet - CHEN GONGSHU (author / narrator)

- REGISTER: educated, formal, essayistic first person; grave and a touch archaic but not
  stilted. Long semicolon-joined clauses; four-character idiom and classical allusion used
  freely and footnoted when they carry weight. Refers to himself as 笔者 "the writer" and
  我 "I." His narrating "shall" is DELIBERATE - do not de-formalize it; check_register flags
  it informationally (B06 33%, B08 29%, B12 43%, B14 0%, B15 33%, B16 36%, B18 25%).
- STANCE: self-justifying yet self-effacing; insists on truthfulness, admits his blunders;
  tender toward dead comrades, bitter and scornful toward the enemy. When quoting hostile/
  puppet or comrades' documents, keep the quoted register DISTINCT from Chen's own dry scorn
  (ch21/ch22/ch24 do this for the memoirs of Zheng Xiuyuan and Wan Molin, Dai's telegrams,
  and the 申报 news report vs Chen's narration).
- Ratio ~4.55-4.78 en/han in narrative; prefaces denser (~5.2-5.3); document-heavy chapters
  run higher (ch21 4.89, ch22 4.70, ch24 5.33 on its many short quoted/table lines). Read
  the note, do not reset.

## Voice sheets - principal & recurring cast

- **DAI LI (戴雨农 / Mr. Dai / 老板 "the Boss").** After ch17 he and Chen meet no more, only
  letters and telegrams; his word is "as a mountain." Warm off duty, abrupt on business. In
  ch24 he makes his one lifetime self-criticism (strong character, poor communication, too
  much done in person) and refuses to let subordinates raise their own funds - so Chen takes
  the arms-donation on his own shoulders.
- **QI QINGBIN (齐庆斌, alt. Ruozhai) & ZHANG ZUOXING (张作兴, alt. Kexin).** Chen's childhood
  friends (Part One ch06); the Shanghai District secretary and radio inspector (ch22). Qi
  carries the "new plan" to Chongqing for the April-First Congress (ch24). The three "jointly
  presided over" the District for six years.
- **ZHENG XIUYUAN (郑修元 / Brother Xiuyuan).** District secretary who held the Shanghai
  District together; his memoir quoted in ch21/ch22. Transferred out (Dec 1939).
- **LIU YUANSHEN (刘原深 / Brother Yuanshen).** The very man who revises "Nameless Heroes" for
  Chen; his living memory-check throughout Part Three. Consult on every Shanghai-cast recall.
- **BI GAOKUI / HUANG ZHIYUAN (毕高奎 / 黄志远).** Leader and deputy of New Group One, the
  purest Shanghai unit; Bi held the First Intelligence Group concurrently (ch24). Both alive
  at the seventy-second year (1983) and consulted for the book.
- **CHEN MO (陈默).** A detachment/cell leader of the Second Action Brigade; led the Yu Yefeng
  sanction (Jan 1940, ch24); "one of the Du household," a source Wan Molin's memoir quotes.
- **Dead comrades carried in memory:** ZENG CHE 曾澈, WANG WEN 王文 (ch11); ZENG ZHONGMING
  曾仲鸣 (ch15/ch16); 陈三才 Chen Sancai (ch21/ch22); 丁文蕙 Ding Wenhui (ch22, the Qingdao martyr).

## Where the book stands

- Part One (北国锄奸) COMPLETE (B01-B05).
- Part Two ("Disgrace at Hanoi") COMPLETE (B06-B13).
- **Part Three ("Renown Won in a Hundred Battles" / 百战声威) is under way (B14-B18).** ch20 =
  self-preface; ch21 = arrival + order of battle; ch22 = the first 1940 sanctions + Fan Xing;
  ch23 = the short "three-sided enemy" framing bridge; ch24 = the full anatomy of the three-
  sided enemy + the Yu Yefeng sanction + Dai's Juntong self-review.
- **NEXT: B19 = ch25** - 第五章 全面检讨奇人奇事 "Chapter 5. A Full Reckoning: Remarkable People,
  Remarkable Deeds," a FULL chapter (~15,600 chars, 1 <h2> + 191 <p> + 2 <br/>). drop=2; the
  2 <br/> are intra-<p> line breaks = 2 MERGE pairs (reconcile ~195 awk-NR txt lines vs 191
  <p>). Opening sub-heading L3 八年抗战初期「军统局」工作检讨 (standalone). Grep p-by-p for further
  standalone/glued/(一)-parens section headings (ch24 had head-glued + tail-glued couplets).
  No images, no note markers.

## What is NEXT

- Batch B19 = ch25 (full chapter). Kickoff is the paste-block at the top. Runs to completion
  (no gate); ends by pasting the B20 kickoff. B20 = ch26 (第六章 泰山鸿毛 同此一掷 "Mount Tai or
  a Feather, All on One Throw"). NOTE: book.json's batches array lumps ch23+ch24 as "B17"; the
  working plan runs ONE AHEAD from ch24 on (ch24 = B18, ch25 = B19). NOTE: ch27 is titled
  第八章 - Part Three skips 第七章, a faithful numbering gap (like Part One skipping ch7).
- The frozen register reference is `reference/B01_frozen.md`. Narrative sits at 4.55-4.78
  en/han; prefaces/document-heavy chapters run higher; a chapter of many short quoted/table
  lines (ch24 = 5.33) runs higher still - alignment/register are the gates, not the raw ratio.
- Sub-heading pattern DIFFERS by chapter. Styles seen: Part One numbered 一/二/三;
  ch11/ch14/ch20-title/ch21/ch22/ch23/ch24-couplet COUPLET-STYLE with NO number prefix;
  ch12/ch13/ch15/ch16/ch17/ch18/ch24-sections numbered-in-parens (一)/(二)…; GLUED sub-heads
  seen ch08/ch16/ch18/ch22 (tail) and ch24 (BOTH tail and HEAD - the new `glued_head`);
  ch13's inner enumerated list rendered `####`. Grep each new chapter p-by-p, and DISTINGUISH
  enumerated LIST items rendered per parity from (一)/(二) SECTION headings (ch24 had both).
- WATCH for source anomalies: cuts, misplaced-「 glitches, corrupt/dropped-character phrases,
  dropped full stops, the in-text "(第N章完，下期续载)" coda/magazine-seam pattern (ch12/ch13/
  ch16/ch21/ch22/ch24), a STRAY glyph fused onto a chapter title (ch22's 杀), a STRAY orphan
  enumerator mid-list (ch24's "(一)"), the ○ (U+25CB) circle-zero in addresses (ch24), and
  pervasive single-character substitutions. Intra-<p> `<br/>` line breaks (new in ch25) are
  MERGE pairs, not paragraph boundaries. Re-grep each batch's source for `\[\d+\]` note
  markers (none through B18).

## Open items for the read-through / completion

- Feed decided renderings back to authority.json on completion: 军统 "the Juntong"; the full
  B02-B18 historical-name set (Part One; the Japanese/negotiator names; the Wang-essay set;
  the Part-Two Hanoi/Chongqing casts; the martyrs; the Shanghai-District staff, order of
  battle, the B16 operative/collaborator cast, and the B18 SMP/gendarmerie/No.76 cast).
- Japanese name readings to verify when the men recur (多田骏, 田代皖一郎, 土肥原贤二, 板垣征四郎,
  近卫文麿, 影佐祯昭, 今井武夫, 晴气庆胤; 大屋久寿雄; 横山秋马; 岩井英一; 大井英夫; and the B18
  gendarmerie officers 大木繁/三浦三郎/纳见敏郎/木下荣市/四方谅二/山崎直吉/长光捷治/大冢清/赤木亲之/
  五岛茂 - rendered inline, romaji to firm up).
- Provisional romanizations to firm up when sources allow (glossary `provisional` rows, incl.
  the Shanghai-District cast, the B16 operatives, and the B18 rows 劳勃生/傅也文/刘俊卿/蒋福田).
- Whole-book reconciliation items: ch09 "Jize County" (para 220, the 鸡泽县 key); the pinyin-
  vs-postal city names (now standardized to pinyin for keyed cities from B18 - re-grep earlier
  chapters for any stray Peiping/Tientsin/Hankow if a reconciliation pass runs). Stray source
  glyph still to resolve: 毛酋 in a ch36 section title.

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01-B18 builds (0/0/0/0). Source is a clean
  digital EPUB, predominantly simplified with residual variant glyphs and pervasive
  digitization glitches (list them, render to plain sense, do not footnote mechanical typos).
  B01-B18 glitch lists are in PROGRESS.md.
- Running-header line 英雄无名-陈恭澍 opens all 43 content files: drop it. drop count is
  variable - most drop=2; ch01/ch10/ch20 drop=3.
- Enumerated ；/：/、 bullet lists, quoted-document/roster lines, salutations, verse lines,
  juxtaposition lines (ch24's 沪上往事/申报 alternation), and 『』-closed dialogue are DELIBERATE
  separate `<p>` - do NOT merge them; only genuine mid-phrase splits (last char not terminal,
  OR a source `<p>` boundary that severs one sentence, OR an intra-<p> `<br/>` as in ch25)
  merge, and those can CHAIN. A line ending on a dash lead-in that is its OWN source `<p>` is
  DELIBERATE, NOT a split. ALWAYS confirm the extracted body count p-by-p against data/src_epub.
- Faithful numbering gaps/anomalies (NOT errors): Part Three skips 第七章 (ch27 = 第八章),
  splits ch10 into (上)/(下); 三面受敌 一往无前 titles two chapters (ch14 and ch24); ch09 printed
  §五 before §四; ch13 restarts its (一)-(五) numbering; ch16 reproduces two whole Wang
  documents; ch21/ch22/ch24 carry magazine "下期续载" seams; ch24 has a source-internal date
  slip (Miura's term 二十年 vs 二十七年). Preserve and, where a reader would stumble, footnote.
- Expect a stray per-task branch at the top of every batch; consolidate onto
  claude/nameless-heroes per rule 2.
