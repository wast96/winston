# HANDOFF: Nameless Heroes (英雄无名), Chen Gongshu. REGISTER REVISION PASS IN PROGRESS

**The translation is COMPLETE (the record is preserved below), and the
commissioner has ordered a whole-book REGISTER REVISION PASS. The authority
for the pass is `REVISION_PLAN.md`; where it and this file disagree, the plan
wins. Batches R1 through R9 run per the plan's §8 schedule; each batch
session updates the kickoff block below for the next one.**

## Message to paste into the next chat

```
Nameless Heroes R7: register revision pass

Branch: claude/nameless-heroes ONLY. First acts: git fetch origin
claude/nameless-heroes && git checkout claude/nameless-heroes && git
reset --hard origin/claude/nameless-heroes. If the harness started you
on a stray branch, consolidate and delete it per CLAUDE.md rule 2.
Never read any other branch.

Read CLAUDE.md, then REVISION_PLAN.md IN FULL (it is the authority for
this pass), then run ./setup.sh.

Scope this batch: ch25, ch26, ch27, ch28, ch29. Content is frozen;
English-to-English register edits only, per REVISION_PLAN.md §3 (defect
classes T1–T6, KEEP list) and §5 (method, exactly). Edits via
edits/<id>_edits.md + apply_edits.py; verify_unit + tic battery
before/after per chapter; spot-audit 10% of edited paragraphs;
check_register --ref reference/R1_frozen.md; rebuild + qa_epub; commit
and push at chapter boundaries.

End of batch: PROGRESS.md updated (tic tables, spot-audit, rejected
findings), HANDOFF.md kickoff updated, and the reply carries BOTH chat
deliverables: the rebuilt EPUB attached AND the next batch's kickoff
pasted verbatim in a fenced code block. Run to completion; no mid-batch
approval stops.
```


## Revision pass state (after R6)

