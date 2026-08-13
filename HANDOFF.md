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
Nameless Heroes B08

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once, then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05), B02 (ch06), B03 (ch07), B04 (ch08), B05 (ch09), B06 (ch10 preface + ch11) and B07 (ch12) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them.

Do Batch B08 = ch13 (ONE unit, 35,117 source chars): 第三章 波诡云谲 风雨欲来 "Chapter 3. Treacherous Tides, a Gathering Storm" — the third chapter of PART TWO ("Disgrace at Hanoi"), continuing the 1939 Hanoi operation against Wang Jingwei. This is a LONG chapter (the largest of Part Two so far) — budget accordingly. Read the last two pages of ch12 English (out/ch12_reading.md) for register + story continuity: at ch12's end Chen is in charge at the Hanoi safe house with the team filling out (Fang Bingxi, Wang Luqiao, then Cen Jiazhuo and Yu Lexing), a "special personage" is secretly helping (deliberately unnamed in the book, "to keep the larger good whole"), rumors spread that Wang may leave Vietnam, and Dai Li has had a large quantity of arms and ammunition sent ahead as "a first move" — with an explicit order to make ready but on NO account act rashly until an order comes. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch13 from data/src (14_index-split-000-0012.txt). DROP the running-header first line 英雄无名-陈恭澍 and CONFIRM the drop count against the source XHTML (ch12 was drop=2 = header + <h2>; ch10 was drop=3). Fix extractor-split paragraphs (a line whose last char is not in 。！？」）…— continues into the next — AND watch the ch12 trap: a line ending in 」 can STILL be a mid-phrase split if a bracketed term like 「用五」先生 is broken across the closing bracket, so re-check any 」-ending line whose next line begins mid-phrase). Enumerated ；/： bullet or quoted-document lines are DELIBERATE separate <p> — confirm against the source HTML <p> count in data/src_epub. WATCH for source cuts (cf. ch08 L402), misplaced-「 glitches (cf. ch09 L164, ch11 L56/L76), and an in-text "(本章完)"/coda pattern (cf. ch12) — leave visible, footnote per rule 4 only where a real cut. GREP the source for note markers (\[\d+\]) and record "none present"/any found in PROGRESS.md. Check the chapter HTML in data/src_epub for set-off formatting; ch06-ch12 had NONE — confirm for ch13.
2. Build data/zh/ch13.txt VERBATIM: extend scripts/clean_batch.py with ch13's drop/merge/heading spec (it verifies source characters are conserved, follows merge CHAINS for 3+-fragment splits). DETERMINE ch13's sub-heading pattern per source — Part Two has used THREE styles so far: ch11 couplet-style with NO number prefix; ch12 numbered-in-parens (一)/(二)/(三). Grep ch13's <p> boundaries and check for glued vs standalone headings and the numbering style; watch for out-of-sequence numbering (cf. ch09 §五 before §四). Write out/ch13_reading.md (## chapter title from book.json; ### sub-headings; one English paragraph per source body line), then run scripts/batch_artifacts.py ch13 (derives out/ch13_en.json FROM the reading.md and rewrites checks.json).
3. Translate to the FROZEN register (Chen's voice sheet + the character voice sheets are in HANDOFF). Consult glossary.json and authority.json BEFORE romanizing anything new; REUSE the settled renderings — the Juntong; Dai Li / Yunong (老板 "the Boss"); Wang Jingwei / 汪兆铭 Wang Zhaoming; 制裁 "sanction"; the Mauser "box-cannon"; Chiang's titles 校长 Commandant / 领袖 Leader / 委员长 Generalissimo / 总裁 Director-General (and 总理 "the Party Leader" = Sun Yat-sen, NOT glossaried — see note); 二楼/三楼 second/third floor; the B06 Hanoi shelf; and the B07 additions (see carry-forward): Konoe's "New Order in East Asia", the "East Asian Cooperative Body", 支那 = "Shina", the Five Ministers' Conference, the Kōain, the Tanaka Memorial, the Yunnan–Vietnam railway, Cen Jiazhuo, Yu Lexing, Zhou Fohai, Chen Gongbo, and the Hanoi team as "the Eighteen Arhats". Part Two PRINCIPALS: Chen(1), Dai Li(2), Wang Jingwei(3), Zheng Jiemin(4), Wang Tianmu(5), Fan Xing(6), 方炳西 Fang Bingxi(7), 王鲁翘 Wang Luqiao(8). New characters get a two-line voice sheet in HANDOFF. Render digitization glitches to plain sense and LIST them in PROGRESS.md; render Republican years literally ("the twenty-eighth year") per the Part-Two/B06 convention (the checker matches the source numeral directly).
4. Checks (per unit): verify_unit.py ch13 (parity + numbers with --noise data/noise.txt auto-found + anchors); check_align.py ch13; regenerate checks.json with scripts/batch_artifacts.py and run check_structure.py --config checks.json + check_content.py --config checks.json; qc_entities.py on a reconstructed bilingual (data/zh body lines + out/ch13_en.json, `> zh` / en pairs — strip the ### heading lines; every glossary row needs a pinyin field); verify the TAIL against the source (rule 4 corollary). check_register.py --ref reference/B01_frozen.md out/ch13_reading.md ("shall" in Chen's narration and any quoted documents is deliberate — do not de-formalize it; B06/B07 ran 33%, verified). For numeric flags: carry real quantities in the English (spell clock times so the checker matches; render exact multi-digit figures as DIGITS so the checker composes them; make 二人/两位 explicit "the two [named]"; Republican years kept literal), and NOISE only idioms/names/places/elided-tens/archaic-numeral-forms/artifacts — add a commented B08 block to data/noise.txt.
5. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (do NOT re-note anything already noted in B01-B07 — the full list is in PROGRESS.md; e.g. Konoe, the New Order in East Asia, 支那/Shina, the Five Ministers' Conference, the Kōain, the Tanaka Memorial, the Twenty-One Demands, the Nine-Power Treaty, Tai'erzhuang, Long Yun, Sun Yat-sen as 总理 are all noted). Merge notes via apparatus_merge.py (numeric character references only; anchors verbatim substrings of the reading.md, in body text not headings — watch American-style period-inside-quote: anchor on the phrase WITHOUT the trailing "." to avoid a false miss). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field — NOT through apparatus_merge's flat-map path), with attestation status; flag any new principal cast principal: true. Confirm whether ch13 carries images.
6. Rebuild the EPUB, qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; write the voice sheet(s) and update HANDOFF.md; commit and push to claude/nameless-heroes.

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B09 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
```

## What is DONE (do not redo)

- **Step 0 (survey).** Ingest + book.json (43 chapters, 5 TOC parts) +
  skeleton EPUB. See the survey section of PROGRESS.md.
- **Batch B01 (ch01-ch05), the front matter.** 67 notes. **VOICE GATE PASSED:**
  the B01 front matter is the FROZEN register reference (`reference/B01_frozen.md`)
  for `check_register.py --ref` from B02 on.
- **Batch B02 (ch06), Part One Section 1.** 322 paragraphs; 24 notes; 17
  glossary rows. The once-per-book blind double-translation and back-translation
  samples were done here.
- **Batch B03 (ch07), Part One Section 2.** 362 paragraphs; the Zhang Jingyao
  case. 11 notes; 24 glossary rows.
- **Batch B04 (ch08), Part One Section 3.** 461 paragraphs; the Ji Hongchang case,
  the Wang Zixiang poison death, the 9 Nov 1934 Guomin Hotel shooting. 12 notes;
  54 glossary rows.
- **Batch B05 (ch09), Part One Section 4.** 332 paragraphs; the Shi Yousan case of
  winter 1934. 9 notes; 72 glossary rows. **Part One COMPLETE.**
- **Batch B06 (ch10 + ch11), Part Two opens.** ch10 = the Part Two Author's Preface
  (26 paras); ch11 = "Bloodshed Against the Enemy" (87 paras, 2 couplet-style
  sub-headings): the North China martyrs eulogized (Zeng Che, Wang Wen), the
  summons to Hong Kong, the flight to Hanoi with Dai Li and Wang Luqiao, the safe
  house set up by Fang Bingxi, Dai's night briefing (surveillance only), and the
  full text of Wang's "Yan Telegram" with Chen's line-by-line rebuttal and the
  Nationalist expulsion resolution. 14 notes (137 cumulative); 59 glossary rows.
  All checks green; epubcheck 0/0/0. EPUB now **11/43 chapters**. **Part Two title
  question RESOLVED: keep "Disgrace at Hanoi"** (the source's own banner 河内辱命;
  河内汪案始末 is only the constituent book-title, on the preface). Detail in
  PROGRESS.md ("Batch B06").
- **Batch B07 (ch12), Part Two Chapter 2.** 第二章 人心叵测别有肺肠 "Unfathomable
  Hearts, Hidden Designs" (131 paras, 3 numbered-in-parens sub-headings). The Hanoi
  team fills out (Cen Jiazhuo, Yu Lexing arrive); the chapter gives WHOLE the two
  long political documents circulated as "instruction" — Konoe's third statement
  (22 Dec) and Chiang's 9,000-char address "Exposing the Enemy State's Plot" (26
  Dec) — then Chen's insistence, backed by Chen Bulei's memoir, the Zhu Zijia
  (Jin Xiongbai) memoir, and the anonymous "Yongwu" diary, that the Juntong had NO
  advance intelligence of Wang's collusion. 16 notes (153 cumulative); 40 glossary
  rows. All checks green; epubcheck 0/0/0. EPUB now **12/43 chapters**. Detail in
  PROGRESS.md ("Batch B07").

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` — derives data/zh/<id>.txt verbatim from data/src,
  applying per-unit drops/merges/heading-splits with a source-conservation check.
  Specs for ch01-ch11. Merge logic FOLLOWS CHAINS (a `<p>` split into 3+ fragments
  is rejoined whole); plain pairs are a chain of length one. **drop is variable:**
  most chapters drop=2 (header + one heading); ch01 drop=3 (header + h1 + h2);
  ch10 drop=3 (header + the Part banner `<h1>` + the chapter `<h3>`).
- `scripts/batch_artifacts.py` — derives out/<id>_en.json FROM out/<id>_reading.md
  and writes checks.json. Author the reading.md; run this (accepts multiple ids).
- `scripts/verify_unit.py <id>` — parity + numbers (auto-finds data/noise.txt; do
  NOT pass --noise, it is treated as a cid) + anchors. Run per unit.
- `scripts/check_content.py` (patched) — name_map skips "_"-prefixed glossary
  categories/entries.
- Glossary is authored/merged BY HAND into the SECTIONED file
  (people/organizations/places/terms), idempotent + re-read-verified. **Every row
  MUST carry a `pinyin` field** — `qc_entities.py` does `rec["pinyin"]` and will
  KeyError otherwise. apparatus_merge's glossary path assumes a FLAT map and would
  corrupt the sectioned file; NOTES still go through apparatus_merge.py (numeric
  character references only; anchors verbatim in body text, not headings).
- **Note-anchor gotcha (B06):** with American-style punctuation the period sits
  INSIDE the closing quote (`Corps."`), so an anchor ending `Corps"` fails as a
  false miss. Anchor on the phrase up to a safe interior point, not across the
  final `."`.
- data/noise.txt carries the B01-B06 project noise rules (each with a comment
  line). Republican years are carried as Gregorian and auto-excused by the checker
  (`+1911`); never noise a year. Elided-tens (十二、三 / 三、四十) and hyperbolic
  round numbers (不远千里 / 百万计) are noised as artifacts; the value stays in the
  English.
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches it;
  re-run setup.sh per session). setup.sh's ONE failing regression test ("hook
  stands down on template stub") is a KNOWN false alarm coupled to real (non-
  template) book state, not a defect; all other regression tests pass.

