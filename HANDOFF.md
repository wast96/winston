# HANDOFF — Midnight (子夜), Mao Dun

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Midnight B10

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Work only on branch claude/midnight. Build the
deliverable as out/Midnight.epub (the builder defaults to out/book.epub, so pass
the path explicitly on every build and every qa run).

data/src/ is regenerable and git-ignored, so if it is missing run
scripts/ingest_epub.py source.epub first to recreate it (Chapters One through
Nine are already translated; do not redo them).

Do Batch B10 = Chapter Ten (unit ch10) end to end. Read the source from
data/src/13_part0011.txt; it is authoritative. Quote it verbatim in the bilingual
QC file and render it faithfully and in full into English in the book's own
novelistic register. Chapter Ten is 13,366 source chars (230 body paragraphs
after the title line).

Chapter Ten carries NONE of the source's own endnotes (the only remaining author
notes are [8][9], both in ch11). So this batch touches source_notes.json only if
you find an inline [n] marker in the source of ch10 (you should not; grep the
source to confirm). Do NOT invent one.

Author out/ch10_bilingual.md (a "## H2 Chapter Ten" line, then per source
paragraph a "> <verbatim source>" line and the English beneath). The safe way to
get verbatim source and exact paragraph parity is to write the English one
paragraph per line and zip it against the source body lines with a short script
(read data/src/13_part0011.txt, drop line 1 = the title 十; the rest are the body
paragraphs; assert the English line count equals the body line count BEFORE
zipping, then write the bilingual). B03/B07/B09's pre-zip assertion each caught a
would-be dropped paragraph, so keep that guard and spot-check alignment at a few
paragraph indices before writing. Then run:
  python3 scripts/split_bilingual.py out/ch10_bilingual.md ch10 "十"
  python3 scripts/check_numbers.py out/ch10_bilingual.md --noise data/noise_zh.txt
  python3 scripts/check_structure.py --pairs data/zh/ch10.txt out/ch10_reading.md
When check_numbers flags a non-quantity numeral (idiom, slang, set phrase, a name
or place with a digit in it, a shape-word like 十字, an approximate range, a
compound the checker cannot sum, an intensifier, an ordinal date the word-list
lacks), add a regex for it to data/noise_zh.txt with a one-line reason; do not
silence a real dropped number. The noise file already carries a generous
ch01..ch09 block, so many recurring items are handled (北四川路 via 四川, 十字街头
via 十字, 大三元, 红头阿三 via 阿三, 斤两, and the clock residue rule (?<=点)四). Number-
rendering habits that keep the checker clean: render 十万 as "one hundred thousand"
(not "a hundred thousand", which the checker cannot sum); write "a hundred/a
thousand" WITH the article; render an adjacent compound like 三千五千 in words and
whitelist the source form (the checker SUMS it into 8000); render 两个/两位/父女两个
"the two of them" so 2 stays visible; ten-odd/ten-or-so for 十几X/十来X; use DIGITS
for hanzi ordinals and for clock/frame numbers (九号, 十六, 9:40); a bare 两 after a
price is the tael (cleared by the (?<=百)两 / (?<=十)两 / (?<=万)两 rules); a bare 百/万
not preceded by a numeral is cleared by the ch03/ch08 bare-百/bare-万 rules. NOTE:
the built-in 十[分] strip eats the 十分 out of a "X十分" clock reading and out of
四十分 etc.; if a clock loses its tens like that, render it with digits and add a
targeted residue rule as B09 did with (?<=点)四.

Add translator footnotes to notes.json under "ch10" at about chapter density (~3-6;
anchors must be verbatim substrings of the English prose; XHTML bodies use NUMERIC
character references for punctuation and dashes, never named entities; literal
Chinese is fine). ch09's translator notes were builder-numbered 50-55, so ch10's
continue from 56. Add every new proper noun / place / firm / term to glossary.json
with one rendering per referent and a status. Reuse the names and vocabulary
already fixed in glossary.json: the Wu-family and combine cast; the bond-market
cast (Zhao Botao / 伯翁 / 老赵, Shang Zhongli, Han Mengxiang, Zhu Yinqiu, Du Zhuzhai,
Li Zhuangfei, Lu Kuangshi); the young set now fixed from ch09 (Zhang Susu, Wu
Zhisheng, Boqing, Fan Bowen, Lin Peishan, Du Xintuo/老箨, Du Xueshi/小杜/老六, Li
Yuting, Ke Zhongmou), Zhao Botao's mistress Liu Yuying (玉英), the Yizhong Trust
Company (益中信托公司), and the terms 五卅 / 三道头 / 红头阿三 / 白俄. Note for glossary
NOTE bodies: use plain Unicode punctuation, NOT numeric refs, because the builder
esc()s glossary notes (a "&#8216;" there renders as literal text). And WRITE
glossary/notes JSON via a Python file, then RE-READ to verify the Chinese: a shell
heredoc mangled 钱庄 in B08.