- **DONE:** R1 (ch06, exemplar, frozen as `reference/R1_frozen.md`). R2 (ch07,
  ch08: 86 + 65 edits). R3 (ch01-ch05, ch09, ch10: 85 edits). R4 (ch11, ch12,
  ch13: 217 edits). R5 (ch14, ch15, ch16, ch17, ch18: 170 edits). **R6 (ch19,
  ch20, ch21, ch22, ch23, ch24): 181 edits total** (ch19 3, ch20 21, ch21 52,
  ch22 66, ch23 1, ch24 38) via `edits/<id>_edits.md` + `apply_edits.py`. The
  front and opening of the Third Part (Shanghai): the author's notice (ch19) and
  preface (ch20), then Chapters 1-4 — arrival + unit inventory (ch21); the Cheng
  Haitao/Wan-Lilang/Fan-Xing/Chen-Mingchu chapter (ch22); the reverent intro on
  the three foes (ch23); the police/gendarmerie/No.76/Yu-Yefeng chapter (ch24).
  Dominated again by DATE accessibility (ch20-ch24 are mission-chronology
  chapters — Republic-year and spelled day-month narration dates ->
  Gregorian/American across 1925-1983, +1911, number-check-safe; ALL quoted-
  document dates LEFT). Plus T6 impersonal "one" thinned where it renders a
  concrete 你/我/我们; adverbial "besides"/"aught"/"still less"/"withal"/"making
  bold" (T1); a few T2 could-not-but/litotes/inversion; light T5 naturalization
  of Mao Wanli's monologue (ch21); recurring "severally" and "one may say/see"
  varied (RULE R1-5); and three RULE R1-1/R1-2 fixes ("all but the executors";
  大显身手 "shown his hand" -> "prowess"; a dangling participle). All fidelity
  gates green (parity by construction; numbers 0 — ch19 4 / ch20 26 / ch21 155 /
  ch22 286 / ch23 7 / ch24 161 pairs; anchors ch19 0 / ch20 2 / ch21 8 / ch22 7
  / ch23 1 / ch24 6 all resolve; align OK; check_content all six "in the paired
  paragraph"). qa_epub PASS + epubcheck 0/0/0/0. **check_register: ch19/ch20/ch23
  within tolerance; ch21/ch22/ch24 flag STILTED — the ch08/ch12/ch17-class
  documentary false positive (large quoted-document/roster mass + Wanli's
  deliberately-analytical monologue; shall% 33-36% the deliberate narrating
  "shall"), NOT chased.** No blind critique this batch (R5 carried one; the
  second is scheduled for R8, §8). Full tic tables + spot-audit + flags in
  PROGRESS.md §R6.
- **Carry-forward for R7+:** voice sheets in REVISION_PLAN.md §3.4; T3 rule as
  practiced — recurring decided proper names/orgs plain in narration after
  book-first use; quotes stay at naming/anatomizing sites, marked irony, titles,
  code names, quoted documents, dialogue, and **note-anchor sites (preserve the
  quotes on any anchor substring; the ch09 generator auto-skipped the "first
  taste of defeat" Beiping-Station anchor)**. Generate T3 quote-strips
  programmatically (byte-exact OLD, uniqueness pre-checked, anchor-aware) and
  skip whole quoted-document/dialogue paragraphs. Spelled-ordinal AND 民國-year
  dates in narration -> American/Gregorian (accessibility); day-only ordinals
  and dates inside quoted documents stay.
- **New noise.txt entries (R6):** `四○七` (ch24 Room 407; the full-width zero ○
  breaks the CJK run so the checker read bare 4/7 which the old spelled ordinals
  covered, RULE R1-3; the real 407 is fixed in English as "Room 407") —
  do-not-revert. R5 `五十一、二`, earlier R4 `二十二、三`, `二○七`, R3 `四、五千`,
  `二十一、二`, `二十七、八`, R2 `三、四两`, R1 `五官`, `四个大字` all stand.
  `scripts/align_dump.py` (QC-only aligned zh|en dumper) stands.
- **R5 RULE R1-3 latent matches (surfaced by date edits, documented):** ch17 p054
  "twenty-second" had been supplying the 2 for 两周 -> fixed by carrying the real
  quantity ("fortnight" -> "two weeks"); ch18 p115 "twenty-ninth" supplies the 9
  the variant 廿九 needs -> kept spelled ("twenty-ninth of April", month only
  Anglicized). Watch this class on every date edit that drops an ordinal word.
- **Tooling do-not-revert:** kickoff_guard Stop hook; apply_edits.py OLD
  uniqueness contract; scripts/align_dump.py; the noise.txt entries above.
- **R9 (whole-book close) reconciliation flags** logged in PROGRESS §R1
  (Baomiju, storey/story, "political operation"), §R2 (ch07 one-off hotel names;
  ch08 group-name / special-commissioner / inspectorate-system quoting), §R3
  (民國-year rendering; 第二处 "Second Bureau"(ch09) vs "Second Department"(ch05);
  "the cook who does the cooking" tautology ch09), §R4 (project-name/hotel
  quoting for "Hanoi work" and "Continental"/"Railway"; "Wang case" quoting;
  ch13 p130 四十年代 "the forties" possible Minguo-40s=1950s; ch13 民前 birth-year
  1884 vs p134 1883; ch13 p152/p155 二月 split), and **§R5 (为虎作伥/虎伥 rendering
  drift ch14 "cat's-paw to the tiger" vs ch17 "the tiger's lackey"; 虎头蛇尾 drift
  ch15 "a tiger's head, a snake's tail" vs ch18 p052 "...trailing off to a snake's
  tail"; ch18 p103 民前四年 = 1908 LEFT unconverted, +1911 does not apply to 民前
  forms; 沐猴而冠 ch18 p010 "play the monkey in a hat"), and **§R6 (为虎作伥 now
  FOUR variants, + ch22 p016 "the tiger's accomplice" and ch23 p006 "playing
  jackal to the tiger" [ch23's is a NOTE ANCHOR, R9 must move it]; 沐猴而冠 also
  ch24 p098 "a monkey crowned and gowned"; ch24 p085 gendarme-roster 二十/二十七
  SOURCE typo LEFT era-year; ch22 p266 桓/恒 bystander-name source glitch; 爪牙
  "cat's-paw" overlaps the 为虎作伥 image, keep the two idioms visibly separate).**

## ⚠ COMMISSIONER DIRECTIVE (2026-08-22): a FOOTNOTE-DENSITY pass (F0) AFTER R9

The commissioner has ordered an additional final pass, **after the whole R1-R9
register revision is complete**, to **greatly increase footnote density** across
the EPUB: explain the little references, the people, places, terms, events, and
allusions a non-specialist Western reader would miss. Density is a reader model,
not a quota — **never add a note just to add one**, but be generous: terms,
people, places, events, and references should be explained. This is authored as
a single final wave, **F0** (one session over the whole book), with its
canon in **REVISION_PLAN.md §12**. When R9 completes the register pass, the R9
reply must serve up the **F0 kickoff** (not a "book complete" notice); the directive
and its kickoff are transcribed in `CORRECTIONS.md` and REVISION_PLAN.md §12 so
they survive every batch seam. Carry this note forward in every HANDOFF until
the footnote pass is itself complete.

---

# Completion record (pre-revision, preserved)

**THE TRANSLATION IS FINISHED. What follows is the completion notice from
B36, kept for the record; the revision pass above supersedes its "no next
batch" instruction. A correction pass, if ever needed, is still governed by
`CORRECTIONS.md`.**

The full completion report is `COMPLETION.md`; read that for the detail. This
page is the one-screen summary.

## What was delivered

- **`out/nameless-heroes.epub`** — the whole memoir, 43 of 43 units, committed
  with `git add -f` on branch `claude/nameless-heroes`.
- **43/43 chapters translated**, clean pending-aware TOC (no placeholder),
  complete coverage.
- **375 translator notes**, 0 source notes (the source carries none of its own).
- **Glossary: 708 rows** (people 479, organizations 71, places 132, terms 26).
- **0 in-text figures**; the source's single image (its cover) is reused
  byte-identical.

## Final gate results

- `qa_epub`: **PASS** — 57 files, 50 documents, 375 note references / 375 bodies
  / 375 backlinks, all links resolve.
- epubcheck 5.1.0: **0 fatals / 0 errors / 0 warnings / 0 infos** (EPUB 3.3).
- Whole-book scripted checks green: parity 6,160/6,160; numbers 0 unresolved;
  register within tolerance of the frozen reference `reference/B01_frozen.md`;
  content displacement limited to the documented homograph/substring false
  positives (ch08 Shunde, ch09 Jize, ch13, ch26, ch38, ch41 — none real).
- Deep audit (`out/deep_audit.md`): fixed-seed 45-pair sample, 44/45 fully
  faithful, zero substantive errors; one title nuance found and fixed.

## Completion work done in the final batch (B36)

- Translated ch43, the Afterword (英雄无名 篇后续话) — a reflective coda over the
  whole five-book memoir, 31 paragraphs, 3 notes, Chen's grave register with the
  deliberate narrating "shall" preserved.
- **Spelling locale unified to American** across prose, notes, and glossary
  (was mixed 736:38; now 0 British / 774 American).
- **张垣 / 张家口 reconciled** to Zhangyuan / Zhangjiakou book-wide, with a
  first-appearance city note at ch08.
- **`authority.json` fed back** under slug `nameless-heroes` (399 new terms, 43
  agreements, 1 honestly-flagged disagreement).
- Wrote `out/term_ledger.md`, `out/deep_audit.md`, and `COMPLETION.md`.

## Anything a later reader/commissioner should know

- Two items were **documented, not silently changed** (see COMPLETION.md
  "Findings that need the commissioner's eye"): 宋子文 rendered pinyin
  "Song Ziwen" where the shelf uses "T. V. Soong" (glossary note bridges it);
  and 制裁/sanction, used from ch02 but formally defined in the ch04 note.
- **Provisional romanizations remain to firm up** (241 people, 19 places, 5
  organizations), each flagged `provisional` in the glossary and marked in the
  build; listed at the end of `out/term_ledger.md`.
- **Tooling that must not be reverted** and the exact clean-checkout rebuild
  commands are in COMPLETION.md ("Provenance and method").

*Do not edit this file further. The book is complete.*
