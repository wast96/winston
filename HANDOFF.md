# HANDOFF, Burn, O Sword! (燃えよ剣), Shiba Ryōtarō

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery: every
batch ends with this file's kickoff block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count. Rewrite it at
the end of every batch; always keep the paste-ready kickoff below as its first
section.

## Message to paste into the next chat

```
Burn, O Sword! B12

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then STYLE.md, then book.json. We are translating Burn, O Sword! (燃えよ剣) by Shiba Ryōtarō from a Japanese digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/burn-o-sword; expect the harness to open you on a stray per-task branch and consolidate per CLAUDE.md rule 2. Deliverable out/burn-o-sword.epub.

Batches 1 to 11 are DONE (ch01 to ch53). ch01 is the FROZEN register reference: reference/ch01_ref.md. Run ./setup.sh; if data/src/ is empty re-run scripts/ingest_epub.py source.epub (Japanese-aware: strips furigana, substitutes 8 gaiji, writes reference/furigana_readings.tsv). No source-note stream. Keep the source's own cover (data/figs/embed0009_HD.jpg), reused byte-identical, exactly as book.json already sets it; the commissioner likes it, do not change it. The known failing test "hook stands down on template stub" is EXPECTED (it only passes on the template placeholder kickoff); every other test passes.

Do Batch 12 = ch54 through ch58 (袂別 / The Parting; 大鳥圭介 / Ōtori Keisuke; 城攻め / The Siege; 沖田総司 / Okita Sōji; 陸軍奉行並 / Assistant Commissioner of the Army), end to end per the CLAUDE.md pipeline, RUN TO COMPLETION. This span carries KONDŌ'S SURRENDER AND THE START OF THE NORTHERN WAR: at Nagareyama the Imperial column closes on the camp and KONDŌ ISAMI gives himself up (still under the alias Ōkubo Yamato) to spare his men — the FINAL PARTING of Kondō and Toshizō (ch54 袂別); Kondō is taken to the new-government camp and, once identified, executed at ITABASHI (Keiō 4/4/25 = 17 May 1868 — read the source before assuming which chapter his death lands in). Toshizō escapes north and throws in with ŌTORI KEISUKE, who is leading the DENSHŪTAI and other shogunal remnants up through the Kantō (ch55); the northern fighting opens with an assault on a CASTLE (ch56 城攻め — most likely UTSUNOMIYA). OKITA SŌJI dies of consumption at the Sendagaya nurseryman's (ch57 沖田総司; historically Keiō 4/5/30 = 19 July 1868). Toshizō is made 陸軍奉行並, ASSISTANT COMMISSIONER OF THE ARMY, in the northern shogunal-resistance command (ch58). Fact-check: Kondō's surrender at Nagareyama and his execution at Itabashi (date, place, the beheading vs seppuku point); Ōtori Keisuke and the Denshūtai's northern march; the Battle of Utsunomiya Castle (Keiō 4/4, taken then lost); Okita Sōji's death at Sendagaya (date, and that he never learned of Kondō's execution); the office 陸軍奉行並 and how Toshizō came by it; any dates/rosters. Oyuki is in the background (invented heroine, flagged ch32 — handle as fiction, no fact-check of her existence); as of ch48 she is Toshizō's acknowledged "wife," last at the Saishō-an above Osaka, and painting the sunset she watched with him. NAGAKURA and HARADA parted from Kondō at the Ōkubo mansion in ch53 to raise a new corps with Haga Yoshimichi — do not write them back into Toshizō's column unless the source does. Do not stop mid-batch except for a genuine blocker or completion. For each chapter:
1. Build data/zh/<id>.txt from data/src with scripts/build_zh.py <id> <srcbase> "<title>" (title line "### <title>" then one body line per non-empty source paragraph, skipping the first two header lines). ch54=58_part0056, ch55=59_part0057, ch56=60_part0058, ch57=61_part0059, ch58=62_part0060. Fix any extractor splits (this source has had none: a narration line ending in 、 before a 「quote」 is the source's own lead-in, handled by the {j} join, NOT a split to merge). Recover scene breaks: the RELIABLE method is to grep the XHTML (data/src_epub/OEBPS/Text/partNNNN.xhtml) for runs of TWO OR MORE consecutive <p><br/></p> in the body and read the text on either side of each run — scripts/scene_map.py reports the same runs by "body paragraph N" but its N has drifted off-by-one, so PLACE *** BY TEXT BOUNDARY, not by the reported index (the single pair right after the chapter title is only the title/body separator; a SINGLE <br/> is a paragraph break, not a scene break). Place *** in the reading at those points. (B11 had one internal *** each in ch49, ch50, ch52; none in ch51, ch53.)
2. Translate to the FROZEN ch01 register. Names Japanese order, surname first, macrons; CONSULT reference/furigana_readings.tsv before romanizing ANY name or word (it has caught readings whole-book, e.g. B08's 花昌町→Kashō-chō, B10's 家隆塚→Karyū-zuka, and B11's 乾→Inui [板垣退助's old surname], 干城→Tateki [谷守部→谷干城], 籬蔭→Riin, 祐邦→Sukekuni). The source uses EXPRESSIVE gikun furigana (e.g. 将軍→たいじゅ, 京→ここ, 近藤→せんせい, 慶喜→うえさま) which are semantic, NOT phonetic, and must not be romanized. Consult glossary.json (302 rows; then authority.json) first, feeding decided renderings back. Use the {j} display-join marker so a quotation reads inline with its lead-in and attribution; verse lines take {p} (one per line). Keep an exchange one paragraph per speaker turn. Watch parity: every 「…」 quote line, every と…いった attribution line, and every 「………」/「───」 silence is its OWN source paragraph and needs its OWN reading line — earlier batches each dropped/merged/INVENTED a line at dialogue or narration seams; make_bilingual's count catches it, a positional re-read fixes it. ALWAYS re-check dense exchanges and run-on narration for count. OBEY STYLE.md (em-dash budget; no scene-primed idioms). Consult the voice sheets below; read the last two pages of ch53's English before starting ch54 (batch seam).
3. Author out/<id>_reading.md (## title, {j}, {p}, ***, blank-separated). Then the battery: bash scripts/check_chapter.sh <id> <srcbase> "<title_en>" runs reading_to_en + make_bilingual (parity refuses on mismatch) + verify_unit (--noise data/noise.txt) + gen_check_config + check_align + check_content + qc_entities + check_apparatus + check_register. Verify each chapter TAIL against the source explicitly (rule 4).
4. Footnotes per the reader model (first-appearance discipline; keep the "NOT re-noted" ledger in PROGRESS.md; note MORE than the glossary row) via apparatus_merge.py (each glossary row MUST carry a "section": people|places|organizations|terms field AND a "pinyin" field — qc_entities crashes on a row without "pinyin"; set pinyin = the romanized en. The merge nests the section and check_apparatus stays clean; render the glossary's DECIDED form verbatim, e.g. 甲陽鎮撫隊→"the Kōyō Chinbutai", 御陵衛士→"the Goryō-eji", 佐川官兵衛→"Sagawa Kanbei", 北添佶麿→"Kitazoe Yoshimaro", or qc_entities/check_content flag it; when the source shortens a name give the glossary a bare-surname en, and do NOT key a name that appears in FRAGILE COMPOUNDS — a Kyoto/Fushimi/Osaka street like 三条通/京町通/谷町筋 is rendered by hand, NOT keyed, or it false-flags). NOTE a check_content substring quirk (documented in PROGRESS B11): the source's own ALIAS 近藤勇平 contains the key 近藤勇 (Kondō Isami) as a substring, so check_content false-flags that one paragraph even though qc_entities (the battery gate) is clean — if a NEW alias-inside-a-key case appears, render faithfully and DOCUMENT the false-flag, do not distort the text. A NOTE ANCHOR must be a verbatim substring of the reading file with LITERAL macrons (ō, not sh&#333;gi) AND WITHOUT embedded straight quotes/apostrophes (pick a clean run of words — an English possessive like "Toshizō's" or a "…"-wrapped phrase will not anchor cleanly). Note BODIES use literal Unicode but numeric character references for any &-entity. Any figure from data/figs/ with a translated caption and real alt text (ch24-53 had none).
5. check_register.py --ref reference/ch01_ref.md out/<id>_reading.md; record in PROGRESS.md. If a chapter flags STILTED, add contractions to the INFORMAL speakers (Toshizō's blunt dialect, Kondō's intimate Bushū) ONLY — leave deliberately formal registers (a ceremonial official, quoted documents/memoir, a set-piece political analysis, Oyuki's refined samurai-widow speech) alone. Battle/narration chapters run em-dash LOW and dialogue-light (B11 ran 2–5 em dashes/file; none flagged STILTED). Keep the source's ── interruptions and legitimate matched pairs, convert discretionary dash-asides to commas/parentheses (Shiba's own （）glosses and his 、-set appositives → commas/parentheses). Fact-check historical claims against real scholarship (never LLM-sourced; IGNORE Grok/Grokipedia), verdict in the note. Add numeral-noise rules to data/noise.txt as new numbered names/idioms/place-names appear (comment each; never noise a real quantity; use spelled forms the checker parses — but write LARGE composite tallies as DIGITS, e.g. "16,400" and "1,600", because the checker does NOT compose them; a romanized place/name whose kanji carries a numeral, e.g. 千住/四谷/精一郎/尚三, needs a noise rule because the digit vanishes; a Western year in kanji/full-width form needs noise; 何百-type vague "hundreds" are noised idioms; block-numbers 丁目 rendered "the Nth block" DO carry the numeral and PASS). NUMBER-CHECK LESSON (B11): the checker needs an explicit "a"/"one" before "million"/"hundred thousand" ("a million koku", "one hundred thousand koku" PASS; "the million koku", "a hundred thousand koku" FAIL); "a score" and multi-word "one thousand six hundred" are NOT read (use "twenty", digits "1,600").
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck (java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/burn-o-sword.epub); record ALL check results and EVERY digitization glitch in PROGRESS.md; update HANDOFF.md; commit and push to claude/burn-o-sword.

End the batch with BOTH chat deliverables (CLAUDE.md rule 1, enforced by the Stop hook): the built EPUB ATTACHED in the chat AND the Batch 13 kickoff PASTED VERBATIM in a fenced code block. Batch 13 = ch59 through ch63.

Cite chapters and sections, never pages.
```

