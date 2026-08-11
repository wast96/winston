# HANDOFF — The Owl's Castle (梟の城, Shiba Ryōtarō)

One batch = one conversation. This file is how a fresh session with no memory
picks up. The paste-ready kickoff is first; everything below it is context.

## Message to paste into the next chat

```
Owl's Castle B05

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json, then STYLE.md (note the "calibrated at the ch01 voice gate" subsection: plain over arcane diction, people-as-agents not body-part calques, keep the author's own tense in gnomic/establishing description, gloss technical terms). We are translating Owl's Castle (梟の城, Shiba Ryōtarō) from an image-only scan (source.pdf) into an annotated English EPUB, per CLAUDE.md. Work ONLY on branch claude/owls-castle; expect the harness to start you on a stray branch and consolidate per rule 2 (fast-forward/cherry-pick any commits onto claude/owls-castle, push it, delete the stray). Deliverable out/owls-castle.epub. Vertical, right-to-left Japanese with furigana; the offset is 0 in this range (printed folio == PDF render page).

Do Batch B05 = ch05 「羅刹谷」 (Rakshasa Valley), PDF pages 149-166 (printed folios 149-166), end to end per the CLAUDE.md pipeline. ch01 is the FROZEN register reference: run scripts/check_register.py --ref out/ch01_reading.md out/ch05_reading.md on ch05 and fix any drift.

Environment / pipeline (the batch engineering is already done and committed; do NOT re-patch or revert the scripts):
1. ./setup.sh, THEN apt-get install -y tesseract-ocr-jpn tesseract-ocr-jpn-vert (setup.sh omits the Japanese packs). epubcheck is at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup.sh if the container was recycled).
2. OCR: render.py 149 166 --dpi 300; then ocr_crop.py 149 166 --left 0.035 --right 0.965 --top 0.075 --bottom 0.955 --lang jpn_vert --psm 5 --no-furniture-strip; ocr_dual.py 149 166 for the second read. Verify pgrep -c tesseract is 0 afterward (OMP_THREAD_LIMIT=1; kill the process GROUP if a run stalls).
3. find_figures.py 149 166 AND eyeball every page for line art (ch01-ch04 were text-only; if ch05 is too, record an empty figure list as a deliberate decision).

Translate:
4. IMPORTANT: the automated assemble.py welds paragraphs on vertical Japanese (the OCR mangles the sentence-final punctuation can_break() relies on). Translate by READING the rendered page images directly (data/png/p0NNNN.png), and build data/zh/ch05.txt as a hand-corrected, paragraph-aligned transcription read off the scan. That file IS the parity surface and the crop-verification record; force-add it (data/zh/ is gitignored). NOTE ON THE OPENER: ch04's final sentence and the Gohei/Gyōzan exchange run onto the TOP of folio 149 and end there ("…それは木さるではなかった。……"); that block is ALREADY in ch04 and is NOT part of ch05. ch05's body begins AFTER the 「羅刹谷」 title on folio 149 ("東山の南に、泉山という、楓樹に蔽われた峰がある。…"). BEFORE translating, read the final two pages of ch04's English (the tail of out/ch04_reading.md) so the voice carries; ch05 opens on a landscape set-piece (a hidden valley south of Higashiyama, the Otonashi-gawa) — expect Shiba's gnomic-present geographic register (keep his tense).
5. Consult glossary.json and STYLE.md BEFORE romanizing any name (Hepburn with macrons; conventional forms for Hideyoshi/Nobunaga/Kyoto/Tokugawa). The principal cast and the major historical/place names are decided in glossary.json; reuse them unchanged and record in PROGRESS which rows you reused. New Kyoto/Higashiyama geography likely (泉山, 音無川, etc.) — add with a status. NOTE: apparatus_merge.py writes glossary rows to the FILE ROOT, but glossary.json is SECTIONED (people/places/terms) — after merging, move each new row into its section (a one-off script preserving bytes, no CJK retyped) and re-run check_content/qc_entities. Or add rows directly into the sections with the Edit tool (that is how B04 did it — no flatten). Crop-verify every proper name, number, unit designation and low-confidence span against the page image / furigana. NEVER invent bridging text: if OCR cuts off mid-sentence or a leaf is damaged, crop the scan and read the actual continuation; verify the unit's FINAL paragraphs against the scan explicitly before shipping (ch05's tail may again spill onto folio 167, the ch06 opener — render it and check).
6. Write out/ch05_reading.md, '## Rakshasa Valley' as the h1 (settle the English title at translation; 羅刹 = rakshasa, a flesh-eating demon of Buddhist myth — footnote it at first body appearance). Add a ch05 entry to data/checks.json (docs + sources). make_bilingual.py ch05 (parity FIRST). Then run: verify_unit.py ch05 (it auto-uses data/noise.txt); check_structure.py --pairs data/zh/ch05.txt out/ch05_reading.md; check_align.py ch05; qc_entities.py out/ch05_bilingual.md glossary.json; check_content.py --config data/checks.json --glossary glossary.json; check_register.py --ref out/ch01_reading.md out/ch05_reading.md.
7. Footnotes per the CLAUDE.md reader model (a Westerner with no Japanese history). Recurring subjects already noted in ch01-ch04 are NOT re-noted (grep notes.json first; cross-reference instead): Iga/Kōga, Tenshō/Eiroku dating, the Iga Rebellion, Honnō-ji, Mount Hiei, Hideyoshi/Nobunaga/Ieyasu, the Sakai tea-masters/Rikyū/Sōgyū/Sōkyū, the Hōin/Hōgen ranks and Kampaku office, Sakai the free-city, the meibutsu tea cult and Matsushima caddy, Tenka Fubu, Sekigahara, the Korea invasion, Tsurumatsu/Hidetsugu, Nanban, the Nara Great Buddha (Tōdai-ji), the zodiac double-hours, Aizen Myō-ō, the wakō/bahan ships and Luzon, the measures shaku/chō/koku/ri/ken/kin, rappa/shinobi, jizamurai/gōshi, AND the B04 first-appearances: 放下僧 juggler-priests, Nyoigatake/Daimonji, the Gion aside, Katō Kiyomasa (加藤肥後守), Maeda Gen'i and the Kyoto magistracy. Note only ch05's NEW first-appearances (羅刹/rakshasa; more Kyoto/Higashiyama geography; anything historical). Anchor notes to BODY phrases (verbatim substrings), not heading-only text — the builder matches body prose and refuses a heading-only anchor. Add via apparatus_merge.py (never a heredoc); check_apparatus.py clean.
8. Rebuild the cumulative EPUB (build_reading_epub.py); qa_epub.py until green; epubcheck. Record every check result in PROGRESS.md (the per-batch "NOT re-noted" list, the register result, and the renderings reused/added).

Deliver end to end; do not pause for approval mid-batch. At the end, in the SAME chat reply: attach the built out/owls-castle.epub AND paste the B06 kickoff (ch06 「忍び文字」 The Ninja Cipher, PDF/printed 167-206) verbatim in a fenced block. Cite printed folios, never PDF page numbers, in the notes.
```

