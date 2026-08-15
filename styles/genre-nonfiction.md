<!-- VOICE_TARGET: a first-rate writer of popular narrative history writing for a general reader -->
# STYLE delta — nonfiction (genre-nonfiction)

Genre layer for a work of narrative nonfiction (history, biography, reportage).
Composes onto `_base.md` plus a language layer. It switches the enrichment
license OFF, adds the interested-witness discipline and the reader-ease
furniture that a fact-dense book lives or dies by, and handles the partisan or
oral author-voice that these sources often carry. The voice-target directive on
this file's first line is woven into the base contract by the composer.

(Obeys CLAUDE.md rule 6: no em dashes in this sheet's prose except inside
quoted examples.)

NOTE (future split): the "author's voice" section below is calibrated to
POPULAR, partisan reportage (报告文学 and the like). When an academic or
neutral-register nonfiction book arrives, split this file into
`genre-nonfiction-reportage` and `genre-nonfiction-academic` rather than
straining one sheet across both. Until then, treat the voice section as
applying where the author is audibly present, and skip it where he is not.

## The voice
The target is a book you would read for pleasure, not a decoding: if a sentence
sounds like a faithful rendering, it fails; if it sounds like a first-rate
popular history someone wrote, it passes. This is history, so nothing
atmospheric may be added (see enrichment, below), and the book is a primary
source whose slant is itself part of what the reader must see (see the
interested-witness discipline).

## Enrichment is OFF; only exactness remains
In fiction, enriching the rendering of atmosphere the source already fixed is
craft. In nonfiction it is NOT permitted. You do not add sensory detail,
weather, mood, or connective drama the source does not state. There is no scene
to "complete"; there is only what the record says. An invented "fact" in a
footnoted documentary edition is a real falsehood, not just a bad sentence.

What remains legitimate is exactness, not decoration: choosing the precise
English verb for the action the source states; completing an English idiom the
sense requires; making explicit a physical relation the source's grammar
already entails. Test: would a reader of the source already picture this,
unprompted, from what the source built? If it needs the benefit of the doubt,
it is invention; stop. (The base's hard floor on invented precision binds
hardest here: where the source is vague, English stays vague.)

## The author's voice: keep the effect, not the texture
Popular and partisan nonfiction narrates in a specific voice, and it is the
point: the author buttonholes the reader, editorializes, admires his subjects,
and tells an astonishing story he has spent years collecting. But that voice is
built from devices of Chinese popular reportage (an oral, exclamatory
register, rhetorical questions, "aha" reveals, sentence-final particles doing
the emotional lifting). Carried into English feature for feature, the same
devices read as a carnival barker in a foreign-affairs essay: the reader feels
talked AT, and distrusts the shouting. The governing rule: **be loyal to the
source's EFFECT, not to its texture.** The author's own reader feels gripped
and chatted-with; your English reader should feel the same, and English
produces that feeling with different means. Keep the STANCE and the HEAT (the
admiration, the sardonic edge, the genuine indignation) and the WARMTH toward
the reader; carry them in the verbs, the nouns, and the rhythm, not in English
punctuation and rhetoric that English does not spend this way. The common way
to ruin the book is to iron the author flat; the other, which happens first, is
to leave his oral texture at full volume and let it read as goofy. Aim between:
lively, not loud.

His devices, and what to do with each:
- **Exclamation points: ration them hard.** English expository prose spends
  them as if rationed. Default: render an exclaimed statement with a flat period
  and let the fact land the punch. Keep the exclamation only inside quoted
  speech and slogans, and for the rare genuine authorial outburst (at most one
  every few pages).
- **Rhetorical (self-answering) questions: convert most to declaratives.** At
  full English strength they read as a docent who keeps turning to face the
  group. Keep one or two per chapter where the question genuinely lands; make
  the rest statements ("China's own services are the least known of all," not
  "And China's services?").
- **The "so it turns out / it seems" reveal.** Staged discovery turns folksy and
  faintly patronizing in English. Drop the wrapper; state the fact. It is
  striking on its own, and your authority survives intact.
- **The anaphora chain** (four "who could have known ..." in a row). Worth a
  trace as a deliberate flourish; at full strength it reads like ad copy. Thin
  it to two, and vary them.
- **The inclusive "we."** Keep it where he includes himself and the reader; it
  is his relationship to the audience. But re-voice plainer and colder any line
  where the warmth curdles into preciousness.

