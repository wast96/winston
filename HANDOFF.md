# HANDOFF

## Message to paste into the next chat

```
The Stealthy Ones B07

Read CLAUDE.md, then STYLE.md, then HANDOFF.md, then book.json.

Do Batch 7 = Chapter 7 「死、死、死」 / "Death, Death, Death" (第七章 死、死、死, PDF
pages 415-460, printed folios 413-458), end to end per the CLAUDE.md pipeline.
Chapters 1-6 are DONE; out/ch01_reading.md is the FROZEN register reference.
Work through the chapter in image batches of 2-4 pages, writing
out/ch07_reading.md incrementally, and keep every figure exact.

STYLE.md is the approved prose contract and is non-negotiable: clean, muscular,
contemporary English that hides the translation machinery. No dashed-in
appositive glosses in NARRATION (convert them to commas, colons, periods, or
parentheses); keep em-dashes only for genuinely interrupted or trailing
DIALOGUE and inside quoted classical text; break long sentences into short
varied ones; break dense paragraphs at each shift of focus; trim doubled
synonyms; active verbs; understatement in narration but keep the author's heat
where the source has it. Match ch01: em-dash near 0.3/1k in NARRATION, sentence
median around 17 words. The war/death set-pieces, quoted period documents
(Frois letters, chronicles like the Shinsho Taikoki, diaries, edicts, poems,
Kirishitan catechism) are DELIBERATELY formal and register-exempt; do NOT
contract them, but DO contract the colloquial speakers (Goemon, Maki in her
soft Kishu register, the rough soldiers, peasants) so the whole does not read
stilted. Run check_register.py --ref out/ch01_reading.md out/ch07_reading.md
and expect an em-dash figure inflated by dialogue and quoted documents, not a
failure; a "shall" flag with a tiny denominator is usually quoted-document text.

BEFORE translating, read the final two pages of the previous unit's English (the
close of out/ch06_reading.md): Goemon flees with Maki and their infant Goichi to
Maki's home village of Nagao in Kishu; setting out to take Maki's young sister
Kazue to safety in Sakai, he is lured off by a decoy and Kazue is abducted and
raped by the Koga spy Torii Moriichiro, who frames Goemon to a Takayama patrol
and carries her off; Goemon cannot find her. He catches, unmasks and interrogates
one of Maki's old abductors (the ninja "Purple Scale"), who bites out his own
tongue. Hideyoshi's Kishu campaign of Tensho 13 (1585) then storms and burns the
Negoro-ji; Goemon fights inside the doomed temple. The chapter ends by tearing
down the Shinsho Taikoki's heroic war-tale: "the truth was no such gorgeous
thing. It was terror and madness, shrieking and roaring... a pitiless stretch of
hours in which men had turned back into beasts." STYLE.md and HANDOFF describe
the voice; those pages ARE the voice. Kazue's fate is an OPEN thread; watch for
its resolution.

This is a Japanese book: vertical, right-to-left, heavy furigana. OCR with
lang=jpn_vert, psm 5, crop left 0.06 / right 0.96 / top 0.09 / bottom 0.935
(validated). Run render.py 415 460 then ocr_crop.py; verify pgrep -c tesseract
is 0. DO NOT rely on ocr_dual.py (chi_sim, wrong for JP) or indents.py
(horizontal-axis, missing folio_present). The OCR is too furigana-corrupted to
translate from: TRANSLATE BY READING THE PAGE IMAGES directly (data/png/p0NNNN
.png; offset printed = pdf - 2), OCR as a structural aid only, and crop-verify
every proper name, number, date, and low-confidence span by eye (scripts/
cropview.py PAGE L T R B does a fractional crop; then Read it). Carry every
troop number, date, and toponym exactly. Record source inconsistencies; render
them as printed, never harmonize. WATCH page-boundary resumptions: re-read the
last line of each PDF page before continuing (a sentence that spans two pages is
where content silently drops).

Apparatus: notes via scripts/apparatus_merge.py, folio-cited, XHTML NUMERIC
character references only (o-macron = &#333;, u-macron = &#363;, a-macron =
&#257;, em-dash = &#8212;, curly apostrophe = &#8217;, curly quotes = &#8220;/
&#8221;, CJK as &#nnnnn;) in note BODIES; note ANCHORS must be verbatim (literal
o/u-macron, straight ASCII quotes, no em-dash) substrings of the reading file,
and must sit in a BODY paragraph, not the chapter heading. Author the notes as a
data/ch07_apparatus.json file (Write tool, not a heredoc) with a "notes":
{"ch07": [...]} block and a "figures": {"ch07": [...]} block, then run
apparatus_merge.py on it. Glossary is SECTIONED (people/organizations/places/
terms) and edited with a structure-preserving JSON round-trip or the Write tool,
NOT apparatus_merge (its glossary merge is flat and breaks the sectioned
builder). Reuse the glossary rows already decided (Goemon, Maki, Hanzo, Hatsuko,
Ieyasu, Hideyoshi, Hidenaga, Kazue, Goichi, Yagoemon, Gisuke, Moriichiro, Tsuda
Kazunaga, Kakuban, the Negoro-ji, Kishiwada, Kudoyama, Nagao, the sohei, the
sword-hunt, etc.); do not re-add or re-note subjects already placed (grep
notes.json and PROGRESS.md's "NOT re-noted" lists first). Flag any new principal
with "principal": true. Build with build_reading_epub.py, then qa_epub.py and
epubcheck (java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/the-stealthy-ones.epub).

Use the book's macron romanization throughout (o/u-macron: Kato, Omi, Kita-no-sho,
Taikoki, Tensho, Ogaki, -no-jo, -ro; and Azai, not Asai). Reading files stay
plain ASCII apostrophes/quotes (typographized at render); o/u/a-macron, c-cedilla
and the em-dash are the only non-ASCII used; do NOT paste curly quotes or
accented Latin (e-acute etc.) in. Cite printed folios in every note; never invent
bridging text; do not pause for approval. Deliver the built EPUB in chat AND
paste the next kickoff verbatim in a fenced code block.
```

