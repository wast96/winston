# HANDOFF, Burn, O Sword! (燃えよ剣), Shiba Ryōtarō

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery: every
batch ends with this file's kickoff block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count. Rewrite it at
the end of every batch; always keep the paste-ready kickoff below as its first
section.

## Message to paste into the next chat

```
Burn, O Sword! B02

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then STYLE.md, then book.json. We are translating Burn, O Sword! (燃えよ剣) by Shiba Ryōtarō from a Japanese digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/burn-o-sword; expect the harness to open you on a stray per-task branch and consolidate per CLAUDE.md rule 2. Deliverable out/burn-o-sword.epub.

Batch 1 (ch01) is DONE and APPROVED at the voice gate. ch01 is now the FROZEN register reference: reference/ch01_ref.md. Run ./setup.sh; if data/src/ is empty re-run scripts/ingest_epub.py source.epub (Japanese-aware: strips furigana, substitutes 8 gaiji, writes reference/furigana_readings.tsv). No source-note stream. Keep the source's own cover (data/figs/embed0009_HD.jpg), reused byte-identical, exactly as book.json already sets it; the commissioner likes it, do not change it.

Do Batch 2 = ch02 through ch07 (六車斬り / Cutting Down Muruma; 七里研之助 / Shichiri Kennosuke; わいわい天王 / The Waiwai Tennō; 分倍河原 / Bubaigawara; 月と泥 / The Moon and the Mud; 江戸道場 / The Edo Dōjō), end to end per the CLAUDE.md pipeline, RUN TO COMPLETION. There is no voice gate this batch (it is passed); do not stop mid-batch except for a genuine blocker or completion. For each chapter:
1. Read the unit from data/src/; build data/zh/<id>.txt (verbatim: "### <title>" then one body line per source paragraph). Fix any extractor splits. Recover scene breaks: in THIS source a run of TWO OR MORE consecutive blank paragraphs (<p><br/></p>) inside the body is a scene break; the single blank pair right after the chapter title is only the title/body separator, not a break. Place *** in the reading at those points.
2. Translate to the FROZEN ch01 register. Names Japanese order, surname first, macrons for long vowels; CONSULT reference/furigana_readings.tsv before romanizing ANY name or word, and consult glossary.json (then authority.json) first, feeding decided renderings back. Use the {j} display-join marker so a short quotation reads inline with its lead-in and attribution (keep a back-and-forth exchange as one paragraph per speaker turn). OBEY STYLE.md: at most one em dash (or one matched pair) per sentence, and never an idiom whose second sense the scene primes (the "make out" in the dark lesson). Write a voice sheet into HANDOFF for every major character at first appearance; flag main cast principal: true in glossary.json; read the last two pages of ch01's English before starting ch02 (batch-seam voice).
3. Write out/<id>_en.json (one English paragraph per source line) and run make_bilingual.py <id> data/src/<file>.txt "<title_en>" out/<id>_en.json; then verify_unit.py <id> --noise data/noise.txt; regenerate the check config with scripts/gen_check_config.py, then check_align.py <id> and check_content.py --config check_config.json and qc_entities.py out/<id>_bilingual.md glossary.json; verify each chapter TAIL against the source explicitly.
4. Footnotes per the reader model in CLAUDE.md (first-appearance discipline; keep the "NOT re-noted" ledger in PROGRESS.md; note MORE than the glossary row) via apparatus_merge.py, check_apparatus.py clean. Glossary rows with attestation status. Any figure from data/figs/ with a translated caption and real alt text.
5. After each chapter run check_register.py --ref reference/ch01_ref.md out/<id>_reading.md (exempt registers per references/register-drift.md); record the result in PROGRESS.md. Fact-check historical claims against real scholarship (never LLM-sourced), verdict in the note.
6. Rebuild the EPUB, qa_epub.py until green, epubcheck if available; record ALL check results and EVERY digitization glitch in PROGRESS.md; update HANDOFF.md; commit and push to claude/burn-o-sword.

End the batch with BOTH chat deliverables (CLAUDE.md rule 1, enforced by the Stop hook): the built EPUB ATTACHED in the chat AND the Batch 3 kickoff PASTED VERBATIM in a fenced code block. Batch 3 = ch08 through ch13.

Cite chapters and sections, never pages.
```

## What is DONE (do not redo)

- Step 0 (ingest + survey), committed. book.json: 68 novel chapters (ch01 to
  ch68) + 3 back-matter units.
- B01 = ch01 「女の夜市」 / "The Women's Night Market", COMPLETE and APPROVED at
  the voice gate. 160 source paragraphs rendered as 124 display paragraphs (via
  the {j} inline-dialogue join); 15 footnotes (continuous 1 to 15); two scene
  breaks; Principal Characters page seeded. All checks green; qa_epub PASS;
  epubcheck 0/0. ch01 FROZEN as the register reference: reference/ch01_ref.md
  (em-dash baseline 12.5/1k, dialogue contractions 24.9/1k). Continuous note
  number so far: 15.

## Tooling in place (do NOT revert)

