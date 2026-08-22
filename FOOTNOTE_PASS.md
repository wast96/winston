# FOOTNOTE_PASS.md — the footnote-density pass for *Zhou Enlai: Commander of the Hidden Front*

Commissioner's instruction, 2026-08-22 (verbatim intent): "go through and
greatly, greatly, greatly increase the density of footnotes in the EPUB; don't
add footnotes just to add them, but make sure that you're explaining all the
little references, the people, etc. I want terms, people, places, events, etc.
explained."

This is a NEW pass, run AFTER the register revision pass (R1-R5) closes. It
overrides `REVISION_PLAN.md` section 6, which held footnotes out of scope; the
commissioner's instruction takes precedence. It follows the footnote doctrine
already written in `CLAUDE.md` ("Footnotes — what earns one") and `STYLE.md`
("Apparatus"); read both before starting. Where this file and those disagree on
mechanics, they win on mechanics and this file wins on the density target.

Runs on branch `claude/zhou-enlai` only. Content is FROZEN: this pass adds and
enriches NOTES; it does not touch the reading prose, numbers, names, or
paragraph structure. (No prose changes were requested and none are made — a
richer note is the deliverable, not a reworded sentence.)

## 1. The target, stated so it is falsifiable

Today: 339 notes across 28 units (1-28 per chapter, ~12 average). The book is
already annotated for the biggest references; this pass takes it from
"the major references are covered" to "a non-specialist Western reader never
hits a name, place, event, office, term, or allusion they cannot place."

The reader to hold in mind (unchanged from CLAUDE.md): **a native English
speaker with no Chinese and no background in Chinese history, culture, or
geography.** After this pass, such a reader should be able to read any chapter
and, at every proper noun and every period term, either already know it or find
a note that places it.

**The one hard rule the commissioner set: density is coverage, not quota.**
"Don't add footnotes just to add them." Every note must carry real, checked
content and answer a real reader question. A note that only restates the
sentence, or glosses a word any English reader knows, is padding and does not
ship. The test for ADDING a note is the reader-need test below; the test for
KEEPING it is "does the body tell the reader something true they needed and did
not have?" If the honest answer to the second is no, cut it.

## 2. What earns a note in THIS pass (the reader-need sweep)

For each chapter, sweep these classes deliberately and annotate every instance
a non-specialist would miss, at its FIRST appearance in the book:

1. **People.** Every named person on first appearance: who they were, their
   role in this history, dates if knowable, and (for a claim about them) the
   fact-check verdict. This is the largest class and the most under-covered
   today: the book has a huge, fast-turning cast (Communists, Kuomintang
   officers, gangsters, foreign figures), and many are named once with no gloss.
   Minor figures get a one-line placement ("X, a Red Squad member"); major ones
   get a real paragraph.
2. **Places.** Cities, districts, streets, foreign Concessions, buildings,
   provinces, native places, prisons, venues. A Western reader does not know
   where Zhabei is, what "Route Ghisi" was, why the Concessions mattered, or
   that a native place carries social weight. Gloss the geography and, where it
   bears on the action (a refuge across a Concession line, a garrison town),
   say why.
3. **Events.** Every dated or named event and campaign: the April 12 coup, the
   Central Plains War, the "encirclement and suppression" campaigns, the
   Fujian Incident, the December 12 Incident, the May Thirtieth Movement, the
   Bose Uprising, the various plenums. Give the year, the one-sentence what, and
   the bearing on the story.
4. **Institutions, offices, ranks, units.** Party and state organs (the
   Politburo, the Comintern's Far Eastern Bureau, the Zhongtong/Juntong, the
   Executive Yuan, Academia Sinica, the concession police), military
   designations, official titles, and the numeral-bearing unit names. Explain
   what the body did and where it sat in the hierarchy.
5. **Terms and period vocabulary.** Charged political lexicon (already partly
   glossed), currency (silver dollars, yuan, "loads" of medicine), material
   culture (clothing, food, objects, transport), the "yellow-fish" and
   underworld argot, honorifics and forms of address, custom and belief.
6. **Allusions, idioms, wordplay, quotations.** Classical citations (Sun Tzu is
   done; sweep for others), chengyu whose picture matters, name-glyph puns (the
   book has them, e.g. 虎狼成群 on Yang Hu and Chen Qun), literary or operatic
   references, and any quoted work (memoirs, essays, the books the Kuomintang
   agents later wrote) — identify the source.
