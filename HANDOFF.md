# HANDOFF, Burn, O Sword! (燃えよ剣), Shiba Ryōtarō

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery: every
batch ends with this file's kickoff block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count. Rewrite it at
the end of every batch; always keep the paste-ready kickoff below as its first
section.

## Message to paste into the next chat

```
Burn, O Sword! B14

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then STYLE.md, then book.json. We are translating Burn, O Sword! (燃えよ剣) by Shiba Ryōtarō from a Japanese digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/burn-o-sword; expect the harness to open you on a stray per-task branch and consolidate per CLAUDE.md rule 2. Deliverable out/burn-o-sword.epub.

Batches 1 to 13 are DONE (ch01 to ch63). ch01 is the FROZEN register reference: reference/ch01_ref.md. Run ./setup.sh; if data/src/ is empty re-run scripts/ingest_epub.py source.epub (Japanese-aware: strips furigana, substitutes 8 gaiji, writes reference/furigana_readings.tsv). No source-note stream. Keep the source's own cover (data/figs/embed0009_HD.jpg), reused byte-identical, exactly as book.json already sets it; the commissioner likes it, do not change it. The known failing test "hook stands down on template stub" is EXPECTED (it only passes on the template placeholder kickoff); every other test passes.

Do Batch 14 = ch64 through ch68 (襲撃 / The Attack; 再会 / Reunion; 官軍上陸 / The Imperial Army Lands; 五稜郭 / Goryōkaku; 砲煙 / Gunsmoke), end to end per the CLAUDE.md pipeline, RUN TO COMPLETION. This span is THE CLIMAX: THE MIYAKO BAY RAID AND THE FALL OF EZO, ending in TOSHIZŌ'S DEATH. At the close of B13 the raiding ship 回天 KAITEN lay hidden off Miyako Bay, Toshizō's boarding party drilled and waiting; the government's ironclad 甲鉄 KŌTETSU (ex-Confederate STONEWALL) lay at anchor with the GATLING gun on its deck. B14: the KAITEN alone (the Takao and Banryū lost in the storm) attacks the Kōtetsu at dawn Meiji 2/3/25 = 6 MAY 1869 under a false flag; the deck is far higher than the Kōtetsu's so the boarders must cross one at a time; the GATLING gun cuts them down; Kaiten captain 甲賀源吾 KŌGA GENGO is KILLED; the raid FAILS and the Kaiten escapes back to Hakodate (ch64 襲撃). Then 再会 Reunion (ch65 — READ THE SOURCE: likely OYUKI returns, or a comrade; handle Oyuki as fiction if she appears, her crisp Edo/samurai register). The new government army LANDS on Ezo (官軍上陸, ~Meiji 2/4 = April–May 1869) and drives on Hakodate/Goryōkaku (ch66); the siege of 五稜郭 GORYŌKAKU tightens (ch67); and Toshizō, leading a sortie, is SHOT AND KILLED near the Ippongi-seki / Bentendaiba on Meiji 2/5/11 = 11 JUNE 1869 (砲煙, ch68 — this is where the ICHIMURA TETSUNOSUKE photograph-errand thread pays off: historically Toshizō sends the boy south out of the doomed fortress with his photograph, a lock of hair, and his last message to the Hino Satō family; render whatever the source has, do not pre-empt or invent). Fact-check: the Miyako Bay raid (dates, the Kaiten's abordage, the Gatling gun, the failure, Kōga Gengo's death); the new-government landing on Ezo (Otobe/Esashi April 1869) and the drive on Hakodate; the fall of Matsumae and the Futamataguchi fighting; the siege and surrender of Goryōkaku (Meiji 2/5/18 = 27 June 1869, AFTER Toshizō's death); Toshizō's death (Meiji 2/5/11 = 11 June 1869, shot leading troops near Ippongi-kan / Bentendaiba — the exact spot and the shooter are debated; render the source's version, footnote the historiographic uncertainty); the Ichimura errand; any dates/rosters. WATCH THE CALENDAR: this whole span is MEIJI 2 (1869) — the raid is 6 May, Toshizō's death 11 June, the surrender of Goryōkaku 27 June. KONDŌ ISAMI and OKITA SŌJI are DEAD (may recur in Toshizō's memory only). SAITŌ HAJIME is GONE: in Shiba's telling Toshizō sent him and MATSUMOTO SUTESUKE south from Matsumae with the lord's pregnant wife (ch61, renamed 山口五郎 Yamaguchi Gorō); do NOT write Saitō into the Ezo endgame unless the source brings him back (historically he never went north at all — he stayed at Aizu; this is Shiba's fiction). KŌGA GENGO dies in ch64 — do not write him living after it. ENOMOTO TAKEAKI (president), ŌTORI KEISUKE (army commissioner), MATSUDAIRA TARŌ (vice-president), ARAI IKUNOSUKE (navy commissioner), NAGAI GENBA-NO-KAMI NAOMUNE (Hakodate magistrate), ICHIMURA TETSUNOSUKE (Toshizō's page), and on the government side KURODA RYŌSUKE (later 黒田清隆 Kiyotaka, who will argue to spare Enomoto's life after the fall) are live figures rendered BY HAND, not keyed. OYUKI is the invented heroine (flagged ch32 — no fact-check of her existence). Do not stop mid-batch except for a genuine blocker or completion. For each chapter:
1. Build data/zh/<id>.txt from data/src with scripts/build_zh.py <id> <srcbase> "<title>" (title line "### <title>" then one body line per non-empty source paragraph, skipping the first two header lines). ch64=68_part0066, ch65=69_part0067, ch66=70_part0068, ch67=71_part0069, ch68=72_part0070. Fix any extractor splits (this source has had none: a narration line ending in 、 before a 「quote」 is the source's own lead-in, handled by the {j} join, NOT a split to merge). Recover scene breaks: the RELIABLE method is to grep the XHTML (data/src_epub/OEBPS/Text/partNNNN.xhtml) for runs of TWO OR MORE consecutive <p><br/></p> in the body and read the text on either side of each run — scripts/scene_map.py reports the same runs by "body paragraph N" but its N has drifted off-by-one, so PLACE *** BY TEXT BOUNDARY, not by the reported index (the single pair right after the chapter title is only the title/body separator; a SINGLE <br/> is a paragraph break, not a scene break). Place *** in the reading at those points. (B13: ch59 had NO internal ***; ch60–ch63 had exactly ONE each. These climax chapters may have more.)
2. Translate to the FROZEN ch01 register. Names Japanese order, surname first, macrons; CONSULT reference/furigana_readings.tsv before romanizing ANY name or word (it has caught readings whole-book, e.g. B13's 尚志→Naomune not Naoyuki, 富士山丸→Fujiyama-maru, 崇広→Takahiro, 恂太郎→Juntarō, 鍽之助→Sennosuke, 長生→Naganari, 坅門隊→Anamon-tai, 野戦速射砲→"Gatling gun"). The source uses EXPRESSIVE gikun furigana (e.g. 将軍→たいじゅ, 京→ここ, 近藤→せんせい, 慶喜→うえさま) which are semantic, NOT phonetic, and must not be romanized. Consult glossary.json (302 rows; then authority.json) first, feeding decided renderings back. Use the {j} display-join marker so a quotation reads inline with its lead-in and attribution; verse lines take {p} (one per line). Keep an exchange one paragraph per speaker turn. Watch parity: every 「…」 quote line, every と…いった attribution line, and every 「………」/「───」 silence is its OWN source paragraph and needs its OWN reading line — B13's ch62 folded zh L116「と答えた。」into the lead-in and make_bilingual's count (149 vs 150) caught it; a positional re-read fixed it. ALWAYS re-check dense exchanges and run-on narration for count. OBEY STYLE.md (em-dash budget; no scene-primed idioms). Consult the voice sheets below; read the last two pages of ch63's English before starting ch64 (batch seam).
3. Author out/<id>_reading.md (## title, {j}, {p}, ***, blank-separated). Then the battery: bash scripts/check_chapter.sh <id> <srcbase> "<title_en>" runs reading_to_en + make_bilingual (parity refuses on mismatch) + verify_unit (--noise data/noise.txt) + gen_check_config + check_align + check_content + qc_entities + check_apparatus + check_register. Verify each chapter TAIL against the source explicitly (rule 4) — and the DEATH SCENE especially: on any long single-pass unit the tail is where faithfulness fails, and this batch ends the hero's life.
4. Footnotes per the reader model (first-appearance discipline; keep the "NOT re-noted" ledger in PROGRESS.md; note MORE than the glossary row) via apparatus_merge.py, built from a small Python encoder like scripts/build_b13_apparatus.py (anchors LITERAL Unicode + verbatim substrings; note BODIES encode every non-ASCII char to a numeric character reference, <i> tags pass through). Each glossary row (if you add any) MUST carry a "section": people|places|organizations|terms field AND a "pinyin" field — qc_entities crashes on a row without "pinyin"; set pinyin = the romanized en. Render the glossary's DECIDED form verbatim, or qc_entities/check_content flag it; do NOT key a name that appears in FRAGILE COMPOUNDS. NOTE the ONE standing check_content false-flag (ch52's alias 近藤勇平 ⊃ key 近藤勇): qc_entities, the battery gate, is clean; if a NEW alias-inside-a-key case appears, render faithfully and DOCUMENT the false-flag, do not distort the text. A NOTE ANCHOR must be a verbatim substring of the reading file with LITERAL macrons (ō, not sh&#333;gi) AND WITHOUT embedded straight quotes/apostrophes (pick a clean run of words — an English possessive like "Toshizō's" or a "…"-wrapped phrase will not anchor cleanly). Any figure from data/figs/ with a translated caption and real alt text (ch24-63 had none).
5. check_register.py --ref reference/ch01_ref.md out/<id>_reading.md; record in PROGRESS.md. If a chapter flags STILTED, add contractions to the INFORMAL speakers (Toshizō's blunt dialect) ONLY — leave deliberately formal registers alone. Battle/narration chapters run em-dash LOW and dialogue-light (B13 ran 4–8/1k vs the 12.7 ref; all within tolerance, none STILTED). STYLE rule 1 governs PILE-UPS, not aggregate rate: no sentence carries 3+ em dashes; a single MATCHED PAIR bracketing an appositive is allowed. Keep the source's ── interruptions (render as a leading ──, U+2500 box-drawing, NOT counted as an em dash) and legitimate matched pairs; convert discretionary dash-asides to commas/parentheses. Fact-check historical claims against real scholarship (never LLM-sourced; IGNORE Grok/Grokipedia), verdict in the note. Add numeral-noise rules to data/noise.txt as new numbered names/idioms/place-names appear (comment each; never noise a real quantity). NUMBER-CHECK LESSONS (confirmed through B13): the checker composes BARE tens+ones as words ("twenty-one", "thirty-six", "fifty-five" PASS) and "six thousand" (ones×thousand) PASS and reads ordinals; but write LARGE composites as DIGITS — thousand-composites ("1,200", "1,269", "21,374"), hundreds+tens ("180"), and kanji/full-width years; a HYPHENATED hundred-compound ("three-hundred-kin") does NOT compose — write "three hundred kin" unhyphenated; keep 里 = "ri" (万里 → "ten thousand ri", not "leagues"); a romanized name/place/ship whose kanji carries a numeral needs a commented noise rule; a numeral idiom (五十歩百歩/四散/一言一句) is noised; a colloquial elided range (百四、五十軒 "140 or 150") misparses — noise the misread fragment (百四) and let the English carry the real count.
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck (java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/burn-o-sword.epub); record ALL check results and EVERY digitization glitch in PROGRESS.md; update HANDOFF.md; commit and push to claude/burn-o-sword.

End the batch with BOTH chat deliverables (CLAUDE.md rule 1, enforced by the Stop hook): the built EPUB ATTACHED in the chat AND the Batch 15 kickoff PASTED VERBATIM in a fenced code block. Batch 15 = ch69 through ch71 (あとがき Afterword / 解説 Commentary / 司馬遼太郎 About the Author) + whole-book reconciliation (check_reconcile.py, term_ledger, deep_audit) + COMPLETION.md — the FINAL batch.

Cite chapters and sections, never pages.
```

