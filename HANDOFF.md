# HANDOFF — Midnight (子夜), Mao Dun

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Midnight B14

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Work only on branch claude/midnight. Build the
deliverable as out/Midnight.epub (the builder defaults to out/book.epub, so pass
the path explicitly on every build and every qa run).

data/src/ is regenerable and git-ignored, so if it is missing run
scripts/ingest_epub.py source.epub first to recreate it (Chapters One through
Thirteen are already translated; do not redo them).

Do Batch B14 = Chapter Fourteen (unit ch14) end to end. Read the source from
data/src/17_part0015.txt; it is authoritative. Quote it verbatim in the bilingual
QC file and render it faithfully and in full into English in the book's own
novelistic register. Chapter Fourteen is 19,912 source chars — the longest chapter
in the book, so budget accordingly (it may run 350+ body paragraphs after the title
line 十四). It is the second half of the filature-strike sequence begun in ch13.

NO source notes remain anywhere. The author's own endnote stream [1]..[9] is
COMPLETE and fully placed (ch01 [1][2], ch02 [3], ch05 [4], ch06 [5][6][7], ch11
[8][9]). So source_notes.json is FROZEN: do not add to it. Everything you add this
batch is a TRANSLATOR footnote (notes.json) only. Still, grep the source for
\[\d+\] at the start as a habit, and if one ever appears, stop and reconcile against
book.json before proceeding.

Author out/ch14_bilingual.md (a "## H2 Chapter Fourteen" line, then per source
paragraph a "> <verbatim source>" line and the English beneath). The safe way to
get verbatim source and exact paragraph parity is to write the English one
paragraph per line into a scratch file (use the scratchpad dir, keep it out of git)
and zip it against the source body lines with a short script (read
data/src/17_part0015.txt, drop line 1 = the title 十四; the rest are the body
paragraphs; the file may lack a trailing newline, so filter blank lines and count
non-empty lines; assert the English line count equals the body line count BEFORE
zipping, then write the bilingual). Every batch's pre-zip assertion has caught a
would-be dropped paragraph, so keep that guard and spot-check alignment at several
paragraph indices before writing (for a long chapter, sample ~10 indices). Then run:
  python3 scripts/split_bilingual.py out/ch14_bilingual.md ch14 "十四"
  python3 scripts/check_numbers.py out/ch14_bilingual.md --noise data/noise_zh.txt
  python3 scripts/check_structure.py --pairs data/zh/ch14.txt out/ch14_reading.md
check_numbers only flags MISSING source numbers (extra English numbers are fine). When
it flags a non-quantity numeral (idiom, slang, a name/place with a digit, a shape-word
like 十字, an approximate range, a compound it cannot sum, an intensifier, an ordinal
the word-list lacks), add a regex for it to data/noise_zh.txt with a one-line reason;
do not silence a real dropped number. When it flags a number that IS faithfully present,
reword to a form the checker parses OR add a documented noise line; when it flags a
genuinely missing number, FIX THE TRANSLATION (B12 caught 二十万 mis-rendered as
"twenty thousand" — it is 200,000, "two hundred thousand"). The noise file already
carries a generous ch01..ch13 block, so many recurring items are handled, including the
ch13 strike-chapter set: 七搭八搭, 不三不四, 四喜子, 小三子, plus 三先生, 阿三, 三马,
十字, 大三元, the tael rules, the bare-百 / bare-万 rules, and the clock residue
(?<=点)四.

Number-rendering habits that keep the checker clean: render 十万 as "one hundred
thousand" and 二十万 as "two hundred thousand" (a bare 十万/二十万 is 100,000 /
200,000, NOT ten/twenty thousand — the exact trap B12 hit); render 三十万 as "three
hundred thousand", 八十万 as "eight hundred thousand", 四十多万 as "four hundred
thousand and more"; write "a hundred/a thousand" WITH the article and "five hundred"/
"one million" WITH A SPACE (no hyphen); render X成 (a tenth) and X折 (a discount) in
WORDS as "X-tenths" so the digit survives (八折 -> "eight-tenths", 九折 -> "nine-tenths")
— do NOT write "eighty per cent", which loses the 8; render two/pair as "the two of
them" so 2 stays visible; render a birth-order nickname so its digit survives (周二姐 ->
"Second Sister Zhou", 老八 -> "Old Eight") or add a noise line; render 五六万 "fifty or
sixty thousand" (60000) not "fifty thousand-odd"; ten-odd/ten-or-so for 十几X/十来X;
render 角 wages "six jiao" (a jiao = a tenth of a yuan); use DIGITS for hanzi ordinals
the word-list lacks (十五号 -> "the 15th") and for any compound the checker cannot sum
(二百五十 -> "250"; 四百三十一 -> "431"); a bare 两 after a price is the tael. NOTE:
the built-in 十[分] strip eats the 十分 out of a "X十分" clock reading; if a clock loses
its tens, render it with digits and add a targeted residue rule as B09 did with (?<=点)四.

