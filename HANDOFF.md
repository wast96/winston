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
Nameless Heroes B10

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once (its ONE failing regression test, "hook stands down on template stub", is a KNOWN false alarm; all others pass), then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05), B02 (ch06), B03 (ch07), B04 (ch08), B05 (ch09), B06 (ch10 preface + ch11), B07 (ch12), B08 (ch13) and B09 (ch14) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them.

Do Batch B10 = ch15 (ONE unit, ~21,830 source chars — the CLIMAX chapter, the second-largest of Part Two): 第五章 博浪一击 误中副车 "Chapter 5. A Blow at Bolang, the Wrong Carriage Struck" — the fifth chapter of PART TWO ("Disgrace at Hanoi"). This is the assassination attempt ITSELF and its failure: Yu Lexing's poison-bread "soft action" that fails testing; the gas device; the "sanction order" (制裁令) finally arriving in the small hours of 19 March of the twenty-eighth year (1939); the botched car chase across the Red River bridge (a missed chance); the night raid on 27 Gao Lang Street, where Wang Luqiao shoots the man crouched under the bed — who proves to be Zeng Zhongming, NOT Wang Jingwei (hence the title: 误中副车 "the wrong carriage struck"); three men captured; and a closing documentary section (五) that quotes three books and corrects them. Read the last two pages of ch14 English (out/ch14_reading.md) and the tail of ch13 (out/ch13_reading.md) for register + story continuity: ch14 framed the operation as three phases and foreshadowed the failure ("却失败了！"); the team and its arms are in place and the sanction order is now imminent. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch15 from data/src (16_index-split-000-0014.txt). drop=2 (running-header `英雄无名-陈恭澍` from <title> + the <h2> chapter title — CONFIRM against data/src_epub/OEBPS/Text/index_split_000_0014.xhtml). FIVE sub-headings, all numbered-in-parens (一)-(五) like ch12/ch13, each its OWN <p> (all standalone, no glued tails): (一)一个经不起考验的「软性行动」; (二)终于下达了霹雳震惊的「制裁令」; (三)错过了一次可以下手的好机会; (四)这就是误了国家大事的那一幕; (五)撇开是非观点且说错在何处. NO <br/>, NO images, NO set-off formatting (confirm). MANY enumerated one-line action bullets (the announced attack plan; the "second-line deployment"; the three decisions; the job-division; the reader-questions; the point-by-point differences) are DELIBERATE separate <p> ending in ；/。 — do NOT merge them and do NOT render them as headings; keep as normal paragraphs (cf. ch08/ch09's ；/： bullet lists). Section (五) quotes THREE external books at length (「蒋总统秘录」, 「戴雨农先生传」, 「汪政权的开场与收场」) as multi-<p> blocks — deliberate separate <p>, kept whole. Re-verify the body count p-by-p against data/src_epub. EXTRACTOR mid-phrase splits to MERGE (source <p> that break one sentence — re-confirm each against the XHTML, indices will differ from the source_epub line numbers): …毒药就|是可以致命的毒药 (药就|是); …一垛矮墙…墙里面，|有一方小院落 (comma); …这不是汪|精卫还有谁？ (汪|精卫, mid-name); …最愉快的一段|时刻 (一段|时刻); …红河追踪和午夜□□那两|节故事 (两|节). GREP the source for note markers (\[\d+\]) and record "none present" in PROGRESS.md (none through B09).
2. Extend scripts/clean_batch.py with ch15's spec (drop=2; merges = the five above, re-derived as body-line pairs; glued {}; standalone = the five (一)-(五) sub-heading lines). Run it (source-conservation check). Write out/ch15_reading.md (## chapter title from book.json = "Chapter 5. A Blow at Bolang, the Wrong Carriage Struck"; ### for each (一)-(五) sub-heading; one English paragraph per source body line; the quoted-book blocks as normal paragraphs — do NOT use {p} verse here). Then run scripts/batch_artifacts.py ch15 (and, to keep checks.json complete, scripts/batch_artifacts.py with no args).
3. Translate to the FROZEN register (Chen's voice sheet + the character voice sheets are in HANDOFF). Consult glossary.json and authority.json BEFORE romanizing anything; REUSE the settled renderings (the Juntong; Dai Li / 老板 / 戴先生 "Mr. Dai"; 汪精卫 Wang Jingwei; 陈璧君 Chen Bijun; 制裁 "sanction" / 制裁令 "sanction order"; 曾仲鸣 Zeng Zhongming; 徐先生 Mr. Xu; 曾先生 Mr. Zeng; 魏春风 Wei Chunfeng; 阮小姐 Miss Nguyen; 曹师昂 Cao Shi'ang; 谭天堑 Tan Tianqian; 张逢义 Zhang Fengyi; 陈步云 Chen Buyun; 余乐醒 Yu Lexing/Dr. Yu; 岑家焯 Cen Jiazhuo; 方炳西 Fang Bingxi; 王鲁翘 Wang Luqiao; 高朗街 Gao Lang Street / Rue Colombert No. 27; 大陆饭店 the Continental Hotel; the B06/B07/B08 shelves). Part Two PRINCIPALS: Chen(1), Dai Li(2), Wang Jingwei(3), Zheng Jiemin(4), Wang Tianmu(5), Fan Xing(6), Fang Bingxi(7), Wang Luqiao(8). Render Republican years literally per the Part-Two convention ("the twenty-eighth year"; the checker matches the source numeral and the Gregorian if carried). NEW cast to add to glossary.json (with pinyin fields; see the voice sheets in HANDOFF): 唐英杰 Tang Yingjie (the reconnaissance specialist), 余鉴声 Yu Jiansheng (action man, Wang Luqiao's assistant — DISTINCT from 余乐醒 Yu Lexing!), and the household/witnesses from the quoted essay (方君璧 Fang Junbi, Zeng's wife; 朱媺 Zhu Mei; 何文杰 He Wenjie; 汪文惺 Wang Wenxing; 陈国琦 Chen Guoqi; 戴芸生 Dai Yunsheng; 何就 He Jiu; 陈国星 Chen Guoxing; 汪圯 Wang Yi), plus 平沼骐一郎 Hiranuma Kiichirō (the 平沼内阁 "Hiranuma cabinet"), 金雄白 Jin Xiongbai (pen name 朱子家 Zhu Zijia), 吴敬恒 Wu Jingheng (稚晖 Zhihui). Books/places: 「蒋总统秘录」, 「戴雨农先生传」, 「汪政权的开场与收场」, 「举一个例」; 红河大桥 the Red River bridge (the Doumer/Long Biên bridge); 打叻/丹道镇 (a hill resort N of Hanoi — Chen's 打叻 vs the biography's 丹道镇; note the discrepancy); 东方汇理银行 the Banque de l'Indochine.

   ⚠ CRITICAL NAME TRAP: ch13 (B08) recorded 郑邦国 "Zheng Bangguo" (4x, in glossary), but ch15 uses 陈邦国 "Chen Bangguo" 16x consistently (he is the big "open-road vanguard" of the raid, one of the three captured). This is the SAME action-team member with a 陈/郑 surname glitch on one side. RESOLVE against real scholarship (the Hanoi assassination-team roster is documented) and reconcile the glossary + any built units to ONE spelling, footnoting the discrepancy per rule 4. Also watch 汪某/汪逆 for Wang; and the many single-char glitches below.
   WATCH ch15's digitization glitches (list in PROGRESS.md, render to plain sense, footnote only real reading uncertainty): 戴光生 for 戴先生 (光→先); 曾光生 for 曾先生; 汪精术 for 汪精卫 (术→卫); 「内工作」 for 「河内工作」 (dropped 河); 引溥 for 引导 (溥→导); 一片一斤 for 一片一片 (斤→片); 解择 for 解释 (择→释); 注妻 for 汪妻 (注→汪); 陈壁君 for 陈璧君 (壁→璧); 曾仲呜 for 曾仲鸣 (呜→鸣, recurring); 江之卑劣 for 汪之卑劣 (江→汪, the same 汪→江 class as ch14); 警犭 for 警犬; the 文/交 swap class in section (五)'s quoted books (摘录交内, 官交书, 本交, 汪交惺 for 汪文惺); 我达以为 for 我还以为; 闲枪声 for 闻枪声; 演示文稿 (anachronism for a plain 演示/demonstration). NUMBER-DENSE for its length: carry the real counts as DIGITS/explicit words (dates 二十八年三月十九/二十/二十一/二十二日; 三十年十/十一月; 民国六十八年/七十年/四十八年/四十一年; 三十七/三十八年; times 二时许, 十一时四十分, 四点钟, 四点五十分, 零时过九分; distances 九十公里, 三公里, 三百公尺, 两百公尺; money 四千五百元 = 九张五百; page/volume refs 二○三页, 九十四页, 四十一页至四十四页, 第十一册, 第五册, 六册; 五人, 七个人, 三组/三辆, 三枪), and NOISE only elided-tens/approximate forms — add a commented B10 block to data/noise.txt for: 八、九百, 四、五百, 四、五十, 四、五样, 五、六响, 五、六个, 七、八分钟, 三两天, 两三分钟, 一两分钟, 十来分钟, and the fullwidth-zero page ref 二○三 (○ = U+25CB, English carries 203).
