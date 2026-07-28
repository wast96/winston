#!/usr/bin/env python3
"""Stop-hook guard: refuse to end a BATCH WRAP-UP reply that forgot to paste the
next-batch kickoff message.

CLAUDE.md rule 1 requires that every batch wrap-up chat reply both (a) attaches the
built EPUB and (b) pastes the next-batch kickoff message VERBATIM inside a fenced
code block. Pointing at HANDOFF.md does not count. This hook enforces (b): when the
assistant's final message looks like a batch wrap-up but contains no fenced ``` code
block, it blocks the stop and tells the assistant to paste the kickoff block.

Design principles:
  - FAIL-OPEN. Any error (missing file, bad JSON, unknown schema) -> allow the stop.
    A guard that traps the user is worse than one that occasionally misses.
  - Only fires on a wrap-up turn (mentions the deliverable EPUB). Normal chat is
    never touched.
  - Capped: blocks at most twice per session, so it can never hard-loop.
"""
import hashlib
import json
import os
import sys
import tempfile

# Substrings that mark a message as a batch wrap-up (case-insensitive).
WRAP_SIGNALS = ("thousand-li.epub", "qa_epub")
# The kickoff message is always pasted inside a fenced code block.
FENCE = "```"
MAX_BLOCKS = 2


def read_last_assistant_text(transcript_path):
    """Return the concatenated text of the last assistant message, or '' on any
    trouble (fail-open)."""
    try:
        lines = open(transcript_path, encoding="utf-8").read().splitlines()
    except Exception:
        return ""
    for line in reversed(lines):
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except Exception:
            continue
        if obj.get("type") != "assistant" and obj.get("role") != "assistant":
            continue
        msg = obj.get("message", obj)
        content = msg.get("content", msg)
        texts = []
        if isinstance(content, str):
            texts.append(content)
        elif isinstance(content, list):
            for part in content:
                if isinstance(part, dict) and part.get("type") == "text":
                    texts.append(part.get("text", ""))
                elif isinstance(part, str):
                    texts.append(part)
        return "\n".join(texts)
    return ""


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0  # no input -> allow stop
    if data.get("stop_hook_active"):
        return 0  # already inside a stop-hook continuation; do not stack
    transcript = data.get("transcript_path")
    session = data.get("session_id", "nosession")
    if not transcript:
        return 0
    text = read_last_assistant_text(transcript)
    if not text:
        return 0
    low = text.lower()
    is_wrapup = any(sig in low for sig in WRAP_SIGNALS)
    has_fence = FENCE in text
    if not is_wrapup or has_fence:
        return 0

    # Cap the number of blocks per session so a non-complying loop can't trap.
    key = hashlib.sha1(session.encode()).hexdigest()[:16]
    counter = os.path.join(tempfile.gettempdir(), "handoff_guard_%s" % key)
    try:
        n = int(open(counter).read().strip())
    except Exception:
        n = 0
    if n >= MAX_BLOCKS:
        return 0
    try:
        open(counter, "w").write(str(n + 1))
    except Exception:
        pass

    print(json.dumps({
        "decision": "block",
        "reason": (
            "This looks like a batch wrap-up, but your reply has no fenced code "
            "block. CLAUDE.md rule 1 requires you to paste the next batch's "
            "paste-ready kickoff message VERBATIM, inside a ``` fenced block, in "
            "this same reply (it is in HANDOFF.md under 'Message to paste into the "
            "next chat'). Add it now, then finish."
        ),
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
