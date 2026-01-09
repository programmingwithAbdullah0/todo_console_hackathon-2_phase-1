# Internal Logic Contracts: Console Todo App (Phase I)

Since Phase I is a monolithic console application, "contracts" represent the function signatures and data flow rather than HTTP endpoints.

## Task Dictionary Structure
```python
{
    "id": int,
    "title": "str",
    "description": "str",
    "completed": bool,
    "created_at": "str (YYYY-MM-DD HH:MM:SS)"
}
```

## Function Signatures

### Create Task
- **Input**: `title: str`, `description: str`
- **Output**: `Task` dictionary
- **Validation**: Title length 1-200, non-empty.

### Update Task
- **Input**: `task_id: int`, `updates: dict` (keys: title, description)
- **Logic**: Partial updates allowed.
- **Error**: Raise/Return error if ID not found.

### Delete Task
- **Input**: `task_id: int`
- **Confirmation**: Required via CLI input.

### List Tasks
- **Input**: None
- **Output**: `list[Task]`
