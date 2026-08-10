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
Lu Xiaofeng 1 B04

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 金鹏王朝 (The Golden Roc Dynasty), Volume 1 of Gu Long's Legend of Lu Xiaofeng, from a digital source EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/lu-xiaofeng-1; expect the harness to start you on a stray per-task branch and consolidate per rule 2 (check out claude/lu-xiaofeng-1, reset to origin, and if a stray branch carries commits, fast-forward or cherry-pick them on, push, and delete the stray). Deliverable out/lu-xiaofeng-1.epub.

Run ./setup.sh first and record any failure in PROGRESS.md. NOTE: the regression harness reports 9/10 green with ONE expected failure ("hook stands down on template stub") — that case only passes while HANDOFF.md holds the template placeholder; now that HANDOFF carries a real kickoff the Stop hook correctly enforces, so that one test necessarily reads FAIL for the rest of the book. Not a defect; do not "fix" it. data/src and data/src_epub are gitignored and regenerable: if they are missing, run scripts/ingest_epub.py source.epub (do NOT overwrite book.json). This book has NO source-edition footnotes; re-grep each unit's source for \[\d+\] and record "none present" per unit in PROGRESS.md.

ch01 remains the FROZEN REFERENCE for register and PARAGRAPHING. Before translating, READ out/ch03_reading.md (Princess Danfeng) AND out/ch04_reading.md (The Great King of the Golden Roc) end to end — those are the freshest voice, plus ch01/ch02 as needed. Study STYLE.md, HANDOFF's "Paragraphing", "Attribution", and the voice sheets (Lu Xiaofeng, Princess Danfeng, the Great King, Shangguan Xue'er, old Huo/Huo Xiu, and the three killers are all now written in HANDOFF). Money/units are SETTLED: keep the period units (cash / catty / tael / li / cun / zhang) with footnotes, no domestication. Watch comma density; em dashes sparingly; contractions measured. Consult glossary.json (now ~56 rows) and authority.json BEFORE romanizing anything.

Do Batch B04 = Chapters 4-5 (ch05 第四章 盛宴 "The Feast", ~9,797 chars, text_file data/src/10_part0000-split-008.txt; and ch06 第五章 悲歌 "A Song of Sorrow", ~7,898 chars, text_file data/src/11_part0000-split-009.txt), end to end per the CLAUDE.md pipeline:
1. Read each unit's source. Fix extractor-split paragraphs (a line whose last char is not in 。！？"）…— continues the next; B03 had none, but re-check per unit). Chapters 1-12 divide themselves with BARE NUMERIC markers (01, 02, ...) that are scene breaks: recover them as *** (copy scratchpad/build_b03.py, re-range the RANGES list and the two builder calls for ch05/ch06, exclude divider lines from the merged source and post-insert *** at the right paragraph boundaries). build_b03.py and scratchpad/qc_config.json are COMMITTED (in scratchpad/) — reuse them; if scratchpad is empty on a fresh container, they are in git under scratchpad/.
2. Translate to the frozen house style (read STYLE.md and the reading.md files): fluent, literary, image-forward, economical; MERGE narration into paragraphs by beat, keep dialogue turns and punch-lines on their own; recast freely; watch comma density. ATTRIBUTION RULE (load-bearing for the checks): every dialogue turn whose source names a capitalised-glossary character (Lu Xiaofeng, Princess Danfeng, Shangguan Xue'er, Xiao Qiuyu, Dugu Fang, Hua Manlou, Ximen Chuixue, the traitors, ...) MUST carry that full rendering once, via a natural "said X" attribution or an action beat — otherwise check_content, qc_entities, AND check_align all flag it. Lowercase-en names (the Great King, the Boss's Wife, old Huo) are exempt from check_content but qc_entities still wants the first/last word ("the"/"King") present. Never invent bridging text; render digitization glitches to plain sense and LIST each in PROGRESS.md; source errors of fact stay visible and get a footnote. Verify each chapter's TAIL against the source before shipping.
3. Author out/ch0N_en.json as MERGED English paragraphs; build via the merged-source method (build_b03.py pattern): make_bilingual.py ch0N <merged_src> "<chapter title>" out/ch0N_en.json 2, insert the bare-numeric -> *** scene breaks, split_bilingual.py. Then verify_unit.py ch0N (parity + numbers with --noise data/noise.txt + anchors); check_align.py ch0N; check_content.py --config scratchpad/qc_config.json (extend docs/sources to add ch05/ch06); qc_entities.py out/ch0N_bilingual.md glossary.json. WATCH THE NUMBER CHECK for tael 两 (五十两/一百多两 patterns are in noise; new amounts may need a new rule — see PROGRESS B03) and for colour/direction idioms (五色/五彩/四射/丑八怪 already noised).
4. Footnotes per the reader model (Western reader, no Chinese background); first-appearance greps + a NOT-re-noted list per unit; density keeps tapering (expect ~4-6/chapter). Use apparatus_merge.py for NOTES only (its glossary path adds rows FLAT and must NOT be used — add glossary rows under the two-level sections directly with Edit/Write and validate with check_apparatus.py). check_apparatus.py clean.
5. Rebuild, qa_epub.py green, epubcheck (/tmp/epubcheck-5.1.0/epubcheck.jar) clean, check_structure.py --config scratchpad/qc_config.json PASS, check_register.py --ref out/ch01_reading.md out/ch05_reading.md and out/ch06_reading.md within tolerance. Record every check in PROGRESS.md; update HANDOFF.md; commit and push to claude/lu-xiaofeng-1.
6. End the batch per CLAUDE.md: attach the rebuilt out/lu-xiaofeng-1.epub in the chat AND paste the B05 kickoff verbatim in the same reply.

