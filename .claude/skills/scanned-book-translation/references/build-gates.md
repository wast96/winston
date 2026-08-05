# Build gates: silent loss

Every failure documented here shipped in a finished book, passed every check,
and was found weeks later.

## The core principle

**Agreement between two derived artifacts is not integrity.**

An EPUB build checked that footnote *references* matched footnote *bodies*.
They agreed perfectly. Twelve of each were missing, because both derive from
the same step — and when that step drops a note, it drops the reference and the
body together, leaving a consistent, complete-looking, wrong book.

Check derived output against the **source of truth** — the notes file, the
chapter list, the source paragraph count — never against another derivative.

## Failure 1 — twelve footnotes silently dropped

**Symptom:** 289 notes written, 277 in the book. No error, no warning, QA green.

**Cause:** notes attach by matching an anchor phrase verbatim in the prose. Over
time prose gets edited and anchors drift out of sync. Mostly capitalisation — an
anchor beginning "a gentleman's word" against a sentence beginning "A
gentleman's word." The builder's matcher found nothing and moved on.

One note was anchored to a phrase that existed only in a section heading, and
headings were not processed for notes at all.

**Gate:**

```python
orphans = [(cid, n["anchor"]) for cid, lst in notes_by_chapter.items()
           for n in lst if not n.get("used")]
if orphans:
    sys.stderr.write("BUILD FAILED: %d note(s) never matched\n" % len(orphans))
    for cid, a in orphans:
        sys.stderr.write("  %-9s %s\n" % (cid, a[:88]))
    sys.exit(2)
```

Added at the end of a project, this gate immediately caught two more orphans
that the twelve-note repair had missed.

**Also:** verify anchors at *write* time, not build time. When you write a note,
assert the anchor appears exactly once in the prose.

**Also:** allow notes on section headings. Several notes are legitimately
*about* the heading — flagging how the book's own table of contents words it.

## Failure 2 — a chapter with no title

**Symptom:** one chapter in the finished EPUB began mid-air, with no title.

**Cause:** its markdown used `# Chapter Six: …` where every other chapter used
`# Book Title` followed by `## Chapter N: …`. The builder skips `#` lines on the
reasoning that the book title belongs on the title page. So the chapter heading,
its subtitle, and its dateline were all discarded.

**Gate:** compare the heading-level shape of the first few headings in every
chapter file. They must all be identical.

```python
shapes = {}
for cid, path in docs.items():
    heads = [l for l in open(path) if l.strip().startswith('#')][:3]
    shape = tuple(len(h) - len(h.lstrip('#')) for h in heads)
    shapes.setdefault(shape, []).append(cid)
assert len(shapes) == 1, shapes
```

## Failure 3 — note numbering running backwards

**Symptom:** QA reported note numbering not sequential in reading order.

**Cause:** candidate notes were sorted by where the anchor *starts*. But the
reference marker renders at the anchor's *end*. When one anchor contains
another — a short name inside a longer phrase — the containing anchor starts
first but ends last, so its marker rendered after the shorter one's and the
numbers ran backwards.

**Fix:** sort by `position + len(anchor)`. Numbers then follow the reader's eye.

**Gate:** assert note reference numbers appear in ascending order across the
whole spine, not just within a document.

## Failure 4 — figure manifest overwritten

**Symptom:** earlier chapters' figures vanished from the manifest.

**Cause:** the figure-detection script rewrote its manifest file on each run.
Running it per chapter destroyed every previous chapter's entries.

**Fix:** merge by page range. Or run it once over the whole book.

## Failure 5 — stale derived files

**Symptom:** the numeric invariant check passed against text that no longer
shipped.

**Cause:** the bilingual QC file was generated once from the prose. Later prose
edits made it stale, so the check validated an old version.

**Fix:** regenerate paired QC files from the current prose before every check
run. Editing prose invalidates every prior check — re-run all of them.

## The gate suite

Minimum for a book-length project. All cheap, all deterministic:

| Gate | Asserts |
|---|---|
| unmatched anchors | every note placed, build fails otherwise |
| heading shape | every chapter file structured identically |
| paragraph parity | source count == translation count, per chapter |
| note ordering | reference numbers ascend across the spine |
| link resolution | every href resolves to an existing id |
| glossary drift | no referent rendered two ways anywhere |
| numeric invariants | every source quantity survives |
| register vs reference | dialogue voice within tolerance |
| archive structure | mimetype first and stored (EPUB) |

Wire these before translating. A gate written on day one prevents defects; the
same gate written at the end merely tells you how many you must now repair.
