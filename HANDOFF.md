# HANDOFF: The Sword Roars in the West Wind — COMPLETE

**The book is COMPLETE.** All 18 units are translated and built: the Preface,
fifteen body chapters, the Works Cited, and the Afterword. The deliverable,
`out/The Sword Roars in the West Wind.epub`, is committed to this branch
(`claude/the-sword-roars`). qa_epub PASSES and epubcheck 5.1.0 reports 0 fatals
/ 0 errors / 0 warnings / 0 infos.

There is no next-batch kickoff. The whole-book completion report is
`COMPLETION.md`: read it for the status-at-a-glance, the per-chapter tally, the
checks run book-wide, the observed error rate (`out/deep_audit.md`), and the
residual uncertainties a reader should know about. The full term ledger is
`out/term_ledger.md`.

## Footnote-density pass (2026-08-22)

On the commissioner's request the footnote apparatus was greatly expanded:
425 notes to 778. See CHANGELOG for the method and per-chapter counts. In
short, the glossary was mined as the quarry: 355 glossary subjects (people,
places, organizations, terms) that appeared in the prose but carried no
footnote were surfaced as notes at their first book-wide appearance, expanded
past the bare glossary row. Two reusable scripts drive it: `note_gaps.py`
finds the gaps, `gap_packets.py` emits per-chapter work packets. This was a
notes-only pass; prose, glossary, figures and structure are unchanged, so the
frozen-reference register and all prose checks are unaffected. qa_epub and
check_apparatus stay green at 778 notes. Any further work remains a corrections
pass, as below.

## What was done in the final batch (B18)

- **Preface (ch00)**, "History Must Not Be Made a Monster": 24 paragraphs, 15
  notes, hand-transcribed off the scan (the Preface runs its own roman-numeral
  sequence). All checks green.
- **Works Cited (ch16)**: a bilingual reference page (books, periodicals,
  newspapers; 178 entries), each an English rendering with the Chinese
  original, transcribed entry by entry off the page images. Rendered as its own
  reading unit; every work cited in the notes resolves here.
- **Afterword (ch17)**, "Keep to Poverty, Endure the Silence": 18 paragraphs,
  5 notes, hand-transcribed; six new glossary rows for figures who appear only
  here (Yang Tianshi, Mao Zemin, Zhang Dingcheng, Li Maotang, Shi Zhongquan,
  Wang Zhengming).
- **Whole-book reconciliation sweep** (see COMPLETION.md for the full list):
  Soong Ching-ling to Song Qingling; Yang Du 1875 to 1874; ch09 Fourth Avenue
  to Sima Road; book-wide title italics unified (ch10-ch13 were plain), with
  four note anchors updated; Grand Theatre to Grand Theater (American), China
  Defence League kept as a proper name; and the latent figure-caption
  double-escape bug fixed book-wide (16 caption/alt fields to ASCII quotes).
- **Cover** confirmed present and embedded byte-identical.
- **authority.json** updated with this book's decided renderings (slug appended
  to 66 existing cross-book renderings; 4 new; 2 newly flagged reconcile for a
  later shelf-level pass).

## Tooling added or changed this batch (do not revert)

- `scripts/make_ledger.py`: renders glossary.json as `out/term_ledger.md`.
- `data/noise.txt`: B18 blocks for ch00 (双百, 老百姓) and ch17 (千变万化,
  一不买二不看, 两无声). All idiom/name numerals, never quantities.
- `data/content_config.json`: ch00 and ch17 added (ch16 is a bibliography, not
  parity-checked, so it is not in the config).
- No behavioral change to the builder. The known figure-caption limitation is
  resolved at the DATA layer: captions now use plain ASCII quotes (the render
  layer curls them); do not reintroduce numeric character references into
  figure captions or alt text, as the builder's HTML-escape step double-escapes
  them. All prior batches' script patches stand.

## Standing decisions a corrections pass must honor

- The polemical register ("our Party," "reactionaries," "running dogs") is the
  author's voice, preserved deliberately; the translator's note inoculates the
  reader.
- "China Defence League" keeps its historical British spelling as the
  organization's own name; this is not a spelling-locale slip.
- Cross-book naming divergences (三马路 "Sanma Road", 四马路 "Sima Road", 伍豪
  "Wuhao", 马斯南路 "Rue Massenet") are correct within this book and flagged in
  authority.json for reconciliation between books, not within this one.

## If more work comes

Further work is a **corrections pass**, per CLAUDE.md: the commissioner files
items in `CORRECTIONS.md` (or pastes them in chat for transcription); global
corrections cascade via a glossary/style change plus a grep-driven edit across
all built units, then rebuild and full QA; local corrections are a fix at one
spot. A zero-item pass is still a clean-checkout regression run. Log every
corrections batch in `CHANGELOG.md`.

Branch hygiene: the canonical branch is `claude/the-sword-roars`. B18 started
on a stray per-task branch (`claude/fervent-cannon-grzuhd`, same commit as
origin/canonical, no remote ref); consolidated onto canonical and the stray
was deleted.
