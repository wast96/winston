# CORRECTIONS

The commissioner files corrections here after reading the EPUB. A pasted chat
message ("ch12: 'X' reads oddly; global: stop rendering Y as Z") is a
first-class corrections input too: the session transcribes it into this file
before acting. This file is the ledger, not a form the commissioner must fill.

Two kinds:

- **GLOBAL** — a rendering, a register rule, or a note policy that must apply
  everywhere ("render X as Y throughout", "stop noting every idiom", "this
  person is actually Z"). Applied via a glossary/style change plus a
  grep-driven edit across ALL built units, INCLUDING note bodies and glossary
  bodies, then rebuild + full QA. A global correction applied to only some
  units is worse than not applying it.
- **LOCAL** — a fix at one spot. Apply, rebuild, QA.

After a batch of corrections: rebuild, run qa_epub, list every file touched in
the reply, and append a dated entry to CHANGELOG.md. A corrections pass with
ZERO items is still a clean-checkout regression run: re-clone, regenerate the
regenerables, rebuild, re-run the whole-book checks, prune stray branches.

## Entry form (append below; greppable, one block per item)

### [GLOBAL|LOCAL] <short title>
Unit: <chapter id, or "book-wide">
Where: <anchor phrase or short quote from the EPUB>
Problem: <what is wrong>
Fix: <what it should be>

## Pending

(none)

## Done

### [GLOBAL] Footnote dates to month-day-year (2026-08-22)
Unit: book-wide (note bodies)
Where: e.g. "the coup of 12 April 1927", "the Wuchang Uprising of 10 October 1911"
Problem: 19 dates in footnote bodies were day-month-year, while the reading
  prose and the translator's note ("Dates are written month-day-year
  throughout") use month-day-year; notes.json even carried the same date in
  both forms. A house-style/consistency defect against the frozen B09 policy
  (STYLE.local "D Month YYYY ... should be zero").
Fix: normalized all 19 to month-day-year ("April 12, 1927"), ranges included
  ("March 22-23, 1927", "December 11-13, 1927"). Note bodies only; no anchor
  affected; check_apparatus clean.

### [GLOBAL] Gloss each street once, book-wide (2026-08-22)
Unit: book-wide (ch03, ch05, ch06, ch07, ch14, ch15 reading files)
Where: e.g. "Avenue Road (today Beijing West Road)" appearing 3x; "Burkill
  Road (today Fengyang Road)" 3x
Problem: 13 "(today X)" parenthetical street glosses re-glossed a street
  already glossed earlier in the book, against the frozen STYLE.local rule
  "gloss a street at most ONCE per name, book-wide ... keep the first, cut the
  rest" (the back Street Gazetteer carries the mapping).
Fix: kept each street's first gloss in reading order; cut the 13 later
  parentheticals. The one anchored gloss (ch04 "Avenue Joffre (today Huaihai
  Middle Road)") is a kept first occurrence, so unaffected. check_apparatus
  clean; no duplicate "(today X)" gloss remains.
