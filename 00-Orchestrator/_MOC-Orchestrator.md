# Orchestrator — Map of Content

> Master routing node for the multi-agent orchestration network.
> This MOC is the knowledge graph entry point. All incoming tasks are decomposed here and routed to the appropriate team MOC.

## Agent Network Status

- **Orchestrator**: Active — routes, delegates, tracks
- **Planning Team**: [[01-Planning-MOC/_MOC-Planning|Planning MOC]] — requirements, stories, sprints
- **Engineering Team**: [[02-Engineering-MOC/_MOC-Engineering|Engineering MOC]] — architecture, code, APIs
- **Validation Team**: [[03-Validation-MOC/_MOC-Validation|Validation MOC]] — testing, security, coverage

## Routing Rules

### Task Decomposition Protocol
1. Receive user message
2. Read conversation log (`{{CONVERSATION_LOG}}`) for full context
3. Classify task type → route to appropriate team lead
4. If task spans multiple domains → decompose into sub-tasks, one per team
5. Never execute directly — always delegate

### Domain Routing Table

| Signal Keywords | Route To | MOC Path |
|---|---|---|
| requirements, features, priorities, stories | Planning Lead | `01-Planning-MOC/` |
| build, implement, code, API, database, UI | Engineering Lead | `02-Engineering-MOC/` |
| test, validate, security, coverage, QA | Validation Lead | `03-Validation-MOC/` |
| cross-cutting, refactor, migration | All Leads (parallel) | Decompose first |

## Session Memory

- [[session-logs/|Session Logs]] — JSONL conversation archives
- [[orchestrator-mental-model.yaml|Mental Model]] — accumulated delegation patterns and team dynamics

## Shared Context

- [[04-Shared-Context/README|README]] — Project overview
- [[04-Shared-Context/CLAUDE|CLAUDE.md]] — Agent behavior guidelines
- [[04-Shared-Context/glossary|Glossary]] — Shared terminology

## Delegation History

Track which agents handled which tasks, success rates, and coordination friction points.
New entries appended after each session by the orchestrator's mental model update cycle.

---
*This MOC is maintained by the Orchestrator agent. It is the single source of truth for task routing.*
