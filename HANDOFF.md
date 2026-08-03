# HANDOFF — Midnight (子夜), Mao Dun

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Midnight B13

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Work only on branch claude/midnight. Build the
deliverable as out/Midnight.epub (the builder defaults to out/book.epub, so pass
the path explicitly on every build and every qa run).

data/src/ is regenerable and git-ignored, so if it is missing run
scripts/ingest_epub.py source.epub first to recreate it (Chapters One through
Twelve are already translated; do not redo them).

Do Batch B13 = Chapter Thirteen (unit ch13) end to end. Read the source from
data/src/16_part0014.txt; it is authoritative. Quote it verbatim in the bilingual
QC file and render it faithfully and in full into English in the book's own
novelistic register. Chapter Thirteen is 10,419 source chars (190 body paragraphs
after the title line 十三).

NO source notes remain anywhere. The author's own endnote stream [1]..[9] is
COMPLETE and fully placed (ch01 [1][2], ch02 [3], ch05 [4], ch06 [5][6][7], ch11
[8][9]); grep of data/src/16_part0014.txt for a leading [n] returned nothing. So
source_notes.json is FROZEN: do not add to it. Everything you add this batch is a
TRANSLATOR footnote (notes.json) only. Still, grep the source for \[\d+\] at the
start as a habit, and if one ever appears, stop and reconcile against book.json
before proceeding.

Author out/ch13_bilingual.md (a "## H2 Chapter Thirteen" line, then per source
paragraph a "> <verbatim source>" line and the English beneath). The safe way to
get verbatim source and exact paragraph parity is to write the English one
paragraph per line into a scratch file (use the scratchpad dir, keep it out of git)
and zip it against the source body lines with a short script (read
data/src/16_part0014.txt, drop line 1 = the title 十三; the rest are the body
paragraphs; assert the English line count equals the body line count BEFORE
zipping, then write the bilingual). B03/B07/B09/B10/B11/B12's pre-zip assertion each
caught a would-be dropped paragraph, so keep that guard and spot-check alignment at
a few paragraph indices before writing. Then run:
  python3 scripts/split_bilingual.py out/ch13_bilingual.md ch13 "十三"
  python3 scripts/check_numbers.py out/ch13_bilingual.md --noise data/noise_zh.txt
  python3 scripts/check_structure.py --pairs data/zh/ch13.txt out/ch13_reading.md
When check_numbers flags a non-quantity numeral (idiom, slang, set phrase, a name
or place with a digit in it, a shape-word like 十字, an approximate range, a
compound the checker cannot sum, an intensifier, an ordinal date the word-list
lacks), add a regex for it to data/noise_zh.txt with a one-line reason; do not
silence a real dropped number. When it flags a number that IS faithfully present,
reword to a form the checker parses OR add a documented noise line; when it flags a
genuinely missing number, FIX THE TRANSLATION (B12 caught 二十万 mis-rendered as
"twenty thousand" — it is 200,000, "two hundred thousand"). The noise file already
carries a generous ch01..ch12 block, so many recurring items are handled: 三先生,
四川, 十字, 大三元, 红头阿三 via 阿三, 斤两, 三马 for 三马路, 夹七夹八, 十二分,
杀千刀, 零碎 (twice, the ch12 dup clears the 零零碎碎 residue), 忘八, 瘪三, 二成/六成,
第二天, the tael rules (?<=百)两 / (?<=十)两 / (?<=万)两 / (?<=百多)两, the bare-百 /
bare-万 rules, and the clock residue (?<=点)四.

Number-rendering habits that keep the checker clean: render 十万 as "one hundred
thousand" and 二十万 as "two hundred thousand" (a bare 十万/二十万 is 100,000 /
200,000, NOT ten/twenty thousand — this is the exact trap B12 hit); render 三十万 as
"three hundred thousand", 八十万 as "eight hundred thousand", 四十多万 as "four
hundred thousand and more"; write "a hundred/a thousand" WITH the article and "five
hundred"/"one million" WITH A SPACE (no hyphen); render X成 (a tenth) and X折 (a
discount) in WORDS as "X-tenths" so the digit survives (八折 -> "eight-tenths",
九折 -> "nine-tenths") — do NOT write "eighty per cent", which loses the 8; render
two/pair as "the two of them" so 2 stays visible; render 五六万 "fifty or sixty
thousand" (60000) not "fifty thousand-odd"; ten-odd/ten-or-so for 十几X/十来X; use
DIGITS for hanzi ordinals the word-list lacks (十五号 -> "the 15th") and for any
compound the checker cannot sum (二百五十 -> "250"; 四百三十一 -> "431"); a bare 两
after a price is the tael. NOTE: the built-in 十[分] strip eats the 十分 out of a
"X十分" clock reading; if a clock loses its tens, render it with digits and add a
targeted residue rule as B09 did with (?<=点)四.

