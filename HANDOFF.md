# HANDOFF — The Longest Day in Chang'an (长安十二时辰), Ma Boyong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 done and approved. Batches 1-4 (ch01-ch04) COMPLETE: translated,
checked, footnoted, built, QA green, committed. Next is Batch 5 (ch05). 21
chapters plus 2 afterwords remain, one chapter per batch (B25 = the two afterwords
together).

## Message to paste into the next chat

```
Read CLAUDE.md in full (the commissioner's rules at the top are non-negotiable),
then HANDOFF.md, then book.json. We are translating 长安十二时辰 (The Longest Day
in Chang'an) by Ma Boyong into an annotated English EPUB; the deliverable is
out/The Longest Day in Chang'an.epub. Step 0 and Batches 1-4 (ch01-ch04) are
done; the 25-batch plan (one chapter per batch) is approved.

Do Batch 5 = ch05 (第五章 未正 / "Chapter Five. The Hour of the Goat, Second Half
(2 p.m.)") end to end. NOTE: data/src/ and data/figs/ are gitignored and rebuild
from source.epub; if data/src/ is absent in a fresh clone, run
`python3 scripts/ingest_epub.py source.epub` first. Read the batch's source from
its text_file in book.json (data/src/10_text00011.txt); the source is
authoritative, quote it verbatim in the bilingual QC file and render it
faithfully and in full. Author one aligned bilingual QC file out/ch05_bilingual.md
(source '>' blockquote line, English paragraph beneath; the chapter title tagged
'## H2 <English title>'; each chapter's opening differs — render whatever the
source has, whether a flash-forward vignette, a scene-setting description, or the
dateline direct; render the source's per-chapter time-gloss final line as the
source's own italic note, prefixed '*[The source appends a note on the hour to
each chapter:]*'). Then generate out/ch05_reading.md and the parity source with
`scripts/split_bilingual.py out/ch05_bilingual.md ch05 "第五章　未正"` (use the exact
full-width-space zh title from book.json). Run
`scripts/check_numbers.py out/ch05_bilingual.md --noise noise.txt` (extend
noise.txt when a NON-quantity numeral is flagged, and record what you add and why;
a real dropped number must still fail) and
`scripts/check_structure.py --pairs data/zh/ch05.txt out/ch05_reading.md` (parity
must be equal). Reuse EVERY decided rendering already in glossary.json (do not
re-romanize a referent that is already decided; add rows only for new referents,
one rendering each, decided before you romanize). Add footnotes to notes.json
under key "ch05" (verbatim English anchors; XHTML bodies with numeric character
references, never named entities; ~3 per chapter, recurring subjects get their
note at first appearance across the whole book, so skip anything already noted in
ch01-ch04). Add any figure specs to figures.json only if the chapter has a real
content illustration in data/figs/ (the source's footnote-marker glyph
Image00004.jpg and the decorative scene-break rule Image00005.jpg are NOT figures).
Rebuild with `scripts/build_reading_epub.py "out/The Longest Day in Chang'an.epub"`
so the pending-aware TOC links ch01-ch05 content and every other chapter's
skeleton, then run `scripts/qa_epub.py "out/The Longest Day in Chang'an.epub"`
until green. Do a blind double-translation of a literary sample and a round-trip
back-translation of a number-dense sample (separate contexts), and record the
checks and the sample error rate in PROGRESS.md. Rewrite HANDOFF.md with the
Batch 6 (= ch06) kickoff message, commit, and push to branch
claude/the-longest-day-in-changan. Cite chapters/sections, never page numbers.
Never invent bridging text; footnote genuine ambiguity rather than smoothing it.
Do not pause for approval mid-batch. Deliver the rebuilt EPUB in chat as an
attached file.
```

## What is DONE (do not redo)

- Step 0 ingest + survey + skeleton EPUB, approved. 25-batch plan approved.
- Batch 1 = ch01, complete and committed: out/ch01_reading.md, data/zh/ch01.txt,
  12 notes in notes.json, glossary.json seeded, EPUB rebuilt, qa_epub PASS.
- Batch 2 = ch02, complete and committed: out/ch02_reading.md, data/zh/ch02.txt,
  3 notes (15 total), glossary.json updated, EPUB metadata formatted for
  Kindle/Apple Books, qa_epub PASS.
- Batch 3 = ch03, complete and committed: out/ch03_reading.md, data/zh/ch03.txt,
  4 notes (19 total), glossary.json updated, noise.txt extended, qa_epub PASS.
- Batch 4 = ch04, complete and committed: out/ch04_reading.md, data/zh/ch04.txt,
  3 notes (22 total), glossary.json updated (44 people / 9 orgs / 46 places / 50
  terms), noise.txt extended (四季/四溅/四合/四望/零星/千金), EPUB rebuilt, qa_epub
  PASS. Blind double-translation (ferry-dilemma exchange) and back-translation
  (sand-table fire-simulation + Nine-Gate Drum) samples both clean, zero errors.
- noise.txt authored for check_numbers (project names/idioms/round numbers); its
  loader does NOT strip trailing comments, so keep every note on its own line.
  External noise patterns fire BEFORE built-in patterns in check_numbers.py.
  The general approximate-"-odd" rule [一二三四五六七八九]十[多几余] lives at the TOP
  of noise.txt on purpose (it must run before the 十几/十多 rules or those orphan
  the leading digit of 八十多/二十几/等).
- check_numbers.py WORD_NUM extended with teen ordinals (thirteenth..sixteenth,
  seventeenth) and "twentieth" (20). No WORD_NUM change was needed for ch04.
- 县尉 rendered "county commandant" (NOT "county magistrate"); decided, in glossary.

## What is NEXT

