# HANDOFF — Midnight (子夜), Mao Dun

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Midnight B12

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Work only on branch claude/midnight. Build the
deliverable as out/Midnight.epub (the builder defaults to out/book.epub, so pass
the path explicitly on every build and every qa run).

data/src/ is regenerable and git-ignored, so if it is missing run
scripts/ingest_epub.py source.epub first to recreate it (Chapters One through
Eleven are already translated; do not redo them).

Do Batch B12 = Chapter Twelve (unit ch12) end to end. Read the source from
data/src/15_part0013.txt; it is authoritative. Quote it verbatim in the bilingual
QC file and render it faithfully and in full into English in the book's own
novelistic register. Chapter Twelve is 13,308 source chars (232 body paragraphs
after the title line 十二).

NO source notes in Chapter Twelve. The author's own endnote stream [1]..[9] is now
COMPLETE and fully placed (ch01 [1][2], ch02 [3], ch05 [4], ch06 [5][6][7], ch11
[8][9]); grep confirmed no inline [n] marker in ch12, and no remaining chapter
carries one. So source_notes.json is FROZEN: do not add to it. Everything you add
this batch is a TRANSLATOR footnote (notes.json) only. Still, grep the source for
\[\d+\] at the start as a habit, and if one ever appears, stop and reconcile
against book.json before proceeding.

Author out/ch12_bilingual.md (a "## H2 Chapter Twelve" line, then per source
paragraph a "> <verbatim source>" line and the English beneath). The safe way to
get verbatim source and exact paragraph parity is to write the English one
paragraph per line and zip it against the source body lines with a short script
(read data/src/15_part0013.txt, drop line 1 = the title 十二; the rest are the body
paragraphs; assert the English line count equals the body line count BEFORE
zipping, then write the bilingual). B03/B07/B09/B10/B11's pre-zip assertion each
caught a would-be dropped paragraph, so keep that guard and spot-check alignment at
a few paragraph indices before writing. Then run:
  python3 scripts/split_bilingual.py out/ch12_bilingual.md ch12 "十二"
  python3 scripts/check_numbers.py out/ch12_bilingual.md --noise data/noise_zh.txt
  python3 scripts/check_structure.py --pairs data/zh/ch12.txt out/ch12_reading.md
When check_numbers flags a non-quantity numeral (idiom, slang, set phrase, a name
or place with a digit in it, a shape-word like 十字, an approximate range, a
compound the checker cannot sum, an intensifier, an ordinal date the word-list
lacks), add a regex for it to data/noise_zh.txt with a one-line reason; do not
silence a real dropped number. The noise file already carries a generous ch01..ch11
block, so many recurring items are handled: 三先生, 四川, 十字, 大三元, 红头阿三 via
阿三, 斤两, 三马 for 三马路, 夹七夹八, 十二分, 杀千刀, 零碎, 忘八, the tael rules
(?<=百)两/(?<=十)两/(?<=万)两, the bare-百/bare-万 rules, and the clock residue
(?<=点)四. Number-rendering habits that keep the checker clean: render 十万 as "one
hundred thousand" (not "a hundred thousand", which the checker cannot sum); write
"a hundred/a thousand" WITH the article and "five hundred"/"one million" WITH A
SPACE (no hyphen); render two/pair as "the two of them" so 2 stays visible; render
五六万 "fifty or sixty thousand" (60000) not "fifty thousand-odd" (五万多=50000);
ten-odd/ten-or-so for 十几X/十来X; render 二楼 "the second floor" so 二=2 stays; use
DIGITS for hanzi ordinals the word-list lacks (e.g. 十五号 -> "the 15th", since
"fifteenth" is not in the list; "fourth/tenth/seventeenth" ARE in the list) and for
any compound the checker cannot sum (e.g. 四百三十一 -> "431"); a bare 两 after a
price is the tael; a bare 百/万 not preceded by a numeral is cleared by the
bare-百/bare-万 rules. NOTE: the built-in 十[分] strip eats the 十分 out of a "X十分"
clock reading; if a clock loses its tens like that, render it with digits and add a
targeted residue rule as B09 did with (?<=点)四. And any compound the checker
mis-sums (a teen-myriad + thousand like 十九万五千, a 一万五 read as 10005) gets a
documented noise line, exactly as B10 did.

