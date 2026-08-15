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
Nameless Heroes B14

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once (its ONE failing regression test, "hook stands down on template stub", is a KNOWN false alarm; all others pass), then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05), B02 (ch06), B03 (ch07), B04 (ch08), B05 (ch09), B06 (ch10 preface + ch11), B07 (ch12), B08 (ch13), B09 (ch14), B10 (ch15), B11 (ch16), B12 (ch17) and B13 (ch18 + ch19) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them. PART TWO ("Disgrace at Hanoi") is COMPLETE; the EPUB now holds 19/43 chapters, 208 notes.

Do Batch B14 = ch20 (ONE unit, ~3,417 source chars): ch20 = 「上海抗日敌后行动」自序 "Author's Preface: Shanghai Behind-the-Lines Operations Against Japan" - the SELF-PREFACE that OPENS PART THREE, whose part title is 「百战声威」 "Renown Won in a Hundred Battles" (Chen's working content-title is 对日抗战上海敌后行动). Chen explains the Part-Three title change, sets the 28-Aug-1939-to-Oct-1941 Shanghai District scope (the same span the ch19 notice announced), and previews the several-hundred action-cases of the Shanghai chapters to come. Read the tail of ch18 English (out/ch18_reading.md section (3): the "作者" self-portrait as one of three Hanoi survivors, the forward reference to Part Three "Renown Won in a Hundred Battles"/百战声威 and the not-yet-titled Part Four, publication set for 七十三年) and ch19 (the author's notice) for register + story continuity. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch20 from data/src (21_index-split-000-0019.txt). CONFIRM structure against data/src_epub/OEBPS/Text/index_split_000_0019.xhtml [parses to 1 <h1>「百战声威」 + 26 <p>, NO <h2>, NO <br/>, NO <img>]. STRUCTURE NUANCE: unlike the Part-Two preface (ch10, drop=3 = header + <h1> + <h2>), here the <h1> is the PART-THREE divider 「百战声威」 and the preface's OWN title 「上海抗日敌后行动」自序 is the FIRST <p> (txt L2), not heading markup. So drop=2 (running header 英雄无名-陈恭澍 + the <h1>「百战声威」 part title), and the L2 title-as-<p> must be handled deliberately: EITHER emit it as a STANDALONE heading (the reading.md ## comes from book.json title_en; if you keep L2 as a body line it duplicates the title) OR fold it - grep p-by-p and decide, recording the choice in PROGRESS. The builder renders Part dividers from book.json structure, so do NOT translate 「百战声威」 as a body paragraph. GREP for (一)-style paren sub-headings [none found in a first pass; Part-One prefaces used bare 一/二/三, ch11/ch14 used couplet-style with no number - confirm p-by-p] and for an in-text coda / 完. GREP the source for note markers (\[\d+\]) and record "none present" (none through B13).
2. Extend scripts/clean_batch.py with ch20's spec (drop=2; merges = re-derived mid-phrase pairs [last char not in 。！？」）…—]; glued {}; standalone = [the L2 自序 title-as-<p>] IF you emit it as a heading, else []). Keep quoted-title / enumerated (；/：/、) lines as SEPARATE <p> and do NOT merge (cf. ch12/ch13/ch16/ch17/ch18). Run it (source-conservation check). Write out/ch20_reading.md (## chapter title from book.json = "Author's Preface: Shanghai Behind-the-Lines Operations Against Japan"; one English paragraph per source body line). Then run scripts/batch_artifacts.py ch20, and ALWAYS finish with a NO-ARG run (the batch_artifacts.py trap: an ID-run writes checks.json with ONLY that unit; the no-arg run restores all 20 units so check_structure/check_content see them).
3. Translate to the FROZEN register (Chen's voice sheet in HANDOFF; prefaces run DENSER, ~5.2 en/han - the B01 prefaces and ch10 are the models). Consult glossary.json and authority.json BEFORE romanizing anything; REUSE the settled renderings: the Juntong; the book title 英雄无名 = "Nameless Heroes" (in-text, NOT "Heroes Without a Name"); Part One 北国锄奸 = "Rooting Out Traitors in the North"; Part Two = "Disgrace at Hanoi" (Chen's own name for it in-text is 河内汪案始末 "The Whole Story of the Wang Case at Hanoi"); Part Three 百战声威 = "Renown Won in a Hundred Battles"; 卷头长白 = "Prefatory Candour"; 上海区 "the Shanghai District"; 军事委员会调查统计局 the Juntong's full name "Bureau of Investigation and Statistics of the Military Affairs Commission"; Dai Li / 戴雨农 "Dai Yunong"; 汪精卫 Wang Jingwei / 汪逆 "the traitor Wang". Render Republican years literally ("the twenty-eighth year"; the checker matches the source numeral). NEW cast is unlikely in a preface, but give pinyin fields for any name and check authority.json/glossary first. Part Three PRINCIPALS reset - this preface opens the Shanghai volume.
   WATCH ch20's digitization glitches (list in PROGRESS.md, render to plain sense, footnote only real reading uncertainty): the same single-character-substitution classes as ch15-ch18 (先↔光, 卫→术, 汪→江, 文↔交, 员→负, 板→扳, 从→徙, 该→孩, 困→因, 科→料, 综→踪, 局→昂, etc.). Dates/counts (the 28 Aug 1939 - Oct 1941 span, the several-hundred cases): carry real values as DIGITS / explicit words; NOISE only elided-tens / approximate / name-embedded / idiom forms - add a commented B14 block to data/noise.txt if needed (the elided-tens block is ordered LONGEST-FIRST; keep any new compound BEFORE the bare form it contains; note that a project noise entry can be PRE-EMPTED by an earlier substring rule - the B13 fix was to noise 千难 not 千难万难 because an earlier 万难 rule stripped the 万难 half first).
