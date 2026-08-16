#!/bin/bash
# B10: rebuild data/zh/ch17.txt + ch18.txt from raw OCR backup, deterministically.
# strip -> assemble -> surgery -> apply_fixes.  Idempotent given the backup.
set -e
cd /home/user/winston
for p in $(seq 333 388); do cp data/txt_backup_b10/p0$p.txt data/txt/p0$p.txt; done
python3 scripts/recovery/b10_strip_furniture.py | grep -iE "NOT FOUND|NO HEADING" || true
python3 scripts/assemble.py ch17 333 363 --offset 44 >/dev/null
python3 scripts/assemble.py ch18 364 388 --offset 44 >/dev/null
python3 scripts/recovery/b10_surgery.py --apply | grep -E "WRITTEN|FAILED|MARKER"
python3 scripts/apply_fixes.py ch17 ch18 | tail -1
python3 scripts/recovery/b10_pagemap.py >/dev/null
echo "rebuild done"
