$Vault = "$env:USERPROFILE\Documents\Obsidian\obsidian-agent-vault"

# See which team would handle a PRD task
agent-vault --vault $Vault route "Create a PRD for the Obsidian Agent Harness Vault"

# See which team would handle engineering work
agent-vault --vault $Vault route "Implement zip ingest and session logging"

# See which team would handle review work
agent-vault --vault $Vault route "Review the codebase for security and release readiness"
