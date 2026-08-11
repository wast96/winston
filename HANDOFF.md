# HANDOFF — Nameless Heroes (英雄无名), Chen Gongshu

This file is the baton. A fresh session with no memory reads it and starts
immediately. **It is the ARCHIVE of the message below, not its delivery:
every batch ends with this file's paste-block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count.** Rewrite
it at the end of every batch; always keep the paste-ready block below as its
first section. When the book completes, replace it with the completion notice
and do not touch it afterward.

## Message to paste into the next chat

Batch 1 stops at the first-chapter VOICE GATE (CLAUDE.md Step 0c). No Batch 2
kickoff is issued yet: the commissioner judges the front matter first, and on
approval it becomes the FROZEN register reference. Paste this block in the
chat now, with the built EPUB attached:

```
Nameless Heroes B01 voice gate (STOP for approval)

Batch B01 (ch01-ch05, the front matter) is complete and built into
out/nameless-heroes.epub (attached). All gates are green: parity, numbers,
anchors (verify_unit), check_align, check_content, check_structure, qa_epub,
and epubcheck 5.1.0 (0 errors / 0 warnings). 67 footnotes, a Principal
Characters page, and the glossary are in place. 军统 was DECIDED as "the
Juntong."

Please judge, before Batch 2:
  1. VOICE — the essayistic first-person register of Chen's authorial "I"
     (read ch01 the Foreword and ch04 "My View of Secret Service Work").
  2. FOOTNOTE DENSITY — 67 notes across the front matter (ch01 6, ch02 20,
     ch03 9, ch04 24, ch05 8); too many, too few, or right.
  3. FORMATTING — including the recovered ch04 sub-headings (five titled
     sections the digitization had flattened into paragraph text) and the
     Principal Characters / glossary pages.

On approval, ch01 (or the front matter as a whole) becomes the frozen
reference for check_register.py --ref, and Batch 2 = ch06 (Part One,
Section 1, ~25k, the first narrative unit) begins in a fresh chat.
```

## What is DONE (do not redo)

- **Step 0 (survey).** Ingest + book.json (43 chapters, 5 TOC parts) +
  skeleton EPUB. See the survey section of PROGRESS.md.
- **Batch B01 (ch01-ch05), the front matter.** Foreword, three book
  introductions, Part One prefatory note. Translated, annotated (67 notes),
  glossary (46 rows) and Principal Characters page authored, cumulative EPUB
  rebuilt. All checks green; epubcheck clean. Continuous note count so far:
  67. Full detail in PROGRESS.md ("Batch B01"). AWAITING the voice gate.

## Tooling in place (do NOT revert)

- `scripts/clean_batch.py` (new): derives data/zh/<id>.txt verbatim from
  data/src, applying per-unit drops/merges/heading-splits with a source-
  conservation check. Used instead of make_bilingual->split_bilingual when a
  batch's logical paragraphs differ from the source <p> boundaries.
- `scripts/batch_artifacts.py` (new): derives out/<id>_en.json from the
  reading files and writes checks.json (docs/sources for the structure and
  content checks).
- `scripts/check_content.py` (patched): name_map skips "_"-prefixed glossary
  categories/entries; it crashed on the sectioned glossary's _about string.
- Glossary authored SECTIONED and merged by hand (validated with
  apparatus_merge.check_text). apparatus_merge's glossary path assumes a FLAT
  {zh: row} map and would corrupt the sectioned file; notes still use it.
- data/noise.txt carries the B01 project noise rules (see PROGRESS.md).
- epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (setup.sh fetches it;
  re-run setup.sh per session). setup.sh's ONE failing regression test ("hook
  stands down on template stub") is a false alarm coupled to template state,
  not a defect; see PROGRESS.md.

## Renderings settled this batch / carry-forward

- 军统 / 军统局 -> "the Juntong" (DECIDED; glossary organizations). Full name
  and anachronism in the ch04 note. Feed back to authority.json on completion.
- Agreed shelf (reused): 戴笠 Dai Li (courtesy name Yunong); 汪精卫 Wang
  Jingwei; 北平 Beiping; 天津 Tianjin.
- Institutions: 力行社 the Lixingshe; 特务处 the Special Services Department;
  调查统计局 the Bureau of Investigation and Statistics; 第二处 the Second
  Department; 站 Station / 区 District (kept distinct); 特工总部 the Special
  Operations Headquarters ("No. 76"); 保密局 the Bureau of Confidential
  Investigation.
