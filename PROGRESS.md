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
