import json, sys
cid = sys.argv[1]
suffix = sys.argv[2] if len(sys.argv) > 2 else 'edits'
notes = [a['anchor'] for a in json.load(open('notes.json')).get(cid, [])]
figs = [f['before'] for f in json.load(open('figures.json')).get(cid, []) if 'before' in f]
olds = [ln[5:].rstrip('\n') for ln in open('edits/%s_%s.md' % (cid, suffix)) if ln.startswith('OLD: ')]
found = False
for o in olds:
    for a in notes:
        if a in o: print("NOTE anchor in OLD:", repr(a[:50]), "|", o[:45]); found = True
    for a in figs:
        if a in o: print("FIGURE anchor in OLD:", repr(a[:50]), "|", o[:45]); found = True
print("--- collisions found; ensure NEW preserves them or add a move ---" if found
      else "--- no anchor collisions ---")
