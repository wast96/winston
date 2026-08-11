# HANDOFF — Burn, O Sword! (燃えよ剣), Shiba Ryōtarō

This file is the baton. A fresh session with no memory reads it and starts
immediately. **It is the ARCHIVE of the kickoff message, not its delivery:
every batch ends with this file's kickoff block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count.** Rewrite it
at the end of every batch; always keep the paste-ready kickoff message below as
its first section.

## Message to paste into the next chat

```
Burn, O Sword! B01

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating Burn, O Sword! (燃えよ剣) by Shiba Ryōtarō, from a Japanese digital EPUB (source.epub), into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/burn-o-sword; expect the harness to open you on a stray per-task branch and consolidate per CLAUDE.md rule 2. Deliverable out/burn-o-sword.epub.

Step 0 (ingest + survey) is DONE and committed: book.json holds 68 titled novel chapters + 3 back-matter units; the skeleton EPUB, qa_epub, and epubcheck are green. The ingest is Japanese-aware: run ./setup.sh, and if data/src/ is empty re-run scripts/ingest_epub.py source.epub (it strips furigana, substitutes the 8 gaiji via data/gaiji_map.json, and writes reference/furigana_readings.tsv). No source-note stream (the novel has no author footnotes).

Do Batch 1 = ch01 only (女の夜市 / "The Women's Night Market"), end to end per the CLAUDE.md pipeline, and STOP at the voice gate (Step 0c). Do NOT go on to Batch 2, and do NOT paste a next-batch kickoff; Batch 1 ends by presenting the chapter for the voice-gate approval instead.
1. Read ch01 from data/src/05_part0003.txt. Fix any extractor-split paragraphs; recover set-off formatting with apply_format_markers.py where the source HTML encodes it (kaiti vignettes, centered-rule scene breaks, verse). This is a vertical-rl Japanese novel; scene breaks are frequent.
2. Translate to the register in CLAUDE.md (a literary Bakumatsu novel; the falsifiable voice test is "could a good contemporary translator of Shiba have written it"). Names in Japanese order, surname first (Hijikata Toshizō), macrons for long vowels (Toshizō, Kondō); CONSULT reference/furigana_readings.tsv for name/word readings before romanizing anything. Write a voice sheet into HANDOFF for every major character at first appearance; flag main cast principal: true in glossary.json. Never invent bridging text; render digitization glitches to plain sense and LIST them in PROGRESS.md; the source's own errors stay visible and footnoted. authority.json is the China shelf and decides nothing here, but still feed decided renderings back.
3. Write out/ch01_en.json (one English paragraph per source line) and run make_bilingual.py ch01 ...; then verify_unit.py ch01 --noise data/noise.txt; check_align.py and check_content.py; verify the chapter TAIL against the source explicitly.
4. Footnotes per the reader model in CLAUDE.md (a Westerner with no Japanese history; sweep material culture, social structure, customs/belief, institutions/money; early chapters usually want 8-15, first-appearance discipline, NOT-re-noted ledger) via apparatus_merge.py, check_apparatus.py clean. Glossary rows with attestation. Any figure from data/figs/ with a translated caption and real alt text.
5. Rebuild the EPUB, qa_epub.py until green, epubcheck if available; record all check results in PROGRESS.md; commit.
6. Present ch01 for the voice gate: attach the rebuilt EPUB AND paste the ch01 reading text in the chat, and STOP for approval of voice, note density, and formatting. On approval it becomes the frozen register reference for check_register.py --ref.

Cite chapters and sections, never pages. Do not pause for approval mid-batch (only at the voice gate at the end).
```

## What is DONE (do not redo)

- Step 0 (ingest + survey), committed. book.json: 68 novel chapters
  (ch01-ch68, titled/unnumbered) + 3 back-matter units (ch69 Afterword,
  ch70 Harada Masato film commentary, ch71 About the Author). Skeleton EPUB
  builds; qa_epub PASS; epubcheck 0/0; checker tests green. Cover reused
  byte-identical. Continuous note number so far: 0.

## Tooling in place (do not revert)

- ingest_epub.py made Japanese-aware: strips <rt>/<rp> furigana (was
  interleaving readings into the base text), substitutes <img class=gaiji>
  via data/gaiji_map.json, counts kana as well as kanji, and dumps
  reference/furigana_readings.tsv (2,025 word/name readings).
- data/gaiji_map.json: 遼 茨 頤 葛 芦, plus レ (kaeriten) and 㝎 (Nosada
  variant of 定, discussed in ch16); embed0008 = publisher logo -> dropped.

## Renderings settled this batch / carry-forward

- Title: "Burn, O Sword!" (with the exclamation). Author: Shiba Ryōtarō.
- Name policy: Japanese order (surname first), macrons for long vowels.
- Nothing else decided yet; glossary.json is empty. ch01 will seed the
  principal cast (Hijikata Toshizō, and whoever else appears).

## Voice sheets (one per major character, written at first appearance)

- (none yet; write them in Batch 1 as characters appear.)

## Where the book stands

- Nothing translated yet. Batch 1 = ch01, the opening (the Hino years,
  before Kyoto).

## What is NEXT

- Batch 1 = ch01 (voice gate). Planned batches after approval (~5-6
  chapters each, final batch light): B02 ch02-07, B03 ch08-13, B04 ch14-18,
  B05 ch19-23, B06 ch24-28, B07 ch29-33, B08 ch34-38, B09 ch39-43,
  B10 ch44-48, B11 ch49-53, B12 ch54-58, B13 ch59-63, B14 ch64-68,
  B15 ch69-71 back matter + whole-book reconciliation + COMPLETION.

## Open items for the read-through

- ch16 (和泉守兼定 / the 之定 signature, 㝎) will want a swordsmith note.
- Confirm romanization of minor Shinsengumi names against
  furigana_readings.tsv as they appear.

## Environment / traps state

- epubcheck available at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches).
- Source is vertical-rl Japanese; heavy furigana and 8 gaiji, all handled at
  ingest. data/src/ is gitignored (regenerable via ingest_epub.py).
- Stray harness branch claude/new-session-47px59 left in place (no unique
  work); all work is on claude/burn-o-sword.
