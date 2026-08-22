# REVISION_PLAN.md — voice/register pass over *China's Secret War*

Commissioner-ordered whole-book voice/register/style pass (2026-08-22),
adapting the shelf's register-rebaseline learnings (imported into
`STYLE.local.md`, "THE REGISTER REBASELINE") to this completed book. This
plan is self-contained: a fresh session needs THIS branch only
(`claude/chinas-secret-war`); everything referenced below is committed here.
Where `HANDOFF.md` disagrees with this plan, this plan wins.

Read in this order before touching anything: `CLAUDE.md`, this file,
`STYLE.md` (composed contract), `STYLE.local.md` (the ledger; its REBASELINE
section is the target), `review/PROTOCOL.md`.

## 1. State of play — what is DONE, do not redo

- 14/14 units translated, 3,285 paragraphs, 251 notes, 284 glossary rows;
  qa_epub PASS; epubcheck clean. Figures pass complete: 182 inline figures +
  36 plates + real cover (commit edc98bf). Deep audit: 1 error in 81 sampled
  paragraphs, both findings fixed. Last content commit before this pass:
  see `git log` for the plan commit; the pre-pass prose is the parent of it.
- Content is FROZEN: this is an **English-to-English re-voicing** of
  gate-approved, audited translation. Every NEW preserves the propositional
  content of its OLD exactly (no fact/name/number/date-value/claim change).
  No paragraph is merged or split (parity untouched), no name re-romanized,
  no note added or removed except a NOTE-ANCHOR move an edit forces. This is
  the defensible reading of CLAUDE.md rule 4 for a register-only pass, as
  established on the sibling book: fidelity is guaranteed by OLD/NEW
  propositional identity, so the pass needs NO source renders and NO data/zh
  (a fresh checkout has neither). If an edit would change what a sentence
  ASSERTS, it is out of scope; leave it and log it for a corrections pass.

## 2. Hard invariants, each with the command that checks it

- **Anchors (the trap specific to THIS book).** 251 note anchors AND 182
  figure `before` anchors live verbatim in the prose. Before applying any
  unit's edits: `python3 scripts/anchor_check.py <id>` (checks OLD lines
  against notes.json and figures.json). Collisions get a NOTE-ANCHOR pair
  (notes) or a same-pass figures.json `before` update (figures). The
  builder's refusal on an unmatched anchor is the backstop, not the check.
  On the sibling book this lesson cost a build failure; here there are 3.5x
  as many figure anchors.
- **Single-match safety:** `scripts/apply_edits.py` aborts unless every OLD
  occurs exactly once; never improvise a third wording when one fails.
- **Build + QA after every unit:** `python3 scripts/build_reading_epub.py &&
  python3 scripts/qa_epub.py` (PASS required); `epubcheck` at each batch end
  (`java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/chinas_secret_war.epub`,
  fetched by setup.sh).
- **Register measurement (informational):** `python3 scripts/check_register.py
  --ref out/ch01_reading.md out/ch*_reading.md`. The dialogue metric is noisy
  in low-speech units (most of this book); judge those on the narration by
  ear and say so in PROGRESS.
- **Tic regression:** `./scripts/register_tics.sh <id>` per unit after edits;
  the near-zero batteries (antique words, DMY dates, British spellings,
  pivots) must STAY near zero.
- **No literal `<i>` in reading files** (builder refuses); emphasis is
  `*asterisks*`.
- **One commit per unit** ("R0x register pass: chNN"), push at every commit
  point.

## 3. The register target

**The falsifiable test (read aloud, every edited sentence):** a smart writer
today explaining this history to an intelligent friend. If a PBS costume-drama
butler could say it, rewrite; if you could say it to that friend, done.
Three voices: documents starchy, narrator modern-neutral, people sound like
people. Full doctrine: `STYLE.local.md` REBASELINE section.

### 3.1 Measured calibration (2026-08-22, pre-pass)

212k words. Per-unit tic counts (kill-list words / could-only / nominalize /
and-the-rest / narration-ellipsis candidates / exclamations / questions /
>90-word sentences / dialogue contractions per 1k):

