# CORRECTIONS

Winston's review surface. Read a batch's EPUB (or `out/<id>_reading.md`), write
corrections here, then say "Apply CORRECTIONS.md."

Two kinds:
- **GLOBAL** — a rendering, register rule, or note policy that must cascade to
  EVERY built unit (via glossary/style change + grep-driven edit + rebuild +
  full QA). A global correction applied to only some units is worse than not
  applying it.
- **LOCAL** — a fix at one spot.

## Template

```
### [GLOBAL|LOCAL] short title
Unit: chNNsNN (or "all")
Where: anchor phrase or quote
Problem: what is wrong
Fix: what it should be
```

## Pending

(none yet)