- ingest_epub.py: Japanese-aware (furigana strip, 8 gaiji via
  data/gaiji_map.json, dumps reference/furigana_readings.tsv). From Step 0.
- data/gaiji_map.json: 遼 茨 頤 葛 芦, plus レ (kaeriten) and 㝎 (之定 variant).
- scripts/check_align.py (B01): scene-break aware; counts source kanji+kana,
  not kanji only.
- scripts/check_content.py (B01): skips '_'-prefixed / non-dict glossary
  sections; scene-break aware.
- scripts/gen_check_config.py (B01, NEW): writes check_config.json for
  check_structure.py / check_content.py. RUN IT each batch before those checks.
- data/noise.txt (B01): Japanese name/idiom numeral rules (歳三, 彦五郎, 喜六,
  六社, 八王子, 百姓, 二重). Add more as numbered names appear.
- DISPLAY JOIN MARKER {j} (B01, whole-book): a reading line prefixed "{j} " is
  merged onto the preceding display paragraph at BUILD time
  (build_reading_epub.py collapsed(), em-dash aware), so a quotation the source
  sets as its own paragraph reads inline. Reading file keeps one line per source
  paragraph, so parity/number/entity checks are untouched. All checks strip {j}.
- STYLE.md (B01, NEW): the house style sheet, seeded by the voice-gate
  corrections (em-dash budget; scene-primed idioms). READ IT each batch; add to
  it when the commissioner corrects a line.
- reference/ch01_ref.md (B01, NEW): the FROZEN register reference for
  check_register.py --ref. Do not edit.

## Voice sheets (one per major character, written at first appearance)

- NARRATOR: third person, wry and knowing, fond of the aside ("or so the story
  goes," "incidentally") and the forward glance to events years ahead. Long
  descriptive sentences alternating with very short flat ones ("It was hotter
  than most years." "He was a dandy."). Period texture, never antiquarian.
- HIJIKATA TOSHIZŌ ("Toshi"): the hero, 22 here. Rough Bushū farm dialect off
  guard, contracted and blunt ("What're we gonna do about that bastard?"). Cool,
  laconic, a dandy, one-word lines ("Before long."). His speech CONTRACTS.
- KONDŌ ISAMI: framing lines only so far, same Bushū dialect ("Toshi."). Warm,
  plain. (Fuller sheet when he returns in the coming chapters.)
- KOZAKURA: shrine maiden, Toshizō's casual lover; pert, teasing, colloquial.
  Contracts.
- OSAE / the woman in the dark: soft, courtly, UNCONTRACTED, the ends of her
  words gentle ("I cannot say it."). Her formality is the point; never contract
  her. Likely Shiba's invention.

## Renderings settled this batch / carry-forward

- Title "Burn, O Sword!"; author Shiba Ryōtarō. Names Japanese order, macrons.
- One rendering per referent, all in glossary.json (people, places,
  organizations, terms). See PROGRESS.md B01 for the full list.
- Style calls: 分際 rendered "station"; 浄闇 "sacred darkness"; 六社明神
  "Rokusha Myōjin" (Ōkunitama gloss at first mention); 万燈 "the ten thousand
  lanterns" (keeps the numeral); 傍点 emphasis rendered as plain English.
- COVER: keep the source's own cover (data/figs/embed0009_HD.jpg), reused
  byte-identical, exactly as book.json sets it. The commissioner likes it. Do
  NOT replace or re-encode it.
- Provisional, worth a second look: Kajikawa Keiji, Senjubō, Kozakura, Osae.

## Where the book stands (story)

- ch01 is the overture, 1857, before Kyoto and the corps. It establishes
  Toshizō (rakish, class-obsessed, dangerous) and plants the woman in the dark
  whose Norishige dagger and Saruwatari crest close the chapter, a thread the
  novel picks up later.

## What is NEXT

- B02 = ch02 to ch07 (kickoff above). Planned after: B03 ch08-13, B04 ch14-18,
  B05 ch19-23, B06 ch24-28, B07 ch29-33, B08 ch34-38, B09 ch39-43, B10 ch44-48,
  B11 ch49-53, B12 ch54-58, B13 ch59-63, B14 ch64-68, B15 ch69-71 back matter +
  whole-book reconciliation + COMPLETION.

## Open items for the read-through

- ch16 (和泉守兼定 / the 之定 signature, 㝎) will want a swordsmith note.
- Confirm minor Shinsengumi and place-name readings against
  reference/furigana_readings.tsv as they appear.

## Environment / traps state

- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches).
- data/src/ and data/src_epub/ are gitignored (regenerate via ingest if empty).
- Scene-break convention: two or more consecutive blank <p><br/></p> inside the
  body = a break; the single pair after the title is only the title/body
  separator. The China-template apply_format_markers.py does NOT parse this
  source's plain <p> HTML, so scene breaks are placed by reading the source.
- Known failing test, EXPECTED: tests/run_tests.py reports "hook stands down on
  template stub" FAIL. It only passes when HANDOFF.md holds the template's
  placeholder kickoff; a real book kickoff makes the guard enforce, as intended.
  Not a translation gate. All other tests pass.
- All work is on branch claude/burn-o-sword.
