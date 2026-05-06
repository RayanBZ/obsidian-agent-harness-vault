from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RouteResult:
    team: str
    lead: str
    workers: list[str]
    rationale: str


PLANNING_KEYWORDS = {
    "prd", "requirements", "roadmap", "persona", "ux", "feature", "scope", "planning",
}

ENGINEERING_KEYWORDS = {
    "build", "implement", "code", "api", "database", "frontend", "backend", "refactor", "deploy",
}

VALIDATION_KEYWORDS = {
    "review", "audit", "security", "test", "coverage", "validate", "release",
}


def route_task(task: str) -> RouteResult:
    lowered = task.lower()

    if any(k in lowered for k in PLANNING_KEYWORDS):
        return RouteResult(
            team="Planning",
            lead="Planning Lead",
            workers=["Product Manager", "UX Researcher"],
            rationale="Detected planning/PRD requirements language.",
        )

    if any(k in lowered for k in VALIDATION_KEYWORDS):
        return RouteResult(
            team="Validation",
            lead="Validation Lead",
            workers=["QA Engineer", "Security Reviewer"],
            rationale="Detected validation/review language.",
        )

    return RouteResult(
        team="Engineering",
        lead="Engineering Lead",
        workers=["Backend Dev", "Frontend Dev"],
        rationale="Defaulted to engineering workflow.",
    )
