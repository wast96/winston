# HANDOFF — The Stealthy Ones (忍びの者〈五右衛門釜煎り〉)

## Message to paste into the next chat

```
The Stealthy Ones B01

Read CLAUDE.md, then HANDOFF.md, then book.json.

Do Batch 1 = Chapter 1 「新しい波」 / "New Waves" (PDF pages 7–70, printed
folios 5–68), end to end per the CLAUDE.md pipeline. This is a Japanese book:
vertical, right-to-left, heavy furigana. Use OCR lang=jpn_vert, psm 5, crop
left 0.06 / right 0.96 / top 0.09 / bottom 0.935 (validated in Batch 0; drops
the top-corner folio, keeps all body text). Run ocr_dual.py for the second
read; crop-verify every proper name, number, and low-confidence span by eye —
furigana sit beside the kanji and can bleed into the main column.

Cite the book's PRINTED FOLIO in every note, never the PDF page. Never invent
bridging text: if OCR cuts off, crop the scan and read the real continuation.
Build the per-character VOICE SHEETS in HANDOFF as characters first appear.
Do not pause for approval mid-batch.

Batch 1 is the FIRST-CHAPTER VOICE GATE (CLAUDE.md Step 0c): when it is done,
STOP and present the built chapter for the commissioner to judge voice, note
density, and formatting. Do NOT start Batch 2. On approval, out/ch01_reading.md
becomes the FROZEN register reference for the rest of the book.

End your reply with the built EPUB attached in chat AND this Batch-2 kickoff
pasted verbatim in a fenced code block (update it for ch02 first).
```

## Status — what is DONE
- Batch 0 (survey): book.json metadata + full 8-chapter structure; offset +2
  verified everywhere; OCR geometry measured; skeleton EPUB built; qa_epub
  PASS; epubcheck clean. Awaiting approval of the batch plan.

## Batch plan (proposed; pending commissioner approval)
- Baseline = one chapter per batch (survey B01–B08). Chapter 5 is 102 pp. and
  should be split at a scene break; other 64–70 pp. chapters may be split too
  if a full chapter overruns one conversation.
- Final batch: afterword 解説 decision, back matter, cover, whole-book
  reconciliation (check 12), COMPLETION.md.

## Tooling in place — do NOT revert
- setup.sh pack list is Japanese (`tesseract-ocr-jpn`, `-jpn-vert`), not
  Chinese. Keep it.
- book.json: source_language "ja", source_script "ja"; source-title/author
  live in the *_zh fields (tagged ja by the builder). pdf_end/printed_end =
  530/528 so ch8 length excludes the afterword.

## Carry-forward
- Chapter English titles are PROVISIONAL (see book.json / PROGRESS); confirm
  at the voice gate.
- Principal cast to watch as they appear (flag `principal:true` in glossary,
  build voice sheets): Ishikawa Goemon (石川五右衛門, hero); his wife Maki
  (マキ); Toyotomi Hideyoshi (秀吉); Oda Nobunaga (信長, dies early); Hattori
  Hanzō (服部半蔵). Verify all readings against the scan before fixing them.
- Historical frame: opens 天正十年 (1582), the year of Nobunaga's fall;
  proceeds through Hideyoshi's rise, the Saiga/Negoro campaigns, to Goemon's
  execution 文禄三年 (1594). Murayama reads it through a political-left lens
  (peasant/ninja world; note the "socialist"/"revolutionary" asides) — footnote
  the author-as-interested-witness moments.

## Environment state
- PaddleOCR unavailable; use ocr_dual.py. epubcheck at /tmp/epubcheck-5.1.0.
- Working branch: `claude/the-stealthy-ones` (single branch for the whole
  book; stray per-task branches get consolidated onto it — see CLAUDE.md
  rule 2).
