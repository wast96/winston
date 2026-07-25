#!/usr/bin/env python3
"""Re-flow a finished translation onto the source's paragraph boundaries.

Why this exists. The source segmentation was rebuilt several times before it
was right, and the translations of the early units were written against the
intermediate versions. Their WORDING is unaffected -- the sentences are the
sentences -- but their paragraph breaks fall where an older, wrong
segmentation put them. Fixing that by hand, one slip at a time, did not
converge: every join or split shifts everything after it, so the next run
reports a different first offender and it is easy to chase the tail forever.

So it is done in one pass instead. The translation is split into sentences,
each source paragraph is given a share of the whole proportional to its length
in Han characters, and sentences are dealt out to fill those shares in order.
Nothing is reworded, nothing is dropped, and the sentence order is untouched:
only the blank lines between paragraphs move.

The assumption is that the translation is faithful and in the same order as
the source, which is exactly what the numeric and content checks exist to
confirm. Run check_align.py afterwards: if a boundary landed a sentence out,
that pair's ratio will sit off the median and can be nudged by hand.

Usage: reflow.py UNIT [--dry-run]
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Sentence end in the English, keeping the terminator with its sentence and
# not breaking on the full stop of an abbreviation or an initial.
# The boundary is the WHITESPACE only. An earlier version let the pattern
# consume the closing quotation marks after the stop, which silently deleted
# them from the prose -- 'a "working wife."' came back as 'a "working wife.'
# and took two footnote anchors with it. Nothing but the space may be matched.
SENT = re.compile(r'(?<=[.!?"”’\')])\s+(?=[A-Z"“‘(])')
ABBR = re.compile(r"\b(?:Mr|Mrs|Ms|Dr|St|No|vol|ed|cf|e\.g|i\.e)\.$", re.I)


def sentences(par):
    out, buf = [], ""
    for piece in SENT.split(par):
        cand = (buf + " " + piece).strip() if buf else piece
        if ABBR.search(cand):
            buf = cand
            continue
        out.append(cand)
        buf = ""
    if buf:
        out.append(buf)
    return [s for s in out if s.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("unit")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    src_path = os.path.join(ROOT, "data", "zh", "%s.txt" % a.unit)
    tgt_path = os.path.join(ROOT, "out", "%s_reading.md" % a.unit)

    src_blocks = [l.rstrip("\n") for l in open(src_path) if l.strip()]
    src_paras = [l for l in src_blocks if not l.startswith("###")]

    lines = [l.rstrip("\n") for l in open(tgt_path)]
    head, body = [], []
    for l in lines:
        if l.strip().startswith("#"):
            head.append(l.strip())
        elif l.strip():
            body.append(l.strip())

    sents = []
    for par in body:
        sents.extend(sentences(par))

    weights = [max(1, len(re.findall(r"[一-鿿]", p))) for p in src_paras]
    total_w = float(sum(weights))
    lens = [len(s) for s in sents]
    total_l = float(sum(lens))

    # Assign sentences to paragraphs by DYNAMIC PROGRAMMING rather than by
    # dealing them out greedily. Greedy gets most boundaries right and leaves
    # a scatter of them one sentence out, because an early rounding error is
    # never revisited. The cost of a paragraph is how far its English length
    # falls from what its Han length predicts, and the DP minimises the total
    # over the whole chapter, so a boundary is only placed badly if placing it
    # well would cost more somewhere else.
    n_s, n_p = len(sents), len(weights)
    if n_s < n_p:
        print("refusing: %d sentences for %d paragraphs" % (n_s, n_p),
              file=sys.stderr)
        return 1
    # NUMBERS AS ANCHORS. Length alone decides only how much English belongs
    # to a paragraph, not which English. Quantities survive translation and
    # are the one content signal that can be matched across the two languages
    # cheaply, so a paragraph is penalised for every numeral its source has
    # that its assigned sentences do not. That is what stops a sentence
    # carrying "in July" from being dealt into the paragraph next to the one
    # whose source says 七月.
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import check_numbers as CN
    src_nums = [CN.source_numbers(p_) for p_ in src_paras]
    sent_nums = [CN.target_numbers(s) for s in sents]

    # NAMES AS ANCHORS TOO. Numerals alone are not enough, because the
    # passages most likely to drift are narrative and carry no numbers: ch02's
    # boundaries slipped by one across roughly paragraphs 48-78, the stretch
    # covering the assassinations and the Lu Haifang episode, where the DP had
    # nothing but length to go on and length cannot tell WHICH sentences
    # belong to a paragraph, only how many characters of them.
    #
    # The glossary is already a hanzi-to-English key maintained for exactly
    # this correspondence, so it is reused here. Only distinctive proper names
    # qualify: a generic rendering like 特务 -> "secret agent / operative"
    # never appears literally in the prose and would poison every paragraph
    # with a phantom miss.
    names = {}
    gpath = os.path.join(ROOT, "glossary.json")
    if os.path.exists(gpath):
        import json as _json
        for _cat, _entries in _json.load(open(gpath)).items():
            for _zh, _e in _entries.items():
                _en = _e.get("en", "")
                if len(_zh) < 2 or "/" in _en or len(_en) < 4:
                    continue
                if not _en[0].isupper():
                    continue
                names[_zh] = _en
    src_names = [{en for zh, en in names.items() if zh in p_} for p_ in src_paras]
    sent_names = [{en for en in names.values() if en in s} for s in sents]

    scale = total_l / total_w
    pre = [0]
    for L in lens:
        pre.append(pre[-1] + L)

    INF = float("inf")
    # cost[p][i] = best cost covering paragraphs p.. with sentences i..
    prev = [INF] * (n_s + 1)
    prev[n_s] = 0.0
    choice = [[0] * (n_s + 1) for _ in range(n_p)]
    for p in range(n_p - 1, -1, -1):
        cur = [INF] * (n_s + 1)
        want = weights[p] * scale
        # paragraph p must leave at least one sentence for each later paragraph
        latest = n_s - (n_p - 1 - p)
        for i in range(min(latest, n_s), -1, -1):
            best, best_j = INF, i + 1
            for j in range(i + 1, min(latest, n_s) + 1):
                if prev[j] == INF:
                    continue
                got = pre[j] - pre[i]
                have = set()
                have_n = set()
                for k2 in range(i, j):
                    have |= sent_nums[k2]
                    have_n |= sent_names[k2]
                missed = len(src_nums[p] - have)
                # A name the source paragraph carries but the assigned
                # sentences do not is weighted like a missing numeral: both
                # are content the translation must contain if the boundary is
                # in the right place.
                # Charged BOTH WAYS. A one-sided penalty only asks whether the
                # paragraph got the names its source has; it is free to be
                # given names its source does not have, which is precisely
                # what a boundary one sentence out looks like from the other
                # side. Charging the stray name as well pins the boundary
                # between two adjacent paragraphs that both mention the same
                # person -- the case the one-sided version could not resolve,
                # and where ch02's last few slips survived.
                missed_n = len(src_names[p] - have_n)
                stray_n = len(have_n - src_names[p])
                c = (prev[j] + abs(got - want) ** 1.5
                     + 900.0 * missed + 900.0 * missed_n + 600.0 * stray_n)
                if c < best:
                    best, best_j = c, j
            cur[i] = best
            choice[p][i] = best_j
        prev = cur

    out, i = [], 0
    for p in range(n_p):
        j = choice[p][i]
        out.append(" ".join(sents[i:j]))
        i = j
    if i < n_s:
        out[-1] = (out[-1] + " " + " ".join(sents[i:])).strip()

    # Nothing may be lost or altered: the characters of the re-flowed
    # paragraphs must be exactly the characters of the sentences that went in,
    # ignoring the whitespace at the joins. Reflow moves paragraph breaks and
    # must never touch a word.
    def squash(x):
        return re.sub(r"\s+", "", x)

    if squash("".join(out)) != squash("".join(sents)):
        print("refusing: re-flow would change the text, not just its "
              "paragraphing", file=sys.stderr)
        return 1

    if len(out) != len(src_paras):
        print("refusing: produced %d paragraphs for %d source"
              % (len(out), len(src_paras)), file=sys.stderr)
        return 1

    text = "\n\n".join(([head[0]] if head else []) + [])
    rebuilt = []
    if head:
        rebuilt.append(head[0])
    # re-insert section headings at their source positions
    hi = 1
    pi = 0
    for block in src_blocks:
        if block.startswith("###"):
            if hi < len(head):
                rebuilt.append(head[hi])
                hi += 1
        else:
            rebuilt.append(out[pi])
            pi += 1

    result = "\n\n".join(rebuilt) + "\n"
    print("%s: %d sentences -> %d paragraphs (source %d)"
          % (a.unit, len(sents), len(out), len(src_paras)))
    if a.dry_run:
        return 0
    open(tgt_path, "w").write(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
