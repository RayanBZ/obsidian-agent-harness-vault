$Vault = "$env:USERPROFILE\Documents\Obsidian\obsidian-agent-vault"

# Validate vault structure
agent-vault --vault $Vault doctor

# Validate from current folder as vault root
agent-vault --vault . doctor

# Run doctor after adding skill files / MOCs
agent-vault --vault $Vault doctor --repair
