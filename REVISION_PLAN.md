# REVISION_PLAN.md — register/style/apparatus pass over the completed book

## 0. Provenance, and the one branch rule (read this first)

This pass imports the register and apparatus lessons from the shelf's other
zh-nonfiction book (worked on branch `claude/the-sword-roars`, its commissioner
register review at its B09). **Everything needed from that branch is reproduced
IN THIS FILE, in full, already adapted to this book and corroborated against
this book's built text by a read-only audit (2026-08-22).**

**HARD RULE: do NOT fetch, read, check out, cherry-pick, or pull ANY file from
`claude/the-sword-roars` or any other branch. All work stays on
`claude/chen-yangshan`. If this plan seems to be missing something, the answer
is to ask the commissioner in chat, never to go look at another branch.**

Where `HANDOFF.md` disagrees with this plan, this plan wins; the handoff
predates the revision.

## 1. State of play — what is DONE, do not redo

The book is COMPLETE and shipped: survey + B01-B10, all on
`claude/chen-yangshan`. 12/12 units, 1,256 body paragraphs, 432 notes, 78
figures, 731 glossary referents; qa_epub PASS, epubcheck 0/0/0; the EPUB is
committed (`git add -f out/chen-yangshan.epub`). Last content commits:
`fe098c5` (B10 close) and `c18b11a` (figure-width cap; MAX_FIG_WIDTH=1000 is
deliberate, keeps the EPUB under the 30 MiB chat limit, do not revert).
`COMPLETION.md` is the completion report; `PROGRESS.md` has every batch log.

Content is FROZEN: this is a style and annotation pass, not a retranslation.
Source lines are never touched, no paragraph is merged or split, no name is
re-romanized outside an explicit correction. The reader-facing text may change
register; it may not change meaning, facts, numbers, names, or structure.

## 2. Hard invariants, each with the command that checks it

- **Parity/anchors/headings:** `python3 scripts/check_structure.py --config
  data/check_config.<id>.json` per touched chapter. Do NOT batch verification
  to the end. CAVEAT: `data/zh/` is gitignored and does not survive a fresh
  checkout (only ch11 was present at B10 close). Handling:
  - Chapters receiving only MECHANICAL edits (tier 1/2 below; single-word or
    punctuation substitutions that cannot move a paragraph boundary): parity is
    invariant by construction. Verify instead that `git diff --stat` shows no
    line-count change in the reading file, and run `check_apparatus.py` plus
    the build (the builder refuses on any broken note/figure anchor).
  - Chapters receiving RECAST edits (tier 3): regenerate that chapter's zh via
    the pipeline (render → ocr_crop with the book's measured crop, recorded in
    PROGRESS B01 → hand-assemble), or scan-verify every recast sentence from
    the page images. A recast paragraph is re-verified against the source as if
    it were new translation (CLAUDE.md rule 4 corollary).
- **Numbers:** `python3 scripts/check_numbers.py --noise data/noise.txt
  out/<id>_bilingual.md` where zh exists; where it does not, mechanical edits
  must never touch a numeral (grep the edit list for digits before applying).
- **Anchors:** every prose edit that breaks a note or figure anchor ships the
  paired anchor edit in the same edit list (NOTE-ANCHOR pairs in the
  apply_edits grammar). The builder's refusal is the backstop, not the check.
- **Typography guard:** reading files stay plain ASCII; straight quotes and
  `...` are typographized at the RENDER layer (this book's convention, per
  CLAUDE.md). So curly quotes/ellipsis characters must NOT be introduced into
  `out/*_reading.md`: `grep -n "[""'']" out/<id>_reading.md` prints nothing.
- **Build + QA after each batch:** `python3 scripts/build_reading_epub.py &&
  python3 scripts/qa_epub.py` green, then
  `java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/chen-yangshan.epub` 0/0/0
  (setup.sh re-fetches epubcheck on a fresh container).
- **Register:** `python3 scripts/check_register.py out/<id>_reading.md --ref
  out/ch01_reading.md`. If tier 3 is approved, ch01 is swept FIRST and
  re-frozen as the reference so the measurement stays coherent.
- Known-benign warnings pinned: check_align flags ch01 pair 33 (verse line,
  legitimate ~10x expansion) and ch05 布礼 ("Bolshevik greetings", 2-char
  closing). Anything else, investigate.

## 3. The register target

### 3.1 The falsifiable voice test (imported, adapted)

