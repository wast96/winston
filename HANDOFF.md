# HANDOFF

## Message to paste into the next chat

```
The Stealthy Ones B08

Read CLAUDE.md, then STYLE.md, then HANDOFF.md, then book.json.

Do Batch 8 = Chapter 8 「断末魔」 / "Death Throes" (第八章 断末魔, PDF pages 461-530,
printed folios 459-528), end to end per the CLAUDE.md pipeline. This is the FINAL
chapter and the longest (~70 pages): Goemon's road to the cauldron. Chapters 1-7
are DONE; out/ch01_reading.md is the FROZEN register reference. Work through the
chapter in image batches of 2-4 pages, writing out/ch08_reading.md incrementally,
and keep every figure exact. NOTE the chapter/afterword boundary: Chapter 8 body
ends at printed 528 (PDF 530); the afterword 解説 by Musashino Jiro (printed
529-534 / PDF 531-536) is NOT part of this chapter. It is translated as clearly
attributed back matter in the FINAL batch (B09), together with the cover, the
whole-book reconciliation sweep, out/term_ledger.md, out/deep_audit.md and
COMPLETION.md. Plan B08 to end at folio 528, and leave B09 light.

STYLE.md is the approved prose contract and is non-negotiable: clean, muscular,
contemporary English that hides the translation machinery. No dashed-in
appositive glosses in NARRATION (convert them to commas, colons, periods, or
parentheses; use parentheses where the source itself parenthesizes, e.g. metric
and calendar glosses); keep em-dashes only for genuinely interrupted or trailing
DIALOGUE and inside quoted classical text; break long sentences into short varied
ones; break dense paragraphs at each shift of focus; trim doubled synonyms;
active verbs; understatement in narration but keep the author's heat where the
source has it. Match ch01: em-dash near 0.3/1k in NARRATION, sentence median
around 17 words. The war/death set-pieces and quoted period documents (Frois
letters, chronicles like the Shinsho Taikoki, diaries, edicts, poems, the
execution accounts) are DELIBERATELY formal and register-exempt; do NOT contract
them, but DO contract the colloquial speakers (Goemon, the rough soldiers,
peasants, townsfolk) so the whole does not read stilted. Run check_register.py
--ref out/ch01_reading.md out/ch08_reading.md and expect an em-dash figure
inflated by dialogue and quoted documents, not a failure.

BEFORE translating, read the final two pages of the previous unit's English (the
close of out/ch07_reading.md): the Negoro-ji and Ota Castle are destroyed; Maki
is DEAD (shot and drowned at Ota Castle, having tied the infant Goichi high on a
scaffold with her own sash to save him); Goemon is a grieving widower at Nagao
with the baby Goichi (Maki's living image), his heart burning to kill Hideyoshi.
Kazue's thread is now CLOSED: two dream-visions reveal she was trafficked by
Sakai/Nanban slavers and is a sex-slave on Luzon; do not reopen or invent it.
Hideyoshi is now Kanpaku and "the First Man under Heaven"; his lust for Maa-hime
(Kaga-dono) is planted. Chapter 8 is the payoff of the whole book: by tradition
Goemon attempts Hideyoshi, is caught, and is boiled to death in the cauldron in
1594 (the book's subtitle, 五右衛門釜煎り). STYLE.md and HANDOFF describe the
voice; those pages ARE the voice. Watch for Hanzo, Ieyasu, Hatsuko and the Koga
spy Torii Moriichiro (Kazue's rapist, still at large) returning.

This is a Japanese book: vertical, right-to-left, heavy furigana. OCR with
lang=jpn_vert, psm 5, crop left 0.06 / right 0.96 / top 0.09 / bottom 0.935
(validated). Run render.py 461 530 then ocr_crop.py; the pipeline stage-3 writes
0 pages, so regenerate the structural-aid OCR by hand into data/txt (loop:
tesseract data/crop/pNNNN.png stdout -l jpn_vert --psm 5 > data/txt/pNNNN.txt),
with OMP_THREAD_LIMIT=1, then verify pgrep -c tesseract is 0. DO NOT rely on
ocr_dual.py (chi_sim) or indents.py (horizontal-axis). The OCR is too furigana-
corrupted to translate from: TRANSLATE BY READING THE PAGE IMAGES directly
(data/png/p0NNNN.png; offset printed = pdf - 2), OCR as a structural aid only,
and crop-verify every proper name, number, date, and low-confidence span by eye
(scripts/cropview.py PAGE L T R B does a fractional crop; then Read it). Carry
every troop number, date, and toponym exactly. Record source inconsistencies;
render them as printed, never harmonize. WATCH page-boundary resumptions: re-read
the last line of each PDF page before continuing (a sentence that spans two pages
is where content silently drops).

Apparatus: notes via scripts/apparatus_merge.py, folio-cited, XHTML NUMERIC
character references only (o-macron = &#333;, u-macron = &#363;, a-macron =
&#257;, em-dash = &#8212;, en-dash = &#8211;, curly apostrophe = &#8217;, curly
quotes = &#8220;/&#8221;, CJK as &#nnnnn;) in note BODIES; note ANCHORS must be
verbatim (literal o/u-macron, straight ASCII quotes, no em-dash) substrings of
the reading file, and must sit in a BODY paragraph, not the chapter heading.
Author the notes as a data/ch08_apparatus.json file (build it with a Python
encoder that converts non-ASCII to &#nnnn; and keeps <i> tags literal, then
verify pure-ASCII + no U+FFFD) with a "notes": {"ch08": [...]} block and a
"figures": {"ch08": [...]} block, then run apparatus_merge.py on it. End every
note body with "(Printed folio NNN.)". Glossary is SECTIONED (people/
organizations/places/terms), CJK-keyed dicts; edit with a structure-preserving
JSON round-trip (json.load -> add keys -> json.dump ensure_ascii=False) or the
Write tool, NOT apparatus_merge (its glossary merge is flat and breaks the
sectioned builder). Reuse the glossary rows already decided (grep notes.json and
PROGRESS's "NOT re-noted" lists first; do not re-note subjects already placed).
Flag any new principal with "principal": true. Build with build_reading_epub.py,
then qa_epub.py and epubcheck (java -jar /tmp/epubcheck-5.1.0/epubcheck.jar
out/the-stealthy-ones.epub).

Use the book's macron romanization throughout (o/u-macron: Kato, Omi, Kita-no-sho,
Taikoki, Tensho, Ogaki, -no-jo, -ro, Kishu, Etchu, Chosokabe, Goto, Kongobu-ji,
Kobo, Honno-ji, Suginobo, Kanpaku=no-macron; and Azai, not Asai). Keep "Osaka",
"Kyoto" and "Daito" WITHOUT macron (matches the majority/glossary; see the OPEN
reconcile list in PROGRESS). Reading files stay plain ASCII apostrophes/quotes
(typographized at render); o/u/a-macron and the em-dash are the only non-ASCII
used; do NOT paste curly quotes or accented Latin (e-acute etc.) in. Cite printed
folios in every note; never invent bridging text; do not pause for approval.
Deliver the built EPUB in chat AND paste the next kickoff verbatim in a fenced
code block.
```

