# HANDOFF — Midnight (子夜), Mao Dun

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Midnight B18

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Work only on branch claude/midnight. Build the
deliverable as out/Midnight.epub (the builder defaults to out/book.epub, so pass
the path explicitly on every build and every qa run).

data/src/ is regenerable and git-ignored, so if it is missing run
scripts/ingest_epub.py source.epub first to recreate it (Chapters One through
Seventeen are already translated; do not redo them).

Do Batch B18 = the FINAL batch: Chapter Eighteen (ch18), Chapter Nineteen (ch19), and
the Afterword (ch20, 后记). This closes the book. Read the source, all authoritative,
from data/src/21_part0019.txt (ch18, 12,247 chars), data/src/22_part0020.txt (ch19,
5,137 chars), and data/src/23_part0021.txt (ch20, 452 chars). Quote each verbatim in
its bilingual QC file and render it faithfully and in full into the book's own
novelistic register. Total B18 is 17,836 source chars.

NO source notes remain anywhere. The author's own endnote stream [1]..[9] is COMPLETE
and fully placed (ch01 [1][2], ch02 [3], ch05 [4], ch06 [5][6][7], ch11 [8][9]). So
source_notes.json is FROZEN: do not add to it. Everything you add this batch is a
TRANSLATOR footnote (notes.json) only. Still, grep each source file for \[\d+\] at the
start as a habit, and if one ever appears, stop and reconcile against book.json before
proceeding.

Do EACH of the three units separately, end to end. For each unit <id> in ch18, ch19,
ch20: author out/<id>_bilingual.md (a "## H2 <English title>" line, then per source
paragraph a "> <verbatim source>" line and the English beneath). The safe way to get
verbatim source and exact paragraph parity is to write the English one paragraph per
line into a scratch file (use the scratchpad dir, keep it out of git) and zip it against
the source body lines with a short script (read the src .txt, DROP LINE 1 = the title
十八 / 十九 / 后记; the rest are the body paragraphs; the file may lack a trailing newline,
so filter blank lines and count non-empty lines; assert the English line count equals
the body line count BEFORE zipping, then write the bilingual). Every batch's pre-zip
assertion has caught a would-be dropped paragraph, so keep that guard and spot-check
alignment at several paragraph indices before writing. Then per unit run:
  python3 scripts/split_bilingual.py out/<id>_bilingual.md <id> "<zh title>"
  python3 scripts/check_numbers.py out/<id>_bilingual.md --noise data/noise_zh.txt
  python3 scripts/check_structure.py --pairs data/zh/<id>.txt out/<id>_reading.md
(zh titles: ch18 "十八", ch19 "十九", ch20 "后记".)
check_numbers only flags MISSING source numbers (extra English numbers are fine). When
it flags a non-quantity numeral (idiom, slang, a name/place with a digit, a shape-word
like 十字, an approximate range, a compound it cannot sum, an intensifier, an ordinal
the word-list lacks), add a regex for it to data/noise_zh.txt with a one-line reason;
do not silence a real dropped number. When it flags a number that IS faithfully present,
reword to a form the checker parses OR add a documented noise line; when it flags a
genuinely missing number, FIX THE TRANSLATION (B12 caught 二十万 mis-rendered as
"twenty thousand" - it is 200,000, "two hundred thousand"; B17 noised 二百五十万=2,500,000
and 五十二万=520,000, compound myriads the checker cannot sum, and 牌九 pai-gow). The noise
file already carries a generous ch01..ch17 block, so many recurring items are handled,
including the strike-chapter set, the launch-party set (牌九, 二百五十万, 五十二万), the tael
rules, the bare-百 / bare-万 rules, the clock residue (?<=点)四, and the like.

