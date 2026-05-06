from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


class AgentVaultError(Exception):
    """Base exception with user-facing remediation text."""

    def __init__(self, message: str, *, remediation: Optional[str] = None, code: str = "AGENT_VAULT_ERROR"):
        super().__init__(message)
        self.message = message
        self.remediation = remediation
        self.code = code

    def to_dict(self) -> dict:
        return {
            "ok": False,
            "code": self.code,
            "message": self.message,
            "remediation": self.remediation,
        }


@dataclass
class CheckResult:
    name: str
    ok: bool
    severity: str = "error"
    detail: str = ""
    remediation: str = ""

    def status_text(self) -> str:
        if self.ok:
            return "PASS"
        return "WARN" if self.severity == "warning" else "FAIL"
