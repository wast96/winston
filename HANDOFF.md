# HANDOFF — On a Hair Trigger (一触即发) by Zhang Yong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 (ingest + survey) done, plan APPROVED. Batches B01 (Prologue +
Chapters 1 to 4), B02 (Chapters 5 to 7), B03 (Chapters 8 to 10), B04 (Chapters 11
to 13) and B05 (Chapters 14 to 15) are DONE, checks green, committed. Batch B06 is
next.

## Message to paste into the next chat

```
Hair Trigger B06 — Chapter 16 (ch16).

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Do Batch B06 end to end: Chapter 16 (ch16), roughly
11,004 source characters. This continues the novel from Batch B05 (the Prologue
and Chapters 1 to 15 are already translated and built).

FIRST, if data/src/ is empty (a fresh container only has source.epub committed),
regenerate the extracted text with: python3 scripts/ingest_epub.py source.epub
(this rewrites data/src/*.txt and data/figs/*; it does not touch book.json,
notes.json, glossary.json, data/noise.txt, or the out/*_bilingual.md files, which
are committed). Then, since the builder reads out/*_reading.md, regenerate the
already-translated reading files and parity sources from the committed bilinguals
before building: for each id ch00..ch15 run
  python3 scripts/split_bilingual.py "out/<id>_bilingual.md" <id> "<zh title>"
(the zh titles are in book.json "title").

Read the unit's source from data/src/ (ch16 = 19_part0017.txt). Translate to the
register in CLAUDE.md: clean, flowing novelistic English, the book's own voice,
all apparatus in the notes and nothing inline.

Author the reading text WITHOUT re-typing the source: write out/ch16_en.txt with
one English paragraph per line (same count and order as the source paragraphs),
then run
  python3 scripts/make_bilingual.py data/src/19_part0017.txt out/ch16_en.txt ch16 "## H2 Chapter 16. The Hills Wind, the Road Turns, and I Meet You Again"
which assembles out/ch16_bilingual.md with the source `>` lines copied verbatim
(it errors on a paragraph-count mismatch). Then
  python3 scripts/split_bilingual.py "out/ch16_bilingual.md" ch16 "第十六章　山回路转又逢君"
generates out/ch16_reading.md and the parity source data/zh/ch16.txt. The book is
flat: one H2 couplet title, then continuous prose, no sections/subsections; source
scene breaks are separate source paragraphs, rendered as paragraph breaks. Watch
for mid-sentence paragraph splits in the source (ch08, ch12 and ch14 each had one;
ch15 had a mid-word split in the recurring 梨花落 aria): keep the parity count,
render each source line as its own paragraph, splitting the English at the
matching point.

Run the checks and record them in PROGRESS.md:
- scripts/check_numbers.py --noise data/noise.txt out/ch16_bilingual.md  (must be
  0 unresolved). The non-quantity noise list lives in data/noise.txt; ADD to it
  (or to WORD_NUM in check_numbers.py for spelled-out ordinals your prose uses)
  whenever a NON-quantity numeral is flagged, and record what you added. Do NOT
  drop a real date/year/time; render clock times so their digits survive (e.g.
  "three thirty", "three forty-five", not "half past three"). The checker protects
  clock hours (十一点/十二点), clock minutes and "-odd" counts. Render instrument
  and vehicle names so the numeral survives where natural.
- scripts/check_structure.py --pairs data/zh/ch16.txt out/ch16_reading.md  (parity
  must be OK). Also sanity-check verbatim fidelity by diffing data/zh/ch16.txt
  (minus its first ### title line) against the source paragraphs (data/src file,
  minus its first two metadata lines) — aim for zero content diffs (the source
  files' missing final newline is the only expected diff).
Apply blind double translation and round-trip back-translation to the argumentative
or lyrical passages and sample the plain narration; give 3 to 5 percent of the
batch the full paranoid audit and report the observed error rate.

Footnotes into notes.json (about 3 for this chapter-equivalent; anchors must be
exact verbatim substrings of the English prose — the builder REFUSES to build on an
unmatched anchor, so verify each with a quick grep -c before building; XHTML bodies
use NUMERIC character references only, e.g. &#8212; &#8216; &#8217; &#8211;, never
named entities; hanzi may be written literally). The chapter-title couplet is the
first thing to footnote, anchored to a thematically apt verbatim phrase in the
chapter's prose (the H2 chapter title itself does not take a note ref). The title
山回路转又逢君 inverts the closing couplet of 岑参《白雪歌送武判官归京》(山回路转不见君，
雪上空留马行处): "I do not see you" becomes "I meet you again" — trace it against
scholarship and say corroborated / uncorroborated / contradicted, and footnote it.
If a line is not a traceable quotation, render it literally and footnote it as such.

Glossary rows into glossary.json for every NEW name, place, org and term, one
decided rendering per referent — CHECK the existing glossary first and reuse those
renderings. Recurring cast now includes: A-Chu / Yang Muchu (阿初/杨慕初, the reborn
Golden Dragon chief), Rong Chu (荣初, Fourth Madam's son), Han Zhengqi (韩正齐, the
police deputy chief now sworn to A-Chu) and his son Han Yu (韩禹), Xia Yuechun
(夏跃春), Young Tang (汤少; source also 汤少礼/汤少棋), He Yashu (和雅淑), Yang Sitong
(杨思桐), Yang Yuhua (杨羽桦, the uncle A-Chu has sworn to kill), the impostor "Yang
Yubo" (杨羽柏), Rong Sheng (荣升), Ronghua (荣华), Third/First Madam, the Golden
Dragon Society, the CCP Special Branch vs Juntong. Keep one rendering per referent
across the whole book. Recurring literary refs get their note at FIRST appearance
(the 梨花落 aria's note is at Chapter 12; the 小松 note is at Chapter 5).

Then rebuild the cumulative EPUB with:
  python3 scripts/build_reading_epub.py "out/On a Hair Trigger.epub"
(the TOC stays pending-aware: translated chapters link their content, the rest
still link their skeleton outline). Run scripts/qa_epub.py "out/On a Hair
Trigger.epub" until green, commit on branch claude/on-a-hair-trigger, and rewrite
HANDOFF.md with a paste-ready B07 kickoff (B07 = ch17). Cite chapters, never page
numbers. Never invent bridging text or silently drop material; footnote genuine
ambiguity and leave it visible. If the source carries a pirate-site watermark line
(as ch06 did), keep it verbatim in the bilingual `>` line but leave it out of the
reading text and footnote it. Do not pause for approval mid-batch. When done,
deliver out/On a Hair Trigger.epub to me as an attached file in the chat.
```

