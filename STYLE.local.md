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

Ye Xiaoshen is a popular narrative historian who buttonholes the reader,
editorializes, and reveres his subjects: the target in English is a first-rate
popular history that carries his heat and his sardonic edge in the verbs and the
rhythm, not in exclamation and rhetorical questions. Read him toward the
gripping-but-controlled register of a good English narrative-history writer
(think the storytelling drive of a Hochschild or a Chang, not a Victorian
chronicle); keep the warmth toward the reader, lose the carnival-barker volume.

### DELIBERATE devices to PRESERVE, not "fix" (a later batch must not iron these out)
- The **front/reverse (正面/背面) parallelism** and other short anaphoric
  one-line paragraphs that pivot a section (e.g. Gu's "public face"/"hidden
  face"; the two Lenin/Yu Zecheng aphorisms). These are the author's structural
  hinge and are parity-locked one-per-source-line. Keep them.
- **Quoted verse and allusion the author himself quotes** (Mao's "dared to bid
  the sun and moon light a new sky"; Lu Xun's "one soldier left"; Yang Du's
  plum-blossom couplet; Ho Chi Minh's couplet; Tan Sitong; the Jingwei bird;
  the closing Latin maxim). Render these at full elevation and footnote; do not
  flatten to plain prose. A blind critic without the source will read them as
  "vague/purple" — they are load-bearing quotations.
- The **interested-witness heat** (the martyr set-pieces, "raised high the
  banner of truth"): keep the temperature; footnote the verdict, never launder
  the framing.

## Calibrated rulings (grows through the book)

Built at the first-chapter voice gate from a blind context-free critique.

### RULE. Trim the source's four-character near-synonym pairs to one word, or draw the real distinction; never mirror the whole parallel string. [#promote]
- **WHY IT HAPPENED.** Ye piles 并列 doubled pairs and four-clause parallels
  (庞大恢宏、光怪陆离; 撇得清清楚楚，切割得干干净净; 以血还血，以牙还牙，以暴力还击暴力…);
  carried feature-for-feature they read as a chain of doubled synonyms, the
  single loudest translationese fingerprint in the draft.
- **FIX.** "droll and daring, elegant and free; grander and stranger, bizarre"
  &rarr; keep the real contrasts ("droll and daring, elegant and unforced"),
  trim the pure synonym to one ("grander and more bizarre"). "answer blood with
  blood, tooth with tooth, force with force, meet the two hands…with the two
  hands" &rarr; "answer blood with blood and force with force, meet
  counter-revolution's two hands with two of the revolution's own."
- **CHECK.** Read every list of three-plus parallel clauses aloud; if two carry
  the same idea, cut one. Grep a finished unit for repeated "and X and Y and Z"
  runs.

### RULE. Render a Chinese idiom for its SENSE when its literal image will not land in English; keep the image only where it lands; push a classical allusion to a note rather than dropping a raw calque in the body. [#promote]
- **WHY IT HAPPENED.** 成语 transplanted as a picture (鱼龙混杂 "fish and dragon";
  九腔十八调 "nine tones eighteen tunes"; 暗鸣则山岳潜形 "a whisper hides mountains";
  灰头土脸 "dust-faced"; 春申门下三千客) is opaque to a reader without the note.
- **FIX.** "a Shanghai of every sort of fish and dragon" &rarr; "a Shanghai that
  jumbled together every kind of character, honest and crooked." "nine registers
  and eighteen tunes" &rarr; "could pitch his voice a dozen ways." "downcast and
  dust-faced" &rarr; "crestfallen."
- **CHECK.** For each idiom ask: could a reader with no note picture this? If
  not, render the sense (and, for a genuine allusion, footnote it).

### RULE. No fake-antique or vaguely grand filler; reach for the plain precise word. [#promote]
- **WHY IT HAPPENED.** Reaching for elevation to match the author's warmth
  produced mock-antique tags ("so amazed the beholder", "rose without a check",
  "reached the summit and past all sounding", "won his whole admiration").
- **FIX.** &rarr; "that left onlookers marveling", "rose fast", "was consummate,
  past all sounding", "won him over completely." Period flavour comes from
  precise period nouns, not from antique grammar.
- **CHECK.** Any phrase that sounds like a Victorian rendering of Scripture goes
  (the CLAUDE.md falsifiable test).

### RULE. 这是X说的 is "so said X", never "that was X"; do not calque the source's trailing attribution formula. [#book]
- **WHY IT HAPPENED.** 敌人不睡觉，这是列宁说的 traced as "…: that was Lenin."
- **FIX.** "The enemy never sleeps &#8212; so said Lenin."
- **CHECK.** Grep built units for "that was " before a name.

### RULE. Where the author glosses his own list by re-listing it, compress; do not print the same run of items twice in two forms. [#book]
- **WHY IT HAPPENED.** 讲究"捆、绑、藏、掖、撕、携、摘、解"，也就是…捆起、绑好… (eight verbs,
  then the same eight re-listed as backstage/onstage) reads as tedious doubling.
- **FIX.** &rarr; "…'bind, tie, hide, tuck, tear, carry, pluck, loose' &#8212; the
  first four for making ready backstage, the last four for the show out front."
- **CHECK.** When the source says 也就是/即 and re-lists, fold the gloss.

### RULE. Ration the ornate atmosphere-epithet; one per stretch, not one per paragraph. [#book]
- **WHY IT HAPPENED.** Ye reaches for a fresh ornate Shanghai/atmosphere phrase
  constantly (灯红酒绿、纸醉金迷; 鱼龙混杂; 危机四伏; 血雨腥风; 波谲云诡); rendered each in
  full they accumulate into purple.
- **FIX.** Keep the strongest instance in a passage, plain the rest.
- **CHECK.** Per section, count the ornate weather/city epithets; if more than
  one or two land in a page, thin them.

### RULE. Litotes and definiteness: 不少 is "a good many," not "no few"; render the article the sense wants. [#promote]
- **WHY IT HAPPENED.** 不少 traced as "no few"; 外国魔术 (a category) rendered "the
  foreign import" instead of "a foreign import." Small calques that still read
  as translated.
- **FIX.** "learned no few lessons" &rarr; "learned a good many lessons";
  "never quite the foreign import" &rarr; "never quite a foreign import."
- **CHECK.** Grep built units for "no few / no small / not a little."

### RULE. No fronted "the more deeply / the more X" adverbials, and no imperative-then-past clash; keep the author's rhetorical questions but in natural English order. [#book]
- **WHY IT HAPPENED.** 怎能不更深理解 traced as "how can we not the more deeply
  understand"; 环顾…(imperative survey) + past tense clashed.
- **FIX.** &rarr; "how can we not understand, more deeply still"; "In all the
  Chinese magic world of the 1920s, only Zhang Huichong caught his eye."
- **CHECK.** Read every rhetorical question aloud; the verb order must be
  ordinary English.

(Round 2 of the blind loop opened "polished, high-accomplishment... mostly
real English" and its findings folded into the rules above; the apparatus read
clean with nothing to blue-pencil.)

### RULE. 享年X岁 is "at the age of X" (died aged X), never "in his Xth year"; and 两/三 + a count-word stays a number when both/all the referents are named. [#promote]
- **WHY IT HAPPENED (B05).** 享年87岁 first drafted "in his eighty-seventh year"
  (which means aged 86, an off-by-one); 两同志 + both names first dropped the
  "two", so the number check flagged a missing 2.
- **FIX.** "let go of the world at the age of eighty-seven"; "the two comrades
  Xiong Jinding and Zhu Duanshou". Naming both people does not carry the count
  for the reader OR the check, so keep the "two/three".
- **CHECK.** Grep a finished unit for "th year" after an age; read every 享年.
  When the source counts a named group (两/三/五 + 同志/人/位), keep the numeral.

### RULE. Render a term the glossary has already DECIDED in its decided form; do not re-translate it fresh. [#book]
- **WHY IT HAPPENED (B05).** 老虎灶 was decided "laohuzao" (and glossed inline at
  its ch03 first use), but B05 first drafted it "tiger-stove" &#8212; caught by
  qc_entities against the glossary, not by eye.
- **FIX.** Consult glossary.json BEFORE rendering any recurring term; laohuzao,
  shikumen, tingzijian stay romanized per the shelf's decisions.
- **CHECK.** Run qc_entities every unit; a "not found in English" on a term (not
  a person) usually means a decided rendering was silently overridden.

### RULE. Render the author's source-criticism as running skeptical argument in plain English, not a wooden "one source says X, another says Y" catalogue; keep the sources' own wrong words and let the note or his next sentence carry the correction. [#book]
- **WHY IT HAPPENED (B07).** Ch07 weighs half a dozen memoirs against one
  another (where the congress met; whether "Fang Lin" was Deng Fa). Traced flat,
  a chain of 却说 / 也说 / 沿袭 / 凡此种种…都是从…而来 reads as a bibliography, and
  the author's dry, deductive voice is lost.
- **FIX.** Keep the connective logic he actually uses ("all of these derive
  from...," "if X, then Y could hardly have..."), and let the sources keep their
  own error (the memoirs' &#8220;British Concession&#8221;; the caption's misidentified
  photo) &#8212; render it as printed, footnote the correction, never launder it into
  the right answer in his mouth.
- **CHECK.** Read a source-criticism run aloud: does it move like a person
  reasoning, or like a footnote pile? Every source's claim stays in that source's
  words; the verdict lives in the note.

## ★ THE REGISTER REBASELINE (B09 commissioner review) ★

This section was written from the commissioner's whole-book read of the B08
build. It is the single most important part of this file. It does not add a few
more tics to fix; it resets the DEFAULT register of the whole book, narration
included, and every remaining chapter (ch09-ch15) must be drafted against it so
the back half is congruous with the front and the final cleanup pass over
ch01-ch08 is short. Read this section before drafting a single paragraph.

### THE MASTER PRINCIPLE (read this first, apply it everywhere)

**Modern-neutral is the default register for everything, narration included.
Period flavour comes from the CONTENT (rickshaws, concessions, silver dollars,
patrolmen, the Green Gang), never from antique SYNTAX.** A book about 1929 does
not have to be written as if published in 1929. Wakeman writes about these same
Shanghai streets in wholly contemporary prose and loses nothing.

Three voices, three registers, and the line between them is bright:
- **Documents sound like documents.** Quoted 1920s-30s communiqués, Party
  resolutions, court verdicts, official telegrams, formal Party language MAY
  stay starchy and formal. That is period work, and it is correct.
- **The narrator sounds like a smart writer today** &#8212; someone explaining this
  history to an intelligent friend who is not in the field. Not a magistrate,
  not a costume-drama butler.
- **People sound like people.** The wet-nurse, the thugs, the cab driver talk
  plainly. The 2007-2013 interviewees (Li Lili, Qian Hong, Nie Li, Dong
  Huifang, Zhang Sengbao, the martyrs' children) talk like people on camera
  now, contractions and all. They currently sound like the narrator, and the
  narrator currently sounds like a magistrate; fix both.

**THE READ-ALOUD TEST (apply to every sentence).** Say it aloud. If you can
hear a PBS costume-drama butler saying it, rewrite it. If you can hear yourself
saying it to a friend who is smart but not in the field, it is done. This test
governs all the rules below; when in doubt, it is the tiebreaker.

What to KEEP (do not "modernize" these): the author's genuine rhetorical
architecture &#8212; the anaphora, the one-line staccato paragraphs, the epithets
("hawks and hounds," "running dogs," "reactionaries," "our Party"). Those are
his voice and read as deliberate style in modern prose too. See also the
"DELIBERATE devices to PRESERVE" list above; that list still stands. The
rebaseline changes the SYNTAX and the FUNCTION-WORD register of the narrator,
not the author's structural devices or his political voice.

### RULE. Kill inversions and fronted objects entirely. Zero survivors. [#promote]
- **WHY.** Fronted-object / inverted-verb order (verb-final 把/topic-comment
  carried into English) is the single loudest "old book" signal. 李强一眼看穿
  became "His guilty scheme Li Qiang saw through at a glance."
- **FIX.** Ordinary subject-verb-object. "Li Qiang saw through the scheme at a
  glance." "Most rare and precious of all: ..." &rarr; "Rarest of all, ..."
- **CHECK.** This is ZERO-tolerance, not "once a chapter." Grep each unit for
  sentences that open with an object or a fronted adverbial where the subject
  arrives late; recast every one. Read openings aloud: does the sentence start
  with who-does-what?

### RULE. Retire the antique function-word set; each has a plain modern equivalent. [#promote]
- **WHY.** No single one is wrong; collectively they are the mothball smell. The
  narrator defaults to 1893.
- **KILL LIST (grep every unit for these):** "besides" as a sentence adverb
  ("and a wet-nurse besides") &rarr; "as well" / "too" / cut; "thereupon,"
  "whereupon" &rarr; "then" / "at that"; "at length," "presently," "ere long,"
  "before long" (when it is every third paragraph) &rarr; "eventually," "soon,"
  or cut; "of a morning / of an evening" &rarr; "in the morning"; "it was gone
  nine" &rarr; "it was past nine"; "had no wish to" &rarr; "did not want to";
  "was wont to" &rarr; "used to"; "in his lifetime" as a quote tag &rarr; "while
  he was alive" or cut; "let slip," "made bold to," "come what may," "for all
  that," "and no mistake," "still less could" &rarr; plain equivalents or cut.
- **FIX.** Reach for the plain modern word the read-aloud test would use.
- **CHECK.** Keep the kill list as a grep battery; run it every unit. A hit is
  not automatically wrong, but each hit must be defended against the read-aloud
  test or replaced.

### RULE. Allow contractions in narration, not only in dialogue. [#promote]
- **WHY.** "did not / could not / would not" at 100% frequency is a huge part of
  the starch. Three "he did not dare" a page reads like a deposition.
- **FIX.** Contract maybe a third of the time, wherever the rhythm wants it.
  "He didn't dare keep 'Miss Wang' at his side either" reads fine. Dialogue and
  the interviewees contract freely; formal documents do not contract at all.
- **CHECK.** If a paragraph of narration has zero contractions and three
  negated auxiliaries, contract one or two by ear.

### RULE. Dialogue and interview speech get full modern treatment. [#promote]
- **WHY.** Characters currently talk like the narrator, i.e. like a magistrate.
  A chengyu spoken in dialogue is not a reason to keep it ceremonial in English.
- **FIX.** Gu Shunzhang: 正求之不得 "That is exactly the chance I could wish for"
  &rarr; "That's exactly the chance I want." Cai Mengjian: 打开天窗说亮话 "let us
  throw open the skylight and speak in the clear" &rarr; "then let's put our
  cards on the table" (keep the skylight image in a NOTE if it is worth it; it
  is a chengyu anyway). The 2007-2013 interviewees speak in contemporary spoken
  English, contractions and all.
- **CHECK.** Read each quoted line as speech. Would a person say it out loud
  today? Documents excepted.

### RULE. Compress rhetorical ceremony; do not preserve it clause for clause. [#promote]
- **WHY.** 怎能不…更… ceremonial questions and paired exclamations are the
  author's HEAT, but rendered full they read as purple, not warm (see the voice
  note up top: carry the heat in the verbs and rhythm, not the volume).
- **FIX.** "How can we not cherish his memory all the more...?" &rarr; "It's
  hard not to think of him." Cut the SECOND of any consecutive rhetorical pair
  outright.
- **CHECK.** Per rhetorical question or exclamation, keep the heat, halve the
  words. Consecutive pair: delete one.

### RULE. Modernize quote tags; vary them. [#promote]
- **WHY.** "said in his lifetime," "recalled in his later years," "disclosed
  many years later" every single time is a tic and an archaism at once.
- **FIX.** "later recalled," "said in a 2007 interview," "wrote decades later,"
  or just "said." 晚年回忆 &rarr; "later recalled," not "recalled in his later
  years." 生前说过 &rarr; "once said" / "said while he was alive."
- **CHECK.** Grep for "in his lifetime," "in his later years," "many years
  later" as tags; vary or plain them.

### RULE. Break the source's sentence topology; the information order is not sacred, the sentence boundary is not sacred. [#promote]
- **WHY.** Chinese academic-narrative prose builds one sentence from a topic
  plus a chain of comma-spliced predicates and stacked appositives, and it reads
  fine because Chinese does not track subject-verb agreement or relative-pronoun
  distance across the chain. English does. Carried over intact, the reader must
  hold the subject in working memory across 60-100 words of apposition. The
  Qian Xuantong sentence in ch08 is the type specimen: subject ("Qian
  Zhuangfei"), then a dash-parenthetical containing a whole second biography
  (Qian Xuantong and the national-language movement, Hu Shi, Lu Xun's <i>A
  Madman's Diary</i>), and only then the main verb ("passed into the Peking
  Medical Specialist School"). The Xu Enzeng title-strings, the Yang Zhihua bio
  in ch02, and the Berzin passage in ch01 do the same.
- **FIX (mechanical).** Any appositive over ~15 words becomes its own sentence,
  placed before or after; the main clause gets its verb within the first ~20
  words. "Qian Zhuangfei was born in 1895... In 1915, with the help of his
  kinsman Qian Xuantong, he passed into the Peking Medical Specialist School.
  (Qian Xuantong was the man at whose urging Lu Xun wrote <i>A Madman's
  Diary</i>...)" Nothing is lost. Same for the author's comma-splice cascades:
  English tolerates two coordinated predicates comfortably, three at a stretch;
  past that, split.
- **CHECK.** For every sentence, find the main verb: is it within the first ~20
  words? Count the appositive between subject and verb: over ~15 words, lift it
  out. Count coordinated predicates: over three, split.

### RULE. De-nominalize: "the [gerund] of the [noun]" becomes a finite verb. [#promote]
- **WHY.** Chinese 的-phrases and verbal nouns tempt "the X-ing of the Y": "the
  scattering of already-exposed Party cadres, the safeguarding of the Party
  Center's organs, the covering of the Party's leading cadres in their move,"
  "the sending-out of spies," "the giving of oneself up, the informing, the
  defecting." Each forces an "of," often two; strung together they make the
  committee-minutes trudge.
- **FIX.** Finite verbs: "scattering cadres who'd been exposed, safeguarding the
  Center's organs, covering the leading cadres as they moved." Convert roughly
  two-thirds of them.
- **CHECK.** Grep each unit for "the [gerund] of" and "the [noun]-and-[noun]
  of"; convert most to verbs.

### RULE. Collapse doubled synonyms to the stronger single word; keep the doublet only when the two words genuinely differ. [#promote]
- **WHY.** (Extends the four-character-pair rule above; the commissioner names
  this the highest flow-per-keystroke edit on the whole list.) Chinese
  four-character parallelism (整顿改组, 威胁利诱) is rhythmic in the original because
  Chinese rhythm is bisyllabic balance; English rhythm is stress VARIATION, so
  every rendered doublet ("tighten up and reorganize," "threats and
  inducements," "corrupt and debased," "arrogant and overbearing," "obeyed to
  his face and defied him behind his back") costs rhythm instead of adding it.
- **FIX.** Collapse to the stronger word when the two do not really differ
  ("reorganize," "coercion," "debased," "overbearing"); keep both only when they
  carry distinct content.
- **CHECK.** Grep "X and Y" pairs where X and Y are near-synonyms; collapse
  roughly two-thirds.

### RULE. Cut the 即 / 也就是 pivots ("which was to say / that is / namely / in other words"). [#promote]
- **WHY.** They render 即 / 也就是 and appear constantly; each stalls the sentence.
- **FIX.** Usually an appositive comma or a colon does the work. "the Zhongtong,
  that is to say the Party Affairs Investigation Section" &rarr; "the Zhongtong
  &#8212; the Party Affairs Investigation Section."
- **CHECK.** Grep "which was to say," "that is to say," "in other words,"
  "namely"; replace most with punctuation.

### RULE. "could only / could not but / could not help / cannot help asking" is a register problem, not a stray tic. [#promote]
- **WHY.** 只能 / 不得不 / 不禁 / 不能不 carried literally. Part of the 1893 default.
- **FIX.** "He could only come without a shadow and go without a trace" &rarr;
  "He had to move without a trace." "We cannot help asking" &rarr; "It's worth
  asking," or just ask the question. 不禁 &rarr; often just cut.
- **CHECK.** Grep "could only," "could not but," "cannot help," "could not
  help"; plain each.

### RULE. "In the end" is not an interrogative intensifier; it calques 到底 / 究竟. [#promote]
- **WHY.** "Did Gu Shunzhang, in the end, perform magic in Hankou or not?"
  "Why, in the end, did Gu Shunzhang want to...?" Native English does not use
  "in the end" this way inside a question.
- **FIX.** "Did he actually perform magic in Hankou?" "So did he or didn't he?"
  "Why did Gu Shunzhang really want to...?" or just cut it. (Narrative "in the
  end" meaning "ultimately, after all" is FINE; only the interrogative use is
  the calque.)
- **CHECK.** Grep "in the end" inside a question; recast. Leave the narrative
  ones.

### RULE. Stop quilting sources out of two-to-five-word scare-quoted fragments; quote only distinctive wording. [#promote]
- **WHY.** Long stretches stitch tiny quotations into the translator's own
  syntax with quotes every few words (the Li Zheshi courtship passage in ch03,
  the Xu Enzeng material in ch08, the Bo Yibo paragraph in ch01). It is faithful
  to the author's fragment-collage method, but in English the visual density of
  quotation marks is exhausting and starts to read as irony / scare-quoting.
- **FIX.** Where the borrowed phrase is unremarkable ("felt he was like the
  older comrades"), drop the quotes and paraphrase. Keep quotes only for
  genuinely distinctive wording that earns them.
- **CHECK.** Count quote-marks per paragraph; if a paragraph has more than a few
  short quoted fragments, un-quote the unremarkable ones. (This is a
  presentation change, not a fidelity change: the words stay, the quote-marks
  go.)

### RULE. Front-load the attribution when a quote shifts tense or person. [#promote]
- **WHY.** Quotes open cold and reveal the speaker only in a trailing "(Zhou
  Enlai, 1980)." Inline, this forces a re-read; ch01's "In the year and a half
  since the 'August Seventh' Conference... organizations have been broken" hits
  as a tense error until the citation lands three sentences later.
- **FIX.** Signal the speaker first wherever a quote changes tense or person:
  "As Zhou Enlai reported in 1929: ..." The trailing (Name, year) citation can
  stay as the precise reference, but a lead-in must warn the reader a quote is
  starting.
- **CHECK.** Any block or inline quote whose first words are in a different
  tense/person than the surrounding narration needs a lead-in signal.

### RULE. Vary or cut "and the rest" / "and the others" for 等 after name-lists. [#promote]
- **WHY.** It renders 等 after every name list and appears dozens of times per
  chapter (62 across ch01-ch08 at review time).
- **FIX.** Vary with "among others," restructure the sentence, or where the list
  is complete, cut it entirely. Do not use the same tag every time.
- **CHECK.** Grep "and the rest" / "and the others" per unit; if either exceeds
  a handful, thin and vary them.

### RULE. Trailing dramatic ellipses are a Chinese punctuation convention; keep them only inside quoted dialogue the source truncates. [#promote]
- **WHY.** "the fellow screamed and let go..." reads as pulp in English
  fiction-adjacent prose. The source's ...... is atmospheric convention.
- **FIX.** In narration, end the sentence with a full stop. Keep "..." only
  where it sits inside a quotation whose source actually breaks off.
- **CHECK.** Grep the ellipsis character; each one in narration becomes a period
  (or the sentence is completed).

### RULE. Restore the predicate after an em-dash aside that has eaten the main verb. [#promote]
- **WHY.** A parenthetical chain swallows the verb: ch01's "The 'removal' of a
  certain 'Qixing Magic Research Society,' and the enlargement of that same
  society... from No. 22... to No. 679..., just left of the Xieqiao Club." No
  main verb; the reader is stranded until the next sentence rescues it. More of
  these in ch04 and ch08.
- **FIX.** Give the sentence a finite main verb; break the parenthetical chain
  out if it is long (see the topology rule).
- **CHECK.** Any sentence with a long em-dash / parenthetical middle: locate the
  main verb. If there isn't one, add it.

### RULE. No sentence-initial numerals. [#promote]
- **WHY.** "350,000 is no small figure." reads as raw.
- **FIX.** Recast: "A figure of 350,000 is no small thing," or spell it, or
  reorder so the sentence does not open on a digit.
- **CHECK.** Grep for a line beginning with a digit; recast.

### RULE. One national spelling anchor: AMERICAN English throughout. [#promote]
- **WHY.** British colloquialisms ("it was gone nine," "welshed on the bill,"
  "and no mistake," "shook his head like a rattle-drum") sit beside American
  "catty-corner" and American spellings. The archaic-genteel register needs one
  national anchor, and the body is mostly American.
- **FIX.** American spelling and idiom everywhere: Center (not Centre), Theater
  (not Theatre), Labor, License, Rumor, Color, honor, neighbor, -ize. This
  includes the not-yet-translated stub TITLES in book.json (ch12 "Licence
  Plate," "Rumour Kills," "True Colour" &rarr; "License Plate," "Rumor Kills,"
  "True Colors"). British colloquialisms go too ("it was gone nine" &rarr; "it
  was past nine").
- **CHECK.** Grep the British-spelling battery (colour|rumour|licence|honour|
  labour|neighbour|theatre|centre|defence|realise|organise|recognise) across
  reading files, notes.json, glossary.json, AND book.json titles.

### RULE. Dates: month-day-year, everywhere. [#book]
- **WHY.** ch01-ch02 used day-month-year ("14 November 1927"); ch03-ch08 use
  month-day-year ("April 15, 1928"). Same book, two formats.
- **FIX.** Month D, YYYY everywhere ("November 14, 1927"). Fix ch01 (19 dates)
  and ch02 (3 dates) to match; draft all later chapters this way.
- **CHECK.** Grep the "D Month YYYY" pattern; there should be zero in the body.

### RULE. The apparatus is part of the register too: gloss once, not every time. [#book]
- **WHY.** Street-name glosses repeat endlessly ("Avenue Road (today Beijing
  West Road)" eight or ten times); repeated person-glosses too (Xu Enzeng's full
  title-string three times). The reader does not need the parenthetical every
  time, and the repetition is its own kind of drag.
- **FIX.** Gloss a street or a repeated title-string at most ONCE per name,
  book-wide, backed by the back-matter gazetteer and Principal Characters page
  (see Apparatus policy below). After the first gloss, use the name plain.
- **CHECK.** Grep a repeated "(today X)" gloss; keep the first, cut the rest.

### Chengyu triage (the three-way rule, extending the idiom rule above) [#promote]
The book stacks chengyu, often unglossed, and treats three different kinds
identically. Sort every idiom into one of three bins:
1. **Self-evident from the image &#8212; keep literal.** "cliff's edge," "tiger's
   mouth." The English picture carries the sense.
2. **Culturally load-bearing but opaque &#8212; keep and FOOTNOTE.** "the Horse King
   has three eyes," "keeps clear of the melon patch and the plum tree" (瓜田李下),
   "gather the moon nearest the water" (近水楼台). The image matters; the reader
   needs the note.
3. **Carries no image an English reader can parse &#8212; silently naturalize to the
   sense.** 不是省油的灯 "no lamp that burns without oil" means "no pushover" and
   nothing in the English suggests it &rarr; render "no pushover." Likewise "lost
   the three souls from her head and the five from her feet" (魂飞魄散) &rarr;
   "scared out of her wits"; "a louse on a bald man's head" (obvious &rarr; keep),
   "water drawn in a bamboo basket" (竹篮打水 = all for nothing) &rarr; naturalize;
   "saying its prayers in a snail shell" &rarr; naturalize.
Worst offender to date: ch06 s1, four chengyu in one sentence ("lower the flags
and still the drums... not to beat the grass and startle the snake... wait by
the stump for the hare, take the turtle in the jar"). Keep at most the one that
lands, naturalize the rest, footnote any single one worth preserving.
- **CHECK.** For each idiom, name its bin before rendering. Bin 3 idioms must
  not reach the body as raw calques.

## Consistency canon (ONE rendering, book-wide) &#8212; decided this review

Draft ch09-ch15 with these already in force; they are also the ch01-ch08
cleanup checklist.

- 中央 (the Party center) &rarr; **Center** (American), never "Centre". (ch05 had
  13 "Centre"; the rest of the book uses "Center".)
- 中央政治局 &rarr; **the Politburo** (with qualifiers as needed: "the Central
  Politburo," "the provisional Central Politburo," "the Standing Committee of
  the CCP Politburo," "an alternate member of the Politburo"). NEVER "Political
  Bureau." (ch07-ch08 drifted to "Political Bureau of the CCP Central
  Committee"; same body, collapse it.)
- The Comintern report of **June 3, 1932** is ONE document. Canonical rendering
  (first appears ch01): issued by **the Special Work Department of the Comintern
  Executive Committee**, titled **"Written Report on the State of Secret Work and
  Special-Service Work of the Communist Parties in the Far Eastern and Near
  Eastern Countries"** (June 3, 1932). ch04 ("Intelligence Department"... "and on
  Their Intelligence Work") and ch08 ("special-agent department"... "Report on
  the State of the Secret and Secret-Service Work...") are the SAME report;
  normalize both to the canonical form so a reader does not think there are
  three documents. Note at first appearance that it is cited again later.
- Xia Yan's memoir 《懒寻旧梦录》 &rarr; **<i>Lazily Seeking Old Dreams</i>**
  (italic), never "Idly Seeking an Old Dream" (ch08). Book titles are italic.
- 董健吾 as head clergyman of St. Peter's &rarr; **presiding pastor** (ch01 had
  "officiating pastor").
- 白色恐怖 &rarr; **the White Terror** (both words capitalized; it is the specific
  1927-onward terror). Not "white terror" / "White terror".
- Set phrase 十里洋场 &rarr; **the ten-li foreign quarter** (lowercase, one form),
  glossed/footnoted once; not "the Ten-Li Foreign Settlement" (ch05).
- Lane/alley names 里 / 坊 / 弄: render FUSED, one capital &#8212; **Jingyuanli,
  Wangdeli, Hehefang, Hengchangli, Fukangli, Sichengli, Fudefang, Yujili**.
  This is the majority form already in the glossary and the standard scholarly
  transliteration; the two split outliers ("Fukang Li," "Sicheng Li") were
  fused to match. One rule, everywhere.
- Place names: **pinyin**, with the period concession/postal name glossed ONCE
  (then via the gazetteer). The one science institution known by its historic
  name: render **the Xujiahui Observatory** (pinyin, for one locale) and note
  its period name Zikawei once; do not leave "Zikawei Observatory" (ch06) beside
  "Xujiahui Road" (ch04).
- Foreign-concession street names keep their **French/English period names with
  a modern pinyin gloss** (Avenue Joffre, Route Voisin (today Fumin Road)); the
  gloss appears once per street (gazetteer).
- 顾顺章 birth year: the text says **born 1895 (one account says 1907)**; the
  Principal Characters page must not introduce a third date. Use 1895 there.
- Measurements: keep **li** where it is idiomatic ("the ten-li foreign quarter")
  with a note; for plain distances the source gives in figures, use ONE metric
  standard (meters/kilometers), do not mix li and meters for ordinary distances.
- Cited-work titles: **English only in the body**, full bilingual entry in the
  back-matter Works Cited. One rule; book titles italic in the body.

## Apparatus policy (decided this review)

- **Translator's note on conventions, up front (expand the existing one).** Half
  a page stating: romanization is pinyin except conventional forms (Whampoa,
  Kuomintang, Chiang Kai-shek, Sun Yat-sen) and Western scholars' own names;
  concession street-names keep their French/English period forms with modern
  pinyin glosses; currency (yuan vs. silver dollars) policy; li retained where
  idiomatic; and &#8212; MOST important &#8212; that "our Party," "reactionaries,"
  "running dogs" and the polemical register are the AUTHOR'S voice, preserved
  deliberately, not the translator's. A Western reader who picks this up cold
  may otherwise mistake the author's voice for the translator's. One paragraph
  inoculates the whole book.
- **Back-matter street gazetteer** (old/period name &rarr; today's name), so each
  street is glossed ONCE in the gazetteer and at most once in the body. Same
  courtesy for the handful of repeated full title-strings.
- **Principal Characters page: grow to ~20 recurring figures** (currently four,
  which promises help it does not deliver). Cover everyone who recurs across
  chapters: the Three Heroes (Qian Zhuangfei, Li Kenong, Hu Di), Li Weihan,
  Chen Yun, Xu Enzeng, Cai Mengjian, Dong Jianwu, Qu Qiubai, Li Qiang, Zhang
  Shenchuan, Chen Geng, Zhou Enlai, Gu Shunzhang, and the rest. Flag them
  `"principal": true` in glossary.json.
- **Brief timeline (1925-1935) in front matter.** The author jumps decades
  constantly (a 2007 interview inside a 1929 event inside a 1975 deathbed
  scene). An anchor page costs little and pays off for a reader without the
  background.
- **TV-drama references get a note on FIRST mention and a cross-reference
  after.** Yu Zecheng / <i>Lurk</i> (潜伏), <i>The Road Through Vicissitudes</i>
  land with zero force for anglophone readers; each needs a first-mention note
  saying it is a famous PRC spy drama, and a cross-reference (not a fresh note)
  when it returns.
- **Flag the author's factual problems with a bracketed [&#8212;Trans.] note,
  uniformly.** When the source contradicts itself (the ch06 trainee counts
  16/18/20; the two rescue-attempt geographies; the ch08 Zhang-Guodong/Yang-
  Yingqi attribution tangle), a consistent [&#8212;Trans.] flag or a footnote lets
  you mark it WITHOUT rewriting the author. Visible interventions are currently
  caption-only, so mid-text problems just sit there looking like translation
  errors. Decide it once, apply it uniformly.
- **Interim stub page for circulated builds.** While ch09-ch15 are unwritten, a
  single "Chapters 9-15 forthcoming" interim page reads better to any outside
  reader than per-section source-page pagination scaffolding; keep the detailed
  stubs in the working branch only.

## Process note (from the commissioner)

Freeze THIS style sheet, translate ch09-ch15 against it, and only THEN run one
mechanical cleanup pass over ch01-ch08. Fixing Center/Centre and dates now and
then re-introducing the drift while drafting new chapters doubles the work.
The back half is drafted congruous; the front half is swept once at the end.

## Decided renderings (this book's word-level ledger)

- 中央特科 &rarr; **the Central Special Branch** (short handle: the Special Branch).
- 红队 / 打狗队 &rarr; **the Red Squad** / **the dog-beating squad** ("beating the
  dogs" for 打狗 = eliminating traitors).
- 特务工作 (of the domestic security organ) &rarr; **special-service work**, not
  "spy work"; 侦察 in the security context &rarr; **investigation / surveillance**,
  not military "reconnaissance" (keep "reconnaissance" for Chen Geng's 1943
  battlefield 侦察).
- 化广奇 &rarr; **Hua Guangqi** (Gu's stage name); 黎明 &rarr; **Liming**, glossed
  "the Dawn" at first use.
- 王庸 &rarr; **Wang Yong** ("Mr. Wang" / "Mr. Wang Yong" in dialogue).
- 亭子间 &rarr; **tingzijian** (italic, first-use note).
- 摩登 &rarr; **modern / gone modern** (the Republican loanword; keep the flavour).
- 万 count-unit &rarr; full value ("310,000", "26,000"), never "31 wan"; the
  book's mixed **arabic+万** ("2.6万") is handled in check_numbers.py.
- 白相人 &rarr; **street-corner toughs**; 巡捕 &rarr; **concession patrolmen**;
  捕房 &rarr; **police station** (concession); 探目 &rarr; **detective sergeant**.
- Names follow authority.json: Chiang Kai-shek, Zhou Enlai, Sun Yat-sen,
  Kuomintang, Avenue Joffre; all others standard pinyin. Western scholars keep
  their own names (魏斐德 = **Wakeman**, not "Wei Feide"; 维克托·乌索夫 = **Victor
  Usov**; 别尔津 = **Berzin** / Jan Berzin).
