# HANDOFF

## Message to paste into the next chat

```
The Stealthy Ones B02

Read CLAUDE.md, then STYLE.md, then HANDOFF.md, then book.json.

Do Batch 2 = Chapter 2 「暖かい流れ」 / "A Warm Current" (PDF pages 71–136,
printed folios 69–134), end to end per the CLAUDE.md pipeline. Chapter 1 is
DONE and out/ch01_reading.md is the FROZEN register reference. Goemon's story
proper begins in this chapter.

STYLE.md is the approved prose contract and is non-negotiable: write clean,
muscular, contemporary English that hides the translation machinery. No dashed-in
appositive glosses; break long sentences into short varied ones; break dense
paragraphs at each shift of focus; trim doubled synonyms; active verbs;
understatement in narration but keep the author's heat where the source has it.
The ch01 baseline to match: em-dash ~0.3/1k (dashes only for interrupted or
trailing dialogue), sentence median ~17 words.

BEFORE translating, read the final two pages of the previous unit's English
(the close of out/ch01_reading.md: Lourenço, the arms-dealer's confession, and
the bridge back to Goemon). STYLE.md and HANDOFF describe the voice; those pages
ARE the voice. Keep the register measured against ch01:
check_register.py --ref out/ch01_reading.md out/ch02_reading.md

This is a Japanese book: vertical, right-to-left, heavy furigana. OCR with
lang=jpn_vert, psm 5, crop left 0.06 / right 0.96 / top 0.09 / bottom 0.935
(validated). Run render.py then ocr_crop.py; verify pgrep -c tesseract is 0.
DO NOT rely on ocr_dual.py (hard-wired to chi_sim, wrong for JP) or indents.py
(horizontal-axis, calls a missing folio_present, does not apply to vertical
text). The OCR is too furigana-corrupted to translate from: TRANSLATE BY
READING THE PAGE IMAGES directly (data/png/p00NN.png), OCR as a structural aid
only, and crop-verify every proper name, number, date, and low-confidence span
by eye (PIL crop + Read). Record source inconsistencies; render them as printed,
never harmonize.

Apparatus: notes via scripts/apparatus_merge.py (folio-cited, XHTML numeric
character references only). Glossary is SECTIONED (people/organizations/places/
terms) and edited with the Write tool, NOT apparatus_merge (its glossary merge
is flat and breaks the sectioned builder). Flag principals with "principal":
true. Build with build_reading_epub.py, then qa_epub.py and epubcheck
(java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/the-stealthy-ones.epub).

Cite printed folios in every note; never invent bridging text; do not pause for
approval. Deliver the built EPUB in chat AND paste the next kickoff verbatim in
a fenced code block.
```

## What is DONE (one line per batch, do not redo)
- Batch 0 (survey): 8-chapter structure, metadata, skeleton EPUB, batching
  approved (8 chapter-batches; translate the afterword; typographic cover).
- Batch 1 (Chapter 1, "New Waves", PDF 7-70 / folios 5-68): COMPLETE. Full
  translation (out/ch01_reading.md, 328 body paras), 67 folio-cited notes,
  glossary with 13 principals, cumulative EPUB. qa_epub PASS, epubcheck 0/0,
  check_apparatus clean, register baseline recorded. This chapter is the VOICE
  GATE and, on approval, the frozen register reference. See PROGRESS.md.

## Tooling in place — do NOT revert
- `data/structure.json` written from book.json (assemble.py and the builder
  read it). Offset printed = pdf - 2.
- Glossary is edited directly (Write tool) as a SECTIONED file; apparatus_merge
  is used for NOTES only. This split is deliberate: apparatus_merge writes a
  FLAT glossary that the builder's render_glossary/render_principals cannot use.
- Fidelity method for this book: translate from page images, not from OCR. The
  ocr_dual / indents scripts are Chinese-template holdovers and are not used
  (see PROGRESS.md for why). If a later batch wants automated parity, adapt
  those scripts for vertical Japanese first; do not trust their current output.

## Renderings settled this batch (in glossary.json; reuse unchanged)
People: Ishikawa Goemon, Hideyoshi, Nobunaga, Tamo, Organtino, Hattori Hanzo,
Etegi, Karasumaru, Hatsuko, Tarao Shinbei, Taki Ukon, Torii Moriichiro,
Lourenço (all flagged principal); plus Nobutada, Nobutaka, Akechi Mitsuhide,
Akechi Mitsuharu, Ieyasu, Katsuyori, Shingen, Kaisen, Anayama Baisetsu, Kiso
Yoshimasa, Murai Sadakatsu, Sasaki Jotei, Xavier, Luis Frois, Gaspar Coelho,
Gaspar Vilela, Takayama Ukon, Tarao Doka, Fujibayashi Nagato-no-kami, Momochi
Sandayu, Hanzaemon, Gamo Katahide, Shimizu Muneharu, Kashiwagi Shirobei, Koichi,
Kadoya Kyuemon, Nobuyasu, Lady Tsukiyama, Toku, Sakai Tadatsugu, Okubo Tadayo,
Valignano, Kasumi, Kashii.
Terms: Deus, garça, orasho, padre/bateren, irmão, the nenbutsu, ninja/shinobi,
ninjutsu, the Five Escapes, the Tarao Crossing. Organizations: the Ikko sect,
the Hokke sect, the Christian faith (Yaso-kyo). Places: Nanban-ji, Azuchi,
Honno-ji, Mount Hiei, Erin-ji, Mount Tenmoku, Arima, Usuki, Funai, Iga,
Echizen, Sakamoto, Takatsuki, Saiga.

