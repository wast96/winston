# HANDOFF — The Longest Day in Chang'an (长安十二时辰), Ma Boyong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 done and approved. Batches 1-5 (ch01-ch05) COMPLETE: translated,
checked, footnoted, built, QA green, committed. Next is Batch 6 (ch06). 20
chapters plus 2 afterwords remain, one chapter per batch (B25 = the two afterwords
together).

Chat naming: each batch runs in its own chat named `Chang'an B<n>` (this batch was
`Chang'an B5`; the next is `Chang'an B6`). CLAUDE.md records the rule; the kickoff
block below opens with that name as its first line on purpose. Keep it there.

## Message to paste into the next chat

```
Chang'an B6
Read CLAUDE.md in full (the commissioner's rules at the top are non-negotiable),
then HANDOFF.md, then book.json. We are translating 长安十二时辰 (The Longest Day
in Chang'an) by Ma Boyong into an annotated English EPUB; the deliverable is
out/The Longest Day in Chang'an.epub. Step 0 and Batches 1-5 (ch01-ch05) are
done; the 25-batch plan (one chapter per batch) is approved.

Do Batch 6 = ch06 (第六章 申初 / "Chapter Six. The Hour of the Monkey, First Half
(3 p.m.)") end to end. It is the longest chapter so far (~25,297 source chars),
so budget accordingly. NOTE: data/src/ and data/figs/ are gitignored and rebuild
from source.epub; if data/src/ is absent in a fresh clone, run
`python3 scripts/ingest_epub.py source.epub` first. Read the batch's source from
its text_file in book.json (data/src/13_text00013.txt); the source is
authoritative, quote it verbatim in the bilingual QC file and render it
faithfully and in full. Author one aligned bilingual QC file out/ch06_bilingual.md
(source '>' blockquote line, English paragraph beneath; the chapter title tagged
'## H2 <English title>'; each chapter's opening differs — render whatever the
source has, whether a flash-forward vignette, a scene-setting description, or the
dateline direct; the source's content-file time-marker heading line is absorbed
into the H2 title, as in ch01-ch05; render the source's per-chapter time-gloss
final line as the source's own italic note, prefixed '*[The source appends a note
on the hour to each chapter:]*'). Then generate out/ch06_reading.md and the parity
source with `scripts/split_bilingual.py out/ch06_bilingual.md ch06 "第六章　申初"`
(use the exact full-width-space zh title from book.json). Run
`scripts/check_numbers.py out/ch06_bilingual.md --noise noise.txt` (extend
noise.txt when a NON-quantity numeral is flagged, and record what you add and why;
a real dropped number must still fail) and
`scripts/check_structure.py --pairs data/zh/ch06.txt out/ch06_reading.md` (parity
must be equal). Reuse EVERY decided rendering already in glossary.json (do not
re-romanize a referent that is already decided; add rows only for new referents,
one rendering each, decided before you romanize). Add footnotes to notes.json
under key "ch06" (verbatim English anchors; XHTML bodies with numeric character
references, never named entities; ~3 per chapter, recurring subjects get their
note at first appearance across the whole book, so skip anything already noted in
ch01-ch05). Add any figure specs to figures.json only if the chapter has a real
content illustration in data/figs/ (the source's footnote-marker glyph
Image00004.jpg and the decorative scene-break rule Image00005.jpg are NOT figures).
Rebuild with `scripts/build_reading_epub.py "out/The Longest Day in Chang'an.epub"`
so the pending-aware TOC links ch01-ch06 content and every other chapter's
skeleton, then run `scripts/qa_epub.py "out/The Longest Day in Chang'an.epub"`
until green. Do a blind double-translation of a literary sample and a round-trip
back-translation of a number-dense sample (separate contexts), and record the
checks and the sample error rate in PROGRESS.md. Rewrite HANDOFF.md with the
Batch 7 (= ch07) kickoff message (its fenced block opening with the line
`Chang'an B7`), commit, and push to branch claude/the-longest-day-in-changan.
Cite chapters/sections, never page numbers. Never invent bridging text; footnote
genuine ambiguity rather than smoothing it. Do not pause for approval mid-batch.
Deliver the rebuilt EPUB in chat as an attached file.
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
  3 notes (22 total), glossary.json updated, noise.txt extended (四季/四溅/四合/
  四望/零星/千金), qa_epub PASS. Blind double-translation and back-translation
  samples clean.
