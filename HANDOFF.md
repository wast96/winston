# HANDOFF — Midnight (子夜), Mao Dun

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Work only on branch claude/midnight. Build the
deliverable as out/Midnight.epub (the builder defaults to out/book.epub, so pass
the path explicitly on every build and every qa run).

data/src/ is regenerable and git-ignored, so if it is missing run
scripts/ingest_epub.py source.epub first to recreate it (Chapter One is already
translated; do not redo it).

Do Batch B02 = Chapter Two (unit ch02) end to end. Read the source from
data/src/05_part0003.txt; it is authoritative. Quote it verbatim in the bilingual
QC file and render it faithfully and in full into English in the book's own
novelistic register.

Chapter Two carries ONE of the source's own endnotes, marked [3] in the text
(its exact wording is in data/src/24_part0022.txt: [3] concerns 公债 speculation,
glossing "棺材边" as a pun on 关税/裁兵/编遣, the three bond issues). Render it as
the SOURCE's own note, not a translator note: add it to source_notes.json under
"ch02" as {"anchor": <verbatim English substring>, "n": 3, "note": <the source
note in English>}. Keep the author's own number 3. The builder places it as a
distinct bracketed teal marker under "Notes in the Original Edition," separate
from the translator's footnotes. Do not fold it in and do not drop it.

Author out/ch02_bilingual.md (a "## H2 Chapter Two" line, then per source
paragraph a "> <verbatim source>" line and the English beneath). The safe way to
get verbatim source and exact paragraph parity is to write the English one
paragraph per line and zip it against the source body lines with a short script
(see how B01 did it). Then run:
  python3 scripts/split_bilingual.py out/ch02_bilingual.md ch02 "二"
  python3 scripts/check_numbers.py out/ch02_bilingual.md --noise data/noise_zh.txt
  python3 scripts/check_structure.py --pairs data/zh/ch02.txt out/ch02_reading.md
When check_numbers flags a non-quantity numeral (idiom, slang, set phrase, a name
with a digit), add a regex for it to data/noise_zh.txt with a one-line reason;
do not silence a real dropped number.

Add translator footnotes to notes.json under "ch02" at about chapter density
(anchors must be verbatim substrings of the English prose; XHTML bodies use
numeric character references, never named entities). Add every new proper noun /
place / firm / bond-market term to glossary.json with one rendering per referent
and a status. The bond market (公债) is central to this chapter: fix its
vocabulary now (公债 government bonds, 多头/空头 bull/bear, 交易所 the exchange,
经纪人 broker, etc.) and cite where a form is attested. Names already fixed for
the whole book are in glossary.json; reuse them (Wu Sunfu, old Mr. Wu, Du
Zhuzhai, Lin Peiyao/the Wu young mistress, etc.).

Rebuild with build_reading_epub.py out/Midnight.epub (the TOC stays
pending-aware: Chapters One and Two link their content, every other unit still
links its skeleton outline), run qa_epub.py out/Midnight.epub until green, commit
on claude/midnight, and rewrite HANDOFF.md with the B03 kickoff. Cite chapters,
never page numbers. Never invent bridging text. Do not pause for approval
mid-batch. Deliver out/Midnight.epub in chat as an attached file.
```

## What is DONE (do not redo)

- Step 0 (ingest + survey) complete and approved. 20 units (ch01..ch19 numbered
  chapters + ch20 afterword); OPF metadata and cover set; skeleton EPUB, qa green.
- Approved batch plan (21,000-char maximum) in book.json "batches": B01..B17 one
  chapter each (ch01..ch17), B18 = ch18 + ch19 + Afterword.
- B01 = Chapter One (ch01): translated, footnoted, glossary seeded, built, qa
  green. out/ch01_reading.md exists. See PROGRESS.md for the full record.
- Builder now has a source-note apparatus (source_notes.json -> a distinct,
  author-numbered "Notes in the Original Edition" section). ch01's [1] and [2]
  are in it. A bug in check_numbers.py (二十多 mis-split) was fixed. A project
  noise file data/noise_zh.txt was started.

## What is NEXT

- Batch B02 = Chapter Two (ch02), 15,257 source chars. See the kickoff above.

## Where the source's own notes fall (for planning)

The nine author endnotes (exact wording in data/src/24_part0022.txt) are keyed
inline as follows: [1][2] ch01 (done); [3] ch02; [4] ch05; [5][6][7] ch06;
[8][9] ch11. All other chapters carry none. Each must go into source_notes.json
under its unit id with its ORIGINAL number, never into notes.json.

## State / traps

- Deliverable filename: out/Midnight.epub. The builder and qa default to
  out/book.epub; always pass out/Midnight.epub explicitly.
- Two note streams, kept apart: translator footnotes (notes.json, numbered 1..N
  by the builder) and the source's own notes (source_notes.json, the author's
  own [n]). Never merge them.
- book.json is the LOGICAL structure. The source cover, colophon (part0000) and
  the source's own table of contents (part0001) are not translatable units.
- Paragraph parity is enforced: one English paragraph per source paragraph. The
  bilingual file's "## H2 <title>" line is the chapter title and is not a
  paragraph pair.
- Branch hygiene: one branch only, claude/midnight. Do not spin off new branches.
