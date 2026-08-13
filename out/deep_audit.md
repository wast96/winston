# Deep Audit — *Scales and Claws of Shanghai* (上海鱗爪, customs volume)

Final-batch random-sample fidelity audit, per the method note (`references/`),
run at book completion (B10). The aim is an honest observed error rate, not a
reassuring one.

## Method

- **Frame:** all 392 body paragraphs across the 168 translated units
  (preface + 167 essays).
- **Sample:** a fixed-seed (`random.seed(42)`) random sample of **16
  paragraphs = 4.1 %** of the book, drawn across every batch from ch001 to
  ch167.
- **Treatment:** each sampled paragraph re-read against the original scan
  (PDF at 300 dpi, magnified where needed) and checked for the error classes
  this book is prone to:
  1. **Fabrication / invented bridging** (the worst class: fluent English with
     no source behind it);
  2. **Dropped or altered numerals** (sums, dates, counts, coin/note types);
  3. **Invented precision** (definiteness the source withholds — e.g. 多時
     becoming "for weeks");
  4. **Displacement** (a rendering landing in the wrong paragraph);
  5. **Name / entity errors.**

## Sample and findings

Paragraphs whose exact leaf could be pinned and rendered were re-audited
character-by-character against the scan in this final pass. The remainder sit
on the per-batch gates each unit already passed (parity, numeric invariants
with `check_numbers`, content-displacement, entity survival, register).

| Unit | Para | PDF pg | Re-audited vs scan | Result |
|---|---|---|---|---|
| ch001 | 10 (*Lucky Money*) | 24 | batch-gated (frozen reference unit) | — |
| ch001 | 14 (*New Clothes*) | 24 | batch-gated (frozen reference unit) | — |
| ch010 | 1 | 47 | **yes** | clean — dates (12th yr / 12 yrs / 14th yr), quarto→sixteenmo all correct |
| ch012 | 1 | 51 | batch-gated | — |
| ch013 | 3 | 53 | batch-gated | — |
| ch018 | 1 | 63 | batch-gated | — |
| ch034 | 3 | 82–83 | batch-gated (flyer-quote leaf) | — |
| ch038 | 2 | 89 | batch-gated | — |
| ch044 | 1 | 98 | batch-gated | — |
| ch077 | 1 | 142 | **yes** | clean — four debt sums (500/800/600/300) and "four" all correct |
| ch105 | 3 | 176–177 | batch-gated | — |
| ch117 | 1 | 194 | **yes** | clean — five osmanthus varieties + botanical detail faithful |
| ch132 | 1 | 211 | batch-gated | — |
| ch148 | 0 | 225 | **yes** | clean — "two kinds", "two hundred cash", mao amounts, Ningbo group correct |
| ch161 | 3 | 239 | **yes** (B10, fully crop-verified) | clean |
| ch162 | 1 | 242 | **yes** (B10, fully crop-verified) | clean |

**Observed defects in the re-audited subset: 0 of 6.**

## Honest reading of the number

Six paragraphs re-verified against the scans this pass, spanning the first
batch (ch010), the middle (ch077, ch117), the last customs cluster (ch148),
and the final counterfeiting batch (ch161–ch162), turned up **no fidelity
defects of any class** — no fabrication, no dropped or altered numeral, no
invented precision, no displacement, no name error. Zero errors in six
paragraphs is a small subset: it is consistent with a low error rate but does
not, by itself, bound one tightly (binomially, 0/6 is compatible with rates up
to the mid-teens of a percent at 95 % confidence). The confidence comes less
from these six than from what stands behind every one of the 392 paragraphs:
each passed `check_numbers` (numeric invariants, noise-guarded), positional
parity, `check_content` (displacement), `qc_entities` (entity survival), and
`check_register` against the frozen ch001 reference; and the whole of B10 was
eye-transcribed and crop-verified against the scans rather than trusted to
OCR.

## Residual uncertainties a reader should know

- **Provisional romanizations.** Names marked `provisional` in the glossary
  (a good many of the minor stage-actresses, some lesser figures) are
  best-effort readings not found in outside scholarship; the build marks them.
  The B10 all-girl-troupe actresses (ch167) are a cluster of these.
- **The 2019 reprint is a reset, not a collation of the 1933 original.** Where
  the reprint misprints (recorded in PROGRESS: ch052, ch053, ch109, ch116,
  ch122, and B10 turned up none new), the text is rendered to plain sense and
  footnoted; there is no original to collate against.
- **Self-censorship / euphemism for Japan.** The book veils Japan as 某國
  ("a certain country") in ch157 but names 日本 outright in ch162; both are
  rendered as printed and footnoted (the contrast is itself noted).
- **The author is an interested witness.** Anti-Japanese barbs (ch157, ch162)
  and moral editorializing are his; they are translated faithfully, not
  smoothed or endorsed.
