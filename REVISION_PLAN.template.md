# REVISION_PLAN.md — whole-book revision pass (template)

Copy this file to `REVISION_PLAN.md` when the commissioner's read of the
finished book produces style or annotation feedback. Fill every section IN
ORDER; the structure is the merged shape of the register passes that actually
worked (the shelf has now run four). Where `HANDOFF.md` disagrees with this
plan, this plan wins; the handoff predates the revision.

MID-BOOK CASE. If the register feedback arrives while chapters remain
untranslated, do NOT run this pass yet. Freeze the new rules into
`STYLE.local.md`, draft every remaining chapter against them so the back half
is congruous, and run ONE mechanical sweep over the earlier chapters at the
end. Fixing drift and then re-introducing it while drafting doubles the work;
this sequencing is a commissioner-stated process rule from the book that hit
the case.

## 1. State of play — what is DONE, do not redo

<one line per completed batch; note counts; checks green; the exact commit of
the last content change. Content is FROZEN: this is a style and annotation
pass, not a retranslation. Source lines are never touched, no paragraph is
merged or split, no name is re-romanized outside an explicit correction.>

## 2. Hard invariants, each with the command that checks it

- Paragraph parity: `python3 scripts/verify_unit.py <id>` per chapter.
  Do NOT batch verification to the end.
- Numbers: included in verify_unit (`--noise data/noise.txt`).
- Anchors: included in verify_unit; paired NOTE-ANCHOR edits for any anchor a
  prose edit breaks.
- Typography guard: `grep -n "[\"']" out/<id>_reading.md` prints nothing
  (or is normalized at the render layer; state which).
- Build + `qa_epub.py` after each batch of chapters.
- Known-benign warnings pinned HERE by exact location: <e.g. smart_quotes
  unbalanced-doubles at ch02:263, ch03:197 are legit multi-paragraph
  quotations>. Anything else, investigate; a "known" warning class once hid a
  genuinely dropped closing quote.

## 3. The register target

3.0 The measured calibration baseline, BEFORE any editing: run
`python3 scripts/register_tics.py --profile`, date the table, and paste it
here. Those counts are the state to improve, the sizing basis for the
batches, and the regression baseline every batch is re-measured against.
Both real register passes started here; a pass planned without measurement
over-predicts defect density by an order of magnitude.

3.1 A falsifiable voice test: <e.g. "could a good contemporary translator of
Mo Yan have written this sentence?">. Quote the commissioner's brief verbatim.

3.2 Defect classes, each with 2-3 LIVE `file:line` examples from this book
(examples, not a to-do list), each with its CAUTION carve-out:
- calqued idioms rendered image-by-image
- transferred Chinese syntax / over-literal images
- fake-antique verb forms, archaic adverbs and particles
- stilted inversion
- wrong-register dialogue (per-character voice spec here)
- pronoun fog in action scenes
- doubled / over-explained renderings
- scare quotes past first occurrence
- scene cards / datelines not yet set off

3.3 An explicit KEEP list: decided renderings, structurally deliberate
repetition, set-off conventions, anything inside a note anchor, deliberately
stiff speakers, quoted documents, classical tags and oaths, characters who
name themselves in the third person. A mechanical pass WILL over-correct 2-3
of these; search the diff for them afterward.

## 4. Triage discipline

One verdict per paragraph: LEAVE / TOUCH / RECAST. Expected distribution:
MOST paragraphs LEAVE. Both real revision passes predicted roughly ten times
more defects than they found; several chapters were entirely clean. A rewrite
that only shuffles synonyms is a defect in the edit list. Calibrate on an
exemplar first: revise one chapter, commit it, and require every later batch
to read that diff as the target.

## 5. Method per chapter (do it exactly like this)

1. `python3 scripts/register_tics.py <id>` for the grep candidates, each
   adjudicated against the KEEP list and the read-aloud test.
2. BLIND CRITIQUE, per unit: `python3 scripts/voice_gate_critique.py prepare
   <id>`, hand `out/<id>_critique_prompt.md`'s contents to ONE fresh
   context-free subagent (no source, no STYLE, no glossary, no project
   context; the blindness is the point), archive with
   `voice_gate_critique.py record <id> <file>`. The blind reader hunts what
   greps cannot. This is the one sanctioned use of a subagent in the pass
   (it must not share context by design); all editing stays in-session and
   sequential. Where the blind reader misread only for lack of the source,
   or flagged something on the KEEP list, record why and skip.
3. Read zh and en in ALIGNED chunks of 40-60 paragraphs. Do not skim only the
   English; half the value is catching quiet fidelity drift (the only real
   fidelity defects any revision pass found were invisible to an
   English-only read).
4. Write the edit list to `edits/<id>_edits.md` in the apply_edits.py grammar
   (OLD occurs exactly once; NOTE-ANCHOR pairs for any anchor an edit breaks;
   NOTE-ADD blocks for new notes). Collect footnote candidates in the SAME
   read, not a second one.
5. `python3 scripts/anchor_check.py <id>`: fix every collision in the edit
   list BEFORE applying (the builder's refusal is the backstop, not the
   check).
6. Apply mechanically: `python3 scripts/apply_edits.py <id>`. If an edit
   cannot apply cleanly, skip it and log why; never improvise a third wording.
7. `python3 scripts/verify_unit.py <id>`, and `register_tics.py <id>` again
   as the regression read against the 3.0 baseline. Next chapter.
8. Spot-audit 10% of edited paragraphs (min 10) against the source for
   meaning drift; record in PROGRESS.md.

## 6. Footnote expansion protocol

- The reader model from CLAUDE.md governs; coverage-driven, not a quota, and
  density tapers hard in the back half once the furniture is covered.
- First-appearance discipline: before adding a note, grep notes.json AND the
  earlier reading files; note goes at FIRST appearance, cross-reference later.
- The glossary is the quarry: list every glossary row with a substantive note
  and the first chapter its rendering appears in; that list IS the per-chapter
  candidate sheet. The footnote must say MORE than the glossary row.
- Build a subject bank (30-60 named subjects) up front so the hunt is
  recall-driven, not improvised.

## 7. Batch structure and contingency

Batches balanced by paragraph count, not chapter count. NO subagent fan-out
(the per-unit blind critic in section 5 is the sole, context-free exception):
a real attempt burned the session budget on agents re-reading shared context;
sequential in-session work is cheaper and easier to keep uniform. If the
session dies: stop at a chapter boundary, commit, push, deliver, and record
the exact resume point ("polished through chNN; notes integrated through
chNN").

Optional role split for a long pass run across sessions: ANALYZE (reads a
chapter against the source, produces the committed edit list) and EXECUTE
(applies the list exactly, runs every check, rebuilds, delivers). One book ran
its whole register pass this way; the split keeps the judgment work and the
mechanical work separately auditable. Calibrate on an exemplar chapter first
either way and require every later batch to read that diff as the target.

## 8. Exit checklist (copy into each batch log)

- [ ] every edited chapter verify_unit green
- [ ] anchor_check clean before every apply (no collision reached the builder)
- [ ] register_tics re-measured against the 3.0 baseline; movement recorded
- [ ] KEEP-list sweep of the diff (a mechanical pass WILL over-correct 2-3)
- [ ] typography guard clean
- [ ] build green, qa_epub PASS
- [ ] spot-audit recorded
- [ ] cross-chapter reconciliation on the final batch (grep-count decided
      renderings; epithet drift; first-appearance mismatches)
- [ ] EPUB attached in chat + kickoff for the next revision batch pasted

## 9. Verbatim kickoff messages

<pre-write the kickoff block for every planned revision batch here>
