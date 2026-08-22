# STYLE.local — book-specific ledger for *China's Secret War*

The living style ledger for THIS book. The composed `STYLE.md` is a build
artifact from the shelf-wide layers; this file is where THIS book's own
decisions accumulate, and it is the only style file a session edits. Sessions
read `STYLE.md` and this file together.

PROVENANCE. This book was translated (B01-B13, complete) against a standalone
STYLE.md that was itself the parent of the shelf's `styles/` layers, so the
composed contract restates the doctrine the book was drafted under; nothing in
the base + lang-zh + genre-nonfiction layers is new to this book. What IS new
is the REGISTER REBASELINE section below, adopted at the commissioner's
direction from the shelf's later register review of a sibling book, as the
target for this book's whole-book voice/register revision pass
(`REVISION_PLAN.md`). The pre-compose standalone STYLE.md is in git history
(commit edc98bf) if a rule's original wording is ever needed.

Tag every rule:
- `#book` — specific to this title. Stays here forever.
- `#promote` — looks general. Candidate to lift into a `styles/` layer between
  books, once a second book corroborates it. See `styles/INDEX.md`.

(Obeys CLAUDE.md rule 6: no em dashes in this file's own prose except inside
quoted before/after examples.)

## Voice sharpening

Hao Zaijin is a 报告文学 insider-historian: he buttonholes the reader,
editorializes freely, admires his subjects, and tells an astonishing story he
spent decades collecting, in an oral, exclamatory, tour-guide register where
rhetorical questions and "aha" reveals do the lifting. The English target is a
first-rate writer of popular narrative history, lively but not loud: keep his
STANCE and HEAT (admiration, sardonic edge, genuine indignation in the
political asides) and his WARMTH toward the reader, carried in verbs, nouns,
and rhythm, never in exclamation marks and docent questions. The B01 voice
gate settled this as "loyalty to effect, not texture"; a first draft carrying
~100 exclamation marks across two chapters needed ~90 cut.

