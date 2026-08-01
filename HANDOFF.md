# HANDOFF — The Autobiography of Huang Mulan

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Huang Mulan B07 — ch17-ch19 (Ch 17. Moving to Hong Kong; Ch 18. Thirty Days a Refugee; Ch 19. A Righteous Rescue of the Worthies). No part poem in this batch (Part Three runs ch13-ch21).

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then book.json, then HANDOFF.md. We are translating The Autobiography of Huang Mulan (黄慕兰自传) into an annotated English EPUB per CLAUDE.md. Work only on branch claude/huang-mulan; build the deliverable at out/The Autobiography of Huang Mulan.epub and present it in chat as an attached file.

Scope reminder (approved): translate ONLY the front matter (ch00), chapters 1-21 (ch01-ch21), and the appendices (ch39-ch43). Chapters 22-38 are out of scope and MUST stay as pending skeleton pages; do not translate or delete them. Batch target is 21,000 source chars max.

B01 (ch00-ch03), B02 (ch04-ch06), B03 (ch07-ch09), B04 (ch10-ch11), B05 (ch12-ch14) and B06 (ch15-ch16) are DONE and committed (see PROGRESS.md). Do Batch B07 = ch17-ch19 (Ch 17. Moving to Hong Kong; Ch 18. Thirty Days a Refugee; Ch 19. A Righteous Rescue of the Worthies), end to end:
1. Regenerate the extracted source if data/src/ is absent (it is gitignored): run scripts/ingest_epub.py source.epub. Read the batch's source from data/src/ (ch17=24_index-split-022.txt, ch18=25_index-split-023.txt, ch19=26_index-split-024.txt). Translate to the register in CLAUDE.md, faithfully and in full. Quote the source VERBATIM in the bilingual QC file: write out/<id>_en.txt (one English paragraph per line, first line = English chapter title), then reuse scripts/gen_bilingual_b02.py (add ch17/ch18/ch19 to its DROP map with the 1-indexed NON-EMPTY line numbers of the header + title + any caption-only/inscription lines). It interleaves verbatim source with your English and asserts paragraph parity. Never invent bridging text; if a passage is genuinely ambiguous or the source is cut, footnote it and leave it visible.
2. NO part poem in B07. Parts remaining: Part Four opens at ch22 and Part Five at ch32, both OUT of scope.
3. Watch for spliced-in image captions (a caption, sometimes an inscription + 说明, dropped mid-paragraph): rejoin the narrative from its verbatim halves, route the photo to figures.json, and put any inscription/说明 in a footnote. Caption-only lines and roster lines (左起/前排…) go to figures.json, not the reading text. Cross-check images per chapter with `grep -o 'images/[0-9]*\.jpg' data/src_epub/index_split_0NN.html`; basenames map to data/figs/. ch17 (index_split_022) carries images 00045-00049; ch18 (index_split_023) carries NONE; ch19 (index_split_024) carries image 00050. (B06 used 00037-00044.)
4. Author out/<id>_bilingual.md per unit (source blockquote line tagged "> ", English beneath; chapter title tagged "## H2 <English title>"). Generate reading + parity with scripts/split_bilingual.py, then run scripts/check_numbers.py out/<id>_bilingual.md --noise data/noise.txt and scripts/check_structure.py --pairs data/zh/<id>.txt out/<id>_reading.md until both are clean. Extend data/noise.txt (source-side name/idiom numerals) and, if a spelled ordinal is missed, WORD_NUM in check_numbers.py, when a flag is a non-quantity; carry every real quantity. NB: the target-side check counts "a hundred"/"a thousand"/"one thousand"/"N thousand"/"N hundred"/teens+"hundred"/"ten thousand"/"N million" but NOT a bare "the hundred"/"the thousand", NOT teen+thousand ("fifteen thousand"), and NOT tens-ones ordinals ("twenty-ninth","forty-fifth") -- for those write the digits (15,000 / 29th / 45th). check_numbers strips thousands separators, so write big numbers with commas as normal.
5. Blind double-translation and back-translation on the argumentative/literary passages (use subagents in fresh context); fact-check names/dates/events against real scholarship (Wikipedia, Baidu Baike, academic sources; never Grok/Grokipedia or any AI-written source). Say corroborated / uncorroborated / contradicted in PROGRESS.md.
6. Add ~3 footnotes per chapter-equivalent to notes.json (keyed by unit id; XHTML bodies with NUMERIC character references; anchors must be verbatim substrings of the English reading prose -- mind that anchors spanning a straight quote need the exact "...,"" punctuation; recurring subjects get their note at FIRST appearance in the book). Extend glossary.json (one rendering per referent; reuse ALL prior decisions -- Kuomintang, Sun Yat-sen, Chiang Kai-shek, Whampoa, Zhou Enlai, He Xiangning, Song Qingling, Liu Shaowen, Pan Hannian, Chen Zhigao, A Ying, Guo Moruo, Zou Taofen, Shen Junru, Zhang Zonglin, Xu Guangping, Zhao Puchu, Kong Xiangxi, Du Yuesheng, Rao Jiaju, the Tuesday Dining Club, the Women's Comfort/Salvation Association, the author's name rows 黄彰定/慕兰/定慧, etc.). Place any images via figures.json (reuse images already in data/figs/).
7. Rebuild with scripts/build_reading_epub.py "out/The Autobiography of Huang Mulan.epub" (TOC stays fully linked; ch22-38 remain pending), run scripts/qa_epub.py until green.
8. Commit, present the EPUB to me directly as an attached file in this chat (not a git link), update PROGRESS.md, and rewrite HANDOFF.md whose first section is the ready-to-paste kickoff message for the NEXT batch (B08 = ch20-ch21), beginning with the label line "Huang Mulan B08".

Cite chapters and sections, never page numbers. Do not pause for approval mid-batch; run the whole batch and report back when it is built and QA-green, and paste the B08 kickoff message at the end of your reply.
```

Every batch kickoff message (here and in every future HANDOFF) MUST begin with a
label line "Huang Mulan B<nn>" naming the batch and its chapter scope, then a
blank line, then the standard "Read CLAUDE.md in full..." instructions.

## What is DONE (do not redo)

- Step 0 (ingest + survey): source ingested (53 spine docs, 105 images,
  254,900 chars). book.json is the logical structure; skeleton EPUB with a fully
  hyperlinked TOC; metadata wired for Kindle/Apple Books; qa_epub PASS.
- B01 = ch00-ch03. 19,695 source chars. Part One 临江仙 folded into ch01. 11
  footnotes. All checks green. See PROGRESS.md.
- B02 = ch04-ch06. 19,567 source chars. Part Two 临江仙 folded into ch05. 9
  footnotes (20 total), incl. the source's OWN endnote in ch05. ~37 glossary rows,
  5 figures. All checks green.
- B03 = ch07-ch09. 18,809 source chars. No part poem. 10 footnotes (30 total),
  incl. the source's OWN endnote in ch08. ~57 glossary rows, 3 figures. All green.
- B04 = ch10-ch11. 11,004 source chars. No part poem, NO images. 9 footnotes (39
  total), incl. the source's OWN TWO endnotes in ch11. All green.
- B05 = ch12-ch14. 18,752 source chars. Part Three 临江仙 folded into ch13. ch12's
  trailing 【注释】 block DROPPED. 10 footnotes (49 total). ~112 glossary rows. 14
  figures (00022-00030, 00032-00036; 00031 skipped). All green.
- B06 = ch15-ch16 (Resistance and National Salvation; Struggle on the Solitary
  Island). 17,874 source chars. No part poem. 7 footnotes (56 total; ch15 50-53,
  ch16 54-56). 165 glossary rows added (totals 342 people / 76 orgs / 49 places /
  14 terms). 8 figures (00037-00041 ch15, 00042-00044 ch16). Blind double-
  translation + back-translation + fact-check done: the 救国会 founding YEAR is
  wrong in the memoir (says 1931; scholarship 1936) -- rendered as written and
  footnoted; 饶家驹 = Robert Jacquinot de Besange, the "One-Armed Father"/Nanshi
  Safe Zone corroborated but his arm was lost in a 1914 fireworks accident, not WWI
  shellfire (memoir version footnoted as contradicted); the ch15/31 caption is
  mirror-reversed in the source and was decoded before translating; the ch15/8
  photo inscription quatrain went to a footnote. Build + qa_epub PASS (97 files,
  17 of 44 chapters, 378 paragraphs). Committed.

## What is NEXT

- B07 = ch17-ch19 (see kickoff above; no part poem). Then B08 ch20-ch21, B09
  ch39-ch43 (appendices). See book.json "batches".

## Reusable machinery (saves time)

- scripts/gen_bilingual_b02.py IS the bilingual generator: a DROP map of
  {unit: (src_file, {1-indexed NON-EMPTY lines to drop = header, title,
  captions, inscriptions})}, plus a POEM map for part-opening chapters. IMPORTANT:
  the DROP indices are 1-indexed over the file's NON-EMPTY lines (blank lines
  skipped) -- enumerate with
  `python3 -c "lines=[l for l in open(f) if l.strip()]; [print(i,l[:50]) for i,l in enumerate(lines,1)]"`.
  B06 added ch15 (drop header+title + captions 7,8,13,14,26,27,31) and ch16 (drop
  header+title + captions 9,10,31,32). B07 has no part poem, so POEM is untouched.
- Finding caption/inscription line numbers: caption-only lines in data/src are
  image captions (photo-caption lines, 原图片说明/封面照片说明 lines, 左起/前排/右起…
  rosters, person-bio lines) or an author's inscription (X为此照题诗云…). A two-line
  photo (title + roster) is ONE image: drop both, fold the roster into the figure
  caption. An inscription goes to a FOOTNOTE, not figures.json. Some source captions
  are MIRROR-REVERSED (printed backwards, e.g. ch15/31) -- decode before translating.
  Cross-check per chapter with `grep -o 'images/[0-9]*\.jpg' data/src_epub/index_split_0NN.html`;
  basenames map straight to data/figs/. Verify placement by grepping the built .xhtml
  for the image basename (the builder silently skips a figure whose "before" anchor is
  not within the FIRST ~80 chars of a reading paragraph). Used so far: B01 00002-00012,
  B02 00013-00018, B03 00019-00021, B04 none, B05 00022-00030 + 00032-00036 (00031
  skipped), B06 00037-00044. Next free: 00045.
- The SOURCE'S OWN endnotes: all four (ch05 [1], ch08 [2], ch11 [3]/[4]) are handled
  and live in ch12's DROPPED 【注释】 block. No in-scope chapter after ch12 has been
  found to carry a source endnote, but grep each unit's HTML for `<sup`/`filepos` to be
  sure (ch15/ch16 had only the chapter-title `<h2 id="filepos...">` -- not an endnote).
- data/noise.txt strips this book's recurring non-quantity numerals. B06 added 千秋,
  大千 (大千世界/张大千), 沙千里, 沈兹九, 星[二三四五] (Tuesday/Wed/Thu/Friday clubs),
  百科 (大百科全书), 八仙桥, 再而三. check_numbers.py NOISE also gained two general
  ordering-safe patterns AT THE TOP (before the generic 几+classifier / 几十 rules):
  r"[幾几][十百千][萬万]" (好几十万 -> stray 万=10000) and r"十[幾几][個个]" (十几个 ->
  stray 十=10). Longest-literal-first; do NOT re-sort the NOISE list.
- check_numbers target-side gotchas: it counts "a hundred"/"a thousand"/"one
  thousand"/"N thousand"/"N hundred"/teens+"hundred"/"ten thousand"/"N million" --
  but NOT a bare "the hundred"/"the thousand", NOT teen+thousand ("fifteen thousand"
  gives only 15), and NOT tens-ones ordinals ("twenty-ninth","forty-fifth" give only
  the tens). For those write the digits (15,000 / 25,000 / 29th / 45th). check_numbers
  _decomma strips thousands separators, so write grouped figures with commas.

## Open items / read-through flags

- book.json author_note still calls Huang Dinghui the "birth name"; the source and
  scholarship make 黄彰定 (Zhangding) the birth/school name, 慕兰 the 1926 name,
  定慧 a 1932 name (per ch12). Translation and glossary are correct; the metadata
  line is worth tidying in a later pass (does not affect the reading text).
- Allusive/subject title still to footnote when reached: 面谒周公 (ch20, 周公 =
  Zhou Enlai; the 周公/Lord Zhou honorific is footnoted at its first appearance in
  ch11, cross-referenced forward to the ch20 title).
- Faithfully-rendered source slips kept visible (not silently corrected): the 救国会
  founding YEAR (memoir 1931, scholarship 1936; ch15, footnoted); Father Rao's arm
  lost in a 1914 accident not WWI (ch15, footnoted); 俞楼's construction credited to
  Zeng Guofan (ch12, footnoted); Chen Fu "propaganda head" vs secretary-general;
  Guan Xiangying "deputy" vs full political commissar. All left as the author wrote.
- Provisional renderings to upgrade if a source turns up: 巴和/"Baho" (ch11 French
  lawyer); 许宝/"Xu Bao" (ch14, possibly truncated); the two 每日译报 British
  publishers 孙特士·斐士/"Sundius Fees" and 拿门·鲍纳/"Norman Bonner" (ch16, English
  names unverified, footnoted provisional); 张曼怡/"Zhang Manyi" (ch16, given as T.V.
  Soong's wife -- some sources give Zhang Leyi). If any is fixed, update glossary.json
  AND grep every built unit for the old form and rebuild.

## State / traps

- Scope is PARTIAL by instruction: ch00, ch01-ch21, ch39-ch43 only. ch22-ch38
  stay as pending skeleton pages (the build handles this; do not delete them).
- Part poems: Part One at ch01, Part Two at ch05, Part Three at ch13 (all DONE).
  Part Four opens at ch22 and Part Five at ch32, both out of scope.
- Note anchors go in BEFORE markup substitution (the builder inserts them and
  REFUSES on an unmatched anchor). XHTML note bodies use NUMERIC character
  references, never named entities. Numbering is continuous and builder-assigned
  in reading order (56 notes through ch16; ch15 = 50-53, ch16 = 54-56).
- Figure "before" anchors must be a substring within the FIRST ~80 characters of a
  paragraph line, or the builder silently skips the figure. A two-line photo caption
  (title + roster) is ONE figure. Verify placement by grepping the built .xhtml for
  the image basename.
- Deliverable filename is exactly out/The Autobiography of Huang Mulan.epub (with
  spaces). data/src/, data/src_epub/, data/figs/, out/*.epub are gitignored and
  rebuild from source.epub; commit the JSON, the reading/bilingual/en md, the
  generator + check scripts, PROGRESS/HANDOFF, data/zh, data/noise.txt.
- Work on ONE branch: claude/huang-mulan (per CLAUDE.md rule 2). If a session starts
  you on a stray branch, consolidate onto the working branch and delete the stray
  (local + remote). Pillow is needed for interior figures (pip install pillow on a
  fresh container) -- B06 had 8 figures, so it was installed.
