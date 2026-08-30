# HANDOFF — A Thousand Li of Rivers and Mountains (千里江山图), Sun Ganlu

The book is fully translated (37 units, qa green). This is the ANNOTATION
RETROFIT (ASSESSMENT.md section 6): four consolidated rounds densify the
footnote apparatus to the directive band and fold the Tier A conformances,
one range at a time. R1 (ch02-ch10), R2 (ch11-ch19) and R3 (ch20-ch28) are
DONE. Next is R4 = ch29-ch37, the LAST round.

## Message to paste into the next chat

```
Read CLAUDE.md in full (it is the v2.4 doctrine; the working rules at the top
are non-negotiable), then ASSESSMENT.md (the commissioning brief; section 6 is
the four-round plan, section 2 is the authority-deviation table), then STYLE.md
and STYLE.local.md together, then HANDOFF.md, then book.json. We are in the
annotation retrofit of 《千里江山图》 (A Thousand Li of Rivers and Mountains, Sun
Ganlu, 2022), an already-complete annotated English EPUB. The working branch is
claude/thousand-li (ONE branch; move any stray work onto it and delete the
stray). The deliverable is out/A Thousand Li of Rivers and Mountains.epub (build
to that exact path). NOTE FOR A FRESH CHECKOUT: the R1-R3 retrofit work lives on
origin/claude/thousand-li; if your local branch is behind (e.g. it sits at the
pre-retrofit B12 "book complete" state and ASSESSMENT.md / authority.json /
scripts/apply_edits.py are missing), fast-forward to origin/claude/thousand-li
before doing anything.

Step 0 (doctrine upgrade) is already DONE on this branch; do NOT redo it. If
data/src/ is missing (it is gitignored), run scripts/ingest_epub.py source.epub
to recreate it.

Do densification round R4 = ch29 The Dyeworks Drying Ground, ch30 The Yangzhou
Master, ch31 The Cemetery, ch32 The Dairy Shed, ch33 North Station, ch34 Fish
Congee, ch35 The Huangpu River, ch36 An Unsigned Letter, ch37 Appendix (nine
units; this is the last of the four rounds). Densify toward the directive band
(aim ~30-40 notes per chapter), THINNEST-FIRST within the round: read the
per-chapter note counts from notes.json and give the currently-thinnest chapters
the most new notes (as of the R3 handoff the thinnest in range are ch36 1, ch29
2, ch33 2, ch35 2, ch31 3, ch32 3; ch30 9 and ch37 6 are the densest). Do NOT
pad: a note must say something a no-background reader needs, and "notes added
just to add them" is the failure mode. Where a short or heavily interior chapter
genuinely caps below the band, say so honestly in PROGRESS.md rather than padding
(R1 landed ~15/chapter, R2 ~2.6/chapter and R3 ~1.4/chapter of NEW notes for
exactly this reason: the later chapters recycle referents already footnoted at
first appearance; see the three "HONEST NOTE ON DENSITY" entries in PROGRESS.md).
DENSITY POLICY FOR R4: if the commissioner has said (in the chat that launches
you, or in CORRECTIONS.md) to push harder toward the band, the levers are to
accept more light material-culture/texture notes at the margin and to relocate
EVERY later-noted first-appearance referent into this round; absent that
instruction, hold to no-pad as R1-R3 did.

ch36 (An Unsigned Letter, styled 龙华牺牲烈士的遗物, "a relic of a martyr who died at
Longhua") and ch37 (the two-part Appendix, 材料一 / 材料二 "Members of the CCP
Underground Organization Who Died in the Related Operations") are the book's
homage payoff: they frame the whole fiction as recovered history and are DENSE
with real names, places, dates and organizations presented as documentary.
Fact-check EVERY named person, place, date and organization there against real
scholarship and say in each note which are real and which are the novel's
invention, and whether the claim is corroborated / uncorroborated / contradicted.
This is the careful, paranoid work of the round; treat it as the main event.
The real 4 April 1933 Longhua execution of the "twenty-four martyrs" is the
anchor fact; verify names against it.

Sourcing and fact-checking (identical to R1-R3):
- Source first-appearance candidates from glossary.json (the term ledger) and
  CLAUDE.md's four coverage domains, plus the lost-in-translation idiom/allusion/
  forms-of-address/tradecraft layer.
- FIRST-APPEARANCE DISCIPLINE IS CRITICAL. Before writing any note, grep the WHOLE
  notes.json (all units, anchors AND bodies) AND the ch01-ch28 reading files for
  the referent: most big referents are ALREADY footnoted at first appearance in
  earlier rounds, and a second note would duplicate. If a referent's dedicated
  note sits later than its first appearance in ch29-ch37, RELOCATE it (add at
  first appearance, remove/trim the later one) unless the later placement is a
  deliberate plot-payoff. If a referent is only MENTIONED in a later note (not
  dedicatedly noted), add a fresh first-appearance note. Never create a duplicate.
- Every new note is fact-checked against REAL scholarship (Wikipedia EN/ZH, Baidu
  Baike, academic/government/museum sources). NEVER Grok, Grokipedia, or any
  AI-written source. Use subagents with web access for the research; have them
  return sourced facts plus a real-vs-fiction and corroborated/uncorroborated/
  invention verdict, and state that verdict IN each note.

Note mechanics (match the existing bodies exactly):
- Bodies are XHTML with NUMERIC character references only (&#8212; em, &#8211; en,
  &#160; nbsp, &#183; middot, &#176; degree, &#38; ampersand), STRAIGHT single
  quotes for 'quoted terms', and LITERAL Chinese characters. A NAMED entity in a
  body breaks the build; apply_edits.py refuses one (this includes &amp; -- use
  &#38;). The pre-retrofit ch23 notes contain &amp; and build fine, but new notes
  through apply_edits must use numeric refs.
- Anchors must be VERBATIM substrings of the reading text (mind that apostrophes
  in the reading text are straight 0x27 but double quotes are curly; anchor on a
  substring that does NOT span a curly quote). A note CAN be attached to a
  scenes.json dateline line (the builder inserts the marker inside the centered
  dateline; R3 did this for 立春 at ch23). Prefer distinctive multi-word anchors
  ending at a clean point. Watch that you file each note in the RIGHT chapter.
- Pipeline per unit: write edits/<id>_edits.md in the apply_edits grammar (### <label>
  TOUCH with OLD:/NEW: for a prose conformance; NOTE-ANCHOR with OLD:/NEW: to move
  an anchor a conformance breaks; NOTE-ADD with ANCHOR:/NOTE: for each new note).
  TOOLING TRAP (hit in R3): apply_edits.py scans only the 5 lines after a ### /
  NOTE-ANCHOR header for OLD:/NEW: and takes the LAST it sees, so two TOUCH or
  NOTE-ANCHOR blocks placed close together BLEED into each other and mis-apply.
  Put TWO blank lines between every TOUCH / NOTE-ANCHOR block. Verify the parse
  before applying (import parse_edits and print each extracted OLD with its count
  in the reading file; each must be 1). Run scripts/anchor_check.py <id>, then
  scripts/apply_edits.py <id> ... (it appends notes, verifies each new anchor
  against the post-edit reading text, and refuses named entities and duplicates).
  apply_edits.py writes notes.json only at the END of a successful run and cannot
  edit an EXISTING note body -- for date normalization and regloss inside existing
  bodies use a small guarded script like R3's scripts/patch_note_bodies_r3.py
  (json.load/json.dump, ensure_ascii=False, indent=2; never a heredoc). If
  apply_edits aborts mid-run, revert any reading-file TOUCHes it already wrote
  (git checkout) before re-running, since notes.json was not written but the
  per-unit reading edits were.

Fold the Tier A conformances that fall in ch29-ch37, content otherwise FROZEN.
The authority-deviation table is ASSESSMENT.md section 2 and the binding forms are
in authority.json (keyed under "thousand-li"); GREP ch29-ch37 for each and conform
any that appear, glossary.json in lockstep, a NOTE-ANCHOR move for any existing
note whose anchor a rename breaks, and out/<id>_en.json synced:
- 白区 "the White area" -> "the White areas" (number). It did NOT appear in the
  ch11-ch28 reading text; grep ch29-ch37 (and, for the reconciliation, the whole
  book) and conform any occurrence.
- 海格路 Avenue Haig, 马斯南路 Route Massenet, 吴淞口 the mouth of the Wusong River,
  大美晚报 the Shanghai Evening Post and Mercury, 反省院 reflection institute: all done
  in earlier rounds; grep the range in case any recurs (ch34/ch35 contain at least
  one authority term -- check which and conform if needed).
- Dates -> "Month D, YYYY": THIS IS THE BIG R4 TIER A JOB. The ch37 appendix
  reading text is full of day-first dates ("10 January", "16 January", "2
  February", "8 February", "4 April" many times, etc.) that must be normalized to
  "Month D, YYYY" (or "Month D" for a bare month-day) in the reading text AND in
  out/ch37a_en.json / ch37b_en.json. Note bodies with day-first dates: ch30 "17
  March", ch33 "28-29 January", ch35 "6 May", ch37 "4 April"/"5 April"/"7
  February"/"10 January" -- normalize via a patch_note_bodies script. Leave
  Republican-reckoning and lunar dates as period voice and footnote them.
  register_tics.py's day-month-date battery should read 0 over the ch29-ch37
  reading text when done (it currently flags the ch37 appendix dates).

Scene-break review (COMMISSIONER DIRECTIVE, carried forward through R4). Review
every unit in the round for SCENE CHANGES that lack a divider and add them to
scenes.json. The principle, calibrated on the ch02 raid: ADD a break at a genuine
scene change (a real jump in place, time AND vantage, the new scene standing apart
from the last); do NOT add at a camera-flip inside a continuous cross-cut, or a
causally/aurally sutured cut (an order and its immediate consequence, one scene
hearing what another does); a perspective change ALONE is not enough. When in
doubt, leave it hard (R2 found no new breaks in ch11-ch19, R3 none in ch20-ch28;
that is a legitimate outcome, do not force breaks). Mechanics: add to the unit's
scenes.json entry a "breaks" string = the opening words of the paragraph that
begins the new scene, VERBATIM from the reading file (include the leading curly
quote if it opens on dialogue; the builder matches startswith), or a "datelines"
string = a terse time/place header line, verbatim, centered. Verify each against
out/<id>_reading.md; after building, grep the chapter xhtml for class="brk" /
class="dateline" to confirm counts. Several ch29-ch37 chapters have NO breaks yet
(ch29, ch34, ch36, ch37); ch36 is a single short letter and ch37 is documentary
lists, so likely 0/0 each -- read and confirm, do not force. Record per chapter in
PROGRESS.md what you added and, for borderline cuts, why you left them hard.

Run scripts/check_structure.py --pairs data/zh/<id>.txt out/<id>_reading.md
(parity) and, on regenerated bilinguals (make_bilingual.py <id> data/src/<file>.txt
"<title>" out/<id>_en.json; source file per book.json text_file: ch29=32_part0030,
ch30=33_part0031, ch31=34_part0032, ch32=35_part0033, ch33=36_part0034,
ch34=37_part0035, ch35=38_part0036, ch36=39_part0037, ch37=40_part0038 AND
41_part0039 -- ch37 is ONE chapter with two H3 sections built from two source
files, its en.json split as ch37a_en.json / ch37b_en.json),
scripts/check_numbers.py out/<id>_bilingual.md --noise check_noise.txt; run
scripts/register_tics.py --profile <the range>; run anchor_check before each
apply_edits. Keep out/<id>_en.json synced with any reading-text conformance.

BECAUSE THIS IS THE LAST ROUND, also do the following instead of writing another
kickoff:
1. WHOLE-BOOK RECONCILIATION. Resolve the first-appearance inversions logged in
   PROGRESS.md and below: the tram (first appears ch07; the note is at ch29, in
   THIS range -- decide whether to relocate a general Settlement-tram note to ch07
   or leave the ch29 French-Concession-tram-company note as specific); Zhonghui
   Trust Bank (中汇银行, first appears ch10, UNNOTED book-wide -- add a first-
   appearance note at ch10, a real Du Yuesheng bank, 1929, lightly renamed); the
   Central Liaison Bureau (ch07 first named, note at ch15); the Peach Blossom
   Spring allusion (ch22 opera lyric, dedicated note at ch28 Xiaotaoyuan payoff --
   left). Grep-count the ~20 decided renderings across ALL built units for drift
   (glossary.json is the source of truth); confirm the TOC links all 37 units;
   confirm note numbering is sequential end to end (qa_epub checks this).
2. FINAL QA. Build, run qa_epub.py to green, spot-read across the spine for
   rendering drift.
3. Write a COMPLETION REPORT (update COMPLETION.md, which currently records the
   pre-retrofit state): the finished apparatus (final note count and per-chapter
   distribution before/after the retrofit), all Tier A conformances folded across
   R1-R4, the checks run book-wide, the residual uncertainties flagged in the
   notes, and the open items. Summarize it in the chat too.

Then rebuild: scripts/build_reading_epub.py "out/A Thousand Li of Rivers and
Mountains.epub", and run scripts/qa_epub.py on it until GREEN (it refuses on an
unmatched note anchor and on non-sequential numbering). Record what ran and what
it found in PROGRESS.md. Commit to claude/thousand-li and push. Cite chapters,
never page numbers. Never invent bridging text. Do not pause for approval mid-round.

When the round is done, your final chat reply MUST contain BOTH, every time:
(1) the stamped EPUB attached as a file, made with python3 scripts/stamp_deliverable.py
R4 (attach out/A Thousand Li of Rivers and Mountains R4.epub), and (2) since this
is the LAST round, the completion-report summary pasted into the chat (in place of
a next-round kickoff). Writing it only into COMPLETION.md does NOT satisfy this; it
must be in the chat.
```

