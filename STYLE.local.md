# STYLE.local.md — The Tragedy of the Chinese Revolution (annotated edition)

This book is an **annotated English edition, not a translation.** The shelf's
composed `STYLE.md` (base + lang + genre) is not used here: there is no source
language to render, no register to control, and `compose_style.py` has no
`lang-en` layer. This file is therefore the whole style contract for the book.
It is the only style file a session edits; read it at the start of every batch.

## The reading text is Isaacs's own prose — preserve it

- The body of `out/<id>_reading.md` is **Harold Isaacs's 1938 text, verbatim.**
  Do not rewrite, modernize, smooth, abridge, or "improve" a single sentence.
  Rule 4 (never invent bridging text) binds here as hard as in any translation:
  the failure mode is a plausible sentence that Isaacs did not write.
- Extraction is a **faithful reset**, not editing. Mechanical fixes only:
  rejoin words split by a line-break hyphen (`produc-\ntivity` → `productivity`,
  but keep real hyphens: `anti-imperialist`); fold the drop-cap initial back
  into its word (`O` + `n the fringes` → `On the fringes`); strip running heads
  (`TRAGEDY OF THE CHINESE REVOLUTION`, the chapter title) and folios; drop the
  in-text superscript reference digits from the prose (they become footnote
  anchors instead). Preserve paragraph breaks exactly.
- **Keep Isaacs's spelling and usage** as printed — British 1938 forms
  (`labour`, `Soviet`, `centre` where he uses it), his punctuation, his
  capitalisation. His em dashes stay. Do not Americanize his text.

## Two note layers, distinguished by NUMERAL SYSTEM (commissioner decision)

- **Author's notes** = Isaacs's own numbered endnotes, moved to the point they
  document. Body is his endnote text, verbatim. Marked in **arabic (1, 2, 3)**,
  exactly as he numbered them.
- **Editorial notes** = the new reader-facing layer. Marked in **roman
  (i, ii, iii)** so the reader tells the two apart at a glance. Do NOT prefix
  them with "Ed." (superseded); the roman numeral is the signal. (Isaacs uses
  arabic, so editorial gets roman; had he used roman, editorial would be
  arabic.)
