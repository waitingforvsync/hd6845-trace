#!/usr/bin/env python3
"""The gate a package's branch must pass before it is pushed to main.

usage: tools/mergecheck.py PREFIX
       tools/mergecheck.py --review-test FILE   (only check 5, on any notes file; changes nothing)

Run it on the package's branch, in its working tree, after merging the shared
repository's main into the branch. It prints each check and ends with PASS or FAIL
(exit status 0 or 1). It checks:

 1. the branch contains the remote's current main (merge it first);
 2. the files changed against main are the tracer's own (trace/PREFIX*.txt,
    notes/blocks/PREFIX.md, floorplan.d/PREFIX.txt, ports.d/PREFIX.txt, tools/PREFIX_*.py),
    notes/signals.md,
    notes/operation.md, or other blocks' trace files (allowed, listed: each must be a fix
    of a clear error, in a commit of its own, and named in the handoff). Anything else
    (the coordinator's files, out/, claims/, shared tools, .claude/, .github/, trace/align.json)
    fails. ports.d/PREFIX.txt, if the package has one, must parse (tools/ports.py); a
    package without one gets a reminder, not a failure;
 3. the full extraction (no TRACE): 0 errors, 0 warnings;
 4. every net name is in the glossary, and no former name is left in the documents;
 5. notes/blocks/PREFIX.md has a "## Review" section whose last verdict line is a clean one.
    A verdict line starts "Round N:". Clean is "Round N: no findings." (or "no issues."), or
    "Round N: no findings that change a connection." for a round whose confirmed findings
    were geometry only (notes/workflow.md, step 6); that second form also needs the proof in
    the section: the words "connections identical", which tools/sameconn.py prints. Notes
    with no "Round N:" line at all (written before that form was used) pass on the words
    "no findings" or "no issues" anywhere in the section, as before. A last verdict line
    that is not clean only warns while STRICT_LAST_ROUND is False (the older rule still
    passes it if "no findings" stands anywhere in the section);
 6. tools/unsure.py: nets that are joined only through uncertain items on the branch but
    not on main (listed; each must be written up in the block notes, not a failure);
 7. a no-op merge into main: main must fast-forward to the branch;
 8. costs/<git user.name>.json (tools/costs.py) is newer than the claim, and the models it
    records for this package are Claude Fable 5.2 only (the project's rule since 2026-11-17).
"""
import os
import re
import subprocess
import sys
import tempfile
import json
import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = os.path.join(ROOT, '.venv', 'bin', 'python')
FABLE = {'claude-fable-5-2'}
COORD = ('notes/work-packages.md', 'notes/ambiguities.md', 'notes/journal.md', 'floorplan.txt',
         'PLAN.md', 'CLAUDE.md', 'README.md')


def run(*cmd, cwd=ROOT, env=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, env={**os.environ, **(env or {})})
    return r.returncode, r.stdout, r.stderr


def git(*args, cwd=ROOT):
    return run('git', *args, cwd=cwd)


def canon():
    if os.environ.get('HD_CANON_REMOTE'):
        return os.environ['HD_CANON_REMOTE']
    for line in git('remote', '-v')[1].splitlines():
        if 'waitingforvsync/hd6845-trace' in line:
            return line.split()[0]
    sys.exit('no remote points at the shared repository')


def unsure_nets(cwd):
    rc, out, err = run(PY, 'tools/unsure.py', cwd=cwd, env={'TRACE': ''})
    return set(re.findall(r'^(\S+): \d+ pieces without the uncertain items', out, re.M))


# When True, check 5 fails if the last "Round N:" line of the Review section is not a clean one.
# Off for now: it is stricter than the gate was (which passed on "no findings" anywhere in the
# section), and the owner has not decided to enforce it. While off, that case only warns.
STRICT_LAST_ROUND = False

