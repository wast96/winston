# STYLE.md — the prose contract for this translation

This is the falsifiable standard the reading text of *Owl's Castle* must meet.
It is adapted from the collection's stealthy-ones style contract (itself written
from a close comparison of a rejected draft against the commissioner's rewrite),
tuned to Shiba Ryōtarō's voice. The lesson of that comparison is structural, not
lexical: the diction is usually fine; the sentence architecture, rhythm, and
paragraphing are where translationese lives. Fixing the voice is therefore
mostly cutting, breaking, reordering, and compressing, and only occasionally
choosing a more vivid word. Do not reach for grander vocabulary. Reach for
cleaner structure.

Shiba is a specific target. His narrative is swift and cinematic; his dialogue
is sharp and character-marked, often in period or regional register; and he
breaks the frame constantly to address the reader directly with historical
digression and dry, opinionated aside (the essayistic habit later called
*Shiba shikan*). All three registers must survive into English as themselves.

## The core principle

Write English that reads as if it were composed in English by a first-rate
novelist, not decoded from Japanese. Fidelity is to the meaning and to the
image, never to the syntax or the information order of the source. The failure
mode to hunt down is audible machinery: prose in which a reader can hear the
Japanese grammar and the translator's own glosses showing through. Good
translation hides the machinery completely.

The test (from CLAUDE.md, sharpened): could a first-rate contemporary translator
of serious literary fiction have written this sentence, unprompted, as original
English? If it sounds like a careful, faithful decoding, it fails. If it sounds
like a novel, it passes.

## What "stilted" means here — the failure modes to eliminate

1. **The dashed-in appositive gloss.** The worst offender. A relative clause or
   identifying phrase jammed between dashes to interrupt the main clause and
   deliver a fact in passing. It is the single loudest tell of translationese.
   The information is real and must be kept, but it has to be given its own
   clean clause or sentence, moving forward, not squeezed in as an aside.
       Avoid: "The ninja, who had crossed the pass at dusk, gave no sign."
       Prefer: "The ninja had crossed the pass at dusk. He gave no sign."

2. **The long periodic sentence as default.** Sentences that stack three or four
   ideas with "and," "which," and subordinate clauses until the whole thing
   sags. When every sentence is built this way, the prose has no pulse. Shiba's
   own narrative is quick; a slack English period betrays it.

3. **Flat literalism.** Rendering an idiom or a stative Japanese construction
   word for word into abstract, lifeless English. The meaning is correct and the
   life is gone.

4. **Doubled synonyms.** Japanese pairs near-synonyms freely (grief and despair,
   settled and untroubled, void and empty). Carried into English as a pair, it
   reads as padding. English wants the one strongest word.

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
- **One idea, one clause, moving forward.** Prefer a sequence of clean statements
  over one clause nested inside another. Let each fact arrive as its own act.
- **Reorder freely; end on the strongest element.** Source information order is
  never binding. Put the point first and let the specifics expand it; land the
  sentence on the concrete or vivid word, not on a trailing subordinate phrase.
  A colon is often the cleanest way to state a thing and then unpack it.
- **Prefer active, transitive verbs and real agents.** Let people and things
  act. Avoid strings of linking verbs and avoid the reflexive passive that
  Japanese invites.

### Paragraphing
- **Break at every shift of focus.** One paragraph should hold one image, one
  beat, one turn. When the camera moves (from the sky to a face, from a face to
  the eyes, from scene to reflection), start a new paragraph. NOTE: paragraph
  parity is checked against the source line count, so a deliberate split or
  merge is a declared parity exception with a written reason, not a silent one.
- **Short paragraphs are welcome**, and a single striking image or a turn of
  thought may stand as its own paragraph. White space is part of the rhythm.

### Diction and idiom
- **Idiomatic before literal, concrete before abstract.** Choose the physical
  verb and the specific noun. When a Japanese construction is stative or
  abstract, find the living English equivalent rather than tracing its shape.
- **Compress where English compresses.** If English would carry a whole clause
  in a single word or phrase, do that. Terseness is a virtue, not a loss.