Number-rendering habits that keep the checker clean: render 十万 as "one hundred
thousand" and 二十万 as "two hundred thousand" (a bare 十万/二十万 is 100,000 / 200,000,
NOT ten/twenty thousand - the exact trap B12 hit); render 三十万 as "three hundred
thousand", 五十万 as "five hundred thousand", 六十万 as "six hundred thousand", 四十多万 as
"four hundred thousand and more"; write "a hundred/a thousand" WITH the article and
"five hundred"/"one million" WITH A SPACE (no hyphen); render X成 (a tenth) and X折 (a
discount) in WORDS as "X-tenths" so the digit survives; do NOT write "eighty per cent",
which loses the 8; render two/pair as "the two of them" so 2 stays visible (a bare
"couple"/"pair" does NOT satisfy the checker - use "two"; note "twice"/"both" DO satisfy
a 两); render a birth-order nickname so its digit survives (三先生 -> "the Third Master",
四小姐/四妹 -> ensure "Fourth" appears in EVERY paragraph that names her, 三哥 -> "Third
Brother", 六叔 -> "Sixth Uncle"); an ordinal survives as a word if the word-list has it
("second"/"third"/"fourth"/"eighth" yes, "fifteenth"/"fortieth" NO - use digits or add a
cardinal like "forty"); render 五六万 "fifty or sixty thousand" (60000) not "fifty
thousand-odd"; ten-odd/ten-or-so for 十几X/十来X (note 十几个 loses its 十 to the built-in
几个 strip: render "ten-odd" so the digit survives); use DIGITS for hanzi ordinals the
word-list lacks (十五号 -> "the 15th") and for any compound the checker cannot sum
(二百五十 -> "250"; 五十二万 -> a noise line as B17 did); a bare 两 after a price is the tael.
NOTE: the built-in 十[分] strip eats the 十分 out of a "X十分" clock reading and out of
十分钟 ("ten minutes"); if a clock loses its tens, render it with digits and add a
targeted residue rule (B09 did (?<=点)四, B15 did (?<=点)二). A month name carries a
numeral: 七月 is "July" (no digit).

Add translator footnotes to notes.json under each unit id at about chapter density
(~3-6 per chapter; the short Afterword may take 0-2). Anchors must be verbatim substrings
of the English prose - verify by grep before building; XHTML bodies use NUMERIC character
references for punctuation and dashes, never named entities; literal Chinese is fine.
ch17's translator notes were builder-numbered 95-100, so B18's continue from 101. There
is only ONE note stream now (translator, in notes.json, builder-numbered 1..N in reading
order); source_notes.json is frozen.
Add every new proper noun / place / firm / term to glossary.json with one rendering per
referent and a status. Reuse the names and vocabulary already fixed in glossary.json (the
whole industrialist / comprador / bond-market / strike cast is there, and B17 added
Napoleon, Cao Cao, the China Tobacco Company, Gaoqiao, the Woosung mouth, the Bronze-Man
Wharf, the Jade Buddha Temple, Zhenjiang and Yangzhou, Number Ninety-Four). Check
glossary.json before you romanize. NOTE for glossary NOTE bodies: use plain Unicode
punctuation, NOT numeric refs, because the builder esc()s glossary notes. notes.json note
bodies, by contrast, are inserted RAW - use numeric char refs there. And WRITE
glossary/notes JSON via a Python file, then RE-READ to verify the Chinese (a shell heredoc
mangled 钱庄 in B08; B10/B15 caught glyph slips only by re-reading).