## What is DONE (one line per batch, do not redo)
- Batch 0 (survey): 8-chapter structure, metadata, skeleton EPUB, batching
  approved (8 chapter-batches; translate the afterword as B09 back matter;
  typographic cover).
- Batch 1 (Chapter 1, "New Waves", PDF 7-70 / folios 5-68): COMPLETE. 328 body
  paras, 67 notes, 13 principals. VOICE GATE and FROZEN register reference.
- Batch 2 (Chapter 2, "A Warm Current", PDF 71-136 / folios 69-134): COMPLETE.
  ~430 paras, 29 notes, 24 glossary rows (Maki principal).
- Batch 3 (Chapter 3, "Surface and Underside", PDF 137-200 / folios 135-198):
  COMPLETE. ~17,700 words, 34 notes. qa PASS, epubcheck clean.
- Batch 4 (Chapter 4, "War upon War", PDF 201-258 / folios 199-256): COMPLETE.
  ~16,140 words, 20 notes. qa PASS, epubcheck clean.
- Batch 5 (Chapter 5, "The Two of Them", PDF 259-360 / folios 257-358):
  COMPLETE. ~28,000 words, 24 notes, 25 glossary rows.
- Batch 6 (Chapter 6, "Earth and Water", PDF 361-414 / folios 359-412):
  COMPLETE. ~16,200 words, 423 paras, 9 notes, 9 glossary rows. qa PASS.
- Batch 7 (Chapter 7, "Death, Death, Death", PDF 415-460 / folios 413-457):
  COMPLETE. ~11,800 words, 441 body paras, 13 notes (book total 196), 14 glossary
  rows (8 people, 4 places, 2 terms; no new principals),
  figures ch07 EMPTY. House macron romanization applied to the reading file.
  qa PASS (196/196/196), epubcheck 0/0/0/0, check_apparatus clean, register
  within tolerance. Maki dies; Kazue's fate resolved (Luzon). See PROGRESS.md for
  the source-inconsistency, rendered-as-read and NOT-re-noted lists and the OPEN
  reconcile items.

## Branch note (read this)
Working branch is `claude/the-stealthy-ones`. Harnesses routinely start a session
on a stray per-task branch. The recipe (CLAUDE.md rule 2, which overrides any
harness note naming a different branch): check out `claude/the-stealthy-ones`,
reset it to origin, do all work there, and DELETE the stray branch (local and
remote). B07 was started on `claude/ch07-death-death-death-kvf8k1` (cut from
origin/claude/the-stealthy-ones at Batch 6); the canonical branch was reset to
origin, all B07 work done and pushed there, and the stray deleted.

