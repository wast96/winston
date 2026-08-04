# HANDOFF — The Longest Day in Chang'an (长安十二时辰), Ma Boyong

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

Status: Step 0 done and approved. Batches 1-24 (ch01-ch24) COMPLETE: translated,
checked, footnoted, built, QA green, committed. Only ONE batch remains: Batch 25
(ch25 后记一 + ch26 后记二, the two afterwords together) — the LAST batch. After it
the whole book is done: it ships the two afterwords, any back matter/colophon, a
whole-book QA pass, and a COMPLETION REPORT instead of another handoff.

Chat naming: each batch runs in its own chat named `Chang'an B<n>` (this batch was
`Chang'an B24`; the next and last is `Chang'an B25`). CLAUDE.md records the rule;
the kickoff block below opens with that name as its first line on purpose.

## Message to paste into the next chat

```
Chang'an B25
Read CLAUDE.md in full (the commissioner's rules at the top are non-negotiable),
then HANDOFF.md, then book.json. We are translating 长安十二时辰 (The Longest Day
in Chang'an) by Ma Boyong into an annotated English EPUB; the deliverable is
out/The Longest Day in Chang'an.epub. Step 0 and Batches 1-24 (ch01-ch24) are
done; this is the LAST batch of the approved 25-batch plan.

Do Batch 25 = ch25 (后记一 / "Afterword I", ~1,838 source chars,
data/src/53_text00050.txt) + ch26 (后记二 / "Afterword II", ~966 source chars,
data/src/55_text00051.txt) TOGETHER, end to end. NOTE: data/src/ and data/figs/ are
gitignored and rebuild from source.epub; if data/src/ is absent in a fresh clone,
run `python3 scripts/ingest_epub.py source.epub` first. These two units are the
author's AFTERWORDS (part="Afterword" in book.json), NOT numbered chapters: they are
essays, so there is NO dateline, NO opening vignette, and NO per-chapter time-gloss
line to render (do not invent one; there is no hour to watch this batch). Each source
file's FIRST line is just the piece's title (后记一 / 后记二) and is absorbed into the
H2 title exactly as the chapter content-marker lines were (ch01-ch24); use the
book.json title_en ("Afterword I" / "Afterword II"). Everything after line 1 is body.

The source is authoritative: quote it verbatim in the bilingual QC files and render
it faithfully and in full. Author ONE aligned bilingual QC file PER unit
(out/ch25_bilingual.md, out/ch26_bilingual.md; source '>' blockquote line, English
paragraph beneath; the title tagged '## H2 <English title>'). Use the most reliable
method (B16-B24 used it): write a small generator PER unit that reads the source
lines from data/src, pairs each with your hand-authored English, MERGES any
extractor-split halves, and ASSERTS the concatenation of every '>' blockquote equals
the source content character-for-character before running the checks (B24 =
scripts/gen_ch24_bilingual.py, 351 body paragraphs). Watch for extractor-split
paragraphs (a logical paragraph broken across two data/src lines, the first ending on
a comma or mid-phrase): scan each source file for a line whose LAST char is not in
。！？"）…— and merge such halves into one bilingual pair (but a line ending in the
full-width close-quote " is already terminal, and a multi-paragraph quotation whose
earlier paragraph's quote is left OPEN stays a separate pair). NOTE 后记一 ends with a
trailing U+200B zero-width-space line to drop (as ch01-ch24 did); check 后记二 too.
Then, for each unit, generate the reading text and the parity source with
`scripts/split_bilingual.py out/ch25_bilingual.md ch25 "后记一"` and
`scripts/split_bilingual.py out/ch26_bilingual.md ch26 "后记二"` (use the exact zh
titles from book.json). Run `scripts/check_numbers.py out/ch25_bilingual.md
--noise noise.txt` and the same for ch26 (后记一 is number-dense: 天宝三载, 四月, 九月,
贺知章 died 享年八十有四 = 84, the Türk-khagan succession, An Lushan's 范阳节度使/河北
采访使 rise — carry every real quantity in the English; extend noise.txt only for
NON-quantity numerals and record what you add and why; a real dropped number must
still fail — the check_numbers traps and the ORDERING rule are documented at length
in noise.txt's header and in the House-style section below). Run
`scripts/check_structure.py --pairs data/zh/ch25.txt out/ch25_reading.md` and the
same for ch26 (parity must be EQUAL each).

Reuse EVERY decided rendering already in glossary.json (grep before you romanize):
贺知章 = He Zhizhang / 贺监 = Director He, 乌苏米施可汗 = Ozmish Khagan, 王忠嗣 = Wang
Zhongsi, 安禄山 = An Lushan, 范阳 = Fanyang, 平卢 = Pinglu, 朔方 = Shuofang, 回纥 (if
present) — CHECK the glossary, add a row only for a genuinely NEW referent, one
rendering each, decided before you romanize (likely-new in the afterwords: 白眉可汗
[the Türks' Baimei/White-Brow Khagan, historical]; 回纥 [the Uyghurs, if not yet
glossed]; 山阴 [He Zhizhang's home, Shanyin]; 河北采访使 [Surveillance Commissioner of
Hebei, Hucker-style]; 大雁塔 [the Great Wild Goose Pagoda]; 曲江池 [Qujiang Pool, if
not glossed]; 《刺客信条》 = Assassin's Creed; 知乎 = Zhihu). Add footnotes to
notes.json under keys "ch25"/"ch26" (verbatim English anchors; XHTML bodies with
numeric character references for punctuation/accents, literal CJK for Chinese terms
is fine; never HTML named entities; ~3 total across the two short pieces, and skip
anything already noted in ch01-ch24 — An Lushan is noted at ch16, He Zhizhang at
ch02, the Türk khaganate/Ozmish at ch01/ch02). Strong candidates: 《刺客信条》/
Assassin's Creed and the 知乎 question that seeded the novel (后记二's origin story);
the 天宝三载 aftermath in 后记一 (the Türk collapse, He Zhizhang's death, An Lushan's
quiet rise foreshadowing 755) if it is not fully covered by the ch16 An Lushan note.
Add figure specs to figures.json only if a unit has a real content illustration in
data/figs/ (the footnote-marker glyph Image00004.jpg and the scene-break rule
Image00005.jpg are NOT figures; ch01-ch24 had none).

BACK MATTER (this is the last batch, so handle it now): the translator's-note page
already renders from book.json's translator_note (verbatim). The colophon in
back_matter.json is INERT by design (the builder renders a colophon ONLY when a
top-level "colophon" key is present; the file ships a "_colophon_schema" stub). Add
a real colophon ONLY if the source has a copyright/imprint/奥付 page worth
translating; otherwise leave back_matter.json inert (the book already has front
matter + translator's note). Do not invent an imprint page.

Rebuild with `scripts/build_reading_epub.py "out/The Longest Day in Chang'an.epub"`
(it should now report 26 of 26 chapters translated), then run
`scripts/qa_epub.py "out/The Longest Day in Chang'an.epub"` until green. Do a
WHOLE-BOOK QA pass: qa_epub PASS across the full 26-document spine; confirm the full
hyperlinked TOC links every part/chapter (no skeleton pages left — ch25/ch26 now have
content); note refs == bodies == backlinks and numbering sequential. Do a blind
double-translation of a literary sample (后记二's Assassin's-Creed / Chang'an-as-dream
passage is ideal) and a round-trip back-translation of a number-dense sample (后记一's
天宝三载 epilogue), in separate contexts, and record the checks and the sample error
rate in PROGRESS.md.

THEN, because this is the LAST batch, write a COMPLETION REPORT (a new file, e.g.
COMPLETION.md) instead of another HANDOFF kickoff: summarize the whole book — 24
chapters + 2 afterwords translated, the total note count, the glossary size, every
check that ran and its final result, and the definition-of-done checklist from
CLAUDE.md ticked off. IMPORTANT re the Stop hook (scripts/check_kickoff_pasted.py):
it blocks the turn only if your commit TOUCHES HANDOFF.md and the kickoff block's
first+last lines are not in your reply. On this final batch there is no next kickoff,
so DO NOT modify HANDOFF.md in your commit (leave it as-is, or the hook will demand a
kickoff block that no longer exists) — put the wrap-up in COMPLETION.md instead.
Commit and push to branch claude/the-longest-day-in-changan. Cite chapters/sections,
never page numbers. Never invent bridging text; footnote genuine ambiguity rather
than smoothing it. Do not pause for approval mid-batch. Deliver the final rebuilt
EPUB in chat as an attached file.
```

