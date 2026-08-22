# STYLE base — the shelf-wide prose contract

This is the shared, language- and genre-neutral core of the collection's prose
contract: the material that was near-verbatim identical across every book's
STYLE.md. It is never used alone. At setup, `scripts/compose_style.py` builds a
book's working `STYLE.md` from three layers plus the book's own ledger:

    _base.md  +  lang-<zh|ja>.md  +  genre-<fiction|nonfiction>.md  +  STYLE.local.md

See `styles/INDEX.md` for how the layers are selected and for the rule on
promoting a book's lesson back into a layer. The composed `STYLE.md` is a BUILD
ARTIFACT: never hand-edit it. A correction for THIS book goes in
`STYLE.local.md`; a lesson that proves general goes back to the layer it
belongs to.

The genre layer supplies the voice target (the kind of writer this book should
read as, woven into the core principle below), and the language layer supplies
the source-specific tells.

(This sheet obeys CLAUDE.md rule 6 in its own prose, headings included: no em
dashes, except inside quoted before/after examples, which may need them.)

## The lesson this contract encodes

The contract was written from a close comparison of a rejected draft against
the commissioner's rewrite of the same passage. The lesson is structural, not
lexical: the diction is usually fine; the sentence architecture, rhythm, and
paragraphing are where translationese lives. Fixing the voice is therefore
mostly cutting, breaking, reordering, and compressing, and only occasionally
choosing a more vivid word. Do not reach for grander vocabulary. Reach for
cleaner structure.

## The core principle

Write English that reads as if it were composed in English by
{{VOICE_TARGET}}, not decoded from the source. Fidelity is to the meaning and
to the fact, never to the syntax or the information order of the source. The
failure mode to hunt down is audible machinery: prose in which a reader can
hear the source grammar and the translator's own glosses showing through. Good
translation hides the machinery completely.

The test (from CLAUDE.md, sharpened): could {{VOICE_TARGET}} have written this
sentence, unprompted, as original English? If it sounds like a careful,
faithful decoding, it fails. If it sounds like a book someone wrote, it passes.

## What "stilted" means: the universal failure modes to eliminate

These six are shelf-wide, source-language-independent. The language layer adds
the tells specific to this book's source language.

