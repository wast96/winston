# HANDOFF — Midnight (子夜), Mao Dun

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Midnight B03

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Work only on branch claude/midnight. Build the
deliverable as out/Midnight.epub (the builder defaults to out/book.epub, so pass
the path explicitly on every build and every qa run).

data/src/ is regenerable and git-ignored, so if it is missing run
scripts/ingest_epub.py source.epub first to recreate it (Chapters One and Two
are already translated; do not redo them).

Do Batch B03 = Chapter Three (unit ch03) end to end. Read the source from
data/src/06_part0004.txt; it is authoritative. Quote it verbatim in the bilingual
QC file and render it faithfully and in full into English in the book's own
novelistic register.

Chapter Three carries NONE of the source's own endnotes (the nine author notes
fall [1][2] ch01, [3] ch02 — all done — then [4] ch05, [5][6][7] ch06, [8][9]
ch11). So there is nothing to add to source_notes.json this batch; do not invent
one.

Author out/ch03_bilingual.md (a "## H2 Chapter Three" line, then per source
paragraph a "> <verbatim source>" line and the English beneath). The safe way to
get verbatim source and exact paragraph parity is to write the English one
paragraph per line and zip it against the source body lines with a short script
(this is how B01 and B02 did it: read data/src/06_part0004.txt, drop line 1 = the
title 三, and the rest are the body paragraphs; assert the English line count
equals the body line count before zipping). Then run:
  python3 scripts/split_bilingual.py out/ch03_bilingual.md ch03 "三"
  python3 scripts/check_numbers.py out/ch03_bilingual.md --noise data/noise_zh.txt
  python3 scripts/check_structure.py --pairs data/zh/ch03.txt out/ch03_reading.md
When check_numbers flags a non-quantity numeral (idiom, slang, set phrase, a name
with a digit, a shape-word like 三角/六角), add a regex for it to data/noise_zh.txt
with a one-line reason; do not silence a real dropped number. The noise file
already carries a generous ch01+ch02 block, so many recurring items are handled.

Add translator footnotes to notes.json under "ch03" at about chapter density
(~3-6; anchors must be verbatim substrings of the English prose; XHTML bodies use
NUMERIC character references for punctuation/dashes, never named entities; literal
Chinese is fine). Add every new proper noun / place / firm / bond-market term to
glossary.json with one rendering per referent and a status. Reuse the names and
the bond-market vocabulary already fixed in glossary.json (Wu Sunfu, old Mr. Wu,
Du Zhuzhai, Lin Peiyao/the Wu young mistress, Zhao Botao, Shang Zhongli, the
cast introduced in ch02, plus 公债 government bonds, 多头/空头 bull/bear, 交易所
the exchange, 经纪人 broker, 交割 settlement, etc.). Note for glossary NOTE bodies:
use plain Unicode punctuation, NOT numeric refs — the builder esc()s glossary
notes, so a "&#8216;" there renders as literal text (see PROGRESS B02 read-through).

Rebuild with build_reading_epub.py out/Midnight.epub (the TOC stays
pending-aware: Chapters One–Three link their content, every other unit still
links its skeleton outline), run qa_epub.py out/Midnight.epub until green, commit
on claude/midnight, and rewrite HANDOFF.md with the B04 kickoff. Cite chapters,
never page numbers. Never invent bridging text. Do not pause for approval
mid-batch. Deliver out/Midnight.epub in chat as an attached file.
```

## What is DONE (do not redo)

- Step 0 (ingest + survey) complete and approved. 20 units (ch01..ch19 numbered
  chapters + ch20 afterword); OPF metadata and cover set; skeleton EPUB, qa green.
- Approved batch plan (21,000-char maximum) in book.json "batches": B01..B17 one
  chapter each (ch01..ch17), B18 = ch18 + ch19 + Afterword.
- B01 = Chapter One (ch01): done. out/ch01_reading.md exists; translator notes
  1-9; source notes [1][2]. See PROGRESS.md.
- B02 = Chapter Two (ch02): done. out/ch02_reading.md exists; translator notes
  10-15; source note [3] ("Coffin-edge", the 公债 pun). Bond-market glossary and
  the ch02 cast fixed for the whole book. check_numbers got two safe fixes and a
  ch02 noise block. qa green. See PROGRESS.md for the full record.

## What is NEXT

- Batch B03 = Chapter Three (ch03), 11,726 source chars. See the kickoff above.

## Where the source's own notes fall (for planning)

The nine author endnotes (exact wording in data/src/24_part0022.txt) are keyed
inline as follows: [1][2] ch01 (done); [3] ch02 (done); [4] ch05; [5][6][7] ch06;
[8][9] ch11. All OTHER chapters (including ch03, ch04) carry none. Each remaining
one goes into source_notes.json under its unit id with its ORIGINAL number, never
into notes.json.

## State / traps

- Deliverable filename: out/Midnight.epub. The builder and qa default to
  out/book.epub; always pass out/Midnight.epub explicitly.
- Two note streams, kept apart: translator footnotes (notes.json, numbered 1..N
  by the builder in reading order — ch02 got 10-15, so ch03 continues from 16)
  and the source's own notes (source_notes.json, the author's own [n]). Never
  merge them.
- book.json is the LOGICAL structure. The source cover, colophon (part0000) and
  the source's own table of contents (part0001) are not translatable units.
- Paragraph parity is enforced: one English paragraph per source paragraph. The
  bilingual file's "## H2 <title>" line is the chapter title and is not a
  paragraph pair. Zip English-per-line against the source body to keep parity
  structural.
- check_numbers note-body rule vs glossary-note rule differ: notes.json /
  source_notes.json bodies are inserted RAW → use numeric char refs for
  punctuation. glossary.json note bodies are esc()d → use plain Unicode
  punctuation. (This asymmetry bit ch01's glossary; new rows avoid it.)
- Branch hygiene: one branch only, claude/midnight. Do not spin off new branches.
