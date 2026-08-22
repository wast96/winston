# ch04 revision edits (R2 sweep) — TIER 1+2, mechanical/tic only

Applied with `python3 scripts/apply_edits.py ch04`. Every OLD occurs exactly
once; every edit is a single-word/phrase substitution or a phrase cut that cannot
move a paragraph boundary. No numeral changes (the cuts drop only the sequence
tag, never a count: "three intelligence stations", "a good many cadres", "more
than twenty connections" all keep their numbers). Note-body date reformats (7
D-Month-YYYY dates) are handled separately in notes.json. ch04 has NO 政治局 hits.
"Such was Chen Yangshan" (ch04:109) PASSES the read-aloud test as a deliberate
summation after a quoted maxim and is LEFT; "Such was the whole of ..." (ch04:151)
fails and is recast. ch04:18 "no small amount of work" is inside He Long's quoted
speech (KEPT per the litotes carve-out for quoted matter).

## TIER 1 — "could not but" formula -> plain equivalent

### p209a T1 TOUCH
OLD: could not but carry a certain risk
NEW: was bound to carry a certain risk
WHY: "could not but + verb" -> plain "was bound to".

## TIER 2 — litotes calque -> stated positively

### p138 T2 TOUCH
OLD: we gathered no little material
NEW: we gathered a good deal of material
WHY: 不少; "no little" litotes calque -> "a good deal of" (narration).

### p199 T2 TOUCH
OLD: his comrades and subordinates had no few legendary stories
NEW: his comrades and subordinates had a good many legendary stories
WHY: 不少; "no few" litotes calque -> "a good many". (The figure `before` anchor
     "In the years when Chen Yangshan headed the Jin-Sui Intelligence General
     Bureau" sits earlier in the paragraph and is untouched.)

## TIER 1 — "Such was" summary formula (recast the one that fails read-aloud)

### p151b T1 TOUCH
OLD: Such was the whole of Zhang He's first entry into Guisui
NEW: That was all that came of Zhang He's first entry into Guisui
WHY: "Such was the whole of ..." fails the read-aloud test (stiff/antique);
     recast to plain summation, colon-explanation following unchanged.

## TIER 2 — "one after another / one after the other" thinned (9 hits dominated
# the chapter; cut three redundant-with-a-count, vary three, keep three natural
# instances: ch04:64, ch04:151, ch04:170)

### p009 T2 TOUCH
OLD: sent a good many cadres down to posts at the base level one after another
NEW: sent a good many cadres down to posts at the base level
WHY: "one after another" redundant after "a good many cadres ... down to posts"; cut.

### p011 T2 TOUCH
OLD: set up three intelligence stations one after another: the Hexi station
NEW: set up three intelligence stations: the Hexi station
WHY: "one after another" redundant after the explicit count "three ... stations"; cut.

### p160 T2 TOUCH
OLD: got inside the enemy and puppet apparatus one after the other
NEW: got inside the enemy and puppet apparatus in turn
WHY: vary; two men entering successively read as "in turn".

### p166 T2 TOUCH
OLD: obtained, one after another, the cipher
NEW: obtained, in succession, the cipher
WHY: vary the recurring tag ("in succession" for items obtained over time).

### p196 T2 TOUCH
OLD: In this period they developed, one after another, more than twenty connections
NEW: In this period they developed more than twenty connections
WHY: "one after another" redundant after "more than twenty connections"; cut
     (the count is untouched).

### p209b T2 TOUCH
OLD: the parcels did indeed arrive, one after another
NEW: the parcels did indeed arrive, a few at a time
WHY: 陆续; vary to the by-sense equivalent (parcels arriving in batches).
