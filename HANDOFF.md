# HANDOFF — Midnight (子夜), Mao Dun

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Midnight B09

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Work only on branch claude/midnight. Build the
deliverable as out/Midnight.epub (the builder defaults to out/book.epub, so pass
the path explicitly on every build and every qa run).

data/src/ is regenerable and git-ignored, so if it is missing run
scripts/ingest_epub.py source.epub first to recreate it (Chapters One through
Eight are already translated; do not redo them).

Do Batch B09 = Chapter Nine (unit ch09) end to end. Read the source from
data/src/12_part0010.txt; it is authoritative. Quote it verbatim in the bilingual
QC file and render it faithfully and in full into English in the book's own
novelistic register. Chapter Nine is 13,659 source chars.

Chapter Nine carries NONE of the source's own endnotes (the only remaining author
notes are [8][9], both in ch11). So this batch touches source_notes.json only if
you find an inline [n] marker in the source of ch09 (you should not; grep the
source to confirm). Do NOT invent one.

Author out/ch09_bilingual.md (a "## H2 Chapter Nine" line, then per source
paragraph a "> <verbatim source>" line and the English beneath). The safe way to
get verbatim source and exact paragraph parity is to write the English one
paragraph per line and zip it against the source body lines with a short script
(this is how B01-B08 did it: read data/src/12_part0010.txt, drop line 1 = the
title 九, and the rest are the body paragraphs; assert the English line count
equals the body line count BEFORE zipping, then write the bilingual). B07 and B03
each dropped one paragraph mid-draft and the pre-zip assertion caught it, so keep
that guard, and spot-check alignment at a few paragraph indices before writing.
Then run:
  python3 scripts/split_bilingual.py out/ch09_bilingual.md ch09 "九"
  python3 scripts/check_numbers.py out/ch09_bilingual.md --noise data/noise_zh.txt
  python3 scripts/check_structure.py --pairs data/zh/ch09.txt out/ch09_reading.md
