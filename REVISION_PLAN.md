# REVISION_PLAN.md — register revision pass for *Zhou Enlai: Commander of the Hidden Front*

Filled from `REVISION_PLAN.template.md` on 2026-08-22, from the measured
findings in `review/REGISTER_PASS_ASSESSMENT.md` (read that first; this plan
operationalizes it). Where `HANDOFF.md` disagrees with this plan, this plan
wins; the handoff predates the revision. All work happens on branch
`claude/zhou-enlai` and only there.

This is a REGISTER pass, not a retranslation. It has three tiers of work
(assessment sections 3A-3C): mechanical consistency, a grep-driven tic sweep
confirmed by ear, and a small bounded set of judgment edits. It is NOT a
whole-book re-voice: the book already sits at or near the modern-register
targets on sentence length, narration contraction rate, exclamation
rationing, and em-dash rate. Expect most paragraphs to be LEFT alone.

## 1. State of play — what is DONE, do not redo

- The book is COMPLETE: 28/28 units, 339 notes, 36 figures, 847 glossary
  rows, qa_epub PASS, epubcheck 5.1.0 clean. Last content commit: `ea8103a`
  (B14 final). See COMPLETION.md.
- The whole-book reconciliation (QC check 12) already ran at B14: spelling
  locale standardized American ("Theatre" survives only in venue proper
  names, a recorded decision); cross-book renderings (Central Special
  Section, Kuomintang, Zhongtong, Juntong, White Terror, Wu Hao) verified
  uniform. Do not redo those sweeps; this pass adds the items B14 missed
  (dates, 政治局, the ledger residuals below).
- A 41-paragraph seeded deep audit found zero substantive errors. Fidelity
  is not in question; do not re-litigate renderings outside this plan's
  scope.
- Content is FROZEN: source lines are never touched, no paragraph is merged
  or split, no name is re-romanized, no fact or hedge changes. Every edit is
  an English-surface edit at an identified defect site.

## 2. Hard invariants, each with the command that checks it

- Paragraph parity, numbers, anchors: `python3 scripts/verify_unit.py <id>`
  per edited chapter, at the time of the edit, never batched to the end.
  PREREQUISITE: `data/zh/` is untracked and currently absent; R1 step (a)
  regenerates it for all 28 units per `scripts/recovery/README.md` (b02-b09
  re-OCR from source.pdf with the recorded crops; b10-b14 rebuild from
  `data/txt_backup_b*`), replays `data/ocr_fixes.json` via `apply_fixes.py`,
  and proves verify_unit green on all 28 units BEFORE any edit. That
  pre-flight is the clean-checkout regression run the corrections workflow
  requires anyway.
- Edits only via `edits/<id>_edits.md` applied by
  `python3 scripts/apply_edits.py <id>` (OLD occurs exactly once;
  NOTE-ANCHOR pairs in the same list as the prose edit that breaks an
  anchor; abort-not-improvise). Never hand-edit a reading file in this pass.
- Typography guard: reading files are plain ASCII plus em dashes; smart
  quotes happen at the render layer. Guard:
  `grep -nP '[“”‘’…]' out/<id>_reading.md` prints
  nothing. (Em dashes are allowed and present; do not "fix" them.)
- Tic battery: `bash scripts/register_tics.sh <id>` per unit; the goal state
  per unit is "every surviving hit defensible aloud", not zero hits.
- Build + `python3 scripts/qa_epub.py` after each batch; epubcheck when
  installed (`./setup.sh` fetches it).
- Register vs frozen reference: `python3 scripts/check_register.py --ref
  out/ch01_reading.md` on every edited unit. NOTE: ch01 itself receives
  Tier A/B edits in this pass; run check_register on the OTHER edited units
  against ch01's PRE-pass state if ch01 is edited in the same batch (keep a
  copy `out/ch01_reading.pre-R.md` from commit `a8dda4c` for the ref).
