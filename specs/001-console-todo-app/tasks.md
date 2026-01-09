# Tasks: Console Todo App

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md, contracts/internal_logic.md

**Tests**: Manual console verification as specified in the plan. No automated test framework requested for Phase I.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure using UV

- [x] T001 Initialize UV project with `uv init` and configure `pyproject.toml`
- [x] T002 Create directory structure `src/` as per plan.md
- [x] T003 [P] Create `README.md` with project description and run instructions

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [x] T004 Implement basic CLI loop and menu structure in `src/main.py`
- [x] T005 Setup in-memory task storage (list/dict) and global state in `src/main.py`
- [x] T006 Implement common error handling utilities and input validation functions in `src/main.py`

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Core Task Lifecycle (Priority: P1) 🎯 MVP

**Goal**: Create, view, and mark tasks as complete.

**Independent Test**: Add "Buy milk", view list (pending), mark complete, view list (complete).

### Implementation for User Story 1

- [x] T007 [US1] Implement `add_task` function with title/description validation in `src/main.py`
- [x] T008 [US1] Implement `view_tasks` function with [✓]/[ ] indicators in `src/main.py`
- [x] T009 [US1] Implement `mark_complete_toggle` function by ID in `src/main.py`
- [x] T010 [US1] Integrate US1 functions into the main CLI loop in `src/main.py`

**Checkpoint**: User Story 1 (MVP) is fully functional and testable.

---

## Phase 4: User Story 2 - Task Maintenance (Priority: P2)

**Goal**: Update and delete tasks.

**Independent Test**: Create task, update title, delete task, confirm list is empty.

### Implementation for User Story 2

- [x] T011 [US2] Implement `update_task` function (partial updates) in `src/main.py`
- [x] T012 [US2] Implement `delete_task` function with confirmation prompt in `src/main.py`
- [x] T013 [US2] Integrate US2 functions into the main CLI loop in `src/main.py`

**Checkpoint**: User Story 2 is functional and integrated.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Final refinements and validation

- [x] T014 [P] Ensure ISO-8601 timestamps are generated correctly for all tasks in `src/main.py`
- [x] T015 Perform manual end-to-end testing of all scenarios in `specs/001-console-todo-app/spec.md`
- [x] T016 Run `quickstart.md` validation (if exists)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Can start immediately.
- **Foundational (Phase 2)**: Depends on Setup.
- **User Stories (Phase 3+)**: Depend on Foundational (Phase 2).
- **Polish (Phase 5)**: Depends on all stories being complete.

### User Story Dependencies

- **US1 (P1)**: The MVP story.
- **US2 (P2)**: Can be implemented after US1.

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1 & 2.
2. Complete Phase 3 (US1).
3. Validate US1 core lifecycle.

### Incremental Delivery

1. Add US2 (Maintenance) after US1 is stable.
2. Final polish and validation.
