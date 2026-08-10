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
Lu Xiaofeng 1 B03

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 金鹏王朝 (The Golden Roc Dynasty), Volume 1 of Gu Long's Legend of Lu Xiaofeng, from a digital source EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/lu-xiaofeng-1; expect the harness to start you on a stray per-task branch and consolidate per rule 2 (check out claude/lu-xiaofeng-1, reset to origin, and if a stray branch carries commits, fast-forward or cherry-pick them on, push, and delete the stray). Deliverable out/lu-xiaofeng-1.epub.

Run ./setup.sh first and record any failure in PROGRESS.md. NOTE: the regression harness reports 9/10 green with ONE expected failure ("hook stands down on template stub") — that case only passes while HANDOFF.md holds the template placeholder; now that HANDOFF carries a real kickoff the Stop hook correctly enforces, so that one test necessarily reads FAIL for the rest of the book. Not a defect; do not "fix" it. data/src and data/src_epub are gitignored and regenerable: if they are missing, run scripts/ingest_epub.py source.epub (do NOT overwrite book.json). This book has NO source-edition footnotes; re-grep each unit's source for \[\d+\] and record "none present" per unit in PROGRESS.md.

ch01 remains the FROZEN REFERENCE for register and PARAGRAPHING. Before translating, READ out/ch01_reading.md (Prologue) AND out/ch02_reading.md (Chapter 1) end to end — the pages ARE the voice. Study STYLE.md, HANDOFF's "Paragraphing" and voice sheets (Lu Xiaofeng's own voice sheet is now written in HANDOFF from B02). Money/units are SETTLED: keep the period units (cash / catty / tael / li / cun / zhang) with footnotes, no domestication. Watch comma density; em dashes sparingly; contractions measured. Consult glossary.json and authority.json BEFORE romanizing anything (glossary.json now holds ~41 rows through B02).

