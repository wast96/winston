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
Nameless Heroes B16

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once (its ONE failing regression test, "hook stands down on template stub", is a KNOWN false alarm; all others pass), then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05), B02 (ch06), B03 (ch07), B04 (ch08), B05 (ch09), B06 (ch10 preface + ch11), B07 (ch12), B08 (ch13), B09 (ch14), B10 (ch15), B11 (ch16), B12 (ch17), B13 (ch18 + ch19), B14 (ch20) and B15 (ch21) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them. PART TWO ("Disgrace at Hanoi") is COMPLETE; PART THREE ("Renown Won in a Hundred Battles" / 百战声威) is under way (ch20 self-preface + ch21, the first Shanghai chapter). The EPUB now holds 21/43 chapters, 218 notes.

Do Batch B16 = ch22 (ONE unit, ~35,471 source chars - the SECOND Shanghai chapter and the LONGEST unit yet, half again as long as ch21): ch22 = 第二章 春云乍展风雷初动 "Chapter 2. Spring Clouds Unfurl, the First Thunder Stirs" - the Shanghai District's first sanction operations of 1940 get under way. Read the tail of ch21 English (out/ch21_reading.md ends by previewing exactly this: at P152-P154 the reorganized District completes "its first action case of a deterrent effect" by mid-October, the Fourth-Brigade deputy Wan Lilang defects to No.76, and the "mysterious international-spy figure" reappears to open a new "intelligence war"; P293-P294 of the ch22 source already name 蒋安华 Jiang Anhua and 毕高奎 Bi Gaokui trading views on a plan submitted "early in the twenty-ninth year") and ch21/ch18 for register + story continuity. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch22 from data/src (23_index-split-000-0021.txt). CONFIRM structure against data/src_epub/OEBPS/Text/index_split_000_0021.xhtml [parses to 1 <h2> + 292 <p>, NO <h1>, NO <br/>, NO <img>]. drop=2 (running header 英雄无名-陈恭澍 + <h2> chapter title). The txt has 294 lines (L1 header + L2 <h2> + 292 body lines) vs 292 <p> - a FIRST PASS suggests 1:1, so GREP p-by-p and DERIVE any merges (last char not in 。！？」』）…—; a source <p> boundary that severs one sentence merges, and can CHAIN), the glued {} and the standalone []. WATCH the SUB-HEADING style: L3 一警百清除障碍以展示威力 looks like the opening COUPLET sub-heading (NO number prefix, cf. ch11/ch14/ch21); a first pass found NO (一)-style numbered parens - confirm p-by-p and place every couplet sub-heading as a `standalone`. Treat 』-closed dialogue, ：/-ended lead-ins, 一、/1- enumerated items, and roster lines as DELIBERATE separate <p> (do NOT merge; cf. ch21). GREP the source for note markers (\[\d+\]) and record "none present" (none through B15).
   STRAY-杀 TITLE GLITCH (flagged since the survey): the source <h2> reads 第二章 春云乍展风雷初动杀 - the trailing 杀 is EXTRANEOUS (a digitization glitch fused onto the couplet title, which is properly 春云乍展／风雷初动). book.json title_en is already clean ("Chapter 2. Spring Clouds Unfurl, the First Thunder Stirs"); the reading.md ## uses title_en. In clean_batch.py ch22's `title` field is dropped (drop=2) and stripped by the checks, so it is apparatus only - use the clean couplet (drop the 杀) there and LIST the 杀 glitch in PROGRESS.md (a mechanical title typo, rendered to plain sense, not footnoted). Confirm the last body line (L294 …预计一周左右即可获得) is the true chapter end or a mid-sentence source cut, and preserve faithfully.