4. Checks: verify_unit.py ch20 (parity + numbers with --noise auto-found + anchors); check_align.py ch20; regenerate checks.json with scripts/batch_artifacts.py (no args) and run check_structure.py --config checks.json + check_content.py --config checks.json (NOTE: check_content prints KNOWN PRE-EXISTING artifacts and exits nonzero because of them - ch07 Zhanggu ×1, ch08 Shunde ×3, ch13 Miss Nguyen/Oya Kusuo/Yuan Haowen ×9 - diacritic/variant substring-match artifacts, NOT regressions; CONFIRM ch20 itself shows "all in the paired paragraph" / 0 displaced. Do NOT add book-TITLE glossary rows keyed on full hanzi, and do NOT add COMMON-NOUN keys - a glossary key must be a distinctive proper noun that renders ONE way everywhere, and must not occur in another chapter with a different rendering [B13 skipped 铅山 for this reason]). qc_entities.py on a reconstructed bilingual (data/zh body lines + out/ch20_en.json, `> zh` / en pairs, strip the ### heading lines; every glossary row needs a pinyin field). Verify the TAIL against the source. check_register.py --ref reference/B01_frozen.md out/ch20_reading.md ("shall" in Chen's narration is deliberate; a preface runs denser - read the note, do not de-formalize).
5. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (the full list is in PROGRESS.md - it now includes the B13 additions: 邓演达 Deng Yanda, the 还都 "return of the capital", 荆轲聂政 Jing Ke and Nie Zheng, 雨花台 Yuhuatai, the 常山/Yan Gaoqing allusion, 传记文学 Biographical Literature). A Part-Three preface earns notes mostly for the STRUCTURE of the book / any new place or institution; 卷头长白, 北国锄奸/河内/百战声威 titles, 军统 the Juntong, the Republican-calendar convention are all covered - do NOT re-note. Be generous but do NOT pad. Merge notes via apparatus_merge.py (numeric character references only in note bodies - keep them ASCII where possible; anchors verbatim ASCII substrings of the reading.md body text, NO em dash and NO quote character - substring traps; multi-occurrence anchors attach at first occurrence). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field; apparatus_merge's glossary path assumes a FLAT map and would corrupt the sectioned file - use it ONLY for notes). Confirm ch20 carries no images (it has none).
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; update HANDOFF.md; commit and push to claude/nameless-heroes. B14 OPENS Part Three - flag that in PROGRESS/HANDOFF (next is B15 = ch21, the first Shanghai chapter).

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B15 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
```

## What is DONE (do not redo)

- **Step 0 (survey).** Ingest + book.json (43 chapters, 5 TOC parts) +
  skeleton EPUB. See the survey section of PROGRESS.md.
- **Batch B01 (ch01-ch05), the front matter.** 67 notes. **VOICE GATE PASSED:**
  the B01 front matter is the FROZEN register reference (`reference/B01_frozen.md`)
  for `check_register.py --ref` from B02 on.
- **Batch B02 (ch06), Part One Section 1.** 322 paragraphs; 24 notes; 17 glossary rows.
  The once-per-book blind double-translation and back-translation samples were done here.
- **Batch B03 (ch07), Part One Section 2.** 362 paragraphs; the Zhang Jingyao case.
- **Batch B04 (ch08), Part One Section 3.** 461 paragraphs; the Ji Hongchang case,
  the Wang Zixiang poison death, the 9 Nov 1934 Guomin Hotel shooting.
- **Batch B05 (ch09), Part One Section 4.** 332 paragraphs; the Shi Yousan case.
  **Part One COMPLETE.**
- **Batch B06 (ch10 + ch11), Part Two opens.** ch10 = the Part Two Author's Preface;
  ch11 = "Bloodshed Against the Enemy". **Part Two title RESOLVED: "Disgrace at Hanoi."**
- **Batch B07 (ch12), Part Two Chapter 2.** "Unfathomable Hearts, Hidden Designs".
- **Batch B08 (ch13), Part Two Chapter 3.** "Treacherous Tides, a Gathering Storm"
  (262 body paragraphs, largest of Part Two). First use of `{p}` verse.
- **Batch B09 (ch14), Part Two Chapter 4.** "Beset on Three Sides, Ever Forward" - a
  very short (520-char) bridge chapter; 0 new notes.
- **Batch B10 (ch15), Part Two Chapter 5.** 第五章 博浪一击 误中副车 "A Blow at Bolang,
  the Wrong Carriage Struck" - the CLIMAX: the failed poison-bread "soft action", the
  sanction order (19 Mar 1939), the botched Red River bridge chase, the night raid
  killing Zeng Zhongming by mistake. 225 paragraphs; 11 notes. **Name trap RESOLVED:
  郑邦国 -> 陈邦国 "Chen Bangguo".**
- **Batch B11 (ch16), Part Two Chapter 6.** 第六章 奸伪卑劣 寿张为幻 "Vile Treachery,
  Illusions Undone" - the reckoning/indictment chapter: Chen owns the failure, escapes
  to Chongqing, quotes and rebuts Wang's eulogy 「曾仲鸣先生行状」 and apologia 「举一个例」,
  Chiang's 17 Apr press conference and Wu Jingheng's 9,000-word essay. 116 paragraphs;
  8 notes; 34 glossary rows.
- **Batch B12 (ch17), Part Two Chapter 7.** 第七章 临深履薄 锲而不舍 "Treading Thin Ice,
  Never Relenting" - Chen recalled to Chongqing, idled as Acting Chief of the Third
  Section, then reassigned to Shanghai. Quotes IN FULL Wang Jingwei's 30 Mar 1939
  autograph letter to 龙云 Long Yun (志舟) - dated NINE DAYS AFTER the sanction, so NOT
  its cause - plus Kagesa Sadaaki's memoir and 蒋总统秘录 on Wang's Hanoi->Shanghai flight,
  the 三点协议事项, and the June 1939 Tokyo talks; ends with Chen's last parting from Dai
  Li and Wang Luqiao's 14 July 1939 arrest. 147 body paragraphs; **9 notes (202
  cumulative)**; **49 glossary rows**. All checks green; qa_epub PASS; epubcheck 0/0/0/0.
  EPUB now **17/43 chapters**. Detail in PROGRESS.md ("Batch B12").
- **Batch B13 (ch18 + ch19), Part Two Chapter 8 + the closing Author's Note. PART TWO
  COMPLETE.** ch18 = 第八章 再接再励前仆后继 "Chapter 8. Renewed Effort, Wave upon Wave" -
  Chen takes over the Shanghai District (12 Aug 1939), tracks Wang's Shanghai/Nanjing
  movements and the 30 Mar 1940 "还都" farce, then mourns the "wave upon wave" of martyrs
  who took up the sanction after Hanoi (Wu Gengshu + Dai Jingyuan, Chen Sancai, Huang
  Yiguang, Shao Mingxian) and accounts for ALL NINETEEN Hanoi participants (dead /
  whereabouts-unknown / living). ch19 = 「英雄无名」作者小启 "A Note from the Author"
  (signed May 1983), announcing the Part-Three Shanghai volume. 138 + 4 body paragraphs;
  **6 notes (208 cumulative)**; **21 glossary rows**. THREE (一)-(三) sub-headings ((一)
  standalone L3; (二)/(三) glued at L31/L86). All checks green; qa_epub PASS; epubcheck
  0/0/0/0. EPUB now **19/43 chapters**. Detail in PROGRESS.md ("Batch B13").

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` - derives data/zh/<id>.txt verbatim from data/src,
  applying per-unit drops/merges/heading-splits with a source-conservation check.
  Specs for ch01-ch17. Merge logic FOLLOWS CHAINS (a `<p>` split into 3+ fragments is
  rejoined whole). **drop is variable:** most chapters drop=2; ch01 and ch10 drop=3.
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
  of them: ch07 Zhanggu (1), ch08 Shunde (3), ch13 Miss Nguyen/Oya Kusuo/Yuan Haowen
  (9) - diacritic/variant forms the substring matcher cannot align. These are NOT
  regressions; the pass criterion for a NEW batch is "the batch's own unit shows all
  name occurrences in the paired paragraph / 0 displaced." Do NOT add book-TITLE
  glossary rows keyed on the full hanzi title, and do NOT add COMMON-NOUN keys: the B12
  near-miss was 小巷子 "little lane" (removed after it cross-flagged ch06/07/13/15). A
  glossary key must be a DISTINCTIVE proper noun that renders ONE way everywhere.
- **Verse marker `{p}`** (first used in ch13): prefix a pure-verse body line with
  `{p} ` and the builder renders `<p class="verse">`; the checks strip it. ch15/16/17
  used none.
- Glossary is authored/merged BY HAND into the SECTIONED file
  (people/organizations/places/terms), idempotent + re-read-verified. **Every row
  MUST carry a `pinyin` field** - `qc_entities.py` does `rec["pinyin"]` and KeyErrors
  otherwise. apparatus_merge's glossary path assumes a FLAT map and would corrupt the
  sectioned file; NOTES still go through apparatus_merge.py.
- **Note-anchor gotchas:** American-style punctuation puts the period INSIDE the
  closing quote (anchor on an interior phrase). The reading.md uses STRAIGHT
  quotes/apostrophes AND U+2014 em dashes freely; keep anchors ASCII, WITHOUT any
  quote character AND without an em dash (either is a substring trap). Multi-occurrence
  anchors attach at the FIRST occurrence (correct first-appearance placement);
  check_structure reports "attach at first of several".
- data/noise.txt carries the B01-B12 project noise rules (each with a comment line).
  Republican years are rendered literally in Part Two ("the twenty-eighth year"); the
  checker matches the source numeral directly. **The elided-tens block is ordered
  LONGEST-FIRST:** a compound like 四、五百 MUST precede the bare 四、五. Fullwidth-zero
  years/refs (一九○五 / 二○三 / 二○九, ○ = U+25CB) AND Latin-O forms (二 O 五 = page 205)
  must be noised - the checker cannot compose them - and the value carried in the
  English. Number-garbles (四万百五千百 = 450 million, 六十万百 = ~600 million) are noised
  and the plain-sense value carried. Name/idiom-embedded numerals are noised too
  (征四郎, 八郎; 十万大山, 百梅; 几两重, 颠三倒四, 千金).
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches it; re-run
  per session). setup.sh's ONE failing regression test ("hook stands down on template
  stub") is a KNOWN false alarm; all other regression tests pass.

