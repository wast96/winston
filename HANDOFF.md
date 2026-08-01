# HANDOFF — The Longest Day in Chang'an (长安十二时辰), Ma Boyong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 done and approved. Batches 1-6 (ch01-ch06) COMPLETE: translated,
checked, footnoted, built, QA green, committed. Next is Batch 7 (ch07). 19
chapters plus 2 afterwords remain, one chapter per batch (B25 = the two afterwords
together).

Chat naming: each batch runs in its own chat named `Chang'an B<n>` (this batch was
`Chang'an B6`; the next is `Chang'an B7`). CLAUDE.md records the rule; the kickoff
block below opens with that name as its first line on purpose. Keep it there.

## Message to paste into the next chat

```
Chang'an B7
Read CLAUDE.md in full (the commissioner's rules at the top are non-negotiable),
then HANDOFF.md, then book.json. We are translating 长安十二时辰 (The Longest Day
in Chang'an) by Ma Boyong into an annotated English EPUB; the deliverable is
out/The Longest Day in Chang'an.epub. Step 0 and Batches 1-6 (ch01-ch06) are
done; the 25-batch plan (one chapter per batch) is approved.

Do Batch 7 = ch07 (第七章 申正 / "Chapter Seven. The Hour of the Monkey, Second
Half (4 p.m.)") end to end. It is ~25,671 source chars (a shade longer than ch06,
the current longest), so budget accordingly. NOTE: data/src/ and data/figs/ are
gitignored and rebuild from source.epub; if data/src/ is absent in a fresh clone,
run `python3 scripts/ingest_epub.py source.epub` first. Read the batch's source
from its text_file in book.json (data/src/15_text00015.txt); the source is
authoritative, quote it verbatim in the bilingual QC file and render it faithfully
and in full. Author one aligned bilingual QC file out/ch07_bilingual.md (source
'>' blockquote line, English paragraph beneath; the chapter title tagged
'## H2 <English title>'; each chapter's opening differs — render whatever the
source has, whether a flash-forward vignette, a scene-setting description, or the
dateline direct; the source's content-file time-marker heading line is absorbed
into the H2 title, as in ch01-ch06; render the source's per-chapter time-gloss
final line as the source's own italic note, prefixed '*[The source appends a note
on the hour to each chapter:]*'). Then generate out/ch07_reading.md and the parity
source with `scripts/split_bilingual.py out/ch07_bilingual.md ch07 "第七章　申正"`
(use the exact full-width-space zh title from book.json). Run
`scripts/check_numbers.py out/ch07_bilingual.md --noise noise.txt` (extend
noise.txt when a NON-quantity numeral is flagged, and record what you add and why;
a real dropped number must still fail — if it is a real quantity, fix the ENGLISH
to carry the value rather than noising it) and
`scripts/check_structure.py --pairs data/zh/ch07.txt out/ch07_reading.md` (parity
must be equal). Reuse EVERY decided rendering already in glossary.json (do not
re-romanize a referent that is already decided; add rows only for new referents,
one rendering each, decided before you romanize). Add footnotes to notes.json
under key "ch07" (verbatim English anchors; XHTML bodies with numeric character
references, never named entities; ~3 per chapter, recurring subjects get their
note at first appearance across the whole book, so skip anything already noted in
ch01-ch06). Add any figure specs to figures.json only if the chapter has a real
content illustration in data/figs/ (the source's footnote-marker glyph
Image00004.jpg and the decorative scene-break rule Image00005.jpg are NOT figures).
Rebuild with `scripts/build_reading_epub.py "out/The Longest Day in Chang'an.epub"`
so the pending-aware TOC links ch01-ch07 content and every other chapter's
skeleton, then run `scripts/qa_epub.py "out/The Longest Day in Chang'an.epub"`
until green. Do a blind double-translation of a literary sample and a round-trip
back-translation of a number-dense sample (separate contexts), and record the
checks and the sample error rate in PROGRESS.md. Rewrite HANDOFF.md with the
Batch 8 (= ch08) kickoff message (its fenced block opening with the line
`Chang'an B8`), commit, and push to branch claude/the-longest-day-in-changan.
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
  terms), noise.txt extended (万千/独一无二/王八/六亲/一了百了), qa_epub PASS.
  Blind double-translation and back-translation samples clean, 0 errors.
