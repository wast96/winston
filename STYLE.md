# STYLE.md — the prose contract for this translation

This is the falsifiable standard the reading text of *Zhou Enlai: Commander of
the Hidden Front* must meet. It is adapted from the collection's prose contract
(written from a close comparison of a rejected literary-translation draft against
the commissioner's rewrite), retuned from Japanese fiction to **Chinese partisan
nonfiction**. The structural lesson of that comparison holds across the shift:
the diction is usually fine; the sentence architecture, rhythm, and paragraphing
are where translationese lives. Fixing the voice is mostly cutting, breaking,
reordering, and compressing, and only occasionally choosing a more vivid word.
Do not reach for grander vocabulary. Reach for cleaner structure.

But this is a work of **history**, not a novel, and that changes two things
absolutely: nothing atmospheric may be added to the source (the fiction
"enrichment" licence is off; see below), and the book is a **partisan primary
source** whose slant is itself part of what the reader must see. Render its voice
and its claims faithfully; the apparatus, not the prose, carries the verdict.

Read this at the start of every batch, alongside CLAUDE.md and HANDOFF.md.
(This sheet obeys CLAUDE.md rule 6 in its own prose: no em dashes here, except
inside quoted examples, which necessarily show them.)

## The core principle

Write English that reads as if it were composed in English by a first-rate
writer of narrative history, not decoded from Chinese. Fidelity is to the meaning
and to the fact, never to the syntax or the information order of the source. The
failure mode to hunt down is audible machinery: prose in which a reader can hear
the Chinese grammar and the translator's own glosses showing through. Good
translation hides the machinery completely.

The test (from CLAUDE.md, sharpened): could a first-rate contemporary writer of
popular history (think of a good English-language account of an intelligence war)
have written this sentence, unprompted, as original English? If it sounds like a
careful, faithful decoding, it fails. If it sounds like a book someone wrote, it
passes.

## What "stilted" means here: the failure modes to eliminate

The general tells, then the Chinese-specific ones.

1. **The dashed-in (or comma'd-in) appositive gloss.** The worst offender. An
   identifying phrase jammed between dashes or commas to interrupt the main
   clause and deliver a fact in passing. It is the loudest tell of
   translationese, and Chinese apposition (`这位…`, `即…`, `原名…`) invites it.
   The information is real and must be kept, but give it its own clean clause or
   sentence, moving forward.
       Avoid: "Chen Geng, who under the alias Wang Yong then ran the intelligence
       section, boarded the train."
       Prefer: "Chen Geng ran the intelligence section under the alias Wang Yong.
       He boarded the train."

2. **The long periodic sentence as default.** Chinese runs on with `而且`,
   `并且`, `从而`, `由于…因此`, stacking three or four ideas until the sentence
   sags. When every sentence is built this way the prose has no pulse. Break it.

3. **Flat literalism.** Rendering an idiom or a stative construction word for
   word into abstract, lifeless English. The meaning is correct and the life is
   gone.

4. **Doubled synonyms / 并列 pairs.** Chinese pairs near-synonyms freely
   (`巩固和发展`, `勇气和毅力`, `搜捕和屠杀`). Carried into English as a pair it
   reads as padding. Take the one strongest word, or draw the real distinction if
   there is one.

5. **The dense wall paragraph.** A single paragraph carrying several distinct
   beats with no break. Break at the shift.

6. **Adjective-linking-verb strings.** Chains of "was / were + adjective" that
   describe without anything acting.

7. **The 的-string / stacked pre-noun modifier.** Chinese piles modifiers before
   the noun with `的`; traced literally it becomes a long adjective train or an
   "of … of …" chain. Unpack it: move the modifiers into clauses or after the
   noun.

8. **Topic-comment fronting as "As for …".** Chinese fronts the topic
   (`关于…方面`, `在…上`). Do not calque it as "As for X, …"; fold the topic into
   the subject and let the sentence move.

9. **The 被-passive and 使-causative.** `被捕` invites "was arrested by"; `使…得以`
   invites "made it so that." Prefer an active agent and a transitive verb where
   English would use one. (Keep the passive where the agent is genuinely unknown
   or beside the point.)

10. **Aspect over-marking.** `了` / `过` / `已经` traced across every clause pile
    up as "already," "had …ed," "went on to." English carries sequence with the
    plain past; use the perfect only where the time relation actually needs it.

11. **Empty connective padding.** `所以说`, `可以说`, `这样一来`, `换句话说`
    often add nothing. Cut them and let the fact stand.

## The rules

### Sentence architecture and rhythm
- **Vary sentence length deliberately; use short sentences as instruments.** A
  short declarative lands a fact, resets the rhythm, and creates emphasis by
  isolation. Follow a long sentence with a short one.
- **One idea, one clause, moving forward.** Prefer a sequence of clean statements
  over one clause nested inside another. Let each fact arrive as its own act.
- **Reorder freely; end on the strongest element.** Source information order is
  never binding. Put the point first and let the specifics expand it; land the
  sentence on the concrete or telling word, not a trailing subordinate phrase. A
  colon is often the cleanest way to state a thing and then unpack it.
- **Prefer active, transitive verbs and real agents.** Let people and
  organizations act. Avoid strings of linking verbs and the reflexive passive
  Chinese invites.

### Paragraphing
- **Break at every shift of focus** (from an operation to its aftermath, from a
  person to the office behind him, from event to the author's comment). NOTE:
  paragraph parity is checked against the source line count, so a deliberate
  split or merge is a **declared parity exception with a written reason**, not a
  silent one.
- **Short paragraphs are welcome.** A single decisive turn may stand alone. White
  space is part of the rhythm.

### Diction and idiom
- **Idiomatic before literal, concrete before abstract.** Choose the physical
  verb and the specific noun. For a stative or abstract Chinese construction,
  find the living English equivalent rather than tracing its shape.
- **Compress where English compresses.** If English carries a whole clause in a
  phrase, do that. Terseness is a virtue.
- **成语 and set images: translate for effect; footnote the ones whose picture
  matters.** Render a four-character idiom for what it does in the sentence
  (`措手不及` → "caught off guard"), keeping the vivid literal image only where it
  lands in English. When the book quotes a classical source as a source (it opens
  on `孙子兵法·谋攻篇` and `知己知彼，百战不殆`), render the quotation and footnote
  the attribution and the literal sense; do not bury it as a bare idiom.
- **The political / period lexicon: use the established English term, keep the
  register, do not inflate.** `白色恐怖` is "the White Terror"; `反动派` are "the
  reactionaries"; `叛徒` a "traitor" or "turncoat"; `租界` the "Concessions."
  These are the author's own charged words (see the partisan-source discipline
  below): render them as his usage, do not neutralize them into copy-editor's
  English, and do not intensify them either. NOTE: `巡捕房` has THREE different
  renderings across the sibling books (authority.json shows "concession police
  station," "police station," "the Municipal Police…"); decide this book's form
  in glossary.json at first use and hold it, and record the decision back into
  authority.json. The same goes for any high-frequency term the shelf disagrees
  on: the glossary decides once, this sheet does not legislate ahead of it.
- **`同志` ("comrade"): a style decision, provisional until the voice gate.**
  The honorific saturates CCP historiography (`陈赓同志`) and is part of the
  author's partisan voice, so it cannot be silently stripped everywhere; but
  "Comrade X" at every occurrence is leaden in English. Working rule: keep
  "Comrade" in direct address and dialogue, and where the author's reverence is
  doing real work (first appearances, the fallen); let the bare name carry
  routine narration; footnote the convention once at first occurrence. Calibrate
  at the ch01 voice gate and record the ruling below.
- **No archaism, no purple.** No mock-antique diction, no Victorian cadence, no
  ornamental adjectives. Period flavour comes from precise nouns (the offices,
  ranks, streets, and organs of 1927-1933 Shanghai), not from fake-old grammar.
- **Never send the reader to a dictionary** unless the precision is the whole
  point (then keep it and footnote). Prefer the common word to the arcane one.

### Names and pronouns
Pinyin, one rendering per referent, decided in `glossary.json` and checked
against `authority.json` before anything is romanized; conventional English forms
where established (Chiang Kai-shek, Sun Yat-sen, the Kuomintang). The shelf has
already agreed `广州` = Guangzhou, not Canton (authority.json, two books); follow
the ledger, not habit, whenever the two pull apart. This book's cast is large, mostly male, and
turns over fast, and many figures carry an alias (`王庸` = Chen Geng, `伍豪` =
Zhou Enlai, `曾培鸿` = Li Qiang): pronoun fog in arrest and chase scenes is a
real risk. Name a figure on a new beat and when he is the object of the sentence;
use a pronoun within a run; re-anchor the full name when a paragraph would
otherwise be ambiguous, and err toward naming when two men of the same side share
a scene. Give an alias its owner's name or a clarifying tag on first use in a
scene so the reader never loses the thread. `qc_entities.py` wants the rendered
name once per paragraph the figure appears in; satisfy it there and let pronouns
carry the rest.

### Punctuation
- **Use the full toolkit for rhythm.** The period chops and isolates; the colon
  states then expands; the semicolon yokes two balanced clauses. Use all three
  deliberately.
- **The em dash: at most TWO per sentence.** Two singles or one matched pair
  bracketing an aside are both fine; three is a pile-up and never ships. When a
  sentence would exceed the budget, swap a dash for a semicolon (a balanced
  second clause), a comma (a light aside), or a period (split it). Never use a
  dash for a parenthetical identifying gloss: if a dash is carrying a fact that
  could be a clause, rewrite it as a clause. (Prose written TO the commissioner
  uses no em dashes at all; the translation may, as English punctuation
  demands.) `check_register.py --ref` tracks the em-dash rate against the
  frozen reference chapter; a jump is a flag to go look.
- **Comma pile-up is the commonest tell; read it aloud.** A serial list or a
  single aside is fine; the enemy is one sentence dragging a train of commas
  until it reads breathless. Fixes in order: split into two sentences; delete a
  needless comma (especially before a coordinated verb sharing its subject: "he
  turned and fled," not "he turned, and fled"); recast to shed a clause.

## What stays sacred (fidelity is absolute, and more so than in fiction)
- **Every fact, name, place, date, number, unit, alias, and quantity, exactly as
  in the source.** Reordering and compression change the sentence, never the
  content. Numerals in unit and case designations are load-bearing; crop-verify
  them.
- **The source's own errors and inconsistencies stay visible**, rendered as
  printed and flagged in a note where it matters, never silently harmonized. A
  name spelled two ways, a date that disagrees with another chapter, a figure
  that does not add up: translate as printed, note the fact. Silently fixing it
  destroys evidence about how the book was made.
- **Footnote anchors are verbatim substrings of the reading text**; when a
  sentence is re-voiced, update its anchor to a phrase that survives.

## Application across the book's modes
This book runs in five registers; each keeps its own voice.
- **Narrative and dramatized episode** (the "legendary" agent stories, the
  chases, the rescues, the executions): the rules above, in full. Keep the pace.
  This is where the book means to grip, and a slack English period betrays it.
- **Exposition and political framing** (`中国共产党的情报保卫工作是…`, the
  potted history, the organizational digressions): the highest-risk zone for
  stiltedness, because density invites long sentences and dash-glosses. Apply the
  rules hardest here. Break the information into short, confident statements. It
  should read like a good writer telling you something, not like a decoded
  reference entry. Distinguish what is Mu Xin's own narration (translate it) from
  what the English reader needs supplied (footnote it); never fold a translator's
  gloss into his sentence.
- **Quoted documents** (telegrams, the forged *Wu Hao Notice*, Zhou Enlai's
  letters, the handwritten 密信, classical citations): render in their own
  register as real documents or real formal writing, never wooden, never
  modernized into chat. These are often the crux of the history and of the
  fact-checking; set them faithfully and let the note do the analysis.
- **Reported speech and dialogue** (`周恩来说：“你们把它拿过来”`): natural and
  contracted, differentiated by speaker. A gangster, a swearing official, and a
  Party leader do not talk alike. But many "quotes" here are quasi-official
  utterances or slogans; keep those at their real weight and do not casualize
  them into banter.
- **The author's own voice** (Mu Xin celebrating his heroes, denouncing the
  traitors, arguing a point): keep its energy and its edge. Flattening it into
  neutral exposition loses the book's character. Where that voice is doing
  partisan work, the note says so; the prose keeps the voice.

## The partisan-source discipline: the defining rule of THIS book
The book is a work of Chinese Communist Party history written from within that
tradition, frankly devoted to its subject and frankly hostile to its enemies.
Two obligations, and they pull the same way:

1. **Render the slant faithfully.** Do not launder the author's framing into
   neutral English, and do not sharpen it either. His heroes are heroes in his
   telling, his `叛徒` are traitors, his `匪` are bandits; keep his words as his.
   Neutralizing a partisan source is its own infidelity: it hides from the reader
   what kind of book this is.
2. **Put the verdict in the note, never in the text.** Where a factual claim can
   be checked against independent scholarship, the **footnote** carries the
   verdict (corroborated, uncorroborated, or contradicted), with real sources
   (never LLM-sourced; see CLAUDE.md rule 5). The translated sentence stays as Mu
   Xin wrote it. Never silently correct the story in the prose. The
   well-documented episodes (Gu Shunzhang's 1931 defection, the *Wu Hao Notice*
   affair, the Longtan Three) are strong corroboration targets; trace claims to
   their earliest source, and say when sources conflict.

## Enrichment is OFF; invented precision is the deadly error
In fiction, enriching the *rendering* of atmosphere the source already fixed is
craft. **In this history it is not permitted.** You do not add sensory detail,
weather, mood, or connective drama that the source does not state. There is no
scene to "complete"; there is only what the record says.

What survives from the fiction doctrine, and hardens:
- **INVENTED PRECISION is forbidden, absolutely.** Where the source is vague,
  English stays vague. `多时` never becomes "for weeks"; `一些人` never becomes
  "a dozen men"; `不久` never becomes "three days later"; `据说` ("it is said")
  stays hedged and is never upgraded to plain assertion. Definiteness the source
  withholds is withheld. This class greps better than it samples; watch for it.
- **Make implicit logic explicit in the NOTE, not in the sentence.** When a
  Chinese reader would silently supply context (why an office carried the weight
  it did, what an event or a slogan meant, who a name was), the English reader
  needs a footnote, not an inserted clause in Mu Xin's prose.
Test: could a careful bilingual reader point at the source and say "that is not
there and is not entailed"? If yes, cut it. The asymmetry is total: nothing you
add ever touches a number, name, date, unit, or factual specific.

## Understatement doctrine: match the source's temperature
Default: trust the fact to carry its charge; the reflexive intensifier weakens.
Put intensity in the verb and the noun, not in an adverb. Strip "very,"
"utterly," "brutally," "heroically" from straight description where the plain
statement hits harder (a martyr's death stated flat is stronger than one
adverb-pushed).

But understatement has a direction. It never cools a source that already runs
hot, and this book runs hot on purpose. Keep the heat where the author has it:
- **his raised political voice** (indignant at the reactionaries, reverent toward
  the fallen): vehement in the source, vehement in English;
- **rhetorical set-pieces** (a martyr's last words, an oath, a denunciation):
  full force;
- **a scene's heightened moment**: a betrayal that horrifies horrifies.
Governing test: is the heat in the source, or am I adding it, or removing it?
Match it. Plain where it is plain, hot where it is hot. Avoid both failure modes:
purple adverb-pushed English, and a bloodless uniform cool that drains the
author's conviction.

## Apparatus, in the same spirit (two heuristics; full policy in CLAUDE.md)
- **Footnote the invisible logic.** When the narrative turns on knowledge the
  original audience shared silently (what the Central Special Section's four
  branches did, why the foreign Concessions were a refuge, what `四一二` or
  `九一八` were, how a `巡捕房` differed from a Chinese police force, who a name
  was), the English reader needs the note or the passage reads as a non-sequitur.
- **Footnote the real world, and grade the claim.** Notes are for history,
  offices, people, geography, money, and custom, and for the fact-check verdict.
  A recurring subject gets its note at its **first appearance in the book**; grep
  `notes.json` and the earlier reading files first, keep the "NOT re-noted" list
  in PROGRESS, and prefer a cross-reference to a repeat.

## Calibrated rulings (seeded at the ch01 voice gate; grows through the book)
This section is a living ledger, in the correction → why → fix form: when the
commissioner corrects a line, record the CLASS of error here, not just the one
fix, so the reasoning travels with the rule. A single correction is a data point;
the rule that prevents the whole class is the deliverable. Empty until the
first-chapter voice gate (Step 0c).

- _(pending the ch01 voice gate)_

## The one-line summary
Cut the scaffolding. Break the walls. Trust the short sentence. Hide the machine.
Add nothing; the verdict goes in the note.
