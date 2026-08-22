# HANDOFF — Chen Yangshan: Hero of the Secret War (秘战英雄陈养山)

## THE BOOK IS COMPLETE; a REVISION PASS is now IN PROGRESS

All 12 units are translated, annotated, built, and verified (COMPLETION.md is
the report). A post-completion register/style/apparatus pass (REVISION_PLAN.md)
is now running, scope **TIER 1+2** (tier 3 declined). Done so far: **R0**
(read-only calibration), **R1** (STYLE.local rebaseline rules + the ch02
exemplar, 26 prose edits + 4 note-date reformats), and **R2** (sweep ch01, ch03,
ch04: 23 prose edits + 2 anchor moves + 18 note-date reformats; see PROGRESS.md).
The ch02/R2 diffs are the calibration target. Next: **R3** (sweep ch05-ch11 +
the apparatus mechanics of plan sec.6).

## Message to paste into the next chat

```
Chen Yangshan REVISION R3 (sweep ch05-ch11 + apparatus)

Read: CLAUDE.md, REVISION_PLAN.md (self-contained; never read or pull from any
other branch), STYLE.local.md (now carries the approved TIER 1+2 rebaseline
rules), PROGRESS.md (the R1 ch02 and R2 ch01/ch03/ch04 diffs are the calibration
target). All work on claude/chen-yangshan. Approved scope: TIER 1+2 ONLY.

Sweep ch05, ch06, ch07, ch08, ch09, ch10, ch11 end to end per plan sec.5 with the
sec.2 verification, honouring the sec.3.3 KEEP list, at the ch02/R2 touch-rate
(most paragraphs LEAVE; a rewrite that only shuffles synonyms is itself a defect).
Apply the STYLE.local rebaseline rules per chapter: Politburo; White Terror;
litotes calques; the could-not-but/help formula; "Such was" (recast ONLY if the
read-aloud test fails, else leave); inversions; 等-tags (vary, no tag dominating,
not zero); one-after-another; the awkward "the X-ing of" nominalizations (leave
the idiomatic ones -- "the founding of", "the vetting of cadres", etc.); doubled
synonyms (collapse only true near-synonyms, keep real distinctions like
威逼利诱). HARD KEEPS this batch: the WHOLE ch07 obituary (悼词, zero register
edits); every {v} block (ch05 Wu Hao notice + two 1961 letters + Mao's directive
+ Guan Fushan recollection; ch08 letters); Chen's own posthumous ch08 writings
(the 13 precepts, the 36-item outline, his dry first person); all verse/couplets.
KNOWN-BENIGN: check_align flags ch05 布礼 ("Bolshevik greetings").

Edits via edits/<id>_edits.md + apply_edits.py, OLD occurring exactly once.
LESSON (R1/R2): before applying, check every edit's OLD against BOTH notes.json
anchors AND figures.json `before` anchors; ship a NOTE-ANCHOR pair for any note
anchor an edit breaks (a body 政治局->Politburo inside an anchor needs one);
never restructure anchored text for a mere tic; ch03/ch04 had no em-dashes, so
recast inversions WITHOUT introducing one unless the file already uses them.

Apparatus mechanics (plan sec.6), do these too:
  - Note-date reformats: reformat every D-Month-YYYY (and bare day-month) in the
    note bodies of ch00 (front matter) and ch05-ch11 to Month D, YYYY, via a json
    load/dump (ensure_ascii=False) -- values never change, order only. (ch01-ch04
    already done in R1/R2.) Also reformat the one glossary.json D-Month-YYYY row.
  - Principal Characters page, grow 3 -> ~15-20: in glossary.json flag the
    recurring cast with "principal": true + a one-line "cast" + "cast_order"
    (plan sec.6 lists the names: Chen Yangshan, Yun Daiying, He Long, Zhou Enlai,
    Chen Geng, Bao Junfu, Li Kenong, Kang Sheng, Gu Shunzhang, Pan Hannian, Zhang
    Suzhen, Chen Kehan, Wang Shiying, Xu Enzeng, Chiang Kai-shek, plus judgment
    picks Lu Nan, Wei Jian, Cheng Jianyu). Pure glossary edit, zero prose risk.
  - Translator's-note sentence: add ONE sentence stating that "our Party", the
    partisan epithets, and the celebratory register are the AUTHOR'S voice,
    preserved deliberately, with the fact-check verdicts in the notes.

Verify per plan sec.2: git diff --stat shows NO net line change on mechanical
chapters, grep the edit lists for digits (no numeral may change), typography
guard (no curly quotes/ellipsis introduced into out/*_reading.md), check_apparatus
clean, builder anchor-refusal backstop. Spot-audit 10% (min 10) of edited
paragraphs; KEEP-list diff sweep. Rebuild (build_reading_epub.py), qa_epub.py,
epubcheck 0/0/0 (keep the EPUB under 30 MiB; MAX_FIG_WIDTH=1000 must hold),
commit, push. Deliver the EPUB in chat and paste the R-final kickoff. Do not
pause for approval mid-batch.
```