- Batch 6 = ch06, complete and committed: out/ch06_reading.md, data/zh/ch06.txt,
  3 notes (28 total), glossary.json updated (57 people / 18 orgs / 86 places / 69
  terms — big place batch: the Jinguang Gate, Changming Ward, the King of Rinan's
  mansion, the Wild Goose Pagoda, the many chase-route wards and canal-route wards,
  and the Right Xiao Guard / Leopard Cavalry / Sixteen Guards; terms rock-oil /
  fierce-fire / fierce-fire thunder / Yan ink / fire-proof cloth / dragon-sill /
  binding-cord / the Tang Rhymes / commissioning the watchtowers). noise.txt
  extended (二十六六/李十二/贾十七/二来/化整为零/两侧/两片/百炼/四溢/万幸); THREE
  flagged numerals were real quantities and were fixed in the ENGLISH instead
  (一百步 "a hundred paces", 十来个 "ten-odd", 三面 "on three sides"). qa_epub PASS
  (28 notes). Blind double-translation (Zhang's "living Chang'an" speech) and
  back-translation (kiln-math + gauge-gate + rhyme-code numbers) both clean, 0
  errors.

## What is NEXT

- Batch 7 = ch07 (第七章 申正, ~25,671 source chars, data/src/15_text00015.txt) —
  now the longest chapter. Then B08=ch08 ... B24=ch24, B25=ch25+ch26. See
  book.json's structure/batches.

## House style set by Batches 1-6 (follow it)

- Register: novelistic thriller prose in the book's own voice; all apparatus in
  notes, none inline. Merge sentences where English wants them merged.
- Openings: NOT every chapter has an epigraph. Each chapter's opening differs
  (flash-forward vignette, a scene-setting description, or the dateline direct;
  ch04 opened with a lyrical Qujiang Pool epigraph, ch05 with the boxwood
  writing-case vignette, ch06 with the Zhang/Cao kiln-duel vignette). Translate
  whatever the source has, and translate a recurring vignette identically in both
  places (ch06's opener recurs verbatim at source line 175). The content-file
  time-marker heading line (e.g. 申初) is absorbed into the H2 chapter title, not
  made a paragraph. The source's per-chapter time-gloss (its own footnote on the
  dateline, e.g. "下午3点。申，又名…") is rendered as the SOURCE's own note, in
  italics, prefixed "*[The source appends a note on the hour to each chapter:]*",
  distinct from translator's notes.
- Names: pinyin, one decided rendering per referent, all in glossary.json. Grep
  the glossary before romanizing anything new. Recurring items already decided
  across ch01-ch06 that MUST be reused verbatim include: Zhang Xiaojing, Li Bi
  (Changyuan), Director He / He Zhizhang, Yao Runeng, Cui Qi, Cao Poyan, Xu Bin,
  Tanqi, Wen Ran, Wen Wuji, the Right Shad, Li Heng (the heir apparent), Li Linfu
  (the Right Minister), Long Bo, Old Ge, the Great Sabao, Tong'er, Wang Yunxiu,
  Ma Ge'er, Xiao Yi, Wang Zhongsi (the military commissioner), Feng Dalun, Prince
  Yong / Li Lin, Yuan Zai, Yang Shenjiao, Princess Changning, Jia Shiqi; the
  Jing'an Bureau, the Lüben Guards, the Jinwu Guard, the Sabao Office, the
  Directorate for the Palace Buildings, the Xuanhui Court, the Dog Kennel, the
  Ministry of Works, the Forestry and Crafts Bureau (虞部), the Court of Judicial
  Review, the Censorate, the Ministry of Justice, the Palace Domestic Service, the
  Right Xiao Guard / Leopard Cavalry / Sixteen Guards of the Southern Command;
  Chang'an, Wannian/Chang'an County, the Vermilion Bird Avenue, the West Market,
  Guangde/Yanshou/Huaiyuan/Xiuzheng/Changming Wards, the Pingkang Quarter, Qujiang
  Pool, the Qixia/Yanxing Gates, the Jinguang Gate, the Daming/Xingqing Palaces,
  the Guangtong Canal, the Onon/Orkhon rivers; shichen ("double-hour"), watchtower,
  constable, buliang chief/men, county commandant (县尉), Wolf Guards, Türk, the
  Sage, His Majesty, Your Highness, the Lantern Festival, Tianbao/Kaiyuan,
  barrier-knife, pocket crossbow, smoke pellet, binding-cord, Que-le Huo-duo, the
  art of the Great Archive, the Nine-Gate Drum, the Five Kennels, the Bear Fire
  Gang, "casting flesh-coins," Kunlun/Zanj slave, Mazda, polo (击鞠), the
  Oil-Sprinkled Ground, rock-oil (石脂), fierce-fire / fierce-fire thunder (猛火/
  猛火雷), fire-proof cloth (火浣布), the dragon-sill (过龙槛), commissioning the
  watchtowers (假节望楼), the Five-Faced Yama / "Zhang the Yama".
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
  in English, an "all-directions" 四X idiom, a swear-word, a myriad-idiom, a
  watchtower rhyme-cipher like 二十六六), extend noise.txt (own-line comments) or
  WORD_NUM, and say so in PROGRESS. But if the flag is a REAL quantity, fix the
  ENGLISH to carry the value instead of noising it (ch06: 一百步 → "a hundred
  paces", 十来个 → "ten-odd", 三面 → "on three sides"). A genuinely dropped number
  must still fail.
- 二楼/二层 ("the second floor / a two-story ...") is rendered with an English
  number-word ("second"/"two-story") so its numeral survives the number check.
  For an approximate "ten-odd" (十余/十几/十来) render "ten-odd" (keeps 10), not "a
  dozen or so" (loses it).

## State / traps

- Working branch is claude/the-longest-day-in-changan; push only there. Do not
  spin off new branches. (A harness note may name a different per-batch branch;
  CLAUDE.md rule 2 and the commissioner override it. Batch 6 was started on a
  stray per-batch branch and all work was moved onto claude/the-longest-day-in-
  changan; the remote's canonical branch is claude/the-longest-day-in-changan.)
- data/src/ and data/figs/ are gitignored; regenerate with ingest_epub.py.
- The bilingual QC file never ships (and is not committed). Note anchors must be
  verbatim English substrings or the build refuses. XHTML note bodies use numeric
  character references, never named entities. The builder inserts note anchors
  BEFORE markup substitution.
- Extractor artifacts: a logical paragraph is sometimes split across two lines in
  data/src (no sentence-ending punctuation on the first). Merge such halves into
  one bilingual pair (ch06 merged the opening vignette's three lines and the
  dateline's two lines). Colon-lead-in speech lines can be kept as separate
  paragraphs. Parity is self-consistent either way (both reading and data/zh are
  derived from the bilingual), so keep each `>` paired with exactly one English
  paragraph.
- Cite by chapter, never by page.
- The source text sometimes uses 中元 ("Ghost Festival") where it means 上元
  ("Lantern Festival"); when encountered, translate the intent, not the literal
  wrong festival name. (BUT: ch06's 盂兰盆节 river-lanterns in Zhang's roll-call is
  a genuine Ghost-Festival reference, not that slip — render it faithfully.)
- Watch for authorial slips (ch03 had 祆正-for-Sabao and a Tianbao-3-vs-"twenty
  years" tutor date; ch04 wrote 麻格心 once for 麻格儿; ch05 line 10 has a doubled
  negative; ch06's time-gloss writes 日铺 for 日晡). Render faithfully, leave
  visible, flag in PROGRESS rather than silently correcting.
- A footnote's subject gets its note at its FIRST appearance in the whole book.
  Before adding a note, grep the built ch01..ch(n-1) reading files: e.g. the
  Guangtong Canal and Wang Zhongsi first appear before ch06, so ch06 did NOT
  re-note them.
