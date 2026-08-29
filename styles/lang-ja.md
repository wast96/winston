# STYLE delta — Japanese source (lang-ja)

Language layer for a Japanese source text. Composes onto `_base.md`. Supplies
the Japanese-specific stilted tells, the em-dash budget, tense handling, and
the romanization convention. The genre layer (fiction or nonfiction) is
separate.

(Obeys CLAUDE.md rule 6: no em dashes in this sheet's prose except inside
quoted examples.)

## Japanese-specific failure modes (add to the six in _base)

7. **The quotative-と dash accretion.** Japanese leans on the quotative particle
   と and on structural punctuation (、。「」（）). Rendered clause by clause,
   the em dash becomes the default English connector for every pause, aside,
   interruption, and と-attribution, so dashes accrete. A display-join that
   stitches two source lines into one sentence then concentrates a clause dash
   and an attribution-seam dash together, which is where pile-ups show up. See
   the em-dash budget below.
8. **The bare romaji common noun.** Do not leave a culturally specific common
   noun untranslated where English has the word or a gloss will serve: "the
   liturgical chant," not "the *shōmyō* chant." Footnote a term of art like
   *gatha* at first use. Keep romaji only for names and for culturally specific
   terms that carry a note (rappa, shinobi, koku).
9. **The disembodied-body-part calque.** Japanese lets a mouth, teeth, or hand
   perform a human act on its own. Recast so the person is the agent: "He had
   the toothy grin of an old ape," not "The teeth grinned like an old ape's."
   (Genuinely idiomatic English like "her eyes smiled" is fine; the target is
   the calque.)
10. **The stiff stative rendered flat.** Unpack a stative Japanese construction
    into a felt, physical one: "as he understood the old man meant kindly, the
    tension seemed suddenly to leave him," not "all at once at ease once he saw
    the old man meant kindly" (which also stutters *at once ... once*). Watch
    for and kill that kind of accidental repetition.
11. **The interiority calque.** Japanese marks an inner state with an organ and
    a location: 心の中で ("within his heart"), 胸に ("in his chest"), and the
    "feel a feeling" shape 悲しみを感じた. Rendered literally it becomes "he
    thought in his heart," "felt a feeling of grief," "in the deep places of the
    heart." English carries interiority in the verb: "he thought," "he grieved,"
    "he was worn out." Strip the organ and the doubled "feel a feeling"; keep
    the physical body only where the scene makes it literal (a hand at the chest).

## Em-dash budget
At most ONE em dash per sentence, OR one matched PAIR used as parenthetical
brackets around an interjection. Never three in a sentence; never combine an em
dash inside a clause with a second at a quote or attribution seam in the same
sentence. When a sentence would exceed the budget, swap one dash for a
semicolon (a balanced second clause), an ellipsis (a hesitation or shocked
pause), a comma (a light aside), or a period (split it). After applying any
display-join, scan each display paragraph for two-or-more-dash sentences and
thin them. `check_register.py --ref` tracks the em-dash rate against the frozen
reference; a jump is a flag to go look.

## Tense: keep the author's own gnomic present
Where the author sets standing description or geography in a timeless present
("The sky over Iga rests on two ranges ... it is propped up by the peaks of
Kasagi"), leave it there. Do NOT mechanically convert scene-setting or
geographic asides to the narrative past. The mix of gnomic present (standing
geography) and past (the action, and habitual "the sun sank ... cloud
gathered") is deliberate and correct.

## Proofread every character you insert
Proofread every Japanese character (kanji or kana) you put into a note or
gloss, character by character, against the glossary or the source. The zh
layer carries this rule from two glosses that shipped wrong characters on a
real book: the romanization was right, the inserted character was not, and an
English-only read cannot catch that. The failure mode is identical in
Japanese. Never trust your own character insertion; verify it.

(The scene-primed second-meaning rule for idioms and phrasal verbs, learned on
a Japanese book, now lives in `_base.md`: the failure is English-side and
language-independent.)

## Romanization and units
- Japanese names in **Hepburn with macrons**; conventional English forms as
  established (Hideyoshi, Kyoto, Tokugawa, the era-names). One rendering per
  referent, decided in `glossary.json` against `authority.json`.
- **Keep the source's own units and proper nouns; do not domesticate them.**
  Japanese measures (<i>ri</i>, <i>chō</i>, <i>ken</i>, <i>shaku</i>,
  <i>sun</i>, <i>koku</i>, <i>kan</i>, <i>mon</i>) stay as they are, never
  converted to miles or inches; a footnote carries the equivalence at first
  use. The same for offices, arms, and place-names.
