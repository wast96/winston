# HANDOFF — On a Hair Trigger (一触即发) by Zhang Yong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 (ingest + survey) done, plan APPROVED. Batch B01 (Prologue +
Chapters 1 to 4) is DONE, checks green, committed. Batch B02 is next.

## Message to paste into the next chat

```
Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Do Batch B02 end to end: Chapters 5 to 7 (ch05, ch06,
ch07), roughly 19,345 source characters. This continues the novel from Batch B01
(the Prologue and Chapters 1 to 4 are already translated and built).

FIRST, if data/src/ is empty (a fresh container only has source.epub committed),
regenerate the extracted text with: python3 scripts/ingest_epub.py source.epub
(this rewrites data/src/*.txt and data/figs/*; it does not touch book.json,
notes.json, glossary.json, or the out/*_bilingual.md files, which are committed).

Read each unit's source from data/src/ (ch05 = 08_part0006.txt, ch06 =
09_part0007.txt, ch07 = 10_part0008.txt). Translate to the register in CLAUDE.md:
clean, flowing novelistic English, the book's own voice, all apparatus in the
notes and nothing inline. Author one aligned bilingual QC file out/<id>_bilingual.md
per unit (source blockquote line, English paragraph beneath; chapter heading tagged
## H2), then generate out/<id>_reading.md and the parity source with
scripts/split_bilingual.py "out/<id>_bilingual.md" <id> "<full Chinese chapter
title, e.g. 第五章　时人不识凌云木>". The book is flat: one H2 couplet title, then
continuous prose, no sections/subsections; source scene breaks are blank
paragraphs, rendered as paragraph breaks. Quote the source VERBATIM in the
bilingual file (copy, do not re-type).

Run the checks and record them in PROGRESS.md:
- scripts/check_numbers.py --noise data/noise.txt out/<id>_bilingual.md  (must be
  0 unresolved). The reign-era / non-quantity noise list already lives in
  data/noise.txt; ADD to it (or to WORD_NUM in check_numbers.py for spelled-out
  ordinals your prose uses) whenever a NON-quantity numeral is flagged, and record
  what you added. Do NOT drop a real date/year/time; render clock times so their
  digits survive (e.g. "three thirty", "three forty-five", not "half past three"),
  as B01 did.
- scripts/check_structure.py --pairs data/zh/<id>.txt out/<id>_reading.md  (parity
  must be OK). Also sanity-check verbatim fidelity by diffing data/zh/<id>.txt
  (minus its first ### title line) against the source paragraphs (data/src file,
  minus its first two metadata lines) — B01 got zero diffs; aim for the same.
Apply blind double translation and round-trip back-translation to the argumentative
or lyrical passages and sample the plain narration; give 3 to 5 percent of the
batch the full paranoid audit and report the observed error rate.

Footnotes into notes.json (about 3 per chapter-equivalent; anchors must be exact
verbatim substrings of the English prose — the builder REFUSES to build on an
unmatched anchor, so verify each with a quick prose.count() before building; XHTML
bodies use NUMERIC character references only, e.g. &#8212; &#8216; &#8217; &#8211;,
never named entities; hanzi may be written literally). The chapter-title couplets
are the first thing to footnote, anchored to a thematically apt verbatim phrase in
that chapter's prose (the H1 chapter title itself does not take a note ref).
Likely sources to verify and footnote: ch05 时人不识凌云木 is from Du Xunhe's 小松
(Xiao song); ch06 宫花旋落已成尘 echoes the Tang "palace-blossom" poems (check Yuan
Zhen / Wang Jian); ch07 却疑春色在邻家 is from Wang Jia's 雨晴 (Yu qing). Confirm each
against scholarship and say corroborated / uncorroborated / contradicted.

Glossary rows into glossary.json for every NEW name, place, org and term, one
decided rendering per referent — CHECK the existing glossary first and reuse those
renderings (the recurring cast: the Rong family, Rong Sheng, A-Chu / Rong Chu,
Jiang Lishui, Cong Hui, Yang Muci, Lao Yu, the CCP 特科 vs 军统, etc.). Keep one
rendering per referent across the whole book.

Then rebuild the cumulative EPUB with:
  python3 scripts/build_reading_epub.py "out/On a Hair Trigger.epub"
(the TOC stays pending-aware: translated chapters link their content, the rest
still link their skeleton outline). Run scripts/qa_epub.py "out/On a Hair
Trigger.epub" until green, commit on branch claude/batch-b01-translation-qc-atxrrl,
and rewrite HANDOFF.md with a paste-ready B03 kickoff (B03 = ch08 to ch10). Cite
chapters, never page numbers. Never invent bridging text or silently drop material;
footnote genuine ambiguity and leave it visible. Do not pause for approval
mid-batch. When done, deliver out/On a Hair Trigger.epub to me as an attached file
in the chat.
```

## What is DONE (do not redo)

- Step 0: ingested source.epub, authored book.json (final), survey approved,
  skeleton EPUB built, QA green. Kindle/Apple Books metadata + cover wired in.
- Batch B01 = Prologue (ch00) + Chapters 1 to 4 (ch01 to ch04), ~20,041 chars.
  Bilingual QC files, reading files, parity sources, 13 footnotes, and 64 glossary
  rows all written; check_numbers (0 unresolved), check_structure (parity OK,
  anchors 13/0, headings uniform, drift 0), blind double translation on 4 passages,
  round-trip back-translation on 1, verbatim parity diff zero. See PROGRESS.md.
- Tooling (this batch): scripts/check_numbers.py now keeps clock minutes intact
  (lookbehind on the 十分 noise patterns) and knows "sixteenth"=16; data/noise.txt
  is the project non-quantity noise list — ALWAYS run check_numbers with
  --noise data/noise.txt.
- out/On a Hair Trigger.epub rebuilt: 5 of 36 units translated, 13 notes, qa green.

## What is NEXT

- Batch B02 = ch05 to ch07 (~19,345 chars). Then B03 = ch08 to ch10, and so on
  through B13 = ch34 to ch35 (see book.json "batches").

## State / traps

- The single working branch for this book is claude/batch-b01-translation-qc-atxrrl
  (a harness note may say otherwise; keep everything on this one branch).
- data/src/ and data/zh/ and build/ are NOT committed (see .gitignore). A fresh
  container has only source.epub + the committed out/*_bilingual.md, notes.json,
  glossary.json, book.json, data/noise.txt. Re-run ingest_epub.py to rebuild
  data/src; re-run split_bilingual.py on each committed bilingual to rebuild
  data/zh and out/*_reading.md if you need them (the builder reads out/*_reading.md,
  so regenerate those before building if the container is fresh).
- Source structure: one spine file per chapter (text/part0006.html = ch05, ...);
  single h2 couplet title; no h3/h4; scene breaks are empty <p> paragraphs.
- The source carries NO notes of its own; every note is the translator's.
- Reign-era dates appear beside their Western years; keep both, and let
  check_numbers see the Western year (extend NOISE for the reign numerals only).
- Deliverable filename has a space: quote it, "out/On a Hair Trigger.epub".
- Write JSON via a file (not shell heredocs) so Chinese glyphs are not mangled;
  re-read to verify. XHTML note bodies use numeric character references only.
- Recurring names get their note at FIRST appearance in the book; reuse glossary
  renderings, do not re-romanize.
