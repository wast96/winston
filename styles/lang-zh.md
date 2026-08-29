<!-- VOICE_TARGET is set by the genre layer, not here. -->
# STYLE delta — Chinese source (lang-zh)

Language layer for a Chinese source text. Composes onto `_base.md`. Supplies
the Chinese-specific stilted tells, a calque sweep to grep every batch, the
em-dash budget, and the romanization convention. The genre layer (fiction or
nonfiction) is separate.

(Obeys CLAUDE.md rule 6: no em dashes in this sheet's prose except inside
quoted examples.)

## Chinese-specific failure modes (add to the six in _base)

7. **The 的-string / stacked pre-noun modifier.** Chinese piles modifiers before
   the noun with 的; traced literally it becomes a long adjective train or an
   "of ... of ..." chain. Unstack: head noun first, modifiers following as
   clauses or after the noun. The nominal special case: 的-phrases and verbal
   nouns tempt "the [gerund] of the [noun]" ("the scattering of exposed
   cadres, the safeguarding of the Center's organs"); each forces an "of," and
   strung together they make the committee-minutes trudge. Convert roughly
   two-thirds to finite verbs ("scattering cadres who had been exposed,
   safeguarding the Center's organs"); LEAVE the genuinely idiomatic set ("the
   founding of the People's Republic," "the killing of these men"). Convert by
   the read-aloud test, not by count.
   <!-- de-nominalization: promoted v2.3, the-sword-roars (B09) +
        chinas-secret-war (adopted, 114 hits measured) + zhou-enlai (42) -->
8. **Topic-comment fronting as "As for ...".** Chinese fronts the topic
   (关于…方面, 在…上). Do not calque it as "As for X, ..."; fold the topic into
   the subject and let the sentence move.
9. **The 被-passive and 使-causative.** 被捕 invites "was arrested by"; 使…得以
   invites "made it so that." Prefer an active agent and a transitive verb where
   English would use one. (Keep the passive where the agent is genuinely unknown
   or beside the point.)
10. **Aspect over-marking.** 了 / 过 / 已经 traced across every clause pile up as
    "already," "had ...ed," "went on to." English carries sequence with the
    plain past; use the perfect only where the time relation actually needs it.
11. **并列 doubled pairs.** Chinese pairs near-synonyms freely (巩固和发展,
    搜捕和屠杀, 侦察监视). Carried into English as a matched pair it reads as
    padding. Take the one strongest word, or draw the real distinction if there
    is one. Never repeat a word to mirror the source's parallelism (到处…到处
    becomes "everywhere," used once).
12. **Empty connective padding.** 所以说, 可以说, 这样一来, 换句话说 often add
    nothing. Cut them and let the fact stand.
13. **成语 transplanted as a picture.** Translate the four-character idiom for
    EFFECT, by sorting every idiom into one of three bins BEFORE rendering:
    <!-- three-bin triage: promoted v2.3, the-sword-roars (chengyu triage) +
         chinas-secret-war (adopted) + chen-yangshan (idiom ruling) +
         on-a-hair-trigger (T1 class of its register pass) -->
    1. **Self-evident from the image: keep it literal.** "Kill the chicken to
       warn the monkey," "the cliff's edge," "the tiger's mouth." The English
       picture carries the sense on its own.
    2. **Culturally load-bearing but opaque: keep it and FOOTNOTE.** 瓜田李下
       ("keeps clear of the melon patch and the plum tree"), 近水楼台. The
       image matters; the reader needs the note.
    3. **No image an English reader can parse: silently naturalize to the
       sense.** 臭不可闻 is "stank to high heaven," not "so smelly it could not
       be smelled"; 鹤立鸡群 is "stood out"; 魂飞魄散 is "scared out of her
       wits"; 竹篮打水 is "all for nothing." A raw bin-3 calque must never
       reach the body; transplanting the picture where it does not land IS the
       chinoiserie effect. When the source stacks several chengyu in one
       sentence, keep at most the one that lands and naturalize the rest.
    A bare one-clause "quoted-proverb" sentence dropped between two narrative
    sentences is the tell that a calque got through; an idiom that is ONLY an
    idiom needs folding into the surrounding sentence or an English frame ("as
    the old saying runs, ...").
14. **对仗 / balanced antithesis.** The source loves balanced phrases
    (枪杆子…刀把子, 一明一暗, 化敌为友、化友为我). Two failure modes, both
    directions: do not trace the parallel into wooden English, and do not
    dissolve it into flat prose when it is doing real rhetorical work. Find the
    English figure that lands the same punch ("turn enemies into friends, and
    friends into our own"); when the figure cannot survive, render the sense and
    footnote the lost image if it matters.
15. **The interiority calque.** Chinese marks an inner state with an organ:
    心里想 / 心中 ("thought in his heart"), 打心眼里, and the doubled "feel a
    feeling" shape. Rendered literally it becomes "he thought in his heart,"
    "felt a feeling of sorrow," "deep in his heart." English carries interiority
    in the verb: "he thought," "he grieved." Strip the organ and the doubled
    "feel a feeling"; keep the body only where the scene makes it literal.

## The calque sweep (grep these every batch)
Word-for-word carries of specific Chinese constructions. Each is a find-and-fix.
- **亲自 / 亲手 ("in person" / "with his own hand(s)").** Chinese flags personal
  agency far more often than English wants it. Usually drop the tag: "Zhou built
  the radio network," not "built it with his own hands."
- **上 / 中 / 下旬 (thirds of a month).** Never "the first ten days of October."
  Use "early October," "mid-October," "late October."
- **以上 / 多 and litotes counting.** "over 40,000 troops," not "more than forty
  thousand men and guns" (人枪 is not "men and guns" in English); do not stack
  four "more than"s in one sentence; 不少 is "a good deal of," not "no small
  amount of."
- **之至 / 极 ("of the very highest").** Recast: "exceptional," "considerable,"
  or restructure. Not "were of the very highest."
- **确实 as a trailing "indeed."** Cut most.
- **等 / 等人 after a name-list as the same tag every time.** "and the rest" /
  "and the others" dozens of times per book is a tic (62 hits on one book, 87
  on another). Vary ("among others"), restructure, or cut where the list is
  complete or the tag re-lists names just given. Target: no single tag
  dominating a unit, NOT zero. Leave a tag that sits inside a note anchor
  alone; do not restructure anchored text for a tic.
  <!-- promoted v2.3: the-sword-roars + chinas-secret-war + chen-yangshan +
       zhou-enlai (all measured) -->
- **纷纷 / 先后 / 相继 / 陆续 as "one after another" every time.** Vary by
  sense: "in turn," "one by one," "in succession," "a few at a time," or cut.
  Keep one instance where it reads best.
  <!-- promoted v2.3: the-sword-roars + zhou-enlai (31 hits measured) -->
- **到底 / 究竟 as "in the end" inside a question.** Native English does not
  use "in the end" as an interrogative intensifier ("Did he, in the end,
  perform magic or not?"). Use "actually" / "really," recast ("So did he or
  didn't he?"), or cut. Narrative "in the end" meaning "ultimately" is fine;
  only the interrogative use is the calque.
  <!-- promoted v2.3: the-sword-roars + chinas-secret-war -->
- **只能 / 不得不 / 不禁 / 不能不 as "could only / could not but / could not
  help."** Part of the antique default (_base kill list). "He could only come
  without a shadow and go without a trace" becomes "He had to move without a
  trace"; "we cannot help asking" becomes "it is worth asking," or just ask
  the question; 不禁 is often simply cut. Idiomatic hits ("could only watch")
  stay.
  <!-- promoted v2.3: the-sword-roars + chinas-secret-war + zhou-enlai -->
- **Bare transliterations and coinages.** 工作网 is "network," not "work net";
  gloss anything a reader cannot picture (马兰纸 "malan-grass paper";
  顺风耳 "downwind ear" wants a gloss even inside a quote).
- **侦察 for a DOMESTIC political-security organ** reads as military scouting.
  Prefer "investigation" / "surveillance" / "counter-surveillance" for the
  security bureaus; keep "reconnaissance" only for genuine military or technical
  reconnaissance. A global decision, applied by context.
- **Collocation calques generally.** A word rendered by its dictionary gloss,
  not the word an English writer reaches for: 破坏 (of the enemy) is "sabotage,"
  not "wrecking"; 心血 is "heart and soul," not "heart's blood"; 半个月 is "two
  weeks," not "half a month"; 打入 is "plant inside / infiltrate," not "drive
  into"; a killing verb (制裁 / 镇压 of a person, 处决, 除掉) is "eliminate /
  execute / kill," never the soft "put down" or "dealt with." Test every content
  word: is this the word a good English writer would use here, or the gloss of
  the Chinese?

## Em-dash budget
At most ONE em dash per sentence, or one matched pair bracketing an aside; never
a pile-up. The source's own —— marks emphatic breaks and the chapter-subtitle
dash; render the sense, do not import a Chinese dash count. When a sentence
would exceed the budget, swap a dash for a semicolon (a balanced second clause),
a comma (a light aside), or a period (split it). `check_register.py --ref`
tracks the em-dash rate against the frozen reference; a jump is a flag to look.

## Source punctuation: render the FUNCTION, not the shape
<!-- promoted v2.3: zhou-enlai (voice-gate ruling 8) + the-sword-roars +
     chinas-secret-war (narration-ellipsis rule, both adopted) -->
- **Trailing ...... in narration.** The source's six-dot ellipsis is an
  atmospheric convention; carried into English narration it reads as pulp
  ("the fellow screamed and let go..."). Close the sentence with a period, or
  complete it. Keep "..." only inside a quotation whose speaker or text
  genuinely breaks off.
- **。…… (full stop plus ellipsis) marking an abridged litany or quotation.**
  In running narrative, cut it; in a quotation, close on a single trailing
  ellipsis.

## Romanization and units
- **Pinyin**, one rendering per referent, decided in `glossary.json` and checked
  against `authority.json` before anything is romanized; conventional English
  forms where established (Chiang Kai-shek, Sun Yat-sen, the Kuomintang, the
  Yangtze). The shelf has already agreed some pulls: 广州 is Guangzhou, not
  Canton (authority.json, multiple books). Follow the ledger, not habit, when
  the two disagree; period flavour can still justify Canton in a fixed phrase if
  the glossary decides so at first use.
- Many figures carry an alias (王庸 = Chen Geng, 伍豪 = Zhou Enlai). Give an
  alias its owner's name or a clarifying tag on first use in a scene so the
  reader never loses the thread; pronoun fog in arrest and chase scenes is a
  real risk in this material.
- Keep period money and measures (silver dollars, li) with a first-use gloss;
  a Chinese count-unit resolves to its full value (30万 is 300,000, never
  "30 wan").

## Proofread every hanzi you insert
Proofread every Chinese character you put into a note or gloss, character by
character, against the glossary or the scan. Two glosses once shipped wrong
characters (谊 for 谋, 闽 for 闸) because the romanization was right but the
inserted character was not, and an English-only read cannot catch that. Never
trust your own character insertion; verify it.
