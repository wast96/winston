# REVISION_PLAN.md: Nameless Heroes register revision pass

Commissioned 2026-08-22 after a comparative style review against the shelf's
composed style-contract system. This plan is the single authority for the
pass. Where `HANDOFF.md` (the completion notice) disagrees with this plan,
this plan wins; the handoff predates the revision. Where this plan disagrees
with a session's improvisation, this plan wins; new rulings are added to §3
of this file, not invented ad hoc.

This file is SELF-CONTAINED on purpose. Everything imported from the shelf's
style system has been transcribed into it. No revision session may fetch,
check out, read, or diff any branch other than `claude/nameless-heroes` (§7).

## 1. State of play: what is DONE, do not redo

- 43/43 units translated; the book is COMPLETE as of commit b760613 (B36).
- 375 translator notes, 0 source notes; glossary 708 rows; cast page built.
- All gates green at completion: parity 6,160/6,160; numbers 0 unresolved;
  qa_epub PASS; epubcheck 5.1.0 clean; fixed-seed deep audit 44/45 faithful,
  zero substantive errors.
- Spelling unified AMERICAN in B36 (0 British forms remain). Do not re-argue.
- Content is FROZEN. This is a REGISTER pass, English-to-English: no source
  line is retranslated from scratch, no paragraph is merged or split, no name
  is re-romanized, no fact, name, number, date-value, or claim changes. Every
  NEW preserves the propositional content of its OLD exactly. The apparatus
  is complete; notes change only as §6 allows.

## 2. Hard invariants, each with the command that checks it

- Paragraph parity + numbers + anchors: `python3 scripts/verify_unit.py <id>`
  (with `--noise data/noise.txt` behavior built in) per chapter, AS each
  chapter finishes. Do NOT batch verification to the end.
- Anchors: any prose edit that breaks a note anchor carries a paired
  NOTE-ANCHOR block in the same edits file; the builder's refusal on an
  unmatched anchor is the backstop, not the check.
- Alignment/displacement after each batch: `python3 scripts/check_align.py`,
  `python3 scripts/check_content.py`. Known-benign displacement false
  positives (homograph/substring): ch08 Shunde, ch09 Jize, ch13, ch26, ch38,
  ch41. Anything new, investigate.
- Register vs the NEW frozen reference (§5.6): `python3 scripts/check_register.py
  --ref reference/R1_frozen.md` on each revised unit (from R2 on).
- Tic battery before AND after each chapter: `bash scripts/revision_tics.sh
  <id>`; both count sets go in PROGRESS.md. The battery is a flag, not a
  verdict: quoted documents legitimately hit it.
- Build + `python3 scripts/qa_epub.py` after each batch; epubcheck when
  available. A failure stops the line.
- Spot-audit 10% of EDITED paragraphs (min 10) per chapter against the
  source for meaning drift; record in PROGRESS.md. The only real fidelity
  defects prior revision passes found were invisible to an English-only read.

## 3. The register target

### 3.1 The falsifiable voice test

**"Could a first-rate translator, publishing this memoir with a serious house
today, have written this sentence?"** The model is a dignified, formal,
GRAVE first-person memoir voice in clean modern English: the gravity comes
from Chen's content and cadence, never from antique function words or calqued
syntax. Chen is an elderly officer writing about his dead; he is allowed to
be formal. He is not allowed to sound like a Victorian deposition.

The read-aloud tiebreaker, adapted: if you can hear a costume-drama butler
saying it, rewrite it; if you can hear a grave, precise, old-fashioned but
LIVING narrator saying it to you across a desk, it stays. This differs
deliberately from the shelf's modern-neutral default for third-person
histories: Chen's persona is content, and this pass modulates it, it does
not raze it.

Three voices, bright lines between them:
- **Chen's narration:** formal, grave, modern-clean. Uncontracted by default
  (persona; see T5 for the exception). The narrating "shall" is DELIBERATE
  and stays.
- **Quoted documents** (orders, telegrams, reports, press items, official
  rulings): period-starchy is CORRECT. Exempt from every tic rule. The
  Dagongbao passage at `out/ch08_reading.md:737` keeps its "whereupon";
  it is evidence, not narration.
- **Dialogue:** people sound like people, differentiated by speaker (§3.2
  T5). A gunman does not talk like a magistrate.

### 3.2 Defect classes (the edit taxonomy: tag every edit T1–T6)

