# HANDOFF — The Golden Roc Dynasty (陆小凤传奇·金鹏王朝, Gu Long)

This file is the baton. A fresh session with no memory reads it and starts
immediately. **It is the ARCHIVE of the kickoff message, not its delivery:
every batch ends with this file's kickoff block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count.** Rewrite it
at the end of every batch; always keep the paste-ready kickoff message below as
its first section. When the book completes, replace the kickoff with the
completion notice and do not touch it afterward (the Stop hook keys off it).

## Message to paste into the next chat

```
Lu Xiaofeng 1 B08 (FINAL — the coda + back matter + whole-book completion)

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 金鹏王朝 (The Golden Roc Dynasty), Volume 1 of Gu Long's Legend of Lu Xiaofeng, from a digital source EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/lu-xiaofeng-1; expect the harness to start you on a stray per-task branch and consolidate per rule 2 (check out claude/lu-xiaofeng-1, reset to origin, and if a stray branch carries commits, fast-forward or cherry-pick them on, push, and delete the stray). Deliverable out/lu-xiaofeng-1.epub.

Run ./setup.sh first and record any failure in PROGRESS.md. NOTE: the regression harness reports 9/10 green with ONE expected failure ("hook stands down on template stub") — that case only passes while HANDOFF.md holds the template placeholder; now that HANDOFF carries a real kickoff the Stop hook correctly enforces, so that one test necessarily reads FAIL for the rest of the book. Not a defect; do not "fix" it. data/src and data/src_epub are gitignored and regenerable: if they are missing, run scripts/ingest_epub.py source.epub (do NOT overwrite book.json). This book has NO source-edition footnotes; re-grep ch13's source for \[\d+\] and record "none present" per unit in PROGRESS.md.

ch01 remains the FROZEN REFERENCE for register and PARAGRAPHING. Before translating, READ out/ch12_reading.md (The Sixth Toe) end to end — the freshest voice — plus ch10/ch11 as needed. Study STYLE.md, HANDOFF's "Paragraphing", "Attribution", and the voice sheets (Lu Xiaofeng, Hua Manlou, Huo Xiu [now revealed the arch-villain], Huo Tianqing [wronged, innocent of Feiyan's murder], Shangguan Feiyan, Shangguan Xue'er, the Shanxi Wild Goose, Zhu Ting / the Boss's Wife). Money/units are SETTLED: keep the period units (cash / catty / tael / li / cun / zhang / chi) with footnotes, no domestication. Watch comma density; em dashes sparingly; contractions measured (the register metric counts only n't/'ll/'re/'ve/'m, not 's/'d) — CONTRACT ORDINARY SPEAKERS INSIDE DIALOGUE (see scratchpad/contract_dialogue.py; a confrontation-heavy chapter reads STILTED otherwise). Consult glossary.json (now 85 rows) and authority.json BEFORE romanizing anything.

Do Batch B08 = the FINAL batch: ch13 (第十二章 尾声 "Coda", ~2,785 chars, text_file data/src/18_part0000-split-016.txt) PLUS the whole-book back matter, reconciliation, and completion report. Run end to end per the CLAUDE.md pipeline:
1. ch13 is SHORT and has NO bare-numeric scene dividers (grep confirmed) — it is ONE scene, so NO *** breaks. ~116 body paragraphs (source lines 3–119). RE-VERIFY extractor splits (a line whose last char is not in 。！？"）…— continues the next; a colon-terminated lead-in to a quoted letter/verse is NOT a split) — ch13 has em-dash-bracketed interior monologue ("——…——"); check per line. TWO trailing lines are publisher end-matter, NOT story text: source line 120 「《陆小凤传奇：金鹏王朝》完」 (the "END" marker) and line 121 「相关情节请看《陆小凤传奇2：绣花大盗》」 (a next-volume teaser for Legend of Lu Xiaofeng 2: The Embroidery Bandit). DECIDE and RECORD in book.json _source_note: cleanest is to EXCLUDE both from the translated chapter body (as the half-title stubs were excluded) and mention them — the "完"/END and the sequel note — either in the Translator's Note or as a one-line closing; do NOT silently drop them. The coda opens with Zhu Ting having sprung the stone-step door (confirming that the mechanism that trapped Huo Xiu in ch12 was Zhu Ting's doing, not "Heaven's will" — Lu's joke).
2. Translate ch13 to the frozen house style (read STYLE.md and out/ch12_reading.md). ATTRIBUTION RULE (load-bearing): every dialogue turn whose source names a CAPITALISED-glossary character (Lu Xiaofeng, Huo Xiu, Zhu Ting, Shangguan Xue'er, Master Lu, Lu Ban, ...) MUST carry that full rendering once. Lowercase-"the" names (the Boss's Wife, the Great King of the Golden Roc, the Shanxi Wild Goose, the Blue-Robe Tower, the Taoist Qingfeng, the Green Wind Temple, jianghu) are exempt from check_content and pass qc_entities via first-word "the". Never invent bridging text; render digitization glitches to plain sense and LIST each in PROGRESS.md; source errors of fact stay visible and footnoted. Verify the TAIL against the source before shipping.
3. Author out/ch13_en.json as MERGED English paragraphs (author into scratchpad/ch13_en.txt, one paragraph per line — the build_b07.py method JSON-encodes it). COPY scratchpad/build_b07.py → build_b08.py, re-range for ch13 (ONE scene, dividers=none so nothing excluded from the merged source except the two title/stub lines; breaks=[]). Then verify_unit.py ch13 (parity + numbers with the built-in data/noise.txt + anchors — do NOT pass --noise to verify_unit); check_align.py ch13; check_content.py --config scratchpad/qc_config.json (ADD ch13 to the config docs+sources first — ch12 was already added in B07); qc_entities.py out/ch13_bilingual.md glossary.json. WATCH THE NUMBER CHECK (矛/盾 spear-and-shield passage; any 一/二 idioms) — noise the idiom class (documented, longest-first) or render so the English carries the value; NEVER noise a real quantity. Spelled numbers tens-ones ("forty-nine"); "ten thousand" needs a space; 一百零八 → "one hundred and eight" (leading "one").
4. Footnotes per the reader model (expect ~2-3 for the coda; density has tapered hard). Use apparatus_merge.py for NOTES only; add glossary rows under the two-level sections directly (scratchpad/add_glossary_b08.py, the json.load/dump path — NOT the flat apparatus path) and validate with check_apparatus.py. check_apparatus.py clean.
5. Rebuild (scripts/build_reading_epub.py). Because the book is now COMPLETE (13/13), the builder should emit the FULL CLEAN TOC (no "pending" placeholders) and the honest coverage sentence — verify. Verify the English chapter titles against the text (ch12 "The Sixth Toe" and ch13 "Coda" confirmed; re-confirm ch13). qa_epub.py green, epubcheck (/tmp/epubcheck-5.1.0/epubcheck.jar) 0/0/0/0, check_structure.py --config PASS, check_register.py --ref out/ch01_reading.md out/ch13_reading.md within tolerance (>=0.45x).
6. WHOLE-BOOK COMPLETION (this is the final batch — do ALL of it, per CLAUDE.md "Definition of done" and check 11):
   - check_reconcile.py (repeated-compound rendering drift → candidates for a human read; glossary-forward usage; spelling locale by curated pairs). Fix or record.
   - By hand: grep-count ~20 decided renderings across ALL built units for drift (e.g. Lu Xiaofeng, Huo Xiu, the Blue-Robe Tower, the Golden Roc, jianghu, tael, the Great King of the Golden Roc, the Four Beauties of Emei, ...); notes appear at first appearance.
   - Random-sample DEEP AUDIT 3–5% with a FIXED seed → out/deep_audit.md, with an honest error-rate statement (zero-in-N proves below ~a bound, not zero); grep for the "invented precision" class.
   - out/term_ledger.md (the auditable term ledger from glossary.json).
   - Feed decided wuxia renderings back into authority.json (it currently holds no wuxia terms).
   - Write COMPLETION.md (from the scanned template's contract).
   - Force-commit the final EPUB: git add -f out/lu-xiaofeng-1.epub.
   - Rewrite THIS HANDOFF to the COMPLETE notice (replace the kickoff; do not touch after — the Stop hook keys off it).
   Record every check in PROGRESS.md; commit and push to claude/lu-xiaofeng-1.
7. End the batch per CLAUDE.md: attach the FINAL out/lu-xiaofeng-1.epub in the chat AND (since the book is complete) state completion plainly in the same reply — there is no next kickoff to paste; say so.

Cite chapters and sections, never pages. Do not pause for approval mid-batch (B08 is a normal batch, no gate; it is the last one).
```

