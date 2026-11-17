#!/usr/bin/env python3
"""The gate a package's branch must pass before it is pushed to main.

usage: tools/mergecheck.py PREFIX

Run it on the package's branch, in its working tree, after merging the shared
repository's main into the branch. It prints each check and ends with PASS or FAIL
(exit status 0 or 1). It checks:

 1. the branch contains the remote's current main (merge it first);
 2. the files changed against main are the tracer's own (trace/PREFIX*.txt,
    notes/blocks/PREFIX.md, floorplan.d/PREFIX.txt, tools/PREFIX_*.py), notes/signals.md,
    notes/operation.md, or other blocks' trace files (allowed, listed: each must be a fix
    of a clear error, in a commit of its own, and named in the handoff). Anything else
    (the coordinator's files, out/, claims/, shared tools, .claude/, .github/, trace/align.json)
    fails;
 3. the full extraction (no TRACE): 0 errors, 0 warnings;
 4. every net name is in the glossary, and no former name is left in the documents;
 5. notes/blocks/PREFIX.md has a "## Review" section that records a clean final round
    (a line containing "no findings" or "no issues");
 6. tools/unsure.py: nets that are joined only through uncertain items on the branch but
    not on main (listed; each must be written up in the block notes, not a failure);
 7. a no-op merge into main: main must fast-forward to the branch.
"""
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = os.path.join(ROOT, '.venv', 'bin', 'python')
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


def main():
    if len(sys.argv) != 2:
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
    own = re.compile(r'^(trace/%s[^/]*\.txt|notes/blocks/%s\.md|floorplan\.d/%s\.txt|tools/%s_[^/]*\.py)$'
                     % ((re.escape(p),) * 4))
    shared_ok = {'notes/signals.md', 'notes/operation.md'}
    others = [f for f in changed if f.startswith('trace/') and f.endswith('.txt') and not own.match(f)]
    bad = [f for f in changed if not own.match(f) and f not in shared_ok and f not in others]
    check(not bad, '2. only the package\'s own files, the glossary and operation.md changed',
          ('not allowed: ' + ' '.join(bad)) if bad else
          ('other blocks\' trace files changed (name each in the handoff): ' + ' '.join(others)) if others else '')

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
    rev = txt.split('## Review', 1)[1] if '## Review' in txt else ''
    rev = rev.split('\n## ', 1)[0]
    clean = re.search(r'no (findings|issues)', rev, re.I)
    check(bool(rev) and bool(clean), '5. notes/blocks/%s.md has a Review section ending in a clean round' % p)

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

    ff = git('merge-base', '--is-ancestor', main_rev, 'HEAD')[0] == 0
    check(ff, '7. main fast-forwards to this branch')

    print('\n' + ('PASS' if not fails else 'FAIL (%d)' % len(fails)))
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
