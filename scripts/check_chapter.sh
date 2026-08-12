#!/usr/bin/env bash
# Run the full per-chapter QC battery for one unit id.
# Usage: bash scripts/check_chapter.sh ch03 06_part0004  (src file base optional)
set -u
cid="$1"
src="$2"     # e.g. 07_part0005
title="$3"   # English title, quoted
cd "$(dirname "$0")/.."
python3 scripts/reading_to_en.py "$cid" || exit 1
python3 scripts/make_bilingual.py "$cid" "data/src/${src}.txt" "$title" "out/${cid}_en.json" || exit 1
echo "--- verify_unit ---"; python3 scripts/verify_unit.py "$cid"
echo "--- gen_check_config ---"; python3 scripts/gen_check_config.py >/dev/null && echo "config regenerated"
echo "--- check_align ---"; python3 scripts/check_align.py "$cid" 2>&1 | grep -E "source|OK|FAIL|WARN" | head
echo "--- check_content ---"; python3 scripts/check_content.py --config check_config.json 2>&1 | grep -E "$cid|OK|displaced|FAIL" | head
echo "--- qc_entities ---"; python3 scripts/qc_entities.py "out/${cid}_bilingual.md" glossary.json 2>&1 | grep -E "misses|FAIL"
echo "--- check_apparatus ---"; python3 scripts/check_apparatus.py 2>&1 | tail -1
echo "--- register ---"; python3 scripts/check_register.py --ref reference/ch01_ref.md "out/${cid}_reading.md" 2>&1 | tail -2
