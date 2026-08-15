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
Nameless Heroes B25

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once (its ONE failing regression test, "hook stands down on template stub", is a KNOWN false alarm; all others pass), then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05), B02 (ch06), B03 (ch07), B04 (ch08), B05 (ch09), B06 (ch10 preface + ch11), B07 (ch12), B08 (ch13), B09 (ch14), B10 (ch15), B11 (ch16), B12 (ch17), B13 (ch18 + ch19), B14 (ch20), B15 (ch21), B16 (ch22), B17 (ch23), B18 (ch24), B19 (ch25), B20 (ch26), B21 (ch27), B22 (ch28), B23 (ch29) and B24 (ch30 + ch31) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them. PARTS ONE, TWO ("Disgrace at Hanoi") and THREE ("Renown Won in a Hundred Battles" / 百战声威) are COMPLETE. The EPUB now holds 31/43 chapters, 284 notes. NOTE on batch numbering: book.json's batches array lumps ch23+ch24 as "B17", so the working batch labels run ONE AHEAD of the book.json array from ch24 on (ch24 = B18 … ch30+ch31 = B24, ch32 = B25). book.json's B24 array entry = ch32 alone; working B25 = ch32, which OPENS PART FOUR.

Do Batch B25 = ch32 = 自序 "Author's Preface" (ONE unit; OPENS PART FOUR "Pacification of the Beiping-Tianjin Region" / 平津地区绥靖戡乱; confirm title_en in book.json = "Author's Preface"). This is the Part-Four self-preface, parallel to the ch10/ch20 part-prefaces. Part Four is the 1946-49 CIVIL-WAR material: after the Japanese surrender Chen commands a special unit (the 平津区特种部队) in the Nationalist-Communist fighting around Beiping and Tianjin. Chen's Nationalist idiom is at its sharpest here: the Communists are 共匪/匪 "the Communist bandits", the war is 绥靖戡乱 "pacification and the suppression of rebellion" - PRESERVE the idiom, do NOT soften it (book.json's translator_note commits to this: "the Communist forces are 'bandits,' the war of 1946-49 a 'pacification'"; footnote where scholarship contests, text stands as written). Read the tail of ch31 (out/ch31_reading.md, the erratum note) and the ch20 self-preface (out/ch20_reading.md) for the part-preface register. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch32 (33_index-split-000-0031.txt) from data/src. CONFIRM structure p-by-p against data/src_epub/OEBPS/Text/index_split_000_0031.xhtml [ch32: 1 <h1> + 1 <h3> + 35 <p>, NO <h2>/<br/>/<img>/[\d+] - CONFIRMED at B24]. **drop=3** (running header 英雄无名-陈恭澍 + <h1> 平津地区绥靖戡乱 [the PART-FOUR super-title, handled by book.json `part`, NOT a chapter heading] + <h3> 自序 [the preface title]) - the ch10/ch20 drop=3 pattern. First body line after drop=3 is 缅怀一辈小兄弟们… (CONFIRM). Do the byte-exact p-by-p diff FIRST (the B19-B24 method: extract <p> inner text, walk each <p> consuming 1 body line, assert every <p> matches its body line) to CONFIRM 35=35 and to LOCATE any SEVERED-<p> boundaries (last char non-terminal → MERGE; parity is data/zh↔reading.md). NO section headings inside (the two enumerated-looking line starts 五个指挥室… p#? and 三十八年一月杪… are BODY sentences beginning with a numeral, NOT headings - keep as body lines). Extend scripts/clean_batch.py with ch32's spec (drop=3; any confirmed severed-<p> merges; NO standalone/glued headings unless the diff reveals one). Run it (source-conservation check must pass). Write out/ch32_reading.md (## from book.json title_en "Author's Preface"; one English paragraph per source body line). Then run scripts/batch_artifacts.py ch32, and ALWAYS finish with a NO-ARG run (the trap: an ID-run writes checks.json with ONLY that unit; the no-arg run restores all 32 units so check_structure/check_content see them).
2. Translate to the FROZEN register (Chen's voice sheet in HANDOFF; prefaces run DENSER, ~5.2-5.3 en/han - the ch20 self-preface was in that band; the narrating "shall" is DELIBERATE, do NOT de-formalize). Consult glossary.json and authority.json BEFORE romanizing anything; REUSE settled renderings: 军统/军统局 "the Juntong"/"the Juntong Bureau"; 戴笠 Dai Li (戴先生 "Mr. Dai", 老板 "the Boss"); the place-name PINYIN convention for keyed cities (北平 Beiping, 天津 Tianjin NOT Peiping/Tientsin); the rail lines named in p#19 (北宁线 "the Beiping-Liaoning line" / 津浦线 "the Tianjin-Pukou line" / 平汉线 "the Beiping-Hankou line" / 平古线 "the Beiping-Gubeikou line" / 平绥线 "the Beiping-Suiyuan line" - historical Republican railway names, render descriptively + confirm). NEW Part-Four vocabulary to DECIDE and key as it recurs: 绥靖 "pacification", 戡乱 "the suppression of rebellion", 共匪/匪 "the Communist bandits", 特种部队 "special forces"/特种组织 "special organization", 指挥室 "command room(s)", the 平津区/平津地区 "the Beiping-Tianjin region". Render Republican years literally (checker matches the source numeral or auto-escapes via +1911; 三十八年 = 1949). WATCH the digitization glitches (list in PROGRESS.md, render to plain sense, footnote only real reading uncertainty): same classes seen throughout (single-char substitutions, dropped stops, dittography, mismatched guillemets ﹁﹂﹃﹄, stray ？, ○/× redactions - the numeric checker mis-reads ○; carry the real value in English and noise only the mis-read glyph-string; × redactions render as em-dash blanks). Dates/counts: carry real values as DIGITS/words; NOISE only idiom/approximate/name-numeral/elided/date-name forms (data/noise.txt already carries the B01-B24 rules; add B25's).
3. Checks: verify_unit.py ch32 (parity + numbers with noise auto-found + anchors); check_align.py ch32; regenerate checks.json with scripts/batch_artifacts.py (no args) and run check_structure.py --config checks.json + check_content.py --config checks.json (NOTE: check_content prints KNOWN PRE-EXISTING artifacts and exits nonzero because of them - ch08 Shunde ×3, ch13 ×9, ch09 "Jize County" ×1, ch26's TWO documented keyed-substring FALSE POSITIVES 武汉卿/劳勃生路; CONFIRM ch32 shows "all in the paired paragraph" / 0 displaced, and align any keyed name/place/TERM to its glossary-decided rendering. A NEW unit's displacements are almost always a keyed name/place/term rendered a DIFFERENT way than the glossary - align the English to the keyed form; the exception is a keyed name that is a SUBSTRING of a larger different referent, a documented false positive, not a fix). Do NOT add COMMON-NOUN or book/periodical keys. qc_entities.py on a reconstructed bilingual (data/zh body lines + out/ch32_en.json, `> zh` / en pairs, strip the ### heading lines; every glossary row needs a pinyin field - the B24 reconstruction one-liner is in PROGRESS/the ch30 method). Verify the TAIL against the source. check_register.py --ref reference/B01_frozen.md out/ch32_reading.md ("shall" is deliberate - read the note, do not de-formalize; a preface runs denser so the ratio will be higher than narrative - alignment/register are the gates, not the raw ratio).
4. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (full list in PROGRESS.md; the big already-covered furniture incl. now: No.76/特工总部 ch04/ch17, 制裁, 忠义救国军 ch21, 蓝衣社 ch08, the tiger bench ch29, the pig-cage van ch30, Dai Li's 1946 air crash ch02/ch25). Part Four OPENS the civil-war material, so expect a FEW new items (the 绥靖/戡乱 framing; the five rail lines if a reader needs them; period military/political terms the preface introduces; any classical allusion). Be generous but do NOT pad, do NOT re-note. Merge notes via apparatus_merge.py (positional arg: apparatus_merge.py data/ch32_apparatus.json; numeric character references only in note bodies; anchors verbatim ASCII substrings of the reading.md body text, NO em dash and NO quote/apostrophe character - substring traps; multi-occurrence anchors attach at the first; TIGHTEN a generic anchor if it would match an earlier paragraph). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field; apparatus_merge's glossary path assumes a FLAT map and would corrupt the sectioned file - use it ONLY for notes; scripts/add_ch30_glossary.py is the latest by-hand pattern, asserting each hanzi key against data/zh). Confirm ch32 carries no images (no <img> - confirmed). For any CJK in a note body use the make_b24_apparatus.py pattern (author bodies with typed hanzi, ASSERT every non-ASCII glyph is present in data/zh/ch32.txt, then convert to NCRs) to defeat the CJK-mangling hazard - and remember a CORRECT glyph may be ABSENT if the source prints a glitch/variant form, so describe such terms with the source's own form + pinyin.
5. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; update HANDOFF.md; commit and push to claude/nameless-heroes. (B25 OPENS PART FOUR; next is B26 = ch33 = 第一章 振衰起敝 二次出发, the FIRST Part-Four chapter, which carries a book.json `sections` array [ch33s01-ch33s04] - the 1946-49 civil-war narrative begins. ch33-ch42 all carry `sections` arrays; confirm scope in book.json. Working batch labels run ONE AHEAD of book.json's batches array: book.json B25 = ch33 = working B26.)

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B26 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
```

## What is DONE (do not redo)

- **Step 0 (survey).** Ingest + book.json (43 chapters, 5 TOC parts) + skeleton EPUB.
- **Batch B01 (ch01-ch05), the front matter.** 67 notes. **VOICE GATE PASSED:** the B01
  front matter is the FROZEN register reference (`reference/B01_frozen.md`) from B02 on.
- **B02-B05 (ch06-ch09). Part One COMPLETE.**
- **B06-B13 (ch10-ch19). Part Two ("Disgrace at Hanoi") COMPLETE.**
- **Batch B14 (ch20), PART THREE OPENS.** ch20 = the Part-Three self-preface.
- **B15-B24 (ch21-ch31). Part Three ("Renown Won in a Hundred Battles" / 百战声威) COMPLETE.**
  ch21 = arrival + order of battle; ch22 = first 1940 sanctions + Fan Xing; ch23 = the "three-sided
  enemy" bridge; ch24 = anatomy of the three-sided enemy + Yu Yefeng sanction + Dai's self-review;
  ch25 = full work-review + arms-gift + Fan Xing puzzle; ch26 = the nameless martyrs; ch27 = the
  张啸林 tycoon-death case; ch28 = the height of renown and blood (Chen's capture recapped); ch29 =
  第十章(上), the disaster chapter, Liu Yuanshen's memoir of the Zhou Xiyuan/Zhu Min trap (breaking off
  on 28 June 1941); **ch30 = 第十章(下), the trap sprung and the two captures; ch31 = the Part-Three
  closing errata note.** Detail per batch in PROGRESS.md.
- **Batch B24 (ch30 + ch31), COMPLETES PART THREE.** ch30 (祸不单行 柱折梁摧 下): drop=2; 1 <h2> +
  110 <p>, NO <br/>/<img>/note-markers, byte-exact p-by-p; 1 severed-<p> merge (91/92); 1 STANDALONE
  三、heading (L3) + 2 TAIL-GLUED headings (四、on L22 after 」, 五、on L76 after ！); inline 第一、/第二、
  enumerations + the 三、四尺 number-range kept as body lines. 108 body paragraphs; ratio 4.64. A
  two-voice chapter: sections 三 = Liu Yuanshen's memoir, sections 四/五 = Chen's own arrest (per ch31
  erratum #8; voice-switch footnoted). ch31 (写在「英雄无名」第三部专书出版前): drop=2; 1 <h1> + 14 <p>;
  the enumerated 一、-八、 items are an ERRATA LIST kept as body lines (NOT headings); 14 body paragraphs;
  ratio 5.48. 8 notes (284 cumulative); 3 net new glossary rows (褚亚鹏/林焕芝/姜绍谟). check_content
  0 displaced (1 fixed: sign "HONGKOU" → keyed "Hongkou"); qc 0 misses; register within tolerance
  (shall 9%/0%). qa_epub PASS; epubcheck 0/0/0/0. **EPUB now 31/43 chapters.** Detail in PROGRESS.md
  ("Batch B24").

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` - derives data/zh/<id>.txt verbatim from data/src, applying per-unit
  drops/merges/heading-splits with a source-conservation check. Specs for ch01-ch31. Merge logic
  FOLLOWS CHAINS. **drop is variable:** most chapters drop=2; ch01/ch10/ch20/ch32 drop=3 (a part
  super-title precedes the preface). `standalone` = a sub-heading kept as its own <p> with no heading
  markup, emitted as `### `; `glued` = a sub-heading fused onto a paragraph's TAIL (endswith), split
  off; `glued_head` = a heading fused onto a paragraph's HEAD (startswith), split off; `merges` =
  source <p> pairs that sever one sentence OR an intra-<p> `<br/>` line break. **B20 lesson: not every
  `<br/>` is a merge** - a `<p>` that is a TABLE/roster is KEPT as rows. **B22/B24 lesson: a chapter
  can carry INNER enumerated 一、二、三 / 第一、第二 DOCUMENT-CLAUSE lists (quoted-agreement clauses,
  errata items, in-paragraph enumerations) that are NOT section headings - keep them as ordinary body
  lines per parity, judged by function.**
- `scripts/batch_artifacts.py` - derives out/<id>_en.json FROM out/<id>_reading.md and writes
  checks.json. Author the reading.md; run this. **TRAP: running it with an ID writes checks.json
  with ONLY that unit; ALWAYS finish with a no-arg run.**
- `scripts/verify_unit.py <id>` - parity + numbers (auto-finds data/noise.txt; do NOT pass
  --noise) + anchors. Run per unit.
- **qc_entities bilingual reconstruction (B24 one-liner):** for each unit, read data/zh/<id>.txt,
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
  name/place/TERM rendered a DIFFERENT way than the glossary: align the English to the keyed form
  (B24: the sign "HONGKOU" was flagged until re-cased to the keyed "Hongkou"). Do NOT add book-TITLE or
  COMMON-NOUN keys.
- **Verse marker `{p}`** (ch13, reused ch26 for the 挽联): prefix a pure-verse line with `{p} `;
  the builder renders `<p class="verse">`; the checks strip it.
- Glossary is authored/merged BY HAND into the SECTIONED file (book/people/organizations/places/
  terms), idempotent + re-read-verified. **Every row MUST carry a `pinyin` field** - qc_entities
  does `rec["pinyin"]` and KeyErrors otherwise. `scripts/add_ch30_glossary.py` is the latest by-hand
  pattern: asserts each hanzi key is a substring of data/zh/<id>.txt. A `/`-joined key holds
  alternate hanzi for one referent; qc splits on `/`. apparatus_merge's glossary path assumes a
  FLAT map and would corrupt the sectioned file; NOTES still go through apparatus_merge.py (positional
  arg, e.g. `apparatus_merge.py data/ch32_apparatus.json`).
- **qc_entities catches term-rendering drift too:** a glossary common-noun term rendered a
  different way flags as a "miss." Align the English to the glossary.
- **GLOSSARY-KEY DISCIPLINE:** a key must be a DISTINCTIVE proper noun (or a distinctive institution)
  that renders ONE way everywhere. Periodicals and books are FOOTNOTES/inline, not keys. One-off
  transliterated Western/Japanese officer names (e.g. Malone, ch30), one-off telegram/roster names,
  and attested Shanghai ROADS are inline, not keyed. A bare surname whose full name is unknown is
  rendered inline.
- **Note-anchor gotchas:** anchors must be ASCII, WITHOUT any quote/apostrophe character AND
  without an em dash (U+2014) - all substring traps. The reading.md uses curly quotes and em
  dashes freely, so pick an anchor phrase with none of them. **Multi-occurrence anchors attach at
  the FIRST occurrence** (B24 "pig-cage van" occurs twice, attaches at the first, intended) - and if
  a short generic anchor would match an EARLIER paragraph than the one you mean, LENGTHEN it.
- **make_b24_apparatus.py pattern (scripts/):** author note bodies as plain ASCII + typed hanzi
  + straight/curly punctuation, ASSERT every non-ASCII hanzi glyph occurs in THAT UNIT's data/zh/<id>.txt,
  then convert every non-ASCII char to a numeric char ref and run apparatus_merge.py. **A CORRECT glyph
  may be ABSENT if the source prints a glitch/variant** (cf. ch25's 洋泾浜, ch28's 洋泾滨) - describe
  such terms with the source's own form + pinyin/English. A note that quotes ANOTHER unit's text (B24's
  voice-switch note referenced ch31 from a ch30 note) is authored ENGLISH-ONLY to avoid the
  cross-unit glyph-assert. Curly quotes / em / en dash are in the `allow` set; AVOID tone-marked pinyin
  in note bodies.
- data/noise.txt carries the B01-B24 project noise rules (each with a comment line). Republican
  years render literally; the checker matches the source numeral (or auto-escapes Republican-year
  N via N+1911). The elided-tens block is ordered LONGEST-FIRST. Name-numeral glyphs are noised.
  Idiom numerals are noised (B24 added 退一万步). **The ○ (U+25CB) address artifact:** the checker
  cannot read ○ as zero - noise the mis-read glyph-string, carry the real value in the English. **×
  (source redaction)** renders as an em-dash blank. Every REAL value is CARRIED and matched as DIGITS.
  **B24 numeric-checker lessons:** the word-map needs "a thousand"/"a hundred" (bare "thousand"/"hundred"
  after a noun do NOT count as 1000/100 - write "a thousand strong" for 千人之众); 十来个 carries as
  "ten or so" (the checker reads 十=10); a counter carried by naming (两个人 after both men are named)
  gets "the two of them" or is noised; 二爷 "Second Master" is ALREADY noised (title element).
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches it; re-run per session).
  setup.sh's ONE failing regression test ("hook stands down on template stub") is a KNOWN false
  alarm; all other regression tests pass.

## Renderings settled / carry-forward

- 军统 / 军统局 -> "the Juntong" / "the Juntong Bureau" (DECIDED). 戴笠 Dai Li (courtesy Yunong;
  老板 "the Boss"; 戴先生 "Mr. Dai"; 戴雨农 "Dai Yunong"); 汪精卫 Wang Jingwei (汪逆 "the traitor
  Wang"). 制裁 "sanction"; 制裁令 "sanction order." 敌伪 "the enemy and the puppets"; 汪伪 "Wang
  puppets"; 沦陷区/沦陷地区 "the fallen zone(s)"; 战区 "war zone"; 后方 "the rear"; 区长 "District
  Chief"/"District chief"; 区本部/区部 "District Headquarters"; 区书记 "District secretary"; 督察
  "inspector" / "inspectorate"; 总督察 "Chief Inspector." Chiang's titles: 校长 "the Commandant",
  委员长/委座 "the Generalissimo", 总裁 "the Director-General"; 领袖 "the Leader"; 总理 "the Party
  Leader" (Sun Yat-sen). 日本宪兵队 "the Japanese gendarmerie"; 七十六号 "No. 76"; 特工总部 "Special
  Operations Headquarters"; 工部局 "Municipal Council"; 公董局 "French Municipal Council"; 公共租界
  "International Settlement"; 法租界 "French Concession"; 巡捕房 the Concession police / "station
  house"; 三民主义 "the Three Principles of the People." 特区法院 "Special District Court"; 中央储备银行
  "Central Reserve Bank"; 会审公廨 "the Mixed Court"; 联合准备银行 "the Federal Reserve Bank" (North China
  puppet bank); 维新政府 "the Reformed Government"; 大道市政府 "the Great Way City Government".
  **B24: 大队长 "brigade commander"; 分队 "sub-brigade" (第三分队 = Third Sub-brigade); 三道头
  "three-stripe head" (Concession police sergeant, explained in ch24); 猪笼车 "pig-cage van"; 高洋房
  "High Foreign House" (a building at No. 76); 内交通/内交站 "internal courier"/"internal courier station";
  預备区/第二区 "Reserve District"/"Second District".**
- **PLACE-NAME CONVENTION (the qc gate enforces the glossary's PINYIN for keyed cities):**
  北平 Beiping, 天津 Tianjin, 汉口 Hankou, 四川 Sichuan, 虹口 Hongkou, 重庆 Chongqing, 闸北 Zhabei,
  沪西 "western Shanghai" (NOT Peiping/Tientsin/Hankow/Szechuen/Hongkew/Chungking). 重庆大公报 =
  "Chongqing Ta Kung Pao". KEYED roads: 愚园路 "Yuyuan Road", 冀东 "East Hebei". Non-keyed attested
  Shanghai ROADS keep their historical forms: Avenue Joffre (霞飞路), Joffre Terrace (霞飞坊), Seymour
  Road (西摩路), Sinza Road (新闸路), Rue Bourgeat (蒲石路), Bubbling Well Road (静安寺路), Jessfield Road
  (极司非尔路), the Lyceum Theatre (兰心大戏院), Avenue Edward VII (爱多亚路), Nanking Road (南京路),
  Mohawk Road (马霍路), the Bund/外滩, Robison Road (劳勃生路 - NOT "Lao Bosheng Road"; the officer
  劳勃生 is keyed "Lao Bosheng", a documented substring false positive), and the many roads listed in
  prior batches. Concession-street rule: keep attested names, PINYIN for the uncertain.
- **Book / part titles (in-text; DECIDED; reuse verbatim):** 英雄无名 = "Nameless Heroes"; Part One
  北国锄奸 = "Rooting Out Traitors in the North"; Part Two = "Disgrace at Hanoi"; Part Three 百战声威
  = "Renown Won in a Hundred Battles"; **Part Four 平津地区绥靖戡乱 = "Pacification of the Beiping-Tianjin
  Region" (book.json `part`; the in-text super-title.**) 蓝衣社 = "the Blue Shirt Society" (NOTED ch08).
  忠义救国军 = "the Loyal and Patriotic Army" (NOTED ch21). 抗日杀奸团 = "the Anti-Japanese Traitor-Killing
  Corps" / 抗团 = "the Kang Corps" (NOTED ch02/ch11; 抗团 keyed B20). Books by FOOTNOTE/inline (not
  glossary): 蒋总统秘录, 戴雨农先生传/全集, 沪滨三次历险实录 (Liu Yuanshen's memoir, quoted through Part
  Three, incl. ch30 sections 三/四/五), 沪上往事 (Wan Molin), 在敌人心脏里 (Zhang Zhiyi, ch26), 大陆宪兵实录
  (ch26), 上海租界问题 (ch27/ch28), 官场现形记 "Officialdom Unmasked" (NOTED ch28), 梨园掌故 "Anecdotes of
  the Pear Garden" (ch31); periodicals: 申报 Shenbao (NOTED ch24), 大公报 Ta Kung Pao, 中华日报/新申报 Xin
  Shen Bao, 中美日报, 传记文学, 南华晚报 South China Evening News (NOTED ch29).
- **B23 shelf (ch29; reuse; all keyed with pinyin):** 周西垣 Zhou Xiyuan, 冯贤 Feng Xian (Zhou's cover
  name - renders its OWN way, NOT "Zhou Xiyuan"), 朱敏 Zhu Min, 刘全德 Liu Quande, 相强伟 Xiang Qiangwei,
  骆成金 Luo Chengjin, 许力求 Xu Liqiu.
- **B24 shelf (ch30/ch31; reuse; all keyed with pinyin):** 褚亚鹏 Chu Yapeng (ex-Beiping courier, the
  Bubbling Well Road electrical-shop station; paraded to ID Chen but did not), 林焕芝 Lin Huanzhi
  (Cantonese action-section chief at No. 76, ex-Fourth Team; brother 林镇城 Lin Zhencheng inline),
  姜绍谟 Jiang Shaomo (courtesy 次烈 Cilie; Shanghai Reserve/Second District chief, carried on after
  Chen's capture). NEW ch30/ch31 notes: the pig-cage van (猪笼车); Malone (马隆/马龙, the French
  contact, two spellings one man); the Double Ninth (重阳, 28 Oct 1941); the section-4 voice switch;
  Biluochun tea (碧螺春); the page-citation apparatus (ch31 errata pages are the author's, to the
  original edition); the opera bill (红拂传/小商河/Yang Zaixing/Yue Fei); reform through labour (劳动改造,
  laogai). Rendered INLINE (not keyed): 仇淑英 Qiu Shuying, 陈贤荣/程远 Chen Xianrong/Cheng Yuan, 孙国昌
  Sun Guochang, 秦尔同/张湘南/顾汉卿 (radio chiefs), 桂涤非 Gui Difei, 马隆/马龙 Malone, 克莱德 Clyde,
  胡永安 Hu Yong'an, 阿平 A-ping; 刘仲康 Liu Zhongkang, 李洪春 Li Hongchun, 梁慧超 Liang Huichao, 杨再兴
  Yang Zaixing, 岳飞 Yue Fei, 随波 Suibo, 徐展 Xu Zhan. (钱新民 Qian Xinmin, 蒋安华 Jiang Anhua already
  keyed.) The variant 余廷智 (ch31, for keyed 余延智 Yu Yanzhi) renders "Yu Yanzhi".
- **Earlier shelves (B15-B22)** remain in PROGRESS.md and prior HANDOFFs; the whole B02-B22 cast is
  keyed. Consult glossary.json before romanizing anything.

## Voice sheet - CHEN GONGSHU (author / narrator)

- REGISTER: educated, formal, essayistic first person; grave and a touch archaic but not stilted.
  Long semicolon-joined clauses; four-character idiom and classical allusion used freely and
  footnoted when they carry weight. Refers to himself as 笔者 "the writer" and 我 "I." His narrating
  "shall" is DELIBERATE - do not de-formalize it; check_register flags it informationally (B06 33%,
  B08 29%, B12 43%, B15 33%, B16 36%, B18 25%, B19 67%, B20 83%, B21 0%, B22 22%, B23 56%, B24 ch30 9%
  - elevated when the chapter reproduces many quoted directives/documents, low in dialogue-heavy
  narrative; NOT a de-formalization either way).
- STANCE: self-justifying yet self-effacing; insists on truthfulness, admits his blunders; tender
  toward dead comrades, bitter and scornful toward the enemy and the Communists. When quoting
  hostile/puppet/comrades' documents (memoirs, telegrams, news reports), keep the quoted register
  DISTINCT from Chen's own dry scorn. **Part Four (from ch32) turns to the 1946-49 civil war: the
  Nationalist idiom sharpens (共匪 "the Communist bandits", 绥靖戡乱 "pacification and the suppression
  of rebellion") - PRESERVE it, footnote where contested, text stands.**
- Ratio ~4.55-4.78 en/han in narrative (B24 ch30 4.64); prefaces denser (~5.2-5.3; ch20 self-preface,
  and expect ch32 in this band); document-heavy chapters run higher (ch24 5.33, ch28 5.09, ch31 5.48).
  Read the note, do not reset.

## Voice sheets - principal & recurring cast

- **DAI LI (戴雨农 / Mr. Dai / 老板 "the Boss").** After ch17 only letters and telegrams; his word
  is "as a mountain." Died in a 1946 air crash (NOTED ch02/ch25). In Part Four the Juntong reorganizes.
- **QI QINGBIN (齐庆斌 / "Old Qi").** Chen's childhood friend; the Shanghai District secretary. In
  ch30 he is arrested the same night as Chen (the two captures); unhurried composure to the end
  ("Don't be anxious... we will spare no effort to save you").
- **LIU YUANSHEN (刘原深).** The man who revises "Nameless Heroes" for Chen; his living memory-check
  through Part Three. His first-person memoir (沪滨三次历险实录) is quoted at length in ch29 (sections
  一/二) and ch30 (section 三): a plainer, more novelistic voice than Chen's, full of dialogue - keep
  it distinct. In ch30 he walks into the Zhou Xiyuan/Zhu Min trap, is seized on Avenue Joffre, handed
  through the Lujiawan station house to No. 76; held fast (威武不屈).
- **CHEN GONGSHU himself.** ch30 sections 四/五 = his OWN arrest (the source marks no switch from Liu's
  voice; footnoted): seized at Qi Qingbin's new flat at dawn on 30 Oct 1941 (ROC 30), his pregnant
  wife taken too, through the French Concession central station to No. 76, his cover as the "internal
  courier Zhang Baozhao" blown by Qian Xinmin. He resolves NOT to seek a quick death, to "win his
  stakes back." **Part Four is the sequel he promises: "in the next book... without the least
  disguise."**
- **JIANG SHAOMO (姜绍谟 / Cilie).** Chief of the Shanghai Reserve District (Second District), never
  exposed; took over the Shanghai work after Chen's capture and carried it to the victory of the war
  of resistance (ch30 close).

## ⚠ Name trap RESOLVED (do not reopen): 陈邦国 / 郑邦国

The Hanoi action-team member the source spells 郑邦国 in ch13 and 陈邦国 in ch15/ch16/ch17 is ONE
man. RESOLVED to **Chen Bangguo (陈邦国)**. Use Chen Bangguo consistently.

## Where the book stands

- Part One (北国锄奸) COMPLETE (B01-B05). Part Two ("Disgrace at Hanoi") COMPLETE (B06-B13). Part
  Three ("Renown Won in a Hundred Battles" / 百战声威) COMPLETE (B14-B24).
- **NEXT: B25 = ch32** (OPENS PART FOUR "Pacification of the Beiping-Tianjin Region"). ch32 = 自序,
  the Part-Four self-preface (parallel to ch10/ch20). 1 <h1> (平津地区绥靖戡乱, the part super-title)
  + 1 <h3> (自序) + 35 <p>, NO <br/>/<img>/note-markers, **drop=3**; no section headings inside. The
  civil-war material begins: Chen commands a special unit in the 1946-49 Nationalist-Communist fighting
  around Beiping and Tianjin; the Nationalist idiom (共匪/绥靖戡乱) sharpens. book.json's B24 array entry
  = ch32 alone.
- After B25: B26 = ch33 = 第一章 振衰起敝 二次出发 (the first Part-Four chapter; carries a book.json
  `sections` array ch33s01-ch33s04). Part Four = ch32-ch43 (ch33-ch42 carry `sections` arrays - the
  1946-49 civil-war narrative). Working batch labels run ONE AHEAD of book.json's batches array from
  ch24 on (ch30+ch31 = B24, ch32 = B25, ch33 = B26).
- The frozen register reference is `reference/B01_frozen.md`. Narrative sits at 4.55-4.78 en/han;
  prefaces denser (~5.2-5.3); document-heavy chapters higher - alignment/register are the gates, not
  the raw ratio.
- Sub-heading pattern DIFFERS by chapter. Styles seen: Part One numbered 一/二/三; ch11/ch14/
  ch20-title/ch21-ch26 COUPLET-STYLE with NO number prefix; ch12/ch13/ch15/ch16/ch17/ch18-sections
  numbered-in-parens (一)/(二)…; ch27/ch28/ch29/ch30 use 一、二、三 enumerated headings (with INNER
  document-clause/errata 一、二、三 / 第一、第二 lists that are NOT headings - judge by function). GLUED
  sub-heads seen ch08/ch16/ch18/ch22/ch24/ch25/ch26/ch27/ch29/ch30 (tail; ch24 also HEAD). Part Four
  chapters ch33-ch42 carry book.json `sections` arrays (headings supplied in book.json). Grep each new
  chapter p-by-p, and DISTINGUISH enumerated LIST items / document clauses (per parity) from SECTION
  headings and run-in labels.
- WATCH for source anomalies: cuts, misplaced-「 glitches, corrupt/dropped-character phrases, dropped
  full stops, magazine-seam codas, a STRAY glyph fused onto a title, a STRAY orphan enumerator, stray
  ？, the ○ (U+25CB) and × redactions, name glitches, variant forms, and pervasive single-character
  substitutions. Intra-<p> `<br/>` line breaks: PROSE splits MERGE, TABLE/roster rows are KEPT.
  Severed-<p> boundaries (a source <p> ending non-terminal) MERGE (ch25/ch26 had 7 each, ch27 2, ch28
  4, ch29 1, ch30 1). Re-grep each batch's source for `\[\d+\]` note markers (none through B24).

## Open items for the read-through / completion

- Feed decided renderings back to authority.json on completion: 军统 "the Juntong"; the full
  B02-B24 historical-name set.
- Japanese name readings to firm up when the men recur (多田骏, 田代皖一郎, 土肥原贤二, 板垣征四郎,
  近卫文麿, 影佐祯昭, 今井武夫, 晴气庆胤; 大屋久寿雄; 横山秋马; 岩井英一; the B18/B20 gendarmerie officers;
  the B22 one-off officers - romaji to firm up).
- Provisional romanizations to firm up (glossary `provisional` rows, incl. the Shanghai-District
  cast, the B16-B24 operatives).
- Whole-book reconciliation items: ch09 "Jize County" (the 鸡泽县 key); the pinyin-vs-postal city
  names (standardized to pinyin from B18); the two B20 keyed-substring false positives (武汉卿 /
  劳勃生路) - both correct as rendered. The Malone spelling (马隆 ch30 §3 / 马龙 ch30 §5, one officer,
  rendered "Malone", footnoted) and the uncertain concession-road pinyin - candidates for a human
  read. Stray source glyph still to resolve: 毛酋 in a ch36 section title.

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01-B24 builds (0/0/0/0). Source is a clean digital
  EPUB, predominantly simplified with residual variant glyphs and pervasive digitization glitches
  (list them, render to plain sense, do not footnote mechanical typos). B01-B24 glitch lists in
  PROGRESS.md.
- Running-header line 英雄无名-陈恭澍 opens all 43 content files: drop it. drop count is variable -
  most drop=2; ch01/ch10/ch20/ch32 drop=3.
- Enumerated ；/：/、 bullet lists, quoted-document/directive/roster lines (INCLUDING intra-<p>
  `<br/>` TABLE rows and INNER document-clause / errata / 第一、第二 lists), salutations, verse lines,
  juxtaposition lines, run-in section labels, and 『』/「」-closed dialogue are DELIBERATE separate
  `<p>`/lines - do NOT merge them; only genuine mid-phrase splits (last char not terminal, OR a source
  `<p>` boundary that severs one sentence, OR an intra-<p> `<br/>` inside PROSE) merge, and those can
  CHAIN. The ：-ended lead-in (memoir/document/dialogue) stays SEPARATE.
- Faithful numbering gaps/anomalies (NOT errors): Part Three skips 第七章 (ch27 = 第八章); 第十章 splits
  into (上)/(下) (ch29/ch30); 三面受敌 一往无前 titles two chapters (ch14 and ch24); ch09 printed §五
  before §四; ch13 restarts its (一)-(五) numbering; ch21/ch22/ch24 carry magazine "下期续载" seams;
  ch28 reproduces two whole court agreements as inner document-clause lists; ch31 is an ERRATA note (a
  一、-八、 list, kept as body lines). Preserve and, where a reader would stumble, footnote.
- Expect a stray per-task branch at the top of every batch; consolidate onto claude/nameless-heroes
  per rule 2.
