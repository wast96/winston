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

### LOCAL ch32 keyed-org hyphenation
Unit: ch32
Where: "we were attached to the 'North China Bandit Suppression Headquarters'" (para 25)
Problem: ch32 (translated B25) rendered 华北剿匪总司令部 as "North China Bandit Suppression
  Headquarters" (and the short 华北剿总 as "...Command") without the hyphen; the org was
  keyed at B27 (ch34) as the hyphenated "North China Bandit-Suppression Headquarters,"
  so check_content flagged para 25 as displaced (pre-existing on the committed HEAD).
Fix: aligned both occurrences to the keyed "North China Bandit-Suppression Headquarters";
  regenerated ch32 en.json; check_content ch32 now 0 displaced. (Applied B28, ch35 batch.)

(move applied blocks here, with the CHANGELOG date)
