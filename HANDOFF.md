# HANDOFF — The Golden Roc Dynasty (陆小凤传奇·金鹏王朝, Gu Long)

This file is the baton. A fresh session with no memory reads it and starts
immediately. **It is the ARCHIVE of the kickoff message, not its delivery:
every batch ends with this file's kickoff block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count.** Rewrite it
at the end of every batch; always keep the paste-ready kickoff message below as
its first section. When the book completes, replace the kickoff with the
completion notice and do not touch it afterward (the Stop hook keys off it).

## Message to paste into the next chat

```
Lu Xiaofeng 1 B05

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 金鹏王朝 (The Golden Roc Dynasty), Volume 1 of Gu Long's Legend of Lu Xiaofeng, from a digital source EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/lu-xiaofeng-1; expect the harness to start you on a stray per-task branch and consolidate per rule 2 (check out claude/lu-xiaofeng-1, reset to origin, and if a stray branch carries commits, fast-forward or cherry-pick them on, push, and delete the stray).  Deliverable out/lu-xiaofeng-1.epub.

Run ./setup.sh first and record any failure in PROGRESS.md. NOTE: the regression harness reports 9/10 green with ONE expected failure ("hook stands down on template stub") — that case only passes while HANDOFF.md holds the template placeholder; now that HANDOFF carries a real kickoff the Stop hook correctly enforces, so that one test necessarily reads FAIL for the rest of the book. Not a defect; do not "fix" it. data/src and data/src_epub are gitignored and regenerable: if they are missing, run scripts/ingest_epub.py source.epub (do NOT overwrite book.json). This book has NO source-edition footnotes; re-grep each unit's source for \[\d+\] and record "none present" per unit in PROGRESS.md.

ch01 remains the FROZEN REFERENCE for register and PARAGRAPHING. Before translating, READ out/ch05_reading.md (The Feast) AND out/ch06_reading.md (A Song of Sorrow) end to end — those are the freshest voice, plus ch01-ch04 as needed. Study STYLE.md, HANDOFF's "Paragraphing", "Attribution", and the voice sheets (Lu Xiaofeng, Ximen Chuixue, Hua Manlou, Princess Danfeng, the Great King, Shangguan Xue'er, old Huo/Huo Xiu, the Honest Monk, Master Sun, Ouyang Qing, and the three killers are all now written in HANDOFF). Money/units are SETTLED: keep the period units (cash / catty / tael / li / cun / zhang) with footnotes, no domestication. Watch comma density; em dashes sparingly; contractions measured. Consult glossary.json (now 63 rows) and authority.json BEFORE romanizing anything.

Do Batch B05 = Chapters 6-7 (ch07 第六章 珠光宝气 "Pearls and Splendour", ~7,174 chars, text_file data/src/12_part0000-split-010.txt; and ch08 第七章 市井七侠 "The Seven Heroes of the Marketplace", ~9,841 chars, text_file data/src/13_part0000-split-011.txt), end to end per the CLAUDE.md pipeline:
1. Read each unit's source. Fix extractor-split paragraphs (a line whose last char is not in 。！？"）…— continues the next; B01-B04 had none, but re-check per unit). Chapters 1-12 divide themselves with BARE NUMERIC markers (01, 02, ...) that are scene breaks: recover them as *** (copy scratchpad/build_b04.py, re-range the CH-lists and the two builder calls for ch07/ch08 — the RANGES list uses spans/singles helpers; find the divider line numbers with grep for the ^01/^02 markers, exclude them from the merged source, and pass the after-paragraph indices as the breaks list). build_b04.py and scratchpad/qc_config.json are COMMITTED (in scratchpad/) — reuse them; if scratchpad is empty on a fresh container, they are in git under scratchpad/.
2. Translate to the frozen house style (read STYLE.md and the reading.md files): fluent, literary, image-forward, economical; MERGE narration into paragraphs by beat, keep dialogue turns and punch-lines on their own; recast freely; watch comma density. ATTRIBUTION RULE (load-bearing for the checks): every dialogue turn whose source names a capitalised-glossary character (Lu Xiaofeng, Princess Danfeng, Shangguan Xue'er, Ximen Chuixue, Hua Manlou, Huo Tianqing, ...) MUST carry that full rendering once, via a natural "said X" attribution or an action beat — otherwise check_content, qc_entities, AND check_align all flag it. Lowercase-en names (the Great King, the Honest Monk, Master Sun, old Huo) are exempt from check_content but qc_entities still wants the first/last word ("the"/"King"/"Master") present. Never invent bridging text; render digitization glitches to plain sense and LIST each in PROGRESS.md; source errors of fact stay visible and get a footnote. Verify each chapter's TAIL against the source before shipping.
3. Author out/ch0N_en.json as MERGED English paragraphs; build via the merged-source method (build_b04.py pattern): make_bilingual.py ch0N <merged_src> "<chapter title>" out/ch0N_en.json 2, insert the bare-numeric -> *** scene breaks, split_bilingual.py. Then verify_unit.py ch0N (parity + numbers with --noise data/noise.txt + anchors); check_align.py ch0N; check_content.py --config scratchpad/qc_config.json (extend docs/sources to add ch07/ch08); qc_entities.py out/ch0N_bilingual.md glossary.json. WATCH THE NUMBER CHECK for tael 两 (patterns after 十/百/千/万/多 are in noise; a NEW amount pattern may need a new documented lookbehind — see PROGRESS B02/B03) and for colour/direction/set idioms (五色/五彩/四射/丑八怪/十足十/六亲不认/飘零 already noised).
4. Footnotes per the reader model (Western reader, no Chinese background); first-appearance greps + a NOT-re-noted list per unit; density keeps tapering (expect ~4-6/chapter). Use apparatus_merge.py for NOTES only (its glossary path adds rows FLAT and must NOT be used — add glossary rows under the two-level sections directly with Edit/Write and validate with check_apparatus.py). check_apparatus.py clean.
5. Rebuild, qa_epub.py green, epubcheck (/tmp/epubcheck-5.1.0/epubcheck.jar) clean, check_structure.py --config scratchpad/qc_config.json PASS, check_register.py --ref out/ch01_reading.md out/ch07_reading.md and out/ch08_reading.md within tolerance. Record every check in PROGRESS.md; update HANDOFF.md; commit and push to claude/lu-xiaofeng-1.
6. End the batch per CLAUDE.md: attach the rebuilt out/lu-xiaofeng-1.epub in the chat AND paste the B06 kickoff verbatim in the same reply.

Cite chapters and sections, never pages. Do not pause for approval mid-batch (B05 is a normal batch, no gate).
```

