# HANDOFF — A Thousand Li of Rivers and Mountains (千里江山图), Sun Ganlu

The book is fully translated AND the four-round annotation retrofit is COMPLETE.
All 37 units are translated, annotated (338 footnotes), and built into one
cumulative, fully navigable EPUB; `qa_epub.py` is green. There is no next round.
The full completion report is in **COMPLETION.md**; the round-by-round record is
in **PROGRESS.md**.

(Obeys CLAUDE.md rule 6: no em dashes in this file's prose.)

## Status: DONE

- Whole book: 37 units translated, cover + front/back matter, full hyperlinked
  TOC, colophon, scene typography. `qa_epub` PASS.
- Retrofit Step 0: doctrine upgraded to v2.4 (CLAUDE.md, styles/, STYLE.md +
  STYLE.local.md, shared scripts). book.json carries deliverable/source_language/
  genre.
- Retrofit R1 = ch02-ch10: +79 notes (217 -> 296). Tier A in range folded.
- Retrofit R2 = ch11-ch19: +23 notes (296 -> 319). Tier A folded.
- Retrofit R3 = ch20-ch28: +13 notes and 1 relocation (319 -> 331). Tier A folded.
- Retrofit R4 = ch29-ch37 (FINAL): +7 notes incl. a ch13 first-appearance
  reconciliation note (331 -> 338). Tier A folded (the big ch37 date job; the last
  吴淞口 reading strays at ch34/ch35; 白区 -> the White areas in note bodies).
  Whole-book reconciliation, final QA, and COMPLETION.md done. See PROGRESS.md for
  the full R4 record and the honest density note.

## Deliverable

`book.json` "deliverable" = `out/A Thousand Li of Rivers and Mountains.epub`
(validate with `stamp_deliverable.py --check`; stamp a round copy with
`stamp_deliverable.py R<n>`). The old `out/thousand-li.epub` was the pre-retrofit
snapshot. The final-named EPUB is force-added on completion (out/*.epub is
gitignored).

## If corrections come in later

The book is shelf-ready; further work is the CORRECTIONS.md workflow (GLOBAL
cascades via glossary/style + grep-driven edit across all built units, then
rebuild + full QA; LOCAL is a one-spot fix). After a corrections batch: rebuild,
run `qa_epub`, list every file touched, append a dated CHANGELOG.md entry.

## Tooling / traps (for any future corrections pass)

- notes.json is written at indent=2 (apply_edits.py's format). Do not hand-reformat.
- apply_edits.py OLD/NEW window bleed: put TWO blank lines between adjacent TOUCH /
  NOTE-ANCHOR blocks; verify the parse before applying.
- Note bodies: numeric character references only, never named entities (&amp; -> &#38;).
- apply_edits.py cannot edit an EXISTING note body; for date/regloss inside bodies
  use a small guarded script (see scripts/patch_note_bodies_r{2,3,4}.py) with
  json.load/json.dump, ensure_ascii=False, indent=2 (never a heredoc).
- conform_r4.py is the pattern for reading/en.json global format conformances whose
  target lines are not unique (e.g. the seven identical ch37 Longhua date lines).
- A note CAN sit on a scenes.json dateline line (the builder inserts the marker
  inside the centered dateline).
- data/src/ is gitignored; recreate with scripts/ingest_epub.py source.epub.
- check_numbers.py needs a bilingual (out/<id>_bilingual.md, gitignored); regenerate
  with make_bilingual.py <id> data/src/<file>.txt "<title>" out/<id>_en.json
  (ch37 via assemble_ch37.py, two source files -> ch37a/ch37b_en.json).
- book.json is the LOGICAL structure. ch01 is an epigraph (no notes). ch37 is one
  chapter with two sections (ch37s01/ch37s02) from two source files.
