# HANDOFF — Nameless Heroes (英雄无名), Chen Gongshu

This file is the baton. A fresh session with no memory reads it and starts
immediately. **It is the ARCHIVE of the kickoff message, not its delivery:
every batch ends with this file's kickoff block PASTED VERBATIM INTO THE
CHAT, alongside the attached EPUB. Writing it here alone does not count.**
Rewrite it at the end of every batch; always keep the paste-ready kickoff
message below as its first section. When the book completes, replace the
kickoff with the completion notice and do not touch it afterward.

## Message to paste into the next chat

```
Nameless Heroes B01

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 英雄无名 (Nameless Heroes) by Chen Gongshu, a Nationalist/Juntong secret-service memoir, from a digital EPUB (source.epub) into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/nameless-heroes; expect the harness to start you on a stray per-task branch and consolidate per CLAUDE.md rule 2 (check out claude/nameless-heroes, reset to origin, carry over any stray commits, delete the stray local and remote). Deliverable: out/nameless-heroes.epub.

Do Batch B01 = ch01-ch05 (the front matter: ch01 Foreword "The Conception of Nameless Heroes"; ch02-ch04 the author's Introductions to the first three books; ch05 Part One's Prefatory Note), about 10,589 source characters. This is expository, first-person authorial prose, NOT narrative yet; it sets the memoir's essayistic voice and, on approval, becomes the frozen register reference. Run it end to end per the CLAUDE.md pipeline:
1. Read the units from data/src/ (ch01=02_index-split-000.txt, ch02=03_...-0001, ch03=04_...-0002, ch04=05_...-0003, ch05=06_...-0004). DROP the running-header first line "英雄无名-陈恭澍" from every file (it is page furniture, not text; do not pair it in the bilingual). Fix any extractor-split paragraphs; recover set-off formatting with apply_format_markers.py only where the source HTML encodes it.
2. GREP each unit's source for the source's own note markers (\[\d+\]) before translating; record "none present" in PROGRESS.md (the survey found none book-wide, but re-check per batch). There is no source_notes stream.
3. Translate to the register contract, consulting glossary.json and authority.json BEFORE romanizing anything. Agreed shelf renderings to reuse: 戴笠 Dai Li, 汪精卫 Wang Jingwei, 北平 Beiping, 天津 Tianjin. DECIDE 军统 this batch and record it: it is a live cross-book reconcile in authority.json (Military Statistics Bureau / the Juntong / Juntong); pick one, note the choice in glossary.json, and it will feed back on completion. Write a voice sheet for Chen Gongshu's authorial "I" into the HANDOFF carry-forward. Never invent bridging text; render digitization glitches to plain sense and LIST them in PROGRESS.md; the source's own factual claims stay visible and footnoted (Chen writes as an interested witness in Nationalist idiom, e.g. "bandits" for the Communist forces, "pacification" for the 1946-49 war: preserve it, footnote where scholarship contests it).
4. Write out/<id>_en.json (one English paragraph per source line) and run make_bilingual.py; then verify_unit.py per unit AS YOU GO; check_align.py + check_content.py; verify each unit's TAIL against the source (rule 4 corollary).
5. Footnotes per the reader model in CLAUDE.md (a Westerner with no background in modern Chinese history: the Juntong and Dai Li, the 力行社/特务处 lineage, 九一八 and 一二八, Whampoa, the "five-part" plan, place names). Be generous but first-appearance-disciplined with the greps and the NOT-re-noted ledger. Glossary rows with attestation status; flag main cast principal: true. Figures: only the cover exists, already placed. Provisional part title "Disgrace at Hanoi" for 河内辱命: the ch03 introduction and (later) the ch10 preface discuss Chen's own title choices, so a translator note there is warranted.
6. Rebuild the EPUB, qa_epub.py until green, epubcheck if available; record all check results in PROGRESS.md; update HANDOFF.md; commit and push to claude/nameless-heroes.

Then STOP at the first-chapter VOICE GATE (CLAUDE.md Step 0c): attach the rebuilt out/nameless-heroes.epub in this chat and ask me to judge voice, footnote density, and formatting before Batch 2. Do NOT paste a Batch 2 kickoff and do NOT begin Batch 2; on approval this front matter becomes the frozen register reference. Cite chapters and sections, never pages. Do not pause for approval mid-batch.
```

