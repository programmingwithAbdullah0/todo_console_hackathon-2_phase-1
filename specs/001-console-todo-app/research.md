# Research: Phase I - In-Memory Python Console Application

## Technical Context
- **Language**: Python 3.13+
- **Primary Dependencies**: UV (package manager), `datetime` (stdlib)
- **Storage**: In-memory `list` of `dict` objects
- **Interface**: Console / CLI
- **Phase Alignment**: Phase I (Simple, no external DB, no auth)

## Research Findings

### Decision: In-Memory Storage Pattern
- **Result**: Use a global `tasks` list and a `next_id` counter.
- **Rationale**: Matches the Phase I requirements for simplicity and avoids unnecessary abstraction before Phase III.
- **Alternatives considered**: Local JSON file (rejected as per "In-Memory" constraint), SQLite (rejected to stay within Phase I scope).

### Decision: Project Structure
- **Result**: Single file `src/main.py`.
- **Rationale**: Minimalist approach for a console app; easy to manage and test in primitive stages.
- **Alternatives considered**: Multi-module (rejected as over-engineered for ~200 lines).

### Decision: Input Validation
- **Result**: Manual stripping and length checks (1-200 chars for title).
- **Rationale**: Meets FR-001 and FR-008 without external validation libraries (keeping dependencies low).

## Dependencies & Best Practices
- **UV**: Use `uv init` for rapid setup.
- **Formatting**: Standard Python `f-strings` for console output.
- **Stability**: Catch non-integer ID inputs (FR-005/FR-007).
