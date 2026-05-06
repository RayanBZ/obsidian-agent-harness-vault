# Engineering — Map of Content

> Knowledge hub for architecture decisions, API specifications, and implementation patterns.
> Managed by the Engineering Lead. Workers (Frontend Dev, Backend Dev) atomize their outputs here.

## Team

- **Lead**: Engineering Lead (claude-opus-4-6) — architecture decisions, delegates implementation
- **Frontend Dev** (claude-sonnet-4-6) — UI components, layouts, client-side state
- **Backend Dev** (claude-sonnet-4-6) — APIs, databases, infrastructure

## Active Artifacts

### Architecture
- [[architecture/|Architecture Decisions]] — ADRs, system design, technical constraints

### API Specs
- [[api-specs/|API Specifications]] — endpoint definitions, schemas, contracts

### Mental Models
- [[mental-models/|Engineering Mental Models]] — accumulated technical knowledge per agent

## Atomization Rules

Every artifact created by an Engineering worker must:
1. Be a single atomic note (one component, one endpoint, one decision)
2. Include YAML frontmatter with `created-by`, `date`, `status`, `tech-stack`, `links`
3. Link back to this MOC via `[[02-Engineering-MOC/_MOC-Engineering]]`
4. Reference originating requirement from `[[01-Planning-MOC/]]` when applicable

## Domain Boundaries

| Path | Frontend Dev | Backend Dev |
|---|---|---|
| `apps/` | read + write + delete | read + write + delete |
| `02-Engineering-MOC/` | read + write | read + write |
| `01-Planning-MOC/` | read only | read only |
| `03-Validation-MOC/` | read only | read only |

Cross-domain writes are **REJECTED** at the harness level. This is how blast radius stays at zero.

## Handoff Protocol

When implementation is complete:
1. Engineering Lead notifies Orchestrator
2. Orchestrator routes to Validation Lead
3. Validation team reads from `02-Engineering-MOC/` and `apps/`
4. Test results written to `03-Validation-MOC/`

---
*This MOC is maintained by the Engineering Lead. Workers contribute atomic notes to subfolders.*