Each class below lists live examples (examples, not a to-do list) and its
CAUTION carve-out. Expected whole-book counts from the pre-pass battery are
in parentheses.

**T1. antique function words (the kill list).** (~800 hits)
"besides" as a sentence adverb (652: `out/ch06_reading.md:299`,
`out/ch08_reading.md:73`) → "as well" / "too" / cut; "thereupon /
whereupon" (64) → "then" / "at that"; "forthwith" (30:
`out/ch09_reading.md:407`) → "at once"; "presently" (22) → "soon";
"at length" → "finally"; "of a morning / of an evening" → "in the
morning"; "of a sudden" (`out/ch08_reading.md:39`, `out/ch16_reading.md:225`)
→ "suddenly"; "there was nothing for it but" (`out/ch08_reading.md:627`) →
"there was nothing to do but" / recast; "had no wish to" → "did not want
to"; "was wont to" → "used to"; "still less" (59) → "let alone" where it
reads stiff; "ere long," "come what may," "made bold to," "and no mistake"
→ plain equivalents or cut. Dates in narration: "the 10th of November,
1934" / "10 November" → "November 10, 1934"; spelled ordinals ("the
nineteenth of October") → "October 19."
- CAUTION: "besides" as a plain preposition ("besides his other duties") is
  fine. Every kill-list hit inside a quoted document stays. A hit is not
  automatically wrong; each survivor must be defended against the read-aloud
  test in the edits file's WHY line.

**T2. the calque set.** (~600 hits)
"could not but" (79: `out/ch12_reading.md:45`, `out/ch26_reading.md:211`) →
"could not help" sparingly, usually recast to the plain verb; "could only"
(71) → "had to" / recast where it calques 只能; "in the end" inside a
question (13: `out/ch08_reading.md:715`, `out/ch09_reading.md:249`) →
"actually" / "really" / cut (narrative "in the end" = "ultimately" is FINE);
"and the rest / and the others" for 等 (148) → vary with "among others,"
restructure, or cut when the list is complete; "that is to say / namely /
which was to say" (42) → an appositive comma, a colon, or a dash; "the
[gerund] of the" nominalizations (250: `out/ch08_reading.md:21`,
`out/ch22_reading.md:45`) → finite verbs, convert roughly two-thirds;
litotes counting ("no small number," "no few") → "a good many," "quite a
few"; fronted objects and inversions ("His guilty scheme he saw through at
a glance" shapes) → subject-verb-object, zero tolerance in narration.
- CAUTION: an idiom Chen quotes or a rendered chengyu that already carries a
  footnote keeps its image. 等-tags inside quoted documents stay.

**T3. scare-quote thinning + quote-tag modernization.** (~4,400 quoted
terms; the highest eye-level win per keystroke)
The source's 「」 emphasis was carried as English quotes on recurring decided
terms: "Beiping Station," "sanction," "stay-behind work," "intelligence
material," "Action Group" (see the wall of them at `out/ch40_reading.md:3`).
Rule: a decided recurring term wears quotes at its FIRST appearance in the
book (where its note or gloss lands) and never again; thereafter plain
(the Beiping Station, sanction, the stay-behind work). Quotes remain for:
genuine verbatim citation, a term the author is anatomizing AS a word, irony
the author himself marks, titles-as-titles, and code names at first use.
Quote-tags: "said in his lifetime," "recalled in his later years," "disclosed
many years later" → "once said," "later recalled," "wrote decades later,"
or just "said"; vary them.
- CAUTION: this is a presentation change, not a fidelity change: the words
  stay, the quote marks go. Inside quoted documents, keep everything. When
  in doubt whether the author's quotes carry irony, keep them.

**T4. sentence topology.** (1,778 narration sentences over 60 words, 449
over 90; semicolons 12.3/1k words; mean 33.5 wps against a genre norm in
the mid-20s)
Split by the SPINE TEST, not word count: (1) more than one finite spine the
reader must track → split at the spine boundary; (2) main verb later than
~20 words in → promote the front matter to its own sentence; (3) a
colon-plus-list is EXEMPT at any length; never break a list. An em-dash or
parenthetical aside that has swallowed the main verb gets the verb restored.
Semicolon chains in narration: target roughly half the current rate; the
semicolon yokes two balanced clauses, it does not staple four predicates.
Appositives over ~15 words become their own sentence.
- CAUTION: quoted documents stay long; Chen's deliberate periodic build-ups
  that LAND (a single spine with a strong close) pass at any length. Do not
  touch most long sentences; triage the 449 first, then >60-word two-spine
  cases as met in reading.

