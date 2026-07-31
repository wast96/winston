# HANDOFF — Midnight (子夜), Mao Dun

This file is the baton. A fresh session with no memory reads it and starts
immediately. Rewrite it at the end of every batch; always keep the paste-ready
kickoff message below as its first section.

## Message to paste into the next chat

```
Read CLAUDE.md in full (the working rules at the top are non-negotiable), then
HANDOFF.md, then book.json. Work only on branch claude/midnight. Build the
deliverable as out/Midnight.epub (the builder defaults to out/book.epub, so pass
the path explicitly on every build and every qa run).

Do Batch B01 = Chapter One (unit ch01) end to end. Read the source from
data/src/04_part0002.txt; it is authoritative, quote it verbatim in the bilingual
QC file, and render it faithfully and in full into English in the book's own
novelistic register.

Chapter One carries two of the SOURCE's own endnotes, marked [1] and [2] in the
text ([1] 英语，即：光，热，力！ at "Light, Heat, Power!"; [2] Grafton，一种名贵的外国
纱). Render these as the source's own notes, kept visibly distinct from your
translator's footnotes; do not fold them into the translator apparatus and do not
drop them. The nine source endnotes are collected in data/src_epub .. part0022;
consult that file for their exact wording.

Author out/ch01_bilingual.md (source blockquote line, English paragraph beneath;
headings tagged), then split_bilingual.py to make out/ch01_reading.md and the
parity source. Run check_numbers.py and check_structure.py. Add translator
footnotes to notes.json at about chapter density (anchors must be verbatim
substrings of the English prose; XHTML note bodies use numeric character
references, never named entities). Add any new proper nouns / places / firms /
terms to glossary.json with attestation (Wu Sunfu, the Wu family, Shanghai
place-names, the bond-market vocabulary). No figures in this chapter.

Rebuild with build_reading_epub.py out/Midnight.epub (the TOC stays pending-aware:
Chapter One links its content, every other unit still links its skeleton
outline), run qa_epub.py out/Midnight.epub until green, commit, and rewrite
HANDOFF.md with the B02 kickoff. Cite chapters, never page numbers. Never invent
bridging text. Do not pause for approval mid-batch. Deliver out/Midnight.epub in
chat as an attached file.
```

## What is DONE (do not redo)

- Step 0 (ingest + survey) complete and approved. Source ingested to data/src/;
  cover pulled to data/figs/cover00277.jpeg; book.json authored (20 units: 19
  numbered chapters ch01..ch19 = source part0002..part0020, plus the afterword
  ch20 = part0021); no sub-chapter sections. OPF metadata enriched for Kindle and
  Apple Books; cover embedded. Skeleton out/Midnight.epub built, qa_epub green.
- Approved batch plan (21,000-char maximum) recorded in book.json "batches":
  B01..B17 are one chapter each (ch01..ch17), B18 = ch18 + ch19 + Afterword.
- Nothing translated yet. No out/*_reading.md exists.

## What is NEXT

- Batch B01 = Chapter One (ch01), 12,282 source chars. See the kickoff above.

## Open items for the read-through

- Nothing open yet. First glossary decisions (protagonist and family names, firm
  names, Shanghai toponyms) get fixed in B01 and carry through the whole book.

## State / traps

- Deliverable filename: out/Midnight.epub. The builder and qa default to
  out/book.epub; always pass out/Midnight.epub explicitly.
- The source carries its OWN 9 endnotes (in the spine's last file, part0022),
  keyed by bracketed markers [1]..[9] inline in the chapters. They are the
  author's, and must be rendered as the source's notes, distinct from translator
  footnotes. Chapter One has [1] and [2]. book.json's _source_note records this.
- book.json is the LOGICAL structure. The source cover, copyright leaf (版权信息,
  part0000) and the source's own table of contents (目录, part0001) are not
  translatable units and are not in "structure".
- The builder's notes page currently says the source "carries none of its own"
  notes. That line will need adjusting once source notes appear, so the reader is
  not told the book has no notes of its own when it does.
- Branch hygiene: one branch only, claude/midnight. Do not spin off new branches.
