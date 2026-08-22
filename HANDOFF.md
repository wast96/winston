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
Nameless Heroes B36

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once (its ONE failing regression test, "hook stands down on template stub", is a KNOWN false alarm; all others pass), then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05) through B35 (ch42) are DONE; the voice gate is PASSED and the FROZEN register reference is reference/B01_frozen.md. Do NOT re-do them. PARTS ONE, TWO ("Disgrace at Hanoi"), THREE ("Renown Won in a Hundred Battles" / 百战声威) are COMPLETE; PART FOUR ("Pacification of the Beiping-Tianjin Region" / 平津地区绥靖戡乱) is nearly complete - ch32 was its self-preface, ch33-ch42 the TEN narrative chapters (all DONE); only the Afterword ch43 remains. The EPUB now holds 42/43 chapters, 371 notes. NOTE on batch numbering: book.json's batches array lumps ch23+ch24 as "B17", so the working batch labels run ONE AHEAD of the book.json array from ch24 on (ch42 = working B35 = book.json's B34 entry; ch43 = working B36 = book.json's B35 entry, the LAST entry).

Do Batch B36 = ch43 = 英雄无名 篇后续话 "Afterword: Closing Remarks" (ONE unit, NO sections; the WHOLE-BOOK COMPLETION batch - the LAST batch). SHORT reflective essay (expect a ratio possibly higher than the narrative band, like the ch32 preface 5.57; alignment/register are the gates, not the raw ratio). Chen's grave essayistic first person at its most reflective, looking back over all five books of the memoir and forward to a hoped-for end of the "sanction"/assassination work of the secret services - PRESERVE the register (the narrating "shall" is DELIBERATE). This is a QUIET, non-narrative coda; no contributed accounts, no unit vocabulary. Read the tail of ch42 (out/ch42_reading.md, the ring-composition close: "The writer, being one of its members, could hardly stand aside... Among the whole record, what is worth setting down lies still in the honesty, the loyal courage, the sacrifice, and the devotion to duty of the students and comrades") for the batch seam. Run it end to end per the CLAUDE.md pipeline, to completion (no approval gate). AS THE FINAL BATCH it ALSO carries the whole-book completion work (see step 5).
1. Read ch43 (44_index-split-000-0042.txt) from data/src. CONFIRM structure p-by-p against data/src_epub/OEBPS/Text/index_split_000_0042.xhtml [ch43: 1 <h2> (英雄无名 篇后续话) + 32 <p>, NO <h1>/<h3>/<br/>/<img>/[\d+], 0 images - CONFIRMED at B35]. **drop=2** (running header 英雄无名-陈恭澍 + <h2> chapter title). NO sections (no <h3>) -> book.json ch43 has NO `sections` array; the reading.md is just `## title_en` + body paragraphs. ⚠ COUNT DISCREPANCY TO RESOLVE FIRST: the raw txt is 33 python-lines (no trailing newline); drop(2) leaves 31 NON-EMPTY body lines, BUT the xhtml shows 32 <p> (31 != 32). Do the byte-exact p-by-p diff FIRST (the B19-B35 method: extract <p> inner text in document order, walk each consuming 1 body line, assert every line matches) to RESOLVE the 1-line gap - most likely an EMPTY <p> in the source (skip it; the extractor may drop it) OR an extractor-split/severed <p> that MERGES two txt lines into one <p> (or vice-versa). Determine which, then set clean_batch.py's ch43 spec accordingly (drop=2; NO standalone [no <h3>]; any confirmed merges; NO glued/glued_head unless the diff reveals one). ALSO scan ！？》-ending lines for glitch-masked severs and grep for a ch36/ch41-class source-injection run (内容提要/篇后续话 fused mid-<p>; near-duplicate scan). Run clean_batch.py (source-conservation check must pass). Write out/ch43_reading.md (## from book.json title_en; NO ### sub-headings; one English paragraph per source body line). Then run scripts/batch_artifacts.py ch43, and ALWAYS finish with a NO-ARG run (the trap: an ID-run writes checks.json with ONLY that unit; the no-arg run restores all 43 units so check_structure/check_content see them).
2. Translate to the FROZEN register (Chen's voice sheet in HANDOFF; the narrating "shall" is DELIBERATE, do NOT de-formalize). Consult glossary.json and authority.json BEFORE romanizing anything; REUSE the settled renderings (PROGRESS.md shelves + HANDOFF "Renderings settled"). The Afterword is REFLECTIVE, not narrative: likely LIGHT on new proper nouns. KEYED terms that may recur (qc enforces where keyed): 制裁 "sanction"; 军统/军统局 "the Juntong"/"the Juntong Bureau"; 保密局 "the Baomiju"; the book/part titles (英雄无名 "Nameless Heroes"; the five parts). Render Republican years literally (checker matches the source numeral or +1911; SPELLED-OUT COMPOUNDS DO NOT compose - write exact multi-part counts as DIGITS, the B26-B35 trap). WATCH the same digitization-glitch classes (single-char/name substitutions, dropped 。 stops, mismatched guillemets ﹁﹂﹃﹄, stray ？/》/！ for a closing 」, ○/〇/× redactions - carry the real value in English, noise only the mis-read glyph-string). data/noise.txt already carries the B01-B35 rules; add B36's if any, ORDER longest-first if a new form is a prefix of an existing rule (and remember the orphan-strip lesson from B35: an existing shorter rule may strip part of your compound first, orphaning a digit - noise the RESIDUAL form, e.g. 千方 after 百计, 两黄金 after 三、五十).
3. Checks: verify_unit.py ch43 (parity + numbers with noise auto-found + anchors); check_align.py ch43; regenerate checks.json with scripts/batch_artifacts.py (no args) and run check_structure.py --config checks.json + check_content.py --config checks.json (NOTE: check_content prints KNOWN PRE-EXISTING artifacts and exits nonzero - ch08 Shunde ×3, ch13 ×9, ch09 "Jize County" ×1, ch26's 武汉卿/劳勃生路 ×2, ch38's 海防/Haiphong ×1, ch41's 河内/Hanoi ×1 [all documented FALSE POSITIVES]; CONFIRM ch43 shows "all in the paired paragraph"/0 displaced, and align any keyed name/place/TERM to its glossary-decided rendering). qc_entities.py on a reconstructed bilingual (data/zh body lines [no ### headings here] + out/ch43_en.json, `> zh`/en pairs; every glossary row needs a pinyin field; WATCH a keyed term rendered as a VERB not the noun, cf. 绥靖/制裁). Verify the TAIL against the source (the very last paragraphs are the book's LAST words - verify explicitly per rule 4). check_register.py --ref reference/B01_frozen.md out/ch43_reading.md ("shall" deliberate).
4. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (full list in PROGRESS.md; the big already-covered furniture incl. the 制裁/sanction work, the Nationalist 绥靖/戡乱/共匪 framing, the Juntong/Baomiju, the Republican-year system, the five-part structure of the memoir). The Afterword is reflective and late - probably FEW new notes (0-3); be generous only where a Western reader would genuinely miss something, do NOT pad, do NOT re-note. Merge notes via apparatus_merge.py (positional arg: apparatus_merge.py data/ch43_apparatus.json; numeric character references only in note bodies; anchors verbatim ASCII substrings of the reading.md body text, NO em dash and NO quote/apostrophe; multi-occurrence anchors attach at the first). Add any glossary rows BY HAND into the sectioned glossary.json (idempotent + re-read-verified, every row with a pinyin field; scripts/add_ch42_glossary.py is the latest by-hand pattern, asserting each hanzi key against data/zh). For any CJK in a note body use the make_ch42_apparatus.py pattern (author bodies with typed hanzi + untoned pinyin, ASSERT every non-ASCII glyph is present in data/zh/ch43.txt, then convert to NCRs). Confirm ch43's image count (grep <img>; ch32-ch42 carried none).
5. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck if available (jar at /tmp/epubcheck-5.1.0/epubcheck.jar; re-run setup.sh per session). ⚠ THIS IS THE WHOLE-BOOK COMPLETION BATCH (CLAUDE.md "Definition of done"): with all 43 chapters now translated, the builder's pending-aware TOC should be CLEAN (43/43, no "pending" placeholder) and the coverage sentence complete - CONFIRM. Run the whole-book reconciliation: check_reconcile.py (repeated-compound rendering drift, glossary-forward usage, spelling-locale pairs) + BY HAND grep-count ~20 decided renderings and confirm notes at first appearance. Address the reconciliation items in PROGRESS/HANDOFF "Open items" (chiefly 张垣 = "Zhangjiakou" in ch08 vs "Zhangyuan" in ch39/ch41/ch42 - decide a whole-book policy and apply, or footnote once; ch09 "Jize County"; the pinyin-vs-postal city names; the documented homograph false positives). Feed the decided renderings back into authority.json. Write out/term_ledger.md (per CLAUDE.md), out/deep_audit.md (a 3-5% random-sample deep audit, fixed seed, honest error-rate statement), and COMPLETION.md (per the scanned template). Commit the final EPUB (git add -f out/nameless-heroes.epub). Rewrite HANDOFF.md to COMPLETE (the completion notice, NOT a next-kickoff) and do NOT touch it after. Record all check results in PROGRESS.md; commit and push to claude/nameless-heroes.

End with the final chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and - since this is the LAST batch and there is no next batch - a COMPLETION NOTICE in place of the kickoff block (the whole book is done: 43/43 chapters, both note streams complete, qa_epub + epubcheck green, COMPLETION.md written). Cite chapters and sections, never pages. Do not pause for approval mid-batch.
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
- **Batch B25 (ch32), OPENS PART FOUR.** ch32 (自序) = the Part-Four self-preface. 10 notes.
- **B26-B34 (ch33-ch41). The first NINE Part-Four narrative chapters. DONE.** Detail in PROGRESS.md.
- **Batch B35 (ch42), the TENTH and LAST full Part-Four NARRATIVE chapter.** 第十章 落叶归根 善其始终
  "Chapter 10. Fallen Leaves Return to the Root, Seen Through to the End" - the disbanding of the
  Pacification Corps and the diaspora of its men: Chen's own leave-taking and the 镇反-era deaths of
  Jiang Tian and Zhang Zuoxing, the reorganization into the Youth National-Salvation Corps, the
  Shanghai drift; the stay-behind men's flight out of besieged Beiping (Zhang Luying's and Liu
  Yuanshen's contributed accounts); the southward journey guarding Chiang's home region at Xikou
  (Wang Hongzhu's, Feng Zhijun's [小灵峰衞戍记], Xiao Runyu's and Wu Chunxiang's accounts) to the
  disbanding at Penghu; and Chen's post-1949 course (the unnamed "great power" cooperation from Hong
  Kong, the Japan mission, the chief-of-Second-Section post, the reunion). Closes with a DELIBERATE
  RING COMPOSITION (opening prose appraisal L3-L9 echoed as an enumerated close L201-L207; L8==L206
  identical, rendered identically). drop=2; 1 <h2> + 4 <h3> (section heads 一/二/三/四 at raw
  L13/L64/L105/L161) + 201 <p>, byte-exact p-by-p, standalone=[13,64,105,161], ONE glitch-masked
  sever merges=[(9,10)] (尽职！之外, the spurious ！ masking a 之外-postposition split), NO
  source-injection. 200 body paragraphs; median ratio 5.27. 10 notes (371 cumulative); 6 net-new
  keyed rows (1 person 冯志俊 Feng Zhijun [graduated from inline]; 5 places 溪口 Xikou/奉化 Fenghua/
  小灵峰 Xiaolingfeng/澎湖 Penghu/马公 Magong). check_content 0 displaced (aligned 3 keyed near-misses:
  张作兴 named not elided, 乌兰华->Ulanhua, 中岛信一 curly->straight apostrophe); qc 0 misses (fixed 1
  verb-form 绥靖 -> the noun "Pacification"); register within tolerance. qa_epub PASS; epubcheck
  0/0/0/0. 8 noise additions (坐六望七, 火冒三丈, 几两金子, 两黄金, 千方, 千丈岩, 30搭机, 十x日). **EPUB
  now 42/43 chapters, 371 notes.** Detail in PROGRESS.md ("Batch B35").

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` - derives data/zh/<id>.txt verbatim from data/src, applying per-unit
  drops/merges/heading-splits with a source-conservation check. Specs for ch01-ch42. Merge logic
  FOLLOWS CHAINS. **drop is variable:** most chapters drop=2; ch01/ch10/ch20/ch32 drop=3 (a part
  super-title precedes the preface). `standalone` = a sub-heading kept as its own line with no
  heading markup, emitted as `### ` (used for both plain-<p> sub-heads AND separate <h3> section
  elements, cf. ch33-ch42's <h3> section heads); `glued` = a heading fused onto a paragraph's
  TAIL; `glued_head` = a heading fused onto a paragraph's HEAD; `merges` = source <p> pairs that
  sever one sentence, AND can be MASKED by a glitch (scan ！？》-ending lines, not just non-terminal
  ones - ch42 L9/L10 had a spurious ！ masking a 之外-postposition split). **A chapter can carry
  INNER enumerated 一、二、三 / 第一、第二 / 其一、其二 DOCUMENT-CLAUSE or NUMBER-RANGE or NAME-LIST or
  OPTION-LIST content that is NOT a section heading - keep those as ordinary body lines per parity,
  judged by function** (ch27-42; ch42's section-1 and section-4 three-point self-reflections and the
  stay-behind decision/recollection points [glitch markers 川/口/囝/〕2/30 for 一/二/三] were kept as
  body lines). **⚠ ch36 taught a SOURCE-DUPLICATION class; ch42's L8==L206 echo is DELIBERATE ring
  composition (NOT an artifact) - both kept, rendered identically.**
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
  HOMOGRAPH FALSE POSITIVE**; **ch41's 河内/Hanoi HOMOGRAPH FALSE POSITIVE** (河内 = the substring of
  护城河内墙 "the moat's inner wall"). The pass criterion for a NEW batch is "the batch's own unit shows
  all name occurrences in the paired paragraph / 0 displaced." A NEW unit's TRUE displacements are
  almost always a keyed name/place/TERM rendered a DIFFERENT way than the glossary: align the English
  to the keyed form (B35: 张作兴 elided->named, 乌兰华 Wulanhua->Ulanhua, 中岛信一 curly->straight
  apostrophe). **Do NOT key a place/term whose hanzi is a substring of a DIFFERENT keyed rendering.
  ⚠ Do NOT key hanzi that renders DIFFERENTLY in another already-shipped chapter (cross-chapter
  conflict): grep the other chapters' data/zh AND their reading.md first (B35 keyed 溪口/奉化/小灵峰/
  澎湖/马公 only after verifying each renders one way everywhere).** Do NOT add book-TITLE or
  COMMON-NOUN keys.
