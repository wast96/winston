# HANDOFF

## Message to paste into the next chat

```
The Stealthy Ones B04

Read CLAUDE.md, then STYLE.md, then HANDOFF.md, then book.json.

Do Batch 4 = Chapter 4 「いくさいくさ」 / "War upon War" (PDF pages 201-258,
printed folios 199-256), end to end per the CLAUDE.md pipeline. Chapters 1-3 are
DONE; out/ch01_reading.md is the FROZEN register reference.

STYLE.md is the approved prose contract and is non-negotiable: clean, muscular,
contemporary English that hides the translation machinery. No dashed-in
appositive glosses in NARRATION (convert them to commas, colons, periods, or
parentheses); keep em-dashes only for genuinely interrupted or trailing
DIALOGUE and inside quoted classical text; break long sentences into short
varied ones; break dense paragraphs at each shift of focus; trim doubled
synonyms; active verbs; understatement in narration but keep the author's heat
where the source has it. Match ch01: em-dash near 0.3/1k in narration, sentence
median around 17 words. NOTE the ch03 lesson: narration appositive dashes are
easy to overuse in the heavy exposition — watch them from the first draft.

BEFORE translating, read the final two pages of the previous unit's English (the
close of out/ch03_reading.md: Goemon sent to watch the Hideyoshi/Katsuie
showdown, the New Year's-Eve inn three ri south of Kyoto, and Goemon standing on
the Saikoku road at the Yamazaki battlefield — Mount Tennō, the Yodo defile, the
18,000 vs 26,000 and 6,000 dead). STYLE.md and HANDOFF describe the voice; those
pages ARE the voice. Keep the register measured against ch01:
check_register.py --ref out/ch01_reading.md out/ch04_reading.md

This is a Japanese book: vertical, right-to-left, heavy furigana. OCR with
lang=jpn_vert, psm 5, crop left 0.06 / right 0.96 / top 0.09 / bottom 0.935
(validated). Run render.py 201 258 then ocr_crop.py; verify pgrep -c tesseract
is 0. DO NOT rely on ocr_dual.py (hard-wired to chi_sim, wrong for JP) or
indents.py (horizontal-axis, calls a missing folio_present). The OCR is too
furigana-corrupted to translate from: TRANSLATE BY READING THE PAGE IMAGES
directly (data/png/p0NNNN.png; offset printed = pdf - 2), OCR as a structural
aid only, and crop-verify every proper name, number, date, and low-confidence
span by eye (PIL crop + Read). This is a war chapter — expect dense troop
numbers, dates, and place-names (Shizugatake, Kita-no-shō, the Komaki/Nagakute
front): carry every figure exactly. Record source inconsistencies; render them
as printed, never harmonize. WATCH page-boundary resumptions — a sentence that
spans two PDF pages is where content silently drops (it did once in ch03; caught
and restored).

Apparatus: notes via scripts/apparatus_merge.py, folio-cited, XHTML NUMERIC
character references only; note ANCHORS must be verbatim (literal, not entity)
substrings of the reading file, and must sit in a BODY paragraph, not the
chapter heading (the builder rejects heading anchors). Glossary is SECTIONED
(people/organizations/places/terms) and edited with a structure-preserving JSON
round-trip or the Write tool, NOT apparatus_merge (its glossary merge is flat
and breaks the sectioned builder). Flag principals with "principal": true. Build
with build_reading_epub.py, then qa_epub.py and epubcheck
(java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/the-stealthy-ones.epub).

Cite printed folios in every note; never invent bridging text; do not pause for
approval. Deliver the built EPUB in chat AND paste the next kickoff verbatim in
a fenced code block.
```

## What is DONE (one line per batch, do not redo)
- Batch 0 (survey): 8-chapter structure, metadata, skeleton EPUB, batching
  approved (8 chapter-batches; translate the afterword; typographic cover).
- Batch 1 (Chapter 1, "New Waves", PDF 7-70 / folios 5-68): COMPLETE. 328 body
  paras, 67 folio-cited notes, 13 principals. This chapter is the VOICE GATE and
  the FROZEN register reference. See PROGRESS.md.
