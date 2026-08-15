# The blind-critique prompt (voice gate)

This is the prompt handed to a CONTEXT-BLIND reader at the voice gate: a fresh
instance given ONLY the built chapter, with no source text, no `STYLE.md`, no
`CLAUDE.md`, no glossary, no knowledge of this project. The blindness is the
whole point. A reader who has seen the style guide grades against the guide; a
reader who has seen the source forgives the English because they know what it
means. We want neither. We want a native English reader who knows only that this
is a translation and can say where the prose does not read right.

`scripts/voice_gate_critique.py prepare <unit>` assembles the chapter text and
writes this prompt above it into `out/<unit>_critique_prompt.md`, ready to hand
to the blind subagent. Do not add project context to that agent.

---

Read this. It is a chapter of an English translation. I want you to tell me, in
detail, every single thing in here that is wrong from the perspective of a
native English speaker.

Focus on this being a translation: it is mostly about how the prose reads. I do
not want things fully invented, but they need to be fixed, because right now
this is not exactly right. Look for translationese and stiltedness: stilted
inversions, calqued idioms, transferred syntax, sentences that stack too many
clauses, dash- or comma-glosses jammed mid-sentence, doubled synonyms, wooden
dialogue, pronoun fog, wrong or fake-antique register, and anything a good
editor would blue-pencil in original English.

Be succinct but precise. No huge paragraphs. No repetition. No notes that manage
feelings about how good it is. Just good, insightful, solid corrections: quote
the phrase or sentence, say what is wrong in a few words, and give the fix.
