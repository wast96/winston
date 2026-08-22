# Register-pass assessment — *Zhou Enlai: Commander of the Hidden Front*

Date: 2026-08-22. Written from a read-only study of the style system on
`claude/the-sword-roars` (commit 8431573) and a measured survey of this
book's 28 built units (223,898 words, 8,945 sentences, 1,367 paragraphs).
This is an assessment only; no translation text was changed in this session.
If a pass is commissioned, run it under the corrections workflow in
CLAUDE.md (content frozen, edits via `edits/<id>_edits.md` and
`apply_edits.py`, zh read against en for anything beyond mechanical swaps,
anchors updated in the same pass, rebuild and full QA after).

## 1. What the sword branch has that this book predates

The sword book was translated after this one and carries style machinery
this book never had:

1. **Layered style contract.** `styles/_base.md` + `lang-zh.md` +
   `genre-nonfiction.md`, composed by `scripts/compose_style.py` into a
   hash-manifested STYLE.md, with `STYLE.local.md` as the book ledger
   (rules tagged `#book` / `#promote`, promotion between books on
   corroboration). This book has a monolithic STYLE.md whose content
   largely seeded those layers; the base and lang-zh material is
   substantively the same doctrine.
2. **The B09 REGISTER REBASELINE** in sword's `STYLE.local.md`. This is
   the piece this book has never been measured against. It came from the
   commissioner's whole-book read of sword's first eight chapters and
   resets the default narrator register to modern-neutral: period flavour
   from content, never from antique syntax. Its concrete rules are the
   checklist in section 3 below.
3. **The blind-critique voice gate** (`review/voice_gate_critic_prompt.md`,
   `scripts/voice_gate_critique.py`): a context-blind native-reader
   critique of the built chapter, fixes applied against the source, then
   distilled into ledger rules.
4. **A final-review protocol** (`review/PROTOCOL.md`): per-unit findings
   files in a dense greppable format, adjudication marks including
   recorded rejections, tail-of-unit paranoia, batched crop queue.
5. **`scripts/register_tics.sh`**: a grep battery that mechanizes the
   rebaseline kill list. It hardcodes `/home/user/winston` paths, so it
   runs against this book unmodified.

## 2. Where this book already meets the rebaseline (do not "fix" these)

Measured on the built reading files:

- **Sentence length is already modern.** Mean 24.9 words, median 22
  (sword pre-rebaseline ran 33; the target band is low-to-mid 20s). Only
  34 narration sentences exceed 90 words.
- **Narration contraction rate is already ~12%** (73 contractions against
  547 uncontracted negated auxiliaries), inside the rebaseline's 10-15%
  target. Dialogue contracts at ~52%. No blanket-contraction work needed.
- **Exclamations are rationed** (151 in 224k words) and rhetorical
  questions are controlled (190 question marks book-wide, most in
  dialogue).
- **Em-dash rate 3.3 per 1,000 words**, under the ch01 reference
  throughout (tracked every batch in PROGRESS).
- **No sentence-initial numerals** (0 hits).
- **Spelling locale** was already standardized American at completion;
  the nine surviving "Theatre" spellings are proper names of real Shanghai
  venues and were a deliberate decision (COMPLETION.md).
- Quoted documents keep their starchy register by design; the partisan
  voice ("our Party," "running dogs," "traitors") is deliberate and
  documented. None of that is a defect.

## 3. Defect inventory, ranked by value per keystroke

### Tier A — mechanical consistency (high value, near-zero risk)

1. **Date format flipped mid-book.** ch00-ch05 and ch09-ch12 use
   day-month ("23 July 1921", 95 instances); ch06-ch08 and ch13-ch27 use
   month-day ("May 21, 1931", 609 instances). The sword canon fixed this
   exact defect (month-day everywhere). Normalize the 95.
2. **Political Bureau vs Politburo.** 51 "Political Bureau" across most
   chapters, 14 "Politburo" in ch19-ch20 only. Same body, two names,
   internal drift. Sword's canon decided "Politburo"; whichever form this
   book's glossary decides, collapse to one and record it in
   authority.json.
3. **"in good time" x16** survives against this book's OWN ledger
   (STYLE.md decided 及时 = "in time / promptly", explicitly not "in good
   time"). One "driving into the heart of the enemy" (ch07) against the
   ledger's 打入 = "plant inside / infiltrate".

### Tier B — the rebaseline kill-list sweep (semi-mechanical, by-ear
confirmation per hit; the sword review called this class the highest
flow-per-keystroke on its list)