## What is DONE (do not redo)

- Step 0 (ingest + survey), committed. book.json: 68 novel chapters (ch01 to
  ch68) + 3 back-matter units (ch69 あとがき, ch70 解説/Commentary, ch71 About
  the Author).
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
- B12 = ch54 to ch58, COMPLETE. Notes 382 to 416.
- B13 = ch59 to ch63, COMPLETE. ch59 艦隊北上 / "The Fleet Turns North" (the
  Enomoto–Toshizō night conversation aboard the Kaiyō; Enomoto's biography), ch60
  小姓市村鉄之助 / "Ichimura Tetsunosuke, the Page" (the page's entry; the Okita
  sickbed flashback; the photograph-errand thread set up), ch61 松前城略取 / "The
  Seizure of Matsumae Castle" (Meiji 1/11; Toshizō's column takes the castle;
  Saitō and Matsumoto sent south with the lord's wife), ch62 甲鉄艦 / "The
  Ironclad" (the Kōtetsu/Stonewall arrives; the Ezo election; the Tōgō digression;
  Toshizō conceives the boarding raid), ch63 宮古湾海戦 / "The Sea Fight at Miyako
  Bay" (the approach; the storm scatters the Banryū/Takao; the Kuroda-vs-Kōtetsu
  drunken-flask scene; the raid readied). Notes 417 to 434 (18 this batch). All
  checks green except the ONE documented ch52 false-flag. qa_epub PASS
  (434/434/434); epubcheck 0/0/0/0. Continuous note number now 434. Glossary
  unchanged at 302 rows (no new keys). 63 of 71 chapters translated. See
  PROGRESS.md B13 for the full record: scene-break placements, the noise
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
- scripts/build_b13_apparatus.py (B13): the small encoder that builds an
  apparatus JSON from Unicode note bodies — anchors literal, bodies numeric-ref
  encoded, <i> tags preserved. Copy/adapt it per batch (build_b14_apparatus.py).
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
  through B13: composes BARE tens+ones as words ("twenty-six", "thirty-six",
  "fifty-five", "twenty-one" PASS) and "six thousand" (ones×thousand) PASS and
  reads ordinals; does NOT compose a HYPHENATED hundred-compound
  ("three-hundred-kin" → write "three hundred kin") nor hundreds+tens ("180" as
  digits) nor thousand-composites ("1,200"/"1,269"/"21,374" as digits) nor
  kanji/full-width years; needs "a"/"one" before "million"/"hundred thousand";
  "five continents" (五大州) composes and PASS; a 有/余 between numerals orphans
  them; numeral idioms and name/place/ship numerals are noised.