## Renderings settled / carry-forward

- 军统 / 军统局 -> "the Juntong" (DECIDED). 蓝衣社 -> "the Blue Shirt Society".
  戴笠 Dai Li (courtesy Yunong; 老板/戴老板 "the Boss"); 汪精卫 Wang Jingwei
  (原名 汪兆铭 "Wang Zhaoming"); 北平 Beiping; 天津 Tianjin.
- Internal units: 力行社 the Lixingshe; 特务处 the Special Services Department;
  调查统计局 the Bureau of Investigation and Statistics; 站 Station / 区 District;
  复兴社 the Renaissance Society; 中统 the Zhongtong; 行动组 the Action Group;
  情报组 the Intelligence Group; 军事组 the Military Group; 督察 "inspector".
- Book's own idiom: 制裁 "sanction"; 绥靖 "pacification"; 戡乱 "suppression of
  the rebellion"; "bandits"; "traitors" for collaborators. Chiang's titles:
  校长 "the Commandant", 领袖 "the Leader", 委员长 "the Generalissimo", 总裁 "the
  Director-General" (party head; Wang = 副总裁 "Vice-Director-General"). 期
  "class". 元/块 "yuan/dollar". Floors: 二楼/三楼/四楼 = "second/third/fourth
  floor", 楼底下/楼下 = "the ground floor".
