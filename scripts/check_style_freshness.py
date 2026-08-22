#!/usr/bin/env python3
"""Report whether a book's composed STYLE.md is still in sync with the layers.

Reads the STYLE_MANIFEST embedded in STYLE.md by compose_style.py, recomputes
the sha256 of each referenced styles/ layer, and prints FRESH or STALE per
layer.

Freshness is INFORMATIONAL WITHIN A BOOK, by design: you do not recompose the
style baseline mid-book (that is the voice-drift risk CLAUDE.md warns about).
A STALE layer is a note for the next book, or for a corrections pass, not a
build failure. So this exits 0 even when stale. It exits non-zero only on a
real fault: STYLE.md missing, no manifest, a layer file gone. Prints what it
measured, always.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


def die(msg):
    sys.stderr.write("check_style_freshness: " + msg + "\n")
    sys.exit(2)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--style", default="STYLE.md")
    ap.add_argument("--styles", default="styles")
    args = ap.parse_args()

    style_path = Path(args.style)
    if not style_path.is_file():
        die("no composed style file at %s (run scripts/compose_style.py)" % args.style)
    text = style_path.read_text(encoding="utf-8")

    m = re.search(r"<!-- STYLE_MANIFEST\n(.*?)\nSTYLE_MANIFEST -->", text, re.S)
    if not m:
        die("%s has no STYLE_MANIFEST; it was not written by compose_style.py"
            % args.style)
    try:
        manifest = json.loads(m.group(1))
        entries = manifest["layers"]
    except (json.JSONDecodeError, KeyError) as e:
        die("STYLE_MANIFEST is malformed: %s" % e)

    styles = Path(args.styles)
    stale, missing = [], []
    print("check_style_freshness: %s (language=%s, genre=%s)"
          % (args.style, manifest.get("language"), manifest.get("genre")))
    for entry in entries:
        name, want = entry["file"], entry["sha256"]
        f = styles / name
        if not f.is_file():
            print("  MISSING  %s (layer file gone)" % name)
            missing.append(name)
            continue
        got = hashlib.sha256(f.read_bytes()).hexdigest()
        if got == want:
            print("  FRESH    %s" % name)
        else:
            print("  STALE    %s (layer changed since this book was composed)" % name)
            stale.append(name)

    if missing:
        die("layer file(s) missing: %s" % ", ".join(missing))
    if stale:
        print("\n%d layer(s) STALE. This is informational: do NOT recompose "
              "mid-book. Note it for the next book or a corrections pass."
              % len(stale))
    else:
        print("\nAll layers fresh.")
    sys.exit(0)


if __name__ == "__main__":
    main()
