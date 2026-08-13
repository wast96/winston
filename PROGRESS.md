# PROGRESS — The Owl's Castle (梟の城, Shiba Ryōtarō)

Running per-batch log. Written as work happens, not at the end.

## Setup (survey session)

- **Source:** Internet Archive scan `fukuronoshiro0000ryot` (2024), Shinchō
  Bunko edition, ISBN 978-4-10-115201-1, ¥890. 674 PDF pages. Image-only; the
  Archive's embedded text layer OCR'd the vertical Japanese as **Latin script**
  and is pure garbage (unusable — confirmed on several pages). We OCR fresh.
- **Script/orientation:** vertical, right-to-left Japanese with **furigana**
  ruby throughout. OCR model **`jpn_vert`, `--psm 5`**. (setup.sh installs only
  the Chinese packs; `tesseract-ocr-jpn` + `tesseract-ocr-jpn-vert` installed
  manually this session — a setup.sh gap to fix for Japanese books.)
- **Page furniture:** running head 梟の城 and the folio are BOTH at the TOP of
  the page (folio alternates top-outer corner; folios are ARABIC numerals).
  Bottom margin is clean (no running foot). Measured body-text crop:
  **left 0.035, right 0.965, top 0.075, bottom 0.955** (fractions of page).
  This crop gives clean OCR with no furniture contamination.
- **PaddleOCR:** not installed (expected); dual-engine substitute is
  `ocr_dual.py` for batches.
- **Offset (READ folios; do not compute):** printed folio == PDF render page
  for folios **7–302** and again **425–660**, but drifts **+2 render pages**
  across folios ~**338–397** (an unnumbered leaf enters around folio 302–338;
  an apparent 1-leaf scan gap around folio 397–425 brings it back). Each
  opener's folio was read directly off the scan. The batch covering folios
  ~302–425 (B09–B13) must build its `data/pagemap/` by reading folios, and
  should check for a possibly missing leaf in the 397–425 span.

## Structure recovery

- The scan is **missing the first table-of-contents leaf** (the sections before
  伊賀ノ山). The full 19-section list was recovered from (a) the surviving second
  TOC leaf (PDF p3: 伊賀ノ山…伏見城 with exact folios) and (b) OCR of the body,
  cross-checked against the Japanese Wikipedia / Shinchōsha listing. Every
  opener's folio was verified on the page image.
- 19 titled novel sections (modelled as ch01–ch19, flat — the book has no
  numbered chapters or sub-sections), + the **解説 afterword** by Muramatsu
  Tsuyoshi (村松剛), folios 653–660, modelled as ch20.
- Novel body: folios **7–652**. First published Kōdansha, Sept 1959 (per the
  colophon line on folio 660). Naoki Prize (42nd, 1960).

## Tooling added this session (do not revert)

- `scripts/find_headings_vert.py` — vertical-text heading detector (the
  template's `find_headings.py` profiles ROWS for horizontal Chinese; this
  transposes to COLUMNS and filters furigana by glyph width). Catches
  fresh-page openers reliably; mid-page breaks needed OCR confirmation.
- `scripts/ocr_survey.py` — survey OCR runner: crop + `jpn_vert`, keeps
  paragraph blanks, and deliberately does NOT apply the Chinese
  `strip_folio`/`strip_runfoot` (see below).

## Flags for Batch 1 / the read-through

- **Batch-1 pipeline patches needed (Japanese):** `ocr_crop.py`'s `despace()`
  only strips spaces adjacent to Han (`一-鿿`), so kana keep OCR spaces; and its
  `strip_folio()` would DELETE a real short dialogue line ending in 。 (this
  book is dialogue-heavy). Use `jpn_vert --psm 5` with the crop above and adapt
  those two functions for kana before Batch 1. Furniture is top-only, so folio/
  runfoot strips are unnecessary if the crop is correct.
- **English section titles are PROVISIONAL** (drafted for the skeleton); settle
  them at the voice gate. Evocative ones to footnote: 水狗 (Water Dog), 修羅
  (Carnage), 五三ノ桐 (Paulownia Crest), 甲賀ノ摩利 (Mari of Kōga), 白い法印
  (the White Hōin).
- **解説 (ch20):** a third-party critical essay. Whether to translate it is the
  commissioner's call (raised in SURVEY.md); it is in the structure so it shows
  in the skeleton, and can be dropped if declined.
- **Title in English:** using "The Owl's Castle"; the film adaptations use
  "Owls' Castle". Confirm at the voice gate.
- **Cover:** the scan's cover is the copyrighted Shinchō woodcut; leaving
  `cover_image` empty so the builder generates a typographic cover.

## Checks run (survey)

- Skeleton EPUB built; `qa_epub.py` PASS (33 files, 26 documents, all links
  resolve); **epubcheck 5.1.0 clean** (0 fatals / 0 errors / 0 warnings).
- Checker regression tests green (setup.sh).

---

## Batch B01 — ch01 おとぎ峠 / Otogi Pass (PDF/printed 7-63, offset 0)

**Status: complete, awaiting the voice gate.** 57 pages, 521 source paragraphs,
~11.9k English words. The chapter opens on Otogi Pass in spring of Tenshō 19
(1591); Shimotsuge Jirōzaemon visits the hermit-ninja Tsuzura Jūzō, a long
flashback recovers the destruction of Iga in the Tenshō 9 rebellion and the
lives of the two disciples (Jūzō and Kazama Gohei), and the chapter closes on
the commission: kill Hideyoshi, paid for by the Sakai tea-merchant Imai Sōkyū.

### Pipeline / engineering
- **OCR:** rendered 7-63 at 300 dpi (PyMuPDF); `ocr_crop.py` with the measured
  crop (L 0.035 R 0.965 T 0.075 B 0.955), `jpn_vert --psm 5`, `--no-furniture-strip`.
  Second read via the Japanese-adapted `ocr_dual.py` (897 disagreement flags to
  prioritise crop-verification). `pgrep -c tesseract` == 0 after every run.
- **Script patches (do NOT revert):**
  - `ocr_crop.py`: kana added to the despace class; `--no-furniture-strip` skips
    the Chinese `strip_folio`/`strip_runfoot` (they delete short Japanese
    dialogue lines ending in 。 and only match Chinese 第X章).
  - `ocr_dual.py`: Japanese second read — crop the body box, run `jpn_vert psm5`
    on a grayscale and an Otsu-binarised variant (fail differently); `--lang/--psm`
    restore the Chinese behaviour.
  - `check_content.py`: skip `_`-prefixed / non-dict glossary sections (was
    crashing on `_about`); subsume a shorter glossary key covered by a longer
    matched key at the same span (kills the 山城-in-丸山城 collision class).
  - `qc_entities.py`: same longest-key-wins subsume fix.
