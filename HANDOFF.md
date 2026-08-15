# HANDOFF, Burn, O Sword! (燃えよ剣), Shiba Ryōtarō

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery: every
batch ends with this file's kickoff block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count. Rewrite it at
the end of every batch; always keep the paste-ready kickoff below as its first
section.

## Message to paste into the next chat

```
Burn, O Sword! B13

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then STYLE.md, then book.json. We are translating Burn, O Sword! (燃えよ剣) by Shiba Ryōtarō from a Japanese digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/burn-o-sword; expect the harness to open you on a stray per-task branch and consolidate per CLAUDE.md rule 2. Deliverable out/burn-o-sword.epub.

Batches 1 to 12 are DONE (ch01 to ch58). ch01 is the FROZEN register reference: reference/ch01_ref.md. Run ./setup.sh; if data/src/ is empty re-run scripts/ingest_epub.py source.epub (Japanese-aware: strips furigana, substitutes 8 gaiji, writes reference/furigana_readings.tsv). No source-note stream. Keep the source's own cover (data/figs/embed0009_HD.jpg), reused byte-identical, exactly as book.json already sets it; the commissioner likes it, do not change it. The known failing test "hook stands down on template stub" is EXPECTED (it only passes on the template placeholder kickoff); every other test passes.

Do Batch 13 = ch59 through ch63 (艦隊北上 / The Fleet Turns North; 小姓市村鉄之助 / Ichimura Tetsunosuke, the Page; 松前城略取 / The Seizure of Matsumae Castle; 甲鉄艦 / The Ironclad; 宮古湾海戦 / The Sea Fight at Miyako Bay), end to end per the CLAUDE.md pipeline, RUN TO COMPLETION. This span carries THE SHIFT TO EZO AND THE SEA WAR. At the close of B12 Toshizō, now 陸軍奉行並 (rikugun-bugyō-nami, Assistant Commissioner of the Army), sailed north on the flagship 開陽丸 KAIYŌ-MARU with ENOMOTO TAKEAKI's fleet. B13: the fleet turns north to EZO (蝦夷地; renamed 北海道 Hokkaidō in 1869) and the shogunal remnant lands and drives on HAKODATE / GORYŌKAKU (ch59 艦隊北上); the page ICHIMURA TETSUNOSUKE 市村鉄之助 enters Toshizō's service (ch60 — historically the boy Toshizō will later send south with his photograph, a lock of hair, and his last message to the Hino Satō family; handle the setup, the errand itself is a later chapter); Toshizō's column takes MATSUMAE CASTLE (ch61 松前城略取, Meiji 1/11 = Nov 1868); the new government's ironclad ram 甲鉄 KŌTETSU (the ex-Confederate STONEWALL) arrives and tips the naval balance (ch62 甲鉄艦); and the shogunal navy's desperate boarding raid on the Kōtetsu, the BATTLE OF MIYAKO BAY (ch63 宮古湾海戦, Meiji 2/3/25 = 6 May 1869 — the KAITEN tries to board, the GATLING gun cuts the boarders down, Toshizō commands the raiding force). Fact-check: Enomoto's fleet reaching Ezo, the Washinoki landing and the drive on Goryōkaku, the founding of the Ezo regime and its election (Enomoto president); the seizure of Matsumae Castle by Hijikata's column; the historicity of Ichimura Tetsunosuke and the photograph-errand thread; the Kōtetsu/Stonewall (ex-Confederate ram, delivered to the new government early 1869); the Miyako Bay raid (dates, the Kaiten's abordage, the Gatling gun, the failure, Kōga Gengo's death); any dates/rosters. WATCH THE CALENDAR: this span crosses from Keiō 4 / Meiji 1 (1868) into MEIJI 2 (1869) — the Miyako Bay fight is 1869. KONDŌ ISAMI is DEAD (beheaded at Itabashi Keiō 4/4/25; grave raised by Toshizō at Aizu Atago-yama) and OKITA SŌJI is DEAD (consumption, Sendagaya, Keiō 4/5/30) — do NOT write either as a living voice; both may recur in Toshizō's memory. NAGAKURA and HARADA are gone (parted ch53); do not write them into the northern column unless the source does. SAITŌ HAJIME (now takes the pen-name 諾斎 "Dakusai") and MATSUMOTO SUTESUKE were Toshizō's vice-commanders of the 新選隊 "Shinsentai" as of ch57–58, BUT historically Saitō stayed to fight at Aizu and did NOT cross to Ezo — READ THE SOURCE before carrying him north; render only what the text has. Ōtori Keisuke, Enomoto Takeaki, Matsudaira Tarō (陸軍奉行 / Commissioner of the Army) are live major characters, rendered BY HAND, not keyed (B11/B12 precedent for one-off and recurring historical figures). Oyuki is in the deep background now (invented heroine, flagged ch32 — handle as fiction, no fact-check of her existence). Do not stop mid-batch except for a genuine blocker or completion. For each chapter:
1. Build data/zh/<id>.txt from data/src with scripts/build_zh.py <id> <srcbase> "<title>" (title line "### <title>" then one body line per non-empty source paragraph, skipping the first two header lines). ch59=63_part0061, ch60=64_part0062, ch61=65_part0063, ch62=66_part0064, ch63=67_part0065. Fix any extractor splits (this source has had none: a narration line ending in 、 before a 「quote」 is the source's own lead-in, handled by the {j} join, NOT a split to merge). Recover scene breaks: the RELIABLE method is to grep the XHTML (data/src_epub/OEBPS/Text/partNNNN.xhtml) for runs of TWO OR MORE consecutive <p><br/></p> in the body and read the text on either side of each run — scripts/scene_map.py reports the same runs by "body paragraph N" but its N has drifted off-by-one, so PLACE *** BY TEXT BOUNDARY, not by the reported index (the single pair right after the chapter title is only the title/body separator; a SINGLE <br/> is a paragraph break, not a scene break). Place *** in the reading at those points. (B12 had exactly ONE internal *** in each of ch54–ch58.)
2. Translate to the FROZEN ch01 register. Names Japanese order, surname first, macrons; CONSULT reference/furigana_readings.tsv before romanizing ANY name or word (it has caught readings whole-book, e.g. B11's 乾→Inui, 干城→Tateki, and B12's 蓼沼→Tadenuma, 尾国峠→Oguni-tōge, 斗筲→toshō, 昌平黌→Shōheikō). The source uses EXPRESSIVE gikun furigana (e.g. 将軍→たいじゅ, 京→ここ, 近藤→せんせい, 慶喜→うえさま) which are semantic, NOT phonetic, and must not be romanized. Consult glossary.json (302 rows; then authority.json) first, feeding decided renderings back. Use the {j} display-join marker so a quotation reads inline with its lead-in and attribution; verse lines take {p} (one per line). Keep an exchange one paragraph per speaker turn. Watch parity: every 「…」 quote line, every と…いった attribution line, and every 「………」/「───」 silence is its OWN source paragraph and needs its OWN reading line — B12's ch57 dropped one at a "老婆が、"→「quote」→"とあきれるほど…" three-line run and make_bilingual's count (164 vs 166) caught it; a positional re-read fixed it. ALWAYS re-check dense exchanges and run-on narration for count. OBEY STYLE.md (em-dash budget; no scene-primed idioms). Consult the voice sheets below; read the last two pages of ch58's English before starting ch59 (batch seam).
3. Author out/<id>_reading.md (## title, {j}, {p}, ***, blank-separated). Then the battery: bash scripts/check_chapter.sh <id> <srcbase> "<title_en>" runs reading_to_en + make_bilingual (parity refuses on mismatch) + verify_unit (--noise data/noise.txt) + gen_check_config + check_align + check_content + qc_entities + check_apparatus + check_register. Verify each chapter TAIL against the source explicitly (rule 4).
4. Footnotes per the reader model (first-appearance discipline; keep the "NOT re-noted" ledger in PROGRESS.md; note MORE than the glossary row) via apparatus_merge.py (each glossary row MUST carry a "section": people|places|organizations|terms field AND a "pinyin" field — qc_entities crashes on a row without "pinyin"; set pinyin = the romanized en. The merge nests the section and check_apparatus stays clean; render the glossary's DECIDED form verbatim, or qc_entities/check_content flag it; when the source shortens a name give the glossary a bare-surname en, and do NOT key a name that appears in FRAGILE COMPOUNDS — a Kyoto/Fushimi/Osaka street like 三条通/京町通/谷町筋/四条通 is rendered by hand, NOT keyed, or it false-flags). NOTE the ONE standing check_content false-flag (ch52's alias 近藤勇平 ⊃ key 近藤勇): qc_entities, the battery gate, is clean; if a NEW alias-inside-a-key case appears, render faithfully and DOCUMENT the false-flag, do not distort the text. A NOTE ANCHOR must be a verbatim substring of the reading file with LITERAL macrons (ō, not sh&#333;gi) AND WITHOUT embedded straight quotes/apostrophes (pick a clean run of words — an English possessive like "Toshizō's" or a "…"-wrapped phrase will not anchor cleanly). Note BODIES use literal Unicode but numeric character references for any &-entity. Any figure from data/figs/ with a translated caption and real alt text (ch24-58 had none).
5. check_register.py --ref reference/ch01_ref.md out/<id>_reading.md; record in PROGRESS.md. If a chapter flags STILTED, add contractions to the INFORMAL speakers (Toshizō's blunt dialect) ONLY — leave deliberately formal registers (a ceremonial official, quoted documents/memoir, a set-piece political analysis, Oyuki's refined samurai-widow speech) alone. Battle/narration chapters run em-dash LOW and dialogue-light. STYLE rule 1 governs PILE-UPS, not aggregate rate: no sentence carries 3+ em dashes; a single MATCHED PAIR bracketing an appositive is allowed (B12 ch58 has several, all legit). Keep the source's ── interruptions (render as a leading ──, U+2500 box-drawing, NOT counted as an em dash) and legitimate matched pairs; convert discretionary dash-asides to commas/parentheses (Shiba's own （）glosses and his 、-set appositives → commas/parentheses). Fact-check historical claims against real scholarship (never LLM-sourced; IGNORE Grok/Grokipedia), verdict in the note. Add numeral-noise rules to data/noise.txt as new numbered names/idioms/place-names appear (comment each; never noise a real quantity). NUMBER-CHECK LESSONS (confirmed through B12): write LARGE composites as DIGITS — hundreds+tens ("150", not "a hundred and fifty"), thousand-composites ("1,687", "1,800", "625,000"), and kanji/full-width years; but the checker DOES compose plain tens×thousand ("thirty thousand", "fifty thousand" PASS) and DOES read ordinals ("first"/"seventh"/"Seventh Regiment" PASS); "a million"/"a hundred thousand" need the article; a romanized name/place/ship whose kanji carries a numeral (e.g. 千代田丸, 六十里, 松五郎) needs a commented noise rule; an idiom with a numeral (四散/四囲/一言一句/万に一つ) is noised; an archaic 有/余 BETWEEN numerals orphans them (noise the compound; the English carries the real quantity).
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck (java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/burn-o-sword.epub); record ALL check results and EVERY digitization glitch in PROGRESS.md; update HANDOFF.md; commit and push to claude/burn-o-sword.

End the batch with BOTH chat deliverables (CLAUDE.md rule 1, enforced by the Stop hook): the built EPUB ATTACHED in the chat AND the Batch 14 kickoff PASTED VERBATIM in a fenced code block. Batch 14 = ch64 through ch68.

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
- B11 = ch49 to ch53, COMPLETE. Notes 340 to 381.
- B12 = ch54 to ch58, COMPLETE. ch54 袂別 / "The Parting" (KONDŌ'S SURRENDER at
  Nagareyama and the FINAL PARTING of Kondō and Toshizō; the Hachiōji
  interrogation of the Satō household; Arima Tōta and Kagawa Keizō), ch55
  大鳥圭介 / "Ōtori Keisuke" (the break-out from Edo; Ōtori made commander at
  Ichikawa, Toshizō second; the march north; the fight at Oyama), ch56 城攻め /
  "The Siege" (Toshizō over Ōtori's objection storms UTSUNOMIYA CASTLE, Keiō
  4/4/19; Saitō and the Izumi-no-kami Kanesada at the gate; Arima grazed), ch57
  沖田総司 / "Okita Sōji" (OKITA'S DEATH at the Sendagaya nursery, Keiō 4/5/30,
  never learning of Kondō's fate; the epitaph in kanbun; Toshizō renames the
  corps the 新選隊 Shinsentai; Saitō "Dakusai" and Matsumoto Sutesuke), ch58
  陸軍奉行並 / "Assistant Commissioner of the Army" (Toshizō made
  rikugun-bugyō-nami; ENOMOTO's fleet reaches Sendai; the great French maneuver;
  the Endō interview and the Kyoto-flashback sparrow duel; Sendai submits;
  Toshizō sails for Ezo on the Kaiyō-maru). Notes 382 to 416 (35 this batch). All
  checks green except the ONE documented ch52 false-flag. qa_epub PASS
  (416/416/416); epubcheck 0/0/0/0. Continuous note number now 416. Glossary
  unchanged at 302 rows (no new keys). 58 of 71 chapters translated. See
  PROGRESS.md B12 for the full record: scene-break placements, the noise
  additions, the number-check confirmations, and the fact-check verdicts.

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
  (ch52: 近藤勇平 ⊃ 近藤勇) false-flags one paragraph. qc_entities (the battery
  gate) does NOT; document the false-flag, do not distort the translation.
- scripts/check_numbers.py PATCHES (target-side only, can only ADD a number):
  B04 reads "a/one hundred and <ten..nineteen>"; B07 folds ONES into the
  hundred+low band. Regression tests pass. DO NOT REVERT. Confirmed limits/reach
  through B12: composes plain tens×thousand ("thirty thousand", "fifty thousand")
  and reads ordinals ("first"/"seventh"), but does NOT compose hundreds+tens
  ("a hundred and fifty" → write "150") nor thousand-composites (write "1,687",
  "1,800", "625,000") nor kanji/full-width years (write DIGITS, noise the source
  form); needs an explicit "a"/"one" before "million"/"hundred thousand"; "a
  score" not read (write "twenty"); a 有/余 BETWEEN numerals orphans the tail
  (noise the compound; English carries the real quantity); vague "hundreds" 何百
  and numeral idioms (四散/四囲/一言一句) are noised; block-numbers 丁目 "the Nth
  block" carry and pass.
- data/noise.txt (B01 to B12): Japanese name/idiom/place/ship numeral rules,
  each commented. Never noise a real quantity. B12 added (all commented): 四散,
  敬三 (ch54); 一翁, 電四郎, 勇四郎, 三九郎, 鑑三郎, 悌二, 三宅, 三拝, 四囲 (ch55);
  千早 (ch56); 松五郎, 六十里, 十有二 (ch57); 一言一句, 孫三郎, 文七郎, 千代田
  (ch58).
- STYLE.md (B01): the house style sheet (em-dash budget; scene-primed idioms).
  READ IT each batch; add to it when the commissioner corrects a line. No new
  rule in B12.
- reference/ch01_ref.md (B01): the FROZEN register reference. Do not edit.

## Voice sheets (one per major character; consult at every dialogue scene)

- NARRATOR: third person, wry and knowing, fond of the aside and the forward
  glance to events years ahead (B12: forward-glances to Ōtori's Meiji career, to
  Arai Ikunosuke as first head of the Central Meteorological Observatory, to the
  Satō family memoirs of Gennosuke and the Sendai interview, to Saitō's old-age
  schoolteaching and Nomura's fate). KEEPS Shiba's own modern parentheticals
  (Western dates; present-day place-names such as "today's Ishinomaki"; quoted
  real records — the Gennosuke recollection ch54, the Sendai-Boshin records ch58)
  AND his bracketed editorial glosses INSIDE dialogue and quotes (（政宗）,
  （小さなマス）, （江戸開城後は…）, etc.). KEEP them all — render as parentheses
  (preferred), commas, or square-bracket glosses; do NOT dash every one.
- HIJIKATA TOSHIZŌ ("Toshi"): the hero, 34–35. Rough Bushū farm dialect off
  guard, contracted and blunt (おらァ, ねえ, かえ); a cool tactician who reads the
  new warfare fast and TOOK IN French method whole at the Sendai maneuver
  (Brunet: "the French emperor would want you for a division commander"). SOLE
  FIELD COMMANDER of the northern remnant; his creed since Kōshū is pure
  fight-to-the-end. By ch58 he is 陸軍奉行並 (rikugun-bugyō-nami, Assistant
  Commissioner of the Army), in French-style uniform, aboard the Kaiyō-maru bound
  for Ezo. He is a poor set-piece orator (the Sendai speech "not so different
  from a gambler-boss's") but unmatched on the field. ALIAS 内藤隼人 "Naitō
  Hayato" from ch53 (watch whether the north still uses it). With OYUKI he was
  another man; she is his acknowledged WIFE (ch48), now in the deep background.
  Sword: 和泉守兼定 (Izumi-no-kami Kanesada) + wakizashi 堀川国広.
- KONDŌ ISAMI: DEAD. Surrendered at Nagareyama (Keiō 4/4/3) as 大久保大和 "Ōkubo
  Yamato" to spare his levy; taken to Itabashi and BEHEADED (Keiō 4/4/25 = 17 May
  1868), head displayed at Sanjō-gawara; Toshizō raised his gravestone (kaimyō
  貫天院殿純義誠忠大居士) on Aizu Atago-yama. Warm, big-jawed Bushū farmer's son;
  the final parting from Toshizō divided them over "what each finds beautiful"
  (Kondō submits to 大義名分, Toshizō fights on). Do NOT write him as a living
  voice; he recurs only in memory.
- OKITA SŌJI: DEAD. Died of consumption at the Sendagaya nurseryman's (植木屋
  平五郎方), Keiō 4/5/30 = 19 July 1868, nursed at the end by no one; sister
  Omitsu (お光, rendered "Omitsu") had parted from him for Shōnai on the very day
  Kondō surrendered. He NEVER LEARNED of Kondō's execution (tradition). Clasped
  the 菊一文字 Kiku-ichimonji at the end. Bright, glib, teasing to the last. Do
  NOT write him as a living voice; recurs only in memory.
- OYUKI (お雪, given name Yuki, self-refers as お雪→"Oyuki", bare 雪→"Yuki"): the
  HEROINE, WHOLLY INVENTED (Shiba's afterword; flagged at ch32). Edo-born samurai
  widow, a painter (art-name Kōka). Register: quiet, CRISP Edo/samurai speech,
  refined and formal (でございます), NO Kyoto softness; leave her low-contraction
  speech ALONE at register gates (characterization). Toshizō's acknowledged WIFE;
  in the deep background since ch49. GLOSSARY KEY is お雪 → "Oyuki"; render お雪 as
  "Oyuki" or qc_entities flags it. Handle as fiction, no fact-check.
- ŌTORI KEISUKE: LIVE major character (entered ch55). Western-trained shogunal
  infantry commander (歩兵頭); son of an Akō village doctor; Ogata Kōan's Tekijuku;
  a brilliant scholar with NO field talent (Toshizō sees through it). Made
  commander of the break-out army at Ichikawa; bookish, cautious, vain, needled
  Toshizō as a "fencing-tradesman" and an unlettered peasant. Leads the remnant
  north with Toshizō. Rendered BY HAND "Ōtori Keisuke"/"Ōtori", NOT keyed. Later
  a distinguished Meiji official (d.1911).
- ENOMOTO TAKEAKI (榎本武揚 / 榎本和泉守 / 榎本釜次郎 "Kamajirō"): LIVE major
  character (named earlier, ON STAGE from ch58). Dutch-trained vice-president of
  the shogunal navy, captain of the Kaiyō-maru; led the fleet out of Shinagawa
  (8/19) to Ezo. Rare among Japanese in having seen Europe; a polished orator and
  statesman (the foil to Toshizō's blunt field-soldier). Grips hands "in the
  Western manner". Future president of the Ezo regime. Rendered BY HAND, not keyed.
- MATSUDAIRA TARŌ: LIVE. Former infantry commander, now 陸軍奉行 (Commissioner of
  the Army, above Toshizō's -nami rank), well disposed toward Toshizō; future
  vice-president of the Ezo regime. Rendered by hand "Matsudaira Tarō" (noted ch47).
- SAITŌ HAJIME (now the pen-name 諾斎 "Dakusai" — "whatever you say, I say yes"):
  captain of the old Third Unit; the miraculous survivor; vice-commander of the
  Shinsentai as of ch57. Terse, droll in later years. WATCH B13: historically
  Saitō stayed to fight at Aizu and did NOT cross to Ezo — render only what the
  source has; do not carry him north on assumption. Glossary key (principal #11).
- MATSUMOTO SUTESUKE (松本捨助): Toshizō's distant relative from Minamitama,
  Bushū; intermediate-license Tennen Rishin-ryū man; no brilliance but charges in
  first and announces "Matsumoto Sutesuke of the Shinsengumi". A second
  vice-commander of the Shinsentai (ch57). Rendered by hand, not keyed.
- FORESHADOWED for B13, rendered by hand until on stage: ICHIMURA TETSUNOSUKE
  (市村鉄之助, the page — the boy Toshizō will send south with his photograph and
  last message; ch60 is his entry), ARAI IKUNOSUKE (荒井郁之助, Kaiyō-maru captain,
  future first head of the Central Meteorological Observatory; ch58), JULES BRUNET
  and the French advisers (ch58), HOSHI JUNTARŌ (星恂太郎, Sendai's Western unit).
- Kyoto-era dead comrades — ITŌ KASHITARŌ, SERIZAWA, NIIMI, KIYOKAWA, YAMANAMI
  (敬助), TŌDŌ HEISUKE, INOUE GENZABURŌ, SHICHIRI, HAYASHI GONSUKE, YAMAZAKI SUSUMU
  (ch49), and now KONDŌ and OKITA: DEAD. Do not write them as living voices.

## Renderings settled / carry-forward

- Title "Burn, O Sword!"; author Shiba Ryōtarō. Names Japanese order, macrons.
- ONE rendering per referent, all in glossary.json (302 rows, unchanged in B12).
  RENDER THE DECIDED FORM VERBATIM: 甲陽鎮撫隊 "the Kōyō Chinbutai", 伝習隊 "the
  Denshūtai", 旗本 "hatamoto", 和泉守兼定 "Izumi-no-kami Kanesada", 佐藤彦五郎
  "Satō Hikogorō", お雪 "Oyuki" (bare 雪 = "Yuki"), 近藤勇 "Kondō Isami",
  坂本竜馬 "Sakamoto Ryōma", 勝海舟 "Katsu Kaishū", 助勤 "jokin", 副長
  "vice-commander", 天然理心流 "the Tennen Rishin-ryū", 誠 "Makoto".
- ALIASES: 大久保大和 "Ōkubo Yamato" (Kondō), 内藤隼人 / 内藤先生 "Naitō Hayato"/
  "Naitō-sensei" (Toshizō). Render as given.
- RENDERED INLINE, NOT KEYED (appear in built chapters / fragile compounds or are
  one-off/recurring historical figures): 慶喜 "Yoshinobu", 板垣退助 "Itagaki
  Taisuke", 松平容保 "Matsudaira Katamori". B12 by-hand figures (not keyed): Ōtori
  Keisuke, Enomoto Takeaki (Izumi-no-kami / Kamajirō), Matsudaira Tarō, Arai
  Ikunosuke, Arima Tōta, Kagawa Keizō, Tani Moribe (谷干城 Tateki), Nakaoka
  Shintarō, Tanaka Kensuke (光顕 Mitsuaki), Saigō Kichinosuke (= Takamori), Ōkubo
  Ichiō, Akizuki Tonosuke, Tatsumi Kanzaburō, Amano Denshirō, Kimura Ryūkichi,
  Ogasawara Shintarō, Torii Tango-no-kami, Toda Tosa-no-kami, Date Yoshikuni
  (伊達慶邦, 陸奥守), Date Masamune (貞山公 Teizan), Endō Bunshichirō, Ōeda
  Magosaburō, Tomi Kogorō, Hoshi Juntarō, Sakuma Teiji, Nomura Risaburō, Okita
  Rintarō, Omitsu (お光), Otsune (Kondō's wife), Matsumoto Ryōjun, Matsumoto
  Sutesuke, Sakai Tadazumi, Jules Brunet, Commodore Perry, Shimizu no Jirōchō,
  Kunisada Chūji. Place/thing by hand: 流山 "Nagareyama", 松戸 "Matsudo", 宇都宮
  "Utsunomiya", 小山 "Oyama", 壬生 "Mibu", 日光 "Nikkō", 蓼沼 "Tadenuma", 千駄ケ谷
  "Sendagaya", 仙台 "Sendai", 青葉城 "Aoba Castle", 日和山 "Hiyoriyama", 開陽丸
  "Kaiyō-maru", 甲鉄 "Kōtetsu", 菊一文字 "Kiku-ichimonji", 昌平黌 "the Shōheikō".
- Era-year form kept with the numeral ("Keiō 4", "the first year of Meiji",
  "Meiji 44"). 戊辰 rendered "the year Boshin". Shiba's own modern intrusions and
  bracketed glosses KEPT.
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
- ch29-ch33 (B07): YAMANAMI'S SEPPUKU; Itō made staff officer; OYUKI enters.
- ch34-ch38 (B08): the ITŌ SPLIT; the Goryō-eji; Saitō planted as a spy; the
  TAISEI HŌKAN.
- ch39-ch43 (B09): the ABURANOKŌJI killing of Itō; the ŌSEI FUKKO; Kondō SHOT;
  the OPENING OF THE BOSHIN WAR.
- ch44-ch48 (B10): TOBA-FUSHIMI and the GREAT COLLAPSE; YOSHINOBU'S FLIGHT; the
  two nights with OYUKI at the Saishō-an.
- ch49-ch53 (B11): the RETREAT TO EDO; the KŌYŌ CHINBUTAI and the DEFEAT AT
  KATSUNUMA; the split from Nagakura/Harada; the MUSTERING at NAGAREYAMA.
- ch54-ch58 (B12): KONDŌ'S SURRENDER AND EXECUTION and the FINAL PARTING; the
  BREAK-OUT under ŌTORI and the march north; the STORMING OF UTSUNOMIYA CASTLE;
  OKITA'S DEATH; Toshizō made ASSISTANT COMMISSIONER OF THE ARMY as ENOMOTO's
  fleet reaches Sendai, the domain submits, and Toshizō sails for EZO.

## What is NEXT

- B13 = ch59 to ch63 (kickoff above): 艦隊北上 / 小姓市村鉄之助 / 松前城略取 /
  甲鉄艦 / 宮古湾海戦. THE SHIFT TO EZO AND THE SEA WAR — the fleet north to
  Hakodate/Goryōkaku; the page Ichimura Tetsunosuke; the seizure of Matsumae
  Castle; the ironclad Kōtetsu (Stonewall); the boarding raid at Miyako Bay (into
  Meiji 2 / 1869). Then B14 ch64-68 (the fall of Goryōkaku and Toshizō's death),
  B15 ch69-71 back matter + whole-book reconciliation + COMPLETION.

## Open items for the read-through (B13)

- CALENDAR: this span crosses Keiō 4 / Meiji 1 (1868) into MEIJI 2 (1869). Keep
  era-years with their numeral; the Miyako Bay fight is Meiji 2/3/25 = 6 May 1869.
- EZO vs HOKKAIDŌ: the region is 蝦夷地 Ezo until renamed 北海道 Hokkaidō in 1869;
  Shiba uses both — render the source's word for the moment.
- SAITŌ AT AIZU: historically Saitō Hajime stayed to fight at Aizu and did NOT
  cross to Ezo; read the source before carrying him north.
- ICHIMURA TETSUNOSUKE: ch60 is his ENTRY; the photograph-errand thread pays off
  in a later chapter (Toshizō's death). Handle the setup, don't pre-empt.
- KŌTETSU / MIYAKO BAY: fact-check the Stonewall's provenance and delivery, the
  Kaiten's abordage, the Gatling gun, Kōga Gengo's death, and the raid's failure.
- OYUKI recurs only in the deep background now; keep her crisp Edo/samurai
  register if she appears. Handle as fiction.

## Environment / traps state

- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches).
- data/src/ and data/src_epub/ are gitignored (regenerate via ingest if empty);
  scene-break detection needs data/src_epub, so re-run ingest before it if empty.
- SCENE BREAKS: place *** BY TEXT BOUNDARY (grep XHTML for 2+ <p><br/></p> runs);
  scene_map.py's index drifts. Single <br/> = paragraph break; the pair after the
  title = title/body separator. (B12: exactly one internal *** in each of
  ch54–ch58.)
- PARITY trap (PROVEN B04-B12): every quote, attribution (と…いった), and silence
  (「………」/「───」) is its own paragraph; a narration lead-in ending in 、 before a
  quote is its own line too (join it for display with {j} on the FOLLOWING line);
  a "老婆が、"→「quote」→"とあきれるほど…"-type run is THREE source lines (B12 ch57
  drop, caught by make_bilingual's count). Never add or drop a beat; a count
  mismatch refuses to write, a positional re-read fixes it.
- NUMBER-CHECK traps (confirmed B12): DIGITS for hundreds+tens ("150"),
  thousand-composites ("1,687"/"1,800"/"625,000") and kanji/full-width years; but
  plain tens×thousand ("thirty thousand"/"fifty thousand") and ordinals compose
  fine; "a million"/"a hundred thousand" need the article; a name/place/ship whose
  kanji carries a numeral needs a commented noise rule; numeral idioms
  (四散/四囲/一言一句/万に一つ) are noised; an archaic 有/余 between numerals orphans
  them (noise the compound, English carries the quantity). Real koku/troop/date
  figures stay in word- or digit-form and DO carry the number.
- CONTENT/ENTITY trap: render the glossary's DECIDED form verbatim or it flags.
  Do NOT key a name in a FRAGILE COMPOUND (Kyoto/Fushimi/Osaka streets, ship
  names with numerals). NEW glossary rows MUST carry both a "section" and a
  "pinyin" field. check_content matches keys by SUBSTRING, so a source ALIAS that
  contains a key (ch52: 近藤勇平 ⊃ 近藤勇) false-flags one paragraph — qc_entities
  does NOT; document it, do not distort the text.
- GLOSSARY CASCADE: adding a global key re-checks EVERY built chapter. Before
  adding, grep data/zh for the key. B12 added NO new keys (all figures by hand),
  so no cascade.
- REGISTER: battle/parting chapters run em-dash LOW and dialogue-light. Contract
  the INFORMAL speakers only (Toshizō's dialect); leave formal registers alone
  (quoted documents/memoir, ceremonial officials, Toshizō's set-piece Sendai
  speech). STYLE rule 1 = no PILE-UP (3+ em dashes in a sentence); a single
  matched PAIR bracketing an appositive is allowed. B12: all within tolerance,
  none STILTED.
- NOTE-ANCHOR trap: the anchor must be a verbatim substring of the reading with
  LITERAL macrons and WITHOUT embedded straight quotes/apostrophes — an English
  possessive ("Toshizō's"), a "…"-wrapped phrase, or an apostrophe name will NOT
  anchor; pick a clean run of words. Note bodies use literal Unicode but numeric
  refs for any &-entity.
- Known failing test, EXPECTED: tests/run_tests.py reports "hook stands down on
  template stub" FAIL (template-only). Not a translation gate. All other tests
  pass.
- All work is on branch claude/burn-o-sword.