## Renderings settled / carry-forward

- 军统 / 军统局 -> "the Juntong" (DECIDED). 戴笠 Dai Li (courtesy Yunong; 老板 "the Boss";
  戴先生 "Mr. Dai"; 戴雨农 "Dai Yunong"); 汪精卫 Wang Jingwei (原名 汪兆铭 "Wang Zhaoming";
  汪逆 "the traitor Wang"; 汪某 "the man Wang"; 汪氏 "Wang"); 陈璧君 Chen Bijun / 汪夫人
  "Madame Wang". 制裁 "sanction"; 制裁令 "sanction order". Chiang's titles: 校长 "the
  Commandant", 领袖 "the Leader", 委员长 "the Generalissimo", 蒋公 "the Generalissimo, Mr.
  Chiang", 总裁 "the Director-General" (Wang = 副总裁 "Vice-Director-General"). 总理 = "the
  Party Leader" / 国父 = "the Father of the Nation" = Sun Yat-sen. Floors: 二楼/三楼 =
  "second/third floor". Republican years literal in Part Two. 引刀成一快，不负少年头 = "I
  bare the blade and laugh, true to the boy I was" (Wang's 1910 poem). 上海滩 "the
  Shanghai Bund". 高朗街 "Gao Lang Street" (DECIDED; NOT "Rue Colombert" - the B12 fix).