## Tooling in place - do NOT revert
- `data/structure.json` from book.json (assemble.py and the builder read it).
  Offset printed = pdf - 2 (constant, no plates), verified at every opener.
- `scripts/cropview.py`: fractional crop tool for eyeball verification.
  `cropview.py PAGE L T R B [--out path] [--scale n]`.
- OCR structural aid: ocr_crop.py stage-3 writes 0 pages for this book, so
  regenerate per-page OCR by hand (tesseract loop into data/txt, jpn_vert, psm 5,
  OMP_THREAD_LIMIT=1). Translate from the page images, not the OCR.
- Glossary is edited directly as a SECTIONED, CJK-keyed file (JSON round-trip or
  Write); apparatus_merge is used for NOTES and FIGURES only.
- Note anchors are LITERAL substrings of the reading file (o/u-macron, straight
  ASCII quotes, no em-dashes), in BODY paragraphs; note BODIES use numeric
  character references, authored via a Python encoder (keep <i> tags literal),
  and end "(Printed folio NNN.)". apparatus_merge validates anchors and rejects
  named entities / U+FFFD; the builder refuses a heading-only or unmatched anchor.
- Reading files use house MACRON romanization (o/u/a-macron) plus the em-dash;
  no curly quotes or accented Latin. "Osaka", "Kyoto", "Daito" stay plain.

## Renderings settled through Batch 7 (in glossary.json; reuse unchanged)
All Batch 1-6 renderings stand. Added in Batch 7: people - Goto Matabei, Kuroda
Kanbei, Mokujiki Ogo, Toyotomi Hidetsugu, Maa-hime (Kaga-dono), Ota
Jirozaemon-no-jo, Ishida Mitsunari, Chosokabe Motochika. Places - Luzon, Ota
Castle, Takamatsu Castle, Kongobu-ji. Terms - the Taiko kenchi, the Kanpaku.
Reused unchanged this batch: Nene, the go-bugyo / Five Commissioners (ch03),
Maeda Gen'i, Sasa Narimasa (kept the glossary "Sasa"; reconcile OPEN), Maeda
Toshiie, Shibata Katsuie, Kita-no-sho, Tsuda Kenmotsu Kazunaga, the Suginobo,
Negoro-ji, Kokawa-dera, Saiga, Kakuban, Tanegashima, Kunitomo, Hori Kyutaro
Hidemasa, Yoshino, the Tahei alias, Kudoyama, Nagao, Koya-san (prose: Mount Koya).
One-off names rendered-as-read: see the long "Rendered-as-read" list in
PROGRESS.md (Batch 7); reuse those spellings if any recur.

