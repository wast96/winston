# ch03 revision edits (R2 sweep) — TIER 1+2, mechanical/tic only

Applied with `python3 scripts/apply_edits.py ch03`. Every OLD occurs exactly
once. Two prose edits break a note anchor and ship a NOTE-ANCHOR pair in the same
list (Politburo at ch03:84; the inversion recast at ch03:88). Note-body date
reformats (7 D-Month-YYYY dates) are handled separately in notes.json via a json
load/dump (apply_edits cannot touch a note body); see PROGRESS.md. No numeral
changes. ch03:114 "one after another" is inside a {v} block (KEPT); ch03:62 is
the only editable "one after another" and, with no domination (the {v} instance
aside), was LEFT. ch03:5/15 "had no wish to" read as natural reported speech and
were LEFT (the tier-1 target is the stiff "could not but" formula, ch03:98/111).

## TIER 1 — Politburo (政治局 -> "the Politburo", never "Political Bureau")

### p084 T1 TOUCH
OLD: a member of the Political Bureau of the CPSU Central Committee, had been assassinated
NEW: a member of the Politburo of the CPSU Central Committee, had been assassinated
WHY: 政治局 = Politburo (the CPSU Политбюро; standard English "Politburo").

# The note anchored on this clause must move with the prose edit:
NOTE-ANCHOR
OLD: Kirov, a member of the Political Bureau of the CPSU Central Committee
NEW: Kirov, a member of the Politburo of the CPSU Central Committee

## TIER 1 — inversion recast (ch03:88, subject-first per plan sec.3.2)

### p088 T1 TOUCH
OLD: So answered, with one voice, several of the chief men Kang Sheng named: Xiao Shouhuang, Ouyang Xin, He Changzhi.
NEW: Several of the chief men Kang Sheng named, Xiao Shouhuang, Ouyang Xin, and He Changzhi, answered with one voice.
WHY: fronted "So answered ..." inversion -> subject-first; the preceding quote
     already carries their words. (No em-dash introduced: ch03 has none.)

# The note on the three cadres was anchored on the old colon-list; re-anchor it
# to the names as they now read in the recast prose:
NOTE-ANCHOR
OLD: several of the chief men Kang Sheng named: Xiao Shouhuang, Ouyang Xin, He Changzhi
NEW: Xiao Shouhuang, Ouyang Xin, and He Changzhi

## TIER 1 — "could not but" formula -> plain equivalent

### p098 T1 TOUCH
OLD: and could not but have known of so grave a matter
NEW: and must have known of so grave a matter
WHY: "could not but have known" (couldn't have failed to know) -> "must have known".

### p111 T1 TOUCH
OLD: it could not but shake Mao Zedong
NEW: it was bound to shake Mao Zedong
WHY: "could not but + verb" -> plain "was bound to".

## TIER 2 — litotes calque -> stated positively

### p067 T2 TOUCH
OLD: wronged not a few comrades
NEW: wronged a good many comrades
WHY: 不少; "not a few" litotes calque -> "a good many" (the plan's prescribed form).
     KEEP in the same paragraph: "which was no small thing" is idiomatic English.

### p099 T2 TOUCH
OLD: He had had no few comrades killed
NEW: He had had a good many comrades killed
WHY: 不少; "no few" litotes calque -> "a good many" (plan sec.3.2 example).
