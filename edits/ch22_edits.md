# ch22 (R4) — Tier-B tic sweep. 47 paragraphs, 0 edits (a clean chapter).
#
# ch22 is saturated with quoted testimony and documents, and the plan's KEEP
# list protects them. Every flagged site resolves to KEEP:
#
# - L41 (the prison memoir: Gu Shunzhang's magic tricks and hypnotism), L47
#   (its continuation, "I knew well in my heart..."): a first-person quoted
#   memoir. "for all that" (for all that I worked for the Party), "He could
#   only say", "besides the ordinary instruments", "His talk of starting a farm
#   and so on", "If I could only win a thread of a crack", "Liao Chengzhi, Luo
#   Dengxian, and the rest" — all inside the memoir; register untouched.
# - L53: "she at length found the Party organization" is inside the quoted
#   Organization Department of the Party Center statement; document register.
# - L81: "too gravely wounded, could only be heard gasping" is inside the Shen
#   Bao news report quoted at length; document register.
# - L97 & L99: "fearing besides that Guo would leak information", "come to
#   Shanghai to seek relatives, and so on", "hit by a comrade's shot, and so
#   on", "besides showing a hypocritical grief" — all inside Shen Zui's quoted
#   account of the assassination; testimony register.
# - L69 (narration): "they were freed one after another" (相继获释, genuine
#   sequence); "Chen Geng, Luo Dengxian, and the rest" (等 name-list); "besides
#   demanding the release of all political prisoners" (除...外,还提出 rendered
#   with besides+gerund, which the KEEP list keeps as modern). Its long
#   sentence is a single-subject action chain (went -> visited -> secured a
#   meeting -> demanded -> proposed), semicolon-separated; no split.
# - L29 & L33 (narration): "and the rest" (等 name/epithet truncations); keep.
# - Nominalization hits (L97/L99 "the morning/evening of the"): time-expression
#   false positives; keep.
# - L73 "and so on the one hand": a FALSE POSITIVE — the text is "and so, on the
#   one hand searched out...", not a 等-tag.
#
# No TOUCH/RECAST blocks. apply_edits.py is a no-op here; verify_unit stays green.