- **B03 shelf (reuse; in glossary.json):** 王天木 = 王大哥 "Elder Brother Wang".
  东交民巷 "the Legation Quarter"; 六国饭店 "the Grand Hôtel des Wagons-Lits"; 热河
  "Rehe"; 关东军 "the Kwantung Army"; 满洲国 "Manchukuo"; 北平军分会 "the Beiping
  Military Branch".
- **B04 shelf (reuse; in glossary.json):** 青帮 "the Green Gang" (+ 开香堂
  "opening the incense hall"); 塘沽协议 "the Tanggu Truce"; 察哈尔民众抗日同盟军 "the
  Chahar People's Anti-Japanese Allied Army"; 驳壳/盒子/木壳 "the Mauser
  'box-cannon'" (C96); 红卫兵 "the Red Guards". Tianjin geography (国民大饭店,
  交通旅馆, 惠中饭店, 利顺德饭店 Astor House, 小白楼, 特别第一区, 劝业场, 紫竹林,
  张家口).
- **B05 shelf (reuse; in glossary.json):** 石友三 Shi Yousan; 王文 Wang Wen; 张炎元/
  张炳华 Zhang Yanyuan (given Binghua); 何应钦 "Minister He"; 阎锡山 Yan Xishan;
  韩复矩 Han Fuju; 土肥原贤二 Doihara Kenji; 多田骏 Tada Hayao / 田代皖一郎 Tashiro
  Kan'ichirō (Japanese readings provisional). 甲/乙/丙地 "Site A/B/C".
