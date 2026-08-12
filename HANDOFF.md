# HANDOFF — Nameless Heroes (英雄无名), Chen Gongshu

This file is the baton. A fresh session with no memory reads it and starts
immediately. **It is the ARCHIVE of the message below, not its delivery:
every batch ends with this file's paste-block PASTED VERBATIM INTO THE CHAT,
alongside the attached EPUB. Writing it here alone does not count.** Rewrite
it at the end of every batch; always keep the paste-ready block below as its
first section. When the book completes, replace it with the completion notice
and do not touch it afterward.

## Message to paste into the next chat

```
Nameless Heroes B02

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub. Run ./setup.sh once, then re-ingest with scripts/ingest_epub.py source.epub (data/src is gitignored/regenerable). B01 (front matter, ch01-ch05) is DONE and the voice gate is PASSED: the B01 front matter is the FROZEN register reference. Do NOT re-do it.

Do Batch B02 = ch06 ONLY (第一节 任重道远 勇往直前, ~25,236 source chars). This is the FIRST NARRATIVE unit: Part One, Section 1, where the story proper begins (the founding of the Beiping station, Chen's meeting with Dai Li, the early work). Run it end to end per the CLAUDE.md pipeline, and run to completion (no mid-batch approval gate now that the voice gate is passed):
1. Read ch06 from data/src (07_index-split-000-0005.txt). DROP the running-header first line 英雄无名-陈恭澍. Fix extractor-split paragraphs (a line whose last char is not in 。！？」）…— continues into the next; watch the source's own mid-paragraph <p> splits). GREP the source for note markers (\[\d+\]) and record "none present" in PROGRESS.md. Recover set-off formatting with scripts/apply_format_markers.py where the source HTML encodes it — narrative chapters often carry scene breaks (centered rule image -> ***) and opening vignettes ({v}); check the chapter HTML in data/src_epub for <p class="center"> / kaiti spans and apply the markers.
2. Build data/zh/ch06.txt VERBATIM from data/src: extend scripts/clean_batch.py with ch06's drop/merge/heading spec (it verifies source characters are conserved), OR use make_bilingual.py -> split_bilingual.py if ch06's paragraphs map 1:1 onto the source <p>. Write out/ch06_en.json + out/ch06_reading.md (## chapter title from book.json; one English paragraph per source body line).
3. Translate to the FROZEN register (Chen's voice sheet is in HANDOFF; read the last two pages of ch05/ch04 English for the seam). Consult glossary.json and authority.json BEFORE romanizing anything new; REUSE the settled renderings (the Juntong; Dai Li / courtesy name Yunong; Beiping; Tianjin; the Lixingshe; the Special Services Department; the Bureau of Investigation and Statistics; Station 站 vs District 区; 制裁 "sanction"; the Nationalist idiom). New characters get a two-line voice sheet in HANDOFF at first appearance. Preserve the Nationalist idiom; footnote where scholarship contests a claim. Render digitization glitches to plain sense and LIST them in PROGRESS.md.
4. Checks: verify_unit.py ch06 (parity + numbers with --noise data/noise.txt + anchors) AS YOU GO; check_align.py; regenerate checks.json with scripts/batch_artifacts.py and run check_structure.py + check_content.py --config checks.json; verify the TAIL against the source (rule 4 corollary). check_register.py --ref against the frozen B01 front matter (exempt registers per references/register-drift.md). This batch is also the place for the once-per-book blind double-translation (check 7) on a representative narrative passage, and a round-trip back-translation sample (check 8).
5. Footnotes per the reader model, first-appearance-disciplined with the greps and the NOT-re-noted ledger (do NOT re-note anything already noted in B01: Dai Li, the Juntong, Beiping/Tianjin, War of Resistance, secret service work, the Republican-calendar convention, etc. — the full list is in PROGRESS.md). Add glossary rows with attestation status; flag any new principal cast principal: true. Figures: the survey found only the cover (already placed); confirm ch06 carries no images.
6. Rebuild the EPUB, qa_epub.py until green, epubcheck if available; record all check results in PROGRESS.md; write the voice sheet(s) and update HANDOFF.md; commit and push to claude/nameless-heroes.

End with the TWO chat deliverables in the SAME final reply (CLAUDE.md banner): the rebuilt out/nameless-heroes.epub ATTACHED as a file, and the Batch B03 kickoff message pasted VERBATIM in a fenced code block. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
```

## What is DONE (do not redo)

- **Step 0 (survey).** Ingest + book.json (43 chapters, 5 TOC parts) +
  skeleton EPUB. See the survey section of PROGRESS.md.
- **Batch B01 (ch01-ch05), the front matter.** Foreword, three book
  introductions, Part One prefatory note. Translated, annotated (67 notes),
  glossary (46 rows) and Principal Characters page authored, cumulative EPUB
  rebuilt. All checks green; epubcheck clean. Continuous note count so far:
  67. Full detail in PROGRESS.md ("Batch B01"). **VOICE GATE PASSED
  (approved by the commissioner):** the B01 front matter is now the FROZEN
  register reference for check_register.py --ref from B02 on.

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

- Batch B02 = ch06 (Part One, Section 1, 任重道远 勇往直前, ~25,236 chars),
  the first narrative unit. Kickoff is the paste-block at the top of this
  file. Runs to completion (no gate); ends by pasting the B03 kickoff.
- The frozen register reference is the B01 front matter; if narrative prose
  proves to want a different baseline, raise it, but do not silently reset it.

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
