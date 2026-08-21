#!/bin/bash
# B13: rebuild data/zh/ch23.txt + ch24.txt from raw OCR backup, deterministically.
# strip -> structure -> assemble -> surgery -> addfixes -> apply_fixes -> pagemap.
# Idempotent given the data/txt_backup_b13 raw-OCR backup.
set -e
cd /home/user/winston
export OMP_THREAD_LIMIT=1
for p in $(seq 485 552); do cp data/txt_backup_b13/p0$p.txt data/txt/p0$p.txt; done
python3 scripts/recovery/b13_structure.py >/dev/null
python3 scripts/recovery/b13_strip_furniture.py | grep -iE "NOT FOUND|AMBIG|NO HEADING" || true
python3 scripts/assemble.py ch23 485 526 --offset 44 >/dev/null
python3 scripts/assemble.py ch24 527 552 --offset 44 >/dev/null
python3 scripts/recovery/b13_surgery.py --apply | grep -E "WRITTEN|FAILED|MARKER|times"
python3 scripts/recovery/b13_addfixes.py >/dev/null
python3 scripts/apply_fixes.py ch23 ch24 | tail -2
python3 scripts/recovery/b13_pagemap.py >/dev/null
echo "rebuild done"
