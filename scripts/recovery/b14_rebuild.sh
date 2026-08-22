#!/bin/bash
# B14: rebuild data/zh/ch25.txt + ch26.txt + ch27.txt from raw OCR backup,
# deterministically.
# strip -> structure -> assemble -> surgery -> addfixes -> apply_fixes -> pagemap.
# Idempotent given the data/txt_backup_b14 raw-OCR backup.
set -e
cd /home/user/winston
export OMP_THREAD_LIMIT=1
for p in $(seq 553 581); do cp data/txt_backup_b14/p0$p.txt data/txt/p0$p.txt; done
python3 scripts/recovery/b14_structure.py >/dev/null
python3 scripts/recovery/b14_strip_furniture.py | grep -iE "NOT FOUND|AMBIG|removed|kept|stripped folios|heading" || true
python3 scripts/assemble.py ch25 553 569 --offset 44 >/dev/null
python3 scripts/assemble.py ch26 570 578 --offset 44 >/dev/null
python3 scripts/assemble.py ch27 579 581 --offset 44 >/dev/null
python3 scripts/recovery/b14_surgery.py --apply | grep -E "WRITTEN|FAILED|MARKER|times|OUT OF ORDER|sections in file"
python3 scripts/recovery/b14_addfixes.py >/dev/null
python3 scripts/apply_fixes.py ch25 ch26 ch27 | tail -3
python3 scripts/recovery/b14_pagemap.py
echo "rebuild done"
