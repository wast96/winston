# CORRECTIONS

The commissioner files corrections here after reading the EPUB. Two kinds:

- **GLOBAL** — a rendering, a register rule, or a note policy that must apply
  everywhere ("render X as Y throughout", "stop noting every idiom", "this
  person is actually Z"). Applied via a glossary/style change plus a grep-driven
  edit across ALL built units, then rebuild + full QA. A global correction
  applied to only some units is worse than not applying it.
- **LOCAL** — a fix at one spot. Apply, rebuild, QA.

After a batch of corrections: rebuild, run qa_epub, list every file touched in
the reply, and append a dated entry to CHANGELOG.md.

## Filed

- [ ] (GLOBAL, standing directive, chat 2026-08-30) Scene breaks. Review every
  chapter for SCENE CHANGES that lack a divider and add them to scenes.json,
  built into rounds R2-R4 (each round covers its own chapters). Principle,
  calibrated with the commissioner on the ch02 raid: add a break at a genuine
  new scene (a real jump in place, time AND vantage); do NOT break a camera-flip
  inside a continuous cross-cut, or a causally/aurally sutured cut (an order and
  its immediate consequence); a perspective change alone is not enough. The ch02
  "Just take them" -> "Two muffled reports" cut was judged a hard cut to LEAVE,
  not break. Full mechanics in the R2 kickoff at the top of HANDOFF.md.

## Template

- [ ] (GLOBAL/LOCAL) <where> — <what is wrong> — <the fix>