- **Enrich the physical scene, but never invent events.** See the enrichment
  doctrine below.
- **Understatement over intensifiers.** See the understatement doctrine below.
- **No archaism, no purple.** No mock-antique diction, no Victorian cadence, no
  ornamental adjectives. The register is clean, controlled, contemporary
  literary English. Period flavour comes from precise nouns (the offices, arms,
  and geography of 1591), not from fake-old grammar.

### Punctuation
- **Use the full toolkit for rhythm.** The period chops and isolates for
  emphasis. The colon states then expands. The semicolon yokes two balanced,
  related clauses. Use all three deliberately.
- **The em dash is for genuine interruption or a real dramatic break only.**
  Never for a parenthetical identifying gloss. If a dash is carrying a fact that
  could be a clause, it is being misused; rewrite it as a clause. (Prose written
  TO the commissioner uses no em dashes at all; the translation may, as English
  punctuation demands.)
- **Comma pile-up is the commonest tell — read it aloud.** A serial list or a
  single parenthetical aside is fine; the enemy is one sentence dragging a train
  of commas until it reads breathless. If you would run out of air, break it.
  Fixes in order of preference: split into two sentences; delete a needless
  comma (especially before a coordinated verb sharing its subject: "he stumbled
  and fell," not "he stumbled, and fell"); recast to shed a clause. After a
  comma-heavy run, drop the optional comma in the next sentence to let the
  passage breathe.
- **Give a real punch-line its own line** when it should land ("Then the water
  turned red."). A one-line paragraph is a legitimate instrument; note that
  splitting a source line this way is a declared parity exception with a reason,
  not a silent one.

## What stays sacred (fidelity is absolute here)
- Every fact, name, place, date, number, unit, and quantity, exactly as in the
  source. Reordering and compression change the sentence, never the content.
- The source's own errors and inconsistencies stay visible (rendered as printed,
  flagged in a note where it matters), never silently harmonized.
- Footnote anchors are verbatim substrings of the reading text; when a sentence
  is re-voiced, its anchor must be updated to a phrase that survives.
- One rendering per name, decided in `glossary.json` (checked against
  `authority.json`) before anything is romanized. Japanese names in Hepburn with
  macrons; conventional English forms (Hideyoshi, Kyoto, Tokugawa) as they are
  established.
- **Keep the source's own units and proper nouns; do not domesticate them.**
  Japanese measures (<i>ri</i>, <i>chō</i>, <i>ken</i>, <i>shaku</i>, <i>sun</i>,
  <i>koku</i>, <i>kan</i>, <i>mon</i>) stay as they are, never converted to miles
  or inches; a footnote carries the equivalence at first use. The same for
  offices, arms, and place-names.

### Names and pronouns
Native prose leans on pronouns and re-anchors the name when a beat turns;
repeating a full name every line reads mechanical (and is partly an artifact of
chasing the name-survival check). Name a character on a new beat, or when they
are the object of the sentence; use a pronoun within a run; re-anchor the full
name once when a paragraph would otherwise be ambiguous. The entity check
(`qc_entities.py`) wants the rendered name once per paragraph the character
appears in — satisfy it there and let pronouns carry the rest. In action scenes
with two men of the same side, err toward naming to kill pronoun fog.

## Application across the book's modes
- **Narrative and description:** the rules above, in full. Keep Shiba's speed.
- **Exposition (the historical and technical digressions):** the highest-risk
  zone for stiltedness, because the density invites long sentences and
  dash-glosses. Apply the rules hardest here. Break the information into short,
  confident statements. A run of exposition should read like a good writer
  telling you something, not like a decoded reference entry. Distinguish what is
  Shiba's own narration (translate it) from what the reader needs supplied
  (footnote it) — do not fold a translator's gloss into his sentence.
- **Dialogue:** natural and contracted, and differentiated by character (see the
  voice sheets in HANDOFF). Registers that are formal by design (a priest's
  invocation, a lord's command, an old villager's dialect, quoted documents)
  keep their formality, but even they must sound like real speech or real formal
  writing, never wooden. Rough men, spies, and peasants do not talk like
  courtiers. Contractions are measured, not stuffed: use them for a living
  voice, but do not pile the same one up, and keep the occasional grave,
  uncontracted line where the weight wants it. A small idiomatic touch that fits
  a speaker is welcome even when it is not literally in the source — that is
  flavour, not licence to invent plot or fact.
- **The author's direct intrusions (fourth-wall asides):** keep their
  buttonholing, conversational, faintly ironic energy. These are Shiba talking
  straight to the reader across four centuries; that is the target register at
  its most relaxed, and flattening it into neutral exposition loses the book's
  signature.

## Enrichment doctrine — where rendering ends and inventing begins

Enriching the RENDERING of what the source already holds is craft. Adding to the
CONTENT is fabrication, and fabrication is the worst error in this work because
nothing downstream catches it.

Legitimate enrichment (make the implicit explicit; choose the exact word):
- ambient conditions the scene has already fixed (name the failing light once
  dusk is established);
- physical properties inherent in a thing already named;
- the physical completion of a stated action in its stated setting;
- the sensory quality the source has already asserted.
Test: would a reader of the source already picture this, unprompted, from what
the source built? If yes, enrich. If not, stop.

Invention (forbidden, absolutely):
- new events or actions;
- new facts about place, person, motive, history;
- INVENTED PRECISION — the deadly one, dressed as enrichment: where the source is
  vague, English stays vague. "A good while" (多時) never becomes "three weeks";
  "a man" never becomes "a tall man." Definiteness the source withholds is
  withheld.
- emotional or interpretive overlay the source keeps closed.
Second test: could a careful bilingual reader point at the source and say "that
is not there and is not entailed"? If yes, cut it.

Asymmetry: enrichment touches only atmosphere and word-choice. It NEVER touches a
number, name, date, unit, or factual specific; those are copied exactly, never
grounded, rounded, or sharpened.

The dial: a light touch, not a repaint. One exact noun and one grounding phrase
usually suffice to lift a line from decoded to composed. Piling on detail becomes
its own infidelity by overriding the source's economy.

## Understatement doctrine — trust the fact, without draining the author

Default: trust the fact to carry its charge; the reflexive intensifier weakens.
Put intensity in the verb and the noun, not in an adverb. This disciplines the
NARRATOR'S DESCRIPTIVE register: strip "very," "utterly," "hideously,"
"terribly" from straight description, physical violence, and grief, where the
plain statement hits harder (Shiba's ninja violence is most chilling stated flat).

But understatement has a direction. It never lowers the temperature of a source
that already runs hot. Keep the heat where the source has it:
- the author's own raised voice (dry, sardonic, sometimes genuinely pointed in
  his historical asides): keep its edge;
- rhetorical set-pieces (curse, oath, prayer, proclamation, confession): full force;
- comedy and the bawdy register: full flavour, never made genteel;
- a character's heightened moment: a speaker who rages, rages.

Governing test: is the heat in the source, or am I adding it, or removing it?
Match the source's temperature. Plain where it is plain, hot where it is hot.
Avoid both failure modes: purple adverb-pushed English, and a bloodless uniform
cool that drains the author's passion, humour, and irony.

## Apparatus, in the same spirit (two heuristics; full policy in CLAUDE.md)
- **Footnote the invisible logic.** When a character acts on a belief the
  original audience shared silently (an omen, a point of etiquette, why an
  office or a crest carries the weight it does), the English reader needs the
  note or the scene reads as a non-sequitur. If you can explain *why* something
  made sense to Shiba's reader for free, that is a note.
- **Do not footnote the invented.** The fiction's own furniture (a made-up
  technique, a codename, a fictional place) gets a glossary line at most.
  Footnotes are for the real world behind the fiction — history, offices,
  customs, money, geography — not for the story's own props.

## The one-line summary
Cut the scaffolding. Break the walls. Trust the short sentence. Hide the machine.
