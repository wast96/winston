# HANDOFF

## Message to paste into the next chat

```
The Stealthy Ones B05

Read CLAUDE.md, then STYLE.md, then HANDOFF.md, then book.json.

Do Batch 5 = Chapter 5 「ふたり」 / "The Two of Them" (PDF pages 259-360,
printed folios 257-358), end to end per the CLAUDE.md pipeline. Chapters 1-4 are
DONE; out/ch01_reading.md is the FROZEN register reference. This is a LONG
chapter (about 101 body pages): work through it in image batches of 2-4 pages,
writing out/ch05_reading.md incrementally, and keep every figure exact.

STYLE.md is the approved prose contract and is non-negotiable: clean, muscular,
contemporary English that hides the translation machinery. No dashed-in
appositive glosses in NARRATION (convert them to commas, colons, periods, or
parentheses); keep em-dashes only for genuinely interrupted or trailing
DIALOGUE and inside quoted classical text; break long sentences into short
varied ones; break dense paragraphs at each shift of focus; trim doubled
synonyms; active verbs; understatement in narration but keep the author's heat
where the source has it. Match ch01: em-dash near 0.3/1k in narration, sentence
median around 17 words. NOTE the ch04 lesson: the war/death set-pieces are
DELIBERATELY formal (samurai death-speeches, classical Taikoki quotes, the
Frois letters) and are register-exempt; do NOT contract them, but DO contract
the colloquial speakers (Goemon, the peasants, rough soldiers) so the whole
does not read stilted. Run check_register.py --ref out/ch01_reading.md
out/ch05_reading.md and expect an elevated-"shall" NOTE (deliberate) rather
than a failure.

BEFORE translating, read the final two pages of the previous unit's English (the
close of out/ch04_reading.md: Katsuie's farewell feast and dance; his and
Oichi's death-vigil; the parting of the three daughters, the eldest Ochacha
torn away crying "Mother!"; Hideyoshi on Mount Atago; the last assault on
Kita-no-shō; the boy Sakuma Jūzō's death; Katsuie firing the nine-storied keep
and showing himself at the topmost window as the flames rise). Chapter 5 opens
straight into the deaths of Katsuie and Oichi. STYLE.md and HANDOFF describe the
voice; those pages ARE the voice.

This is a Japanese book: vertical, right-to-left, heavy furigana. OCR with
lang=jpn_vert, psm 5, crop left 0.06 / right 0.96 / top 0.09 / bottom 0.935
(validated). Run render.py 259 360 then ocr_crop.py; verify pgrep -c tesseract
is 0. DO NOT rely on ocr_dual.py (hard-wired to chi_sim, wrong for JP) or
indents.py (horizontal-axis, calls a missing folio_present). The OCR is too
furigana-corrupted to translate from: TRANSLATE BY READING THE PAGE IMAGES
directly (data/png/p0NNNN.png; offset printed = pdf - 2), OCR as a structural
aid only, and crop-verify every proper name, number, date, and low-confidence
span by eye (PIL crop + Read). Carry every troop number, date, and toponym
exactly. Record source inconsistencies; render them as printed, never harmonize.
WATCH page-boundary resumptions: re-read the last line of each PDF page before
continuing (a sentence that spans two pages is where content silently drops).

Apparatus: notes via scripts/apparatus_merge.py, folio-cited, XHTML NUMERIC
character references only (ō = &#333;, ū = &#363;, em-dash = &#8212;) in note
BODIES; note ANCHORS must be verbatim (literal ō/ū, straight ASCII quotes, no
em-dash) substrings of the reading file, and must sit in a BODY paragraph, not
the chapter heading. Glossary is SECTIONED (people/organizations/places/terms)
and edited with a structure-preserving JSON round-trip or the Write tool, NOT
apparatus_merge (its glossary merge is flat and breaks the sectioned builder).
Reuse the glossary rows already decided (Katsuie, Oichi, the Lady Yodo,
Ochacha, Maa, Maeda Toshiie, Sakuma Morimasa, etc.); do not re-add or re-note
subjects already placed. Flag principals with "principal": true. Build with
build_reading_epub.py, then qa_epub.py and epubcheck
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
  ~430 paras, 29 notes (total 96), 24 glossary rows (Maki principal; total 14).
- Batch 3 (Chapter 3, "Surface and Underside", PDF 137-200 / folios 135-198):
  COMPLETE. ~17,700 words, 34 notes (total 130), 25 glossary rows. qa PASS,
  epubcheck 0/0/0/0.
- Batch 4 (Chapter 4, "War upon War", PDF 201-258 / folios 199-256): COMPLETE.
  ~16,140 words, 337 paras, 20 notes (total 150), 42 glossary rows (people 92,
  places 45, terms 25; no new principals), figures ch04 EMPTY. qa PASS,
  epubcheck 0/0/0/0, check_apparatus clean, register within tolerance. See
  PROGRESS.md.

## Branch note (read this)
Working branch is `claude/the-stealthy-ones`. This batch was started by the
harness on a stray branch (`claude/ch04-war-upon-war-4lkrp8`), which was
identical to origin/claude/the-stealthy-ones; the canonical branch was synced
to origin and the stray deleted locally. The stray remote ref never existed
(the delete-push reported "remote ref does not exist"), so nothing is stranded.
An older stray remote (`claude/stealthy-ones-b03-ygoea4`) may still exist on
GitHub pointing at ab1b943; harmless, delete from the UI if you wish. Do all
further work on `claude/the-stealthy-ones`.

## Tooling in place - do NOT revert
- `data/structure.json` from book.json (assemble.py and the builder read it).
  Offset printed = pdf - 2 (constant, no plates).
- Glossary is edited directly as a SECTIONED file (JSON round-trip or Write);
  apparatus_merge is used for NOTES only.
- Note anchors are LITERAL substrings of the reading file (ō/ū, straight ASCII
  quotes, no em-dashes), in BODY paragraphs; note BODIES use numeric character
  references (&#333; ō, &#363; ū, &#8212; em-dash, &#8217; apostrophe optional,
  CJK as &#nnnnn;). apparatus_merge validates; the builder refuses a
  heading-only anchor.
- Reading files stay plain ASCII apostrophes/quotes (typographized at render);
  ō/ū/ā, ç, and the em-dash (—) are the only non-ASCII used. Do NOT paste curly
  quotes in (a contraction pass slipped curly apostrophes in once; caught and
  converted).
- Fidelity method: translate from page images, not OCR. ocr_dual / indents are
  Chinese-template holdovers, not used.

## Renderings settled through Batch 4 (in glossary.json; reuse unchanged)
All Batch 1-3 renderings stand. Added in Batch 4:
People: Maeda Toshiie, Maeda Toshinaga, Sakuma Morimasa (Genba-no-jō), Shibata
Katsumasa, Yasuda/Sakuma Yasumasa, Shibata Katsutoyo, Takigawa Kazumasu, Yamaji
Masakuni (Shōgen), Nakagawa Kiyohide (Sebei), Kuwayama Shigeharu, Asakura
Yoshikage, Hori Hidemasa, Shima Sakon, Menju Shōsuke, Nakamura Bunkasai,
Manpukumaru, Ochacha (= the future Lady Yodo), Maa, Nejiri, Haigo Goemon,
Fukushima Masanori, Katō Yoshiaki, Katagiri Katsumoto, Wakisaka Yasuharu,
Sakuma Jūzō.
Places: Shizugatake, Lake Yogo, Kita-no-shō, Odani castle, Nagahama, Kinomoto,
Mount Ōiwa, Tsuruga, Fuchū, Mount Atago, Himeji, Ise, Yanagase.
Terms: hyōrōgan, shuriken, umajirushi, the Seven Spears of Shizugatake.
One-off minor names rendered-as-read (not glossed): see the "Rendered-as-read"
list in PROGRESS.md; reuse those spellings if any recur.

## Carry-forward VOICE SHEETS (consult at every scene)
- NARRATOR (the load-bearing voice): Murayama Tomoyoshi's own, writing 1962-63.
  Wry, materialist, sweeping in exposition, intimate in scene. Breaks the fourth
  wall constantly: quotes his sources by name (the Shinsho Taikōki, the Frois
  letters) and pokes at them, reads a wooden statue at Fukui, cites his own age,
  laments a beautiful girl ground down by a brutal age, sets loyalty against
  cold self-interest. Frank about sex, violence, and the body. Keep the wit, the
  interventions, the heat, and the tenderness.
- Goemon: the hero; hard-bitten Iga exception; a thief and shinobi who has quit
  the trade and wants free of the ninja life. Missing two front teeth. A
  thoroughgoing materialist whose heart is being thawed by Maki's love ("as
  spring melts thick ice"); could not conceive of dying without her. Sent by
  Ieyasu (via Hanzō) to watch the wars; a professed bystander who is drawn
  despite himself to Hideyoshi and, this chapter, moved to tears by Katsuie. Kills
  Yamaji with five shuriken (the deed the Taikōki gives to Kiyomasa). His future
  executioner (Hideyoshi) and the cauldron are planted for thirteen years hence.
- Maki (principal): Goemon's wife; a Saiga hill girl, guileless, devoted, soft
  Kishu register. The still centre of his life; knows nothing of distrust.
- Hattori Hanzō: sharp, tireless, calculating; loyal to Ieyasu yet self-serving;
  a gambler and cold materialist who works faith as pure technique. (Off-stage
  this batch; gave Goemon the nanban-iron chain mail.)
- Ieyasu: patient, dissembling; bides his time, watching Hideyoshi rise with "a
  face of perfect unconcern on the surface, and underneath a mounting
  impatience." Sends Goemon to see the Hideyoshi/Katsuie reckoning through.
- Hideyoshi (full antagonist, now central): small, mean, rat-faced, scuttling,
  yet an overwhelming taut vital force; a thoroughgoing realist and born
  strategist; flamboyant in body (huge snores, sneezes, everything); tireless.
  A spurned, calculating heart: long lusted after Oichi, cannot have her, and
  turns the whole grudge onto her daughter Ochacha, whom he takes "to settle to
  his heart's content." Nobunaga's "monkey" and "bald rat." Goemon's eventual
  executioner.
- Shibata Katsuie: proud old veteran (sixty), cast by history as a rash boar but
  in truth a plain, brave, feeling man with none of Hideyoshi's cunning; undone
  by Toshiie's betrayal; magnanimous even to his betrayer; dies with dignity and
  a farewell dance. Enma-faced in the Fukui statue.
- Oichi: Nobunaga's sister, "the fairest in the realm"; thirty-six/seven; twice a
  castle-wife on the brink (Odani, Kita-no-shō); chooses to die with Katsuie
  rather than live as the chattel of her son's killer. A deep, still, pale
  beauty with something raging under it.
- Ochacha (= the Lady Yodo, future): eldest daughter, seventeen, image of her
  mother; torn from Oichi crying "Mother!"; passes into Hideyoshi's keeping. The
  seed of the whole later tragedy (the cauldron, thirteen years on) is here.
- Prior live threads and minor cast (Oyu dead; Moriichirō, Torii Kihachirō,
  Chika, the Koga net; Hatsuko, Karasumaru, Etegi; the Iga remnant hunting
  Hanzō; the crypto-Christian strand): as in the Batch 1-3 handoffs.

## Where the story stands
Chapter 4 has carried the Shizugatake war to its end. Katsuie is beaten (Toshiie's
betrayal decided it), has retreated to Kita-no-shō, held his farewell feast, and
sent his three daughters out to Hideyoshi; as the chapter closes he fires the
nine-storied keep and stands at the topmost window with Oichi resolved to die
beside him. Goemon has watched it all from the ceiling, killed the traitor
Yamaji, and been shaken by Katsuie's dignity and Oichi's choice. Hideyoshi is
now the coming master of the realm, and has taken Ochacha (the future Lady Yodo)
in a spirit of appetite and revenge. Chapter 5, "The Two of Them" (ふたり), opens
straight into the deaths.

## Batch 5 scope
Chapter 5, "The Two of Them" (第五章 ふたり), PDF 259-360, printed folios
257-358. A LONG chapter (~101 body pages): batch the reading, keep the folio
offset (printed = pdf - 2), and re-measure at the opener. Expect the deaths of
Katsuie and Oichi and the aftermath of Shibata's fall, and Goemon's story
turning back toward Maki. Carry every figure exactly.

## Open traps / environment
- Vertical-JP OCR is furigana-corrupted; translate from images, crop-verify.
- Glossary sectioned; apparatus_merge for notes only. Note anchors LITERAL
  substrings in BODY paragraphs; note bodies use numeric character references.
- NARRATION em-dashes: keep near 0.3/1k from the first draft. The formal
  death-speeches / classical quotes are register-exempt (do not contract), but
  contract the colloquial speakers so the register check stays in tolerance.
- Use the macron romanization (Katō, Ōmi, Kita-no-shō, Taikōki, -no-jō, -rō;
  Azai not Asai). A whole-chapter reconcile of Koya vs Kōya (高野) is open for
  the final batch (glossary has "Koya-san", ch04 prose has "Mount Kōya").
- Page-boundary resumptions drop content: re-read the last line of the previous
  PDF page before continuing.
- OMP_THREAD_LIMIT=1 for tesseract; check pgrep -c tesseract = 0 after OCR.
- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (java present).
- No data/pagemap/ for ch02-ch04 yet (only ch01 emits in-text page markers); qa
  still PASSES and every note cites its printed folio in prose. Optional
  follow-up: add ch02-ch04 to data/pagemap.
- One checker regression test ("hook stands down on template stub") fails; a
  template corner case that does not affect real batch replies.
