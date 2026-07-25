# Register drift

The failure you cannot see by reading, and the cheapest one to catch.

## What happened

A fifteen-chapter translation, one approved reference chapter setting the
standard. Nobody noticed anything wrong. Reading any single chapter, the prose
was fine.

Measured against the reference, contractions inside dialogue:

| | reference | ch2 | ch3 | ch4 | ch5 | ch6 |
|---|---|---|---|---|---|---|
| per 1,000 speech words | **16.2** | 10.4 | 8.5 | 8.7 | 2.8 | **0.37** |

By chapter six there were **two contractions in 136 places where English wants
one**. Criminals, a swearing head of state, conspirators plotting a murder —
and not one of them said "don't."

A second marker moved in step: **"shall" as a share of shall+will in dialogue**
went 0% → 0% → 5% → 0% → 21% → 25%.

Two independent formality markers, sliding the same direction. The prose had
become the exact stilted thing the project's first draft had been rejected for.

## Why reading does not catch it

- It is **gradual**. No chapter is far from its neighbour.
- It is **distributed**. No single sentence is wrong.
- The translator has **no memory of the earlier register** by chapter twelve.
- Each chapter is **internally consistent**, so nothing jars within a chapter.

Measuring within-chapter fifths confirmed this: each chapter was uniform in
itself. The step was always *between* chapters, and the slide was monotonic.

## The measurement

Two numbers per chapter, both free, both from `check_register.py`:

**1. Dialogue contraction rate.** Extract quoted speech, count `n't 'll 're 've
'm` per thousand speech words. Compare to the reference chapter.

Threshold: below ~45% of the reference rate, the chapter has gone formal.

**2. "Shall" share.** `shall / (shall + will)` inside speech. Anything above
~10% when the reference is near zero is a formality signal.

**Caveat:** chapters with little dialogue (under ~400 speech words) are noisy.
Flag them but do not act on them.

## Fixing it

Contract inside quoted speech. **Never blanket-substitute.** Four registers
must keep their formality, and a mechanical pass breaks all four:

### 1. Speakers whose stiffness is deliberate

Foreign officials, ceremonial voices, any speaker the source itself renders in
formulaic language. On the real project, Japanese officers' speech was
deliberately stiff in the original — a period convention — and there was
already a footnote explaining it. Contracting them would have contradicted the
book's own apparatus. 61 paragraphs were correctly excluded on this ground.

### 2. Quoted documents

Telegrams, newspaper copy, proclamations, public declarations, letters. These
are not speech and do not take speech's register.

### 3. Classical tags, proverbs, set-piece oaths

The full form is the point. A proverb rendered with "doesn't" is worse than
leaving the chapter formal. On the real project the first pass wrongly
contracted a proverb and an oath and both had to be restored individually.

### 4. A character naming himself in the third person

That construction is itself a register marker — a man staking his standing on
what he has just said. Contracting around it flattens the effect.

**Expect the first pass to over-correct two or three of these.** Check
specifically for it afterward: search the diff for proverbs, oaths and
documents.

## What not to chase

**Punctuation rates vary legitimately.** Em-dashes on the real book ranged 4.3
to 17.9 per thousand words against a reference of 12.2 — a fourfold spread, and
a genuine inconsistency. It was left alone deliberately.

Inspecting the dense paragraphs showed the dashes doing real work: dialogue
interruption, appositives, dramatic pause. Converting them wholesale to commas
would have damaged prose that read well. **Faking uniformity by degrading
sentences is worse than an honest spread.**

Some of the variation is also the source's: a chapter whose original has more
parenthetical structure will legitimately take more dashes.

Report the spread. If the user wants it closed, it needs a human pass.

## Other markers worth watching

Weaker but occasionally informative:

- **Sentence median length** — rose from 13 to 16 across the drift.
- **Restrictive "that" clauses** — rose steadily; more subordination is more
  formal.
- **Participial openers** ("Seeing X, he…") — a translationese tell if they
  climb.
- **Colon-introduced glosses** — fell as the prose stiffened.

## The rule

**Measure every chapter against the reference as you finish it.** It costs
nothing. Caught at chapter five, it is one chapter to fix. Caught at the end,
it is the whole book — and by then the fix is a large mechanical edit across
prose you can no longer easily re-read, with a real risk of breaking footnote
anchors, which is exactly what happened.