## What is DONE (do not redo)

- **Step 0 survey** (prior session): ingested the source, authored book.json
  (13 units), built the skeleton EPUB.
- **B01 = Prologue (ch01)** — COMPLETE, revised at the voice gate (rounds 2-5).
  4 vignettes; 154 paragraphs; 15 footnotes. **ch01 is the FROZEN REGISTER
  REFERENCE** (contractions 40.3/1k, rhythm CV 0.75).
- **B02 = Chapter 1 (ch02, 有四条眉毛的人)** — COMPLETE. 289 merged paragraphs;
  11 footnotes. Lu Xiaofeng arrives; the Blue-Robe Tower and the three killers.
- **B03 = Chapters 2-3 (ch03 丹凤公主 + ch04 大金鹏王)** — COMPLETE. ch03: 323
  merged paragraphs (3 scenes), 4 footnotes. ch04: 333 merged paragraphs (4
  scenes), 6 footnotes. The princess is named; the fallen kingdom and Lu's
  contract are established.
- **B04 = Chapters 4-5 (ch05 盛宴 + ch06 悲歌)** — COMPLETE. ch05: 306 merged
  paragraphs (3 scenes), 6 footnotes. ch06: 272 merged paragraphs (4 scenes),
  4 footnotes. 10 new glossary rows (63 total). Every check green: numbers 0
  unresolved, align no strays (median 4.00 / 3.86), content all-in-paragraph
  (284 / 241 occurrences, 2 displacements fixed), qc_entities 0 misses,
  apparatus 0/0, structure ALL PASS (parity 46 anchors), qa_epub PASS, epubcheck
  5.1.0 0/0/0/0, register 26.0 (0.64x) / 22.0 (0.54x) within tolerance. **The
  cast is assembled (Ximen Chuixue won over by the shaved moustache; Zhu Ting
  summoned by banknote); Xiao Qiuyu and Dugu Fang are murdered as warnings by
  the Blue-Robe Tower; Xue'er accuses Princess Danfeng of the killings; Liu Yuhen
  reappears alive and takes Xue'er home; Huo Tianqing invites Lu to the Pavilion
  of Pearls and Splendour.** NOTE: this batch spanned a model change (Fable 5 →
  Opus 4.8) mid-way; register re-checked and held (see PROGRESS B04).

