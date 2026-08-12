# HANDOFF, Burn, O Sword! (燃えよ剣), Shiba Ryōtarō

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery: every
batch ends with this file's kickoff block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count. Rewrite it at
the end of every batch; always keep the paste-ready kickoff below as its first
section.

## Message to paste into the next chat

```
Burn, O Sword! B04

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then STYLE.md, then book.json. We are translating Burn, O Sword! (燃えよ剣) by Shiba Ryōtarō from a Japanese digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/burn-o-sword; expect the harness to open you on a stray per-task branch and consolidate per CLAUDE.md rule 2. Deliverable out/burn-o-sword.epub.

Batches 1, 2 and 3 are DONE. ch01 is the FROZEN register reference: reference/ch01_ref.md. Run ./setup.sh; if data/src/ is empty re-run scripts/ingest_epub.py source.epub (Japanese-aware: strips furigana, substitutes 8 gaiji, writes reference/furigana_readings.tsv). No source-note stream. Keep the source's own cover (data/figs/embed0009_HD.jpg), reused byte-identical, exactly as book.json already sets it; the commissioner likes it, do not change it. The known failing test "hook stands down on template stub" is EXPECTED (it only passes on the template placeholder kickoff); every other test passes.

Do Batch 4 = ch14 through ch18 (ついに誕生 / Born at Last; 四条大橋 / Shijō Great Bridge; 高瀬川 / The Takase River; 祇園「山の尾」/ The Yamanoo in Gion; 士道 / The Warrior's Code), end to end per the CLAUDE.md pipeline, RUN TO COMPLETION. Do not stop mid-batch except for a genuine blocker or completion. For each chapter:
1. Build data/zh/<id>.txt from data/src (title line "### <title>" then one body line per source paragraph; the mechanical build has been: skip the first two header lines, keep non-empty lines). Fix any extractor splits (this source has had none: a narration line ending in 、 before a 「quote」 is the source's own lead-in, handled by the {j} join, NOT a split to merge). Recover scene breaks with scripts/scene_map.py OEBPS/Text/partNNNN.xhtml (a run of TWO OR MORE consecutive <p><br/></p> in the body is a break; the single pair after the title is only the title/body separator). Place *** in the reading at those points.
2. Translate to the FROZEN ch01 register. Names Japanese order, surname first, macrons; CONSULT reference/furigana_readings.tsv before romanizing ANY name or word (it caught Rokusha/Momonoi in B02 and Tobari Fushigorō / Yamanami-not-Sannan in B03; note the source also uses EXPRESSIVE gikun furigana like 将軍→たいじゅ, 京→ここ, 近藤→せんせい, which are semantic glosses, NOT phonetic, and must not be romanized), and consult glossary.json (then authority.json) first, feeding decided renderings back. Use the {j} display-join marker so a quotation reads inline with its lead-in and attribution; keep an exchange one paragraph per speaker turn. Watch parity: every 「…」 quote line, every と…いった attribution line, and every 「………」 silence is its OWN source paragraph and needs its OWN reading line. OBEY STYLE.md (em-dash budget; no scene-primed idioms). Consult the voice sheets below; read the last two pages of ch13's English before starting ch14 (batch seam).
3. Author out/<id>_reading.md (## title, {j}, ***, blank-separated). Derive the flat array with scripts/reading_to_en.py <id>, then make_bilingual.py <id> data/src/<file>.txt "<title_en>" out/<id>_en.json (parity refuses on mismatch). Then the battery: bash scripts/check_chapter.sh <id> <srcbase> "<title_en>" runs reading_to_en + make_bilingual + verify_unit (--noise data/noise.txt) + gen_check_config + check_align + check_content + qc_entities + check_apparatus + check_register. Verify each chapter TAIL against the source explicitly (rule 4).
4. Footnotes per the reader model (first-appearance discipline; keep the "NOT re-noted" ledger in PROGRESS.md; note MORE than the glossary row) via apparatus_merge.py (each glossary row MUST carry a "section": people|places|organizations|terms field; the merge nests it and check_apparatus stays clean). Any figure from data/figs/ with a translated caption and real alt text.
5. check_register.py --ref reference/ch01_ref.md out/<id>_reading.md; record in PROGRESS.md. Fact-check historical claims against real scholarship (never LLM-sourced; IGNORE Grok/Grokipedia), verdict in the note. Add numeral-noise rules to data/noise.txt as new numbered names/idioms appear (comment each; never noise a real quantity).
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck (java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/burn-o-sword.epub); record ALL check results and EVERY digitization glitch in PROGRESS.md; update HANDOFF.md; commit and push to claude/burn-o-sword.

End the batch with BOTH chat deliverables (CLAUDE.md rule 1, enforced by the Stop hook): the built EPUB ATTACHED in the chat AND the Batch 5 kickoff PASTED VERBATIM in a fenced code block. Batch 5 = ch19 through ch23.

Cite chapters and sections, never pages.
```

