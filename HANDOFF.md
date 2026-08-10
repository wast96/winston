# HANDOFF — The Golden Roc Dynasty (陆小凤传奇·金鹏王朝, Gu Long)

This file is the baton. A fresh session with no memory reads it and starts
immediately. **It is the ARCHIVE of the kickoff message, not its delivery:
every batch ends with this file's kickoff block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count.** Rewrite it
at the end of every batch; always keep the paste-ready kickoff message below as
its first section. When the book completes, replace the kickoff with the
completion notice and do not touch it afterward (the Stop hook keys off it).

> **B01 ended at the first-chapter VOICE GATE (Step 0c). B02 does NOT begin
> until the commissioner has read the Prologue and approved the voice, note
> density, and formatting.** The block below is the B02 kickoff-in-waiting:
> paste it to start B02 ONLY after that approval. On approval, ch01 becomes the
> permanent frozen reference for `check_register.py --ref`.

## Message to paste into the next chat

```
Lu Xiaofeng 1 B02

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 金鹏王朝 (The Golden Roc Dynasty), Volume 1 of Gu Long's Legend of Lu Xiaofeng, from a digital source EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/lu-xiaofeng-1; expect the harness to start you on a stray per-task branch and consolidate per rule 2 (check out claude/lu-xiaofeng-1, reset to origin, and if a stray branch carries commits, fast-forward or cherry-pick them on, push, and delete the stray). Deliverable out/lu-xiaofeng-1.epub.

Run ./setup.sh first and record any failure in PROGRESS.md. NOTE: the checker regression harness reports 9/10 green with ONE expected failure ("hook stands down on template stub") — that case only passes while HANDOFF.md holds the template placeholder; now that HANDOFF carries a real kickoff the Stop hook correctly enforces, so that one test necessarily reads FAIL for the rest of the book. Not a defect; do not "fix" it. data/src and data/src_epub are gitignored and regenerable: if they are missing, run scripts/ingest_epub.py source.epub (do NOT overwrite book.json). This book has NO source-edition footnotes; re-grep this unit's source for \[\d+\] and record "none present" in PROGRESS.md.

ch01 (the Prologue) is the APPROVED FROZEN REFERENCE for register and PARAGRAPHING. Before translating, READ out/ch01_reading.md end to end and study HANDOFF's "Voice / house style", "Paragraphing", and voice sheets — the pages ARE the voice. Money/units are SETTLED: keep the period units (cash/catty/tael/li/cun/zhang) with footnotes, no domestication. Watch comma density (split clumsy comma runs; use em dashes only sparingly). Consult glossary.json and authority.json BEFORE romanizing anything (glossary.json holds the B01 shelf renderings; keep one rendering per referent).

Do Batch B02 = Chapter 1 (ch02, 第一章 有四条眉毛的人 / "The Man with Four Eyebrows"; ~10,407 source chars; text_file data/src/07_part0000-split-005.txt), end to end per the CLAUDE.md pipeline:
1. Read ch02 from its text_file. Fix extractor-split paragraphs (a line whose last char is not in 。！？"）…— continues the next). Chapters 1-12 divide themselves with BARE NUMERIC markers (01, 02, ...) that are scene breaks, NOT titled sections: recover them as *** (a *** line, not a paragraph) at the numeric-divider boundaries and record how in PROGRESS. ch02 has NO book.json sections, so its reading.md is one H1 + prose + *** breaks.
2. Translate to the frozen ch01 house style (HANDOFF "Voice / house style"): fluent, literary, image-forward, economical; recast freely for natural English; punch-lines on their own line; contractions measured; dialogue characterised; watch comma density; no invented substance. FOLLOW THE PARAGRAPHING RULE: MERGE adjacent narration into paragraphs by beat — do NOT render one source line per paragraph — keeping dialogue turns and punch-lines on their own. Lu Xiaofeng himself arrives here — write his voice sheet into HANDOFF at first speech. Never invent bridging text; render digitization glitches to plain sense and LIST each in PROGRESS.md; the source's own errors of fact stay visible and get a footnote. Verify the chapter's TAIL against the source before shipping.
3. Author out/ch02_en.json as MERGED English paragraphs, then build via the merged-source method (Paragraphing step 2): group the source lines, concatenate each group VERBATIM into out/ch02_src_merged.txt, run make_bilingual.py ch02 <merged_src> "Chapter 1. The Man with Four Eyebrows" out/ch02_en.json 2, insert the bare-numeric -> *** scene breaks, split_bilingual.py. Then verify_unit.py ch02 (parity + numbers with --noise data/noise.txt + anchors); check_align.py ch02; check_content.py --config <cfg>; qc_entities.py out/ch02_bilingual.md glossary.json. Add ch02 to a check config with docs/sources (copy the scratchpad qc_config from B01, or make one: {"docs":{"ch01":...,"ch02":...},"sources":{...},"notes":"notes.json","heading_depth":2}).
4. Footnotes per the reader model (Western reader, no Chinese background); first-appearance greps + a NOT-re-noted list; note density tapers from B01's 14 as the furniture is covered — expect fewer. Use apparatus_merge.py for NOTES (its glossary path adds rows FLAT and must NOT be used — add glossary rows under the two-level sections directly and validate with check_apparatus.py; see the do-not-revert note). check_apparatus.py clean.
5. Rebuild, qa_epub.py green, epubcheck (/tmp/epubcheck-5.1.0/epubcheck.jar) clean, check_register.py --ref out/ch01_reading.md out/ch02_reading.md within tolerance. Record every check in PROGRESS.md; update HANDOFF.md; commit and push to claude/lu-xiaofeng-1.
6. End the batch per CLAUDE.md: attach the rebuilt out/lu-xiaofeng-1.epub in the chat AND paste the B03 kickoff verbatim in the same reply.

Cite chapters and sections, never pages. Do not pause for approval mid-batch (B02 is a normal batch, no gate).
```

