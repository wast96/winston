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
Nameless Heroes B30

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once (its ONE failing regression test, "hook stands down on template stub", is a KNOWN false alarm; all others pass), then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05) through B29 (ch36) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them. PARTS ONE, TWO ("Disgrace at Hanoi") and THREE ("Renown Won in a Hundred Battles" / 百战声威) are COMPLETE; PART FOUR ("Pacification of the Beiping-Tianjin Region" / 平津地区绥靖戡乱) is OPEN - ch32 was its self-preface, ch33/ch34/ch35/ch36 the first four narrative chapters. The EPUB now holds 36/43 chapters, 319 notes. NOTE on batch numbering: book.json's batches array lumps ch23+ch24 as "B17", so the working batch labels run ONE AHEAD of the book.json array from ch24 on (ch36 = working B29 = book.json's B28 entry; ch37 = working B30 = book.json's B29 entry).

Do Batch B30 = ch37 = 第五章 兵连祸结 民不聊生 "Chapter 5. War Unending, the People Destitute" (ONE unit; the FIFTH Part-Four narrative chapter). NARRATIVE chapter (expect a ratio roughly in the ch33-ch36 band ~5.1-5.4, but alignment/register are the gates, not the raw ratio): the fall of Shimen (Shijiazhuang) and its aftermath; the pacification unit welcomed in one place and shunned in another; and a bitter fight between a local corps and the Communist militia. ch37 carries a book.json `sections` array [ch37s01 一、石门之失共军十万总攻国军数千人苦撑 "1. The Fall of Shimen: 100,000 Communist Troops Attack, a Few Thousand Nationalists Hold On"; ch37s02 二、环境不同受欢迎与被排斥 "2. Different Ground: Welcomed Here, Shunned There"; ch37s03 三、地方团队与中共民兵的一场苦战 "3. A Bitter Fight: Local Corps against the Communist Militia"] - confirm all three title_en in book.json. Chen's Nationalist idiom stays at its sharpest (共匪/匪 "the Communist bandits", 绥靖戡乱, 匪谍/共酋/共干, 匪军/匪干/匪区) - PRESERVE it, do NOT soften; footnote where scholarship contests, text stands. WATCH: the section-1 title itself carries numerals (十万 100,000, 数千 a few thousand) — the title is a `### ` heading (stripped by the checks), but if any body line restates these, carry exact troop counts as DIGITS. Read the tail of ch36 (out/ch36_reading.md) for the batch seam (ch36 ended section 4 with the Battle of Shijiazhuang; ch37 section 1 reopens on 石门之失, its fall) and the settled Part-Four register/vocab. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch37 (38_index-split-000-0036.txt) from data/src. CONFIRM structure p-by-p against data/src_epub/OEBPS/Text/index_split_000_0036.xhtml [ch37: 1 <h2> (第五章 兵连祸结 民不聊生) + 3 <h3> (the three section headings 一、/二、/三、) + 144 <p>, NO <h1>/<br/>/<img>/[\d+], 0 images - CONFIRMED at B29]. **drop=2** (running header 英雄无名-陈恭澍 + <h2> chapter title). The THREE section headings are SEPARATE <h3> ELEMENTS -> emit each as a `standalone ### ` in clean_batch.py (the ch33-ch36 method). NO count discrepancy expected: the raw txt has NO trailing newline, so it is 149 lines (wc -l counts 148); 149 - drop(2) = 147 body lines = 3 <h3> + 144 <p> = 147. Do the byte-exact p-by-p diff FIRST (the B19-B29 method: extract <p> inner text AND the <h3> texts in document order, walk each consuming 1 body line, assert every line matches) to PIN the 3 heading line-numbers, CONFIRM the count, and LOCATE any SEVERED-<p> boundaries (last char non-terminal -> MERGE; scan ！？》-ending lines too for glitch-MASKED severs, cf. ch33/ch35/ch36 where a stray ！ stood for a closing 」). ⚠ ALSO watch for the ch36-class SOURCE-DUPLICATION artifact (ch36's chapter preamble + section-1 opening were printed 2-3x, with the section-1 heading text fused mid-<p>): if the p-by-p diff shows a run of near-identical paragraphs or a heading text glued inside a <p>, it is a source artifact — translate ALL of it faithfully (parity preserved, nothing dropped/invented, each pass per its own wording) and footnote the repetition. CRITICAL: keep INNER 一、二、三 / 其一、其二 enumerations, number-ranges and name-lists as BODY lines per parity (the ch27-36 lesson: judge by function, not by the leading numeral). Extend scripts/clean_batch.py with ch37's spec (drop=2; the 3 confirmed standalone <h3> heading line-numbers, 1-based; any confirmed severed-<p> merges; NO glued/glued_head unless the diff reveals one). Run it (source-conservation check must pass). Write out/ch37_reading.md (## from book.json title_en; the 3 sections as ### sub-headings from book.json section title_en; one English paragraph per source body line). Then run scripts/batch_artifacts.py ch37, and ALWAYS finish with a NO-ARG run (the trap: an ID-run writes checks.json with ONLY that unit; the no-arg run restores all 37 units so check_structure/check_content see them).
2. Translate to the FROZEN register (Chen's voice sheet in HANDOFF; the narrating "shall" is DELIBERATE, do NOT de-formalize). Consult glossary.json and authority.json BEFORE romanizing anything; REUSE the B25-B29-settled Part-Four renderings (PROGRESS.md "Settled Part-Four renderings" + the B26/B27/B28/B29 shelves). KEYED terms to reuse consistently in the BODY (qc enforces where keyed): 特种部队 "special-operations unit", 特种组织 "special organization"; 军统/军统局 "the Juntong"/"the Juntong Bureau"; 保密局 "the Baomiju"; 绥靖总队 "the Pacification Corps"; 总队 "Corps"/总队长 "Corps Commander"; 大队 "brigade"/大队长 "brigade commander"; 中队 "company"; 分队 "sub-brigade"; 直属组 "directly subordinate section"; 部队长 "unit commander"; 编制 "establishment"; 配属关系 "relation of attachment"; 指挥室 "command room"; 指挥员 "commanding officer" vs 指挥官 "commander"; 北平行辕 "the Beiping Field Headquarters"; 华北剿匪总司令部 "North China Bandit-Suppression Headquarters"; 绥靖 "pacification"/戡乱 "suppression of rebellion"/剿匪 "bandit-suppression"/匪谍 "Communist spies"/共酋 "Communist chieftains"/共干 "Communist cadres". KEYED PLACES/TERMS from B29 to reuse: 石家庄 Shijiazhuang, 石门 Shimen (Chen's usual name for it), 安次 Anci, 安国 Anguo, 正定 Zhengding; 掏心战术 "the heart-extraction tactic", 平津保三角地带 "the Beiping-Tianjin-Baoding triangle". KEYED people likely to recur: 傅作义 Fu Zuoyi, 安春山 An Chunshan, 朱占奎 Zhu Zhankui, 吕正操 Lü Zhengcao, 聂荣臻 Nie Rongzhen, 毛泽东 Mao Zedong, 林彪 Lin Biao, 李玉林 Li Yulin. The Mao epithets 毛酋/毛贼 render "the bandit chief Mao"/"the bandit Mao Zedong" (noted at ch36). Render Republican years literally (the checker matches the source numeral or auto-escapes via +1911; ordinal forms compose - but SPELLED-OUT COMPOUNDS DO NOT: write exact multi-part counts like 十万/数千/两千 as DIGITS 100,000 / a few thousand / 2,000, since "three thousand five hundred" composes to {3000,500} not {3500} - the B26-B29 trap). WATCH the digitization glitches (list in PROGRESS.md, render to plain sense, footnote only real reading uncertainty): same classes throughout (single-char substitutions e.g. ch36's 珍/殄, 右/石, 借/惜, 有/为; dropped 。 stops; dittography; mismatched guillemets ﹁﹂﹃﹄; stray ？/》/！ often standing for a closing 」; stray ︸/︴/|/〔/〕/《 glyphs; ○/〇/× redactions - the numeric checker mis-reads ○/〇; carry the real value in English and noise only the mis-read glyph-string; × redactions render as em-dash "——th" blanks). Dates/counts: carry real values as DIGITS/words; NOISE only idiom/approximate/name-numeral/elided/date-name/counter-by-naming/place-name-numeral forms (data/noise.txt already carries the B01-B29 rules incl. B29's 三角地带/五台/十余万/三〇式/千奇百怪/老千/七、八十/四望/万急/张建三/张建二; add B30's).
3. Checks: verify_unit.py ch37 (parity + numbers with noise auto-found + anchors); check_align.py ch37; regenerate checks.json with scripts/batch_artifacts.py (no args) and run check_structure.py --config checks.json + check_content.py --config checks.json (NOTE: check_content prints KNOWN PRE-EXISTING artifacts and exits nonzero because of them - ch08 Shunde ×3, ch13 ×9, ch09 "Jize County" ×1, ch26's TWO documented keyed-substring FALSE POSITIVES 武汉卿/劳勃生路; CONFIRM ch37 shows "all in the paired paragraph" / 0 displaced, and align any keyed name/place/TERM to its glossary-decided rendering. A NEW unit's displacements are almost always a keyed name/place/term rendered a DIFFERENT way than the glossary - align the English to the keyed form). Do NOT add COMMON-NOUN or book/periodical keys. qc_entities.py on a reconstructed bilingual (data/zh body lines minus the `### ` heading lines + out/ch37_en.json, `> zh` / en pairs; every glossary row needs a pinyin field - the reconstruction one-liner is in PROGRESS/the ch30-ch36 method; WATCH the keyed term rendered as a VERB not the noun, cf. 绥靖 "pacify" vs "pacification"). Verify the TAIL against the source. check_register.py --ref reference/B01_frozen.md out/ch37_reading.md ("shall" deliberate).
4. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (full list in PROGRESS.md; the big already-covered furniture incl. the Nationalist 绥靖/戡乱/共匪 framing, the Marshall Mission/Committee of Three/Executive HQ, the Lizhi Plan/Class, the Youth Army, Fu Zuoyi/Beiping's surrender, the Baomiju, Whampoa, the Marco Polo Bridge, fabi, the Republican-year system, the Transport Police Corps, the Three-Anti/Five-Anti/Suppress-Counterrevolutionaries campaigns, the Social Affairs Department, the Cultural Revolution/Red Guards, Lin Biao's 1971 death, and from B29: the Battle of Shijiazhuang [12 Nov 1947], the Nationalist recovery of Yan'an [Mar 1947], the heart-extraction tactic, the Type 38/Type 30 rifles, the Paojuzi prison, the Mao epithets, and the scholarship verdict that Mao was NOT at Anguo in 1947). LIKELY new for ch37: whatever fresh material culture / institutions / place-lore the three sections raise (the fall of Shimen and the local-corps-vs-militia fight are the new ground). Be generous but do NOT pad, do NOT re-note. Merge notes via apparatus_merge.py (positional arg: apparatus_merge.py data/ch37_apparatus.json; numeric character references only in note bodies; anchors verbatim ASCII substrings of the reading.md body text, NO em dash and NO quote/apostrophe character - substring traps; multi-occurrence anchors attach at the first; TIGHTEN a generic anchor). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field; apparatus_merge's glossary path assumes a FLAT map and would corrupt the sectioned file - use it ONLY for notes; scripts/add_ch36_glossary.py is the latest by-hand pattern, asserting each hanzi key against data/zh). For any CJK in a note body use the make_ch36_apparatus.py pattern (author bodies with typed hanzi + untoned pinyin, ASSERT every non-ASCII glyph is present in data/zh/ch37.txt, then convert to NCRs) - and remember a CORRECT glyph may be ABSENT if the source prints a glitch/variant form, so describe such terms with the source's own form + pinyin. Confirm ch37's image count (grep <img>; ch32-ch36 carried none).
5. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; update HANDOFF.md; commit and push to claude/nameless-heroes. (Next is B31 = ch38 = 第六章 曲直分明 反复无常, 4 sections; confirm scope in book.json. Working batch labels run ONE AHEAD of book.json's batches array: book.json B30 = ch38 = working B31. Part Four = ch32-ch43; after ch42 only ch43 = the Afterword remains.)

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B31 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
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
  4 <h3> + 153 <p>, TWO severed-<p> merges. 151 body paragraphs; ratio 5.32. 6 notes; 12 keyed rows.
- **Batch B27 (ch34), the DOCTRINAL Part-Four chapter.** 第二章 自动自发 同心同德. drop=2; 1 <h2> + 3 <h3>
  + 127 <p>, ZERO severs; standalone=[15,53,90]. 127 body paragraphs; ratio 5.19. 3 notes; 3 keyed rows.
- **Batch B28 (ch35), the THIRD Part-Four NARRATIVE chapter.** 第三章 一番风雨 几片落叶. drop=2; 1 <h2> +
  4 <h3> + 196 <p>, TWO glitch-masked severs; standalone=[8,49,77,141]. 194 body paragraphs; ratio 5.15.
  8 notes (311 cumulative); 5 keyed rows. Fixed a pre-existing ch32 hyphenation displacement (CORRECTIONS).
- **Batch B29 (ch36), the FOURTH Part-Four NARRATIVE chapter.** 第四章 掌握先机 备多力分. drop=2; 1 <h2> +
  4 <h3> (section heads 一/二/三/四) + 188 <p>, byte-exact p-by-p, standalone=[18,71,108,154], ONE glitch-
  masked sever merges=[(49,50)] (由﹁地方！|转向﹁中央﹂, the ！ for 」). The "1-line count scare" was a
  trailing-newline miscount (file is 194 lines, wc -l 193; 194-2=192=4 h3+188 p). **⚠ MAJOR SOURCE
  DUPLICATION:** the intelligence-timeliness preamble is printed 3× (z2-16, z18-32, z33-37), the Anguo raid
  + contributor intros 2×, and z33 fuses the section-1 heading text mid-<p> — a digital-source artifact,
  translated in FULL per rule 4 with a footnote at the head of section 1. 187 body paragraphs; median ratio
  5.42 (two long contributed memoir-accounts + the tripled preamble). 8 notes (319 cumulative); 13 net-new
  keyed rows (6 people, 5 places, 2 terms). check_content 0 displaced; qc 0 misses; register within tolerance.
  qa_epub PASS; epubcheck 0/0/0/0. **EPUB now 36/43 chapters.** 11 noise additions (三角地带, 五台, 十余万,
  三〇式, 千奇百怪, 老千, 七、八十, 四望, 万急, 张建三, 张建二). Detail in PROGRESS.md ("Batch B29").

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` - derives data/zh/<id>.txt verbatim from data/src, applying per-unit
  drops/merges/heading-splits with a source-conservation check. Specs for ch01-ch36. Merge logic
  FOLLOWS CHAINS. **drop is variable:** most chapters drop=2; ch01/ch10/ch20/ch32 drop=3 (a part
  super-title precedes the preface). `standalone` = a sub-heading kept as its own line with no
  heading markup, emitted as `### ` (used for both plain-<p> sub-heads AND separate <h3> section
  elements, cf. ch33-ch36's <h3> section heads); `glued` = a heading fused onto a paragraph's
  TAIL; `glued_head` = a heading fused onto a paragraph's HEAD; `merges` = source <p> pairs that
  sever one sentence OR an intra-<p> `<br/>` line break, AND can be MASKED by a glitch (scan
  ！？》-ending lines, not just non-terminal ones - ch33 L19/20, ch35 L25/26 & L136/137, ch36 L49/50).
  **A chapter can carry INNER enumerated 一、二、三 / 第一、第二 DOCUMENT-CLAUSE or NUMBER-RANGE or
  NAME-LIST content that is NOT a section heading - keep those as ordinary body lines per parity,
  judged by function** (ch27-36). **⚠ ch36 taught a new anomaly class: SOURCE DUPLICATION (a chapter's
  opening printed 2-3x, with a section-heading text fused mid-<p>). Preserve it all per rule 4; footnote it.**
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
  matching inside 武汉卿 "Wu Hanqing"; 劳勃生 "Lao Bosheng" matching inside 劳勃生路 "Robison Road."**
  The pass criterion for a NEW batch is "the batch's own unit shows all name occurrences in the paired
  paragraph / 0 displaced." A NEW unit's TRUE displacements are almost always a keyed name/place/TERM
  rendered a DIFFERENT way than the glossary: align the English to the keyed form. **Do NOT key a place/term
  whose hanzi is a substring of a DIFFERENT keyed rendering.** Do NOT add book-TITLE or COMMON-NOUN keys.
- **Verse marker `{p}`** (ch13, reused ch26): prefix a pure-verse line with `{p} `; the builder
  renders `<p class="verse">`; the checks strip it.
- Glossary is authored/merged BY HAND into the SECTIONED file (book/people/organizations/places/
  terms), a dict keyed by hanzi, idempotent + re-read-verified. **Every row MUST carry a `pinyin`
  field** - qc_entities does `rec["pinyin"]` and KeyErrors otherwise. `scripts/add_ch36_glossary.py`
  is the latest by-hand pattern: covers people/places/terms sections in one pass, asserts each
  hanzi key is a substring of that unit's data/zh/<id>.txt. apparatus_merge's glossary path assumes a
  FLAT map and would corrupt the sectioned file; NOTES still go through apparatus_merge.py (positional arg).
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
  (ch36 deliberately used this: the duplication note's anchor "already carries within it the sense
  of" attaches at the FIRST of two occurrences, i.e. the head of section 1.)
- **make_ch36_apparatus.py pattern (scripts/):** author note bodies as plain ASCII + typed hanzi +
  UNTONED pinyin + straight quotes, allow em-dash, ASSERT every non-ASCII glyph occurs in THAT UNIT's
  data/zh/<id>.txt, then convert every non-ASCII char to a numeric char ref and run apparatus_merge.py.
  **A CORRECT glyph may be ABSENT if the source prints a glitch/variant** - describe such terms with
  the source's own form + pinyin/English. A note that quotes ANOTHER unit's text is authored
  ENGLISH-ONLY to avoid the cross-unit glyph-assert. AVOID tone-marked pinyin and curly quotes.
- data/noise.txt carries the B01-B29 project noise rules (each with a comment line). Republican
  years render literally; the checker matches the source numeral (or auto-escapes Republican-year
  N via N+1911). **SPELLED-OUT COMPOUNDS DO NOT COMPOSE** (target "three thousand five hundred" =
  {3000,500}, not 3500): write exact multi-part counts as DIGITS (3,500 / 120 / 3,200,000). **ORDER
  MATTERS in noise.txt:** a longer numeral idiom must precede a shorter one that is its prefix, or the
  shorter consumes it and orphans a digit (B29: 十余万 had to be placed BEFORE the bare 十余, else 十余
  fired first and left 万=10000 unmatched). Name-numeral glyphs, idiom numerals, approximate ranges,
  place-name numerals, and counter-by-naming forms are noised. The ○ (U+25CB) and 〇 (U+3007)
  address/redaction artifacts: the checker cannot read them as digits - noise the mis-read glyph-string,
  carry the real value in English. × (source redaction) renders as an em-dash blank.
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches it; re-run per session).
  setup.sh's ONE failing regression test ("hook stands down on template stub") is a KNOWN false
  alarm; all other regression tests pass.

## Renderings settled / carry-forward

- 军统 / 军统局 -> "the Juntong" / "the Juntong Bureau" (DECIDED). 保密局 -> "the Baomiju" (DECIDED, B26;
  the Juntong's 1946 successor). 戴笠 Dai Li (courtesy Yunong; 老板 "the Boss"; 戴先生 "Mr. Dai"). 制裁
  "sanction". 敌伪 "the enemy and the puppets"; 沦陷区 "the fallen zone(s)". Chiang's titles: 校长 "the
  Commandant", 委员长/委座 "the Generalissimo", 总裁 "the Director-General"; 领袖 "the Leader"; 总理 "the
  Party Leader" (Sun Yat-sen). 三民主义 "the Three Principles of the People."
- **B24 (Shanghai unit vocab):** 大队长 "brigade commander"; 分队 "sub-brigade"; 三道头 "three-stripe
  head"; 内交通 "internal courier".
- **B25 PART-FOUR vocab (reuse):** 总队 "Corps" / 总队长 "Corps Commander"; 大队 "brigade"; 中队 "company";
  指挥室 "command room"; 指挥员 "commanding officer" vs 指挥官 "commander"; 突击队 "assault team"; 直属组
  "directly subordinate section"; 部队长 "unit commander"; 编制 "establishment"; 配属关系 "relation of
  attachment"; 留置工作 "stay-behind work"; 绥靖 "pacification" / 戡乱 "suppression of rebellion" / 剿匪
  "bandit-suppression" / 匪谍 "Communist spies" / 共酋 "Communist chieftains" / 共干 "Communist cadres";
  收复区 "recovered areas" / 交战区 "combat zones"; 行辕 "Field Headquarters". Republican years literal.
- **B26 PART-FOUR vocab (ch33; reuse):** 特种部队 "special-operations unit" (KEYED term); 特种组织
  "special organization" (KEYED term); 联合会报 "joint briefing"; 直属通信员 "directly subordinate courier";
  外勤单位 "field unit"; 第二厅 "the Second Bureau"; 双重关系 "double relationship" / 双重任务 "double
  mission". 华北忠义救国军 "the North China Loyal and Patriotic Army" (built on the keyed 忠义救国军).
- **B29 PART-FOUR vocab (ch36; reuse):** 掏心战术 "the heart-extraction tactic" (KEYED term); 平津保三角地带
  "the Beiping-Tianjin-Baoding triangle" (KEYED term/place); 暂编第三军/暂三军 "the Provisional Third Army";
  联合肃奸组 "the Joint Traitor-Rooting Group"; 任务编组 "task-detachment"; 三通 "the three connections";
  三八式/三〇式 "the Type 38"/"Type 30" rifles; 弄权 "abuse of power"; 匪酋 "bandit chieftains" / 匪军 "the
  bandit army/forces" / 匪干 "bandit cadres" / 匪区 "bandit-held territory". The Mao epithets: 毛酋 "the
  bandit chief Mao" (book.json title level "the Bandit Chief"), 毛贼泽东 "the bandit Mao Zedong", 毛某 "the
  man Mao"/"Mao".
- **PLACE-NAME CONVENTION (the qc gate enforces the glossary's PINYIN for keyed cities/gates):**
  北平 Beiping, 天津 Tianjin. KEYED (B29): 石家庄 Shijiazhuang, 石门 Shimen, 安次 Anci, 安国 Anguo,
  正定 Zhengding. KEYED gates 安定门 Andingmen, 西直门 Xizhimen; KEYED 冀东 "East Hebei". Standard provinces
  render inline in pinyin (河北 Hebei NOT keyed, 山西 Shanxi, 山东 Shandong, 河南 Henan, 陕西 Shaanxi,
  绥远 Suiyuan, 察哈尔 Chahar). 冀中 "Central Hebei", 冀南 "South Hebei", 冀东 "East Hebei"; 晋察冀 "Jin-Cha-Ji".
  Rail lines by dashed pinyin (Ping-Han, Zheng-Tai, Bei-Ning, Ping-Gu, Ping-Sui, Ping-Bao, Zhe-Gan,
  Long-Hai). 五台山 the Wutai Mountains, 太行山 the Taihang Mountains, 延安 Yan'an, 药王庙 the Temple of the
  Medicine King - all INLINE.
- **Book / part titles (in-text; DECIDED; reuse verbatim):** 英雄无名 = "Nameless Heroes"; Part One
  北国锄奸 = "Rooting Out Traitors in the North"; Part Two = "Disgrace at Hanoi"; Part Three 百战声威
  = "Renown Won in a Hundred Battles"; Part Four 平津地区绥靖戡乱 = "Pacification of the Beiping-Tianjin
  Region". 忠义救国军 = "the Loyal and Patriotic Army".
- **B25 shelf (ch32; keyed):** 叶剑英 Ye Jianying, 刘培初 Liu Peichu, 李宗仁 Li Zongren, 傅作义 Fu Zuoyi,
  计兆祥 Ji Zhaoxiang; orgs 绥靖总队, 军事调处执行部, 军事三人小组, 励志训练班; term 励志计划.
- **B26 shelf (ch33; keyed):** people 李玉林 Li Yulin, 罗敬 Luo Jing, 侯腾 Hou Teng, 吴安之 Wu Anzhi,
  马汉三 Ma Hansan (= the "Mr. Ma" of Meizha Hutong, recurs in ch36 section 2 inline as 马先生), 张家铨 Zhang
  Jiaquan, 史泓 Shi Hong, 陈诚 Chen Cheng; orgs 保密局, 人民服务总队; terms 特种部队, 特种组织. 刘原深 Liu
  Yuanshen keyed earlier.
- **B27 shelf (ch34; keyed):** orgs 交警总队 "Transport Police Corps", 华北剿匪总司令部 "North China
  Bandit-Suppression Headquarters"; person 聂恩俊 Nie Enjun (provisional).
- **B28 shelf (ch35; keyed):** people 李鸣秋 Li Mingqiu (the go-between; provisional), 李运昌 Li Yunchang,
  罗荣桓 Luo Ronghuan, 黄郛 Huang Fu; org 东北人民解放军 "the Northeast People's Liberation Army".
- **B29 shelf (ch36; keyed):** people 安春山 An Chunshan (Provisional Third Army cmdr; provisional), 朱占奎
  Zhu Zhankui (Anci magistrate, re-defector; provisional), 刘玉珠 Liu Yuzhu (the gun-gift fixer; provisional),
  萧润宇 Xiao Runyu (section-3 account author; provisional), 牛广金 Niu Guangjin (section-4 account author;
  provisional), 吕正操 Lü Zhengcao (Central Hebei Military District cmdr; attested); places 石家庄/石门/安次/
  安国/正定; terms 掏心战术, 平津保三角地带. Kept INLINE (per the ch33-36 decisions): 罗历戎 Luo Lirong, 刘英
  Liu Ying, 张铁林 Zhang Tielin, the section/work-group rosters, 曾泽生 Zeng Zesheng, 刘伯承 Liu Bocheng, 胡宗南
  Hu Zongnan, 邓宝珊 Deng Baoshan, 傅东菊 Fu Dongju, the border-region committee, the Shimen relief mission.
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
  bandits", 绥靖戡乱, 匪酋, the Mao epithets 毛酋/毛贼) - PRESERVE it, footnote where contested, text stands.**
- Ratio ~4.55-4.78 en/han in NARRATIVE; prefaces denser (ch32 5.57); DOCUMENT/QUOTE-HEAVY chapters
  run higher (ch33 5.32, ch34 5.19, ch35 5.15, ch36 5.42 - two contributed memoir-accounts + a tripled
  preamble). Read the note, do not reset. Alignment/register are the gates, not the raw ratio.

## Voice sheets - principal & recurring cast (Part Four)

- **CHEN GONGSHU himself.** Commands the First Brigade of the Pacification Corps in the Beiping-Tianjin
  region, 1946-49; also (against his will) leader of the Baomiju's Beiping directly subordinate section.
- **ZHENG JIEMIN (郑介民 / Mr. Zheng).** Chen's old Beiping-days superior; Chief of the Second Bureau of
  the Ministry of National Defense, government rep on the Executive Headquarters, head of the Lizhi Class.
- **LIU PEICHU (刘培初).** Corps Commander of the Pacification Corps; ascetic, hard-driving.
- **THE THREE FIRST-BRIGADE PILLARS (ch33 s4):** LI YULIN (李玉林, deputy cmdr, "Fifth Brother"; central to
  ch36's gun-gift affair), LUO JING (罗敬, political director), LIU YUANSHEN (刘原深, chief secretary).
- **MAO RENFENG (毛人凤 / Mr. Mao).** Head of the Baomiju; imposed the Beiping directly subordinate section.

## ⚠ Name trap RESOLVED (do not reopen): 陈邦国 / 郑邦国

The Hanoi action-team member the source spells 郑邦国 in ch13 and 陈邦国 in ch15/ch16/ch17 is ONE
man. RESOLVED to **Chen Bangguo (陈邦国)**. Use Chen Bangguo consistently.

## Where the book stands

- Part One (北国锄奸) COMPLETE (B01-B05). Part Two ("Disgrace at Hanoi") COMPLETE (B06-B13). Part
  Three ("Renown Won in a Hundred Battles" / 百战声威) COMPLETE (B14-B24).
- **Part Four ("Pacification of the Beiping-Tianjin Region") OPEN: B25 = ch32 (self-preface) DONE;
  B26 = ch33 (第一章) DONE; B27 = ch34 (第二章, doctrinal) DONE; B28 = ch35 (第三章, narrative) DONE;
  B29 = ch36 (第四章, narrative) DONE.**
- **NEXT: B30 = ch37** = 第五章 兵连祸结 民不聊生 "Chapter 5. War Unending, the People Destitute" - a
  NARRATIVE chapter (the fall of Shimen and its aftermath; the pacification unit welcomed in one place and
  shunned in another; a bitter local-corps-vs-Communist-militia fight). Structure CONFIRMED at B29: 1 <h2>
  + 3 <h3> (section heads 一、/二、/三、) + 144 <p>, NO <h1>/<br/>/<img>/note-markers, 0 images, **drop=2**;
  the 3 <h3> are SEPARATE elements -> `standalone ### `. NO count discrepancy (raw txt = 149 lines, no
  trailing newline; 149 - 2 = 147 = 3 <h3> + 144 <p>). book.json ch37 carries `sections` [ch37s01-ch37s03].
  Grep p-by-p for severed-<p> boundaries (non-terminal AND glitch-masked ！？》) AND for a ch36-class
  source-duplication run (near-identical paragraphs / a heading text fused mid-<p>).
- After B30: B31 = ch38 = 第六章 曲直分明 反复无常 (4 sections). Part Four = ch32-ch43; ch33-ch42 carry
  `sections` arrays (the 1946-49 narrative); ch43 = the Afterword. Working batch labels run ONE AHEAD of
  book.json's batches array from ch24 on (ch36 = B29, ch37 = B30, ch38 = B31).
- The frozen register reference is `reference/B01_frozen.md`. Prefaces denser (ch32 = 5.57);
  document/quote-heavy chapters higher (ch33 = 5.32, ch34 = 5.19, ch35 = 5.15, ch36 = 5.42) -
  alignment/register are the gates, not the raw ratio.
- Sub-heading pattern: Part Four chapters ch33-ch42 carry book.json `sections` arrays; the section
  headings appear in the source as SEPARATE <h3> ELEMENTS that emit as `standalone ### `. DISTINGUISH
  enumerated LIST items / document clauses / number-ranges / name-lists (kept as body lines per parity)
  from the true section headings. Grep each new chapter p-by-p.
- WATCH for source anomalies: cuts, misplaced-「 glitches, corrupt/dropped-character phrases, dropped
  full stops, a STRAY glyph fused onto a title, stray ？/》/！ (often standing for a closing 」), the
  ○ (U+25CB) / 〇 (U+3007) and × redactions, name glitches, variant forms, pervasive single-character
  substitutions, severed-<p> boundaries (MERGE; can be glitch-MASKED), AND the ch36-class SOURCE
  DUPLICATION (a chapter's opening printed 2-3x, heading text fused mid-<p> - preserve all, footnote it).
  Re-grep each batch's source for `\[\d+\]` note markers (none through B29).

## Open items for the read-through / completion

- Feed decided renderings back to authority.json on completion: 军统 "the Juntong"; 保密局 "the Baomiju";
  the full B02-B29 historical-name set; the Part-Four vocabulary (绥靖/戡乱/绥靖总队/励志计划/特种部队/
  特种组织/掏心战术/平津保三角地带 etc.).
- Japanese name readings to firm up when the men recur.
- Provisional romanizations to firm up (glossary `provisional` rows, incl. the B29 people 安春山/朱占奎/
  刘玉珠/萧润宇/牛广金; the B26 people 李玉林/罗敬/侯腾/吴安之/马汉三/张家铨/史泓; 刘培初/计兆祥).
- Whole-book reconciliation items: ch09 "Jize County" (the 鸡泽县 key); the pinyin-vs-postal city names;
  the two B20 keyed-substring false positives (武汉卿 / 劳勃生路). The Malone spelling (ch30, footnoted).
  The ch32 "Fifth Part" numbering discrepancy (footnoted). The garbled deputy-chief-of-staff surname
  glyph 鿄 (ch36, rendered "—— Shuzai") - firm up if identifiable. The Mao-at-Anguo intelligence is
  footnoted as a scholarship verdict (ch36).

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01-B29 builds (0/0/0/0). Source is a clean digital
  EPUB, predominantly simplified with residual variant glyphs and pervasive digitization glitches
  (list them, render to plain sense, do not footnote mechanical typos). B01-B29 glitch lists in
  PROGRESS.md. **ch36 added a SOURCE-DUPLICATION class (opening printed 2-3x) - watch for it.**
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