- **Furigana leakage** is confined to the chapter-opener page (p0007); body
  pages OCR cleanly. Automated `assemble.py` welds paragraphs badly on vertical
  Japanese (OCR mangles the sentence-final punctuation `can_break()` relies on),
  so the translation was made by **reading the rendered page images directly**;
  `data/zh/ch01.txt` is a hand-corrected, paragraph-aligned transcription read
  off the scan (this IS the crop-verification record — no separate ocr_fixes
  replay, since the source text was transcribed, not machine-OCR'd then patched).
  Every proper name and number was verified against the page image / furigana.
- **Figures:** none. `find_figures.py` found nothing and every page was eyeballed
  for line art; ch01 is text-only. Empty figure list recorded as deliberate.

### Checks run (all green)
- `check_numbers.py --noise data/noise.txt`: **0 unresolved** (521 pairs). Added
  Japanese noise entries (names 五平/百地/千宗易/三河, idioms 四散/四囲/三脚/
  四半刻/十数/幾千億/百年松/零細, and 五、六十 / 八〇 / 一万二千 as
  carried-but-under-parsed forms) — all documented in `data/noise.txt`.
- `check_structure.py --pairs`: parity **521 | 521 OK**.
- `check_align.py`: 521/521, median ratio 9.50 en/han; 30 short-dialogue ratio
  outliers, all expected (one-line utterances), none a real drop.
- `check_content.py` (via `data/checks.json`): **all name occurrences in the
  paired paragraph** (286 occurrences); 0 displaced after the subsume fix.
- `qc_entities.py`: **0 misses** (census: 重蔵 x86, 伊賀 x67, 次郎左衛門 x58,
  五平 x31, 信長 x21 …). Re-anchored 6 pronoun-only paragraphs to name the
  character; 山城/丸山城 false positives removed by the subsume fix.
- `check_apparatus.py`: **0 failures / 0 warnings** (15 notes).
- Build: `qa_epub.py` **PASS** (34 files, 27 documents; 15 refs / 15 bodies /
  15 backlinks; 49 page-list entries). **epubcheck 5.1.0: 0/0/0/0.**
- Tail verified against the scan (p63): the closing beat 「秀吉を刺す」/「左様か」
  → "We are going to kill Hideyoshi." / "Is that so." reads faithfully.

### Footnotes (15) — reader model, at first appearance
Iga & Kōga (ninja provinces); Tenshō 19 = 1591; the shaku (and the units
policy); Otogi Pass / 御斎峠; tōyaku (Swertia japonica); the Iga Rebellion
(1579 failed, 1581 annihilation — with the note that Shiba's 12,000 is low vs
40-60k modern estimates); the chō; rappa; jizamurai; the Honnō-ji Incident &
Ieyasu's Iga crossing; the burning of Mount Hiei / Ikkō massacres; the Aekuni
Shrine ambush (traditional, not firmly documented); the koku; Sen no Rikyū
(with the anachronism note: Rikyū was ordered to die on the 28th of the 2nd
month of Tenshō 19, a month before the scene); the Hōkō-ji Great Buddha.

### NOT re-noted / carry-forward for later batches
- Recurring subjects placed here (do not re-note; cross-reference): Iga/Kōga,
  Tenshō dating, shaku/chō/koku/ri/ken measures, rappa/shinobi/ninja, jizamurai,
  Nobunaga, the Iga Rebellion, Honnō-ji, Hideyoshi, the Sakai tea-masters.
- The plot's paymaster (Imai Sōkyū) and the Great Buddha rendezvous are set up
  here; the meeting itself falls in a later chapter.

### Voice sheets (major cast — consult at every dialogue scene)
- **Tsuzura Jūzō (葛籠重蔵):** mid-30s, thick-shouldered, unusually tall for a
  ninja; terse, guarded, minimal in speech ("What have you come for?"). Since his
  family's murder he has lost the shinobi "apparition" and runs on a raw, human
  hunger for revenge; purposeless and monk-like at the pass, but the coiled force
  in him is felt by everyone. Uses わし / plain samurai forms; not uneducated.
- **Shimotsuge Jirōzaemon (下柘植次郎左衛門):** the disfigured old master; gruff,
  archaic, teasing, wry ("あはは"), commanding but secretly tender toward Jūzō.
  Nihilist creed: "be as earth, stone, wind; hold no human heart." Speaks with
  old dialectal/samurai endings (〜じゃ, 〜のう, 出い, 居申したわ), uses われ for
  "you". A creature of pure flux — "a face like a coelenterate sheathed in slime."
- **Kazama Gohei (風間五平):** beautiful, almost androgynous ("like a shrine-maiden
  girl"); cool, clever, detached, the clerkly killer. Philosophical, nihilist in
  a colder key than Jūzō — questions the whole ascetic ninja vocation and wants
  "the pleasures of the human world." Polite ます/です forms to his master, but
  distrustful ("The Master is a man full of guile").
- **Kuroami (黒阿弥 / 佐那具ノ黒阿弥):** Jūzō's aged genin, under five shaku, past
  fifty, a face "like a boy's"; near-silent, flatly loyal — answers everything
  with 「左様か」 ("Is that so").
- **Kisaru (木猿):** offstage so far; Jirōzaemon's fierce, unreadable daughter,
  Gohei's betrothed; vows to run Gohei through herself if he betrayed Iga.

### Register reference
On approval at the voice gate, `out/ch01_reading.md` becomes the FROZEN register
reference: run `check_register.py --ref out/ch01_reading.md` from B02 on.

### Voice-gate re-presentation (fresh container)
Branch hygiene: harness opened this session on a stray branch
(`claude/owls-castle-b01-nvvquy`) that was already identical to
`origin/claude/owls-castle` (both at `fdd978f`); fast-forwarded local
`claude/owls-castle` and deleted the stray (local + remote) per rule 2. No work
was stranded.

Rebuilt from a clean checkout and re-verified every gate (the container was
recycled, so `out/` had no build):
- Build: `qa_epub.py` **PASS** (34 files, 27 documents; 16 refs / 16 bodies /
  16 backlinks; 49 page-list entries). **epubcheck 5.1.0: 0/0/0/0.**
- `check_structure.py --pairs`: parity **521 | 521 OK**.
- `check_numbers.py --noise data/noise.txt` (bilingual): **0 unresolved** (521).
- `check_content.py`: **286 name occurrences, all in the paired paragraph**.
- `qc_entities.py`: **0 misses** (census 重蔵 x72, 伊賀 x64 …).
- `check_apparatus.py`: **0 failures / 0 warnings** (16 notes).
- `verify_unit.py ch01`: numbers 0 unresolved, **16 anchors ok**.
- Principal Characters page renders (5 flagged: Jūzō, Gohei, Jirōzaemon,
  Kisaru, Kuroami).
- **Tail re-verified against the scan** (rendered p63): 次郎左衛門が帰ってから →
  "After Jirōzaemon had gone, the mountain rain settled into a steady fall";
  菜種梅雨 → "the rape-blossom rains"; closing 「秀吉を刺す」/「左様か」 → "We are
  going to kill Hideyoshi." / "Is that so." Faithful.

Note count is **16** (the 15 logged above plus the sunset-gatha note added in the
voice-gate revisions).

Environment note (out of scope for this batch, pre-existing): the checker
regression suite has one FAIL, `hook stands down on template stub` in
`tests/run_tests.py` — the `kickoff_guard.py` placeholder stand-down for
*template-maintenance* sessions. It does not touch this book: our `HANDOFF.md`
carries a real B01 kickoff (first line `Owl's Castle B01`), not the template
placeholder, so the guard behaves correctly here. Left for a template-tooling
session; not fixed inside a translation batch to avoid disturbing the Stop hook.

---

## Batch B02 — ch02 濡れ大仏 / The Rain-Soaked Buddha (PDF/printed 64-89, offset 0)

**Status: complete.** 26 pages, 276 source paragraphs, ~5.3k English words, 6 new
footnotes. All checks green (details below). ch01 is the frozen register
reference; ch02 measured against it and within tolerance.

The chapter: Jūzō descends from Otogi Pass toward Nara, is ambushed at a spring
by Kisaru (now onstage) in an erotic, teasing scene, then takes an inn at
Aburazaka where the taciturn courtesan Kohagi turns out to be Imai Sōkyū's
guide-agent. At the Hour of the Ox he keeps the rendezvous at the foot of the
ruined, roofless Nara Great Buddha. In the Aizen-dō he meets the compromised
handlers (Matsukura Kurando and Kumobei); one of their men has been found
stabbed under the Buddha, the mission is already leaked, and Jūzō kills Matsukura,
conscripts the coward Kumobei, and rides for Sōkyū's mansion in Sakai at dawn.

### Two ch01 corrections bundled this batch (please note)
1. **Dropped ch01 tail restored.** ch01's last two paragraphs were missing: at
   the very top of folio 64 (before the ch02 title) Jūzō instructs Kuroami to
   keep a Kyoto shop under the cover name Iseya Kahei and wait for word, and the
   narrator adds that Kuroami "took it in as though it were idle talk of the
   world." ch01 stopped one beat early at 「左様か」/"Is that so." Both
   `data/zh/ch01.txt` and `out/ch01_reading.md` now carry the two paragraphs
   (ch01 parity is now 523 | 523). This is exactly the tail-drop failure rule 4
   warns about; found by reading folio 64 against the scan.
2. **ch01 Great Buddha note was wrong; corrected.** ch01 noted the rendezvous
   "Great Buddha" as Hideyoshi's Hōkō-ji in Kyoto. ch02 makes it unambiguous
   (Aburazaka, Kumoizaka, the Nigatsu-dō, Tamukeyama Hachiman, Tōdai-ji): the
   meeting is at the NARA Tōdai-ji Great Buddha, the colossal bronze Vairocana,
   roofless and rain-exposed since Matsunaga Hisahide burned its hall in 1567.
   The ch01 note now identifies the Nara Buddha correctly and cross-references
   ch02. Verified against scholarship (see fact-check below).

### Pipeline / engineering
- Rendered 64-89 at 300 dpi; `ocr_crop.py` with the batch-1 crop (L 0.035 R 0.965
  T 0.075 B 0.955), `jpn_vert --psm 5`, `--no-furniture-strip`; second read via
  `ocr_dual.py`. `pgrep -c tesseract` == 0 after every run. No scripts changed.
- Translated by reading the rendered page images directly; `data/zh/ch02.txt` is
  the hand-corrected, paragraph-aligned transcription (the parity surface and the
  crop-verification record). Force-added (data/zh is gitignored).
- **Crop-verified** off the page image / furigana: all proper names (松永弾正久秀,
  三好三人衆, 武田勝頼, 毘廬遮那仏, 多聞院, 松倉蔵人, 雲兵衛, 懸巣ノ次郎, 小萩,
  呂宋, 飛火野, 愛染明王), every number, and two content words the OCR mangled:
  p68 森 "the woods gave out" (OCR read 麻/林) and p70 立ツ髪 (the swept-up
  townsman hairstyle of Jūzō's disguise).
- **Figures:** none. `find_figures.py` found nothing and every page was eyeballed;
  ch02 is text-only. Empty figure list recorded as a deliberate decision.

### Checks run (all green)
- `verify_unit.py ch01 ch02`: ch01 numbers **0 unresolved** (523 pairs), **17
  anchors ok**; ch02 numbers **0 unresolved** (276 pairs), **6 anchors ok**.
- `check_structure.py --pairs`: parity **ch01 523 | 523**, **ch02 276 | 276**.
- `check_numbers.py` (via verify_unit): added noise entries for proper-noun
  numerals only (二月堂, 手向山八幡, 三好三人衆/三好/三人衆, 千手堂) — all are
  temple/shrine/coalition names, never real quantities; every real quantity
  (十五丁, 四、五間, 二十年, 十月十日, 永禄十年, 五十, 二十人, 五十人, 銀二枚,
  半年) is carried in the English.
- `check_align.py ch02`: median ratio 10.43 en/han; 18 short-dialogue ratio
  outliers (all high-ratio one-line utterances, none a low-ratio drop).
- `check_content.py`: **all name occurrences in the paired paragraph** (ch01 289,
  ch02 128); 0 displaced.
- `qc_entities.py`: **0 misses** both units. Named Jūzō once in 19 pronoun-only
  ch02 paragraphs (pronouns carry the rest, per STYLE); rendered the bare 「乱波」
  sneer as "Rappa." for glossary consistency.
- `check_apparatus.py`: **0 failures / 0 warnings** (ch01 17, ch02 6 notes).
- `check_register.py --ref out/ch01_reading.md`: **within tolerance**
  (contractions 9.4/1k = 0.60x ref, em-dash 8.7/1k, rhythm CV 0.74).
- Build: `qa_epub.py` **PASS** (20 documents, 817 paragraphs; 23 refs / 23 bodies
  / 23 backlinks; 49 page-list entries). **epubcheck 5.1.0: 0/0/0/0.**
- **Tail verified against the scan** (rendered p89): the closing Iga-neutrality
  aside (Iga men serving Takeda Katsuyori and Tokugawa Ieyasu at once, contact
  kept up in the Suruga mountains; warlords therefore withholding their weightiest
  secrets from Iga hands) renders faithfully; no invented text.

### Fact-check (real scholarship, not LLM sources)
- The 1567 burning of the Tōdai-ji Daibutsuden: corroborated. Matsunaga Hisahide
  fired the Great Buddha Hall on the tenth day of the tenth month of Eiroku 10
  (1567) during his war with the Miyoshi Sanninshū, who had fortified there; the
  Buddha's head fell and the bronze then sat exposed to the weather for over a
  century, rehoused only in 1709. Matches Shiba's exposition and the quoted
  多聞院 (Tamon-in) diary passage. (Wikipedia; Japanese Wiki Corpus; Tōdai-ji
  temple history; nippon.com.) The Iga-serving-both-sides anecdote (ch02 close)
  is presented by Shiba as "it is said" and is footnoted as the author's claim.

### Footnotes (6 new, at first appearance) + 1 added to ch01
New in ch02: the ruined Nara Great Buddha (anchored on "But there was no hall
over it."); Matsunaga Danjō Hisahide + the 1567 fire; the Tamon-in diary; Aizen
Myō-ō (the passion wisdom-king, apt to the scene); the bahan/wakō pirate ship +
Luzon and the coming Korea invasion; Takeda Katsuyori (framing the Iga anecdote
as the author's). Added to ch01 at its true first appearance: the zodiac
double-hours ("at the Hour of the Ox" = roughly 1 to 3 a.m.), a gap in ch01.

### NOT re-noted (already placed in ch01; cross-referenced, not repeated)
Iga/Kōga; rappa/shinobi/ninja; jizamurai/gōshi; Hideyoshi; Imai Sōkyū and the
Sakai tea-masters; the measures (shaku/chō/koku/ri/ken; 十五丁, 四、五間 carried);
Tenshō dating; Nobunaga; the Iga Rebellion; Honnō-ji; Tokugawa Ieyasu; Mino. The
rendezvous Great Buddha's ch01 note was corrected in place (see above) rather
than re-noted.

### Renderings — reused unchanged (consulted before romanizing)
Tsuzura Jūzō, Kazama Gohei (the 風 "Kaza" reference), Shimotsuge Jirōzaemon (ての
御 = her father), Kisaru, Kuroami, Imai Sōkyū, Oda Nobunaga, Toyotomi Hideyoshi,
Tokugawa Ieyasu, Shibata (house), Iga, Kōga, Sakai, Kasagi, the Kizu, Nara, the
Honnō-ji, rappa, Tenshō, Mino, ri/chō/ken/shaku/koku.

### Renderings — added this batch (glossary.json)
People: Matsunaga Hisahide (松永久秀/弾正久秀/久秀), Matsukura Kurando (松倉蔵人/
蔵人, provisional), Kumobei (雲兵衛, provisional), Kakesu-no-Jirō (懸巣ノ次郎,
provisional), Kohagi (小萩), Takeda Katsuyori, Iseya Kahei (伊勢屋嘉兵衛,
Kuroami's ch01 cover), the Miyoshi Triumvirate (三好三人衆). Places: Tōdai-ji,
Nigatsu-dō, Aburazaka, Tobuhino, Kai, Mikawa, Suruga, Luzon (呂宋), the Aizen-dō,
the Tamon-in. Terms: Aizen Myō-ō, Vairocana (毘廬遮那仏), bahan ship (ばはん船).

### Voice sheets — updates
- **Kisaru (木さる/木猿):** now onstage. Fierce, playful, physically fearless;
  teases and provokes Jūzō, springs on him half-naked, offers her body "one day"
  while insisting she hates Gohei yet goes to find him at her father's order.
  Speaks lightly, half-mocking (「ふふ」, 「え、この雨の中で?」). Still a virgin
  (Jūzō judges). A coiled equal to Jūzō, not a victim.
- **Kohagi (小萩):** the Nara courtesan / Sōkyū's guide-agent. Two registers: a
  slow, heavy, near-mute plainness as the bought woman, and a quick, clipped,
  amused sharpness once she drops the mask ("What amuses me is myself"). Polite
  ます/でございます throughout; a possible Kōga operative who may kill Jūzō "some
  day." He does not kill her, and half regrets it.
- **Matsukura Kurando (松倉蔵人):** scarred ex-bandit past fifty, puffed-up and
  loose-tongued; gruff samurai bluster (じゃ、ぞ) over a coward's nerve. Killed
  mid-sentence.
- **Kumobei (雲兵衛):** young, sturdy, "a wandering balladeer's good-natured
  face"; ex-wakō sailor, self-described coward. Cringing, deferential
  (ござる、畏れ入る). Conscripted; the surviving thread into the capital.

### Engineering note for future batches (glossary via apparatus_merge)
`apparatus_merge.py` treats `glossary.json` as a FLAT `{zh: row}` map and writes
new rows at the ROOT of the file, but this project's glossary is SECTIONED
(people/places/terms). The 21 rows this batch were merged, then moved into their
sections with a one-off script (bytes preserved, no CJK retyped) and verified
(no stray root keys; check_content/qc_entities clean). Future batches: after
`apparatus_merge`, move glossary rows into people/places/terms, or add them to a
section directly. Notes and figures merge correctly as-is.

### Environment
- setup.sh installed the Chinese packs only; `tesseract-ocr-jpn` +
  `tesseract-ocr-jpn-vert` installed manually (the known setup.sh gap). epubcheck
  re-fetched to /tmp/epubcheck-5.1.0. The pre-existing checker-regression FAIL
  (`hook stands down on template stub`) persists and is unrelated to this book
  (our HANDOFF carries a real kickoff, so the Stop hook behaves correctly).

## Batch B03 — ch03 白い法印 / The White Hōin (PDF/printed 90-123, offset 0)

**Status: complete.** 34 pages, 385 source paragraphs, ~6.3k English words, 16
new footnotes. All checks green (details below). ch01 is the frozen register
reference; ch03 measured against it and within tolerance (contr 19.4/1k = 1.23x,
em-dash 15.7/1k, rhythm CV 0.81).

The chapter: Jūzō crosses Tobuhino at dawn (still turning over the courtesan
Kohagi, whom he spared) and rides on to Sakai. In the pleasure quarter he lets a
Sakai loafer, Sōgorō, lead him to a house, where Kohagi reappears in disguise as
a hostess — a second, deliberate contact. That night Jūzō breaks into Imai
Sōkyū's mansion. The long central set-piece is Sōkyū's biography (his rise as
the arms-merchant who bankrolled Nobunaga's and then Hideyoshi's guns, from the
Matsushima-caddy audience of 1568 to his eclipse by the Konishi under Hideyoshi)
and the tea-room confrontation in which the reason for the commission is drawn
out: Hideyoshi's planned invasion of Korea will strangle Sōkyū's China trade, so
the merchant wants him dead. Sōkyū appoints Kohagi — revealed as his adopted
daughter, born a princess of a fallen house — as Jūzō's contact and paymaster.
Jūzō leaves for the capital, aching for Kohagi against his own creed.

### Tail verified against the scan (rule 4)
The chapter's final sentence runs OFF folio 123 and completes on the first line
of folio 124 (「…小萩の肉体への思慕がうずいているのを覚えた。」), just above the
ch04 title. Folio 124 was rendered and read to recover the true continuation; the
final paragraph is faithful to it (no invented bridging text).

### Checks run (all green)
- **Parity:** 385 | 385 (`check_structure --pairs`, `verify_unit`).
- **Numbers:** `check_numbers` 0 unresolved over 385 pairs (with `data/noise.txt`).
  New noise entries (proper-noun numerals / idioms, all with the English form they
  carry): 惣五郎 Sōgorō (5), 千利休 Sen no Rikyū (1000), 九州 Kyūshū (9), 三宅
  Miyake (3), 巨万 "colossal" (万), 五体 "frame" (5), 四肢 "limbs" (4). Two real
  koku amounts (千二百 = 1,200; 二千二百 = 2,200) noised because the parser composes
  千+百 on the source side but not the English "one/two thousand two hundred"; the
  English carries the full value (same limitation the 一万二千 entry documents).
- **Entities:** `qc_entities` 0 misses (census 重蔵×90, 秀吉×22, 信長×21, 小萩×18,
  法印×13, 惣五郎×10, …). `check_content` OK across all units (220 ch03 name
  occurrences, all in the paired paragraph).
- **Alignment:** `check_align` median ratio 9.65; the outliers flagged are all
  short dialogue lines (max source line 27 chars) — benign ratio inflation, no
  displaced content.
- **Apparatus:** `check_apparatus` 0 failures / 0 warnings; 16 note anchors all
  resolve. `build_reading_epub` PASS; `qa_epub` PASS (39 refs / 39 bodies / 39
  backlinks, 49 pagebreaks); **epubcheck 0 fatals / 0 errors / 0 warnings**.

### Footnotes — NOT re-noted (already placed in ch01–ch02; cross-referenced)
Iga/Kōga, rappa/shinobi, jizamurai/gōshi, Tenshō/Eiroku dating, the zodiac
double-hours, koku/kin(new)/chō/ri/ken/shaku, the Iga Rebellion, Honnō-ji, Mount
Hiei, Hideyoshi, Nobunaga, Ieyasu, the Sakai tea-masters/Rikyū, Tsuda Sōgyū, the
ruined Nara Great Buddha (Tōdai-ji, burned by Matsunaga 1567), Aizen Myō-ō, the
bahan/wakō ships and Luzon. Imai Sōkyū already appears in ch01–ch02; ch03 adds one
crisp identity note at his first ch03 mention (dates, the three-tea-masters
grouping) rather than re-noting the general tea-master row.

### Footnotes — new this batch (16, ch03's own first-appearances)
The fox / fourth-hour joke; Sakai as a self-governing merchant free-city (moats
filled 1583); Imai Sōkyū (identity/dates); **法印 Hōin / 法眼 Hōgen / 大蔵卿**
(the chapter-title rank, granted to laymen); **関白 Kampaku**; Takeno Jōō; the
Matsushima caddy and the meibutsu tea-utensil cult; Nobunaga's 1568 Kyoto entry /
Ashikaga Yoshiaki; Tenka Fubu; the *kin* (catty); the Hōkō-ji Great Buddha
(Hideyoshi's, distinct from the Nara one); Sekigahara (forward reference, fixes
the "now" at 1591); the Kita-no-mandokoro; Hideyoshi's Korea invasion (the plot's
engine); Tsurumatsu's death / Hidetsugu; Nanban iron.

### Minor source point left unfootnoted (the low-stakes tier)
Folio 105 credits Nobunaga in 1568 with having "just pacified this Suruga and
Mino"; in fact his base provinces were Owari and Mino, not Suruga. Rendered as
printed (fidelity), and the discrepancy is named inside the Yoshiaki/1568 note
rather than given its own note.

### Renderings — reused unchanged (consulted before romanizing)
Tsuzura Jūzō / 重蔵 Jūzō, Shimotsuge Jirōzaemon, Kohagi, Imai Sōkyū, Oda
Nobunaga / 信長, Toyotomi Hideyoshi / 秀吉, Tokugawa Ieyasu / 家康, Sen no Sōeki
(= Rikyū), Tsuda Sōgyū, Matsukura Kurando, Iga, Kōga, Sakai, Nara, the Honnō-ji,
Tōdai-ji, Tobuhino, Kai, Mikawa, Suruga, Mino, Ōmi, Yamato, Yamashiro, Luzon,
rappa, Tenshō, Eiroku, koku/chō/ri/ken/shaku.

### Renderings — added this batch (glossary.json; 44 rows)
People (17): Imai Sōkun (今井宗薫) / Sōkun (宗薫), Sōgorō (惣五郎), Aida Gen'emon
(会田源右衛門, Jūzō's alias), Takeno Jōō (武野紹鴎), Naya Sōji (納屋宗次), Imai
Nobutsune (今井信経), Dewa-no-kami Muneyoshi (出羽守宗慶), Ashikaga Yoshiaki
(足利義昭), Tōkichirō (藤吉郎), Azai Nagamasa (浅井長政), Konishi Ryūsa (小西隆佐),
Konishi Yukinaga (小西行長) / Yukinaga (行長), Tsurumatsu (鶴松), Hidetsugu (秀次),
Sen no Rikyū (千利休, = 千宗易). Places (17): Ōsaka, Akutagawa, Ibaraki, Odani
Castle, Yamazaki, the Daitoku-ji, Sekigahara, Shiwaku, Shōdoshima, Kyūshū,
Kawachi, Echigo, Izumi, Abiko, the Jōraku-ji, the Myōkoku-ji, Byakugō-ji. Terms
(10): Hōin (法印), Hōgen (法眼), Ōkurakyō (大蔵卿), the Kampaku (関白), the
Matsushima (松島肩衝), Tenka Fubu (天下布武), Nanban (南蛮), kin (斤),
Settsu-no-kami (摂津守), the Kita-no-mandokoro (北政所). All merged via
`apparatus_merge.py`, then moved from the file root into people/places/terms
with a one-off byte-preserving script (no stray root keys; content/entity clean).

### Voice sheets — updates
- **Imai Sōkyū (今井宗久):** the White Hōin. A frail, tiny old man with a large,
  childlike face; heavy-lidded, near-motionless, urbane. Cold irony under perfect
  composure; a war-profiteer's pride (he believes he MADE Nobunaga and Hideyoshi
  — his "one patch of darkness") and a merchant's hatred of the low-born Kampaku
  who displaced him. Speaks in a cultivated, faintly archaic register (じゃ,
  くるる, 拝し奉る); a single 小心 (timid) streak shows when Jūzō names the plot.
- **Kohagi (小萩):** deepened. Revealed as Sōkyū's adopted daughter, born a
  princess of a fallen noble house, now his agent and Jūzō's appointed contact.
  Cool, unbreakable poise; a smoky half-smile that never gives way; needles Jūzō
  and sees straight through him. Offers herself as "a courtesan"; Jūzō is drawn
  and angry at himself for it.
- **Sōgorō (惣五郎):** the Sakai loafer. Coarse, cocky townsman-swagger; treats a
  country samurai as beneath a day-laborer, brags of the merchants' court ranks,
  a weak head for drink. A one-scene comic guide.

### No figures
`find_figures.py 90 123` returned nothing; every page eyeballed for line art —
ch03 is text-only (as ch01–ch02). Recorded as a deliberate empty figure list.

## Batch B04 — ch04 木さると五平 / Kisaru and Gohei (PDF/printed 124-148, offset 0)

**Status: complete.** 25 pages, 286 source paragraphs, ~4.6k English words, 5 new
footnotes. All checks green (details below). ch01 is the frozen register
reference; ch04 measured against it and within tolerance (contr 24.0/1k = 1.52x,
em-dash 21.5/1k, rhythm CV 0.68). The high contraction/dash counts are the
chapter's nature: it is almost all dialogue, much of it interrupted (source ——),
rendered faithfully.

The chapter shifts to Kyoto and the OTHER pair. Kisaru, on the Shijō riverbank,
works a ninja crowd-illusion (めくらまし) — she hypnotises a whole crowd into a
phantom summer squall under a clear sky. Gohei has been shadowing her; he follows
her to her lodging in the half-ruined Chinnō-in, where the eccentric monk-abbot
Iten Gyōzan (who buries himself in the bamboo grove "to become the bamboo") reads
Gohei at once as a rappa with an evil face. In her room Kisaru interrogates Gohei
in her father's name; he confesses he has deserted Iga, taken the alias Gero
Shōbei Yasuji, and now serves Maeda Gen'i, the magistrate of Kyoto, at 200 koku,
hunting the provinces' spies in the capital. He forces himself on her (a flat,
un-purpled rape scene), makes her his creature, and extracts that Jūzō is in the
capital — the lead that could raise him to 1000 koku. Kisaru, wiping Jūzō's face
from her mind, parts from Iga. The chapter closes on Gohei leaving and a
muffled-footed woman passing Gyōzan on the path: "It was not Kisaru. ……"

### Tail verified against the scan (rule 4)
ch04's final sentence runs OFF folio 148 ("赤い口を開けて、") and completes on the
FIRST lines of folio 149 (the Gohei/Gyōzan alms exchange, then "五平が立ち去った
あと…それは木さるではなかった。……"), just above the ch05 title 羅刹谷. Folio 149 was
rendered and read to recover the true continuation; paragraphs 280-286 are faithful
to it (no invented bridging text). B05 must NOT re-include folio 149's ch04 portion
(everything before the 羅刹谷 title); ch05's body begins "東山の南に、泉山という…".
Likewise the ch03-tail line at the very top of folio 124 (体への思慕が…) is ch03's,
already placed, and is NOT part of ch04.

### Pipeline / engineering
- Rendered 124-148 (+149 for the tail) at 300 dpi; `ocr_crop.py` with the batch-1
  crop (L 0.035 R 0.965 T 0.075 B 0.955), `jpn_vert --psm 5`, `--no-furniture-strip`;
  second read via `ocr_dual.py`. `pgrep -c tesseract` == 0 after every run. No
  scripts changed.
- Translated by reading the rendered page images directly; `data/zh/ch04.txt` is
  the hand-corrected, paragraph-aligned transcription (the parity surface and the
  crop-verification record). Force-added (data/zh is gitignored).
- **Crop-verified** off the page image / furigana: the alias 下呂正兵衛康次 (OCR
  read 康光; the 冫+欠 radical of 次 is unmistakable at 6x — Gero Shōbei **Yasuji**,
  not Yasumitsu); 蔵縄手ノ鹿次 (furigana くらなわて/ししじ → Kuranawate-no-Shishiji);
  and all proper names/numbers (如意ヶ岳, 青蓮院, 鴨川, 四条大橋, 祇園, 建仁寺, 松原通,
  六波羅, 清水, 珍皇院, 以天仰山, 竹ノ上人, 前田玄以, 加藤肥後守, 三条, 二百石, 千石).
  OCR "人竹" was spurious — the monk is 竹ノ上人 (the Bamboo Saint) and elsewhere
  bare 竹; folio 124 「艮（うしとら）」 (northeast) was OCR'd as 上/良.
- **Figures:** none. `find_figures.py 124 148` returned nothing and every page was
  eyeballed for line art; ch04 is text-only (as ch01-ch03). Empty figure list
  recorded as a deliberate decision.

### Checks run (all green)
- **Parity:** 286 | 286 (`check_structure --pairs`, `verify_unit`).
- **Numbers:** `check_numbers` 0 unresolved over 286 pairs (with `data/noise.txt`).
  New noise entries — Kyoto place-names whose numeral is the name, not a count:
  四条 (Shijō), 三条 (Sanjō), 六波羅 (Rokuhara). Every real quantity is carried in
  the English (二十年 twenty years, 五、六歩 five or six steps, 二百石 two hundred
  koku, 千石 a thousand koku, 二つ三つ two or three, 八月 eighth month, 半月 half a
  month, 一間 a single ken). Reworded one line so the parser reads the carried
  1000 ("a thousand-koku place", not a bare "that thousand-koku").
- **Entities:** `qc_entities` 0 misses (census 五平×73, 伊賀×15, 仰山×14, 重蔵×8, …).
  Named Gohei in 8 pronoun-only 五平 paragraphs (STYLE: name once per paragraph the
  character appears in; pronouns carry the rest). `check_content` OK across all
  units (ch04 114 name occurrences, all in the paired paragraph).
- **Alignment:** `check_align` median ratio 10.50; 23 outliers, all short dialogue
  lines (benign high-ratio inflation; no low-ratio drop). Exit 0.
- **Apparatus:** `check_apparatus` 0 failures / 0 warnings; 5 note anchors all
  resolve (`verify_unit`: 5 anchors ok). `build_reading_epub` PASS; `qa_epub`
  PASS (44 refs / 44 bodies / 44 backlinks, 49 pagebreaks); **epubcheck 0/0/0/0**.
- **Register:** `check_register --ref out/ch01_reading.md` — within tolerance.

### Regression caught and fixed in-batch
Adding 木さる → Kisaru as a glossary key retroactively broke ch02's check_content
(ch02 introduced Kisaru as 木さる with pronoun-carried paragraphs, and passed only
because 木さる was NOT a glossary key). Removed the 木さる row; the 木猿 entry already
notes the ch04 spelling. 木さる is therefore uncensused, exactly as in ch02.

### Footnotes — NOT re-noted (already placed in ch01-ch03; cross-referenced)
Iga/Kōga, rappa/shinobi, jizamurai/gōshi, Tenshō dating (the "1591" fixed here by
this spring / eighth month), the measures (koku/ken/shaku/chō/ri — 二百石/千石/一間
carried), the Iga Rebellion, Nobunaga, Hideyoshi, Ieyasu, Honnō-ji, Tōdai-ji (the
ch02 plot the narration ties Gohei back to), Matsukura Kurando, Sōkyū/the Sakai
tea-masters. The zodiac double-hours, Aizen Myō-ō, etc. do not recur here.

### Footnotes — new this batch (5, ch04's own first-appearances)
放下僧 juggler-priests (itinerant entertainer-monks); 如意ヶ岳 Nyoigatake (Higashiyama
peak, later the Daimonji bonfire slope); the 祇園 Gion aside (not yet a teahouse
quarter in 1591); 加藤肥後守 = Katō Kiyomasa (why an Iga man in his service was
killed); 前田玄以 Maeda Gen'i (Hideyoshi's magistrate of Kyoto and his web of
informers — the office Gohei has entered). Kyoto street/temple geography and the
novel's own props (Chinnō-in, the Bamboo Saint/Gyōzan, the めくらまし illusion) get
glossary rows, not footnotes, per STYLE (don't footnote the fiction's own furniture).

### Minor points left unfootnoted (the low-stakes tier)
The 珍皇院 Chinnō-in and 竹ノ上人 Bamboo Saint are the story's own inventions (evoking
the real Rokudō-Chinnō-ji); the 土佐旧一条家 (Tosa Ichijō) surname Gohei borrows is a
passing colour detail. All are glossary rows only. The temple is called both a
Shingon foundation and its monk a 禅僧 (Zen monk) — Shiba's own slight inconsistency,
rendered as printed.

### Renderings — reused unchanged (consulted before romanizing)
Tsuzura Jūzō / 重蔵 Jūzō, Kazama Gohei / 五平 Gohei, Shimotsuge Jirōzaemon /
次郎左衛門, Kisaru (木さる = 木猿), Matsukura Kurando, Tōdai-ji, Iga, rappa,
Tenshō, koku/ken/shaku.

### Renderings — added this batch (glossary.json; 21 rows)
People (8): Maeda Gen'i (前田玄以) / Gen'i (玄以) / Maeda (前田), Katō Higo-no-kami
(加藤肥後守), Iten Gyōzan (以天仰山) / Gyōzan (仰山), Kuranawate-no-Shishiji
(蔵縄手ノ鹿次, provisional), Gero Shōbei Yasuji (下呂正兵衛康次, Gohei's alias).
Places (12): Shijō (四条), Sanjō (三条), the Kamo river (鴨川), Higashiyama (東山),
Nyoigatake (如意ヶ岳), the Shōren-in (青蓮院), Gion (祇園), Kennin-ji (建仁寺),
Matsubara road (松原通), Rokuhara (六波羅), Kiyomizu (清水), the Chinnō-in (珍皇院,
provisional), Tosa (土佐). Terms (1): the Bamboo Saint (竹ノ上人). All added directly
into people/places/terms sections (no apparatus_merge glossary flatten this batch —
notes-only merge). Removed one stray row (木さる) after the ch02 regression above.

### Voice sheets — updates
- **Kazama Gohei (五平):** now a lead. Cold, clerkly, cruel; a beautiful face with
  "a mean little shadow at the corner of the mouth" when he smiles. To Kisaru he
  uses superior/intimate わし・じゃ (not the polite ます・です he gave his master in
  ch01). Has deserted Iga for ambition, serves Maeda Gen'i as a spy-catcher under
  the alias Gero Shōbei Yasuji, and rapes and recruits his own betrothed without
  warmth — "a hollow look," "a barefaced emptiness." Means to use her against Jūzō.
- **Kisaru (木さる):** the crowd-illusion virtuoso (playful, imperious, cheeky as
  she browbeats the mob), then the fierce ninja-daughter interrogator ("In my
  father's stead I will ask you"), then broken open: her body betrays "the child in
  her," Jūzō's face rises unbidden as she is taken, and by the act's end she has
  "parted from Iga for good." Ends half-believing she loves Gohei, tempted by the
  thousand-koku wife she might become — and still secretly holding Jūzō.
- **Iten Gyōzan (仰山), new:** the monk-abbot of the ruined Chinnō-in; old, riddling,
  self-mocking, unkillable in argument. Buries himself in the bamboo "to become the
  bamboo"; reads Gohei's face as a rappa's on sight. Craggy, wry じゃ/わい/おる
  register — a one-chapter chorus figure who names the theme (the shadow arts turned
  to selfish gain leave an "evil cast" on the face).

## Batch B05 — ch05 羅刹谷 / Rakshasa Valley (PDF/printed 149-166, offset 0)

Jūzō and Kuroami cross the Ukiyo-bashi into Rakshasa Valley, south of Higashiyama,
to a ruined Yakushi hall where Kuroami has mustered some twenty masterless rappa
(Iga, Kōga, one from Harima). Jūzō is installed as their unseen chief; their charge
is not robbery but to "curse the world" — set anti-Toyotomi rumour flying over the
Korea-war levy. A long essayistic middle (Shiba's own historical digression) turns
on Hideyoshi's gold: the mines of Sado and Ikuno, the 金賦 largesse of Tenshō 13/17,
the Jurakudai hoard, and Jūzō's reading of Sōkyū's design — Sakai's wealth behind
Ieyasu, Hattori Hanzō the broker, the Iga gōshi to rise again. Closes with Jūzō and
Kuroami on the cliff: Kohagi is a suspected Kōga infiltrator (Kuroami will kill her
on sight, Jūzō consents); if Gohei has deserted, Jūzō must be the one to cut him
down. 152 source paragraphs; 6 new notes (book total 50).

### Tail verified against the scan (rule 4)
ch05's final paragraph (folio 166) reads off the scan as: 重蔵と黒阿弥は…崖の上で
別れた。黒阿弥は…数丈下の暗い地面へ…跳んだ。重蔵はそのまま更に崖を攀じ、稜線を
南へ伝って泉涌寺参道の松並木へ出た。まだ、夜が明けるのにだいぶ間がある。夜の京の
地図を体に入れるために、天明まで町を歩いてみるつもりだった。 Rendered faithfully as
the closing paragraph. Folio 167 was rendered and confirmed to be entirely the ch06
opener (忍び文字, Gohei and the kunoichi); ch05 does NOT spill onto it. The top of
folio 149 is ch04's tail (the Gohei/Gyōzan exchange), already placed in B04 and not
re-translated here — ch05's body begins after the 羅刹谷 title with 東山の南に、泉山…

### Crop-verified this batch (names / numbers / low-confidence spans)
- Numbers: 二百五十五万石 (Ieyasu's Kantō, 2,550,000 koku), the gold figures 金子五千枚 /
  銀子三万枚 / 二万六千枚 / 三十万五千両 (folio 160), 禄高八千石 (Hanzō), 百十軒 / 十八人
  (the Ōmi levy), 四十万 / 千万石. All confirmed against magnified crops.
- Names: 服部半蔵 / 石見守 / 江戸麹町半蔵門 (folio 162), 聚楽第 / 別墅 (folio 160),
  堺の富力 (NOT 合力; folio 161), 夏見ノ耳次 (folio 154, no furigana on 耳次 — reading a
  project call, provisional). 翕然と従った (folio 159): the OCR "きい、きゅう然" is the
  complex 翕 mis-split; rendered "fell in behind him… to a man" (robust to the reading).

### Checks run (all green)
- verify_unit ch05: numbers 0 unresolved (152 pairs), anchors 0.
- check_structure --pairs: parity 152 | 152 OK.
- check_align ch05: median 9.79 en/han; the flagged pairs are all short dialogue/
  one-clause lines (expected ratio noise), no real drops.
- qc_entities: 0 misses (census: 重蔵 x37, 黒阿弥 x34, 秀吉 x23…).
- check_content --config data/checks.json: ch05 129 occurrences all in the paired
  paragraph; content alignment OK across all five units.
- check_register --ref out/ch01_reading.md: 16.7 contr/1k (1.06x ref) after a pass of
  natural contractions through Jūzō/Kuroami dialogue; within tolerance (was 5.4/0.34x
  STILTED on first draft — Kuroami's ござる register kept its weight on a few grave
  lines and his self-naming).
- check_apparatus: 0 failures, 0 warnings (50 notes book-wide).
- build_reading_epub: 5 of 20 chapters, 50 notes, 49 pagebreaks.
- qa_epub: PASS (34 files, 27 documents, all links resolve).
- epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings / 0 infos.

### noise.txt additions (data/noise.txt, ch05 block)
Two false-positive classes and one parser-limitation class:
- 百姓 (peasantry) and 何百年 ("hundreds of years"): the 百 is not the count 100.
- 二百五十五万 / 三十万五千 / 二万六千 / 百十: real quantities carried in the English, but
  the check_numbers English-word parser cannot compose "two million…thousand",
  "three hundred and five thousand", "twenty-six thousand", or "hundred and ten".
  Noised on the SOURCE side per the B03 二千二百/千二百 precedent (safe: noise only
  removes source numerals, never masks a drop; each value verified present in the EN).

### Footnotes — NOT re-noted (already placed in ch01-ch04; cross-referenced)
Iga/Kōga, Tenshō dating (Tenshō 9/10/13/17), the Iga Rebellion, Honnō-ji, Hideyoshi/
Nobunaga/Ieyasu, Imai Sōkyū, the Hōin rank, Sakai the free-city, Tenka Fubu,
Sekigahara (here foreshadowed "nine years off"), the Korea invasion (唐入り/朝鮮出兵 —
the ch03 "his design to attack Korea" note covers it), Hideyoshi's heirless-ness
(秀吉に子がない — the ch03 Tsurumatsu note), the Hōkō-ji Great Buddha (京の大仏 / 方広寺),
the zodiac double-hours (子ノ刻, 暮四ツ, 二刻), the measures (尺/丁/石/両), rappa/shinobi,
jizamurai/gōshi, and the B04 first-appearances. The Battle of Yamazaki (1582) and
Akechi Mitsuhide's usurpation-comparison are historical context the reader already has
from the ch01 Honnō-ji note and are left un-noted.

### Footnotes — new this batch (6, ch05's own first-appearances)
1. 羅刹 rakshasa — the flesh-eating demon and the valley legend (anchor "this is
   Rakshasa Valley").
2. Sennyū-ji — the imperial mortuary temple since Emperor Shijō; the crossing "out of
   the world of the living" (anchor "the burial ground of one sovereign after another").
3. Hattori Hanzō — the historical Iga ninja who served Ieyasu and brokered the
   Tokugawa–Iga tie (anchor "brought by Hattori Hanzō").
4. the gold largesse — Hideyoshi's 金賦 of 1585 and 1589; the figures assessed as "of
   the order reported by contemporaries" (anchor "the gold largesse").
5. the Jurakudai — Hideyoshi's palace (ch07's title, 聚楽) (anchor "the Jurakudai").
6. the kōshin monkey — the kōshin vigil and the see/hear/speak-no-evil monkeys (anchor
   "a carved kōshin monkey").

### Minor points left unfootnoted (the low-stakes tier)
The swordsmith 国広 Kunihiro (a glossary row; a fine-blade prop, "a Kunihiro" like "a
Stradivarius"), 音無川 (name means "the soundless river", left plain), 浮世橋 (its sense
carried by the surrounding lines), 丈 jō and 畳 (tatami) as loose height/area units
(kept without a note; shaku/ken are already glossed), 五畿内/中国 as region labels.

### No figures
find_figures 149-166 returned nothing; every page eyeballed for line art. ch05 is
text-only, like ch01-ch04. Empty figure list is a deliberate decision (figures.json
stays {} — no chapter in this book has carried a figure).

### Renderings — reused unchanged (consulted before romanizing)
Tsuzura Jūzō / 重蔵 Jūzō, 黒阿弥 Kuroami, 今井宗久 Imai Sōkyū, 小萩 Kohagi, Kisaru
(木さる = 木猿), 下柘植次郎左衛門 Shimotsuge Jirōzaemon, 風間五平 Gohei, 伊勢屋嘉兵衛
Iseya Kahei, Hideyoshi, Ieyasu, Nobunaga, 明智光秀 (Mitsuhide), 柴田勝家 (Katsuie),
Iga/Kōga, Sakai, Ōsaka, rappa, Tenshō, koku/shaku/chō/ri, the Chinnō-in, Higashiyama.

### Renderings — added this batch (glossary.json; 23 rows)
People (5): Hattori Hanzō (服部半蔵), Iwami-no-kami (石見守), Mitsuhide (光秀, bare
surname-reading), Katsuie (勝家, bare given name), Natsumi-no-Mimiji (夏見ノ耳次,
provisional). Places (16): Rakshasa Valley (羅刹谷), Senzan (泉山, provisional),
Sennyū-ji (泉涌寺), the Otonashi-gawa (音無川), the Ukiyo-bashi (浮世橋), Shimogyō
(下京), the Hōkō-ji (方広寺), Sado (佐渡), Ikuno (生野), the Jurakudai (聚楽第), Edo
(江戸), the Kantō (関東), Korea (朝鮮), the Ming (大明), Shikoku (四国), the Chūgoku
provinces (中国), Kishū (紀州), the Five Home Provinces (五畿内). Terms (3): rakshasa
(羅刹), Kunihiro (国広), kōshin (庚申). Added directly into the sectioned
people/places/terms with the Edit tool (notes-only apparatus_merge, no flatten). A
bare 宗久→Sōkyū row was tried and REMOVED: its "Sōkyū" substring collided with "Imai
Sōkyū" across ch03's paragraph alignment and retroactively tripped check_content on a
pronoun-carried ch03 paragraph that had shipped clean. Bare 宗久 stays consistent in
prose but is not a checked anchor (same as before this batch).

### Voice sheets — updates
- **Tsuzura Jūzō:** back onstage as the reflective strategist. Terse, guarded, blunt
  (わし); reads the age like a merchant reading a ledger, "not a breath of moisture" in
  the rappa's eye. Won't kill Kohagi himself (has lain with her once) but consents to
  Kuroami doing it; the revenge-hunger of ch01 now hardens into a will to "throw
  himself, body and life, into this work" for Iga's sake.
- **Kuroami:** a LEAD this chapter. Aged (past fifty), the shinobi art made flesh;
  humble-archaic ござる/ござろう servant register to Jūzō, whom he has known "since
  swaddling-clothes" and chides like a father. Cold, practical, superstitious in his
  creed (no women inside a ninja's 結界); can "snuff out his own presence" mid-sentence.
  Runs the muster as "Iseya Kahei" the whetter; installs the unseen Jūzō as chief.

## Batch B06 — ch06 忍び文字 / The Ninja Cipher (PDF/printed 167-206, offset 0)

Gohei's thread. The chapter turns on the shinobi cipher and introduces the fictional
Kashima swordsman Watanabe Satoru, whom Kohagi bankrolls and pits against Jūzō as a
test; Jūzō spares him without drawing his blade. 312 source paragraphs, 5 new notes
(book total 55).

### Pipeline
render 167-207 --dpi 300; ocr_crop 167-206 (--left 0.035 --right 0.965 --top 0.075
--bottom 0.955 --lang jpn_vert --psm 5 --no-furniture-strip); ocr_dual 167-206;
`pgrep -c tesseract` 0 after each. assemble.py NOT used (welds paragraphs on this
vertical OCR, as before). data/zh/ch06.txt hand-transcribed off the rendered page
images (the parity + crop-verification surface); force-added (data/zh gitignored).
Setup gap unchanged: setup.sh installs only the Chinese packs; jpn + jpn_vert added
manually. epubcheck re-fetched to /tmp/epubcheck-5.1.0 (container was recycled).

### Checks (all green)
- **Numbers:** verify_unit ch06 — 0/312 unresolved. noise.txt gained a ch06 block:
  二条 (Nijō place-name, the 二 not a count; covers 二条河原), 三方 (sanbō offering-stand,
  三 not a count), 源九郎 (Kurō, the 九 a name), 五官 (the five senses, idiom). The
  hyphenated "two-hundred-koku" would not parse — rendered "a warrior of two hundred
  koku". くノ一 did NOT flag (its 一 is handled by the built-ins).
- **Parity:** check_structure 312 | 312 OK. One early off-by-one fixed: source folds
  "それには女は答えず、" with Kohagi's message into one paragraph; the draft had split it.
- **Entities:** qc_entities 0 misses (census: 重蔵 x78, 小萩 x52, 五平 x29, 乱波 x22).
  Many fixes: 重蔵さま/様 was first drafted "Lord Tsuzura" (surname) — changed to "Lord
  Jūzō"/"Master Jūzō" so the 重蔵→Jūzō anchor lands; pronoun-carried 五平/小萩/二条/乱波
  paragraphs re-anchored with the name/term.
- **Content:** check_content OK across all units (ch06 216 name occurrences placed).
  No regression from the new rows (大坂城 already "Ōsaka Castle" in ch03).
- **Alignment:** check_align — 20 pairs out of the median band, all short dialogue,
  the parenthetical thoughts, and the cipher block (English shorter than the glyphs);
  no low-ratio drop on a substantial paragraph.
- **Register:** check_register --ref out/ch01_reading.md — 0.74x of the ch01 baseline,
  "within tolerance". Ch06 runs deliberately more formal (Kohagi's でございます register,
  Watanabe's stilted-then-corrupted speech, Jūzō's gravity); a light contraction pass
  on the rough easterner Watanabe's lines lifted it from 0.67x. Kohagi's polite
  register and the grave lines kept uncontracted by design.
- **Apparatus:** check_apparatus 0/0. qa_epub PASS (20 docs, 55 refs/bodies/backlinks).
  epubcheck 0 fatals / 0 errors / 0 warnings.

### One real omission caught and fixed (rule 4)
The draft dropped the clause しかし吉祥天女に似た顔の (a Kisshōten simile) at a column
boundary on the dense p196 — a mid-sentence drop check_align would not see (9 han in a
185-han paragraph). Caught on an OCR-coverage cross-check (grep 吉祥 in data/txt hit
p196), verified against the scan, restored in both data/zh/ch06.txt and the reading,
and Kisshōten added to the glossary + a footnote. An OCR kanji-bigram coverage diff
(OCR compounds absent from the transcription) surfaced only OCR garbles of content
already present (小菊=小萩, 衆楽=聚楽, 炒兵=妙兵衛), no other drop.

### The cipher device — how it is rendered
The enciphered slip (P20) is set as a centered `verse` block reproducing the printed
shinobi-moji glyphs as-is; the decoded message (P26) is a `vignette` (italic) block
carrying the English of the hiragana Gohei reads out. The shinobi-moji note explains
the invented syllabary. The glyphs are real-but-random CJK; e-readers with a CJK
fallback font show them, which is the point (an alien script), and the note carries
the meaning regardless.

### Notes added (5) — ch06 NEW first-appearances only
kunoichi (the 女→く-ノ-一 word-play, the shadow-world's view of the female agent);
shinobi-moji / the ninja cipher (the 49-sign syllabary; the chapter title; why writing
in cipher is itself a threat); the Kashima/Katori swordsmanship tradition (+ Bokuden,
cross-referenced forward); Miyamoto Musashi / the Yoshioka of Kyoto (flagged as a
proleptic aside — Musashi a child in 1591); Kisshōten (the Buddhist beauty-goddess).

### NOT re-noted (already placed in ch01-ch05; cross-referenced, not repeated)
Iga/Kōga, the Iga Rebellion, Tenshō/Eiroku dating, Honnō-ji, Hideyoshi/Nobunaga/
Ieyasu, Maeda Gen'i and the Kyoto magistracy, Sōkyū and the Sakai tea-masters, the
Hōin/Ōkurakyō ranks, the Jurakudai (noted in B05), the Hōkō-ji, the zodiac double-hours
(酉ノ刻/丑ノ刻/子ノ刻 all carried without a fresh note), rappa/shinobi, koku/chō/shaku/ken/
tsubo, the Kantō, Ōsaka Castle. Yoshitsune already glossed (source here 源九郎義経).

### No figures
find_figures 167-206 returned nothing; every page eyeballed for line art. ch06 is
text-only like ch01-ch05. Empty figure list is a deliberate decision (figures.json
stays {}).

### Renderings — reused unchanged (consulted before romanizing)
重蔵/葛籠重蔵 Jūzō/Tsuzura Jūzō, 黒阿弥 Kuroami, 風間五平/五平 Kazama Gohei/Gohei, 小萩
Kohagi, 今井宗久 Imai Sōkyū, 木さる/木猿 Kisaru, 下柘植次郎左衛門 Shimotsuge Jirōzaemon,
前田玄以 Maeda Gen'i, 伊勢屋嘉兵衛 Iseya Kahei, 珍皇院 the Chinnō-in, 方広寺 the Hōkō-ji,
聚楽第 the Jurakudai, 大蔵卿/法印 Ōkurakyō/Hōin, 家康 Ieyasu, 秀吉 Hideyoshi, 大坂/大坂城
Ōsaka/Ōsaka Castle, 三条 Sanjō, 鴨川 the Kamo, 乱波 rappa, koku/chō/shaku/ken.

### Renderings — added this batch (glossary.json; 27 rows)
People (11): Watanabe Satoru (渡辺慧, provisional — 慧 unglossed in the scan, the reading
a project call; narration uses bare 慧), Sakakibara Yasumasa (榊原康政), Tsukahara Bokuden
(塚原卜伝), Matsubayashi Samanosuke (松林左馬助, provisional), Ashikaga Yoshiteru (足利義輝),
Miyamoto Musashi (宮本武蔵), Taira no Shigemori (平重盛), Yoshinaka (義仲, Kiso Yoshinaka),
Myōbei (妙兵衛), Sunetsugi (すね次, provisional), Chōsokabe (長曾我部). Places (14): Nijō
(二条, covers 二条河原), Amidagamine (阿弥陀ヶ峰), Komatsudani (小松谷), Hitachi (常陸),
Kashima (鹿島), Katori (香取), Bandō (坂東), Ōsaka Castle (大坂城), Yanagimachi (柳町),
Wakasaya (若狭屋), Nakagyō (中京), Konoe (近衛), Marutamachi (丸太町), Sakaimachi (堺町 —
NOT the port city 堺). Terms (3): kunoichi (くノ一), ninja cipher / shinobi-moji (忍び文字),
Kisshōten (吉祥天女). Added directly into the sectioned people/places/terms (Edit tool,
no apparatus_merge flatten); notes merged via apparatus_merge. Substring-trap guard held
(B05 lesson): NO bare 慧→Satoru row ("Satoru" ⊂ "Watanabe Satoru"); bare 長曾我部→Chōsokabe
only (base form, longer renderings contain it); 二条→Nijō as the base (not 二条河原).

### Voice sheets — updates
- **Kohagi:** the chapter's psychological centre. Imai Sōkyū's adopted daughter and
  agent; polite ます/でございます, a smoky half-smile, a Noh-mask calm over a rappa's
  ruthlessness. She engineers the Jūzō-Gohei meeting and, on impulse, conceives of
  killing Jūzō as a way to reclaim the rappa's heart she feels herself losing to him —
  "a fierce kind of love". She crumbles for one instant (calls "Lord Tsuzura—") and
  hates herself for it. Manipulative and tender at once; runs a net of rappa (Myōbei,
  Sunetsugi) and bankrolls Watanabe with Sōkyū's gold.
- **Kazama Gohei:** opens the chapter, cold and vain; superior わし/じゃ, a "mean little
  shadow at the corner of the mouth". Unnerved by the cipher (a rappa lets fear stand,
  does not master it); slices the letter-box in four. Serves Maeda Gen'i at 200 koku.
- **Watanabe Satoru (new):** fictional Kashima-school rōnin, 28-29, broad-shouldered,
  a mad blue light in his eye; earnest and boastful, innocent of money (the east barely
  used coin) and so enslaved by it. Rough eastern register, contracts freely; his
  swagger cracks under Jūzō's ninja arts. Killed off — spared, rather — at the close.
- **Tsuzura Jūzō:** the reflective strategist again; sees through his own heart (he went
  to "nail" Kohagi's scheme but really went to see her), and grows "shabby by the moment"
  in his own eyes. The rooftop-of-the-Jurakudai duel he sets is pure ninja theatre.

## Batch B07 — ch07 聚楽 / Juraku (PDF/printed 207-236, offset 0)

**Status: complete.** 30 pages, 280 source paragraphs, ~7.0k English words, 5 new
notes (book total 60). All checks green (details below). ch01 is the frozen
register reference; ch07 measured against it at 0.99x (contractions living, not
stilted).

The chapter, in three movements. (1) The Jurakudai by night: Jūzō infiltrates the
moated palace (leather water-spider, shinobi rake), marvels at its Hōrai-like
beauty, and keeps a rooftop rendezvous with Kazama Gohei. Gohei, now Maeda Gen'i's
spy-catcher at 200 koku, will not be turned back to the rappa life; he lets Jūzō
pass "this once" but vows to hunt him from tomorrow, then fires a tea-pavilion as
a diversion (and kills several guards). By Iga's law Jūzō should cut him down;
he cannot. (2) The town: Jūzō walks Shijō, re-meets the spared Kumobei (from ch02)
and sets him as an ear at the Iseya; the street rumours (Mōri/Chōsokabe/Tokugawa/
Hosokawa/Hidetsugu behind the fire; the real one: Konishi Yukinaga's discontent
over the Korea war he must lead) confirm the anti-Toyotomi feeling Kuroami's
rappa are sowing. (3) Komatsudani: Jūzō visits Kohagi to force the truth of who
she serves; she confesses she wanted "to see the colour of his blood," watched
the Watanabe duel, offers herself; he means to kill her, cannot, kicks her down,
falls into "a fierce rush of love," and in anger at his own weakness drives his
blade through the fat of her right thigh — pinning her, sparing her — and vanishes.

### Tail verified against the scan (rule 4)
ch07's final paragraphs run onto folio 237: 同時に、おのれの不覚への／怒りが、重蔵の
右手をつかがしらに逆手にもちかえせしめた。刀は…女の右股のつけ根の脂肪を突き通した。
鋩子が畳を縫った。女は声もたてなかった。重蔵は刀を捨てて、寮から消えた。 Rendered
faithfully as the closing three paragraphs (no invented bridging text). Folio 237
was rendered and read: ch07 ends there; the ch08 opener 京の盗賊 / The Thief of the
Capital begins lower on 237 with 真葛ヶ原の萩の花に露がおりた。 — **B08 must NOT
re-translate that spillover.** The top of folio 207 is ch06's tail (慧… spared),
already placed in B06 and not re-translated here; ch07's body begins after the
聚楽 title with 聚楽第は、京の内野にある。

### Pipeline / engineering
- Rendered 207-237 (237 for the tail) at 300 dpi; `ocr_crop.py` with the standing
  crop (L 0.035 R 0.965 T 0.075 B 0.955), `jpn_vert --psm 5`, `--no-furniture-strip`;
  second read via `ocr_dual.py`. `pgrep -c tesseract` == 0 after each run. No
  scripts changed.
- Translated by reading the rendered page images directly; `data/zh/ch07.txt` is
  the hand-corrected, paragraph-aligned transcription (parity + crop-verification
  surface). Force-added (data/zh gitignored). `assemble.py` used only as a coverage
  cross-check (it welds paragraphs as always) — it caught one paragraph the
  page-level read had compressed (濠のふちからしずかに身を水中に没した。 on folio 209),
  which was restored.
- **Crop-verified** off the page image / furigana (6x PyMuPDF clips): 宇土二十四万石
  (Uto, 240,000 koku), 朝鮮王宣祖（せんそ）の母親平（へい） (King Sŏnjo / "mother Hei"),
  天竺 (Tenjiku), the middle of folio 218 (a suspected duplicated しかし line — only ONE
  present), the left of folio 222 (陽除けのはずの笠…) and 228 (the Watanabe re-meeting
  order). All numbers/names confirmed.
- **Figures:** none. `find_figures.py 207 236` returned nothing and every page was
  eyeballed for line art; ch07 is text-only (as ch01-ch06). Empty figure list
  recorded as a deliberate decision (figures.json stays {}).

### Checks run (all green)
- **Parity:** 280 | 280 (`check_structure --pairs`, `verify_unit`).
- **Numbers:** `verify_unit` / `check_numbers` 0 unresolved over 280 pairs. New
  `data/noise.txt` (ch07 block): 弥九郎 (Yakurō, the 九 a name), 三和土 (tataki
  packed-earth floor, the 三 part of the word). Reworded one line so the parser
  reads the carried 300 ("swells to three hundred", not a bare "three"). Every real
  quantity carried: 二百石/三百石/千石/二千石/万石, 二十四万石, 二丈, 二十人, 数丁/数間/
  数尺, 九年/十年, 半刻/小半刻.
- **Entities:** `qc_entities` 0 misses (census: 重蔵 x103, 五平 x31, 小萩 x22, 乱波 x20,
  伊賀 x11, 朝鮮 x10, 関白 x10, 黒阿弥 x9, 聚楽第 x8, 秀吉 x7). Named the character in two
  pronoun-only paragraphs (Kazama Gohei's scent; Jūzō's will). `check_content` OK
  across all seven units (ch07 208 name occurrences, 0 displaced).
- **Alignment:** `check_align` median ratio 10.48; 19 pairs out of band, all short
  dialogue / one-line utterances (high-ratio) or 3-4 char lines like "Jūzō?" — no
  low-ratio drop on a substantial paragraph.
- **Register:** `check_register --ref out/ch01_reading.md` — **0.99x of the ch01
  baseline, within tolerance**; contractions living (Gohei/Jūzō/Kumobei dialogue),
  Kohagi's でございます register kept polite by design, the essayistic asides kept in
  Shiba's gnomic present.
- **Apparatus:** `check_apparatus` 0/0; `verify_unit` 5 anchors ok. `qa_epub` PASS
  (20 documents, 60 refs/bodies/backlinks, 75 pagebreaks); **epubcheck 0/0/0/0**.

### Footnotes — new this batch (5, ch07's own first-appearances)
1. **Hōrai** (蓬莱 / Penglai) — the mythic isle of the immortals; the tower's shape
   (anchor "the isle of Hōrai").
2. **Konishi Yukinaga** (弥九郎 / 小西行長) — the Sakai medicine-merchant's son risen to
   lord of Uto, who did lead the 1592 Korea vanguard; a Christian daimyō (Agostinho),
   executed after Sekigahara — cross-referenced to the ch03 Sekigahara note.
   Corroborated (anchor "Konishi Yukinaga, Settsu-no-kami, lord of Uto").
3. **Sŏnjo** (朝鮮王宣祖) — the reigning king of Chosŏn Korea; the "mother Hei" league is
   Shiba's own baseless street-rumour (the narration says so). Presented as false
   (anchor "the mother of the Korean king Sŏnjo").
4. **Tenjiku** (天竺) — the old name for India; with Luzon, "to the ends of the earth"
   (anchor "to Tenjiku and to Luzon").
5. **The east/Kamigata swordsmanship proverb** (上り音曲、下り兵法) — refinement from the
   Kyoto region, martial prowess from the east (Azuma/Kantō); ties to the B06 Kashima
   note (anchor "swordsmanship down from the east").

### NOT re-noted (already placed in ch01-ch06; cross-referenced, not repeated)
Iga/Kōga, Tenshō/Eiroku dating, the Iga Rebellion, Honnō-ji, Hideyoshi/Nobunaga/
Ieyasu, Maeda Gen'i and the Kyoto magistracy (奉行/隠密役), Sōkyū and the Sakai
tea-masters, the Hōin/Ōkurakyō ranks and the Kampaku office, the Jurakudai (noted
B05 — the ch07 title; the opening's Ōmiya/Jōfuku-ji/Ichijō/Shimochōjamachi bounds
are self-locating and left un-noted), the Hōkō-ji, the Korea invasion (朝鮮入り/唐入り)
and Hideyoshi's heirless-ness (Tsurumatsu/Hidetsugu), Konishi Ryūsa (ch03), Sekigahara
(ch03), the zodiac double-hours (子ノ下刻/丑ノ上刻 carried without a fresh note) and the
半刻/小半刻 durations, rappa/shinobi, kunoichi, the Kashima/Katori tradition (B06),
Watanabe Satoru (B06), the Chōsokabe / Sakaimachi (B06), Tōdai-ji & Matsukura Kurando
& Kumobei (ch02), Iseya Kahei (ch01), Amidagamine/Komatsudani/Bandō (B06), Luzon
(ch02), the measures (koku/chō/ken/shaku/jō).

### Minor points left unfootnoted (the low-stakes tier)
一条 (Ichijō, the Jurakudai's north bound) is NOT a glossary key — the same two
characters are the counter 一条 ("a single [rake]") on folio 209, so a checked row
would false-flag that paragraph; kept in prose only. 平 (Hei) is likewise NOT a
glossary key (its single char ⊂ 五平 Gohei / 平城 etc.; the substring-trap guard).
The leather water-spider / shinobi rake (革水蜘蛛 / 忍び熊手) and "tread the tally of
castles" (城かず) are the fiction's own ninja furniture — glossary rows, not footnotes
(STYLE: don't footnote the story's props). "One dog barks at a shadow…" (一犬虚に吠ゆれ
ば万犬実に鳴く) rendered with its sense; the Chinese proverb left un-noted.

### Renderings — reused unchanged (consulted before romanizing)
重蔵/葛籠重蔵 Jūzō, 風間五平/五平 Kazama Gohei/Gohei, 黒阿弥 Kuroami, 小萩 Kohagi,
今井宗久/宗久 Imai Sōkyū/Sōkyū, 木さる Kisaru, 下柘植次郎左衛門 Shimotsuge Jirōzaemon,
渡辺慧 Watanabe Satoru, 前田玄以 Maeda Gen'i, 雲兵衛 Kumobei, 松倉蔵人 Matsukura Kurando,
伊勢屋嘉兵衛 Iseya Kahei, 秀吉 Hideyoshi, 家康 Ieyasu, 秀次 Hidetsugu, 小西行長 Konishi
Yukinaga, 隆佐 Konishi Ryūsa (bare, uncensused), 摂津守 Settsu-no-kami, 大蔵卿 Ōkurakyō,
法印 Hōin, 関白 Kampaku, 長曾我部 Chōsokabe, 堺町 Sakaimachi, 聚楽第 the Jurakudai,
方広寺 the Hōkō-ji, 東大寺 Tōdai-ji, 四条 Shijō, 阿弥陀ヶ峰 Amidagamine, 小松谷 Komatsudani,
坂東 Bandō, 鹿島 Kashima, 呂宋 Luzon, 朝鮮 Korea, くノ一 kunoichi, koku/chō/ken/shaku/jō.

### Renderings — added this batch (glossary.json; 16 rows)
People (5): 弥九郎 Yakurō (Konishi Yukinaga's common name), 毛利 Mōri, 細川 Hosokawa,
徳川 Tokugawa (house), 宣祖 Sŏnjo. Places (9): 内野 the Uchino, 大宮 Ōmiya, 浄福寺 the
Jōfuku-ji, 下長者町 Shimochōjamachi, 天竺 Tenjiku, 宇土 Uto, 粟田 Awata, 高麗 Korea
(older name), 蓬莱 Hōrai. Terms (2): 革水蜘蛛 leather water-spider, 忍び熊手 shinobi rake.
Added directly into the sectioned people/places/terms via a byte-preserving JSON
load/dump (ensure_ascii=False; git diff = insertions only, no reformat of existing
rows); notes merged via `apparatus_merge.py`. Substring-trap guard held (B05/B06
lesson): 一条 and 平 deliberately NOT added (see above).

### Voice sheets — updates
- **Tsuzura Jūzō:** the rappa's solitude at its height on the Jurakudai roof (face
  to face, alone, with the master of the realm); with Gohei, the old-comrade warmth
  under the duty to kill (borrows a bantering tone because his heart won't rise to
  it). With Kohagi the psychological climax of the book so far: goes to force the
  truth, is disarmed by her, cannot kill her, kicks her down, and — beaten by a
  "fierce rush of love" and furious at his own weakness — drives the blade through
  her thigh instead of her life. Terse, blunt (わし); reads the age like a ledger.
- **Kazama Gohei:** the assured spy-catcher; cold, glib, self-mocking (likens
  himself to a vanishing star). Will not go back to the rappa life; sets fire to
  the Juraku as a diversion and kills without hesitation; lets Jūzō pass "this once,"
  hunting him from tomorrow "to Tenjiku and Luzon." Superior わし/じゃ.
- **Kuroami:** the practical genin; ござる register, chides gently. Sees the fire's
  opening at once and moves the rumour-net; "no help for it" as he tucks his master in.
- **Kohagi:** deepened again. Polite ます/でございます, the smoky half-smile that does not
  freeze even under the blade; a wet, throaty laugh. Wanted "to see the colour of his
  blood," watched the Watanabe duel from the shadows, offers herself as a courtesan;
  under Jūzō's kill-threat she is drunk on her own strange desire, and wins — the
  point sinks. Her true master still hidden (Sōkyū's agent, a suspected Kōga plant).
- **Kumobei (雲兵衛):** back from ch02, the timid ex-wakō; clownish, over-grateful,
  deferential (ございます), begs to attend Jūzō; set as an ear at the Iseya.

### Environment
- setup.sh installed the Chinese packs only; `tesseract-ocr-jpn` + `-jpn-vert`
  installed manually (the known setup.sh gap). epubcheck re-fetched to
  /tmp/epubcheck-5.1.0 (container was recycled). The pre-existing checker-regression
  FAIL (`hook stands down on template stub`) persists and is unrelated to this book.

## Batch B08 — ch08 京の盗賊 / The Thief of the Capital (PDF/printed 237-301, offset 0)

580 source paragraphs. Autumn of Tenshō 19 (1591): Tsurumatsu is dead, Hideyoshi
half-broken and driving toward the Korea war. Kuroami's rappa band has turned to
thieving in the capital's low city to mock Hideyoshi's order; Kuroami hunts and
fails to kill Gohei (the Shijō-bridge fight). Jūzō, told the truth by Kisaru,
learns her father Shimotsuge Jirōzaemon is alive in Kyoto disguised as the mad
monk "Gyōzan"/the Saint of the Bamboo, and that Shimotsuge, Gohei and Kisaru are
now aligned against him (selling him to make Kisaru a 1000-koku samurai's wife).
At a Yanagimachi brothel Gohei proposes collusion; Jūzō refuses (throws a kozuka),
kills the informer courtesan Haruzemi, and escapes by smoke-bomb across the
ceiling. Then the long Shiba-shikan digression on Maeda Gen'i (the ox-cart
anecdote; his double game between Toyotomi and Tokugawa) and Gohei's audience,
where Gen'i unmasks him as an Iga rappa, raises him to 300 koku, and sets him to
hunt the thief — while Gohei reads Gen'i's own secret tilt toward the Tokugawa.

### Pipeline / engineering
- OCR: render 237-302 (302 for the tail check); ocr_crop 237-301 (L0.035 R0.965
  T0.075 B0.955, jpn_vert psm5, --no-furniture-strip); ocr_dual 237-301.
  pgrep -c tesseract 0 after each. **Translation was done by reading the rendered
  page images directly** and hand-building data/zh/ch08.txt (the parity surface);
  assemble.py welds this vertical Japanese and is coverage-only.
- **Two drops caught and fixed (rule 4 / the corollary about long single-pass
  units).** The chapter-opener (folios 237-238, dense with furigana leakage) was
  first-drafted with three clauses compressed away: `五十を過ぎて儲けたただ一人の子で
  あっただけに`, `鶴松が息を引きとるとすぐ東福寺に駈けこんで、にわかに髻を切った。切りながら`,
  and `髻を切るよりもはるかに` — all restored, and source paras 3+4 corrected to the
  ONE paragraph they are in the source (no indent at 五十を過ぎて). On folio 286 a whole
  clause `藤本安兵衛の組が追捕したところ、妖術を使って消えたという` was dropped and a non-source
  bridge (`妖術ではあるまい`) had crept in; both fixed to the printed text. Caught by the
  distinctive-compound grep of the raw data/txt OCR against the transcription
  (the B06/B07 method) — note the grep is meaningless until data/zh holds the
  HAND transcription (assemble.py silently overwrote it once; restore before
  grepping). After the fixes: 300 distinct 3+-kanji OCR compounds, 0 absent from
  the transcription (remainder are OCR garbles of present content).
- **Tail verified against the scan (rule 4):** ch08 ends on folio 302 at
  `五平は、ひそかに心の躍るのを覚えて、思わず陰湿な笑いが唇許にのぼった。`, BEFORE the ch09
  title 甲賀ノ摩利. ch07's tail occupies the TOP of 237 (through 重蔵は刀を捨てて、寮から
  消えた。) and was NOT re-translated. B09 must not re-translate the 甲賀ノ摩利 opener
  on 302.
- Figures: text-only chapter (ch01-ch07 all were); no figure list — deliberate.
- Crop-verified: クロロガキ (a padlock-pick; kept as "kurorogaki" with a descriptive
  gloss), 欟ながらの刀 (rendered "scabbard and all"), 乱波のでしょうを隠している (Gohei hides
  his rappa birth), 仰山/ぎょうざん (Gyōzan), the p266 betrayal-reasoning columns,
  and the Ishida/Kanamori/Kiyomasa names against the furigana.

### Checks run (all green)
- verify_unit ch08: numbers 0/580 unresolved; anchors 6 ok.
- check_structure --pairs: parity 580 | 580 OK.
- check_align ch08: 580/580, median ratio 10.62 en/han (short dialogue lines ride
  high, expected).
- qc_entities: 0 misses (census 重蔵 x124, 五平 x81, 黒阿弥 x55, 玄以 x19 …).
- check_content: ch08 400 name occurrences, all in the paired paragraph.
- check_register --ref out/ch01_reading.md: **14.0/1k, 0.89x ref** (within
  tolerance). First draft was STILTED at 0.02x — a full contraction pass on the
  casual dialogue (Jūzō, Kisaru, the low-city banter) was needed, exactly the ch05
  lesson; Kuroami's grave ござる, Gohei's obsequious まする to Gen'i, and the quoted
  Gen'i-to-Gifu letter were left uncontracted by design. (Watch the auto-pass for
  clause-final over-contraction: "you're."/"there's."/"how it's" were reverted.)
- check_apparatus: 0 failures. qa_epub: PASS (66 refs/bodies/backlinks, all links
  resolve). epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings / 0 infos.

### data/noise.txt — added this batch (name/word numerals; longest-literal order)
十郎左衛門, 十郎左 (Maekawa Jūrōzaemon); 三法師 (Sanbōshi); 三成 (Mitsunari); 一条
(the Ichijō house); 百地 (Momochi); 億劫 (okkū, "a burden"); 二重 (double); 二階 (the
upper storey); 一尺五寸 (blade length — carried in English as "a shaku and a half").
千金 was NOT noised — the English now carries it ("a thousand-gold steed").

### Footnotes (6 new, at first appearance)
1. Makuzugahara (the utamakura moor east of Kyoto, famed for autumn bush-clover).
2. Ishida Jibu-no-shōyū = Ishida Mitsunari (1560-1600); central at Sekigahara.
3. The field of Yamazaki (Hideyoshi's 1582 victory over Akechi after Honnō-ji).
4. The Toyotomi Five Commissioners (go-bugyō; Gen'i and Mitsunari both members).
5. Yanagimachi (the licensed pleasure-quarter of the capital, pre-Shimabara).
6. The "crossing of Iga" (Iga-goe): Ieyasu's 1582 flight over Iga under Hattori
   Hanzō — historically attested, the numbers (78 / 200 / 1000 kan) less firm.
   Corroborated in the note (rule 5).

### NOT re-noted (already placed in ch01-ch07; cross-referenced, not repeated)
Tsurumatsu's death (ch03), Nyoigatake/Daimonji (ch04), Tenshō dating & the Iga
Rebellion (ch01), Honnō-ji (ch01), Hideyoshi/Nobunaga/Ieyasu, Maeda Gen'i & the
Kyoto magistracy (ch04), Hattori Hanzō (ch05), Katō Kiyomasa (ch04), the
Hōin/Ōkurakyō/Kampaku titles (ch03), Sekigahara, the Korea invasion & Konishi
Yukinaga (ch03/ch07), Sen no Rikyū & the tea/wabi cult (ch03), the Jurakudai &
Hōkō-ji (ch07/ch03), Shijō/Komatsudani/Shimochōjamachi geography (ch06/ch07),
Tenjiku (ch07), the kozuka/wakizashi/sageo furniture, the measures (koku/chō/ken/
shaku/kan), rappa/shinobi and jōnin/genin, kunoichi (ch06). The Seven Forms
(七方出), the ninja-tool catalog, and the legendary Iga-ninja roll are the
tradition's own furniture — glossary/prose, self-explained by Shiba, not
footnoted (STYLE: don't footnote the story's props).

### Minor points left unfootnoted (low-stakes tier)
Genpei ("since the old days of the Genji and the Heike") left proverbial;
Nobutada/Sanbōshi/Hidenobu and the Uto-castle episode are narrated in full by
Shiba/Gohei (glossary rows, no note); 右府/Minister of the Right self-glosses to
Nobunaga in the next sentence; 警視総監 ("Superintendent-General of Police") is
Shiba's own deliberate modern analogy (shikan), kept as-is.

### Renderings — reused unchanged (consulted before romanizing)
重蔵 Jūzō, 五平/風間五平 Gohei/Kazama Gohei, 黒阿弥 Kuroami, 小萩 Kohagi, 木さる Kisaru,
下柘植次郎左衛門 Shimotsuge Jirōzaemon, 今井宗久 Imai Sōkyū, 前田玄以/玄以 Maeda Gen'i/Gen'i,
下呂正兵衛康次 Gero Shōbei Yasuji, 雲兵衛 Kumobei, 伊勢屋嘉兵衛 Iseya Kahei, 服部半蔵 Hattori
Hanzō, 楯岡ノ道順 Tateoka-no-Dōjun & 音羽ノ城戸 Otowa-no-Kido (already in glossary — used
the glossary forms, not "Dōjun of Tateoka" etc.), 松原通 "Matsubara road" (glossary),
秀吉/信長/家康/徳川, 大蔵卿法印 Ōkurakyō-Hōin, 京都奉行 Kyoto magistrate, 方広寺 Hōkō-ji,
四条(大橋) Shijō, 小松谷 Komatsudani, 下長者町 Shimochōjamachi, 笠置 Kasagi, 柳町 Yanagimachi,
天竺 Tenjiku, 呂宋/Luzon, 大和/山城/三河/美濃/紀州/土佐/関東/大坂, koku/chō/ken/shaku/小半刻.

### Renderings — added this batch (glossary.json; 22 rows)
People (12): 石田三成 Ishida Mitsunari, 三成 Mitsunari, 清正 Kiyomasa, 正則 Masanori,
前川十郎左衛門 Maekawa Jūrōzaemon, 十郎左衛門 Jūrōzaemon, 藤本安兵衛 Fujimoto Yasubei,
金森 Kanamori, 春蟬 Haruzemi, 信忠 Nobutada, 三法師 Sanbōshi, 織田秀信 Oda Hidenobu.
Places (9): 真葛ヶ原 Makuzugahara, 東福寺 Tōfuku-ji, 東寺 Tō-ji, 二条城 Nijō castle,
岐阜城 Gifu castle, 尾張 Owari, 甲府 Kōfu, 中村 Nakamura, 大和小路 Yamato-kōji.
Terms (1): 七方出 the Seven Forms (shichihōde). Added directly into the sectioned
people/places/terms via a byte-preserving JSON load/dump (ensure_ascii=False;
insertions only). Gen'i's aliases 徳善院 Tokuzen'in and 半夢斎 Hanmusai kept in prose
only (rendered consistently; 徳善院玄以 = "Gen'i" once, so not a checked glossary key).
Substring-trap guard held: 一条 and 平/五平 stayed out of the glossary as before.

### Voice sheets — updates
- **Tsuzura Jūzō:** the age has turned under him — grudge has cooled into the one
  "tremendous ninja's stage" of killing the master of the realm; the rest (Gohei,
  Kohagi, even Kisaru) is "play within this time of waiting." Reads the betrayal of
  the three (father, Gohei, Kisaru) and laughs it off as the fool's role; still
  cannot kill a woman who comes to him, but kills the informer courtesan Haruzemi
  without a flicker ("the men of Iga count a life no more than a mosquito's").
- **Kuroami:** acts on his own to execute the traitor Gohei (the jōnin plans, the
  genin does the dirty work); loses the Shijō fight to Gohei's nimbler art, comes
  home with a cut wrist and a rare bashful smile, and rages at Jūzō's softness
  ("ten years fiddling with the Buddha on Otogi Pass"). Grave archaic ござる.
- **Kazama Gohei:** cold, glib, self-serving; proposes open collusion to Jūzō
  (both keep their roles, both profit); to Gen'i he plays the ambitious samurai
  sick of the rappa's low place, and reads his master's secret Tokugawa tilt.
  Superior わし/じゃ to inferiors, obsequious まする to Gen'i.
- **Shimotsuge Jirōzaemon:** ALIVE and in Kyoto, master of the 七方出 disguise, best
  at the monk-form; has lived a decade as the mad "Gyōzan"/Saint of the Bamboo,
  crossing to Iga every ten days. Gruff, teasing, われ for "you", 〜じゃ; dotes on
  Kisaru (his daughter) enough to sell Jūzō for her sake — but a rappa's loyalty
  is provisional and Jūzō would cut him without mercy if he turned.
- **Kisaru (木さる):** Shimotsuge's daughter; wants to be Gohei's wife, begged her
  father to arrange it (which set the sale of Jūzō in motion); loves Jūzō too and
  cannot untangle her own heart (trained in renjutsu from age three, "a guileless
  apparition"). Asks Jūzō to take her, then won't pledge; pushes him away in tears.
- **Maeda Gen'i (徳善院/半夢斎):** the shrewd, tangled magistrate — a former Owari abbot
  risen by wit; the ox-cart tyrant who cowed the capital; secretly tilting to the
  Tokugawa (historically the first to warn Ieyasu of the Ishida rising). Lordly,
  heavy-lidded, formal; sets Gohei to "probe, not seize."

### Where the story stands (end of ch08)
The three-way trap has hardened: Shimotsuge + Gohei + Kisaru are selling Jūzō to
the Maeda/magistracy for Gohei's rise; Gen'i, tilting Tokugawa, wants the affair
watched not closed. Jūzō, now a stranger and enemy to all of them, holds to the
one strike on Hideyoshi and waits for the perfect moment. ch09 甲賀ノ摩利 / Mari of
Kōga (opener already on folio 302) turns to Kōga — presumably Kohagi's true side.

### Environment
- setup.sh installed the Chinese packs only; tesseract-ocr-jpn + -jpn-vert
  installed manually (known gap). epubcheck 5.1.0 at /tmp/epubcheck-5.1.0 (present;
  container had it). The pre-existing checker-regression FAIL (hook stands down on
  template stub) persists and is unrelated to this book.
- **Trap for the next session:** `assemble.py chNN a b` WRITES data/zh/chNN.txt and
  will clobber a hand transcription. Redirect it or back up data/zh/chNN.txt first;
  the coverage grep must run against the HAND file, not the welded one.

## Batch B09 — ch09 甲賀ノ摩利 / Mari of Kōga (printed folios 302-337)

**Scope done end to end.** ch09 body begins on folio 302 after the 甲賀ノ摩利 title
(しかし、前田玄以は風間五平が思ったほど甘い男ではなかった。) and its tail SPILLS onto
folio 338 (PDF 340), five paragraphs before the 奇妙な事故 title, ending
「わるい虫じゃ」/ 黒阿弥は苦虫を嚙みつぶしたような顔を作った。 Those spillover paragraphs are
translated as part of ch09; B10 must NOT re-translate them (ch10 body begins after the
title with 錯綜した関係にある京の忍者のあいだに、ひとつの真空地帯ができた。).

### CRITICAL: a scanner double-feed inside this chapter (corrects the survey offset note)
The survey said "offset 0 through folio 302 ... +2 drift across ~338-397." The real
mechanism, verified this batch by reading every folio and the OCR: **PDF pages 326 and
327 are DUPLICATE leaves** (re-scans of folios 324 and 325; confirmed by identical OCR
and by the running-head folios reading 324, 325 on those PDF pages). The true sequence
resumes at **PDF 328 = folio 326**. So:
- PDF 302-325 == folios 302-325 (offset 0)
- **PDF 326, 327 = folios 324, 325 (DUPLICATES; skipped)**
- **PDF 328-339 = folios 326-337 (folio = PDF minus 2)**
- PDF 340 = folio 338 = ch10 opener (matches the kickoff's "PDF 340 = printed 338")
No content was lost: folio 325's cliffhanger (…彼自身の胸に) continues cleanly at PDF 328
(…響くものがある。), and PDF 326/327 only repeat folios 324/325, which were transcribed
directly from PDF 324/325. **B10-B13: the +2 drift begins at folio 326 (PDF 328), i.e.
folio = PDF - 2 from PDF 328 onward through this span; build data/pagemap accordingly.**
The coverage grep was run over PDF 302-339 with 326/327 excluded.

### Checks run (all green)
- **Transcription:** hand-built data/zh/ch09.txt from the page images (324 body paragraphs
  + title). Coverage cross-check: extracted every 3+-kanji compound from the raw OCR
  (PDF 302-339, dups 326/327 excluded) and confirmed each appears in the hand file; all
  115 "missing" hits were OCR garbles of content present (e.g. 塵利支天→摩利支天,
  承丁入道→承禎入道, the roster names, the mantra). No drops.
- **check_numbers** (--noise data/noise.txt): 0 unresolved (324 pairs).
- **check_structure / verify_unit:** parity 324 | 324 OK; anchors 11 ok.
- **check_align:** median 9.15 en/han, 17 short-line outliers (all short dialogue lines,
  in line with the accepted ch08 pattern; no missing text).
- **qc_entities:** 0 misses (top: 甲賀 54, 洞玄 43, 玄以 40, 伊賀 38, 黒阿弥 20).
- **check_content:** OK across all units (272 name occurrences in ch09, all in the paired
  paragraph; two initial 摩利洞玄/"Mari Dōgen" displacements fixed).
- **check_register** (--ref out/ch01_reading.md): **1.21x** the ch01 reference
  (contractions 19.0/1k vs 15.8; em-dash 14.6/1k; rhythm CV 0.81). Dialogue-heavy
  chapter contracted as written, so it sits ABOVE the reference, not below; no post-hoc
  contraction pass needed (the recurring stilted failure mode was avoided).
- **qa_epub:** PASS (34 files, 27 documents, 77 notes ref/body/backlink match, all links
  resolve). **epubcheck 5.1.0:** 0 fatals / 0 errors / 0 warnings / 0 infos.

### Figures
find_figures.py 302-339 returned nothing; eyeballed every page. ch09 is text-only (like
ch01-ch08). Empty figure list recorded as a deliberate decision.

### Notes added (11 new first-appearances; book total 66 -> 77)
Marishiten/Mārīcī (the deva behind the 甲賀ノ摩利 byname); the Udaifu (右府 = Nobunaga, court
title); the Naifu (内府 = Ieyasu, Naidaijin); the daughter of the lord of Odani (Yodo-dono;
the dead child Tsurumatsu, cross-ref ch03); Rokkaku/Sasaki Yoshikata (Hakkansai, Kohagi's
real father, historical; the Kohagi tie is the novel's invention); the 1487 Magari campaign
and shogun Yoshihisa; the fifty-three houses of Kōga; Kōga Saburō (medieval legend); Oiro
Tayuya / Prince Shōtoku's spy (the Iga founding myth); Hideyoshi's Odawara campaign (1590);
Nagoya castle in Hizen (the Korean-war HQ, distinct from Owari Nagoya).

### NOT re-noted (already placed earlier; cross-referenced instead)
Iga/Kōga, Tenshō/Eiroku/Kōji/Bunroku dating, the Iga Rebellion, Honnō-ji, Hideyoshi/
Nobunaga/Ieyasu, the Hōin/Kampaku/Ōkurakyō/Ishida-office titles, Imai Sōkyū and the Sakai
merchants, Ishida Mitsunari (石田治部少輔/三成), the Korea invasion and Konishi Yukinaga,
Tsurumatsu/Hidetsugu, the measures (kan/koku/kanmon), rappa/shinobi/jōnin/genin, 方広寺/
Hōkō-ji, Gifu castle, Maeda Gen'i and the Kyoto magistracy, Hattori Hanzō, おとぎ峠/Otogi Pass.
Left deliberately unfootnoted (minor / self-explaining in the text): the 53-house roster
names, Kyōgoku house, Ishida Masatsugu, the Korean place-names (Pusan/Tongnae/Yangsan/
Miryang/Kimhae/Kyŏngju/Iki), Nigatsu-dō lacquer, boar's-gall folk medicine, the
「甲賀古士訴状」 document, the 文禄/天正二十年 dual-era dating (rendered so both years show).

### Renderings — reused unchanged
All principal cast and majors from glossary.json: Tsuzura Jūzō (葛籠重蔵/重蔵), Kazama Gohei
(風間五平/五平), Shimotsuge Jirōzaemon (下柘植次郎左衛門), Kuroami (黒阿弥), Kohagi (小萩), Imai
Sōkyū (今井宗久), Maeda Gen'i (前田/玄以; aliases 徳善院 Tokuzen'in in prose only), Ishida
Mitsunari (石田三成/三成), Hideyoshi/Nobunaga/Ieyasu, Iga/Kōga/Ōmi/Sakai/Gifu, 方広寺 Hōkō-ji,
Iseya Kahei (伊勢屋嘉兵衛), おとぎ峠 Otogi Pass, the measures.

### Renderings — added to glossary.json this batch
people: 摩利洞玄 Mari Dōgen (+ bare 洞玄 Dōgen), 望月刑部左衛門 Mochizuki Gyōbuzaemon (+ bare
刑部左衛門 Gyōbuzaemon), 抜関斎 Hakkansai (= Rokkaku Yoshikata), 承禎入道 Jōtei. terms: 摩利支天
Marishiten, 甲賀三郎 Kōga Saburō, 甲賀文 Kōga letter (fictional device, glossary line not
footnote). places: 釜山城 Pusan castle (added so it subsumes the 山城/Yamashiro substring in
qc/content). The Kōga byname 甲賀ノ摩利 renders "Mari of Kōga"; the short 摩利 alone = "Mari"
is NOT glossaried (substring of both 摩利洞玄 and 摩利支天).

### noise.txt added (source-side name numerals; longest first)
四郎兵衛, 十郎, 八郎, 七郎, 三郎, 五郎, 四方, 八田, 三雲, 三河 (roster/name numerals);
六角 (Rokkaku); 三満多 (Marishiten mantra syllable); 十四、五 ("fourteen or fifteen", the 五
reads 15). Real quantities kept in the English: fifty kanmon, a million koku, three hundred /
two hundred Kōga men, fifty-three houses, nine years, ten years, ten days, half a year, a
year or two, Tenshō 10 / Eiroku 5 & 11 / Chōkyō 1 / Bunroku 1 / Tenshō 20, 3rd month 26th day.

### Where the story stands (end of ch09)
The Kōga side is now on the board and Kohagi's secret is out: she is the daughter of Rokkaku
(Sasaki) Yoshikata, raised in the Kōga arts by Mochizuki Gyōbuzaemon and planted on Imai
Sōkyū by Ishida Mitsunari. Gen'i, still hunting the "capital thief," recalls the old debt
and hires Mari Dōgen of Kōga, the aged rappa who once carried him out of the Honnō-ji trap.
Dōgen and Jūzō each learn the other is the enemy leader; each sizes the other up (Dōgen: "a
trial of skill between Kōga and Iga"). Then Hideyoshi leaves for the Korean war and the
capital's shadow-war goes quiet: Jūzō, waiting for the coming collapse of the Toyotomi world,
lies low but will NOT leave the capital; Dōgen, uneasy at the silence, stays on in Gen'i's
grounds disguised as a shrine-keeper. Dōgen has already glimpsed the sleeping Kohagi at the
Komatsudani villa and left a Kōga calling-card.