## Done so far
- **Survey:** 19-section structure recovered into book.json; metadata set; skeleton
  EPUB built; page furniture measured (top-only; crop L0.035 R0.965 T0.075 B0.955;
  model jpn_vert psm5); offset 0 for folios 7-302 and 425-660, drifts +2 across
  ~338-397 (B09-B13 must build data/pagemap by reading folios there).
- **B01 = ch01 おとぎ峠 / Otogi Pass (folios 7-63): COMPLETE, approved at the voice
  gate.** ch01 is the FROZEN register reference. (523 source paragraphs, 17 notes.)
- **B02 = ch02 濡れ大仏 / The Rain-Soaked Buddha (folios 64-89): COMPLETE.** 276
  source paragraphs, 6 notes. Kisaru and Kohagi introduced; Matsukura killed,
  Kumobei conscripted.
- **B03 = ch03 白い法印 / The White Hōin (folios 90-123): COMPLETE.** 385 source
  paragraphs, 16 notes. Sōkyū's biography and the tea-room confrontation; the
  commission's motive (Hideyoshi's Korea war) drawn out; Kohagi revealed as
  Sōkyū's adopted daughter and made Jūzō's contact.
- **B04 = ch04 木さると五平 / Kisaru and Gohei (folios 124-148, tail on 149): COMPLETE.**
  286 source paragraphs, 5 new notes. All checks green (numbers 0, parity 286|286,
  qc_entities/check_content/check_apparatus clean, register within tolerance,
  qa_epub PASS, epubcheck 0/0/0/0). Shifts to Kyoto: Kisaru's crowd-illusion on the
  Shijō riverbank; the monk Gyōzan at the ruined Chinnō-in; Gohei confesses he has
  deserted Iga to serve Maeda Gen'i (magistrate of Kyoto) as Gero Shōbei Yasuji,
  rapes and recruits Kisaru, and learns Jūzō is in the capital. Notes total: 44.

## ch01 corrections made earlier (do NOT undo)
1. ch01's dropped final two paragraphs restored in B02 (Iseya Kahei shop
   instruction + "idle talk of the world"); ch01 parity is 523 | 523.
