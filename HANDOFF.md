# HANDOFF — Midnight (子夜), Mao Dun

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Midnight B08

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Work only on branch claude/midnight. Build the
deliverable as out/Midnight.epub (the builder defaults to out/book.epub, so pass
the path explicitly on every build and every qa run).

data/src/ is regenerable and git-ignored, so if it is missing run
scripts/ingest_epub.py source.epub first to recreate it (Chapters One through
Seven are already translated; do not redo them).

Do Batch B08 = Chapter Eight (unit ch08) end to end. Read the source from
data/src/11_part0009.txt; it is authoritative. Quote it verbatim in the bilingual
QC file and render it faithfully and in full into English in the book's own
novelistic register. Chapter Eight is the longest chapter so far (16,002 source
chars); do not rush the parity.

Chapter Eight carries NONE of the source's own endnotes (the next author notes are
[8][9], both in ch11). So this batch touches source_notes.json only if you find an
inline [n] marker in the source of ch08 (you should not, and a grep of the source
confirms it). Do NOT invent one.

Author out/ch08_bilingual.md (a "## H2 Chapter Eight" line, then per source
paragraph a "> <verbatim source>" line and the English beneath). The safe way to
get verbatim source and exact paragraph parity is to write the English one
paragraph per line and zip it against the source body lines with a short script
(this is how B01-B07 did it: read data/src/11_part0009.txt, drop line 1 = the
title 八, and the rest are the body paragraphs; assert the English line count
equals the body line count BEFORE zipping, then write the bilingual). B07 dropped
one paragraph mid-draft and the pre-zip assertion caught it, so keep that guard.
Then run:
  python3 scripts/split_bilingual.py out/ch08_bilingual.md ch08 "八"
  python3 scripts/check_numbers.py out/ch08_bilingual.md --noise data/noise_zh.txt
  python3 scripts/check_structure.py --pairs data/zh/ch08.txt out/ch08_reading.md
When check_numbers flags a non-quantity numeral (idiom, slang, set phrase, a name
with a digit, a shape-word, an approximate range, a compound the checker cannot sum,
an intensifier, an ordinal date the word-list lacks), add a regex for it to
data/noise_zh.txt with a one-line reason; do not silence a real dropped number. The
noise file already carries a generous ch01..ch07 block, so many recurring items are
handled (the tael 两 after a price; a 万 not preceded by a numeral; 三先生 the Third
Master; 成千成百; 一不做二不休; the 十来 "about ten" marker; the 十钟/十半 clock residues;
names like A Er/Qiliqiao/Li Si; 第三者/三角形/十足; and the habits below).
Number-rendering habits that keep the checker clean: render 十万 as "one hundred
thousand" (not "a hundred thousand", which the checker cannot sum), spell a compound
the checker can parse or whitelist the source form (it cannot sum compound
hundreds/hundred-thousands or teen-thousands in spelled English), render 二人/两位/
两姊妹/两个 "the two of them / the two sisters / these two" so the count 2 stays
visible, and give a "十几X" as "ten-odd X" so the 十 is accounted (the built-in
几-measure stripper eats 几X first and would otherwise orphan the 十; if the residue
reads 十来, the ch07 十来 rule now clears it). A hanzi ordinal like 第二十三 is safest
rendered with the digits ("No. 23"), and frame/order numbers (九号, 第十号) with digits.

Add translator footnotes to notes.json under "ch08" at about chapter density (~3-6;
anchors must be verbatim substrings of the English prose; XHTML bodies use NUMERIC
character references for punctuation and dashes, never named entities; literal
Chinese is fine). ch07's translator notes were builder-numbered 39-43, so ch08's
continue from 44. Add every new proper noun / place / firm / term to glossary.json
with one rendering per referent and a status. Reuse the names and vocabulary already
fixed in glossary.json (Wu Sunfu, old Mr. Wu, Du Zhuzhai/Fufang, Lin Peiyao/the Wu
young mistress, Lin Peishan, Huifang/the Fourth Young Lady, Ah Xuan, Fan Bowen, Wu
Zhisheng, Du Xueshi, Du Xintuo, Zhang Susu, Li Yuting, Zhao Botao, Shang Zhongli,
Han Mengxiang, the combine cast Sun Jiren/Wang Hefu/Tang Yunshan, the silk-and-bank
cast Zhu Yinqiu/Chen Junyi/Zhou Zhongwei, the filature staff Tu Weiyue/Mo Gancheng/
Yao Jinfeng/Xue Baozhu/Wang Jinzhen/pockmarked Li/Qian Baosheng/Gui Changlin/He
Xiumei/A Zhen, plus the bond-market, silk-trade, filature and combine terms).
Note for glossary NOTE bodies: use plain Unicode punctuation, NOT numeric refs,
because the builder esc()s glossary notes (a "&#8216;" there renders as literal text;
see PROGRESS B02 read-through).