Add translator footnotes to notes.json under "ch14" at about chapter density (~3-6;
anchors must be verbatim substrings of the English prose — verify by grep before
building; XHTML bodies use NUMERIC character references for punctuation and dashes,
never named entities; literal Chinese is fine). ch13's translator notes were
builder-numbered 73-77, so ch14's continue from 78. There is only ONE note stream
now (translator, in notes.json, builder-numbered 1..N in reading order);
source_notes.json is frozen.
Add every new proper noun / place / firm / term to glossary.json with one rendering
per referent and a status. Reuse the names and vocabulary already fixed in
glossary.json. The ch13 strike cast is now all in glossary.json — the Yuhua Silk
Filature (裕华丝厂), Tu Weiyue/屠夜壶, Mo Gancheng, Gui Changlin, Qian Baosheng,
pockmarked Li, A Zhen, Wang Jinzhen, Yao Jinfeng, Zhu Guiying, Xue Baozhu, He Xiumei,
Zeng Jiaju, Second Sister Zhou (周二姐), Qian Qiaolin (钱巧林), Auntie Xu (徐阿姨),
Lu Xiaobao (陆小宝), Zhang Axin (张阿新), Chen Yue'e (陈月娥), Ma Jin (玛金),
Cai Zhen (蔡真), Jin Xiaomei (金小妹), Jin Heshang (金和尚), Xiao Sanzi (小三子),
Sixizi (四喜子), A Xiang (阿祥), Ke Zuofu (克佐甫), plus the yellow union (黄色工会)
and the party jargon (革命高潮/总路线/右倾/机会主义). Chapter Fourteen carries the
strike out onto the street, so expect the same mill-and-union cast plus police,
保安队/公安局, and possibly Wu Sunfu and Tu Weiyue again — check glossary.json before
you romanize. NOTE for glossary NOTE bodies: use plain Unicode punctuation, NOT numeric
refs, because the builder esc()s glossary notes. notes.json note bodies, by contrast,
are inserted RAW — use numeric char refs there. And WRITE glossary/notes JSON via a
Python file, then RE-READ to verify the Chinese (a shell heredoc mangled 钱庄 in B08,
and B10 caught a 亨->享 slip only by re-reading).

Rebuild with build_reading_epub.py out/Midnight.epub (the TOC stays pending-aware:
Chapters One through Fourteen link their content, every other unit still links its
skeleton outline), run qa_epub.py out/Midnight.epub until green, commit on
claude/midnight, and rewrite HANDOFF.md with the B15 kickoff. Cite chapters, never
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
- B08 = Chapter Eight (ch08): done. Translator notes 44-49; NO source notes.
- B09 = Chapter Nine (ch09): done. Translator notes 50-55; 213 paras; NO source notes.
- B10 = Chapter Ten (ch10): done. Translator notes 56-61; 230 paras; NO source notes.
- B11 = Chapter Eleven (ch11): done. Translator notes 62-66; 205 paras; the LAST
  TWO author source notes [8][9] placed. All nine author notes [1]..[9] now built.
- B12 = Chapter Twelve (ch12): done. Translator notes 67-72; 232 paras; NO source
  notes. Fixed a real number error (二十万 = 200,000, not "twenty thousand").
