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


def hook_test(failures):
    """Simulate the Stop hook: it must BLOCK a wrap-up reply missing the
    kickoff block, PASS one that pastes it, ignore normal chat, and fail
    open on garbage input."""
    import json, tempfile
    hook = os.path.join(ROOT, ".claude", "hooks", "kickoff_guard.py")
    if not os.path.exists(hook):
        return
    # The hook deliberately stands down when HANDOFF.md still carries the
    # template's placeholder kickoff (a template-maintenance session is not
    # a book batch). To test the ENFORCING path, stage a realistic kickoff,
    # and restore the real file afterward no matter what.
    hpath = os.path.join(ROOT, "HANDOFF.md")
    handoff_backup = open(hpath).read()
    first = "Test Book B02"
    open(hpath, "w").write(
        "# HANDOFF\n\n## Message to paste into the next chat\n\n"
        "```\n%s\n\nRead CLAUDE.md, then HANDOFF.md. Do batch B02.\n```\n"
        % first)

    import uuid as _uuid
    _run_tag = _uuid.uuid4().hex[:8]

    def run(reply, session):
        session = session + "-" + _run_tag  # the hook caps blocks per
        # session in a /tmp counter; a reused id would exhaust the cap
        # across test runs and fake a failure
        tr = tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False)
        tr.write(json.dumps({"type": "assistant",
                             "message": {"content": [
                                 {"type": "text", "text": reply}]}}) + "\n")
        tr.close()
        p = subprocess.run([sys.executable, hook], capture_output=True,
                           text=True, input=json.dumps(
                               {"transcript_path": tr.name,
                                "session_id": session}))
        os.unlink(tr.name)
        return p.returncode, p.stdout

    rc, out = run("Batch done, qa_epub green, book.epub attached.", "t-block")
    blocked = '"decision": "block"' in out or '"decision":"block"' in out
    if not blocked:
        failures.append("hook: wrap-up WITHOUT kickoff was not blocked")
    print("hook blocks kickoff-less wrap-up:", "OK" if blocked else "FAIL")

    good = "Batch done, qa_epub green.\n```\n%s\nrest of kickoff\n```" % first
    rc, out = run(good, "t-pass")
    passed = "block" not in out
    if not passed:
        failures.append("hook: compliant wrap-up was blocked: %s" % out)
    print("hook passes compliant wrap-up:", "OK" if passed else "FAIL")

    rc, out = run("Just a normal chat reply about nothing.", "t-chat")
    if "block" in out:
        failures.append("hook: normal chat was blocked")
    print("hook ignores normal chat:", "OK" if "block" not in out else "FAIL")

    p = subprocess.run([sys.executable, hook], capture_output=True, text=True,
                       input="NOT JSON")
    if p.returncode != 0 or "block" in p.stdout:
        failures.append("hook: did not fail open on garbage input")
    print("hook fails open on garbage:", "OK"
          if p.returncode == 0 and "block" not in p.stdout else "FAIL")

    # placeholder stand-down: with the template's stub HANDOFF restored, a
    # wrap-up-looking reply must NOT be blocked (the false positive happened)
    open(hpath, "w").write(handoff_backup)
    rc, out = run("Batch done, qa_epub green, book.epub attached.", "t-stub")
    if "block" in out:
        failures.append("hook: blocked during template maintenance "
                        "(placeholder stand-down broken)")
    print("hook stands down on template stub:", "OK"
          if "block" not in out else "FAIL")


def builder_test(failures):
    """Build the stub skeleton twice: qa_epub must PASS and the OPF must be
    byte-identical (deterministic dcterms:modified). Then verify the builder
    REFUSES an unmatched note anchor (the 12-lost-footnotes gate)."""
    import shutil, zipfile
    out1 = os.path.join(ROOT, "out", "_test1.epub")
    out2 = os.path.join(ROOT, "out", "_test2.epub")
    build = os.path.join(ROOT, "scripts", "build_reading_epub.py")
    qa = os.path.join(ROOT, "scripts", "qa_epub.py")
    try:
        for o in (out1, out2):
            p = subprocess.run([sys.executable, build, o],
                               capture_output=True, text=True)
            if p.returncode != 0:
                failures.append("builder: skeleton build failed:\n" + p.stderr)
                print("builder skeleton build: FAIL")
                return
        p = subprocess.run([sys.executable, qa, out1],
                           capture_output=True, text=True)
        ok = p.returncode == 0
        if not ok:
            failures.append("builder: qa_epub failed:\n" + p.stdout)
        print("builder skeleton qa_epub:", "OK" if ok else "FAIL")
        opf1 = zipfile.ZipFile(out1).read("OEBPS/content.opf")
        opf2 = zipfile.ZipFile(out2).read("OEBPS/content.opf")
        det = opf1 == opf2
        if not det:
            failures.append("builder: two builds differ (non-deterministic "
                            "metadata reintroduced)")
        print("builder deterministic OPF:", "OK" if det else "FAIL")

        # refuse-on-unmatched-anchor round trip
        notes_path = os.path.join(ROOT, "notes.json")
        backup = open(notes_path).read()
        import json as _json
        book = _json.load(open(os.path.join(ROOT, "book.json")))
        cid = book["structure"][0]["id"]
        reading = os.path.join(ROOT, "out", "%s_reading.md" % cid)
        made_reading = not os.path.exists(reading)
        try:
            if made_reading:
                with open(reading, "w") as fh:
                    fh.write("## Test Chapter\n\nA plain test paragraph.\n")
            _json.dump({cid: [{"anchor": "THIS ANCHOR MATCHES NOTHING",
                               "note": "orphan"}]},
                       open(notes_path, "w"))
            p = subprocess.run([sys.executable, build, out1],
                               capture_output=True, text=True)
            refused = p.returncode != 0
            if not refused:
                failures.append("builder: did NOT refuse an unmatched anchor")
            print("builder refuses orphan anchor:", "OK" if refused else "FAIL")
        finally:
            open(notes_path, "w").write(backup)
            if made_reading and os.path.exists(reading):
                os.unlink(reading)
    finally:
        for o in (out1, out2):
            if os.path.exists(o):
                os.unlink(o)


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

    hook_test(failures)
    builder_test(failures)

    if failures:
        print("\n" + "\n".join(failures))
        return 1
    print("all checker regression tests green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
