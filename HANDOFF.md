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
Lu Xiaofeng 1 B07

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 金鹏王朝 (The Golden Roc Dynasty), Volume 1 of Gu Long's Legend of Lu Xiaofeng, from a digital source EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/lu-xiaofeng-1; expect the harness to start you on a stray per-task branch and consolidate per rule 2 (check out claude/lu-xiaofeng-1, reset to origin, and if a stray branch carries commits, fast-forward or cherry-pick them on, push, and delete the stray).  Deliverable out/lu-xiaofeng-1.epub.

Run ./setup.sh first and record any failure in PROGRESS.md. NOTE: the regression harness reports 9/10 green with ONE expected failure ("hook stands down on template stub") — that case only passes while HANDOFF.md holds the template placeholder; now that HANDOFF carries a real kickoff the Stop hook correctly enforces, so that one test necessarily reads FAIL for the rest of the book. Not a defect; do not "fix" it. data/src and data/src_epub are gitignored and regenerable: if they are missing, run scripts/ingest_epub.py source.epub (do NOT overwrite book.json). This book has NO source-edition footnotes; re-grep each unit's source for \[\d+\] and record "none present" per unit in PROGRESS.md.

ch01 remains the FROZEN REFERENCE for register and PARAGRAPHING. Before translating, READ out/ch10_reading.md (The Flying Swallow Comes and Goes) AND out/ch11_reading.md (The Maze Tower) end to end — those are the freshest voice, plus ch08/ch09 as needed. Study STYLE.md, HANDOFF's "Paragraphing", "Attribution", and the voice sheets (Lu Xiaofeng, Ximen Chuixue, Hua Manlou, Princess/Shangguan Danfeng, Huo Tianqing, the Shanxi Wild Goose, Sikong Zhaixing, Huo Xiu/old Huo, Shangguan Feiyan, and the four beauties Ma Xiuzhen/Sun Xiuqing/Ye Xiuzhu/Shi Xiuxue are all written in HANDOFF). Money/units are SETTLED: keep the period units (cash / catty / tael / li / cun / zhang) with footnotes, no domestication. Watch comma density; em dashes sparingly; contractions measured (and note the register metric counts only n't/'ll/'re/'ve/'m, not 's/'d). Consult glossary.json (now 81 rows) and authority.json BEFORE romanizing anything.

