# Obsidian Router Skill

## Purpose
Route data through the Obsidian knowledge graph using MOC (Map of Content) nodes as routing targets.

## Protocol

### 1. Identify the data type
- **Requirement** → `01-Planning-MOC/requirements/`
- **User Story** → `01-Planning-MOC/user-stories/`
- **Architecture Decision** → `02-Engineering-MOC/architecture/`
- **API Spec** → `02-Engineering-MOC/api-specs/`
- **Test Plan** → `03-Validation-MOC/test-plans/`
- **Security Report** → `03-Validation-MOC/security-reports/`

### 2. Check domain permissions
Verify your agent definition allows `upsert: true` for the target path.

### 3. Update the MOC
After routing data, update the relevant MOC to include a link to the new note.

### 4. Cross-link
Add wikilinks (`[[path/to/note]]`) to create graph edges across team boundaries.

## Naming Convention
- Format: `YYYY-MM-DD-slug-name.md`
- Lowercase, hyphen-separated
- YAML frontmatter required