- **Book / part titles (in-text renderings, DECIDED; reuse verbatim):** 英雄无名 =
  "Nameless Heroes" (NOT "Heroes Without a Name"); Part One 北国锄奸 = "Rooting Out
  Traitors in the North"; Part Two = "Disgrace at Hanoi" (Chen's own in-text name for
  it is 河内汪案始末 "The Whole Story of the Wang Case at Hanoi"); Part Three 百战声威 =
  "Renown Won in a Hundred Battles"; 卷头长白 = "Prefatory Candour"; 军事委员会调查统计局
  the Juntong's full name = "Bureau of Investigation and Statistics of the Military
  Affairs Commission". B13 additions in glossary: 传记文学 = "Biographical Literature"
  (the Zhuanji Wenxue journal); 新一组 = "New Group One"; 雨花台 = "Yuhuatai"; the Wang-case
  martyrs Chen Sancai, Huang Yiguang, Dai Jingyuan (原名 Dai Xingbing), Shao Mingxian,
  Wu Gengshu; 极司非而路 = "Jessfield Road" (a source-variant spelling of 极司菲尔路).
- **B03-B11 shelves (reuse; in glossary.json):** the Juntong internal units,
  Tianjin/Beiping/Hong Kong/Hanoi geography, the Mauser "box-cannon", the Green Gang,
  the Kwantung Army, Manchukuo, the "Yan Telegram", the Three Principles of the People,
  Konoe's "New Order in East Asia", 支那 = "Shina", the Kōain, the Tanaka Memorial;
  people: Cen Jiazhuo, Yu Lexing, Zhou Fohai, Chen Gongbo, Gao Zongwu, Mei Siping,
  Kagesa, Konoe, Long Yun, Zeng Zhongming; Hanoi: 徐先生 "Mr. Xu", 魏春风 Wei Chunfeng,
  阮小姐 Miss Nguyen, 高朗街 "Gao Lang Street", Haiphong; the B10/B11 additions (Chen
  Bangguo, Tang Yingjie, Yu Jiansheng, the Zeng household, Hiranuma, Wu Jingheng, the
  National Defense Council roster, the traitor/puppet archetypes, the elders and 行状
  revolutionaries, Dana + the three captured). Books handled by FOOTNOTE (ch15/ch17):
  蒋总统秘录, 戴雨农先生传, 戴雨农先生全集, 汪政权的开场与收场, 沪滨三次历险实录.