2. Extend scripts/clean_batch.py with ch22's spec (drop=2; merges/glued/standalone as derived). Run it (source-conservation check). Write out/ch22_reading.md (## from book.json title_en; one English paragraph per source body line; couplet sub-headings as ### ; any inner enumerated list #### per ch13 precedent). Then run scripts/batch_artifacts.py ch22, and ALWAYS finish with a NO-ARG run (the batch_artifacts.py trap: an ID-run writes checks.json with ONLY that unit; the no-arg run restores all 22 units so check_structure/check_content see them).
3. Translate to the FROZEN register (Chen's voice sheet in HANDOFF; narrative ~4.55-4.78 en/han, but a document-heavy chapter runs higher - ch21 measured 4.89 with its long quoted memoirs; read the note, do not reset). Consult glossary.json and authority.json BEFORE romanizing anything; REUSE the settled Part-Three renderings (all now keyed with pinyin): 上海区 "the Shanghai District"; 区长 "District Chief"; the Juntong; 制裁 "sanction"; 督察 "inspector" (align common-noun terms to the glossary - the qc_entities gate); 敌伪 "the enemy and the puppets"; 汪伪 "Wang puppets"; 忠义救国军 "the Loyal and Patriotic Army"; 特工总部/七十六号 "Special Operations Headquarters"/"No. 76" (丁默邨/李士群, NOTED - do NOT re-note); 抗日杀奸团/抗团 "Anti-Japanese Traitor-Killing Corps"/"Kang Corps" (NOTED ch02/ch11). Shanghai CAST now keyed (B15): 郑修元 Zheng Xiuyuan, 陈第容/陈明楚 Chen Dirong/Chen Mingchu, 黄志远 Huang Zhiyuan, 赵理君 Zhao Lijun (cover 凌秋云 "Ling Qiuyun"), 毛万里 Mao Wanli, 刘原深 Liu Yuanshen, 蒋安华 Jiang Anhua, 吉震苍 Ji Zhencang, 毕高奎 Bi Gaokui, 孙大成 Sun Dacheng, 万里浪 Wan Lilang, 萧杰英/萧张权 the Xiao siblings, 张璜 Zhang Huang, 潘绍岳 Pan Shaoyue, 杜月笙 Du Yuesheng (NOTED ch17), the eight action brigades and five intelligence groups. Give pinyin fields for EVERY new name and check authority.json/glossary first. Render Republican years literally ("the twenty-ninth year"; the checker matches the source numeral).
   WATCH ch22's digitization glitches (list in PROGRESS.md, render to plain sense, footnote only real reading uncertainty): the same single-character-substitution / homophone / dropped-punctuation classes seen ch15-ch21 (先↔光, 卫→术, 汪→江, 文↔交, 员→负, 板→扳, 从→徙, 该→孩, 困→因, 科→料, 综→踪, 局→昂, 为→伪, 买→真, 处→书, 问→间, 捉→提, 僧→憎, 隐→稳, 接二连二 for 接二连三, dropped 。, etc.) plus the STRAY 杀 title glitch above. Dates/counts: carry real values as DIGITS / explicit words; NOISE only elided-tens / approximate / name-embedded / idiom forms - add a commented B16 block to data/noise.txt if needed (the elided-tens block is ordered LONGEST-FIRST; keep any new compound BEFORE the bare form it contains; a project noise entry can be PRE-EMPTED by an earlier substring rule; name-numeral glyphs like 万-in-a-name and bare 万里/万兄 must come AFTER the longer forms).
4. Checks: verify_unit.py ch22 (parity + numbers with --noise auto-found + anchors); check_align.py ch22; regenerate checks.json with scripts/batch_artifacts.py (no args) and run check_structure.py --config checks.json + check_content.py --config checks.json (NOTE: check_content prints KNOWN PRE-EXISTING artifacts and exits nonzero because of them - now just ch08 Shunde ×3 and ch13 Miss Nguyen/Oya Kusuo/Yuan Haowen ×9 (ch07 Zhanggu is GONE, resolved in B15 by removing the 掌故 common-noun key); CONFIRM ch22 itself shows "all in the paired paragraph" / 0 displaced. Do NOT add book-TITLE glossary rows keyed on full hanzi, and do NOT add COMMON-NOUN keys - a glossary key must be a distinctive proper noun that renders ONE way everywhere, and must not occur in another chapter with a different rendering; periodicals/books go to FOOTNOTES, not the glossary). qc_entities.py on a reconstructed bilingual (data/zh body lines + out/ch22_en.json, `> zh` / en pairs, strip the ### heading lines; every glossary row needs a pinyin field - and align any common-noun term to its glossary-decided rendering, e.g. 督察 "inspector"). Verify the TAIL against the source (rule 4 corollary - CRITICAL on a 35k-char single-pass unit, the longest yet). check_register.py --ref reference/B01_frozen.md out/ch22_reading.md ("shall" in Chen's narration is deliberate - read the note, do not de-formalize; ch21 ran 33%).
5. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (the full list is in PROGRESS.md). A Shanghai sanction-operation chapter earns notes for NEW places / institutions / persons / methods / customs the reader would miss; the concessions, Du Yuesheng/Green Gang, the Juntong, 制裁, 忠义救国军, No.76, the Kang Corps, 越界筑路, 法币, the Republican calendar are all covered - do NOT re-note. Be generous but do NOT pad. Merge notes via apparatus_merge.py (numeric character references only in note bodies; anchors verbatim ASCII substrings of the reading.md body text, NO em dash and NO quote/apostrophe character - substring traps; multi-occurrence anchors attach at first occurrence). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field; apparatus_merge's glossary path assumes a FLAT map and would corrupt the sectioned file - use it ONLY for notes). Confirm whether ch22 carries images (ch21 had none; ch22's XHTML has NO <img> - confirm).
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; update HANDOFF.md; commit and push to claude/nameless-heroes. (next is B17 = ch23, the third Shanghai chapter.)

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B17 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
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
- **Batch B15 (ch21), Part Three Chapter 1.** ch21 = 第一章 十里洋场重振雄威 "Chapter 1.
  Back in Shanghai, Our Might Restored" - the FIRST Shanghai chapter (~21,426 chars, 1 <h2>
  + 162 <p>). Chen arrives in fallen Shanghai (Aug 1939), is appointed District Chief (takes
  over 12 Aug 1939), and rebuilds the shattered District: the 14-office search after Chen
  Dirong's betrayal, Zheng Xiuyuan holding it single-handed (three excerpts from his memoir
  "沪滨三次历险实录"), the duplex command center, and a full order-of-battle roll (inner
  staff, five intelligence groups, eight action brigades, New Group One, the Kang Corps).
  drop=2; **3 mid-phrase merges** (L56/57, L93/94, L107/108); **4 couplet sub-headings**
  (standalone L3/L37/L82/L112); the **serialization coda "(第一章完下期续载)"** glued at P147
  with 7 trailing paragraphs, preserved. **155 body paragraphs; 8 notes (218 cumulative);
  19 glossary rows added, the 掌故 common-noun key removed (this also RESOLVED ch07's
  Zhanggu artifact).** 赵君 RESOLVED to 赵理君 Zhao Lijun. All checks green; qa_epub PASS;
  epubcheck 0/0/0/0. **EPUB now 21/43 chapters.** Detail in PROGRESS.md ("Batch B15").

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` - derives data/zh/<id>.txt verbatim from data/src,
  applying per-unit drops/merges/heading-splits with a source-conservation check.
  Specs for ch01-ch21. Merge logic FOLLOWS CHAINS. **drop is variable:** most chapters
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
  the reading.md/en.json + notes.json + glossary.json + figures.json.
- `scripts/check_content.py` (patched) - name_map skips "_"-prefixed glossary
  categories/entries. It flags KNOWN PRE-EXISTING artifacts and exits NONZERO because
  of them: **now just ch08 Shunde (3) and ch13 Miss Nguyen/Oya Kusuo/Yuan Haowen (9)**
  - diacritic/variant forms the substring matcher cannot align. **ch07 Zhanggu (1) is
  GONE** (B15 removed the 掌故 common-noun-colliding key). These are NOT regressions; the
  pass criterion for a NEW batch is "the batch's own unit shows all name occurrences in
  the paired paragraph / 0 displaced." Do NOT add book-TITLE or COMMON-NOUN keys.
- **Verse marker `{p}`** (first used ch13): prefix a pure-verse line with `{p} `; the
  builder renders `<p class="verse">`; the checks strip it.
- Glossary is authored/merged BY HAND into the SECTIONED file
  (book/people/organizations/places/terms), idempotent + re-read-verified. **Every row
  MUST carry a `pinyin` field** - `qc_entities.py` does `rec["pinyin"]` and KeyErrors
  otherwise. apparatus_merge's glossary path assumes a FLAT map and would corrupt the
  sectioned file; NOTES still go through apparatus_merge.py.
- **qc_entities catches term-rendering drift too:** a glossary common-noun term rendered
  a different way flags as a "miss." Align the English to the glossary (督察 "inspector").
- **GLOSSARY-KEY DISCIPLINE (reinforced B15):** a key must be a DISTINCTIVE proper noun
  that renders ONE way everywhere and must NOT occur elsewhere with a different rendering.
  掌故 (magazine "Zhanggu" in ch12, common noun "old lore" in ch07/ch21) violated this and
  was removed; periodicals/books are FOOTNOTES, not glossary keys. A bare surname whose
  full name is unknown is rendered inline, not keyed.
- **Note-anchor gotchas:** anchors must be ASCII, WITHOUT any quote/apostrophe character
  AND without an em dash (U+2014) - all substring traps. The reading.md uses straight
  quotes/apostrophes and em dashes freely. Multi-occurrence anchors attach at the FIRST
  occurrence; check_structure reports "attach at first of several."
- data/noise.txt carries the B01-B15 project noise rules (each with a comment line).
  Republican years render literally; the checker matches the source numeral. **The
  elided-tens block is ordered LONGEST-FIRST** (四、五百 before 四、五; B15 slotted 三、五十
  into it). **Name-numeral glyphs** (万 in a name) are noised: 毛万里, 万里兄, 万里浪, 万某,
  万即, and bare 万里 / 万兄 must come AFTER the longer forms so those strip first. Event
  date-names (九一八, 一二八, 七一四) and idioms (百利而无一损, 万般, 四出, 凋零, 接二连二)
  are noised; every REAL value is carried in the English and matched.
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
  Lang Street."
- **Book / part titles (in-text renderings, DECIDED; reuse verbatim):** 英雄无名 =
  "Nameless Heroes"; Part One 北国锄奸 = "Rooting Out Traitors in the North"; Part Two =
  "Disgrace at Hanoi" (Chen's in-text 河内汪案始末 = "The Whole Story of the Wang Case at
  Hanoi"); Part Three 百战声威 = "Renown Won in a Hundred Battles"; 军事委员会调查统计局 =
  "Bureau of Investigation and Statistics of the Military Affairs Commission." 蓝衣社 =
  "the Blue Shirt Society" (NOTED ch08). 忠义救国军 = "the Loyal and Patriotic Army"
  (NOTED ch21). 特工总部/七十六号 = "Special Operations Headquarters"/"No. 76" (NOTED
  ch04/ch17). 抗日杀奸团/抗团 = "Anti-Japanese Traitor-Killing Corps"/"Kang Corps"
  (NOTED ch02/ch11). Books handled by FOOTNOTE (not glossary): 蒋总统秘录, 戴雨农先生传,
  汪政权的开场与收场, 沪滨三次历险实录 (Zheng Xiuyuan's Shanghai memoir), and the "Zhanggu"
  (掌故) Hong Kong magazine (inline-glossed in ch12; its glossary key was REMOVED in B15).
- **B15 shelf (ch21; reuse; all keyed with pinyin):** the whole Shanghai District cast -
  郑修元 Zheng Xiuyuan, 陈第容/陈明楚 Chen Dirong/Chen Mingchu, 黄志远 Huang Zhiyuan, 赵理君
  Zhao Lijun (cover 凌秋云 "Ling Qiuyun"), 刘原深 Liu Yuanshen, 蒋安华 Jiang Anhua (3rd
  Brigade), 吉震苍 Ji Zhencang (2nd Brigade, cover 赵圣), 毕高奎 Bi Gaokui (New Group One),
  孙大成 Sun Dacheng (Kang Corps, a cover name), 万里浪 Wan Lilang (4th-Brigade traitor ->
  No.76), 刘时雍 Liu Shiyong, 萧杰英 Xiao Jieying / 萧张权 Xiao Zhangquan (the Xiao siblings),
  张璜 Zhang Huang, 杨震裔 Yang Zhenyi, 王世英 Wang Shiying, 潘绍岳 Pan Shaoyue, 翁光辉 Weng
  Guanghui + 吴乃宪 Wu Naixian (the first two Shanghai District chiefs), 戴藏宜 Dai Cangyi
  (Dai Li's son), 杜月笙 Du Yuesheng (NOTED ch17). NEW notes: 忠义救国军, 秦晋之说, 越界筑路,
  亭子间, 白相人, 法币, 唐生智, 邓演达/两广事件.

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
  it informationally (B06 33%, B08 29%, B12 43%, B14 0% (a no-dialogue preface), B15 33%).
- STANCE: self-justifying yet self-effacing; insists on truthfulness, admits his blunders;
  tender toward dead comrades, bitter and scornful toward the enemy. When quoting hostile/
  puppet or comrades' documents, keep the quoted register DISTINCT from Chen's own dry
  scorn (ch21 does this for Zheng Xiuyuan's memoir and Liu Shaokui's embedded memoir).
- Ratio ~4.55-4.78 en/han in narrative; prefaces denser (~5.2-5.3); document-heavy chapters
  run higher (ch21 measured 4.89 with its long quoted memoirs). Read the note, do not reset.

## Voice sheets - principal & recurring cast

- **DAI LI (戴雨农 / Mr. Dai / 老板 "the Boss").** After ch17 he and Chen meet no more, only
  letters and telegrams; his word is "as a mountain" (ch21). Warm off duty, abrupt on
  business; gives orders with little reason.
- **MAO WANLI (毛万里 / Brother Wanli).** Chief Inspector in Shanghai, tasked with the plan
  to sanction Wang Jingwei; sanguine, "a lucky star." An old, deep private friend of Chen's.
  Later director of the Southeast Office (Shangrao/Yanshan, Jiangxi). Named coyly as bare 万里
  / 万兄 too (noised).
- **ZHENG XIUYUAN (郑修元 / Brother Xiuyuan).** District secretary who held the Shanghai
  District together single-handed after the 14-office search; restless, brave, does
  everything in person; his memoir "沪滨三次历险实录" is quoted at length in ch21. Later head
  of the Bureau's personnel section.
- **WANG TIANMU (王天木).** Former Shanghai District chief; loyalty in doubt; sent back to
  Tianjin after a quarrel with Dai. Daughters Kangzi (蝉红) and Yinzi (蝉绿) in Shanghai;
  Yinzi was attached to Wang Luqiao.
- **LIU YUANSHEN (刘原深 / Brother Yuanshen).** Intelligence compiler-reviewer, later an
  action-brigade leader; the very man who now revises "Nameless Heroes" for Chen - Chen's
  living memory-check throughout Part Three. Consult on every Shanghai-cast recall.
- **NEW cast built out in B15 (all keyed):** the five intelligence-group leaders (朱啸谷,
  刘健, 张圣才/葛越溪, 盛志成, 时寿章/朱岑楼), the eight action-brigade leaders (赵理君 1st,
  吉震苍 2nd, 蒋安华 3rd, 万里浪/刘时雍 then 徐晚枫/封企曾 4th, 汪福谦 5th, 潘绍岳 6th, 张秉权
  7th, 萧张权 8th), 毕高奎/黄志远 of New Group One, 孙大成 of the Kang Corps. These carry
  into ch22's operations.
- **Dead comrades carried in memory:** ZENG CHE 曾澈, WANG WEN 王文 (ch11); ZENG ZHONGMING
  曾仲鸣 (ch15/ch16); the B13 Wang-case martyrs; 陈三才 Chen Sancai (ch21, via New Group One).

## Where the book stands

- Part One (北国锄奸) COMPLETE (B01-B05).
- Part Two ("Disgrace at Hanoi") COMPLETE (B06-B13). The assassination FAILED; Chen took
  over the Shanghai District; the whole Hanoi cast is laid to rest in the record.
- **Part Three ("Renown Won in a Hundred Battles" / 百战声威) is under way (B14-B15).** ch20
  = self-preface; ch21 = the first Shanghai chapter (arrival, appointment, rebuilding the
  District, the full order of battle). ch21 ends previewing ch22: the reorganized District's
  first deterrent action case (mid-Oct 1939), Wan Lilang's defection to No.76, and the
  reappearing "international-spy" figure opening a new "intelligence war."
- **NEXT: B16 = ch22** - 第二章 春云乍展风雷初动 "Chapter 2. Spring Clouds Unfurl, the First
  Thunder Stirs," the SECOND Shanghai chapter and the LONGEST unit yet (~35,471 chars, 1
  <h2> + 292 <p>). drop=2; couplet-style sub-headings (L3 一警百清除障碍以展示威力 opens);
  STRAY 杀 fused onto the <h2> title (drop it; book.json title_en is clean; list the glitch).

## What is NEXT

- Batch B16 = ch22 (the second Shanghai chapter). Kickoff is the paste-block at the top.
  Runs to completion (no gate); ends by pasting the B17 kickoff. B17 = ch23.
- The frozen register reference is `reference/B01_frozen.md`. Narrative sits at 4.55-4.78
  en/han; prefaces/document-heavy chapters run higher.
- Sub-heading pattern DIFFERS by chapter. Styles seen: Part One numbered 一/二/三;
  ch11/ch14/ch20-title/ch21 COUPLET-STYLE with NO number prefix; ch12/ch13/ch15/ch16/ch17/
  ch18 numbered-in-parens (一)/(二)…; ch08/ch16/ch18 have a GLUED sub-heading; ch13's inner
  enumerated list rendered `####`. Grep each new chapter p-by-p.