- B13 = Chapter Thirteen (ch13): done. out/ch13_reading.md; translator notes 73-77
  (Tu the Chamber-pot/屠夜壶; the jiao/角; the yellow union/黄色工会; the revolutionary
  high tide/革命高潮 Li Lisan-line jargon; Ke Zuofu/克佐甫). 190 paragraphs; NO source
  notes. Added the ch13 strike cast (Second Sister Zhou, Qian Qiaolin, Auntie Xu,
  Lu Xiaobao, Zhang Axin, Chen Yue'e, Ma Jin, Cai Zhen, Jin Xiaomei, Jin Heshang,
  Xiao Sanzi, Sixizi, A Xiang, Ke Zuofu, the Yuhua Silk Filature) plus a ch13 noise
  block (七搭八搭, 不三不四, 四喜子, 小三子). qa green, 77 notes. See PROGRESS.md.

## What is NEXT

- Batch B14 = Chapter Fourteen (ch14), 19,912 source chars (the longest chapter),
  NO source notes (the author-note stream is complete). See the kickoff above.

## The source's own notes are COMPLETE (for planning)

The nine author endnotes (exact wording in data/src/24_part0022.txt) are all placed:
[1][2] ch01; [3] ch02; [4] ch05; [5][6][7] ch06; [8][9] ch11. source_notes.json is
FROZEN. All OTHER chapters (ch03, ch04, ch07..ch10, ch12..ch20) carry none. From
B12 on there is only ONE note stream: the translator footnotes in notes.json.

## State / traps

- Deliverable filename: out/Midnight.epub. The builder and qa default to
  out/book.epub; always pass out/Midnight.epub explicitly.
- Only one note stream remains: translator footnotes (notes.json, numbered 1..N by
  the builder in reading order; ch13 got 73-77, so ch14's continue from 78).
  source_notes.json is complete and frozen; do not add to it.
- book.json is the LOGICAL structure. The source cover, colophon (part0000) and
  the source's own table of contents (part0001) are not translatable units.
- Paragraph parity is enforced: one English paragraph per source paragraph. The
  bilingual file's "## H2 <title>" line is the chapter title and is not a paragraph
  pair. Zip English-per-line against the source body to keep parity structural, and
  assert the counts match BEFORE writing the bilingual. Source files may lack a
  trailing newline, so filter blank lines when counting. Spot-check alignment too.
- check_numbers note-body rule vs glossary-note rule differ: notes.json bodies are
  inserted RAW, so use numeric char refs for punctuation. glossary.json note bodies
  are esc()d, so use plain Unicode punctuation. WRITE all of them via a Python file
  and RE-READ to verify the Chinese glyphs. check_numbers flags only MISSING source
  numbers; extra English numbers (Third Master, the two of them) are harmless.
- The BIG number trap (B12): a bare 十万/二十万/三十万 is 100,000 / 200,000 / 300,000,
  NOT ten/twenty/thirty thousand. Render X万 as (X hundred thousand) when X < 10.
  When check_numbers reports a genuinely missing quantity, fix the translation, do
  not add noise.
- The checker cannot sum compound hundreds / hundred-thousands / teen-thousands in
  spelled English, SUMS an adjacent compound (三千五千 -> 8000; 二千五六百 -> 2600),
  reads a hanzi numeral in a name/place as a count (四川, 大三元, 阿三, 三马路, 瘪三,
  四喜子, 小三子), reads a X成/X折 as a bare digit, needs a SPACE in "five hundred"/
  "one million" and the article in "a hundred", and its word-list has limited ordinals
  ("fourth/tenth/sixteenth/seventeenth/thirtieth" yes; "fifteenth" NO - use digits).
  A birth-order nickname's digit survives if you render it in words (周二姐 ->
  "Second Sister Zhou", 老八 -> "Old Eight"); otherwise add a noise line.
  NOISE ORDER IS LOAD-BEARING: a longer token must be stripped before a shorter rule
  that is a prefix of it, and a residual-adjacency pass (e.g. the second 零碎) must
  come AFTER the rule that creates the residue.
- When building the bilingual, write the English to a scratch file one paragraph
  per line and zip it against the source body with a Python script; keep the scratch
  files out of git (use the scratchpad dir).
- Branch hygiene: one branch only, claude/midnight. Each batch has arrived on a
  stray claude/midnight-b<nn>-* branch; the up-to-date work lives on
  origin/claude/midnight. Fast-forward local claude/midnight to it, do the batch
  there, push claude/midnight, and delete the stray (local + remote/tracking ref).
  Do not spin off new branches.