- **B12 shelf (ch17; reuse; in glossary.json, all with pinyin).** The Chongqing/Juntong
  cast: 王兆槐 Wang Zhaohuai, 王持平 Wang Chiping, 周伟龙 Zhou Weilong, 徐钟奇 Xu Zhongqi,
  赵世瑞 Zhao Shirui, 陶一珊 Tao Yishan, 赵理君 Zhao Lijun, 胡尚武 Hu Shangwu, 白绳祖 Bai
  Shengzu, 潘其武 Pan Qiwu, 王飞 Wang Fei, 帅崇兴 Shuai Chongxing, 朱啸谷 Zhu Xiaogu, 刘俊卿
  Liu Junqing, 刘绍奎 Liu Shaokui, 王亢子 Wang Kangzi (蝉红), 王因子 Wang Yinzi (蝉绿). The
  Japanese: 犬养健 Inukai Ken, 犬养毅 Inukai Tsuyoshi, 周隆庠 Zhou Longxiang, 有田八郎 Arita
  Hachirō, 西尾寿造 Nishio Toshizō, 佐藤贤了 Satō Kenryō, 矢野征记 Yano Seiki, 清水董三
  Shimizu Tōzō, 谷垣专一 Tanigaki Sen'ichi, 仓冈克行 Kuraoka Katsuyuki, 板垣征四郎 Itagaki
  Seishirō (= the existing 坂垣 row; source writes 板垣/坂垣/扳垣). Chinese: 陈调元 Chen
  Diaoyuan, 邓龙光 Deng Longguang. Orgs: 南华日报 South China Daily News, 西南运输公司
  Southwest Transport Company, 特务团 Special Service Regiment, 中央训练团 Central Training
  Corps, 政友会 Seiyūkai, 临时政府 Provisional Government, 维新政府 Reformed Government. Ships:
  北光丸 Hokkō Maru, 霞飞将军 Général Joffre. Places: 望龙门 Wanglongmen, 浮屠关 Futuguan,
  愚园路 Yuyuan Road, 杜美路 Route Doumer, 极司菲尔路 Jessfield Road (No. 76), 卡尔登公寓
  Carlton Apartments, 吴淞口 Wusong bar, 黄埔江 Huangpu River, 麦阳路 Maiyang Road, 基隆
  Keelung. Western contemporaries (Hitler, Mussolini, Lenin, Stalin, Trotsky) rendered
  directly, NOT glossary'd.