Do Batch B07 = Chapter 11, the climax (ch12 第十一章 第六根足趾 "The Sixth Toe", ~31,104 chars, text_file data/src/17_part0000-split-015.txt, dividers at source lines 3/161/203/363 = 5 scenes). NOTE: this is the long climax; scene 5 (after divider line 363) runs ~877 source lines on its own — budget the pass accordingly and verify its TAIL against the source explicitly (rule 4 corollary: on a long unit the tail is where faithfulness fails). Run end to end per the CLAUDE.md pipeline:
1. Read the unit's source. Fix extractor-split paragraphs (a line whose last char is not in 。！？"）…— continues the next; re-check per unit — a colon-terminated lead-in to a quoted letter/verse is NOT a split). A survey of ch12 found NO extractor splits, but re-verify. Chapters 1-12 divide themselves with BARE NUMERIC markers (01, 02, ...) that are scene breaks: recover them as *** (COPY scratchpad/build_b06.py, which reads English one-paragraph-per-line from scratchpad/<id>_en.txt and JSON-encodes it — re-range the CH-list and the builder call for ch12 using the spans/singles helpers; the divider line numbers are 3/161/203/363, EXCLUDE them from the merged source, and pass the after-paragraph indices as the breaks list). build_b06.py and scratchpad/qc_config.json are COMMITTED (in scratchpad/) — reuse them.
2. Translate to the frozen house style (read STYLE.md and the reading.md files): fluent, literary, image-forward, economical; MERGE narration into paragraphs by beat, keep dialogue turns and punch-lines on their own; recast freely; watch comma density. ATTRIBUTION RULE (load-bearing for the checks): every dialogue turn whose source names a CAPITALISED-glossary character (Lu Xiaofeng, Shangguan Danfeng, Shangguan Feiyan, Ximen Chuixue, Hua Manlou, Huo Tianqing, Huo Xiu, Sikong Zhaixing, the Great King of the Golden Roc, Ma Xiuzhen, ...) MUST carry that full rendering once, via a natural "said X" attribution or an action beat — otherwise check_content, qc_entities, AND check_align all flag it. Lowercase-"the" names (the Shanxi Wild Goose, the Two Elders of Mount Shang, the Heaven's Bird sect, the Blue-Robe Tower, the Four Beauties of Emei, jianghu) are exempt from check_content and pass qc_entities trivially via first-word "the". Never invent bridging text; render digitization glitches to plain sense and LIST each in PROGRESS.md; source errors of fact stay visible and get a footnote. Verify the chapter's TAIL against the source before shipping.
3. Author out/ch12_en.json as MERGED English paragraphs (author them into scratchpad/ch12_en.txt, one paragraph per line — the build_b06.py method JSON-encodes it, so no quote-escaping to fight); build via the merged-source method (build_b06.py pattern): it runs make_bilingual.py ch12 <merged_src> "Chapter 11. The Sixth Toe" out/ch12_en.json 2, inserts the bare-numeric -> *** scene breaks, split_bilingual.py. Then verify_unit.py ch12 (parity + numbers with the built-in data/noise.txt + anchors — do NOT pass --noise to verify_unit); check_align.py ch12; check_content.py --config scratchpad/qc_config.json (ch12 already in the config docs/sources); qc_entities.py out/ch12_bilingual.md glossary.json. WATCH THE NUMBER CHECK for tael 两 (patterns after 十/百/千/万/多 are in noise; a NEW amount pattern may need a new documented lookbehind) and for colour/direction/set idioms (五色/五彩/四射/四下/四溅/丑八怪/十足十/六亲不认/飘零/五成/千古/三分之一/四分之一/胡说八道/万贯 already noised). Spelled numbers must use the tens-ones form ("forty-nine", not "nine-and-forty"); "ten thousand" needs a SPACE, not a hyphen; 一百零八 → "one hundred and eight" (the leading "one" is needed or the matcher misses it).
4. Footnotes per the reader model (Western reader, no Chinese background); first-appearance greps + a NOT-re-noted list per unit; density keeps tapering (expect ~4-6). The "第六根足趾"/sixth-toe reveal is the volume's central mystery — footnote whatever real-world logic (physiognomy, dynastic legitimacy, the sixth digit) a Western reader needs, without spoiling or inventing. Use apparatus_merge.py for NOTES only (its glossary path adds rows FLAT and must NOT be used — add glossary rows under the two-level sections directly, e.g. scratchpad/add_glossary_b06.py, and validate with check_apparatus.py). check_apparatus.py clean.
5. Rebuild (scripts/build_reading_epub.py), qa_epub.py green, epubcheck (/tmp/epubcheck-5.1.0/epubcheck.jar) clean, check_structure.py --config scratchpad/qc_config.json PASS, check_register.py --ref out/ch01_reading.md out/ch12_reading.md within tolerance (>=0.45x; the metric counts only n't/'ll/'re/'ve/'m — leave Ximen Chuixue's monosyllabic register, the mad "Kings"' archaic royal register, and quoted classical/verse UNcontracted, contract the ordinary speakers). Record every check in PROGRESS.md; update HANDOFF.md; commit and push to claude/lu-xiaofeng-1.
6. End the batch per CLAUDE.md: attach the rebuilt out/lu-xiaofeng-1.epub in the chat AND paste the B08 kickoff verbatim in the same reply.

Cite chapters and sections, never pages. Do not pause for approval mid-batch (B07 is a normal batch, no gate).
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
  ch09 283 merged paragraphs (5 scenes) / 4 notes; ch10 237 (2 scenes) / 4;
  ch11 289 (4 scenes) / 5. 5 new glossary rows (81 total). Every check green:
  numbers 0 unresolved all three, align no strays (median 4.11 / 4.09 / 4.21),
  content all-in-paragraph (305 / 257 / 269), qc_entities 0 misses, apparatus
  0/0, structure ALL PASS (69 anchors), qa_epub PASS, epubcheck 5.1.0 0/0/0/0,
  register 0.63x (ch09) / 0.72x (ch10) / 0.59x (ch11) within tolerance. **The
  four Emei beauties waylay Lu in his bath; Ximen Chuixue kills Dugu Yihe (=
  the traitor Ping Duhe) after Huo Tianqing has already halved his force with
  the Paired Phoenixes in Flight; Dugu dies crying "I understand!"; black
  poisoned needles cut down Sun Xiuqing (carried off by Ximen through the
  window) and Shi Xiuxue (dead in Hua Manlou's arms); Shangguan Feiyan, in Huo
  Xiu's power, comes to warn/kill Hua and flees; Shangguan Danfeng never
  reaches the Pavilion (carried off) and a phoenix-pun threat-verse warns Lu to
  turn back; Lu and Hua climb Huo Xiu's mountain "Maze Tower," pass a hall of
  four mad "Great Kings of the Golden Roc," and find Huo Xiu warming wine on
  the floor.**

## Tooling in place (do NOT revert)

- `scratchpad/build_b06.py` — the CURRENT merged-paragraph builder (re-ranged
  copy of build_b05.py). Reads English one-paragraph-per-line from
  `scratchpad/<id>_en.txt`, asserts `len(RANGES) == len(en lines)`, writes
  `out/<id>_en.json`, builds the merged source (dividers EXCLUDED),
  make_bilingual, split_bilingual (which also writes `data/zh/<id>.txt`), then
  post-inserts `***`. COMMITTED. Copy + re-range per new unit; `python3
  scratchpad/build_b06.py ch12` runs one unit. `scratchpad/qc_config.json` — the
  check_content / check_structure config ({docs, sources, notes}); ALREADY
  extended through ch11 (add ch12? it is already listed). `scratchpad/
  add_glossary_b06.py` — the json.load/dump glossary helper (adds rows under the
  two-level sections; NOT the flat apparatus path). All COMMITTED.
  (build_b03/b04/b05.py remain as earlier copies.)
- `data/noise.txt`: B01-B05 entries (see PROGRESS), plus **B06 additions**:
  `三分之一` / `四分之一` (fraction idioms → "a third"/"a quarter"), `胡说八道`
  (the 八 idiom), `万贯` (figurative ten-thousand = immense wealth). Each
  documented in-file, all justified by real flags. Keep.
- **glossary.json is TWO-LEVEL** (`section -> {zh: row}`). `apparatus_merge.py`
  adds glossary rows FLAT, which the builder/qc choke on. **Use apparatus_merge
  for NOTES only; add glossary rows under sections directly (add_glossary_b06.py
  or Edit/Write) and validate with check_apparatus.py.**
- `scripts/check_content.py`, `check_align.py`, `check_numbers.py`,
  `check_structure.py`, `verify_unit.py`: the `***`-skip and spelled-number
  patches are load-bearing. **verify_unit self-locates data/noise.txt — do NOT
  pass it `--noise`.**
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
   `split_bilingual.py`. (See `scratchpad/build_b06.py`; the range lists use the
   `spans`/`singles` helpers, dividers EXCLUDED.)
3. **Scene breaks** (ch02-ch12): the source's bare-numeric markers (01, 02, ...)
   are EXCLUDED from the merged source; `***` is post-inserted into
   `out/<id>_reading.md` after the paragraph that ends each scene (build takes
   the list of after-paragraph indices = the cumulative paragraph count at each
   scene end — count them off the drafted en.txt).
4. All checks run on the merged pairs (`***` skipped everywhere).

## Attribution (load-bearing — do NOT drop)

Rapid dialogue must name its speaker or three checks fail at once
(`check_content` wants each CAPITALISED glossary name in every paragraph its
source attributes to that character; `qc_entities` wants the first/last
name-word; bare interjections are `check_align` ratio outliers). **Give each
dialogue turn the character's full name once via a natural attribution ("said
Lu Xiaofeng", "said Ma Xiuzhen", "Ximen Chuixue smiled") then let pronouns
carry the rest.** In a two-hander, tag both speakers each turn if needed —
Gu Long's own staccato does the same and it reads fine. **Lowercase-"the"
glossary names are exempt from check_content and pass qc_entities trivially via
the article "the".** **CAUTION: source SHORT FORMS may not trigger the check** —
上官丹凤 (the source's usual form of Princess Danfeng) is NOT the glossary key
丹凤公主, and 独孤/西门 alone are not the full keys, so those paragraphs carry no
name-requirement; still render them consistently (Shangguan Danfeng, Dugu,
Ximen). **Watch DISPLACEMENT:** a paragraph whose source names X but whose
English pushed the name into a neighbouring merged paragraph fails
check_content; restore the name in-place.

## Voice / house style (the frozen register — match it exactly)

**`STYLE.md` (repo root) is the worked-example version — read it before
translating.** Fluency over literalism; economy; comma density watched; em
dashes only when they beat a comma cluster and sparingly; image-forward,
concrete diction; vary rhythm, punch-lines on their own line; contractions
measured; paragraph by beat; dialogue characterised (voice sheets); names once
then pronouns; NO invented substance; keep cultural nouns and period units,
footnoted. Read the freshest reading.md files (ch10, ch11) end to end before
translating. **Register-metric note:** `check_register` counts contractions of
the form n't/'ll/'re/'ve/'m ONLY (not 's/'d). If a chapter reads STILTED, raise
the count by contracting ordinary-speaker "is not/will not/I have/you are" —
but LEAVE Ximen Chuixue's monosyllabic killer register, the mad "Kings"' royal
"We/Our", quoted classical anecdotes/letters/verse, and ceremonial
self-namings UNcontracted (those are deliberate and exempt).

## Voice sheets (consult at every dialogue scene)

Earlier cast (unchanged unless noted): **Ximen Chuixue** (near-silent,
absolute, monosyllabic; killing as sacred office; in ch09-10 kills Dugu Yihe,
spares then carries off the needle-struck Sun Xiuqing who loves him, saying
"I am always hungry after a killing"). **Hua Manlou** (gentle, warm, unhurried;
serene declaratives; blind and joyful; reads a man from his voice and his
killing-air; in B06 catches Shi Xiuxue's blades, then holds her as she dies of
the poison, and grieves the pitilessness of life; his lost "swallow" Feiyan
returns and flees). **Lu Xiaofeng** (the laziest, wriest man alive; sees
everything; ox-stubborn once set; wry, economical; goads an angry man for
sport; unfrightened by the Maze Tower — "when they bid me stop, I stop"). **the
Great King / Shangguan Danfeng / old Huo(=Huo Xiu) / the Shanxi Wild Goose /
Sikong Zhaixing / the Honest Monk / Master Sun / Ouyang Qing / Xue'er** — as
before.

- **Huo Tianqing** (霍天青) — low, strong, MEASURED voice; supremely
  self-assured, proud but will not be thought proud; a latent ally. In B06 he
  is grave and courteous, gives Lu the threat-verse letter and Huo Xiu's
  Daughter's Red, and quietly confirms he broke Dugu Yihe's force with the
  Paired Phoenixes in Flight before Ximen came. Master of the Heaven's Bird
  sect; will not seize the Pavilion's wealth though it lies open to him.
- **Huo Xiu / old Huo** (霍休) — the richest man under heaven living as a
  cranky recluse; = the minister Shangguan Mu. Finally SEEN at the close of B06:
  a suit of blue cloth washed white, broken straw sandals, warming wine on the
  floor from a battered pewter pot. Loathes company and women; an old bachelor;
  hoards famous wines; his mountain "Maze Tower" (108 contrivances) hides a
  vault of arms and treasure and four mad "Great Kings." His voice opens B07.

**New in B06:**

- **the four Emei beauties** (峨嵋四秀, the Four Beauties of Emei) — disciples
  of Dugu Yihe, generation-name 秀. **Ma Xiuzhen** (马秀真, 大师姐): tall,
  phoenix-eyed, cold killing air; imperious, leads, but relents and bows to Lu
  once bested in wit. **Sun Xiuqing** (孙秀青, Sun the Second): big eyes, thin
  lips, the sharpest tongue, spares no one; loves Ximen Chuixue against all
  sense; struck by a poisoned needle and carried off by Ximen (fate open).
  **Ye Xiuzhu** (叶秀珠, Miss Ye the Third): the honest, plain, blushing one.
  **Shi Xiuxue** (石秀雪, 小师妹): youngest; gentlest-seeming, hottest-tempered,
  twin short-swords; dares to love — loses her heart to Hua Manlou and dies of
  the poison in his arms.
- **Shangguan Feiyan** (上官飞燕) — the flying-swallow thief-girl of the
  Prologue, sister of Xue'er; now fallen into Huo Xiu's power, her every
  movement his to command. Soft, honeyed, plaintive; jealous of the dying Shi
  Xiuxue; torn — she loves Hua Manlou but is sent to warn (once) and to kill
  (this time) him, and cannot; she flees rather than be held. "If I am to die,
  I would die as she did, in your arms."

## Renderings settled to date / carry-forward

**People:** (prior) Lu Xiaofeng, Ximen Chuixue, Hua Manlou, Zhang Fang, Granny
Xiong, Shangguan Feiyan, Little Beijing, Zhu Ting, the Iron-Faced Judge,
Soul-Hook, Liu Yuhen, Xiao Qiuyu, Dugu Fang, Princess/Shangguan Danfeng, the
Great King of the Golden Roc, Huo Xiu (old Huo) = Shangguan Mu, Dugu Yihe (NOT
Dugu Fang) = Ping Duhe, Yan Tieshan = Yan Liben, Shangguan Xue'er, Shangguan
Jin, Ye Gucheng, the Honest Monk, Master Sun, Ouyang Qing, Datong/Dazhi, Huo
Tianqing, Su Shaoqing/Su Shaoying, Ma Xingkong, the Shanxi Wild Goose, Sikong
Zhaixing, Fan E, Master Jian the Second, Zhao the Pockmarked, the Two Elders of
Mount Shang, the Old Man of Heaven's Birds. **B06:** 马秀真 → Ma Xiuzhen; 孙秀青
→ Sun Xiuqing (孙老二 → Sun the Second, inline); 叶秀珠 → Ye Xiuzhu (叶三姑娘 →
Miss Ye the Third); 石秀雪 → Shi Xiuxue; 峨嵋四秀 → the Four Beauties of Emei;
胡道人 → the Taoist Hu / Master Hu (minor, inline). The short forms 独孤/西门
render "Dugu"/"Ximen" after the full name.

**Organisations:** Water Snake Gang, the Blue-Robe Tower (青衣楼 — the First
Tower 青衣第一楼 may be Huo Xiu's mountain tower, a B07 thread), the Golden Roc,
the Ten Thousand Plum Manor, the Pavilion of Pearls and Splendour, the Heaven's
Bird sect, the Seven Heroes of the Marketplace. **B06:** the Four Beauties of
Emei (峨嵋四秀; note the shared 秀 generation-name).

**Places:** Jiangnan, the Nine Provinces, Guanzhong, the Central Lands, Emei
(a Taoist sword-order at the Xuanzhen Temple 玄真观), Yanbei, Shanxi, the Qilian
Mountains, Mount Tai, Taiyuan, Yet Another Village.

**Terms / epithets (inline unless noted):** jianghu, lightness-skill, guqin,
living Bodhisattva, wangba, point-sealing, judge's pens, the Flying Phoenix
Needles, Bamboo-Leaf Green, Huadiao, the Seven Swords of Emei / Three Heroes
and Four Beauties, the Saber-and-Sword Double Kill (七七四十九 → "seven times
seven, the forty-nine forms"), Twin Painted Wings, the Twin Perfections of
Guanzhong, the Finger-Flicking art, the swallow's-three-skimmings,
sulphur-and-saltpetre thunderbolts. **B06 (fiction's own furniture, inline):**
the Phoenix Spreads its Wings (凤凰展翅), the Paired Phoenixes in Flight (凤双飞),
the Little Sky-Star (小天星), the Tiantu point (天突); the maze signs *Push* /
*Turn* / *Stop* / *Drink* / *Smash* (推/转/停/喝/摔, italic). **B06 (footnoted):**
Gongsun Daniang & the jianqi sword-form (剑器, Du Fu); the bagua eight-trigram
emblem & Taoist Emei; the dantian (丹田); hemp mourning-dress; the 花=Hua/flower
pun; 吃醋 "eating vinegar" = jealousy; Cao Cao's morning-dew couplet (譬如朝露);
Feiyan = "flying swallow" & the ch10 title; the Danfeng/Xiaofeng phoenix pun in
the threat-verse; Daughter's Red (女儿红); the Virgin-Body discipline (童子功);
the slow slicing (凌迟); the red dust (红尘). Luzhou Daqu / blue-and-white
porcelain / dragon-brocade robe / palace eunuchs are inline, unfootnoted.

**Money/units — DECIDED:** keep period units (cash / catty / tael / li / cun /
zhang) with footnotes, book-wide, no domestication. **authority.json** still
holds no wuxia terms; feed decided renderings back on completion (final batch).

## Where the book stands (story state)

- Prologue (ch01) → Chapter 7 (ch08): as before — the King's contract; the cast
  assembled; the Blue-Robe Tower's murders; Xue'er's accusation; the Pavilion
  feast; Yan Tieshan unmasked and killed; Ximen cuts the seven bought blades
  and Su Shaoying; Huo Tianqing's called-off duel; the tavern fire-bombed;
  Sikong Zhaixing (as the dog-cook) reveals 200,000 taels paid to steal the
  Princess.
- **Chapter 8 (ch09):** The four Emei beauties waylay Lu in his bath to
  question him, then invite him to their master (secretly Dugu Yihe) at the
  Pavilion. Ximen Chuixue fells a tree and Hua Manlou catches Shi Xiuxue's
  blades; she is smitten. Lu works out Huo Xiu = Shangguan Mu and Dugu Yihe =
  Ping Duhe. At Yan Tieshan's coffin Huo Tianqing breaks Dugu Yihe's force with
  the Paired Phoenixes in Flight; Ximen Chuixue then comes to kill him.
- **Chapter 9 (ch10):** In the carriage the beauties banter (Sun Xiuqing loves
  Ximen). By the river Ximen tells Lu that Dugu Yihe is dead — Dugu died crying
  "I understand!" then said nothing more; Ximen is "hungry." At a mulberry-wood
  tavern black poisoned needles strike Sun Xiuqing (Ximen carries her off) and
  Shi Xiuxue, who dies in Hua Manlou's arms. Shangguan Feiyan, in Huo Xiu's
  power, comes to warn/kill Hua and flees; his "swallow" is gone again.
- **Chapter 10 (ch11):** At the lotus pond Huo Tianqing gives Lu the
  phoenix-pun threat-verse letter (Shangguan Danfeng never came; she has been
  carried off) and Huo Xiu's Daughter's Red. Lu and Hua reason the wine came
  from Huo Xiu's mountain tower, perhaps the First Blue-Robe Tower, and climb to
  it. Past the maze (Push/Turn/Stop/Drink/Smash) they find a vault of arms and
  treasure and four mad old men each claiming to be the Great King of the Golden
  Roc — and, beyond them, Huo Xiu warming wine on the floor.

## What is NEXT

- **B07 = ch12 (第十一章 第六根足趾 "The Sixth Toe")** — the ~31k climax, its own
  batch. 5 scenes (dividers 3/161/203/363; scene 5 is very long, ~877 lines).
  Huo Xiu / the Maze Tower's secret, the four false Kings, and the "sixth toe"
  that resolves who the true Great King and the true traitors are; the fate of
  Shangguan Danfeng and Shangguan Feiyan.
- Then: **B08 = ch13 (第十二章 尾声, the short coda) + back matter, whole-book
  reconciliation (check_reconcile.py), authority.json feedback, term_ledger,
  deep_audit, COMPLETION.md, final EPUB force-committed.**

## Traps / environment

- Stray-branch trap: each session starts on a stray per-task branch;
  consolidate onto claude/lu-xiaofeng-1 (rule 2) and delete the stray.
- ch2 onward: bare-numeric dividers (01, 02, ...) render as `***` scene breaks,
  NOT TOC sections; hand-inserted after split_bilingual (build_b06.py takes the
  after-paragraph indices = cumulative paragraph counts).
- make_bilingual skip=2 every unit (line 1 running-title stub, line 2 chapter
  title). Confirm per unit.
- Extractor splits: a line whose last char is not terminal punctuation continues
  the next — EXCEPT a colon-terminated lead-in to a quoted letter/verse. ch11's
  verse-letter (source lines 43-44) was merged into one paragraph; a survey of
  ch12 found NO extractor splits (re-verify).
- **Number check**: 两 is both "two" and the tael measure word — noised after
  十/百/千/万/多. Colour/direction/set idioms + fraction idioms hide stray
  numerals — noise them (documented, longest-first) or render so the English
  carries the value. NEVER noise a real quantity. Spelled numbers tens-ones
  ("forty-nine"); "ten thousand" needs a space; 一百零八 → "one hundred and
  eight" (leading "one" required).
- **Register metric counts ONLY n't/'ll/'re/'ve/'m.** A confrontation chapter
  heavy with Ximen Chuixue / the royal "We/Our" / quoted classical text reads
  low; fix by contracting the ORDINARY speakers, not the exempt registers.
- verify_unit.py self-locates data/noise.txt — do NOT pass it `--noise`.
- data/src and data/src_epub are gitignored (regenerate with ingest_epub.py);
  source.epub and data/figs (the cover) ARE tracked. The deliverable EPUB is
  gitignored and attached in chat each batch; force-commit it (`git add -f`)
  only on the FINAL batch.
- epubcheck at /tmp/epubcheck-5.1.0/epubcheck.jar.
- English chapter titles in book.json are provisional; verify against the text
  as each chapter is done (ch09 "The Four Beauties of Emei" / ch10 "The Flying
  Swallow Comes and Goes" / ch11 "The Maze Tower" confirmed).
```