Rebuild with build_reading_epub.py out/Midnight.epub (the TOC becomes fully translated:
all twenty units link their content). Because this is the LAST batch, ALSO: render any
back matter the book has (a colophon from back_matter.json if present; the translator's
note is already wired from book.json's translator_note), and do a WHOLE-BOOK QA pass -
run qa_epub.py out/Midnight.epub until green across the whole spine, and validate with
epubcheck (java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/Midnight.epub), which must
report 0 errors / 0 warnings. Then, instead of another handoff, write a COMPLETION REPORT
(whole-book: units, total notes, glossary size, check results, observed error rate from
the random-sample deep audit). Commit on claude/midnight. Cite chapters, never page
numbers. Never invent bridging text. Do not pause for approval mid-batch. Deliver
out/Midnight.epub in chat as an attached file.
```

## What is DONE (do not redo)

- Step 0 (ingest + survey) complete and approved. 20 units (ch01..ch19 numbered
  chapters + ch20 afterword); OPF metadata and cover set; skeleton EPUB, qa green.
- Approved batch plan (21,000-char maximum) in book.json "batches": B01..B17 one
  chapter each (ch01..ch17), B18 = ch18 + ch19 + Afterword.
- B01..B16: done (Chapters One through Sixteen). Translator notes 1-94; all nine
  author source notes [1]..[9] placed and frozen. See earlier PROGRESS.md entries.
- B17 = Chapter Seventeen (ch17): done. out/ch17_reading.md; 215 paragraphs; NO source
  notes. Translator notes 95-100 (天字第一号 "the very best under heaven"; 王母娘娘 the
  Queen Mother of the West; 上有天堂下有苏杭; 说曹操曹操到 / Cao Cao; 拜皇忏 the Imperial
  Litany; 三山五岳 the Three Mountains and the Five Peaks). Added glossary rows: Napoleon,
  Cao Cao; the China Tobacco Company; Gaoqiao, the Woosung mouth, the Bronze-Man Wharf,
  the Jade Buddha Temple, Zhenjiang and Yangzhou, Number Ninety-Four. Added three noise
  lines (牌九; 二百五十万; 五十二万). qa green, 100 notes, check_numbers 0 unresolved, parity
  215/215, epubcheck 0/0.

## What is NEXT

- Batch B18 = the FINAL batch: Chapter Eighteen (ch18, 12,247 chars, src
  data/src/21_part0019.txt), Chapter Nineteen (ch19, 5,137 chars, src
  data/src/22_part0020.txt), and the Afterword (ch20, 452 chars, src
  data/src/23_part0021.txt). NO source notes in any of them. Translator notes continue
  from 101. This batch CLOSES THE BOOK: do back matter + whole-book QA + a completion
  report instead of another handoff. See the kickoff above.

## The source's own notes are COMPLETE (for planning)

The nine author endnotes (exact wording in data/src/24_part0022.txt) are all placed:
[1][2] ch01; [3] ch02; [4] ch05; [5][6][7] ch06; [8][9] ch11. source_notes.json is
FROZEN. All OTHER chapters carry none. There is only ONE note stream now: the
translator footnotes in notes.json.

## State / traps

- Deliverable filename: out/Midnight.epub. The builder and qa default to
  out/book.epub; always pass out/Midnight.epub explicitly.
- APPLE BOOKS / epubcheck: the EPUB must validate clean. epubcheck 5.1.0 lives at
  /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetched from the w3c/epubcheck GitHub
  release if a fresh container lacks it - B17 re-fetched it cleanly). Run it after every
  build; it must be 0 errors / 0 warnings. Keep the book.json "uid" a valid, stable
  urn:uuid (already fixed); do NOT reintroduce a non-hexadecimal urn:uuid:.
- Only one note stream remains: translator footnotes (notes.json, numbered 1..N by
  the builder in reading order; ch17 got 95-100, so B18's continue from 101).
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
  are esc()d (build_reading_epub.py line ~423), so use plain Unicode punctuation.
  WRITE all of them via a Python file and RE-READ to verify the Chinese glyphs.
  check_numbers flags only MISSING source numbers; extra English numbers are harmless.
- The BIG number trap (B12): a bare 十万/二十万/三十万 is 100,000 / 200,000 / 300,000,
  NOT ten/twenty/thirty thousand. Render X万 as (X hundred thousand) when X < 10.
  When check_numbers reports a genuinely missing quantity, fix the translation, do
  not add noise.
- The checker cannot sum compound hundreds / hundred-thousands / teen-thousands in
  spelled English, SUMS an adjacent compound (三千五千 -> 8000; 二千五六百 -> 2600),
  reads a hanzi numeral in a name/place as a count (四川, 大三元, 阿三, 三马路, 瘪三,
  四喜子, 小三子, 黎八, 屠夜壶, 二百五 slang, 牌九), reads a X成/X折/十分之X as a bare
  digit, reads 零 in 凋零 as zero, needs a SPACE in "five hundred"/"one million" and the
  article in "a hundred", and its word-list has limited ordinals ("second/third/
  fourth/eighth/tenth/sixteenth/seventeenth/thirtieth" yes; "fifteenth"/"fortieth" NO
  - use digits, or add a bare cardinal like "forty"). A bare "couple"/"pair" does NOT
  satisfy a 两; render "two" (but "twice"/"both" DO). A month name ("July" for 七月)
  carries no digit. The built-in 几个 strip can orphan the 十 of 十几个 (residue 10):
  render "ten-odd". The built-in 十分 strip eats 十分钟 -> render "ten minutes" freely
  (10 is extra/harmless). Watch 四小姐/四妹: EVERY paragraph naming her needs "Fourth"
  or the 四 reads as a dropped 4 (B17 audited this paragraph by paragraph).
  NOISE ORDER IS LOAD-BEARING: a longer token must be stripped before a shorter rule
  that is a prefix of it, and a residual-adjacency pass must come AFTER the rule that
  creates the residue.
- When building the bilingual, write the English to a scratch file one paragraph
  per line and zip it against the source body with a Python script; keep the scratch
  files out of git (use the scratchpad dir).
- Branch hygiene: one branch only, claude/midnight. Each batch tends to start on a
  stray claude/midnight-b<nn>-* branch; the up-to-date work lives on
  origin/claude/midnight. Fast-forward local claude/midnight to it, do the batch
  there, push claude/midnight, and delete the stray (local + remote/tracking ref).
  Do not spin off new branches. B17 started on claude/midnight-b17-ch17-kbofkp and was
  moved onto claude/midnight; that stray was never pushed, so nothing to delete remotely.
