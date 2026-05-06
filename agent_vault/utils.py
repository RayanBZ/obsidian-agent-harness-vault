from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def slugify(text: str, *, max_len: int = 64) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    if not text:
        text = "task"
    return text[:max_len].strip("-") or "task"


def atomic_write_text(path: Path, text: str, *, encoding: str = "utf-8") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding=encoding)
    os.replace(tmp, path)


def append_jsonl(path: Path, obj: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(obj, ensure_ascii=False, default=str) + "\n")


def safe_relative(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve())).replace("\\", "/")
    except Exception:
        return str(path)


def sha256_file(path: Path, *, max_bytes: int | None = None) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        remaining = max_bytes
        while True:
            chunk_size = 1024 * 1024
            if remaining is not None:
                if remaining <= 0:
                    break
                chunk_size = min(chunk_size, remaining)
            b = f.read(chunk_size)
            if not b:
                break
            h.update(b)
            if remaining is not None:
                remaining -= len(b)
    return h.hexdigest()


def is_probably_text(path: Path, sample_size: int = 4096) -> bool:
    text_exts = {
        ".txt", ".md", ".markdown", ".py", ".js", ".jsx", ".ts", ".tsx", ".json", ".yaml", ".yml",
        ".toml", ".ini", ".cfg", ".css", ".scss", ".html", ".xml", ".csv", ".sql", ".sh", ".ps1",
        ".bat", ".dockerfile", ".env", ".gitignore", ".lua", ".go", ".rs", ".java", ".c", ".cpp", ".h",
    }
    if path.suffix.lower() in text_exts or path.name.lower() in {"dockerfile", "makefile", "readme", "license"}:
        return True
    try:
        data = path.read_bytes()[:sample_size]
    except Exception:
        return False
    if not data:
        return True
    if b"\x00" in data:
        return False
    try:
        data.decode("utf-8")
        return True
    except UnicodeDecodeError:
        return False


def read_text_sample(path: Path, *, max_chars: int = 12000) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        if len(text) > max_chars:
            return text[:max_chars] + "\n\n[TRUNCATED BY AGENT-VAULT INGEST]"
        return text
    except Exception as exc:
        return f"[UNREADABLE TEXT FILE: {type(exc).__name__}: {exc}]"


def command_exists(name: str) -> bool:
    return shutil.which(name) is not None


def format_exception(exc: BaseException) -> str:
    return f"{type(exc).__name__}: {exc}"


def normalize_agent_name(name: str) -> str:
    return slugify(name.replace("_", "-").replace(" ", "-"), max_len=80)


def truncate(text: str, max_chars: int = 24000) -> str:
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "\n\n[TRUNCATED]"


def print_json(obj: Any) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False, default=str))
