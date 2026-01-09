# Data Model: Console Todo App

## Entities

### Task
- **id**: `int` (Primary Key, unique, sequential)
- **title**: `str` (1-200 characters, mandatory)
- **description**: `str` (0-1000 characters, optional)
- **completed**: `bool` (Default: `False`)
- **created_at**: `str` (ISO-8601 format string, generated at creation)

## Validation Rules
- **Title**: Mandatory, must not be whitespace-only, max 200 chars.
- **Description**: Optional, max 1000 chars.
- **ID**: Positive integer, must exist in the current session list for updates/deletes.

## State Transitions
- **Pending -> Completed**: Triggered by `mark_complete()` (toggle).
- **Completed -> Pending**: Triggered by `mark_complete()` (toggle).
- **Exists -> Deleted**: Permanent removal from the in-memory list.
