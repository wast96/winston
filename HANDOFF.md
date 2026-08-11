# HANDOFF — The Owl's Castle (梟の城, Shiba Ryōtarō)

One batch = one conversation. This file is how a fresh session with no memory
picks up. The paste-ready kickoff is first; everything below it is context.

## Message to paste into the next chat

```
Owl's Castle B03

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json, then STYLE.md (note the "calibrated at the ch01 voice gate" subsection: plain over arcane diction, people-as-agents not body-part calques, keep the author's own tense in gnomic/establishing description, gloss technical terms). We are translating Owl's Castle (梟の城, Shiba Ryōtarō) from an image-only scan (source.pdf) into an annotated English EPUB, per CLAUDE.md. Work ONLY on branch claude/owls-castle; expect the harness to start you on a stray branch and consolidate per rule 2 (fast-forward/cherry-pick any commits onto claude/owls-castle, push it, delete the stray). Deliverable out/owls-castle.epub. Vertical, right-to-left Japanese with furigana; the offset is 0 in this range (printed folio == PDF render page).

Do Batch B03 = ch03 「白い法印」 (The White Hōin), PDF pages 90-123 (printed folios 90-123), end to end per the CLAUDE.md pipeline. ch01 is the FROZEN register reference: run scripts/check_register.py --ref out/ch01_reading.md on ch03 and fix any drift.

Environment / pipeline (the batch engineering is already done and committed; do NOT re-patch or revert the scripts):
1. ./setup.sh, THEN apt-get install -y tesseract-ocr-jpn tesseract-ocr-jpn-vert (setup.sh omits the Japanese packs). epubcheck is at /tmp/epubcheck-5.1.0/epubcheck.jar (re-fetch per setup.sh if the container was recycled).
2. OCR: render.py 90 123 --dpi 300; then ocr_crop.py 90 123 --left 0.035 --right 0.965 --top 0.075 --bottom 0.955 --lang jpn_vert --psm 5 --no-furniture-strip; ocr_dual.py 90 123 for the second read. Verify pgrep -c tesseract is 0 afterward (OMP_THREAD_LIMIT=1; kill the process GROUP if a run stalls).
3. find_figures.py 90 123 AND eyeball every page for line art (ch01-ch02 were text-only; if ch03 is too, record an empty figure list as a deliberate decision).

Translate:
4. IMPORTANT: the automated assemble.py welds paragraphs on vertical Japanese (the OCR mangles the sentence-final punctuation can_break() relies on). Translate by READING the rendered page images directly (data/png/p00NN.png), and build data/zh/ch03.txt as a hand-corrected, paragraph-aligned transcription read off the scan. That file IS the parity surface and the crop-verification record; force-add it (data/zh/ is gitignored). BEFORE translating, read the final two pages of ch02's English (the tail of out/ch02_reading.md) so the voice carries; the story resumes where ch02 stopped (Jūzō riding at dawn for Imai Sōkyū's mansion in Sakai).
5. Consult glossary.json and STYLE.md BEFORE romanizing any name (Hepburn with macrons; conventional forms for Hideyoshi/Nobunaga/Kyoto/Tokugawa). The principal cast and the major historical names/places are decided in glossary.json; reuse them unchanged and record in PROGRESS which rows you reused. Add new names with a status; flag any new principal with principal:true. NOTE: apparatus_merge.py writes glossary rows to the FILE ROOT, but glossary.json is SECTIONED (people/places/terms) — after merging, move each new row into its section (a one-off script preserving bytes, no CJK retyped) and re-run check_content/qc_entities. Crop-verify every proper name, number, unit designation and low-confidence span against the page image / furigana. NEVER invent bridging text: if OCR cuts off mid-sentence or a leaf is damaged, crop the scan and read the actual continuation; verify the unit's FINAL paragraphs against the scan explicitly before shipping.
6. Write out/ch03_reading.md, '## The White Hōin' as the h1 (settle the English title at translation; 法印 Hōin is a high Buddhist priestly rank), one paragraph per source paragraph. Add a ch03 entry to data/checks.json (docs + sources). make_bilingual.py ch03 (parity FIRST). Then run: verify_unit.py ch03 (it auto-uses data/noise.txt); check_structure.py --pairs data/zh/ch03.txt out/ch03_reading.md; check_align.py ch03; qc_entities.py out/ch03_bilingual.md glossary.json; check_content.py --config data/checks.json --glossary glossary.json; check_register.py --ref out/ch01_reading.md.
7. Footnotes per the CLAUDE.md reader model (a Westerner with no Japanese history). Recurring subjects already noted in ch01-ch02 are NOT re-noted (grep notes.json first; cross-reference instead): Iga/Kōga, Tenshō/Eiroku dating, the Iga Rebellion, Honnō-ji, Mount Hiei, Hideyoshi, the Sakai tea-masters/Rikyū, the Nara Great Buddha (Tōdai-ji, ruined by Matsunaga 1567), the zodiac double-hours, Aizen Myō-ō, the wakō/bahan ships and Luzon, and the measures shaku/chō/koku/ri/ken, rappa/shinobi, jizamurai/gōshi. Note only ch03's NEW first-appearances. Anchor notes to BODY phrases (verbatim substrings), not heading-only text — the builder matches body prose and refuses a heading-only anchor. Add via apparatus_merge.py (never a heredoc); check_apparatus.py clean.
8. Rebuild the cumulative EPUB (build_reading_epub.py); qa_epub.py until green; epubcheck. Record every check result in PROGRESS.md (the per-batch "NOT re-noted" list, the register result, and the renderings reused/added).

Deliver end to end; do not pause for approval mid-batch. At the end, in the SAME chat reply: attach the built out/owls-castle.epub AND paste the B04 kickoff (ch04 「木さると五平」 Kisaru and Gohei, PDF/printed 124-148) verbatim in a fenced block. Cite printed folios, never PDF page numbers, in the notes.
```

