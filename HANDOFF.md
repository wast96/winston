# HANDOFF, Burn, O Sword! (燃えよ剣), Shiba Ryōtarō

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery: every
BATCH ends with its kickoff block pasted verbatim into the chat, alongside the
attached EPUB. Batch 1 is different: it ends at the VOICE GATE (Step 0c) and
does NOT issue a next-batch kickoff; it presents ch01 for approval instead.

## Message to paste into the next chat

Batch 1 is at the FIRST-CHAPTER VOICE GATE (Step 0c), waiting on the
commissioner. There is deliberately no next-batch kickoff here yet: ch01 is
presented in the chat (the reading text plus the attached EPUB) for a judgment
on voice, note density, and formatting. Nothing after ch01 should be translated
until that judgment comes back.

On approval, ch01 becomes the FROZEN reference for `check_register.py --ref`,
and the Batch 2 kickoff is written here and pasted into a fresh chat. Planned
Batch 2 scope (from the approved survey): B02 = ch02 through ch07 (six
chapters). If the commissioner asks for changes at the gate, apply them to ch01
first, rebuild, and re-present before freezing the reference.

## What is DONE (do not redo)

- Step 0 (ingest + survey), committed. book.json: 68 novel chapters (ch01 to
  ch68) + 3 back-matter units (ch69 Afterword, ch70 film commentary, ch71 About
  the Author). Skeleton EPUB, qa_epub, epubcheck all green.
- B01 = ch01 「女の夜市」 / "The Women's Night Market", COMPLETE and committed,
  awaiting the voice gate. 160 paragraphs, 15 footnotes (numbering 1 to 15), two
  scene breaks, Principal Characters page seeded. All checks green (see
  PROGRESS.md for the full list); qa_epub PASS; epubcheck 0/0. Continuous note
  number so far: 15.

## Tooling in place (do NOT revert)

- ingest_epub.py: Japanese-aware (strips furigana, substitutes 8 gaiji via
  data/gaiji_map.json, dumps reference/furigana_readings.tsv). From Step 0.
- data/gaiji_map.json: 遼 茨 頤 葛 芦, plus レ (kaeriten) and 㝎 (Nosada variant
  of 定). embed0008 = publisher logo, dropped. From Step 0.
- scripts/check_align.py (B01): scene-break/marker aware, and counts SOURCE
  characters as kanji+kana, not kanji only. The China-template version counted
  `***` as a paragraph and, counting only Han, gave a meaningless ratio on a
  Japanese source. Do not revert to Han-only.
- scripts/check_content.py (B01): skips `_`-prefixed / non-dict glossary
  sections (the `_about` string crashed it), and is scene-break aware.
- scripts/gen_check_config.py (B01, NEW): writes check_config.json (docs +
  sources for translated units) for check_structure.py and check_content.py.
  RUN IT at the start of every batch's check pass, before those two checks.
- data/noise.txt (B01): Japanese name/idiom numeral rules appended (歳三, 彦五郎,
  喜六, 六社, 八王子, 百姓, 二重). Do not delete; each is a name/idiom, not a
  real quantity. Add more as later chapters introduce numbered names.

## Voice sheets (one per major character, written at first appearance)

- NARRATOR: Shiba's characteristic voice, third person, wry and knowing, fond of
  the aside ("or so the story goes," "incidentally") and the forward glance to
  events years ahead (the Ikedaya, the Shinsengumi). Period texture kept, never
  antiquarian. Literary but plain; long descriptive sentences alternating with
  very short flat ones ("It was hotter than most years." "He was a dandy.").
- HIJIKATA TOSHIZŌ ("Toshi"): the hero, aged 22 here. Rough Bushū farm dialect
  when off guard, contracted and blunt ("What're we gonna do about that
  bastard?"; "None to be found?"). Cool, laconic, a dandy, given to one-word
  lines ("Before long."). Interior thoughts terse and appetitive. Not vulgar for
  its own sake; controlled menace. His speech CONTRACTS; keep it colloquial.
- KONDŌ ISAMI: appears only in the framing first lines, in the same Bushū
  dialect as Toshizō ("Toshi."). Warm, plain. (Fuller sheet when he returns.)
- KOZAKURA: shrine maiden, Toshizō's casual lover; pert, teasing, colloquial
  ("You, with this person?"; "You really lay with her?"). Contracts.
- OSAE / the woman in the dark: soft, courtly, uncontracted, the ends of her
  words gentle ("I cannot say it."; "It does not trouble me."). Her formality is
  the whole point of the scene and must NOT be contracted. Likely Shiba's
  invention.

## Renderings settled this batch / carry-forward

- Title "Burn, O Sword!"; author Shiba Ryōtarō. Names Japanese order, macrons.
- One rendering per referent, now in glossary.json: Hijikata Toshizō, Kondō
  Isami, Satō Hikogorō, Kozakura, Osae, Saruwatari, Kajikawa Keiji; Ishida
  village, Bushū Tama, Fuchū, Hachiōji, the Kōshū Highway, the Ōkunitama Shrine,
  Senjubō; the Shinsengumi; Ishida Powder; ri; village headman (nanushi).
- Style calls: 分際 rendered "station" throughout; 浄闇 "sacred darkness";
  六社明神 "Rokusha Myōjin" (with the Ōkunitama gloss at first mention); 万燈
  "the ten thousand lanterns" (keeps the numeral); 傍点 emphasis rendered as
  plain English, no marker.
- Uncertain / provisional (flagged in glossary, worth a second look): Kajikawa
  Keiji (given-name reading uncertain), Senjubō (from the source furigana),
  Kozakura and Osae (romanizations mine).

## Where the book stands (story)

- ch01 is the overture, set in 1857, before Kyoto and before the corps. It
  establishes Toshizō's character (rakish, class-obsessed, dangerous) and plants
  the woman-in-the-dark whose Norishige dagger and Saruwatari crest close the
  chapter, a thread the novel will pick up.

## What is NEXT

- The voice gate. On approval, freeze ch01 as the register reference and begin
  B02 = ch02 to ch07. Planned batches after that (about six chapters each, final
  batch light): B03 ch08-13, B04 ch14-18, B05 ch19-23, B06 ch24-28, B07 ch29-33,
  B08 ch34-38, B09 ch39-43, B10 ch44-48, B11 ch49-53, B12 ch54-58, B13 ch59-63,
  B14 ch64-68, B15 ch69-71 back matter + whole-book reconciliation + COMPLETION.

## Open items for the read-through

- ch16 (和泉守兼定 / the 之定 signature, 㝎) will want a swordsmith note.
- Confirm the reading of minor Shinsengumi and place names against
  reference/furigana_readings.tsv as they appear.
- くらやみ祭 recurs only here; ch01 note 7 already frames it honestly.

## Environment / traps state

- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches).
- data/src/ and data/src_epub/ are gitignored (regenerate with
  scripts/ingest_epub.py source.epub if empty at session start).
- Scene-break convention for THIS source: a run of two or more consecutive blank
  paragraphs (`<p><br/></p>`) INSIDE the body is a scene break; the single blank
  pair right after the chapter title is only the title/body separator, not a
  break. The China-template apply_format_markers.py does NOT parse this source's
  plain `<p>` HTML, so scene breaks were placed by reading the source directly.
- Known failing test, EXPECTED: `tests/run_tests.py` reports "hook stands down
  on template stub" FAIL. That test only passes when HANDOFF.md still holds the
  template's placeholder kickoff; a real book kickoff makes the guard enforce, as
  intended. Not a translation gate. See PROGRESS.md. All other tests pass.
- All work is on branch claude/burn-o-sword.
