#!/usr/bin/env python3
"""Reverse-lookup verified hanzi from glossary.json by English rendering.
Usage: gloss_hanzi.py "Zhou Enlai" "Qu Qiubai" ...
Prints, per query, every glossary entry (any section) whose 'en' or key matches.
"""
import sys, json, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
g=json.load(open(os.path.join(ROOT,'glossary.json')))
sections=[k for k in g if isinstance(g[k],dict) and k not in ('_about','book')]
for q in sys.argv[1:]:
    ql=q.lower()
    print('==== %s ====' % q)
    found=False
    for sec in sections:
        for hz,rec in g[sec].items():
            en=rec.get('en','') if isinstance(rec,dict) else ''
            if en.lower()==ql or ql in en.lower():
                found=True
                extra=[]
                for f in ('pinyin','status'):
                    if isinstance(rec,dict) and rec.get(f): extra.append(rec[f])
                print('  [%s] %s = %s  (%s)' % (sec, hz, en, ', '.join(extra)))
    if not found: print('  (no glossary match)')
