#!/usr/bin/env python3
"""Claim a tracing package, so that everyone sees at once who is working where.

usage: tools/claim.py list
       tools/claim.py take PREFIX --region "x0-x1 x y0-y1[; ...]" --what "TEXT" [--overlap-ok] [--dry]
       tools/claim.py release PREFIX [--note "TEXT"] [--dry]
       tools/claim.py done PREFIX --merged COMMIT --handoff FILE [--continue] [--dry]
       tools/claim.py handoffs

`take` first pulls: it must be run in the main checkout, on branch main, and it
fast-forwards that checkout to the shared repository's main (and stops if it cannot), so
that you choose from the current master list and claims. It also refuses a prefix that
the master list on main does not name.

A claim is one file, claims/PREFIX.md, on the main branch of the shared repository. `take`
writes it and pushes it to main straight away, as a commit of its own, without touching
your working tree or your branch (it builds the commit with git plumbing on top of the
remote's main). Two people taking the same prefix at the same moment cannot both succeed:
the second push is rejected, the tool fetches again, sees the claim and stops.

`take` refuses a prefix that is already claimed, and refuses a region that overlaps an
active claim's region unless --overlap-ok is given. Use that only after reading the other
claim and its block notes and agreeing who draws which wires (wiring packages often cross
other regions; say in --what what you will and will not draw there).

`release` removes the claim. The coordinator releases claims when it merges the work;
release your own claim only if you abandon the package (say why with --note, and leave
notes that let the next person resume).

`done` is run after a merge into main (the /trace6845 command does this). It writes the
tracer's proposals for the coordinator's files (master list status, Re-read items,
ambiguities, corrections to other blocks' notes, floor plan) to handoffs/PREFIX-<time>.md, and
in the same commit either keeps the claim (--continue: the same person carries on with the
package, e.g. the next round of a loop) or releases it. The coordinator works through
handoffs/ (`handoffs` lists them) and removes each file once applied; nothing waits on that.
`take` of a package you already hold is a no-op, so a loop can call it every time.

`list` prints the active claims, with the date of the last commit on each claim's branch.

The tool needs write access to the shared repository (ask its owner). It finds the
shared repository's remote by its URL; set HD_CANON_REMOTE to override.
"""
import argparse
import datetime
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CANON_URL = 'waitingforvsync/hd6845-trace'
CLAIMS = 'claims'
HANDOFFS = 'handoffs'
PREFIX_RE = re.compile(r'^[a-z][a-z0-9_]*$')
REGION_RE = re.compile(r'(\d+)\s*-\s*(\d+)\s*x\s*(\d+)\s*-\s*(\d+)')


def git(*args, env=None, check=True, input=None):
    r = subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True,
                       env={**os.environ, **(env or {})}, input=input)
    if check and r.returncode:
        sys.exit('git %s failed:\n%s' % (' '.join(args), r.stderr.strip()))
    return r


def canon_remote():
    if os.environ.get('HD_CANON_REMOTE'):
        return os.environ['HD_CANON_REMOTE']
    for line in git('remote', '-v').stdout.splitlines():
        name, url = line.split()[:2]
        if CANON_URL in url:
            return name
    sys.exit('no remote points at %s; add one (git remote add origin '
             'https://github.com/%s.git) or set HD_CANON_REMOTE' % (CANON_URL, CANON_URL))


def fetch(remote):
    git('fetch', '-q', remote, '+refs/heads/*:refs/remotes/%s/*' % remote)
    return git('rev-parse', '%s/main' % remote).stdout.strip()


def claims_at(rev):
    """{prefix: text} of the claim files in commit rev."""
    r = git('ls-tree', '--name-only', rev, CLAIMS + '/', check=False)
    out = {}
    for path in r.stdout.split():
        name = os.path.basename(path)
        if name.endswith('.md') and name != 'README.md':
            out[name[:-3]] = git('show', '%s:%s' % (rev, path)).stdout
    return out


def field(text, name):
    m = re.search(r'^\|\s*%s\s*\|\s*(.*?)\s*\|\s*$' % re.escape(name), text, re.M)
    return m.group(1) if m else ''


