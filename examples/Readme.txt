####Example Startup####

# Clone the private repo
git clone https://github.com/RayanBZ/obsidian-agent-harness-vault.git
cd obsidian-agent-harness-vault

# Create and activate a virtual environment
py -3.11 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1

# Install locally as editable package
python -m pip install --upgrade pip
pip install -e .

# Confirm CLI is available
agent-vault --help
  
$Vault = "$env:USERPROFILE\Documents\Obsidian\obsidian-agent-vault"
agent-vault --vault $Vault doctor
agent-vault --vault $Vault prd "Create a PRD for Agent Vault v0.2 with better ingest, YAML routing, and GitHub review support" --agent-depth deep --dry-run
explorer "$Vault\05-Sessions"


###Helpful One Liners###

# Run a dry-run PRD and then open the latest session
agent-vault --vault $Vault prd "Create a PRD for session replay support" --agent-depth deep --dry-run; Get-ChildItem "$Vault\05-Sessions" -Directory | Sort LastWriteTime -Descending | Select -First 1 | Invoke-Item

# Validate, route, then dry-run a dev task
agent-vault --vault $Vault doctor; agent-vault --vault $Vault route "Implement configurable routing"; agent-vault --vault $Vault dev "Implement configurable routing from multi-team-config.yaml" --agent-depth deep --dry-run

# Review the harness and open generated session folder
agent-vault --vault $Vault review "Review this codebase for MVP release readiness" . --agent-depth max --dry-run; explorer "$Vault\05-Sessions"