Do Batch B03 = Chapters 2-3 (ch03 第二章 丹凤公主 "Princess Danfeng", ~7,656 chars, text_file data/src/08_part0000-split-006.txt; and ch04 第三章 大金鹏王 "The Great King of the Golden Roc", ~8,931 chars, text_file data/src/09_part0000-split-007.txt), end to end per the CLAUDE.md pipeline:
1. Read each unit's source. Fix extractor-split paragraphs (a line whose last char is not in 。！？"）…— continues the next; ch02 had zero, but re-check per unit). Chapters 1-12 divide themselves with BARE NUMERIC markers (01, 02, ...) that are scene breaks: recover them as *** (see B02's method — copy scratchpad/build_ch02.py, re-range for each new unit, exclude divider lines from the merged source and post-insert *** into the reading.md at the right paragraph boundaries).
2. Translate to the frozen ch01/ch02 house style (read STYLE.md and the two frozen chapters): fluent, literary, image-forward, economical; MERGE narration into paragraphs by beat, keep dialogue turns and punch-lines on their own; recast freely for natural English; watch comma density. New characters: Princess Danfeng (丹凤公主 — she is the "girl in black" who knelt to Lu at ch02's close, now named) and the Great King of the Golden Roc (大金鹏王 — the fallen king whose story anchors the volume). Write voice sheets into HANDOFF at first speech. Never invent bridging text; render digitization glitches to plain sense and LIST each in PROGRESS.md; the source's own errors of fact stay visible and get a footnote. Verify each chapter's TAIL against the source before shipping.
3. Author out/ch0N_en.json as MERGED English paragraphs, then build via the merged-source method (copy scratchpad/build_ch02.py, re-range per unit): make_bilingual.py ch0N <merged_src> "<chapter title>" out/ch0N_en.json 2, insert the bare-numeric -> *** scene breaks, split_bilingual.py. Then verify_unit.py ch0N (parity + numbers with --noise data/noise.txt + anchors); check_align.py ch0N; check_content.py --config <cfg>; qc_entities.py out/ch0N_bilingual.md glossary.json. Extend the qc_config to include ch03 and ch04 (copy scratchpad/qc_config.json from B02).
4. Footnotes per the reader model (Western reader, no Chinese background); first-appearance greps + a NOT-re-noted list per unit; note density continues to taper as furniture is covered — expect fewer per chapter than in B02. Use apparatus_merge.py for NOTES (its glossary path adds rows FLAT and must NOT be used — add glossary rows under the two-level sections directly and validate with check_apparatus.py; see the do-not-revert note). check_apparatus.py clean.
5. Rebuild, qa_epub.py green, epubcheck (/tmp/epubcheck-5.1.0/epubcheck.jar) clean, check_register.py --ref out/ch01_reading.md out/ch03_reading.md and out/ch04_reading.md within tolerance. Record every check in PROGRESS.md; update HANDOFF.md; commit and push to claude/lu-xiaofeng-1.
6. End the batch per CLAUDE.md: attach the rebuilt out/lu-xiaofeng-1.epub in the chat AND paste the B04 kickoff verbatim in the same reply.

Cite chapters and sections, never pages. Do not pause for approval mid-batch (B03 is a normal batch, no gate).
```

## What is DONE (do not redo)

- **Step 0 survey** (prior session): ingested the source, authored book.json
  (13 units), built the skeleton EPUB. Committed to claude/lu-xiaofeng-1.
- **B01 = Prologue (ch01)** — COMPLETE, at the voice gate, REVISED rounds 2-5.
  4 vignette sections; 154 paragraphs; 15 footnotes; 21 glossary rows; 0
  figures. Every check green. **ch01 is the FROZEN REGISTER REFERENCE**
  (contractions 40.3/1k, rhythm CV 0.75).
- **B02 = Chapter 1 (ch02, 有四条眉毛的人)** — COMPLETE. 289 merged paragraphs
  from 370 source body lines (6 scenes divided by bare-numeric markers).
  11 new footnotes (density down from B01's 15, as expected); 20 new glossary
  rows (10 people, 1 org, 4 places, 3 terms + 2 principal/cast). All checks
  green (numbers 0 unresolved, align OK median 3.75 en/han, content 143 name
  occurrences all placed, qc_entities 0 misses, apparatus 0/0, structure PASS,
  qa_epub PASS, epubcheck 5.1.0 0/0/0/0, register 29.5/1k CV 0.77 within
  tolerance). **Lu Xiaofeng arrives; his voice sheet is now written below.**

## Tooling in place (do NOT revert)

- `data/noise.txt`: B01 additions (`第二天`); B02 additions (王八蛋, 王八,
  三七二十一, `[「"]十[」"]`, 四分五裂, 五彩缤纷, 四顾, 百炼, 四平八稳,
  `(?<=[百千万萬])两` — measure-word disambiguator for tael). Each entry
  documented in the file's comments; all justified by real ch02 flags. Keep.
- **glossary.json is TWO-LEVEL** (`section -> {zh: row}`), which is what the
  builder (`render_glossary`) and `qc_entities` require. `apparatus_merge.py`
  adds glossary rows FLAT at the top level, which BOTH of those consumers
  choke on. **So: use apparatus_merge.py for NOTES only; add glossary rows
  under the sections directly (Write tool, never a shell heredoc — that is the
  rule's real target) and validate with `check_apparatus.py`.** Do not "fix"
  by flattening the glossary. CONCRETE TRAP (hit twice): if the batch
  apparatus JSON you pass to `apparatus_merge.py` still contains a `"glossary"`
  block, the merge re-adds those rows FLAT every time. Strip the `glossary`
  block from the apparatus JSON before merging (B02 did notes-only merges and
  the manual glossary-rows-in-sections approach — it works). NOTES-only merges
  are safe.
- `scripts/check_content.py` (B01): `name_map` skips `_`-prefixed / non-dict
  top-level glossary keys. (B02): `paragraphs()` now skips `***` scene-break
  markers — without it, a target with scene breaks slips one pair off the
  source per break. Keep both.
- `scripts/check_align.py` (B02): `paras()` now skips `***` scene-break
  markers. Same reason as above.
- `scripts/check_numbers.py` (B02): `spelled_numbers` now recognises
  "N hundred and M" and "a hundred and M" for bare ones-digit M. Needed for
  "one hundred and eight" (Blue-Robe Tower) → 108. Additive change; the
  check_numbers regression fixtures still pass 5/5.
- **Regression harness**: `./setup.sh` reports "CHECKER REGRESSION TESTS
  FAILED", but 9/10 with ONE EXPECTED failure (`hook stands down on template
  stub`). Not a defect; the hook correctly ENFORCES against the live HANDOFF.

## Paragraphing (book-wide rule set at the voice gate — do NOT revert)

The commissioner rejected the first, 1:1 rendering (one source line = one
English paragraph) as too choppy. **From here on, MERGE adjacent narration
lines into paragraphs grouped by beat**; keep dialogue turns and deliberate
punch-lines on their own. Method that preserves the pipeline's guarantees:

1. Author `out/<id>_en.json` as the MERGED English paragraphs (one array
   entry per final paragraph, in reading order; section-title entries stay
   plain and become `### ` H3 in the H3 step — ch01 only; ch02+ chapters
   have no book.json sections).
