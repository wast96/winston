# HANDOFF — Midnight (子夜), Mao Dun

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Midnight B06

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Work only on branch claude/midnight. Build the
deliverable as out/Midnight.epub (the builder defaults to out/book.epub, so pass
the path explicitly on every build and every qa run).

data/src/ is regenerable and git-ignored, so if it is missing run
scripts/ingest_epub.py source.epub first to recreate it (Chapters One through
Five are already translated; do not redo them).

Do Batch B06 = Chapter Six (unit ch06) end to end. Read the source from
data/src/09_part0007.txt; it is authoritative. Quote it verbatim in the bilingual
QC file and render it faithfully and in full into English in the book's own
novelistic register.

Chapter Six carries THREE of the source's own endnotes: [5], [6], [7]. Their exact
wording is in data/src/24_part0022.txt (the file that collects the nine author
notes): [5] "绯洋伞" = a transliteration of an English word meaning "fiancée"; [6]
"Poetic and love" = "诗意与恋爱"; [7] "麦歇曾" = French "Monsieur Zeng" (Du Xintuo
studied in France, hence the habit). Find each inline marker [5][6][7] in the
source of ch06, render each as the SOURCE's own note (distinct from your translator
footnotes), and add all three to source_notes.json under "ch06" with their ORIGINAL
numbers 5, 6, 7. See how ch01's [1][2], ch02's [3] and ch05's [4] were done in
source_notes.json for the shape.

Author out/ch06_bilingual.md (a "## H2 Chapter Six" line, then per source paragraph
a "> <verbatim source>" line and the English beneath). The safe way to get verbatim
source and exact paragraph parity is to write the English one paragraph per line and
zip it against the source body lines with a short script (this is how B01-B05 did it:
read data/src/09_part0007.txt, drop line 1 = the title 六, and the rest are the body
paragraphs; assert the English line count equals the body line count BEFORE zipping,
then write the bilingual). Then run:
  python3 scripts/split_bilingual.py out/ch06_bilingual.md ch06 "六"
  python3 scripts/check_numbers.py out/ch06_bilingual.md --noise data/noise_zh.txt
  python3 scripts/check_structure.py --pairs data/zh/ch06.txt out/ch06_reading.md
When check_numbers flags a non-quantity numeral (idiom, slang, set phrase, a name
with a digit, a shape-word, an approximate range, a compound the checker cannot sum,
an intensifier like 十二分/一百二十分, an ordinal date the word-list lacks), add a regex
for it to data/noise_zh.txt with a one-line reason; do not silence a real dropped
number. The noise file already carries a generous ch01+ch02+ch03+ch04+ch05 block, so
many recurring items are handled (the tael 两 after a price; a 万 not preceded by a
numeral; names like A Er/Qiliqiao/Li Si; and the general habits below).
Number-rendering habits that keep the checker clean: render 十万 as "one hundred
thousand" (not "a hundred thousand", which the checker cannot sum), spell a compound
the checker can parse or whitelist the source form (it cannot sum compound
hundreds/hundred-thousands or teen-thousands in spelled English), and render 二人/两位
"the two of them" so the count 2 stays visible.

Add translator footnotes to notes.json under "ch06" at about chapter density (~3-6;
anchors must be verbatim substrings of the English prose; XHTML bodies use NUMERIC
character references for punctuation and dashes, never named entities; literal
Chinese is fine). ch05's translator notes were builder-numbered 28-33, so ch06's
continue from 34. Add every new proper noun / place / firm / term to glossary.json
with one rendering per referent and a status. Reuse the names and vocabulary already
fixed in glossary.json (Wu Sunfu, old Mr. Wu, Du Zhuzhai, Lin Peiyao/the Wu young
mistress, Lin Peishan, Ah Xuan, Fan Bowen, Zhao Botao, Shang Zhongli, the
silk-and-bank cast Sun Jiren, Wang Hefu, Zhu Yinqiu, Chen Junyi, Zhou Zhongwei, Tang
Yunshan; the filature staff Tu Weiyue, Mo Gancheng, Wang Jinzhen, pockmarked Li; Du
Xueshi; plus the bond-market, silk-trade and combine terms). Watch for Du Xintuo
(杜新箨, the France-returned dandy of source note [7]) and any new Wu-house guests.
Note for glossary NOTE bodies: use plain Unicode punctuation, NOT numeric refs,
because the builder esc()s glossary notes (a "&#8216;" there renders as literal text;
see PROGRESS B02 read-through).

