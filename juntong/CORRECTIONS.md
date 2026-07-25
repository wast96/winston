# CORRECTIONS

Write corrections here after reading `out/juntong.epub`. Two kinds:

## GLOBAL
A rendering, register rule or note policy that must cascade across the whole
book ("render X as Y everywhere", "stop noting every idiom", "this person is
actually Z"). Applied via glossary/style change plus a grep-driven edit across
ALL unit markdown, then rebuild and full QA. A global correction applied to
only some chapters is worse than not applying it.

## LOCAL
A fix at one spot. Apply, rebuild, QA.

Format, one per block:

    [GLOBAL|LOCAL] unit-id (page)
    what is wrong:
    what it should be:

---