2. Group the source body lines into the same paragraphs and build a MERGED
   source by concatenating each group's original lines VERBATIM (no re-typing
   — join with '' since every body line ends on terminal punctuation; check
   this per unit). Run `make_bilingual.py <id> <merged_src> <title> en.json 2`
   so parity + verbatim stay true by construction, then `split_bilingual.py`.
   (B01's generator was `regen_ch01.py`; B02's is `scratchpad/build_ch02.py`.
   Copy and re-range it per chapter. The merged-source file
   `out/<id>_src_merged.txt` is a throwaway, gitignored.)
3. **Scene breaks** in ch02-ch12: the source's bare-numeric markers (01, 02,
   ...) are EXCLUDED from the merged source (they aren't paragraphs), and
   `***` is post-inserted into `out/<id>_reading.md` after `split_bilingual`
   at the paragraph boundaries corresponding to those source lines. B02's
   `build_ch02.py` prints the correct paragraph-numbers-to-insert-after; the
   post-insert is a tiny Python one-liner (see the batch's history).
4. All checks then run on the merged pairs. `check_align.py`,
   `check_content.py`, `verify_unit.py`, and `check_structure.py` all now
   skip `***` correctly.

## Voice / house style (the register ch01+ch02 freeze — match it exactly)

Set by the commissioner at the voice gate and held through B02. The bar: it
should read like a **novel a good translator chose to publish in English**,
not a crib of the source. Project-agnostic; applies to every chapter.
**`STYLE.md` (repo root) is the in-depth, worked-example version — read it
before translating; this is the compact companion.**

- **Fluency over literalism.** Translate the meaning and the image, not the
  word order. Recast, reorder, resubordinate freely so each sentence lands as
  natural English. Dynamic equivalence, not calque.
- **Economy — the big one.** Cut pleonasm and limp connective tissue. Say a
  doubled idea once, well. Trim a weak simile rather than render it weakly.
  But NEVER cut plot, a name, a number, or a real image — lose padding, keep
  substance. When genuinely unsure, keep it.
- **Comma density / rhythm.** Not anti-comma; but avoid clumsy 4-, 5-, 6-comma
  pile-ups. Fixes, in order: split into two sentences; drop a needless comma
  (e.g. before a coordinated verb); recast to remove a parenthetical. Em
  dashes ONLY when they beat a comma cluster, and sparingly.
- **Image-forward diction.** Concrete, exact, never purple.
- **Rhythm.** Vary length; punch-lines on their own line.
- **Contractions, measured.** Living voice in both narration and dialogue,
  but never stuffed.
- **Paragraph by beat, not by sentence.** Dialogue turns each get their own
  line.
- **Dialogue is characterised.** Each voice distinct (see voice sheets). A
  small idiomatic touch that fits the speaker is welcome even if not literally
  in the source. Flavour only, never plot.
- **Names vs pronouns.** Name a character on a new beat or as an object; use
  a pronoun within a run. Keep the FULL glossary rendering in each paragraph
  that names the character (the name checks want the character's full name
  once per paragraph they appear in). B02 pattern: add short attributions
  ("said Zhu Ting", "said the Boss's Wife", "said the Iron-Faced Judge") to
  short dialogue turns — it satisfies check_content and reads natural for a
  banter chapter.
- **No invented substance.** Colour comes from diction and rhythm, never from
  facts, thoughts, or events the source doesn't have.
- **Mechanics.** Italics `*word*`; ellipsis `...`; em-dash cutoff (`pois—`);
  keep cultural nouns and the period units, footnoted (see the DONE line on
  money/units).

Read the frozen chapters (out/ch01_reading.md, out/ch02_reading.md) end to
end before translating.

## Voice sheets (consult at every dialogue scene)

- **Ximen Chuixue** — near-silent, absolute, monosyllabic. Speaks only to
  state intent; treats killing as a sacred office and speech as waste. Cold,
  exact, white-robed. (Prologue only, so far.)
- **Hua Manlou** — gentle, warm, unhurried; courteous even to a would-be
  killer. Short serene declaratives; dry understatement for a weapon. (Prologue.)
- **Granny Xiong** — grandmotherly sing-song vendor patter over casual
  cruelty; flat candour when the mask drops. (Prologue.)
- **Shangguan Feiyan** — quick, bright, forthright, teasing; girlish
  silver-bell laugh. (Prologue.)
- **Cui Yidong** — swaggering bully, deflates instantly before real power.
  (Prologue.)
- **Lu Xiaofeng** (B02) — **the LAZIEST man alive.** Lies flat on a bed with a
  full cup of wine on his chest and breathes it up and back by lung-craft.
  Does not sit up for the Blue-Robe Tower's two Great Enforcers crashing
  through his window, does not sit up when three of the strangest killers of
  the jianghu converge on his room. Wry, teasing, faintly filthy: shows his
  power the way an old beggar pinches a bedbug. His humour is dry, ironic,
  self-aware; his kindness — for Zhu Ting the plump tinkerer, his childhood
  friend — is disguised as elaborate flirtation with Zhu Ting's wife. Coarse
  when it suits him ("live wangba", "dead wangba"). Signature: closed eyes,
  half-mumbled reply, then a stroke of impossible skill without visibly
  moving. His trademark red cape is never worn on-page in ch02 — just hangs
  on the stand by his bed — but it is the mark of him for anyone who spots it.
  Contractions natural; never grandiose; sees everything.
- **Zhu Ting** (B02) — cheerful, plump, philosophical, easygoing.
  Wry equanimity; talks like a self-mocking gourmand. Rarely raises voice;
  cracks jokes at his own expense; deeply loyal to Lu Xiaofeng under the
  banter. "A child needs to pee, a wife wants to stray — nobody has ever
  stopped either one" is the shape of his sentences.
- **the Boss's Wife** (B02) — saucy, quick-tempered, spirited; domestic
  banter with hips on hands. Slang, expressive. Not a fool; sees through the
  play Lu is running with her but goes along for the sake of her husband.
- **Iron-Faced Judge** (B02) — Blue-Robe Tower enforcer; formal officialese
  with menace; laughs often, and the scar twists when he does, "worse than
  any evil spirit painted on the wall of some derelict temple." Bit of a
  bully; slips into "shall" and courtly diction with a man he wants to
  handle carefully.
- **Soul-Hook** (B02) — Iron-Faced Judge's partner; less voluble, more
  practical. Sneers when cornered.
- **Liu Yuhen** (B02) — wounded, half-faced, hook-and-ball-handed; brooding
  poetic despair; quotes classical verse when he speaks at all. Very few
  lines; each one weighs.
- **Xiao Qiuyu** (B02) — the Heartbreak Swordsman. Refined, scholarly,
  ever-smiling; speaks softly and kills as it pleases him. Melancholy
  turn of phrase, blade-sharp eye.
- **Dugu Fang** (B02) — terse, deadpan. "I don't kill wild dogs. I watch
  other men kill." Ritual jokes (the door-knocking business) at his own
  expense.
- **Little Beijing** (B02) — cheeky, servile-outward, sly-inward inn waiter,
  in the Blue-Robe Tower's pay; treats himself to the naked bait-courtesan
  once his masters ride off. One-liner voice.
- **The Princess in black** (B02, unnamed here) — silent almost to the point
  of ceremony; when she speaks it is a soft, dreamy line. Ethereal, elegant,
  mysterious; kneels to Lu, receives his flight through the roof with grave
  approval. **Named in B03 as 丹凤公主 (Princess Danfeng); the reader will
  meet her as the girl who knelt to Lu at ch02's close.** Write her voice
  sheet at first speech in B03.

## Renderings settled to date / carry-forward

**People (pinyin, no tone marks):** Lu Xiaofeng, Ximen Chuixue, Hua Manlou,
Zhang Fang, **Granny Xiong** (熊姥姥; pinyin Xiong Laolao), Hong Tao,
Zhao Gang, Cui Yidong, Shangguan Feiyan, Xiaohong / Xiaocui / Xiaoyu /
Xiaoyun. **B02 additions:** Little Beijing (小北京), Zhu Ting (朱停; principal,
"the Boss"), the Boss's Wife (老板娘 — the only address she ever gets),
the Iron-Faced Judge (铁面判官), Soul-Hook (勾魂手), Liu Yuhen (柳余恨,
formerly the Jade-Faced Gentleman 玉面郎君), Xiao Qiuyu (萧秋雨, the
Heartbreak Swordsman 断肠剑客), Dugu Fang (独孤方, the Solitary Rider of a
Thousand Li 千里独行), and the group name the Four Heroes of Jiangdong
(江东四杰).

**Organisations:** Water Snake Gang (水蛇帮); **B02:** the Blue-Robe Tower
(青衣楼) — 108 towers × 108 men.

**Places:** Jiangnan (江南), the Nine Provinces (九州); **B02:** the
Dragon-Soaring Inn (龙翔客栈), Huangshi Town (黄石镇), the Yingchun
Pavilion (迎春阁), the Green Cloud Inn (青云客栈).

**Terms:** jianghu (江湖, romanised), lightness-skill (轻功/qinggong), guqin
(古琴), sugar-roasted chestnuts (糖炒栗子), living Bodhisattva (活菩萨);
**B02:** wangba (王八, romanised — the whole ch02 running joke turns on the
word; footnoted at first appearance), point-sealing (点穴/dianxue),
judge's pens (判官笔 — the panguan-clerk's brush-shaped iron weapons).

**Epithets (footnotes, not glossary; one-offs):** the Lightning Blade (闪电刀),
"One Blade Quells the Nine Provinces" (一刀镇九州), Jade Linked-Rings (玉连环),
the Flower-Blade Terror (花刀太岁), Room Heaven (天字号房). **B02 further:**
Peach Blossom Hall (桃花厅) — the room in the Yingchun Pavilion. Miss Nine
(九姑娘) — the bait courtesan; a numbering address, not a name.

**Character-count idiom** (五个字/四个字/两个字) rendered with "words" (see
ch01's Ximen Chuixue vignette and ch01's note 10). Continue this policy.

**Money / units — DECIDED:** keep the period units (cash / catty / tael / li
/ cun / zhang) with their footnotes, book-wide. No domestication.

**authority.json** still holds no wuxia terms; feed the decided renderings
back on completion (final batch).

## Where the book stands (story state)

- The Prologue (ch01) is four self-contained vignettes: Granny Xiong the
  moon-mad poisoner, the "Honest Monk" who robs and slaughters the Water
  Snake Gang, Ximen Chuixue who rides a thousand li to avenge a stranger,
  and Hua Manlou the blind joyful swordsman — whose closing talk turns to
  his friend Lu Xiaofeng, the man with four eyebrows.
- **Chapter 1 (ch02) puts the pieces on the board.** Two Blue-Robe Tower
  enforcers (Iron-Faced Judge, Soul-Hook) chase Lu Xiaofeng north on their
  boss's orders. He evades them at the Dragon-Soaring Inn (leaves a naked
  decoy tied to a rafter), then humiliates the "Four Heroes of Jiangdong" at
  a brothel in Huangshi Town and sends the two thugs on to the Boss's Wife
  as a riddle. Zhu Ting the plump inventor — Lu's childhood friend — comes
  on stage and takes the visit with wry equanimity. Meanwhile Lu lies on a
  bed at the Green Cloud Inn with a cup of wine on his chest, needling the
  Boss's Wife into carrying his plan (an ostensible affair, meant to keep
  Zhu Ting alive by making his death cost the Tower a bloody scandal). The
  two enforcers arrive; Lu pinches Soul-Hook's whip between two fingers,
  warns them off Zhu Ting, and threatens to burn the Tower's 108 buildings
  to ash. Before he can send them home, three of the jianghu's strangest
  killers turn up in his room: the ruined Liu Yuhen, the smiling Xiao
  Qiuyu, the elusive Dugu Fang. Liu Yuhen kills the Iron-Faced Judge on
  the spot; Xiao Qiuyu cuts Soul-Hook's tendons and sends him home with a
  two-month warning. Then, on the evening wind, music and a rain of flowers
  — a nameless girl in pure black silk walks in and kneels to Lu Xiaofeng.
  He crashes through the roof to get away. She calls him "very, very
  clever." (She is Princess Danfeng of the Golden Roc, whom B03 names.)

