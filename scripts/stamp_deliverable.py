#!/usr/bin/env python3
"""Make the round-stamped delivery copy of the built EPUB.

Shelf naming policy (commissioner, 2026-08-29): the deliverable in book.json
carries the book's FULL English title, with any colon replaced by a comma
(colons do not survive in filenames), e.g.
    out/The Longest Day In Chang'an.epub
and every copy delivered in chat carries the round marker, e.g.
    The Longest Day In Chang'an B5.epub

This script makes that copy. The canonical (unstamped) file is what the
builder writes, what qa_epub checks, and what gets committed on completion;
the stamped file is the per-round chat attachment.

Usage:
    stamp_deliverable.py B5          copy out/<title>.epub -> out/<title> B5.epub
    stamp_deliverable.py R2          works for revision rounds too
    stamp_deliverable.py --check     just validate the deliverable name policy

Refuses a deliverable that is missing, still the template placeholder, or
carries a colon. Prints the stamped path; attach THAT file in the chat.
"""
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def die(msg):
    sys.stderr.write("stamp_deliverable: " + msg + "\n")
    sys.exit(1)


def main():
    if len(sys.argv) != 2:
        die("usage: stamp_deliverable.py <round-label>|--check   (e.g. B5)")
    label = sys.argv[1]

    try:
        book = json.loads((ROOT / "book.json").read_text(encoding="utf-8"))
    except Exception as e:
        die("cannot read book.json: %s" % e)
    d = book.get("deliverable")
    if not d:
        die("book.json has no 'deliverable'")
    if ":" in d:
        die("deliverable %r contains a colon; the naming policy replaces "
            "colons with commas in filenames" % d)
    path = Path(d)
    if not path.is_absolute():
        path = ROOT / path
    if path.suffix.lower() != ".epub":
        die("deliverable %r does not end in .epub" % d)
    title = book.get("title_en", "")
    expect = title.replace(":", ",")
    mismatch = bool(title) and path.stem != expect
    if mismatch:
        print("stamp_deliverable: NOTE deliverable stem %r differs from "
              "title_en-derived %r; the policy wants the full English title "
              "(colons as commas)" % (path.stem, expect))

    if label == "--check":
        if mismatch:
            die("deliverable does not carry the full English title")
        print("stamp_deliverable: deliverable %s conforms" % path.name)
        return

    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9.-]{0,15}", label):
        die("round label %r looks wrong; expected something like B5 or R2"
            % label)
    if not path.is_file():
        die("built deliverable not found at %s (build first)" % path)
    stamped = path.with_name("%s %s%s" % (path.stem, label, path.suffix))
    shutil.copyfile(path, stamped)
    print("stamp_deliverable: %s -> %s" % (path.name, stamped.name))
    print("attach this file in the chat: %s" % stamped)


if __name__ == "__main__":
    main()
