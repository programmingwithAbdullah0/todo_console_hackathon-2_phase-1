# Feature Specification: Console Todo App

**Feature Branch**: `001-console-todo-app`
**Created**: 2026-01-04
**Status**: Draft
**Input**: User description: "The Evolution of Todo - Hackathon II. Phase I - In-Memory Python Console Application. Version: 1.0.0. Features: Add Task, Delete Task, Update Task, View Task List, Mark Task Complete/Pending. Core constraints: NO manual coding, in-memory, Python 3.13+, UV package manager, Console interface only."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Core Task Lifecycle (Priority: P1)

As a user, I want to create, view, and mark tasks as complete so that I can manage my daily work effectively.

**Why this priority**: This covers the core value proposition of the application. Without being able to add and see tasks, the app has no utility.

**Independent Test**: Can be fully tested by adding "Buy milk", viewing the list to see it marked as pending, then marking it complete and verifying the status change in the list.

**Acceptance Scenarios**:

1. **Given** no tasks exist, **When** I add task "Buy groceries" with description "Milk, eggs", **Then** task #1 is created with status "pending" and a success message is displayed.
2. **Given** task #1 exists and is "pending", **When** I mark task #1 as complete, **Then** its status changes to "complete" and the list displays it with a [✓] indicator.

---

### User Story 2 - Task Maintenance (Priority: P2)

As a user, I want to update and delete tasks so that I can keep my list accurate as requirements change or tasks become irrelevant.

**Why this priority**: Users frequently make mistakes or change priorities. Maintenance features are essential for a long-lived list.

**Independent Test**: Can be tested by creating a task, updating its title, then deleting it and confirming it no longer appears in the list.

**Acceptance Scenarios**:

1. **Given** task #1 has title "Buy groceries", **When** I update task #1 title to "Order groceries", **Then** the title is updated and a success message is displayed.
2. **Given** task #1 exists, **When** I delete task #1 and confirm with "yes", **Then** task #1 is removed and "No tasks yet" is displayed in the list view.

---

### Edge Cases

- **Empty/Whitespace Title**: If a user tries to add or update a task with an empty or whitespace-only title, the system must reject it with an error message: "Error: Title cannot be empty".
- **Title Length Limit**: Titles exceeding 200 characters must be rejected or truncated with a warning (per F-101 validation rules).
- **Non-existent ID**: If a user attempts to update, delete, or mark a task with an ID that doesn't exist (e.g., #99), the system must show: "Error: Task #99 not found".
- **Invalid ID Input**: If a user enters non-numeric text for a task ID, the system must show: "Error: Invalid task ID. Please enter a number".

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST support adding a task with a mandatory title (1-200 chars) and an optional description (max 1000 chars).
- **FR-002**: System MUST auto-assign a unique, sequential numeric ID to each new task starting from 1.
- **FR-003**: System MUST set the default status of new tasks to "pending".
- **FR-004**: System MUST allow viewing all tasks with their ID, title, and status (✓ for complete, [ ] or ✗ for pending).
- **FR-005**: System MUST allow deleting a task by ID, requiring a confirmation (yes/no) before removal.
- **FR-006**: System MUST allow updating a task's title and/or description while preserving the ID and creation timestamp.
- **FR-007**: System MUST allow toggling a task's status between "pending" and "complete" by ID.
- **FR-008**: System MUST store all data in-memory for the duration of the session (no persistence required for Phase I).

### Key Entities *(include if feature involves data)*

- **Task**: Represents a single item of work.
  - `id`: Unique integer
  - `title`: String (1-200 chars)
  - `description`: String (up to 1000 chars)
  - `completed`: Boolean
  - `created_at`: Datetime

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can add a new task and see it displayed in the main menu summary in under 10 seconds of interaction.
- **SC-002**: System successfully handles 1,000+ tasks in-memory without exceeding 50MB of memory usage.
- **SC-003**: 100% of invalid inputs (empty titles, invalid IDs) are caught and reported with specific error messages without crashing the application.
- **SC-004**: All state changes (add, update, delete, complete) are immediately reflected in the "View All Tasks" list view.
