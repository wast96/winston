# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

<!-- Newest first. Example:
## 2026-01-01 — corrections batch 1
- GLOBAL: renamed "X" to "Y" everywhere (glossary + grep across ch01-ch08); rebuilt, qa green.
- LOCAL: fixed dropped clause at ch03 §2 folio 45.
-->

## 2026-08-16 — B09 review, round two: attribution, footnotes, spine method

Factual integrity (priority 1):
- ch08 attribution non sequitur resolved in the TEXT, not just the note: the
  block quote is now front-loaded "the one Zhang Guodong sets down: ..." so
  "His account is borne out by Meng Zhen" follows cleanly; the footnote was
  re-anchored and trimmed to explain that the 1999 Yang/Zhang volume reprints
  Zhang Guodong's memoir. Faithful to the source, which does attribute the
  passage to Zhang Guodong.

Still-open items from round one (genuinely missed or text-only):
- ch08 "no lamp that burned without oil" -> "no pushover" (was flagged, missed).
- ch06 flagship inversion "His guilty scheme Li Qiang saw through at a glance"
  -> "Li Qiang saw through his scheme at a glance."
- (Windtalkers note and the ch06 Zhang-count note were already added in round
  one; the reviewer was reading the pre-commit build.)

Footnotes (priority 2 — de-bundling + placement, demonstrated on the named
notes; full book-wide sweep specified in STYLE.local.md and carried in the
kickoff):
- Split the bundled conjuring note into a Han-spectacles note (at "Hundred
  Entertainments") and a Tang-conjuring note (at "Method of the Seven Sages").
- Moved the six-pleasure-house and the purge-enforcer markers from the HEAD of
  their lists to the last item (marker-at-clause-end rule).
- tingzijian de-duplicated: kept the ch01 first-appearance footnote, removed the
  redundant inline gloss in ch03 (one gloss mechanism per term).

Prose / register:
- Applied the reviewer's spine-test split to the Cixi/cabinet-of-wonders
  sentence (split the front, kept the list intact).
- "besides" as a sentence-tail adverb eliminated across ch01-ch08 (~15
  instances, the biggest remaining 1893 signal); the "apart from" and sentence-
  initial "And besides" uses left as correct modern English.

New item:
- ch05 "yawning again and again ... knew he had caught a chill": verified
  against the scan (source reads 呵欠 / 着凉), so kept "yawning" and added a
  translator's footnote explaining that in Chinese medicine repeated yawning is
  read as a sign of a chill, so a reader will not take it for a slip.

Style doc: added the long-sentence SPINE TEST (spine count, main-verb position,
lists exempt, one em-dash parenthetical, documents exempt, the 90/60-word
triage), the footnote mechanics (one note = one referent, marker at
sentence/clause end, the inline/footnote/glossary boundary, density balance),
a narration-contraction target, and updated the residual-tic counts.

REMAINING mechanical sweeps (specified in the doc, carried in the kickoff): the
book-wide marker-placement pass (~88 mid-clause markers), the ch01-thin /
ch07-08-backfill density rebalance, narration contractions to 10-15%, and the
spine-test pass over the ~100 narration sentences above 90 words.

## 2026-08-16 — B09 commissioner review: register rebaseline + corrections (ch01-ch08)

Style doc (the deliverable the commissioner asked for first):
- STYLE.local.md: added the top section "THE REGISTER REBASELINE (B09
  commissioner review)" encoding the pattern behind every note as RULE / WHY /
  FIX / CHECK entries, plus a consistency canon and an apparatus policy, so the
  back half (ch09-ch15) is drafted congruous and the eventual ch01-ch08 cleanup
  is fast. Later notes were sided with over earlier ones (modern-neutral is now
  the default register, not the archaic voice).

Outright errors (all seven, each verified against the 300-DPI scan):
- ch03: "took ages and called one another by sisterly rank" was a mis-parse of
  照年龄大小; now "ranked themselves by age" (which is what makes Li Zheshi Third
  Sister).
- ch03: the Qu Qiubai brush/xiao/flute passage kept "her" (source reads 她的; the
  instruments are Li Zheshi's) and was disambiguated to "her own" so it no
  longer reads as a pronoun error.
- ch06: "North Zhejiang Road (today North Zhejiang Road)" was a collapsed
  distinction; source has 北浙江路（今浙江北路）, now "North Zhejiang Road (today
  Zhejiang North Road)."
- ch07: 语惊四座 rendered "struck the room dumb" contradicted the applause that
  followed; now "electrified the room" (both occurrences).
- Principal Characters: Gu Shunzhang's birth year fixed to 1895 to match the
  text (was 1903, a third date the book never gives).
- ch08 and ch06: the Zhang-Guodong / Yang-Yingqi attribution tangle and the
  16/18/20 trainee counts are the author's own; both now carry a footnote
  flagging the source's inconsistency rather than a silent rewrite.

GLOBAL consistency sweeps (grep-driven across reading files, notes, glossary,
figures, book.json; anchors kept in sync, builder + qa_epub + epubcheck clean):
- American spelling throughout (Center, Theater, License/Rumor/Color, and the
  ch12/ch15 stub titles); British colloquialisms de-Britished ("gone nine,"
  "welshed," "and no mistake," "rattle-drum").
- Dates month-day-year everywhere (converted ch01's 19 and ch02's 3 DMY dates).
- "Political Bureau" -> "Politburo" (ch07-ch08).
- The June 3, 1932 Comintern report given ONE issuer and title in all three
  chapters that cite it.
- Xia Yan's memoir one title, "Lazily Seeking Old Dreams" (italic); Dong Jianwu
  "presiding pastor"; "White Terror" capitalized; the observatory "Xujiahui"
  (period name Zikawei noted); lane names fused (Fukangli, Sichengli, Taihefang
  brought into line with the glossary majority); "the ten-li foreign quarter."

Named prose fixes: chengyu triage on the flagged idioms (footnoted the
load-bearing ones, naturalized the opaque ones, de-cluttered the four-in-a-row
in ch06); modernized quote tags ("later recalled" for "in his later years");
modernized the flagged dialogue lines (Gu Shunzhang, Cai Mengjian); word-choice
items (kindly cab driver, "spent his days," "has striven," number agreement,
the ch08 mistress scene); the Qian Xuantong sentence split off its embedded
second biography; ch08 "in the end" interrogatives recast; a fronted-object
inversion fixed; the narration trailing ellipsis closed.

Apparatus: translator's note expanded with a conventions paragraph and a
voice-inoculation paragraph ("our Party" is the author's voice, not the
translator's); Principal Characters grown from 4 to 17, adding glossary rows for
Li Kenong and Hu Di; footnotes added for the attribution tangle, the trainee
counts, the moon-nearest-water idiom, and the Windtalkers film allusion.

REMAINING (specified in STYLE.local.md, carried in the kickoff): the systematic
sentence-by-sentence register de-archaizing of all narration across ch01-ch08
(inversions, antique function words, narration contractions, doublets,
de-nominalization, quote-fragment un-quoting, attribution front-loading, "and
the rest / and the others" variation) is a whole-book pass a single session
could not finish exhaustively; it is now fully governed by the frozen doc.

## 2026-08-16 — B07 (ch07) global correction
- GLOBAL: 卡德路 "Cardan Road" → "Carter Road" (verified against Shanghai
  road-name scholarship: 卡德路 = Carter Road, today Shimen No. 2 Road). Fixed
  glossary.json (places) and the two occurrences in out/ch04_reading.md; ch04
  rebuilt in the cumulative EPUB. No other built unit used the form.
