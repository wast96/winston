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
Nameless Heroes B17

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once (its ONE failing regression test, "hook stands down on template stub", is a KNOWN false alarm; all others pass), then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05), B02 (ch06), B03 (ch07), B04 (ch08), B05 (ch09), B06 (ch10 preface + ch11), B07 (ch12), B08 (ch13), B09 (ch14), B10 (ch15), B11 (ch16), B12 (ch17), B13 (ch18 + ch19), B14 (ch20), B15 (ch21) and B16 (ch22) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them. PART TWO ("Disgrace at Hanoi") is COMPLETE; PART THREE ("Renown Won in a Hundred Battles" / 百战声威) is under way (ch20 self-preface + ch21/ch22, the first two Shanghai chapters). The EPUB now holds 22/43 chapters, 225 notes.

Do Batch B17 = ch23 (ONE unit, ~534 source chars, a SHORT framing chapter, the shortest since ch19): ch23 = 第三章 爱国情操 道德规范 "Chapter 3. Patriotic Spirit, Moral Bounds" - a brief bridge that names the Shanghai District's "three-sided enemy" (concession police, the Shanghai Japanese Gendarmerie, and No.76) and previews the two chapters to come, closing on the Yu Yefeng (俞叶封) sanction that ch22 promised to recount. Read the tail of ch22 English (out/ch22_reading.md; ch22 ended with the moral-conscience essay, the Christmas 1939 Weldon Dance Hall sanction of Chen Dirong/He Xingjian, the Wang Tianmu riddle, and the new plan to strike armed Japanese; it names 俞叶封 Yu Yefeng, sanctioned 14 Jan 1940, "recounted in the next chapter") and ch22/ch21 for register + story continuity. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch23 from data/src (24_index-split-000-0022.txt). CONFIRM structure against data/src_epub/OEBPS/Text/index_split_000_0022.xhtml [parses to 1 <h2> + 8 <p>, NO <h1>, NO <br/>, NO <img>]. drop=2 (running header 英雄无名-陈恭澍 + <h2> chapter title). The txt has 10 lines (L1 header + L2 <h2> + 8 body lines L3-L10) vs 8 <p> - CONFIRMED 1:1, no merges (L4-L10 all end on terminal punctuation). L3 初生之犊组成了一枝生力军 is the opening COUPLET sub-heading (NO number prefix, cf. ch11/ch14/ch21/ch22) - place it as a `standalone`. L4-L10 are 7 body paragraphs. GREP the source for note markers (\[\d+\]) and record "none present" (none through B16).
2. Extend scripts/clean_batch.py with ch23's spec (drop=2; merges=[]; glued={}; standalone=[3]). Run it (source-conservation check; expect "ch23: 7 body paragraphs, 1 sub-headings, source conserved OK"). Write out/ch23_reading.md (## from book.json title_en "Chapter 3. Patriotic Spirit, Moral Bounds"; one English paragraph per source body line; the couplet sub-heading L3 as ### ). Then run scripts/batch_artifacts.py ch23, and ALWAYS finish with a NO-ARG run (the batch_artifacts.py trap: an ID-run writes checks.json with ONLY that unit; the no-arg run restores all 23 units so check_structure/check_content see them).
3. Translate to the FROZEN register (Chen's voice sheet in HANDOFF; a short framing essay, narrative band ~4.55-4.78 en/han, may run higher on so few paragraphs - read the note, do not reset). Consult glossary.json and authority.json BEFORE romanizing anything; REUSE the settled Part-Three renderings (all keyed with pinyin): 上海区 "the Shanghai District"; the Juntong; 制裁 "sanction"; 督察 "inspector" (align common-noun terms to the glossary - the qc_entities gate); 敌伪 "the enemy and the puppets"; 汪伪 "Wang puppets"; 忠义救国军 "the Loyal and Patriotic Army"; 特工总部/七十六号 "Special Operations Headquarters"/"No. 76" (丁默邨/李士群, NOTED - do NOT re-note); 新亚和平促进会 "New Asia Peace Promotion Association" (ch22); 俞叶封 Yu Yefeng (keyed B16). Note 日本宪兵队 renders "Japanese gendarmerie" (a recurring term); 上海日本宪兵队 "the Shanghai Japanese Gendarmerie." Render Republican years literally ("抗战八年" = "the eight years of the War of Resistance"; the checker matches the source numeral). WATCH ch23's digitization glitches (list in PROGRESS.md, render to plain sense, footnote only real reading uncertainty): the same classes seen ch15-ch22 (e.g. 百性 for 百姓 in L6, a homophone). Dates/counts: carry real values; NOISE only idiom/approximate forms (八年 "eight years" is REAL - carry it; the data/noise.txt already carries the B01-B16 rules).
4. Checks: verify_unit.py ch23 (parity + numbers with --noise auto-found + anchors); check_align.py ch23; regenerate checks.json with scripts/batch_artifacts.py (no args) and run check_structure.py --config checks.json + check_content.py --config checks.json (NOTE: check_content prints KNOWN PRE-EXISTING artifacts and exits nonzero because of them - ch08 Shunde ×3 and ch13 Miss Nguyen/Oya Kusuo/Yuan Haowen ×9; CONFIRM ch23 itself shows "all in the paired paragraph" / 0 displaced, and align any keyed name/place to its glossary-decided rendering as B16 had to for 杜美路/羊皮巷/连谋). Do NOT add COMMON-NOUN or book/periodical keys. qc_entities.py on a reconstructed bilingual (data/zh body lines + out/ch23_en.json, `> zh` / en pairs, strip the ### heading line; every glossary row needs a pinyin field). Verify the TAIL against the source. check_register.py --ref reference/B01_frozen.md out/ch23_reading.md ("shall" in Chen's narration is deliberate - read the note, do not de-formalize; ch22 ran 36%).
5. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (the full list is in PROGRESS.md). ch23 is a short framing chapter and MOST of its furniture is already covered (No.76/特工总部/丁默邨/李士群, the Japanese gendarmerie, 制裁, the concessions, 忠义救国军, the Republican calendar). Be generous but do NOT pad; a note may be earned by the Japanese-gendarmerie "谈虎色变" terror the chapter foregrounds, if a reader would miss it, but likely 0-2 notes suffice. Merge notes via apparatus_merge.py (numeric character references only in note bodies; anchors verbatim ASCII substrings of the reading.md body text, NO em dash and NO quote/apostrophe character - substring traps). Add any glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field; apparatus_merge's glossary path assumes a FLAT map and would corrupt the sectioned file - use it ONLY for notes). Confirm ch23 carries no images (its XHTML has NO <img> - confirm).
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; update HANDOFF.md; commit and push to claude/nameless-heroes. (next is B18 = ch24, 第四章 三面受敌 一往无前 "Beset on Three Sides, Ever Forward," ~17,105 chars, the fuller chapter that carries the Yu Yefeng sanction detail.)

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B18 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
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
- **Batch B15 (ch21), Part Three Chapter 1.** ch21 = 第一章 十里洋场重振雄威 "Back in Shanghai,
  Our Might Restored." Chen arrives (Aug 1939), takes over the shattered District, rebuilds
  the full order of battle. 8 notes; 19 glossary rows; the 掌故 common-noun key removed.
- **Batch B16 (ch22), Part Three Chapter 2.** ch22 = 第二章 春云乍展风雷初动 "Spring Clouds
  Unfurl, the First Thunder Stirs" - the SECOND Shanghai chapter and the LONGEST unit yet
  (~35,471 chars, 1 <h2> + 292 <p>). The first sanction operations of 1940: Cheng Haitao
  (18 Oct 1939); the DDS Cafe near-kidnapping and Wan Lilang's defection to No.76; the
  Geng Jiaji figure; Qi Qingbin/Zhang Zuoxing installed; the Fan Xing reunion + New Group
  One order of battle; the moral-conscience essay closing on the Weldon Dance Hall sanction
  of Chen Dirong/He Xingjian (Christmas 1939) and the Wang Tianmu riddle. drop=2; **3 merges**
  (L31/32, L221/222, L279/280); **3 standalone sub-headings** (L3/L40/L64) + **2 glued**
  (L108/L202); the **STRAY 杀 title glitch** dropped; the **coda glitch 第三章完** (三-for-二)
  rendered "Chapter Two." **286 body paragraphs; 7 notes (225 cumulative); 29 glossary rows.**
  All checks green; qa_epub PASS; epubcheck 0/0/0/0. **EPUB now 22/43 chapters.** Detail in
  PROGRESS.md ("Batch B16").

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` - derives data/zh/<id>.txt verbatim from data/src,
  applying per-unit drops/merges/heading-splits with a source-conservation check.
  Specs for ch01-ch22. Merge logic FOLLOWS CHAINS. **drop is variable:** most chapters
  drop=2; ch01/ch10/ch20 drop=3. `standalone` = a sub-heading kept as its own <p> with
  no heading markup, emitted as a `### ` line; `glued` = a sub-heading fused onto a
  paragraph's tail, split off; `merges` = source <p> pairs that sever one sentence.
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
  hanzi `title` field (e.g. ch22's stray 杀) never surfaces.
- `scripts/check_content.py` (patched) - name_map skips "_"-prefixed glossary
  categories/entries. It flags KNOWN PRE-EXISTING artifacts and exits NONZERO because
  of them: **ch08 Shunde (3) and ch13 Miss Nguyen/Oya Kusuo/Yuan Haowen (9)** - diacritic/
  variant forms the substring matcher cannot align. These are NOT regressions; the pass
  criterion for a NEW batch is "the batch's own unit shows all name occurrences in the
  paired paragraph / 0 displaced." A NEW unit's displacements are almost always a keyed
  name/place rendered a DIFFERENT way than the glossary (B16 had four: 杜美路 "Route Doumer",
  羊皮巷 "Yangpi Lane", 连谋 "Lian Mou", 鸡泽县 "Jize County"): align the English (or, for a
  clear case-only place mismatch, the glossary) to the keyed form. Do NOT add book-TITLE or
  COMMON-NOUN keys.
- **Verse marker `{p}`** (first used ch13): prefix a pure-verse line with `{p} `; the
  builder renders `<p class="verse">`; the checks strip it.
- Glossary is authored/merged BY HAND into the SECTIONED file
  (book/people/organizations/places/terms), idempotent + re-read-verified. **Every row
  MUST carry a `pinyin` field** - `qc_entities.py` does `rec["pinyin"]` and KeyErrors
  otherwise. apparatus_merge's glossary path assumes a FLAT map and would corrupt the
  sectioned file; NOTES still go through apparatus_merge.py.
- **qc_entities catches term-rendering drift too:** a glossary common-noun term rendered
  a different way flags as a "miss." Align the English to the glossary (督察 "inspector").
- **GLOSSARY-KEY DISCIPLINE (reinforced B15/B16):** a key must be a DISTINCTIVE proper noun
  that renders ONE way everywhere and must NOT occur elsewhere with a different rendering.
  掌故 (magazine vs common noun) violated this and was removed; periodicals (新申报) and books
  (沪上往事) are FOOTNOTES/inline, not glossary keys. A bare surname whose full name is
  unknown is rendered inline, not keyed.
- **Note-anchor gotchas:** anchors must be ASCII, WITHOUT any quote/apostrophe character
  AND without an em dash (U+2014) - all substring traps. The reading.md uses curly
  quotes/apostrophes and em dashes freely, so pick an anchor phrase with none of them (e.g.
  ch22 used "the Xiongnu not yet destroyed", "GPU training", "one basketful", "Badlands" -
  a bare word inside "curly quotes" works, "the GPU" did not because of the quote). Multi-
  occurrence anchors attach at the FIRST occurrence; check_structure reports "attach at
  first of several."
- **make_ch22_apparatus.py pattern (scratchpad):** author note bodies as plain unicode in a
  Python file (Write tool), convert every non-ASCII char to a numeric char ref
  programmatically, then write data/<id>_apparatus.json and run apparatus_merge.py. **The
  CJK-heredoc mangling hazard is REAL:** in B16 the idiom 为山九仞，功亏一篑 came through the
  Write tool corrupted (功亏一簓 / 为山九他); caught by grepping the CJK out of the script and
  verifying each glyph before converting. Keep hanzi in note bodies to the minimum needed and
  eyeball it.
- data/noise.txt carries the B01-B16 project noise rules (each with a comment line).
  Republican years render literally; the checker matches the source numeral. **The
  elided-tens block is ordered LONGEST-FIRST.** **Name-numeral glyphs** (万 in a name) are
  noised: the B15 Wan-Lilang forms (万里浪/万某/万即/万兄/万里) plus the B16 additions (万有何/
  万队/万答/万逆/万与 bare-surname Wan; 万墨林/万先失 Wan Molin; 万想不到/万千 idioms). Idiom
  numerals (外八字/合十/不三不四/两个钱/八旬) and the coda glitch (第三章完) are noised too;
  every REAL value is CARRIED in the English and matched (二人/三人 -> "the two"/"both"/"the
  three"; 五点四十分 -> "five-forty"; 两百/一百 -> "two hundred"/"one hundred"; etc.).
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches it; re-run
  per session). setup.sh's ONE failing regression test ("hook stands down on template
  stub") is a KNOWN false alarm; all other regression tests pass.

## Renderings settled / carry-forward

- 军统 / 军统局 -> "the Juntong" (DECIDED). 戴笠 Dai Li (courtesy Yunong; 老板 "the Boss";
  戴先生 "Mr. Dai"; 戴雨农 "Dai Yunong"); 汪精卫 Wang Jingwei (汪逆 "the traitor Wang").
  制裁 "sanction"; 制裁令 "sanction order." 敌伪 "the enemy and the puppets" / "enemy-and-
  puppet"; 汪伪 "Wang puppets"; 沦陷区 "the fallen zone"; 日寇 "Japanese invaders"; 区长
  "District Chief"; 督察 "inspector"; 总督察 "Chief Inspector." Chiang's titles: 校长 "the
  Commandant", 委员长 "the Generalissimo", 总裁 "the Director-General" (Wang = 副总裁
  "Vice-Director-General"). 总理 = "the Party Leader" = Sun Yat-sen. Floors: 二楼/三楼 =
  "second/third floor." Republican years literal. 上海滩 "the Shanghai Bund." 高朗街 "Gao
  Lang Street." 日本宪兵队 "the Japanese gendarmerie"; 七十六号 "No. 76."
- **Book / part titles (in-text renderings, DECIDED; reuse verbatim):** 英雄无名 =
  "Nameless Heroes"; Part One 北国锄奸 = "Rooting Out Traitors in the North"; Part Two =
  "Disgrace at Hanoi" (Chen's in-text 河内汪案始末 = "The Whole Story of the Wang Case at
  Hanoi"); Part Three 百战声威 = "Renown Won in a Hundred Battles"; 军事委员会调查统计局 =
  "Bureau of Investigation and Statistics of the Military Affairs Commission." 蓝衣社 =
  "the Blue Shirt Society" (NOTED ch08). 忠义救国军 = "the Loyal and Patriotic Army"
  (NOTED ch21). 特工总部/七十六号 = "Special Operations Headquarters"/"No. 76" (NOTED
  ch04/ch17). 抗日杀奸团/抗团 = "Anti-Japanese Traitor-Killing Corps"/"Kang Corps"
  (NOTED ch02/ch11). 新亚和平促进会 = "New Asia Peace Promotion Association" (ch22). Books
  handled by FOOTNOTE/inline (not glossary): 蒋总统秘录, 戴雨农先生传, 汪政权的开场与收场,
  沪滨三次历险实录 (Zheng Xiuyuan's memoir), 沪上往事 (Wan Molin's memoir, NOTED ch22), and
  the "Zhanggu" (掌故) magazine; periodicals: 新申报, 中华日报.
- **B15 shelf (ch21; reuse; all keyed):** the whole Shanghai District cast - 郑修元 Zheng
  Xiuyuan, 陈第容/陈明楚 Chen Dirong/Chen Mingchu, 黄志远 Huang Zhiyuan, 赵理君 Zhao Lijun
  (cover 凌秋云), 刘原深 Liu Yuanshen, 蒋安华 Jiang Anhua, 吉震苍 Ji Zhencang (cover 赵圣),
  毕高奎 Bi Gaokui, 孙大成 Sun Dacheng, 万里浪 Wan Lilang, 刘时雍 Liu Shiyong, 萧杰英/萧张权
  the Xiao siblings, 张璜 Zhang Huang, 潘绍岳 Pan Shaoyue, 翁光辉/吴乃宪 the first two chiefs,
  戴藏宜 Dai Cangyi, 杜月笙 Du Yuesheng (NOTED ch17), 朱啸谷 Zhu Xiaogu, the five intel groups
  and eight action brigades.
- **B16 shelf (ch22; reuse; all keyed with pinyin):** 程海涛 Cheng Haitao, 耿嘉基 Geng Jiaji
  ("Secretary Geng"), 王一新 Wang Yixin, 马河图/岳清江/丁寳龄 Ma Hetu/Yue Qingjiang/Ding
  Baoling (Wang Tianmu's three bodyguards), 何行健/何天风 He Xingjian/He Tianfeng, 汪秋芳/汪芳
  Wang Qiufang/Wang Fang, 田淑君 Tian Shujun, 傅胜蓝/丁文蕙 Fu Shenglan/Ding Wenhui (the
  Qingdao tragedy), 俞叶封 Yu Yefeng, 虞洽卿 Yu Qiaqing, 贺耀组 He Yaozu (figurehead director),
  褚民谊 Chu Minyi, 万墨林 Wan Molin, 傅炳宸 Fu Bingchen, 傅式说 Fu Shishuo (source misprints
  傅 as 传), 邵飘萍 Shao Piaowei (action man; NOTED as journalist-namesake), 张圣才 Zhang
  Shengcai, 陈默 Chen Mo, 赵刚义 Zhao Gangyi, 钱人龙 Qian Renlong, 伊凡诺夫 Ivanov, 顾兰君 Gu
  Lanjun, 杨虎 Yang Hu, 范纪曼 Fan Jiman (alias of Fan Xing). NEW ch22 notes: 条子/gold bars,
  GPU, 邵飘萍 the journalist, 匈奴未灭, 为山九仞, 万墨林/沪上往事, the Badlands (歹土). Concession
  streets: keep the attested names (Avenue Joffre/Foch/Haig, Bubbling Well/Jessfield/Seymour/
  Sinza/Yates/Moulmein Roads, Route Doumer/Ratard) and use pinyin for the uncertain (Beile/
  Kangti/Shanzhong/Geluoxi Roads) rather than invent a French name.

## ⚠ Name trap RESOLVED (do not reopen): 陈邦国 / 郑邦国

The Hanoi action-team member the source spells 郑邦国 in ch13 and 陈邦国 in ch15/ch16/ch17
is ONE man. RESOLVED to **Chen Bangguo (陈邦国)**: glossary key renamed; the built ch13 unit
updated; the discrepancy footnoted at the first ch15 occurrence. Romanization stays
`provisional`. Use Chen Bangguo consistently.

## Voice sheet - CHEN GONGSHU (author / narrator)

- REGISTER: educated, formal, essayistic first person; grave and a touch archaic but not
  stilted. Long semicolon-joined clauses; four-character idiom and classical allusion used
  freely and footnoted when they carry weight. Refers to himself as 笔者 "the writer" and
  我 "I." His narrating "shall" is DELIBERATE - do not de-formalize it; check_register flags
  it informationally (B06 33%, B08 29%, B12 43%, B14 0% (a no-dialogue preface), B15 33%,
  B16 36%).
- STANCE: self-justifying yet self-effacing; insists on truthfulness, admits his blunders;
  tender toward dead comrades, bitter and scornful toward the enemy. When quoting hostile/
  puppet or comrades' documents, keep the quoted register DISTINCT from Chen's own dry
  scorn (ch21/ch22 do this for Zheng Xiuyuan's memoir, Bi Gaokui's account, Dai's telegrams,
  and Wan Molin's memoir).
- Ratio ~4.55-4.78 en/han in narrative; prefaces denser (~5.2-5.3); document-heavy chapters
  run higher (ch21 measured 4.89; ch22 measured 4.70). Read the note, do not reset.

## Voice sheets - principal & recurring cast

- **DAI LI (戴雨农 / Mr. Dai / 老板 "the Boss").** After ch17 he and Chen meet no more, only
  letters and telegrams; his word is "as a mountain." Warm off duty, abrupt on business;
  gives orders with little reason. In ch22 he scolds Chen "timid as a mouse," then refuses
  (with the 为山九仞 allusion) Chen's offer of an outsider's bank money.
- **MAO WANLI (毛万里 / Brother Wanli).** Chief Inspector in Shanghai, tasked with the plan
  to sanction Wang Jingwei; an old, deep private friend of Chen's. Named coyly as bare 万里
  / 万兄 (noised).
- **ZHENG XIUYUAN (郑修元 / Brother Xiuyuan).** District secretary who held the Shanghai
  District together single-handed; his memoir is quoted at length in ch21/ch22. Transferred
  out (Dec 1939) after the ch22 DDS-Cafe near-kidnapping.
- **QI QINGBIN (齐庆斌, alt. name Ruozhai) & ZHANG ZUOXING (张作兴, alt. name Kexin).**
  Chen's childhood friends (Part One ch06); installed in ch22 as Shanghai District secretary
  and radio inspector. Qi is upright and scrupulous; Zhang quick, straight, pockmarked (a
  liability for field work). The three "jointly presided over" the District for six years.
- **WANG TIANMU (王天木).** Former Shanghai/Tianjin District chief; loyalty in doubt. In ch22,
  his three bodyguards (Ma Hetu, Yue Qingjiang, Ding Baoling) carry out the Christmas 1939
  sanction of Chen Dirong/He Xingjian; Wang himself does NOT flee - a riddle Chen never solves;
  No.76 then holds him for years.
- **LIU YUANSHEN (刘原深 / Brother Yuanshen).** The very man who revises "Nameless Heroes" for
  Chen; Chen's living memory-check throughout Part Three. Consult on every Shanghai-cast recall.
- **FAN XING / FAN JIMAN (范行 / 范纪曼).** The "great international spy," recruited by the
  Beiping Station (Part One); reappears in ch22 in Shanghai, and Chen reopens the "intelligence
  war," reporting his takes under a false name. His teeth-marked girlfriend Peng Yaluo and a
  Latvian at the "Deer-Horn Trading Company" thicken the mystery. A fresh discovery "in the
  middle of the 29th year" is promised.
- **BI GAOKUI / HUANG ZHIYUAN (毕高奎 / 黄志远).** Leader and deputy of New Group One, the
  purest and most effective Shanghai unit; Bi France-trained, met Dai in a midnight audience.
  Both alive at the seventy-second year (1983) and consulted for the book.
- **Dead comrades carried in memory:** ZENG CHE 曾澈, WANG WEN 王文 (ch11); ZENG ZHONGMING
  曾仲鸣 (ch15/ch16); 陈三才 Chen Sancai (ch21/ch22, avenged Sept 1941 via New Group One's
  killing of the traitor Ivanov); the Qingdao martyr 丁文蕙 Ding Wenhui (ch22).

## Where the book stands

- Part One (北国锄奸) COMPLETE (B01-B05).
- Part Two ("Disgrace at Hanoi") COMPLETE (B06-B13).
- **Part Three ("Renown Won in a Hundred Battles" / 百战声威) is under way (B14-B16).** ch20 =
  self-preface; ch21 = arrival + order of battle; ch22 = the first 1940 sanction operations,
  the Fan Xing reunion, and the moral-conscience essay. ch22 ends naming 俞叶封 Yu Yefeng
  (sanctioned 14 Jan 1940) as "recounted in the next chapter."
- **NEXT: B17 = ch23** - 第三章 爱国情操 道德规范 "Chapter 3. Patriotic Spirit, Moral Bounds,"
  a SHORT framing chapter (~534 chars, 1 <h2> + 8 <p>). drop=2; ONE standalone couplet
  sub-heading (L3 初生之犊组成了一枝生力军); no merges, no glued, no images, no note markers.
  It names the "three-sided enemy" (concession police, the Shanghai Japanese Gendarmerie,
  No.76) and previews ch24.

## What is NEXT

- Batch B17 = ch23 (short framing chapter). Kickoff is the paste-block at the top. Runs to
  completion (no gate); ends by pasting the B18 kickoff. B18 = ch24 (三面受敌 一往无前,
  ~17,105 chars, the fuller chapter with the Yu Yefeng sanction detail).
- The frozen register reference is `reference/B01_frozen.md`. Narrative sits at 4.55-4.78
  en/han; prefaces/document-heavy chapters run higher; a very short unit can run higher on
  few paragraphs.
- Sub-heading pattern DIFFERS by chapter. Styles seen: Part One numbered 一/二/三;
  ch11/ch14/ch20-title/ch21/ch22/ch23 COUPLET-STYLE with NO number prefix; ch12/ch13/ch15/
  ch16/ch17/ch18 numbered-in-parens (一)/(二)…; ch08/ch16/ch18/ch22 have GLUED sub-heading(s);
  ch13's inner enumerated list rendered `####`. Grep each new chapter p-by-p.
- WATCH for source anomalies: cuts, misplaced-「 glitches, corrupt/dropped-character
  phrases, dropped full stops, the in-text "(第N章完)" coda pattern (ch12/ch13/ch16/ch21/ch22;
  ch21 and ch22 carry "下期续载" magazine seams; ch22's coda 第三章完 is a 三-for-二 glitch),
  a STRAY glyph fused onto a chapter title (ch22's 杀), and pervasive single-character
  substitutions. Re-grep each batch's source for `\[\d+\]` note markers (none through B16).

## Open items for the read-through / completion

- Feed decided renderings back to authority.json on completion: 军统 "the Juntong"; the full
  B02-B16 historical-name set (Part One; the Japanese/negotiator names; the Wang-essay set;
  the Part-Two Hanoi/Chongqing casts; the martyrs; the Shanghai-District staff, order of
  battle, and the B16 operative/collaborator cast).
- Japanese name readings to verify when the men recur (多田骏, 田代皖一郎, 土肥原贤二,
  板垣征四郎, 近卫文麿, 影佐祯昭, 今井武夫, 晴气庆胤; 大屋久寿雄; 横山秋马; 岩井英一 of the
  Kōain; 大井英夫 "Ōi Hideo" of the Shanghai gendarmerie, new in ch22).
- Provisional romanizations to firm up when sources allow (glossary `provisional` rows,
  incl. the whole Shanghai-District cast and the B16 operatives).
- Stray source glyphs still to resolve: 毛酋 in a ch36 section title (ch22's 杀 title and
  第三章完 coda are handled in B16).

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01-B16 builds (0/0/0/0). Source is a clean
  digital EPUB, predominantly simplified with residual variant glyphs and pervasive
  digitization glitches (list them, render to plain sense, do not footnote mechanical
  typos). B01-B16 glitch lists are in PROGRESS.md.
- Running-header line 英雄无名-陈恭澍 opens all 43 content files: drop it. drop count is
  variable - most drop=2; ch01/ch10/ch20 drop=3.
- Enumerated ；/：/、 bullet lists, quoted-document/roster lines, salutations, verse lines,
  and 『』-closed dialogue in the source are DELIBERATE separate `<p>` - do NOT merge them;
  only genuine mid-phrase splits (last char not terminal, OR a source `<p>` boundary that
  severs one sentence) merge, and those can CHAIN across 3+ fragments. A line ending on a
  dash lead-in that is its OWN source `<p>` is DELIBERATE, NOT a split (cf. ch20 L12, ch21
  L51/L66, ch22 L7/L46/L183). ALWAYS confirm the extracted body count p-by-p against
  data/src_epub.
- Faithful numbering gaps/anomalies (NOT errors): Part Three skips ch7, splits ch10 into
  (上)/(下); 三面受敌 一往无前 titles two chapters (ch14 and ch24); ch09 printed §五 before
  §四; ch13 restarts its (一)-(五) numbering; ch16 reproduces two whole Wang documents; ch21
  and ch22 carry magazine "下期续载" seams. Preserve and, where a reader would stumble, footnote.
- Expect a stray per-task branch at the top of every batch; consolidate onto
  claude/nameless-heroes per rule 2.
