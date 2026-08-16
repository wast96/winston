# ch01 register de-archaizing + date-consistency edits (B09 continuation)
# Applied via scripts/apply_edits.py ch01. English->English re-voicing of the
# gate-approved, B09-corrected text: every NEW preserves the propositional
# content of its OLD exactly (no fact/name/number/date-value change), only the
# register and the syntax. Dates: day-month -> month-day per the rebaseline
# (the ch01 sweep the B09 STATE claimed was NOT actually applied to these).

### p035 [T3] TOUCH  date day-month -> month-day
OLD: the report in the same paper on 1 December, do more than confirm
NEW: the report in the same paper on December 1, do more than confirm
WHY: 1 December -> December 1 (rebaseline: month-day-year everywhere).

### p131 [T3] TOUCH  diary dateline consistency
OLD: {d} 11 June
NEW: {d} June 11
WHY: diary's own first entry is "June 10, 1943"; the rest ran day-month.

### p147 [T3] TOUCH  diary dateline consistency
OLD: {d} 6 July
NEW: {d} July 6
WHY: match month-day of the diary's first dateline.

### p151 [T3] TOUCH  diary dateline consistency
OLD: {d} 11 July
NEW: {d} July 11
WHY: match month-day of the diary's first dateline.

### p155 [T3] TOUCH  diary dateline consistency
OLD: {d} 13 July
NEW: {d} July 13
WHY: match month-day of the diary's first dateline.

### p159 [T3] TOUCH  diary dateline consistency
OLD: {d} 16 July
NEW: {d} July 16
WHY: match month-day of the diary's first dateline.

### p195 [T3] TOUCH  date day-month -> month-day
OLD: moving the date from 12 November to 8 November.
NEW: moving the date from November 12 to November 8.
WHY: month-day-year everywhere (narration; the quoted "twelfth of November" stays).

### p227 [T3] TOUCH  date day-month -> month-day
OLD: On 9 October that year
NEW: On October 9 that year
WHY: month-day-year everywhere.

### p227 [T3] TOUCH  date day-month -> month-day
OLD: on the night of 10 October took
NEW: on the night of October 10 took
WHY: month-day-year everywhere.

### p301 [T3] TOUCH  date day-month -> month-day
OLD: On 28 May the Party Center
NEW: On May 28 the Party Center
WHY: month-day-year everywhere.

### p301 [T3] TOUCH  date day-month -> month-day
OLD: in the concessions on 30 May, against
NEW: in the concessions on May 30, against
WHY: month-day-year everywhere.

### p301 [T3] TOUCH  date day-month -> month-day
OLD: On 30 May, more than two thousand students
NEW: On May 30, more than two thousand students
WHY: month-day-year everywhere.

### p017 [T3] TOUCH  contraction in narration
OLD: left the stage for good, he still could not keep away.
NEW: left the stage for good, he still couldn't keep away.
WHY: rebaseline: contract ~10-15% of narration negatives by ear.

### p163 [T5] RECAST  modernize quote tag, drop em-dash pair
OLD: as Bo Yibo — who fought at his side in those days — disclosed many years later, was this:
NEW: as Bo Yibo, who fought at his side in those days, later disclosed, was this:
WHY: "disclosed many years later" tag archaism; also trims the em-dash pair to commas.

### p163 [T5] RECAST  rhetorical ceremony -> declaratives (keep the quoted poem + Luo quote)
OLD: and made the two together his own "contest of endurance" with the enemy — how can we not cherish his memory all the more, the memory carried in "In the jumbled hills a lofty scholar lies; out of the deep dense woods a hero comes" (a poem the late Ho Chi Minh, Chairman of the Vietnam Workers' Party, gave to Chen Geng)? How can we not understand, more deeply still, what Luo Qingchang said at the symposium for the making of the television drama *General Chen Geng*: "
NEW: and made the two together his own "contest of endurance" with the enemy, it is hard not to think of him in the poem the late Ho Chi Minh, Chairman of the Vietnam Workers' Party, gave him: "In the jumbled hills a lofty scholar lies; out of the deep dense woods a hero comes." And it is hard not to weigh more plainly what Luo Qingchang said at the symposium for the making of the television drama *General Chen Geng*: "
WHY: two consecutive rhetorical questions (怎能不...更...) compressed to declaratives per the rebaseline; the quoted poem, its attribution, and the Luo quote are preserved verbatim.

### p179 [T6] TOUCH  archaic "could only" -> plain verb
OLD: The Chinese Communists who went forward and fought could only hide themselves, and go to ground.
NEW: The Chinese Communists who went forward and fought had to hide themselves, and go to ground.
WHY: rebaseline "could only" register rule.

### p183 [T6] TOUCH  cut 不能不 "could not help"
OLD: Thus at the flood of revolution they could not help outdoing one another in fervor and radicalism;
NEW: Thus at the flood of revolution they outdid one another in fervor and radicalism;
WHY: "could not help" calques 不能不; cut per the rebaseline.

### p205 [T6] TOUCH  cut the 即/也就是 pivot "namely"
OLD: the "Resolution on the Party's Organizational Questions" — namely, that "the Provisional Central Politburo should establish
NEW: the "Resolution on the Party's Organizational Questions," which said that "the Provisional Central Politburo should establish
WHY: "namely" pivot replaced with a relative clause; also drops one em-dash.

### p219 [T7] RECAST  de-nominalize "the [gerund] of" chain
OLD: the scattering of already-exposed Party cadres, the safeguarding of the Party Center's organs, the covering of the Party's leading cadres in their move to Shanghai, and the secret carrying of supplies and even arms — none of it could have been done
NEW: scattering cadres who had already been exposed, safeguarding the Party Center's organs, covering the Party's leading cadres as they moved to Shanghai, and secretly carrying supplies and even arms — none of it could have been done
WHY: the type-specimen "the [gerund] of the [noun]" chain the rebaseline names; finite/gerund verbs, same content.

### p093 [T7] TOUCH  de-nominalize "the gathering of"
OLD: with the gathering of intelligence and material shared out among many, it would take less time
NEW: with intelligence and material gathered and shared out among many, it would take less time
WHY: de-nominalize per the rebaseline.

### p221 [T1] TOUCH  trim fronted-superlative doublet
OLD: Rarest and most precious of all, in the very time
NEW: Rarest of all, in the very time
WHY: rebaseline's own fix example; collapses the synonym doublet.

### p037 [T6] TOUCH  vary the 等 tag "and the rest"
OLD: Mu Xin, Zhang Guotao and the rest run further still
NEW: Mu Xin, Zhang Guotao and others run further still
WHY: thin/vary "and the rest" (narration).

### p255 [T3] TOUCH  contractions in narration
OLD: Mei Gongbin was not much caught up in it, and certainly was not "suddenly arrested in secret,
NEW: Mei Gongbin wasn't much caught up in it, and certainly wasn't "suddenly arrested in secret,
WHY: contract narration negatives by ear (rebaseline).

# --- NOTE-ANCHOR moves applied out-of-band (prose already edited above) via
# scratchpad/fix_anchors.py, each verified as a substring of the post-edit
# reading file. Recorded here for the audit trail; do NOT re-run (OLD gone):
#   "a poem the late Ho Chi Minh...gave to Chen Geng" -> "the poem...gave him"
#   "on the night of 10 October took the viceroy's yamen" -> "...of October 10..."
#   "as Bo Yibo — who fought at his side in those days" -> "as Bo Yibo, who..."
# LESSON: cross-check OLD strings against notes.json anchors BEFORE editing.