## What is NEXT

- **B03 = ch03 (第二章 丹凤公主) + ch04 (第三章 大金鹏王)**. The Princess
  in black is named and speaks; the fallen kingdom of the Golden Roc, the
  vengeance-motive, and Lu Xiaofeng's contract are established.
- Then the book.json plan: B04 ch4-5 (ch05, ch06), B05 ch6-7 (ch07, ch08),
  B06 ch8-10 (ch09, ch10, ch11), B07 ch11 (ch12, the ~31k climax), B08 ch12
  (ch13, the coda) + back matter / reconciliation / completion.

## Traps / environment

- Stray-branch trap: each session starts on a stray per-task branch;
  consolidate onto claude/lu-xiaofeng-1 (rule 2) and delete the stray.
- ch2 onward: bare-numeric section dividers (01, 02, ...) render as `***`
  scene breaks, NOT TOC sections. `apply_format_markers.py` does not find
  markers in this book's HTML (there are none), so `***` is inserted BY HAND
  after `split_bilingual.py` at the paragraph boundaries that correspond to
  the source's divider lines. See B02's `build_ch02.py` + one-liner Python
  post-insert. Also see the tooling do-not-revert list for the `***` skip
  patches to check_align / check_content / verify_unit.
- make_bilingual skip=2 for every unit (line 1 = running-title stub, line 2 =
  chapter title). Confirm per unit.
- data/src and data/src_epub are gitignored (regenerate with ingest_epub.py);
  source.epub and data/figs (the cover) ARE tracked.
- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetched it).
- English chapter titles in book.json are provisional; verify against the
  translated text as each chapter is done.
- **Attribution vs qc_entities / check_content:** these checks require the
  character's full glossary rendering (or first/last word, for qc_entities)
  in every paragraph where the source names the character. For B02 that
  meant adding short "said X" attributions to about 30 short dialogue turns
  where the source's `<Name>道` had been dropped in English. That WAS the
  correct fix for this chapter's banter, and it also lifted the check_align
  ratios into range. Continue this pattern: give each dialogue turn the
  character's full name once (via a natural attribution), then let pronouns
  carry the rest of the paragraph.
