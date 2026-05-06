from __future__ import annotations

from .router import RouteResult


def build_prompt(task: str, route: RouteResult, mode: str, agent_depth: str) -> str:
    return f"""
You are operating inside the Obsidian Agent Harness Vault.

Task Mode: {mode}
Agent Depth: {agent_depth}
Primary Team: {route.team}
Lead Agent: {route.lead}
Workers: {', '.join(route.workers)}

Task:
{task}

Requirements:
- Follow the vault routing model.
- Produce implementation-ready output.
- Use structured markdown.
- Include risks, assumptions, and next steps.
- Do not hallucinate missing files or project structure.
""".strip()
