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
Nameless Heroes B13

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once (its ONE failing regression test, "hook stands down on template stub", is a KNOWN false alarm; all others pass), then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05), B02 (ch06), B03 (ch07), B04 (ch08), B05 (ch09), B06 (ch10 preface + ch11), B07 (ch12), B08 (ch13), B09 (ch14), B10 (ch15), B11 (ch16) and B12 (ch17) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them.

Do Batch B13 = ch18 + ch19 (TWO units, ~16,683 source chars): ch18 = 第八章 再接再励前仆后继 "Chapter 8. Renewed Effort, Wave upon Wave" (~16,173 chars) - the EIGHTH and LAST chapter of PART TWO ("Disgrace at Hanoi"): the successive patriots who took up the sanction of Wang after Chen (前仆后继 = "one falls, the next steps forward"), the Nanjing "还都" (return-of-the-capital) farce of 30 March 1940, and Chen mourning the Hanoi-case dead. ch19 = 「英雄无名」作者小启 "A Note from the Author" (~510 chars) - a short authorial notice CLOSING Part Two, signed 陈恭澍谨启七十二年五月 (May 1983), inviting former 上海区 comrades to send in corrections/material before the Part Three (Shanghai) volume runs in 传记文学. Read the tail of ch17 English (out/ch17_reading.md section (3): Chen's last parting from Dai Li, the reassignment to Shanghai, Wang Luqiao's 14 July 1939 arrest, and the closing 后记/十九个-participants forward reference) and ch17 for register + story continuity. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch18 from data/src (19_index-split-000-0017.txt) and ch19 (20_index-split-000-0018.txt). Both drop=2 (running header 英雄无名-陈恭澍 from <title> + the <h2> chapter title; CONFIRM against data/src_epub/OEBPS/Text/index_split_000_0017.xhtml [parses to 1 <h2> + 143 <p>, NO <br/>, NO <img>] and index_split_000_0018.xhtml [1 <h2> + 4 <p>, NO <br/>, NO <img>]). ch18 has THREE numbered-in-parens sub-headings (一)-(三): (一)总是跟在后头就已失去机先 [L3, STANDALONE, its own <p>]; (二)痛定思痛字字为汪案牺牲者悼念 [GLUED to the tail of L31, cf. ch08/ch16]; (三)生死荣辱之中也有幸与不幸 [GLUED to the tail of L86, cf. ch08/ch16] - grep each p-by-p against data/src_epub to CONFIRM standalone vs glued and re-derive the exact glued-heading substrings. ch19 has NO sub-headings (4 body <p>: the 拙着…第三部 announcement, the 三种态度/两点谅解 body, the 来信请寄 line, and the 陈恭澍谨启七十二年五月 signature line - keep the signature as its own paragraph). RE-DERIVE each extractor mid-phrase split against the XHTML (last char not in 。！？」）…—): scan both units p-by-p; keep quoted-document / roster / enumerated (；/：/、) lines as SEPARATE <p> and do NOT merge (cf. ch12/ch13/ch16/ch17). GREP each source for note markers (\[\d+\]) and record "none present" in PROGRESS.md (none through B12). NOTE: check whether ch18 carries an in-text "(第八章完)" or Part-Two-closing coda (ch12/ch13/ch16 had one; ch14/ch15/ch17 did not) - confirm by grep, don't assume.
2. Extend scripts/clean_batch.py with ch18's + ch19's specs (drop=2 each; ch18 merges = the re-derived mid-phrase pairs, glued {31: "(二)…", 86: "(三)…"}, standalone [3]; ch19 merges = any re-derived pairs, glued {}, standalone []). Run it (source-conservation check). Write out/ch18_reading.md and out/ch19_reading.md (## chapter title from book.json; ### for each ch18 (一)-(三) sub-heading; one English paragraph per source body line). Then run scripts/batch_artifacts.py ch18 && scripts/batch_artifacts.py ch19, and ALWAYS finish with a NO-ARG run (the batch_artifacts.py trap: an ID-run writes checks.json with ONLY that unit; the no-arg run restores all 19 units so check_structure/check_content see them).
3. Translate to the FROZEN register (Chen's voice sheet + character voice sheets in HANDOFF). Consult glossary.json and authority.json BEFORE romanizing anything; REUSE the settled renderings (the Juntong; Dai Li / 老板 / 戴先生 "Mr. Dai" / 戴雨农 "Dai Yunong"; 汪精卫 Wang Jingwei / 汪逆 "the traitor Wang" / 汪某 "the man Wang"; 陈璧君 Chen Bijun; 制裁 "sanction" / 制裁令 "sanction order"; 王鲁翘 Wang Luqiao; 方炳西 Fang Bingxi; 毛万里 Mao Wanli; 郑修元 Zheng Xiuyuan; 上海区 "the Shanghai District"; 南京区 "the Nanjing District"; 上海滩 "the Shanghai Bund"; the B06-B12 shelves - the B12 shelf now includes the whole Shanghai/Chongqing/Japanese cast: Wang Zhaohuai, Wang Chiping, Zhou Weilong, Xu Zhongqi, Zhao Lijun, Pan Qiwu, Zhu Xiaogu, the Wang Tianmu daughters Kangzi/Yinzi; Inukai Ken/Tsuyoshi, Zhou Longxiang, Arita Hachirō, Nishio Toshizō, Satō Kenryō, Itagaki Seishirō, Chen Diaoyuan; the Provisional/Reformed Governments, the Central Training Corps, the Hokkō Maru; Jessfield Road/No. 76, Route Doumer, Yuyuan Road). Part Two PRINCIPALS: Chen(1), Dai Li(2), Wang Jingwei(3), Zheng Jiemin(4), Wang Tianmu(5), Fan Xing(6), Fang Bingxi(7), Wang Luqiao(8). Render Republican years literally per the Part-Two convention ("the twenty-eighth year"; the checker matches the source numeral). NEW cast likely to add: the "wave upon wave" of Shanghai/Nanjing sanction-team personnel and any officials in the "还都" farce (give pinyin fields; check authority.json/glossary for existing rows first).
   WATCH ch18/ch19's digitization glitches (list in PROGRESS.md, render to plain sense, footnote only real reading uncertainty): the same single-character-substitution classes as ch15/ch16/ch17 (先↔光, 卫→术, 鸣→呜, 汪→江, 文↔交, 声→望, 员→负, 凤→见, 板→扳, 从→徙, 该→孩, 众→家, 浓→渡, 簸→箥, 鸦→雅, 彻→澈). NUMBER-DENSE dates (the 30 March 1940 还都, casualty/roster figures): carry real counts as DIGITS / explicit words; NOISE only elided-tens / approximate / name-embedded / idiom forms - add a commented B13 block to data/noise.txt as needed (the elided-tens block is ordered LONGEST-FIRST; keep any new compound BEFORE the bare form it contains; fullwidth-zero years/pages 一九○○ / 二○X use ○ = U+25CB and must be noised with the value carried in English, cf. the B10/B11/B12 entries 二○三 / 二○九).
4. Checks (per unit): verify_unit.py ch18 and ch19 (parity + numbers with --noise auto-found + anchors); check_align.py ch18 / ch19; regenerate checks.json with scripts/batch_artifacts.py (no args) and run check_structure.py --config checks.json + check_content.py --config checks.json (NOTE: check_content prints KNOWN PRE-EXISTING artifacts and exits nonzero because of them - ch07 Zhanggu, ch08 Shunde, ch13 Miss Nguyen/Oya Kusuo/Yuan Haowen - diacritic/variant substring-match artifacts, NOT regressions; CONFIRM ch18/ch19 themselves show "all in the paired paragraph" / 0 displaced. Do NOT add book-TITLE glossary rows keyed on full hanzi, and do NOT add COMMON-NOUN keys - the B12 near-miss was 小巷子 "little lane", which cross-flagged ch06/07/13/15; a glossary key must be a distinctive proper noun that renders ONE way everywhere it appears). qc_entities.py on a reconstructed bilingual per unit (data/zh body lines + out/chNN_en.json, `> zh` / en pairs, strip the ### heading lines; every glossary row needs a pinyin field). Verify each unit's TAIL against the source (ch18's Part-Two close; ch19's 陈恭澍谨启七十二年五月 signature). check_register.py --ref reference/B01_frozen.md out/ch18_reading.md out/ch19_reading.md ("shall" in Chen's narration is deliberate; a quoted document may lift the ratio - read the note, do not de-formalize).
5. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (the full list is in PROGRESS.md - it now includes the B12 additions: 志舟 Zhizhou, No. 76 Jessfield Road, 长板坡 Changbanpo, 杜公馆/Du Yuesheng, the ROC 青天白日满地红旗 flag, 百梅 Baimei, the 戴雨农先生全集 and 沪滨三次历险实录 sources, the Qiantang bore; and the B11/B10 items). ch18/ch19 earn NEW notes only for first-appearance material (the 还都 "return of the capital", any new Hanoi-case martyrs, 传记文学 the journal); be generous but do NOT pad, consult the NOT-re-noted list first. Merge notes via apparatus_merge.py (numeric character references only in note bodies - keep them ASCII where possible; anchors verbatim ASCII substrings of the reading.md body text, NO em dash and NO quote character - substring traps; multi-occurrence anchors attach at first occurrence). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field; apparatus_merge's glossary path assumes a FLAT map and would corrupt the sectioned file - use it ONLY for notes). Confirm ch18/ch19 carry no images.
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; update HANDOFF.md; commit and push to claude/nameless-heroes. B13 COMPLETES Part Two - flag that in PROGRESS/HANDOFF (next is B14 = ch20, the Part Three Shanghai preface).

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B14 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
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
- **Part Two - "Disgrace at Hanoi" (河内辱命)** is NEARLY COMPLETE: B06 = Preface (ch10) +
  Chapter 1 (ch11); B07 = Ch2 (ch12); B08 = Ch3 (ch13); B09 = Ch4 (ch14); B10 = Ch5
  (ch15, the CLIMAX); B11 = Ch6 (ch16, the reckoning); B12 = Ch7 (ch17, the recall +
  Shanghai reassignment). The assassination FAILED; Chen has been recalled, reprimanded,
  and reassigned to Shanghai, where he has taken over the Shanghai District. Wang Luqiao
  is arrested; Wang Tianmu's loyalty is in doubt; the pursuit of Wang goes on.
- **NEXT: B13 = ch18 + ch19** - ch18 第八章 再接再励 前仆后继 "Renewed Effort, Wave upon
  Wave" (the successive martyrs, the 30 Mar 1940 Nanjing 还都 farce) + ch19 作者小启 "A Note
  from the Author" (the short notice CLOSING Part Two, signed May 1983). **B13 COMPLETES
  Part Two.** ~16,683 chars; ch18 has three (一)-(三) sub-headings ((一) standalone L3,
  (二)/(三) glued at L31/L86); ch19 has none (4 body <p>).

## What is NEXT

- Batch B13 = ch18 + ch19 (Part Two, Chapter 8 + the closing author's note). Kickoff is
  the paste-block at the top. Runs to completion (no gate); ends by pasting the B14
  kickoff. B14 = ch20 (the Part Three "Shanghai" preface).
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
