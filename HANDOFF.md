# HANDOFF — On a Hair Trigger (一触即发) by Zhang Yong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 (ingest + survey) done, plan APPROVED. Batches B01 (Prologue +
Chapters 1 to 4) and B02 (Chapters 5 to 7) are DONE, checks green, committed.
Batch B03 is next.

## Message to paste into the next chat

```
Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Do Batch B03 end to end: Chapters 8 to 10 (ch08, ch09,
ch10), roughly 15,194 source characters. This continues the novel from Batch B02
(the Prologue and Chapters 1 to 7 are already translated and built).

FIRST, if data/src/ is empty (a fresh container only has source.epub committed),
regenerate the extracted text with: python3 scripts/ingest_epub.py source.epub
(this rewrites data/src/*.txt and data/figs/*; it does not touch book.json,
notes.json, glossary.json, data/noise.txt, or the out/*_bilingual.md files, which
are committed). Then, since the builder reads out/*_reading.md, regenerate the
already-translated reading files and parity sources from the committed bilinguals
before building: for each id ch00..ch07 run
  python3 scripts/split_bilingual.py "out/<id>_bilingual.md" <id> "<zh title>"
(the zh titles are in book.json "title").

Read each unit's source from data/src/ (ch08 = 11_part0009.txt, ch09 =
12_part0010.txt, ch10 = 13_part0011.txt). Translate to the register in CLAUDE.md:
clean, flowing novelistic English, the book's own voice, all apparatus in the
notes and nothing inline.

Author the reading text WITHOUT re-typing the source: write out/<id>_en.txt with
one English paragraph per line (same count and order as the source paragraphs),
then run
  python3 scripts/make_bilingual.py data/src/<file>.txt out/<id>_en.txt <id> "## H2 <English chapter title>"
which assembles out/<id>_bilingual.md with the source `>` lines copied verbatim
(it errors on a paragraph-count mismatch). Then
  python3 scripts/split_bilingual.py "out/<id>_bilingual.md" <id> "<full Chinese chapter title, e.g. 第八章　前度杨郎今又来>"
generates out/<id>_reading.md and the parity source data/zh/<id>.txt. The book is
flat: one H2 couplet title, then continuous prose, no sections/subsections; source
scene breaks are separate source paragraphs, rendered as paragraph breaks.

Run the checks and record them in PROGRESS.md:
- scripts/check_numbers.py --noise data/noise.txt out/<id>_bilingual.md  (must be
  0 unresolved). The non-quantity noise list lives in data/noise.txt; ADD to it
  (or to WORD_NUM in check_numbers.py for spelled-out ordinals your prose uses)
  whenever a NON-quantity numeral is flagged, and record what you added. Do NOT
  drop a real date/year/time; render clock times so their digits survive (e.g.
  "three thirty", "three forty-five", not "half past three").
- scripts/check_structure.py --pairs data/zh/<id>.txt out/<id>_reading.md  (parity
  must be OK). Also sanity-check verbatim fidelity by diffing data/zh/<id>.txt
  (minus its first ### title line) against the source paragraphs (data/src file,
  minus its first two metadata lines) — aim for zero content diffs (the source
  files' missing final newline is the only expected diff).
Apply blind double translation and round-trip back-translation to the argumentative
or lyrical passages and sample the plain narration; give 3 to 5 percent of the
batch the full paranoid audit and report the observed error rate.

Footnotes into notes.json (about 3 per chapter-equivalent; anchors must be exact
verbatim substrings of the English prose — the builder REFUSES to build on an
unmatched anchor, so verify each with a quick grep -c before building; XHTML
bodies use NUMERIC character references only, e.g. &#8212; &#8216; &#8217; &#8211;,
never named entities; hanzi may be written literally). The chapter-title couplets
are the first thing to footnote, anchored to a thematically apt verbatim phrase in
that chapter's prose (the H2 chapter title itself does not take a note ref). Likely
title sources to verify against scholarship and footnote (say corroborated /
uncorroborated / contradicted): ch08 前度杨郎今又来 plays on Liu Yuxi's 前度刘郎
("Liu of former days comes again", from 再游玄都观); ch09 开门人即闭门人 and ch10
误剪同心一片花 (同心花 / the tied-heart flower) — trace each, and if a line is not a
traceable quotation, render it literally and footnote it as such.

Glossary rows into glossary.json for every NEW name, place, org and term, one
decided rendering per referent — CHECK the existing glossary first and reuse those
renderings (recurring cast: the Rong family, Rong Sheng, A-Chu / Rong Chu, Rong
Gui, Jiang Lishui, Yang Muci, Lao Yu, Du Luning, Yu Xiaojiang, He Yashu, the CCP
特科 vs 军统 / Juntong, etc.). Keep one rendering per referent across the whole book.

Then rebuild the cumulative EPUB with:
  python3 scripts/build_reading_epub.py "out/On a Hair Trigger.epub"
(the TOC stays pending-aware: translated chapters link their content, the rest
still link their skeleton outline). Run scripts/qa_epub.py "out/On a Hair
Trigger.epub" until green, commit on branch claude/on-a-hair-trigger,
and rewrite HANDOFF.md with a paste-ready B04 kickoff (B04 = ch11 to ch13). Cite
chapters, never page numbers. Never invent bridging text or silently drop material;
footnote genuine ambiguity and leave it visible. If the source carries a pirate-site
watermark line (as ch06 did), keep it verbatim in the bilingual `>` line but leave
it out of the reading text and footnote it. Do not pause for approval mid-batch.
When done, deliver out/On a Hair Trigger.epub to me as an attached file in the chat.
```