Add translator footnotes to notes.json under "ch12" at about chapter density (~3-6;
anchors must be verbatim substrings of the English prose; XHTML bodies use NUMERIC
character references for punctuation and dashes, never named entities; literal
Chinese is fine). ch11's translator notes were builder-numbered 62-66, so ch12's
continue from 67. There is only ONE note stream now (translator, in notes.json,
builder-numbered 1..N in reading order); source_notes.json is frozen.
Add every new proper noun / place / firm / term to glossary.json with one rendering
per referent and a status. Reuse the names and vocabulary already fixed in
glossary.json: the Wu-family and combine cast; the bond-market cast (Zhao Botao /
老赵, Shang Zhongli, Han Mengxiang, Zhu Yinqiu, Du Zhuzhai, Li Zhuangfei, Lu
Kuangshi, He Shen'an, Liu Yuying); the young set (Zhang Susu, Wu Zhisheng, Boqing,
Fan Bowen, Lin Peishan, Du Xintuo/阿新, Du Xueshi/老六, Li Yuting, Ke Zhongmou); Tang
Yunshan, Huang Fen; the ch10-ch11 additions (Peng Dehuai, the Red Army/红军, the
Iron Army/铁军, Soviet/苏维埃, San Malu, the Chinese Securities Exchange, Feng Yunqing,
Feng Meiqing, Old Ninth, Avenue Joffre/霞飞路, Avenue Edward VII/爱多亚路, the
Tianjin-Pukou line/津浦线, the Beiyang government/北洋政府); and the terms 公债/多头/
空头/交割/停板/补进/涨风/编遣/快报, 五卅 / 三道头 / 红头阿三 / 白俄. Note for glossary
NOTE bodies: use plain Unicode punctuation, NOT numeric refs, because the builder
esc()s glossary notes (a "&#8216;" there renders as literal text). notes.json note
bodies, by contrast, are inserted RAW - use numeric char refs there. And WRITE
glossary/notes JSON via a Python file, then RE-READ to verify the Chinese: a shell
heredoc mangled 钱庄 in B08, and B10 caught a 亨->享 slip only by re-reading.

Rebuild with build_reading_epub.py out/Midnight.epub (the TOC stays pending-aware:
Chapters One through Twelve link their content, every other unit still links its
skeleton outline), run qa_epub.py out/Midnight.epub until green, commit on
claude/midnight, and rewrite HANDOFF.md with the B13 kickoff. Cite chapters, never
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
- B11 = Chapter Eleven (ch11): done. out/ch11_reading.md; translator notes 62-66
  (rising wind/涨风 pun; the dog biting Lu Dongbin/狗咬吕洞宾; the Western Gaol/西牢;
  bottom-of-the-chest money/垫箱钱; the window-blind fortune-omen). 205 paragraphs;
  the LAST TWO author source notes [8][9] placed (source_notes.json "ch11": [8] on
  "Reds threaten Hankow, reported!", [9] on "Jiamen"/茄门). All nine author notes
  [1]..[9] now built (snote1..snote9). Added the ch11 cast/places/terms (Liu Yuying,
  He Shen'an, Avenue Joffre, Avenue Edward VII, the Tianjin-Pukou line, Shanxi, the
  Western Gaol, the Customs House, the North China Daily News, the Beiyang
  government, rising wind/涨风, Jiamen/茄门, the Seven-Year Long-Term and Ninety-Six
  Bonds, bottom-of-the-chest money, bulletin/快报), plus a ch11 noise block
  (杀千刀, 零碎, 忘八). qa green, 66 notes. See PROGRESS.md for the full record.

## What is NEXT

- Batch B12 = Chapter Twelve (ch12), 13,308 source chars (232 body paragraphs), NO
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
  the builder in reading order; ch11 got 62-66, so ch12's continue from 67).
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
  and RE-READ to verify the Chinese glyphs (B10 caught a 亨->享 slip only on the
  re-read).
- The checker cannot sum compound hundreds / hundred-thousands / teen-thousands in
  spelled English, SUMS an adjacent compound (三千五千 -> 8000; 一万五 -> 10005;
  四百三十一 -> 400+31 unmatched), reads a hanzi numeral in a name/place as a count
  (四川, 大三元, 阿三, 三马路), reads "the hundred" as no numeral, needs a SPACE in
  "five hundred"/"one million" and the article in "a hundred", and its word-list has
  limited ordinals ("fourth/tenth/sixteenth/seventeenth/thirtieth" yes; "fifteenth"
  NO - use digits). NOISE ORDER IS LOAD-BEARING: a longer token must be stripped
  before a shorter rule that is a prefix of it. When the checker flags a number that
  IS faithfully in the translation, reword to a form it parses OR add a documented
  noise regex; when it flags a genuinely missing number, fix the translation.
- When building the bilingual, write the English to a scratch file one paragraph
  per line and zip it against the source body with a Python script; keep the scratch
  files out of git (use the scratchpad dir).
- Branch hygiene: one branch only, claude/midnight. Each batch has arrived on a
  stray claude/midnight-b<nn>-* branch; the up-to-date work lives on
  origin/claude/midnight. Fast-forward local claude/midnight to it, do the batch
  there, push claude/midnight, and delete the stray (local + remote/tracking ref).
  Do not spin off new branches.
