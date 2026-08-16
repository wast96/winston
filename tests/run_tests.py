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

    # placeholder stand-down: when HANDOFF.md still carries the template's
    # placeholder kickoff (first line "(First line: ...)"), a wrap-up-looking
    # reply must NOT be blocked (the false positive happened). Stage an actual
    # stub here; the restored real handoff of an active book is NOT a stub, so
    # relying on handoff_backup made this subcase false-fail on every book.
    open(hpath, "w").write(
        "# HANDOFF\n\n## Message to paste into the next chat\n\n"
        "```\n(First line: <Project> <Bxx>)\n\nRead CLAUDE.md, then "
        "HANDOFF.md. Do the batch.\n```\n")
    rc, out = run("Batch done, qa_epub green, book.epub attached.", "t-stub")
    open(hpath, "w").write(handoff_backup)  # restore the real handoff
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


def style_test(failures):
    """Compose the shelf-wide style layers for a fiction (ja) and a nonfiction
    (zh) book and assert: mechanical layer selection, VOICE_TARGET substituted
    with no placeholder left, deterministic output, the freshness check reads
    FRESH then STALE, and the composer refuses a genre layer missing its
    VOICE_TARGET directive."""
    import json, re, shutil, tempfile
    compose = os.path.join(ROOT, "scripts", "compose_style.py")
    fresh = os.path.join(ROOT, "scripts", "check_style_freshness.py")
    styles = os.path.join(ROOT, "styles")
    if not os.path.isfile(compose) or not os.path.isdir(styles):
        return
    tmp = tempfile.mkdtemp(prefix="styletest_")
    try:
        cases = {
            "fic": ({"title_en": "T", "source_language": "ja",
                     "subjects": ["FICTION / Historical"]},
                    "ja", "fiction", "translator of serious literary fiction"),
            "non": ({"title_en": "T", "source_language": "zh",
                     "subjects": ["History / Asia / China"]},
                    "zh", "nonfiction", "writer of popular narrative history"),
        }
        for tag, (book, lang, genre, voice) in cases.items():
            bj = os.path.join(tmp, "%s.book.json" % tag)
            out = os.path.join(tmp, "%s.STYLE.md" % tag)
            open(bj, "w").write(json.dumps(book))
            p = subprocess.run([sys.executable, compose, "--book", bj,
                                "--styles", styles, "--out", out,
                                "--local", os.path.join(tmp, "%s.local.md" % tag)],
                               capture_output=True, text=True)
            if p.returncode != 0:
                failures.append("compose_style %s failed: %s" % (tag, p.stderr))
                print("compose_style %s:" % tag, "FAIL")
                continue
            text = open(out).read()
            man = json.loads(re.search(
                r"<!-- STYLE_MANIFEST\n(.*?)\nSTYLE_MANIFEST -->", text, re.S).group(1))
            ok = (man["language"] == lang and man["genre"] == genre
                  and "{{" not in text and voice in text)
            if not ok:
                failures.append("compose_style %s: wrong selection/substitution "
                                "(lang=%s genre=%s)" % (tag, man["language"], man["genre"]))
            print("compose_style %s (%s/%s):" % (tag, lang, genre),
                  "OK" if ok else "FAIL")
            # determinism
            out2 = os.path.join(tmp, "%s.2.STYLE.md" % tag)
            subprocess.run([sys.executable, compose, "--book", bj, "--styles",
                            styles, "--out", out2, "--local",
                            os.path.join(tmp, "%s.2.local.md" % tag)],
                           capture_output=True, text=True)
            det = open(out).read() == open(out2).read()
            if not det:
                failures.append("compose_style %s: non-deterministic output" % tag)
            print("compose_style %s deterministic:" % tag, "OK" if det else "FAIL")

        # freshness: FRESH against the real layers, STALE against a mutated copy
        fic_out = os.path.join(tmp, "fic.STYLE.md")
        p = subprocess.run([sys.executable, fresh, "--style", fic_out,
                            "--styles", styles], capture_output=True, text=True)
        fresh_ok = p.returncode == 0 and "All layers fresh" in p.stdout
        if not fresh_ok:
            failures.append("check_style_freshness: not FRESH on unchanged layers")
        print("check_style_freshness fresh:", "OK" if fresh_ok else "FAIL")

        styles2 = os.path.join(tmp, "styles_moved")
        shutil.copytree(styles, styles2)
        with open(os.path.join(styles2, "lang-ja.md"), "a") as fh:
            fh.write("\n<!-- moved -->\n")
        p = subprocess.run([sys.executable, fresh, "--style", fic_out,
                            "--styles", styles2], capture_output=True, text=True)
        stale_ok = p.returncode == 0 and "STALE" in p.stdout
        if not stale_ok:
            failures.append("check_style_freshness: did NOT detect a moved layer")
        print("check_style_freshness stale-detect:", "OK" if stale_ok else "FAIL")

        # composer must refuse a genre layer with no VOICE_TARGET directive
        styles3 = os.path.join(tmp, "styles_bad")
        shutil.copytree(styles, styles3)
        gf = os.path.join(styles3, "genre-fiction.md")
        open(gf, "w").write(re.sub(r"<!--\s*VOICE_TARGET:.*?-->", "",
                                   open(gf).read(), count=1))
        bj = os.path.join(tmp, "fic.book.json")
        p = subprocess.run([sys.executable, compose, "--book", bj, "--styles",
                            styles3, "--out", os.path.join(tmp, "bad.STYLE.md"),
                            "--local", os.path.join(tmp, "bad.local.md")],
                           capture_output=True, text=True)
        refused = p.returncode != 0 and "VOICE_TARGET" in p.stderr
        if not refused:
            failures.append("compose_style: did NOT refuse a missing VOICE_TARGET")
        print("compose_style refuses missing VOICE_TARGET:",
              "OK" if refused else "FAIL")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


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
    style_test(failures)

    if failures:
        print("\n" + "\n".join(failures))
        return 1
    print("all checker regression tests green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
