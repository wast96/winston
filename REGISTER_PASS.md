# REGISTER_PASS.md — whole-book English register revision (the R-series)

This document is the complete operating instruction for revising the English
register of the finished translation, chapter by chapter, across ch02 to ch35.
It is written to be executed by two roles, which may be different models in
different sessions:

- **ANALYZE** reads a chapter closely against the source and produces a
  committed edit list.
- **EXECUTE** applies that edit list exactly, runs every check, rebuilds the
  EPUB, commits, and delivers.

ch00 and ch01 are already revised (commit `895d19c`) and are the register
exemplar. Before doing anything else, both roles MUST read:

1. `CLAUDE.md` (all standing rules still apply: one branch
   `claude/on-a-hair-trigger`, never invent or drop content, deliver the EPUB
   in chat every batch, no mid-batch pauses, no em dashes in prose written to
   the commissioner).
2. This file, in full.
3. The exemplar diff: `git show 895d19c`, and the finished `out/ch00_reading.md`
   and `out/ch01_reading.md`. That diff IS the register target; internalize the
   size and kind of its changes before writing or applying a single edit.

## What this pass is, and is not

The commissioner's finding, confirmed by inspection: the translation is
faithful but at many points keeps too much Chinese. Idioms are rendered
image-by-image (calques), the source's cinematic scene cards sit as broken
body copy, and some sentences carry transferred Chinese syntax that reads as
translationese. The fix is a STYLE-ONLY editing pass.

This pass is NOT a retranslation. Content is frozen: every clause of the
source survives, nothing is added, all names and terms keep their
`glossary.json` renderings, all footnotes stay. The annotate-don't-smooth rule
still governs CONTENT (a genuine ambiguity stays footnoted, never paraphrased
away); this pass changes only how already-faithful English reads.

## The register target

Fluent mid-century literary English for a 1930s Shanghai thriller: warm,
slightly formal narrative prose; period diction without archaism for its own
sake; dialogue that sounds spoken. The reader should never feel the Chinese
under the English. When in doubt, match the revised ch00/ch01.

## Failure taxonomy — what to fix, with real examples from this book