## ⚠ Name trap RESOLVED (do not reopen): 陈邦国 / 郑邦国

The Hanoi action-team member the source spells 郑邦国 in ch13 (B08) and 陈邦国 in ch15
(B10) + ch16 (B11) + ch17 (B12) plus the quoted Biography of Dai Yunong (陈). This is ONE
man (one of the three captured). RESOLVED to **Chen Bangguo (陈邦国)**: glossary key
renamed; the BUILT ch13 unit updated; the discrepancy footnoted at the first ch15
occurrence. Romanization stays `provisional`. Use Chen Bangguo consistently.

## Voice sheet - CHEN GONGSHU (author / narrator)

- REGISTER: educated, formal, essayistic first person; grave and a touch archaic but
  not stilted. Long semicolon-joined clauses; four-character idiom and classical
  allusion used freely and footnoted when they carry weight. Refers to himself as
  笔者 "the writer" and 我 "I". His narrating "shall" is DELIBERATE - do not
  de-formalize it; check_register flags it informationally (B06 33%, B08 29%, B10 9%,
  B11 0%, B12 43%, verified deliberate - the B12 spike is the quoted Wang letter +
  Kagesa memoir).
- STANCE: self-justifying yet self-effacing; insists on truthfulness, admits his
  blunders; tender toward dead comrades, bitter and scornful toward the enemy. When
  quoting hostile/puppet documents (Wang's letter, Kagesa's memoir, the 蒋总统秘录),
  keep the quoted register (formal, literary, self-pitying / bureaucratic-Japanese)
  DISTINCT from Chen's own dry scorn. Keep those registers apart when they recur.
- Ratio ~4.55-4.78 en/han in narrative; prefaces denser (~5.2); document-/essay-heavy
  chapters run higher (ch12 4.84, ch13 4.79, ch15 4.60, ch16 4.78, ch17 4.78). A
  chapter thick with quoted documents lifts it; read the note, do not reset.

## Voice sheets - principal & recurring cast

- **DAI LI (戴雨农 / Mr. Dai / 老板 "the Boss").** In ch17 gave Chen the new Shanghai task
  over a farewell banquet, then the LAST parting - after ch17 they meet no more, only
  letters and telegrams ("追忆前情，言之心痛"). Warm off duty, abrupt on business.
- **MAO RENFENG (毛人凤 / Mr. Mao).** Ran the Juntong Chongqing HQ ("Xiaoxiangzi") as Dai's
  representative; kind to Chen (gave him a tunic, taught him the paperwork). Younger
  brother 毛万里 Mao Wanli runs the Shanghai region as inspector-general and directs Wang
  Luqiao's sanction mission.