- **B06 shelf (reuse; in glossary.json):** 河内 Hanoi; 安南 Annam; 越南 Vietnam;
  重庆 Chongqing; 跑马地 Happy Valley / 半山 the Mid-Levels / 薄扶林道 Pok Fu Lam
  Road / 山光饭店 the Sanguang Hotel (Hong Kong); 塘沽 Tanggu; 吴淞口 Wusong; 黄浦江
  the Huangpu; 冀东 East Hebei; 虹口 Hongkou. 曾澈 Zeng Che; 方炳西 Fang Bingxi
  (**principal**); 王鲁翘 Wang Luqiao (**principal**); 齐庆斌 Qi Qingbin; 陈资一 Chen
  Ziyi; 周世光 Zhou Shiguang; 胡永荃 Hu Yongquan; 陈璧君 Chen Bijun; 陈春圃 Chen
  Chunpu; 李士群 Li Shiqun / 叶吉卿 Ye Jiqing. Japanese: 近卫文麿 Konoe Fumimaro;
  影佐祯昭 Kagesa Sadaaki; 今井武夫 Imai Takeo; 晴气庆胤 Haruke Yoshitane; 伊藤芳男
  Itō Yoshio (readings provisional). Negotiators: 高宗武 Gao Zongwu; 梅思平 Mei
  Siping; 林柏生 Lin Baisheng. Nationalist elders: 林森 Lin Sen; 张继 Zhang Ji;
  吴敬恒 Wu Jingheng (Zhihui); 陈布雷 Chen Bulei. Orgs: 滦榆游击总部 the Luan-Yu
  Guerrilla Command; 抗日杀奸团 the Anti-Japanese Traitor-Killing Corps (抗团); 梅机关
  the Ume Kikan; 满铁株式会社 the South Manchuria Railway Company; 国民参政会 the
  People's Political Council; 天津区 the Tianjin District; 太古公司 Butterfield &
  Swire; 怡和洋行 Jardine Matheson; 渣华公司 the Java-China-Japan Line. Terms: 艳电
  the "Yan Telegram"; 和平三原则 the "Three Principles of Peace"; 孔明车 the "Kongming
  cart" (Indochina cyclo). Unresolved: 剑秋 "Jianqiu" (a 1932 Nanjing "elder
  brother", identity uncertain); the L69 source corruption 我已经和他的爱 (footnoted).
