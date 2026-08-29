# HANDOFF — A Thousand Li of Rivers and Mountains (千里江山图), Sun Ganlu

The book is fully translated (37 units, qa green). This is the ANNOTATION
RETROFIT (ASSESSMENT.md section 6): four consolidated rounds densify the
footnote apparatus to the directive band and fold the Tier A conformances,
one range at a time. R1 (ch02-ch10) is DONE. Next is R2.

## Message to paste into the next chat

```
Read CLAUDE.md in full (it is now the v2.4 doctrine; the working rules at the
top are non-negotiable), then STYLE.md and STYLE.local.md together, then
HANDOFF.md, then book.json. We are in the annotation retrofit of 《千里江山图》
(A Thousand Li of Rivers and Mountains, Sun Ganlu, 2022), an already-complete
annotated English EPUB. The working branch is claude/thousand-li (ONE branch;
move any stray work onto it and delete the stray). The deliverable is
out/A Thousand Li of Rivers and Mountains.epub (build to that exact path).

Step 0 (doctrine upgrade) is already DONE on this branch; do NOT redo it. If
data/src/ is missing (it is gitignored), run scripts/ingest_epub.py source.epub
to recreate it.

Do densification round R2 = ch11 The Tenant, ch12 A Letter from Afar, ch13 The
Revolving Door, ch14 New Year's Eve, ch15 Code Words, ch16 The Bank, ch17 The
Suitcase, ch18 The Maochang Coal Company, ch19 February (nine units; four
rounds cover the whole book). Densify toward the directive band (aim ~30-40
notes per chapter), THINNEST-FIRST within the round: read the per-chapter note
counts from notes.json and give the currently-thinnest chapters the most new
notes. Do NOT pad: a note must say something a no-background reader needs, and
"notes added just to add them" is the failure mode. Where a short or heavily
interior chapter genuinely caps below the band, say so honestly in PROGRESS.md
rather than padding (R1 landed ~14/chapter for exactly this reason).

Sourcing and fact-checking (identical to R1):
- Source first-appearance candidates from glossary.json (the term ledger) and
  CLAUDE.md's four coverage domains, plus the lost-in-translation idiom/
  allusion/forms-of-address layer.
- FIRST-APPEARANCE DISCIPLINE IS CRITICAL. Before writing any note, grep the
  WHOLE notes.json (all units, anchors AND bodies) for the referent: many
  early referents were footnoted by the original batches at a LATER
  recurrence, and a second note would duplicate. If a referent's dedicated
  note sits later than its first appearance in ch11-ch19, RELOCATE it (add at
  first appearance, remove/trim the later one) unless the later placement is a
  deliberate plot-payoff (e.g. Garrick at ch23). If it is only MENTIONED in a
  later note (not dedicatedly noted), add a fresh first-appearance note. Never
  create a duplicate. Log any inversion you leave for the whole-book
  reconciliation.
- Every new note is fact-checked against REAL scholarship (Wikipedia EN/ZH,
  Baidu Baike, academic/government/museum sources). NEVER Grok, Grokipedia, or
  any AI-written source. Use subagents with web access for the research; have
  them return sourced facts plus a real-vs-fiction and corroborated/
  uncorroborated/invention verdict, and state that verdict IN each note.

Note mechanics (match the existing bodies exactly):
- Bodies are XHTML with NUMERIC character references only (&#8212; em, &#8211;
  en, &#160; nbsp, &#183; middot), STRAIGHT single quotes for 'quoted terms'
  (the existing bodies use 0x27, not curly), and LITERAL Chinese characters.
  A named entity in a body breaks the build; apply_edits.py refuses one.
- Anchors must be VERBATIM substrings of the reading text (mind that
  apostrophes in the body prose are straight 0x27 but nested quotes may be
  curly; the reading text uses curly double quotes). A new anchor must NOT
  contain, or be contained by, another anchor in the same unit that shares its
  end position, or the builder inverts the two note numbers (this bit R1 once:
  a ch02 anchor contained the existing "Longhua Garrison Command"). Prefer
  distinctive multi-word anchors that end at a clean point.
- Pipeline per unit: write edits/<id>_edits.md in the apply_edits grammar
  (### <label> TOUCH for a prose conformance with OLD:/NEW:; NOTE-ANCHOR with
  OLD:/NEW: to move an anchor a conformance breaks; NOTE-ADD with ANCHOR:/NOTE:
  for each new note). Run scripts/anchor_check.py <id>, then
  scripts/apply_edits.py <id> ... (it appends notes to notes.json via
  json.dump, verifies each new anchor against the post-edit reading text, and
  refuses named entities and duplicates).

Fold the Tier A conformances that fall in ch11-ch19, content otherwise FROZEN:
- Names (authority conformances), with glossary.json updated in lockstep and a
  NOTE-ANCHOR move for any existing note whose anchor the rename breaks:
  马斯南路 Massenet Road -> Route Massenet (first appears ch11; the ch11 note is
  anchored "Massenet Road", so move the anchor in the same pass). GREP the
  range for the other authority names and conform any that appear:
  大美晚报 Da Mei Wan Bao -> the Shanghai Evening Post and Mercury; and confirm
  the R1 conformances (老闸 Louza, 吴淞口 the mouth of the Wusong River) do not
  recur unconformed.
- Dates -> "Month Day, Year": normalize any day-first date in the reading text
  AND in the ch11-ch19 note bodies (the pre-retrofit note bodies carry
  day-first forms like "28 January 1932"; reorder them to "January 28, 1932").
  Leave Republican-reckoning and lunar dates as period voice and footnote
  them. register_tics.py's day-month-date battery should read 0 over the range
  when done.

Run scripts/check_structure.py --pairs data/zh/<id>.txt out/<id>_reading.md
(parity) and, on regenerated bilinguals where out/<id>_en.json exists,
scripts/check_numbers.py out/<id>_bilingual.md --noise check_noise.txt; run
scripts/register_tics.py --profile <the range>; run anchor_check before each
apply_edits. Then rebuild:
scripts/build_reading_epub.py "out/A Thousand Li of Rivers and Mountains.epub",
and run scripts/qa_epub.py on it until GREEN (it refuses on an unmatched note
anchor and on non-sequential numbering). Record what ran and what it found in
PROGRESS.md. Commit to claude/thousand-li and push. Cite chapters, never page
numbers. Never invent bridging text. Do not pause for approval mid-round.

When the round is done, your final chat reply MUST contain BOTH, every time:
(1) the stamped EPUB attached as a file, made with
python3 scripts/stamp_deliverable.py R2 (attach
out/A Thousand Li of Rivers and Mountains R2.epub), and (2) the R3 kickoff
message (R3 = ch20-ch28) pasted VERBATIM in a fenced code block in the same
reply. Also rewrite HANDOFF.md so its first section is that R3 kickoff. Writing
the kickoff only into HANDOFF.md does NOT satisfy this; it must be in the chat.
```

