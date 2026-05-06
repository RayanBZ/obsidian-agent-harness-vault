# Obsidian // Agent Harness Vault
!(/main/bsidian_Agent Harness Vault.png)
A local, Windows-friendly orchestration system that turns an Obsidian knowledge vault into an executable multi-agent workspace. The project combines a structured vault, agent skill files, routing MOCs, persistent mental-model notes, and a Python CLI named agent-vault. Instead of using Obsidian only as documentation, the harness treats the vault as the source of truth for agent roles, team boundaries, task routing, context, and output destinations.

The MVP focuses on a sequential, controlled workflow rather than immediately launching many agents in parallel. Users can run commands such as agent-vault prd, agent-vault dev, agent-vault review, and agent-vault route to initialize planning, development, code/document review, or general orchestration tasks. Agent Depth settings allow the user to choose how much reasoning and review effort the harness should apply, from quick routing to deeper validation passes.

The harness owns configuration loading, prompt construction, session logging, ingest manifests, Claude CLI subprocess calls, file routing, and fail-point reporting. Claude owns reasoning, writing, planning, reviewing, and synthesis. The goal is to create a repeatable local system where PRDs, code plans, reviews, logs, and outputs are automatically organized back into the Obsidian vault.

## Package: Agent Vault MVP Harness

Below are examples of use-cases for the Agent Harness structure - all logic is built and routed through Obsidian + Python, while Claude (or your choice of LLM) maintains the reasoning, writing, planning, and synthesis of your agent substructure. 

```powershell
agent-vault run "Analyze this project and create an implementation plan"
agent-vault prd "Create a PRD for a FiveM server diagnostics product" --agent-depth deep
agent-vault dev "Implement the agent-vault CLI MVP" --agent-depth standard
agent-vault review "Review this codebase for release readiness" .\some-folder --agent-depth deep
```

The harness deliberately owns:

- config loading
- route selection
- prompt construction
- Claude subprocess execution
- session logging
- ingest manifests
- output routing into Obsidian
- error handling and fail-point outputs

Claude owns reasoning, writing, reviewing, planning, and code/content generation.

## Windows install

From PowerShell:

```powershell
cd C:\path\to\agent-vault-mvp
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e .
```

If PowerShell blocks activation for this terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Initialize the vault

If you have the vault zip:

```powershell
agent-vault init --vault "$env:USERPROFILE\Documents\Obsidian\obsidian-agent-vault" --from-zip "$env:USERPROFILE\Downloads\obsidian-agent-vault_SkillFileFix.zip"
```

If the vault is already extracted:

```powershell
agent-vault --vault "$env:USERPROFILE\Documents\Obsidian\obsidian-agent-vault" doctor --repair
```

## Validate the vault

```powershell
agent-vault --vault "$env:USERPROFILE\Documents\Obsidian\obsidian-agent-vault" doctor --repair
```

`doctor` checks Python, vault folders, config YAML, agent files, skill files, mental-model folders, the accidental literal brace folder issue, and whether `claude` is on PATH.

## Agent depth

The MVP is sequential by design. It does **not** start with 9 parallel agents.

| Depth | Meaning | Typical stages |
|---|---|---|
| `quick` / `0` | light pass | Orchestrator + lead |
| `standard` / `1` | normal pass | Orchestrator + lead + one worker |
| `deep` / `2` | thorough pass | Orchestrator + lead + all selected workers + lead synthesis |
| `max` / `3` | highest MVP effort | Primary team plus validation pass |

Examples:

```powershell
agent-vault --vault . prd "Create a PRD for an Obsidian agent harness" --agent-depth deep
agent-vault --vault . dev "Build the Python CLI package" --agent-depth standard
agent-vault --vault . review "Review the release bundle" .\dist\agent-vault-mvp.zip --agent-depth max
```

## Commands

### `init`

Initializes or extracts a vault and creates runtime folders.

```powershell
agent-vault init --vault C:\Vaults\obsidian-agent-vault --from-zip C:\Downloads\obsidian-agent-vault_SkillFileFix.zip
```

### `doctor`

Validates vault readiness and Claude CLI availability.

```powershell
agent-vault --vault C:\Vaults\obsidian-agent-vault doctor --repair
```

### `route`

Shows deterministic routing without running agents.

```powershell
agent-vault route "Build an API and UI for task review"
```

### `run`

Generic orchestration command.

```powershell
agent-vault --vault C:\Vaults\obsidian-agent-vault run "Analyze the vault and propose next steps" --agent-depth standard
```

### `prd`

Planning/PRD workflow. It bakes in the required PRD components:

- Purpose / Goal
- User Personas
- Features
- Requirements & Scope
- Success Metrics
- UX / Design
- Risks, dependencies, assumptions, and implementation readiness

```powershell
agent-vault --vault C:\Vaults\obsidian-agent-vault prd "Create a PRD for a local multi-agent harness" --agent-depth deep
```

### `dev`

Development/coding workflow. It routes to Engineering and dynamically loads the vault's engineering lead/backend/frontend skill files.

```powershell
agent-vault --vault C:\Vaults\obsidian-agent-vault dev "Implement a safe ingest module for zip files and folders" --agent-depth deep
```

### `review`

Review workflow for codebases, documents, skill files, GitHub links, zip files, folders, and photo/image metadata.

```powershell
agent-vault --vault C:\Vaults\obsidian-agent-vault review "Review this for release readiness" .\my-project .\docs\spec.md --agent-depth max
```

For GitHub URLs, the default behavior is to record the link. To clone a public repo for review:

```powershell
agent-vault --vault C:\Vaults\obsidian-agent-vault review "Review this repo" https://github.com/org/repo --clone-links
```

### `ingest`

Creates an ingest manifest without running Claude.

```powershell
agent-vault --vault C:\Vaults\obsidian-agent-vault ingest .\my-project .\archive.zip .\diagram.png
```

### `status`

Lists recent sessions.

```powershell
agent-vault --vault C:\Vaults\obsidian-agent-vault status
```

## Dry run mode

Use `--dry-run` to generate session artifacts and prompts without calling Claude:

```powershell
agent-vault --vault . dev "Build the CLI" --agent-depth deep --dry-run
```

This is useful for debugging prompt construction, routing, ingest manifests, and session logging.

## Session outputs

Every run creates:

```text
05-Sessions/<timestamp-mode-task>/
  task.md
  route.json
  ingest-manifest.json
  ingest-summary.md
  conversation-log.jsonl
  prompts/
  outputs/
  final.md
```

The final output is also routed to the appropriate MOC area:

- PRDs: `01-Planning-MOC/requirements/`
- Dev plans: `02-Engineering-MOC/architecture/`
- Reviews: `03-Validation-MOC/coverage-maps/`

## Notes and limitations

- This MVP is sequential, not parallel.
- Photos/images are ingested as metadata only. Use a model/tooling path that supports image interpretation for visual analysis.
- GitHub URLs are recorded by default. Use `--clone-links` to clone public repositories when Git is available.
- Zip extraction uses path traversal protection and size/member limits.
- Claude execution requires the `claude` CLI to be on PATH. Without it, run `--dry-run` to generate prompts and artifacts.
