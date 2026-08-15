# styles/ — the composable prose contract

The collection's style guidance is not one file per book. It is a small set of
reusable LAYERS that compose into each book's working contract, so a lesson
learned on one book can lift every future book of the same kind, and so a
Chinese novel or a Japanese history gets the right combination for free without
anyone hand-writing a new contract.

## The three names to keep straight

- **`styles/*.md` (these files) are the LAYERS.** Canonical, shelf-wide, edited
  deliberately and rarely. Identical in both master branches (kept in sync by
  `tools/sync_shared.sh`, master is upstream).
- **`STYLE.md` in a book is the COMPOSED contract.** A BUILD ARTIFACT written by
  `scripts/compose_style.py`. Never hand-edit it; it is regenerated from the
  layers. Its header records which layers and which content-hashes it was built
  from, so `scripts/check_style_freshness.py` can tell you when the layers have
  moved on.
- **`STYLE.local.md` in a book is the LEDGER.** This is where a book's own
  voice-gate rulings and decided renderings accumulate, in the
  correction -> why -> fix form. It is the ONLY style file a book session edits.
  The composer reads it alongside `STYLE.md`; sessions read both.

## Selection (mechanical, from book.json)

`scripts/compose_style.py` picks the layers with no judgment call:

- **Language** from `source_language`: `zh` -> `lang-zh.md`, `ja` -> `lang-ja.md`.
- **Genre** from `book.json` `genre` if present (`fiction` | `nonfiction`);
  otherwise inferred from `subjects`: any subject whose first token is
  `FICTION`, or that contains the word "fiction", selects fiction; anything else
  (History, Biography, Political Science, ...) selects nonfiction. When the
  inference is not obviously right for a given book, set `genre` explicitly in
  `book.json` and stop guessing.

Composed contract = `_base.md` + `lang-<x>.md` + `genre-<y>.md`, with
`{{VOICE_TARGET}}` filled from the chosen genre layer's directive, and
`STYLE.local.md` appended (created from `STYLE.local.template.md` on first run).

Current layer matrix (write a new layer only when a real book needs a
combination the corpus has not yet exercised):

|            | fiction              | nonfiction                    |
|------------|----------------------|-------------------------------|
| **zh**     | lang-zh + fiction    | lang-zh + nonfiction          |
| **ja**     | lang-ja + fiction    | lang-ja + nonfiction          |

To add a source language, write `lang-<code>.md` on the same shape as the
existing two (source-specific failure modes numbered from 7, an em-dash budget,
romanization and units) and add the mapping above. To add or split a genre
(the reportage/academic split is already flagged inside `genre-nonfiction.md`),
write the new `genre-*.md` with a `VOICE_TARGET` directive on its first line. In
either case, add the new file to the `SHARED` list in `tools/sync_shared.sh` so
it reaches both master branches.

## The promotion rule (how the layers stay current instead of going stale)

A book's lessons land in its `STYLE.local.md`. Most are book-specific and stay
there. Some are general and belong in a layer, or the layers slowly go wrong.
The discipline that prevents both staleness and over-generalization:

1. **Tag as you go.** A rule written into `STYLE.local.md` is marked `#book`
   (specific to this title) or `#promote` (looks general). This is a cheap call
   by whoever just made the correction, not a later forensic audit.
2. **Never edit a layer mid-book.** A book session only ever edits its own
   `STYLE.local.md`. Changing the shelf-wide baseline while a book is in flight
   is exactly the voice-drift risk CLAUDE.md warns about.
3. **Promote between books, with corroboration.** Moving a `#promote` rule into
   a layer is a deliberate, single-writer step on `master`: gather the
   `#promote` candidates from finished books, and promote a rule when it is
   independently corroborated (one book proposing it is `provisional`; two
   books reaching for the same rule promotes it). Each promoted rule carries a
   provenance comment naming the books that motivated it, so a future reader can
   tell a battle-tested rule from an over-generalized one and can trace a bad
   rule back. After a promotion, run `sync_shared.sh` on the EPUB master so both
   branches carry the identical layer.

## Auto-evolution at the voice gate

The voice gate (CLAUDE.md Step 0c) runs a blind-critique loop that evolves
`STYLE.local.md` before the commissioner ever reads the chapter: a
context-blind reader flags what reads wrong as English, the fixes are applied
against the source, and the correction CLASSES are distilled into new
`STYLE.local.md` rules (general ones tagged `#promote`). See Step 0c and
`review/voice_gate_critic_prompt.md`. This is the main engine that keeps the
ledger, and through promotion the layers, sharp.