## What is DONE (do not redo)

- Step 0 ingest + survey + skeleton EPUB, approved. 25-batch plan approved.
- Batches 1-23 (ch01-ch23) complete and committed. (See prior handoffs / PROGRESS.md
  for the per-batch detail; note count reached 79 by end of ch23.)
- Batch 24 = ch24 (第二十四章 巳初 / Snake hour, first half, 9 a.m.), the FINAL
  narrative chapter, complete and committed: out/ch24_reading.md, data/zh/ch24.txt,
  scripts/gen_ch24_bilingual.py (351 body paragraphs, 21,169 source chars incl. the
  gloss; verbatim concat == source char-for-char, L2-L356). 3 notes (82 total: the
  咏柳 "Ode to the Willow" poem / He Zhizhang's coded name; 茵芋酒/大风疾 the Medicine
  King's yinyu-wine and leprosy; 翁仲 the wengzhong tomb-guardian statue). glossary
  +6 rows (people 刘骆谷/Liu Luogu, 张守珪/Zhang Shougui; terms 寄粜/consignment-sale,
  太子宾客/Guest of the Heir Apparent, 翰林/Hanlin academician; place 柳京/the Willow
  Capital). noise.txt +2 (百思 [idiom]; 八千六百 [the 8600贯 consignment payment,
  carried analytically in English]). No WORD_NUM change. Checks: verbatim PASS;
  check_numbers 0 unresolved (352 pairs); parity 352/352 EQUAL; qa_epub PASS (82
  notes); blind double-translation (L353 closing panorama) and round-trip
  back-translation (L108/L111 account numbers) both clean, 0 content errors.
  HOUR MATCHES: ch24 is 巳初/9 a.m., its dateline is 巳初, and the gloss describes
  巳/9 a.m. — all agree. SOURCE VARIANT flagged: L85 营山杂胡 for 营州杂胡 (An Lushan's
  origin), rendered with the decided referent "a mongrel Hu of Yingzhou." RESOLUTION:
  the ch23 traitor 陆三 was bought by the 平卢留后院; paymaster = 安禄山; but the TRUE
  mastermind is 贺东 (He Dong), 贺知章's adopted son, out of filial devotion; he
  self-immolates. Li Bi confesses he poisoned the comatose 贺知章. The novel ends on
  Zhang Xiaojing's first tear over Chang'an. （全文终） rendered "(The End)".

## What is NEXT

- Batch 25 = ch25 (后记一, ~1,838) + ch26 (后记二, ~966) TOGETHER, the LAST batch:
  the two authorial afterwords, plus any back matter/colophon, a whole-book QA pass,
  and a COMPLETION REPORT (not another handoff). data/src/53_text00050.txt and
  data/src/55_text00051.txt. See book.json's structure (both part="Afterword").
- After B25 the whole EPUB is done: front matter + 24 chapters + 2 afterwords, full
  hyperlinked TOC with NO skeleton pages left, figures (none — the book has no content
  illustrations), 82+ footnotes at reference density, glossary + translator's note
  current, qa_epub PASS across the whole spine.

## House style set by Batches 1-24 (follow it)

- Register: novelistic thriller prose in the book's own voice; all apparatus in
  notes, none inline. Merge sentences where English wants them merged. Keep the
  book's own coarseness where it is coarse (ch13 "我他妈"; ch23/ch24 kept Feng Dalun's
  小娼妇 = "little whore"). The Son of Heaven's imperial 朕 = royal "Us/We/Our"; 陛下 =
  "Your Majesty" (address) / "His Majesty" (reference); 圣人/圣上 = "the Sage"; 微臣 =
  "your humble servant"; 坤道 = "female Daoist"; 妾身 = "I". The afterwords are
  ESSAYS in the author's own expository/personal voice — keep that register (do not
  novelize them), and 后记二 is first-person (马伯庸 speaking as "I").
