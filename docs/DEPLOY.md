# Windows Deployment Guide

This guide deploys a multi-agent Obsidian vault on Windows using Obsidian as the knowledge management backbone and Claude Code as the model/runtime interface.

## Prerequisites

| Software | Purpose |
|---|---|
| Node.js LTS | Claude Code runtime dependency |
| Python 3.10+ | Python CLI harness |
| Claude Code | Model/runtime interface |
| Obsidian | Knowledge management |
| Git | Version control |

## Install software

```powershell
winget install OpenJS.NodeJS.LTS
winget install Obsidian.Obsidian
winget install Git.Git
```

Install Claude Code using the current official installer for your environment.

Verify installation:

```powershell
node --version
python --version
claude --version
git --version
```

## Project setup

```powershell
mkdir "insert here"
cd "insert here"
git clone "insert here"
cd "insert here"
```

## Python harness setup

```powershell
py -3.11 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e .
```

## Environment variables

If your model runtime requires an API key, store it outside git:

```powershell
[Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "insert here", "User")
```

Never commit real API keys, local machine paths, runtime logs, or session transcripts.

## Open in Obsidian

1. Launch Obsidian.
2. Choose **Open folder as vault**.
3. Select the project root.
4. Start with `00-Orchestrator/_MOC-Orchestrator.md`.

## Validate the vault

```powershell
agent-vault --vault . doctor --repair
```

The doctor command validates `.pi/multi-team/multi-team-config.yaml`, agent persona files, skill files, expertise files, MOC files, root `CLAUDE.md`, runtime folders, and Claude CLI availability.

## Run a smoke test

```powershell
agent-vault --vault . route "Create a PRD for the ingestion workflow" --mode prd
agent-vault --vault . prd "Create a PRD for the ingestion workflow" --agent-depth deep --dry-run
agent-vault --vault . status
```

## Runtime folders

These folders are created or maintained by the harness:

```text
.pi/multi-team/sessions/
.pi/multi-team/logs/
05-Sessions/
```

Use `.gitkeep` files to keep empty structure in git. Do not commit real runtime logs.
