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
Nameless Heroes B05

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once, then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05), B02 (ch06), B03 (ch07) and B04 (ch08) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them.

Do Batch B05 = ch09 ONLY (第四节 急功躁进铸成大错 "Section 4. Impatience Breeds a Grave Blunder", ~35,150 source chars). Part One, Section 4: the Shi Yousan (石友三) case of the winter of 1934, already PREVIEWED at the tail of ch08 — an over-hasty operation in the Tianjin Japanese concession that failed: the executors 先鸿霞 (Xian Hongxia, Wang Wen's boyhood friend and Shi Yousan's adjutant, already glossed provisional) and 老褚 (old Chu) were taken by the Japanese gendarmerie and lost; 史大川 (Shi Dachuan) escaped but left in anger over a misunderstanding; Shi Yousan, protected by the Japanese garrison commanders 多田骏/田代皖一郎, had his warrant cancelled and was given a government post, only to be executed for rebellion early in the War of Resistance. Read the last two pages of ch08 English for the seam (ch08 ends on this exact lead-in). Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch09 from data/src (10_index-split-000-0008.txt). DROP the running-header first line 英雄无名-陈恭澍. Fix extractor-split paragraphs (a line whose last char is not in 。！？」）…— continues into the next; the enumerated ；/： bullet lists are DELIBERATE separate <p> and must NOT be merged — confirm against the source HTML <p> count in data/src_epub). WATCH for source cuts like ch08's line 402 (a bullet that trails off mid-phrase into the next bullet — leave visible, do NOT merge, footnote per rule 4). GREP the source for note markers (\[\d+\]) and record "none present"/any found in PROGRESS.md. Check the chapter HTML in data/src_epub for set-off formatting; ch06/ch07/ch08 had NONE (plain narrative) — confirm.
2. Build data/zh/ch09.txt VERBATIM from data/src: extend scripts/clean_batch.py with ch09's drop/merge/heading spec (it verifies source characters are conserved). DETERMINE the sub-heading pattern per source: grep for the first (space-style "一 …" like ch06/ch08, or 、-style "一、…" like ch07) and for whether later numbered headings (二 三 …) are STANDALONE lines or GLUED to a paragraph tail (grep for a terminal 。/」 immediately followed by 二/三/四/五 + space); set clean_batch's `glued`/`standalone` spec accordingly. Write out/ch09_reading.md (## chapter title from book.json; one English paragraph per source body line), then run scripts/batch_artifacts.py ch09 (it derives out/ch09_en.json FROM the reading.md).
3. Translate to the FROZEN register (Chen's voice sheet + the character voice sheets are in HANDOFF; read the last two pages of ch08 English for the seam). Consult glossary.json and authority.json BEFORE romanizing anything new; REUSE the settled renderings (the Juntong; Dai Li / Yunong; Wang Tianmu / 王大哥 "Elder Brother Wang"; the Beiping/Tianjin Station; the Action/Intelligence/Military Group; 制裁 "sanction"; the Mauser "box-cannon"; the concessions and Tianjin geography; the Commandant/Leader/Generalissimo = Chiang; 二楼/三楼/四楼 = second/third/fourth floor). Carry forward: 石友三 Shi Yousan, 先鸿霞 Xian Hongxia, 老褚 old Chu, 史大川 Shi Dachuan, 王文 Wang Wen, 多田骏 Tada Hayao, 田代皖一郎 Tashiro Kan'ichirō (all in glossary.json). New characters get a two-line voice sheet in HANDOFF. Render digitization glitches to plain sense and LIST them in PROGRESS.md.
4. Checks: verify_unit.py ch09 (parity + numbers with --noise data/noise.txt + anchors — invoke as `verify_unit.py ch09`, it auto-finds data/noise.txt); check_align.py ch09; regenerate checks.json with scripts/batch_artifacts.py and run check_structure.py + check_content.py --config checks.json; qc_entities.py on a reconstructed bilingual (data/zh + out/ch09_en.json, `> zh` / en pairs); verify the TAIL against the source (rule 4 corollary). check_register.py --ref reference/B01_frozen.md out/ch09_reading.md ("shall" in Chen's narration is deliberate — do not de-formalize it; dialogue contractions are fine). The once-per-book blind double-translation (check 7) and back-translation sample (check 8) were done in B02; a spot re-check is enough. For numeric flags: carry real quantities in the English (spell clock times so the checker matches, e.g. "four forty-five"; make 二人/二位/两位 explicit "the two [named]"), and NOISE only idioms/names/places/elided-tens/artifacts — add a commented B05 block to data/noise.txt.
5. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (do NOT re-note anything already noted in B01/B02/B03/B04 — the full list is in PROGRESS.md; e.g. Shi Yousan, the Japanese concession, the Mauser, the Green Gang, the Tanggu Truce, the sanction euphemism, the Juntong, the Blue Shirt Society are all already noted). Merge notes via apparatus_merge.py (numeric character references only). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified — NOT through apparatus_merge's flat-map path), with attestation status; flag any new principal cast principal: true. Confirm ch09 carries no images.
6. Rebuild the EPUB, qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; write the voice sheet(s) and update HANDOFF.md; commit and push to claude/nameless-heroes.

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B06 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
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
  paragraphs; the Zhang Jingyao case in full. 11 notes (102 cumulative); 24
  glossary rows. All checks green; epubcheck 0/0/0. Detail in PROGRESS.md.
- **Batch B04 (ch08), Part One Section 3** ("Tangled Roots, a Substitute
  Sacrifice"). 461 paragraphs across six sub-sections — the longest unit so
  far; the Ji Hongchang case, the Wang Zixiang poison death, and the 9 Nov 1934
  Guomin Hotel shooting in which Liu Shaorang was killed by mistake. 12 notes
  (114 cumulative); 54 glossary rows. All checks green; epubcheck 0/0/0. EPUB
  now 8/43 chapters. Detail in PROGRESS.md ("Batch B04").

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` — derives data/zh/<id>.txt verbatim from data/src,
  applying per-unit drops/merges/heading-splits with a source-conservation
  check. Specs for ch06 (glued headings), ch07 (standalone), ch08 (one
  standalone + five glued; line 402 deliberately unmerged as a source cut).
- `scripts/batch_artifacts.py` — derives out/<id>_en.json FROM
  out/<id>_reading.md and writes checks.json. Author the reading.md; run this.
- `scripts/verify_unit.py <id>` — parity + numbers (auto-finds data/noise.txt;
  do NOT pass --noise, it is treated as a cid) + anchors. Run per unit.
- `scripts/check_content.py` (patched) — name_map skips "_"-prefixed glossary
  categories/entries.
- Glossary is authored/merged BY HAND into the SECTIONED file
  (people/organizations/places/terms), idempotent + re-read-verified.
  apparatus_merge's glossary path assumes a FLAT map and would corrupt the
  sectioned file; NOTES still go through apparatus_merge.py (numeric character
  references only).
- data/noise.txt carries the B01+B02+B03+B04 project noise rules (each with a
  comment line). Note the B04 lookbehind trick `(?<=五)两个房`: the auto-guard
  refuses to strip a pattern that begins with a numeral when a numeral
  precedes it, so an explicit lookbehind is the way to detach a glued count.
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches it;
  re-run setup.sh per session). setup.sh's ONE failing regression test ("hook
  stands down on template stub") is a KNOWN false alarm coupled to real (non-
  template) book state, not a defect; all other regression tests pass.

## Renderings settled / carry-forward

- 军统 / 军统局 -> "the Juntong" (DECIDED). 蓝衣社 -> "the Blue Shirt Society"
  (the enemy's exonym for the Lixingshe/Renaissance Society). 戴笠 Dai Li
  (courtesy Yunong); 汪精卫 Wang Jingwei; 北平 Beiping; 天津 Tianjin.
- Internal units: 力行社 the Lixingshe; 特务处 the Special Services Department;
  调查统计局 the Bureau of Investigation and Statistics; 站 Station / 区 District;
  复兴社 the Renaissance Society; 中统 the Zhongtong; 行动组 the Action Group;
  情报组 the Intelligence Group; 军事组 the Military Group; 督察 "inspector".
- Book's own idiom: 制裁 "sanction"; 绥靖 "pacification"; 戡乱 "suppression of
  the rebellion"; "bandits"; "traitors" for collaborators. Chiang's titles:
  校长 "the Commandant", 领袖 "the Leader", 委员长 "the Generalissimo". 期
  "class". 元/块 "yuan/dollar". Floors: 二楼/三楼/四楼 = "second/third/fourth
  floor", 楼底下/楼下 = "the ground floor".
- **B03 shelf (reuse; in glossary.json):** 王天木 = 王大哥 "Elder Brother Wang"
  / 王大嫂 "elder sister-in-law Wang" (cover "Zheng Shisong"). 东交民巷 "the
  Legation Quarter"; 六国饭店 "the Grand Hôtel des Wagons-Lits"; 热河 "Rehe";
  关东军 "the Kwantung Army"; 满洲国 "Manchukuo"; 北平军分会 "the Beiping
  Military Branch". Brothel-quarter idiom (八大胡同, 清吟小班, 打茶围, etc.).
- **B04 shelf (reuse; in glossary.json):** 蓝衣社 "the Blue Shirt Society";
  青帮 "the Green Gang" (+ 开香堂 "opening the incense hall"); 塘沽协议 "the
  Tanggu Truce"; 察哈尔民众抗日同盟军 "the Chahar People's Anti-Japanese Allied
  Army" (renamed 抗日讨蒋军 "the Anti-Japanese, Chiang-Chastising Army"); 驳壳/
  盒子/木壳 "the Mauser 'box-cannon'" (C96); 红卫兵 "the Red Guards"; 毛婆江青
  "the Mao hag Jiang Qing". Tianjin geography: 国民大饭店 "the Guomin Hotel",
  交通旅馆 "the Jiaotong Hotel", 惠中饭店 "the Huizhong Hotel", 利顺德饭店 "the
  Lishunde Hotel" (Astor House), 小白楼 "Xiaobailou", 特别第一区 "the First
  Special District", 劝业场 "the Quanyechang", 紫竹林 "Zizhulin", 张家口
  "Zhangjiakou". Names: see PROGRESS.md B04 glossary list (王子襄, 王玉梅, 吕一民,
  吴萍, 王文, 郑恩普, 傅丹墀, 杨玉珊, 陈国瑞, 任应岐, 商震, 于学忠, 樊钟秀,
  靳云鹗, 吴佩孚, 佟麟阁, 杨虎城, 李大钊, 先鸿霞, 老褚, 史大川, 多田骏,
  田代皖一郎, and others). Japanese readings provisional — verify on recurrence.

## Voice sheet — CHEN GONGSHU (author / narrator)

- REGISTER: educated, formal, essayistic first person; grave and a touch
  archaic but not stilted. Long semicolon-joined clauses; four-character idiom
  and classical allusion used freely and footnoted when they carry weight.
- STANCE: self-justifying yet self-effacing; insists on truthfulness, admits
  his blunders (the Liu Shaorang error, the "though I did not kill Boren"
  confession over Wang Zixiang); tender toward dead comrades, bitter and
  scornful toward the enemy; rhetorical questions and exclamations for emphasis.
- IDIOM: unbroken Nationalist idiom of 1980s Taiwan. Preserve it; footnote
  where a claim is contested. He quotes enemy documents (the "General Ji
  Hongchang" booklet) at length in order to rebut them point by point — keep
  the quoted propaganda's inflated register distinct from his own dry rebuttal.
- FORMALITY: courteous 先生 "Mr." for superiors/elders; warm 兄 "brother" for
  colleagues; 爷 "Master" address-forms (郑三爷 "Third Master Zheng"). Chen's
  narrating "shall" is DELIBERATE — do not de-formalize it; check_register
  flags it informationally (B04 ran at 55%, verified deliberate).
- Ratio ~4.5-4.7 en/han in narrative (ch06 4.55, ch07 4.62, ch08 4.70; the
  heavy quoted-document matter runs a touch looser). Keep the semicolon rhythm.

## Voice sheets — principal & recurring cast

- **DAI LI (戴雨农 / Mr. Dai).** Warm and informal off duty, abrupt and close-
  mouthed on business; tests a man sideways; never boasts. In B04, reasonable
  and mindful of old ties (the labored report saving Wang Tianmu's life),
  "generous and forbearing, not so stern and unfeeling as rumor made him."
- **ZHENG JIEMIN (郑介民 / Mr. Zheng).** Educated, urbane, the theorist;
  measured, reasoned instructions; composed under pressure. By B04 recalled to
  Nanjing (off the North China stage).
- **WANG TIANMU (王天木 / 王大哥 "Elder Brother Wang").** The operational
  planner: worldly, cool, terse decisive speech; loyalties turn ambiguous later
  (Hanoi). In B04 he is quietly removed from the board (the "Case of the Corpse
  in the Trunk"; Dai gets him a life sentence to save him). Keep him unsentimental.
- **FAN XING (范行).** The enigma: silver-tongued, evasive, literary talk and
  never politics; the Beiping Station's intelligence pillar (his "Great Red
  Building" tip in B04 went unread at the time). Render his charm and the
  narrator's steady suspicion side by side; do not tip the mystery.
- **BAI SHIWEI (白世维).** The gunman of the Zhang Jingyao case; in B04 chief of
  the Beiping Station Action Group, but he plans and does not come to Tianjin.
  Terse in action.
- **CHEN's B04 team (carry forward where they recur):**
  - **WANG WEN (王文, real name Wang Wenhan).** The new Beiping action man and
    the Ji-case gunman: solid, wholly genuine, a slight stammer (hence slow
    speech), quiet — "what should not be said he never adds a word to" — but
    high-spirited before a job and thorough after (declines the car so as to
    leave no license-plate trace). Terse, plain speech.
  - **WU PING (吴萍).** Tianjin Station veteran, Tianjin-born and knows the city
    "as the palm of his hand"; fond of guns; openhanded; the look-out/cover and
    driver. Steady, practical, a little sentimental (weeps for Wang Zixiang).
  - **LÜ YIMIN (吕一民).** The Intelligence Group chief: guarded, refined,
    "honest-looking," slight Tianjin accent; conservative about intelligence
    work's dignity; the patient developer of the Zheng Enpu line.
  - **YANG YUSHAN (杨玉珊).** The liaison who does the on-the-spot recon; cool
    nerve and quick wit (the rubber-ball ruse); thorough, checks her runner
    twice. Later marries Zheng Enpu.
  - **ZHENG ENPU (郑恩普 / "Third Master Zheng").** Scrupulous, "steady" (not
    deep or sly), a man good as gold at his word; sympathetic to Ji at first and
    slow to be persuaded; "openhanded," widely respected.
  - **WANG ZIXIANG (王子襄, Dr.).** Pure-hearted, ardent, generous physician-
    turned-agent; a gift for the work but green; tries poisons on himself with
    "perfect composure" — which kills him. Chen's "nameless hero I revere the
    most." (Dies in B04.)

## Where the book stands

- Front matter (B01); the story opens (B02, ch06): 1931 audience with Chiang,
  the Special Research Class, Dai Li, the Honggongci class, the Beiping Station,
  the Fan Xing mystery, Dai's 1933 inspection.
- **B03 (ch07):** the Zhang Jingyao case in full (7 May 1933), and a long coda.
- **B04 (ch08):** the Ji Hongchang case. Autumn 1933 the Action Groups are
  enlarged; a Green-Gang false alarm; Wang Tianmu is quietly removed and Wang
  Zixiang made Tianjin chief, then dies testing a poison. Through 1934, sanction
  orders for Shi Yousan, Ji Hongchang, Zhang Bi; the fugitive Ji (routed from
  the Chahar alliance) is tracked via the Zheng Enpu / Fu Danchi line to the
  Guomin Hotel; a last-minute venue switch (Jiaotong → Guomin) and a change of
  mahjong seats mean Wang Wen's three shots kill Liu Shaorang, a Southwest KMT
  delegate, by mistake (李代桃僵); Ji only grazed. Long coda: the newspaper
  reports, the point-by-point rebuttal of the 1979 Communist booklet, Ji's
  extradition and execution (with Ren Yingqi) on 24 Nov 1934, his full biography,
  and the Zhengzhou grave's later desecration in the Cultural Revolution. Ends
  on the lead-in to the Shi Yousan case (ch09).

## What is NEXT

- Batch B05 = ch09 (Part One, Section 4, 急功躁进铸成大错, ~35,150 chars): the
  Shi Yousan case of winter 1934, already PREVIEWED at the ch08 tail — a hasty
  failed operation; the executors Xian Hongxia and old Chu lost to the Japanese
  gendarmerie, Shi Dachuan's angry departure, Shi Yousan's protection by the
  Japanese and later execution. Kickoff is the paste-block at the top of this
  file. Runs to completion (no gate); ends by pasting the B06 kickoff.
- The frozen register reference is `reference/B01_frozen.md`. Narrative sits at
  4.55-4.70 en/han; if later matter wants a different baseline, RAISE it, do not
  silently reset.
- Sub-heading pattern DIFFERS by chapter (ch06 space-style + glued; ch07 、-style
  + standalone; ch08 space-style, 一 standalone + 二–六 glued). Grep ch09 to
  determine its pattern and set clean_batch's spec.
- WATCH for source cuts (ch08 line 402 trailed off mid-bullet into the next
  bullet — left unmerged and footnoted per rule 4). Re-grep each batch's source
  for \[\d+\] note markers (none present through B04).

## Open items for the read-through / completion

- Feed decided renderings back to authority.json on completion: 军统 "the
  Juntong"; 蓝衣社 "the Blue Shirt Society"; 关东军 "the Kwantung Army"; and the
  B02/B03/B04 historical names (张宗昌, 蔡锷, 宋哲元, 段祺瑞, 孙传芳, 胡汉民,
  张学良, 任应岐, 商震, 于学忠, 吴佩孚, 佟麟阁, 杨虎城, 李大钊, 樊钟秀).
- Japanese name readings to verify when the men recur (多田骏 Tada Hayao,
  田代皖一郎 Tashiro Kan'ichirō, 山本荣治, 大冢清, 中岛信一, 冈村).
- Stray source glyphs still to resolve in later batches: trailing 杀 on the
  ch22 title; 寿张为幻 in the ch16 title; 毛酋 in a ch36 section title.
- Whether "Disgrace at Hanoi" survives as the Part Two title after the ch10
  preface is translated (Chen rejected 河内刺汪).
- Provisional romanizations to firm up when sources allow (see glossary
  `provisional` rows, incl. the B04 agents 吕一民, 吴萍, 王文, 郑恩普, 杨玉珊,
  先鸿霞, 史大川, and the redacted poison "X霜" in ch08 §2 src 148).

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01–B04 builds. Source is a clean
  digital EPUB, predominantly simplified with residual variant glyphs and
  pervasive digitization glitches (list them, render to plain sense, do not
  footnote mechanical typos). B01-B04 glitch lists are in PROGRESS.md.
- Running-header line 英雄无名-陈恭澍 opens all 43 content files: drop it (drop=2
  in each clean_batch spec, header + <h2> section title).
- Enumerated ；/： bullet lists in the source are DELIBERATE separate <p> — do
  NOT merge them; only genuine mid-phrase splits (last char not terminal)
  merge. Confirm against the source HTML <p> count. And beware source CUTS (a
  bullet that trails off mid-phrase, as ch08 line 402): leave unmerged, footnote.
- Faithful numbering gaps (NOT errors): Part Three skips ch7, splits ch10 into
  (上)/(下); 三面受敌 一往无前 titles two different chapters.
- Expect a stray per-task branch at the top of every batch; consolidate onto
  claude/nameless-heroes per rule 2.