Rebuild with build_reading_epub.py out/Midnight.epub (the TOC stays pending-aware:
Chapters One through Eight link their content, every other unit still links its
skeleton outline), run qa_epub.py out/Midnight.epub until green, commit on
claude/midnight, and rewrite HANDOFF.md with the B09 kickoff. Cite chapters, never
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
  source note [4] (Mammon). Added the combine/filature terms and a ch05 noise block.
- B06 = Chapter Six (ch06): done. out/ch06_reading.md; translator notes 34-38;
  source notes [5][6][7] (feiyangsan/poetic and love/Monsieur Zeng). Added Du Xintuo,
  Qu Yuan, Jessfield Park, the Dalai Hotel, and the Bakuninism/万能博士/布尔乔亚/Nobel
  terms; ch06 noise block.
- B07 = Chapter Seven (ch07): done. out/ch07_reading.md; translator notes 39-43
  (Dawes/Young; 用人不疑; 反间计; 洪门; 人生如朝露); NO source notes. Added the mill/union
  cast (Qian Baosheng, Gui Changlin, He Xiumei, A Zhen), Yunqing, Mr. Wang (=Wang
  Jingwei), Dawes/Young, the Bankers' Guild, the Tongyuan native bank, the Hongmen,
  Hong Kong/America/England/Japan, and the filature/finance terms (overseer,
  inspector, naphtha-launch, loafer, industrial bonds, 反间计, finance/industrial
  capital); ch07 noise block (三先生; 成千成百; 一不做二不休; 十来; 十钟/十半). qa green,
  43 notes. See PROGRESS.md for the full record.

## What is NEXT

- Batch B08 = Chapter Eight (ch08), 16,002 source chars (the longest yet), and no
  source notes. See the kickoff above.

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
  by the builder in reading order; ch07 got 39-43, so ch08's translator notes
  continue from 44) and the source's own notes (source_notes.json, the author's
  own [n]). Never merge them. ch08 has NO source notes.
- book.json is the LOGICAL structure. The source cover, colophon (part0000) and
  the source's own table of contents (part0001) are not translatable units.
- Paragraph parity is enforced: one English paragraph per source paragraph. The
  bilingual file's "## H2 <title>" line is the chapter title and is not a
  paragraph pair. Zip English-per-line against the source body to keep parity
  structural, and assert the counts match BEFORE writing the bilingual (this
  caught a dropped paragraph in B03 and again in B07).
- check_numbers note-body rule vs glossary-note rule differ: notes.json /
  source_notes.json bodies are inserted RAW, so use numeric char refs for
  punctuation. glossary.json note bodies are esc()d, so use plain Unicode
  punctuation.
- The checker cannot sum compound hundreds/hundred-thousands or teen-thousands in
  spelled-out English, reads a hanzi numeral in a name as a count, and its
  word-list has no arbitrary ordinals. NOISE ORDER IS LOAD-BEARING: a longer token
  must be stripped before a shorter rule that is a prefix of it. Known traps now in
  the file: 一百二十个 before 一百二; 十几X orphaning 十 (render "ten-odd X", and the
  十来 rule clears a 十来 residue); 十一点 orphaning 十 (十钟/十半 residue rules); a
  bare 万 needs a numeral before it. When the checker flags a number that IS
  faithfully in the translation, add a documented noise regex (or render it in a
  form the checker parses); when it flags a genuinely missing number, fix the
  translation.
- When building the bilingual, write the English to a scratch file one paragraph
  per line and zip it against the source body with a Python script; keep the scratch
  files out of git (use the scratchpad dir).
- Branch hygiene: one branch only, claude/midnight. Each batch has arrived on a
  stray claude/midnight-b<nn>-* branch identical to origin/claude/midnight; the
  up-to-date work lives on origin/claude/midnight. Fast-forward local
  claude/midnight to it, do the batch there, push claude/midnight, and delete the
  stray (local + remote/tracking ref). Do not spin off new branches.
