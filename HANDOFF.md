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
Nameless Heroes B15

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once (its ONE failing regression test, "hook stands down on template stub", is a KNOWN false alarm; all others pass), then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05), B02 (ch06), B03 (ch07), B04 (ch08), B05 (ch09), B06 (ch10 preface + ch11), B07 (ch12), B08 (ch13), B09 (ch14), B10 (ch15), B11 (ch16), B12 (ch17), B13 (ch18 + ch19) and B14 (ch20) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them. PART TWO ("Disgrace at Hanoi") is COMPLETE; PART THREE ("Renown Won in a Hundred Battles" / 百战声威) has OPENED with its self-preface (ch20). The EPUB now holds 20/43 chapters, 210 notes.

Do Batch B15 = ch21 (ONE unit, ~21,426 source chars - the FIRST Shanghai chapter and much longer than the ch20 preface): ch21 = 第一章 十里洋场重振雄威 "Chapter 1. Back in Shanghai, Our Might Restored" - Chen, newly appointed District Chief (Aug 1939), restores the shattered Shanghai District's machinery. Read the tail of ch20 English (out/ch20_reading.md: the compressed preview of exactly this - the Aug-1939 arrival, the appointment telegram, the half-stalled District, acting chief "Mr. Zhao", secretary Zheng Xiuyuan, and the Chen Dirong betrayal that had the enemy search fourteen offices) and ch18/ch19 for register + story continuity. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch21 from data/src (22_index-split-000-0020.txt). CONFIRM structure against data/src_epub/OEBPS/Text/index_split_000_0020.xhtml [parses to 1 <h2> 第一章 十里洋场重振雄威 + 162 <p>, NO <h1>, NO <br/>, NO <img>]. drop=2 (running header 英雄无名-陈恭澍 + <h2> chapter title). The txt has 163 lines (L1 header + L2 <h2> + 161 body lines) vs 162 <p>, so ~1 extractor mid-phrase split (or a sub-heading to place) to resolve p-by-p - GREP p-by-p against the source XHTML and DERIVE the merges (last char not in 。！？」）…—), the glued {} and the standalone []. Sub-headings here are COUPLET-STYLE with NO number prefix (cf. ch11/ch14/the chapter title itself); a first pass found NO (一)-style numbered parens - confirm p-by-p; L3 死无对证永成悬疑的一桩大反... looks like the opening couplet sub-heading. WATCH the SERIALIZATION CODA: the chapter carries "(第一章完下期续载)" ("End of Chapter 1, continued next issue") GLUED to the tail near L157, with further <p> (L158-L163) AFTER it - a magazine-installment seam faithfully reproduced; resolve p-by-p and preserve it (cf. the (第N章完) coda in ch12/ch13/ch16, but here with 下期续载 and trailing content). GREP the source for note markers (\[\d+\]) and record "none present" (none through B14).
2. Extend scripts/clean_batch.py with ch21's spec (drop=2; merges/glued/standalone as derived). Keep quoted-title / enumerated (；/：/、) / roster / salutation lines as SEPARATE <p> and do NOT merge (cf. ch12/ch13/ch16/ch17/ch18). Run it (source-conservation check). Write out/ch21_reading.md (## chapter title from book.json = "Back in Shanghai, Our Might Restored"; one English paragraph per source body line; couplet sub-headings as ### ; any inner enumerated list #### per ch13 precedent). Then run scripts/batch_artifacts.py ch21, and ALWAYS finish with a NO-ARG run (the batch_artifacts.py trap: an ID-run writes checks.json with ONLY that unit; the no-arg run restores all 21 units so check_structure/check_content see them).
3. Translate to the FROZEN register (Chen's voice sheet in HANDOFF; narrative runs ~4.55-4.78 en/han - a Shanghai action chapter, not a preface). Consult glossary.json and authority.json BEFORE romanizing anything; REUSE the settled renderings: the Juntong; 上海区 "the Shanghai District"; 区长 "District Chief"; 军事委员会调查统计局 "Bureau of Investigation and Statistics of the Military Affairs Commission"; Dai Li / 戴雨农 "Dai Yunong" / 老板 "the Boss"; 汪精卫 Wang Jingwei / 汪逆 "the traitor Wang" / 汪伪 "Wang puppets"; 敌伪 "the enemy and the puppets"; 制裁 "sanction"; 蓝衣社 "the Blue Shirt Society" (NOTED ch08, do NOT re-note); 沦陷区 "the fallen zone"; 日寇 "Japanese invaders"; 十里洋场 the chapter-title epithet for Shanghai "the ten-mile foreign concession/Bund". Part Three PRINCIPALS: this is where the Shanghai cast is BUILT - the ch20 preview names 郑修元 Zheng Xiuyuan (District secretary, glossary), 陈第容 Chen Dirong (the traitor-secretary, glossary), 黄志远 Huang Zhiyuan (glossary), and "a Mr. Zhao" (赵君, the acting chief - NOT yet glossary-keyed; if ch21 gives his full name, add it then). Give pinyin fields for EVERY name and check authority.json/glossary first. Render Republican years literally ("the twenty-eighth year"; the checker matches the source numeral).
   WATCH ch21's digitization glitches (list in PROGRESS.md, render to plain sense, footnote only real reading uncertainty): the same single-character-substitution / homophone classes seen ch15-ch20 (先↔光, 卫→术, 汪→江/江→汪, 文↔交, 员→负, 板→扳, 从→徙, 该→孩, 困→因, 科→料, 综→踪, 局→昂, 为→伪, 买→真, 处→书, 问→间, 捉→提, etc.). Dates/counts: carry real values as DIGITS / explicit words; NOISE only elided-tens / approximate / name-embedded / idiom forms - add a commented B15 block to data/noise.txt if needed (the elided-tens block is ordered LONGEST-FIRST; keep any new compound BEFORE the bare form it contains; a project noise entry can be PRE-EMPTED by an earlier substring rule).
4. Checks: verify_unit.py ch21 (parity + numbers with --noise auto-found + anchors); check_align.py ch21; regenerate checks.json with scripts/batch_artifacts.py (no args) and run check_structure.py --config checks.json + check_content.py --config checks.json (NOTE: check_content prints KNOWN PRE-EXISTING artifacts and exits nonzero because of them - ch07 Zhanggu ×1, ch08 Shunde ×3, ch13 Miss Nguyen/Oya Kusuo/Yuan Haowen ×9 - diacritic/variant substring-match artifacts, NOT regressions; CONFIRM ch21 itself shows "all in the paired paragraph" / 0 displaced. Do NOT add book-TITLE glossary rows keyed on full hanzi, and do NOT add COMMON-NOUN keys - a glossary key must be a distinctive proper noun that renders ONE way everywhere, and must not occur in another chapter with a different rendering). qc_entities.py on a reconstructed bilingual (data/zh body lines + out/ch21_en.json, `> zh` / en pairs, strip the ### heading lines; every glossary row needs a pinyin field - and align any common-noun term to its glossary-decided rendering, e.g. 督察 "inspector", the B14 near-miss). Verify the TAIL against the source (rule 4 corollary - critical on a 21k-char single-pass unit; the tail near the (第一章完) coda especially). check_register.py --ref reference/B01_frozen.md out/ch21_reading.md ("shall" in Chen's narration is deliberate - read the note, do not de-formalize).
5. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (the full list is in PROGRESS.md). A Shanghai action chapter earns notes for NEW Shanghai places / institutions / persons / customs the reader would miss; 十里洋场, the Concessions, the Juntong, 制裁, the Republican-calendar convention, 蓝衣社 are all covered - do NOT re-note. Be generous but do NOT pad. Merge notes via apparatus_merge.py (numeric character references only in note bodies - keep them ASCII where possible; anchors verbatim ASCII substrings of the reading.md body text, NO em dash and NO quote character - substring traps; multi-occurrence anchors attach at first occurrence). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field; apparatus_merge's glossary path assumes a FLAT map and would corrupt the sectioned file - use it ONLY for notes). Confirm whether ch21 carries images (a first pass found NONE - confirm).
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; update HANDOFF.md; commit and push to claude/nameless-heroes. (next is B16 = ch22, the second Shanghai chapter - note the stray 杀 on the ch22 title flagged in the open-items list.)

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B16 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
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
  Illusions Undone" - the reckoning/indictment chapter. 116 paragraphs; 8 notes; 34 rows.
- **Batch B12 (ch17), Part Two Chapter 7.** 第七章 临深履薄 锲而不舍 "Treading Thin Ice,
  Never Relenting" - recall to Chongqing, then Shanghai reassignment; quotes Wang's 30 Mar
  1939 letter to Long Yun, Kagesa's memoir, 蒋总统秘录. 147 body paragraphs; 9 notes; 49 rows.
- **Batch B13 (ch18 + ch19), Part Two Chapter 8 + the closing Author's Note. PART TWO
  COMPLETE.** ch18 = 第八章 再接再励前仆后继 "Chapter 8. Renewed Effort, Wave upon Wave" -
  takes over the Shanghai District (12 Aug 1939), the 30 Mar 1940 "还都" farce, the "wave
  upon wave" of martyrs, and the accounting of all NINETEEN Hanoi participants. ch19 =
  「英雄无名」作者小启 "A Note from the Author" (signed May 1983). 138 + 4 body paragraphs;
  6 notes (208 cumulative); 21 glossary rows.
- **Batch B14 (ch20), PART THREE OPENS.** ch20 = 「上海抗日敌后行动」自序 "Author's Preface:
  Shanghai Behind-the-Lines Operations Against Japan" - the self-preface opening Part Three
  ("Renown Won in a Hundred Battles" / 百战声威). Chen recounts the title's evolution, sets
  the Aug-1939-Oct-1941 scope, and gives a compressed portrait of the Shanghai District
  (its ~1,000-strong order of battle, the two-year tally: 200+ own casualties, 100+ traitors
  sanctioned, ~40 Japanese officers killed, the enemy's Nov-1941 press exposé), previewing
  ch21. 26 body paragraphs; **2 notes (210 cumulative); 2 glossary rows.** drop=3 (cf. ch10:
  header + <h1>百战声威 Part banner + <h3> preface title); 26 <p> map 1:1, NO merges. All
  checks green; qa_epub PASS; epubcheck 0/0/0/0. **EPUB now 20/43 chapters.** Detail in
  PROGRESS.md ("Batch B14").

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` - derives data/zh/<id>.txt verbatim from data/src,
  applying per-unit drops/merges/heading-splits with a source-conservation check.
  Specs for ch01-ch20. Merge logic FOLLOWS CHAINS (a `<p>` split into 3+ fragments is
  rejoined whole). **drop is variable:** most chapters drop=2; ch01/ch10/ch20 drop=3.
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
  glossary rows keyed on the full hanzi title, and do NOT add COMMON-NOUN keys: a
  glossary key must be a DISTINCTIVE proper noun that renders ONE way everywhere.
- **Verse marker `{p}`** (first used in ch13): prefix a pure-verse body line with
  `{p} ` and the builder renders `<p class="verse">`; the checks strip it.
- Glossary is authored/merged BY HAND into the SECTIONED file
  (book/people/organizations/places/terms), idempotent + re-read-verified. **Every row
  MUST carry a `pinyin` field** - `qc_entities.py` does `rec["pinyin"]` and KeyErrors
  otherwise. apparatus_merge's glossary path assumes a FLAT map and would corrupt the
  sectioned file; NOTES still go through apparatus_merge.py.
- **qc_entities catches term-rendering drift too:** a glossary common-noun term rendered
  a different way in the batch flags as a "miss" (the B14 fix: 督察 rendered "supervisor"
  -> corrected to the glossary-decided "inspector"). Align the English to the glossary,
  or the term is not really settled.
- **Note-anchor gotchas:** American-style punctuation puts the period INSIDE the
  closing quote (anchor on an interior phrase). The reading.md uses STRAIGHT
  quotes/apostrophes AND U+2014 em dashes freely; keep anchors ASCII, WITHOUT any
  quote character AND without an em dash (either is a substring trap). Multi-occurrence
  anchors attach at the FIRST occurrence; check_structure reports "attach at first of several".
- data/noise.txt carries the B01-B14 project noise rules (each with a comment line).
  Republican years are rendered literally ("the twenty-eighth year"); the checker
  matches the source numeral directly. **The elided-tens block is ordered LONGEST-FIRST:**
  a compound like 四、五百 MUST precede the bare 四、五. Fullwidth-zero years/refs
  (一九○五 / 二○三 / 二○九, ○ = U+25CB) AND Latin-O forms (二 O 五 = page 205) must be
  noised - the checker cannot compose them - and the value carried in the English.
  Number-garbles are noised and the plain-sense value carried. Name/idiom-embedded
  numerals are noised too. B14 added 百数十 (hundred-odd), 十余 (ten-odd), 528 (the 随着 glitch).
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches it; re-run
  per session). setup.sh's ONE failing regression test ("hook stands down on template
  stub") is a KNOWN false alarm; all other regression tests pass.

## Renderings settled / carry-forward

- 军统 / 军统局 -> "the Juntong" (DECIDED). 戴笠 Dai Li (courtesy Yunong; 老板 "the Boss";
  戴先生 "Mr. Dai"; 戴雨农 "Dai Yunong"); 汪精卫 Wang Jingwei (原名 汪兆铭 "Wang Zhaoming";
  汪逆 "the traitor Wang"; 汪某 "the man Wang"; 汪氏 "Wang"); 陈璧君 Chen Bijun / 汪夫人
  "Madame Wang". 制裁 "sanction"; 制裁令 "sanction order". 敌伪 "the enemy and the puppets"
  / "enemy-and-puppet"; 汪伪 "Wang puppets"; 沦陷区 "the fallen zone"; 日寇 "Japanese
  invaders"; 区长 "District Chief"; 督察 "inspector". Chiang's titles: 校长 "the Commandant",
  领袖 "the Leader", 委员长 "the Generalissimo", 蒋公 "the Generalissimo, Mr. Chiang", 总裁
  "the Director-General" (Wang = 副总裁 "Vice-Director-General"). 总理 = "the Party Leader" /
  国父 = "the Father of the Nation" = Sun Yat-sen. Floors: 二楼/三楼 = "second/third floor".
  Republican years literal. 上海滩 "the Shanghai Bund". 高朗街 "Gao Lang Street" (NOT
  "Rue Colombert"). 北平站/天津站 "Beiping Station"/"Tianjin Station".
- **Book / part titles (in-text renderings, DECIDED; reuse verbatim):** 英雄无名 =
  "Nameless Heroes" (NOT "Heroes Without a Name"); Part One 北国锄奸 = "Rooting Out
  Traitors in the North"; Part Two = "Disgrace at Hanoi" (Chen's own in-text name for
  it is 河内汪案始末 "The Whole Story of the Wang Case at Hanoi"); Part Three 百战声威 =
  "Renown Won in a Hundred Battles"; 卷头长白 = "Prefatory Candour"; 军事委员会调查统计局
  = "Bureau of Investigation and Statistics of the Military Affairs Commission". 传记文学 =
  "Biographical Literature"; 新一组 = "New Group One"; 蓝衣社 = "the Blue Shirt Society"
  (NOTED ch08 - do NOT re-note). B14: the Part-Three title's Chinese evolution (百战声威 →
  抗战期间上海敌后行动 → 上海敌后行动 → 上海抗日敌后行动) is rendered in ch20's second paragraph.
- **B03-B13 shelves (reuse; in glossary.json):** the Juntong internal units,
  Tianjin/Beiping/Hong Kong/Hanoi/Shanghai geography, the Mauser "box-cannon", the Green
  Gang, the Kwantung Army, Manchukuo, the "Yan Telegram", the Three Principles of the
  People, Konoe's "New Order in East Asia", 支那 = "Shina", the Kōain, the Tanaka Memorial;
  the Part-Two Hanoi/Chongqing/Japanese casts; the B13 Wang-case martyrs (Chen Sancai,
  Huang Yiguang, Dai Jingyuan, Shao Mingxian, Wu Gengshu) and 极司非而路/极司菲尔路 "Jessfield
  Road". Books handled by FOOTNOTE (not glossary): 蒋总统秘录, 戴雨农先生传, 戴雨农先生全集,
  汪政权的开场与收场, 沪滨三次历险实录.
- **B14 shelf (ch20; reuse; in glossary.json, all with pinyin):** 陈第容 Chen Dirong (the
  assistant secretary who leaked, provisional), 黄志远 Huang Zhiyuan (the comrade who kept
  the newspaper sheets, provisional). REUSED: 郑修元 Zheng Xiuyuan (District secretary).
  赵君 "a Mr. Zhao" (acting chief) rendered inline, NOT glossary-keyed (surname only; firm
  up in B15 if ch21 names him). NEW notes: Yama / the 勾魂簿 soul-register; the 新申报 /
  中华日报 occupation papers.

## ⚠ Name trap RESOLVED (do not reopen): 陈邦国 / 郑邦国

The Hanoi action-team member the source spells 郑邦国 in ch13 (B08) and 陈邦国 in ch15
(B10) + ch16 (B11) + ch17 (B12). This is ONE man. RESOLVED to **Chen Bangguo (陈邦国)**:
glossary key renamed; the BUILT ch13 unit updated; the discrepancy footnoted at the first
ch15 occurrence. Romanization stays `provisional`. Use Chen Bangguo consistently.

## Voice sheet - CHEN GONGSHU (author / narrator)

- REGISTER: educated, formal, essayistic first person; grave and a touch archaic but
  not stilted. Long semicolon-joined clauses; four-character idiom and classical
  allusion used freely and footnoted when they carry weight. Refers to himself as
  笔者 "the writer" and 我 "I". His narrating "shall" is DELIBERATE - do not
  de-formalize it; check_register flags it informationally (B06 33%, B08 29%, B10 9%,
  B11 0%, B12 43%, B14 0%, verified deliberate - a preface with no dialogue and no
  narrating "shall" reads 0%, as ch20 did).
- STANCE: self-justifying yet self-effacing; insists on truthfulness, admits his
  blunders; tender toward dead comrades, bitter and scornful toward the enemy. When
  quoting hostile/puppet documents, keep the quoted register DISTINCT from Chen's own
  dry scorn.
- Ratio ~4.55-4.78 en/han in narrative; prefaces denser (~5.2, and ch20 measured 5.31);
  document-/essay-heavy chapters run higher. A chapter thick with quoted documents lifts
  it; read the note, do not reset. A Shanghai action chapter (B15+) should sit back in
  the 4.55-4.78 narrative band.

## Voice sheets - principal & recurring cast

- **DAI LI (戴雨农 / Mr. Dai / 老板 "the Boss").** After ch17 he and Chen meet no more,
  only letters and telegrams. Warm off duty, abrupt on business.
- **MAO RENFENG (毛人凤 / Mr. Mao)** ran the Chongqing HQ; younger brother 毛万里 Mao Wanli
  ran the Shanghai region as inspector-general.
- **WANG LUQIAO (王鲁翘 / Luqiao).** The trigger-man who shot Zeng in error; ARRESTED
  14 July 1939, shipped back to Hanoi, sentenced to life; freed after the war.
- **FANG BINGXI (方炳西 / Brother Bingxi).** Advance man / cipher-holder; wound up Hanoi
  after Chen's recall. Survives.
- **WANG TIANMU (王天木).** Former Shanghai District chief; loyalty in doubt by ch17 (Dai
  sends Chen partly to recover him). Daughters Kangzi (蝉红) and Yinzi (蝉绿) in Shanghai.
- **YU LEXING (余乐醒 / Dr. Yu).** France-trained chemist. Split: 余乐醒 = "Brother Yu
  Lexing"; 乐醒兄 = "Brother Lexing".
- **NEW Shanghai-District cast introduced in the ch20 preview (build them out in B15):**
  郑修元 Zheng Xiuyuan (District secretary who held it together single-handed), 陈第容 Chen
  Dirong (assistant secretary in charge of personnel - the traitor whose leak had the enemy
  search 14 offices), 黄志远 Huang Zhiyuan (old comrade, kept the enemy press sheets), and
  "a Mr. Zhao" (赵君, the hard-pressed acting chief). These are the seam into Part Three.
- **Dead comrades carried in memory:** ZENG CHE 曾澈, WANG WEN 王文 (ch11); ZENG ZHONGMING
  曾仲鸣 (ch15/ch16); the B13 Wang-case martyrs.

## Where the book stands

- Part One (北国锄奸) COMPLETE (B01-B05).
- Part Two ("Disgrace at Hanoi" / 河内辱命) COMPLETE (B06-B13). The assassination FAILED;
  Wang Jingwei died at Nagoya 10 Nov 1944; Chen took over the Shanghai District; the whole
  Hanoi cast is laid to rest in the record.
- **Part Three ("Renown Won in a Hundred Battles" / 百战声威) has OPENED (B14 = ch20, the
  self-preface).** The Shanghai volume covers 上海区 operations Aug 1939 - Oct 1941 (several
  hundred action-cases; ~1,000 personnel).
- **NEXT: B15 = ch21** - 第一章 十里洋场重振雄威 "Chapter 1. Back in Shanghai, Our Might
  Restored," the FIRST Shanghai chapter (~21,426 chars, 1 <h2> + 162 <p>). drop=2;
  couplet-style sub-headings (NO numbered parens found in a first pass); a "(第一章完
  下期续载)" serialization coda glued near L157 with trailing content - resolve p-by-p.

## What is NEXT

- Batch B15 = ch21 (the first Shanghai chapter). Kickoff is the paste-block at the top.
  Runs to completion (no gate); ends by pasting the B16 kickoff. B16 = ch22 (mind the
  stray 杀 on the ch22 title).
- The frozen register reference is `reference/B01_frozen.md`. Narrative sits at
  4.55-4.78 en/han; prefaces/document-heavy chapters run higher.
- Sub-heading pattern DIFFERS by chapter. Styles seen: Part One numbered 一/二/三;
  ch11/ch14/ch20-title COUPLET-STYLE with NO number prefix; ch12/ch13/ch15/ch16/ch17/ch18
  numbered-in-parens (一)/(二)…; ch08/ch16/ch18 have a GLUED sub-heading; ch13's inner
  enumerated list 一、-六、 rendered `####`. Grep each new chapter p-by-p.
- WATCH for source anomalies: cuts, misplaced-「 glitches, corrupt/dropped-character
  phrases, terminal-」 name-splits, the in-text "(第N章完)" coda pattern (ch12/ch13/ch16;
  ch21 has "(第一章完下期续载)" WITH continued-next-issue + trailing content), fullwidth-zero
  (U+25CB) and Latin-O number forms, and pervasive single-character substitutions. Re-grep
  each batch's source for `\[\d+\]` note markers (none present through B14).

## Open items for the read-through / completion

- Feed decided renderings back to authority.json on completion: 军统 "the Juntong"; the
  full B02-B14 historical-name set (Part One; the B06-B07 Japanese/negotiator/elder names;
  the B08 Wang-essay set; the B10/B11 additions; the B12 Chongqing/Shanghai/Japanese cast;
  the B13 martyrs; the B14 Shanghai-District staff).
- Japanese name readings to verify when the men recur (多田骏, 田代皖一郎, 土肥原贤二,
  坂垣/板垣征四郎, 近卫文麿, 影佐祯昭, 今井武夫, 晴气庆胤, 伊藤芳男; 大屋久寿雄 "Ōya Kusuo";
  平沼骐一郎 "Hiranuma Kiichirō"; 川樾 "Kawagoe"; 犬养健/毅 "Inukai", 有田八郎 "Arita
  Hachirō", 西尾寿造 "Nishio Toshizō", 佐藤贤了 "Satō Kenryō", 矢野征记 "Yano Seiki",
  清水董三 "Shimizu Tōzō", 谷垣专一 "Tanigaki", 仓冈克行 "Kuraoka").
- Identify 剑秋 "Jianqiu" (a 1932 Nanjing "elder brother" of Chen) when sources allow.
- Stray source glyphs still to resolve: trailing 杀 on the ch22 title; 毛酋 in a ch36
  section title.
- Provisional romanizations to firm up when sources allow (glossary `provisional` rows,
  incl. the B10/B11/B12 additions and the B14 Shanghai staff 陈第容, 黄志远; 赵君 "Mr. Zhao"
  awaits his full name in ch21).

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01-B14 builds (0/0/0/0). Source is a clean
  digital EPUB, predominantly simplified with residual variant glyphs and pervasive
  digitization glitches (list them, render to plain sense, do not footnote mechanical
  typos). B01-B14 glitch lists are in PROGRESS.md.
- Running-header line 英雄无名-陈恭澍 (from the `<title>`) opens all 43 content files: drop
  it. drop count is variable - most drop=2; ch01/ch10/ch20 drop=3.
- Enumerated ；/：/、 bullet lists, quoted-document/roster lines, salutations, and verse
  lines in the source are DELIBERATE separate `<p>` - do NOT merge them; only genuine
  mid-phrase splits (last char not terminal, OR a source `<p>` boundary that severs one
  sentence) merge, and those can CHAIN across 3+ fragments. ALWAYS confirm the extracted
  body count p-by-p against data/src_epub. A dash-ended lead-in (…如下者–, cf. ch20 L12)
  that is its OWN source `<p>` is DELIBERATE, NOT a split.
- Faithful numbering gaps/anomalies (NOT errors): Part Three skips ch7, splits ch10 into
  (上)/(下); 三面受敌 一往无前 titles two different chapters (ch14 and ch24); ch09 printed
  §五 before §四; ch13 restarts its (一)-(五) numbering for the appended essay; ch16
  reproduces two whole Wang documents; ch21 carries a magazine "下期续载" seam. Preserve and,
  where a reader would stumble, footnote.
- GLOSSARY-KEY DISCIPLINE (the B12 lesson): a key must be a DISTINCTIVE proper noun that
  renders ONE way everywhere. Do NOT key common nouns or full book titles. Books -> FOOTNOTES.
  A bare surname whose full name is not yet known (赵君 "Mr. Zhao") is rendered inline, not keyed.
- Expect a stray per-task branch at the top of every batch; consolidate onto
  claude/nameless-heroes per rule 2.