- Glossary is authored/merged BY HAND into the SECTIONED file (book/people/organizations/places/
  terms), a dict keyed by hanzi, idempotent + re-read-verified. **Every row MUST carry a `pinyin`
  field** - qc_entities does `rec["pinyin"]` and KeyErrors otherwise. `scripts/add_ch42_glossary.py`
  is the latest by-hand pattern: covers people/places in one pass, asserts each hanzi key is a
  substring of that unit's data/zh/<id>.txt. **⚠ If a keyed name/place contains an apostrophe, set
  the glossary `en` to the CURLY-apostrophe form the reading.md renders, or check_content/qc will
  miss it** (新保安 en = "Xinbao’an"). apparatus_merge's glossary path assumes a FLAT map and would
  corrupt the sectioned file; NOTES still go through apparatus_merge.py.
- **qc_entities catches term-rendering drift too:** a glossary common-noun/term rendered a different
  way (or as a VERB not the noun) flags as a "miss." Align the English to the glossary (B26/B30/B32/
  B35: 绥靖 keyed "pacification" flagged when rendered the verb "pacify"/"pacifying").
- **make_ch42_apparatus.py pattern (scripts/):** author note bodies as plain ASCII + typed hanzi +
  UNTONED pinyin + straight quotes, allow em-dash, ASSERT every non-ASCII glyph occurs in THAT UNIT's
  data/zh/<id>.txt, then convert every non-ASCII char to a numeric char ref and run apparatus_merge.py.
  **A CORRECT glyph may be ABSENT if the source prints a glitch/variant** - describe such terms with
  the source's own form + pinyin/English (the ch42 万岁/万税 pun's glyphs happened all to be present).
