# HANDOFF, Burn, O Sword! (燃えよ剣), Shiba Ryōtarō

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery: every
batch ends with this file's kickoff block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count. Rewrite it at
the end of every batch; always keep the paste-ready kickoff below as its first
section.

## Message to paste into the next chat

```
Burn, O Sword! B15 (FINAL BATCH)

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then STYLE.md, then book.json. We are translating Burn, O Sword! (燃えよ剣) by Shiba Ryōtarō from a Japanese digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/burn-o-sword; expect the harness to open you on a stray per-task branch and consolidate per CLAUDE.md rule 2. Deliverable out/burn-o-sword.epub.

Batches 1 to 14 are DONE — the whole NOVEL (ch01 to ch68) is translated, annotated, and built; Toshizō dies in ch68 砲煙 and the novel ends （完）. ch01 is the FROZEN register reference: reference/ch01_ref.md. Run ./setup.sh; if data/src/ or data/src_epub/ is empty re-run scripts/ingest_epub.py source.epub (Japanese-aware: strips furigana, substitutes 8 gaiji, writes reference/furigana_readings.tsv). No source-note stream. Keep the source's own cover (data/figs/embed0009_HD.jpg), reused byte-identical, exactly as book.json already sets it; the commissioner likes it, do not change it. The known failing test "hook stands down on template stub" is EXPECTED (template-only); every other test passes. 457 notes so far; glossary 302 rows (no new keys in B14).

B15 is the FINAL batch: the three BACK-MATTER units + whole-book reconciliation + COMPLETION. Run to completion per the CLAUDE.md pipeline; the FINAL batch is planned light but it CLOSES THE BOOK. Units (each a single spine document):
- ch69 あとがき / Afterword (src 73_part0071) — Shiba's OWN afterword. THIS IS WHERE HE STATES OYUKI IS INVENTED; render faithfully, it is the authority behind every "Oyuki is fiction" footnote. First person, essayistic; keep Shiba's voice.
- ch70 解説 / Commentary (src 74_part0072) — 解説──そびえ立つ歴史的遺産『燃えよ剣』を映画化して, by the FILM DIRECTOR Harada Masato (原田眞人), on adapting the novel for the screen (his 2021 film). A signed essay; keep its register; fact-check any historical/film claims lightly.
- ch71 司馬遼太郎 / About the Author (src 75_part0073) — a short publisher's bio of Shiba Ryōtarō (1923–1996). Watch dates/works; fact-check the bio.

For each unit: build data/zh/<id>.txt with scripts/build_zh.py <id> <srcbase> "<title>"; grep the XHTML (data/src_epub/OEBPS/Text/partNNNN.xhtml) for runs of TWO OR MORE consecutive <p><br/></p> to place *** BY TEXT BOUNDARY (the first run per part is the title/body separator; single <br/> is a paragraph break); translate to the FROZEN ch01 register (essay/critical register is EXEMPT from dialogue-contraction expectations — see references/register-drift.md; do not force contractions into an essay); consult reference/furigana_readings.tsv before romanizing ANY name, then glossary.json (302 rows) then authority.json; author out/<id>_reading.md ({j}/{p}/*** as needed) and run the battery bash scripts/check_chapter.sh <id> <srcbase> "<title_en>" (parity refuses on mismatch; --noise data/noise.txt); verify each unit's TAIL against the source; footnotes per the reader model via apparatus_merge.py built from a small encoder like scripts/build_b14_apparatus.py (anchors LITERAL + UNIQUE substrings, bodies numeric-ref encoded, <i> passes through); add commented noise rules for new numbered names/idioms; check_register.py --ref and record in PROGRESS.md.

THEN the FINAL, whole-book steps (CLAUDE.md "Definition of done"):
- WHOLE-BOOK RECONCILIATION: run scripts/check_reconcile.py (repeated-compound rendering drift; glossary-forward usage; spelling-locale pairs); by hand grep-count ~20 decided renderings across ALL built units and confirm first-appearance notes; write out/term_ledger.md (feed decided renderings back into authority.json on completion).
- DEEP AUDIT: random-sample 3–5% deep audit with a FIXED seed; grep the "invented-precision" class; write out/deep_audit.md with an honest error-rate statement.
- Rebuild the EPUB (scripts/build_reading_epub.py) — the TOC should now be CLEAN (no "pending"), coverage sentence FULL (71/71); qa_epub.py green; epubcheck (java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/burn-o-sword.epub) 0/0/0/0.
- Write COMPLETION.md from the scanned template; commit the final EPUB (git add -f out/burn-o-sword.epub); rewrite HANDOFF.md to COMPLETE and do not touch it after. Record everything in PROGRESS.md; commit and push to claude/burn-o-sword.

CALENDAR / CANON reminders for the back matter: the novel's events closed at Meiji 2 (1869) — the Miyako raid 6 May, Toshizō's death Meiji 2/5/11 = 20 JUNE 1869 (NOT 11 June — a lunar-day-as-Gregorian slip; corrected and footnoted in B14 ch68), Goryōkaku's surrender Meiji 2/5/18 = 27 June 1869. Shiba (b. 1923 as Fukuda Teiichi, d. 1996) wrote 燃えよ剣 serialized 1962–1964. Harada Masato's film adaptation is 2021. VERIFY these against real scholarship (never LLM-sourced; IGNORE Grok/Grokipedia); verdicts in the notes.

End the batch with BOTH chat deliverables (CLAUDE.md rule 1, enforced by the Stop hook): the built FINAL EPUB ATTACHED in the chat AND — because this is the LAST batch — a short COMPLETION note IN THE CHAT in place of a next-batch kickoff (state that the book is COMPLETE: 71/71 units, all checks green, and point to COMPLETION.md). There is no B16.

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
- B13 = ch59 to ch63, COMPLETE. Notes 417 to 434.
- B14 = ch64 to ch68, COMPLETE — THE CLIMAX AND THE HERO'S DEATH. ch64 襲撃 /
  "The Attack" (the Miyako Bay raid; the Kaiten alone boards the Kōtetsu; the
  Gatling gun; the raid fails; Kōga Gengo killed), ch65 再会 / "Reunion" (Oyuki
  returns to Toshizō at the Kōnoike house in Hakodate — sent by the dying Okita
  through Yūjirō), ch66 官軍上陸 / "The Imperial Army Lands" (the Otobe landing;
  the parting from Oyuki; the ICHIMURA ERRAND — photograph, sword 和泉守兼定,
  hair, the 小切紙 note signed 義豊, message to Satō Hikogorō; the Futamataguchi
  victory), ch67 五稜郭 / "Goryōkaku" (the Port Arthur digression; the haiku;
  Matsumae/Kikonai fall; the naval annihilation; Nakajima Saburōsuke), ch68 砲煙
  / "Gunsmoke" (the ghost-night; the death sortie; TOSHIZŌ SHOT AND KILLED at the
  Ippongi barrier, Meiji 2/5/11 = 20 June 1869; the Oyuki epilogue; （完）).
  Notes 435 to 457 (23 this batch). All checks green except the ONE documented
  ch52 false-flag. qa_epub PASS (457/457/457); epubcheck 0/0/0/0. Continuous note
  number now 457. Glossary unchanged at 302 rows. 68 of 71 units translated —
  THE WHOLE NOVEL IS DONE; only the 3 back-matter units remain. See PROGRESS.md
  B14 for the full record (scene-break placements, the noise additions, the
  number-check confirmations, the DEATH-DATE correction, and the fact-checks).

## Tooling in place (do NOT revert)

- ingest_epub.py: Japanese-aware (furigana strip, 8 gaiji via
  data/gaiji_map.json, dumps reference/furigana_readings.tsv). From Step 0.
- data/gaiji_map.json: 遼 茨 頤 葛 芦, plus レ (kaeriten) and 㝎 (之定 variant).
- DISPLAY JOIN MARKER {j} (B01, whole-book): a reading line prefixed "{j} " is
  merged onto the preceding display paragraph at BUILD time. Chains. VERSE MARKER
  {p} (one per verse line); also {v}/{d}/{g}. All stripped by the checks.
  reading_to_en.py counts BY LINE; {j}/{p}/*** lines and the ## title are
  handled/skipped, so they are EXTRA (do not consume a source-parity slot).
- scripts/scene_map.py: reports 2+ <p><br/></p> runs, BUT its "body paragraph N"
  index has drifted off-by-one. RELIABLE method: grep the XHTML for the <br/>
  runs and place *** by the TEXT on either side. Needs data/src_epub.
- scripts/reading_to_en.py, check_chapter.sh, apparatus_merge.py, build_zh.py,
  build_reading_epub.py, qa_epub.py — unchanged since B02-B04.
- scripts/build_b14_apparatus.py (B14, adapted from build_b13): the small encoder
  that builds an apparatus JSON from Unicode note bodies — anchors literal +
  UNIQUE, bodies numeric-ref encoded, <i> preserved. Copy/adapt per batch
  (build_b15_apparatus.py). NOTE: an anchor must be a UNIQUE substring of the
  reading (a repeated word like "Shinobirika" appearing twice fails the merge —
  pick a longer run).
- scripts/qc_entities.py (B03 PATCH): SKIPS single-kanji glossary keys. DO NOT
  REVERT. Requires every glossary row to have a "pinyin" field (KeyError without).
- scripts/check_content.py: matches glossary keys by SUBSTRING, so the ch52 alias
  近藤勇平 ⊃ 近藤勇 false-flags one paragraph. qc_entities (the battery gate) does
  NOT; document the false-flag, do not distort the translation.
- scripts/check_numbers.py PATCHES (target-side only, can only ADD a number):
  B04 "a/one hundred and <ten..nineteen>"; B07 folds ONES into the hundred+low
  band. Regression tests pass. DO NOT REVERT. Reach confirmed through B14: composes
  BARE tens+ones as words, "eighty thousand" (八万), "two/three thousand",
  bare hundreds ("eight hundred"), "five hundred and thirty" (530), and reads
  ordinals; but a plain 百 needs an ARTICLE ("about a hundred" PASSES, "some
  hundred" FAILS); write DIGITS for hundreds+tens (150/250), thousand-composites
  (35,000), and kanji/full-width numerals used as place-names (203/613/734);
  keep hundred-compounds UNHYPHENATED ("three hundred kin"); 里 = "ri"; a numeral
  idiom / name-place-ship numeral is noised; an elided range (二十七、八 / 十二、三)
  usually composes if you write both bounds as words.
- data/noise.txt (B01 to B14): commented Japanese name/idiom/place/ship numeral
  rules. Never noise a real quantity. B14 added (all commented): 三陸, 四方八方,
  金八郎, 平八郎 (ch64); 千代田形 (ch65); 伊庭八郎, 心形一刀流, 二股, 二分金,
  百戦練磨 (ch66); 大二郎, 政五郎, 三郎助, 千代ケ岱, 二〇三 (ch67); 一本木, 政一郎
  (ch68).
- STYLE.md (B01): the house style sheet (em-dash budget; scene-primed idioms).
  READ IT each batch. No new rule in B14.
- reference/ch01_ref.md (B01): the FROZEN register reference. Do not edit.

## Voice sheets (one per major character; consult at every dialogue scene)

Most of the cast has now left the stage (dead or sent away). For the BACK MATTER
(B15) the "voice" that matters is Shiba's own essayistic first person (afterword)
and a signed critical essay (commentary) — neither is dialogue; the
register-contraction expectation is EXEMPT (see references/register-drift.md).

- NARRATOR: third person, wry and knowing, fond of the aside and the forward
  glance (B14: the Port Arthur / Russo-Japanese-War digression, Kondratenko and
  Stoessel, Tōgō at Miyako, Ichimura's death in the Seinan War 1877, the modern
  place-names, the quoted Kuroda dispatch). KEEPS Shiba's modern intrusions
  (Western dates; present-day names; the anachronistic "Hokkaidō") and bracketed
  glosses — render as parentheses/commas/square-bracket glosses, do NOT dash them.
- HIJIKATA TOSHIZŌ ("Toshi"): DEAD (ch68, Meiji 2/5/11 = 20 June 1869, shot at
  the Ippongi barrier leading a sortie). Recurs only in memory / the back matter.
  His last self-naming: "Hijikata Toshizō, vice-commander of the Shinsengumi."
- OYUKI (お雪 → "Oyuki", bare 雪 → "Yuki"): the HEROINE, WHOLLY INVENTED (Shiba's
  afterword — ch69 is where he SAYS SO; the ch65 reunion and the ch68 temple-
  offering epilogue are fiction). Crisp Edo/samurai register, refined/formal
  (でございます), low contraction — leave alone at register gates. Died at
  Yokohama (per ch68's close); nothing more known. GLOSSARY KEY お雪 → "Oyuki".
- ENOMOTO TAKEAKI, ŌTORI KEISUKE, MATSUDAIRA TARŌ, ARAI IKUNOSUKE, NAGAI
  NAOMUNE (玄蕃頭): LIVE at the fall; of the eight Ezo ministers only Toshizō was
  killed; four (Enomoto, Arai, Ōtori, Nagai) were pardoned and served the Meiji
  government. Rendered BY HAND, not keyed.
- ICHIMURA TETSUNOSUKE: sent south with the photograph/sword/hair errand (ch66);
  reached the Satō/Hijikata families (ch68, Meiji 2/7); later died in the Seinan
  War 1877. KŌGA GENGO: DEAD (ch64). NAKAJIMA SABUROSUKE: DEAD with his two sons
  at Chiyogatai (ch67, Meiji 2/5/15). All by hand, not keyed.
- KONDŌ ISAMI, OKITA SŌJI, INOUE GENZABURŌ, YAMAZAKI SUSUMU and the Kyoto dead:
  DEAD — memory only (they appear as GHOSTS in ch68's opening, which is proper).
  SAITŌ HAJIME: GONE from the northern story since ch61 (Shiba's fiction); do not
  bring him back.

## Renderings settled / carry-forward

- Title "Burn, O Sword!"; author Shiba Ryōtarō. Names Japanese order, macrons.
- ONE rendering per referent, all in glossary.json (302 rows, unchanged in B14).
  RENDER THE DECIDED FORM VERBATIM: 土方歳三 "Hijikata Toshizō", 近藤勇 "Kondō
  Isami", 沖田総司 "Okita Sōji", 井上源三郎 "Inoue Genzaburō", 山崎烝 "Yamazaki
  Susumu", お雪 "Oyuki" (bare 雪 = "Yuki"), 会津 "Aizu", 武州多摩 "Bushū Tama"
  (NOT "Tamagawa in Bushū"), 甲鉄 "Kōtetsu", 里 "ri", 旗本 "hatamoto", 副長
  "vice-commander", 局長 "commander", 助勤 "jokin", 誠 "Makoto", 新選組
  "the Shinsengumi", 和泉守兼定 "Izumi-no-kami Kanesada", 佐藤彦五郎 "Satō
  Hikogorō".
- SHIPS (by hand, decided forms): 開陽 "Kaiyō", 回天 "Kaiten", 蟠竜 "Banryū",
  高雄 "Takao", 甲鉄 "Kōtetsu" (later 東艦 "Azuma"), 春日 "Kasuga", 陽春 "Yōshun",
  第一丁卯 "Teibō No. 1", 飛竜 "Hiryū", 豊安 "Hōan", 戊辰 "Boshin", 晨風 "Shinpū",
  富士山丸 "Fujiyama-maru", 朝陽 "Chōyō", 千代田形 "Chiyodagata".
- B14 by-hand figures (NOT keyed): Kōga Gengo, Ōtsuka Namijirō, Nomura Risaburō,
  Kasama Kinpachirō, Katō Sakutarō, Shingū Isamu, Tōgō Heihachirō, Ogasawara
  Naganari, Sawa Chūsuke, Yamatoya Yūjirō, Kōnoike Zen'emon, Iba Hachirō (bro
  Sōtarō), Yoshizawa Daijirō, Komai Masagorō, Nakajima Saburōsuke (sons Kōtarō,
  Eijirō), Tachikawa Chikara (later Takabayashi Kyokai), Shimada Kai, Ozeki
  Masaichirō, Hoshi Juntarō, Anzai Kichizaemon, Enomoto Takeaki, Ōtori Keisuke,
  Matsudaira Tarō, Arai Ikunosuke, Nagai Naomune, Kuroda Ryōsuke→Kiyotaka,
  Ichimura Tetsunosuke. Places by hand: Miyako Bay, Cape Heizaki, Sanriku,
  Shinagawa, Cape Inubō, Otobe, Esashi, Futamataguchi (Naka-/Shimo-Futamata,
  Nakayama Pass, Uzuragoe), Hakamagoshi-yama, Katsuradake, Kikonai, Matsumae,
  Yafurai, Muroran, Washinoki, Mori, Sawara, Kakkumi, Arikawa, Tōbetsu,
  Bentenzaki, Chiyogatai, Mount Hakodate, Ippongi (barrier), Eikoku Bridge,
  Jizō-machi, Tsukishima, Kameda, Goryōkaku, Aomori, Yokohama, Uraga, Nōryō-ji,
  Shōmyō-ji, Yūhigaoka, Ishida, Hino, Ōgaki, Port Arthur / 203-Meter Hill.
  Kaimyō: 歳進院殿誠山義豊大居士 "Saishin'in-den Seizan Gihō Daikoji"; imina 義豊
  "Yoshitoyo".
- Era-year form kept with the numeral ("Meiji 2", "Kaei 6"). 戊辰 "the year
  Boshin". Shiba's modern intrusions and bracketed glosses KEPT.
- ★ CORRECTED FACT (carry into the back matter & COMPLETION): TOSHIZŌ DIED
  Meiji 2/5/11 = 20 JUNE 1869 (Gregorian), NOT 11 June — the kickoff's "11 June"
  was a lunar-day-as-Gregorian slip; footnoted in ch68. Goryōkaku surrendered
  Meiji 2/5/18 = 27 June 1869.
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
- ch34-ch38 (B08): the ITŌ SPLIT; the Goryō-eji; Saitō planted; the TAISEI HŌKAN.
- ch39-ch43 (B09): the ABURANOKŌJI killing; the ŌSEI FUKKO; Kondō SHOT; the war.
- ch44-ch48 (B10): TOBA-FUSHIMI; YOSHINOBU'S FLIGHT; the two nights with OYUKI.
- ch49-ch53 (B11): the RETREAT TO EDO; the KŌYŌ CHINBUTAI and KATSUNUMA; the split.
- ch54-ch58 (B12): KONDŌ'S EXECUTION; the break-out; UTSUNOMIYA; OKITA'S DEATH;
  Toshizō sails for EZO.
- ch59-ch63 (B13): THE SHIFT TO EZO — Hakodate/Goryōkaku taken; ICHIMURA enters;
  MATSUMAE CASTLE; the IRONCLAD KŌTETSU; the boarding raid readied.
- ch64-ch68 (B14): THE CLIMAX — the MIYAKO BAY RAID (Kōga Gengo dies); OYUKI'S
  RETURN; the LANDING and the ICHIMURA ERRAND; FUTAMATAGUCHI and the fall of the
  fleet; and TOSHIZŌ'S DEATH at the Ippongi barrier (Meiji 2/5/11 = 20 June
  1869). （完） — the novel ends.

## What is NEXT

- B15 = ch69 to ch71 back matter (kickoff above): あとがき Afterword (Shiba —
  states Oyuki is invented), 解説 Commentary (Harada Masato, on the film),
  司馬遼太郎 About the Author. PLUS the whole-book steps: check_reconcile.py,
  out/term_ledger.md (feed authority.json), out/deep_audit.md (fixed-seed 3–5%),
  CLEAN TOC + FULL coverage rebuild, COMPLETION.md. THE FINAL BATCH — it closes
  the book; end with the FINAL EPUB attached and a COMPLETION note in the chat
  (no next kickoff — there is no B16).

## Open items for the read-through (B15)

- BACK-MATTER REGISTER: the afterword and commentary are ESSAYS, not narrative;
  keep the author's/critic's own first-person voice; the dialogue-contraction
  expectation is EXEMPT (references/register-drift.md). Do not force contractions.
- ch69 あとがき: Shiba's authority for the Oyuki-is-fiction footnotes — render it
  faithfully and completely; verify its tail (rule 4).
- ch70 解説: signed by the film director Harada Masato (原田眞人); about his 2021
  adaptation. Fact-check film/historical claims lightly; verdicts in notes.
- ch71 About the Author: a short bio of Shiba (Fukuda Teiichi, 1923–1996);
  verify the dates and the list of works.
- RECONCILIATION: grep-count ~20 decided renderings across ALL built units; check
  first-appearance notes; term_ledger + deep_audit; then feed authority.json.

## Environment / traps state

- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches).
- data/src/ and data/src_epub/ are gitignored (regenerate via ingest if empty);
  scene-break detection needs data/src_epub, so re-run ingest before it if empty.
- SCENE BREAKS: place *** BY TEXT BOUNDARY (grep XHTML for 2+ <p><br/></p> runs);
  scene_map.py's index drifts. (B14: every one of ch64-ch68 had exactly ONE
  internal ***.)
- PARITY trap (PROVEN B04-B14): every quote, attribution (と…いった), and silence
  (「………」/「───」) is its own paragraph; a narration lead-in ending in 、 before a
  quote is its own line too (join it for display with {j} on the FOLLOWING line).
  A count mismatch refuses to write; a positional re-read fixes it.
- NUMBER-CHECK traps (confirmed B14): plain 百 needs an ARTICLE ("about a
  hundred" PASS, "some hundred" FAIL); write DIGITS for hundreds+tens and
  thousand-composites and place-name numerals (203/613/734); keep hundred-
  compounds UNHYPHENATED; elided ranges compose if BOTH bounds are words; real
  koku/troop/date/ton figures carry the number.
- CONTENT/ENTITY trap: render the glossary's DECIDED form verbatim or it flags
  (B14: お雪→"Oyuki" not a pronoun; 武州多摩→"Bushū Tama" not "Tamagawa in
  Bushū"). qc_entities is the GATE (clean); check_content's ch52 substring
  false-flag stands — document, do not distort.
- NOTE-ANCHOR trap: the anchor must be a verbatim UNIQUE substring of the reading
  with LITERAL macrons/kana and WITHOUT embedded straight quotes/apostrophes; a
  repeated word (B14: "Shinobirika" x2) fails the merge — pick a longer run.
- REGISTER: battle/narration and ESSAY chapters run em-dash LOW and dialogue-
  light and pass ("little dialogue — noisy"); contract only INFORMAL speakers;
  leave formal registers and essays alone. STYLE rule 1 = no PILE-UP (3+ em
  dashes in a sentence); a single matched PAIR bracketing an appositive is
  allowed; the source's ── interruptions render as a leading U+2500, not counted.
- Known failing test, EXPECTED: tests/run_tests.py "hook stands down on template
  stub" FAIL (template-only). Not a translation gate. All other tests pass.
- All work is on branch claude/burn-o-sword.
```
