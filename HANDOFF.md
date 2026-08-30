# HANDOFF — A Thousand Li of Rivers and Mountains (千里江山图), Sun Ganlu

The book is fully translated (37 units, qa green). This is the ANNOTATION
RETROFIT (ASSESSMENT.md section 6): four consolidated rounds densify the
footnote apparatus to the directive band and fold the Tier A conformances,
one range at a time. R1 (ch02-ch10) and R2 (ch11-ch19) are DONE. Next is R3.

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
to that exact path).

Step 0 (doctrine upgrade) is already DONE on this branch; do NOT redo it. If
data/src/ is missing (it is gitignored), run scripts/ingest_epub.py source.epub
to recreate it.

Do densification round R3 = ch20 The Xingchang Apothecary, ch21 The Tanglong
Door, ch22 The Tiannan Teahouse, ch23 Garrick, ch24 Backstage, ch25 Jiaoli,
ch26 The Guisheng, ch27 The Gonghexiang Wharf, ch28 Xiaotaoyuan (nine units;
four rounds cover the whole book). Densify toward the directive band (aim ~30-40
notes per chapter), THINNEST-FIRST within the round: read the per-chapter note
counts from notes.json and give the currently-thinnest chapters the most new
notes (as of the R2 handoff the thinnest in range are ch24 5, ch27 5, ch26 6).
Do NOT pad: a note must say something a no-background reader needs, and "notes
added just to add them" is the failure mode. Where a short or heavily interior
chapter genuinely caps below the band, say so honestly in PROGRESS.md rather
than padding (R1 landed ~15/chapter and R2 ~2.6/chapter of NEW notes for exactly
this reason: the middle chapters recycle referents already footnoted at first
appearance; see the two "HONEST NOTE ON DENSITY" entries in PROGRESS.md). DENSITY
POLICY FOR R3: if the commissioner has said (in the chat that launches you, or in
CORRECTIONS.md) to push harder toward the band, the levers are to accept more
light material-culture/texture notes at the margin and to relocate EVERY
later-noted first-appearance referent into this round; absent that instruction,
hold to no-pad as R1 and R2 did.

Sourcing and fact-checking (identical to R1/R2):
- Source first-appearance candidates from glossary.json (the term ledger) and
  CLAUDE.md's four coverage domains, plus the lost-in-translation idiom/
  allusion/forms-of-address/tradecraft layer.
- FIRST-APPEARANCE DISCIPLINE IS CRITICAL. Before writing any note, grep the
  WHOLE notes.json (all units, anchors AND bodies) AND the ch01-ch19 reading
  files for the referent: most big referents (the concessions and their police,
  the Songhu Garrison and its Judge Advocate's office, the Special Operations
  Headquarters / Party Affairs Investigation Section, the Guangzhou Uprising, the
  August 7th Conference, the courier lines, Shen Bao, the Bund, the zhang measure)
  are ALREADY footnoted at first appearance in earlier rounds, and a second note
  would duplicate. If a referent's dedicated note sits later than its first
  appearance in ch20-ch28, RELOCATE it (add at first appearance, remove/trim the
  later one) unless the later placement is a deliberate plot-payoff (e.g. Garrick
  at ch23, which is an identity-reveal note that references its ch08 first
  appearance -- probably leave, but check). If a referent is only MENTIONED in a
  later note (not dedicatedly noted), add a fresh first-appearance note. Never
  create a duplicate. Log any inversion you leave for the whole-book reconciliation
  (the open ones so far: Zhonghui Trust Bank unnoted, first appears ch10; the
  Garrick brand first appears ch08, dedicated note at ch23; the tram first appears
  ch07, note at ch29; the Central Liaison Bureau first named ch07, note at ch15).
- Every new note is fact-checked against REAL scholarship (Wikipedia EN/ZH, Baidu
  Baike, academic/government/museum sources). NEVER Grok, Grokipedia, or any
  AI-written source. Use subagents with web access for the research; have them
  return sourced facts plus a real-vs-fiction and corroborated/uncorroborated/
  invention verdict, and state that verdict IN each note.

