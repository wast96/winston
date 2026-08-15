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
Nameless Heroes B24

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once (its ONE failing regression test, "hook stands down on template stub", is a KNOWN false alarm; all others pass), then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05), B02 (ch06), B03 (ch07), B04 (ch08), B05 (ch09), B06 (ch10 preface + ch11), B07 (ch12), B08 (ch13), B09 (ch14), B10 (ch15), B11 (ch16), B12 (ch17), B13 (ch18 + ch19), B14 (ch20), B15 (ch21), B16 (ch22), B17 (ch23), B18 (ch24), B19 (ch25), B20 (ch26), B21 (ch27), B22 (ch28) and B23 (ch29) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them. PART TWO ("Disgrace at Hanoi") is COMPLETE; PART THREE ("Renown Won in a Hundred Battles" / 百战声威) is nearly done (ch20 self-preface + ch21-ch29). The EPUB now holds 29/43 chapters, 276 notes. NOTE on batch numbering: book.json's batches array lumps ch23+ch24 as "B17", so the working batch labels run ONE AHEAD of the book.json array from ch24 on (ch24 = B18 … ch29 = B23, ch30+ch31 = B24). book.json's B23 array entry = ch30+ch31 (chars 16275); working B24 = BOTH, and B24 COMPLETES PART THREE.