Cite chapters and sections, never pages. Do not pause for approval mid-batch (B04 is a normal batch, no gate).
```

## What is DONE (do not redo)

- **Step 0 survey** (prior session): ingested the source, authored book.json
  (13 units), built the skeleton EPUB.
- **B01 = Prologue (ch01)** — COMPLETE, revised at the voice gate (rounds 2-5).
  4 vignettes; 154 paragraphs; 15 footnotes; 21 glossary rows. **ch01 is the
  FROZEN REGISTER REFERENCE** (contractions 40.3/1k, rhythm CV 0.75).
- **B02 = Chapter 1 (ch02, 有四条眉毛的人)** — COMPLETE. 289 merged paragraphs;
  11 footnotes; 20 glossary rows. Lu Xiaofeng arrives; the Blue-Robe Tower and
  the three strange killers.
- **B03 = Chapters 2-3 (ch03 丹凤公主 + ch04 大金鹏王)** — COMPLETE. ch03: 323
  merged paragraphs (3 scenes), 4 footnotes. ch04: 333 merged paragraphs (4
  scenes), 6 footnotes. 15 new glossary rows. Every check green: numbers 0
  unresolved, align no strays (median 3.81/3.88), content all-in-paragraph (252
  / 295 occurrences), qc_entities 0 misses, apparatus 0/0, structure ALL PASS,
  qa_epub PASS, epubcheck 5.1.0 0/0/0/0, register 27.3 (0.68x) / 23.2 (0.58x)
  within tolerance. **The princess is named (Princess Danfeng), the fallen
  kingdom of the Golden Roc and Lu's contract are established.**

## Tooling in place (do NOT revert)

- `scratchpad/build_b03.py` — the merged-paragraph builder (RANGES list per
  unit; writes merged source, make_bilingual, split_bilingual, post-inserts
  `***`). COMMITTED. Copy + re-range per new unit. `scratchpad/qc_config.json`
  — the check_content / check_structure config ({docs, sources, notes}); extend
  docs/sources for each new unit. COMMITTED.
- `data/noise.txt`: B01 (`第二天`), B02 (王八蛋/王八/三七二十一/十-shape/四顾/
  百炼/四平八稳/四分五裂/五彩缤纷/`(?<=[百千万萬])两`), **B03 additions**:
  `(?<=十)两一(?=锭)` then `(?<=十)两` then `(?<=多)两` (tael measure word:
  五十两→50, 五十两一锭→50, 一百多两→100 — ORDER load-bearing), `丑八怪`,
  `五色缤纷`/`五色`/`五彩`, `四射`. Each documented in-file; all justified by
  real flags. Keep.
- **glossary.json is TWO-LEVEL** (`section -> {zh: row}`). `apparatus_merge.py`
  adds glossary rows FLAT, which the builder/qc choke on. **Use apparatus_merge
  for NOTES only; add glossary rows under sections directly (Edit/Write) and
  validate with check_apparatus.py.** Strip any `glossary` block from the batch
  apparatus JSON before merging. (B03 did notes-only merges + manual glossary
  rows — works.)
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
   `split_bilingual.py`. (See `scratchpad/build_b03.py`; the RANGES list is a
   list of (start,end) source-line spans, dividers EXCLUDED.)
3. **Scene breaks** (ch02-ch12): the source's bare-numeric markers (01, 02, ...)
   are EXCLUDED from the merged source; `***` is post-inserted into
   `out/<id>_reading.md` after the paragraph that ends each scene (build_b03.py
   takes the list of after-paragraph indices).
4. All checks run on the merged pairs (`***` skipped everywhere).

## Attribution (load-bearing — do NOT drop)

Rapid dialogue must name its speaker or three checks fail at once
(`check_content` wants each capitalised glossary name in every paragraph its
source attributes to that character; `qc_entities` wants the first/last name-word;
bare interjections are `check_align` ratio outliers). **Give each dialogue turn
the character's full name once via a natural attribution ("said Lu Xiaofeng",
"Princess Danfeng smiled", "said the little girl") then let pronouns carry the
rest.** In a two-hander, tag one speaker consistently and vary the other with
action beats (matches the frozen ch02 Zhu Ting / Boss's-Wife exchange). B03
added ~73 such attributions. Lowercase-en names (the Great King, the Boss's
Wife, old Huo, the Iron-Faced Judge) are exempt from check_content but
qc_entities still needs their first/last word ("the"/"King") somewhere in the
paragraph — a line with no "the" in it (e.g. a bare "Mm.") will fail, so tag it.

## Voice / house style (the frozen register — match it exactly)

**`STYLE.md` (repo root) is the worked-example version — read it before
translating.** The bar: it should read like a novel a good translator chose to
publish in English. Fluency over literalism; economy (cut pleonasm, say a
doubled idea once); comma density watched (split, or drop a needless comma, em
dashes only when they beat a comma cluster and sparingly); image-forward,
concrete diction; vary rhythm, punch-lines on their own line; contractions
measured; paragraph by beat; dialogue characterised (voice sheets); names once
then pronouns; NO invented substance; keep cultural nouns and period units,
footnoted. Read the freshest reading.md files (ch03, ch04) end to end before
translating.

## Voice sheets (consult at every dialogue scene)

Prologue/ch02 cast (unchanged): **Ximen Chuixue** (near-silent, absolute,
monosyllabic; killing as sacred office), **Hua Manlou** (gentle, warm, unhurried;
serene declaratives, dry understatement; blind and joyful; feels danger ten li
off; in B03-B04 he is a guest of the Golden Roc and clearly smitten with the
vanished Shangguan Feiyan), **Granny Xiong**, **Shangguan Feiyan** (quick, bright,
teasing; a thief-girl; VANISHED at the top of ch04 — a live plot thread), **Lu
Xiaofeng** (the laziest man alive; wry, teasing, faintly filthy; sees everything;
shows power like an old beggar pinching a bedbug; won't rise from a bed or risk
his neck "for any friend" — then rides the carriage anyway; the red cape marks
him), **Zhu Ting** (cheerful, plump, philosophical tinkerer; "a chair that
bites"), **the Boss's Wife**, **Iron-Faced Judge** (dead), **Soul-Hook**
(tendons cut), **Liu Yuhen**, **Xiao Qiuyu**, **Dugu Fang**, **Little Beijing**.

**New in B03:**

- **Princess Danfeng** (丹凤公主) — soft, dreamy, gracious; a low, musical voice,
  "as though a whole garden of spring flowers had opened at once." Shrewd and
  self-aware beneath the courtesy: she reads Lu perfectly and names her own
  designs without shame ("Because I can no longer keep myself from beginning to
  tempt you"; "you're the most likeable scoundrel of the lot"). Grave dignity
  when she speaks of her father, the fallen kingdom, or the family's hidden
  poverty; tender candour at the end of ch04. Rarely raises her voice.
- **the Great King of the Golden Roc** (大金鹏王) — a fallen monarch's ceremonial,
  archaic register (this is the source of ch04's elevated "shall"; keep it, it
  is deliberate). His words carry the ring of command ("Young man, come here";
  "I will have them return the treasure…"). Swings between pride of name and
  blood, blazing hatred for the three traitors, and broken, weeping gratitude.
  Proud even in ruin: "the heirs of the Golden Roc have never yet used any man's
  need to force a friend's hand." Do not contract his speech freely.
- **Shangguan Xue'er** (上官雪儿) — a girl of twelve who "can lie without so much
  as a blink." Outwardly sweet, biddable, "as though she had never told half a
  lie in her life"; inwardly sly, precocious, needling (claims to be twenty, the
  princess's elder cousin, and leads Lu in circles). Cheeky banter ("Hey
  yourself, little cousin"), then abruptly grave and suspicious — she is hunting
  her vanished sister's corpse in the garden and suspects Hua Manlou and even
  the old King. Shangguan Feiyan's little sister.
- **old Huo / Huo Xiu** (霍休) — the richest man under heaven playing a cranky,
  reclusive hermit in a mountain hut. Dry, terse, deadpan, worldly; flat
  maxims and cynical wisdom ("how can a man give a treasure away? … once the
  treasures are broken wood, you can give them away"). Sips his wine unmoved
  while his hut is smashed; needles Lu about the hound that can outrun him. One
  of the three traitor-ministers (was Shangguan Mu); does not yet know he is
  found out.

## Renderings settled to date / carry-forward

**People:** Lu Xiaofeng, Ximen Chuixue, Hua Manlou, Zhang Fang, Granny Xiong,
Hong Tao, Zhao Gang, Cui Yidong, Shangguan Feiyan, Little Beijing, Zhu Ting,
the Boss's Wife, the Iron-Faced Judge, Soul-Hook, Liu Yuhen (formerly the
Jade-Faced Gentleman), Xiao Qiuyu (the Heartbreak Swordsman), Dugu Fang (the
Solitary Rider of a Thousand Li), the Four Heroes of Jiangdong. **B03:**
Princess Danfeng (丹凤公主, principal), the Great King of the Golden Roc (大金鹏王),
Huo Xiu (霍休, "old Huo"), Dugu Yihe (独孤一鹤 — NOT Dugu Fang), Yan Tieshan
(阎铁珊), Shangguan Xue'er (上官雪儿), Shangguan Jin (上官谨), the traitors'
original names Shangguan Mu / Ping Duhe / Yan Liben (上官木/平独鹤/严立本), Ye
Gucheng (叶孤城, the Lord of White Cloud City).

**Organisations:** Water Snake Gang, the Blue-Robe Tower (青衣楼 — 108 towers ×
108 men; its head is secretly Dugu Yihe). **B03:** the Golden Roc (金鹏王朝, the
fallen kingdom; the volume's title).

**Places:** Jiangnan, the Nine Provinces, the Dragon-Soaring Inn, Huangshi Town,
the Yingchun Pavilion, the Green Cloud Inn. **B03:** Guanzhong (关中), the Central
Lands (中土), Emei (峨嵋).

**Terms:** jianghu, lightness-skill (qinggong), guqin, sugar-roasted chestnuts,
living Bodhisattva, wangba, point-sealing (dianxue), judge's pens (panguan bi).

**Epithets / one-offs (footnote or inline, not glossary):** the Lightning Blade,
Jade Linked-Rings, Room Heaven, Peach Blossom Hall, Miss Nine. **B03:** the
Emei sword-sect, White Cloud City / Flying-Immortal Isle / the Southern Sea
(叶孤城's), the Ten Thousand Plum Manor (万梅山庄, Ximen Chuixue's), the Wooden
Taoist (木道人) of Wudang, the Chan master Dabei (大悲禅师) of Shaolin, Persian
grape-wine, the Heartbreak Sword (断肠剑), chain-spear (练子枪), man-flesh buns.

**Character-count idiom** (五个字 etc.) rendered with "words". **Money/units —
DECIDED:** keep period units (cash / catty / tael / li / cun / zhang) with
footnotes, book-wide, no domestication.

**authority.json** still holds no wuxia terms; feed decided renderings back on
completion (final batch).

## Where the book stands (story state)

- Prologue (ch01): four vignettes ending on Hua Manlou and his friend Lu
  Xiaofeng, the man with four eyebrows.
- Chapter 1 (ch02): Lu evades the Blue-Robe Tower's two enforcers, shields Zhu
  Ting, humiliates the Four Heroes of Jiangdong; the enforcers arrive; then
  three of the jianghu's strangest killers (Liu Yuhen, Xiao Qiuyu, Dugu Fang)
  turn up — Liu kills the Iron-Faced Judge, Xiao cuts Soul-Hook's tendons; a
  nameless girl in black kneels to Lu, and he bolts through the roof.
- **Chapter 2 (ch03):** Lu flees (wine-cup still in hand) to the mountain hut of
  "old Huo". The three killers — now revealed as the girl's bodyguards — smash
  the hut; the "little girl" (Shangguan Xue'er) announces her mistress, Princess
  Danfeng. Lu's mock-extortion over the "priceless" furniture forces Dugu Fang
  to name the richest man alive — Huo Xiu — and everyone sees old Huo IS Huo Xiu.
  Lu boards the princess's flower-decked carriage; learns Xue'er is twelve (she
  lied about being twenty) and is Shangguan Feiyan's little sister; rides to meet
  the Great King.
- **Chapter 3 (ch04):** The Great King tells his tale — the far kingdom of the
  Golden Roc, overrun fifty years ago by a greedy neighbour and Cossack cavalry;
  the old King split the treasury among four ministers to preserve the line. One
  (uncle Shangguan Jin) was loyal; three turned traitor and took new names:
  Yan Liben → Yan Tieshan (the Guanzhong jewel magnate), Ping Duhe → Dugu Yihe
  (Emei master AND secret head of the Blue-Robe Tower), Shangguan Mu → Huo Xiu
  (the richest man). The King wants justice, not blood: the treasure returned,
  and the three to repent before the old King's spirit-tablet. A sugar-water
  toast (poured for wine to spare the King's swollen legs) shows Lu the family's
  hidden poverty; that, and not being coerced, moves him to accept. He wants
  Ximen Chuixue, Zhu Ting (to fortify the mansion), and Hua Manlou — who, in a
  test Lu engineered, catches and shatters Xiao Qiuyu's Heartbreak Sword.
  Meanwhile Shangguan Feiyan has vanished (Hua Manlou plainly cares for her);
  Xue'er suspects murder. Lu and Hua close the chapter joking about man-flesh
  buns and soul-stealing wine.

## What is NEXT

- **B04 = ch05 (第四章 盛宴 The Feast) + ch06 (第五章 悲歌 A Song of Sorrow)**.
- Then: B05 ch07-08, B06 ch09-11, B07 ch12 (the ~31k climax), B08 ch13 (coda) +
  back matter / reconciliation / completion.

## Traps / environment

- Stray-branch trap: each session starts on a stray per-task branch;
  consolidate onto claude/lu-xiaofeng-1 (rule 2) and delete the stray.
- ch2 onward: bare-numeric dividers (01, 02, ...) render as `***` scene breaks,
  NOT TOC sections; hand-inserted after split_bilingual (build_b03.py takes the
  after-paragraph indices). `apply_format_markers.py` finds nothing in this
  book's HTML.
- make_bilingual skip=2 every unit (line 1 running-title stub, line 2 chapter
  title). Confirm per unit.
- **Number check, tael 两**: 两 is both "two" and the tael measure word. Noise
  strips it after 十/百/千/万/多 (and the 五十两一锭 glue-case); a NEW amount
  pattern (e.g. 两 after a bare units-digit) may parse wrong and need a new,
  documented lookbehind rule. Never noise a real quantity; fix the English to
  carry it.
- **Number check, idioms**: colour idioms (五色/五彩/五彩缤纷), direction idioms
  (四射/四顾/四面…), and set four-char idioms hide stray numerals; noise them
  (documented, longest-first) or render so the English carries the value.
- data/src and data/src_epub are gitignored (regenerate with ingest_epub.py);
  source.epub and data/figs (the cover) ARE tracked. The deliverable EPUB is
  gitignored and attached in chat each batch; force-commit it (`git add -f`)
  only on the FINAL batch.
- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar.
- English chapter titles in book.json are provisional; verify against the
  translated text as each chapter is done (ch03 "Princess Danfeng" and ch04
  "The Great King of the Golden Roc" confirmed).
```