## What is DONE (do not redo)

- **Step 0 survey** (prior session): ingested the source, authored book.json
  (13 units), built the skeleton EPUB. Committed to claude/lu-xiaofeng-1.
- **B01 = the Prologue (ch01)** — COMPLETE, at the voice gate, REVISED TWICE on
  commissioner feedback (round 2: merge paragraphs; round 3: full literary
  re-render to the house style below). 4 vignette sections; **154 paragraphs**;
  14 footnotes; 21 glossary rows; 0 figures. Every check green (parity,
  numbers, align, content, entities, apparatus, structure, qa_epub, epubcheck
  0/0/0/0). ch01 is the intended FROZEN REGISTER REFERENCE (contractions
  **38.9/1k**, rhythm CV 0.78), pending the commissioner's re-read at the gate.
  Full detail in PROGRESS.md. **Money/units DECIDED: keep the period units
  (cash / catty / tael / li / cun / zhang) with footnotes, book-wide — no
  domestication.**

## Tooling in place (do NOT revert)

- `data/noise.txt`: `第二天` added (idiom "the next day/morning"; NOT the
  ordinal). Keep it. Do not noise 第一/第二 generally — ch01's plank pieces
  are legitimately "first/second piece".
- **glossary.json is TWO-LEVEL** (`section -> {zh: row}`), which is what the
  builder (`render_glossary`) and `qc_entities` require. `apparatus_merge.py`
  adds glossary rows FLAT at the top level, which BOTH of those consumers
  choke on. **So: use apparatus_merge.py for NOTES only; add glossary rows
  under the sections directly (Write tool, never a shell heredoc — that is the
  rule's real target) and validate with `check_apparatus.py`.** Do not "fix"
  by flattening the glossary.
- `scripts/check_content.py`: `name_map` skips `_`-prefixed / non-dict
  top-level glossary keys (it crashed on the string-valued `_about`). Matches
  the guard already in `qc_entities` and `render_glossary`. Keep it; the
  regression harness stays 9/10 (the 1 failure is the expected template-stub
  hook case, see below).
- **Regression harness**: `./setup.sh` reports "CHECKER REGRESSION TESTS
  FAILED", but it is 9/10 with ONE EXPECTED failure — `hook stands down on
  template stub`. That test asserts the Stop hook stays quiet against the
  current HANDOFF.md, which is only true while HANDOFF holds the template
  placeholder ("(First line: ..."). Now that HANDOFF carries a real kickoff,
  the hook correctly ENFORCES, so that one test necessarily fails for the rest
  of the book. Do not attempt to "fix" it; it is the guard working.

## Paragraphing (book-wide rule set at the voice gate — do NOT revert)

The commissioner rejected the first, 1:1 rendering (one source line = one
English paragraph) as too choppy. **From here on, MERGE adjacent narration
lines into paragraphs grouped by beat**; keep dialogue turns and deliberate
punch-lines on their own. Method that preserves the pipeline's guarantees:

1. Author `out/<id>_en.json` as the MERGED English paragraphs (one array
   entry per final paragraph, in reading order; section-title entries stay
   plain and become `### ` H3 in the H3 step).
2. Group the source body lines into the same paragraphs and build a MERGED
   source by concatenating each group's original lines VERBATIM (no re-typing
   — join with '' since every ch01 line ends on terminal punctuation; check
   this per unit). Run `make_bilingual.py <id> <merged_src> <title> en.json 2`
   so parity + verbatim stay true by construction, then the H3 step, then
   `split_bilingual.py`. (B01's generator is the pattern:
   scratchpad `regen_ch01.py` with a `RANGES` list of inclusive line spans;
   copy and re-range it per chapter. The merged-source file
   `out/<id>_src_merged.txt` is a throwaway, gitignored.)