- Book's own terms kept as idiom: 制裁 "sanction" (targeted killing); 绥靖
  "pacification" and 戡乱 "suppression of the rebellion" (the 1946-49 war);
  "bandits" / "the bandit chief Mao" (毛酋) for the Communists; "traitors" for
  collaborators. All preserved, flagged in notes where scholarship contests
  the claim (e.g. the Chahar army attribution, the Ji Hongchang note).
- Part/book titles (provisional, may refine): 北国锄奸 "Rooting Out Traitors
  in the North"; 河内辱命 "Disgrace at Hanoi" (published as 河内汪案始末, "The
  Full Story of the Wang Case at Hanoi"; see the ch03 note and, later, the
  ch10 preface); 百战声威 "Renown Won in a Hundred Battles"; 平津地区绥靖戡乱
  "Pacification of the Beiping-Tianjin Region".
- Japanese names are RECONSTRUCTED readings (provisional): 山本荣治 Yamamoto
  Eiji; 大冢清 Ōtsuka Kiyoshi; 中岛信一 Nakajima Shin'ichi; 冈村 Okamura.
  Verify against Japanese sources when they recur in the narrative.

## Voice sheet — CHEN GONGSHU (author / narrator)

- REGISTER: educated, formal, essayistic first person; grave and a touch
  archaic but not stilted. Long sentences with semicolon-joined clauses;
  four-character idiom and classical allusion used freely (养虎遗患,
  李代桃僵, 富贵不淫, 一了百了) and footnoted when they carry weight.
- STANCE: self-justifying yet self-effacing; disavows self-promotion ("I am
  no more than the thread that stitches the pages together"), insists on
  truthfulness, admits his own blunders. Tender toward the dead comrades,
  bitter toward the enemy. Rhetorical questions and exclamations for emphasis.
- IDIOM: unbroken Nationalist idiom of 1980s Taiwan (see settled renderings).
  Preserve it; do not soften. Footnote where a claim is contested.
- FORMALITY: courteous 先生 "Mr." for superiors and elders (Mr. Dai Li);
  warm 兄 "Brother" for close colleagues (Brother Xiuyuan).
- English target ratio ~4.6-5.3 en/han (this batch's medians). Merge clauses
  where English wants them merged; keep the semicolon rhythm where it reads.

## Where the book stands

- Front matter translated. Chen states his purpose (record the nameless dead
  of the secret service before the last witnesses die), his method (truthful,
  first-person, nothing invented), and summarizes the five assassination
  cases of Book One, the Hanoi attempt on Wang Jingwei (Book Two), and the
  Shanghai operations (Book Three). No narrative yet.

## What is NEXT

- STOP at the voice gate. Do NOT begin Batch 2 in this conversation, and do
  NOT paste a Batch 2 kickoff.
- After approval: freeze the register reference, then Batch 2 = ch06 (Part
  One, Section 1, 任重道远 勇往直前, ~25,236 chars) begins in a fresh chat.
  ch06 is the first narrative unit; reconsider whether the frozen reference
  should be revisited once narrative prose exists.

## Open items for the read-through

- Confirm at the voice gate: the recovered ch04 sub-headings (five titled
  sections), footnote density, and the "the Juntong" rendering.
- 军统 consistency across the whole book; feed the decision back to
  authority.json on completion.
- Japanese name readings (above) to verify when the men recur.
- Stray source glyphs still to resolve in later batches: trailing 杀 on the
  ch22 title; 寿张为幻 in the ch16 title; 毛酋 in a ch36 section title.
- Whether "Disgrace at Hanoi" survives as the part title after the ch10
  preface is translated (Chen rejected 河内刺汪; the book was titled
  河内汪案始末).

## Environment / traps state

- epubcheck available (5.1.0), clean on the B01 build. Source is a clean
  digital EPUB, predominantly simplified with residual variant glyphs and
  scattered digitization glitches (list them, render to plain sense, do not
  footnote mechanical typos). B01's glitch list is in PROGRESS.md.
- Running-header line 英雄无名-陈恭澍 opens all 43 content files: drop it
  (clean_batch.py handles the B01 units; the count is baked into its per-unit
  "drop" spec).
- Faithful numbering gaps (NOT errors): Part Three skips ch7, splits ch10 into
  (上)/(下); 三面受敌 一往无前 titles two different chapters.
- Expect a stray per-task branch at the top of every batch; consolidate onto
  claude/nameless-heroes per rule 2.
