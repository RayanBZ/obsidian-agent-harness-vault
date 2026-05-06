# Review the repo itself
agent-vault --vault $Vault review "Review this harness codebase for reliability, Windows compatibility, and missing edge cases" . --agent-depth deep

# Review a specific Python module
agent-vault --vault $Vault review "Review the CLI implementation for argparse edge cases and bad failure modes" .\agent_vault\cli.py --agent-depth deep

# Review all agent skill files
agent-vault --vault $Vault review "Review all agent skill files for consistency, overlap, and missing engineering guidance" "$Vault\.pi\multi-team\agents" --agent-depth max

# Review a zip file
agent-vault --vault $Vault review "Review this packaged vault zip and identify files that should or should not be committed" "$env:USERPROFILE\Downloads\obsidian-agent-vault_SkillFileFix.zip" --agent-depth deep

# Review docs
agent-vault --vault $Vault review "Review the README for Windows setup clarity and missing install steps" .\README.md --agent-depth standard
