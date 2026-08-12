# HANDOFF, Burn, O Sword! (燃えよ剣), Shiba Ryōtarō

This file is the baton. A fresh session with no memory reads it and starts
immediately. It is the ARCHIVE of the kickoff message, not its delivery: every
batch ends with this file's kickoff block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count. Rewrite it at
the end of every batch; always keep the paste-ready kickoff below as its first
section.

## Message to paste into the next chat

```
Burn, O Sword! B03

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then STYLE.md, then book.json. We are translating Burn, O Sword! (燃えよ剣) by Shiba Ryōtarō from a Japanese digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/burn-o-sword; expect the harness to open you on a stray per-task branch and consolidate per CLAUDE.md rule 2. Deliverable out/burn-o-sword.epub.

Batches 1 and 2 are DONE. ch01 is the FROZEN register reference: reference/ch01_ref.md. Run ./setup.sh; if data/src/ is empty re-run scripts/ingest_epub.py source.epub (Japanese-aware: strips furigana, substitutes 8 gaiji, writes reference/furigana_readings.tsv). No source-note stream. Keep the source's own cover (data/figs/embed0009_HD.jpg), reused byte-identical, exactly as book.json already sets it; the commissioner likes it, do not change it. The known failing test "hook stands down on template stub" is EXPECTED (it only passes on the template placeholder kickoff); every other test passes.

Do Batch 3 = ch08 through ch13 (桂小五郎 / Katsura Kogorō; 八王子討入り / The Hachiōji Raid; スタスタ坊主 / The Sutasuta Monk; 疫病神 / The Bringer of Ill Luck; 浪士組 / The Rōshigumi; 清河と芹沢 / Kiyokawa and Serizawa), end to end per the CLAUDE.md pipeline, RUN TO COMPLETION. Do not stop mid-batch except for a genuine blocker or completion. For each chapter:
1. Build data/zh/<id>.txt from data/src (title line "### <title>" then one body line per source paragraph; the mechanical build in B02 was: skip the first two header lines, keep non-empty lines). Fix any extractor splits (this source has had none: a narration line ending in 、 before a 「quote」 is the source's own lead-in, handled by the {j} join, NOT a split to merge). Recover scene breaks with scripts/scene_map.py OEBPS/Text/partNNNN.xhtml (a run of TWO OR MORE consecutive <p><br/></p> in the body is a break; the single pair after the title is only the title/body separator). Place *** in the reading at those points.
2. Translate to the FROZEN ch01 register. Names Japanese order, surname first, macrons; CONSULT reference/furigana_readings.tsv before romanizing ANY name or word (this caught Rokusha-not-Muruma and Momonoi-not-Momoi in B02), and consult glossary.json (then authority.json) first, feeding decided renderings back. Use the {j} display-join marker so a quotation reads inline with its lead-in and attribution; keep an exchange one paragraph per speaker turn. Watch parity: every 「…」 quote line, every と…いった attribution line, and every 「………」 silence is its OWN source paragraph and needs its OWN reading line (dropping a といった。 line was the recurring parity break in B02). OBEY STYLE.md (em-dash budget; no scene-primed idioms). Consult the voice sheets below; read the last two pages of ch07's English before starting ch08 (batch seam).
3. Author out/<id>_reading.md (## title, {j}, ***, blank-separated). Derive the flat array with scripts/reading_to_en.py <id>, then make_bilingual.py <id> data/src/<file>.txt "<title_en>" out/<id>_en.json (parity refuses on mismatch). Then the battery: bash scripts/check_chapter.sh <id> <srcbase> "<title_en>" runs reading_to_en + make_bilingual + verify_unit (--noise data/noise.txt) + gen_check_config + check_align + check_content + qc_entities + check_apparatus + check_register. Verify each chapter TAIL against the source explicitly (rule 4).
4. Footnotes per the reader model (first-appearance discipline; keep the "NOT re-noted" ledger in PROGRESS.md; note MORE than the glossary row) via apparatus_merge.py (each glossary row MUST carry a "section": people|places|organizations|terms field now; the merge nests it and check_apparatus stays clean). Any figure from data/figs/ with a translated caption and real alt text.
5. check_register.py --ref reference/ch01_ref.md out/<id>_reading.md; record in PROGRESS.md. Fact-check historical claims against real scholarship (never LLM-sourced; IGNORE Grok/Grokipedia), verdict in the note. Add numeral-noise rules to data/noise.txt as new numbered names/idioms appear (comment each; never noise a real quantity).
6. Rebuild the EPUB (scripts/build_reading_epub.py), qa_epub.py until green, epubcheck (java -jar /tmp/epubcheck-5.1.0/epubcheck.jar out/burn-o-sword.epub); record ALL check results and EVERY digitization glitch in PROGRESS.md; update HANDOFF.md; commit and push to claude/burn-o-sword.

End the batch with BOTH chat deliverables (CLAUDE.md rule 1, enforced by the Stop hook): the built EPUB ATTACHED in the chat AND the Batch 4 kickoff PASTED VERBATIM in a fenced code block. Batch 4 = ch14 through ch18.

Cite chapters and sections, never pages.
```

