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
Nameless Heroes B26

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once (its ONE failing regression test, "hook stands down on template stub", is a KNOWN false alarm; all others pass), then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05), B02 (ch06), B03 (ch07), B04 (ch08), B05 (ch09), B06 (ch10 preface + ch11), B07 (ch12), B08 (ch13), B09 (ch14), B10 (ch15), B11 (ch16), B12 (ch17), B13 (ch18 + ch19), B14 (ch20), B15 (ch21), B16 (ch22), B17 (ch23), B18 (ch24), B19 (ch25), B20 (ch26), B21 (ch27), B22 (ch28), B23 (ch29), B24 (ch30 + ch31) and B25 (ch32) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them. PARTS ONE, TWO ("Disgrace at Hanoi") and THREE ("Renown Won in a Hundred Battles" / 百战声威) are COMPLETE; PART FOUR ("Pacification of the Beiping-Tianjin Region" / 平津地区绥靖戡乱) is OPEN - ch32 was its self-preface. The EPUB now holds 32/43 chapters, 294 notes. NOTE on batch numbering: book.json's batches array lumps ch23+ch24 as "B17", so the working batch labels run ONE AHEAD of the book.json array from ch24 on (ch32 = working B25 = book.json's B24 entry; ch33 = working B26 = book.json's B25 entry).

