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
   clauses or after the noun.
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
    EFFECT. Keep the vivid literal image only where it lands in English ("kill
    the chicken to warn the monkey" works); use the natural English idiom where
    the image would not (臭不可闻 is "stank to high heaven," not "so smelly it
    could not be smelled"; 鹤立鸡群 is "stood out," not "stood out like a crane
    among chickens"). Footnote the ones whose flavour survives neither way.
    Transplanting the picture where it does not land IS the chinoiserie effect;
    avoid it.
14. **对仗 / balanced antithesis.** The source loves balanced phrases
    (枪杆子…刀把子, 一明一暗, 化敌为友、化友为我). Two failure modes, both
    directions: do not trace the parallel into wooden English, and do not
    dissolve it into flat prose when it is doing real rhetorical work. Find the
    English figure that lands the same punch ("turn enemies into friends, and
    friends into our own"); when the figure cannot survive, render the sense and
    footnote the lost image if it matters.

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
