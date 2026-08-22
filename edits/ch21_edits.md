# ch21 (R4) — Tier-B tic sweep + spine test on the flagged long sentences.
# 104 paragraphs, 5 edits. A rescue narrative thick with name-lists.
#
# SPINE TEST:
# - L65 (Chen Geng's defiant denunciation, "he ran through... how X—how Y, and
#   how Z"): a single-spine rhetorical how-list; a list is never broken, and the
#   author's heat is kept (STYLE understatement doctrine). Keep.
# - L109 (Deng Wenyi's biography): a chain of single-spine sentences; the long
#   one has one main spine with an embedded "when Chiang... founded..." clause.
#   Reads clearly. Keep.
# - L201 (Zhou Enlai's hall report): a genuine multi-spine run-on (asked ->
#   gathered -> reported -> explained -> said -> told). Split once, below.
#
# KEPT:
# - The 18 等-tags ("and the rest"/"and the others"): genuine list-truncations
#   whose membership VARIES site to site (Chen Geng + Luo Dengxian + Liao
#   Chengzhi; + Yu Wenhua; Song Qingling + reporters; the women's block; the
#   cellmates). Not drift on one fixed referent; each reads naturally. The ch15
#   exemplar's rule was to LEAVE genuine 等-lists. The mild "Chen Geng and the
#   rest" vs "and the others" alternation is FLAGGED in PROGRESS for R5's
#   whole-book check_reconcile.py human read, the plan's designated place.
# - "let slip" at L83 in "let slip no chance" -> see edit (de-antiqued to match
#   R3's "let slip no [X]" precedent; the modern reveal-sense "let slip" is the
#   one the KEEP list protects, not this inverted "let slip no chance").
# - "Before long"/"before long" (161, 201): 不久, modern; keep.
# - L5 "wrecking"/"The wrecking of the Central Military Commission" (破坏): the
#   diction-ledger residual deliberately deferred to R5's whole-book cascade
#   (per HANDOFF); left untouched here so it is not double-handled.

### ch21 [T3] TOUCH
OLD: At length they announced
NEW: Later they announced
WHY: 后来,敌人声称; source is 后来 (afterward/later), not "finally" — "At length" over-formalizes; narration (plan 3.2 site)

### ch21 [T1] TOUCH
OLD: besides Tan Guofu
NEW: apart from Tan Guofu
WHY: 除谭国辅外,还有...; 除...外 noun-phrase "besides" -> "apart from" (ch15/ch18 precedent)

### ch21 [T4] TOUCH
OLD: and could only quibble at last
NEW: and at last had no choice but to quibble
WHY: 最后只好狡辩; 只好 = "had no choice but to", not the softer "could only" (narration; enemy cornered)

### ch21 [T3] TOUCH
OLD: let slip no chance to expose the enemy
NEW: missed no chance to expose the enemy
WHY: 不放过任何机会揭露敌人; the inverted antique "let slip no [chance]" -> plain modern "missed no chance" (R3 de-antiqued the same "let slip not a moment" pattern)

### ch21 [T-spine] RECAST
OLD: gather in the hall, where Zhou Enlai gave a report on the situation, explaining that
NEW: gather in the hall. There Zhou Enlai reported on the situation, explaining that
WHY: L201 spine test: split the ask->gather->report->explain->say->tell run-on once at the hall, so the report and its content read as their own sentence