## Done so far
- **Survey:** 19-section structure recovered into book.json; metadata set; skeleton
  EPUB built; page furniture measured (top-only; crop L0.035 R0.965 T0.075 B0.955;
  model jpn_vert psm5); offset 0 for folios 7-302 and 425-660, drifts +2 across
  ~338-397 (B09-B13 must build data/pagemap by reading folios there).
- **B01 = ch01 おとぎ峠 / Otogi Pass (folios 7-63): COMPLETE, approved at the voice
  gate.** ch01 is the FROZEN register reference. (After B02 it is 523 source
  paragraphs, 17 notes: the dropped final two paragraphs and one zodiac-hour note
  were restored/added in B02, see below.)
- **B02 = ch02 濡れ大仏 / The Rain-Soaked Buddha (folios 64-89): COMPLETE.** 276
  source paragraphs, ~5.3k words, 6 new notes. All checks green (numbers 0, parity
  276|276, qc_entities/check_content/check_apparatus clean, register within
  tolerance, qa_epub PASS, epubcheck 0/0/0/0). Kisaru and Kohagi introduced;
  Matsukura Kurando killed, Kumobei conscripted.

## Two ch01 corrections made in B02 (do NOT undo)
1. ch01's dropped final two paragraphs restored (the Iseya Kahei shop instruction
   to Kuroami + the "idle talk of the world" narration, folio 64 top). ch01 parity
   is now 523 | 523.
2. ch01's Great Buddha note was factually wrong (it said Hideyoshi's Hōkō-ji in
   Kyoto); corrected to the NARA Tōdai-ji Vairocana, roofless since Matsunaga
   burned it in 1567. Verified against scholarship.

## Tooling in place (do NOT revert)
- `ocr_crop.py`: kana added to the despace class; `--no-furniture-strip` skips the
  Chinese strip_folio/strip_runfoot (they delete short Japanese dialogue lines
  ending in 。 and only match Chinese 第X章). Furniture here is top-only, cropped.
- `ocr_dual.py`: Japanese second read (jpn_vert psm5 on grayscale + Otsu variant).
- `check_content.py` / `qc_entities.py`: skip non-dict glossary sections; subsume a
  shorter glossary key covered by a longer matched key at the same span.
- `data/checks.json`: the {docs, sources} config. Add each new unit (ch01, ch02 in).
- `data/noise.txt`: check_numbers noise. B02 added proper-noun numerals
  (二月堂, 手向山八幡, 三好三人衆/三好/三人衆, 千手堂). Extend per its header,
  longest literal first; never noise a real quantity.
- **apparatus_merge glossary gotcha:** it flattens glossary rows to the file ROOT,
  but glossary.json is sectioned. After merging, move rows into people/places/terms
  (one-off byte-preserving script) and re-check. Notes/figures merge fine as-is.
- **Note anchors:** must be verbatim substrings of the BODY prose; the builder
  refuses a heading-only anchor (it searches body paragraphs). Anchor title-style
  notes to a body phrase near the first mention.

## Method note (every batch)
`assemble.py` is unreliable on this vertical-Japanese OCR (welds paragraphs). The
working method: translate by reading the rendered page images directly, and
hand-build `data/zh/chNN.txt` as a corrected, paragraph-aligned transcription (the
parity surface and crop-verification record). Force-add it (data/zh is gitignored).

