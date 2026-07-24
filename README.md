# Wang Yaqiao translation package

Setup:
1. Put the book PDF in this folder named exactly: source.pdf
2. Open this folder in Claude Code (desktop app, Code tab, or `claude`
   in a terminal here).
3. Say: "Read CLAUDE.md and process the whole book."

It will set up its own environment, generalize the builder, and run
prologue + chapters 2-15 end to end without stopping (chapter 1 is done,
in reference/). Expect this to take multiple long sessions; it commits
per chapter, so interruptions resume cleanly.

When it finishes: read out/wang-yaqiao.epub with PROGRESS.md beside it,
write your corrections into CORRECTIONS.md, then say: "Apply
CORRECTIONS.md." Global corrections cascade across the entire book.

Contents:
- CLAUDE.md          — the full playbook (pipeline, style contract, traps)
- glossary.json      — every rendering decided so far, with status
- notes.json         — chapter 1's 58 annotations (format reference + live data)
- CORRECTIONS.md     — your review surface
- scripts/           — the working pipeline from chapter 1
- reference/         — finished chapter 1: prose, notes, EPUB (the quality bar)