- data/noise.txt (B01 to B13): Japanese name/idiom/place/ship numeral rules,
  each commented. Never noise a real quantity. B13 added (all commented): 五稜郭
  (ch59); 五十歩百歩, 百四 (ch61); 八太郎, 源六, 佐七郎, 弥七 (ch62); 四国屋,
  中島四郎, 大三郎 (ch63).
- STYLE.md (B01): the house style sheet (em-dash budget; scene-primed idioms).
  READ IT each batch; add to it when the commissioner corrects a line. No new
  rule in B13.
- reference/ch01_ref.md (B01): the FROZEN register reference. Do not edit.

## Voice sheets (one per major character; consult at every dialogue scene)

- NARRATOR: third person, wry and knowing, fond of the aside and the forward
  glance to events years ahead (B13: the Tōgō Heihachirō digression to Tsushima
  1905, Ōmura Masujirō's assassination, Kuroda Kiyotaka as future PM, Ichimura's
  death in the Seinan War 1877, the Kaiyō's Dutch building, the Sino-Japanese-War
  song of the Azuma). KEEPS Shiba's own modern parentheticals (Western dates;
  present-day place-names such as "the city of Miyako in Iwate prefecture";
  quoted real records — the Bakusōroku, the Yokohama Herald, the門人 recollection
  of Ōmura) AND his bracketed editorial glosses. KEEP them all — render as
  parentheses (preferred), commas, or square-bracket glosses; do NOT dash every
  one.