- **B07 shelf (reuse; in glossary.json):** Konoe's slogans 东亚新秩序 "New Order in East
  Asia"; 东亚协同体 "East Asian Cooperative Body"; 支那 rendered "Shina" (derogatory
  Japanese exonym, noted); 五相会议 "the Five Ministers' Conference"; 兴亚院 "the Kōain"
  (Asia Development Board); 对支院 "the Tai-Shi Board"; 田中奏折 "the Tanaka Memorial"
  (forgery); 二十一条款 "the Twenty-One Demands"; 九国公约 "the Nine-Power Treaty"; 马关条约
  "the Treaty of Shimonoseki"; 国家总动员法 "the National General Mobilization Law".
  People: 岑家焯 Cen Jiazhuo; 余乐醒 Yu Lexing; 龙云 Long Yun; 有田 Arita (八郎); 平沼骐一郎
  Hiranuma Kiichirō; 田中义一 Tanaka Giichi; 广田 Hirota (弘毅); 重光葵 Shigemitsu Mamoru;
  袁世凯 Yuan Shikai; 周佛海 Zhou Fohai; 陈公博 Chen Gongbo; 金雄白 Jin Xiongbai / 朱子家 Zhu
  Zijia; 用五 "Yongwu" (identity unknown); 孙哲生 Sun Zhesheng (= 孙科); 蒋廷黻 Jiang Tingfu;
  张季鸾 Zhang Jiluan; 甘乃光 Gan Naiguang; 陈树人 Chen Shuren; 彦慈 Yanci; 彭学沛 Peng Xuepei.
  Places: 台儿庄 Tai'erzhuang; 张鼓峰 Zhanggufeng; 珊瑚坝 Shanhuba; 上清寺 Shangqingsi; 美专校街
  Meizhuanxiao Street; 北碚 Beibei; 桂林 Guilin; 滇越路 the Yunnan–Vietnam railway; 掌故 Zhanggu
  (HK magazine); 临澧训练班 the Linli Training Class. 总理 = "the Party Leader" (Sun Yat-sen),
  DECIDED but deliberately NOT glossaried (ambiguous with 内阁总理 "cabinet premier").

## Voice sheet — CHEN GONGSHU (author / narrator)

- REGISTER: educated, formal, essayistic first person; grave and a touch
  archaic but not stilted. Long semicolon-joined clauses; four-character idiom
  and classical allusion used freely and footnoted when they carry weight.
- STANCE: self-justifying yet self-effacing; insists on truthfulness, admits his
  blunders; tender toward dead comrades, bitter and scornful toward the enemy;
  rhetorical questions and exclamations for emphasis. In B06 he mourns the North
  China martyrs (Zeng Che, Wang Wen) at length and turns a long self-reproach on
  his own survival ("the good fortune is yours, and the ill must be mine").
- IDIOM: unbroken Nationalist idiom of 1980s Taiwan. Preserve it; footnote where a
  claim is contested. Keeps quoted enemy documents' inflated register distinct
  from his own dry rebuttal (the 艳电 rendered in period-diplomatic English, his
  gloss dry and scornful).
- FORMALITY: courteous 先生 "Mr." for superiors/elders; warm 兄 "Brother" for
  colleagues; 大哥 "elder brother" for close seniors. Chen's narrating "shall" is
  DELIBERATE — do not de-formalize it; check_register flags it informationally
  (B06 ch11 ran 33%, verified deliberate).
- Ratio ~4.55-4.76 en/han in narrative (ch11 4.76). Prefaces run denser (ch10
  5.18, like the B01 front matter). Keep the semicolon rhythm.

## Voice sheets — principal & recurring cast

- **DAI LI (戴雨农 / Mr. Dai / 老板 "the Boss").** Warm and informal off duty, abrupt
  and close-mouthed on business; tests a man sideways. In B06 (Hanoi) grave,
  overburdened, close-mouthed even with Chen: gives the mission in guarded,
  roundabout terms, rebukes Chen obliquely (the marriage-report jab), then softens;
  fixes only two tasks (surveillance of Wang; watch the Wang faction) and a lone
  mysterious contact Chen alone may meet. Flies back to Chongqing inside 48 hours.
- **FANG BINGXI (方炳西 / Brother Bingxi).** **Part Two principal (cast 7).** The
  advance man of the Hanoi team: reached Hanoi first, rented and fitted the safe
  house, bought the secondhand two-door Ford, speaks fluent French (smooths the
  customs). Selfless, seeing it through "without thought of name or place"; one of
  the operation's few survivors (Chen twice corrects himself on whether Bingxi is
  still living — a poignant late insertion). Quiet, competent, off-stage-practical.
