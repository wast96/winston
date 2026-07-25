# Inside the Juntong — translation package

Shen Zui, 军统内幕 (3rd ed., Beijing 2001). Annotated English translation.

Setup:
1. Put the book PDF in this folder named exactly: source.pdf
2. Open this folder in Claude Code and say: "Read CLAUDE.md and continue the book."

It resumes from PROGRESS.md and commits per unit, so interruptions are cheap.

When it finishes: read out/juntong.epub with PROGRESS.md beside it, write
corrections into CORRECTIONS.md, then say "Apply CORRECTIONS.md."

Contents:
- CLAUDE.md          — the playbook (pipeline, style contract, traps)
- book.json          — the 25-unit structure map and check config
- glossary.json      — every rendering decided so far, with status
- notes.json         — the annotation apparatus
- PROGRESS.md        — working state; read this first
- CORRECTIONS.md     — your review surface
- scripts/           — the pipeline
- out/               — reading markdown per unit, and the EPUB