## What is DONE (one line per batch, do not redo)
- Batch 0 (survey): 8-chapter structure, metadata, skeleton EPUB, batching
  approved (8 chapter-batches; translate the afterword; typographic cover).
- Batch 1 (Chapter 1, "New Waves", PDF 7-70 / folios 5-68): COMPLETE. 328 body
  paras, 67 notes, 13 principals. VOICE GATE and FROZEN register reference.
- Batch 2 (Chapter 2, "A Warm Current", PDF 71-136 / folios 69-134): COMPLETE.
  ~430 paras, 29 notes (total 96), 24 glossary rows (Maki principal).
- Batch 3 (Chapter 3, "Surface and Underside", PDF 137-200 / folios 135-198):
  COMPLETE. ~17,700 words, 34 notes (total 130). qa PASS, epubcheck clean.
- Batch 4 (Chapter 4, "War upon War", PDF 201-258 / folios 199-256): COMPLETE.
  ~16,140 words, 20 notes (total 150). qa PASS, epubcheck clean.
- Batch 5 (Chapter 5, "The Two of Them", PDF 259-360 / folios 257-358):
  COMPLETE. ~28,000 words, 24 notes (total 174), 25 glossary rows.
- Batch 6 (Chapter 6, "Earth and Water", PDF 361-414 / folios 359-412):
  COMPLETE. ~16,200 words, 423 body paras, 9 notes (total 183), 9 glossary rows
  (3 people, 3 places, 3 terms; no new principals), figures ch06 EMPTY. Two
  register-exempt Shinsho Taikoki battle-quotes rendered inline. qa PASS
  (183/183/183), epubcheck 0/0/0/0, check_apparatus clean, register within
  tolerance. See PROGRESS.md for source-inconsistency, rendered-as-read and
  NOT-re-noted lists.

## Branch note (read this)
Working branch is `claude/the-stealthy-ones`. The B06 session was started by the
harness on a stray branch (`claude/ch06-earth-water-hkahbi`) that pointed at the
same commit as origin/claude/the-stealthy-ones (Batch 5 complete); the canonical
branch was reset to origin, all Batch 6 work was done and pushed on
`claude/the-stealthy-ones`, and the stray branch was DELETED (local and remote).
Do all further work on `claude/the-stealthy-ones`. If a fresh session starts on a
stray per-task branch, check out the canonical branch, reset it to origin, do the
work there, and delete the stray (CLAUDE.md rule 2 overrides any harness note
that names a different branch).

## Tooling in place - do NOT revert
- `data/structure.json` from book.json (assemble.py and the builder read it).
  Offset printed = pdf - 2 (constant, no plates).
