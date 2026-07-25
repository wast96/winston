---
name: scanned-book-translation
description: Translate a scanned, image-only book into an annotated English EPUB, accurately and readably, without burning the budget. Use when the user wants a book-length translation from a PDF scan or photographs, an annotated edition with footnotes, OCR-to-EPUB conversion of a long work, or historical fact-checking of a translated text. Covers OCR verification strategy, register control across chapters, footnote apparatus, build gates, and a measured cost model of which quality checks are worth their tokens.
---

# Translating a scanned book

Long translation projects fail in three ways, and only one of them is obvious.

1. **Accuracy** — dropped numbers, mangled names, invented sentences.
2. **Register** — the voice drifts chapter to chapter until the book reads as
   two different translators. Invisible while it happens.
3. **Cost** — the verification burns ten times what it needs to, and most of
   the spend goes on checks that catch nothing.

This skill is built from a completed fifteen-chapter book. Everything below is
what the evidence said, including the parts that were expensive mistakes.

---

## Read this first: the cost model

A real project consumed roughly a quarter of a heavy monthly subscription. Most
of that was avoidable without losing a single real catch. Here is where it went
and what it bought.

### What caught real defects, per token spent

| Check | Cost | Real defects caught |
|---|---|---|
| **Numeric invariant script** | trivial | repeated dropped/altered numbers |
| **Unmatched-anchor build gate** | trivial | **12 footnotes silently missing** |
| **Register stylometry vs reference** | trivial | whole-book voice collapse |
| **Paragraph parity** | trivial | structural drops |
| **Heading-shape check** | trivial | a chapter shipping with no title |
| **Targeted crop-verify of names/numbers** | low | real name mangles, a fake street |
| **Scholarship research** | high | the entire historical apparatus |
| **Whole-page image eye-reading** | **very high** | nothing the crops missed |
| **Blind double translation** | **very high** | ~1 finding across a whole book |
| **Round-trip back-translation** | high | **zero** |

The top five are scripts. They run in seconds, they never get bored, and they
found the worst defects in the project — including twelve footnotes that had
been missing from the book for weeks while every check reported green.

### The three expensive mistakes, named

**1. Reading whole page images by eye.** Over a hundred high-resolution image
reads. The reasoning was "verify everything against the scan." But OCR failure
on CJK scans is not gibberish — it is names and numbers coming out as
plausible valid words. That is a tiny fraction of each page. Crop-verify the
risky spans; do not read the page. Same catches, a fraction of the cost.

**2. Blind double translation of every chapter.** A second model translating
the same text in a fresh context, then diffing. Across an entire book this
produced approximately one substantive finding. Mean agreement ran ~0.69 at
word level, and every low-agreement passage turned out to be ordinary stylistic
variation. **Do not do this per chapter.** Do it once, on one representative
chapter, to calibrate — then stop.

**3. Round-trip back-translation.** Translate back to the source language and
compare. Zero findings. The numeric invariant check catches the same omissions
for a thousandth of the cost. Skip entirely.

### Cost rules

- **Scripts before models.** If a check can be a regex, it must be a regex.
- **Never read a whole page image when a crop will do.** Budget image reads
  like money, because they are.
- **Batch research.** One well-scoped research pass covering several chapters
  beats one agent per chapter. Tell the researcher what you already know so it
  does not re-derive it.
- **Write the QA gate before the content.** A check added at the end finds
  problems you must now fix across everything. The same check on day one
  prevents them.
- **Long replies cost tokens too.** Report findings, not process.
- **Delete nothing, re-read nothing.** Keep state in files, not in context.

---

## Designing checks people actually read

A check that emits noise is a check nobody reads, and the one real failure
hides in the scroll. This is not a style preference — it is the difference
between a gate and a decoration.

Three rules, each learned by breaking it:

**1. Every false positive must be silenceable.** The numeric check is only
usable because measure words and idioms are stripped first (一位, 十分, 三十六
计). Un-stripped, every page throws a dozen hits, you start skimming, and a real
dropped number sails through. Budget time for growing that noise list; it is
the check, not overhead around it.