2. ch01's Great Buddha note corrected in B02 to the NARA Tōdai-ji Vairocana
   (roofless since Matsunaga burned it 1567), not Hideyoshi's Hōkō-ji. In B03,
   Hideyoshi's OWN Great Buddha (方広寺大仏, the Kyoto Hōkō-ji) appears and is
   footnoted as DISTINCT from the Nara one. Keep the two straight.

## Tooling in place (do NOT revert)
- `ocr_crop.py`: kana in the despace class; `--no-furniture-strip` skips the
  Chinese strip_folio/strip_runfoot. Furniture here is top-only, cropped.
- `ocr_dual.py`: Japanese second read (jpn_vert psm5 on grayscale + Otsu variant).
- `check_content.py` / `qc_entities.py`: skip non-dict glossary sections; subsume a
  shorter glossary key covered by a longer matched key at the same span.
- `data/checks.json`: the {docs, sources} config. ch01-ch04 in.
- `data/noise.txt`: check_numbers noise. B03 added 惣五郎, 千利休, 九州, 三宅, 巨万,
  五体, 四肢, 二千二百 / 千二百. B04 added the Kyoto place-names 四条 (Shijō), 三条
  (Sanjō), 六波羅 (Rokuhara) — numeral is the name, not a count. Extend per its
  header, longest literal first; never noise a real quantity you dropped.
- **apparatus_merge glossary gotcha:** it flattens glossary rows to the file ROOT,
  but glossary.json is sectioned. B02/B03 merged then moved rows; B04 added rows
  DIRECTLY into people/places/terms with the Edit tool (no flatten, cleaner). Either
  way, re-check content/entities after. Notes/figures merge fine as-is.
- **Note anchors:** must be verbatim substrings of the BODY prose; the builder
  refuses a heading-only anchor. Pick a unique body phrase (a string that appears
  once) so the marker lands where you mean.

## Method note (every batch)
`assemble.py` is unreliable on this vertical-Japanese OCR (welds paragraphs). The
working method: translate by reading the rendered page images directly, and
hand-build `data/zh/chNN.txt` as a corrected, paragraph-aligned transcription (the
parity surface and crop-verification record). Force-add it (data/zh is gitignored).
**A chapter's last sentence can run onto the next chapter's opener folio** — ch03's
did (onto 124), and ch04's did (onto 149, the Gohei/Gyōzan exchange, ending "それは
木さるではなかった。……"). Always render the next folio's top to recover the true
tail before shipping (rule 4), and make sure the NEXT batch does not re-translate it.

