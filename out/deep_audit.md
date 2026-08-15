# Deep audit — Owl's Castle

Random-sample fidelity audit, run on completion of the final novel chapter.

## ch19 (伏見城 / Fushimi Castle), the climax chapter

- Population: 310 body paragraphs.
- Sample: 14 paragraphs (4.5%), fixed seed 19.
- Indices audited: 22, 55, 61, 75, 102, 133, 148, 177, 201, 261, 266, 270, 299, 304.
- Method: each sampled paragraph read on the Japanese side against the English
  side, checking for dropped clauses, altered numbers or names, and the
  "invented precision" class (definiteness the source withholds).

Result: zero fidelity errors in the sample. Numbers, units (two shaku, the
Hour of the Rat, thirteen ri), names, and register all survive; no invented
precision was found. Spot cases: 血なます rendered "blood minced on our
spear-points" (the namasu image kept); 十重二十重 rendered "tenfold and
twentyfold"; the closing gnomic present (小萩が答える, "answers Kohagi") kept as
present per the tense rule.

Honest confidence statement: zero errors in 14 paragraphs proves an error rate
below roughly 20% at 95% confidence, not zero. The true rate is far lower: every
proper name, number and unit in ch19 was crop-verified against the scan before
translation, the compound-coverage grep over the raw OCR found no dropped
meaningful compound, and the final two paragraphs were re-read against folio 652
before shipping.

## Book-wide mechanical checks (all 19 units)

These are the cheap, exhaustive checks; all green on the whole spine:

- Numeric invariants: 0 unresolved across every unit.
- Paragraph parity: every unit source-lines == translation-paragraphs.
- Entity survival (qc_entities) and displacement (check_content): 0 misses,
  every name in its paired paragraph.
- Spelling locale: 0 British / 130 American after the completion cascade.
- qa_epub: PASS (34 files, 27 documents, all links resolve).
- epubcheck 5.1.0: 0 fatals / 0 errors / 0 warnings.

## Caveat

The per-chapter audits for ch01 through ch18 were performed in their own
batches; this report's fresh random sample covers ch19 only. The whole-book
mechanical checks above cover all 19 units and are green.
