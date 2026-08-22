# HANDOFF: Nameless Heroes (英雄无名), Chen Gongshu. REGISTER REVISION PASS IN PROGRESS

**The translation is COMPLETE (the record is preserved below), and the
commissioner has ordered a whole-book REGISTER REVISION PASS. The authority
for the pass is `REVISION_PLAN.md`; where it and this file disagree, the plan
wins. Batches R1 through R13 run per the plan's §8 schedule; each batch
session updates the kickoff block below for the next one.**

## Message to paste into the next chat

```
Nameless Heroes R01: register revision pass, EXEMPLAR batch (ch06) + gate

Branch: claude/nameless-heroes ONLY. First acts: git fetch origin
claude/nameless-heroes && git checkout claude/nameless-heroes && git reset
--hard origin/claude/nameless-heroes. If the harness started you on a stray
branch, consolidate and delete it per CLAUDE.md rule 2. Never fetch, check
out, read, or diff any other branch; REVISION_PLAN.md is self-contained.

Read CLAUDE.md, then REVISION_PLAN.md IN FULL (it is the authority for this
pass), then run ./setup.sh.

Scope this batch: ch06 ONLY, the exemplar. Content is frozen;
English-to-English register edits only, per REVISION_PLAN.md §3 (defect
classes T1-T6, KEEP list) and §5 (method, exactly):
1. Tic battery before (bash scripts/revision_tics.sh ch06); read zh/en
   aligned; triage LEAVE/TOUCH/RECAST; write edits/ch06_edits.md; apply via
   scripts/apply_edits.py ch06.
2. Seed the voice sheets into REVISION_PLAN.md §3.4 as you meet the
   speakers.
3. verify_unit ch06; tic battery after; tail check against the source;
   spot-audit 10% of edited paragraphs.
4. Blind-critique the REVISED chapter (plan §5 step 6); adjudicate
   ACCEPT/REJECT-with-reason in PROGRESS.md; fold real findings into the
   edits and the plan's §3.5.
5. Freeze the revised ch06 as reference/R1_frozen.md; smoke-test
   scripts/check_register.py --ref reference/R1_frozen.md.
6. Rebuild, qa_epub green, update PROGRESS.md and this HANDOFF kickoff,
   commit, push.

Then STOP at the exemplar gate (REVISION_PLAN.md §9): the final reply
presents 8-12 before/after excerpt pairs spanning T1-T6, the ch06 tic
before/after table, the rebuilt EPUB ATTACHED, and the R2 kickoff (plan §11
canon, scope ch07 + ch08) pasted VERBATIM in a fenced code block. Do NOT
begin R2. The commissioner either pastes the R2 kickoff into a fresh chat
(approval) or types corrections in this chat; corrections become §3.5 rules,
ch06 is re-revised and re-presented here.
```

---

# Completion record (pre-revision, preserved)

**THE TRANSLATION IS FINISHED. What follows is the completion notice from
B36, kept for the record; the revision pass above supersedes its "no next
batch" instruction. A correction pass, if ever needed, is still governed by
`CORRECTIONS.md`.**

The full completion report is `COMPLETION.md`; read that for the detail. This
page is the one-screen summary.

## What was delivered

- **`out/nameless-heroes.epub`** — the whole memoir, 43 of 43 units, committed
  with `git add -f` on branch `claude/nameless-heroes`.
- **43/43 chapters translated**, clean pending-aware TOC (no placeholder),
  complete coverage.
- **375 translator notes**, 0 source notes (the source carries none of its own).
- **Glossary: 708 rows** (people 479, organizations 71, places 132, terms 26).
- **0 in-text figures**; the source's single image (its cover) is reused
  byte-identical.

## Final gate results

- `qa_epub`: **PASS** — 57 files, 50 documents, 375 note references / 375 bodies
  / 375 backlinks, all links resolve.
- epubcheck 5.1.0: **0 fatals / 0 errors / 0 warnings / 0 infos** (EPUB 3.3).
- Whole-book scripted checks green: parity 6,160/6,160; numbers 0 unresolved;
  register within tolerance of the frozen reference `reference/B01_frozen.md`;
  content displacement limited to the documented homograph/substring false
  positives (ch08 Shunde, ch09 Jize, ch13, ch26, ch38, ch41 — none real).
- Deep audit (`out/deep_audit.md`): fixed-seed 45-pair sample, 44/45 fully
  faithful, zero substantive errors; one title nuance found and fixed.

## Completion work done in the final batch (B36)

- Translated ch43, the Afterword (英雄无名 篇后续话) — a reflective coda over the
  whole five-book memoir, 31 paragraphs, 3 notes, Chen's grave register with the
  deliberate narrating "shall" preserved.
- **Spelling locale unified to American** across prose, notes, and glossary
  (was mixed 736:38; now 0 British / 774 American).
- **张垣 / 张家口 reconciled** to Zhangyuan / Zhangjiakou book-wide, with a
  first-appearance city note at ch08.
- **`authority.json` fed back** under slug `nameless-heroes` (399 new terms, 43
  agreements, 1 honestly-flagged disagreement).
- Wrote `out/term_ledger.md`, `out/deep_audit.md`, and `COMPLETION.md`.

## Anything a later reader/commissioner should know

- Two items were **documented, not silently changed** (see COMPLETION.md
  "Findings that need the commissioner's eye"): 宋子文 rendered pinyin
  "Song Ziwen" where the shelf uses "T. V. Soong" (glossary note bridges it);
  and 制裁/sanction, used from ch02 but formally defined in the ch04 note.
- **Provisional romanizations remain to firm up** (241 people, 19 places, 5
  organizations), each flagged `provisional` in the glossary and marked in the
  build; listed at the end of `out/term_ledger.md`.
- **Tooling that must not be reverted** and the exact clean-checkout rebuild
  commands are in COMPLETION.md ("Provenance and method").

*Do not edit this file further. The book is complete.*
