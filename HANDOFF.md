# HANDOFF — Midnight (子夜), Mao Dun

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Midnight B05

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Work only on branch claude/midnight. Build the
deliverable as out/Midnight.epub (the builder defaults to out/book.epub, so pass
the path explicitly on every build and every qa run).

data/src/ is regenerable and git-ignored, so if it is missing run
scripts/ingest_epub.py source.epub first to recreate it (Chapters One through
Four are already translated; do not redo them).

Do Batch B05 = Chapter Five (unit ch05) end to end. Read the source from
data/src/08_part0006.txt; it is authoritative. Quote it verbatim in the bilingual
QC file and render it faithfully and in full into English in the book's own
novelistic register.

Chapter Five carries ONE of the source's own endnotes: [4]. Its exact wording is
in data/src/24_part0022.txt (the file that collects the nine author notes). Find
the inline [4] marker in the source of ch05, render the note as the SOURCE's own
note (distinct from your translator footnotes), and add it to source_notes.json
under "ch05" with its ORIGINAL number 4 (never into notes.json). See how ch01's
[1][2] and ch02's [3] were done in source_notes.json for the shape.

Author out/ch05_bilingual.md (a "## H2 Chapter Five" line, then per source
paragraph a "> <verbatim source>" line and the English beneath). The safe way to
get verbatim source and exact paragraph parity is to write the English one
paragraph per line and zip it against the source body lines with a short script
(this is how B01-B04 did it: read data/src/08_part0006.txt, drop line 1 = the
title 五, and the rest are the body paragraphs; assert the English line count
equals the body line count BEFORE zipping, then write the bilingual). Then run:
  python3 scripts/split_bilingual.py out/ch05_bilingual.md ch05 "五"
  python3 scripts/check_numbers.py out/ch05_bilingual.md --noise data/noise_zh.txt
  python3 scripts/check_structure.py --pairs data/zh/ch05.txt out/ch05_reading.md
When check_numbers flags a non-quantity numeral (idiom, slang, set phrase, a name
with a digit, a shape-word, an approximate range, a compound hundred the checker
cannot sum), add a regex for it to data/noise_zh.txt with a one-line reason; do
not silence a real dropped number. The noise file already carries a generous
ch01+ch02+ch03+ch04 block, so many recurring items are handled (including the two
general B03 rules -- the tael 两 after a price is stripped, and a 万 not preceded
by a numeral is idiom/residue -- and the B04 names A Er/Qiliqiao/Li Si etc.).
Two general number-rendering habits from B04 keep the checker clean: render 十万
as "one hundred thousand" (not "a hundred thousand", which the checker cannot sum
to 100000), and render any elided-unit compound the checker misreads (e.g. 一万二
= 12,000) faithfully in words and whitelist the source form.

Add translator footnotes to notes.json under "ch05" at about chapter density
(~3-6; anchors must be verbatim substrings of the English prose; XHTML bodies use
NUMERIC character references for punctuation and dashes, never named entities;
literal Chinese is fine). Add every new proper noun / place / firm / term to
glossary.json with one rendering per referent and a status. Reuse the names and
vocabulary already fixed in glossary.json (Wu Sunfu, old Mr. Wu, Du Zhuzhai, Lin
Peiyao/the Wu young mistress, Zhao Botao, Shang Zhongli, the silk-and-bank cast
Sun Jiren, Wang Hefu, Zhu Yinqiu, Chen Junyi, Zhou Zhongwei, Tang Yunshan; the
ch04 Shuangqiao cast Zeng Canghai [now dead], Zeng Jiaju, Fei the little-moustache;
the filature staff Tu Weiyue, Mo Gancheng, and the mill workers; plus the
bond-market and silk-trade terms). Note for glossary NOTE bodies: use plain
Unicode punctuation, NOT numeric refs, because the builder esc()s glossary notes
(a "&#8216;" there renders as literal text; see PROGRESS B02 read-through).

