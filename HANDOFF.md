# HANDOFF — On a Hair Trigger (一触即发) by Zhang Yong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 (ingest + survey) done, plan APPROVED. Batches B01 (Prologue +
Chapters 1 to 4), B02 (Chapters 5 to 7) and B03 (Chapters 8 to 10) are DONE,
checks green, committed. Batch B04 is next.

## Message to paste into the next chat

```
Hair Trigger B04 — Chapters 11 to 13 (ch11, ch12, ch13).

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Do Batch B04 end to end: Chapters 11 to 13 (ch11, ch12,
ch13), roughly 18,985 source characters. This continues the novel from Batch B03
(the Prologue and Chapters 1 to 10 are already translated and built).

FIRST, if data/src/ is empty (a fresh container only has source.epub committed),
regenerate the extracted text with: python3 scripts/ingest_epub.py source.epub
(this rewrites data/src/*.txt and data/figs/*; it does not touch book.json,
notes.json, glossary.json, data/noise.txt, or the out/*_bilingual.md files, which
are committed). Then, since the builder reads out/*_reading.md, regenerate the
already-translated reading files and parity sources from the committed bilinguals
before building: for each id ch00..ch10 run
  python3 scripts/split_bilingual.py "out/<id>_bilingual.md" <id> "<zh title>"
(the zh titles are in book.json "title").

Read each unit's source from data/src/ (ch11 = 14_part0012.txt, ch12 =
15_part0013.txt, ch13 = 16_part0014.txt). Translate to the register in CLAUDE.md:
clean, flowing novelistic English, the book's own voice, all apparatus in the
notes and nothing inline.

Author the reading text WITHOUT re-typing the source: write out/<id>_en.txt with
one English paragraph per line (same count and order as the source paragraphs),
then run
  python3 scripts/make_bilingual.py data/src/<file>.txt out/<id>_en.txt <id> "## H2 <English chapter title>"
which assembles out/<id>_bilingual.md with the source `>` lines copied verbatim
(it errors on a paragraph-count mismatch). Then
  python3 scripts/split_bilingual.py "out/<id>_bilingual.md" <id> "<full Chinese chapter title, e.g. 第十一章　平生际遇似萍飘>"
generates out/<id>_reading.md and the parity source data/zh/<id>.txt. The book is
flat: one H2 couplet title, then continuous prose, no sections/subsections; source
scene breaks are separate source paragraphs, rendered as paragraph breaks.

Run the checks and record them in PROGRESS.md:
- scripts/check_numbers.py --noise data/noise.txt out/<id>_bilingual.md  (must be
  0 unresolved). The non-quantity noise list lives in data/noise.txt; ADD to it
  (or to WORD_NUM in check_numbers.py for spelled-out ordinals your prose uses)
  whenever a NON-quantity numeral is flagged, and record what you added. Do NOT
  drop a real date/year/time; render clock times so their digits survive (e.g.
  "three thirty", "three forty-five", not "half past three"). The checker now
  protects clock hours (十一点/十二点) as well as clock minutes and "-odd" counts.
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
uncorroborated / contradicted): ch11 平生际遇似萍飘 (life adrift like duckweed; cf.
文天祥 过零丁洋 身世浮沉雨打萍); ch12 何日归家洗客袍 is a direct line from 蒋捷 一剪梅·
舟过吴江; ch13 琵琶声泣血泪仇 plays on 白居易 琵琶行 — trace each, and if a line is not
a traceable quotation, render it literally and footnote it as such.

Glossary rows into glossary.json for every NEW name, place, org and term, one
decided rendering per referent — CHECK the existing glossary first and reuse those
renderings (recurring cast: the Rong family, Rong Sheng, A-Chu / Rong Chu, Rong
Gui, Ronghua, Jiang Lishui, Yang Muci, Yang Yubo, Madam Yang / Yingzi, Yang Sitong,
Lao Yu, He Yashu, He Yashan, the Tang family, the CCP 特科 Special Branch vs 军统 /
Juntong, etc.). Keep one rendering per referent across the whole book.

Then rebuild the cumulative EPUB with:
  python3 scripts/build_reading_epub.py "out/On a Hair Trigger.epub"
(the TOC stays pending-aware: translated chapters link their content, the rest
still link their skeleton outline). Run scripts/qa_epub.py "out/On a Hair
Trigger.epub" until green, commit on branch claude/on-a-hair-trigger,
and rewrite HANDOFF.md with a paste-ready B05 kickoff (B05 = ch14 to ch15). Cite
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
  13 footnotes. See PROGRESS.md.
- Batch B02 = Chapters 5 to 7 (ch05 to ch07), ~19,345 chars, 483 paragraphs.
  10 footnotes (#14 to #23), 24 new glossary rows. See PROGRESS.md.
- Batch B03 = Chapters 8 to 10 (ch08 to ch10), ~15,194 chars, 419 paragraphs.
  Bilingual QC files, reading files, parity sources, 9 footnotes (#24 to #32),
  and 24 new glossary rows all written; check_numbers 0 unresolved on all units,
  check_structure parity OK, verbatim parity zero content diffs, blind double
  translation on 6 passages + 1 back-translation, paranoid audit ~4% at 0
  observed error rate. One generic checker fix (clock-hour lookbehind on 一点)
  and two noise.txt additions (万丈, 五、六十). See PROGRESS.md.
- out/On a Hair Trigger.epub rebuilt: 11 of 36 units translated, 32 notes, qa green.

## What is NEXT

- Batch B04 = ch11 to ch13 (~18,985 chars). Then B05 = ch14 to ch15, and so on
  through B13 = ch34 to ch35 (see book.json "batches").

## State / traps

- The single working branch for this book is claude/on-a-hair-trigger (the
  book-slug branch). CLAUDE.md rule 2 (one branch) governs; a harness note may
  name another branch, but fold all work onto claude/on-a-hair-trigger and retire
  any stray branch (B02 and B03 were each folded on and their stray batch
  branches retired).
- data/src/ and data/zh/ and build/ are NOT committed (see .gitignore). A fresh
  container has only source.epub + the committed out/*_bilingual.md, notes.json,
  glossary.json, book.json, data/noise.txt. Re-run ingest_epub.py to rebuild
  data/src; re-run split_bilingual.py on each committed bilingual (ch00..ch10) to
  rebuild data/zh and out/*_reading.md BEFORE building (the builder reads the
  reading files).
- Authoring flow (established B02): write out/<id>_en.txt (one English paragraph
  per source paragraph), then scripts/make_bilingual.py to get the bilingual with
  verbatim `>` source lines, then split_bilingual.py. Do NOT hand-type the source
  into the bilingual.
- Source structure: one spine file per chapter; single H2 couplet title; no h3/h4;
  scene breaks are separate source paragraphs (blank paragraphs in the original),
  rendered as paragraph breaks. The source carries NO notes of its own; every note
  is the translator's. Watch for mid-sentence paragraph splits in the source (ch08
  had one, lines 102-103); keep the parity count, render each source line as its
  own paragraph.
- check_numbers noise: data/noise.txt is the project non-quantity list; ALWAYS
  run with --noise data/noise.txt, and ADD to it when a non-quantity numeral is
  flagged. The checker now protects clock hours (十一点/十二点), clock minutes
  (二十分/三十分) and compound "-odd" counts (二十多/三十多) via digit lookbehinds;
  WORD_NUM knows eleven..thirteen, sixteenth, seventeenth. Prose that spells out
  a new ordinal the source prints as a digit needs a WORD_NUM entry.
- Reign-era dates appear beside their Western years; keep both, and let
  check_numbers see the Western year.
- Deliverable filename has a space: quote it, "out/On a Hair Trigger.epub".
- Write JSON via a file (not shell heredocs) so Chinese glyphs are not mangled;
  re-read to verify. XHTML note bodies use numeric character references only.
- Recurring names get their note at FIRST appearance in the book; reuse glossary
  renderings, do not re-romanize.
- Prose written TO the commissioner (this HANDOFF, PROGRESS, chat) uses no em
  dashes (CLAUDE.md rule 6); the translation itself may use them.
