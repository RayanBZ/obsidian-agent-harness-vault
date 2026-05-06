# List recent sessions
agent-vault --vault $Vault status

# Open sessions folder in Explorer
explorer "$Vault\05-Sessions"

# Open latest session folder manually
Get-ChildItem "$Vault\05-Sessions" -Directory | Sort-Object LastWriteTime -Descending | Select-Object -First 1 | Invoke-Item