## What is DONE (do not redo)

- Step 0 (ingest + survey), committed. book.json: 68 novel chapters (ch01 to
  ch68) + 3 back-matter units.
- B01 = ch01 「女の夜市」 / "The Women's Night Market", COMPLETE and APPROVED at
  the voice gate. ch01 FROZEN as the register reference (reference/ch01_ref.md;
  em-dash baseline 12.7/1k, dialogue contractions 24.9/1k). Notes 1 to 15.
- B02 = ch02 to ch07, COMPLETE. ch02 六車斬り / "Cutting Down Rokusha", ch03
  七里研之助 / "Shichiri Kennosuke", ch04 わいわい天王 / "The Waiwai Tennō", ch05
  分倍河原 / "Bubaigawara", ch06 月と泥 / "The Moon and the Mud", ch07 江戸道場 /
  "The Edo Dōjō". Notes 16 to 55.
- B03 = ch08 to ch13, COMPLETE. ch08 桂小五郎 / "Katsura Kogorō", ch09 八王子討入り
  / "The Hachiōji Raid", ch10 スタスタ坊主 / "The Sutasuta Monk", ch11 疫病神 /
  "The Bringer of Ill Luck", ch12 浪士組 / "The Rōshigumi", ch13 清河と芹沢 /
  "Kiyokawa and Serizawa". Notes 56 to 100 (45 this batch). All checks green;
  qa_epub PASS; epubcheck 0/0/0/0. Continuous note number so far: 100. See
  PROGRESS.md B03 for the full record, the fact-check verdicts, and every
  settled rendering.

## Tooling in place (do NOT revert)

- ingest_epub.py: Japanese-aware (furigana strip, 8 gaiji via
  data/gaiji_map.json, dumps reference/furigana_readings.tsv). From Step 0.
- data/gaiji_map.json: 遼 茨 頤 葛 芦, plus レ (kaeriten) and 㝎 (之定 variant).
- DISPLAY JOIN MARKER {j} (B01, whole-book): a reading line prefixed "{j} " is
  merged onto the preceding display paragraph at BUILD time (single space,
  em-dash aware). Reading keeps one line per source paragraph, so parity /
  number / entity checks are untouched. All checks strip {j}.
- scripts/scene_map.py (B02): reports scene breaks from the raw data/src_epub
  XHTML (runs of two or more <p><br/></p> in the body). Run per chapter.
- scripts/reading_to_en.py (B02): derives out/<id>_en.json from the authored
  out/<id>_reading.md so the flat parity array cannot drift.
- scripts/check_chapter.sh (B02): the per-chapter QC battery in one call.
- scripts/apparatus_merge.py (B02): glossary rows REQUIRE a "section" field and
  are nested into people/places/organizations/terms. Every glossary row must
  set "section".
- scripts/qc_entities.py (B03 PATCH): SKIPS single-kanji glossary keys (zh
  length < 2). A single-kanji name key false-hits by raw substring: 権 (Gon)
  inside 権力 / 権威 / 政権, 里 (ri) inside 郷里, etc. This bites the whole
  political half of the book. check_content already skips zh length < 2; this
  matches it. Named referents stay in the glossary; only the unreliable
  substring check is dropped for them. DO NOT REVERT.
- data/noise.txt (B01 to B03): Japanese name/idiom numeral rules, each
  commented. Add more as numbered names / teen-elisions appear. Never noise a
  real quantity.
- STYLE.md (B01): the house style sheet (em-dash budget; scene-primed idioms).
  READ IT each batch; add to it when the commissioner corrects a line.
- reference/ch01_ref.md (B01): the FROZEN register reference. Do not edit.

## Voice sheets (one per major character; consult at every dialogue scene)

- NARRATOR: third person, wry and knowing, fond of the aside ("or so the story
  goes," "incidentally") and the forward glance to events years ahead. Long
  descriptive sentences alternating with very short flat ones. Period texture,
  never antiquarian. Uses Shiba's own modern parentheticals and asides (the
  Kōrakuen of today; Ehime prefecture; the Zengakuren analogy): KEEP them.
