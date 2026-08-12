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
Nameless Heroes B04

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once, then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05), B02 (ch06) and B03 (ch07) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them.

Do Batch B04 = ch08 ONLY (第三节 盘根错节 李代桃僵, ~36,344 source chars — the longest unit so far). Part One, Section 3: the Ji Hongchang (吉鸿昌) case — the 9 Nov 1934 shooting inside the Guomin Hotel (国民大饭店) in the Tianjin French Concession, the first clash with the Communists in North China, in which the wrong man was killed by mistake (李代桃僵 "a plum dies in the peach's place"; the man killed by error is 刘绍勷, already glossed provisional in glossary.json). Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch08 from data/src (09_index-split-000-0007.txt). DROP the running-header first line 英雄无名-陈恭澍. Fix extractor-split paragraphs (a line whose last char is not in 。！？」）…— continues into the next; the enumerated ；/： bullet lists are DELIBERATE separate <p> and must NOT be merged — confirm against the source HTML <p> count in data/src_epub). GREP the source for note markers (\[\d+\]) and record "none present"/any found in PROGRESS.md. Check the chapter HTML in data/src_epub for set-off formatting; ch06/ch07 had NONE (plain narrative) — confirm (no images/center/kt/duokan classes -> nothing to recover with scripts/apply_format_markers.py).
2. Build data/zh/ch08.txt VERBATIM from data/src: extend scripts/clean_batch.py with ch08's drop/merge/heading spec (it verifies source characters are conserved). The first sub-heading is space-style "一 煽扬赤焰的叛国者皆曰可杀" (like ch06). DETERMINE per source whether the later numbered sub-headings (二 三 …) are STANDALONE lines (as in ch07) or GLUED to a paragraph tail (as in ch06): grep for a terminal 。 immediately followed by 二/三/四/五 + space, and for standalone heading lines; handle each as clean_batch's `glued`/`standalone` spec. Write out/ch08_en.json + out/ch08_reading.md (## chapter title from book.json; one English paragraph per source body line). NOTE: batch_artifacts.py derives out/ch08_en.json FROM out/ch08_reading.md — author the reading.md, then run it.
3. Translate to the FROZEN register (Chen's voice sheet + the character voice sheets are in HANDOFF; read the last two pages of ch07 English for the seam — ch07 ended on this same Ji Hongchang lead-in). Consult glossary.json and authority.json BEFORE romanizing anything new; REUSE the settled renderings (the Juntong; Dai Li / Yunong; Zheng Jiemin; Wang Tianmu / cover Zheng Shisong = 王大哥 "Elder Brother Wang" / 王大嫂 "elder sister-in-law Wang"; Fan Xing; Bai Shiwei; Qi Nanpu; Yang Ying; He Yingqin; the Kwantung Army; Manchukuo; Beiping/Tianjin Station; 制裁 "sanction"; the Commandant/the Leader/the Generalissimo = Chiang; the numbered classes 期; the Nationalist idiom; 二楼/三楼/四楼 = second/third/fourth floor, 楼底下 = ground floor). New characters (Ji Hongchang and his circle now on the page as characters; the action team) get a two-line voice sheet in HANDOFF. Render digitization glitches to plain sense and LIST them in PROGRESS.md.
4. Checks: verify_unit.py ch08 (parity + numbers with --noise data/noise.txt + anchors) AS YOU GO; check_align.py; regenerate checks.json with scripts/batch_artifacts.py and run check_structure.py + check_content.py --config checks.json; qc_entities.py on a reconstructed bilingual (data/zh + out/ch08_en.json, `> zh` / en pairs); verify the TAIL against the source (rule 4 corollary — this is a long single unit, so the tail is where faithfulness fails). check_register.py --ref reference/B01_frozen.md out/ch08_reading.md ("shall" in Chen's narration is deliberate — do not de-formalize it; dialogue contractions are expected and fine). The once-per-book blind double-translation (check 7) and back-translation sample (check 8) were done in B02; a spot re-check is enough.
5. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (do NOT re-note anything already noted in B01/B02/B03 — the full list is in PROGRESS.md; e.g. Ji Hongchang, the Chahar anti-Japanese army, Feng Yuxiang, Shi Yousan, the Kwantung Army, Manchukuo, the Legation Quarter, the Grand Hôtel des Wagons-Lits, Tianjin, "sanction", the Juntong, the Lixingshe are all already noted). Add glossary rows with attestation status; flag any new principal cast principal: true. Figures: survey found only the cover (already placed); confirm ch08 carries no images.
6. Rebuild the EPUB, qa_epub.py until green, epubcheck if available; record all check results in PROGRESS.md; write the voice sheet(s) and update HANDOFF.md; commit and push to claude/nameless-heroes.

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B05 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
```

## What is DONE (do not redo)

- **Step 0 (survey).** Ingest + book.json (43 chapters, 5 TOC parts) +
  skeleton EPUB. See the survey section of PROGRESS.md.
- **Batch B01 (ch01-ch05), the front matter.** Foreword, three book
  introductions, Part One prefatory note. 67 notes. **VOICE GATE PASSED:** the
  B01 front matter is the FROZEN register reference (`reference/B01_frozen.md`)
  for `check_register.py --ref` from B02 on. Detail in PROGRESS.md.
- **Batch B02 (ch06), Part One Section 1** ("A Heavy Charge, Pressing
  Onward"). 322 paragraphs; 24 notes (91 cumulative); 17 glossary rows. The
  once-per-book blind double-translation and back-translation samples were done
  here. Detail in PROGRESS.md ("Batch B02").
- **Batch B03 (ch07), Part One Section 2** ("A Startling Debut"). 362
  paragraphs across four titled sub-sections; the Zhang Jingyao case in full.
  11 notes (102 cumulative); 24 glossary rows. All checks green; epubcheck
  0/0/0. EPUB now 7/43 chapters. Detail in PROGRESS.md ("Batch B03").

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` — derives data/zh/<id>.txt verbatim from data/src,
  applying per-unit drops/merges/heading-splits with a source-conservation
  check. ch06 spec (glued headings), ch07 spec (standalone headings, one merge).
- `scripts/batch_artifacts.py` — derives out/<id>_en.json FROM
  out/<id>_reading.md and writes checks.json. Author the reading.md; run this.
- `scripts/check_content.py` (patched) — name_map skips "_"-prefixed glossary
  categories/entries.
- Glossary is authored/merged BY HAND into the SECTIONED file
  (people/organizations/places/terms), idempotent + re-read-verified.
  apparatus_merge's glossary path assumes a FLAT map and would corrupt the
  sectioned file; NOTES still go through apparatus_merge.py (numeric character
  references only).
- data/noise.txt carries the B01+B02+B03 project noise rules.
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches it;
  re-run setup.sh per session). setup.sh's ONE failing regression test ("hook
  stands down on template stub") is a KNOWN false alarm coupled to real (non-
  template) book state, not a defect; all other regression tests pass.

## Renderings settled / carry-forward

- 军统 / 军统局 -> "the Juntong" (DECIDED). Agreed shelf: 戴笠 Dai Li (courtesy
  Yunong); 汪精卫 Wang Jingwei; 北平 Beiping; 天津 Tianjin.
- Institutions: 力行社 the Lixingshe; 特务处 the Special Services Department;
  调查统计局 the Bureau of Investigation and Statistics; 站 Station / 区 District;
  复兴社 the Renaissance Society; 中统 the Zhongtong; 革命军人同志会 "the Military
  Association" (军会), 革命青年同志会 "the Youth Association" (青会).
- Book's own terms kept as idiom: 制裁 "sanction"; 绥靖 "pacification"; 戡乱
  "suppression of the rebellion"; "bandits"/"the bandit chief Mao" (毛酋);
  "traitors" for collaborators.
- Chiang's titles: 校长 "the Commandant", 领袖 "the Leader", 委员长 "the
  Generalissimo", 蒋公 "Mr. Chiang". 期 "class". 中央军校 "the Central Military
  Academy". 特派员 "special commissioner". 元 "yuan". 制裁令 "sanction order".
- **B03 settled shelf (reuse; in glossary.json):** 王天木 = 王大哥 "Elder Brother
  Wang" / 王大嫂 "elder sister-in-law Wang" (address forms; his cover "Zheng
  Shisong"). 督办 "Superintendent" (Zhang Jingyao's title as the tailor uses it).
  东交民巷 "the Legation Quarter"; 六国饭店 "the Grand Hôtel des Wagons-Lits";
  热河 "Rehe"; 关东军 "the Kwantung Army"; 满洲国 "Manchukuo"; 北平军分会 "the
  Beiping Military Branch"; 韩家潭 "Hanjiatan". Brothel-quarter idiom: 八大胡同
  "the Eight Great Hutongs"; 清吟小班 "pure-singing house"; 打茶围 "beating the
  tea-circle"; 逛窑子 "touring the brothels"; 花名 "flower-name". Floors: 二楼/
  三楼/四楼 = "second/third/fourth floor", 楼底下/楼下 = "the ground floor". The
  bathhouse 清华园 = "the Qinghuayuan". Names: 赵庭贵 Zhao Tinggui; 应元勋 Ying
  Yuanxun (tailor, "Manager Ying"); 飞龙 Feilong; 含春 Hanchun; 张宗昌 Zhang
  Zongchang; 蔡锷 Cai E; 小凤仙 Xiao Fengxian; 宋哲元 Song Zheyuan; 段祺瑞 Duan
  Qirui; 施从滨 Shi Congbin; 吉章简 Ji Zhangjian; 蒋孝先 Jiang Xiaoxian; 韩文焕
  Han Wenhuan; 丁昌 Ding Chang; 宣侠父 Xuan Xiafu; 南汉宸 Nan Hanchen. 常石谷/
  常世五 = "Chang Shigu"/"Chang Shiwu" (Zhang's hotel-register aliases).
- Japanese names are RECONSTRUCTED provisional readings (verify when they
  recur): 山本荣治 Yamamoto Eiji; 大冢清 Ōtsuka Kiyoshi; 中岛信一 Nakajima
  Shin'ichi; 冈村 Okamura. 坂垣征四郎 → Itagaki Seishirō (attested; source writes
  坂垣 for 板垣).

## Voice sheet — CHEN GONGSHU (author / narrator)

- REGISTER: educated, formal, essayistic first person; grave and a touch
  archaic but not stilted. Long semicolon-joined clauses; four-character idiom
  and classical allusion used freely and footnoted when they carry weight.
- STANCE: self-justifying yet self-effacing; insists on truthfulness, admits
  his blunders; tender toward dead comrades, bitter toward the enemy;
  rhetorical questions and exclamations for emphasis.
- IDIOM: unbroken Nationalist idiom of 1980s Taiwan (see settled renderings).
  Preserve it; footnote where a claim is contested.
- FORMALITY: courteous 先生 "Mr." for superiors/elders; warm 兄 "brother" for
  close colleagues. Chen's narrating "shall" (formal future) is DELIBERATE —
  do not de-formalize it; check_register flags it informationally.
- Ratio ~4.6-5.3 en/han; narrative runs terser (ch06 4.55, ch07 4.62). Merge
  clauses where English wants them merged; keep the semicolon rhythm.

## Voice sheets — principal & recurring cast

- **DAI LI (戴雨农 / Mr. Dai).** Warm and informal off duty, abrupt and close-
  mouthed on business; tests a man sideways; never boasts. Dislikes his men
  asking favors of others ("solve our own difficulties ourselves"). "Mr. Dai" /
  "Dai Yunong."
- **ZHENG JIEMIN (郑介民 / Mr. Zheng).** Educated, urbane, the theorist; measured,
  reasoned instructions (relays the sanction order in numbered points); composed
  under pressure, no note of urging; generous, treats subordinates as his own.
  Cantonese, Whampoa 2nd class. "Mr. Zheng" / "Mr. Jiemin."
- **WANG TIANMU (王天木 / 王大哥 "Elder Brother Wang").** Now the operational
  planner: worldly, cool, "the bamboo already formed in his breast"; sketches
  ruses (the Zhao-visit cover), tips stewards, manages the courtesan cover with
  easy patter; terse decisive speech ("I have a way; keep your nerve"). Loyalties
  turn ambiguous later (Hanoi) — keep him unsentimental. His men are 兄 "brother."
- **FAN XING (范行).** The enigma (introduced B02): silver-tongued, evasive,
  several languages, literary talk and never politics. Render his charm and the
  narrator's steady suspicion side by side; do not tip the mystery.
- **BAI SHIWEI (白世维 / 世维兄 "brother Shiwei", 白三爷 "Third Master Bai").**
  The gunman. Shandong, seventh-class academy; volunteers of himself; high in
  spirit before the act, then silent and unwilling to speak of it after ("a
  dead-knot of the mind"). Terse in action ("Gave him three of them; eight parts
  done for"). Later deputy chief of the Beiping police.
- **QI NANPU (戚南谱 / 老戚 "Old Qi").** Steady, unhurried, dutiful; the fixer who
  buys the tools ("buy a knife, isn't it just as serviceable?") and works the
  car and the ground; "for the public good and the private alike I have a duty
  I cannot shirk."
- **YANG YING (杨英).** "A bit of a mule's temper"; bookish and scholarly, but
  prick him and spur him and he will do what the others do.
- **FEILONG (飞龙) and YING YUANXUN (应元勋), B03.** Feilong: a Suzhou courtesan,
  chubby, soft Wu-accented Beiping speech, but crisp and quick-witted in answer
  ("Set your minds at rest, gentlemen; little schooling though I have had, I
  would never be so wanting in sense"). Ying Yuanxun: the Yingyuantai tailor,
  "Manager Ying" — first laconic and worldly-cautious, then jovial and generous
  (breaks into a great laugh, insists on a "banquet of consolation").

## Where the book stands

- Front matter (B01); the story opens (B02, ch06): 1931 audience with Chiang,
  the Special Research Class, meeting Dai Li, the Honggongci training class, the
  founding of the Beiping Station, the Fan Xing mystery, Dai's 1933 Beiping
  inspection.
- **B03 (ch07):** the Zhang Jingyao case in full. March 1933: the Kwantung Army
  takes Rehe; Itagaki, at Tianjin, buys up warlords to wreck North China. The
  Beiping/Tianjin units get a 7-day sanction order (relayed by Zheng Jiemin in a
  brothel-quarter parlor). Days of fruitless reconnaissance of the Legation
  Quarter and the Grand Hôtel des Wagons-Lits; the tailor Ying Yuanxun's
  unwitting tip fixes Zhang's third-floor rooms; Bai Shiwei kills him with three
  shots (7 May 1933). Long coda: the newspaper cover-name, Sun Chuanfang's flight
  and later killing by Shi Jianqiao, the "inside line" source and the
  Chiang-record passage, Chen's Lixingshe promotion, Dai Li's enlargement of the
  station (the Action Group under Bai Shiwei), and the human-interest tailpieces
  (the tailor's laugh; the courtesan Feilong). Ends on the lead-in to the Ji
  Hongchang case.

## What is NEXT

- Batch B04 = ch08 (Part One, Section 3, 盘根错节 李代桃僵, ~36,344 chars — the
  LONGEST unit so far): the Ji Hongchang case, the 9 Nov 1934 Guomin Hotel
  (Tianjin French Concession) shooting, the first clash with the Communists in
  North China, in which the wrong man (刘绍勷 Liu Shaorang, already glossed
  provisional) is killed by mistake (李代桃僵). Kickoff is the paste-block at the
  top of this file. Runs to completion (no gate); ends by pasting the B05 kickoff.
- The frozen register reference is `reference/B01_frozen.md`. ch06 sat at 4.55,
  ch07 at 4.62 en/han; if later narrative wants a different baseline, RAISE it,
  do not silently reset.
- Sub-heading pattern DIFFERS by chapter: ch06 glued the numbered headings to a
  paragraph tail; ch07 kept them standalone. ch08's first is space-style
  ("一 …") like ch06 — grep to determine whether the rest are glued or
  standalone and set clean_batch's spec accordingly.

## Open items for the read-through / completion

- Feed decided renderings back to authority.json on completion: 军统 "the
  Juntong" (resolving the three-way reconcile); 关东军 "the Kwantung Army"
  (already on shelf); and the B02/B03 historical names (张宗昌, 蔡锷, 宋哲元,
  段祺瑞, 孙传芳, 胡汉民, 张学良).
- Japanese name readings to verify when the men recur.
- Stray source glyphs still to resolve in later batches: trailing 杀 on the
  ch22 title; 寿张为幻 in the ch16 title; 毛酋 in a ch36 section title.
- Whether "Disgrace at Hanoi" survives as the Part Two title after the ch10
  preface is translated (Chen rejected 河内刺汪; the book was titled 河内汪案始末).
- Provisional romanizations to firm up when sources allow: 赵庭贵, 应元勋, 飞龙,
  含春, 蒋孝先, 韩文焕, 丁昌, 杨英, 戚南谱, 范行.

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01/B02/B03 builds. Source is a
  clean digital EPUB, predominantly simplified with residual variant glyphs and
  pervasive digitization glitches (list them, render to plain sense, do not
  footnote mechanical typos). B01/B02/B03 glitch lists are in PROGRESS.md.
- Running-header line 英雄无名-陈恭澍 opens all 43 content files: drop it (drop=2
  in each clean_batch spec, header + <h2> section title).
- Enumerated ；/： bullet lists in the source (Zheng's numbered instructions,
  the planning lists) are DELIBERATE separate <p> — do NOT merge them; only
  genuine mid-phrase splits (last char not terminal, continuing a sentence)
  merge. Confirm against the source HTML <p> count.
- Faithful numbering gaps (NOT errors): Part Three skips ch7, splits ch10 into
  (上)/(下); 三面受敌 一往无前 titles two different chapters.
- Expect a stray per-task branch at the top of every batch; consolidate onto
  claude/nameless-heroes per rule 2.
