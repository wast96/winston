#!/usr/bin/env python3
"""Stop-hook guard: refuse to end a BATCH WRAP-UP reply that forgot to paste
the next-batch kickoff message.

CLAUDE.md rule 1 requires that every batch wrap-up chat reply both (a) attaches
the built EPUB and (b) pastes the next-batch kickoff message VERBATIM inside a
fenced code block. Pointing at HANDOFF.md does not count. This hook enforces
(b). It was written after the same omission recurred on four separate books;
prose in CLAUDE.md did not fix it, a hook did.

Design principles (each learned on a real project):
  - FAIL-OPEN. Any error (missing file, bad JSON, unknown schema) -> allow the
    stop. A guard that traps the user is worse than one that occasionally
    misses.
  - SELF-CONFIGURING. The wrap-up signal is the deliverable filename read from
    book.json (key "deliverable", else "<uid>.epub", else any .epub mention)
    plus "qa_epub"; nothing to edit per project.
  - FINGERPRINT, not just any fence: if HANDOFF.md carries a kickoff block
    under "## Message to paste into the next chat", the block's first
    non-empty line must appear in the reply. A casual mention of the batch
    name is not enough; the whole block must be pasted. If HANDOFF.md has no
    such block (e.g. the book is complete), any fenced block passes.
  - Honors stop_hook_active (never stacks inside a continuation).
  - Capped at MAX_BLOCKS per session so a non-complying loop can never trap.

Last-batch caveat: when the book completes, HANDOFF.md's kickoff section is
replaced by the completion notice, and this hook stops demanding a block that
no longer exists.
"""
import hashlib
import json
import os
import re
import sys
import tempfile

FENCE = "```"
MAX_BLOCKS = 2
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def wrap_signals():
    sigs = ["qa_epub"]
    try:
        book = json.load(open(os.path.join(ROOT, "book.json"), encoding="utf-8"))
        d = book.get("deliverable")
        if d:
            sigs.append(os.path.basename(d).lower())
        else:
            sigs.append(".epub")
    except Exception:
        sigs.append(".epub")
    return sigs


def kickoff_first_line():
    """First non-empty line of the fenced kickoff block in HANDOFF.md, or ''."""
    try:
        text = open(os.path.join(ROOT, "HANDOFF.md"), encoding="utf-8").read()
    except Exception:
        return ""
    m = re.search(r"## Message to paste into the next chat.*?```[^\n]*\n(.*?)```",
                  text, re.S)
    if not m:
        return ""
    for line in m.group(1).splitlines():
        if line.strip():
            return line.strip()
    return ""


def read_last_assistant_text(transcript_path):
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
        return 0
    if data.get("stop_hook_active"):
        return 0
    transcript = data.get("transcript_path")
    session = data.get("session_id", "nosession")
    if not transcript:
        return 0
    text = read_last_assistant_text(transcript)
    if not text:
        return 0
    low = text.lower()
    if not any(sig in low for sig in wrap_signals()):
        return 0

    first = kickoff_first_line()
    if first:
        ok = first in text
        want = ("paste the kickoff block from HANDOFF.md verbatim; its first "
                "line is: %r" % first)
    else:
        ok = FENCE in text
        want = ("paste the next-batch kickoff message verbatim inside a "
                "``` fenced block (from HANDOFF.md, section 'Message to paste "
                "into the next chat')")
    if ok:
        return 0

    key = hashlib.sha1(session.encode()).hexdigest()[:16]
    counter = os.path.join(tempfile.gettempdir(), "kickoff_guard_%s" % key)
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
            "This looks like a batch wrap-up, but the reply does not contain "
            "the pasted kickoff message. CLAUDE.md requires every batch to end "
            "with two things in the chat: the attached EPUB and the pasted "
            "kickoff block — %s. Add it now, then finish." % want
        ),
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