1. **The dashed-in (or comma'd-in) appositive gloss.** The worst offender. A
   relative clause or identifying phrase jammed between dashes or commas to
   interrupt the main clause and deliver a fact in passing. It is the single
   loudest tell of translationese. The information is real and must be kept,
   but it has to be given its own clean clause or sentence, moving forward, not
   squeezed in as an aside.
       Avoid: "The general, who had crossed the mountains at dawn, gave the order."
       Prefer: "The general had crossed the mountains at dawn. He gave the order."
2. **The long periodic sentence as default.** Sentences that stack three or
   four ideas with "and," "which," and subordinate clauses until the whole
   thing sags. When every sentence is built this way, the prose has no pulse.
3. **Flat literalism.** Rendering an idiom or a stative construction word for
   word into abstract, lifeless English. The meaning is correct and the life is
   gone.
4. **Doubled synonyms.** The source pairs near-synonyms freely (grief and
   despair, settled and untroubled). Carried into English as a pair, it reads
   as padding. English wants the one strongest word, or the real distinction if
   there is one.
5. **The dense wall paragraph.** A single paragraph carrying several distinct
   images or beats with no break, so the eye and the ear get no rest.
6. **Adjective-linking-verb strings.** Chains of "was / were + adjective" that
   describe without any thing acting.

## The rules

### Sentence architecture and rhythm
- **Vary sentence length deliberately, and use short sentences as instruments.**
  A short declarative lands a fact, resets the rhythm, and creates emphasis by
  isolation. Follow a long, flowing sentence with a short one. A sentence
  fragment is allowed where it sets a scene or strikes a note.
- **One idea, one clause, moving forward.** Prefer a sequence of clean
  statements over one clause nested inside another. Let each fact arrive as its
  own act.
- **Reorder freely; end on the strongest element.** Source information order is
  never binding. Put the point first and let the specifics expand it; land the
  sentence on the concrete or vivid word, not on a trailing subordinate phrase.
  A colon is often the cleanest way to state a thing and then unpack it.
- **Prefer active, transitive verbs and real agents.** Let people, things, and
  institutions act. Avoid strings of linking verbs and the reflexive passive
  the source invites.

### Paragraphing
- **Break at every shift of focus.** One paragraph should hold one image, one
  beat, one turn. When the focus moves (from the sky to a face, from an
  operation to its aftermath, from scene to reflection), start a new paragraph.
  NOTE: paragraph parity is checked against the source line count, so a
  deliberate split or merge is a DECLARED parity exception with a written
  reason, not a silent one.
- **Short paragraphs are welcome**, and a single striking image or a turn of
  thought may stand as its own paragraph. White space is part of the rhythm.

### Diction and idiom
- **Idiomatic before literal, concrete before abstract.** Choose the physical
  verb and the specific noun. When a source construction is stative or
  abstract, find the living English equivalent rather than tracing its shape.
- **Compress where English compresses.** If English would carry a whole clause
  in a single word or phrase, do that. Terseness is a virtue, not a loss.
- **No archaism, no purple.** No mock-antique diction, no Victorian cadence, no
  ornamental adjectives. The register is clean, controlled, contemporary
  English. Period flavour comes from precise nouns (the offices, arms, ranks,
  and geography of the period), not from fake-old grammar.
- **Never send the reader to a dictionary.** Prefer the common word to the
  exact but arcane one, unless the precision is the whole point (then keep it
  and footnote).

### Punctuation
- **Use the full toolkit for rhythm.** The period chops and isolates for
  emphasis. The colon states then expands. The semicolon yokes two balanced,
  related clauses. Use all three deliberately.
- **The em dash is for genuine interruption or a real dramatic break only.**
  Never for a parenthetical identifying gloss. If a dash is carrying a fact that
  could be a clause, it is being misused; rewrite it as a clause. (The per-
  sentence em-dash BUDGET is set by the language layer, which knows how the
  source punctuation accretes dashes.) Prose written TO the commissioner uses no
  em dashes at all; the translation may, as English punctuation demands.
- **Comma pile-up is the commonest tell; read it aloud.** A serial list or a
  single parenthetical aside is fine; the enemy is one sentence dragging a
  train of commas until it reads breathless. Fixes, in order of preference:
  split into two sentences; delete a needless comma (especially before a
  coordinated verb sharing its subject: "he stumbled and fell," not "he
  stumbled, and fell"); recast to shed a clause.
- **Give a real punch-line its own line** when it should land ("Then the water
  turned red."). A one-line paragraph is a legitimate instrument; splitting a
  source line this way is a declared parity exception with a reason.

## Numbers, dates, and units (shelf-wide house style)
- **Values are exact and sacred; only the FORMAT is Englished.** Reproduce
  every figure the source gives; never round, sharpen, or convert a value. But
  render dates and numerals in English convention, not source convention: "On
  March 21," not the source's "3/21"; a count-unit resolves to its full value
  ("300,000," never a transliterated "30 wan").
- **Spell out whole numbers below 100** and rhetorical or idiomatic rounds ("a
  hundred battles," "nearly a hundred years"); **use figures for 100 and up**,
  for anything needing a comma, and for statistics run together ("more than 300
  killed, more than 500 arrested, more than 5,000 missing"). Do not mix the two
  in one breath ("five thousand ... 2,100").
- **Vagueness the source keeps stays vague** (see the hard floor on invention):
  "a good while" is not "three weeks"; "over a hundred" is not "a hundred and
  twenty."
- **Keep period money and measures** with a first-use gloss where a modern
  reader would miss the sense; the language layer lists this source's units.

## Names and pronouns

Native prose leans on pronouns and re-anchors the name when a beat turns;
repeating a full name every line reads mechanical (and is partly an artifact of
chasing the name-survival check). Name a character on a new beat, or when they
are the object of the sentence; use a pronoun within a run; re-anchor the full
name once when a paragraph would otherwise be ambiguous. In action scenes with
two figures of the same side, err toward naming to kill pronoun fog. The
opposite error is the loud "this is translated" tell: the source restates a
full name where English pronominalizes, giving you "X opened it ... X could have
... but X sealed it up," three names deep where English wants "he" twice. When
one person owns a run of sentences, name once and let pronouns carry the rest.
The entity check (`qc_entities.py`) wants the rendered name once per paragraph
the character appears in: satisfy it there and let pronouns carry the rest.

One rendering per referent, DECIDED in `glossary.json` and checked against
`authority.json` before anything is romanized. (Romanization system and
conventional-form exceptions are set by the language layer.)

## What stays sacred (fidelity is absolute here)
- Every fact, name, place, date, number, unit, and quantity, exactly as in the
  source. Reordering and compression change the sentence, never the content.
  Numerals in unit and case designations are load-bearing; crop-verify them.
- The source's own errors and inconsistencies stay visible: rendered as
  printed, flagged in a note where it matters, never silently harmonized. A
  name spelled two ways, a date that disagrees with another chapter, a figure
  that does not add up: translate as printed, note the fact. Silently fixing it
  destroys evidence about how the book was made.
- Footnote anchors are verbatim substrings of the reading text; when a sentence
  is re-voiced, its anchor must be updated to a phrase that survives.

## The hard floor on invention (both genres, no exceptions)

Enriching the RENDERING of what the source already holds may or may not be
permitted (the genre layer decides). Adding to the CONTENT never is.
Fabrication is the worst error in this work because nothing downstream catches
it.

Forbidden absolutely, in every book:
- new events or actions;
- new facts about place, person, motive, date, number, history;
- **INVENTED PRECISION**, the deadly one, dressed as enrichment: where the
  source is vague, English stays vague. "A good while" never becomes "three
  weeks"; "a man" never becomes "a tall man"; "some people" never becomes "a
  dozen men"; "it is said" stays hedged and is never upgraded to plain
  assertion. Definiteness the source withholds is withheld. This class greps
  better than it samples; watch for it.
- emotional or interpretive overlay the source keeps closed.

Governing test: could a careful bilingual reader point at the source and say
"that is not there and is not entailed"? If yes, cut it. The asymmetry is
total: whatever latitude the genre layer grants touches only atmosphere and
word-choice, and NEVER a number, name, date, unit, or factual specific.

## Understatement doctrine — trust the fact, without draining the author

Default: trust the fact to carry its charge; the reflexive intensifier weakens.
Put intensity in the verb and the noun, not in an adverb. This disciplines the
NARRATOR'S DESCRIPTIVE register: strip "very," "utterly," "hideously,"
"terribly" from straight description, physical violence, and grief, where the
plain statement hits harder.

But understatement has a direction. It never lowers the temperature of a source
that already runs hot. Keep the heat where the source has it:
- the author's own raised voice (dry, sardonic, sometimes genuinely pointed in
  the asides): keep its edge;
- rhetorical set-pieces (curse, oath, prayer, proclamation, confession): full
  force;
- comedy and the bawdy register: full flavour, never made genteel;
- a character's heightened moment: a speaker who rages, rages.

Governing test: is the heat in the source, or am I adding it, or removing it?
Match the source's temperature. Plain where it is plain, hot where it is hot.
Avoid both failure modes: purple adverb-pushed English, and a bloodless uniform
cool that drains the author's passion, humour, and irony.

## Application across the book's modes (framework)

Every book runs in several registers, and each keeps its own voice. The genre
layer names this book's specific modes; the constants are:
- **Narrative and description:** the rules above, in full. Keep the source's
  pace; a slack English period betrays a quick original.
- **Exposition (historical, technical, institutional digression):** the
  highest-risk zone for stiltedness, because the density invites long sentences
  and dash-glosses. Apply the rules hardest here. Break the information into
  short, confident statements. A run of exposition should read like a good
  writer telling you something, not like a decoded reference entry. Distinguish
  what is the author's own narration (translate it) from what the reader needs
  supplied (footnote it); never fold a translator's gloss into the author's
  sentence.
- **Dialogue and quoted speech:** natural and contracted, differentiated by
  character (keep the VOICE SHEETS in HANDOFF current and consult them at every
  dialogue scene). Registers formal by design (a prayer, a command, a dialect,
  a quoted document) keep their formality, but even they must sound like real
  speech or real formal writing, never wooden.
- **The author's own voice / direct intrusions:** keep its energy and edge.
  Flattening it into neutral exposition loses the book's signature.

## Apparatus, in the same spirit (two heuristics; full policy in CLAUDE.md)
- **Footnote the invisible logic.** When a character acts on a belief the
  original audience shared silently (an omen, a point of etiquette, why an
  office or a crest carries the weight it does), the English reader needs the
  note or the scene reads as a non-sequitur. If you can explain WHY something
  made sense to the original reader for free, that is a note.
- **Footnote the real world, not the book's own furniture.** History, offices,
  customs, money, geography, and (in nonfiction) the fact-check verdict earn
  notes. The book's own coinages, codenames, and invented props get a glossary
  line at most.

## The one-line summary
Cut the scaffolding. Break the walls. Trust the short sentence. Hide the machine.
