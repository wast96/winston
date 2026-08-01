# HANDOFF — The Autobiography of Huang Mulan

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Huang Mulan B05 — ch12-ch14 (Ch 12. In Seclusion by West Lake; Ch 13. The Voice of Justice; Ch 14. The Tongyi Company). Ch 13 OPENS Part Three.

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then book.json, then HANDOFF.md. We are translating The Autobiography of Huang Mulan (黄慕兰自传) into an annotated English EPUB per CLAUDE.md. Work only on branch claude/huang-mulan; build the deliverable at out/The Autobiography of Huang Mulan.epub and present it in chat as an attached file.

Scope reminder (approved): translate ONLY the front matter (ch00), chapters 1-21 (ch01-ch21), and the appendices (ch39-ch43). Chapters 22-38 are out of scope and MUST stay as pending skeleton pages; do not translate or delete them. Batch target is 21,000 source chars max.

B01 (ch00-ch03), B02 (ch04-ch06), B03 (ch07-ch09) and B04 (ch10-ch11) are DONE and committed (see PROGRESS.md). Do Batch B05 = ch12-ch14 (Ch 12. In Seclusion by West Lake; Ch 13. The Voice of Justice; Ch 14. The Tongyi Company), end to end:
1. Regenerate the extracted source if data/src/ is absent (it is gitignored): run scripts/ingest_epub.py source.epub. Read the batch's source from data/src/ (ch12=18_index-split-016.txt, ch13=20_index-split-018.txt, ch14=21_index-split-019.txt). Translate to the register in CLAUDE.md, faithfully and in full. Quote the source VERBATIM in the bilingual QC file: write out/<id>_en.txt (one English paragraph per line, first line = English chapter title; for ch13, lines 2..n = the Part Three 临江仙 poem as italic epigraph lines, matching the ch05 pattern), then reuse scripts/gen_bilingual_b02.py (add ch12/ch13/ch14 to its DROP map with the header/title/caption line numbers, and add ch13 to the POEM map). It interleaves verbatim source with your English and asserts paragraph parity. Never invent bridging text; if a passage is genuinely ambiguous or the source is cut, footnote it and leave it visible. (B03's parity check caught an invented recap paragraph in ch09 this way -- trust the check.)
2. PART THREE POEM: Part Three opens at ch13. Fold the Part Three 临江仙 ci from index_split_017.html into ch13 as an italic epigraph at the chapter head (book.json already has ch13 part_poem_src=index_split_017.html). Read the poem lines VERBATIM from data/src/19_index-split-017.txt via the POEM map (title + stanza lines), exactly as B02 did for the Part Two poem in ch05. NOTE: ch12 (index_split_016.html) is the file that also holds the 【注释】 endnote blocks the earlier chapters linked to (ch05 [1], ch08 [2], ch11 [3]/[4]) -- when translating ch12, watch for its OWN body text vs. that trailing 注释 apparatus; the注释 block belongs to the endnotes already rendered, not to ch12's reading text (grep the html to see where ch12's prose ends).
3. Watch for spliced-in image captions (a caption, sometimes an inscription + 说明, dropped mid-paragraph): rejoin the narrative from its verbatim halves, route the photo to figures.json, and put any inscription/说明 in a footnote. Caption-only lines go to figures.json, not the reading text. Cross-check images per chapter with `grep -o 'images/[0-9]*\.jpg' data/src_epub/index_split_0NN.html`; basenames map to data/figs/. (B04 ch10/ch11 had NO images; earlier batches used 00002-00021.)
4. Author out/<id>_bilingual.md per unit (source blockquote line tagged "> ", English beneath; chapter title tagged "## H2 <English title>"; poem lines for ch13 as their own paragraph lines). Generate reading + parity with scripts/split_bilingual.py, then run scripts/check_numbers.py out/<id>_bilingual.md --noise data/noise.txt and scripts/check_structure.py --pairs data/zh/<id>.txt out/<id>_reading.md until both are clean. Extend data/noise.txt (source-side name/idiom numerals) and, if a spelled ordinal is missed, WORD_NUM in check_numbers.py, when a flag is a non-quantity; carry every real quantity. check_numbers now strips thousands separators, so grouped figures like "2,500,000" read as one number -- write big numbers with commas as normal.
5. Blind double-translation and back-translation on the argumentative/literary passages (use subagents in fresh context); fact-check names/dates/events against real scholarship (Wikipedia, Baidu Baike, academic sources; never Grok/Grokipedia or any AI-written source). Say corroborated / uncorroborated / contradicted in PROGRESS.md.
6. Add ~3 footnotes per chapter-equivalent to notes.json (keyed by unit id; XHTML bodies with NUMERIC character references; anchors must be verbatim substrings of the English reading prose; recurring subjects get their note at FIRST appearance in the book). Extend glossary.json (one rendering per referent; reuse ALL prior decisions -- Kuomintang, Sun Yat-sen, Chiang Kai-shek, Whampoa, Zhou Enlai, Chen Duxiu, He Chang, Chen Tanqiu, Rao Shushi, Guan Xiangying, Pan Hannian, Chen Geng, Chen Zhigao, Chen Qishou/Jieqing, Xiang Zhongfa, Gu Shunzhang, Kang Sheng, Dong Zhujun, the author's name rows 黄彰定/慕兰/定慧, etc.). Place any images via figures.json (reuse images already in data/figs/).
7. Rebuild with scripts/build_reading_epub.py "out/The Autobiography of Huang Mulan.epub" (TOC stays fully linked; ch22-38 remain pending), run scripts/qa_epub.py until green.
8. Commit, present the EPUB to me directly as an attached file in this chat (not a git link), update PROGRESS.md, and rewrite HANDOFF.md whose first section is the ready-to-paste kickoff message for the NEXT batch (B06 = ch15-ch16), beginning with the label line "Huang Mulan B06".

Cite chapters and sections, never page numbers. Do not pause for approval mid-batch; run the whole batch and report back when it is built and QA-green, and paste the B06 kickoff message at the end of your reply.
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
  footnotes (20 total), incl. the source's OWN endnote in ch05 (Wan Xiyan death
  discrepancy). ~37 glossary rows, 5 figures. All checks green. See PROGRESS.md.
