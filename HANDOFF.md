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
Nameless Heroes B07

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once, then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05), B02 (ch06), B03 (ch07), B04 (ch08), B05 (ch09) and B06 (ch10 preface + ch11) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them.

Do Batch B07 = ch12 (ONE unit, 19,990 source chars): 第二章 人心叵测别有肺肠 "Chapter 2. Unfathomable Hearts, Hidden Designs" — the second chapter of PART TWO ("Disgrace at Hanoi"), continuing the 1939 Hanoi operation against Wang Jingwei. Read the last two pages of ch11 English (out/ch11_reading.md) for register + story continuity: at ch11's end Dai Li has flown back to Chongqing leaving Chen in charge at the Hanoi safe house with Fang Bingxi and Wang Luqiao, the task limited to surveillance; Chen holds a name-card for a mysterious high-level contact he alone is to meet, and reinforcements are trickling in. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch12 from data/src (13_index-split-000-0011.txt). DROP the running-header first line 英雄无名-陈恭澍 (drop=2: header + <h2> chapter title). Fix extractor-split paragraphs (a line whose last char is not in 。！？」）…— continues into the next; enumerated ；/： bullet or quoted-document lines are DELIBERATE separate <p> — confirm against the source HTML <p> count in data/src_epub). WATCH for source cuts (cf. ch08 L402) and misplaced-「 glitches (cf. ch09 L164, ch11 L56/L76) — leave visible, footnote per rule 4 only where a real cut. GREP the source for note markers (\[\d+\]) and record "none present"/any found in PROGRESS.md. Check the chapter HTML in data/src_epub for set-off formatting; ch06-ch11 had NONE — confirm for ch12.
2. Build data/zh/ch12.txt VERBATIM: extend scripts/clean_batch.py with ch12's drop/merge/heading spec (it verifies source characters are conserved, follows merge CHAINS for 3+-fragment splits). DETERMINE ch12's sub-heading pattern per source — ch11 used COUPLET-STYLE headings with NO number prefix (一道急急令飞渡万里关山 standalone; 只限于行踪监视与活动侦察 glued to a paragraph tail), UNLIKE ch06-09's numbered 一/二/三. Grep ch12's <p> boundaries and check for glued vs standalone headings; watch for out-of-sequence numbering (cf. ch09 §五 before §四). Write out/ch12_reading.md (## chapter title from book.json; ### sub-headings; one English paragraph per source body line), then run scripts/batch_artifacts.py ch12 (derives out/ch12_en.json FROM the reading.md and rewrites checks.json).
3. Translate to the FROZEN register (Chen's voice sheet + the character voice sheets are in HANDOFF). Consult glossary.json and authority.json BEFORE romanizing anything new; REUSE the settled renderings — the Juntong; Dai Li / Yunong (老板 "the Boss"); Wang Jingwei / 汪兆铭 Wang Zhaoming; 制裁 "sanction"; the Mauser "box-cannon"; the concessions; Chiang's titles 校长 Commandant / 领袖 Leader / 委员长 Generalissimo / 总裁 Director-General; 二楼/三楼 second/third floor; and the B06 Hanoi shelf (see carry-forward): Hanoi/Annam, the safe house = the "Hanoi operation" command post, the Kongming-cart cyclo, the Yan Telegram, the mysterious high-level contact. Part Two PRINCIPALS now: Chen(1), Dai Li(2), Wang Jingwei(3), Zheng Jiemin(4), Wang Tianmu(5), Fan Xing(6), 方炳西 Fang Bingxi(7), 王鲁翘 Wang Luqiao(8). New characters get a two-line voice sheet in HANDOFF. Render digitization glitches to plain sense and LIST them in PROGRESS.md.
4. Checks (per unit): verify_unit.py ch12 (parity + numbers with --noise data/noise.txt auto-found + anchors); check_align.py ch12; regenerate checks.json with scripts/batch_artifacts.py and run check_structure.py + check_content.py --config checks.json; qc_entities.py on a reconstructed bilingual (data/zh + out/ch12_en.json, `> zh` / en pairs — every glossary row needs a pinyin field); verify the TAIL against the source (rule 4 corollary). check_register.py --ref reference/B01_frozen.md out/ch12_reading.md ("shall" in Chen's narration is deliberate — do not de-formalize it; B06 ch11 ran 33%, verified). For numeric flags: carry real quantities in the English (spell clock times so the checker matches; make 二人/两位 explicit "the two [named]"; Republican years render as Gregorian — the checker auto-excuses via +1911), and NOISE only idioms/names/places/elided-tens/artifacts — add a commented B07 block to data/noise.txt.
5. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (do NOT re-note anything already noted in B01-B06 — the full list is in PROGRESS.md; e.g. the Yan Telegram, the Ume Kikan, Konoe, the Anti-Japanese Traitor-Killing Corps, the Kongming cart, 总裁/Director-General are all noted). Merge notes via apparatus_merge.py (numeric character references only; anchors verbatim substrings of the reading.md, in body text not headings — watch American-style period-inside-quote: anchor on the phrase WITHOUT the trailing "." to avoid a false miss). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field — NOT through apparatus_merge's flat-map path), with attestation status; flag any new principal cast principal: true. Confirm whether ch12 carries images.
6. Rebuild the EPUB, qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; write the voice sheet(s) and update HANDOFF.md; commit and push to claude/nameless-heroes.

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B08 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
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
  Jingwei. B06 gave the Author's Preface (ch10) and Chapter 1 (ch11): the summons,
  the flight to Hanoi, the safe house, Dai Li's surveillance-only briefing, and the
  Yan Telegram dissected. At ch11's end Chen is left in charge at Hanoi with Fang
  Bingxi and Wang Luqiao, holding a name-card for a mysterious high-level contact.
- **NEXT: B07 = ch12** 第二章 人心叵测别有肺肠 "Unfathomable Hearts, Hidden Designs".

## What is NEXT

- Batch B07 = ch12 (Part Two, Chapter 2, 19,990 chars). Kickoff is the paste-block
  at the top of this file. Runs to completion (no gate); ends by pasting the B08
  kickoff.
- The frozen register reference is `reference/B01_frozen.md`. Narrative sits at
  4.55-4.76 en/han; prefaces denser (~5.2). If later matter wants a different
  baseline, RAISE it, do not silently reset.
- Sub-heading pattern DIFFERS by chapter. Part One used numbered 一/二/三 (space- or
  、-style); ch11 (Part Two) used COUPLET-STYLE headings with NO number prefix
  (standalone and glued). Grep each new chapter to determine its pattern and set
  clean_batch's spec. Watch for out-of-sequence numbering (cf. ch09 §五 before §四).
- WATCH for source anomalies: cuts (ch08 L402), misplaced-「 glitches (ch09 L164,
  ch11 L56/L76), corrupt phrases (ch11 L69 我已经和他的爱, footnoted). Re-grep each
  batch's source for `\[\d+\]` note markers (none present through B06).

## Open items for the read-through / completion

- Feed decided renderings back to authority.json on completion: 军统 "the Juntong";
  蓝衣社 "the Blue Shirt Society"; 关东军 "the Kwantung Army"; and the B02-B06
  historical names (张宗昌, 蔡锷, 宋哲元, 段祺瑞, 孙传芳, 胡汉民, 张学良, 任应岐, 商震,
  于学忠, 吴佩孚, 佟麟阁, 杨虎城, 李大钊, 樊钟秀, 韩复榘, 刘郁芬, 王树常, 李培基,
  孙殿英, 庞炳勋, 李际春, 白坚武, 阎锡山, and the B06 set: 近卫文麿, 影佐祯昭, 高宗武,
  梅思平, 今井武夫, 林森, 张继, 吴敬恒, 陈布雷, 林柏生).
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