Rebuild with build_reading_epub.py out/Midnight.epub (the TOC stays
pending-aware: Chapters One through Five link their content, every other unit
still links its skeleton outline), run qa_epub.py out/Midnight.epub until green,
commit on claude/midnight, and rewrite HANDOFF.md with the B06 kickoff. Cite
chapters, never page numbers. Never invent bridging text. Do not pause for
approval mid-batch. Deliver out/Midnight.epub in chat as an attached file.
```

## What is DONE (do not redo)

- Step 0 (ingest + survey) complete and approved. 20 units (ch01..ch19 numbered
  chapters + ch20 afterword); OPF metadata and cover set; skeleton EPUB, qa green.
- Approved batch plan (21,000-char maximum) in book.json "batches": B01..B17 one
  chapter each (ch01..ch17), B18 = ch18 + ch19 + Afterword.
- B01 = Chapter One (ch01): done. out/ch01_reading.md; translator notes 1-9;
  source notes [1][2]. See PROGRESS.md.
- B02 = Chapter Two (ch02): done. out/ch02_reading.md; translator notes 10-15;
  source note [3]. Bond-market glossary and the ch02 cast fixed for the book.
- B03 = Chapter Three (ch03): done. out/ch03_reading.md; translator notes 16-21;
  no source note. Added the ch03 cast/firm/places, the loan-and-cocoon trade
  terms, and a ch03 noise block (tael 两; bare 万).
- B04 = Chapter Four (ch04): done. out/ch04_reading.md; translator notes 22-27;
  no source note. Added the Shuangqiao cast (Zeng Canghai, Zeng Jiaju, A Er, A
  Jin, Jinbao, Fei Xiaosheng, Battalion Commander He, Li Si, pockmarked Wang,
  Chen Laoba, Sun Chuanfang), the Shuangqiao places/firms, and rural-order terms
  (土皇帝, 三民主义, 圣谕广训, 保卫团, 省防军, 印子钱, 公安分局, 曾剥皮, 党证). ch04
  noise block added (names read as counts + 一万二). qa green, 27 notes. See
  PROGRESS.md for the full record.

## What is NEXT

- Batch B05 = Chapter Five (ch05), 13,394 source chars, and its source note [4].
  See the kickoff above.

## Where the source's own notes fall (for planning)

The nine author endnotes (exact wording in data/src/24_part0022.txt) are keyed
inline as follows: [1][2] ch01 (done); [3] ch02 (done); [4] ch05 (NEXT);
[5][6][7] ch06; [8][9] ch11. All OTHER chapters (ch03, ch04 done) carry none.
Each remaining one goes into source_notes.json under its unit id with its ORIGINAL
number, never into notes.json.

## State / traps

- Deliverable filename: out/Midnight.epub. The builder and qa default to
  out/book.epub; always pass out/Midnight.epub explicitly.
- Two note streams, kept apart: translator footnotes (notes.json, numbered 1..N
  by the builder in reading order; ch04 got 22-27, so ch05's translator notes
  continue from 28) and the source's own notes (source_notes.json, the author's
  own [n]). Never merge them. ch05 has source note [4].
- book.json is the LOGICAL structure. The source cover, colophon (part0000) and
  the source's own table of contents (part0001) are not translatable units.
- Paragraph parity is enforced: one English paragraph per source paragraph. The
  bilingual file's "## H2 <title>" line is the chapter title and is not a
  paragraph pair. Zip English-per-line against the source body to keep parity
  structural, and assert the counts match BEFORE writing the bilingual (this
  caught a dropped paragraph in B03).
- check_numbers note-body rule vs glossary-note rule differ: notes.json /
  source_notes.json bodies are inserted RAW, so use numeric char refs for
  punctuation. glossary.json note bodies are esc()d, so use plain Unicode
  punctuation.
- The checker cannot sum compound hundreds/hundred-thousands in spelled-out
  English, and reads a hanzi numeral in a name as a count. When it flags a number
  that IS faithfully in the translation, add a documented noise regex (or, for
  a sum, render it in a form the checker parses: "one hundred thousand", not "a
  hundred thousand"); when it flags a number that is genuinely missing, fix the
  translation. B04 added the names A Er/Qiliqiao/Li Si/Chen Laoba and the elided
  一万二 to the noise file.
- When building the bilingual, write the English to a scratch file one paragraph
  per line and zip it against the source body with a Python script; do not hand-
  edit 200+ blockquote lines. Keep the scratch files out of git (or in the
  scratchpad dir).
- Branch hygiene: one branch only, claude/midnight. Do not spin off new branches.
  (A stray claude/midnight-b04-ch04-* branch appeared at the B04 kickoff; its
  commits were fast-forwarded onto claude/midnight and it should be deleted.)