## Carry-forward VOICE SHEETS (consult at every scene)
- NARRATOR (the load-bearing voice): Murayama Tomoyoshi's own, writing 1962-63.
  Wry, materialist, sweeping in exposition, intimate in scene. Breaks the fourth
  wall constantly: quotes his sources by name (the Shinsho Taikoki, the Hoan
  Taikoki, the Frois letters, Nobunaga's letters) and pokes at them, cites his
  own visits (Mount Koya's Daimon, the Ota Castle monument), condemns Hideyoshi
  and the ruling class from a frankly leftist stance, is frank about sex,
  violence and the body (the overseas slave-trade, the water-attack), and reads
  the peasants with tenderness. In ch07 he savages the Taiko kenchi and the
  sword-hunt and calls Hideyoshi "the brigand-demon of Japan" (quoting the Hoan
  Taikoki). Keep the wit, the interventions, the anti-war and anti-tyrant anger,
  and the tenderness.
- Goemon: the hero; hard-bitten Iga exception; thief and shinobi who quit the
  trade; missing two front teeth; a crack marksman. A materialist thawed by
  Maki's love, now SHATTERED by her death at Ota Castle. A widower with the
  infant son Goichi (Maki's living image), his one tether. His heart burns to
  kill Hideyoshi; his executioner Hideyoshi and the cauldron are planted for
  ~1594. Register: plain, materialist, tender to Goichi and the dead Maki;
  speaks Kishu dialect with villagers; can rage.
- Maki (was principal): Goemon's wife; a Saiga hill girl, guileless, devoted,
  soft Kishu register. DEAD as of ch07 (shot and drowned at Ota Castle, having
  tied Goichi high to save him). The still centre of Goemon's grief; her double
  is Hatsuko and the Nanban-ji Madonna.
- Kazue (glossed, NOT principal): Maki's boyish younger sister, 15. Thread now
  CLOSED: abducted and raped by Moriichiro (ch06), then trafficked by Sakai/
  Nanban slavers to Luzon, where she is a sex-slave (ch07 dream-visions). Do not
  reopen or invent her fate.
- Goichi (glossed): Goemon and Maki's infant son, ~1yr2mo, Maki's living image
  and Goemon's tether in ch07-08.
- Hattori Hanzo: sharp, tireless, calculating, secretive; loyal to Ieyasu yet
  self-serving; a cold materialist with no sense of sin; his one real feeling is
  his love for Hatsuko. Off-stage in ch07; watch for his return in ch08.
- Torii Moriichiro (glossed): the yellow-eyed, right-forefinger-missing Koga spy;
  Ieyasu's/Hanzo's agent; a serial rapist with a "collar-slipping" escape trick.
  Kazue's rapist and abductor. Still at large; a live villain into ch08.
- Ieyasu: patient, dissembling, self-mastering ("the old badger"); off-stage in
  ch07; Goemon's break with him is complete.
- Hideyoshi: small, mean, rat-faced, an overwhelming vital force; a born
  strategist and shameless charmer; a lecher in his prosperity. As of ch07 he is
  KANPAKU and "the First Man under Heaven", master of the realm, and the
  destroyer of everyone Goemon loved. Goemon's target and eventual executioner.
- Hatsuko (principal): Hanzo's spirited young woman, Maki's exact double; daughter
  of the Shiroko merchant Kadoya Kyuemon; fought at Nagakute in ninja garb.
- Prior live threads and minor cast (Tamo/Sister Kiara the crypto-Christian nun;
  Chika, Hanzo's other woman; the Koga net; the Iga remnant; the Saiga/Negoro
  gunsmith Tsuda Kenmotsu Kazunaga, now Hideyoshi's man): as in the Batch 1-6
  handoffs.

## Where the story stands
Chapter 7 has destroyed Goemon's world: the Negoro-ji burned, the Saiga rising
drowned at Ota Castle, Maki killed, Kazue lost overseas to the slave-trade. The
materialist backbone is now the indictment of Hideyoshi's rule (the Taiko kenchi
and sword-hunt that made the peasant a half-serf; the overseas trafficking of
women). Goemon survives as a grieving widower at Nagao with the infant Goichi,
burning to avenge Maki on Hideyoshi. Hideyoshi has become Kanpaku and "the First
Man under Heaven". Chapter 8, "Death Throes" (断末魔), is the final chapter and the
payoff: Goemon's road to the cauldron. Expect his move against Hideyoshi, his
capture, and by tradition his execution by boiling in 1594. Watch for Hanzo,
Ieyasu, Hatsuko and Moriichiro to return.

## Batch 8 scope
Chapter 8, "Death Throes" (第八章 断末魔), PDF 461-530, printed folios 459-528 (the
divider page is PDF 461 = folio 459). The FINAL chapter and the longest (~70
pages). Batch the reading in 2-4 page image groups, keep the folio offset
(printed = pdf - 2), and re-measure at the opener. Carry every figure exactly
(find_figures.py plus eyeball; record even an EMPTY list). END the chapter at
folio 528 (PDF 530); do NOT translate the afterword 解説 (printed 529-534 / PDF
531-536) here. The FINAL batch (B09) carries the afterword as back matter, the
cover, the whole-book reconciliation sweep (check 12), term_ledger.md,
deep_audit.md and COMPLETION.md; plan B08 to leave B09 light.

## Open traps / environment
- Vertical-JP OCR is furigana-corrupted; translate from images, crop-verify with
  scripts/cropview.py. Regenerate the data/txt structural-aid OCR by hand.
- Glossary sectioned and CJK-keyed; apparatus_merge for notes+figures only. Note
  anchors LITERAL substrings in BODY paragraphs; note bodies numeric char refs,
  ending "(Printed folio NNN.)".
- NARRATION em-dashes: keep low; convert appositive dash-glosses (use parens
  where the source parenthesizes). Dialogue trailing/interruption em-dashes and
  quoted-document dashes are licensed.
- Use the macron romanization; keep "Osaka", "Kyoto", "Daito" plain. OPEN
  reconcile items for B09: Koya-san vs Mount Koya; Osaka vs Osaka-macron; Daito
  vs Daito-macron; Sasa vs Sassa Narimasa. Fix all + glossary at the reconcile.
- Kazue's fate is CLOSED (Luzon); Maki is DEAD. Do not reopen or invent either.
- Page-boundary resumptions drop content: re-read the last line of the previous
  PDF page before continuing.
- OMP_THREAD_LIMIT=1 for tesseract; check pgrep -c tesseract = 0 after OCR.
- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (java present).
- No data/pagemap/ for ch02-ch08 (only ch01 emits in-text page markers); qa
  still PASSES and every note cites its printed folio in prose.
- One checker regression test ("hook stands down on template stub") fails; a
  template corner case that does not affect real batch replies.