## What is DONE (do not redo)

- Step 0 (ingest + survey), committed. book.json: 68 novel chapters (ch01 to
  ch68) + 3 back-matter units.
- B01 = ch01 「女の夜市」 / "The Women's Night Market", COMPLETE and APPROVED at
  the voice gate. ch01 FROZEN as the register reference (reference/ch01_ref.md;
  em-dash baseline 12.7/1k, dialogue contractions 24.9/1k). Notes 1 to 15.
- B02 = ch02 to ch07, COMPLETE. Notes 16 to 55.
- B03 = ch08 to ch13, COMPLETE. Notes 56 to 100.
- B04 = ch14 to ch18, COMPLETE. Notes 101 to 143.
- B05 = ch19 to ch23, COMPLETE. Notes 144 to 180.
- B06 = ch24 to ch28, COMPLETE. Notes 181 to 208.
- B07 = ch29 to ch33, COMPLETE. Notes 209 to 234.
- B08 = ch34 to ch38, COMPLETE. Notes 235 to 272.
- B09 = ch39 to ch43, COMPLETE. Notes 273 to 310.
- B10 = ch44 to ch48, COMPLETE. Notes 311 to 339.
- B11 = ch49 to ch53, COMPLETE. ch49 江戸へ / "To Edo" (the last Saishō-an
  morning and parting from Oyuki; the Fujiyama-maru voyage east; the sea-burial
  of YAMAZAKI SUSUMU in the Kitan Strait; Okita wasting; landfall at Shinagawa),
  ch50 北征 / "The Northern March" (the KŌYŌ CHINBUTAI formed; SATŌ SURUGA-NO-KAMI
  and the Kōfu plan; DANZAEMON's men and money; the wakadoshiyori/yoriai ranks;
  the 500,000-koku promise; Okita moved to the Sendagaya nurseryman's), ch51
  甲州進撃 / "Advance into Kōshū" (Itagaki's Inui→Itagaki name-change and Shingen
  propaganda; the HINO HOMECOMING at Satō Hikogorō's, the horo, sister Onobu, the
  Kasuga-tai; the RACE FOR KŌFU LOST), ch52 勝沼の戦い / "The Battle of Katsunuma"
  (AMEMIYA KEIJIRŌ; the four-kin gun's first shot; the fight at KASHIO, Kondō
  left-handed; the KŌYŌ CHINBUTAI DISBANDED), ch53 流山屯集 / "Mustering at
  Nagareyama" (the split from HARADA and NAGAKURA; Toshizō's choice of AIZU via
  NAGAREYAMA; the parting-walk; the Meiji-9 memorial-stele digression, Yoshinobu
  weeping; the march to Matsudo). Notes 340 to 381 (42 this batch). All checks
  green except ONE documented false-flag (ch52 check_content substring quirk on
  the alias 近藤勇平; see PROGRESS B11 and rule 4 of the kickoff). qa_epub PASS
  (381/381/381); epubcheck 0/0/0/0. Continuous note number now 381. Glossary 302
  rows (1 new key: 甲陽鎮撫隊). 53 of 71 chapters translated. See PROGRESS.md B11
  for the full record: scene-break placements, the noise additions, the
  number-check lessons, and the fact-check verdicts.

