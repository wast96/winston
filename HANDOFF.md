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
Nameless Heroes B33

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once (its ONE failing regression test, "hook stands down on template stub", is a KNOWN false alarm; all others pass), then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05) through B32 (ch39) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them. PARTS ONE, TWO ("Disgrace at Hanoi") and THREE ("Renown Won in a Hundred Battles" / 百战声威) are COMPLETE; PART FOUR ("Pacification of the Beiping-Tianjin Region" / 平津地区绥靖戡乱) is OPEN - ch32 was its self-preface, ch33/ch34/ch35/ch36/ch37/ch38/ch39 the first seven narrative chapters. The EPUB now holds 39/43 chapters, 343 notes. NOTE on batch numbering: book.json's batches array lumps ch23+ch24 as "B17", so the working batch labels run ONE AHEAD of the book.json array from ch24 on (ch39 = working B32 = book.json's B31 entry; ch40 = working B33 = book.json's B32 entry).

Do Batch B33 = ch40 = 第八章 抚今追昔 烟波千里 "Chapter 8. Musing on Past and Present, Mist over a Thousand Miles" (ONE unit; the EIGHTH Part-Four narrative chapter). NARRATIVE chapter (expect a ratio roughly in the ch33-ch39 band ~5.1-5.6, but alignment/register are the gates, not the raw ratio). ch40 carries a book.json `sections` array of FOUR [ch40s01 一、三人同步各行各事走上了三条路 "1. Three Men in Step, Each His Own Way, onto Three Roads"; ch40s02 二、华北战场为人所忽视的头号大敌 "2. The Overlooked Arch-Enemy of the North China Front"; ch40s03 三、但愿你们坚苦刻励永远活在那里 "3. May You, Steadfast and Striving, Live On There Forever"; ch40s04 四、每一仗败阵都输得心有未甘 "4. Every Defeat Lost with Unyielding Regret"] - confirm all four title_en in book.json. Chen's Nationalist idiom stays at its sharpest (共匪/匪 "the Communist bandits", 绥靖戡乱, 匪谍/共酋/共干, 匪军/匪干/匪区) - PRESERVE it, do NOT soften; footnote where scholarship contests, text stands. Read the tail of ch39 (out/ch39_reading.md) for the batch seam (ch39 closed section 3 with the plan to move the First Brigade south: Zheng Jiemin's charge to prepare the "stay-behind work", Li Yulin's Sept-1948 trip to Nanjing with the plan outline and the request to transfer the brigade south, and the drawing-in of the remote field units) and the settled Part-Four register/vocab. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate):
1. Read ch40 (41_index-split-000-0039.txt) from data/src. CONFIRM structure p-by-p against data/src_epub/OEBPS/Text/index_split_000_0039.xhtml [ch40: 1 <h2> (第八章 抚今追昔 烟波千里) + 4 <h3> (the four section headings 一、/二、/三、/四、) + 170 <p>, NO <h1>/<br/>/<img>/[\d+], 0 images - CONFIRMED at B32]. **drop=2** (running header 英雄无名-陈恭澍 + <h2> chapter title). The FOUR section headings are SEPARATE <h3> ELEMENTS -> emit each as a `standalone ### ` in clean_batch.py (the ch33-ch39 method). ⚠ 1-LINE COUNT SCARE (the ch36/ch38/ch39 pattern): the raw txt has NO trailing newline, so it is 176 lines (wc -l counts 175); 176 - drop(2) = 174 body lines = 4 <h3> + 170 <p> = 174. Do the byte-exact p-by-p diff FIRST (the B19-B32 method: extract <p> inner text AND the <h3> texts in document order, walk each consuming 1 body line, assert every line matches) to PIN the 4 heading line-numbers, CONFIRM the count, and LOCATE any SEVERED-<p> boundaries (last char non-terminal -> MERGE; scan ！？》-ending lines too for glitch-MASKED severs, cf. ch33/ch35/ch36 where a stray ！ stood for a closing 」; ch37/ch38/ch39 had NONE - their ！/？-enders were all complete sentences). ALSO watch for the ch36-class SOURCE-DUPLICATION artifact (a chapter's opening printed 2-3x, a heading text fused mid-<p>); ch37/ch38/ch39 had none (the near-duplicate scan found nothing >0.6). CRITICAL: keep INNER 一、二、三 / 其一、其二 enumerations, number-ranges and name-lists as BODY lines per parity (the ch27-39 lesson: judge by function, not by the leading numeral; note ch39's option-list used the glitched marker 凵 for 一, kept as body lines and rendered (1)-(3)). Extend scripts/clean_batch.py with ch40's spec (drop=2; the 4 confirmed standalone <h3> heading line-numbers, RAW 1-based; any confirmed severed-<p> merges; NO glued/glued_head unless the diff reveals one). Run it (source-conservation check must pass). Write out/ch40_reading.md (## from book.json title_en; the 4 sections as ### sub-headings from book.json section title_en; one English paragraph per source body line). Then run scripts/batch_artifacts.py ch40, and ALWAYS finish with a NO-ARG run (the trap: an ID-run writes checks.json with ONLY that unit; the no-arg run restores all 40 units so check_structure/check_content see them).
2. Translate to the FROZEN register (Chen's voice sheet in HANDOFF; the narrating "shall" is DELIBERATE, do NOT de-formalize). Consult glossary.json and authority.json BEFORE romanizing anything; REUSE the B25-B32-settled Part-Four renderings (PROGRESS.md "Settled Part-Four renderings" + the B26/B27/B28/B29/B30/B31/B32 shelves). KEYED terms to reuse consistently in the BODY (qc enforces where keyed): 特种部队 "special-operations unit", 特种组织 "special organization"; 军统/军统局 "the Juntong"/"the Juntong Bureau"; 保密局 "the Baomiju"; 绥靖总队 "the Pacification Corps"; 总队 "Corps"/总队长 "Corps Commander"; 大队 "brigade"/大队长 "brigade commander"; 中队 "company"; 分队 "sub-brigade"; 区队 "district company"; 小组 "small group"; 直属组 "directly subordinate section"; 突击队 "assault team"; 第二指挥室 "Second Command Room"; 指挥室 "command room"; 指挥员 "commanding officer" vs 指挥官 "commander"; 部队长 "unit commander"; 编制 "establishment"; 配属关系 "relation of attachment"; 自衞队/自卫队 "self-defense corps"; 北平行辕 "the Beiping Field Headquarters"; 华北剿匪总司令部 "North China Bandit-Suppression Headquarters" (华北剿总 = "the North China Bandit-Suppression Headquarters"); 绥靖 "pacification" (⚠ the KEYED noun - do NOT render as the VERB "pacify"/"pacified"; qc flags it, cf. the ch37/ch39 fixes)/戡乱 "suppression of rebellion"/剿匪 "bandit-suppression"/匪谍 "Communist spies"/共酋 "Communist chieftains"/共干 "Communist cadres"; 留置工作 "stay-behind work". KEYED PLACES/PEOPLE likely to recur (qc enforces the glossary PINYIN/rendering): 傅作义 Fu Zuoyi, 聂荣臻 Nie Rongzhen, 林彪 Lin Biao, 郑介民 Zheng Jiemin, 李玉林 Li Yulin, 刘培初 Liu Peichu, 陈振山 Chen Zhenshan, 王兆芬 Wang Zhaofen, 张鲁颖 Zhang Luying, 孙兰峰 Sun Lanfeng, 郭景云 Guo Jingyun, 鲁英庆 Lu Yingqing (source glitches 鲁英尘/鲁英屡); 石家庄 Shijiazhuang, 涿县 Zhuoxian, 涞水 Laishui, 保定 Baoding, 新保安 Xinbao'an (glossary en carries a CURLY apostrophe "Xinbao’an" to match reading.md typography), 张家口 Zhangjiakou, 塘沽 Tanggu. ⚠ 张垣 = the literary name of Zhangjiakou is rendered "Zhangyuan" INLINE (NOT keyed - ch08 renders the same 张垣 as "Zhangjiakou"; a whole-book reconciliation item). Render Republican years literally (the checker matches the source numeral or auto-escapes via +1911; ordinal forms compose - but SPELLED-OUT COMPOUNDS DO NOT: write exact multi-part counts like 十万/两千/三千五百 as DIGITS 100,000 / 2,000 / 3,500, since "three thousand five hundred" composes to {3000,500} not {3500} - the B26-B32 trap). WATCH the digitization glitches (list in PROGRESS.md, render to plain sense, footnote only real reading uncertainty): same classes throughout (single-char/name substitutions incl. glitched surnames; dropped 。 stops; dittography; mismatched guillemets ﹁﹂﹃﹄; stray ？/》/！ often standing for a closing 」; stray ︸/︴/|/〔/〕/《/⋮/≥/）/〞/" glyphs; enumeration-marker glitches 工/口/闫/出/〇/囝/困/凵 for 一/二/三/四/七; orphaned 。 at a <p> head; ○/〇/× redactions - the numeric checker mis-reads ○/〇; carry the real value in English and noise only the mis-read glyph-string; × redactions render as em-dash "——th" blanks). Dates/counts: carry real values as DIGITS/words; NOISE only idiom/approximate/name-numeral/elided/date-name/counter-by-naming/place-name-numeral forms (data/noise.txt already carries the B01-B32 rules incl. B32's 六神无主/赵百川/崔万兴/一来二去/顚三倒四/三心两意/数九寒天; add B33's). ⚠ ENUMERATION MARKERS: render list ordinals with a number the checker reads (spelled "First/Second/Third", or arabic "(1)(2)(3)"), NOT roman "(i)(ii)"; roman markers do not carry the numeral and flag as unaccounted (the ch37/ch38/ch39 fixes rendered glitched markers as arabic).
3. Checks: verify_unit.py ch40 (parity + numbers with noise auto-found + anchors); check_align.py ch40; regenerate checks.json with scripts/batch_artifacts.py (no args) and run check_structure.py --config checks.json + check_content.py --config checks.json (NOTE: check_content prints KNOWN PRE-EXISTING artifacts and exits nonzero because of them - ch08 Shunde ×3, ch13 ×9, ch09 "Jize County" ×1, ch26's TWO documented keyed-substring FALSE POSITIVES 武汉卿/劳勃生路, and ch38's 海防/Haiphong HOMOGRAPH FALSE POSITIVE [海防 = "coast defense" common noun, keyed as the place Haiphong]; CONFIRM ch40 shows "all in the paired paragraph" / 0 displaced, and align any keyed name/place/TERM to its glossary-decided rendering. A NEW unit's displacements are almost always a keyed name/place/term rendered a DIFFERENT way than the glossary - align the English to the keyed form; a genuine common-noun HOMOGRAPH of a keyed place is a documented false positive, translation stands). Do NOT add COMMON-NOUN or book/periodical keys. ⚠ BEFORE keying a NEW name/place, grep the OTHER chapters' data/zh for the same hanzi and confirm it renders the SAME way there - a cross-chapter conflict (like 张垣 Zhangyuan vs ch08's Zhangjiakou at B32) means render inline, do NOT key. qc_entities.py on a reconstructed bilingual (data/zh body lines minus the `### ` heading lines + out/ch40_en.json, `> zh` / en pairs; every glossary row needs a pinyin field - the reconstruction one-liner is in PROGRESS/the ch30-ch39 method; WATCH the keyed term rendered as a VERB not the noun, cf. 绥靖 "pacify" vs "pacification"). Verify the TAIL against the source. check_register.py --ref reference/B01_frozen.md out/ch40_reading.md ("shall" deliberate).
4. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (full list in PROGRESS.md; the big already-covered furniture incl. the Nationalist 绥靖/戡乱/共匪 framing, the Marshall Mission/Committee of Three/Executive HQ, the Lizhi Plan/Class, the Youth Army, Fu Zuoyi/Beiping's surrender, the Baomiju, Whampoa, the Marco Polo Bridge, fabi, the Republican-year system, the Transport Police Corps, the Three-Anti/Five-Anti/Suppress-Counterrevolutionaries campaigns, the Social Affairs Department, the Cultural Revolution/Red Guards, Lin Biao's 1971 death, the Battle of Shijiazhuang, the recovery of Yan'an, the heart-extraction tactic, the Type 38/Type 30 rifles, the Mao epithets, the province one-char abbreviations 晋/察/冀/鲁/豫, the 三光部队 epithet, Jing Ke's Yi River song, Du Xinwu/Hongmen/Green Gang, the Four Great Dan, the chicken-feather post, the baojia system, Moxingling, He Long/Xiao Ke, Kangda, the Eighth Route Army/Eighteenth Group Army, the chuigushou, the Hanyang rifle, the 用而不疑 maxim; and from B32: the City of the Wrongfully Dead, the Battle of Laishui, the Battle of Xinbao'an/Pingjin Campaign, the Fu-Zuoyi intelligence leak/Fu Dongju, "Be a nameless hero"/the book's title, the Dagong Bao, the Kanjurwa Khutukhtu, the 数九 nines of winter). LIKELY new for ch40: whatever fresh material culture / institutions / place-lore the four sections raise (the fates of the three men, the "arch-enemy" of the North China front, the dead comrades, the string of defeats). Be generous but do NOT pad, do NOT re-note. Merge notes via apparatus_merge.py (positional arg: apparatus_merge.py data/ch40_apparatus.json; numeric character references only in note bodies; anchors verbatim ASCII substrings of the reading.md body text, NO em dash and NO quote/apostrophe character - substring traps; multi-occurrence anchors attach at the first; TIGHTEN a generic anchor). Add glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field; apparatus_merge's glossary path assumes a FLAT map and would corrupt the sectioned file - use it ONLY for notes; scripts/add_ch39_glossary.py is the latest by-hand pattern, asserting each hanzi key against data/zh; ⚠ if a place/name has an apostrophe, set the glossary en to the CURLY-apostrophe form the reading.md uses, cf. Xinbao’an). For any CJK in a note body use the make_ch39_apparatus.py pattern (author bodies with typed hanzi + untoned pinyin, ASSERT every non-ASCII glyph is present in data/zh/ch40.txt, then convert to NCRs) - and remember a CORRECT glyph may be ABSENT if the source prints a glitch/variant form, so describe such terms with the source's own form + pinyin. Confirm ch40's image count (grep <img>; ch32-ch39 carried none).
5. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session); record all check results in PROGRESS.md; update HANDOFF.md; commit and push to claude/nameless-heroes. (Next is B34 = ch41; confirm scope in book.json. Working batch labels run ONE AHEAD of book.json's batches array: book.json B33 = ch41 = working B34. Part Four = ch32-ch43; after ch42 only ch43 = the Afterword remains.)

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B34 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
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
  4 <h3> + 188 <p>, standalone=[18,71,108,154], ONE glitch-masked sever merges=[(49,50)]. **⚠ MAJOR
  SOURCE DUPLICATION** (the intelligence-timeliness preamble printed 3×, the Anguo raid 2×, a heading
  fused mid-<p>), translated in FULL with a footnote. 187 body paragraphs; median ratio 5.42. 8 notes;
  13 keyed rows.
- **Batch B30 (ch37), the FIFTH Part-Four NARRATIVE chapter.** 第五章 兵连祸结 民不聊生. drop=2; 1 <h2> +
  3 <h3> + 144 <p>, byte-exact, standalone=[11,43,90], NO severs, NO duplication. 144 body paragraphs;
  median ratio 5.50. 8 notes; 12 keyed rows. 7 noise additions.
- **Batch B31 (ch38), the SIXTH Part-Four NARRATIVE chapter.** 第六章 曲直分明 反复无常 (the Zhu Zhankui
  defection case). drop=2; 1 <h2> + 4 <h3> + 135 <p>, byte-exact, standalone=[15,46,69,113], NO severs,
  NO duplication. 135 body paragraphs; median ratio 5.55. 8 notes (335 cumulative); 10 keyed rows.
  check_content 1 "displaced" = the DOCUMENTED 海防/Haiphong HOMOGRAPH FALSE POSITIVE. 8 noise additions.
- **Batch B32 (ch39), the SEVENTH Part-Four NARRATIVE chapter.** 第七章 瞻前顾后 未雨绸缪 "Looking Before
  and After, Providing Against the Storm" — Wang Zhaofen's account of the First Command Room's work at
  Zhuoxian (the Zhenmin Herald, the "iron triangle," the mass encoffining after Laishui, the
  "Cleanse-the-Source" movement); Zhang Luying's account of the Fifth Command Room at Zhangyuan; Chen's
  reckoning of Fu Zuoyi's vacillating strategy and the destruction of the 35th Army at Xinbao'an and the
  11th Army Group at Zhangyuan; the Nanjing conference, the audience with Chiang ("Be a nameless hero"),
  and the plan to move the First Brigade south. drop=2; 1 <h2> + 3 <h3> (section heads 一/二/三) + 179
  <p>, byte-exact p-by-p, standalone=[15,61,133], NO severs (all ！/？-enders complete), NO
  source-duplication. 179 body paragraphs; median ratio 5.58 (document/quote-heavy). 8 notes (343
  cumulative); 15 net-new keyed rows (10 people, 5 places). check_content 0 displaced; qc 0 misses
  (fixed 1 verb-form 绥靖 -> the noun "pacification"); register within tolerance. qa_epub PASS; epubcheck
  0/0/0/0. **EPUB now 39/43 chapters, 343 notes.** 7 noise additions (六神无主, 赵百川, 崔万兴, 一来二去,
  顚三倒四, 三心两意, 数九寒天). DROPPED the 张垣 key (cross-chapter conflict with ch08's Zhangjiakou;
  rendered "Zhangyuan" inline). Detail in PROGRESS.md ("Batch B32").

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` - derives data/zh/<id>.txt verbatim from data/src, applying per-unit
  drops/merges/heading-splits with a source-conservation check. Specs for ch01-ch39. Merge logic
  FOLLOWS CHAINS. **drop is variable:** most chapters drop=2; ch01/ch10/ch20/ch32 drop=3 (a part
  super-title precedes the preface). `standalone` = a sub-heading kept as its own line with no
  heading markup, emitted as `### ` (used for both plain-<p> sub-heads AND separate <h3> section
  elements, cf. ch33-ch39's <h3> section heads); `glued` = a heading fused onto a paragraph's
  TAIL; `glued_head` = a heading fused onto a paragraph's HEAD; `merges` = source <p> pairs that
  sever one sentence OR an intra-<p> `<br/>` line break, AND can be MASKED by a glitch (scan
  ！？》-ending lines, not just non-terminal ones - ch33 L19/20, ch35 L25/26 & L136/137, ch36 L49/50;
  BUT ch37/ch38/ch39's ！/？-enders were all complete sentences, NOT severs). **A chapter can carry
  INNER enumerated 一、二、三 / 第一、第二 DOCUMENT-CLAUSE or NUMBER-RANGE or NAME-LIST or OPTION-LIST
  content that is NOT a section heading - keep those as ordinary body lines per parity, judged by
  function** (ch27-39; ch39's L50-53 option-list used the glitch marker 凵 for 一, kept as body lines,
  rendered (1)-(3)). **⚠ ch36 taught a SOURCE-DUPLICATION class (a chapter's opening printed 2-3x, a
  section-heading text fused mid-<p>). Preserve it all per rule 4; footnote it. ch37/ch38/ch39 had none.**
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
  County" (1)**; **B20's TWO keyed-substring FALSE POSITIVES 武汉卿/劳勃生路**; **ch38's 海防/Haiphong
  HOMOGRAPH FALSE POSITIVE** (海防 = "coast defense" common noun). The pass criterion for a NEW batch is
  "the batch's own unit shows all name occurrences in the paired paragraph / 0 displaced." A NEW unit's
  TRUE displacements are almost always a keyed name/place/TERM rendered a DIFFERENT way than the
  glossary: align the English to the keyed form. **Do NOT key a place/term whose hanzi is a substring of
  a DIFFERENT keyed rendering. ⚠ Do NOT key hanzi that renders DIFFERENTLY in another already-shipped
  chapter (cross-chapter conflict): grep the other chapters' data/zh first (B32 dropped 张垣→Zhangyuan
  because ch08 renders 张垣 as Zhangjiakou).** Do NOT add book-TITLE or COMMON-NOUN keys.
- **Verse marker `{p}`** (ch13, reused ch26): prefix a pure-verse line with `{p} `; the builder
  renders `<p class="verse">`; the checks strip it.
- Glossary is authored/merged BY HAND into the SECTIONED file (book/people/organizations/places/
  terms), a dict keyed by hanzi, idempotent + re-read-verified. **Every row MUST carry a `pinyin`
  field** - qc_entities does `rec["pinyin"]` and KeyErrors otherwise. `scripts/add_ch39_glossary.py`
  is the latest by-hand pattern: covers people/places sections in one pass, asserts each hanzi key
  is a substring of that unit's data/zh/<id>.txt. **⚠ If a keyed name/place contains an apostrophe,
  set the glossary `en` to the CURLY-apostrophe form the reading.md renders (’, U+2019), or
  check_content/qc will miss it** (B32: 新保安 en = "Xinbao’an"). apparatus_merge's glossary path
  assumes a FLAT map and would corrupt the sectioned file; NOTES still go through apparatus_merge.py.
- **qc_entities catches term-rendering drift too:** a glossary common-noun/term rendered a
  different way (or as a VERB not the noun) flags as a "miss." Align the English to the glossary
  (B26/B30/B32: 绥靖 keyed "pacification" flagged when rendered the verb "pacify"/"pacified"). qc has a
  first/last-word fallback, so a keyed en that starts with "the" is trivially satisfied - prefer
  distinctive en.
- **GLOSSARY-KEY DISCIPLINE:** a key must be a DISTINCTIVE proper noun (or a distinctive institution)
  that renders ONE way EVERYWHERE (across ALL chapters). Periodicals and books are FOOTNOTES/inline.
  One-off transliterated Western/Japanese/Mongol names, one-off telegram/roster/memoir names, standard
  province names, and attested Shanghai ROADS are inline. A bare surname whose full name is unknown is
  rendered inline. NEVER key hanzi that is a substring of a different keyed rendering, NOR hanzi that
  renders differently in an already-shipped chapter. (A name inline in one chapter can GRADUATE to a
  key when it becomes central: 常绍曾 inline ch36 -> keyed ch37; 张鲁颖 inline ch38 -> keyed ch39.)
- **Note-anchor gotchas:** anchors must be ASCII, WITHOUT any quote/apostrophe character AND
  without an em dash (U+2014) - all substring traps. The reading.md uses curly quotes and em
  dashes freely, so pick an anchor phrase with none of them. **Multi-occurrence anchors attach at
  the FIRST occurrence** - if a short generic anchor would match an EARLIER paragraph, LENGTHEN it.
- **make_ch39_apparatus.py pattern (scripts/):** author note bodies as plain ASCII + typed hanzi +
  UNTONED pinyin + straight quotes, allow em-dash, ASSERT every non-ASCII glyph occurs in THAT UNIT's
  data/zh/<id>.txt, then convert every non-ASCII char to a numeric char ref and run apparatus_merge.py.
  **A CORRECT glyph may be ABSENT if the source prints a glitch/variant** - describe such terms with
  the source's own form + pinyin/English. A note that quotes ANOTHER unit's text or names ABSENT from
  this unit (e.g. 傅冬菊 Fu Dongju at ch39) is authored ENGLISH-ONLY to avoid the glyph-assert.
- **⚠ ENUMERATION MARKERS carry a numeral the checker reads.** Render list ordinals as spelled
  ordinals ("First/Second/Third", cf. ch34) or arabic "(1)(2)(3)", NOT roman "(i)(ii)(iii)": roman
  markers do not carry the value and flag as unaccounted numbers. Glitch-marked items with no source
  numeral rendered as arabic are safe/target-only (the checker is source->target only).
- data/noise.txt carries the B01-B32 project noise rules (each with a comment line). Republican
  years render literally; the checker matches the source numeral (or auto-escapes Republican-year
  N via N+1911). **SPELLED-OUT COMPOUNDS DO NOT COMPOSE** (target "three thousand five hundred" =
  {3000,500}, not 3500): write exact multi-part counts as DIGITS (3,500 / 120 / 3,200,000). **ORDER
  MATTERS in noise.txt:** a longer numeral idiom must precede a shorter one that is its prefix. Idiom
  numerals (六神无主, 顚三倒四, 三心两意, 数九寒天, 一来二去...), name-numeral glyphs (赵百川, 崔万兴...),
  approximate ranges, place-name numerals, and counter-by-naming forms are noised. The ○ (U+25CB) and
  〇 (U+3007) address/redaction/code artifacts: the checker cannot read them as digits - noise the
  mis-read glyph-string, carry the real value in English. × (source redaction) renders as an em-dash
  blank (第x纵队 -> "the ——th Column").
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches it; re-run per session).
  setup.sh's ONE failing regression test ("hook stands down on template stub") is a KNOWN false
  alarm; all other regression tests pass.

## Renderings settled / carry-forward

- 军统 / 军统局 -> "the Juntong" / "the Juntong Bureau" (DECIDED). 保密局 -> "the Baomiju" (DECIDED, B26).
  戴笠 Dai Li (courtesy Yunong; 老板 "the Boss"; 戴先生 "Mr. Dai"). 制裁 "sanction". 敌伪 "the enemy and
  the puppets"; 沦陷区 "the fallen zone(s)". Chiang's titles: 校长 "the Commandant", 委员长/委座 "the
  Generalissimo", 总裁 "the Director-General"; 领袖 "the Leader"; 总理 "the Party Leader" (Sun Yat-sen);
  蒋公/蒋主席/总统 "His Excellency Chiang"/"Chairman Chiang"/"the President". 三民主义 "the Three
  Principles of the People."
- **B24 (Shanghai unit vocab):** 大队长 "brigade commander"; 分队 "sub-brigade"; 三道头 "three-stripe
  head"; 内交通 "internal courier".
- **B25 PART-FOUR vocab (reuse):** 总队 "Corps" / 总队长 "Corps Commander"; 大队 "brigade"; 中队 "company";
  指挥室 "command room"; 指挥员 "commanding officer" vs 指挥官 "commander"; 突击队 "assault team"; 直属组
  "directly subordinate section"; 部队长 "unit commander"; 编制 "establishment"; 配属关系 "relation of
  attachment"; 留置工作 "stay-behind work"; 绥靖 "pacification" / 戡乱 "suppression of rebellion" / 剿匪
  "bandit-suppression" / 匪谍 "Communist spies" / 共酋 "Communist chieftains" / 共干 "Communist cadres";
  收复区 "recovered areas" / 交战区 "combat zones"; 行辕 "Field Headquarters" (北平行辕 "the Beiping Field
  Headquarters"). Republican years literal.
- **B26 PART-FOUR vocab (ch33; reuse):** 特种部队 "special-operations unit" (KEYED); 特种组织 "special
  organization" (KEYED); 联合会报 "joint briefing"; 直属通信员 "directly subordinate courier"; 外勤单位
  "field unit"; 第二厅 "the Second Bureau"; 双重关系 "double relationship" / 双重任务 "double mission".
- **B29 PART-FOUR vocab (ch36; reuse):** 掏心战术 "the heart-extraction tactic" (KEYED); 平津保三角地带
  "the Beiping-Tianjin-Baoding triangle" (KEYED); 暂编第三军/暂三军 "the Provisional Third Army"; 三八式/
  三〇式 "the Type 38"/"Type 30" rifles; 匪酋 "bandit chieftains" / 匪军 "the bandit army/forces" / 匪干
  "bandit cadres" / 匪区 "bandit-held territory". The Mao epithets: 毛酋 "the bandit chief Mao", 毛贼泽东
  "the bandit Mao Zedong", 毛某 "the man Mao"/"Mao".
- **B30 PART-FOUR vocab (ch37; reuse):** 北郊混合组 "the North-Suburb Mixed Group" etc. (descriptive unit
  names, rendered consistently but NOT keyed); 情报小组 "intelligence squad"; 自衞队/自卫队 "self-defense
  corps"; 三光部队 "the Strip-It-Clean Force" (noted); 灰色地带 "gray zone"; 保甲/保公所 "baojia" /
  "baojia office" (noted). 华北剿总 = "the North China Bandit-Suppression Headquarters".
- **B31 PART-FOUR vocab (ch38; reuse):** 突击队 "assault team" / 直属突击队 "directly subordinate assault
  team"; 区队 "district company" / 区队长 "district-company commander"; 分队 "sub-brigade"; 小组 "small
  group" / 小组长 "group leader"; 骑兵班 "cavalry squad"; 第二指挥室 "Second Command Room"; 打情报
  "beating out intelligence"; 扩大游击面 "widening the guerrilla front"; 用而不疑、疑而不用; 泱泱大度.
  抗日军政大学/抗大 "the Anti-Japanese University"/"Kangda"; 八路军/第十八集团军 "the Eighth Route
  Army"/"the Eighteenth Group Army".
- **B32 PART-FOUR vocab (ch39; reuse):** 保安团/保安旅/保安大队 "Peace-Preservation Regiment/Brigade/
  Battalion"; 行政督察专员公署 "Administrative Inspectorate Commissioner's Office" / 专员 "commissioner";
  混合组 "Mixed Group"; 情报组 "Intelligence Group" / 绥靖组 "Pacification Group" / 突击组 "Assault Group";
  第一指挥室/第五指挥室 "First/Fifth Command Room"; 灰色人物 "gray figure" / 两面人 "man of two faces";
  中航 "China National Aviation"; 陆大 "the Army War College"; 军校特别研究班 "the Military Academy
  Special Research Class"; 门户之见 "sectarian bias"; 反间 "the counter-agent"; the 0760 unit code carried
  as digits; the "iron triangle of Beiping-Tianjin-Baoding" (平津保铁三角, descriptive, built on the
  keyed 平津保三角地带). Rail lines by dashed pinyin (Ping-Han, Jin-Pu, Ping-Sui, Ping-Cheng, Ping-Jin,
  Bei-Ning, Ping-Bao, Ping-Gu).
- **PLACE-NAME CONVENTION (the qc gate enforces the glossary's PINYIN for keyed cities/places):**
  北平 Beiping, 天津 Tianjin. KEYED: 石家庄 Shijiazhuang, 石门 Shimen, 安次 Anci, 安国 Anguo, 正定
  Zhengding (B29); 立水桥 Lishuiqiao, 大兴 Daxing, 赵家坟 Zhaojiafen (B30); 王庆沱 Wangqingtuo, 杨柳青
  Yangliuqing, 独流 Duliu, 静海 Jinghai, 顺义 Shunyi, 唐官屯 Tangguantun (B31); 涿县 Zhuoxian, 涞水
  Laishui, 保定 Baoding, 新保安 Xinbao’an (curly-apostrophe en) (B32); 张家口 Zhangjiakou, 塘沽 Tanggu.
  ⚠ 张垣 = the literary name of Zhangjiakou, rendered "Zhangyuan" INLINE (NOT keyed - ch08 renders 张垣
  as Zhangjiakou; whole-book reconciliation item). KEYED gates 安定门 Andingmen, 西直门 Xizhimen. KEYED
  冀东 "East Hebei". Standard provinces inline in pinyin (河北 Hebei, 山西 Shanxi, 山东 Shandong, 河南
  Henan, 陕西 Shaanxi, 绥远 Suiyuan, 察哈尔 Chahar); 晋察冀 "Jin-Cha-Ji", 晋冀鲁豫 "Jin-Ji-Lu-Yu" (the
  one-char abbreviations noted at ch37). 五台山 the Wutai Mountains, 太行山 the Taihang Mountains, 延安
  Yan'an - INLINE. The many one-mention places of ch39 (归绥 Guisui, 包头 Baotou, 承德 Chengde, 葫芦岛
  Huludao, 长春 Changchun, 济南 Jinan, 开封 Kaifeng, 香林寺 Xianglin Temple etc.) are INLINE.
- **Book / part titles (in-text; DECIDED; reuse verbatim):** 英雄无名 = "Nameless Heroes"; Part One
  北国锄奸 = "Rooting Out Traitors in the North"; Part Two = "Disgrace at Hanoi"; Part Three 百战声威
  = "Renown Won in a Hundred Battles"; Part Four 平津地区绥靖戡乱 = "Pacification of the Beiping-Tianjin
  Region". 忠义救国军 = "the Loyal and Patriotic Army".
- **B32 shelf (ch39; keyed):** people 王兆芬 Wang Zhaofen (First Command Room, section-1 account author),
  张鲁颖 Zhang Luying (Fifth Command Room, section-2 account author; graduated from inline in ch38),
  陈振山 Chen Zhenshan (Second/Northeast Brigade cmdr), 孟广第 Meng Guangdi (Baoding Group, sub-account),
  鲁英庆 Lu Yingqing (35th Army cmdr, Laishui suicide; source glitches 鲁英尘/鲁英屡), 郭景云 Guo Jingyun
  (35th Army cmdr, Xinbao'an suicide), 孙兰峰 Sun Lanfeng (11th Army Group cmdr), 李铭鼎 Li Mingding
  (division cmdr, Laishui suicide), 李中庸 Li Zhongyong (Second-district commissioner), 王凤岗 Wang
  Fenggang ("iron triangle" commissioner) — all provisional; places 涿县 Zhuoxian, 涞水 Laishui, 保定
  Baoding, 新保安 Xinbao’an (decided). Kept INLINE (glossary-key discipline): 王有声/张荫梧/赵伯衡/孙祖义/
  崔老选/崔万兴/赵百川(=赵明山)/陈凤桐/王志毅/白德昭/贡楚格策登/乌瑞山/仁亲道尔吉/孙文良/钟宁寿/楚溪春/
  何思源/刘瑶章/范汉杰/王云孙/杨予/魏宁; the Communist commanders 刘伯承/陈毅/徐向前; 张垣 Zhangyuan
  (reconciliation item). Villages/places inline: 宛平/小稻村/望都/易县/多伦/宣化/怀安/沙城/万全/柴沟堡/
  下花园/通县/丰台/张飞店/南苑/归绥/包头/集宁/大同/太原/承德/葫芦岛/长春/济南/开封/唐山/丰润/昌黎/
  秦皇岛/房山/定兴/满城/大沽口/青岛/香林寺.
- **Earlier shelves (B15-B31)** remain in PROGRESS.md and prior HANDOFFs; the whole B02-B31 cast is
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
  Xiao Runyu / Niu Guangjin; ch37's Lu Deming, Chang Shaozeng, Tian Yingjie; ch38's Wang Hongzhu /
  Chang Shaozeng / Wu Chunxiang / Wang Zhiyi; ch39's Wang Zhaofen / Zhang Luying / Meng Guangdi). Keep
  these in a plain, vivid first person DISTINCT from Chen's own essayistic frame; Chen's inserted 笔者
  附注 (writer's notes) return to his grave register. Set a long extracted account WITHOUT an outer
  quote layer (double quotes only for the account's own quoted terms/inner speech), the way ch39
  presents Wang Zhaofen's account, to avoid unreadable nested guillemets.
- Ratio ~4.55-4.78 en/han in NARRATIVE; prefaces denser (ch32 5.57); DOCUMENT/QUOTE-HEAVY chapters
  run higher (ch33 5.32, ch34 5.19, ch35 5.15, ch36 5.42, ch37 5.50, ch38 5.55, ch39 5.58). Read the
  note, do not reset. Alignment/register are the gates, not the raw ratio.

## Voice sheets - principal & recurring cast (Part Four)

- **CHEN GONGSHU himself.** Commands the First Brigade of the Pacification Corps in the Beiping-Tianjin
  region, 1946-49; also (against his will) leader of the Baomiju's Beiping directly subordinate section.
- **ZHENG JIEMIN (郑介民 / Mr. Zheng).** Chen's old Beiping-days superior; Chief of the Second Bureau of
  the Ministry of National Defense, government rep on the Executive Headquarters, head of the Lizhi
  Class. In ch39 he charges Chen (informally) to prepare the "stay-behind work."
- **LIU PEICHU (刘培初).** Corps Commander of the Pacification Corps; ascetic, hard-driving; Chen is at
  odds with him (ch39: Chen wants the First Brigade transferred south, which needs Liu's assent).
- **THE THREE FIRST-BRIGADE PILLARS (ch33 s4):** LI YULIN (李玉林, deputy cmdr, "Fifth Brother"; ch39
  sent to Nanjing with the stay-behind plan), LUO JING (罗敬, political director), LIU YUANSHEN (刘原深,
  chief secretary).
- **THE FIELD MEN:** CHANG SHAOZENG (常绍曾), TIAN YINGJIE (田英杰), FENG YUZHU (冯玉柱), LIU ZIYUAN
  (刘子元); the account-authors WANG ZHAOFEN (王兆芬, First Command Room), ZHANG LUYING (张鲁颖, Fifth
  Command Room), CHEN ZHENSHAN (陈振山, Northeast/Second Brigade).
- **FU ZUOYI (傅作义).** Commander-in-chief of the North China Bandit-Suppression HQ; Chen paints him as
  vacillating, "sectarian," clinging to Chahar-Suiyuan; his best army destroyed at Xinbao'an (ch39),
  and he surrenders Beiping in early 1949.

## ⚠ Name trap RESOLVED (do not reopen): 陈邦国 / 郑邦国

The Hanoi action-team member the source spells 郑邦国 in ch13 and 陈邦国 in ch15/ch16/ch17 is ONE
man. RESOLVED to **Chen Bangguo (陈邦国)**. Use Chen Bangguo consistently.

## Where the book stands

- Part One (北国锄奸) COMPLETE (B01-B05). Part Two ("Disgrace at Hanoi") COMPLETE (B06-B13). Part
  Three ("Renown Won in a Hundred Battles" / 百战声威) COMPLETE (B14-B24).
- **Part Four ("Pacification of the Beiping-Tianjin Region") OPEN: B25 = ch32 (self-preface) DONE;
  B26 = ch33 (第一章) DONE; B27 = ch34 (第二章, doctrinal) DONE; B28 = ch35 (第三章) DONE; B29 = ch36
  (第四章) DONE; B30 = ch37 (第五章) DONE; B31 = ch38 (第六章) DONE; B32 = ch39 (第七章) DONE.**
- **NEXT: B33 = ch40** = 第八章 抚今追昔 烟波千里 "Chapter 8. Musing on Past and Present, Mist over a
  Thousand Miles" - a NARRATIVE chapter, FOUR sections (ch40s01-ch40s04). Structure CONFIRMED at B32:
  1 <h2> + 4 <h3> (section heads 一/二/三/四) + 170 <p>, NO <h1>/<br/>/<img>/note-markers, 0 images,
  **drop=2**; the 4 <h3> are SEPARATE elements -> `standalone ### `. ⚠ 1-line count scare (ch36/ch38/
  ch39 pattern): raw txt = 176 lines (no trailing newline; wc -l 175); 176 - 2 = 174 = 4 h3 + 170 p.
  src 41_index-split-000-0039.txt. Grep p-by-p for severed-<p> boundaries (non-terminal AND
  glitch-masked ！？》) AND for a ch36-class source-duplication run.
- After B33: B34 = ch41. Part Four = ch32-ch43; ch33-ch42 carry `sections` arrays (the 1946-49
  narrative); ch43 = the Afterword. Working batch labels run ONE AHEAD of book.json's batches array
  from ch24 on (ch39 = B32, ch40 = B33, ch41 = B34).
- The frozen register reference is `reference/B01_frozen.md`. Prefaces denser (ch32 = 5.57);
  document/quote-heavy chapters higher (ch33-ch39 = 5.15-5.58) - alignment/register are the gates,
  not the raw ratio.
- Sub-heading pattern: Part Four chapters ch33-ch42 carry book.json `sections` arrays; the section
  headings appear in the source as SEPARATE <h3> ELEMENTS that emit as `standalone ### `. DISTINGUISH
  enumerated LIST items / document clauses / number-ranges / name-lists / OPTION-lists (kept as body
  lines per parity) from the true section headings. Grep each new chapter p-by-p.
- WATCH for source anomalies: cuts, misplaced-「 glitches, corrupt/dropped-character phrases, dropped
  full stops, a STRAY glyph fused onto a title, stray ？/》/！/〞/" (often standing for a closing 」), the
  ○ (U+25CB) / 〇 (U+3007) and × redactions, name glitches, variant forms, pervasive single-character
  substitutions, enumeration-marker glitches (工/口/闫/出/凵 for 一/二/三/七), orphaned 。 at a <p> head,
  severed-<p> boundaries (MERGE; can be glitch-MASKED), AND the ch36-class SOURCE DUPLICATION.
  Re-grep each batch's source for `\[\d+\]` note markers (none through B32).

## Open items for the read-through / completion

- Feed decided renderings back to authority.json on completion: 军统 "the Juntong"; 保密局 "the Baomiju";
  the full B02-B32 historical-name set; the Part-Four vocabulary.
- Japanese/Mongol name readings to firm up when the men recur (incl. the Kanjurwa Khutukhtu's brother).
- Provisional romanizations to firm up (glossary `provisional` rows, incl. the B32 people 王兆芬/张鲁颖/
  陈振山/孟广第/鲁英庆/郭景云/孙兰峰/李铭鼎/李中庸/王凤岗; the B30/B31 people; 刘培初/计兆祥).
- Whole-book reconciliation items: ch09 "Jize County"; the pinyin-vs-postal city names; the two B20
  keyed-substring false positives (武汉卿 / 劳勃生路); ch38's 海防/Haiphong homograph; **张垣 rendered
  "Zhangjiakou" in ch08 but "Zhangyuan" in ch39 (the literary vs modern name of the same city - decide
  a whole-book policy at reconciliation)**; the Malone spelling (ch30); the ch32 "Fifth Part" numbering
  discrepancy; the garbled deputy-chief-of-staff surname glyph 鿄 (ch36); the Mao-at-Anguo intelligence
  (ch36); 杜心吾/杜心五 and 程艳秋/程砚秋 name-form variants (ch37); the 鲁英庆/鲁英尘/鲁英屡 name glitches
  (ch39, one man = Lu Yingqing).

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01-B32 builds (0/0/0/0). Source is a clean digital
  EPUB, predominantly simplified with residual variant glyphs and pervasive digitization glitches
  (list them, render to plain sense, do not footnote mechanical typos). B01-B32 glitch lists in
  PROGRESS.md. **ch36 added a SOURCE-DUPLICATION class (opening printed 2-3x) - watch for it; ch37/ch38/
  ch39 had none.**
- Running-header line 英雄无名-陈恭澍 opens all 43 content files: drop it. drop count is variable -
  most drop=2; ch01/ch10/ch20/ch32 drop=3.
- Enumerated ；/：/、 bullet lists, quoted-document/directive/roster lines (INCLUDING intra-<p>
  `<br/>` TABLE rows and INNER document-clause / range / name-list / option-list / 第一、第二 lists),
  salutations, verse lines, run-in section labels, and 『』/「」-closed dialogue are DELIBERATE separate
  lines - do NOT merge them; only genuine mid-phrase splits (last char not terminal, OR a source <p>
  boundary that severs one sentence - possibly MASKED by a glitch ！/？/》 for 」, OR an intra-<p>
  `<br/>` inside PROSE) merge, and those can CHAIN. (ch37/ch38/ch39 had NO merges: their ！-enders were
  complete.)
- Faithful numbering gaps/anomalies (NOT errors): Part Three skips 第七章 (ch27 = 第八章); 第十章 splits
  into (上)/(下) (ch29/ch30); 三面受敌 一往无前 titles two chapters; ch32 numbers the Beiping-Tianjin
  volume "the Fifth Part" though Shanghai was "the Third Part" (footnoted). Preserve and footnote.
- Expect a stray per-task branch at the top of every batch; consolidate onto claude/nameless-heroes
  per rule 2.