## Tooling in place (do NOT revert)

- `scratchpad/build_b04.py` — the merged-paragraph builder, current version
  (CH05/CH06 range lists built from `spans`/`singles` helpers; writes merged
  source, make_bilingual, split_bilingual, post-inserts `***`). COMMITTED. Copy
  + re-range per new unit; `python3 scratchpad/build_b04.py ch07` runs one unit.
  `scratchpad/qc_config.json` — the check_content / check_structure config
  ({docs, sources, notes}); extend docs/sources for each new unit. COMMITTED.
  (build_b03.py and build_ch02.py remain as earlier copies.)
- `data/noise.txt`: B01 (`第二天`), B02 (王八蛋/王八/三七二十一/十-shape/四顾/
  百炼/四平八稳/四分五裂/五彩缤纷/`(?<=[百千万萬])两`), B03 (`(?<=十)两一(?=锭)`
  then `(?<=十)两` then `(?<=多)两` — ORDER load-bearing — 丑八怪/五色缤纷/
  五色/五彩/四射), **B04 additions**: `十足十` (full-measure idiom), `六亲不认`
  (six-kinships idiom), `飘零` (wanderer's-lot compound, 零≠0). Each documented
  in-file; all justified by real flags. Keep.
- **glossary.json is TWO-LEVEL** (`section -> {zh: row}`). `apparatus_merge.py`
  adds glossary rows FLAT, which the builder/qc choke on. **Use apparatus_merge
  for NOTES only; add glossary rows under sections directly (Edit/Write) and
  validate with check_apparatus.py.** Strip any `glossary` block from the batch
  apparatus JSON before merging. (B03/B04 did notes-only merges + manual
  glossary rows — works.)
- `scripts/check_content.py`, `check_align.py`, `check_numbers.py`,
  `check_structure.py`, `verify_unit.py`: the `***`-skip and spelled-number
  patches from B01/B02 are load-bearing. Do not revert.
- **Regression harness**: `./setup.sh` reports FAILED but 9/10 with ONE EXPECTED
  failure (`hook stands down on template stub`) — the hook correctly enforces
  against the live HANDOFF. Not a defect.

## Paragraphing (book-wide rule — do NOT revert)

The commissioner rejected 1:1 rendering as too choppy. **MERGE adjacent
narration lines into paragraphs grouped by beat; keep dialogue turns and
deliberate punch-lines on their own.** Method (preserves every pipeline
guarantee):

1. Author `out/<id>_en.json` as the MERGED English paragraphs (one array entry
   per final paragraph, reading order).
2. Group source body lines into the same paragraphs; build a MERGED source by
   concatenating each group's original lines VERBATIM (join with '' — every body
   line ends on terminal punctuation; check per unit). `make_bilingual.py <id>
   <merged_src> <title> en.json 2` → parity + verbatim by construction, then
   `split_bilingual.py`. (See `scratchpad/build_b04.py`; the range lists use the
   `spans`/`singles` helpers, dividers EXCLUDED.)
