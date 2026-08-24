# HANDOFF: Nameless Heroes (英雄无名), Chen Gongshu. REGISTER PASS COMPLETE; FOOTNOTE PASS (F0) NEXT

**The translation is COMPLETE and the whole-book REGISTER REVISION PASS (R1
through R9) is now COMPLETE. The book is NOT yet in its final state: the
commissioner has ordered ONE further pass, the FOOTNOTE-DENSITY wave (F0), a
single session over the whole book. The authority for F0 is `REVISION_PLAN.md`
§12. The next-chat message below is the F0 kickoff, NOT a "book complete"
notice. Only when the footnote pass is done is the book COMPLETE.**

## Message to paste into the next chat

```
Nameless Heroes F0: footnote-density pass (single wave, whole book)

Branch: claude/nameless-heroes ONLY. First acts: git fetch origin
claude/nameless-heroes && git checkout claude/nameless-heroes && git
reset --hard origin/claude/nameless-heroes. If the harness started you
on a stray branch, consolidate and delete it per CLAUDE.md rule 2.
Never read any other branch.

Read CLAUDE.md (esp. "Footnotes — what earns one" and rule 5 on
fact-checking), then REVISION_PLAN.md §12 IN FULL (the authority for this
pass), then run ./setup.sh.

Scope: the WHOLE BOOK, all 43 chapters, in one wave. Content is FROZEN —
add footnotes only, no prose changes. GREATLY increase footnote density:
explain every term, person, place, event, institution, and allusion a
non-specialist Western reader would miss — but never add a note just to
add one. Author notes via apparatus_merge.py (numeric character references
only), anchors verified verbatim; check_apparatus.py clean; fact-check
against real scholarship, never LLM-sourced, verdicts stated; respect
first-appearance discipline (grep earlier occurrences) and keep a "NOT
re-noted" ledger. Do ch01 FIRST as the density exemplar and pause once to
present it (§12.4); then run to completion. Rebuild + qa_epub (+ epubcheck);
commit and push AT EVERY CHAPTER BOUNDARY; record the resume point in
PROGRESS.md so an interrupted session resumes with this same kickoff.

End when the whole book is densified: PROGRESS.md updated (final note
count, sources, NOT-re-noted ledger), COMPLETION.md rewritten, HANDOFF.md
marked COMPLETE, and the reply carries the rebuilt EPUB attached.
```


## Register pass state (COMPLETE, R1 through R9)

- **DONE:** R1 (ch06, exemplar, frozen as `reference/R1_frozen.md`). R2 (ch07,
  ch08). R3 (ch01-ch05, ch09, ch10). R4 (ch11-ch13). R5 (ch14-ch18). R6
  (ch19-ch24). R7 (ch25-ch29). R8 (ch30-ch35). **R9 (ch36-ch43 plus the
  whole-book close): ~229 edits** (ch36 47, ch37 11, ch38 10, ch39 32, ch40 66,
  ch41 31, ch42 30, ch43 2). R9 covered Chapters 4-10 of the Fifth Part plus the
  Afterword: dense military chronologies (ch39/ch40/ch41), the Zhu Zhankui
  defector case (ch38), and the reflective coda (ch43). Dominant edit was DATE
  accessibility (~230 Republic-year and spelled day-month narration dates ->
  Gregorian/American, +1911); all quoted documents and reproduced comrade
  accounts LEFT WHOLE with their internal dates. Full detail, tic tables,
  spot-audit, deep audit, and whole-book close in PROGRESS.md §R9.
- **Whole-book close (R9):** check_reconcile no hard failures (candidates only);
  KEEP-list diff-grep net delta 0 for shall/sanction/traitor/Juntong/Beiping;
  ~20 decided renderings consistent book-wide; rail-line drift (R8 flag)
  resolved (prose uses Jin-Pu/Ping-Han/Bei-Ning/Ping-Sui uniformly); deep audit
  10/10 faithful; qa_epub PASS + epubcheck 5.1.0 0/0/0/0. COMPLETION.md carries
  the honest before/after prose-quality statement.
- **Two mechanical catches this batch:** the number check flagged 三十五年 first
  rendered 1936 (should be 1946, Republic 35 + 1911) in ch40; the whole-book
  close caught three narration dates missed in the per-chapter passes (ch36 p062,
  ch39 p041, ch40 p063). All five corrected and re-verified.
- **New noise.txt entry (R9):** `三十八、九` (ch40 p101, elided 1949-50; RULE
  R1-3). Do-not-revert. All prior R1-R8 noise entries stand.
- **Tooling do-not-revert:** kickoff_guard Stop hook; apply_edits.py OLD
  uniqueness contract; scripts/align_dump.py; every noise.txt entry.

## ⚠ COMMISSIONER DIRECTIVE (2026-08-22): the FOOTNOTE-DENSITY pass (F0) IS NOW DUE

With the register pass complete, F0 is the next and (per the current plan) final
pass. It **greatly increases footnote density** across the EPUB: explain the
little references, people, places, terms, events, and allusions a non-specialist
Western reader would miss. Density is a reader model, not a quota — **never add
a note just to add one**, but be generous. It is authored as a SINGLE final wave,
F0, one session over the whole book, canon in **REVISION_PLAN.md §12** (also
transcribed in `CORRECTIONS.md`). Do ch01 first as the density exemplar and pause
once (§12.4) to present it; then run to completion. Only after F0 is the book
COMPLETE, at which point COMPLETION.md is rewritten and this handoff is marked
COMPLETE.

---

# Completion record (translation + register pass, preserved)

**THE TRANSLATION IS FINISHED and the R1-R9 REGISTER PASS IS FINISHED.** The full
completion report is `COMPLETION.md` (read that for detail, including the register
pass before/after assessment). This page is the one-screen summary.

## What was delivered

- **`out/nameless-heroes.epub`** — the whole memoir, 43 of 43 units, register-
  revised, committed with `git add -f` on branch `claude/nameless-heroes`.
- **43/43 chapters translated**, clean pending-aware TOC, complete coverage.
- **375 translator notes**, 0 source notes (the source carries none of its own).
- **Glossary: 708 rows.** 0 in-text figures; the source's cover reused
  byte-identical.

## Final gate results (after R9)

- `qa_epub`: **PASS** — 57 files, 50 documents, 375 note references / 375 bodies
  / 375 backlinks, all links resolve.
- epubcheck 5.1.0: **0 fatals / 0 errors / 0 warnings / 0 infos** (EPUB 3.3).
- Whole-book scripted checks green: parity 6,160/6,160; numbers 0 unresolved;
  register within tolerance of `reference/R1_frozen.md` (documentary/near-zero-
  dialogue chapters read STILTED, the known false positive); content displacement
  limited to the documented homograph/substring false positives.
- Deep audit: R9 re-ran the protocol on 10 fresh edited pairs, 10/10 faithful,
  zero substantive errors; the pre-pass fixed-seed 45-pair sample was 44/45.

## Anything a later reader/commissioner should know

- The register pass converted narration dates book-wide to Gregorian/American;
  quoted documents keep their period register and dates by design.
- Provisional romanizations remain flagged `provisional` in the glossary
  (listed at the end of `out/term_ledger.md`); F0 may firm some up as it
  fact-checks, but that is not its main charge.
- The clean-checkout rebuild commands are in COMPLETION.md ("Provenance and
  method").

*Do not mark this file COMPLETE until the F0 footnote pass is finished.*
