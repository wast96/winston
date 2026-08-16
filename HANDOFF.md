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
Nameless Heroes B28

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once (its ONE failing regression test, "hook stands down on template stub", is a KNOWN false alarm; all others pass), then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05) through B27 (ch34) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them. PARTS ONE, TWO ("Disgrace at Hanoi") and THREE ("Renown Won in a Hundred Battles" / 百战声威) are COMPLETE; PART FOUR ("Pacification of the Beiping-Tianjin Region" / 平津地区绥靖戡乱) is OPEN - ch32 was its self-preface, ch33 the first narrative chapter, ch34 the doctrinal chapter. The EPUB now holds 34/43 chapters, 303 notes. NOTE on batch numbering: book.json's batches array lumps ch23+ch24 as "B17", so the working batch labels run ONE AHEAD of the book.json array from ch24 on (ch34 = working B27 = book.json's B26 entry; ch35 = working B28 = book.json's B27 entry).

Do Batch B28 = ch35 = 第三章 一番风雨 几片落叶 "Chapter 3. A Spell of Storm, a Few Fallen Leaves" (ONE unit; the THIRD Part-Four narrative chapter). This is a NARRATIVE chapter (expect a narrative ratio ~4.55-4.78, NOT the doctrinal 5.19 of ch34 - but alignment/register are the gates, not the raw ratio): Chen reports for duty and fixes the chain of command, gathers old comrades to build up the First Brigade's strength, teases a lead out of personal connections, and closes on a cautionary ending. ch35 carries a book.json `sections` array [ch35s01 一、投文报到确定配属关系 "1. Reporting for Duty, Fixing the Chain of Command"; ch35s02 二、广纳故旧情义重实力增强 "2. Gathering Old Comrades: Loyalty Deepens, Strength Grows"; ch35s03 三、从个人关系中理出来一条线索 "3. A Lead Teased from Personal Connections"; ch35s04 四、往事已成云烟结局足堪警惕 "4. The Past Now Vapor, the Ending a Warning"] - confirm all four title_en in book.json. Chen's Nationalist idiom stays at its sharpest (共匪/匪 "the Communist bandits", 绥靖戡乱 "pacification and the suppression of rebellion", 匪谍/共酋/共干) - PRESERVE it, do NOT soften; footnote where scholarship contests, text stands. Read the tail of ch34 (out/ch34_reading.md) for the batch seam and the settled Part-Four register/vocab. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch35 (36_index-split-000-0034.txt) from data/src. CONFIRM structure p-by-p against data/src_epub/OEBPS/Text/index_split_000_0034.xhtml [ch35: 1 <h2> (第三章 一番风雨 几片落叶) + 4 <h3> (the four section headings 一、/二、/三、/四、) + 196 <p>, NO <h1>/<br/>/<img>/[\d+] - CONFIRMED at B27]. **drop=2** (running header 英雄无名-陈恭澍 + <h2> chapter title). The FOUR section headings are SEPARATE <h3> ELEMENTS (their own whole lines in the txt) -> emit each as a `standalone ### ` in clean_batch.py (the ch33/ch34 method, NOT tail-glued). After drop=2 the txt has 200 body lines = 4 section-heading lines + 196 <p> lines. Do the byte-exact p-by-p diff FIRST (the B19-B27 method: extract <p> inner text AND the <h3> texts in document order, walk each consuming 1 body line, assert every line matches) to PIN the 4 heading line-numbers and to LOCATE any SEVERED-<p> boundaries (last char non-terminal -> MERGE; scan ！？》-ending lines too for glitch-MASKED severs, cf. ch33's stray ！ for 」). CRITICAL: keep INNER 一、二、三 / 第一、第二 enumerations, number-ranges and name-lists as BODY lines per parity (the ch27-34 lesson: judge by function, not by the leading numeral). Extend scripts/clean_batch.py with ch35's spec (drop=2; the 4 confirmed standalone <h3> heading line-numbers, 1-based; any confirmed severed-<p> merges; NO glued/glued_head unless the diff reveals one). Run it (source-conservation check must pass). Write out/ch35_reading.md (## from book.json title_en; the 4 sections as ### sub-headings from book.json section title_en; one English paragraph per source body line). Then run scripts/batch_artifacts.py ch35, and ALWAYS finish with a NO-ARG run (the trap: an ID-run writes checks.json with ONLY that unit; the no-arg run restores all 35 units so check_structure/check_content see them).
2. Translate to the FROZEN register (Chen's voice sheet in HANDOFF; NARRATIVE ~4.55-4.78 en/han; the narrating "shall" is DELIBERATE, do NOT de-formalize). Consult glossary.json and authority.json BEFORE romanizing anything; REUSE the B25/B26/B27-settled Part-Four renderings (PROGRESS.md "Settled Part-Four renderings" + the B26/B27 rows). KEYED terms to reuse consistently in the BODY (qc enforces): 特种部队 "special-operations unit", 特种组织 "special organization"; 军统/军统局 "the Juntong"/"the Juntong Bureau"; 保密局 "the Baomiju"; 中统 "the Zhongtong"; 复兴社 "the Renaissance Society"; 绥靖总队 "the Pacification Corps"; 总队 "Corps"/总队长 "Corps Commander"; 大队 "brigade"/大队长 "brigade commander"; 中队 "company"; 分队 "sub-brigade"; 直属组 "directly subordinate section"; 部队长 "unit commander"; 编制 "establishment"; 配属关系 "relation of attachment" (ch35s01's title is 确定配属关系 - the chapter's own subject); 联合会报 "joint briefing"/会报 "briefing"; 指挥室 "command room"; 指挥员 "commanding officer" vs 指挥官 "commander"; 交警总队 "Transport Police Corps" (KEYED B27); 华北剿匪总司令部 "North China Bandit-Suppression Headquarters" (KEYED B27); 绥靖 "pacification"/戡乱 "suppression of rebellion"/剿匪 "bandit-suppression"/匪谍 "Communist spies"/共酋 "Communist chieftains"/共干 "Communist cadres". KEYED people to reuse: 李玉林 Li Yulin, 罗敬 Luo Jing, 刘原深 Liu Yuanshen, 刘培初 Liu Peichu, 聂恩俊 Nie Enjun (KEYED B27), 侯腾 Hou Teng, 吴安之 Wu Anzhi, 马汉三 Ma Hansan, 张家铨 Zhang Jiaquan, 史泓 Shi Hong, 陈诚 Chen Cheng, 郑介民 Zheng Jiemin, 毛人凤 Mao Renfeng, 戴笠 Dai Li; INLINE (per the ch33/ch34 decision, do NOT key): 王兆芬 Wang Zhaofen, 张作兴 Zhang Zuoxing. Render Republican years literally (the checker matches the source numeral or auto-escapes via +1911; NARRATIVE and ordinal forms both compose - but SPELLED-OUT COMPOUNDS DO NOT: write 3,500 / 2,500 / 1,500 as DIGITS, since "three thousand five hundred" composes to {3000,500} not {3500} - the B26/B27 trap). WATCH the digitization glitches (list in PROGRESS.md, render to plain sense, footnote only real reading uncertainty): same classes throughout (single-char substitutions, dropped 。 stops, dittography, mismatched guillemets ﹁﹂﹃﹄, stray ？/》/！ often standing for a closing 」, stray ︸/︴/|/≤ glyphs, ○/〇/× redactions - the numeric checker mis-reads ○/〇; carry the real value in English and noise only the mis-read glyph-string; × redactions render as em-dash blanks). Dates/counts: carry real values as DIGITS/words; NOISE only idiom/approximate/name-numeral/elided/date-name/counter-by-naming/place-name-numeral forms (data/noise.txt already carries the B01-B27 rules incl. the ch34 place-names 东四/四象桥 and the ordering trick for 三数百; add B28's).
3. Checks: verify_unit.py ch35 (parity + numbers with noise auto-found + anchors); check_align.py ch35; regenerate checks.json with scripts/batch_artifacts.py (no args) and run check_structure.py --config checks.json + check_content.py --config checks.json (NOTE: check_content prints KNOWN PRE-EXISTING artifacts and exits nonzero because of them - ch08 Shunde ×3, ch13 ×9, ch09 "Jize County" ×1, ch26's TWO documented keyed-substring FALSE POSITIVES 武汉卿/劳勃生路; CONFIRM ch35 shows "all in the paired paragraph" / 0 displaced, and align any keyed name/place/TERM to its glossary-decided rendering. A NEW unit's displacements are almost always a keyed name/place/term rendered a DIFFERENT way than the glossary - align the English to the keyed form). Do NOT add COMMON-NOUN or book/periodical keys. qc_entities.py on a reconstructed bilingual (data/zh body lines minus the `### ` heading lines + out/ch35_en.json, `> zh` / en pairs; every glossary row needs a pinyin field - the reconstruction one-liner is in PROGRESS/the ch30-ch34 method; WATCH the keyed term rendered as a VERB not the noun, cf. 绥靖 "pacify" vs "pacification"). Verify the TAIL against the source. check_register.py --ref reference/B01_frozen.md out/ch35_reading.md ("shall" deliberate; expect a NARRATIVE ratio, lower than ch34's doctrinal 5.19).
4. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (full list in PROGRESS.md; the big already-covered furniture incl. the Nationalist 绥靖/戡乱/共匪 framing, the Marshall Mission/Committee of Three/Executive HQ, the Lizhi Plan, the Jiangxi bandit-suppression/别働总队, the Youth Army, Fu Zuoyi/Beiping's surrender, the Baomiju [ch04], Whampoa, the Marco Polo Bridge, fabi, the Republican-year system, and from B26/B27: 特种部队/特种组织, Yan'an, the Zhongshan tunic [ch06], the Renaissance Society/Blue Shirts [ch08], Duan Qirui [ch07], the Legation Quarter/Hotel of Six Nations [ch06], the Transport Police Corps, the India-Burma Expeditionary Force, Tan/Han Family Cooking). Be generous but do NOT pad, do NOT re-note. Merge notes via apparatus_merge.py (positional arg: apparatus_merge.py data/ch35_apparatus.json; numeric character references only in note bodies; anchors verbatim ASCII substrings of the reading.md body text, NO em dash and NO quote/apostrophe character - substring traps; multi-occurrence anchors attach at the first; TIGHTEN a generic anchor). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field; apparatus_merge's glossary path assumes a FLAT map and would corrupt the sectioned file - use it ONLY for notes; scripts/add_ch34_glossary.py is the latest by-hand pattern, asserting each hanzi key against data/zh). For any CJK in a note body use the make_ch34_apparatus.py pattern (author bodies with typed hanzi + untoned pinyin, ASSERT every non-ASCII glyph is present in data/zh/ch35.txt, then convert to NCRs) - and remember a CORRECT glyph may be ABSENT if the source prints a glitch/variant form, so describe such terms with the source's own form + pinyin. Confirm ch35's image count (grep <img>; ch32-ch34 carried none).
5. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; update HANDOFF.md; commit and push to claude/nameless-heroes. (Next is B29 = ch36; ch33-ch42 all carry `sections` arrays; confirm scope in book.json. Working batch labels run ONE AHEAD of book.json's batches array: book.json B28 = ch36 = working B29. Part Four = ch32-ch43; after ch42 only ch43 = the Afterword remains. NOTE the open trap: a stray source glyph 毛酋 in a ch36 section title, which book.json renders "the Bandit Chief".)

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B29 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
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
- **Batch B25 (ch32), OPENS PART FOUR.** ch32 (自序) = the Part-Four self-preface. 35 body paragraphs;
  ratio 5.57 (preface, denser). 10 notes; 10 net-new keyed glossary rows.
- **Batch B26 (ch33), FIRST Part-Four NARRATIVE chapter.** 第一章 振衰起敝 二次出发. drop=2; 1 <h2> +
  4 <h3> (section heads) + 153 <p>, byte-exact p-by-p, TWO severed-<p> merges (L17/18 张炎元、|侯腾 inside
  the 浮生掠影集 quote; L19/20 masked by a stray ！ for 」). 151 body paragraphs; median ratio 5.32
  (document-heavy: Luo Jing's ~17-para autobiography, Liu Peichu/Li Yulin quotes). 6 notes (300 cumulative);
  12 net-new keyed glossary rows (8 people, 2 orgs, 2 terms). check_content 0 displaced; qc 0 misses;
  register within tolerance. qa_epub PASS; epubcheck 0/0/0/0. **EPUB now 33/43 chapters.** Detail in
  PROGRESS.md ("Batch B26").
- **Batch B27 (ch34), the DOCTRINAL Part-Four chapter.** 第二章 自动自发 同心同德. drop=2; 1 <h2> + 3 <h3>
  (section heads 一/二/三) + 127 <p>, byte-exact p-by-p, ZERO severed-<p> merges; standalone=[15,53,90].
  127 body paragraphs; median ratio 5.19 (doctrinal/definitional, as expected). 3 notes (303 cumulative);
  3 net-new keyed glossary rows (交警总队, 华北剿匪总司令部, 聂恩俊). check_content 0 displaced; qc 0 misses;
  register within tolerance ("shall" 33% deliberate). qa_epub PASS; epubcheck 0/0/0/0. **EPUB now 34/43
  chapters.** Detail in PROGRESS.md ("Batch B27"). 5 noise additions (三数百 [ordered before 三数], 四象桥,
  十三、四, 四壁, 两租界, 东四).

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` - derives data/zh/<id>.txt verbatim from data/src, applying per-unit
  drops/merges/heading-splits with a source-conservation check. Specs for ch01-ch33. Merge logic
  FOLLOWS CHAINS. **drop is variable:** most chapters drop=2; ch01/ch10/ch20/ch32 drop=3 (a part
  super-title precedes the preface). `standalone` = a sub-heading kept as its own line with no
  heading markup, emitted as `### ` (used for both plain-<p> sub-heads AND separate <h3> section
  elements, cf. ch33's four <h3> and ch34's three); `glued` = a heading fused onto a paragraph's
  TAIL; `glued_head` = a heading fused onto a paragraph's HEAD; `merges` = source <p> pairs that
  sever one sentence OR an intra-<p> `<br/>` line break, AND can be MASKED by a glitch (ch33 L19/20:
  a stray ！ standing for the closing 」, so also scan ！？》-ending lines, not just non-terminal ones).
  **A chapter can carry INNER enumerated 一、二、三 / 第一、第二 DOCUMENT-CLAUSE or NUMBER-RANGE or
  NAME-LIST content that is NOT a section heading - keep those as ordinary body lines per parity,
  judged by function** (ch27-33).
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
  documented false positive. A NEW unit's TRUE displacements are almost always a keyed name/place/TERM
  rendered a DIFFERENT way than the glossary: align the English to the keyed form (B26 examples: the keyed
  gates 安定门/西直门 must render "Andingmen"/"Xizhimen", not "An'ding Gate"; 冀东冀北 as "East Hebei and
  North Hebei" so the keyed 冀东 "East Hebei" survives as a substring). **Do NOT key a place/term whose
  hanzi is a substring of a DIFFERENT keyed rendering** (B25 河北 not keyed; ch33 华北忠义救国军 rendered
  inline on top of the keyed 忠义救国军). Do NOT add book-TITLE or COMMON-NOUN keys.
- **Verse marker `{p}`** (ch13, reused ch26): prefix a pure-verse line with `{p} `; the builder
  renders `<p class="verse">`; the checks strip it.
- Glossary is authored/merged BY HAND into the SECTIONED file (book/people/organizations/places/
  terms), a dict keyed by hanzi, idempotent + re-read-verified. **Every row MUST carry a `pinyin`
  field** - qc_entities does `rec["pinyin"]` and KeyErrors otherwise. `scripts/add_ch33_glossary.py`
  is the latest by-hand pattern: covers people/organizations/terms sections in one pass, asserts each
  hanzi key is a substring of data/zh/ch33.txt. apparatus_merge's glossary path assumes a FLAT map and
  would corrupt the sectioned file; NOTES still go through apparatus_merge.py (positional arg).
- **qc_entities catches term-rendering drift too:** a glossary common-noun/term rendered a
  different way (or as a VERB not the noun) flags as a "miss." Align the English to the glossary
  (B26: 绥靖 keyed "pacification" flagged when rendered the verb "pacify"). qc has a first/last-word
  fallback, so a keyed en that starts with "the" is trivially satisfied - prefer distinctive en.
- **GLOSSARY-KEY DISCIPLINE:** a key must be a DISTINCTIVE proper noun (or a distinctive institution)
  that renders ONE way everywhere. Periodicals and books are FOOTNOTES/inline. One-off transliterated
  Western/Japanese officer names, one-off telegram/roster/memoir names, standard province names, and
  attested Shanghai ROADS are inline. A bare surname whose full name is unknown is rendered inline.
  NEVER key hanzi that is a substring of a different keyed rendering.
- **Note-anchor gotchas:** anchors must be ASCII, WITHOUT any quote/apostrophe character AND
  without an em dash (U+2014) - all substring traps. The reading.md uses curly quotes and em
  dashes freely, so pick an anchor phrase with none of them. **Multi-occurrence anchors attach at
  the FIRST occurrence** - if a short generic anchor would match an EARLIER paragraph, LENGTHEN it.
- **make_ch33_apparatus.py pattern (scripts/):** author note bodies as plain ASCII + typed hanzi +
  UNTONED pinyin + straight quotes, allow em-dash, ASSERT every non-ASCII glyph occurs in THAT UNIT's
  data/zh/<id>.txt, then convert every non-ASCII char to a numeric char ref and run apparatus_merge.py.
  **A CORRECT glyph may be ABSENT if the source prints a glitch/variant** - describe such terms with
  the source's own form + pinyin/English. A note that quotes ANOTHER unit's text is authored
  ENGLISH-ONLY to avoid the cross-unit glyph-assert. AVOID tone-marked pinyin and curly quotes.
- data/noise.txt carries the B01-B26 project noise rules (each with a comment line). Republican
  years render literally; the checker matches the source numeral (or auto-escapes Republican-year
  N via N+1911). **SPELLED-OUT COMPOUNDS DO NOT COMPOSE** (target "three thousand five hundred" =
  {3000,500}, not 3500; "a hundred and twenty" = {100,20}, not 120): write exact multi-part counts as
  DIGITS (3,500 / 120 / 1,500). Name-numeral glyphs are noised (B26 added 马汉三/英千里/陈资一). Idiom
  numerals noised (B26 added 百废待擧; earlier 百废待兴/百事待擧/退一万步/万一/五旬). The ○ (U+25CB) and 〇
  (U+3007) address/redaction artifacts: the checker cannot read them as digits - noise the mis-read
  glyph-string, carry the real value in English. × (source redaction) renders as an em-dash blank.
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches it; re-run per session).
  setup.sh's ONE failing regression test ("hook stands down on template stub") is a KNOWN false
  alarm; all other regression tests pass.

## Renderings settled / carry-forward

- 军统 / 军统局 -> "the Juntong" / "the Juntong Bureau" (DECIDED). 保密局 -> "the Baomiju" (DECIDED, B26;
  the Juntong's 1946 successor). 戴笠 Dai Li (courtesy Yunong; 老板 "the Boss"; 戴先生 "Mr. Dai"). 制裁
  "sanction". 敌伪 "the enemy and the puppets"; 沦陷区 "the fallen zone(s)". Chiang's titles: 校长 "the
  Commandant", 委员长/委座 "the Generalissimo", 总裁 "the Director-General"; 领袖 "the Leader"; 总理 "the
  Party Leader" (Sun Yat-sen). 日本宪兵队 "the Japanese gendarmerie"; 七十六号 "No. 76"; 特工总部 "Special
  Operations Headquarters"; 三民主义 "the Three Principles of the People."
- **B24 (Shanghai unit vocab):** 大队长 "brigade commander"; 分队 "sub-brigade"; 三道头 "three-stripe
  head"; 内交通 "internal courier".
- **B25 PART-FOUR vocab (reuse):** 总队 "Corps" / 总队长 "Corps Commander"; 大队 "brigade"; 中队 "company";
  指挥室 "command room"; 指挥员 "commanding officer" vs 指挥官 "commander"; 突击队 "assault team"; 直属组
  "directly subordinate section"; 部队长 "unit commander"; 编制 "establishment"; 配属关系 "relation of
  attachment"; 留置工作 "stay-behind work"; 绥靖 "pacification" / 戡乱 "suppression of rebellion" / 剿匪
  "bandit-suppression" / 匪谍 "Communist spies" / 共酋 "Communist chieftains" / 共干 "Communist cadres";
  收复区 "recovered areas" / 交战区 "combat zones"; 行辕 "Field Headquarters". Republican years literal.
- **B26 PART-FOUR vocab (ch33; reuse):** 特种部队 "special-operations unit" (KEYED term; the ch34s01
  title glosses it "Special Forces" at TITLE level only); 特种组织 "special organization" (KEYED term);
  联合会报 "joint briefing"; 直属通信员 "directly subordinate courier"; 配属关系 "relation of attachment";
  外勤单位 "field unit"; 第二厅 "the Second Bureau" (of the Ministry of National Defense); 稽查处长 "chief
  of the inspection department" / 督察长 "chief inspector"; 双重关系 "double relationship" / 双重任务
  "double mission". 华北忠义救国军 "the North China Loyal and Patriotic Army" (built on the keyed 忠义救国军,
  NOT separately keyed). Marshall / Colonel Robertson INLINE (Western).
- **PLACE-NAME CONVENTION (the qc gate enforces the glossary's PINYIN for keyed cities/gates):**
  北平 Beiping, 天津 Tianjin. KEYED gates 安定门 Andingmen, 西直门 Xizhimen (render EXACTLY these, not
  "...Gate"); non-keyed Beiping gates/lanes render in the -men/-hutong pinyin form (Dongzhimen,
  Di'anmen, Jiaodaokou, Mayuan Hutong, Meizha Hutong). KEYED 冀东 "East Hebei". Standard provinces
  render inline in pinyin (河北 Hebei NOT keyed, 绥远 Suiyuan, 山东 Shandong, 河南 Henan, 山西 Shanxi);
  提篮桥 "Tilanqiao Prison", 西苑机场 "Xiyuan airfield" inline. Rail lines by dashed pinyin (Jin-Pu,
  Ping-Han, Ping-Sui, Long-Hai).
- **Book / part titles (in-text; DECIDED; reuse verbatim):** 英雄无名 = "Nameless Heroes"; Part One
  北国锄奸 = "Rooting Out Traitors in the North"; Part Two = "Disgrace at Hanoi"; Part Three 百战声威
  = "Renown Won in a Hundred Battles"; Part Four 平津地区绥靖戡乱 = "Pacification of the Beiping-Tianjin
  Region". 忠义救国军 = "the Loyal and Patriotic Army". Books by FOOTNOTE/inline (not glossary):
  刘培初's 浮生掠影集 "Fleeting Glimpses of a Floating Life" (quoted ch32/ch33; publisher 正中书局 = "the
  Cheng Chung Book Company").
- **B25 shelf (ch32; keyed):** 叶剑英 Ye Jianying, 刘培初 Liu Peichu, 李宗仁 Li Zongren, 傅作义 Fu Zuoyi,
  计兆祥 Ji Zhaoxiang; orgs 绥靖总队, 军事调处执行部, 军事三人小组, 励志训练班; term 励志计划.
- **B26 shelf (ch33; keyed):** people 李玉林 Li Yulin (deputy brigade cmdr, a pillar), 罗敬 Luo Jing
  (political director / cover calligrapher, a pillar), 侯腾 Hou Teng, 吴安之 Wu Anzhi, 马汉三 Ma Hansan,
  张家铨 Zhang Jiaquan, 史泓 Shi Hong, 陈诚 Chen Cheng; orgs 保密局 the Baomiju, 人民服务总队 the People's
  Service Corps; terms 特种部队 "special-operations unit", 特种组织 "special organization". 刘原深 Liu
  Yuanshen (the third pillar, collator of the series) was already keyed at an earlier batch.
- **B27 shelf (ch34; keyed):** orgs 交警总队 "Transport Police Corps", 华北剿匪总司令部 "North China
  Bandit-Suppression Headquarters" (the 0760-code issuer; built on the keyed 剿匪 "bandit-suppression");
  person 聂恩俊 Nie Enjun (First Brigade quartermaster; provisional). Kept INLINE (per the ch33 decision):
  王兆芬 Wang Zhaofen, 张作兴 Zhang Zuoxing, the spy students 杨荣远/王铭扬, the brigade-commander roster,
  the command-room COs, 廖耀湘 Liao Yaoxiang, 唐鲁孙 Tang Lusun, the Tianjin joint-office members. B27
  reused the keyed 特种部队/特种组织 in the body (title-level "Special Forces" is title-only); 谭家菜/韩家菜,
  the India-Burma Expeditionary Force, and the Transport Police Corps are FOOTNOTED.
- **Earlier shelves (B15-B24)** remain in PROGRESS.md and prior HANDOFFs; the whole B02-B24 cast is
  keyed. Consult glossary.json before romanizing anything.

## Voice sheet - CHEN GONGSHU (author / narrator)

- REGISTER: educated, formal, essayistic first person; grave and a touch archaic but not stilted.
  Long semicolon-joined clauses; four-character idiom and classical allusion used freely and
  footnoted when they carry weight. Refers to himself as 笔者 "the writer" and 我 "I." His narrating
  "shall" is DELIBERATE - do not de-formalize it; check_register flags it informationally.
- STANCE: self-justifying yet self-effacing; insists on truthfulness, admits his blunders; tender
  toward dead comrades, bitter and scornful toward the enemy and the Communists. When quoting
  hostile/puppet/comrades' documents, keep the quoted register DISTINCT from Chen's own dry scorn.
  **Part Four (from ch32) is the 1946-49 civil war: the Nationalist idiom sharpens (共匪 "the Communist
  bandits", 绥靖戡乱 "pacification and the suppression of rebellion") - PRESERVE it, footnote where
  contested, text stands.**
- Ratio ~4.55-4.78 en/han in NARRATIVE; prefaces denser (ch32 5.57); DOCUMENT/QUOTE-HEAVY chapters
  run higher (ch33 = 5.32, ~half quoted memoir). Read the note, do not reset. Alignment/register are
  the gates, not the raw ratio.

## Voice sheets - principal & recurring cast (Part Four)

- **CHEN GONGSHU himself.** Commands the First Brigade of the Pacification Corps in the Beiping-Tianjin
  region, 1946-49; also (against his will) leader of the Baomiju's Beiping directly subordinate section.
- **ZHENG JIEMIN (郑介民 / Mr. Zheng).** Chen's old Beiping-days superior; now Chief of the Second Bureau
  of the Ministry of National Defense, government rep on the Executive Headquarters, head of the Lizhi
  Class. Chen works under him through Part Four.
- **LIU PEICHU (刘培初).** Corps Commander of the Pacification Corps; ascetic, hard-driving (Chen dislikes
  his methods); author of the quoted memoir Fleeting Glimpses of a Floating Life.
- **THE THREE FIRST-BRIGADE PILLARS (introduced ch33 section 4):** LI YULIN (李玉林, deputy commander,
  the East-Hebei guerrilla and Japanese-prison survivor "Fifth Brother"); LUO JING (罗敬, political
  director, the upright calligrapher of the covers, bomb-wounded at Chongqing 1941); LIU YUANSHEN
  (刘原深, chief secretary and field commanding officer, the series' collator).
- **MAO RENFENG (毛人凤 / Mr. Mao).** Head of the Baomiju; would-be heir to Dai Li; imposed the Beiping
  directly subordinate section on Chen. Zheng and Mao run parallel, unconnected chains under the Ministry.

## ⚠ Name trap RESOLVED (do not reopen): 陈邦国 / 郑邦国

The Hanoi action-team member the source spells 郑邦国 in ch13 and 陈邦国 in ch15/ch16/ch17 is ONE
man. RESOLVED to **Chen Bangguo (陈邦国)**. Use Chen Bangguo consistently.

## Where the book stands

- Part One (北国锄奸) COMPLETE (B01-B05). Part Two ("Disgrace at Hanoi") COMPLETE (B06-B13). Part
  Three ("Renown Won in a Hundred Battles" / 百战声威) COMPLETE (B14-B24).
- **Part Four ("Pacification of the Beiping-Tianjin Region") OPEN: B25 = ch32 (self-preface) DONE;
  B26 = ch33 (第一章, first narrative chapter) DONE; B27 = ch34 (第二章, the doctrinal chapter) DONE.**
- **NEXT: B28 = ch35** = 第三章 一番风雨 几片落叶 "Chapter 3. A Spell of Storm, a Few Fallen Leaves" - a
  NARRATIVE chapter (reporting for duty and fixing the chain of command; gathering old comrades; a lead
  teased from personal connections; a cautionary ending). Structure CONFIRMED at B27: 1 <h2> + 4 <h3>
  (section heads 一、/二、/三、/四、) + 196 <p>, NO <h1>/<br/>/<img>/note-markers, **drop=2**; the 4 <h3>
  are SEPARATE elements -> `standalone ### `. After drop=2 the txt has 200 body lines = 4 heading + 196 <p>.
  Grep p-by-p for severed-<p> boundaries (non-terminal AND glitch-masked ！？》). book.json ch35 carries
  `sections` [ch35s01-ch35s04]. Expect a NARRATIVE ratio (~4.55-4.78), not ch34's doctrinal 5.19.
- After B28: B29 = ch36. Part Four = ch32-ch43; ch33-ch42 carry `sections` arrays (the 1946-49 narrative);
  ch43 = the Afterword. Working batch labels run ONE AHEAD of book.json's batches array from ch24 on
  (ch33 = B26, ch34 = B27, ch35 = B28). Open trap: a stray source glyph 毛酋 in a ch36 section title
  (book.json renders it "the Bandit Chief").
- The frozen register reference is `reference/B01_frozen.md`. Narrative sits at 4.55-4.78 en/han;
  prefaces denser (ch32 = 5.57); document/quote-heavy chapters higher (ch33 = 5.32); doctrinal higher
  still (ch34 = 5.19) - alignment/register are the gates, not the raw ratio.
- Sub-heading pattern: Part Four chapters ch33-ch42 carry book.json `sections` arrays; the section
  headings appear in the source as SEPARATE <h3> ELEMENTS that emit as `standalone ### `. DISTINGUISH
  enumerated LIST items / document clauses / number-ranges / name-lists (kept as body lines per parity)
  from the true section headings. Grep each new chapter p-by-p.
- WATCH for source anomalies: cuts, misplaced-「 glitches, corrupt/dropped-character phrases, dropped
  full stops, a STRAY glyph fused onto a title, stray ？/》/！ (often standing for a closing 」), the
  ○ (U+25CB) / 〇 (U+3007) and × redactions, name glitches, variant forms, pervasive single-character
  substitutions. Severed-<p> boundaries MERGE, and can be MASKED by a glitch (ch33 L19/20). Re-grep each
  batch's source for `\[\d+\]` note markers (none through B27).

## Open items for the read-through / completion

- Feed decided renderings back to authority.json on completion: 军统 "the Juntong"; 保密局 "the Baomiju";
  the full B02-B26 historical-name set; the Part-Four vocabulary (绥靖/戡乱/绥靖总队/励志计划/特种部队/
  特种组织 etc.).
- Japanese name readings to firm up when the men recur.
- Provisional romanizations to firm up (glossary `provisional` rows, incl. the B26 people 李玉林/罗敬/
  侯腾/吴安之/马汉三/张家铨/史泓 and 人民服务总队; 刘培初/计兆祥 marked provisional).
- Whole-book reconciliation items: ch09 "Jize County" (the 鸡泽县 key); the pinyin-vs-postal city names;
  the two B20 keyed-substring false positives (武汉卿 / 劳勃生路). The Malone spelling (ch30, footnoted).
  Stray source glyph still to resolve: 毛酋 in a ch36 section title (book.json renders it "the Bandit
  Chief"). The ch32 "Fifth Part" numbering discrepancy (footnoted; restated as Chen's own count in ch33).

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01-B26 builds (0/0/0/0). Source is a clean digital
  EPUB, predominantly simplified with residual variant glyphs and pervasive digitization glitches
  (list them, render to plain sense, do not footnote mechanical typos). B01-B26 glitch lists in
  PROGRESS.md.
- Running-header line 英雄无名-陈恭澍 opens all 43 content files: drop it. drop count is variable -
  most drop=2; ch01/ch10/ch20/ch32 drop=3.
- Enumerated ；/：/、 bullet lists, quoted-document/directive/roster lines (INCLUDING intra-<p>
  `<br/>` TABLE rows and INNER document-clause / range / name-list / 第一、第二 lists), salutations,
  verse lines, run-in section labels, and 『』/「」-closed dialogue are DELIBERATE separate lines
  - do NOT merge them; only genuine mid-phrase splits (last char not terminal, OR a source <p>
  boundary that severs one sentence - possibly MASKED by a glitch ！/？/》 for 」, OR an intra-<p>
  `<br/>` inside PROSE) merge, and those can CHAIN.
- Faithful numbering gaps/anomalies (NOT errors): Part Three skips 第七章 (ch27 = 第八章); 第十章 splits
  into (上)/(下) (ch29/ch30); 三面受敌 一往无前 titles two chapters; ch32 numbers the Beiping-Tianjin
  volume "the Fifth Part" though Shanghai was "the Third Part" (footnoted). Preserve and footnote.
- Expect a stray per-task branch at the top of every batch; consolidate onto claude/nameless-heroes
  per rule 2.