## Renderings settled in glossary.json (reuse unchanged; consult before romanizing)
Principal cast (principal:true): Tsuzura Jūzō (葛籠重蔵), Kazama Gohei (風間五平),
Shimotsuge Jirōzaemon (下柘植次郎左衛門), Kisaru (木猿), Kuroami (黒阿弥).
B02 people added: Matsunaga Hisahide, Matsukura Kurando, Kumobei, Kakesu-no-Jirō,
Kohagi, Takeda Katsuyori, Iseya Kahei, the Miyoshi Triumvirate. Places added:
Tōdai-ji, Nigatsu-dō, Aburazaka, Tobuhino, Kai, Mikawa, Suruga, Luzon, the
Aizen-dō, the Tamon-in. Terms added: Aizen Myō-ō, Vairocana, bahan ship. Earlier
historical/place/term rows (Nobunaga, Hideyoshi, Ieyasu, Sōkyū, Rikyū, Iga, Kōga,
Sakai, rappa, Tenshō, tōyaku, etc.) are all in glossary.json.

## Voice sheets (consult at every dialogue scene)
- **Tsuzura Jūzō:** mid-30s, thick-shouldered, tall for a ninja; terse, guarded.
  Runs on a raw hunger for revenge under a monk-like idleness; a coiled force.
  Plain samurai forms (わし). In B02: dry, teasing, darkly bawdy with Kisaru and
  Kohagi; kills coldly for the work and calls it not inhuman but the Iga way.
- **Shimotsuge Jirōzaemon:** the disfigured old master; gruff, archaic, teasing,
  wry (あはは), secretly tender toward Jūzō. Creed: be as earth, stone, wind; hold
  no human heart. Old dialect (〜じゃ, 〜のう), われ for "you".
- **Kazama Gohei:** beautiful, androgynous, cool, clerkly killer; nihilist in a
  colder key than Jūzō; wants the pleasures of the human world. Polite ます/です to
  his master, distrustful. Offstage in B02; a lead again in ch04.
- **Kuroami:** Jūzō's aged genin, under five shaku, past fifty, a boy's face;
  near-silent, flatly loyal (「左様か」). Now posing as Kyoto shopkeeper Iseya Kahei.
- **Kisaru:** Jirōzaemon's fierce daughter, Gohei's betrothed. Onstage in B02:
  playful, physically fearless, provoking; hates Gohei yet goes to find him at her
  father's order; still a maiden. A coiled equal to Jūzō, not a victim. Lead in ch04.
- **Kohagi (B02):** Nara courtesan / Sōkyū's guide-agent, a likely Kōga operative.
  Two registers: a heavy near-mute plainness as the bought woman, a quick amused
  sharpness once the mask drops. May kill Jūzō "some day"; he spares her.
- **Kumobei (B02):** young ex-wakō sailor, coward, cringing (ござる、畏れ入る);
  Jūzō's conscripted thread into the capital.

## Where the story stands (end of ch02)
Nine years after Iga was destroyed and with Hideyoshi ruling Japan, Jūzō has taken
the commission to assassinate him, paid by the Sakai merchant Imai Sōkyū. In ch02
he crosses to Nara, keeps the Hour-of-the-Ox rendezvous at the ruined Nara Great
Buddha, finds his handlers compromised (a leak, a dead man), kills the loose-
tongued Matsukura, conscripts Kumobei, and rides for Sōkyū's mansion in Sakai at
dawn. Kisaru has gone to the capital to find Gohei. ch03 「白い法印」 (The White
Hōin) follows.

## Next batch
B03 = ch03 「白い法印」 / The White Hōin, PDF/printed 90-123 (34 pages), offset 0.
Then B04 = ch04 「木さると五平」 / Kisaru and Gohei, 124-148.

## Open traps / environment
- Furigana leakage clusters on chapter-opener pages; body pages OCR cleanly.
- Offset stays 0 through folio 302; do not assume it later (see the survey note).
- Section English titles beyond ch01 are provisional; settle each at translation.
  ch03 = "The White Hōin" (法印 = a high Buddhist priestly rank; footnote it).
- OMP_THREAD_LIMIT=1 for tesseract; verify pgrep -c tesseract is 0 after OCR.
- Do not write CJK into JSON via a shell heredoc; use apparatus_merge.py or the
  Write tool, then re-read to verify.
- Pre-existing checker-regression FAIL (`hook stands down on template stub`) is
  unrelated to this book; leave it for a template-tooling session.
