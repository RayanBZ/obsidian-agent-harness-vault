# v0.2.0 Public Package Archive

This folder contains a public-safe copy of the v0.2.0 package.

Sanitization applied:

- personal identifiers removed
- API key examples replaced
- local machine paths replaced

The nested duplicate `obsidian-agent-vault.zip` was intentionally omitted from the sanitized archive to avoid reintroducing unsanitized duplicate content. The expanded vault files are included in the archive.

## Rebuild the zip

```powershell
$base64 = Get-Content dist\agent-vault-harness-v0.2-public-sanitized.zip.b64 -Raw
[IO.File]::WriteAllBytes("dist\agent-vault-harness-v0.2-public-sanitized.zip", [Convert]::FromBase64String($base64))
```

SHA256:

```text
c98f12bea4a410ffa1e4ced772c3ac6b30771a275b05b3cb199cb0799f43d65d
```
