# ch02 revision edits (R1 exemplar) — TIER 1+2, mechanical/tic only

Applied with `python3 scripts/apply_edits.py ch02`. Every OLD occurs exactly
once; every edit is a single-word or phrase substitution that cannot move a
paragraph boundary (parity invariant by construction). No numeral changes.
Note-body date reformats are handled separately in notes.json (apply_edits
cannot edit a note body); see PROGRESS.md.

## TIER 1 — Politburo (政治局 -> "the Politburo", never "Political Bureau")

### p006 T1 TOUCH
OLD: The provisional Central Political Bureau, headed by Qu Qiubai
NEW: The provisional Central Politburo, headed by Qu Qiubai
WHY: 政治局 = Politburo (shelf canon); "Political Bureau" is a bare calque.

### p007 T1 TOUCH
OLD: the provisional Political Bureau decided to move the central organs
NEW: the provisional Politburo decided to move the central organs
WHY: 政治局 = Politburo.

### p009 T1 TOUCH
OLD: the members of the provisional Political Bureau who came back from Wuhan
NEW: the members of the provisional Politburo who came back from Wuhan
WHY: 政治局 = Politburo.

### p010a T1 TOUCH
OLD: one of the alternate members of the provisional Political Bureau. He came back
NEW: one of the alternate members of the provisional Politburo. He came back
WHY: 政治局 = Politburo.

### p010b T1 TOUCH
OLD: made a member of the provisional Political Bureau Standing Committee
NEW: made a member of the provisional Politburo Standing Committee
WHY: 政治局常委 = Politburo Standing Committee.

### p018 T1 TOUCH
OLD: where the Political Bureau met and worked
NEW: where the Politburo met and worked
WHY: 政治局 = Politburo.

### p019 T1 TOUCH
OLD: the place served the Political Bureau as a spot to meet
NEW: the place served the Politburo as a spot to meet
WHY: 政治局 = Politburo.

### p090 T1 TOUCH
OLD: the attempt to rescue Political Bureau member Peng Pai
NEW: the attempt to rescue Politburo member Peng Pai
WHY: 政治局委员 = Politburo member.

### p092 T1 TOUCH
OLD: Ren Bishi, a member of the Central Political Bureau, went to Jingye Lane
NEW: Ren Bishi, a member of the Central Politburo, went to Jingye Lane
WHY: 中央政治局 = Central Politburo.

### p190a T1 TOUCH
OLD: the provisional Central Political Bureau, he was made a member of the Political Bureau and director
NEW: the provisional Central Politburo, he was made a member of the Politburo and director
WHY: 政治局 = Politburo (both occurrences in this clause).

## TIER 1 — White Terror (白色恐怖 -> "the White Terror", the specific KMT terror)

### p003 T1 TOUCH
OLD: the teeth of the white terror
NEW: the teeth of the White Terror
WHY: 白色恐怖, the specific post-1927 terror; definite, not generic.

### p008 T1 TOUCH
OLD: where the white terror held sway
NEW: where the White Terror held sway
WHY: 白色恐怖, specific.

### p010w T1 TOUCH
OLD: the shadow of the white terror
NEW: the shadow of the White Terror
WHY: 白色恐怖, specific.

### p150 T1 TOUCH
OLD: the white terror hanging over the whole city
NEW: the White Terror hanging over the whole city
WHY: 白色恐怖 in Tianjin; the same named terror, definite.

### p186 T1 TOUCH
OLD: under the white terror it did much
NEW: under the White Terror it did much
WHY: 白色恐怖, specific.

### p272 T1 TOUCH
OLD: under the white terror in Shanghai
NEW: under the White Terror in Shanghai
WHY: 白色恐怖, specific.

### p292 T1 TOUCH
OLD: The white terror was exceptionally cruel
NEW: The White Terror was exceptionally cruel
WHY: 白色恐怖 in Chongqing; the same named terror, definite.

## TIER 1 — litotes / stiff auxiliaries

### p054 T1 TOUCH
OLD: and he could not help asking:
NEW: and he couldn't help asking:
WHY: prescribed plain equivalent for the "could not help" formula (tier-1 only,
     not the declined tier-3 narration-contraction program).

### p306 T2 TOUCH
OLD: found in it no small convenience and good cover
NEW: found it a great convenience and good cover
WHY: 不少方便; "no small convenience" is a litotes calque -> state positively.
     (KEEP ch02:115 "no small contribution": inside Chen Geng's {v} letter.)

## TIER 2 — nominalization to finite verb

### p058 T2 TOUCH
OLD: would that not be exactly the drawing of a double agent out of the enemy's camp?
NEW: would that not be exactly drawing a double agent out of the enemy's camp?
WHY: awkward "the X-ing of" nominalization -> finite verb.

## TIER 2 — "one after another" varied (keeps ch02:293 as the retained instance)

### p005 T2 TOUCH
OLD: betrayed the revolution one after the other
NEW: betrayed the revolution in turn
WHY: 先后; vary the recurring "one after another" tag.

### p109 T2 TOUCH
OLD: and the rest had one after another left Shanghai, some for Tianjin
NEW: and the rest had left Shanghai one by one, some for Tianjin
WHY: 先后; vary (keeps the trailing "and the rest").

### p269 T2 TOUCH
OLD: stole a dozen-odd gold bars from his aunt's house one after another
NEW: stole a dozen-odd gold bars from his aunt's house, a few at a time
WHY: 陆续; vary to the by-sense equivalent.

## TIER 2 — 等-tags thinned (surgical; anchored tags left in place)

### p020 T2 TOUCH
OLD: wed; Li Weihan, Deng Xiaoping, and the rest all warmly agreed
NEW: wed; the others all warmly agreed
WHY: cut the redundant re-listing (the same names were named a clause earlier
     in the banquet sentence, which carries a note anchor and is untouched).

### p036 T2 TOUCH
OLD: Chen Lifu, Zhang Daofan, Yang Jianhong, and others set about building a detective apparatus
NEW: Chen Lifu, Zhang Daofan, Yang Jianhong, among others, set about building a detective apparatus
WHY: vary the dominant "and others" tag with "among others". Tag varied AFTER
     the names only, so the figure `before` anchor "That March, Chen Lifu, Zhang
     Daofan, Yang Jianhong" (first ~80 chars of the para) stays intact.

### p297 T2 TOUCH
OLD: the disaffected warlords and politicians of Sichuan and Guizhou, and so on
NEW: the disaffected warlords and politicians of Sichuan and Guizhou
WHY: "and so on" is redundant after the opener "many connections ... that could
     be used"; cut where the list is plainly illustrative.
