# ASSESSMENT.md — retrofit assessment of a completed book (template)

Copy to `ASSESSMENT.md` on the BOOK'S branch and fill every section in order.
This is a READ-ONLY inspection: no translation text changes in this session.
Its product is a commissioning decision: whether the book earns a retrofit
pass against the CURRENT shelf standard, of what kind, and at what size. The
shape is the assessment that worked on a real book (zhou-enlai's register
assessment, 2026-08-22), extended to cover the footnote-density directive.

(Obeys CLAUDE.md rule 6: no em dashes in this file's prose.)

## 0. Upgrade the toolkit BEFORE measuring, and the doctrine BEFORE any pass

Older book branches carry the CLAUDE.md, style files, and scripts of the
template version they forked (see the fork note in the book's
TEMPLATE_CHANGELOG.md, and `check_style_freshness.py`). Two consequences:

1. **For this assessment:** copy the current shared scripts onto the branch
   first (at minimum `scripts/register_tics.py`, `scripts/check_register.py`,
   `scripts/anchor_check.py`), or run them from a masters checkout. Measuring
   with the old tools misses what the new ones were built to see.
2. **For any commissioned pass:** step one of the pass is replacing the
   branch's template files (CLAUDE.md, `styles/`, shared scripts, templates)
   with the current masters' versions, THEN composing STYLE.md if the book
   predates the layer system. A session working on the old branch otherwise
   follows the outdated doctrine sitting in it, including the retired
   footnote-density model. Record here which template version the book forked
   and what it therefore predates.

## 1. What the book predates

<one paragraph: fork version, what shipped since that matters here (the
composed style system, the register rebaseline, the footnote-density
directive, the naming policy), and which of this book's own practices later
became shelf canon or were later overruled.>

## 2. Measured state (paste the numbers; measurement before opinion)

- **Size:** <units, words, paragraphs, current note count>.
- **Tic profile:** paste the `register_tics.py --profile` table, dated.
- **Register vs reference:** `check_register.py --ref <frozen reference>`
  summary. If the book predates the voice gate and has NO frozen reference,
  say so; use its first chapter as the baseline and mark every conclusion
  accordingly.
- **Footnote density vs the directive:** notes per unit and words per note
  per chapter. Benchmarks: books annotated under the current directive run
  roughly 40 to 60 notes per unit on chapter-sized units, and words-per-note
  should not swing more than about 2-3x across the book. State this book's
  numbers against both.
- **Consistency spot-checks:** date-format split, spelling-locale strays,
  the two or three highest-traffic decided renderings grep-counted, and the
  book's renderings checked against the current `authority.json` (status
  `decided` entries bind; list every place this book deviates and whether the
  deviation is recorded).

## 3. What already meets the standard (do NOT "fix" these)

<list, with numbers, everything at or near target: metrics inside tolerance,
densities already generous, deliberate register features, the book's KEEP
list if it has one. Every prior pass over-predicted defect density by an
order of magnitude; this section is what keeps the pass small.>

## 4. Defect inventory, ranked by value per keystroke

- **Tier A: mechanical consistency** (near-zero risk; grep-locatable):
  date-format normalization, locale strays, ledger violations, renderings
  that drifted from the book's own decisions or from adjudicated
  authority.json entries. <counts per item>
- **Tier B: kill-list sweep** (semi-mechanical, by-ear confirmation per
  hit): the register_tics batteries with material counts, each with its
  carve-outs. <counts per battery>
- **Tier C: judgment work** (bounded, needs zh-against-en reading): spine
  test candidates, chapters that drift register, and the FOOTNOTE
  DENSIFICATION workstream: chapters below the density benchmark, the
  glossary-as-quarry candidate count, and the four coverage domains plus the
  lost-in-translation layer swept per CLAUDE.md. Size it honestly: <N>
  chapters at roughly <M> new notes each.

## 5. Scores (relative to the genre's published English benchmark)

<accessibility to a no-background reader / translation fidelity / prose
against native-authored peers, each with one sentence of evidence; current
overall and projected after each tier, so the commissioner can buy tiers
separately.>

## 6. Verdict and commissioning proposal

<recommended pass: none / tic sweep / densification / full register plus
densification. Batch count and rough per-batch scope. What is explicitly out
of scope. The standing cautions: content is frozen; most paragraphs LEAVE;
the pass runs under REVISION_PLAN.template.md with anchor_check before every
apply; and the first act of the pass is section 0's template upgrade.>