Rebuild with build_reading_epub.py out/Midnight.epub (the TOC stays pending-aware:
Chapters One through Six link their content, every other unit still links its
skeleton outline), run qa_epub.py out/Midnight.epub until green, commit on
claude/midnight, and rewrite HANDOFF.md with the B07 kickoff. Cite chapters, never
page numbers. Never invent bridging text. Do not pause for approval mid-batch.
Deliver out/Midnight.epub in chat as an attached file.
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
  no source note. Added the Shuangqiao cast, places/firms, rural-order terms, and
  a ch04 noise block (names read as counts + 一万二).
- B05 = Chapter Five (ch05): done. out/ch05_reading.md; translator notes 28-33;
  source note [4] (Mammon = the god of wealth). Added Sun Yat-sen/Li Hongzhang/
  Zhang Zhidong, Hangzhou/Su Causeway/West Lake/Great Eastern Port, and the combine
  and filature terms (建国方略, 四大干路, 期丝, 米贴, 赏工, 信托公司, 公债套利, 工会,
  铜牌子). ch05 noise block added (四射; 一百五十万; 十九日; 一百二; 一万八千; 九百八十).
  qa green, 33 notes. See PROGRESS.md for the full record.

## What is NEXT

- Batch B06 = Chapter Six (ch06), 12,137 source chars, and its source notes
  [5][6][7]. See the kickoff above.

## Where the source's own notes fall (for planning)

The nine author endnotes (exact wording in data/src/24_part0022.txt) are keyed
inline as follows: [1][2] ch01 (done); [3] ch02 (done); [4] ch05 (done);
[5][6][7] ch06 (NEXT); [8][9] ch11. All OTHER chapters (ch03, ch04 done) carry none.
Each remaining one goes into source_notes.json under its unit id with its ORIGINAL
number, never into notes.json.

## State / traps

- Deliverable filename: out/Midnight.epub. The builder and qa default to
  out/book.epub; always pass out/Midnight.epub explicitly.
- Two note streams, kept apart: translator footnotes (notes.json, numbered 1..N
  by the builder in reading order; ch05 got 28-33, so ch06's translator notes
  continue from 34) and the source's own notes (source_notes.json, the author's
  own [n]). Never merge them. ch06 has source notes [5][6][7].
- book.json is the LOGICAL structure. The source cover, colophon (part0000) and
  the source's own table of contents (part0001) are not translatable units.
- Paragraph parity is enforced: one English paragraph per source paragraph. The
  bilingual file's "## H2 <title>" line is the chapter title and is not a
  paragraph pair. Zip English-per-line against the source body to keep parity
  structural, and assert the counts match BEFORE writing the bilingual (this
  caught a dropped paragraph in B03). Note that verse on separate source lines
  counts as separate paragraphs (the ch05 quatrain was four).
- check_numbers note-body rule vs glossary-note rule differ: notes.json /
  source_notes.json bodies are inserted RAW, so use numeric char refs for
  punctuation. glossary.json note bodies are esc()d, so use plain Unicode
  punctuation.
- The checker cannot sum compound hundreds/hundred-thousands or teen-thousands in
  spelled-out English, reads a hanzi numeral in a name as a count, and its
  word-list has no arbitrary ordinals (十九日 = "the nineteenth" had to be
  whitelisted). Also note a built-in stripper interaction: 十分 (=very) is stripped
  inside 一百二十分, leaving a residue 一百二 that must itself be whitelisted. When the
  checker flags a number that IS faithfully in the translation, add a documented
  noise regex (or render it in a form the checker parses); when it flags a genuinely
  missing number, fix the translation.
- When building the bilingual, write the English to a scratch file one paragraph
  per line and zip it against the source body with a Python script; keep the scratch
  files out of git (use the scratchpad dir).
- Branch hygiene: one branch only, claude/midnight. A stray
  claude/midnight-b05-ch05-* branch appeared at the B05 kickoff; its (identical)
  history was already on claude/midnight, and it was deleted (local + tracking ref
  pruned; it never existed on the remote). Do not spin off new branches.