## What is DONE

- The whole book: 37 units translated, cover + front/back matter, full TOC,
  qa_epub PASS. See COMPLETION.md for the pre-retrofit completion report.
- Retrofit Step 0: doctrine upgraded to v2.4 (CLAUDE.md, styles/, STYLE.md +
  STYLE.local.md, REVISION_PLAN.template.md, all shared scripts). book.json gained
  deliverable/source_language/genre.
- Retrofit R1 = ch02-ch10: 79 new notes (217 -> 296). Tier A in range folded.
- Retrofit R2 = ch11-ch19: 23 new notes (296 -> 319). Tier A in range folded
  (ch11 Route Massenet + Avenue Haig, ch13 the mouth of the Wusong River; 12
  note-body date normalizations). Scene-break review: no new breaks warranted.
- Retrofit R3 = ch20-ch28: 13 new fact-checked notes and 1 relocation (319 -> 331),
  thinnest-first (ch24 5->8, ch27 5->7, ch26 6->9). New notes: ch21 Jardine Matheson
  + the Xiguan newspaper-street/Press-Association/clipping-bureau apparatus; ch22
  the Tanka boat people; ch23 the Beginning of Spring solar term (on the dateline);
  ch24 the comprador, Canton embroidery, the Dashatou airfield; ch25 the salted-fish
  idiom (咸鱼翻身); ch26 the Qinhuai River, Minnan tangerine-red cakes, and the
  osmanthus-sugared-taro note RELOCATED from ch31 (its first appearance is ch26);
  ch27 the Zhoushan Archipelago and 瞒天过海. Tier A folded: ch22 大美晚报 -> the
  Shanghai Evening Post and Mercury (note anchor moved + body reglossed, glossary
  "decided") and 反省院 -> reflection institute (case, note anchor moved + body
  lowercased, glossary "decided"); ch27 吴淞口 -> the mouth of the Wusong River
  (reading + scenes.json break + en.json in one pass) and "a piece of theatre" ->
  "a piece of theater" (x2); 7 note-body date normalizations. glossary.json,
  out/ch22_en.json and out/ch27_en.json synced. Scene-break review: no new breaks
  warranted. qa green, 331 notes. See PROGRESS.md for the full R3 record and the
  honest density note.