**2. Do not fail on behaviour that is correct.** A structural check was written
to flag footnote anchors matching the prose more than once, reasoning that the
note might attach to the wrong occurrence. Run against a real book it emitted
twenty-odd failures per run — "Du Yuesheng (134 occurrences)" — every one of
them correct, because recurring-character notes are *deliberately* anchored to a
bare name and *deliberately* attach at its first appearance. The check was
measuring the project's own policy and calling it a defect. Only zero matches is
a failure; multiplicity is informational, behind a flag.

**3. Make the tool filter, not just report.** Auto-extracting proper names from
Chinese OCR yields real names *and* junk, unavoidably: surnames are also common
words (马上 "immediately", 顾左右 from an idiom, 郑重 "solemnly"). No extractor
can tell them apart. But the dual-OCR disagreement can: on a test page it cut 31
candidates to 9 worth an eyeball, and all 8 disagreements were genuine name
mangles (王亚樵 read as 王亚检, 李国杰 as 李国赤). **Where two OCR configs agree,
there is nothing to look at.** That single filter is a 3–4× cut in image reads,
which is the most expensive thing in the whole pipeline.

The general form: when a check cannot distinguish signal from noise, find a
cheap second signal that can, and filter on it. Do not push the triage onto the
reader — the reader is the expensive component.

---

## Pipeline

### Phase 0 — set up the gate before translating anything

Do this first. It is an hour that saves days.

1. Confirm the page offset (PDF page vs printed page) once, then trust it.
2. Establish the **reference chapter**: one chapter translated to the standard
   the user has approved. Everything is measured against this.
3. Wire up, and prove they fail correctly:
   - `check_numbers.py` on a bilingual QC file
   - `check_structure.py` for parity, anchors, headings, glossary drift
   - `check_register.py` against the reference chapter
   - a **build gate that refuses to build** on any unmatched footnote anchor
4. Create the glossary with one rendering per referent and a status per entry:
   `attested` (found in outside scholarship), `provisional` (your romanization,
   not found), `decided` (a project style call).

### Phase 1 — per chapter

```
render → OCR → targeted verify → translate → check → annotate → build → commit
```

**Render.** PyMuPDF, not poppler. Poppler cannot decode JBIG2 streams common in
scans and will fail with "Unknown segment type."

**OCR.** Two configurations of the same engine (e.g. psm 6 and psm 4) diffed
against each other is a free second opinion and a good substitute when a better
engine will not install. Crop the margins first: many books print a vertical
running title in the outer margin that corrupts line ends.

**Targeted verify — the money-saver.** Extract from the OCR every proper name,
every numeral, every unit number, and every span where the two OCR passes
disagree. Magnify and read ONLY those. `verify_names.py` does this.

**Translate.** See "Register" below.

**Check.** Build the bilingual QC file (source line, then translation) and run
the number and structure checks. Fix real drops; extend the noise list for
false positives.

**Annotate.** See "Apparatus" below.

**Build and commit.** Per chapter, so a regression has a small blast radius.

### Phase 2 — final sweep

Re-run everything, because editing prose invalidates every prior check. Then
measure register across all chapters at once and fix drift.

---

## Register: the thing you cannot see by reading

This is the hardest-won lesson in the skill.

Over fifteen chapters the dialogue drifted from **16.2 contractions per
thousand words** in the approved reference chapter to **0.37** by chapter six.
In 136 places where English wants a contraction, the text used two. Gangsters,
a swearing head of state, conspirators — and nobody said "don't." The prose had
become exactly the stilted thing the first draft had been rejected for, and it
happened gradually enough that no single chapter looked wrong.

**A second marker moved with it:** "shall" as a share of shall+will in dialogue
went from 0% to 25%.

### The rule

Measure every chapter against the reference chapter as you finish it. Two
numbers, both free:

- **dialogue contraction rate** — the primary signal
- **"shall" share** — the confirmation

If contractions fall below roughly half the reference rate, the chapter has
gone formal. Fix it then, while it is one chapter.

### Fixing it without wrecking it

Contract inside speech — but **never blanket-substitute**. Four registers keep
their formality, and a mechanical pass will break all of them:

- **Speakers whose stiffness is deliberate.** Foreign officials, ceremonial
  speech, any voice the source itself marks as formulaic. If you have a note
  explaining that a character's speech is stiff by convention, do not undo it.