- Batch 2 (Chapter 2, "A Warm Current", PDF 71-136 / folios 69-134): COMPLETE.
  ~430 body paras, 29 notes (book total 96), 24 new glossary rows (Maki added as
  principal, book total 14), figures ch02 EMPTY. See PROGRESS.md.
- Batch 3 (Chapter 3, "Surface and Underside", PDF 137-200 / folios 135-198):
  COMPLETE. ~17,700 words, 34 notes (book total 130), 25 new glossary rows (no
  new principals; book total 14), figures ch03 EMPTY. qa_epub PASS, epubcheck
  0/0/0/0, check_apparatus clean, em-dash back to 4.3/1k after a narration-dash
  pass. See PROGRESS.md.

## Branch note (read this)
All batches (1, 2, 3) live as one continuous linear history on the working
branch this session is on (`claude/stealthy-ones-b03-ygoea4`), which is where
the task harness places the session and the only branch the task rules permit
pushing to. The local `claude/the-stealthy-ones` is STALE (still at the survey
commit) and does NOT contain Batch 1-3; do not reset onto it or work would be
stranded. Keep committing/pushing to the branch the harness gives you; it holds
the full cumulative history. If the commissioner wants everything consolidated
onto a single canonical name, that is a deliberate branch-rename decision for
them to make, not blind surgery.

## Tooling in place — do NOT revert
- `data/structure.json` from book.json (assemble.py and the builder read it).
  Offset printed = pdf - 2.
- Glossary is edited directly as a SECTIONED file (structure-preserving JSON
  round-trip in Python, or the Write tool); apparatus_merge is used for NOTES
  only. Deliberate: apparatus_merge writes a FLAT glossary the builder cannot
  render.
