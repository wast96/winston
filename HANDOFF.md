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
Nameless Heroes B12

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once (its ONE failing regression test, "hook stands down on template stub", is a KNOWN false alarm; all others pass), then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05), B02 (ch06), B03 (ch07), B04 (ch08), B05 (ch09), B06 (ch10 preface + ch11), B07 (ch12), B08 (ch13), B09 (ch14), B10 (ch15) and B11 (ch16) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them.

Do Batch B12 = ch17 (ONE unit, ~17,446 source chars): 第七章 临深履薄 锲而不舍 "Chapter 7. Treading Thin Ice, Never Relenting" - the seventh chapter of PART TWO ("Disgrace at Hanoi"), FOLLOWING the reckoning-and-indictment chapter (ch16). Recalled to Chongqing, given a "punishment of the spirit," then reassigned to Shanghai, Chen presses on against Wang: the grinding pain of failure, the comrades left at Hanoi and their follow-up actions (INCLUDING a quoted letter Wang Jingwei wrote to 龙云 Long Yun - 「志舟先生主席勋鉴：…」, 志舟 being Long Yun's courtesy name), a three-point agreement (三点协议事项), and the renewed thousand-li pursuit of Wang. Read the tail of ch16 English (out/ch16_reading.md section (4): the "(End of Chapter Six)" coda + the four bridge paragraphs) and ch16 for register + story continuity: ch16 ended with Chen setting foot on the "Shanghai Bund" and Brother Wang Luqiao already arrested there. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch17 from data/src (18_index-split-000-0016.txt). drop=2 (running header 英雄无名-陈恭澍 from <title> + the <h2> chapter title; CONFIRM against data/src_epub/OEBPS/Text/index_split_000_0016.xhtml, which parses to 1 <h2> + 151 <p>). NO <br/>, NO images, NO set-off formatting (confirm). THREE numbered-in-parens sub-headings (一)-(三) like ch12/ch13/ch15/ch16: (一)失败之苦是非常折磨人的 [~L3]; (二)留在河内的同志们还有后续行动 [~L45]; (三)千里追踪奋勇杀敌的再出发 [~L108]. Grep each candidate p-by-p against data/src_epub to confirm STANDALONE vs GLUED (cf. ch08/ch16). A quoted letter to Long Yun (「志舟先生主席勋鉴：…」) and a 三点协议事项 enumerated list appear: keep quoted-document / roster / bullet lines as separate <p> and do NOT merge (cf. ch12/ch13/ch16). EXTRACTOR mid-phrase splits to MERGE (the tail lines L150 "…视我们为第一号目标" and L151 "…亦在直" run on, non-terminal; and others) - re-derive each exact body-line pair against the XHTML (last char not in 。！？」）…—). GREP the source for note markers (\[\d+\]) and record "none present" in PROGRESS.md (none through B11). NOTE: ch17 has NO in-text "(第N章完)" coda; its final paragraph forward-references a 后记 (postscript) that will account for the fates of the 十九个 Hanoi participants - a forward reference, not a cut.
2. Extend scripts/clean_batch.py with ch17's spec (drop=2; merges = the mid-phrase pairs, re-derived as body-line pairs; glued/standalone for the (一)-(三) headings per the p-by-p grep). Run it (source-conservation check). Write out/ch17_reading.md (## chapter title from book.json = "Chapter 7. Treading Thin Ice, Never Relenting"; ### for each (一)-(三) sub-heading; one English paragraph per source body line; the quoted Long Yun letter and the three-point agreement as normal paragraphs - do NOT use {p} verse). Then run scripts/batch_artifacts.py ch17, and ALWAYS finish with a NO-ARG run (the batch_artifacts.py trap: an ID-run writes checks.json with ONLY that unit; the no-arg run restores all 17 units so check_structure/check_content see them).
3. Translate to the FROZEN register (Chen's voice sheet + character voice sheets in HANDOFF). Consult glossary.json and authority.json BEFORE romanizing anything; REUSE the settled renderings (the Juntong; Dai Li / 老板 / 戴先生 "Mr. Dai" / 戴雨农 "Dai Yunong"; 汪精卫 Wang Jingwei / 汪逆 "the traitor Wang" / 汪某 "the man Wang"; 陈璧君 Chen Bijun; 制裁 "sanction" / 制裁令 "sanction order"; 王鲁翘 Wang Luqiao; 方炳西 Fang Bingxi; 魏春风 Wei Chunfeng; 阮小姐 Miss Nguyen; 龙云 Long Yun [courtesy 志舟 "Zhizhou"]; the Hanoi team; 上海滩 "the Shanghai Bund"; the B06-B11 shelves). Part Two PRINCIPALS: Chen(1), Dai Li(2), Wang Jingwei(3), Zheng Jiemin(4), Wang Tianmu(5), Fan Xing(6), Fang Bingxi(7), Wang Luqiao(8). Render Republican years literally per the Part-Two convention ("the twenty-eighth year"; the checker matches the source numeral). NEW cast likely to add: Shanghai-station / Hanoi-follow-up personnel and any officials in the quoted letter (give pinyin fields; check authority.json/glossary for existing rows first). 
   WATCH ch17's digitization glitches (list in PROGRESS.md, render to plain sense, footnote only real reading uncertainty): the same single-character-substitution classes as ch15/ch16 (先↔光, 卫→术, 鸣→呜, 汪→江, 文↔交, 声→聋, 其→共, 间→问, 便→遍, 是→走/遍, 这→违, 随→隧, 春→舂, 看↔着, 木→本, 澈→彻). NUMBER-DENSE letter/agreement (dates, the 三点 agreement, the 十九个 participants): carry real counts as DIGITS / explicit words; NOISE only elided-tens / approximate forms - add a commented B12 block to data/noise.txt as needed (the elided-tens block is ordered LONGEST-FIRST; keep any new compound BEFORE the bare form it contains).
4. Checks (per unit): verify_unit.py ch17 (parity + numbers with --noise auto-found + anchors); check_align.py ch17; regenerate checks.json with scripts/batch_artifacts.py (no args) and run check_structure.py --config checks.json + check_content.py --config checks.json (NOTE: check_content prints KNOWN PRE-EXISTING artifacts and exits nonzero because of them - ch07 Zhanggu, ch08 Shunde, ch13 Miss Nguyen/Oya Kusuo/Yuan Haowen - diacritic/variant substring-match artifacts, NOT regressions; CONFIRM ch17 itself shows "all in the paired paragraph" / 0 displaced, and do NOT add book-TITLE glossary rows keyed on full hanzi); qc_entities.py on a reconstructed bilingual (data/zh body lines + out/ch17_en.json, `> zh` / en pairs, strip the ### heading lines; every glossary row needs a pinyin field); verify the TAIL against the source (the 后记 forward-reference and 十九个 participants). check_register.py --ref reference/B01_frozen.md out/ch17_reading.md ("shall" in Chen's narration is deliberate; a quoted letter may lift the ratio - read the note, do not de-formalize).
5. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (the full list is in PROGRESS.md - it now includes the B11 additions: the chapter-title diary source, Yue Fei / twelve gold tablets, Wang's 引刀成一快 poem, Munich/Sudetenland/Hácha, 梁孟, the 卫/-wei pun, 甲午/庚子, the 1935 Chahar affair; and the B10 items). This chapter earns NEW notes only for its first-appearance material; be generous but do NOT pad, consult the NOT-re-noted list first. Merge notes via apparatus_merge.py (numeric character references only in note bodies - keep them ASCII where possible; anchors verbatim ASCII substrings of the reading.md body text, NO em dash and NO quote character - substring traps; multi-occurrence anchors attach at first occurrence). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field; apparatus_merge's glossary path assumes a FLAT map and would corrupt the sectioned file - use it ONLY for notes). Confirm ch17 carries no images.
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; update HANDOFF.md; commit and push to claude/nameless-heroes.

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B13 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
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
  killing Zeng Zhongming by mistake, and the documentary section (五). 225 body
  paragraphs; 11 notes. **Name trap RESOLVED: 郑邦国 -> 陈邦国 "Chen Bangguo".**
- **Batch B11 (ch16), Part Two Chapter 6.** 第六章 奸伪卑劣 寿张为幻 "Vile Treachery,
  Illusions Undone" - the reckoning-and-indictment chapter closing Part Two: Chen owns
  the failure and escapes to Chongqing, then quotes IN FULL and rebuts Wang's eulogy
  「曾仲鸣先生行状」 (6 Apr 1939) and his apologia 「举一个例」 (9 Apr 1939, enclosing the
  doctored 国防最高会议第五十四次 record with its attendee roster), and copies out Chiang's
  17 Apr press conference and Wu Jingheng's 9,000-word essay 「对汪精卫「举一个例」的进一解」.
  116 body paragraphs; **8 notes (193 cumulative)**; **34 glossary rows**. All checks
  green; qa_epub PASS; epubcheck 0/0/0/0. EPUB now **16/43 chapters**. Detail in
  PROGRESS.md ("Batch B11").

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` - derives data/zh/<id>.txt verbatim from data/src,
  applying per-unit drops/merges/heading-splits with a source-conservation check.
  Specs for ch01-ch16. Merge logic FOLLOWS CHAINS (a `<p>` split into 3+ fragments is
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
  glossary rows keyed on the full hanzi title (they cross-flag other chapters that
  render the same title slightly differently - this bit B10; quoted books are handled
  by FOOTNOTES, not glossary rows).
- **Verse marker `{p}`** (first used in ch13): prefix a pure-verse body line with
  `{p} ` and the builder renders `<p class="verse">`; the checks strip it. ch15/ch16
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
- data/noise.txt carries the B01-B11 project noise rules (each with a comment line).
  Republican years are rendered literally in Part Two ("the twenty-eighth year"); the
  checker matches the source numeral directly. **The elided-tens block is ordered
  LONGEST-FIRST:** a compound like 四、五百 MUST precede the bare 四、五. Fullwidth-zero
  years/refs (一九○五 / 二○三, ○ = U+25CB) AND Latin-O forms (二 O 五 = page 205) must be
  noised - the checker cannot compose them - and the value carried in the English.
  Number-garbles (四万百五千百 = 450 million, 六十万百 = ~600 million, 九十六百一十五 = 9,615)
  are noised and the plain-sense value carried in the English.
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
  Shanghai Bund".
- **B03-B10 shelves (reuse; in glossary.json):** the Juntong internal units,
  Tianjin/Beiping/Hong Kong/Hanoi geography, the Mauser "box-cannon", the Green Gang,
  the Kwantung Army, Manchukuo, the "Yan Telegram", the Three Principles of the People,
  Konoe's "New Order in East Asia", 支那 = "Shina", the Kōain, the Tanaka Memorial;
  people: Cen Jiazhuo, Yu Lexing, Zhou Fohai, Chen Gongbo, Gao Zongwu, Mei Siping,
  Kagesa, Konoe, Long Yun, Zeng Zhongming; Hanoi: 徐先生 "Mr. Xu", 魏春风 Wei Chunfeng,
  阮小姐 Miss Nguyen, 高朗街 "Gao Lang Street" (Rue Colombert No. 27), Haiphong; the B10
  additions (Chen Bangguo, Tang Yingjie, Yu Jiansheng, the Zeng household, Hiranuma,
  Wu Jingheng, Jin Xiongbai / Zhu Zijia, Fang Junbi). Books handled by FOOTNOTE (ch15):
  蒋总统秘录, 戴雨农先生传, 汪政权的开场与收场.
- **B11 shelf (ch16; reuse; in glossary.json, all with pinyin).** National Defense
  Council roster & officials: 于右任 Yu Youren, 居正 Ju Zheng, 孔祥熙 Kong Xiangxi (H. H.
  Kung), 翁文灏 Weng Wenhao, 邵力子 Shao Lizi, 陈立夫 Chen Lifu, 陈果夫 Chen Guofu, 董显光
  Dong Xianguang, 张群 Zhang Qun, 徐堪 Xu Kan, 徐谟 Xu Mo, 顾祝同 Gu Zhutong (Mo-san), 白崇禧
  Bai Chongxi (Jiansheng), 唐生智 Tang Shengzhi (Meng-xiao), 徐永昌 Xu Yongchang (Ci-chen;
  source 次展/次辰 = misprint for 次宸), 陶德曼 Trautmann, 川樾 Kawagoe. Traitor/puppet
  archetypes: 秦桧 Qin Hui, 李完用 Yi Wan-yong, 吴三桂 Wu Sangui, 溥仪 Puyi, 哈柴 Hácha, 张伯伦
  Chamberlain, 苏锡文 Su Xiwen, 梁鸿志 Liang Hongzhi. Elders: 李石曾 Li Shizeng, 张溥泉 Zhang
  Puquan (= Zhang Ji). 行状 revolutionaries: 方君瑛 Fang Junying, 黎仲实 Li Zhongshi, 俞云纪
  Yu Yunji. Hanoi: 丹娜 Dana (métisse cover-driver), and the three captured (cover names):
  袁伯勋 Yuan Boxun, 孙亚东 Sun Yadong, 杨卫河 Yang Weihe. Western contemporaries (Hitler,
  Mussolini, Lenin, Stalin, Trotsky) rendered directly, NOT glossary'd.

## ⚠ Name trap RESOLVED (do not reopen): 陈邦国 / 郑邦国

The Hanoi action-team member the source spells 郑邦国 in ch13 (B08) and 陈邦国 in ch15
(B10) + ch16 (B11) plus the quoted Biography of Dai Yunong (陈). This is ONE man (one of
the three captured). RESOLVED to **Chen Bangguo (陈邦国)**: glossary key renamed; the BUILT
ch13 unit updated; the discrepancy footnoted at the first ch15 occurrence. Romanization
stays `provisional`. Use Chen Bangguo consistently in all remaining batches.

## Voice sheet - CHEN GONGSHU (author / narrator)

- REGISTER: educated, formal, essayistic first person; grave and a touch archaic but
  not stilted. Long semicolon-joined clauses; four-character idiom and classical
  allusion used freely and footnoted when they carry weight. Refers to himself as
  笔者 "the writer" and 我 "I". His narrating "shall" is DELIBERATE - do not
  de-formalize it; check_register flags it informationally (B06 33%, B08 29%, B10 9%,
  B11 0%, verified deliberate).
- STANCE: self-justifying yet self-effacing; insists on truthfulness, admits his
  blunders; tender toward dead comrades, bitter and scornful toward the enemy. In ch16
  the stance was a cold documentary indictment: he quoted Wang's own 行状 eulogy and
  举一个例 apologia AT LENGTH and rebutted them, keeping the quoted-Wang register (formal,
  literary, self-pitying) DISTINCT from Chen's own dry scorn, and Wu Jingheng's essay
  DISTINCT again (sardonic, mocking, vigorous classical-vernacular). Keep those three
  registers apart when quoted material recurs.
- Ratio ~4.55-4.76 en/han in narrative; prefaces denser (~5.2); document-/essay-heavy
  chapters run higher (ch12 4.84, ch13 4.79, ch15 4.60, ch16 4.78). A quoted letter in
  ch17 may lift it; read the note, do not reset.

## Voice sheets - principal & recurring cast

- **DAI LI (戴雨农 / Mr. Dai / 老板 "the Boss").** Recalled Chen to Chongqing; at ch16's
  end, in a "letting bygones be bygones" spirit, gave Chen the new Shanghai task over a
  banquet. Warm off duty, abrupt on business.
- **WANG LUQIAO (王鲁翘 / Luqiao).** Part Two principal (cast 8). The trigger-man who shot
  Zeng in error; bluff, bold, loyal ("没关系，咱们再干！"). By ch16's end already transferred
  to Shanghai and ARRESTED there (his Hanoi capture "left for later telling").
- **FANG BINGXI (方炳西 / Brother Bingxi).** Part Two principal (cast 7). The advance man /
  cipher-holder; in ch16 took charge of winding up Hanoi after Chen's recall. Survives.
- **YU LEXING (余乐醒 / Brother Lexing / Dr. Yu).** France-trained chemist, chief of staff;
  brooding, thin-skinned. NOTE the split: 余乐醒 = "Brother Yu Lexing"; 乐醒兄 = "Brother
  Lexing". Off-stage after ch16 (Bingxi to arrange the Hanoi comrades' dispositions).
- **CEN JIAZHUO / MR. XU / WEI CHUNFENG / TANG YINGJIE / CHEN BUYUN / CHEN BANGGUO / YU
  JIANSHENG.** Hanoi cast; see the B08/B10 shelf and glossary. Wei Chunfeng and the
  métisse Dana saw Chen safely out to Haiphong (ch16). Chen never saw Tang Yingjie or
  Chen Buyun again after Hanoi.
- **ZHENG JIEMIN / WANG TIANMU / FAN XING.** Part Two principals (4, 5, 6), off-stage in
  B06-B11; render straight when they recur (Wang Tianmu's loyalty is tested later).
- **Dead comrades carried in memory:** ZENG CHE 曾澈, WANG WEN 王文 (ch11); and ZENG
  ZHONGMING 曾仲鸣, killed at Hanoi in Wang's place (ch15), whose eulogy Wang wrote and
  Chen rebutted (ch16).

## Where the book stands

- Part One (北国锄奸) is COMPLETE (B01-B05).
- **Part Two - "Disgrace at Hanoi" (河内辱命)** is UNDERWAY: B06 = Preface (ch10) +
  Chapter 1 (ch11); B07 = Ch2 (ch12); B08 = Ch3 (ch13); B09 = Ch4 (ch14); B10 = Ch5
  (ch15, the CLIMAX); B11 = Ch6 (ch16, the reckoning/indictment). The assassination
  FAILED; Chen has been recalled, reprimanded ("punishment of the spirit"), and
  reassigned to SHANGHAI to continue sanctioning Wang. Wang Luqiao is already arrested
  there.
- **NEXT: B12 = ch17** 第七章 临深履薄 锲而不舍 "Treading Thin Ice, Never Relenting" -
  Chen presses on: the pain of failure, the comrades still at Hanoi and their follow-up
  actions (a quoted Wang letter to Long Yun), a three-point agreement, the renewed
  pursuit. ~17,446 chars, three (一)-(三) sub-headings, NO in-text 完 coda.

## What is NEXT

- Batch B12 = ch17 (Part Two, Chapter 7). Kickoff is the paste-block at the top. Runs
  to completion (no gate); ends by pasting the B13 kickoff.
- The frozen register reference is `reference/B01_frozen.md`. Narrative sits at
  4.55-4.76 en/han; document-/essay-heavy chapters run higher; a quoted letter in ch17
  may lift it. Read the note, do not reset.
- Sub-heading pattern DIFFERS by chapter. Styles seen: Part One numbered 一/二/三;
  ch11/ch14 COUPLET-STYLE with NO number prefix; ch12/ch13/ch15/ch16/ch17
  numbered-in-parens (一)/(二)…; ch08/ch16 have a GLUED sub-heading (on a paragraph tail);
  ch13's inner enumerated list 一、-六、 rendered `####`. Grep each new chapter p-by-p.
- WATCH for source anomalies: cuts, misplaced-「 glitches, corrupt/dropped-character
  phrases, terminal-」 name-splits, the in-text "(第N章完)" coda pattern (ch12/ch13/ch16;
  ch17 has none), fullwidth-zero (U+25CB) and Latin-O number forms, and pervasive
  single-character substitutions. Re-grep each batch's source for `\[\d+\]` note markers
  (none present through B11).

## Open items for the read-through / completion

- Feed decided renderings back to authority.json on completion: 军统 "the Juntong"; the
  full B02-B11 historical-name set (Part One; the B06-B07 Japanese/negotiator/elder
  names; the B08 Wang-essay set; the B10 additions; the B11 additions - the National
  Defense Council roster, the traitor/puppet archetypes, the elders and 行状
  revolutionaries).
- Japanese name readings to verify when the men recur (多田骏, 田代皖一郎, 土肥原贤二,
  坂垣征四郎, 近卫文麿, 影佐祯昭, 今井武夫, 晴气庆胤, 伊藤芳男; 大屋久寿雄 "Ōya Kusuo";
  平沼骐一郎 "Hiranuma Kiichirō"; 川樾 "Kawagoe" - added B11).
- Identify 剑秋 "Jianqiu" (a 1932 Nanjing "elder brother" of Chen) when sources allow.
- Stray source glyphs: 寿张为幻 in the ch16 title was flagged and footnoted (rendered by
  sense "Illusions Undone"; source uncertainty noted). Still to resolve in later
  batches: trailing 杀 on the ch22 title; 毛酋 in a ch36 section title.
- Provisional romanizations to firm up when sources allow (glossary `provisional` rows,
  incl. the B10/B11 additions: Tang Yingjie, Yu Jiansheng, Chen Bangguo, the Zeng
  household; Su Xiwen, Dana, the three captured (Yuan Boxun/Sun Yadong/Yang Weihe),
  Li Zhongshi, Yu Yunji).

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01-B11 builds (0/0/0/0). Source is a clean
  digital EPUB, predominantly simplified with residual variant glyphs and pervasive
  digitization glitches (list them, render to plain sense, do not footnote mechanical
  typos). B01-B11 glitch lists are in PROGRESS.md.
- Running-header line 英雄无名-陈恭澍 (from the `<title>`) opens all 43 content files: drop
  it. drop count is variable - most drop=2; ch01 and ch10 drop=3.
- Enumerated ；/：/、 bullet lists, quoted-document/roster lines, and verse lines in the
  source are DELIBERATE separate `<p>` - do NOT merge them; only genuine mid-phrase
  splits (last char not terminal, OR a source `<p>` boundary that severs one sentence)
  merge, and those can CHAIN across 3+ fragments. ALWAYS confirm the extracted body
  count p-by-p against data/src_epub.
- Faithful numbering gaps/anomalies (NOT errors): Part Three skips ch7, splits ch10 into
  (上)/(下); 三面受敌 一往无前 titles two different chapters (ch14 and ch24); ch09 printed
  §五 before §四; ch13 restarts its (一)-(五) numbering for the appended essay; ch16
  reproduces two whole Wang documents + a doctored meeting record. Preserve and, where a
  reader would stumble, footnote.
- Expect a stray per-task branch at the top of every batch; consolidate onto
  claude/nameless-heroes per rule 2.
