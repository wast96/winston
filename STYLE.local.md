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

(Obeys CLAUDE.md rule 6: no em dashes in this file's own prose except inside
quoted before/after examples.)

## Voice sharpening (if this book has a nameable authorial voice)

Yao Huafei writes admiring Party-biography reportage: warm toward its subject,
reverent toward the martyrs, dense with dates and offices. In English aim for a
first-rate popular biographer of the intelligence world (think a plainer John
le Carre writing nonfiction): controlled, concrete, unhurried. Keep the
author's genuine admiration and indignation, but carry them in verbs and facts,
never in a stacked adverb or a heroic-formula phrase. The recurring temptation
is the Party-report register (絶対安全, 英勇就義, 坚贞不屈) at full English volume;
hold it down.

## Calibrated rulings (grows through the book)

### RULE. Ration the heroic set-phrase; a martyrdom/valor formula loses force by repetition. [#promote]
- **WHY IT HAPPENED.** Party reportage has a fixed stock of virtue-formulas that
  recur every few lines: 出色地完成 ("carried it off brilliantly"), 谈何容易
  ("no easy thing"), 绝对安全 ("absolute safety"), 英勇就义 ("went bravely to his
  death"). Rendered one-for-one, the SAME English phrase lands three to five
  times in a chapter and reads as boilerplate; the fifth martyrdom is flatter
  than the first.
- **FIX.** Vary the verb and drop the intensifier. "carried it off brilliantly"
  five times becomes "pulled it off," "brought it off cleanly," "saw it
  through," "handled it faultlessly." "went bravely to his death" becomes "met
  his death unflinching," "gave his life," "was executed." "absolute safety"
  becomes "safe" (keep ONE emphatic use per episode for the source's heat).
- **CHECK.** grep the built unit for the worst offenders before shipping:
  `grep -oE "carried it off (brilliantly|superbly)|no easy thing|absolutely? safe|went bravely to his death"`;
  more than two hits of any one phrase in a chapter is a rewrite.

### RULE. A four-character idiom (成语) is translated for EFFECT, never dropped in as a bare English calque. [#promote]
- **WHY IT HAPPENED.** The source studs narration with 成语. Traced literally
  they land as odd bare sentences a native writer would never set down: 一石激起
  千层浪 "One stone raises a thousand waves." as its own sentence; 久旱逢甘霖 as
  "read ... as a man reads rain" (which cannot parse: one does not "read rain").
- **FIX.** Fold the image into the surrounding sentence as a clause, or render
  the sense: "roused the fury of the Chinese people; one stone had raised a
  thousand waves." "pored over the articles like a man drinking rain after long
  drought." Keep the picture only where it lands in running English; otherwise
  give the meaning.
- **CHECK.** A one-clause "quoted-proverb" sentence dropped between two
  narrative sentences is the tell; read for sentences that are ONLY an idiom.

### RULE. Thin the water/storm imagery; the source runs it constantly, English tires of it fast. [#book]
- **WHY IT HAPPENED.** This book's stock metaphors for revolution are flood and
  storm (红色革命风暴, 滚滚洪流, 翻天覆地, 乘风破浪, 风起云涌). Carried every time,
  English gets "flood," "storm," "surge," "rolling flood," "wind and wave"
  within a page.
- **FIX.** Keep one strong instance per passage; vary or cut the repeats
  ("flood of the great revolution" near "rolling flood" becomes "surge of the
  great revolution").
- **CHECK.** grep a finished section for `flood|storm|surge|tide|wind and wave`;
  cluster hits mean thin them.

### RULE. Kill the editorial adjective on an inanimate object and the coined compound; they read as propaganda or as non-English. [#promote]
- **WHY IT HAPPENED.** Partisan source diction attaches a verdict-adjective to a
  thing (罪恶的子弹 "wicked bullets") and coins heroic compounds (惊天动地
  "world-overturning," 心明眼亮 "bright-eyed and clear," 高呼 rendered
  "high-hearted"). The verdict belongs to the note, not the noun; the coinage is
  not English.
- **FIX.** "The wicked bullets tore into the crowd" -> "The bullets tore into
  the crowd" (the fact is the horror). "world-overturning struggle" ->
  "world-shaking struggle." Let plain nouns and verbs carry the charge.
- **CHECK.** The understatement-doctrine read: is the heat in the source's FACT
  or in my adjective? If the adjective, cut it.

### RULE. Unstack the fronted/inverted sentence into subject-first English. [#promote]
- **WHY IT HAPPENED.** Chinese topic-fronting and existential 有 produce
  "In the depth of his confusion there was among his fellow clerks one named
  ..." and "there took root in him the creed of ...". Traced, they read as
  fake-literary inversion.
- **FIX.** Put the subject first: "One of his fellow clerks, Zhu Kongyang, was a
  man of advanced ideas." "the creed of ... took root in him."
- **CHECK.** Sentences opening "There was/were," "In the X of Y there ...," or a
  long adverbial before the subject; recast subject-first unless the inversion
  is doing real emphatic work.

### RULE. A classical tag or quoted maxim needs an English frame, not a bare drop. [#book]
- **WHY IT HAPPENED.** The author quotes a saying inline with only quotation
  marks: 忠孝怎能两全 rendered as a bare '"how can a man be loyal and filial
  both?"' mid-narrative, which reads as a non-sequitur to a reader who does not
  know it is proverbial.
- **FIX.** Frame it: "But as the old question runs, how can a man be loyal and
  filial at once?" A light lead-in ("as the saying has it," "in the old phrase")
  tells the reader this is received wisdom, not the narrator's own aside.
- **CHECK.** A quotation mark opening mid-paragraph with no "he said" / "the
  saying runs" nearby.

### RULE. Ration the "impression / influence" formula and cap figurative images at one per two sentences. [#promote]
- **WHY IT HAPPENED.** Reportage marks every meeting of note with 留下了深刻的
  印象 / 产生了深刻的影响. Rendered literally it becomes "left a deep impression
  / mark" five or six times a chapter. Separately, the source often stacks two
  metaphors in adjacent sentences (甘霖 + 暗夜光明; a lamp in the dark AND a light
  in the dark); English tires of a repeated image far faster than Chinese.
- **FIX.** Vary the impression formula: "stayed with him," "he never forgot,"
  "won X's lasting regard," "made a deep impression" (keep one literal use). Keep
  ONE metaphor where the source doubles; if an image (lamp / light in the dark)
  has already been used in the passage, cut its echo.
- **CHECK.** grep `impression|left a .* mark|marked .* deeply`; and read for two
  similes within adjacent sentences.

### RULE. No fake-literary clefts or antique light-verbs in plain narration. [#promote]
- **WHY IT HAPPENED.** Reaching for gravitas produces "It was across six years
  of a clerk's life that a great change came over him" (cleft) and "the strike
  worked a vast change in how he saw his life" (antique "work a change"). Both
  read as costume, not narration.
- **FIX.** Subject-verb-object: "Six years as a clerk changed his thinking." "The
  strike transformed how he saw his life." Save the cleft for real emphasis.
- **CHECK.** Sentences opening "It was ... that ..." and the collocation "worked
  a change/impression."

### RULE. NOTE DENSITY: gloss every proper noun a non-specialist might not know. [#book]
- **COMMISSIONER DIRECTIVE (Batch 1 gate).** "A lot more footnotes to explain
  the names and places and all that... a high density explaining everything just
  in case there's a gap in my knowledge" &#8212; but "don't add footnotes just
  to add them." So: default to FOOTNOTING, not to omitting. Every named person,
  place, institution, event, office, journal, and period term that a well-read
  Western reader without a China background might not place gets a note at its
  first appearance: who/what/when, why it matters here, and the fact-check
  verdict where a claim is checkable. This overrides the base layer's "tier of
  minor discrepancies left unfootnoted" and its "8-15 notes" early-chapter guide.
- **THE ONLY THINGS TO SKIP.** Genuinely universal knowledge (Shanghai, Beijing,
  "the Yangtze"), and anything the surrounding prose already fully explains. A
  note must still SAY something (a date-span, a fate, a significance) beyond the
  name; a bare "X was a person" is the padding the directive forbids.
- **RESULT.** Chapter 1 carries 73 notes (was 24). Keep this density for every
  chapter; let it taper only as recurring figures get their note once, at first
  appearance (grep notes.json + earlier reading files before re-noting).
- **CHECK.** Read each built chapter asking "could a smart reader hit a name
  here and not know who it is?" If yes, and no note is near, add one.

## Decided renderings (this book's word-level ledger)

_One rendering per recurring item, like the glossary but for diction and
function words. Wrong form on the left, decided form on the right. Grows through
the book._

- 水乡(县城) -> "canal town" (not "water-country town", a calque that also
  collides with "county"). #book
- 四海为家 -> "lived wherever the work sent him" (not "made his home wherever he
  was"). #book
- 一分为二 -> "it cut both ways" / "there are two sides to it" (not "everything
  has two sides", a stiff maxim-calque). #promote
- 初生之犊不畏虎 -> "a green recruit's / beginner's fearlessness" (naturalize; do
  not leave the calf-and-tiger calque raw in prose). #promote
- 绝对安全 -> "safe" (keep "absolutely/wholly safe" at most once per episode).
  #promote
- 田园如画 -> "like a painting" (not "make a picture"). #book
- 相信科学 / 追求上进 -> "put her faith in science" / "had ambition" (render the
  stance, do not leave the bare slogan-calque). #book

## Revision rebaseline (register/style/apparatus pass, R1+) [provenance: REVISION_PLAN.md sec.3]

These rules were approved for the post-completion revision pass, scope TIER 1+2
(tier 3, the deeper topology/contraction rebaseline, was declined by the
commissioner). They are the standing calibration for every revision batch;
the ch02 exemplar diff is the touch-rate target. The governing discipline is
the plan's own: MOST paragraphs LEAVE, a rewrite that only shuffles synonyms is
itself a defect, and when in doubt keep. Honour the KEEP list (plan sec.3.3):
{v} documents, verse, the ch07 obituary, the author's institutional first
person and partisan epithets, and any decided glossary rendering are all frozen.

### RULE. 政治局 is "the Politburo", never "Political Bureau". [#book]
- **WHY.** "Political Bureau" is a bare calque of 政治局; the shelf canon and
  standard English usage is "the Politburo" (with qualifiers as needed:
  "the provisional Politburo", "the Politburo Standing Committee").
- **FIX.** Substitute "Politburo" for "Political Bureau" wherever it renders
  政治局, keeping the qualifier ("provisional Central Politburo", "Politburo
  member"). Purely mechanical; no boundary moves.
- **CHECK.** `grep -n "Political Bureau"` on a swept unit returns nothing.

### RULE. 白色恐怖 is "the White Terror" (capitalized) for the specific KMT terror. [#book]
- **WHY.** The book uses 白色恐怖 as a named historical phenomenon (the post-1927
  KMT terror, extending through the civil-war period); lowercase "white terror"
  under-marks it and the book was split (21 lc / 6 cap at R0).
- **FIX.** Capitalize both words. CARVE-OUT: a genuinely generic, indefinite use
  ("a white terror descended") stays lowercase; read each hit. In ch02 all seven
  body hits were the specific definite terror and were capitalized.
- **CHECK.** `grep -ni "white terror"` and read each; no lowercase specific use
  survives, no generic use is wrongly capitalized.

### RULE. Dates are Month D, YYYY everywhere, apparatus included. [#promote]
- **WHY.** The body was already uniform (Month D, YYYY); the outliers were
  D-Month-YYYY dates in note bodies and one glossary row ("30 August 1929").
- **FIX.** Reformat D-Month-YYYY to Month D, YYYY. Reformat ONLY: the day,
  month, and year values never change (a note that flags a source's wrong year
  keeps that year). Note bodies are edited directly in notes.json via a small
  json load/dump (ensure_ascii=False), NOT by apply_edits (which cannot touch a
  note body) and NEVER by shell heredoc.
- **CHECK.** grep the swept unit's notes for `[0-9]{1,2} (January|...|December)`;
  none remain.

### RULE. Retire the litotes calque; state the thing positively. [#promote]
- **WHY.** 不少/极大 rendered as "no small X" ("no small convenience") is a
  litotes calque that reads as period stiffness in narration.
- **FIX.** Recast to the positive ("a great convenience"). CARVE-OUT: leave it
  where it sits inside a {v} document or quoted matter (ch02:115 "made no small
  contribution", inside Chen Geng's letter, is KEPT), and leave a genuinely
  idiomatic English litotes if one reads naturally.
- **CHECK.** `grep -n "no small\|no few\|no little"`, read each against the KEEP
  list before touching.

### RULE. "could not but / could not help / had no wish to" get the plain equivalent. [#promote]
- **WHY.** These are stiff litotes-adjacent auxiliaries flagged at R0.
- **FIX.** Plain equivalents: "had to", "couldn't help", "did not want to". NOTE
  ON SCOPE: the contraction here ("couldn't help asking") is the prescribed
  tier-1 equivalent for THIS formula only; it is NOT the declined tier-3 program
  of contracting narration generally. Do not read the exemplar as licence to
  contract narration elsewhere.
- **CHECK.** `grep -n "could not but\|could not help\|had no wish"`.

### RULE. 等-tags: vary and thin, but only genuine tics; keep the tag alive. [#promote]
- **WHY.** 等/等人 rendered as "and others / and the others / and the rest / and
  so on" recurs (76 book-wide). The defect is a single tag DOMINATING and, worse,
  a tag re-listing names already just named, or clustering three to a paragraph.
- **FIX.** Three techniques: cut where the list is complete or the tag is
  redundant with an opener like "many ... that could be used: ..., and so on";
  reposition/vary ("among others"); and cut a redundant re-listing ("Zhou Enlai,
  Li Weihan, Deng Xiaoping, and the others laid on a banquet ... the others all
  warmly agreed", not the names a second time). Target: no single tag dominating,
  NOT zero. Be surgical: in ch02 the tags were already well varied, so only three
  genuine tics were touched, and any tag sitting inside a note anchor was LEFT
  (do not restructure anchored text for a tic; the anchor breaks).
- **CHECK.** After a sweep, no single tag dominates the unit and no paragraph
  stacks three; `grep` the changed spans against note anchors first.

### RULE. "one after another / one after the other" is varied, not repeated. [#promote]
- **WHY.** 先后/一个个/陆续 all fall to "one after another"; it recurred 16 times
  book-wide.
- **FIX.** Vary by sense: "in turn", "one by one", "a few at a time", "in
  succession", or cut. Keep one instance where it reads best; not zero.
- **CHECK.** `grep -n "one after another\|one after the other"`; more than one or
  two of the same phrasing in a chapter is a rewrite.

### RULE. Convert the awkward "the X-ing of the Y" nominalization to a finite verb, where it helps. [#promote]
- **WHY.** 的 nominal phrases calque to "the drawing of a double agent out of the
  enemy's camp"; a finite verb reads better ("drawing a double agent out ...").
- **FIX.** Convert the awkward ones to finite verbs; LEAVE the idiomatic set
  outright ("the founding of the nation / of the Section", "the killing of these
  men", "the shooting of the four" all read naturally). This is the smallest of
  the classes: in ch02 only one conversion earned its place. Do not force the
  ones that already read as English.
- **CHECK.** `grep -noE "the [a-z]+ing of"`; convert only what fails the
  read-aloud test.