3. **Scene breaks** (ch02-ch12): the source's bare-numeric markers (01, 02, ...)
   are EXCLUDED from the merged source; `***` is post-inserted into
   `out/<id>_reading.md` after the paragraph that ends each scene (build takes
   the list of after-paragraph indices — count them off the drafted en.json).
4. All checks run on the merged pairs (`***` skipped everywhere).

## Attribution (load-bearing — do NOT drop)

Rapid dialogue must name its speaker or three checks fail at once
(`check_content` wants each capitalised glossary name in every paragraph its
source attributes to that character; `qc_entities` wants the first/last name-word;
bare interjections are `check_align` ratio outliers). **Give each dialogue turn
the character's full name once via a natural attribution ("said Lu Xiaofeng",
"Ximen Chuixue smiled", "said the hunter") then let pronouns carry the rest.**
In a two-hander, tag one speaker consistently and vary the other with action
beats. Lowercase-en names (the Great King, the Honest Monk, Master Sun, old Huo)
are exempt from check_content but qc_entities still needs their first/last word
("the"/"King"/"Master") somewhere in the paragraph. **Watch for DISPLACEMENT:**
a paragraph whose source names X but whose English pushed the name into a
different merged paragraph fails check_content — B04 had 2 (a pronoun where the
source repeated the name); fix by restoring the name in-place.

## Voice / house style (the frozen register — match it exactly)

**`STYLE.md` (repo root) is the worked-example version — read it before
translating.** The bar: it should read like a novel a good translator chose to
publish in English. Fluency over literalism; economy (cut pleonasm, say a
doubled idea once); comma density watched (split, or drop a needless comma, em
dashes only when they beat a comma cluster and sparingly); image-forward,
concrete diction; vary rhythm, punch-lines on their own line; contractions
measured; paragraph by beat; dialogue characterised (voice sheets); names once
then pronouns; NO invented substance; keep cultural nouns and period units,
footnoted. Read the freshest reading.md files (ch05, ch06) end to end before
translating.

## Voice sheets (consult at every dialogue scene)

