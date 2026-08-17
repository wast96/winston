#!/bin/bash
# B11: rebuild data/zh/ch19.txt + ch20.txt from raw OCR backup, deterministically.
# strip -> assemble -> surgery -> apply_fixes -> pagemap.  Idempotent given backup.
set -e
cd /home/user/winston
for p in $(seq 389 428); do cp data/txt_backup_b11/p0$p.txt data/txt/p0$p.txt; done
python3 scripts/recovery/b11_strip_furniture.py | grep -iE "NOT FOUND|NO HEADING|NOT MATCHED" || true
python3 scripts/assemble.py ch19 389 405 --offset 44 >/dev/null
python3 scripts/assemble.py ch20 406 428 --offset 44 >/dev/null
python3 scripts/recovery/b11_surgery.py --apply | grep -E "WRITTEN|FAILED|MARKER"
python3 scripts/apply_fixes.py ch19 ch20 | tail -2
python3 scripts/recovery/b11_pagemap.py >/dev/null
echo "rebuild done"
