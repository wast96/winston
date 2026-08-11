# PROGRESS

## Batch 1 = Chapter 1, "New Waves" (PDF 7-70, printed folios 5-68) — COMPLETE

The chapter is a bridging prologue to Murayama's Goemon saga: it sets the stage
of 1582 (the Honno-ji Incident, the fall of the Takeda, the ninja's turn to the
Tokugawa after the Tarao crossing, the Christian mission at the Nanban-ji and
the seminaries) and ends by turning time back a year to rejoin the hero,
Ishikawa Goemon, whose story proper starts in Chapter 2. Goemon himself is only
named here, not yet on stage.

### Deliverables shipped
- `out/ch01_reading.md`: full clean translation, 328 body paragraphs, 4 scene
  breaks, one chapter heading. 18,700 words. The correction surface.
- 67 footnotes in `notes.json` (folio-cited throughout), glossary rows in
  `glossary.json` (13 principals flagged for the Principal Characters page),
  page map for folio citations.
- `out/the-stealthy-ones.epub`: cumulative build, full pending-aware TOC.

### Checks run and results
- `qa_epub.py`: PASS (8 documents, 67 refs / 67 bodies / 67 backlinks all
  resolve, 48 pagebreak markers, all links resolve).
- `epubcheck 5.1.0`: 0 fatals / 0 errors / 0 warnings / 0 infos (store-clean).
- `check_apparatus.py`: 0 failures, 0 warnings.
- `check_register.py`: baseline recorded (this is the FROZEN REFERENCE), taken
  AFTER the voice-gate re-voice (see below): dialogue contractions 8.8/1k,
  shall-share 0%, em-dash 0.3/1k, rhythm CV 0.63, sentence median 17.

