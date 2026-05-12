# Agent Vault Workflow

This project supports two complementary workflows:

1. Native Claude/Obsidian vault workflow — open the repo as an Obsidian vault, keep `.pi/multi-team/` as the agent brain, and use Claude Code from the project root.
2. Python CLI harness workflow — use `agent-vault` for deterministic routing, prompt construction, ingest manifests, session artifacts, and output routing.

The Python harness owns orchestration, file routing, subprocess calls, session logging, and fail-point outputs. Claude remains responsible for reasoning, writing, planning, coding, review, and synthesis.

## Recommended MVP loop

```powershell
$Vault = "insert here"
agent-vault --vault $Vault doctor --repair
agent-vault --vault $Vault route "Create a PRD for the ingestion workflow" --mode prd
agent-vault --vault $Vault prd "Create a PRD for the ingestion workflow" --agent-depth deep --dry-run
agent-vault --vault $Vault dev "Implement the next CLI improvement" --agent-depth standard
agent-vault --vault $Vault review "Review the package before release" . --agent-depth max --dry-run
```

## Agent Depth

- `quick` / `0`: Orchestrator + lead.
- `standard` / `1`: Orchestrator + lead + first worker.
- `deep` / `2`: Orchestrator + lead + all selected workers + lead synthesis.
- `max` / `3`: Primary team plus validation pass.

## Output routing

- PRDs: `01-Planning-MOC/requirements/`
- Dev plans: `02-Engineering-MOC/architecture/`
- Reviews: `03-Validation-MOC/coverage-maps/`
- Raw session artifacts: `05-Sessions/<session-id>/`
