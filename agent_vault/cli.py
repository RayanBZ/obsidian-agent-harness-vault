from __future__ import annotations

import argparse
import json
from pathlib import Path

from .claude_runner import ClaudeRunner
from .config import load_config
from .ingest import ingest_paths
from .prompts import build_prompt
from .router import route_task
from .session import create_session
from .utils import atomic_write_text, print_json
from .validators import validate_vault


def cmd_doctor(args: argparse.Namespace) -> int:
    checks = validate_vault(args.vault)
    payload = [
        {
            "name": c.name,
            "ok": c.ok,
            "severity": c.severity,
            "detail": c.detail,
            "remediation": c.remediation,
        }
        for c in checks
    ]
    print_json(payload)
    return 0


def cmd_route(args: argparse.Namespace) -> int:
    route = route_task(args.task)
    print_json(route.__dict__)
    return 0


def run_mode(args: argparse.Namespace, mode: str) -> int:
    load_config(args.vault)

    route = route_task(args.task)
    session = create_session(args.vault, mode, args.task)

    prompt = build_prompt(args.task, route, mode, args.agent_depth)

    atomic_write_text(session.prompts / "primary-prompt.md", prompt)
    atomic_write_text(session.root / "route.json", json.dumps(route.__dict__, indent=2))

    ingest_manifest = ingest_paths([Path(p) for p in args.paths], root=args.vault)
    atomic_write_text(session.root / "ingest-manifest.json", json.dumps(ingest_manifest, indent=2))

    if args.dry_run:
        print("Dry run complete.")
        print(session.root)
        return 0

    runner = ClaudeRunner(cwd=args.vault)
    result = runner.run_prompt(prompt)

    atomic_write_text(session.outputs / "claude-output.md", result.stdout)

    print(result.stdout)

    if result.stderr:
        print(result.stderr)

    return result.returncode


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="agent-vault")
    parser.add_argument("--vault", type=Path, default=Path.cwd())

    sub = parser.add_subparsers(dest="command", required=True)

    doctor = sub.add_parser("doctor")
    doctor.set_defaults(func=cmd_doctor)

    route = sub.add_parser("route")
    route.add_argument("task")
    route.set_defaults(func=cmd_route)

    for name in ["run", "prd", "dev", "review"]:
        p = sub.add_parser(name)
        p.add_argument("task")
        p.add_argument("paths", nargs="*")
        p.add_argument("--agent-depth", default="standard")
        p.add_argument("--dry-run", action="store_true")
        p.set_defaults(func=lambda a, mode=name: run_mode(a, mode))

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)