- B03 = ch07-ch09. 18,809 source chars. No part poem. 10 footnotes (30 total),
  incl. the source's OWN endnote in ch08 (Wan Xixian, Mao's Selected Works). ~57
  glossary rows, 3 figures (00019-00021). ch09 title corrected to "Head of the
  Rescue Department". All checks green. See PROGRESS.md.
- B04 = ch10-ch11 (Victory in the First Battle; The "Wu Hao" Notices). 11,004
  source chars. No part poem, NO images. 9 footnotes (39 total), incl. the
  source's OWN TWO endnotes in ch11 ([3] Chen not a 巡捕房 lawyer; [4] Li Yimang
  repunctuated the quoted 启事). ~47 glossary rows. Blind double-translation +
  back-translation + fact-check done (Wu Hao/Awakening Society, 伍豪启事 affair,
  Xiang Zhongfa 22-24 June 1931, Central Soviet late-1931 stats all corroborated;
  Huang's warning role publicized 1993 but historiographically disputed; 巴和
  rendered "Baho", French original unverified). 电椅 footnoted as a torture chair.
  Build + qa_epub PASS (75 files, 50 documents, 12 of 44 chapters). Committed.

## What is NEXT

- B05 = ch12-ch14 (see kickoff above; Part Three opens at ch13, fold its 临江仙).
  Then B06 ch15-ch16, B07 ch17-ch19, B08 ch20-ch21, B09 ch39-ch43 (appendices).
  See book.json "batches".

## Reusable machinery (saves time)

- scripts/gen_bilingual_b02.py IS the bilingual generator: a DROP map of
  {unit: (src_file, {1-indexed NON-EMPTY lines to drop = header, title,
  captions})}, plus an optional POEM map for part-opening chapters. IMPORTANT:
  the DROP indices are 1-indexed over the file's NON-EMPTY lines (blank lines are
  skipped by src_lines) -- enumerate with
  `python3 -c "print([l for l in open(f) if l.strip()])"` to get true indices.
  Add the units, write out/<id>_en.txt, run it; it asserts source/English
  paragraph parity before writing (a mismatch usually means a dropped caption line
  OR an invented/merged paragraph). B04 added ch10/ch11 (drop only header+title).
- Finding caption line numbers: caption-only lines in data/src are image captions
  (person-bio lines, 原图片说明/图片说明 lines, 右起… name rosters, or a standalone
  photo caption). Cross-check images per chapter with
  `grep -o 'images/[0-9]*\.jpg' data/src_epub/index_split_0NN.html`; the basenames
  map straight to data/figs/. Used so far: B01 00002-00012, B02 00013-00018, B03
  00019-00021. B04 ch10/ch11: NONE.
