# The blind-critique prompt (voice gate) — ANNOTATED EDITION variant

This is the prompt handed to a CONTEXT-BLIND reader at the voice gate of an
ANNOTATED edition (a historical English source reproduced verbatim, with an
added apparatus). The blindness is the whole point: no source, no `STYLE.md`,
no `CLAUDE.md`, no glossary, no knowledge of the project. For an annotated
edition there is no translation register to grade — the body is a fixed
historical text — so the reader judges the EDITORIAL APPARATUS: the voice of
the added notes, their density/coverage, their clarity, and the formatting.

`scripts/voice_gate_critique.py prepare <unit>` selects this prompt
automatically when `book.json` says `"edition_kind": "annotated"`, and labels
each note (author) or (editorial). Do not add project context to the agent.

ADJUDICATING THE RETURN (for the session, never for the blind reader): the
blindness that makes the critic honest also produces known false positives.
Before accepting a finding, check it against the book's KEEP list in
`STYLE.local.md`. Recurring annotation-edition classes: the body's 1930s
British spelling and the author's partisan phrasing are the fixed source, not
defects; a note that flags the author's own bias is content, not editorializing;
an "uncorroborated" or "contradicted" verdict is deliberate, not hedging.

---

Read this. It is one chapter of an annotated reading edition of a work of
history first published in 1938.

IMPORTANT: the body text is the original author's own prose, reproduced
VERBATIM. Do NOT critique its wording, style, sentence length, or its 1930s
British spelling — it is a fixed historical document and cannot be changed.
Ignore the body except as context for the notes.

What you ARE judging is the EDITORIAL APPARATUS added for this edition: the
footnotes listed at the end. Each is labelled (author) — the original author's
own reference note — or (editorial) — a note added for this edition. Judge ONLY
the (editorial) notes, plus coverage and formatting. Tell me, precisely:

1. VOICE OF THE NOTES. Do the (editorial) notes read as clean, concise,
   consistent modern English? Flag any that are wordy, that editorialize or
   manage feelings, that hedge limply, that shift register, that merely restate
   the body, or that give a bare identification ("X was a person") without
   saying why it matters here.

2. DENSITY / COVERAGE. You are a general reader with no background in modern
   Chinese history. Name anything in the text — a person, place, institution,
   office, party, event, or foreign/period term — that you could not place and
   that has NO note. Equally, flag any (editorial) note that tells you something
   you plainly did not need (padding).

3. CLARITY. Any (editorial) note that is confusing, ambiguous, circular, or
   that seems to contradict itself or the text. (You cannot check facts; flag
   only what reads wrong.)

4. FORMATTING. Anything about how the notes and their markers read that is off.

Be succinct and precise: quote the note or phrase, say what is wrong in a few
words, give the fix. No long paragraphs, no repetition, no praise.
