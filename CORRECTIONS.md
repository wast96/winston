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

### [GLOBAL] Oyuki-is-fiction: cite the right source (commentary, not Shiba's afterword)
Unit: book-wide (notes at ch32 and ch68)
Where: ch32 note on "the art-name Kōka"; ch68 note on "there was a small woman who left an offering"
Problem: Both notes stated that Shiba declares Oyuki invented "in his afterword."
  On reading the actual back matter in B15, Shiba's afterword (ch69) speaks only
  of Hijikata and never mentions Oyuki. The explicit statement that Oyuki is a
  created character is in the film-director Harada Masato's commentary (ch70):
  "She is a created character, but there are signs that Shiba overlaid on her the
  story of how he and his own wife first came together."
Fix: Reworded both notes to attribute the statement to this edition's commentary
  (ch70) and to say plainly that Shiba's own afterword does not discuss her. The
  underlying fact (Oyuki is Shiba's invention) is unchanged and well attested; only
  the mis-cited source was corrected. The new ch70 note on "She is a created
  character" is now the primary authority the other two point back to.
  Applied to notes.json (authoritative) and the archival source apparatus files
  out/ch32_apparatus.json and out/b14_apparatus.json. CHANGELOG: 2026-08-15 (B15).