- WATCH for source anomalies: cuts, misplaced-「 glitches, corrupt/dropped-character
  phrases, dropped full stops, the in-text "(第N章完)" coda pattern (ch12/ch13/ch16; ch21
  had "(第一章完下期续载)" WITH continued-next-issue + trailing content), a STRAY glyph fused
  onto a chapter title (ch22's 杀; cf. the survey's flag), fullwidth-zero (U+25CB) and
  Latin-O number forms, and pervasive single-character substitutions. Re-grep each batch's
  source for `\[\d+\]` note markers (none present through B15).

## Open items for the read-through / completion

- Feed decided renderings back to authority.json on completion: 军统 "the Juntong"; the full
  B02-B15 historical-name set (Part One; the Japanese/negotiator names; the Wang-essay set;
  the Part-Two Hanoi/Chongqing casts; the B13 martyrs; the B14/B15 Shanghai-District staff
  and order of battle).
- Japanese name readings to verify when the men recur (多田骏, 田代皖一郎, 土肥原贤二,
  板垣征四郎, 近卫文麿, 影佐祯昭, 今井武夫, 晴气庆胤; 大屋久寿雄 "Ōya Kusuo"; 横山秋马
  "Yokoyama Shūma" and 岩井英一 "Iwai Eiichi" of the Kōain, both new in ch21's Liu-Shaokui
  memoir quote).