## What is DONE (do not redo)

- Step 0 (ingest + survey), committed. book.json: 68 novel chapters (ch01 to
  ch68) + 3 back-matter units.
- B01 = ch01 「女の夜市」 / "The Women's Night Market", COMPLETE and APPROVED at
  the voice gate. ch01 FROZEN as the register reference (reference/ch01_ref.md;
  em-dash baseline 12.7/1k, dialogue contractions 24.9/1k). Notes 1 to 15.
- B02 = ch02 to ch07, COMPLETE. ch02 六車斬り / "Cutting Down Rokusha" (title
  corrected from the survey's "Muruma" per the source furigana), ch03 七里研之助
  / "Shichiri Kennosuke", ch04 わいわい天王 / "The Waiwai Tennō", ch05 分倍河原 /
  "Bubaigawara", ch06 月と泥 / "The Moon and the Mud", ch07 江戸道場 / "The Edo
  Dōjō". Notes 16 to 55 (40 this batch). All checks green; qa_epub PASS;
  epubcheck 0/0/0/0. Continuous note number so far: 55. See PROGRESS.md B02 for
  the full record, the fact-check verdicts, and every settled rendering.

## Tooling in place (do NOT revert)

- ingest_epub.py: Japanese-aware (furigana strip, 8 gaiji via
  data/gaiji_map.json, dumps reference/furigana_readings.tsv). From Step 0.
- data/gaiji_map.json: 遼 茨 頤 葛 芦, plus レ (kaeriten) and 㝎 (之定 variant).
- DISPLAY JOIN MARKER {j} (B01, whole-book): a reading line prefixed "{j} " is
  merged onto the preceding display paragraph at BUILD time (build_reading_epub
  collapsed(), single space, em-dash aware: no space when either side of the
  seam is an em dash). Reading keeps one line per source paragraph, so parity /
  number / entity checks are untouched. All checks strip {j}.
- scripts/check_align.py, check_content.py, gen_check_config.py (B01): scene-
  break aware; run gen_check_config each batch before check_align/content.
- scripts/scene_map.py (B02, NEW): reports scene breaks from the raw
  data/src_epub XHTML (runs of two or more <p><br/></p> in the body); the
  ingest collapses those blanks in data/src so they are invisible there. Run it
  per chapter. Validated against ch01 (breaks after 48, 115).
- scripts/reading_to_en.py (B02, NEW): derives out/<id>_en.json from the
  authored out/<id>_reading.md so the flat parity array cannot drift from the
  display file. make_bilingual then cross-checks the count against data/src.
- scripts/check_chapter.sh (B02, NEW): the per-chapter QC battery in one call.
- scripts/apparatus_merge.py (B02, PATCH): glossary rows now REQUIRE a
  "section" field and are nested into people/places/organizations/terms. The
  old flat placement broke the build (render_glossary reads top-level keys as
  section headings). Every future glossary row must set "section".
- data/noise.txt (B01+B02): Japanese name/idiom numeral rules, each commented.
  Add more as numbered names / teen-elisions (十X、Y) appear. Never noise a real
  quantity.
- STYLE.md (B01): the house style sheet (em-dash budget; scene-primed idioms).
  READ IT each batch; add to it when the commissioner corrects a line.
- reference/ch01_ref.md (B01): the FROZEN register reference. Do not edit.

## Voice sheets (one per major character; consult at every dialogue scene)

- NARRATOR: third person, wry and knowing, fond of the aside ("or so the story
  goes," "incidentally") and the forward glance to events years ahead (Toshizō
  "who a few years hence would be vice-commander of the Shinsengumi"). Long
  descriptive sentences alternating with very short flat ones. Period texture,
  never antiquarian. Uses Shiba's own modern parentheticals ("the Kōrakuen of
  today"): keep them.
- HIJIKATA TOSHIZŌ ("Toshi"): the hero, 22 to 23 here. Rough Bushū farm dialect
  off guard, contracted and blunt ("What're we gonna do about that bastard?").
  Cool, laconic, a dandy, a natural tactician. Class-obsessed and a little
  twisted about it (the Katsura scene). His speech CONTRACTS; his cruelty is
  matter-of-fact ("Now that the man knew of the affair, he could not be left
  alive.").
- KONDŌ ISAMI: warm, plain, big-jawed Bushū farmer's son; slow to show
  surprise (scratches his backside instead), generous, eats voraciously, a
  little dim about Toshizō's fastidiousness. Believes in 気組 ("fighting
  spirit"). Calls Toshizō "Toshi." Bushū dialect ("歳の野郎…").
- OKITA SŌJI: 20, an Edo-born rōnin's son, the corps' finest blade. Bright,
  boyish, glib, teasing, needles Toshizō affectionately ("You took your sweet
  time"), chatters even in danger, cool as ice in a fight and unbloodied after
  it. Contracts freely; quick Edo tongue. Innocent about women. His smile is a
  recurring beat.
- SHICHIRI KENNOSUKE: the antagonist, ~30, an iai master of the Araki-ryū.
  Fleshy jowls, cold sharp eyes, insolent and mocking ("What, a medicine-
  seller?"; "Give it up, boy."), makes game of people, uses the new -kun
  suffix. Condescending calm that never quite breaks.
- OSAE / お佐絵 (from ch01): soft, courtly, UNCONTRACTED, gentle word-endings,
  refers to herself by name. Never contract her. Likely Shiba's invention.
- OSEN / せん (ch03-04): the Senjubō daughter, now Hiruma Hanzō's wife; composed,
  formal ("あなたさま…ございます"), was Toshizō's casual conquest. Narrator uses
  おせん ("Osen"), she names herself せん ("Sen"): the source varies and the
  point (Toshizō half-remembers her name) is made explicit; keep both.
- KOZAKURA (ch01, ch06): bell-shaking shrine maiden, Toshizō's casual lover;
  pert, teasing, colloquial. Contracts.
- SATŌ HIKOGORŌ: Toshizō's brother-in-law and the Tennen Rishin-ryū's patron;
  genial great-householder, mild, trusting, never doubts a man's word; funds
  the future Shinsengumi. Warm Bushū speech.

## Renderings settled / carry-forward

- Title "Burn, O Sword!"; author Shiba Ryōtarō. Names Japanese order, macrons.
- ONE rendering per referent, all in glossary.json (people/places/
  organizations/terms sections). Enforced by check_content. Full B02 list in
  git; highlights: 気組 "fighting spirit"; 居合 "iai"; 代官 "intendant"; 旗本
  "hatamoto"; 衢地 "a ground of highways"; 六車宗伯 "Rokusha Sōhaku"; 桃井春蔵
  "Momonoi Shunzō"; 猿田彦 "Sarutahiko" (source ruby さるだひこ noted); the sword
  schools by ryū name (Tennen Rishin-ryū, Kōgen Ittō-ryū, Ryūgō-ryū, Hokushin
  Ittō-ryū, Shintō Munen-ryū, Araki-ryū, Nen-ryū). 上石原 = "Kamiishiwara"
  (no hyphen), matching ch01. 半造 renders "Hanzō" (full "Hiruma Hanzō" in the
  pinyin field); 周作 renders "Shūsaku" (full "Chiba Shūsaku" in pinyin).
- Style calls held from B01: 浄闇 "sacred darkness"; 六社明神 "Rokusha Myōjin";
  万燈 keeps its numeral. Era years keep the era form and carry the numeral
  ("the eleventh year of Tenpō, 1840"), matching ch01's "fourth year of Ansei".
- COVER: keep data/figs/embed0009_HD.jpg byte-identical, as book.json sets it.
- Principal Characters page flags: Hijikata (1), Kondō (2), Okita (3), Inoue
  (4), Nagakura (5), Shichiri (6), Harada (7), Katsura (8).
- Provisional, worth a second look as they recur: Segi Kamon, Matsudaira Iori,
  Osaki, Rihei/Jōshūya, Zenkai, Tatsukichi, Gon, Onobu, Otsune, Fukatsu.

## Where the book stands (story)

- ch01 (1857) is the overture: Toshizō as a rakish, dangerous farmer's son.
- ch02 to ch07: Toshizō kills Rokusha Sōhaku, the Kōgen Ittō-ryū deputy at
  Fuchū, over the affair with Osae; the Hachiōji school hunts him (disguised as
  waiwai-tennō); he and Okita rout them at Bubaigawara; the feud follows
  Shichiri to the Edo dōjō (Kondō's Shieikan, Koishikawa), which closes on the
  first entrance of Katsura Kogorō, come as a borrowed swordsman. The core cast
  is now assembled at the Edo hall (Kondō, Toshizō, Okita, Inoue, Nagakura,
  Todō, Harada) on the eve of the political story.

## What is NEXT

- B03 = ch08 to ch13 (kickoff above). Then B04 ch14-18, B05 ch19-23,
  B06 ch24-28, B07 ch29-33, B08 ch34-38, B09 ch39-43, B10 ch44-48,
  B11 ch49-53, B12 ch54-58, B13 ch59-63, B14 ch64-68, B15 ch69-71 back matter +
  whole-book reconciliation + COMPLETION.

## Open items for the read-through

- ch08 桂小五郎: Katsura's own chapter; his register (educated, controlled,
  Chōshū) sets up the political thread. Confirm Katsura/Kido details.
- ch16 (和泉守兼定 / the 之定 signature, 㝎) will want a swordsmith note.
- Confirm minor Shinsengumi and place-name readings against
  reference/furigana_readings.tsv as they appear.

## Environment / traps state

- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches).
- data/src/ and data/src_epub/ are gitignored (regenerate via ingest if empty);
  scene_map.py needs data/src_epub, so re-run ingest before it if empty.
- Scene-break convention: two or more consecutive blank <p><br/></p> inside the
  body = a break; the single pair after the title is only the title/body
  separator. Use scripts/scene_map.py (it reads the raw XHTML).
- PARITY trap (recurred twice in B02): the source sets every quote, every
  attribution (と…いった), and every silence (「………」) as its own paragraph.
  Each needs its own reading line; folding a といった。 into the quote drops a
  line and breaks parity. make_bilingual catches it; reading_to_en + a quick
  index scan against data/zh locates it.
- NUMBER-CHECK trap: "the hundred-odd" does not register 100 (needs "a
  hundred-odd"); 二人 needs "two"/"the two" in the English; teen-elisions like
  十二、三 / 十八、九 (the second numeral is the ones-digit of a teen) get a
  noise rule. Names with numerals get a noise rule. Never noise a real quantity.
- Known failing test, EXPECTED: tests/run_tests.py reports "hook stands down on
  template stub" FAIL. It only passes when HANDOFF.md holds the template's
  placeholder kickoff; a real book kickoff makes the guard enforce, as intended.
  Not a translation gate. All other tests pass.
- All work is on branch claude/burn-o-sword.
