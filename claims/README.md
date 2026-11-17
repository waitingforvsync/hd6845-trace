# Claims

One file per package being traced, `PREFIX.md`, written by `tools/claim.py take` and
pushed straight to main, so that everyone sees who is working where. Do not edit these
files by hand. `tools/claim.py list` shows them with each branch's last commit.

A claim belongs to whoever is working: `tools/claim.py done` keeps it (`--continue`) or
releases it when they merge, and `tools/claim.py release` frees it if they stop. The
coordinator's part of a merge is in `handoffs/`, so nobody waits for it. How work is shared: `notes/workflow.md`.
