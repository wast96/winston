#!/usr/bin/env bash
# Sync the shared layer FROM the scanned template (the upstream for shared
# code) INTO this checkout. Run on the EPUB template branch after landing a
# shared fix on claude/translation-template-master, then review the diff and
# commit. One fix, two branches, no drift.
set -eu
SRC=${1:-claude/translation-template-master}
SHARED=(
  scripts/check_numbers.py scripts/check_structure.py scripts/qa_epub.py
  scripts/check_align.py scripts/check_content.py scripts/qc_entities.py
  scripts/check_register.py scripts/check_apparatus.py
  scripts/check_reconcile.py scripts/verify_unit.py scripts/apply_edits.py
  scripts/apparatus_merge.py scripts/smart_quotes.py scripts/reflow.py
  tests/run_tests.py data/noise.txt authority.json COLLECTION.md
  REVISION_PLAN.template.md COMPLETION.template.md review/PROTOCOL.md
  .claude/hooks/kickoff_guard.py
)
for f in "${SHARED[@]}"; do
  git checkout "$SRC" -- "$f" 2>/dev/null && echo "synced $f" \
    || echo "SKIP (not on $SRC): $f"
done
python3 tests/run_tests.py
echo "review with: git diff --cached"
