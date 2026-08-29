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

## Two note layers, one stream

- **Author's notes** = Isaacs's own numbered endnotes, moved to the point they
  document. Body is his endnote text, verbatim. **Unmarked.**
- **Editorial notes** = the new reader-facing layer. Each **opens with `Ed. `**
  (rendered from the note body — put a leading `<i>Ed.</i>&#160;` in the note
  text) so the reader always knows which voice is speaking.
- Both share the builder's single continuous numbering (auto-assigned). The
  notes page and popups distinguish them by the `Ed.` mark.

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
- `check_register.py` / `check_reconcile.py` still apply to the **editorial**
  prose for consistency (name forms, spelling locale, date format), not to
  Isaacs's text.

## Consistency canon (bind body + notes + glossary)

- Reading text: **Isaacs's own British 1938 spelling and Wade-Giles**, verbatim.
- Editorial apparatus: **American English**, dates **Month D, YYYY**, pinyin for
  modern name forms.
- Footnote marks sit after closing punctuation; editorial notes carry the
  `Ed.` prefix; numbering is continuous, builder-assigned.

_(Voice-gate rulings from the Batch 1 critique loop accumulate below, in the
RULE / WHY / FIX / CHECK form.)_
