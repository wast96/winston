#!/usr/bin/env python3
"""Add B36's one new keyed glossary row BY HAND into the sectioned glossary.json.
Idempotent; every row carries a pinyin field (qc_entities does rec['pinyin']).
Each hanzi key is verified as a substring of the authoritative data/zh/ch43.txt
so a Write-tool CJK mangling cannot slip a corrupted key into the glossary.

B36 = ch43 (英雄无名 篇后续话, the Afterword: a reflective coda over the whole
five-book memoir). It is LIGHT on new proper nouns. The only genuinely new named
figure worth a key is 刘绍唐 Liu Shaotang, founder and editor of the journal
Biographical Literature (传记文学, already keyed as an organization), in which the
whole memoir was serialized; he is met and thanked here for the first time, and
carries a first-appearance footnote. His hanzi appear nowhere else in the corpus
(no cross-chapter conflict), so keying him is safe.

Rendered INLINE, NOT keyed (glossary-key discipline): 刘原深 Liu Yuanshen and 罗敬
Luo Jing are already keyed from earlier parts; 戴雨农（笠) is the already-keyed 戴笠
Dai Li (courtesy Yunong), written here in the source's own 戴雨农（笠) form and NOT
re-keyed. No new places. The five constituent-book titles are handled in-text and
in the first footnote, not as glossary rows."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOSS = os.path.join(ROOT, "glossary.json")
ZH = os.path.join(ROOT, "data", "zh", "ch43.txt")

ADDS = {
    "people": {
        "刘绍唐": {
            "en": "Liu Shaotang",
            "pinyin": "Liu Shaotang",
            "status": "decided",
            "note": "1921-2000; founder and, for some four decades, editor of the "
                    "Taipei monthly Biographical Literature, the foremost venue for "
                    "Republican-era memoir and first-hand historical recollection, "
                    "in which the whole of Chen's memoir was serialized. Chen thanks "
                    "him in the Afterword for the fixed venue and the support he "
                    "gave.",
        },
    },
}


def main():
    zh = open(ZH, encoding="utf-8").read()
    for sect, rows in ADDS.items():
        for hanzi in rows:
            assert hanzi in zh, "key not in data/zh/ch43.txt: %s" % hanzi
    g = json.load(open(GLOSS, encoding="utf-8"))
    added = 0
    for sect, rows in ADDS.items():
        g.setdefault(sect, {})
        for hanzi, row in rows.items():
            if hanzi in g[sect]:
                continue
            g[sect][hanzi] = row
            added += 1
    json.dump(g, open(GLOSS, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("added %d new rows" % added)
    g2 = json.load(open(GLOSS, encoding="utf-8"))
    for sect, rows in ADDS.items():
        for hanzi, row in rows.items():
            assert g2[sect][hanzi]["en"] == row["en"], hanzi
            assert "pinyin" in g2[sect][hanzi], hanzi
    print("re-read verify OK")


if __name__ == "__main__":
    main()
