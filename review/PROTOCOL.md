# review/ — the final review pass protocol

Run a structured review pass before declaring the book done (and again after
any large repair). This directory holds its artifacts. The protocol is the
one that produced ~430 verified fixes on one book and a clean six-part audit
on another; keep the shape.

## Structure

- `review/STATUS.md` — the authoritative DONE / PENDING ledger, one line per
  unit, plus the batched crop queue (scan verifications are expensive; queue
  them, then read them in one sitting).
- `review/findings/<unit>.txt` — one file per unit (or unit range), reviewer
  output kept VERBATIM, adjudication marks added inline later.

## Findings line format (dense, greppable, one line per issue)

    PARA 45 | OMISSION       | HIGH | 13th committee name dropped; crop + insert
    PARA 39 | VERIFY-SCAN    | HIGH | 半伟龙 = 周伟龙 Zhou Weilong; crop
    PARA  9 | MISTRANSLATION | HIGH | 四一 = April the First works, not Forty-One
    PARA  8 | GLOSSARY       | MED  | "great agent" x13 vs "senior agent" x44; cascade
    PARA 71 | REGISTER       | MED  | 美帝 softened; restore
    PARA 17 | PROSE          | LOW  | smoother phrasing

Categories: MISTRANSLATION / VERIFY-SCAN / OMISSION / GLOSSARY / REGISTER /
PROSE / CONTEXT. Severity HIGH / MED / LOW. CONTEXT marks sentence-level
rewrites a mechanical pass must skip. Every findings file ends with a one-line
`SUMMARY:` verdict.

## Adjudication

Mark each finding inline: `[ACCEPT]`, `[REJECT <reason>]`,
`[SCAN-CONFIRMED <reading>]`. Applied items stay listed (harmless);
STATUS.md is the ledger. RECORD REJECTED FINDINGS TOO — a rejected finding
with its reason is evidence the review looked, and stops the next session
re-raising it.

## Method per unit

1. Read the unit's bilingual pairing paragraph by paragraph against source.
2. Queue every previously "OCR-trusted" reading for crop verification; do not
   interleave image reads with prose review.
3. GLOSSARY findings cascade book-wide (including note and glossary bodies),
   never per-unit.
4. Pay disproportionate attention to each unit's TAIL (the fabrication class)
   and to run-in headings merged into first paragraphs.
5. After applying: re-run verify_unit, rebuild, qa_epub; re-verify any repair
   of fabricated text as if it were new translation.