- Openings/datelines/time-gloss: these apply to the 24 numbered chapters only. The
  AFTERWORDS have none — do not add a dateline, vignette, or time-gloss. Each
  afterword's source line 1 is its title (后记一/后记二), absorbed into the H2 title.
- Scene breaks: rendered as a plain paragraph break with NO separator glyph (the rule
  image Image00005.jpg is not a figure), matching ch01-ch24.
- Names: pinyin, one decided rendering per referent, all in glossary.json (134
  people, 237 terms, 204 places as of ch24). GREP the glossary before romanizing
  anything new. Cast/terms to reuse verbatim in the afterwords include: He Zhizhang /
  Director He (贺监), Ozmish Khagan (乌苏米施可汗), Wang Zhongsi, An Lushan (安禄山, noted
  ch16), Fanyang/Pinglu/Shuofang, the Türks (突厥) / Türk Wolf Guards, the aphids
  (蚍蜉), the Vermilion Bird Avenue, Qujiang Pool, the Leyou Plateau. Titles/offices
  per Hucker: 节度使 = military commissioner, 采访使 = Surveillance Commissioner,
  员外郎 = vice-director, 主事 = recorder, 都尉 = Commander, 靖安令 = the Director of
  the Jing'an Bureau, 靖安司丞 = Deputy Director.