- **⚠ ENUMERATION MARKERS carry a numeral the checker reads.** Render list ordinals as spelled
  ordinals ("First/Second/Third", cf. ch34/ch42) or arabic "(1)(2)(3)", NOT roman "(i)(ii)(iii)":
  roman markers do not carry the value and flag as unaccounted. Glitch-marked items with no source
  numeral rendered as arabic are safe/target-only (the checker is source->target only).
- **data/noise.txt** carries the B01-B35 project noise rules (each with a comment line). Republican
  years render literally; the checker matches the source numeral (or auto-escapes Republican-year
  N via N+1911). **SPELLED-OUT COMPOUNDS DO NOT COMPOSE** (target "three thousand five hundred" =
  {3000,500}, not 3500): write exact multi-part counts as DIGITS. **ORDER MATTERS:** a longer numeral
  idiom must precede a shorter one that is its prefix. **⚠ ORPHAN-STRIP LESSON (B35):** an existing
  SHORTER rule may strip part of your compound FIRST, orphaning a digit - a full-compound rule then
  never matches. Noise the RESIDUAL form instead (千方 after the existing 百计 strips it in 千方百计;
  两黄金 after the existing 三、五十 strips it in 三、五十两黄金). Idiom numerals, name-numeral glyphs,
  approximate ranges, place-name numerals, counter-by-naming and measure-word (两 tael after 几)
  forms are noised. ○ (U+25CB) / 〇 (U+3007) / × redaction artifacts: noise the mis-read glyph-string,
  carry the real value in English.
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches it; re-run per session).
  setup.sh's ONE failing regression test ("hook stands down on template stub") is a KNOWN false
  alarm; all other regression tests pass.