## Revision-pass provenance (do not violate)

`REVISION_PLAN.md` is the operating document and it is SELF-CONTAINED: every
imported rule is reproduced there in full. **Do NOT fetch, read, or pull
anything from `claude/the-sword-roars` or any other branch; all work stays on
`claude/chen-yangshan`.** Where this file and the plan disagree, the plan wins.

Any further work is a **corrections pass**, not a batch: the commissioner reads
the EPUB and files items in `CORRECTIONS.md` (or pastes them in chat, and you
transcribe them there first). Follow the corrections workflow in CLAUDE.md —
global corrections cascade via a glossary/style change plus a grep-driven edit
across ALL built units including note and glossary bodies, then rebuild and full
QA; local corrections are a single-spot fix. A zero-item corrections pass is
still a clean-checkout regression run.

## Final state

- **12 of 12 units** (ch00 foreword; ch01-ch06; ch07-ch09 appendices I-III;
  ch10 references; ch11 afterword). 1,256 body paragraphs.
- **432 footnotes**, **78 figures**, **731 glossary referents** (52 provisional,
  all minor bit-part names).
- **Deliverable:** `out/chen-yangshan.epub` (committed with `git add -f`).
  qa_epub PASS (104 files, 432/432/432 notes resolve); epubcheck 5.1.0 0/0/0.
  Title page reads COMPLETE.
- **Ledgers current:** `notes.json`, `glossary.json`, `figures.json`, `book.json`,
  `authority.json` (fed this book's decided renderings). `out/term_ledger.md` and
  `out/deep_audit.md` rendered. `COMPLETION.md`, `PROGRESS.md`, `CHANGELOG.md`
  current.
- **Branch:** all work on `claude/chen-yangshan`.

## Do-not-revert (accumulated tooling, still in force)

- OCR body crop: `ocr_crop.py --lang chi_sim --psm 6 --left 0.045 --right 0.985
  --top 0.08 --running-head "秘战英雄陈养山"`, recto (PDF even) `--bottom 0.945`,
  verso (PDF odd) `--bottom 0.915`. Front-matter pages 7-8 use a different crop.
- Builder: section-nav omits pending sections; refuses on an unmatched note anchor
  or unplaced figure; figure `alt` carries no straight double quotes;
  `strip_runfoot` removes the verso book-title foot.
- `apparatus_merge` merges glossary rows into sections; **REPLACES a unit's
  figures wholesale** — for a chapter split across batches, always re-include the
  prior batch's figures or they are dropped silently (this bit ch02; recovered in
  B10). `data/zh` is gitignored and regenerated per unit; run per-unit checks with
  the scoped `data/check_config.<id>.json`.

## Environment notes for a future rebuild

- `./setup.sh` once; epubcheck at `/tmp/epubcheck-5.1.0/epubcheck.jar` (setup
  re-fetches on a fresh container). `OMP_THREAD_LIMIT=1` for tesseract.
- Rebuild: `python3 scripts/build_reading_epub.py`, `python3 scripts/qa_epub.py`,
  `java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/chen-yangshan.epub`.
- The setup.sh regression "hook stands down on template stub: FAIL" is benign
  (the fixture expects a placeholder HANDOFF; this one is a real/complete handoff).