VERDICT = re.compile(r'^[\s*_>-]*Round\s+\d+[*_]*\s*:[*_]*\s*(.*?)[\s*_]*$', re.I | re.M)
CLEAN = re.compile(r'^no (findings|issues)\.?$', re.I)
CLEAN_CONN = re.compile(r'^no (findings|issues) that changes? a connection\.?$', re.I)


def review_verdict(txt):
    """(ok, why) for check 5, from the text of a block's notes."""
    if '## Review' not in txt:
        return False, 'no "## Review" section'
    rev = txt.split('## Review', 1)[1].split('\n## ', 1)[0]
    verdicts = VERDICT.findall(rev)
    if not verdicts:
        if re.search(r'no (findings|issues)', rev, re.I):
            return True, 'no "Round N:" verdict line; passed on the words "no findings" (the older form)'
        return False, 'no line "Round N: no findings."'
    last = verdicts[-1].strip()
    if CLEAN.match(last):
        return True, ''
    if CLEAN_CONN.match(last):
        if re.search(r'connections identical', rev, re.I):
            return True, 'last round: geometry-only findings, with tools/sameconn.py\'s "connections identical"'
        return False, ('the last round says "no findings that change a connection" but the section does not record '
                       'tools/sameconn.py\'s "connections identical" (run it on the package and on every file)')
    why = 'the last verdict line is not clean: "Round ...: %s"' % last[:80]
    if not STRICT_LAST_ROUND and re.search(r'no (findings|issues)', rev, re.I):
        return True, ('warning: ' + why + '; passed on the words "no findings" elsewhere in the section '
                      '(the older rule; STRICT_LAST_ROUND is off)')
    return False, why