## Renderings settled / carry-forward

- 军统 / 军统局 -> "the Juntong" / "the Juntong Bureau" (DECIDED). 保密局 -> "the Baomiju" (DECIDED, B26).
  戴笠 Dai Li (courtesy Yunong; 老板 "the Boss"; 戴先生 "Mr. Dai"). 制裁 "sanction". 敌伪 "the enemy and
  the puppets"; 沦陷区 "the fallen zone(s)". Chiang's titles: 校长 "the Commandant", 委员长/委座 "the
  Generalissimo", 总裁 "the Director-General"; 领袖 "the Leader"; 总理 "the Party Leader" (Sun Yat-sen);
  蒋公/蒋主席/总统 "His Excellency Chiang"/"Chairman Chiang"/"the President"; 先总统蒋公 "the late President
  His Excellency Chiang". 三民主义 "the Three Principles of the People."
- **PART-FOUR vocab (reuse):** 总队 "Corps" / 总队长 "Corps Commander"; 大队 "brigade" / 大队长 "brigade
  commander" / 大队附 "brigade adjutant"; 中队 "company"; 分队 "sub-brigade"; 区队 "district company" /
  区队长 "district-company commander"; 小组 "small group" / 小组长 "group leader"; 指挥室 "command room";
  指挥员 "commanding officer" vs 指挥官 "commander"; 突击队 "assault team"; 直属 "directly subordinate";
  编制 "establishment"; 留置工作 "stay-behind work"; 绥靖 "pacification" (KEYED noun, NOT the verb
  "pacify") / 戡乱 "suppression of rebellion" / 剿匪 "bandit-suppression" / 匪谍 "Communist spies" / 共酋
  "Communist chieftains" / 共干 "Communist cadres" / 共匪 "the Communist bandits"; 华北剿总 "the North
  China Bandit-Suppression Headquarters". 特种部队 "special-operations unit" / 特种组织 "special
  organization". 青年救国团 "the Youth National-Salvation Corps" (胡轨 Hu Gui as director-general);
  戡建总队 "the Suppression-and-Reconstruction Corps"; 人民服务总队 "the People's Service Corps"; 政治营
  "the Political Battalion"; 马公要塞守备团 "the Magong Fortress Garrison Regiment" (B35).
