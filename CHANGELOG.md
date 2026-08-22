# CHANGELOG

Dated record of what changed and, for global corrections, what cascaded where.

<!-- Newest first. Example:
## 2026-01-01 — corrections batch 1
- GLOBAL: renamed "X" to "Y" everywhere (glossary + grep across ch01-ch08); rebuilt, qa green.
- LOCAL: fixed dropped clause at ch03 §2 folio 45.
-->

## 2026-08-22 — footnote-density pass (book stays COMPLETE)

Commissioner asked to greatly increase footnote density: explain the "little
references" a Western reader misses (people, places, organizations, events,
terms). Notes-only pass; no prose, glossary, figure or structure change.

- GLOBAL (apparatus): +353 footnotes, 425 -> 778, continuous book-wide.
  Method: the glossary is the quarry. Of the ~636 glossary rows carrying a
  vetted, researched note, 355 named subjects appeared in the prose but were
  never touched by any existing footnote. Each was surfaced as a footnote at
  its FIRST book-wide appearance, expanded past the bare glossary row with the
  subject's role in this book's narrative and stable, established facts
  (dates, offices). Content rests on the project's own vetted glossary
  scholarship plus the prose, per rule 5; notable figures/events were
  web-verified against Wikipedia / Baidu Baike; obscure roster names and
  uncertain identifications are flagged in-note, never invented (rule 4).
- Per-chapter adds (first-appearance placement, so each subject noted once):
  ch00 +2, ch01 +19, ch02 +1, ch03 +13, ch04 +33, ch05 +29, ch06 +59,
  ch07 +43, ch08 +16, ch09 +2, ch10 +27, ch11 +1, ch12 +45, ch13 +32,
  ch14 +31. ch15 had no uncovered glossary subjects; ch16 (Works Cited) and
  ch17 (Afterword) unchanged.
- TOOLING (do not revert): `scripts/note_gaps.py` (finds glossary subjects
  present in the prose but untouched by any note) and `scripts/gap_packets.py`
  (emits per-chapter first-appearance work packets). Reusable next book.
- Every note merged through `apparatus_merge.py` (verbatim-anchor and
  numeric-entity validation) and placed at first appearance by the builder.
  Rebuilt; qa_epub PASS (778 references / 778 bodies / 778 backlinks);
  check_apparatus 0 failures / 0 warnings. Docs updated: COMPLETION.md,
  PROGRESS.md, HANDOFF.md.
- BRANCH HYGIENE: session opened on a stray branch `claude/the-sword-roars-
  ztmxk9` (local only; never pushed to origin). Consolidated onto the
  canonical `claude/the-sword-roars`; stray deleted and its stale
  remote-tracking ref pruned.

## 2026-08-22 — corrections pass + full QA sweep (book stays COMPLETE)

Zero commissioner items, so a clean-checkout regression run, plus one
commissioner instruction (rename the deliverable). The regression run caught
two real regressions against the frozen B09 STYLE.local policy and fixed both.

- DELIVERABLE RENAME: `out/sword-roars.epub` -> `out/The Sword Roars in the
  West Wind.epub`. Changed only `book.json` `deliverable` (builder, qa_epub and
  the Stop hook all read that key). Old committed EPUB retired from git; new
  file added. Rebuilt content is byte-identical to the prior EPUB (unzip-diff
  verified); only the filename changed. Doc refs updated in COMPLETION.md,
  HANDOFF.md, PROGRESS.md.
- GLOBAL: footnote dates normalized to month-day-year. 19 day-month-year dates
  in note bodies ("12 April 1927" -> "April 12, 1927"; ranges "22-23 March
  1927" -> "March 22-23, 1927") brought into line with the prose and the
  translator's-note promise of month-day-year throughout. notes.json only; no
  note anchor affected. Cascade check: grep of the "D Month YYYY" pattern now
  zero across out/*_reading.md, notes.json, glossary.json, figures.json,
  book.json.
- GLOBAL: street glosses de-duplicated to once-per-street book-wide, per the
  STYLE.local rule "keep the first, cut the rest" (back Street Gazetteer carries
  the mapping). Cut 13 repeated "(today X)" parentheticals across ch03, ch05,
  ch06, ch07, ch14, ch15, keeping each street's first gloss in reading order.
  The one anchored gloss (ch04 "Avenue Joffre (today Huaihai Middle Road)") is
  a kept first occurrence. Cascade check: no "(today X)" gloss appears more than
  once book-wide; check_apparatus 0/0.
- QA: rebuilt; qa_epub PASS; epubcheck 5.1.0 0/0/0/0; check_apparatus 0/0;
  check_reconcile epithet-drift SKIPPED (no data/zh in clean checkout),
  glossary-forward 1120/1140 (unchanged by these edits; the 20 unused decided
  forms are notes-only or short-form variants), spelling-locale flags only the
  deliberate "China Defence League" x3; term_ledger regenerated, in sync with
  glossary.json.
- Files touched: book.json, notes.json, out/ch03_reading.md, out/ch05_reading.md,
  out/ch06_reading.md, out/ch07_reading.md, out/ch14_reading.md,
  out/ch15_reading.md, out/term_ledger.md (regenerated, no change),
  out/The Sword Roars in the West Wind.epub (new), out/sword-roars.epub
  (removed), COMPLETION.md, HANDOFF.md, PROGRESS.md, CORRECTIONS.md,
  CHANGELOG.md.

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