## Reader-ease conventions (what keeps a fact-dense book readable)
A book that runs on institutions, campaigns, and dozens of recurring people is
carried less by any single sentence than by whether the furniture stays put.
- **One handle per organization, forever.** Every organ gets its full formal
  rendering at first appearance and ONE fixed short handle thereafter (the
  Special Branch, the Social Affairs Department, Juntong, Zhongtong). Never
  alternate between a translation and a transliteration for the same organ, and
  never re-expand the full title once the handle is set except at a chapter
  re-introduction where the reader genuinely needs the reminder. Handles are
  DECIDED in `glossary.json`, checked against `authority.json`. Alphabet soup
  and pinyin soup are both failure states.
- **Use vs. mention.** When the author discusses a word AS a word (anatomizing a
  term, playing two terms against each other), the source term stays visible:
  italic romanization with a gloss at first mention ("<i>tewu</i>, 'special
  agent'"), then argue about it in English. When he merely USES the word, use
  the decided English rendering. A pun that cannot survive gets a footnote, not
  a strained English pun.
- **Famous quotations use the canonical English where one exists.** "Political
  power grows out of the barrel of a gun," not a fresh coinage; Sun Tzu's "to
  subdue the enemy without fighting." A reader who half-knows these must be able
  to recognize them. If the book's version differs from the received text,
  render what the book prints and footnote the difference.
- **Scare quotes: keep his, add none.** The author's quotation marks around a
  loaded term carry irony, distance, or verbatim officialese; they are content.
  Keep them where he has them. Budget for translator-added scare quotes: zero.
- **Party-jargon abstraction stack.** Political and campaign vocabulary rendered
  as stacked abstractions ("the expansion-ization of the elimination of
  counter-revolutionaries") is unreadable. Render the MEANING in plain English
  ("the purge swept up the innocent") and put the term itself in a gloss or note
  at first appearance. Slogans quoted AS slogans keep their shape; narration
  ABOUT the campaigns reads as plain English.

## The institutional first person is a deliberate choice
Where the author writes from inside his side (我党 "our Party," 我军 "our army,"
我们 "we," 敌我 "the enemy and ourselves"), keep it, and keep it consistent: it
drops the reader inside the source's voice, which is right for a partisan
source. Do not let it leak into passages the author writes from the outside.

## Interested-witness discipline: the partisanship is content, not error
A book written from within its subject celebrates its own side, adopts its
vocabulary, treats its own side's violence more gently than the enemy's, and is
most partisan on the contested episodes. Two obligations, pulling the same way:
1. **Render the slant faithfully.** Do not launder the framing into neutral
   English, and do not sharpen it either. His heroes are heroes in his telling,
   his 叛徒 are traitors, his 汉奸 are collaborators; keep his words as his.
   Neutralizing a partisan source is its own infidelity: it hides from the
   reader what kind of book this is.
2. **Put the verdict in the note, never the text.** Where a factual claim can be
   checked against independent scholarship, the FOOTNOTE carries the verdict
   (corroborated / partly / uncorroborated / contradicted), with real sources
   (never LLM-sourced; CLAUDE.md rule 5). The translated sentence stays as the
   author wrote it. Trace claims to their earliest source; say when sources
   conflict. Loaded terms get a first-appearance note, once, explaining the
   charge, then the rendering stands.

## Mode application (refines the _base framework)
Beyond narrative and exposition, nonfiction usually adds:
- **Quoted documents** (telegrams, letters, forged notices, classical
  citations): render in their own register as real documents or real formal
  writing, never wooden, never modernized into chat. These are often the crux
  of the history and of the fact-checking; set them faithfully and let the note
  do the analysis.
- **Reported speech and interview quotes:** natural and contracted,
  differentiated by speaker (a gangster, a general, a Party leader do not talk
  alike; keep the voice sheets in HANDOFF current). But many "quotes" are
  quasi-official utterances or slogans; keep those at their real weight and do
  not casualize them into banter.

## Register-drift caveat for reportage
Measure every unit against the FROZEN reference chapter, never a running
average. The primary signal is the dialogue contraction rate; but reportage
units vary wildly in how much quoted speech they carry, so in a unit with only
a handful of dialogue sentences the contraction rate is noise. Judge those units
on the narratorial signals (sentence-length spread, question and exclamation
retention, em-dash and semicolon rates) and SAY in PROGRESS that the dialogue
metric was quiet. Do not blanket-contract: the exempt registers (quoted
documents, slogans and set-piece phrases, a speaker formal by design, the
author's own formal passages) keep their form.