- **B35 shelf (ch42; keyed):** person 冯志俊 Feng Zhijun (小灵峰衞戍记 author; graduated from inline in
  ch41); places 溪口 Xikou, 奉化 Fenghua, 小灵峰 Xiaolingfeng, 澎湖 Penghu, 马公 Magong (all decided;
  each renders one way across every chapter). Kept INLINE: 江田 Jiang Tian, 张作兴 Zhang Zuoxing (keyed
  earlier), 陶铸 Tao Zhu, 李运昌 Li Yunchang, 李鸣秋 Li Mingqiu, 聂恩俊 Nie Enjun, 白世维 Bai Shiwei,
  孙时林 Sun Shilin, 何思源 He Siyuan, 刘不同 Liu Butong, 李浩昆 Li Haokun, 吴尙游 Wu Shangyou, 胡轨 Hu Gui,
  梅长龄 Mei Changling, 马寿泉 Ma Shouquan, 黄文炳 Huang Wenbing, 李良荣 Li Liangrong, 乌瑞山 Wu Ruishan,
  汤恩伯 Tang Enbo, 李振清 Li Zhenqing, 孙文良 Sun Wenliang, 唐纵 Tang Zong, 韩尙英 Han Shangying, 曹霄青
  Cao Xiaoqing, 渡边渡 Watanabe Wataru, 和知鹰二 Wachi Takaji, 根本博 Nemoto Hiroshi. Places inline:
  上海/南京/杭州/宁波/绍兴/厦门/漳州/泉州/长泰/岩溪/林墩/青岛/基隆/台北/台中/香港/东京/北投/跑马地/惠安/
  高雄/白沙/蒋家 Jiangjia. Settled vocab: 镇压反革命/镇反 "the Suppression of Counter-Revolutionaries";
  提篮桥 "Tilanqiao"; 花雕/陈绍 "huadiao"/"chenshao" (Shaoxing wines); 乩童 "spirit-medium boy"; 白团
  "the White Group"; 某一大国 "a certain great power" (the US, footnoted); CAT "Civil Air Transport".
  乌兰华 -> "Ulanhua" (keyed form from 北国锄奸 ch04). 张垣 -> "Zhangyuan" inline (reconciliation item).