- HIJIKATA TOSHIZŌ ("Toshi"): the hero, 22 to 28 across the book. Rough Bushū
  farm dialect off guard, contracted and blunt. Cool, laconic, a dandy, a
  natural tactician. Class-obsessed and a little twisted about it (the Katsura
  scene, ch08). His speech CONTRACTS; his cruelty is matter-of-fact. In Kyoto
  (from ch13) he insists on being called "Hijikata," not "Toshi," and starts
  imposing rank and order; he is the cold engine of the new party.
- KONDŌ ISAMI: warm, plain, big-jawed Bushū farmer's son; slow to show
  surprise, generous, eats voraciously, believes in 気組 ("fighting spirit").
  Weeps at the thought of guarding the shogun (ch12). Calls Toshizō "Toshi"
  (learning to say "Hijikata"). Bushū dialect.
- OKITA SŌJI: 20 to 21, an Edo-born rōnin's son, the corps' finest blade.
  Bright, boyish, glib, teasing, needles Toshizō affectionately, clowns when
  danger is near, cool as ice in a fight. Contracts freely; quick Edo tongue.
  His smile is a recurring beat.
- SHICHIRI KENNOSUKE: the early antagonist, an iai master of the Araki-ryū.
  Fleshy jowls, cold sharp eyes, insolent and mocking, makes game of people.
  Follows the feud to Kyoto (ch10: has "gone up to Kyoto"); watch for his
  return.
- YAMANAMI KEISUKE (from ch11): the eldest house-guest, a learned Sendai man;
  educated, controlled, faintly stiff and formulaic; a sincere expel-the-
  barbarian idealist. Speaks in a Sendai accent, frames things bookishly,
  praises everything of Kyoto. Toshizō despises him ("Yamanami is a fox"). His
  gentleness will destroy him (seppuku, 1865). His stiffness is DELIBERATE
  register, not drift.
- SERIZAWA KAMO (from ch13): huge, drunken, arrogant, volatile Mito rōnin of
  the Shintō Munen-ryū. Rough, mocking, grandiose ("Ho, a rare visitor";
  "What, that stripling?"); dangerous when crossed. Toshizō's uneasy first ally
  and, soon, his target.
- KIYOKAWA HACHIRŌ (ch11, ch13): brilliant strategist-orator of Dewa; grand,
  formal, oratorical set-pieces (revere-the-Emperor rhetoric); vain and
  manipulative. Keep his speeches elevated but comprehensible.
- KATSURA KOGORŌ (ch07 to ch08): educated, controlled, Chōshū; unfailingly
  courteous, evasive rather than combative ("I would run"). The historical
  Runaway Kogorō / future Kido Takayoshi; Toshizō's opposite in every
  advantage.
- OSEN / せん (ch03 to ch09): the Senjubō daughter, now Hiruma Hanzō's wife;
  soft, formal, UNCONTRACTED, gentle word-endings; terrified of Toshizō, whom
  she betrays in ch09. Never contract her.
- SATŌ HIKOGORŌ and ONOBU (his wife, Toshizō's sister, ch12): the great-
  headman brother-in-law, genial, trusting, funds the swords; Onobu is
  big-bellied, quiet, dotes on Toshizō. Warm Bushū speech.

## Renderings settled / carry-forward

- Title "Burn, O Sword!"; author Shiba Ryōtarō. Names Japanese order, macrons.
- ONE rendering per referent, all in glossary.json. Enforced by check_content.
  B03 highlights: 和泉守兼定 "Izumi-no-kami Kanesada"; ノサダ "Nosada"; 虎徹
  "Kotetsu"; 講武所 "the Kōbusho"; 辻斬り "tsujigiri"; 鉄扇 "iron war-fan";
  尊皇攘夷 "Revere-the-Emperor and Expel-the-Barbarian" (sonnō jōi); 浪士組 "the
  Rōshigumi"; 京都守護職 "the Kyoto Protector"; 天狗党 "the Tengu Party"; 壬生
  "Mibu"; 新徳寺 "the Shintoku-ji"; 中仙道 "the Nakasendō". Guards: jōdan
  "overhead guard", chūdan "middle guard", gedan "low guard". Corps units
  rendered "the Fifth Unit / the Third Unit". 三多摩 "the Three Tama"; 多摩十騎衆
  "the Ten Horsemen of Tama". Era-year form kept with the numeral (e.g. "the
  second of Bunkyū"). Modern intrusions Shiba himself makes (metric distances,
  clock times, prefecture names) are KEPT as his own asides.
- Names settled B03: 戸張節五郎 "Tobari Fushigorō" (source ruby); 山南敬助
  "Yamanami Keisuke" (not Sannan); 芹沢鴨 "Serizawa Kamo"; 清河八郎 "Kiyokawa
  Hachirō"; 松平容保 "Matsudaira Katamori"; 山岡鉄太郎 "Yamaoka Tetsutarō" (the
  future Tesshū); 新見錦 "Niimi Nishiki"; 斎藤一 "Saitō Hajime"; the Serizawa
  band (平間重助 Hirama Jūsuke, 野口健司 Noguchi Kenji, 平山五郎 Hirayama Gorō).