- **Quoted documents.** Telegrams, newspaper copy, proclamations, letters.
- **Classical tags, proverbs, and set-piece oaths.** The full form is the point.
  A proverb rendered with "doesn't" is worse than no fix at all.
- **A character naming himself in the third person.** That construction is a
  register marker; contracting around it flattens it.

On the real project the first pass over-corrected three of these and they had
to be reverted individually. Expect that, and check for it.

### What not to chase

Punctuation rates (em-dash, semicolon, colon) vary legitimately with how much
parenthetical material the source has. On the real book em-dashes ranged 4.3 to
17.9 per thousand and the dense chapters were using them for genuine work —
dialogue interruption, appositives. **Flattening that mechanically would have
damaged prose that read well.** Report the spread; do not fake uniformity by
degrading sentences.

---

## Accuracy

### The absolute rule

**Never invent a bridging sentence.** If the OCR cuts off mid-thought, go back
to the scan and read the continuation. A fluent invented sentence is the worst
error this kind of project can produce, because nothing downstream will catch
it — not the number check, not the parity check, not a reader. It reads
perfectly and it is fiction.

### The defect classes, in order of danger

1. **Invented bridging text.** Catastrophic, undetectable. See above.
2. **Plausible name mangles.** OCR turns a real person into a different real
   word. Only crop-verification catches these.
3. **Dropped numbers.** The script catches these. Run it always.
4. **Invented precision.** The source says "a good while"; the translation says
   "for weeks." You supplied definiteness the original withheld. No mechanical
   check finds this — only reading a sample by hand. On the real book this was
   a genuine one-off rather than a pattern, which is worth knowing: sample,
   confirm, and don't assume it is systemic.
5. **Silent structural loss.** Notes, headings, whole paragraphs disappearing
   because a builder skipped what it could not match. See below.

### Build gates: never let a builder drop content silently

The single worst defect on the real project: **twelve footnotes were written
and were not in the book.** Their anchors had drifted out of sync with the
prose — mostly capitalisation. The builder skipped unmatched anchors, and QA
passed because references and bodies still agreed **with each other**: twelve
of each, both absent.

**Agreement between two derived artifacts is not integrity.** Check derived
output against the *source of truth* — the notes file — not against itself.

Make the build **fail loudly** when anything cannot be placed. On the real
project that gate caught two further orphans within minutes of being added.

Same lesson, different shape: one chapter's markdown used a single `#` where
every other used two levels. The builder treated it as the book title and
skipped it, and that chapter shipped **with no title** for weeks. Check that
every chapter file has the same heading shape.

### Random-sample deep audit

Once, at the end: sample 3–5% of paragraphs at a fixed random seed, run the
mechanical screens, then **read them by hand against the source**. This is the
only check that finds invented precision and register problems inside otherwise
correct prose. On 32 sampled paragraphs: zero substantive errors, two mechanical
flags both false positives, one real infelicity found only by reading.

Report the confidence honestly. Zero errors in 32 does not prove a rate below
about 11%; it proves you have no evidence of a problem.

---

## Apparatus: footnotes that earn their place

Three kinds of note, and nothing else:

1. **References a reader will not catch.** Who a person is, what an institution
   or object is — with real content. Check claims against scholarship and
   **say in the note** whether the book is corroborated, uncorroborated, or
   contradicted.
2. **Wordplay and texture lost in translation.** Idioms with their literal
   image, classical allusions, register shifts, names whose meaning matters.
3. **Translation uncertainty.** Damaged-scan readings with alternates
   considered, provisional romanizations, genuine ambiguities. State what the
   scan shows and why you chose your reading.

**Density:** calibrate to the reference chapter and hold it. Drifting from 3.3
notes per printed page down to 1.5 is the same failure as register drift.

**Anchors:** verify at write time, not build time. An anchor must be a verbatim
substring, and you should check that the instant you write it.

**Recurring subjects** get their note at first appearance in the BOOK, not
first appearance per chapter.

**Do not harmonize the source's own inconsistencies.** If the book prints a
name two ways, or dates the same event differently in two chapters, translate
each as printed and flag the contradiction in a note. Silently fixing it
destroys evidence about how the book was made.