Rebuild with build_reading_epub.py out/Midnight.epub (the TOC stays pending-aware:
Chapters One through Ten link their content, every other unit still links its
skeleton outline), run qa_epub.py out/Midnight.epub until green, commit on
claude/midnight, and rewrite HANDOFF.md with the B11 kickoff. Cite chapters, never
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
- B09 = Chapter Nine (ch09): done. out/ch09_reading.md; translator notes 50-55
  (May Thirtieth / 五卅运动; 三道头; 红头阿三; Yuan Zhen 曾经沧海难为水; 猿鹤虫沙; 丢那妈).
  213 paragraphs. Added the ch09 cast (Boqing, Ke Zhongmou; Nero, Homer, Hector,
  Shakespeare, Wu Song, young Zhang = Zhang Xueliang), the Yizhong Trust Company
  (first named), the Sun Sun Company, the Da San Yuan, the Hua'an Building, the
  Louza police station, the Xin Shijie Hotel, and the many street/place names
  (Nichengqiao, the Racecourse, North Sichuan / Zhejiang / Yunnan Roads, the
  Risheng Lou, Changbang Road, the Majestic, the Liwalida, the Seine, Rome, Greece,
  France, Bengbu, Hubei/Jiangxi/Jiangsu/Zhejiang/Fujian, the Yangtze, Wen-Tai,
  Ning-Shao, Wuxue, Shashi, Tianjin, Guangzhou, Macau), plus terms 五卅 / 三道头 /
  红头阿三 / 白俄 / 马赛曲 / 张桂军, and a ch09 noise block (四川; 十字; 四散; 四伏; 大三元;
  阿三; 七猜八猜; 斤两; the clock residue (?<=点)四). One checker word added: "thirtieth"=30
  in check_numbers.py WORD_NUM. qa green, 55 notes. See PROGRESS.md for the full
  record.

## What is NEXT

- Batch B10 = Chapter Ten (ch10), 13,366 source chars (230 body paragraphs), and
  no source notes. See the kickoff above.

## Where the source's own notes fall (for planning)

The nine author endnotes (exact wording in data/src/24_part0022.txt) are keyed
inline as follows: [1][2] ch01 (done); [3] ch02 (done); [4] ch05 (done);
[5][6][7] ch06 (done); [8][9] ch11. All OTHER chapters (ch03, ch04, ch07..ch10,
ch12..ch20) carry none. Each remaining one goes into source_notes.json under its
unit id with its ORIGINAL number, never into notes.json. (Confirmed: [8][9] sit in
data/src/14_part0012.txt = ch11, next to "Reds threaten Hankow" and 丢那妈.)

## State / traps

- Deliverable filename: out/Midnight.epub. The builder and qa default to
  out/book.epub; always pass out/Midnight.epub explicitly.
- Two note streams, kept apart: translator footnotes (notes.json, numbered 1..N
  by the builder in reading order; ch09 got 50-55, so ch10's continue from 56) and
  the source's own notes (source_notes.json, the author's own [n]). Never merge
  them. ch10 has NO source notes.
- book.json is the LOGICAL structure. The source cover, colophon (part0000) and
  the source's own table of contents (part0001) are not translatable units.
- Paragraph parity is enforced: one English paragraph per source paragraph. The
  bilingual file's "## H2 <title>" line is the chapter title and is not a
  paragraph pair. Zip English-per-line against the source body to keep parity
  structural, and assert the counts match BEFORE writing the bilingual. Spot-check
  alignment at a few indices too. In ch09 the four verse lines of Du Xintuo's poem
  are four separate source paragraphs and got four separate English lines; watch
  for embedded verse/quoted matter that the source sets on its own lines.
- check_numbers note-body rule vs glossary-note rule differ: notes.json /
  source_notes.json bodies are inserted RAW, so use numeric char refs for
  punctuation. glossary.json note bodies are esc()d, so use plain Unicode
  punctuation. WRITE both via a Python file and RE-READ to verify the Chinese
  glyphs.
- The checker cannot sum compound hundreds/hundred-thousands or teen-thousands in
  spelled English, SUMS an adjacent compound like 三千五千 into 8000, reads a hanzi
  numeral in a name/place as a count (四川, 大三元, 阿三), reads "the hundred" as no
  numeral, and its word-list has no arbitrary ordinals (thirtieth was added for
  ch09). NOISE ORDER IS LOAD-BEARING: a longer token must be stripped before a
  shorter rule that is a prefix of it. When the checker flags a number that IS
  faithfully in the translation, add a documented noise regex (or render it in a
  form the checker parses); when it flags a genuinely missing number, fix the
  translation.
- When building the bilingual, write the English to a scratch file one paragraph
  per line and zip it against the source body with a Python script; keep the scratch
  files out of git (use the scratchpad dir).
- Branch hygiene: one branch only, claude/midnight. Each batch has arrived on a
  stray claude/midnight-b<nn>-* branch; the up-to-date work lives on
  origin/claude/midnight. Fast-forward local claude/midnight to it, do the batch
  there, push claude/midnight, and delete the stray (local + remote/tracking ref).
  Do not spin off new branches.