- Batch 5 = ch05, complete and committed: out/ch05_reading.md, data/zh/ch05.txt,
  3 notes (25 total), glossary.json updated (51 people / 15 orgs / 60 places / 57
  terms — big place/office batch: the southwest wards, Daming/Xingqing Palaces,
  Onon/Orkhon rivers, and the Works/Justice/Review/Censorate/Domestic-Service
  offices), noise.txt extended (万千/独一无二/王八/六亲/一了百了), EPUB rebuilt,
  qa_epub PASS (25 notes). Blind double-translation (Cao Poyan's necklace + the
  gazelle image) and back-translation (bamboo-pole depot + Wang Zhongsi's three
  titles + polo-field dimensions) samples both clean, 0 errors.

## What is NEXT

- Batch 6 = ch06 (第六章 申初, ~25,297 source chars, data/src/13_text00013.txt) —
  the LONGEST chapter to date. Then B07=ch07 ... B24=ch24, B25=ch25+ch26. See
  book.json's structure/batches.

## House style set by Batches 1-5 (follow it)

- Register: novelistic thriller prose in the book's own voice; all apparatus in
  notes, none inline. Merge sentences where English wants them merged.
- Openings: NOT every chapter has an epigraph. Each chapter's opening differs
  (flash-forward vignette, a scene-setting description, or the dateline direct;
  ch04 opened with a lyrical Qujiang Pool epigraph, ch05 with a flash-forward
  vignette of the boxwood writing-case that recurs verbatim later in the chapter).
  Translate whatever the source has, and translate a recurring vignette
  identically in both places. The content-file time-marker heading line (e.g.
  未正) is absorbed into the H2 chapter title, not made a paragraph. The source's
  per-chapter time-gloss (its own Duokan footnote on the dateline, e.g.
  "下午2点。未，又名…") is rendered as the SOURCE's own note, in italics, prefixed
  "*[The source appends a note on the hour to each chapter:]*", distinct from
  translator's notes.
- Names: pinyin, one decided rendering per referent, all in glossary.json. Grep
  the glossary before romanizing anything new. Recurring items already decided
  across ch01-ch05 that MUST be reused verbatim include: Zhang Xiaojing, Li Bi
  (Changyuan), Director He / He Zhizhang, Yao Runeng, Cui Qi, Cao Poyan, Xu Bin,
  Tanqi, Wen Ran, the Right Shad, Li Heng (the heir apparent), Li Linfu (the Right
  Minister), Long Bo, Old Ge, the Great Sabao, Tong'er, Wang Yunxiu, Ma Ge'er,
  Xiao Yi, Wang Zhongsi (the military commissioner), Feng Dalun, Prince Yong /
  Li Lin, Yuan Zai, Yang Shenjiao, Princess Changning; the Jing'an Bureau, the
  Lüben Guards, the Jinwu Guard, the Sabao Office, the Directorate for the Palace
  Buildings, the Xuanhui Court, the Dog Kennel, the Ministry of Works, the
  Forestry and Crafts Bureau (虞部), the Court of Judicial Review, the Censorate,
  the Ministry of Justice, the Palace Domestic Service; Chang'an, Wannian/Chang'an
  County, the Vermilion Bird Avenue, the West Market, Xiuzheng/Jingshan/Guangde/
  Daning/Jinggong/Tongji/Guangxing/Anle Wards, the Pingkang Quarter, Qujiang Pool,
  the Furong Garden, the Shaoling Plain, the Qixia/Yanxing Gates, the Daming/
  Xingqing Palaces, the Onon/Orkhon rivers; shichen ("double-hour"), watchtower,
  constable, buliang chief/men, county commandant (县尉), Wolf Guards, Türk, the
  Sage, His Majesty, Your Highness, the Lantern Festival, Tianbao/Kaiyuan,
  barrier-knife, pocket crossbow, smoke pellet, Que-le Huo-duo, the art of the
  Great Archive, the Nine-Gate Drum, the Five Kennels, the Bear Fire Gang, the
  Zhuxin Pavilion, "casting flesh-coins," Kunlun/Zanj slave, Mazda, polo (击鞠),
  the Oil-Sprinkled Ground.
