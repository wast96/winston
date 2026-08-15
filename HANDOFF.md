# HANDOFF, Burn, O Sword! (燃えよ剣), Shiba Ryōtarō

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery: every
batch ends with this file's kickoff block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count. Rewrite it at
the end of every batch; always keep the paste-ready kickoff below as its first
section.

## Message to paste into the next chat

```
Burn, O Sword! B11

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then STYLE.md, then book.json. We are translating Burn, O Sword! (燃えよ剣) by Shiba Ryōtarō from a Japanese digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/burn-o-sword; expect the harness to open you on a stray per-task branch and consolidate per CLAUDE.md rule 2. Deliverable out/burn-o-sword.epub.

Batches 1 to 10 are DONE (ch01 to ch48). ch01 is the FROZEN register reference: reference/ch01_ref.md. Run ./setup.sh; if data/src/ is empty re-run scripts/ingest_epub.py source.epub (Japanese-aware: strips furigana, substitutes 8 gaiji, writes reference/furigana_readings.tsv). No source-note stream. Keep the source's own cover (data/figs/embed0009_HD.jpg), reused byte-identical, exactly as book.json already sets it; the commissioner likes it, do not change it. The known failing test "hook stands down on template stub" is EXPECTED (it only passes on the template placeholder kickoff); every other test passes.

Do Batch 11 = ch49 through ch53 (江戸へ / To Edo; 北征 / The Northern March; 甲州進撃 / Advance into Kōshū; 勝沼の戦い / The Battle of Katsunuma; 流山屯集 / Mustering at Nagareyama), end to end per the CLAUDE.md pipeline, RUN TO COMPLETION. This span carries the RETREAT TO EDO and the CORPS'S UNDOING: after Toba-Fushimi the Shinsengumi sail east on the Fujiyama-maru; the corps is refitted and sent west again as the KŌYŌ CHINBUTAI (甲陽鎮撫隊) to hold Kōshū (Kai province) and Kōfu Castle; they are BEATEN at KATSUNUMA (勝沼) on Keiō 4/3/6 (late March 1868) by the new-government advance; and the remnant musters at NAGAREYAMA (流山) in Shimōsa, where KONDŌ ISAMI is surrounded and gives himself up to the Imperial forces (the parting of Kondō and Toshizō). Fact-check: the Kōyō Chinbutai's formation and Kōfu-Castle objective; the Battle of Katsunuma date and outcome; Kondō's surrender at Nagareyama (early April 1868); Okita's removal to Edo and worsening consumption; any dates/rosters. Oyuki continues in the background (she is the invented heroine, flagged at ch32 — handle as fiction, no fact-check of her existence); as of ch48 she is Toshizō's acknowledged "wife," last with him at the Saishō-an retreat above Osaka. Do not stop mid-batch except for a genuine blocker or completion. For each chapter:
1. Build data/zh/<id>.txt from data/src with scripts/build_zh.py <id> <srcbase> "<title>" (title line "### <title>" then one body line per non-empty source paragraph, skipping the first two header lines). ch49=53_part0051, ch50=54_part0052, ch51=55_part0053, ch52=56_part0054, ch53=57_part0055. Fix any extractor splits (this source has had none: a narration line ending in 、 before a 「quote」 is the source's own lead-in, handled by the {j} join, NOT a split to merge). Recover scene breaks: the RELIABLE method is to grep the XHTML (data/src_epub/OEBPS/Text/partNNNN.xhtml) for runs of TWO OR MORE consecutive <p><br/></p> in the body and read the text on either side of each run — scripts/scene_map.py reports the same runs by "body paragraph N" but its N has drifted off-by-one against later chapters, so PLACE *** BY TEXT BOUNDARY, not by the reported index (the single pair right after the chapter title is only the title/body separator; a SINGLE <br/> is a paragraph break, not a scene break). Place *** in the reading at those points. (B10 had one internal *** each in ch46, ch47, ch48; none in ch44, ch45.)
2. Translate to the FROZEN ch01 register. Names Japanese order, surname first, macrons; CONSULT reference/furigana_readings.tsv before romanizing ANY name or word (it has caught readings whole-book, e.g. B08's 花昌町→Kashō-chō, B09's 野津鎮雄→Shizuo, and B10's 家隆塚→Karyū-zuka [the tomb, vs the poet 家隆→Ietaka] and 聞多→Monta). The source uses EXPRESSIVE gikun furigana (e.g. 将軍→たいじゅ, 京→ここ, 近藤→せんせい, 慶喜→うえさま) which are semantic, NOT phonetic, and must not be romanized. Consult glossary.json (301 rows; then authority.json) first, feeding decided renderings back. Use the {j} display-join marker so a quotation reads inline with its lead-in and attribution; verse lines take {p} (one per line). Keep an exchange one paragraph per speaker turn. Watch parity: every 「…」 quote line, every と…いった attribution line, and every 「………」/「───」 silence is its OWN source paragraph and needs its OWN reading line — earlier batches each dropped/merged/INVENTED a line at dialogue or narration seams; make_bilingual's count catches it, a positional re-read fixes it. ALWAYS re-check dense exchanges and run-on narration for count. OBEY STYLE.md (em-dash budget; no scene-primed idioms). Consult the voice sheets below; read the last two pages of ch48's English before starting ch49 (batch seam).
3. Author out/<id>_reading.md (## title, {j}, {p}, ***, blank-separated). Then the battery: bash scripts/check_chapter.sh <id> <srcbase> "<title_en>" runs reading_to_en + make_bilingual (parity refuses on mismatch) + verify_unit (--noise data/noise.txt) + gen_check_config + check_align + check_content + qc_entities + check_apparatus + check_register. Verify each chapter TAIL against the source explicitly (rule 4).
4. Footnotes per the reader model (first-appearance discipline; keep the "NOT re-noted" ledger in PROGRESS.md; note MORE than the glossary row) via apparatus_merge.py (each glossary row MUST carry a "section": people|places|organizations|terms field AND a "pinyin" field — qc_entities crashes on a row without "pinyin"; set pinyin = the romanized en. The merge nests the section and check_apparatus stays clean; render the glossary's DECIDED form verbatim, e.g. 御香宮→"Gokō-no-miya", 林権助→"Hayashi Gonsuke", 佐川官兵衛→"Sagawa Kanbei", 伝習隊→"the Denshūtai", 御陵衛士→"the Goryō-eji", or qc_entities/check_content flag it; when the source shortens a name give the glossary a bare-surname en, and do NOT key a name that appears in FRAGILE COMPOUNDS — a Kyoto/Fushimi/Osaka street like 三条通/京町通/谷町筋 is rendered by hand, NOT keyed, or it false-flags). A NOTE ANCHOR must be a verbatim substring of the reading file with LITERAL macrons (ō, not sh&#333;gi) AND WITHOUT embedded straight quotes/apostrophes (pick a clean run of words — an English possessive like "Magistrate's" or a "…"-wrapped phrase will not anchor cleanly; Gen'ichirō-style apostrophes also break an anchor). Note BODIES use literal Unicode but numeric character references for any &-entity. Any figure from data/figs/ with a translated caption and real alt text (ch24-48 had none).
5. check_register.py --ref reference/ch01_ref.md out/<id>_reading.md; record in PROGRESS.md. If a chapter flags STILTED, add contractions to the INFORMAL speakers (Toshizō's blunt dialect, Kondō's intimate Bushū) ONLY — leave deliberately formal registers (a ceremonial official, quoted documents/memoir, a set-piece political analysis, Oyuki's refined samurai-widow speech) alone. Battle/narration chapters run em-dash LOW and dialogue-light (B10 ran 5.2–15.1/1k; ch48, a formal intimate two-hander, flagged STILTED and was left as characterization after contracting only Toshizō's casual lines — that call is documented in PROGRESS). Keep the source's ── interruptions and legitimate matched pairs, convert discretionary dash-asides to commas/parentheses (Shiba's own （）glosses and his 、-set appositives → commas/parentheses; a dialogue chapter can spike the em-dash rate if you dash every appositive, so watch it). Fact-check historical claims against real scholarship (never LLM-sourced; IGNORE Grok/Grokipedia), verdict in the note. Add numeral-noise rules to data/noise.txt as new numbered names/idioms/place-names appear (comment each; never noise a real quantity; use spelled forms the checker parses — but write LARGE composite tallies as DIGITS, e.g. "16,400", because the checker does NOT compose "sixteen thousand four hundred" into one value; write 3-digit tallies "one hundred and fifty" NOT "a hundred and fifty"; a romanized place/name whose kanji carries a numeral, e.g. 半四郎/八丁畷/又三郎, needs a noise rule because the digit vanishes; a Western year in kanji/full-width form, e.g. 千八百六十/一八六〇, needs noise because the checker cannot compose it, and the English carries the digits; 何百/何百日-type vague "hundreds" are noised idioms; block-numbers 丁目 rendered "the Nth block" DO carry the numeral and PASS).
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck (java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/burn-o-sword.epub); record ALL check results and EVERY digitization glitch in PROGRESS.md; update HANDOFF.md; commit and push to claude/burn-o-sword.

End the batch with BOTH chat deliverables (CLAUDE.md rule 1, enforced by the Stop hook): the built EPUB ATTACHED in the chat AND the Batch 12 kickoff PASTED VERBATIM in a fenced code block. Batch 12 = ch54 through ch58.

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
- B10 = ch44 to ch48, COMPLETE. ch44 鳥羽伏見の戦い・その三 / "(III)" (Toshizō on
  the wall-top; the sword-charge into the Shizuki-an grove; the Aizu matchlocks
  outmatched by Satsuma Minié rifles; HAYASHI GONSUKE shot three times, directing
  seated; the flank march behind the Gokō-no-miya with SAGAWA KANBEI; the
  magistrate's office burns, the fight becomes a slaughter), ch45 その四 / "(IV)"
  (the "theatre" conceit; Ernest Satow; the Sekigahara parallel; Nagakura vs a
  fleeing "soldier"; the brocade banner, the Tōdō defection, the great collapse;
  the deaths of Sakuma and Kubota; back to Osaka), ch46 大坂の歳三 / "Toshizō at
  Osaka" (the rout; the visit to the wounded Kondō and dying Okita; Oyuki's plum
  branches; MATSUMOTO RYŌJUN tells him YOSHINOBU HAS FLED; the reconstructed
  flight via a US warship to the Kaiyō-maru; Fukuchi Gen'ichirō's memoir),
  ch47 松林 / "The Pine Wood" (the Kondō–Toshizō Ashikaga-Takauji "war of ideas"
  debate; Matsudaira Tarō and the Dutch drill-manual; sailing set for the 12th on
  the Fujiyama-maru; the Oyuki reunion in the pine wood; two days' leave),
  ch48 西昭庵 / "Saishō-an" (the Yūhigaoka retreat; Fujiwara no Ietaka's tomb; the
  two nights with Oyuki; "danna-sama"). Notes 311 to 339 (29 this batch). All
  checks green; qa_epub PASS (339/339/339); epubcheck 0/0/0/0. Continuous note
  number now 339. Glossary 301 rows. 48 of 71 chapters translated. See PROGRESS.md
  B10 for the full record: the noise additions, the two entity-fixes (代官 in
  ch46, お雪 in ch48), and the fact-check verdicts (brocade banner date/effect,
  Yoshinobu's flight, Hayashi Gonsuke's death, Sagawa Kanbei, Sakuma/Kubota,
  Ernest Satow, Fujiwara no Ietaka).

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
  index has drifted off-by-one on later chapters. RELIABLE method: grep the XHTML
  for the <br/> runs and place *** by the TEXT on either side. Needs data/src_epub
  (re-run ingest if empty).
- scripts/reading_to_en.py, check_chapter.sh, apparatus_merge.py, build_zh.py,
  build_reading_epub.py, qa_epub.py — unchanged since B02-B04.
- scripts/qc_entities.py (B03 PATCH): SKIPS single-kanji glossary keys. DO NOT
  REVERT. NOTE: it requires every glossary row to have a "pinyin" field — a row
  added without it raises KeyError. Set pinyin = the romanized en on every new row.
- scripts/check_numbers.py PATCHES (target-side only, can only ADD a number):
  B04 reads "a/one hundred and <ten..nineteen>" (110-119); B07 folds ONES into
  the hundred+low band so "one hundred and two" = 百二 maps. Regression tests
  pass. DO NOT REVERT. Known limits (B09/B10): the checker does NOT compose
  "sixteen thousand four hundred" into 16400, nor a kanji/full-width year like
  千八百六十/一八六〇 into 1860 (write DIGITS, noise the source form); "tenfold"
  is not read as 10 (write "ten times"); a 余 BETWEEN numerals (七十余万) splits
  the run and orphans the tail unit (noise the compound, carry the value in
  words) — but 余 before a COUNTER (二十余名) is fine; vague "hundreds" (何百,
  何百日) are noised idioms; block-numbers 丁目 rendered "the Nth block" carry
  and pass.
- data/noise.txt (B01 to B10): Japanese name/idiom/place numeral rules, each
  commented. Never noise a real quantity. B10 added (all commented): 半四郎,
  八丁畷 (ch44); 三成, 又三郎, 零時 (ch45); [ch46 needed none]; 千八百六十, 一八六〇
  (ch47); 何百 (ch48).
- STYLE.md (B01): the house style sheet (em-dash budget; scene-primed idioms).
  READ IT each batch; add to it when the commissioner corrects a line. No new
  rule in B10.
- reference/ch01_ref.md (B01): the FROZEN register reference. Do not edit.

## Voice sheets (one per major character; consult at every dialogue scene)

- NARRATOR: third person, wry and knowing, fond of the aside and the forward
  glance to events years ahead (B10 flashes forward to Sagawa Kanbei's death in
  the 1877 Seinan War, to Matsudaira Tarō and Enomoto at Hakodate, and to a
  101-year-old Osaka woman who witnessed the Yodo boats of wounded). KEEPS Shiba's
  own modern parentheticals (Western dates; present-day place-names such as the
  Osaka Prefectural Office and Keihan Tenma station in ch47; quoted real
  memoirs — Ernest Satow's diary and Fukuchi Gen'ichirō's account in ch45/ch46)
  AND his bracketed editorial glosses INSIDE dialogue and quotes (（南北線）,
  （松平正質・幕軍総督）, （武揚）, etc.). KEEP them all — render as parentheses
  (preferred), commas, or square-bracket glosses in quoted documents; do NOT dash
  every one (that spikes the em-dash rate).
- HIJIKATA TOSHIZŌ ("Toshi"): the hero, now 34 (states it himself, ch48). Rough
  Bushū farm dialect off guard, contracted and blunt (おらァ, ねえ, 面白え); a cool
  tactician who reads the new warfare fast (delights in the Dutch infantry manual,
  ch47; means to re-arm the corps Western-style). SOLE FIELD COMMANDER of the
  Shinsengumi. His creed (ch40): fidelity/節義 alone; the sword a thing of single
  purpose. After Yoshinobu's flight (ch46) his loyalty turns personal and defiant:
  "Let Yoshinobu flee, let Katamori flee — Hijikata Toshizō will fight on." With
  OYUKI he is another man: earnest, boyish, halting, "more talkative than was his
  wont" (ch47-48); he takes two days' leave for her, longs to be called
  "danna-sama." OYUKI is his acknowledged WIFE ("we two are husband and wife,"
  ch48). Sword: 和泉守兼定 (Izumi-no-kami Kanesada, 二尺八寸) + wakizashi 堀川国広.
- KONDŌ ISAMI: warm, plain, big-jawed Bushū farmer's son; weeps easily; calls
  Toshizō "Toshi". SHOT in the right shoulder at Sumizome (ch41), healing at Osaka
  (a month, he's told, ch46). His politics are a muddle but he has caught the
  "war of ideas" (ch47): the brocade banner has made the Tokugawa side rebels, and
  to fight on is to become "a second Ashikaga Takauji"; he is fatalistic, quoting
  six-hundred-year-old precedent. A kite in a fair wind, weak in decline. Sword:
  the Kotetsu. WATCH B11: history has him surrender at Nagareyama.
- OKITA SŌJI: the finest blade; bright, glib, teasing, cool. CONSUMPTION grave —
  bedridden at Osaka, wasted, no flesh on his arm, ashamed of it (ch46). Still the
  clear frightening smile. Arranged Oyuki's plum branch by his pillow. WATCH B11:
  removed to Edo; his decline deepens.
- OYUKI (お雪, given name Yuki, self-refers as 雪 "Yuki"): the HEROINE, WHOLLY
  INVENTED (Shiba's afterword; flagged at ch32). Edo-born samurai widow, a painter
  (art-name Kōka) of the Shijō-Maruyama school; paints only hydrangeas. Register:
  quiet, few wasted words, quick-witted, CRISP Edo/samurai speech, refined and
  formal (でございます), NO Kyoto softness — she COMMANDS rather than coaxes; leave
  her low-contraction speech ALONE at register gates (it is characterization). Now
  Toshizō's acknowledged WIFE. In B10 she came to Osaka, tended Okita and Kondō,
  reunited with Toshizō in the pine wood, and spent two nights with him at the
  Saishō-an on Yūhigaoka. GLOSSARY KEY is お雪 → "Oyuki"; render お雪 as "Oyuki"
  (not "her"/"Yuki") or qc_entities flags it; bare 雪 in her self-reference is
  "Yuki". Handle as fiction, no fact-check of her existence.
- SAITŌ HAJIME: captain of the Third Unit; Toshizō's SPY planted inside the
  Goryō-eji (from ch37). Resurfaced at Toba-Fushimi (ch44, among the surviving
  captains). Terse; watch for his role in the eastern campaign.
- NAGAKURA SHINPACHI: Matsumae-han deserter, Edo-bred; captain of the Second Unit,
  now a full hatamoto of the Ōgobangumi after the corps' 1867 elevation (ch45).
  Bold, capable; stood in as corps commander at Osaka; wept with joy at Toshizō's
  news of Oyuki (ch47). Steady, at peace with death.
- HARADA SANOSUKE: hot-blooded Iyo spearman, captain of the Tenth Unit; simple,
  animal-loyal to Kondō; a belly-scar from an old botched suicide. Fought his
  spear to splinters at Fushimi (ch44); wept, tender, at Toshizō's happiness
  (ch47). Has a wife somewhere he has lost track of in the war.
- MATSUMOTO RYŌJUN (松本良順): the Tokugawa house physician, ~37-38, bold and
  bluff, "a taste for war"; tends Kondō and Okita at Osaka; it is he who breaks
  the news of Yoshinobu's flight to Toshizō (ch46). Historically Pompe's pupil,
  later the first army surgeon-general. Established/noted (ch28, ch42).
- SAGAWA KANBEI (佐川官兵衛): NEW glossary key in B10 (ch44). Aizu senior retainer,
  38, six hundred koku, "the Aizu ogre"; captain of the Bessentai (Special-
  Selection corps); Toshizō's field-partner at Fushimi (the flank march). Right
  eye taken by a shell-splinter, fought on. FACT: survived to fight the Aizu War,
  then died a Meiji policeman against the Satsuma rebels in 1877. Noted ch44/45.
- HAYASHI GONSUKE: DEAD. The 63-year-old Aizu artillery commander (ch43), shot
  three times at Fushimi and directing seated in the road (ch44), died of the
  wounds during the battle. His son Hayashi Matasaburō was killed in the same
  fighting (ch45). Noted ch45. Do not write him as a living voice.
- ITŌ KASHITARŌ, SERIZAWA, NIIMI, KIYOKAWA, YAMANAMI, SHICHIRI: DEAD.
- FORESHADOWED for later batches (rendered by hand, not yet major): MATSUDAIRA
  TARŌ (Western-minded shogunal officer, future vice-president of the Ezo
  republic at Hakodate; ch46-47), ENOMOTO TAKEAKI / 榎本和泉守武揚 (Dutch-trained
  navy commander of the Kaiyō-maru, future leader of the northern resistance;
  ch46), ŌTORI KEISUKE (leads the Denshūtai north; enters at ch55).

## Renderings settled / carry-forward

- Title "Burn, O Sword!"; author Shiba Ryōtarō. Names Japanese order, macrons.
- ONE rendering per referent, all in glossary.json (301 rows). RENDER THE DECIDED
  FORM VERBATIM: 旗本 "hatamoto", 御陵衛士 "the Goryō-eji", 見廻組 "the
  Mimawarigumi", 和泉守兼定 "Izumi-no-kami Kanesada", 御香宮 "Gokō-no-miya",
  林権助 "Hayashi Gonsuke", 王政復古 "the Restoration of Imperial Rule". B10 new
  keys: 佐川官兵衛 "Sagawa Kanbei" (person), 伝習隊 "the Denshūtai" (organization).
  お雪 "Oyuki" (bare 雪 = "Yuki").
- RENDERED INLINE, NOT KEYED (appear in built chapters / fragile compounds):
  慶喜 "Yoshinobu" (徳川慶喜 "Tokugawa Yoshinobu"), 家康 "Ieyasu", 秀吉 "Hideyoshi",
  大坂 "Osaka", 会津中将松平容保 "Matsudaira Katamori"/"the Aizu Lieutenant-General",
  松平越中守 "Matsudaira Echū-no-kami" (Sadaaki, Kuwana), 大山弥助 "Ōyama Yasuke"
  (= Ōyama Iwao). Osaka/Kyoto/Fushimi STREETS by hand: 京町通 "Kyōmachi-dōri",
  両替町通 "Ryōgaemachi-dōri", 新町通 "Shinmachi-dōri", 谷町筋 "Tanimachi-suji",
  下寺町 "Shimotera-machi". B10 one-off historical figures rendered by hand (not
  keyed): Ernest Satow, Fukuchi Gen'ichirō (Ōchi), Matsudaira Tarō, Enomoto
  Takeaki, Inoue Monta (later Kaoru), Asano Mimasaka-no-kami Ujihiro, Itakura
  Iga-no-kami, Sakuma Ōmi-no-kami Nobuhisa, Kubota Bizen-no-kami Shizuaki, Shirai
  Gorōdayū, Matsuzawa Suiemon, Miyata Hanshirō, Nomura Rihachi, Hayashi
  Matasaburō, Sagawa's Bessentai, Ashikaga Takauji, Kusunoki Masashige, Tokugawa
  Mitsukuni, Fujiwara no Ietaka (tomb 家隆塚 "Karyū-zuka"). Place/thing by hand:
  指月庵の森 "the Shizuki-an grove", 夕陽ケ丘 "Yūhigaoka", 富士山丸
  "the Fujiyama-maru", 開陽丸 "the Kaiyō-maru", 歩兵心得 "the Infantry Handbook".
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
- ch29-ch33 (B07): YAMANAMI'S SEPPUKU; Itō made staff officer; the Osae betrayal;
  OYUKI enters; the Satchō alliance; Itō turns to 討幕.
- ch34-ch38 (B08): the ITŌ SPLIT; the Goryō-eji formed; Toshizō kills Shichiri;
  Saitō planted as a spy; Oyuki becomes his lover; the TAISEI HŌKAN.
- ch39-ch43 (B09): the ABURANOKŌJI killing of Itō; Kondō's collapse and the ŌSEI
  FUKKO; the corps sent to hold Fushimi; Kondō SHOT, command to Toshizō; and the
  OPENING OF THE BOSHIN WAR (Nozu's first shot, Keiō 4/1/3 = 27 Jan 1868).
- ch44-ch48 (B10): the REST OF TOBA-FUSHIMI and the GREAT COLLAPSE — Toshizō's
  sword-charges, Hayashi Gonsuke's death, the BROCADE BANNER and the Tōdō
  defection, the rout to Osaka; then YOSHINOBU'S FLIGHT by warship (learned from
  Matsumoto Ryōjun); the corps ordered to sail east on the Fujiyama-maru; and the
  two nights with OYUKI at the Saishō-an before the retreat.

## What is NEXT

- B11 = ch49 to ch53 (kickoff above): 江戸へ / 北征 / 甲州進撃 / 勝沼の戦い /
  流山屯集. The retreat to Edo and the corps's undoing: refit as the KŌYŌ
  CHINBUTAI, the march on Kōfu, the DEFEAT AT KATSUNUMA, and KONDŌ'S SURRENDER at
  Nagareyama. Then B12 ch54-58, B13 ch59-63, B14 ch64-68, B15 ch69-71 back matter
  + whole-book reconciliation + COMPLETION.

## Open items for the read-through (B11)

- KŌYŌ CHINBUTAI (甲陽鎮撫隊): fact-check the corps's re-formation and its Kōfu-
  Castle objective (Kai province), and the race with the new-government column for
  Kōfu.
- BATTLE OF KATSUNUMA (勝沼): fact-check the date (Keiō 4/3/6 = late March 1868)
  and the rout of the Kōyō Chinbutai.
- KONDŌ AT NAGAREYAMA: fact-check his surrender to the Imperial forces at
  Nagareyama in Shimōsa (early April 1868) and the parting from Toshizō (his
  execution at Itabashi likely falls in a later chapter — read the source before
  assuming where it lands).
- OKITA: his removal to Edo and the worsening consumption (he was left at Osaka in
  B10; watch how the source brings him east).
- OYUKI recurs in the background — keep her crisp, refined Edo/samurai register;
  she is Toshizō's acknowledged wife as of ch48. Handle as fiction.

## Environment / traps state

- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches).
- data/src/ and data/src_epub/ are gitignored (regenerate via ingest if empty);
  scene-break detection needs data/src_epub, so re-run ingest before it if empty.
- SCENE BREAKS: place *** BY TEXT BOUNDARY (grep XHTML for 2+ <p><br/></p> runs);
  scene_map.py's index drifts. Single <br/> = paragraph break; the pair after the
  title = title/body separator. (B10: internal *** in ch46/ch47/ch48; none in
  ch44/ch45.)
- PARITY trap (PROVEN B04-B10): every quote, attribution (と…いった), and silence
  (「………」/「───」) is its own paragraph; a narration lead-in ending in 、 before a
  quote is its own line too (join it for display with {j} on the FOLLOWING line).
  Never add or drop a beat the source does not have; make_bilingual refuses on a
  count mismatch, a positional re-read fixes it. Re-check dense exchanges AND
  run-on narration.
- NUMBER-CHECK traps (B09/B10 lessons): DIGITS for large composite tallies
  ("16,400") and for kanji/full-width years (noise 千八百六十/一八六〇, English
  "1860"); "ten times" not "tenfold" (十倍); "one hundred and fifty" not "a
  hundred and fifty"; a 余 BETWEEN numerals orphans the unit (noise the compound,
  carry the value in words) but 余 before a COUNTER (二十余名) is fine; a
  romanized name/place whose kanji carries a numeral needs a commented noise rule
  (B10: 半四郎, 八丁畷, 三成, 又三郎); midnight 零時 and vague "hundreds" 何百 are
  noised; four-char idioms with digits need noise; block-numbers 丁目 rendered
  "the Nth block" carry and pass. Real koku/troop/date/age/measure figures stay in
  word-form and DO carry the number.
- CONTENT/ENTITY trap: render the glossary's DECIDED form verbatim or it flags.
  Do NOT key a name in a FRAGILE COMPOUND. NEW glossary rows MUST carry both a
  "section" and a "pinyin" field (qc_entities KeyErrors on a row without pinyin).
  B10 caught two: 代官 "intendant" dropped once in ch46; お雪 rendered "her"/"Yuki"
  twice in ch48 (the key is お雪 → "Oyuki").
- GLOSSARY CASCADE: adding a global key re-checks EVERY built chapter. Before
  adding, grep data/zh for the key; if an old chapter rendered it differently,
  match the old form OR edit the old chapter + re-derive + rebuild. B10's 2 new
  keys (佐川官兵衛, 伝習隊) were both new to the book — no cascade.
- REGISTER: battle/narration chapters run em-dash LOW and dialogue-light (noisy
  contraction stats are expected). A DIALOGUE-heavy formal chapter can flag
  STILTED (ch48 did): contract the INFORMAL speakers only (Toshizō's dialect,
  Kondō's intimate Bushū); leave formal registers alone (Oyuki, ceremonial
  officials, quoted memoir). Also watch the em-dash ceiling: dashing every
  appositive spikes the rate (ch47 hit 17.0 before conversion to commas).
- NOTE-ANCHOR trap: the anchor must be a verbatim substring of the reading with
  LITERAL macrons and WITHOUT embedded straight quotes/apostrophes — an English
  possessive ("Magistrate's"), a "…"-wrapped phrase, or an apostrophe name
  (Gen'ichirō) will NOT anchor; pick a clean run of words. Note bodies use literal
  Unicode but numeric refs for any &-entity.
- Known failing test, EXPECTED: tests/run_tests.py reports "hook stands down on
  template stub" FAIL (template-only). Not a translation gate. All other tests
  pass.
- All work is on branch claude/burn-o-sword.
