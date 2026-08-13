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
Nameless Heroes B06

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once, then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05), B02 (ch06), B03 (ch07), B04 (ch08) and B05 (ch09) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them.

Do Batch B06 = ch10 + ch11 (TWO units, ~13,734 source chars): ch10 = 「河内汪案始末」自序 "Author's Preface: The Full Story of the Wang Case at Hanoi" (2,295 chars; the Part Two preface); ch11 = 第一章 浴血杀敌奋勇抗战 "Chapter 1. Bloodshed Against the Enemy, Valiant Resistance" (11,439 chars). This OPENS PART TWO, "Disgrace at Hanoi" — the story of the 1939 Juntong attempt on the arch-collaborator Wang Jingwei (汪精卫) at Hanoi. Part One (the North China rooting-out) is closed; expect a new cast. Read the last two pages of ch09 English (out/ch09_reading.md) only for register continuity — the story jumps to a new theatre and time. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch10 from data/src (11_index-split-000-0009.txt) and ch11 (12_index-split-000-0010.txt). DROP the running-header first line 英雄无名-陈恭澍 (drop=2: header + <h2>). Fix extractor-split paragraphs (a line whose last char is not in 。！？」）…— continues into the next; enumerated ；/： bullet lists are DELIBERATE separate <p> — confirm against the source HTML <p> count in data/src_epub). WATCH for source cuts like ch08 line 402 and the ch09 misplaced-「 glitch — leave visible, footnote per rule 4 where a real cut. GREP each source for note markers (\[\d+\]) and record "none present"/any found in PROGRESS.md. Check the chapter HTML in data/src_epub for set-off formatting; ch06-ch09 had NONE (plain narrative) — confirm for ch10/ch11.
2. Build data/zh/ch10.txt and data/zh/ch11.txt VERBATIM: extend scripts/clean_batch.py with each unit's drop/merge/heading spec (it verifies source characters are conserved, and now follows merge CHAINS for 3+-fragment splits). DETERMINE each chapter's sub-heading pattern per source (grep: space-style "一 …" like ch06/ch08/ch09, or 、-style "一、…" like ch07; and whether later numbers are STANDALONE lines or GLUED to a paragraph tail — grep for a terminal 。/」 immediately followed by 二/三 + space). ch10 is a short preface (may have no sub-headings). Watch for OUT-OF-SEQUENCE numbering as in ch09 (§五 printed before §四) — verify heading order against XHTML byte positions and preserve + footnote any anomaly. Write out/ch10_reading.md and out/ch11_reading.md (## chapter title from book.json; one English paragraph per source body line), then run scripts/batch_artifacts.py ch10 ch11 (it derives out/<id>_en.json FROM the reading.md and rewrites checks.json).
3. Translate to the FROZEN register (Chen's voice sheet + the character voice sheets are in HANDOFF). Consult glossary.json and authority.json BEFORE romanizing anything new; REUSE the settled renderings (the Juntong; Dai Li / Yunong; the Beiping/Tianjin Station; the Action/Intelligence/Military Group; 制裁 "sanction"; the Mauser "box-cannon"; the concessions; the Commandant/Leader/Generalissimo = Chiang; 二楼/三楼/四楼 = second/third/fourth floor). Carry forward the Part Two principals as they first appear: 汪精卫 Wang Jingwei (already glossed), and the Hanoi team when named. New characters get a two-line voice sheet in HANDOFF. Render digitization glitches to plain sense and LIST them in PROGRESS.md.
4. Checks (per unit): verify_unit.py ch10 and verify_unit.py ch11 (parity + numbers with --noise data/noise.txt auto-found + anchors); check_align.py; regenerate checks.json with scripts/batch_artifacts.py and run check_structure.py + check_content.py --config checks.json; qc_entities.py on a reconstructed bilingual (data/zh + out/<id>_en.json, `> zh` / en pairs — every glossary row needs a pinyin field); verify each unit's TAIL against the source (rule 4 corollary). check_register.py --ref reference/B01_frozen.md out/ch10_reading.md out/ch11_reading.md ("shall" in Chen's narration is deliberate — do not de-formalize it). For numeric flags: carry real quantities in the English (spell clock times so the checker matches; make 二人/两位 explicit "the two [named]"; Republican years render as Gregorian — the checker auto-excuses via +1911), and NOISE only idioms/names/places/elided-tens/artifacts — add a commented B06 block to data/noise.txt.
5. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (do NOT re-note anything already noted in B01-B05 — the full list is in PROGRESS.md; e.g. Wang Jingwei may already be glossed but check whether he carries a NOTE yet). Merge notes via apparatus_merge.py (numeric character references only; anchors verbatim substrings of the reading.md, in body text not headings). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field — NOT through apparatus_merge's flat-map path), with attestation status; flag any new principal cast principal: true. Confirm whether ch10/ch11 carry images.
6. Rebuild the EPUB, qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; write the voice sheet(s) and update HANDOFF.md; commit and push to claude/nameless-heroes.

Note the open question: the Part Two book title. book.json currently gives Part Two as "Disgrace at Hanoi" (from 河内辱命); the ch10 preface title is 「河内汪案始末」 "The Full Story of the Wang Case at Hanoi", and Chen is said to have rejected 河内刺汪. Read the ch10 preface and decide whether the Part Two heading should be revised; record the decision in PROGRESS.md and, if changed, update book.json's part label.

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B07 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
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
- **Batch B05 (ch09), Part One Section 4** ("Impatience Breeds a Grave Blunder").
  332 paragraphs; the Shi Yousan case of winter 1934 — the failed poisoning plot,
  Xian Hongxia and old Chu lost to the gendarmerie, Shi Dachuan's angry departure
  after Liu Zhaonan's embezzlement, Chen's flight to Guisui/Ulanhua and five
  months at the Nanjing "Site B," his restoration as Tianjin Station chief, and
  Shi Yousan's rehabilitation and later execution. 9 notes (123 cumulative); 72
  glossary rows. All checks green; epubcheck 0/0/0. EPUB now **9/43 chapters**.
  Detail in PROGRESS.md ("Batch B05"). **Part One is COMPLETE.**

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` — derives data/zh/<id>.txt verbatim from data/src,
  applying per-unit drops/merges/heading-splits with a source-conservation check.
  Specs for ch01-ch09. The merge logic now FOLLOWS CHAINS (a `<p>` the extractor
  split into 3+ fragments, e.g. ch09 89→90→91, is rejoined whole); plain pairs are
  a chain of length one, so ch01-ch08 output is unchanged.
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
- data/noise.txt carries the B01-B05 project noise rules (each with a comment
  line). Republican years are carried as Gregorian and auto-excused by the checker
  (`+1911`); never noise a year. The B04 lookbehind trick `(?<=五)两个房` detaches a
  glued count.
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches it;
  re-run setup.sh per session). setup.sh's ONE failing regression test ("hook
  stands down on template stub") is a KNOWN false alarm coupled to real (non-
  template) book state, not a defect; all other regression tests pass.

## Renderings settled / carry-forward

- 军统 / 军统局 -> "the Juntong" (DECIDED). 蓝衣社 -> "the Blue Shirt Society".
  戴笠 Dai Li (courtesy Yunong); 汪精卫 Wang Jingwei; 北平 Beiping; 天津 Tianjin.
- Internal units: 力行社 the Lixingshe; 特务处 the Special Services Department;
  调查统计局 the Bureau of Investigation and Statistics; 站 Station / 区 District;
  复兴社 the Renaissance Society; 中统 the Zhongtong; 行动组 the Action Group;
  情报组 the Intelligence Group; 军事组 the Military Group; 督察 "inspector".
- Book's own idiom: 制裁 "sanction"; 绥靖 "pacification"; 戡乱 "suppression of
  the rebellion"; "bandits"; "traitors" for collaborators. Chiang's titles:
  校长 "the Commandant", 领袖 "the Leader", 委员长 "the Generalissimo". 期
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
- **B05 shelf (reuse; in glossary.json):** 石友三 Shi Yousan; 先鸿霞 Xian Hongxia;
  老褚 old Chu; 史大川 Shi Dachuan; 刘兆南 Liu Zhaonan; 贺参谋 "Staff Officer He";
  王云孙 Wang Yunsun; 王平一 Wang Pingyi (inspector); 侯子川 Hou Zichuan; 连谋 Lian
  Mou (style Liangshun, "老连"); 张炎元/张炳华 Zhang Yanyuan (given Binghua, district
  chief); 毛万里 Mao Wanli; 陈恭治 Chen Gongzhi (Chen's elder brother); 何应钦
  "Minister He"; 阎锡山 Yan Xishan; 韩复矩 Han Fuju; 土肥原贤二 Doihara Kenji;
  多田骏 Tada Hayao / 田代皖一郎 Tashiro Kan'ichirō (Japanese readings provisional).
  Geography: 归绥 Guisui (frontier exile), 乌兰华 Ulanhua, 卧佛寺街 Wofosi Street,
  秋田街 Akita Street, 黄寺 the Yellow Temple, 世界日报 the Shijie Ribao, 二十九军
  the Twenty-ninth Army, 甲/乙/丙地 "Site A/B/C" (the Juntong's own detention houses).

## Voice sheet — CHEN GONGSHU (author / narrator)

- REGISTER: educated, formal, essayistic first person; grave and a touch
  archaic but not stilted. Long semicolon-joined clauses; four-character idiom
  and classical allusion used freely and footnoted when they carry weight.
- STANCE: self-justifying yet self-effacing; insists on truthfulness, admits his
  blunders (in B05 the whole Shi Yousan fiasco is confessed as "my dereliction
  and misjudgment," and the flight into exile told against himself); tender toward
  dead comrades, bitter and scornful toward the enemy; rhetorical questions and
  exclamations for emphasis.
- IDIOM: unbroken Nationalist idiom of 1980s Taiwan. Preserve it; footnote where a
  claim is contested. Keeps quoted enemy documents' inflated register distinct
  from his own dry rebuttal.
- FORMALITY: courteous 先生 "Mr." for superiors/elders; warm 兄 "Brother" for
  colleagues; 大哥 "elder brother" for close seniors (Zheng Enpu, Lian Liangshun).
  Chen's narrating "shall" is DELIBERATE — do not de-formalize it; check_register
  flags it informationally (B05 ran at 23%, verified deliberate).
- Ratio ~4.55-4.70 en/han in narrative (ch06 4.55, ch07 4.62, ch08 4.70, ch09
  4.66). Keep the semicolon rhythm.

## Voice sheets — principal & recurring cast

- **DAI LI (戴雨农 / Mr. Dai).** Warm and informal off duty, abrupt and close-
  mouthed on business; tests a man sideways. In B05, grave and face-conscious over
  the scandal, but in the end mild and forbearing at Chen's reckoning ("The state
  has its law, the household its rules"), giving him a year's confinement and then
  quietly restoring him — "generous, not so stern as rumor made him."
- **ZHENG JIEMIN (郑介民 / Mr. Zheng).** Educated, urbane, the theorist; measured,
  reasoned instructions. Off the North China stage by B04; his B05 dictum on the
  Fan Xing line — "Let it out long and long; draw it tight and tight" — shows the
  patient cast of mind. May recur in the Hanoi/Shanghai theatres.
- **WANG TIANMU (王天木 / 王大哥 "Elder Brother Wang").** The operational planner:
  worldly, cool, terse decisive speech; loyalties turn ambiguous later (Hanoi).
  WATCH for him in Part Two — the Hanoi affair is where his loyalty is tested.
- **FAN XING (范行 / sobriquet 纪曼 "Jiman").** The enigma: silver-tongued,
  evasive, literary talk and never politics; the Beiping Station's intelligence
  pillar. In B05, acting Beiping Station chief; loyal and warm to Chen in his
  disgrace ("Our tie is not as another's"), yet the narrator's steady suspicion
  and the unsolved riddle of his two women friends persist. Render his charm and
  Chen's wariness side by side; do not tip the mystery. By ch09's end he has moved
  (reportedly to Shanghai) — may recur in Part Three.
- **WANG WEN (王文, real name Wang Wenhan).** The Beiping action man: solid, wholly
  genuine, a slight stammer (hence slow speech, and worse when angry), quiet — but
  high-spirited before a job. In B05 he over-reaches: greedy for merit, he rushes
  the Shi Yousan plot and botches it, then relays Shi Dachuan's account through
  tears. Ends jailed at "Site C." Terse, plain, remorseful speech.
- **XIAN HONGXIA (先鸿霞).** Shi Yousan's personal adjutant and Wang Wen's sworn
  brother; careful, close-thinking, a patriot who asks nothing and will not have
  his name spoken until he has shown a result; brave to the last (reaches for his
  gun, curses and kicks his captors). Seized and lost to the gendarmerie in B05 —
  one of the "nameless heroes." Speaks (via relay) earnest, unadorned, resolute.
- **SHI DACHUAN (史大川).** The other inside man (an "Adjutant Shi"), a big,
  raw-boned, grievance-ridden soldier turned by Xian Hongxia; risks his life to
  bring word of the disaster, weeps telling it, then — misjudged as a spy and
  frightened off by Liu Zhaonan — leaves in bitter anger ("feel your own
  conscience!"). Blunt, hot, honest speech. Gone by chapter's end.
- **Chen's Part-One team (mostly off-stage now):** WU PING 吴萍, LÜ YIMIN 吕一民,
  YANG YUSHAN 杨玉珊 (marries Zheng Enpu), ZHENG ENPU 郑恩普 ("Third Master Zheng,"
  later the monk Xingci), BAI SHIWEI 白世维. See B04 HANDOFF/PROGRESS for their
  full sheets; carry forward only where they recur.

## Where the book stands

- Part One (北国锄奸, "Rooting Out Traitors in the North") is COMPLETE: front
  matter (B01); the story's opening and the Fan Xing mystery (B02, ch06); the
  Zhang Jingyao case (B03, ch07); the Ji Hongchang case (B04, ch08); the Shi
  Yousan case, Chen's disgrace and exile and restoration (B05, ch09).
- **NEXT: Part Two — "Disgrace at Hanoi" (河内辱命)**, the 1939 attempt on Wang
  Jingwei. B06 opens it with the Author's Preface (ch10) and Chapter 1 (ch11).

## What is NEXT

- Batch B06 = ch10 + ch11 (Part Two preface + Chapter 1, ~13,734 chars). Kickoff
  is the paste-block at the top of this file. Runs to completion (no gate); ends by
  pasting the B07 kickoff.
- The frozen register reference is `reference/B01_frozen.md`. Narrative sits at
  4.55-4.70 en/han; if later matter wants a different baseline, RAISE it, do not
  silently reset.
- Sub-heading pattern DIFFERS by chapter (space-style vs 、-style; standalone vs
  glued). Grep each new chapter to determine its pattern and set clean_batch's
  spec. ch10 is a short preface (may have no sub-headings).
- WATCH for source anomalies: ch08 line 402 (a bullet trailing off mid-phrase,
  left unmerged + footnoted); ch09 printed §五 BEFORE §四 (out-of-sequence
  numbering, preserved + footnoted) and had a misplaced-「 glitch (L164→165). Verify
  heading ORDER against XHTML byte positions, not just presence. Re-grep each
  batch's source for `\[\d+\]` note markers (none present through B05).

## Open items for the read-through / completion

- Feed decided renderings back to authority.json on completion: 军统 "the Juntong";
  蓝衣社 "the Blue Shirt Society"; 关东军 "the Kwantung Army"; and the B02-B05
  historical names (张宗昌, 蔡锷, 宋哲元, 段祺瑞, 孙传芳, 胡汉民, 张学良, 任应岐,
  商震, 于学忠, 吴佩孚, 佟麟阁, 杨虎城, 李大钊, 樊钟秀, 韩复榘, 刘郁芬, 王树常,
  李培基, 孙殿英, 庞炳勋, 李际春, 白坚武, 阎锡山).
- Japanese name readings to verify when the men recur (多田骏 Tada Hayao, 田代皖一郎
  Tashiro Kan'ichirō, 土肥原贤二 Doihara Kenji, 坂垣征四郎 Itagaki Seishirō,
  山本荣治, 大冢清, 中岛信一, 冈村).
- Stray source glyphs still to resolve in later batches: trailing 杀 on the ch22
  title; 寿张为幻 in the ch16 title; 毛酋 in a ch36 section title.
- **Part Two title:** decide, on reading the ch10 preface, whether "Disgrace at
  Hanoi" survives as the Part Two heading (Chen rejected 河内刺汪; the preface title
  is 河内汪案始末). Record the decision; update book.json if changed.
- Provisional romanizations to firm up when sources allow (see glossary
  `provisional` rows, incl. the B04/B05 agents and the redacted poison "X霜" in
  ch08 §2 src 148).

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01-B05 builds (0/0/0). Source is a
  clean digital EPUB, predominantly simplified with residual variant glyphs and
  pervasive digitization glitches (list them, render to plain sense, do not
  footnote mechanical typos). B01-B05 glitch lists are in PROGRESS.md.
- Running-header line 英雄无名-陈恭澍 opens all 43 content files: drop it (drop=2 in
  each clean_batch spec, header + <h2> section title).
- Enumerated ；/： bullet lists in the source are DELIBERATE separate <p> — do NOT
  merge them; only genuine mid-phrase splits (last char not terminal) merge, and
  now those can CHAIN across 3+ fragments. Confirm against the source HTML <p>
  count. Beware source CUTS (ch08 L402) and misplaced brackets (ch09 L164).
- Faithful numbering gaps/anomalies (NOT errors): Part Three skips ch7, splits
  ch10 into (上)/(下); 三面受敌 一往无前 titles two different chapters; ch09 printed
  §五 before §四. Preserve and footnote.
- Expect a stray per-task branch at the top of every batch; consolidate onto
  claude/nameless-heroes per rule 2.