His signature devices, and the standing calls on each [#book]:
- **The datebook chronology** (ch01 walks Zhou Enlai's 1927 one dated entry at
  a time): KEEP the staccato; do not fuse entries into summary.
- **The one-line punch paragraph**: keep the isolation where it earns its
  place; the exclamation on it usually goes.
- **The extended metaphor strand** (secrets as buried treasure, the archive as
  a martial-arts manual, research as testing deep water): render concretely
  and consistently, but pull back rather than amplify; the preface's mining
  metaphor is overwrought even for Hao.
- **The inclusive "we"**: keep where he includes himself and the reader;
  re-voice plainer any line where the warmth curdles ("shall we take up the
  engineering of that cultural gene?" is faithful and fatal).
- **The anaphora chain** (有谁知道…有谁想到…, four in a row): thin to two, vary.

### DELIBERATE features to PRESERVE (a revision pass must not iron these out)
- **The partisan register is content** (interested-witness doctrine, in the
  genre layer): 我党 "our Party," 汉奸 "traitors," the author's scare quotes
  around “特务”/“抢救”, his verdicts and his silences. Corrections go in
  notes, never in his mouth. Do not launder, do not sharpen.
- **Quoted documents, telegrams, directives, slogans** (逼供信, 砸烂公检法,
  抢救失足者…): full formality, no contractions, shapes kept. They are
  evidence, not narration.
- **The anatomizing of 特务 itself** (ch01 opens by discussing the word AS a
  word; 特区/特务 pun in s9): the italic *tewu* mentions stay visible; the
  use-vs-mention boundary stands.
- **对仗 set-pieces** where the figure lands ("the gun" and "the knife";
  化敌为友，化友为我 "turn enemies into friends, and friends into our own").
- **Verse blocks (`{p}`), datelines, asterisms**, and each chapter's
  **Principal Sources** register (a source list reads as a source list).
- **Deliberately formal speakers** (Mao pronouncing, Kang Sheng orating, an
  interrogator reading charges) per the HANDOFF voice sheets; and the 101-name
  ch12 roster and all unit designations (第37军 class), which are load-bearing
  and crop-verified, not prose to re-voice.
- **All 251 note anchors and 182 figure `before` anchors** are verbatim
  substrings of the prose. Any edit that touches one must move it in the same
  pass (`scripts/anchor_check.py` before applying; the builder's refusal is
  the backstop).

## ★ THE REGISTER REBASELINE (adopted for the revision pass) ★

Adopted at the commissioner's direction from the shelf's register review of a
sibling book (its STYLE.local, "THE REGISTER REBASELINE," B09), adapted to
this book's measured state. It resets the DEFAULT register: **modern-neutral
for everything, narration included. Period flavour comes from the CONTENT
(the offices, campaigns, silver dollars, security organs), never from antique
SYNTAX.** Wakeman writes these same decades in wholly contemporary prose and
loses nothing.

Three voices, three registers, and the line between them is bright:
- **Documents sound like documents.** Quoted communiqués, resolutions,
  telegrams, formal Party language stay starchy. That is period work.
- **The narrator sounds like a smart writer today**, explaining this history
  to an intelligent friend who is not in the field.
- **People sound like people.** Speakers in scenes talk plainly; the author's
  2000s interviewees (the old cadres he visits) talk like people on camera,
  contractions and all, unless a voice sheet marks them formal.

**THE READ-ALOUD TEST (the tiebreaker for every edit).** Say it aloud. If you
can hear a PBS costume-drama butler, rewrite it. If you can hear yourself
saying it to a smart friend, it is done.

What this book already gets right, measured at adoption (keep the batteries
running as regression guards, but expect near-zero hits): antique function
words (9 hits in 212k words), archaic quote tags (0), 即/也就是 pivots (1),
day-month dates (0), British spellings (0), "in the end" interrogatives (3).
The rebaseline work in THIS book is the rules below.

### RULE. Contractions in dialogue and interview speech; and sparingly in narration. [#promote, adopted]
- **WHY.** The book is nearly contraction-free end to end (0.2/1k overall;
  whole chapters at 0.0). Quoted speech and the 2000s interviewees sound like
  the narrator, and the narrator sounds like a deposition. This is the single
  largest source of starch remaining.
- **FIX.** Dialogue and interviewees contract freely where the speaker is not
  formal by design. Narration contracts ~10-15% of its negated auxiliaries,
  by ear ("he didn't dare" beside "he did not dare"). Quoted documents,
  slogans, and formal-by-design speakers contract NOT AT ALL.
- **CHECK.** `check_register.py --ref out/ch01_reading.md` (informational;
  the dialogue metric is noisy in low-speech units, judge those on narration
  by ear). Per narration paragraph with three-plus negated auxiliaries,
  contract one or two.

### RULE. Ration the authorial reveal-bang; the fact lands with a period. [#book]
- **WHY.** 141 exclamation marks book-wide, 64 of them in ch09 alone, most on
  narration reveals ("At least half of the outside intellectuals were sent in
  by the Nationalists!"). The B01 rationing held early but slipped in the
  hottest chapters.
- **FIX.** Keep exclamations inside quoted speech and slogans, and the rare
  genuine authorial outburst (at most one every few pages). Everything else:
  period. The Rescue Campaign's horror lands harder plain.
- **CHECK.** `register_tics.sh` narration-exclamation battery; ch09 is the
  test case.
- **CAUTION.** The author's raised voice is his signature; this is rationing,
  not flattening. Keep the strongest one per stretch.

### RULE. Convert most self-answering rhetorical questions to declaratives. [#book]
- **WHY.** 234 question marks book-wide; a good share are the docent's 呢?/
  岂不…? pivot, not real questions. (Interrogation scenes' real questions are
  real; leave them.)
- **FIX.** Keep one or two per chapter where the question genuinely lands;
  state the rest.
- **CHECK.** Read every narration "?" aloud: is anyone actually asking?

### RULE. Kill inversions and fronted objects; zero survivors in narration. [#promote, adopted]
- **WHY.** The single loudest "old book" signal ("His guilty scheme X saw
  through at a glance"). Calibration found none glaring, but the blind
  critique hunts what greps cannot.
- **FIX.** Subject-verb-object. "Rarest of all, ..." not "Most rare and
  precious of all: ...".
- **CHECK.** Blind critique + read openings aloud.

### RULE. De-nominalize "the [gerund/-ment] of the": convert about two-thirds to finite verbs. [#promote, adopted]
- **WHY.** 114 hits book-wide (ch09 15, ch10 16). Strung together they make
  the committee-minutes trudge.
- **FIX.** "The cracking of the false stone case caused a stir" &rarr;
  "Cracking the false stone case caused a stir." IDIOMATIC ones stay ("the
  founding of the People's Republic").
- **CHECK.** `register_tics.sh` nominalization battery; convert by ear, not
  by count.

### RULE. Collapse doubled synonyms to the stronger word; keep only real distinctions. [#promote, adopted]
- **WHY.** 并列 pairs (巩固和发展, 搜捕和屠杀) read as padding in English;
  Chinese rhythm is bisyllabic balance, English rhythm is stress variation,
  so the rendered doublet costs rhythm instead of adding it. The highest
  flow-per-keystroke edit on the sibling book's list.
- **FIX.** "threats and inducements" &rarr; "coercion" (unless both nodes
  genuinely differ). Never repeat a word to mirror parallelism.
- **CHECK.** Grep "X and Y" near-synonym pairs per unit; collapse ~2/3.

### RULE. Vary or cut "and the rest / and the others" for 等. [#promote, adopted]
- **WHY.** 31 hits; ch01 carries 11. The same tag every time is a tic.
- **FIX.** "among others," restructure, or cut where the list is complete.
- **CHECK.** Battery; more than a handful per unit means thin and vary.

### RULE. Plain the archaic "could only / could not but / cannot help" class. [#promote, adopted]
- **WHY.** 只能/不得不/不禁 carried literally; 26 hits. Many are idiomatic
  ("could come only through the ports" is fine); the archaic ones are not.
- **FIX.** "could only fall back on heavy-handed means" &rarr; "had to fall
  back on heavy-handed means"; "we cannot help asking" &rarr; ask the
  question, or "it is worth asking."
- **CHECK.** Battery; judge each hit aloud.

### RULE. Narration ellipses close; quoted speech that truncates keeps them. [#promote, adopted]
- **WHY.** Trailing ...... is Chinese atmospheric convention; in English
  narration it reads as pulp. 16 narration-side candidates.
- **FIX.** End the sentence with a period, or complete it.
- **CHECK.** Battery (the pattern excludes quote-adjacent hits).

### RULE. Long sentences split by the SPINE TEST, not word count. [#promote, adopted]
- **WHY.** Load, not length: how many finite spines must the reader track,
  and where does the main verb land? One spine reads fine at any length; a
  second whole biography between subject and verb does not. Only 19 narration
  sentences run over 90 words in this book; most will pass.
- **FIX.** Any appositive over ~15 words becomes its own sentence; the main
  verb arrives within the first ~20 words; over three coordinated predicates,
  split. Colon-plus-list sentences are EXEMPT at any length (the pile-up IS
  the effect; never break a list). Quoted documents are EXEMPT.
- **CHECK.** Battery lists the >90-word sentences; count spines per hit.

### RULE. Front-load attribution when a quote shifts tense or person; vary quote tags. [#promote, adopted]
- **WHY.** A quote that opens cold in another tense reads as an error until
  the trailing citation lands. Same-tag repetition ("later recalled" every
  time) is a tic.
- **FIX.** "As Zhou Enlai reported in 1929: ..."; vary "later recalled,"
  "said in a 2007 interview," "wrote decades later," plain "said."
- **CHECK.** Any quote whose first words shift tense/person needs a lead-in.

### RULE. Chengyu triage, three bins, applied wherever the pass touches one. [#promote, adopted]
- **BINS.** (1) Self-evident image: keep literal ("kill the chicken to warn
  the monkey"). (2) Load-bearing but opaque: keep and footnote. (3) No
  parsable image: silently naturalize to the sense (魂飞魄散 "scared out of
  her wits"). A raw bin-3 calque must not stand in the body.
- **CHECK.** For each idiom the pass meets, name its bin before editing.

### Apparatus mechanics (adopted; run as checks in the final batch) [#promote, adopted]
- **One note = one referent**; a bundled note splits, or its marker moves to
  the end of the list it serves.
- **Markers sit at sentence end or the end of the clause holding the
  referent**, never mid-phrase; anchors move with them in the same pass.
- **One gloss mechanism per term** (inline under ~8 words and needed to
  parse; footnote for context; glossary for recurring furniture), one gloss
  per term book-wide.
- **Density balance**: words-per-note per chapter should not swing more than
  ~2-3x across the book (ch08 at 8 notes / 182 paragraphs vs ch02 at 36 is
  the pair to eyeball).
- **CHECK.** R04 (final batch) runs these as a sweep; they are not per-unit
  work.

## Calibration baseline (measured 2026-08-22, pre-pass; the state to improve)

212k words, 14 units. Contractions 0.2/1k overall (dialogue-bearing units:
ch02 0.4/1k STILTED vs ch01 ref 2.0/1k; ch04/ch08/ch11/ch12/ch13 at 0.0).
Exclamations 141 (ch09 64, ch06/ch07/ch08 ~29, ch10 20, ch01 15); question
marks 234; nominalizations 114; "and the rest/others" 31; could-only class
26; narration-ellipsis candidates 16; >90-word sentences 19; antique
function words 9; pivots 1; "in the end?" 3; DMY dates 0; British spellings
0; archaic quote tags 0. Full per-unit table in REVISION_PLAN.md §3.

## Decided renderings (this book's word-level ledger)

The full term ledger is `glossary.json` (284 rows) + `out/term_ledger.md`;
`authority.json` binds the shelf. Function-word and diction decisions that
recur in revision:

- 侦察 in the domestic-security context &rarr; **investigation /
  surveillance / counter-surveillance**; "reconnaissance" only for genuine
  military/technical work (the army 二部, 技术侦察 SIGINT).
- Organization handles, one each, forever: **the Special Branch** (中央特科),
  **the Social Affairs Department** (中社部 after first gloss), **Juntong**,
  **Zhongtong**, **the Border Security** (边保), **the Eighth Route offices**
  (八办). Never alternate translation and transliteration.
- 特务 as a word under discussion &rarr; italic ***tewu*** with gloss; in
  plain use &rarr; the decided rendering ("agent," "special services" by
  context). The 特区/特务 pun gets its note, not a strained English pun.
- Famous lines use canonical English: "Political power grows out of the
  barrel of a gun"; Sun Tzu's "to subdue the enemy without fighting."
- Nicknames translate when the meaning is the point (董胖子 "Fatty Dong");
  a nom de guerre that is effectively a name stays pinyin; per-name in
  glossary.json.
- Count-units resolve fully (30万 = 300,000); vagueness stays vague (多时 =
  "a good while"); military designations in digits ("the 37th Army").
- Translator-added scare quotes: budget zero. The author's own stay.
- American spelling and idiom throughout (626 curated hits, 0 British, at
  reconciliation; keep it so).
