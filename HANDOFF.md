# HANDOFF — Zhou Enlai: Commander of the Hidden Front

The book is COMPLETE and the register pass (R1-R5) is CLOSED. We are now in the
**footnote-density pass** (FOOTNOTE_PASS.md). FN1 (ch00-ch05) is done; **FN2
(ch06-ch11) is next.** One batch = one fresh chat, started by pasting the block
below. FN1 stopped at a light annotation-depth gate for the commissioner; do
NOT begin FN2 until the commissioner has seen FN1's density and approved the
depth.

## Message to paste into the next chat

```
Zhou Enlai FN2 (footnote-density pass)

Read CLAUDE.md, then FOOTNOTE_PASS.md (it governs this pass), then STYLE.md ("Apparatus" and the partisan-source discipline), then this HANDOFF and PROGRESS.md's FN1 section. Branch claude/zhou-enlai only; fold any stray branch per CLAUDE.md rule 2. Content is FROZEN: this pass ADDS and enriches footnotes only, no prose/number/name/paragraph change. Notes are authored as a JSON file and merged with scripts/apparatus_merge.py (never a heredoc); anchors are verbatim UNIQUE substrings of out/<id>_reading.md; note bodies are XHTML with numeric character references only; people notes carry no hanzi, term/place/event notes carry glossary-verified hanzi decoded and checked; cite printed folios where a note cites a page; never invent; fact-check every claim against real scholarship (Wikipedia/Baidu Baike/academic, NEVER Grok/Grokipedia/AI) with the verdict stated in the note. Use scripts/fa_check.py (first-appearance grep across notes.json + reading files) before every note and scripts/gloss_hanzi.py for hanzi. data/zh is a parity scaffold not needed for a notes-only pass; do not regenerate it unless a check requires it.

Do batch FN2 = greatly increase footnote density on ch06-ch11 (Yang Dengying and the first counter-espionage tie; the tiger's den; Fengtian; the Action Section and the Red Squad; the Avenue Joffre gunfights) per FOOTNOTE_PASS.md sections 2-6: sweep every chapter for people, places, events, institutions/offices/ranks/units, terms and period vocabulary, and allusions/idioms/quotations, and annotate every instance a non-specialist Western reader would miss AT ITS FIRST appearance book-wide. Density is coverage, not quota: every note carries real checked content and answers a real reader question; add nothing just to add it. Run the first-appearance check before every note and keep the "NOT re-noted" list in PROGRESS. RECONCILE the FN1-logged item: trim the ch07 Liu Bocheng note to a cross-reference to the new ch01 first-appearance note. Then rebuild, check_apparatus.py, qa_epub (epubcheck if installed), PROGRESS + CHANGELOG, commit, push.

End with the rebuilt EPUB attached in chat AND the FN3 kickoff pasted verbatim in a fenced block (same form as this one, ch12-ch17). Do not pause for approval mid-batch.
```

## What is DONE (do not redo)

- Translation of all 28 units (ch00-ch27); register pass R1-R5 (see COMPLETION.md).
- **FN1 footnote-density pass, ch00-ch05: +46 notes (339 -> 385; ch00-ch05
  109 -> 155).** Per-unit counts, the full "NOT re-noted" list, the fact-check
  verdicts, and the reconciliation item are in PROGRESS.md's FN1 section.
  Merged via `data/fn1_notes_a.json` (ch00-01) and `data/fn1_notes_b.json`
  (ch02-05).

## Carry-forward for the footnote pass

- **First-appearance discipline is the main guard against redundancy.** Before
  every note run `python3 scripts/fa_check.py "Subject"`: it lists which reading
  files mention it (in order) and any notes.json anchor/body that already covers
  it. Note at the FIRST appearance book-wide; cross-reference, never re-note.
- **RECONCILE (FN2):** Liu Bocheng has a new first-appearance ID at ch01
  (Nanchang) and an existing episode note at ch07 — trim the ch07 note to a
  cross-reference ("see the note at chapter 1"). No other FN1 addition has a
  ch06+ duplicate.
- **Pre-existing later-chapter notes whose subject first appears in ch06-ch11**
  will surface in FN2; check each with fa_check and place the ID at first
  appearance, trimming the later note. Known: Du Yuesheng (full at ch14, first
  appears ch04 — glancing, left un-noted in FN1; if ch06-ch11 has a substantive
  first appearance, note there); Yang Dengying (Bao Junfu) is a subject of ch06,
  already noted at ch04's "first to discover... Yang Dengying" — enrich at ch06
  only if the ch04 note is insufficient, else cross-ref.
- **Hanzi:** people notes carry none. Term/org/place/event notes carry hanzi as
  numeric character references (`&#20116;...`), each decoded with
  `python3 -c "import html;print(html.unescape('...'))"` and cross-checked
  against `scripts/gloss_hanzi.py` output or the scan. Never hand-type a glyph
  you have not verified. Merge validates for U+FFFD and named entities.
- **Voice of the notes:** concise, one referent per note; dates; role in the
  1927-35 period AND later fate/how they died; verdict "(Corroborated.)" or a
  graded claim. Match the existing note bodies (see ch00-ch05 for the model).

## Do not revert (accumulated tooling)

- `scripts/fa_check.py` (first-appearance grep) and `scripts/gloss_hanzi.py`
  (glossary hanzi reverse-lookup) — added in FN1; keep for every FN batch.
- `data/ocr_fixes.json`; `scripts/recovery/` (b01-b14 + r5/date generators);
  `data/noise.txt` (extend, never prune); `data/check_config.json`; builder
  invariants (pending-aware then cleaned TOC; note pop-ups with endnotes
  fallback; refusal to build on an unmatched anchor or unplaced figure;
  byte-identical cover copy; render-layer smart quotes).

## State / environment

- Deliverable: `out/zhou-enlai.epub` (committed with `git add -f` on
  `claude/zhou-enlai`). 28/28 chapters, **385 notes**, 36 figures, 496
  pagebreaks. qa_epub PASS; epubcheck 5.1.0 0/0/0.
- Ledgers: `glossary.json` (847 rows), `notes.json` (385), `figures.json`,
  `book.json`, `authority.json`; `out/term_ledger.md` and `out/deep_audit.md`
  are from the register close (refresh term_ledger only at FN5).
- `data/zh` is absent on a fresh checkout (untracked/regenerable) and was NOT
  regenerated for FN1 (parity scaffold, not needed for a notes-only pass;
  rationale in PROGRESS.md FN1). Regenerate per `scripts/recovery/README.md`
  only if a later batch needs qc_entities/parity.
- Body offset constant 44 (printed = PDF - 44). `OMP_THREAD_LIMIT=1` for
  tesseract; `pgrep -c tesseract` must read 0 after a run. One pre-existing
  failing regression test ("hook stands down on template stub"), template
  maintenance only, unrelated to the book.

## Environment / rebuild from clean checkout

1. `./setup.sh`
2. `python3 scripts/build_reading_epub.py`
3. `python3 scripts/qa_epub.py`
4. `java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/zhou-enlai.epub`
(A notes-only FN batch does not need `data/zh`; regenerate it only if a check
that reads the source requires it.)
