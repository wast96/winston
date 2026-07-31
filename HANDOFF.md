# HANDOFF — The Autobiography of Huang Mulan

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Read CLAUDE.md in full (the working rules at the top are non-negotiable), then book.json, then HANDOFF.md. We are translating The Autobiography of Huang Mulan (黄慕兰自传) into an annotated English EPUB per CLAUDE.md. Work only on branch claude/huang-mulan; build the deliverable at out/The Autobiography of Huang Mulan.epub and present it in chat as an attached file.

Scope reminder (approved): translate ONLY the front matter (ch00), chapters 1-21 (ch01-ch21), and the appendices (ch39-ch43). Chapters 22-38 are out of scope and MUST stay as pending skeleton pages; do not translate or delete them. Batch target is 21,000 source chars max.

Do Batch B01 = ch00-ch03 (Note on the Reissue; Ch 1. My Childhood; Ch 2. The May Fourth Awakening; Ch 3. Giving Myself to the Revolution), end to end:
1. Read the batch's source text from data/src/ (already extracted at ingest: ch00=04_index-split-002.txt, ch01=06_index-split-004.txt, ch02=07_index-split-005.txt, ch03=08_index-split-006.txt). Translate to the register in CLAUDE.md, faithfully and in full. Quote the source VERBATIM in the bilingual QC file (copy, do not re-type). Never invent bridging text; if a passage is genuinely ambiguous or the source is cut, footnote it and leave it visible. The source carries no notes of its own, so all notes are the translator's.
2. ch01 is the first chapter of Part One: fold in the part-opening 临江仙·壮志慕兰 ci poem (source index_split_003.html, in data/src_epub/) as an epigraph at the head of the chapter. Do the same pattern for the first chapter of any later part when you reach it (part_poem_src is recorded in book.json).
3. Author one aligned out/<id>_bilingual.md per unit (source blockquote line, English beneath; headings tagged ## / ### / ####). Generate reading text + parity source with scripts/split_bilingual.py, then run scripts/check_numbers.py and scripts/check_structure.py --pairs.
4. Blind double-translation and back-translation on the argumentative/literary passages; fact-check names/dates/events against real scholarship (Wikipedia, Baidu Baike, academic sources — never Grok/Grokipedia or any AI-written source). Say corroborated / uncorroborated / contradicted.
5. Add footnotes to notes.json (keyed by unit id, ~3 per chapter-equivalent, three kinds, XHTML bodies with NUMERIC character references; anchors must be verbatim substrings of the English prose). Extend glossary.json with attestation/status (decide one rendering per referent BEFORE romanizing: Huang Mulan/黄慕兰, her birth name Huang Dinghui/黄定慧, Zhou Enlai, the "Wu Hao"/伍豪 alias, place names, etc.). Place any of this unit's images via figures.json (reuse images already in data/figs/).
6. Rebuild with scripts/build_reading_epub.py "out/The Autobiography of Huang Mulan.epub" (the TOC stays fully linked; ch22-38 remain pending), run scripts/qa_epub.py until green.
7. Commit, present the EPUB to me directly as an attached file in this chat (not a git link), update PROGRESS.md, and rewrite HANDOFF.md whose first section is the ready-to-paste kickoff message for the NEXT batch (B02 = ch04-ch06).

Cite chapters and sections, never page numbers. Do not pause for approval mid-batch; run the whole batch and report back when it is built and QA-green, and paste the B02 kickoff message at the end of your reply.
```

## What is DONE (do not redo)

- Step 0 (ingest + survey): source ingested (53 spine docs, 105 images,
  254,900 chars total). book.json authored as the logical structure; skeleton
  EPUB built with a fully hyperlinked TOC; qa_epub PASS. Metadata wired for
  Kindle/Apple Books (Dublin Core + colour cover). Survey committed and pushed.
- No chapters translated yet.

## What is NEXT

- Batch B01 = ch00-ch03 (see kickoff above). Then B02 ch04-ch06, B03 ch07-ch09,
  B04 ch10-ch11, B05 ch12-ch14, B06 ch15-ch16, B07 ch17-ch19, B08 ch20-ch21,
  B09 ch39-ch43 (appendices). Nine batches total; see book.json "batches".

## Open items for the read-through

- English chapter/part titles in book.json are provisional working renderings;
  refine as translation settles the sense. Allusive titles to footnote when
  reached: 伍豪启事 (ch11, "Wu Hao" = Zhou Enlai's alias), 曲水流觞 (ch23, out of
  scope), 棠棣情深 (ch38, out of scope), 面谒周公 (ch20, 周公 = Zhou Enlai).
- Author's birth year: the book's own chronology (Appendix II) gives 1907-07-18;
  some external sources say 1906. Note the discrepancy when it comes up; follow
  the book, flag the divergence.

## State / traps

- Scope is PARTIAL by instruction: ch00, ch01-ch21, ch39-ch43 only. ch22-ch38
  stay as pending skeleton pages (the build handles this; do not delete them).
- Each of the five parts opens with a 临江仙 ci poem on its divider page; fold it
  into the first chapter of the part (part_poem_src in book.json). In scope this
  affects ch01 (Part One) and ch05 (Part Two) and ch13 (Part Three).
- The source carries NO footnotes/endnotes of its own; every note is the
  translator's. Render any inline emphasis/quoted verse faithfully.
- The source's own TOC page and running header (黄慕兰自传) are not reproduced;
  the copyright leaf is metadata; the source's duplicate 附录四 label (on both
  ch42 and ch43) is preserved, not renumbered. See book.json _source_note.
- Anchors for notes go in BEFORE markup substitution (the builder inserts them);
  the builder REFUSES to build on an unmatched anchor. XHTML note bodies use
  numeric character references, never named entities.
- Build/QA are green as of Step 0; keep the deliverable filename exactly
  out/The Autobiography of Huang Mulan.epub (note the spaces).
