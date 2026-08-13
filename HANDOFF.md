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
Nameless Heroes B09

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once, then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05), B02 (ch06), B03 (ch07), B04 (ch08), B05 (ch09), B06 (ch10 preface + ch11), B07 (ch12) and B08 (ch13) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them.

Do Batch B09 = ch14 (ONE unit, only ~520 source chars): 第四章 三面受敌 一往无前 "Chapter 4. Beset on Three Sides, Ever Forward" — the fourth chapter of PART TWO ("Disgrace at Hanoi"). This is a VERY SHORT bridge chapter (a preview of the action to come). Read the last two pages of ch13 English (out/ch13_reading.md) for register + story continuity: at ch13's end the Hanoi team has filled out with the action men and their arms, the operation has moved from surveillance into the preparation-before-action stage, and Chen has closed with a long biographical essay on Wang Jingwei; the "sanction order" from above is still awaited. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch14 from data/src (15_index-split-000-0013.txt). It has drop=2 (running-header `英雄无名-陈恭澍` from <title> + the <h2> chapter title — CONFIRM against the source XHTML in data/src_epub). Only 6 <p>: ONE couplet-style sub-heading with NO number prefix (L3 「壁垒坚强迎接多方面的挑战」, like ch11's style — standalone <p>) and FIVE body paragraphs (L4-8). NO <br/>, NO images, NO set-off formatting (confirm). No extractor mid-phrase splits expected (all five body lines end terminal) — but re-verify p-by-p against data/src_epub as always. GREP the source for note markers (\[\d+\]) and record "none present" in PROGRESS.md.
2. Extend scripts/clean_batch.py with ch14's spec (drop=2; merges []; glued {}; standalone [3] for the couplet sub-heading). Run it (source-conservation check). Write out/ch14_reading.md (## chapter title from book.json = "Chapter 4. Beset on Three Sides, Ever Forward"; ### 「Fortress Firm, Meeting Challenge from Every Side」 for the couplet sub-heading; one English paragraph per source body line), then run scripts/batch_artifacts.py ch14.
3. Translate to the FROZEN register (Chen's voice sheet + the character voice sheets are in HANDOFF). Consult glossary.json and authority.json BEFORE romanizing anything; REUSE the settled renderings (the Juntong; Dai Li / 老板; 汪精卫 Wang Jingwei; 制裁 "sanction"; the B06/B07/B08 shelves). Part Two PRINCIPALS: Chen(1), Dai Li(2), Wang Jingwei(3), Zheng Jiemin(4), Wang Tianmu(5), Fan Xing(6), Fang Bingxi(7), Wang Luqiao(8). Render Republican years literally per the Part-Two convention. WATCH ch14's digitization glitches (list them in PROGRESS.md, render to plain sense, footnote only real reading uncertainty): 江案 for 汪案 ("the Wang case", 江 for 汪, appears 2-3x); 纯粹去百姓 for 纯粹老百姓 (去 for 老); 出卖而国家利益 for …我国家利益 (而 for 我); 不偏不倚的文代 for …交代 (文 for 交). This chapter is number-dense for its length: carry the real counts as DIGITS/explicit words (第一/二/三阶段; 两个半月; 十天; 一天; 十七、八人 → "seventeen or eighteen men"; 四、五人; 三、四人; 二、三人), and NOISE only elided-tens/approximate forms (十七、八, 四、五, 三、四, 二、三) — add a commented B09 block to data/noise.txt. The chapter foreshadows the three phases of the operation and the coming failure ("却失败了！").
4. Checks (per unit): verify_unit.py ch14 (parity + numbers with --noise auto-found + anchors); check_align.py ch14; regenerate checks.json with scripts/batch_artifacts.py and run check_structure.py --config checks.json + check_content.py --config checks.json; qc_entities.py on a reconstructed bilingual (data/zh body lines + out/ch14_en.json, `> zh` / en pairs, strip the ### heading lines; every glossary row needs a pinyin field); verify the TAIL against the source. check_register.py --ref reference/B01_frozen.md out/ch14_reading.md ("shall" in Chen's narration is deliberate; a 520-char chapter may swing the ratios — read the note, do not de-formalize).
5. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (the full list is in PROGRESS.md; this short chapter likely warrants FEW or ZERO new notes — do not pad; nothing here obviously needs one beyond what B01-B08 already cover). Merge any notes via apparatus_merge.py (numeric character references only; anchors verbatim substrings of the reading.md, in body text not headings; watch the American-style period-inside-quote and straight-vs-curly-quote anchor traps from B08). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field) only if ch14 introduces a new referent (it likely introduces none). Confirm ch14 carries no images.
6. Rebuild the EPUB, qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; update HANDOFF.md; commit and push to claude/nameless-heroes.

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B10 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
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
  a Gathering Storm" (262 body paragraphs — the largest chapter of Part Two). An
  operational half — the special personage "Mr. Xu," the order to verify Wang's
  departure, the want of inside intelligence, the action team and its arms arriving —
  then an in-text "(本章完)" marker, then an appended biographical essay on Wang Jingwei
  (his 1910 bomb plot, his whole political history, his errors, his verse). 21 notes
  (174 cumulative); 84 glossary rows. First use of the `{p}` verse marker. All checks
  green; qa_epub PASS; epubcheck 0/0/0. EPUB now **13/43 chapters**. Detail in
  PROGRESS.md ("Batch B08").

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` — derives data/zh/<id>.txt verbatim from data/src,
  applying per-unit drops/merges/heading-splits with a source-conservation check.
  Specs for ch01-ch13. Merge logic FOLLOWS CHAINS (a `<p>` split into 3+ fragments is
  rejoined whole; a `<br/>` prose pair can be folded into a chain — cf. ch13's
  L156/157/158). **drop is variable:** most chapters drop=2; ch01 and ch10 drop=3.
- `scripts/batch_artifacts.py` — derives out/<id>_en.json FROM out/<id>_reading.md
  and writes checks.json. Author the reading.md; run this (accepts multiple ids).
  `body_lines` strips `#`-headings, `***`, and the `{vdgp}` set-off prefix.
- `scripts/verify_unit.py <id>` — parity + numbers (auto-finds data/noise.txt; do NOT
  pass --noise, it is treated as a cid) + anchors. Run per unit.
- `scripts/check_content.py` (patched) — name_map skips "_"-prefixed glossary
  categories/entries.
- **Verse marker `{p}`** (first used in ch13): prefix a pure-verse body line with
  `{p} ` and the builder renders `<p class="verse">` (italic, indented); the checks
  and batch_artifacts strip the prefix. Only mark body lines that are ENTIRELY verse;
  render lines that MIX verse and prose as normal paragraphs with the verse quoted
  inline (cf. ch13's 南岳道中 quatrain + lead-in on one line).
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
- data/noise.txt carries the B01-B08 project noise rules (each with a comment line).
  Republican years are rendered literally in Part Two ("the twenty-eighth year"); the
  checker matches the source numeral directly. Elided-tens (十七、八 / 三、四) and
  idioms/hyperbole are noised as artifacts; the value stays in the English. Fullwidth-
  zero years (一九○五, ○ = U+25CB) must be noised — the checker cannot compose them —
  and the Gregorian carried in the English.
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches it; re-run
  per session). setup.sh's ONE failing regression test ("hook stands down on template
  stub") is a KNOWN false alarm coupled to real (non-template) book state, not a
  defect; all other regression tests pass.

## Renderings settled / carry-forward

- 军统 / 军统局 -> "the Juntong" (DECIDED). 戴笠 Dai Li (courtesy Yunong; 老板 "the Boss");
  汪精卫 Wang Jingwei (原名 汪兆铭 "Wang Zhaoming"); 陈璧君 Chen Bijun. 制裁 "sanction".
  Chiang's titles: 校长 "the Commandant", 领袖 "the Leader", 委员长 "the Generalissimo",
  总裁 "the Director-General" (Wang = 副总裁 "Vice-Director-General"). 总理 = "the Party
  Leader" / 国父 = "the Father of the Nation" = Sun Yat-sen (孙中山 now in glossary,
  attested; 总理 deliberately NOT glossaried — ambiguous with 内阁总理). Floors: 二楼/三楼
  = "second/third floor". Republican years literal in Part Two.
