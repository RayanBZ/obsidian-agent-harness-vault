# Multi-Agent Orchestration Network

9-agent platform using Obsidian as the knowledge backbone.

## Architecture
- **Orchestrator** (claude-opus-4-6) — decomposes and routes tasks
- **3 Team Leads** (claude-opus-4-6) — delegate, never execute
- **6 Workers** (claude-sonnet-4-6) — execute within domain boundaries

## Teams
1. **Planning** — requirements, user stories, sprint plans
2. **Engineering** — architecture, APIs, implementation
3. **Validation** — testing, security, coverage
