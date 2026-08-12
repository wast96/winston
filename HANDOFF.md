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
Nameless Heroes B03

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once, then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05) and B02 (ch06) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them.

Do Batch B03 = ch07 ONLY (第二节 一鸣惊人 不同凡响, ~21,263 source chars). Part One, Section 2: the payoff of the Zhang Jingyao case (白世维 "startling debut") and the Beiping Station's early operations. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch07 from data/src (08_index-split-000-0006.txt). DROP the running-header first line 英雄无名-陈恭澍. Fix extractor-split paragraphs (a line whose last char is not in 。！？」）…— continues into the next). GREP the source for note markers (\[\d+\]) and record "none present" in PROGRESS.md. Check the chapter HTML in data/src_epub for set-off formatting; ch06 had NONE (plain narrative), so expect the same, but confirm with scripts/apply_format_markers.py logic (no images/center/kt classes -> nothing to recover).
2. Build data/zh/ch07.txt VERBATIM from data/src: extend scripts/clean_batch.py with ch07's drop/merge/heading spec (it verifies source characters are conserved). Watch for numbered sub-sections (一 二 三 …) that the digitization GLUES onto the tail of a paragraph, exactly as in ch06 — grep the source for a terminal 。 immediately followed by 一/二/三/四/五 + space, and for a standalone heading line. Write out/ch07_en.json + out/ch07_reading.md (## chapter title from book.json; one English paragraph per source body line).
3. Translate to the FROZEN register (Chen's voice sheet + the new-character voice sheets are in HANDOFF; read the last two pages of ch06 English for the seam). Consult glossary.json and authority.json BEFORE romanizing anything new; REUSE the settled renderings (the Juntong; Dai Li / Yunong; Zheng Jiemin; Wang Tianmu / cover Zheng Shisong; Fan Xing; Bai Shiwei; Beiping/Tianjin Station; 制裁 "sanction"; the Commandant/the Leader/the Generalissimo = Chiang; the numbered classes 期; the Nationalist idiom). New characters get a two-line voice sheet in HANDOFF. Render digitization glitches to plain sense and LIST them in PROGRESS.md.
4. Checks: verify_unit.py ch07 (parity + numbers with --noise data/noise.txt + anchors) AS YOU GO; check_align.py; regenerate checks.json with scripts/batch_artifacts.py and run check_structure.py + check_content.py --config checks.json; qc_entities.py on a reconstructed bilingual; verify the TAIL against the source (rule 4 corollary). check_register.py --ref reference/B01_frozen.md out/ch07_reading.md ("shall" in Chen's narration is deliberate — do not de-formalize it). The once-per-book blind double-translation (check 7) and back-translation sample (check 8) were done in B02; a spot re-check is enough.
5. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (do NOT re-note anything already noted in B01/B02 — the full list is in PROGRESS.md; e.g. Zhang Jingyao, the Legation Quarter, the Beiping Station, the 期 classes, "sanction", the Commandant, Itagaki, the Grand Hôtel des Wagons-Lits all already noted). Add glossary rows with attestation status; flag any new principal cast principal: true. Figures: survey found only the cover (already placed); confirm ch07 carries no images.
6. Rebuild the EPUB, qa_epub.py until green, epubcheck if available; record all check results in PROGRESS.md; write the voice sheet(s) and update HANDOFF.md; commit and push to claude/nameless-heroes.

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B04 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
```

## What is DONE (do not redo)

- **Step 0 (survey).** Ingest + book.json (43 chapters, 5 TOC parts) +
  skeleton EPUB. See the survey section of PROGRESS.md.
- **Batch B01 (ch01-ch05), the front matter.** Foreword, three book
  introductions, Part One prefatory note. Translated, annotated (67 notes),
  glossary and Principal Characters page authored, cumulative EPUB rebuilt.
  All checks green; epubcheck clean. Full detail in PROGRESS.md ("Batch B01").
  **VOICE GATE PASSED (approved by the commissioner):** the B01 front matter
  is now the FROZEN register reference (concatenated into
  `reference/B01_frozen.md`) for check_register.py --ref from B02 on.
- **Batch B02 (ch06), Part One Section 1** ("A Heavy Charge, Pressing
  Onward"), the first narrative unit. 322 paragraphs, five sub-sections;
  24 notes (91 cumulative); 17 glossary rows added (principals now 6). All
  checks green; epubcheck 0/0/0. The once-per-book blind double-translation
  and back-translation samples were done here. Full detail in PROGRESS.md
  ("Batch B02"). EPUB now 6/43 chapters.

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` (new): derives data/zh/<id>.txt verbatim from
  data/src, applying per-unit drops/merges/heading-splits with a source-
  conservation check. Used instead of make_bilingual->split_bilingual when a
  batch's logical paragraphs differ from the source <p> boundaries.
- `scripts/batch_artifacts.py` (new): derives out/<id>_en.json from the
  reading files and writes checks.json (docs/sources for the structure and
  content checks).
- `scripts/check_content.py` (patched): name_map skips "_"-prefixed glossary
  categories/entries; it crashed on the sectioned glossary's _about string.
- Glossary authored SECTIONED and merged by hand (validated with
  apparatus_merge.check_text). apparatus_merge's glossary path assumes a FLAT
  {zh: row} map and would corrupt the sectioned file; notes still use it.
- data/noise.txt carries the B01 project noise rules (see PROGRESS.md).
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches it;
  re-run setup.sh per session). setup.sh's ONE failing regression test ("hook
  stands down on template stub") is a false alarm coupled to template state,
  not a defect; see PROGRESS.md.

## Renderings settled this batch / carry-forward

- 军统 / 军统局 -> "the Juntong" (DECIDED; glossary organizations). Full name
  and anachronism in the ch04 note. Feed back to authority.json on completion.
- Agreed shelf (reused): 戴笠 Dai Li (courtesy name Yunong); 汪精卫 Wang
  Jingwei; 北平 Beiping; 天津 Tianjin.
- Institutions: 力行社 the Lixingshe; 特务处 the Special Services Department;
  调查统计局 the Bureau of Investigation and Statistics; 第二处 the Second
  Department; 站 Station / 区 District (kept distinct); 特工总部 the Special
  Operations Headquarters ("No. 76"); 保密局 the Bureau of Confidential
  Investigation.
- Book's own terms kept as idiom: 制裁 "sanction" (targeted killing); 绥靖
  "pacification" and 戡乱 "suppression of the rebellion" (the 1946-49 war);
  "bandits" / "the bandit chief Mao" (毛酋) for the Communists; "traitors" for
  collaborators. All preserved, flagged in notes where scholarship contests
  the claim (e.g. the Chahar army attribution, the Ji Hongchang note).
- Part/book titles (provisional, may refine): 北国锄奸 "Rooting Out Traitors
  in the North"; 河内辱命 "Disgrace at Hanoi" (published as 河内汪案始末, "The
  Full Story of the Wang Case at Hanoi"; see the ch03 note and, later, the
  ch10 preface); 百战声威 "Renown Won in a Hundred Battles"; 平津地区绥靖戡乱
  "Pacification of the Beiping-Tianjin Region".
