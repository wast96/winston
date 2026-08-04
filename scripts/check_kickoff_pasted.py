#!/usr/bin/env python3
"""Stop hook: block the turn from ending until the next-batch kickoff message
has actually been pasted into the chat reply.

The commissioner's rule (CLAUDE.md) is that every batch's final chat reply must
paste the fenced kickoff block verbatim, in addition to saving it in HANDOFF.md.
This has been forgotten repeatedly. This hook enforces it deterministically.

How it decides:
  - It engages ONLY right after a batch commit, detected as "the current git
    HEAD commit modified HANDOFF.md". On ordinary turns it does nothing.
  - It reads the kickoff block from HANDOFF.md (the fenced ``` block under the
    "## Message to paste into the next chat" heading) and takes its FIRST and
    LAST non-empty lines as fingerprints.
  - It reads the last assistant message from the session transcript. If BOTH
    fingerprints appear there, the block was pasted -> allow (and record a
    marker keyed to HEAD so later turns on the same commit never re-check).
  - Otherwise -> block, telling the model to paste the block verbatim.

Fail-safe: any error (missing files, git not available, unparseable transcript)
exits 0 and allows the stop. The hook must never wedge a session.
"""
import json
import os
import re
import subprocess
import sys


def out_allow():
    sys.exit(0)


def out_block(reason):
    print(json.dumps({"decision": "block", "reason": reason}))
    sys.exit(0)


def git(root, *args):
    return subprocess.run(["git", "-C", root, *args],
                          capture_output=True, text=True, timeout=10)


def read_kickoff_fingerprints(handoff_path):
    """Return (first_line, last_line) of the fenced kickoff block, or None."""
    try:
        text = open(handoff_path, encoding="utf-8").read()
    except OSError:
        return None
    m = re.search(r"## Message to paste into the next chat\s*\n+```[^\n]*\n(.*?)\n```",
                  text, re.DOTALL)
    if not m:
        return None
    lines = [l.strip() for l in m.group(1).splitlines() if l.strip()]
    if len(lines) < 2:
        return None
    return lines[0], lines[-1]


def last_assistant_text(transcript_path):
    """Concatenate the text blocks of the final assistant message in the JSONL."""
    try:
        raw = open(transcript_path, encoding="utf-8").read().splitlines()
    except OSError:
        return None
    text = None
    for line in raw:
        line = line.strip()
        if not line:
            continue
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        if ev.get("type") != "assistant":
            continue
        msg = ev.get("message", {})
        content = msg.get("content", "")
        if isinstance(content, str):
            text = content
        elif isinstance(content, list):
            parts = [b.get("text", "") for b in content
                     if isinstance(b, dict) and b.get("type") == "text"]
            text = "".join(parts)
    return text


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        out_allow()

    # Avoid infinite loops: if we already blocked once and are being re-invoked
    # inside the same stop, don't keep blocking.
    if payload.get("stop_hook_active"):
        out_allow()

    root = payload.get("cwd") or os.getcwd()
    transcript_path = payload.get("transcript_path")
    handoff = os.path.join(root, "HANDOFF.md")

    if not transcript_path or not os.path.exists(handoff):
        out_allow()

    # Gate: only engage right after a commit that touched HANDOFF.md.
    head = git(root, "rev-parse", "HEAD")
    if head.returncode != 0:
        out_allow()
    head_sha = head.stdout.strip()
    changed = git(root, "diff-tree", "--no-commit-id", "--name-only", "-r", head_sha)
    if changed.returncode != 0 or "HANDOFF.md" not in changed.stdout.split():
        out_allow()

    # Marker: once satisfied for this HEAD, never re-check on later turns.
    marker = os.path.join(root, ".git", "kickoff-pasted-marker")
    try:
        if open(marker).read().strip() == head_sha:
            out_allow()
    except OSError:
        pass

    fp = read_kickoff_fingerprints(handoff)
    if not fp:
        out_allow()
    first_line, last_line = fp

    reply = last_assistant_text(transcript_path) or ""
    if first_line in reply and last_line in reply:
        try:
            with open(marker, "w") as fh:
                fh.write(head_sha)
        except OSError:
            pass
        out_allow()

    out_block(
        "The next-batch kickoff message was NOT pasted into your chat reply. "
        "CLAUDE.md requires the fenced kickoff block (the one under "
        "'## Message to paste into the next chat' in HANDOFF.md) to be pasted "
        "VERBATIM at the end of the batch-completion reply, in a fenced code "
        "block, in addition to saving it in HANDOFF.md. Paste it now, exactly "
        "as it appears in HANDOFF.md (it begins with '" + first_line + "')."
    )


if __name__ == "__main__":
    main()