**Modern-neutral is the default register for everything, narration included.
Period flavour comes from the CONTENT (the offices, silver dollars, patrolmen,
the concessions, the Green Gang), never from antique SYNTAX.** A book about
1929 does not have to be written as if published in 1929.

Three voices, and the line between them is bright:
- **Documents sound like documents.** Quoted letters, telegrams, verdicts,
  communiqués, resolutions, the obituary genre: these MAY stay starchy and
  formal. That is period work and it is correct.
- **The narrator sounds like a smart writer today,** explaining this history to
  an intelligent friend who is not in the field.
- **People sound like people.** Quoted speech is speech.

**THE READ-ALOUD TEST, the universal tiebreaker: say the sentence aloud. If a
costume-drama butler could deliver it, rewrite it. If you could say it to a
smart friend, it is done.**

Commissioner's brief, verbatim (2026-08-22 chat): "take a look ... at the way
styles are set up for claude/the-sword-roars ... tell me if you think you can
adapt the learnings from that to another voice/register/style pass over the
book"; and the standing Batch-1 gate directive on notes remains in force
("a high density explaining everything ... but don't add footnotes just to add
them").

### 3.2 Defect classes, with live examples from THIS book and their carve-outs

The audit counts below are the 2026-08-22 baseline over `out/ch*_reading.md`
(ch02s45 excluded as a QC slice) and the apparatus. This book starts far
cleaner than the sibling book did (its own voice-gate rules already banned
clefts, antique light-verbs, and most inversion), so expect LOW counts; the
sibling's whole-book rebaseline is reproduced here as the rulebook, but the
touch-rate here should be a fraction of what that book needed.

**T1. Mechanical, unambiguous (tier 1):**
- *Date format.* One form book-wide: Month D, YYYY ("November 14, 1927").
  The body is already uniform; the outliers are in the APPARATUS: ~15
  D-Month-YYYY dates in notes.json (e.g. "30 August 1929", "7 July 1937",
  "30 October 1945"), 1 in glossary.json. Fix the apparatus only.
- *Politburo.* 政治局 renders as **the Politburo** (with qualifiers as needed),
  NEVER "Political Bureau". This book: 19 "Political Bureau" vs 3 "Politburo"
  (e.g. ch02:7,9,10 "the provisional Political Bureau"). Collapse to
  "the provisional Politburo" etc. This is the shelf canon.
- *White Terror.* Capitalize both words for the specific post-1927 terror.
  This book is split: 21 lowercase vs 6 capitalized (e.g. ch01:120,124).
  CARVE-OUT: a generic use ("a white terror descended") stays lowercase if any
  exists; read each hit.
- *Spelling locale.* American, already clean (reconcile: 0 British/438
  American; 0 "Centre"). Re-run the battery at the end as regression only.
- *Inversions.* "So answered, with one voice, several of the chief men ..."
  (ch03:88) becomes subject-first ("Several of the chief men ... answered with
  one voice"). "Such was ..." (ch04:109, ch04:151) is a borderline summary
  formula: recast if the read-aloud test fails, else leave; do not exceed the
  evidence.
- *Litotes calques.* "no few" (ch03:99 "had had no few comrades killed" →
  "a good many"), "no small" x5 (read each; "no small figure" class recasts,
  idiomatic ones may stand).
- *"could not but / could not help / had no wish to"* (~6 total, e.g.
  ch02:54, ch03:98): plain equivalents ("had to", "couldn't help", "did not
  want to" / "didn't want to").
- *Sentence-initial numerals.* Grep `^[0-9]` on reading files; recast any hit.
- *Ellipses in narration.* ~10 hits; keep "..." only inside quotations the
  source truncates; narration gets a period. CARVE-OUT: several hits are
  inside {v} documents or quoted speech (ch02:115, ch02:252); those stay.

**T2. Tic thinning (tier 1, judgment-lite):**
- *等-tags.* "and others" x47, "and the others" x18, "and the rest" x12.
  Vary with "among others", restructure, or cut where the list is complete.
  Target: no single tag dominating; not zero.
- *"one after another"* x16 (ch01:77,86,122 ...): vary with "in turn",
  "one by one", or cut.
- *Nominalizations.* ~18 "the X-ing of the Y" (ch01:60, ch02:125 ...): convert
  roughly two-thirds to finite verbs; leave the ones that read naturally.
- *即/也就是 pivots.* Grep "that is to say|which was to say|in other words|
  namely": replace most with an appositive comma, colon, or dash.
- *Quote tags.* Grep "in his lifetime|in his later years" as TAGS: modernize
  ("later recalled", "once said"). CARVE-OUT: literal uses are fine and both
  current hits (ch04:192, ch06:52 "pieces he wrote in his lifetime") ARE
  literal; expect near-zero edits here.
- *Doubled synonyms.* 并列 pairs rendered as English doublets ("threats and
  inducements" class): collapse to the stronger word when the two do not
  really differ; keep real distinctions. Collapse roughly two-thirds of true
  near-synonym pairs; when in doubt, keep.

**T3. The register rebaseline proper (tier 3, COMMISSIONER-GATED):**
- *Contractions in narration.* Currently near zero outside dialogue (ch03-ch06
  narration: 2/6/2/0 "n't"). If approved: contract 10-15% of narration
  negatives/auxiliaries, by ear, wherever rhythm wants it. Documents, the
  obituary, and formal quoted matter NEVER contract.
- *Sentence topology, the SPINE TEST.* Split by load, not length: (1) more
  than one finite spine to track → split; (2) main verb must land within
  ~20 words, an appositive over ~15 words between subject and verb is lifted
  out into its own sentence; (3) a colon-plus-list is EXEMPT at any length,
  never break a list. Triage: look only at narration sentences over ~90 words,
  and over ~60 with two-plus spines. Quoted documents are exempt (they are
  evidence, not narration).
- *Ceremony compression.* Rhetorical questions and paired exclamations: keep
  the heat, halve the words; of a consecutive pair, cut the second.
- *De-quilting.* Paragraphs stitching many 2-5-word quoted fragments: unquote
  the unremarkable ones, keep quotes only for genuinely distinctive wording
  (presentation change only; the words stay).
- *Front-load attribution.* Any quote that shifts tense/person gets a lead-in
  ("As X reported in 1929: ...") even when a trailing citation stays.

**Chengyu triage (applies at every tier when an idiom is touched):** three
bins. (1) Self-evident image → keep literal ("tiger's mouth"). (2) Culturally
load-bearing but opaque → keep AND footnote. (3) No parseable image → silently
naturalize to the sense ("no pushover", "scared out of her wits"). A bin-3
idiom must never sit in the body as a raw calque.

### 3.3 The KEEP list (a mechanical pass WILL over-correct 2-3 of these; grep the diff for them afterward)

- **The ch07 obituary, whole.** It is a 悼词 in the fixed memorial-notice
  genre; its formality ("passed over into membership", "laboring hard and to
  marked effect") is deliberate and noted. Zero register edits.
- **Every {v} block**: the two 1988-letter renderings (ch03 and ch08, kept
  deliberately distinct per the B10 reconcile, cross-referenced by note), the
  ch04 top-secret letter, the ch05 Wu Hao notice and the two 1961 letters, Mao's
  directive, Guan Fushan's recollection. Documents stay starchy.
- **Chen's own posthumous writings (ch08)**: his dry first-person, the 13
  precepts, the 36-item outline. The plain stiffness is his voice.
- **Verse and couplets**: the {p} prison poem, the Wang Shukai couplet, the
  four calligraphy tributes' renderings.
- **The author's institutional first person** ("our Party", "we") and the
  partisan epithets ("traitors", "running dogs", "reactionaries"): the
  interested-witness discipline keeps them; verdicts live in the notes.
- **Decided renderings**: everything in glossary.json and the STYLE.local
  word ledger; one rendering per referent, changed only through the glossary
  with a grep-cascade, never ad hoc. "Avenue Joffre" (fixed in B10) stands.
- **Anything inside a note or figure anchor**, unless its NOTE-ANCHOR pair
  ships in the same edit list.
- **The heroic set-phrases already rationed** per STYLE.local: do not
  re-inflate OR further deflate; that calibration is settled.
- **"Peking Union Medical College Hospital"** (institutional name), "a
  Cantonese" (demonym), romanized cited titles ("Teke Mimi Zhan"): correct
  fixed forms, not register defects.

### 3.4 Consistency canon for THIS book (decided now, applied in tier 1)

- 政治局 → **the Politburo** (never "Political Bureau").
- 白色恐怖 → **the White Terror** (capitalized) for the specific terror.
- Dates: **Month D, YYYY** everywhere, apparatus included.
- Spelling: **American**, throughout (already true; regression only).
- Party center: **the (Party) Center** (already uniform; regression only).

## 4. Triage discipline

One verdict per paragraph: LEAVE / TOUCH / RECAST. Expected distribution: MOST
paragraphs LEAVE. Both prior revision passes on the shelf over-predicted defect
density by roughly ten times; this book's baseline counts above total a few
HUNDRED candidate tokens across 1,256 paragraphs, most of them one-word
substitutions. A rewrite that only shuffles synonyms is a defect in the edit
list. RECAST exists only if tier 3 is approved. Calibrate on an exemplar
first: revise one chapter, commit it, and require every later batch to read
that diff as the target.

## 5. Method per chapter (do it exactly like this)

1. Run the grep battery (3.2) over the chapter; walk the hits in context.
   For tier-3 chapters also read zh and en in ALIGNED chunks of 40-60
   paragraphs (regenerated zh, or the page images for the touched spans);
   an English-only read misses quiet fidelity drift.
2. Write the edit list to `edits/<id>_edits.md` in the apply_edits.py grammar
   (OLD occurs exactly once; NOTE-ANCHOR pairs for any anchor an edit breaks;
   NOTE-ADD blocks for any new note). Collect apparatus fixes in the same
   read, not a second one.
3. Apply mechanically: `python3 scripts/apply_edits.py <id>`. If an edit does
   not apply cleanly, skip it and log why; never improvise a third wording.
4. Verify per section 2 (structure/apparatus/build for mechanical chapters;
   full battery for recast chapters). Next chapter.
5. Spot-audit 10% of edited paragraphs (min 10) against the scan for meaning
   drift; record in PROGRESS.md.

## 6. Apparatus work in this pass (mechanics, not expansion)

The 432 notes are at the commissioner-approved density; this pass does NOT
expand coverage. Scope:
- **One note = one referent.** Audit for bundled notes (a body naming several
  distinct referents, or saying "named above"): split by referent, marker at
  its referent; a tight single-location list may keep one note with the marker
  moved to the END of the list.
- **Marker placement.** In the built EPUB, no superscript mid-phrase; move
  markers to sentence/clause end, updating anchors in notes.json in the same
  pass.
- **One gloss mechanism per term.** Inline appositive only when under ~8 words
  AND needed to parse; footnote for context; glossary for recurrers, noted
  once at first appearance. Grep recurring terms for double-glossing.
- **Principal Characters page: grow from 3 to ~15-20.** Flag the recurring
  cast in glossary.json (`"principal": true`, one-line `cast`, `cast_order`):
  Chen Yangshan, Yun Daiying, He Long, Zhou Enlai, Chen Geng, Bao Junfu,
  Li Kenong, Kang Sheng, Gu Shunzhang, Pan Hannian, Zhang Suzhen, Chen Kehan,
  Wang Shiying, Xu Enzeng, Chiang Kai-shek, plus judgment picks (Lu Nan,
  Wei Jian, Cheng Jianyu). Pure glossary edit, zero prose risk.
- **Translator's note**: add one sentence stating that "our Party", the
  epithets, and the celebratory register are the AUTHOR'S voice, preserved
  deliberately, with the fact-check verdicts in the notes. One sentence
  inoculates the whole book.
- (Optional, commissioner's call: a back-matter street/place gazetteer was
  valuable on the sibling book; this book leans less on street names, so
  propose only if the audit shows repeated "(today X)" glosses.)

## 7. Batch structure and contingency

- **R0 (calibration, read-only).** Full diagnostic battery + notes audit +
  the two-way sample (one section current vs tier-3 rebaselined, plus 8-10
  before/after sentences). STOP; commissioner picks the tier: (a) tier 1+2
  only, or (b) all three. Nothing edited in R0.
- **R1.** Ledger update (write the approved rules into STYLE.local.md as the
  book's imported rebaseline section, tagged, with this plan cited as
  provenance) + the exemplar chapter (ch01 if tier 3, else ch02, the largest)
  end to end, committed, diff presented.
- **R2-R3.** The remaining chapters in two batches balanced by paragraph
  count (roughly ch02-ch04 / ch05-ch11 + apparatus + principals + translator's
  note), each ending with build + QA + commit + EPUB in chat.
- **R-final.** Whole-book regression: full battery re-run, reconcile sweep,
  register table across the spine (re-frozen reference if tier 3), epubcheck,
  dated CHANGELOG entry, COMPLETION.md addendum, final EPUB committed
  (`git add -f`) and delivered.

NO subagent fan-out (a real attempt on this shelf burned the budget re-reading
shared context; sequential in-session work is cheaper and uniform). If a
session dies: stop at a chapter boundary, commit, push, deliver, and record
the exact resume point in PROGRESS.md.

## 8. Exit checklist (copy into each batch log)

- [ ] every edited chapter verified per section 2
- [ ] typography guard clean (reading files still plain ASCII)
- [ ] no numeral changed anywhere (grep the edit lists for digits)
- [ ] build green, qa_epub PASS, epubcheck 0/0/0
- [ ] spot-audit recorded in PROGRESS.md
- [ ] KEEP-list sweep of the diff (obituary, {v} blocks, precepts, verse,
      partisan register, decided renderings untouched)
- [ ] on R-final: reconcile sweep + register table + CHANGELOG + COMPLETION
      addendum + EPUB committed and attached in chat
- [ ] EPUB attached in chat + the next batch's kickoff pasted

## 9. Verbatim kickoff messages

### R0 (paste to start the pass)

```
Chen Yangshan REVISION R0 (calibration, read-only)

Read, in order: CLAUDE.md, then REVISION_PLAN.md (it is self-contained; do NOT
read or pull anything from any other branch), then COMPLETION.md, STYLE.md,
STYLE.local.md. All work on claude/chen-yangshan; the book is COMPLETE and
content is FROZEN.

Do R0 per the plan: (1) the full grep battery of plan §3.2 per chapter, walked
in context, with per-chapter counts; (2) the notes audit of plan §6 (bundles,
mid-phrase markers, double glosses) over all 432 notes in the built EPUB;
(3) the two-way sample: one narrative section rendered current vs tier-3
rebaselined, plus 8-10 before/after sentences spanning the classes; honour the
KEEP list (§3.3) throughout. NO file edits, no commits, no rebuild.

Deliver in chat: the tic table, the notes-audit summary, the two-way sample,
and STOP for the commissioner's tier decision (tier 1+2, or all three).
```

### R1 (paste after the tier decision; fill the [TIER] bracket)

```
Chen Yangshan REVISION R1 (ledger + exemplar)

Read: CLAUDE.md, REVISION_PLAN.md (self-contained; never read other branches),
STYLE.md, STYLE.local.md, and the R0 results in PROGRESS.md. Approved scope:
[TIER 1+2 | ALL THREE TIERS]. All work on claude/chen-yangshan.

Do R1 per the plan: write the approved rules into STYLE.local.md (tagged,
provenance REVISION_PLAN.md §3); then the exemplar chapter ([ch01 if tier 3,
else ch02]) end to end by plan §5: edits via edits/<id>_edits.md +
apply_edits.py, verification per plan §2, spot-audit, KEEP-list diff sweep.
[If tier 3: re-freeze swept ch01 as the register reference.] Rebuild, qa_epub,
epubcheck, commit, push. Deliver the EPUB in chat, present the exemplar diff,
and paste the R2 kickoff.
```

### R2 / R3 (pattern; fill the chapter range)

```
Chen Yangshan REVISION R[2|3] (sweep [ch02-ch04 | ch05-ch11 + apparatus])

Read: CLAUDE.md, REVISION_PLAN.md (self-contained; never read other branches),
STYLE.local.md (now carries the approved rules), PROGRESS.md (the exemplar
diff is the calibration target). All work on claude/chen-yangshan.

Sweep the listed chapters per plan §5 with the §2 verification, honouring the
§3.3 KEEP list; [R3 also: the apparatus mechanics of §6, the Principal
Characters growth, the translator's-note sentence]. Rebuild, qa_epub,
epubcheck, commit, push. Deliver the EPUB in chat and paste the next kickoff
(R3, or R-final).
```

### R-final

```
Chen Yangshan REVISION R-final (whole-book regression + close)

Read: CLAUDE.md, REVISION_PLAN.md, STYLE.local.md, PROGRESS.md. All work on
claude/chen-yangshan; never read other branches.

Re-run the full battery across the spine (structure/apparatus/build/qa/
epubcheck, reconcile sweep, register table [against the re-frozen ch01 if tier
3]); KEEP-list sweep of the whole revision diff; dated CHANGELOG entry;
COMPLETION.md addendum recording the pass and final counts; commit the final
EPUB (git add -f out/chen-yangshan.epub); push. Deliver the EPUB and the
addendum in chat. HANDOFF.md returns to "COMPLETE; further work is a
corrections pass."
```
