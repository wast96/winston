# HANDOFF — The Autobiography of Huang Mulan

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Huang Mulan B04 — ch10-ch11 (Ch 10. Victory in the First Battle; Ch 11. The "Wu Hao" Notices).

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then book.json, then HANDOFF.md. We are translating The Autobiography of Huang Mulan (黄慕兰自传) into an annotated English EPUB per CLAUDE.md. Work only on branch claude/huang-mulan; build the deliverable at out/The Autobiography of Huang Mulan.epub and present it in chat as an attached file.

Scope reminder (approved): translate ONLY the front matter (ch00), chapters 1-21 (ch01-ch21), and the appendices (ch39-ch43). Chapters 22-38 are out of scope and MUST stay as pending skeleton pages; do not translate or delete them. Batch target is 21,000 source chars max.

B01 (ch00-ch03), B02 (ch04-ch06) and B03 (ch07-ch09) are DONE and committed (see PROGRESS.md). Do Batch B04 = ch10-ch11 (Ch 10. Victory in the First Battle; Ch 11. The "Wu Hao" Notices), end to end:
1. Regenerate the extracted source if data/src/ is absent (it is gitignored): run scripts/ingest_epub.py source.epub. Read the batch's source from data/src/ (ch10=16_index-split-014.txt, ch11=17_index-split-015.txt). Translate to the register in CLAUDE.md, faithfully and in full. Quote the source VERBATIM in the bilingual QC file: write out/<id>_en.txt (one English paragraph per line, first line = English chapter title), then reuse scripts/gen_bilingual_b02.py (add ch10/ch11 to its DROP map with the header/title/caption line numbers; no part poem in this batch). It interleaves verbatim source with your English and asserts paragraph parity. Never invent bridging text; if a passage is genuinely ambiguous or the source is cut, footnote it and leave it visible. (B03's parity check caught an invented recap paragraph in ch09 this way -- trust the check.)
2. No part poem in B04 (Part Two runs ch05-ch12; Part Three opens at ch13). Watch for spliced-in image captions (a caption, sometimes an inscription + 说明, dropped mid-paragraph): rejoin the narrative from its verbatim halves, route the photo to figures.json, and put any inscription/说明 in a footnote. Caption-only lines go to figures.json, not the reading text. THE SOURCE'S OWN ENDNOTES: ch11 (伍豪启事 / index_split_015.html) carries TWO source endnotes, [3] and [4], that link forward to a 【注释】 block in index_split_016.html (grep index_split_015.html for <sup>/filepos). [3] is an author's note ("陈一向自己挂牌开业，并非巡捕房律师，李一氓记忆有误——作者注"); [4] notes the quoted passage was re-punctuated by Li Yimang. Render both faithfully as the source's OWN notes, distinct from your translator's notes (as B02 did for ch05 [1] and B03 for ch08 [2]). Extend data/noise.txt with \[\d+\] already covers the bracket markers.
3. Author out/<id>_bilingual.md per unit (source blockquote line tagged "> ", English beneath; chapter title tagged "## H2 <English title>"). Generate reading + parity with scripts/split_bilingual.py, then run scripts/check_numbers.py out/<id>_bilingual.md --noise data/noise.txt and scripts/check_structure.py --pairs data/zh/<id>.txt out/<id>_reading.md until both are clean. Extend data/noise.txt (source-side name/idiom numerals) and, if a spelled ordinal is missed, WORD_NUM in check_numbers.py, when a flag is a non-quantity; carry every real quantity (write compound numbers as digits if the spelled form is not detected).
4. Blind double-translation and back-translation on the argumentative/literary passages (use subagents in fresh context); fact-check names/dates/events against real scholarship (Wikipedia, Baidu Baike, academic sources; never Grok/Grokipedia or any AI-written source). Say corroborated / uncorroborated / contradicted in PROGRESS.md. Note ch11 centers on the "伍豪启事" (the 1932 fake "Wu Hao [Zhou Enlai] renounces communism" notices planted by the Kuomintang, and the Party's rebuttal); "伍豪/Wu Hao" is Zhou Enlai's alias -- footnote at first appearance in the unit.
5. Add ~3 footnotes per chapter-equivalent to notes.json (keyed by unit id; XHTML bodies with NUMERIC character references; anchors must be verbatim substrings of the English reading prose; recurring subjects get their note at FIRST appearance in the book). Extend glossary.json (one rendering per referent; reuse all prior decisions -- Kuomintang, Sun Yat-sen, Chiang Kai-shek, Whampoa, Zhou Enlai, Chen Duxiu, He Chang, Chen Tanqiu, Rao Shushi, Guan Xiangying, Pan Hannian, Chen Geng, Chen Zhigao, the author's name rows 黄彰定/慕兰/定慧, etc.). Place any of the unit's images via figures.json (reuse images already in data/figs/; B03 used 00019-00021).
6. Rebuild with scripts/build_reading_epub.py "out/The Autobiography of Huang Mulan.epub" (TOC stays fully linked; ch22-38 remain pending), run scripts/qa_epub.py until green.
7. Commit, present the EPUB to me directly as an attached file in this chat (not a git link), update PROGRESS.md, and rewrite HANDOFF.md whose first section is the ready-to-paste kickoff message for the NEXT batch (B05 = ch12-ch14, which DOES open Part Three: fold the Part Three 临江仙 poem from index_split_017.html into ch13), beginning with the label line "Huang Mulan B05".

Cite chapters and sections, never page numbers. Do not pause for approval mid-batch; run the whole batch and report back when it is built and QA-green, and paste the B05 kickoff message at the end of your reply.
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
- B03 = ch07-ch09 (In Longhua Prison; Racing North and South; Head of the Rescue
  Department). 18,809 source chars. No part poem. 10 footnotes (30 total), incl.
  the source's OWN endnote in ch08 (Wan Xixian, Mao's Selected Works citation).
  ~57 glossary rows, 3 figures (00019-00021). Blind double-translation + fact-
  check done. ch09 title corrected from "Rescuing the Minister" to "Head of the
  Rescue Department" (营救部长 = her POST, footnoted). Build + qa_epub PASS (75
  files, 50 documents, 10 of 44 chapters). Committed and pushed.

