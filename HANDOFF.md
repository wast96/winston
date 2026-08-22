# HANDOFF: Nameless Heroes (英雄无名), Chen Gongshu. REGISTER REVISION PASS IN PROGRESS

**The translation is COMPLETE (the record is preserved below), and the
commissioner has ordered a whole-book REGISTER REVISION PASS. The authority
for the pass is `REVISION_PLAN.md`; where it and this file disagree, the plan
wins. Batches R1 through R9 run per the plan's §8 schedule; each batch
session updates the kickoff block below for the next one.**

## Message to paste into the next chat

```
Nameless Heroes R3: register revision pass

Branch: claude/nameless-heroes ONLY. First acts: git fetch origin
claude/nameless-heroes && git checkout claude/nameless-heroes && git
reset --hard origin/claude/nameless-heroes. If the harness started you
on a stray branch, consolidate and delete it per CLAUDE.md rule 2.
Never read any other branch.

Read CLAUDE.md, then REVISION_PLAN.md IN FULL (it is the authority for
this pass), then run ./setup.sh.

Scope this batch: ch01–ch05, ch09, ch10 (front matter is light-touch).
Content is frozen; English-to-English register edits only, per
REVISION_PLAN.md §3 (defect classes T1–T6,
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


## Revision pass state (after R2)

- **DONE:** R1 (ch06, exemplar, frozen as `reference/R1_frozen.md`). R2 (ch07,
  ch08): ch07 86 edits, ch08 65 edits via `edits/ch07_edits.md` /
  `edits/ch08_edits.md` + `apply_edits.py`; all fidelity gates green (ch07
  parity 362/362, ch08 461/461; numbers 0; anchors 11 & 13; align OK; content
  clean bar the documented ch08 Shunde substring FP); spot-audits clean (2
  slips caught and fixed: ch07 p162 "in detail", ch08 p346 顾虑 nuance);
  qa_epub PASS + epubcheck 0/0/0/0. Full tic tables + findings in PROGRESS.md
  §R2. **ch08 check_register STILTED is a documented false positive** (its
  "speech" is dominated by quoted documents + deliberately-formal speakers;
  see PROGRESS §R2 and references/register-drift.md §§1-2) — do not chase it
  by contracting formal/document speech.
- **Carry-forward for R3+:** voice sheets in REVISION_PLAN.md §3.4; T3 rule as
  practiced — recurring decided proper names/orgs plain in narration after
  book-first use; quotes stay at naming/anatomizing sites, marked irony,
  titles, code names, quoted documents, dialogue, note-anchor sites. R3 front
  matter (ch01-05) is light-touch (closest to target already). Generate T3
  quote-strips programmatically (byte-exact OLD, uniqueness pre-checked) and
  skip whole quoted-document/dialogue paragraphs.
- **New noise.txt entry (R2):** `三、四两` (enumerated pair + recap 两; see
  PROGRESS §R2) — do-not-revert. Earlier R1 entries 五官, 四个大字 also stand.
- **Tooling do-not-revert:** kickoff_guard Stop hook; apply_edits.py OLD
  uniqueness contract; the noise.txt entries above.
- **R9 (whole-book close) reconciliation flags** logged in PROGRESS §R1 (Baomiju, storey/story,
  "political operation") and §R2 (ch07 one-off hotel names; ch08 group-name /
  special-commissioner / inspectorate-system quoting).

## ⚠ COMMISSIONER DIRECTIVE (2026-08-22): a FOOTNOTE-DENSITY pass (F0) AFTER R9

The commissioner has ordered an additional final pass, **after the whole R1-R9
register revision is complete**, to **greatly increase footnote density** across
the EPUB: explain the little references, the people, places, terms, events, and
allusions a non-specialist Western reader would miss. Density is a reader model,
not a quota — **never add a note just to add one**, but be generous: terms,
people, places, events, and references should be explained. This is authored as
a single final wave, **F0** (one session over the whole book), with its
canon in **REVISION_PLAN.md §12**. When R9 completes the register pass, the R9
reply must serve up the **F0 kickoff** (not a "book complete" notice); the directive
and its kickoff are transcribed in `CORRECTIONS.md` and REVISION_PLAN.md §12 so
they survive every batch seam. Carry this note forward in every HANDOFF until
the footnote pass is itself complete.

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
