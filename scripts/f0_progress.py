#!/usr/bin/env python3
"""Tiny F0 bookkeeping helper: update the resume marker and append a chapter's
ledger block into PROGRESS.md at the <!-- F0_LEDGER_APPEND --> anchor.

Usage: f0_progress.py <cid> <block_file>
  <cid>        e.g. ch04 (becomes the new "last COMPLETE chapter")
  <block_file> a markdown file whose contents are appended verbatim as the
               chapter's ledger entry (author it with the Write tool).
Idempotent-ish: refuses to append if the exact block is already present.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "PROGRESS.md")
ANCHOR = "<!-- F0_LEDGER_APPEND -->"


def main(cid, block_path):
    block = open(block_path, encoding="utf-8").read().strip()
    s = open(P, encoding="utf-8").read()
    s = re.sub(r"last COMPLETE chapter = ch\d+",
               "last COMPLETE chapter = %s" % cid, s, count=1)
    if block and block in s:
        print("block already present; only resume marker updated")
    else:
        s = s.replace(ANCHOR, block + "\n\n" + ANCHOR, 1)
    open(P, "w", encoding="utf-8").write(s)
    print("PROGRESS updated: resume=%s" % cid)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
