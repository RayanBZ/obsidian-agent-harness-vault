# Planning — Map of Content

> Knowledge hub for requirements, user stories, and sprint planning.
> Managed by the Planning Lead. Workers (Product Manager, UX Researcher) atomize their outputs here.

## Team

- **Lead**: Planning Lead (claude-opus-4-6) — decomposes planning tasks, delegates to workers
- **Product Manager** (claude-sonnet-4-6) — requirements, features, acceptance criteria
- **UX Researcher** (claude-sonnet-4-6) — personas, journeys, usability analysis

## Active Artifacts

### Requirements
- [[requirements/|All Requirements]] — feature specs, acceptance criteria, constraints

### User Stories
- [[user-stories/|All User Stories]] — atomized user stories with priority tags

### Sprint Plans
- [[sprint-plans/|All Sprint Plans]] — sprint-scoped work packages

## Atomization Rules

Every artifact created by a Planning worker must:
1. Be a single atomic note (one concept per file)
2. Include YAML frontmatter with `created-by`, `date`, `status`, `links`
3. Link back to this MOC via `[[01-Planning-MOC/_MOC-Planning]]`
4. Cross-link to related notes in other team MOCs where applicable

## Handoff Protocol

When planning artifacts are ready for engineering:
1. Planning Lead notifies Orchestrator
2. Orchestrator routes to Engineering Lead
3. Engineering Lead reads from `01-Planning-MOC/` (read-only for engineering)
4. Engineering creates implementation notes in `02-Engineering-MOC/`

---
*This MOC is maintained by the Planning Lead. Workers contribute atomic notes to subfolders.*