## What is DONE (do not redo)

- Step 0: ingested source.epub, authored book.json (final), survey approved,
  skeleton EPUB built, QA green. Kindle/Apple Books metadata + cover wired in.
- Batch B01 = Prologue (ch00) + Chapters 1 to 4 (ch01 to ch04), ~20,041 chars.
  13 footnotes, 64 glossary rows. See PROGRESS.md.
- Batch B02 = Chapters 5 to 7 (ch05 to ch07), ~19,345 chars, 483 paragraphs.
  Bilingual QC files, reading files, parity sources, 10 footnotes (#14 to #23),
  and 24 new glossary rows all written; check_numbers 0 unresolved on all units,
  check_structure parity OK, verbatim parity zero content diffs, blind double
  translation on 3 passages + back-translation on 1, paranoid audit ~4.5% at 0
  observed error rate. See PROGRESS.md.
- out/On a Hair Trigger.epub rebuilt: 8 of 36 units translated, 23 notes, qa green.

## What is NEXT

- Batch B03 = ch08 to ch10 (~15,194 chars). Then B04 = ch11 to ch13, and so on
  through B13 = ch34 to ch35 (see book.json "batches").

## State / traps

- The single working branch for this book is claude/on-a-hair-trigger (the
  book-slug branch). CLAUDE.md rule 2 (one branch) governs; a harness note may
  name another branch, but fold all work onto claude/on-a-hair-trigger and retire
  any stray branch (B02 was folded on and its stray batch branch retired).
- data/src/ and data/zh/ and build/ are NOT committed (see .gitignore). A fresh
  container has only source.epub + the committed out/*_bilingual.md, notes.json,
  glossary.json, book.json, data/noise.txt. Re-run ingest_epub.py to rebuild
  data/src; re-run split_bilingual.py on each committed bilingual (ch00..ch07) to
  rebuild data/zh and out/*_reading.md BEFORE building (the builder reads the
  reading files).
- Authoring flow (established B02): write out/<id>_en.txt (one English paragraph
  per source paragraph), then scripts/make_bilingual.py to get the bilingual with
  verbatim `>` source lines, then split_bilingual.py. Do NOT hand-type the source
  into the bilingual.
- Source structure: one spine file per chapter; single H2 couplet title; no h3/h4;
  scene breaks are separate source paragraphs (blank paragraphs in the original),
  rendered as paragraph breaks. The source carries NO notes of its own; every note
  is the translator's.
- check_numbers noise: data/noise.txt is the project non-quantity list — ALWAYS
  run with --noise data/noise.txt, and ADD to it when a non-quantity numeral is
  flagged. check_numbers.py now protects clock minutes (二十分/三十分) and compound
  "-odd" counts (二十多/三十多) via digit lookbehinds; WORD_NUM knows sixteenth=16,
  seventeenth=17.
- Reign-era dates appear beside their Western years; keep both, and let
  check_numbers see the Western year.
- Deliverable filename has a space: quote it, "out/On a Hair Trigger.epub".
- Write JSON via a file (not shell heredocs) so Chinese glyphs are not mangled;
  re-read to verify. XHTML note bodies use numeric character references only.
- Recurring names get their note at FIRST appearance in the book; reuse glossary
  renderings, do not re-romanize.