Note mechanics (match the existing bodies exactly):
- Bodies are XHTML with NUMERIC character references only (&#8212; em, &#8211;
  en, &#160; nbsp, &#183; middot), STRAIGHT single quotes for 'quoted terms' (the
  existing bodies use 0x27, not curly), and LITERAL Chinese characters. A named
  entity in a body breaks the build; apply_edits.py refuses one.
- Anchors must be VERBATIM substrings of the reading text (mind that apostrophes
  in the body prose are straight 0x27 but the reading text uses curly double
  quotes; anchor on a substring that does NOT span a curly quote). A new anchor
  must NOT contain, or be contained by, another anchor in the same unit that
  shares its end position, or the builder inverts the two note numbers (qa_epub
  catches it as non-sequential numbering). Prefer distinctive multi-word anchors
  ending at a clean point. Watch that you file each note in the RIGHT chapter
  (R2 mis-filed one line ch17-vs-ch16; apply_edits' verbatim-substring guard
  caught it).
- Pipeline per unit: write edits/<id>_edits.md in the apply_edits grammar
  (### <label> TOUCH for a prose conformance with OLD:/NEW:; NOTE-ANCHOR with
  OLD:/NEW: to move an anchor a conformance breaks; NOTE-ADD with ANCHOR:/NOTE:
  for each new note). Run scripts/anchor_check.py <id>, then
  scripts/apply_edits.py <id> ... (it appends notes to notes.json, verifies each
  new anchor against the post-edit reading text, and refuses named entities and
  duplicates). apply_edits.py writes notes.json only at the END of a successful
  run and cannot edit an EXISTING note body -- for date normalization and
  name-regloss inside existing bodies use a small guarded script like R2's
  scripts/patch_note_bodies.py (json.load/json.dump, ensure_ascii=False, indent=2;
  never a heredoc). If apply_edits aborts mid-run, revert any reading-file TOUCHes
  it already wrote (git checkout) before re-running, since notes.json was not
  written but the per-unit reading edits were.

Fold the Tier A conformances that fall in ch20-ch28, content otherwise FROZEN.
The authority-deviation table is ASSESSMENT.md section 2 and the binding forms
are in authority.json (keyed under "thousand-li"); GREP ch20-ch28 for each and
conform any that appear, with glossary.json in lockstep and a NOTE-ANCHOR move
for any existing note whose anchor a rename breaks:
- 大美晚报 Da Mei Wan Bao -> the Shanghai Evening Post and Mercury (appears ch22;
  there is an existing ch22 note anchored "Da Mei Wan Bao", so MOVE that anchor
  and regloss the body in the same pass).
- 反省院 the Reflection Institute -> reflection institute (a CASE fix; appears
  ch22; lowercase the generic institution, capitalize only in a proper name).
- 吴淞口 the Wusong bar -> the mouth of the Wusong River (appears ch27 as
  "The Guisheng came in across the Wusong bar" -- and that exact phrase is ALSO
  the ch27 scene-break anchor in scenes.json, so conform the reading text AND
  update the scenes.json ch27 "breaks" string in the same pass, then rebuild and
  re-grep class="brk" to confirm the break still renders). R1 did ch07, R2 ch13;
  grep the range for any further occurrences.
- 海格路 Avenue Haig, 马斯南路 Route Massenet: done in R2 (ch11); grep anyway in case
  either recurs in ch20-ch28.
- 白区 "the White area" -> "the White areas" (a number fix, ~13 occurrences
  book-wide); grep the range and conform those that fall in it.
- Dates -> "Month Day, Year": normalize any day-first date in the reading text
  AND in the ch20-ch28 note bodies. The known ch20-ch28 note-body day-first dates
  are: ch20 "23 June 1925"; ch22 "16 January 1933", "20 August 1925", "23 October",
  "13 November"; ch24 "20 March 1926"; ch28 "30 November 1931" (reorder each to
  Month Day, Year, or Month Day for a bare month-day). Leave Republican-reckoning
  and lunar dates as period voice and footnote them. register_tics.py's
  day-month-date battery should read 0 over the reading text of the range when done.

