# REVISION PLAN — register polish + generous annotation, whole book

Commissioner's brief (2026-08-04): make the prose feel non-clumsy to a Western
reader while preserving poeticness where it earns its place ("things can still
be beautiful, they just have to be clear, and it's gotta be gripping"); do not
go HAM — fix it up, make it better, keep fidelity to the original; and expand
the footnotes generously so a non-specialist catches all the little references.
Formatting clarity (what is body text vs. what is not) is ALREADY DONE — see
§1. This plan covers what remains, structured so one executing session can do
it in at most three batches, ideally two or one.

Read CLAUDE.md first (the commissioner's rules at the top are non-negotiable:
one branch = `claude/the-longest-day-in-changan`, deliver the EPUB in chat
after every batch, never invent, no em dashes in prose written TO the
commissioner). This plan supplements it; where HANDOFF.md disagrees with this
plan, this plan wins — HANDOFF.md predates the revision and describes the
finished first-draft state.

---

## 1. State of play — what is DONE, do not redo

Committed at `a10fa8d` (plus this plan's commit) on the working branch:

- **Set-off formatting recovered from the source EPUB.** The reading files now
  carry markers the builder renders distinctly: `***` alone on a line = scene
  break (110 across the book, from the source's centered rule image);
  `{v} ` prefix = chapter-opening vignette (the source's kaiti passages);
  `{d} ` prefix = dateline/place lines (centered small caps); `{g} ` prefix =
  the source's own hour-note (bordered end-block). `{p} ` = verse is defined
  and styled but not yet applied anywhere (see §5).
- **Typography.** All 26 units converted to curly quotes/apostrophes;
  notes.json anchors remapped (0 unresolved); glossary/book.json display
  strings converted. `scripts/smart_quotes.py` is the idempotent normalizer.
- **Builder/checker upgrades.** `build_reading_epub.py` renders the new
  classes, centers chapter titles, and drops char-count clutter from the
  Contents page. `check_structure.py` parity skips `***` and strips the
  prefixes. `scripts/verify_unit.py chNN` is the one-command per-unit gate
  (parity + numbers + anchors). `noise.txt` gained two lookbehind fixes
  (`十一`, `六个字`) so replaying old chapters is clean.
- **Fidelity repairs already made:** ch03 invented speaker tag removed
  (zh + en), ch09 missing closing quote restored.
- **Prose polish PARTIALLY done** by an interrupted pass: ch01, ch04, ch05,
  ch06, ch07 each carry a first tranche of good conservative line edits
  (roughly the first 15–40% of each file). Treat these five like every other
  chapter — sweep them start to finish; the existing edits just mean less to do.
- **Verified baseline:** all 26 units currently pass verify_unit (numbers 0
  unresolved, 86/86 anchors, parity EQUAL) and the EPUB builds green
  (`qa_epub.py` PASS).

What REMAINS = this plan: (A) register polish of all 26 units, (B) footnote
expansion from 86 to roughly 230–300, (C) verse marking, (D) final QA +
delivery. That is the whole job; nothing else is open.

---

## 2. Hard invariants (mechanically checked; violating any one fails the batch)

1. **Line discipline.** `data/zh/<id>.txt` line N ↔ reading-file paragraph N,
   1:1, minus `***` lines which have no zh partner. Never merge, split, add,
   or delete paragraphs. Blank lines separate paragraphs; keep the shape.
2. **Markers.** `***` lines and `{v} `/`{d} `/`{g} ` prefixes stay exactly
   where they are. Do not edit the text of `{d}` or `{g}` lines at all.
   `{v}` vignette text MAY be polished. You may ADD `{p} ` per §5.
3. **Numbers.** Every numeral, date, year, count, distance, sum keeps its
   value (words or digits both fine). `verify_unit.py` replays the number
   check per unit; if it flags a NON-quantity numeral, extend noise.txt per
   its own header rules (ordering is load-bearing; longest first; prefer a
   lookbehind over a broad strip — see the `十一`/`六个字` entries as models)
   and record why in PROGRESS.md. A real dropped number must still fail.
4. **Glossary.** One rendering per referent, already decided in glossary.json
   (656 rows). Never re-romanize, never vary a name/title/office/place. Grep
   the glossary before writing any proper noun.
5. **Existing anchors.** Every anchor in notes.json must survive
   byte-for-byte. Get the per-chapter list with:
   `python3 -c "import json;[print(e['anchor']) for e in json.load(open('notes.json')).get('chNN',[])]"`.
   Text inside those exact phrases is off-limits to edits (around them is fair
   game). If you genuinely must rephrase through one, update the anchor in
   notes.json in the same batch and re-verify. The builder refuses to build on
   an unmatched anchor, so this cannot slip through silently.
6. **Typography.** Curly quotes only; em dashes; ellipsis style as found.
   Multi-paragraph quotations: no closing quote on a continuing paragraph, the
   next re-opens. After all edits re-run `python3 scripts/smart_quotes.py`
   (idempotent; also re-verifies anchors). Its "unbalanced doubles" warnings
   are EXPECTED at exactly these legitimate continuation lines: ch02:263,
   ch02:603, ch03:197, ch10:61, ch10:593 — plus any new multi-paragraph
   quotes your edits legitimately create; anything else, investigate (ch09
   once hid a genuinely dropped closing quote this way).
7. **Fidelity.** Never add content, never drop content, never launder an
   ambiguity into fluency. If the English deviates from the zh line (omission,
   addition, wrong sense), fix it to match and log it in PROGRESS.md under
   "fidelity fixes". The zh file is authoritative; read the zh line for every
   paragraph you touch.

Per-unit gate: `python3 scripts/verify_unit.py chNN` after finishing each
chapter, before moving to the next. Do not batch verification to the end.

---

## 3. Register specification — what to fix, what to keep

### 3.1 The target voice

Contemporary literary English for a fast historical thriller: transparent,
concrete, stress-final sentences; lyrical only where the source is lyrical.
Period flavor comes from CONTENT — titles, objects, forms of address, units
(li, zhang, chi, "mark", finger-snap all stay) — never from fake-antique
grammar. Default test for any sentence you touch: could a good contemporary
translator of, say, Mo Yan or Jin Yong have written it? If it sounds like a
Victorian rendering of Scripture, it goes.

### 3.2 Fix list — the recurring defect classes, with live examples

Each class below names real instances (file:line as of this commit). The
listed instances are EXAMPLES, not an exhaustive to-do list: sweep every
paragraph of every chapter for the class, fix what matches, leave what
doesn't. Expect roughly 15–40 touches per chapter; the goal is a quiet edit,
not a new translation.

**A. Fake-antique verb forms and constructions.** "was become" (ch24:591 "the
residence was become a stretch of broken walls" → "had become"/"was now"),
"there could be seen X" (ch24:567 → "…and half-hidden amid the green willows
stood an exquisite residence…"), "durst", "would fain", "whereat". Replace
with plain modern forms.

**B. Archaic adverbs/particles used as translationese.** "whereupon"
(ch05:133, ch07:239, ch07:645, ch10:527 → "at that", "and then", or restructure),
"not a whit" (ch05:35, ch07:243, ch07:337, ch23:335 → "not in the least", "not
one bit"), "in a twinkling" (ch24:577 → "in an instant"), "scarce" as adverb
(ch10:45, ch19:521, ch20:377, ch24:427 → "scarcely"/"barely"; CAUTION ch16:249
"scarce" is a true adjective of scarcity — leave those), "upon the air"
(ch15:9, ch22:127 → "in the air" or restructure), "X than his/their wont"
(ch18:159, ch19:103 → "than usual"). Also sweep for: "amidst"→"amid" where it
clatters, "betook/bethought", "say you", "yonder", "presently" in the archaic
sense, "ere", "nigh".

**C. Stilted inversion and fronting.** "Broad and high it spread" (ch24),
"Steam as it might, it could not boil away…" (ch15:11 area). English wants
subject-first except for deliberate emphasis; un-invert unless the source
paragraph is itself marked/lyrical (vignettes may keep one inversion if it
sings).

**D. Calqued phrasing that no English writer would produce.** The interrupted
pass fixed instances worth imitating: "their inspections went a shade faster
than their wont" → "…than usual"; "filed in single file" → "filed up the
ramp" (redundancy); "but every man's shoulders were faintly taut" → "every
man's shoulders drawn faintly tight" (false-contrast 但/却 rendered as "but"
when English wants apposition); "land was worth its weight in gold" →
"an inch of ground cost an inch of gold" (寸土寸金 — keeping the image beats
substituting a stock English idiom); "kept them under close guard" → "under
close watch" (watching, not guarding). Generalize: watch 却/倒/竟 rendered as
mechanical "but/yet/actually", 便/就 as "then", 只见 as "one saw only", 不由得
as "could not help but" every single time — vary or drop.

**E. Wrong-register dialogue.** Characters must sound like themselves:
Zhang Xiaojing terse, streetwise, occasionally coarse (the coarseness stays:
"我他妈" ch13, 小娼妇 = "little whore" ch23/24 are decided renderings); Li Bi
young, precise, bookish; clerks and brokers colloquial; the court formal; the
Son of Heaven's 朕 = royal "Us/We/Our", 圣人 = "the Sage" (decided). Fix
bookish constructions in street mouths ("has your lordship a house already
engaged?" is right for Cui Liulang flattering a client; "I shall presently
investigate" in a runner's mouth is not). Contractions are welcome in
informal speech and forbidden in memorials/edicts.

**F. Pronoun fog in action scenes.** Fight and chase paragraphs where "he"
switches referent mid-sentence. Re-anchor with names sparingly (once per
confusion point, not every clause) — but check the zh first; if the source is
deliberately delaying the reveal of who acted, keep the delay and let word
order do the work.

**G. Monotonous sentence machinery.** Chains of "and then… and then", three
consecutive sentences opening with the same subject pronoun, semicolon pileups
transcribing Chinese comma-chains. Merge or re-hinge clauses WITHIN the
paragraph (never across paragraphs). Keep the source's information order where
it reads fine; re-order within a sentence when English stress wants the
payload at the end.

**H. Over-explained or doubled renderings.** Where the first draft rendered
one zh phrase twice ("belt and braces": "counted and tallied up the crates"),
keep the better half.

### 3.3 Keep list — do NOT "fix" these

- The `{v}` vignettes' dream-logic and any closing panorama's lyricism — polish
  word choice, keep the strangeness and the rhythm.
- Decided renderings and forms of address (grep glossary.json; see also the
  House-style section of HANDOFF.md): the Sage, Us/We/Our, "your humble
  servant", Director He, the aphids (蚍蜉), Wolf Guards, the Jing'an Bureau,
  all offices per Hucker, all measure units (li, zhang, chi, arm-span, fen,
  finger-snap, "mark" for 刻), "ten-odd" for 十余.
- Deliberate repetition that is structural in the source (the wolf imagery,
  the watchtower signal formulae, ritual/liturgical passages).
- The multi-paragraph-quotation convention and all `{d}`/`{g}` lines.
- Anything inside an existing note anchor phrase.

### 3.4 Method per chapter (do it exactly like this — it is what worked)

1. Read the chapter's zh and reading files side by side in aligned chunks of
   40–60 paragraphs (`data/zh/chNN.txt` line k ↔ reading paragraph k, `***`
   excluded). Do NOT skim only the English: half the value of this pass is
   catching quiet fidelity drift, and that requires the zh line.
2. Make edits with targeted Edit calls on distinctive substrings, several
   per call where convenient. Never rewrite whole paragraphs that need one
   word. Do not re-read the file after each edit.
3. While reading, collect footnote candidates (§4) and verse candidates (§5)
   for the chapter in one pass — do not make a second full read for notes.
4. Finish the chapter: `python3 scripts/verify_unit.py chNN`. Fix anything it
   flags NOW. Then the next chapter.
5. Keep a running log (chapter → number of touches, fidelity fixes, notes
   added) in memory or a scratch file; it becomes the PROGRESS.md entry.

---

## 4. Footnotes — from 86 to generous

### 4.1 Targets and kinds

- Target 6–12 NEW notes per numbered chapter (ch01 may take up to 14; the
  short afterwords ch25/ch26 need at most 1–3 more, they are already dense
  with notes). Whole-book target ≈ 230–300 total. Do not pad: every note must
  answer something a curious non-specialist would actually wonder.
- The three kinds that earn a note (CLAUDE.md): (1) references — people,
  offices, institutions, places, buildings, objects, customs, festivals,
  foods, garments, texts, with real historical content, stating corroborated /
  uncorroborated / contradicted where the book meets the record; (2) texture
  lost in translation — idioms with their literal image, classical allusions,
  register shifts, names whose literal meaning matters; (3) genuine
  translation uncertainty — the readings considered.
- 2–4 sentences each. Give the Chinese (literal CJK is fine) for key terms.
  Fact-check the claims you are least sure of (Wikipedia, Baidu Baike,
  academic sources; NEVER an AI-generated reference); when you cannot
  corroborate, say so in the note.

### 4.2 First-appearance protocol (the one rule that prevents rework)

A subject gets its note at its FIRST appearance in the BOOK. Before writing a
note in chNN:
1. `grep -l "<term>" out/ch0*_reading.md out/ch1*_reading.md …` restricted to
   chapters BEFORE yours — if it appears earlier, the note belongs there
   (add it there if you are doing that chapter in this batch; otherwise skip
   and log it).
2. Check the 86 existing subjects:
   `python3 -c "import json,re;n=json.load(open('notes.json'));[print(c,'|',e['anchor'][:60],'|',re.sub('<[^>]+>','',e['note'])[:90]) for c in sorted(n) for e in n[c]]"`
   Never duplicate or half-overlap one (An Lushan ch16, He Zhizhang ch02, the
   Türk khaganate/Ozmish ch01/ch02, the aphids ch09, the full list via the
   command).

### 4.3 The glossary is your quarry

glossary.json rows carry attestations and mini-histories that were researched
per batch. Mine them: for each chapter, list glossary terms whose English
rendering first occurs in that chapter and whose row has a substantive
`note` field — those are pre-researched footnote candidates:

```python
import json, re, glob
g = json.load(open('glossary.json')); files = sorted(glob.glob('out/ch*_reading.md'))
texts = {f[4:8]: open(f).read() for f in files}
order = sorted(texts)
for sec, entries in g.items():
    if sec.startswith('_'): continue
    for zh, rec in entries.items():
        en = rec.get('en'); note = rec.get('note','')
        if not en or len(note) < 40: continue
        first = next((c for c in order if en in texts[c]), None)
        if first: print(first, '|', en, '|', zh, '|', note[:100])
```

Sort that output by chapter and you have most of the per-chapter candidate
list already researched. The footnote should SAY MORE than the glossary row
(the glossary states the rendering; the note tells the reader what the thing
was) — do not just copy the row.

### 4.4 High-value subject bank (verify first appearance by grep; skip any
already noted)

The ward/curfew system as lived reality; the West Market and its
administration; travel passes (过所); the watchtower signal system (望楼);
the Jing'an Bureau as the novel's invention; the "great archive method"
(大案牍术) as the novel's data-driven conceit; the buliang-ren (不良人) and
their chief; the Lüben Guards (旅贲军); the Right Xiaowei Guard; the Longwu
Army; the shouzhuo-lang (守捉郎); Zoroastrianism in Tang Chang'an (祆教, the
sabao 萨保); Nestorian Christianity and Yisi (景教/伊斯 — the Stele note lives
at ch25, an earlier who-is-Yisi note may still be due at his first scene);
Ge Lao and the underground city; rock-oil/petroleum (石脂) and Meng Huo Lei
(猛火雷); the Lantern Festival and the great lantern wheel (太上玄元灯楼);
the ba-deng procession (拔灯); Chang'an street food (水盆羊肉, 火晶柿子,
三勒浆, mint leaf 薄荷叶); the fish-pouch and robe-color rank system; the
clepsydra and time-keeping (the "mark"/刻); the sand table; Yan Zhenqing;
Sun Simiao the Medicine King; the novel's renaming convention for real
figures (何执正=贺知章, 林九郎=李林甫, 郭利仕=高力士 — ONE note at first
occurrence of the pattern, likely ch02, stating the novel's practice and the
historical originals; check what the He Zhizhang ch02 note already says);
Li Bi the historical statesman vs. the novel's young Daoist; Wang Zhongsi;
Wang Yunxiu; Yuan Zai; Cen Shen the poet as a character; 杨太真/the Precious
Consort; the Crown Prince and the Li Linfu succession struggle; Qujiang Pool;
the Leyou Plateau; Xingqing Palace and the Hall of Blazing Light; the
Vermilion Bird Avenue; Chang'an's canals (漕渠); Big Wild Goose Pagoda (noted
ch25? — grep). Anything in this bank that greps to a chapter in your batch and
is unnoted is close to a free note via §4.3.

### 4.5 Anchors and integration

- Anchor = short verbatim phrase copied from the FINAL edited English at the
  subject's first occurrence, distinctive enough to be unique or
  first-occurrence-safe (the builder attaches at the first match; multiple
  occurrences are fine and expected for recurring names).
- Note body = XHTML string: `<i>` for emphasis/titles; numeric character
  references for typographic punctuation (`&#8212;` em dash, `&#160;` nbsp,
  `&#215;` ×); literal CJK welcome; NEVER named entities (`&mdash;` breaks
  the XML build).
- Integrate by loading notes.json in Python (`json.load` → append to the
  unit's list → `json.dump(..., ensure_ascii=False, indent=2)`), never by
  hand-editing braces. Order within a unit's list does not matter (numbering
  is assigned by anchor position in reading order), but keep the list roughly
  in narrative order for maintainability.
- After integration: rebuild. The builder REFUSES on any unmatched anchor and
  qa_epub.py checks refs == bodies == backlinks and sequential numbering, so
  a green build is the proof.

---

## 5. Verse ({p}) — small, do it during the read

While reading each chapter (§3.4), when a paragraph is ENTIRELY a set-off
poem, song, chant, or inscription being recited or read out (not a couplet
quoted inside a prose sentence), prefix it `{p} `. Candidates to check while
you pass: the Ode to the Willow moment (ch24 — the couplet is quoted inline
in prose; probably stays prose), the Türk songs/oaths, the lantern-festival
verses, any 诗/歌行 recitation set as its own paragraph in the zh. Expect
maybe 5–15 across the whole book. When in doubt, leave it prose — a wrong
{p} is worse than a missing one.

---

## 6. Batch structure (≤3 batches; 2 is the plan)

Run each batch in its own chat, named `Chang'an R1` / `Chang'an R2`
(continuing the naming convention in CLAUDE.md). Both batches follow §3.4
per chapter, then close with the batch checklist below.

**Why not subagent fan-out:** the first attempt burned the session limit on
8 parallel agents that each re-read all the shared context. Do the work
IN-SESSION, sequentially, chapter by chapter. It is cheaper and the quality
is easier to keep uniform. Token economy: read zh+en in aligned chunks once,
edit with small targeted calls, never re-read a file you just edited, verify
per chapter, keep notes-in-progress in one scratch buffer per batch.

### Batch R1 — ch01–ch13 (~half the book)

1. Chapters ch01…ch13 per §3.4 (polish + collect notes + {p}), verify_unit
   after each.
2. Integrate R1's new notes into notes.json (§4.5); re-run
   `python3 scripts/smart_quotes.py` (normalizes any stray straight quote
   typed during editing; expected warnings per §2.6).
3. Rebuild + QA:
   `python3 scripts/build_reading_epub.py "out/The Longest Day in Chang'an.epub"`
   then `python3 scripts/qa_epub.py "out/The Longest Day in Chang'an.epub"`
   until PASS.
4. Record in PROGRESS.md (touches per chapter, fidelity fixes, notes added,
   noise.txt changes); append a dated entry to CHANGELOG.md listing files
   touched. Do NOT modify HANDOFF.md (a Stop hook demands kickoff-block
   pasting when HANDOFF.md is in a commit; this plan replaces that flow —
   batch state lives in PROGRESS.md/CHANGELOG.md and §7's checklist).
5. Commit with a clear message; `git push -u origin
   claude/the-longest-day-in-changan` (retry per CLAUDE.md git rules).
6. ATTACH the rebuilt EPUB in chat (CLAUDE.md rule 1 — the file is the
   deliverable, every batch).

### Batch R2 — ch14–ch26 + whole-book close

1. Chapters ch14…ch24 per §3.4; then ch25/ch26 (essays — polish for the
   author's own expository, personal voice; first-person in ch26; NO
   thriller-izing, no datelines/vignettes exist there), verify_unit after each.
2. Integrate R2 notes; smart_quotes pass; any first-appearance notes that R1
   discovered belong in R2 chapters get written now (check the R1 log).
3. Whole-book consistency sweep: grep-audit a handful of glossary renderings
   that edits could have grazed (spot-check ~20 high-frequency terms:
   `grep -c "the Sage" out/ch*_reading.md` style); re-run verify_unit on ALL
   26 units; rebuild; qa_epub PASS across the full spine (refs == bodies ==
   backlinks, numbering sequential).
4. Final numbers: report total note count, per-chapter touch counts, fidelity
   fixes, in PROGRESS.md; dated CHANGELOG.md entry; update COMPLETION.md's
   note-count line to the new totals with a one-paragraph revision addendum.
5. Commit, push, ATTACH the final EPUB in chat.

### Contingency R3

Only if R2 runs out of room: R2 stops at a chapter boundary, commits, pushes,
delivers the current EPUB, and records the resume point in PROGRESS.md
("polished through chNN; notes integrated through chNN"). R3 picks up from
the recorded point and runs the close-out (§6-R2 steps 3–5).

---

## 7. Batch-exit checklist (both batches; copy into the batch log)

- [ ] Every chapter in scope swept against its zh file, per §3.4
- [ ] verify_unit PASS for every unit in scope (and, in R2, all 26)
- [ ] New notes integrated; no orphan anchors (build succeeds)
- [ ] smart_quotes.py re-run; warnings only at known-legit continuation lines
- [ ] qa_epub.py PASS
- [ ] PROGRESS.md + CHANGELOG.md updated (files touched, counts, fixes)
- [ ] HANDOFF.md NOT in the commit
- [ ] Committed and pushed to claude/the-longest-day-in-changan (only)
- [ ] EPUB attached in chat

---

## 8. Kickoff messages (paste one per batch chat, verbatim)

### R1

```
Chang'an R1
Read CLAUDE.md in full (the commissioner's rules at the top are non-negotiable),
then REVISION_PLAN.md in full — it is the operating document for this batch and
overrides HANDOFF.md, which describes the pre-revision state. We are executing
the register-polish + footnote-expansion revision of the finished translation
of 长安十二时辰 (The Longest Day in Chang'an); the deliverable is
out/The Longest Day in Chang'an.epub, attached in chat at batch end.

Do Batch R1 = chapters ch01 through ch13, end to end, per REVISION_PLAN.md:
for each chapter, the §3.4 method (aligned zh/en read, conservative register
polish per §3.2/§3.3, collect footnotes per §4 and verse per §5, verify_unit
after each chapter); then integrate the new notes, re-run smart_quotes.py,
rebuild, qa_epub until PASS, update PROGRESS.md and CHANGELOG.md (not
HANDOFF.md), commit, push to claude/the-longest-day-in-changan, and attach the
EPUB in chat. NOTE: data/src/ and data/figs/ are gitignored; if a script needs
them, run `python3 scripts/ingest_epub.py source.epub` first — but this batch
should not need them (data/zh/ is committed and is the alignment source).
ch01/ch04/ch05/ch06/ch07 are partially polished already — sweep them fully
anyway. Work in-session, sequentially; do NOT fan out subagents. Do not pause
for approval mid-batch. Never invent bridging text; fix fidelity drift to
match the zh and log it.
```

### R2

```
Chang'an R2
Read CLAUDE.md in full (the commissioner's rules at the top are non-negotiable),
then REVISION_PLAN.md in full — it is the operating document for this batch and
overrides HANDOFF.md. Batch R1 (ch01–ch13) is done and committed; check
PROGRESS.md's R1 entry for any first-appearance notes R1 deferred to later
chapters, and do them in their chapters this batch.

Do Batch R2 = chapters ch14 through ch26 plus the whole-book close, per
REVISION_PLAN.md §6-R2: polish ch14–ch24 per §3.4; ch25/ch26 are the author's
afterwords — essays in his own voice, polish accordingly; verify_unit after
each; integrate notes; smart_quotes.py; whole-book consistency sweep and
verify_unit on ALL 26 units; rebuild; qa_epub PASS; final counts into
PROGRESS.md, dated CHANGELOG.md entry, revision addendum in COMPLETION.md (do
not touch HANDOFF.md); commit, push to claude/the-longest-day-in-changan, and
attach the final EPUB in chat. If the session cannot finish, stop at a chapter
boundary, commit/push/deliver, and record the exact resume point in
PROGRESS.md per §6-R3. Do not pause for approval mid-batch. Never invent
bridging text; fix fidelity drift to match the zh and log it.
```