- **Numbering restarts each chapter** for both streams (keeps roman marks short
  and matches Isaacs's per-chapter scheme). notes.json entries carry a kind:
  editorial notes set `"ed": true`; author notes omit it. The builder keeps two
  per-chapter counters and renders arabic vs lowercase-roman superscripts, with
  distinct ref/backlink ids per stream. (Implemented and QA'd in Batch 1.)

## Editorial-note register and content

- **American English** in editorial prose (shelf default), even though Isaacs's
  text is British — the two voices are meant to be distinct. Dates: **Month D,
  YYYY**.
- Concise and factual. Say who/what/when, why it matters *here*, and the
  fact-check verdict where checkable: **corroborated / uncorroborated /
  contradicted**, naming the real source (Wikipedia, Baidu Baike, academic
  works — **never** Grok/Grokipedia or any AI-written reference, rule 5).
- Generous density (commissioner directive): assume **no** background in modern
  Chinese history. Every named person, place, institution, office, party/
  Comintern body, and period term a well-read Western reader might not place
  gets a note at **first appearance** — who they are, their fate, the stakes.
  A bare "X was a person" is padding; a note must say something.
- Mark the author-as-interested-witness: where Isaacs's Trotskyist standpoint
  shapes a factual claim, note it with evidence — without arguing the politics.

## Names — keep Wade-Giles in the text, give pinyin in the apparatus

- Isaacs writes 1930s **Wade-Giles** (Chiang Kai-shek, Borodin, Kuomintang,
  Chang Tso-lin, Wuhan, Canton). **His forms stay in the body.**
- The glossary and the first-appearance editorial note give the **modern pinyin**
  and, where useful, the **Chinese characters**, so a name here can be matched
  to a present-day account. Glossary key = hanzi; `en` = the Wade-Giles form
  Isaacs uses; `pinyin` = modern pinyin; `note` = identification.
- One decided rendering per referent (glossary is the ledger). Consult
  `authority.json` for shelf-wide agreement before deciding a form.

## Formatting

- Block quotations (Isaacs quotes documents, speeches, resolutions at length):
  render with the builder's block-quote marker (to be added in Batch 1 —
  proposed line prefix `{q} `, styled as an indented block). Until then do not
  fake them as body paragraphs.
- Scene/section shifts inside a chapter (Isaacs uses white-space breaks, no
  titles): render as `***` where the source clearly breaks.
- **Printed-page anchors for the linked index:** every batch writes
  `data/pagemap/<unit>.json` (printed folio -> the body-paragraph index where
  that page begins), so the builder emits `epub:type="pagebreak"` anchors. The
  final batch parses the printed index and renders a back-matter **Index** page
  whose folio references link to those anchors (commissioner wants the index
  kept and navigable). Generate the pagemap during extraction, when the
  PDF-page-to-paragraph boundaries are still in hand.
- `check_register.py` / `check_reconcile.py` still apply to the **editorial**
  prose for consistency (name forms, spelling locale, date format), not to
  Isaacs's text.

## Consistency canon (bind body + notes + glossary)

- Reading text: **Isaacs's own British 1938 spelling and Wade-Giles**, verbatim.
- Editorial apparatus: **American English**, dates **Month D, YYYY**, pinyin for
  modern name forms.
- Footnote marks sit after closing punctuation. The two streams are told apart
  by NUMERAL SYSTEM, not a prefix: author notes arabic (1, 2, 3), editorial
  notes roman (i, ii, iii); both restart each chapter and are builder-assigned.
- Author notes = ALL of Isaacs's own notes: his numbered back-of-book endnotes
  AND his occasional asterisked page-foot footnotes, folded into one arabic
  stream and numbered by position. This means the arabic numbers are the
  edition's own sequence, not Isaacs's printed endnote numbers (his asterisks
  were unnumbered, and ch01's back matter even carries an orphan note 31 with
  no in-text mark, recorded as an editorial note). Do not promise the reader
  the numbers match the 1938 back matter.

_(Voice-gate rulings from the Batch 1 critique loop accumulate below, in the
RULE / WHY / FIX / CHECK form.)_

### Batch 1 voice-gate rulings (blind-critique loop) #book

**RULE: No "Pinyin: X" trailer.** Give the modern (pinyin) form once, inside
the identification, not as an appended tag.
- WHY: the notes led with the pinyin form ("Zeng Guofan (1811&#8211;1872)&#8230;")
  and then repeated it ("Pinyin: Zeng Guofan"). The glossary already carries the
  pinyin too, so the trailer was triply redundant; where WG and pinyin coincide
  (Wang Mang) it said nothing.
- FIX: open the note with the modern form and dates; drop every "Pinyin:"
  trailer. If a WG&#8594;pinyin bridge is worth spelling out, do it once inline
  ("the Kuang-hs&#252;, or Guangxu, Emperor").
- CHECK: `grep -c "Pinyin:" ` the editorial notes returns 0.

**RULE: The fact-check verdict tag is for checkable claims only.** Put
(corroborated / uncorroborated / contradicted) only on a real, checkable or
contested assertion &#8212; a date, a figure, one of Isaacs's specific claims.
- WHY: a bare "(corroborated)" on "Cathay is an old European name for China"
  reads as mechanical filler, and applying it to some plain glosses but not
  others (the zemstvos analogy) looked arbitrary.
- FIX: no verdict tag on a definitional gloss, an etymology, or an analogy;
  keep it where a claim is actually being checked.
- CHECK: every "(corroborated)" sits on a sentence a reader could in principle
  verify.

**RULE: One subject, one note.** An event and its protagonist may each get a
note, but they must not duplicate the same dates/fate/epithets.
- WHY: the Taiping note, the Hung note, and a third "Tien Wang" note each
  repeated Hong's dates, "brother of Jesus," "Heavenly King," and his 1864
  death.
- FIX: event note = the event (span, scale, God-worshippers, capital); person
  note = the person (the idiosyncratic spelling, his role); fold one-line
  restatements (Tien Wang) into the person note.
- CHECK: no two editorial notes in a unit state the same birth/death or title.

**RULE: Don't gloss ordinary English.** Note period, foreign, or technical
terms; never define a word an educated general reader knows ("pauperized").
- FIX: keep the framing content, cut the dictionary definition.

**RULE: Apparatus housekeeping is not a reader footnote.** Source
note-numbering quirks, orphan back-notes, and the like go in PROGRESS /
COMPLETION, not a popup hung on an unrelated body phrase.
- WHY: the ch01 orphan-endnote-31 note was anchored to "increases in transport
  and shipping," which has nothing to do with it (a misleading anchor), and the
  duplicated citation it preserved is already in the edition.
- FIX: log the discrepancy in PROGRESS's source-discrepancy list; no reader
  note.

**RULE: Map the old romanizations for the reader.** A general reader cannot map
Isaacs's pre-1949 spellings (Canton, Kwangsi, Tientsin, Hupeh, Annam) to modern
China. Gloss the load-bearing places at first appearance, and orient the reader
once that the book keeps period spellings with modern forms in the glossary.
- CHECK: every place that carries narrative weight has a first-appearance note
  or a glossary row; the trivial one-off locations are named as a deliberate
  skip tier in PROGRESS.

### Batch 2 voice-gate rulings (front-matter blind-critique loop) #book

**RULE: The note marker lands ON the term it defines.** Anchor a definitional
note at (the end of) the exact phrase being glossed, not on a filler word short
of it.
- WHY: the April-Theses note was anchored to "up to his famous" and the *actuel*
  gloss to "acquires thereby the most," so both markers sat one word before the
  term the note explains and read like misplaced flags.
- FIX: when the term is italicized (rendered `*...*` in the reading), the anchor
  may include the asterisks (`*actuel*`, `*Theses of April 4*, *1917*`); the
  builder matches anchors before markup substitution, so this is safe.
- CHECK: read each note's anchor phrase; the glossed word is its last content
  word.

**RULE: A content note explains the text, not the edition.** Keep editorial
method (what the notes "flag," how the apparatus works) out of the note bodies;
that belongs in the edition note, PROGRESS, or COMPLETION.
- WHY: the interested-witness note ended "the notes below flag his theory where
  it shapes a claim, without arguing the politics" &#8212; a policy statement the
  reader does not need mid-note.
- FIX: state the fact (this introduction is itself partisan) and stop.

**RULE: Don't restate the body.** A note must add what the prose does not
already say; do not paraphrase the sentence it hangs on.
- WHY: the historical-materialism note's second sentence ("Trotsky opens by
  insisting that the label alone guarantees nothing") merely re-said the
  paragraph; the John Adams note closed by restating "central to his character."
- FIX: cut the restatement; give an outside fact (dates, fate, origin, framework)
  or nothing.

**RULE: No printed-folio parentheticals in note prose.** Roman page ranges like
"(vii&#8211;x)" are meaningless in a reflowable EPUB and were used in only two
notes.
- WHY: front-matter kickoffs say cite ROMAN not arabic folios &#8212; but that
  governs WHICH system when a citation is genuinely needed, not a license to drop
  bare page ranges into identifications. The linked index (final batch) is the
  mechanism that makes folios navigable.
- FIX: drop the parenthetical; if a cross-reference is wanted, name the unit
  ("the introduction that follows"), not a page range.

**RULE: One note per subject, book-wide, at the earliest reading appearance.**
The front matter READS before ch01, so shared cast (Kuomintang, Sun Yat-sen,
Chiang, the Comintern, the Bolsheviks) first appears here, not in ch01. A blind
per-unit critic will flag these as "undefined" because it cannot see the other
units; that is a cross-unit false positive when the term is already noted in an
EARLIER-READING unit (ch00a) or on the Principal Characters page.
- FIX: note at the first reading appearance; do not re-note a thing already
  covered by an earlier-reading unit &#8212; add a within-unit note only where the
  term is genuinely first met in THIS unit (the ch00b Kuomintang note).
- CHECK: before adding a note, grep notes.json AND remember reading order is
  ch00a &#8594; ch00b &#8594; ch01 &#8594; ...; log residual cross-unit overlaps in
  PROGRESS for the final reconciliation sweep.