def regions(text):
    return [tuple(int(v) for v in m.groups()) for m in REGION_RE.finditer(text)]


def overlaps(a, b):
    ax0, ax1, ay0, ay1 = a
    bx0, bx1, by0, by1 = b
    return ax0 < bx1 and bx0 < ax1 and ay0 < by1 and by0 < ay1


def who():
    r = subprocess.run(['gh', 'api', 'user', '-q', '.login'], capture_output=True, text=True)
    if r.returncode == 0 and r.stdout.strip():
        return r.stdout.strip()
    return git('config', 'user.name', check=False).stdout.strip() or 'unknown'


def commit_change(remote, base, path, content, message):
    """Commit on top of base: path set to content (or removed if content is None). path may be a
    list of (path, content) pairs, all changed in the one commit."""
    changes = path if isinstance(path, list) else [(path, content)]
    with tempfile.TemporaryDirectory() as d:
        env = {'GIT_INDEX_FILE': os.path.join(d, 'index')}
        git('read-tree', base, env=env)
        for p, c in changes:
            if c is None:
                git('update-index', '--force-remove', p, env=env)
            else:
                blob = git('hash-object', '-w', '--stdin', input=c).stdout.strip()
                git('update-index', '--add', '--cacheinfo', '100644,%s,%s' % (blob, p), env=env)
        tree = git('write-tree', env=env).stdout.strip()
    return git('commit-tree', tree, '-p', base, '-m', message).stdout.strip()


def push(remote, commit):
    r = git('push', '-q', remote, '%s:refs/heads/main' % commit, check=False)
    if r.returncode == 0:
        return 'ok'
    err = r.stderr
    if 'non-fast-forward' in err or 'fetch first' in err or 'rejected' in err and 'denied' not in err:
        return 'race'
    if '403' in err or 'denied' in err.lower() or 'permission' in err.lower():
        sys.exit('push to main refused: you need write access to the shared repository '
                 '(ask its owner).\n' + err.strip())
    sys.exit('push failed:\n' + err.strip())


def cmd_list(a):
    remote = canon_remote()
    base = fetch(remote)
    cl = claims_at(base)
    if not cl:
        print('no active claims')
        return
    for p, text in sorted(cl.items()):
        br = field(text, 'Branch') or p
        last = git('log', '-1', '--format=%cd', '--date=format:%Y-%m-%d %H:%M',
                   '%s/%s' % (remote, br), check=False).stdout.strip() or 'no branch yet'
        print('%-8s %-14s claimed %s  last commit %s  status %s\n         region %s\n         %s' % (
            p, field(text, 'Who'), field(text, 'Claimed'), last, field(text, 'Status') or 'tracing',
            field(text, 'Region'), field(text, 'What')))


def pull_main(remote):
    """Fast-forward the local main checkout to the remote's main, or stop."""
    br = git('symbolic-ref', '--short', 'HEAD', check=False).stdout.strip()
    if br != 'main':
        sys.exit('claim from the main checkout, on branch main (you are on %r): '
                 'git switch main, then run this again' % br)
    r = git('pull', '-q', '--ff-only', remote, 'main', check=False)
    if r.returncode:
        sys.exit('could not pull %s/main into this checkout (fast-forward only):\n%s\n'
                 'Commit or move aside local changes to main, then run this again.' % (remote, r.stderr.strip()))
    print('pulled %s/main: %s' % (remote, git('log', '-1', '--format=%h %s').stdout.strip()))


def on_master_list(prefix, rev):
    """True if notes/work-packages.md at rev names the prefix: `p`, or within `a1`-`a6`."""
    txt = git('show', '%s:notes/work-packages.md' % rev, check=False).stdout
    if re.search(r'`%s`' % re.escape(prefix), txt):
        return True
    m = re.match(r'^([a-z_]+?)(\d+)$', prefix)
    if m:
        for lo, hi in re.findall(r'`%s(\d+)`\s*(?:-|\.\.\.|to)\s*`%s(\d+)`' % ((re.escape(m.group(1)),) * 2), txt):
            if int(lo) <= int(m.group(2)) <= int(hi):
                return True
        if re.search(r'`%s(\d+)`, `' % re.escape(m.group(1)), txt) and re.search(r'`%s`' % re.escape(prefix), txt):
            return True
    return False


