# HANDOFF

## Message to paste into the next chat

```
The Stealthy Ones B03

Read CLAUDE.md, then STYLE.md, then HANDOFF.md, then book.json.

Do Batch 3 = Chapter 3 「表と裏」 / "Surface and Underside" (PDF pages 137-200,
printed folios 135-198), end to end per the CLAUDE.md pipeline. Chapters 1 and 2
are DONE; out/ch01_reading.md is the FROZEN register reference.

STYLE.md is the approved prose contract and is non-negotiable: clean, muscular,
contemporary English that hides the translation machinery. No dashed-in
appositive glosses (convert them to commas, colons, periods, or parentheses);
keep em-dashes only for genuinely interrupted or trailing DIALOGUE; break long
sentences into short varied ones; break dense paragraphs at each shift of focus;
trim doubled synonyms; active verbs; understatement in narration but keep the
author's heat where the source has it. Match ch01: em-dash near 0.3/1k in
narration, sentence median around 17 words.

BEFORE translating, read the final two pages of the previous unit's English (the
close of out/ch02_reading.md: the long death-and-rebirth meditation, Goemon and
Hanzo drinking, the warm-current-of-Hatsuko's-sap passage, and Hanzo tossing
Hatsuko onto the bedding). STYLE.md and HANDOFF describe the voice; those pages
ARE the voice. Keep the register measured against ch01:
check_register.py --ref out/ch01_reading.md out/ch03_reading.md

This is a Japanese book: vertical, right-to-left, heavy furigana. OCR with
lang=jpn_vert, psm 5, crop left 0.06 / right 0.96 / top 0.09 / bottom 0.935
(validated). Run render.py 137 200 then ocr_crop.py; verify pgrep -c tesseract
is 0. DO NOT rely on ocr_dual.py (hard-wired to chi_sim, wrong for JP) or
indents.py (horizontal-axis, calls a missing folio_present). The OCR is too
furigana-corrupted to translate from: TRANSLATE BY READING THE PAGE IMAGES
directly (data/png/p0NNNN.png; offset printed = pdf - 2), OCR as a structural
aid only, and crop-verify every proper name, number, date, and low-confidence
span by eye (PIL crop + Read). Record source inconsistencies; render them as
printed, never harmonize.

Apparatus: notes via scripts/apparatus_merge.py, folio-cited, XHTML NUMERIC
character references only; note ANCHORS must be verbatim (literal, not entity)
substrings of the reading file. Glossary is SECTIONED (people/organizations/
places/terms) and edited with the Write tool or a structure-preserving insert,
NOT apparatus_merge (its glossary merge is flat and breaks the sectioned
builder). Flag principals with "principal": true. Build with
build_reading_epub.py, then qa_epub.py and epubcheck
(java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/the-stealthy-ones.epub).

Cite printed folios in every note; never invent bridging text; do not pause for
approval. Deliver the built EPUB in chat AND paste the next kickoff verbatim in
a fenced code block.
```

## What is DONE (one line per batch, do not redo)
- Batch 0 (survey): 8-chapter structure, metadata, skeleton EPUB, batching
  approved (8 chapter-batches; translate the afterword; typographic cover).
- Batch 1 (Chapter 1, "New Waves", PDF 7-70 / folios 5-68): COMPLETE. 328 body
  paras, 67 folio-cited notes, 13 principals, register baseline. This chapter is
  the VOICE GATE and the frozen register reference. See PROGRESS.md.
- Batch 2 (Chapter 2, "A Warm Current", PDF 71-136 / folios 69-134): COMPLETE.
  ~430 body paras, 29 folio-cited notes (book total 96), 24 new glossary rows
  (Maki added as a principal, book total 14), figures.json ch02 recorded EMPTY.
  qa_epub PASS, epubcheck 0/0/0/0, check_apparatus clean, register within
  tolerance. See PROGRESS.md.

## Tooling in place — do NOT revert
- `data/structure.json` from book.json (assemble.py and the builder read it).
  Offset printed = pdf - 2.
- Glossary is edited directly (Write tool / structure-preserving insert) as a
  SECTIONED file; apparatus_merge is used for NOTES only. Deliberate:
  apparatus_merge writes a FLAT glossary the builder cannot render.