- **WANG LUQIAO (王鲁翘 / Luqiao).** **Part Two principal (cast 8).** Shandong man,
  police-academy graduate, ex-bodyguard of Dai Li; just off "a professional
  strong-arm man" in Guangxi. Trim and dashing, courteous and frank with Chen,
  careful not to say more than his place allows. Co-lead of the Hanoi action team.
- **WANG TIANMU (王天木 / 王大哥 "Elder Brother Wang").** The operational planner:
  worldly, cool, terse decisive speech. In B06 he holds the Luan-Yu Guerrilla
  Command while Chen goes to Hanoi. WATCH — his loyalty is tested later in the
  Hanoi affair; render him straight for now, do not tip it.
- **CEN JIAZHUO (岑家焯 / Senior Jiazhuo).** New in B07 (cast, not principal). A
  Guangdong man, Chen's Whampoa senior (third class), and once deputy head of the
  Nanjing training class's education section. Silent, steady, with a gift for
  command; sent to Hanoi to assist. Chen faults his younger self for consulting
  this elder in everything instead of sharing authority with him. Render him grave
  and unshowy.
- **YU LEXING (余乐醒 / Brother Lexing / Dr. Yu).** New in B07 (cast, not principal).
  Hunan man, France-trained doctor of chemistry, high in the Juntong (deputy
  director of the Linli Training Class under Dai Li); made the Hanoi unit's chief
  of staff and technical adviser. Tall, thin, lamp-eyed, prematurely grey, cigarette
  in hand; a brooding, over-thinking, narrow-hearted man of intense professional
  devotion. The analyst who lays out Japan's basic China-policy for the team.
- **ZENG CHE (曾澈).** Tianjin Station secretary → Tianjin District chief; led the
  抗团. Warm to Chen (calls him "Second Brother," never "chief"); martyred at
  Beiping in 1940 after 300+ days of torture, aged 27. A "nameless hero"; eulogized
  in ch11. (Now dead; carry forward only in memory.)
- **ZHENG JIEMIN (郑介民 / Mr. Zheng).** Educated, urbane, the theorist; measured,
  reasoned instructions. Off-stage in B06; may recur in the Hanoi/Shanghai theatres.
- **FAN XING (范行 / "Jiman").** The Beiping intelligence enigma; silver-tongued,
  evasive. By ch09's end moved (reportedly to Shanghai); may recur in Part Three.
  Render his charm and Chen's wariness side by side; do not tip the mystery.
- **Part-One team (mostly off-stage now):** WANG WEN 王文 (martyred at Beiping 1939,
  eulogized in ch11), WU PING 吴萍, LÜ YIMIN 吕一民, ZHENG ENPU 郑恩普, BAI SHIWEI
  白世维. See earlier HANDOFF/PROGRESS for their full sheets.

## Where the book stands

- Part One (北国锄奸, "Rooting Out Traitors in the North") is COMPLETE (B01-B05).
- **Part Two — "Disgrace at Hanoi" (河内辱命)** is UNDERWAY: the 1939 attempt on Wang
  Jingwei. B06 gave the Author's Preface (ch10) and Chapter 1 (ch11); B07 gave
  Chapter 2 (ch12): the two enemy/Chiang documents dissected and Chen's case that
  the Juntong had no advance word of Wang's collusion. At ch12's end Chen holds the
  Hanoi post with the team filling out (Fang Bingxi, Wang Luqiao, Cen Jiazhuo, Yu
  Lexing), a "special personage" secretly helping (unnamed), rumors that Wang may
  leave Vietnam, and Dai's arms sent ahead with a strict order: make ready, but do
  not act until commanded.
- **NEXT: B08 = ch13** 第三章 波诡云谲 风雨欲来 "Treacherous Tides, a Gathering Storm"
  (the storm the title names is the operation turning from surveillance to action).

## What is NEXT

- Batch B08 = ch13 (Part Two, Chapter 3, 35,117 chars — the largest of Part Two so
  far). Kickoff is the paste-block at the top of this file. Runs to completion (no
  gate); ends by pasting the B09 kickoff.