## Carry-forward VOICE SHEETS (consult at every scene)
- NARRATOR (the load-bearing voice): Murayama's own, a man of the political
  left writing in 1962. Wry, materialist, sweeping in exposition and intimate in
  scene. He breaks the fourth wall constantly: addresses "readers," inserts
  himself and his real family, predicts a socialist Japan, traces the Tokugawa
  spy service to the modern thought-police. Frank and earthy about sex and
  violence. Keep the wit, keep the interventions, keep it flowing and vernacular
  (the commissioner's explicit ask: natural, smooth, native-speaker English).
- Goemon (coming in ch2, only named here): the hero; hard-bitten, striking, an
  Iga exception to the "plain, poor-featured" type. Thief, shinobi, folk avenger.
- Tamo: a burned, half-crippled beggar-woman, once an Iga kunoichi (the cat-art),
  survivor of Ichijodani (1573) and Momochi/Iga (1581). Mute with grief; speaks
  rarely and simply; mourns Kashii, who died shielding her. Even kindness wounds
  her.
- Lourenço (Irmão): blind former biwa-player, gentle and humble, western dialect.
  Render as an old, kindly, faintly archaic voice ("Aye," "I, now, Tamo," "there
  is no sorrow like it").
- Organtino: the Italian padre; gentle, patient, warm; halting Japanese.
- Hattori Hanzo: sharp, tireless, calculating; loyal to Ieyasu yet self-serving
  (filches Hatsuko from his lord); a big, hard-bitten man. Deferential in speech
  to his lord.
- Tarao Doka: canny old Koga ninja chief; folksy, colloquial, western dialect
  (uses "ja"), fond of go/gambling metaphors; shrewd under a deferential surface.
- Honda Tadakatsu: blunt, decisive, fatalistic-practical loyal retainer.
- Ieyasu: genial, curious, decisive; a "silent lecher" who warms to people
  ("Splendid, splendid! Make me a present of those two.").
- Hatsuko: bold merchant's daughter turned kunoichi; energetic, fearless,
  defiant ("I am a woman ninja!"); playful with Etegi.
- Etegi: enormous (41 kan), good-natured, earnest, humble; devoted to Karasumaru.
- Karasumaru: fat 13-year-old orphan; shy, taciturn, gentle, a child's heart.
- The three Koga antagonists (Goemon's coming enemies): Shinbei (youngest, quick,
  handsome, the leader), Taki Ukon (reserved, methodical, slow but always right),
  Torii Moriichiro (eldest, sallow, thick-fleshed, flighty, cruel; mock-gallant
  menace, one forefinger missing).

## Where the story stands
Chapter 1 ends on a metafictional hinge: the narrator leaves Torii tailing the
Sakai gunpowder-merchant, turns time back a year, and promises to follow how
Goemon has lived through "the new waves of history" since the previous novel
closed. Threads left live: Tamo at the Takatsuki seminary (kitchen-hand, drawn
to the faith only by loneliness, mourning Kashii); the three Koga ninja youths
there on a secret mission to get muskets and powder from the Christians; Hatsuko
hidden by Hanzo, training as a kunoichi with Etegi and Karasumaru; Hideyoshi
risen after Yamazaki; Ieyasu bound to the ninja after the Tarao crossing.

## Batch 2 scope
Chapter 2, "A Warm Current" (第二章 暖かい流れ), PDF 71-136, printed folios
69-134. Longer than ch01 (about 66 PDF pages). Goemon's story proper begins.
Read the folio off the scan at each opener (offset printed = pdf - 2) and
re-measure if unpaginated plates appear.

## Open traps / environment
- Vertical-JP OCR is furigana-corrupted; translate from images, crop-verify.
- Glossary sectioned (Write tool); apparatus_merge for notes only.
- OMP_THREAD_LIMIT=1 for tesseract; check pgrep -c tesseract = 0 after OCR.
- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (java present).
- One checker regression test ("hook stands down on template stub") fails; it is
  a template corner case and does not affect real batch replies.
