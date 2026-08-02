# HANDOFF — The Autobiography of Huang Mulan

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Huang Mulan B09 — ch39-ch43 (the appendices; the LAST batch): Appendix I. Afterword (后记); Appendix II. A Chronology of Huang Mulan's Life (黄慕兰生平大事表); Appendix III. A Brief Life of Comrade Liu Shaowen (刘少文同志简介); Appendix IV. My Grandmother, a Daughter of the Party (我的外婆 党的女儿); Editor's Postscript (编后记). No part poem. This FINISHES the commissioned scope.

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then book.json, then HANDOFF.md, then PROGRESS.md. We are translating The Autobiography of Huang Mulan (黄慕兰自传) into an annotated English EPUB per CLAUDE.md. Work only on branch claude/huang-mulan; build the deliverable at out/The Autobiography of Huang Mulan.epub and present it in chat as an attached file.

Scope reminder (approved): translate ONLY the front matter (ch00), chapters 1-21 (ch01-ch21), and the appendices (ch39-ch43). Chapters 22-38 are out of scope and MUST stay as pending skeleton pages; do not translate or delete them. B01-B08 (ch00-ch21) are DONE and committed (see PROGRESS.md). B09 = ch39-ch43 is the LAST batch.

Do Batch B09 = ch39-ch43 end to end:
1. Regenerate the extracted source if data/src/ is absent (it is gitignored): run scripts/ingest_epub.py source.epub, and pip install pillow if figures are placed. Read the batch's source from data/src/ (ch39=49_index-split-047.txt, ch40=50_index-split-048.txt, ch41=51_index-split-049.txt, ch42=52_index-split-050.txt, ch43=53_index-split-051.txt). Translate to the register in CLAUDE.md, faithfully and in full. Quote the source VERBATIM in the bilingual QC file: write out/<id>_en.txt (one English paragraph per line, first line = English title), then reuse scripts/gen_bilingual_b02.py (add ch39-ch43 to its DROP map with the 1-indexed NON-EMPTY line numbers of the header + title + any caption-only/roster/说明 lines). It interleaves verbatim source with your English and asserts paragraph parity. Enumerate non-empty lines with `python3 -c "lines=[l for l in open(f) if l.strip()]; [print(i,l[:60]) for i,l in enumerate(lines,1)]"`. Never invent bridging text; footnote genuinely ambiguous or cut passages and leave them visible.
2. NB ch40 (大事表) is a CHRONOLOGY -- a dense run of dated year/month entries; check_numbers will flag many. Carry EVERY real date/quantity as digits (years like 1907, 1926, 1957; day-ordinals 21st/22nd/25th need digits; tens-ones ORDINALS "twenty-ninth" need digits; but cardinal tens and tens-ones "forty-five"/"fifty" spell out fine -- see the check_numbers facts below). It is a table-like list; keep the source's line/entry structure (one entry per paragraph) and let paragraph parity hold. ch39 is only 184 chars (a short afterword); ch43 编后记 is the editor's postscript (labeled 附录四 in the source, duplicating ch42's label -- rendered as the editor's postscript, NOT renumbered; see book.json _source_note).
3. Watch for spliced-in captions/rosters/说明 as before: caption-only lines and roster lines (左起/前排…) go to figures.json, not the reading text; an inscription/说明 goes to a FOOTNOTE. Cross-check images per chapter with `grep -o 'images/[0-9]*\.jpg' data/src_epub/index_split_0NN.html` (ch39=047, ch40=048, ch41=049, ch42=050, ch43=051); basenames map to data/figs/. Next free figure basename after B08 is 00053 (B08 used 00051-00052 in ch21); verify per chapter with the grep.
4. Author out/<id>_bilingual.md per unit (source blockquote line tagged "> ", English beneath; chapter title tagged "## H2 <English title>"). Generate reading + parity with scripts/split_bilingual.py, then run scripts/check_numbers.py out/<id>_bilingual.md --noise data/noise.txt and scripts/check_structure.py --pairs data/zh/<id>.txt out/<id>_reading.md until both are clean. Extend data/noise.txt (source-side name/idiom numerals) and, if a spelled ordinal is missed, WORD_NUM in check_numbers.py, only when a flag is a non-quantity; carry every real quantity.
5. Blind double-translation and back-translation on any argumentative/literary passages (use subagents in fresh context); fact-check names/dates/events against real scholarship (Wikipedia, Baidu Baike, academic sources; never Grok/Grokipedia or any AI-written source). Say corroborated / uncorroborated / contradicted in PROGRESS.md. The chronology (ch40) is a rich fact-check surface -- verify its landmark dates.
6. Add ~3 footnotes per chapter-equivalent to notes.json (keyed by unit id; XHTML bodies with NUMERIC character references; anchors must be verbatim substrings of the English reading prose -- mind that anchors spanning a straight/curly quote need the exact punctuation; recurring subjects get their note at FIRST appearance in the book, so many people are already noted -- do NOT re-note them; check notes.json). Numbering continues from 74 (builder-assigned in reading order). Extend glossary.json (one rendering per referent; reuse ALL prior decisions -- Liu Shaowen, Zhou Enlai, Chen Zhigao, the author's name rows 黄彰定/慕兰/定慧, etc.). Place any images via figures.json (reuse images already in data/figs/).
7. Rebuild with scripts/build_reading_epub.py "out/The Autobiography of Huang Mulan.epub" (TOC stays fully linked; ch22-38 remain pending), run scripts/qa_epub.py until green.
8. THIS IS THE LAST BATCH. After ch39-ch43 are in: do any back matter (a colophon from back_matter.json if the book has one; the translator's note already renders from book.json translator_note -- review it) and run a WHOLE-BOOK QA pass (qa_epub green across the full spine; spot-grep the built units for glossary consistency of the recurring names; confirm ch22-38 are still pending skeleton pages and ch00/ch01-ch21/ch39-ch43 are all translated). Then, INSTEAD of another handoff kickoff, write a COMPLETION REPORT into HANDOFF.md (what was delivered, final counts: chapters translated, notes, figures, glossary rows; the open read-through flags carried from PROGRESS; anything the commissioner should know). Commit, and present the final EPUB to me directly as an attached file in this chat (not a git link).

Cite chapters and sections, never page numbers. Do not pause for approval mid-batch; run the whole batch and report back when it is built and QA-green, and paste the completion report at the end of your reply.
```

Every batch kickoff message (here and in every future HANDOFF) MUST begin with a
label line "Huang Mulan B<nn>" naming the batch and its chapter scope, then a
blank line, then the standard "Read CLAUDE.md in full..." instructions.

## What is DONE (do not redo)

- Step 0 (ingest + survey): source ingested (53 spine docs, 105 images,
  254,900 chars). book.json is the logical structure; skeleton EPUB with a fully
  hyperlinked TOC; metadata wired for Kindle/Apple Books; qa_epub PASS.
- B01 = ch00-ch03. 19,695 chars. Part One 临江仙 folded into ch01. 11 notes.
- B02 = ch04-ch06. 19,567 chars. Part Two 临江仙 folded into ch05. 9 notes (20 total).
- B03 = ch07-ch09. 18,809 chars. No part poem. 10 notes (30 total).
- B04 = ch10-ch11. 11,004 chars. No part poem, NO images. 9 notes (39 total).
- B05 = ch12-ch14. 18,752 chars. Part Three 临江仙 folded into ch13. 10 notes (49
  total). 14 figures (00022-00030, 00032-00036).
- B06 = ch15-ch16. 17,874 chars. No part poem. 7 notes (56 total). 8 figures
  (00037-00044). 救国会 founding YEAR wrong in the memoir (1931 vs scholarship 1936)
  -- footnoted; Father Rao's arm lost in a 1914 accident not WWI -- footnoted.
- B07 = ch17-ch19. 16,085 chars. No part poem. 10 notes (66 total). 6 figures
  (00045-00050). Fixed a 3-vs-2-person referent slip; Ho Chi Minh/Haiphong 1939
  anachronism footnoted; Chen Di-as-Zhongshan-captain unverified, footnoted.
- B08 = ch20-ch21 (An Audience with Zhou Enlai; Cast into Prison Together).
  17,413 chars (ch20 6,283; ch21 11,130). No part poem. 8 notes (74 total; ch20
  67-69, ch21 70-74). 2 figures (00051 1991 Detroit reunion, 00052 1946 Chen
  siblings -- both in ch21; ch20 has no images). 46 glossary rows (totals 421
  people / 105 orgs / 93 places / 23 terms). Two check_numbers.py bug fixes:
  (a) (?<!十) lookbehind on the 一+classifier NOISE rules so 十一年/十一个 read 11 not
  10; (b) 万一 added high in the built-in NOISE list so 万一路上 doesn't orphan a 万.
  data/noise.txt gained 万千, 港九, 四目, 十两. QC: blind double-translation +
  back-translation deep audit both clean (0 omissions/embellishments); fact-check
  footnoted 周夔龙->周伟龙 (name slip), the Ye Ting/Chiang piggyback (unverified),
  and the "14 base areas" figure (non-canonical; 19 is the 1945 count). Build +
  qa_epub PASS (105 files, 22 of 44 chapters, 462 paragraphs). Committed.

## What is NEXT

- B09 = ch39-ch43 (the appendices) -- the LAST batch (see kickoff above). After it,
  the commissioned scope (ch00, ch01-ch21, ch39-ch43) is COMPLETE. ch22-ch38 stay
  as pending skeleton pages by instruction. See book.json "batches".

## Reusable machinery (saves time)

- scripts/gen_bilingual_b02.py IS the bilingual generator: a DROP map of
  {unit: (src_file, {1-indexed NON-EMPTY lines to drop = header, title,
  captions, rosters, inscriptions})}, plus a POEM map for part-opening chapters.
  The DROP indices are 1-indexed over the file's NON-EMPTY lines (blank lines
  skipped) -- enumerate with
  `python3 -c "lines=[l for l in open(f) if l.strip()]; [print(i,l[:50]) for i,l in enumerate(lines,1)]"`.
  B08 added ch20 (drop 1,2 -- no images) and ch21 (drop 1,2,26,43,44,45). B09 has
  no part poem, so POEM is untouched.
- Finding caption/inscription line numbers: caption-only lines in data/src are
  image captions (photo-caption lines, 原图片说明/封面照片说明 lines, 左起/前排/后排…
  rosters, person-bio lines) or an author's inscription (X为此照题诗云…). A two-line
  photo (title + roster) is ONE image: drop both, fold the roster into the figure
  caption. An inscription goes to a FOOTNOTE, not figures.json. A caption that sits
  BETWEEN two complete paragraphs (both ending on a full stop, as in ch21) is a
  clean standalone -- just drop it; only a caption that splits a sentence (ch03)
  needs the narrative rejoined from its verbatim halves. Cross-check per chapter
  with `grep -o 'images/[0-9]*\.jpg' data/src_epub/index_split_0NN.html`; basenames
  map straight to data/figs/. Verify placement by grepping the built .xhtml for the
  image basename (the builder silently skips a figure whose "before" anchor is not
  within the FIRST ~80 chars of a reading paragraph -- so prefer an anchor from the
  START of the paragraph, ideally with no apostrophe). Used so far: B01 00002-00012,
  B02 00013-00018, B03 00019-00021, B04 none, B05 00022-00030 + 00032-00036 (00031
  skipped), B06 00037-00044, B07 00045-00050, B08 00051-00052. Next free: 00053.
- The SOURCE'S OWN endnotes: all four (ch05 [1], ch08 [2], ch11 [3]/[4]) are handled
  and live in ch12's DROPPED 【注释】 block. No in-scope chapter after ch12 has been
  found to carry a source endnote (ch15-ch21 checked: only the chapter-title
  `<h2 id="filepos...">`), but grep each unit's HTML for `<sup`/`filepos` to be sure.
- data/noise.txt strips this book's recurring non-quantity numerals. B08 added 万千
  (思绪万千), 港九, 四目 (四目对视), 十两 (十两黄金 -- 两/tael reads as 2, merges 十两->12,
  like B04's 一百两; carry the ten-tael quantity in the reading text). Longest-literal
  -first; do NOT re-sort the NOISE list.
- check_numbers.py fixes from B08 (both GENERAL, verified no regression): (a) the two
  measure-word NOISE patterns r"一[...]" now begin r"(?<!十)一[...]" so a 一 that is
  part of 十一/二十一 is not stripped (十一年 -> 11, was 10). (b) r"万一" was inserted
  near the TOP of the built-in NOISE list (right after the fractions rule, BEFORE the
  一[classifier] block) so 万一 strips whole before the 一路 rule can orphan the 万.
- check_numbers target-side facts (verified by reading the script): spelled_numbers
  DOES count cardinal tens ("fifty"->50) and cardinal tens-ones ("forty-five"->45),
  and "over/past <tens>" ("over fifty"->50), and "a hundred"/"a thousand"/"one
  thousand"/"N thousand"/"N hundred"/teens+"hundred"/"ten thousand"/"N million". It
  does NOT count tens-ones ORDINALS ("twenty-ninth","forty-fifth" give only the tens)
  or plural tens ("sixties" -- use singular "sixty or seventy" for 60/70), nor
  teen+thousand ("fifteen thousand" gives only 15). For those, and for day-ordinals
  (21st/22nd/25th), write the digits. _decomma strips thousands separators, so write
  grouped figures with commas as normal. The ch40 chronology will lean on all of this.

## Open items / read-through flags

- book.json author_note still calls Huang Dinghui the "birth name"; the source and
  scholarship make 黄彰定 (Zhangding) the birth/school name, 慕兰 the 1926 name,
  定慧 a 1932 name (per ch12). Translation and glossary are correct; the metadata
  line is worth tidying in a later pass (does not affect the reading text). The ch40
  chronology is a natural place to CONFIRM the name/date timeline against the body.
- Faithfully-rendered source slips kept visible (not silently corrected), all
  footnoted: the 救国会 founding YEAR (memoir 1931, scholarship 1936; ch15); Father
  Rao's arm lost in a 1914 accident not WWI (ch15); "Chairman Ho Chi Minh"/Haiphong
  1939 (ch17, anachronistic); Chen Di as captain of the Zhongshan (ch18, unverified);
  周夔龙/Zhou Kuilong likely a slip for 周伟龙/Zhou Weilong (ch21); the Ye Ting-carried
  -wounded-Chiang anecdote (ch21, unverified); the "fourteen base areas" figure (ch20,
  non-canonical). Also left as the author wrote (un-footnoted minor points): 俞楼's
  construction credited to Zeng Guofan (ch12); Chen Fu "propaganda head" vs
  secretary-general (ch07/08); Guan Xiangying "deputy" vs full political commissar
  (ch10). B07 fixed a 3-vs-2-person referent slip (国母孙夫人和廖夫人 = TWO people).
- Provisional renderings to upgrade if a source turns up: 巴和/"Baho" (ch11); 许宝/
  "Xu Bao" (ch14); the two 每日译报 publishers "Fees"/"Bonner" (ch16); 张曼怡/"Zhang
  Manyi" (ch16); and the one-off names flagged "provisional" in glossary.json,
  including B08's Xu Jingwei, Zhou Kuilong (likely Zhou Weilong), Chen Youdan, Zhang
  Fusheng, Wang Yukun, Ge Xiuluan, Jiang Zhicheng, Zhang Ruichu, Chen Xinzhu, Huiqing,
  Guo Fajin, Chen Tingxiang, Liying, Chen Yingu, Wan Changjie, Wan Xikan, Hu Nanhu.
  If any is fixed, update glossary.json AND grep every built unit for the old form
  and rebuild. ch41 (刘少文简介) is a good place to cross-check Liu Shaowen's dates.

## State / traps

- Scope is PARTIAL by instruction: ch00, ch01-ch21, ch39-ch43 only. ch22-ch38
  stay as pending skeleton pages (the build handles this; do not delete them).
- Part poems: Part One at ch01, Part Two at ch05, Part Three at ch13 (all DONE, all
  in scope). Part Four opens at ch22 and Part Five at ch32, both OUT of scope, so
  B09 (the appendices) has NO part poem.
- Note anchors go in BEFORE markup substitution (the builder inserts them and
  REFUSES on an unmatched anchor). XHTML note bodies use NUMERIC character
  references, never named entities. Numbering is continuous and builder-assigned
  in reading order (74 notes through ch21; ch20 = 67-69, ch21 = 70-74). Recurring
  subjects are noted at FIRST appearance, so most major figures are already noted --
  do NOT re-note; check notes.json before adding.
- Figure "before" anchors must be a substring within the FIRST ~80 characters of a
  paragraph line, or the builder silently skips the figure. Prefer an anchor from the
  paragraph start with no apostrophe. A two-line photo caption (title + roster) is ONE
  figure. Verify placement by grepping the built .xhtml for the image basename.
- Deliverable filename is exactly out/The Autobiography of Huang Mulan.epub (with
  spaces). data/src/, data/src_epub/, data/figs/manifest.json, out/*.epub,
  out/*_bilingual.md are gitignored and rebuild from source.epub; commit the JSON,
  the reading/en md, data/zh, data/noise.txt, the generator + check scripts,
  PROGRESS/HANDOFF. (data/figs/*.jpg|png ARE tracked.)
- Work on ONE branch: claude/huang-mulan (per CLAUDE.md rule 2). If a session starts
  you on a stray per-session branch, consolidate onto claude/huang-mulan and delete
  the stray (local + remote). B08 (like B02/B04/B07) started on a stray branch that
  pointed at the same commit; reset local claude/huang-mulan to origin and worked
  there. Pillow is needed for interior figures (pip install pillow on a fresh
  container).
