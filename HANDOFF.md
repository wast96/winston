# HANDOFF — The Owl's Castle (梟の城, Shiba Ryōtarō)

One batch = one conversation. This file is how a fresh session with no memory
picks up. The paste-ready kickoff is first; everything below it is context.

## Message to paste into the next chat

```
Owl's Castle B04

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json, then STYLE.md (note the "calibrated at the ch01 voice gate" subsection: plain over arcane diction, people-as-agents not body-part calques, keep the author's own tense in gnomic/establishing description, gloss technical terms). We are translating Owl's Castle (梟の城, Shiba Ryōtarō) from an image-only scan (source.pdf) into an annotated English EPUB, per CLAUDE.md. Work ONLY on branch claude/owls-castle; expect the harness to start you on a stray branch and consolidate per rule 2 (fast-forward/cherry-pick any commits onto claude/owls-castle, push it, delete the stray). Deliverable out/owls-castle.epub. Vertical, right-to-left Japanese with furigana; the offset is 0 in this range (printed folio == PDF render page).

Do Batch B04 = ch04 「木さると五平」 (Kisaru and Gohei), PDF pages 124-148 (printed folios 124-148), end to end per the CLAUDE.md pipeline. ch01 is the FROZEN register reference: run scripts/check_register.py --ref out/ch01_reading.md out/ch04_reading.md on ch04 and fix any drift.

Environment / pipeline (the batch engineering is already done and committed; do NOT re-patch or revert the scripts):
1. ./setup.sh, THEN apt-get install -y tesseract-ocr-jpn tesseract-ocr-jpn-vert (setup.sh omits the Japanese packs). epubcheck is at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup.sh if the container was recycled).
2. OCR: render.py 124 148 --dpi 300; then ocr_crop.py 124 148 --left 0.035 --right 0.965 --top 0.075 --bottom 0.955 --lang jpn_vert --psm 5 --no-furniture-strip; ocr_dual.py 124 148 for the second read. Verify pgrep -c tesseract is 0 afterward (OMP_THREAD_LIMIT=1; kill the process GROUP if a run stalls).
3. find_figures.py 124 148 AND eyeball every page for line art (ch01-ch03 were text-only; if ch04 is too, record an empty figure list as a deliberate decision).

Translate:
4. IMPORTANT: the automated assemble.py welds paragraphs on vertical Japanese (the OCR mangles the sentence-final punctuation can_break() relies on). Translate by READING the rendered page images directly (data/png/p0NNNN.png), and build data/zh/ch04.txt as a hand-corrected, paragraph-aligned transcription read off the scan. That file IS the parity surface and the crop-verification record; force-add it (data/zh/ is gitignored). NOTE ON THE OPENER: ch03's final sentence runs off folio 123 and completes on the FIRST line of folio 124 ("…小萩の肉体への思慕がうずいているのを覚えた。") — that line is ALREADY in ch03 and is NOT part of ch04; ch04's body begins after the 「木さると五平」 title on folio 124 ("四条の河原に集まっていた一かたまりの頭が…"). BEFORE translating, read the final two pages of ch03's English (the tail of out/ch03_reading.md) so the voice carries; the story shifts to Kyoto (the Shijō riverbank) and to Kisaru and Gohei.
5. Consult glossary.json and STYLE.md BEFORE romanizing any name (Hepburn with macrons; conventional forms for Hideyoshi/Nobunaga/Kyoto/Tokugawa). The principal cast and the major historical names/places are decided in glossary.json; reuse them unchanged and record in PROGRESS which rows you reused. Kisaru (木猿, also written 木さる) and Kazama Gohei (風間五平) are principals already in the glossary — reuse those forms. Add new names with a status; flag any new principal with principal:true. NOTE: apparatus_merge.py writes glossary rows to the FILE ROOT, but glossary.json is SECTIONED (people/places/terms) — after merging, move each new row into its section (a one-off script preserving bytes, no CJK retyped) and re-run check_content/qc_entities. Crop-verify every proper name, number, unit designation and low-confidence span against the page image / furigana. NEVER invent bridging text: if OCR cuts off mid-sentence or a leaf is damaged, crop the scan and read the actual continuation; verify the unit's FINAL paragraphs against the scan explicitly before shipping.
6. Write out/ch04_reading.md, '## Kisaru and Gohei' as the h1 (settle the English title at translation), one paragraph per source paragraph. Add a ch04 entry to data/checks.json (docs + sources). make_bilingual.py ch04 (parity FIRST). Then run: verify_unit.py ch04 (it auto-uses data/noise.txt); check_structure.py --pairs data/zh/ch04.txt out/ch04_reading.md; check_align.py ch04; qc_entities.py out/ch04_bilingual.md glossary.json; check_content.py --config data/checks.json --glossary glossary.json; check_register.py --ref out/ch01_reading.md out/ch04_reading.md.
7. Footnotes per the CLAUDE.md reader model (a Westerner with no Japanese history). Recurring subjects already noted in ch01-ch03 are NOT re-noted (grep notes.json first; cross-reference instead): Iga/Kōga, Tenshō/Eiroku dating, the Iga Rebellion, Honnō-ji, Mount Hiei, Hideyoshi/Nobunaga/Ieyasu, the Sakai tea-masters/Rikyū/Sōgyū/Sōkyū, the Hōin/Hōgen ranks and Kampaku office, Sakai the free-city, the meibutsu tea cult and Matsushima caddy, Tenka Fubu, Sekigahara, the Korea invasion, Tsurumatsu/Hidetsugu, Nanban, the Nara Great Buddha (Tōdai-ji), the zodiac double-hours, Aizen Myō-ō, the wakō/bahan ships and Luzon, and the measures shaku/chō/koku/ri/ken/kin, rappa/shinobi, jizamurai/gōshi. Note only ch04's NEW first-appearances (Kyoto geography — Shijō, the Kamo river, Nyoigatake/Daimonji, etc. — is likely). Anchor notes to BODY phrases (verbatim substrings), not heading-only text — the builder matches body prose and refuses a heading-only anchor. Add via apparatus_merge.py (never a heredoc); check_apparatus.py clean.
8. Rebuild the cumulative EPUB (build_reading_epub.py); qa_epub.py until green; epubcheck. Record every check result in PROGRESS.md (the per-batch "NOT re-noted" list, the register result, and the renderings reused/added).

Deliver end to end; do not pause for approval mid-batch. At the end, in the SAME chat reply: attach the built out/owls-castle.epub AND paste the B05 kickoff (ch05 「羅刹谷」 Rakshasa Valley, PDF/printed 149-166) verbatim in a fenced block. Cite printed folios, never PDF page numbers, in the notes.
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
  paragraphs, ~6.3k words, 16 new notes. All checks green (numbers 0, parity
  385|385, qc_entities/check_content/check_apparatus clean, register within
  tolerance, qa_epub PASS, epubcheck 0/0/0/0). Sōkyū's biography and the
  tea-room confrontation; the commission's motive (Hideyoshi's Korea war) drawn
  out; Kohagi revealed as Sōkyū's adopted daughter and made Jūzō's contact.

## ch01 corrections made earlier (do NOT undo)
1. ch01's dropped final two paragraphs restored in B02 (Iseya Kahei shop
   instruction + "idle talk of the world"); ch01 parity is 523 | 523.
2. ch01's Great Buddha note corrected in B02 to the NARA Tōdai-ji Vairocana
   (roofless since Matsunaga burned it 1567), not Hideyoshi's Hōkō-ji. NOTE: in
   B03, Hideyoshi's OWN Great Buddha (方広寺大仏, the Kyoto Hōkō-ji, begun 1586)
   appears and is footnoted as DISTINCT from the Nara one. Keep the two straight.

## Tooling in place (do NOT revert)
- `ocr_crop.py`: kana in the despace class; `--no-furniture-strip` skips the
  Chinese strip_folio/strip_runfoot. Furniture here is top-only, cropped.
- `ocr_dual.py`: Japanese second read (jpn_vert psm5 on grayscale + Otsu variant).
- `check_content.py` / `qc_entities.py`: skip non-dict glossary sections; subsume a
  shorter glossary key covered by a longer matched key at the same span.
- `data/checks.json`: the {docs, sources} config. ch01, ch02, ch03 in.
- `data/noise.txt`: check_numbers noise. B03 added 惣五郎, 千利休, 九州, 三宅, 巨万,
  五体, 四肢, and the koku amounts 二千二百 / 千二百 (see PROGRESS for why). Extend
  per its header, longest literal first; never noise a real quantity you dropped.
- **apparatus_merge glossary gotcha:** it flattens glossary rows to the file ROOT,
  but glossary.json is sectioned. After merging, move rows into people/places/terms
  (one-off byte-preserving script) and re-check. Notes/figures merge fine as-is.
- **Note anchors:** must be verbatim substrings of the BODY prose; the builder
  refuses a heading-only anchor. Anchor title-style notes to a body phrase near
  the first mention.

## Method note (every batch)
`assemble.py` is unreliable on this vertical-Japanese OCR (welds paragraphs). The
working method: translate by reading the rendered page images directly, and
hand-build `data/zh/chNN.txt` as a corrected, paragraph-aligned transcription (the
parity surface and crop-verification record). Force-add it (data/zh is gitignored).
**A chapter's last sentence can run onto the next chapter's opener folio** (ch03's
did — onto folio 124, above the ch04 title); always render the next folio's top to
recover the true tail before shipping (rule 4).

## Renderings settled in glossary.json (reuse unchanged; consult before romanizing)
Principal cast (principal:true): Tsuzura Jūzō (葛籠重蔵), Kazama Gohei (風間五平),
Shimotsuge Jirōzaemon (下柘植次郎左衛門), Kisaru (木猿), Kuroami (黒阿弥).
B03 people added: Imai Sōkun / Sōkun, Sōgorō, Aida Gen'emon (Jūzō's Sakai alias),
Takeno Jōō, Naya Sōji, Imai Nobutsune, Dewa-no-kami Muneyoshi, Ashikaga Yoshiaki,
Tōkichirō, Azai Nagamasa, Konishi Ryūsa, Konishi Yukinaga / Yukinaga, Tsurumatsu,
Hidetsugu, Sen no Rikyū (= 千宗易). B03 places added: Ōsaka, Akutagawa, Ibaraki,
Odani Castle, Yamazaki, the Daitoku-ji, Sekigahara, Shiwaku, Shōdoshima, Kyūshū,
Kawachi, Echigo, Izumi, Abiko, the Jōraku-ji, the Myōkoku-ji, Byakugō-ji. B03
terms added: Hōin, Hōgen, Ōkurakyō, the Kampaku, the Matsushima, Tenka Fubu,
Nanban, kin, Settsu-no-kami, the Kita-no-mandokoro. Earlier rows (Nobunaga,
Hideyoshi, Ieyasu, Sōkyū, Sōgyū, Iga, Kōga, Sakai, Nara, rappa, Tenshō, tōyaku,
the measures, etc.) are all in glossary.json.

## Voice sheets (consult at every dialogue scene)
- **Tsuzura Jūzō:** mid-30s, thick-shouldered, tall for a ninja; terse, guarded.
  Runs on a raw hunger for revenge under a monk-like idleness; a coiled force.
  Plain samurai forms (わし). Dry, darkly bawdy with Kisaru/Kohagi; kills coldly
  for the work and calls it the Iga way. In B03: self-aware of one weakness — "By
  nature I am weak where the wanting of a woman is concerned" — and drawn to
  Kohagi against his creed; needles Sōkyū to draw out the plot.
- **Kazama Gohei:** beautiful, androgynous, cool, clerkly killer; nihilist in a
  colder key than Jūzō; wants the pleasures of the human world. Polite ます/です to
  his master, distrustful. A lead again in ch04 (Kyoto).
- **Shimotsuge Jirōzaemon:** the disfigured old master; gruff, archaic, teasing,
  wry (あはは), secretly tender toward Jūzō. Creed: be as earth, stone, wind; hold
  no human heart. Old dialect (〜じゃ, 〜のう), われ for "you".
- **Kuroami:** Jūzō's aged genin, under five shaku, past fifty, a boy's face;
  near-silent, flatly loyal (「左様か」). Posing as Kyoto shopkeeper Iseya Kahei.
- **Kisaru (木さる/木猿):** Jirōzaemon's fierce daughter, Gohei's betrothed.
  Playful, physically fearless, provoking; hates Gohei yet went to find him at her
  father's order; still a maiden. A coiled equal to Jūzō, not a victim. A lead in
  ch04 (opens on the Shijō riverbank in Kyoto).
- **Kohagi (小萩):** revealed in B03 as Imai Sōkyū's ADOPTED DAUGHTER, born a
  princess of a fallen noble house; now his agent and Jūzō's appointed contact and
  paymaster. Cool, unbreakable poise; a smoky half-smile that never gives way;
  sees through Jūzō and needles him. Polite ます/でございます. Likely a Kōga-trained
  operative who may kill Jūzō "some day."
- **Imai Sōkyū (今井宗久):** the White Hōin. Frail, tiny old man, large childlike
  face, heavy-lidded, urbane; cold irony over a war-profiteer's pride (believes he
  MADE Nobunaga and Hideyoshi) and a merchant's hatred of the low-born Kampaku.
  Cultivated, faintly archaic speech (じゃ, くるる, 拝し奉る); one 小心 streak.
- **Sōgorō (惣五郎, B03):** the Sakai loafer; coarse, cocky townsman-swagger, weak
  head for drink; a one-scene comic guide.

## Where the story stands (end of ch03)
Nine years after Iga fell, with Hideyoshi ruling, Jūzō has taken the commission to
assassinate him, paid by the Sakai arms-merchant Imai Sōkyū. In ch03 Jūzō reaches
Sakai, breaks into Sōkyū's mansion, and in the tea-room draws out the motive:
Hideyoshi's planned invasion of Korea will strangle Sōkyū's China trade. Sōkyū
appoints his adopted daughter Kohagi as Jūzō's contact and paymaster; Jūzō leaves
for the capital, aching for Kohagi against his own creed. ch04 「木さると五平」
(Kisaru and Gohei) shifts to Kyoto and the other pair.

## Next batch
B04 = ch04 「木さると五平」 / Kisaru and Gohei, PDF/printed 124-148 (25 pages),
offset 0. Then B05 = ch05 「羅刹谷」 / Rakshasa Valley, 149-166.

## Open traps / environment
- Furigana leakage clusters on chapter-opener pages; body pages OCR cleanly.
- Offset stays 0 through folio 302; do not assume it later (see the survey note).
- A chapter's tail can spill onto the next opener folio — render it and verify.
- OMP_THREAD_LIMIT=1 for tesseract; verify pgrep -c tesseract is 0 after OCR.
- Do not write CJK into JSON via a shell heredoc; use apparatus_merge.py or the
  Write tool, then re-read to verify.
- Pre-existing checker-regression FAIL (`hook stands down on template stub`) is
  unrelated to this book; leave it for a template-tooling session.
