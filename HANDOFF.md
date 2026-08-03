# HANDOFF — Midnight (子夜), Mao Dun

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Midnight B17

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Work only on branch claude/midnight. Build the
deliverable as out/Midnight.epub (the builder defaults to out/book.epub, so pass
the path explicitly on every build and every qa run).

data/src/ is regenerable and git-ignored, so if it is missing run
scripts/ingest_epub.py source.epub first to recreate it (Chapters One through
Sixteen are already translated; do not redo them).

Do Batch B17 = Chapter Seventeen (unit ch17) end to end. Read the source from
data/src/20_part0018.txt; it is authoritative. Quote it verbatim in the bilingual
QC file and render it faithfully and in full into English in the book's own
novelistic register. Chapter Seventeen is 13,863 source chars.

NO source notes remain anywhere. The author's own endnote stream [1]..[9] is
COMPLETE and fully placed (ch01 [1][2], ch02 [3], ch05 [4], ch06 [5][6][7], ch11
[8][9]). So source_notes.json is FROZEN: do not add to it. Everything you add this
batch is a TRANSLATOR footnote (notes.json) only. Still, grep the source for
\[\d+\] at the start as a habit, and if one ever appears, stop and reconcile against
book.json before proceeding.

Author out/ch17_bilingual.md (a "## H2 Chapter Seventeen" line, then per source
paragraph a "> <verbatim source>" line and the English beneath). The safe way to
get verbatim source and exact paragraph parity is to write the English one
paragraph per line into a scratch file (use the scratchpad dir, keep it out of git)
and zip it against the source body lines with a short script (read
data/src/20_part0018.txt, drop line 1 = the title 十七; the rest are the body
paragraphs; the file may lack a trailing newline, so filter blank lines and count
non-empty lines; assert the English line count equals the body line count BEFORE
zipping, then write the bilingual). Every batch's pre-zip assertion has caught a
would-be dropped paragraph, so keep that guard and spot-check alignment at several
paragraph indices before writing. Then run:
  python3 scripts/split_bilingual.py out/ch17_bilingual.md ch17 "十七"
  python3 scripts/check_numbers.py out/ch17_bilingual.md --noise data/noise_zh.txt
  python3 scripts/check_structure.py --pairs data/zh/ch17.txt out/ch17_reading.md
check_numbers only flags MISSING source numbers (extra English numbers are fine). When
it flags a non-quantity numeral (idiom, slang, a name/place with a digit, a shape-word
like 十字, an approximate range, a compound it cannot sum, an intensifier, an ordinal
the word-list lacks), add a regex for it to data/noise_zh.txt with a one-line reason;
do not silence a real dropped number. When it flags a number that IS faithfully present,
reword to a form the checker parses OR add a documented noise line; when it flags a
genuinely missing number, FIX THE TRANSLATION (B12 caught 二十万 mis-rendered as
"twenty thousand" - it is 200,000, "two hundred thousand"). The noise file already
carries a generous ch01..ch16 block, so many recurring items are handled, including
the strike-chapter set (七搭八搭, 不三不四, 四喜子, 小三子, 三先生, 阿三, 三马, 十字,
大三元, 两脚朝天, 三对六面, 四边, 胡说八道, 凋零, 二百五(?!十), the tael rules, the
bare-百 / bare-万 rules, the clock residue (?<=点)四, and 四平八稳).

Number-rendering habits that keep the checker clean: render 十万 as "one hundred
thousand" and 二十万 as "two hundred thousand" (a bare 十万/二十万 is 100,000 /
200,000, NOT ten/twenty thousand - the exact trap B12 hit); render 三十万 as "three
hundred thousand", 八十万 as "eight hundred thousand", 四十多万 as "four hundred
thousand and more"; write "a hundred/a thousand" WITH the article and "five hundred"/
"one million" WITH A SPACE (no hyphen); render X成 (a tenth) and X折 (a discount) in
WORDS as "X-tenths" so the digit survives (八折 -> "eight-tenths", 九折 -> "nine-tenths");
render 十分之五 as "five-tenths" and 千分之十 as "ten parts in a thousand"; do NOT write
"eighty per cent", which loses the 8; render two/pair as "the two of them" so 2 stays
visible (a bare "couple"/"pair" does NOT satisfy the checker - use "two"; note
"twice"/"both" DO satisfy a 两); render a birth-order nickname so its digit survives
(周二姐 -> "Second Sister Zhou", 老八 -> "Old Eight", 黎八 -> "Li the Eighth",
六叔 -> "Sixth Uncle", 曾老二 -> "Zeng the Second", 吴老三 -> "Wu the Third"); an ordinal
survives as a word if the word-list has it ("second"/"third"/"fourth"/"eighth" yes,
"fifteenth"/"fortieth" NO - use digits or add a cardinal like "forty"); render 五六万
"fifty or sixty thousand" (60000) not "fifty thousand-odd"; ten-odd/ten-or-so for
十几X/十来X (and note 十几个 loses its 十 to the built-in 几个 strip: render "ten-odd" so
the digit survives, as B15 did); render 角 wages "six jiao" (a jiao = a tenth of a
yuan); render 七八万 "seventy or eighty thousand"; use DIGITS for hanzi ordinals the
word-list lacks (十五号 -> "the 15th") and for any compound the checker cannot sum
(二百五十 -> "250"; 一百零二 -> "102"; note 二百五 colloquial "250" is now noised); a bare
两 after a price is the tael. NOTE: the built-in 十[分] strip eats the 十分 out of a
"X十分" clock reading; if a clock loses its tens, render it with digits and add a
targeted residue rule (B09 did (?<=点)四, B15 did (?<=点)二 for 七点二十分). A month name
carries a numeral: 七月 is "July" (no digit), so if the checker flags the 七 of a bare
七月, add a noise line.