3. All checks then run on the merged pairs exactly as before.

## Voice / house style (the register ch01 froze — match it exactly)

Set by the commissioner at the voice gate. The bar: it should read like a
**novel a good translator chose to publish in English**, not a crib of the
source. Project-agnostic; applies to every chapter.

- **Fluency over literalism.** Translate the meaning and the image, not the
  word order. Recast, reorder, resubordinate freely so each sentence lands as
  natural English. If a rendering smells of source grammar, tear the structure
  down and rebuild it. Dynamic equivalence, not calque.
- **Economy — the big one.** Cut pleonasm and limp connective tissue. Source
  prose often repeats or pads; English shouldn't. If an idea is doubled, say it
  once, well. Trim a weak simile rather than render it weakly. But NEVER cut
  plot, a name, a number, or a real image — lose the padding, keep the
  substance. When genuinely unsure, keep it.
- **Comma density / rhythm (watch this).** The reader is not anti-comma, but
  hates awkward pile-ups. Don't let one sentence carry a long train of commas
  that reads clumsily. Fixes, in order of preference: split into two sentences;
  drop a needless comma (e.g. before a coordinated verb: "he stumbled and
  pitched down", not "he stumbled, and pitched down"); recast to remove a
  parenthetical. Use an em dash ONLY when it genuinely beats a comma cluster,
  and sparingly — most sentences want none. Serial-list commas and one
  deliberate parenthetical aside are fine; it's the 4-, 5-, 6-comma runs that
  read like a speech, not prose. Read the sentence aloud; if you'd run out of
  breath, break it.
- **Image-forward diction.** Reach for the concrete, evocative phrase over the
  flat one. Exact, not purple. One vivid word beats three vague ones.
- **Rhythm.** Vary sentence length and opening. Follow a long, flowing sentence
  with a short flat one. A deliberate fragment or one-line paragraph is a tool
  — spend it on a beat that should land. Punch-lines get their own line; never
  bury them mid-paragraph.
- **Contractions, measured.** Use them for a living voice in BOTH narration and
  dialogue, but don't stuff them — three of the same contraction in one
  sentence reads worse than none. A couple of grave, uncontracted lines can be
  right for weight.
- **Paragraph by beat, not by sentence.** Group narration into paragraphs that
  hold one moment together; break at a shift of subject, place, or beat.
  Dialogue turns each get their own line.
- **Dialogue is characterised.** Each voice distinct (see the voice sheets). A
  small idiomatic touch that fits the speaker is welcome even if not literally
  in the source. Flavour only, never plot.
- **Names vs pronouns.** Name a character on a new beat or as an object; use a
  pronoun within a run. Do NOT re-state the name every line. (The name checks
  want the character's rendering once per paragraph it appears in, which merged
  paragraphs give you naturally — keep the FULL rendering there, since
  check_content matches the full glossary form.)
- **No invented substance.** Colour comes from diction and rhythm, never from
  facts, thoughts, or events the source doesn't have. Atmosphere is tone, not
  added narration.
- **Mechanics.** Italics via `*word*` in the en.json (builder renders `<i>`).
  Ellipsis `...` for a trailing voice, an em-dash cutoff (`pois—`) for speech
  cut off. Keep cultural nouns and the period units, footnoted (see the DONE
  line for the settled money/units call).

Read the frozen reference chapter (out/ch01_reading.md) end to end before
translating — the pages ARE the voice; this list only names what they do.

## Voice sheets (consult at every dialogue scene)

- **Ximen Chuixue** — near-silent, absolute, monosyllabic. Speaks only to
  state intent, never to explain or observe courtesy ("Kill you." / "Zhao
  Gang."; four words in the whole vignette). Treats killing as a sacred office
  and speech as waste. Cold, exact, white-robed.
- **Hua Manlou** — gentle, warm, unhurried; courteous even to a man trying to
  kill him. Short serene declaratives; dry understatement for a weapon ("I
  have no need of any more holes, big holes or small"). Open-hearted and
  entirely unself-pitying about his blindness; talks of snow-sound and
  flower-scent with real joy.
- **Granny Xiong** — grandmotherly, sing-song vendor patter over casual
  cruelty; flat candour when the mask drops ("Only that I felt like killing
  someone"); teasing ("Silly boy").
- **Shangguan Feiyan** — quick, bright, forthright, teasing; frank about being
  a thief ("I only ever steal from robbers"); girlish silver-bell laugh;
  curious, quick to warm.
- **Cui Yidong** — swaggering bully; third-person "老子" bluster and threats
  built on his One-Hole name; deflates instantly the moment real power appears.
- **Lu Xiaofeng** — NOT yet heard (only described: four eyebrows, two pairs of
  eyes/ears, three hands). Write his voice sheet in B02 at his first speech.

## Renderings settled this batch / carry-forward

- Pinyin, no tone marks. People: Lu Xiaofeng, Ximen Chuixue, Hua Manlou, Zhang
  Fang, **Granny Xiong** (熊姥姥; pinyin Xiong Laolao), Hong Tao, Zhao Gang,
  Cui Yidong, Shangguan Feiyan, and courtesans Xiaohong/Xiaocui/Xiaoyu/Xiaoyun.
- Orgs: **Water Snake Gang** (水蛇帮). Places: **Jiangnan** (江南), **the Nine
  Provinces** (九州). Terms: **jianghu** (江湖, kept romanized), **lightness-
  skill** (轻功/qinggong), **guqin** (古琴), **sugar-roasted chestnuts**,
  **living Bodhisattva** (活菩萨).
- Epithets (in footnotes, not glossary — one-offs): the Lightning Blade
  (闪电刀), "One Blade Quells the Nine Provinces" (一刀镇九州), Jade
  Linked-Rings (玉连环), the Flower-Blade Terror (花刀太岁; Taisui = "Terror").
- Character-count idiom 五个字/四个字/两个字 rendered with "words" (matches the
  English word counts in the Ximen exchange); note 10 tells the reader Chinese
  counts by character so "five words" for the 5-char 一刀镇九州 and 我是个瞎子
  ("I am a blind man", 5 words) reads true. 瞎子 -> "a blind man" (keeps the
  five-word tally). Carry this policy forward.
- authority.json holds no wuxia terms yet; feed the decided renderings back on
  completion (final batch).

## Where the book stands (story state)

- The Prologue is four self-contained vignettes, each introducing a figure of
  the jianghu: Granny Xiong the moon-mad poisoner (a threat, not yet tied to
  the plot); the "Honest Monk", a humble-seeming master who robs and then
  slaughters the Water Snake Gang; Ximen Chuixue, who rides a thousand li to
  avenge a stranger; and Hua Manlou, the blind, joyful swordsman, whose closing
  talk turns to his friend Lu Xiaofeng — the man with four eyebrows — which
  hands the reader straight into Chapter 1. No continuing plot thread yet; the
  prologue sets tone and dramatis personae.

## What is NEXT

- **B02 = Chapter 1 (ch02, 有四条眉毛的人)** once the voice is approved. Then
  the book.json plan: B03 ch2-3, B04 ch4-5, B05 ch6-7, B06 ch8-10, B07 ch11
  (the ~31k climax), B08 ch12 + back matter / reconciliation / completion.

## Traps / environment

- Stray-branch trap: each session starts on a stray per-task branch;
  consolidate onto claude/lu-xiaofeng-1 (rule 2) and delete the stray.
- ch2 onward: bare-numeric section dividers (01, 02, ...) render as `***`
  scene breaks, NOT TOC sections. The source is `<div class="calibre1">`
  prose; apply_format_markers may not find `kt`/Image00005/dateline markers
  (there are none), so scene breaks may need inserting by hand at the divider
  lines — record the method in PROGRESS.
- make_bilingual skip=2 for every unit (line 1 = running-title stub, line 2 =
  chapter title). Confirm per unit.
- data/src and data/src_epub are gitignored (regenerate with ingest_epub.py);
  source.epub and data/figs (the cover) ARE tracked.
- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetched it).
- English chapter titles in book.json are provisional; check against the
  translated text as each chapter is done.
