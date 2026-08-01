# HANDOFF — The Longest Day in Chang'an (长安十二时辰), Ma Boyong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 done and approved. Batches 1-8 (ch01-ch08) COMPLETE: translated,
checked, footnoted, built, QA green, committed. Next is Batch 9 (ch09). 17
chapters plus 2 afterwords remain, one chapter per batch (B25 = the two
afterwords together).

Chat naming: each batch runs in its own chat named `Chang'an B<n>` (this batch
was `Chang'an B8`; the next is `Chang'an B9`). CLAUDE.md records the rule; the
kickoff block below opens with that name as its first line on purpose. Keep it
there.

## Message to paste into the next chat

```
Chang'an B9
Read CLAUDE.md in full (the commissioner's rules at the top are non-negotiable),
then HANDOFF.md, then book.json. We are translating 长安十二时辰 (The Longest Day
in Chang'an) by Ma Boyong into an annotated English EPUB; the deliverable is
out/The Longest Day in Chang'an.epub. Step 0 and Batches 1-8 (ch01-ch08) are
done; the 25-batch plan (one chapter per batch) is approved.

Do Batch 9 = ch09 (第九章 酉正 / "Chapter Nine. The Hour of the Rooster, Second
Half (6 p.m.)") end to end. It is ~14,154 source chars. NOTE: data/src/ and
data/figs/ are gitignored and rebuild from source.epub; if data/src/ is absent in
a fresh clone, run `python3 scripts/ingest_epub.py source.epub` first. Read the
batch's source from its text_file in book.json (data/src/19_text00019.txt); the
source is authoritative, quote it verbatim in the bilingual QC file and render it
faithfully and in full. Author one aligned bilingual QC file out/ch09_bilingual.md
(source '>' blockquote line, English paragraph beneath; the chapter title tagged
'## H2 <English title>'; each chapter's opening differs — render whatever the
source has, whether a flash-forward vignette, a scene-setting description, or the
dateline direct, and translate a recurring vignette identically in both places;
the source's content-file time-marker heading line is absorbed into the H2 title,
as in ch01-ch08; render the source's per-chapter time-gloss final line as the
source's own italic note, prefixed '*[The source appends a note on the hour to
each chapter:]*'). Watch for the source's scene-break rules (Image00005.jpg): the
house style renders each scene shift as a plain paragraph break, no separator
glyph. Then generate out/ch09_reading.md and the parity source with
`scripts/split_bilingual.py out/ch09_bilingual.md ch09 "第九章　酉正"` (use the
exact full-width-space zh title from book.json). Run
`scripts/check_numbers.py out/ch09_bilingual.md --noise noise.txt` (extend
noise.txt when a NON-quantity numeral is flagged, and record what you add and why;
a real dropped number must still fail — if it is a real quantity, fix the ENGLISH
to carry the value rather than noising it) and
`scripts/check_structure.py --pairs data/zh/ch09.txt out/ch09_reading.md` (parity
must be equal). Reuse EVERY decided rendering already in glossary.json (do not
re-romanize a referent that is already decided; add rows only for new referents,
one rendering each, decided before you romanize). Add footnotes to notes.json
under key "ch09" (verbatim English anchors; XHTML bodies with numeric character
references, never named entities; ~3 per chapter, recurring subjects get their
note at first appearance across the whole book, so skip anything already noted in
ch01-ch08). Add any figure specs to figures.json only if the chapter has a real
content illustration in data/figs/ (the source's footnote-marker glyph
Image00004.jpg and the decorative scene-break rule Image00005.jpg are NOT figures).
Rebuild with `scripts/build_reading_epub.py "out/The Longest Day in Chang'an.epub"`
so the pending-aware TOC links ch01-ch09 content and every other chapter's
skeleton, then run `scripts/qa_epub.py "out/The Longest Day in Chang'an.epub"`
until green. Do a blind double-translation of a literary sample and a round-trip
back-translation of a number-dense sample (separate contexts), and record the
checks and the sample error rate in PROGRESS.md. Rewrite HANDOFF.md with the
Batch 10 (= ch10) kickoff message (its fenced block opening with the line
`Chang'an B10`), commit, and push to branch claude/the-longest-day-in-changan.
Cite chapters/sections, never page numbers. Never invent bridging text; footnote
genuine ambiguity rather than smoothing it. Do not pause for approval mid-batch.
Deliver the rebuilt EPUB in chat as an attached file.
```

## What is DONE (do not redo)

- Step 0 ingest + survey + skeleton EPUB, approved. 25-batch plan approved.
- Batch 1 = ch01, complete and committed: 12 notes, glossary seeded, qa PASS.
- Batch 2 = ch02, complete: 3 notes (15 total), EPUB metadata set for Kindle/Apple
  Books, qa PASS.
- Batch 3 = ch03, complete: 4 notes (19 total), noise.txt extended, qa PASS.
- Batch 4 = ch04, complete: 3 notes (22 total), noise.txt extended, qa PASS.
- Batch 5 = ch05, complete: 3 notes (25 total), noise.txt extended, qa PASS.
- Batch 6 = ch06, complete: 3 notes (28 total), noise.txt extended (three flagged
  numerals were real quantities fixed in the ENGLISH), qa PASS.
- Batch 7 = ch07, complete: 3 notes (31 total), noise.txt extended (8 idiom/name
  numerals; ONE real count, 张小敬等三人, fixed in the ENGLISH), qa PASS.
- Batch 8 = ch08, complete and committed: out/ch08_reading.md, data/zh/ch08.txt,
  3 notes (34 total), glossary.json updated (4 people / 3 orgs / 6 places / 16
  terms — Yisi, Alopen, Mishihe, Registrar Pang; the Secretariat, the Phoenix
  Pavilion, the Bureau of Sacrifices; Yining/Buzheng/Yankang Wards, the Kaiyuan
  Gate, the Daqin Temple, the Persian Temple; the cross-and-lotus, Nestorian
  temple/monk, the Three Foreign Religions, Manichaeism, Sham, deacon, archbishop,
  ordination certificate, the confession room, the Ordinance to Cherish Written
  Characters, spirit-summoning rue incense, Zhenguan, modao, makara, registrar).
  Crucially the PRE-SEEDED renderings were reused, not re-romanized: 右杀 = "the
  Right Shad", 乌苏米施可汗 = "Ozmish Khagan", 阿史那 = "Ashina", 景教 = "Nestorian".
  noise.txt extended (万物/二是/胡说八道/六耳 — all idiom/enumerator numerals). qa
  PASS (34 notes). Blind double-translation (the Laozi straw-dogs exchange) and
  back-translation (the 15-circuits / 300-prefectures speech) both clean, 0 errors.

## What is NEXT

- Batch 9 = ch09 (第九章 酉正, ~14,154 source chars, data/src/19_text00019.txt).
  Then B10=ch10 ... B24=ch24, B25=ch25+ch26. See book.json's structure/batches.

## House style set by Batches 1-8 (follow it)

- Register: novelistic thriller prose in the book's own voice; all apparatus in
  notes, none inline. Merge sentences where English wants them merged.
- Openings: NOT every chapter has an epigraph. Each chapter's opening differs
  (flash-forward vignette, scene-setting description, or the dateline direct);
  translate whatever the source has, and translate a recurring vignette
  identically in both places (ch04 Qujiang epigraph recurs at its climax; ch05
  writing-case, ch06 kiln-duel, ch07's festival-crowd sentence, and ch08's
  plain-oil-fritters vignette each recur verbatim later and were translated
  identically). The content-file time-marker heading line (e.g. 酉初) is absorbed
  into the H2 chapter title, not made a paragraph. The source's per-chapter
  time-gloss (its own footnote on the dateline) is rendered as the SOURCE's own
  note, in italics, prefixed "*[The source appends a note on the hour to each
  chapter:]*", distinct from translator's notes. Its ordinary words are translated;
  only technical hour-names are romanized.
- Scene breaks: the source divides multi-scene chapters with a decorative rule
  image (Image00005.jpg, alt="line"). House style renders each scene shift as a
  plain paragraph break with NO separator glyph (the rule image is not a figure),
  matching ch01-ch08. If visible scene breaks are ever wanted, that is a global
  change across all chapters at once, not a per-batch call.
- Names: pinyin, one decided rendering per referent, all in glossary.json. Grep
  the glossary before romanizing anything new. Recurring items already decided
  across ch01-ch08 that MUST be reused verbatim include: Zhang Xiaojing, Li Bi
  (Changyuan), Director He / He Zhizhang (+ sons He Dong, He Zeng), Yao Runeng,
  Cui Qi, Cao Poyan, Xu Bin, Tanqi, Wen Ran, Wen Wuji, Li Heng (heir apparent),
  Li Linfu (the Right Minister), Long Bo, Old Ge, the Great Sabao, Tong'er, Wang
  Yunxiu, Ma Ge'er, Xiao Yi, Wang Zhongsi (military commissioner), Feng Dalun,
  Prince Yong / Li Lin, Yuan Zai, Jia Shiqi, Gan Shoucheng, Adjutant Zhao / Zhao
  Qilang; and the Batch-8 cast: the Right Shad (右杀), Ozmish Khagan (乌苏米施可汗),
  Ashina (阿史那), Yisi (伊斯), Alopen (阿罗本), Mishihe (弥施诃), Registrar Pang
  (庞录事). Orgs: the Jing'an Bureau, the Lüben Guards, the Jinwu Guard, the Right
  Xiao Guard / Leopard Cavalry / Sixteen Guards of the Southern Command, the Court
  of Judicial Review, the Censorate, the Ministry of Justice/Works, the Forestry
  and Crafts Bureau (虞部), the Palace Domestic Service, the Jingzhao Prefecture,
  the Stores Section (仓曹), the Secretariat (中书省) / the Phoenix Pavilion (凤阁),
  the Bureau of Sacrifices (祠部). Places: Chang'an, Wannian/Chang'an County, the
  Vermilion Bird Avenue, the West Market, the many wards (incl. Yining/Buzheng/
  Yankang from ch08), the Leyou Plateau, the Cibei Temple, the Daqin/Persian
  Temple, the Kaiyuan Gate, the Chengtian/Zhuque Gates. Terms: shichen
  ("double-hour"), watchtower, constable, buliang chief/men, county commandant
  (县尉), Wolf Guards, Türk, the Sage, His Majesty, Your Highness, the Lantern
  Festival, Tianbao/Kaiyuan/Zhenguan, barrier-knife (障刀), modao (陌刀),
  pocket crossbow, smoke pellet, binding-cord, Que-le Huo-duo, the art of the
  Great Archive, the Nine-Gate Drum, rock-oil, fierce-fire / fierce-fire thunder,
  the Five-Faced Yama, the plum-blossom jade, the curtained hat, Plan B/C, and
  the ch08 Nestorian cluster (景教 = "Nestorian"; the cross-and-lotus; Nestorian
  temple/monk; the Three Foreign Religions; Manichaeism; deacon; archbishop;
  ordination certificate; the confession room).
- Titles/address: 太子/东宫 = "heir apparent" / "the Eastern Palace"; 司丞 (Li Bi)
  = "Deputy Director" (李司丞 = "Deputy Director Li"); 贺监 (He) = "Director He";
  都尉 (Zhang) = "Commander"; 旅帅 (Cui) = "Commander"; 节度 (Wang) = "military
  commissioner"; 殿下 = "Your Highness"; 陛下 = "His Majesty"; 圣人 = "the Sage".
  OFFICE-TITLE renderings: 主事 = "recorder"; 录事 = "registrar" (kept distinct;
  庞录事 = "Registrar Pang"); 评事 = "Evaluator"; 参军 = "adjutant" (Adjutant Zhao);
  将军 (Gan) = "General"; 员外郎 (He Dong) = "vice-director"; 执事 = "deacon";
  大主教 = "archbishop"; 工部/虞部/大理寺/御史台/刑部/内侍省/仓曹/中书省/祠部 per
  Hucker (see glossary). 永王 = "Prince Yong"; 节级 = "warder"; 云麾将军 = "General
  of the Cloud Banner"; 右杀 = "the Right Shad".
- Numbers: run check_numbers with --noise noise.txt every batch. When it flags a
  non-quantity numeral (a name, an idiom, a round number spelled out analytically
  in English, an "all-directions" 四X idiom, a swear-word, a myriad-idiom, a
  ranking-name, a list enumerator like 二是/二来, a cipher), extend noise.txt
  (own-line comments) or WORD_NUM, and say so in PROGRESS. But if the flag is a
  REAL quantity, fix the ENGLISH to carry the value instead of noising it (ch06:
  一百步 → "a hundred paces", 十来个 → "ten-odd", 三面 → "on three sides"; ch07:
  张小敬等三人 → "the three of them"). A genuinely dropped number must still fail.
- 二楼/二层 rendered with an English number-word so its numeral survives; for
  approximate "ten-odd" (十余/十几/十来) render "ten-odd" (keeps 10), not "a dozen
  or so" (loses it).

## State / traps

- Working branch is claude/the-longest-day-in-changan; push only there. Do not
  spin off new branches. (A harness note may name a different per-batch branch;
  CLAUDE.md rule 2 and the commissioner override it. Batches 6, 7, and 8 were each
  started on a stray per-batch branch and all work was consolidated onto
  claude/the-longest-day-in-changan, the remote's canonical branch, with the stray
  branches deleted. B8 specifically: the session opened on
  claude/the-longest-day-in-changan-vgrwzo, which had no remote and had diverged
  ahead of the stale local canonical branch; it was reset onto
  origin/claude/the-longest-day-in-changan and the stray deleted before work.)
- data/src/ and data/figs/ are gitignored; regenerate with ingest_epub.py.
- The bilingual QC file never ships (and is not committed). Note anchors must be
  verbatim English substrings or the build refuses. XHTML note bodies use numeric
  character references, never named entities. The builder inserts note anchors
  BEFORE markup substitution.
- Extractor artifacts: a logical paragraph is sometimes split across two lines in
  data/src (no sentence-ending punctuation on the first). Merge such halves into
  one bilingual pair (ch07/ch08 merged the opening vignette's two lines and the
  dateline's two lines). Colon-lead-in speech lines can be kept as separate
  paragraphs. Parity is self-consistent either way.
- Cite by chapter, never by page.
- The source sometimes uses 中元 ("Ghost Festival") where it means 上元 ("Lantern
  Festival"); translate the intent, not the literal wrong festival name. (BUT
  ch06's 盂兰盆节 river-lanterns in Zhang's roll-call is a genuine Ghost-Festival
  reference, not that slip — render it faithfully.)
- Watch for authorial slips (ch03 祆正-for-Sabao and a Tianbao-3-vs-"twenty years"
  tutor date; ch04 麻格心 once for 麻格儿; ch05 line 10 doubled negative; ch06 and
  ch07 time-gloss write 日铺 for 日晡; ch07 line 69 writes 五桶 where the math needs
  十五桶; ch08 time-gloss writes 17是至19时 for 17时至19时, and the line-94 vignette
  drops 油 from 油子). Render faithfully, leave visible, flag in PROGRESS rather
  than silently correcting.
- A footnote's subject gets its note at its FIRST appearance in the whole book.
  Before adding a note, grep the built ch01..ch(n-1) reading files. Already-noted
  or already-appeared-and-passed subjects to NOT re-note include: He Zhizhang,
  Yuan Zai, Prince Yong, Ozmish Khagan (noted ch01), the Right Shad (first
  appeared ch02, note-slot past), Sun Simiao, the Right Xiao Guard, the Censorate,
  and everything in notes.json ch01-ch08.
