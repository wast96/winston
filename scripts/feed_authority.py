#!/usr/bin/env python3
"""Feed Nameless Heroes' decided/attested renderings back into authority.json
(the cross-book name authority), tagged with this book's slug. Completion-batch
step. Idempotent: re-running adds nothing new. Provisional glossary rows are
SKIPPED (they are the romanizations still to be firmed up, not authority).

For each fed (hanzi, english):
  - existing authority term: append the slug to the matching rendering, or add
    the rendering if this book renders it a new way; then RECOMPUTE that term's
    status from its full rendering set (article-only differences -> 'agreed-
    article-varies'; a real disagreement -> 'reconcile'; a single rendering ->
    'agreed'). Only touched terms are rewritten; the note is preserved.
  - new authority term: create it with the glossary category, this book's slug,
    a trimmed plain note, and status 'agreed'.
Run with --apply to write; default is a dry-run summary.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = "nameless-heroes"
SECT2CAT = {"people": "people", "organizations": "organizations",
            "places": "places", "terms": "terms"}
FEED_STATUS = {"decided", "attested"}


def norm(r):
    r = r.strip()
    for art in ("the ", "The ", "a ", "A ", "an ", "An "):
        if r.startswith(art):
            return r[len(art):].lower()
    return r.lower()


def recompute_status(renderings):
    norms = {norm(r) for r in renderings}
    if len(norms) == 1:
        return "agreed-article-varies" if len(renderings) > 1 else "agreed"
    return "reconcile"


def trim_note(s):
    s = (s or "").strip()
    if len(s) <= 240:
        return s
    cut = s[:240]
    dot = cut.rfind(". ")
    return (cut[:dot + 1] if dot > 80 else cut).rstrip()


def main(apply):
    gloss = json.load(open(os.path.join(ROOT, "glossary.json"), encoding="utf-8"))
    auth = json.load(open(os.path.join(ROOT, "authority.json"), encoding="utf-8"))
    terms = auth["terms"]

    new_terms = 0
    new_renderings = 0
    slug_appends = 0
    already = 0
    touched = set()

    for sect, cat in SECT2CAT.items():
        rows = gloss.get(sect, {})
        if not isinstance(rows, dict):
            continue
        for hanzi, row in rows.items():
            if row.get("status") not in FEED_STATUS:
                continue
            en = (row.get("en") or "").strip()
            if not en:
                continue
            if hanzi in terms:
                rd = terms[hanzi]["renderings"]
                if en in rd:
                    if SLUG in rd[en]:
                        already += 1
                    else:
                        rd[en].append(SLUG)
                        slug_appends += 1
                        touched.add(hanzi)
                else:
                    rd[en] = [SLUG]
                    new_renderings += 1
                    touched.add(hanzi)
            else:
                terms[hanzi] = {
                    "renderings": {en: [SLUG]},
                    "category": cat,
                    "status": "agreed",
                    "note": trim_note(row.get("note", "")),
                }
                new_terms += 1

    # recompute status only for pre-existing terms we touched
    for hanzi in touched:
        terms[hanzi]["status"] = recompute_status(terms[hanzi]["renderings"])

    print("new terms:        %d" % new_terms)
    print("new renderings:   %d (this book disagrees with prior books)" % new_renderings)
    print("slug appends:     %d (this book agrees with a prior rendering)" % slug_appends)
    print("already had slug: %d" % already)
    print("touched existing: %d" % len(touched))
    print("authority terms total: %d" % len(terms))

    if new_renderings:
        print("\n-- new-rendering (potential reconcile) terms --")
        # show them for review
        shown = 0
        for sect, cat in SECT2CAT.items():
            for hanzi, row in gloss.get(sect, {}).items():
                if row.get("status") in FEED_STATUS and hanzi in terms:
                    rd = terms[hanzi]["renderings"]
                    en = (row.get("en") or "").strip()
                    if en in rd and rd[en] == [SLUG] and len(rd) > 1 and shown < 60:
                        print("   %s  ->  %s   (others: %s)" %
                              (hanzi, en, ", ".join(r for r in rd if r != en)))
                        shown += 1

    if apply:
        json.dump(auth, open(os.path.join(ROOT, "authority.json"), "w",
                             encoding="utf-8"), ensure_ascii=False, indent=1)
        # re-read verify
        a2 = json.load(open(os.path.join(ROOT, "authority.json"), encoding="utf-8"))
        assert a2["terms"]["军统"], "sanity"
        print("\nAPPLIED and re-read verified.")
    else:
        print("\nDRY-RUN (pass --apply to write).")


if __name__ == "__main__":
    main("--apply" in sys.argv)