- **B03-B07 shelves (reuse; in glossary.json):** see the earlier HANDOFF/PROGRESS
  detail — the Juntong internal units, Tianjin/Beiping/Hong Kong/Hanoi geography, the
  Mauser "box-cannon", the Green Gang, the Kwantung Army, Manchukuo, the "Yan Telegram",
  the Three Principles of Peace, Konoe's "New Order in East Asia", 支那 = "Shina", the
  Five Ministers' Conference, the Kōain, the Tanaka Memorial, the Yunnan–Vietnam
  railway, the Hanoi team as "the Eighteen Arhats"; and the people: Cen Jiazhuo, Yu
  Lexing, Zhou Fohai, Chen Gongbo, Gao Zongwu, Mei Siping, Kagesa Sadaaki, Konoe,
  Long Yun, Zeng Zhongming, etc.
- **B08 shelf (reuse; in glossary.json).** Hanoi operation: 徐先生 "Mr. Xu" (the
  deliberately-unnamed special personage, pseudonym-surname 徐); 曾先生 "Mr. Zeng" (the
  Fujianese go-between — DISTINCT from Zeng Che and Zeng Zhongming); 魏春风 Wei Chunfeng;
  阮小姐 Miss Nguyen (阮 = Nguyễn); 曹师昂 Cao Shi'ang; 谭天堑 Tan Tianqian; 张逢义 Zhang
  Fengyi; 郑邦国 Zheng Bangguo; 陈步云 Chen Buyun; 黄强 Huang Qiang (Mujing); 何芝园 He
  Zhiyuan; 王芄生 Wang Fansheng; 谷正鼎 Gu Zhengding; the Continental Hotel on Paul Bert;
  高朗街 "Gao Lang Street" (Rue Colombert, No. 27 = Wang's residence); 海防 Haiphong;
  息烽 Xifeng (the Juntong's own detention camp). Wang-essay history: 载沣 Zaifeng (the
  Prince Regent); 同盟会 the Tongmenghui; 民报 the Min Bao; 章太炎 Zhang Taiyan; 梁启超
  Liang Qichao + 保皇党 the Royalists; 黄兴 Huang Xing; 宋教仁 Song Jiaoren; 陶成章 Tao
  Chengzhang; 光复会 the Restoration Society; 鲍罗廷 Borodin / 马林 Maring / 越飞 Joffe;
  中山舰事件 the Zhongshan Warship Incident; 宁汉分裂 the Ninghan Split; 陈独秀 Chen Duxiu;
  周恩来 Zhou Enlai; 叶挺 Ye Ting / 贺龙 He Long; 张发奎 Zhang Fakui; 沈崧 Shen Song
  (Cigao); 顾孟余 Gu Mengyu; the Marco Polo Bridge Incident; 陶德曼 Trautmann; 刘豫/张邦昌
  Liu Yu / Zhang Bangchang (the puppet-emperor archetype); 甘必大 Gambetta; 李后主 Li Yu
  (the Latter Ruler Li); 山海经 the Shanhaijing + the Jingwei-bird myth; 甲午战争 the
  First Sino-Japanese War; 琉球 the Ryukyus. Provisional romanizations for obscure
  operatives / Japanese readings are marked in glossary.json.

## Voice sheet — CHEN GONGSHU (author / narrator)

- REGISTER: educated, formal, essayistic first person; grave and a touch archaic but
  not stilted. Long semicolon-joined clauses; four-character idiom and classical
  allusion used freely and footnoted when they carry weight. Refers to himself as
  笔者 "the writer" and 我 "I". His narrating "shall" is DELIBERATE — do not
  de-formalize it; check_register flags it informationally (B06 33%, B08 29%,
  verified deliberate).
- STANCE: self-justifying yet self-effacing; insists on truthfulness, admits his
  blunders; tender toward dead comrades, bitter and scornful toward the enemy;
  rhetorical questions and exclamations for emphasis. In B08 he digresses freely (the
  card-playing at the Xu residence, the "idle talk"), then turns a long, unsparing
  historical-moral essay on Wang Jingwei, keeping the quoted enemy documents' and
  Wang's own poetry's inflated/plaintive register distinct from his own dry scorn.
- Ratio ~4.55-4.76 en/han in narrative; prefaces denser (~5.2); document-/essay-heavy
  chapters run higher (ch12 4.84, ch13 4.79). Keep the semicolon rhythm.

## Voice sheets — principal & recurring cast

- **DAI LI (戴雨农 / Mr. Dai / 老板 "the Boss").** Warm off duty, abrupt and close-mouthed
  on business; grave and overburdened at Hanoi. In B08 he presses Chen by telegram
  (verify Wang's departure; make ready but do not act), and — a late revelation from
  Cao Shi'ang — may have slipped into Hanoi again unannounced, warning off a transport
  official and hauling a woman out of Tan Tianqian's wardrobe. Movements ever hard to
  fathom.
- **FANG BINGXI (方炳西 / Brother Bingxi).** Part Two principal (cast 7). The advance man:
  rented and fitted the safe house, fluent French, off-stage-practical, generous (in B08
  he covers Chen's card losses without shaming him). One of the operation's few survivors.
- **WANG LUQIAO (王鲁翘 / Luqiao).** Part Two principal (cast 8). Shandong man, ex-bodyguard
  of Dai Li; co-lead of the Hanoi action team; a fellow northerner who shares Chen's
  homesick craving for northern food (and the card games).
- **WANG TIANMU (王天木 / 王大哥 "Elder Brother Wang").** The operational planner: worldly,
  cool, terse. WATCH — his loyalty is tested later in the Hanoi affair; render him
  straight for now, do not tip it.
- **CEN JIAZHUO (岑家焯 / Senior Jiazhuo).** Chen's Whampoa senior; silent, steady, a gift
  for command. Grave and unshowy.
- **YU LEXING (余乐醒 / Brother Lexing / Dr. Yu).** France-trained chemist, the unit's chief
  of staff and technical adviser; brooding, over-thinking. In B08 his fluent French wins
  him no local contacts — a foil to Mr. Xu's easy reach.
- **MR. XU (徐先生).** NEW in B08 (cast, not principal; a pseudonym — the deliberately
  unnamed "special personage"). Jiangsu (Wuxi) man, ~40s, Europe/America-educated in
  political economy; short and stocky, thick spectacles, bold and bookless in manner.
  Deeply embedded in the Hanoi overseas-Chinese community and with the French police;
  aids "from behind the scenes" as a guest-retainer, says "you people" not "we," never
  writes a word down. Affable, tactful (hides in his study during the card games).
- **WEI CHUNFENG (魏春风).** NEW in B08 (cast, not principal). A brilliant young overseas-
  Chinese, ~20, Fujian stock raised in Annam; four tongues, knows every corner of Hanoi;
  the team's local guide and navigator, in love with the Annamese Miss Nguyễn. Eager,
  quick, endlessly curious about the work.
- **CAO SHI'ANG (曹师昂).** NEW in B08 (cast, not principal; a survivor Chen meets again
  decades later). Hunan aviator, French military-aviation graduate, flew for the French
  Volunteer Air Squadron; bold and open-hearted, came to Hanoi with his French wife and
  two revolvers. It is his late testimony that makes Chen doubt Dai Li never returned.
- **TAN TIANQIAN (谭天堑).** NEW in B08 (cast, not principal). A melancholy Hunan man,
  French-trained in finance, just out of Xifeng detention; on a separate secret mission,
  travelling with a French companion he hides; ends, decades later, in tragedy Chen has
  yet to tell. Render his gloom and Chen's wary sympathy.
- **ZHENG JIEMIN (郑介民 / Mr. Zheng).** Part Two principal (cast 4). Educated, urbane, the
  theorist. Off-stage in B06-B08; Chen firmly denies the (mistaken) accounts that Zheng
  directed the Hanoi operation.
- **FAN XING (范行 / "Jiman").** Part Two principal (cast 6). The Beiping intelligence enigma;
  silver-tongued, evasive. May recur; render his charm and Chen's wariness side by side.
- **Dead comrades carried in memory:** ZENG CHE 曾澈 (martyred Beiping 1940), WANG WEN 王文
  (martyred 1939); both eulogized in ch11.

## Where the book stands

- Part One (北国锄奸) is COMPLETE (B01-B05).
- **Part Two — "Disgrace at Hanoi" (河内辱命)** is UNDERWAY: B06 gave the Preface (ch10)
  and Chapter 1 (ch11); B07 gave Chapter 2 (ch12); B08 gave Chapter 3 (ch13) — the team
  and its arms in place, surveillance turned toward action, plus the long Wang-Jingwei
  essay. The "sanction order" is still awaited.
- **NEXT: B09 = ch14** 第四章 三面受敌 一往无前 "Beset on Three Sides, Ever Forward" — a
  VERY SHORT (~520-char) bridge chapter previewing the three phases of the operation and
  foreshadowing its failure. Then ch15 (B10) is the assassination attempt itself
  (博浪一击 误中副车 "A Blow at Bolang, the Wrong Carriage Struck").

## What is NEXT

- Batch B09 = ch14 (Part Two, Chapter 4, ~520 chars — trivially short). Kickoff is the
  paste-block at the top of this file. Runs to completion (no gate); ends by pasting the
  B10 kickoff. Likely FEW or ZERO new notes and no new glossary rows.
- The frozen register reference is `reference/B01_frozen.md`. Narrative sits at 4.55-4.76
  en/han; prefaces denser (~5.2); document-/essay-heavy chapters run higher (ch12 4.84,
  ch13 4.79). A 520-char chapter may swing the ratios — read the note, do not reset.
- Sub-heading pattern DIFFERS by chapter. FOUR styles seen: Part One numbered 一/二/三;
  ch11/ch14 COUPLET-STYLE with NO number prefix; ch12/ch13 numbered-in-parens (一)/(二);
  and ch13's inner enumerated list 一、–六、 rendered `#### `. ch13 also RESTARTS its
  parenthesized numbering for the appended essay. Grep each new chapter to set the spec.
- WATCH for source anomalies: cuts, misplaced-「 glitches, corrupt/dropped-character
  phrases, terminal-」 name-splits (ch12), the in-text "(本章完)"/coda pattern (ch12,
  ch13), fullwidth-zero (U+25CB) years (ch13), and single-character substitutions
  (ch14's 江案 for 汪案, etc.). Re-grep each batch's source for `\[\d+\]` note markers
  (none present through B08).

## Open items for the read-through / completion

- Feed decided renderings back to authority.json on completion: 军统 "the Juntong"; the
  B02-B08 historical names (the full Part-One set, plus the B06-B07 Japanese/negotiator/
  elder names, plus the B08 set: 孙中山, 载沣, 善耆, 章太炎, 梁启超, 黄兴, 宋教仁, 陶成章,
  鲍罗廷, 马林, 越飞, 陈炯明, 陈独秀, 周恩来, 叶挺, 贺龙, 张发奎, 沈崧, 顾孟余, 郑学稼,
  唐有壬, 董其昌, 元遗山, 王宠惠, 宋子文).
- Japanese name readings to verify when the men recur (多田骏, 田代皖一郎, 土肥原贤二,
  坂垣征四郎, 近卫文麿, 影佐祯昭, 今井武夫, 晴气庆胤, 伊藤芳男; and the B08 additions
  矢荻 "Yagi", 铃木/玲木 "Suzuki", 大屋久寿雄 "Ōya Kusuo", 吉冈文六 "Yoshioka Bunroku").
- Identify 剑秋 "Jianqiu" (a 1932 Nanjing "elder brother" of Chen) when sources allow.
- Stray source glyphs still to resolve in later batches: trailing 杀 on the ch22 title;
  寿张为幻 in the ch16 title; 毛酋 in a ch36 section title.
- Provisional romanizations to firm up when sources allow (see glossary `provisional`
  rows — many B08 operatives and the Nguyễn/Yagi/Suzuki readings among them).

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01-B08 builds (0/0/0). Source is a clean
  digital EPUB, predominantly simplified with residual variant glyphs and pervasive
  digitization glitches (list them, render to plain sense, do not footnote mechanical
  typos). B01-B08 glitch lists are in PROGRESS.md.
- Running-header line 英雄无名-陈恭澍 (from the `<title>`) opens all 43 content files: drop
  it. drop count is variable — most drop=2; ch01 and ch10 drop=3.
- Enumerated ；/： bullet lists and quoted-document/verse lines in the source are
  DELIBERATE separate `<p>` — do NOT merge them; only genuine mid-phrase splits (last
  char not terminal, OR a source `<p>` boundary that severs one sentence — cf. ch13's
  天|下, 走|上极端, 专事国际情报|由王芄生) merge, and those can CHAIN across 3+ fragments.
  `<br/>` inside one `<p>` splits into extra extracted lines — decide per case (fold a
  prose pair into a merge; keep a verse block as separate `{p}` lines). ALWAYS confirm
  the extracted body count p-by-p against data/src_epub.
- Faithful numbering gaps/anomalies (NOT errors): Part Three skips ch7, splits ch10 into
  (上)/(下); 三面受敌 一往无前 titles two different chapters (ch14 and ch24); ch09 printed §五
  before §四; ch13 restarts its (一)–(五) numbering for the appended essay. Preserve and,
  where a reader would stumble, footnote.
- Expect a stray per-task branch at the top of every batch; consolidate onto
  claude/nameless-heroes per rule 2.
