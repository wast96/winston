#!/bin/bash
# Register tic battery for the CSW voice/register pass (adapted from the
# sword-roars B09 battery to this book's measured profile; see
# REVISION_PLAN.md for the calibration table). Usage: register_tics.sh chNN
# A hit is a CANDIDATE, not automatically a defect: each must pass or fail
# the read-aloud test / its rule's carve-outs (quoted documents, slogans,
# formal-by-design speakers are exempt).
cd "$(dirname "$0")/.."
f="out/$1_reading.md"
echo "########## $1 ##########"
echo "=== [antique fn-words] (kill list; near-zero in this book, keep it so) ==="
grep -noiE "\b(thereupon|whereupon|at length|presently|ere long|of a morning|of an evening|was wont to|had no wish to|made bold to|come what may|and no mistake|still less could|forthwith|let slip)\b" "$f"
echo "=== [could only / not but / not help] (plain the archaic ones) ==="
grep -noE "(could only|could not but|could not help|cannot help|not help but)" "$f"
echo "=== [pivots 即/也就是] ==="
grep -noE "(that is to say|which was to say|in other words| namely[ ,])" "$f"
echo "=== [de-nominalize 'the Xing of the'] (convert ~2/3; idiomatic ones stay) ==="
grep -noE "[Tt]he [a-z]+(ing|ment) of the" "$f"
echo "=== [等-tag 'and the rest / and the others'] (vary or cut) ==="
grep -noE "(and the rest|and the others)" "$f"
echo "=== [quote-tag archaisms] ==="
grep -noE "(disclosed many years later|in his lifetime|in his later years|in her later years|recalled in his later years|said in his lifetime|would recall)" "$f"
echo "=== [narration ellipsis] (quoted speech that truncates is exempt) ==="
grep -noE '\.\.\.[^"”]' "$f"
echo "=== [narration exclamation] (authorial reveal-bangs; ration hard) ==="
grep -noE '^[^"”]*![^"”]*$' "$f" | grep -vE '"|”' | head -40
echo "=== [in the end inside a question] (到底/究竟 calque) ==="
grep -noE "in the end[^.!?]*\?" "$f"
echo "=== [sentence-initial numeral] ==="
grep -noE "^[0-9]" "$f"
echo "=== [day-month dates] (book standard is month-day) ==="
grep -noE "\b([0-9]{1,2}) (January|February|March|April|May|June|July|August|September|October|November|December)\b" "$f"
echo "=== [British spellings] (book locale is American) ==="
grep -noiE "\b(colour|rumour|licence|honour|labour|neighbour|theatre|centre|defence|realise|organise|recognise)\b" "$f"
echo "=== [no few / no small] (litotes calque) ==="
grep -noE "(no few|no small|not a little)" "$f"
echo "=== [>90-word narration sentences] (spine test; lists + documents exempt) ==="
python3 - "$f" <<'EOF'
import re, sys
text = " ".join(l.strip() for l in open(sys.argv[1]) if l.strip() and not l.startswith("#"))
sents = [s for s in re.split(r'(?<=[.!?])["”]?\s+', text) if len(s.split()) > 1]
for s in sents:
    if len(s.split()) > 90:
        print("%d words: %s..." % (len(s.split()), s[:110]))
EOF