- Numbers: run check_numbers with --noise noise.txt every unit. When it flags a
  non-quantity numeral (a name with a digit, an idiom, a round number spelled out
  analytically, an "all-directions" 四X idiom, a myriad-idiom, a character-COUNT, a
  literary-form idiom, a 两-idiom, an "in the event" 万一), extend noise.txt (own-line
  comments) or WORD_NUM, and say so in PROGRESS. ORDERING is load-bearing: a new strip
  pattern must precede any shorter built-in/earlier entry that would eat part of it
  first; watch the reverse traps documented in noise.txt (a pre-existing entry
  orphaning a residual, e.g. 四肢百骸 → noise 百骸; the built-in MEASURE rules
  一[…张/天/个…] running AFTER the --noise pass and orphaning a bare 万/十, e.g. noise
  the whole 万一/十一; a name-with-digit like 陆三). If a flag is a REAL quantity, fix
  the ENGLISH to carry the value instead of noising it (ch24: 三人 → "the three of
  them"; 八千六百贯 → "eight thousand six hundred strings" [noised for the checker,
  value carried]; 百万之众 → "a million strong"). A genuinely dropped number must still
  fail. The checker's English parser reads cardinals and a FEW ordinals (first-tenth,
  thirteenth-seventeenth, twentieth, twenty-fifth) but NOT eleventh/eighteenth/
  nineteenth nor the other compound ordinals unless ADDED to WORD_NUM, and CANNOT
  build "150"/"8600" from analytic words but CAN match "a hundred/thousand/million";
  so carry high compounds as digits or as "a hundred/thousand/million," and note when
  you noise a compound because the value is carried in words. For 后记一: 享年八十有四 =
  84 ("eighty-four years old" carries it; 八十有四 = 八十 + 有 + 四, so the checker sees
  84 from 八十四 — verify, and if the intervening 有 breaks it, carry "eighty-four" and
  it composes from TENS+ONES); 天宝三载/四月/九月 are real (third year, fourth/ninth
  month). 二十余年-style approximates are already noised.
- 二楼/二层 rendered with an English number-word so the numeral survives; approximate
  "ten-odd" (十余/十几/十来) render "ten-odd" (keeps 10), not "a dozen or so". Units:
  尺 = chi, 里 = li, 丈 = zhang, 抱 = arm-span, 分 = fen, 弹指 = finger-snap, 刻 = mark.

## State / traps

- Working branch is claude/the-longest-day-in-changan; push only there. Do not spin
  off new branches. (A harness note may name a different per-batch branch; CLAUDE.md
  rule 2 and the commissioner override it. B24 opened on claude/changan-b24-
  translation-jf3jxp, whose HEAD equaled origin/claude/the-longest-day-in-changan; the
  canonical branch was checked out, reset to origin, the work done there, committed and
  pushed. Do the same for B25.)
- data/src/ and data/figs/ are gitignored; regenerate with ingest_epub.py. The
  bilingual QC files never ship (and are not committed). Note anchors must be verbatim
  English substrings or the build refuses; make the anchor unique. XHTML note bodies:
  literal CJK is fine, numeric character references for typographic punctuation and
  accented Latin, never HTML named entities. The builder inserts anchors BEFORE markup
  substitution.
- When editing the JSON ledgers, use a Python load/modify/dump (ensure_ascii=False,
  indent=2 for glossary.json AND notes.json) rather than hand-editing braces; then
  json.load to verify.
- The verbatim-generator method (B16-B24) is the repeatable safeguard: read source
  lines from data/src, pair with hand-authored English, merge extractor-split halves,
  assert concat of all '>' lines == source content char-for-char BEFORE the checks.
  For the afterwords write ONE generator per unit (gen_ch25_bilingual.py,
  gen_ch26_bilingual.py). NOTE 后记一 ends with a trailing U+200B line (drop it), like
  the chapters; check 后记二's tail too.
- Cite by chapter/afterword, never by page.
- STOP HOOK: scripts/check_kickoff_pasted.py (wired in .claude/settings.json) blocks
  the turn from ending after any commit that TOUCHES HANDOFF.md unless the kickoff
  block's first AND last lines both appear verbatim in your final chat reply. On the
  LAST batch there is no next kickoff — so DO NOT touch HANDOFF.md in the B25 commit;
  write the wrap-up in COMPLETION.md and leave HANDOFF.md unmodified, and the hook
  will not fire.
- A footnote's subject gets its note at its FIRST appearance in the whole book. Before
  adding a note, grep the built ch01..ch24 reading files AND check notes.json.
  Already-noted subjects to NOT re-note include everything in notes.json ch01-ch24
  (An Lushan ch16, He Zhizhang ch02, Ozmish Khagan/the Türk khaganate ch01/ch02, the
  aphids ch09, and the full ch01-ch24 list).