Counts across all 28 units:

- **"besides" x87**, mostly the trailing "...and a reward besides." form
  that the sword review named the single loudest antique signal. Swap for
  "as well" / "too" / cut.
- **"and the rest" x37 + "and the others" x50**: the 等 tag rendered the
  same way every time. Vary ("among others"), restructure, or cut where
  the list is complete.
- **"one after another" x31**: the 纷纷/相继 calque at fixed wording.
  Vary ("in turn," "one by one") or cut.
- **"could only" x22, "could not but/help" x6**: plain the archaic ones
  ("had to," or just the verb); idiomatic hits stay.
- **"no few / no small / not a little" x20**: litotes calques; "a good
  many," "considerable."
- **Antique stragglers**: "at length" x4, "let slip" x5, "thereupon /
  whereupon / presently" x3, plus scattered phrases of the same register
  ("as ill luck had it," "was given to startling acts" class) that the
  grep battery will not catch and a read of the flagged chapters will.
- **Nominalizations**: 42 hits of "the [gerund/ment] of the"; convert
  roughly two-thirds to finite verbs per the rebaseline rule.
- **Narration ellipses**: ~20 "..." occurrences; keep only those inside
  quotations that genuinely break off (several are; each needs a look).

### Tier C — judgment edits (bounded, needs zh-against-en reading)

- **34 narration sentences over 90 words**: apply the spine test (split
  at spine boundaries, main verb inside the first ~20 words, protect
  colon-plus-list sentences at any length).
- **Doubled 并列 pairs**: ch01's voice gate already disciplined these, and
  most chapters read clean, but the biographical/memorial chapters (ch15
  is the type specimen) run noticeably more elevated-antique than the
  operational chapters: "enjoyed no little standing," "Through the long
  night he went on searching, high and low," "the foreign menace was not
  lifted." Some of that is quoted memorial-inscription register and
  correctly starchy; the narration around it drifts toward the same
  register and should not. A read of ch15-ch16 (the enlightened-gentry
  biographies) against the rebaseline would yield the densest findings.
- **Terminology variety worth a look, not necessarily a fix**: 叛徒
  renders as traitor (240) / renegade (29) / turncoat (11). If the
  variation tracks the source's own variation it stands; if it is
  per-batch drift, decide and collapse.

## 4. Prose quality score

Scale: relative to English-language popular narrative history as
published (the genre benchmark the style contract itself names: Hochschild,
Chang, Wakeman's popular mode), not relative to other translations.

Current state:

- **Accessibility to a native English reader with no Chinese: 9/10.**
  The apparatus is the book's outstanding feature: 339 verdict-graded
  footnotes, principal-characters page, folio-followable page markers,
  aliases tagged at first use in scene. A general reader is never lost.
- **Translation quality: 8.5/10.** Zero substantive errors in the 41-
  paragraph seeded audit; 100%-verified final batch; parity, numbers,
  entities, displacement all green; the partisan register faithfully kept.
- **Prose against native-authored genre peers: 7/10.** The best chapters
  (ch01, ch24) genuinely pass the "book someone wrote" test. The tics
  above, plus the elevated-antique drift in the biographical chapters,
  give the whole a faint but persistent translated accent that a good
  trade editor would blue-pencil.

**Overall now: 7.5/10. After a register pass: ~8.5/10** (Tier A+B alone
reach roughly 8; Tier C buys the rest). The ceiling short of retranslation
is about there: the residual is Mu Xin's own compilation structure
(repeated episode recaps, chapter-to-chapter overlap, e.g. the Carlton
Theatre meeting told in ch02 and twice in ch09), which fidelity forbids
smoothing away.

## 5. Verdict: worth it, as a bounded tic sweep, not a re-voice

Substantial, not marginal, for Tiers A and B: a few hundred edit sites,
grep-locatable with `scripts/register_tics.sh` (imported from the sword
branch) plus the counts above, each confirmed by ear, anchors re-verified,
one rebuild and full QA at the end. Tier C is worth one bounded read of
the flagged sentences and the ch15-class chapters. A blanket whole-book
re-voice is NOT recommended: the metrics in section 2 show the book
already sits at or near the rebaseline targets, and both prior revision
passes on the shelf over-predicted defect density by an order of
magnitude. Expect most paragraphs to be left alone; that is the pass
working, not failing.
