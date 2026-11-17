# Handoffs

One file per merge of a package's work, `PREFIX-<time>.md`, written by `tools/claim.py done`
and pushed straight to main: the tracer's proposals for the coordinator's files (master list
status, Re-read items, ambiguities, corrections to other blocks' notes, floor plan). The
coordinator applies each and removes the file (`tools/claim.py handoffs` lists them). Claims
are separate (`claims/`): a tracer keeps or releases the claim when writing the handoff, so
nobody waits for the coordinator. How work is shared: `notes/workflow.md`.