Scene-break review (COMMISSIONER DIRECTIVE, carried forward from R2 to R3 and R4).
As part of each round, review every unit in the round for SCENE CHANGES that lack
a divider and add them to scenes.json. The principle, calibrated with the
commissioner on the ch02 raid:
- ADD a break at a genuine scene change: a real jump in place, time AND vantage,
  where the new scene stands apart from the last (the establishing vignettes of
  ch02, each character at a different place at the same hour, are the model).
- Do NOT add a break at a camera-flip inside a continuous cross-cut sequence, or
  where the cut is causally or aurally sutured (an order and its immediate
  consequence, one scene hearing what another does). Those stay hard cuts; a
  divider there over-segments and is "too much." A perspective change ALONE is not
  enough; it must be a new SCENE. When in doubt, leave it hard. (R2 found NO new
  breaks warranted in ch11-ch19: ch11/ch12 are single-scene and the rest were
  already segmented at their genuine scene changes; that is a legitimate outcome
  -- do not force breaks.)
- Mechanics: add to the unit's scenes.json entry a "breaks" string = the opening
  words of the paragraph that begins the new scene, VERBATIM from the reading file
  (include the leading curly quote if the paragraph opens on dialogue; the builder
  matches startswith), or a "datelines" string = a terse time/place header line,
  verbatim, rendered centered. Verify each string against out/<id>_reading.md;
  after building, grep the chapter xhtml for class="brk" / class="dateline" to
  confirm the counts. Record in PROGRESS.md what you added per chapter and, for
  borderline cuts, why you left them hard. Several chapters have NO breaks yet
  (ch20, ch22, ch24, ch29, ch34, ch36-ch37); some are genuinely single-scene, so
  do NOT force breaks on them. Carry this scene-break directive forward into the
  R4 kickoff you write.

Run scripts/check_structure.py --pairs data/zh/<id>.txt out/<id>_reading.md
(parity) and, on regenerated bilinguals (make_bilingual.py <id> data/src/<file>.txt
"<中文标题>" out/<id>_en.json, source file per book.json text_file),
scripts/check_numbers.py out/<id>_bilingual.md --noise check_noise.txt; run
scripts/register_tics.py --profile <the range>; run anchor_check before each
apply_edits. Keep out/<id>_en.json synced with any reading-text conformance
(R1/R2 precedent). Then rebuild:
scripts/build_reading_epub.py "out/A Thousand Li of Rivers and Mountains.epub",
and run scripts/qa_epub.py on it until GREEN (it refuses on an unmatched note
anchor and on non-sequential numbering). Record what ran and what it found in
PROGRESS.md. Commit to claude/thousand-li and push. Cite chapters, never page
numbers. Never invent bridging text. Do not pause for approval mid-round.

