# HANDOFF: Nameless Heroes (英雄无名), Chen Gongshu. REGISTER REVISION PASS IN PROGRESS

**The translation is COMPLETE (the record is preserved below), and the
commissioner has ordered a whole-book REGISTER REVISION PASS. The authority
for the pass is `REVISION_PLAN.md`; where it and this file disagree, the plan
wins. Batches R1 through R13 run per the plan's §8 schedule; each batch
session updates the kickoff block below for the next one.**

## Message to paste into the next chat

```
Nameless Heroes R2: register revision pass

Branch: claude/nameless-heroes ONLY. First acts: git fetch origin
claude/nameless-heroes && git checkout claude/nameless-heroes && git
reset --hard origin/claude/nameless-heroes. If the harness started you
on a stray branch, consolidate and delete it per CLAUDE.md rule 2.
Never read any other branch.

Read CLAUDE.md, then REVISION_PLAN.md IN FULL (it is the authority for
this pass), then run ./setup.sh.

Scope this batch: ch07, ch08. Content is frozen; English-to-English
register edits only, per REVISION_PLAN.md §3 (defect classes T1–T6,
KEEP list) and §5 (method, exactly). Edits via edits/<id>_edits.md +
apply_edits.py; verify_unit + tic battery before/after per chapter;
spot-audit 10% of edited paragraphs; check_register --ref
reference/R1_frozen.md; rebuild + qa_epub; commit and push at chapter
boundaries.

End of batch: PROGRESS.md updated (tic tables, spot-audit, rejected
findings), HANDOFF.md kickoff updated, and the reply carries BOTH chat
deliverables: the rebuilt EPUB attached AND the next batch's kickoff
pasted verbatim in a fenced code block. Run to completion; no mid-batch
approval stops.
```


## Revision pass state (after R1)

- **DONE:** R1 (ch06, the exemplar): 260 register edits + 1 note-anchor move
  via `edits/ch06_edits.md`; all gates green (parity 322/322, numbers 0,
  anchors 24/24, align OK, content clean); spot-audit 21/21 faithful; tic
  table and full findings in PROGRESS.md §R1; revised ch06 frozen as
  `reference/R1_frozen.md` (the register reference for R2–R13).
- **AWAITING:** the exemplar gate (REVISION_PLAN.md §9). Approval = the
  commissioner pastes the R2 kickoff above into a fresh chat. Corrections
  typed in the R1 chat become §3.5 rules; ch06 is then re-revised and
  re-presented.
- **Carry-forward for R2:** voice sheets seeded in REVISION_PLAN.md §3.4
  (Chen-in-scene, Dai Li, Zheng Jiemin, Wang Tianmu, Wu Youquan, and the
  quasi-official recruiting voice); T3 rule as practiced in ch06 — recurring
  decided terms plain after their book-first quoted use; quotes stay at
  naming constructions, name-as-name, anatomized words, marked irony,
  quoted documents, and note-anchor sites. New noise.txt entries: 五官,
  四个大字. R13 reconciliation flags logged in PROGRESS.md §R1 (Baomiju
  rendering, storey/story, "political operation").
- **Tooling do-not-revert:** kickoff_guard Stop hook; apply_edits.py OLD
  uniqueness contract; the R1 noise.txt entries above.

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
