#!/usr/bin/env python3
"""Plumbing for the voice-gate blind-critique loop (CLAUDE.md Step 0c).

The loop's value is a CONTEXT-BLIND reader: a fresh instance handed only the
built chapter, with no source text, no STYLE.md, no glossary, no project
context, asked where the English does not read right. This script does the
deterministic parts; the model does the reading, the fixing, and the evolving.

  prepare <unit>   Assemble the chapter's English prose and its notes into a
                   readable, context-free document, and write it beneath the
                   canonical blind-critic prompt as out/<unit>_critique_prompt.md.
                   Hand THAT file's contents to a fresh subagent with NO other
                   context. Do not add project context to that agent.

  record <unit> <critique_file>
                   Archive a returned critique under review/voice_gate/ with a
                   provenance header and an auto-incremented round number, so the
                   evolution of STYLE.local.md is traceable.

This script never touches STYLE.md or STYLE.local.md; applying fixes and
distilling rules is the session's work, directed by CLAUDE.md Step 0c.
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path

PROMPT_FILE = Path("review/voice_gate_critic_prompt.md")


def die(msg):
    sys.stderr.write("voice_gate_critique: " + msg + "\n")
    sys.exit(1)


def render_reading(text):
    """Turn a *_reading.md into natural reading prose: strip the structural
    markers a reader never sees, keep the words."""
    out = []
    for line in text.splitlines():
        s = line.rstrip("\n")
        if s.strip() == "***":
            out.append("* * *")
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            out.append(m.group(2))          # heading text, no ATX marks
            continue
        # set-off markers: drop the leading token, keep the content
        s = re.sub(r"^\{[vdgp]\}\s?", "", s)
        out.append(s)
    return "\n".join(out)


def detag(xhtml):
    """XHTML note body -> plain text for a prose read."""
    t = re.sub(r"<[^>]+>", "", xhtml)
    return html.unescape(t).strip()


def cmd_prepare(args):
    reading = Path(args.out) / ("%s_reading.md" % args.unit)
    if not reading.is_file():
        die("no reading file at %s" % reading)
    prose = render_reading(reading.read_text(encoding="utf-8")).strip()

    notes_block = ""
    notes_path = Path(args.notes)
    if notes_path.is_file():
        try:
            notes = json.loads(notes_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            die("%s is not valid JSON: %s" % (notes_path, e))
        unit_notes = notes.get(args.unit, [])
        if unit_notes:
            lines = ["", "", "---", "", "NOTES (these are prose too; judge them):", ""]
            for n in unit_notes:
                anchor = n.get("anchor", "")
                lines.append("- [%s] %s" % (anchor, detag(n.get("note", ""))))
            notes_block = "\n".join(lines)

    if not PROMPT_FILE.is_file():
        die("missing blind-critic prompt at %s" % PROMPT_FILE)
    prompt_full = PROMPT_FILE.read_text(encoding="utf-8")
    # everything after the first '---' rule is the prompt handed to the reader
    parts = prompt_full.split("\n---\n", 1)
    prompt = (parts[1] if len(parts) == 2 else prompt_full).strip()

    doc = (prompt + "\n\n" + "=" * 70 + "\n\n"
           + "CHAPTER UNDER REVIEW\n\n" + prose + notes_block + "\n")
    out_path = Path(args.out) / ("%s_critique_prompt.md" % args.unit)
    out_path.write_text(doc, encoding="utf-8")
    print("voice_gate_critique: wrote %s (%d chars of chapter text)"
          % (out_path, len(prose)))
    print("  Hand this file's CONTENTS to a fresh subagent with NO other context.")
    print("  It must not see the source, STYLE.md, the glossary, or this project.")


def cmd_record(args):
    src = Path(args.critique)
    if not src.is_file():
        die("no critique file at %s" % src)
    outdir = Path("review/voice_gate")
    outdir.mkdir(parents=True, exist_ok=True)
    existing = list(outdir.glob("%s_round*_critique.md" % args.unit))
    rounds = [int(m.group(1)) for p in existing
              for m in [re.search(r"_round(\d+)_critique", p.name)] if m]
    n = (max(rounds) + 1) if rounds else 1
    dest = outdir / ("%s_round%d_critique.md" % (args.unit, n))
    header = ("<!-- blind voice-gate critique | unit=%s | round=%d | "
              "reader was context-blind (no source, no STYLE, no project) -->\n\n"
              % (args.unit, n))
    dest.write_text(header + src.read_text(encoding="utf-8"), encoding="utf-8")
    print("voice_gate_critique: recorded round %d -> %s" % (n, dest))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="out", help="dir holding <unit>_reading.md")
    ap.add_argument("--notes", default="notes.json")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("prepare", help="build the blind-critique prompt document")
    p.add_argument("unit")
    p.set_defaults(func=cmd_prepare)
    r = sub.add_parser("record", help="archive a returned critique with provenance")
    r.add_argument("unit")
    r.add_argument("critique")
    r.set_defaults(func=cmd_record)
    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
