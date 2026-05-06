from __future__ import annotations

from pathlib import Path

from .errors import CheckResult
from .utils import command_exists


REQUIRED_FOLDERS = [
    "00-Orchestrator",
    "01-Planning-MOC",
    "02-Engineering-MOC",
    "03-Validation-MOC",
    "05-Sessions",
]


def validate_vault(vault_root: Path) -> list[CheckResult]:
    checks: list[CheckResult] = []

    for folder in REQUIRED_FOLDERS:
        path = vault_root / folder
        checks.append(
            CheckResult(
                name=f"folder:{folder}",
                ok=path.exists(),
                severity="error",
                detail=str(path),
                remediation=f"Create missing folder: {path}",
            )
        )

    checks.append(
        CheckResult(
            name="claude-cli",
            ok=command_exists("claude"),
            severity="warning",
            detail="Checks if Claude CLI is available on PATH.",
            remediation="Install Claude Code and ensure `claude` is on PATH.",
        )
    )

    return checks
