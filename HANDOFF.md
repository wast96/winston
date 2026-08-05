# HANDOFF — <book title>

This file is the baton. A fresh session with no memory reads it and starts
immediately. **It is the ARCHIVE of the kickoff message, not its delivery:
every batch ends with this file's kickoff block PASTED VERBATIM INTO THE
CHAT, alongside the attached EPUB. Writing it here alone does not count.** Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section. When the book completes, replace
the kickoff with the completion notice and do not touch it afterward (the Stop
hook keys off it).

## Message to paste into the next chat

```
(First line: the project label and batch, e.g. "My Book B02", then a blank
line. Then the kickoff body per START_HERE.md's Message 2: read CLAUDE.md,
HANDOFF.md, book.json; the batch scope with unit ids (chapters/sections, never pages);
any script fix this batch needs; end with "attach the EPUB and paste the next
kickoff in the same reply". Batch 1's version ends at the voice gate instead.
On the last batch, ask for back matter, the whole-book reconciliation sweep,
COMPLETION.md, and the final EPUB committed.)
```

## What is DONE (do not redo)

- (one line per completed batch: unit ids, note count so far, glossary rows,
  figures; the current continuous note number)

## Tooling in place (do not revert)

- (every script patch accumulated this project, by batch, with one line on
  what it fixed; the measured crop parameters; the check_structure config)

## Renderings settled this batch / carry-forward

- (new glossary decisions; the standing carry-forward list a memoryless
  session needs so it does not re-romanize)

## Voice sheets (one per major character, written at first appearance)

- (e.g. "CHEN QIANLI: terse, working-class Shanghai; contracts everything;
  calls seniors 'Old <surname>'. Never florid." Two lines each; consult at
  every dialogue scene.)

## Where the book stands

- (two or three sentences of plot/argument state at the end of the last
  translated unit, so the next session translates in context)

## What is NEXT

- Batch <Bxx> = <scope, unit ids>. Any pending script fix.

## Open items for the read-through

- (provisional readings still open; history flags; anything uncertain)

## Environment / traps state

- (epubcheck available or not; extractor quirks of this source;
  stray-branch note; anything that bit this session)