- Provisional romanizations to firm up when sources allow (glossary `provisional` rows,
  incl. the whole B15 Shanghai-District cast).
- Stray source glyphs still to resolve: 毛酋 in a ch36 section title (ch22's title 杀 is
  handled in B16). The ch22 last line (…预计一周左右即可获得) may be a mid-sentence source cut
  - confirm at build.

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01-B15 builds (0/0/0/0). Source is a clean
  digital EPUB, predominantly simplified with residual variant glyphs and pervasive
  digitization glitches (list them, render to plain sense, do not footnote mechanical
  typos). B01-B15 glitch lists are in PROGRESS.md.
- Running-header line 英雄无名-陈恭澍 opens all 43 content files: drop it. drop count is
  variable - most drop=2; ch01/ch10/ch20 drop=3.
- Enumerated ；/：/、 bullet lists, quoted-document/roster lines, salutations, verse lines,
  and 『』-closed dialogue in the source are DELIBERATE separate `<p>` - do NOT merge them;
  only genuine mid-phrase splits (last char not terminal, OR a source `<p>` boundary that
  severs one sentence) merge, and those can CHAIN across 3+ fragments. A line ending on a
  dash lead-in that is its OWN source `<p>` is DELIBERATE, NOT a split (cf. ch20 L12, ch21
  L51/L66). ALWAYS confirm the extracted body count p-by-p against data/src_epub.
- Faithful numbering gaps/anomalies (NOT errors): Part Three skips ch7, splits ch10 into
  (上)/(下); 三面受敌 一往无前 titles two chapters (ch14 and ch24); ch09 printed §五 before
  §四; ch13 restarts its (一)-(五) numbering for the appended essay; ch16 reproduces two
  whole Wang documents; ch21 carries a magazine "下期续载" seam mid-chapter. Preserve and,
  where a reader would stumble, footnote.
- Expect a stray per-task branch at the top of every batch; consolidate onto
  claude/nameless-heroes per rule 2.