- Japanese names are RECONSTRUCTED readings (provisional): 山本荣治 Yamamoto
  Eiji; 大冢清 Ōtsuka Kiyoshi; 中岛信一 Nakajima Shin'ichi; 冈村 Okamura.
  坂垣征四郎 → Itagaki Seishirō (STANDARD/attested; source writes 坂垣 for 板垣).
  Verify against Japanese sources when they recur in the narrative.
- **B02 settled shelf (reuse; in glossary.json):** Chiang's titles — 校长 "the
  Commandant", 领袖 "the Leader", 委员长 "the Generalissimo", 蒋公 "Mr. Chiang"
  (all Chiang Kai-shek; noted once at ch06). 期 "class" (numbered graduating
  classes; 老大哥 "elder brother", 小老弟 "little brother"). 中央军校 "the
  Central Military Academy"; 军会 "the Military Association" (革命军人同志会);
  青会 "the Youth Association" (革命青年同志会); 复兴社 "the Renaissance Society";
  中统 "the Zhongtong". 特派员 "special commissioner". 洪公祠 "the Honggongci".
  郑士松/王天木 — cover name "Zheng Shisong", real name Wang Renqiang, working
  name "Wang Tianmu". 元 "yuan". 制裁令 "sanction order". 六国饭店 "the Grand
  Hôtel des Wagons-Lits". 四维学会 "the Siwei Society". Places: 南京 Nanjing,
  徐州 Xuzhou, 洛阳 Luoyang, 福州 Fuzhou, 郑州 Zhengzhou, 开封 Kaifeng, 海参崴
  Vladivostok. The 京沪杭平津汉港穗赣 string = Nanjing, Shanghai, Hangzhou,
  Beiping, Tianjin, Hankou, Hong Kong, Guangzhou, Jiangxi.

## Voice sheet — CHEN GONGSHU (author / narrator)

- REGISTER: educated, formal, essayistic first person; grave and a touch
  archaic but not stilted. Long sentences with semicolon-joined clauses;
  four-character idiom and classical allusion used freely (养虎遗患,
  李代桃僵, 富贵不淫, 一了百了) and footnoted when they carry weight.
- STANCE: self-justifying yet self-effacing; disavows self-promotion ("I am
  no more than the thread that stitches the pages together"), insists on
  truthfulness, admits his own blunders. Tender toward the dead comrades,
  bitter toward the enemy. Rhetorical questions and exclamations for emphasis.
- IDIOM: unbroken Nationalist idiom of 1980s Taiwan (see settled renderings).
  Preserve it; do not soften. Footnote where a claim is contested.
- FORMALITY: courteous 先生 "Mr." for superiors and elders (Mr. Dai Li);
  warm 兄 "Brother" for close colleagues (Brother Xiuyuan).
- English target ratio ~4.6-5.3 en/han (front matter); narrative runs a touch
  terser (ch06 median 4.55). Merge clauses where English wants them merged;
  keep the semicolon rhythm where it reads. Chen's narrating "shall" (for the
  future: "I shall set out below") is DELIBERATE period register — do not
  de-formalize it; check_register flags it informationally and it is fine.