- HIJIKATA TOSHIZŌ ("Toshi"): the hero, 34–35. Rough Bushū farm dialect off
  guard, contracted and blunt (おらァ, ねえ, かえ); but with his superior/peer
  ENOMOTO he speaks MEASUREDLY (the ch59 night talk, the ch62 war-council). A cool
  tactician who reads the new warfare fast; SOLE FIELD COMMANDER of the northern
  remnant; his creed is pure fight-to-the-end ("Kondō died for having failed to
  take Kōshū Castle; in recompense I mean to take the ironclad"). By B13 he is
  陸軍奉行並 (rikugun-bugyō-nami, assistant army commissioner) in the Ezo regime,
  aboard the Kaiten, drilling the boarding party. His genius is field-tactics and
  reconnaissance, not the great hall. ALIAS 内藤隼人 "Naitō Hayato" from ch53
  (dormant in the north). With OYUKI he was another man; she is his acknowledged
  WIFE (ch48), deep background. Sword: 和泉守兼定 (Izumi-no-kami Kanesada) +
  wakizashi 堀川国広. B14 ENDS HIS LIFE (ch68, Meiji 2/5/11) — verify the death
  scene's tail against the source explicitly; never invent his last words.
- ENOMOTO TAKEAKI (榎本武揚 / 榎本和泉守 / 榎本釜次郎 "Kamajirō"): LIVE major
  character, ON STAGE B12–B13. Dutch-trained president of the Ezo regime, captain
  of the (now sunk) Kaiyō-maru. Rare among Japanese in having seen Europe; a
  polished orator, statesman, and optimist (the narrator likens him to Kondō in
  that). Grips hands "in the Western manner". Deeply chiseled "Spanish" face,
  figure-eight mustache, self-designed navy uniform, five gold sleeve-stripes.
  Fond of the Shinsengumi. Rendered BY HAND, not keyed. Future Meiji statesman
  (d.1908).
- ŌTORI KEISUKE: LIVE (entered ch55). Western-trained shogunal infantry commander,
  now army commissioner (陸軍奉行) of the Ezo regime; a brilliant scholar with no
  field talent; bookish, cautious, vain, needled Toshizō as an unlettered peasant.
  Rendered BY HAND "Ōtori Keisuke"/"Ōtori", NOT keyed. Later a distinguished Meiji
  official (d.1911).
- MATSUDAIRA TARŌ: LIVE. Vice-president (副総裁) of the Ezo regime; former
  infantry commander, well disposed toward Toshizō; young, all smiles. Rendered by
  hand "Matsudaira Tarō" (noted ch47).
- ARAI IKUNOSUKE (荒井郁之助): LIVE. Navy commissioner (海軍奉行) of the Ezo
  regime; former Kaiyō captain; sends the scout-ships. Future first head of the
  Central Meteorological Observatory. Rendered by hand, not keyed.
- ICHIMURA TETSUNOSUKE (市村鉄之助): ON STAGE from ch60. Toshizō's page (小姓),
  16, of the Ōgaki domain in Mino; slender, clear-eyed, said to look like Okita
  Sōji (his pride). Enlisted at Fushimi at 15 (lied "nineteen"), taken on "for
  Okita's sake"; nursed the dying Okita; his brother Gōzō fled and vanished. Grave,
  devoted, brave in every fight. THE PHOTOGRAPH-ERRAND boy — historically Toshizō
  sends him south from the doomed fortress with his photograph, hair, and last
  message to the Satō family; PAYS OFF IN B14's death chapters. Killed in the
  Seinan War, 1877. Rendered by hand, not keyed.
- KŌGA GENGO (甲賀源吾): ON STAGE ch62–ch63. Captain of the Kaiten; 31; a shogunal
  retainer (not hereditary hatamoto), fourth son of a Kakegawa samurai, descended
  from the Kōga ninja line; a serious navigator trained under Yatabori and Arai;
  terse, capable, well-disposed to Toshizō (Toshizō thinks him "the finest talent
  in Hakodate", built like Tōdō Heisuke or Nagakura). DIES in the Miyako Bay raid
  (ch64) — do not write him living after it. Rendered by hand, not keyed.
- KURODA RYŌSUKE (黒田了介, later 黒田清隆 Kiyotaka): LIVE, government side (entered
  ch63). Satsuma staff officer commanding the army units against Ezo; drunk,
  high-handed, but able (the comic-tragic Kōtetsu flask scene is his). Future
  director of Hokkaidō colonization and 2nd PM of Japan; will argue to SPARE
  ENOMOTO after the fall. Rendered by hand, not keyed.
- SAITŌ HAJIME (諾斎 "Dakusai"; renamed 山口五郎 "Yamaguchi Gorō" ch61): GONE from
  the northern story. In Shiba's telling he crossed to Ezo and fought at Matsumae,
  then Toshizō SENT HIM AWAY at Matsumae Castle (ch61) with Matsumoto Sutesuke,
  escorting the Matsumae lord's pregnant wife to Edo — Toshizō's device to save
  his life. Do NOT write him into the Ezo endgame unless the source brings him
  back. Historically he never went north (stayed at Aizu); lived to the end of
  Meiji as Yamaguchi/Fujita Gorō, policeman then school clerk. Glossary key
  (principal #11). Recurs only as the "odd man" reminiscence.
- MATSUMOTO SUTESUKE (松本捨助): sent south with Saitō from Matsumae (ch61); given
  ten ryō to Saitō's thirty (he has family and land, Saitō none). Rendered by
  hand, not keyed. Likely gone from the Ezo endgame.
- OYUKI (お雪, given name Yuki, self-refers お雪→"Oyuki", bare 雪→"Yuki"): the
  HEROINE, WHOLLY INVENTED (Shiba's afterword; flagged ch32). Edo-born samurai
  widow, a painter (art-name Kōka). Register: quiet, CRISP Edo/samurai speech,
  refined and formal (でございます), NO Kyoto softness; leave her low-contraction
  speech ALONE at register gates. Toshizō's acknowledged WIFE; deep background
  since ch49. GLOSSARY KEY is お雪 → "Oyuki". MAY RETURN in ch65 再会 "Reunion" —
  handle as fiction, no fact-check.
- KONDŌ ISAMI: DEAD (beheaded Itabashi Keiō 4/4/25; grave raised by Toshizō at
  Aizu Atago-yama). Recurs only in memory. OKITA SŌJI: DEAD (consumption,
  Sendagaya, Keiō 4/5/30); recurs in memory (and appeared in the ch60 sickbed
  FLASHBACK, which is proper). Kyoto-era dead comrades (Itō, Serizawa, Niimi,
  Yamanami, Tōdō Heisuke, Inoue Genzaburō, Yamazaki Susumu, etc.) — DEAD, memory
  only. NAGAKURA and HARADA parted ch53; do not write them north unless the source
  does.

## Renderings settled / carry-forward

- Title "Burn, O Sword!"; author Shiba Ryōtarō. Names Japanese order, macrons.
- ONE rendering per referent, all in glossary.json (302 rows, unchanged in B13).
  RENDER THE DECIDED FORM VERBATIM: 甲陽鎮撫隊 "the Kōyō Chinbutai", 伝習隊 "the
  Denshūtai", 旗本 "hatamoto", 和泉守兼定 "Izumi-no-kami Kanesada", 佐藤彦五郎
  "Satō Hikogorō", お雪 "Oyuki" (bare 雪 = "Yuki"), 近藤勇 "Kondō Isami",
  勝海舟 "Katsu Kaishū", 助勤 "jokin", 副長 "vice-commander", 局長 "commander",
  天然理心流 "the Tennen Rishin-ryū", 誠 "Makoto", 甲鉄 "Kōtetsu", 里 "ri".
- ALIASES: 大久保大和 "Ōkubo Yamato" (Kondō), 内藤隼人 / 内藤先生 "Naitō Hayato"/
  "Naitō-sensei" (Toshizō). Render as given.
- SHIPS (by hand, decided forms): 開陽(丸) "Kaiyō"/"Kaiyō-maru", 回天 "Kaiten",
  蟠竜 "Banryū", 高雄 "Takao", 神速 "Shinsoku", 長鯨 "Chōgei", 大江 "Ōe", 鳳凰
  "Hōō", 甲鉄 "Kōtetsu" (later 東艦 "Azuma"), 春日 "Kasuga", 陽春 "Yōshun",
  第一丁卯 "Teibō No. 1", 飛竜(丸) "Hiryū", 豊安 "Hōan", 戊辰 "Boshin", 晨風
  "Shinpū", 富士山丸 "Fujiyama-maru".
- RENDERED INLINE, NOT KEYED (built chapters / fragile compounds / one-off or
  recurring historical figures). B13 by-hand figures (not keyed): Enomoto Takeaki
  (Izumi-no-kami / Kamajirō / Enbei-son Takeaki), Enomoto Enbei Takenori (father),
  Ōtori Keisuke, Matsudaira Tarō, Arai Ikunosuke, Ichimura Tetsunosuke, Ichimura
  Gōzō, Kōga Gengo, Kōga Magodayū, Yatabori Keizō (later Kō), Kuroda Ryōsuke
  (later Kiyotaka), Ishii Tominosuke, Nakajima Shirō, Kagaya Daizaburō, Ōmura
  Masujirō, Ōkuma Hachitarō (later Shigenobu), Tōgō Heihachirō, Akatsuka Genroku,
  Kuroda Kizaemon, Tanimoto Ryōsuke, Kumasaki Sashichirō, Ogasawara Naganari,
  Yamamoto Gonbee, Nagai Genba-no-kami Naomune (Mondo-no-shō), Hoshi Juntarō,
  Shibusawa Seiichirō, Terasawa Shintarō, Matsumae Takahiro, Matsumae Shima-no-kami
  Norihiro, Shimizudani Kinnaru, Takahashi Sakuzaemon, Inō Tadataka, Nicole,
  Yamaguchi Gorō (= Saitō), Matsumoto Sutesuke, Nomura Risaburō, Ōshima Torao,
  Kasama Kinpachirō, Katō Sakutarō, Itō Yashichi, Miyake Hachigorō, Kawasaki
  Kinjirō, Furuhashi Teizō, Sakai Sennosuke, Sakai Ryōsuke. Place/thing by hand:
  Washinoki, Funka Bay, Hakodate (箱館/函館), Goryōkaku, Kameda, Motomachi,
  Matsumae, Esashi, Bentenjima, Kakkumi, Yunokawa, Tōbetsu, Kikonai, Shiriuchi,
  Fukushima (Matsumae), Ōno-guchi, Hokkeji-yama, Jizō-yama, Tsukishima, Aomori,
  Miyako Bay, Kuji, Same/Same-mura, Yamada Bay, Rotterdam, Dordrecht, The Hague,
  Wetteren, Schleswig, the Merwede, Kōga district / Ōmi, Kakegawa, the Anamon
  squad, the Gatling gun.
- Era-year form kept with the numeral ("Keiō 4", "Meiji 2", "Ansei 2"). 戊辰
  rendered "the year Boshin". Shiba's own modern intrusions and bracketed glosses
  KEPT.
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
- ch49-ch53 (B11): the RETREAT TO EDO; the KŌYŌ CHINBUTAI and KATSUNUMA; the
  split from Nagakura/Harada; the MUSTERING at NAGAREYAMA.
- ch54-ch58 (B12): KONDŌ'S SURRENDER AND EXECUTION and the FINAL PARTING; the
  break-out under ŌTORI; the STORMING OF UTSUNOMIYA; OKITA'S DEATH; Toshizō made
  assistant army commissioner as ENOMOTO's fleet reaches Sendai and Toshizō sails
  for EZO.
- ch59-ch63 (B13): THE SHIFT TO EZO AND THE SEA WAR — the fleet north to
  Washinoki and the taking of Hakodate/Goryōkaku; the page ICHIMURA; the SEIZURE
  OF MATSUMAE CASTLE (Saitō sent away); the Ezo election and the IRONCLAD KŌTETSU;
  the approach to Miyako Bay and the boarding raid readied.

## What is NEXT

- B14 = ch64 to ch68 (kickoff above): 襲撃 / 再会 / 官軍上陸 / 五稜郭 / 砲煙.
  THE CLIMAX — the MIYAKO BAY RAID (Kōga Gengo dies), the government LANDING on
  Ezo, the SIEGE OF GORYŌKAKU, and TOSHIZŌ'S DEATH (Meiji 2/5/11 = 11 June 1869);
  the Ichimura photograph-errand pays off. All Meiji 2 / 1869.
- B15 = ch69 to ch71 back matter (あとがき Afterword / 解説 Commentary by Harada
  Masato / 司馬遼太郎 About the Author) + whole-book reconciliation + COMPLETION.
  THE FINAL batch.

## Open items for the read-through (B14)

- CALENDAR: the whole span is MEIJI 2 (1869). The raid Meiji 2/3/25 = 6 May;
  Toshizō's death Meiji 2/5/11 = 11 June; Goryōkaku's surrender Meiji 2/5/18 =
  27 June (AFTER Toshizō dies). Keep era-years with their numeral.
- TOSHIZŌ'S DEATH SCENE (ch68): the exact spot (near Ippongi-kan / Bentendaiba)
  and the fatal shot are historiographically debated; render the SOURCE's version
  faithfully and footnote the uncertainty. Verify the tail against the source
  explicitly — this is the hero's death and the emotional peak; NEVER invent last
  words or bridging.
- ICHIMURA ERRAND (ch68 area): the photograph/hair/last-message thread set up in
  ch60 pays off; render what the source has, do not pre-empt or embellish.
- OYUKI: may return in ch65 再会 "Reunion". Keep her crisp Edo/samurai register;
  handle as fiction, no fact-check.
- KŌGA GENGO dies in ch64 — memory only thereafter.
- MIYAKO BAY / LANDING / GORYŌKAKU: fact-check the raid's outcome and Kōga's
  death, the government landing (Otobe/Esashi, April–May 1869), the Futamataguchi
  fighting, and the siege and surrender of Goryōkaku; verdicts in the notes.

## Environment / traps state

- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches).
- data/src/ and data/src_epub/ are gitignored (regenerate via ingest if empty);
  scene-break detection needs data/src_epub, so re-run ingest before it if empty.
- SCENE BREAKS: place *** BY TEXT BOUNDARY (grep XHTML for 2+ <p><br/></p> runs);
  scene_map.py's index drifts. Single <br/> = paragraph break; the pair after the
  title = title/body separator. (B13: ch59 NONE internal; ch60–ch63 exactly one.)
- PARITY trap (PROVEN B04-B13): every quote, attribution (と…いった), and silence
  (「………」/「───」) is its own paragraph; a narration lead-in ending in 、 before a
  quote is its own line too (join it for display with {j} on the FOLLOWING line).
  B13 ch62 dropped zh L116「と答えた。」(folded into the lead-in), caught by
  make_bilingual's 149-vs-150 count; a positional re-read split it out. Never add
  or drop a beat; a count mismatch refuses to write, a positional re-read fixes it.
- NUMBER-CHECK traps (confirmed B13): the checker composes BARE tens+ones as words
  ("twenty-six"/"thirty-six"/"fifty-five"/"twenty-one" PASS) and "six thousand"
  and reads ordinals; write DIGITS for thousand-composites ("1,200"/"1,269"/
  "21,374"), hundreds+tens ("180"), and kanji/full-width years; a HYPHENATED
  hundred-compound ("three-hundred-kin") does NOT compose → "three hundred kin";
  keep 里 = "ri" (万里 → "ten thousand ri"); numeral idioms/name-place-ship
  numerals noised; a colloquial elided range (百四、五十) misparses → noise the
  misread fragment, English carries the count. Real koku/troop/date/ton figures
  stay in word- or digit-form and DO carry the number.
- CONTENT/ENTITY trap: render the glossary's DECIDED form verbatim or it flags
  (B13: 局長→"commander" not "commandant" ch60; 副長→"vice-commander" ch62;
  助勤→"jokin" ch63; and restore a shortened full name — pair-30 ch59 needed the
  full "Hijikata Toshizō"). Do NOT key a name in a FRAGILE COMPOUND. NEW glossary
  rows MUST carry both a "section" and a "pinyin" field. check_content matches keys
  by SUBSTRING, so the ch52 alias 近藤勇平 ⊃ 近藤勇 false-flags one paragraph —
  qc_entities does NOT; document it, do not distort the text.
- GLOSSARY CASCADE: adding a global key re-checks EVERY built chapter. Before
  adding, grep data/zh for the key. B13 added NO new keys, so no cascade.
- REGISTER: battle/sea chapters run em-dash LOW and dialogue-light (B13 4–8/1k vs
  12.7 ref). Contract the INFORMAL speakers only (Toshizō's dialect off guard);
  leave formal registers alone (Enomoto, quoted documents, ceremonial court
  speech). A 0.0-contraction chapter reads "little dialogue — noisy" and passes.
  STYLE rule 1 = no PILE-UP (3+ em dashes in a sentence); a single matched PAIR
  bracketing an appositive is allowed. B13: all within tolerance, none STILTED.
- NOTE-ANCHOR trap: the anchor must be a verbatim substring of the reading with
  LITERAL macrons and WITHOUT embedded straight quotes/apostrophes; pick a clean
  run of words. Build notes with a small Python encoder (scripts/build_b13_
  apparatus.py): bodies numeric-ref encoded, <i> tags preserved.
- Known failing test, EXPECTED: tests/run_tests.py reports "hook stands down on
  template stub" FAIL (template-only). Not a translation gate. All other tests
  pass.
- All work is on branch claude/burn-o-sword.