**T1. Chengyu and idiom calques.** An idiom rendered image-by-image where the
image does not land in English. Render the EFFECT. Keep a literal image only
when it genuinely works in English (per CLAUDE.md's idiom rule), and footnote
an idiom only when its flavor is lost and matters.

- 铺天盖地的红 "lay smothered under a red that covered heaven and earth"
  → "was drowned in wedding red from gate to rooftop."
- 迅雷不及掩耳 "quick as a thunderclap that leaves no time to cover the ears"
  → "before anyone could so much as react."
- 水落石出 "until the water sinks and the stones show through"
  → "until the whole truth is out."
- KEEP (already lands in English): 如鱼得水 "like a fish that has found
  water"; 李代桃僵 rendered vividly and footnoted in ch29. Do not churn these.

**T2. Scene cards.** The author writes cinematically. A paragraph whose source
is ONLY a place, date, time, or bare transition stamp is a scene card. Set it
in italics with `*...*` and phrase it naturally.

- Cards: 中国，上海。→ `*China. Shanghai.*` · 1910年，春。→ `*Spring, 1910.*` ·
  深夜。→ `*Deep in the night.*` · 三天后。→ `*Three days later.*` ·
  同一时刻。→ `*At the same moment.*`
- NOT cards (leave as roman prose): any stamp that reads as a narrative
  sentence with imagery, e.g. 华灯初上 "The bright lamps were just being lit."
- Dates inside cards read naturally: 宣统二年，1910年，初春。→
  `*Early spring, 1910 — the second year of the Xuantong reign.*`

**T3. Transferred syntax and over-literal images.** Chinese clause order or
imagery kept at the cost of English rhythm. Reshape freely WITHIN the
paragraph; merging or resequencing clauses inside one paragraph is allowed and
encouraged. Paragraph boundaries are inviolable (see constraints).

- "a lush green lawn spread its two graceful wings to gather in a courtyard
  of pear blossom" → "a green lawn curved like two graceful wings around a
  courtyard of pear blossom."
- 撇了撇嘴 "gave a twist of her lips" → "curled her lip."
- 鼻酸 "felt her own nose sting" → "felt the sting of tears rise."

**T4. Scare quotes.** The source uses 引号 far more liberally than English.
Rule: keep quotes that mark true irony, pretense, a nickname, or a cited term
at their FIRST occurrence in a scene; drop them on repetition once
established; never quote an ordinary idiom or emphasis. (Example: in the ch16
training exercise, keep the first "shot" and "wipe out" that establish the
game, drop the quotes on later repetitions within the same scene.)

**T5. Stiff dialogue.** Allow contractions in casual and intimate speech;
keep elevated diction for elevated speakers and formal moments (Old Madam
Rong, official interrogations, public declarations). Do not flatten register
differences BETWEEN characters; the servants and the matriarch must not sound
alike. Vary or un-invert "said X" tags where they cluster.

**T6. Punctuation tics.** Typography is already normalized book-wide (curly
quotes, typographic apostrophes, real ellipses, single !). Every edited line
MUST preserve this: curly `“ ” ‘ ’`, apostrophe `’`, ellipsis `…`, unspaced em
dashes in prose. Introducing a straight quote is a build-stopping regression
(the guard command below catches it). Multi-paragraph quotations keep the
convention: each continuing paragraph reopens `“`, only the final one closes.

## Triage discipline — do not churn

Per paragraph, exactly one verdict:

- **LEAVE** (expected: most paragraphs). Already natural. Fidelity to the
  existing good prose is part of the job; a rewrite that only shuffles
  synonyms is a defect in the edit list.
- **TOUCH** (common). One phrase swapped, a tag smoothed, quotes dropped.
- **RECAST** (rare; calque-dense or tangled). Rewrite the paragraph whole,
  against the source line directly above it in the bilingual file.

The ch00/ch01 exemplar calibrates: ch00 (a stylized cinematic prologue) was
RECAST nearly throughout; ch01 (ordinary narration) needed 9 targeted edits in
100 paragraphs. Ordinary chapters should look like ch01, not ch00.

## Hard constraints (violating any of these is a failed batch)

1. Edit ONLY the English lines of `out/<id>_bilingual.md`. NEVER touch a `>`
   source line, anything in `data/`, or `source.epub`.
2. Paragraph parity is 1:1 and inviolable: one English paragraph per source
   paragraph, no merging, no splitting, no dropping. `check_structure.py`
   enforces; run it, do not trust.
3. Nothing invented, nothing dropped. Every numeral survives
   (`check_numbers.py` enforces). If a de-calqued idiom legitimately loses a
   lexicalized numeral (e.g. 二丈金刚), add a commented row to
   `data/noise.txt` with the reason; never force the numeral in awkwardly and
   never silence a real quantity.
4. Note anchors in `notes.json` must remain verbatim substrings of the English
   prose. Before editing any paragraph, check the unit's anchors. If an edit
   must change anchor wording, the edit list carries a paired NOTE-ANCHOR item
   and EXECUTE updates `notes.json` in the same commit. The builder refuses to
   build on an unmatched anchor; that is the backstop, not the check.
5. Names and terms exactly per `glossary.json`. This pass never re-romanizes
   and never renames.
6. Source oddities that are footnoted stay as they are (the Tang Shaoli/Shaoqi
   slip, the Yang Muci/Muchu misprints, the Ronghua/Huamei bookstore
   inconsistency, watermark notes). Style pass, not story repair.
7. One branch: `claude/on-a-hair-trigger`. No new branches, no PRs.

## Phase A — ANALYZE (per chapter)

Input: `out/<id>_bilingual.md` (source `>` line with its English beneath),
`notes.json` (this unit's anchors), `glossary.json` as reference, and the
exemplar.

Read the chapter in FULL, English against source, and write the edit list to
`edits/<id>_edits.md`. Committed, so analysis and execution can run in
different sessions. Format, one block per edit, in paragraph order:

```
### p<NNN> [T1|T2|T3|T4|T5|T6] TOUCH|RECAST
OLD: <exact current English text: the full line for RECAST, or a substring
     that occurs EXACTLY ONCE in the file for TOUCH>
NEW: <replacement text, final typography>
WHY: <one line: the source phrase and what was wrong>
```

`p<NNN>` is the 1-based index of the paragraph among the file's `>` pairs.
If an edit affects a paragraph containing a note anchor and the anchor phrase
cannot survive verbatim, add immediately after that block:

```
NOTE-ANCHOR: OLD: <current anchor> NEW: <new anchor, verbatim substring of NEW>
```

End the file with a summary line:
`SUMMARY: <n> paragraphs, <n> leave, <n> touch, <n> recast`.

Analysis quality bar: every OLD must be copied exactly (not retyped); every
NEW must be checked against the source line for meaning drift before it is
written down; an edit that changes meaning is the worst possible output of
this pass.

## Phase B — EXECUTE (per batch)

For each chapter in the batch, in order:

1. Read `edits/<id>_edits.md` fully. Sanity-read each NEW against the source
   line in the bilingual file; if an edit would change meaning, drop material,
   or break a constraint, SKIP it and record the skip with a reason in
   `PROGRESS.md` (do not improvise a third wording).
2. Apply edits to `out/<id>_bilingual.md` programmatically with exact-match
   replacement asserting count == 1 per OLD (write via Python, not shell
   heredoc, per the CJK-mangling trap). Apply NOTE-ANCHOR items to
   `notes.json` in the same operation.
3. Regenerate and verify the chapter:
   ```
   python3 scripts/split_bilingual.py out/<id>_bilingual.md <id> "<zh_title from book.json>"
   python3 scripts/check_structure.py --pairs data/zh/<id>.txt out/<id>_reading.md
   python3 scripts/check_numbers.py out/<id>_bilingual.md --noise data/noise.txt
   grep -n "[\"']" out/<id>_reading.md        # typography guard: must print nothing
   ```
4. After all chapters in the batch:
   ```
   python3 scripts/build_reading_epub.py "out/On a Hair Trigger.epub"
   python3 scripts/qa_epub.py "out/On a Hair Trigger.epub"
   ```
   Both must be green. The builder refusing on an anchor means step 2 missed a
   NOTE-ANCHOR item; fix and rebuild, never delete a note to get past it.
5. Spot-audit: re-read 10% of edited paragraphs (minimum 10) against their
   source lines for meaning drift. Record the result in `PROGRESS.md`.
6. Record in `PROGRESS.md` (batch label, chapters, edit counts applied and
   skipped, checks run and results), append a dated entry to `CHANGELOG.md`,
   rewrite `HANDOFF.md`'s kickoff for the next batch, commit everything
   (including `edits/`), push to `claude/on-a-hair-trigger`.
7. Deliver `out/On a Hair Trigger.epub` in chat with a short summary, and end
   the reply with the next kickoff message verbatim in a fenced block.

Fresh-session note: `data/src` and `data/zh` are gitignored. If `data/zh` is
empty, regenerate it by running `scripts/split_bilingual.py` for every unit
(ids and zh titles from `book.json`) before running checks; if `data/src` is
needed, run `scripts/ingest_epub.py source.epub`.

## Batch plan

Twelve batches, labeled R01 to R12. A batch = ANALYZE then EXECUTE for its
chapters, end to end, no pause between phases unless the roles run in
separate sessions (in which case ANALYZE commits its edit lists and hands off).

| Batch | Chapters | Batch | Chapters |
|-------|----------|-------|----------|
| R01 | ch02 ch03 ch04 | R07 | ch18 ch19 ch20 |
| R02 | ch05 ch06 ch07 | R08 | ch21 ch22 ch23 |
| R03 | ch08 ch09 ch10 | R09 | ch24 ch25 ch26 |
| R04 | ch11 ch12 ch13 | R10 | ch27 ch28 ch29 |
| R05 | ch14 ch15 | R11 | ch30 ch31 ch32 |
| R06 | ch16 ch17 | R12 | ch33 ch34 ch35 |

Kickoff labels follow the house convention: first line `Hair Trigger R<nn>`.

## Definition of done (whole pass)

- All 34 chapters triaged with committed edit lists in `edits/`.
- All accepted edits applied; skips documented in `PROGRESS.md`.
- Book-wide after R12: parity OK and 0 unresolved numerals on all 36 units,
  `qa_epub` PASS, typography guard clean on all 36 reading files, and a final
  whole-book read-through of the EPUB's first and last pages of every chapter
  for register consistency.
- `CHANGELOG.md` carries one dated entry per batch; `COMPLETION.md` gains a
  paragraph recording the register pass.
- The finished EPUB delivered in chat.