## What is DONE (do not redo)

- **Step 0 survey** (prior session): ingested the source, authored book.json
  (13 units), built the skeleton EPUB.
- **B01 = Prologue (ch01)** — COMPLETE, revised at the voice gate (rounds 2-5).
  4 vignettes; 154 paragraphs; 15 footnotes. **ch01 is the FROZEN REGISTER
  REFERENCE** (contractions 40.3/1k, rhythm CV 0.75).
- **B02 = Chapter 1 (ch02)** — COMPLETE. 289 merged paragraphs; 11 footnotes.
- **B03 = Chapters 2-3 (ch03 + ch04)** — COMPLETE. ch03 323 / 4 notes; ch04
  333 / 6 notes.
- **B04 = Chapters 4-5 (ch05 盛宴 + ch06 悲歌)** — COMPLETE. ch05 306 / 6;
  ch06 272 / 4.
- **B05 = Chapters 6-7 (ch07 珠光宝气 + ch08 市井七侠)** — COMPLETE. ch07 226 /
  4; ch08 346 / 6.
- **B06 = Chapters 8-10 (ch09 峨嵋四秀 + ch10 飞燕去来 + ch11 迷楼)** — COMPLETE.
  ch09 283 / 4; ch10 237 / 4; ch11 289 / 5. (81 glossary rows at end of B06.)