Add translator footnotes to notes.json under "ch17" at about chapter density (~3-6;
anchors must be verbatim substrings of the English prose - verify by grep before
building; XHTML bodies use NUMERIC character references for punctuation and dashes,
never named entities; literal Chinese is fine). ch16's translator notes were
builder-numbered 89-94, so ch17's continue from 95. There is only ONE note stream
now (translator, in notes.json, builder-numbered 1..N in reading order);
source_notes.json is frozen.
Add every new proper noun / place / firm / term to glossary.json with one rendering
per referent and a status. Reuse the names and vocabulary already fixed in
glossary.json (the industrialist/comprador/bond-market cast is all there now: Wu Sunfu
= Wu the Third, Zhao Botao, Du Zhuzhai, Wang Hefu, Sun Jiren, Zhu Yinqiu, Chen Junyi,
Zhou Zhongwei = the Red-Headed Match, Tu Weiyue = Tu the Chamber-pot, Han Mengxiang,
Li Yuting, Xu Manli, Staff Officer Lei Ming, Shang Zhongli, Feng Yunqing, Feng
Meiqing, He Shen'an, Liu Yuying, Lu Kuangshi, plus the Yizhong Company, the Chinese
Securities Exchange, the Daya Securities Trust Company, the silk filatures and the
strike cast). Check glossary.json before you romanize. NOTE for glossary NOTE bodies:
use plain Unicode punctuation, NOT numeric refs, because the builder esc()s glossary
notes. notes.json note bodies, by contrast, are inserted RAW - use numeric char refs
there. And WRITE glossary/notes JSON via a Python file, then RE-READ to verify the
Chinese (a shell heredoc mangled 钱庄 in B08, B10 caught a 亨->享 slip only by
re-reading, B15 caught a 流寇->流嬇 slip only by re-reading).

Rebuild with build_reading_epub.py out/Midnight.epub (the TOC stays pending-aware:
Chapters One through Seventeen link their content, every other unit still links its
skeleton outline), run qa_epub.py out/Midnight.epub until green, and ALSO validate
with epubcheck (java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/Midnight.epub) which
must report 0 errors / 0 warnings (see State / traps: the Apple Books fix). Commit on
claude/midnight, and rewrite HANDOFF.md with the B18 kickoff. Cite chapters, never
page numbers. Never invent bridging text. Do not pause for approval mid-batch.
Deliver out/Midnight.epub in chat as an attached file.
```

## What is DONE (do not redo)

- Step 0 (ingest + survey) complete and approved. 20 units (ch01..ch19 numbered
  chapters + ch20 afterword); OPF metadata and cover set; skeleton EPUB, qa green.
- Approved batch plan (21,000-char maximum) in book.json "batches": B01..B17 one
  chapter each (ch01..ch17), B18 = ch18 + ch19 + Afterword.
- B01..B15: done (Chapters One through Fifteen). Translator notes 1-88; all nine
  author source notes [1]..[9] placed and frozen. See earlier PROGRESS.md entries.
- B16 = Chapter Sixteen (ch16): done. out/ch16_reading.md; 154 paragraphs; NO source
  notes. Translator notes 89-94 (A-Ying = the mother's pet name for Zhu Guiying, not
  the delegate A Ying; the Empty City Stratagem of Zhuge Liang; the Swedish Match
  Trust / Ivar Kreuger; 花旗/茄门 = Flowery-Flag man / German; 开门七件事 the seven
  necessities; 二百五 slang for a half-wit). Added glossary rows: Zhuge Liang, the
  Swedish Match Trust, the Sino-Swedish Match Company, the All-China Match
  Manufacturers' Association, the Guangdong Match Trade Guild, the Match Trade
  Federation of the Three Eastern Provinces, the Ministry of Industry and Commerce,
  the Hongyun Lou. Added two noise lines (凋零, 二百五(?!十)). qa green, 94 notes,
  check_numbers 0 unresolved, parity 154/154, epubcheck 0/0.

## What is NEXT

- Batch B17 = Chapter Seventeen (ch17), 13,863 source chars, src
  data/src/20_part0018.txt, NO source notes. Translator notes continue from 95.
  See the kickoff above.

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
  release if a fresh container lacks it). Run it after every build; it must be 0
  errors / 0 warnings. The one historical defect was book.json "uid" being an invalid
  urn:uuid: (now fixed and valid); keep the uid a valid UUID and stable across builds
  so Apple treats each rebuild as the same book. Do NOT reintroduce a non-hexadecimal
  urn:uuid:.
- Only one note stream remains: translator footnotes (notes.json, numbered 1..N by
  the builder in reading order; ch16 got 89-94, so ch17's continue from 95).
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
  四喜子, 小三子, 黎八, 屠夜壶, 二百五 slang), reads a X成/X折/十分之X as a bare digit,
  reads 零 in 凋零 as zero, needs a SPACE in "five hundred"/"one million" and the
  article in "a hundred", and its word-list has limited ordinals ("second/third/
  fourth/eighth/tenth/sixteenth/seventeenth/thirtieth" yes; "fifteenth"/"fortieth" NO
  - use digits, or add a bare cardinal like "forty"). A bare "couple"/"pair" does NOT
  satisfy a 两; render "two" (but "twice"/"both" DO). A month name ("July" for 七月)
  carries no digit; watch the 七/etc if the checker flags it. The built-in 几个 strip
  can orphan the 十 of 十几个 (residue 10): render "ten-odd" so the digit survives.
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
  Do not spin off new branches.