- **WANG LUQIAO (王鲁翘 / Luqiao).** Part Two principal (cast 8). The trigger-man who shot
  Zeng in error; bluff, bold, loyal. Transferred Hanoi->Shanghai, ARRESTED 14 July 1939
  in the French Concession (a tryst with Wang Yinzi), shipped back to Hanoi, sentenced
  to life; freed after the war with Zhang Fengyi, Yu Jiansheng, Chen Bangguo.
- **FANG BINGXI (方炳西 / Brother Bingxi).** Part Two principal (cast 7). The advance man /
  cipher-holder; wound up Hanoi after Chen's recall. Survives.
- **WANG TIANMU (王天木).** Part Two principal (cast 5). Former Shanghai District chief; by
  ch17 his loyalty is in doubt (the "you turtle's egg" telegram; Dai sends Chen to
  Shanghai partly to understand and recover him, guaranteeing his safety). His daughters
  Kangzi (蝉红) and Yinzi (蝉绿) are in Shanghai. His turn is a live thread going into B13.
- **YU LEXING (余乐醒 / Brother Lexing / Dr. Yu).** France-trained chemist; the "small can"
  poison-gas device he left in the Wang bathroom resurfaces in ch17 (Chen Bijun asks
  Chen about it at his 1941 arrest). NOTE the split: 余乐醒 = "Brother Yu Lexing"; 乐醒兄 =
  "Brother Lexing".
- **CAO SHI'ANG (曹师昂) / TAN TIANQIAN (谭天堑).** Hanoi comrades with follow-up actions in
  ch17 (Cao's French wife "interviewed" Chen Bijun; Tan's scheme failed and he was
  punished). Render straight if they recur.
- **ZHENG JIEMIN / FAN XING.** Part Two principals (4, 6), off-stage in B06-B12.
- **Dead comrades carried in memory:** ZENG CHE 曾澈, WANG WEN 王文 (ch11); ZENG ZHONGMING
  曾仲鸣, killed at Hanoi in Wang's place (ch15/ch16). B13 (ch18, 前仆后继) will name the
  successive Shanghai/Nanjing martyrs who followed.

## Where the book stands