Do Batch B24 = ch30 + ch31 (TWO units; COMPLETES PART THREE): ch30 = 第十章 祸不单行 柱折梁摧(下) "Chapter 10. Troubles Never Come Singly; Pillars Snap, Beams Fall (Part 2)" and ch31 = 写在「英雄无名」第三部专书出版前 "Written Before the Third Volume Went to Press" (confirm both title_en in book.json). ch30 continues DIRECTLY from ch29's cliffhanger: ch29 (the (上) half) broke off on 28 June 1941 with Liu Yuanshen (刘原深, acting commander of the 第一行动大队) walking into the Zhou Xiyuan (周西垣) / Zhu Min (朱敏) trap over the sanction of Xu Liqiu (许力求) - and closed with Chen's own capture (自投罗网, end of the tenth month) and the line that the 军统局-led Shanghai work did NOT cease. ch30 (下) = section 三、仁者之心终为幺么所乘 onward: Liu's memoir (沪滨三次历险实录) recounts the trap sprung and his capture, then from section 四 Chen resumes his OWN narration (per ch31's own note #8: 第十章的一、二、三段系刘原深原稿，自第四段起仍为笔者自述 - keep the two voices distinct). ch31 is the Part-Three closing note: an ERRATA/addendum list correcting earlier chapters. Read the tail of ch29 English (out/ch29_reading.md, section 二's close on the 28 June meeting + Chen's capture recap) and ch29 for register + story continuity. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch30 (31_index-split-000-0029.txt) and ch31 (32_index-split-000-0030.txt) from data/src. CONFIRM structure p-by-p against data/src_epub/OEBPS/Text/index_split_000_0029.xhtml [ch30: 1 <h2> + 110 <p>, NO <h1>/<br/>/<img>/[\d+]] and .../index_split_000_0030.xhtml [ch31: 1 <h1> + 14 <p>, NO <h2>/<br/>/<img>/[\d+]]. drop=2 for BOTH (ch30: running header + <h2> title; ch31: running header + <h1> title - CONFIRM ch31's first body line is 抗战期间... and that drop=2 is right for an <h1>-titled front-matter piece). Do the byte-exact p-by-p diff FIRST (the B19-B23 method: extract <p> inner text, walk each <p> consuming 1 body line, assert every <p> matches its body line) to CONFIRM 110=110 / 14=14 and to LOCATE any SEVERED-<p> boundaries (last char non-terminal → MERGE; parity is data/zh↔reading.md, NOT the raw <p> count). HEADS UP - ch30: ONE STANDALONE enumerated heading at p#0 三、仁者之心终为幺么所乘 (幺么 = "petty villain", cf. ch29 L70); a SECTION 四 heading MUST exist somewhere later (ch31 note #8 says 第十章 runs to a fourth段) - FIND it (may be standalone OR tail-glued; grep 四、); severed-<p> candidates flagged at p#19/p#70/p#73/p#88 (confirm which are real mid-phrase merges vs ：-ended memoir/document lead-ins like p#1 …其文如下：). ch30 opens 下文仍是原深兄的亲身经历…其文如下： and continues Liu's first-person memoir. HEADS UP - ch31: the enumerated 一、-八、 items at p#5-p#13 are an ERRATA/addendum LIST (每 item "关于…(见第X章第X页)…") - these are DOCUMENT-CLAUSE list items kept as ORDINARY body lines per parity (cf. ch28's inner 一二三 clause lists), NOT section headings and NOT in `standalone`. They cite EARLIER chapters by 页 (page) numbers that our EPUB does not have - render the corrections faithfully but do NOT invent page cross-references; keep the source's own "(见第X章…)" wording as written (it is the author's, not ours).
2. Extend scripts/clean_batch.py with ch30's and ch31's specs (drop=2 each; the confirmed severed-<p> merges; ch30's standalone 三、heading at p#0 + the section 四 heading; ch31 has NO section headings, just the errata list as body lines). Run it (source-conservation check must pass). Write out/ch30_reading.md and out/ch31_reading.md (## from book.json title_en; one English paragraph per source body line; ch30's section headings as ### ). Then run scripts/batch_artifacts.py ch30 ch31, and ALWAYS finish with a NO-ARG run (the trap: an ID-run writes checks.json with ONLY those units; the no-arg run restores all 31 units so check_structure/check_content see them).
3. Translate to the FROZEN register (Chen's voice sheet in HANDOFF; narrative sits at 4.55-4.78 en/han, prefaces/document-heavy chapters higher; ch29 ran 4.97 with heavy dialogue/telegrams; ch30 is memoir-narrative + Chen's resumed narration, ch31 a short editorial note - expect mid-range ratios; the narrating "shall" is DELIBERATE, do NOT de-formalize). Consult glossary.json and authority.json BEFORE romanizing anything; REUSE the settled Part-Three renderings (see "Renderings settled" + the B15-B23 shelf sections of HANDOFF - all keyed with pinyin): the ch29 cast recurs in ch30 - 周西垣 Zhou Xiyuan / 冯贤 Feng Xian (his cover name, renders its OWN way NOT "Zhou Xiyuan"), 朱敏 Zhu Min, 刘全德 Liu Quande, 相强伟 Xiang Qiangwei, 骆成金 Luo Chengjin, 许力求 Xu Liqiu, 刘原深 Liu Yuanshen, 齐庆斌 Qi Qingbin, 万里浪 Wan Lilang; the Juntong/the Juntong Bureau; 制裁 "sanction"; 敌伪 "the enemy and the puppets"; 特工总部/七十六号 "Special Operations Headquarters"/"No. 76"; 第一行动大队 "First Action Brigade"; 日本宪兵队 "the Japanese gendarmerie". ch31's errata cites recur EARLIER names - REUSE their keyed forms (耿嘉基/耿? confirm; 徐寿新 Xu Shouxin/朱承我, 余延智 Yu Yanzhi, 周锡良 Zhou Xiliang - all keyed B20; 俞叶封 Yu Yefeng; 张啸林 Zhang Xiaolin + 林怀部 Lin Huaibu keyed B20; 陈公博 Chen Gongbo). IMPORTANT place-name convention (the check_content/qc_entities gate): keyed CITY/PROVINCE names render in PINYIN per the glossary; non-keyed attested Shanghai ROADS keep their historical names, pinyin only for the genuinely uncertain. Render Republican years literally (checker matches the source numeral or auto-escapes via +1911). WATCH the digitization glitches (list in PROGRESS.md, render to plain sense, footnote only real reading uncertainty): same classes seen ch15-ch29 (single-char substitutions, dropped stops, dittography, mismatched guillemets, stray ？, and ○/× redactions in room/lane/phone numbers - the numeric checker mis-reads ○; carry the real value in English and noise only the mis-read glyph-string; × redactions render as em-dash blanks; ch31's 页-page numbers in the errata are REAL cited numbers - carry them but they refer to the source's pagination, not ours). Dates/counts: carry real values as DIGITS/words; NOISE only idiom/approximate/name-numeral/elided/date-name forms (data/noise.txt already carries the B01-B23 rules; add B24's).
4. Checks: verify_unit.py ch30 and ch31 (parity + numbers with noise auto-found + anchors); check_align.py ch30 ch31; regenerate checks.json with scripts/batch_artifacts.py (no args) and run check_structure.py --config checks.json + check_content.py --config checks.json (NOTE: check_content prints KNOWN PRE-EXISTING artifacts and exits nonzero because of them - ch08 Shunde ×3, ch13 ×9, ch09 "Jize County" ×1, ch26's TWO documented keyed-substring FALSE POSITIVES 武汉卿/劳勃生路; CONFIRM ch30/ch31 each show "all in the paired paragraph" / 0 displaced, and align any keyed name/place/TERM to its glossary-decided rendering. A NEW unit's displacements are almost always a keyed name/place/term rendered a DIFFERENT way than the glossary - align the English to the keyed form; the exception is a keyed name that is a SUBSTRING of a larger different referent, a documented false positive, not a fix). Do NOT add COMMON-NOUN or book/periodical keys. qc_entities.py on a reconstructed bilingual per unit (data/zh body lines + out/chNN_en.json, `> zh` / en pairs, strip the ### heading lines; every glossary row needs a pinyin field). Verify the TAIL of each unit against the source. check_register.py --ref reference/B01_frozen.md out/ch30_reading.md (and ch31) ("shall" is deliberate - read the note, do not de-formalize).
5. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (full list in PROGRESS.md; the big already-covered furniture incl. now: No.76/特工总部 ch04/ch17, 制裁, 忠义救国军 ch21, the tiger bench 老虎凳 ch29, the Little Red Devils/Ruijin ch29, the Changsha fire ch29, the Advanced Education Class/Linli class ch29, the South China Evening News ch29, Dai Li's 1946 air crash ch02/ch25). ch30 (the trap sprung + Liu's capture + Chen's resumed narration) and ch31 (the errata note) - expect a FEW new items (any classical allusion in the 仁者之心 / 幺么 vein; period figures/institutions the errata introduces); be generous but do NOT pad, do NOT re-note. Merge notes via apparatus_merge.py (positional arg: apparatus_merge.py data/ch30_apparatus.json, then data/ch31_apparatus.json; numeric character references only in note bodies; anchors verbatim ASCII substrings of the reading.md body text, NO em dash and NO quote/apostrophe character - substring traps; multi-occurrence anchors attach at the first; TIGHTEN a generic anchor if it would match an earlier paragraph). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field; apparatus_merge's glossary path assumes a FLAT map and would corrupt the sectioned file - use it ONLY for notes; scripts/add_ch29_glossary.py is the latest by-hand pattern, asserting each hanzi key against data/zh). Confirm ch30/ch31 carry no images (neither XHTML has <img> - confirm). For any CJK in a note body use the make_ch29_apparatus.py pattern (author bodies with typed hanzi, ASSERT every non-ASCII glyph is present in data/zh/chNN.txt, then convert to NCRs) to defeat the CJK-mangling hazard - and remember a CORRECT glyph may be ABSENT if the source prints a glitch/variant form, so describe such terms with the source's own form + pinyin.
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; update HANDOFF.md; commit and push to claude/nameless-heroes. (B24 COMPLETES PART THREE; next is B25 = ch32 = 「平津绥靖」自序, the Part-Four author's preface - confirm scope in book.json: book.json's B24 = ch32 alone. Part Four "Pacification of the Beiping-Tianjin Region" = ch32-ch43, and ch33-ch42 carry book.json `sections` arrays - the 1946-49 civil-war material.)

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B25 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
```

## What is DONE (do not redo)

- **Step 0 (survey).** Ingest + book.json (43 chapters, 5 TOC parts) + skeleton EPUB.
- **Batch B01 (ch01-ch05), the front matter.** 67 notes. **VOICE GATE PASSED:** the B01
  front matter is the FROZEN register reference (`reference/B01_frozen.md`) from B02 on.
- **B02-B05 (ch06-ch09). Part One COMPLETE.**
- **B06-B13 (ch10-ch19). Part Two ("Disgrace at Hanoi") COMPLETE.**
- **Batch B14 (ch20), PART THREE OPENS.** ch20 = the Part-Three self-preface.
- **Batch B15 (ch21).** Arrival + order of battle. **Batch B16 (ch22).** First 1940 sanctions
  + Fan Xing. **Batch B17 (ch23).** The "three-sided enemy" framing bridge. **Batch B18 (ch24).**
  The anatomy of the three-sided enemy + the Yu Yefeng sanction + Dai's self-review. **Batch B19
  (ch25).** The full work-review + the arms-gift + the Fan Xing intelligence puzzle.
- **Batch B20 (ch26), Part Three Chapter 6.** 第六章 泰山鸿毛 同此一掷 - the martyr-roster chapter
  (321 body paragraphs; 11 notes; 27 net new glossary rows). Two documented keyed-substring FALSE
  POSITIVES (武汉卿/劳勃生路). Detail in PROGRESS.md ("Batch B20").
- **Batch B21 (ch27), Part Three Chapter 8.** 第八章 大亨之死 扑朔迷离 - the 张啸林 tycoon-death case
  (killed 14 Aug 1940 by 林怀部 Lin Huaibu). Part Three SKIPS 第七章 (faithful gap: ch26 = 第六章,
  ch27 = 第八章). 133 body paragraphs; 6 notes; 2 net new glossary rows (赵圣, 黄金荣). Detail in
  PROGRESS.md ("Batch B21").
- **Batch B22 (ch28), Part Three Chapter 9.** 第九章 声威大震血浪腥风 "Fearsome Renown, Waves of
  Blood" - the height-of-renown-and-blood chapter, continuing ch27's tail. THREE sections: Chen's
  reflections on killing/war/conscience; the Fu Xiao'an / Zhu Sheng axe-killing in full (the
  reproduced Chongqing Ta Kung Pao report + the Japanese spokesman Mabuchi's 新申报 statement + the
  Zhou Fohai diary on the mayoral succession); the puppet institutional offensive (the two
  reproduced court-retrocession agreements 公共租界 1930 / 法租界 1931, the Zhou Fohai diary on the
  court "takeover", the killing of the Frenchman Duluo, the Central Reserve Bank sabotage, the No. 76
  bloody reprisal at the Bank of China), closing on Chen's own capture. **drop=2; 1 <h2> + 224 <p>,
  NO <br/>/<img>/note-markers, byte-exact p-by-p; 4 severed-<p> merges (80/81, 135/136, 157/158,
  214/215); 3 STANDALONE enumerated 一、二、三 section headings (L3/L49/L129); inner document-clause
  一、二、三 lists kept as ordinary body lines.** 217 body paragraphs; 8 notes (267 cumulative); 3 net
  new glossary rows (朱升 Zhu Sheng, 联合准备银行 the Federal Reserve Bank, 会审公廨 the Mixed Court).
  One displacement FIXED by aligning to the keyed TERM 东亚新秩序 "New Order in East Asia". check_content
  0 displaced; qc 0 misses. All checks green; qa_epub PASS; epubcheck 0/0/0/0. **EPUB now 28/43
  chapters.** Detail in PROGRESS.md ("Batch B22").
- **Batch B23 (ch29), Part Three Chapter 10 (上).** 第十章 祸不单行 柱折梁摧(上) "Troubles Never Come
  Singly; Pillars Snap, Beams Fall (Part 1)" - the disaster chapter, the FIRST half of a two-part
  chapter (ch30 = 下). A two-voice chapter: Chen's essayistic narration frames Liu Yuanshen's (刘原深)
  first-person memoir 沪滨三次历险实录. TWO sections: (1) 是我误了他的锦绣前程 - Chen loses a son, the bureau
  summons Liu Yuanshen to the Chengdu Advanced Education Class, Chen persuades him to stay and hands him
  the acting command of the First Action Brigade (the Changsha-fire dispatch, the seventeen classmates,
  Dai Li anecdotes); (2) 人性理性交织下的特务活动 - Liu takes over, meets the three sub-brigade leaders,
  and is drawn into the Zhou Xiyuan/Zhu Min trap over the Xu Liqiu sanction, breaking off on the 28 June
  meeting; Chen's closing narration recaps his own capture. **drop=2; 1 <h2> + 72 <p>, NO <br/>/<img>/
  note-markers, byte-exact p-by-p; 1 severed-<p> merge (65/66); 1 STANDALONE enumerated 一、heading (L3);
  1 TAIL-GLUED 二、heading on L33 after a terminal 。.** 70 body paragraphs; ratio 4.97; 9 notes (276
  cumulative); 7 net new glossary rows (周西垣/冯贤/朱敏/刘全德/相强伟/骆成金/许力求). check_content 0
  displaced; qc 0 misses; register within tolerance ("shall" 56%, deliberate). qa_epub PASS; epubcheck
  0/0/0/0. **EPUB now 29/43 chapters.** Detail in PROGRESS.md ("Batch B23").

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` - derives data/zh/<id>.txt verbatim from data/src, applying per-unit
  drops/merges/heading-splits with a source-conservation check. Specs for ch01-ch28. Merge logic
  FOLLOWS CHAINS. **drop is variable:** most chapters drop=2; ch01/ch10/ch20 drop=3. `standalone`
  = a sub-heading kept as its own <p> with no heading markup, emitted as `### `; `glued` = a
  sub-heading fused onto a paragraph's TAIL (endswith), split off; `glued_head` = a heading fused
  onto a paragraph's HEAD (startswith), split off; `merges` = source <p> pairs that sever one
  sentence OR an intra-<p> `<br/>` line break (the extractor renders `<br/>` as a newline).
  **B20 lesson: not every `<br/>` is a merge** - a `<p>` that is a TABLE/roster (each `<br/>` a
  data row) is KEPT as rows, only a `<br/>`-split PROSE sentence merges. **B20/B21 lesson: a
  tail-glued heading can end in a full-width `」`** (the three-tell's `」` case). **B22 lesson: a
  chapter can carry INNER enumerated 一、二、三 DOCUMENT-CLAUSE lists (quoted-agreement clauses) that
  are NOT section headings - keep them as ordinary body lines per parity, judged by function.**
- `scripts/batch_artifacts.py` - derives out/<id>_en.json FROM out/<id>_reading.md and writes
  checks.json. Author the reading.md; run this. **TRAP: running it with an ID writes checks.json
  with ONLY that unit; ALWAYS finish with a no-arg run.**
- `scripts/verify_unit.py <id>` - parity + numbers (auto-finds data/noise.txt; do NOT pass
  --noise) + anchors. Run per unit.
- `scripts/build_reading_epub.py` - builds out/nameless-heroes.epub. Uses book.json `title_en`
  for the visible chapter H1; `### ` sub-headings render as <h2>; notes collect in
  OEBPS/notes.xhtml with popup semantics.
- `scripts/check_content.py` (patched) - name_map skips "_"-prefixed glossary categories. It
  flags KNOWN PRE-EXISTING artifacts and exits NONZERO: **ch08 Shunde (3), ch13 (9), ch09 "Jize
  County" (1)** - NOT regressions. **B20 added TWO documented keyed-substring FALSE POSITIVES:
  武汉 "Wuhan" matching inside the person 武汉卿 "Wu Hanqing"; 劳勃生 "Lao Bosheng" matching inside
  the road 劳勃生路 "Robison Road".** The pass criterion for a NEW batch is "the batch's own unit
  shows all name occurrences in the paired paragraph / 0 displaced" - EXCEPT a keyed name that is a
  substring of a larger different referent (person or road), a documented false positive, not a fix.
  A NEW unit's TRUE displacements are almost always a keyed name/place/TERM rendered a DIFFERENT way
  than the glossary: align the English to the keyed form (B22: the keyed term 东亚新秩序 "New Order in
  East Asia", first rendered lowercase, flagged twice until aligned). Do NOT add book-TITLE or
  COMMON-NOUN keys.
- **Verse marker `{p}`** (ch13, reused ch26 for the 挽联): prefix a pure-verse line with `{p} `;
  the builder renders `<p class="verse">`; the checks strip it.
- Glossary is authored/merged BY HAND into the SECTIONED file (book/people/organizations/places/
  terms), idempotent + re-read-verified. **Every row MUST carry a `pinyin` field** - qc_entities
  does `rec["pinyin"]` and KeyErrors otherwise. `scripts/add_ch28_glossary.py` is the latest by-hand
  pattern: asserts each hanzi key is a substring of data/zh/<id>.txt. A `/`-joined key holds
  alternate hanzi for one referent; qc splits on `/`. apparatus_merge's glossary path assumes a
  FLAT map and would corrupt the sectioned file; NOTES still go through apparatus_merge.py (positional
  arg, e.g. `apparatus_merge.py data/ch28_apparatus.json`).
- **qc_entities catches term-rendering drift too:** a glossary common-noun term rendered a
  different way flags as a "miss." Align the English to the glossary.
- **GLOSSARY-KEY DISCIPLINE:** a key must be a DISTINCTIVE proper noun (or a distinctive institution)
  that renders ONE way everywhere. Periodicals and books are FOOTNOTES/inline, not keys. One-off
  transliterated Western/Japanese officer names, one-off telegram/roster names, and attested Shanghai
  ROADS are inline, not keyed. A bare surname whose full name is unknown is rendered inline.
- **Note-anchor gotchas:** anchors must be ASCII, WITHOUT any quote/apostrophe character AND
  without an em dash (U+2014) - all substring traps. The reading.md uses curly quotes and em
  dashes freely, so pick an anchor phrase with none of them. **Multi-occurrence anchors attach at
  the FIRST occurrence** - and if a short generic anchor would match an EARLIER paragraph than the
  one you mean, LENGTHEN it (B22: "scene from" also occurred in an opera line, so the note used
  "still but a scene from"; and "governor of the" was tightened to "concurrently governor of the").
- **make_ch28_apparatus.py pattern (scripts/):** author note bodies as plain ASCII + typed hanzi
  + straight/curly punctuation, ASSERT every non-ASCII hanzi glyph occurs in data/zh/<id>.txt, then
  convert every non-ASCII char to a numeric char ref and run apparatus_merge.py. **A CORRECT glyph
  may be ABSENT if the source prints a glitch/variant** (cf. ch25's 洋泾浜, ch28's 洋泾滨) - describe
  such terms with the source's own form + pinyin/English, not the correct hanzi. Curly quotes / em /
  en dash are in the `allow` set (converted to NCRs, not asserted); AVOID tone-marked pinyin in
  note bodies (write diacritics as NCRs or use plain pinyin).
- data/noise.txt carries the B01-B22 project noise rules (each with a comment line). Republican
  years render literally; the checker matches the source numeral (or auto-escapes Republican-year
  N via N+1911). The elided-tens block is ordered LONGEST-FIRST. Name-numeral glyphs are noised.
  Idiom numerals are noised. **The ○ (U+25CB) address artifact:** the checker cannot read ○ as
  zero - noise the mis-read glyph-string, carry the real value in the English. **× (source
  redaction)** renders as an em-dash blank. Every REAL value is CARRIED and matched as DIGITS.
  **B22 lesson: a project noise pattern can be pre-empted by a built-in that eats its head** (the
  built-in 成千 fired inside 成千上万 before the project rule, leaving 上万; the fix was to noise the
  剩下的 tail 上万 instead of the whole idiom). Real small counts (三国同盟 "three-Power", 两方面
  "these two", 二人 "the two") are CARRIED in the English, not noised.
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches it; re-run per session).
  setup.sh's ONE failing regression test ("hook stands down on template stub") is a KNOWN false
  alarm; all other regression tests pass.

## Renderings settled / carry-forward

- 军统 / 军统局 -> "the Juntong" / "the Juntong Bureau" (DECIDED). 戴笠 Dai Li (courtesy Yunong;
  老板 "the Boss"; 戴先生 "Mr. Dai"; 戴雨农 "Dai Yunong"); 汪精卫 Wang Jingwei (汪逆 "the traitor
  Wang"). 制裁 "sanction"; 制裁令 "sanction order." 敌伪 "the enemy and the puppets"; 汪伪 "Wang
  puppets"; 沦陷区/沦陷地区 "the fallen zone(s)"; 战区 "war zone"; 后方 "the rear"; 区长 "District
  Chief"/"District chief"; 督察 "inspector" / "inspectorate"; 总督察 "Chief Inspector." Chiang's
  titles: 校长 "the Commandant", 委员长/委座 "the Generalissimo", 总裁 "the Director-General"; 领袖
  "the Leader"; 总理 "the Party Leader" (Sun Yat-sen). 日本宪兵队 "the Japanese gendarmerie"; 七十六号
  "No. 76"; 特工总部 "Special Operations Headquarters"; 工部局 "Municipal Council"; 公董局 "French
  Municipal Council"; 公共租界 "International Settlement"; 法租界 "French Concession"; 巡捕房 the
  Concession police / "police station"; 三民主义 "the Three Principles of the People." 特区法院 "Special
  District Court"; 中央储备银行 "Central Reserve Bank"; 会审公廨 "the Mixed Court" (KEYED B22); 联合准备银行
  "the Federal Reserve Bank" (KEYED B22, the North China puppet bank); 维新政府 "the Reformed
  Government"; 大道市政府 "the Great Way City Government" (NOTED B22).
- **PLACE-NAME CONVENTION (the qc gate enforces the glossary's PINYIN for keyed cities):**
  北平 Beiping, 天津 Tianjin, 汉口 Hankou, 四川 Sichuan, 虹口 Hongkou, 重庆 Chongqing (NOT Peiping/
  Tientsin/Hankow/Szechuen/Hongkew/Chungking). 重庆大公报 = "Chongqing Ta Kung Pao". KEYED roads:
  愚园路 "Yuyuan Road", 冀东 "East Hebei". Non-keyed attested Shanghai ROADS keep their historical
  forms: Avenue Edward VII (爱多亚路), Nanking Road (南京路), Mohawk Road (马霍路), the Bund/外滩,
  Robison Road (劳勃生路 - NOT "Lao Bosheng Road"; the officer 劳勃生 is keyed "Lao Bosheng", a
  documented substring false positive), Yates Rd (同孚路), Route Wagner (华格臬路), Avenue Foch (福煦路),
  Avenue Joffre (霞飞路), and the many roads listed in prior batches. Concession-street rule: keep
  attested names, use PINYIN for the uncertain (B22: 祥德路 Xiangde Road, 白赛仲路 Baisaizhong Road,
  恺自迩路 Kaiziěr Road, 西爱咸斯路 Xi'aixiansi Road, 善钟路 Shanzhong Road).
- **Book / part titles (in-text; DECIDED; reuse verbatim):** 英雄无名 = "Nameless Heroes"; Part One
  北国锄奸 = "Rooting Out Traitors in the North"; Part Two = "Disgrace at Hanoi"; Part Three 百战声威
  = "Renown Won in a Hundred Battles." 蓝衣社 = "the Blue Shirt Society" (NOTED ch08). 忠义救国军 =
  "the Loyal and Patriotic Army" (NOTED ch21). 抗日杀奸团 = "the Anti-Japanese Traitor-Killing Corps"
  / 抗团 = "the Kang Corps" (NOTED ch02/ch11; 抗团 keyed B20). Books by FOOTNOTE/inline (not glossary):
  蒋总统秘录, 戴雨农先生传/全集, 沪滨三次历险实录 (Zheng Xiuyuan / Liu Yuanshen's memoir, quoted through
  Part Three), 沪上往事 (Wan Molin), 在敌人心脏里 (Zhang Zhiyi, ch26), 大陆宪兵实录 (ch26), 上海租界问题
  (ch27/ch28), 官场现形记 "Officialdom Unmasked" (NOTED ch28); periodicals: 申报 Shenbao (NOTED ch24),
  大公报 Ta Kung Pao, 中华日报/新申报 Xin Shen Bao (occupation papers, ch20/ch28), 中美日报, 传记文学.
- **B15/B16 shelf (ch21/ch22):** 郑修元 Zheng Xiuyuan, 陈第容/陈明楚 Chen Dirong/Chen Mingchu, 黄志远
  Huang Zhiyuan, 赵理君 Zhao Lijun, 刘原深 Liu Yuanshen, 毕高奎 Bi Gaokui, 孙大成 Sun Dacheng, 万里浪
  Wan Lilang, 戴藏宜 Dai Cangyi, 杜月笙 Du Yuesheng (NOTED ch17), 俞叶封 Yu Yefeng, 万墨林 Wan Molin,
  范纪曼 Fan Jiman (= 范行 Fan Xing), 张啸林/杜/黄金荣 the three Green-Gang tycoons (张啸林 NOTED ch04),
  曾澈 Zeng Che, 王文 Wang Wen, 王天木 Wang Tianmu.
- **B18 shelf (ch24):** 劳勃生 Lao Bosheng (NOTED); 更新舞台 Gengxin Stage; 新艳秋 Xin Yanqiu (NOTED);
  袁殊 Yuan Shu (NOTED); 刘俊卿 Liu Junqing, 蒋福田 Jiang Futian (concession police); 刘绍奎 Liu
  Shaokui, 周伟龙 Zhou Weilong (道三 Daosan).
- **B19 shelf (ch25):** 秦启荣 Qin Qirong (NOTED); 毛人凤 Mao Renfeng (NOTED); 潘汉年 Pan Hannian
  (NOTED); 聂崇侯 Nie Chonghou; 潘子欣 Pan Zixin; 胡永荃 Hu Yongquan; 彭雅萝 Peng Yaluo; 高荣 Gao Rong.
- **B20 shelf (ch26; reuse; all keyed with pinyin):** 丁默邨 Ding Mocun, 汪时璟 Wang Shiying, 施何成
  Shi Hecheng, 邵范九 Shao Fanjiu, 陶联芳 Tao Lianfang, 徐寿新 Xu Shouxin (= 朱承我 Zhu Chengwo),
  徐寿棪 Xu Shouyan, 徐文祺 Xu Wenqi, 余延智 Yu Yanzhi, 周锡良 Zhou Xiliang, 张执一 Zhang Zhiyi,
  赤木亲之 Akagi Chikayuki, 林秀澄 Hayashi Hidezumi, 李正梁/李亮 Li Zhengliang/Li Liang, 林怀部 Lin
  Huaibu, 俞作柏 Yu Zuobai, 林之江 Lin Zhijiang, 萧焕文/萧杰英/萧张权 the Xiao family, 陈植琚 Chen Zhiju,
  李鑫 Li Xin, 缪维 Miao Wei, 黄克忠 Huang Kezhong, 向松坡 Xiang Songpo; 上海职工运动委员会 the Shanghai
  Workers'-Movement Committee, 抗团 the Kang Corps.
- **B21 shelf (ch27; reuse; keyed with pinyin):** 赵圣 Zhao Sheng (working name of the Second Action
  Brigade commander = 吉震苍 Ji Zhencang, both keyed, each renders its own way), 黄金荣 Huang Jinrong
  (third Green-Gang tycoon). NEW ch27 notes: the 八一三 August Thirteenth Incident (1937); the two
  municipal councils (工部局/公董局); the Reformed Government (维新政府, Liang Hongzhi/Chen Qun); the
  Central Reserve Bank + Special District Court + Zhou Fohai.
- **B23 shelf (ch29; reuse; all keyed with pinyin):** 周西垣 Zhou Xiyuan (the turned third-sub-brigade
  leader; the trap that takes Liu Yuanshen), 冯贤 Feng Xian (Zhou's cover name - renders its OWN way,
  NOT "Zhou Xiyuan", per the source's deliberate use), 朱敏 Zhu Min (Zhou's secretary/informant), 刘全德
  Liu Quande (first-sub-brigade leader, ex-Ruijin), 相强伟 Xiang Qiangwei (second-sub-brigade leader),
  骆成金 Luo Chengjin (Xiang's deputy), 许力求 Xu Liqiu (South China Evening News director, the bait
  target). NEW ch29 notes: the Changsha fire (长沙大火, 1938); the Linli class (临沣 for 临澧); the
  Advanced Education Class (高等教育班/中央军校); Xiaozhilong (消治龙, sulfa); the Little Red Devils/Ruijin;
  the tiger bench (老虎凳); the South China Evening News (南华晚报); Du Fu's 出师未捷身先死; Garrick/State
  Express 555 cigarettes. Rendered INLINE (not keyed): 祝慎之 Zhu Shenzhi; the classmate roster (唐与元/
  张学礼/张毓檀/吴菊生/杨继志/张维贤; the martyred 狄玺庭/李玉顺/刘士愚/丁履敬); bureau personnel 李肖白/周康;
  Wuhan-internship 刘培初/张树勋/陈仙洲.
- **B22 shelf (ch28; reuse; keyed with pinyin):** 朱升 Zhu Sheng (the servant who axed Fu Xiao'an,
  11 Oct 1940; variants 朱生/朱升源 and alias 陈中南 inline), 联合准备银行 the Federal Reserve Bank
  (North China puppet bank), 会审公廨 the Mixed Court. NEW ch28 notes: Cao Song's poem 一将功成万骨枯;
  the Double Tenth; the Great Way City Government; the Mixed Court; the Federal Reserve Bank (vs the
  Central Reserve Bank) + Cheng Xigeng's 1939 assassination; Yue opera / 盘夫索夫 / Yao Shuijuan; Yang
  Xiuqiong + Chu Minyi's carriage jibe; 官场现形记 "Officialdom Unmasked". Rendered INLINE (not keyed):
  裴可权 Pei Kequan, 盛礼约 Sheng Liyue (/盛郁 Sheng Yu), 王晓籁 Wang Xiaolai, 张法尧 Zhang Fayao,
  余祥琴 Yu Xiangqin, 杜洛 Duluo (the Frenchman shot by New Group One), 柳汝祥 Liu Ruxiang, 钱书城 Qian
  Shucheng, the one-off Japanese officers (臼井宽三 Usui Kanzō, 马渊 Mabuchi, 前田 Maeda, 谷荻 Yahagi,
  樱井 Sakurai, 曾弥 Sone, 青木 Aoki, 西园寺 Saionji, 犬养 Inukai, 木村市大郎 Kimura Ichitarō, 结城 Yūki,
  日高 Hidaka, 上田 Ueda), the sanctioned bank staff (季明远/张永纲/厉鼎模) and operatives (叶东山/赵家鑫/
  何凤祥/丁小宝/董威/田杰林/林镇城), 程锡庚 Cheng Xigeng, 曹松 Cao Song, 杨秀琼 Yang Xiuqiong, 姚水娟 Yao
  Shuijuan, 宋有圭 Song Yougui, 程/彭 Cheng/Peng, 杨惺华 Yang Xinghua, 徐谟 Xu Mo, 吴昆吾 Wu Kunwu.

## Voice sheet - CHEN GONGSHU (author / narrator)

- REGISTER: educated, formal, essayistic first person; grave and a touch archaic but not stilted.
  Long semicolon-joined clauses; four-character idiom and classical allusion used freely and
  footnoted when they carry weight. Refers to himself as 笔者 "the writer" and 我 "I." His narrating
  "shall" is DELIBERATE - do not de-formalize it; check_register flags it informationally (B06 33%,
  B08 29%, B12 43%, B15 33%, B16 36%, B18 25%, B19 67%, B20 83%, B21 0%, B22 22% - elevated when the
  chapter reproduces many quoted directives/documents; ch28 carries Dai's directive + two formal court
  agreements with "shall" clauses, so the narrating "shall" is back; ch27 carried no directives, so it
  did not arise there. NOT a de-formalization either way).
- STANCE: self-justifying yet self-effacing; insists on truthfulness, admits his blunders; tender
  toward dead comrades, bitter and scornful toward the enemy and the Communists. When quoting
  hostile/puppet/comrades' documents (memoirs, telegrams, news reports, the Zhou Fohai diary, the
  Mabuchi statement), keep the quoted register DISTINCT from Chen's own dry scorn.
- Ratio ~4.55-4.78 en/han in narrative; prefaces denser (~5.2-5.3); document-heavy chapters run
  higher (ch21 4.89, ch22 4.70, ch24 5.33, ch25 4.97, ch26 4.98, ch27 4.82, ch28 5.09 median). Read
  the note, do not reset.

## Voice sheets - principal & recurring cast

- **DAI LI (戴雨农 / Mr. Dai / 老板 "the Boss").** After ch17 only letters and telegrams; his word
  is "as a mountain." In ch28 his "非大流血不足以寒敌胆" directive is reproduced, and he approves the
  Fu Xiao'an reward (70,000 yuan) without a word about the missing prior ruling.
- **QI QINGBIN (齐庆斌) & ZHANG ZUOXING (张作兴).** Chen's childhood friends; the Shanghai District
  secretary and radio inspector. In ch28 Qi Qingbin handles the Fu Xiao'an case with his usual
  unreadable calm ("A promise given is to be kept").
- **ZHENG XIUYUAN (郑修元).** District secretary who held the Shanghai District together; his memoir
  沪滨三次历险实录 is quoted throughout Part Three.
- **LIU YUANSHEN (刘原深).** The very man who revises "Nameless Heroes" for Chen; his living
  memory-check throughout Part Three. In ch28 he is asked to serve two more months as acting commander
  of the First Action Brigade. **In ch29 his own first-person memoir (沪滨三次历险实录) is quoted at
  length** (sections 一/二, and continuing into ch30's section 三): a PLAINER, more novelistic voice
  than Chen's ("以平实的笔触"), full of dialogue - keep it distinct from Chen's dry essayistic scorn. He
  narrates walking into the Zhou Xiyuan/Zhu Min trap; ch30 (下) carries the trap sprung and his capture.
  He held fast under torture and kept the organization safe (威武不屈).
- **SUN DACHENG (孙大成).** The Kang Corps action leader; in ch28 he made a special trip Tianjin->
  Beiping over the Wang Shiying case, and his group sanctioned Cheng Xigeng (1939).
- **Dead comrades carried in memory:** ZENG CHE 曾澈, WANG WEN 王文; the ch26 martyrs; and now the
  Fu Xiao'an assassin ZHU SHENG (朱升), sent to the rear, fate unknown.

## ⚠ Name trap RESOLVED (do not reopen): 陈邦国 / 郑邦国

The Hanoi action-team member the source spells 郑邦国 in ch13 and 陈邦国 in ch15/ch16/ch17 is ONE
man. RESOLVED to **Chen Bangguo (陈邦国)**. Use Chen Bangguo consistently.

## Where the book stands

- Part One (北国锄奸) COMPLETE (B01-B05). Part Two ("Disgrace at Hanoi") COMPLETE (B06-B13).
- **Part Three ("Renown Won in a Hundred Battles" / 百战声威) nearly done (B14-B23).** ch20 =
  self-preface; ch21 = arrival + order of battle; ch22 = first 1940 sanctions + Fan Xing; ch23 =
  the "three-sided enemy" bridge; ch24 = the anatomy of the three-sided enemy + Yu Yefeng sanction
  + Dai's self-review; ch25 = the full work-review + arms-gift + Fan Xing puzzle; ch26 = the
  nameless martyrs; ch27 = the 张啸林 tycoon-death case; ch28 = the height of renown and blood
  (closing on Chen's own capture); ch29 = 第十章(上) the disaster chapter, Liu Yuanshen's memoir of
  the Zhou Xiyuan/Zhu Min trap (breaking off on 28 June 1941). REMAINING in Part Three: ch30 (第十章
  下) + ch31 (the Part-Three closing errata note).
- **NEXT: B24 = ch30 + ch31** (COMPLETES PART THREE). ch30 = 第十章 祸不单行 柱折梁摧(下), the SECOND
  half: section 三、仁者之心终为幺么所乘 onward - Liu Yuanshen's memoir carries the trap sprung and his
  capture, then from section 四 Chen resumes his OWN narration (per ch31 note #8). 1 <h2> + 110 <p>,
  NO <br/>/<img>/note-markers, drop=2; standalone 三、heading at p#0, a section 四 heading to FIND,
  severed-<p> candidates p#19/70/73/88. ch31 = 写在「英雄无名」第三部专书出版前, 1 <h1> + 14 <p>, drop=2;
  the enumerated 一、-八、 items (p#5-13) are an ERRATA LIST (DOCUMENT-CLAUSE body lines, NOT section
  headings). book.json's B23 array entry = ch30+ch31.

## What is NEXT

- Batch B24 = ch30 + ch31. Kickoff is the paste-block at the top. Runs to completion (no gate); ends by
  pasting the B25 kickoff. B24 COMPLETES PART THREE; B25 = ch32 (「平津绥靖」自序, the Part-Four author's
  preface; book.json's B24 = ch32 alone). Part Four "Pacification of the Beiping-Tianjin Region" =
  ch32-ch43 (ch33-ch42 carry book.json `sections` arrays - the 1946-49 civil-war material). Working
  batch labels run ONE AHEAD of book.json's batches array from ch24 on (ch24 = B18 … ch29 = B23,
  ch30+ch31 = B24).
- The frozen register reference is `reference/B01_frozen.md`. Narrative sits at 4.55-4.78 en/han;
  document-heavy chapters run higher (ch24 5.33, ch25 4.97, ch26 4.98, ch27 4.82, ch28 5.09) -
  alignment/register are the gates, not the raw ratio.
- Sub-heading pattern DIFFERS by chapter. Styles seen: Part One numbered 一/二/三; ch11/ch14/
  ch20-title/ch21-ch26 COUPLET-STYLE with NO number prefix; ch12/ch13/ch15/ch16/ch17/ch18-sections
  numbered-in-parens (一)/(二)…; ch27/ch28/ch29 use 一、二、三 enumerated headings (ch28 also had INNER
  一、二、三 document-clause lists that are NOT headings - judge by function). GLUED sub-heads seen
  ch08/ch16/ch18/ch22 (tail), ch24 (BOTH tail and HEAD), ch25 (two tail-glued), ch26 (two tail-glued,
  one ending in `」`), ch27 (two tail-glued, one ending in `」`), ch29 (one tail-glued after a
  terminal 。). Grep each new chapter p-by-p, and DISTINGUISH enumerated LIST items / document clauses
  (per parity) from 一、 / (一) SECTION headings and from run-in labels.
- WATCH for source anomalies: cuts, misplaced-「 glitches, corrupt/dropped-character phrases,
  dropped full stops, the "(第N章完，下期续载)" coda/magazine-seam pattern, a STRAY glyph fused onto a
  title, a STRAY orphan enumerator, stray ？, the ○ (U+25CB) and × redactions in addresses/names, a
  name glitch (ch28's 陈公傅 for 陈公博), variant forms (洋泾滨/洋泾浜), and pervasive single-character
  substitutions. Intra-<p> `<br/>` line breaks: PROSE splits MERGE, TABLE/roster rows are KEPT (ch26).
  Severed-<p> boundaries (a source <p> ending non-terminal) MERGE (ch25/ch26 each had 7, ch27 had 2,
  ch28 had 4). Re-grep each batch's source for `\[\d+\]` note markers (none through B22).

## Open items for the read-through / completion

- Feed decided renderings back to authority.json on completion: 军统 "the Juntong"; the full
  B02-B22 historical-name set.
- Japanese name readings to firm up when the men recur (多田骏, 田代皖一郎, 土肥原贤二, 板垣征四郎,
  近卫文麿, 影佐祯昭, 今井武夫, 晴气庆胤; 大屋久寿雄; 横山秋马; 岩井英一; the B18/B20 gendarmerie officers;
  the B22 one-off officers 臼井宽三 Usui Kanzō, 马渊 Mabuchi, 前田 Maeda, 谷荻 Yahagi, 樱井 Sakurai,
  曾弥 Sone, 青木 Aoki, 西园寺 Saionji, 犬养 Inukai, 木村市大郎 Kimura Ichitarō, 结城 Yūki, 日高 Hidaka -
  romaji to firm up).
- Provisional romanizations to firm up (glossary `provisional` rows, incl. the Shanghai-District
  cast, the B16 operatives, the B18/B19/B22 rows).
- Whole-book reconciliation items: ch09 "Jize County" (the 鸡泽县 key); the pinyin-vs-postal city
  names (standardized to pinyin from B18); the two B20 keyed-substring false positives (武汉卿 /
  劳勃生路) - both correct as rendered, flagged only by substring match. The B22 uncertain-road pinyin
  (祥德路/白赛仲路/恺自迩路/西爱咸斯路) and the transliterated foreign court-agreement signatories - candidates
  for a human read. Stray source glyph still to resolve: 毛酋 in a ch36 section title.

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01-B22 builds (0/0/0/0). Source is a clean digital
  EPUB, predominantly simplified with residual variant glyphs and pervasive digitization glitches
  (list them, render to plain sense, do not footnote mechanical typos). B01-B22 glitch lists in
  PROGRESS.md.
- Running-header line 英雄无名-陈恭澍 opens all 43 content files: drop it. drop count is variable -
  most drop=2; ch01/ch10/ch20 drop=3.
- Enumerated ；/：/、 bullet lists, quoted-document/directive/roster lines (INCLUDING intra-<p>
  `<br/>` TABLE rows, ch26, and INNER document-clause 一、二、三 lists, ch28), salutations, verse lines,
  juxtaposition lines, run-in section labels, and 『』-closed dialogue are DELIBERATE separate
  `<p>`/lines - do NOT merge them; only genuine mid-phrase splits (last char not terminal, OR a source
  `<p>` boundary that severs one sentence, OR an intra-<p> `<br/>` inside PROSE) merge, and those can
  CHAIN.
- Faithful numbering gaps/anomalies (NOT errors): Part Three skips 第七章 (ch27 = 第八章); ch10 splits
  into (上)/(下), and so does 第十章 of Part Three (ch29 = 上, ch30 = 下); 三面受敌 一往无前 titles two
  chapters (ch14 and ch24); ch09 printed §五 before §四; ch13 restarts its (一)-(五) numbering; ch16
  reproduces two whole Wang documents; ch21/ch22/ch24 carry magazine "下期续载" seams; ch24 has a
  source-internal date slip; ch25 has a 每日/每月 directive discrepancy (footnoted); ch26 marks a
  section 二、 with the "一、" only implicit; ch28 reproduces two whole court agreements as inner
  document-clause lists. Preserve and, where a reader would stumble, footnote.
- Expect a stray per-task branch at the top of every batch; consolidate onto claude/nameless-heroes
  per rule 2.
