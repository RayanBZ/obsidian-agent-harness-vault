param(
  [string]$VaultPath = "$env:USERPROFILE\Documents\Obsidian\obsidian-agent-vault",
  [string]$VaultZip = ""
)

$ErrorActionPreference = "Stop"

Write-Host "Creating Python virtual environment..."
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\pip.exe install -e .

if ($VaultZip -ne "") {
  Write-Host "Initializing vault from zip: $VaultZip"
  .\.venv\Scripts\agent-vault.exe init --vault $VaultPath --from-zip $VaultZip
} else {
  Write-Host "No vault zip provided. Running doctor against: $VaultPath"
}

.\.venv\Scripts\agent-vault.exe --vault $VaultPath doctor --repair

Write-Host ""
Write-Host "Install complete. Activate with:"
Write-Host "  .\.venv\Scripts\Activate.ps1"
Write-Host "Then run:"
Write-Host "  agent-vault --vault `"$VaultPath`" route `"Build a PRD for the harness`""