- **Book / part titles (in-text; DECIDED; reuse verbatim):** 英雄无名 = "Nameless Heroes"; Part One
  北国锄奸 = "Rooting Out Traitors in the North"; Part Two = "Disgrace at Hanoi"; Part Three 百战声威
  = "Renown Won in a Hundred Battles"; Part Four 平津地区绥靖戡乱 = "Pacification of the Beiping-Tianjin
  Region". 忠义救国军 = "the Loyal and Patriotic Army". Chen's own earlier volumes cited in-text:
  "Counter-Agent Work in the Latter Period of the War of Resistance" (抗战后期反间活动).
- **Earlier shelves (B15-B34)** remain in PROGRESS.md and prior HANDOFFs; the whole B02-B34 cast is
  keyed. Consult glossary.json before romanizing anything.

## Voice sheet - CHEN GONGSHU (author / narrator)

- REGISTER: educated, formal, essayistic first person; grave and a touch archaic but not stilted.
  Long semicolon-joined clauses; four-character idiom and classical allusion used freely and
  footnoted when they carry weight. Refers to himself as 笔者 "the writer" and 我 "I." His narrating
  "shall" is DELIBERATE - do not de-formalize it; check_register flags it informationally.
- STANCE: self-justifying yet self-effacing; insists on truthfulness, admits his blunders; tender
  toward dead comrades, bitter and scornful toward the enemy and the Communists. **Part Four is the
  1946-49 civil war and its aftermath: the Nationalist idiom is at its sharpest (共匪, 绥靖戡乱, 匪谍,
  the Mao epithets) - PRESERVE it, footnote where contested, text stands.** ch42's section 4 and the
  Afterword (ch43) turn REFLECTIVE, looking back over the whole five-book memoir and Chen's own later
  intelligence career.
