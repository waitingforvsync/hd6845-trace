#!/bin/bash
# Start or resume work on a claimed package in a worktree of its own:   tools/newwork.sh PREFIX [DIR]
# DIR defaults to a sibling directory hd6845-trace-PREFIX. Only for a package you hold the claim
# for. Use one worktree per agent: several agents in one working tree overwrite each other.
#   - DIR already a worktree (the next round of a loop): merges origin/main into it and reuses it.
#   - your branch PREFIX exists (merged or not, here or on origin): a worktree on it, origin/main
#     merged in, so you carry on from where you were.
#   - otherwise: a new branch PREFIX from origin/main.
# Links cache/ and .venv/ from this checkout (not in git; cache/ is about 10 GB) and pushes the branch.
cd "$(dirname "$0")/.." || exit 1
p="$1"; [ -n "$p" ] || { echo "usage: tools/newwork.sh PREFIX [DIR]"; exit 2; }
git fetch -q origin || exit 1
claim=$(git show "origin/main:claims/$p.md" 2>/dev/null) \
  || { echo "newwork: $p is not claimed on origin/main; run tools/claim.py take first"; exit 2; }
owner=$(printf '%s\n' "$claim" | sed -n 's/^| Who | \(.*\) |$/\1/p')
me=$(gh api user -q .login 2>/dev/null || git config user.name)
[ "$owner" = "$me" ] || { echo "newwork: $p is claimed by $owner, not by you ($me)"; exit 2; }
dir="${2:-$(cd .. && pwd)/hd6845-trace-$p}"

if [ -e "$dir/.git" ]; then
  (cd "$dir" && git merge -q --no-edit origin/main) || { echo "newwork: merging origin/main into $dir needs resolving there"; exit 1; }
  echo "newwork: reusing $dir (origin/main merged in)"; exit 0
fi
if git rev-parse -q --verify "refs/heads/$p" >/dev/null; then
  git worktree add -q "$dir" "$p" || exit 1
elif git rev-parse -q --verify "origin/$p" >/dev/null; then
  git worktree add -q -b "$p" "$dir" "origin/$p" || exit 1
else
  git worktree add -q -b "$p" "$dir" origin/main || exit 1
fi
[ -e "$dir/cache" ] || ln -s "$PWD/cache" "$dir/cache"
[ -e "$dir/.venv" ] || ln -s "$PWD/.venv" "$dir/.venv"
(cd "$dir" && git merge -q --no-edit origin/main) || { echo "newwork: merging origin/main into $dir needs resolving there"; exit 1; }
(cd "$dir" && git push -q -u origin "$p") && echo "newwork: $dir on branch $p (pushed)"