- Known-benign warnings (pinned by R1's pre-flight, 2026-08-22). The QC
  scaffold `data/zh/` is regenerated per unit; anything below is a
  regeneration artifact of THIS container (tesseract 5.3.4, vs the original
  build's tesseract), NOT a defect in the shipped English. Anything NOT on
  this list gets investigated, every time.
  - **26 of 28 units regenerate fully green** (parity + numbers + anchors):
    ch00, ch02, ch04&#8211;ch27. ch00 and ch02 were recovered by R1 (see the
    "do not revert" list); the rest reproduce from `scripts/recovery/`.
  - **ch01 and ch03: PARITY not reproducible in this container.** These are
    the two oldest batches (B01 front matter, B02) and predate the raw-OCR
    backup discipline (only b10&#8211;b14 have `data/txt_backup_b*`). Their
    character stream reproduces (apply_fixes replays the char fixes) but the
    tesseract-5.3.4 BLANK-LINE paragraph structure drifts from the build's:
    ch01 shows zh 32 vs en 38 (six OCR-welded paragraph boundaries; §2 welds
    are mapped, §3 is ambiguous and NOT force-split, because a wrong split
    yields a data/zh that passes parity while pairing the wrong lines &#8212;
    worse than an honest fail); ch03 shows zh 38 vs en 37 (a p83 photo-page
    body displacement the new OCR renders differently). The shipped book
    built green at B14; this is a scaffold-reproducibility limit only. R1's
    edits on ch01/ch03 are Tier A mechanical swaps (dates, Politburo, "in
    good time") that preserve numbers and paragraph count; they are verified
    by the zh-independent guard set: apply_edits (OLD-unique, structure- and
    anchor-preserving) + notes.json anchor grep + the builder's anchor
    refusal + a direct number/typography grep on each edit + check_register.
  - **Benign zh number-pairing artifacts** (parity OK, one unresolved
    number-pair each, all zh-side OCR/segmentation drift; the en is correct):
    `ch04` pair 37 (unaccounted `[7]`), `ch15` pair 36 (`[2,10,30,1948]`, an
    Edgar Snow memoir quote where a date landed in an adjacent zh paragraph),
    `ch16` pair 2 (`[0,5,6,7,8]`, OCR-garbled "龙华兵工厂"/1865 date). When an
    edited unit's verify_unit shows ONLY its pinned artifact, it is clean.

## 3. The register target

3.1 The falsifiable voice test, from STYLE.md and the rebaseline: could a
first-rate contemporary writer of popular narrative history have written
this sentence, unprompted, as original English? Supporting read-aloud test:
if you can hear a costume-drama butler in it, rewrite it; if you can hear
yourself saying it to a smart friend not in the field, it is done. Period
flavour comes from CONTENT (concessions, silver dollars, patrolmen, the
Green Gang), never from antique syntax. The narrator sounds like a smart
writer today; documents sound like documents; people sound like people.

3.2 Defect classes, live examples from THIS book, and the carve-out each
class must respect. Examples are illustrations, not the to-do list; the
to-do list is generated per unit by `register_tics.sh` plus the greps below.

- **Trailing/antique "besides" (87 hits).**
  `out/ch06_reading.md:15` "Zhang Daofan there was, besides,";
  `out/ch15_reading.md:139` "…and a hand of social intelligence besides."
  Fix: "as well," "too," or cut. CAUTION: sentence-initial "Besides, …" in
  informal narration or dialogue is modern and usually stands.
- **The 等 tag at fixed wording ("and the rest" 37, "and the others" 50).**
  `out/ch23_reading.md:131` and `:133` use it twice in adjacent paragraphs.
  Fix: vary ("among others"), restructure, or cut where the list is
  complete. CAUTION: inside quoted documents, render what the document says.
- **"one after another" (31 hits, the 纷纷/相继/陆续 calque).**
  `out/ch15_reading.md:11`, `out/ch18_reading.md:63`, `out/ch23_reading.md:29`.
  Fix: "in turn," "one by one," a plural verb, or cut. CAUTION: keep it
  where genuine sequence is the point and the rhythm holds; consult the
  source word (纷纷 wants "everywhere/in droves" more than sequence).
- **Litotes calques ("no few" 5, "no small" 15, "not a little").**
  `out/ch01_reading.md:81` "this is no small hindrance". Fix: "a good
  many," "considerable," "a real obstacle." CAUTION:
  `out/ch08_reading.md:39` "no small thing, that!" sits in quoted speech
  and keeps its flavour; quoted memoirs (`out/ch06_reading.md:77`) too.
- **"could only / could not but / could not help" (28 hits).**
  `out/ch04_reading.md:131` "he could only go back and hide". Fix: "had to,"
  or just the verb. CAUTION: idiomatic modern uses stand ("could only wait
  tables" `ch04:17` is fine); first-person quoted memoir ("I could only
  take my lumps" `ch05:40`) stands.
- **Antique stragglers.** `out/ch19_reading.md:55` "Presently Chiang
  Kai-shek came"; `out/ch20_reading.md:49` "thereupon"; `out/ch21_reading.md:27`
  "At length they announced"; `out/ch11_reading.md:59` "let slip not a
  moment". Fix: "soon," "then," "at that," "finally," "wasted not a
  moment." CAUTION: "let slip" meaning inadvertently reveal
  (`out/ch07_reading.md:37` "Xu Enzeng also let slip that…") is modern
  idiomatic English and stays. Also sweep by eye for the same register in
  phrases the battery cannot catch ("as ill luck had it" `out/ch21_reading.md:17`,
  "was given to startling acts" `out/ch15_reading.md:15`).
- **Nominalizations, "the [gerund] of the" (42 raw hits).**
  `out/ch00_reading.md:5` "the building of the Central Special Section";
  `out/ch02_reading.md:21` "The furnishing of the whole house, the food…".
  Fix: finite verbs, roughly two-thirds of the real hits. CAUTION: the grep
  false-positives on time expressions ("the morning of the 12th",
  `ch01:29`) and on the author's genuine heat ("the awakening of the
  Chinese people", `ch01:11`); leave both.
- **Ledger residuals (the book's own decided renderings, drifted).**
  "in good time" x16 (`out/ch03_reading.md:5`, `out/ch07_reading.md:39`)
  where the STYLE.md ledger decided 及时 = "in time / promptly"; "driving
  into the heart of the enemy" (`out/ch07_reading.md:39`) against 打入 =
  "plant inside / infiltrate". CAUTION: read each 及时 site; where the
  English sense is genuinely "before it was too late," "in time" alone
  suffices.
- **Narration ellipses (~20 raw "..." hits).** Fix: in narration, end the
  sentence. CAUTION: nearly all current hits are QUOTATION abridgment marks
  (the ch07 memoir passages, e.g. `out/ch07_reading.md:57`); STYLE.md
  ruling 8 keeps those. Expect only a handful of real narration hits.
- **Long-sentence spine test (34 narration sentences over 90 words).**
  Regenerate the list per unit (assessment section 3, or:
  split sentences, count words). Split ONLY where two or more finite spines
  load the reader; a single-spine colon-plus-list sentence passes at any
  length and a list is NEVER broken to shorten a sentence. Densest sites:
  ch19 (5), ch23 (3), ch24 (3), ch25 (3).
- **Elevated-antique narration drift in the biographical chapters.**
  ch15 and ch16 (the enlightened-gentry biographies) run a register the
  operational chapters do not: `out/ch15_reading.md:19` "he enjoyed no
  little standing in society"; `ch15:5` "he broke free at last of the old
  traditions". These two chapters get a full aligned zh-en read (ch15 as
  the R1 exemplar). CAUTION: the Yang Xianzhen memorial inscription
  (`ch15:9`-`13`) is a quoted document and keeps its formal register
  entirely; the drift to fix is the narration AROUND the quotes borrowing
  their register.

Global consistency items (Tier A, all in R1):

- **Date format.** 95 day-month dates ("23 July 1921") in ch00-ch05 and
  ch09-ch12 against 609 month-day ("May 21, 1931") in the rest. Normalize
  ALL to month-day ("July 23, 1921"). Mechanical and regexable; generate
  the edit lists by script, apply via apply_edits.py, and grep notes.json
  for any anchor containing a rewritten date string (NOTE-ANCHOR pairs).
  Ranges ("from 11 April into the morning of the 12th") are rewritten by
  hand at the same sites, not by the regex.
- **政治局: decide "the Politburo", cascade everywhere.** The glossary has
  NO entry (that is why it drifted): "Political Bureau" x51 (most
  chapters), "Politburo" x14 (ch19-ch20). DECISION for this pass: adopt
  **the Politburo** (the standard term in English-language CCP scholarship;
  reader-ease wins over decode). First occurrence in ch01 may keep one
  formal expansion ("the Political Bureau (Politburo)" or footnote wording
  per the existing note, checked at edit time), then "the Politburo"
  book-wide, including notes.json and glossary entries that mention it.
  Record the decision in glossary.json AND authority.json. If the
  commissioner prefers minimal churn ("Political Bureau" everywhere, 14
  edits instead of ~51), say so in the R1 chat before work starts; the
  plan's default is Politburo.
- **叛徒 variety check (investigate, do not pre-judge).** traitor 240 /
  renegade 29 / turncoat 11. In R5's reconciliation, sample ~15 sites per
  variant against the source: if the variation tracks distinct source words
  (叛徒/变节分子/叛逆), it stands and is recorded as deliberate; if it is
  per-batch drift on the same source word, collapse to "traitor" with
  "turncoat/renegade" allowed only where the same sentence already used
  "traitor".

3.3 The explicit KEEP list. A mechanical pass WILL over-correct 2-3 of
these; search the diff for them after every batch:

- Quoted documents, displayed set-off passages (the Wu Hao notices, Mao's
  proclamation, telegrams, court and Party documents), memoir and testimony
  block quotes, and the ch15 memorial inscription: register untouched,
  ellipsis abridgment marks untouched, no contractions added, litotes and
  ceremony intact.
- The institutional first person ("our Party," "our army," "we," "the enemy
  and ourselves") and the partisan lexicon ("reactionaries," "running
  dogs," "traitors," "White Terror"): the author's voice, kept.
- "Comrade" per the STYLE.md ruling (direct address, dialogue, reverence at
  first appearances and for the fallen); do not thin it mechanically.
- Canonical quotations in their received English (Sun Tzu, "Political power
  grows out of the barrel of a gun" class).
- "Theatre" inside venue proper names (Carlton, Peacock Oriental, Beijing,
  Lido): a recorded B14 decision.
- Every decided rendering in the STYLE.md word ledger and glossary.json;
  every note anchor (any edit that touches one carries its NOTE-ANCHOR pair
  in the same edit list); scene-break and set-off markers (`***`, `{v}`,
  `{d}`, `{p}`); paragraph boundaries absolutely.
- The em-dash rate and the existing contraction rate: both already at
  target. This pass does not add contractions by quota and does not swap
  em dashes wholesale.
- "let slip" in its modern sense; "in the end" in narration; sentence-
  initial "Besides," where it reads spoken-modern; litotes and archaism
  inside quotation marks anywhere.

## 4. Triage discipline

One verdict per flagged site: LEAVE / TOUCH / RECAST. The unit of work is
the FLAGGED SITE (a tic hit, a listed sentence, a global item), not the
paragraph: unflagged paragraphs are not read for style in Tier B batches.
Expected yield, calibrated on the measured counts: roughly 300-450 edits
book-wide across ~230 tic sites, ~95 date sites, ~65 Politburo sites, ~34
long sentences, plus the ch15/ch16 aligned reads. Both prior revision
passes on this shelf over-predicted defect density by an order of
magnitude; if a batch's edit list wants to touch most paragraphs of a
chapter, the batch is churning: stop and recalibrate against the R1
exemplar diff. A rewrite that only shuffles synonyms is a defect in the
edit list. Chapters with near-zero tics (ch00, ch10, ch13, ch26, ch27) are
expected to come back almost clean; that is the pass working.

## 5. Method per chapter (do it exactly like this)

1. Run `bash scripts/register_tics.sh <id>` and the extra greps from 3.2
   (litotes, 等-tags, "one after another", nominalizations, long
   sentences). Collect the site list.
2. For each site, consult the paired source line
   (`python3 scripts/make_bilingual.py <id>` after verify_unit is green;
   pairing is positional). Mechanical swaps (dates, besides, thereupon)
   need only the English read aloud; anything touching meaning, sequence,
   or a hedge gets the source line read. For ch15 and ch16 ONLY, read zh
   against en in aligned 40-60 paragraph chunks, whole chapter, per the
   full-revision method.
3. Write `edits/<id>_edits.md` in the apply_edits.py grammar (OLD exactly
   once; NOTE-ANCHOR pairs for any anchor a prose edit breaks; tier tag in
   the header line). Commit the edit list BEFORE applying.
4. `python3 scripts/apply_edits.py <id>`; if an edit cannot apply cleanly,
   skip and log why; never improvise a third wording.
5. `python3 scripts/verify_unit.py <id>`; `check_register.py --ref` per
   section 2; re-run `register_tics.sh <id>` and confirm every surviving
   hit is defended. Next chapter.
6. Spot-audit 10% of edited paragraphs (min 10 per batch) against the
   source for meaning drift; record in PROGRESS.md.

## 6. Footnote expansion protocol

Not in scope. This pass adds notes ONLY where an edit creates the need
(none expected) or where a 3.2 edit reveals a genuine reading uncertainty.
The apparatus was completed and reconciled at B14; note density is a
settled decision. NOTE-ADD blocks in an edit list therefore require a WHY
that names the new need.

## 7. Batch structure and contingency

Five batches, balanced by flagged-site load (not paragraph count). One
batch = one conversation, started by pasting the kickoff from section 9.
NO subagent fan-out. Each batch: edits applied, per-unit checks green,
cumulative EPUB rebuilt, qa_epub PASS (epubcheck when installed), PROGRESS
and CHANGELOG entries, commit, push to `claude/zhou-enlai`, EPUB attached
in chat, next kickoff pasted verbatim.

- **R1 — foundation, globals, exemplar.**
  (a) `./setup.sh`; regenerate `data/zh/` for all 28 units per
  `scripts/recovery/README.md`; replay `apply_fixes.py`; verify_unit green
  on all 28 units BEFORE any edit; pin known-benign warnings in section 2;
  snapshot `out/ch01_reading.pre-R.md` as the register ref.
  (b) Tier A globals: date normalization (95 sites, scripted edit-list
  generation); the Politburo cascade (prose + notes + glossary +
  authority.json); "in good time" x16; ch07 "driving into"; any other
  STYLE.md-ledger residual a grep turns up.
  (c) The exemplar: ch15 full treatment (Tier B sweep + aligned zh-en read
  + spine test). Its committed diff is the calibration target every later
  batch must match.
  (d) Rebuild, qa_epub, epubcheck, spot-audit, CHANGELOG.
- **R2 — tic sweep, front:** ch00-ch08 (372 paras, ~70 tic hits, 6 long
  sentences). Includes ch01; re-verify its note anchors carefully (28
  notes) and keep the pre-R register snapshot as ref.
- **R3 — tic sweep, middle:** ch09-ch14, ch16, ch17 (362 paras, ~80 tic
  hits; ch16 gets the full aligned read like ch15).
- **R4 — tic sweep, back:** ch18-ch22 (316 paras, ~85 tic hits; ch19's 5
  and ch21's 2 long sentences; ch19-ch20 already carry the Politburo form
  from R1).
- **R5 — tail + reconciliation + close.** ch23-ch27 (242 paras, ~40 tic
  hits). Then: the 叛徒 variety check (3.2); whole-book re-run of
  register_tics.sh with every surviving hit defended; `check_reconcile.py`;
  grep the diff for KEEP-list over-corrections; full rebuild; qa_epub +
  epubcheck; a fresh 15-paragraph spot audit drawn from edited paragraphs
  book-wide; update COMPLETION.md with a dated revision record; final EPUB
  committed with `git add -f out/zhou-enlai.epub`; restore HANDOFF.md to
  its completion state (no kickoff section); CHANGELOG.

Contingency: if a session dies, stop at a chapter boundary, commit, push,
deliver, and record the exact resume point in PROGRESS.md ("R3 applied
through ch12; ch13 site list drafted, not applied"). Edit lists are
committed before application precisely so a dead session loses no analysis.

## 8. Exit checklist (copy into each batch log)

- [ ] every edited chapter verify_unit green
- [ ] typography guard clean (curly/ellipsis grep prints nothing)
- [ ] register_tics.sh re-run; surviving hits defended in PROGRESS.md
- [ ] check_register vs the pre-R ch01 snapshot within tolerance
- [ ] build green, qa_epub PASS (epubcheck when installed)
- [ ] spot-audit recorded in PROGRESS.md
- [ ] diff searched for KEEP-list over-corrections
- [ ] R5 only: reconciliation sweep, COMPLETION.md revision record, final
      EPUB committed
- [ ] EPUB attached in chat + next kickoff pasted verbatim

## 9. Verbatim kickoff messages

### R1

```
Zhou Enlai R1 (revision)

Read CLAUDE.md, then REVISION_PLAN.md (it governs this pass; where HANDOFF.md disagrees, the plan wins), then STYLE.md and review/REGISTER_PASS_ASSESSMENT.md. All work on branch claude/zhou-enlai only; if the session starts on a stray branch, fold it per CLAUDE.md rule 2. Content is FROZEN: English-surface edits at flagged sites only, no paragraph merged or split, no facts or hedges changed, edits only via edits/<id>_edits.md + scripts/apply_edits.py.

Do batch R1 end to end per REVISION_PLAN.md section 7: (a) setup.sh; regenerate data/zh for all 28 units per scripts/recovery/README.md and replay apply_fixes.py; verify_unit green on ALL units before any edit; pin known-benign warnings in the plan's section 2; snapshot out/ch01_reading.pre-R.md; (b) Tier A globals: normalize the 95 day-month dates to month-day, cascade the Politburo decision (plan section 3.2; default "the Politburo", record in glossary.json and authority.json), fix the "in good time" and "driving into" ledger residuals; (c) the ch15 exemplar: full tic sweep plus aligned zh-en read plus spine test, per plan sections 3-5; (d) rebuild, qa_epub, epubcheck, 10% spot-audit, PROGRESS and CHANGELOG entries, commit, push.

Do not pause for approval mid-batch. Cite printed folios in any new note text. Never invent bridging text. End the batch with the rebuilt EPUB attached in chat AND the R2 kickoff from REVISION_PLAN.md section 9 pasted verbatim in a fenced block.
```

### R2

```
Zhou Enlai R2 (revision)

Read CLAUDE.md, then REVISION_PLAN.md (it governs; where HANDOFF.md disagrees, the plan wins), then STYLE.md. Branch claude/zhou-enlai only; fold any stray branch per CLAUDE.md rule 2. Content FROZEN; edits only via edits/<id>_edits.md + scripts/apply_edits.py. Before editing, read the committed R1 exemplar diff for ch15: every edit list in this batch must match its restraint.

Do batch R2 = tic sweep of ch00-ch08 per REVISION_PLAN.md sections 3-5: register_tics.sh plus the section 3.2 greps per unit, source consulted at every non-mechanical site, LEAVE/TOUCH/RECAST verdicts, spine test on the flagged long sentences, KEEP list respected (quoted documents and memoirs untouched). ch01 carries 28 note anchors; pair every broken anchor in the same edit list, and run check_register against out/ch01_reading.pre-R.md. If data/zh is missing (fresh container), regenerate per scripts/recovery/README.md and verify_unit green before editing.

Per unit: apply, verify_unit, re-run tics, defend survivors in PROGRESS.md. Then rebuild, qa_epub (epubcheck if installed), 10% spot-audit (min 10), CHANGELOG, commit, push. Do not pause for approval. End with the rebuilt EPUB attached in chat AND the R3 kickoff from REVISION_PLAN.md section 9 pasted verbatim in a fenced block.
```

### R3

```
Zhou Enlai R3 (revision)

Read CLAUDE.md, then REVISION_PLAN.md (it governs; where HANDOFF.md disagrees, the plan wins), then STYLE.md. Branch claude/zhou-enlai only; fold any stray branch per CLAUDE.md rule 2. Content FROZEN; edits only via edits/<id>_edits.md + scripts/apply_edits.py. Calibrate against the committed ch15 exemplar diff before writing the first edit list.

Do batch R3 = tic sweep of ch09-ch14 and ch17, plus the FULL treatment of ch16 (aligned zh-en read like ch15; it is the other elevated-antique biography chapter), per REVISION_PLAN.md sections 3-5. Source consulted at every non-mechanical site; KEEP list respected. If data/zh is missing, regenerate per scripts/recovery/README.md and verify_unit green before editing.

Per unit: apply, verify_unit, re-run register_tics.sh, defend survivors in PROGRESS.md, check_register vs out/ch01_reading.pre-R.md. Then rebuild, qa_epub (epubcheck if installed), 10% spot-audit (min 10), CHANGELOG, commit, push. Do not pause for approval. End with the rebuilt EPUB attached in chat AND the R4 kickoff from REVISION_PLAN.md section 9 pasted verbatim in a fenced block.
```

### R4

```
Zhou Enlai R4 (revision)

Read CLAUDE.md, then REVISION_PLAN.md (it governs; where HANDOFF.md disagrees, the plan wins), then STYLE.md. Branch claude/zhou-enlai only; fold any stray branch per CLAUDE.md rule 2. Content FROZEN; edits only via edits/<id>_edits.md + scripts/apply_edits.py. Calibrate against the committed ch15 exemplar diff.

Do batch R4 = tic sweep of ch18-ch22 per REVISION_PLAN.md sections 3-5, including the spine test on ch19's five and ch21's two flagged long sentences. ch19-ch20 already carry the Politburo form from R1; do not re-decide it. Source consulted at every non-mechanical site; KEEP list respected (ch20-ch22 are dense with quoted testimony; abridgment ellipses and document register stay). If data/zh is missing, regenerate per scripts/recovery/README.md and verify_unit green before editing.

Per unit: apply, verify_unit, re-run register_tics.sh, defend survivors in PROGRESS.md, check_register vs out/ch01_reading.pre-R.md. Then rebuild, qa_epub (epubcheck if installed), 10% spot-audit (min 10), CHANGELOG, commit, push. Do not pause for approval. End with the rebuilt EPUB attached in chat AND the R5 kickoff from REVISION_PLAN.md section 9 pasted verbatim in a fenced block.
```

### R5

```
Zhou Enlai R5 (revision, final)

Read CLAUDE.md, then REVISION_PLAN.md (it governs; where HANDOFF.md disagrees, the plan wins), then STYLE.md. Branch claude/zhou-enlai only; fold any stray branch per CLAUDE.md rule 2. Content FROZEN; edits only via edits/<id>_edits.md + scripts/apply_edits.py. Calibrate against the committed ch15 exemplar diff.

Do batch R5 = tic sweep of ch23-ch27, then the pass-closing sweep, per REVISION_PLAN.md sections 3-5 and 7: the 叛徒 variety check (plan section 3.2; sample against source, collapse only if it is drift, record the verdict); whole-book register_tics.sh re-run with every surviving hit defended; check_reconcile.py; grep the full pass diff for KEEP-list over-corrections; fresh 15-paragraph spot audit drawn from edited paragraphs book-wide. If data/zh is missing, regenerate per scripts/recovery/README.md and verify_unit green before editing.

Close out: rebuild, qa_epub, epubcheck; update COMPLETION.md with a dated revision record (edit counts per tier, spot-audit result, the 叛徒 verdict); commit the final EPUB with git add -f out/zhou-enlai.epub; restore HANDOFF.md to its completion state with NO kickoff section (the pass is over; further work is corrections per CLAUDE.md); CHANGELOG; commit, push. Do not pause for approval. End with the final EPUB attached in chat and a closing summary; there is no next kickoff.
```
