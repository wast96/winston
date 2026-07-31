# HANDOFF — On a Hair Trigger (一触即发) by Zhang Yong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 (ingest + survey) is done and the 13-batch plan is APPROVED.
Nothing is translated yet. Batch 1 is next.

## Message to paste into the next chat

```
Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Do Batch B01 end to end: the Prologue (ch00) and
Chapters 1 to 4 (ch01, ch02, ch03, ch04), which is roughly 20,041 source
characters. This is the opening of the novel: 1910 Shanghai and Tokyo (the
prologue), then the Rong household in 1911 and the four chapters that follow.

Read each unit's source text from data/src/ (ch00 = 03_part0001.txt,
ch01 = 04_part0002.txt, ch02 = 05_part0003.txt, ch03 = 06_part0004.txt,
ch04 = 07_part0005.txt). Translate to the register in CLAUDE.md: clean, flowing
novelistic English prose, the book's own voice, all apparatus in the notes and
nothing inline. Author one aligned bilingual QC file out/<id>_bilingual.md per
unit (source blockquote line, English paragraph beneath; chapter heading tagged
## H2), then generate out/<id>_reading.md and the parity source with
scripts/split_bilingual.py. This book is flat: each chapter is one H2 heading
(the couplet title) followed by continuous prose, no sections and no
subsections; scene breaks in the source are blank paragraphs, so render them as
paragraph breaks.

Run the checks and record them in PROGRESS.md: scripts/check_numbers.py on each
bilingual file (every numeral, date and year must survive; the story is full of
years like 宣统三年 / 1911, so extend the NOISE list for reign-era and non-quantity
numerals rather than forcing them), and scripts/check_structure.py --pairs on
each reading file for paragraph parity. Apply blind double translation and
round-trip back-translation to the argumentative or lyrical passages and sample
the plain narration; give 3 to 5 percent of the batch the full paranoid audit
and report the observed error rate.

Footnotes into notes.json (about 3 per chapter-equivalent; anchors must be exact
verbatim substrings of the English prose; XHTML bodies use numeric character
references, never named entities). The chapter-title couplets are the first
thing to footnote: several are classical quotations (ch01 草木摇落露为霜 is from Cao
Pi's Yan'ge xing; others echo Tang and Song lines), and each title's source and
literal image earns a note at its chapter. Glossary rows into glossary.json for
every name, place, org and term, one decided rendering per referent, before you
romanize anything: the Rong family (荣家) and its members, 金莲, 荣升, 荣归, the twins
motif, place and reign-era names. Fact-check any real history (reign eras, dates,
places) against scholarship and say corroborated, uncorroborated or contradicted.

Then rebuild the cumulative EPUB to out/On a Hair Trigger.epub (the TOC stays
pending-aware: translated chapters link their content, the rest still link their
skeleton outline), run scripts/qa_epub.py until it is green, commit, and rewrite
HANDOFF.md with a paste-ready B02 kickoff. Cite chapters, never page numbers.
Never invent bridging text or silently drop material; footnote genuine
ambiguity and leave it visible. Do not pause for approval mid-batch. When done,
deliver out/On a Hair Trigger.epub to me as an attached file in the chat.
```

## What is DONE (do not redo)

- Step 0: ingested source.epub (38 spine docs, 1 image, 231,699 chars of
  chapter text), authored book.json, ran survey, built the skeleton EPUB, QA
  green. Committed and pushed on branch claude/on-a-hair-trigger.
- book.json structure is final: Prologue (ch00) + 35 chapters (ch01 to ch35),
  flat (no sections). The source's own cover page and 目录 are intentionally
  dropped; the builder regenerates a title page and a full hyperlinked contents.
- Metadata for Kindle and Apple Books is wired into the builder: refined title,
  creator with MARC aut role and file-as, language, date, publisher,
  description, subjects, original title as dc:source, a stable urn:uuid, plus the
  cover image (cover-image property and legacy cover meta) and a cover page.
- Batch plan APPROVED at a 21,000-char maximum: 13 batches, in book.json under
  "batches".

## What is NEXT

- Batch B01 = Prologue (ch00) + Chapters 1 to 4 (ch01 to ch04), ~20,041 chars.
- Then B02 = ch05 to ch07, and so on through B13 = ch34 to ch35 (see book.json
  "batches").

## Open items for the read-through

- Chapter titles: the 35 title_en in book.json are PROVISIONAL literary
  renderings of the seven-character couplet headings. Finalize each with its
  classical source as its chapter is translated, and footnote the allusion.
- Names not yet decided: settle the Rong family renderings and 金莲 (given name,
  literally "golden lotus," which the text plays on against her natural,
  unbound feet) in glossary.json at first appearance in B01.

## State / traps

- Source structure: one spine file per chapter (text/part0002.html = ch01, and
  so on; text/part0001.html = prologue). Chapters carry a single h2 couplet
  title; no h3/h4 anywhere; scene breaks are empty <p> paragraphs.
- The source carries NO notes of its own; every note is the translator's.
- Reign-era dates (宣统二年 = 1910, 宣统三年 = 1911) appear beside their Western
  years; keep both and let check_numbers see them (extend NOISE for the reign
  numerals, do not drop the Western year).
- Deliverable filename has a space: quote it, out/On a Hair Trigger.epub.
- Write JSON via Python (not shell heredocs) so Chinese glyphs are not mangled;
  re-read to verify.