- Note anchors are LITERAL substrings of the reading file (use ō, ū, straight
  quotes, no em-dashes), while note BODIES use numeric character references
  (&#8212; etc.). apparatus_merge validates both.
- Fidelity method for this book: translate from page images, not from OCR. The
  ocr_dual / indents scripts are Chinese-template holdovers, not used.

## Renderings settled so far (in glossary.json; reuse unchanged)
All of Batch 1's renderings stand (see the list in the previous handoff / the
glossary). Added in Batch 2:
People: Maki (principal, Goemon's wife), Oyu, Soda Yoichiro, Kuki Yoshitaka,
Naya Sukezaemon (= Ruson/Luzon Sukezaemon), Mori Ranmaru, Kobo Daishi. (Akechi
Mitsuhide and Torii Moriichiro were already glossed in Batch 1.)
Places: Sakai, Hamamatsu, the Myokoku-ji, the Honjuji, the Jofukuji, Nanzen-ji,
Negoro-ji, Koya-san, the Chinu Sea, Nabari.
Terms: kunoichi, the shichihode, the egoshu, the sotetsu, Kishimojin, nyujo,
the Man'yoshu.
Goemon's Tokugawa alias is Saeki Dennai. Other names used once and rendered as
read (not glossed): Matsui Yukan, Miyoshi Yukiyasu, Nikko Shonin, Abe Hisanobu,
Kudobei, Tsuji Yahei, Shinshi Rokuro-dayu, Yomoda Tajima-no-kami, Bomaru,
Rikimaru, Niwa Nagahide, Akechi Hidemitsu, Kozan (of Chozen-ji).

## Carry-forward VOICE SHEETS (consult at every scene)
- NARRATOR (the load-bearing voice): Murayama Tomoyoshi's own, a man of the
  political left writing about 1962. Wry, materialist, sweeping in exposition,
  intimate in scene. Breaks the fourth wall constantly: addresses "readers,"
  inserts himself and his real wife, cites his own imprisonment and his oil
  painting, sets Buddhist and Christian eschatology side by side and finds both
  wanting. Frank and earthy about sex and violence. Keep the wit and the
  interventions; keep it flowing and vernacular.
- Goemon: the hero; hard-bitten, an Iga exception to the plain-featured type;
  thief and shinobi who has quit the trade. Missing two front teeth (knocked out
  for a disguise). Now a tender husband; wants free of the ninja life; his one
  tie back to it is Hanzo. Rough, familiar speech ("ja", "ore"); murmurs
  endearments to Maki; a materialist who feels the old homesickness of the blood.
- Maki (NEW, principal): Goemon's wife; a poor Saiga hill-country girl (Ikko
  stock, family harried by the Negoro monks), guileless, devoted, plain-spoken
  in a soft Kishu register ("ya", "へえ", "です"). Not a seductress; the still
  center of Goemon's life. Physical double of Hatsuko, though unrelated. Wrinkles
  her nose at "eel again today?"
- Hattori Hanzo: sharp, tireless, calculating; loyal to Ieyasu yet wholly
  self-serving. A gambler who relishes staking his own neck; a cold
  materialist who works the "possessing spirit" as pure technique. Cynical
  playbook: make your lord fear you, hold his secrets, be indispensable, steer
  him. Coarse, boastful, ends every self-justification foaming a little at the
  mouth. Filched Hatsuko from Ieyasu and has a ready lie for it.
- Hatsuko: bold, energetic, fearless kunoichi; teases Goemon, dominates Hanzo
  even in the bedchamber; hysterical fits that only clowning defuses. Sharper,
  higher, more nasal voice than Maki. Casts a hypnotic pull over men.
- Oyu (NEW): a Tarao kunoichi planted among Nobunaga's women at Azuchi; poised,
  quick, warm-seeming; plays the smitten Yoichiro and feeds rumor to Ranmaru. A
  double agent in Hanzo's net.
- Etegi: enormous (41 kan), good-natured, earnest, humble; besotted with Hatsuko.
- Karasumaru: fat teenage orphan; shy, taciturn, gentle; besotted with Hatsuko.
- Torii Moriichiro (a Koga antagonist): eldest, sallow, thick-fleshed, cruel,
  yellow-whited sunken eyes, one forefinger missing; a runner in the ninja net.
- Tamo, Lourenço, Organtino, Tarao Doka, Ieyasu, Shinbei, Taki Ukon: as in the
  Batch 1 handoff (still live in the saga).

## Where the story stands
Chapter 2 has re-told the fall of Nobunaga from underneath: Ieyasu, through
Hanzo's ninja net (Oyu feeding Ranmaru the lie that Mitsuhide was intriguing
with Ieyasu, Torii Moriichiro carrying word east), maneuvered Akechi Mitsuhide
into the Honno-ji revolt, and Goemon, hidden above the ceiling, was the sole
witness to Nobunaga's death and himself dealt the final strokes. Goemon now
lives at Hamamatsu as "Saeki Dennai" on 30 koku, with Maki; he loathes and
cannot quite escape Hanzo. Hideyoshi, having crushed Mitsuhide at Yamazaki, is
stepping onto the main stage. Threads live: Goemon's wish to quit the ninja for
good; the secret that Momochi Sandayu and Fujibayashi Nagato were one man; the
Maki/Hatsuko doubling; Hanzo consolidating the Iga men under the Tokugawa.

## Batch 3 scope
Chapter 3, "Surface and Underside" (第三章 表と裏), PDF 137-200, printed folios
135-198. Read the folio off the scan at each opener (offset printed = pdf - 2)
and re-measure if unpaginated plates appear. The title echoes the chapter-2
theme (history's visible face vs. its hidden workings), so expect more of the
Ieyasu/Hanzo/ninja machinery behind Hideyoshi's rise.

## Open traps / environment
- Vertical-JP OCR is furigana-corrupted; translate from images, crop-verify.
- Glossary sectioned (Write tool); apparatus_merge for notes only. Note anchors
  must be LITERAL substrings of the reading file, not entity-encoded.
- This chapter's dialogue carries many source em-dashes (interrupted/trailing
  speech), which are legitimate; kill only NARRATION dashes.
- No data/pagemap/ch02.json yet (ch02 has no in-text page markers; notes still
  cite folios in prose). Optional follow-up: add ch02 to data/pagemap.
- OMP_THREAD_LIMIT=1 for tesseract; check pgrep -c tesseract = 0 after OCR.
- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (java present).
- One checker regression test ("hook stands down on template stub") fails; a
  template corner case that does not affect real batch replies.