7. **The author as interested witness.** Where Mu Xin's account is self-serving,
   shaped by its political moment, or contradicted by independent scholarship,
   the note says so with evidence. This is not new density for its own sake; it
   is the partisan-source discipline (STYLE.md) applied at more sites.

Do NOT annotate: words a general English reader knows; things already noted
earlier in the book (cross-reference instead); the author's plain narration
where nothing is missing. The deliberately-unfootnoted tier of minor low-stakes
discrepancies (named in PROGRESS) stays unfootnoted unless the commissioner asks.

## 3. The glossary is the quarry (and the first-appearance map)

`glossary.json` has 847 rows — every one is a rendered referent that recurs.
For each chapter:
- Pull the glossary rows whose zh appears in this chapter's `data/zh`.
- Any row with substantive content and no existing note at its first textual
  appearance is a footnote candidate. The note must say MORE than the glossary
  row (the row decides the rendering; the note tells the reader who/what/why).
- `qc_entities.py` already maps which entities appear where; use it to find
  first appearances fast.

## 4. First-appearance discipline (do not re-note)

Recurring subjects get ONE note, at first appearance book-wide. Before adding
any note:
1. `grep` the subject in `notes.json` AND in all earlier `out/ch*_reading.md`.
2. If it is already noted earlier, add nothing; if this chapter is the FIRST
   appearance and an earlier note is wrongly placed later, move it here.
3. Keep a per-batch **"NOT re-noted (already placed)"** list in PROGRESS.md,
   exactly as the register/translation batches did.
4. Prefer a cross-reference ("see the note on X at its first appearance") to a
   second note on the same subject.

Because this pass adds notes to chapters whose neighbors are already annotated,
the first-appearance check is the main guard against redundancy. Run it every
time.

## 5. Fact-checking (CLAUDE.md rule 5 — non-negotiable)

- Check every factual claim against REAL scholarship: Wikipedia, Baidu Baike,
  academic sources. **NEVER** cite Grok/Grokipedia or any AI-written reference.
- State the verdict IN the note: corroborated / uncorroborated / contradicted,
  with the source. A contradicted source claim stays faithful in the prose and
  is footnoted, never silently corrected.
- Repetition is not corroboration; trace a claim to its earliest source; say
  when sources conflict; leave the source language where the record does.
- `data/check_config.json` already holds docs + sources for ch00-ch27; extend it.
- **Proofread every hanzi you insert into a note, character by character,
  against the glossary or the scan** (STYLE.md round-2 rule; two glosses once
  shipped wrong characters). Never trust your own character insertion.
- Never invent. Where the record is silent or the scan is unreadable, the note
  says so; leave the gap honest. Invented precision is the deadly error.

## 6. Mechanics (apparatus-only; content frozen)

- Author each batch's notes as a plain JSON file (the Write tool, NEVER a shell
  heredoc), then merge with `python3 scripts/apparatus_merge.py <file>.json`.
  Shape: `{"notes": {"<unit_id>": [{"anchor": ..., "note": ...}, ...]}}`.
  (glossary/figures keys optional; this pass is notes-first.)
- **Anchors are verbatim substrings of `out/<unit>_reading.md`**, verified at
  write time (apparatus_merge refuses otherwise; the builder's refusal is the
  backstop). Anchors may sit on section headings. Pick a stable, unique anchor
  phrase; if a phrase occurs twice in a unit, lengthen it.
- Note bodies are XHTML: `<i>` for emphasis, NUMERIC character references only
  (`&#160;`, `&#8212;`), never named entities. No U+FFFD.
- **Always cite the book's own PRINTED FOLIO** in a note, never the PDF page.
- Numbering is continuous book-wide and assigned by the builder; note markers
  sit after closing punctuation.
- `check_apparatus.py` must be clean after each merge; the builder REFUSES to
  build on an unmatched anchor.

## 7. Batch structure (one batch = one conversation, per CLAUDE.md)

The book is annotated front to back so the first-appearance ledger builds in
reading order. Five batches, sized like the register pass:

- **FN1 — ch00-ch05** (Preface, the Section's founding, the early intelligence
  heroes, the Longtan Three). The densest cast-introduction stretch; it sets the
  density calibration and the "NOT re-noted" ledger. Deliver FN1 and let the
  commissioner see the new density on a first chapter before FN2 (a light voice
  gate for annotation: is this the right depth, or too much / too little?).
