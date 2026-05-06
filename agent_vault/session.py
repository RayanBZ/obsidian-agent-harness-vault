from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .utils import atomic_write_text, slugify, utc_now_iso


@dataclass
class SessionPaths:
    root: Path
    prompts: Path
    outputs: Path


def create_session(vault_root: Path, mode: str, task: str) -> SessionPaths:
    timestamp = utc_now_iso().replace(":", "-")
    slug = slugify(task)
    root = vault_root / "05-Sessions" / f"{timestamp}-{mode}-{slug}"
    prompts = root / "prompts"
    outputs = root / "outputs"

    prompts.mkdir(parents=True, exist_ok=True)
    outputs.mkdir(parents=True, exist_ok=True)

    atomic_write_text(root / "task.md", f"# Task\n\n{task}\n")

    return SessionPaths(root=root, prompts=prompts, outputs=outputs)
