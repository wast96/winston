#!/usr/bin/env python3
"""Regression harness for the template's checker scripts.

Run from the project root:  python3 tests/run_tests.py

Two fixtures for check_numbers.py:
  tests/check_numbers_pass.md  — known traps; every pair must be clean.
  tests/check_numbers_fail.md  — real drops; every pair must flag.

The point: check_numbers accumulated the same fix nine separate times across
nine books, and at least twice a fix broke another case (a NOISE narrowing
that ate 三十步; an ordering change that orphaned a 万). Any edit to the
checkers must keep this harness green before it ships.

Extend the fixtures every time a project discovers a new trap: add the pair
here in the same commit as the fix.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run_numbers(fixture):
    p = subprocess.run(
        [sys.executable, os.path.join(ROOT, "scripts", "check_numbers.py"),
         os.path.join(ROOT, "tests", fixture)],
        capture_output=True, text=True)
    return p.returncode, p.stdout


def main():
    failures = []

    rc, out = run_numbers("check_numbers_pass.md")
    if rc != 0:
        failures.append("PASS fixture flagged pairs (false positives "
                        "reintroduced):\n" + out)
    print("check_numbers pass-fixture:", "OK" if rc == 0 else "FAIL")

    rc, out = run_numbers("check_numbers_fail.md")
    # every pair in the fail fixture must flag
    expected = sum(1 for line in open(
        os.path.join(ROOT, "tests", "check_numbers_fail.md"))
        if line.startswith(">"))
    flagged = out.count("pair ")
    if flagged < expected:
        failures.append("FAIL fixture: only %d of %d drops detected — a "
                        "noise rule is masking a real drop:\n%s"
                        % (flagged, expected, out))
    print("check_numbers fail-fixture: %d/%d drops detected %s"
          % (flagged, expected, "OK" if flagged >= expected else "FAIL"))

    if failures:
        print("\n" + "\n".join(failures))
        return 1
    print("all checker regression tests green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
