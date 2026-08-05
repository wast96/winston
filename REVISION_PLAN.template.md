# REVISION_PLAN.md — whole-book revision pass (template)

Copy this file to `REVISION_PLAN.md` when the commissioner's read of the
finished book produces style or annotation feedback. Fill every section IN
ORDER; the structure is the merged shape of the two revision passes that
actually worked. Where `HANDOFF.md` disagrees with this plan, this plan wins;
the handoff predates the revision.

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

1. Read zh and en in ALIGNED chunks of 40-60 paragraphs. Do not skim only the
   English; half the value is catching quiet fidelity drift (the only real
   fidelity defects either revision pass found were invisible to an
   English-only read).
2. Write the edit list to `edits/<id>_edits.md` in the apply_edits.py grammar
   (OLD occurs exactly once; NOTE-ANCHOR pairs for any anchor an edit breaks;
   NOTE-ADD blocks for new notes). Collect footnote candidates in the SAME
   read, not a second one.
3. Apply mechanically: `python3 scripts/apply_edits.py <id>`. If an edit
   cannot apply cleanly, skip it and log why; never improvise a third wording.
4. `python3 scripts/verify_unit.py <id>`. Next chapter.
5. Spot-audit 10% of edited paragraphs (min 10) against the source for
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

Batches balanced by paragraph count, not chapter count. NO subagent fan-out:
a real attempt burned the session budget on agents re-reading shared context;
sequential in-session work is cheaper and easier to keep uniform. If the
session dies: stop at a chapter boundary, commit, push, deliver, and record
the exact resume point ("polished through chNN; notes integrated through
chNN").

## 8. Exit checklist (copy into each batch log)

- [ ] every edited chapter verify_unit green
- [ ] typography guard clean
- [ ] build green, qa_epub PASS
- [ ] spot-audit recorded
- [ ] cross-chapter reconciliation on the final batch (grep-count decided
      renderings; epithet drift; first-appearance mismatches)
- [ ] EPUB attached in chat + kickoff for the next revision batch pasted

## 9. Verbatim kickoff messages

<pre-write the kickoff block for every planned revision batch here>