- Part One (北国锄奸) is COMPLETE (B01-B05).
- **Part Two - "Disgrace at Hanoi" (河内辱命)** is COMPLETE (B06-B13): B06 = Preface (ch10) +
  Chapter 1 (ch11); B07 = Ch2 (ch12); B08 = Ch3 (ch13); B09 = Ch4 (ch14); B10 = Ch5
  (ch15, the CLIMAX); B11 = Ch6 (ch16, the reckoning); B12 = Ch7 (ch17, the recall +
  Shanghai reassignment); B13 = Ch8 (ch18, the successive martyrs + 还都 farce + the
  19-participant accounting) + ch19 (the closing Author's Note). The assassination FAILED;
  Wang Jingwei died at Nagoya on 10 Nov 1944; Chen has taken over the Shanghai District,
  and the whole Hanoi cast has been laid to rest in the record.
- **NEXT: B14 = ch20** - 「上海抗日敌后行动」自序 "Author's Preface: Shanghai Behind-the-Lines
  Operations Against Japan," the SELF-PREFACE that OPENS Part Three ("Renown Won in a
  Hundred Battles" / 百战声威). ~3,417 chars; 1 <h1>「百战声威」 (part divider) + 26 <p>, no
  <h2>. STRUCTURE NUANCE: the preface's own title 「上海抗日敌后行动」自序 is the first <p>
  (L2), not heading markup - drop=2 (header + <h1> part title), decide L2 heading-vs-fold.

## What is NEXT

- Batch B14 = ch20 (the Part Three "Shanghai" self-preface, 「上海抗日敌后行动」自序). Kickoff
  is the paste-block at the top. Runs to completion (no gate); ends by pasting the B15
  kickoff. B15 = ch21 (the first Shanghai chapter of Part Three).
- The frozen register reference is `reference/B01_frozen.md`. Narrative sits at
  4.55-4.78 en/han; document-/essay-heavy chapters run higher; a chapter with quoted
  documents may lift it. Read the note, do not reset.
- Sub-heading pattern DIFFERS by chapter. Styles seen: Part One numbered 一/二/三;
  ch11/ch14 COUPLET-STYLE with NO number prefix; ch12/ch13/ch15/ch16/ch17/ch18
  numbered-in-parens (一)/(二)…; ch08/ch16/ch18 have a GLUED sub-heading (on a paragraph
  tail); ch13's inner enumerated list 一、-六、 rendered `####`. Grep each new chapter
  p-by-p.
- WATCH for source anomalies: cuts, misplaced-「 glitches, corrupt/dropped-character
  phrases, terminal-」 name-splits, the in-text "(第N章完)" coda pattern (ch12/ch13/ch16;
  ch14/ch15/ch17 had none - CONFIRM for ch18 by grep), fullwidth-zero (U+25CB) and
  Latin-O number forms, and pervasive single-character substitutions. Re-grep each
  batch's source for `\[\d+\]` note markers (none present through B12).

## Open items for the read-through / completion

- Feed decided renderings back to authority.json on completion: 军统 "the Juntong"; the
  full B02-B12 historical-name set (Part One; the B06-B07 Japanese/negotiator/elder
  names; the B08 Wang-essay set; the B10/B11 additions; the B12 Chongqing/Shanghai/
  Japanese cast and the Provisional/Reformed governments).
- Japanese name readings to verify when the men recur (多田骏, 田代皖一郎, 土肥原贤二,
  坂垣/板垣征四郎, 近卫文麿, 影佐祯昭, 今井武夫, 晴气庆胤, 伊藤芳男; 大屋久寿雄 "Ōya Kusuo";
  平沼骐一郎 "Hiranuma Kiichirō"; 川樾 "Kawagoe"; the B12 additions: 犬养健/毅 "Inukai",
  有田八郎 "Arita Hachirō", 西尾寿造 "Nishio Toshizō", 佐藤贤了 "Satō Kenryō", 矢野征记
  "Yano Seiki", 清水董三 "Shimizu Tōzō", 谷垣专一 "Tanigaki", 仓冈克行 "Kuraoka").
- Identify 剑秋 "Jianqiu" (a 1932 Nanjing "elder brother" of Chen) when sources allow.
- Stray source glyphs still to resolve: trailing 杀 on the ch22 title; 毛酋 in a ch36
  section title. (ch16 寿张为幻 and ch17 世居/廷企 handled by sense + PROGRESS list.)
- Provisional romanizations to firm up when sources allow (glossary `provisional` rows,
  incl. the B10/B11/B12 additions: Tang Yingjie, Yu Jiansheng, Chen Bangguo, the Zeng
  household; Su Xiwen, Dana, the three captured, Li Zhongshi, Yu Yunji; the B12
  Chongqing/Shanghai personnel and 矢野/谷垣/仓冈).

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01-B12 builds (0/0/0/0). Source is a clean
  digital EPUB, predominantly simplified with residual variant glyphs and pervasive
  digitization glitches (list them, render to plain sense, do not footnote mechanical
  typos). B01-B12 glitch lists are in PROGRESS.md.
- Running-header line 英雄无名-陈恭澍 (from the `<title>`) opens all 43 content files: drop
  it. drop count is variable - most drop=2; ch01 and ch10 drop=3.
- Enumerated ；/：/、 bullet lists, quoted-document/roster lines, salutations, and verse
  lines in the source are DELIBERATE separate `<p>` - do NOT merge them; only genuine
  mid-phrase splits (last char not terminal, OR a source `<p>` boundary that severs one
  sentence) merge, and those can CHAIN across 3+ fragments. ALWAYS confirm the extracted
  body count p-by-p against data/src_epub.
- Faithful numbering gaps/anomalies (NOT errors): Part Three skips ch7, splits ch10 into
  (上)/(下); 三面受敌 一往无前 titles two different chapters (ch14 and ch24); ch09 printed
  §五 before §四; ch13 restarts its (一)-(五) numbering for the appended essay; ch16
  reproduces two whole Wang documents. Preserve and, where a reader would stumble, footnote.
- GLOSSARY-KEY DISCIPLINE (the B12 lesson): a key must be a DISTINCTIVE proper noun that
  renders ONE way everywhere. Do NOT key common nouns (小巷子 "little lane" cross-flagged
  four chapters) or full book titles (they cross-flag chapters rendering the title
  slightly differently). Books -> FOOTNOTES.
- Expect a stray per-task branch at the top of every batch; consolidate onto
  claude/nameless-heroes per rule 2.
