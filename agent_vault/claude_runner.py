from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path

from .errors import AgentVaultError
from .utils import command_exists


@dataclass
class ClaudeResult:
    returncode: int
    stdout: str
    stderr: str


class ClaudeRunner:
    def __init__(self, *, cwd: Path):
        self.cwd = cwd

    def ensure_available(self) -> None:
        if not command_exists("claude"):
            raise AgentVaultError(
                "Claude CLI was not found on PATH.",
                remediation="Install Claude Code and ensure the `claude` executable is available.",
                code="CLAUDE_NOT_FOUND",
            )

    def run_prompt(self, prompt: str) -> ClaudeResult:
        self.ensure_available()

        proc = subprocess.run(
            ["claude", "-p", prompt],
            cwd=str(self.cwd),
            capture_output=True,
            text=True,
        )

        return ClaudeResult(
            returncode=proc.returncode,
            stdout=proc.stdout,
            stderr=proc.stderr,
        )
