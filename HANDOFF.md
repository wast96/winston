# HANDOFF, Burn, O Sword! (燃えよ剣), Shiba Ryōtarō

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery: every
batch ends with this file's kickoff block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count. Rewrite it at
the end of every batch; always keep the paste-ready kickoff below as its first
section.

## Message to paste into the next chat

```
Burn, O Sword! B08

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then STYLE.md, then book.json. We are translating Burn, O Sword! (燃えよ剣) by Shiba Ryōtarō from a Japanese digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/burn-o-sword; expect the harness to open you on a stray per-task branch and consolidate per CLAUDE.md rule 2. Deliverable out/burn-o-sword.epub.

Batches 1 to 7 are DONE (ch01 to ch33). ch01 is the FROZEN register reference: reference/ch01_ref.md. Run ./setup.sh; if data/src/ is empty re-run scripts/ingest_epub.py source.epub (Japanese-aware: strips furigana, substitutes 8 gaiji, writes reference/furigana_readings.tsv). No source-note stream. Keep the source's own cover (data/figs/embed0009_HD.jpg), reused byte-identical, exactly as book.json already sets it; the commissioner likes it, do not change it. The known failing test "hook stands down on template stub" is EXPECTED (it only passes on the template placeholder kickoff); every other test passes.

Do Batch 8 = ch34 through ch38 (与兵衛の店 / Yohei's Place; 二条中洲の決闘 / The Duel at Nijō Nakasu; 菊章旗 / The Chrysanthemum Banner; お雪と / With Oyuki; 江戸日記 / Edo Diary), end to end per the CLAUDE.md pipeline, RUN TO COMPLETION. This span carries the ITŌ FACTION SPLIT gathering (the Kōdai-ji / Goryō-eji breakaway and the road to the Aburanokōji killing of 1867 — fact-check dates in the notes), OYUKI's continuation (ch37 お雪と; she is the invented heroine, flagged at ch32 — handle as fiction, no fact-check of her existence), and Edo material (ch38). Do not stop mid-batch except for a genuine blocker or completion. For each chapter:
1. Build data/zh/<id>.txt from data/src with scripts/build_zh.py <id> <srcbase> "<title>" (title line "### <title>" then one body line per non-empty source paragraph, skipping the first two header lines). ch34=38_part0036, ch35=39_part0037, ch36=40_part0038, ch37=41_part0039, ch38=42_part0040. Fix any extractor splits (this source has had none: a narration line ending in 、 before a 「quote」 is the source's own lead-in, handled by the {j} join, NOT a split to merge). Recover scene breaks: the RELIABLE method is to grep the XHTML (data/src_epub/OEBPS/Text/partNNNN.xhtml) for runs of TWO OR MORE consecutive <p><br/></p> in the body and read the text on either side of each run — scripts/scene_map.py reports the same runs by "body paragraph N" but its N has drifted off-by-one against later chapters, so PLACE *** BY TEXT BOUNDARY, not by the reported index (the single pair right after the chapter title is only the title/body separator; a SINGLE <br/> is a paragraph break, not a scene break). Place *** in the reading at those points.
2. Translate to the FROZEN ch01 register. Names Japanese order, surname first, macrons; CONSULT reference/furigana_readings.tsv before romanizing ANY name or word (it caught Rokusha/Momonoi in B02, Yamanami-not-Sannan in B03, Toshima/Mikura/Akazawa/Kujō in B04, Matsubara-an/Yoshimaro/Mizuo/Tantora in B05, Tojima/Makita/Kijima in B06, and in B07: 明里→あけさと Akesato, 尚志→なおむね Naomune not Naoyuki, 恩智左近→おんじのさこん Onji Sakon, 豊玉→ほうぎょく Hōgyoku, 常州→じょうしゅう but rendered "Hitachi" — see traps; note the source also uses EXPRESSIVE gikun furigana like 将軍→たいじゅ, 京→ここ, 近藤→せんせい, which are semantic glosses, NOT phonetic, and must not be romanized), and consult glossary.json (280 rows; then authority.json) first, feeding decided renderings back. Use the {j} display-join marker so a quotation reads inline with its lead-in and attribution; verse lines take {p} (one per line). Keep an exchange one paragraph per speaker turn. Watch parity: every 「…」 quote line, every と…いった attribution line, and every 「………」 silence is its OWN source paragraph and needs its OWN reading line — B04-B07 each dropped/merged lines in dialogue and narration seams (B07 collapsed a lead-in + 「ぜひ」 + attribution into one paragraph in ch31; make_bilingual's count caught it). ALWAYS re-check dense exchanges and run-on narration for count. OBEY STYLE.md (em-dash budget; no scene-primed idioms). Consult the voice sheets below; read the last two pages of ch33's English before starting ch34 (batch seam).
3. Author out/<id>_reading.md (## title, {j}, {p}, ***, blank-separated). Then the battery: bash scripts/check_chapter.sh <id> <srcbase> "<title_en>" runs reading_to_en + make_bilingual (parity refuses on mismatch) + verify_unit (--noise data/noise.txt) + gen_check_config + check_align + check_content + qc_entities + check_apparatus + check_register. Verify each chapter TAIL against the source explicitly (rule 4).
4. Footnotes per the reader model (first-appearance discipline; keep the "NOT re-noted" ledger in PROGRESS.md; note MORE than the glossary row) via apparatus_merge.py (each glossary row MUST carry a "section": people|places|organizations|terms field; the merge nests it and check_apparatus stays clean; render the glossary's DECIDED form verbatim, e.g. 外島機兵衛→"Toshima Kihee", 常州→"Hitachi", or qc_entities/check_content flag it; when the source shortens a name give the glossary a bare-surname en, and do NOT key a name that appears in FRAGILE COMPOUNDS — a Kyoto street like 坊城通/三条通 is rendered by hand ("the Bōjō avenue" / "the Sanjō avenue"), NOT keyed, or 坊城通四条 false-flags). A NOTE ANCHOR must be a verbatim substring of the reading file with LITERAL macrons (ō, not sh&#333;gi); note BODIES use numeric character references for &-entities. Any figure from data/figs/ with a translated caption and real alt text (ch24-33 had none).
5. check_register.py --ref reference/ch01_ref.md out/<id>_reading.md; record in PROGRESS.md. If a chapter flags STILTED, add contractions to the INFORMAL speakers (Toshizō's blunt dialect, Kondō's intimate Bushū) ONLY — leave deliberately formal registers (Itō's set-piece debate, a ceremonial official, quoted documents) alone (ch33 needed this). Fact-check historical claims against real scholarship (never LLM-sourced; IGNORE Grok/Grokipedia), verdict in the note. Add numeral-noise rules to data/noise.txt as new numbered names/idioms/place-names appear (comment each; never noise a real quantity; and use spelled forms the checker parses — "a hundred or so", and for 3-digit tallies write "one hundred and two", NOT "a hundred and two").
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck (java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/burn-o-sword.epub); record ALL check results and EVERY digitization glitch in PROGRESS.md; update HANDOFF.md; commit and push to claude/burn-o-sword.

End the batch with BOTH chat deliverables (CLAUDE.md rule 1, enforced by the Stop hook): the built EPUB ATTACHED in the chat AND the Batch 9 kickoff PASTED VERBATIM in a fenced code block. Batch 9 = ch39 through ch43.

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
- B07 = ch29 to ch33, COMPLETE. ch29 憎まれ歳三 / "Toshizō the Hated" (Yamanami's
  seppuku, Okita his second), ch30 四条橋の雲 / "Clouds over Shijō Bridge" (the
  French-style reorganization, Itō made staff officer, the Satchō alliance
  foreshadowed, Toshizō's haiku), ch31 堀川の雨 / "Rain on the Horikawa"
  (Toshizō's romantic history, the Osae/Shichiri betrayal reveal, the night
  ambush), ch32 お雪 / "Oyuki" (the INVENTED heroine's entrance), ch33 紅白 /
  "Red and White" (Kondō and the jikisan offer, the resolve to apply the Code to
  Itō). Notes 209 to 234 (26 this batch). All checks green; qa_epub PASS
  (234/234/234); epubcheck 0/0/0/0. Continuous note number now 234. Glossary 280
  rows. 33 of 71 chapters translated. See PROGRESS.md B07 for the full record:
  the ch31 parity miss, the number fixes, the check_numbers gate patch, the
  常州→Hitachi cascade (ch27 edited), the ch33 register-contraction pass, and the
  ten fact-check verdicts.

## Tooling in place (do NOT revert)

- ingest_epub.py: Japanese-aware (furigana strip, 8 gaiji via
  data/gaiji_map.json, dumps reference/furigana_readings.tsv). From Step 0.
- data/gaiji_map.json: 遼 茨 頤 葛 芦, plus レ (kaeriten) and 㝎 (之定 variant).
- DISPLAY JOIN MARKER {j} (B01, whole-book): a reading line prefixed "{j} " is
  merged onto the preceding display paragraph at BUILD time. Chains (consecutive
  {j} lines fold onto the same growing paragraph). VERSE MARKER {p} (one per
  verse line, indented italic); also {v}/{d}/{g} for vignette/dateline/hourgloss.
  All are stripped by the parity / number / entity / content checks.
- scripts/scene_map.py: reports 2+ <p><br/></p> runs, BUT its "body paragraph N"
  index has drifted off-by-one on later chapters (a dropped empty/ruby paragraph
  upstream). RELIABLE method: grep the XHTML for the <br/> runs and place *** by
  the TEXT on either side (see the ch33 procedure in PROGRESS). Needs
  data/src_epub (re-run ingest if empty).
- scripts/reading_to_en.py, check_chapter.sh, apparatus_merge.py, build_zh.py,
  build_reading_epub.py, qa_epub.py — unchanged since B02-B04.
- scripts/qc_entities.py (B03 PATCH): SKIPS single-kanji glossary keys. DO NOT
  REVERT.
- scripts/check_numbers.py PATCHES (target-side only, can only ADD a number):
  * B04: spelled_numbers reads "a/one hundred and <ten..nineteen>" (110-119).
  * B07: spelled_numbers now folds ONES into the hundred+low band, so
    "one hundred and two" = 百二 (102) maps — the 101-109 gap the checker used to
    skip. Write "one hundred and N", NOT "a hundred and N" (the rule keys on
    "one"/digit words). Regression tests pass with this. DO NOT REVERT.
- data/noise.txt (B01 to B07): Japanese name/idiom/place numeral rules, each
  commented. Add more as numbered names / teen-elisions / place-names appear.
  Never noise a real quantity. B07 added: 十郎, 小三郎, ナポレオン三世, 九州
  (ch30); 七条, 八軒家, 万が一 (ch31); 十津川, 三巴 (ch32).
- STYLE.md (B01): the house style sheet (em-dash budget; scene-primed idioms).
  READ IT each batch; add to it when the commissioner corrects a line. No new
  rule in B07.
- reference/ch01_ref.md (B01): the FROZEN register reference. Do not edit.

## Voice sheets (one per major character; consult at every dialogue scene)

- NARRATOR: third person, wry and knowing, fond of the aside and the forward
  glance to events years ahead. Long descriptive sentences alternating with very
  short flat ones. KEEPS Shiba's own modern parentheticals (Western dates; the
  present-day place-names; quoted real letters, diaries, memoirs — Nagakura,
  and in B07 Tanaka Mitsuaki's cited reminiscence of fearing Hijikata, ch32).
  KEEP them all.
- HIJIKATA TOSHIZŌ ("Toshi"): the hero, 22 to 30. Rough Bushū farm dialect off
  guard, contracted and blunt. Cool, laconic, a dandy, a natural tactician,
  class-obsessed, the cold ENGINE of the corps; cruelty matter-of-fact. His one
  soft spot was his SECRET HAIKU (pen-name Hōgyoku, 豊玉, known only to Okita) —
  and now, from B07, OYUKI: at the end of ch32 he tells Okita, for the first time
  ever of a woman, "I've fallen for a woman." He calls himself "a brawler" and a
  "craftsman" who wants only to raise the corps into the first fighting-band
  under heaven. Reads Itō as the real danger; treats his own unpopularity ("the
  hated") as the vice-commander's proper burden — he takes the hatred so Kondō
  stays loved.
- KONDŌ ISAMI: warm, plain, big-jawed Bushū farmer's son; slow, generous,
  weeps easily; calls Toshizō "Toshi"; Bushū dialect. GROWN VAIN since Edo
  (B06): plays the daimyō, dreams of rank; outshone by Itō and pained to be
  thought unlettered. In B07 he leans hard on Itō, chants the Nihon Gaishi and
  casts himself as Kusunoki Masashige, and is wooed by the rōjū Ogasawara toward
  becoming a direct shogunal retainer (jikisan) — which forces the break with
  Itō. At ch33's end he resolves to apply the Code to Itō. Keeps women lavishly
  (Kōnoike money). Sword: the Kotetsu.
- OKITA SŌJI: 20 to 22, Edo-born, the corps' finest blade. Bright, boyish, glib,
  teasing, cool as ice in a fight; the ONE who knows Toshizō's haiku and heart;
  a picky eater. His CONSUMPTION is now overt — in B07 (ch29) he coughs blood in
  the saddle on the ride after Yamanami and thinks "I too may not have long."
  He was Yamanami's second at the seppuku. Toshizō confides Oyuki to him alone.
- YAMANAMI KEISUKE: DEAD (ch29 seppuku, Okita his second, Keiō 1). Do not write
  him as a living voice past ch29.
- ITŌ KASHITARŌ: pale, handsome, refined, an actor's looks; a Kokugaku scholar
  and Hokushin Ittō-ryū master; a topple-the-shogunate ideologue inside the
  corps. In B07 made STAFF OFFICER (参謀, a grand empty title, no command), his
  faction seated where they can do least harm; he writes textbook tanka, courts
  the Chōshū men, and on the Hiroshima trip (ch33) secretly learns of the Satchō
  alliance and resolves on 討幕, declaring he will raise "a righteous corps"
  cutting loose from Kondō and Toshizō. Educated Edo speech, "-kun"/"-san". The
  Kōdai-ji breakaway (Goryō-eji) and the Aburanokōji killing (1867) are AHEAD
  (B08+). His faction: Shinohara Tainoshin, Hattori Takeo, Kanō Michinosuke,
  Sano Shimenosuke, Nakanishi Noboru, Utsumi Jirō, and his brother Suzuki
  Mikisaburō.
- OYUKI (お雪, given name Yuki): NEW in B07 (ch32), the HEROINE and the one
  WHOLLY INVENTED character (Shiba's afterword; flagged in the apparatus at
  ch32). An Edo-born samurai widow (of a fictional Ōgaki foot-guard, Kada
  Shinjirō) living alone in Kyoto, a painter (art-name Kōka) of the
  Shijō-Maruyama school; her family are Kan'ei-ji temple-officials. Register:
  quiet, few wasted words, quick-witted, CRISP Edo/samurai speech with NO Kyoto
  accent (the very thing that draws Toshizō — an Edo savor he had forgotten; she
  commands rather than coaxes). Reserved bearing, plain warmth in the eyes. She
  wears no honorific-heavy Kyoto softness. She recurs to the end (ch37 お雪と is
  next). By the same left-mitsudomoe crest, an omen is planted at their meeting.
- HARADA SANOSUKE: hot-blooded Iyo spearman, risen from chūgen stock, a
  belly-scar from an old half-botched suicide; rough, animal-loyal to Kondō.
- SHICHIRI KENNOSUKE: the early antagonist, an iai master, cold mocking eyes, a
  RUSTY / shrill kan-high voice; Chōshū ties. In B07 (ch31-32) he ambushed
  Toshizō twice on the Horikawa by night with a Totsukawa hireling and a ring of
  drifters, sheltered (Toshizō guesses) in the Tosa or Satsuma mansion, and
  ESCAPED AGAIN. "Hijikata is mine to deal with." STILL AT LARGE.
- OSAE (佐絵 / お佐絵): the Fuchū shrine-daughter Toshizō loved in Bushū. B07
  (ch31) REVEALED she betrayed him: in Kyoto she took the Chōshū man Yonezawa
  Tōji for a lover, told him "I know Hijikata," and he set Shichiri on the
  Nijōhanjiki-chō ambush. Her tie to the plotters is live.
- KATSURA KOGORŌ (= Kido Takayoshi): the Chōshū Kyoto agent, cool, lucky; a
  signer of the Satchō alliance (ch33). Recurring survivor; diary quoted as real.
- SERIZAWA KAMO, NIIMI NISHIKI, KIYOKAWA HACHIRŌ: DEAD. Do not revive.

## Renderings settled / carry-forward

- Title "Burn, O Sword!"; author Shiba Ryōtarō. Names Japanese order, macrons.
- ONE rendering per referent, all in glossary.json (280 rows). Enforced by
  check_content and qc_entities. RENDER THE DECIDED FORM VERBATIM: e.g. 旗本 ->
  "hatamoto", 武州多摩 -> "Bushū Tama", 京都守護職 -> "the Kyoto Protector",
  所司代 -> "the Shoshidai", 総長 -> "general secretary", 参謀 -> "staff
  officer", 助勤 -> "jokin", 監察 -> "inspector", 局中法度 -> "the Code of the
  Corps", 外島機兵衛 -> "Toshima Kihee" (furigana とじま but glossary keeps
  Toshima).
- B07 settled forms. People: Chiba Shūsaku, Takeda Kōunsai (NOT Kanryūsai),
  Tanuma Genba-no-kami, Akesato, Tanaka Tosa, Shinonome-dayū, Yonezawa Tōji,
  Kōnoike Zen'emon, Ōtani Gyōbu, Tōkichi, Matsubara Chūji, Yoshimura Kan'ichirō,
  Katsu Kaishū, Matsudaira Yoshinaga, Go-Daigo, Onji Sakon, Nagai Naomune,
  Shishido Bingo-no-suke, Yamagata Hanzō, Léon Roches, Hōgyoku (豊玉), Oyuki
  (お雪, PRINCIPAL cast_order 12), Kada Shinjirō, Tanaka Mitsuaki, Yoshida Ryōdō,
  Ogasawara Iki-no-kami, Saigō Kichinosuke, Hirosawa Hyōsuke. Kanō 鵰雄 (roster
  variant) = "Kanō Michinosuke" (same man as the B06 key 加納道之助). 木戸孝允 =
  "Kido Takayoshi" (rendered inline, no key; = Katsura Kogorō). Places: Tsuruga,
  Echizen, Kaga, Raikō-ji, Mount Tsukuba, Hitachi (常州 — NOT "Jōshū"; see
  traps), Ōtsu, the Maekawa mansion, Himeji, Ōgaki (大垣), Totsukawa, Kuwana,
  Karatsu, Bakan. Terms: Nihon Gaishi.
- KYOTO STREETS use "the X avenue" (established: the Bōjō avenue, the Sanjō
  avenue, Horikawa Avenue), NOT "X-dōri". Not glossary-keyed (fragile compounds).
- Era-year form kept with the numeral ("the first year of Keiō", "Keiō 2").
  Shiba's own modern intrusions KEPT.
- COVER: keep data/figs/embed0009_HD.jpg byte-identical, as book.json sets it.
- Principal Characters page flags: Hijikata (1), Kondō (2), Okita (3), Inoue
  (4), Nagakura (5), Shichiri (6), Harada (7), Katsura (8), Yamanami (9),
  Serizawa (10), Saitō Hajime (11), OYUKI (12, added B07).

## Where the book stands (story)

- ch01 to ch07 (B01-B02): the Tama-country prologue; the core cast assembles.
- ch08 to ch13 (B03): the dōjō ruined by epidemic; the Rōshigumi; Kyoto at Mibu.
- ch14 to ch18 (B04): the founding; the name SHINSENGUMI (1863); the Serizawa
  purge. Kondō sole head; Toshizō the cold engine.
- ch19 to ch23 (B05): the CODE OF THE CORPS; the IKEDAYA INCIDENT (1864).
- ch24 to ch28 (B06): the KINMON / HAMAGURI GATE INCIDENT; Kondō's vanity; ITŌ
  recruited; YAMANAMI deserts (New Year, Keiō 1).
- ch29 to ch33 (B07): YAMANAMI'S SEPPUKU (Okita his second). The corps recast on
  the FRENCH model, Itō made STAFF OFFICER. Toshizō's incapacity for love laid
  bare (the tayū Shinonome; the Osae betrayal), then OYUKI enters — the one
  woman he falls for. The SATCHŌ ALLIANCE is sealed (Jan 1866), unknown to the
  corps; Itō, learning of it on the Hiroshima trip, turns to 討幕. Kondō is wooed
  toward becoming a DIRECT SHOGUNAL RETAINER (jikisan), which forces the coming
  break with Itō; at ch33's end Kondō resolves to apply the Code to him.

## What is NEXT

- B08 = ch34 to ch38 (kickoff above): 与兵衛の店 (Yohei's Place); 二条中洲の決闘
  (The Duel at Nijō Nakasu); 菊章旗 (The Chrysanthemum Banner); お雪と (With
  Oyuki); 江戸日記 (Edo Diary). Then B09 ch39-43, B10 ch44-48, B11 ch49-53, B12
  ch54-58, B13 ch59-63, B14 ch64-68, B15 ch69-71 back matter + whole-book
  reconciliation + COMPLETION.

## Open items for the read-through (B08)

- The ITŌ SPLIT: the Kōdai-ji / Goryō-eji breakaway and the road to the
  Aburanokōji killing (1867). Fact-check the Goryō-eji formation and the
  Aburanokōji Incident dates in the notes; watch the faction roster.
- ch35 二条中洲の決闘 (a duel) — follow the set-piece; watch parity in the fight.
- ch36 菊章旗 (the Chrysanthemum Banner) — likely the imperial brocade banner /
  the drift toward the Restoration war; fact-check any dates.
- ch37 お雪と (With Oyuki) — the heroine continues; watch her Edo/samurai
  register (crisp, commanding, no Kyoto softness), and keep her rendered "Oyuki".
- ch38 江戸日記 (Edo Diary) — Edo material; watch for quoted-document register
  (exempt from the contraction target).

## Environment / traps state

- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches).
- data/src/ and data/src_epub/ are gitignored (regenerate via ingest if empty);
  scene-break detection needs data/src_epub, so re-run ingest before it if empty.
- SCENE BREAKS: place *** BY TEXT BOUNDARY. Grep the XHTML for 2+ <p><br/></p>
  runs and read the paragraphs on either side; scene_map.py's index has drifted
  off-by-one on later chapters. A single <br/> is a paragraph break, not a scene
  break; the pair right after the title is the title/body separator.
- PARITY trap, PROVEN AGAIN in B07 (ch31): the source sets every quote,
  attribution (と…いった), and silence (「………」) as its own paragraph, AND a
  narration lead-in ending in 、 before a quote is its own line too. B07 miss:
  ch31 merged the lead-in + 「ぜひ」 + attribution (3 lines → 1). make_bilingual's
  count refused it; a positional re-read located it. ALWAYS re-check dense
  exchanges AND run-on narration for count.
- NUMBER-CHECK traps: name/place/fabric numerals each take a commented noise
  rule (B07 added 十郎, 小三郎, ナポレオン三世, 九州, 七条, 八軒家, 万が一, 十津川,
  三巴); write 3-digit tallies as "one hundred and two" (the checker keys on
  "one"/digits, not "a"); "one hundred thousand" not "a hundred thousand"; real
  koku/troop/date/age/measure figures stay in the English word-forms.
- CONTENT/ENTITY trap: render the glossary's decided form verbatim; a REVERSED
  name flags (ch31 "Toshizō Hijikata" -> "Hijikata Toshizō"). Do NOT key a name
  that appears in a FRAGILE COMPOUND (Kyoto streets 坊城通四条 etc. — render by
  hand). SUBSTRING COLLISION both ways (お佐絵 contains 佐絵 — do not key the bare
  form).
- GLOSSARY CASCADE: adding a global key re-checks EVERY built chapter. Before
  adding, grep data/zh for the key across chapters; if an old chapter rendered it
  differently, either match the old form or edit the old chapter + re-derive (B07
  unified 常州 -> "Hitachi", editing ch27). 常州 is "Hitachi", NOT "Jōshū" (which
  is reserved for 上州 = Kōzuke, to avoid the two-provinces-one-romanization
  collision).
- REGISTER: if a chapter flags STILTED, contract the INFORMAL speakers only
  (Toshizō's dialect, Kondō's intimate Bushū); leave deliberately formal
  registers alone (Itō's debate, a ceremonial official, quoted documents). ch33
  needed this.
- NOTE-ANCHOR trap: the anchor must be a verbatim substring of the reading with
  LITERAL macrons; a note body uses numeric refs for &-entities only. Anchors
  are matched pre-marker-strip, so an anchor inside a {p}/{j} line is fine as
  long as it does not include the marker itself.
- Known failing test, EXPECTED: tests/run_tests.py reports "hook stands down on
  template stub" FAIL (template-only). Not a translation gate. All other tests
  pass.
- All work is on branch claude/burn-o-sword.
