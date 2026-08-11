# HANDOFF — The Rebel (叛逆者) / Bi Yu

This file is the baton. A fresh session with no memory reads it and starts
immediately. **It is the ARCHIVE of the kickoff message, not its delivery:
every batch ends with this file's kickoff block PASTED VERBATIM INTO THE
CHAT, alongside the attached EPUB. Writing it here alone does not count.**
Rewrite it at the end of every batch; always keep the paste-ready kickoff
message below as its first section. When the book completes, replace the
kickoff with the completion notice and do not touch it afterward (the Stop
hook keys off it).

## Message to paste into the next chat

```
The Rebel B01

Read CLAUDE.md in full (the working rules at the top are non-negotiable), then HANDOFF.md, then book.json. We are translating 《叛逆者》(The Rebel) by Bi Yu (畀愚), People's Literature Publishing House 2020, a collection of FOUR Republican-era espionage novellas, from the digital source EPUB into an annotated English EPUB, following CLAUDE.md exactly. Work ONLY on branch claude/the-rebel; expect the harness to start you on a stray per-session branch and consolidate per CLAUDE.md rule 2 (check out claude/the-rebel, reset to origin, carry over any stray commits, push, delete the stray). Deliverable is out/the_rebel.epub.

This is BATCH 1 and it STOPS at the first-chapter voice gate (Step 0c), NOT at a next-batch kickoff. Run ./setup.sh first.

Do Batch B01 = The Rebel installments 1-7 (units ch01 through ch07), end to end per the CLAUDE.md pipeline:
1. Read ch01-ch07 from data/src/ (04_part0002.txt .. 10_part0008.txt). Fix extractor-split paragraphs (a line whose last char is not in 。！？"）…— continues the next); recover any set-off formatting with apply_format_markers.py where the source HTML encodes it. Grep the batch for the source's own note markers (\[\d+\]) and record "none present" in PROGRESS.md (the survey found none book-wide).
2. Translate to the register: literary contemporary English, third-person, restrained; preserve the shifts between narration and terse dialogue. This is a serious espionage novel, not pulp. Consult glossary.json and authority.json BEFORE romanizing ANY name or term. Pinyin for names (Lin Nansheng, Gu Shenyan, Zuo Qiuming). Real historical figures and institutions appear from the first page and MUST match the shelf: Ding Mocun (丁默邨), Wang Jingwei (汪精卫), Dai Li (戴笠), the Juntong/军统 and Zhongtong/中统, No. 76 (76号, the Jessfield Road secret-service HQ), the puppet/collaborationist (汪伪) apparatus, Chongqing as the wartime capital. Check authority.json for the decided renderings of 军统/中统/戴笠/汪精卫 and the Shanghai concession streets and institutions before inventing your own.
3. Write voice sheets (two lines each, into this HANDOFF) at first appearance for at least: Lin Nansheng (林楠笙, the protagonist agent), Gu Shenyan (顾慎言, his elegant spymaster and training-class director), Zuo Qiuming (左秋明, fellow trainee, now a liaison officer), and Ding Mocun (丁默邨, the historical turncoat). Flag the main cast principal: true in glossary.json.
4. Write out/<id>_en.json (one English paragraph per source line) and run make_bilingual.py per unit; then verify_unit.py per unit AS YOU GO; check_align.py + check_content.py; verify each unit's TAIL against the source (rule 4 corollary). No register --ref yet (this batch defines it).
5. Footnotes per the reader model in CLAUDE.md: a Westerner with no background in modern Chinese history, so this batch is footnote-dense (expect 8-15 on the opening chapters) across material culture, social structure, custom, and institutions/money, PLUS the historical people and events (Ding Mocun's near-assassination, the 76号 apparatus, the Wang Jingwei regime, Reuters/路透社 cover, the concentration-camp detail in Hong Kong). Fact-check every historical claim against real scholarship (Wikipedia / Baidu Baike / academic; NEVER an AI-written source); state the verdict in the note; the source's own errors of fact stay visible and footnoted. Use apparatus_merge.py, never a shell heredoc; keep the NOT-re-noted ledger in PROGRESS.md; glossary rows with attestation.
6. Rebuild the EPUB, qa_epub.py until green, epubcheck (jar at /tmp/epubcheck-5.1.0/epubcheck.jar) if available; record all check results in PROGRESS.md; commit; push claude/the-rebel.
7. STOP at the voice gate: present the built chapter(s) for a read, ATTACH the EPUB in the chat, and ask the commissioner to judge voice, footnote density, and formatting before this becomes the frozen register reference. Do NOT start Batch 2.

Cite chapters and sections, never pages. Do not pause for approval mid-batch; only stop at the voice gate.
```

## What is DONE (do not redo)

- Step 0 survey complete: source ingested, book.json authored (51 units,
  ch01-ch51, four parts), skeleton EPUB green (qa_epub PASS, epubcheck 5.1.0
  clean), branch consolidated onto claude/the-rebel. Batch plan approved
  (9 batches). No translation yet.

## Tooling in place (do not revert)

- None beyond the template. epubcheck jar at /tmp/epubcheck-5.1.0/epubcheck.jar
  (fetched by setup.sh). No source-notes stream (the source carries none).

## Renderings settled this batch / carry-forward

- Novella English titles: 叛逆者 = The Rebel, 邮差 = The Postman, 氰化钾 =
  Potassium Cyanide, 胭脂 = Rouge. Collection subtitle: "Four Novellas".
- Names/terms still to be decided against authority.json in B01 (do not
  pre-romanize without checking): 军统 Juntong, 中统 Zhongtong, 戴笠 Dai Li,
  汪精卫 Wang Jingwei, 76号 No. 76 / Jessfield Road, 汪伪 the puppet regime.

## Voice sheets (one per major character, written at first appearance)

- (none yet; B01 writes the first sheets — see kickoff step 3)

## Where the book stands

- Nothing translated yet. The Rebel opens with Lin Nansheng, a Nationalist
  intelligence agent, shot and smuggled out of Shanghai to a Japanese army
  hospital in Hong Kong, his spine wound leaving him unable to feel pain; a
  colleague, Zuo Qiuming, gives him a new false identity. The narrative then
  flashes back to his Shanghai station work and his handler Gu Shenyan.

## What is NEXT

- Batch B01 = The Rebel 1-7 (ch01-ch07). Ends at the voice gate.
- After the gate freezes the reference: B02 = The Rebel 8-14 (ch08-ch14).

## Open items for the read-through

- (none yet)

## Environment / traps state

- epubcheck available (jar path above). Source is clean simplified-Chinese
  digital text; watch for the pervasive commercial-ebook glitches CLAUDE.md
  lists (character swaps, mismatched guillemets, dittography): render to plain
  sense and LIST in PROGRESS.md, footnote only genuine reading uncertainty.
- Harness starts sessions on a stray per-session branch; consolidate onto
  claude/the-rebel per rule 2 (done once this session; expect it again).