## What is NEXT

- R4 = ch29-ch37 (see the kickoff above), the LAST round; ch36 is the unsigned
  letter and ch37 the two-part appendix, both dense with real names/places/dates to
  fact-check. R4 also does the whole-book reconciliation, final QA, and a COMPLETION
  REPORT instead of another kickoff.

## Deliverable

book.json "deliverable" = out/A Thousand Li of Rivers and Mountains.epub (full
English title; validate with stamp_deliverable.py --check; stamp a round copy with
stamp_deliverable.py R<n>). The old tracked out/thousand-li.epub is the PRE-retrofit
snapshot and is stale; leave it until whole-book completion, when the final-named
EPUB is force-added (out/*.epub is gitignored).

## First-appearance inversions still open (for the whole-book reconciliation in R4)

- Zhonghui Trust Bank (中汇银行): first appears ch10, UNNOTED book-wide; real Du
  Yuesheng bank (1929), lightly renamed. Add a first-appearance note at ch10.
- the tram (first appears ch07; the note at ch29 is specific to the French
  Concession tram company; a general Settlement-tram note could go at ch07). ch29
  is in the R4 range, so decide it there.
- the Central Liaison Bureau / 中央交通局 (first named ch07; the courier-lines note is
  at ch15).
- the Peach Blossom Spring / Tao Yuanming allusion: a ch22 opera lyric glances by it;
  the dedicated note is at ch28 (the Xiaotaoyuan title payoff) and stays.
- (Closed in R3) the osmanthus-sugared taro shoots note relocated ch31 -> ch26.
- (Closed earlier) Letters from Afar first-appearance note added at ch12; Garrick's
  ch23 identity-reveal note kept (deliberate payoff, checked).

## Story state (unchanged by the retrofit)

The retrofit does not touch the story. For plot, deaths, identities and
carry-forward renderings, see the archived batch notes in git history and
COMPLETION.md; key renderings live in glossary.json (the single source of truth).

## Tooling / traps

- notes.json is written at indent=2 (apply_edits.py's format). Do not hand-reformat.
- apply_edits.py OLD/NEW window bleed: put TWO blank lines between adjacent TOUCH /
  NOTE-ANCHOR blocks (R3 trap; the parser scans only 5 lines and takes the last
  OLD/NEW). Verify the parse before applying.
- Note-numbering trap: an anchor that contains another same-unit anchor with the
  same end position inverts the numbers; qa_epub catches it as "numbering is not
  sequential." Choose non-overlapping anchors.
- A note CAN sit on a scenes.json dateline line (the builder inserts the marker
  inside the centered dateline; R3 did this at ch23).
- check_numbers.py needs a bilingual (out/<id>_bilingual.md, gitignored). Regenerate
  with make_bilingual.py <id> data/src/<file>.txt "<title>" out/<id>_en.json.
- Note bodies: numeric character references only, never named entities (&amp; -> &#38;).
- Reading-text content is FROZEN in the retrofit except the Tier A conformances;
  register_tics hits in the frozen prose are informational this round.
- scripts/patch_note_bodies_r3.py (R3) and scripts/patch_note_bodies.py (R2) are the
  pattern for editing EXISTING note bodies (dates, reglosses) and removing a note.
- book.json is the LOGICAL structure. ch01 is an epigraph (no notes). ch37 is one
  chapter with two sections (ch37s01, ch37s02) from two source files, its reading.md
  using "### " H3 headings and its English split as ch37a_en.json / ch37b_en.json.
- data/src/ and out/*_bilingual.md and out/*.epub are gitignored; tracked are
  out/*_reading.md, out/*_en.json, data/zh/*.txt, edits/*.md, notes.json,
  glossary.json, scenes.json, STYLE.md, STYLE.local.md, scripts/*.
