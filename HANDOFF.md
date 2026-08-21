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
Nameless Heroes B32

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once (its ONE failing regression test, "hook stands down on template stub", is a KNOWN false alarm; all others pass), then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05) through B31 (ch38) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them. PARTS ONE, TWO ("Disgrace at Hanoi") and THREE ("Renown Won in a Hundred Battles" / 百战声威) are COMPLETE; PART FOUR ("Pacification of the Beiping-Tianjin Region" / 平津地区绥靖戡乱) is OPEN - ch32 was its self-preface, ch33/ch34/ch35/ch36/ch37/ch38 the first six narrative chapters. The EPUB now holds 38/43 chapters, 335 notes. NOTE on batch numbering: book.json's batches array lumps ch23+ch24 as "B17", so the working batch labels run ONE AHEAD of the book.json array from ch24 on (ch38 = working B31 = book.json's B30 entry; ch39 = working B32 = book.json's B31 entry).

Do Batch B32 = ch39 = 第七章 瞻前顾后 未雨绸缪 "Chapter 7. Looking Before and After, Providing Against the Storm" (ONE unit; the SEVENTH Part-Four narrative chapter). NARRATIVE chapter (expect a ratio roughly in the ch33-ch38 band ~5.1-5.6, but alignment/register are the gates, not the raw ratio). ch39 carries a book.json `sections` array of THREE [ch39s01 一、清理战场中的所见所为 "1. What I Saw and Did While Clearing the Battlefield"; ch39s02 二、再三更改迄无定向的战略方针 "2. A Strategy Revised Again and Again, Still Without Direction"; ch39s03 三、一点赤心为全队前程预作安排 "3. A Loyal Heart Providing for the Whole Unit's Future"] - confirm all three title_en in book.json. Chen's Nationalist idiom stays at its sharpest (共匪/匪 "the Communist bandits", 绥靖戡乱, 匪谍/共酋/共干, 匪军/匪干/匪区) - PRESERVE it, do NOT soften; footnote where scholarship contests, text stands. Read the tail of ch38 (out/ch38_reading.md) for the batch seam (ch38 closed section 4 with the fall of Zhu Zhankui - the defector who betrayed the assault team - and the tragedy of the staff officer Gu Shoulin) and the settled Part-Four register/vocab. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch39 (40_index-split-000-0038.txt) from data/src. CONFIRM structure p-by-p against data/src_epub/OEBPS/Text/index_split_000_0038.xhtml [ch39: 1 <h2> (第七章 瞻前顾后 未雨绸缪) + 3 <h3> (the three section headings 一、/二、/三、) + 179 <p>, NO <h1>/<br/>/<img>/[\d+], 0 images - CONFIRMED at B31]. **drop=2** (running header 英雄无名-陈恭澍 + <h2> chapter title). The THREE section headings are SEPARATE <h3> ELEMENTS -> emit each as a `standalone ### ` in clean_batch.py (the ch33-ch38 method). ⚠ 1-LINE COUNT SCARE (the ch36/ch38 pattern): the raw txt has NO trailing newline, so it is 184 lines (wc -l counts 183); 184 - drop(2) = 182 body lines = 3 <h3> + 179 <p> = 182. Do the byte-exact p-by-p diff FIRST (the B19-B31 method: extract <p> inner text AND the <h3> texts in document order, walk each consuming 1 body line, assert every line matches) to PIN the 3 heading line-numbers, CONFIRM the count, and LOCATE any SEVERED-<p> boundaries (last char non-terminal -> MERGE; scan ！？》-ending lines too for glitch-MASKED severs, cf. ch33/ch35/ch36 where a stray ！ stood for a closing 」; ch37/ch38 had NONE - their ！/？-enders were all complete sentences). ALSO watch for the ch36-class SOURCE-DUPLICATION artifact (a chapter's opening printed 2-3x, a heading text fused mid-<p>); ch37/ch38 had none (the near-duplicate scan found nothing >0.6). CRITICAL: keep INNER 一、二、三 / 其一、其二 enumerations, number-ranges and name-lists as BODY lines per parity (the ch27-38 lesson: judge by function, not by the leading numeral; note ch38's four-point judgment used glitched markers 〇/2/囝/困 for （一）-（四）, all kept as body lines and rendered (1)-(4)). Extend scripts/clean_batch.py with ch39's spec (drop=2; the 3 confirmed standalone <h3> heading line-numbers, RAW 1-based; any confirmed severed-<p> merges; NO glued/glued_head unless the diff reveals one). Run it (source-conservation check must pass). Write out/ch39_reading.md (## from book.json title_en; the 3 sections as ### sub-headings from book.json section title_en; one English paragraph per source body line). Then run scripts/batch_artifacts.py ch39, and ALWAYS finish with a NO-ARG run (the trap: an ID-run writes checks.json with ONLY that unit; the no-arg run restores all 39 units so check_structure/check_content see them).
2. Translate to the FROZEN register (Chen's voice sheet in HANDOFF; the narrating "shall" is DELIBERATE, do NOT de-formalize). Consult glossary.json and authority.json BEFORE romanizing anything; REUSE the B25-B31-settled Part-Four renderings (PROGRESS.md "Settled Part-Four renderings" + the B26/B27/B28/B29/B30/B31 shelves). KEYED terms to reuse consistently in the BODY (qc enforces where keyed): 特种部队 "special-operations unit", 特种组织 "special organization"; 军统/军统局 "the Juntong"/"the Juntong Bureau"; 保密局 "the Baomiju"; 绥靖总队 "the Pacification Corps"; 总队 "Corps"/总队长 "Corps Commander"; 大队 "brigade"/大队长 "brigade commander"; 中队 "company"; 分队 "sub-brigade"; 区队 "district company"; 小组 "small group"; 骑兵班 "cavalry squad"; 直属组 "directly subordinate section"; 突击队 "assault team"/直属突击队 "directly subordinate assault team"; 第二指挥室 "Second Command Room"; 指挥室 "command room"; 指挥员 "commanding officer" vs 指挥官 "commander"; 部队长 "unit commander"; 编制 "establishment"; 配属关系 "relation of attachment"; 自衞队/自卫队 "self-defense corps"; 北平行辕 "the Beiping Field Headquarters"; 华北剿匪总司令部 "North China Bandit-Suppression Headquarters"; 绥靖 "pacification" (⚠ the KEYED noun - do NOT render as the VERB "pacify"/"pacified"; qc flags it, cf. the ch37 fix)/戡乱 "suppression of rebellion"/剿匪 "bandit-suppression"/匪谍 "Communist spies"/共酋 "Communist chieftains"/共干 "Communist cadres". KEYED PLACES/TERMS to reuse: 石家庄 Shijiazhuang, 石门 Shimen, 安次 Anci, 安国 Anguo, 正定 Zhengding, 立水桥 Lishuiqiao, 大兴 Daxing, 赵家坟 Zhaojiafen; 王庆沱 Wangqingtuo, 杨柳青 Yangliuqing, 独流 Duliu, 静海 Jinghai, 顺义 Shunyi, 唐官屯 Tangguantun; 掏心战术 "the heart-extraction tactic", 平津保三角地带 "the Beiping-Tianjin-Baoding triangle". KEYED people likely to recur: 傅作义 Fu Zuoyi, 聂荣臻 Nie Rongzhen, 李玉林 Li Yulin, 常绍曾 Chang Shaozeng, 汪鸿翥 Wang Hongzhu, 吴春祥 Wu Chunxiang, 谷守林 Gu Shoulin, 刘原深 Liu Yuanshen. Render Republican years literally (the checker matches the source numeral or auto-escapes via +1911; ordinal forms compose - but SPELLED-OUT COMPOUNDS DO NOT: write exact multi-part counts like 十万/两千/三千五百 as DIGITS 100,000 / 2,000 / 3,500, since "three thousand five hundred" composes to {3000,500} not {3500} - the B26-B31 trap). WATCH the digitization glitches (list in PROGRESS.md, render to plain sense, footnote only real reading uncertainty): same classes throughout (single-char substitutions; dropped 。 stops; dittography; mismatched guillemets ﹁﹂﹃﹄; stray ？/》/！ often standing for a closing 」; stray ︸/︴/|/〔/〕/《/⋮/≥/） glyphs; enumeration-marker glitches 工/口/闫/出/〇/囝/困 for 一/二/三/四/七; orphaned 。 at a <p> head; ○/〇/× redactions - the numeric checker mis-reads ○/〇; carry the real value in English and noise only the mis-read glyph-string; × redactions render as em-dash "——th" blanks). Dates/counts: carry real values as DIGITS/words; NOISE only idiom/approximate/name-numeral/elided/date-name/counter-by-naming/place-name-numeral forms (data/noise.txt already carries the B01-B31 rules incl. B31's 五、六万/六旬/三五一/化整为零/二门/唐二里/汤二里/一一五; add B32's). ⚠ ENUMERATION MARKERS: render list ordinals with a number the checker reads (spelled "First/Second/Third", or arabic "(1)(2)(3)"), NOT roman "(i)(ii)"; roman markers do not carry the numeral and flag as unaccounted (the ch37/ch38 fixes converted glitched markers to arabic).
3. Checks: verify_unit.py ch39 (parity + numbers with noise auto-found + anchors); check_align.py ch39; regenerate checks.json with scripts/batch_artifacts.py (no args) and run check_structure.py --config checks.json + check_content.py --config checks.json (NOTE: check_content prints KNOWN PRE-EXISTING artifacts and exits nonzero because of them - ch08 Shunde ×3, ch13 ×9, ch09 "Jize County" ×1, ch26's TWO documented keyed-substring FALSE POSITIVES 武汉卿/劳勃生路, and ch38's 海防/Haiphong HOMOGRAPH FALSE POSITIVE [海防 = "coast defense" common noun, keyed as the place Haiphong]; CONFIRM ch39 shows "all in the paired paragraph" / 0 displaced, and align any keyed name/place/TERM to its glossary-decided rendering. A NEW unit's displacements are almost always a keyed name/place/term rendered a DIFFERENT way than the glossary - align the English to the keyed form; a genuine common-noun HOMOGRAPH of a keyed place [like 海防] is a documented false positive, translation stands). Do NOT add COMMON-NOUN or book/periodical keys. qc_entities.py on a reconstructed bilingual (data/zh body lines minus the `### ` heading lines + out/ch39_en.json, `> zh` / en pairs; every glossary row needs a pinyin field - the reconstruction one-liner is in PROGRESS/the ch30-ch38 method; WATCH the keyed term rendered as a VERB not the noun, cf. 绥靖 "pacify" vs "pacification"). Verify the TAIL against the source. check_register.py --ref reference/B01_frozen.md out/ch39_reading.md ("shall" deliberate).
4. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (full list in PROGRESS.md; the big already-covered furniture incl. the Nationalist 绥靖/戡乱/共匪 framing, the Marshall Mission/Committee of Three/Executive HQ, the Lizhi Plan/Class, the Youth Army, Fu Zuoyi/Beiping's surrender, the Baomiju, Whampoa, the Marco Polo Bridge, fabi, the Republican-year system, the Transport Police Corps, the Three-Anti/Five-Anti/Suppress-Counterrevolutionaries campaigns, the Social Affairs Department, the Cultural Revolution/Red Guards, Lin Biao's 1971 death; from B29-B31: the Battle of Shijiazhuang, the recovery of Yan'an, the heart-extraction tactic, the Type 38/Type 30 rifles, the Mao epithets, the province one-char abbreviations 晋/察/冀/鲁/豫, the 三光部队 epithet, Jing Ke's Yi River song, Du Xinwu/Hongmen/Green Gang, the Four Great Dan, the chicken-feather post, the baojia system, Moxingling; and from B31: He Long/Xiao Ke, Kangda [the Anti-Japanese University], the Eighth Route Army/Eighteenth Group Army, the chuigushou, the Hanyang rifle, the 用而不疑 maxim). LIKELY new for ch39: whatever fresh material culture / institutions / place-lore the three sections raise (a battlefield-clearing / strategy / evacuation-planning chapter). Be generous but do NOT pad, do NOT re-note. Merge notes via apparatus_merge.py (positional arg: apparatus_merge.py data/ch39_apparatus.json; numeric character references only in note bodies; anchors verbatim ASCII substrings of the reading.md body text, NO em dash and NO quote/apostrophe character - substring traps; multi-occurrence anchors attach at the first; TIGHTEN a generic anchor). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field; apparatus_merge's glossary path assumes a FLAT map and would corrupt the sectioned file - use it ONLY for notes; scripts/add_ch38_glossary.py is the latest by-hand pattern, asserting each hanzi key against data/zh). For any CJK in a note body use the make_ch38_apparatus.py pattern (author bodies with typed hanzi + untoned pinyin, ASSERT every non-ASCII glyph is present in data/zh/ch39.txt, then convert to NCRs) - and remember a CORRECT glyph may be ABSENT if the source prints a glitch/variant form, so describe such terms with the source's own form + pinyin. Confirm ch39's image count (grep <img>; ch32-ch38 carried none).
5. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; update HANDOFF.md; commit and push to claude/nameless-heroes. (Next is B33 = ch40; confirm scope in book.json. Working batch labels run ONE AHEAD of book.json's batches array: book.json B32 = ch40 = working B33. Part Four = ch32-ch43; after ch42 only ch43 = the Afterword remains.)

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B33 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
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
  8 notes; 5 keyed rows. Fixed a pre-existing ch32 hyphenation displacement (CORRECTIONS).
- **Batch B29 (ch36), the FOURTH Part-Four NARRATIVE chapter.** 第四章 掌握先机 备多力分. drop=2; 1 <h2> +
  4 <h3> (section heads 一/二/三/四) + 188 <p>, byte-exact p-by-p, standalone=[18,71,108,154], ONE glitch-
  masked sever merges=[(49,50)] (由﹁地方！|转向﹁中央﹂, the ！ for 」). The "1-line count scare" was a
  trailing-newline miscount (file is 194 lines, wc -l 193; 194-2=192=4 h3+188 p). **⚠ MAJOR SOURCE
  DUPLICATION:** the intelligence-timeliness preamble is printed 3× (z2-16, z18-32, z33-37), the Anguo raid
  + contributor intros 2×, and z33 fuses the section-1 heading text mid-<p> — a digital-source artifact,
  translated in FULL per rule 4 with a footnote at the head of section 1. 187 body paragraphs; median ratio
  5.42. 8 notes (319 cumulative); 13 net-new keyed rows. check_content 0 displaced; qc 0 misses.
- **Batch B30 (ch37), the FIFTH Part-Four NARRATIVE chapter.** 第五章 兵连祸结 民不聊生 "War Unending, the
  People Destitute" — the fall of Shimen (Lu Deming's account), the North-Suburb Group welcomed while the
  West-Suburb Group was shunned by the North China Bandit-Suppression HQ, and Tian Yingjie's first-person
  account of the Oct-1948 night battle of Lishuiqiao. drop=2; 1 <h2> + 3 <h3> (section heads 一/二/三) +
  144 <p>, byte-exact p-by-p, standalone=[11,43,90], NO severs (the two ！-enders L79/L91 are complete
  sentences with orphaned/glitch punctuation, not mid-predicate severs), NO source-duplication. 144 body
  paragraphs; median ratio 5.50 (document/quote-heavy: two long contributed accounts + an embedded doggerel
  song). 8 notes (327 cumulative); 12 net-new keyed rows (9 people, 3 places). check_content 0 displaced;
  qc 0 misses (fixed 2 verb-form 绥靖 renderings to the keyed noun "pacification"); register within
  tolerance. qa_epub PASS; epubcheck 0/0/0/0. 7 noise additions (二十多, 二流子,
  一两百, 八达岭, 万寿山, 二〇八, 两淡). Detail in PROGRESS.md ("Batch B30").
- **Batch B31 (ch38), the SIXTH Part-Four NARRATIVE chapter.** 第六章 曲直分明 反复无常 "Right and Wrong
  Made Plain, yet Ever Fickle" — the case of the defector Zhu Zhankui (朱占奎), made a district
  commissioner and major-general security commander, who worked with Chen's assault team through 1948
  and then lured the Second Command Room and assault team into a "widened guerrilla front" trap and
  defected back to the Communists; built on three contributed accounts by the assault team's three
  commanders (Wang Hongzhu / Chang Shaozeng / Wu Chunxiang) plus Wang Zhiyi's "Story of Zhu Zhankui",
  and closing with the Hong Kong tragedy of the staff officer Gu Shoulin. drop=2; 1 <h2> + 4 <h3>
  (section heads 一/二/三/四) + 135 <p>, byte-exact p-by-p, standalone=[15,46,69,113], NO severs (the
  ！/？-enders L48/L106 are complete terminal sentences), NO source-duplication. 135 body paragraphs;
  median ratio 5.55 (document/quote-heavy: four contributed accounts). 8 notes (335 cumulative); 10
  net-new keyed rows (4 people, 6 places). check_content 1 "displaced" = the DOCUMENTED 海防/Haiphong
  HOMOGRAPH FALSE POSITIVE (海防 here = "coast defense" common noun, correctly rendered); qc 0 real
  misses (绥靖 x8 rendered the noun "pacification", no verb drift); register within tolerance. qa_epub
  PASS; epubcheck 0/0/0/0. **EPUB now 38/43 chapters, 335 notes.** 8 noise additions (五、六万, 六旬,
  三五一, 化整为零, 二门, 唐二里/汤二里, 一一五). Detail in PROGRESS.md ("Batch B31").

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` - derives data/zh/<id>.txt verbatim from data/src, applying per-unit
  drops/merges/heading-splits with a source-conservation check. Specs for ch01-ch37. Merge logic
  FOLLOWS CHAINS. **drop is variable:** most chapters drop=2; ch01/ch10/ch20/ch32 drop=3 (a part
  super-title precedes the preface). `standalone` = a sub-heading kept as its own line with no
  heading markup, emitted as `### ` (used for both plain-<p> sub-heads AND separate <h3> section
  elements, cf. ch33-ch37's <h3> section heads); `glued` = a heading fused onto a paragraph's
  TAIL; `glued_head` = a heading fused onto a paragraph's HEAD; `merges` = source <p> pairs that
  sever one sentence OR an intra-<p> `<br/>` line break, AND can be MASKED by a glitch (scan
  ！？》-ending lines, not just non-terminal ones - ch33 L19/20, ch35 L25/26 & L136/137, ch36 L49/50;
  BUT ch37's ！-enders were all complete sentences, NOT severs). **A chapter can carry INNER enumerated
  一、二、三 / 第一、第二 DOCUMENT-CLAUSE or NUMBER-RANGE or NAME-LIST content that is NOT a section
  heading - keep those as ordinary body lines per parity, judged by function** (ch27-37; ch37's Lu
  Deming document nested 一/二/三/四 top-items over 工/口/闫/出-glitched sub-items, all body lines).
  **⚠ ch36 taught a SOURCE-DUPLICATION class (a chapter's opening printed 2-3x, a section-heading text
  fused mid-<p>). Preserve it all per rule 4; footnote it. ch37 had none.**
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
  renders `<p class="verse">`; the checks strip it. (ch37's embedded doggerel song was rendered as
  prose paragraphs per parity, NOT with {p}, since the source runs it as running <p> text.)
- Glossary is authored/merged BY HAND into the SECTIONED file (book/people/organizations/places/
  terms), a dict keyed by hanzi, idempotent + re-read-verified. **Every row MUST carry a `pinyin`
  field** - qc_entities does `rec["pinyin"]` and KeyErrors otherwise. `scripts/add_ch37_glossary.py`
  is the latest by-hand pattern: covers people/places sections in one pass, asserts each hanzi key
  is a substring of that unit's data/zh/<id>.txt. apparatus_merge's glossary path assumes a FLAT map
  and would corrupt the sectioned file; NOTES still go through apparatus_merge.py (positional arg).
- **qc_entities catches term-rendering drift too:** a glossary common-noun/term rendered a
  different way (or as a VERB not the noun) flags as a "miss." Align the English to the glossary
  (B26/B30: 绥靖 keyed "pacification" flagged when rendered the verb "pacify"/"pacified"). qc has a
  first/last-word fallback, so a keyed en that starts with "the" is trivially satisfied - prefer
  distinctive en.
- **GLOSSARY-KEY DISCIPLINE:** a key must be a DISTINCTIVE proper noun (or a distinctive institution)
  that renders ONE way everywhere. Periodicals and books are FOOTNOTES/inline. One-off transliterated
  Western/Japanese officer names, one-off telegram/roster/memoir names, standard province names, and
  attested Shanghai ROADS are inline. A bare surname whose full name is unknown is rendered inline.
  NEVER key hanzi that is a substring of a different keyed rendering. (A name inline in one chapter can
  GRADUATE to a key when it becomes central: 常绍曾 was inline in ch36, keyed in ch37.)
- **Note-anchor gotchas:** anchors must be ASCII, WITHOUT any quote/apostrophe character AND
  without an em dash (U+2014) - all substring traps. The reading.md uses curly quotes and em
  dashes freely, so pick an anchor phrase with none of them. **Multi-occurrence anchors attach at
  the FIRST occurrence** - if a short generic anchor would match an EARLIER paragraph, LENGTHEN it.
- **make_ch37_apparatus.py pattern (scripts/):** author note bodies as plain ASCII + typed hanzi +
  UNTONED pinyin + straight quotes, allow em-dash, ASSERT every non-ASCII glyph occurs in THAT UNIT's
  data/zh/<id>.txt, then convert every non-ASCII char to a numeric char ref and run apparatus_merge.py.
  **A CORRECT glyph may be ABSENT if the source prints a glitch/variant** - describe such terms with
  the source's own form + pinyin/English. A note that quotes ANOTHER unit's text is authored
  ENGLISH-ONLY to avoid the cross-unit glyph-assert. AVOID tone-marked pinyin and curly quotes.
- **⚠ ENUMERATION MARKERS carry a numeral the checker reads.** Render list ordinals as spelled
  ordinals ("First/Second/Third", cf. ch34) or arabic "(1)(2)(3)", NOT roman "(i)(ii)(iii)": roman
  markers do not carry the value and flag as unaccounted numbers (the B30/ch37 fix converted the
  sub-item markers (i)-(viii) to (1)-(8); the checker is source->target only, so glitch-marked items
  with no source numeral rendered as arabic are safe/target-only).
- data/noise.txt carries the B01-B30 project noise rules (each with a comment line). Republican
  years render literally; the checker matches the source numeral (or auto-escapes Republican-year
  N via N+1911). **SPELLED-OUT COMPOUNDS DO NOT COMPOSE** (target "three thousand five hundred" =
  {3000,500}, not 3500): write exact multi-part counts as DIGITS (3,500 / 120 / 3,200,000). **ORDER
  MATTERS in noise.txt:** a longer numeral idiom must precede a shorter one that is its prefix, or the
  shorter consumes it and orphans a digit (B29: 十余万 had to precede the bare 十余). Name-numeral
  glyphs, idiom numerals (incl. 两 = "both" in 名利两淡), approximate ranges, place-name numerals
  (八达岭/万寿山), and counter-by-naming forms are noised. The ○ (U+25CB) and 〇 (U+3007)
  address/redaction/code artifacts: the checker cannot read them as digits - noise the mis-read
  glyph-string (二〇八, 〇七六〇), carry the real value in English. × (source redaction) renders as
  an em-dash blank.
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
  mission". 华北忠义救国军 "the North China Loyal and Patriotic Army" (built on the keyed 忠义救国军);
  滦榆游击总司令部 "the Luan-Yu Guerrilla General Headquarters".
- **B29 PART-FOUR vocab (ch36; reuse):** 掏心战术 "the heart-extraction tactic" (KEYED term); 平津保三角地带
  "the Beiping-Tianjin-Baoding triangle" (KEYED term/place); 暂编第三军/暂三军 "the Provisional Third Army";
  联合肃奸组 "the Joint Traitor-Rooting Group"; 任务编组 "task-detachment"; 三通 "the three connections";
  三八式/三〇式 "the Type 38"/"Type 30" rifles; 弄权 "abuse of power"; 匪酋 "bandit chieftains" / 匪军 "the
  bandit army/forces" / 匪干 "bandit cadres" / 匪区 "bandit-held territory". The Mao epithets: 毛酋 "the
  bandit chief Mao", 毛贼泽东 "the bandit Mao Zedong", 毛某 "the man Mao"/"Mao".
- **B30 PART-FOUR vocab (ch37; reuse):** 北郊混合组 "the North-Suburb Mixed Group" / 西郊混合组 "the
  West-Suburb Mixed Group" / 北郊组 "the North-Suburb Group" (descriptive unit names, rendered
  consistently but NOT keyed); 情报小组 "intelligence squad"; 自衞队/自卫队 "self-defense corps";
  三光部队 "the Strip-It-Clean Force" (noted; the 三光 pun); 灰色地带 "gray zone"; 三不管地区 "district
  of the three unmanaged"; 保甲/保公所 "baojia" / "baojia office" (noted); 复兴社 "the Renaissance
  Society"; 洪门 "the Hongmen" / 青帮 "the Green Gang" / 龙头 "dragon head" / 大字辈 "Da-character
  generation" (noted). 华北剿总 = "the North China Bandit-Suppression Headquarters" (the keyed
  华北剿匪总司令部). The 0760 unit code and the 208th Division carried as digits.
- **B31 PART-FOUR vocab (ch38; reuse):** the assault-team internal hierarchy — 突击队 "assault team" /
  直属突击队 "directly subordinate assault team"; 区队 "district company" / 区队长 "district-company
  commander"; 分队 "sub-brigade"; 小组 "small group" / 小组长 "group leader"; 骑兵班 "cavalry squad" /
  骑兵组 "cavalry group". 第二指挥室 "Second Command Room"; 自衞队/自卫队 "self-defense corps"; 打情报
  "beating out intelligence" (Chen's own jargon for capturing enemy documents); 扩大游击面 "widening the
  guerrilla front" (Zhu's betrayal pretext); 用而不疑、疑而不用 "employ a man and doubt him not..."; 泱泱
  大度 "the grand bearing of a great state". 抗日军政大学/抗大 "the Anti-Japanese University"/"Kangda";
  八路军/第十八集团军 "the Eighth Route Army"/"the Eighteenth Group Army".
- **PLACE-NAME CONVENTION (the qc gate enforces the glossary's PINYIN for keyed cities/places):**
  北平 Beiping, 天津 Tianjin. KEYED (B29): 石家庄 Shijiazhuang, 石门 Shimen, 安次 Anci, 安国 Anguo,
  正定 Zhengding. KEYED (B30): 立水桥 Lishuiqiao, 大兴 Daxing, 赵家坟 Zhaojiafen. KEYED (B31): 王庆沱
  Wangqingtuo, 杨柳青 Yangliuqing, 独流 Duliu, 静海 Jinghai, 顺义 Shunyi, 唐官屯 Tangguantun. KEYED gates 安定门
  Andingmen, 西直门 Xizhimen; 东直门 Dongzhimen INLINE. KEYED 冀东 "East Hebei". Standard provinces
  render inline in pinyin (河北 Hebei NOT keyed, 山西 Shanxi, 山东 Shandong, 河南 Henan, 陕西 Shaanxi,
  绥远 Suiyuan, 察哈尔 Chahar). 冀中 "Central Hebei", 冀南 "South Hebei"; 晋察冀 "Jin-Cha-Ji", 晋冀鲁豫
  "Jin-Ji-Lu-Yu" (the one-char province abbreviations noted at ch37). Rail lines by dashed pinyin
  (Ping-Han, Zheng-Tai, Bei-Ning, Ping-Sui, Ping-Bao, De-Shi, Jin-Pu, Long-Hai). 五台山 the Wutai
  Mountains, 太行山 the Taihang Mountains, 太岳 the Taiyue, 延安 Yan'an, 万寿山 Wanshou Hill, 十三陵 the
  Ming Tombs, 八达岭 Badaling, 西山 the Western Hills - all INLINE.
- **Book / part titles (in-text; DECIDED; reuse verbatim):** 英雄无名 = "Nameless Heroes"; Part One
  北国锄奸 = "Rooting Out Traitors in the North"; Part Two = "Disgrace at Hanoi"; Part Three 百战声威
  = "Renown Won in a Hundred Battles"; Part Four 平津地区绥靖戡乱 = "Pacification of the Beiping-Tianjin
  Region". 忠义救国军 = "the Loyal and Patriotic Army".
- **B25 shelf (ch32; keyed):** 叶剑英 Ye Jianying, 刘培初 Liu Peichu, 李宗仁 Li Zongren, 傅作义 Fu Zuoyi,
  计兆祥 Ji Zhaoxiang; orgs 绥靖总队, 军事调处执行部, 军事三人小组, 励志训练班; term 励志计划.
- **B26 shelf (ch33; keyed):** people 李玉林 Li Yulin, 罗敬 Luo Jing, 侯腾 Hou Teng, 吴安之 Wu Anzhi,
  马汉三 Ma Hansan, 张家铨 Zhang Jiaquan, 史泓 Shi Hong, 陈诚 Chen Cheng; orgs 保密局, 人民服务总队;
  terms 特种部队, 特种组织. 刘原深 Liu Yuanshen; 郑恩普 Zheng Enpu keyed earlier.
- **B27 shelf (ch34; keyed):** orgs 交警总队 "Transport Police Corps", 华北剿匪总司令部 "North China
  Bandit-Suppression Headquarters"; person 聂恩俊 Nie Enjun (provisional).
- **B28 shelf (ch35; keyed):** people 李鸣秋 Li Mingqiu, 李运昌 Li Yunchang, 罗荣桓 Luo Ronghuan, 黄郛
  Huang Fu; org 东北人民解放军 "the Northeast People's Liberation Army".
- **B29 shelf (ch36; keyed):** people 安春山 An Chunshan, 朱占奎 Zhu Zhankui, 刘玉珠 Liu Yuzhu, 萧润宇
  Xiao Runyu, 牛广金 Niu Guangjin, 吕正操 Lü Zhengcao (attested); places 石家庄/石门/安次/安国/正定; terms
  掏心战术, 平津保三角地带.
- **B30 shelf (ch37; keyed):** people 常绍曾 Chang Shaozeng (North-Suburb Group leader, three quoted
  accounts; graduated from inline in ch36), 田英杰 Tian Yingjie (the Lishuiqiao "Captain Tian"), 卢德明
  Lu Deming (Shimen account author), 刘子元 Liu Ziyuan (Daxing self-defense brigade cmdr), 冯玉柱 Feng
  Yuzhu (successor North-Suburb leader), 王抚洲 Wang Fuzhou (Third-Route-Army manager, later Taiwan
  vice-minister), 白家祺 Bai Jiaqi (Lt Col, the Guohun-song author), 杜心吾 Du Xinwu (Cili martial-arts
  master; source spells 心吾 for 心五), 程艳秋 Cheng Yanqiu (the opera dan; also 程砚秋) - all provisional;
  places 立水桥 Lishuiqiao, 大兴 Daxing, 赵家坟 Zhaojiafen (decided). Kept INLINE (glossary-key discipline):
  the Shimen defenders 罗历戎/李文定/刘英/刘清池/赵劲军/侯子固; the Communist figures 杨得志/杨成武/刘伯承/
  杨秀峰/薄一波/黄敬(俞启威); the training roster 钱致伦/王忠/尹东耕/阎尚新; the Ninth-Route staff 齐庆斌/
  张克新/陈肇基/骆永康; the Lishuiqiao-night names 米仁甫/马良知/李志达/路焕仲, the grooms 庄飞/杨天铎/张岳生,
  王镇吾, 白世维.
- **B31 shelf (ch38; keyed):** people 汪鸿翥 Wang Hongzhu (first assault-team cmdr, section-2 account
  author), 吴春祥 Wu Chunxiang (third assault-team cmdr, section-4 account author), 谷守林 Gu Shoulin
  (Second-Command-Room staff officer, the Hong Kong tragedy) — all provisional; 萧克 Xiao Ke (attested,
  He Long's 120th-Division deputy); places 王庆沱 Wangqingtuo, 杨柳青 Yangliuqing, 独流 Duliu, 静海
  Jinghai, 顺义 Shunyi, 唐官屯 Tangguantun (decided). Kept INLINE (glossary-key discipline): 王志毅/董英/
  任卓宣/徐佛观/张鲁颖/李长清/徐立德/杨士毅/窦玉麟/张保权/贾叔铭/赵濶亭/李葆章(=李保章)/张侗夫/陈俊祥/任德勤/
  赵子侠/王维宁/吴玉林/刘纯熙/张麟阁/马钟麟/孙守义/刘楚枫/张培植/汪鸿骏(≠汪鸿翥)/刘伯承/中野; the villages
  五重山/白房村/牛栏山/赵家寨子/王家庄子/青王庄/唐二里(=汤二里)/昌平/永清/固安/沧县/德县/德州/清河镇/南苑/
  喜峰口/都山/明孝陵. Name-form variants (same referent, inline): 朱占奎/朱占魁, 李葆章/李保章, 唐二里/汤二里.
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
- **Contributed accounts.** Part Four quotes long first-person memoir-accounts by comrades (ch36's
  Xiao Runyu / Niu Guangjin; ch37's Lu Deming, Chang Shaozeng, Tian Yingjie). Keep these in a plain,
  vivid first person DISTINCT from Chen's own essayistic frame; Chen's inserted 笔者附注 (writer's notes)
  return to his grave register. ch37's Tian Yingjie Lishuiqiao narrative is the most vivid: fast, tense,
  concrete battle prose.
- Ratio ~4.55-4.78 en/han in NARRATIVE; prefaces denser (ch32 5.57); DOCUMENT/QUOTE-HEAVY chapters
  run higher (ch33 5.32, ch34 5.19, ch35 5.15, ch36 5.42, ch37 5.50, ch38 5.55). Read the note, do
  not reset. Alignment/register are the gates, not the raw ratio.

## Voice sheets - principal & recurring cast (Part Four)

- **CHEN GONGSHU himself.** Commands the First Brigade of the Pacification Corps in the Beiping-Tianjin
  region, 1946-49; also (against his will) leader of the Baomiju's Beiping directly subordinate section.
- **ZHENG JIEMIN (郑介民 / Mr. Zheng).** Chen's old Beiping-days superior; Chief of the Second Bureau of
  the Ministry of National Defense, government rep on the Executive Headquarters, head of the Lizhi Class.
- **LIU PEICHU (刘培初).** Corps Commander of the Pacification Corps; ascetic, hard-driving.
- **THE THREE FIRST-BRIGADE PILLARS (ch33 s4):** LI YULIN (李玉林, deputy cmdr, "Fifth Brother"), LUO
  JING (罗敬, political director), LIU YUANSHEN (刘原深, chief secretary).
- **MAO RENFENG (毛人凤 / Mr. Mao).** Head of the Baomiju; imposed the Beiping directly subordinate section.
- **THE FIELD MEN (B30):** CHANG SHAOZENG (常绍曾, North-/West-Suburb Group leader, once Chen's pupil),
  TIAN YINGJIE (田英杰, "Captain Tian" of Lishuiqiao), FENG YUZHU (冯玉柱, Chang's successor), LIU ZIYUAN
  (刘子元, Daxing self-defense brigade cmdr).

## ⚠ Name trap RESOLVED (do not reopen): 陈邦国 / 郑邦国

The Hanoi action-team member the source spells 郑邦国 in ch13 and 陈邦国 in ch15/ch16/ch17 is ONE
man. RESOLVED to **Chen Bangguo (陈邦国)**. Use Chen Bangguo consistently.

## Where the book stands

- Part One (北国锄奸) COMPLETE (B01-B05). Part Two ("Disgrace at Hanoi") COMPLETE (B06-B13). Part
  Three ("Renown Won in a Hundred Battles" / 百战声威) COMPLETE (B14-B24).
- **Part Four ("Pacification of the Beiping-Tianjin Region") OPEN: B25 = ch32 (self-preface) DONE;
  B26 = ch33 (第一章) DONE; B27 = ch34 (第二章, doctrinal) DONE; B28 = ch35 (第三章, narrative) DONE;
  B29 = ch36 (第四章, narrative) DONE; B30 = ch37 (第五章, narrative) DONE; B31 = ch38 (第六章,
  narrative) DONE.**
- **NEXT: B32 = ch39** = 第七章 瞻前顾后 未雨绸缪 "Chapter 7. Looking Before and After, Providing Against
  the Storm" - a NARRATIVE chapter, THREE sections (ch39s01-ch39s03). Structure CONFIRMED at B31: 1
  <h2> + 3 <h3> (section heads 一/二/三) + 179 <p>, NO <h1>/<br/>/<img>/note-markers, 0 images,
  **drop=2**; the 3 <h3> are SEPARATE elements -> `standalone ### `. ⚠ 1-line count scare (ch36/ch38
  pattern): raw txt = 184 lines (no trailing newline; wc -l 183); 184 - 2 = 182 = 3 <h3> + 179 <p>.
  src 40_index-split-000-0038.txt. Grep p-by-p for severed-<p> boundaries (non-terminal AND
  glitch-masked ！？》) AND for a ch36-class source-duplication run.
- After B32: B33 = ch40. Part Four = ch32-ch43; ch33-ch42 carry `sections` arrays (the 1946-49
  narrative); ch43 = the Afterword. Working batch labels run ONE AHEAD of book.json's batches array
  from ch24 on (ch38 = B31, ch39 = B32, ch40 = B33).
- The frozen register reference is `reference/B01_frozen.md`. Prefaces denser (ch32 = 5.57);
  document/quote-heavy chapters higher (ch33 = 5.32, ch34 = 5.19, ch35 = 5.15, ch36 = 5.42, ch37 =
  5.50, ch38 = 5.55) - alignment/register are the gates, not the raw ratio.
- Sub-heading pattern: Part Four chapters ch33-ch42 carry book.json `sections` arrays; the section
  headings appear in the source as SEPARATE <h3> ELEMENTS that emit as `standalone ### `. DISTINGUISH
  enumerated LIST items / document clauses / number-ranges / name-lists (kept as body lines per parity)
  from the true section headings. Grep each new chapter p-by-p.
- WATCH for source anomalies: cuts, misplaced-「 glitches, corrupt/dropped-character phrases, dropped
  full stops, a STRAY glyph fused onto a title, stray ？/》/！ (often standing for a closing 」), the
  ○ (U+25CB) / 〇 (U+3007) and × redactions, name glitches, variant forms, pervasive single-character
  substitutions, enumeration-marker glitches (工/口/闫/出 for 一/二/三/七), orphaned 。 at a <p> head,
  severed-<p> boundaries (MERGE; can be glitch-MASKED), AND the ch36-class SOURCE DUPLICATION.
  Re-grep each batch's source for `\[\d+\]` note markers (none through B30).

## Open items for the read-through / completion

- Feed decided renderings back to authority.json on completion: 军统 "the Juntong"; 保密局 "the Baomiju";
  the full B02-B30 historical-name set; the Part-Four vocabulary (绥靖/戡乱/绥靖总队/励志计划/特种部队/
  特种组织/掏心战术/平津保三角地带 etc.).
- Japanese name readings to firm up when the men recur.
- Provisional romanizations to firm up (glossary `provisional` rows, incl. the B30 people 常绍曾/田英杰/
  卢德明/刘子元/冯玉柱/王抚洲/白家祺/杜心吾/程艳秋; the B29 people 安春山/朱占奎/刘玉珠/萧润宇/牛广金; the
  B26 people 李玉林/罗敬/侯腾/吴安之/马汉三/张家铨/史泓; 刘培初/计兆祥).
- Whole-book reconciliation items: ch09 "Jize County" (the 鸡泽县 key); the pinyin-vs-postal city names;
  the two B20 keyed-substring false positives (武汉卿 / 劳勃生路). The Malone spelling (ch30, footnoted).
  The ch32 "Fifth Part" numbering discrepancy (footnoted). The garbled deputy-chief-of-staff surname
  glyph 鿄 (ch36, rendered "—— Shuzai"). The Mao-at-Anguo intelligence footnoted as a scholarship
  verdict (ch36). 杜心吾/杜心五 and 程艳秋/程砚秋 name-form variants (ch37, both noted/keyed).

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01-B30 builds (0/0/0/0). Source is a clean digital
  EPUB, predominantly simplified with residual variant glyphs and pervasive digitization glitches
  (list them, render to plain sense, do not footnote mechanical typos). B01-B30 glitch lists in
  PROGRESS.md. **ch36 added a SOURCE-DUPLICATION class (opening printed 2-3x) - watch for it; ch37 had none.**
- Running-header line 英雄无名-陈恭澍 opens all 43 content files: drop it. drop count is variable -
  most drop=2; ch01/ch10/ch20/ch32 drop=3.
- Enumerated ；/：/、 bullet lists, quoted-document/directive/roster lines (INCLUDING intra-<p>
  `<br/>` TABLE rows and INNER document-clause / range / name-list / 第一、第二 lists), salutations,
  verse lines, run-in section labels, and 『』/「」-closed dialogue are DELIBERATE separate lines
  - do NOT merge them; only genuine mid-phrase splits (last char not terminal, OR a source <p>
  boundary that severs one sentence - possibly MASKED by a glitch ！/？/》 for 」, OR an intra-<p>
  `<br/>` inside PROSE) merge, and those can CHAIN. (ch37 had NO merges: its ！-enders were complete.)
- Faithful numbering gaps/anomalies (NOT errors): Part Three skips 第七章 (ch27 = 第八章); 第十章 splits
  into (上)/(下) (ch29/ch30); 三面受敌 一往无前 titles two chapters; ch32 numbers the Beiping-Tianjin
  volume "the Fifth Part" though Shanghai was "the Third Part" (footnoted). Preserve and footnote.
- Expect a stray per-task branch at the top of every batch; consolidate onto claude/nameless-heroes
  per rule 2.
