#!/usr/bin/env bash
# One-command environment setup for an EPUB-translation session. Idempotent.
# Much lighter than the scanned-book template: no OCR engine, no renderer.
set -u
REPORT=SETUP_REPORT.txt
: > "$REPORT"
note() { echo "$*" | tee -a "$REPORT"; }

python3 -c "import PIL" 2>/dev/null || pip install -q pillow \
  || note "PIP FAILED: pillow (figure/cover handling degrades gracefully)"

# epubcheck: the store-conformance gate qa_epub.py cannot replace
EC_DIR=/tmp/epubcheck-5.1.0
if [ ! -f "$EC_DIR/epubcheck.jar" ]; then
  if command -v java >/dev/null; then
    curl -sL -o /tmp/epubcheck.zip \
      https://github.com/w3c/epubcheck/releases/download/v5.1.0/epubcheck-5.1.0.zip \
      && unzip -q -o /tmp/epubcheck.zip -d /tmp/ \
      || note "FETCH FAILED: epubcheck (run qa_epub.py alone and say so)"
  else
    note "java missing: epubcheck unavailable (run qa_epub.py alone and say so)"
  fi
fi

python3 tests/run_tests.py >>"$REPORT" 2>&1 \
  && note "checker regression tests: green" \
  || note "CHECKER REGRESSION TESTS FAILED — fix before translating"
note "setup done; anything above marked FAILED goes in PROGRESS.md"
