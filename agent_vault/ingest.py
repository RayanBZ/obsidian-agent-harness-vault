from __future__ import annotations

from pathlib import Path
from typing import Any

from .utils import is_probably_text, read_text_sample, safe_relative, sha256_file


def ingest_paths(paths: list[Path], *, root: Path) -> list[dict[str, Any]]:
    manifest: list[dict[str, Any]] = []

    for p in paths:
        if not p.exists():
            manifest.append({
                "path": str(p),
                "exists": False,
            })
            continue

        if p.is_dir():
            manifest.append({
                "path": safe_relative(p, root),
                "type": "directory",
            })
            continue

        entry: dict[str, Any] = {
            "path": safe_relative(p, root),
            "size": p.stat().st_size,
            "sha256": sha256_file(p, max_bytes=1024 * 1024),
        }

        if is_probably_text(p):
            entry["kind"] = "text"
            entry["sample"] = read_text_sample(p)
        else:
            entry["kind"] = "binary"

        manifest.append(entry)

    return manifest