When check_numbers flags a non-quantity numeral (idiom, slang, set phrase, a name
with a digit, a shape-word, an approximate range, a compound the checker cannot sum,
an intensifier, an ordinal date the word-list lacks), add a regex for it to
data/noise_zh.txt with a one-line reason; do not silence a real dropped number. The
noise file already carries a generous ch01..ch08 block, so many recurring items are
handled. Number-rendering habits that keep the checker clean (learned across
B01-B08): render 十万 as "one hundred thousand" (not "a hundred thousand", which the
checker cannot sum); write "a hundred/a thousand" WITH the article (not "the
hundred"), or the checker reads no numeral; the checker SUMS an adjacent compound
like 三千五千 into 8000, so render such a range in words and whitelist the source
form; render 二人/两位/两个/父女两个 "the two of them / these two" so the count 2 stays
visible; give a "十几X" as "ten-odd X" and a "十来X" as the same; a hanzi ordinal like
第二十三 is safest with digits ("No. 23"), and clock/frame numbers (九号, 十六) with
digits. A bare 两 that is the tael after a price is cleared by the ch03/ch08 (?<=百)两
/(?<=十)两/(?<=万)两 rules; a bare 百/万 not preceded by a numeral is cleared by the
ch03/ch08 bare-百/bare-万 rules.

Add translator footnotes to notes.json under "ch09" at about chapter density (~3-6;
anchors must be verbatim substrings of the English prose; XHTML bodies use NUMERIC
character references for punctuation and dashes, never named entities; literal
Chinese is fine). ch08's translator notes were builder-numbered 44-49, so ch09's
continue from 50. Add every new proper noun / place / firm / term to glossary.json
with one rendering per referent and a status. Reuse the names and vocabulary already
fixed in glossary.json (the Wu-family and combine cast; the bond-market cast Zhao
Botao / Han Mengxiang / Du Zhuzhai; and the ch08 cast now fixed there: Feng Yunqing,
He Shen'an, Feng Meiqing/Ah Mei, Liu Yuying, Old Ninth the concubine, Lu Kuangshi,
Li Zhuangfei, the Yuanfeng native bank, Mingyuan, the Bai residence, plus 编遣/裁兵/
印子钱/庄票/笑面虎). Note for glossary NOTE bodies: use plain Unicode punctuation, NOT
numeric refs, because the builder esc()s glossary notes (a "&#8216;" there renders as
literal text; see PROGRESS B02 read-through). And WRITE glossary/notes JSON via a
Python file, then RE-READ to verify the Chinese: a shell heredoc silently mangled
钱庄 into a wrong glyph in B08 and it had to be repaired.

Rebuild with build_reading_epub.py out/Midnight.epub (the TOC stays pending-aware:
Chapters One through Nine link their content, every other unit still links its
skeleton outline), run qa_epub.py out/Midnight.epub until green, commit on
claude/midnight, and rewrite HANDOFF.md with the B10 kickoff. Cite chapters, never
page numbers. Never invent bridging text. Do not pause for approval mid-batch.
Deliver out/Midnight.epub in chat as an attached file.
```

## What is DONE (do not redo)

- Step 0 (ingest + survey) complete and approved. 20 units (ch01..ch19 numbered
  chapters + ch20 afterword); OPF metadata and cover set; skeleton EPUB, qa green.
- Approved batch plan (21,000-char maximum) in book.json "batches": B01..B17 one
  chapter each (ch01..ch17), B18 = ch18 + ch19 + Afterword.
- B01 = Chapter One (ch01): done. Translator notes 1-9; source notes [1][2].
- B02 = Chapter Two (ch02): done. Translator notes 10-15; source note [3].
- B03 = Chapter Three (ch03): done. Translator notes 16-21; no source note.
- B04 = Chapter Four (ch04): done. Translator notes 22-27; no source note.
- B05 = Chapter Five (ch05): done. Translator notes 28-33; source note [4].
- B06 = Chapter Six (ch06): done. Translator notes 34-38; source notes [5][6][7].
- B07 = Chapter Seven (ch07): done. Translator notes 39-43; NO source notes.
- B08 = Chapter Eight (ch08): done. out/ch08_reading.md; translator notes 44-49
  (笑面虎; 绿头巾/cuckold; 请君入瓮; Mencius 好色; 放白鸽/仙人跳; 公妻); NO source notes.
  Added the ch08 cast (Feng Yunqing, He Shen'an, Feng Meiqing, Liu Yuying, Old
  Ninth, Zhang Daqian, Zhang Ziping, Zhu Bolu, Liu Bao, Jin Ma, A Shun), Mingyuan,
  the Bai residence, the Yuanfeng native bank, the term 笑面虎, and a ch08 noise
  block (零用; 五彩; 张大千; (?<=万)两; 三千五千; 六宝; 千金; 一百五六十; bare-百 rule).
  qa green, 49 notes. See PROGRESS.md for the full record.

## What is NEXT

- Batch B09 = Chapter Nine (ch09), 13,659 source chars, and no source notes. See
  the kickoff above.

## Where the source's own notes fall (for planning)

The nine author endnotes (exact wording in data/src/24_part0022.txt) are keyed
inline as follows: [1][2] ch01 (done); [3] ch02 (done); [4] ch05 (done);
[5][6][7] ch06 (done); [8][9] ch11. All OTHER chapters (ch03, ch04, ch07..ch10,
ch12..ch20) carry none. Each remaining one goes into source_notes.json under its
unit id with its ORIGINAL number, never into notes.json.

## State / traps

- Deliverable filename: out/Midnight.epub. The builder and qa default to
  out/book.epub; always pass out/Midnight.epub explicitly.
- Two note streams, kept apart: translator footnotes (notes.json, numbered 1..N
  by the builder in reading order; ch08 got 44-49, so ch09's translator notes
  continue from 50) and the source's own notes (source_notes.json, the author's
  own [n]). Never merge them. ch09 has NO source notes.
- book.json is the LOGICAL structure. The source cover, colophon (part0000) and
  the source's own table of contents (part0001) are not translatable units.
- Paragraph parity is enforced: one English paragraph per source paragraph. The
  bilingual file's "## H2 <title>" line is the chapter title and is not a
  paragraph pair. Zip English-per-line against the source body to keep parity
  structural, and assert the counts match BEFORE writing the bilingual (this
  caught a dropped paragraph in B03 and again in B07). Spot-check alignment at a
  few indices too: B08's block bookkeeping was briefly off by one and the
  index spot-check confirmed the pairing was in fact correct.
- check_numbers note-body rule vs glossary-note rule differ: notes.json /
  source_notes.json bodies are inserted RAW, so use numeric char refs for
  punctuation. glossary.json note bodies are esc()d, so use plain Unicode
  punctuation. WRITE both via a Python file and RE-READ to verify the Chinese
  glyphs; a shell heredoc mangled 钱庄 in B08.
- The checker cannot sum compound hundreds/hundred-thousands or teen-thousands in
  spelled English, SUMS an adjacent compound like 三千五千 into 8000, reads a hanzi
  numeral in a name as a count, reads "the hundred" as no numeral, and its
  word-list has no arbitrary ordinals. NOISE ORDER IS LOAD-BEARING: a longer token
  must be stripped before a shorter rule that is a prefix of it. Known traps now in
  the file: 一百二十个 before 一百二; 十几X orphaning 十 (render "ten-odd X"); 十一点
  orphaning 十 (十钟/十半 residues); a bare 万 or 百 needs a numeral before it; a 两
  after 百/十/万 is the tael. When the checker flags a number that IS faithfully in
  the translation, add a documented noise regex (or render it in a form the checker
  parses); when it flags a genuinely missing number, fix the translation.
- When building the bilingual, write the English to a scratch file one paragraph
  per line and zip it against the source body with a Python script; keep the scratch
  files out of git (use the scratchpad dir).
- Branch hygiene: one branch only, claude/midnight. Each batch has arrived on a
  stray claude/midnight-b<nn>-* branch; the up-to-date work lives on
  origin/claude/midnight. Fast-forward local claude/midnight to it, do the batch
  there, push claude/midnight, and delete the stray (local + remote/tracking ref).
  Do not spin off new branches.