- **B07 = Chapter 11 (ch12 第六根足趾 "The Sixth Toe")** — COMPLETE. **1235
  merged paragraphs** (1:1, dialogue-heavy; 4 scenes, breaks after 157/198/357)
  / **6 footnotes** (total 75 book-wide). **4 new glossary rows (85 total):**
  青枫 the Taoist Qingfeng, 鲁班 Lu Ban (attested), 鲁大师 Master Lu, 青风观 the
  Green Wind Temple. Every check green: parity 1235=1235, numbers 0 unresolved,
  align median 4.00 no strays, content 1169 all-in-paragraph, qc_entities 0
  misses, apparatus 0/0, structure ALL PASS (75 anchors), qa_epub PASS,
  epubcheck 5.1.0 0/0/0/0, register 0.66x (after a dialogue-contraction pass;
  first build read 0.36x STILTED). **THE CLIMAX RESOLVES:** the Golden Roc
  kings bear SIX TOES on each foot (異相); the "Great King" Lu served and the
  four mad "Kings" are all impostors, the true King and Princess Danfeng long
  since murdered. Shangguan Feiyan (with a lover) killed Danfeng and the King,
  impersonated Danfeng, and used Lu to kill the ministers; she confesses, Hua
  Manlou forgives her, Lu frees her, and the hidden mastermind cuts her throat
  to silence her. Lu wrongly accuses Huo Tianqing (who nobly renounces the
  Heaven's Bird sect to spare his disciples and accepts the duel) — but Huo
  Tianqing was framed: he was playing chess at the Green Wind Temple when Feiyan
  died hundreds of li off, then poisoned and passed off as a suicide, the abbot
  Qingfeng bought to bear false witness (and the temple then burned).
  **The mastermind is HUO XIU** — Grand Helmsman of the 108 Blue-Robe Towers,
  who killed the Great King (grown poor, would reclaim the fortune), seduced
  Feiyan with jewels (not Huo Tianqing, as all believed), and meant Lu and Hua
  for a walled grave. He drops an iron cage to shield himself while he escapes
  the vault by a trapdoor — but the trapdoor is sealed: **Zhu Ting** (heir of
  Master Lu, of Lu Ban's line) got out first and jammed the mechanism, caging
  Huo Xiu in his own trap ("inviting the ruler into the urn"). Xue'er and the
  Boss's Wife are safe. Lu credits "Heaven's will"; Hua does not believe him.

## Tooling in place (do NOT revert)

- `scratchpad/build_b07.py` — the CURRENT merged-paragraph builder (re-ranged
  copy of build_b06.py, ONE unit). Copy + re-range per new unit; for ch13,
  dividers=none, breaks=[]. COMMITTED. `scratchpad/qc_config.json` — the
  check_content / check_structure config ({docs, sources, notes}); extended
  through **ch12** in B07 (ADD ch13 next). `scratchpad/add_glossary_b07.py` —
  the json.load/dump glossary helper (adds rows under the two-level sections;
  NOT the flat apparatus path). `scratchpad/contract_dialogue.py` — raises the
  contraction count by contracting ordinary speakers INSIDE dialogue only
  (narration left as the frozen reference has it); rerun after authoring en.txt
  if a confrontation chapter reads STILTED. All COMMITTED. (build_b03..b06.py
  remain as earlier copies.)
- `data/noise.txt`: B01-B06 entries (see PROGRESS), plus **B07 additions**
  (each documented in-file, all justified by real flags): `三分` (three-tenths
  "a touch/somewhat"), `千娇百媚` (bewitching), `四散` (four-directions), `(?<=把)两`
  (tael 两 after 把), `合十` (双手合十/双掌合十 — 十 = the ten fingers of the
  gesture, not the count 10). Keep.
- **glossary.json is TWO-LEVEL** (`section -> {zh: row}`). `apparatus_merge.py`
  adds glossary rows FLAT, which the builder/qc choke on. **Use apparatus_merge
  for NOTES only; add glossary rows under sections directly (add_glossary_b0N.py
  or Edit/Write) and validate with check_apparatus.py.**
- `scripts/check_content.py`, `check_align.py`, `check_numbers.py`,
  `check_structure.py`, `verify_unit.py`: the `***`-skip and spelled-number
  patches are load-bearing. **verify_unit self-locates data/noise.txt — do NOT
  pass it `--noise`.** Number-check gotchas that recurred in B07: the tael 两
  (noised after 十/百/千/万/多/把); the 十 inside 合十; 1,980 must be rendered in
  DIGITS ("1,980 catties") or cn_to_int's single 1980 splits to 1000+980;
  一百零八 needs the leading "one"; 四X direction idioms; fen-as-tenths (三分/五成).
- **Regression harness**: `./setup.sh` reports FAILED but 9/10 with ONE EXPECTED
  failure (`hook stands down on template stub`). Not a defect.

## Paragraphing (book-wide rule — do NOT revert)

The commissioner rejected 1:1 rendering as too choppy. **MERGE adjacent
narration lines into paragraphs grouped by beat; keep dialogue turns and
deliberate punch-lines on their own.** In practice the DIALOGUE-HEAVY chapters
(ch11, ch12) run essentially 1:1 because each Gu Long source line is already
its own beat — that is correct, not choppy; the "don't be choppy" note is
about not splitting one beat across several English lines. Method:

1. Author the MERGED English paragraphs into `scratchpad/<id>_en.txt`, one
   paragraph per line, reading order.
2. Group source body lines into the same paragraphs; the builder concatenates
   each group's original lines VERBATIM (join with '' — every body line ends on
   terminal punctuation; check per unit). `make_bilingual.py <id> <merged_src>
   <title> en.json 2` → parity + verbatim by construction, then
   `split_bilingual.py`. (See `scratchpad/build_b07.py`; the range lists use the
   `spans`/`singles` helpers, dividers EXCLUDED.)
3. **Scene breaks** (ch02-ch12): the source's bare-numeric markers (01, 02, ...)
   are EXCLUDED from the merged source; `***` is post-inserted after the
   paragraph that ends each scene. **ch13 has NO markers → NO breaks.**
4. All checks run on the merged pairs (`***` skipped everywhere).

## Attribution (load-bearing — do NOT drop)

Rapid dialogue must name its speaker or three checks fail at once
(`check_content` wants each CAPITALISED glossary name in every SOURCE paragraph
that contains that character's hanzi key — including the `X道` attribution tag;
`qc_entities` wants the first/last name-word; bare interjections are
`check_align` ratio outliers). **Give each dialogue turn the character's full
name once via a natural attribution ("said Lu Xiaofeng", "said Huo Xiu") then
let pronouns carry the rest.** In a two-hander, tag both speakers each turn —
Gu Long's own staccato does the same and it reads fine. **Lowercase-"the"
glossary names are exempt from check_content and pass qc_entities trivially via
the article "the".** **CAUTION: source SHORT FORMS may not trigger the check** —
上官丹凤 is NOT the glossary key 丹凤公主, 雪儿 is not the key 上官雪儿, 独孤/西门
alone are not the full keys; render those consistently anyway. **Watch
DISPLACEMENT:** in B07 exactly one paragraph (源 line 530, a 陆小凤道 line) shipped
without "Lu Xiaofeng" and was caught by both check_content and qc_entities;
restore the name in-place.

## Voice / house style (the frozen register — match it exactly)

**`STYLE.md` (repo root) is the worked-example version — read it before
translating.** Fluency over literalism; economy; comma density watched; em
dashes only when they beat a comma cluster and sparingly; image-forward,
concrete diction; vary rhythm, punch-lines on their own line; contractions
measured; paragraph by beat; dialogue characterised (voice sheets); names once
then pronouns; NO invented substance; keep cultural nouns and period units,
footnoted. Read the freshest reading.md (ch12) end to end before translating.
**Register-metric note:** `check_register` counts contractions of the form
n't/'ll/'re/'ve/'m ONLY (not 's/'d). A confrontation chapter reads STILTED;
fix by contracting the ORDINARY speakers INSIDE dialogue
(`scratchpad/contract_dialogue.py`) — but LEAVE narration as the frozen
reference has it, and LEAVE quoted classical laments/verse, Ximen Chuixue's
monosyllabic killer register, and a character's grave duel line UNcontracted
(e.g. Huo Tianqing's "which shall it be, you or I?" kept "shall").

## Voice sheets (consult at every dialogue scene)

- **Lu Xiaofeng** — the laziest, wriest man alive; sees everything; ox-stubborn
  once set ("pull me and I balk, drive me and I back away"); goads an angry man
  for sport; grieves a win that was not his to make (Huo Tianqing); credits his
  own cleverest stroke to "Heaven's will" and won't be believed.
- **Hua Manlou** — gentle, warm, unhurried; serene declaratives; blind and
  joyful; only love in his heart, no hate; forgives even Shangguan Feiyan
  ("you never did ask me to love you"); a true gentleman ("a gentleman and a
  fool are much of a muchness, at times").
- **Huo Xiu / old Huo** (霍休) = Shangguan Mu — REVEALED the arch-villain and
  Grand Helmsman of the 108 Blue-Robe Towers. Genial, avaricious, conscienceless;
  people are tools ("I want them alive, they live; I want them dead, they die");
  loves money above all (the fortune is "like a wife — alive or dead I let no
  man share it"; catches flung coins one-handed, would take a dead man's cash and
  sell the clothes off the corpse); wry to the last; only misstep, forgetting
  Lu and he were old friends and that Zhu Ting could unmake his maze.
- **Huo Tianqing** (霍天青) — proud past bearing (would surpass all men, even his
  own father); grave, low, measured; INNOCENT of Feiyan's murder — framed and
  poisoned by Huo Xiu. Renounces the Heaven's Bird sect (snaps his bamboo token)
  to spare his disciples dying for him; accepts the duel ("in a world that holds
  Huo Tianqing, there should be no Lu Xiaofeng").
- **Shangguan Feiyan** (上官飞燕) — soft, honeyed, plaintive over a viper's
  heart; lifelong resentment of the cousin-princess who outranked her (wore her
  cast-offs, ate her leavings); murdered Princess Danfeng and impersonated her;
  loved not Huo Tianqing but Huo Xiu's jewels; disavows the doomed Liu Yuhen
  coldly; dies at Huo Xiu's hand still not believing her lover could do it.
- **Shangguan Xue'er / Xue'er** (上官雪儿) — twelve, lies without a blink, threatens
  to cry "ravish" to get her way; grief for her sister real under the mischief;
  digs up the princess's body with Lu; safe at the end.
- **the Shanxi Wild Goose** (山西雁) — grave, upright; by martial generation Huo
  Tianqing's nephew though decades his elder; would break all ties if Huo Tianqing
  proved guilty; names Lu "not a little phoenix but a little fox".
- **the Taoist Qingfeng** (青枫) — the Green Wind Temple's abbot, Huo Tianqing's
  chess-friend, bought by Huo Xiu to bear false witness; burned with his temple.
- **Zhu Ting / the Boss's Wife** — Zhu Ting, heir of Master Lu (of Lu Ban's line),
  the first hand under heaven at contrivances; too lazy to be tricked; springs the
  sealed vault and jams Huo Xiu's escape. The Boss's Wife, a great beauty, the
  decoy that keeps him alive; both safe at the close.

## Renderings settled to date / carry-forward

**People:** (prior, all decided) Lu Xiaofeng, Ximen Chuixue, Hua Manlou, Zhang
Fang, Granny Xiong, Shangguan Feiyan, Little Beijing, Zhu Ting, the Iron-Faced
Judge, Soul-Hook, Liu Yuhen, Xiao Qiuyu, Dugu Fang, Princess/Shangguan Danfeng,
the Great King of the Golden Roc, Huo Xiu (old Huo) = Shangguan Mu, Dugu Yihe =
Ping Duhe, Yan Tieshan = Yan Liben, Shangguan Xue'er, Shangguan Jin, Ye Gucheng,
the Honest Monk, Master Sun, Ouyang Qing, Datong/Dazhi, Huo Tianqing, Su
Shaoqing/Su Shaoying, Ma Xingkong, the Shanxi Wild Goose, Sikong Zhaixing, Fan E
(= Master Fan the Elder), Master Jian the Second, Zhao the Pockmarked, the Two
Elders of Mount Shang, the Old Man of Heaven's Birds, Ma Xiuzhen, Sun Xiuqing
(= Sun the Second), Ye Xiuzhu, Shi Xiuxue, Cui Yidong. **B07:** 青枫 → the Taoist
Qingfeng; 鲁班 → Lu Ban (attested, real figure); 鲁大师 → Master Lu; 包乌鸦 → Bao
the Crow (inline, minor — the bun-seller of the Seven Heroes). Source slips kept
smooth: 樊天仪 rendered "Fan E" (the ch08 ledger name); 三师妹 → "our Third Sister"
(carries 3, though Sun Xiuqing was "the Second" earlier).

**Organisations:** Water Snake Gang, the Blue-Robe Tower (青衣楼; the First
Blue-Robe Tower 青衣第一楼 is Huo Xiu's mountain vault, confirmed in B07; Huo Xiu is
the Grand Helmsman 总瓢把子 of the 108 towers), the Golden Roc, the Ten Thousand
Plum Manor, the Pavilion of Pearls and Splendour, the Heaven's Bird sect, the
Seven Heroes of the Marketplace, the Four Beauties of Emei.

**Places:** Jiangnan, the Nine Provinces, Guanzhong, the Central Lands, Emei,
Yanbei, Shanxi, the Qilian Mountains, Mount Tai, Taiyuan, Yet Another Village.
**B07:** 青风观 → the Green Wind Temple (the abbot 青枫/Qingfeng's name chimes with
it — glossed in the glossary note, not footnoted).

**Terms / epithets (inline unless noted):** jianghu, lightness-skill, guqin,
living Bodhisattva, wangba, point-sealing, judge's pens, the Flying Phoenix
Needles, Bamboo-Leaf Green, Huadiao, Daughter's Red, Luzhou Daqu, the
Virgin-Body discipline, the red dust, the maze signs Push/Turn/Stop/Drink/Smash.
**B07 (inline):** 灵犀一指/心有灵犀 → "heart and finger were of one mind" (Lu's
Spirit-Skewering Finger); 飞燕针 → the Flying Swallow Needle (set against the
Flying Phoenix Needles — the swallow/phoenix pun mirrors Feiyan/Danfeng); 总瓢把子
→ the Grand Helmsman; 玉枕穴 → the Jade Pillow point; 黄泉 → the Yellow Springs;
尺 → chi (period unit); 时辰 → "hours". **B07 (footnoted):** the six-toe 異相
physiognomy; 愿生生世世莫生于帝王家 (the Liu-Song abdication lament); Tian Dan /
Emperor Guangwu / Li Houzhu / Song Huizong + 诗书画 three perfections; 多情自古空余恨
(the couplet & the pun on Liu Yuhen's name); 鲁班 Lu Ban; 请君入瓮 (invite the
ruler into the urn).

**Money/units — DECIDED:** keep period units (cash / catty / tael / li / cun /
zhang / chi) with footnotes, book-wide, no domestication. **authority.json**
still holds no wuxia terms; feed the decided renderings back on completion (B08).

## Where the book stands (story state)

- Prologue (ch01) → Chapter 10 (ch11): as before — the King's contract; the
  cast assembled; the Blue-Robe Tower's murders; the Pavilion feast; Yan
  Tieshan unmasked and killed; the Four Beauties of Emei; Dugu Yihe halved by
  Huo Tianqing then killed by Ximen; Sun Xiuqing carried off, Shi Xiuxue dead;
  Feiyan flees Hua; the threat-verse; Lu and Hua climb to Huo Xiu's Maze Tower,
  past the four mad "Kings", and find Huo Xiu warming wine.
- **Chapter 11 (ch12 第六根足趾 "The Sixth Toe") — the climax, resolved:** see the
  B07 entry in "What is DONE" above. In sum: the six-toe mark; every "Great King"
  an impostor; the true King and Danfeng long dead; Feiyan the sub-plotter,
  confessed and then silenced; Huo Tianqing framed and murdered; **Huo Xiu the
  arch-villain, caged in his own trap by Zhu Ting.** Xue'er and the Boss's Wife
  safe; Danfeng's six-toed body dug up and identified.

## What is NEXT

- **B08 = ch13 (第十二章 尾声 "Coda") + WHOLE-BOOK COMPLETION** — the FINAL batch.
  The short coda (~2.8k, one scene, no dividers) opens with Zhu Ting having
  sprung the door (the "Heaven's will" was Zhu Ting all along) and closes the
  volume; two publisher end-matter lines (the "完"/END marker and a teaser for
  Legend of Lu Xiaofeng 2: The Embroidery Bandit) must be handled and recorded,
  not dropped. Then ALL the completion tasks: check_reconcile, ~20 grep-count
  drift checks, a 3–5% fixed-seed deep audit (out/deep_audit.md), out/
  term_ledger.md, authority.json feedback, COMPLETION.md, the final EPUB
  force-committed, and this HANDOFF rewritten to COMPLETE.

## Traps / environment

- Stray-branch trap: each session starts on a stray per-task branch;
  consolidate onto claude/lu-xiaofeng-1 (rule 2) and delete the stray.
- ch2–ch12: bare-numeric dividers (01, 02, ...) render as `***`, hand-inserted
  after split_bilingual (build takes the cumulative paragraph counts). **ch13 has
  none.** The **kickoff-vs-source scene-count slip** in B07 (source has 4 markers,
  not "5 scenes") is a reminder to grep the markers yourself, not trust prose.
- make_bilingual skip=2 every unit (line 1 running-title stub, line 2 chapter
  title). Confirm per unit.
- Extractor splits: a line whose last char is not terminal punctuation continues
  the next — EXCEPT a colon-terminated lead-in to a quoted letter/verse. ch12 had
  NONE (re-verified). ch13 has em-dash interior monologue — check per line.
- **Number check**: 两 tael (noised after 十/百/千/万/多/把); 合十's 十; digit form
  for 4-digit numbers (1,980); leading "one" for 一百零八; four-directions 四X;
  fen-as-tenths 三分/五成. NEVER noise a real quantity.
- **Register metric counts ONLY n't/'ll/'re/'ve/'m.** Contract ordinary speakers
  inside dialogue (contract_dialogue.py); leave narration, classical quotes, and
  the grave duel line.
- verify_unit.py self-locates data/noise.txt — do NOT pass it `--noise`.
- data/src and data/src_epub are gitignored (regenerate with ingest_epub.py);
  source.epub and data/figs (the cover) ARE tracked. The deliverable EPUB is
  gitignored and attached in chat each batch; **force-commit it (`git add -f`)
  on the FINAL batch (B08).**
- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar. The number/verify checks over
  ~1200 pairs run for minutes — background them.
- English chapter titles in book.json are provisional; verify against the text
  (ch12 "The Sixth Toe" confirmed; confirm ch13 "Coda").
```