def main():
    if len(sys.argv) == 3 and sys.argv[1] == '--review-test':
        ok, why = review_verdict(open(sys.argv[2]).read())
        print('%s  5. Review section ends in a clean round%s' % ('ok  ' if ok else 'FAIL', ('\n      ' + why) if why else ''))
        sys.exit(0 if ok else 1)
    if len(sys.argv) != 2 or sys.argv[1].startswith('-'):
        sys.exit(__doc__)
    p = sys.argv[1]
    remote = canon()
    fails = []

    def check(ok, what, detail=''):
        print('%s  %s%s' % ('ok  ' if ok else 'FAIL', what, ('\n      ' + detail) if detail else ''))
        if not ok:
            fails.append(what)

    git('fetch', '-q', remote)
    main_rev = git('rev-parse', '%s/main' % remote)[1].strip()
    contains = git('merge-base', '--is-ancestor', main_rev, 'HEAD')[0] == 0
    check(contains, '1. the branch contains %s/main (%s)' % (remote, main_rev[:7]),
          '' if contains else 'run: git merge %s/main, resolve, re-run' % remote)

    changed = git('diff', '--name-only', '%s...HEAD' % main_rev)[1].split()
    own = re.compile(r'^(trace/%s[^/]*\.txt|notes/blocks/%s\.md|floorplan\.d/%s\.txt|ports\.d/%s\.txt|tools/%s_[^/]*\.py)$'
                     % ((re.escape(p),) * 5))
    shared_ok = {'notes/signals.md', 'notes/operation.md'}
    others = [f for f in changed if f.startswith('trace/') and f.endswith('.txt') and not own.match(f)]
    bad = [f for f in changed if not own.match(f) and f not in shared_ok and f not in others
           and not re.match(r'^costs/[A-Za-z0-9_.-]+\.json$', f)]
    check(not bad, '2. only the package\'s own files, the glossary and operation.md changed',
          ('not allowed: ' + ' '.join(bad)) if bad else
          ('other blocks\' trace files changed (name each in the handoff): ' + ' '.join(others)) if others else '')

    if os.path.exists(os.path.join(ROOT, 'ports.d', p + '.txt')):
        rc, out, err = run(PY, 'tools/ports.py', '--prefix', p)
        perr = [l for l in out.splitlines() if l.startswith('ERROR') and ('ports.d/%s.txt:' % p) in l]
        check(not perr and bool(out), '2b. ports.d/%s.txt parses' % p, '\n      '.join(perr) or err.strip()[:300])
    else:
        print('info  2b. no ports.d/%s.txt: expected for new work (notes/tracing-guide.md, section 8)' % p)

    rc, out, err = run(PY, 'tools/netlist.py', env={'TRACE': ''})
    head = (out.splitlines() or [err.strip()])[0]
    m = re.search(r'(\d+) errors, (\d+) warnings', head)
    check(bool(m) and m.group(1) == '0' and m.group(2) == '0', '3. extraction: ' + head)

    rc, out, err = run(PY, 'tools/signals.py', env={'TRACE': ''})
    m = re.search(r'(\d+) not in notes/signals.md', out)
    check(bool(m) and m.group(1) == '0', '4a. glossary: ' + (out.splitlines() or [''])[0])
    rc, out, err = run(PY, 'tools/signals.py', '--docs')
    check('no former names left' in out, '4b. former names in the documents', out.strip()[:500])

    notes = os.path.join(ROOT, 'notes', 'blocks', p + '.md')
    txt = open(notes).read() if os.path.exists(notes) else ''
    ok, why = review_verdict(txt)
    check(ok, '5. notes/blocks/%s.md has a Review section ending in a clean round' % p, why)

    with tempfile.TemporaryDirectory(dir=os.path.join(ROOT, 'cache', 'scratch')) as d:
        wt = os.path.join(d, 'main')
        git('worktree', 'add', '-q', '--detach', wt, main_rev)
        os.symlink(os.path.join(ROOT, 'cache'), os.path.join(wt, 'cache'))
        os.symlink(os.path.join(ROOT, '.venv'), os.path.join(wt, '.venv'))
        before = unsure_nets(wt)
        os.remove(os.path.join(wt, 'cache'))
        os.remove(os.path.join(wt, '.venv'))
        git('worktree', 'remove', '--force', wt)
    after = unsure_nets(ROOT)
    new = sorted(after - before)
    print('info  6. nets newly joined only through uncertain items: %s' % (' '.join(new) or 'none'))
    if new:
        missing = [n for n in new if n not in txt]
        check(not missing, '6. each is written up in the block notes', ('not mentioned: ' + ' '.join(missing)) if missing else '')

    who = git('config', 'user.name')[1].strip()
    cpath = os.path.join(ROOT, 'costs', re.sub(r'[^A-Za-z0-9_.-]+', '_', who) + '.json')
    if not os.path.exists(cpath):
        check(False, '8. cost report costs/%s.json' % os.path.basename(cpath)[:-5], 'run: python3 tools/costs.py, and commit it')
    else:
        rec = json.load(open(cpath))
        pk = {k: v for k, v in rec.get('by_package', {}).items() if k == p or k.startswith(p + '_')}
        models = set()
        for v in pk.values():
            models |= set(v.get('models', {}))
        models -= {'<synthetic>'}
        claim = git('show', '%s:claims/%s.md' % (main_rev, p))[1]
        cm = re.search(r'^\|\s*Claimed\s*\|\s*(.*?)\s*\|', claim, re.M)
        fresh = True
        if cm:
            try:
                fresh = datetime.datetime.fromisoformat(rec['generated']) >= datetime.datetime.strptime(cm.group(1), '%Y-%m-%d %H:%M %z')
            except (KeyError, ValueError):
                pass
        check(fresh, '8a. cost report written after the claim', '' if fresh else 'run: python3 tools/costs.py again')
        ok = bool(models) and models <= FABLE
        check(ok, '8b. the package was traced with Claude Fable 5.2 (models seen: %s)' % (', '.join(sorted(models)) or 'none'),
              '' if ok else 'tracing here is done with claude-fable-5-2 only (.claude/settings.json; /trace6845 runs on it)')

    ff = git('merge-base', '--is-ancestor', main_rev, 'HEAD')[0] == 0
    check(ff, '7. main fast-forwards to this branch')

    print('\n' + ('PASS' if not fails else 'FAIL (%d)' % len(fails)))
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
