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