## What is DONE

- The whole book: 37 units translated, cover + front/back matter, full TOC,
  qa_epub PASS. See COMPLETION.md for the pre-retrofit completion report.
- Retrofit Step 0: doctrine upgraded to v2.4 (CLAUDE.md, styles/, STYLE.md +
  STYLE.local.md, REVISION_PLAN.template.md, all shared scripts the branch
  lacked). book.json gained deliverable/source_language/genre. See PROGRESS.md.
- Retrofit R1 = ch02-ch10: 73 new fact-checked notes (book-wide 217 -> 290),
  thinnest-first (ch05 +15). Tier A conformances in range folded (Louza,
  Wusong, dates). political-tutelage note relocated ch18 -> ch05. qa green.
  Per-chapter totals now: ch02 27, ch03 10, ch04 14, ch05 18, ch06 7, ch07 21,
  ch08 14, ch09 12, ch10 10.

## What is NEXT

- R2 = ch11-ch19 (see the kickoff above). R3 = ch20-ch28. R4 = ch29-ch37
  (the last round; ch37 is the two-part appendix). Adjust the split if a round
  runs long, but keep the whole book covered in four rounds.

## Deliverable rename (important)

The deliverable is now book.json "deliverable" =
out/A Thousand Li of Rivers and Mountains.epub (the full English title, colons
would become commas; there are none here). Validate with
stamp_deliverable.py --check; stamp a round copy with stamp_deliverable.py R<n>.
The old tracked out/thousand-li.epub is the PRE-retrofit snapshot and is now
stale; leave it until whole-book completion, when the final-named EPUB is
force-added (out/*.epub is gitignored).

## First-appearance inversions still open (for the whole-book reconciliation)

These referents are footnoted later than their first appearance; R1 did NOT
move them (either the later note is a deliberate reveal, or the content fits
the later spot better, or the first appearance is outside R1's range). A final
reconciliation pass should decide:
- Garrick / 茄力克 (first appears ch08; the dedicated note is at ch23, and is a
  DELIBERATE identity-reveal note that references ch08 — probably leave).
- the tram (first appears ch07; the note at ch29 is specific to the French
  Concession tram company — a general Settlement-tram note could go at ch07).
- the Central Liaison Bureau / 中央交通局 (first named ch07; the courier-lines
  note is at ch15).
- the Nanchang Field Headquarters (first named ch05; the note is at ch07,
  where Chiang's move to Nanchang is the actual subject — content fits ch07).

## Story state (unchanged by the retrofit)

The retrofit does not touch the story. For the plot, deaths, identities and
carry-forward renderings, see the archived batch notes in git history and
COMPLETION.md. Key renderings live in glossary.json (the single source of
truth). The novel: a fictional secret mission (evacuating the Communist
Central from Shanghai, code-named "A Thousand Li of Rivers and Mountains")
against the real backdrop of the 1933 White-Terror underground; the closing
appendix frames it as homage to the real Longhua martyrs.

## Tooling / traps

- notes.json is now written at indent=2 (apply_edits.py's format); it was
  indent=1 before R1. Do not hand-reformat.
- The note-numbering trap: an anchor that contains another same-unit anchor
  with the same end position inverts the numbers; qa_epub catches it as
  "numbering is not sequential." Choose non-overlapping anchors.
- check_numbers.py needs a bilingual (out/<id>_bilingual.md, gitignored).
  Regenerate with make_bilingual.py <id> data/src/<file>.txt "<Title>"
  out/<id>_en.json for units that have an _en.json (ch06 onward). ch01-ch05
  have no _en.json; their numerals are unchanged by an annotation round.
- Reading-text content is FROZEN in the retrofit except the Tier A
  conformances; do not "fix" register in the reading text (register_tics hits
  in the frozen prose are informational this round).
- book.json is the LOGICAL structure. ch01 is an epigraph (no notes). ch37 is
  one chapter with two sections (ch37s01, ch37s02) from two source files.
- data/src/ and out/*_bilingual.md and out/*.epub are gitignored; tracked are
  out/*_reading.md, out/*_en.json, data/zh/*.txt, edits/*.md, notes.json,
  glossary.json, scenes.json, STYLE.md, STYLE.local.md.
