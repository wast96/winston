# STYLE, Burn, O Sword! house style sheet

Standing style rules for this translation, seeded by corrections the
commissioner made at the ch01 voice gate and added to as the book proceeds.
Read it at the start of every batch, alongside CLAUDE.md and HANDOFF.md. Each
rule records the correction, WHY the error happened, and the fix, so the
reasoning travels with the rule. A single correction is a data point; the rule
that prevents the whole class is the deliverable.

(This sheet obeys CLAUDE.md rule 6 in its own prose: no em dashes here, except
inside the quoted examples, which necessarily show them.)

## 1. Em dashes: one per sentence, or one matched pair. Never a pile-up.

RULE. A sentence carries at most ONE em dash, OR one matched PAIR of em dashes
used as parenthetical brackets around an interjection. Never three in a
sentence. Never combine an em dash inside a clause with a second em dash at a
quote or attribution seam in the same sentence. When a sentence would exceed
the budget, swap one dash for:
- a semicolon, when the second half is a balanced independent clause;
- an ellipsis, for a hesitation, a shocked pause, or a trailing-off;
- a comma, for a light aside;
- a period, to split the sentence.

WHY IT HAPPENED. Japanese leans on the quotative particle と and on structural
punctuation (、。「」（）). Rendering clause by clause, the em dash became the
default English connector for every pause, aside, interruption, and
と-attribution, so dashes accreted. The `{j}` display-join then stitched two
source lines into one sentence, concentrating a clause dash and an
attribution-seam dash together, which is where the pile-ups showed up.

EXAMPLES from ch01 (before, then after):
- "(...come from Edo—that would do.)—and Toshizō walked..."
  becomes "(...come from Edo; that would do.)—and Toshizō walked..."
  (a semicolon inside the aside; one seam dash is left).
- "and then—\"You—with this person?\"—made a show of astonishment."
  becomes "and then—\"You... with this person?\"—made a show of astonishment."
  (an ellipsis for the shocked pause; the bracketing pair around the quote is
  a legitimate matched pair and stays).

LEFT STANDING at the gate (one dash each, so within budget):
"(A woman is her rank.)—so he believed." and
"(This is not it.)—for she was not the girl he had imagined."

CHECK. After applying the `{j}` joins, scan each display paragraph for any
sentence with two or more em dashes and thin it. `check_register.py --ref`
tracks the em-dash rate against the frozen ch01 reference; a jump is a flag to
go look.

## 2. Idioms and phrasal verbs: no scene-primed second meaning.

RULE. Before using an idiom or phrasal verb, test it against the immediate
scene. If the setting activates a different literal sense of the phrase, choose
a single-sense wording instead. This matters most in terse interior thoughts,
which lack the surrounding words that would otherwise disambiguate.

WHY IT HAPPENED. For （わからぬ）, Toshizō's blunt "I do not understand / I
cannot figure her out," the draft read "(I cannot make her out.)". But the
scene is pitch dark (the festival lanterns are all out), and darkness primes
the VISUAL sense of "make out," so the line read as being about eyesight
("I cannot see her") rather than comprehension.

FIX. "(I cannot make her out.)" becomes "(I can't make sense of her.)". Render
わからぬ / わからない as "do not understand" or "cannot make sense of," never
"make out."

WATCH LIST (phrasal verbs whose second sense a scene can supply): "make out"
(see / understand) in darkness; "take in" (grasp / inhale) around breath, smoke,
or scent; "lost" (bewildered / asleep / dead) around sleep or death; "come" and
"take" in the erotic scenes; "strike" (hit / occur to) in a fight. When two
senses are both live, pick the wording that leaves only one.

## How to add to this sheet

When the commissioner corrects a line, record the CLASS of error here, not just
the one fix: the before and after, why it happened, and the rule that prevents
the whole class next time.