4. Checks (per unit): verify_unit.py ch15 (parity + numbers with --noise auto-found + anchors); check_align.py ch15; regenerate checks.json with scripts/batch_artifacts.py (no args) and run check_structure.py --config checks.json + check_content.py --config checks.json (note: check_content prints PRE-EXISTING ch13 name-map artifacts — Miss Nguyen/Oya Kusuo/Yuan Haowen — and exits 0; confirm ch15 itself is clean); qc_entities.py on a reconstructed bilingual (data/zh body lines + out/ch15_en.json, `> zh` / en pairs, strip the ### heading lines; every glossary row needs a pinyin field); verify the TAIL against the source (the closing paragraph 制裁汪精卫的工作，并不到此为止…还有多方面的发展…更多的牺牲！ and the 举一个例 / 吴稚晖 passage before it). check_register.py --ref reference/B01_frozen.md out/ch15_reading.md ("shall" in Chen's narration is deliberate; the two long quoted-book blocks may push the ratio up like ch12/ch13 — read the note, do not de-formalize).
5. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (the full list is in PROGRESS.md). This chapter EARNS several NEW notes (it is dense with first-appearance material): candidates — the TITLE allusion 博浪一击/误中副车 (Zhang Liang's iron-cudgel ambush of Qin Shi Huang at Bolangsha, which "struck the attendant carriage by mistake" — the exact frame for killing Zeng in Wang's place); the Red River / Doumer (Long Biên) bridge; 制裁令 as the formal kill-order (already glossed — do NOT re-note 制裁 itself); Zeng Zhongming's death + Wang's 「曾仲鸣先生行状」 eulogy; the three source books (蒋总统秘录 / 戴雨农先生传 / 汪政权的开场与收场 — REAL books; give the scholarship verdict IN the note, corroborated/uncorroborated); Wang's apologia 「举一个例」 and the 国防最高会议 record he is said to have doctored; 吴稚晖 Wu Zhihui; 平沼骐一郎 / the Hiranuma cabinet; 朱执信 Zhu Zhixin (if not already noted); the idioms 不入虎穴焉得虎子, 罪不及妻孥, 打草惊蛇 (footnote only where they carry weight — be generous but do NOT pad; consult the NOT-re-noted list first). Merge notes via apparatus_merge.py (numeric character references only; anchors verbatim substrings of the reading.md, in body text not headings; watch the American-style period-inside-quote and straight-vs-curly-quote anchor traps from B06/B08). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field). Confirm ch15 carries no images.
6. Rebuild the EPUB, qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; update HANDOFF.md; commit and push to claude/nameless-heroes.

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B11 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
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
  11 notes; 24 glossary rows.
- **Batch B04 (ch08), Part One Section 3.** 461 paragraphs; the Ji Hongchang case,
  the Wang Zixiang poison death, the 9 Nov 1934 Guomin Hotel shooting. 12 notes; 54 rows.
- **Batch B05 (ch09), Part One Section 4.** 332 paragraphs; the Shi Yousan case of
  winter 1934. 9 notes; 72 glossary rows. **Part One COMPLETE.**
- **Batch B06 (ch10 + ch11), Part Two opens.** ch10 = the Part Two Author's Preface;
  ch11 = "Bloodshed Against the Enemy" (the North China martyrs; the flight to Hanoi;
  the "Yan Telegram" with Chen's rebuttal). 14 notes (137 cumulative); 59 rows.
  **Part Two title RESOLVED: keep "Disgrace at Hanoi."**
- **Batch B07 (ch12), Part Two Chapter 2.** "Unfathomable Hearts, Hidden Designs"
  (131 paras). The two long documents (Konoe's third statement, Chiang's 9,000-char
  address); Chen's case that the Juntong had no advance word of Wang's collusion.
  16 notes (153 cumulative); 40 rows.
- **Batch B08 (ch13), Part Two Chapter 3.** 第三章 波诡云谲 风雨欲来 "Treacherous Tides,
  a Gathering Storm" (262 body paragraphs — the largest chapter of Part Two). The
  operational half (Mr. Xu, the order to verify Wang's departure, the action team and
  its arms arriving), an in-text "(本章完)" marker, then an appended biographical essay
  on Wang Jingwei. 21 notes (174 cumulative); 84 glossary rows. First use of `{p}` verse.
- **Batch B09 (ch14), Part Two Chapter 4.** 第四章 三面受敌 一往无前 "Beset on Three
  Sides, Ever Forward" — a very short (520-char) bridge chapter: one couplet-style
  sub-heading + FIVE body paragraphs, framing the operation as three phases and
  foreshadowing its failure. 0 new notes (174 cumulative); 0 new glossary rows. All
  checks green; qa_epub PASS; epubcheck 0/0/0. EPUB now **14/43 chapters**. Detail in
  PROGRESS.md ("Batch B09").

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` — derives data/zh/<id>.txt verbatim from data/src,
  applying per-unit drops/merges/heading-splits with a source-conservation check.
  Specs for ch01-ch14. Merge logic FOLLOWS CHAINS (a `<p>` split into 3+ fragments is
  rejoined whole; a `<br/>` prose pair can be folded into a chain — cf. ch13's
  L156/157/158). **drop is variable:** most chapters drop=2; ch01 and ch10 drop=3.
- `scripts/batch_artifacts.py` — derives out/<id>_en.json FROM out/<id>_reading.md
  and writes checks.json. Author the reading.md; run this (accepts multiple ids;
  no args = all ch*_reading.md, which keeps checks.json complete). `body_lines`
  strips `#`-headings, `***`, and the `{vdgp}` set-off prefix.
- `scripts/verify_unit.py <id>` — parity + numbers (auto-finds data/noise.txt; do NOT
  pass --noise, it is treated as a cid) + anchors. Run per unit.
- `scripts/check_content.py` (patched) — name_map skips "_"-prefixed glossary
  categories/entries. NOTE: it flags PRE-EXISTING ch13 name-map artifacts (Miss
  Nguyen / Oya Kusuo / Yuan Haowen — diacritic/variant forms the substring matcher
  cannot align) and still exits 0; those are not new failures.
- **Verse marker `{p}`** (first used in ch13): prefix a pure-verse body line with
  `{p} ` and the builder renders `<p class="verse">`; the checks and batch_artifacts
  strip the prefix. Only mark body lines that are ENTIRELY verse.
- Glossary is authored/merged BY HAND into the SECTIONED file
  (people/organizations/places/terms), idempotent + re-read-verified. **Every row
  MUST carry a `pinyin` field** — `qc_entities.py` does `rec["pinyin"]` and KeyErrors
  otherwise. apparatus_merge's glossary path assumes a FLAT map and would corrupt the
  sectioned file; NOTES still go through apparatus_merge.py.
- **Note-anchor gotchas:** (B06) American-style punctuation puts the period INSIDE the
  closing quote (`Corps."`), so an anchor ending `Corps"` fails as a false miss —
  anchor on an interior phrase. (B08) the reading.md uses STRAIGHT quotes/apostrophes;
  an anchor written with curly `"`/`'` will not match — keep anchors ASCII, ideally
  without any quote character.
- data/noise.txt carries the B01-B09 project noise rules (each with a comment line).
  Republican years are rendered literally in Part Two ("the twenty-eighth year"); the
  checker matches the source numeral directly. Elided-tens (十七、八 / 四、五 / 三、四 /
  二、三 etc.) and idioms/hyperbole are noised as artifacts; the value stays in the
  English. Fullwidth-zero years/refs (一九○五 / 二○三, ○ = U+25CB) must be noised — the
  checker cannot compose them — and the value carried in the English.
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches it; re-run
  per session). setup.sh's ONE failing regression test ("hook stands down on template
  stub") is a KNOWN false alarm coupled to real (non-template) book state, not a
  defect; all other regression tests pass.

## Renderings settled / carry-forward

- 军统 / 军统局 -> "the Juntong" (DECIDED). 戴笠 Dai Li (courtesy Yunong; 老板 "the Boss";
  戴先生 "Mr. Dai"); 汪精卫 Wang Jingwei (原名 汪兆铭 "Wang Zhaoming"); 陈璧君 Chen Bijun.
  制裁 "sanction"; 制裁令 "sanction order". Chiang's titles: 校长 "the Commandant", 领袖
  "the Leader", 委员长 "the Generalissimo", 总裁 "the Director-General" (Wang = 副总裁
  "Vice-Director-General"). 总理 = "the Party Leader" / 国父 = "the Father of the Nation"
  = Sun Yat-sen (孙中山 in glossary; 总理 deliberately NOT glossaried). Floors: 二楼/三楼
  = "second/third floor". Republican years literal in Part Two. 为虎作伥 rendered
  "playing the tiger's cat's-paw" (matching ch13; earlier ch02 "a tiger's accomplice").
- **B03-B07 shelves (reuse; in glossary.json):** the Juntong internal units,
  Tianjin/Beiping/Hong Kong/Hanoi geography, the Mauser "box-cannon", the Green Gang,
  the Kwantung Army, Manchukuo, the "Yan Telegram", the Three Principles of Peace,
  Konoe's "New Order in East Asia", 支那 = "Shina", the Five Ministers' Conference, the
  Kōain, the Tanaka Memorial, the Yunnan-Vietnam railway, the Hanoi team as "the
  Eighteen Arhats"; people: Cen Jiazhuo, Yu Lexing, Zhou Fohai, Chen Gongbo, Gao
  Zongwu, Mei Siping, Kagesa Sadaaki, Konoe, Long Yun, Zeng Zhongming, etc.
- **B08 shelf (reuse; in glossary.json).** Hanoi operation: 徐先生 "Mr. Xu"; 曾先生 "Mr.
  Zeng"; 魏春风 Wei Chunfeng; 阮小姐 Miss Nguyen; 曹师昂 Cao Shi'ang; 谭天堑 Tan Tianqian;
  张逢义 Zhang Fengyi; 郑邦国 Zheng Bangguo (⚠ but ch15 has 陈邦国 — see the B10 name
  trap); 陈步云 Chen Buyun; 黄强 Huang Qiang; 何芝园 He Zhiyuan; 王芄生 Wang Fansheng; 谷正鼎
  Gu Zhengding; the Continental Hotel; 高朗街 "Gao Lang Street" (Rue Colombert, No. 27);
  海防 Haiphong; 息烽 Xifeng. Wang-essay history names (Zaifeng, the Tongmenghui, the Min
  Bao, Zhang Taiyan, Liang Qichao, Huang Xing, Song Jiaoren, Tao Chengzhang, Borodin/
  Maring/Joffe, the Zhongshan Warship Incident, the Ninghan Split, Chen Duxiu, Zhou
  Enlai, Ye Ting/He Long, Zhang Fakui, Shen Song, Gu Mengyu, Trautmann, Gambetta, Li
  Yu, the Shanhaijing/Jingwei-bird, the First Sino-Japanese War, the Ryukyus). See the
  B08 PROGRESS detail. Provisional romanizations for obscure operatives are marked.
- **B09 shelf.** ch14 introduced NO new referents (a bridge chapter) — reused the
  settled Wang Jingwei / Mr. Dai / sanction rows only.

## Voice sheet — CHEN GONGSHU (author / narrator)

- REGISTER: educated, formal, essayistic first person; grave and a touch archaic but
  not stilted. Long semicolon-joined clauses; four-character idiom and classical
  allusion used freely and footnoted when they carry weight. Refers to himself as
  笔者 "the writer" and 我 "I". His narrating "shall" is DELIBERATE — do not
  de-formalize it; check_register flags it informationally (B06 33%, B08 29%,
  verified deliberate; a very short chapter like ch14 can read 0% simply for want of
  the word).
- STANCE: self-justifying yet self-effacing; insists on truthfulness, admits his
  blunders; tender toward dead comrades, bitter and scornful toward the enemy;
  rhetorical questions and exclamations for emphasis. In ch15 (the botched
  assassination) this stance is at its rawest — he narrates his own hesitations, the
  missed chance on the bridge, the shattering phone call ("你们搞错了！"), and then
  turns to a documentary self-reckoning, quoting three books against his own memory
  and owning the failure. Keep the quoted-book register (official/journalistic)
  distinct from his own dry, remorseful first person.
- Ratio ~4.55-4.76 en/han in narrative; prefaces denser (~5.2); document-/essay-heavy
  chapters run higher (ch12 4.84, ch13 4.79); a very short chapter swings wide (ch14
  5.33 on 5 paragraphs). ch15's two long quoted-book blocks will pull its ratio up.

## Voice sheets — principal & recurring cast

- **DAI LI (戴雨农 / Mr. Dai / 老板 "the Boss").** Warm off duty, abrupt and close-mouthed
  on business; grave and overburdened at Hanoi. In ch15 he sends the "sanction order"
  by telegram (relayed through Fang Bingxi), having positioned "hard-action" men at
  Hanoi with evident forethought; Chen is careful NOT to overstate Dai's role in the
  historic decision.
- **WANG LUQIAO (王鲁翘 / Luqiao).** Part Two principal (cast 8). Shandong man, ex-bodyguard
  of Dai Li; co-lead of the Hanoi action team and the designated trigger-man. In ch15
  he shoots the man under the bed (Zeng Zhongming, in error), and takes the news with
  a bluff "没关系，咱们再干！". Bluff, bold, loyal; shares Chen's homesick northern tastes.
- **FANG BINGXI (方炳西 / Brother Bingxi).** Part Two principal (cast 7). The advance man:
  the safe house, fluent French, off-stage-practical; holds the cipher book and decodes
  for Chen; carries the sanction order in by night; likely bears a "supervisory" role.
- **YU LEXING (余乐醒 / Brother Lexing / Dr. Yu).** France-trained chemist, chief of staff
  and technical adviser; brooding, over-thinking, thin-skinned ("开不得玩笑…自尊心特别强").
  In ch15 he champions the poison-bread "soft action" and the gas device — both fail —
  and Chen must humor him ("我只有洗耳恭听的份") while quietly preferring a hard strike.
- **CEN JIAZHUO (岑家焯 / Senior Jiazhuo).** Chen's Whampoa senior; silent, steady, a gift
  for command. In ch15 he breaks his usual reserve to volunteer for the "second-line
  deployment" should Chen fall.
- **MR. XU (徐先生).** The deliberately unnamed "special personage" (a pseudonym). Deeply
  embedded in Hanoi's overseas-Chinese community and with the French police; aids "from
  behind the scenes," never writes a word down, says "you people." In ch15 he finds the
  bread-delivery angle, counsels a clean quick job, and delivers the two shattering
  phone calls at dawn ("你们搞错了…受伤的是曾仲鸣" and "有三个人被逮去了").
- **WEI CHUNFENG (魏春风).** The brilliant young overseas-Chinese guide (Fujian stock,
  raised in Annam; four tongues). In ch15 he tails the Wangs, arranges the bread, and —
  the "及时雨" — bribes the two Annamese plainclothes police (4,500 piastres) to clear
  the raid; pure of motive ("但得报效国家，绝无任何要求").
- **WANG TIANMU (王天木 / 王大哥).** The operational planner: worldly, cool, terse. Off-stage
  in ch15. WATCH — his loyalty is tested later in the Hanoi affair; render him straight.
- **ZHENG JIEMIN (郑介民 / Mr. Zheng).** Part Two principal (cast 4). The theorist; off-stage
  in B06-B09. Chen firmly denies accounts that Zheng directed the Hanoi operation.
- **FAN XING (范行 / "Jiman").** Part Two principal (cast 6). The Beiping intelligence enigma;
  silver-tongued, evasive. May recur; render his charm and Chen's wariness side by side.
- NEW in ch15 (add voice/glossary rows in B10):
  - **TANG YINGJIE (唐英杰).** The action team's reconnaissance specialist ("技有专长") —
    scales the roof of Wang's house to verify the third-floor bedroom; leads the raiders
    over the wall. Nimble and skilled, but with "几段不切实的往事" that make Chen watch him;
    slips out to "buy stomach medicine" and is gently distrusted.
  - **YU JIANSHENG (余鉴声).** Action man, Wang Luqiao's second in the raid — DISTINCT from
    Yu Lexing (余乐醒). Cool-headed (restrains the hot-blooded Chen Bangguo, "还是判明车子
    上究竟是些什么人"); one of the three captured (seven years). Render him steady, sensible.
  - **CHEN/ZHENG BANGGUO (陈邦国 in ch15 / 郑邦国 in ch13 — RESOLVE the surname).** The big,
    powerful "open-road vanguard" who axes the doors and fires the covering shots;
    impetuous, itching to charge ("我说冲上去就干"); one of the three captured. Render his
    bull-headed eagerness against Yu Jiansheng's caution.
- **Dead comrades carried in memory:** ZENG CHE 曾澈 (martyred Beiping 1940), WANG WEN 王文
  (martyred 1939), eulogized in ch11; and now **ZENG ZHONGMING 曾仲鸣**, killed at Hanoi
  in Wang's place (the 误中副车 of the title) — the operation's tragic mis-hit.

## Where the book stands

- Part One (北国锄奸) is COMPLETE (B01-B05).
- **Part Two — "Disgrace at Hanoi" (河内辱命)** is UNDERWAY: B06 = Preface (ch10) + Chapter 1
  (ch11); B07 = Chapter 2 (ch12); B08 = Chapter 3 (ch13); B09 = Chapter 4 (ch14, the short
  bridge). The team, arms, and plan are set and the sanction order is imminent.
- **NEXT: B10 = ch15** 第五章 博浪一击 误中副车 "A Blow at Bolang, the Wrong Carriage Struck"
  — the CLIMAX: the failed poison-bread "soft action," the sanction order, the bridge
  chase, the night raid that kills Zeng Zhongming by mistake, and the documentary
  reckoning. ~21,830 chars, five (一)-(五) sub-sections.

## What is NEXT

- Batch B10 = ch15 (Part Two, Chapter 5). Kickoff is the paste-block at the top. Runs to
  completion (no gate); ends by pasting the B11 kickoff. This is a note-rich chapter
  (unlike ch14) — expect a healthy count of NEW notes and glossary rows.
- The frozen register reference is `reference/B01_frozen.md`. Narrative sits at 4.55-4.76
  en/han; prefaces denser (~5.2); document-/essay-heavy chapters run higher (ch12 4.84,
  ch13 4.79); ch15's quoted-book blocks will lift it. Read the note, do not reset.
- Sub-heading pattern DIFFERS by chapter. Styles seen: Part One numbered 一/二/三;
  ch11/ch14 COUPLET-STYLE with NO number prefix; ch12/ch13/ch15 numbered-in-parens
  (一)/(二)…; ch13's inner enumerated list 一、–六、 rendered `#### `. Grep each new chapter.
- WATCH for source anomalies: cuts, misplaced-「 glitches, corrupt/dropped-character
  phrases, terminal-」 name-splits, the in-text "(本章完)" coda pattern (ch12, ch13),
  fullwidth-zero (U+25CB) years/refs, and single-character substitutions (the 汪→江 class:
  ch14's 江案, ch15's 江之卑劣; the 先→光, 文↔交, 呜→鸣 classes in ch15). Re-grep each
  batch's source for `\[\d+\]` note markers (none present through B09).

## Open items for the read-through / completion

- **RESOLVE the 陈邦国/郑邦国 surname** (ch15 vs ch13) against scholarship and reconcile
  the glossary + built units to one spelling; footnote the discrepancy.
- Feed decided renderings back to authority.json on completion: 军统 "the Juntong"; the
  full B02-B09 historical-name set (Part One; the B06-B07 Japanese/negotiator/elder
  names; the B08 Wang-essay set; the B10 additions — Hiranuma Kiichirō, Wu Zhihui, Jin
  Xiongbai, Fang Junbi, etc.).
- Japanese name readings to verify when the men recur (多田骏, 田代皖一郎, 土肥原贤二,
  坂垣征四郎, 近卫文麿, 影佐祯昭, 今井武夫, 晴气庆胤, 伊藤芳男; 矢荻 "Yagi", 铃木 "Suzuki",
  大屋久寿雄 "Ōya Kusuo", 吉冈文六 "Yoshioka Bunroku"; and B10's 平沼骐一郎 "Hiranuma").
- Verify the three ch15 source books and their citations against real scholarship:
  「蒋总统秘录」 (Sankei Shimbun's Chiang record), 「戴雨农先生传」 (the 1979 Dai bio), 金雄白
  /朱子家's 「汪政权的开场与收场」; state the verdict in the notes.
- Identify 剑秋 "Jianqiu" (a 1932 Nanjing "elder brother" of Chen) when sources allow.
- Stray source glyphs still to resolve in later batches: trailing 杀 on the ch22 title;
  寿张为幻 in the ch16 title; 毛酋 in a ch36 section title.
- Provisional romanizations to firm up when sources allow (glossary `provisional` rows).

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01-B09 builds (0/0/0). Source is a clean
  digital EPUB, predominantly simplified with residual variant glyphs and pervasive
  digitization glitches (list them, render to plain sense, do not footnote mechanical
  typos). B01-B09 glitch lists are in PROGRESS.md.
- Running-header line 英雄无名-陈恭澍 (from the `<title>`) opens all 43 content files: drop
  it. drop count is variable — most drop=2; ch01 and ch10 drop=3.
- Enumerated ；/： bullet lists and quoted-document/verse lines in the source are
  DELIBERATE separate `<p>` — do NOT merge them; only genuine mid-phrase splits (last
  char not terminal, OR a source `<p>` boundary that severs one sentence — cf. ch13's
  天|下, ch15's 药就|是, 汪|精卫) merge, and those can CHAIN across 3+ fragments. `<br/>`
  inside one `<p>` splits into extra extracted lines — decide per case. ALWAYS confirm
  the extracted body count p-by-p against data/src_epub.
- Faithful numbering gaps/anomalies (NOT errors): Part Three skips ch7, splits ch10 into
  (上)/(下); 三面受敌 一往无前 titles two different chapters (ch14 and ch24); ch09 printed §五
  before §四; ch13 restarts its (一)–(五) numbering for the appended essay. Preserve and,
  where a reader would stumble, footnote.
- Expect a stray per-task branch at the top of every batch; consolidate onto
  claude/nameless-heroes per rule 2.