- `scripts/cropview.py` (Batch 5): fractional crop tool for eyeball verification.
  `cropview.py PAGE L T R B [--out path] [--scale n]`.
- Glossary is edited directly as a SECTIONED file (JSON round-trip or Write);
  apparatus_merge is used for NOTES and FIGURES only. Its glossary merge is flat
  and would break the sectioned builder.
- Note anchors are LITERAL substrings of the reading file (o/u-macron, straight
  ASCII quotes, no em-dashes), in BODY paragraphs; note BODIES use numeric
  character references. apparatus_merge validates anchors as substrings and
  rejects named entities / U+FFFD; the builder refuses a heading-only or
  unmatched anchor.
- Reading files stay plain ASCII apostrophes/quotes (typographized at render);
  o/u/a-macron, c-cedilla and the em-dash are the only non-ASCII used. Do NOT
  paste curly quotes or accented Latin (e-acute etc.) in.
- Fidelity method: translate from page images, not OCR. ocr_dual / indents are
  Chinese-template holdovers, not used.
- Quoted-document convention: personal/dramatic LETTERS render as `{v}` vignette
  blocks (ch03 has two); chronicle/battle quotes (Shinsho Taikoki, Frois
  reports) render INLINE as quoted paragraphs (ch03/ch05/ch06). Verse uses `{p}`.

## Renderings settled through Batch 6 (in glossary.json; reuse unchanged)
All Batch 1-5 renderings stand. Added in Batch 6: people — Hidenaga (Hashiba
Hidenaga), Yagoemon (Maki's father; 弥五右衛門, NOT Goemon), Gisuke (Maki's
brother). Places — Kishiwada, Kudoyama, Nagao. Terms — the sohei (warrior-monks),
the sword-hunt (katanazarae), the Great Pagoda of Negoro (tahoto / Negoro no
Daito). Reused unchanged this batch: Tsuda Kazunaga, Kakuban, Torii Moriichiro,
Torii Kihachiro, Kazue, Goichi, Hatsuko (= 葉津子, the principal), Shima Sakon,
the Negoro-ji, Koya-san, Saiga, Kokawa-dera, Tanegashima, Kunitomo. One-off names
rendered-as-read: see the long "Rendered-as-read" list in PROGRESS.md (Batch 6);
reuse those spellings if any recur.

