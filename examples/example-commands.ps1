$Vault = "$env:USERPROFILE\Documents\Obsidian\obsidian-agent-vault"

agent-vault --vault $Vault doctor --repair
agent-vault --vault $Vault route "Build a PRD for an Obsidian agent harness"
agent-vault --vault $Vault prd "Create a PRD for a local Agent Vault harness" --agent-depth deep --dry-run
agent-vault --vault $Vault dev "Implement robust zip and folder ingest in the CLI" --agent-depth standard --dry-run
agent-vault --vault $Vault review "Review the vault skill files for consistency" "$Vault\.pi\multi-team\agents" --agent-depth deep --dry-run
agent-vault --vault $Vault status
