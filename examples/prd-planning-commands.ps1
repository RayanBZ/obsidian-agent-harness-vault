$Vault = "$env:USERPROFILE\Documents\Obsidian\obsidian-agent-vault"

# Generate a PRD with standard depth
agent-vault --vault $Vault prd "Create a PRD for a local multi-agent Obsidian harness" --agent-depth standard

# Deep PRD pass
agent-vault --vault $Vault prd "Create a PRD for Agent Depth controls, including quick, standard, deep, and max modes" --agent-depth deep

# Dry-run PRD prompt/session artifacts without calling Claude
agent-vault --vault $Vault prd "Create a PRD for GitHub repo ingestion support" --agent-depth deep --dry-run

# PRD for a feature with explicit components
agent-vault --vault $Vault prd "Define the purpose, personas, MVP scope, success metrics, and UX flow for a review command that ingests codebases, zips, docs, and GitHub links" --agent-depth max