## Carry-forward VOICE SHEETS (consult at every scene)
- NARRATOR (the load-bearing voice): Murayama Tomoyoshi's own, writing 1962-63.
  Wry, materialist, sweeping in exposition, intimate in scene. Breaks the fourth
  wall constantly: quotes his sources by name (the Shinsho Taikoki, the Frois
  letters, the Tamon-in diary) and pokes at them, cites his own 1963 visits
  (Negoro-ji in ch06), condemns the ruling class and the temple-lords ("not
  human, beasts") from a frankly leftist stance, is frank about sex, violence
  and the body (the Moriichiro-as-serial-rapist passage, ch06), and reads the
  Kishu peasants with tenderness. In ch06 he savages the temple economy and the
  Taikoki's heroic war-tale alike. Keep the wit, the interventions, the heat, the
  anticlerical and anti-war anger, and the tenderness.
- Goemon: the hero; hard-bitten Iga exception; a thief and shinobi who has quit
  the trade. Missing two front teeth. A thoroughgoing materialist thawed by
  Maki's love; now a father (son Goichi). A crack marksman (200-pace range). Has
  renounced the ninja/samurai world; in ch06 he is a fugitive farmer at Nagao,
  throws in his lot with the Kishu peasants against the samurai, and (the
  materialist) prays to Christ for the first time when Kazue is taken. His
  executioner Hideyoshi and the cauldron are planted for ~9 years hence. Register:
  plain, materialist, tender to Maki; speaks Kishu dialect with the villagers;
  can rage.
- Maki (principal): Goemon's wife; a Saiga hill girl, guileless, devoted, soft
  Kishu register ("あて", "〜や/〜じゃ"). Her double is Hatsuko and the Nanban-ji
  Madonna. The still centre of Goemon's life; in ch06 keeping house at her
  father's village with the infant Goichi.
- Kazue (glossed, NOT principal): Maki's boyish, dark, sharp-eyed younger sister,
  15, who longs for Sakai. Abducted and raped by Moriichiro en route to Sakai and
  carried off by Hideyoshi's men — her fate is an OPEN thread into ch07.
- Hattori Hanzo: sharp, tireless, calculating, secretive; loyal to Ieyasu yet
  self-serving; a cold materialist with no sense of sin. His one real feeling is
  his love for Hatsuko. In ch06 he is off-stage but his agents (Moriichiro, the
  "Purple Scale") reach into Goemon's refuge.
- Torii Moriichiro (glossed): the yellow-eyed, right-forefinger-missing Koga spy;
  Ieyasu's/Hanzo's agent lodged at the Negoro Suginobo as a fake Kirishitan; a
  serial rapist with a "collar-slipping" escape trick, unconfident in his arts.
  In ch06 he lures Goemon off, rapes and abducts Kazue, and frames Goemon. A live
  villain into ch07.
- Ieyasu: patient, dissembling, self-mastering ("the old badger"); off-stage in
  ch06 but Goemon's break with him is complete.
- Hideyoshi: small, mean, rat-faced, an overwhelming vital force; a born
  strategist and shameless charmer. In ch06 he opens his Kishu campaign, burns
  the Negoro-ji by a bypass-and-massacre ruse. Goemon's eventual executioner.
- Hatsuko (principal): Hanzo's spirited young woman, Maki's exact double; daughter
  of the Shiroko merchant Kadoya Kyuemon; fought at Nagakute in ninja garb. The
  tragedy of Ieyasu's demand for her, and the substitution of Maki, is behind us.
- Prior live threads and minor cast (Tamo/Sister Kiara the crypto-Christian nun;
  Chika, Hanzo's other woman; the Koga net; the Iga remnant; the Saiga/Negoro
  gunsmith Tsuda Kazunaga; the Suginobo cloister): as in the Batch 1-5 handoffs.

## Where the story stands
Chapter 6 has carried Goemon's family into hiding at Nagao in Kishu; the
materialist backbone (the temple economy, the yamabushi/ninja origins, the Negoro
arms trade and its Great Pagoda); the class-solidarity of the Kishu peasants; the
rape and abduction of Kazue by Moriichiro; and Hideyoshi's Kishu campaign of
Tensho 13 (1585), which storms and burns the Negoro-ji. It ends on the author's
flat indictment of the Taikoki's heroic war-tale: the reality was terror,
madness, and men turned to beasts. Chapter 7, "Death, Death, Death" (死、死、死),
takes up from there; expect the continuation of the Kishu/Saiga destruction, and
watch for the resolution of Kazue's fate and Goemon's next move.

## Batch 7 scope
Chapter 7, "Death, Death, Death" (第七章 死、死、死), PDF 415-460, printed folios
413-458 (the divider page is PDF 415 = folio 413). Batch the reading, keep the
folio offset (printed = pdf - 2), and re-measure at the opener. Carry every
figure exactly (find_figures.py plus eyeball; record even an EMPTY list). Final
batch (B09) carries back matter, the afterword, cover, whole-book reconciliation
and the completion report — plan the last two batches light.

## Open traps / environment
- Vertical-JP OCR is furigana-corrupted; translate from images, crop-verify with
  scripts/cropview.py.
- Glossary sectioned; apparatus_merge for notes+figures only. Note anchors
  LITERAL substrings in BODY paragraphs; note bodies use numeric character refs.
- NARRATION em-dashes: keep low; convert appositive dash-glosses. Dialogue
  trailing/interruption em-dashes and quoted-document dashes are licensed.
- Use the macron romanization (Kato, Omi, Kita-no-sho, Taikoki, -no-jo, -ro;
  Azai not Asai). The Koya vs Koya-san macron reconcile is still OPEN for the
  final batch (glossary "Koya-san"; ch04-06 prose "Mount Koya").
- Kazue's fate is an OPEN narrative thread; do not close or invent it.
- Page-boundary resumptions drop content: re-read the last line of the previous
  PDF page before continuing.
- OMP_THREAD_LIMIT=1 for tesseract; check pgrep -c tesseract = 0 after OCR.
- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (java present).
- No data/pagemap/ for ch02-ch06 yet (only ch01 emits in-text page markers); qa
  still PASSES and every note cites its printed folio in prose.
- One checker regression test ("hook stands down on template stub") fails; a
  template corner case that does not affect real batch replies.
