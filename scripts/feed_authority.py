#!/usr/bin/env python3
"""Feed this book's decided renderings back into authority.json on completion
(the cross-book name ledger; CLAUDE.md glossary discipline + authority _about
'Feed every new book's decided renderings back in on completion'). Idempotent.

This is an annotated English edition: the body keeps Isaacs's 1930s Wade-Giles,
while the glossary records the MODERN pinyin form for cross-book matching. The
shelf standardizes on pinyin, so the pinyin form is what is registered here
(with a note that this book prints the Wade-Giles form in its text). For a
hanzi already on the shelf: this book's slug is appended to the matching pinyin
rendering, or the pinyin is added as a recorded rendering if the shelf has not
seen it. For a hanzi new to the shelf: a single-book entry is created.

Writes authority.json in place; re-reads to verify.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = "tragedy-of-the-chinese-revolution"
SEC_CAT = {"people": "people", "organizations": "organizations",
           "places": "places", "terms": "terms"}


def main():
    g = json.load(open(os.path.join(ROOT, "glossary.json"), encoding="utf-8"))
    apath = os.path.join(ROOT, "authority.json")
    a = json.load(open(apath, encoding="utf-8"))
    terms = a["terms"]

    added, appended = 0, 0
    for sec, cat in SEC_CAT.items():
        for zh, rec in g.get(sec, {}).items():
            form = (rec.get("pinyin") or rec.get("en") or "").strip()
            if not form:
                continue
            wg = rec.get("en", "")
            wg_note = ("This annotated English edition of Isaacs prints the "
                       "Wade-Giles form “%s” in its text." % wg) if wg else ""
            if zh in terms:
                rends = terms[zh].setdefault("renderings", {})
                if form in rends:
                    if SLUG not in rends[form]:
                        rends[form].append(SLUG)
                        appended += 1
                else:
                    rends[form] = [SLUG]
                    appended += 1
            else:
                note = rec.get("note", "")
                if wg_note:
                    note = (note + " " + wg_note).strip() if note else wg_note
                terms[zh] = {
                    "renderings": {form: [SLUG]},
                    "category": cat,
                    "status": "single-book",
                    "note": note,
                }
                added += 1

    with open(apath, "w", encoding="utf-8") as fh:
        json.dump(a, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    back = json.load(open(apath, encoding="utf-8"))["terms"]
    for sec in SEC_CAT:
        for zh, rec in g.get(sec, {}).items():
            form = (rec.get("pinyin") or rec.get("en") or "").strip()
            if form and (zh not in back or SLUG not in
                         back[zh]["renderings"].get(form, [])):
                raise SystemExit("verify failed for %s/%s" % (zh, form))
    print("authority.json: %d new entries, %d slugs appended; total terms=%d"
          % (added, appended, len(back)))


if __name__ == "__main__":
    main()