## Voice sheets — new principal cast (B02)

- **DAI LI (戴雨农 / Mr. Dai)** now on the page as a character: warm and
  informal off duty (mahjong, film outings, small eating-houses), abrupt and
  close-mouthed on business ("You will come to understand it in time"; answers
  a question with silence); tests a man sideways (the Cao Xiaoqing sounding-
  out); never boasts of his own deeds. Chen reveres him but records the
  brush-offs. Address: "Mr. Dai" / "Dai Yunong"; his men are 兄 "brother."
- **ZHENG JIEMIN (郑介民 / Mr. Zheng).** Educated, urbane, the theorist of the
  service; generous, treats subordinates "as his own sons and younger
  brothers." Speaks in measured, reasoned instructions (the Fan Xing
  handling-principles). Cantonese, Whampoa 2nd class, studied in Russia.
  Chen's affection for him is plain. Address: "Mr. Zheng" / "Mr. Jiemin."
- **WANG TIANMU (王天木 / cover Zheng Shisong, brother Tianmu).** Sixteen years
  Chen's senior and worldly where Chen is green; a dandy (narrow Western
  suit, silk tie) with "a bellyful" of learning; Baoding + Japanese officer
  schooling, ex-Northwest-Army, once a bandit-taming "commander." Terse in
  company ("brother Tianmu said nothing"). Dai's old friend and near in-law.
  His loyalties turn ambiguous later (Hanoi) — keep him unsentimental.
- **FAN XING (范行, courtesy Jiman).** The enigma: silver-tongued, "everything
  to the point," literary talk always on his lips and never politics; several
  languages; evasive, flushes when caught. Chen never resolves him in this
  section ("Guess if you can — what was his true identity?"). Render his charm
  and the narrator's steady suspicion side by side; do not tip the mystery.

## Where the book stands

- Front matter translated (B01). Chen's purpose, method, and the summaries of
  the four books.
- **B02 (ch06):** the story proper opens. 1931: Chen is one of fourteen picked
  from Chiang's audience for the Special Research Class; drifts, jobless after
  the September 18th Incident, into lodging with Huang Jianqiu and Zhang
  Yanyuan, where he first meets Dai Li. Dai draws him in as an unpaid
  watcher, then (1932) has him recruit thirty men for the Honggongci Special
  Service Police Training Class — Chen is class monitor with a secret
  reporting task. Graduated, he is sent (Nov 1932) to found the Beiping
  Station with Yang Ying and Qi Nanpu, stopping in Tianjin to meet Wang
  Tianmu. 1933: the station takes shape; the Fan Xing intelligence mystery
  opens (unresolved, a 21-year thread); Zheng Jiemin arrives as North China
  special commissioner; Dai Li inspects Beiping, ties in the Northeastern
  notable Wu Youquan and the Siwei Society. The section closes on the
  station's first "sanction" — the 7 May 1933 killing of the traitor Zhang
  Jingyao at the Grand Hôtel des Wagons-Lits, carried out by Bai Shiwei.

## What is NEXT

- Batch B03 = ch07 (Part One, Section 2, 一鸣惊人 不同凡响, ~21,263 chars):
  the Zhang Jingyao case as "a startling debut" (Bai Shiwei), and the Beiping
  Station's early operations. Kickoff is the paste-block at the top of this
  file. Runs to completion (no gate); ends by pasting the B04 kickoff.
- The frozen register reference is `reference/B01_frozen.md`. ch06 sat at
  4.55 en/han (narrative terser than the essayistic front matter); if later
  narrative wants a different baseline, raise it, do not silently reset it.
- ch06 confirmed the sub-heading pattern for narrative chapters: numbered
  sections (一 二 三 …) are GLUED to the tail of the preceding paragraph (and
  the first is a standalone line); handle in clean_batch.py exactly as ch06.

## Open items for the read-through

- Confirm at the voice gate: the recovered ch04 sub-headings (five titled
  sections), footnote density, and the "the Juntong" rendering.
- 军统 consistency across the whole book; feed the decision back to
  authority.json on completion.
- Japanese name readings (above) to verify when the men recur.
- Stray source glyphs still to resolve in later batches: trailing 杀 on the
  ch22 title; 寿张为幻 in the ch16 title; 毛酋 in a ch36 section title.
- Whether "Disgrace at Hanoi" survives as the part title after the ch10
  preface is translated (Chen rejected 河内刺汪; the book was titled
  河内汪案始末).

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01 build. Source is a clean
  digital EPUB, predominantly simplified with residual variant glyphs and
  scattered digitization glitches (list them, render to plain sense, do not
  footnote mechanical typos). B01's glitch list is in PROGRESS.md.
- Running-header line 英雄无名-陈恭澍 opens all 43 content files: drop it
  (clean_batch.py handles the B01 units; the count is baked into its per-unit
  "drop" spec).
- Faithful numbering gaps (NOT errors): Part Three skips ch7, splits ch10 into
  (上)/(下); 三面受敌 一往无前 titles two different chapters.
- Expect a stray per-task branch at the top of every batch; consolidate onto
  claude/nameless-heroes per rule 2.
