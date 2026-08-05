#!/usr/bin/env bash
# One-command environment setup for a translation session. Idempotent; run at
# the top of every fresh session. Records anything that would not install in
# SETUP_REPORT.txt instead of failing the whole run (a bad apt package can
# abort a whole transaction, so packages install individually).
set -u
REPORT=SETUP_REPORT.txt
: > "$REPORT"
note() { echo "$*" | tee -a "$REPORT"; }

# --- Python stack (rendering, image work; PyMuPDF because poppler often
# cannot decode old scans' JBIG2 streams) ---
for pkg in pymupdf pillow numpy opencv-python-headless; do
  python3 -c "import ${pkg%%-*}" 2>/dev/null || pip install -q "$pkg" \
    || note "PIP FAILED: $pkg"
done

# --- OCR: tesseract + language packs. Install ONE AT A TIME. Edit the pack
# list for this book's script (Traditional: chi-tra + chi-tra-vert;
# simplified: chi-sim + chi-sim-vert). ---
if ! command -v tesseract >/dev/null; then
  sudo apt-get update -qq 2>>"$REPORT" || true
  sudo apt-get install -y -qq tesseract-ocr 2>>"$REPORT" \
    || note "APT FAILED: tesseract-ocr"
fi
for pack in tesseract-ocr-chi-sim tesseract-ocr-chi-sim-vert \
            tesseract-ocr-chi-tra tesseract-ocr-chi-tra-vert; do
  dpkg -s "$pack" >/dev/null 2>&1 || sudo apt-get install -y -qq "$pack" \
    2>>"$REPORT" || note "APT FAILED: $pack"
done

# PaddleOCR is a stronger primary engine but its weights host is usually
# unreachable from sandboxes; try quickly, fall back to ocr_dual.py's
# tesseract psm 6 / psm 4 / inverted-threshold trio and SAY SO in PROGRESS.md.
python3 -c "import paddleocr" 2>/dev/null || note "PaddleOCR not installed \
(expected); dual-engine substitute is scripts/ocr_dual.py"

# --- OMP discipline: mandatory or tesseract spawns spinning orphans ---
grep -q OMP_THREAD_LIMIT ~/.bashrc 2>/dev/null \
  || echo 'export OMP_THREAD_LIMIT=1' >> ~/.bashrc
export OMP_THREAD_LIMIT=1

# --- epubcheck: the store-conformance gate qa_epub.py cannot replace ---
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

# --- smoke test ---
python3 tests/run_tests.py >>"$REPORT" 2>&1 \
  && note "checker regression tests: green" \
  || note "CHECKER REGRESSION TESTS FAILED — fix before translating"
note "setup done; anything above marked FAILED goes in PROGRESS.md"
