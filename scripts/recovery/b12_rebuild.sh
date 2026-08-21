#!/bin/bash
# B12: rebuild data/zh/ch21.txt + ch22.txt from raw OCR backup, deterministically.
# strip -> assemble -> surgery -> apply_fixes -> pagemap.  Idempotent given the
# data/txt_backup_b12 raw-OCR backup.
set -e
cd /home/user/winston
export OMP_THREAD_LIMIT=1
for p in $(seq 429 484); do cp data/txt_backup_b12/p0$p.txt data/txt/p0$p.txt; done
python3 scripts/recovery/b12_strip_furniture.py | grep -iE "NOT FOUND|AMBIG|NO HEADING" || true
python3 scripts/assemble.py ch21 429 457 --offset 44 >/dev/null
python3 scripts/assemble.py ch22 458 484 --offset 44 >/dev/null
python3 scripts/recovery/b12_surgery.py --apply | grep -E "WRITTEN|FAILED|MARKER"
python3 scripts/recovery/b12_addfixes.py >/dev/null
python3 scripts/apply_fixes.py ch21 ch22 | tail -2
python3 scripts/recovery/b12_pagemap.py >/dev/null
echo "rebuild done"
