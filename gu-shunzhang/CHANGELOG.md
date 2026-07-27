# CHANGELOG

Dated entries summarising what each corrections batch cascaded where, and any
project-structural changes.

## 2026-07-27 — Project set up

- Created the `gu-shunzhang` project (branch `claude/gu-shunzhang`) for Gu
  Shunzhang's 特務工作之理論與實際 (1933), styled on the Wang Yaqiao / Juntong /
  Shanghai-underworld projects but with a batch workflow and an eight-check QC
  contract.
- Committed `source.pdf` (National Central Library scan, 298 pp) to the branch.
- Generated `book.json` (8 chapters, 37 sections) from the PDF's embedded
  bookmarks; enriched it with English titles from the translated TOC
  (`reference/toc_translated.md`) and flagged two structural discrepancies.
- Seeded `glossary.json`; wrote CLAUDE.md, README, PROGRESS, HANDOFF,
  CORRECTIONS. No book text translated yet.
