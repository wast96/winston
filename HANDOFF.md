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
Lu Xiaofeng 1 B06

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 金鹏王朝 (The Golden Roc Dynasty), Volume 1 of Gu Long's Legend of Lu Xiaofeng, from a digital source EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/lu-xiaofeng-1; expect the harness to start you on a stray per-task branch and consolidate per rule 2 (check out claude/lu-xiaofeng-1, reset to origin, and if a stray branch carries commits, fast-forward or cherry-pick them on, push, and delete the stray).  Deliverable out/lu-xiaofeng-1.epub.

Run ./setup.sh first and record any failure in PROGRESS.md. NOTE: the regression harness reports 9/10 green with ONE expected failure ("hook stands down on template stub") — that case only passes while HANDOFF.md holds the template placeholder; now that HANDOFF carries a real kickoff the Stop hook correctly enforces, so that one test necessarily reads FAIL for the rest of the book. Not a defect; do not "fix" it. data/src and data/src_epub are gitignored and regenerable: if they are missing, run scripts/ingest_epub.py source.epub (do NOT overwrite book.json). This book has NO source-edition footnotes; re-grep each unit's source for \[\d+\] and record "none present" per unit in PROGRESS.md.

ch01 remains the FROZEN REFERENCE for register and PARAGRAPHING. Before translating, READ out/ch07_reading.md (Pearls and Splendour) AND out/ch08_reading.md (The Seven Heroes of the Marketplace) end to end — those are the freshest voice, plus ch05/ch06 as needed. Study STYLE.md, HANDOFF's "Paragraphing", "Attribution", and the voice sheets (Lu Xiaofeng, Ximen Chuixue, Hua Manlou, Princess Danfeng, the Great King, Shangguan Xue'er, old Huo/Huo Xiu, the Honest Monk, Master Sun, Ouyang Qing, Huo Tianqing, the Shanxi Wild Goose, Sikong Zhaixing, Su Shaoying, and the bun-pedlar are all written in HANDOFF). Money/units are SETTLED: keep the period units (cash / catty / tael / li / cun / zhang) with footnotes, no domestication. Watch comma density; em dashes sparingly; contractions measured (and note the register metric counts only n't/'ll/'re/'ve/'m, not 's/'d). Consult glossary.json (now 76 rows) and authority.json BEFORE romanizing anything.

Do Batch B06 = Chapters 8-10 (ch09 第八章 峨嵋四秀 "The Four Beauties of Emei", ~10,307 chars, text_file data/src/14_part0000-split-012.txt, dividers at source lines 3/26/117/176/239 = 5 scenes; ch10 第九章 飞燕去来 "The Flying Swallow Comes and Goes", ~8,477 chars, text_file data/src/15_part0000-split-013.txt, dividers 3/106 = 2 scenes; ch11 第十章 迷楼 "The Maze Tower", ~8,490 chars, text_file data/src/16_part0000-split-014.txt, dividers 3/112/179/234 = 4 scenes), end to end per the CLAUDE.md pipeline:
1. Read each unit's source. Fix extractor-split paragraphs (a line whose last char is not in 。！？"）…— continues the next; re-check per unit — a colon-terminated lead-in to a quoted letter/verse is NOT a split, cf. ch08 line 222). Chapters 1-12 divide themselves with BARE NUMERIC markers (01, 02, ...) that are scene breaks: recover them as *** (COPY scratchpad/build_b05.py, which reads English one-paragraph-per-line from scratchpad/<id>_en.txt and JSON-encodes it — re-range the CH-lists and the builder calls for ch09/ch10/ch11 using the spans/singles helpers; find the divider line numbers with grep for the ^0[0-9] markers, EXCLUDE them from the merged source, and pass the after-paragraph indices as the breaks list). build_b05.py and scratchpad/qc_config.json are COMMITTED (in scratchpad/) — reuse them; if scratchpad is empty on a fresh container, they are in git under scratchpad/.
2. Translate to the frozen house style (read STYLE.md and the reading.md files): fluent, literary, image-forward, economical; MERGE narration into paragraphs by beat, keep dialogue turns and punch-lines on their own; recast freely; watch comma density. ATTRIBUTION RULE (load-bearing for the checks): every dialogue turn whose source names a CAPITALISED-glossary character (Lu Xiaofeng, Princess Danfeng, Ximen Chuixue, Hua Manlou, Huo Tianqing, Sikong Zhaixing, Su Shaoying, Mount Tai, Emei, ...) MUST carry that full rendering once, via a natural "said X" attribution or an action beat — otherwise check_content, qc_entities, AND check_align all flag it. Lowercase-"the" names (the Shanxi Wild Goose, the Two Elders of Mount Shang, the Heaven's Bird sect, the Seven Heroes of the Marketplace, the Blue-Robe Tower, jianghu) are exempt from check_content and pass qc_entities trivially via first-word "the". Never invent bridging text; render digitization glitches to plain sense and LIST each in PROGRESS.md; source errors of fact stay visible and get a footnote. Verify each chapter's TAIL against the source before shipping.
3. Author out/ch0N_en.json as MERGED English paragraphs (author them into scratchpad/ch0N_en.txt, one paragraph per line — the build_b05.py method JSON-encodes it, so no quote-escaping to fight); build via the merged-source method (build_b05.py pattern): it runs make_bilingual.py ch0N <merged_src> "<chapter title>" out/ch0N_en.json 2, inserts the bare-numeric -> *** scene breaks, split_bilingual.py. Then verify_unit.py ch0N (parity + numbers with the built-in data/noise.txt + anchors — do NOT pass --noise to verify_unit, it self-locates the file); check_align.py ch0N; check_content.py --config scratchpad/qc_config.json (extend docs/sources to add ch09/ch10/ch11); qc_entities.py out/ch0N_bilingual.md glossary.json. WATCH THE NUMBER CHECK for tael 两 (patterns after 十/百/千/万/多 are in noise; a NEW amount pattern may need a new documented lookbehind — see PROGRESS B02/B03) and for colour/direction/set idioms (五色/五彩/四射/四下/四溅/丑八怪/十足十/六亲不认/飘零/五成/千古 already noised). Spelled numbers must use the tens-ones form ("forty-nine", not "nine-and-forty") or the matcher misses them; "ten thousand" needs a SPACE, not a hyphen.
4. Footnotes per the reader model (Western reader, no Chinese background); first-appearance greps + a NOT-re-noted list per unit; density keeps tapering (expect ~4-6/chapter). Use apparatus_merge.py for NOTES only (its glossary path adds rows FLAT and must NOT be used — add glossary rows under the two-level sections directly, e.g. a json.load/dump helper like scratchpad/add_glossary_b05.py, and validate with check_apparatus.py). check_apparatus.py clean.
5. Rebuild (scripts/build_reading_epub.py), qa_epub.py green, epubcheck (/tmp/epubcheck-5.1.0/epubcheck.jar) clean, check_structure.py --config scratchpad/qc_config.json PASS, check_register.py --ref out/ch01_reading.md out/ch09_reading.md out/ch10_reading.md out/ch11_reading.md within tolerance (>=0.45x; the metric counts only n't/'ll/'re/'ve/'m — leave Ximen Chuixue's monosyllabic register and quoted classical/verse UNcontracted, contract the ordinary speakers). Record every check in PROGRESS.md; update HANDOFF.md; commit and push to claude/lu-xiaofeng-1.
6. End the batch per CLAUDE.md: attach the rebuilt out/lu-xiaofeng-1.epub in the chat AND paste the B07 kickoff verbatim in the same reply.

Cite chapters and sections, never pages. Do not pause for approval mid-batch (B06 is a normal batch, no gate).
```

## What is DONE (do not redo)

- **Step 0 survey** (prior session): ingested the source, authored book.json
  (13 units), built the skeleton EPUB.
- **B01 = Prologue (ch01)** — COMPLETE, revised at the voice gate (rounds 2-5).
  4 vignettes; 154 paragraphs; 15 footnotes. **ch01 is the FROZEN REGISTER
  REFERENCE** (contractions 40.3/1k, rhythm CV 0.75).
- **B02 = Chapter 1 (ch02)** — COMPLETE. 289 merged paragraphs; 11 footnotes.
- **B03 = Chapters 2-3 (ch03 + ch04)** — COMPLETE. ch03 323 paras / 4 notes;
  ch04 333 paras / 6 notes.
- **B04 = Chapters 4-5 (ch05 盛宴 + ch06 悲歌)** — COMPLETE. ch05 306 paras /
  6 notes; ch06 272 paras / 4 notes. 10 glossary rows (63 total).
- **B05 = Chapters 6-7 (ch07 珠光宝气 + ch08 市井七侠)** — COMPLETE. ch07: 226
  merged paragraphs (3 scenes), 4 footnotes. ch08: 346 merged paragraphs (3
  scenes), 6 footnotes. 13 new glossary rows (76 total). Every check green:
  numbers 0 unresolved both units, align no strays (median 4.33 / 4.23),
  content all-in-paragraph (226 / 257 occurrences), qc_entities 0 misses,
  apparatus 0/0, structure ALL PASS (56 anchors), qa_epub PASS, epubcheck 5.1.0
  0/0/0/0, register 0.50x (ch07) / 0.77x (ch08) within tolerance. **Yan Tieshan
  is unmasked as the traitor Yan Liben and dies; Ximen Chuixue slaughters his
  bought blades and Su Shaoying of Emei; Princess Danfeng takes her own revenge
  from the lotus pond; Huo Tianqing challenges Lu, then calls the duel off by
  letter; the Shanxi Wild Goose and the Seven Heroes of the Marketplace fail to
  drive Lu off; the Blue-Robe Tower fire-bombs the tavern; Sikong Zhaixing (in
  the dog-cook's skin) reveals someone has paid 200,000 taels to steal the
  Princess away, and holds the arsonists for Lu to question.**

## Tooling in place (do NOT revert)

- `scratchpad/build_b05.py` — the CURRENT merged-paragraph builder. It reads the
  English one-paragraph-per-line from `scratchpad/<id>_en.txt` (so no
  JSON-escaping is hand-fought across hundreds of paragraphs), asserts
  `len(RANGES) == len(en lines)`, writes `out/<id>_en.json`, builds the merged
  source (dividers EXCLUDED), make_bilingual, split_bilingual, then post-inserts
  `***`. COMMITTED. Copy + re-range per new unit; `python3
  scratchpad/build_b05.py ch09` runs one unit. `scratchpad/qc_config.json` — the
  check_content / check_structure config ({docs, sources, notes}); extend for
  each new unit. `scratchpad/add_glossary_b05.py` — the json.load/dump glossary
  helper (adds rows under the two-level sections; NOT the flat apparatus path).
  All COMMITTED. (build_b03.py / build_b04.py remain as earlier copies.)
- `data/noise.txt`: B01 (`第二天`), B02 (王八蛋/王八/三七二十一/十-shape/四顾/
  百炼/四平八稳/四分五裂/五彩缤纷/`(?<=[百千万萬])两`), B03 (`(?<=十)两一(?=锭)`
  then `(?<=十)两` then `(?<=多)两` — ORDER load-bearing — 丑八怪/五色缤纷/
  五色/五彩/四射), B04 (`十足十`/`六亲不认`/`飘零`), **B05 additions**: `五成`
  (fraction idiom = "half"), `四下` (all-sides idiom), `四溅` (sparks-splash
  idiom), `千古` (through-the-ages, 千 figurative). Each documented in-file; all
  justified by real flags. Keep.
- **glossary.json is TWO-LEVEL** (`section -> {zh: row}`). `apparatus_merge.py`
  adds glossary rows FLAT, which the builder/qc choke on. **Use apparatus_merge
  for NOTES only; add glossary rows under sections directly (add_glossary_b05.py
  or Edit/Write) and validate with check_apparatus.py.** Strip any `glossary`
  block from the batch apparatus JSON before merging.
- `scripts/check_content.py`, `check_align.py`, `check_numbers.py`,
  `check_structure.py`, `verify_unit.py`: the `***`-skip and spelled-number
  patches are load-bearing. Do not revert. **verify_unit self-locates
  data/noise.txt — do NOT pass it `--noise` (that adds phantom cids and crashes
  the anchor step).**
- **Regression harness**: `./setup.sh` reports FAILED but 9/10 with ONE EXPECTED
  failure (`hook stands down on template stub`). Not a defect.

## Paragraphing (book-wide rule — do NOT revert)

The commissioner rejected 1:1 rendering as too choppy. **MERGE adjacent
narration lines into paragraphs grouped by beat; keep dialogue turns and
deliberate punch-lines on their own.** Method (preserves every pipeline
guarantee):

1. Author the MERGED English paragraphs into `scratchpad/<id>_en.txt`, one
   paragraph per line, reading order.
2. Group source body lines into the same paragraphs; the builder concatenates
   each group's original lines VERBATIM (join with '' — every body line ends on
   terminal punctuation; check per unit). `make_bilingual.py <id> <merged_src>
   <title> en.json 2` → parity + verbatim by construction, then
   `split_bilingual.py`. (See `scratchpad/build_b05.py`; the range lists use the
   `spans`/`singles` helpers, dividers EXCLUDED.)
3. **Scene breaks** (ch02-ch12): the source's bare-numeric markers (01, 02, ...)
   are EXCLUDED from the merged source; `***` is post-inserted into
   `out/<id>_reading.md` after the paragraph that ends each scene (build takes
   the list of after-paragraph indices — count them off the drafted en.txt).
4. All checks run on the merged pairs (`***` skipped everywhere).

## Attribution (load-bearing — do NOT drop)

Rapid dialogue must name its speaker or three checks fail at once
(`check_content` wants each CAPITALISED glossary name in every paragraph its
source attributes to that character; `qc_entities` wants the first/last name-word;
bare interjections are `check_align` ratio outliers). **Give each dialogue turn
the character's full name once via a natural attribution ("said Lu Xiaofeng",
"Ximen Chuixue smiled", "said the Shanxi Wild Goose") then let pronouns carry
the rest.** In a two-hander, tag one speaker consistently and vary the other
with action beats (a long Lu ↔ Sikong Zhaixing two-hander in ch08 named both
every turn and still read fine — Gu Long's own staccato does the same).
**Lowercase-"the" glossary names are exempt from check_content and pass
qc_entities trivially via the article "the".** **CAUTION: an idiom can contain a
glossary anchor** — 泰山北斗 ("supreme authority") holds 泰山/Mount Tai, so it is
rendered "the Mount Tai and Pole Star of the martial world" to satisfy the
anchor AND keep the metaphor. **Watch for DISPLACEMENT:** a paragraph whose
source names X but whose English pushed the name into a different merged
paragraph fails check_content; restore the name in-place.

## Voice / house style (the frozen register — match it exactly)

**`STYLE.md` (repo root) is the worked-example version — read it before
translating.** Fluency over literalism; economy; comma density watched; em
dashes only when they beat a comma cluster and sparingly; image-forward,
concrete diction; vary rhythm, punch-lines on their own line; contractions
measured; paragraph by beat; dialogue characterised (voice sheets); names once
then pronouns; NO invented substance; keep cultural nouns and period units,
footnoted. Read the freshest reading.md files (ch07, ch08) end to end before
translating. **Register-metric note:** `check_register` counts contractions of
the form n't/'ll/'re/'ve/'m ONLY (not 's/'d). If a chapter reads STILTED,
raise the count by converting ordinary-speaker "is not/will not/I have/you are"
to won't/isn't/I've/you're — but LEAVE Ximen Chuixue's monosyllabic killer
register, quoted classical anecdotes/letters/verse, and ceremonial
self-namings uncontracted (those are deliberate and exempt).

## Voice sheets (consult at every dialogue scene)

Earlier cast (unchanged): **Ximen Chuixue** (near-silent, absolute,
monosyllabic; killing as sacred office — reconfirmed in ch07: he cuts seven
bought blades and Su Shaoying without a wasted word; spares the boy, then kills
when goaded, mourning the adversary he will never meet in twenty years; forbids
Princess Danfeng the sword forever because "a sword is not for killing men from
behind"; breaks each used blade and vanishes into the mist), **Hua Manlou**
(gentle, warm, unhurried; serene declaratives, dry understatement; blind and
joyful; reads a man from his voice and his killing-air; in ch07 turns Ma
Xingkong out the window with a sleeve; in ch08 grieves Su Shaoying's needless
death), **Lu Xiaofeng** (the laziest, wriest man alive; sees everything;
ox-stubborn once set; CLEAN-SHAVEN and fretting his moustache back; wry,
economical, unbeatable — he breaks a steel suicide-knife with a chopstick, then
simply refuses to fight at all; won't be scared off by fire-bombs), **Princess
Danfeng / Shangguan Danfeng** (soft, dreamy, gracious low voice — but in ch07
she rises from the lotus pond in a black-sharkskin diving-suit and kills Yan
Tieshan from behind, all hatred and venom; wounded by Xue'er's slander;
defiant; warming to Lu — the interrupted bed-scene resumes in ch08's rain
before the arson breaks it), **the Great King of the Golden Roc** (fallen
monarch's ceremonial, archaic register — no scene this batch), **old Huo / Huo
Xiu** (dry, terse — no scene this batch), **Shangguan Xue'er** ("a body"-speech
little goblin; her ch06 "Flying Phoenix Needles" accusation is tested in ch07
and proves a lie — Danfeng has never heard the words), **the Honest Monk**,
**Master Sun**, **Ouyang Qing** (no scene this batch).

**New in B05:**

- **Huo Tianqing** (霍天青) — low, strong, MEASURED voice; speaks slowly so
  every ear turns and every word is heard; supremely self-assured, proud but
  will not be thought proud; cold and unmoving under Ximen's blade and Danfeng's
  attack ("Not that I daren't. That I won't"). Sole bloodline heir of the
  Heaven's Bird sect, terribly high in generation despite being under thirty.
  Bound to Yan Tieshan by a 国士 debt; his grief for Yan shows as NO expression
  ("no expression is often the most grieving of all"). Challenges Lu to a
  sunrise duel out of that debt — then calls it off in a letter of high
  classical honour (明日黄花 / 义气两字), having weighed loyalty against loyalty.
  A latent ally.
- **the Shanxi Wild Goose** (山西雁) — a bald, sallow, boorish country-codger on
  the surface; underneath, the great hero of Guanzhong, thirty years famed for
  his twin iron palms, Huo Tianqing's martial-NEPHEW. Rough, hearty, "his
  mother's" (他娘的) at every breath; blunt and self-mocking ("you're a great
  plague, I'm a great good man"); eats a wine-cup like broad beans. Would die
  for Huo but WILL NOT scheme dishonourably — when Danfeng accuses him of it he
  laughs wildly and owns he could never. Loyal, plain, grieving under the bluff.
- **Sikong Zhaixing** (司空摘星) — the king of thieves; proud, playful, roguish.
  Steals only on a wager, never anything of value; being robbed by him is an
  honour. Master of "changing faces" (disguise) — wore Zhao the Pockmarked's
  skin so well even Lu was fooled, until the somersaults gave him away. Throws
  out his chest, banters, keeps a client's secret to the grave — but "even
  thieves have their Way" (盗亦有道): he spares the theft and avenges the arson
  because Lu risked the fire to save "him."
- **the bun-pedlar** (卖包子的小贩, one of the Seven Heroes) — cold, deadpan,
  tough, fearless; hawks human-flesh dog-poison buns and jokes about it; stacks
  his buns eight chi high and balances on one leg; ready to cut his own throat
  sooner than fail Huo Tianqing; wry and generous once Lu bests and befriends
  him.
- **Su Shaoying** (苏少英, alias 苏少卿) — gentle scholarly surface (the Yan
  tutor), hot-blooded youth beneath; proud of Emei; wields Dugu Yihe's own
  Saber-and-Sword Double Kill. Spared by Ximen Chuixue ("come again in twenty
  years"), he cannot bear the wait and rushes to his death; Hua Manlou mourns
  him.

## Renderings settled to date / carry-forward

**People:** Lu Xiaofeng, Ximen Chuixue, Hua Manlou, Zhang Fang, Granny Xiong,
Shangguan Feiyan, Little Beijing, Zhu Ting, the Iron-Faced Judge, Soul-Hook,
Liu Yuhen, Xiao Qiuyu, Dugu Fang, the Four Heroes of Jiangdong, Princess
Danfeng / Shangguan Danfeng, the Great King of the Golden Roc, Huo Xiu (old
Huo), Dugu Yihe (NOT Dugu Fang), Yan Tieshan, Shangguan Xue'er, Shangguan Jin,
Shangguan Mu / Ping Duhe / Yan Liben (traitors' names), Ye Gucheng, the Honest
Monk, Master Sun, Ouyang Qing, Datong / Dazhi, Huo Tianqing. **B05:** Su
Shaoqing / Su Shaoying (the alias and the real name — Su the Second of the
Three Heroes and Four Beauties), Ma Xingkong (云里神龙 → the Divine Dragon in
the Clouds), the Shanxi Wild Goose (山西雁), Sikong Zhaixing (司空摘星, the king
of thieves), Fan E (樊鹗, Master Fan the Elder), Master Jian the Second
(简二先生), Zhao the Pockmarked (赵大麻子), the Two Elders of Mount Shang
(商山二老), the Old Man of Heaven's Birds (天禽老人). **NOTE the two Yan
surnames:** 阎铁珊 (Yan Tieshan) and 严立本 (Yan Liben) are ONE man — the source
uses both, and the ch07 unmasking turns on the pair.

**Organisations:** Water Snake Gang, the Blue-Robe Tower (青衣楼 — head secretly
Dugu Yihe; fire-bombs the tavern in ch08), the Golden Roc (金鹏王朝), the Ten
Thousand Plum Manor, the Pavilion of Pearls and Splendour (珠光宝气阁 / 阎府).
**B05:** the Heaven's Bird sect (天禽门, Huo Tianqing's school), the Seven Heroes
of the Marketplace (市井七侠; 山西七义 → the Seven Righteous of Shanxi, inline).

**Places:** Jiangnan, the Nine Provinces, Guanzhong, the Central Lands, Emei,
Yanbei, Shanxi, the Qilian Mountains. **B05:** Mount Tai (泰山, glossary +
footnote; BEWARE 泰山北斗 idiom → "Mount Tai and Pole Star"), Taiyuan (太原,
inline), Yet Another Village (又一村, the tavern, inline).

**Terms / epithets (inline unless noted):** jianghu, lightness-skill (qinggong),
guqin, living Bodhisattva, wangba, point-sealing (dianxue), judge's pens, the
Flying Phoenix Needles, Bamboo-Leaf Green, Huadiao. **B05:** the Seven Swords
of Emei / Three Heroes and Four Beauties (峨嵋七剑 / 三英四秀), the Saber-and-Sword
Double Kill (刀剑双杀七七四十九式 → "seven times seven, the forty-nine forms"),
Twin Painted Wings (双飞彩翼), "the hearts that beat as one through a single
thread" (心有灵犀一点通, Li Shangyin, footnoted), the Twin Perfections of
Guanzhong (关中双绝), the Finger-Flicking art (弹指神通), the fish-scaled
coiling-dragon rod of purple gold (Ma Xingkong's weapon), the
swallow's-three-skimmings (燕子三抄水), sulphur-and-saltpetre thunderbolts
(硝磺霹雳弹).

**Money/units — DECIDED:** keep period units (cash / catty / tael / li / cun /
zhang) with footnotes, book-wide, no domestication. **authority.json** still
holds no wuxia terms; feed decided renderings back on completion (final batch).

## Where the book stands (story state)

- Prologue (ch01) → Chapter 5 (ch06): as before — the King's contract; the cast
  (Ximen Chuixue, Zhu Ting, Hua Manlou) assembled; Xiao Qiuyu and Dugu Fang
  murdered by the Blue-Robe Tower; Xue'er's accusation of Princess Danfeng;
  Liu Yuhen alive; Huo Tianqing's invitation.
- **Chapter 6 (ch07):** The feast at the Pavilion of Pearls and Splendour. Su
  Shaoqing's Southern-Tang pearl anecdote. Lu names "Steward Yan" and unmasks
  the host Yan Tieshan as the traitor Yan Liben; Yan calls in bought fighters;
  Ximen Chuixue arrives and cuts down all seven, and Su Shaoying of Emei
  (Dugu Yihe's disciple). Princess Danfeng rises from the lotus pond in a
  sharkskin diving-suit and runs Yan through from behind; Ximen forbids her the
  sword forever. Huo Tianqing, grieving without expression, holds Lu answerable
  for Yan's death and challenges him to a sunrise duel at the Green Wind Temple.
  Lu tests Xue'er's "Flying Phoenix Needles" story on Danfeng — she has never
  heard the words; Xue'er lied. Danfeng weeps.
- **Chapter 7 (ch08):** At the inn before the duel, the Shanxi Wild Goose (Huo's
  martial-nephew) and the Seven Heroes of the Marketplace gather to force Lu to
  leave, to spare Huo Tianqing. Lu breaks the bun-pedlar's suicide-knife with a
  chopstick and simply agrees to go — no fight. Huo's letter arrives calling the
  duel off ("honour and duty alone shine down the ages"). Then the Blue-Robe
  Tower fire-bombs "Zhao the Pockmarked's" tavern with thunderbolt-bombs ("a
  small lesson"). Lu survives; the dog-cook is revealed as Sikong Zhaixing, the
  king of thieves in disguise, who cut off the arsonists' hands, and reveals
  that someone paid 200,000 taels to have the Princess stolen away — "not in the
  way you're thinking." The arsonists wait bound in the wood for Lu to question.

## What is NEXT

- **B06 = ch09 (第八章 峨嵋四秀 The Four Beauties of Emei) + ch10 (第九章 飞燕去来
  The Flying Swallow Comes and Goes) + ch11 (第十章 迷楼 The Maze Tower)**. The
  Emei beauties land (foreshadowed since ch04/ch05); Shangguan Feiyan's thread
  resurfaces (飞燕 = flying swallow); the Maze Tower. Interrogate the arsonists;
  who paid to steal the Princess; the Blue-Robe Tower / Dugu Yihe closes in.
- Then: B07 ch12 (the ~31k climax 第十一章 第六根手指 / "The Sixth Toe"), B08
  ch13 (coda) + back matter / reconciliation / completion.

## Traps / environment

- Stray-branch trap: each session starts on a stray per-task branch;
  consolidate onto claude/lu-xiaofeng-1 (rule 2) and delete the stray.
- ch2 onward: bare-numeric dividers (01, 02, ...) render as `***` scene breaks,
  NOT TOC sections; hand-inserted after split_bilingual (build_b05.py takes the
  after-paragraph indices). `apply_format_markers.py` finds nothing in this
  book's HTML.
- make_bilingual skip=2 every unit (line 1 running-title stub, line 2 chapter
  title). Confirm per unit.
- Extractor splits: a line whose last char is not terminal punctuation continues
  the next — EXCEPT a colon-terminated lead-in to a quoted letter/verse (ch08
  line 222 霍天青的信：), which is its own paragraph.
- **Number check**: 两 is both "two" and the tael measure word — noised after
  十/百/千/万/多. Colour/direction/set idioms hide stray numerals — noise them
  (documented, longest-first) or render so the English carries the value. NEVER
  noise a real quantity. Spelled numbers must be tens-ones ("forty-nine"); "ten
  thousand" needs a space not a hyphen.
- **Register metric counts ONLY n't/'ll/'re/'ve/'m** (not 's/'d). A confrontation
  chapter heavy with Ximen Chuixue / quoted classical text will read low; fix by
  contracting the ORDINARY speakers, not the exempt registers.
- verify_unit.py self-locates data/noise.txt — do NOT pass it `--noise`.
- data/src and data/src_epub are gitignored (regenerate with ingest_epub.py);
  source.epub and data/figs (the cover) ARE tracked. The deliverable EPUB is
  gitignored and attached in chat each batch; force-commit it (`git add -f`)
  only on the FINAL batch.
- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar.
- English chapter titles in book.json are provisional; verify against the text
  as each chapter is done (ch07 "Pearls and Splendour" / ch08 "The Seven Heroes
  of the Marketplace" confirmed).
```