- Note anchors are LITERAL substrings of the reading file (use ō/ū, straight
  ASCII quotes, no em-dashes in the anchor), sit in BODY paragraphs (not the
  heading), while note BODIES use numeric character references (&#8212; etc.).
  apparatus_merge validates both; the builder refuses a heading-only anchor.
- Reading files stay plain ASCII apostrophes/quotes (typographized at render);
  ō/ū/ā and ç (Lourenço) are the only non-ASCII allowed. Do NOT paste curly
  quotes in.
- Fidelity method for this book: translate from page images, not from OCR. The
  ocr_dual / indents scripts are Chinese-template holdovers, not used.

## Renderings settled so far (in glossary.json; reuse unchanged)
All of Batch 1-2's renderings stand. Added in Batch 3:
People: Torii Kihachirō, Chika, Asano Nagamasa, Katō Kiyomasa (=Toranosuke),
Shibata Katsuie, Niwa Nagahide, Nobukatsu, Nobutaka, Sanbōshi (=Oda Hidenobu),
Nene (=Kōdai-in), Yomoda Tajima-no-kami, Oichi, the Lady Yodo (=Chacha).
Places: Yono, Ueno (Iga), the Shōfuku-ji, the Daitoku-ji, Yamazaki, Mount Tennō,
Kiyosu, Gifu.
Terms: tenton no jutsu, kamari, the Five Commissioners (go-bugyō), the sanmai.
One-off Taikōki/Kiyosu/kabuki names rendered as read (not glossed): see the list
in PROGRESS.md ("Rendered-as-read"). Reuse those spellings if any recur.

## Carry-forward VOICE SHEETS (consult at every scene)
- NARRATOR (the load-bearing voice): Murayama Tomoyoshi's own, writing 1962-63.
  Wry, materialist, sweeping in exposition, intimate in scene. Breaks the fourth
  wall constantly: quotes his sources by name and pokes at them, checks a word
  in the dictionary, cites his own boyhood and a kabuki he saw last month, sets
  Buddhist and Christian eschatology side by side and reads both materially,
  resents postwar Americanization, was twice jailed under the wartime state.
  Frank about sex and violence. Keep the wit, the interventions, the heat.
- Goemon: the hero; hard-bitten Iga exception to the plain type; a thief and
  shinobi who has quit the trade and wants free of the ninja life. Missing two
  front teeth. Tender husband to Maki; a thoroughgoing materialist who feels the
  cold "loneliness" of the void when he broods; now sent by Ieyasu (via Hanzō)
  to watch the wars. First glimpsed his future executioner Hideyoshi this batch.
- Maki (principal): Goemon's wife; a Saiga hill girl, guileless, devoted, soft
  Kishu register. The still centre of his life; physical double of Hatsuko.
- Hattori Hanzō: sharp, tireless, calculating; loyal to Ieyasu yet wholly
  self-serving; a gambler and cold materialist who works faith as pure
  technique. Coarse, boastful, foams a little at the mouth self-justifying. In
  ch03: weeps genuinely before the crypto-Christian Maria, then ravishes Chika;
  keeps women at Hamamatsu (Hatsuko) and Yono (Chika); spun a ninja ambush into
  a "miracle." A "traitor to the ninja world" the Iga remnant now hunt.
- Hatsuko: bold, energetic kunoichi; teases; hysterical fits defused by
  clowning; sharper/higher voice than Maki; hypnotic pull over men.
- Ieyasu: patient, dissembling — "a face of perfect unconcern on the surface,
  and underneath a mounting impatience"; bides his time while Hideyoshi rises.
- Torii Moriichirō (Koga antagonist, in the ninja net): sallow, hollow-eyed,
  cruel, jealous; no love in him, only appetite; a poorly-trained shinobi (cried
  out when stabbed). Carried Oyu's death-news to Hanzō.
- Oyu, Etegi, Karasumaru, Tamo, Lourenço, Organtino, Tarao Doka, Shinbei, Taki
  Ukon, the three Koga youths: as in the Batch 1-2 handoffs (still live).
- NEW this batch, likely recurring: Hideyoshi (now full on-stage) — small, mean,
  rat-faced, scuttling, yet an overwhelming taut vital force; single-minded
  ambition that impresses even Goemon; the coming antagonist and Goemon's
  eventual executioner. Shibata Katsuie — proud old veteran, undone at Kiyosu.

## Where the story stands
Chapter 3 has retold Nobunaga's fall and Hideyoshi's rise from surface and
underside. Oyu is dead (killed after Yamazaki); Moriichirō reported it. Hideyoshi
consolidated power (Kiyosu Conference; the grand Daitoku-ji funeral over an empty
coffin), and Goemon — sent by Ieyasu to observe — saw him for the first time from
the ceiling and could not shake the image. The anti-Hideyoshi bloc (Shibata,
Nobutaka, with Oichi married to Katsuie) is forming; Hideyoshi has cowed Gifu and
returned in triumph; both sides wait for spring. Goemon stands at the Yamazaki
battlefield as the chapter closes. Live threads: the coming Hideyoshi/Shibata war
(Shizugatake); Goemon's wish to quit the ninja; Hanzō's crypto-Christianity and
the Iga remnant hunting him; the cauldron and the Yodo-castle capture planted for
thirteen years hence.

## Batch 4 scope
Chapter 4, "War upon War" (第四章 いくさいくさ), PDF 201-258, printed folios
199-256. Read the folio off the scan at each opener (offset printed = pdf - 2)
and re-measure if unpaginated plates appear (none so far in this book). The title
signals the war-heavy stretch: expect the Shizugatake campaign and its aftermath,
dense with troop numbers, dates, and toponyms — carry every figure exactly.

## Open traps / environment
- Vertical-JP OCR is furigana-corrupted; translate from images, crop-verify.
- Glossary sectioned; apparatus_merge for notes only. Note anchors LITERAL
  substrings, in BODY paragraphs (heading anchors are rejected by the builder).
- NARRATION em-dashes: keep them near 0.3/1k from the first draft (ch03 needed a
  whole conversion pass because the heavy exposition invited appositive dashes).
- Page-boundary resumptions drop content: re-read the last line of the previous
  PDF page before continuing (ch03 lost, then restored, the Onna Taikōki sentence
  across PDF 148→149).
- OMP_THREAD_LIMIT=1 for tesseract; check pgrep -c tesseract = 0 after OCR.
- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (java present).
- No data/pagemap/ for ch02/ch03 yet (only ch01 emits in-text page markers); qa
  still PASSES and every note cites its printed folio in prose. Optional
  follow-up: add ch02/ch03 to data/pagemap for in-text folio markers.
- One checker regression test ("hook stands down on template stub") fails; a
  template corner case that does not affect real batch replies.