## What is NEXT

- B04 = ch10-ch11 (see kickoff above). Then B05 ch12-ch14, B06 ch15-ch16,
  B07 ch17-ch19, B08 ch20-ch21, B09 ch39-ch43 (appendices). See book.json
  "batches".

## Reusable machinery (saves time)

- scripts/gen_bilingual_b02.py IS the bilingual generator: a DROP map of
  {unit: (src_file, {1-indexed NON-EMPTY lines to drop = header, title,
  captions})}, plus an optional POEM map for part-opening chapters. IMPORTANT:
  the DROP indices are 1-indexed over the file's NON-EMPTY lines (the Read tool's
  line numbers can differ if the file has blank lines) -- enumerate with
  `python3 -c "print([l for l in open(f) if l.strip()])"` or the little dumper in
  the B03 transcript to get true indices. Add the units, write out/<id>_en.txt,
  run it; it asserts source/English paragraph parity before writing (a mismatch
  usually means a dropped caption line OR an invented/merged paragraph).
- Finding caption line numbers: caption-only lines in data/src are image captions
  (person-bio lines, 原图片说明/图片说明 lines, 右起… name rosters, or a standalone
  photo caption). Cross-check images per chapter with
  `grep -o 'images/[0-9]*\.jpg' data/src_epub/index_split_0NN.html`; the basenames
  map straight to data/figs/. B01 used 00002-00012, B02 00013-00018, B03
  00019-00021.
- The SOURCE'S OWN endnotes: some chapters carry a bracketed [n] in the extracted
  text linking (via a filepos anchor in the HTML) to a 【注释】 block in a later
  index_split_*.html. Handled so far: ch05 [1] (-> index_split_016#filepos297051),
  ch08 [2] (-> index_split_016#filepos297881). PENDING: ch11 [3] and [4] (in
  index_split_015.html -> index_split_016.html), due in B04. Grep the unit's HTML
  for `<sup`/`filepos` and render each as the source's own note.
- data/noise.txt strips this book's recurring non-quantity numerals. B03 added
  weekday names 礼拜[一..六], prisoner numbers 七○四/七○五, 立三/百色, 八字/八拜,
  and the footnote-marker pattern \[\d+\]. Extend as new false positives appear;
  every real quantity must be carried (write big/compound counts as digits if the
  spelled form is not auto-detected -- e.g. B03 wrote "108" and "28th").

## Open items / read-through flags

- book.json author_note still calls Huang Dinghui the "birth name"; the source and
  scholarship make 黄彰定 (Zhangding) the birth/school name, 慕兰 the 1926 name,
  定慧 a later (1932) name. Translation and glossary are correct; the metadata line
  is worth tidying in a later pass (does not affect the reading text).
- Allusive/subject titles still to footnote when reached: 伍豪启事 (ch11, "Wu Hao"
  = Zhou Enlai's alias -- due B04), 面谒周公 (ch20, 周公 = Zhou Enlai).
- Faithfully-rendered source slips flagged by B03's fact-check (kept visible, not
  silently corrected): the memoir calls Chen Fu the Northern Bureau "propaganda
  head" (scholarship: secretary-general); Tan Yankai's headship of the Yuelu
  Academy is unverified (the academy had ceased in 1903). Both left in the text as
  the author wrote them; the relevant notes avoid repeating the unverified claim.

## State / traps

- Scope is PARTIAL by instruction: ch00, ch01-ch21, ch39-ch43 only. ch22-ch38
  stay as pending skeleton pages (the build handles this; do not delete them).
- Part poems: Part One at ch01, Part Two at ch05 (both DONE). Part Three opens at
  ch13 (index_split_017.html) -- fold that poem into ch13 when B05 reaches it.
  B04 (ch10-ch11) has NO part poem.
- Note anchors go in BEFORE markup substitution (the builder inserts them and
  REFUSES on an unmatched anchor). XHTML note bodies use NUMERIC character
  references, never named entities. Numbering is continuous and builder-assigned
  in reading order (30 notes through ch09).
- Figure "before" anchors must be a substring within the FIRST 80 characters of a
  paragraph line, or the builder silently skips the figure. Verify placement by
  grepping the built .xhtml for the image basename.
- Deliverable filename is exactly out/The Autobiography of Huang Mulan.epub (with
  spaces). data/src/, data/src_epub/, data/figs/, out/*.epub are gitignored and
  rebuild from source.epub; commit the JSON, the reading/bilingual/en md, the
  generator script, PROGRESS/HANDOFF, data/zh, data/noise.txt.
- Work on ONE branch: claude/huang-mulan (per CLAUDE.md rule 2). If a session
  starts you on a stray branch, consolidate onto the working branch and delete the
  stray (local + remote). Pillow needed for interior figures (pip install pillow
  on a fresh container).