Prologue/ch02 cast (unchanged): **Ximen Chuixue** (near-silent, absolute,
monosyllabic; killing as sacred office — CONFIRMED live in ch06: he holds
killing "a thing sacred and beautiful", the blood-flower on the blade the one
beauty on earth; will not be begged, bargained, or goaded, but yields to Lu's
shaved moustache on a whim; refuses no favour because "what I mean to do, no
one need ask of me"), **Hua Manlou** (gentle, warm, unhurried; serene
declaratives, dry understatement; blind and joyful; feels danger ten li off;
now openly, achingly in love with the vanished Shangguan Feiyan — sings Li Yu
for her, thinks the worst where she is concerned, "loves deeply because he had
never loved before"), **Granny Xiong**, **Shangguan Feiyan** (quick, bright,
teasing; a thief-girl; VANISHED since ch04 — sings a dying-girl's song on the
mountain then vanishes again, leaving a strand of hair; a LIVE plot thread; her
death is asserted by Xue'er and denied by Lu), **Lu Xiaofeng** (the laziest,
wriest, faintly filthy man alive; sees everything; won't risk his neck "for any
friend" then does; the red cape and the four eyebrows mark him — NOW CLEAN-
SHAVEN from ch06, moustache shaved to buy Ximen's help, and fretting it back;
in ch05 he extorts, banters bawdily with a courtesan, and strips a false heart
bare to Hua Manlou's reproach), **Zhu Ting** ("a chair that bites"; summoned
this batch by a 5,000-tael banknote and a soy-sauce phoenix cipher), **the
Boss's Wife**, **Iron-Faced Judge** (dead), **Soul-Hook** (dead — killed by
Xiao Qiuyu, his hooks left on Xiao's corpse), **Liu Yuhen** (the death-seeker;
reported killed by Princess Danfeng in ch06's accusation, then walks in ALIVE
and mild to fetch Xue'er home — a live mystery), **Xiao Qiuyu** (the Heartbreak
Swordsman — MURDERED, ch05, a blood-man dying at Lu's feet unable to speak),
**Dugu Fang** (the Solitary Rider — MURDERED, ch06, pinned to a shrine wall
with judge's pens), **Little Beijing**.

Cast from B03 (unchanged): **Princess Danfeng** (soft, dreamy, gracious, a low
musical voice; shrewd and self-aware; grave dignity over her father and the
fallen kingdom; tender candour — in B04 she comes to Lu's room, is forestalled
by Xue'er's prank, and leaves wounded but believing him; accused by Xue'er of
being the killer behind all three murders), **the Great King of the Golden Roc**
(a fallen monarch's ceremonial, archaic register — source of the elevated
"shall"; keep it; proud, hate-filled, then broken with gratitude — hosts the
feast in a dragon-brocade robe, all high spirits), **old Huo / Huo Xiu** (dry,
terse, deadpan, worldly — no scene this batch).

**New in B04:**

- **the Honest Monk** (老实和尚) — a ragged, square-faced monk who literally
  cannot tell a lie; stammering, mortified, painfully literal. He has done the
  one dishonest thing of his life (visited a courtesan) and must confess it
  because he is honest; then, tormented by Lu's teasing, chants penances and
  crawls off down the street in earnest ("if he says he'll crawl ten li, he
  will not crawl nine and a half"). Comic pathos; every word wrung out of him.
- **Master Sun** (孙老爷, "Turtle-Spawn Sun the Great Master") — a tiny,
  big-headed, gleefully shameless wastrel; the only man who can find the oracles
  Datong and Dazhi. Deadpan, self-mocking ("the greatest rascal under heaven is
  me"), transactional (fifty taels a question, three rules), drunk but sharp.
  Pawns himself between windfalls and waits to be redeemed.
- **Ouyang Qing** (欧阳情) — the top courtesan of the Yiqing Court; honeyed,
  practised, mercenary. All sweetness and fated-love patter while the money
  flows; the instant Lu turns out broke the smile curdles and she pleads a
  stomach-ache. A quick, professional read of a mark.
- **the hunter** (ch06, unnamed) — a plain hillman, curious and literal, easily
  gulled; the vehicle for Xue'er's aunt-and-grand-nephew prank and Hua Manlou's
  earthworm-and-flesh deadpan that routs him.

## Renderings settled to date / carry-forward

**People:** Lu Xiaofeng, Ximen Chuixue, Hua Manlou, Zhang Fang, Granny Xiong,
Hong Tao, Zhao Gang, Cui Yidong, Shangguan Feiyan, Little Beijing, Zhu Ting,
the Boss's Wife, the Iron-Faced Judge, Soul-Hook, Liu Yuhen, Xiao Qiuyu, Dugu
Fang, the Four Heroes of Jiangdong, Princess Danfeng, the Great King of the
Golden Roc, Huo Xiu (old Huo), Dugu Yihe (NOT Dugu Fang), Yan Tieshan,
Shangguan Xue'er, Shangguan Jin, Shangguan Mu / Ping Duhe / Yan Liben (traitors'
original names), Ye Gucheng. **B04:** the Honest Monk (老实和尚), Master Sun
(孙老爷; 龟孙子大老爷 → Turtle-Spawn Sun the Great Master), Ouyang Qing (欧阳情),
Datong / Dazhi (大通/大智, the two hermit oracles), Huo Tianqing (霍天青, Yan
Tieshan's steward). NOTE the two Yan surnames: 阎铁珊 (Yan Tieshan) and 严立本
(Yan Liben) both romanise as Yan — one man; the source uses 严立本 in ch06 where
Huo Tianqing's rescue is told. **Watch in B05:** the Shanxi Wild Goose (山西雁,
"the great hero of Guanzhong", named in ch05) will likely appear; 霍天青's own
scenes begin.

**Organisations:** Water Snake Gang, the Blue-Robe Tower (青衣楼 — 108 towers ×
108 men; head secretly Dugu Yihe), the Golden Roc (金鹏王朝, the fallen kingdom /
volume title). **B04:** the Ten Thousand Plum Manor (万梅山庄, Ximen Chuixue's
estate — moved to organizations/places), the Pavilion of Pearls and Splendour
(珠光宝气阁 / 阎府, Yan Tieshan's jewel seat — gives ch07 its title 珠光宝气).

**Places:** Jiangnan, the Nine Provinces, the Dragon-Soaring Inn, Huangshi
Town, the Yingchun Pavilion, the Green Cloud Inn, Guanzhong, the Central Lands,
Emei. **B04 (inline, not glossary unless noted):** Yanbei (燕北, footnoted),
Shanxi (山西), the Qilian Mountains (祁连山), the Shanglin Spring tavern (上林春),
the Yiqing Court (怡情院) and Xiaoxiang Court (潇湘院) brothels.

**Terms:** jianghu, lightness-skill (qinggong), guqin, sugar-roasted chestnuts,
living Bodhisattva, wangba, point-sealing (dianxue), judge's pens (panguan bi).
**B04:** Bamboo-Leaf Green (竹叶青, glossary + footnote), Flying Phoenix Needles
(飞凤针, Princess Danfeng's poisoned weapon), Huadiao wine (花雕, footnoted),
huaya / "mark" (花押, footnoted).

**Epithets / one-offs (footnote or inline, not glossary):** the Lightning
Blade, Jade Linked-Rings, Room Heaven, Peach Blossom Hall, Miss Nine, White
Cloud City / Flying-Immortal Isle / the Southern Sea, the Ten Thousand Plum
Manor, the Wooden Taoist (木道人) of Wudang, the Chan master Dabei (大悲禅师) of
Shaolin, Persian grape-wine, the Heartbreak Sword (断肠剑), chain-spear (练子枪),
man-flesh buns. **B04:** the Seven Swords of Emei / Three Heroes and Four
Beauties (峨嵋七剑, 三英四秀 — foreshadowed, will land in ch09), the Shanxi Wild
Goose (山西雁), Li Bai's 将进酒 "Bring in the Wine", Li Yu's 长相思 "Endless
Longing".

**Character-count idiom** (五个字 etc.) rendered with "words". **Money/units —
DECIDED:** keep period units (cash / catty / tael / li / cun / zhang) with
footnotes, book-wide, no domestication.

**authority.json** still holds no wuxia terms; feed decided renderings back on
completion (final batch).

## Where the book stands (story state)

- Prologue (ch01): four vignettes ending on Hua Manlou and Lu Xiaofeng, the man
  with four eyebrows.
- Chapter 1 (ch02): Lu evades the Blue-Robe Tower, humiliates the Four Heroes;
  three strange killers (Liu Yuhen, Xiao Qiuyu, Dugu Fang) appear; a girl in
  black kneels to Lu; he bolts through the roof.
- Chapter 2 (ch03): Lu flees to old Huo's hut; the three killers smash it;
  Xue'er announces Princess Danfeng; Lu's furniture-extortion exposes old Huo as
  Huo Xiu, the richest man; Lu boards the flower-carriage and rides to the King.
- Chapter 3 (ch04): the Great King's tale — the Golden Roc, overrun fifty years
  back; four ministers, one loyal (Shangguan Jin) and three turned traitor (now
  Yan Tieshan, Dugu Yihe, Huo Xiu). The King wants the treasure returned and
  the three to repent, not blood. A sugar-water toast reveals the family's
  hidden poverty; Lu accepts. He wants Ximen Chuixue, Zhu Ting, and Hua Manlou
  (who shatters Xiao Qiuyu's sword in a test Lu engineered). Shangguan Feiyan has
  vanished; Hua Manlou cares for her; Xue'er suspects murder.
- **Chapter 4 (ch05):** The feast. Lu sends for Zhu Ting by banknote-and-cipher.
  Night: Danfeng comes to his room but Xue'er has slipped in first as a prank;
  Danfeng, wounded, leaves. Morning: Lu and Hua go hunting the oracles Datong
  and Dazhi via the Honest Monk and Master Sun; the oracles confirm the Golden
  Roc's history but say there is NO WAY to move Ximen Chuixue. Then Xiao Qiuyu
  staggers in a dying blood-man, murdered, unable to speak; the Blue-Robe Tower
  has dumped Soul-Hook's hooks and a "Blood for blood / this is the end of those
  who meddle" warning. Lu, ox-stubborn, resolves to fetch Ximen and burn his
  Manor if refused.
- **Chapter 5 (ch06):** At the flowerless Ten Thousand Plum Manor, Ximen refuses
  to be begged or burned out — then agrees to come if Lu shaves his moustache,
  and Lu does. On the way home, a heartbreak song on the mountain: Hua Manlou
  knows the voice for Shangguan Feiyan's, but she vanishes, leaving hair in a
  basin. Behind the shrine's shattered god hangs Dugu Fang, murdered like Xiao.
  At a village tavern the drunk, grieving pair sing Li Bai and Li Yu; Xue'er
  arrives via a gulled hunter, shows a golden swallow she says fell from her
  dead sister's body, and accuses Princess Danfeng of killing Feiyan, Xiao,
  Dugu AND Liu Yuhen with her Flying Phoenix Needles. Then Liu Yuhen — supposedly
  dead — walks in alive and mild and takes Xue'er home in the King's carriage.
  Huo Tianqing's invitation to the Pavilion of Pearls and Splendour arrives.

## What is NEXT

- **B05 = ch07 (第六章 珠光宝气 Pearls and Splendour) + ch08 (第七章 市井七侠
  The Seven Heroes of the Marketplace)**. Lu enters Yan Tieshan's jewel world;
  Huo Tianqing's hospitality; the seven marketplace heroes.
- Then: B06 ch09-11, B07 ch12 (the ~31k climax 第六根足趾), B08 ch13 (coda) +
  back matter / reconciliation / completion.

## Traps / environment

- Stray-branch trap: each session starts on a stray per-task branch;
  consolidate onto claude/lu-xiaofeng-1 (rule 2) and delete the stray.
- ch2 onward: bare-numeric dividers (01, 02, ...) render as `***` scene breaks,
  NOT TOC sections; hand-inserted after split_bilingual (build_b04.py takes the
  after-paragraph indices). `apply_format_markers.py` finds nothing in this
  book's HTML.
- make_bilingual skip=2 every unit (line 1 running-title stub, line 2 chapter
  title). Confirm per unit.
- **Number check, tael 两**: 两 is both "two" and the tael measure word. Noise
  strips it after 十/百/千/万/多 (and the 五十两一锭 glue-case); a NEW amount
  pattern may need a new documented lookbehind. Never noise a real quantity.
- **Number check, idioms**: colour idioms (五色/五彩), direction idioms (四射/
  四顾), set four-char idioms (十足十/六亲不认/三七二十一/四平八稳/四分五裂),
  and lexical compounds (飘零) hide stray numerals; noise them (documented,
  longest-first) or render so the English carries the value.
- **Displacement in check_content**: a merged paragraph whose source names a
  character but whose English pushed the name elsewhere fails; restore the name
  in-place (B04 had 2).
- data/src and data/src_epub are gitignored (regenerate with ingest_epub.py);
  source.epub and data/figs (the cover) ARE tracked. The deliverable EPUB is
  gitignored and attached in chat each batch; force-commit it (`git add -f`)
  only on the FINAL batch.
- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar.
- English chapter titles in book.json are provisional; verify against the text
  as each chapter is done (ch03-ch06 titles confirmed: Princess Danfeng / The
  Great King of the Golden Roc / The Feast / A Song of Sorrow).
- Model may change mid-batch (this happened in B04: Fable 5 → Opus 4.8). Re-run
  check_register against the FROZEN ch01 ref after any switch and record it;
  B04 held within tolerance.
```