Add translator footnotes to notes.json under "ch13" at about chapter density (~3-6;
anchors must be verbatim substrings of the English prose — verify by grep before
building; XHTML bodies use NUMERIC character references for punctuation and dashes,
never named entities; literal Chinese is fine). ch12's translator notes were
builder-numbered 67-72, so ch13's continue from 73. There is only ONE note stream
now (translator, in notes.json, builder-numbered 1..N in reading order);
source_notes.json is frozen.
Add every new proper noun / place / firm / term to glossary.json with one rendering
per referent and a status. Reuse the names and vocabulary already fixed in
glossary.json: the Wu-family and combine cast; the bond-market cast (Zhao Botao /
老赵, Shang Zhongli, Han Mengxiang, Liu Yuying, Xu Manli, Lu Kuangshi); the Yizhong
partners (Wang Hefu, Sun Jiren, Huang Fen, Tang Yunshan/云山); the mill cast (Tu
Weiyue/三先生, Qian Baosheng); the ch12 additions (Yan Xishan, the Yuanda native
bank, Dezhou, Jinan, Xuzhou, Hongkou, Zhabei, the Northern Enlarged Conference, the
general sympathetic strike/总同盟罢工, held-back pay/存工, the plum-rain season/黄梅天,
the Industrial Plan/实业计划); and the terms 公债/多头/空头/交割/停板/补进/涨风/快报,
五卅 / 三道头 / 红头阿三 / 白俄. Chapter Thirteen is the strike chapter (the silk
filatures), so expect the mill-and-union cast (姚金凤, 何秀妹, 钱葆生, 桂长林,
王金贞, 薛宝珠, 朱桂英 and the like) — most are already in glossary.json; check before
you romanize. NOTE for glossary NOTE bodies: use plain Unicode punctuation, NOT
numeric refs, because the builder esc()s glossary notes. notes.json note bodies, by
contrast, are inserted RAW — use numeric char refs there. And WRITE glossary/notes
JSON via a Python file, then RE-READ to verify the Chinese (a shell heredoc mangled
钱庄 in B08, and B10 caught a 亨->享 slip only by re-reading).

Rebuild with build_reading_epub.py out/Midnight.epub (the TOC stays pending-aware:
Chapters One through Thirteen link their content, every other unit still links its
skeleton outline), run qa_epub.py out/Midnight.epub until green, commit on
claude/midnight, and rewrite HANDOFF.md with the B14 kickoff. Cite chapters, never
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
- B12 = Chapter Twelve (ch12): done. out/ch12_reading.md; translator notes 67-72
  (Uncle/表叔 address joke; Big Cannon/大炮 = Huang Fen's nickname; the White
  Wuchang/白无常; Ramona/雷梦娜; the Industrial Plan/实业计划; the plum-rain
  season/黄梅天). 232 paragraphs; NO source notes. Fixed a real number error
  (二十万 = 200,000, not "twenty thousand"). Added the ch12 cast/places/terms
  (Yan Xishan, the Yuanda native bank, Dezhou, Jinan, Xuzhou, Hongkou, Zhabei, the
  Northern Enlarged Conference, general sympathetic strike, held-back pay, Ramona,
  Big Cannon, the White Wuchang, the plum-rain season, the Industrial Plan) plus a
  ch12 noise block (瘪三, 二千五六百, 六成, 二成, 第二天, the 零碎 dup, (?<=百多)两).
  qa green, 72 notes. See PROGRESS.md for the full record.

## What is NEXT

- Batch B13 = Chapter Thirteen (ch13), 10,419 source chars (190 body paragraphs), NO
  source notes (the author-note stream is complete). See the kickoff above.

## The source's own notes are COMPLETE (for planning)

The nine author endnotes (exact wording in data/src/24_part0022.txt) are all placed:
[1][2] ch01; [3] ch02; [4] ch05; [5][6][7] ch06; [8][9] ch11. source_notes.json is
FROZEN. All OTHER chapters (ch03, ch04, ch07..ch10, ch12..ch20) carry none. From
B12 on there is only ONE note stream: the translator footnotes in notes.json.

## State / traps

- Deliverable filename: out/Midnight.epub. The builder and qa default to
  out/book.epub; always pass out/Midnight.epub explicitly.
- Only one note stream remains: translator footnotes (notes.json, numbered 1..N by
  the builder in reading order; ch12 got 67-72, so ch13's continue from 73).
  source_notes.json is complete and frozen; do not add to it.
- book.json is the LOGICAL structure. The source cover, colophon (part0000) and
  the source's own table of contents (part0001) are not translatable units.
- Paragraph parity is enforced: one English paragraph per source paragraph. The
  bilingual file's "## H2 <title>" line is the chapter title and is not a
  paragraph pair. Zip English-per-line against the source body to keep parity
  structural, and assert the counts match BEFORE writing the bilingual. Spot-check
  alignment at a few indices too.
- check_numbers note-body rule vs glossary-note rule differ: notes.json bodies are
  inserted RAW, so use numeric char refs for punctuation. glossary.json note bodies
  are esc()d, so use plain Unicode punctuation. WRITE all of them via a Python file
  and RE-READ to verify the Chinese glyphs.
- The BIG number trap (B12): a bare 十万/二十万/三十万 is 100,000 / 200,000 / 300,000,
  NOT ten/twenty/thirty thousand. Render X万 as (X hundred thousand) when X < 10.
  When check_numbers reports a genuinely missing quantity, fix the translation, do
  not add noise.
- The checker cannot sum compound hundreds / hundred-thousands / teen-thousands in
  spelled English, SUMS an adjacent compound (三千五千 -> 8000; 二千五六百 -> 2600),
  reads a hanzi numeral in a name/place as a count (四川, 大三元, 阿三, 三马路, 瘪三),
  reads a X成/X折 as a bare digit, needs a SPACE in "five hundred"/"one million" and
  the article in "a hundred", and its word-list has limited ordinals
  ("fourth/tenth/sixteenth/seventeenth/thirtieth" yes; "fifteenth" NO - use digits).
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