def cmd_take(a):
    if not PREFIX_RE.match(a.prefix):
        sys.exit('prefix: lower case letters, digits, underscore; starting with a letter')
    mine = regions(a.region)
    if not mine:
        sys.exit('--region: give at least one "x0-x1 x y0-y1" in metal-shot pixels')
    remote = canon_remote()
    if not a.dry:
        pull_main(remote)
    me = who()
    now = datetime.datetime.now().astimezone().strftime('%Y-%m-%d %H:%M %z')
    text = ('# Claim: %s\n\nWritten by `tools/claim.py take`. Removed by the coordinator when the work is\n'
            'merged, or by `tools/claim.py release` if it is abandoned.\n\n'
            '| Field | Value |\n|---|---|\n| Who | %s |\n| Claimed | %s |\n| Region | %s |\n'
            '| What | %s |\n| Branch | %s |\n| Status | tracing |\n') % (a.prefix, me, now, a.region, a.what, a.branch or a.prefix)
    for attempt in range(5):
        base = fetch(remote)
        cl = claims_at(base)
        if a.prefix in cl:
            if field(cl[a.prefix], 'Who') == me and not field(cl[a.prefix], 'Status').startswith('merged'):
                print('you already hold %s: carry on (tools/newwork.sh %s reuses your worktree)' % (a.prefix, a.prefix))
                return
            sys.exit('%s is already claimed:\n%s' % (a.prefix, cl[a.prefix]))
        if not on_master_list(a.prefix, base):
            sys.exit('%s is not on the master list (notes/work-packages.md on main); '
                     'ask the coordinator to add it' % a.prefix)
        clash = [(p, field(t, 'Who'), field(t, 'Region')) for p, t in cl.items()
                 if not field(t, 'Status').startswith('merged') and any(overlaps(r, s) for r in mine for s in regions(field(t, 'Region')))]
        if clash and not a.overlap_ok:
            sys.exit('the region overlaps active claims:\n' +
                     '\n'.join('  %s (%s): %s' % c for c in clash) +
                     '\nRead those claims and their notes; if you can divide the work, '
                     'say how in --what and add --overlap-ok.')
        c = commit_change(remote, base, '%s/%s.md' % (CLAIMS, a.prefix), text,
                          'Claim %s: %s (%s)' % (a.prefix, a.what, me))
        if a.dry:
            print('dry run: would push this claim to %s/main:\n\n%s' % (remote, text))
            return
        res = push(remote, c)
        if res == 'ok':
            print('claimed %s; pushed to %s/main as %s' % (a.prefix, remote, c[:7]))
            print('next: tools/newwork.sh %s   (or: git switch -c %s %s/main)' % (
                a.prefix, a.branch or a.prefix, remote))
            return
    sys.exit('main kept moving; try again')


def cmd_release(a):
    remote = canon_remote()
    for attempt in range(5):
        base = fetch(remote)
        cl = claims_at(base)
        if a.prefix not in cl:
            sys.exit('%s is not claimed' % a.prefix)
        msg = 'Release claim %s' % a.prefix + (': %s' % a.note if a.note else '')
        c = commit_change(remote, base, '%s/%s.md' % (CLAIMS, a.prefix), None, msg)
        if a.dry:
            print('dry run: would push "%s" to %s/main' % (msg, remote))
            return
        if push(remote, c) == 'ok':
            print('released %s (%s)' % (a.prefix, c[:7]))
            return
    sys.exit('main kept moving; try again')