- **FN2 — ch06-ch11** (Yang Deng­ying, the tiger's den, Fengtian, the Action
  Section and Red Squad, the Avenue Joffre gunfights).
- **FN3 — ch12-ch17** (the manhunt aftermath, the Ren Bishi rescue, the "new
  chapter" trio, the radio and communications chiefs).
- **FN4 — ch18-ch22** (the radio men, the Gu Shunzhang defection and its
  averting, the manhunts — testimony-dense, so many quoted figures to place).
- **FN5 — ch23-ch27 + whole-book apparatus reconciliation.** Annotate the tail,
  then: re-grep the whole book for un-noted first appearances the per-batch
  sweeps missed; confirm no subject is double-noted; verify every note's folio;
  refresh `out/term_ledger.md`; update COMPLETION.md with the new note count and
  the density record. Final EPUB committed with `git add -f`.

Each batch: notes authored + merged, `check_apparatus.py` clean, cumulative EPUB
rebuilt, `qa_epub.py` PASS (epubcheck when installed), PROGRESS + CHANGELOG
entries, commit, push to `claude/zhou-enlai`, **EPUB attached in chat AND the
next FN kickoff pasted verbatim** (the two chat deliverables, per CLAUDE.md).

## 8. Exit checklist (copy into each batch log)

- [ ] reader-need sweep run over all six classes for each chapter in the batch
- [ ] first-appearance check run for every new note; "NOT re-noted" list recorded
- [ ] every factual claim fact-checked against real scholarship, verdict in note
- [ ] every inserted hanzi proofread character-by-character
- [ ] folios cited from the printed page, not the PDF
- [ ] `check_apparatus.py` clean; no unmatched anchors
- [ ] build green, qa_epub PASS (epubcheck when installed)
- [ ] notes.json note count recorded (before → after) in PROGRESS
- [ ] EPUB attached in chat + next FN kickoff pasted verbatim
- [ ] FN5 only: whole-book reconciliation, COMPLETION.md density record, final
      EPUB committed

## 9. Kickoff (paste this to start FN1)

```
Zhou Enlai FN1 (footnote-density pass)

Read CLAUDE.md, then FOOTNOTE_PASS.md (it governs this pass), then STYLE.md ("Apparatus" and the partisan-source discipline). Branch claude/zhou-enlai only; fold any stray branch per CLAUDE.md rule 2. Content is FROZEN: this pass ADDS and enriches footnotes only, no prose/number/name/paragraph change. Notes are authored as a JSON file and merged with scripts/apparatus_merge.py (never a heredoc); anchors are verbatim substrings of out/<id>_reading.md; bodies are XHTML with numeric character references only; cite printed folios; never invent, fact-check against real scholarship (never LLM-sourced) with the verdict stated in the note. If data/zh is missing, regenerate per scripts/recovery/README.md and verify_unit green first.

Do batch FN1 = greatly increase footnote density on ch00-ch05 per FOOTNOTE_PASS.md sections 2-6: sweep every chapter for people, places, events, institutions/offices/ranks/units, terms and period vocabulary, and allusions/idioms/quotations, and annotate every instance a non-specialist Western reader would miss AT ITS FIRST appearance book-wide. Density is coverage, not quota: every note carries real checked content and answers a real reader question; add nothing just to add it. Use the glossary (847 rows) as the quarry; run the first-appearance check (grep notes.json + earlier reading files) before every note and keep the "NOT re-noted" list in PROGRESS. Then rebuild, check_apparatus.py, qa_epub (epubcheck if installed), PROGRESS + CHANGELOG, commit, push.

STOP after FN1 and present the newly dense first chapters to the commissioner as a light annotation-depth gate (right depth, too much, or too little?) before FN2. Do not pause for approval mid-batch otherwise. End with the rebuilt EPUB attached in chat AND the FN2 kickoff pasted verbatim in a fenced block (draft it in the same form as this one, ch06-ch11).
```

The FN2-FN5 kickoffs follow the same template (swap the chapter range and the
one-line focus from section 7); the running session drafts each next kickoff at
the end of its batch, as the register pass did. FN5's kickoff must also carry
the whole-book apparatus-reconciliation and close-out tasks from section 7.