**T5. dialogue naturalization.** (contractions in the whole book: 14)
Dialogue gets full natural-speech treatment, differentiated by speaker.
"Set your mind at ease and go; the affairs here I will take charge of and
see to" (`out/ch16_reading.md:71` area) is a magistrate, not a comrade
talking to a friend → "Don't worry, go. I'll take care of things here."
Luqiao (`out/ch16_reading.md:45`), Tang Yingjie (`out/ch16_reading.md:61`),
couriers, gunmen, gangsters contract freely and speak in living rhythm;
Dai Li speaks tersely, with authority, still naturally. Build two-line
voice sheets for the recurring speakers (Chen-in-scene, Dai Li, Wang
Tianmu, Luqiao, Tang Yingjie, Zheng Jiemin, Bai Shiwei) in R1 and keep them
in this file's §3.4.
- CAUTION: Chen's own NARRATION stays uncontracted (persona), except where a
  rhythm genuinely demands one; quasi-official utterances, oaths, and slogans
  keep their weight; quoted documents never contract. Chen's reported speech
  in formal settings (to the Commandant) stays formal: formality toward a
  superior is characterization.

**T6. impersonal register thinning.** (~450 impersonal "one may / might /
could / must / dared")
Where "one" renders a generic 人/谁/也 or a hedging 可以说, thin roughly
two-thirds: "one dared not look him full in the face" → "no one dared look
him full in the face" / "I dared not..."; "one may say" → "you could say" /
state it plainly; "it may be imagined" → "you can imagine" or cut.
- CAUTION: keep "one" where Chen is genuinely generalizing as an essayist
  (his reflective codas), and keep the deliberate narrating "shall." This
  class is modulation, not eradication; when a sentence is grave on purpose,
  leave it.

### 3.3 The KEEP list (a mechanical pass WILL over-correct some of these; grep the diff for them afterward)

- The narrating **"shall"** (188, deliberate, verified across batches).
- **Quoted documents, press items, orders, telegrams, rulings**: register,
  length, archaisms, quotes, 等-tags, everything.
- **Chen's interested-witness heat**: "the utterly evil Communist Party,"
  "traitors," "sanction," the martyr set-pieces, the reverence. His slant is
  content. Never launder, never sharpen.
- **Decided glossary renderings** (708 rows; the Juntong, Beiping Station,
  sanction as a term of art, laohuzao-class romanizations). Consult
  `glossary.json` before touching any recurring term.
- **Set-off markers** `***`, `{v}` `{d}` `{g}` `{p}` and everything inside
  them; scene-break rules; datelines.
- **Note anchors**: verbatim substrings; a broken anchor gets its paired
  NOTE-ANCHOR edit in the same block.
- **Chengyu already footnoted** for their image; the "scale and half a claw"
  class of idioms that LAND in English.
- **Faithful oddities recorded in PROGRESS.md** (the source's own errors,
  numbering gaps, the preserved anachronisms). Nothing in this pass corrects
  the author.
- Chen's structural devices: the reflective codas, rhetorical questions that
  genuinely land (halve ceremony, keep the question), one-line paragraph
  pivots.

### 3.4 Voice sheets (seeded in R1, grown as speakers recur)

- **Chen-in-scene (young Chen speaking):** earnest, quick, deferential to
  seniors, candid about his own greenness; contracts with friends ("Then I'll
  go and see him at once"), stays uncontracted and formal toward the
  Commandant and in formal replies ("I should be glad to learn").
- **Dai Li (Dai Yunong):** terse, warm-but-guarded, never explains himself;
  short declaratives, plain verbs, the occasional silence AS the answer;
  contracts in offhand practical asides ("don't take it out for fun"), never
  in mission instructions or anything quasi-official.
- **Zheng Jiemin:** the staff officer: measured, complete sentences, careful
  hedges ("its reliability is uneven"), principles enumerated; formal with
  everyone, warmth carried by content rather than diction; never contracts.
- **Wang Tianmu (Zheng Shisong):** polished, worldly, urbane host; speaks
  little on the page so far (ch06: welcomes, one dinner) — when he does,
  give him easy social fluency, never stiffness; sixteen years Chen's senior
  and lets it show as ease, not pomp.
- **Wu Youquan (Wu Taixun):** the open-handed young magnate: colloquial,
  direct, unbothered ("My father did not scrape it off the land!");
  contractions fine; no literary furniture.
- **Recruiter Yi / organizational voices (ch06):** quasi-official recruitment
  speech keeps its slogan cadence and formality verbatim-weight (T5 CAUTION);
  do not naturalize the creed.

### 3.5 New rulings ledger (append-only, during the pass)

- **RULE R1-1: wrong-image idiom calques are fidelity defects, first
  priority.** WHY: the R1 blind critique's best catches were renderings that
  assert a WRONG meaning in English ("for his sake" for 为了他的事, "showing
  his hand" for 一显身手, "in good part" for largely, 刮地皮 as farming,
  "cracked the case" for a plot that never happened). FIX: at every idiom,
  ask what the English claims, not just whether it is smooth. CHECK: the
  spot-audit reads for asserted meaning, not fluency.
- **RULE R1-2: no dangling or absolute participle openers in narration.**
  WHY: "Hearing that…", "Checking the dates…", "Repenting his errors…" — the
  subject never arrives; the class recurred a dozen times in ch06. FIX:
  give the clause a subject or promote it to a sentence. CHECK: grep the
  diff for sentence-initial -ing without a following subject.
- **RULE R1-3: month-name words can fake out the number check.** WHY: "it
  may be" satisfied 五官's 5 via the May-month substring match, so the old
  text passed and the honest revision failed. FIX: when an edit surfaces a
  zh idiom-numeral, the remedy is a documented noise entry (五官, 四个大字
  added), never wording contorted to keep a false match. CHECK: any new
  noise entry carries its reason in data/noise.txt.
- **RULE R1-4: blind-reader flags on Chen's persona are REJECT-by-class.**
  WHY: 346 of 493 R1 findings named the deliberate furniture (笔者, humility
  formulas, topic frames, source-carried doubling, quoted documents, org
  terms of art, his political heat). FIX: adjudicate them as classes, cite
  the KEEP list, and record the classes once per batch instead of item by
  item. CHECK: PROGRESS lists the reject classes with one example each.
- **RULE R1-5: keep an eye on repeated translator-tics the battery does not
  count.** WHY: the critique surfaced density problems in "unable well to
  decline," "call it X—it was really Y," "the good of it was," "may be
  called," "in it" — each fine once, loud at four. FIX: when the aligned
  read meets the same rendering twice in a chapter, vary or thin the later
  ones. CHECK: note recurring tics per chapter in PROGRESS.

## 4. Triage discipline

One verdict per paragraph: LEAVE / TOUCH / RECAST. Expected distribution:
MOST paragraphs LEAVE. Prior passes predicted roughly ten times more defects
than they found; the tic battery says this book is denser than those, but
the discipline stands: an edit that only shuffles synonyms is a defect in
the edit list. TOUCH = one class fixed in place (a kill-list word, a quote
pair dropped, a date). RECAST = the sentence rebuilt (topology, dialogue);
every RECAST gets its zh line re-read first and its WHY names the class.
Calibrate on the exemplar (R1): revise ch06, commit it, gate it; every later
batch reads that diff as the target before starting.

## 5. Method per chapter (do it exactly like this)

1. Run `bash scripts/revision_tics.sh <id>`; note the counts (the "before"
   column).
2. Read zh and en in ALIGNED chunks of 40–60 paragraphs (regenerate the
   bilingual with `make_bilingual.py` if needed; it is QC-only and never
   ships). Triage per §4; write `edits/<id>_edits.md` in the apply_edits.py
   grammar as you read: `### p<NNN> [T1..T6] TOUCH|RECAST` / OLD (exactly
   once in the file) / NEW (final typography) / WHY (class + zh phrase for
   every RECAST); NOTE-ANCHOR pairs for any anchor an edit brushes.
3. Apply mechanically: `python3 scripts/apply_edits.py <id>`. If an edit
   cannot apply cleanly, skip it and log why; never improvise a third
   wording in the apply step.
4. `python3 scripts/verify_unit.py <id>`; re-run the tic battery (the
   "after" column); `check_register.py --ref reference/R1_frozen.md`
   (from R2 on). Tail check: re-read the final paragraphs against zh.
5. Spot-audit 10% of edited paragraphs (min 10) against the source; record.
6. Blind critique (R1 and §7's two spot batches only): hand the REVISED
   chapter, alone, no source, no plan, to a context-blind reader with this
   prompt, verbatim: *"Read this. It is a chapter of an English translation
   of a Chinese memoir. Tell me, in detail, every single thing in here that
   reads wrong to a native English speaker: translationese, stilted
   inversions, calqued idioms, transferred syntax, wooden dialogue,
   fake-antique register, sentences that stack too many clauses. Quote the
   phrase, say what is wrong in a few words, give the fix. No praise, no
   repetition."* Adjudicate findings ACCEPT / REJECT-with-reason in
   PROGRESS.md (a blind reader will flag quoted documents and deliberate
   gravity; those are REJECT, and the reason is the record). Real findings
   become §3.5 rules.
7. Next chapter. Commit at chapter boundaries.

## 6. Footnotes in this pass

The apparatus is COMPLETE (375 notes). This pass adds notes only where an
edit creates the need: (a) a T2/T5 naturalization discards an idiom image
genuinely worth keeping → NOTE-ADD at first occurrence, numeric character
references only; (b) nothing else. No density rebalancing, no new research.
NOTE-ANCHOR maintenance is mandatory wherever prose edits touch anchors.

## 7. Branch discipline (non-negotiable, per the commissioner)

- ALL work happens on **`claude/nameless-heroes`**. First acts of every
  revision session, before reading anything else:
  `git fetch origin claude/nameless-heroes && git checkout claude/nameless-heroes
  && git reset --hard origin/claude/nameless-heroes`.
- If the harness started the session on a stray per-task branch: consolidate
  per CLAUDE.md rule 2 (carry any commits onto the canonical branch, push,
  delete the stray local AND remote) before batch work begins.
- **Never fetch, check out, read, or diff any other branch**, including the
  shelf's other books and templates. This plan transcribes everything the
  pass needs; if something seems missing, the answer is a §3.5 ruling made
  here, not an expedition to another branch.
- Push `claude/nameless-heroes` at every batch end (retry with backoff per
  CLAUDE.md; keep committing locally if the push fails, and surface it).

## 8. Batch structure and schedule

Balanced by prose volume; sequential, in-session, NO subagent fan-out (a
real attempt burned a session budget on agents re-reading shared context).
If a session dies: stop at a chapter boundary, commit, push, deliver, record
the exact resume point in PROGRESS.md.

**Schedule (consolidated per commissioner directive 2026-08-22): the register
pass runs R1-R9 — SEVEN batches after R1/R2, not eleven.** The original 13-round
plan was set before per-batch cost was known; R2 (49k words, 823 paragraphs)
used only a small fraction of a fresh session's budget, so batches are safely
~1.5-2x larger. Each batch still commits and pushes AT EVERY CHAPTER BOUNDARY,
so a session death costs at most the chapter in flight (resume point in
PROGRESS.md). Then ONE final footnote wave, **F0** (§12).

| Batch | Units | ~En words | Notes |
|---|---|---|---|
| R1 | ch06 | 21k | EXEMPLAR + setup; ends at the gate (§9) — DONE |
| R2 | ch07, ch08 | 49k | first post-gate batch — DONE |
| R3 | ch01–ch05, ch09, ch10 | 42k | front matter is light-touch (closest to target already) |
| R4 | ch11, ch12, ch13 | 58k | |
| R5 | ch14, ch15, ch16, ch17, ch18 | 65k | + blind-critique spot check on one revised chapter |
| R6 | ch19, ch20, ch21, ch22, ch23, ch24 | 68k | |
| R7 | ch25, ch26, ch27, ch28, ch29 | 63k | |
| R8 | ch30, ch31, ch32, ch33, ch34, ch35 | 67k | + second blind-critique spot check |
| R9 | ch36, ch37, ch38, ch39, ch40, ch41, ch42, ch43 + whole-book close | 74k | reconciliation, re-score, COMPLETION update; serves the F0 kickoff |

R9 additionally runs: `check_reconcile.py`; the whole-book tic battery with
the final table into PROGRESS.md; a diff-grep for every KEEP-list item
(§3.3); grep-count of ~20 decided renderings; rebuild; qa_epub + epubcheck;
an honest before/after prose-quality statement appended to `COMPLETION.md`;
rewrites `HANDOFF.md` so its next-chat message is the **F0 footnote-pass
kickoff** (§12), NOT a "book complete" notice (the book is not done until the
footnote pass is).

## 9. Commissioner touchpoints (kept to the minimum)

1. **The exemplar gate, once (end of R1).** The R1 reply presents: 8–12
   before/after excerpt pairs chosen to span T1–T6, the ch06 tic-count
   before/after table, the rebuilt EPUB attached, and the R2 kickoff pasted
   in a fenced block. Approve by pasting the R2 kickoff into a fresh chat;
   or type corrections in the same chat, and the session folds them into
   §3.5 as rules, re-revises, and re-presents. The approved revised ch06 is
   frozen as `reference/R1_frozen.md`, the register reference for the rest
   of the pass.
2. **Nothing else until R9.** Batches R3–R8 run to completion per
   CLAUDE.md rule 3; each batch reply carries the two chat deliverables
   (EPUB attached + next kickoff pasted, per the CLAUDE.md banner). No
   mid-batch questions; genuine blockers only.
3. **R9** delivers the finished register-revised edition and the re-scored
   assessment, and serves the **F0** footnote-pass kickoff (§12).
4. **F0** (one wave) then delivers the footnote-densified final edition; its
   ch01 exemplar checkpoint (§12.4) is the only mid-pass touchpoint.

## 10. Score accounting (what "as high as possible" means, falsifiably)

Pre-pass: accessibility 5.5/10, translation quality 9/10, prose-vs-genre
6/10; composite ~6.5. Target: composite 8–8.5 without touching the 9 (the
spot audits and parity gates exist to protect it). The levers, by axis:
- Accessibility: T1+T2 kill (battery counts in NARRATION near zero), T3
  quote density (first-use only for decided terms), T4 (no >90-word
  two-spine narration sentences; narration semicolons roughly halved).
- Prose-vs-genre: T4 rhythm, T5 living dialogue, T6 modulation; the blind
  critiques are the falsifiable check (a blind reader should stop flagging
  register within two spot checks).
- Translation quality: unchanged by design; the deep-audit protocol re-runs
  on 10 fresh pairs in R9 as proof.

## 11. Verbatim kickoff canon

Every batch reply pastes the NEXT batch's kickoff assembled from this canon:
the fixed body below with the two `{...}` fields filled from the §8 table
(and, for R9, the F0-handoff noted there). The assembled kickoff is also
written into `HANDOFF.md` under `## Message to paste into the next chat`
(re-arming the Stop hook) before the reply is sent.

FIXED BODY (fill `{Rn}` and `{units}`; keep everything else verbatim):

    Nameless Heroes {Rn}: register revision pass

    Branch: claude/nameless-heroes ONLY. First acts: git fetch origin
    claude/nameless-heroes && git checkout claude/nameless-heroes && git
    reset --hard origin/claude/nameless-heroes. If the harness started you
    on a stray branch, consolidate and delete it per CLAUDE.md rule 2.
    Never read any other branch.

    Read CLAUDE.md, then REVISION_PLAN.md IN FULL (it is the authority for
    this pass), then run ./setup.sh.

    Scope this batch: {units}. Content is frozen; English-to-English
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

R1 uses its own kickoff (written at plan time, archived in `HANDOFF.md`):
it adds the exemplar-gate STOP, the voice-sheet seeding, the blind critique,
and the freezing of `reference/R1_frozen.md`, and its scope is ch06 only.

## 12. The footnote-density pass (F0, one wave), AFTER R9 — commissioner directive 2026-08-22

After the whole register revision (R1-R9) is complete, the commissioner has
ordered ONE more pass over the finished EPUB: **greatly increase footnote
density** so a non-specialist Western reader has every reference explained.
This section is the authority for that pass, exactly as §§1-11 are for the
register pass. It is added here (not invented ad hoc later) so it survives
every batch seam; the directive is also transcribed in `CORRECTIONS.md`.

### 12.1 What the pass does

- **Goal:** explain the little things a reader with no Chinese and no
  background would miss — **terms, people, places, events, institutions,
  allusions, idioms, customs**. The register pass left the prose clean; this
  pass makes it legible.
- **Density is a reader model, not a quota.** Be generous, but **never add a
  note just to add one.** Every note must tell the reader something they need
  and cannot get from the sentence. Redundant, padding, or "throat-clearing"
  notes are defects in the note list exactly as synonym-shuffle edits were in
  the register pass.
- The footnote CONTRACT is CLAUDE.md's "Footnotes — what earns one" section,
  applied at full strength: the four domains (material culture, social
  structure, customs and belief, institutions and money); the four kinds
  (translation uncertainty; a reference a non-specialist won't catch, with the
  verdict stated; texture lost in translation; the author as interested
  witness). First-appearance discipline with the greps; a "NOT re-noted"
  ledger per batch; the glossary is the quarry and the note says MORE than the
  glossary row.

### 12.2 Hard invariants (each with its check)

- **Content still frozen.** This pass adds NOTES ONLY. No prose word changes
  except the minimal anchor-bearing substring already present (notes attach to
  verbatim substrings of the shipped text; if an anchor is not present
  verbatim, pick a different anchor, do NOT reword the prose).
- **Fidelity of the note bodies:** fact-check against real scholarship
  (CLAUDE.md rule 5 / `references/fact-checking.md`); NEVER source LLM-written
  references; state the verdict (corroborated / uncorroborated / contradicted);
  a contradicted source-claim stays faithful in the text and is footnoted.
  Trace claims to the earliest source; repetition is not corroboration.
- **Never invent.** An uncertain identification is footnoted AS uncertain, not
  guessed with false confidence (RULE R1-1's spirit: say what you actually
  know).
- **Mechanics:** author notes ONLY via `apparatus_merge.py` (never a shell
  heredoc into JSON); anchors verbatim, verified at write time; note bodies are
  XHTML with **numeric character references only** (no named entities); a
  chapter H1 cannot carry a note; numbering is the builder's. `check_apparatus.py`
  clean; the builder's refuse-on-unmatched-anchor is the backstop for BOTH note
  streams, not the check.
- **Two note streams stay separate** (translator notes vs the author's own — the
  source carries none here, but the guard stands).
- Build + `qa_epub.py` after each batch (note refs == bodies == backlinks, all
  links resolve); epubcheck when available. A failure stops the line.

### 12.3 Method per chapter (do it like the register pass)

1. Read the chapter's shipped English against the source in aligned chunks.
2. List every notable term/person/place/event/allusion; check `glossary.json`
   and existing `notes.json` FIRST (do not duplicate an existing note; respect
   first-appearance — grep the built book for the term's earlier occurrences).
3. Draft note bodies with sources; fact-check; state verdicts.
4. Author via `apparatus_merge.py`; `check_apparatus.py` clean; verify every
   new anchor is a verbatim substring at write time.
5. Rebuild; `qa_epub.py` (+ epubcheck); record counts + the "NOT re-noted"
   ledger + sources used in PROGRESS.md.
6. Commit at chapter boundaries (a session death then costs only the chapter
   in flight; record the resume point in PROGRESS.md).

### 12.4 One wave: F0 (commissioner directive — a single footnote pass)

The footnote pass is **one wave, F0**, over the whole book (all 43 chapters),
not a multi-batch schedule. It runs like the register pass — chapter by
chapter, committing and pushing at every chapter boundary — but as a single
conversation. Because it is one session over the whole book, it leans on the
harness's context summarization; if a session ends before ch43, it RESUMES
(same F0 kickoff, from the recorded resume point in PROGRESS.md) rather than
spawning a new batch id.

**Internal exemplar checkpoint (the one mid-pass touchpoint).** Do **ch01
first** and, in the same session, pause once to present its before/after note
counts and 6-10 sample new notes spanning the four kinds (material culture,
social structure, customs/belief, institutions/money), so the commissioner can
calibrate density and voice before the rest of the book. On approval, ch01's
density is the reference for ch02-ch43; then F0 runs to completion without
further stops. (If the commissioner prefers no stop, ch01 still serves as the
self-set density reference.)

F0 closes with: whole-book note reconciliation (no duplicate notes across
first-appearances; every anchor resolves), final rebuild, qa_epub + epubcheck,
the final note count into PROGRESS.md, and `COMPLETION.md` rewritten to the
footnote-densified final edition. Only then is the book COMPLETE.

### 12.5 Verbatim F0 kickoff

The F0 reply (and any resume) pastes this kickoff verbatim:

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

When R9 completes the register pass, the R9 reply serves up this **F0** kickoff
in place of a "book complete" notice, and rewrites HANDOFF.md so its "Message
to paste into the next chat" is the F0 kickoff.