- The frozen register reference is `reference/B01_frozen.md`. Narrative sits at
  4.55-4.76 en/han; prefaces denser (~5.2); document-heavy chapters run higher
  (ch12 4.84, dominated by two long quoted texts). If later matter wants a different
  baseline, RAISE it, do not silently reset.
- Sub-heading pattern DIFFERS by chapter. THREE styles seen: Part One numbered
  一/二/三 (space- or 、-style); ch11 COUPLET-STYLE with NO number prefix; ch12
  numbered-in-parens (一)/(二)/(三). Grep each new chapter to determine its pattern
  and set clean_batch's spec. Watch for out-of-sequence numbering (cf. ch09 §五
  before §四).
- WATCH for source anomalies: cuts (ch08 L402), misplaced-「 glitches (ch09 L164,
  ch11 L56/L76), corrupt phrases (ch11 L69 我已经和他的爱, footnoted), the ch12
  「用五」先生 split hidden behind a terminal 」, and the ch12 in-text "(本章完)"/coda
  pattern (chapter marked "ended" mid-file, then a short set-off coda). Re-grep each
  batch's source for `\[\d+\]` note markers (none present through B07).

## Open items for the read-through / completion

- Feed decided renderings back to authority.json on completion: 军统 "the Juntong";
  蓝衣社 "the Blue Shirt Society"; 关东军 "the Kwantung Army"; and the B02-B06
  historical names (张宗昌, 蔡锷, 宋哲元, 段祺瑞, 孙传芳, 胡汉民, 张学良, 任应岐, 商震,
  于学忠, 吴佩孚, 佟麟阁, 杨虎城, 李大钊, 樊钟秀, 韩复榘, 刘郁芬, 王树常, 李培基,
  孙殿英, 庞炳勋, 李际春, 白坚武, 阎锡山, and the B06 set: 近卫文麿, 影佐祯昭, 高宗武,
  梅思平, 今井武夫, 林森, 张继, 吴敬恒, 陈布雷, 林柏生; and the B07 set: 龙云, 有田八郎,
  平沼骐一郎, 田中义一, 广田弘毅, 重光葵, 袁世凯, 孙科, 蒋廷黻, 周佛海, 陈公博, 金雄白).
- Japanese name readings to verify when the men recur (多田骏 Tada Hayao, 田代皖一郎
  Tashiro Kan'ichirō, 土肥原贤二 Doihara Kenji, 坂垣征四郎 Itagaki Seishirō, 近卫文麿
  Konoe Fumimaro, 影佐祯昭 Kagesa Sadaaki, 今井武夫 Imai Takeo, 晴气庆胤 Haruke
  Yoshitane, 中岛信一 Nakajima Shin'ichi, 伊藤芳男 Itō Yoshio).
- Identify 剑秋 "Jianqiu" (a 1932 Nanjing "elder brother" of Chen, dined with Dai Li;
  paired with 炳华 = Zhang Yanyuan) when sources allow.
- Stray source glyphs still to resolve in later batches: trailing 杀 on the ch22
  title; 寿张为幻 in the ch16 title; 毛酋 in a ch36 section title.
- Provisional romanizations to firm up when sources allow (see glossary
  `provisional` rows).

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01-B06 builds (0/0/0). Source is a
  clean digital EPUB, predominantly simplified with residual variant glyphs and
  pervasive digitization glitches (list them, render to plain sense, do not
  footnote mechanical typos). B01-B06 glitch lists are in PROGRESS.md.
- Running-header line 英雄无名-陈恭澍 opens all 43 content files: drop it (in each
  clean_batch spec). drop count is variable — most drop=2 (header + one heading);
  ch01 and ch10 drop=3 (an extra heading: a卷前+构想, or the Part banner + chapter
  title).
- Enumerated ；/： bullet lists and quoted-document lines in the source are
  DELIBERATE separate <p> — do NOT merge them; only genuine mid-phrase splits (last
  char not terminal) merge, and those can CHAIN across 3+ fragments. Confirm against
  the source HTML <p> count. Beware source CUTS and misplaced brackets.
- Faithful numbering gaps/anomalies (NOT errors): Part Three skips ch7, splits ch10
  into (上)/(下); 三面受敌 一往无前 titles two different chapters; ch09 printed §五
  before §四; ch11 cross-references a "fifth section" of Book One that (as collected)
  has four. Preserve and footnote.
- Expect a stray per-task branch at the top of every batch; consolidate onto
  claude/nameless-heroes per rule 2.
