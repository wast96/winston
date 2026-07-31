# HANDOFF — The Autobiography of Huang Mulan

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Read CLAUDE.md in full (the working rules at the top are non-negotiable), then book.json, then HANDOFF.md. We are translating The Autobiography of Huang Mulan (黄慕兰自传) into an annotated English EPUB per CLAUDE.md. Work only on branch claude/huang-mulan; build the deliverable at out/The Autobiography of Huang Mulan.epub and present it in chat as an attached file.

Scope reminder (approved): translate ONLY the front matter (ch00), chapters 1-21 (ch01-ch21), and the appendices (ch39-ch43). Chapters 22-38 are out of scope and MUST stay as pending skeleton pages; do not translate or delete them. Batch target is 21,000 source chars max.

B01 (ch00-ch03) is DONE and committed (see PROGRESS.md). Do Batch B02 = ch04-ch06 (Ch 4. A Convergence of Winds and Clouds; Ch 5. Going Underground; Ch 6. Secretary to the Central Committee), end to end:
1. Regenerate the extracted source if data/src/ is absent (it is gitignored): run scripts/ingest_epub.py source.epub. Read the batch's source from data/src/ (ch04=09_index-split-007.txt, ch05=11_index-split-009.txt, ch06=12_index-split-010.txt). Translate to the register in CLAUDE.md, faithfully and in full. Quote the source VERBATIM in the bilingual QC file (the B01 method: read source lines from data/src/*.txt with a small generator and interleave your English from out/<id>_en.txt, so nothing is re-typed). Never invent bridging text; if a passage is genuinely ambiguous or the source is cut, footnote it and leave it visible.
2. ch05 is the first chapter of Part Two: fold in the part-opening 临江仙 ci poem (source index_split_008.html, in data/src_epub/) as an italic epigraph at the head of ch05, exactly as ch01 did for Part One (part_poem_src is in book.json). ch04 and ch06 have no part poem.
3. Watch for the reissue's spliced-in image captions: the source often inserts an image with its caption (sometimes an inscribed poem plus a 说明 editorial note) into the middle of a running paragraph. Rejoin the narrative sentence from its verbatim halves, send the photo to figures.json, and if there is inscription/说明 text put it in a footnote. Caption-only lines in data/src go to figures.json, not into the reading text.
4. Author out/<id>_bilingual.md per unit (source blockquote line tagged "> ", English beneath; chapter title tagged "## H2 <English title>"). Generate reading + parity with scripts/split_bilingual.py, then run scripts/check_numbers.py out/<id>_bilingual.md --noise data/noise.txt and scripts/check_structure.py --pairs data/zh/<id>.txt out/<id>_reading.md until both are clean. Extend data/noise.txt (source-side name/idiom numerals) and, if a spelled ordinal is missed, WORD_NUM in check_numbers.py, when a flag is a non-quantity; carry every real quantity (write compound wages/big counts as digits if the spelled form is not detected).
5. Blind double-translation and back-translation on the argumentative/literary passages (use subagents in fresh context); fact-check names/dates/events against real scholarship (Wikipedia, Baidu Baike, academic sources; never Grok/Grokipedia or any AI-written source). Say corroborated / uncorroborated / contradicted in PROGRESS.md.
6. Add ~3 footnotes per chapter-equivalent to notes.json (keyed by unit id; XHTML bodies with NUMERIC character references; anchors must be verbatim substrings of the English reading prose; recurring subjects get their note at FIRST appearance in the book). Extend glossary.json (one rendering per referent; reuse the B01 decisions: Kuomintang, Sun Yat-sen, Chiang Kai-shek, Whampoa, Canton-Hankou Railway, and the author's name rows 黄彰定 birth / 慕兰 1926 / 定慧 1932). Place any of the unit's images via figures.json (reuse images already in data/figs/).
7. Rebuild with scripts/build_reading_epub.py "out/The Autobiography of Huang Mulan.epub" (TOC stays fully linked; ch22-38 remain pending), run scripts/qa_epub.py until green.
8. Commit, present the EPUB to me directly as an attached file in this chat (not a git link), update PROGRESS.md, and rewrite HANDOFF.md whose first section is the ready-to-paste kickoff message for the NEXT batch (B03 = ch07-ch09).

Cite chapters and sections, never page numbers. Do not pause for approval mid-batch; run the whole batch and report back when it is built and QA-green, and paste the B03 kickoff message at the end of your reply.
```

## What is DONE (do not redo)

- Step 0 (ingest + survey): source ingested (53 spine docs, 105 images,
  254,900 chars). book.json is the logical structure; skeleton EPUB with a fully
  hyperlinked TOC; metadata wired for Kindle/Apple Books; qa_epub PASS.
- B01 = ch00-ch03 (Note on the Reissue; My Childhood; The May Fourth Awakening;
  Giving Myself to the Revolution). 19,695 source chars, all four units
  translated in full, Part One 临江仙 poem folded into ch01. 11 footnotes,
  ~55 glossary rows, 11 figures placed. All checks green (check_numbers with
  data/noise.txt, parity, anchors, headings, drift), blind double-translation and
  back-translation done, scholarship fact-check done (see PROGRESS.md). Build +
  qa_epub PASS (67 files, 50 documents). Committed and pushed.

## What is NEXT

- B02 = ch04-ch06 (see kickoff above). Then B03 ch07-ch09, B04 ch10-ch11,
  B05 ch12-ch14, B06 ch15-ch16, B07 ch17-ch19, B08 ch20-ch21, B09 ch39-ch43
  (appendices). Nine batches total; see book.json "batches".

## Reusable machinery from B01 (saves time)

- Bilingual generator pattern: write out/<id>_en.txt (one English paragraph per
  line, first line = English chapter title), then a small script that reads the
  verbatim source paragraphs from data/src/*.txt (dropping the running-header
  line 黄慕兰自传, the chapter-title line, and caption-only lines) and interleaves
  them with the English. This guarantees verbatim source quotation. The B01 copy
  is in the session scratchpad; re-create it for the new indices (enumerate the
  source lines first to get the right paragraph indices and to spot captions).
- data/noise.txt already strips this book's recurring non-quantity numerals
  (centuries/decades, 老百姓, 零星, 四乡, 万众一心, 十字, 两党, 八达岭, 广九, 李立三,
  book-title numerals). check_numbers.py NOISE now also strips 八十几 / 三十多 style
  "-odd" compounds, and WORD_NUM has spelled ordinals (fifteenth, ninetieth, ...).
  Extend both as new false positives appear.

## Open items / read-through flags

- book.json author_note still calls Huang Dinghui the "birth name"; the source and
  scholarship both make 黄彰定 (Zhangding) the birth/school name, 慕兰 the 1926 name,
  定慧 a later (1932) name. The translation and glossary are correct; the metadata
  line is worth tidying in a later pass (it does not affect the reading text).
- Allusive titles still to footnote when reached: 伍豪启事 (ch11, "Wu Hao" = Zhou
  Enlai's alias), 面谒周公 (ch20, 周公 = Zhou Enlai). Out-of-scope allusive titles
  (曲水流觞 ch23, 棠棣情深 ch38) will not be reached.

## State / traps

- Scope is PARTIAL by instruction: ch00, ch01-ch21, ch39-ch43 only. ch22-ch38
  stay as pending skeleton pages (the build handles this; do not delete them).
- Part poems: Part Two opens at ch05 (index_split_008.html), Part Three at ch13
  (index_split_017.html). Fold each into the first chapter of its part, as ch01
  did for Part One.
- The reissue splices image captions (and sometimes inscribed poems + 说明 notes)
  into running paragraphs; rejoin the narrative from verbatim halves, route the
  image to figures.json and the inscription to a footnote. Watch for sentences
  that break off (a source cut): footnote and leave visible, never invent.
- The source carries NO footnotes/endnotes of its own; every note is the
  translator's. Note anchors go in BEFORE markup substitution (the builder inserts
  them and REFUSES on an unmatched anchor). XHTML note bodies use numeric character
  references, never named entities.
- Deliverable filename is exactly out/The Autobiography of Huang Mulan.epub (with
  spaces). data/src/ and data/src_epub/ and out/*.epub are gitignored and rebuild
  from source.epub; commit the JSON, the reading/bilingual md, PROGRESS/HANDOFF.
- Work on ONE branch: claude/huang-mulan (per CLAUDE.md rule 2). Pillow is needed
  for interior figure conversion (pip install pillow if a fresh container lacks it).
