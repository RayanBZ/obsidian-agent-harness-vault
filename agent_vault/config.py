from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass
class VaultConfig:
    vault_root: Path
    config_path: Path
    raw: dict[str, Any]

    @property
    def orchestrator(self) -> dict[str, Any]:
        return self.raw.get("orchestrator", {})

    @property
    def teams(self) -> list[dict[str, Any]]:
        return self.raw.get("teams", [])


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Expected YAML mapping in {path}")
    return data


def discover_config(vault_root: Path) -> Path:
    candidates = [
        vault_root / "multi-team-config.yaml",
        vault_root / ".pi" / "multi-team" / "multi-team-config.yaml",
    ]
    for c in candidates:
        if c.exists():
            return c
    raise FileNotFoundError("Could not locate multi-team-config.yaml")


def load_config(vault_root: Path) -> VaultConfig:
    config_path = discover_config(vault_root)
    return VaultConfig(vault_root=vault_root, config_path=config_path, raw=load_yaml(config_path))
