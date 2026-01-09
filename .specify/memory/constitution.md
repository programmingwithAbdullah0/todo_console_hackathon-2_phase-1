<!--
Sync Impact Report:
- Version change: null -> 1.0.0
- List of modified principles (old title -> new title if renamed):
  - [PRINCIPLE_1_NAME] -> I. Spec-First Development (MANDATORY)
  - [PRINCIPLE_2_NAME] -> II. Architecture Values (Statelessness & Cloud-Native)
  - [PRINCIPLE_3_NAME] -> III. Technology Stack Constraints
  - [PRINCIPLE_4_NAME] -> IV. Security & Privacy Standards
  - [PRINCIPLE_5_NAME] -> V. Code Quality & Testing Discipline
- Added sections:
  - Evolution Across Phases
  - Conflict Resolution & Success Criteria
- Templates requiring updates (✅ updated / ⚠ pending):
  - .specify/templates/plan-template.md (✅ updated)
  - .specify/templates/spec-template.md (✅ updated)
  - .specify/templates/tasks-template.md (✅ updated)
- Follow-up TODOs if any placeholders intentionally deferred: None
-->

# The Evolution of Todo Constitution

## Core Principles

### I. Spec-First Development (MANDATORY)
**Golden Rule**: No code shall be written manually. Every feature must follow the SDD pipeline: Constitution → Specify → Plan → Tasks → Implement.
- NO manual coding - All implementation via Claude Code.
- NO improvisation - Every line traces back to a validated task.
- NO shortcuts - Refine specs until AI generates correct output.
- Enforcement: All pull requests must reference Task IDs and Spec sections.

### II. Architecture Values (Statelessness & Cloud-Native)
- **Statelessness (Phase III+)**: NO localStorage/sessionStorage. State must persist to database (Neon PostgreSQL).
- **Cloud-Native (Phase IV+)**: Containerize everything (Docker), Kubernetes native (Minikube/Helm), 12-Factor App principles, mandatory health checks (`/health`, `/ready`).
- **Event-Driven (Phase V)**: Loose coupling via Kafka, async by default, idempotent handlers, event sourcing mindset.

### III. Technology Stack Constraints
- **Backend**: Python 3.13+ (FastAPI, SQLModel, UV).
- **Frontend**: TypeScript (Next.js 16+ App Router, Tailwind CSS).
- **Infrastructure**: Docker, Kubernetes, Helm, Kafka, Dapr.
- **Auth & AI**: Better Auth (JWT), OpenAI Agents SDK, Official MCP SDK.
- **Database**: Neon PostgreSQL.

### IV. Security & Privacy Standards
- **Authentication**: JWT tokens only (issued by Better Auth, validated by FastAPI).
- **Isolation**: Every query filtered by authenticated `user_id`. No global queries.
- **Privacy**: No PII in logs; SQL injection prevention (parameterized queries); XSS prevention (React auto-escaping).
- **Infrastructure**: HTTPS only in production; environment secrets (no committed keys).

### V. Code Quality & Testing Discipline
- **File Headers**: Every file MUST include Module name, Purpose, Phase, Task IDs, and Spec references.
- **Python**: Async by default, type hints everywhere, docstrings for public functions, JSON structured logging.
- **Testing**: Manual (Phase I-II), Unit/Integration/Contract (Phase III+), Health/Smoke/Load (Phase IV-V).
- **Performance**: API < 200ms p95, DB < 100ms.

## Evolution Across Phases

| Principle | Phase I | Phase II | Phase III | Phase IV | Phase V |
|-----------|---------|---------|-----------|-----------|---------|
| Spec-First Development | ✅ | ✅ | ✅ | ✅ | ✅ |
| Stateless Architecture | ❌ | ❌ | ✅ | ✅ | ✅ |
| Kubernetes Deployment | ❌ | ❌ | ❌ | ✅ | ✅ |
| Event-Driven (Kafka) | ❌ | ❌ | ❌ | ❌ | ✅ |
| Dapr Integration | ❌ | ❌ | ❌ | ❌ | ✅ |
| JWT Authentication | ❌ | ✅ | ✅ | ✅ | ✅ |
| MCP Tools | ❌ | ❌ | ✅ | ✅ | ✅ |

## Governance

### Conflict Resolution
When spec files conflict, follow this hierarchy:
**Constitution > Hackathon Requirements > Specify > Plan > Tasks**

### Success Criteria
The project is successful when:
1. All 5 phases are complete.
2. Every feature traces to specs (Task IDs in all code files).
3. AI agents generated 100% of code.
4. Deployed to cloud (Phase V).
5. No violations of this Constitution.

### Amendment Policy
- MAJOR: Version bump for principle removals or redefinitions.
- MINOR: New principle or material additions.
- PATCH: Formatting, wording, or typo fixes.

**Version**: 1.0.0 | **Ratified**: 2026-01-04 | **Last Amended**: 2026-01-04
