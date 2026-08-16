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
