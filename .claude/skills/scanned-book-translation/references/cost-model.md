# Cost model

Measured on a completed fifteen-chapter translation with full historical
apparatus. The project consumed roughly a quarter of a heavy monthly
subscription budget. Most of that was avoidable.

## Where the money actually went

Roughly, in descending order:

1. **Whole-page image reading** — over a hundred high-resolution page images
   read by eye, at 2 half-page reads per printed page across five chapters.
2. **Blind double translation** — a second model re-translating each chapter in
   a fresh context, then a diff. Roughly 85k tokens per chapter, several
   chapters, plus the diffing.
3. **Research subagents** — one per chapter, each 80–140k tokens.
4. **Infrastructure thrashing** — perhaps fifteen turns lost to an OCR process
   problem that was self-inflicted (orphaned child processes).
5. **Verbose reporting** — long explanatory replies that repeated context the
   user already had.

## What each bought

### Whole-page image reading — cut it

**Bought: nothing that targeted crops would not have caught.**

The reasoning was sound-sounding: verify every page against the scan rather
than trusting OCR. But it misidentifies the threat. OCR failure on a CJK scan
is not gibberish — gibberish is obvious and self-flagging. The dangerous
failure is a name or number coming out as a *different plausible valid word*.
Those occupy a few percent of a page.

**Replace with:** extract candidate spans from the OCR (proper names, numerals,
unit designations, and anything where two OCR configurations disagree),
magnify only those, read only those. One name-strip crop is a small fraction of
a full page read.

Real catches from the targeted method: a famous jurist's name mangled into a
nobody; a street name that does not exist, hiding a real street; an author's
own factual error, caught because the name was verified and then checked
against the record.

### Blind double translation — do it once, not per chapter

**Bought: approximately one finding across an entire book.**

Two independent translations of the same passage, diffed, produced a mean
word-level agreement around 0.69. Every single low-agreement passage inspected
turned out to be ordinary stylistic variation — one translator writing "did not
agree," the other "was unconvinced." Zero meaning conflicts across every
chapter checked.

The one genuine catch was an over-confident transliteration: a name rendered
with a definite English spelling the source did not actually determine.

**Replace with:** run it ONCE on a single representative chapter to calibrate
whether the primary translation is sound. If agreement is high and divergences
are stylistic, stop. Spend the saving on the numeric and structural checks,
which catch more for a thousandth of the cost.

### Round-trip back-translation — cut entirely

**Bought: zero findings.**

Translating the English back to the source language and comparing was proposed
as an omission detector. The numeric invariant check detects the same class of
omission — dropped quantities — deterministically and for free. Length-ratio
comparison on the bilingual file catches dropped clauses.

### Research subagents — keep, but scope them

**Bought: the entire historical apparatus, which was the most valuable output
of the project.** This is where the money *should* go.

But they were badly scoped:

- One agent per chapter meant re-deriving shared context repeatedly. Several
  agents independently established the same background facts.
- Prompts did not say what was already known, so agents re-researched settled
  questions.
- Some returned 140k tokens of which perhaps a fifth was used.

**Better:** batch two or three chapters per agent where the subject matter
overlaps. Open the prompt with a compact statement of what is already
established and explicitly instruct: *do not re-derive these*. Ask for verdicts
and sources, not narrative. Cap the scope: "the three most valuable things you
can tell me are X, Y, Z."

### Scripts — spend more here, not less

Every high-value catch on the project came from a script:

- dropped numbers → the invariant checker
- twelve missing footnotes → an anchor gate added at the very end, which would
  have caught them on day one
- a whole-book voice collapse → sixty lines of stylometry
- a chapter shipping with no title → a heading-shape comparison
- a dangling note reference → the EPUB link checker

Total cost of all of them: negligible. Total value: the worst defects in the
project.

## Rules

1. **If a check can be a regex, it must be a regex.** Never spend a model call
   on something deterministic.
2. **Build the gate before the content.** A check added at the end finds
   problems you must now fix everywhere. The same check on day one prevents
   them from being created.
3. **Budget image reads like money.** Crop, don't page.
4. **Calibrate expensive checks once, then stop.** If a check produces no
   findings on its first two runs, it is not going to start.
5. **Batch and pre-brief research.** Tell it what you know.
6. **Keep state in files, not context.** `PROGRESS.md` written as you go means
   a summarized context loses nothing.
7. **Report findings, not process.** The user does not need the narration.
8. **Fix your own infrastructure failures fast.** Check load average and orphan
   processes before concluding a tool is slow.

## A rough target

The same book, done again with this skill, should cost on the order of a third
to a quarter of the original — with *more* defects caught, because the cheap
structural gates would be in place from the first chapter rather than the last.