## Renderings settled in glossary.json (reuse unchanged; consult before romanizing)
Principal cast (principal:true): Tsuzura Jūzō (葛籠重蔵), Kazama Gohei (風間五平),
Shimotsuge Jirōzaemon (下柘植次郎左衛門), Kisaru (木猿; written 木さる in ch04),
Kuroami (黒阿弥). Kohagi (小萩) and Imai Sōkyū (今井宗久) are the other leads.
B04 people added: Maeda Gen'i / Gen'i / Maeda (前田玄以/玄以/前田), Katō Higo-no-kami
(加藤肥後守 = Katō Kiyomasa), Iten Gyōzan / Gyōzan (以天仰山/仰山), Kuranawate-no-
Shishiji (蔵縄手ノ鹿次), Gero Shōbei Yasuji (下呂正兵衛康次, Gohei's alias). B04
places added: Shijō (四条), Sanjō (三条), the Kamo river (鴨川), Higashiyama (東山),
Nyoigatake (如意ヶ岳), the Shōren-in (青蓮院), Gion (祇園), Kennin-ji (建仁寺),
Matsubara road (松原通), Rokuhara (六波羅), Kiyomizu (清水), the Chinnō-in (珍皇院),
Tosa (土佐). B04 terms added: the Bamboo Saint (竹ノ上人). Earlier rows (Nobunaga,
Hideyoshi, Ieyasu, Sōkyū, Sōgyū, Iga, Kōga, Sakai, Nara, Tōdai-ji, rappa, Tenshō,
the measures, the B03 Sakai/tea rows, etc.) are all in glossary.json.

## Voice sheets (consult at every dialogue scene)
- **Tsuzura Jūzō:** mid-30s, thick-shouldered, tall for a ninja; terse, guarded.
  A raw hunger for revenge under a monk-like idleness. Plain samurai forms (わし).
  Dry, darkly bawdy; drawn to Kohagi against his creed. (Offstage in ch04, but his
  face haunts Kisaru; Gohei now hunts him for the 1000-koku reward.)
- **Kazama Gohei:** a LEAD in ch04. Beautiful, androgynous, cold, clerkly, cruel;
  a "mean little shadow at the corner of the mouth" when he smiles. To Kisaru he
  uses superior/intimate わし・じゃ (not the polite ます・です he gives his master).
  Has deserted Iga for ambition; serves Maeda Gen'i as a spy-catcher under the alias
  Gero Shōbei Yasuji; rapes and recruits his own betrothed without warmth ("a hollow
  look," "a barefaced emptiness"). Means to use Kisaru against Jūzō.
- **Shimotsuge Jirōzaemon:** the disfigured old master; gruff, archaic, teasing, wry
  (あはは), secretly tender toward Jūzō. Creed: be as earth, stone, wind. Old dialect
  (〜じゃ, 〜のう), われ for "you". (Kisaru acts "in his stead" in ch04.)
- **Kuroami:** Jūzō's aged genin, under five shaku, past fifty, a boy's face;
  near-silent, flatly loyal (「左様か」). Posing as Kyoto shopkeeper Iseya Kahei.
- **Kisaru (木さる/木猿):** a LEAD in ch04. The crowd-illusion virtuoso (playful,
  imperious, cheeky); then the fierce ninja-daughter interrogator; then broken open
  — her body betrays "the child in her," Jūzō's face rises as she is taken, and she
  "parts from Iga for good." Ends half-believing she loves Gohei, tempted by the
  thousand-koku wife she might become, still secretly holding Jūzō. Cool formal
  お前様・こなた in the interrogation; her father's daughter under the maiden.
- **Kohagi (小萩):** Imai Sōkyū's adopted daughter, born a princess of a fallen
  house; now his agent and Jūzō's contact and paymaster. Cool, unbreakable poise; a
  smoky half-smile; sees through Jūzō. Polite ます/でございます. (Offstage in ch04.)
- **Imai Sōkyū (今井宗久):** the White Hōin. Frail, tiny, urbane old arms-merchant;
  cold irony over a war-profiteer's pride and a merchant's hatred of the low-born
  Kampaku. Cultivated, faintly archaic speech (じゃ, くるる). (Offstage in ch04.)
- **Iten Gyōzan (仰山), ch04:** the monk-abbot of the ruined Chinnō-in; old,
  riddling, self-mocking, unkillable in argument. Buries himself in the bamboo "to
  become the bamboo"; reads Gohei as a rappa on sight. Craggy wry じゃ/わい/おる. A
  one-chapter chorus who names the theme (shadow arts turned to selfish gain leave
  an "evil cast" on the face). May reappear (a woman passes him at ch04's close).

## Where the story stands (end of ch04)
Two threads now run in parallel. THREAD A (Jūzō, ch01-03): hired to kill Hideyoshi,
paid by Imai Sōkyū of Sakai, with Kohagi as his contact; he has reached the capital,
aching for Kohagi. THREAD B (ch04): his fellow disciple Gohei has DESERTED Iga for
the new order — he serves Maeda Gen'i, magistrate of Kyoto, as a spy-hunter, and has
just turned his own betrothed Kisaru into his creature and learned that Jūzō is in
the capital. The two men, and the two women, are set on a collision course. The
chapter ends with an unidentified woman slipping past Gyōzan in the dark — not
Kisaru. ch05 「羅刹谷」 (Rakshasa Valley) turns to a hidden valley south of
Higashiyama.

## Next batch
B05 = ch05 「羅刹谷」 / Rakshasa Valley, PDF/printed 149-166 (18 pages), offset 0.
ch05's body begins AFTER the 羅刹谷 title on folio 149; the top of 149 is ch04's tail
(already placed) — do NOT re-translate it. Then B06 = ch06 「忍び文字」 / The Ninja
Cipher, 167-206.

## Open traps / environment
- Furigana leakage clusters on chapter-opener pages; body pages OCR cleanly.
- Offset stays 0 through folio 302; do not assume it later (see the survey note).
- A chapter's tail can spill onto the next opener folio — render it and verify; make
  sure the next batch does not re-translate the spillover.
- OMP_THREAD_LIMIT=1 for tesseract; verify pgrep -c tesseract is 0 after OCR.
- Do not write CJK into JSON via a shell heredoc; use apparatus_merge.py or the
  Write/Edit tool, then re-read to verify.
- Numerals inside place-names (四条/三条/六波羅) are the NAME, not a count; noise them
  (done for these three). Real quantities always carried in the English.
- Pre-existing checker-regression FAIL (`hook stands down on template stub`) is
  unrelated to this book; leave it for a template-tooling session.
