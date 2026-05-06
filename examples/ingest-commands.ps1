# Build an ingest manifest for a folder
agent-vault --vault $Vault ingest .\agent_vault

# Ingest multiple inputs
agent-vault --vault $Vault ingest .\agent_vault .\README.md .\pyproject.toml

# Ingest a vault zip
agent-vault --vault $Vault ingest "$env:USERPROFILE\Downloads\obsidian-agent-vault_SkillFileFix.zip"

# Ingest skill files only
agent-vault --vault $Vault ingest "$Vault\.pi\multi-team\agents"