## What is DONE (do not redo)

- **Step 0 (survey), 2026-08-11.** Ingested source.epub (45 spine docs, 1
  image, 624,120 chars). Authored book.json: 43 chapters, 37 sections, 5 TOC
  parts. Ran survey (35 batches at ~18k chars, out/SURVEY.md). Built the
  skeleton EPUB: qa_epub PASS, epubcheck 5.1.0 clean. Committed + pushed to
  claude/nameless-heroes; stray harness branch removed. Continuous note
  number so far: 0.

## Tooling in place (do not revert)

- No script patches this project yet. Checker regression tests green
  (setup.sh). epubcheck 5.1.0 at /tmp/epubcheck-5.1.0/epubcheck.jar (fetched
  by setup.sh; re-run setup per session).

## Renderings settled this batch / carry-forward

- Agreed from authority.json (reuse, do not re-decide): 戴笠 Dai Li; 汪精卫
  Wang Jingwei; 北平 Beiping; 天津 Tianjin.
- OPEN, decide in B01: 军统 (live three-way reconcile on the shelf). Also
  pending first-appearance: 陈恭澍 Chen Gongshu (author), 力行社, 特务处,
  调查统计局, 戴笠's courtesy name 雨农.
- Provisional English part/book titles (may refine at the voice gate):
  北国锄奸 "Rooting Out Traitors in the North"; 河内辱命 "Disgrace at Hanoi";
  百战声威 "Renown Won in a Hundred Battles"; 平津地区绥靖戡乱 "Pacification
  of the Beiping-Tianjin Region".

## Voice sheets (one per major character, written at first appearance)

- CHEN GONGSHU (author / narrator): to be written in B01. First-person
  memoirist; educated, formal, self-justifying but plain-spoken; writes in
  the Nationalist idiom of the 1980s looking back on the 1930s-40s. Fill in
  the two-line spec (register, tics, formality) from the actual prose.

## Where the book stands

- Nothing translated yet. B01 is the front matter (foreword + three book
  introductions + Part One prefatory note), where Chen states his purpose:
  to record the "nameless heroes" of the secret service before the last
  witnesses die, as truthful record and not memoir-as-self-promotion.

## What is NEXT

- Batch B01 = ch01-ch05 (front matter), then STOP at the voice gate.
- After the gate: B02 = ch06 (Part One, Section 1, ~25k), the first
  narrative unit; consider whether the frozen register reference should be
  revisited once narrative prose exists.

## Open items for the read-through

- 军统 rendering (reconcile) once decided: verify consistency across the book
  and feed back to authority.json on completion.
- Stray source glyphs to resolve in context: trailing 杀 on the ch22 title;
  寿张为幻 in the ch16 title; 毛酋 in a ch36 section title (derogatory "Mao
  chieftain").
- Whether "Disgrace at Hanoi" survives as the part title after the ch10
  preface is translated (Chen rejected 河内刺汪; the finished book was titled
  河内汪案始末).

## Environment / traps state

- epubcheck available (5.1.0). Source is a clean digital EPUB, predominantly
  simplified with residual variant glyphs (鬪 価 値 鄕): digitization
  glitches, list them, do not footnote mechanical typos.
- Running-header line "英雄无名-陈恭澍" opens all 43 content files: drop it.
- Faithful numbering gaps (NOT errors): Part Three skips ch7, splits ch10
  into (上)/(下); 三面受敌 一往无前 titles two different chapters.
- Expect a stray per-task branch at the top of every batch; consolidate onto
  claude/nameless-heroes per rule 2.