- Batch 5 = ch05 (第五章 未正, ~13,336 source chars, data/src/10_text00011.txt).
  Then B06=ch06 ... B24=ch24, B25=ch25+ch26. See book.json's structure/batches.

## House style set by Batches 1-4 (follow it)

- Register: novelistic thriller prose in the book's own voice; all apparatus in
  notes, none inline. Merge sentences where English wants them merged.
- Openings: NOT every chapter has an epigraph. Each chapter's opening differs
  (flash-forward vignette, a scene-setting description, or the dateline direct;
  ch04 opened with a lyrical Qujiang Pool epigraph). Translate whatever the source
  has. The source's per-chapter time-gloss (its own Duokan footnote on the
  dateline, e.g. "下午1点。未，又名…") is rendered as the SOURCE's own note, in
  italics, prefixed "*[The source appends a note on the hour to each chapter:]*",
  distinct from translator's notes.
- Names: pinyin, one decided rendering per referent, all in glossary.json. Grep
  the glossary before romanizing anything new. Recurring items already decided
  across ch01-ch04 that MUST be reused verbatim include: Zhang Xiaojing, Li Bi
  (Changyuan), Director He / He Zhizhang, Yao Runeng, Cui Qi, Cao Poyan, Xu Bin,
  Tanqi, Wen Ran, the Right Shad, Li Heng (the Crown Prince), Li Linfu (the Right
  Minister), Long Bo, Old Ge, the Great Sabao, Tong'er, Wang Yunxiu, Ma Ge'er,
  Xiao Yi, Wang Zhongsi (the military commissioner); the Jing'an Bureau, the Lüben
  Guards, the Jinwu Guard, the Sabao Office, the Directorate for the Palace
  Buildings, the Xuanhui Court; Chang'an, Wannian/Chang'an County, the Vermilion
  Bird Avenue, the West Market, Xiuzheng/Jingshan/Guangde Wards, the Pingkang
  Quarter, Qujiang Pool, the Furong Garden, the Shaoling Plain, the Qixia/Yanxing
  Gates; shichen ("double-hour"), watchtower, constable, buliang chief/men, Wolf
  Guards, Türk, the Sage, His Majesty, Your Highness, the Lantern Festival,
  Tianbao/Kaiyuan, barrier-knife, pocket crossbow, smoke pellet, Que-le Huo-duo,
  the art of the Great Archive, the Nine-Gate Drum, the Five Kennels, the Bear
  Fire Gang, the Zhuxin Pavilion, "casting flesh-coins," Kunlun/Zanj slave, Mazda.
- Titles/address: 太子/东宫 = "heir apparent" / "the Eastern Palace"; 司丞 (Li Bi)
  = "Deputy Director"; 令/贺监 (He) = "Director" / "Director He"; 都尉 (Zhang) =
  "Commander"; 旅帅 (Cui) = "Commander" (崔旅帅 = "Commander Cui"); 节度 (Wang) =
  "military commissioner" (王节度 = "the military commissioner Wang"); 殿下 = "Your
  Highness"; 陛下 = "His Majesty"; 圣人 = "the Sage"; 那一位 / 宫里那位 = "that one
  person" (the Crown Prince, kept ambiguous).
- Numbers: run check_numbers with --noise noise.txt every batch. When it flags a
  non-quantity numeral (a name, an idiom, a round number spelled out analytically
  in English, an "all-directions" 四X idiom), extend noise.txt (own-line comments)
  or WORD_NUM, and say so in PROGRESS. A genuinely dropped number must still fail.
- 二楼/二层 ("the second floor / a two-story ...") is rendered with an English
  number-word ("second"/"two-story") so its numeral survives the number check; do
  NOT render it as a bare "upstairs" unless the pair carries the 2 elsewhere.

## State / traps

- Working branch is claude/the-longest-day-in-changan; push only there. Do not
  spin off new branches. (A harness note may name a different per-batch branch;
  CLAUDE.md rule 2 and the commissioner override it. Batch 4 was started on a
  stray branch "claude/batch-4-chapter-four-…"; all work was moved onto
  claude/the-longest-day-in-changan and the stray branch deleted, local + remote.)
- data/src/ and data/figs/ are gitignored; regenerate with ingest_epub.py.
- The bilingual QC file never ships. Note anchors must be verbatim English
  substrings or the build refuses. XHTML note bodies use numeric character
  references, never named entities. The builder inserts note anchors BEFORE
  markup substitution.
- Extractor artifacts: a logical paragraph is sometimes split across two lines in
  data/src (no sentence-ending punctuation on the first). Merge such halves into
  one bilingual pair (ch03 merged source lines 40+41; ch04 merged the epigraph's
  three lines and the dateline's split full-stop). Colon-lead-in speech lines can
  be kept as separate paragraphs. Parity is self-consistent either way (both
  reading and data/zh are derived from the bilingual), so keep each `>` paired
  with exactly one English paragraph.
- Cite by chapter, never by page.
- The source text sometimes uses 中元 ("Ghost Festival") where it means 上元
  ("Lantern Festival"); when encountered, translate the intent, not the literal
  wrong festival name.
- Watch for authorial slips (ch03 had 祆正-for-Sabao and a Tianbao-3-vs-"twenty
  years" tutor date; ch04 wrote 麻格心 once for 麻格儿). Render faithfully, leave
  visible, and flag in PROGRESS rather than silently correcting.
- A footnote's subject gets its note at its FIRST appearance in the whole book.
  Before adding a note, grep the built ch01..ch(n-1) reading files: e.g. Qujiang
  Pool and Wang Zhongsi first appear in ch01, so ch04 did NOT footnote them even
  though the chapter turns on them (their glossary rows may still be added later).
