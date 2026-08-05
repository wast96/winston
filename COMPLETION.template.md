# COMPLETION.md — whole-book completion report (template)

Written on the final batch INSTEAD of another handoff. Copy to
`COMPLETION.md` and fill every section; this is the document the commissioner
reads to know what they now have and how far to trust it.

## Status at a glance

<N/N units translated; total notes; figures; glossary rows by category
(people / orgs / places / terms); qa_epub PASS with file counts; epubcheck
result; the deliverable filename and the commit that contains it.>

## What the finished edition contains

<front matter, chapters, set-off conventions used, back matter, cover,
translator's note. State explicitly what was deliberately NOT invented to
fill an optional slot (e.g. back_matter left inert because the book has no
errata).>

## Per-chapter tally

| Unit | Title | Folios | Paragraphs | Notes | Figures |

## Batching as executed

<one line per batch, with dates and any deviation from the approved plan.>

## Checks run book-wide, and what they found

<the numbered QC contract from CLAUDE.md, each with its final whole-book
result. Include the whole-book reconciliation sweep results: rendering
counts, epithet drift found/fixed, first-appearance moves.>

## Observed error rate

<the random-sample deep audit: population, sample size and %, fixed seed,
flags and their adjudication, the honest confidence statement ("zero errors
in N proves a rate below about X%, not zero"). Link out/deep_audit.md.>

## Findings that need the commissioner's eye

<anything a machine check cannot settle: disputed readings, register calls,
places where sources contradict the book.>

## Residual uncertainties a reader should know about

<every provisional glossary reading, every damaged-scan gap, every standing
editorial omission — each already flagged in the notes; list them here
consolidated.>

## Reliability map (historical books)

<if the book makes checkable historical claims: the per-claim verdict table
(DOCUMENTED / DISPUTED / REFUTED), the shape of the unreliability, and what
is reliably accurate vs reliably invented. Link out/reliability_map.md if
written separately.>

## Provenance and method

<source edition, scan quality, OCR engines used, the pipeline as actually
run, builder features that must not be reverted, environment notes for any
future rebuild (exact build + qa commands with the real deliverable name).>

## Definition of done — met

<walk the CLAUDE.md definition-of-done list and check each item, including:
final EPUB committed (`git add -f`), authority.json fed back, term ledger
rendered, CHANGELOG current, HANDOFF rewritten to COMPLETE.>