## Tooling in place (do NOT revert)

- ingest_epub.py: Japanese-aware (furigana strip, 8 gaiji via
  data/gaiji_map.json, dumps reference/furigana_readings.tsv). From Step 0.
- data/gaiji_map.json: 遼 茨 頤 葛 芦, plus レ (kaeriten) and 㝎 (之定 variant).
- DISPLAY JOIN MARKER {j} (B01, whole-book): a reading line prefixed "{j} " is
  merged onto the preceding display paragraph at BUILD time. Chains. VERSE MARKER
  {p} (one per verse line, indented italic); also {v}/{d}/{g} for
  vignette/dateline/hourgloss. All are stripped by the parity/number/entity/
  content checks. reading_to_en.py counts BY LINE (one content line per source
  body line); {j}/{p}/*** lines and the ## title are handled/skipped.
- scripts/scene_map.py: reports 2+ <p><br/></p> runs, BUT its "body paragraph N"
  index has drifted off-by-one. RELIABLE method: grep the XHTML for the <br/>
  runs and place *** by the TEXT on either side. Needs data/src_epub (re-run
  ingest if empty).
- scripts/reading_to_en.py, check_chapter.sh, apparatus_merge.py, build_zh.py,
  build_reading_epub.py, qa_epub.py — unchanged since B02-B04.
- scripts/qc_entities.py (B03 PATCH): SKIPS single-kanji glossary keys. DO NOT
  REVERT. NOTE: it requires every glossary row to have a "pinyin" field — a row
  added without it raises KeyError. Set pinyin = the romanized en on every new row.
- scripts/check_content.py: matches glossary keys by SUBSTRING with no
  longest-match/exclusion logic, so a source alias that literally contains a key
  (B11: 近藤勇平 ⊃ 近藤勇) false-flags one paragraph. qc_entities (the battery
  gate) does NOT; document the false-flag, do not distort the translation.
- scripts/check_numbers.py PATCHES (target-side only, can only ADD a number):
  B04 reads "a/one hundred and <ten..nineteen>"; B07 folds ONES into the
  hundred+low band. Regression tests pass. DO NOT REVERT. Known limits: does NOT
  compose "sixteen thousand four hundred"/"one thousand six hundred" (write
  DIGITS), nor a kanji/full-width year (write DIGITS, noise the source form);
  needs an explicit "a"/"one" before "million"/"hundred thousand" (B11); "a
  score" is not read (write "twenty"); a 余 BETWEEN numerals orphans the tail
  unit (noise the compound) but 余 before a COUNTER is fine; vague "hundreds"
  (何百) are noised idioms; block-numbers 丁目 "the Nth block" carry and pass.
- data/noise.txt (B01 to B11): Japanese name/idiom/place numeral rules, each
  commented. Never noise a real quantity. B11 added (all commented): 利三郎
  (ch49); 千駄ケ谷 (ch50); 四谷, 精一郎 (ch51); 三品一郎, 千屋 (ch52); 尚三,
  千住 (ch53).
- STYLE.md (B01): the house style sheet (em-dash budget; scene-primed idioms).
  READ IT each batch; add to it when the commissioner corrects a line. No new
  rule in B11.
- reference/ch01_ref.md (B01): the FROZEN register reference. Do not edit.

## Voice sheets (one per major character; consult at every dialogue scene)

- NARRATOR: third person, wry and knowing, fond of the aside and the forward
  glance to events years ahead (B11 flashes forward to Amemiya Keijirō's Meiji
  business empire, to Itagaki Taisuke and Kataoka Kenkichi as future People's-
  Rights statesmen, and to the 1888 memorial stele where Yoshinobu weeps over
  Kondō's and Toshizō's names). KEEPS Shiba's own modern parentheticals (Western
  dates; present-day place-names such as "today's Hino city"; quoted real
  records — the Riin Shiwa memoir in ch51, the steward Oguri's letter in ch53)
  AND his bracketed editorial glosses INSIDE dialogue and quotes (（慶喜）,
  （千葉県）, （歳三の変名）, etc.). KEEP them all — render as parentheses
  (preferred), commas, or square-bracket glosses; do NOT dash every one.
- HIJIKATA TOSHIZŌ ("Toshi"): the hero, 34. Rough Bushū farm dialect off guard,
  contracted and blunt (おらァ, ねえ, かえ); a cool tactician who reads the new
  warfare fast (means to re-arm Western-style; delights in the Infantry
  Handbook). SOLE FIELD COMMANDER. After the Kōshū rout his creed hardens into
  pure fight-to-the-end (ch53): "I don't think about winning and losing any more.
  I just fight while there's life in me. The interesting part of my life has
  finally raised its curtain." He chooses AIZU-via-Nagareyama almost alone, and
  parts from Nagakura/Harada. ALIAS from ch53: 内藤隼人 "Naitō Hayato" / "Naitō-
  sensei" (carry it forward in the northern campaign). With OYUKI he is another
  man, earnest and boyish; she is his acknowledged WIFE (ch48), last at the
  Saishō-an painting the sunset. Sword: 和泉守兼定 (Izumi-no-kami Kanesada) +
  wakizashi 堀川国広.
- KONDŌ ISAMI: warm, plain, big-jawed Bushū farmer's son; weeps easily; calls
  Toshizō "Toshi". His right shoulder (shot at Sumizome, ch41) still pains him;
  drinks left-handed (ch51). Chased the dream of a Kōfu fief and a daimyō's rank,
  turned into a "warring-domains warrior" by the 500,000-koku promise (ch50); rode
  a daimyō palanquin to his Hino homecoming (ch51); BEATEN for the first time at
  Kōshū and badly downcast after (ch52-53). Marches under the alias 大久保大和
  "Ōkubo Yamato". WATCH B12: history has him SURRENDER at Nagareyama (ch54 袂別)
  and be executed at Itabashi (Keiō 4/4/25 = 17 May 1868). Sword: the Kotetsu.
- OKITA SŌJI: the finest blade; bright, glib, teasing, cool even dying. CONSUMPTION
  grave — could scarcely walk aboard ship (ch49), moved to the Sendagaya
  nurseryman's (植木屋平五郎方) to convalesce (ch50-51), never learned how the war
  went. Still the clear translucent smile. WATCH B12: ch57 沖田総司 is his DEATH
  (historically Keiō 4/5/30 = 19 July 1868, at Sendagaya).
- OYUKI (お雪, given name Yuki, self-refers as お雪→"Oyuki", bare 雪→"Yuki"): the
  HEROINE, WHOLLY INVENTED (Shiba's afterword; flagged at ch32). Edo-born samurai
  widow, a painter (art-name Kōka) of the Shijō-Maruyama school. Register: quiet,
  CRISP Edo/samurai speech, refined and formal (でございます), NO Kyoto softness;
  leave her low-contraction speech ALONE at register gates (characterization).
  Toshizō's acknowledged WIFE. In B11 (ch49) she saw him off from the Saishō-an,
  stayed on to paint the sunset they watched together, and receded into the
  background. GLOSSARY KEY is お雪 → "Oyuki"; render お雪 as "Oyuki" or qc_entities
  flags it. Handle as fiction, no fact-check of her existence.
- SAITŌ HAJIME: captain of the Third Unit; Toshizō's former SPY inside the
  Goryō-eji. REJOINED at the Igakusho and went to Nagareyama (ch53); insisted on
  raising the 誠 banner against Kondō's caution. Terse; a core man of the northern
  remnant. Watch his role in B12.
- NAGAKURA SHINPACHI & HARADA SANOSUKE: PARTED from Kondō at the Ōkubo mansion in
  Fukagawa (ch53) to raise a new corps with 芳賀宜通 (Haga Yoshimichi, a Shintō
  Munen-ryū master and old Matsumae friend of Nagakura's). They leave Toshizō's
  column here; do NOT write them back in unless the source does. Nagakura: bold,
  wide-acquainted, could no longer stomach Kondō's lordly airs. Harada: hot-
  blooded Iyo spearman, animal-loyal but cut to the quick by Kondō ("I've
  misjudged you"), rose to leave; a belly-scar from an old botched suicide.
- MATSUMOTO RYŌJUN (松本良順): the Tokugawa house physician; tended Kondō and Okita
  at the Igakusho. RENAMED 松本順 "Matsumoto Jun" after the Restoration (rose to
  army surgeon-general); it is he who does the calligraphy for the 1876/1888
  memorial stele (ch53). Same man; render the source's name for the period.
- ŌTORI KEISUKE: FORESHADOWED, enters ch55. Western-trained shogunal officer who
  leads the Denshūtai and other remnants north; Toshizō will join him. Render by
  hand until then.
- FORESHADOWED / rendered by hand, not yet major: ENOMOTO TAKEAKI / 榎本武揚
  (Dutch-trained navy commander of the Kaiyō-maru, future leader of the northern
  resistance; named in ch50/ch53 as a war-party ringleader Yoshinobu admonished),
  MATSUDAIRA TARŌ (army war-party, future vice-president of the Ezo republic;
  ch53), KATSU KAISHŪ and YAMAOKA TESSHŪ (the Edo-surrender negotiators; ch53).
- OKITA's Kyoto-era dead comrades, ITŌ KASHITARŌ, SERIZAWA, NIIMI, KIYOKAWA,
  YAMANAMI (敬助), TŌDŌ HEISUKE, INOUE GENZABURŌ, SHICHIRI, HAYASHI GONSUKE,
  YAMAZAKI SUSUMU (died ch49): DEAD. Do not write them as living voices.

## Renderings settled / carry-forward

- Title "Burn, O Sword!"; author Shiba Ryōtarō. Names Japanese order, macrons.
- ONE rendering per referent, all in glossary.json (302 rows). RENDER THE DECIDED
  FORM VERBATIM: 甲陽鎮撫隊 "the Kōyō Chinbutai" (B11 NEW org key), 旗本 "hatamoto",
  和泉守兼定 "Izumi-no-kami Kanesada", 佐川官兵衛 "Sagawa Kanbei", 伝習隊 "the
  Denshūtai", お雪 "Oyuki" (bare 雪 = "Yuki"), 山崎烝 "Yamazaki Susumu", 豊玉
  "Hōgyoku", 北添佶麿 "Kitazoe Yoshimaro", 望月亀弥太 "Mochizuki Kameyata",
  近藤勇 "Kondō Isami", 助勤 "jokin", 副長 "vice-commander", 監察 "inspector".
- ALIASES: 大久保大和 "Ōkubo Yamato" (Kondō, from ch51/52/53), 内藤隼人 /
  内藤先生 "Naitō Hayato"/"Naitō-sensei" (Toshizō, from ch53). Render as given.
- RENDERED INLINE, NOT KEYED (appear in built chapters / fragile compounds):
  慶喜 "Yoshinobu", 板垣退助/乾退助 "Itagaki Taisuke"/"Inui Taisuke", 武田信玄
  "Takeda Shingen", 松平容保 "Matsudaira Katamori". B11 one-off historical figures
  rendered by hand (not keyed): Yamauchi Yōdō (鯨海酔侯 "Geikai Suikō"), Iwakura
  Tomomi, Itagaki Suruga-no-kami Nobukata, Satō Hikogorō (glossary), Satō Jin,
  Gennosuke, Onobu, Inoue Taisuke, Hida Hamagorō, Torii Tango-no-kami, Ogata
  Shuntarō, Ōishi Kuwajirō, Shimada Kai, Sōma Kazue, Okita Rintarō, Omitsu,
  Nomura Risaburō, Kawazu Izu-no-kami Sukekuni, Hattori Chikuzen-no-kami, Satō
  Suruga-no-kami, Nakayama Seiichirō, Danzaemon, Amemiya Keijirō (+ ancestor
  Amemiya Yamashiro-no-kami Masashige), Tani Moribe (谷干城 Tateki), Kataoka
  Kenkichi, Ogasawara Kenkichi, Hase Shigeki, Kitamura Chōbei, Mishina Ichirō,
  Matsubara Shintarō, Sakuma Kensuke, Imamura Wasuke, Ōkubo Shuzen-no-kami, Haga
  Yoshimichi, Hayashi Shintarō, Maeno Gorō, Chūjō Tsunehachirō, Kasuya Ryōjun,
  Hijikata Hayato, Kondō Yūgorō, Ōtsuki Bankei, Matsumoto Jun, Oguri Shōzō,
  Matsumoto Sutesuke, Chūsuke, Kyūkichi. Place/thing by hand: 甲府城/舞鶴城 "Kōfu
  Castle (Maizuru Castle)", 勝沼 "Katsunuma", 柏尾 "Kashio", 笹子峠 "Sasago Pass",
  流山 "Nagareyama", 高幡不動 "Takahata Fudō", 千住大橋 "Senju Great Bridge",
  母衣 "horo", シャグマ "shaguma", 誠 "Makoto".
- Era-year form kept with the numeral ("Keiō 4", "the first year of Meiji").
  Shiba's own modern intrusions and bracketed glosses KEPT.
- COVER: keep data/figs/embed0009_HD.jpg byte-identical, as book.json sets it.
- Principal Characters page flags unchanged (Hijikata 1, Kondō 2, Okita 3, Inoue
  4, Nagakura 5, Shichiri 6, Harada 7, Katsura 8, Yamanami 9, Serizawa 10, Saitō
  Hajime 11, OYUKI 12).

## Where the book stands (story)

- ch01-ch07 (B01-B02): the Tama-country prologue; the core cast assembles.
- ch08-ch13 (B03): the dōjō ruined by epidemic; the Rōshigumi; Kyoto at Mibu.
- ch14-ch18 (B04): the founding; the name SHINSENGUMI (1863); the Serizawa purge.
- ch19-ch23 (B05): the CODE OF THE CORPS; the IKEDAYA INCIDENT (1864).
- ch24-ch28 (B06): the KINMON / HAMAGURI GATE INCIDENT; ITŌ recruited; YAMANAMI
  deserts.
- ch29-ch33 (B07): YAMANAMI'S SEPPUKU; Itō made staff officer; OYUKI enters; the
  Satchō alliance; Itō turns to 討幕.
- ch34-ch38 (B08): the ITŌ SPLIT; the Goryō-eji formed; Toshizō kills Shichiri;
  Saitō planted as a spy; Oyuki becomes his lover; the TAISEI HŌKAN.
- ch39-ch43 (B09): the ABURANOKŌJI killing of Itō; Kondō's collapse and the ŌSEI
  FUKKO; Kondō SHOT, command to Toshizō; the OPENING OF THE BOSHIN WAR.
- ch44-ch48 (B10): the REST OF TOBA-FUSHIMI and the GREAT COLLAPSE; YOSHINOBU'S
  FLIGHT by warship; the corps ordered east on the Fujiyama-maru; the two nights
  with OYUKI at the Saishō-an.
- ch49-ch53 (B11): the RETREAT TO EDO and the corps's UNDOING — the Fujiyama-maru
  voyage and Yamazaki's sea-burial; the refit as the KŌYŌ CHINBUTAI and the march
  on Kōfu; the HINO HOMECOMING; the DEFEAT AT KATSUNUMA and the corps DISBANDED;
  the split from Nagakura/Harada; Toshizō's resolve on AIZU and the MUSTERING at
  NAGAREYAMA under aliases (Ōkubo Yamato / Naitō Hayato).

## What is NEXT

- B12 = ch54 to ch58 (kickoff above): 袂別 / 大鳥圭介 / 城攻め / 沖田総司 /
  陸軍奉行並. KONDŌ'S SURRENDER at Nagareyama and the FINAL PARTING; his execution
  at Itabashi; Toshizō north with ŌTORI KEISUKE and the Denshūtai; the CASTLE
  ASSAULT (Utsunomiya); OKITA'S DEATH; Toshizō made Assistant Commissioner of the
  Army. Then B13 ch59-63, B14 ch64-68, B15 ch69-71 back matter + whole-book
  reconciliation + COMPLETION.

## Open items for the read-through (B12)

- KONDŌ AT NAGAREYAMA: fact-check the surrender to the Imperial column (early
  April 1868), the parting from Toshizō, and the execution at Itabashi (Keiō
  4/4/25 = 17 May 1868) — read the source before assuming which chapter the death
  lands in (the surrender is ch54 袂別; the execution may fall later).
- ŌTORI KEISUKE + the DENSHŪTAI: fact-check his leadership of the shogunal
  remnant north and the link-up with Toshizō (ch55).
- UTSUNOMIYA CASTLE: fact-check the assault/capture and loss (Keiō 4/4, ch56).
- OKITA SŌJI: his death at the Sendagaya nurseryman's (Keiō 4/5/30), and that he
  never learned of Kondō's fate (ch57).
- 陸軍奉行並 (Assistant Commissioner of the Army): fact-check the office and how
  Toshizō came by it in the northern command (ch58).
- OYUKI recurs only in the background now; keep her crisp Edo/samurai register.
  Handle as fiction.

## Environment / traps state

- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches).
- data/src/ and data/src_epub/ are gitignored (regenerate via ingest if empty);
  scene-break detection needs data/src_epub, so re-run ingest before it if empty.
- SCENE BREAKS: place *** BY TEXT BOUNDARY (grep XHTML for 2+ <p><br/></p> runs);
  scene_map.py's index drifts. Single <br/> = paragraph break; the pair after the
  title = title/body separator. (B11: internal *** in ch49/ch50/ch52; none in
  ch51/ch53.)
- PARITY trap (PROVEN B04-B11): every quote, attribution (と…いった), and silence
  (「………」/「───」) is its own paragraph; a narration lead-in ending in 、 before a
  quote is its own line too (join it for display with {j} on the FOLLOWING line).
  Never add or drop a beat the source does not have; make_bilingual refuses on a
  count mismatch, a positional re-read fixes it.
- NUMBER-CHECK traps: DIGITS for large composite tallies ("1,600", "16,400") and
  for kanji/full-width years; explicit "a"/"one" before "million"/"hundred
  thousand" (B11); "a score" not read (use "twenty"); a romanized name/place whose
  kanji carries a numeral needs a commented noise rule (B11: 利三郎, 千駄ケ谷, 四谷,
  精一郎, 三品一郎, 千屋, 尚三, 千住); vague "hundreds" 何百 are noised; block-
  numbers 丁目 "the Nth block" carry and pass. Real koku/troop/date figures stay
  in word-form and DO carry the number.
- CONTENT/ENTITY trap: render the glossary's DECIDED form verbatim or it flags.
  Do NOT key a name in a FRAGILE COMPOUND. NEW glossary rows MUST carry both a
  "section" and a "pinyin" field. check_content matches keys by SUBSTRING, so a
  source ALIAS that contains a key (B11: 近藤勇平 ⊃ 近藤勇) false-flags one
  paragraph — qc_entities does NOT; document it, do not distort the text.
- GLOSSARY CASCADE: adding a global key re-checks EVERY built chapter. Before
  adding, grep data/zh for the key; if an old chapter rendered it differently,
  match the old form OR edit + re-derive + rebuild. B11's 1 new key (甲陽鎮撫隊)
  was new to the book — no cascade.
- REGISTER: battle/parting chapters run em-dash LOW and dialogue-light. Contract
  the INFORMAL speakers only (Toshizō's dialect, Kondō's intimate Bushū); leave
  formal registers alone (quoted documents/memoir, ceremonial officials). B11 ran
  2-5 em dashes/file, none STILTED.
- NOTE-ANCHOR trap: the anchor must be a verbatim substring of the reading with
  LITERAL macrons and WITHOUT embedded straight quotes/apostrophes — an English
  possessive ("Toshizō's"), a "…"-wrapped phrase, or an apostrophe name will NOT
  anchor; pick a clean run of words. Note bodies use literal Unicode but numeric
  refs for any &-entity.
- Known failing test, EXPECTED: tests/run_tests.py reports "hook stands down on
  template stub" FAIL (template-only). Not a translation gate. All other tests
  pass.
- All work is on branch claude/burn-o-sword.
