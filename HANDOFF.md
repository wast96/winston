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
Nameless Heroes B29

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once (its ONE failing regression test, "hook stands down on template stub", is a KNOWN false alarm; all others pass), then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05) through B28 (ch35) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them. PARTS ONE, TWO ("Disgrace at Hanoi") and THREE ("Renown Won in a Hundred Battles" / 百战声威) are COMPLETE; PART FOUR ("Pacification of the Beiping-Tianjin Region" / 平津地区绥靖戡乱) is OPEN - ch32 was its self-preface, ch33/ch34/ch35 the first three narrative chapters. The EPUB now holds 35/43 chapters, 311 notes. NOTE on batch numbering: book.json's batches array lumps ch23+ch24 as "B17", so the working batch labels run ONE AHEAD of the book.json array from ch24 on (ch35 = working B28 = book.json's B27 entry; ch36 = working B29 = book.json's B28 entry).

Do Batch B29 = ch36 = 第四章 掌握先机 备多力分 "Chapter 4. Seizing the Initiative, Spread Too Thin" (ONE unit; the FOURTH Part-Four narrative chapter). NARRATIVE chapter (expect a ratio roughly in the ch33-ch35 band 5.1-5.3, but alignment/register are the gates, not the raw ratio): intelligence value and its use; a freak mischance that nearly drew Chen into an abuse-of-power affair; the "heart-extraction" tactic mistimed and the Bandit Chief's escape; and the fighting and sacrifice at the Battle of Shijiazhuang. ch36 carries a book.json `sections` array [ch36s01 一、从情报的价値观念说到情报运用 "1. From the Value of Intelligence to Its Use"; ch36s02 二、阴错阳差几乎牵涉到弄权事件 "2. A Freak Mischance, Nearly Drawn into an Abuse of Power"; ch36s03 三、﹁掏心战术﹂失时机毛酋在逃 "3. The 'Heart-Extraction' Tactic Mistimed; the Bandit Chief Escapes"; ch36s04 四、我们在石家庄之役的战斗和牺牲 "4. Our Fighting and Sacrifice at the Battle of Shijiazhuang"] - confirm all four title_en in book.json. OPEN TRAP: 毛酋 appears 2x in the source (the ch36s03 title 毛酋在逃 + at least once in the body); 毛酋 = 毛 Mao + 酋 "chieftain," a scornful Nationalist epithet for Mao Zedong. book.json renders it "the Bandit Chief" (title level); render 毛酋 CONSISTENTLY (decide "the bandit chief Mao"/"the Mao chieftain" in body, keep title as book.json). Chen's Nationalist idiom stays at its sharpest (共匪/匪 "the Communist bandits", 绥靖戡乱, 匪谍/共酋/共干) - PRESERVE it, do NOT soften; footnote where scholarship contests, text stands. Read the tail of ch35 (out/ch35_reading.md) for the batch seam and the settled Part-Four register/vocab. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch36 (37_index-split-000-0035.txt) from data/src. CONFIRM structure p-by-p against data/src_epub/OEBPS/Text/index_split_000_0035.xhtml [ch36: 1 <h2> (第四章 掌握先机 备多力分) + 4 <h3> (the four section headings 一、/二、/三、/四、) + 188 <p>, NO <h1>/<br/>/<img>/[\d+], 0 images - CONFIRMED at B28]. **drop=2** (running header 英雄无名-陈恭澍 + <h2> chapter title). The FOUR section headings are SEPARATE <h3> ELEMENTS -> emit each as a `standalone ### ` in clean_batch.py (the ch33/ch34/ch35 method). ⚠ COUNT DISCREPANCY TO RESOLVE FIRST: the raw txt has 193 lines, so drop=2 leaves 191 body lines, but 4 <h3> + 188 <p> = 192 elements. That 1-line gap means the ingest concatenated a boundary OR one <p> is empty/blank (a U+200B or dropped line) - the byte-exact p-by-p diff will PIN it. Do the diff FIRST (the B19-B28 method: extract <p> inner text AND the <h3> texts in document order, walk each consuming 1 body line, assert every line matches) to PIN the 4 heading line-numbers, RESOLVE the 1-line discrepancy, and LOCATE any SEVERED-<p> boundaries (last char non-terminal -> MERGE; scan ！？》-ending lines too for glitch-MASKED severs, cf. ch33's/ch35's stray ！ for 」). CRITICAL: keep INNER 一、二、三 / 其一、其二 enumerations, number-ranges and name-lists as BODY lines per parity (the ch27-35 lesson: judge by function, not by the leading numeral). Extend scripts/clean_batch.py with ch36's spec (drop=2; the 4 confirmed standalone <h3> heading line-numbers, 1-based; any confirmed severed-<p> merges; NO glued/glued_head unless the diff reveals one). Run it (source-conservation check must pass). Write out/ch36_reading.md (## from book.json title_en; the 4 sections as ### sub-headings from book.json section title_en; one English paragraph per source body line). Then run scripts/batch_artifacts.py ch36, and ALWAYS finish with a NO-ARG run (the trap: an ID-run writes checks.json with ONLY that unit; the no-arg run restores all 36 units so check_structure/check_content see them).
2. Translate to the FROZEN register (Chen's voice sheet in HANDOFF; the narrating "shall" is DELIBERATE, do NOT de-formalize). Consult glossary.json and authority.json BEFORE romanizing anything; REUSE the B25-B28-settled Part-Four renderings (PROGRESS.md "Settled Part-Four renderings" + the B26/B27/B28 rows). KEYED terms to reuse consistently in the BODY (qc enforces): 特种部队 "special-operations unit", 特种组织 "special organization"; 军统/军统局 "the Juntong"/"the Juntong Bureau"; 保密局 "the Baomiju"; 中统 "the Zhongtong"; 复兴社 "the Renaissance Society"; 绥靖总队 "the Pacification Corps"; 总队 "Corps"/总队长 "Corps Commander"; 大队 "brigade"/大队长 "brigade commander"; 中队 "company"; 分队 "sub-brigade"; 直属组 "directly subordinate section"; 部队长 "unit commander"; 编制 "establishment"; 配属关系 "relation of attachment"; 联合会报 "joint briefing"/会报 "briefing"; 指挥室 "command room"; 指挥员 "commanding officer" vs 指挥官 "commander"; 北平行辕 "the Beiping Field Headquarters"; 交警总队 "Transport Police Corps"; 华北剿匪总司令部 "North China Bandit-Suppression Headquarters"; 绥靖 "pacification"/戡乱 "suppression of rebellion"/剿匪 "bandit-suppression"/匪谍 "Communist spies"/共酋 "Communist chieftains"/共干 "Communist cadres". KEYED people likely to recur: 李玉林 Li Yulin, 罗敬 Luo Jing, 刘原深 Liu Yuanshen, 刘培初 Liu Peichu, 聂恩俊 Nie Enjun, 张家铨 Zhang Jiaquan, 史泓 Shi Hong, 郑介民 Zheng Jiemin, 毛人凤 Mao Renfeng, 戴笠 Dai Li, 李宗仁 Li Zongren, 傅作义 Fu Zuoyi; the B28-new keys 李鸣秋 Li Mingqiu, 李运昌 Li Yunchang, 罗荣桓 Luo Ronghuan, 黄郛 Huang Fu, 东北人民解放军 "the Northeast People's Liberation Army"; 林彪 Lin Biao, 陶铸 Tao Zhu, 聂荣臻 Nie Rongzhen, 毛泽东 Mao Zedong. INLINE (do NOT key): 张作兴 Zhang Zuoxing (inline since ch33). Render Republican years literally (the checker matches the source numeral or auto-escapes via +1911; ordinal forms compose - but SPELLED-OUT COMPOUNDS DO NOT: write exact multi-part counts like 3,500 / 120 / 1,500 as DIGITS, since "three thousand five hundred" composes to {3000,500} not {3500} - the B26/B27/B28 trap). WATCH the digitization glitches (list in PROGRESS.md, render to plain sense, footnote only real reading uncertainty): same classes throughout (single-char substitutions e.g. 车/军 and 季/李 seen in ch35, dropped 。 stops, dittography, mismatched guillemets ﹁﹂﹃﹄, stray ？/》/！ often standing for a closing 」, stray ︸/︴/|/≤/︼ glyphs, ○/〇/× redactions - the numeric checker mis-reads ○/〇; carry the real value in English and noise only the mis-read glyph-string; × redactions render as em-dash "——th" blanks). Dates/counts: carry real values as DIGITS/words; NOISE only idiom/approximate/name-numeral/elided/date-name/counter-by-naming/place-name-numeral forms (data/noise.txt already carries the B01-B28 rules incl. counter-by-naming 二人/两地/两者/两旁, name-numeral 万力民, place-name 四平街, approximate 一百三、四十/一百零几; add B29's).
3. Checks: verify_unit.py ch36 (parity + numbers with noise auto-found + anchors); check_align.py ch36; regenerate checks.json with scripts/batch_artifacts.py (no args) and run check_structure.py --config checks.json + check_content.py --config checks.json (NOTE: check_content prints KNOWN PRE-EXISTING artifacts and exits nonzero because of them - ch08 Shunde ×3, ch13 ×9, ch09 "Jize County" ×1, ch26's TWO documented keyed-substring FALSE POSITIVES 武汉卿/劳勃生路; CONFIRM ch36 shows "all in the paired paragraph" / 0 displaced, and align any keyed name/place/TERM to its glossary-decided rendering. A NEW unit's displacements are almost always a keyed name/place/term rendered a DIFFERENT way than the glossary - align the English to the keyed form). Do NOT add COMMON-NOUN or book/periodical keys. qc_entities.py on a reconstructed bilingual (data/zh body lines minus the `### ` heading lines + out/ch36_en.json, `> zh` / en pairs; every glossary row needs a pinyin field - the reconstruction one-liner is in PROGRESS/the ch30-ch35 method; WATCH the keyed term rendered as a VERB not the noun, cf. 绥靖 "pacify" vs "pacification"). Verify the TAIL against the source. check_register.py --ref reference/B01_frozen.md out/ch36_reading.md ("shall" deliberate).
4. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (full list in PROGRESS.md; the big already-covered furniture incl. the Nationalist 绥靖/戡乱/共匪 framing, the Marshall Mission/Committee of Three/Executive HQ, the Lizhi Plan/Class, the Jiangxi bandit-suppression/别働总队, the Youth Army, Fu Zuoyi/Beiping's surrender, the Baomiju [ch04], Whampoa, the Marco Polo Bridge, fabi, the Republican-year system, the Transport Police Corps, and from B28: the Jin'ao-Yudong Bridge, the 1927 Party Purge / Ning-Han Split, the Guangzhou Uprising, Lin Biao's 1971 death, the Three-Anti/Five-Anti/Suppress-Counterrevolutionaries campaigns, the Social Affairs Department, the Cultural Revolution/Red Guards). LIKELY new for ch36: the Battle of Shijiazhuang (石家庄之役, the PLA's Nov-1947 capture of Shijiazhuang - a real, notable battle); the "heart-extraction tactic" (掏心战术) if it needs a gloss. Be generous but do NOT pad, do NOT re-note. Merge notes via apparatus_merge.py (positional arg: apparatus_merge.py data/ch36_apparatus.json; numeric character references only in note bodies; anchors verbatim ASCII substrings of the reading.md body text, NO em dash and NO quote/apostrophe character - substring traps; multi-occurrence anchors attach at the first; TIGHTEN a generic anchor). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field; apparatus_merge's glossary path assumes a FLAT map and would corrupt the sectioned file - use it ONLY for notes; scripts/add_ch35_glossary.py is the latest by-hand pattern, asserting each hanzi key against data/zh). For any CJK in a note body use the make_ch35_apparatus.py pattern (author bodies with typed hanzi + untoned pinyin, ASSERT every non-ASCII glyph is present in data/zh/ch36.txt, then convert to NCRs) - and remember a CORRECT glyph may be ABSENT if the source prints a glitch/variant form (cf. ch35's 玉𬟽 for 蝀), so describe such terms with the source's own form + pinyin. Confirm ch36's image count (grep <img>; ch32-ch35 carried none).
5. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; update HANDOFF.md; commit and push to claude/nameless-heroes. (Next is B30 = ch37; ch33-ch42 all carry `sections` arrays; confirm scope in book.json. Working batch labels run ONE AHEAD of book.json's batches array: book.json B29 = ch37 = working B30. Part Four = ch32-ch43; after ch42 only ch43 = the Afterword remains.)

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B30 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
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
- **Batch B28 (ch35), the THIRD Part-Four NARRATIVE chapter.** 第三章 一番风雨 几片落叶. drop=2; 1 <h2> +
  4 <h3> (section heads 一/二/三/四) + 196 <p>, byte-exact p-by-p, TWO glitch-masked severed-<p> merges
  (L25/26 天津站！|长时, the ！ for 」 splitting 站长; L136/137 在打流！|﹂, the dialogue's closing ﹂ orphaned);
  standalone=[8,49,77,141]. 194 body paragraphs; median ratio 5.15 (marble-bridge digression + essayistic
  reflection lift it above the ~4.55-4.78 narrative guide). 8 notes (311 cumulative); 5 net-new keyed
  glossary rows (李鸣秋, 李运昌, 罗荣桓, 黄郛 people; 东北人民解放军 org). check_content 0 displaced (+ fixed a
  PRE-EXISTING ch32 hyphenation displacement, see CORRECTIONS.md); qc 0 misses; register within tolerance
  ("shall" 11% deliberate). qa_epub PASS; epubcheck 0/0/0/0. **EPUB now 35/43 chapters.** Detail in
  PROGRESS.md ("Batch B28"). 8 noise additions (两旁, 两者, 二人, 两地, 万力民, 四平街, 一百三、四十, 一百零几).

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
  field** - qc_entities does `rec["pinyin"]` and KeyErrors otherwise. `scripts/add_ch35_glossary.py`
  is the latest by-hand pattern: covers people/organizations/terms sections in one pass, asserts each
  hanzi key is a substring of that unit's data/zh/<id>.txt. apparatus_merge's glossary path assumes a FLAT map and
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
- **make_ch35_apparatus.py pattern (scripts/):** author note bodies as plain ASCII + typed hanzi +
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
- **B28 shelf (ch35; keyed):** people 李鸣秋 Li Mingqiu (the ex-Communist go-between, the chapter's pivot;
  provisional), 李运昌 Li Yunchang (East-Hebei guerrilla chief, later CCP general/Minister of Railways),
  罗荣桓 Luo Ronghuan (NE-army commissar, later marshal), 黄郛 Huang Fu (the diplomat Yingbai, He Yingqin's
  early-1930s Beiping stand-in); org 东北人民解放军 "the Northeast People's Liberation Army" (Lin Biao/Tao
  Zhu's field army; source once prints the glitch 东北人民解放车 车/军). Kept INLINE (per the ch33 decision):
  白家祺 Bai Jiaqi, the interpreter trio 王智斌/齐枕平/郭子中, 李耀 Li Yao, 李长清 Li Changqing, the
  introduced officers 庞兆丰/刘文勋/张筱璞/魏钧, the Shanghai-days colleagues 毛一鹭/黄维/洪复予/周祺卿,
  尹擎宇 Yin Qingyu, Jiang Tian's Communist kin 江灏/江振寰, the Whampoa-days roster (郭大荣/赵锦文/俞镛/
  丁维经/王文翰/李靖难/卢濬泉/帅崇兴/惠济/王登梯/方鼎英/吴思豫/万力民/何焜/钟期光), 范行 Fan Xing. 华北忠义
  救国军 renders on the keyed 忠义救国军; 华北人民解放军 and 东北剿匪总司令部 (one mention each) inline. FOOTNOTED
  in B28: the Jin'ao-Yudong Bridge, the Du Fu couplet, 逐鹿/逐臭, Lin Biao's 1971 death, the 1927 Party Purge,
  the Guangzhou Uprising, the Social Affairs Department (Luo Ronghuan attribution flagged as Chen's surmise),
  the Three-Anti/Five-Anti/Suppress-Counterrevolutionaries campaigns.
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
  B26 = ch33 (第一章) DONE; B27 = ch34 (第二章, doctrinal) DONE; B28 = ch35 (第三章, narrative) DONE.**
- **NEXT: B29 = ch36** = 第四章 掌握先机 备多力分 "Chapter 4. Seizing the Initiative, Spread Too Thin" - a
  NARRATIVE chapter (intelligence value/use; a freak mischance nearly drawing Chen into an abuse-of-power
  affair; the "heart-extraction" tactic mistimed and the Bandit Chief's escape; the fighting and sacrifice
  at the Battle of Shijiazhuang). Structure CONFIRMED at B28: 1 <h2> + 4 <h3> (section heads 一、/二、/三、/四、)
  + 188 <p>, NO <h1>/<br/>/<img>/note-markers, 0 images, **drop=2**; the 4 <h3> are SEPARATE elements ->
  `standalone ### `. ⚠ COUNT DISCREPANCY: raw txt = 193 lines, so drop=2 leaves 191 body lines, but 4 <h3>
  + 188 <p> = 192 elements - a 1-line gap (an ingest-concatenated boundary OR one empty <p>) that the
  byte-exact p-by-p diff must resolve FIRST. Grep p-by-p for severed-<p> boundaries (non-terminal AND
  glitch-masked ！？》). book.json ch36 carries `sections` [ch36s01-ch36s04]. OPEN TRAP: 毛酋 (Mao +
  "chieftain," a scornful epithet for Mao Zedong) appears 2x - book.json renders it "the Bandit Chief"
  (title level); render CONSISTENTLY in body.
- After B29: B30 = ch37. Part Four = ch32-ch43; ch33-ch42 carry `sections` arrays (the 1946-49 narrative);
  ch43 = the Afterword. Working batch labels run ONE AHEAD of book.json's batches array from ch24 on
  (ch34 = B27, ch35 = B28, ch36 = B29).
- The frozen register reference is `reference/B01_frozen.md`. Prefaces denser (ch32 = 5.57);
  document/quote-heavy chapters higher (ch33 = 5.32); doctrinal higher still (ch34 = 5.19); ch35 = 5.15
  (bridge digression + essayistic reflection) - alignment/register are the gates, not the raw ratio.
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
  Stray source glyph 毛酋 (scornful epithet for Mao Zedong) is the ACTIVE B29/ch36 trap (book.json
  renders it "the Bandit Chief"; render consistently in body). The ch32 "Fifth Part" numbering discrepancy (footnoted; restated as Chen's own count in ch33).

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