def cmd_done(a):
    """After a merge to main: write the handoff for the coordinator to handoffs/, and either keep
    the claim (--continue: you carry on with the same package) or release it, in one commit."""
    remote = canon_remote()
    handoff = open(a.handoff).read().strip()
    me = who()
    now = datetime.datetime.now().astimezone()
    stamp = now.strftime('%Y-%m-%d %H:%M %z')
    for attempt in range(5):
        base = fetch(remote)
        cl = claims_at(base)
        if a.prefix not in cl:
            sys.exit('%s is not claimed' % a.prefix)
        if field(cl[a.prefix], 'Who') not in (me, ''):
            sys.exit('%s is claimed by %s, not by you (%s)' % (a.prefix, field(cl[a.prefix], 'Who'), me))
        if git('merge-base', '--is-ancestor', a.merged, base, check=False).returncode:
            sys.exit('%s is not on %s/main: merge first' % (a.merged, remote))
        hpath = '%s/%s-%s-%s.md' % (HANDOFFS, a.prefix, now.strftime('%Y%m%d-%H%M%S'), a.merged[:7])
        k = 2
        while git('cat-file', '-e', '%s:%s' % (base, hpath), check=False).returncode == 0:
            hpath = '%s/%s-%s-%s-%d.md' % (HANDOFFS, a.prefix, now.strftime('%Y%m%d-%H%M%S'), a.merged[:7], k)
            k += 1
        htext = ('# Handoff: %s\n\nWritten by `tools/claim.py done`. The coordinator applies it and removes this file.\n\n'
                 '| Field | Value |\n|---|---|\n| Who | %s |\n| Merged | %s |\n| Written | %s |\n| Continuing | %s |\n\n%s\n'
                 % (a.prefix, me, a.merged[:7], stamp, 'yes' if a.cont else 'no, claim released', handoff))
        changes = [(hpath, htext)]
        if a.cont:
            text = cl[a.prefix]
            status = 'tracing (part merged %s at %s)' % (a.merged[:7], stamp)
            text = re.sub(r'^\| Status \|.*$', '| Status | %s |' % status, text, flags=re.M) if '| Status |' in text \
                else text.rstrip('\n') + '\n| Status | %s |\n' % status
            changes.append(('%s/%s.md' % (CLAIMS, a.prefix), text))
            msg = 'Handoff %s (%s); claim kept, %s continues' % (a.prefix, a.merged[:7], me)
        else:
            changes.append(('%s/%s.md' % (CLAIMS, a.prefix), None))
            msg = 'Handoff %s (%s); claim released' % (a.prefix, a.merged[:7])
        c = commit_change(remote, base, changes, None, msg)
        if a.dry:
            print(htext)
            return
        if push(remote, c) == 'ok':
            print('%s: handoff written to %s; claim %s (%s)' % (a.prefix, hpath, 'kept' if a.cont else 'released', c[:7]))
            return
    sys.exit('main kept moving; try again')


def cmd_handoffs(a):
    remote = canon_remote()
    base = fetch(remote)
    names = git('ls-tree', '--name-only', base, HANDOFFS + '/', check=False).stdout.split()
    names = [n for n in names if n.endswith('.md') and not n.endswith('README.md')]
    if not names:
        print('no handoffs waiting')
    for n in names:
        t = git('show', '%s:%s' % (base, n)).stdout
        print('%-40s %-14s merged %s  %s' % (n, field(t, 'Who'), field(t, 'Merged'), field(t, 'Written')))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    sub.add_parser('list')
    t = sub.add_parser('take')
    t.add_argument('prefix')
    t.add_argument('--region', required=True)
    t.add_argument('--what', required=True)
    t.add_argument('--branch')
    t.add_argument('--overlap-ok', action='store_true')
    t.add_argument('--dry', action='store_true')
    r = sub.add_parser('release')
    r.add_argument('prefix')
    r.add_argument('--note')
    r.add_argument('--dry', action='store_true')
    d = sub.add_parser('done')
    d.add_argument('prefix')
    d.add_argument('--merged', required=True)
    d.add_argument('--handoff', required=True)
    d.add_argument('--continue', dest='cont', action='store_true')
    d.add_argument('--dry', action='store_true')
    sub.add_parser('handoffs')
    a = ap.parse_args()
    {'list': cmd_list, 'take': cmd_take, 'release': cmd_release, 'done': cmd_done, 'handoffs': cmd_handoffs}[a.cmd](a)


if __name__ == '__main__':
    main()
