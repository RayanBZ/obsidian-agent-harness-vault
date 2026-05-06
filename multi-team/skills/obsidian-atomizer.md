# Obsidian Atomizer Skill

## Purpose
Break outputs into atomic notes for the Obsidian knowledge graph.

## Atomic Note Principles

### One concept per note
Each note captures exactly one idea, decision, or artifact.

### Frontmatter is mandatory
```yaml
---
created-by: [agent-name]
date: YYYY-MM-DD
status: draft | review | approved | archived
type: requirement | story | adr | api-spec | test-plan | security-report
priority: critical | high | medium | low
links: []
tags: []
---
```

### Link aggressively
- Link to parent MOC
- Link to related notes in same domain
- Cross-reference upstream/downstream notes in other domains
