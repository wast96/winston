#!/bin/bash
# Register-tic battery for the revision pass (REVISION_PLAN.md §3.2).
# Usage: scripts/revision_tics.sh ch06 [ch07 ...]     or: scripts/revision_tics.sh all
# Prints a count per class per unit. A hit is a FLAG, not a verdict: quoted
# documents legitimately hit the battery (REVISION_PLAN.md §3.1); each
# surviving hit must be defended against the read-aloud test, not sed'd blind.
cd "$(dirname "$0")/.."

units="$@"
if [ "$1" = "all" ]; then
  units=$(ls out/ch*_reading.md | sed 's|out/\(ch[0-9]*\)_reading.md|\1|')
fi

count() { grep -ciE "$2" "$1" 2>/dev/null || true; }

for u in $units; do
  f="out/${u}_reading.md"
  [ -f "$f" ] || { echo "$u: missing $f"; continue; }
  echo "########## $u ##########"
  echo "T1 besides(adverbial, approx):     $(grep -ciE '(^|[,;] ?)besides\b|besides[.,]' "$f")"
  echo "T1 thereupon/whereupon:            $(count "$f" '\b(thereupon|whereupon)\b')"
  echo "T1 forthwith/presently/at length:  $(count "$f" '\b(forthwith|presently|at length|ere long)\b')"
  echo "T1 of-a-morning/evening/sudden:    $(count "$f" '\bof (a morning|an evening|a sudden)\b')"
  echo "T1 wont/no wish/made bold/still-less: $(count "$f" '\b(was wont to|had no wish to|made bold to|come what may|and no mistake|still less)\b')"
  echo "T1 nothing for it:                 $(count "$f" 'nothing for it')"
  echo "T1 day-month dates:                $(count "$f" '\b[0-9]{1,2}(st|nd|rd|th)? (of )?(January|February|March|April|May|June|July|August|September|October|November|December)\b')"
  echo "T2 could not but / could only:     $(count "$f" '\b(could not but|could only)\b')"
  echo "T2 cannot/could-not help:          $(count "$f" '\b(cannot help|could not help|not help but)\b')"
  echo "T2 in-the-end question:            $(count "$f" 'in the end[^.]*\?')"
  echo "T2 and-the-rest/others:            $(count "$f" '\band the (rest|others)\b')"
  echo "T2 pivots (namely/that is to say): $(count "$f" '\b(that is to say|which was to say|namely)\b')"
  echo "T2 gerund-of nominalizations:      $(count "$f" '\b[Tt]he [a-z]+(ing|ment) of the\b')"
  echo "T2 litotes (no small/no few):      $(count "$f" '\bno (small|few|little)\b')"
  echo "T3 quoted terms (straight pairs):  $(($(grep -o '"' "$f" | wc -l)/2))"
  echo "T3 archaic quote tags:             $(count "$f" '(in his lifetime|in his later years|recalled in his later years|disclosed many years later)')"
  echo "T5 contractions:                   $(grep -coE "[a-z]+n't" "$f")"
  echo "T6 impersonal one:                 $(count "$f" '\bone (may|might|could|must|can|dared)\b')"
  echo "T4 semicolons:                     $(grep -o ';' "$f" | wc -l)"
  python3 - "$f" <<'EOF'
import re, sys
body = '\n'.join(l for l in open(sys.argv[1]).read().splitlines()
                 if l and not l.startswith('#') and not l.startswith('{') and l.strip() != '***')
sents = re.split(r'(?<=[.!?])\s+(?=[A-Z"“])', body)
lens = [len(s.split()) for s in sents if len(s.split()) > 2]
if lens:
    print(f"T4 sentences >60 / >90 words:      {sum(1 for l in lens if l>60)} / {sum(1 for l in lens if l>90)}  (mean {sum(lens)/len(lens):.1f} wps)")
EOF
done
