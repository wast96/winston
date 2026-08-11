#!/usr/bin/env python3
"""Raise the contraction count of ch12 to the house register by contracting
ordinary speakers INSIDE dialogue only. Narration voice is left as-is (matching
the frozen ch01/ch11 reference, which keeps most narration uncontracted); the
quoted classical lament has nothing contractible, so it is safe. The metric
(check_register) counts only n't / 'll / 're / 've / 'm.

Operates on scratchpad/ch12_en.txt, one paragraph per line. Contracts only text
that falls inside a double-quoted span ("..."). Re-run build_b07 after.
"""
import re
import sys

# n't-forms first (so "have not" -> "haven't" before "I have" -> "I've"), then
# 'll / 're / 've / 'm. Word-boundary anchored; case-sensitive on the leading
# word so sentence-initial forms are handled by explicit capitalized entries.
REPL = [
    (r"\bcannot\b", "can't"), (r"\bCannot\b", "Can't"),
    (r"\bdo not\b", "don't"), (r"\bDo not\b", "Don't"),
    (r"\bdoes not\b", "doesn't"), (r"\bDoes not\b", "Doesn't"),
    (r"\bdid not\b", "didn't"), (r"\bDid not\b", "Didn't"),
    (r"\bis not\b", "isn't"), (r"\bIs not\b", "Isn't"),
    (r"\bare not\b", "aren't"), (r"\bAre not\b", "Aren't"),
    (r"\bwas not\b", "wasn't"), (r"\bWas not\b", "Wasn't"),
    (r"\bwere not\b", "weren't"), (r"\bWere not\b", "Weren't"),
    (r"\bhave not\b", "haven't"), (r"\bHave not\b", "Haven't"),
    (r"\bhas not\b", "hasn't"), (r"\bHas not\b", "Hasn't"),
    (r"\bhad not\b", "hadn't"), (r"\bHad not\b", "Hadn't"),
    (r"\bwill not\b", "won't"), (r"\bWill not\b", "Won't"),
    (r"\bwould not\b", "wouldn't"), (r"\bWould not\b", "Wouldn't"),
    (r"\bshould not\b", "shouldn't"), (r"\bShould not\b", "Shouldn't"),
    (r"\bcould not\b", "couldn't"), (r"\bCould not\b", "Couldn't"),
    (r"\bmust not\b", "mustn't"), (r"\bMust not\b", "Mustn't"),
    (r"\bneed not\b", "needn't"), (r"\bNeed not\b", "Needn't"),
    (r"\bI am\b", "I'm"),
    (r"\bI have\b", "I've"),
    (r"\byou have\b", "you've"), (r"\bYou have\b", "You've"),
    (r"\bwe have\b", "we've"), (r"\bWe have\b", "We've"),
    (r"\bthey have\b", "they've"), (r"\bThey have\b", "They've"),
    (r"\bI will\b", "I'll"),
    (r"\byou will\b", "you'll"), (r"\bYou will\b", "You'll"),
    (r"\bwe will\b", "we'll"), (r"\bWe will\b", "We'll"),
    (r"\bthey will\b", "they'll"), (r"\bThey will\b", "They'll"),
    (r"\bhe will\b", "he'll"), (r"\bHe will\b", "He'll"),
    (r"\bshe will\b", "she'll"), (r"\bShe will\b", "She'll"),
    (r"\bit will\b", "it'll"), (r"\bIt will\b", "It'll"),
    (r"\bthere will\b", "there'll"), (r"\bThere will\b", "There'll"),
    (r"\bthat will\b", "that'll"), (r"\bThat will\b", "That'll"),
    (r"\byou are\b", "you're"), (r"\bYou are\b", "You're"),
    (r"\bwe are\b", "we're"), (r"\bWe are\b", "We're"),
    (r"\bthey are\b", "they're"), (r"\bThey are\b", "They're"),
]


def contract_span(s):
    for pat, rep in REPL:
        s = re.sub(pat, rep, s)
    return s


def process_line(line):
    # Replace inside every double-quoted span only.
    return re.sub(r'"[^"]*"', lambda m: contract_span(m.group(0)), line)


def main(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    out = [process_line(l) for l in lines]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    print("contracted dialogue in %s" % path)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "scratchpad/ch12_en.txt")