- The SOURCE'S OWN endnotes: some chapters carry a bracketed [n] in the extracted
  text linking (via a filepos anchor in the HTML) to a 【注释】 block in a later
  index_split_*.html (the block lives in index_split_016.html = ch12). Handled so
  far: ch05 [1] (-> filepos297051), ch08 [2] (-> filepos297881), ch11 [3]
  (-> filepos298209, "Chen not a 巡捕房 lawyer") and [4] (-> filepos298455, "Li
  Yimang repunctuated the 启事"). Render each as the source's OWN note, clearly
  attributed and distinct from the translator's notes. Grep the unit's HTML for
  `<sup`/`filepos`. NB for B05: ch12 IS index_split_016.html, whose tail holds the
  【注释】 block itself -- do not translate that trailing apparatus as ch12 body text.
- data/noise.txt strips this book's recurring non-quantity numerals. B04 added
  `一百两` (tael-unit merge -> 102) and `[一二两三四五六七八九十]钟` (十一点钟 clock
  residue). check_numbers.py now also strips thousands separators between digits
  (_decomma), so grouped figures ("2,500,000") count as one number -- write big
  numbers with commas as normal, no need to un-group them.

## Open items / read-through flags

- book.json author_note still calls Huang Dinghui the "birth name"; the source and
  scholarship make 黄彰定 (Zhangding) the birth/school name, 慕兰 the 1926 name,
  定慧 a later (1932) name. Translation and glossary are correct; the metadata line
  is worth tidying in a later pass (does not affect the reading text).
- Allusive/subject titles still to footnote when reached: 面谒周公 (ch20, 周公 =
  Zhou Enlai -- the 周公/Lord Zhou honorific is now footnoted at its first
  appearance in ch11, cross-referenced forward to the ch20 title).
- Faithfully-rendered source slips kept visible (not silently corrected): the
  memoir calls Chen Fu the Northern Bureau "propaganda head" (scholarship:
  secretary-general); Tan Yankai's headship of the Yuelu Academy is unverified;
  the memoir calls Guan Xiangying "deputy political commissar of the Second Front
  Red Army" (he was the FULL commissar of the 红二方面军; "deputy" belongs to the
  earlier 红二军团). All left as the author wrote them; notes avoid repeating the
  unverified claims.
- 巴和 (the French lawyer in the 伍豪启事 rebuttal): rendered "Baho" (provisional);
  the Chinese form is attested but the French original is not established. If a
  later source turns up the real French name, update the glossary AND grep every
  built unit for "Baho" and rebuild.

## State / traps

- Scope is PARTIAL by instruction: ch00, ch01-ch21, ch39-ch43 only. ch22-ch38
  stay as pending skeleton pages (the build handles this; do not delete them).
- Part poems: Part One at ch01, Part Two at ch05 (both DONE). Part Three opens at
  ch13 (index_split_017.html) -- fold that poem into ch13 in B05. Part Four opens
  at ch22 and Part Five at ch32, but those are out of scope.
- Note anchors go in BEFORE markup substitution (the builder inserts them and
  REFUSES on an unmatched anchor). XHTML note bodies use NUMERIC character
  references, never named entities. Numbering is continuous and builder-assigned
  in reading order (39 notes through ch11; ch10 = 31-33, ch11 = 34-39).
- Figure "before" anchors must be a substring within the FIRST 80 characters of a
  paragraph line, or the builder silently skips the figure. Verify placement by
  grepping the built .xhtml for the image basename.
- Deliverable filename is exactly out/The Autobiography of Huang Mulan.epub (with
  spaces). data/src/, data/src_epub/, data/figs/, out/*.epub are gitignored and
  rebuild from source.epub; commit the JSON, the reading/bilingual/en md, the
  generator + check scripts, PROGRESS/HANDOFF, data/zh, data/noise.txt.
- Work on ONE branch: claude/huang-mulan (per CLAUDE.md rule 2). If a session
  starts you on a stray branch, consolidate onto the working branch and delete the
  stray (local + remote). B04's session opened on such a stray branch and was
  consolidated. Pillow needed for interior figures (pip install pillow on a fresh
  container) -- B04 had no figures so it was not needed.
