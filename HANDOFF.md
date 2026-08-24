# HANDOFF: Nameless Heroes (英雄无名), Chen Gongshu. **COMPLETE**

**The book is COMPLETE.** The translation, the whole-book register revision
(R1–R9), and the final **F0 footnote-density pass** (a single wave over all 43
chapters, REVISION_PLAN §12) are all finished. There is no next batch and no
kickoff to paste. Read `COMPLETION.md` for the full record.

## Final state

- **Deliverable:** `out/Nameless Heroes, The Memoirs of a Nationalist Secret Agent.epub`, committed with `git add -f` on
  branch `claude/nameless-heroes`.
- **43 of 43 units** translated, register-revised, and footnote-densified; clean
  pending-aware TOC; complete coverage.
- **628 translator notes** (375 after the register pass; **+253 added in F0**),
  0 source notes (the source carries none of its own).
- **Glossary: 708 rows.** 0 in-text figures; the source's cover reused
  byte-identical.

## Final gate results (after F0)

- `qa_epub`: **PASS** — 57 files, 50 documents, 628 note references / 628 bodies
  / 628 backlinks, all links resolve.
- epubcheck 5.1.0: **0 fatals / 0 errors / 0 warnings / 0 infos** (EPUB 3.3).
- `check_apparatus`: 0 failures / 0 warnings.
- Whole-book note reconciliation: no duplicate anchors; no duplicate glosses
  introduced by F0 (first-appearance discipline held; recurring furniture glossed
  once and referenced thereafter). Content stayed FROZEN — notes only.

## What F0 did

Greatly increased footnote density so a non-specialist Western reader has every
term, person, place, event, institution, and allusion explained — generous but
never padded, one gloss per item at first appearance. All notes fact-checked
against real scholarship (never LLM-sourced; the one Grokipedia link that
surfaced was excluded per rule 5), verdicts stated, disputed claims footnoted as
disputed with the text left faithful. Per-chapter counts, sources, and
NOT-re-noted ledgers are in `PROGRESS.md` (§ "F0 COMPLETE"); the pass summary is
in `COMPLETION.md` (§ "The F0 footnote-density pass").

## Notes for any later reader/commissioner

- **Anchor rule (learned in F0):** a note anchor must never contain a literal
  `&`, `<`, or `>` — those pass `apparatus_merge` (which checks the raw
  reading.md) but break the build (which matches XHTML-escaped text). Pick a
  different substring.
- The register pass converted narration dates to Gregorian/American; quoted
  documents keep their period register and dates by design.
- Provisional romanizations remain flagged `provisional` in the glossary (listed
  at the end of `out/term_ledger.md`).
- Setup regression: the one known false alarm ("hook stands down on template
  stub") still FAILS by design — the kickoff_guard Stop hook is correctly
  ENFORCING because this HANDOFF carries a real (non-template) message, which is
  exactly what that test inverts. Benign; all other checker regression tests
  green.

*The book is COMPLETE. This handoff is not to be touched further.*