### Voice-gate revision (commissioner feedback)
The first build was judged too stilted. The commissioner rewrote the opening
paragraphs to model the target voice; from that comparison a prose contract was
written to `STYLE.md` (approved), and the WHOLE chapter was re-voiced to it.
The fix was structural, not lexical: kill the dashed-in appositive gloss, break
long periodic sentences into short varied ones, break dense paragraphs at each
shift of focus, trim doubled synonyms, de-translationese, prefer active verbs,
hold understatement in narration while keeping the author's heat where the
source has it. The register numbers show the change: em-dash use fell from
16.3/1k to 0.3/1k (the four survivors are all interrupted/trailing dialogue),
sentence median from 23 words to 17. All 67 footnote anchors were reconciled to
the new prose (12 re-pointed in notes.json; all resolve). Content fidelity
verified: 47 critical name/number tokens all present, 18,321 words (tighter than
the first draft's 18,693, from trimming, not cutting). `STYLE.md` now governs
every remaining chapter.

### OCR and fidelity method (important, book-specific)
- OCR: tesseract `jpn_vert`, psm 5, crop left 0.06 / right 0.96 / top 0.09 /
  bottom 0.935 (as specified; drops the top-corner folio, keeps all body text).
  Verified `pgrep -c tesseract` = 0 after each run.
- `ocr_dual.py` was NOT used: it is hard-wired to `chi_sim` and horizontal psm
  4/6, wrong for vertical Japanese. `indents.py` likewise measures a horizontal
  indent axis and calls a `folio_present` helper that does not exist in
  `ocr_crop.py`; it does not apply to vertical text and was not run. These are
  Chinese-template scripts not yet adapted to this book.
- Because vertical-Japanese OCR with heavy furigana bleed is too corrupt to
  translate from directly (e.g. 洛中 read as 潜中, 乞食 as 包食, 鴨川 as 嶋川),
  the chapter was translated by reading every page image (PDF 8-70) directly,
  with the primary OCR used only as a structural aid. This is the skill's
  high-value method (targeted crop-verification against the scan), applied
  wholesale for a literary text.
- Crop-verified spans (recorded here so a fresh checkout knows what was
  eye-read): the Nobutada vs Hideyoshi monogamy attribution (folio 10); the
  fortress-burning verb in Tamo's backstory (folio 13); the ten-member
  wood/earth/man escape lists (folio 17); the Koichi / Higashi-Yubune identity
  (folio 49). Every proper name, unit number, and date was read off the image.

### Parity / number checks (declared exception, with reason)
- `data/zh/` and `data/txt/` are gitignored (copyrighted source, never shipped).
  The assembled `data/zh/ch01.txt` is raw vertical-JP OCR whose paragraph
  segmentation (blank-line based) over-splits at furigana artifacts and page
  boundaries: 423 OCR "paragraphs" against 328 true print paragraphs read from
  the images. Positional bilingual pairing and `check_numbers` against this OCR
  side are therefore NOT meaningful and were not used as a gate. Fidelity was
  instead guaranteed by direct image reading plus targeted crop-verification of
  every name, number, and date. This is the honest posture for this book; if a
  later batch adapts the OCR pipeline for vertical Japanese, revisit.

### Figures
- None. This chapter's scan carries no photographs, plates, or line diagrams
  (it is unbroken body text). Recorded here as a deliberate empty figure list.

### Source inconsistencies noted, NOT harmonized (rendered as printed)
- Hattori Hanzo's age: folio 29 gives 42 ("going on forty-two"), folio 32 gives
  41. Rendered as printed at each spot; a one-year slip, left visible, not
  footnoted (the minor-discrepancy tier).
- "Padre Francisco Frois" (folio 25): the chronicler is usually Luis Frois. The
  differing given name is footnoted, not corrected.
- "Dutch pirates" in the arms trade (folio 67): an anachronism or loose usage;
  in 1582 the sea-traders were Portuguese and Spanish. Footnoted, not corrected.

### Note-density and the "NOT re-noted (already placed)" list
Density is front-loaded on the reference-heavy opening (the 1582 political frame
and the ninja-history digressions) and tapers naturally through the
character/comedy stretches (Etegi, Hatsuko, Karasumaru), which is healthy for
this material. Recurring subjects were noted at first appearance and
cross-referenced, not re-noted, thereafter: Nobunaga, Hideyoshi, Ieyasu, the
Ikko sect / Ishiyama war, the Tensho Iga War (placed on the Momochi-fort note),
Kashii, the jonin/chunin/genin ranks, the traditional units (shaku/sun/ri/cho/
ryo on one note; kan on another), and the author-as-interested-witness lens
(placed on the "first seize the soul" note, revisited only where the author's
intrusions are themselves the subject: the Special Higher Police line, the
socialist-Japan aside, the woman-in-bondage aside).

### Environment note
`setup.sh` installed the render/OCR stack and the jpn + jpn-vert packs cleanly.
One checker regression test fails: "hook stands down on template stub"
(kickoff_guard placeholder stand-down). It is a template-maintenance corner
case; the two cases that matter for a real batch reply both pass ("hook blocks
kickoff-less wrap-up", "hook passes compliant wrap-up"). PaddleOCR not installed
(expected).

## Batch 2 = Chapter 2, "A Warm Current" (第二章 暖かい流れ, PDF 71-136, printed folios 69-134) — COMPLETE

Goemon's story proper begins. The chapter runs from his quiet Sakai idyll with
his wife Maki, through his recruitment by Hattori Hanzo into Ieyasu's service
(as "Saeki Dennai"), to the engineered destruction of Nobunaga: the novel's
central conceit is that Ieyasu, through Hanzo's ninja net (the kunoichi Oyu,
Torii Moriichiro), sowed the disinformation that pushed Akechi Mitsuhide to
revolt, and that Goemon alone witnessed Nobunaga's death at the Honno-ji. It
closes on a long materialist meditation on death and rebirth (Kobo Daishi,
Maitreya, Christ) and the uneasy Goemon/Hanzo bond, mediated by Maki's double,
Hatsuko.

### Deliverables shipped
- `out/ch02_reading.md`: full clean translation, ~430 body paragraphs, one
  chapter heading, one Man'yoshu verse block (`{p}`), one folk-amulet block
  (`{p}`). The correction surface.
- 29 folio-cited notes in `notes.json` (book total 96), front-loaded on the
  Sakai/history digressions and tapering; every ch02 note cites its printed
  folio and cross-references ch01 where a subject recurs.
- 24 new sectioned glossary rows in `glossary.json` (Maki added as a principal,
  cast_order 1.5, right after Goemon; book total 14 principals). Edited with a
  structure-preserving insert, NOT apparatus_merge.
- `figures.json`: `ch02` recorded as a deliberate EMPTY figure list (unbroken
  body text; no photographs, plates, or line diagrams).
- `out/the-stealthy-ones.epub`: cumulative build, 2 of 8 chapters translated.

### Checks run and results
- `build_reading_epub.py`: OK (2/8 chapters, 96 notes, 48 pagebreaks).
- `qa_epub.py`: PASS (8 documents, 96 refs / 96 bodies / 96 backlinks resolve;
  48 page-list entries match 48 markers; all links resolve).
- `epubcheck 5.1.0`: 0 fatals / 0 errors / 0 warnings / 0 infos (store-clean).
- `check_apparatus.py`: 0 failures, 0 warnings.
- `check_register.py --ref out/ch01_reading.md`: within tolerance of the frozen
  reference. Contractions 13.6/1k (ch01 8.8 — a dialogue-heavier chapter),
  shall 29% (deliberate: the Kobo Daishi vow and two formal narrator asides),
  em-dash 3.9/1k, sentence median 14, rhythm CV 0.72.

### Register / em-dash note (important)
First pass ran em-dash at 6.8/1k; a targeted pass converted ~40 NARRATION
appositive/parenthetical dashes to commas, colons, periods, or parentheses,
bringing it to ~3.7/1k. The survivors are almost all legitimate interrupted or
trailing DIALOGUE, which this chapter has in unusual quantity: Goemon's dialect
murmurs (「...しもうたわ——」), Mitsuhide's broken speech overheard through the
floor, Nobunaga's death-cries, and Hatsuko's banter. That is faithful to a
source that is itself dash-heavy in speech here; it is not the ch01 defect
(dashed-in glosses), which was eliminated.

### OCR and fidelity method (unchanged from ch01)
- Rendered PDF 71-136 (render.py, 300 dpi); OCR jpn_vert psm 5, crop
  0.06/0.96/0.09/0.935; verified `pgrep -c tesseract` = 0. ocr_dual.py and
  indents.py NOT used (Chinese-template holdovers). Translated by reading every
  page image directly; OCR a structural aid only.
- Crop-verified by eye (recorded so a fresh checkout knows what was eye-read):
  temple names 本受寺 Honjuji / 浄福寺 Jofukuji (f.70,74); Kishu toponyms 雑賀崎
  Saigazaki / 鞆淵川 Tomobuchi-gawa / 細野 Hosono (f.73); 竜口 Ryuko / Momochi
  mansion (f.84); 納屋助左衛門 Naya Sukezaemon, dates 1562/1593 (f.77-79);
  Matsui Yukan, Kuki Yoshitaka, Miyoshi Yukiyasu, Nikko, Abe Hisanobu, sotetsu
  dimensions (f.79-84); the healing-amulet block and clan names (f.87-89);
  Saeki Dennai + 30 koku, 九度兵衛 Kudobei, Tsuji Yahei, the four Oda officers,
  Shinshi Rokuro-dayu (f.89-96); Kaisen death-poem 安禅不必須山水… and cited
  sources 真書太閤記 / 三河後風土記 (f.97); Mitsuhide's 500,000-koku fief (f.96);
  the atrocity numbers Hiei 1,600 / Nagashima 14,000 / Erin-ji 80+ (f.110);
  Yomoda Tajima-no-kami / Soda Yoichiro, the Mori brothers' ages (f.99-102);
  13,000 / Hidemitsu / Jono (f.105); the Chinese-elixir names and figures and
  the ninja terms rappa/nokizaru (f.129,132). Every proper name, unit number,
  and date in the chapter was read off the image.

### Source inconsistencies / readings noted, NOT harmonized (rendered as printed)
- 三好之康 (Miyoshi Yukiyasu, f.81) as donor of Myokoku-ji: the historical donor
  is usually given as Miyoshi Jikkyu (三好実休/義賢). Rendered as printed.
- 紅毛人 "red-haired foreigners" (f.72) for the Sakai foreigners: strictly the
  Dutch, an anachronism/loose usage in 1581 (as with ch01's "Dutch pirates").
  Rendered as printed, not footnoted (minor tier).
- Kuki's iron ships numbered "ten" (f.79); history usually counts six or seven.
  Noted in the footnote.
- Nagashima dead given as 14,000 (f.110); estimates run much higher. Noted.
- 斉青理大明神 in the healing amulet (f.88): an obscure folk-charm deity name,
  romanized "Seiseiri Daimyojin" as printed; reading uncertain, left as read.
- 担猿 (f.132), a regional term for low-grade ninja: furigana hard to read on the
  scan; rendered "nokizaru". If a later reader can read the furigana cleanly,
  confirm.

### Figures
- None. Recorded as a deliberate empty figure list (`figures.json` ch02: []).

### Note-density and the "NOT re-noted (already placed)" list
Density front-loaded on the Sakai free-city, ninja-history, and Christmas/
resurrection digressions; the character/comedy stretches (Maki, Oyu/Yoichiro,
Hatsuko/Etegi/Karasumaru) carry few or no new notes, which is healthy. Recurring
subjects were cross-referenced to their ch01 notes, NOT re-noted: Nobunaga,
Hideyoshi, Ieyasu, the Honno-ji (line noted afresh, subject cross-ref'd), Mount
Hiei, Erin-ji/Kaisen, the Iga crossing (= ch01's Tarao Crossing), Momochi/
Fujibayashi, the Bansenshukai, Takayama Ukon, Katsuyori/Tenmoku, the Special
Higher Police / author-persecution lens, shaku/sun/kan, and the nenbutsu. New
notes cover: the Chinu Sea, the Man'yoshu, Nabari, Negoro-ji, the Kirishitan
decalogue, the Nanzen-ji gate / Goemon legend, Kishimojin, the Maria image,
Naya/Luzon Sukezaemon, the Nihon Seikyo-shi, the Sakai egoshu, Kuki's iron
ships, the Myokoku-ji sotetsu, the jo, Kudobei/Shingen, the shichihode, the
koku, the Furinkazan banner, Mitsuhide's humiliation-as-motive, the Momochi=
Fujibayashi secret, Mori Ranmaru, "the enemy is at the Honno-ji", the Hiei/
Nagashima massacres, The Peanuts, En no Gyoja / the Peacock King, Kobo Daishi /
eternal meditation, and the author's materialism.

### Deferred (follow-up, does not block the build)
- No `data/pagemap/ch02.json` was built, so the ch02 chapter has no in-text
  printed-page markers (ch01 does). qa_epub still PASSES (it counts whatever
  markers exist). Every ch02 note cites its printed folio in prose, so notes
  remain followable. A later pass can add ch02 to data/pagemap for parity.

## Batch 3 = Chapter 3, "Surface and Underside" (第三章 表と裏, PDF 137-200, printed folios 135-198) — COMPLETE

The novel's method-chapter. Its title, 表と裏 (surface and underside), is its
procedure: the fall of Nobunaga and the rise of Hideyoshi are retold from the
"surface" (the Edo chronicle Shinsho Taikōki, the kabuki stage) and set against
the "underside" (Goemon, and Hanzō's ninja net). Threads: Oyu's death reported
by Torii Moriichirō (with the Yamazaki/Chūgoku-return legends the Taikōki
dresses up); Hanzō's crypto-Christian devotions at the Shōfuku-ji and the
riddle of his faith; the Iga-remnant ninja who brand Hanzō a traitor and ambush
him at the Maria image; the Kiyosu Conference and Nobunaga's grand Daitoku-ji
funeral, where Goemon, hidden in the ceiling, first sees Hideyoshi — the man who
will one day boil him. The chapter plants the cauldron (folio 181) and the real
last meeting at Yodo castle thirteen years on (folio 196), and closes on Goemon
at the crimson Yamazaki battlefield.

### Deliverables shipped
- `out/ch03_reading.md`: full clean translation, ~17,700 words, one chapter
  heading, 2 quoted-document vignette blocks (`{v}`: Nobunaga's "bald rat"
  letter to Nene; the kabuki father's letter). The correction surface.
- 34 folio-cited notes in `notes.json` (book total 130), front-loaded on the
  Taikōki/kabuki/history/religion allusions and cross-referencing ch01/ch02
  where subjects recur.
- 25 new sectioned glossary rows (`glossary.json`): 13 people, 8 places, 4
  terms. No new principals (book total 14). Edited via a structure-preserving
  JSON round-trip, NOT apparatus_merge.
- `figures.json`: `ch03` recorded as a deliberate EMPTY figure list.
- `out/the-stealthy-ones.epub`: cumulative build, 3 of 8 chapters translated.

### Checks run and results
- `build_reading_epub.py`: OK (3/8 chapters, 130 notes, 48 pagebreaks).
- `qa_epub.py`: PASS (15 documents, 130 refs / 130 bodies / 130 backlinks
  resolve; 48 page-list entries match 48 markers; all links resolve).
- `epubcheck 5.1.0`: 0 fatals / 0 errors / 0 warnings / 0 infos (store-clean).
- `check_apparatus.py`: 0 failures, 0 warnings.
- `check_register.py --ref out/ch01_reading.md`: em-dash 4.3/1k (ch01 0.3, ch02
  3.9 — in range), sentence median 17 (matches ch01), rhythm CV 0.69.
  Contractions 3.2/1k and shall 56% run high-formal and the tool flags DRIFT;
  this is a deliberate, documented deviation (see below), not the ch01 defect.

### The em-dash / register pass (important)
First-draft narration leaned on dashed-in appositive glosses (the ch01 defect):
em-dash ran 14.3/1k, with ~190 of 255 dashes in narration. A targeted pass
converted every NARRATION appositive/parenthetical dash to commas, semicolons,
colons, periods, or parentheses (script over quote-aware spans, then hand-fixed
~15 awkward joins and merged 11 page-boundary continuations that had become
paragraphs opening with ", ..."). Result: em-dash 4.3/1k; the ~86 survivors are
interrupted/trailing DIALOGUE and dashes inside quoted classical text (the
Taikōki battle-scenes, the funeral drama, the kabuki). This is the ch01
voice-gate fix applied to ch03.

The low contraction rate (3.2/1k vs ch01's 8.8) and high "shall" share (56%) are
inherent to this chapter, which is ~70% exposition and quoted classical text —
registers STYLE.md and the checker both mark EXEMPT: the Shinsho Taikōki battle
account and funeral drama, Lourenço's Christian sermon and the confession
dialogue, Nobunaga's court-letter, the Sanmon Gosan no Kiri kabuki and the
Goemon jisei, the Kiyosu council, the ninja-purists' declamation. The genuinely
casual dialogue (the roadside talk, Hideyoshi and the peasants, the Kyoto
townsfolk) has been contracted. Forcing the number higher would mean contracting
quoted ceremonial text, which STYLE forbids.

### OCR and fidelity method (unchanged from ch01/ch02)
- Rendered PDF 137-200 (render.py, 300 dpi); OCR jpn_vert psm 5, crop
  0.06/0.96/0.09/0.935; verified `pgrep -c tesseract` = 0. ocr_dual.py and
  indents.py NOT used (Chinese-template holdovers). Translated by reading every
  page image directly; OCR a structural aid only.
- Crop-verified by eye against magnified crops (recorded so a fresh checkout
  knows what was eye-read): the whole Shinsho Taikōki battle-quotation on the
  dense pages (PDF 141-142, 149) and the body-double reversal (PDF 149) were
  read at 2-3x column crops; every proper name, unit number, date, and money
  figure in the chapter was read off the image (the funeral cost figures on
  folio 188 — 50 gold / 300 silver / 10,000 kan / 1,000 bales rice / 1,100
  silver / 50 koku / 1,000 kan; the conversions 1 gold = 35 koku, 1,750 koku,
  1,680 koku, 4,200 bales; the Yamazaki battle 18,000 / 26,000 / 6,000+;
  Kiyomasa 22 / Yomoda 38 / Nobunaga 49 / Sanbōshi 7; 550 koku, 300,000 koku,
  120,000 koku; 185 / 197 / 13 / 124 / 200 / 382 years; 270m / 140m / 10 chō).
- check_numbers / positional-bilingual parity NOT used as a gate: the assembled
  vertical-JP OCR is furigana-corrupted and over-splits paragraphs, so
  positional pairing is not meaningful (documented at ch01). Fidelity guaranteed
  by direct image reading + eye-verification of every name/number/date.
- One faithfulness catch, fixed before shipping: a first pass DROPPED a sentence
  that spanned the PDF 148→149 page break (the Onna Taikōki / Sawa Juji source
  attribution and the Kōtoku-ji's modern address and war destruction); restored
  in full. A reminder that page-boundary resumptions are where content is lost.

### Source inconsistencies / readings noted, NOT harmonized (rendered as printed)
- Hanzō, hunting for who would ambush him (folio 172), thinks first of
  "Nobunaga's party" — though Nobunaga has been dead some weeks. Rendered as
  printed; the reasoning still works (he rules out the political actors and
  lands on the Iga remnant). Left visible, not footnoted (minor tier).
- 四方田但馬守政孝 Yomoda Tajima-no-kami (the lord, held in reserve) vs 四方田
  又兵衛 Yomoda Matabei (the veranda-fighter in the Taikōki quote): the author
  explicitly flags that whether the two were kin is unknown. Both rendered as
  printed. Recorded in the glossary row.
- The play (folio 194) calls the Ming emperor 神宗 "Shinsō, the twelfth
  emperor" — the Wanli emperor (Shenzong), whose reign postdates Goemon; a
  kabuki anachronism, rendered as printed.
- タムレ (folio 169), the second of the two modern dances the author names: the
  reading is uncertain on the scan; rendered "tamure" and footnoted as such.

### Note-density and the "NOT re-noted (already placed)" list
Front-loaded on the Taikōki/kabuki/history/religion allusions; tapers through
the action and dialogue stretches, which is healthy. Recurring subjects were
cross-referenced to their ch01/ch02 notes, NOT re-noted: Nobunaga, Hideyoshi,
Ieyasu, Mitsuhide, the Honnō-ji, the Tarao/Iga crossing, Momochi=Fujibayashi,
En no Gyōja / the Peacock King, Kōbō Daishi, the Ikkō sect / Ishiyama, Takayama
Ukon, the Nanzen-ji Goemon legend, the shaku/sun/ri/chō/koku/kan units, the
Special-Higher-Police / author-persecution lens (revisited on the postwar-
Americanization and materialist-religion notes). New notes cover: the surface/
underside method, the Shinsho Taikōki, Shizuka/Manabe, Bakin's Hakkenden, Enma,
the Seven Bands of Musashi, kamari/Kōjirin, Katō Kiyomasa, the Onna Taikōki
modern sources, the bashaku risings, the Chigachi/Hattori dual surname, the Ōnin
War, Yagyū, the dual-grave sanmai and the outcaste burial-workers, Steichen's
Christian Daimyō, Asano Nagamasa / the Five Commissioners, the sermon's social
charge, postwar Americanization, the materialist theory of religion, the Jesuit
nonresistance claim, the Twist/tamure, the Kiyosu Conference, the Five Constant
Virtues, the Daitoku-ji funeral / Sōken-in, the cauldron (kamairi), tenton no
jutsu, the empty coffin / Koretō Taiji-ki, the "bald rat" letter, Namiki Gohei /
Sanmon Gosan no Kiri, the Goemon jisei, the Yodo-castle foreshadow, Azai/Oichi/
Yodo, and the Battle of Yamazaki / Tennōzan.

### Rendered-as-read, not glossed (one-off Taikōki / Kiyosu / kabuki names)
Yomoda Matabei, Kimura Jirō-uemon, Murai Matabei, Yasuda Sakubei, Kajiwara
Matauemon, Akashi Gitayū, Kuroda Kanbei, Nakagawa Sebei, Fukushima Ichimatsu,
Katagiri Sukesaku, Asano Hachirōzaemon, Ikeda Shōnyū(sai), Hachiya Dewa-no-kami,
Tsutsui Junkei, Sakuma Genba/Morimasa, Maeda Matazaemon/Toshiie, Sassa
Kuranosuke/Narimasa, Mori Katsuzō, Mōri Kawachi-no-kami, Hosokawa Fujitaka/
Tadaoki, Gamō Ujisato, Takigawa Kazumasu/Shōgen, Shibata Katsutoyo; Sō Sokei and
Namiki Gohei (kabuki); Kurihara Ryūan, Sawa Juji, the third Enjaku (cited
authors/actors); Kakunen and Seishin (the Shōfuku-ji monks); Kadoya (ch02).


## Batch 4 = Chapter 4, "War upon War" (PDF 201-258, printed folios 199-256) - COMPLETE

Chapter 4 is the war chapter. It carries the Shizugatake campaign end to end:
Hideyoshi's tireless New Year at Himeji, the Ise expedition, the long stand-off
around Lake Yogo, Yamaji's betrayal and his family's crucifixion, Sakuma
Morimasa's raid on Mount Oiwa, Hideyoshi's celebrated Great Return from Ogaki,
Maeda Toshiie's decisive withdrawal, the Seven Spears, and the fall of
Kita-no-sho, ending with Katsuie atop the burning nine-storied keep. Goemon
watches throughout as Ieyasu's observer, is drawn against his will to Hideyoshi,
and quietly reckons his own life against Maki's love. The chapter's emotional
core is the death-vigil of Katsuie and Oichi and the parting of their three
daughters (the eldest, Ochacha, the future Lady Yodo).

### Deliverables shipped
- `out/ch04_reading.md`: full clean translation, 337 body paragraphs, ~16,140
  words, one chapter heading, no scene breaks (continuous prose). The
  correction surface.
- 20 footnotes in `notes.json` (folio-cited; book total 150), 42 new glossary
  rows (`glossary.json`: people 67->92, places 32->45, terms 21->25). No new
  principals. Figures ch04 EMPTY (text-only chapter; no plates or line art).
- `out/the-stealthy-ones.epub`: cumulative build, 4 of 8 chapters, full
  pending-aware TOC.

### Checks run and results
- `qa_epub.py`: PASS (15 documents, 150 refs / 150 bodies / 150 backlinks all
  resolve, 48 pagebreak markers, all links resolve).
- `epubcheck 5.1.0`: 0 fatals / 0 errors / 0 warnings / 0 infos (store-clean).
- `check_apparatus.py`: 0 failures, 0 warnings.
- `check_register.py --ref out/ch01_reading.md`: within tolerance after a
  targeted contraction pass. Final: contractions 6.1/1k (ref 8.8, 0.70x),
  shall-share 23% (elevated but DELIBERATE: confined to the formal death-speeches
  of Katsuie and Oichi, the Menju/Shima Sakon Taikoki set-piece, and the Frois
  letter), em-dash 1.0/1k (ref 0.3; the surplus is all interrupted/passionate
  dialogue and quoted classical text, not narration appositives), sentence
  median 16, rhythm CV 0.69. Narration em-dashes were converted to
  commas/colons/periods/parentheses from the first draft, per the ch03 lesson.
- Tail verification (rule 4 corollary): the final page (folio 256) was
  translated directly from the p0258 image and re-checked; Katsuie drawing up
  the ladder, firing the keep, and appearing at the ninth-story window all match.

### OCR and fidelity method (book-specific, unchanged)
- OCR: tesseract `jpn_vert`, psm 5, crop left 0.06 / right 0.96 / top 0.09 /
  bottom 0.935. `pgrep -c tesseract` = 0 after the run. OCR used as a
  STRUCTURAL aid only; the chapter was translated by reading every page image
  (PDF 202-258) directly, since vertical-JP OCR with furigana bleed is too
  corrupt to translate from. `ocr_dual.py` / `indents.py` not used
  (Chinese-template holdovers).
- Crop-verified by eye (recorded so a fresh checkout knows what was eye-read):
  the 900-plus / 490,000-koku / 75,000 / 60,000-30,000 / 8,500 / 550m / 420m
  figures; the Seven Spears roster and its koku rewards (Masanori 3,500, the
  rest 3,000 each, Ishiko Hyosuke's brother Nagamatsu 1,000); the hyorogan
  recipe (30/5/30/30/30 monme, 5 bu); the disputed "prowess" line at folio 211
  (confirmed the source reads 勝家軍, Katsuie's front line); the new name Koichi
  of Higashi-Yubune (東湯舟の小一). check_numbers / positional parity NOT used
  as a gate (documented at ch01: the vertical-JP OCR over-splits and mangles).

### Source inconsistencies / readings noted, NOT harmonized (rendered as printed)
- OICHI'S AGE: folio 246 gives her as thirty-seven, folio 255 as thirty-six.
  Both rendered as printed; footnoted at folio 255.
- The seven captives (Yamaji's family), seized by Kimura, a Hideyoshi-side
  officer at the Shinmei fort, are crucified "on the left wing of Katsuie's
  front line" (勝家軍, crop-confirmed). Rendered as printed; the oddity is left
  visible (minor tier, not footnoted).
- Morimasa's brother is named Yasuda Yasumasa at folio 205 and Sakuma Yasumasa
  at folio 223. Both rendered as printed; recorded in the glossary row.
- Manpukumaru's killing is laid to Hideyoshi's hand (Oichi's speech and the
  narrator), on Nobunaga's order. Historically the order was Nobunaga's; the
  footnote says so and renders the text as printed.
- Sakuma Juzo (Maa's betrothed): fourteen at the betrothal "last year" (folio
  249), fifteen at the final assault (folio 256). A year's passing; not
  footnoted (minor).

### Rendered-as-read (one-off minor figures/places NOT given glossary rows)
Reuse these spellings if any recur. Officers: Ogane Tohachiro, Kimura Shigekore,
Kimura Kinainosuke, Osaki Uemon-no-jo, Nomura Katsujiro, Tonami Hayato, Hori
Hidemasa (glossed), Ogawa Suketada, Kinoshita Hanuemon, Ujiie Naomichi, Inaba
Ittetsu, Yamaoka Kagetaka, Tominaga Shinrokuro, Hirano Nagayasu, Kasuya
Sukeuemon-no-jo, Sakurai Sakichi, Ishiko Hyosuke, Achako (waiting-woman), Iseya
(draper). Battlefield hills/points (rendered as read): Uchinakao, Fumuro, Mano,
Doki-yama, Shinmei-yama, Gongen-zaka, Kineyama, Kitsunezuka, Bessho-yama,
Shige-yama, Nakatani, Anegawa, Iinoura, Chausu-yama, Shufukuji-zaka,
Shimizu-dani, Hachigamine, Iwasaki, Hayashidani-yama, Gyoichi, Niwato-hama,
Shimo-Yogo, Kokufu, Seki, Mine, Takatsuki(Omi), Kinomoto (glossed), Sekigahara,
Tarui, Fujikawa, Odani (glossed), Imajo. Terms rendered in place: kusazuri,
shikoro, shinobi-no-o, mete-zashi/yoroi-doshi, Rakan-ken, Ryuo-ken, suigetsu,
kubi-jikken, Soshu Sadamune, "brush-head" helmet, byakudan-migaki, tentsuki
crest, jumonji-yari.

### NOT re-noted (already placed earlier in the book; cross-referenced)
koku (ch02), ri/league (ch01), kan (ch01), shaku/sun (ch01), the hour-names
(ch01), kamari (ch03), tenton no jutsu (glossary), Enma (ch03), the Shinsho
Taikoki (ch03), Luis Frois and Valignano (ch01), Momochi Sandayu (ch01),
Ishiyama Hongan-ji (ch01/02), Ichijodani (ch01), Azai Nagamasa and Odani (ch03),
Oichi and the Lady Yodo (ch03), Koichi/Karasumaru/Etegi/Hatsuko (earlier
batches), Kiyomasa=Toranosuke (ch03). Prefer cross-referencing these.

### For the whole-book reconciliation (final batch)
- Koya/Kojirin spelling: the pre-existing glossary renders 高野山 as "Koya-san"
  (no macron); ch04 prose uses "Mount Koya" with the macron ("K" + long o) at
  folio 246. Pick one at the final reconcile.
- The Taikoki is rendered "Shinsho Taikoki" (with the long-o macron on Taiko),
  matching ch03.

## Batch 5 = Chapter 5, "The Two of Them" (PDF 259-360, printed folios 257-358) — COMPLETE

The longest chapter and the emotional pivot of the book. It opens straight into
the deaths of Katsuie and Oichi, follows Goemon home to Maki, then runs a long
expository arc (the Shugendo/yamabushi origins of ninjutsu, the wealth and
warrior-monks of Negoro and Saiga, the coming of the matchlock to Tanegashima
and its spread through Negoro, Sakai and Kunitomo, the gunpowder and saltpeter
trade) before turning to the Komaki-Nagakute war of Tensho 12 (1584), where
Hanzo's unified ninja corps hands Ieyasu the victory. The last third is the
tragedy: Hideyoshi wins over Nobukatsu by diplomacy; Ieyasu, at peace at last,
demands Hatsuko; Hanzo, unwilling to give her up, substitutes Maki (Goemon's
wife, her double) and has her drugged and carried to Ieyasu, again and again,
while Goemon is sent away escorting Ogimaru to Osaka. Goemon discovers it,
forgives Maki absolutely, renounces the ninja and samurai world, and the three
of them (a son, Goichi, has been born) vanish from Hamamatsu.

### Deliverables shipped
- `out/ch05_reading.md`: full clean translation, one chapter heading, ~28,000
  words, 571 blocks (verse lines for the two folk songs, the Kokawa hymn, and
  Kyonyo's poem marked with `{p}`). The correction surface.
- 24 footnotes in `notes.json` (folio-cited; book total now 174). New glossary
  rows: 16 people, 6 places, 3 terms. Figures ch05 recorded EMPTY (a text-only
  novel; the one find_figures hit on p276 is a dense-text-column false positive,
  confirmed by eye).
- `out/the-stealthy-ones.epub`: cumulative build, 5 of 8 chapters.

### Checks run and results
- Translated from the page images directly (OCR furigana-corrupted, as expected);
  every proper name, troop number, date, unit and toponym crop-verified by eye
  where the reading was not plain. Recorded crop-verifications include the 250
  koku of Hanzo's raise (OCR read 350), the moat "forty tatami / seventeen
  tatami" (an odd unit, rendered as printed), the 3/6 and 3/10 dates, the
  rampart dimensions, and the Kazue-age and Tokika-yama readings.
- `qa_epub.py`: PASS (174 refs / 174 bodies / 174 backlinks all resolve).
- `epubcheck 5.1.0`: 0 fatals / 0 errors / 0 warnings / 0 infos.
- `check_apparatus.py`: 0 failures, 0 warnings.
- `check_register.py --ref out/ch01_reading.md`: within tolerance (contractions
  9.5/1k, 1.07x ref; shall 0%; em-dash 8.5/1k; sentence median 15; rhythm 0.68).
  The em-dash total is high ONLY because the chapter is exceptionally
  dialogue-heavy (the whole last third is dialogue, where the source's dashes
  mark genuine trailing and interrupted speech) and because the two long Frois
  letters carry the author's own dashed editorial insertions (register-exempt
  quoted documents). Narration appositive dash-glosses were hunted down and
  converted to commas, colons or parentheses; the remaining narration dashes are
  author fourth-wall asides and dramatic breaks.
- Number-parity and content checks (check_numbers/check_content) need a paired
  source file; none exists for this image-translation batch (same as ch02-ch04).
  Numbers were carried by crop-verification at write time instead. The tail was
  verified against the scan as the final pages were written (rule 4 corollary).

### Register note (ch04 lesson applied)
The war and death set-pieces are deliberately formal and were NOT contracted:
Katsuie's death-speech, the Frois Osaka-castle and moat letters, the Teppoki
quote, the Tamon-in diary, the Kokawa pilgrim-hymn, and Kiara's catechism (a
faithful rendering of Kirishitan doctrine). The colloquial speakers (Hatsuko,
Maki in her soft Kishu register, Goemon, the rough soldiers, the modern temple
priest) were contracted so the whole does not read stilted.

### Source inconsistencies (rendered as printed, never harmonized)
- Kazue's age: at folio 263 Maki calls her sister "nine years younger" (about
  seven at their parting); at folio 273 the author's family register makes her
  "four years younger." Both rendered as printed; footnoted at folio 273.
- Hideyoshi's departure from Osaka: folio 280 gives the 10th of the third month
  (advancing to Sakamoto); folio 296 gives the 21st (the march to the front).
  Both rendered as printed; not footnoted (the reader can read it as a first
  move and a second).
- The Shinobi-gumi is "some two hundred" ninja in the author's own voice (folio
  293) but "three hundred" in the enemy's hearsay (folio 313). Rendered as
  printed; the enemy figure is plainly rumor and is left to stand.
- The Nagakute moat is measured in "tatami" (jo) of width and depth in the Frois
  letter (folio 281); an unusual linear use of the unit, rendered as printed.
- Hanzo, in his rage before the Madonna, charges Ieyasu with having "his own
  mother killed"; historically false (Odai-no-kata outlived him). Rendered as
  printed and footnoted as the measure of Hanzo's bitterness.

### NOT re-noted (already placed earlier in the book; cross-referenced)
En no Gyoja Ozunu / Shugendo (ch02), Kobo Daishi & Shingon (ch01/ch02), the
Nagashino battle (ch01), Ichijodani & the Asakura (ch01), Kashii & Tamo (ch01),
the Iga crossing (ch01/ch02), Luis Frois / Valignano / the Nanban-ji / Deus /
garasa / Organtino / Lourenco (ch01), the Ikko sect & Ishiyama Hongan-ji
(ch01/ch02), Kuki's iron ships (ch02), Kato Toranosuke = Kiyomasa (ch03), the
cauldron (ch03), aloeswood / sanmai / Enma (ch03), the Man'yoshu (ch02), Santa
Maria & the child Kirishito (ch02), the Seven Spears of Shizugatake (ch04), the
nine-storied keep & Oichi (ch04), koku/ri/ken/shaku/sun/cho/tsubo/kan units and
the hour-names (ch01-ch04), kamari (ch03), the intercalary month (ch04), Honda
Tadakatsu (ch01). Prefer cross-referencing these.

### Rendered-as-read (one-off names/places NOT given glossary rows)
Reuse these spellings if any recur. People: Bunkasai (glossed as Nakamura
Bunkasai), Idomotoya Genbei, Saiga Magoshichi, Soeda Ryushun, Nakagawa Kan'emon,
Nakagawa Seizosu, Nabeta Naitosuke, Kinoshita Kangeyu, Kani Saizo (noted),
Mizuno Tadashige, Osuga Yasutaka, Nakamura Kazuuji, Inaba Ittetsu, Tsugawa
Genbanojo, Okada Nagato-no-kami, Asai Tamiyamaru, Oda Nagamasu, Horio Yoshiharu,
Tsutsui Junkei, Tsutsui Sadatsugu, Miyoshi Hidetsugu (= Hidetsugu), Yagoemon,
Kiino, Gisuke, Niwa Ujitsugu & Ujishige, Shibatsuji Seiuemon, Tachibanaya
Matasaburo ("Teppo Mata"), Tanegashima Tokitaka & Oribe-no-jo, Shinokawa
Koshiro, Yasaka Kinbei & Wakasa (noted), Nanpo Bunshi, Kakuban (glossed),
Ikenaga Kuro Choa, Murakami Naojiro, Tsuboi Sakae (noted), Gaspar Vilela
(glossed ch01). Places: Hosono, Tomobuchi R., Kishi R., Kino R., Nagao, Mount
Tokika, Wakayama, Katsuragi, Mii-dera, Omine, Daigo-ji, Sanbo-in, Renge-jo-in,
Kakuban Hill, Kokawa-dera, Ebisujima, the Hawk's Nest, Goboyama, Akibayama,
Sagi-no-mori, Ninomiya-yama, Futatsubori, Iwasaki-yama, Gakuden, Obata, Irogane,
Fujigatake, Yarigane, Hachiman wood, Kanare R., Shonai R., Yada R., Seto, Inaba,
Odome/Noda/Matsukawado, Kamijo, Okusa, Ikeuchi, Haguro, Kaneyama, Kariyasuga,
Hoshizaki, Matsushima, Utsumi, Chita, Kagamigahara, Nagashima, Kishiwada, Yumi-
cho, Takajo-machi, Shiroko, Shodoshima (Komi/Kobe/Tonohama), Nagara & Machiya
rivers, Yatagawara. Terms rendered in place: goma, tokin, oizuru, sashimono,
kubi-jikken / kubi-taimen / kubi-mishiri / kubi-zoroe / kubi-kesho, sanbo,
san-san-kudo, jinshogi, musha-bashiri, ishibiya, compisan, kurusu, inheruno,
tendo, onchо (grace), Adan & Eva, the Iga sleeping-drug.

### For the whole-book reconciliation (final batch)
- The Koya/Koya-san macron question is still open (glossary "Koya-san"; ch04 and
  ch05 prose use "Mount Koya"). Settle at the reconcile.
- Hideyoshi's shifting titles/names (Hashiba Chikuzen, "Chikuzen-dono" in Frois)
  are rendered as they appear; consistent with the glossary "Hideyoshi".

## Batch 6 = Chapter 6, "Earth and Water" (第六章 土と水, PDF 361-414, printed folios 359-412) — COMPLETE

The chapter turns from the Goemon/Maki tragedy of ch05 to the destruction of
the Negoro-Saiga world. Goemon, Maki and their infant Goichi take refuge at
Maki's home village of Nagao in Kishū, on temple land under the Negoro-ji. The
first half is Murayama's expository and materialist backbone: the geography of
the Kii peninsula and the Kino River; a scathing anticlerical anatomy of the
temple economy and the fear-of-death it feeds on; the yamabushi/Shugendō
origins of the warrior-monks and ninjutsu; the wealth and arms of the Negoro-ji,
its Great Pagoda, and its aged gun-pioneer Tsuda Kenmotsu Kazunaga (with the
Koga spy Moriichirō lodged at the Suginobō). The second half is the war: Maeda
Gen'i's sword-edict, the mass muster at Negoro, the class-solidarity scene on
the riverbed, Kazue's abduction and rape by Moriichirō (who frames Goemon to a
Takayama patrol and carries her off), the capture and suicide of the abductor
"Purple Scale," and Hideyoshi's Kishū campaign of Tenshō 13 (1585) ending in the
storming and burning of the Negoro-ji — told twice, once through two long
Shinsho Taikōki set-pieces (the Amano/Unkai and Enkaku/Shima Sakon duels) and
then flatly denounced by the author: "the truth was no such gorgeous thing. It
was terror and madness... men turned back into beasts."

### Deliverables shipped
- `out/ch06_reading.md`: full clean translation, one chapter heading, 423 body
  paragraphs, ~16,200 words. Two register-exempt Shinsho Taikōki battle-quotes
  rendered inline as quoted paragraphs (matching ch03/ch05). The correction
  surface.
- 9 footnotes in `notes.json` (folio-cited; book total now 183): Kudoyama/Sanada
  Yukimura/the sequel, Shirakawa's "three things," the Great Pagoda (Daitō,
  extant National Treasure), the Age of the Latter Law (mappō), the sword-hunt,
  the historical Kishū campaign, Dainichi Nyorai (cross-ref Fudō), the Water
  Margin, and the war-tale reciters (kōshaku).
- Glossary: 3 people (Hidenaga, Yagoemon, Gisuke), 3 places (Kishiwada,
  Kudoyama, Nagao), 3 terms (the sōhei, the sword-hunt, the Great Pagoda of
  Negoro / tahōtō). No new principals. Edited via structure-preserving JSON
  round-trip, NOT apparatus_merge.
- `figures.json`: `ch06` recorded as a deliberate EMPTY list (text-only chapter;
  `find_figures.py 361 414` returned nothing).
- `out/the-stealthy-ones.epub`: cumulative build, 6 of 8 chapters translated.

### Checks run and results
- Translated from the page images directly (vertical-JP OCR furigana-corrupted,
  as for ch01-05); OCR a structural aid only. Every proper name, troop number,
  date, unit and toponym crop-verified where not plain. Crop-verifications
  recorded: the 鶏冠山 = Mount Tokika reading (reused from ch05); the tax figures
  on folio 362 (one koku four to yield / six to nengu / bare five to left / two
  koku eaten / one koku five to short) and that it is Yagoemon's reckoning, not
  Goemon's; the Sengokubori/Hama/Shakuzen-ji commander roster (folios 386-387);
  and 葉津子 = Hatsuko (the principal, confirmed against glossary — the woman
  "false ninja" Moriichirō attacked at Nagakute a year before).
- `build_reading_epub.py`: OK (6/8 chapters, 183 notes, 48 pagebreaks).
- `qa_epub.py`: PASS (15 documents, 183 refs / 183 bodies / 183 backlinks all
  resolve; 48 page-list entries match 48 markers; all links resolve).
- `epubcheck 5.1.0`: 0 fatals / 0 errors / 0 warnings / 0 infos (store-clean).
- `check_apparatus.py`: 0 failures, 0 warnings.
- `check_register.py --ref out/ch01_reading.md`: within tolerance. em-dash
  1.0/1k (ref 0.3; the surplus is interrupted/trailing DIALOGUE and the two
  quoted Taikōki set-pieces, not narration appositives — those were converted
  to commas/colons/periods), sentence median 16 (ref 17), rhythm CV 0.68 (ref
  0.63). Contractions 20.7/1k run high because the chapter is exceptionally
  dialogue-heavy (villagers, priests, Goemon, Maki, Kazue all colloquial). The
  "shall" flag is a 2-token artifact: both are register-exempt (the quoted
  transmigration monologue and Maeda Gen'i's quoted sword-edict).
- Tail verification (rule 4 corollary): the final page (folio 411) and the two
  Taikōki quotes were read directly against the p411-413 images; the closing
  line ("men turned back into beasts") and both duels match the scan.

### Source inconsistencies / readings noted, NOT harmonized (rendered as printed)
- The author's round-number arithmetic does not perfectly fit a strict Tenshō
  13 (1585): the Daitō is "four hundred and fifty-eight years" old since its
  1129 founding (folio 368; = 1587) and "three hundred and eighty years" old at
  his 1963 visit (folio 370; = 1583); Iwasakibō's oration gives "four hundred
  and forty years" since Kakuban (folio 383) and "the hundred-and-seventh
  Emperor" (Ōgimachi is usually counted the 106th). All rendered as printed;
  these are the author's approximations, not footnoted (minor tier).
- The Taikōki's "fifteen thousand" at the forts (folio 399) is corrected by the
  author himself in the same breath ("half that or less"); rendered as printed.
- Mount Kōya said to have been "granted by the Emperor Kanmu" (folio 363);
  history usually credits Emperor Saga's 816 grant to Kūkai. Rendered as printed
  (minor tier, not footnoted).

### Rendered-as-read (one-off names/places/terms NOT given glossary rows)
Reuse these spellings if any recur. People: Ōtomo no Kujiko, the Retired
Emperors Toba/Kanmu/Kazan/Shirakawa, Kujō Kanezane, Minamoto no Yoshitsune,
Hatakeyama Motokuni & Akitaka, Yusa Kawachi-no-kami Masakata, Maeda Gen'i, Hori
Kyūtarō Hidemasa, Nagaoka Yoichirō Tadaoki, Gamō Chūsaburō Ujisato, Hasegawa
Tōgorō Hidekazu, Takayama Ukon-tayū Nagafusa, Iwasakibō, Sugimotobō, Iwamurobō,
Hyōe-Saburō, Gennojō, Denbei, Genzaburō, the old woman Yoshino, Yamauchi
Saburō-tayū, Takayanagi Kenmotsu, Takamatsu Tōnai, Suzuki Magoichi, Ten'i
Hamazaemon, Tsuya Magokurō, Nakamura Magoheiji, the Purple Scale (Murasaki no
Uroko), Amano Gen'uemon, Unkai, Enkaku, Han'nyo, Rendatsu, Kiichi Hōgen Kenkai,
Iizasa Chōi, Matsumoto Bizen-no-kami, Kawasumi (Kawasumi Taikōki), Oze Hoan
(Hoan Taikōki), Yamatoya Tarōbei, Kiino (Maki's late mother). Places: Ōmine/Kii/
Hatenashi ranges, Kishū Fuji, Wakanoura, the Waka River, Katsuragi, the Gyōja
Hall, Uenoyama, Kumatori, Sengokubori, Shakuzen-ji, Hama castle, Oyama Pass,
Ochaya Gotenyama, Kobayashidera-machi, Takaya castle, Ryūmon, Mount Kurama.
Terms rendered in place: goma (self-glossed), the Yoshitsune torch, kunai/
tsubokiri/shikoro/tetsubishi/kurogaki, earth-/water-/man-hiding (do-/sui-/jin-
ton), the art of the changed shape (henshi-jutsu), the collar-slipping method,
the four-legged practice, the art of the shifting decoy voice, esoteric prayer
(kaji-kitō), the rite of subjugation (chōbuku), the roban, the central pillar,
the nyoi hōju wish-jewel, the nine-ringed finial, the Niō, the Burning Hell,
nyobon, jingasa, abatis (sakamogi), the bamboo palisade.

### NOT re-noted (already placed earlier in the book; cross-referenced)
En no Gyōja / Ozunu & Shugendō (ch02), Kōbō Daishi & Shingon & Mount Kōya
(ch01/ch02), Fudō Myōō (ch05 — the Dainichi note cross-refs it), the Ikkō sect
& Ishiyama Hongan-ji (ch01/ch02), Mount Hiei & Mii-dera (ch01/ch05), the
matchlock & Tanegashima & Kunitomo (ch05), Negoro-ji & Kokawa-dera & Saiga &
Kakuban & Tsuda Kazunaga (ch05), the cauldron / Nanzen-ji Goemon legend
(ch02/ch03), kamari & tenton no jutsu (ch03), the Shinsho Taikōki (ch03), Shima
Sakon (ch04), the realm of the Asura (ch05), chagayu (ch05), Torii Moriichirō &
Torii Kihachirō & Ikenaga Kurō Chōa & Yasaka Kinbei & Shibatsuji Seiuemon &
Etegi (ch05), Hatsuko & Kazue & Goichi & Maki & Saeki Dennai (placed), Nagakute
& Kishiwada & Ōkusa (ch05), the koku/ri/shaku/sun/chō/tan/tsubo units and the
hour-names (ch01-04), the nenbutsu (ch01). Prefer cross-referencing these.
