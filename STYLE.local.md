# STYLE.local — book-specific ledger

The living style ledger for THIS book. The composed `STYLE.md` is a build
artifact from the shelf-wide layers; this file is where THIS book's own
decisions accumulate, and it is the only style file a session edits. Sessions
read `STYLE.md` and this file together.

Seeded at the first-chapter voice gate (CLAUDE.md Step 0c) and added to as the
book proceeds. Each rule records the correction, WHY the error happened, and
the fix, so the reasoning travels with the rule. A single correction is a data
point; the rule that prevents the whole class is the deliverable.

Tag every rule:
- `#book` — specific to this title (a character's voice, a term this book
  decides, a quirk of this author). Stays here forever.
- `#promote` — looks general (a whole-language or whole-genre tell). Stays here
  for this book, and is a candidate to lift into a `styles/` layer between
  books, once a second book corroborates it. See `styles/INDEX.md`.
- `#adopted` — added beside `#promote` when the rule was imported from a
  sibling book's ledger rather than discovered here. Adoption is not
  corroboration; surviving application here is validation (INDEX.md's
  promotion rule spells out the difference).

Hygiene: when a later batch sharpens an existing rule, AMEND it in place;
never append a second copy of the same rule further down (a real ledger grew
duplicate contraction rules this way, and the two drifted).

(Obeys CLAUDE.md rule 6: no em dashes in this file's own prose except inside
quoted before/after examples.)

## Voice sharpening (if this book has a nameable authorial voice)

_Two lines fixing the genre layer's generic voice target to THIS author: who
they read like in English, their signature registers. Fill at the voice gate._

## DELIBERATE devices to PRESERVE (the KEEP list)

_Fill at the voice gate; grow as the book reveals itself. Everything a
mechanical sweep, a blind critique, or a later revision pass must NOT "fix":
the author's structural devices (anaphora, one-line punch paragraphs,
parity-locked parallelisms), load-bearing quoted verse and allusion, the
partisan register where it is content, deliberately formal speakers, quoted
documents, and anything sitting inside a note or figure anchor. Every book
that ran a revision pass needed this list; the passes over-corrected two or
three of these when it was missing or stale, and the diff had to be searched
for them afterward. Blind critics reliably flag load-bearing quotations as
"vague or purple"; this list is what the adjudication step checks before
accepting such a finding._

## Consistency canon (ONE decision, book-wide; decide at setup or the gate)

_Decisions that bind body, notes, glossary, and book.json titles alike._

- **Date format: "Month D, YYYY."** Shelf default. Adopted as a Tier A
  conformance in the R1 retrofit; the R1 range (ch02-ch10, body and notes) is
  conformed, and `register_tics.py`'s `day-month-date` battery reads 0 over
  that range. NOT YET SWEPT book-wide: ch11 and up still carry day-first note
  dates ("28 January 1932") from the pre-retrofit batches; R2 through R4
  normalize their own ranges, and the book is uniform only after R4.
- **Spelling locale: American.** Shelf default. Real venue names keep their
  own spelling ("the Lyceum Theatre," "the Grand Theatre," "the Carlton
  Theatre") and are exempt from the `british-spelling` battery.
- **Organization handles:** one rendering per organ, in `glossary.json`
  (the term ledger). Named real events keep their attested capitalization
  (the May Thirtieth Movement, the January 28 Incident, the Great Revolution).
- **First appearance:** a recurring referent is footnoted at its FIRST
  appearance in the book. The pre-retrofit batches sometimes noted a referent
  at a later recurrence; R1 relocated the clean cases whose first appearance
  falls in ch02-ch10 (political tutelage moved ch18 -> ch05) and added fresh
  first-appearance notes for referents only mentioned in passing later
  (Suzhou Creek, Nanshi, the silver dollar, the boycott of Japanese goods).
  Remaining inversions are logged in HANDOFF for a whole-book reconciliation.

## Calibrated rulings (grows through the book)

_Empty until the first-chapter voice gate. Each entry:_

### RULE. <the general rule that prevents the whole class> [#book | #promote]
- **WHY IT HAPPENED.** <the source-language or process cause, so the class is
  recognizable next time>
- **FIX.** <before, then after>
- **CHECK.** <the script or the read that catches a recurrence>

## Decided renderings (this book's word-level ledger)

_One rendering per recurring item, like the glossary but for diction and
function words. Wrong form on the left, decided form on the right. Grows through
the book. Full ledger in `glossary.json`; the authority conformances land here._

- 老闸捕房: "the Laozha Police Station" -> **"the Louza police station"** (R1,
  authority name; Louza is the attested English of the SMP station).
- 吴淞口: "the Wusong bar" -> **"the mouth of the Wusong River"** (R1, authority;
  the ch13 occurrence conformed in R2).
- 马斯南路: "Massenet Road" -> **"Route Massenet"** (R2, authority; ch11, 2
  occurrences, the ch11 note anchor moved and its body reglossed).
- 海格路: "Haige Road" -> **"Avenue Haig"** (R2, authority; ch11, 1 occurrence,
  the ch11 'Zhaozhujiao Road' note body reglossed).
- 大美晚报: "Da Mei Wan Bao" -> **"the Shanghai Evening Post and Mercury"** (R3,
  authority; ch22, 1 occurrence, the ch22 note anchor moved to the English masthead
  and its body reglossed; glossary flipped to "decided").
- 反省院: "the Reflection Institute" -> **"reflection institute"** (R3, authority
  CASE fix; ch22, 1 occurrence, generic lowercased, the proper "Capital Reflection
  Institute" kept capitalized; the ch22 note anchor moved and its body opening
  lowercased; glossary flipped to "decided").
- 吴淞口: the ch27 occurrence conformed in R3 ("The Guisheng came in across the
  mouth of the Wusong River"); the scenes.json ch27 break string updated in the
  same pass so the divider still renders.
- "a piece of theatre" -> **"a piece of theater"** (R3, American-spelling locale
  conformance; ch27, x2). Real concession venue names (the Lehua Theatre etc.)
  keep their period "Theatre" spelling and stay exempt.
- 吴淞口: the ch34 (x2) and ch35 (x2) reading occurrences conformed in R4 ("the
  Wusong bar" -> "the mouth of the Wusong River"), the last reading-text strays
  book-wide; out/ch34_en.json and out/ch35_en.json synced.
- 白区: "the White area" -> **"the White areas"** (R4, authority number). It does
  NOT appear in the reading text anywhere book-wide; conformed only in the ch11
  note body (ch06 already plural) and flipped to "decided" in glossary.json.
- Dates -> "Month D, YYYY": the last day-first dates in the book (all 11 in the
  ch37 appendix reading text, plus note-body dates in ch30/ch33/ch35/ch37) were
  normalized in R4; register_tics day-month-date now reads 0 book-wide. The book
  is uniform after R4. (COMPLETE across R1-R4.)
