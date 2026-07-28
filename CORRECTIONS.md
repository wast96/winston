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

## Template

- [ ] (GLOBAL/LOCAL) <where> — <what is wrong> — <the fix>
