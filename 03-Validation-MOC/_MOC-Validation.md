# Validation — Map of Content

> Knowledge hub for test plans, security reviews, and coverage analysis.
> Managed by the Validation Lead. Workers (QA Engineer, Security Reviewer) atomize their outputs here.

## Team

- **Lead**: Validation Lead (claude-opus-4-6) — test strategy, delegates validation tasks
- **QA Engineer** (claude-sonnet-4-6) — test cases, regression, automation
- **Security Reviewer** (claude-sonnet-4-6) — threat models, auth, OWASP compliance

## Active Artifacts

### Test Plans
- [[test-plans/|Test Plans]] — test suites, regression matrices, edge cases

### Security Reports
- [[security-reports/|Security Reports]] — threat models, vulnerability assessments, pen test results

### Coverage Maps
- [[coverage-maps/|Coverage Maps]] — code coverage, feature coverage, risk heat maps

## Atomization Rules

Every artifact created by a Validation worker must:
1. Be a single atomic note (one test plan, one threat model, one coverage report)
2. Include YAML frontmatter with `created-by`, `date`, `status`, `severity`, `links`
3. Link back to this MOC via `[[03-Validation-MOC/_MOC-Validation]]`
4. Reference the engineering artifact being validated from `[[02-Engineering-MOC/]]`

## Domain Boundaries

| Path | QA Engineer | Security Reviewer |
|---|---|---|
| `03-Validation-MOC/test-plans/` | read + write | read only |
| `03-Validation-MOC/security-reports/` | read only | read + write |
| `03-Validation-MOC/coverage-maps/` | read + write | read + write |
| `02-Engineering-MOC/` | read only | read only |
| `apps/` | read only | read only |

## Feedback Loop

When validation finds issues:
1. Validation Lead reports to Orchestrator with severity + affected domain
2. Orchestrator routes back to Engineering Lead
3. Engineering workers fix within their domain boundaries
4. Validation re-tests — cycle continues until pass

---
*This MOC is maintained by the Validation Lead. Workers contribute atomic notes to subfolders.*