- Titles/address: 太子/东宫 = "heir apparent" / "the Eastern Palace"; 司丞 (Li Bi)
  = "Deputy Director"; 令/贺监 (He) = "Director" / "Director He"; 都尉 (Zhang) =
  "Commander"; 旅帅 (Cui) = "Commander" (崔旅帅 = "Commander Cui"); 节度 (Wang) =
  "military commissioner"; 殿下 = "Your Highness"; 陛下 = "His Majesty"; 圣人 =
  "the Sage"; 那一位 / 宫里那位 = "that one person" (the heir apparent, kept
  ambiguous). OFFICE-TITLE renderings: 主事 = "recorder" (Recorder Xu, Recorder
  Feng); 评事 = "Evaluator"; 工部/虞部/大理寺/御史台/刑部/内侍省 per Hucker (see
  glossary). 永王 = "Prince Yong"; 节级 = "warder".
- Numbers: run check_numbers with --noise noise.txt every batch. When it flags a
  non-quantity numeral (a name, an idiom, a round number spelled out analytically
  in English, an "all-directions" 四X idiom, a swear-word like 王八, a myriad-idiom
  like 万千), extend noise.txt (own-line comments) or WORD_NUM, and say so in
  PROGRESS. A genuinely dropped number must still fail.
- 二楼/二层 ("the second floor / a two-story ...") is rendered with an English
  number-word ("second"/"two-story") so its numeral survives the number check.
  For an approximate "ten-odd" (十余/十几) render "ten-odd" (keeps 10), not "a
  dozen or so" (loses it).

## State / traps

- Working branch is claude/the-longest-day-in-changan; push only there. Do not
  spin off new branches. (A harness note may name a different per-batch branch;
  CLAUDE.md rule 2 and the commissioner override it. Batches 4 and 5 were each
  started on a stray per-batch branch; all work was moved onto
  claude/the-longest-day-in-changan and the stray branch deleted, local + remote.)
- data/src/ and data/figs/ are gitignored; regenerate with ingest_epub.py.
- The bilingual QC file never ships (and is not committed). Note anchors must be
  verbatim English substrings or the build refuses. XHTML note bodies use numeric
  character references, never named entities. The builder inserts note anchors
  BEFORE markup substitution.
- Extractor artifacts: a logical paragraph is sometimes split across two lines in
  data/src (no sentence-ending punctuation on the first). Merge such halves into
  one bilingual pair (ch03 merged source lines 40+41; ch04 merged the epigraph's
  three lines; ch05 merged the three-line opening vignette). Colon-lead-in speech
  lines can be kept as separate paragraphs. Parity is self-consistent either way
  (both reading and data/zh are derived from the bilingual), so keep each `>`
  paired with exactly one English paragraph.
- Cite by chapter, never by page.
- The source text sometimes uses 中元 ("Ghost Festival") where it means 上元
  ("Lantern Festival"); when encountered, translate the intent, not the literal
  wrong festival name.
- Watch for authorial slips (ch03 had 祆正-for-Sabao and a Tianbao-3-vs-"twenty
  years" tutor date; ch04 wrote 麻格心 once for 麻格儿; ch05 line 10 has a doubled
  negative 并未没引起注意 = "drew no notice"). Render faithfully, leave visible,
  flag in PROGRESS rather than silently correcting.
- A footnote's subject gets its note at its FIRST appearance in the whole book.
  Before adding a note, grep the built ch01..ch(n-1) reading files: e.g. Wang
  Zhongsi and the Five Kennels first appear before ch05, so ch05 did NOT re-note
  them even though the chapter turns on Wang Zhongsi's daughter.