When the round is done, your final chat reply MUST contain BOTH, every time:
(1) the stamped EPUB attached as a file, made with
python3 scripts/stamp_deliverable.py R3 (attach
out/A Thousand Li of Rivers and Mountains R3.epub), and (2) the R4 kickoff message
(R4 = ch29-ch37, the last round; ch36 is the unsigned letter and ch37 the two-part
appendix, both dense with real names/places/dates to fact-check, and R4 also does
any whole-book reconciliation and final QA) pasted VERBATIM in a fenced code block
in the same reply. Also rewrite HANDOFF.md so its first section is that R4 kickoff.
Writing the kickoff only into HANDOFF.md does NOT satisfy this; it must be in the
chat.
```

## What is DONE

- The whole book: 37 units translated, cover + front/back matter, full TOC,
  qa_epub PASS. See COMPLETION.md for the pre-retrofit completion report.
- Retrofit Step 0: doctrine upgraded to v2.4 (CLAUDE.md, styles/, STYLE.md +
  STYLE.local.md, REVISION_PLAN.template.md, all shared scripts). book.json gained
  deliverable/source_language/genre.
- Retrofit R1 = ch02-ch10: 79 new notes (217 -> 296). Tier A in range folded
  (Louza, Wusong ch07, dates). Per-chapter: ch02 28, ch03 11, ch04 14, ch05 18,
  ch06 8, ch07 22, ch08 15, ch09 12, ch10 11.
- Retrofit R2 = ch11-ch19: 23 new fact-checked notes (296 -> 319), thinnest-first.
  Tier A in range folded: ch11 Route Massenet (x2, note anchor moved + body
  reglossed) and Avenue Haig (note body reglossed), ch13 the mouth of the Wusong
  River; glossary.json + out/ch11_en.json + out/ch13_en.json synced; 12 note-body
  day-first dates normalized. Scene-break review: no new breaks warranted.
  qa green. Per-chapter: ch11 12, ch12 15, ch13 10, ch14 7, ch15 7, ch16 10,
  ch17 5, ch18 9, ch19 5. See PROGRESS.md for the full R2 record and the honest
  density note.

## What is NEXT

- R3 = ch20-ch28 (see the kickoff above). R4 = ch29-ch37 (the last round; ch37
  is the two-part appendix). Adjust the split if a round runs long, but keep the
  whole book covered in four rounds.

## Deliverable

book.json "deliverable" = out/A Thousand Li of Rivers and Mountains.epub (full
English title; validate with stamp_deliverable.py --check; stamp a round copy
with stamp_deliverable.py R<n>). The old tracked out/thousand-li.epub is the
PRE-retrofit snapshot and is stale; leave it until whole-book completion, when
the final-named EPUB is force-added (out/*.epub is gitignored).

## First-appearance inversions still open (for the whole-book reconciliation)

- Zhonghui Trust Bank (中汇银行): first appears ch10, UNNOTED book-wide; real Du
  Yuesheng bank (1929), lightly renamed. Add a first-appearance note at ch10.
- Garrick / 茄力克 (first appears ch08; the dedicated note is at ch23, a deliberate
  identity-reveal note referencing ch08 -- probably leave).
- the tram (first appears ch07; the note at ch29 is specific to the French
  Concession tram company; a general Settlement-tram note could go at ch07).
- the Central Liaison Bureau / 中央交通局 (first named ch07; the courier-lines note
  is at ch15).
- the Nanchang Field Headquarters (first named ch05; the note is at ch07, where
  Chiang's move to Nanchang is the actual subject -- content fits ch07).
- Letters from Afar: first-appearance note added at ch12 in R2; the ch26 note is a
  distinct three-title gloss and stays put.

## Story state (unchanged by the retrofit)

The retrofit does not touch the story. For plot, deaths, identities and
carry-forward renderings, see the archived batch notes in git history and
COMPLETION.md; key renderings live in glossary.json (the single source of truth).

## Tooling / traps

- notes.json is written at indent=2 (apply_edits.py's format). Do not hand-reformat.
- Note-numbering trap: an anchor that contains another same-unit anchor with the
  same end position inverts the numbers; qa_epub catches it as "numbering is not
  sequential." Choose non-overlapping anchors.
- check_numbers.py needs a bilingual (out/<id>_bilingual.md, gitignored).
  Regenerate with make_bilingual.py <id> data/src/<file>.txt "<中文标题>"
  out/<id>_en.json (all of ch06 onward have _en.json; ch01-ch05 do not).
- Reading-text content is FROZEN in the retrofit except the Tier A conformances;
  register_tics hits in the frozen prose are informational this round.
- scripts/patch_note_bodies.py (R2) is the pattern for editing EXISTING note
  bodies (dates, name reglosses) that apply_edits.py cannot touch.
- book.json is the LOGICAL structure. ch01 is an epigraph (no notes). ch37 is one
  chapter with two sections (ch37s01, ch37s02) from two source files.
- data/src/ and out/*_bilingual.md and out/*.epub are gitignored; tracked are
  out/*_reading.md, out/*_en.json, data/zh/*.txt, edits/*.md, notes.json,
  glossary.json, scenes.json, STYLE.md, STYLE.local.md, scripts/*.
