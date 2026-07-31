# HANDOFF — The Autobiography of Huang Mulan

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Huang Mulan B03 — ch07-ch09 (Ch 7. In Longhua Prison; Ch 8. Racing North and South; Ch 9. Rescuing the Minister).

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then book.json, then HANDOFF.md. We are translating The Autobiography of Huang Mulan (黄慕兰自传) into an annotated English EPUB per CLAUDE.md. Work only on branch claude/huang-mulan; build the deliverable at out/The Autobiography of Huang Mulan.epub and present it in chat as an attached file.

Scope reminder (approved): translate ONLY the front matter (ch00), chapters 1-21 (ch01-ch21), and the appendices (ch39-ch43). Chapters 22-38 are out of scope and MUST stay as pending skeleton pages; do not translate or delete them. Batch target is 21,000 source chars max.

B01 (ch00-ch03) and B02 (ch04-ch06) are DONE and committed (see PROGRESS.md). Do Batch B03 = ch07-ch09 (Ch 7. In Longhua Prison; Ch 8. Racing North and South; Ch 9. Rescuing the Minister), end to end:
1. Regenerate the extracted source if data/src/ is absent (it is gitignored): run scripts/ingest_epub.py source.epub. Read the batch's source from data/src/ (ch07=13_index-split-011.txt, ch08=14_index-split-012.txt, ch09=15_index-split-013.txt). Translate to the register in CLAUDE.md, faithfully and in full. Quote the source VERBATIM in the bilingual QC file: write out/<id>_en.txt (one English paragraph per line, first line = English chapter title), then reuse the B02 generator scripts/gen_bilingual_b02.py (add ch07/ch08/ch09 to its DROP map with the header/title/caption line numbers; no part poem in this batch). It interleaves verbatim source with your English and asserts paragraph parity. Never invent bridging text; if a passage is genuinely ambiguous or the source is cut, footnote it and leave it visible.
2. No part poem in B03 (Part Two runs ch05-ch12; Part Three opens at ch13). Watch for spliced-in image captions (a caption, sometimes an inscribed poem + 说明, dropped mid-paragraph): rejoin the narrative from its verbatim halves, route the photo to figures.json, and put any inscription/说明 in a footnote. Caption-only lines go to figures.json, not the reading text. Also watch for the source's OWN endnotes (a bracketed [n] linking to a 【注释】 in a later index_split_*.html): render them faithfully as the source's own notes, distinct from your translator's notes (B02 handled one such in ch05 — grep index_split_011/012/013.html for <sup> / filepos links to check).
3. Author out/<id>_bilingual.md per unit (source blockquote line tagged "> ", English beneath; chapter title tagged "## H2 <English title>"). Generate reading + parity with scripts/split_bilingual.py, then run scripts/check_numbers.py out/<id>_bilingual.md --noise data/noise.txt and scripts/check_structure.py --pairs data/zh/<id>.txt out/<id>_reading.md until both are clean. Extend data/noise.txt (source-side name/idiom numerals) and, if a spelled ordinal is missed, WORD_NUM in check_numbers.py, when a flag is a non-quantity; carry every real quantity (write compound wages/big counts as digits if the spelled form is not detected).
4. Blind double-translation and back-translation on the argumentative/literary passages (use subagents in fresh context); fact-check names/dates/events against real scholarship (Wikipedia, Baidu Baike, academic sources; never Grok/Grokipedia or any AI-written source). Say corroborated / uncorroborated / contradicted in PROGRESS.md.
5. Add ~3 footnotes per chapter-equivalent to notes.json (keyed by unit id; XHTML bodies with NUMERIC character references; anchors must be verbatim substrings of the English reading prose; recurring subjects get their note at FIRST appearance in the book). Extend glossary.json (one rendering per referent; reuse all prior decisions — Kuomintang, Sun Yat-sen, Chiang Kai-shek, Whampoa, Canton-Hankou Railway, Zhou Enlai, Chen Duxiu, He Chang, Chen Tanqiu, Rao Shushi, the author's name rows 黄彰定/慕兰/定慧, etc.). Place any of the unit's images via figures.json (reuse images already in data/figs/).
6. Rebuild with scripts/build_reading_epub.py "out/The Autobiography of Huang Mulan.epub" (TOC stays fully linked; ch22-38 remain pending), run scripts/qa_epub.py until green.
7. Commit, present the EPUB to me directly as an attached file in this chat (not a git link), update PROGRESS.md, and rewrite HANDOFF.md whose first section is the ready-to-paste kickoff message for the NEXT batch (B04 = ch10-ch11), beginning with the label line "Huang Mulan B04".

Cite chapters and sections, never page numbers. Do not pause for approval mid-batch; run the whole batch and report back when it is built and QA-green, and paste the B04 kickoff message at the end of your reply.
```

Every batch kickoff message (here and in every future HANDOFF) MUST begin with a
label line "Huang Mulan B<nn>" naming the batch and its chapter scope, then a
blank line, then the standard "Read CLAUDE.md in full..." instructions.

## What is DONE (do not redo)

- Step 0 (ingest + survey): source ingested (53 spine docs, 105 images,
  254,900 chars). book.json is the logical structure; skeleton EPUB with a fully
  hyperlinked TOC; metadata wired for Kindle/Apple Books; qa_epub PASS.
- B01 = ch00-ch03 (Note on the Reissue; My Childhood; The May Fourth Awakening;
  Giving Myself to the Revolution). 19,695 source chars. Part One 临江仙 folded
  into ch01. 11 footnotes. All checks green. See PROGRESS.md.
- B02 = ch04-ch06 (A Convergence of Winds and Clouds; Going Underground;
  Secretary to the Central Committee). 19,567 source chars. Part Two 临江仙 folded
  into ch05. 9 footnotes (20 total), incl. the source's OWN endnote in ch05
  (Wan Xiyan death discrepancy). ~37 glossary rows, 5 figures. All checks green,
  blind double-translation + back-translation + scholarship fact-check done (see
  PROGRESS.md). Build + qa_epub PASS (72 files, 50 documents, 7 of 44 chapters).
  Committed and pushed.

## What is NEXT

- B03 = ch07-ch09 (see kickoff above). Then B04 ch10-ch11, B05 ch12-ch14,
  B06 ch15-ch16, B07 ch17-ch19, B08 ch20-ch21, B09 ch39-ch43 (appendices).
  See book.json "batches".

## Reusable machinery (saves time)

- scripts/gen_bilingual_b02.py IS the bilingual generator: a DROP map of
  {unit: (src_file, {1-indexed lines to drop = header, title, captions})}, and an
  optional POEM map for part-opening chapters. It prepends any poem lines
  (verbatim) and asserts source/English paragraph parity before writing. To use
  it for a new batch, add the units to its DROP map (enumerate the source lines
  first with `cat -n data/src/<file>` to find caption line numbers), write the
  out/<id>_en.txt files, then run it. Verbatim source quotation is guaranteed
  because it reads data/src/*.txt directly.
- Finding caption line numbers: caption-only lines in data/src are image captions
  (person bio lines like "宋庆龄（1893~1981），…", 原图片说明/图片说明 lines, 右起…
  name rosters). Cross-check images per chapter with
  `grep -o 'images/[0-9]*\.jpg' data/src_epub/index_split_0NN.html` — the basenames
  map straight to data/figs/. B01 used 00002-00012, B02 used 00013-00018.
- data/noise.txt strips this book's recurring non-quantity numerals. B02 added
  成千上万, 万岁, 二老, 凋零, 三妻四妾, 不三不四, 四合院, 颠三倒四, 胡说八道,
  六神无主, 十有八九, 第二天, and place names 九江/万安. Extend as new false
  positives appear; every real quantity must be carried in the English (write big
  counts as digits if the spelled form is not auto-detected).

## Open items / read-through flags

- book.json author_note still calls Huang Dinghui the "birth name"; the source and
  scholarship make 黄彰定 (Zhangding) the birth/school name, 慕兰 the 1926 name,
  定慧 a later (1932) name. Translation and glossary are correct; the metadata line
  is worth tidying in a later pass (does not affect the reading text).
- Allusive/subject titles still to footnote when reached: 伍豪启事 (ch11, "Wu Hao"
  = Zhou Enlai's alias), 面谒周公 (ch20, 周公 = Zhou Enlai). ch09 "营救部长"
  (Rescuing the Minister) — the minister is Yang Yong'ai / the Xiang-E-Xi affair;
  confirm at translation time.
- The source carries its OWN endnotes in some chapters (a bracketed [n] → a
  【注释】 block in a later index_split file). One was handled in ch05. B03 must
  grep index_split_011/012/013.html for <sup>/filepos footnote links and, if any,
  render them as the source's own notes.

## State / traps

- Scope is PARTIAL by instruction: ch00, ch01-ch21, ch39-ch43 only. ch22-ch38
  stay as pending skeleton pages (the build handles this; do not delete them).
- Part poems: Part One at ch01, Part Two at ch05 (both DONE). Part Three opens at
  ch13 (index_split_017.html) — fold that poem into ch13 when B05 reaches it.
  B03 (ch07-ch09) has NO part poem.
- Note anchors go in BEFORE markup substitution (the builder inserts them and
  REFUSES on an unmatched anchor). XHTML note bodies use NUMERIC character
  references, never named entities. Numbering is continuous and builder-assigned
  in reading order.
- Deliverable filename is exactly out/The Autobiography of Huang Mulan.epub (with
  spaces). data/src/, data/src_epub/, data/figs/, out/*.epub are gitignored and
  rebuild from source.epub; commit the JSON, the reading/bilingual/en md, the
  generator script, PROGRESS/HANDOFF, data/zh, data/noise.txt.
- Work on ONE branch: claude/huang-mulan (per CLAUDE.md rule 2). If a session
  starts you on a stray branch, consolidate onto claude/huang-mulan and delete the
  stray (both local + remote), as B02 did. Pillow needed for interior figures
  (pip install pillow on a fresh container).