```
unit    words kill cldO  nom rest elip excl  qst >90w ctr/1k
ch00      961    0    0    0    0    0    0    2    0   0.0
ch01    24469    1    2   10   11    6   20   15    2   0.2   (ref: 2.0/1k in speech)
ch02    27000    2    0   10    3    5    7   19    3   0.1   STILTED vs ref
ch03    19964    0    5    7    1    0    0   18    0   0.2
ch04     6653    0    0    3    0    0    0    8    0   0.0   little dialogue
ch05    20764    0    4    0    4    0    4   12    1   0.3
ch06    17454    1    3    2    1    0    2   29    2   0.4
ch07    13711    0    2    6    0    0   13   31    1   0.1
ch08    12198    1    4   12    0    0    0   29    1   0.0
ch09    19891    1    3   15    5    3   64   38    1   0.5   ← hottest unit
ch10    22398    3    2   16    2    0   20   17    1   0.4
ch11    14343    0    0   10    3    0    1   10    4   0.0
ch12    10478    0    1   10    0    2   10    4    2   0.0
ch13     1882    0    0   13    1    0    0    2    1   0.0
```

Reading of the table: the book is ALREADY modern on the syntax-archaism axis
(the sibling book's "1893 default" problem barely exists here). The real work
is (a) **speech naturalness**: contractions in dialogue/interview speech, and
~10-15% of narration negatives, exempt registers untouched; (b) **heat
rationing**: ch09's 64 exclamations and the docent questions book-wide;
(c) **judgment sweeps**: ~114 nominalizations (convert ~2/3), 31 "and the
rest," 26 could-only, 16 narration ellipses, 19 long sentences by the spine
test; (d) whatever the **blind critique** finds that greps cannot.

### 3.2 Defect classes for edit tags (each with live examples)

- **[T1] Speech register** (uncontracted/wooden dialogue and interview
  speech): whole-book; e.g. any quoted scene line reading like the narrator.
  CAUTION: voice sheets in HANDOFF; formal-by-design speakers stay formal.
- **[T2] Heat calibration** (authorial reveal-bang, docent question, "so it
  turns out" wrapper): ch09:93 "At least half of the outside intellectuals
  were sent in by the Nationalists!" → period. CAUTION: keep the strongest
  per stretch; quoted slogans keep their bang.
- **[T3] Antique/calque function words** (kill list, could-only class,
  pivots, "in the end?" interrogatives, litotes): ch03:111 "could only fall
  back on the resources of power" → "had to fall back on". CAUTION: idiomatic
  "could come only through the ports" (ch03:381) is fine English; leave.
- **[T4] Nominalization** ("the Xing of the"): ch09:489 "The cracking of the
  false stone case caused a stir" → "Cracking the false stone case...".
  CAUTION: "the founding of the state" is idiomatic; leave.
- **[T5] Doubled synonyms / 等-tags / repetition tics**: ch01:104 "...Li
  Yuchao, and the rest — were prodigies" (vary/cut; 11 in ch01 alone).
- **[T6] Sentence topology** (spine test, appositive between subject and
  verb, em-dash aside that ate the verb, sentence-initial numerals): the 19
  >90-word sentences; count spines first, lists and documents exempt.
- **[T7] Punctuation convention** (narration ellipses → period; marker-
  placement repairs where an edit moves an anchor).
- **[T8] Pronoun rhythm** (name-every-line where English pronominalizes, and
  the reverse fog): blind-critique-driven; qc_entities wants the name once
  per paragraph, pronouns carry the rest.

### 3.3 The KEEP list (a mechanical pass WILL over-correct 2-3 of these; grep the diff for them)

Everything under "DELIBERATE features to PRESERVE" in `STYLE.local.md`:
partisan register and the author's scare quotes; quoted documents/telegrams/
slogans (no contractions, shapes kept); *tewu* use-vs-mention; the datebook
chronology; 对仗 set-pieces; verse `{p}` blocks and datelines; Principal
Sources sections; formal-by-design speakers; unit designations and the ch12
roster; all note and figure anchors; decided renderings (glossary.json).

## 4. Triage discipline

One verdict per paragraph: LEAVE / TOUCH / RECAST. Expected distribution:
**MOST paragraphs LEAVE**: this book measures far cleaner than the sibling
did at its pass, and both prior revision passes on the shelf over-predicted
defects by an order of magnitude. RECAST needs a named T-class and the spine
test; a rewrite that shuffles synonyms is itself a defect in the edit list.
R01 is the calibration batch: its committed diff is the exemplar every later
batch must read first and match in restraint.

## 5. Method per unit (do it exactly like this)

1. `./scripts/register_tics.sh <id>` for the grep candidates.
2. **Blind critique**: `python3 scripts/voice_gate_critique.py prepare <id>`;
   hand `out/<id>_critique_prompt.md` contents to ONE fresh context-free
   subagent (no source, no STYLE, no glossary, no project context; the
   blindness is the point); archive the result with
   `voice_gate_critique.py record <id> <file>`. This is the one sanctioned
   use of a subagent in the pass (it must not share context by design); all
   editing stays in-session and sequential.
3. Adjudicate battery hits + critique findings against the KEEP list and the
   read-aloud test; write `edits/<id>_edits.md` in the apply_edits grammar
   (`### pNNN [T1..T8] TOUCH|RECAST`, OLD/NEW/WHY; NOTE-ANCHOR pairs where
   needed). Where the blind reader misread only because it lacked the source,
   record why and skip.
4. `python3 scripts/anchor_check.py <id>`; fix collisions (figure `before`
   updates go in figures.json in the same commit).
5. `python3 scripts/apply_edits.py <id>`; a failed OLD is skipped and logged,
   never improvised.
6. Build + qa_epub; `register_tics.sh <id>` regression; commit "R0x register
   pass: <id>"; push.
7. Spot-check: re-read every NEW against its OLD for propositional identity
   (numbers, names, dates, claims); note the check in PROGRESS.
8. New rules discovered → `STYLE.local.md` (RULE/WHY/FIX/CHECK, tagged);
   never edit `STYLE.md` or `styles/`.

## 6. Footnote work in this pass

None per-unit (density and coverage were settled at completion). R04 runs
the adopted apparatus checks once, book-wide: bundled notes (one note = one
referent), mid-phrase markers, double-glossed terms, density spread (ch08 vs
ch02). Fix what those sweeps surface; do not hunt beyond them.

## 7. Batch structure and contingency

Four batches, one conversation each, sized by word count; sequential, NO
subagent fan-out (the blind critic per §5.2 is the sole, context-free
exception). If a session dies: stop at a unit boundary, commit, push,
record the resume point in PROGRESS.

- **R01 — calibration + exemplar: ch00 + ch01 + ch09** (~45k words). ch01
  because it is the reference voice (its diff re-anchors the register for
  everything after) and carries the most 等-tags; ch09 because it is the
  hottest unit (64 bangs, 38 questions) and stress-tests heat rationing
  against the KEEP list. After R01, `out/ch01_reading.md` (as revised) IS
  the register reference for R02-R04.
- **R02 — ch02 + ch03 + ch04 + ch05** (~74k words; ch02's STILTED dialogue
  flag is the priority item).
- **R03 — ch06 + ch07 + ch08** (~43k words; heaviest question-mark units).
- **R04 — ch10 + ch11 + ch12 + ch13** (~49k words) **+ the closing sweep**:
  apparatus checks (§6), whole-book tic regression (all 14 batteries),
  check_register table, epubcheck, a dated CHANGELOG entry, COMPLETION.md
  addendum recording the pass, and HANDOFF rewritten to post-pass state.

Estimated total across the four sessions: roughly 250-400 accepted edits
book-wide (the sibling's equivalent pass ran ~8 units in one session at
lower per-unit depth; the blind critique adds depth per unit here).

## 8. Exit checklist (copy into each batch's PROGRESS entry)

- [ ] every edited unit: apply_edits clean, build + qa_epub PASS
- [ ] anchor_check run BEFORE apply, per unit; figure/note anchors moved in
      the same commit where needed
- [ ] tic batteries re-run; near-zero batteries still near zero
- [ ] OLD/NEW propositional spot-check recorded in PROGRESS
- [ ] KEEP-list grep over the batch diff (contractions inside quoted
      documents; softened partisan terms; broken 对仗; lost *tewu* italics)
- [ ] blind critiques archived under review/voice_gate/
- [ ] one commit per unit, pushed; EPUB attached in chat; next kickoff pasted
- [ ] (R04 only) closing sweep of §7 complete

## 9. Verbatim kickoff messages

### R01

```
China's Secret War R01 (register pass)

Read CLAUDE.md, then HANDOFF.md, then REVISION_PLAN.md, then STYLE.md and
STYLE.local.md (its REGISTER REBASELINE section is the target). Run
./setup.sh. Work on branch claude/chinas-secret-war only; if the harness
starts you elsewhere, consolidate per CLAUDE.md rule 2.

Do revision batch R01 = ch00 + ch01 + ch09, per REVISION_PLAN.md §5 exactly:
English-to-English re-voicing, content frozen, edits via edits/<id>_edits.md
+ apply_edits.py, anchor_check before every apply (218 figure anchors are
live in the prose), blind critique per unit via voice_gate_critique.py, one
commit per unit, build + qa_epub each. Expected distribution: MOST
paragraphs LEAVE. R01's diff is the exemplar for R02-R04: restraint is part
of the deliverable. Do not pause for approval mid-batch. Deliver the EPUB in
chat and paste the R02 kickoff from REVISION_PLAN.md §9.
```

### R02

```
China's Secret War R02 (register pass)

Read CLAUDE.md, then HANDOFF.md, then REVISION_PLAN.md, then STYLE.md and
STYLE.local.md. Run ./setup.sh. Branch claude/chinas-secret-war only.

Do revision batch R02 = ch02 + ch03 + ch04 + ch05 per REVISION_PLAN.md §5.
FIRST read the R01 diff (git log, "R01 register pass" commits) as the
exemplar for depth and restraint. ch02's stilted-dialogue flag is the
priority item. The register reference is the REVISED out/ch01_reading.md.
Content frozen; anchor_check before every apply; blind critique per unit;
one commit per unit; build + qa_epub each; do not pause for approval.
Deliver the EPUB in chat and paste the R03 kickoff from REVISION_PLAN.md §9.
```

### R03

```
China's Secret War R03 (register pass)

Read CLAUDE.md, then HANDOFF.md, then REVISION_PLAN.md, then STYLE.md and
STYLE.local.md. Run ./setup.sh. Branch claude/chinas-secret-war only.

Do revision batch R03 = ch06 + ch07 + ch08 per REVISION_PLAN.md §5. Read the
R01 diff first as the exemplar. These are the heaviest question-mark units:
convert the docent questions, keep the real ones (interrogation scenes ask
real questions). Content frozen; anchor_check before every apply; blind
critique per unit; one commit per unit; build + qa_epub each; do not pause
for approval. Deliver the EPUB in chat and paste the R04 kickoff from
REVISION_PLAN.md §9.
```

### R04

```
China's Secret War R04 (register pass, final)

Read CLAUDE.md, then HANDOFF.md, then REVISION_PLAN.md, then STYLE.md and
STYLE.local.md. Run ./setup.sh. Branch claude/chinas-secret-war only.

Do revision batch R04 = ch10 + ch11 + ch12 + ch13 per REVISION_PLAN.md §5
(read the R01 diff first), THEN the closing sweep per §7: apparatus checks
(§6), whole-book tic regression, check_register table, epubcheck, CHANGELOG
entry, COMPLETION.md addendum, and rewrite HANDOFF.md to post-pass state
(remove the kickoff section so the Stop hook stands down). Content frozen;
anchor_check before every apply; blind critique per unit; one commit per
unit. Deliver the final EPUB in chat with a summary of the whole pass
(edits per unit, classes, anything left for a corrections pass).
```