---

## Fact-checking a popular history

If the book intersects documented history, the apparatus is where most of the
value is. Hard-won method:

**Repetition is not corroboration.** A claim appearing in a dozen outlets is
often one source copied twelve times. Trace claims to their earliest
appearance. On the real book, the central claim of several chapters traced to a
single family memoir published decades after the events — and was absent from
the memoir of the person best placed to know.

**Leave the source language.** The decisive checks came from outside the
book's own literature entirely: naval records in a third language, national
reference works in a fourth, a parliamentary record that placed a man on
another continent on the day the book put him in a hotel.

**Check what a masthead actually is.** Pieces carrying a major newspaper's name
turned out to be popular-book excerpt columns — reprints, not reporting.

**Look for the shape of the errors.** Individual corrections are less valuable
than the pattern they form. Sorting one book's claims by date and type revealed
that everything before a certain year checked out and everything after it
collapsed — which said more about the book than any single correction.

Record verdicts as **CORROBORATED / PARTLY / UNCORROBORATED / CONTRADICTED**,
with sources, per claim.

---

## Practical traps

**Rendering.** PyMuPDF only for JBIG2 scans.

**Figure captions** are often vertical text in the outer margin beside the
image. Crop that zone and OCR it. If no caption is legible, say so — never
invent an identification. Captions frequently carry information the body text
does not.

**Manifest overwrites.** Figure-detection scripts that rewrite their manifest
each run will silently destroy earlier chapters' entries. Merge, don't
overwrite.

**Killing subprocesses.** Killing a parent leaves orphaned OCR children
consuming every core. On the real project seven orphans ran for half an hour,
load average hit 33 on 4 cores, and a page went from 3 seconds to timing out.
Kill the process group, verify with `pgrep`, and check load before blaming the
tool.

**Background jobs die with the shell.** A job backgrounded with `&` inside a
foreground command is killed when that command times out. If each unit of work
is fast, just run batches in the foreground — far more reliable than fighting
process lifecycle.

**Escaping order in builders.** Insert note anchors BEFORE any markup
substitution, or the substitution eats the anchors.

**Sorting a noise list by pattern length reintroduces bugs.** Character classes
make short patterns look long. Order longest-literal-first by hand and say so
in a comment.

---

## Deliverables

- `out/<book>.epub` — one XHTML per chapter, one spine, continuous note
  numbering, mimetype stored first
- `out/chNN_reading.md` — the correction surface the user actually reads
- `out/chNN_bilingual.md` — paired QC file (never ship this)
- `notes.json`, `glossary.json`, `figures.json`
- `PROGRESS.md` — per chapter: page range, note count, names added with status,
  and **anything flagged for the user's read-through**. Write it as you go.
- A **term ledger** rendering the glossary so someone who reads no source
  language can audit every rendering.

---

## References

- `references/cost-model.md` — the full spend breakdown and what to cut
- `references/register-drift.md` — the measurements, the fix, the exemptions
- `references/build-gates.md` — silent-loss failure modes and the gates
- `references/fact-checking.md` — source criticism for popular history

## Scripts

All four were run against a finished fifteen-chapter book before being written
up here, and their thresholds are set from what that produced — not guessed.

- `scripts/check_numbers.py` — quantity survival (run every chapter).
  `--noise FILE` for project-specific false positives; you will need it.
- `scripts/check_register.py` — voice drift vs the reference chapter.
  Chapters under ~1,200 speech words are flagged noisy rather than failed.
  Elevated "shall" is a warning, not a failure: some speakers are formal on
  purpose.
- `scripts/check_structure.py` — parity, anchors, headings, glossary drift.
  Compares only the opening headings (`--heading-depth`, default 2), because
  deeper structure varies legitimately — a prologue has no numbered sections.
  Builder-injected anchors such as datelines go in a `datelines` config key,
  which waives them but still prints them, so the waiver list cannot quietly
  become a way of hiding real orphans.
- `scripts/verify_names.py` — targeted crop verification instead of page reads.
  With `--auto` it shows only spans the two OCR configs disagree on; `--all`
  shows every candidate. Named `--terms` are always shown.