- **Contributed accounts.** Part Four quotes long first-person memoir-accounts by comrades (ch36-ch42).
  Keep these in a plain, vivid first person DISTINCT from Chen's own essayistic frame; Chen's inserted
  笔者附注 (writer's notes) return to his grave register. Set a long extracted account WITHOUT an outer
  quote layer (double quotes only for the account's own quoted terms/inner speech), the ch39/ch41/ch42
  method, to avoid unreadable nested guillemets. (The Afterword ch43 has NO contributed accounts.)
- Ratio ~4.55-4.78 en/han in NARRATIVE; prefaces denser (ch32 5.57); document/quote-heavy chapters run
  higher (ch33-ch42 = 5.15-5.58; ch42 5.27). Read the note, do not reset. Alignment/register are the
  gates, not the raw ratio.

## Voice sheets - principal & recurring cast (Part Four)

- **CHEN GONGSHU himself.** Commanded the First Brigade of the Pacification Corps in the
  Beiping-Tianjin region, 1946-49; also (against his will) leader of the Baomiju's Beiping directly
  subordinate section. After the disbanding: drifting in Shanghai, then Taiwan; the unnamed "great
  power" cooperation from Hong Kong (1949-), the Japan mission (1957-), chief of the Second Section of
  the Defense Ministry Intelligence Bureau (promoted major general 1960).
- **ZHENG JIEMIN (郑介民 / Mr. Zheng).** Chen's old Beiping-days superior; later director of the
  National Security Bureau. In ch42 he tells Chen "Better go first to Taiwan," and later recalls him
  from Japan.
- **LIU PEICHU (刘培初).** Corps Commander of the Pacification Corps; ascetic, hard-driving; in ch42
  he quietly gives the destitute Chen six taels of gold.
- **LI YULIN (李玉林).** Deputy brigade commander, "Fifth Brother"; took the brigade south to Penghu
  and struck root there, becoming Penghu county magistrate. The most accomplished of the band.
- **THE ACCOUNT-AUTHORS (Part Four):** WANG ZHAOFEN (王兆芬), ZHANG LUYING (张鲁颖), LIU YUANSHEN
  (刘原深), WANG HONGZHU (汪鸿翥), FENG ZHIJUN (冯志俊, 小灵峰衞戍记), XIAO RUNYU (萧润宇), WU CHUNXIANG
  (吴春祥).

## ⚠ Name trap RESOLVED (do not reopen): 陈邦国 / 郑邦国

The Hanoi action-team member the source spells 郑邦国 in ch13 and 陈邦国 in ch15/ch16/ch17 is ONE
man. RESOLVED to **Chen Bangguo (陈邦国)**. Use Chen Bangguo consistently.

## Where the book stands

- Part One (北国锄奸) COMPLETE (B01-B05). Part Two ("Disgrace at Hanoi") COMPLETE (B06-B13). Part
  Three ("Renown Won in a Hundred Battles" / 百战声威) COMPLETE (B14-B24).
- **Part Four ("Pacification of the Beiping-Tianjin Region") NEARLY COMPLETE: B25 = ch32
  (self-preface) DONE; B26-B34 = ch33-ch41 (the first NINE narrative chapters) DONE; B35 = ch42
  (第十章, the TENTH and LAST full narrative chapter) DONE.**
- **NEXT and LAST: B36 = ch43** = 英雄无名 篇后续话 "Afterword: Closing Remarks" - a SHORT reflective
  coda, NO sections. Structure CONFIRMED at B35: 1 <h2> + 32 <p>, NO <h1>/<h3>/<br/>/<img>/note-markers,
  0 images, drop=2. src 44_index-split-000-0042.txt. ⚠ 1-line count question to resolve with the
  byte-exact diff FIRST: raw 33 python-lines; drop=2 -> 31 NON-EMPTY body lines but the xhtml shows
  32 <p> (likely an empty <p> the extractor drops, OR an extractor-split). B36 is the WHOLE-BOOK
  COMPLETION batch (back matter, check_reconcile.py, authority.json feedback, term_ledger.md,
  deep_audit.md, COMPLETION.md, clean TOC, HANDOFF -> COMPLETE) per CLAUDE.md's "Definition of done".
- The frozen register reference is `reference/B01_frozen.md`.
- Sub-heading pattern: Part Four chapters ch33-ch42 carry book.json `sections` arrays (the <h3> section
  heads emit as `standalone ### `); ch43 (the Afterword) has NO sections. DISTINGUISH enumerated LIST
  items / document clauses / number-ranges / name-lists (kept as body lines per parity) from true
  section headings. Grep each new chapter p-by-p.
- WATCH for source anomalies: cuts, misplaced-「 glitches, corrupt/dropped-character phrases, dropped
  full stops, a STRAY glyph fused onto a title, stray ？/》/！/〞/" (often standing for a closing 」),
  the ○ (U+25CB) / 〇 (U+3007) and × redactions, name glitches, variant forms, pervasive
  single-character substitutions, enumeration-marker glitches, orphaned 。 at a <p> head, severed-<p>
  boundaries (MERGE; can be glitch-MASKED - ch42 had a spurious ！), AND the ch36-class SOURCE
  DUPLICATION (ch42's L8==L206 echo was DELIBERATE, not an artifact). Re-grep each batch's source for
  `\[\d+\]` note markers (none through B35).

## Open items for the read-through / completion (B36 = the completion batch handles these)

- Feed decided renderings back to authority.json on completion: 军统 "the Juntong"; 保密局 "the Baomiju";
  制裁 "sanction"; the full B02-B35 historical-name set; the Part-Four vocabulary.
- Japanese/Mongol name readings to firm up (incl. the Kanjurwa Khutukhtu's brother; and the B35
  Japanese ex-officers 渡边渡/和知鹰二/根本博).
- Provisional romanizations to firm up (glossary `provisional` rows, incl. 刘培初/计兆祥/冯志俊 and the
  B30-B34 people).
- Whole-book reconciliation items: ch09 "Jize County"; the pinyin-vs-postal city names; the two B20
  keyed-substring false positives (武汉卿 / 劳勃生路); ch38's 海防/Haiphong homograph; ch41's 河内/Hanoi
  homograph (substring of 护城河内墙 "the moat's inner wall"); **张垣 rendered "Zhangjiakou" in ch08 but
  "Zhangyuan" in ch39/ch41/ch42 (the literary vs modern name of the same city - decide a whole-book
  policy at reconciliation)**; the Malone spelling (ch30); the ch32 "Fifth Part" numbering discrepancy;
  the garbled deputy-chief-of-staff surname glyph 鿄 (ch36); the Mao-at-Anguo intelligence (ch36);
  杜心吾/杜心五 and 程艳秋/程砚秋 name-form variants (ch37); the 鲁英庆/鲁英尘/鲁英屡 name glitches (ch39,
  one man = Lu Yingqing); the 茶碇农场 "Chading Farm" reading (ch42).

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01-B35 builds (0/0/0/0). Source is a clean digital
  EPUB, predominantly simplified with residual variant glyphs and pervasive digitization glitches
  (list them, render to plain sense, do not footnote mechanical typos). B01-B35 glitch lists in
  PROGRESS.md.
- Running-header line 英雄无名-陈恭澍 opens all 43 content files: drop it. drop count is variable -
  most drop=2; ch01/ch10/ch20/ch32 drop=3.
- Enumerated ；/：/、 bullet lists, quoted-document/directive/roster lines (INCLUDING inner
  document-clause / range / name-list / option-list / 一、二、三 / 其一、其二 lists), salutations, verse
  lines, run-in section labels, and 『』/「」-closed dialogue are DELIBERATE separate lines - do NOT
  merge them; only genuine mid-phrase splits (last char not terminal, OR a source <p> boundary that
  severs one sentence - possibly MASKED by a glitch ！/？/》 for 」) merge, and those can CHAIN.
- Faithful numbering gaps/anomalies (NOT errors): Part Three skips 第七章 (ch27 = 第八章); 第十章 splits
  into (上)/(下) (ch29/ch30); 三面受敌 一往无前 titles two chapters; ch32 numbers the Beiping-Tianjin
  volume "the Fifth Part" though Shanghai was "the Third Part" (footnoted). Preserve and footnote.
- Expect a stray per-task branch at the top of every batch; consolidate onto claude/nameless-heroes
  per rule 2.