## What is DONE (do not redo)

- Step 0: ingested source.epub, authored book.json (final), survey approved,
  skeleton EPUB built, QA green. Kindle/Apple Books metadata + cover wired in.
- Batch B01 = Prologue (ch00) + Chapters 1 to 4 (ch01 to ch04), ~20,041 chars.
  13 footnotes (#1 to #13). See PROGRESS.md.
- Batch B02 = Chapters 5 to 7 (ch05 to ch07), ~19,345 chars, 483 paragraphs.
  10 footnotes (#14 to #23), 24 new glossary rows. See PROGRESS.md.
- Batch B03 = Chapters 8 to 10 (ch08 to ch10), ~15,194 chars, 419 paragraphs.
  9 footnotes (#24 to #32), 24 new glossary rows. See PROGRESS.md.
- Batch B04 = Chapters 11 to 13 (ch11 to ch13), ~18,985 chars, 512 paragraphs.
  10 footnotes (#33 to #42), 15 new glossary rows. See PROGRESS.md.
- Batch B05 = Chapters 14 to 15 (ch14 to ch15), ~20,027 chars, 514 paragraphs.
  Bilingual QC files, reading files, parity sources, 7 footnotes (#43 to #49) and
  11 new glossary rows all written; check_numbers 0 unresolved on both units,
  check_structure parity OK, verbatim parity zero content diffs, blind double
  translation on 5 passages + round-trip back-translation on 4 passages + paranoid
  audit ~4% (one substantive fix at ch14 para 20, then 0 residual). Eight
  noise.txt additions, no checker code change. See PROGRESS.md.
- out/On a Hair Trigger.epub rebuilt: 16 of 36 units translated, 49 notes, qa green.

## What is NEXT

- Batch B06 = ch16 (~11,004 chars). Then B07 = ch17, and so on through
  B13 = ch34 to ch35 (see book.json "batches").

## State / traps

- The single working branch for this book is claude/on-a-hair-trigger (the
  book-slug branch). CLAUDE.md rule 2 (one branch) governs; a harness note may
  name another branch, but fold all work onto claude/on-a-hair-trigger and retire
  any stray branch (B02..B05 stray batch branches were each folded on and deleted).
- data/src/ and data/zh/ and build/ are NOT committed (see .gitignore). A fresh
  container has only source.epub + the committed out/*_bilingual.md, notes.json,
  glossary.json, book.json, data/noise.txt. Re-run ingest_epub.py to rebuild
  data/src; re-run split_bilingual.py on each committed bilingual (ch00..ch15) to
  rebuild data/zh and out/*_reading.md BEFORE building (the builder reads the
  reading files).
- Authoring flow (established B02): write out/<id>_en.txt (one English paragraph
  per source paragraph), then scripts/make_bilingual.py to get the bilingual with
  verbatim `>` source lines, then split_bilingual.py. Do NOT hand-type the source
  into the bilingual.
- Source structure: one spine file per chapter; single H2 couplet title; no h3/h4;
  scene breaks are separate source paragraphs, rendered as paragraph breaks. The
  source carries NO notes of its own; every note is the translator's. Watch for
  mid-sentence paragraph splits in the source (ch08, ch12, ch14 each had one; ch15
  had a mid-word split in the 梨花落 aria); keep the parity count, render each source
  line as its own paragraph and split the English at the matching point.
- check_numbers noise: data/noise.txt is the project non-quantity list; ALWAYS
  run with --noise data/noise.txt, and ADD to it when a non-quantity numeral is
  flagged. The checker protects clock hours/minutes and "-odd" counts via digit
  lookbehinds; WORD_NUM knows one..thirteen, teens, tens, and some ordinals. Prefer
  rendering a quantity so its digit survives over noising it; noise only genuine
  non-quantity numerals (idioms, 零 in 凋零/飘零, bachelor-slang 五 in 王老五, etc.).
- Reign-era dates appear beside their Western years; keep both, and let
  check_numbers see the Western year.
- Deliverable filename has a space: quote it, "out/On a Hair Trigger.epub".
- Write JSON via a file (not shell heredocs) so Chinese glyphs are not mangled;
  re-read to verify (and scan `en` fields for stray hanzi). XHTML note bodies use
  numeric character references only.
- Recurring names AND recurring literary allusions get their note at FIRST
  appearance in the book; reuse glossary renderings, do not re-romanize. The 梨花落
  aria (情探 / 王魁负桂英) is footnoted at Chapter 12; 小松 (杜荀鹤) at Chapter 5.
- Prose written TO the commissioner (this HANDOFF, PROGRESS, chat) uses no em
  dashes (CLAUDE.md rule 6); the translation itself may use them.
- Plot state after B05: the hospital bombing has killed the Fourth Madam (Yang
  Mulian), Rongrong and the young nurse; A-Chu has sworn the blood oath, taken up
  the Golden Dragon Society, bound Han Zhengqi to him, and left the Rong house.
  Han Zhengqi's account of the past (ch15) contradicts the Fourth Madam's ch13
  confession in its details, and the novel leaves the discrepancy standing. Keep
  杨羽柏 = "Yang Yubo" for BOTH the dead father and the impostor uncle; the uncle's
  own name is Yang Yuhua (the man A-Chu has sworn to kill).
