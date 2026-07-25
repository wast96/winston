# Final sweep — accuracy and stylistic unity

*A whole-book pass over the translated text: the prologue and chapters 1–6.
Chapters 7–15 exist as assessments rather than translation and are not in
scope here.*

---

## The two defects that mattered

### 1. Twelve footnotes were not in the book

**289 notes were written. 277 were shipping.** Twelve had anchors that no
longer matched the prose — mostly capitalisation slips ("a gentleman's word"
against a sentence beginning "A gentleman's word"), one wording drift, one
anchored to a phrase that exists only in a section heading.

They failed silently. The builder skipped any note whose anchor didn't match,
and `qa_epub` stayed green because references and bodies still agreed *with
each other* — twelve of each, both absent. The check could not see the
difference between a note that was never meant to exist and one that had been
swallowed.

All twelve are now in the book, and **the builder now refuses to produce an
EPUB if any anchor fails to match**, printing the offenders. That check
immediately earned itself by catching two more during this sweep.

### 2. Chapter six was shipping without its title

Its markdown used a single `#` for the chapter heading where every other file
uses the two-level convention. The builder treats `#` as the book title and
skips it — so chapter six's title, subtitle and dateline were all silently
dropped from the finished book. Nobody would have noticed except by opening
that chapter and finding it starts mid-air.

Fixed; the chapter now renders its heading and its dateline note.

---

## Stylistic unity: the drift is real and measurable

You said you drafted one part under one model and one under another. I didn't
guess at the boundary — I measured the prose, and the signal is unambiguous.

**Contractions inside dialogue**, against chapter one as the bar:

| | ch1 (the bar) | ch2 | ch3 | ch4 | ch5 | ch6 |
|---|---|---|---|---|---|---|
| **before** | 16.2 | 10.4 | 8.5 | 8.7 | 2.8 | **0.37** |
| **after** | 13.4 | 9.5 | 7.3 | 8.5 | 20.1 | **11.0** |

Chapter six had **two** contractions in 136 places where English wants one.
Gangsters, Chiang Kai-shek swearing, Japanese officers conspiring — and nobody
said "don't." That is exactly the stiltedness that got the first draft
rejected, and it had crept in measurably.

**"Shall" as a share of shall+will in dialogue** told the same story from
another angle: 0% in chapters 1, 2 and 4, rising to 21% in ch5 and 25% in ch6.
Two independent formality markers moving together.

### What I changed, and what I deliberately didn't

This was not a blanket substitution. Three registers keep their starch because
the stiffness is doing work:

- **The Japanese officers.** Their formulaic speech is a period convention the
  Chinese itself observes, and chapter six's notes already comment on it. 61
  paragraphs left untouched on this ground.
- **Quoted documents** — telegrams, newspaper copy, declarations.
- **Classical tags and set-piece oaths.** Two of these I had to put *back*
  after the first pass caught them: a proverb about not climbing to the Three
  Treasures Hall without business, and the oath about not being born on the
  same day but praying to die on it. Also Wang's ultimatum where he names
  himself in the third person — the formality there is the character marker.

Chapter five now sits slightly *above* the bar at 20.1. I'd rather it overshoot
into naturalness than sit at 2.8.

### The residual I left alone

Em-dashes still range from 17.9 per thousand in ch3 to 4.3 in ch6, against
12.2 in chapter one. That is a genuine unity gap and I chose not to flatten it
mechanically. Inspecting the dense paragraphs, the dashes are doing real work —
dialogue interruption, appositives, dramatic pause — and converting them
wholesale to commas would damage prose that currently reads well. Faking
uniformity by degrading sentences is a worse outcome than an honest spread.

If you want it closed, it needs a human pass, not a script.

---

## Accuracy verification, whole book

Everything re-run after the prose edits, since editing text invalidates every
prior check:

| Check | Result |
|---|---|
| Quantity invariants (numbers, dates, counts) | **0 unresolved** across all six units, 793 pairs |
| Paragraph parity, source vs English | **exact** in every unit |
| Glossary drift (one rendering per referent) | **0** |
| Note anchors resolving | **289 of 289** |
| Entity coverage | misses adjudicated — all pronoun substitution, no dropped content |
| EPUB structure | **PASS**, 42 files, all links resolve |

### The invented-precision defect: a one-off, not a pattern

The deep audit had caught me rendering a deliberately vague duration as "for
weeks." I swept the whole book for that defect class — definite English
durations and counts paired with vague source markers. Four candidates
surfaced; **all four were false positives**, with the definiteness present in
the source each time ("two months of surveillance," "many days," "many years").

So that error was isolated rather than systematic, which is the more reassuring
finding.

---

## What this pass did not test

Register is measurable at the margins — contractions, modals, punctuation — and
those margins are now aligned. Whether the prose is *good*, whether the
novelistic voice carries, whether a given sentence lands: none of that is
visible to any check I can run. That judgement is still yours, and chapter one
remains the bar.