Do Batch B26 = ch33 = 第一章 振衰起敝 二次出发 "Chapter 1. Reviving the Ailing, a Second Start" (ONE unit; the FIRST Part-Four NARRATIVE chapter, following the ch32 self-preface). This is where the 1946-49 civil-war narrative begins: Chen returns to Beiping and stands up the First Brigade of the 国防部绥靖总队 (the Pacification Corps). ch33 carries a book.json `sections` array [ch33s01 一、一支新制特种部队的产生 "The Birth of a New Special-Operations Unit"; ch33s02 二、重返旧地景物依稀 "Return to Old Ground, Faintly Familiar"; ch33s03 三、复杂的人事关系与重叠的工作任务 "Tangled Personnel Ties and Overlapping Duties"; ch33s04 四、亦师亦友战斗中的伙伴工作上的能手 "Mentors and Friends: Comrades in Battle, Masters at the Work"] - confirm all four title_en in book.json. Chen's Nationalist idiom stays at its sharpest here (共匪/匪 "the Communist bandits", 绥靖戡乱 "pacification and the suppression of rebellion") - PRESERVE it, do NOT soften; footnote where scholarship contests, text stands as written (book.json's translator_note commits to this). Read the tail of ch32 (out/ch32_reading.md) for the batch seam and the just-set Part-Four register/vocab. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch33 (34_index-split-000-0032.txt) from data/src. CONFIRM structure p-by-p against data/src_epub/OEBPS/Text/index_split_000_0032.xhtml [ch33: 1 <h2> (第一章 振衰起敝 二次出发) + 4 <h3> (the four section headings 一、/二、/三、/四、) + 153 <p>, NO <h1>/<br/>/<img>/[\d+] - CONFIRMED at B25]. **drop=2** (running header 英雄无名-陈恭澍 + <h2> chapter title). The FOUR section headings are SEPARATE <h3> ELEMENTS (they appear as their OWN whole lines in the txt) -> emit each as a `standalone ### ` in clean_batch.py (NOT tail-glued, unlike ch27-30's enumerated heads). After drop=2 the txt has 157 body lines = 4 section-heading lines + 153 <p> lines. Do the byte-exact p-by-p diff FIRST (the B19-B25 method: extract <p> inner text AND the <h3> texts in document order, walk each consuming 1 body line, assert every line matches) to PIN the 4 heading line-numbers and to LOCATE any SEVERED-<p> boundaries (last char non-terminal -> MERGE; at least p#13 ends non-terminal on 、: …你与副厅长张炎元、 - confirm and merge its chain). CRITICAL: the INNER 一、二、三、四 enumerations are BODY lines, NOT headings, kept per parity (the ch27-30 lesson): the number-range 三、四岁 / 二十二、三年 (p#39, p#55-57), the name-list 陈资一、周世光 (p#112), 第二、三、四部书 (p#145), and the quoted committee-duties list 一、…二、…三、…四、 inside one <p> (p#146). Extend scripts/clean_batch.py with ch33's spec (drop=2; the 4 confirmed standalone <h3> heading line-numbers; any confirmed severed-<p> merges; NO glued/glued_head unless the diff reveals one). Run it (source-conservation check must pass). Write out/ch33_reading.md (## from book.json title_en; the 4 sections as ### sub-headings from book.json section title_en; one English paragraph per source body line). Then run scripts/batch_artifacts.py ch33, and ALWAYS finish with a NO-ARG run (the trap: an ID-run writes checks.json with ONLY that unit; the no-arg run restores all 33 units so check_structure/check_content see them).
2. Translate to the FROZEN register (Chen's voice sheet in HANDOFF; NARRATIVE runs ~4.55-4.78 en/han, NOT the preface's 5.2-5.57 band; the narrating "shall" is DELIBERATE, do NOT de-formalize). Consult glossary.json and authority.json BEFORE romanizing anything; REUSE the B25-settled Part-Four renderings (in PROGRESS.md "Settled Part-Four renderings"): 军统/军统局 "the Juntong"/"the Juntong Bureau"; the place PINYIN convention (北平 Beiping, 天津 Tianjin); 绥靖总队 "the Pacification Corps" (KEYED B25), 总队 "Corps"/总队长 "Corps Commander", 大队 "brigade"/大队长 "brigade commander" (B24), 中队 "company", 分队 "sub-brigade", 指挥室 "command room", 指挥员 "commanding officer" vs 指挥官 "commander", 突击队 "assault team", 直属组 "directly subordinate section", 部队长 "unit commander", 编制 "establishment", 配属关系 "relation of attachment", 留置工作 "stay-behind work", 绥靖 "pacification"/戡乱 "suppression of rebellion"/剿匪 "bandit-suppression"/匪谍 "Communist spies"/共酋 "Communist chieftains"/共干 "Communist cadres", 收复区 "recovered areas"/交战区 "combat zones", 行辕 "Field Headquarters". KEYED B25 people to reuse: 叶剑英 Ye Jianying, 刘培初 Liu Peichu, 李宗仁 Li Zongren, 傅作义 Fu Zuoyi, 计兆祥 Ji Zhaoxiang; orgs 军事调处执行部 the Military Mediation Executive Headquarters, 军事三人小组 the Committee of Three, 励志训练班 the Lizhi Training Class; term 励志计划 the Lizhi Plan. NEW ch33 vocabulary to DECIDE and key as it recurs: 特种部队 (book.json ch34s01 title_en glosses it "Special Forces"; but ch33s01 新制特种部队 title_en = "New Special-Operations Unit" - RECONCILE to one rendering and use it consistently, keying it), 特种组织 "Special Organization" (ch34s01), and the recurring cast that reappears (吴安之 and the 张炎元/侯腾 command chain, and the many operatives named in section 四). Render Republican years literally (三十五年 = 1946 … 三十八年 = 1949; checker matches the source numeral or auto-escapes via +1911). WATCH the digitization glitches (list in PROGRESS.md, render to plain sense, footnote only real reading uncertainty): same classes seen throughout (single-char substitutions, dropped stops, dittography, mismatched guillemets ﹁﹂﹃﹄, stray ？/》/！, ○/× redactions - the numeric checker mis-reads ○; carry the real value in English and noise only the mis-read glyph-string; × redactions render as em-dash blanks). Dates/counts: carry real values as DIGITS/words; NOISE only idiom/approximate/name-numeral/elided/date-name forms (data/noise.txt already carries the B01-B25 rules; add B26's; watch the 二十二、三年 elided-year and 三、四岁 range).
3. Checks: verify_unit.py ch33 (parity + numbers with noise auto-found + anchors); check_align.py ch33; regenerate checks.json with scripts/batch_artifacts.py (no args) and run check_structure.py --config checks.json + check_content.py --config checks.json (NOTE: check_content prints KNOWN PRE-EXISTING artifacts and exits nonzero because of them - ch08 Shunde ×3, ch13 ×9, ch09 "Jize County" ×1, ch26's TWO documented keyed-substring FALSE POSITIVES 武汉卿/劳勃生路; CONFIRM ch33 shows "all in the paired paragraph" / 0 displaced, and align any keyed name/place/TERM to its glossary-decided rendering. A NEW unit's displacements are almost always a keyed name/place/term rendered a DIFFERENT way than the glossary - align the English to the keyed form; the exception is a keyed name that is a SUBSTRING of a larger different referent, a documented false positive, not a fix). Do NOT add COMMON-NOUN or book/periodical keys. qc_entities.py on a reconstructed bilingual (data/zh body lines minus the `### ` heading lines + out/ch33_en.json, `> zh` / en pairs; every glossary row needs a pinyin field - the reconstruction one-liner is in PROGRESS/the ch30-ch32 method). Verify the TAIL against the source. check_register.py --ref reference/B01_frozen.md out/ch33_reading.md ("shall" deliberate; NARRATIVE ratio, so expect ~4.6-4.8, LOWER than ch32's preface - alignment/register are the gates, not the raw ratio).
4. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (full list in PROGRESS.md; the big already-covered furniture incl. now, from B25: the Nationalist 绥靖/戡乱/共匪 civil-war framing, the Marshall Mission/Committee of Three/Executive Headquarters, the Lizhi Plan, the Jiangxi bandit-suppression/别働总队, the Youth Army, the five rail lines, Fu Zuoyi/Beiping's surrender, Fenghua/Chiang's retirement, the Temple of Agriculture; plus older furniture No.76/特工总部 ch04/ch17, 制裁, 忠义救国军 ch21, 蓝衣社 ch08). ch33 opens the on-the-ground civil-war narrative, so expect NEW items (the 特种部队/特种组织 concept if a reader needs it; Beiping-region geography/institutions the chapter introduces; period military terms; any classical allusion). Be generous but do NOT pad, do NOT re-note. Merge notes via apparatus_merge.py (positional arg: apparatus_merge.py data/ch33_apparatus.json; numeric character references only in note bodies; anchors verbatim ASCII substrings of the reading.md body text, NO em dash and NO quote/apostrophe character - substring traps; multi-occurrence anchors attach at the first; TIGHTEN a generic anchor if it would match an earlier paragraph). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field; apparatus_merge's glossary path assumes a FLAT map and would corrupt the sectioned file - use it ONLY for notes; scripts/add_ch32_glossary.py is the latest by-hand pattern, asserting each hanzi key against data/zh, and covers people/organizations/terms sections). Confirm ch33 carries no images (no <img> - confirmed). For any CJK in a note body use the make_ch32_apparatus.py pattern (author bodies with typed hanzi + untoned pinyin, ASSERT every non-ASCII glyph is present in data/zh/ch33.txt, then convert to NCRs) to defeat the CJK-mangling hazard - and remember a CORRECT glyph may be ABSENT if the source prints a glitch/variant form, so describe such terms with the source's own form + pinyin.
5. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; update HANDOFF.md; commit and push to claude/nameless-heroes. (Next is B27 = ch34 = 第二章 自动自发 同心同德, which also carries a book.json `sections` array [ch34s01-ch34s03]; ch33-ch42 all carry `sections` arrays; confirm scope in book.json. Working batch labels run ONE AHEAD of book.json's batches array: book.json B26 = ch34 = working B27. Part Four = ch32-ch43; after ch42 only ch43 = the Afterword remains.)

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B27 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
```

## What is DONE (do not redo)

- **Step 0 (survey).** Ingest + book.json (43 chapters, 5 TOC parts) + skeleton EPUB.
- **Batch B01 (ch01-ch05), the front matter.** 67 notes. **VOICE GATE PASSED:** the B01
  front matter is the FROZEN register reference (`reference/B01_frozen.md`) from B02 on.
- **B02-B05 (ch06-ch09). Part One COMPLETE.**
- **B06-B13 (ch10-ch19). Part Two ("Disgrace at Hanoi") COMPLETE.**
- **Batch B14 (ch20), PART THREE OPENS.** ch20 = the Part-Three self-preface.
- **B15-B24 (ch21-ch31). Part Three ("Renown Won in a Hundred Battles" / 百战声威) COMPLETE.**
  Detail per batch in PROGRESS.md.
- **Batch B25 (ch32), OPENS PART FOUR.** ch32 (自序) = the Part-Four self-preface (parallel to
  ch10/ch20): drop=3 (running header + <h1> 平津地区绥靖戡乱 part super-title + <h3> 自序); 1 <h1> +
  1 <h3> + 35 <p>, NO <br/>/<img>/note-markers, byte-exact p-by-p, NO severed-<p> merges, no section
  headings inside (the two numeral-opening body sentences kept as body lines). 35 body paragraphs;
  ratio 5.57 (preface, denser). 10 notes (294 cumulative); 10 net-new keyed glossary rows (5 people,
  4 orgs, 1 term). The 1946-49 civil-war material begins; the Nationalist idiom (共匪/绥靖戡乱) framed
  by a footnote, preserved not softened. check_content 0 displaced; qc 0 misses; register within
  tolerance. qa_epub PASS; epubcheck 0/0/0/0. **EPUB now 32/43 chapters.** Detail in PROGRESS.md
  ("Batch B25").

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` - derives data/zh/<id>.txt verbatim from data/src, applying per-unit
  drops/merges/heading-splits with a source-conservation check. Specs for ch01-ch32. Merge logic
  FOLLOWS CHAINS. **drop is variable:** most chapters drop=2; ch01/ch10/ch20/ch32 drop=3 (a part
  super-title precedes the preface). `standalone` = a sub-heading kept as its own <p>/line with no
  heading markup, emitted as `### ` (used for both plain-<p> sub-heads AND separate <h3> section
  elements, cf. ch33's four <h3>); `glued` = a heading fused onto a paragraph's TAIL (endswith),
  split off; `glued_head` = a heading fused onto a paragraph's HEAD (startswith), split off; `merges`
  = source <p> pairs that sever one sentence OR an intra-<p> `<br/>` line break. **A chapter can carry
  INNER enumerated 一、二、三 / 第一、第二 DOCUMENT-CLAUSE or NUMBER-RANGE or NAME-LIST content that is
  NOT a section heading - keep those as ordinary body lines per parity, judged by function** (ch27-32;
  ch33 has 三、四岁 / 二十二、三年 / 陈资一、周世光 / a committee-duties 一、二、三、四 list, all body).
- `scripts/batch_artifacts.py` - derives out/<id>_en.json FROM out/<id>_reading.md and writes
  checks.json. Author the reading.md; run this. **TRAP: running it with an ID writes checks.json
  with ONLY that unit; ALWAYS finish with a no-arg run.**
- `scripts/verify_unit.py <id>` - parity + numbers (auto-finds data/noise.txt; do NOT pass
  --noise) + anchors. Run per unit.
- **qc_entities bilingual reconstruction (one-liner):** for each unit, read data/zh/<id>.txt,
  keep non-`### ` lines as body, zip with out/<id>_en.json, write `> <zh>\n\n<en>\n\n` pairs to
  out/<id>_bilingual.md, run `qc_entities.py out/<id>_bilingual.md`. Bilinguals are QC-only, never
  ship, gitignored/regenerable.
- `scripts/build_reading_epub.py` - builds out/nameless-heroes.epub. Uses book.json `title_en`
  for the visible chapter H1; `### ` sub-headings render as <h2>; notes collect in
  OEBPS/notes.xhtml with popup semantics.
- `scripts/check_content.py` (patched) - name_map skips "_"-prefixed glossary categories. It
  flags KNOWN PRE-EXISTING artifacts and exits NONZERO: **ch08 Shunde (3), ch13 (9), ch09 "Jize
  County" (1)** - NOT regressions. **B20's TWO documented keyed-substring FALSE POSITIVES: 武汉 "Wuhan"
  matching inside 武汉卿 "Wu Hanqing"; 劳勃生 "Lao Bosheng" matching inside 劳勃生路 "Robison Road".**
  The pass criterion for a NEW batch is "the batch's own unit shows all name occurrences in the paired
  paragraph / 0 displaced" - EXCEPT a keyed name that is a substring of a larger different referent, a
  documented false positive, not a fix. A NEW unit's TRUE displacements are almost always a keyed
  name/place/TERM rendered a DIFFERENT way than the glossary: align the English to the keyed form.
  **B25 lesson: do NOT key a place/term whose hanzi is a substring of a DIFFERENT keyed rendering** -
  河北 (Hebei) was NOT keyed because it is a substring of the keyed 河北大经路 -> "Dajing Road" (which
  carries no "Hebei"); and 绥远/戡乱 were left inline (standard/common-noun, appear in many chapters).
  Do NOT add book-TITLE or COMMON-NOUN keys.
- **Verse marker `{p}`** (ch13, reused ch26 for the 挽联): prefix a pure-verse line with `{p} `;
  the builder renders `<p class="verse">`; the checks strip it.
- Glossary is authored/merged BY HAND into the SECTIONED file (book/people/organizations/places/
  terms), idempotent + re-read-verified. **Every row MUST carry a `pinyin` field** - qc_entities
  does `rec["pinyin"]` and KeyErrors otherwise. `scripts/add_ch32_glossary.py` is the latest by-hand
  pattern: covers people/organizations/terms sections in one pass, asserts each hanzi key is a
  substring of data/zh/ch32.txt. A `/`-joined key holds alternate hanzi for one referent; qc splits
  on `/`. apparatus_merge's glossary path assumes a FLAT map and would corrupt the sectioned file;
  NOTES still go through apparatus_merge.py (positional arg, e.g. `apparatus_merge.py data/ch33_apparatus.json`).
- **qc_entities catches term-rendering drift too:** a glossary common-noun term rendered a
  different way flags as a "miss." Align the English to the glossary. (qc has a first/last-word
  fallback, so a keyed en that starts with "the" is trivially satisfied - prefer distinctive en.)
- **GLOSSARY-KEY DISCIPLINE:** a key must be a DISTINCTIVE proper noun (or a distinctive institution)
  that renders ONE way everywhere. Periodicals and books are FOOTNOTES/inline, not keys. One-off
  transliterated Western/Japanese officer names, one-off telegram/roster names, standard province
  names, and attested Shanghai ROADS are inline, not keyed. A bare surname whose full name is unknown
  is rendered inline. And NEVER key hanzi that is a substring of a different keyed rendering (B25 河北).
- **Note-anchor gotchas:** anchors must be ASCII, WITHOUT any quote/apostrophe character AND
  without an em dash (U+2014) - all substring traps. The reading.md uses curly quotes and em
  dashes freely, so pick an anchor phrase with none of them. **Multi-occurrence anchors attach at
  the FIRST occurrence** - and if a short generic anchor would match an EARLIER paragraph than the
  one you mean, LENGTHEN it.
- **make_ch32_apparatus.py pattern (scripts/):** author note bodies as plain ASCII + typed hanzi +
  UNTONED pinyin + straight quotes, allow em-dash, ASSERT every non-ASCII glyph occurs in THAT UNIT's
  data/zh/<id>.txt, then convert every non-ASCII char to a numeric char ref and run apparatus_merge.py.
  **A CORRECT glyph may be ABSENT if the source prints a glitch/variant** - describe such terms with
  the source's own form + pinyin/English. A note that quotes ANOTHER unit's text is authored
  ENGLISH-ONLY to avoid the cross-unit glyph-assert. AVOID tone-marked pinyin and curly quotes in
  note bodies (they trip the per-glyph assert unless present in that unit's zh).
- data/noise.txt carries the B01-B25 project noise rules (each with a comment line). Republican
  years render literally; the checker matches the source numeral (or auto-escapes Republican-year
  N via N+1911). The elided-tens block is ordered LONGEST-FIRST. Name-numeral glyphs are noised.
  **Idiom numerals are noised** (B25 added 百废待兴 / 百事待擧, where 百 = "myriad," not 100; earlier
  退一万步, 万一, 五旬 etc.). **The ○ (U+25CB) address artifact:** the checker cannot read ○ as zero -
  noise the mis-read glyph-string, carry the real value in the English. **× (source redaction)**
  renders as an em-dash blank. Every REAL value is CARRIED and matched as DIGITS. Word-map needs "a
  thousand"/"a hundred" (bare "thousand"/"hundred" after a noun do NOT count as 1000/100).
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches it; re-run per session).
  setup.sh's ONE failing regression test ("hook stands down on template stub") is a KNOWN false
  alarm; all other regression tests pass.

## Renderings settled / carry-forward

- 军统 / 军统局 -> "the Juntong" / "the Juntong Bureau" (DECIDED). 戴笠 Dai Li (courtesy Yunong;
  老板 "the Boss"; 戴先生 "Mr. Dai"; 戴雨农 "Dai Yunong"); 汪精卫 Wang Jingwei (汪逆 "the traitor
  Wang"). 制裁 "sanction"; 制裁令 "sanction order." 敌伪 "the enemy and the puppets"; 汪伪 "Wang
  puppets"; 沦陷区 "the fallen zone(s)"; 战区 "war zone"; 后方 "the rear"; 区长 "District Chief";
  区本部/区部 "District Headquarters"; 督察 "inspector." Chiang's titles: 校长 "the Commandant",
  委员长/委座 "the Generalissimo", 总裁 "the Director-General"; 领袖 "the Leader"; 总理 "the Party
  Leader" (Sun Yat-sen). 日本宪兵队 "the Japanese gendarmerie"; 七十六号 "No. 76"; 特工总部 "Special
  Operations Headquarters"; 工部局 "Municipal Council"; 公董局 "French Municipal Council"; 公共租界
  "International Settlement"; 法租界 "French Concession"; 巡捕房 "station house"; 三民主义 "the Three
  Principles of the People."
- **B24 (Shanghai unit vocab):** 大队长 "brigade commander"; 分队 "sub-brigade"; 三道头 "three-stripe
  head" (Concession police sergeant); 猪笼车 "pig-cage van"; 高洋房 "High Foreign House"; 内交通/内交站
  "internal courier"/"internal courier station"; 預备区/第二区 "Reserve District"/"Second District".
- **B25 PART-FOUR vocab (in PROGRESS.md "Settled Part-Four renderings"; reuse):** 总队 "Corps" / 总队长
  "Corps Commander"; 大队 "brigade"; 中队 "company"; 指挥室 "command room"; 指挥员 "commanding officer"
  vs 指挥官 "commander"; 突击队 "assault team"; 直属组 "directly subordinate section" / 直属员
  "directly subordinate agent"; 部队长 "unit commander"; 部队代号 "unit code-name"; 编制 "establishment";
  配属关系 "relation of attachment"; 留置工作 "stay-behind work"; 绥靖 "pacification" / 戡乱 "suppression
  of rebellion" / 剿匪 "bandit-suppression" / 匪谍 "Communist spies" / 共酋 "Communist chieftains" / 共干
  "Communist cadres"; 收复区 "recovered areas" / 交战区 "combat zones"; 军需官 "quartermaster"; 行辕
  "Field Headquarters" / 行辕主任 "director"; 剿匪总部/绥靖公署 "Bandit Suppression Headquarters"/
  "Pacification Office". Republican years literal (三十五年 = 1946 … 三十八年 = 1949).
- **PLACE-NAME CONVENTION (the qc gate enforces the glossary's PINYIN for keyed cities):**
  北平 Beiping, 天津 Tianjin, 汉口 Hankou, 四川 Sichuan, 虹口 Hongkou, 重庆 Chongqing, 闸北 Zhabei.
  KEYED roads: 愚园路 "Yuyuan Road", 冀东 "East Hebei". Non-keyed attested Shanghai ROADS keep their
  historical forms (Avenue Joffre, Seymour Road, Bubbling Well Road, Robison Road 劳勃生路 - NOT "Lao
  Bosheng Road"; the officer 劳勃生 is keyed "Lao Bosheng", a documented substring false positive).
  Standard provinces render inline in pinyin (河北 Hebei, 绥远 Suiyuan, 山东 Shandong, 河南 Henan,
  山西 Shanxi, 察哈尔 Chahar [keyed], 热河 Rehe [keyed]); 归绥 Guisui.
- **Book / part titles (in-text; DECIDED; reuse verbatim):** 英雄无名 = "Nameless Heroes"; Part One
  北国锄奸 = "Rooting Out Traitors in the North"; Part Two = "Disgrace at Hanoi"; Part Three 百战声威
  = "Renown Won in a Hundred Battles"; **Part Four 平津地区绥靖戡乱 = "Pacification of the Beiping-Tianjin
  Region" (book.json `part`; the in-text super-title).** 蓝衣社 = "the Blue Shirt Society" (NOTED ch08).
  忠义救国军 = "the Loyal and Patriotic Army" (NOTED ch21). 抗日杀奸团 / 抗团 = "the Anti-Japanese
  Traitor-Killing Corps" / "the Kang Corps" (NOTED ch02/ch11). Books by FOOTNOTE/inline (not glossary):
  刘培初's 浮生掠影集 "Fleeting Glimpses of a Floating Life" (quoted ch32); 蒋总统秘录, 戴雨农先生传,
  刘原深's 沪滨三次历险实录, 官场现形记 "Officialdom Unmasked", 梨园掌故 "Anecdotes of the Pear Garden";
  periodicals 申报 Shenbao, 大公报 Ta Kung Pao.
- **B25 shelf (ch32; reuse; all keyed with pinyin):** 叶剑英 Ye Jianying (Communist rep on the
  Executive HQ; later a PRC marshal), 刘培初 Liu Peichu (Pacification Corps Commander; memoir author;
  = the Wuhan practice-corps leader of ch29), 李宗仁 Li Zongren (Beiping Field HQ director; 1949 acting
  president), 傅作义 Fu Zuoyi (North China Bandit Suppression C-in-C; the negotiated surrender of
  Beiping Jan 1949), 计兆祥 Ji Zhaoxiang (stay-behind wireless operator, martyr); orgs 绥靖总队 the
  Pacification Corps, 军事调处执行部 the Military Mediation Executive Headquarters, 军事三人小组 the
  Committee of Three, 励志训练班 the Lizhi Training Class; term 励志计划 the Lizhi Plan. Rendered INLINE
  (one-off): 马歇尔 Marshall, 罗柏森 Colonel Robertson, 侯腾 Hou Teng, 徐启明 Xu Qiming, 张家铨 Zhang
  Jiaquan, 史泓 Shi Hong, 雷处长 Director Lei.
- **Earlier shelves (B15-B24)** remain in PROGRESS.md and prior HANDOFFs; the whole B02-B24 cast is
  keyed. Consult glossary.json before romanizing anything.

## Voice sheet - CHEN GONGSHU (author / narrator)

- REGISTER: educated, formal, essayistic first person; grave and a touch archaic but not stilted.
  Long semicolon-joined clauses; four-character idiom and classical allusion used freely and
  footnoted when they carry weight. Refers to himself as 笔者 "the writer" and 我 "I." His narrating
  "shall" is DELIBERATE - do not de-formalize it; check_register flags it informationally (elevated
  when a chapter reproduces many quoted directives/documents, low in dialogue-heavy narrative; NOT a
  de-formalization either way).
- STANCE: self-justifying yet self-effacing; insists on truthfulness, admits his blunders; tender
  toward dead comrades, bitter and scornful toward the enemy and the Communists. When quoting
  hostile/puppet/comrades' documents, keep the quoted register DISTINCT from Chen's own dry scorn.
  **Part Four (from ch32) is the 1946-49 civil war: the Nationalist idiom sharpens (共匪 "the Communist
  bandits", 绥靖戡乱 "pacification and the suppression of rebellion") - PRESERVE it, footnote where
  contested, text stands.**
- Ratio ~4.55-4.78 en/han in NARRATIVE; prefaces denser (ch20 self-preface; ch32 self-preface 5.57);
  document-heavy chapters run higher. Read the note, do not reset. ch33 is Part-Four NARRATIVE, so
  expect the ~4.6-4.8 band, LOWER than ch32's preface.

## Voice sheets - principal & recurring cast (Part Four)

- **CHEN GONGSHU himself.** Part Four is the sequel he promised at the close of Part Three: his own
  role, "without the least disguise." He commands the First Brigade of the Pacification Corps in the
  Beiping-Tianjin region, 1946-49.
- **ZHENG JIEMIN (郑介民 / Mr. Zheng).** Chen's old Beiping-days superior, now the government
  representative on the Military Mediation Executive Headquarters and head of the Lizhi Training Class;
  Chen works under his leadership through Part Four (still under him in autumn 1949, ch32 close).
- **DAI LI (戴雨农 / the Boss).** Died in a 1946 air crash (NOTED ch02/ch25); the Juntong reorganizes
  into the Ministry of National Defense in the postwar period.
- **LIU PEICHU (刘培初).** Corps Commander of the Pacification Corps; author of the quoted memoir
  Fleeting Glimpses of a Floating Life; earlier led the Wuhan practice corps (ch29).

## ⚠ Name trap RESOLVED (do not reopen): 陈邦国 / 郑邦国

The Hanoi action-team member the source spells 郑邦国 in ch13 and 陈邦国 in ch15/ch16/ch17 is ONE
man. RESOLVED to **Chen Bangguo (陈邦国)**. Use Chen Bangguo consistently.

## Where the book stands

- Part One (北国锄奸) COMPLETE (B01-B05). Part Two ("Disgrace at Hanoi") COMPLETE (B06-B13). Part
  Three ("Renown Won in a Hundred Battles" / 百战声威) COMPLETE (B14-B24).
- **Part Four ("Pacification of the Beiping-Tianjin Region") OPEN: B25 = ch32 (the self-preface) DONE.**
- **NEXT: B26 = ch33** = 第一章 振衰起敝 二次出发 "Chapter 1. Reviving the Ailing, a Second Start" - the
  FIRST Part-Four NARRATIVE chapter. Structure CONFIRMED at B25: 1 <h2> + 4 <h3> (section headings
  一、/二、/三、/四、) + 153 <p>, NO <h1>/<br/>/<img>/note-markers, **drop=2**; the 4 <h3> are SEPARATE
  elements -> `standalone ### ` (NOT tail-glued); at least one severed-<p> at the 张炎元、 boundary
  (p#13); the inner 一、二、三、四 enumerations/ranges/name-lists (三、四岁 / 二十二、三年 / 陈资一、周世光 /
  第二、三、四部书 / a committee-duties list) are BODY lines. book.json ch33 carries `sections`
  [ch33s01-ch33s04]. NEW vocab: reconcile 特种部队 ("Special Forces" per ch34s01 title vs "Special-
  Operations Unit" per ch33s01 title) to ONE rendering + key it; 特种组织 "Special Organization".
- After B26: B27 = ch34 (第二章 自动自发 同心同德, `sections` ch34s01-ch34s03). Part Four = ch32-ch43;
  ch33-ch42 carry `sections` arrays (the 1946-49 civil-war narrative); ch43 = the Afterword. Working
  batch labels run ONE AHEAD of book.json's batches array from ch24 on (ch32 = B25, ch33 = B26).
- The frozen register reference is `reference/B01_frozen.md`. Narrative sits at 4.55-4.78 en/han;
  prefaces denser (ch32 = 5.57); document-heavy chapters higher - alignment/register are the gates,
  not the raw ratio.
- Sub-heading pattern DIFFERS by chapter. Part Four chapters ch33-ch42 carry book.json `sections`
  arrays; the section headings appear in the source as SEPARATE <h3> ELEMENTS (ch33 confirmed) that
  emit as `standalone ### `. DISTINGUISH enumerated LIST items / document clauses / number-ranges /
  name-lists (kept as body lines per parity) from the true section headings. Grep each new chapter
  p-by-p.
- WATCH for source anomalies: cuts, misplaced-「 glitches, corrupt/dropped-character phrases, dropped
  full stops, a STRAY glyph fused onto a title, stray ？/》/！, the ○ (U+25CB) and × redactions, name
  glitches, variant forms, and pervasive single-character substitutions. Intra-<p> `<br/>` line breaks:
  PROSE splits MERGE, TABLE/roster rows are KEPT. Severed-<p> boundaries (a source <p> ending
  non-terminal) MERGE. Re-grep each batch's source for `\[\d+\]` note markers (none through B25).

## Open items for the read-through / completion

- Feed decided renderings back to authority.json on completion: 军统 "the Juntong"; the full
  B02-B25 historical-name set; the Part-Four vocabulary (绥靖/戡乱/绥靖总队/励志计划 etc.).
- Japanese name readings to firm up when the men recur (multi-Part list in prior HANDOFFs).
- Provisional romanizations to firm up (glossary `provisional` rows, incl. the Shanghai-District
  cast, the B16-B25 operatives; 刘培初 Liu Peichu / 计兆祥 Ji Zhaoxiang marked provisional).
- Whole-book reconciliation items: ch09 "Jize County" (the 鸡泽县 key); the pinyin-vs-postal city
  names (standardized to pinyin from B18); the two B20 keyed-substring false positives (武汉卿 /
  劳勃生路) - both correct as rendered. The Malone spelling (ch30, one officer, footnoted). Stray
  source glyph still to resolve: 毛酋 in a ch36 section title (book.json renders it "the Bandit Chief").
  The ch32 "Fifth Part" numbering discrepancy (footnoted; Chen's own count).

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01-B25 builds (0/0/0/0). Source is a clean digital
  EPUB, predominantly simplified with residual variant glyphs and pervasive digitization glitches
  (list them, render to plain sense, do not footnote mechanical typos). B01-B25 glitch lists in
  PROGRESS.md.
- Running-header line 英雄无名-陈恭澍 opens all 43 content files: drop it. drop count is variable -
  most drop=2; ch01/ch10/ch20/ch32 drop=3.
- Enumerated ；/：/、 bullet lists, quoted-document/directive/roster lines (INCLUDING intra-<p>
  `<br/>` TABLE rows and INNER document-clause / range / name-list / 第一、第二 lists), salutations,
  verse lines, run-in section labels, and 『』/「」-closed dialogue are DELIBERATE separate `<p>`/lines
  - do NOT merge them; only genuine mid-phrase splits (last char not terminal, OR a source `<p>`
  boundary that severs one sentence, OR an intra-<p> `<br/>` inside PROSE) merge, and those can CHAIN.
  The ：-ended lead-in (memoir/document/dialogue) stays SEPARATE.
- Faithful numbering gaps/anomalies (NOT errors): Part Three skips 第七章 (ch27 = 第八章); 第十章 splits
  into (上)/(下) (ch29/ch30); 三面受敌 一往无前 titles two chapters (ch14 and ch24); ch32 numbers the
  Beiping-Tianjin volume "the Fifth Part" though Shanghai was "the Third Part" (footnoted). Preserve
  and, where a reader would stumble, footnote.
- Expect a stray per-task branch at the top of every batch; consolidate onto claude/nameless-heroes
  per rule 2.