- COVER: keep data/figs/embed0009_HD.jpg byte-identical, as book.json sets it.
- Principal Characters page flags now: Hijikata (1), Kondō (2), Okita (3),
  Inoue (4), Nagakura (5), Shichiri (6), Harada (7), Katsura (8), Yamanami (9),
  Serizawa (10), Saitō Hajime (11).
- Provisional, worth a second look as they recur: 松平上総介 Matsudaira
  Kazusa-no-suke, 平間重助 Hirama Jūsuke, and the older B01/B02 provisionals.

## Where the book stands (story)

- ch01 to ch07 (B01 to B02): the Tama-country prologue. Toshizō the rakish
  farmer's son; the Rokusha killing and the Shichiri feud; the core cast
  assembles at the Edo dōjō as Katsura makes his first entrance.
- ch08 to ch13 (B03): Katsura outfences Shichiri and Toshizō's class-hatred is
  fixed; the Hachiōji raid (Sutasuta-monk ambush) shuts the Hiruma hall; the
  1862 measles/cholera epidemic ruins the dōjō and drives the company to enlist
  in the shogunate's Rōshigumi; Toshizō buys his Kanesada and kills a
  night-duelist leaving Edo; in Kyoto at the Mibu Shintokuji, Kiyokawa reveals
  the corps's secret imperial purpose, and Toshizō resolves to break away, kill
  Kiyokawa, and found a new party, allying with the violent Mito man Serizawa
  Kamo. The core Shinsengumi is assembling at Mibu.

## What is NEXT

- B04 = ch14 to ch18 (kickoff above). Then B05 ch19-23, B06 ch24-28, B07
  ch29-33, B08 ch34-38, B09 ch39-43, B10 ch44-48, B11 ch49-53, B12 ch54-58,
  B13 ch59-63, B14 ch64-68, B15 ch69-71 back matter + whole-book reconciliation
  + COMPLETION.

## Open items for the read-through

- ch14 ついに誕生 ("Born at Last") is the founding of the Shinsengumi proper;
  confirm the corps-formation details, the naming, and the Aizu connection.
- The Kanesada / Nosada / 㝎 swordsmith material was handled in ch12 (note at
  "The Nosada,"), with the fact-check that Hijikata's real blade was the
  11th-gen Aizu Kanesada; the book.json _gaiji_note guess of "ch16" was off by
  one file, the 兼㝎 gaiji image is in part0014 (ch12). Watch ch16 高瀬川 for any
  further sword discussion.
- Confirm minor Shinsengumi and Kyoto place-name readings against
  reference/furigana_readings.tsv as they appear; watch for Shichiri's return.

## Environment / traps state

- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches).
- data/src/ and data/src_epub/ are gitignored (regenerate via ingest if empty);
  scene_map.py needs data/src_epub, so re-run ingest before it if empty.
- Scene-break convention: two or more consecutive blank <p><br/></p> inside the
  body = a break; the single pair after the title is only the title/body
  separator. Use scripts/scene_map.py.
- PARITY trap: the source sets every quote, every attribution (と…いった), and
  every silence (「………」) as its own paragraph. Each needs its own reading
  line. make_bilingual catches a miscount; reading_to_en + an index scan locates
  it.
- NUMBER-CHECK traps: teen-elisions (十二、三 etc.) and tens-elisions (三、四十 =
  "thirty or forty") take a noise rule; names with numerals take a noise rule;
  a hundred-plus-tens value wants the "one hundred and thirty" word-form (not
  "a hundred and thirty") to satisfy the check. Never noise a real quantity.
- CONTENT-CHECK trap: render the glossary's decided form verbatim in a paragraph
  that names a glossaried referent (e.g. write "Bushū Tama", "Okita Sōji" in
  full where the source uses the full name), or check_content reports a phantom
  displacement.
- Known failing test, EXPECTED: tests/run_tests.py reports "hook stands down on
  template stub" FAIL (it only passes on the template placeholder kickoff). Not
  a translation gate. All other tests pass.
- All work is on branch claude/burn-o-sword.
