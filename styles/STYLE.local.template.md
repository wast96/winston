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

_Decisions that bind body, notes, glossary, and book.json titles alike. At
minimum: date format (shelf default "Month D, YYYY") and spelling locale
(shelf default American), decided BEFORE Batch 1 per `_base.md`; the
narration-contraction dial calibrated at the voice gate (shelf default in
`genre-nonfiction.md`); organization handles (one per organ, forever);
capitalization of named events. Three books shipped a mid-book date-format
flip because this canon did not exist yet; write the decision down here the
moment it is made._

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
the book._
