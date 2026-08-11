# HANDOFF

## Message to paste into the next chat

```
The Stealthy Ones B06

Read CLAUDE.md, then STYLE.md, then HANDOFF.md, then book.json.

Do Batch 6 = Chapter 6 「土と水」 / "Earth and Water" (第六章 土と水, PDF pages
361-414, printed folios 359-412), end to end per the CLAUDE.md pipeline.
Chapters 1-5 are DONE; out/ch01_reading.md is the FROZEN register reference.
Work through the chapter in image batches of 2-4 pages, writing
out/ch06_reading.md incrementally, and keep every figure exact.

STYLE.md is the approved prose contract and is non-negotiable: clean, muscular,
contemporary English that hides the translation machinery. No dashed-in
appositive glosses in NARRATION (convert them to commas, colons, periods, or
parentheses); keep em-dashes only for genuinely interrupted or trailing
DIALOGUE and inside quoted classical text; break long sentences into short
varied ones; break dense paragraphs at each shift of focus; trim doubled
synonyms; active verbs; understatement in narration but keep the author's heat
where the source has it. Match ch01: em-dash near 0.3/1k in NARRATION, sentence
median around 17 words. The war/death set-pieces, quoted period documents
(Frois letters, chronicles, diaries, Kirishitan catechism, poems) are
DELIBERATELY formal and register-exempt; do NOT contract them, but DO contract
the colloquial speakers (Goemon, Maki in her soft Kishu register, Hatsuko, rough
soldiers, peasants) so the whole does not read stilted. Run check_register.py
--ref out/ch01_reading.md out/ch06_reading.md and expect an em-dash figure
inflated by dialogue and quoted documents, not a failure.

BEFORE translating, read the final two pages of the previous unit's English (the
close of out/ch05_reading.md): Goemon returns to Hamamatsu on the 15th of the
second month, finds Maki drugged and gone, follows the abductors to the castle
and hears Hanzo's voice, and grasps the whole trick: Ieyasu demanded Hatsuko;
Hanzo, unwilling to give her up, made Maki (Goemon's wife, her double) the
substitute and had her drugged and carried to Ieyasu, again and again, while
Goemon was sent off escorting Ogimaru to Osaka. A son, Goichi, has been born.
Goemon tells Maki everything (their vow of no secrets), forgives her utterly
("Maki is Maki!"), renounces the ninja and samurai world as beasts, and the
three of them vanish from Hamamatsu the next day. The chapter closes on the
author's question: "Where had the three of them gone?" STYLE.md and HANDOFF
describe the voice; those pages ARE the voice.

This is a Japanese book: vertical, right-to-left, heavy furigana. OCR with
lang=jpn_vert, psm 5, crop left 0.06 / right 0.96 / top 0.09 / bottom 0.935
(validated). Run render.py 361 414 then ocr_crop.py; verify pgrep -c tesseract
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
character references only (ō = &#333;, ū = &#363;, em-dash = &#8212;, curly
apostrophe = &#8217;, CJK as &#nnnnn;) in note BODIES; note ANCHORS must be
verbatim (literal ō/ū, straight ASCII quotes, no em-dash) substrings of the
reading file, and must sit in a BODY paragraph, not the chapter heading.
Glossary is SECTIONED (people/organizations/places/terms) and edited with a
structure-preserving JSON round-trip or the Write tool, NOT apparatus_merge (its
glossary merge is flat and breaks the sectioned builder). Reuse the glossary
rows already decided (Goemon, Maki, Hanzo, Hatsuko, Ieyasu, Hideyoshi, Chika,
Etegi, Karasumaru, Tamo/Kiara, Kashii, the Koga net, etc.); do not re-add or
re-note subjects already placed (grep notes.json and PROGRESS.md's
"NOT re-noted" list first). Flag any new principal with "principal": true. Build
with build_reading_epub.py, then qa_epub.py and epubcheck
(java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/the-stealthy-ones.epub).

Use the book's macron romanization throughout (ō/ū: Katō, Ōmi, Kita-no-shō,
Taikōki, Tenshō, Ōgaki, -no-jō, -rō; and Azai, not Asai). Cite printed folios in
every note; never invent bridging text; do not pause for approval. Deliver the
built EPUB in chat AND paste the next kickoff verbatim in a fenced code block.
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
  ~16,140 words, 337 paras, 20 notes (total 150). qa PASS, epubcheck clean.
- Batch 5 (Chapter 5, "The Two of Them", PDF 259-360 / folios 257-358):
  COMPLETE. ~28,000 words, 571 blocks, 24 notes (total 174), 25 glossary rows
  (people 108, places 51, terms 28; no new principals), figures ch05 EMPTY. qa
  PASS (174/174/174), epubcheck 0/0/0/0, check_apparatus clean, register within
  tolerance. See PROGRESS.md for the source-inconsistency and rendered-as-read
  lists.

## Branch note (read this)
Working branch is `claude/the-stealthy-ones`. This batch was started by the
harness on a stray branch (`claude/ch05-two-of-them-2w3vqj`), which pointed at
the same commit as origin/claude/the-stealthy-ones (through Batch 4); the
canonical branch was synced to origin and all Batch 5 work was done and pushed
on `claude/the-stealthy-ones`. Do all further work on
`claude/the-stealthy-ones`. If a fresh session starts on a stray per-task
branch, check out the canonical branch, reset it to origin, do the work there,
and delete the stray.

## Tooling in place - do NOT revert
- `data/structure.json` from book.json (assemble.py and the builder read it).
  Offset printed = pdf - 2 (constant, no plates).
- `scripts/cropview.py` (added Batch 5): fractional crop tool for eyeball
  verification. `cropview.py PAGE L T R B [--out path] [--scale n]`.
- Glossary is edited directly as a SECTIONED file (JSON round-trip or Write);
  apparatus_merge is used for NOTES only.
- Note anchors are LITERAL substrings of the reading file (ō/ū, straight ASCII
  quotes, no em-dashes), in BODY paragraphs; note BODIES use numeric character
  references. apparatus_merge validates; the builder refuses a heading-only or
  unmatched anchor.
- Reading files stay plain ASCII apostrophes/quotes (typographized at render);
  ō/ū/ā, ç, and the em-dash (—) are the only non-ASCII used. Do NOT paste curly
  quotes or accented Latin (é etc.) in; both slipped in once and were caught.
- Fidelity method: translate from page images, not OCR. ocr_dual / indents are
  Chinese-template holdovers, not used.

## Renderings settled through Batch 5 (in glossary.json; reuse unchanged)
All Batch 1-4 renderings stand. Added in Batch 5 (people): Honda Tadakatsu,
Ishikawa Kazumasa, Sasa Narimasa, Kennyo, Kyonyo, Ikeda Tsuneoki (= Shonyu),
Mori Nagayoshi, Ii Naomasa, Sakakibara Yasumasa, Chosokabe Motochika, Ogimaru
(= Hashiba Hideyasu / Yuki Hideyasu), Kakuban, Tsuda Kazunaga, Kazue, Goichi,
Aoba no Kaja. Places: Osaka, Nagakute, Komaki, Saigazaki, Tanegashima, Kunitomo.
Terms: the Shinobi-gumi, chagayu, the Red Guard (akazonae). One-off names
rendered-as-read (not glossed): see the long "Rendered-as-read" list in
PROGRESS.md; reuse those spellings if any recur.

## Carry-forward VOICE SHEETS (consult at every scene)
- NARRATOR (the load-bearing voice): Murayama Tomoyoshi's own, writing 1962-63.
  Wry, materialist, sweeping in exposition, intimate in scene. Breaks the fourth
  wall constantly: quotes his sources by name (the Shinsho Taikoki, the Frois
  letters, the Tamon-in diary, Inagaki Shisei, Murakami Naojiro) and pokes at
  them, cites his own 1963 visits to Negoro-ji, Mount Koya and Shodoshima,
  reads a beautiful girl ground down by a brutal age, sets loyalty against cold
  self-interest, and condemns the ruling class ("not human, beasts") from a
  frankly leftist stance. Frank about sex, violence, the body, and about
  Christianity as the religion of the oppressed (rendered with respect and
  irony). Keep the wit, the interventions, the heat, and the tenderness.
- Goemon: the hero; hard-bitten Iga exception; a thief and shinobi who has quit
  the trade. Missing two front teeth. A thoroughgoing materialist whose heart
  was thawed by Maki's love; now a father (son Goichi, born Tensho 12). A crack
  marksman (200-pace range). By the end of ch05 he has renounced the ninja and
  samurai world entirely and fled with Maki and Goichi to become a farmer. His
  future executioner (Hideyoshi) and the cauldron are planted for thirteen years
  hence. Register: plain, materialist, tender to Maki; can be dry and wry.
- Maki (principal): Goemon's wife; a Saiga hill girl, guileless, devoted, soft
  Kishu register ("あて", "〜や/〜じゃ", warm and simple). Her double is Hatsuko
  and the Nanban-ji Madonna. In ch05 she is drugged and given to Ieyasu as
  Hatsuko's substitute without ever knowing it (she remembers it as a recurring
  nightmare). The still centre of Goemon's life.
- Hattori Hanzo: sharp, tireless, calculating, secretive; loyal to Ieyasu yet
  self-serving; a cold materialist who works faith as pure technique and has NO
  sense of sin (the amoral man). His one point of real feeling is his fierce
  love for Hatsuko: to keep her from Ieyasu he substituted Maki. A chunin by
  birth who left Iga early, so weaker in body-arts than the genin-born Goemon.
- Ieyasu: patient, dissembling, self-mastering; bides his time. Called "the old
  badger" (tanuki). Rose at Komaki-Nagakute to near-parity with Hideyoshi
  (Suruga, Totomi, Mikawa, Kai, Shinano = 1.4M koku, an "immovable rock"). Gave
  up his son Ogimaru as Hideyoshi's hostage-heir. Took Hatsuko/Maki by drugged
  abduction. Once his own son Nobuyasu's death, now this: the author's coldest
  portrait of feudal power over bodies.
- Hideyoshi: small, mean, rat-faced, scuttling, yet an overwhelming vital force;
  a born strategist and shameless charmer ("iron-faced"), who weeps on command
  and wins men by brazen flattery (the Yatagawara prostration before Nobukatsu).
  "Simple in matters of the heart" next to the calculating Ieyasu. Building
  Osaka castle. Magnanimous even to brave enemies (Honda Tadakatsu). Goemon's
  eventual executioner; long lusted after Oichi, now settling the grudge on her
  daughter Ochacha (the future Lady Yodo).
- Hatsuko (principal): Hanzo's spirited young woman, 17; Maki's exact double; an
  only child of the Shiroko merchant Kadoya Kyuemon. Cheeky, manic, fearless;
  fought at Nagakute in ninja garb (wounded, a 10cm calf scar). Ieyasu, who bed
  her once during the Iga escape, now wants her; the whole tragedy turns on
  Hanzo's refusal to give her up.
- Tamo / Sister Kiara (Clara): the burned-face woman ninja of ch01's opening,
  now a Christian nun keeping the Iga crypto-Christian temple; her face and the
  Madonna's both resemble Maki and Hatsuko. Gentle, devout, but can flare.
- Prior live threads and minor cast (Oyu dead, betrayed by Torii Moriichiro, who
  reappeared this batch as the yellow-eyed Koga spy and was routed at Nagakute;
  Chika, Hanzo's other woman at Yono; the Koga net; the Iga remnant; the
  crypto-Christian strand): as in the Batch 1-4 handoffs.

## Where the story stands
Chapter 5 has carried the deaths of Katsuie and Oichi, the whole Komaki-Nagakute
war (Ieyasu's victory, credited to Hanzo's unified ninja corps), Hideyoshi's
diplomatic capture of Nobukatsu and the giving of Ogimaru as hostage, and the
firearms/Negoro/Saiga expository backbone. Its tragic close: Ieyasu demands
Hatsuko; Hanzo substitutes Maki and has her drugged and taken to Ieyasu
repeatedly while Goemon is away; Goemon discovers it, forgives Maki absolutely,
renounces the ninja/samurai world, and vanishes from Hamamatsu with Maki and
their infant son Goichi. Chapter 6, "Earth and Water" (土と水), takes up from
there.

## Batch 6 scope
Chapter 6, "Earth and Water" (第六章 土と水), PDF 361-414, printed folios
359-412 (the divider page is PDF 361 = folio 359). Batch the reading, keep the
folio offset (printed = pdf - 2), and re-measure at the opener. Carry every
figure exactly (find_figures.py plus eyeball; record even an EMPTY list).

## Open traps / environment
- Vertical-JP OCR is furigana-corrupted; translate from images, crop-verify with
  scripts/cropview.py.
- Glossary sectioned; apparatus_merge for notes only. Note anchors LITERAL
  substrings in BODY paragraphs; note bodies use numeric character references.
- NARRATION em-dashes: keep low; convert appositive dash-glosses. Dialogue
  trailing/interruption em-dashes and quoted-document dashes are licensed.
- Use the macron romanization (Kato, Omi, Kita-no-sho, Taikoki, -no-jo, -ro;
  Azai not Asai). The Koya vs Koya-san macron reconcile is still OPEN for the
  final batch (glossary "Koya-san"; ch04/ch05 prose "Mount Koya").
- Page-boundary resumptions drop content: re-read the last line of the previous
  PDF page before continuing.
- OMP_THREAD_LIMIT=1 for tesseract; check pgrep -c tesseract = 0 after OCR.
- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (java present).
- No data/pagemap/ for ch02-ch05 yet (only ch01 emits in-text page markers); qa
  still PASSES and every note cites its printed folio in prose.
- One checker regression test ("hook stands down on template stub") fails; a
  template corner case that does not affect real batch replies.
