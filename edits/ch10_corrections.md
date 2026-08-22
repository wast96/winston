# ch10 corrections-pass edits (source-dependent faithfulness items)
#
# These resolve the four source-dependent flags logged in PROGRESS.md's R04
# entry, each crop-verified against source.pdf before touching the text. The
# R04 register edits live in edits/ch10_edits.md (already applied, committed at
# a0c5d30) and are NOT re-run here; this separate list is applied with
# scripts/apply_edits.py --suffix corrections ch10.
#
# Verified crops (printed folios cited):
#  - folio 307 (pdf 343): 苦熬十四年的抗日战争 -> "fourteen bitter years".
#  - folio 323 (pdf 359): 抗日战争已经打了十五年 -> "fifteen years".
#    14 vs 15 is the source's own inconsistency (1931 vs inclusive reckoning);
#    the "eight years" elsewhere is the 1937 full-scale-war span. Rendered as
#    printed, footnoted (NOTE-ADD below). No number changed.
#  - folio 313 (pdf 349): 八路军三个师派了三个参谋 -> three officers posted;
#    folio 314 and the surveillance run print 三人 / 两个联络参谋 in one breath;
#    only Zhou Liwu and Luo Bolun are named. Source's own three/two slip;
#    rendered as printed, footnoted. No count changed.
#  - folio 339 (pdf 375): "章炳南"误写为"张炳南" — the martyr's surname 章 (Zhang)
#    miscarved as the homophone 张 (Zhang). Both are "Zhang" in pinyin, so the
#    old English ("'Zhang Bingnan' written by mistake for 'Zhang Bingnan'") was
#    self-nullifying. TOUCH below makes the error legible; NOTE-ADD carries the
#    two characters. (The performer at folio 335 correctly reads 章炳南.)
#  - folio 332 (pdf 368): 当晚王实味被处死 — the body text says only "put to
#    death"; the "dry well" is the later documented record, not the book's
#    text. Handled by refining the existing note directly in notes.json.

### p339 [T6] TOUCH
OLD: To this day the martyrs' monument here bears the names of nineteen of them, with "Zhang Bingnan" written by mistake for "Zhang Bingnan."
NEW: To this day the martyrs' monument here bears the names of nineteen of them, though it carves the martyr Zhang Bingnan's surname with the wrong character.
WHY: 至今，这里的烈士纪念碑还镌刻着其中十九人的名字，"章炳南"误写为"张炳南"。 The author's point is that the monument miscarved the surname 章 as the homophone 张; both romanize to "Zhang," so the old rendering said a name was mistaken for itself. Same fact (surname miscarved), now legible; the characters go in the footnote.

NOTE-ADD
ANCHOR: with the wrong character
NOTE: The performer's surname is &#31456; (Zhang); the monument miscarves it as the common homophone &#24352; (Zhang). The two characters are plainly different in Chinese but identical in pinyin, so the slip &#8212; the author's whole point &#8212; vanishes in romanization. He appears earlier in this chapter as the Border Security yangge troupe's well-known performer.
WHY: without the two characters, an English reader cannot see what the monument got wrong.

NOTE-ADD
ANCHOR: fought for fifteen years
NOTE: The book reckons the war's length inconsistently. This chapter opens by calling it &#8220;fourteen bitter years&#8221; (counting from the 1931 Mukden Incident to 1945); &#8220;fifteen years&#8221; here is the author's own figure, given as printed. The &#8220;eight years&#8221; spoken of elsewhere is the older conventional span, counted from the 1937 Marco Polo Bridge Incident. No one count is corrected against the others.
WHY: a reader who noticed "fourteen" at the chapter's head will trip on "fifteen" here; the note owns the source's inconsistency rather than papering over it.

NOTE-ADD
ANCHOR: became the Nationalists' open intelligence officers in Yan'an
NOTE: Three officers were posted, one to each of the Eighth Route Army's three divisions, and the account here and below slips between &#8220;the three&#8221; and &#8220;the two&#8221;: by the 1945 scenes only two are named and shadowed, Zhou Liwu and Luo Bolun. Both counts stand as the source gives them.
WHY: the "three... stayed on" here and the "two liaison staff officers" a few paragraphs down read as a contradiction; it is the source's own, and the note says so.
